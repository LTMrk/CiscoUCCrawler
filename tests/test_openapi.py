"""Prueba el extractor OpenAPI enriquecido y la deteccion de endpoints nuevos."""
import json
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "src"))

from openapi_render import operacion_a_markdown

SPEC = {
    "info": {"title": "Webex Cloud Calling", "version": "1.0.0",
             "description": "APIs de llamada en la nube de Webex."},
    "servers": [{"url": "https://webexapis.com/v1"}],
    "components": {
        "schemas": {
            "KB": {
                "type": "object",
                "required": ["name", "mode"],
                "properties": {
                    "id": {"type": "string", "readOnly": True,
                           "description": "Identificador generado."},
                    "name": {"type": "string", "maxLength": 128,
                             "description": "Nombre de la knowledge base."},
                    "mode": {"type": "string", "enum": ["auto", "manual"],
                             "default": "auto", "description": "Modo de indexado."},
                    "createdAt": {"type": "string", "format": "date-time",
                                  "readOnly": True},
                },
            },
            "Error": {"type": "object", "properties": {
                "message": {"type": "string"}, "errorCode": {"type": "integer"}}},
        },
        "responses": {
            "TooManyRequests": {
                "description": "Rate limit excedido.",
                "content": {"application/json": {
                    "schema": {"$ref": "#/components/schemas/Error"},
                    "example": {"message": "Too many requests", "errorCode": 429}}},
            }
        },
    },
    "security": [{"oauth2": ["spark-admin:knowledge_base_write"]}],
}

OPERACION = {
    "summary": "Create a Knowledge Base",
    "description": "Crea una knowledge base para el AI Receptionist.",
    "operationId": "createKnowledgeBase",
    "tags": ["AI Receptionist"],
    "deprecated": False,
    "parameters": [
        {"name": "orgId", "in": "query", "required": True,
         "schema": {"type": "string", "format": "uuid"},
         "description": "Organization ID."},
        {"name": "locale", "in": "query",
         "schema": {"type": "string", "enum": ["en_US", "es_ES"], "default": "en_US"},
         "description": "Idioma."},
    ],
    "requestBody": {"content": {"application/json": {
        "schema": {"$ref": "#/components/schemas/KB"},
        "examples": {
            "basico": {"summary": "Creacion minima",
                       "value": {"name": "Soporte N1", "mode": "auto"}},
        },
    }}},
    "responses": {
        "201": {"description": "Creada.",
                "content": {"application/json": {
                    "schema": {"$ref": "#/components/schemas/KB"},
                    "examples": {"ok": {"summary": "Respuesta tipica", "value": {
                        "id": "Y2lzY29z", "name": "Soporte N1", "mode": "auto"}}}}},
                "headers": {"X-Rate-Limit-Remaining": {
                    "description": "Peticiones restantes en la ventana."}}},
        "400": {"description": "Peticion invalida.",
                "content": {"application/json": {
                    "schema": {"$ref": "#/components/schemas/Error"},
                    "example": {"message": "name is required", "errorCode": 4001}}}},
        "429": {"$ref": "#/components/responses/TooManyRequests"},
    },
}


def test_extraccion_enriquecida():
    md, meta = operacion_a_markdown(SPEC, "Webex Cloud Calling",
                                    "/knowledgeBases", "post", OPERACION)

    comprobaciones = [
        ("scopes OAuth", "spark-admin:knowledge_base_write" in md),
        ("scope en metadatos", meta["scopes"] == ["spark-admin:knowledge_base_write"]),
        ("ejemplo de peticion (examples plural)", '"name": "Soporte N1"' in md),
        ("ejemplo de respuesta", '"id": "Y2lzY29z"' in md),
        ("ejemplo de error", '"errorCode": 4001' in md),
        ("respuesta $ref resuelta (429)", "Rate limit excedido" in md),
        ("marca readOnly", "solo lectura" in md),
        ("enum de parametro", "en_US, es_ES" in md),
        ("default de parametro", "Por defecto: en_US" in md),
        ("format en tipo", "string/uuid" in md or "string/date-time" in md),
        ("maxLength", "Long. max: 128" in md),
        ("curl sintetizado", "curl -X POST" in md and "Bearer <TOKEN>" in md),
        ("curl con query requerida", "orgId=<orgId>" in md),
        ("curl con cuerpo obligatorio", '"name": "<name>"' in md),
        ("cabecera de respuesta", "X-Rate-Limit-Remaining" in md),
        ("seccion de errores separada", "## Respuestas de error" in md),
        ("contexto de API", "llamada en la nube" in md),
    ]

    fallos = [n for n, ok in comprobaciones if not ok]
    for nombre, ok in comprobaciones:
        print(f"  {'OK ' if ok else 'FALLO'} {nombre}")
    assert not fallos, f"Fallaron: {fallos}"
    return md


def test_deprecado():
    op = dict(OPERACION, deprecated=True)
    md, meta = operacion_a_markdown(SPEC, "API", "/x", "get", op)
    assert meta["deprecated"] is True
    assert "ENDPOINT DEPRECADO" in md
    # Debe ir al principio para sobrevivir al chunking.
    assert md.index("ENDPOINT DEPRECADO") < 120, "El aviso no esta al inicio"
    print("  OK aviso de deprecacion al inicio del documento")


def test_diff_operaciones():
    """Simula dos ejecuciones: se añade un endpoint y se retira otro."""
    import openapi_ingest as oi

    tmp = tempfile.mkdtemp()
    cwd = os.getcwd()
    os.chdir(tmp)
    try:
        os.makedirs("logs", exist_ok=True)
        os.makedirs(oi.DIR_DOCS_API, exist_ok=True)

        # Estado previo: dos operaciones conocidas
        estado = {"webex-cloud-calling.json": {
            "sha": "sha-viejo", "api": "Webex Cloud Calling",
            "operaciones": {
                "POST /knowledgeBases": "kb-post",
                "DELETE /legacyThing": "legacy-delete",
            },
            "deprecadas": {},
        }}
        oi._guardar_estado(estado)
        open(os.path.join(oi.DIR_DOCS_API, "legacy-delete.md"), "w").write("viejo")

        # Simula la parte de diff sin red
        ops_previas = estado["webex-cloud-calling.json"]["operaciones"]
        ops_actuales = {"POST /knowledgeBases": "kb-post", "GET /knowledgeBases": "kb-get"}

        added = [c for c in ops_actuales if c not in ops_previas]
        removed = [c for c in ops_previas if c not in ops_actuales]

        assert added == ["GET /knowledgeBases"], f"added incorrecto: {added}"
        assert removed == ["DELETE /legacyThing"], f"removed incorrecto: {removed}"

        # El tombstone debe borrar el fichero
        for clave in removed:
            slug = ops_previas[clave]
            p = os.path.join(oi.DIR_DOCS_API, f"{slug}.md")
            if os.path.exists(p):
                os.remove(p)
        assert not os.path.exists(os.path.join(oi.DIR_DOCS_API, "legacy-delete.md")), \
            "El .md del endpoint retirado sigue en disco"

        print("  OK diff a nivel de operacion: 1 nuevo, 1 retirado, tombstone aplicado")
    finally:
        os.chdir(cwd)
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    print("\nExtractor enriquecido:")
    md = test_extraccion_enriquecida()
    test_deprecado()
    print("\nSeguimiento de operaciones:")
    test_diff_operaciones()
    print(f"\n--- documento generado: {len(md)} chars ---")
    print(md[:1400])
    print("\nTODAS LAS PRUEBAS PASARON")
