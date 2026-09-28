#!/usr/bin/env python3
"""
probe_devnet.py — Sondeo de diagnostico de developer.cisco.com.

NO forma parte del ETL ni de CI. Es una herramienta de una sola pasada, solo
lectura, para responder a las preguntas que deciden la configuracion del
rastreo y que no se pueden contestar mirando el codigo:

  1. robots.txt: se puede entrar en /docs/ y /site/? hay Crawl-delay? hay
     sitemaps declarados?
  2. sitemap.xml: existe? es un <sitemapindex>? cuantas URLs de colaboracion
     trae? (descubrir_por_sitemap ya recursa en indices, pero solo si hay uno)
  3. Barra final: confirma que /docs/<x> responde 301 hacia /docs/<x>/. Es la
     causa raiz por la que este dominio no entraba en el corpus.
  4. SSR o SPA: cuanto texto trae el HTML crudo, sin ejecutar JavaScript. Si
     viene servido, no hace falta esperar hidratacion y se puede bajar el
     js_code de custom_behaviors.
  5. Origen del contenido: rastro de PubHub (pubhub.devnetcloud.com) o de un
     blob de estado (__NEXT_DATA__, window.__...). Si el contenido sale de
     ficheros estaticos, una ingesta estructurada al estilo de
     openapi_ingest.py seria mejor que rascar el DOM.
  6. Inventario de doc-sets DESDE EL SITEMAP, contrastado con la allowlist de
     config.json. No desde el HTML de /docs/: ese indice lo construye
     JavaScript y no enlaza nada en el HTML crudo, asi que rastrearlo no
     descubre ningun doc-set.

Solo stdlib: tiene que poder ejecutarse sin instalar crawl4ai ni Playwright.

    python3 tools/probe_devnet.py
    python3 tools/probe_devnet.py --url https://developer.cisco.com/docs/axl/
"""

import argparse
import gzip
import json
import os
import re
import sys
import urllib.error
import urllib.request
import urllib.robotparser
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "src"))
try:
    from fetch_policy import USER_AGENT
except Exception:                                    # ejecucion fuera del repo
    USER_AGENT = "CiscoUCCrawler/2.0 (documentation indexing for internal RAG)"

BASE = "https://developer.cisco.com"
TIMEOUT = 45

# URLs representativas. Se sondean SIN barra final a proposito: es la forma
# que generaba el 301.
#
# Se han retirado /docs/finesse/rest-api-dev-guide y /docs/jabber-bots, que
# un sondeo real confirmo como 404: eran doc-sets vivos cuando quedaron
# registrados en logs/error.log y ya no existen. Una URL muerta no dice nada
# sobre barra final ni sobre renderizado, que es lo que mide esta seccion.
URLS_MUESTRA = [
    "/docs",
    "/docs/axl",
    "/docs/axl/axl-developer-guide",
    "/docs/finesse",
    "/docs/unity-connection",
    "/docs/contact-center-express",
    "/docs/customer-voice-portal",
    "/docs/packaged-contact-center",
    "/site/sxml",
    "/site/collaboration",
    "/site/unity-connection/documentation",
    "/site/roomdevices",
]


class _SoloTexto(HTMLParser):
    """Extrae texto visible. Suficiente para medir si el HTML crudo trae
    contenido o solo el esqueleto de la aplicacion."""

    SALTAR = {"script", "style", "noscript", "template"}

    def __init__(self):
        super().__init__()
        self.trozos = []
        self._ignorando = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SALTAR:
            self._ignorando += 1

    def handle_endtag(self, tag):
        if tag in self.SALTAR and self._ignorando:
            self._ignorando -= 1

    def handle_data(self, data):
        if not self._ignorando:
            texto = data.strip()
            if texto:
                self.trozos.append(texto)

    @property
    def texto(self):
        return " ".join(self.trozos)


def pedir(url, metodo="GET", seguir=False):
    """Devuelve (codigo, cabeceras, cuerpo). No sigue redirecciones salvo que
    se pida: el objetivo del sondeo es precisamente verlas."""

    class _SinRedirigir(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None

    handlers = [] if seguir else [_SinRedirigir]
    opener = urllib.request.build_opener(*handlers)
    req = urllib.request.Request(url, method=metodo, headers={
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip",
    })
    try:
        with opener.open(req, timeout=TIMEOUT) as resp:
            cuerpo = resp.read()
            if resp.headers.get("Content-Encoding") == "gzip":
                cuerpo = gzip.decompress(cuerpo)
            return resp.status, dict(resp.headers), cuerpo
    except urllib.error.HTTPError as e:
        cuerpo = b""
        try:
            cuerpo = e.read()
            if e.headers.get("Content-Encoding") == "gzip":
                cuerpo = gzip.decompress(cuerpo)
        except Exception:
            pass
        return e.code, dict(e.headers or {}), cuerpo
    except Exception as e:
        return None, {"_error": str(e)}, b""


def titulo(texto):
    print()
    print("=" * 72)
    print(texto)
    print("=" * 72)


# ---------------------------------------------------------------------------
# 1. robots.txt
# ---------------------------------------------------------------------------

def sondear_robots():
    titulo("1. robots.txt")
    codigo, _, cuerpo = pedir(f"{BASE}/robots.txt", seguir=True)
    print(f"HTTP {codigo}")
    if not cuerpo:
        print("Sin cuerpo. No se puede evaluar la politica de rastreo.")
        return []

    texto = cuerpo.decode("utf-8", "replace")
    print("-" * 72)
    print(texto.strip()[:4000])
    print("-" * 72)

    rp = urllib.robotparser.RobotFileParser()
    rp.parse(texto.splitlines())

    print("\nVeredicto para nuestro User-Agent:")
    for ruta in ["/docs/", "/docs/axl/", "/site/", "/site/collaboration/",
                 "/web/axl/home", "/codeexchange/"]:
        permitido = rp.can_fetch(USER_AGENT, BASE + ruta)
        print(f"  {'PERMITIDO' if permitido else 'PROHIBIDO':10} {ruta}")

    retardo = rp.crawl_delay(USER_AGENT)
    print(f"\nCrawl-delay: {retardo if retardo is not None else 'no declarado'}")

    sitemaps = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", texto)
    print(f"Sitemaps declarados: {sitemaps or 'ninguno'}")
    return sitemaps


# ---------------------------------------------------------------------------
# 2. sitemaps
# ---------------------------------------------------------------------------

def sondear_sitemaps(declarados):
    """Devuelve el conjunto de URLs de /docs/ y /site/ vistas en los sitemaps.

    Es la salida mas util del sondeo: el indice de /docs/ lo construye
    JavaScript y no enlaza nada en el HTML crudo, asi que el sitemap es la
    unica forma de saber que doc-sets existen realmente.
    """
    titulo("2. Sitemaps")
    candidatos = list(dict.fromkeys(declarados + [f"{BASE}/sitemap.xml"]))
    documentacion = set()

    for sm in candidatos:
        codigo, _, cuerpo = pedir(sm, seguir=True)
        print(f"\n{sm}  ->  HTTP {codigo}  ({len(cuerpo)} bytes)")
        if codigo != 200 or not cuerpo:
            continue

        if cuerpo[:2] == b"\x1f\x8b":
            cuerpo = gzip.decompress(cuerpo)

        try:
            raiz = ET.fromstring(cuerpo)
        except ET.ParseError as e:
            print(f"  No es XML valido ({e}). Primeros bytes: {cuerpo[:120]!r}")
            continue

        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        es_indice = raiz.tag.endswith("sitemapindex")
        locs = [(l.text or "").strip() for l in raiz.findall(".//s:loc", ns)]
        print(f"  Tipo: {'sitemapindex' if es_indice else 'urlset'} | {len(locs)} <loc>")

        if es_indice:
            print("  IMPORTANTE: hay que recursar en los hijos (ya soportado en "
                  "descubrir_por_sitemap).")
            for hijo in locs[:10]:
                print(f"    - {hijo}")
        else:
            colab = [u for u in locs
                     if re.search(r"/(docs|site)/", urlparse(u).path)]
            documentacion.update(colab)
            print(f"  URLs bajo /docs/ o /site/: {len(colab)}")

    print(f"\nTotal de URLs de /docs/ o /site/ vistas en sitemaps: "
          f"{len(documentacion)}")
    return documentacion


# ---------------------------------------------------------------------------
# 3, 4 y 5. barra final, SSR y origen del contenido
# ---------------------------------------------------------------------------

RASTROS = {
    "pubhub": re.compile(rb"pubhub\.devnetcloud\.com", re.I),
    "__NEXT_DATA__": re.compile(rb"__NEXT_DATA__"),
    "window.__": re.compile(rb"window\.__[A-Z_]+"),
    "ng-version": re.compile(rb"ng-version="),
    "id=\"root\"": re.compile(rb"id=[\"']root[\"']"),
}


RE_TITLE = re.compile(rb"<title[^>]*>(.*?)</title>", re.I | re.S)


def _titulo_html(cuerpo):
    """<title> de la pagina, limpio. Vacio si no hay."""
    m = RE_TITLE.search(cuerpo)
    if not m:
        return ""
    texto = re.sub(rb"\s+", b" ", m.group(1)).strip()
    return texto.decode("utf-8", "replace")[:120]


def sondear_paginas(rutas):
    titulo("3-5. Barra final, renderizado sin JS y origen del contenido")
    print(f"{'ruta':52} {'sin/':>5} {'con/':>5} {'chars':>7}  rastros")
    print("-" * 100)

    resumen = {"redirigen": 0, "ssr": 0, "shells": []}

    for ruta in rutas:
        sin_barra = urljoin(BASE, ruta)
        con_barra = sin_barra.rstrip("/") + "/"

        cod_sin, cab_sin, _ = pedir(sin_barra, metodo="HEAD")
        cod_con, _, cuerpo = pedir(con_barra, seguir=True)

        destino = cab_sin.get("Location") or cab_sin.get("location") or ""
        if cod_sin in (301, 302, 303, 307, 308):
            resumen["redirigen"] += 1

        parser = _SoloTexto()
        try:
            parser.feed(cuerpo.decode("utf-8", "replace"))
        except Exception:
            pass
        n = len(parser.texto)

        # 200 chars es el umbral que usa crawler_ai para descartar un documento.
        if n >= 2000:
            resumen["ssr"] += 1
        elif n < 200:
            resumen["shells"].append(con_barra)

        rastros = [k for k, r in RASTROS.items() if r.search(cuerpo)]
        print(f"{ruta:52} {str(cod_sin):>5} {str(cod_con):>5} {n:>7}  "
              f"{','.join(rastros) or '-'}")
        # El <title> es lo unico que identifica un doc-set desconocido. Sin
        # el, la lista de "fuera de la allowlist" deja preguntas abiertas
        # que no se pueden cerrar desde el codigo: docs/cmse llevaba meses
        # sin identificar por eso.
        nombre = _titulo_html(cuerpo)
        if nombre:
            print(f"{'':52} title: {nombre}")
        if destino:
            print(f"{'':52} Location: {destino}")

    print("-" * 100)
    print(f"Redirigen sin barra final : {resumen['redirigen']}/{len(rutas)}")
    print(f"Traen contenido sin JS    : {resumen['ssr']}/{len(rutas)}  (>=2000 chars)")
    print(f"Shell vacio sin JS        : {len(resumen['shells'])}/{len(rutas)}  (<200 chars)")
    print()
    if resumen["redirigen"]:
        print("=> Confirma la causa raiz: sin barra final el origen responde 3xx.")
        print("   Lo cubren global_settings.hosts_barra_final y la rama 3xx de")
        print("   fetch_policy.tras_respuesta.")
    if resumen["shells"]:
        # Una mayoria de paginas servidas NO permite bajar la espera: basta
        # con que una pagina que interesa llegue vacia para perderla. Lo que
        # decide es si alguna de las que se quiere indexar es un shell.
        print("=> Hay paginas que llegan VACIAS sin JavaScript:")
        for u in resumen["shells"]:
            print(f"     {u}")
        print("   Mantener el js_code de custom_behaviors para")
        print("   developer.cisco.com. Si alguna de estas es solo un indice de")
        print("   navegacion, lo suyo es marcarla en discovery_only_regex en")
        print("   lugar de intentar rescatarla.")
    else:
        print("=> Ninguna pagina de la muestra depende de JavaScript: se puede")
        print("   bajar la espera de custom_behaviors y ahorrar tiempo de lote.")


# ---------------------------------------------------------------------------
# 6. inventario de doc-sets
# ---------------------------------------------------------------------------

def inventariar_docsets(urls_sitemap):
    """Inventario de doc-sets contrastado con la allowlist de config.json.

    Se construye desde el sitemap y no desde el HTML de /docs/: ese indice lo
    genera JavaScript, asi que rastrearlo no descubre nada. Esta es la lista
    que hay que revisar para decidir que entra y que no.
    """
    titulo("6. Doc-sets del sitemap frente a la allowlist")

    if not urls_sitemap:
        print("Sin URLs de sitemap: no se puede inventariar. Revisar la")
        print("seccion 2 (robots.txt puede haber dejado de declararlos).")
        return

    # La allowlist del dominio se compone de dos partes: lo que declara
    # path_allowlist_regex y la alternacion que crawler_ai genera desde
    # devnet_docsets. Hay que reproducir las DOS o el inventario dira que
    # esta fuera casi todo.
    compiladas, docsets_declarados = [], {}
    try:
        with open("config.json", encoding="utf-8") as fh:
            cfg = json.load(fh)
        patrones = list(cfg["path_allowlist_regex"].get("developer.cisco.com", []))
        docsets_declarados = cfg.get("devnet_docsets") or {}
        if docsets_declarados:
            patrones.append(
                r"^https?://developer\.cisco\.com/(docs|site)/(%s)(/|$)"
                % "|".join(docsets_declarados))
        compiladas = [re.compile(p) for p in patrones]
    except Exception as e:
        print(f"No se pudo leer la allowlist de config.json: {e}")

    # Agrupa por doc-set: /docs/<set>/... y /site/<set>/...
    grupos = {}
    for u in urls_sitemap:
        partes = [p for p in urlparse(u).path.split("/") if p]
        if len(partes) < 2:
            continue
        grupos.setdefault(f"{partes[0]}/{partes[1]}", []).append(u)

    dentro, fuera = [], []
    for clave, miembros in sorted(grupos.items()):
        admitido = any(r.match(m) for m in miembros for r in compiladas)
        (dentro if admitido else fuera).append((clave, len(miembros)))

    print(f"{len(grupos)} doc-sets en el sitemap "
          f"({len(dentro)} admitidos, {len(fuera)} fuera)\n")

    print(f"-- ADMITIDOS por la allowlist ({len(dentro)}) " + "-" * 30)
    for clave, n in dentro:
        print(f"  {n:4d} URLs  {clave}")

    print(f"\n-- FUERA de la allowlist ({len(fuera)}) " + "-" * 33)
    print("  Repasar esta lista: lo que sea de colaboracion hay que anadirlo")
    print("  a path_allowlist_regex. El resto (Meraki, DNA Center, SD-WAN,")
    print("  NSO, AppDynamics, seguridad...) se queda fuera a proposito.\n")
    for clave, n in fuera:
        print(f"  {n:4d} URLs  {clave}")

    # Bloque listo para pegar: la friccion de anadir un doc-set no debe ser
    # reescribir una regex a mano.
    if fuera:
        print("\n-- Para admitir alguno, pegar en config.json -> devnet_docsets "
              + "-" * 5)
        print('  "<slug>": "<clave de copilot_pack.PRODUCTOS>",   p. ej.:')
        for clave, _ in fuera[:10]:
            print(f'  "{clave.split("/", 1)[1]}": "misc",')
        print("  (La prueba test_copilot_pack falla si la clave de producto")
        print("   no existe, asi que allowlist y taxonomia no se separan.)")

    _cobertura_frente_al_corpus(grupos, {c for c, _ in dentro})


# Con menos de este numero de paginas, un doc-set admitido esta capturado a
# medias: se tiene la raiz y poco mas. Es un umbral de atencion, no un
# veredicto; hay doc-sets legitimamente de una sola pagina.
UMBRAL_DOCSET_FLACO = 3


def _cobertura_frente_al_corpus(grupos, admitidos):
    """Paginas que cada doc-set ADMITIDO ha aportado al manifiesto.

    OJO con la tentacion de comparar contra el numero de URLs del sitemap:
    el de PubHub declara UNA sola URL por doc-set, la raiz. Comparar "1 en
    sitemap frente a 13 en corpus" no mide nada, y la primera version de
    esta seccion daba 287 doc-sets "flacos" que en realidad eran los de
    Meraki, ACI y Nexus, con cero paginas porque estan fuera a proposito.

    Lo que si dice algo es el recuento absoluto sobre los admitidos: un
    doc-set con una o dos paginas es la raiz y poco mas. En PubHub el indice
    lateral lo pinta JavaScript, asi que ahi es donde se pierde el resto.
    """
    titulo("7. Cobertura de los doc-sets admitidos")

    try:
        with open("logs/manifest.json", encoding="utf-8") as fh:
            entradas = json.load(fh)["entradas"]
    except Exception as e:
        print(f"Sin manifiesto que contrastar ({e}). Normal antes del primer ETL.")
        return

    capturadas = {}
    for url, entrada in entradas.items():
        if "developer.cisco.com" not in url or entrada.get("status") != "active":
            continue
        partes = [p for p in urlparse(url).path.split("/") if p]
        if len(partes) >= 2:
            clave = f"{partes[0]}/{partes[1]}"
            capturadas[clave] = capturadas.get(clave, 0) + 1

    flacos = []
    for clave in sorted(admitidos | (set(capturadas) & set(grupos))):
        paginas = capturadas.get(clave, 0)
        marca = "  <-- flaco" if paginas < UMBRAL_DOCSET_FLACO else ""
        print(f"  {paginas:4d} paginas  {clave}{marca}")
        if paginas < UMBRAL_DOCSET_FLACO:
            flacos.append((clave, paginas))

    total = sum(capturadas.get(c, 0) for c in admitidos)
    print(f"\n{total} paginas de colaboracion en el corpus, "
          f"{len(admitidos)} doc-sets admitidos, {len(flacos)} por debajo de "
          f"{UMBRAL_DOCSET_FLACO} paginas.")

    if flacos:
        print("\nLos flacos, por orden de probabilidad de causa:")
        print("  1. El indice lateral de PubHub se pinta con JavaScript y el")
        print("     js_code de custom_behaviors no espera lo suficiente. Ver")
        print("     la seccion 4: si el HTML crudo trae poco texto, es esto.")
        print("  2. Profundidad insuficiente en domain_depths.")
        print("  3. Doc-set que de verdad tiene una sola pagina.")
        for clave, n in flacos:
            print(f"     {clave}: {n}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--url", action="append", default=None,
                    help="Ruta o URL extra a sondear. Repetible.")
    ap.add_argument("--saltar-sitemaps", action="store_true")
    args = ap.parse_args()

    print(f"Sondeo de {BASE}")
    print(f"User-Agent: {USER_AGENT}")

    declarados = sondear_robots()
    urls_sitemap = set()
    if not args.saltar_sitemaps:
        urls_sitemap = sondear_sitemaps(declarados)

    rutas = list(URLS_MUESTRA)
    for u in (args.url or []):
        ruta = urlparse(u).path if u.startswith("http") else u
        if ruta not in rutas:
            rutas.append(ruta)
    sondear_paginas(rutas)

    inventariar_docsets(urls_sitemap)

    titulo("Fin")
    print("Pegar esta salida en el PR: es lo que justifica los valores de")
    print("config.json para developer.cisco.com.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
