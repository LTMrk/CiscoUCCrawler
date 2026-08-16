---
doc_id: webex-contact-center-post-v2-tasks-taskid-messages
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v2/tasks/{taskId}/messages
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.965434+00:00
---

# POST /v2/tasks/{taskId}/messages

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `appendTaskMessageV2`

## Resumen
Append Task Message

## Descripción
This feature is currently in Beta. Contact your Cisco team if you want access to this feature.

Appends an inbound message to an existing `workItem` or `customMessaging` task. Use this API after the initial task has been created through Create Task. Requires `cjp:task_write` OAuth scope. For partner-initiated inbound message appends, the `cjp:task_write` scope must be present in the partner application's access token.

On success, returns a `202` response containing the append event identifier as `data.id`. Partners can use this identifier to correlate subsequent webhook delivery for the appended message.

## Parámetros
- `Authorization` [header] (string) **(requerido)**: Bearer token used to authorize the request.
- `taskId` [path] (string) **(requerido)**: UUID of the existing task to which the message will be appended.

## Respuestas
- **202**: Accepted. The response returns the append event identifier in `data.id`.
  - `meta` (object) **(requerido)**: Response metadata.
    - `orgId` (string) **(requerido)**: UUID of the organization, inferred from the authorization token.
  - `data` (object) **(requerido)**: Response data.
    - `id` (string) **(requerido)**: Append event identifier for the message. If `aliasId` is a valid UUID, the platform reuses it as the event identifier; otherwise a UUID is generated. Use this ID to correlate downstream webhook delivery for the appended message.
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **429**: Too Many Requests
- **500**: Internal Server Error

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
