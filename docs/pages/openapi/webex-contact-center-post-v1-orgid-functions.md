---
doc_id: webex-contact-center-post-v1-orgid-functions
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/{orgId}/functions
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.967937+00:00
---

# POST /v1/{orgId}/functions

**API:** Webex Contact Center
**Área:** Functions
**operationId:** `create`

## Resumen
Create a Custom Function

## Descripción
Create a new custom function. The source code is provided as an escaped string and the runtime defaults to the highest supported runtime for the given language.

Scope: `cjp:config_write`

## Parámetros
- `orgId` [path] (string) **(requerido)**: Organization ID.

## Cuerpo de la petición (application/json)
- `name` (string): Function name. Must be unique within the organization.
- `description` (string): Human-readable description of the function.
- `language` (string): Programming language. Defaults to `js`. Valores: js, py.
- `selectedRuntime` (string): Runtime identifier (case-sensitive). For example, `nodejs22.x` or `python3.13`. Defaults to the highest supported runtime for the chosen language.
- `timeoutInSec` (integer): Maximum execution time for the function, in seconds.
- `sourceCode` (string): Function source code as an escaped string. The handler must be an exported async function `export const handle = async (request, response) => { ... }`. Read inputs from `request.inputs.*`, set the result via `response.data = { ... }`, and `return response`.
- `inputs` (array): Declared inputs of the function.
  - `name` (string): Input variable name.
  - `dataType` (string): Input data type. Valores: boolean, datetime, decimal, integer, json, string.
  - `value` (object): Default or sample value for the input.
- `outputs` (string): Stringified JSON of output variable names mapped to sample values.

## Respuestas
- **201**: Custom function created successfully.
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
- **400**: Bad Request. Causes include: function body missing or malformed payload.
- **401**: Unauthorized.
- **409**: Conflict. A function with the same name already exists in the org.
- **500**: Internal Server Error.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
