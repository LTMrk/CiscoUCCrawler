"""
openapi_ingest.py — Ingesta de la referencia de la API de Webex.

FUENTE
------
github.com/webex/webex-openapi-specs, public-spec/, licencia CC BY 4.0.
No es un espejo que va por detrás de developer.webex.com: según Cisco, estos
specs son la fuente de verdad de sus colecciones Postman y forman parte del
pipeline oficial de publicación — cuando añaden endpoints, deprecan otros o
cambian parámetros, los specs se actualizan por el mismo proceso que publica
la documentación. La web y el repo salen del mismo sitio.

SEGUIMIENTO A NIVEL DE OPERACIÓN
--------------------------------
La versión anterior solo guardaba el SHA del fichero: sabía QUE un spec había
cambiado, pero no QUÉ había cambiado. Dos consecuencias malas:

  1. No había forma de enterarse de los endpoints nuevos, que es justo lo que
     hay que vigilar en una API que crece.
  2. Un endpoint RETIRADO dejaba su .md en disco para siempre. El RAG seguía
     respondiendo sobre un endpoint que ya no existe.

Ahora se persiste el conjunto de operaciones (METODO ruta) por spec, se
diffea entre ejecuciones y se emite logs/openapi_deltas.json con added /
removed / deprecated. Los .md de operaciones retiradas se borran (tombstone),
igual que se hace con las páginas rastreadas.
"""

import json
import os
import urllib.error
import urllib.request

from openapi_render import operacion_a_markdown
from state_store import DIR_DOCS, ahora, hash_contenido, iso

API_CONTENIDOS = "https://api.github.com/repos/webex/webex-openapi-specs/contents/public-spec"
RUTA_ESTADO_SPECS = "logs/openapi_state.json"
RUTA_DELTAS_API = "logs/openapi_deltas.json"
DIR_DOCS_API = os.path.join(DIR_DOCS, "openapi")

USER_AGENT = "CiscoUCCrawler/2.0 (+https://github.com/TU-ORG/CiscoUCCrawler)"
METODOS_HTTP = {"get", "post", "put", "delete", "patch", "options", "head"}


def _get_json(url, token=None):
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
    })
    if token:
        # En GitHub Actions, secrets.GITHUB_TOKEN sube el limite de 60 a 5000
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


def _slug(nombre_spec, metodo, ruta):
    base = f"{nombre_spec.rsplit('.', 1)[0]}-{metodo}-{ruta}".lower()
    base = base.replace("/", "-").replace("{", "").replace("}", "")
    base = "".join(c if c.isalnum() or c == "-" else "-" for c in base)[:150]
    return "-".join(filter(None, base.split("-")))


def _parsear_spec(nombre, crudo):
    if nombre.endswith(".json"):
        return json.loads(crudo)
    import yaml  # solo se importa si hay specs YAML
    return yaml.safe_load(crudo)


def _operaciones_de(spec):
    """Genera (clave, ruta, metodo, operacion) con los parámetros de nivel de
    ruta ya heredados en cada operación."""
    for ruta, item in (spec.get("paths") or {}).items():
        if not isinstance(item, dict):
            continue
        params_ruta = item.get("parameters", [])
        for metodo, operacion in item.items():
            if metodo.lower() not in METODOS_HTTP or not isinstance(operacion, dict):
                continue
            if params_ruta:
                operacion = dict(operacion)
                operacion["parameters"] = params_ruta + list(operacion.get("parameters", []))
            yield f"{metodo.upper()} {ruta}", ruta, metodo, operacion


def ingerir_openapi(token=None, forzar=False, specs_permitidos=None):
    """Descarga los specs cambiados, regenera sus documentos y reporta el
    delta a nivel de operación.

    Devuelve (resumen_por_spec, deltas) donde deltas contiene added / removed
    / deprecated como listas de "API: METODO ruta"."""
    os.makedirs(DIR_DOCS_API, exist_ok=True)
    estado = _cargar_estado()
    resumen = {}
    deltas = {"added": [], "removed": [], "deprecated": [], "specs_cambiados": []}

    try:
        ficheros = _get_json(API_CONTENIDOS, token=token)
    except urllib.error.URLError as e:
        return {"_error": f"No se pudo listar public-spec: {e}"}, deltas

    vistos = set()

    for fichero in ficheros:
        nombre = fichero.get("name", "")
        if not nombre.endswith((".json", ".yaml", ".yml")):
            continue
        if specs_permitidos and not any(nombre.startswith(p) for p in specs_permitidos):
            resumen[nombre] = {"estado": "omitido por allowlist"}
            continue

        vistos.add(nombre)
        sha_remoto = fichero.get("sha")
        previo = estado.get(nombre, {})
        ops_previas = previo.get("operaciones", {}) or {}
        deprecadas_previas = previo.get("deprecadas", {}) or {}

        if previo.get("sha") == sha_remoto and not forzar:
            resumen[nombre] = {"estado": "sin cambios", "operaciones": len(ops_previas)}
            continue

        try:
            crudo = _get_texto(fichero["download_url"])
            spec = _parsear_spec(nombre, crudo)
        except urllib.error.URLError as e:
            resumen[nombre] = {"estado": f"error de descarga: {e}"}
            continue
        except Exception as e:
            resumen[nombre] = {"estado": f"error de parseo: {e}"}
            continue

        nombre_api = (spec.get("info") or {}).get("title", nombre)
        version_api = (spec.get("info") or {}).get("version", "")
        ops_actuales = {}
        deprecadas_actuales = {}

        for clave, ruta, metodo, operacion in _operaciones_de(spec):
            markdown, meta = operacion_a_markdown(spec, nombre_api, ruta, metodo, operacion)
            slug = _slug(nombre, metodo, ruta)
            ops_actuales[clave] = slug

            if meta["deprecated"]:
                deprecadas_actuales[clave] = True
                # Solo se reporta la TRANSICION a deprecado, no el estado.
                if not deprecadas_previas.get(clave):
                    deltas["deprecated"].append(f"{nombre_api}: {clave}")

            if clave not in ops_previas:
                deltas["added"].append(f"{nombre_api}: {clave}")

            # Front matter: permite filtrar por metadatos ANTES de la busqueda
            # vectorial, que para preguntas de API es mas preciso que la
            # similitud semantica sola.
            cabecera = (
                "---\n"
                f"doc_id: {slug}\n"
                f"source: webex-openapi-specs/public-spec/{nombre}\n"
                f"api: {nombre_api}\n"
                f"api_version: {version_api}\n"
                f"method: {metodo.upper()}\n"
                f"path: {ruta}\n"
                f"operation_id: {operacion.get('operationId', '')}\n"
                f"tags: {', '.join(operacion.get('tags', []))}\n"
                f"deprecated: {str(meta['deprecated']).lower()}\n"
                f"scopes: {', '.join(meta['scopes'])}\n"
                f"license: CC-BY-4.0\n"
                f"retrieved_at: {iso(ahora())}\n"
                "---\n\n"
            )
            with open(os.path.join(DIR_DOCS_API, f"{slug}.md"), "w", encoding="utf-8") as f:
                f.write(cabecera + markdown)

        # Tombstones: operaciones que estaban y ya no. Sin esto el RAG sigue
        # respondiendo sobre endpoints retirados indefinidamente.
        for clave, slug in ops_previas.items():
            if clave not in ops_actuales:
                deltas["removed"].append(f"{nombre_api}: {clave}")
                ruta_md = os.path.join(DIR_DOCS_API, f"{slug}.md")
                if os.path.exists(ruta_md):
                    os.remove(ruta_md)

        estado[nombre] = {
            "sha": sha_remoto,
            "api": nombre_api,
            "api_version": version_api,
            "operaciones": ops_actuales,
            "deprecadas": deprecadas_actuales,
            "content_sha": hash_contenido(crudo),
            "actualizado": iso(ahora()),
        }
        deltas["specs_cambiados"].append(nombre)
        resumen[nombre] = {
            "estado": "regenerado",
            "operaciones": len(ops_actuales),
            "deprecadas": len(deprecadas_actuales),
        }

    # Un spec que desaparece del repo se limpia entero.
    for nombre in [n for n in list(estado) if n not in vistos]:
        if specs_permitidos and not any(nombre.startswith(p) for p in specs_permitidos):
            continue
        api = estado[nombre].get("api", nombre)
        for clave, slug in (estado[nombre].get("operaciones") or {}).items():
            deltas["removed"].append(f"{api}: {clave}")
            ruta_md = os.path.join(DIR_DOCS_API, f"{slug}.md")
            if os.path.exists(ruta_md):
                os.remove(ruta_md)
        estado.pop(nombre, None)

    _guardar_estado(estado)

    os.makedirs(os.path.dirname(RUTA_DELTAS_API), exist_ok=True)
    with open(RUTA_DELTAS_API, "w", encoding="utf-8") as f:
        json.dump({"run_at": iso(ahora()), **deltas}, f, indent=2, ensure_ascii=False)

    return resumen, deltas


if __name__ == "__main__":
    import sys
    res, dl = ingerir_openapi(
        token=os.environ.get("GITHUB_TOKEN"),
        forzar="--forzar" in sys.argv,
    )
    for k, v in sorted(res.items()):
        print(f"{k}: {v}")
    print(f"\nNuevos: {len(dl['added'])} | Retirados: {len(dl['removed'])} "
          f"| Deprecados: {len(dl['deprecated'])}")
    for clave in dl["added"][:20]:
        print(f"  + {clave}")
    for clave in dl["removed"][:20]:
        print(f"  - {clave}")
    for clave in dl["deprecated"][:20]:
        print(f"  ! {clave}")
