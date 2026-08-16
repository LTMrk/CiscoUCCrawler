---
doc_id: webex-meeting-delete-meetings-postmeetingchats
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: DELETE
path: /meetings/postMeetingChats
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.385109+00:00
---

# DELETE /meetings/postMeetingChats

**API:** Webex Meetings
**Área:** Chats
**operationId:** `Delete Meeting Chats`

## Resumen
Delete Meeting Chats

## Descripción
Deletes the meeting chats of a finished [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) specified by `meetingId`.

Use this operation to delete the chats of a finished [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) when they are ready. Please note that only **meeting instances** in state `ended` are supported for `meetingId`. **Meeting series**, **scheduled meetings** and `in-progress` **meeting instances** are not supported.

## Parámetros
- `meetingId` [query] (string) **(requerido)**: A unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the chats belong. Meeting IDs of a scheduled [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings) meeting are not supported.

## Respuestas
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
