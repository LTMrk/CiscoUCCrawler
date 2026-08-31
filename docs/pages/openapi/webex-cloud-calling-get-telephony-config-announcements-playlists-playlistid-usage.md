---
doc_id: webex-cloud-calling-get-telephony-config-announcements-playlists-playlistid-usage
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/announcements/playlists/{playListId}/usage
operation_id: getPlaylistUsage
tags: Call Queue Settings with Playlist Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.247327+00:00
---

# GET /telephony/config/announcements/playlists/{playListId}/usage

**API:** Webex Cloud Calling
**Área:** Call Queue Settings with Playlist Settings
**operationId:** `getPlaylistUsage`

## Resumen
Get Playlist Usage

## Parámetros
- `playListId` [path] (string) (**requerido**): Unique identifier of the playlist.
- `playlistUsageType` [query] (string): Filter usage by type. Valores: feature, location.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/announcements/playlists/<playListId>/usage' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `id` (string) (**requerido**): Identifier of the playlist.
- `locations` (array) (**requerido**): List of locations using this playlist.
  - `id` (string) (**requerido**): Location identifier.
  - `name` (string) (**requerido**): Location name.
  - `featureReference` (object) (**requerido**): Feature referencing the playlist.
    - `id` (string) (**requerido**): Feature identifier.
    - `name` (string) (**requerido**): Feature name.
    - `type` (string) (**requerido**): Feature type.

### Ejemplo — respuesta 200
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL1BMQVlMSVNULzg1NWU1N2M0LWUzYTAtNGEyZS1hYWYxLTQ3ZWUxMmI3M2U2MA",
  "locations": [
    {
      "name": "RCDN6",
      "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzAxNWFmN2QzLTRlNzktNGY2ZC04Nzk5LWRlMjEzYTBhZDNhYQ",
      "featureReference": {
        "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUVVFVUUvNGFlMzJkMTAtNWI0Zi00NmNmLWI4ZTQtYmE2YzNiZjMyZGZi",
        "name": "Test Call Queue",
        "type": "CALL_QUEUE"
      }
    },
    {
      "name": "RCDN6",
      "id": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzAxNWFmN2QzLTRlNzktNGY2ZC04Nzk5LWRlMjEzYTBhZDNhYQ",
      "featureReference": {
        "id": "Y2lzY29zcGFyazovL3VzL0NBTExfUVVFVUUvMTkyNDYxMjEtZDhiYi00NTdjLWEzZjQtNGQ3YTBlYmQ4Nzk2",
        "name": "Test Call Queue 3",
        "type": "CALL_QUEUE"
      }
    }
  ]
}
```

## Respuestas de error
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.

## Contexto de la API
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs