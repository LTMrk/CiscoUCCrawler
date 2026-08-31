---
doc_id: webex-contact-center-delete-v1-monitor-requestid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: DELETE
path: /v1/monitor/{requestId}
operation_id: deleteMonitoringRequestRoute
tags: Call Monitoring
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.140985+00:00
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
- `requestId` [path] (string/UUID) (**requerido**): The id with which the monitoring request has been created.

## Ejemplo de invocación
```bash
curl -X DELETE '/v1/monitor/<requestId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**202**: The delete request was accepted for processing

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