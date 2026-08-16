---
doc_id: webex-contact-center-delete-v1-orgid-functions-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: DELETE
path: /v1/{orgId}/functions/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.968263+00:00
---

# DELETE /v1/{orgId}/functions/{id}

**API:** Webex Contact Center
**Área:** Functions
**operationId:** `delete`

## Resumen
Delete a Custom Function

## Descripción
Delete a custom function by ID. Use `isForceDeletion=true` to delete even when the function is referenced by one or more flows.

Scope: `cjp:config_write`

## Parámetros
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `id` [path] (string) **(requerido)**: Custom function ID.
- `isForceDeletion` [query] (boolean): If `true`, deletes the function regardless of its usage in flows.

## Respuestas
- **204**: Custom function deleted successfully.
- **400**: Bad Request.
- **401**: Unauthorized.
- **404**: No function found for the supplied ID.
- **500**: Internal Server Error.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
