---
doc_id: webex-messaging-get-room-linkedfolders-id
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
method: GET
path: /room/linkedFolders/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.510093+00:00
---

# GET /room/linkedFolders/{id}

**API:** Webex Messaging
**Área:** ECM folder linking
**operationId:** `Get ECM Folder Details`

## Resumen
Get ECM Folder Details

## Descripción
Get details for a room ECM folder with the specified folder id.

## Parámetros
- `id` [path] (string) **(requerido)**: The unique identifier for the folder.

## Respuestas
- **200**: OK
  - `id` (string): A unique identifier for the folder.
  - `roomId` (string): A unique identifier for the room to which the folder should be linked to.
  - `roomType` (string): The room type.  * `direct` - 1:1 room  * `group` - group room Valores: direct, group.
  - `driveId` (string) **(requerido)**: Sharepoint or OneDrive drive id. It can be queried via MS Graph APIs.
  - `itemId` (string) **(requerido)**: Sharepoint or OneDrive item id. It can be queried via MS Graph APIs.
  - `defaultFolder` (string): Indicates if this is the default content storage for the room.
  - `displayName` (string) **(requerido)**: This should match the folder name in the ECM backend.
  - `contentUrl` (string): Folder's content URL.
  - `creatorId` (string): The person ID of the person who created this folder link.
  - `created` (string): The date and time when the folder link was created.
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
