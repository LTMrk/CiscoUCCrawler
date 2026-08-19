---
doc_id: webex-cloud-calling-get-convergedrecordings-recordingid-metadata
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /convergedRecordings/{recordingId}/metadata
operation_id: get_recording_metadata
tags: Converged Recordings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.988890+00:00
---

# GET /convergedRecordings/{recordingId}/metadata

**API:** Webex Cloud Calling
**Área:** Converged Recordings
**operationId:** `get_recording_metadata`

## Resumen
Get Recording metadata

## Descripción
Retrieves metadata details for a recording with a specified recording ID. The recording must be owned by the authenticated user.

For information on the metadata fields, refer to [Metadata Guide](https://developer.webex.com/docs/api/guides/consolidated-metadata-documentation-and-samples-guide)

Get Recording metadata requires the `spark-compliance:recordings_read` scope for compliance officer, `spark-admin:recordings_read` for admin and `spark:recordings_read` for user.

## Parámetros
- `recordingId` [path] (string) (**requerido**): A unique identifier for the recording.
- `showAllTypes` [query] (boolean): If `showAllTypes` is `true`, all attributes will be shown. If it's `false` or not specified, the following attributes of the metadata will be hidden.                                           serviceData.callActivity.mediaStreams                                           serviceData.callActivity.participants                                           serviceData.callActivity.redirectInfo                                           serviceData.callActivity.redirectedCall Por defecto: False.

## Ejemplo de invocación
```bash
curl -X GET '/convergedRecordings/<recordingId>/metadata' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string):
- `orgId` (string):
- `ownerId` (string):
- `ownerType` (string):
- `ownerName` (string):
- `ownerEmail` (string):
- `storageRegion` (string):
- `serviceType` (string):
- `version` (string):
- `serviceData` (object):
  - `callRecordingId` (string):
  - `locationId` (string):
  - `callSessionId` (string):
  - `personality` (string):
  - `callingParty` (object):
    - `actor` (object):
      - `type` (string):
      - `id` (string):
    - `number` (string):
  - `calledParty` (object):
    - `actor` (object):
      - `type` (string):
      - `id` (string):
    - `number` (string):
  - `callId` (string):
  - `session` (object):
    - `startTime` (string):
    - `stopTime` (string):
  - `recordingType` (string):
  - `answererInfo` (object):
    - `actor` (object):
      - `type` (string):
      - `id` (string):
    - `number` (string):
  - `recordingActions` (array):
    - `action` (string):
    - `time` (string):
  - `callActivity` (array):
    - `timeStamp` (string):
    - `mediaStreams` (array):
      - `streamId` (string):
      - `mode` (string):
      - `mLineIndex` (string):
    - `participants` (array):
      - `actor` (object) (**requerido**):
        - `type` (string):
        - `id` (string):
      - `aor` (string) (**requerido**):
      - `send` (string) (**requerido**):
    - `announcementData` (object):
      - `announcementFilename` (string):
      - `announcementTimestamp` (string):
      - `announcementParticipants` (array):
      - `announcementType` (string):
  - `managedBy` (object):
    - `actor` (object):
      - `type` (string):
      - `id` (string):
    - `number` (string):
  - `connectedParty` (object):

### Ejemplo — respuesta 200
```json
{
  "id": "81bb582c-e93e-40aa-abf6-962b620f6db4",
  "orgId": "ee8ebeb0-f077-4384-bb50-9de6141c7bac",
  "ownerId": "************************************",
  "ownerType": "USER",
  "ownerName": "PRS TestUser1",
  "ownerEmail": "nshtestwebex+prstestuser1@gmail.com",
  "storageRegion": "US",
  "serviceType": "calling",
  "version": "1.2",
  "serviceData": {
    "callRecordingId": "81bb582c-e93e-40aa-abf6-962b620f6db4",
    "locationId": "************************************",
    "callSessionId": "fe2f5688-91a8-4799-a867-a396bb2b024a",
    "personality": "originator",
    "callingParty": {
      "actor": {
        "type": "USER",
        "id": "c2335e53-c41b-423d-a41e-da0bf56e2038"
      },
      "number": "sip:####PII-EXPOSURE####@X.X.X.X"
    },
    "calledParty": {
      "actor": {
        "type": "USER",
        "id": "ac7913cd-d943-4e34-81a8-f66ad1a5e376"
      },
      "number": "sip:4060@X.X.X.X;user=phone"
    },
    "callId": "callhalf-581329:0",
    "session": {
      "startTime": "2023-11-07T08:50:21Z",
      "stopTime": "2023-11-07T08:55:19Z"
    },
    "recordingType": "alwaysON",
    "answererInfo": {
      "actor": {
        "type": "USER",
        "id": "ac7913cd-d943-4e34-81a8-f66ad1a5e376"
      },
      "number": "sip:4060@X.X.X.X;user=phone"
    },
    "recordingActions": [
      {
        "action": "PAUSE",
        "time": "2023-11-07T08:50:23Z"
      }
    ],
    "callActivity": [
      {
        "timeStamp": "2023-11-07T08:50:25Z",
        "mediaStreams": [
  ... (truncado)
```
**204**: No Content

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