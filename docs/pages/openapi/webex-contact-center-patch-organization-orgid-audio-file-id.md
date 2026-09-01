---
doc_id: webex-contact-center-patch-organization-orgid-audio-file-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PATCH
path: /organization/{orgid}/audio-file/{id}
operation_id: patchConfig_1
tags: Audio Files
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.646678+00:00
---

# PATCH /organization/{orgid}/audio-file/{id}

**API:** Webex Contact Center
**Área:** Audio Files
**operationId:** `patchConfig_1`

## Resumen
Partially update Audio File by ID

## Descripción
Partially update Audio File by ID in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): Resource ID of the Audio File.

## Cuerpo de la petición (application/json)
- `description` (string): A short description of the dial plan. Long. max: 255.

## Cuerpo de la petición (multipart/form-data)
- `description` (string): A short description of the dial plan. Long. max: 255.

## Ejemplo de invocación
```bash
curl -X PATCH '/organization/<orgid>/audio-file/<id>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): A name for the Agent's personal greeting file. It should have valid extension i.e. .wav Long. max: 80.
- `contentType` (string) (**requerido**): Indicates Content-Type of the Audio file. It can take one of these values: AUDIO_WAV, AUDIO_X_WAV Valores: AUDIO_WAV, TEXT_HTML, TEXT_PHP, AUDIO_X_WAV, APPLICATION_OCTET_STREAM.
- `blobId` (string): Identifier for the audio file.
- `url` (string/url): Audio file download url.
- `description` (string): A short description of the dial plan. Long. max: 255.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `audioFile` (string/binary):
- `createdTime` (integer/int64) (solo lectura): Creation time(in epoch millis) of this resource.
- `lastUpdatedTime` (integer/int64) (solo lectura): Time(in epoch millis) when this resource was last updated.

## Respuestas de error
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs