---
doc_id: webex-contact-center-get-v1-monitor-sessions
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /v1/monitor/sessions
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.962861+00:00
---

# GET /v1/monitor/sessions

**API:** Webex Contact Center
**Área:** Call Monitoring
**operationId:** `fetchMonitoringSessionsRoute`

## Resumen
Fetch Monitoring Sessions

## Descripción
Fetches all active subscriptions for a given clientID.

## Respuestas
- **202**: The fetch session request was accepted for processing.
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **412**: Precondition Failed
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
