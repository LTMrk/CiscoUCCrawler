---
doc_id: webex-contact-center-get-organization-orgid-user-by-dynamic-skill-id-skillid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/user/by-dynamic-skill-id/{skillId}
operation_id: getUsersByDynamicSkillIdUser
tags: Users
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.783799+00:00
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
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `skillId` [path] (string) (**requerido**): The dynamic skill ID to fetch users for
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(firstName, lastName, email, value)  The examples below show some search queries - "Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/user/by-dynamic-skill-id/<skillId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `meta` (object): Additional properties for Meta.
- `data` (array): List of Data.
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `firstName` (string): The first name of the user.
  - `lastName` (string): The last name of the user.
  - `email` (string): The email address of the user.
  - `dynamicSkill` (object): Data transfer object representing dynamic skills assigned to a user
    - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `skillId` (string) (**requerido**): The ID of the skill.
    - `skillName` (string): The name of the skill. Used for bulk upload operations to resolve skill by name instead of ID.
    - `textValue` (string): A short textual description that represents a skill the agent has. Long. max: 100.
    - `booleanValue` (boolean): Indicates whether the agent has this skill (True) or does not have the skill (False).
    - `proficiencyValue` (integer/int32): A number between 0 and 10 to indicate how proficient the agent is in this skill.
    - `enumValue` (string): The enum value for enum-type skills. Supports multiple values as pipe-delimited string (e.g., '30|20|10').
    - `enumSkillValues` (string): Indicates a value that represents a skill the agent has.
    - `createdTime` (integer/int64): This is the created time of the entity.
    - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
- `meta` (object): Additional properties for Meta.
- `data` (array): List of Data.
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `firstName` (string): The first name of the user.
  - `lastName` (string): The last name of the user.
  - `email` (string): The email address of the user.
  - `dynamicSkill` (object): Data transfer object representing dynamic skills assigned to a user
    - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `skillId` (string) (**requerido**): The ID of the skill.
    - `skillName` (string): The name of the skill. Used for bulk upload operations to resolve skill by name instead of ID.
    - `textValue` (string): A short textual description that represents a skill the agent has. Long. max: 100.
    - `booleanValue` (boolean): Indicates whether the agent has this skill (True) or does not have the skill (False).
    - `proficiencyValue` (integer/int32): A number between 0 and 10 to indicate how proficient the agent is in this skill.
    - `enumValue` (string): The enum value for enum-type skills. Supports multiple values as pipe-delimited string (e.g., '30|20|10').
    - `enumSkillValues` (string): Indicates a value that represents a skill the agent has.
    - `createdTime` (integer/int64): This is the created time of the entity.
    - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

## Respuestas de error
- **401**: Unauthorized Operation
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "401",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "401",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **403**: Operation is forbidden
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "403",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "403",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **404**: Resource not found or URI is invalid
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "404",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "404",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "429",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "429",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **500**: An Unexpected Error Occurred
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "500",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "500",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs