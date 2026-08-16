---
doc_id: webex-contact-center-put-v1-callbacks-organization-orgid-scheduled-callback-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PUT
path: /v1/callbacks/organization/{orgId}/scheduled-callback/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.963335+00:00
---

# PUT /v1/callbacks/organization/{orgId}/scheduled-callback/{id}

**API:** Webex Contact Center
**Área:** Callbacks
**operationId:** `UpdateScheduledCallbackById`

## Resumen
Update scheduled callback by Id

## Descripción
Update an existing scheduled callback by Id,those whose scheduled trigger time has already passed cannot be updated. Requires 'cjp:user' scope for authorization.

## Parámetros
- `orgId` [path] (string) **(requerido)**: The organization ID for which the callback is being scheduled. This should be a valid UUID.
- `id` [path] (string) **(requerido)**: The id with which the Scheduled Callback has been created.

## Respuestas
- **200**: The request was successfully updated.
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **404**: Not Found
- **429**: Too Many Requests
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
