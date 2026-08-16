---
doc_id: webex-contact-center-post-v1-agentburnout-action
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/agentburnout/action
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.921552+00:00
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
- `X-ORGANIZATION-ID` [header] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `interactionId` (string): A unique identifier for each interaction or contact within the contact center.
- `agentId` (string): The identifier for the agent whose burnout index has been calculated.
- `clientId` (string): The name of the client initiating the action related to the agent burnout index. The name is limited to a maximum of 20 characters.
- `actionType` (string): Specifies the type of action initiated based on the agent burnout index
- `actionDateType` (object): The Epoch timestamp indicating the precise time at which the action was executed.

## Respuestas
- **200**: Successful operation
  - `data` (object): The data object contains the details of the action taken.
    - `id` (string): A unique identifier for the action taken.
    - `interactionId` (string): A unique identifier for each interaction or contact within the contact center.
    - `orgId` (string): The organization ID to which the agent belongs.
    - `agentId` (string): The identifier for the agent whose burnout index has been calculated.
    - `clientId` (string): The name of the client initiating the action related to the agent burnout index. The name is limited to a maximum of 20 characters.
    - `actionType` (string): Specifies the type of action initiated based on the agent burnout index
    - `actionDateTime` (integer): The Epoch timestamp indicating the precise time at which the action was executed.
    - `createdDateTime` (integer): The Epoch timestamp indicating the time when the action was created.
  - `trackingId` (string): The unique tracking ID for this request.
- **400**: Validation Error
- **401**: Unauthorized Operation
- **403**: Forbidden Operation
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited.
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
