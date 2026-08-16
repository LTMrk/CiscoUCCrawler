---
doc_id: webex-contact-center-delete-organization-orgid-desktop-layout-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: DELETE
path: /organization/{orgid}/desktop-layout/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.938114+00:00
---

# DELETE /organization/{orgid}/desktop-layout/{id}

**API:** Webex Contact Center
**Área:** Desktop Layout
**operationId:** `deleteConfig_14`

## Resumen
Delete specific Desktop Layout by ID

## Descripción
Delete an existing Desktop Layout by ID in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Desktop Layout.

## Respuestas
- **200**: OK
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **412**: Resource referred in other entity(s). Please get all the reference entities info by invoking Get incoming-references api.
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
