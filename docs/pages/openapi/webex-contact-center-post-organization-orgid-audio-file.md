---
doc_id: webex-contact-center-post-organization-orgid-audio-file
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/audio-file
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.931033+00:00
---

# POST /organization/{orgid}/audio-file

**API:** Webex Contact Center
**Área:** Audio Files
**operationId:** `createConfig_26`

## Resumen
Create a new Audio File

## Descripción
Create a new Audio File in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `audioFileInfo` (object) **(requerido)**:
  - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: A name for the Agent's personal greeting file. It should have valid extension i.e. .wav
  - `contentType` (string) **(requerido)**: Indicates Content-Type of the Audio file. It can take one of these values: AUDIO_WAV, AUDIO_X_WAV Valores: AUDIO_WAV, TEXT_HTML, TEXT_PHP, AUDIO_X_WAV, APPLICATION_OCTET_STREAM.
  - `blobId` (string): Identifier for the audio file.
  - `url` (string): Audio file download url.
  - `description` (string): A short description of the dial plan.
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not
  - `audioFile` (string):
  - `createdTime` (integer): Creation time(in epoch millis) of this resource.
  - `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.
- `audioFile` (string) **(requerido)**:

## Cuerpo de la petición (multipart/form-data)
- `audioFileInfo` (object) **(requerido)**:
  - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: A name for the Agent's personal greeting file. It should have valid extension i.e. .wav
  - `contentType` (string) **(requerido)**: Indicates Content-Type of the Audio file. It can take one of these values: AUDIO_WAV, AUDIO_X_WAV Valores: AUDIO_WAV, TEXT_HTML, TEXT_PHP, AUDIO_X_WAV, APPLICATION_OCTET_STREAM.
  - `blobId` (string): Identifier for the audio file.
  - `url` (string): Audio file download url.
  - `description` (string): A short description of the dial plan.
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not
  - `audioFile` (string):
  - `createdTime` (integer): Creation time(in epoch millis) of this resource.
  - `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.
- `audioFile` (string) **(requerido)**:

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: A name for the Agent's personal greeting file. It should have valid extension i.e. .wav
  - `contentType` (string) **(requerido)**: Indicates Content-Type of the Audio file. It can take one of these values: AUDIO_WAV, AUDIO_X_WAV Valores: AUDIO_WAV, TEXT_HTML, TEXT_PHP, AUDIO_X_WAV, APPLICATION_OCTET_STREAM.
  - `blobId` (string): Identifier for the audio file.
  - `url` (string): Audio file download url.
  - `description` (string): A short description of the dial plan.
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not
  - `audioFile` (string):
  - `createdTime` (integer): Creation time(in epoch millis) of this resource.
  - `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
