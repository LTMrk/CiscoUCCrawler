---
doc_id: webex-messaging-post-attachment-actions
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
method: POST
path: /attachment/actions
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.509544+00:00
---

# POST /attachment/actions

**API:** Webex Messaging
**Área:** Attachment Actions
**operationId:** `Create an Attachment Action`

## Resumen
Create an Attachment Action

## Descripción
Create a new attachment action.

## Cuerpo de la petición (application/json)
- `type` (string) **(requerido)**: The type of action to perform. Valores: submit.
- `messageId` (string) **(requerido)**: The ID of the message which contains the attachment.
- `inputs` (object) **(requerido)**: The attachment action's inputs.
  - `Name` (string):
  - `Url` (string):
  - `Email` (string):
  - `Tel` (string):

### Ejemplo de petición
```json
{
  "type": "submit",
  "messageId": "GFyazovL3VzL1BFT1BMRS80MDNlZmUwNy02Yzc3LTQyY2UtOWI4NC",
  "inputs": {
    "Name": "John Andersen",
    "Url": "https://example.com",
    "Email": "john.andersen@example.com",
    "Tel": "+1 408 555 7209"
  }
}
```

## Respuestas
- **202**: Accepted
  - `id` (string): A unique identifier for the action.
  - `personId` (string): The ID of the person who performed the action.
  - `roomId` (string): The ID of the room in which the action was performed.
  - `type` (string) **(requerido)**: The type of action performed. Valores: submit.
  - `messageId` (string) **(requerido)**: The parent message on which the attachment action was performed.
  - `inputs` (object): The action's inputs.
    - `Name` (string):
    - `Url` (string):
    - `Email` (string):
    - `Tel` (string):
  - `created` (string): The date and time the action was created.
- **400**: Bad Request
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found
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
