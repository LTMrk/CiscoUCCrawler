---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-callrecording-announcements
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/callRecording/announcements
operation_id: getLocationCallRecordingAnnouncementSettings
tags: Features: Call Recording
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.487312+00:00
---

# GET /telephony/config/locations/{locationId}/callRecording/announcements

**API:** Webex Cloud Calling
**Área:** Features: Call Recording
**operationId:** `getLocationCallRecordingAnnouncementSettings`

## Resumen
Get Location Call Recording Announcement Settings

## Descripción
Retrieve the location call recording announcements setting.

The Compliance Announcement feature interacts with the Call Recording feature, specifically with the playback of the start/stop announcement. When the compliance announcement is played to the PSTN party, and the PSTN party is connected to a party with call recording enabled, then the start/stop announcement is inhibited.

Retrieving location compliance announcement setting requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve compliance announcement settings for this location.
- `orgId` [query] (string): Retrieve compliance announcement setting from this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/callRecording/announcements' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `useOrgLevelAnnouncementEnabled` (boolean) (**requerido**): Flag to indicate whether to use the organization level call recording announcement settings. If the flag is set to true, indicates that the callRecordingAnnouncementSelection setting is inherited from the organization-level configuration. If the flag is set to false, indicates that the callRecordingAnnouncementSelection setting is customized at the location level.
- `start` (object) (**requerido**): The start announcement settings for this location.
  - `type` (string): Type of announcement file to be played.  * `CUSTOM` - Custom announcement file.  * `DEFAULT` - Default announcement file. Valores: CUSTOM, DEFAULT.
  - `audioAnnouncementFile` (object): The custom audio announcement file to be played.
    - `id` (string): Unique identifier for the custom audio announcement file.
    - `fileName` (string): The original file name of the uploaded custom audio announcement.
    - `mediaFileType` (string): Type of the announcement file. Type is an enum with supported values WAV Valores: WAV.
    - `level` (string): Announcement audio file level. Valores: ORGANIZATION, LOCATION.
    - `isTextToSpeech` (boolean): Indicates if the announcement is created by TTS.
- `stop` (object) (**requerido**): The stop announcement settings for this location.
  - `type` (string): Type of announcement file to be played.  * `CUSTOM` - Custom announcement file.  * `DEFAULT` - Default announcement file. Valores: CUSTOM, DEFAULT.
  - `audioAnnouncementFile` (object): The custom audio announcement file to be played.
    - `id` (string): Unique identifier for the custom audio announcement file.
    - `fileName` (string): The original file name of the uploaded custom audio announcement.
    - `mediaFileType` (string): Type of the announcement file. Type is an enum with supported values WAV Valores: WAV.
    - `level` (string): Announcement audio file level. Valores: ORGANIZATION, LOCATION.
    - `isTextToSpeech` (boolean): Indicates if the announcement is created by TTS.
- `pause` (object) (**requerido**): The pause announcement settings for this location.
  - `type` (string): Type of announcement file to be played.  * `CUSTOM` - Custom announcement file.  * `DEFAULT` - Default announcement file. Valores: CUSTOM, DEFAULT.
  - `audioAnnouncementFile` (object): The custom audio announcement file to be played.
    - `id` (string): Unique identifier for the custom audio announcement file.
    - `fileName` (string): The original file name of the uploaded custom audio announcement.
    - `mediaFileType` (string): Type of the announcement file. Type is an enum with supported values WAV Valores: WAV.
    - `level` (string): Announcement audio file level. Valores: ORGANIZATION, LOCATION.
    - `isTextToSpeech` (boolean): Indicates if the announcement is created by TTS.
