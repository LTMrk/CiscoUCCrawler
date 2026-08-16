---
doc_id: webex-contact-center-get-organization-orgid-auto-csat-autocsatid-question-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/auto-csat/{autoCsatId}/question/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.923361+00:00
---

# GET /organization/{orgid}/auto-csat/{autoCsatId}/question/{id}

**API:** Webex Contact Center
**Área:** Auto CSAT
**operationId:** `getConfigAutoCSATQuestion1`

## Resumen
Get specific Auto CSAT mapped Question by ID

## Descripción
Retrieve an existing Auto CSAT mapped Question by ID in a given organization. Deprecated. Use GET /ai-feature/auto-csat/question/{id} instead.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `autoCsatId` [path] (string) **(requerido)**: Resource ID of the Auto CSAT resource
- `id` [path] (string) **(requerido)**: Resource ID of the Auto CSAT mapped Question.

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `questionId` (string) **(requerido)**: Question ID that is mapped for Auto CSAT configuration
  - `questionnaireId` (string) **(requerido)**: Questionnaire ID corresponding to the Question ID that is mapped for Auto CSAT configuration
  - `createdTime` (integer): This is the created time of the entity.
  - `lastUpdatedTime` (integer): This is the updated time of the entity.
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
