---
doc_id: webex-contact-center-post-v1-tasks-taskid-resume
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/tasks/{taskId}/resume
operation_id: resumeTaskRoute
tags: Tasks
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-15T14:56:57.693655+00:00
---

# POST /v1/tasks/{taskId}/resume

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `resumeTaskRoute`

## Resumen
Resume Task

## Descripción
Access this endpoint when users such as administrators, supervisors, or agents with an agent license need to resume a previously paused task. This API is supported only for non-real-time digital channels, such as email, social, etc. Authorization requires the `cjp:user` scope. For a list of potential response messages, refer to the [Call Control API Guide](/docs/contact-control-apis).

## Parámetros
- `taskId` [path] (string/UUID) (**requerido**): The unique ID represents the interaction or task that the user wants to resume.

## Ejemplo de invocación
```bash
curl -X POST '/v1/tasks/<taskId>/resume' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**202**: The request is accepted for processing

## Respuestas de error
- **401**: Unauthorized
- **403**: Forbidden Request
- **404**: Not Found
- **429**: Too many requests
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs