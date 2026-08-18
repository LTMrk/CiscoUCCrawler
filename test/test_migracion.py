"""Reproduce el TypeError de migracion de esquema v1 -> v2 y valida el arreglo."""
import json
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "src"))

import openapi_ingest as oi
import report


# Formato v1 exacto que produjo el fallo en GitHub Actions:
# "operaciones" era un CONTADOR, no un mapa.
ESTADO_V1 = {
    "webex-cloud-calling.json": {
        "sha": "abc123",
        "operaciones": 412,
        "content_sha": "deadbeef",
        "actualizado": "2026-08-16T11:30:00+00:00",
    },
    "webex-messaging.json": {
        "sha": "def456",
        "operaciones": 87,
        "content_sha": "cafe",
        "actualizado": "2026-08-16T11:30:00+00:00",
    },
}


def _escribir_doc(slug, spec, metodo, ruta, deprecated=False):
    os.makedirs(oi.DIR_DOCS_API, exist_ok=True)
    contenido = (
        "---\n"
        f"doc_id: {slug}\n"
        f"source: webex-openapi-specs/public-spec/{spec}\n"
        "api: Webex Cloud Calling\n"
        f"method: {metodo}\n"
        f"path: {ruta}\n"
        f"deprecated: {str(deprecated).lower()}\n"
        "---\n\n# contenido\n"
    )
    with open(os.path.join(oi.DIR_DOCS_API, f"{slug}.md"), "w", encoding="utf-8") as f:
        f.write(contenido)


def test_migracion_reconstruye_desde_disco():
    tmp = tempfile.mkdtemp()
    cwd = os.getcwd()
    os.chdir(tmp)
    try:
        os.makedirs("logs", exist_ok=True)
        with open(oi.RUTA_ESTADO_SPECS, "w", encoding="utf-8") as f:
            json.dump(ESTADO_V1, f)

        # Documentos ya generados por la ejecucion anterior
        _escribir_doc("cc-post-kb", "webex-cloud-calling.json", "POST", "/knowledgeBases")
        _escribir_doc("cc-get-kb", "webex-cloud-calling.json", "GET", "/knowledgeBases")
        _escribir_doc("cc-old", "webex-cloud-calling.json", "GET", "/legacy", deprecated=True)

        estado = oi._cargar_estado()

        assert estado["_schema_version"] == oi.SCHEMA_VERSION
        ops = estado["webex-cloud-calling.json"]["operaciones"]
        assert isinstance(ops, dict), f"No migro a dict: {type(ops)}"
        assert ops == {
            "POST /knowledgeBases": "cc-post-kb",
            "GET /knowledgeBases": "cc-get-kb",
            "GET /legacy": "cc-old",
        }, f"Reconstruccion incorrecta: {ops}"
        assert estado["webex-cloud-calling.json"]["deprecadas"] == {"GET /legacy": True}
        # El SHA se conserva: no hace falta regenerar lo reconstruido.
        assert estado["webex-cloud-calling.json"]["sha"] == "abc123"

        # Spec sin documentos en disco: no se puede reconstruir, se fuerza
        # la regeneracion invalidando el SHA.
        assert estado["webex-messaging.json"]["operaciones"] == {}
        assert estado["webex-messaging.json"]["sha"] is None, \
            "Deberia invalidar el SHA para regenerar"

        print("  OK migracion v1->v2: 3 operaciones reconstruidas del front matter,")
        print("     spec sin docs marcado para regeneracion")
    finally:
        os.chdir(cwd)
        shutil.rmtree(tmp, ignore_errors=True)


def test_len_sobre_int_no_revienta():
    """El crash original: len() sobre el contador del esquema v1."""
    lineas = []
    report._seccion_inventario(ESTADO_V1, lineas)
    salida = "\n".join(lineas)
    assert "412" in salida and "87" in salida, "El contador v1 deberia mostrarse igual"
    assert "**499**" in salida, f"Total incorrecto:\n{salida}"

    # Y con el esquema v2
    lineas = []
    report._seccion_inventario({
        "_schema_version": 2,
        "x.json": {"api": "A", "operaciones": {"a": "1", "b": "2"},
                   "deprecadas": {"a": True}, "actualizado": "2026-08-17T00:00:00"},
    }, lineas)
    salida = "\n".join(lineas)
    assert "| A | 2 | 1 |" in salida, f"Inventario v2 incorrecto:\n{salida}"
    assert "_schema_version" not in salida, "La clave de esquema no debe salir como API"

    print("  OK report tolera int (v1) y dict (v2) sin reventar")


def test_estado_corrupto():
    """Un estado ilegible no debe tumbar la ejecucion."""
    tmp = tempfile.mkdtemp()
    cwd = os.getcwd()
    os.chdir(tmp)
    try:
        os.makedirs("logs", exist_ok=True)
        with open(oi.RUTA_ESTADO_SPECS, "w", encoding="utf-8") as f:
            f.write("{esto no es json valido")
        estado = oi._cargar_estado()
        assert estado == {"_schema_version": oi.SCHEMA_VERSION}
        print("  OK estado corrupto -> se regenera desde cero sin excepcion")
    finally:
        os.chdir(cwd)
        shutil.rmtree(tmp, ignore_errors=True)


def test_tipos_inesperados():
    """Valores raros en el estado no deben propagarse como excepcion."""
    for valor in [None, "texto", [], 42]:
        lineas = []
        report._seccion_inventario({"x.json": {"api": "A", "operaciones": valor}}, lineas)
    print("  OK tipos inesperados en 'operaciones' tolerados")


if __name__ == "__main__":
    print("\nMigracion de esquema openapi_state.json:")
    test_migracion_reconstruye_desde_disco()
    test_len_sobre_int_no_revienta()
    test_estado_corrupto()
    test_tipos_inesperados()
    print("\nTODAS LAS PRUEBAS PASARON")
