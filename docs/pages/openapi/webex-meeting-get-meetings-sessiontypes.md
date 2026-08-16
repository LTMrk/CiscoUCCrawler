---
doc_id: webex-meeting-get-meetings-sessiontypes
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetings/sessionTypes
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.395779+00:00
---

# GET /meetings/sessionTypes

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `listMeetingSessionTypes`

## Resumen
List Meeting Session Types

## Descripción
List all the meeting session types enabled for a given user.

## Parámetros
- `hostEmail` [query] (string): Email address for the user. This parameter is only used if the user or application calling the API has the admin-level scopes. If set, the admin may specify the email of a user in a site they manage and the API will list all the meeting session types enabled for the user.
- `siteUrl` [query] (string): Webex site URL to query. If `siteUrl` is not specified, the users' preferred site will be used. If the authorization token has the admin-level scopes, the admin can set the Webex site URL on behalf of the user specified in the `hostEmail` parameter.

## Respuestas
- **200**: OK
  - `items` (array): Meeting session type array
    - `id` (string) **(requerido)**: Unique identifier for the meeting session type.
    - `name` (string) **(requerido)**: Name of the meeting session type.
    - `type` (string) **(requerido)**: Meeting session type.  * `meeting` - Meeting session type for a meeting.  * `webinar` - Meeting session type for a webinar.  * `privateMeeting` - Meeting session type for a private meeting. Valores: meeting, webinar, privateMeeting.
    - `attendeesCapacity` (number): The maximum number of attendees for the meeting session type.
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
