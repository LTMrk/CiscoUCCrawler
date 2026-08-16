---
doc_id: webex-contact-center-get-organization-orgid-user-by-dynamic-skill-id-skillid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/user/by-dynamic-skill-id/{skillId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.954814+00:00
---

# GET /organization/{orgid}/user/by-dynamic-skill-id/{skillId}

**API:** Webex Contact Center
**Área:** Users
**operationId:** `getUsersByDynamicSkillIdUser`

## Resumen
Get users by dynamic skill ID

## Descripción
Fetches all users assigned to a specific dynamic skill with search and pagination support. Returns user details with the specific dynamic skill value.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `skillId` [path] (string) **(requerido)**: The dynamic skill ID to fetch users for
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(firstName, lastName, email, value)  The examples below show some search queries - "Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.

## Respuestas
- **200**: OK
  - `meta` (object): Additional properties for Meta.
  - `data` (array): List of Data.
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `firstName` (string): The first name of the user.
    - `lastName` (string): The last name of the user.
    - `email` (string): The email address of the user.
    - `dynamicSkill` (object): Data transfer object representing dynamic skills assigned to a user
      - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
      - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
      - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
      - `skillId` (string) **(requerido)**: The ID of the skill.
      - `skillName` (string): The name of the skill. Used for bulk upload operations to resolve skill by name instead of ID.
      - `textValue` (string): A short textual description that represents a skill the agent has.
      - `booleanValue` (boolean): Indicates whether the agent has this skill (True) or does not have the skill (False).
      - `proficiencyValue` (integer): A number between 0 and 10 to indicate how proficient the agent is in this skill.
      - `enumValue` (string): The enum value for enum-type skills. Supports multiple values as pipe-delimited string (e.g., '30|20|10').
      - `enumSkillValues` (string): Indicates a value that represents a skill the agent has.
      - `createdTime` (integer): This is the created time of the entity.
      - `lastUpdatedTime` (integer): This is the updated time of the entity.
  - `meta` (object): Additional properties for Meta.
  - `data` (array): List of Data.
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `firstName` (string): The first name of the user.
    - `lastName` (string): The last name of the user.
    - `email` (string): The email address of the user.
    - `dynamicSkill` (object): Data transfer object representing dynamic skills assigned to a user
      - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
      - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
      - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
      - `skillId` (string) **(requerido)**: The ID of the skill.
      - `skillName` (string): The name of the skill. Used for bulk upload operations to resolve skill by name instead of ID.
      - `textValue` (string): A short textual description that represents a skill the agent has.
      - `booleanValue` (boolean): Indicates whether the agent has this skill (True) or does not have the skill (False).
      - `proficiencyValue` (integer): A number between 0 and 10 to indicate how proficient the agent is in this skill.
      - `enumValue` (string): The enum value for enum-type skills. Supports multiple values as pipe-delimited string (e.g., '30|20|10').
      - `enumSkillValues` (string): Indicates a value that represents a skill the agent has.
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
