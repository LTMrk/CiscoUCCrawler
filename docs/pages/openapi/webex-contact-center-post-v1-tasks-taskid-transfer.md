---
doc_id: webex-contact-center-post-v1-tasks-taskid-transfer
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/tasks/{taskId}/transfer
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.964452+00:00
---

# POST /v1/tasks/{taskId}/transfer

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `transferTaskRoute`

## Resumen
Transfer Task

## Descripción
Access this endpoint when the user has to transfer a call to another user. Requires one of the following scopes 'cjp:user' or 'cloud-contact-center:pod_conv' scope for authorization. For a list of possible response messages, see the [Call Control API Guide](/docs/contact-control-apis).

## Parámetros
- `taskId` [path] (string) **(requerido)**: The unique ID represents the task that the user is currently working on. It will be generated automatically during the creation of a new task.

## Cuerpo de la petición (application/json)
- `to` (string) **(requerido)**: The user destination ID or the entry point ID to transfer, maximum length 43 characters.
- `destinationType` (string) **(requerido)**: The user can transfer to another user in the team(```agent```), queue(```queue```), dial number(```dialNumber```), entry point(```entrypointDialNumber```).

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
