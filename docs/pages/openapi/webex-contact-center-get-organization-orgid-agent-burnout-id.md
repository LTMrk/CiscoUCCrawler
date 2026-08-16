---
doc_id: webex-contact-center-get-organization-orgid-agent-burnout-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/agent-burnout/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.921697+00:00
---

# GET /organization/{orgid}/agent-burnout/{id}

**API:** Webex Contact Center
**Área:** Agent Wellbeing
**operationId:** `getConfigAgentBurnout`

## Resumen
Get specific Agent Burnout resource by ID

## Descripción
Retrieve an existing Agent Burnout resource by ID in a given organization. Deprecated. Use GET /ai-feature/agent-burnout/{id} instead.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Agent Burnout resource.

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `enabled` (boolean) **(requerido)**: Used to toggle the state of the agent burnout  configuration from active to inactive and vice-versa. Mandatory for create/update operation.
  - `agentInclusionType` (string) **(requerido)**: Provides information whether all or specific agents are selected for Agent Wellbeing. If the value is missing in response, the consumer should assume a value as ALL. Valores: ALL, SPECIFIC.
  - `wellnessBreakReminders` (string): Provides information whether Wellness break reminders are enabled or disabled. If the value is missing in response, the consumer should assume a value as DISABLED. Valores: DISABLED, ENABLED.
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
