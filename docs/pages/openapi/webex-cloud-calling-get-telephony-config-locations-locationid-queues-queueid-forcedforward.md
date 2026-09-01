---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-queues-queueid-forcedforward
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/queues/{queueId}/forcedForward
operation_id: getCallQueueForcedForward
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.694162+00:00
---

# GET /telephony/config/locations/{locationId}/queues/{queueId}/forcedForward

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `getCallQueueForcedForward`

## Resumen
Get Details for a Call Queue Forced Forward

## Descripción
Retrieve Call Queue policy Forced Forward details.

This policy allows calls to be temporarily diverted to a configured destination.

Retrieving call queue Forced Forward details requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve settings for a call queue in this location.
- `queueId` [path] (string) (**requerido**): Retrieve settings for the call queue with this identifier.
- `orgId` [query] (string): Retrieve call queue settings from this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/queues/<queueId>/forcedForward' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `forcedForwardEnabled` (boolean) (**requerido**): Whether or not the call queue forced forward routing policy setting is enabled.
- `transferPhoneNumber` (string): Call gets transferred to this number when action is set to `TRANSFER`. This can also be an extension.
- `playAnnouncementBeforeEnabled` (boolean) (**requerido**): Indicates whether an announcement plays to callers before the action is applied.
- `audioMessageSelection` (string) (**requerido**): The type of announcement to be played.  * `DEFAULT` - Default Audio Message Selection.  * `CUSTOM` - Custom Audio Message Selection. Valores: DEFAULT, CUSTOM.
- `audioFiles` (array): List of Announcement Audio Files when `audioMessageSelection` is `CUSTOM`.
  - `id` (string) (**requerido**): A unique identifier for the announcement.
  - `fileName` (string) (**requerido**): Audio announcement file name.
  - `mediaFileType` (string) (**requerido**): Audio announcement file type.  * `WAV` - WAV File Extension.  * `WMA` - WMA File Extension.  * `3GP` - 3GP File Extension. Valores: WAV, WMA, 3GP.
  - `level` (string) (**requerido**): Audio announcement file type location.  * `ORGANIZATION` - Audio file is configured across organization.  * `LOCATION` - Audio file is configured across location.  * `ENTITY` - Audio file is configured on instance level. Valores: ORGANIZATION, LOCATION, ENTITY.
  - `isTextToSpeech` (boolean) (**requerido**): Indicates whether the announcement is a text-to-speech file.

### Ejemplo — respuesta 200
```json
{
  "forcedForwardEnabled": true,
  "transferPhoneNumber": "+911235557890",
  "playAnnouncementBeforeEnabled": true,
  "audioMessageSelection": "DEFAULT",
  "audioFiles": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC9jZWRkODcwYS1lMTkzLTQxNmQtYmM3OS1mNzkyYmUyMzlhOGI",
      "fileName": "AUDIO_FILE.wav",
      "mediaFileType": "WAV",
      "level": "ORGANIZATION",
      "isTextToSpeech": false
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC8zMjAxNjRmNC1lNWEzLTQxZmYtYTMyNi02N2MwOThlNDFoNmc",
      "fileName": "AUDIO_FILE_1.wav",
      "mediaFileType": "WAV",
      "level": "LOCATION",
      "isTextToSpeech": false
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC8zMjAxNjRmNC1lNWEzLTQxZmYtYTMyNi02N2MwOThlNDFrMWY",
      "fileName": "AUDIO_FILE_3.wav",
      "mediaFileType": "WAV",
      "level": "ORGANIZATION",
      "isTextToSpeech": false
    }
  ]
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