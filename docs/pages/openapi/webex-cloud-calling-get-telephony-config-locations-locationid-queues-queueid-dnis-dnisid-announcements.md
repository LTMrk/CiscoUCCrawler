---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-queues-queueid-dnis-dnisid-announcements
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/queues/{queueId}/dnis/{dnisId}/announcements
operation_id: getDnisAnnouncementsForACallQueue
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.271120+00:00
---

# GET /telephony/config/locations/{locationId}/queues/{queueId}/dnis/{dnisId}/announcements

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `getDnisAnnouncementsForACallQueue`

## Resumen
Get DNIS Announcements for a Call Queue

## Descripción
Get the announcement settings for a specific DNIS (Dialed Number Identification Service) entry in a call queue.

This includes welcome message, comfort message, music on hold, wait message, and whisper message settings.

Retrieving DNIS announcements requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): The location ID where the call queue exists.
- `queueId` [path] (string) (**requerido**): The call queue ID.
- `dnisId` [path] (string) (**requerido**): The DNIS ID.
- `orgId` [query] (string): The organization ID of the customer.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/queues/<queueId>/dnis/<dnisId>/announcements' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `customDnisAnnouncementSettingsEnabled` (boolean): Whether custom DNIS announcement settings are enabled for this DNIS.
- `welcomeMessage` (object): Welcome message settings.
  - `enabled` (boolean): Whether the welcome message is enabled.
  - `alwaysEnabled` (boolean): Whether to always play the welcome message.
  - `greeting` (string): The greeting type. Valores: DEFAULT, CUSTOM.
  - `audioAnnouncementFiles` (array): List of audio announcement files.
    - `id` (string): Announcement file ID.
    - `fileName` (string): Name of the announcement file.
    - `mediaFileType` (string): Media file type of the announcement. Valores: WAV.
    - `level` (string): Level at which the announcement is defined. Valores: ORGANIZATION, LOCATION, ENTITY.
    - `isTextToSpeech` (boolean): Whether the file is a text-to-speech file.
- `comfortMessage` (object): Comfort message settings.
  - `enabled` (boolean): Whether the comfort message is enabled.
  - `timeBetweenMessages` (integer): Time between comfort messages in seconds.
  - `greeting` (string): The greeting type. Valores: DEFAULT, CUSTOM.
  - `audioAnnouncementFiles` (array): List of audio announcement files.
    - `id` (string): Announcement file ID.
    - `fileName` (string): Name of the announcement file.
    - `mediaFileType` (string): Media file type of the announcement. Valores: WAV.
    - `level` (string): Level at which the announcement is defined. Valores: ORGANIZATION, LOCATION, ENTITY.
    - `isTextToSpeech` (boolean): Whether the file is a text-to-speech file.
- `comfortMessageBypass` (object): Comfort message bypass settings.
  - `enabled` (boolean): Whether the comfort message bypass is enabled.
  - `callWaitingAgeThreshold` (integer): Call waiting age threshold in seconds.
  - `greeting` (string): The greeting type. Valores: DEFAULT, CUSTOM.
  - `audioAnnouncementFiles` (array): List of audio announcement files.
    - `id` (string): Announcement file ID.
    - `fileName` (string): Name of the announcement file.
    - `mediaFileType` (string): Media file type of the announcement. Valores: WAV.
    - `level` (string): Level at which the announcement is defined. Valores: ORGANIZATION, LOCATION, ENTITY.
    - `isTextToSpeech` (boolean): Whether the file is a text-to-speech file.
- `mohMessage` (object): Music on hold message settings.
  - `normalSource` (object):
    - `enabled` (boolean): Whether the source is enabled.
    - `greeting` (string): The greeting type. Valores: DEFAULT, CUSTOM, PLAYLIST.
    - `audioAnnouncementFiles` (array): List of audio announcement files.
      - `id` (string): Announcement file ID.
      - `fileName` (string): Name of the announcement file.
      - `mediaFileType` (string): Media file type of the announcement. Valores: WAV.
      - `level` (string): Level at which the announcement is defined. Valores: ORGANIZATION, LOCATION, ENTITY.
      - `isTextToSpeech` (boolean): Whether the file is a text-to-speech file.
    - `audioPlaylistId` (string): Audio playlist ID.
    - `audioPlaylistName` (string): Audio playlist name.
  - `alternateSource` (object):
    - `enabled` (boolean): Whether the source is enabled.
    - `greeting` (string): The greeting type. Valores: DEFAULT, CUSTOM, PLAYLIST.
    - `audioAnnouncementFiles` (array): List of audio announcement files.
      - `id` (string): Announcement file ID.
      - `fileName` (string): Name of the announcement file.
      - `mediaFileType` (string): Media file type of the announcement. Valores: WAV.
      - `level` (string): Level at which the announcement is defined. Valores: ORGANIZATION, LOCATION, ENTITY.
      - `isTextToSpeech` (boolean): Whether the file is a text-to-speech file.
    - `audioPlaylistId` (string): Audio playlist ID.
    - `audioPlaylistName` (string): Audio playlist name.
- `waitMessage` (object): Wait message settings.
  - `enabled` (boolean): Whether the wait message is enabled.
  - `waitMode` (string): Wait mode for the message. Valores: TIME, POSITION.
  - `handlingTime` (integer): Maximum waiting time in minutes.
  - `defaultHandlingTime` (integer): Default handling time in minutes.
  - `queuePosition` (integer): Maximum queue position.

### Ejemplo — respuesta 200
```json
{
  "customDnisAnnouncementSettingsEnabled": true,
  "welcomeMessage": {
    "enabled": true,
    "alwaysEnabled": false,
    "greeting": "DEFAULT"
  },
  "comfortMessage": {
    "enabled": true,
    "timeBetweenMessages": 30,
    "greeting": "DEFAULT"
  },
  "comfortMessageBypass": {
    "enabled": false,
    "callWaitingAgeThreshold": 30,
    "greeting": "DEFAULT"
  },
  "mohMessage": {
    "normalSource": {
      "enabled": true,
      "greeting": "DEFAULT"
    },
    "alternateSource": {
      "enabled": false,
      "greeting": "DEFAULT"
    }
  },
  "waitMessage": {
    "enabled": false,
    "waitMode": "TIME",
    "handlingTime": 100,
    "defaultHandlingTime": 5,
    "queuePosition": 100,
    "highVolumeMessageEnabled": false,
    "estimatedWaitingTime": 10,
    "callbackOptionEnabled": false,
    "minimumEstimatedCallbackTime": 30,
    "internationalCallbackEnabled": false,
    "playUpdatedEstimatedWaitMessage": false
  },
  "whisperMessage": {
    "enabled": false,
    "greeting": "DEFAULT"
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