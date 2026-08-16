---
doc_id: webex-contact-center-post-v1-orgid-functions-id-lock
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/{orgId}/functions/{id}:lock
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.968540+00:00
---

# POST /v1/{orgId}/functions/{id}:lock

**API:** Webex Contact Center
**Área:** Functions
**operationId:** `lockFnById`

## Resumen
Lock a Custom Function

## Descripción
Acquire an edit lock on a custom function to prevent concurrent writes by other users.

Scope: `cjp:config_write`

## Parámetros
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `id` [path] (string) **(requerido)**: Custom function ID.

## Respuestas
- **200**: Custom function locked successfully.
- **400**: Bad Request.
- **401**: Unauthorized.
- **404**: No function found for the supplied ID.
- **500**: Internal Server Error.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
