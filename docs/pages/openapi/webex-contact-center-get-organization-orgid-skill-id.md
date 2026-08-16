---
doc_id: webex-contact-center-get-organization-orgid-skill-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/skill/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.949707+00:00
---

# GET /organization/{orgid}/skill/{id}

**API:** Webex Contact Center
**Área:** Skill
**operationId:** `getConfig_3`

## Resumen
Get specific Skill by ID

## Descripción
Retrieve an existing Skill by ID in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Skill.

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: Indicates the name of the skill. Once created, name cannot be modified.
  - `description` (string): Indicates the description of the skill.
  - `serviceLevelThreshold` (integer) **(requerido)**: Allows to set the time that a customer request can be in a queue before the system flags it as outside the service level.    If the agent completes a customer service request within this time interval, the system considers it within the service level.  It is required only for a create or an update operation.
  - `enumSkillValues` (array):
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string) **(requerido)**: Indicates the name of the enumSkillValue.
    - `description` (string): Indicates the description of the enumSkillValue.
    - `skillId` (string): Represents the skillId of the enumSkillValue.
    - `createdTime` (integer): This is the created time of the entity.
    - `lastUpdatedTime` (integer): This is the updated time of the entity.
  - `active` (boolean) **(requerido)**: Indicates the status of the skill whether it is active(when true) or not active(when false). It is required only during a create or an update operation.
  - `dynamicSkill` (boolean): Indicates whether the skill is a dynamic skill or not. Default value is false.
  - `skillType` (string) **(requerido)**: This can be of the following types  PROFICIENCY: id = 0  BOOLEAN: id = 1  TEXT: id = 2  ENUM: id = 3  Once created, skillType cannot be modified. Valores: Proficiency, Boolean, Text, enum.
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
