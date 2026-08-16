---
doc_id: webex-contact-center-patch-organization-orgid-v2-agent-personal-greeting-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PATCH
path: /organization/{orgid}/v2/agent-personal-greeting/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.930783+00:00
---

# PATCH /organization/{orgid}/v2/agent-personal-greeting/{id}

**API:** Webex Contact Center
**Área:** Agent Personal Greeting Files
**operationId:** `patchV2ConfigAgentPersonalGreeting`

## Resumen
Partially update Greeting File by ID

## Descripción
Partially update Greeting File by ID in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Greeting File.

## Cuerpo de la petición (application/json)
- `attributeTag` (string): This is used to identify the purpose of a greeting.
- `greetingPurposeId` (string): Id of the greeting purpose

## Cuerpo de la petición (multipart/form-data)
- `attributeTag` (string): This is used to identify the purpose of a greeting.
- `greetingPurposeId` (string): Id of the greeting purpose

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: A name for the Agent's personal greeting file. It should have valid extension i.e. .wav
  - `contentType` (string) **(requerido)**: Indicates Content-Type of the Audio file. It can take one of these values: AUDIO_WAV, AUDIO_X_WAV Valores: AUDIO_WAV, TEXT_HTML, TEXT_PHP, AUDIO_X_WAV, APPLICATION_OCTET_STREAM.
  - `blobId` (string): Identifier for the audio file.
  - `url` (string): Audio file download url.
  - `agentId` (string) **(requerido)**: Agent Id with which this greeting file is to be associated with.
  - `firstName` (string): First Name of the Agent with whom this greeting file is to be associated with.
  - `lastName` (string): Last Name of the Agent with whom this greeting file is to be associated with.
  - `email` (string): Email of the Agent with whom this greeting file is to be associated with.
  - `agentActive` (boolean): Indicates whether the Agent with whom this greeting file is to be associated with is active or not active
  - `ciUserId` (string): Id of the Agent in common identity with whom this greeting file is to be associated with.
  - `greetingPurposeId` (string): Id of the greeting purpose
  - `greetingPurposeName` (string): Name of the greeting purpose
  - `audioFile` (string): Audio File.
  - `createdTime` (integer): This is the created time of the entity.
  - `lastUpdatedTime` (integer): This is the updated time of the entity.
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
