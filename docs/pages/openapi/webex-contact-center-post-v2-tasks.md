---
doc_id: webex-contact-center-post-v2-tasks
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v2/tasks
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.965339+00:00
---

# POST /v2/tasks

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `createTaskRouteV2`

## Resumen
Create Task

## Descripción
This feature is currently in Beta. Contact your Cisco team if you want access to this feature.

Creates a new contact center task using the v2 task contract. The request body must include a `channelType` discriminator to select the task variant — `workItem` for structured form tasks, `customMessaging` for conversational messaging tasks, or `telephony` for voice tasks.

On success, returns a `201` response containing the task ID, which can be used to track the task lifecycle.

Requires `cjp:task_write` OAuth scope. For partner-initiated inbound tasks (`workItem`, `customMessaging`), the `cjp:task_write` scope must be present in the partner application's access token. When an authenticated agent initiates an outdial (`telephony`) task, ensure the `cjp:task_write` scope is included in the agent's access token.

## Parámetros
- `Authorization` [header] (string) **(requerido)**: Bearer token used to authorize the request.

## Respuestas
- **201**: The new task was successfully requested for creation
  - `meta` (object) **(requerido)**: Response metadata.
    - `orgId` (string) **(requerido)**: UUID of the organization, inferred from the authorization token.
  - `data` (object) **(requerido)**: Response data.
    - `id` (string) **(requerido)**: UUID of the created task. Use this ID to monitor and manage the task lifecycle via subsequent API calls.
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
