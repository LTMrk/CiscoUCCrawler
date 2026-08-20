---
doc_id: webex-contact-center-patch-v1-tasks-taskid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PATCH
path: /v1/tasks/{taskId}
operation_id: PatchTaskRoute
tags: Tasks
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.733583+00:00
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
- `taskId` [path] (string/UUID) (**requerido**): The unique ID represents the task that the user is currently working on. It will be generated automatically during the creation of a new task.

## Cuerpo de la petición (application/json)
- `attributes` (object) (**requerido**): This is a schema free data tuple to pass-on specific data, depending on the outboundType. Supports a maximum of 30 tuples. Each tuple can have a key up to 200 bytes (up to 200 UTF-8 characters) and a value up to 1024 bytes (up to 1024 UTF-8 characters).

## Ejemplo de invocación
```bash
curl -X PATCH '/v1/tasks/<taskId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"attributes": {}}'
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