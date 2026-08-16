---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-queues-queueid-strandedcalls
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/locations/{locationId}/queues/{queueId}/strandedCalls
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.605375+00:00
---

# PUT /telephony/config/locations/{locationId}/queues/{queueId}/strandedCalls

**API:** Webex Cloud Calling
**Área:** Features:  Call Queue
**operationId:** `updateCallQueueStrandedCalls`

## Resumen
Update a Call Queue Stranded Calls Service

## Descripción
Update the designated Call Stranded Calls Service.

Allow admin to modify configured Stranded Calls settings, including whether the stranded calls queue policy will be triggered when all agents are unreachable.

Updating a call queue stranded calls requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) **(requerido)**: Location in which this call queue exists.
- `queueId` [path] (string) **(requerido)**: Update setting for the call queue with the matching ID.
- `orgId` [query] (string): Update call queue settings from this organization.

## Cuerpo de la petición (application/json)
- `action` (string) **(requerido)**: The call processing action type.  * `NONE` - Call remains in the queue.  * `BUSY` - Calls are removed from the queue and are provided with the Busy treatment. If the queue is configured with the Call Forwarding Busy or the Voice Messaging service, then the call is handled accordingly.  * `TRANSFER` - Calls are removed from the queue and are transferred to the configured `transferPhoneNumber`.  * `NIGHT_SERVICE` - Calls are handled according to the Night Service configuration. If the Night Service action is set to `none`, then this is equivalent to this policy being set to `none` (that is, calls remain in the queue).  * `RINGING` - Calls are removed from the queue and are provided with ringing until the caller releases the call. The ringback tone played to the caller is localized according to the country code of the caller.  * `ANNOUNCEMENT` - Calls are removed from the queue and are provided with an announcement that is played in a loop until the caller releases the call. Valores: NONE, BUSY, TRANSFER, NIGHT_SERVICE, RINGING, ANNOUNCEMENT.
- `transferPhoneNumber` (string): Call gets transferred to this number when action is set to `TRANSFER`. This can also be an extension.
- `audioMessageSelection` (string) **(requerido)**: The type of announcement to be played.  * `DEFAULT` - Default Audio Message Selection.  * `CUSTOM` - Custom Audio Message Selection. Valores: DEFAULT, CUSTOM.
- `audioFiles` (array): List of pre-configured Announcement Audio Files when `audioMessageSelection` is `CUSTOM`.
  - `id` (string): A unique identifier for the announcement. `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement.
  - `fileName` (string): Audio announcement file name.
  - `mediaFileType` (string): Audio announcement file type.  * `WAV` - WAV File Extension.  * `WMA` - WMA File Extension.  * `3GP` - 3GP File Extension. Valores: WAV, WMA, 3GP.
  - `level` (string): Audio announcement file type location.  * `ORGANIZATION` - Audio file is configured across organisation.  * `LOCATION` - Audio file is configured across location.  * `ENTITY` - Audio file is configured on instance level. Valores: ORGANIZATION, LOCATION, ENTITY.
- `triggerPolicyWhenAllAgentsAreUnreachableEnabled` (boolean): Trigger stranded calls queue policy when all agents are unreachable.

### Ejemplo de petición
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
  "triggerPolicyWhenAllAgentsAreUnreachableEnabled": true
}
```

## Respuestas
- **204**: No Content
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
