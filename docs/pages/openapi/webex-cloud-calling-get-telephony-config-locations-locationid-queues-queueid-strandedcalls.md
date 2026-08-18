---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-queues-queueid-strandedcalls
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/queues/{queueId}/strandedCalls
operation_id: getCallQueueStrandedCalls
tags: Features:  Call Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.302085+00:00
---

# GET /telephony/config/locations/{locationId}/queues/{queueId}/strandedCalls

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `getCallQueueStrandedCalls`

## Resumen
Get Details for a Call Queue Stranded Calls

## Descripción
Allow admin to view default/configured Stranded Calls settings, including whether the stranded calls queue policy will be triggered when all agents are unreachable.

Stranded-All agents logoff Policy: If the last agent staffing a queue “unjoins” the queue or signs out, then all calls in the queue become stranded.
Stranded-Unavailable Policy: This policy allows for the configuration of the processing of calls that are in a staffed queue when all agents are unavailable.

Retrieving call queue Stranded Calls details requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Retrieve settings for a call queue in this location.
- `queueId` [path] (string) (**requerido**): Retrieve settings for the call queue with this identifier.
- `orgId` [query] (string): Retrieve call queue settings from this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/queues/<queueId>/strandedCalls' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `action` (string) (**requerido**): The call processing action type.  * `NONE` - Call remains in the queue.  * `BUSY` - Calls are removed from the queue and are provided with the Busy treatment. If the queue is configured with the Call Forwarding Busy or the Voice Messaging service, then the call is handled accordingly.  * `TRANSFER` - Calls are removed from the queue and are transferred to the configured `transferPhoneNumber`.  * `NIGHT_SERVICE` - Calls are handled according to the Night Service configuration. If the Night Service action is set to `none`, then this is equivalent to this policy being set to `none` (that is, calls remain in the queue).  * `RINGING` - Calls are removed from the queue and are provided with ringing until the caller releases the call. The ringback tone played to the caller is localized according to the country code of the caller.  * `ANNOUNCEMENT` - Calls are removed from the queue and are provided with an announcement that is played in a loop until the caller releases the call. Valores: NONE, BUSY, TRANSFER, NIGHT_SERVICE, RINGING, ANNOUNCEMENT.
- `transferPhoneNumber` (string): Call gets transferred to this number when action is set to `TRANSFER`. This can also be an extension.
- `audioMessageSelection` (string) (**requerido**): The type of announcement to be played.  * `DEFAULT` - Default Audio Message Selection.  * `CUSTOM` - Custom Audio Message Selection. Valores: DEFAULT, CUSTOM.
- `audioFiles` (array): List of Announcement Audio Files when `audioMessageSelection` is `CUSTOM`.
  - `id` (string) (**requerido**): A unique identifier for the announcement.
  - `fileName` (string) (**requerido**): Audio announcement file name.
  - `mediaFileType` (string) (**requerido**): Audio announcement file type.  * `WAV` - WAV File Extension.  * `WMA` - WMA File Extension.  * `3GP` - 3GP File Extension. Valores: WAV, WMA, 3GP.
  - `level` (string) (**requerido**): Audio announcement file type location.  * `ORGANIZATION` - Audio file is configured across organization.  * `LOCATION` - Audio file is configured across location.  * `ENTITY` - Audio file is configured on instance level. Valores: ORGANIZATION, LOCATION, ENTITY.
  - `isTextToSpeech` (boolean) (**requerido**): Indicates whether the announcement is a text-to-speech file.
- `triggerPolicyWhenAllAgentsAreUnreachableEnabled` (boolean): Trigger stranded calls queue policy when all agents are unreachable.

### Ejemplo — respuesta 200
```json
{
  "action": "NONE",
  "transferPhoneNumber": "+911235557890",
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
  ],
  "triggerPolicyWhenAllAgentsAreUnreachableEnabled": true
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