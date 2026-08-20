---
doc_id: webex-contact-center-put-v1-agents-session-state
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PUT
path: /v1/agents/session/state
operation_id: stateRoute
tags: Agents
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.730664+00:00
---

# PUT /v1/agents/session/state

**API:** Webex Contact Center
**Área:** Agents
**operationId:** `stateRoute`

## Resumen
State Change

## Descripción
Allows the user to toggle between the Idle and Available states. An Administrator within the organization having an Agent license can perform a self state change when they have an active agent session. Supervisors can perform a self state change as well as state changes for agents and admin users within their authorized teams when 'Change Agent States' module is enabled. Requires 'cjp:user' scope for authorization.For a list of possible response messages, see the [Call Control API Guide](/docs/contact-control-apis).

## Cuerpo de la petición (application/json)
- `state` (string) (**requerido**): It represents the current state of the user. Can be set to ```Available``` or ```Idle```.
- `auxCodeId` (string) (**requerido**): Auxiliary Codes are status codes which an agent can select in Webex Contact Center Agent Desktop. They are of two types: ```Idle``` and ```Wrap-Up``` codes, and every agent profile must have one of each for the agent to use. Idle codes are used to explain an agent's unavailability to take customer contacts, such as during a lunch break or a meeting. Wrap-up codes indicate the result of customer contacts, such as successful resolution or escalation of the contact. Creating and managing auxiliary codes requires an administrator role and the appropriate cjp:config_write or cjp:config_read scopes, maximum length 36 characters.
- `lastStateChangeReason` (string): It represents the reason of the last state change request, maximum length 128 characters.
- `agentId` (string): User for which state change is initiated, maximum length 36 characters.

## Ejemplo de invocación
```bash
curl -X PUT '/v1/agents/session/state' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"state": "<state>", "auxCodeId": "<auxCodeId>"}'
```

## Respuestas correctas
**202**: The state change request was accepted for processing

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