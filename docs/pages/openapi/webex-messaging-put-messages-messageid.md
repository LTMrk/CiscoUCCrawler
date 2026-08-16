---
doc_id: webex-messaging-put-messages-messageid
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
method: PUT
path: /messages/{messageId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.512994+00:00
---

# PUT /messages/{messageId}

**API:** Webex Messaging
**Área:** Messages
**operationId:** `Edit a Message`

## Resumen
Edit a Message

## Descripción
Update a message you have posted not more than 10 times.

Specify the `messageId` of the message you want to edit.

Edits of messages containing files or attachments are not currently supported.
If a user attempts to edit a message containing files or attachments a `400 Bad Request` will be returned by the API with a message stating that the feature is currently unsupported.

There is also a maximum number of times a user can edit a message. The maximum currently supported is 10 edits per message.
    If a user attempts to edit a message greater that the maximum times allowed the API will return 400 Bad Request with a message stating the edit limit has been reached.

While only the `roomId` and `text` or `markdown` attributes are *required* in the request body, a common pattern for editing message is to first call `GET /messages/{id}` for the message you wish to edit and to then update the `text` or `markdown` attribute accordingly, passing the updated message object in the request body of the `PUT /messages/{id}` request.
When this pattern is used on a message that included markdown, the `html` attribute must be deleted prior to making the `PUT` request.

## Parámetros
- `messageId` [path] (string) **(requerido)**: The unique identifier for the message.

## Cuerpo de la petición (application/json)
- `roomId` (string) **(requerido)**: The room ID of the message.
- `text` (string): The message, in plain text. If `markdown` is specified this parameter may be *optionally* used to provide alternate text for UI clients that do not support rich text. The maximum message length is 7439 bytes.
- `markdown` (string): The message, in Markdown format. If this attribute is set ensure that the request does NOT contain an `html` attribute.

## Respuestas
- **200**: OK
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
      - `fileId` (string) **(requerido)**: The `fileId` of the attachment.
      - `type` (string) **(requerido)**: The type of attachment.  * `external` - Attachment stored externally.  * `native` - Attachment stored within the Webex platform. Valores: external, native.
      - `contentUrl` (string) **(requerido)**: The URL for the content.
  - `created` (string): The date and time the message was created.
  - `updated` (string): The date and time that the message was last edited by the author. This field is only present when the message contents have changed.
  - `isVoiceClip` (boolean): `true` if the audio file is a voice clip recorded by the client; `false` if the audio file is a standard audio file not posted using the voice clip feature.
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
