---
doc_id: webex-contact-center-post-v1-orgid-functions-import
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/{orgId}/functions:import
operation_id: importFn
tags: Functions
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.741055+00:00
---

# POST /v1/{orgId}/functions:import

**API:** Webex Contact Center
**Área:** Functions
**operationId:** `importFn`

## Resumen
Import a Custom Function

## Descripción
Import a custom function from a previously exported function-definition JSON file, uploaded as the multipart `file` part (not a zip or base64 envelope). Use `overwrite=true` to replace any existing function with the same name.

Scope: `cjp:config_write`

## Parámetros
- `orgId` [path] (string) (**requerido**): Organization ID.
- `overwrite` [query] (boolean): If `true`, overwrites a function with the same name if one already exists. Por defecto: False.
- `associatedRcs` [query] (array): Optional list of associated routing-context IDs.

## Cuerpo de la petición (multipart/form-data)
- `file` (string/binary) (**requerido**): Function-definition JSON document produced by the export API, uploaded as the multipart file part (not a zip or base64 envelope).

## Ejemplo de invocación
```bash
curl -X POST '/v1/<orgId>/functions:import' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"file": "<file>"}'
```

## Respuestas correctas
**201**: Custom function imported successfully.
- `fnCode` (string): Function source code as an escaped string. The handler is an exported async function `export const handle = async (request, response) => { ... }`.
- `fnMetadata` (object): Metadata for a custom function (no source code). Returned in list responses and inside the `fnMetadata` envelope of a single-function response.
  - `id` (string): Function ID. Hexadecimal ObjectId.
  - `orgId` (string): Organization ID that owns the function.
  - `name` (string): Function name.
  - `description` (string): Human-readable description of the function.
  - `language` (string): Programming language. Valores: js, py.
  - `selectedRuntime` (string): Runtime identifier.
  - `status` (string): Lifecycle status. Valores: Draft, Published.
  - `timeoutInSec` (integer/int32): Maximum execution time for the function, in seconds.
  - `tagVersionMap` (object): Map of publish tag to the function version it currently points to.
  - `lockedBy` (string): User ID currently holding the edit lock, or empty if unlocked.
  - `createdBy` (string): User ID that created the function.
  - `createdDate` (string/date-time): Timestamp the function was created.
  - `lastModifiedBy` (string): User ID that last modified the function.
  - `lastModifiedDate` (string/date-time): Timestamp of the most recent modification.

### Ejemplo — respuesta 201
```json
{
  "fnCode": "export const handle = async (request, response) => {\n  response.data = { areaCode: String(request.inputs.ani || '').slice(-10).slice(0, 3) };\n  return response;\n}\n",
  "fnMetadata": {
    "id": "64f1b2c3d4e5f6a7b8c9d0e1",
    "orgId": "8eb7da9a-c81c-4d13-b08b-38fdeb7330d8",
    "name": "validateZipCode",
    "description": "Returns true if the supplied US zip code is in a valid 5-digit format.",
    "language": "js",
    "selectedRuntime": "nodejs22.x",
    "status": "Published",
    "timeoutInSec": 3,
    "tagVersionMap": {
      "Dev": "1",
      "Latest": "1"
    },
    "lockedBy": "",
    "createdBy": "user@example.com",
    "createdDate": "2026-05-28T14:23:01Z",
    "lastModifiedBy": "user@example.com",
    "lastModifiedDate": "2026-05-28T14:23:01Z"
  }
}
```

## Respuestas de error
- **400**: Bad Request. The supplied function-definition file is corrupted or malformed.
  Ejemplo:
```json
{
  "code": "InvalidRequest",
  "message": "The campaign ID is missing"
}
```
- **401**: Unauthorized.
- **500**: Internal Server Error.
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