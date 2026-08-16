---
doc_id: webex-contact-center-post-orgid-project-projectid-flows-flowid-publish
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /{orgId}/project/{projectId}/flows/{flowId}:publish
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.966480+00:00
---

# POST /{orgId}/project/{projectId}/flows/{flowId}:publish

**API:** Webex Contact Center
**Área:** Flows
**operationId:** `publishFlowVersionUsingPOST`

## Resumen
Publish a Flow or Subflow

## Descripción
Returns the published flow in response.

The Publish API validates the basic structure of the flows. We recommend manually verifying the published flows before proceeding with live traffic.

Scope: `cjp:config_write`. Roles: [`Organizational Full Admin`, `Supervisor`, `Contact Center Service Admin`, `User Admin`]

## Parámetros
- `flowId` [path] (string) **(requerido)**: ID of the flow/subflow to publish.
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `projectId` [path] (string) **(requerido)**: Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `TrackingId` [header] (string): ID for tracking.
- `skipValidation` [query] (boolean): If true, the flow's pre-publish validation is skipped. Use with care.
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW'.

## Cuerpo de la petición (application/json)
- `comment` (string): A comment to provide context on publishing the flow.
- `tagIds` (array): Tag IDs appropriate to this version. It must be one of 'Live', 'Test', 'Dev', 'Latest.

## Respuestas
- **200**: OK
  - `associatedChannels` (array): Channels associated with the flow.
    - `channelType` (string): Channel type associated with the flow version.
    - `id` (string): Identifier of the associated channel.
    - `name` (string): Display name of the associated channel.
  - `assignedRS` (array): Assigned Routing Strategy.
  - `createdBy` (string): Email of the account which created the flow.
  - `createdDate` (string): Date of creation of the flow.
  - `draftVersion` (object): Represents a specific version of a flow or subflow, including diagram, process, variables, and validation details.
    - `associatedChannels` (array): Channels associated with the flow version. Export and import payloads preserve this metadata so channel-specific activities, such as custom messaging activities, can be validated and resolved correctly.
      - `channelType` (string): Channel type associated with the flow version.
      - `id` (string): Identifier of the associated channel.
      - `name` (string): Display name of the associated channel.
    - `comment` (string): Publish note
    - `createdBy` (string): Email of the account which created the flow version
    - `createdDate` (string): Date of creation of the version object
    - `description` (string): Description of the Flow Version
    - `diagram` (object): Represents the visual graph metadata for a flow, including widgets and additional diagram properties.
      - `properties` (object): Additional properties are listed here
      - `widgets` (object): Holds the activities and links
    - `eventFlows` (object): Represents event-specific flow diagrams and global event mappings for a flow version.
      - `eventsMap` (object): Holds global events
      - `properties` (object): Holds information on additional properties
    - `flowId` (string): Flow/Subflow ID to which the version belongs
    - `flowType` (string): Flow Type (FLOW/SUBFLOW). Default value is FLOW
    - `id` (string): Version object ID
    - `lastModifiedBy` (string): Email of the account which modified the flow version last
    - `lastModifiedDate` (string): Date the version object is last modified
    - `name` (string): Name of the Flow Version
    - `orgId` (string): Organization ID
    - `persist` (boolean): Determines whether the version object needs to be persisted in the DB
    - `process` (object): Represents the executable process graph for a flow version, including activities and links.
      - `activities` (object): Stores list of activities/events
      - `links` (array): Stores list of links
        - `conditionExpr` (string): Condition expression. It is one of 'out', and 'default'
        - `id` (string): Link ID
        - `properties` (object): Additional properties are stored here
        - `sourceActivityId` (string): Activity from which the link originates
        - `targetActivityId` (string): Activity to which the link connects
    - `runtimeVariables` (array): Output variables of the activities configured in the flow
      - `activityName` (string): Name of the activity
- **201**: Created
- **400**: Bad request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **500**: Internal Server Error

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
