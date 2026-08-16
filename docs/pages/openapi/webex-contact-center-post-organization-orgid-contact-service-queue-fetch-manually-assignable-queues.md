---
doc_id: webex-contact-center-post-organization-orgid-contact-service-queue-fetch-manually-assignable-queues
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/contact-service-queue/fetch-manually-assignable-queues
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.934934+00:00
---

# POST /organization/{orgid}/contact-service-queue/fetch-manually-assignable-queues

**API:** Webex Contact Center
**Área:** Contact Service Queue
**operationId:** `getManuallyAssignableCSQsContactServiceQueue`

## Resumen
List manually assignable Contact Service Queues

## Descripción
Retrieve a list of Contact Service Queues that are eligible for manual contact assignment based on the provided criteria in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `agentId` (string): Unique identifier of the agent (CI user ID) for whom manually assignable queues should be retrieved.
- `teamId` (string): Unique identifier of the team that the agent belongs to. Used to scope the queues that the agent can be manually assigned contacts from.

## Respuestas
- **200**: Successfully fetched the manually assignable contact service queues for the given agent and team.
  - `data` (array): List of manually assignable contact service queues for the given agent and team.
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
