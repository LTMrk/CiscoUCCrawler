"""
sanitizer.py — Poda del DOM y eliminación de ruido vectorial.

ESTRATEGIA EN TRES CAPAS
------------------------
Capa 1 (estructural): elimina nodos por etiqueta, rol ARIA y selector CSS.
    Barre lo obvio y determinista: nav, header, footer, aside, script, style,
    banners de cookies, widgets de feedback.

Capa 2 (heurística): elimina bloques por densidad de enlaces y ratio de
    puntuación. Un <div> con 40 enlaces y 12 palabras es un menú aunque no
    lleve etiqueta <nav>. Esto captura la navegación que Cisco renderiza
    como divs genéricos.

Capa 3 (estadística, cross-documento): los avisos legales, disclaimers de
    marca registrada y pies repetidos sobreviven a las capas 1 y 2 porque
    están dentro del contenido principal. Se detectan por FRECUENCIA
    DOCUMENTAL: un bloque de texto cuyo hash normalizado aparece en más del
    N% del corpus es plantilla, no contenido. Los fingerprints se persisten
    para que las ejecuciones incrementales los apliquen sin recalcular.

Por qué importa para RAG: cada bloque repetido que sobrevive se convierte en
un chunk casi idéntico en el índice vectorial. Con cientos de páginas, los
avisos legales dominan el espacio de embeddings y las búsquedas devuelven
boilerplate en lugar de documentación.
"""

import hashlib
import json
import os
import re
from collections import Counter

from bs4 import BeautifulSoup, NavigableString

# ---------------------------------------------------------------------------
# Capa 1: poda estructural
# ---------------------------------------------------------------------------

# Etiquetas que nunca aportan contenido documental.
TAGS_ELIMINAR = [
    "script", "style", "noscript", "template", "svg", "canvas",
    "iframe", "form", "button", "input", "select", "textarea",
    "nav", "header", "footer", "aside", "dialog",
]

# Roles ARIA de navegación y chrome de página.
ROLES_ELIMINAR = [
    "navigation", "banner", "contentinfo", "complementary",
    "search", "menu", "menubar", "toolbar", "dialog", "alertdialog",
    "tablist",
]

# Selectores que sobreviven a lo anterior. Se combinan con los de config.json.
SELECTORES_RUIDO_BASE = [
    "#onetrust-banner-sdk", "#onetrust-consent-sdk", ".onetrust-pc-dark-filter",
    ".cookie-banner", "[class*='cookie']", "[id*='cookie']",
    "[class*='breadcrumb']", "[class*='sidebar']", "[class*='side-nav']",
    "[class*='toc']", "[class*='table-of-contents']",
    "[class*='feedback']", "[class*='rating']", "[class*='was-this-helpful']",
    "[class*='social']", "[class*='share']",
    "[class*='related-content']", "[class*='recommend']",
    "[class*='skip-link']", ".sr-only", ".visually-hidden",
    "[aria-hidden='true']",
    "[class*='legal']", "[class*='disclaimer']", "[class*='copyright']",
    "[class*='trademark']",
]

# Contenedores que suelen envolver el contenido real, en orden de preferencia.
CANDIDATOS_CONTENIDO = [
    "main", "article", "[role='main']", "#fw-content",
    "[class*='documentation']", "[class*='article-body']",
    "[class*='content-body']", ".content", "#content",
]

# Etiquetas cuyo contenido se preserva íntegro (no se toca ni normaliza).
TAGS_PRESERVAR = {"pre", "code", "table", "thead", "tbody", "tr", "td", "th"}


def _eliminar_por_estructura(soup, selectores_extra=None):
    for tag in TAGS_ELIMINAR:
        for nodo in soup.find_all(tag):
            nodo.decompose()

    for rol in ROLES_ELIMINAR:
        for nodo in soup.find_all(attrs={"role": rol}):
            nodo.decompose()

    selectores = list(SELECTORES_RUIDO_BASE) + list(selectores_extra or [])
    for selector in selectores:
        try:
            for nodo in soup.select(selector):
                nodo.decompose()
        except Exception:
            # Un selector malformado en config.json no debe abortar la poda.
            continue

    # Comentarios HTML.
    for comentario in soup.find_all(string=lambda t: isinstance(t, NavigableString)
                                    and t.strip().startswith("<!--")):
        comentario.extract()

    return soup


