---
doc_id: webex-contact-center-post-organization-orgid-ai-feature-auto-csat-question
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/ai-feature/auto-csat/question
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.922049+00:00
---

# POST /organization/{orgid}/ai-feature/auto-csat/question

**API:** Webex Contact Center
**Área:** AI Feature
**operationId:** `createConfigAutoCSATQuestion2`

## Resumen
Create a new Question mapped to AutoCSAT

## Descripción
Create a new Auto CSAT mapped Question in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `questionId` (string) **(requerido)**: Question ID that is mapped for Auto CSAT configuration
- `questionnaireId` (string) **(requerido)**: Questionnaire ID corresponding to the Question ID that is mapped for Auto CSAT configuration
- `createdTime` (integer): This is the created time of the entity.
- `lastUpdatedTime` (integer): This is the updated time of the entity.

## Respuestas
- **201**: Created
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `questionId` (string) **(requerido)**: Question ID that is mapped for Auto CSAT configuration
  - `questionnaireId` (string) **(requerido)**: Questionnaire ID corresponding to the Question ID that is mapped for Auto CSAT configuration
  - `createdTime` (integer): This is the created time of the entity.
  - `lastUpdatedTime` (integer): This is the updated time of the entity.
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
