---
doc_id: webex-contact-center-post-v1-agents-reload
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/agents/reload
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.961739+00:00
---

# POST /v1/agents/reload

**API:** Webex Contact Center
**Área:** Agents
**operationId:** `reloadRoute`

## Resumen
Reload

## Descripción
Allows the user to receive all the contact assigned to particular agent and state. Requires 'cjp:user' scope for authorization.

## Respuestas
- **202**: The reload request was accepted for processing
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
