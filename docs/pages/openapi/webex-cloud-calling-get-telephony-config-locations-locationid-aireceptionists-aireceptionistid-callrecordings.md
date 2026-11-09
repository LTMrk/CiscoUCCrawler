---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-aireceptionists-aireceptionistid-callrecordings
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/aiReceptionists/{aiReceptionistId}/callRecordings
operation_id: getCallRecordingSettingsForAnAIReceptionist
tags: AI Receptionist for Webex Calling, AI Receptionist
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-09T12:44:27.946495+00:00
---

# GET /telephony/config/locations/{locationId}/aiReceptionists/{aiReceptionistId}/callRecordings

**API:** Webex Cloud Calling
**Área:** AI Receptionist for Webex Calling, AI Receptionist
**operationId:** `getCallRecordingSettingsForAnAIReceptionist`

## Resumen
Get Call Recording Settings for an AI Receptionist

## Descripción
Retrieve Call Recording settings for an AI Receptionist.

The Call Recording feature provides a hosted mechanism to record the calls placed and received on the Carrier platform for replay and archival. This feature is helpful for quality assurance, security, training, and more.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location in which the AI Receptionist exists.
- `aiReceptionistId` [path] (string) (**requerido**): Retrieve Call Recording settings for this AI Receptionist.
- `orgId` [query] (string): Retrieve Call Recording settings for an AI Receptionist in this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/aiReceptionists/<aiReceptionistId>/callRecordings' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `enabled` (boolean) (**requerido**): `true` if call recording is enabled for the AI Receptionist.
- `startAnnouncement` (object) (**requerido**): Call Recording start announcement settings.
  - `internalCallsEnabled` (boolean) (**requerido**): When `true`, an announcement is played when call recording starts for internal calls.
  - `pstnCallsEnabled` (boolean) (**requerido**): When `true`, an announcement is played when call recording starts for PSTN calls.
- `repeat` (object) (**requerido**): Beep sound plays periodically during recording.
  - `enabled` (boolean) (**requerido**): `true` when ongoing call recording tone will be played at the designated interval.
  - `interval` (integer) (**requerido**): Interval at which warning tone "beep" will be played. This interval is an integer from 10 to 80 seconds in increments of 10.
- `postCallRecordingSettings` (object) (**requerido**): Post call recording settings for AI-powered features.
  - `transcriptEnabled` (boolean) (**requerido**): When `true`, call transcription is enabled.
  - `summaryAndActionItemsEnabled` (boolean) (**requerido**): When `true`, AI-generated summary and action items are enabled.
- `serviceProvider` (string) (**requerido**): Service provider identifier used for the third-party recording integration.
- `externalGroup` (string) (**requerido**): Group utilized by the service provider providing call recording service.
- `externalIdentifier` (string) (**requerido**): Unique identifier utilized by the service provider providing call recording service.

### Ejemplo — respuesta 200
```json
{
  "enabled": true,
  "startAnnouncement": {
    "internalCallsEnabled": true,
    "pstnCallsEnabled": true
  },
  "repeat": {
    "enabled": true,
    "interval": 20
  },
  "postCallRecordingSettings": {
    "transcriptEnabled": true,
    "summaryAndActionItemsEnabled": false
  },
  "serviceProvider": "WSWYZ25455",
  "externalGroup": "WSWYZ25455L31161",
  "externalIdentifier": "a34iidrh5o@64941297.int10.bcld.webex.com"
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