---
doc_id: webex-meeting-delete-meetinginvitees-meetinginviteeid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: DELETE
path: /meetingInvitees/{meetingInviteeId}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.386154+00:00
---

# DELETE /meetingInvitees/{meetingInviteeId}

**API:** Webex Meetings
**Área:** Invitees
**operationId:** `Delete a Meeting Invitee`

## Resumen
Delete a Meeting Invitee

## Descripción
Removes a meeting invitee identified by a `meetingInviteeId` specified in the URI. The deleted meeting invitee cannot be recovered.

If the meeting invitee is associated with a meeting series, the invitee will be removed from the entire meeting series. If the invitee is associated with a scheduled meeting, the invitee will be removed from only that scheduled meeting.

## Parámetros
- `meetingInviteeId` [path] (string) **(requerido)**: Unique identifier for the invitee to be removed. This parameter only applies to an invitee to a meeting series or a scheduled meeting. It doesn't apply to an invitee to an ended or ongoing meeting instance.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin on-behalf-of scopes. If set, the admin may specify the email of a user in a site they manage and the API will delete a meeting invitee that is hosted by that user.
- `sendEmail` [query] (boolean): If `true`, send an email to the invitee.

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
