---
doc_id: webex-contact-center-post-organization-orgid-v2-contact-service-queue-fetch-by-grouped-assistant-skill
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/v2/contact-service-queue/fetch-by-grouped-assistant-skill
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.936613+00:00
---

# POST /organization/{orgid}/v2/contact-service-queue/fetch-by-grouped-assistant-skill

**API:** Webex Contact Center
**Área:** Contact Service Queue
**operationId:** `getAllCSQGroupedAssistantSkillContactServiceQueue`

## Resumen
List queue mapping summary grouped by Assistant Skill

## Descripción
Retrieve a list of queue mapping summary for a specified list of Assistant Skills specified in a given organization. The summary currently includes mapped queue count, and the last assigned time of queue mapping.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.

## Cuerpo de la petición (application/json)
- `assistantSkillIds` (array): List of AssistantSkill ids to fetch. If property is unspecified or set to null, then all assistantSkillIds mapped will be returned.

## Respuestas
- **200**: OK
  - `meta` (object): Additional properties for Meta.
  - `data` (array): List of Data.
    - `assistantSkillId` (string): ID of Assistant Skill in AI Studio
    - `associatedQueueCount` (integer): Number of queues mapped to this Assistant Skill ID
    - `lastAssistantSkillUpdatedTime` (integer): Last updated time Assistant Skill mapping i.e. timestamp corresponding to most recently added queue mapping
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
