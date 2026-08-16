---
doc_id: webex-cloud-calling-get-convergedrecordings-recordingid-metadata
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /convergedRecordings/{recordingId}/metadata
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.580498+00:00
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
- `recordingId` [path] (string) **(requerido)**: A unique identifier for the recording.
- `showAllTypes` [query] (boolean): If `showAllTypes` is `true`, all attributes will be shown. If it's `false` or not specified, the following attributes of the metadata will be hidden.                                           serviceData.callActivity.mediaStreams                                           serviceData.callActivity.participants                                           serviceData.callActivity.redirectInfo                                           serviceData.callActivity.redirectedCall

## Respuestas
- **200**: OK
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
- **204**: No Content
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
