---
doc_id: webex-cloud-calling-put-telephony-config-locations-locationid-musiconhold
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/locations/{locationId}/musicOnHold
operation_id: Update Music On Hold
tags: Location Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.723972+00:00
---

# PUT /telephony/config/locations/{locationId}/musicOnHold

**API:** Webex Cloud Calling
**Área:** Location Call Settings
**operationId:** `Update Music On Hold`

## Resumen
Update Music On Hold

## Descripción
Update the location's music on hold settings.

Location music on hold settings allows you to play music when a call is placed on hold or parked.

Updating a location's music on hold settings requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Update music on hold settings for this location.
- `orgId` [query] (string): Update music on hold settings for this organization.

## Cuerpo de la petición (application/json)
- `mohEnabled` (boolean): Music on hold is enabled or disabled for the workspace.
- `greeting` (string): Greeting type for the workspace.  * `DEFAULT` - Play music configured at location level.  * `CUSTOM` - Play custom music when call is placed on hold or parked. An audio file must already have been successfully uploaded to specify this option. Valores: DEFAULT, CUSTOM.
- `audioAnnouncementFile` (object):
  - `id` (string): A unique identifier for the [announcement](/docs/api/v1/features-announcement-repository). `name`, `mediaFileType`, `level` are mandatory if `id` is not provided for uploading an announcement. If all four fields are provided, file with given `id` is used and other fields are ignored.
  - `fileName` (string): Audio announcement file name.
  - `mediaFileType` (string): Audio announcement file type.  * `WAV` - WAV File Extension. Valores: WAV.
  - `level` (string): Audio announcement file type location.  * `ORGANIZATION` - Specifies this audio file is configured across the organization.  * `LOCATION` - Specifies this audio file is configured across the location. Valores: ORGANIZATION, LOCATION.

### Ejemplo — petición
```json
{
  "callHoldEnabled": true,
  "callParkEnabled": true,
  "greeting": "SYSTEM",
  "audioFile": {
    "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC9jZWRkODcwYS1lMTkzLTQxNmQtYmM3OS1mNzkyYmUyMzlhOGI",
    "fileName": "AUDIO_FILE.wav",
    "mediaFileType": "WAV",
    "level": "ORGANIZATION"
  },
  "playlistId": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC9iYzZjOTYwYi01ZDJjLTRiM2QtYjRlZC0wNWY1ZmFhMTJjZjA"
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/locations/<locationId>/musicOnHold' \
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