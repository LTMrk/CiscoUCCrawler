---
doc_id: webex-meeting-put-admin-meeting-userconfig-sessiontypes
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: PUT
path: /admin/meeting/userconfig/sessionTypes
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.390266+00:00
---

# PUT /admin/meeting/userconfig/sessionTypes

**API:** Webex Meetings
**Área:** Session Types
**operationId:** `Update User Session Types`

## Resumen
Update User Session Types

## Descripción
Assign session types to specific users.

* At least one of the following body parameters is required to update a specific user session type: `personId`, `email`.

## Cuerpo de la petición (application/json)
- `siteUrl` (string) **(requerido)**: Site URL for the session type.
- `personId` (string): A unique identifier for the user.
- `email` (string): The email of the user.
- `sessionTypeIds` (array) **(requerido)**: An array of the session type ID.

## Respuestas
- **200**: OK
  - `personId` (string): A unique identifier for the user.
  - `email` (string): The email of the user.
  - `siteUrl` (string): Site URL for the user.
  - `sessionTypes` (array): All session types are supported by the user on the site.
    - `id` (string): The ID of the session type.
    - `shortName` (string): The short name of the session type.
    - `name` (string): The name of the session type.
    - `type` (string): The meeting type of meeting that you can create with the session type.  * `meeting` - Meeting Center.  * `webinar` - Webinar meeting.  * `privateMeeting` - Private meeting.  * `EventCenter` - Event Center.  * `SupportCenter` - Support Center.  * `TrainCenter` - Training Center. Valores: meeting, webinar, privateMeeting, EventCenter, SupportCenter, TrainCenter.
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
