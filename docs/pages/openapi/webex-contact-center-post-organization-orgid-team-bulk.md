---
doc_id: webex-contact-center-post-organization-orgid-team-bulk
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/team/bulk
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.951391+00:00
---

# POST /organization/{orgid}/team/bulk

**API:** Webex Contact Center
**Área:** Team
**operationId:** `saveAllConfigTeam`

## Resumen
Bulk save Teams

## Descripción
Create, Update or delete Teams in bulk in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `items` (array): List of items in the bulk request.
  - `itemIdentifier` (integer): Unique item identifier for a bulk operation.
  - `item` (object): Team schema.
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string) **(requerido)**: Enter the name for the team. Generally, use names that indicate the function of the team, such as Billing or Customer Support. This field should be specified for create and update operation. Two teams in the same site in an organization cannot share the same name.
    - `teamType` (string) **(requerido)**: Team type can be the following:  AGENT: You assign a specific number of agents to the team.  CAPACITY: You don’t assign any specific number of agents to the team. You use capacity-based teams for voice mailboxes or agent groups that are not managed by the Webex Contact Center system.  Once created, teamType cannot be modified. Valores: AGENT, CAPACITY.
    - `teamStatus` (string) **(requerido)**: Select the status of the team to indicate whether the team is available to handle customer contacts. Can be one of: IN_SERVICE/NOT_AVAILABLE. Valores: IN_SERVICE, NOT_AVAILABLE.
    - `dialedNumber` (string): Enter the dial number where the system distributes the calls for this team.  This setting is applicable only for capacity-based teams.
    - `capacity` (integer): Enter the maximum number of simultaneous contacts that this team can handle. This setting is applicable only for capacity-based teams.
    - `active` (boolean) **(requerido)**: Specify whether the team is active or not Active.
    - `siteId` (string) **(requerido)**: Identifier for a site which is a physical contact center location under the control of your enterprise. Once specified, siteId should not be modified.
    - `desktopLayoutId` (string): Identifier for an agent desktop layout which  a Contact Center administrator has configured.
    - `skillProfileId` (string): (Optional) If your enterprise uses the optional Skills-Based Routing feature, you can select a skill profile for this team.  Note: You can’t assign this profile to a capacity-based team.
    - `multiMediaProfileId` (string): (Optional) If your organization administrator enables Multimedia for your enterprise, you can select a multimedia profile for this team.  Note: You can’t assign this profile to a capacity-based team.
    - `userIds` (array): Specify the agents id who will be part of this team.  Note: You can’t assign this profile to a capacity-based team.
    - `description` (string): Description.
    - `systemDefault` (boolean): Indicates whether the created resource is system created or not
    - `rankQueuesForTeam` (boolean) **(requerido)**: Indicates whether the queues should be ranked for the team.
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
  - `requestAction` (string): Identifier for action type. Possible values are `SAVE` and `DELETE`.

## Respuestas
- **207**: Multi-Status
  - `items` (array):
    - `itemIdentifier` (integer): Unique item identifier for a bulk operation.
    - `status` (integer): Indicates the error status code.
    - `operationType` (string): The kind of operation desired of an entity. Valores: CREATE, UPDATE, DELETE, GET.
    - `href` (string): The resource URI of an entity.
    - `apiError` (object): Response body for an API error.
      - `trackingId` (string): An opaque identifier for mapping protocol failures to service internal codes.   When specified in a request, it can be used for co-relating events across services
      - `error` (object): Details of an error.
        - `key` (string): An application defined error code.
        - `message` (array): A message providing details about the error.
          - `description` (string): A human readable explanation for the occurrence of an error.
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
