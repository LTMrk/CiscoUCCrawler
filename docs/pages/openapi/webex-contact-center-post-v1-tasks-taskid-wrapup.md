---
doc_id: webex-contact-center-post-v1-tasks-taskid-wrapup
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/tasks/{taskId}/wrapup
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.963975+00:00
---

# POST /v1/tasks/{taskId}/wrapup

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `agentWrapUpRoute`

## Resumen
Wrap Up Task

## Descripción
Access this endpoint when the user has to wrap up a call. Requires one of the following scopes 'cjp:user' or 'cloud-contact-center:pod_conv' for authorization. For a list of possible response messages, see the [Call Control API Guide](/docs/contact-control-apis).

## Parámetros
- `taskId` [path] (string) **(requerido)**: The unique ID represents the task that the user is currently working on. It will be generated automatically during the creation of a new task.

## Cuerpo de la petición (application/json)
- `auxCodeId` (string) **(requerido)**: Auxiliary codes are status codes which an agent can select in Webex Contact Center Agent Desktop. They are of two types: ```Idle``` and ```Wrap-Up``` codes, and every agent profile must have one of each for the agent to use. Idle codes are used to explain an agent's unavailability to take customer contacts, such as during a lunch break or a meeting. Wrap-up codes indicate the result of customer contacts, such as successful resolution or escalation of the contact. Creating and managing auxiliary codes requires an administrator role and the appropriate cjp:config_write or cjp:config_read scopes, maximum length 36 characters.
- `wrapUpReason` (string) **(requerido)**: Every wrap up reason will have an unique auxillary code. Use this field to specify the reason for wrapping up the call, maximum length 128 characters.

## Respuestas
- **202**: The request is accepted for processing
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
