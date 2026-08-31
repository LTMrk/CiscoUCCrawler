---
doc_id: webex-contact-center-get-v1-monitor-sessions
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/monitor/sessions
operation_id: fetchMonitoringSessionsRoute
tags: Call Monitoring
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.140858+00:00
---

# GET /v1/monitor/sessions

**API:** Webex Contact Center
**Área:** Call Monitoring
**operationId:** `fetchMonitoringSessionsRoute`

## Resumen
Fetch Monitoring Sessions

## Descripción
Fetches all active subscriptions for a given clientID.

## Ejemplo de invocación
```bash
curl -X GET '/v1/monitor/sessions' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**202**: The fetch session request was accepted for processing.

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