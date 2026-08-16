---
doc_id: webex-contact-center-delete-organization-orgid-multimedia-profile-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: DELETE
path: /organization/{orgid}/multimedia-profile/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.945186+00:00
---

# DELETE /organization/{orgid}/multimedia-profile/{id}

**API:** Webex Contact Center
**Área:** Multimedia Profile
**operationId:** `deleteConfig_11`

## Resumen
Delete specific Multimedia Profile by ID

## Descripción
Delete an existing Multimedia Profile by ID in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Multimedia Profile.

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
