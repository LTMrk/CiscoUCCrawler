---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-callrecording
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/people/me/settings/callRecording
operation_id: getMyCallRecordingSettings
tags: Call Settings For Me
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.145954+00:00
---

# GET /telephony/config/people/me/settings/callRecording

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getMyCallRecordingSettings`

## Resumen
Get My Call Recording Settings

## Descripción
Get details of call recording settings associated with the authenticated user.

Call recording settings allow you to access and customize options that determine when and how your calls are recorded, providing control over recording modes and notifications.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/me/settings/callRecording' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `enabled` (boolean) (**requerido**): Indicates whether Call Recording is enabled for the user or not.
- `vendor` (object) (**requerido**): List of available vendors and their details.
  - `id` (string) (**requerido**): Unique identifier of a vendor.
  - `name` (string) (**requerido**): Name of a call recording vendor.
  - `loginUrl` (string) (**requerido**): Login URL of the vendor.
- `recordingMode` (string) (**requerido**): * `Always` - Call recording is always enabled.  * `Never` - Call recording is never enabled.  * `On Demand` - Call recording is started and stopped manually by the user.  * `Always with Pause/Resume` - Call recording is always enabled with the ability to pause and resume.  * `On Demand with User Initiated Start` - Call recording is started manually by the user. Valores: Always, Never, On Demand, Always with Pause/Resume, On Demand with User Initiated Start.
- `pauseResumeNotifyMethod` (string): * `Beep` - A beep is played when call recording is paused or resumed.  * `Play Announcement` - An announcement is played when call recording is paused or resumed. Valores: Beep, Play Announcement.
- `announcementEnabled` (boolean): If `true`, an announcement is played when call recording starts.
- `warningToneEnabled` (boolean): If `true`, a warning tone is played when call recording starts.
- `warningToneDuration` (number): Duration of the warning tone in seconds. Duration can be configured between 10 and 1800 seconds.
- `selectiveCallRecordingSettings` (object): Selective call recording settings. Applicable when `recordingMode` is set to either `Always` or `Always with Pause/Resume`.
  - `recordInboundInternalCallsEnabled` (boolean) (**requerido**): If `true`, inbound internal calls are recorded.
  - `recordInboundExternalCallsEnabled` (boolean) (**requerido**): If `true`, inbound external calls are recorded.
  - `recordOutboundInternalCallsEnabled` (boolean) (**requerido**): If `true`, outbound internal calls are recorded.
  - `recordOutboundExternalCallsEnabled` (boolean) (**requerido**): If `true`, outbound external calls are recorded.

### Ejemplo — respuesta 200
```json
{
  "enabled": true,
  "vendor": {
    "id": "Y2lzY29zcGFyazovL3VzL1JFQ09SRElOR19WRU5ET1IvZmVjYjYzNGUtYzMyZS00ZWJmLThlYzMtMmVhYjk3Y2IyNjNk",
    "name": "ITFDual",
    "loginUrl": "https://www.itfdualportal.com"
  },
  "recordingMode": "Always",
  "pauseResumeNotifyMethod": "Beep",
  "announcementEnabled": true,
  "warningToneEnabled": false,
  "warningToneDuration": 70,
  "selectiveCallRecordingSettings": {
    "recordInboundInternalCallsEnabled": true,
    "recordInboundExternalCallsEnabled": true,
    "recordOutboundInternalCallsEnabled": false,
    "recordOutboundExternalCallsEnabled": true
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