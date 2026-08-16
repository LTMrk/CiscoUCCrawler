---
doc_id: webex-contact-center-post-v1-orgid-functions-import
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/{orgId}/functions:import
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.968374+00:00
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
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `overwrite` [query] (boolean): If `true`, overwrites a function with the same name if one already exists.
- `associatedRcs` [query] (array): Optional list of associated routing-context IDs.

## Cuerpo de la petición (multipart/form-data)
- `file` (string) **(requerido)**: Function-definition JSON document produced by the export API, uploaded as the multipart file part (not a zip or base64 envelope).

## Respuestas
- **201**: Custom function imported successfully.
  - `fnCode` (string): Function source code as an escaped string. The handler is an exported async function `export const handle = async (request, response) => { ... }`.
  - `fnMetadata` (object): Metadata for a custom function (no source code). Returned in list responses and inside the `fnMetadata` envelope of a single-function response.
    - `id` (string): Function ID. Hexadecimal ObjectId.
    - `orgId` (string): Organization ID that owns the function.
    - `name` (string): Function name.
    - `description` (string): Human-readable description of the function.
    - `language` (string): Programming language. Valores: js, py.
    - `selectedRuntime` (string): Runtime identifier.
    - `status` (string): Lifecycle status. Valores: Draft, Published.
    - `timeoutInSec` (integer): Maximum execution time for the function, in seconds.
    - `tagVersionMap` (object): Map of publish tag to the function version it currently points to.
    - `lockedBy` (string): User ID currently holding the edit lock, or empty if unlocked.
    - `createdBy` (string): User ID that created the function.
    - `createdDate` (string): Timestamp the function was created.
    - `lastModifiedBy` (string): User ID that last modified the function.
    - `lastModifiedDate` (string): Timestamp of the most recent modification.
- **400**: Bad Request. The supplied function-definition file is corrupted or malformed.
- **401**: Unauthorized.
- **500**: Internal Server Error.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
