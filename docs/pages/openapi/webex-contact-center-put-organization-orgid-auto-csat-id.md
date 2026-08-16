---
doc_id: webex-contact-center-put-organization-orgid-auto-csat-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PUT
path: /organization/{orgid}/auto-csat/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.923714+00:00
---

# PUT /organization/{orgid}/auto-csat/{id}

**API:** Webex Contact Center
**Área:** Auto CSAT
**operationId:** `updateConfigAutoCSAT`

## Resumen
Update specific Auto CSAT resource by ID

## Descripción
Update an existing Auto CSAT resource by ID in a given organization. Deprecated. Use PUT /ai-feature/auto-csat/{id} instead.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Auto CSAT resource.

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `enabled` (boolean) **(requerido)**: Used to toggle the state of the Auto CSAT resource configuration from active to inactive and vice-versa. Mandatory for create/update operation.
- `agentInclusionType` (string) **(requerido)**: Provides information whether all or specific agents are selected for Auto CSAT. Valores: ALL, SPECIFIC.
- `surveyDataSource` (string) **(requerido)**: Survey Data Source Type Valores: EXPERIENCE_MANAGEMENT, GLOBAL_VARIABLE.
- `selectedGlobalVariableId` (string) **(requerido)**: Selected Global Variable ID
- `createdTime` (integer): This is the created time of the entity.
- `lastUpdatedTime` (integer): This is the updated time of the entity.

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `enabled` (boolean) **(requerido)**: Used to toggle the state of the Auto CSAT resource configuration from active to inactive and vice-versa. Mandatory for create/update operation.
  - `agentInclusionType` (string) **(requerido)**: Provides information whether all or specific agents are selected for Auto CSAT. Valores: ALL, SPECIFIC.
  - `surveyDataSource` (string) **(requerido)**: Survey Data Source Type Valores: EXPERIENCE_MANAGEMENT, GLOBAL_VARIABLE.
  - `selectedGlobalVariableId` (string) **(requerido)**: Selected Global Variable ID
  - `createdTime` (integer): This is the created time of the entity.
  - `lastUpdatedTime` (integer): This is the updated time of the entity.
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **412**: Resource referred in other entity(s). Please get all the reference entities info by invoking Get incoming-references api.
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
