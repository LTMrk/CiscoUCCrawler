---
doc_id: webex-contact-center-post-v1-tasks-taskid-assign
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/tasks/{taskId}/assign
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.964873+00:00
---

# POST /v1/tasks/{taskId}/assign

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `assignRoute`

## Resumen
Assign Task

## Descripción
Access this endpoint when users such as administrators, supervisors, or agents with an agent license need to assign tasks to themselves. Authorization requires the `cjp:user` scope. For a list of potential response messages, refer to the [Call Control API Guide](/docs/contact-control-apis).

## Parámetros
- `taskId` [path] (string) **(requerido)**: The unique ID represents the task that the user want to assign.

## Respuestas
- **202**: The request is accepted for processing
- **401**: Unauthorized
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
