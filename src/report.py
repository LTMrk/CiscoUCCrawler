"""
report.py — Genera el resumen de la ejecución para GITHUB_STEP_SUMMARY.

Vive en un fichero propio en lugar de embebido en etl.yml porque el YAML de
GitHub Actions y el Python multilínea se llevan mal: comillas anidadas e
indentación del escalar de bloque rompen el parseo del workflow entero.
Aquí además es testeable.
"""

import json
import os
import sys

RUTAS = {
    "openapi": "logs/openapi_deltas.json",
    "paginas": "logs/deltas.json",
    "cuarentena": "logs/quarantine.json",
    "specs": "logs/openapi_state.json",
}


def _leer(ruta):
    if not os.path.exists(ruta):
        return None
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def _seccion_openapi(d, lineas):
    if not d:
        return
    lineas.append("### Cambios en la API de Webex")
    lineas.append(
        f"**{len(d.get('added', []))} nuevos** · "
        f"{len(d.get('removed', []))} retirados · "
        f"{len(d.get('deprecated', []))} recién deprecados"
    )
    lineas.append("")

    bloques = [
        ("Endpoints nuevos", d.get("added", []), "🆕"),
        ("Recién deprecados", d.get("deprecated", []), "⚠️"),
        ("Retirados (tombstone emitido)", d.get("removed", []), "🗑️"),
    ]
    for titulo, items, icono in bloques:
        if not items:
            continue
        lineas.append(f"<details><summary>{icono} {titulo} ({len(items)})</summary>\n")
        for item in items[:100]:
            lineas.append(f"- `{item}`")
        if len(items) > 100:
            lineas.append(f"- ... y {len(items) - 100} más")
        lineas.append("\n</details>\n")


def _contar(valor):
    """El esquema v1 guardaba `operaciones` como int y el v2 como dict.
    El reporte nunca debe tumbar el workflow por un estado antiguo."""
    if isinstance(valor, dict):
        return len(valor)
    if isinstance(valor, int):
        return valor
    return 0


def _seccion_inventario(estado, lineas):
    if not isinstance(estado, dict):
        return
    filas = []
    for nombre, datos in sorted(estado.items()):
        if nombre.startswith("_") or not isinstance(datos, dict):
            continue
        filas.append((
            datos.get("api", nombre),
            _contar(datos.get("operaciones")),
            _contar(datos.get("deprecadas")),
            (datos.get("actualizado") or "")[:10],
        ))
    if not filas:
        return
    lineas.append("### Inventario de la API indexada")
    lineas.append("| API | Operaciones | Deprecadas | Última actualización |")
    lineas.append("|---|---:|---:|---|")
    for api, n_ops, n_dep, fecha in filas:
        lineas.append(f"| {api} | {n_ops} | {n_dep} | {fecha} |")
    lineas.append(f"| **Total** | **{sum(f[1] for f in filas)}** | "
                  f"**{sum(f[2] for f in filas)}** | |")
    lineas.append("")


def _seccion_paginas(d, lineas):
    if not d:
        return
    lineas.append("### Páginas rastreadas")
    lineas.append(f"Modo: `{d.get('modo', '?')}`")
    lineas.append(
        f"+{len(d.get('added', []))} nuevas · "
        f"~{len(d.get('modified', []))} modificadas · "
        f"-{len(d.get('removed', []))} retiradas · "
        f"{d.get('unchanged_count', 0)} sin cambios"
    )

    semillas = d.get("semillas_encoladas", 0)
    if semillas:
        lineas.append("")
        lineas.append(f"{semillas} URL(s) encoladas desde semillas y sitemaps "
                      "de `config.json`, por delante de la frontera arrastrada.")

    redirecciones = d.get("redirected", [])
    if redirecciones:
        lineas.append("")
        lineas.append(f"### {len(redirecciones)} redirección(es) seguida(s)")
        lineas.append("El origen movio el recurso y el rastreo continuo en el "
                      "destino. No son fallos.")
        lineas.append("")
        for salto in redirecciones[:20]:
            lineas.append(f"- {salto}")
        if len(redirecciones) > 20:
            lineas.append(f"- ...y {len(redirecciones) - 20} mas")
    lineas.append("")


def _seccion_cuarentena(d, lineas):
    if not d:
        return
    lineas.append(f"### {len(d)} URL(s) en cuarentena")
    lineas.append("Rechazadas por el WAF de origen. No se reintentan "
                  "automáticamente: requieren decisión manual.")
    lineas.append("")
    for url, datos in sorted(d.items())[:30]:
        lineas.append(f"- `[{datos.get('codigo')}]` x{datos.get('veces')} {url}")
    lineas.append("")


def construir_resumen():
    lineas = ["## Resumen del lote", ""]
    _seccion_openapi(_leer(RUTAS["openapi"]), lineas)
    _seccion_inventario(_leer(RUTAS["specs"]), lineas)
    _seccion_paginas(_leer(RUTAS["paginas"]), lineas)
    _seccion_cuarentena(_leer(RUTAS["cuarentena"]), lineas)
    return "\n".join(lineas)


def main():
    resumen = construir_resumen()
    destino = os.environ.get("GITHUB_STEP_SUMMARY")
    if destino:
        with open(destino, "a", encoding="utf-8") as f:
            f.write(resumen + "\n")
    else:
        sys.stdout.write(resumen + "\n")


if __name__ == "__main__":
    main()
    
