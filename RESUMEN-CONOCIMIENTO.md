# Conocimiento indexado por CiscoUCCrawler

Inventario de lo que contiene el corpus RAG. Lo regenera `src/resumen_rag.py` en cada ejecución del ETL: **no editar a mano**.

Actualizado: 2026-08-24 16:32 UTC

## Totales

| Concepto | Valor |
|---|---:|
| Documentación de producto | 12.085 documentos |
| Operaciones de API (OpenAPI) | 2.061 |
| Documentación de repositorios | 651 documentos |
| Volumen total | 562.8 M caracteres |
| URLs pendientes de rastrear | 6.864 |

> El rastreo **no ha terminado**: quedan 6.864 URLs en la frontera. Las cifras de abajo son cobertura parcial y crecerán en las siguientes ejecuciones.

## Cobertura por producto

| Producto | Documentos | Guías distintas | Versiones | M caracteres |
|---|---:|---:|---|---:|
| Cisco Unified Communications Manager (CUCM) | 2.991 | 698 | 12.5.1 (555), 15 (294), 12.5.1SU4 (282) | 157.1 |
| Cisco Unified/Packaged Contact Center Enterprise (UCCE, PCCE, ICM) | 1.665 | 785 | 12.5.1 (432), 15.0.1 (416), 12.6.1 (413) | 99.5 |
| Cisco Unity Connection | 1.396 | 266 | 15 (408), 14 (273), 12X (273) | 76.0 |
| Cisco Unified CVP, Finesse y CUIC | 1.109 | 692 | 15.0.1 (208), 12.6 (186), 12.6.2 (177) | 38.0 |
| Cisco IM and Presence Service y Jabber | 1.267 | 331 | 12.5.1 (151), 12.8 (73), 12.6 (72) | 36.7 |
| Cisco Unified Contact Center Express (UCCX) | 600 | 246 | 12.5 (150), 12.5.1SU1 (131), 15.0 (114) | 33.9 |
| Cisco Expressway, MRA y VCS | 790 | 254 | X14-0 (113), X14-0-2 (76), X15-0 (73) | 32.5 |
| Telefonos IP y endpoints de TelePresence | 949 | 412 | 10.0 (46), 10.3.1 (28), 9.1.1 (14) | 31.5 |
| Cisco CUBE, IOS Voice y SIP | 233 | 205 | — | 14.8 |
| Documentos varios de colaboracion Cisco | 617 | 388 | 1.1 (49), 19X (43), 12.5 (23) | 12.5 |
| Contact Center (otros componentes) | 193 | 106 | 12.5 (44), 12.5.1 (42), 12.6.2 (27) | 4.5 |
| Guias de diseno (CVD, SRND, Preferred Architecture) | 93 | 65 | 12X (21), 14 (20) | 3.4 |
| Webex Cloud, Control Hub y Webex Calling | 70 | 49 | — | 1.7 |
| Cisco Meeting Server y conferencing | 105 | 105 | — | 1.0 |
| Business Edition, UC on UCS y plataforma | 7 | 7 | — | 0.1 |

La columna *Guías distintas* cuenta familias documentales, es decir guías únicas ignorando la versión. Un número muy inferior al de documentos indica que el corpus tiene varias releases de la misma guía.

## APIs REST de Webex

| API | Operaciones | M caracteres |
|---|---:|---:|
| Webex Cloud Calling | 1.091 | 6.73 |
| Webex Contact Center | 449 | 2.91 |
| Webex Meetings | 171 | 1.57 |
| Webex Admin | 148 | 1.02 |
| Webex Device | 101 | 0.71 |
| Webex Messaging | 63 | 0.42 |
| Webex Broadworks Calling | 19 | 0.09 |
| Webex Wholesale | 18 | 0.10 |
| Webex for UCM | 1 | 0.00 |

## Documentación de repositorios GitHub

| Repositorio | Documentos | M caracteres |
|---|---:|---:|
| `webex/webex-js-sdk` | 262 | 2.99 |
| `webex/widgets` | 105 | 1.45 |
| `webex/WebexPlaybooks` | 94 | 0.59 |
| `webex/components` | 32 | 0.15 |
| `CiscoDevNet/cvp-sample-code` | 27 | 0.12 |
| `CiscoDevNet/finesse-sample-code` | 26 | 0.14 |
| `webex/webex-byova-gateway-python` | 25 | 0.29 |
| `CiscoDevNet/webexcc-digital-channels` | 19 | 0.10 |
| `CiscoDevNet/webex-contact-center-widget-starter` | 16 | 0.05 |
| `CiscoDevNet/xapi-samples` | 15 | 0.02 |
| `webex/dataSourceSchemas` | 5 | 0.04 |
| `webex/react-widgets` | 3 | 0.01 |
| `webex/postman-webex-calling` | 3 | 0.01 |
| `CiscoDevNet/voice-gateway-api-tcl-vxml-sample-scripts` | 2 | 0.01 |
| `webex/sdk-component-adapter` | 2 | 0.01 |
| `CiscoDevNet/axl-ansible-examples` | 2 | 0.01 |
| `webex/webex-android-sdk` | 1 | 0.00 |
| `CiscoDevNet/serviceability-python-zeep-samples` | 1 | 0.00 |
| `CiscoDevNet/axl-python-zeep-samples` | 1 | 0.01 |
| `CiscoDevNet/unity-connection-apis-python-samples` | 1 | 0.00 |
| `webex/EmbeddedAppKitchenSink` | 1 | 0.01 |
| `CiscoDevNet/jabber-web-sample` | 1 | 0.00 |
| `webex/postman-webex-meetings` | 1 | 0.01 |
| `webex/webexconnect-javascript-sdk` | 1 | 0.00 |
| `CiscoDevNet/xe-sip-api-code` | 1 | 0.01 |
| `webex/webexconnect-android-sdk` | 1 | 0.00 |
| `webex/webexconnect-ios-sdk` | 1 | 0.00 |
| `webex/webex-ios-sdk` | 1 | 0.00 |
| `webex/webex-java-sdk` | 1 | 0.01 |

## Qué NO está cubierto

Decisiones deliberadas, documentadas en `config.json`:

- **developer.webex.com**: la referencia de API se obtiene de los OpenAPI oficiales en su lugar (`webex-openapi-specs`), que es el mismo origen del que se publica ese portal.
- **De developer.cisco.com, todo lo que no es colaboración**: Meraki, DNA Center, SD-WAN, NSO, Crosswork, XDR, Spaces, UCS/HyperFlex y PSIRT quedan fuera por allowlist. También `/codeexchange/`, que duplica la ingesta de repositorios de GitHub, y `/web/`, que el `robots.txt` del sitio prohíbe.
- **Productos en EoL** (Webex Experience Management) y **repos deprecados** (`spark-ios-sdk`, `spark-android-sdk`): documentar algo retirado produce respuestas activamente incorrectas.
- **Guías de usuario final** y páginas de marketing: son ruido vectorial que compite con la documentación técnica.
- **Hilos de foro sin validar**: de community.cisco.com solo entran los artículos curados (`/ta-p/`), no las discusiones.
