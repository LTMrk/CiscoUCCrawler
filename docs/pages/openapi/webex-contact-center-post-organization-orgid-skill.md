---
doc_id: webex-contact-center-post-organization-orgid-skill
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/skill
operation_id: createConfigSkill
tags: Skill
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.109761+00:00
---

# POST /organization/{orgid}/skill

**API:** Webex Contact Center
**Área:** Skill
**operationId:** `createConfigSkill`

## Resumen
Create a new Skill

## Descripción
Create a new Skill in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): Indicates the name of the skill. Once created, name cannot be modified. Long. max: 80.
- `description` (string): Indicates the description of the skill. Long. max: 255.
- `serviceLevelThreshold` (integer/int32) (**requerido**): Allows to set the time that a customer request can be in a queue before the system flags it as outside the service level.    If the agent completes a customer service request within this time interval, the system considers it within the service level.  It is required only for a create or an update operation.
- `enumSkillValues` (array): List of Enum Skill Values.
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) (**requerido**): Indicates the name of the enumSkillValue. Long. max: 80.
  - `description` (string): Indicates the description of the enumSkillValue. Long. max: 255.
  - `skillId` (string): Represents the skillId of the enumSkillValue.
  - `createdTime` (integer/int64): This is the created time of the entity.
  - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
- `active` (boolean) (**requerido**): Indicates the status of the skill whether it is active(when true) or not active(when false). It is required only during a create or an update operation.
- `dynamicSkill` (boolean): Indicates whether the skill is a dynamic skill or not. Default value is false.
- `skillType` (string) (**requerido**): This can be of the following types  PROFICIENCY: id = 0  BOOLEAN: id = 1  TEXT: id = 2  ENUM: id = 3  Once created, skillType cannot be modified. Valores: Proficiency, Boolean, Text, enum.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `createdTime` (integer/int64): This is the created time of the entity.
- `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

### Ejemplo — petición
```json
{
  "name": "German Speaking",
  "description": "Skill to speak fluent German",
  "serviceLevelThreshold": 0,
  "active": true,
  "skillType": "Boolean"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/skill' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"active": true, "name": "<name>", "serviceLevelThreshold": 0, "skillType": "<skillType>"}'
```

## Respuestas correctas
**201**: Created
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): Indicates the name of the skill. Once created, name cannot be modified. Long. max: 80.
- `description` (string): Indicates the description of the skill. Long. max: 255.
- `serviceLevelThreshold` (integer/int32) (**requerido**): Allows to set the time that a customer request can be in a queue before the system flags it as outside the service level.    If the agent completes a customer service request within this time interval, the system considers it within the service level.  It is required only for a create or an update operation.
- `enumSkillValues` (array): List of Enum Skill Values.
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) (**requerido**): Indicates the name of the enumSkillValue. Long. max: 80.
  - `description` (string): Indicates the description of the enumSkillValue. Long. max: 255.
  - `skillId` (string): Represents the skillId of the enumSkillValue.
  - `createdTime` (integer/int64): This is the created time of the entity.
  - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
- `active` (boolean) (**requerido**): Indicates the status of the skill whether it is active(when true) or not active(when false). It is required only during a create or an update operation.
- `dynamicSkill` (boolean): Indicates whether the skill is a dynamic skill or not. Default value is false.
- `skillType` (string) (**requerido**): This can be of the following types  PROFICIENCY: id = 0  BOOLEAN: id = 1  TEXT: id = 2  ENUM: id = 3  Once created, skillType cannot be modified. Valores: Proficiency, Boolean, Text, enum.
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