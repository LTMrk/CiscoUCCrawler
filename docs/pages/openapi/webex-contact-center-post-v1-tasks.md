---
doc_id: webex-contact-center-post-v1-tasks
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /v1/tasks
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.963514+00:00
---

# POST /v1/tasks

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `CreateTaskRoute`

## Resumen
Create Task

## Descripción
This API is to create a task for work or handling assignments. Represents both inbound tasks (originating from customer-facing channels) and outbound tasks (originating from contact center to customer-facing channel). Requires 'cjp:user' scope for authorization. For a list of possible response messages, see the Call Control API Guide.

## Cuerpo de la petición (application/json)
- `destination` (string) **(requerido)**: A valid customer DN, on which the response is expected, maximum length 36 characters.
- `entryPointId` (string) **(requerido)**: An entryPointId for respective task. For ```CALLBACK``` and ```OUTDIAL``` this should be an outboundEP. For ```EXECUTE_FLOW``` this should be an inboundEP which is mapped to a flow that will be triggered, maximum length 36 characters.
- `attributes` (object): This is a schema free data tuple to pass-on specific data, depending on the outboundType. Supports a maximum of 30 tuples. Each tuple can have a key up to 200 bytes (up to 200 UTF-8 characters) and a value up to 1024 bytes (up to 1024 UTF-8 characters).
- `outboundType` (string): The outbound type for the task. Supported values are ```CALLBACK```, ```OUTDIAL```, and ```EXECUTE_FLOW```. Use ```OUTDIAL``` when the user is logged into the Agent Desktop and needs to make an outbound call to the customer. Use ```CALLBACK``` when the user is not logged in and needs to schedule a callback to the customer. Use ```EXECUTE_FLOW``` when the task is linked to a predefined flow triggered through an Inbound Entrypoint.
- `mediaType` (string) **(requerido)**: The media type for the request. The ```telephony``` type is required for ```EXECUTE_FLOW``` and ```CALLBACK```. The supported value is ```telephony```.
- `origin` (string): The contact center number, which is an ANI Outdial number, that will be used while making a call to the customer. This field is mandatory for ```EXECUTE_FLOW``` and ```OUTDIAL``` type while it is optional for ```CALLBACK```. If not provided for ```CALLBACK``` type, default out-dial ANI configuration will be used, maximum length 36 characters. The origin value must exactly match one of the configured Outdial ANIs in the agent profile.
- `callback` (object): Details for a callback task.
  - `callbackOrigin` (string) **(requerido)**: The source of callback request. The supported value is ```web```.
  - `callbackType` (string) **(requerido)**: The type of callback. The supported value is ```immediate```.
- `customAttributes` (object): This is a schema-free data tuple to pass on specific SIP header data, Supports a maximum of 20 headers, selected alphabetically if more than 20 are present. Each header key is converted to lowercase, and hyphens are retained. The payload is restricted to 1100 bytes to comply with RFC3261 when using UDP. No header values are logged to ensure PII protection.Ex:The Caller ID Name is included as 'caller_id_name', derived from the appropriate SIP header

## Respuestas
- **201**: The new task was successfully requested for creation
  - `meta` (object) **(requerido)**: Response metadata.
    - `orgId` (string) **(requerido)**: UUID of the organization, inferred from the authorization token.
  - `data` (object) **(requerido)**: Response data.
    - `id` (string) **(requerido)**: UUID of the created task. Use this ID to monitor and manage the task lifecycle via subsequent API calls.
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **500**: Internal Server Error
- **503**: Service Unavailable

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
