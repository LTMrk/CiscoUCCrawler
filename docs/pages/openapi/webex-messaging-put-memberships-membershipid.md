---
doc_id: webex-messaging-put-memberships-membershipid
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
method: PUT
path: /memberships/{membershipId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.512326+00:00
---

# PUT /memberships/{membershipId}

**API:** Webex Messaging
**Área:** Memberships
**operationId:** `Update a Membership`

## Resumen
Update a Membership

## Descripción
Updates properties for a membership by ID.

Specify the membership ID in the `membershipId` URI parameter.

## Parámetros
- `membershipId` [path] (string) **(requerido)**: The unique identifier for the membership.

## Cuerpo de la petición (application/json)
- `isModerator` (boolean) **(requerido)**: Whether or not the participant is a room moderator.
- `isRoomHidden` (boolean) **(requerido)**: When set to true, hides direct spaces in the teams client. Any new message will make the room visible again.

### Ejemplo de petición
```json
{
  "isModerator": true,
  "isRoomHidden": false
}
```

## Respuestas
- **200**: OK
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
