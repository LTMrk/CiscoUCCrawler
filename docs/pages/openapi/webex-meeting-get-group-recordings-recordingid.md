---
doc_id: webex-meeting-get-group-recordings-recordingid
source: webex-openapi-specs/public-spec/webex-meeting.json
api: Webex Meetings
api_version: 1.0.0
method: GET
path: /group/recordings/{recordingId}
operation_id: getGroupRecordingById
tags: Recordings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.499165+00:00
---

# GET /group/recordings/{recordingId}

**API:** Webex Meetings
**Área:** Recordings
**operationId:** `getGroupRecordingById`

## Resumen
Get Group Recording Details

## Descripción
Retrieves details for a group recording for a service app which has group recording access.

* Only recordings which are in the `available` status and not shared by others can be listed. Those in the `deleted` or `purged` status or shared by others can't be listed.

* One of the `personId` parameter and `hostEmail` header must be specified so that only recordings of meetings hosted by the person of `personId` or `hostEmail` will be returned.

#### Request Header

* `timezone`: *[Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default is UTC if `timezone` is not defined.*

* `hostEmail`: Email of the user whose recordings will be retrieved. The `hostEmail` parameter is optional, but one of the `personId` parameter and `hostEmail` header must be specified.

## Parámetros
- `personId` [query] (string): Person ID of the user whose recordings will be retrieved. The person ID can be retrieved from the [People APIs](/docs/api/v1/people), e.g. [Lit People](/docs/api/v1/people/list-people). Note that a person ID retrieved from the People APIs is a Base64-encoded string, e.g. `Y2lzY29zcGFyazovL3VzL1BFT1BMRS9kNDdiMmU3ZC01ZTBmLTRmNjktYWVmNC1lNGZmOTBhZWE3Yzk`. The person ID in the raw UUID format which is the last part of the Base64-decoded string, e.g. `d47b2e7d-5e0f-4f69-aef4-e4ff90aea7c9`, is also supported. The `personId` parameter is optional, but one of the `personId` parameter and `hostEmail` header must be specified.
- `recordingId` [path] (string) (**requerido**): A unique identifier for the recording.
- `timezone` [header] (string): e.g. UTC
- `hostEmail` [header] (string): Email of the user whose recordings will be retrieved. The `hostEmail` parameter is optional, but one of the `personId` parameter and `hostEmail` header must be specified.

## Ejemplo de invocación
```bash
curl -X GET '/group/recordings/<recordingId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): A unique identifier for recording.
- `meetingId` (string) (**requerido**): Unique identifier for the recording's ended meeting instance.
- `scheduledMeetingId` (string): Unique identifier for the recording's scheduled meeting instance.
- `meetingSeriesId` (string): Unique identifier for the recording's meeting series.
- `topic` (string) (**requerido**): The recording's topic.
- `createTime` (string) (**requerido**): The date and time recording was created in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. Please note that it's not the time the record button was clicked in meeting but the time the recording file was generated offline.
- `timeRecorded` (string) (**requerido**): The date and time recording started in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. It indicates when the record button was clicked in the meeting.
- `siteUrl` (string) (**requerido**): Site URL for the recording.
- `downloadUrl` (string) (**requerido**): The download link for the recording. This attribute is not available if `prevent downloading` has been turned on for the recording being requested. The `prevent downloading` option can be viewed and set on page when editing a recording.
- `playbackUrl` (string) (**requerido**): The playback link for recording.
- `password` (string) (**requerido**): The recording's password.
- `format` (string) (**requerido**): * `MP4` - Recording file format is MP4.  * `ARF` - Recording file format is ARF, a proprietary Webex recording format.  * `UPLOADED` - The recording file is uploaded manually. Valores: MP4, ARF, UPLOADED.
- `serviceType` (string) (**requerido**): * `MeetingCenter` - The service type for the recording is meeting.  * `EventCenter` - The service type for the recording is the event.  * `TrainingCenter` - The service type for the recording is the training session.  * `SupportCenter` - The service type for the recording is the support meeting. Valores: MeetingCenter, EventCenter, TrainingCenter, SupportCenter.
- `durationSeconds` (number) (**requerido**): The duration of the recording in seconds.
- `sizeBytes` (number) (**requerido**): The size of the recording file in bytes.
- `shareToMe` (boolean) (**requerido**): Whether or not the recording has been shared to the current user.
- `temporaryDirectDownloadLinks` (object): The download links for MP4/ARF, audio, and transcript of the recording without HTML page rendering in browser or HTTP redirect. This attribute is not available if the user is not a [Compliance Officer](/docs/compliance#compliance) and **Prevent Downloading** has been turned on for the recording being requested. The Prevent Downloading option can be viewed and set on page when editing a recording. Note that there are various products in [Webex Suite](https://www.cisco.com/c/en/us/products/conferencing/product_comparison.html) such as "Webex Meetings", "Webex Training" and "Webex Events".
  - `recordingDownloadLink` (string): The download link for recording MP4/ARF file without HTML page rendering in browser or HTTP redirect. Expires 3 hours after the API request.
  - `audioDownloadLink` (string): The download link for recording audio file without HTML page rendering in browser or HTTP redirect. This attribute is not available if **Prevent Downloading** has been turned on for the recording being requested. Expires 3 hours after the API request.
  - `transcriptDownloadLink` (string): The download link for recording transcript file without HTML page rendering in browser or HTTP redirect. This attribute is not available if **Prevent Downloading** has been turned on for the recording being requested. Expires 3 hours after the API request.
  - `expiration` (string): The date and time when `recordingDownloadLink`, `audioDownloadLink`, and `transcriptDownloadLink` expire in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
- `integrationTags` (array): External keys of the parent meeting created by an integration application. The key can be Zendesk ticket IDs, Jira IDs, Salesforce Opportunity IDs, etc. The integration application queries recordings by a key in its own domain.
- `status` (string) (**requerido**): * `available` - Recording is available.  * `deleted` - Recording has been moved to the recycle bin.  * `purged` - Recording has been purged from the recycle bin. Please note that only a compliance officer can access recordings with a `purged` status. Valores: available, deleted, purged.

### Ejemplo — respuesta 200
```json
{
  "id": "4f914b1dfe3c4d11a61730f18c0f5387",
  "meetingId": "f91b6edce9864428af084977b7c68291_I_166641849979635652",
  "scheduledMeetingId": "f91b6edce9864428af084977b7c68291_20200713T121500Z",
  "meetingSeriesId": "f91b6edce9864428af084977b7c68291",
  "topic": "Example Topic",
  "createTime": "2020-07-13T17:11:35Z",
  "timeRecorded": "2020-07-13T17:05:35Z",
  "siteUrl": "site4-example.webex.com",
  "downloadUrl": "https://site4-example.webex.com/site4/lsr.php?RCID=b91990e37417bda24986e46cf43345ab",
  "playbackUrl": "https://site4-example.webex.com/site4/ldr.php?RCID=69201a61d1d94a84aca18817261d1a73",
  "password": "********",
  "temporaryDirectDownloadLinks": {
    "recordingDownloadLink": "https://site4-example.webex.com/nbr/MultiThreadDownloadServlet?siteid=2062842&recordid=305462&confid=137735449369118342&language=en_US&userid=3516472&serviceRecordID=305492&ticket=SDJTSwAAAIUBSHkvL6Z5ddyBim5%2FHcJYcvn6IoXNEyCE2mAYQ5BlBg%3D%3D&timestamp=1567125236465&islogin=yes&isprevent=no&ispwd=yes",
    "audioDownloadLink": "https://site4-example.webex.com/nbr/downloadMedia.do?siteid=2062842&recordid=305462&confid=137735449369118342&language=en_US&userid=3516472&serviceRecordID=305492&ticket=SDJTSwAAAIXCIXsuBt%2BAgtK7WoQ2VhgeI608N4ZMIJ3vxQaQNZuLZA%3D%3D&timestamp=1567125236708&islogin=yes&isprevent=no&ispwd=yes&mediaType=1",
    "transcriptDownloadLink": "https://site4-example.webex.com/nbr/downloadMedia.do?siteid=2062842&recordid=305462&confid=137735449369118342&language=en_US&userid
  ... (truncado)
```

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