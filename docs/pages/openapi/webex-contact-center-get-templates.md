---
doc_id: webex-contact-center-get-templates
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /templates
operation_id: listFlowTemplates
tags: Templates
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.762856+00:00
---

# GET /templates

**API:** Webex Contact Center
**Área:** Templates
**operationId:** `listFlowTemplates`

## Resumen
List Flow Templates

## Descripción
List available flow templates that can be used to create new flows.

Scope: `cjp:config_read`

## Parámetros
- `type` [query] (string): Filter by flow or subflow. Valores: flow, subflow.

## Ejemplo de invocación
```bash
curl -X GET '/templates' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Array of template metadata with IDs, names, and descriptions.
- (array de:)
  - `id` (string): Template ID.
  - `name` (string): Template name.
  - `description` (string): Human-readable description of the template.
  - `type` (string): Template kind. One of `flow` or `subflow`. Valores: flow, subflow.
  - `flow` (object): Flow JSON document (formerly Flow IR / FDL 2.0). Describes a flow as top-level metadata plus arrays of nodes, edges, variables, event flows, and preferences.
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

### Ejemplo — respuesta 200
```json
[
  {
    "id": "tmpl-customer-callback",
    "name": "Customer Callback",
    "description": "Offers a callback when estimated wait time exceeds a threshold.",
    "type": "flow"
  }
]
```

## Respuestas de error
- **401**: Unauthorized.
- **403**: Forbidden.
- **404**: Not Found.
- **429**: Too Many Requests.

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs