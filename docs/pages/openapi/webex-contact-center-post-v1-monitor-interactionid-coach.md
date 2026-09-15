---
doc_id: webex-contact-center-post-v1-monitor-interactionid-coach
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/monitor/{interactionId}/coach
operation_id: coachRoute
tags: Call Monitoring
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-15T08:04:07.496164+00:00
---

# POST /v1/monitor/{interactionId}/coach

**API:** Webex Contact Center
**Área:** Call Monitoring
**operationId:** `coachRoute`

## Resumen
Whisper Coach Request

## Descripción
This feature is currently in Beta. Contact your Cisco team if you want access to this feature.

Create a Whisper Coach request for the supervisor to coach the agent on a call that is being monitored already. Requires scope 'cloud-contact-center:pod_conv' and 'cjp.supervisor'.

## Parámetros
- `interactionId` [path] (string/UUID) (**requerido**): The unique ID representing the monitored interaction that the supervisor needs to coach.

## Ejemplo de invocación
```bash
curl -X POST '/v1/monitor/<interactionId>/coach' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**202**: The Whisper Coach request was accepted for processing

## Respuestas de error
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request - feature unavailable, non-supervisor, or insufficient Whisper Coach permissions
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs