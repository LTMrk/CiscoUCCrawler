---
doc_id: webex-contact-center-get-organization-orgid-cad-variable-reportable-count
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/cad-variable/reportable-count
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.943664+00:00
---

# GET /organization/{orgid}/cad-variable/reportable-count

**API:** Webex Contact Center
**Área:** Global Variables
**operationId:** `getReportableCountConfig`

## Resumen
Get reportable count for Global Variable(s)

## Descripción
Get count for all the reportable Global Variable(s) in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Respuestas
- **200**: OK
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
