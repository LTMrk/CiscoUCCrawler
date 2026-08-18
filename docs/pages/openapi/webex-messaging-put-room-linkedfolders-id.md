---
doc_id: webex-messaging-put-room-linkedfolders-id
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
api_version: 1.0.0
method: PUT
path: /room/linkedFolders/{id}
operation_id: Update an ECM Linked Folder
tags: ECM folder linking
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.803227+00:00
---

# PUT /room/linkedFolders/{id}

**API:** Webex Messaging
**Área:** ECM folder linking
**operationId:** `Update an ECM Linked Folder`

## Resumen
Update an ECM Linked Folder

## Descripción
Updates the configuration of the specified Room folder. There is no data validation happening for the request. Please ensure the correct `driveId` and `itemId.` These can be collected from the MS Graph API. The `contentUrl` and `displayName` are used only for user convenience. The folder will be configured with the MS folder name as `displayName`, and the `contentURL` may be updated or corrected as needed. To assess final configuration, please make a GET request on the linkedFolder.

## Parámetros
- `id` [path] (string) (**requerido**): The unique identifier for the room folder.

## Cuerpo de la petición (application/json)
- `roomId` (string) (**requerido**): ID of the room that contains the room tab in question.
- `contentUrl` (string) (**requerido**): Content URL of the folder.
- `displayName` (string) (**requerido**): This should match the folder name in the ECM backend.
- `driveId` (string) (**requerido**): Sharepoint or OneDrive drive id. It can be queried via MS Graph APIs.
- `itemId` (string) (**requerido**): Sharepoint or OneDrive item id. It can be queried via MS Graph APIs.
- `defaultFolder` (string) (**requerido**): Makes the folder the default storage for the space.

### Ejemplo — petición
```json
{
  "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
  "contentUrl": "https://cisco-my.sharepoint.com/personal/naalluri/123",
  "displayName": "OneDrive folder for shared documents",
  "driveId": "123",
  "itemId": "456",
  "defaultFolder": "false"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/room/linkedFolders/<id>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"roomId": "<roomId>", "contentUrl": "<contentUrl>", "displayName": "<displayName>", "driveId": "<driveId>", "itemId": "<itemId>", "defaultFolder": "<defaultFolder>"}'
```

## Respuestas correctas
**200**: OK
- `id` (string): A unique identifier for the folder.
- `roomId` (string): A unique identifier for the room to which the folder should be linked to.
- `roomType` (string): The room type.  * `direct` - 1:1 room  * `group` - group room Valores: direct, group.
- `driveId` (string) (**requerido**): Sharepoint or OneDrive drive id. It can be queried via MS Graph APIs.
- `itemId` (string) (**requerido**): Sharepoint or OneDrive item id. It can be queried via MS Graph APIs.
- `defaultFolder` (string): Indicates if this is the default content storage for the room.
- `displayName` (string) (**requerido**): This should match the folder name in the ECM backend.
- `contentUrl` (string): Folder's content URL.
- `creatorId` (string): The person ID of the person who created this folder link.
- `created` (string): The date and time when the folder link was created.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hL1RBQlMvZDg1ZTYwNj",
  "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
  "roomType": "group",
  "driveId": "123",
  "itemId": "456",
  "defaultFolder": "false",
  "displayName": "OneDrive folder for shared documents",
  "contentUrl": "https://cisco-my.sharepoint.com/personal/naalluri/123",
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