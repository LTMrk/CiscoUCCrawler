---
doc_id: webex-contact-center-post-v1-monitor-taskid-bargein
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/monitor/{taskId}/bargeIn
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.962547+00:00
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
- `taskId` [path] (string) **(requerido)**: The unique ID representing the task that needs to be barged by the supervisor.

## Respuestas
- **202**: The bargeIn request was accepted for processing
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **412**: Precondition Failed
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
