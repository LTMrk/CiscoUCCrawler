---
doc_id: webex-messaging-get-messages-direct
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
api_version: 1.0.0
method: GET
path: /messages/direct
operation_id: List Direct Messages
tags: Messages
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.808512+00:00
---

# GET /messages/direct

**API:** Webex Messaging
**Área:** Messages
**operationId:** `List Direct Messages`

## Resumen
List Direct Messages

## Descripción
List all messages in a 1:1 (direct) room. Use the `personId` or `personEmail` query parameter to specify the room. Each message will include content attachments if present.

The list sorts the messages in descending order by creation date.

## Parámetros
- `parentId` [query] (string): List messages with a parent, by ID.
- `personId` [query] (string): List messages in a 1:1 room, by person ID.
- `personEmail` [query] (string): List messages in a 1:1 room, by person email.

## Ejemplo de invocación
```bash
curl -X GET '/messages/direct' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array):
  - `id` (string): The unique identifier for the message.
  - `roomId` (string): The room ID of the message.
  - `roomType` (string): The type of room. Will always be `direct`.
  - `text` (string): The message, in plain text. If `markdown` is specified this parameter may be *optionally* used to provide alternate text for UI clients that do not support rich text.
  - `markdown` (string): The message, in Markdown format.
  - `files` (array): Public URLs for files attached to the message. For the supported media types and the behavior of file uploads, see [Message Attachments](/docs/api/basics#message-attachments).
  - `personId` (string): The person ID of the message author.
  - `personEmail` (string): The email address of the message author.
  - `created` (string): The date and time the message was created.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vODQxZjY5MjAtNDdlZC00NmE0LWI2YmItZTVjM2M1YTc3Yzgy",
      "roomType": "direct",
      "text": "Hey there, what do you think of this project update presentation (http://sharepoint.example.com/presentation.pptx)?",
      "markdown": "Hey there, what do you think of [this project update presentation](http://sharepoint.example.com/presentation.pptx)?",
      "html": "<p>Hey there, what do you think of <a href=\\\"http://sharepoint.example.com/presentation.pptx\\\" rel=\\\"nofollow\\\">this project update presentation</a>?</p>",
      "files": [
        "http://www.example.com/images/media.png"
      ],
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
      "personEmail": "matt@example.com",
      "attachments": [
        {
          "contentType": "application/vnd.microsoft.card.adaptive",
          "content": {
            "type": "AdaptiveCard",
            "version": "1.0",
            "body": [
              {
                "type": "TextBlock",
                "text": "Adaptive Cards",
                "size": "large"
              }
            ],
            "actions": [
              {
                "type": "Action.OpenUrl",
                "url": "http://adapt
  ... (truncado)
```

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **423**: Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **428**: Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex Messaging APIs offer robust programmatic access to messaging features within Webex, including sending and receiving messages, managing spaces, memberships, attachments, and moderating content. These APIs enable integration with bots, workflow automation, notification systems, and custom messaging solutions to enhance team collaboration and productivity. Use cases include building chatbots, integrating with ticketing or alerting platforms, automating onboarding flows, and creating custom collaboration experiences tailored to business needs.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs