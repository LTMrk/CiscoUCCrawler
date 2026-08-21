---
doc_id: webex-contact-center-post-organization-orgid-contact-service-queue-fetch-by-userid-skillprofileid
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/contact-service-queue/fetch-by-userId-skillProfileId
operation_id: getSkillBasedCSQsBySkillProfileIdAndUserIdContactServiceQueue
tags: Contact Service Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.734727+00:00
---

# POST /organization/{orgid}/contact-service-queue/fetch-by-userId-skillProfileId

**API:** Webex Contact Center
**Área:** Contact Service Queue
**operationId:** `getSkillBasedCSQsBySkillProfileIdAndUserIdContactServiceQueue`

## Resumen
List skill-based Contact Service Queues by skill profile ID and user ID

## Descripción
Retrieve a list of skill-based Contact Service Queues associated with the given skill profile ID and user ID combination in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `skillProfileId` (string/uuid): Unique identifier of the skill profile to look up queues for.
- `dynamicSkills` (array): Dynamic skill values used to further narrow down the matching skill-based queues. Used by the dynamic-skills lookup endpoint.
  - `skillId` (string): The unique identifier of the dynamic skill
  - `textValue` (string): Text value for text-type dynamic skills
  - `booleanValue` (boolean): Boolean value for boolean-type dynamic skills
  - `proficiencyValue` (integer/int32): Proficiency value for proficiency-type dynamic skills (range: 0-10)
  - `enumSkillValues` (array): Set of enumerated skill values for enum-type dynamic skills
- `userId` (string/uuid): Unique identifier of the user (agent) whose skill-based queues should be retrieved. Used by the user-and-skill-profile lookup endpoint.

### Ejemplo — petición
```json
{
  "skillProfileId": "af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "userId": "660e0a5a-8230-47d7-ae98-047fb180e1ff",
  "dynamicSkills": [
    {
      "skillId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
      "proficiencyValue": 7
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/contact-service-queue/fetch-by-userId-skillProfileId' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `meta` (object): Additional properties for Meta.
- `data` (array): List of Data.
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string/uuid): Unique identifier of the contact service queue.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `channelType` (string): Channel type of the contact service queue (for example, `TELEPHONY`, `CHAT`, `EMAIL`, `SOCIAL`).
  - `name` (string): Display name of the contact service queue.
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