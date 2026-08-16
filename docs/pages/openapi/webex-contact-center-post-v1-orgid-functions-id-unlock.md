---
doc_id: webex-contact-center-post-v1-orgid-functions-id-unlock
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/{orgId}/functions/{id}:unlock
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.968457+00:00
---

# POST /v1/{orgId}/functions/{id}:unlock

**API:** Webex Contact Center
**Área:** Functions
**operationId:** `unlockFnById`

## Resumen
Unlock a Custom Function

## Descripción
Release the edit lock on a custom function so that other users can edit it.

Scope: `cjp:config_write`

## Parámetros
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `id` [path] (string) **(requerido)**: Custom function ID.

## Respuestas
- **200**: Custom function unlocked successfully.
- **400**: Bad Request.
- **401**: Unauthorized.
- **404**: No function found for the supplied ID.
- **500**: Internal Server Error.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
