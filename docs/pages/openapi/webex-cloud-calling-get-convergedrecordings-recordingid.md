---
doc_id: webex-cloud-calling-get-convergedrecordings-recordingid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /convergedRecordings/{recordingId}
operation_id: get_recording_details
tags: Converged Recordings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.179252+00:00
---

# GET /convergedRecordings/{recordingId}

**API:** Webex Cloud Calling
**Área:** Converged Recordings
**operationId:** `get_recording_details`

## Resumen
Get Recording Details

## Descripción
Retrieves details for a recording with a specified recording ID.

Only recordings of owner with the authenticated user may be retrieved.

Get Recording Details requires the `spark-compliance:recordings_read` scope for compliance officer, `spark-admin:recordings_read` scope for admin and `spark:recordings_read` scope for user.

#### Request Header

* `timezone`: *[Time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) in conformance with the [IANA time zone database](https://www.iana.org/time-zones). The default is UTC if `timezone` is not defined.*

## Parámetros
- `recordingId` [path] (string) (**requerido**): A unique identifier for the recording.
- `timezone` [header] (string): e.g. UTC

## Ejemplo de invocación
```bash
curl -X GET '/convergedRecordings/<recordingId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): A unique identifier for recording.
- `topic` (string) (**requerido**): The recording's topic.
- `createTime` (string) (**requerido**): The date and time recording was created in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. Please note that it's not the time the record button was clicked in meeting but the time the recording file was generated offline.
- `timeRecorded` (string) (**requerido**): The date and time recording started in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format. It indicates when the record button was clicked in the meeting.
- `format` (string) (**requerido**): * `MP3` - Recording file format is MP3. Valores: MP3.
- `serviceType` (string) (**requerido**): * `calling` - Recording service-type is calling.  * `customerAssist` - Call Recordings of a Customer Assist Queue. Valores: calling, customerAssist.
- `durationSeconds` (number) (**requerido**): The duration of the recording in seconds.
- `sizeBytes` (number) (**requerido**): The size of the recording file in bytes.
- `temporaryDirectDownloadLinks` (object): The download links for the MP3 audio of the recordings without rendering an HTML page in a browser or an HTTP redirect. This attribute is available only for authorized users or a [Compliance Officer](/docs/compliance#compliance). This attribute is not available if the user is an admin with scope `spark-admin:recordings_read` or if **Prevent Downloading** has been turned on for the recording being requested.
  - `audioDownloadLink` (string): The download link for recording audio file without HTML page rendering in browser or HTTP redirect.  Expires 3 hours after the API request.
  - `transcriptDownloadLink` (string): The download link for recording transcript file without HTML page rendering in browser or HTTP redirect.  Expires 3 hours after the API request.
  - `suggestedNotesDownloadLink` (string): The download API for recording notes. The user access token is required to download the recording notes. Expires 3 hours after the API request.
  - `shortNotesDownloadLink` (string): The download API for recording short notes. The user access token is required to download the recording short notes. Expires 3 hours after the API request.
  - `actionItemsDownloadLink` (string): The download API for recording action items. The user access token is required to download the recording action items. Expires 3 hours after the API request.
  - `expiration` (string): The date and time when `recordingDownloadLink`, `audioDownloadLink`, `transcriptDownloadLink`, `suggestedNotesDownloadLink`, `shortNotesDownloadLink` and `actionItemsDownloadLink` expire in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) compliant format.
- `status` (string) (**requerido**): * `available` - Recording is available.  * `deleted` - Recording has been moved to the recycle bin.  * `purged` - Recording has been purged from the recycle bin. Please note that only a compliance officer can access recordings with a `purged` status. Valores: available, deleted, purged.
- `ownerId` (string) (**requerido**): Webex UUID for recording owner/host.
- `ownerEmail` (string) (**requerido**): Webex email for recording owner/host.
- `ownerType` (string) (**requerido**): * `user` - Recording belongs to a user.  * `place` - Recording belongs to a workspace device.  * `virtualLine` - Recording belongs to a workspace device. Valores: user, place, virtualLine, callQueue.
- `storageRegion` (string) (**requerido**): Storage location for recording within Webex datacenters.
- `serviceData` (object): Fields relevant to each service Type.
  - `locationId` (string): Webex calling location for recording user.
  - `callSessionId` (string): Call ID for which recording was done.

### Ejemplo — respuesta 200
```json
{
  "id": "62807eaf-0c89-492e-a3c3-c4751812603b",
  "topic": "call with default",
  "createTime": "2023-11-01T23:09:05+08:00",
  "timeRecorded": "2023-11-01T15:27:29+08:00",
  "temporaryDirectDownloadLinks": {
    "audioDownloadLink": "https://nsq1wss.dmz.webex.com/nbr/MultiThreadDownloadServlet?type=calling&orgId=59e67527-4651-4c90-b2f0-4f86c3bb6608&recordUUID=62807eaf-0c89-492e-a3c3-c4751812603b&ticket=SDJTSwAAAIV9%2BooFzh%2FkPd1Edek7wtCLYrVcjsJ2RTHGbhwYHpWOEQ%3D%3D&timestamp=1699495025258",
    "suggestedNotesDownloadLink": "https://aibridge-sa1.dmz.webex.com/wbxaibridge/api/v2/notes/e823b9ee-4c4d-4e91-9379-502a9c8c9e6d?contentType=html&resourceType=CallingRecording&resourceId=e31feef9-38bf-456b-898b-be59d310a490&token=QUhTSwAAAIU2M4Tf2_V07LJZ9K5v3S4stc0ETlKC2vkbmDtqQ89fkTw_GfhGHqnMY4U-T8wfjdHsOmAER_fa2AJrAQ6ZLs3u8IiqJxhb26YY9jXTj1QZ-ITGrC4OJACXqxgxFx43o3XTQ_ORJm2_x7A4SBhrWKYFJFIy9TcT6vOE8c45lAvteEsRcfSP49dJ5y7klaWUI1s1",
    "actionItemsDownloadLink": "https://aibridge-sa1.dmz.webex.com/wbxaibridge/api/v2/actionItems/0715435b-c6f9-49f5-be66-e3cbd9f65c0d?contentType=html&resourceType=CallingRecording&resourceId=e31feef9-38bf-456b-898b-be59d310a490&token=QUhTSwAAAIU2M4Tf2_V07LJZ9K5v3S4stc0ETlKC2vkbmDtqQ89fkTw_GfhGHqnMY4U-T8wfjdHsOmAER_fa2AJrAQ6ZLs3u8IiqJxhb26YY9jXTj1QZ-ITGrC4OJACXqxgxFx43o3XTQ_ORJm2_x7A4SBhrWKYFJFIy9TcT6vOE8c45lAvteEsRcfSP49dJ5y7klaWUI1s1",
    "shortNotesDownloadLink": "https://aibridge-sa1.dmz.webex.com/wbxaibridge/api/v2/shortNotes/e823b9ee-4c4d-4e91-937
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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs