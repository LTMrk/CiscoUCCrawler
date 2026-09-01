---
doc_id: webex-contact-center-patch-organization-orgid-user-bulk-update-dynamic-skill-skillid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PATCH
path: /organization/{orgid}/user/bulk/update-dynamic-skill/{skillId}
operation_id: patchDynamicSkillsUser
tags: Users
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.693115+00:00
---

# PATCH /organization/{orgid}/user/bulk/update-dynamic-skill/{skillId}

**API:** Webex Contact Center
**Área:** Users
**operationId:** `patchDynamicSkillsUser`

## Resumen
Bulk partial update Users with dynamic skills

## Descripción
Assign or unassign a dynamic skill to/from multiple users in bulk for a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `skillId` [path] (string) (**requerido**): Dynamic skill ID used for bulk update

## Cuerpo de la petición (application/json)
- `items` (array): List of items in the bulk request.
  - `itemIdentifier` (integer/int32): Unique item identifier for a bulk operation.
  - `item` (object): Data transfer object for updating dynamic skills assigned to a user
    - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `userId` (string): The unique identifier of the user whose dynamic skills are being updated
    - `enumSkillValues` (array): Set of enumerated skill values for enum-type dynamic skills
    - `textValue` (string): Text value for text-type dynamic skills (maximum 100 characters) Long. max: 100.
    - `booleanValue` (boolean): Boolean value for boolean-type dynamic skills
    - `proficiencyValue` (integer/int32): Proficiency value for proficiency-type dynamic skills (range: 0-10)
    - `skillId` (string): The unique identifier of the dynamic skill being updated
    - `createdTime` (integer/int64): This is the created time of the entity.
    - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
  - `requestAction` (string): Identifier for action type. Possible values are `SAVE` and `DELETE`.

## Ejemplo de invocación
```bash
curl -X PATCH '/organization/<orgid>/user/bulk/update-dynamic-skill/<skillId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**207**: Multi-Status
- `items` (array):
  - `itemIdentifier` (integer/int32): Unique item identifier for a bulk operation.
  - `status` (integer/int32): Indicates the error status code.
  - `operationType` (string): The kind of operation desired of an entity. Valores: CREATE, UPDATE, DELETE, GET.
  - `href` (string): The resource URI of an entity.
  - `apiError` (object): Response body for an API error.
    - `trackingId` (string): An opaque identifier for mapping protocol failures to service internal codes.   When specified in a request, it can be used for co-relating events across services
    - `error` (object): Details of an error.
      - `key` (string): An application defined error code.
      - `message` (array): A message providing details about the error.
        - `description` (string): A human readable explanation for the occurrence of an error.
- `items` (array):
  - `itemIdentifier` (integer/int32): Unique item identifier for a bulk operation.
  - `status` (integer/int32): Indicates the error status code.
  - `operationType` (string): The kind of operation desired of an entity. Valores: CREATE, UPDATE, DELETE, GET.
  - `href` (string): The resource URI of an entity.
  - `apiError` (object): Response body for an API error.
    - `trackingId` (string): An opaque identifier for mapping protocol failures to service internal codes.   When specified in a request, it can be used for co-relating events across services
    - `error` (object): Details of an error.
      - `key` (string): An application defined error code.
      - `message` (array): A message providing details about the error.
        - `description` (string): A human readable explanation for the occurrence of an error.

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