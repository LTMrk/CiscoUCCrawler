"""
crawler_ai.py — Orquestador del pipeline CiscoUCCrawler.

FLUJO
-----
  1. Ingesta de la referencia de la API desde los OpenAPI oficiales
     (openapi_ingest). No pasa por el WAF y da datos estructurados.
  2. Determinación del modo: BOOTSTRAP si el manifiesto está vacío,
     INCREMENTAL en adelante.
  3. Construcción de la frontera: sitemaps declarados en robots.txt en la
     primera pasada; frontera persistida en las siguientes.
  4. Por cada URL dentro del presupuesto del lote: política de acceso ->
     fetch -> sanitización -> comparación de hash -> escritura si hay delta.
  5. Emisión de deltas.json, persistencia de frontera y more_work.flag,
     un único commit al final.

CORRECCIONES SOBRE LA VERSIÓN ANTERIOR
--------------------------------------
  - git_commit_and_push() se llamaba DENTRO del bucle: un push por página,
    con rebase contra remoto en cada iteración. Ahora es un commit al final.
  - Las URLs fallidas se añadían a `visited` pero nunca al estado, así que se
    reintentaban indefinidamente entre ejecuciones. Ahora hay fail_count con
    aparcado tras 5 fallos.
  - La deduplicación por hash global descartaba páginas legítimamente
    parecidas. Ahora la comparación es por URL.
  - El markdown se escribía en modo append sobre un fichero consolidado, lo
    que duplica chunks en cada recrawl. Ahora es un fichero por documento.
"""

import asyncio
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from urllib.parse import urljoin, urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig

from fetch_policy import USER_AGENT, PoliticaAcceso
from sanitizer import DetectorBoilerplate, sanitizar
from state_store import (
    ManifestStore, cargar_frontera, guardar_frontera,
)
import openapi_ingest


# ---------------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------------

def load_config():
    config_path = "config.json"
    default_config = {
        "global_settings": {
            "default_max_depth": 1,
            "requests_per_minute": 20,
            "respect_robots": True,
            "bootstrap_budget": 400,
            "incremental_budget": 120,
            "boilerplate_threshold": 0.25,
        },
        "domain_depths": {},
        "seeds": [],
        "sitemaps": [],
        "blocked_patterns": [],
        "custom_behaviors": [],
        "SELECTORES_RUIDO_CSS": [],
    }
    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                usuario = json.load(f)
            for clave, valor in usuario.items():
                if isinstance(valor, dict) and isinstance(default_config.get(clave), dict):
                    default_config[clave].update(valor)
                else:
                    default_config[clave] = valor
        except Exception as e:
            log_error("CONFIG", f"config.json ilegible, usando defaults: {e}")
    return default_config


CONFIG = load_config()
GS = CONFIG.get("global_settings", {})
BLOCKED_PATTERNS = CONFIG.get("blocked_patterns", [])
SELECTORES_RUIDO_CSS = CONFIG.get("SELECTORES_RUIDO_CSS", [])


def _compilar(patrones, etiqueta):
    """Compila regex tolerando errores: un patrón malformado se registra y se
    descarta, en lugar de tumbar toda la ejecución."""
    compiladas = []
    for p in patrones:
        try:
            compiladas.append(re.compile(p))
        except re.error as e:
            log_error("CONFIG", f"Regex inválida en {etiqueta}: {p!r} -> {e}")
    return compiladas


BLOCKED_REGEX = _compilar(CONFIG.get("blocked_regex", []), "blocked_regex")
DISCOVERY_ONLY_REGEX = _compilar(CONFIG.get("discovery_only_regex", []), "discovery_only_regex")
PATH_ALLOWLIST = {
    dominio: _compilar(patrones, f"path_allowlist_regex[{dominio}]")
    for dominio, patrones in (CONFIG.get("path_allowlist_regex") or {}).items()
}


# ---------------------------------------------------------------------------
# Filtros de URL (lógica preexistente, conservada)
# ---------------------------------------------------------------------------

def normalize_url(url):
    return url.split("#")[0].split("?")[0].rstrip("/")


def is_blocked_by_user(url):
    url_lower = url.lower()
    if any(p in url_lower for p in BLOCKED_PATTERNS):
        return True
    return any(r.search(url) for r in BLOCKED_REGEX)


def esta_en_allowlist(url):
    """Deny-by-default por dominio. Si el dominio tiene allowlist declarada,
    la URL debe casar con alguna de sus regex. Un dominio sin allowlist se
    rige solo por la blocklist.

    Este es el control primario para www.cisco.com: el sitio tiene millones
    de URLs y una blocklist nunca alcanzaría a cubrir el ruido. Con allowlist
    se invierte la carga: solo entra lo que se ha declarado valioso."""
    netloc = urlparse(url).netloc.lower()
    for dominio, patrones in PATH_ALLOWLIST.items():
        if dominio in netloc:
            return any(r.match(url) for r in patrones)
    return True


def es_solo_descubrimiento(url):
    """Páginas que se rastrean para extraer enlaces pero no se indexan.
    Un índice de guías es una lista de títulos: como chunk vectorial no
    responde a nada y además compite en similitud con los documentos reales,
    desplazándolos en el top-k."""
    return any(r.match(url) for r in DISCOVERY_ONLY_REGEX)


def is_strict_en_us(url):
    parsed = urlparse(url.lower())
    if "cisco.com" in parsed.netloc and "/c/" in parsed.path and "/c/en/us/" not in parsed.path:
        return False
    if ("webex.com" in parsed.netloc
            and bool(re.search(r"/[a-z]{2}-[a-z]{2}/", parsed.path))
            and "/en-us/" not in parsed.path):
        return False
    return True


def is_allowed_domain(url):
    return any(d in url for d in
               ["cisco.com", "webex.com", "webexconnect.io", "webexengage.io"])


def url_aceptable(url):
    return (url.startswith("http")
            and is_allowed_domain(url)
            and is_strict_en_us(url)
            and not is_blocked_by_user(url)
            and esta_en_allowlist(url))


def get_max_depth_for_url(url):
    netloc = urlparse(url.lower()).netloc
    for dominio, prof in CONFIG.get("domain_depths", {}).items():
        if dominio in netloc:
            return prof
    return GS.get("default_max_depth", 1)


def get_custom_behavior(url):
    """Devuelve (css_selector, js_code). La purga por JS sigue siendo útil
    para nodos que solo existen tras la hidratación; la poda dura la hace
    después sanitizer.py sobre el HTML resultante."""
    url_lower = url.lower()
    js_purge = ""
    if SELECTORES_RUIDO_CSS:
        selectores = ",".join(SELECTORES_RUIDO_CSS).replace("'", "\\'")
        js_purge = f"document.querySelectorAll('{selectores}').forEach(n => n?.remove());\n"

    for comportamiento in CONFIG.get("custom_behaviors", []):
        if comportamiento.get("pattern", "").lower() in url_lower:
            js = comportamiento.get("js_code", "await new Promise(r => setTimeout(r, 1500));")
            return comportamiento.get("css_selector"), js_purge + js

    return None, js_purge + "await new Promise(r => setTimeout(r, 1500));"


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

def log_error(url, motivo):
    os.makedirs("logs", exist_ok=True)
    with open("logs/error.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}] {motivo} | {url}\n")


def log_info(mensaje):
    print(f"[crawler] {mensaje}", flush=True)


def git_commit_and_push(mensaje):
    """Un único commit al final de la ejecución."""
    try:
        subprocess.run(["git", "config", "--global", "user.name",
                        "github-actions[bot]"], check=True)
        subprocess.run(["git", "config", "--global", "user.email",
                        "github-actions[bot]@users.noreply.github.com"], check=True)
        estado = subprocess.run(["git", "status", "--porcelain"],
                                capture_output=True, text=True)
        if not estado.stdout.strip():
            log_info("Sin cambios que commitear.")
            return
        subprocess.run(["git", "add", "docs/", "logs/", "config.json"], check=True)
        subprocess.run(["git", "commit", "-m", mensaje], check=True)
        subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=False)
        subprocess.run(["git", "push"], check=True)
    except Exception as e:
        log_error("GIT_PUSH", str(e))


