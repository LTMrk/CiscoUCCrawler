---
doc_id: webex-contact-center-get-orgid-project-projectid-v2-activities-activityname-inputs-inputname-choices
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /{orgId}/project/{projectId}/v2/activities/{activityName}/inputs/{inputName}/choices
operation_id: getActivityInputChoices
tags: Activities
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.855031+00:00
---

# GET /{orgId}/project/{projectId}/v2/activities/{activityName}/inputs/{inputName}/choices

**API:** Webex Contact Center
**Área:** Activities
**operationId:** `getActivityInputChoices`

## Resumen
Get Activity Input Choices

## Descripción
Resolve choices for an activity input. Use this when an activity input requires a value from a predefined or dynamically resolved set (e.g., available queues, audio files, agents).

This endpoint is only valid for inputs that expose choices (an input whose definition includes `allowedValues` or a `choicesEndpoint`, as returned by `describeActivity`). Calling it for an input that does not support choices returns 400.

Pass `search` to filter the choices (type-ahead). Add `validate=true` together with `search` to do a point-lookup of a single value instead of filtering — the match is against the choice's `value` (its ID), not its display `name`. For a cascading input whose allowed values depend on a sibling input, supply the parent with `parentInputName` and `parentValue`; otherwise a cascading input returns 400.

Filtering and validation apply only to dynamic (`choicesEndpoint`-backed) inputs. A static input always returns its full enumerated list regardless of `search`/`validate`.

Scope: `cjp:config_read`

## Parámetros
- `orgId` [path] (string) (**requerido**): Organization ID.
- `projectId` [path] (string) (**requerido**): Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `activityName` [path] (string) (**requerido**): Activity type name.
- `inputName` [path] (string) (**requerido**): Input field name. Must be an input that exposes choices (has `allowedValues` or a `choicesEndpoint`).
- `search` [query] (string): Search text used to filter the returned choices (type-ahead). When `validate=true`, this is instead the single value to look up.
- `validate` [query] (boolean): When `true` and `search` is supplied, performs a point-lookup of the single value in `search` (matched against the choice's `value`/ID) instead of filtering. Por defecto: False.
- `parentValue` [query] (string): Parent input value for a cascading/dynamic input (for example, the selected `channelType`).
- `parentInputName` [query] (string): Parent input name for a cascading/dynamic input. Required when `parentValue` is provided.

## Ejemplo de invocación
```bash
curl -X GET '/<orgId>/project/<projectId>/v2/activities/<activityName>/inputs/<inputName>/choices' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Resolved choices for the input, plus resolution metadata.
- `count` (integer): Number of choices returned.
- `source` (string): How the choices were resolved. Valores: list, search, validate, dynamic, static.
- `choices` (array): The resolved choices.
  - `name` (string): Human-readable label shown in authoring UIs.
  - `value` (string): The choice value/ID, suitable for use as the activity input value.
- `parentInputName` (string): Parent input name echoed back for cascading resolution (empty when not cascading).
- `parentValue` (string): Parent input value echoed back for cascading resolution (empty when not cascading).
- `isSearchEnabled` (boolean): True when the input supports server-side search/filtering.
- `resolvedInput` (string): The input name the choices were resolved for.
- `activity` (string): The activity name the input belongs to.
- `input` (string): The requested input name.

### Ejemplo — respuesta 200
```json
{
  "count": 2,
  "source": "static",
  "choices": [
    {
      "name": "Voice",
      "value": "TELEPHONY"
    },
    {
      "name": "Work item",
      "value": "WORK_ITEM"
    }
  ],
  "parentInputName": "",
  "parentValue": "",
  "isSearchEnabled": false,
  "resolvedInput": "channelType",
  "activity": "queue-lookup",
  "input": "channelType"
}
```

## Respuestas de error
- **400**: Bad Request — a cascading input was queried without its parent (`parentInputName`/`parentValue`), or the input does not support choices.
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
- **429**: Too Many Requests.

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs