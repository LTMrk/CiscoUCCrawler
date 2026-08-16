---
doc_id: webex-contact-center-get-v1-orgid-functions-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /v1/{orgId}/functions/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.968038+00:00
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
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `id` [path] (string) **(requerido)**: Custom function ID. Hexadecimal ObjectId returned by the create or list APIs.
- `versionOrTag` [query] (string): Version number or publish tag of the source code to return (for example, `Dev`, `Live`, or `2`). If omitted, the draft version is returned.
- `metaDataOnly` [query] (string): If `true`, returns only metadata and excludes source code. If `false` or omitted, returns both metadata and source code.

## Respuestas
- **200**: Custom function retrieved successfully.
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
- **400**: Bad Request. A required parameter was missing or had an invalid format.
- **401**: Unauthorized.
- **404**: No function found for the supplied ID.
- **500**: Internal Server Error.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