# ---------------------------------------------------------------------------
# Capa 2: heurísticas de densidad
# ---------------------------------------------------------------------------

def _densidad_enlaces(nodo):
    """Ratio de caracteres dentro de <a> sobre el total del nodo."""
    texto_total = nodo.get_text(" ", strip=True)
    if not texto_total:
        return 1.0
    texto_enlaces = " ".join(a.get_text(" ", strip=True) for a in nodo.find_all("a"))
    return len(texto_enlaces) / max(len(texto_total), 1)


def _eliminar_por_heuristica(soup, umbral_densidad=0.6, min_enlaces=4):
    """Elimina contenedores que se comportan como menús: mucha densidad de
    enlaces y poco texto propio. No toca nodos con bloques de código o tablas,
    que sí son contenido aunque contengan enlaces."""
    for nodo in soup.find_all(["div", "ul", "ol", "section", "span"]):
        if not nodo.parent:  # ya eliminado en una pasada previa
            continue
        if nodo.find(["pre", "code", "table"]):
            continue

        enlaces = nodo.find_all("a")
        if len(enlaces) < min_enlaces:
            continue

        if _densidad_enlaces(nodo) >= umbral_densidad:
            nodo.decompose()

    return soup


def _seleccionar_raiz_contenido(soup):
    """Escoge el contenedor con más texto útil entre los candidatos."""
    mejor, mejor_puntaje = None, 0
    for selector in CANDIDATOS_CONTENIDO:
        try:
            for nodo in soup.select(selector):
                puntaje = len(nodo.get_text(" ", strip=True))
                if puntaje > mejor_puntaje:
                    mejor, mejor_puntaje = nodo, puntaje
        except Exception:
            continue
    return mejor if mejor is not None else soup


# ---------------------------------------------------------------------------
# Capa 3: detección de boilerplate por frecuencia documental
# ---------------------------------------------------------------------------

RUTA_FINGERPRINTS = "logs/boilerplate_fingerprints.json"

_RE_ESPACIOS = re.compile(r"\s+")
# Solo años de 4 dígitos y fechas ISO. NO se normalizan dígitos arbitrarios:
# hacerlo colapsaba bloques legítimamente distintos que solo se diferencian
# por un número ("Paso 1" vs "Paso 2", "Release 14.5" vs "Release 15.0"), lo
# que producía falsos positivos y borraba contenido real.
_RE_ANIO = re.compile(r"\b(19|20)\d{2}\b")
_RE_FECHA_ISO = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")


def normalizar_bloque(texto):
    """Normalización conservadora: colapsa solo lo que varía por el mero paso
    del tiempo, para que '© 2025 Cisco' y '© 2026 Cisco' colisionen en el
    mismo hash sin arrastrar contenido legítimo con ellos."""
    t = texto.lower().strip()
    t = _RE_FECHA_ISO.sub("<fecha>", t)
    t = _RE_ANIO.sub("<anio>", t)
    t = _RE_ESPACIOS.sub(" ", t)
    return t


def hash_bloque(texto):
    return hashlib.sha1(normalizar_bloque(texto).encode("utf-8")).hexdigest()[:16]


