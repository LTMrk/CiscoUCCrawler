# CONTEXTO_PROYECTO.md

Auditoría estática generada el 2026-08-25. Regenerar a mano si el repo cambia mucho — no se actualiza solo (a diferencia de `RESUMEN-CONOCIMIENTO.md`, que sí).

## Qué es

ETL que rastrea documentación oficial de Cisco UC/Webex, la limpia y la empaqueta para consumo por Microsoft 365 Copilot (chat sin licencia de agentes → 1 ZIP; opcionalmente agentes por producto vía SharePoint).

## Arquitectura

```
config.json (seeds, allowlists) ──▶ crawler_ai.py (orquestador)
                                        │
                    ┌───────────────────┼───────────────────┐
                    ▼                   ▼                   ▼
            openapi_ingest.py   repos_ingest.py    rastreo www.cisco.com /
            (specs Webex)       (repos GitHub)     community / help.webex /
                    │                   │           developer.cisco.com
                    │                   │                   │
                    │                   │            fetch_policy.py (rate
                    │                   │            limit, backoff, robots)
                    │                   │                   │
                    │                   │            sanitizer.py (poda ruido)
                    │                   │                   │
                    └───────────────────┴───────────────────┘
                                        ▼
                    docs/pages/ + docs/pages/openapi/ + docs/repos/
                                        │
                                        ▼
                    resumen_rag.py ──▶ RESUMEN-CONOCIMIENTO.md
                                        │
                                        ▼
                    copilot_pack.py ──▶ dist/copilot/_zips/*.zip
```

| Módulo | Líneas | Rol |
|---|---:|---|
| `copilot_pack.py` | 1.074 | Empaqueta docs/ en .txt + ZIP para Copilot (perfiles `chat`/`sharepoint`) |
| `crawler_ai.py` | 771 | Orquestador: allowlist, redirecciones 3xx, sitemaps, bucle de rastreo |
| `fetch_policy.py` | 386 | Rate limiting, backoff 429, circuit breaker, cuarentena por dominio |
| `openapi_ingest.py` | 367 | Ingesta de specs OpenAPI de Webex (GitHub, no WAF) |
| `state_store.py` | 361 | Manifiesto de estado, detección de cambios, tombstones |
| `repos_ingest.py` | 361 | Ingesta de Markdown de 29 repos GitHub curados |
| `openapi_render.py` | 345 | Operación OpenAPI → documento Markdown |
| `sanitizer.py` | 333 | Poda de ruido HTML en 3 capas (estructural/heurística/estadística) |
| `resumen_rag.py` | 244 | Genera el inventario `RESUMEN-CONOCIMIENTO.md` |
| `report.py` | 159 | Resumen de ejecución para GitHub Actions |
| `tools/probe_devnet.py` | — | Sondeo de una sola pasada (no ETL/CI), diagnostica un dominio nuevo antes de darlo de alta |

## Stack tecnológico

| Capa | Tecnología |
|---|---|
| Lenguaje | Python 3.11 |
| Rastreo | `crawl4ai` 0.9.2 + Playwright/Chromium |
| Parsing HTML | `beautifulsoup4` + `lxml` |
| Config | `config.json` + `PyYAML` |
| CI/CD | GitHub Actions (`.github/workflows/etl.yml`), 2 jobs: `process-documents` (rastreo, encadenado por presupuesto de tiempo) → `paquete-copilot` (empaquetado, solo si la frontera queda vacía) |
| Tests | `unittest`-style scripts en `tests/`, sin pytest |

## Estado actual

| Métrica | Valor |
|---|---:|
| Commits totales | 12.234 (la inmensa mayoría, `docs(incremental)` automáticos del bot) |
| Working tree | Limpio — todo commiteado |
| Corpus rastreado (`docs/pages`) | 12.230 páginas |
| Operaciones OpenAPI | 2.061 |
| Documentos de repos GitHub | 651 |
| Volumen en disco (`docs/`) | 591 MB |
| URLs pendientes en frontera | 10.550 (rastreo incompleto, se sigue encadenando) |
| Dominios con allowlist | `www.cisco.com`, `community.cisco.com`, `help.webex.com`, `developer.cisco.com` |
| Seeds | 39 |
| Repos GitHub curados | 29 (`webex/*` + `CiscoDevNet/*`) |

**Desarrollo reciente detectado (no visible en la sesión anterior de este chat):** soporte para `developer.cisco.com` — antes descartado por parecer una SPA vacía; `tools/probe_devnet.py` diagnosticó que la causa real era una redirección 301 por falta de barra final, no falta de SSR. Se añadió `hosts_barra_final` en `config.json`, manejo genérico de redirecciones 3xx en `crawler_ai.py` (`destino_redireccion`, `decidir_redireccion`, con detección de bucles y límite de saltos) y 19 tests nuevos en `test_crawler.py`.

**Pendiente / riesgos conocidos:**
- Frontera con 10.550 URLs — el corpus crecerá varios lotes más antes de estabilizarse.
- `dist/` está en `.gitignore` (correcto: son ZIPs regenerables). `graphify-out/` (grafo de dependencias de `src/`, generado con `/graphify`) **no está ignorado y ya está trackeado en git** — son artefactos derivados versionados sin necesidad; valorar añadirlo a `.gitignore` y sacarlo del árbol.
- Sin `pytest` instalado en el entorno local por defecto (los tests corren como script `python tests/test_X.py`).
