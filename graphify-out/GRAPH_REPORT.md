# Graph Report - src  (2026-08-24)

## Corpus Check
- Corpus is ~16,066 words - fits in a single context window. You may not need a graph.

## Summary
- 254 nodes · 431 edges · 10 communities (9 shown, 1 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Empaquetado para Copilot
- Ingesta de Repos GitHub
- Politica de Acceso y Reintentos
- Orquestador del Crawler
- Sanitizacion de HTML
- Ingesta de Specs OpenAPI
- Renderizado de Operaciones API
- Resumen de Ejecucion CI
- Fachada de Politica de Acceso
- Union-Find de Duplicados

## God Nodes (most connected - your core abstractions)
1. `deep_crawl()` - 19 edges
2. `ManifestStore` - 18 edges
3. `ahora()` - 15 edges
4. `ingerir_openapi()` - 14 edges
5. `iso()` - 14 edges
6. `ingerir_repos()` - 12 edges
7. `recolectar()` - 11 edges
8. `PoliticaAcceso` - 10 edges
9. `operacion_a_markdown()` - 10 edges
10. `DetectorBoilerplate` - 10 edges

## Surprising Connections (you probably didn't know these)
- `deep_crawl()` --calls--> `PoliticaAcceso`  [EXTRACTED]
  crawler_ai.py → fetch_policy.py
- `deep_crawl()` --calls--> `ingerir_openapi()`  [EXTRACTED]
  crawler_ai.py → openapi_ingest.py
- `deep_crawl()` --calls--> `ingerir_repos()`  [EXTRACTED]
  crawler_ai.py → repos_ingest.py
- `deep_crawl()` --calls--> `generar()`  [EXTRACTED]
  crawler_ai.py → resumen_rag.py
- `deep_crawl()` --calls--> `DetectorBoilerplate`  [EXTRACTED]
  crawler_ai.py → sanitizer.py

## Import Cycles
- None detected.

## Communities (10 total, 1 thin omitted)

### Community 0 - "Empaquetado para Copilot"
Cohesion: 0.06
Nodes (55): a_texto_plano(), _celdas(), clasificar_producto(), clave_version(), comprimir(), comprimir_todo(), _emitir(), empaquetar() (+47 more)

### Community 1 - "Ingesta de Repos GitHub"
Cohesion: 0.07
Nodes (36): _cargar_estado(), _documento(), _es_ingerible(), _ficheros_del_repo(), _get_json(), _get_texto(), _guardar_estado(), ingerir_repos() (+28 more)

### Community 2 - "Politica de Acceso y Reintentos"
Cohesion: 0.08
Nodes (12): BackoffPolicy, CircuitBreaker, Cuarentena, RateLimiter, fetch_policy.py — Política de acceso responsable y manejo de 403 / 429. POSTURA…, robots.txt suele declarar los sitemaps: la vía de descubrimiento que el…, Token bucket por dominio. Serializa las peticiones a un mismo host aunque el…, Backoff exponencial con jitter completo, honrando Retry-After. (+4 more)

### Community 3 - "Orquestador del Crawler"
Cohesion: 0.14
Nodes (26): _compilar(), deep_crawl(), descubrir_por_sitemap(), es_solo_descubrimiento(), esta_en_allowlist(), get_custom_behavior(), get_max_depth_for_url(), git_commit_and_push() (+18 more)

### Community 4 - "Sanitizacion de HTML"
Cohesion: 0.11
Nodes (20): bloques_a_markdown(), _densidad_enlaces(), DetectorBoilerplate, _eliminar_por_estructura(), _eliminar_por_heuristica(), extraer_bloques(), hash_bloque(), normalizar_bloque() (+12 more)

### Community 5 - "Ingesta de Specs OpenAPI"
Cohesion: 0.20
Nodes (15): _cargar_estado(), _get_json(), _get_texto(), _guardar_estado(), ingerir_openapi(), _migrar_estado(), _operaciones_de(), _parsear_spec() (+7 more)

### Community 6 - "Renderizado de Operaciones API"
Cohesion: 0.22
Nodes (15): _bloque_json(), _deref(), describir_schema(), extraer_ejemplos(), extraer_scopes(), operacion_a_markdown(), openapi_render.py — Conversión de una operación OpenAPI a documento RAG. QUÉ SE…, Recoge ejemplos tanto de `example` (legado) como de `examples` (mapa con… (+7 more)

### Community 7 - "Resumen de Ejecucion CI"
Cohesion: 0.31
Nodes (10): construir_resumen(), _contar(), _leer(), main(), report.py — Genera el resumen de la ejecución para GITHUB_STEP_SUMMARY. Vive en…, El esquema v1 guardaba `operaciones` como int y el v2 como dict. El reporte…, _seccion_cuarentena(), _seccion_inventario() (+2 more)

### Community 8 - "Fachada de Politica de Acceso"
Cohesion: 0.20
Nodes (5): PoliticaAcceso, Fachada que agrupa las cuatro piezas y decide antes de cada petición., Devuelve (permitido: bool, motivo: str)., HEAD condicional barato ANTES de levantar el navegador. Por qué existe: las…, Clasifica el resultado. Devuelve una de: 'ok' | 'no_modificado' | 'reintentar'…

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ManifestStore` connect `Ingesta de Repos GitHub` to `Orquestador del Crawler`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Why does `deep_crawl()` connect `Orquestador del Crawler` to `Empaquetado para Copilot`, `Ingesta de Repos GitHub`, `Sanitizacion de HTML`, `Ingesta de Specs OpenAPI`, `Fachada de Politica de Acceso`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Why does `PoliticaAcceso` connect `Fachada de Politica de Acceso` to `Politica de Acceso y Reintentos`, `Orquestador del Crawler`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Should `Empaquetado para Copilot` be split into smaller, more focused modules?**
  _Cohesion score 0.06140350877192982 - nodes in this community are weakly interconnected._
- **Should `Ingesta de Repos GitHub` be split into smaller, more focused modules?**
  _Cohesion score 0.06894049346879536 - nodes in this community are weakly interconnected._
- **Should `Politica de Acceso y Reintentos` be split into smaller, more focused modules?**
  _Cohesion score 0.07661290322580645 - nodes in this community are weakly interconnected._
- **Should `Orquestador del Crawler` be split into smaller, more focused modules?**
  _Cohesion score 0.1396011396011396 - nodes in this community are weakly interconnected._