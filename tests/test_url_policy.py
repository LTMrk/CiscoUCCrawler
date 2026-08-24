"""Valida path_allowlist_regex / blocked_regex / discovery_only_regex contra
URLs reales de cisco.com, community.cisco.com y help.webex.com."""
import json
import os
import re
import sys
from urllib.parse import urlparse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "src"))

# fetch_policy no importa crawl4ai, asi que la canonicalizacion se prueba de
# verdad en lugar de reimplementarla como el resto de este fichero.
from fetch_policy import canonicalizar_url

CONFIG = json.load(open(os.path.join(RAIZ, "config.json")))

HOSTS_BARRA_FINAL = CONFIG["global_settings"].get("hosts_barra_final")

ALLOW = {d: [re.compile(p) for p in ps]
         for d, ps in CONFIG["path_allowlist_regex"].items()}
BLOCK = [re.compile(p) for p in CONFIG["blocked_regex"]]
SUBSTR = CONFIG["blocked_patterns"]
DISC = [re.compile(p) for p in CONFIG["discovery_only_regex"]]


def en_allowlist(url):
    net = urlparse(url).netloc.lower()
    for dominio, patrones in ALLOW.items():
        if dominio in net:
            return any(r.match(url) for r in patrones)
    return True


def bloqueada(url):
    if any(s in url.lower() for s in SUBSTR):
        return True
    return any(r.search(url) for r in BLOCK)


def aceptada(url):
    return en_allowlist(url) and not bloqueada(url)


def solo_descubrimiento(url):
    return any(r.match(url) for r in DISC)


# URLs reales observadas en resultados de busqueda
DEBE_PASAR = [
    # Documentacion tecnica densa: el objetivo del RAG
    "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/systemConfig/cucm_b_system-configuration-guide-15.html",
    "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/systemConfig/cucm_b_system-configuration-guide-15/cucm_m_configure-enterprise-parameters-and-services.html",
    "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/systemConfig/cucm_b_system-configuration-guide-15/cucm_m_tcp-and-udp-port-usage-12-0.html",
    "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/systemConfig/cucm_b_system-configuration-guide-15/cucm_b_system-configuration-guide-14_chapter_0111.html",
    # Indices de guias (descubrimiento)
    "https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html",
    "https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html",
    "https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-15/model.html",
    "https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/series.html",
    # Articulos curados del foro
    "https://community.cisco.com/t5/networking-knowledge-base/please-help-to-find-technical-doccumentation-and-confiig/ta-p/3852613",
    # help.webex.com en sus dos formatos de articulo
    "https://help.webex.com/article/en-us/ig9wh2",
    "https://help.webex.com/en-us/article/ngcto76/End-of-Life-EoL-Announcement-for-End-Users",
    # Las cinco APIs REST de Unity Connection, no solo CUPI
    "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/APIs_Pages/b_Cisco_Unity_Connection_APIs.html",
    "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API.html",
    "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUTI_API/b_CUTI_API/b_CUTI_API_chapter_01.html",
    "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUMI_API/b_CUMI_API.html",
    "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUNI_API/b_CUNI_API.html",
    # Gateways de voz: SRST vive en voice_ip_comm, pero los VG analogicos
    # cuelgan de /td/docs/routers/access/, fuera del arbol de colaboracion.
    "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/SCCP_and_SIP_SRST_Admin_Guide/srst_overview.html",
    "https://www.cisco.com/c/en/us/td/docs/routers/access/vg450/software/configuration/guide/vg450-scg/vg450-scg_chapter_01.html",
    "https://www.cisco.com/c/en/us/td/docs/routers/access/vg400/software/configuration/guide/vg400-scg.html",
    # Ejemplos de configuracion: el tipo de documento que mas se consulta en
    # soporte y que la allowlist no contemplaba.
    "https://www.cisco.com/c/en/us/support/unified-communications/unified-border-element/products-configuration-examples-list.html",
    # developer.cisco.com (DevNet). En forma canonica, CON barra final: es la
    # que produce canonicalizar_url y la unica que el origen sirve sin 301.
    "https://developer.cisco.com/docs/axl/",
    "https://developer.cisco.com/docs/axl/axl-developer-guide/",
    "https://developer.cisco.com/docs/finesse/rest-api-dev-guide/",
    "https://developer.cisco.com/docs/contact-center-express/cti-protocol-overview/",
    "https://developer.cisco.com/docs/packaged-contact-center/api-dev-guide/",
    "https://developer.cisco.com/docs/customer-voice-portal/",
    "https://developer.cisco.com/docs/jabber-bots/",
    "https://developer.cisco.com/docs/ios-xe-voip/",
    "https://developer.cisco.com/site/unity-connection/documentation/",
    "https://developer.cisco.com/site/roomdevices/",
    "https://developer.cisco.com/site/collaboration/call-control/unified-presence/documentation/",
]

DEBE_BLOQUEAR = [
    # Colateral comercial y avisos de EoL
    "https://www.cisco.com/c/en/us/products/collateral/contact-center/webex-experience-management/a-wxm-offer-eol.html",
    "https://www.cisco.com/c/en/us/products/collateral/unified-communications/spark-flex-plan/collaboration-flex-plan3-og.html",
    "https://www.cisco.com/c/en/us/products/collateral/conferencing/webex-meeting-center/webex-work-offer-eol.html",
    "https://www.cisco.com/c/en/us/products/eos-eol-policy.html",
    "https://www.cisco.com/c/en/us/products/warranty-listing.html",
    "https://www.cisco.com/c/en/us/products/conferencing/webex-meeting-center/eos-eol-notice-listing.html",
    "https://www.cisco.com/c/en/us/products/contact-center/webex-experience-management/eos-eol-notice-listing.html",
    # Corporativo
    "https://www.cisco.com/web/about/ac227/ac228/ac231/about_cisco_takeback_recycling.html",
    "https://www.cisco.com/c/en/us/about/press/2026/example.html",
    # Guias de usuario final
    "https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-user-guide-list.html",
    # Hilos de foro sin certificar
    "https://community.cisco.com/t5/ip-telephony/cucm-sip-trunk-issue/td-p/4123456",
    "https://community.cisco.com/t5/ip-telephony/re-cucm-sip-trunk/m-p/4123457",
    # Binarios
    "https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/https/configuration/12-4t/https-12-4t-book.pdf",
    # Fuera del ambito de colaboracion (allowlist lo excluye)
    "https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/config-guide.html",
    "https://www.cisco.com/c/en/us/td/docs/security/firepower/config.html",
    "https://www.cisco.com/c/en/us/solutions/enterprise-networks/index.html",
    # Otros idiomas
    "https://www.cisco.com/c/es-es/support/unified-communications/products-list.html",
    # La regex de gateways se acota a vg\\d+: el resto del arbol de routers
    # sigue fuera. Sin esta frontera, admitir el VG450 arrastraria todo el
    # arbol de routing y switching del ISR y del Catalyst 8000.
    "https://www.cisco.com/c/en/us/td/docs/routers/access/4000/software/configuration/guide/isr4000.html",
    "https://www.cisco.com/c/en/us/td/docs/routers/access/800/software/configuration/guide/800-scg.html",
    "https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8000v/config.html",
    # Y las guias de IOS ajenas a voz tampoco entran.
    "https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr/configuration/guide/ipaddr.html",
    # developer.cisco.com fuera de colaboracion. Es la mayor parte del sitio, y
    # la razon de declarar el dominio en path_allowlist_regex: sin allowlist,
    # esta_en_allowlist() lo deja pasar todo y el corpus se llena de ruido.
    "https://developer.cisco.com/docs/meraki/",
    "https://developer.cisco.com/docs/dna-center/",
    "https://developer.cisco.com/docs/sd-wan/",
    "https://developer.cisco.com/docs/ucs-dev-center-hyperflex/",
    "https://developer.cisco.com/docs/wireless-troubleshooting-tools/",
    "https://developer.cisco.com/meraki/api-v1/",
    "https://developer.cisco.com/psirt/",
    "https://developer.cisco.com/learning/labs/collab-xapi-intro/",
    # Code Exchange: duplica repos_ingest.py y lo que habia ingerido eran
    # extensiones de AppDynamics.
    "https://developer.cisco.com/codeexchange/github/repo/Appdynamics/activemq-monitoring-extension",
    "https://developer.cisco.com/codeexchange/search",
    # robots.txt de developer.cisco.com prohibe /web/. No se entra ahi.
    "http://developer.cisco.com/web/axl/home",
    "https://developer.cisco.com/web/sip/wiki/-/wiki/Main/Requirements",
]

SOLO_DESCUBRIMIENTO = [
    "https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html",
    "https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/series.html",
    "https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-15/model.html",
    "https://help.webex.com/en-us/all-products",
    # Indices de DevNet: se recorren por sus enlaces, no se indexan. Su texto
    # es una lista de titulos y ademas renderizan vacios sin JavaScript.
    "https://developer.cisco.com/docs/",
    "https://developer.cisco.com/site/collaboration/",
]

NO_SOLO_DESCUBRIMIENTO = [
    "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/systemConfig/cucm_b_system-configuration-guide-15.html",
    "https://help.webex.com/en-us/article/ngcto76/algo",
    "https://developer.cisco.com/docs/finesse/",
    "https://developer.cisco.com/docs/axl/axl-developer-guide/",
]

# Canonicalizacion de URL. (entrada, salida esperada).
#
# Es la prueba que protege el corpus existente: si canonicalizar_url dejara de
# quitar la barra en www.cisco.com, cambiarian los doc_id de los mas de 12.000
# documentos ya rastreados (se derivan de la URL en state_store.doc_id_para) y
# el manifiesto los tomaria por documentos nuevos.
CANONICALIZACION = [
    # developer.cisco.com canonicaliza CON barra: quitarla provocaba un 301 por
    # URL, que sin rama 3xx se contaba como fallo. Causa raiz de que este
    # dominio nunca entrara en el corpus.
    ("https://developer.cisco.com/docs/finesse",
     "https://developer.cisco.com/docs/finesse/"),
    ("https://developer.cisco.com/docs/finesse/",
     "https://developer.cisco.com/docs/finesse/"),
    ("https://developer.cisco.com/docs/axl/axl-developer-guide?x=1#frag",
     "https://developer.cisco.com/docs/axl/axl-developer-guide/"),
    # La raiz y los ficheros con extension no llevan barra.
    ("https://developer.cisco.com/", "https://developer.cisco.com"),
    ("https://developer.cisco.com/docs/foo/spec.json",
     "https://developer.cisco.com/docs/foo/spec.json"),
    # Resto de dominios: comportamiento de siempre.
    ("https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/x.html",
     "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/x.html"),
    ("https://www.cisco.com/c/en/us/support/foo/",
     "https://www.cisco.com/c/en/us/support/foo"),
    ("https://help.webex.com/en-us/article/abc/#seccion",
     "https://help.webex.com/en-us/article/abc"),
]


def main():
    fallos = []

    for u in DEBE_PASAR:
        if not aceptada(u):
            motivo = "allowlist" if not en_allowlist(u) else "blocklist"
            fallos.append(f"  FALSO NEGATIVO ({motivo}): {u}")

    for u in DEBE_BLOQUEAR:
        if aceptada(u):
            fallos.append(f"  FALSO POSITIVO (deberia bloquearse): {u}")

    for u in SOLO_DESCUBRIMIENTO:
        if not solo_descubrimiento(u):
            fallos.append(f"  NO marcada como descubrimiento: {u}")

    for u in NO_SOLO_DESCUBRIMIENTO:
        if solo_descubrimiento(u):
            fallos.append(f"  Marcada como descubrimiento por error: {u}")

    for entrada, esperada in CANONICALIZACION:
        obtenida = canonicalizar_url(entrada, HOSTS_BARRA_FINAL)
        if obtenida != esperada:
            fallos.append(f"  Canonicalizacion: {entrada}\n"
                          f"      esperada  {esperada}\n"
                          f"      obtenida  {obtenida}")
        # Idempotencia: es lo que impide el ping-pong "barra si / barra no"
        # al seguir la redireccion que la propia normalizacion provoco.
        if canonicalizar_url(obtenida, HOSTS_BARRA_FINAL) != obtenida:
            fallos.append(f"  Canonicalizacion no idempotente: {obtenida}")

    total = (len(DEBE_PASAR) + len(DEBE_BLOQUEAR) + len(SOLO_DESCUBRIMIENTO)
             + len(NO_SOLO_DESCUBRIMIENTO) + len(CANONICALIZACION))

    if fallos:
        print(f"{len(fallos)} fallo(s) de {total} casos:\n")
        print("\n".join(fallos))
        sys.exit(1)

    print(f"Los {total} casos se clasifican correctamente.")
    print(f"  {len(DEBE_PASAR)} admitidas | {len(DEBE_BLOQUEAR)} bloqueadas | "
          f"{len(SOLO_DESCUBRIMIENTO)} solo-descubrimiento | "
          f"{len(CANONICALIZACION)} canonicalizaciones")


if __name__ == "__main__":
    main()
  
