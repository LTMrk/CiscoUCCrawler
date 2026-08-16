---
doc_id: webex-contact-center-put-v1-orgid-functions-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PUT
path: /v1/{orgId}/functions/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.968184+00:00
---

# PUT /v1/{orgId}/functions/{id}

**API:** Webex Contact Center
**Área:** Functions
**operationId:** `update`

## Resumen
Update a Custom Function

## Descripción
Update an existing custom function by ID. Replaces the draft source code and metadata with the supplied body.

Scope: `cjp:config_write`

## Parámetros
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `id` [path] (string) **(requerido)**: Custom function ID.

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
- **200**: Custom function updated successfully.
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
- **400**: Bad Request. Causes include: function body missing, malformed payload, or duplicate function name.
- **401**: Unauthorized.
- **500**: Internal Server Error.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
