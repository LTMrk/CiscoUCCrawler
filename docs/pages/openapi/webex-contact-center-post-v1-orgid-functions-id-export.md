---
doc_id: webex-contact-center-post-v1-orgid-functions-id-export
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/{orgId}/functions/{id}:export
operation_id: exportFn
tags: Functions
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.152904+00:00
---

# POST /v1/{orgId}/functions/{id}:export

**API:** Webex Contact Center
**Área:** Functions
**operationId:** `exportFn`

## Resumen
Export a Custom Function

## Descripción
Export a custom function for the given version or publish tag. Returns the plain function-definition JSON (name, language, runtime, description, source code, inputs, and outputs), suitable for re-importing via the import API.

Scope: `cjp:config_read`

## Parámetros
- `orgId` [path] (string) (**requerido**): Organization ID.
- `id` [path] (string) (**requerido**): Custom function ID.
- `versionOrTag` [query] (string): Version number or publish tag of the source code to export. If omitted, the latest published version is exported.

## Ejemplo de invocación
```bash
curl -X POST '/v1/<orgId>/functions/<id>:export' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Export succeeded.
- `name` (string): Function name.
- `language` (string): Source language of the function (for example, `js`, `py`).
- `runtime` (string): Runtime the function executes on.
- `description` (string): Human-readable description of the function.
- `sourceCode` (string): Full function source code.
- `inputs` (array): Declared function inputs.
- `outputs` (string): Declared function outputs as a JSON-encoded string.

### Ejemplo — respuesta 200
```json
{
  "name": "validateZipCode",
  "language": "js",
  "runtime": "nodejs22.x",
  "description": "Validates and normalizes a US ZIP code.",
  "sourceCode": "export const handle = (request, response) => { /* ... */ };",
  "inputs": [],
  "outputs": "{\"myOutputVar1\": 7, \"myOutputVar2\": \"String data\"}"
}
```

## Respuestas de error
- **400**: Bad Request. The function ID has an invalid format.
  Ejemplo:
```json
{
  "code": "InvalidRequest",
  "message": "The campaign ID is missing"
}
```
- **401**: Unauthorized.
- **500**: Export failed.
  Ejemplo:
```json
{
  "code": "InvalidRequest",
  "message": "The campaign ID is missing"
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs