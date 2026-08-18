---
doc_id: webex-contact-center-post-v2-tasks
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v2/tasks
operation_id: createTaskRouteV2
tags: Tasks
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.854055+00:00
---

# POST /v2/tasks

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `createTaskRouteV2`

## Resumen
Create Task

## Descripción
This feature is currently in Beta. Contact your Cisco team if you want access to this feature.

Creates a new contact center task using the v2 task contract. The request body must include a `channelType` discriminator to select the task variant — `workItem` for structured form tasks, `customMessaging` for conversational messaging tasks, or `telephony` for voice tasks.

On success, returns a `201` response containing the task ID, which can be used to track the task lifecycle.

Requires `cjp:task_write` OAuth scope. For partner-initiated inbound tasks (`workItem`, `customMessaging`), the `cjp:task_write` scope must be present in the partner application's access token. When an authenticated agent initiates an outdial (`telephony`) task, ensure the `cjp:task_write` scope is included in the agent's access token.

## Parámetros
- `Authorization` [header] (string) (**requerido**): Bearer token used to authorize the request.

## Cuerpo de la petición (application/json)
- (uno de:)
  - `origin` (object) (**requerido**): Origin of the task. For inbound `workItem` tasks, this represents the customer.
    - `id` (string) (**requerido**): Customer's identifier, such as an email address.
    - `name` (string): Optional human-readable display name for the customer.
  - `destination` (object) (**requerido**): Destination for the workItem task. The `type` must be `businessAddress`.
    - `id` (string) (**requerido**): Business address associated with the configured workItem channel entry point.
    - `type` (string) (**requerido**): Must be `businessAddress` for `workItem` tasks. Valores: businessAddress, dialNumber.
  - `channelType` (string) (**requerido**): Discriminator field. Must be `workItem` for custom channel task creation. Valores: workItem.
  - `channel` (string) (**requerido**): Identifier of the configured workItem channel in the organization. Required for `workItem` requests.
  - `flowSettings` (object): Schema-free data map to pass specific data to the externalized flow settings. Supports a maximum of 15 tuples. Each tuple can have a key up to 200 bytes and a value up to 512 bytes.
  - `globalVariables` (object): Schema-free data map to pass specific data depending on the outbound type. Values are validated against the global variables configured in the organization. Supports a maximum of 30 tuples. Each tuple can have a key up to 200 bytes and a value up to 1024 bytes. **Migrating from v1:** Previously named `attributes`.
  - `channelParams` (object) (**requerido**): Work item channel parameters.
    - `type` (string) (**requerido**): Must be `work-item-form` for work item channel parameters. Valores: work-item-form.
    - `message` (object) (**requerido**): Work item message payload.
      - `aliasId` (string) (**requerido**): Identifier of the work item message.
      - `workItemData` (object) (**requerido**): Structured key-value payload for the work item form. Maximum 50 entries; keys up to 100 UTF-8 bytes, values up to 1024 UTF-8 bytes.
      - `timestamp` (integer/int64) (**requerido**): Unix epoch timestamp in milliseconds representing when the work item was originated.
  - `origin` (object) (**requerido**): Origin of the task. For inbound `customMessaging` tasks, this represents the customer.
    - `id` (string) (**requerido**): Customer's identifier, such as an email address or user ID.
    - `name` (string): Optional human-readable display name for the customer.
  - `destination` (object) (**requerido**): Destination for the customMessaging task. The `type` must be `businessAddress`.
    - `id` (string) (**requerido**): Business address associated with the configured custom messaging channel entry point.
    - `type` (string) (**requerido**): Must be `businessAddress` for `customMessaging` tasks. Valores: businessAddress.
  - `channelType` (string) (**requerido**): Channel type for this request. Valores: customMessaging.
  - `channel` (string) (**requerido**): Identifier of the configured custom messaging channel in the organization. Required for `customMessaging` requests.
  - `flowSettings` (object): Schema-free data map to pass specific data to the externalized flow settings. Supports a maximum of 15 tuples. Each tuple can have a key up to 200 bytes and a value up to 512 bytes.
  - `globalVariables` (object): Schema-free data map to pass specific data depending on the outbound type. Values are validated against the global variables configured in the organization. Supports a maximum of 30 tuples. Each tuple can have a key up to 200 bytes and a value up to 1024 bytes. **Migrating from v1:** Previously named `attributes`.
  - `channelParams` (object) (**requerido**): Custom messaging channel parameters. The `type` field is a discriminator that determines the shape of `message`. Use `text` for a plain text message, or `text-with-attachments` for a message with one or more file attachments.
    - `type` (string) (**requerido**): Discriminator for the custom messaging type. Must be `text` when the message contains only text, or `text-with-attachments` when the message includes file attachments. The value must match the shape of the `message` field — sending `attachments` with `type: "text"` or omitting `attachments` with `type: "text-with-attachments"` returns a `400`. Valores: text, text-with-attachments.
    - `message` (object) (**requerido**): The message payload. Must match the shape indicated by `type`: a `TextMessage` when `type` is `text`, or a `TextWithAttachment` when `type` is `text-with-attachments`.
  - `origin` (object) (**requerido**): Origin of the outbound telephony task. May be the agent's information or a configured outbound ANI in the organization.
    - `id` (string) (**requerido**): Outbound ANI or agent identifier used for the telephony call.
    - `name` (string): Optional display name. May be omitted or null for telephony tasks.
  - `destination` (object) (**requerido**): Destination for the telephony task. The `type` must be `dialNumber`.
    - `id` (string) (**requerido**): The dial number to call. **Migrating from v1:** Previously the top-level `destination` field (plain string).
    - `type` (string) (**requerido**): Must be `dialNumber` for `telephony` tasks. Valores: businessAddress, dialNumber.
  - `channelType` (string) (**requerido**): Discriminator field. Must be `telephony` for voice task creation. **Migrating from v1:** Previously named `mediaType`. Valores: telephony.
  - `channel` (string): Not applicable for telephony tasks. May be omitted or set to `null`.
  - `flowSettings` (object): Schema-free data map to pass specific data to the externalized flow settings. Supports a maximum of 15 tuples. Each tuple can have a key up to 200 bytes and a value up to 512 bytes.
  - `globalVariables` (object): Schema-free data map to pass specific data depending on the outbound type. Values are validated against the global variables configured in the organization. Supports a maximum of 30 tuples. Each tuple can have a key up to 200 bytes and a value up to 1024 bytes. **Migrating from v1:** Previously named `attributes`.
  - `channelParams` (object) (**requerido**): Telephony channel parameters.
    - `type` (string) (**requerido**): Must be `telephony` for telephony channel parameters. Valores: telephony.
    - `entryPointId` (string) (**requerido**): UUID of the entry point for the task. For `CALLBACK` and `OUTDIAL`, this must be an outbound entry point. For `EXECUTE_FLOW`, this must be an inbound entry point mapped to the flow to be triggered. **Migrating from v1:** Previously a top-level field, now nested under `channelParams`.
    - `outboundType` (string) (**requerido**): The outbound type for the task. Use `OUTDIAL` when the agent needs to make an outbound call to the customer. Use `CALLBACK` when scheduling a callback — `callback` field is required. Use `EXECUTE_FLOW` to trigger a predefined flow through an inbound entry point. Use `RECORD_GREETING` to record a personalized agent greeting. Valores: CALLBACK, OUTDIAL, EXECUTE_FLOW, RECORD_GREETING.
    - `callback` (object): Required when `outboundType` is `CALLBACK`. Must be omitted or `null` for `OUTDIAL`, `EXECUTE_FLOW`, and `RECORD_GREETING`. When provided, `type` must be `immediate` and `origin` must be `web`. **Migrating from v1:** Previously a top-level `callback` object with fields `callbackType` and `callbackOrigin`; now nested under `channelParams`.
      - (todos de:)
        - `type` (string) (**requerido**): Callback execution mode. Currently only `immediate` is supported. **Migrating from v1:** Previously named `callbackType`. Valores: immediate.
        - `origin` (string) (**requerido**): Channel that originated the callback request. The supported value is `web`. **Migrating from v1:** Previously named `callbackOrigin`. Valores: web.
        - `number` (string): Optional callback number. Provided when the callback flow supplies a specific number to dial back.
    - `sipHeaders` (object): Optional map of SIP headers forwarded to the telephony infrastructure for the call. Supports up to 20 headers (selected alphabetically if more than 20 are provided). Each key is converted to lowercase with hyphens retained. The payload is restricted to 1100 bytes to comply with RFC 3261 (UDP). Header values are not logged to ensure PII protection. **Migrating from v1:** Previously named `customAttributes`.

### Create a workItem task — petición
```json
{
  "origin": {
    "id": "customer@domain.com",
    "name": "Customer Name"
  },
  "destination": {
    "id": "customer-support@biz.com",
    "type": "businessAddress"
  },
  "channelType": "workItem",
  "channel": "support-form",
  "channelParams": {
    "type": "work-item-form",
    "message": {
      "aliasId": "msg-001",
      "workItemData": {
        "name": "customer name",
        "email": "customer@domain.com"
      },
      "timestamp": 1732786800000
    }
  }
}
```

### Create a telephony (callback) task — petición
```json
{
  "origin": {
    "id": "+18000000000",
    "name": null
  },
  "destination": {
    "id": "+19780000000",
    "type": "dialNumber"
  },
  "channelType": "telephony",
  "channelParams": {
    "type": "telephony",
    "entryPointId": "aef6455f-ccd6-4261-bb00-e80f845c01b0",
    "outboundType": "CALLBACK",
    "callback": {
      "type": "immediate",
      "origin": "web",
      "number": "+19780000000"
    }
  }
}
```

### Create a customMessaging task (text only) — petición
```json
{
  "origin": {
    "id": "customer@example.com",
    "name": "Customer Name"
  },
  "destination": {
    "id": "support@channel.biz",
    "type": "businessAddress"
  },
  "channelType": "customMessaging",
  "channel": "my-custom-channel",
  "channelParams": {
    "type": "text",
    "message": {
      "aliasId": "123e4567-e89b-12d3-a456-426614174000",
      "text": "Hello, I need help with my order.",
      "timestamp": 1732786800000
    }
  }
}
```

### Create a customMessaging task (text with attachments) — petición
```json
{
  "origin": {
    "id": "customer@example.com",
    "name": "Customer Name"
  },
  "destination": {
    "id": "support@channel.biz",
    "type": "businessAddress"
  },
  "channelType": "customMessaging",
  "channel": "my-custom-channel",
  "channelParams": {
    "type": "text-with-attachments",
    "message": {
      "aliasId": "123e4567-e89b-12d3-a456-426614174001",
      "text": "Please see the attached screenshot.",
      "attachments": [
        {
          "fileName": "screenshot.png",
          "mimeType": "image/png",
          "fileUrl": "https://cdn.example.com/files/screenshot.png"
        }
      ],
      "timestamp": 1732786800000
    }
  }
}
```

## Ejemplo de invocación
```bash
curl -X POST '/v2/tasks' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**201**: The new task was successfully requested for creation
- `meta` (object) (**requerido**): Response metadata.
  - `orgId` (string/uuid) (**requerido**): UUID of the organization, inferred from the authorization token.
- `data` (object) (**requerido**): Response data.
  - `id` (string/uuid) (**requerido**): UUID of the created task. Use this ID to monitor and manage the task lifecycle via subsequent API calls.

### Ejemplo — respuesta 201
```json
{
  "meta": {
    "orgId": "658d1102-8c11-4850-a809-d7a99cc1c22f"
  },
  "data": {
    "id": "768d1102-8c11-4850-a809-d7a99cc1c22e"
  }
}
```

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