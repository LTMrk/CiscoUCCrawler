---
doc_id: webex-contact-center-post-v1-captures-query
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /v1/captures/query
operation_id: downloadMultiRecordingPath
tags: Captures
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.772876+00:00
---

# POST /v1/captures/query

**API:** Webex Contact Center
**Área:** Captures
**operationId:** `downloadMultiRecordingPath`

## Resumen
List Captures

## Descripción
Retrieve a list of Captures given a set of task IDs.

### Captures Availability

Not all tasks will have captures by default and they will be available based on the organization's configurations and retention policy. Querying closed tasks is recommended, as open tasks may return incomplete data.

Transcripts retrieved through this API are post-interaction artifacts.
- For voice, transcripts are available when at least one transcript based configuration/feature is enabled such as Auto CSAT, Agent Well Being, Call Drop Summary, Topics Analytics.

- For digital channels such as Chat, Email, Social, Work Item, and Custom Messaging, transcripts are generated from the conversation messages. Please refer [guide for digital transcripts](/docs/guide-for-digital-transcripts) for more details

### URL Expiry

The maximum duration of validity of pre signed URL or default value when no value is passed for urlExpiration is 60 minutes.

### Authentication & Authorization

This API requires a valid bearer token. The caller must satisfy the scope and role requirements for one of the following:

#### Service App
- **Required Scope:** `cjp:config_read`
- The `orgId` must be provided in the request body and must match the token's org.
- For service app setup, refer to [Contact Center Service Apps](/docs/contact-center-service-apps).

#### Org Admin
- **Required Scopes:** `Identity:SCIM` and `Identity:Organization`
- **Required Role (one of):** `id_full_admin`, `id_readonly_admin`, `cjp.admin`, or `atlas-portal.partner.provision_admin`
- The user must belong to the organization being queried. If `orgId` is provided in the request body, it must match the token's org. If `orgId` is omitted, it is inferred from the token.

#### Partner Admin
- **Required Scope:** `Identity:SCIM` for the managed org
- **Required Role:** `atlas-portal.partner.salesadmin`
- The org ID must be included in the managed org list. This is accomplished by adding the org to the `Managed customer orgs` list in control hub.

#### Supervisor
- **Required Role:** `cjp.supervisor`
- The user must belong to the organization being queried. If `orgId` is provided in the request body, it must match the token's org. If `orgId` is omitted, it is inferred from the token.

**Note:** Please refer to the contact center setup documentation for the configuration details.

## Cuerpo de la petición (application/json)
- `query` (object) (**requerido**):
  - `orgId` (string): Organization ID to use for this operation. If unspecified, inferred from token. Token must have permission to interact with this organization.
  - `urlExpiration` (integer/int32): Expiration time of returned s3 url (in minutes).
  - `taskIds` (array) (**requerido**): Comma separated list of taskIds to gather captures for. Maximum number of taskIds allowed are 10
  - `includeSegments` (boolean): Flag; (true) for individual capture segments of main recording, (false) for a stitched capture.
  - `includeVARecordings` (boolean): Flag; (true) for including virtual agent (VA) recordings, (false) for excluding virtual agent recordings. The default value is false.
  - `includeScreenRecordings` (boolean): Flag; (true) will return screen recording if available else will return empty array, (false) will exclude screen recordings. The default value is false.
  - `includeAllDigitalVersions` (boolean): Flag; (true) returns all available digital transcript artifacts for each requested task, including both legacy and schema-versioned digital transcript artifacts when both exist. (false) or omitted returns the default Captures behavior. This field applies only to digital transcript artifacts and does not change recording or voice transcript retrieval.

## Ejemplo de invocación
```bash
curl -X POST '/v1/captures/query' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"query": {}}'
```

## Respuestas correctas
**200**: Returns Recording and Transcription details. If a provided taskId is not found for the specified organization, the API will return a 200 OK response with empty recording and transcription fields for that task.
This behavior is intentional to allow partial results when multiple taskIds are provided; unmatched taskIds do not result in a 4xx error.
- `meta` (object) (**requerido**):
  - `orgId` (string/uuid): Organization ID used for this operation.
  - `urlExpiration` (integer/int32): Number of minutes (from now) when the signed url expires.
- `data` (array) (**requerido**):
  - `taskId` (string/uuid): The ID of the task.
  - `recording` (array) (**requerido**):
    - `id` (string): The ID of the recording.
    - `segment` (boolean): Flag; Indicates if this is the entire recording or only a segment of main recording. This flag will be always false for consult callType.
    - `attributes` (object) (**requerido**):
      - `fileName` (string): The file name of the recording.
      - `filePath` (string): Capture download url.
      - `startTime` (integer/int64): Begin time of capture(epoch timestamp)
      - `stopTime` (integer/int64): End time of capture(epoch timestamp).
      - `participants` (array): Comma separated list of CI user Id (UUID) of agents, masked customer contact email/phone details and virtual agent id if any involved in the recording.
      - `channel1` (string): Caller - channel contains caller audio only, Agent - channel contains agent audio only for main call and its segments, VA - channel contains virtual agent audio only.
      - `channel2` (string): Agent if callType is consult. For main callType, Agent/Caller/VA/Others based on number of participants.
      - `callType` (string): main if recording belongs to main call; consult if recording belongs to consult call; va-main if recording belongs to virtual agent in main call; va-consult if recording belongs to virtual agent in consult call.
      - `sensitive` (boolean): Applicable only to virtual agent recordings. Flag; (true) indicates the virtual agent recording may contain sensitive information, (false) otherwise.
  - `transcription` (array) (**requerido**):
    - `Source` (string): Source of the transcription
    - `Provider` (string): Provider of the generated transcription
    - `id` (string): Voice Channel Transcript: Ccai ConfigId, Digital Channel Transcript: Conversation Id
    - `fileName` (string): The file name of the transcript.
    - `filePath` (string): Capture download url. Please refer [Transcript Details Guide](/docs/digital-transcript-json-details) for more details.
    - `startTime` (string): Begin time of capture(epoch timestamp)
    - `languageCode` (string): Language of the transcript
    - `createTime` (string): Create time of capture(epoch timestamp)
  - `screenRecordings` (array):
    - `id` (string) (**requerido**): The ID of the screen recording.
    - `attributes` (object) (**requerido**):
      - `fileName` (string) (**requerido**): The file name of the screen recording.
      - `filePath` (string) (**requerido**): Screen recording download URL.
      - `startTime` (integer/int64) (**requerido**): Begin time of screen recording (epoch timestamp)
      - `stopTime` (integer/int64) (**requerido**): End time of screen recording (epoch timestamp).
      - `agentId` (string) (**requerido**): The ID of the agent whose screen was recorded.
      - `screenId` (string) (**requerido**): The ID of the screen being recorded.

## Respuestas de error
- **400**: Error: urlExpiration should be greater than 0.
- **401**: Unauthorized, token is invalid
- **403**: Forbidden From Accessing Resources
- **404**: Not Found
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs