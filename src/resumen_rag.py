"""
resumen_rag.py — Inventario en Markdown del conocimiento que contiene el RAG.

PARA QUE SIRVE
--------------
Responde a la pregunta que no responde ningun log: "que sabe ahora mismo este
RAG". Los deltas dicen que cambio en el ultimo lote; el manifiesto es una
estructura de maquina. Aqui se emite un documento legible con la cobertura por
producto, las versiones presentes, las APIs indexadas y lo que queda por
rastrear.

Sirve para dos cosas distintas:

  - Auditar la cobertura antes de prometerle algo a un agente. Si alguien
    pregunta "puede el agente resolver dudas de CUCM 15", la respuesta esta en
    la tabla de versiones, no en una suposicion.
  - Detectar regresiones de rastreo. Si un producto baja de 400 a 40
    documentos entre ejecuciones, algo se rompio en la allowlist o en el WAF, y
    el diff de este fichero en git lo hace evidente sin abrir un solo log.

Se regenera en cada ejecucion del ETL, antes del commit, para que quede
versionado junto a los documentos que describe.
"""

import collections
import json
import os
import re

from copilot_pack import (
    ETIQUETAS, clasificar_producto, clave_version, etiqueta_version,
    familia_documental,
)

DIR_PAGINAS = os.path.join("docs", "pages")
DIR_API = os.path.join(DIR_PAGINAS, "openapi")
DIR_REPOS = os.path.join("docs", "repos")
RUTA_SALIDA = "RESUMEN-CONOCIMIENTO.md"
RUTA_FRONTERA = os.path.join("logs", "frontier.json")

FRONTMATTER = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)


def _frontmatter(ruta):
    try:
        with open(ruta, "r", encoding="utf-8", errors="replace") as fh:
            cabecera = fh.read(4096)
    except OSError:
        return {}
    encontrado = FRONTMATTER.match(cabecera)
    if not encontrado:
        return {}
    meta = {}
    for linea in encontrado.group(1).splitlines():
        if ":" in linea:
            clave, valor = linea.split(":", 1)
            meta[clave.strip()] = valor.strip()
    return meta


def _recorrer(directorio, recursivo=False):
    if not os.path.isdir(directorio):
        return
    if recursivo:
        for raiz, _, ficheros in os.walk(directorio):
            for fichero in ficheros:
                if fichero.endswith(".md"):
                    yield os.path.join(raiz, fichero)
    else:
        for fichero in os.listdir(directorio):
            if fichero.endswith(".md"):
                yield os.path.join(directorio, fichero)


def _miles(n):
    return f"{n:,}".replace(",", ".")


def recopilar():
    """Recorre el corpus y devuelve la estadistica por producto, API y repo."""
    productos = collections.defaultdict(
        lambda: {"docs": 0, "chars": 0, "versiones": collections.Counter(),
                 "familias": set()})
    apis = collections.defaultdict(lambda: {"ops": 0, "chars": 0})
    repos = collections.defaultdict(lambda: {"docs": 0, "chars": 0, "desc": ""})

    for ruta in _recorrer(DIR_PAGINAS):
        meta = _frontmatter(ruta)
        url = meta.get("source_url", "")
        if not url:
            continue
        clave = clasificar_producto(url)
        entrada = productos[clave]
        entrada["docs"] += 1
        entrada["chars"] += os.path.getsize(ruta)
        entrada["familias"].add(familia_documental(url))
        version = etiqueta_version(url)
        if version:
            entrada["versiones"][version] += 1

    for ruta in _recorrer(DIR_API):
        meta = _frontmatter(ruta)
        nombre = meta.get("api", "Webex")
        apis[nombre]["ops"] += 1
        apis[nombre]["chars"] += os.path.getsize(ruta)

    for ruta in _recorrer(DIR_REPOS, recursivo=True):
        meta = _frontmatter(ruta)
        nombre = meta.get("repo", "desconocido")
        repos[nombre]["docs"] += 1
        repos[nombre]["chars"] += os.path.getsize(ruta)

    return productos, apis, repos


def _pendientes():
    try:
        with open(RUTA_FRONTERA, "r", encoding="utf-8") as fh:
            return len(json.load(fh))
    except (OSError, json.JSONDecodeError, TypeError):
        return 0


def _tabla_productos(productos):
    lineas = ["| Producto | Documentos | Guías distintas | Versiones | M caracteres |",
              "|---|---:|---:|---|---:|"]
    orden = sorted(productos.items(), key=lambda kv: -kv[1]["chars"])
    for clave, datos in orden:
        # Las tres versiones con mas documentos: da la foto real de a que
        # release responde el agente sin volcar la lista entera.
        top = datos["versiones"].most_common(3)
        versiones = ", ".join(f"{v} ({_miles(n)})" for v, n in top) or "—"
        lineas.append(
            f"| {ETIQUETAS.get(clave, clave)} | {_miles(datos['docs'])} | "
            f"{_miles(len(datos['familias']))} | {versiones} | "
            f"{datos['chars'] / 1e6:.1f} |")
    return lineas


def generar(ruta_salida=RUTA_SALIDA, fecha=None):
    productos, apis, repos = recopilar()
    total_docs = sum(d["docs"] for d in productos.values())
    total_chars = sum(d["chars"] for d in productos.values())
    total_ops = sum(a["ops"] for a in apis.values())
    total_repos_docs = sum(r["docs"] for r in repos.values())
    pendientes = _pendientes()

    sello = fecha or __import__("datetime").datetime.now(
        __import__("datetime").timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lineas = [
        "# Conocimiento indexado por CiscoUCCrawler",
        "",
        "Inventario de lo que contiene el corpus RAG. Lo regenera "
        "`src/resumen_rag.py` en cada ejecución del ETL: **no editar a mano**.",
        "",
        f"Actualizado: {sello}",
        "",
        "## Totales",
        "",
        "| Concepto | Valor |",
        "|---|---:|",
        f"| Documentación de producto | {_miles(total_docs)} documentos |",
        f"| Operaciones de API (OpenAPI) | {_miles(total_ops)} |",
        f"| Documentación de repositorios | {_miles(total_repos_docs)} documentos |",
        f"| Volumen total | {(total_chars + sum(a['chars'] for a in apis.values()) + sum(r['chars'] for r in repos.values())) / 1e6:.1f} M caracteres |",
        f"| URLs pendientes de rastrear | {_miles(pendientes)} |",
        "",
    ]

    if pendientes:
        lineas += [
            f"> El rastreo **no ha terminado**: quedan {_miles(pendientes)} URLs "
            f"en la frontera. Las cifras de abajo son cobertura parcial y "
            f"crecerán en las siguientes ejecuciones.",
            "",
        ]

    lineas += ["## Cobertura por producto", ""]
    lineas += _tabla_productos(productos)
    lineas += [
        "",
        "La columna *Guías distintas* cuenta familias documentales, es decir "
        "guías únicas ignorando la versión. Un número muy inferior al de "
        "documentos indica que el corpus tiene varias releases de la misma "
        "guía.",
        "",
    ]

    if apis:
        lineas += ["## APIs REST de Webex", "",
                   "| API | Operaciones | M caracteres |", "|---|---:|---:|"]
        for nombre, datos in sorted(apis.items(), key=lambda kv: -kv[1]["ops"]):
            lineas.append(f"| {nombre} | {_miles(datos['ops'])} | "
                          f"{datos['chars'] / 1e6:.2f} |")
        lineas.append("")

    if repos:
        lineas += ["## Documentación de repositorios GitHub", "",
                   "| Repositorio | Documentos | M caracteres |", "|---|---:|---:|"]
        for nombre, datos in sorted(repos.items(), key=lambda kv: -kv[1]["docs"]):
            lineas.append(f"| `{nombre}` | {_miles(datos['docs'])} | "
                          f"{datos['chars'] / 1e6:.2f} |")
        lineas.append("")
    else:
        lineas += ["## Documentación de repositorios GitHub", "",
                   "Sin ingerir todavía. Se puebla con `repos_allowlist` de "
                   "`config.json`.", ""]

    lineas += [
        "## Qué NO está cubierto",
        "",
        "Decisiones deliberadas, documentadas en `config.json`:",
        "",
        "- **developer.webex.com**: la referencia de API se obtiene de los "
        "OpenAPI oficiales en su lugar (`webex-openapi-specs`), que es el "
        "mismo origen del que se publica ese portal.",
        "- **De developer.cisco.com, todo lo que no es colaboración**: Meraki, "
        "DNA Center, SD-WAN, NSO, Crosswork, XDR, Spaces, UCS/HyperFlex y "
        "PSIRT quedan fuera por allowlist. También `/codeexchange/`, que "
        "duplica la ingesta de repositorios de GitHub, y `/web/`, que el "
        "`robots.txt` del sitio prohíbe.",
        "- **Productos en EoL** (Webex Experience Management) y **repos "
        "deprecados** (`spark-ios-sdk`, `spark-android-sdk`): documentar algo "
        "retirado produce respuestas activamente incorrectas.",
        "- **Guías de usuario final** y páginas de marketing: son ruido "
        "vectorial que compite con la documentación técnica.",
        "- **Hilos de foro sin validar**: de community.cisco.com solo entran "
        "los artículos curados (`/ta-p/`), no las discusiones.",
        "",
    ]

    with open(ruta_salida, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lineas))
    return ruta_salida, {"documentos": total_docs, "operaciones": total_ops,
                         "repos": total_repos_docs, "pendientes": pendientes}


if __name__ == "__main__":
    ruta, resumen = generar()
    print(f"{ruta}: {resumen['documentos']} documentos, "
          f"{resumen['operaciones']} operaciones de API, "
          f"{resumen['repos']} documentos de repos, "
          f"{resumen['pendientes']} URLs pendientes.")
