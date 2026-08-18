---
doc_id: webex-admin-post-admin-recordings-query
source: webex-openapi-specs/public-spec/webex-admin.json
api: Webex Admin
api_version: 1.0.0
method: POST
path: /admin/recordings/query
operation_id: queryRecordingsForAdminOrComplianceOfficer
tags: Recordings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:42.575379+00:00
---

# POST /admin/recordings/query

**API:** Webex Admin
**Área:** Recordings
**operationId:** `queryRecordingsForAdminOrComplianceOfficer`

## Resumen
Query Recordings For an Admin or Compliance Officer

## Descripción
Queries recordings for an admin or compliance officer with filters in the request body. You can specify a date range, a parent meeting ID, the maximum number of recordings to return, and additional filters such as siteUrl, integrationTag, topic, format, serviceType, and status.

The list returned is sorted in descending order by the date and time that the recordings were created.

Long result sets are split into [pages](/docs/basics#pagination).

* If `meetingId` is specified, only recordings associated with the specified meeting will be listed. Please note that when `meetingId` is specified, parameters of `siteUrl`, `from`, and `to` will be ignored.

* If `siteUrl` is specified, all the recordings on the specified site are listed; otherwise, all the recordings on the admin user's or compliance officer's preferred site are listed. All the available Webex sites and the admin user's or compliance officer's preferred site can be retrieved by the [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.

#### Request Header

* `timezone`: *[Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default is UTC if `timezone` is not defined.*

## Parámetros
- `timezone` [header] (string): e.g. UTC

## Cuerpo de la petición (application/json)
- `max` (number): Maximum number of recordings to return in a single page. `max` must be equal to or greater than `1` and equal to or less than `100`. Por defecto: 10.
- `from` (string): Starting date and time (inclusive) for recordings to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `from` cannot be after `to`.
- `to` (string): Ending date and time (exclusive) for query recordings to return, in any [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. `to` cannot be before `from`.
- `meetingId` (string): Unique identifier for the parent meeting series, scheduled meeting, or meeting instance for which recordings are being requested. If a meeting series ID is specified, the operation returns an array of recordings for the specified meeting series. If a scheduled meeting ID is specified, the operation returns an array of recordings for the specified scheduled meeting. If a meeting instance ID is specified, the operation returns an array of recordings for the specified meeting instance. If not specified, the operation returns an array of recordings for all the current user's meetings. When `meetingId` is specified, the `siteUrl` parameter is ignored.
- `siteUrl` (string): URL of the Webex site which the API lists recordings from. If not specified, the API lists recordings from user's preferred site. All available Webex sites and preferred site of the user can be retrieved by [Get Site List](/docs/api/v1/meeting-preferences/get-site-list) API.
- `integrationTag` (string): External key of the parent meeting created by an integration application. This parameter is used by the integration application to query recordings by a key in its own domain such as a Zendesk ticket ID, a Jira ID, a Salesforce Opportunity ID, etc. An integrationTag created by one client cannot be accessed or used as a filtering parameter by another client. For example, if a meeting has an `integrationTag` of "Sales" which is created by the client behind the developer portal, then this integrationTag can't be accessed on the meeting or its recordings by another client. Neither can it be used to filter meetings or recordings by a client other than the one that created the integrationTag of "Sales".
- `topic` (string): Recording topic. If specified, the API filters recordings by topic in a case-insensitive manner.
- `format` (string): Recording's file format. If specified, the API filters recordings by format. Valores: MP4, ARF.
- `serviceType` (string): The service type for recordings. If specified, the API filters recordings by service type. Valores: MeetingCenter, EventCenter, SupportCenter, TrainingCenter.
- `status` (string):  Valores: available, deleted, purged. Por defecto: available.
- `timezone` (string): Optional timezone override for the request (if not provided, UTC is used).

### Ejemplo — petición
```json
{
  "max": 10,
  "from": "2020-07-12T09:30:00+08:00",
  "to": "2020-07-31T09:30:00+08:00",
  "meetingId": "f91b6edce9864428af084977b7c68291_I_166641849979635652",
  "siteUrl": "site4-example.webex.com",
  "integrationTag": "dbaeceebea5c4a63ac9d5ef1edfe36b9",
  "topic": "John's Meeting",
  "format": "ARF",
  "serviceType": "MeetingCenter",
  "status": "available"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/admin/recordings/query' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
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
  - `hostDisplayName` (string) (**requerido**): Display name for the meeting host.
  - `hostEmail` (string) (**requerido**): Email address for the meeting host.
  - `siteUrl` (string) (**requerido**): Site URL for the recording.
  - `downloadUrl` (string) (**requerido**): The download link for recording. This attribute is not available if **Prevent downloading** has been turned on for the recording being requested. The **Prevent downloading** option can be viewed and set by a site admin on [Control Hub](https://help.webex.com/en-us/article/sxdj4ab/Manage-Security-for-a-Cisco-Webex-Site-in-Cisco-Webex-Control-Hub).
  - `playbackUrl` (string) (**requerido**): The playback link for recording.
  - `format` (string) (**requerido**): * `MP4` - Recording file format is MP4.  * `ARF` - Recording file format is ARF, a proprietary Webex recording format.  * `UPLOADED` - The recording file is uploaded manually. Valores: MP4, ARF, UPLOADED.
  - `serviceType` (string) (**requerido**): The service type for the recording.  * `MeetingCenter` - The service type for the recording is meeting.  * `EventCenter` - The service type for the recording is the event.  * `TrainingCenter` - The service type for the recording is the training session.  * `SupportCenter` - The service type for the recording is the support meeting. Valores: MeetingCenter, EventCenter, TrainingCenter, SupportCenter.
  - `durationSeconds` (number) (**requerido**): The duration of the recording, in seconds.
  - `sizeBytes` (number) (**requerido**): The size of the recording file, in bytes.
  - `integrationTags` (array): External keys of the parent meeting created by an integration application. They could be Zendesk ticket IDs, Jira IDs, Salesforce Opportunity IDs, etc. The integration application queries recordings by a key in its own domain.
  - `status` (string) (**requerido**): * `available` - Recording is available.  * `deleted` - Recording has been moved into recycle bin.  * `purged` - Recording has been purged from the recycle bin. Please note that only a compliance officer can access recordings with a `purged` status. Valores: available, deleted, purged.

### Ejemplo — respuesta 200
```json
{
  "items": [
    {
      "id": "4f914b1dfe3c4d11a61730f18c0f5387",
      "meetingId": "f91b6edce9864428af084977b7c68291_I_166641849979635652",
      "scheduledMeetingId": "f91b6edce9864428af084977b7c68291_20200713T121500Z",
      "meetingSeriesId": "f91b6edce9864428af084977b7c68291",
      "topic": "John's Meeting",
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
The Webex Admin APIs provide comprehensive programmatic access to administrative functions for managing Webex organizations, users, licenses, and settings. These APIs enable automation of user provisioning, license assignment, compliance management, and audit event retrieval. Administrators can integrate with enterprise identity systems, enforce security policies, monitor usage, and streamline onboarding/offboarding processes. The APIs support granular control over organizational resources, making them ideal for large-scale deployments and custom admin tooling.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs