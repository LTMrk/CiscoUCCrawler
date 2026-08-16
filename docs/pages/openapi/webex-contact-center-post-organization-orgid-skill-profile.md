---
doc_id: webex-contact-center-post-organization-orgid-skill-profile
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/skill-profile
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.950324+00:00
---

# POST /organization/{orgid}/skill-profile

**API:** Webex Contact Center
**Área:** Skill Profile
**operationId:** `createConfig_4`

## Resumen
Create a new Skill Profile

## Descripción
Create a new Skill Profile in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `skillProfileDTO` [query] () **(requerido)**: Skill profile configuration data

## Respuestas
- **201**: Created
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: Indicates the name of the skill Profile. It is required only during a create or an update operation.
  - `description` (string): A short description of the skill profile.
  - `activeSkills` (array) **(requerido)**: In activeSkills and activeEnumSkills at least one skill is mandatory.
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `textValue` (string): A short textual description that represents a skill the agent has.
    - `booleanValue` (boolean) **(requerido)**: Indicates whether the agent has this skill (True) or does not have the skill (False).
    - `proficiencyValue` (integer): A number between 0 and 10 to indicate how proficient the agent is in this skill.
    - `skillId` (string) **(requerido)**: Indicates a value that represents a skill the agent has.
    - `createdTime` (integer): This is the created time of the entity.
    - `lastUpdatedTime` (integer): This is the updated time of the entity.
    - `skillName` (string): Name of the skill, included in the payload only when 'includeSkillDetails' is true.
  - `activeEnumSkills` (array): Indicates a value that represents a skill the agent has.
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `enumSkillValueId` (string) **(requerido)**: ID of the enumSkillValue.
    - `createdTime` (integer): This is the created time of the entity.
    - `lastUpdatedTime` (integer): This is the updated time of the entity.
    - `enumSkillName` (string): Enum skill name, included in the payload only if 'includeSkillDetails' is true.
    - `enumSkillValue` (string): Enum skill value, included only if 'includeSkillDetails' is true.
    - `enumSkillId` (string): Enum skill ID, included only if 'includeSkillDetails' is true.
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
