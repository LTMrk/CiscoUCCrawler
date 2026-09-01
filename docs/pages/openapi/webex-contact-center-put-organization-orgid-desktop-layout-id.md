---
doc_id: webex-contact-center-put-organization-orgid-desktop-layout-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PUT
path: /organization/{orgid}/desktop-layout/{id}
operation_id: updateConfig_14
tags: Desktop Layout
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.659072+00:00
---

# PUT /organization/{orgid}/desktop-layout/{id}

**API:** Webex Contact Center
**Área:** Desktop Layout
**operationId:** `updateConfig_14`

## Resumen
Update specific Desktop Layout by ID

## Descripción
Update an existing Desktop Layout by ID in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): Resource ID of the Desktop Layout.

## Cuerpo de la petición (application/json)
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): A name for the Desktop Layout. Long. max: 255.
- `description` (string): A short description indicating the context of the Desktop Layout. Long. max: 255.
- `editedBy` (string) (**requerido**): Indicates who modified the Desktop Layout. Long. max: 255.
- `jsonFileName` (string) (**requerido**): Enter the name of the file. Long. max: 255.
- `jsonFileContent` (string) (**requerido**): Enter the Desktop Layout json.
- `global` (boolean) (**requerido**): Indicates if the Desktop Layout is a global layout or a custom layout.
- `status` (boolean) (**requerido**): Indicates if the Desktop Layout is in active state or inactive.
- `defaultJsonModified` (boolean) (**requerido**): Indicates if the default Desktop Layout is modified.
- `validated` (boolean) (**requerido**): Indicates if the Desktop Layout is validated.
- `validatedTime` (integer/int64): Validated time(in epoch milliseconds) of this resource.
- `defaultJsonModifiedTime` (integer/int64): Default Json Modified time(in epoch milliseconds) of this resource.
- `modifiedTime` (integer/int64): Modified time(in epoch milliseconds) of this resource.
- `teamIds` (array): Specify the teams id to assign to this Desktop Layout.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `createdTime` (integer/int64): This is the created time of the entity.
- `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

## Ejemplo de invocación
```bash
curl -X PUT '/organization/<orgid>/desktop-layout/<id>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"defaultJsonModified": true, "editedBy": "<editedBy>", "global": true, "jsonFileContent": "<jsonFileContent>", "jsonFileName": "<jsonFileName>", "name": "<name>"}'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): A name for the Desktop Layout. Long. max: 255.
- `description` (string): A short description indicating the context of the Desktop Layout. Long. max: 255.
- `editedBy` (string) (**requerido**): Indicates who modified the Desktop Layout. Long. max: 255.
- `jsonFileName` (string) (**requerido**): Enter the name of the file. Long. max: 255.
- `jsonFileContent` (string) (**requerido**): Enter the Desktop Layout json.
- `global` (boolean) (**requerido**): Indicates if the Desktop Layout is a global layout or a custom layout.
- `status` (boolean) (**requerido**): Indicates if the Desktop Layout is in active state or inactive.
- `defaultJsonModified` (boolean) (**requerido**): Indicates if the default Desktop Layout is modified.
- `validated` (boolean) (**requerido**): Indicates if the Desktop Layout is validated.
- `validatedTime` (integer/int64): Validated time(in epoch milliseconds) of this resource.
- `defaultJsonModifiedTime` (integer/int64): Default Json Modified time(in epoch milliseconds) of this resource.
- `modifiedTime` (integer/int64): Modified time(in epoch milliseconds) of this resource.
- `teamIds` (array): Specify the teams id to assign to this Desktop Layout.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
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