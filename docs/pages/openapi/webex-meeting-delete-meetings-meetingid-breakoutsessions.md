---
doc_id: webex-meeting-delete-meetings-meetingid-breakoutsessions
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: DELETE
path: /meetings/{meetingId}/breakoutSessions
operation_id: deleteBreakoutSessions
tags: Meetings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.489213+00:00
---

# DELETE /meetings/{meetingId}/breakoutSessions

**API:** Webex Meetings
**Área:** Meetings
**operationId:** `deleteBreakoutSessions`

## Resumen
Delete Meeting Breakout Sessions

## Descripción
Deletes breakout sessions with a specified meeting ID. The deleted breakout sessions cannot be recovered. The value of `enabledBreakoutSessions` attribute is set to `false` automatically.
This operation applies to meeting series and scheduled meetings. It doesn't apply to ended or in-progress meeting instances.

## Parámetros
- `meetingId` [path] (string) (**requerido**): Unique identifier for the meeting. This parameter applies to meeting series and scheduled meetings. It doesn't apply to ended or in-progress meeting instances.
- `sendEmail` [query] (boolean): Whether or not to send emails to host and invitees. It is an optional field and default value is true.
- `hostEmail` [header] (string): e.g. `john.andersen@example.com` (string, optional) - Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin-level scopes. If set, the admin may specify the email of a user in a site they manage and the API will delete breakout sessions that are created by that user.

## Ejemplo de invocación
```bash
curl -X DELETE '/meetings/<meetingId>/breakoutSessions' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**204**: No Content

## Respuestas de error
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

## Contexto de la API
The Webex Meetings APIs enable developers to schedule, manage, and retrieve information about Webex meetings, webinars, and events. They provide endpoints for meeting creation, participant management, recordings, transcripts, in-meeting features such as chat and closed captions, and post-meeting analytics. Common use cases include integrating meeting scheduling into calendar apps, automating follow-ups with recordings and transcripts, embedding meeting controls in custom portals, and extracting insights for compliance or productivity analysis. The APIs support both real-time and asynchronous w...

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs