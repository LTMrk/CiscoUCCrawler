---
doc_id: webex-contact-center-post-v1-agentburnout-action
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/agentburnout/action
operation_id: post_action
tags: Agent Wellbeing
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.751472+00:00
---

# POST /v1/agentburnout/action

**API:** Webex Contact Center
**Área:** Agent Wellbeing
**operationId:** `post_action`

## Resumen
Record the realtime burnout events

## Descripción
The endpoint need to be invoked by Partners and Third-Party that will subscribe to the Agent Burnout system, in order to take certain action based on the agent burnout index calculated.

## Parámetros
- `X-ORGANIZATION-ID` [header] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `interactionId` (string): A unique identifier for each interaction or contact within the contact center.
- `agentId` (string): The identifier for the agent whose burnout index has been calculated.
- `clientId` (string): The name of the client initiating the action related to the agent burnout index. The name is limited to a maximum of 20 characters.
- `actionType` (string): Specifies the type of action initiated based on the agent burnout index
- `actionDateType` (object): The Epoch timestamp indicating the precise time at which the action was executed.

## Ejemplo de invocación
```bash
curl -X POST '/v1/agentburnout/action' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: Successful operation
- `data` (object): The data object contains the details of the action taken.
  - `id` (string): A unique identifier for the action taken.
  - `interactionId` (string): A unique identifier for each interaction or contact within the contact center.
  - `orgId` (string): The organization ID to which the agent belongs.
  - `agentId` (string): The identifier for the agent whose burnout index has been calculated.
  - `clientId` (string): The name of the client initiating the action related to the agent burnout index. The name is limited to a maximum of 20 characters.
  - `actionType` (string): Specifies the type of action initiated based on the agent burnout index
  - `actionDateTime` (integer/int64): The Epoch timestamp indicating the precise time at which the action was executed.
  - `createdDateTime` (integer/int64): The Epoch timestamp indicating the time when the action was created.
- `trackingId` (string): The unique tracking ID for this request.

## Respuestas de error
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden Operation
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited.
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs