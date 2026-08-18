---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-queues-queueid-nightservice
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/queues/{queueId}/nightService
operation_id: updateCallQueueNightService
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.301390+00:00
---

# PUT /telephony/config/locations/{locationId}/queues/{queueId}/nightService

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `updateCallQueueNightService`

## Resumen
Update a Call Queue Night Service

## Descripción
Update Call Queue Night Service details.

Configure the call queue to route calls differently during the hours when the queue is not in service. This is
determined by a schedule that defines the business hours of the queue.

Updating call queue night service details requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Update settings for a call queue in this location.
- `queueId` [path] (string) (**requerido**): Update settings for the call queue night service with this identifier.
- `orgId` [query] (string): Update call queue night service settings from this organization.

## Cuerpo de la petición (application/json)
- `nightServiceEnabled` (boolean) (**requerido**): Enable or disable call queue night service routing policy.
- `action` (string): The call processing action type.  * `BUSY` - The caller hears a fast busy tone.  * `TRANSFER` - Transfers the call to number specified in `transferPhoneNumber`. Valores: BUSY, TRANSFER.
- `transferPhoneNumber` (string): Call gets transferred to this number when action is set to `TRANSFER`. This can also be an extension.
- `playAnnouncementBeforeEnabled` (boolean) (**requerido**): Indicates whether an announcement plays to callers before the action is applied.
- `announcementMode` (string) (**requerido**): The type of announcements to played.  * `NORMAL` - Plays announcement as per `audioMessageSelection`.  * `MANUAL` - Plays announcement as per `manualAudioMessageSelection`. Valores: NORMAL, MANUAL.
- `audioMessageSelection` (string) (**requerido**): The type of announcements to be played when announcementMode is set to `NORMAL`.  * `DEFAULT` - Default Audio Message Selection.  * `CUSTOM` - Custom Audio Message Selection. Valores: DEFAULT, CUSTOM.
- `audioFiles` (array): List of pre-configured Announcement Audio Files when `audioMessageSelection` is `CUSTOM`.
  - `id` (string): A unique identifier for the announcement. `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement.
  - `fileName` (string): Audio announcement file name.
  - `mediaFileType` (string): Audio announcement file type.  * `WAV` - WAV File Extension.  * `WMA` - WMA File Extension.  * `3GP` - 3GP File Extension. Valores: WAV, WMA, 3GP.
  - `level` (string): Audio announcement file type location.  * `ORGANIZATION` - Audio file is configured across organisation.  * `LOCATION` - Audio file is configured across location.  * `ENTITY` - Audio file is configured on instance level. Valores: ORGANIZATION, LOCATION, ENTITY.
- `businessHoursName` (string): Name of the schedule configured for a night service as one of from `businessHourSchedules` list.
- `businessHoursLevel` (string): The above mentioned schedule is org or location specific. (Must be from `businessHourSchedules` list)  * `ORGANIZATION` - Schedule is configured across an organization.  * `LOCATION` - Schedule is configured across a location. Valores: ORGANIZATION, LOCATION.
- `forceNightServiceEnabled` (boolean) (**requerido**): Force night service regardless of business hour schedule.
- `manualAudioMessageSelection` (string) (**requerido**): The type of announcements to be played when announcementMode is set to `MANUAL`.  * `DEFAULT` - Default Audio Message Selection.  * `CUSTOM` - Custom Audio Message Selection. Valores: DEFAULT, CUSTOM.
- `manualAudioFiles` (array): List Of pre-configured Audio Files.
  - `id` (string): A unique identifier for the announcement. `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement.
  - `fileName` (string): Audio announcement file name.
  - `mediaFileType` (string): Audio announcement file type.  * `WAV` - WAV File Extension.  * `WMA` - WMA File Extension.  * `3GP` - 3GP File Extension. Valores: WAV, WMA, 3GP.
  - `level` (string): Audio announcement file type location.  * `ORGANIZATION` - Audio file is configured across organisation.  * `LOCATION` - Audio file is configured across location.  * `ENTITY` - Audio file is configured on instance level. Valores: ORGANIZATION, LOCATION, ENTITY.

### Ejemplo — petición
```json
{
  "nightServiceEnabled": true,
  "action": "TRANSFER",
  "transferPhoneNumber": "1234",
  "playAnnouncementBeforeEnabled": true,
  "announcementMode": "NORMAL",
  "audioMessageSelection": "DEFAULT",
  "audioFiles": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC9jZWRkODcwYS1lMTkzLTQxNmQtYmM3OS1mNzkyYmUyMzlhOGI",
      "fileName": "AUDIO_FILE.wav",
      "mediaFileType": "WAV",
      "level": "ORGANIZATION"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC8zMjAxNjRmNC1lNWEzLTQxZmYtYTMyNi02N2MwOThlNDFoNmc",
      "fileName": "AUDIO_FILE_1.wav",
      "mediaFileType": "WAV",
      "level": "LOCATION"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC8zMjAxNjRmNC1lNWEzLTQxZmYtYTMyNi02N2MwOThlNDFrMWY",
      "fileName": "AUDIO_FILE_3.wav",
      "mediaFileType": "WAV",
      "level": "ORGANIZATION"
    }
  ],
  "businessHourSchedules": [
    {
      "scheduleName": "Working Hour",
      "scheduleLevel": "LOCATION"
    }
  ],
  "businessHoursLevel": "LOCATION",
  "businessHoursName": "Working Hour",
  "forceNightServiceEnabled": true,
  "manualAudioMessageSelection": "DEFAULT",
  "manualAudioFiles": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC9jZWRkODcwYS1lMTkzLTQxNmQtYmM3OS1mNzkyYmUyMzlhOGI",
      "fileName": "AUDIO_FILE.wav",
      "mediaFileType": "WAV",
      "level": "ORGANIZATION"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC8zMjAxNjRmNC1lNWEzLTQxZmYtYTMyNi02N2MwOThlNDFoNmc",
      "fileName": "AUDI
  ... (truncado)
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/queues/<queueId>/nightService' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"nightServiceEnabled": true, "playAnnouncementBeforeEnabled": true, "announcementMode": "<announcementMode>", "audioMessageSelection": "<audioMessageSelection>", "forceNightServiceEnabled": true, "manualAudioMessageSelection": "<manualAudioMessageSelection>"}'
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