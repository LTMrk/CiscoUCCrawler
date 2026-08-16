---
doc_id: webex-cloud-calling-get-telephony-config-announcements-playlists-playlistid-usage
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/announcements/playlists/{playListId}/usage
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.594555+00:00
---

# GET /telephony/config/announcements/playlists/{playListId}/usage

**API:** Webex Cloud Calling
**Área:** Call Queue Settings with Playlist Settings
**operationId:** `getPlaylistUsage`

## Resumen
Get Playlist Usage

## Parámetros
- `playListId` [path] (string) **(requerido)**: Unique identifier of the playlist.
- `playlistUsageType` [query] (string): Filter usage by type.

## Respuestas
- **200**: OK
  - `id` (string) **(requerido)**: Identifier of the playlist.
  - `locations` (array) **(requerido)**: List of locations using this playlist.
    - `id` (string) **(requerido)**: Location identifier.
    - `name` (string) **(requerido)**: Location name.
    - `featureReference` (object) **(requerido)**: Feature referencing the playlist.
      - `id` (string) **(requerido)**: Feature identifier.
      - `name` (string) **(requerido)**: Feature name.
      - `type` (string) **(requerido)**: Feature type.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
