---
doc_id: webex-contact-center-patch-v1-tasks-taskid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PATCH
path: /v1/tasks/{taskId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.963745+00:00
---

# PATCH /v1/tasks/{taskId}

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `PatchTaskRoute`

## Resumen
Update Task

## Descripción
This API is to update a task. Represents both inbound tasks (originating from customer-facing channels) and outbound tasks (originating from contact center to customer-facing channel). Requires one of the following scopes 'cjp:user' or 'cloud-contact-center:pod_conv' for authorization.. For a list of possible response messages, see the Call Control API Guide.

## Parámetros
- `taskId` [path] (string) **(requerido)**: The unique ID represents the task that the user is currently working on. It will be generated automatically during the creation of a new task.

## Cuerpo de la petición (application/json)
- `attributes` (object) **(requerido)**: This is a schema free data tuple to pass-on specific data, depending on the outboundType. Supports a maximum of 30 tuples. Each tuple can have a key up to 200 bytes (up to 200 UTF-8 characters) and a value up to 1024 bytes (up to 1024 UTF-8 characters).

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
