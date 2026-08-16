---
doc_id: webex-contact-center-delete-v1-monitor-requestid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: DELETE
path: /v1/monitor/{requestId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.962932+00:00
---

# DELETE /v1/monitor/{requestId}

**API:** Webex Contact Center
**Área:** Call Monitoring
**operationId:** `deleteMonitoringRequestRoute`

## Resumen
Delete Monitoring Request

## Descripción
Delete a particular monitoring request that was created. Requires scope 'cloud-contact-center:pod_conv' and 'cjp.supervisor'.

## Parámetros
- `requestId` [path] (string) **(requerido)**: The id with which the monitoring request has been created.

## Respuestas
- **202**: The delete request was accepted for processing
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **412**: Precondition Failed
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
