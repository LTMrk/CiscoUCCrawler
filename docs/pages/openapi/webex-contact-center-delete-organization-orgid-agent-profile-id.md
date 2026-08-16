---
doc_id: webex-contact-center-delete-organization-orgid-agent-profile-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: DELETE
path: /organization/{orgid}/agent-profile/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.939395+00:00
---

# DELETE /organization/{orgid}/agent-profile/{id}

**API:** Webex Contact Center
**Área:** Desktop Profile
**operationId:** `deleteConfigDesktopProfile`

## Resumen
Delete specific Desktop Profile by ID

## Descripción
Delete an existing Desktop Profile by ID in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Desktop Profile.

## Respuestas
- **204**: No Content
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **412**: Resource referred in other entity(s). Please get all the reference entities info by invoking Get incoming-references api.
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
