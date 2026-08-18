---
doc_id: webex-messaging-get-messages
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
api_version: 1.0.0
method: GET
path: /messages
operation_id: List Messages
tags: Messages
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.807937+00:00
---

# GET /messages

**API:** Webex Messaging
**Área:** Messages
**operationId:** `List Messages`

## Resumen
List Messages

## Descripción
Lists all messages in a room.  Each message will include content attachments if present.

The list sorts the messages in descending order by creation date.

Long result sets will be split into [pages](/docs/basics#pagination).

## Parámetros
- `roomId` [query] (string) (**requerido**): List messages in a room, by ID.
- `parentId` [query] (string): List messages with a parent, by ID.
- `mentionedPeople` [query] (array): List messages with these people mentioned, by ID. Use `me` as a shorthand for the current API user. Only `me` or the person ID of the current user may be specified. Bots must include this parameter to list messages in group rooms (spaces).
- `before` [query] (string): List messages sent before a date and time.
- `beforeMessage` [query] (string): List messages sent before a message, by ID.
- `max` [query] (number): Limit the maximum number of messages in the response. Cannot exceed 100 if used with `mentionedPeople`. Por defecto: 50.

## Ejemplo de invocación
```bash
curl -X GET '/messages?roomId=<roomId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array):
  - `id` (string): The unique identifier for the message.
  - `parentId` (string): The unique identifier for the parent message.
  - `roomId` (string): The room ID of the message.
  - `roomType` (string): The type of room.  * `direct` - 1:1 room  * `group` - group room Valores: direct, group.
  - `text` (string): The message, in plain text. If `markdown` is specified this parameter may be *optionally* used to provide alternate text for UI clients that do not support rich text.
  - `markdown` (string): The message, in Markdown format.
  - `html` (string): The text content of the message, in HTML format. This read-only property is used by the Webex clients.
  - `files` (array): Public URLs for files attached to the message. For the supported media types and the behavior of file uploads, see [Message Attachments](/docs/basics#message-attachments).
  - `personId` (string): The person ID of the message author.
  - `personEmail` (string): The email address of the message author.
  - `mentionedPeople` (array): People IDs for anyone mentioned in the message.
  - `mentionedGroups` (array): Group names for the groups mentioned in the message.
  - `attachments` (array): Message content attachments attached to the message. See the [Cards Guide](/docs/buttons-and-cards) for more information.
    - `content` (object):
      - `fileId` (string) (**requerido**): The `fileId` of the attachment.
      - `type` (string) (**requerido**): The type of attachment.  * `external` - Attachment stored externally.  * `native` - Attachment stored within the Webex platform. Valores: external, native.
      - `contentUrl` (string) (**requerido**): The URL for the content.
  - `created` (string): The date and time the message was created.
  - `updated` (string): The date and time that the message was last edited by the author. This field is only present when the message contents have changed.
  - `isVoiceClip` (boolean): `true` if the audio file is a voice clip recorded by the client; `false` if the audio file is a standard audio file not posted using the voice clip feature.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTJkYjNiZTAtNDNiZC0xMWU2LThhZTktZGQ1YjNkZmM1NjVk",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
      "roomType": "group",
      "text": "PROJECT UPDATE - A new project plan has been published on http://example.com/s/lf5vj. The PM for this project is Mike C. and the Engineering Manager is Jane W.",
      "markdown": "**PROJECT UPDATE** A new project plan has been published on <http://example.com/s/lf5vj>. The PM for this project is <@personEmail:mike@example.com> and the Engineering Manager is <@personEmail:jane@example.com>.",
      "html": "<p><strong>PROJECT UPDATE</strong> A new project plan has been published <a href=\\\"http://example.com/s/lf5vj\\\" rel=\\\"nofollow\\\">here</a>. The PM for this project is mike@example.com and the Engineering Manager is jane@example.com.</p>",
      "files": [
        "http://www.example.com/images/media.png"
      ],
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
      "personEmail": "matt@example.com",
      "mentionedPeople": [
        "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8yNDlmNzRkOS1kYjhhLTQzY2EtODk2Yi04NzllZDI0MGFjNTM,Y2lzY29zcGFyazovL3VzL1BFT1BMRS83YWYyZjcyYy0xZDk1LTQxZjAtYTcxNi00MjlmZmNmYmM0ZDg"
      ],
      "mentionedGroups": [
        "all"
      ],
      "attac
  ... (truncado)
```
- Cabecera `Link`: 

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