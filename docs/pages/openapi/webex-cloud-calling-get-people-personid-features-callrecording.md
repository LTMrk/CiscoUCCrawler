---
doc_id: webex-cloud-calling-get-people-personid-features-callrecording
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /people/{personId}/features/callRecording
operation_id: Read Call Recording Settings for a Person
tags: User Call Settings (1/2)
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.361380+00:00
---

# GET /people/{personId}/features/callRecording

**API:** Webex Cloud Calling
**Área:** User Call Settings (1/2)
**operationId:** `Read Call Recording Settings for a Person`

## Resumen
Read Call Recording Settings for a Person

## Descripción
Retrieve a person's Call Recording settings.

The Call Recording feature provides a hosted mechanism to record the calls placed and received on the Carrier platform for replay and archival. This feature is helpful for quality assurance, security, training, and more.

This API requires a full or user administrator or location administrator auth token with the `spark-admin:people_read` scope.

<div><Callout type="warning">A person with a Webex Calling Standard license is eligible for the Call Recording feature only when the Call Recording vendor is Webex.</Callout></div>

## Parámetros
- `personId` [path] (string) (**requerido**): Unique identifier for the person.
- `orgId` [query] (string): ID of the organization in which the person resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.

## Ejemplo de invocación
```bash
curl -X GET '/people/<personId>/features/callRecording' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `enabled` (boolean) (**requerido**): `true` if call recording is enabled.
- `record` (string) (**requerido**): Call recording scenario.  * `Always` - Incoming and outgoing calls will be recorded with no control to start, stop, pause, or resume.  * `Never` - Calls will not be recorded.  * `Always with Pause/Resume` - Calls are always recorded, but user can pause or resume the recording. Stop recording is not supported.  * `On Demand with User Initiated Start` - Records only the portion of the call after the recording start (`*44`) has been entered. Pause, resume, and stop controls are supported. Valores: Always, Never, Always with Pause/Resume, On Demand with User Initiated Start.
- `recordVoicemailEnabled` (boolean) (**requerido**): When `true`, voicemail messages are also recorded.
- `notification` (object) (**requerido**): Pause/resume notification settings.
  - `type` (string) (**requerido**): Type of pause/resume notification.  * `None` - No notification sound played when call recording is paused or resumed.  * `Beep` - A beep sound is played when call recording is paused or resumed.  * `Play Announcement` - A verbal announcement is played when call recording is paused or resumed. Valores: None, Beep, Play Announcement.
  - `enabled` (boolean) (**requerido**): `true` when the notification feature is in effect. `false` indicates notification is disabled.
- `repeat` (object) (**requerido**): Beep sound plays periodically.
  - `interval` (number) (**requerido**): Interval at which warning tone "beep" will be played. This interval is an integer from 10 to 1800 seconds
  - `enabled` (boolean) (**requerido**): `true` when ongoing call recording tone will be played at the designated interval. `false` indicates no warning tone will be played.
- `serviceProvider` (string) (**requerido**): Name of the service provider providing call recording service.
- `externalGroup` (string) (**requerido**): Group utilized by the service provider providing call recording service.
- `externalIdentifier` (string) (**requerido**): Unique person identifier utilized by the service provider providing call recording service.
- `startStopAnnouncement` (object) (**requerido**): Call Recording starts and stops announcement settings.
  - `internalCallsEnabled` (boolean) (**requerido**): When `true`, an announcement is played when call recording starts and an announcement is played when call recording ends for internal calls.
  - `pstnCallsEnabled` (boolean) (**requerido**): When `true`, an announcement is played when call recording starts and an announcement is played when call recording ends for PSTN calls.
- `selectiveCallRecordingSettings` (object): Settings for selective call recording based on call direction and type.
  - `recordInboundInternalCallsEnabled` (boolean) (**requerido**): When `true`, inbound internal calls are recorded.
  - `recordInboundExternalCallsEnabled` (boolean) (**requerido**): When `true`, inbound external calls are recorded.
  - `recordOutboundInternalCallsEnabled` (boolean) (**requerido**): When `true`, outbound internal calls are recorded.
  - `recordOutboundExternalCallsEnabled` (boolean) (**requerido**): When `true`, outbound external calls are recorded.

### Ejemplo — respuesta 200
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
  "recordVoicemailEnabled": false,
  "startStopAnnouncementEnabled": false,
  "notification": {
    "enabled": true,
    "type": "None"
  },
  "repeat": {
    "interval": 15,
    "enabled": false
  },
  "serviceProvider": "WSWYZ25455",
  "externalGroup": "WSWYZ25455L31161",
  "externalIdentifier": "a34iidrh5o@64941297.int10.bcld.webex.com",
  "startStopAnnouncement": {
    "internalCallsEnabled": false,
    "pstnCallsEnabled": false
  },
  "callRecordingAccessSettings": {
    "viewAndPlayRecordingsEnabled": false,
    "downloadRecordingsEnabled": false,
    "deleteRecordingsEnabled": false,
    "shareRecordingsEnabled": false
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