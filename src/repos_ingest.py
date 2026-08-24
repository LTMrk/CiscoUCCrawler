"""
repos_ingest.py — Ingesta de documentacion en Markdown de repositorios GitHub.

QUE APORTA QUE NO APORTE EL CRAWLER
-----------------------------------
El crawler recorre documentacion de producto: como configurar, como
diagnosticar. Los repos de github.com/webex aportan la otra mitad, la de
integracion: como se autentica un SDK, que devuelve cada widget, como se monta
una Embedded App. Son preguntas reales de soporte que el arbol de cisco.com no
responde porque viven en developer.webex.com, que es una SPA no rastreable
(ver `degraded_seeds` en config.json).

POR QUE UNA LISTA CURADA Y NO LA ORGANIZACION ENTERA
----------------------------------------------------
La organizacion tiene 68 repos y meterlos todos empeoraria el RAG:

  - Varios estan deprecados por su propio README (`spark-ios-sdk` dice
    "DEPRECATE. Check our newer iOS SDK", `spark-android-sdk` dice "This repo
    is DEPRECATED"). Es el mismo criterio que retiro Webex Experience
    Management de las semillas: documentacion de algo retirado no es contenido
    neutro, produce respuestas activamente incorrectas.
  - Otros son fontaneria de bajo nivel (`webrtc-core`, `ts-sdp`,
    `web-capabilities`) o guias de estilo internas (`web-styleguide`): no
    responden a ninguna pregunta de un agente de colaboracion y compiten en el
    espacio vectorial.

La lista vive en config.json (`repos_allowlist`) para poder ajustarla sin
tocar codigo.

QUE FICHEROS SE INGIEREN
------------------------
Solo Markdown, y no todo: se descartan CHANGELOG, LICENSE, CONTRIBUTING y
similares, que son ruido documental puro y ademas casi identicos entre repos,
justo el tipo de bloque repetido que el sanitizador persigue en las paginas
web. Se descarta tambien lo que cuelga de node_modules o de directorios de
test.
"""

import json
import os
import time
import urllib.error
import urllib.request
from urllib.parse import quote

from state_store import DIR_DOCS, ahora, hash_contenido, iso

RUTA_ESTADO_REPOS = "logs/repos_state.json"
RUTA_DELTAS_REPOS = "logs/repos_deltas.json"
# DIR_DOCS ya vale "docs/pages" (definido en state_store.py). Un
# os.path.join(DIR_DOCS, "repos") aqui anidaria los documentos de repos DENTRO
# de pages/, mezclandolos con las paginas web rastreadas. Se calcula como
# directorio HERMANO de pages/ para mantenerlos separados.
DIR_DOCS_REPOS = os.path.join(os.path.dirname(DIR_DOCS), "repos")

USER_AGENT = "CiscoUCCrawler/3.0 (documentation indexing for internal RAG)"

# Tamano maximo por fichero. Un .md de 300 KB en un repo de codigo casi siempre
# es un volcado generado (referencia de API autogenerada, listado de simbolos),
# no prosa util.
MAX_BYTES_FICHERO = 300_000

# Suelo minimo. Un monorepo como webex-js-sdk tiene un README por paquete y
# muchos son un titulo y una linea ("# @webex/plugin-foo"). Como chunk no
# responden a nada, pero si compiten en similitud con la documentacion real:
# son cortos, asi que cualquier consulta que mencione el nombre del paquete los
# puntua alto. 400 bytes es aproximadamente un titulo mas un parrafo.
MIN_BYTES_FICHERO = 400

# Ficheros de gobernanza del repo: iguales en todos los repos y sin contenido
# tecnico. Si entran, el detector de boilerplate los veria repetidos, pero para
# entonces ya habrian gastado presupuesto de crawl y espacio de indice.
NOMBRES_EXCLUIDOS = {
    "changelog.md", "changelog-old.md", "license.md", "licence.md",
    "contributing.md", "code_of_conduct.md", "codeofconduct.md",
    "security.md", "support.md", "authors.md", "maintainers.md",
    "pull_request_template.md", "issue_template.md", "notice.md",
}

# Directorios sin valor documental o con contenido generado.
FRAGMENTOS_RUTA_EXCLUIDOS = (
    "node_modules/", "/test/", "/tests/", "__tests__/", "/fixtures/",
    "/.github/", "/coverage/", "/dist/", "/build/", "/vendor/",
    "/examples/generated/",
)


class LimiteApiAgotado(RuntimeError):
    """La API de GitHub ha devuelto 403 por agotamiento de cuota."""


# Reintentos ante fallo transitorio del servidor. El arbol recursivo de un
# monorepo como webex-js-sdk hace trabajar bastante a la API y devuelve 504 con
# cierta frecuencia; sin reintento, ese repositorio se pierde entero en cada
# ejecucion y el corpus queda con un hueco permanente que nadie nota.
INTENTOS = 3
ESPERA_BASE = 3  # segundos, con retroceso lineal


def _get_json(url, token=None):
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
    })
    if token:
        # En GitHub Actions, secrets.GITHUB_TOKEN sube el limite de 60 a 5000
        # peticiones/hora. Con 29 repos son ~58 peticiones solo de metadatos y
        # arboles: sin token se agota la cuota a mitad de la ingesta.
        req.add_header("Authorization", f"Bearer {token}")

    ultimo = None
    for intento in range(1, INTENTOS + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as err:
            # Un 403 por cuota y un 403 por permisos se parecen en el codigo
            # pero exigen acciones opuestas: esperar frente a revisar el token.
            # Sin distinguirlos, la ingesta parece "repos que no existen".
            if err.code == 403 and err.headers.get("X-RateLimit-Remaining") == "0":
                reset = err.headers.get("X-RateLimit-Reset", "?")
                raise LimiteApiAgotado(
                    f"cuota de la API agotada (reintentar tras {reset}). "
                    f"{'Pasa un token para subir el limite de 60 a 5000/hora.' if not token else ''}"
                ) from err
            # 4xx es un problema nuestro (no existe, sin permiso): reintentar
            # no lo arregla y solo gasta cuota.
            if err.code < 500 or intento == INTENTOS:
                raise
            ultimo = err
        except (urllib.error.URLError, TimeoutError) as err:
            if intento == INTENTOS:
                raise
            ultimo = err
        print(f"    reintento {intento}/{INTENTOS} tras {ultimo}", flush=True)
        time.sleep(ESPERA_BASE * intento)
    raise ultimo  # inalcanzable, pero deja explicito que aqui no se cae en None


def _get_texto(url, token=None):
    cabeceras = {"User-Agent": USER_AGENT}
    if token:
        cabeceras["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=cabeceras)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _cargar_estado():
    if not os.path.exists(RUTA_ESTADO_REPOS):
        return {"version": 1, "repos": {}}
    try:
        with open(RUTA_ESTADO_REPOS, "r", encoding="utf-8") as fh:
            estado = json.load(fh)
    except (json.JSONDecodeError, OSError):
        return {"version": 1, "repos": {}}
    estado.setdefault("repos", {})
    return estado


def _guardar_estado(estado):
    os.makedirs(os.path.dirname(RUTA_ESTADO_REPOS), exist_ok=True)
    with open(RUTA_ESTADO_REPOS, "w", encoding="utf-8") as fh:
        json.dump(estado, fh, indent=1, ensure_ascii=False)


def _url_cruda(repo, rama, ruta):
    """URL de descarga del fichero, con la ruta codificada.

    No es cosmetico: en webex-js-sdk hay ficheros con espacio en el nombre
    ("packages/calling/usm sdk flow.md") y urllib rechaza la peticion entera
    con InvalidURL, tumbando la ingesta del repositorio completo.
    """
    return f"https://raw.githubusercontent.com/{repo}/{rama}/{quote(ruta)}"


def _url_navegable(repo, rama, ruta):
    """URL del fichero en la web de GitHub, para citar como fuente."""
    return f"https://github.com/{repo}/blob/{rama}/{quote(ruta)}"


def _slug(repo, ruta):
    """Identificador estable y legible del documento."""
    base = f"{repo}-{ruta}".lower()
    limpio = "".join(c if c.isalnum() else "-" for c in base)
    while "--" in limpio:
        limpio = limpio.replace("--", "-")
    return limpio.strip("-")[:150]


def _es_ingerible(ruta, tamano):
    if not ruta.lower().endswith(".md"):
        return False
    if os.path.basename(ruta).lower() in NOMBRES_EXCLUIDOS:
        return False
    marcada = "/" + ruta.lower()
    if any(f in marcada for f in FRAGMENTOS_RUTA_EXCLUIDOS):
        return False
    return MIN_BYTES_FICHERO <= tamano <= MAX_BYTES_FICHERO


def _documento(meta_repo, ruta, texto):
    """Envuelve el markdown con el mismo frontmatter que usa el resto del
    corpus, para que copilot_pack y el consumidor RAG no distingan el origen."""
    repo = meta_repo["full_name"]
    rama = meta_repo["default_branch"]
    url = _url_navegable(repo, rama, ruta)
    licencia = (meta_repo.get("license") or {}).get("spdx_id") or "sin declarar"
    cabecera = [
        "---",
        f"doc_id: {_slug(repo, ruta)}",
        f"source_url: {url}",
        f"repo: {repo}",
        f"ruta: {ruta}",
        f"licencia: {licencia}",
        f"retrieved_at: {iso(ahora())}",
        "---",
        "",
        f"# {meta_repo['name']} — {ruta}",
        "",
        f"Repositorio: {repo}",
    ]
    if meta_repo.get("description"):
        cabecera.append(f"Descripcion del repositorio: {meta_repo['description']}")
    cabecera += ["", texto.strip(), "",
                 "---",
                 f"> Fuente: {url} (licencia {licencia})"]
    return "\n".join(cabecera) + "\n"


def _ficheros_del_repo(repo, token):
    """Devuelve (metadatos, [(ruta, sha, tamano)]) o (None, []) si no procede."""
    try:
        meta = _get_json(f"https://api.github.com/repos/{repo}", token)
    except urllib.error.HTTPError as err:
        print(f"  {repo}: HTTP {err.code} al leer metadatos. Se omite.", flush=True)
        return None, []

    if meta.get("archived"):
        # Un repo archivado no recibe correcciones. Mismo criterio que con los
        # productos en EoL: mejor no responder que responder desactualizado.
        print(f"  {repo}: archivado en origen. Se omite.", flush=True)
        return None, []

    rama = meta.get("default_branch", "main")
    try:
        arbol = _get_json(
            f"https://api.github.com/repos/{repo}/git/trees/{rama}?recursive=1",
            token)
    except urllib.error.HTTPError as err:
        print(f"  {repo}: HTTP {err.code} al leer el arbol. Se omite.", flush=True)
        return None, []

    if arbol.get("truncated"):
        print(f"  {repo}: arbol truncado por la API; se ingiere lo recibido.",
              flush=True)

    ficheros = [
        (n["path"], n["sha"], n.get("size", 0))
        for n in arbol.get("tree", [])
        if n.get("type") == "blob" and _es_ingerible(n["path"], n.get("size", 0))
    ]
    return meta, ficheros


def ingerir_repos(token=None, repos_permitidos=None, forzar=False):
    """Sincroniza el Markdown de los repos permitidos contra docs/repos/.

    Devuelve (resumen, deltas). Igual que openapi_ingest, emite tombstones: un
    fichero que desaparece del repo se borra del corpus, para que el RAG no
    siga citando documentacion retirada.
    """
    if not repos_permitidos:
        print("repos_allowlist vacia: no se ingiere ningun repositorio.",
              flush=True)
        return {"repos": 0, "documentos": 0}, {"added": [], "modified": [],
                                               "removed": []}

    os.makedirs(DIR_DOCS_REPOS, exist_ok=True)
    estado = _cargar_estado()
    previos = estado.get("repos", {})
    nuevos_estado = {}
    deltas = {"added": [], "modified": [], "removed": []}
    total_docs = 0

    for repo in repos_permitidos:
        print(f"repos: {repo}", flush=True)
        try:
            meta, ficheros = _ficheros_del_repo(repo, token)
        except LimiteApiAgotado as e:
            # Se aborta el bucle, no solo este repo: sin cuota los siguientes
            # fallarian igual y dejarian el estado a medias. Lo ya escrito se
            # conserva y el resto se recupera en la siguiente ejecucion.
            print(f"repos: {e} Se detiene la ingesta y se conserva lo hecho.",
                  flush=True)
            for pendiente in repos_permitidos[repos_permitidos.index(repo):]:
                if pendiente in previos:
                    nuevos_estado[pendiente] = previos[pendiente]
            break
        if meta is None:
            # Se conserva el estado anterior: un fallo transitorio de la API no
            # debe provocar el borrado masivo de sus documentos.
            if repo in previos:
                nuevos_estado[repo] = previos[repo]
            continue

        antes = previos.get(repo, {}).get("ficheros", {})
        ahora_ficheros = {}

        for ruta, sha, _tam in ficheros:
            ahora_ficheros[ruta] = sha
            if not forzar and antes.get(ruta) == sha:
                total_docs += 1
                continue
            crudo = _url_cruda(repo, meta["default_branch"], ruta)
            try:
                texto = _get_texto(crudo, token)
            except urllib.error.HTTPError as err:
                print(f"    {ruta}: HTTP {err.code}. Se omite.", flush=True)
                ahora_ficheros.pop(ruta, None)
                continue
            destino = os.path.join(DIR_DOCS_REPOS, _slug(repo, ruta) + ".md")
            with open(destino, "w", encoding="utf-8") as fh:
                fh.write(_documento(meta, ruta, texto))
            deltas["modified" if ruta in antes else "added"].append(f"{repo}/{ruta}")
            total_docs += 1

        # Tombstones: lo que estaba y ya no esta.
        for ruta in set(antes) - set(ahora_ficheros):
            destino = os.path.join(DIR_DOCS_REPOS, _slug(repo, ruta) + ".md")
            if os.path.exists(destino):
                os.remove(destino)
            deltas["removed"].append(f"{repo}/{ruta}")

        nuevos_estado[repo] = {
            "ficheros": ahora_ficheros,
            "default_branch": meta["default_branch"],
            "descripcion": meta.get("description") or "",
            "estrellas": meta.get("stargazers_count", 0),
            "actualizado": iso(ahora()),
        }

    # Un repo retirado de la allowlist tambien deja tombstones.
    for repo in set(previos) - set(nuevos_estado):
        for ruta in previos[repo].get("ficheros", {}):
            destino = os.path.join(DIR_DOCS_REPOS, _slug(repo, ruta) + ".md")
            if os.path.exists(destino):
                os.remove(destino)
            deltas["removed"].append(f"{repo}/{ruta}")

    estado["repos"] = nuevos_estado
    _guardar_estado(estado)
    os.makedirs(os.path.dirname(RUTA_DELTAS_REPOS), exist_ok=True)
    with open(RUTA_DELTAS_REPOS, "w", encoding="utf-8") as fh:
        json.dump(deltas, fh, indent=1, ensure_ascii=False)

    resumen = {"repos": len(nuevos_estado), "documentos": total_docs}
    print(f"repos: {resumen['repos']} repositorios, {resumen['documentos']} "
          f"documentos (+{len(deltas['added'])} ~{len(deltas['modified'])} "
          f"-{len(deltas['removed'])}).", flush=True)
    return resumen, deltas
