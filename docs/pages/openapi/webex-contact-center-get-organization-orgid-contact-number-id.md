---
doc_id: webex-contact-center-get-organization-orgid-contact-number-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/contact-number/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.933407+00:00
---

# GET /organization/{orgid}/contact-number/{id}

**API:** Webex Contact Center
**Área:** Contact Number
**operationId:** `getConfig_21`

## Resumen
Get specific Contact Number by ID

## Descripción
Retrieve an existing Contact Number by ID in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Contact Number.

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `number` (string) **(requerido)**: The customized ani number.
  - `createdTime` (integer): Creation time(in epoch millis) of this resource.
  - `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