async def descubrir_por_sitemap(politica, semillas):
    """Descubrimiento vía sitemap declarado en robots.txt. Es la vía que el
    operador expone deliberadamente: una petición devuelve cientos de URLs en
    lugar de rastrear el sitio enlace a enlace."""
    import urllib.error
    import urllib.request
    import xml.etree.ElementTree as ET

    encontradas = set()
    sitemaps = list(CONFIG.get("sitemaps", []))
    for semilla in semillas:
        sitemaps.extend(politica.robots.sitemaps(semilla))

    for sm in dict.fromkeys(sitemaps):
        try:
            req = urllib.request.Request(sm, headers=politica.cabeceras())
            with urllib.request.urlopen(req, timeout=60) as resp:
                raiz = ET.fromstring(resp.read())
            ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            nuevas = 0
            for loc in raiz.findall(".//s:loc", ns):
                u = normalize_url((loc.text or "").strip())
                if url_aceptable(u):
                    encontradas.add(u)
                    nuevas += 1
            log_info(f"Sitemap OK ({nuevas} URLs utiles): {sm}")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                # El robots.txt de cisco.com declara sitemaps que ya no
                # existen. Es ruido del origen, no un fallo nuestro: se
                # informa pero no ensucia error.log.
                log_info(f"Sitemap declarado en robots.txt pero inexistente (404): {sm}")
            else:
                log_error(sm, f"Sitemap HTTP {e.code}")
        except Exception as e:
            log_error(sm, f"Sitemap ilegible: {e}")

    return encontradas


# ---------------------------------------------------------------------------
# Bucle principal
# ---------------------------------------------------------------------------

