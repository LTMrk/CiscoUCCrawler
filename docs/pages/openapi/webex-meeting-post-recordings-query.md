---
doc_id: webex-meeting-post-recordings-query
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
method: POST
path: /recordings/query
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:33.402553+00:00
---

# POST /recordings/query

**API:** Webex Meetings
**Área:** Recordings
**operationId:** `queryRecordings`

## Resumen
Query Recordings

## Descripción
Queries recordings with filters in the request body. You can specify a date range, a parent meeting ID, the maximum number of recordings to return, and additional filters such as siteUrl, integrationTag, hostEmail, topic, format, serviceType, and status.

Only recordings of meetings hosted by or shared with the authenticated user will be listed.

The list returned is sorted in descending order by the date and time that the recordings were created.

Long result sets are split into [pages](/docs/basics#pagination).

* If `meetingId` is specified, only recordings associated with the specified meeting will be listed. **NOTE**: when `meetingId` is specified, parameter of `siteUrl` will be ignored.

* If `siteUrl` is specified, recordings of the specified site will be listed; otherwise, the API lists recordings of all the user's sites. All available Webex sites and preferred site of the user can be retrieved by [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

#### Request Header

* `timezone`: *[Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default is UTC if `timezone` is not defined.*

## Parámetros
- `timezone` [header] (string): e.g. UTC

## Cuerpo de la petición (application/json)
- `max` (number): Maximum number of recordings to return in a single page. `max` must be equal to or greater than `1` and equal to or less than `100`.
- `from` (string): Starting date and time (inclusive) for recordings to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `from` cannot be after `to`.
- `to` (string): Ending date and time (exclusive) for query recordings to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `to` cannot be before `from`.
- `meetingId` (string): Unique identifier for the parent meeting series, scheduled meeting, or meeting instance for which recordings are being requested. If a meeting series ID is specified, the operation returns an array of recordings for the specified meeting series. If a scheduled meeting ID is specified, the operation returns an array of recordings for the specified scheduled meeting. If a meeting instance ID is specified, the operation returns an array of recordings for the specified meeting instance. If no ID is specified, the operation returns an array of recordings for all meetings of the current user. When `meetingId` is specified, the `siteUrl` parameter is ignored.
- `siteUrl` (string): URL of the Webex site from which the API lists recordings. If not specified, the API lists recordings from all of a user's sites. All available Webex sites and the preferred site of the user can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.
- `integrationTag` (string): External key of the parent meeting created by an integration application. This parameter is used by the integration application to query recordings by a key in its own domain, such as a Zendesk ticket ID, a Jira ID, a Salesforce Opportunity ID, etc. An integrationTag created by one client cannot be accessed or used as a filtering parameter by another client. For example, if a meeting has an `integrationTag` of "Sales" which is created by the client behind the developer portal, then this integrationTag can't be accessed on the meeting or its recordings by another client. Neither can it be used to filter meetings or recordings by a client other than the one that created the integrationTag of "Sales".
- `hostEmail` (string): Email address for the meeting host. This property is only used if the caller has admin-level meeting scopes. If set, the admin may specify the email of a user in a site they manage and the API will return recordings of that user.
- `topic` (string): Recording's topic. If specified, the API filters recordings by topic in a case-insensitive manner.
- `format` (string): Recording's file format. If specified, the API filters recordings by format. Valores: MP4, ARF.
- `serviceType` (string): The service type for recordings. If this item is specified, the API filters recordings by service-type. Valores: MeetingCenter, EventCenter, SupportCenter, TrainingCenter.
- `status` (string): Recording's status. If not specified or `available`, retrieves recordings that are available. Otherwise, if specified as `deleted`, retrieves recordings that have been moved into the recycle bin. The `purged` status only applies if the user calling the API is a Compliance Officer and `meetingId` is specified. Valores: available, deleted, purged.

### Ejemplo de petición
```json
{
  "max": 10,
  "from": "2020-07-12T09:30:00+08:00",
  "to": "2020-07-31T09:30:00+08:00",
  "meetingId": "f91b6edce9864428af084977b7c68291_I_166641849979635652",
  "siteUrl": "site4-example.webex.com",
  "integrationTag": "dbaeceebea5c4a63ac9d5ef1edfe36b9",
  "hostEmail": "john.andersen@example.com",
  "topic": "John's Meeting",
  "format": "ARF",
  "serviceType": "MeetingCenter",
  "status": "available"
}
```

## Respuestas
- **200**: OK
  - `items` (array): An array of recording objects.
    - `id` (string) **(requerido)**: A unique identifier for the recording.
    - `meetingId` (string) **(requerido)**: Unique identifier for the recording's ended meeting instance.
    - `scheduledMeetingId` (string): Unique identifier for the recording's scheduled meeting instance.
    - `meetingSeriesId` (string): Unique identifier for the recording's meeting series.
    - `topic` (string) **(requerido)**: The recording's topic.
    - `createTime` (string) **(requerido)**: The date and time recording was created in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. Please note that it's not the time the record button was clicked in meeting but the time the recording file was generated offline.
    - `timeRecorded` (string) **(requerido)**: The date and time recording started in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. It indicates when the record button was clicked in the meeting.
    - `siteUrl` (string) **(requerido)**: Site URL for the recording.
    - `downloadUrl` (string) **(requerido)**: The download link for recording. This attribute is not available if **Prevent downloading** has been turned on for the recording being requested. The **Prevent downloading** option can be viewed and set by a site admin on [Control Hub](https://help.webex.com/en-us/article/sxdj4ab/Manage-Security-for-a-Cisco-Webex-Site-in-Cisco-Webex-Control-Hub).
    - `playbackUrl` (string) **(requerido)**: The playback link for recording.
    - `password` (string) **(requerido)**: The recording's password.
    - `format` (string) **(requerido)**: * `MP4` - Recording file format is MP4.  * `ARF` - Recording file format is ARF, a proprietary Webex recording format.  * `UPLOADED` - The recording file is uploaded manually. Valores: MP4, ARF, UPLOADED.
    - `serviceType` (string) **(requerido)**: The service type for the recording.  * `MeetingCenter` - The service type for the recording is meeting.  * `EventCenter` - The service type for the recording is the event.  * `TrainingCenter` - The service type for the recording is the training session.  * `SupportCenter` - The service type for the recording is the support meeting. Valores: MeetingCenter, EventCenter, TrainingCenter, SupportCenter.
    - `durationSeconds` (number) **(requerido)**: The duration of the recording, in seconds.
    - `sizeBytes` (number) **(requerido)**: The size of the recording file, in bytes.
    - `shareToMe` (boolean) **(requerido)**: Whether or not the recording has been shared to the current user. This attribute is hidden if the user calling the API is a Compliance Officer and `hostEmail` is not specified.
    - `integrationTags` (array): External keys of the parent meeting created by an integration application. They could be Zendesk ticket IDs, Jira IDs, Salesforce Opportunity IDs, etc. The integration application queries recordings by a key in its own domain.
    - `status` (string) **(requerido)**: * `available` - Recording is available.  * `deleted` - Recording has been moved into recycle bin.  * `purged` - Recording has been purged from the recycle bin. Only applies if the user calling the API is a Compliance Officer and `meetingId` is specified. Valores: available, deleted, purged.
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
