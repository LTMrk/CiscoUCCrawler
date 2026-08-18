---
doc_id: webex-contact-center-post-organization-orgid-agent-personal-greeting
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/agent-personal-greeting
operation_id: createConfigAgentPersonalGreeting
tags: Agent Personal Greeting Files
deprecated: true
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.771948+00:00
---

# POST /organization/{orgid}/agent-personal-greeting

> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.

**API:** Webex Contact Center
**Área:** Agent Personal Greeting Files
**operationId:** `createConfigAgentPersonalGreeting`

## Resumen
Create a new Greeting File

## Descripción
Create a new Greeting File in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `agentPersonalGreetingInfo` (object) (**requerido**): Agent Personal Greeting Agent Personal Greetings With Attribute Tag schema.
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) (**requerido**): A name for the Agent's personal greeting file. It should have valid extension i.e. .wav Long. max: 80.
  - `contentType` (string) (**requerido**): Indicates Content-Type of the Audio file. It can take one of these values: AUDIO_WAV, AUDIO_X_WAV Valores: AUDIO_WAV, TEXT_HTML, TEXT_PHP, AUDIO_X_WAV, APPLICATION_OCTET_STREAM.
  - `blobId` (string): Identifier for the audio file.
  - `url` (string/url): Audio file download url.
  - `agentId` (string) (**requerido**): Agent Id with which this greeting file is to be associated with.
  - `attributeTag` (string): This is used to identify the purpose of a greeting. Long. max: 80.
  - `firstName` (string): First Name of the Agent with whom this greeting file is to be associated with.
  - `lastName` (string): Last Name of the Agent with whom this greeting file is to be associated with.
  - `email` (string): Email of the Agent with whom this greeting file is to be associated with.
  - `agentActive` (boolean): Indicates whether the Agent with whom this greeting file is to be associated with is active or not active
  - `ciUserId` (string): Id of the Agent in common identity with whom this greeting file is to be associated with.
  - `audioFile` (string/binary): Audio File.
  - `createdTime` (integer/int64): This is the created time of the entity.
  - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
- `audioFile` (string/binary) (**requerido**):

## Cuerpo de la petición (multipart/form-data)
- `agentPersonalGreetingInfo` (object) (**requerido**): Agent Personal Greeting Agent Personal Greetings With Attribute Tag schema.
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) (**requerido**): A name for the Agent's personal greeting file. It should have valid extension i.e. .wav Long. max: 80.
  - `contentType` (string) (**requerido**): Indicates Content-Type of the Audio file. It can take one of these values: AUDIO_WAV, AUDIO_X_WAV Valores: AUDIO_WAV, TEXT_HTML, TEXT_PHP, AUDIO_X_WAV, APPLICATION_OCTET_STREAM.
  - `blobId` (string): Identifier for the audio file.
  - `url` (string/url): Audio file download url.
  - `agentId` (string) (**requerido**): Agent Id with which this greeting file is to be associated with.
  - `attributeTag` (string): This is used to identify the purpose of a greeting. Long. max: 80.
  - `firstName` (string): First Name of the Agent with whom this greeting file is to be associated with.
  - `lastName` (string): Last Name of the Agent with whom this greeting file is to be associated with.
  - `email` (string): Email of the Agent with whom this greeting file is to be associated with.
  - `agentActive` (boolean): Indicates whether the Agent with whom this greeting file is to be associated with is active or not active
  - `ciUserId` (string): Id of the Agent in common identity with whom this greeting file is to be associated with.
  - `audioFile` (string/binary): Audio File.
  - `createdTime` (integer/int64): This is the created time of the entity.
  - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
- `audioFile` (string/binary) (**requerido**):

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/agent-personal-greeting' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"agentPersonalGreetingInfo": {}, "audioFile": "<audioFile>"}'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): A name for the Agent's personal greeting file. It should have valid extension i.e. .wav Long. max: 80.
- `contentType` (string) (**requerido**): Indicates Content-Type of the Audio file. It can take one of these values: AUDIO_WAV, AUDIO_X_WAV Valores: AUDIO_WAV, TEXT_HTML, TEXT_PHP, AUDIO_X_WAV, APPLICATION_OCTET_STREAM.
- `blobId` (string): Identifier for the audio file.
- `url` (string/url): Audio file download url.
- `agentId` (string) (**requerido**): Agent Id with which this greeting file is to be associated with.
- `attributeTag` (string): This is used to identify the purpose of a greeting. Long. max: 80.
- `firstName` (string): First Name of the Agent with whom this greeting file is to be associated with.
- `lastName` (string): Last Name of the Agent with whom this greeting file is to be associated with.
- `email` (string): Email of the Agent with whom this greeting file is to be associated with.
- `agentActive` (boolean): Indicates whether the Agent with whom this greeting file is to be associated with is active or not active
- `ciUserId` (string): Id of the Agent in common identity with whom this greeting file is to be associated with.
- `audioFile` (string/binary): Audio File.
- `createdTime` (integer/int64): This is the created time of the entity.
- `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

## Respuestas de error
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "400",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "400",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **401**: Unauthorized Operation
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "401",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "401",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **403**: Operation is forbidden
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "403",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "403",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **409**: Similar entity is already present
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "409",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "409",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "429",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "429",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **500**: An Unexpected Error Occurred
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "500",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "500",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs