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
python3 tools/purgar_fuera_de_allowlist.py          # informe; --aplicar borra
```

Dos workflows, y la separación es deliberada: `etl.yml` **extrae** (rastreo,
OpenAPI, repos, commit) y `paquete.yml` **empaqueta** lo ya almacenado. El
segundo es stdlib pura, tarda segundos en prepararse y se lanza solo desde
Actions sin arrastrar un rastreo de 50 minutos. `etl.yml` lo invoca por
`workflow_call` únicamente cuando la frontera queda vacía.

Las pruebas no usan pytest; cada fichero es un script:

```bash
for t in tests/test_*.py; do python3 "$t" || break; done
```

Los workflows usan ese mismo glob, así que **no hay que registrar nada**:
basta con crear `tests/test_*.py`. Dentro de cada fichero, el bloque
`__main__` también descubre las funciones `test_*` solo.

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

**El checkout del ETL es superficial, y no es un descuido.** El repositorio
lleva 2.693 ejecuciones commiteadas, 12.780 documentos y 260 MB de `.git`.
Con `fetch-depth: 0` el checkout del 2026-09-27 pasó de 20 minutos y el
lote no llegó a rastrear nada: la guarda de "Ejecutar pipeline" aborta
cuando quedan menos de 5 minutos útiles. `git_commit_and_push` intenta el
push directo y solo hace `--unshallow` si la rama ha divergido, cosa que
con el grupo de concurrencia solo pasa si empuja una persona a la vez.

**Las semillas se encolan ANTES de la frontera arrastrada.** Al revés
quedaban detrás de 7.000 URLs: 62 lotes, más de once horas, y la frontera
crece por el camino.

**Una URL que nunca sirve contenido tiene que quedar registrada igual.**
`registrar_fallo` hacía `return` cuando la URL no estaba en el manifiesto,
que es justo el caso frecuente (DOM vacío, markdown por debajo del mínimo).
Sin entrada, `debe_visitar` la da por desconocida, el enlace se redescubre
al rastrear la página padre y vuelve a encolarse. Para siempre. Eso es lo
que mantenía escrito `more_work.flag` y encadenaba el ETL sin fin: 84.387
líneas de fallo en `error.log` sobre unas 16.000 URLs.

**Una página sin cuerpo pero con enlaces NO es un fallo.** Es
`registrar_descubrimiento`: se registra con TTL normal y se vuelve a
recorrer. En PubHub la página de sección es el único sitio desde el que se
descubren los capítulos del doc-set; tratarla como fallo la aparca 14 días
y se lleva por delante medio doc-set.

**Los doc-sets de DevNet se declaran UNA vez**, en `config.devnet_docsets`
(`slug -> producto`). De ahí salen a la vez la allowlist de rastreo (la
compone `crawler_ai._regex_docsets_devnet`) y la taxonomía del paquete
(`copilot_pack.DOCSETS_DEVNET`). Eran dos listas y se desincronizaban en
silencio: `site/hcs` estaba admitido pero sin mapear y sus 15 documentos
caían en "misc". `tests/test_copilot_pack.py` falla si se vuelven a
separar.

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

- El encadenado sin fin está resuelto por la raíz (`registrar_fallo` y
  `registrar_descubrimiento` ya dejan entrada en el manifiesto), y además
  `etl.yml` tiene un tope de 12 lotes por cadena como red de seguridad. Si
  ese tope salta de forma recurrente, la frontera ha vuelto a no converger.
- `docs/cmse` **resuelto**: su `<title>` es "Cisco Metrics Search Engine".
  Telemetría, no colaboración. Se queda fuera. Con eso el inventario de
  DevNet queda cerrado: 55 doc-sets admitidos de 338, y ninguno de los 283
  restantes es de colaboración.
- **La cobertura de DevNet es el agujero abierto.** 31 de los 55 doc-sets
  admitidos tienen menos de 3 páginas en el corpus, y el dominio entero
  aporta 277. Entre los de UNA página: `docs/webex-calling`,
  `docs/cisco-meeting-server`, `docs/customer-voice-portal`,
  `docs/webex-xml-api-reference-guide`; `docs/axl` se queda en cuatro.
  El sondeo apunta a la causa: `/docs/axl/` sirve 936 caracteres de HTML
  crudo (el índice del doc-set lo pinta JavaScript) pero
  `/docs/axl/axl-developer-guide/` sirve 52.840 (las páginas de contenido SÍ
  vienen del servidor). O sea: el contenido está ahí y lo que falla es
  descubrirlo desde la raíz del doc-set. Falta comprobar si con el
  `registrar_descubrimiento` nuevo basta, o si los enlaces del índice no son
  `<a href>` y hay que desplegarlos desde `js_code`. **No se puede atacar por
  el JSON del índice: `robots.txt` de DevNet trae `Disallow: /*.json`.**
- `/docs/unity-connection/` responde 404 incluso con barra final. El doc-set
  vivo es `/site/unity-connection/`, que ya está seedeado.
- **La frontera de developer.cisco.com está vacía: el dominio ya convergió
  en 341 URLs.** Rastrear más no descubre nada nuevo; la única palanca que
  queda son las semillas. Por eso `docs/axl-schema-reference`,
  `docs/axl/axl-developer-guide` y `docs/serviceability` se seedean
  explícitamente en lugar de esperar a que el índice los enlace.
- **Una semilla que la allowlist rechaza no da error: se descarta en
  silencio.** `tests/test_url_policy.py` pasa ahora todas las de
  `config.seeds` por `url_aceptable`, que es la única forma barata de que
  ese fallo deje de ser mudo.
- Los esquemas de implantación de CUCM y CUC vienen de www.cisco.com, no de
  DevNet. `products-implementation-design-guides-list.html` sí funciona
  (queda en `discovery` y de ahí salen los SRND). En cambio
  `products-technical-reference-list.html` devuelve **302 a `series.html`**
  para CUCM y para CUC: Cisco ya no publica esa página. Las dos semillas se
  retiraron.
- **La guarda de semillas no detecta una semilla muerta, solo una
  inadmisible.** `test_url_policy.py` comprueba que la allowlist acepta la
  URL; que el servidor la sirva es otra cosa. Las tres semillas retiradas
  (`docs/serviceability`, 404, y las dos `technical-reference-list`, 302)
  pasaban la prueba sin problema. Para eso está el estado del manifiesto:
  `gone`, `redirect` y `failed`.
- **El diccionario de datos de CUCM no existe en HTML.** La página de
  `products-programming-reference-guides-list.html` sí se rastrea y de ella
  salen `jtapi_dev` (50), `tapi_dev` (44) y `callReportingBillingAdmin`
  (42), pero no enlaza ningún `datadictionary` en HTML: solo PDF, que
  `blocked_regex` bloquea por diseño. No es un fallo del rastreo.
- Las raíces de doc-set de DevNet siguen sin servir contenido:
  `/docs/axl-schema-reference/` da 0 caracteres tras sanitizar (queda
  `failed`) y `/docs/serviceability/` responde 404 (`gone`), como
  `/docs/unity-connection/`. `/docs/axl/axl-developer-guide/` sí entra
  (`active`), pero no enlaza sus capítulos: el índice también lo pinta
  JavaScript. Las semillas no bastan; queda el `js_code`.
- **`paquete.yml` no es del todo stdlib pura.** `copilot_pack.py` sí lo es,
  pero `tests/test_copilot_pack.py` importa `crawler_ai` para comprobar que
  la allowlist y la taxonomía salen de `devnet_docsets`, y eso arrastra
  `sanitizer` -> `bs4`. El workflow instala `beautifulsoup4` y nada más. El
  fallo estuvo latente meses porque `paquete-copilot` solo se ejecuta cuando
  la frontera queda vacía, y hasta el 2026-09-27 nunca quedó.
- La purga ya se aplicó: −344 documentos, −2.694 entradas del manifiesto y
  −1.437 de la cuarentena, que baja de 1.440 a 3 (las tres son 403 reales
  del WAF de www.cisco.com). El manifiesto queda en cuatro hosts:
  www.cisco.com, developer.cisco.com, help.webex.com y roomos.cisco.com.
- `deep_crawl()` no tiene cobertura: es el bucle de E/S. Sus decisiones sí
  están extraídas y probadas (`decidir_redireccion`, `parsear_sitemap`).

## Convenciones

- Deny-by-default **por host y por ruta**: el host debe estar declarado en
  `path_allowlist_regex` y la URL casar con alguna de sus regex. Un host sin
  declarar queda fuera, no dentro. Antes pasaba lo contrario y bastaba un
  enlace de pie de página para meter un subdominio entero: 2.699 entradas en
  54 hosts, 2.145 solo del Bug Search Tool. `esta_en_allowlist` usa
  `.match()` (anclado); `blocked_regex` usa `.search()`.
- Sin evasión de bots: se respeta `robots.txt`, se hace backoff ante 429 y
  se retrocede ante 403.
- Endurecer una allowlist no retira lo ya indexado: sigue en `docs/pages/`
  y en el manifiesto, y el ZIP lo sigue empaquetando. Después de tocarla,
  pasar `tools/purgar_fuera_de_allowlist.py`.
- Los ficheros de `logs/` son estado generado. Ante un conflicto de merge,
  toma la versión de `main` y reaplica el filtro; no los fusiones a mano.

## Skills

`.claude/skills/` trae caveman, ponytail y superpowers vendorizados (MIT).
Ver `.claude/skills/README.md` para origen, licencias y cómo actualizarlos.
