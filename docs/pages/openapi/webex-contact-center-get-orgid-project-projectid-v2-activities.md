---
doc_id: webex-contact-center-get-orgid-project-projectid-v2-activities
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /{orgId}/project/{projectId}/v2/activities
operation_id: listActivityDefinitions
tags: Activities
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.854587+00:00
---

# GET /{orgId}/project/{projectId}/v2/activities

**API:** Webex Contact Center
**Área:** Activities
**operationId:** `listActivityDefinitions`

## Resumen
List Activity Definitions

## Descripción
List all available activity types with their full schemas, including inputs, outputs, ports, and descriptions. The response is sufficient on its own to construct nodes — there is no separate schema endpoint.

Scope: `cjp:config_read`

## Parámetros
- `orgId` [path] (string) (**requerido**): Organization ID.
- `projectId` [path] (string) (**requerido**): Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.

## Ejemplo de invocación
```bash
curl -X GET '/<orgId>/project/<projectId>/v2/activities' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Array of activity definitions.
- (array de:)
  - `activityName` (string): Stable activity type identifier referenced by a flow node's `properties.activityName`. Read the value verbatim from this endpoint; it is not always kebab-case (for example, `SetCallerID`, `Feedback-V2`, `queue-lookup`).
  - `displayName` (string): Human-readable name shown in authoring UIs.
  - `category` (string): High-level grouping the activity belongs to (for example, `core`).
  - `group` (string): Group the activity belongs to. An open set; observed values include `action`, `enum-gateway`, `http-request`, `parse-activity`, `set-variable`, and `terminating-action`. Read the value verbatim rather than assuming a fixed set.
  - `activityType` (string): Underlying activity classification used by the runtime (for example, `action`, `start`).
  - `inputs` (array): Declared inputs for the activity.
    - `name` (string): Input field name.
    - `type` (string): Input data type (for example, `string`, `boolean`, `int`, `object[]`).
    - `required` (boolean): True if the input must be supplied.
    - `defaultValue` (object): Default value applied when the input is not supplied. May be null. Type matches `type`.
    - `showOnCondition` (string): Expression controlling when this input is shown in authoring UIs, evaluated against sibling input values. Null when the input is always shown.
    - `isSecure` (boolean): True if the input holds sensitive data that should be masked.
    - `allowedValues` (array): Enumerated allowed values for a static-choice input. Null when the input is unconstrained or resolves its choices dynamically via `choicesEndpoint`.
    - `choicesEndpoint` (string): Relative endpoint used to resolve choices dynamically for this input. Null when the input has no dynamic choices.
    - `children` (array): Nested inputs for composite/object inputs. Empty when the input has no children.
      - (referencia circular a ActivityInput)
    - `description` (string): Human-readable description of the input.
  - `outputs` (array): Declared outputs for the activity.
    - `name` (string): Output field name.
    - `type` (string): Output data type.
    - `description` (string): Human-readable description of the output.
  - `outputPorts` (array): Output ports the activity may exit through. An edge's `condition` must match one of these ports' `condition` values.
    - `condition` (string): Port condition. An edge's `condition` must match one of these verbatim (for example, `default`, `error`).
    - `label` (string): Human-readable port label shown in authoring UIs. May be empty.
    - `isErrorPath` (boolean): True if this port is the activity's error path.

### Ejemplo — respuesta 200
```json
[
  {
    "activityName": "play-message",
    "displayName": "Play Message",
    "category": "core",
    "group": "action",
    "activityType": "action"
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