async def deep_crawl():
    os.makedirs("docs", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

    manifiesto = ManifestStore()
    modo = manifiesto.modo
    presupuesto = (GS.get("bootstrap_budget", 400) if modo == ManifestStore.MODO_BOOTSTRAP
                   else GS.get("incremental_budget", 120))
    log_info(f"Modo: {modo.upper()} | presupuesto de este lote: {presupuesto} URLs")

    # -- Paso 1: referencia de la API desde la fuente oficial ---------------
    resumen_api = openapi_ingest.ingerir_openapi(
        token=os.environ.get("GITHUB_TOKEN"),
        specs_permitidos=CONFIG.get("openapi_specs_allowlist"),
    )
    total_ops = sum(v.get("operaciones", 0) for v in resumen_api.values()
                    if isinstance(v, dict))
    log_info(f"OpenAPI: {total_ops} operaciones en {len(resumen_api)} specs.")

    politica = PoliticaAcceso(
        peticiones_por_minuto=GS.get("requests_per_minute", 20),
        respetar_robots=GS.get("respect_robots", True),
    )

    detector = DetectorBoilerplate(
        umbral_frecuencia=GS.get("boilerplate_threshold", 0.25)
    ).cargar()

    # -- Paso 2: frontera ----------------------------------------------------
    cola = asyncio.Queue()
    encolados = set()

    pendientes = cargar_frontera()
    if pendientes:
        for u, d in pendientes:
            await cola.put((u, d))
            encolados.add(u)
        log_info(f"Frontera restaurada: {len(pendientes)} URLs pendientes.")
    else:
        semillas = [normalize_url(s.strip()) for s in CONFIG.get("seeds", []) if s.strip()]
        candidatas = set(s for s in semillas if url_aceptable(s))

        if modo == ManifestStore.MODO_BOOTSTRAP:
            candidatas |= await descubrir_por_sitemap(politica, semillas)
        else:
            # En incremental se reevalúa lo conocido cuyo TTL haya vencido.
            candidatas |= {u for u in manifiesto.entradas if manifiesto.debe_visitar(u)}

        for u in sorted(candidatas):
            await cola.put((u, 0))
            encolados.add(u)
        log_info(f"Frontera inicial: {cola.qsize()} URLs.")

    procesadas = 0
    visitadas_este_lote = set()

    # BrowserConfig: ajustes de navegador para TODA la sesión. Aquí es donde
    # crawl4ai acepta `headers` — no en CrawlerRunConfig, que es por petición.
    # Solo caben cabeceras estáticas; los validadores condicionales, que
    # varían por URL, se resuelven con el HEAD previo (precheck_condicional).
    browser_cfg = BrowserConfig(
        headless=True,
        user_agent=USER_AGENT,
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        },
        # No descarga imágenes: es un crawler de documentación, y reduce
        # el ancho de banda que consumimos del origen.
        text_mode=True,
        verbose=False,
    )

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        while not cola.empty() and procesadas < presupuesto:
            if politica.breaker.abierto:
                log_info("Circuit breaker abierto: demasiados errores. "
                         "Se detiene el lote y se conserva la frontera.")
                break

            url, profundidad = await cola.get()
            if url in visitadas_este_lote:
                continue
            visitadas_este_lote.add(url)

            permitido, motivo = politica.puede_solicitar(url)
            if not permitido:
                log_error(url, f"Omitida: {motivo}")
                continue

            if not manifiesto.debe_visitar(url):
                continue

            await politica.antes_de_solicitar(url)
            procesadas += 1

            css, js = get_custom_behavior(url)
            validadores = manifiesto.cabeceras_condicionales(url)

            # HEAD condicional previo: si el origen dice 304, nos ahorramos
            # levantar el navegador para esta URL.
            previo = await politica.precheck_condicional(url, validadores)
            if previo and previo[0] == 304:
                manifiesto.registrar_no_modificado(url)
                politica.breaker.registrar(True)
                continue

            try:
                # CrawlerRunConfig: ajustes por petición. La firma antigua de
                # arun() con kwargs sueltos (css_selector, page_timeout...)
                # está deprecada desde la 0.8.x. Y `headers` NO va aquí:
                # pertenece a BrowserConfig.
                opciones_run = dict(
                    cache_mode=CacheMode.BYPASS,
                    exclude_external_links=True,
                    remove_overlay_elements=True,
                    process_iframes=False,
                    js_code=js,
                    page_timeout=45000,
                    check_robots_txt=GS.get("respect_robots", True),
                    verbose=False,
                )
                if css:
                    opciones_run["css_selector"] = css

                run_cfg = CrawlerRunConfig(**opciones_run)
                resultado = await crawler.arun(url=url, config=run_cfg)

                codigo = getattr(resultado, "status_code", None)
                if codigo is None:
                    codigo = 200 if getattr(resultado, "success", False) else 599

                accion, espera = politica.tras_respuesta(url, codigo)

                if accion == "no_modificado":
                    manifiesto.registrar_no_modificado(url)
                    continue

                if accion == "desaparecido":
                    manifiesto.registrar_desaparecido(url)
                    log_info(f"Tombstone emitido para {url}")
                    continue

                if accion == "cuarentena":
                    manifiesto.registrar_bloqueo(url, codigo)
                    log_error(url, f"HTTP {codigo}: en cuarentena, sin reintento automático.")
                    continue

                if accion == "reintentar":
                    log_info(f"HTTP {codigo}: reintento tras {espera:.1f}s")
                    await asyncio.sleep(espera)
                    await cola.put((url, profundidad))
                    visitadas_este_lote.discard(url)
                    continue

                if accion == "fallo" or not getattr(resultado, "html", None):
                    manifiesto.registrar_fallo(url)
                    log_error(url, f"HTTP {codigo} o DOM vacío.")
                    continue

                # -- Sanitización -------------------------------------------
                solo_descubrimiento = es_solo_descubrimiento(url)

                if solo_descubrimiento:
                    # Página de navegación: no se sanitiza ni se indexa, pero
                    # sí se recorren sus enlaces más abajo.
                    markdown, bloques = "", []
                else:
                    markdown, bloques = sanitizar(
                        resultado.html,
                        selectores_extra=SELECTORES_RUIDO_CSS,
                        detector=detector if modo == ManifestStore.MODO_INCREMENTAL else None,
                    )

                    if modo == ManifestStore.MODO_BOOTSTRAP:
                        # En la captura completa se acumula estadística de
                        # plantilla; el filtrado real se aplica al consolidar.
                        detector.observar(bloques)

                    if len(markdown) < 200:
                        manifiesto.registrar_fallo(url)
                        log_error(url, f"Markdown insuficiente tras sanitizar ({len(markdown)} chars).")
                        markdown = ""

                # -- Delta ---------------------------------------------------
                if markdown:
                    cambio, doc_id = manifiesto.registrar_contenido(url, markdown)
                    cabeceras_resp = getattr(resultado, "response_headers", None) or {}
                    if isinstance(cabeceras_resp, dict):
                        manifiesto.registrar_cabeceras(
                            url,
                            cabeceras_resp.get("etag") or cabeceras_resp.get("ETag"),
                            cabeceras_resp.get("last-modified") or cabeceras_resp.get("Last-Modified"),
                        )
                    if cambio:
                        manifiesto.escribir_documento(doc_id, url, markdown)
                        log_info(f"Delta -> {doc_id}")

                # -- Expansión de la frontera --------------------------------
                if profundidad < get_max_depth_for_url(url):
                    enlaces = getattr(resultado, "links", {}) or {}
                    for enlace in enlaces.get("internal", []):
                        href = enlace.get("href") if isinstance(enlace, dict) else None
                        if not href:
                            continue
                        siguiente = normalize_url(urljoin(url, href))
                        if (siguiente not in encolados
                                and siguiente not in visitadas_este_lote
                                and url_aceptable(siguiente)
                                and manifiesto.debe_visitar(siguiente)):
                            await cola.put((siguiente, profundidad + 1))
                            encolados.add(siguiente)

            except Exception as e:
 
