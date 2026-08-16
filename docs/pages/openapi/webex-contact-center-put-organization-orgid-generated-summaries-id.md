---
doc_id: webex-contact-center-put-organization-orgid-generated-summaries-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PUT
path: /organization/{orgid}/generated-summaries/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.924118+00:00
---

# PUT /organization/{orgid}/generated-summaries/{id}

**API:** Webex Contact Center
**Área:** Generated Summaries
**operationId:** `updateConfigGeneratedSummaries`

## Resumen
Update specific Generated Summaries resource by ID

## Descripción
Update an existing Generated Summaries resource by ID in a given organization. Deprecated. Use PUT /ai-feature/generated-summaries/{id} instead.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Generated Summaries resource.

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `callDropSummariesEnabled` (boolean): Used to toggle the enable/disable call drop summaries for Generated Summaries configuration. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
- `virtualAgentTransferSummariesEnabled` (boolean): Used to toggle the enable/disable virtual agent transfer summaries for Generated Summaries configuration. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
- `consultTransferSummariesEnabled` (boolean): Used to toggle the enable/disable mid call consult/transfer summaries in Generated Summaries configuration. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
- `agentInclusionType` (string): Provides information whether all or specific agents are selected for generated summaries. Valores: ALL, SPECIFIC.
- `createdTime` (integer): This is the created time of the entity.
- `lastUpdatedTime` (integer): This is the updated time of the entity.

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `callDropSummariesEnabled` (boolean): Used to toggle the enable/disable call drop summaries for Generated Summaries configuration. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
  - `virtualAgentTransferSummariesEnabled` (boolean): Used to toggle the enable/disable virtual agent transfer summaries for Generated Summaries configuration. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
  - `consultTransferSummariesEnabled` (boolean): Used to toggle the enable/disable mid call consult/transfer summaries in Generated Summaries configuration. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
  - `agentInclusionType` (string): Provides information whether all or specific agents are selected for generated summaries. Valores: ALL, SPECIFIC.
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
