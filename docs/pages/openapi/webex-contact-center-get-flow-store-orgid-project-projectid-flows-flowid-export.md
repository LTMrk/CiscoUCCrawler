---
doc_id: webex-contact-center-get-flow-store-orgid-project-projectid-flows-flowid-export
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /flow-store/{orgId}/project/{projectId}/flows/{flowId}:export
operation_id: exportFlowVersionUsingGET
tags: Legacy Flows
deprecated: true
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.153175+00:00
---

# GET /flow-store/{orgId}/project/{projectId}/flows/{flowId}:export

> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.

**API:** Webex Contact Center
**Área:** Legacy Flows
**operationId:** `exportFlowVersionUsingGET`

## Resumen
Export a Flow or Subflow

## Descripción
**Deprecated.** Use the Flow export endpoint (`GET /flow-store/{orgId}/project/{projectId}/v2/flows/{flowId}:export`, operationId `exportFlowV2`) instead. The V1 Flow APIs operate on the raw FDL format and will continue to function but will not receive new features.

Returns the exported flow/subflow in response, including associated channel metadata used to preserve channel-specific activity behavior during export and re-import.

Scope: `cjp:config_read`. Roles: [`Organizational Full Admin`, `Supervisor`, `Contact Center Service Admin`, `User Admin`]

## Parámetros
- `flowId` [path] (string) (**requerido**): ID of the flow/subflow to export.
- `orgId` [path] (string) (**requerido**): Organization ID.
- `projectId` [path] (string) (**requerido**): Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `version` [query] (string): Version ID. Possible values are 'draft', 'latest' or version ID like '64b92c004ccd9f3d1c680709'. Defaulted to 'latest'. Por defecto: latest.
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW'. Por defecto: FLOW.

## Ejemplo de invocación
```bash
curl -X GET '/flow-store/<orgId>/project/<projectId>/flows/<flowId>:export' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
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
  - `severity` (string): Severity of the error. Either ERROR or RECOMMENDATION
- `variableOrders` (object): Determines the order in which variables appear in the Agent's desktop
- `variables` (array): Variables in the version object
  - `description` (string): Description for the variable
  - `desktopLabel` (string): Variable name shown on Agent Desktop
  - `id` (string): Identifier for the variable
  - `isAgentEditable` (boolean): Determines whether is eligible for desktop agent to edit
  - `isCAD` (boolean): Determines whether variable is agent viewable

### Ejemplo — respuesta 200
```json
{
  "id": "65c28d9db2a2375974066579",
  "flowId": "661c7bc712eaf357de7e4aeb",
  "name": "TestFlow",
  "flowType": "FLOW",
  "orgId": "8eb7da9a-c81c-4d13-b08b-38fdeb7330d8",
  "version": 1,
  "validating": false
}
```

## Respuestas de error
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs