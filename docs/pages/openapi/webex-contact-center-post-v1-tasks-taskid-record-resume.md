---
doc_id: webex-contact-center-post-v1-tasks-taskid-record-resume
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/tasks/{taskId}/record/resume
operation_id: resumeRecordingRoute
tags: Tasks
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.709679+00:00
---

# POST /v1/tasks/{taskId}/record/resume

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `resumeRecordingRoute`

## Resumen
Resume Recording Task

## Descripción
When configured by the administrator, telephony tasks are often being recorded for various reasons. When an user is handling sensitive customer information, he/she might resume the recording after the pause. For a list of possible response messages, see the [Call Control API Guide](/docs/contact-control-apis). Requires OAuth scope cjp:user. The authenticated user must have a UserProfile of type Agent to access this API.

## Parámetros
- `taskId` [path] (string/UUID) (**requerido**): The unique ID represents the task that the user is currently working on. It will be generated automatically during the creation of a new task.

## Cuerpo de la petición (application/json)
- `autoResumed` (boolean) (**requerido**): The setting to mention if the recording has to resume automatically.

## Ejemplo de invocación
```bash
curl -X POST '/v1/tasks/<taskId>/record/resume' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"autoResumed": true}'
```

## Respuestas correctas
**202**: The request is accepted for processing

## Respuestas de error
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs