---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-queues-queueid-holidayservice
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/locations/{locationId}/queues/{queueId}/holidayService
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.604322+00:00
---

# GET /telephony/config/locations/{locationId}/queues/{queueId}/holidayService

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `getCallQueueHolidayService`

## Resumen
Get Details for a Call Queue Holiday Service

## Descripción
Retrieve Call Queue Holiday Service details.

Configure the call queue to route calls differently during the holidays.

Retrieving call queue holiday service details requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Retrieve settings for a call queue in this location.
- `queueId` [path] (string) **(requerido)**: Retrieve settings for the call queue with this identifier.
- `orgId` [query] (string): Retrieve call queue settings from this organization.

## Respuestas
- **200**: OK
  - `holidayServiceEnabled` (boolean) **(requerido)**: Whether or not the call queue holiday service routing policy is enabled.
  - `action` (string) **(requerido)**: The call processing action type.  * `BUSY` - The caller hears a fast-busy tone.  * `TRANSFER` - Transfers the call to number specified in `transferPhoneNumber`. Valores: BUSY, TRANSFER.
  - `holidayScheduleLevel` (string) **(requerido)**: The schedule mentioned in `holidayScheduleName` is org or location specific. (Must be from `holidaySchedules` list)  * `LOCATION` - Schedule is configured across a location.  * `ORGANIZATION` - Schedule is configured across an organization. Valores: LOCATION, ORGANIZATION.
  - `holidayScheduleName` (string): Name of the schedule configured for a holiday service as one of from `holidaySchedules` list.
  - `transferPhoneNumber` (string): Call gets transferred to this number when action is set to `TRANSFER`. This can also be an extension.
  - `playAnnouncementBeforeEnabled` (boolean) **(requerido)**: Indicates whether an announcement plays to callers before the action is applied.
  - `audioMessageSelection` (string) **(requerido)**: The type of announcement to be played.  * `DEFAULT` - Default Audio Message Selection.  * `CUSTOM` - Custom Audio Message Selection. Valores: DEFAULT, CUSTOM.
  - `audioFiles` (array): List of Announcement Audio Files when `audioMessageSelection` is `CUSTOM`.
    - `id` (string) **(requerido)**: A unique identifier for the announcement.
    - `fileName` (string) **(requerido)**: Audio announcement file name.
    - `mediaFileType` (string) **(requerido)**: Audio announcement file type.  * `WAV` - WAV File Extension.  * `WMA` - WMA File Extension.  * `3GP` - 3GP File Extension. Valores: WAV, WMA, 3GP.
    - `level` (string) **(requerido)**: Audio announcement file type location.  * `ORGANIZATION` - Audio file is configured across organization.  * `LOCATION` - Audio file is configured across location.  * `ENTITY` - Audio file is configured on instance level. Valores: ORGANIZATION, LOCATION, ENTITY.
    - `isTextToSpeech` (boolean) **(requerido)**: Indicates whether the announcement is a text-to-speech file.
  - `holidaySchedules` (array): Lists the pre-configured holiday schedules.
    - `scheduleName` (string) **(requerido)**: Name of the schedule configured for a holiday service.
    - `scheduleLevel` (string) **(requerido)**: Indicates whether the schedule in scheduleName is specific to the organization or location.  * `LOCATION` - Schedule is configured across a location.  * `ORGANIZATION` - Schedule is configured across an organization. Valores: LOCATION, ORGANIZATION.
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
