---
doc_id: webex-contact-center-post-orgid-project-projectid-v2-flows-flowid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /{orgId}/project/{projectId}/v2/flows/{flowId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.967330+00:00
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
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `projectId` [path] (string) **(requerido)**: Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `flowId` [path] (string) **(requerido)**: Flow ID.
- `expectedVersion` [query] (integer): Expected current draft version for optimistic locking. The request fails with 409 Conflict if the server-side version does not match. Omit to skip the check.
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW'.

## Cuerpo de la petición (application/json)
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
    - `key` (string): Stable, unique edge key within the flow. Used as the patch-merge key for `upsert_edges` and `remove_edge_keys`.
    - `from_node` (string): Name of the source node. Must reference a node in the same process.
    - `from_port` (string): Output port name on the source node. Must match an `outputPorts[].name` exposed by the source activity definition.
    - `to_node` (string): Name of the target node. Must reference a node in the same process.
    - `condition` (string): Branch condition this edge fires on. Aliases: `done` -> `out`, `NewPhoneContact` -> `out`, `defaultBranch` -> `default`.
- `preferences` (array): Flow-level preferences.
  - `name` (string): Preference name.
  - `type` (string): Preference value type.
  - `value` (string): Preference value, encoded as a string.

## Respuestas
- **200**: Updated flow metadata, including the new `version`.
  - `flow` (object): The persisted flow document, including the server-assigned `id`.
  - `preflightWarnings` (array): Non-blocking warnings raised while persisting the flow (for example, references that resolve but are flagged for review). Empty when there are none.
  - `preflightWarningsCount` (integer): Number of entries in `preflightWarnings`.
- **400**: Bad Request.
- **401**: Unauthorized.
- **403**: Forbidden.
- **404**: Not Found.
- **409**: Conflict — `expectedVersion` does not match the current draft version.
- **422**: Unprocessable Entity — flow document failed validation.
- **429**: Too Many Requests.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
