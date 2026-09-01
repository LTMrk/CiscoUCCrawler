---
doc_id: webex-contact-center-post-v1-orgid-functions-id-publish
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/{orgId}/functions/{id}:publish
operation_id: publish
tags: Functions
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.717160+00:00
---

# POST /v1/{orgId}/functions/{id}:publish

**API:** Webex Contact Center
**Área:** Functions
**operationId:** `publish`

## Resumen
Publish a Custom Function

## Descripción
Publish the latest draft of a custom function under one or more tags (`Dev`, `Test`, `Latest`, `Live`). Ensure the function has been created or updated before calling this API.

Scope: `cjp:config_write`

## Parámetros
- `orgId` [path] (string) (**requerido**): Organization ID.
- `id` [path] (string) (**requerido**): Custom function ID.

## Cuerpo de la petición (application/json)
- `tags` (array): Publish tags to apply to this version.
- `comment` (string): Optional publish comment.

## Ejemplo de invocación
```bash
curl -X POST '/v1/<orgId>/functions/<id>:publish' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: Custom function published successfully.
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
- **400**: Bad Request. The function ID is missing or has an invalid format.
  Ejemplo:
```json
{
  "code": "InvalidRequest",
  "message": "The campaign ID is missing"
}
```
- **401**: Unauthorized.
- **500**: Publish failed.
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