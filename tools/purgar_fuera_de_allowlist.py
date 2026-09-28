#!/usr/bin/env python3
"""
purgar_fuera_de_allowlist.py — Retira del corpus lo que la allowlist ya no admite.

POR QUE HACE FALTA
------------------
Endurecer `path_allowlist_regex` solo afecta a lo que se rastrea A PARTIR DE
AHORA. Lo ya indexado sigue en docs/pages/ y en logs/manifest.json: el ZIP lo
sigue empaquetando y el agente lo sigue citando. El sintoma no es un error,
es una respuesta con una fuente que ya se habia decidido excluir.

Esto paso al pasar el deny-by-default de "por ruta" a "por host": 2.699
entradas del manifiesto vivian en 54 hosts nunca declarados (2.145 solo del
Bug Search Tool) y 348 documentos de marketing seguian en el corpus.

USO
---
    python3 tools/purgar_fuera_de_allowlist.py            # informe, no toca nada
    python3 tools/purgar_fuera_de_allowlist.py --aplicar  # borra y reescribe

Se ejecuta desde la raiz del repo: las rutas de estado son relativas.
"""

import argparse
import collections
import json
import os
import sys
from urllib.parse import urlparse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "src"))

# crawler_ai es importable sin crawl4ai: su import va dentro de deep_crawl().
from crawler_ai import url_aceptable            # noqa: E402
from fetch_policy import RUTA_CUARENTENA        # noqa: E402
from state_store import DIR_DOCS, RUTA_FRONTERA, RUTA_MANIFIESTO  # noqa: E402


def _fuera(ruta, claves):
    """URLs de `claves` que la allowlist ya no admite, leidas de `ruta`."""
    if not os.path.exists(ruta):
        return []
    with open(ruta, encoding="utf-8") as fh:
        return [u for u in claves(json.load(fh)) if not url_aceptable(u)]


def analizar():
    """Devuelve (sobrantes, frontera_sucia, cuarentena_sucia, manifiesto).
    No modifica nada."""
    with open(RUTA_MANIFIESTO, encoding="utf-8") as fh:
        manifiesto = json.load(fh)

    sobrantes = {url: entrada
                 for url, entrada in manifiesto.get("entradas", {}).items()
                 if not url_aceptable(url)}

    frontera_sucia = _fuera(RUTA_FRONTERA, lambda d: [i["url"] for i in d])
    # La cuarentena es el otro sitio donde queda estado muerto: 1.369 de sus
    # 1.440 URLs eran 403 del Bug Search Tool, un host que ya no se rastrea.
    cuarentena_sucia = _fuera(RUTA_CUARENTENA, list)

    return sobrantes, frontera_sucia, cuarentena_sucia, manifiesto


def aplicar(sobrantes, manifiesto):
    """Borra los .md y retira las entradas. Devuelve el numero de ficheros."""
    borrados = 0
    for url, entrada in sobrantes.items():
        doc_id = entrada.get("doc_id")
        if doc_id:
            ruta = os.path.join(DIR_DOCS, f"{doc_id}.md")
            if os.path.exists(ruta):
                os.remove(ruta)
                borrados += 1
        manifiesto["entradas"].pop(url, None)

    with open(RUTA_MANIFIESTO, "w", encoding="utf-8") as fh:
        json.dump(manifiesto, fh, indent=2, ensure_ascii=False)

    if os.path.exists(RUTA_FRONTERA):
        with open(RUTA_FRONTERA, encoding="utf-8") as fh:
            frontera = json.load(fh)
        limpia = [i for i in frontera if url_aceptable(i["url"])]
        with open(RUTA_FRONTERA, "w", encoding="utf-8") as fh:
            json.dump(limpia, fh, indent=2)

    if os.path.exists(RUTA_CUARENTENA):
        with open(RUTA_CUARENTENA, encoding="utf-8") as fh:
            cuarentena = json.load(fh)
        limpia = {u: v for u, v in cuarentena.items() if url_aceptable(u)}
        with open(RUTA_CUARENTENA, "w", encoding="utf-8") as fh:
            json.dump(limpia, fh, indent=2, ensure_ascii=False)

    return borrados


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--aplicar", action="store_true",
                    help="Borra de verdad. Sin esto solo se informa.")
    args = ap.parse_args()

    sobrantes, frontera_sucia, cuarentena_sucia, manifiesto = analizar()

    por_host = collections.Counter(urlparse(u).netloc for u in sobrantes)
    con_documento = sum(1 for e in sobrantes.values()
                        if e.get("doc_id") and os.path.exists(
                            os.path.join(DIR_DOCS, f"{e['doc_id']}.md")))

    print(f"Entradas del manifiesto fuera de la allowlist: {len(sobrantes)}")
    print(f"  ...con documento en {DIR_DOCS}/: {con_documento}")
    print(f"URLs de la frontera fuera de la allowlist:     {len(frontera_sucia)}")
    print(f"URLs en cuarentena fuera de la allowlist:      {len(cuarentena_sucia)}")
    print("\nPor host:")
    for host, n in por_host.most_common(25):
        print(f"  {n:6}  {host}")

    if not args.aplicar:
        print("\nInforme solamente. Repite con --aplicar para borrar.")
        return 0

    borrados = aplicar(sobrantes, manifiesto)
    print(f"\nBorrados {borrados} documentos, retiradas {len(sobrantes)} "
          f"entradas, {len(frontera_sucia)} URLs de la frontera y "
          f"{len(cuarentena_sucia)} de la cuarentena.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
