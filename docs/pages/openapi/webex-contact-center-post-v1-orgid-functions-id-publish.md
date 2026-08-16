---
doc_id: webex-contact-center-post-v1-orgid-functions-id-publish
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/{orgId}/functions/{id}:publish
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.968671+00:00
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
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `id` [path] (string) **(requerido)**: Custom function ID.

## Cuerpo de la petición (application/json)
- `tags` (array): Publish tags to apply to this version.
- `comment` (string): Optional publish comment.

## Respuestas
- **200**: Custom function published successfully.
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
- **400**: Bad Request. The function ID is missing or has an invalid format.
- **401**: Unauthorized.
- **500**: Publish failed.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
