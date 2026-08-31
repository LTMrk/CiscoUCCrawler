---
doc_id: webex-contact-center-post-organization-orgid-dial-plan
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/dial-plan
operation_id: createConfigDialPlan
tags: Dial Plan
deprecated: true
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.091370+00:00
---

# POST /organization/{orgid}/dial-plan

> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.

**API:** Webex Contact Center
**Área:** Dial Plan
**operationId:** `createConfigDialPlan`

## Resumen
Create a new Dial Plan

## Descripción
Create a new Dial Plan in a given organization.

**Deprecated:** Dial Plan configuration is deprecated. Dial Plan is no longer available as an Agent Profile setting, so agents can no longer  use them for agent dial number validation.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): Enter the name for the dial plan. Long. max: 80.
- `description` (string): A short description of the dial plan. Long. max: 255.
- `regularExpression` (string) (**requerido**): A regular expression specifies the format of the phone number and the characters that you can use while dialing a number. Long. max: 255.
- `prefix` (string): (Optional) Enter a prefix that the system automatically adds to the phone number that the agent enters. For example, digit 1 for long-distance calls within the United States. Long. max: 50.
- `strippedChars` (string): Enter the characters that system removes from the phone number that the agent dials.For example, left and right parentheses, space, and hyphen. Long. max: 128.
- `active` (boolean) (**requerido**): Specify whether the dial plan is active or not
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `createdTime` (integer/int64): This is the created time of the entity.
- `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/dial-plan' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"active": true, "name": "<name>", "regularExpression": "<regularExpression>"}'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): Enter the name for the dial plan. Long. max: 80.
- `description` (string): A short description of the dial plan. Long. max: 255.
- `regularExpression` (string) (**requerido**): A regular expression specifies the format of the phone number and the characters that you can use while dialing a number. Long. max: 255.
- `prefix` (string): (Optional) Enter a prefix that the system automatically adds to the phone number that the agent enters. For example, digit 1 for long-distance calls within the United States. Long. max: 50.
- `strippedChars` (string): Enter the characters that system removes from the phone number that the agent dials.For example, left and right parentheses, space, and hyphen. Long. max: 128.
- `active` (boolean) (**requerido**): Specify whether the dial plan is active or not
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