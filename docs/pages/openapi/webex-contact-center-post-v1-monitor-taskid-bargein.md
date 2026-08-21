---
doc_id: webex-contact-center-post-v1-monitor-taskid-bargein
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/monitor/{taskId}/bargeIn
operation_id: bargeInRoute
tags: Call Monitoring
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.798634+00:00
---

# POST /v1/monitor/{taskId}/bargeIn

**API:** Webex Contact Center
**Área:** Call Monitoring
**operationId:** `bargeInRoute`

## Resumen
BargeIn Request

## Descripción
Create a successful barge-in request for the supervisor to barge in the call that is being monitored already. Requires scope 'cloud-contact-center:pod_conv' and 'cjp.supervisor'.

## Parámetros
- `taskId` [path] (string/UUID) (**requerido**): The unique ID representing the task that needs to be barged by the supervisor.

## Ejemplo de invocación
```bash
curl -X POST '/v1/monitor/<taskId>/bargeIn' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**202**: The bargeIn request was accepted for processing

## Respuestas de error
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **412**: Precondition Failed
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs