---
doc_id: webex-contact-center-post-v1-tasks-taskid-unhold
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/tasks/{taskId}/unhold
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.964137+00:00
---

# POST /v1/tasks/{taskId}/unhold

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `agentUnHoldRoute`

## Resumen
Resume Task

## Descripción
Access this endpoint when the user has to resume a call from hold. When an user is done consulting, the previously held interaction with the customer should be resumed. It is not applicable for chats and emails. Requires one of the following scopes 'cjp:user','cloud-contact-center:pod_conv' for authorization. For a list of possible response messages, see the [Call Control API Guide](/docs/contact-control-apis).

## Parámetros
- `taskId` [path] (string) **(requerido)**: The unique ID represents the task that the user is currently working on. It will be generated automatically during the creation of a new task.

## Cuerpo de la petición (application/json)
- `mediaResourceId` (string) **(requerido)**: It is an identifier of a media resource, maximum length 36 characters

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
