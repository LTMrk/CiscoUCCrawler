---
doc_id: webex-meeting-get-recordingreport-meetingarchivesummaries
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /recordingReport/meetingArchiveSummaries
operation_id: List Meeting Archive Summaries
tags: Recording Report
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.495462+00:00
---

# GET /recordingReport/meetingArchiveSummaries

**API:** Webex Meetings
**Área:** Recording Report
**operationId:** `List Meeting Archive Summaries`

## Resumen
List Meeting Archive Summaries

## Descripción
Lists of meeting archive summaries. You can specify a date range and the maximum number of meeting archive summaries to return.

Meeting archive summaries are only available to full administrators, not even the meeting host.

The list returned is sorted in descending order by the date and time that the archives were created.

Long result sets are split into [pages](/docs/basics#pagination).

* If `siteUrl` is specified, the meeting archive summaries of the specified site will be listed; otherwise, meeting archive summaries of the user's preferred site will be listed. All available Webex sites and the preferred site of the user can be retrieved by the `Get Site List` API.

#### Request Header

* `timezone`: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default is UTC if `timezone` is not defined.

## Parámetros
- `max` [query] (number): Maximum number of meeting archive summaries to return in a single page. `max` must be equal to or greater than `1` and equal to or less than `100`. Por defecto: 10.
- `from` [query] (string): Starting date and time (inclusive) for meeting archive summaries to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `from` cannot be after `to`. Please note that the interval between `to` and `from` cannot exceed 30 days. Por defecto: If `to` is specified, the default value is 7 days before `to`; if `to` is not specified, the default value is 7 days before the current date and time..
- `to` [query] (string): Ending date and time (exclusive) for meeting archive summaries to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `to` cannot be before `from`. Please note that the interval between `to` and `from` cannot exceed 30 days. Por defecto: If `from` is specified, the default value is 7 days after `from`; if `from` is not specified, the default value is the current date and time..
- `siteUrl` [query] (string): URL of the Webex site which the API lists meeting archive summaries from. If not specified, the API lists meeting archive summaries for recordings from the user's preferred site. All available Webex sites and the preferred site of the user can be retrieved by `Get Site List` API.
- `timezone` [header] (string): e.g. UTC

## Ejemplo de invocación
```bash
curl -X GET '/recordingReport/meetingArchiveSummaries' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): An array of meeting archive summaries objects.
  - `archiveId` (string): A unique identifier for the meeting archive summary.
  - `serviceType` (string): Recording achrive summary's service-type. Valores: MeetingCenter, EventCenter, TrainingCenter, SupportCenter.
  - `title` (string): Meeting title.
  - `createTime` (string): The date and time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format that when the archive was created by the system.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "archiveId": "7d7ea5f42b921eace05386ca24ad730e_R_1000634462",
      "serviceType": "MeetingCenter",
      "title": "Test003_xml",
      "createTime": "2022-10-31T15:50:11Z"
    },
    {
      "archiveId": "7d7ea5f42b921eace05386ca24ad730e_R_1000634107",
      "serviceType": "MeetingCenter",
      "title": "Gang test pwd 01_xml",
      "createTime": "2022-10-31T09:08:00Z"
    },
    {
      "archiveId": "7d7ea5f42b921eace05386ca24ad730e_R_1000633967",
      "serviceType": "MeetingCenter",
      "title": "Numeric password Test2_xml",
      "createTime": "2022-10-31T07:53:05Z"
    },
    {
      "archiveId": "7d7ea5f42b921eace05386ca24ad730e_R_1000633912",
      "serviceType": "MeetingCenter",
      "title": "Numeric password Test2_xml",
      "createTime": "2022-10-31T07:44:31Z"
    }
  ]
}
```
- Cabecera `Link`: 

## Respuestas de error
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

## Contexto de la API
The Webex Meetings APIs enable developers to schedule, manage, and retrieve information about Webex meetings, webinars, and events. They provide endpoints for meeting creation, participant management, recordings, transcripts, in-meeting features such as chat and closed captions, and post-meeting analytics. Common use cases include integrating meeting scheduling into calendar apps, automating follow-ups with recordings and transcripts, embedding meeting controls in custom portals, and extracting insights for compliance or productivity analysis. The APIs support both real-time and asynchronous w...

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs