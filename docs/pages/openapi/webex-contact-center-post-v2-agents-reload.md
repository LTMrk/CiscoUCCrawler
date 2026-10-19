---
doc_id: webex-contact-center-post-v2-agents-reload
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v2/agents/reload
operation_id: ReloadRoute
tags: Agents
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-10-19T09:48:26.422219+00:00
---

# POST /v2/agents/reload

**API:** Webex Contact Center
**Área:** Agents
**operationId:** `ReloadRoute`

## Resumen
Reload

## Descripción
Requests restoration of the active agent session, including agent state and assigned interaction context. This asynchronous API returns `202 Accepted` when the request is accepted for processing; the restoration result is delivered over WebSocket. The success notification is selected by the API version persisted when the agent logged in, not by the reload endpoint version. A V1 login session receives `AgentReloginSuccess`, and a V2 login session receives `AgentChannelReloginSuccess`; therefore, either reload endpoint can result in either success notification. The active session remains on its login version until the agent logs out and starts a new session. See [AgentReloginSuccess](/docs/contact-control-apis#agentreloginsuccess) and [AgentChannelReloginSuccess](/docs/contact-control-apis#agentchannelreloginsuccess) in the Contact Control API Guide. Requires the 'cjp:user' scope for authorization.

## Parámetros
- `Authorization` [header] (string) (**requerido**): The bearer token would be sent to validate the active users.

## Ejemplo de invocación
```bash
curl -X POST '/v2/agents/reload' \
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