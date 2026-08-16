---
doc_id: webex-contact-center-post-v1-agents-buddylist
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/agents/buddyList
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.961820+00:00
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
- `agentProfileId` (string) **(requerido)**: The profile ID of a particular agent. Can be obtained from [Users API](/docs/users), maximum length 36 characters.
- `mediaType` (string) **(requerido)**: The media type for the request. The supported values are ```telephony```, ```chat```, ```social```, ```email```, ```workItem``` and ```customMessaging```.
- `state` (string): It represents the current state of the returned agents which can be either ```Available``` or ```Idle```. If state is omitted from the payload, the API will return a list of both available and idle agents. This is useful for consult scenarios, since consulting an idle agent is also supported.

## Respuestas
- **202**: The buddy agents request was accepted for processing
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
