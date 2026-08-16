---
doc_id: webex-cloud-calling-get-telephony-config-people-me-settings-secondarylines-lineownerid-callrecording
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/people/me/settings/secondaryLines/{lineownerId}/callRecording
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.562149+00:00
---

# GET /telephony/config/people/me/settings/secondaryLines/{lineownerId}/callRecording

**API:** Webex Cloud Calling
**Área:** Call Settings For Me
**operationId:** `getMySecondaryLinesCallRecordingSettings`

## Resumen
Get My Secondary Line Owner's Call Recording Settings

## Descripción
Get details of call recording settings associated with a secondary line of the authenticated user.

Note that an authenticated user can only retrieve information for their configured secondary lines.

Call recording settings allow you to access and customize options that determine when and how your calls are recorded, providing control over recording modes and notifications.

This API requires a user auth token with a scope of `spark:telephony_config_read`.

## Parámetros
- `lineownerId` [path] (string) **(requerido)**: Unique identifier for the secondary line owner (applicable only for Virtual Lines).

## Respuestas
- **200**: OK
  - `enabled` (boolean) **(requerido)**: Indicates whether Call Recording is enabled for the user or not.
  - `vendor` (object) **(requerido)**: List of available vendors and their details.
    - `id` (string) **(requerido)**: Unique identifier of a vendor.
    - `name` (string) **(requerido)**: Name of a call recording vendor.
    - `loginUrl` (string) **(requerido)**: Login URL of the vendor.
  - `recordingMode` (string) **(requerido)**: * `Always` - Call recording is always enabled.  * `Never` - Call recording is never enabled.  * `On Demand` - Call recording is started and stopped manually by the user.  * `Always with Pause/Resume` - Call recording is always enabled with the ability to pause and resume.  * `On Demand with User Initiated Start` - Call recording is started manually by the user. Valores: Always, Never, On Demand, Always with Pause/Resume, On Demand with User Initiated Start.
  - `pauseResumeNotifyMethod` (string): * `Beep` - A beep is played when call recording is paused or resumed.  * `Play Announcement` - An announcement is played when call recording is paused or resumed. Valores: Beep, Play Announcement.
  - `announcementEnabled` (boolean): If `true`, an announcement is played when call recording starts.
  - `warningToneEnabled` (boolean): If `true`, a warning tone is played when call recording starts.
  - `warningToneDuration` (number): Duration of the warning tone in seconds. Duration can be configured between 10 and 1800 seconds.
  - `selectiveCallRecordingSettings` (object): Selective call recording settings. Applicable when `recordingMode` is set to either `Always` or `Always with Pause/Resume`.
    - `recordInboundInternalCallsEnabled` (boolean) **(requerido)**: If `true`, inbound internal calls are recorded.
    - `recordInboundExternalCallsEnabled` (boolean) **(requerido)**: If `true`, inbound external calls are recorded.
    - `recordOutboundInternalCallsEnabled` (boolean) **(requerido)**: If `true`, outbound internal calls are recorded.
    - `recordOutboundExternalCallsEnabled` (boolean) **(requerido)**: If `true`, outbound external calls are recorded.
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
