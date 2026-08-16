---
doc_id: webex-contact-center-post-v1-orgid-functions-id-export
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/{orgId}/functions/{id}:export
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.968761+00:00
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
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `id` [path] (string) **(requerido)**: Custom function ID.
- `versionOrTag` [query] (string): Version number or publish tag of the source code to export. If omitted, the latest published version is exported.

## Respuestas
- **200**: Export succeeded.
  - `name` (string): Function name.
  - `language` (string): Source language of the function (for example, `js`, `py`).
  - `runtime` (string): Runtime the function executes on.
  - `description` (string): Human-readable description of the function.
  - `sourceCode` (string): Full function source code.
  - `inputs` (array): Declared function inputs.
  - `outputs` (string): Declared function outputs as a JSON-encoded string.
- **400**: Bad Request. The function ID has an invalid format.
- **401**: Unauthorized.
- **500**: Export failed.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
