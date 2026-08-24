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


DOCSETS_COLABORACION = [
    # Revisados uno a uno sobre el inventario del sitemap de PubHub
    # (sondeo del 2026-08-24: 339 doc-sets, 312 fuera de la allowlist inicial).
    "docs/axl-schema-reference", "docs/broadworks", "docs/cisco-meeting-server",
    "docs/enterprise-icm-vru-interface-specification",
    "docs/extension-mobility-api", "docs/jabber-web",
    "docs/multiplatform-phones", "docs/user-data-services",
    "docs/webdialer", "docs/webdialer-docs", "docs/webex-calling",
    "docs/webex-connect-partner-resources", "docs/webex-meetings",
    "docs/webex-xml-api-reference-guide",
    "site/cti-protocol", "site/ctios", "site/curri",
    "site/enterprise-chat-and-email", "site/im-and-presence",
    "site/jabber-guestsdk", "site/packaged-contact-center",
    "site/uc-express-services", "site/uc-gateway-services",
    "site/uc-manager-sip", "site/user-data-services",
    "site/webex-developer", "site/webex-integration",
    # SXML vive en /docs/ ademas de /site/, y PAWS es la API de instalacion y
    # upgrade de CUCM y Unity. Ninguno de los dos estaba declarado.
    "docs/sxml", "site/paws",
]

# Muestra de lo que el mismo inventario dejaba fuera y debe seguir fuera: son
# la mayor parte del portal.
DOCSETS_AJENOS = [
    "docs/catalyst-center", "docs/nexus-dashboard", "docs/sdwan", "docs/aci",
    "docs/crosswork", "docs/cisco-xdr", "docs/firepower", "docs/intersight",
    "docs/pyats", "docs/nso", "docs/appdynamics", "docs/cyber-vision",
    "docs/thousandeyes", "docs/iox", "docs/modeling-labs",
    "docs/identity-services-engine", "docs/stealthwatch",
    "docs/secure-endpoint", "docs/support-apis", "docs/psirt",
    "docs/sandbox", "docs/licenses",
    "site/aci", "site/security", "site/sandbox", "site/index", "site/archive",
    "site/nso", "site/appdynamics", "site/meraki-dashboard-demo",
    "site/zero-trust", "site/networking",
    # Producto retirado por Cisco en 2019: documentar algo muerto produce
    # respuestas activamente incorrectas, que es el criterio del proyecto.
    "docs/context-service", "site/context-service",
]


def test_allowlist_admite_toda_la_colaboracion_del_sitemap():
    for ruta in DOCSETS_COLABORACION:
        u = f"https://developer.cisco.com/{ruta}/"
        assert ca.url_aceptable(u), f"la allowlist rechaza colaboracion: {ruta}"


def test_allowlist_rechaza_el_resto_del_portal():
    for ruta in DOCSETS_AJENOS:
        u = f"https://developer.cisco.com/{ruta}/"
        assert not ca.url_aceptable(u), f"la allowlist admite lo ajeno: {ruta}"


def test_ningun_docset_de_colaboracion_cae_en_misc():
    """Un doc-set admitido pero sin clasificar acaba en "Documentos varios",
    que es justo donde el agente no lo encuentra al preguntar por su producto.
    """
    sys.path.insert(0, os.path.join(RAIZ, "src"))
    from copilot_pack import clasificar_producto

    sin_clasificar = [
        ruta for ruta in DOCSETS_COLABORACION
        if clasificar_producto(f"https://developer.cisco.com/{ruta}/") == "misc"
    ]
    assert not sin_clasificar, f"caen en misc: {sin_clasificar}"


def test_allowlist_filtra_el_sitemap_de_pubhub():
    """URLs reales del sitemap de PubHub (sondeo del 2026-08-24).

    Ese sitemap trae 449 URLs de /docs/ y /site/, pero la mayoria no son de
    colaboracion: cubre todo DevNet. Es justo el trabajo de la allowlist
    dejar pasar unas y no otras, asi que se comprueba con ejemplos de ambas.
    """
    admitidas = [
        "https://developer.cisco.com/site/sxml/",
        "https://developer.cisco.com/docs/axl/",
        "https://developer.cisco.com/docs/contact-center-express/",
    ]
    rechazadas = [
        "https://developer.cisco.com/docs/cisco-nexus-openconfig-yang-release-10-1x/",
        "https://developer.cisco.com/docs/legacy-umbrella-api/",
        "https://developer.cisco.com/site/security/",
        "https://developer.cisco.com/docs/appdynamics/agent-installer-platform-service/",
        "https://developer.cisco.com/site/zero-trust/",
        "https://developer.cisco.com/docs/cisco-spaces-firehose/api/",
        "https://developer.cisco.com/docs/nx-api-dme-model-9-3-1-reference/",
        "https://developer.cisco.com/docs/quick-start-cloud-security-api/",
        "https://developer.cisco.com/site/network-visibility-module/",
        "https://developer.cisco.com/site/nso/video/",
    ]
    for u in admitidas:
        assert ca.url_aceptable(u), f"la allowlist rechaza colaboracion: {u}"
    for u in rechazadas:
        assert not ca.url_aceptable(u), f"la allowlist admite lo ajeno: {u}"


def test_sitemap_de_pubhub_declarado():
    """El indice de /docs/ lo construye JavaScript y no enlaza nada en el HTML
    crudo (0 doc-sets encontrados en el sondeo). Sin este sitemap declarado no
    hay forma de descubrir los doc-sets: solo entrarian las semillas."""
    with open(os.path.join(RAIZ, "config.json"), encoding="utf-8") as fh:
        cfg = json.load(fh)
    assert any("pubhub" in s for s in cfg["sitemaps"]), \
        "falta el sitemap de PubHub en config.sitemaps"


def test_semillas_devnet_vivas():
    """/docs/jabber-bots devolvia 404 en el sondeo: el doc-set desaparecio.
    Una semilla muerta se reencola y falla en cada ejecucion."""
    with open(os.path.join(RAIZ, "config.json"), encoding="utf-8") as fh:
        semillas = json.load(fh)["seeds"]
    assert not any("jabber-bots" in s for s in semillas), \
        "jabber-bots devuelve 404: no debe ser semilla"
    devnet = [s for s in semillas if "developer.cisco.com" in s]
    assert devnet, "no quedan semillas de developer.cisco.com"
    for s in devnet:
        assert ca.url_aceptable(s), f"semilla que la propia allowlist rechaza: {s}"
        assert ca.normalize_url(s) == s, f"semilla no canonica (barra final): {s}"


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
