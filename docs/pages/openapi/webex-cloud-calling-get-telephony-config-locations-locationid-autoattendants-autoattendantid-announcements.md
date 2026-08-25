---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-autoattendants-autoattendantid-announcements
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/autoAttendants/{autoAttendantId}/announcements
operation_id: listAutoAttendantAnnouncementFiles
tags: Features:  Auto Attendant
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-25T10:28:32.466127+00:00
---

# GET /telephony/config/locations/{locationId}/autoAttendants/{autoAttendantId}/announcements

**API:** Webex Cloud Calling
**Área:** Features:  Auto Attendant
**operationId:** `listAutoAttendantAnnouncementFiles`

## Resumen
Read the List of Auto Attendant Announcement Files

## Descripción
List file info for all auto attendant announcement files associated with this auto attendant.

Auto attendant announcement files contain messages and music that callers hear while waiting in the queue. A auto attendant can be configured to play whatever subset of these announcement files is desired.

Retrieving this list of files requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

Note that uploading of announcement files via API is not currently supported, but is available via Webex Control Hub.

## Parámetros
- `locationId` [path] (string) (**requerido**): Location in which this auto attendant exists.
- `autoAttendantId` [path] (string) (**requerido**): Retrieve announcement files for the auto attendant with this identifier.
- `orgId` [query] (string): Retrieve announcement files for a auto attendant from this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/autoAttendants/<autoAttendantId>/announcements' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `announcements` (array) (**requerido**): Array of announcements for this auto attendant.
  - `id` (string) (**requerido**): ID of the announcement.
  - `fileName` (string) (**requerido**): Name of greeting file.
  - `fileSize` (string) (**requerido**): Size of greeting file in kilo-bytes.
  - `mediaFileType` (string) (**requerido**): * `WMA` - WMA File Extension.  * `WAV` - WAV File Extension.  * `GP` - 3GP File Extension.  * `MOV` - MOV File Extension. Valores: WMA, WAV, GP, MOV.
  - `level` (string) (**requerido**): * `ORGANIZATION` - Organization level.  * `LOCATION` - Location level.  * `ENTITY` - Entity level. Valores: ORGANIZATION, LOCATION, ENTITY.
  - `isTextToSpeech` (boolean) (**requerido**): Indicates whether the announcement is a text-to-speech file.

### Ejemplo — respuesta 200
```json
{
  "announcements": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC9kODc5YWZlZC1jNTRhLTQyOTctOGY0Mi02ZmEyMDJjN2E1M2E",
      "fileName": "Greeting-1.wav",
      "fileSize": "33456",
      "mediaFileType": "WAV",
      "level": "ORGANIZATION"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC8zMjAxNjRmNC1lNWEzLTQxZmYtYTMyNi02N2MwOThlNDFrMWY",
      "fileName": "Greeting-2.wav",
      "fileSize": "32356",
      "mediaFileType": "WAV",
      "level": "LOCATION"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC8zMjAxNjRmNC1lNWEzLTQxZmYtYTMyNi02N2MwOThlNDFoNmc",
      "fileName": "Greeting-3.wav",
      "fileSize": "31237",
      "mediaFileType": "WAV",
      "level": "ORGANIZATION"
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