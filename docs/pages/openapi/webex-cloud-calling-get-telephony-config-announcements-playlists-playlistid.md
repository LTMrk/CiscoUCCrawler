---
doc_id: webex-cloud-calling-get-telephony-config-announcements-playlists-playlistid
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/announcements/playlists/{playlistId}
operation_id: getAnnouncementPlaylist
tags: Features: Announcement Playlist
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:08.013770+00:00
---

# GET /telephony/config/announcements/playlists/{playlistId}

**API:** Webex Cloud Calling
**Área:** Features: Announcement Playlist
**operationId:** `getAnnouncementPlaylist`

## Resumen
Get Announcement Playlist

## Descripción
Fetch details of announcement playlist by its ID at an organization level.

This API requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `playlistId` [path] (string) (**requerido**): Unique identifier of an announcement playlist.
- `orgId` [query] (string): Get an announcement playlist in this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/announcements/playlists/<playlistId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Unique identifier of the playlist.
- `name` (string) (**requerido**): Unique name of the playlist.
- `lastUpdated` (string) (**requerido**): Last updated timestamp (in UTC format) of the playlist.
- `fileSize` (string) (**requerido**): Size of the files in kilobytes.
- `fileCount` (string) (**requerido**): Number of files in the playlist.
- `announcements` (array) (**requerido**): List of announcement details associated with playlist.
  - `id` (string) (**requerido**): Unique identifier of the announcement.
  - `name` (string) (**requerido**): Name of the announcement.
  - `fileName` (string): File name of the uploaded binary announcement greeting.
  - `fileSize` (string) (**requerido**): Size of the file in kilobytes.
  - `mediaFileType` (string) (**requerido**): Media file type of the announcement file.
  - `lastUpdated` (string) (**requerido**): Last updated timestamp (in UTC format) of the announcement.
  - `level` (string) (**requerido**): The level at which this playlist exists. Valores: ORGANIZATION.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC9iYzZjOTYwYi01ZDJjLTRiM2QtYjRlZC0wNWY1ZmFhMTJjZjA",
  "name": "testingAnnouncementPlaylist",
  "lastUpdated": "2024-03-06T07:06:36.396Z",
  "fileSize": "4279",
  "fileCount": 1,
  "announcements": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC83ODNmNjNhZi1jNDU1LTRhZWItODg0OS1jZThjNDQ4ZmNjNTg",
      "name": "TestAnnouncement1TT",
      "mediaFileType": "WAV",
      "fileName": "12Soft Piano Music_16000_mon1 copy.wav",
      "fileSize": "4279",
      "lastUpdated": "2023-06-06 13:51:02",
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