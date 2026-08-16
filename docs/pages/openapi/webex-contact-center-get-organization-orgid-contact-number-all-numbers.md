---
doc_id: webex-contact-center-get-organization-orgid-contact-number-all-numbers
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/contact-number/all-numbers
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.933106+00:00
---

# GET /organization/{orgid}/contact-number/all-numbers

**API:** Webex Contact Center
**Área:** Contact Number
**operationId:** `getAllContactNumbers`

## Resumen
List all contact numbers(property - number)

## Descripción
Retrieve a list of  only contact numbers(property - number) from Contact Number(s) without pagination in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Respuestas
- **200**: OK
  - (array de:)
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
