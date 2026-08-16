---
doc_id: webex-meeting-get-meetingsummaries
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetingSummaries
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.390367+00:00
---

# GET /meetingSummaries

**API:** Webex Meetings
**Área:** Summaries
**operationId:** `getSummaryByMeetingID`

## Resumen
Get Summary by Meeting ID

## Descripción
Get the summary of an ended [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) by the meeting ID.

Please note that only **meeting instances** in state `ended` are supported, and currently the meeting ID of a meeting series, a scheduled meeting, an in-progress meeting instance, or a scheduled personal room meeting is not supported for this API. This API can only fetch summaries that you have access to, and if a meeting summary is deleted, you won't be able to see it either. And, this is an API for normal user. If you are a compliance officer, please use the Get Summary For Compliance Officer API

## Parámetros
- `meetingId` [query] (string): Unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the summary belongs. Please note that currently the meeting ID of a meeting series, a scheduled meeting, an in-progress meeting instance, or a scheduled personal room meeting is not supported for this API. If `meetingId` is not specified, the query will be rejected.

## Respuestas
- **200**: OK
  - `items` (array): Meeting summary object.
    - `id` (string): A unique identifier for the summary.
    - `meetingId` (string): Unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the summary belongs.
    - `status` (string): * `available` - Summary is available.  * `deleted` - Summary has been deleted.   Normal users can only see available summaries. Compliance officers can see both available and deleted summaries. Valores: available, deleted.
    - `notes` (object): Meeting summaries in HTML format
      - `content` (string) **(requerido)**: Summary of the meeting in HTML format
    - `actionItems` (array): A list of action items
      - `content` (string) **(requerido)**: Action item in plaintext
- **400**: Bad Request
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
