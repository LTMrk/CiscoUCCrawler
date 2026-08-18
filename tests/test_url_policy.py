"""Valida path_allowlist_regex / blocked_regex / discovery_only_regex contra
URLs reales de cisco.com, community.cisco.com y help.webex.com."""
import json
import os
import re
import sys
from urllib.parse import urlparse

CONFIG = json.load(open(os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "config.json")))

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
]

SOLO_DESCUBRIMIENTO = [
    "https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html",
    "https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/series.html",
    "https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-15/model.html",
    "https://help.webex.com/en-us/all-products",
]

NO_SOLO_DESCUBRIMIENTO = [
    "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/systemConfig/cucm_b_system-configuration-guide-15.html",
    "https://help.webex.com/en-us/article/ngcto76/algo",
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

    total = (len(DEBE_PASAR) + len(DEBE_BLOQUEAR)
             + len(SOLO_DESCUBRIMIENTO) + len(NO_SOLO_DESCUBRIMIENTO))

    if fallos:
        print(f"{len(fallos)} fallo(s) de {total} casos:\n")
        print("\n".join(fallos))
        sys.exit(1)

    print(f"Las {total} URLs se clasifican correctamente.")
    print(f"  {len(DEBE_PASAR)} admitidas | {len(DEBE_BLOQUEAR)} bloqueadas | "
          f"{len(SOLO_DESCUBRIMIENTO)} solo-descubrimiento")


if __name__ == "__main__":
    main()
  
