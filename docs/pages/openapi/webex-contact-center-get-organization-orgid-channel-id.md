---
doc_id: webex-contact-center-get-organization-orgid-channel-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/channel/{id}
operation_id: getConfigChannel
tags: Channel
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-17T19:59:29.844058+00:00
---

# GET /organization/{orgid}/channel/{id}

**API:** Webex Contact Center
**Área:** Channel
**operationId:** `getConfigChannel`

## Resumen
Get specific Channel by ID

## Descripción
Retrieve an existing Channel by ID in a given organization. Set includeLogoUrlVersioned to true to include logoUrlVersioned in the response.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): Resource ID of the Channel
- `includeLogoUrlVersioned` [query] (boolean): Include logoUrlVersioned in the response. Por defecto: False.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/channel/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): Enter a name for the agent profile. Long. max: 80.
- `description` (string): Channel description Long. max: 255.
- `channelType` (string) (**requerido**): Type of channel Valores: TELEPHONY, EMAIL, FAX, CHAT, VIDEO, OTHERS, SOCIAL_CHANNEL, WORK_ITEM, CUSTOM_MESSAGING.
- `logoType` (string) (**requerido**): Type of logo. Use MOMENTUM to reference a Momentum icon by name, or LOGO_URL to upload a binary image file. Valores: MOMENTUM, LOGO_URL.
- `logoIconName` (string): Momentum icon name (required when logoType is MOMENTUM) Long. max: 100.
- `logoUrl` (string) (solo lectura): Public CDN URL of the uploaded logo image (read-only — populated by the server after upload when logoType is LOGO_URL). Do not supply this field on create/update; send the binary image as the 'logoFile' multipart part instead.
- `logoUrlVersioned` (string) (solo lectura): Versioned CDN URL of the uploaded logo image — stored without Cache-Control so CloudFront always fetches the latest binary immediately (read-only, populated by the server alongside logoUrl).
- `numberOfAsset` (integer/int64): Number of assets using this channel
- `messagingPolicy` (object): Messaging policy configuration for CUSTOM_MESSAGING channels
  - `maxMessageCharacters` (integer/int32) (**requerido**): Maximum number of characters per message (1-20000)
  - `allowFileAttachments` (boolean) (**requerido**): Whether file attachments are allowed
  - `maxNumberOfAttachments` (integer/int32): Maximum number of attachments per message
  - `maxTotalAttachmentSizeMegabytes` (integer/int32): Maximum total attachment size in MB
  - `maxSingleAttachmentSizeMegabytes` (integer/int32): Maximum single attachment size in MB
  - `allowedFileTypes` (object): Allowed file types mapped by file type. Valid file types: 'images', 'videos', 'audio', 'documents', 'others'. Each file type has a predefined list of allowed extensions. Example: {"documents": ["pdf", "docx"], "images": ["jpg", "png"]}
- `createdTime` (integer/int64): This is the created time of the entity.
- `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

## Respuestas de error
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