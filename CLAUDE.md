# CiscoUCCrawler

ETL que construye un corpus RAG sobre Cisco UC y Webex para Microsoft 365
Copilot. Corre en GitHub Actions, es incremental y se encadena solo.

Todo el código y los comentarios están en español. Mantenlo así.

## Cómo se ejecuta

Siempre desde la raíz del repo: las rutas de config y estado son relativas.

```bash
python3 src/crawler_ai.py          # pipeline completo (env MINUTOS_LIMITE)
python3 src/resumen_rag.py         # regenera RESUMEN-CONOCIMIENTO.md
python3 src/copilot_pack.py --fuente devnet --zip   # ZIP solo de DevNet
python3 tools/probe_devnet.py      # sondeo de developer.cisco.com (necesita red)
```

Las 7 pruebas no usan pytest; cada fichero es un script:

```bash
for t in tests/test_*.py; do python3 "$t" || break; done
```

Si añades un fichero de pruebas, regístralo **en los dos sitios**:
`.github/workflows/tests.yml` y `.github/workflows/etl.yml`.

## Cosas que no se deducen del código

**crawl4ai se importa dentro de `deep_crawl()`, no arriba.** Es lo que hace
`crawler_ai` importable sin Playwright y lo que permite que CI tarde 20
segundos. `tests.yml` falla a propósito si alguien lo sube al nivel de
módulo. No lo muevas.

**developer.cisco.com canonicaliza CON barra final.** Quitarla provoca un
301 en cada URL. Está cubierto por `global_settings.hosts_barra_final` y la
rama 3xx de `fetch_policy.tras_respuesta`. El README afirmaba durante meses
que ese dominio era "una SPA que devuelve un shell vacío": era falso, y por
esa creencia se perdieron 127 URLs de Finesse, CVP, PCCE y UCCX.

**El índice de `/docs/` lo construye JavaScript**: rastrearlo no descubre
ningún doc-set. El descubrimiento va por el sitemap de PubHub, declarado en
`config.sitemaps`.

**`robots.txt` de DevNet prohíbe `/web/`**, donde viven las versiones legacy
de CURRI, SXML, JTAPI y TAPI. Pero `/site/curri/` y `/site/sxml/` SÍ están
permitidos y son los equivalentes vigentes. No confundas las dos rutas.

**Las semillas se encolan ANTES de la frontera arrastrada.** Al revés
quedaban detrás de 7.000 URLs: 62 lotes, más de once horas, y la frontera
crece por el camino.

## Cómo verificar que un lote hizo algo

**No mires `logs/error.log` para las redirecciones.** Solo recibe
`log_error`; los aciertos salen por `log_info`, que es `print()` a stdout.
Mira el resumen del job en Actions, que trae el recuento de redirecciones
seguidas y de URLs encoladas desde semillas. Alternativa persistente:

```bash
python3 -c "import json; m=json.load(open('logs/manifest.json'))['entradas']; \
print(sum(1 for v in m.values() if v.get('status')=='redirect'))"
```

Dos veces en el desarrollo una configuración correcta no hizo nada por cómo
se consumía, y el síntoma fue **silencio, no error**. Ante "no aparece lo que
debería", sospecha del consumo antes que de las regex.

## Estado y pendientes

- El ETL se auto-encadena cada ~11 min porque la frontera no converge
  (`logs/more_work.flag`). Consume minutos de runner indefinidamente. Sin
  resolver.
- `docs/cmse` de DevNet sigue sin identificar; fuera de la allowlist hasta
  confirmarlo.
- `deep_crawl()` no tiene cobertura: es el bucle de E/S. Sus decisiones sí
  están extraídas y probadas (`decidir_redireccion`, `parsear_sitemap`).
- 365 URLs en cuarentena por 403, casi todas de `bst.cloudapps.cisco.com`.
  Ruido antiguo, ajeno al rastreo de colaboración.

## Convenciones

- Deny-by-default: en dominios grandes solo entra lo declarado en
  `path_allowlist_regex`. `esta_en_allowlist` usa `.match()` (anclado);
  `blocked_regex` usa `.search()`.
- Sin evasión de bots: se respeta `robots.txt`, se hace backoff ante 429 y
  se retrocede ante 403.
- Un doc-set admitido pero sin mapear en `copilot_pack.DOCSETS_DEVNET` cae
  en "misc", que es donde el agente no lo encuentra. Allowlist y taxonomía
  se tocan a la vez.
- Los ficheros de `logs/` son estado generado. Ante un conflicto de merge,
  toma la versión de `main` y reaplica el filtro; no los fusiones a mano.

## Skills

`.claude/skills/` trae caveman, ponytail y superpowers vendorizados (MIT).
Ver `.claude/skills/README.md` para origen, licencias y cómo actualizarlos.
