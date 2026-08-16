"""
fetch_policy.py — Política de acceso responsable y manejo de 403 / 429.

POSTURA DE DISEÑO
-----------------
Este módulo NO contiene evasión de detección de bots. No falsifica TLS
fingerprints, no rota proxies residenciales y no aplica parches stealth para
ocultar que Playwright está automatizando el navegador.

La distinción operativa importa:

  429 Too Many Requests
      El origen dice "vas demasiado rápido". Es un problema de caudal y se
      resuelve con backoff. Implementado aquí, honrando Retry-After.

  403 Forbidden (Akamai Bot Manager)
      El origen dice "no quiero acceso automatizado por esta vía". Insistir
      con camuflaje no arregla nada: convierte un problema de configuración
      en una carrera armamentística que se pierde en la siguiente
      actualización del WAF, y expone el proyecto a bloqueo por IP del runner
      de GitHub Actions (rango público y compartido, trivial de banear).
      Aquí un 403 pone la URL en CUARENTENA y la reporta para resolución por
      la vía correcta.

VÍAS CORRECTAS PARA EL 403, EN ORDEN DE PREFERENCIA
---------------------------------------------------
  1. Usar la fuente estructurada oficial cuando existe. Para la referencia de
     la API de Webex, github.com/webex/webex-openapi-specs publica los specs
     bajo CC BY 4.0. Ver openapi_ingest.py — elimina la necesidad de tocar
     developer.webex.com.
  2. Descubrimiento por sitemap.xml en lugar de seguir enlaces a ciegas:
     menos peticiones, menos ruido, y es el canal que el operador expone
     deliberadamente para rastreadores.
  3. GET condicional (ETag / If-Modified-Since): un 304 cuesta casi nada al
     origen. Ver state_store.cabeceras_condicionales.
  4. User-Agent honesto con URL de contacto. Un rastreador identificable y
     lento se comporta estadísticamente distinto de una botnet, que es lo que
     los sistemas de reputación miden.
  5. Si tras todo lo anterior sigue habiendo 403: contactar a Cisco. Tienen
     canal de soporte para desarrolladores y programa de partners; para un
     proyecto de documentación interna, una excepción de allowlist o un
     acuerdo de acceso es una conversación normal, no un favor extraordinario.
"""

import json
import os
import random
import time
import urllib.robotparser
from collections import defaultdict, deque
from datetime import datetime, timezone
from urllib.parse import urlparse, urlunparse

RUTA_CUARENTENA = "logs/quarantine.json"

# Identificación honesta. Sustituir la URL de contacto por la del repositorio
# real: es lo que permite al operador contactar en lugar de banear a ciegas.
USER_AGENT = (
    "CiscoUCCrawler/2.0 (+https://github.com/TU-ORG/CiscoUCCrawler; "
    "documentation indexing for internal RAG; contact: tu-email@dominio)"
)


class RobotsCache:
    """Cachea y respeta robots.txt por dominio."""

    def __init__(self, user_agent=USER_AGENT):
        self.user_agent = user_agent
        self._parsers = {}

    def _parser_para(self, url):
        parsed = urlparse(url)
        clave = f"{parsed.scheme}://{parsed.netloc}"
        if clave in self._parsers:
            return self._parsers[clave]

        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(urlunparse((parsed.scheme, parsed.netloc, "/robots.txt", "", "", "")))
        try:
            rp.read()
        except Exception:
            # Si robots.txt no es accesible, se asume permisivo pero se
            # mantiene el rate limiting conservador.
            rp = None
        self._parsers[clave] = rp
        return rp

    def permitido(self, url):
        rp = self._parser_para(url)
        if rp is None:
            return True
        try:
            return rp.can_fetch(self.user_agent, url)
        except Exception:
            return True

    def crawl_delay(self, url, por_defecto=1.0):
        rp = self._parser_para(url)
        if rp is None:
            return por_defecto
        try:
            d = rp.crawl_delay(self.user_agent)
            return float(d) if d else por_defecto
        except Exception:
            return por_defecto

    def sitemaps(self, url):
        """robots.txt suele declarar los sitemaps: la vía de descubrimiento
        que el operador expone a propósito."""
        rp = self._parser_para(url)
        if rp is None:
            return []
        try:
            return list(rp.site_maps() or [])
        except Exception:
            return []


