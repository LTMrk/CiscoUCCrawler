---
doc_id: webex-meeting-delete-meetings-meetingid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: DELETE
path: /meetings/{meetingId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.394874+00:00
---

# DELETE /meetings/{meetingId}

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `deleteMeeting`

## Resumen
Delete a Meeting

## Descripción
<div>
<Callout type="warning">If only guests are waiting in the lobby and the host or cohost has not started the meeting, the meeting state remains `inProgress` for 5 minutes after the last guest leaves. The meeting cannot be deleted during this time. If the meeting is started by the host or cohost and then ended normally, it can be deleted immediately after it ends.</Callout>
</div>

Deletes a meeting with a specified meeting ID. The deleted meeting cannot be recovered. This operation applies to meeting series and scheduled meetings. It doesn't apply to ended or in-progress meeting instances. Ad-hoc meetings created by [Create a Meeting](/docs/api/v1/meetings/create-a-meeting) with `adhoc` of `true` and a `roomId` cannot be deleted.

* If the `meetingId` value specified is for a scheduled meeting, the operation deletes that scheduled meeting without impact on other scheduled meeting of the parent meeting series.

* If the `meetingId` value specified is for a meeting series, the operation deletes the entire meeting series.

## Parámetros
- `meetingId` [path] (string) **(requerido)**: Unique identifier for the meeting to be deleted. This parameter applies to meeting series and scheduled meetings. It doesn't apply to ended or in-progress meeting instances.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. If set, the admin may specify the email of a user in a site they manage and the API will delete a meeting that is hosted by that user.
- `sendEmail` [query] (boolean): Whether or not to send emails to host and invitees. It is an optional field and default value is true.

## Respuestas
- **204**: No Content
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found
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
