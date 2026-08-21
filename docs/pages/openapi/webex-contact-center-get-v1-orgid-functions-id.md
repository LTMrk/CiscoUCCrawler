---
doc_id: webex-contact-center-get-v1-orgid-functions-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/{orgId}/functions/{id}
operation_id: findById
tags: Functions
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.809351+00:00
---

# GET /v1/{orgId}/functions/{id}

**API:** Webex Contact Center
**Área:** Functions
**operationId:** `findById`

## Resumen
Get a Custom Function

## Descripción
Retrieve a custom function by its ID. Use `versionOrTag` to fetch a specific published version, or omit it to get the draft.

Scope: `cjp:config_read`

## Parámetros
- `orgId` [path] (string) (**requerido**): Organization ID.
- `id` [path] (string) (**requerido**): Custom function ID. Hexadecimal ObjectId returned by the create or list APIs.
- `versionOrTag` [query] (string): Version number or publish tag of the source code to return (for example, `Dev`, `Live`, or `2`). If omitted, the draft version is returned.
- `metaDataOnly` [query] (string): If `true`, returns only metadata and excludes source code. If `false` or omitted, returns both metadata and source code. Por defecto: false.

## Ejemplo de invocación
```bash
curl -X GET '/v1/<orgId>/functions/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Custom function retrieved successfully.
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

### Ejemplo — respuesta 200
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
- **400**: Bad Request. A required parameter was missing or had an invalid format.
  Ejemplo:
```json
{
  "code": "InvalidRequest",
  "message": "The campaign ID is missing"
}
```
- **401**: Unauthorized.
- **404**: No function found for the supplied ID.
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