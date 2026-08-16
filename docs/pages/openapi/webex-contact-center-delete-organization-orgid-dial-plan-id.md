---
doc_id: webex-contact-center-delete-organization-orgid-dial-plan-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: DELETE
path: /organization/{orgid}/dial-plan/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.941588+00:00
---

# DELETE /organization/{orgid}/dial-plan/{id}

**API:** Webex Contact Center
**Área:** Dial Plan
**operationId:** `deleteConfigDialPlan`

## Resumen
Delete specific Dial Plan by ID

## Descripción
Delete an existing Dial Plan by ID in a given organization.

**Deprecated:** Dial Plan configuration is deprecated. Dial Plan is no longer available as an Agent Profile setting, so agents can no longer  use them for agent dial number validation.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Dial Plan.

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
