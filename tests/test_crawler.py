"""Pruebas de crawler_ai: políticas de URL, redirecciones y sitemaps.

Este fichero existe porque crawler_ai.py era el único módulo de src/ sin
ninguna cobertura: 346 sentencias al 0%. Y ahí vive justo la parte del manejo
de redirecciones que no probaba nadie — estaba verificado que un 301 se
clasificara como "redirigido" (test_pipeline) y que el estado se registrara
bien (test_pipeline), pero no que el crawler decidiera seguir el salto.

No necesita red ni navegador: crawl4ai se importa de forma diferida dentro de
deep_crawl(), así que el resto del módulo es importable tal cual. La primera
prueba verifica esa propiedad, porque es de lo que depende que este fichero
pueda correr en CI en segundos.
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "src"))

# crawler_ai lee config.json de forma relativa al directorio de trabajo.
os.chdir(RAIZ)

import crawler_ai as ca


class RespuestaFalsa:
    """Sustituto de CrawlResult de crawl4ai.

    Solo reproduce los atributos que lee el pipeline. Un doble así es lo que
    permite probar el manejo de redirecciones sin levantar un Chromium — y
    también documenta exactamente de qué campos dependemos, que es lo que hay
    que revisar si crawl4ai cambia su API.
    """

    def __init__(self, status_code=200, redirected_url=None,
                 response_headers=None, html="<html></html>", links=None):
        self.status_code = status_code
        self.redirected_url = redirected_url
        self.response_headers = response_headers or {}
        self.html = html
        self.links = links or {}


# ---------------------------------------------------------------------------

def test_crawler_importable_sin_crawl4ai():
    """El import de crawl4ai es diferido: sin esto, ni este fichero ni el
    workflow de PRs podrían correr sin descargar Playwright y un navegador."""
    assert "crawl4ai" not in sys.modules, (
        "crawler_ai importó crawl4ai al cargarse. El import debe seguir "
        "dentro de deep_crawl(); ver la nota de la cabecera del módulo.")


def test_destino_desde_redirected_url():
    """crawl4ai expone redirected_url cuando el navegador ya siguió el salto."""
    r = RespuestaFalsa(301, redirected_url="https://developer.cisco.com/docs/finesse/")
    assert ca.destino_redireccion(
        "https://developer.cisco.com/docs/finesse", r
    ) == "https://developer.cisco.com/docs/finesse/"


def test_destino_desde_cabecera_location():
    """Si redirected_url no está, se cae a la cabecera Location. Esta rama es
    la red de seguridad ante un cambio de API de crawl4ai."""
    r = RespuestaFalsa(301, response_headers={"Location": "/docs/axl/"})
    assert ca.destino_redireccion(
        "https://developer.cisco.com/docs/axl", r
    ) == "https://developer.cisco.com/docs/axl/"


def test_destino_location_relativa_y_mayusculas():
    """Location puede ser relativa, y las cabeceras HTTP no distinguen mayúsculas."""
    r = RespuestaFalsa(302, response_headers={"location": "rest-api-dev-guide"})
    assert ca.destino_redireccion(
        "https://developer.cisco.com/docs/finesse/", r
    ) == "https://developer.cisco.com/docs/finesse/rest-api-dev-guide/"


def test_destino_se_normaliza():
    """El destino pasa por normalize_url: fragmento y query fuera, barra final
    puesta en los hosts que la canonicalizan."""
    r = RespuestaFalsa(301, redirected_url="https://developer.cisco.com/docs/axl?x=1#frag")
    assert ca.destino_redireccion(
        "https://developer.cisco.com/docs/axl", r
    ) == "https://developer.cisco.com/docs/axl/"


def test_destino_ausente():
    """Un 3xx sin redirected_url ni Location no da destino: se registra, no se
    inventa uno."""
    assert ca.destino_redireccion("https://developer.cisco.com/docs/axl",
                                  RespuestaFalsa(301)) is None


def test_decision_seguir():
    accion, saltos = ca.decidir_redireccion(
        "https://developer.cisco.com/docs/finesse",
        "https://developer.cisco.com/docs/finesse/", 0)
    assert (accion, saltos) == ("seguir", 1)


def test_decision_sin_destino():
    accion, _ = ca.decidir_redireccion("https://developer.cisco.com/docs/axl", None)
    assert accion == "sin_destino"


def test_decision_bucle():
    """El caso que provocaría un bucle infinito: el origen redirige a la misma
    URL que ya teníamos normalizada."""
    u = "https://developer.cisco.com/docs/finesse/"
    accion, _ = ca.decidir_redireccion(u, u, 0)
    assert accion == "bucle"


def test_decision_corta_cadenas_largas():
    """Tope de saltos: una cadena que no converge se abandona en lugar de
    consumir el presupuesto del lote."""
    accion, saltos = ca.decidir_redireccion(
        "https://developer.cisco.com/docs/a",
        "https://developer.cisco.com/docs/axl/",
        saltos_previos=ca.MAX_SALTOS_REDIRECCION)
    assert accion == "demasiados_saltos"
    assert saltos == ca.MAX_SALTOS_REDIRECCION + 1

    # Justo por debajo del tope sí pasa.
    accion, _ = ca.decidir_redireccion(
        "https://developer.cisco.com/docs/a",
        "https://developer.cisco.com/docs/axl/",
        saltos_previos=ca.MAX_SALTOS_REDIRECCION - 1)
    assert accion == "seguir"


def test_decision_destino_fuera_de_politica():
    """Una redirección no es un salvoconducto: el destino vuelve a pasar por
    la allowlist. Sin esto, un 301 desde una URL de colaboración hacia Meraki
    metería en el corpus justo lo que la allowlist excluye."""
    accion, _ = ca.decidir_redireccion(
        "https://developer.cisco.com/docs/finesse",
        "https://developer.cisco.com/docs/meraki/", 0)
    assert accion == "no_aceptable"


def test_decision_acepta_inyeccion_de_dependencias():
    """max_saltos y es_aceptable son inyectables para poder probar ramas sin
    depender de config.json."""
    accion, _ = ca.decidir_redireccion(
        "http://a/1", "http://a/2", 0, max_saltos=99, es_aceptable=lambda u: True)
    assert accion == "seguir"


def test_sitemap_urlset():
    xml = b"""<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <url><loc>https://developer.cisco.com/docs/axl/</loc></url>
      <url><loc>https://developer.cisco.com/docs/finesse/</loc></url>
    </urlset>"""
    es_indice, locs = ca.parsear_sitemap(xml)
    assert es_indice is False
    assert locs == ["https://developer.cisco.com/docs/axl/",
                    "https://developer.cisco.com/docs/finesse/"]


def test_sitemap_index_se_distingue():
    """Un <sitemapindex> no lista páginas sino otros sitemaps. Tratarlo como
    un urlset hacía que el descubrimiento por sitemap devolviera cero URLs."""
    xml = b"""<?xml version="1.0" encoding="UTF-8"?>
    <sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <sitemap><loc>https://developer.cisco.com/sitemap-docs.xml</loc></sitemap>
      <sitemap><loc>https://developer.cisco.com/sitemap-site.xml</loc></sitemap>
    </sitemapindex>"""
    es_indice, locs = ca.parsear_sitemap(xml)
    assert es_indice is True
    assert len(locs) == 2


def test_sitemap_ignora_locs_vacias():
    xml = b"""<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <url><loc>https://developer.cisco.com/docs/axl/</loc></url>
      <url><loc></loc></url>
    </urlset>"""
    _, locs = ca.parsear_sitemap(xml)
    assert locs == ["https://developer.cisco.com/docs/axl/"]


def test_politica_de_url_real_coincide_con_test_url_policy():
    """test_url_policy.py REIMPLEMENTA la lógica de allow/block sobre
    config.json en lugar de importarla, porque hasta ahora crawler_ai no era
    importable. Eso deja una vía de deriva: la reimplementación puede seguir
    pasando mientras la función real cambia.

    Aquí se cierra: se reutilizan sus listas de URLs reales y se comprueban
    contra url_aceptable() y es_solo_descubrimiento() de verdad.
    """
    sys.path.insert(0, os.path.join(RAIZ, "tests"))
    import test_url_policy as tup

    for u in tup.DEBE_PASAR:
        assert ca.url_aceptable(u), f"url_aceptable() la rechaza: {u}"
    for u in tup.DEBE_BLOQUEAR:
        assert not ca.url_aceptable(u), f"url_aceptable() la admite: {u}"
    for u in tup.SOLO_DESCUBRIMIENTO:
        assert ca.es_solo_descubrimiento(u), f"no marcada como descubrimiento: {u}"
    for u in tup.NO_SOLO_DESCUBRIMIENTO:
        assert not ca.es_solo_descubrimiento(u), f"marcada por error: {u}"
    for entrada, esperada in tup.CANONICALIZACION:
        assert ca.normalize_url(entrada) == esperada, entrada


def test_profundidad_por_dominio():
    """developer.cisco.com necesita 3: /docs/ -> doc-set -> página -> subpágina."""
    assert ca.get_max_depth_for_url("https://developer.cisco.com/docs/axl/") == 3
    assert ca.get_max_depth_for_url("https://community.cisco.com/t5/x/ta-p/1") == 1
    # Un dominio no declarado cae al valor por defecto.
    assert (ca.get_max_depth_for_url("https://ejemplo.invalid/x")
            == ca.GS.get("default_max_depth", 1))


def test_comportamiento_personalizado_de_devnet():
    """developer.cisco.com tiene una espera de hidratación declarada; el resto
    de dominios recibe la espera por defecto. En ambos casos se antepone la
    purga por JS de los selectores de ruido."""
    css, js = ca.get_custom_behavior("https://developer.cisco.com/docs/axl/")
    assert "setTimeout" in js
    if ca.SELECTORES_RUIDO_CSS:
        assert "querySelectorAll" in js

    declarado = [c["js_code"] for c in ca.CONFIG["custom_behaviors"]
                 if c["pattern"] == "developer.cisco.com"]
    assert declarado and declarado[0] in js


def test_config_declara_developer_cisco_com():
    """Contrato de configuración: si alguien quita la allowlist del dominio,
    esta_en_allowlist() vuelve a 'todo permitido' para él y el corpus se llena
    de Meraki, DNA Center y Code Exchange."""
    with open(os.path.join(RAIZ, "config.json"), encoding="utf-8") as fh:
        cfg = json.load(fh)
    assert "developer.cisco.com" in cfg["path_allowlist_regex"]
    assert "developer.cisco.com" in (
        cfg["global_settings"].get("hosts_barra_final") or [])


if __name__ == "__main__":
    pruebas = [v for k, v in sorted(globals().items())
               if k.startswith("test_") and callable(v)]
    for prueba in pruebas:
        prueba()
        print(f"  OK {prueba.__name__}")
    print(f"\n{len(pruebas)} PRUEBAS PASARON")
