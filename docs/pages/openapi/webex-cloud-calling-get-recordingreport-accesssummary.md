---
doc_id: webex-cloud-calling-get-recordingreport-accesssummary
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /recordingReport/accessSummary
operation_id: List of Recording Audit Report Summaries
tags: Recording Report
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.746493+00:00
---

# GET /recordingReport/accessSummary

**API:** Webex Cloud Calling
**Área:** Recording Report
**operationId:** `List of Recording Audit Report Summaries`

## Resumen
List of Recording Audit Report Summaries

## Descripción
Lists of recording audit report summaries. You can specify a date range and the maximum number of recording audit report summaries to return.

Only recording audit report summaries of meetings hosted by or shared with the authenticated user will be listed.

The list returned is sorted in descending order by the date and time that the recordings were created.

Long result sets are split into [pages](/docs/basics#pagination).

* If `siteUrl` is specified, the recording audit report summaries of the specified site will be listed; otherwise, recording audit report summaries of the user's preferred site will be listed. All available Webex sites and the preferred site of the user can be retrieved by the `Get Site List` API.

#### Request Header

* `timezone`: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default is UTC if `timezone` is not defined.

## Parámetros
- `max` [query] (number): Maximum number of recording audit report summaries to return in a single page. `max` must be equal to or greater than `1` and equal to or less than `100`. Por defecto: 10.
- `from` [query] (string): Starting date and time (inclusive) for recording audit report summaries to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `from` cannot be after `to`. Please note that the interval between `to` and `from` cannot exceed 90 days and the interval between the current time and `from` cannot exceed 365 days. Por defecto: If `to` is specified, the default value is 7 days before `to`; if `to` is not specified, the default value is 7 days before the current date and time..
- `to` [query] (string): Ending date and time (exclusive) for recording audit report summaries to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `to` cannot be before `from`. Please note that the interval between `to` and `from` cannot exceed 90 days and the interval between the current time and `from` cannot exceed 365 days. Por defecto: If `from` is specified, the default value is 7 days after `from`; if `from` is not specified, the default value is the current date and time..
- `hostEmail` [query] (string): Email address for the meeting host. This parameter is only used if the user or application calling the API has the admin on-behalf-of scopes. If set, the admin may specify the email of a user in a site they manage and the API will return recording audit report summaries of that user. If a special value of `all` is set for `hostEmail`, the admin can list recording audit report summaries of all users on the target site, not of a single user.
- `siteUrl` [query] (string): URL of the Webex site which the API lists recording audit report summaries from. If not specified, the API lists summary audit report for recordings from the user's preferred site. All available Webex sites and the preferred site of the user can be retrieved by `Get Site List` API.
- `timezone` [header] (string): e.g. UTC

## Ejemplo de invocación
```bash
curl -X GET '/recordingReport/accessSummary' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): An array of recording audit report summaries objects.
  - `recordingId` (string): A unique identifier for the recording.
  - `topic` (string): The recording's topic.
  - `timeRecorded` (string): The date and time the recording started in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. the time is the record button was clicked in the meeting.
  - `siteUrl` (string): Site URL for the recording.
  - `hostEmail` (string): Email address for the meeting host.
  - `viewCount` (number): The number of times the recording was viewed.
  - `downloadCount` (number): The number of times the recording was downloaded.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "recordingId": "4f914b1dfe3c4d11a61730f18c0f5387",
      "topic": "Example Topic",
      "timeRecorded": "2020-07-13T17:05:35Z",
      "siteUrl": "site4-example.webex.com",
      "hostEmail": "john.andersen@example.com",
      "viewCount": 18,
      "downloadCount": 10
    },
    {
      "recordingId": "3324fb76946249cfa07fc30b3ccbf580",
      "topic": "Example Topic",
      "timeRecorded": "2020-07-13T17:05:35Z",
      "siteUrl": "site4-example.webex.com",
      "hostEmail": "john.andersen@example.com",
      "viewCount": 0,
      "downloadCount": 2
    },
    {
      "recordingId": "42b80117a2a74dcf9863bf06264f8075",
      "topic": "Example Topic",
      "timeRecorded": "2020-07-13T17:05:35Z",
      "siteUrl": "site4-example.webex.com",
      "hostEmail": "john.andersen@example.com",
      "viewCount": 7,
      "downloadCount": 20
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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs