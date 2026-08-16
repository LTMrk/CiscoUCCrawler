---
doc_id: webex-contact-center-patch-organization-orgid-user-id-reskill
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PATCH
path: /organization/{orgid}/user/{id}/reskill
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.957487+00:00
---

# PATCH /organization/{orgid}/user/{id}/reskill

**API:** Webex Contact Center
**Área:** Users
**operationId:** `reSkillAgentUser`

## Resumen
Reskill Agents

## Descripción
Reskill agents by assigning or unassigning skills.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the User.

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `skillProfileId` (string): The unique identifier of the skill profile to assign to the agent
- `dynamicSkills` (object): Container for dynamic skills operations (add/remove)
  - `add` (array): List of dynamic skills to be added to the agent
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `userId` (string): The unique identifier of the user whose dynamic skills are being updated
    - `enumSkillValues` (array): Set of enumerated skill values for enum-type dynamic skills
    - `textValue` (string): Text value for text-type dynamic skills (maximum 100 characters)
    - `booleanValue` (boolean): Boolean value for boolean-type dynamic skills
    - `proficiencyValue` (integer): Proficiency value for proficiency-type dynamic skills (range: 0-10)
    - `skillId` (string): The unique identifier of the dynamic skill being updated
    - `createdTime` (integer): This is the created time of the entity.
    - `lastUpdatedTime` (integer): This is the updated time of the entity.
  - `remove` (array): List of dynamic skill IDs to be removed from the agent
- `createdTime` (integer): This is the created time of the entity.
- `lastUpdatedTime` (integer): This is the updated time of the entity.

## Respuestas
- **204**: No Content
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
