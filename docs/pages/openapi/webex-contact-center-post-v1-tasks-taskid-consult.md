---
doc_id: webex-contact-center-post-v1-tasks-taskid-consult
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/tasks/{taskId}/consult
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.964533+00:00
---

# POST /v1/tasks/{taskId}/consult

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `consultRoute`

## Resumen
Consult Task

## Descripción
Access this endpoint when the user has to consult a call to another user. Requires one of the following scopes 'cjp:user' or 'cloud-contact-center:pod_conv' for authorization. For a list of possible response messages, see the [Call Control API Guide](/docs/contact-control-apis).

## Parámetros
- `taskId` [path] (string) **(requerido)**: The unique ID represents the task that the user is currently working on. It will be generated automatically during the creation of a new task.

## Cuerpo de la petición (application/json)
- `to` (string) **(requerido)**: The destination ID to consult, maximum length 36 characters.
- `destinationType` (string) **(requerido)**: The user can consult to another user in the team(```agent```), queue(```queue```), entry point(```entryPoint```) or dial number(```dialNumber```).  When consulting an Entry Point (EP) that is associated with multiple Directory Numbers (DNs), the consult typically goes to one of the associated DNs.
- `holdParticipants` (boolean): This allows the caller to specify their preference for whether the main call should be placed on hold or not during consult.

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
