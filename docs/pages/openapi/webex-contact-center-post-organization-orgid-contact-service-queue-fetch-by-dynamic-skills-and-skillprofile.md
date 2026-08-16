---
doc_id: webex-contact-center-post-organization-orgid-contact-service-queue-fetch-by-dynamic-skills-and-skillprofile
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/contact-service-queue/fetch-by-dynamic-skills-and-skillProfile
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.934713+00:00
---

# POST /organization/{orgid}/contact-service-queue/fetch-by-dynamic-skills-and-skillProfile

**API:** Webex Contact Center
**Área:** Contact Service Queue
**operationId:** `getSkillBasedCSQsByDynamicSkillsAndSkillProfileContactServiceQueue`

## Resumen
List skill-based Contact Service Queues by dynamic skills and skill profile

## Descripción
Retrieve a list of skill-based Contact Service Queues that match the given dynamic skills and skill profile criteria in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `skillProfileId` (string): Unique identifier of the skill profile to look up queues for.
- `dynamicSkills` (array): Dynamic skill values used to further narrow down the matching skill-based queues. Used by the dynamic-skills lookup endpoint.
  - `skillId` (string): The unique identifier of the dynamic skill
  - `textValue` (string): Text value for text-type dynamic skills
  - `booleanValue` (boolean): Boolean value for boolean-type dynamic skills
  - `proficiencyValue` (integer): Proficiency value for proficiency-type dynamic skills (range: 0-10)
  - `enumSkillValues` (array): Set of enumerated skill values for enum-type dynamic skills
- `userId` (string): Unique identifier of the user (agent) whose skill-based queues should be retrieved. Used by the user-and-skill-profile lookup endpoint.

## Respuestas
- **200**: OK
  - `meta` (object): Additional properties for Meta.
  - `data` (array): List of Data.
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): Unique identifier of the contact service queue.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `channelType` (string): Channel type of the contact service queue (for example, `TELEPHONY`, `CHAT`, `EMAIL`, `SOCIAL`).
    - `name` (string): Display name of the contact service queue.
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
