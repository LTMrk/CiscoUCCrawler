---
doc_id: webex-contact-center-post-organization-orgid-dial-number
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/dial-number
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.939909+00:00
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
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `dialledNumber` (string): The dialed number(DN) used to map to entry points.
- `extension` (string): The extension used to map to entry points.
- `routingPrefix` (string): The routing prefix is mapped to a location and can be prefixed with an extension
- `esn` (string): The esn is routing prefix with extension
- `routePointId` (string): The identifier of a route point of WxC which is similar to entry point of WxCC
- `entryPointId` (string) **(requerido)**: The identifier of an entry point to which you want to map the DN.
- `entryPointName` (string) **(requerido)**: The entryPoint name of the entryPointId.
- `defaultAni` (boolean): The default dial number for the tenant to make outdial calls. The default dial number is displayed in the customer's caller ID, if an agent does not select a specific outdial ANI (Automatic Number Identification) for an outdial call.  A default value is automatically set once and entry point mapping is created
- `location` (string): The ID of the location as configured on Webex Calling(applicable only for Webex Calling).
- `regionId` (string): Specify the telephony region id.  You can pass id for one of these regions:  US (USA), CA (Canada), MX (Mexico), AU (Australia), SG (Singapore), GB (United Kingdom), DE (Germany)  You can retrieve it by calling /api/global/telephony-region API.
- `createdTime` (integer): This is the created time of the entity.
- `lastUpdatedTime` (integer): This is the updated time of the entity.
- `dialledNumberDigits` (string):

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `dialledNumber` (string): The dialed number(DN) used to map to entry points.
  - `extension` (string): The extension used to map to entry points.
  - `routingPrefix` (string): The routing prefix is mapped to a location and can be prefixed with an extension
  - `esn` (string): The esn is routing prefix with extension
  - `routePointId` (string): The identifier of a route point of WxC which is similar to entry point of WxCC
  - `entryPointId` (string) **(requerido)**: The identifier of an entry point to which you want to map the DN.
  - `entryPointName` (string) **(requerido)**: The entryPoint name of the entryPointId.
  - `defaultAni` (boolean): The default dial number for the tenant to make outdial calls. The default dial number is displayed in the customer's caller ID, if an agent does not select a specific outdial ANI (Automatic Number Identification) for an outdial call.  A default value is automatically set once and entry point mapping is created
  - `location` (string): The ID of the location as configured on Webex Calling(applicable only for Webex Calling).
  - `regionId` (string): Specify the telephony region id.  You can pass id for one of these regions:  US (USA), CA (Canada), MX (Mexico), AU (Australia), SG (Singapore), GB (United Kingdom), DE (Germany)  You can retrieve it by calling /api/global/telephony-region API.
  - `createdTime` (integer): This is the created time of the entity.
  - `lastUpdatedTime` (integer): This is the updated time of the entity.
  - `dialledNumberDigits` (string):
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
