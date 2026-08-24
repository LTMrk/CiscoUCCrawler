# CiscoUCCrawler

Pipeline ETL que construye y mantiene una base de conocimiento sobre **Cisco
Unified Communications y Webex**, lista para alimentar un RAG (Retrieval-
Augmented Generation) — en concreto, agentes especialistas de M365 Copilot.

No es un scraper puntual. Corre semanalmente vía GitHub Actions, detecta
cambios, actualiza lo modificado, retira lo que ha desaparecido en origen y
deja un inventario legible de qué sabe en cada momento.

## Para qué sirve

Un agente de soporte de Cisco UC necesita responder con precisión sobre
CUCM, Unity Connection, Expressway, Contact Center, gateways de voz y las
APIs de Webex — y que la respuesta cite una fuente real, no que el modelo
improvise sobre su conocimiento general (que suele ir desactualizado y no
distingue versiones).

Este repositorio resuelve la parte de **adquisición y preparación del
conocimiento**:

1. Rastrea la documentación oficial de Cisco, evitando ruido (menús,
   banners, guías de usuario final, marketing).
2. Ingiere la referencia de API de Webex desde specs OpenAPI oficiales.
3. Ingiere documentación de integración desde repositorios GitHub curados
   (SDKs, ejemplos de código).
4. Detecta y descarta duplicados entre versiones de una misma guía.
5. Empaqueta el resultado en el formato que un agente de M365 Copilot puede
   consumir de verdad.
6. Publica un inventario (`RESUMEN-CONOCIMIENTO.md`) que dice, en cada
   ejecución, qué cubre el corpus y qué falta.

## Fuentes de información

| Fuente | Qué aporta | Cómo se accede |
|---|---|---|
| **www.cisco.com** (`/td/docs/`, `/support/`) | Guías de administración, configuración, troubleshooting, diseño (CVD/SRND) y command reference de CUCM, Unity Connection, Expressway, Contact Center (UCCE/UCCX/CVP/Finesse), gateways de voz (CUBE, VG, SRST) y endpoints | Rastreo con `crawl4ai` + Playwright, con **allowlist de rutas por dominio** (deny-by-default: solo entra lo declarado útil) |
| **community.cisco.com** | Artículos técnicos curados (knowledge base) | Solo `/ta-p/` (artículos), nunca hilos de discusión sin validar |
| **help.webex.com** | Documentación de producto de Webex | Rastreo acotado a `/article/` |
| **github.com/webex/webex-openapi-specs** | Especificación completa de las APIs REST de Webex (Cloud Calling, Contact Center, Messaging, Meetings, Admin, Device...) | Fuente estructurada, licencia CC-BY-4.0. Es el mismo pipeline que usa Cisco para publicar developer.webex.com, así que no va por detrás |
| **github.com/webex/** y **github.com/CiscoDevNet/** (lista curada) | Documentación de integración: cómo se autentica un SDK, qué devuelve un widget, ejemplos de AXL/CUPI/CVP/Finesse | Markdown de 29 repositorios seleccionados, filtrando ficheros de gobernanza (LICENSE, CHANGELOG) y código generado |

### Lo que se excluye deliberadamente

- **developer.webex.com y developer.cisco.com**: son aplicaciones
  JavaScript que devuelven un shell vacío al rastreo; la referencia de API
  se obtiene de los OpenAPI oficiales en su lugar.
- **Productos en fin de vida** (p. ej. Webex Experience Management) y
  **repositorios deprecados** por su propio README: documentar algo
  retirado produce respuestas activamente incorrectas.
- **Guías de usuario final** y páginas de marketing: compiten como ruido
  vectorial con la documentación técnica real.
- **Otros idiomas**: solo `en-us`.

La lista completa de qué entra y por qué está en `config.json`, con el
motivo documentado en cada exclusión.

## Cómo se mantiene actualizado

El corpus no es una foto fija. En cada ejecución:

- Se compara el hash del contenido sanitizado contra la última visita; solo
  se reescribe lo que cambió.
- Un documento que desaparece de origen se borra del corpus (*tombstone*),
  para que el RAG no siga citando algo retirado.
- Los deltas (`+nuevos ~modificados -retirados`) quedan en `logs/` y en el
  resumen de cada ejecución de GitHub Actions.

## Pipeline

El workflow (`.github/workflows/etl.yml`) tiene dos jobs. El primero hace la
ingesta y corre semanalmente, con presupuesto de tiempo acotado por lote: si
queda trabajo pendiente, encadena la siguiente ejecución en vez de perder lo
avanzado. El segundo empaqueta el resultado, y solo se dispara cuando el
primero termina sin dejar trabajo pendiente.

```
job "process-documents"                       job "paquete-copilot"
────────────────────────                      ─────────────────────
config.json (seeds, allowlists)
        │
        ▼
crawler_ai.py ──┬── openapi_ingest.py   (specs de Webex)
                ├── repos_ingest.py     (repos GitHub curados)
                └── rastreo www.cisco.com / community / help.webex.com
                         │
                         ▼
                  sanitizer.py  (poda de ruido: nav, banners, boilerplate)
                         │
                         ▼
                  docs/pages/ + docs/repos/   (corpus en Markdown)
                         │
                         ▼
                  resumen_rag.py                  ──▶  copilot_pack.py
                  → RESUMEN-CONOCIMIENTO.md              → dist/copilot/  (paquete para el agente)
```

## Estructura del repositorio

```
src/
  crawler_ai.py       orquestador del pipeline
  fetch_policy.py      rate limiting, backoff, respeto de robots.txt
  sanitizer.py          poda de ruido del HTML (3 capas: estructural, heurística, estadística)
  state_store.py        manifiesto de estado, detección de cambios, tombstones
  openapi_ingest.py      ingesta de specs OpenAPI de Webex
  openapi_render.py       conversión de operación OpenAPI a documento
  repos_ingest.py         ingesta de Markdown desde repos GitHub curados
  resumen_rag.py           genera RESUMEN-CONOCIMIENTO.md
  copilot_pack.py           empaqueta el corpus para un agente de M365 Copilot
  report.py                  resumen de la ejecución para GitHub Actions

config.json            seeds, allowlists, blocklists, listas curadas de repos y specs
docs/pages/             corpus rastreado de cisco.com / community / help.webex.com
docs/repos/             corpus ingerido de repositorios GitHub
logs/                   estado, deltas y diagnóstico de cada ejecución
tests/                  pruebas de regresión (contrato de config, políticas de URL, extractores)
RESUMEN-CONOCIMIENTO.md inventario del corpus, se regenera en cada ejecución
```

## Principios de diseño

- **Sin evasión de bots.** Se respeta `robots.txt`, se hace backoff ante
  429 y se retrocede ante 403 en vez de camuflar el tráfico.
- **Deny-by-default.** En dominios grandes (cisco.com tiene millones de
  URLs) solo se rastrea lo declarado explícitamente útil, no lo que no está
  bloqueado.
- **Nada se pierde en silencio.** Fallos de red, cuota de API agotada o
  contenido retirado quedan registrados y son recuperables en la siguiente
  ejecución, no se tragan.
- **El corpus se audita solo.** `RESUMEN-CONOCIMIENTO.md` es la fuente de
  verdad sobre qué cubre el agente hoy, versionada junto al contenido que
  describe.
