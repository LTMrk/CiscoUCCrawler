---
doc_id: webex-messaging-post-memberships
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
api_version: 1.0.0
method: POST
path: /memberships
operation_id: Create a Membership
tags: Memberships
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.807101+00:00
---

# POST /memberships

**API:** Webex Messaging
**Área:** Memberships
**operationId:** `Create a Membership`

## Resumen
Create a Membership

## Descripción
Add someone to a room by Person ID or email address, optionally making them a moderator. Compliance Officers cannot add people to empty (team) spaces.

## Cuerpo de la petición (application/json)
- `roomId` (string) (**requerido**): The room ID.
- `personId` (string): The person ID.
- `personEmail` (string): The email address of the person.
- `isModerator` (boolean): Whether or not the participant is a room moderator.

### Ejemplo — petición
```json
{
  "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
  "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
  "personEmail": "john.andersen@example.com",
  "isModerator": true
}
```

## Ejemplo de invocación
```bash
curl -X POST '/memberships' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"roomId": "<roomId>"}'
```

## Respuestas correctas
**200**: OK
- `id` (string): A unique identifier for the membership.
- `roomId` (string): The room ID.
- `personId` (string): The person ID.
- `personEmail` (string): The email address of the person.
- `personDisplayName` (string): The display name of the person.
- `personOrgId` (string): The organization ID of the person.
- `isModerator` (boolean): Whether or not the participant is a room moderator.
- `isRoomHidden` (boolean): Whether or not the direct type room is hidden in the Webex clients.
- `roomType` (string): The type of room the membership is associated with.  * `direct` - 1:1 room.  * `group` - Group room. Valores: direct, group.
- `isMonitor` (boolean): Whether or not the participant is a monitoring bot (deprecated).
- `created` (string): The date and time when the membership was created.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL01FTUJFUlNISVAvMGQwYzkxYjYtY2U2MC00NzI1LWI2ZDAtMzQ1NWQ1ZDExZWYzOmNkZTFkZDQwLTJmMGQtMTFlNS1iYTljLTdiNjU1NmQyMjA3Yg",
  "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
  "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mNWIzNjE4Ny1jOGRkLTQ3MjctOGIyZi1mOWM0NDdmMjkwNDY",
  "personEmail": "john.andersen@example.com",
  "personDisplayName": "John Andersen",
  "personOrgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi85NmFiYzJhYS0zZGNjLTExZTUtYTE1Mi1mZTM0ODE5Y2RjOWE",
  "isModerator": true,
  "isRoomHidden": false,
  "roomType": "direct",
  "isMonitor": false,
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