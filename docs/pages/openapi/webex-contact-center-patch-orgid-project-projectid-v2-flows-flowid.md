---
doc_id: webex-contact-center-patch-orgid-project-projectid-v2-flows-flowid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PATCH
path: /{orgId}/project/{projectId}/v2/flows/{flowId}
operation_id: patchFlowV2Draft
tags: Flows
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.858473+00:00
---

# PATCH /{orgId}/project/{projectId}/v2/flows/{flowId}

**API:** Webex Contact Center
**Área:** Flows
**operationId:** `patchFlowV2Draft`

## Resumen
Patch a Flow Draft

## Descripción
Apply partial updates to an existing flow draft without replacing the entire document. The patch body is a Patch Draft Contract — server-side merge, idempotent, and re-validated after the merge. The patch is rejected if the merged document fails validation, so the draft is never left in a broken state. The body may also include top-level overrides such as `name` and `description`.

Pass `expectedVersion` as a query parameter to enable optimistic locking; the request fails with `409 Conflict` if the server-side version does not match. Omit `expectedVersion` to skip the check.

Scope: `cjp:config_write`

## Parámetros
- `orgId` [path] (string) (**requerido**): Organization ID.
- `projectId` [path] (string) (**requerido**): Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `flowId` [path] (string) (**requerido**): Flow ID.
- `expectedVersion` [query] (integer/int32): Expected current draft version for optimistic locking. The request fails with 409 Conflict if the server-side version does not match. Omit to skip the check.
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW'. Por defecto: FLOW.

## Cuerpo de la petición (application/json)
- `upsert_nodes` (array): Nodes to insert or replace. Matched by `name`. If a node with the same name exists, it is fully replaced; otherwise a new node is created.
- `upsert_edges` (array): Edges to insert or replace, matched by `id`.
- `remove_node_names` (array): Names of nodes to remove. Edges referencing a removed node must also be removed in the same patch, or the merged document will fail validation.
- `remove_edge_keys` (array): Identifiers of edges to remove.

### Ejemplo — petición
```json
{
  "upsert_nodes": [
    {
      "id": "node-welcome",
      "name": "WelcomeMessage",
      "activityType": "action",
      "properties": {
        "activityName": "play-message",
        "prompt": {
          "promptType": "text",
          "text": "Thanks for calling. Please hold.",
          "textType": "text"
        }
      }
    }
  ],
  "upsert_edges": [
    {
      "id": "edge-1",
      "from": "NewContact",
      "to": "WelcomeMessage",
      "condition": "out",
      "properties": {}
    }
  ],
  "remove_node_names": [],
  "remove_edge_keys": []
}
```

## Ejemplo de invocación
```bash
curl -X PATCH '/<orgId>/project/<projectId>/v2/flows/<flowId>' \
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
- **422**: Unprocessable Entity — merged flow document failed validation.
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