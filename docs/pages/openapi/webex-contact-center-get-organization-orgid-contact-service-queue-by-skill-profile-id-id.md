---
doc_id: webex-contact-center-get-organization-orgid-contact-service-queue-by-skill-profile-id-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/contact-service-queue/by-skill-profile-id/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.934457+00:00
---

# GET /organization/{orgid}/contact-service-queue/by-skill-profile-id/{id}

**API:** Webex Contact Center
**Área:** Contact Service Queue
**operationId:** `getSkillBasedCSQsBySkillProfileIdPublicContactServiceQueue`

## Resumen
List skill-based Contact Service Queues by skill profile ID (public)

## Descripción
Retrieve a list of skill-based Contact Service Queues associated with a given skill profile ID, accessible to authorized clients in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: ID of this contact center resource.

## Respuestas
- **200**: OK
  - `meta` (object): Additional properties for Meta.
  - `data` (array): List of Data.
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): Unique identifier of the contact service queue.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `channelType` (string): Channel type of the contact service queue (for example, `TELEPHONY`, `CHAT`, `EMAIL`, `SOCIAL`).
    - `name` (string): Display name of the contact service queue.
    - `skillScore` (integer): Aggregated score (0-100) of how well the queue's static skill requirements match the caller's skill profile. Higher is a better match.
    - `qsrType` (string): Type of queue skill requirement evaluated. Typical values: `PROFICIENCY`, `TEXT`, `BOOLEAN`, `ENUM`.
    - `dynamicSkillScore` (integer): Aggregated score (0-100) of how well the queue's dynamic skill requirements match the caller's supplied dynamic skill values.
    - `skillProfileSkillsMatch` (boolean): `true` if every static skill requirement defined on the queue is satisfied by the caller's skill profile.
    - `dynamicSkillsMatch` (boolean): `true` if every dynamic skill requirement defined on the queue is satisfied by the caller's dynamic skill values.
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
