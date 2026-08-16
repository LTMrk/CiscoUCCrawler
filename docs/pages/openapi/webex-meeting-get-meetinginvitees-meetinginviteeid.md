---
doc_id: webex-meeting-get-meetinginvitees-meetinginviteeid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetingInvitees/{meetingInviteeId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.385939+00:00
---

# GET /meetingInvitees/{meetingInviteeId}

**API:** Webex Meetings
**Área:** Invitees
**operationId:** `Get a Meeting Invitee`

## Resumen
Get a Meeting Invitee

## Descripción
Retrieve details for a meeting invitee identified by a `meetingInviteeId` in the URI.

## Parámetros
- `meetingInviteeId` [path] (string) **(requerido)**: Unique identifier for the invitee whose details are being requested.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin on-behalf-of scopes. If set, the admin may specify the email of a user in a site they manage and the API will return details for a meeting invitee that is hosted by that user.

## Respuestas
- **200**: OK
  - `id` (string) **(requerido)**: Unique identifier for meeting invitee.
  - `email` (string) **(requerido)**: Email address for meeting invitee. This attribute can be modified by `Update a Meeting Invitee` API.
  - `displayName` (string) **(requerido)**: Display name for meeting invitee. This attribute can be modified by `Update a Meeting Invitee` API.
  - `coHost` (boolean): Whether or not invitee is a designated alternate host for the meeting. See [Add Alternate Hosts for Cisco Webex Meetings](https://help.webex.com/b5z6he/) for more details.
  - `meetingId` (string) **(requerido)**: Unique identifier for the meeting for which invitees are being requested. The meeting can be a meeting series, a scheduled meeting, or a meeting instance which has ended or is ongoing.
  - `panelist` (boolean): If `true`, the invitee is a designated panelist for the event meeting.
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
