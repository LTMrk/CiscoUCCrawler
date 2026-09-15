---
doc_id: webex-contact-center-get-organization-orgid-v2-channel
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/v2/channel
operation_id: getAllConfigWithMetaDataChannel
tags: Channel
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-15T15:08:16.247920+00:00
---

# GET /organization/{orgid}/v2/channel

**API:** Webex Contact Center
**Área:** Channel
**operationId:** `getAllConfigWithMetaDataChannel`

## Resumen
List Channels

## Descripción
Retrieve a list of Channels in a given organization. Supports pagination metadata. Set includeLogoUrlVersioned to true to include logoUrlVersioned in the response. Note: Returning array fields in the List (Get All) API response is deprecated. To retrieve the complete resource with all fields, please use the Get-by-ID API instead.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Filter expression
- `attributes` [query] (string/string): Supported attributes
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(name)  The examples below show some search queries - "Cisco" - field=="name";value=="Cisco" - fields=in=("name");value=="Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.
- `sort` [query] (string): Sortable properties Por defecto: name.
- `includeCount` [query] (boolean): If set to true, the API response includes the asset count. Por defecto: False.
- `singleObjectResponse` [query] (boolean): Specify whether to include array fields in the response. This query parameter should be used only when the response contains a single record. It is not supported for responses with multiple objects and throws an exception. Por defecto: False.
- `includeLogoUrlVersioned` [query] (boolean): Include logoUrlVersioned in the response. Por defecto: False.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/v2/channel' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `meta` (object): Additional properties for Meta.
- `data` (array): List of Data.
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string): Enter a name for the agent profile. Long. max: 80.
  - `description` (string): Channel description Long. max: 255.
  - `channelType` (string): Type of channel Valores: TELEPHONY, EMAIL, FAX, CHAT, VIDEO, OTHERS, SOCIAL_CHANNEL, WORK_ITEM, CUSTOM_MESSAGING.
  - `logoType` (string): Type of logo. Use MOMENTUM to reference a Momentum icon by name, or LOGO_URL to upload a binary image file. Valores: MOMENTUM, LOGO_URL.
  - `logoIconName` (string): Momentum icon name (required when logoType is MOMENTUM) Long. max: 100.
  - `logoUrl` (string) (solo lectura): Public CDN URL of the uploaded logo image (read-only — populated by the server after upload when logoType is LOGO_URL). Do not supply this field on create/update; send the binary image as the 'logoFile' multipart part instead.
  - `logoUrlVersioned` (string) (solo lectura): Versioned CDN URL of the uploaded logo image — stored without Cache-Control so CloudFront always fetches the latest binary immediately (read-only, populated by the server alongside logoUrl).
  - `numberOfAsset` (integer/int64): Number of assets using this channel
  - `createdTime` (integer/int64): This is the created time of the entity.
  - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

### Ejemplo — respuesta 200
```json
{
  "data": [
    {
      "logoIconName": "momentumIconName",
      "logoUrlVersioned": "https://wxcc-config-resource-nonprod-cdn.ciscoccservice.com/org-id/channel-logo/versioned/uuid.png",
      "description": "Channel Desc",
      "channelType": "WORK_ITEM",
      "version": 1,
      "logoUrl": "https://wxcc-config-resource-nonprod-cdn.ciscoccservice.com/org-id/channel-logo/uuid.png",
      "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
      "numberOfAsset": 5,
      "name": "Agent-Profile(Auto WrapUp)",
      "createdTime": 123456789,
      "lastUpdatedTime": 123456789,
      "id": "93912f11-6017-404b-bf14-5331890b1797",
      "logoType": "MOMENTUM"
    }
  ],
  "meta": {
    "additionalProp2": "string",
    "additionalProp3": "string",
    "additionalProp1": "string"
  }
}
```

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