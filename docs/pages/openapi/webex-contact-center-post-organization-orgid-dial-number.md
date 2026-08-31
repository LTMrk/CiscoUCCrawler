---
doc_id: webex-contact-center-post-organization-orgid-dial-number
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/dial-number
operation_id: createConfig_14
tags: Dial Number
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.694420+00:00
---

# POST /organization/{orgid}/dial-number

**API:** Webex Contact Center
**Área:** Dial Number
**operationId:** `createConfig_14`

## Resumen
Create a new Dialed Number Mapping

## Descripción
Create a new Dialed Number Mapping in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `dialledNumber` (string): The dialed number(DN) used to map to entry points. Long. max: 20.
- `extension` (string): The extension used to map to entry points. Long. max: 10.
- `routingPrefix` (string): The routing prefix is mapped to a location and can be prefixed with an extension Long. max: 7.
- `esn` (string): The esn is routing prefix with extension Long. max: 17.
- `routePointId` (string): The identifier of a route point of WxC which is similar to entry point of WxCC
- `entryPointId` (string) (**requerido**): The identifier of an entry point to which you want to map the DN.
- `entryPointName` (string) (**requerido**): The entryPoint name of the entryPointId.
- `defaultAni` (boolean): The default dial number for the tenant to make outdial calls. The default dial number is displayed in the customer's caller ID, if an agent does not select a specific outdial ANI (Automatic Number Identification) for an outdial call.  A default value is automatically set once and entry point mapping is created
- `location` (string): The ID of the location as configured on Webex Calling(applicable only for Webex Calling).
- `regionId` (string): Specify the telephony region id.  You can pass id for one of these regions:  US (USA), CA (Canada), MX (Mexico), AU (Australia), SG (Singapore), GB (United Kingdom), DE (Germany)  You can retrieve it by calling /api/global/telephony-region API.
- `createdTime` (integer/int64): This is the created time of the entity.
- `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
- `dialledNumberDigits` (string):

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/dial-number' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"entryPointId": "<entryPointId>", "entryPointName": "<entryPointName>"}'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `dialledNumber` (string): The dialed number(DN) used to map to entry points. Long. max: 20.
- `extension` (string): The extension used to map to entry points. Long. max: 10.
- `routingPrefix` (string): The routing prefix is mapped to a location and can be prefixed with an extension Long. max: 7.
- `esn` (string): The esn is routing prefix with extension Long. max: 17.
- `routePointId` (string): The identifier of a route point of WxC which is similar to entry point of WxCC
- `entryPointId` (string) (**requerido**): The identifier of an entry point to which you want to map the DN.
- `entryPointName` (string) (**requerido**): The entryPoint name of the entryPointId.
- `defaultAni` (boolean): The default dial number for the tenant to make outdial calls. The default dial number is displayed in the customer's caller ID, if an agent does not select a specific outdial ANI (Automatic Number Identification) for an outdial call.  A default value is automatically set once and entry point mapping is created
- `location` (string): The ID of the location as configured on Webex Calling(applicable only for Webex Calling).
- `regionId` (string): Specify the telephony region id.  You can pass id for one of these regions:  US (USA), CA (Canada), MX (Mexico), AU (Australia), SG (Singapore), GB (United Kingdom), DE (Germany)  You can retrieve it by calling /api/global/telephony-region API.
- `createdTime` (integer/int64): This is the created time of the entity.
- `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
- `dialledNumberDigits` (string):

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