---
doc_id: webex-contact-center-get-organization-orgid-v2-contact-service-queue-by-user-id-userid-agent-based-queues
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/v2/contact-service-queue/by-user-id/{userid}/agent-based-queues
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.936280+00:00
---

# GET /organization/{orgid}/v2/contact-service-queue/by-user-id/{userid}/agent-based-queues

**API:** Webex Contact Center
**Área:** Contact Service Queue
**operationId:** `getCSQByUserIDForAgentBasedQueueContactServiceQueue`

## Resumen
List agent-based Contact Service Queues by user ID

## Descripción
Retrieve a list of agent-based Contact Service Queues by user ID in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `userid` [path] (string) **(requerido)**:
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(firstName, lastName, email)  The examples below show some search queries - "Cisco" - field=="firstName";value=="Cisco" - fields=in=("firstName","lastName");value=="Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.

## Respuestas
- **200**: OK
  - `meta` (object): Additional properties for Meta.
  - `data` (array): List of Data.
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): Unique identifier of the contact service queue.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string): Display name of the contact service queue.
    - `routingPattern` (string): Routing pattern through which the agent is associated with this queue. Typical values: `TEAM_BASED`, `AGENT_BASED`, `SKILLS_BASED`.
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
