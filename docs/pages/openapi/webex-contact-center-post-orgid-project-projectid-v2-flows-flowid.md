---
doc_id: webex-contact-center-post-orgid-project-projectid-v2-flows-flowid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /{orgId}/project/{projectId}/v2/flows/{flowId}
operation_id: saveFlowV2Draft
tags: Flows
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.758629+00:00
---

# POST /{orgId}/project/{projectId}/v2/flows/{flowId}

**API:** Webex Contact Center
**Área:** Flows
**operationId:** `saveFlowV2Draft`

## Resumen
Save a Flow Draft

## Descripción
Save a complete flow document as the current draft, replacing the existing draft. Pass `expectedVersion` as a query parameter to enable optimistic locking; the request fails with `409 Conflict` if the server-side version does not match. Omit `expectedVersion` to skip the check.

Scope: `cjp:config_write`

## Parámetros
- `orgId` [path] (string) (**requerido**): Organization ID.
- `projectId` [path] (string) (**requerido**): Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `flowId` [path] (string) (**requerido**): Flow ID.
- `expectedVersion` [query] (integer/int32): Expected current draft version for optimistic locking. The request fails with 409 Conflict if the server-side version does not match. Omit to skip the check.
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW'. Por defecto: FLOW.

## Cuerpo de la petición (application/json)
- `flowName` (string): Name of the flow.
- `flowType` (string): Flow type. One of `FLOW` or `SUBFLOW`. Valores: FLOW, SUBFLOW.
- `contactType` (string): Channel type the flow is intended for (for example, `telephony`, `customMessaging`, `workItem`, `genericAction`).
- `description` (string): Human-readable description of the flow.
- `version` (integer/int64): Monotonically increasing version number of the document.
- `status` (string): Lifecycle state of the document. One of `Draft` or `Published`. Valores: Draft, Published.
- `nodes` (array): Activity nodes in the main flow process.
  - `name` (string): Stable, unique node name within the flow. Used as the patch-merge key for `upsert_nodes` and `remove_node_names`.
  - `activityName` (string): Activity type this node instantiates. Must match an `activityName` returned by `listActivityDefinitions`.
  - `inputs` (object): Input values for the activity, keyed by input name. Shape depends on the activity definition.
  - `outputs` (object): Declared output bindings for the activity, keyed by output name. Used to map activity outputs to flow variables.
  - `position` (object): Node position on the flow canvas.
    - `x` (number): Horizontal coordinate in pixels.
    - `y` (number): Vertical coordinate in pixels.
- `edges` (array): Edges connecting nodes in the main flow process.
  - `key` (string): Stable, unique edge key within the flow. Used as the patch-merge key for `upsert_edges` and `remove_edge_keys`.
  - `from_node` (string): Name of the source node. Must reference a node in the same process.
  - `from_port` (string): Output port name on the source node. Must match an `outputPorts[].name` exposed by the source activity definition.
  - `to_node` (string): Name of the target node. Must reference a node in the same process.
  - `condition` (string): Branch condition this edge fires on. Aliases: `done` -> `out`, `NewPhoneContact` -> `out`, `defaultBranch` -> `default`.
- `variables` (array): Flow variables.
  - `name` (string): Variable name.
  - `type` (string): Variable data type (for example, `STRING`, `INTEGER`, `BOOLEAN`).
  - `value` (string): Default value as a string.
  - `description` (string): Human-readable description of the variable.
  - `isCAD` (boolean): True if this variable is exposed as Call-Associated Data.
  - `isAgentEditable` (boolean): True if agents can edit the variable value at runtime.
  - `isReportable` (boolean): True if the variable is included in reporting.
  - `isSecure` (boolean): True if the variable holds sensitive data and must be masked in logs and reports.
- `eventFlows` (array): Event-handler subflows bound to specific events.
  - `event` (string): Name of the event this subflow handles. Must reference an event from `listEventSpecifications`.
  - `nodes` (array): Activity nodes in the event-handler process.
    - `name` (string): Stable, unique node name within the flow. Used as the patch-merge key for `upsert_nodes` and `remove_node_names`.
    - `activityName` (string): Activity type this node instantiates. Must match an `activityName` returned by `listActivityDefinitions`.
    - `inputs` (object): Input values for the activity, keyed by input name. Shape depends on the activity definition.
    - `outputs` (object): Declared output bindings for the activity, keyed by output name. Used to map activity outputs to flow variables.
    - `position` (object): Node position on the flow canvas.
      - `x` (number): Horizontal coordinate in pixels.
      - `y` (number): Vertical coordinate in pixels.
  - `edges` (array): Edges in the event-handler process.
    - `key` (string): Stable, unique edge key within the flow. Used as the patch-merge key for `upsert_edges` and `remove_edge_keys`.
    - `from_node` (string): Name of the source node. Must reference a node in the same process.
    - `from_port` (string): Output port name on the source node. Must match an `outputPorts[].name` exposed by the source activity definition.
    - `to_node` (string): Name of the target node. Must reference a node in the same process.
    - `condition` (string): Branch condition this edge fires on. Aliases: `done` -> `out`, `NewPhoneContact` -> `out`, `defaultBranch` -> `default`.
