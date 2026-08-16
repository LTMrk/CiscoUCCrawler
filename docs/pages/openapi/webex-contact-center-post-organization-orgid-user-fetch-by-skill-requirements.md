---
doc_id: webex-contact-center-post-organization-orgid-user-fetch-by-skill-requirements
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/user/fetch-by-skill-requirements
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.954991+00:00
---

# POST /organization/{orgid}/user/fetch-by-skill-requirements

**API:** Webex Contact Center
**Área:** Users
**operationId:** `getUsersBySkillRequirementsUser`

## Resumen
Get the agents matching skill requirements criteria

## Descripción
This API can be used to fetch the agents who match the provided skill requirements criteria. Maximum of 50 skill requirements criteria can be passed in the request.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(firstName, lastName, email)  The examples below show some search queries - "Cisco" - field=="firstName";value=="Cisco" - fields=in=("firstName","lastName");value=="Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.

## Cuerpo de la petición (application/json)
- `skillRequirements` (array):
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `skillId` (string) **(requerido)**: Skill ID reference
  - `skillName` (string): Indicates the name of the skill. Once created, name cannot be modified.
  - `skillType` (string): This can be of the following types  PROFICIENCY: id = 0  BOOLEAN: id = 1  TEXT: id = 2  ENUM: id = 3  Once created, skillType cannot be modified.
  - `condition` (string) **(requerido)**: Indicates a value that represents a skill the agent has.
  - `skillValue` (string) **(requerido)**: A short textual description that represents a skill the agent has.
  - `weight` (integer): Weight for proficiency skill requirement
  - `dynamicSkill` (boolean): Indicates whether the skill is a dynamic skill or not. Default value is false.
  - `createdTime` (integer): This is the created time of the entity.
  - `lastUpdatedTime` (integer): This is the updated time of the entity.

### Ejemplo de petición
```json
{
  "skillRequirements": [
    {
      "organizationId": "0271223b-91de-427d-872a-1b3c1bb746b9",
      "id": "5e8cdad5-94da-4ffc-86d7-c904e4490626",
      "skillId": "bc5658a9-5aa7-45ec-b960-43dcfc73c34d",
      "skillName": "skillA",
      "skillType": "TEXT",
      "condition": "IS",
      "skillValue": "abc"
    },
    {
      "condition": "IS",
      "skillValue": "8",
      "skillName": "ProfSkillC",
      "skillType": "PROFICIENCY",
      "skillId": "c683cf8d-49e8-4e85-9e08-c8749affa9cc"
    }
  ]
}
```

## Respuestas
- **200**: OK
  - `meta` (object): Metadata of response with paging information
    - `orgid` (string): Organization ID.
    - `page` (integer): Current page number.
    - `pageSize` (integer): Page size for current data set.
    - `totalPages` (integer): Number of pages.
    - `totalRecords` (integer): Total number of items.
    - `links` (object): Map of pagination links with `self`, `next`, `prev`, `last`, and `first`.
  - `data` (array):
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `firstName` (string): The first name of the user. Can be changed using Users Management in Cisco Webex Control Hub.
    - `lastName` (string): The last name of the user. Can be changed using Users Management in Cisco Webex Control Hub.
    - `email` (string): The email address of the user. Can be changed using Users Management in Cisco Webex Control Hub.
    - `skillProfileName` (string): The skillProfileName  of the user.
    - `createdTime` (integer): This is the created time of the entity.
    - `lastUpdatedTime` (integer): This is the updated time of the entity.
  - `meta` (object): Metadata of response with paging information
    - `orgid` (string): Organization ID.
    - `page` (integer): Current page number.
    - `pageSize` (integer): Page size for current data set.
    - `totalPages` (integer): Number of pages.
    - `totalRecords` (integer): Total number of items.
    - `links` (object): Map of pagination links with `self`, `next`, `prev`, `last`, and `first`.
  - `data` (array):
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `firstName` (string): The first name of the user. Can be changed using Users Management in Cisco Webex Control Hub.
    - `lastName` (string): The last name of the user. Can be changed using Users Management in Cisco Webex Control Hub.
    - `email` (string): The email address of the user. Can be changed using Users Management in Cisco Webex Control Hub.
    - `skillProfileName` (string): The skillProfileName  of the user.
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
