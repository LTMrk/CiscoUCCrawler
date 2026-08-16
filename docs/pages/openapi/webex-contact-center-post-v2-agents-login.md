---
doc_id: webex-contact-center-post-v2-agents-login
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v2/agents/login
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.962143+00:00
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
- `Authorization` [header] (string) **(requerido)**: The bearer token would be sent to validate the active users.

## Cuerpo de la petición (application/json)
- `dialNumber` (string) **(requerido)**: A dialNumber field contains the number to dial such as a route point or extension, maximum length 43 characters.
- `teamId` (string): The unique ID representing a team of users. Leaving this field blank is valid for supervisor role but invalid for agent role, maximum length 36 characters.
- `isExtension` (boolean): It indicates if the dialNumber field is full number or extension. It is set to false by default.
- `roles` (array) **(requerido)**: It represents the current role of the user. The user can either be an ```agent``` or a ```supervisor```.
- `deviceType` (string): It represents the way to differentiate type of login request (```AGENT_DN```, ```EXTENSION```, ```BROWSER```). Leaving this field is valid for supervisor role but invalid for agent role.
- `deviceId` (string): It is equal to dialNumber for AGENT_DN & EXTENSION deviceType and for BROWSER it is populated as webrtc-AgentUUID, maximum length 43 characters.

## Respuestas
- **202**: The login request was accepted for processing
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
