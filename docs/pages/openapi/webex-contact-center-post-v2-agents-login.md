---
doc_id: webex-contact-center-post-v2-agents-login
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v2/agents/login
operation_id: LoginRoute
tags: Agents
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.747592+00:00
---

# POST /v2/agents/login

**API:** Webex Contact Center
**Área:** Agents
**operationId:** `LoginRoute`

## Resumen
Login

## Descripción
Allows the user to login to their desktop. It does not allow a duplicate login and sends an error message over websocket, if an active session already exists. Requires 'cjp:user' scope for authorization. For a list of possible response messages, see the [Call Control API Guide](/documentation/guides/contact-control-apis).

## Parámetros
- `Authorization` [header] (string) (**requerido**): The bearer token would be sent to validate the active users.

## Cuerpo de la petición (application/json)
- `dialNumber` (string) (**requerido**): A dialNumber field contains the number to dial such as a route point or extension, maximum length 43 characters.
- `teamId` (string): The unique ID representing a team of users. Leaving this field blank is valid for supervisor role but invalid for agent role, maximum length 36 characters.
- `isExtension` (boolean): It indicates if the dialNumber field is full number or extension. It is set to false by default.
- `roles` (array) (**requerido**): It represents the current role of the user. The user can either be an ```agent``` or a ```supervisor```.
- `deviceType` (string): It represents the way to differentiate type of login request (```AGENT_DN```, ```EXTENSION```, ```BROWSER```). Leaving this field is valid for supervisor role but invalid for agent role.
- `deviceId` (string): It is equal to dialNumber for AGENT_DN & EXTENSION deviceType and for BROWSER it is populated as webrtc-AgentUUID, maximum length 43 characters.

## Ejemplo de invocación
```bash
curl -X POST '/v2/agents/login' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"dialNumber": "<dialNumber>", "roles": []}'
```

## Respuestas correctas
**202**: The login request was accepted for processing

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