---
doc_id: webex-contact-center-get-orgid-project-projectid-v2-flows-flowid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /{orgId}/project/{projectId}/v2/flows/{flowId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.967183+00:00
---

# GET /{orgId}/project/{projectId}/v2/flows/{flowId}

**API:** Webex Contact Center
**Área:** Flows
**operationId:** `getFlowV2`

## Resumen
Get a Flow

## Descripción
Retrieve the current draft of a flow as a flow document. To fetch a specific published version, use the `:export` endpoint.

Scope: `cjp:config_read`

## Parámetros
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `projectId` [path] (string) **(requerido)**: Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `flowId` [path] (string) **(requerido)**: Flow ID.
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW'.

## Respuestas
- **200**: Flow JSON document.
  - `flowName` (string): Name of the flow.
  - `flowType` (string): Flow type. One of `FLOW` or `SUBFLOW`. Valores: FLOW, SUBFLOW.
  - `contactType` (string): Channel type the flow is intended for (for example, `telephony`, `customMessaging`, `workItem`, `genericAction`).
  - `description` (string): Human-readable description of the flow.
  - `version` (integer): Monotonically increasing version number of the document.
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
- **401**: Unauthorized.
- **403**: Forbidden.
- **404**: Not Found.
- **429**: Too Many Requests.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
