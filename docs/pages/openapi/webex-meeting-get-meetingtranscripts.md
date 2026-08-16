---
doc_id: webex-meeting-get-meetingtranscripts
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: GET
path: /meetingTranscripts
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.390760+00:00
---

# GET /meetingTranscripts

**API:** Webex Meetings
**Área:** Transcripts
**operationId:** `List Meeting Transcripts`

## Resumen
List Meeting Transcripts

## Descripción
Lists available transcripts of an ended [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances).

Use this operation to list transcripts of an ended [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) when they are ready. Please note that only **meeting instances** in state `ended` are supported for `meetingId`. **Meeting series**, **scheduled meetings** and `in-progress` **meeting instances** are not supported.

#### Request Header

* `timezone`: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default is UTC if `timezone` is not defined.

## Parámetros
- `max` [query] (number): Maximum number of transcripts to return in a single page. `max` must be equal to or greater than `1` and equal to or less than `100`.
- `from` [query] (string): Starting date and time (inclusive) for transcripts to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `from` cannot be after `to`.
- `to` [query] (string): Ending date and time (exclusive) for List transcripts to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `to` cannot be before `from`.
- `meetingId` [query] (string): Unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the transcript belongs. Please note that currently the meeting ID of a scheduled [personal room](https://help.webex.com/en-us/article/nul0wut/Webex-Personal-Rooms-in-Webex-Meetings) meeting is not supported for this API. If `meetingId` is not specified, the operation returns an array of transcripts for all meetings of the current user.
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the `admin-level` scopes. If set, the admin may specify the email of a user in a site they manage and the API will return details for a meeting that is hosted by that user. If `meetingId` is not specified, it can not support `hostEmail`.
- `siteUrl` [query] (string): URL of the Webex site from which the API lists transcripts. If not specified, the API lists transcripts from user's preferred site. All available Webex sites and the preferred site of the user can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

## Respuestas
- **200**: OK
  - `items` (array): Transcript array.
    - `id` (string) **(requerido)**: A unique identifier for the transcript.
    - `siteUrl` (string) **(requerido)**: URL of the Webex site from which the API lists meeting transcripts.
    - `startTime` (string) **(requerido)**: Start time for the meeting transcript in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
    - `meetingTopic` (string) **(requerido)**: The meeting's topic.
    - `meetingId` (string) **(requerido)**: Unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the transcripts belong.
    - `scheduledMeetingId` (string) **(requerido)**: Unique identifier for scheduled meeting with which the current meeting is associated. Only apples to a meeting instance which is happening or has happened. This is the `id` of the scheduled meeting with which the instance is associated.
    - `meetingSeriesId` (string): Unique identifier for the parent meeting series to which the recording belongs.
    - `hostUserId` (string) **(requerido)**: Unique identifier for the meeting host.
    - `vttDownloadLink` (string) **(requerido)**: The download link for the transcript vtt file.
    - `txtDownloadLink` (string) **(requerido)**: The download link for the transcript txt file.
    - `status` (string) **(requerido)**: * `available` - Transcript is available.  * `deleted` - Transcript has been deleted. Valores: available, deleted.
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
