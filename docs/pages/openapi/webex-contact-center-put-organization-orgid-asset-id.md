---
doc_id: webex-contact-center-put-organization-orgid-asset-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PUT
path: /organization/{orgid}/asset/{id}
operation_id: updateConfigAsset
tags: Asset
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-15T15:08:16.240136+00:00
---

# PUT /organization/{orgid}/asset/{id}

**API:** Webex Contact Center
**Área:** Asset
**operationId:** `updateConfigAsset`

## Resumen
Update specific Asset by ID

## Descripción
Update an existing Asset by ID in a given organization. Supported for WORK_ITEM assets. For CUSTOM_MESSAGING assets, use PATCH instead.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): Resource ID of the Asset

## Cuerpo de la petición (application/json)
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): Enter a name for the agent profile. Long. max: 80.
- `description` (string): Asset description Long. max: 255.
- `channelType` (string) (**requerido**): Type of channel (WORK_ITEM or CUSTOM_MESSAGING) Valores: TELEPHONY, EMAIL, FAX, CHAT, VIDEO, OTHERS, SOCIAL_CHANNEL, WORK_ITEM, CUSTOM_MESSAGING.
- `channelName` (string) (solo lectura): Channel name (read-only, included when includeChannelName=true)
- `channelId` (string) (**requerido**): Channel ID reference
- `businessAddress` (string) (**requerido**): Business address (immutable after creation, max 200 chars, no special JSON chars) Long. max: 200.
- `dataSchema` (array): List of data schema items for the asset. Required for WORK_ITEM channel type. At least one item must have isViewable=true and one must have isRequired=true. Maximum size enforced by config-limit framework (default 50 items).
  - `id` (string) (solo lectura): Unique identifier of the data schema item (auto-generated)
  - `fieldKey` (string) (**requerido**): Unique field identifier key within the asset Long. max: 100.
  - `displayName` (string) (**requerido**): Human-readable display name for the field Long. max: 80.
  - `isViewable` (boolean): Indicates if the field is viewable by agents Por defecto: False.
  - `isRequired` (boolean): Indicates if the field is required for submission Por defecto: False.
- `webhookConfig` (object): Webhook configuration for CUSTOM_MESSAGING assets
  - `webhookUrl` (string): HTTPS webhook URL for receiving events (max 2000 chars, must start with https://). Required on CREATE. On UPDATE, omit to keep existing URL. Long. max: 2000.
  - `webhookSecret` (string) (solo escritura): Secret token for webhook authentication (min 32, max 256 chars). Required on CREATE. On UPDATE, omit to keep existing secret. Write-only — never returned in responses. Long. max: 256.
- `createdTime` (integer/int64): This is the created time of the entity.
- `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

## Ejemplo de invocación
```bash
curl -X PUT '/organization/<orgid>/asset/<id>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"businessAddress": "<businessAddress>", "channelId": "<channelId>", "channelType": "<channelType>", "name": "<name>"}'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): Enter a name for the agent profile. Long. max: 80.
- `description` (string): Asset description Long. max: 255.
- `channelType` (string) (**requerido**): Type of channel (WORK_ITEM or CUSTOM_MESSAGING) Valores: TELEPHONY, EMAIL, FAX, CHAT, VIDEO, OTHERS, SOCIAL_CHANNEL, WORK_ITEM, CUSTOM_MESSAGING.
- `channelName` (string) (solo lectura): Channel name (read-only, included when includeChannelName=true)
- `channelId` (string) (**requerido**): Channel ID reference
- `businessAddress` (string) (**requerido**): Business address (immutable after creation, max 200 chars, no special JSON chars) Long. max: 200.
- `dataSchema` (array): List of data schema items for the asset. Required for WORK_ITEM channel type. At least one item must have isViewable=true and one must have isRequired=true. Maximum size enforced by config-limit framework (default 50 items).
  - `id` (string) (solo lectura): Unique identifier of the data schema item (auto-generated)
  - `fieldKey` (string) (**requerido**): Unique field identifier key within the asset Long. max: 100.
  - `displayName` (string) (**requerido**): Human-readable display name for the field Long. max: 80.
  - `isViewable` (boolean): Indicates if the field is viewable by agents Por defecto: False.
  - `isRequired` (boolean): Indicates if the field is required for submission Por defecto: False.
- `webhookConfig` (object): Webhook configuration for CUSTOM_MESSAGING assets
  - `webhookUrl` (string): HTTPS webhook URL for receiving events (max 2000 chars, must start with https://). Required on CREATE. On UPDATE, omit to keep existing URL. Long. max: 2000.
  - `webhookSecret` (string) (solo escritura): Secret token for webhook authentication (min 32, max 256 chars). Required on CREATE. On UPDATE, omit to keep existing secret. Write-only — never returned in responses. Long. max: 256.
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
- **404**: Resource not found or URI is invalid
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "404",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "404",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **412**: Resource referred in other entity(s). Please get all the reference entities info by invoking Get incoming-references api.
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "412",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "412",
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