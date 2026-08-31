---
doc_id: webex-contact-center-post-v1-tasks-taskid-accept
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/tasks/{taskId}/accept
operation_id: acceptTaskRoute
tags: Tasks
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.750910+00:00
---

# POST /v1/tasks/{taskId}/accept

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `acceptTaskRoute`

## Resumen
Accept Task

## Descripción
Access this endpoint when the user has to accept either an inbound or an outbound requests. The request can be social, a chat or an email. Requires one of the following scopes 'cjp:user' or 'cloud-contact-center:pod_conv' for authorization. For a list of possible response messages, see the [Call Control API Guide](/docs/contact-control-apis).

## Parámetros
- `taskId` [path] (string/UUID) (**requerido**): The unique ID represents the task that the user is currently working on. It will be generated automatically during the creation of a new task.

## Ejemplo de invocación
```bash
curl -X POST '/v1/tasks/<taskId>/accept' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**202**: The request is accepted for processing

## Respuestas de error
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs