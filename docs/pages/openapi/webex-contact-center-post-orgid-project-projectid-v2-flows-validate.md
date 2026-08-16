---
doc_id: webex-contact-center-post-orgid-project-projectid-v2-flows-validate
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /{orgId}/project/{projectId}/v2/flows:validate
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.966847+00:00
---

# POST /{orgId}/project/{projectId}/v2/flows:validate

**API:** Webex Contact Center
**Área:** Flows
**operationId:** `validateFlowV2`

## Resumen
Validate a Flow

## Descripción
Dry-run validate a flow definition without persisting it. Use this to check correctness before importing.

Note: validation is more lenient than import. A flow that passes `:validate` can still be rejected by `:import` (for example, a missing start activity), so a successful validation does not guarantee a successful import.

Scope: `cjp:config_write`

## Parámetros
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `projectId` [path] (string) **(requerido)**: Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.

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
- **200**: Validation result.
  - `valid` (boolean): True if the document passed validation.
  - `errors` (array): Blocking errors. Empty when `valid` is true.
    - `activityName` (string): Name of the activity the error relates to.
    - `condition` (string): Edge condition the error relates to, when applicable.
    - `from` (string): Source node label of the offending edge, when applicable.
    - `edge` (string): Human-readable description of the offending edge, when applicable.
    - `suggestion` (string): Suggested fix.
    - `message` (string): Human-readable explanation of the error.
    - `severity` (string): Severity of the issue. Valores: ERROR.
  - `warnings` (array): Non-blocking warnings and recommendations.
    - `severity` (string): Severity of the issue. Valores: WARNING, RECOMMENDATION.
    - `code` (string): Stable warning code.
    - `message` (string): Human-readable explanation of the warning.
  - `summary` (string): Human-readable summary of the validation outcome.
- **400**: Bad Request — Invalid flow schema or missing required fields.
- **401**: Unauthorized.
- **403**: Forbidden.
- **404**: Not Found.
- **429**: Too Many Requests.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
