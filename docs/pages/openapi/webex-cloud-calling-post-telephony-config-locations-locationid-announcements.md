---
doc_id: webex-cloud-calling-post-telephony-config-locations-locationid-announcements
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/locations/{locationId}/announcements
operation_id: Upload a binary announcement greeting at the location level
tags: Features: Announcement Repository
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.285198+00:00
---

# POST /telephony/config/locations/{locationId}/announcements

**API:** Webex Cloud Calling
**Área:** Features: Announcement Repository
**operationId:** `Upload a binary announcement greeting at the location level`

## Resumen
Upload a binary announcement greeting at the location level

## Descripción
Upload a binary file to the announcement repository at a location level.

An admin can upload a file at a location level. This file will be uploaded to the announcement repository.

Your request will need to be an `application/json` request with the announcement details including name, fileUri, fileName, and isTextToSpeech fields.

This API requires a full administrator or location administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Unique identifier of a location where an announcement is being created.
- `orgId` [query] (string): Create an announcement for location in this organization.

## Cuerpo de la petición (application/json)
- `name` (string) (**requerido**): Name of the announcement. Long. max: 256.
- `fileUri` (string) (**requerido**): URI of the announcement file. Long. max: 256.
- `fileName` (string) (**requerido**): File name of the announcement. Long. max: 80.
- `isTextToSpeech` (boolean) (**requerido**): Indicates whether the announcement is text-to-speech.

### Ejemplo — petición
```json
{
  "name": "Public_Announcement",
  "fileUri": "https://example.com/announcements/greeting.wav",
  "fileName": "greeting.wav",
  "isTextToSpeech": false
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/locations/<locationId>/announcements' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "fileUri": "<fileUri>", "fileName": "<fileName>", "isTextToSpeech": true}'
```

## Respuestas correctas
**201**: Created
- `id` (string) (**requerido**): Unique identifier of the announcement.

### Ejemplo — respuesta 201
```json
{
  "id": "Y2lzY29zcGFyazovL3VzL0FOTk9VTkNFTUVOVC8zMjAxNjRmNC1lNWEzLTQxZmYtYTMyNi02N2MwOThlNDFkMWQ"
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