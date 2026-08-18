---
doc_id: webex-meeting-get-group-recordings
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /group/recordings
operation_id: listGroupRecordings
tags: Recordings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.498923+00:00
---

# GET /group/recordings

**API:** Webex Meetings
**Área:** Recordings
**operationId:** `listGroupRecordings`

## Resumen
List Group Recordings

## Descripción
List group recordings for a service app which has group recording access. You can specify a date range, the maximum number of recordings to return, and `personId` or `hostEmail` of whom the recordings will be retrieved.

* The list returned is sorted in descending order by the date and time that the recordings were created.

* Only recordings which are in the `available` status and not shared by others can be listed. Those in the `deleted` or `purged` status or shared by others can't be listed.

* Long result sets are split into [pages](/docs/basics#pagination).

* If `siteUrl` is specified, the API lists group recordings on the specified site; otherwise, the API lists group recordings on all the sites managed by the service app. All the sites managed by a service app can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

* One of the `personId` parameter and `hostEmail` header must be specified so that only recordings of meetings hosted by the person of `personId` or `hostEmail` will be returned.

#### Request Header

* `timezone`: [Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default is UTC if `timezone` is not defined.

* `hostEmail`: Email of the user whose recordings will be retrieved. The `hostEmail` parameter is optional, but one of the `personId` parameter and `hostEmail` header must be specified.

## Parámetros
- `personId` [query] (string): Person ID of the user whose recordings will be retrieved. The person ID can be retrieved from the [People APIs](/docs/api/v1/people), e.g. [Lit People](/docs/api/v1/people/list-people). Note that a person ID retrieved from the People APIs is a Base64-encoded string, e.g. `Y2lzY29zcGFyazovL3VzL1BFT1BMRS9kNDdiMmU3ZC01ZTBmLTRmNjktYWVmNC1lNGZmOTBhZWE3Yzk`. The person ID in the raw UUID format which is the last part of the Base64-decoded string, e.g. `d47b2e7d-5e0f-4f69-aef4-e4ff90aea7c9`, is also supported. The `personId` parameter is optional, but one of the `personId` parameter and `hostEmail` header must be specified.
- `max` [query] (number): Maximum number of recordings to return in a single page. `max` must be equal to or greater than `1` and equal to or less than `100`. Por defecto: 10.
- `from` [query] (string): Starting date and time (inclusive) for recordings to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `from` cannot be after `to`. The interval between `from` and `to` must be within 30 days. Por defecto: If only `to` is specified, the default `from` value is 7 days before `to`; if no `to` or `from` is specified, the default `from` value is 7 days before current date and time..
- `to` [query] (string): Ending date and time (exclusive) for List recordings to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `to` cannot be before `from`. The interval between `from` and `to` must be within 30 days. Por defecto: If `from` is specified, the default value is 7 days after `from`; if `from` is not specified, the default value is the current date and time..
- `siteUrl` [query] (string): URL of the Webex site which the API lists recordings from. If not specified, the API lists recordings from user's preferred site. All available Webex sites and preferred site of the user can be retrieved by [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.
- `integrationTag` [query] (string): External key of the parent meeting created by an integration application. This parameter is used by the integration application to query recordings by a key in its own domain such as a Zendesk ticket ID, a Jira ID, a Salesforce Opportunity ID, etc. An integrationTag created by one client cannot be accessed or used as a filtering parameter by another client. For example, if a meeting has an `integrationTag` of "Sales" which is created by the client behind the developer portal, then this integrationTag can't be accessed on the meeting or its recordings by another client. Neither can it be used to filter meetings or recordings by a client other than the one that created the integrationTag of "Sales".
- `format` [query] (string): Recording's file format. If specified, the API filters recordings by format. Valores: MP4, ARF.
- `serviceType` [query] (string): The service type for recordings. If specified, the API filters recordings by service type. Valores: MeetingCenter, EventCenter, SupportCenter, TrainingCenter.
- `timezone` [header] (string): e.g. UTC
- `hostEmail` [header] (string): Email of the user whose recordings will be retrieved. The `hostEmail` parameter is optional, but one of the `personId` parameter and `hostEmail` header must be specified.

## Ejemplo de invocación
```bash
curl -X GET '/group/recordings' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `items` (array): An array of recording objects.
  - `id` (string) (**requerido**): A unique identifier for the recording.
  - `meetingId` (string) (**requerido**): Unique identifier for the recording's ended meeting instance.
  - `scheduledMeetingId` (string): Unique identifier for the recording's scheduled meeting instance.
  - `meetingSeriesId` (string): Unique identifier for the recording's meeting series.
  - `topic` (string) (**requerido**): The recording's topic.
  - `createTime` (string) (**requerido**): The date and time recording was created in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. Please note that it's not the time the record button was clicked in meeting but the time the recording file was generated offline.
  - `timeRecorded` (string) (**requerido**): The date and time recording started in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. It indicates when the record button was clicked in the meeting.
  - `siteUrl` (string) (**requerido**): Site URL for the recording.
  - `downloadUrl` (string) (**requerido**): The download link for recording. This attribute is not available if **Prevent downloading** has been turned on for the recording being requested. The **Prevent downloading** option can be viewed and set by a site admin on [Control Hub](https://help.webex.com/en-us/article/sxdj4ab/Manage-Security-for-a-Cisco-Webex-Site-in-Cisco-Webex-Control-Hub).
  - `playbackUrl` (string) (**requerido**): The playback link for recording.
  - `password` (string) (**requerido**): The recording's password.
  - `format` (string) (**requerido**): * `MP4` - Recording file format is MP4.  * `ARF` - Recording file format is ARF, a proprietary Webex recording format.  * `UPLOADED` - The recording file is uploaded manually. Valores: MP4, ARF, UPLOADED.
  - `serviceType` (string) (**requerido**): The service type for the recording.  * `MeetingCenter` - The service type for the recording is meeting.  * `EventCenter` - The service type for the recording is the event.  * `TrainingCenter` - The service type for the recording is the training session.  * `SupportCenter` - The service type for the recording is the support meeting. Valores: MeetingCenter, EventCenter, TrainingCenter, SupportCenter.
  - `durationSeconds` (number) (**requerido**): The duration of the recording, in seconds.
  - `sizeBytes` (number) (**requerido**): The size of the recording file, in bytes.
  - `shareToMe` (boolean) (**requerido**): Whether or not the recording has been shared to the current user. This attribute is hidden if the user calling the API is a Compliance Officer and `hostEmail` is not specified.
  - `integrationTags` (array): External keys of the parent meeting created by an integration application. They could be Zendesk ticket IDs, Jira IDs, Salesforce Opportunity IDs, etc. The integration application queries recordings by a key in its own domain.
  - `status` (string) (**requerido**): * `available` - Recording is available.  * `deleted` - Recording has been moved into recycle bin.  * `purged` - Recording has been purged from the recycle bin. Only applies if the user calling the API is a Compliance Officer and `meetingId` is specified. Valores: available, deleted, purged.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "4f914b1dfe3c4d11a61730f18c0f5387",
      "meetingId": "f91b6edce9864428af084977b7c68291_I_166641849979635652",
      "scheduledMeetingId": "f91b6edce9864428af084977b7c68291_20200713T121500Z",
      "meetingSeriesId": "f91b6edce9864428af084977b7c68291",
      "topic": "Example Topic",
      "createTime": "2020-07-13T17:11:35Z",
      "timeRecorded": "2020-07-13T17:05:35Z",
      "hostDisplayName": "John Andersen",
      "hostEmail": "john.andersen@example.com",
      "siteUrl": "site4-example.webex.com",
      "downloadUrl": "https://site4-example.webex.com/site4/lsr.php?RCID=b91990e37417bda24986e46cf43345ab",
      "playbackUrl": "https://site4-example.webex.com/site4/ldr.php?RCID=69201a61d1d94a84aca18817261d1a73",
      "password": "********",
      "format": "ARF",
      "serviceType": "MeetingCenter",
      "durationSeconds": 18416,
      "sizeBytes": 168103,
      "shareToMe": false,
      "integrationTags": [
        "dbaeceebea5c4a63ac9d5ef1edfe36b9",
        "85e1d6319aa94c0583a6891280e3437d",
        "27226d1311b947f3a68d6bdf8e4e19a1"
      ],
      "status": "available"
    },
    {
      "id": "3324fb76946249cfa07fc30b3ccbf580",
      "meetingId": "f91b6edce9864428af084977b7c68291_I_166641849979635652",
      "scheduledMeetingId": "f91b6edce9864428af084977b7c68291_20200713T121500Z",
      "meetingSeriesId": "f91b6edce9864428af084977b7c68291",
      "topic": "Example Topic",
      "createTime": "2020-07-13T17:11:34Z",
      "timeReco
  ... (truncado)
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