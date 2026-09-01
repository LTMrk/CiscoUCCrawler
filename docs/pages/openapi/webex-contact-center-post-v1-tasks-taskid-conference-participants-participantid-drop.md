---
doc_id: webex-contact-center-post-v1-tasks-taskid-conference-participants-participantid-drop
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/tasks/{taskId}/conference/participants/{participantId}/drop
operation_id: dropConferenceParticipantsRoute
tags: Tasks
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.710607+00:00
---

# POST /v1/tasks/{taskId}/conference/participants/{participantId}/drop

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `dropConferenceParticipantsRoute`

## Resumen
Drop Participant From Conference

## Descripción
Access this endpoint when the user needs to drop a specific participant from an active conference associated with a task. This operation removes only the targeted participant while keeping the remaining parties in the conference. Requires `cjp:user` scope for  authorization. For a list of possible response messages, see the [Call Control API Guide](/docs/contact-control-apis)

## Parámetros
- `taskId` [path] (string/UUID) (**requerido**): The taskId represents the task that the user is currently working on. It will be generated automatically during the creation of a new task.
- `participantId` [path] (string) (**requerido**): The ID of the participant ( Agent / DN / Entry Point DN / Customer) to be dropped from the conference, maximum length 36 characters.

## Ejemplo de invocación
```bash
curl -X POST '/v1/tasks/<taskId>/conference/participants/<participantId>/drop' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**202**: The request is accepted for processing

## Respuestas de error
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **429**: Too many requests
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs