---
doc_id: webex-contact-center-put-organization-orgid-team-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PUT
path: /organization/{orgid}/team/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.951743+00:00
---

# PUT /organization/{orgid}/team/{id}

**API:** Webex Contact Center
**Área:** Team
**operationId:** `updateConfigTeam`

## Resumen
Update specific Team by ID

## Descripción
Update an existing Team by ID in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Team.
- `teamDTO` [query] () **(requerido)**:

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string): Indicates the name of the team such as Billing or Customer Support
  - `teamType` (string): Team type can be the following:  AGENT: A specific number of agents are assigned to the team.  CAPACITY: Specific number of agents not assigned to the team. Capacity-based teams for voice mailboxes or agent groups that are not managed by the Webex Contact Center system. Valores: AGENT, CAPACITY.
  - `teamStatus` (string): Indicates whether the team is available to handle customer contacts. Can be one of: IN_SERVICE/NOT_AVAILABLE. Valores: IN_SERVICE, NOT_AVAILABLE.
  - `dialedNumber` (string): The dial number where the system distributes the calls for this team.  This setting is applicable only for capacity-based teams.
  - `capacity` (integer): The maximum number of simultaneous contacts that this team can handle. This setting is applicable only for capacity-based teams.
  - `active` (boolean): Indicates whether the team is active(when true) or not active(when false).
  - `siteId` (string): Identifier for a site which is a physical contact center location under the control of your enterprise.
  - `desktopLayoutId` (string): Identifier for an agent desktop layout which  a Contact Center administrator has configured.
  - `siteName` (string): The name of the site this team belongs to.
  - `skillProfileId` (string): Id of the skill profile for this team if your enterprise uses the optional Skills-Based Routing feature.
  - `multiMediaProfileId` (string): Id of the multimedia profile for this team.
  - `userIds` (array): Indicates the agents id(s) who are part of this team.
  - `description` (string): Indicates the team
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not
  - `rankQueuesForTeam` (boolean): Rank Queues For Team.
  - `queueRankings` (array): List of Queue Rankings.
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `queueId` (string) **(requerido)**: Queue Id.
    - `rank` (integer) **(requerido)**: Rank.
    - `createdTime` (integer): This is the created time of the entity.
    - `lastUpdatedTime` (integer): This is the updated time of the entity.
  - `createdTime` (integer): This is the created time of the entity.
  - `lastUpdatedTime` (integer): This is the updated time of the entity.
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **412**: Resource referred in other entity(s). Please get all the reference entities info by invoking Get incoming-references api.
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
