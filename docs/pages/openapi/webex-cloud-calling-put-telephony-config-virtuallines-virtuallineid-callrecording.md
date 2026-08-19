---
doc_id: webex-cloud-calling-put-telephony-config-virtuallines-virtuallineid-callrecording
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/virtualLines/{virtualLineId}/callRecording
operation_id: Configure Call Recording Settings for a Virtual Line
tags: Virtual Line Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.173854+00:00
---

# PUT /telephony/config/virtualLines/{virtualLineId}/callRecording

**API:** Webex Cloud Calling
**Área:** Virtual Line Call Settings
**operationId:** `Configure Call Recording Settings for a Virtual Line`

## Resumen
Configure Call Recording Settings for a Virtual Line

## Descripción
Configure virtual line's Call Recording settings.

The Call Recording feature provides a hosted mechanism to record the calls placed and received on the Carrier platform for replay and archival. This feature is helpful for quality assurance, security, training, and more.

This API requires a full, user, or location administrator auth token with the `spark-admin:telephony_config_write` scope.

## Parámetros
- `virtualLineId` [path] (string) (**requerido**): Unique identifier for the virtual line.
- `orgId` [query] (string): ID of the organization in which the virtual profile resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Cuerpo de la petición (application/json)
- `enabled` (boolean): `true` if call recording is enabled.
- `record` (string): Call recording scenario.  * `Always` - Incoming and outgoing calls will be recorded with no control to start, stop, pause, or resume.  * `Never` - Calls will not be recorded.  * `Always with Pause/Resume` - Calls are always recorded, but user can pause or resume the recording. Stop recording is not supported.  * `On Demand with User Initiated Start` - Records only the portion of the call after the recording start (`*44`) has been entered. Pause, resume, and stop controls are supported. Valores: Always, Never, Always with Pause/Resume, On Demand with User Initiated Start.
- `recordVoicemailEnabled` (boolean): When `true`, voicemail messages are also recorded.
- `notification` (object): Pause/resume notification settings.
  - `type` (string): Type of pause/resume notification. If `enabled` is `true` and `type` is not provided then `type` is set to `Beep` by default.  * `Beep` - A beep sound is played when call recording is paused or resumed.  * `Play Announcement` - A verbal announcement is played when call recording is paused or resumed. Valores: Beep, Play Announcement.
  - `enabled` (boolean): `true` when notification feature is in effect. `false` indicates notification is disabled.
- `repeat` (object): Beep sound plays periodically.
  - `interval` (number): Interval at which warning tone "beep" will be played. This interval is an integer from 10 to 1800 seconds
  - `enabled` (boolean): `true` when ongoing call recording tone will be played at the designated interval. `false` indicates no warning tone will be played.
- `startStopAnnouncement` (object): Call Recording starts and stops announcement settings.
  - `internalCallsEnabled` (boolean): When `true`, an announcement is played when call recording starts and an announcement is played when call recording ends for internal calls.
  - `pstnCallsEnabled` (boolean): When `true`, an announcement is played when call recording starts and an announcement is played when call recording ends for PSTN calls.
- `selectiveCallRecordingSettings` (object): Settings for selective call recording based on call direction and type. These settings only apply when `record` is set to `Always` or `Always with Pause/Resume`.
  - `recordInboundInternalCallsEnabled` (boolean): When `true`, inbound internal calls are recorded.
  - `recordInboundExternalCallsEnabled` (boolean): When `true`, inbound external calls are recorded.
  - `recordOutboundInternalCallsEnabled` (boolean): When `true`, outbound internal calls are recorded.
  - `recordOutboundExternalCallsEnabled` (boolean): When `true`, outbound external calls are recorded.

### Ejemplo — petición
```json
{
  "enabled": true,
  "record": "Never",
  "selectiveCallRecordingSettings": {
    "recordInboundInternalCallsEnabled": true,
    "recordInboundExternalCallsEnabled": true,
    "recordOutboundInternalCallsEnabled": true,
    "recordOutboundExternalCallsEnabled": true
  },
  "notification": {
    "enabled": true,
    "type": "Play Announcement"
  },
  "recordVoicemailEnabled": true,
  "repeat": {
    "enabled": true
  },
  "startStopAnnouncement": {
    "internalCallsEnabled": true,
    "pstnCallsEnabled": true
  }
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/virtualLines/<virtualLineId>/callRecording' \
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