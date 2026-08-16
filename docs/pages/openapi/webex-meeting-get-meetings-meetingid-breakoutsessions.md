---
doc_id: webex-meeting-get-meetings-meetingid-breakoutsessions
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetings/{meetingId}/breakoutSessions
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.398535+00:00
---

# GET /meetings/{meetingId}/breakoutSessions

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `listBreakoutSessions`

## Resumen
List Meeting Breakout Sessions

## Descripción
Lists meeting breakout sessions for a meeting with a specified `meetingId`.

This operation can be used for meeting series, scheduled meeting and ended or ongoing meeting instance objects. See the [Webex Meetings](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) guide for more information about the types of meetings.

* If the meeting of `meetingId` is in progress, the operation returns the breakout sessions which are currently held in the meeting.

* If the meeting of `meetingId` is ended meeting instance, the operation returns the breakout sessions which happended during the meeting instance.

* Otherwise, if it's a meeting series or scheduled meeting and it's not in progress, the operation returns the breakout sessions which are created when the meeting is scheduled.

## Parámetros
- `meetingId` [path] (string) **(requerido)**: Unique identifier for the meeting. This parameter applies to meeting series, scheduled meeting and ended or ongoing meeting instance objects. Please note that currently meeting ID of a scheduled [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings) meeting is not supported for this API.
- `hostEmail` [header] (string): e.g. `john.andersen@example.com` (string, optional) - Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. If set, the admin may specify the email of a user in a site they manage and the API will return details for a meeting that is hosted by that user.

## Respuestas
- **200**: OK
  - `items` (array): Breakout sessions information for meeting.
    - `id` (string) **(requerido)**: Unique identifier for breakout session.
    - `name` (string) **(requerido)**: Name for breakout session.
    - `invitees` (array): Invitees for breakout session. Only applies to breakout sessions which are created when meeting is scheduled.
    - `startTime` (string): The time the breakout session was started. Only applies to breakout sessions of ended meeting instances.
    - `endTime` (string): The time the breakout session was ended. Only applies to breakout sessions of ended meeting instances.
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
