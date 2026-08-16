---
doc_id: webex-messaging-get-memberships
source: webex-openapi-specs/public-spec/webex-messaging.json
api: Webex Messaging
method: GET
path: /memberships
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.511992+00:00
---

# GET /memberships

**API:** Webex Messaging
**Área:** Memberships
**operationId:** `List Memberships`

## Resumen
List Memberships

## Descripción
Lists all room memberships. By default, lists memberships for rooms to which the authenticated user belongs.

Use query parameters to filter the response.

Use `roomId` to list memberships for a room, by ID.

**NOTE**: For moderated team spaces, the list of memberships will include only the space moderators if the user is a team member but not a direct participant of the space.

Use either `personId` or `personEmail` to filter the results. The `roomId` parameter is required when using these parameters.

When the requester is a compliance officer, they can query by `personId` or `personEmail` **WITHOUT** specifying a `roomId`. The response will include **ALL** memberships for the user where a space is owned by an org to which the user belongs.

Long result sets will be split into [pages](/docs/basics#pagination).

## Parámetros
- `roomId` [query] (string): List memberships associated with a room, by ID.
- `personId` [query] (string): List memberships associated with a person, by ID. The `roomId` parameter is required when using this parameter.
- `personEmail` [query] (string): List memberships associated with a person, by email address. The `roomId` parameter is required when using this parameter.
- `max` [query] (number): Limit the maximum number of memberships in the response.

## Respuestas
- **200**: OK
  - `items` (array):
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
