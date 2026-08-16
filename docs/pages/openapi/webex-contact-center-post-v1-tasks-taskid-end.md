---
doc_id: webex-contact-center-post-v1-tasks-taskid-end
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/tasks/{taskId}/end
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.963895+00:00
---

# POST /v1/tasks/{taskId}/end

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `endTaskRoute`

## Resumen
End Task

## Descripción
Access this endpoint when the user has to end either an inbound or an outbound requests. Requires one of the following scopes 'cjp:user' or 'cloud-contact-center:pod_conv' for authorization. For a list of possible response messages, see the [Call Control API Guide](/docs/contact-control-apis).

## Parámetros
- `taskId` [path] (string) **(requerido)**: The unique ID represents the task that the user is currently working on. It will be generated automatically during the creation of a new task.

## Respuestas
- **202**: The request is accepted for processing
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