- `preferences` (array): Flow-level preferences.
  - `name` (string): Preference name.
  - `type` (string): Preference value type.
  - `value` (string): Preference value, encoded as a string.

### Ejemplo — petición
```json
{
  "flowName": "Customer_Support_Main",
  "flowType": "FLOW",
  "contactType": "telephony",
  "description": "Routes inbound support calls to the main support queue.",
  "version": 3,
  "status": "Draft",
  "nodes": [
    {
      "name": "NewPhoneContact",
      "activityName": "NewPhoneContact",
      "inputs": {},
      "outputs": {},
      "position": {
        "x": 100,
        "y": 200
      }
    },
    {
      "name": "PlayMessage_1",
      "activityName": "PlayMessage",
      "inputs": {
        "audioFile": "welcome.wav"
      },
      "outputs": {},
      "position": {
        "x": 300,
        "y": 200
      }
    }
  ],
  "edges": [
    {
      "key": "edge-1",
      "from_node": "NewPhoneContact",
      "from_port": "out",
      "to_node": "PlayMessage_1",
      "condition": "out"
    }
  ],
  "variables": [
    {
      "name": "FlowVar1",
      "type": "STRING",
      "value": "var1",
      "description": "",
      "isCAD": true,
      "isAgentEditable": true,
      "isReportable": false,
      "isSecure": false
    }
  ],
  "eventFlows": [],
  "preferences": [
    {
      "name": "hideSecureCADWarning",
      "type": "Boolean",
      "value": "true"
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/<orgId>/project/<projectId>/v2/flows/<flowId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: Updated flow metadata, including the new `version`.
- `flow` (object): The persisted flow document, including the server-assigned `id`.
- `preflightWarnings` (array): Non-blocking warnings raised while persisting the flow (for example, references that resolve but are flagged for review). Empty when there are none.
- `preflightWarningsCount` (integer/int32): Number of entries in `preflightWarnings`.

### Ejemplo — respuesta 200
```json
{
  "flow": {
    "id": "661c7bc712eaf357de7e4aeb",
    "orgId": "8eb7da9a-c81c-4d13-b08b-38fdeb7330d8",
    "version": 0,
    "flowType": "FLOW",
    "name": "SamplePlayMessageFlow",
    "description": "Minimal sample flow: greet the caller, then disconnect",
    "status": "Draft",
    "createdBy": "user@example.com",
    "createdDate": "2026-01-15T09:12:00.000Z",
    "lastModifiedBy": "user@example.com",
    "lastModifiedDate": "2026-05-20T14:30:00.000Z"
  },
  "preflightWarnings": [],
  "preflightWarningsCount": 0
}
```

## Respuestas de error
- **400**: Bad Request.
  Ejemplo:
```json
{
  "code": "INVALID_FLOW",
  "message": "Flow document failed validation.",
  "details": [
    {
      "path": "/nodes/2/inputs/queue",
      "code": "UNKNOWN_QUEUE",
      "message": "Queue 'Main_Support_Quueue' was not found in the project."
    }
  ]
}
```
- **401**: Unauthorized.
- **403**: Forbidden.
- **404**: Not Found.
- **409**: Conflict — `expectedVersion` does not match the current draft version.
- **422**: Unprocessable Entity — flow document failed validation.
  Ejemplo:
```json
{
  "valid": false,
  "errors": [
    {
      "activityName": "start",
      "condition": "onTimeoutBOGUS",
      "from": "NewContact",
      "suggestion": "Use one of: out",
      "message": "Condition 'onTimeoutBOGUS' is not valid for activity 'start'.",
      "severity": "ERROR",
      "edge": "NewContact->WelcomeMessage(onTimeoutBOGUS)"
    }
  ],
  "warnings": [
    {
      "severity": "RECOMMENDATION",
      "code": "FC1007",
      "message": "Add descriptions for activities"
    }
  ],
  "summary": "1 error(s), 1 warning(s)."
}
```
- **429**: Too Many Requests.

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs