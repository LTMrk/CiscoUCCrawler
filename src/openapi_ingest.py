"""
openapi_ingest.py — Ingesta de la referencia de la API de Webex desde la
fuente estructurada oficial, sin scraping.

POR QUÉ ESTE MÓDULO SUSTITUYE AL SCRAPING DE developer.webex.com
-----------------------------------------------------------------
Cisco publica los OpenAPI de la suite Webex en github.com/webex/webex-openapi-specs
bajo licencia CC BY 4.0 (redistribución y adaptación permitidas, incluso
comerciales, con atribución). El directorio public-spec/ contiene, entre otros:
webex-admin, webex-broadworks, webex-cloud-calling, webex-contact-center,
webex-device, webex-meeting, webex-messaging, webex-ucm y webex-wholesale.

Ventajas frente a rascar el estado hidratado de la SPA:
  - No hay WAF: raw.githubusercontent.com no aplica Akamai Bot Manager.
  - No hay HTML que sanitizar ni ruido vectorial que podar.
  - Los datos son completos: esquemas de request/response, parámetros y
    códigos de error, que el HTML renderizado solo muestra parcialmente.
  - El delta es gratis: la API de GitHub devuelve el SHA de cada blob, así que
    detectar cambios cuesta UNA petición para todo el corpus de la API.

GRANULARIDAD DE CHUNKING
------------------------
Se emite un documento Markdown POR OPERACIÓN (método + ruta), no por fichero
de spec. Un spec completo son cientos de miles de tokens; una operación es
una unidad semántica autocontenida — que es exactamente lo que debe recuperar
el agente cuando alguien pregunta "cómo creo una knowledge base".
"""

import json
import os
import urllib.error
import urllib.request

from state_store import DIR_DOCS, hash_contenido, iso, ahora

API_CONTENIDOS = "https://api.github.com/repos/webex/webex-openapi-specs/contents/public-spec"
RUTA_ESTADO_SPECS = "logs/openapi_state.json"
DIR_DOCS_API = os.path.join(DIR_DOCS, "openapi")

ATRIBUCION = (
    "> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.\n"
    "> https://github.com/webex/webex-openapi-specs\n"
)

USER_AGENT = "CiscoUCCrawler/2.0 (+https://github.com/TU-ORG/CiscoUCCrawler)"