- `resume` (object) (**requerido**): The resume announcement settings for this location.
  - `type` (string): Type of announcement file to be played.  * `CUSTOM` - Custom announcement file.  * `DEFAULT` - Default announcement file. Valores: CUSTOM, DEFAULT.
  - `audioAnnouncementFile` (object): The custom audio announcement file to be played.
    - `id` (string): Unique identifier for the custom audio announcement file.
    - `fileName` (string): The original file name of the uploaded custom audio announcement.
    - `mediaFileType` (string): Type of the announcement file. Type is an enum with supported values WAV Valores: WAV.
    - `level` (string): Announcement audio file level. Valores: ORGANIZATION, LOCATION.
    - `isTextToSpeech` (boolean): Indicates if the announcement is created by TTS.
- `failureProceedWithCall` (object) (**requerido**): The failure proceed with call announcement settings for this location.
  - `type` (string): Type of announcement file to be played.  * `CUSTOM` - Custom announcement file.  * `DEFAULT` - Default announcement file. Valores: CUSTOM, DEFAULT.
  - `audioAnnouncementFile` (object): The custom audio announcement file to be played.
    - `id` (string): Unique identifier for the custom audio announcement file.
    - `fileName` (string): The original file name of the uploaded custom audio announcement.
    - `mediaFileType` (string): Type of the announcement file. Type is an enum with supported values WAV Valores: WAV.
    - `level` (string): Announcement audio file level. Valores: ORGANIZATION, LOCATION.
    - `isTextToSpeech` (boolean): Indicates if the announcement is created by TTS.
- `failureEndWithCall` (object) (**requerido**): The failure end with call announcement settings for this location.
  - `type` (string): Type of announcement file to be played.  * `CUSTOM` - Custom announcement file.  * `DEFAULT` - Default announcement file. Valores: CUSTOM, DEFAULT.
  - `audioAnnouncementFile` (object): The custom audio announcement file to be played.
    - `id` (string): Unique identifier for the custom audio announcement file.
    - `fileName` (string): The original file name of the uploaded custom audio announcement.
    - `mediaFileType` (string): Type of the announcement file. Type is an enum with supported values WAV Valores: WAV.
    - `level` (string): Announcement audio file level. Valores: ORGANIZATION, LOCATION.
    - `isTextToSpeech` (boolean): Indicates if the announcement is created by TTS.

### Ejemplo — respuesta 200
```json
{
  "useOrgLevelAnnouncementEnabled": false,
  "start": {
    "type": "CUSTOM",
    "audioAnnouncementFile": {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC9iOTg2MWI3MS1hN2MxLTQxZmUtYjNmZC1lZDNkOTdjYTFjMzQ=",
      "fileName": "SampleAnnouncement",
      "mediaFileType": "WAV",
      "level": "ORGANIZATION",
      "isTextToSpeech": true
    }
  },
  "stop": {
    "type": "CUSTOM",
    "audioAnnouncementFile": {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC82ZjU0Y2NhNS05ZWY5LTQ3N2EtYThkNi0wY2EyNzU4MTAxM2Y=",
      "fileName": "SampleAnnouncement",
      "mediaFileType": "WAV",
      "level": "ORGANIZATION",
      "isTextToSpeech": true
    }
  },
  "pause": {
    "type": "CUSTOM",
    "audioAnnouncementFile": {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC82M2NiYTMwOS05NjQ2LTQzMjUtOTZlNC02N2ZmYWVlZjNiOWI=",
      "fileName": "SampleAnnouncement",
      "mediaFileType": "WAV",
      "level": "ORGANIZATION",
      "isTextToSpeech": true
    }
  },
  "resume": {
    "type": "CUSTOM",
    "audioAnnouncementFile": {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC8xM2NlNzBkYS00NDkwLTQ2OWItOTg4YS1mYjA0MzExNmQ3ZTU=",
      "fileName": "SampleAnnouncement",
      "mediaFileType": "WAV",
      "level": "ORGANIZATION",
      "isTextToSpeech": true
    }
  },
  "failureEndWithCall": {
    "type": "CUSTOM",
    "audioAnnouncementFile": {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC9mZTU4YTE1ZS1kNzMwLTQ4ZGYtYWU4Ny1jNjc5YjM3YmQ4Mzk=",
      "fileName": "SampleAnn
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