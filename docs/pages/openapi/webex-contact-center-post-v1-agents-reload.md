---
doc_id: webex-contact-center-post-v1-agents-reload
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/agents/reload
operation_id: reloadRoute
tags: Agents
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.797270+00:00
---

# POST /v1/agents/reload

**API:** Webex Contact Center
**Área:** Agents
**operationId:** `reloadRoute`

## Resumen
Reload

## Descripción
Allows the user to receive all the contact assigned to particular agent and state. Requires 'cjp:user' scope for authorization.

## Ejemplo de invocación
```bash
curl -X POST '/v1/agents/reload' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**202**: The reload request was accepted for processing

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