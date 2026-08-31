---
doc_id: webex-contact-center-post-v1-agents-buddylist
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/agents/buddyList
operation_id: buddyAgentsRoute
tags: Agents
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.746958+00:00
---

# POST /v1/agents/buddyList

**API:** Webex Contact Center
**Área:** Agents
**operationId:** `buddyAgentsRoute`

## Resumen
Buddy Agents List

## Descripción
Returns the list of agents in the given state and media according to agent profile settings. Requires 'cjp:user' scope for authorization.

## Cuerpo de la petición (application/json)
- `agentProfileId` (string) (**requerido**): The profile ID of a particular agent. Can be obtained from [Users API](/docs/users), maximum length 36 characters.
- `mediaType` (string) (**requerido**): The media type for the request. The supported values are ```telephony```, ```chat```, ```social```, ```email```, ```workItem``` and ```customMessaging```.
- `state` (string): It represents the current state of the returned agents which can be either ```Available``` or ```Idle```. If state is omitted from the payload, the API will return a list of both available and idle agents. This is useful for consult scenarios, since consulting an idle agent is also supported.

## Ejemplo de invocación
```bash
curl -X POST '/v1/agents/buddyList' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"agentProfileId": "<agentProfileId>", "mediaType": "<mediaType>"}'
```

## Respuestas correctas
**202**: The buddy agents request was accepted for processing

## Respuestas de error
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs