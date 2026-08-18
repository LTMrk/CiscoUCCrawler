---
doc_id: webex-messaging-put-room-tabs-id
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
api_version: 1.0.0
method: PUT
path: /room/tabs/{id}
operation_id: Update a Room Tab
tags: Room Tabs
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.811723+00:00
---

# PUT /room/tabs/{id}

**API:** Webex Messaging
**Área:** Room Tabs
**operationId:** `Update a Room Tab`

## Resumen
Update a Room Tab

## Descripción
Updates the content URL of the specified Room Tab ID.

## Parámetros
- `id` [path] (string) (**requerido**): The unique identifier for the Room Tab.

## Cuerpo de la petición (application/json)
- `roomId` (string) (**requerido**): ID of the room that contains the room tab in question.
- `contentUrl` (string) (**requerido**): Content URL of the Room Tab. URL must use `https` protocol.
- `displayName` (string) (**requerido**): User-friendly name for the room tab.

### Ejemplo — petición
```json
{
  "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
  "contentUrl": "https://www.cisco.com",
  "displayName": "Cisco HomePage"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/room/tabs/<id>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"roomId": "<roomId>", "contentUrl": "<contentUrl>", "displayName": "<displayName>"}'
```

## Respuestas correctas
**200**: OK
- `id` (string): A unique identifier for the Room Tab.
- `roomId` (string): A unique identifier for the room containing the room tab.
- `roomType` (string): The room type.  * `direct` - 1:1 room  * `group` - group room Valores: direct, group.
- `displayName` (string) (**requerido**): User-friendly name for the room tab.
- `contentUrl` (string): Room Tab's content URL.
- `creatorId` (string): The person ID of the person who created this Room Tab.
- `created` (string): The date and time when the Room Tab was created.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL01FTUJFUlNISVAvMGQwYzkxYjYtY2U2MC00NzI1LWI2ZDAtMzQ1NWQ1ZDExZWYzOmNkZTFkZDQwLTJmMGQtMTFlNS1iYTljLTdiNjU1NmQyMjA3Yg",
  "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
  "roomType": "group",
  "displayName": "Cisco HomePage",
  "contentUrl": "https://www.cisco.com",
  "creatorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
  "created": "2015-10-18T14:26:16.203Z"
}
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