class RateLimiter:
    """Token bucket por dominio. Serializa las peticiones a un mismo host
    aunque el crawler procese varios en paralelo."""

    def __init__(self, peticiones_por_minuto=20):
        self.intervalo = 60.0 / max(peticiones_por_minuto, 1)
        self._ultima = defaultdict(float)

    async def esperar(self, url, delay_minimo=None, asyncio_sleep=None):
        import asyncio
        dormir = asyncio_sleep or asyncio.sleep

        dominio = urlparse(url).netloc
        intervalo = max(self.intervalo, delay_minimo or 0)
        transcurrido = time.monotonic() - self._ultima[dominio]
        if transcurrido < intervalo:
            # Jitter: evita un patrón de temporización perfectamente regular,
            # que además de ser detectable produce ráfagas sincronizadas.
            await dormir(intervalo - transcurrido + random.uniform(0, 0.4))
        self._ultima[dominio] = time.monotonic()


class BackoffPolicy:
    """Backoff exponencial con jitter completo, honrando Retry-After."""

    def __init__(self, base=2.0, maximo=300.0, intentos_max=4):
        self.base = base
        self.maximo = maximo
        self.intentos_max = intentos_max

    def espera_para(self, intento, retry_after=None):
        if retry_after:
            try:
                return min(float(retry_after), self.maximo)
            except (TypeError, ValueError):
                pass
        techo = min(self.maximo, self.base ** (intento + 1))
        return random.uniform(0, techo)  # full jitter

    def debe_reintentar(self, intento, codigo):
        if intento >= self.intentos_max:
            return False
        # 403 NO se reintenta: no es transitorio, es una decisión del operador.
        return codigo in (429, 500, 502, 503, 504, 408)


class CircuitBreaker:
    """Si el ratio de error se dispara, se aborta la ejecución limpiamente en
    lugar de seguir golpeando un origen que claramente nos está rechazando."""

    def __init__(self, ventana=20, umbral_error=0.5, minimo_muestras=10):
        self.resultados = deque(maxlen=ventana)
        self.umbral_error = umbral_error
        self.minimo_muestras = minimo_muestras

    def registrar(self, ok):
        self.resultados.append(1 if ok else 0)

    @property
    def abierto(self):
        if len(self.resultados) < self.minimo_muestras:
            return False
        ratio_error = 1 - (sum(self.resultados) / len(self.resultados))
        return ratio_error >= self.umbral_error


class Cuarentena:
    """Registro de URLs rechazadas por el WAF. No se reintentan de forma
    automática: se listan en un artefacto para decisión humana."""

    def __init__(self, ruta=RUTA_CUARENTENA):
        self.ruta = ruta
        self.entradas = {}
        if os.path.exists(ruta):
            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    self.entradas = json.load(f)
            except Exception:
                self.entradas = {}

    def añadir(self, url, codigo, detalle=""):
        registro = self.entradas.setdefault(url, {"veces": 0})
        registro["veces"] += 1
        registro["codigo"] = codigo
        registro["detalle"] = detalle
        registro["ultima_vez"] = datetime.now(timezone.utc).isoformat()

    def contiene(self, url):
        return url in self.entradas

    def guardar(self):
        os.makedirs(os.path.dirname(self.ruta), exist_ok=True)
        with open(self.ruta, "w", encoding="utf-8") as f:
            json.dump(self.entradas, f, indent=2, sort_keys=True)

    def informe(self):
        if not self.entradas:
            return "Sin URLs en cuarentena."
        lineas = [
            f"{len(self.entradas)} URL(s) rechazadas por el WAF de origen.",
            "No se reintentan automáticamente. Opciones:",
            "  - Usar la fuente estructurada oficial si existe "
            "(ver openapi_ingest.py para la referencia de la API de Webex).",
            "  - Reducir peticiones_por_minuto y volver a probar en otra ejecución.",
            "  - Solicitar acceso a Cisco vía soporte para desarrolladores.",
            "",
        ]
        for url, datos in sorted(self.entradas.items())[:50]:
            lineas.append(f"  [{datos.get('codigo')}] x{datos['veces']}  {url}")
        return "\n".join(lineas)


class PoliticaAcceso:
    """Fachada que agrupa las cuatro piezas y decide antes de cada petición."""

    def __init__(self, peticiones_por_minuto=20, respetar_robots=True):
        self.robots = RobotsCache()
        self.limiter = RateLimiter(peticiones_por_minuto)
        self.backoff = BackoffPolicy()
        self.breaker = CircuitBreaker()
        self.cuarentena = Cuarentena()
        self.respetar_robots = respetar_robots

    def puede_solicitar(self, url):
        """Devuelve (permitido: bool, motivo: str)."""
        if self.cuarentena.contiene(url):
            return False, "en cuarentena por rechazo previo del WAF"
        if self.respetar_robots and not self.robots.permitido(url):
            return False, "excluida por robots.txt"
        return True, ""

    async def antes_de_solicitar(self, url):
        delay = self.robots.crawl_delay(url, por_defecto=0)
        await self.limiter.esperar(url, delay_minimo=delay)

    def cabeceras(self, extra=None):
        cabeceras = {
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        }
        if extra:
            cabeceras.update(extra)
        return cabeceras

    async def precheck_condicional(self, url, validadores):
        """HEAD condicional barato ANTES de levantar el navegador.

        Por qué existe: las cabeceras If-None-Match / If-Modified-Since son
        POR URL, y crawl4ai solo admite cabeceras a nivel de BrowserConfig,
        que es por sesión. No hay forma de pasar validadores distintos en
        cada arun().

        La solución resulta mejor que la original: un HEAD cuesta ~100 ms y
        no transfiere cuerpo, mientras que un render de Playwright cuesta
        3-5 s. Si el origen responde 304, nos ahorramos el render entero.

        Solo se ejecuta si ya hay validadores guardados, así que en BOOTSTRAP
        no añade ni una petición. Devuelve (codigo, cabeceras) o None si no
        procede o si falla, en cuyo caso se sigue con el flujo normal.
        """
        if not validadores:
            return None

        import asyncio
        import urllib.error
        import urllib.request

        def _head():
            req = urllib.request.Request(
                url, method="HEAD", headers=self.cabeceras(validadores))
            try:
                with urllib.request.urlopen(req, timeout=20) as resp:
                    return resp.status, dict(resp.headers)
            except urllib.error.HTTPError as e:
                return e.code, dict(e.headers or {})
            except Exception:
                return None

        try:
            return await asyncio.to_thread(_head)
        except Exception:
            return None

    def tras_respuesta(self, url, codigo, retry_after=None, intento=0):
        """Clasifica el resultado. Devuelve una de:
        'ok' | 'no_modificado' | 'reintentar' | 'cuarentena' | 'desaparecido' | 'fallo'
        y los segundos de espera si procede."""
        if codigo == 304:
            self.breaker.registrar(True)
            return "no_modificado", 0
        if 200 <= codigo < 300:
            self.breaker.registrar(True)
            return "ok", 0
        if codigo in (404, 410):
            self.breaker.registrar(True)  # respuesta válida, no fallo de acceso
            return "desaparecido", 0
        if codigo == 403:
            self.breaker.registrar(False)
            self.cuarentena.añadir(url, 403, "Rechazado por el WAF de origen")
            return "cuarentena", 0
        if self.backoff.debe_reintentar(intento, codigo):
            self.breaker.registrar(False)
            return "reintentar", self.backoff.espera_para(intento, retry_after)

        self.breaker.registrar(False)
        if codigo == 429:
            # Agotados los reintentos de un 429: la cadencia global es
            # demasiado agresiva para este origen. Se aparca la URL.
            self.cuarentena.añadir(url, 429, "Rate limit persistente tras backoff")
            return "cuarentena", 0
        return "fallo", 0
      
