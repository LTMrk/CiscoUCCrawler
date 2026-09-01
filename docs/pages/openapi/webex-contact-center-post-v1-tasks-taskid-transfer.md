---
doc_id: webex-contact-center-post-v1-tasks-taskid-transfer
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/tasks/{taskId}/transfer
operation_id: transferTaskRoute
tags: Tasks
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.709789+00:00
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
- `taskId` [path] (string/UUID) (**requerido**): The unique ID represents the task that the user is currently working on. It will be generated automatically during the creation of a new task.

## Cuerpo de la petición (application/json)
- `to` (string) (**requerido**): The user destination ID or the entry point ID to transfer, maximum length 43 characters.
- `destinationType` (string) (**requerido**): The user can transfer to another user in the team(```agent```), queue(```queue```), dial number(```dialNumber```), entry point(```entrypointDialNumber```).

## Ejemplo de invocación
```bash
curl -X POST '/v1/tasks/<taskId>/transfer' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"to": "<to>", "destinationType": "<destinationType>"}'
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