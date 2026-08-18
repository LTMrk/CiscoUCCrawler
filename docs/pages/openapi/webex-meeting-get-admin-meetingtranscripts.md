---
doc_id: webex-meeting-get-admin-meetingtranscripts
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /admin/meetingTranscripts
operation_id: List Meeting Transcripts For Compliance Officer
tags: Transcripts
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.474254+00:00
---

# GET /admin/meetingTranscripts

**API:** Webex Meetings
**Área:** Transcripts
**operationId:** `List Meeting Transcripts For Compliance Officer`

## Resumen
List Meeting Transcripts For Compliance Officer

## Descripción
Lists available or deleted transcripts of an ended [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) for a specific site.

The returned list is sorted in descending order by the date and time that the transcript was created.

#### Request Header

* `timezone`: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default is UTC if `timezone` is not defined.

## Parámetros
- `from` [query] (string): Starting date and time (inclusive) for transcripts to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `from` cannot be after `to`. Por defecto: If only `to` is specified, the default `from` value is 7 days before `to`; if no `to` or `from` is specified, the default `from` value is 7 days before the current date and time..
- `to` [query] (string): Ending date and time (exclusive) for List transcripts to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `to` cannot be before `from`. Por defecto: If `from` is specified, the default value is 7 days after `from`; if `from` is not specified, the default value is the current date and time..
- `max` [query] (number): Maximum number of transcripts to return in a single page. `max` must be equal to or greater than `1` and equal to or less than `100`. Por defecto: 10.
- `siteUrl` [query] (string) (**requerido**): URL of the Webex site from which the API lists transcripts.

## Ejemplo de invocación
```bash
curl -X GET '/admin/meetingTranscripts?siteUrl=<siteUrl>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): Transcript array
  - `id` (string) (**requerido**): A unique identifier for the transcript.
  - `siteUrl` (string) (**requerido**): URL of the Webex site from which the API lists meeting transcripts.
  - `startTime` (string) (**requerido**): Start time for the meeting transcript in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
  - `meetingTopic` (string) (**requerido**): The meeting's topic.
  - `meetingId` (string) (**requerido**): Unique identifier for the [meeting instance](/docs/meetings#meeting-series-scheduled-meetings-and-meeting-instances) to which the transcripts belong.
  - `scheduledMeetingId` (string) (**requerido**): Unique identifier for scheduled meeting with which the current meeting is associated. Only apples to a meeting instance which is happening or has happened. This is the `id` of the scheduled meeting with which the instance is associated.
  - `meetingSeriesId` (string): Unique identifier for the parent meeting series to which the recording belongs.
  - `hostUserId` (string) (**requerido**): Unique identifier for the meeting host.
  - `vttDownloadLink` (string) (**requerido**): The download link for the transcript vtt file.
  - `txtDownloadLink` (string) (**requerido**): The download link for the transcript txt file.
  - `status` (string) (**requerido**): * `available` - Transcript is available.  * `deleted` - Transcript has been deleted. Valores: available, deleted.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "8ce1f918-c138-4041-bb4a-5e01eeaadedb_M_0fc6ec11d9b6c909e04e1f6c76accda9",
      "startTime": "2020-06-02T20:30:15.042Z",
      "meetingId": "0ed74a1c0551494fb7a04e2881bf50ae_I_166022169160077044",
      "meetingTopic": "John's Meeting 01",
      "siteUrl": "example.webex.com",
      "scheduledMeetingId": "0ed74a1c0551494fb7a04e2881bf50ae_20210401T232500Z",
      "meetingSeriesId": "0ed74a1c0551494fb7a04e2881bf50ae",
      "hostUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS83QkFCQkU5OS1CNDNFLTREM0YtOTE0Ny1BMUU5RDQ2QzlDQTA",
      "vttDownloadLink": "http://site-example.webex.com/v1/meetingTranscripts/5e01eeaadedb_M_0fc6ec11d9b6c909e04e1f6c76accda9/download?format=vtt",
      "txtDownloadLink": "http://site-example.webex.com/v1/meetingTranscripts/5e01eeaadedb_M_0fc6ec11d9b6c909e04e1f6c76accda9/download?format=txt",
      "status": "available"
    },
    {
      "id": "074d892d-c7f7-4864-95db-31f7ae94206f_M_39f4371ca39c4a98b7f6ecc74247151e",
      "startTime": "2020-06-01T20:30:15.042Z",
      "meetingId": "0ed74a1c0551494fb7a04e2881bf50ae_I_166022169160077044",
      "meetingTopic": "John's Meeting 02",
      "siteUrl": "example.webex.com",
      "scheduledMeetingId": "0ed74a1c0551494fb7a04e2881bf50ae_20210401T232500Z",
      "meetingSeriesId": "0ed74a1c0551494fb7a04e2881bf50ae",
      "hostUserId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jN2ZkNzNmMi05ZjFlLTQ3ZjctYWEwNS05ZWI5OGJiNjljYzY",
      "vttDownloadLink": "http://site-example.webex.com/v1/meetingTran
  ... (truncado)
```

## Respuestas de error
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

## Contexto de la API
The Webex Meetings APIs enable developers to schedule, manage, and retrieve information about Webex meetings, webinars, and events. They provide endpoints for meeting creation, participant management, recordings, transcripts, in-meeting features such as chat and closed captions, and post-meeting analytics. Common use cases include integrating meeting scheduling into calendar apps, automating follow-ups with recordings and transcripts, embedding meeting controls in custom portals, and extracting insights for compliance or productivity analysis. The APIs support both real-time and asynchronous w...

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs