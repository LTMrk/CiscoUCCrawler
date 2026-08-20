---
doc_id: webex-contact-center-post-orgid-project-projectid-flows-flowid-publish
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /{orgId}/project/{projectId}/flows/{flowId}:publish
operation_id: publishFlowVersionUsingPOST
tags: Flows
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.737873+00:00
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
- `flowId` [path] (string) (**requerido**): ID of the flow/subflow to publish.
- `orgId` [path] (string) (**requerido**): Organization ID.
- `projectId` [path] (string) (**requerido**): Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `TrackingId` [header] (string): ID for tracking.
- `skipValidation` [query] (boolean): If true, the flow's pre-publish validation is skipped. Use with care. Por defecto: False.
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW'. Por defecto: FLOW.

## Cuerpo de la petición (application/json)
- `comment` (string): A comment to provide context on publishing the flow.
- `tagIds` (array): Tag IDs appropriate to this version. It must be one of 'Live', 'Test', 'Dev', 'Latest.

## Ejemplo de invocación
```bash
curl -X POST '/<orgId>/project/<projectId>/flows/<flowId>:publish' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `associatedChannels` (array): Channels associated with the flow.
  - `channelType` (string): Channel type associated with the flow version.
  - `id` (string): Identifier of the associated channel.
  - `name` (string): Display name of the associated channel.
- `assignedRS` (array): Assigned Routing Strategy.
- `createdBy` (string): Email of the account which created the flow.
- `createdDate` (string/date-time): Date of creation of the flow.
- `draftVersion` (object): Represents a specific version of a flow or subflow, including diagram, process, variables, and validation details.
  - `associatedChannels` (array): Channels associated with the flow version. Export and import payloads preserve this metadata so channel-specific activities, such as custom messaging activities, can be validated and resolved correctly.
    - `channelType` (string): Channel type associated with the flow version.
    - `id` (string): Identifier of the associated channel.
    - `name` (string): Display name of the associated channel.
  - `comment` (string): Publish note
  - `createdBy` (string): Email of the account which created the flow version
  - `createdDate` (string/date-time): Date of creation of the version object
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
  - `lastModifiedDate` (string/date-time): Date the version object is last modified
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
    - `description` (string): Determines whether the variable needs to be visible on the UI
    - `displayName` (string): Display name of the activity
    - `isSecure` (boolean): Determines whether a variable is marked sensitive
    - `name` (string): Name of the runtime variable
    - `path` (string): Path of the runtime variable
    - `source` (string): Source of the runtime variable. Either 'Event' or 'Activity'
    - `type` (string): Data type of the runtime variable
    - `uiVisible` (boolean): Determines whether the variable needs to be visible on the UI
  - `settings` (array): Settings for the flow version
    - `group` (string): The group the setting belongs to.
    - `name` (string): The name of the flow version setting
    - `type` (string): The setting type.
    - `value` (string): The setting value.
  - `validating` (boolean): Determines whether the version object needs to be validated
  - `validationResults` (array): Validation errors are stored here
    - `activityId` (string): Activity identifier
    - `activityLabel` (string): Activity label
    - `code` (string): Error code
    - `docLink` (string): Document link
    - `message` (string): Error message to be displayed on the UI

### Ejemplo — respuesta 200
```json
{
  "id": "65c28d9db2a2375974066579",
  "projectId": "5e5c9ad6d61f870d6d778c1b",
  "orgId": "8eb7da9a-c81c-4d13-b08b-38fdeb7330d8",
  "flowType": "FLOW",
  "status": "Draft",
  "version": 1
}
```
**201**: Created

## Respuestas de error
- **400**: Bad request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **500**: Internal Server Error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs