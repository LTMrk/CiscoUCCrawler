---
doc_id: webex-contact-center-post-v2-tasks-taskid-messages
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v2/tasks/{taskId}/messages
operation_id: appendTaskMessageV2
tags: Tasks
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.145888+00:00
---

# POST /v2/tasks/{taskId}/messages

**API:** Webex Contact Center
**Área:** Tasks
**operationId:** `appendTaskMessageV2`

## Resumen
Append Task Message

## Descripción
This feature is currently in Beta. Contact your Cisco team if you want access to this feature.

Appends an inbound message to an existing `workItem` or `customMessaging` task. Use this API after the initial task has been created through Create Task. Requires `cjp:task_write` OAuth scope. For partner-initiated inbound message appends, the `cjp:task_write` scope must be present in the partner application's access token.

On success, returns a `202` response containing the append event identifier as `data.id`. Partners can use this identifier to correlate subsequent webhook delivery for the appended message.

## Parámetros
- `Authorization` [header] (string) (**requerido**): Bearer token used to authorize the request.
- `taskId` [path] (string/uuid) (**requerido**): UUID of the existing task to which the message will be appended.

## Cuerpo de la petición (application/json)
- (uno de:)
  - `mediaType` (string) (**requerido**): Media type for this request. Must be `workItem`. Valores: workItem.
  - `channelParams` (object) (**requerido**): Work item channel parameters.
    - `type` (string) (**requerido**): Must be `work-item-form` for work item channel parameters. Valores: work-item-form.
    - `message` (object) (**requerido**): Work item message payload.
      - `aliasId` (string) (**requerido**): Identifier of the work item message.
      - `workItemData` (object) (**requerido**): Structured key-value payload for the work item form. Maximum 50 entries; keys up to 100 UTF-8 bytes, values up to 1024 UTF-8 bytes.
      - `timestamp` (integer/int64) (**requerido**): Unix epoch timestamp in milliseconds representing when the work item was originated.
  - `mediaType` (string) (**requerido**): Media type for this request. Must be `customMessaging`. Valores: customMessaging.
  - `channelParams` (object) (**requerido**): Custom messaging channel parameters. The `type` field is a discriminator that determines the shape of `message`. Use `text` for a plain text message, or `text-with-attachments` for a message with one or more file attachments.
    - `type` (string) (**requerido**): Discriminator for the custom messaging type. Must be `text` when the message contains only text, or `text-with-attachments` when the message includes file attachments. The value must match the shape of the `message` field — sending `attachments` with `type: "text"` or omitting `attachments` with `type: "text-with-attachments"` returns a `400`. Valores: text, text-with-attachments.
    - `message` (object) (**requerido**): The message payload. Must match the shape indicated by `type`: a `TextMessage` when `type` is `text`, or a `TextWithAttachment` when `type` is `text-with-attachments`.

### Append a workItem message — petición
```json
{
  "mediaType": "workItem",
  "channelParams": {
    "type": "work-item-form",
    "message": {
      "aliasId": "alias-wi-001",
      "workItemData": {
        "name": "customer name",
        "email": "customer@domain.com"
      },
      "timestamp": 1732786800000
    }
  }
}
```

### Append a customMessaging text message — petición
```json
{
  "mediaType": "customMessaging",
  "channelParams": {
    "type": "text",
    "message": {
      "aliasId": "123e4567-e89b-12d3-a456-426614174000",
      "text": "I have additional details to share.",
      "timestamp": 1732786800000
    }
  }
}
```

### Append a customMessaging message with attachments — petición
```json
{
  "mediaType": "customMessaging",
  "channelParams": {
    "type": "text-with-attachments",
    "message": {
      "aliasId": "123e4567-e89b-12d3-a456-426614174001",
      "text": "Please review the attached files.",
      "attachments": [
        {
          "fileName": "details.pdf",
          "mimeType": "application/pdf",
          "fileUrl": "https://cdn.example.com/files/details.pdf"
        }
      ],
      "timestamp": 1732786800000
    }
  }
}
```

## Ejemplo de invocación
```bash
curl -X POST '/v2/tasks/<taskId>/messages' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**202**: Accepted. The response returns the append event identifier in `data.id`.
- `meta` (object) (**requerido**): Response metadata.
  - `orgId` (string/uuid) (**requerido**): UUID of the organization, inferred from the authorization token.
- `data` (object) (**requerido**): Response data.
  - `id` (string/uuid) (**requerido**): Append event identifier for the message. If `aliasId` is a valid UUID, the platform reuses it as the event identifier; otherwise a UUID is generated. Use this ID to correlate downstream webhook delivery for the appended message.

### Ejemplo — respuesta 202
```json
{
  "meta": {
    "orgId": "658d1102-8c11-4850-a809-d7a99cc1c22f"
  },
  "data": {
    "id": "123e4567-e89b-12d3-a456-426614174000"
  }
}
```

## Respuestas de error
- **400**: Bad Request
- **401**: Unauthorized, Token is Invalid
- **403**: Forbidden Request
- **429**: Too Many Requests
- **500**: Internal Server Error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs