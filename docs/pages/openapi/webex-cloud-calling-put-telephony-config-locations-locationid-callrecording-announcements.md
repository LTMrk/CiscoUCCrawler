---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-callrecording-announcements
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/callRecording/announcements
operation_id: updateLocationCallRecordingAnnouncementSettings
tags: Features: Call Recording
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.313511+00:00
---

# PUT /telephony/config/locations/{locationId}/callRecording/announcements

**API:** Webex Cloud Calling
**Área:** Features: Call Recording
**operationId:** `updateLocationCallRecordingAnnouncementSettings`

## Resumen
Update Location Call Recording Announcement Settings

## Descripción
Update Location Call Recording Announcement Settings.

The Compliance Announcement feature interacts with the Call Recording feature, specifically with the playback of the start/stop announcement. When the compliance announcement is played to the PSTN party, and the PSTN party is connected to a party with call recording enabled, then the start/stop announcement is inhibited.

Updating the location compliance announcement requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Update the call recording announcements setting for this location.
- `orgId` [query] (string): Update the call recording announcements setting from this organization.

## Cuerpo de la petición (application/json)
- `useOrgLevelAnnouncementEnabled` (boolean): Flag to indicate whether to use the organization level call recording announcement settings. If the flag is set to true, indicates that the callRecordingAnnouncementSelection setting is inherited from the organization-level configuration. If the flag is set to false, indicates that the callRecordingAnnouncementSelection setting is customized at the location level.
- `start` (object): The start announcement settings for this location.
  - `type` (string): Type of announcement file to be played.  * `CUSTOM` - Custom announcement file.  * `DEFAULT` - Default announcement file. Valores: CUSTOM, DEFAULT.
  - `audioAnnouncementFileId` (string): Unique identifier for the custom audio announcement file.
- `stop` (object): The stop announcement settings for this location.
  - `type` (string): Type of announcement file to be played.  * `CUSTOM` - Custom announcement file.  * `DEFAULT` - Default announcement file. Valores: CUSTOM, DEFAULT.
  - `audioAnnouncementFileId` (string): Unique identifier for the custom audio announcement file.
- `pause` (object): The pause announcement settings for this location.
  - `type` (string): Type of announcement file to be played.  * `CUSTOM` - Custom announcement file.  * `DEFAULT` - Default announcement file. Valores: CUSTOM, DEFAULT.
  - `audioAnnouncementFileId` (string): Unique identifier for the custom audio announcement file.
- `resume` (object): The resume announcement settings for this location.
  - `type` (string): Type of announcement file to be played.  * `CUSTOM` - Custom announcement file.  * `DEFAULT` - Default announcement file. Valores: CUSTOM, DEFAULT.
  - `audioAnnouncementFileId` (string): Unique identifier for the custom audio announcement file.
- `failureEndWithCall` (object): The failure end with call announcement settings for this location.
  - `type` (string): Type of announcement file to be played.  * `CUSTOM` - Custom announcement file.  * `DEFAULT` - Default announcement file. Valores: CUSTOM, DEFAULT.
  - `audioAnnouncementFileId` (string): Unique identifier for the custom audio announcement file.
- `failureProceedWithCall` (object): The failure proceed with call announcement settings for this location.
  - `type` (string): Type of announcement file to be played.  * `CUSTOM` - Custom announcement file.  * `DEFAULT` - Default announcement file. Valores: CUSTOM, DEFAULT.
  - `audioAnnouncementFileId` (string): Unique identifier for the custom audio announcement file.

### Ejemplo — petición
```json
{
  "useOrgLevelAnnouncementEnabled": false,
  "start": {
    "type": "CUSTOM",
    "audioAnnouncementFileId": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC9iOTg2MWI3MS1hN2MxLTQxZmUtYjNmZC1lZDNkOTdjYTFjMzQ="
  },
  "stop": {
    "type": "CUSTOM",
    "audioAnnouncementFileId": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC82ZjU0Y2NhNS05ZWY5LTQ3N2EtYThkNi0wY2EyNzU4MTAxM2Y="
  },
  "pause": {
    "type": "CUSTOM",
    "audioAnnouncementFileId": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC82M2NiYTMwOS05NjQ2LTQzMjUtOTZlNC02N2ZmYWVlZjNiOWI="
  },
  "resume": {
    "type": "CUSTOM",
    "audioAnnouncementFileId": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC8xM2NlNzBkYS00NDkwLTQ2OWItOTg4YS1mYjA0MzExNmQ3ZTU="
  },
  "failureEndWithCall": {
    "type": "CUSTOM",
    "audioAnnouncementFileId": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC9mZTU4YTE1ZS1kNzMwLTQ4ZGYtYWU4Ny1jNjc5YjM3YmQ4Mzk="
  },
  "failureProceedWithCall": {
    "type": "CUSTOM",
    "audioAnnouncementFileId": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC80ZjU0Y2NhNS05ZWY5LTQ3N2EtYThkNi0wY2EyNzU4MTAxM2Y="
  }
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/callRecording/announcements' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
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