def _get_json(url, token=None):
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
    })
    if token:
        # En GitHub Actions, secrets.GITHUB_TOKEN sube el límite de 60 a 5000
        # peticiones/hora. No es obligatorio para este volumen.
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _get_texto(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read().decode("utf-8")


def _cargar_estado():
    if os.path.exists(RUTA_ESTADO_SPECS):
        try:
            with open(RUTA_ESTADO_SPECS, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def _guardar_estado(estado):
    os.makedirs(os.path.dirname(RUTA_ESTADO_SPECS), exist_ok=True)
    with open(RUTA_ESTADO_SPECS, "w", encoding="utf-8") as f:
        json.dump(estado, f, indent=2, sort_keys=True)


# ---------------------------------------------------------------------------
# Resolución de $ref y renderizado
# ---------------------------------------------------------------------------

def _resolver_ref(spec, ref, profundidad=0):
    """Resuelve un $ref local (#/components/...). Corta a profundidad 6 para
    no colgarse en esquemas recursivos, comunes en definiciones grandes."""
    if profundidad > 6 or not ref.startswith("#/"):
        return {}
    nodo = spec
    for parte in ref[2:].split("/"):
        if not isinstance(nodo, dict) or parte not in nodo:
            return {}
        nodo = nodo[parte]
    return nodo


def _describir_schema(spec, schema, profundidad=0, visitados=None):
    """Aplana un esquema JSON a líneas legibles. El objetivo no es
    reconstruir el JSON Schema, sino producir texto que se embeba bien:
    nombre de campo, tipo, si es obligatorio y su descripción."""
    if visitados is None:
        visitados = set()
    if not isinstance(schema, dict) or profundidad > 4:
        return []

    if "$ref" in schema:
        ref = schema["$ref"]
        if ref in visitados:
            return [f"{'  ' * profundidad}- (referencia circular a {ref.split('/')[-1]})"]
        visitados = visitados | {ref}
        schema = _resolver_ref(spec, ref)

    lineas = []
    if schema.get("type") == "array" and "items" in schema:
        lineas.append(f"{'  ' * profundidad}- (array de:)")
        lineas += _describir_schema(spec, schema["items"], profundidad + 1, visitados)
        return lineas

    obligatorios = set(schema.get("required", []))
    for nombre, prop in (schema.get("properties") or {}).items():
        if "$ref" in prop:
            prop_res = _resolver_ref(spec, prop["$ref"])
        else:
            prop_res = prop
        tipo = prop_res.get("type", "object")
        req = " **(requerido)**" if nombre in obligatorios else ""
        desc = (prop_res.get("description") or "").strip().replace("\n", " ")
        enum = prop_res.get("enum")
        extra = f" Valores: {', '.join(map(str, enum))}." if enum else ""
        lineas.append(f"{'  ' * profundidad}- `{nombre}` ({tipo}){req}: {desc}{extra}".rstrip())

        if prop_res.get("type") == "object" or "properties" in prop_res:
            lineas += _describir_schema(spec, prop_res, profundidad + 1, visitados)
        elif prop_res.get("type") == "array" and "items" in prop_res:
            lineas += _describir_schema(spec, prop_res["items"], profundidad + 1, visitados)

    return lineas


def operacion_a_markdown(spec, nombre_api, ruta, metodo, operacion):
    """Genera un documento autocontenido para una única operación."""
    resumen = operacion.get("summary") or operacion.get("operationId") or ""
    descripcion = (operacion.get("description") or "").strip()
    op_id = operacion.get("operationId", "")
    tags = ", ".join(operacion.get("tags", []))
    servidores = spec.get("servers") or []
    base = servidores[0].get("url", "") if servidores else ""

    partes = [
        f"# {metodo.upper()} {ruta}",
        "",
        f"**API:** {nombre_api}",
    ]
    if tags:
        partes.append(f"**Área:** {tags}")
    if op_id:
        partes.append(f"**operationId:** `{op_id}`")
    if base:
        partes.append(f"**URL base:** `{base}`")
    if resumen:
        partes += ["", f"## Resumen", resumen]
    if descripcion:
        partes += ["", "## Descripción", descripcion]

    # Parámetros (los de nivel de ruta se heredan en la operación).
    parametros = list(operacion.get("parameters") or [])
    if parametros:
        partes += ["", "## Parámetros"]
        for p in parametros:
            if "$ref" in p:
                p = _resolver_ref(spec, p["$ref"])
            nombre = p.get("name", "?")
            sitio = p.get("in", "?")
            req = " **(requerido)**" if p.get("required") else ""
            tipo = (p.get("schema") or {}).get("type", "")
            desc = (p.get("description") or "").strip().replace("\n", " ")
            partes.append(f"- `{nombre}` [{sitio}] ({tipo}){req}: {desc}".rstrip())

    # Cuerpo de la petición.
    body = operacion.get("requestBody")
    if body:
        if "$ref" in body:
            body = _resolver_ref(spec, body["$ref"])
        contenido = (body.get("content") or {})
        for tipo_mime, definicion in contenido.items():
            esquema = definicion.get("schema") or {}
            lineas = _describir_schema(spec, esquema)
            if lineas:
                partes += ["", f"## Cuerpo de la petición ({tipo_mime})"] + lineas
            ejemplo = definicion.get("example")
            if ejemplo is not None:
                partes += ["", "### Ejemplo de petición", "```json",
                           json.dumps(ejemplo, indent=2, ensure_ascii=False), "```"]

    # Respuestas.
    respuestas = operacion.get("responses") or {}
    if respuestas:
        partes += ["", "## Respuestas"]
        for codigo, definicion in sorted(respuestas.items(), key=lambda kv: str(kv[0])):
            if "$ref" in definicion:
                definicion = _resolver_ref(spec, definicion["$ref"])
            desc = (definicion.get("description") or "").strip().replace("\n", " ")
            partes.append(f"- **{codigo}**: {desc}")
            if str(codigo).startswith("2"):
                for _mime, d in (definicion.get("content") or {}).items():
                    lineas = _describir_schema(spec, d.get("schema") or {})
                    partes += [f"  {l}" for l in lineas[:40]]

    # Seguridad.
    seguridad = operacion.get("security", spec.get("security"))
    if seguridad:
        esquemas = []
        for s in seguridad:
            esquemas.extend(s.keys())
        if esquemas:
            partes += ["", f"**Autenticación:** {', '.join(sorted(set(esquemas)))}"]

    partes += ["", "---", ATRIBUCION]
    return "\n".join(partes)


# ---------------------------------------------------------------------------
# Orquestación
# ---------------------------------------------------------------------------

def ingerir_openapi(token=None, forzar=False, specs_permitidos=None):
    """Descarga los specs cambiados y regenera sus documentos.

    specs_permitidos: lista de prefijos de nombre de fichero. None o vacía
    ingiere todos. Filtrar importa para la calidad del retrieval: cada spec
    fuera del ámbito del agente aporta cientos de operaciones que compiten en
    el espacio vectorial sin poder responder nunca a una consulta real.

    Devuelve un resumen {api: {estado, operaciones}} apto para logging.
    El delta se calcula con el SHA de blob que devuelve la API de GitHub:
    si el SHA no cambió, el fichero es idéntico y se salta la descarga."""
    os.makedirs(DIR_DOCS_API, exist_ok=True)
    estado = {} if forzar else _cargar_estado()
    resumen = {}

    try:
        ficheros = _get_json(API_CONTENIDOS, token=token)
    except urllib.error.URLError as e:
        return {"_error": f"No se pudo listar public-spec: {e}"}

    for fichero in ficheros:
        nombre = fichero.get("name", "")
        if not nombre.endswith((".json", ".yaml", ".yml")):
            continue
        if specs_permitidos and not any(nombre.startswith(p) for p in specs_permitidos):
            resumen[nombre] = {"estado": "omitido por allowlist", "operaciones": 0}
            continue

        sha_remoto = fichero.get("sha")
        previo = estado.get(nombre, {})
        if previo.get("sha") == sha_remoto and not forzar:
            resumen[nombre] = {"estado": "sin cambios", "operaciones": previo.get("operaciones", 0)}
            continue

        try:
            crudo = _get_texto(fichero["download_url"])
        except urllib.error.URLError as e:
            resumen[nombre] = {"estado": f"error de descarga: {e}"}
            continue

        try:
            if nombre.endswith(".json"):
                spec = json.loads(crudo)
            else:
                import yaml  # solo se importa si hay specs YAML
                spec = yaml.safe_load(crudo)
        except Exception as e:
            resumen[nombre] = {"estado": f"error de parseo: {e}"}
            continue

        nombre_api = (spec.get("info") or {}).get("title", nombre)
        metodos = {"get", "post", "put", "delete", "patch", "options", "head"}
        n_ops = 0

        for ruta, item in (spec.get("paths") or {}).items():
            if not isinstance(item, dict):
                continue
            params_ruta = item.get("parameters", [])
            for metodo, operacion in item.items():
                if metodo.lower() not in metodos or not isinstance(operacion, dict):
                    continue
                # Los parámetros de nivel de ruta aplican a todas sus operaciones.
                if params_ruta:
                    operacion = dict(operacion)
                    operacion["parameters"] = params_ruta + list(operacion.get("parameters", []))

                markdown = operacion_a_markdown(spec, nombre_api, ruta, metodo, operacion)
                slug = (f"{nombre.rsplit('.', 1)[0]}-{metodo}-{ruta}"
                        .lower().replace("/", "-").replace("{", "").replace("}", ""))
                slug = "".join(c if c.isalnum() or c == "-" else "-" for c in slug)[:150]
                slug = "-".join(filter(None, slug.split("-")))

                destino = os.path.join(DIR_DOCS_API, f"{slug}.md")
                cabecera = (
                    "---\n"
                    f"doc_id: {slug}\n"
                    f"source: webex-openapi-specs/public-spec/{nombre}\n"
                    f"api: {nombre_api}\n"
                    f"method: {metodo.upper()}\n"
                    f"path: {ruta}\n"
                    f"license: CC-BY-4.0\n"
                    f"retrieved_at: {iso(ahora())}\n"
                    "---\n\n"
                )
                with open(destino, "w", encoding="utf-8") as f:
                    f.write(cabecera + markdown)
                n_ops += 1

        estado[nombre] = {
            "sha": sha_remoto,
            "operaciones": n_ops,
            "content_sha": hash_contenido(crudo),
            "actualizado": iso(ahora()),
        }
        resumen[nombre] = {"estado": "regenerado", "operaciones": n_ops}

    _guardar_estado(estado)
    return resumen


if __name__ == "__main__":
    import sys
    tok = os.environ.get("GITHUB_TOKEN")
    res = ingerir_openapi(token=tok, forzar="--forzar" in sys.argv)
    for k, v in sorted(res.items()):
        print(f"{k}: {v}")
      