def extraer_bloques(raiz):
    """Divide el contenido en bloques de texto a nivel de elemento."""
    bloques = []
    for nodo in raiz.find_all(
        ["p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "pre", "table", "blockquote", "div"]
    ):
        # Solo hojas de texto: evita contar el mismo texto en padre e hijo.
        if nodo.find(["p", "li", "pre", "table", "div"]):
            continue
        texto = nodo.get_text(" ", strip=True)
        if texto:
            bloques.append((nodo.name, texto))
    return bloques


class DetectorBoilerplate:
    """Acumula frecuencia documental de bloques y persiste los fingerprints.

    Uso en BOOTSTRAP: se llama observar() en cada página, y al final
    consolidar() calcula qué bloques son plantilla.
    Uso en INCREMENTAL: se carga el fichero y se aplica es_boilerplate()
    directamente, sin recalcular.
    """

    def __init__(self, umbral_frecuencia=0.25, min_documentos=8, max_longitud=600):
        self.contador = Counter()
        self.total_documentos = 0
        self.fingerprints = set()
        self.umbral_frecuencia = umbral_frecuencia
        self.min_documentos = min_documentos
        self.max_longitud = max_longitud

    def cargar(self, ruta=RUTA_FINGERPRINTS):
        if os.path.exists(ruta):
            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    datos = json.load(f)
                self.fingerprints = set(datos.get("fingerprints", []))
                self.contador = Counter(datos.get("contador", {}))
                self.total_documentos = datos.get("total_documentos", 0)
            except Exception:
                pass
        return self

    def guardar(self, ruta=RUTA_FINGERPRINTS):
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump({
                "fingerprints": sorted(self.fingerprints),
                "contador": dict(self.contador),
                "total_documentos": self.total_documentos,
            }, f, indent=2)

    def observar(self, bloques):
        self.total_documentos += 1
        # set() para que un bloque repetido dentro de la misma pagina cuente
        # una sola vez: medimos frecuencia DOCUMENTAL, no de termino.
        for h in {hash_bloque(t) for _, t in bloques}:
            self.contador[h] += 1

    def consolidar(self):
        if self.total_documentos < self.min_documentos:
            # Con pocos documentos la estadistica no es fiable; no marcamos nada
            # para evitar borrar contenido legitimo.
            return self.fingerprints
        limite = max(2, int(self.total_documentos * self.umbral_frecuencia))
        self.fingerprints = {h for h, c in self.contador.items() if c >= limite}
        return self.fingerprints

    def es_boilerplate(self, texto):
        if len(texto) > self.max_longitud:
            # Un bloque muy largo repetido suele ser contenido legitimo
            # (ej. una tabla de codigos de error identica en varias paginas).
            return False
        return hash_bloque(texto) in self.fingerprints


# ---------------------------------------------------------------------------
# Serialización a Markdown apto para chunking
# ---------------------------------------------------------------------------

def _tabla_a_markdown(tabla):
    filas = []
    for tr in tabla.find_all("tr"):
        celdas = [td.get_text(" ", strip=True).replace("|", "\\|")
                  for td in tr.find_all(["td", "th"])]
        if celdas:
            filas.append("| " + " | ".join(celdas) + " |")
    if len(filas) >= 1:
        cabecera = filas[0]
        n_cols = cabecera.count("|") - 1
        separador = "|" + "---|" * max(n_cols, 1)
        return "\n".join([cabecera, separador] + filas[1:])
    return ""


def bloques_a_markdown(raiz, detector=None):
    """Convierte el DOM podado a Markdown, saltando bloques marcados como
    boilerplate. Preserva código y tablas, que son señal de alto valor para
    consultas técnicas."""
    salida = []
    niveles = {"h1": "#", "h2": "##", "h3": "###", "h4": "####", "h5": "#####", "h6": "######"}

    for nombre, texto in extraer_bloques(raiz):
        if nombre == "table":
            # Se omiten aquí: se emiten abajo como Markdown real. Emitirlas
            # también aplanadas duplicaría el contenido en el índice vectorial.
            continue
        if detector is not None and detector.es_boilerplate(texto):
            continue
        if nombre in niveles:
            salida.append(f"{niveles[nombre]} {texto}")
        elif nombre == "li":
            salida.append(f"- {texto}")
        elif nombre == "pre":
            salida.append(f"```\n{texto}\n```")
        else:
            salida.append(texto)

    # Tablas por separado, con formato Markdown real.
    for tabla in raiz.find_all("table"):
        md = _tabla_a_markdown(tabla)
        if md:
            salida.append(md)

    return "\n\n".join(salida)


def sanitizar(html, selectores_extra=None, detector=None):
    """Punto de entrada. Devuelve (markdown, bloques) — los bloques se
    devuelven para alimentar al detector durante la fase BOOTSTRAP."""
    if not html:
        return "", []

    # lxml es notablemente más rápido y tolerante con HTML de SPA que html.parser.
    try:
        soup = BeautifulSoup(html, "lxml")
    except Exception:
        soup = BeautifulSoup(html, "html.parser")

    soup = _eliminar_por_estructura(soup, selectores_extra)
    soup = _eliminar_por_heuristica(soup)
    raiz = _seleccionar_raiz_contenido(soup)

    bloques = extraer_bloques(raiz)
    markdown = bloques_a_markdown(raiz, detector=detector)

    # Colapsa líneas en blanco excesivas.
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()
    return markdown, bloques
  
