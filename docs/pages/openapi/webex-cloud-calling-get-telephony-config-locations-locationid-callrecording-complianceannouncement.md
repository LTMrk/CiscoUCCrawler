---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-callrecording-complianceannouncement
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/callRecording/complianceAnnouncement
operation_id: getDetailsOfCallRecordingComplianceAnnouncementForTheLocation
tags: Features: Call Recording
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.273078+00:00
---

# GET /telephony/config/locations/{locationId}/callRecording/complianceAnnouncement

**API:** Webex Cloud Calling
**Área:** Features: Call Recording
**operationId:** `getDetailsOfCallRecordingComplianceAnnouncementForTheLocation`

## Resumen
Get Details of Call Recording Compliance Announcement for the Location

## Descripción
Retrieve the location compliance announcement settings.

The Compliance Announcement feature interacts with the Call Recording feature, specifically with the playback of the start/stop announcement. When the compliance announcement is played to the PSTN party, and the PSTN party is connected to a party with call recording enabled, then the start/stop announcement is inhibited.

Retrieving location compliance announcement setting requires a full, read-only, or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve compliance announcement settings for this location.
- `orgId` [query] (string): Retrieve compliance announcement setting from this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/callRecording/complianceAnnouncement' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `inboundPSTNCallsEnabled` (boolean) (**requerido**): Flag to indicate whether the call recording START/STOP announcement is played to an inbound caller.
- `useOrgSettingsEnabled` (boolean) (**requerido**): Flag to indicate whether to use the customer level compliance announcement default settings.
- `outboundPSTNCallsEnabled` (boolean) (**requerido**): Flag to indicate whether the call recording START/STOP announcement is played to an outbound caller.
- `outboundPSTNCallsDelayEnabled` (boolean) (**requerido**): Flag to indicate whether compliance announcement is played after a specified delay in seconds.
- `delayInSeconds` (number) (**requerido**): Number of seconds to wait before playing the compliance announcement.
- `useOrgLevelAnnouncementEnabled` (boolean) (**requerido**): Flag to indicate whether to use the organization level custom compliance announcement. If this flag is set to true, takes the organization's announcement setting. If this flag is set to false, takes the location's custom announcement.
- `customComplianceAnnouncement` (object) (**requerido**): Custom compliance announcement settings.
  - `type` (string): Type of compliance announcement to be played. Type is an enum with supported values CUSTOM | DEFAULT. CUSTOM is used to play a custom announcement file. DEFAULT is used to play the default system announcement file. Valores: CUSTOM, DEFAULT.
  - `audioAnnouncementFile` (object):
    - `id` (string): Unique identifier for the custom audio announcement file.
    - `fileName` (string): The original file name of the uploaded custom audio announcement.
    - `mediaFileType` (string): Type of the announcement file. Type is an enum with supported values WAV Valores: WAV.
    - `level` (string): Announcement audio file level. Valores: ORGANIZATION, LOCATION.
    - `isTextToSpeech` (boolean): Indicates if the announcement is created by TTS.

### Ejemplo — respuesta 200
```json
{
  "inboundPSTNCallsEnabled": true,
  "useOrgSettingsEnabled": true,
  "outboundPSTNCallsEnabled": false,
  "outboundPSTNCallsDelayEnabled": false,
  "delayInSeconds": 10,
  "useOrgLevelAnnouncementEnabled": false,
  "customComplianceAnnouncement": {
    "type": "CUSTOM",
    "audioAnnouncementFile": {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC82YTcwZWQ4MS1hZGM5LTQ4OWEtODhjOC0zMWI3ODllODQ1ODU",
      "fileName": "SampleAnnouncement",
      "mediaFileType": "WAV",
      "level": "ORGANIZATION",
      "isTextToSpeech": true
    }
  }
}
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