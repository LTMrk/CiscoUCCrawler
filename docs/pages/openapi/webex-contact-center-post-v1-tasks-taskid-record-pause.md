---
doc_id: webex-contact-center-post-v1-tasks-taskid-record-pause
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/tasks/{taskId}/record/pause
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.964292+00:00
---

# POST /v1/tasks/{taskId}/record/pause

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `pauseRecordingRoute`

## Resumen
Pause Recording Task

## Descripción
When configured by the administrator, telephony tasks are often being recorded for various reasons. When an user is handling sensitive customer information, he/she might want to pause the recording and later on resume recording. For a list of possible response messages, see the [Call Control API Guide](/docs/contact-control-apis). Requires OAuth scope cjp:user. The authenticated user must have a UserProfile of type Agent to access this API.

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
