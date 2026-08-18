---
doc_id: webex-contact-center-post-organization-orgid-holiday-list
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/holiday-list
operation_id: createConfigHolidayList
tags: Holiday List
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.762908+00:00
---

# POST /organization/{orgid}/holiday-list

**API:** Webex Contact Center
**Área:** Holiday List
**operationId:** `createConfigHolidayList`

## Resumen
Create a new Holiday List

## Descripción
Create a new Holiday List in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): Enter a name for the holiday list. Long. max: 80.
- `description` (string): (Optional) Enter a description of the holiday list. Long. max: 255.
- `holidays` (array) (**requerido**): Holiday list.
  - `name` (string) (**requerido**): Name. Long. max: 80.
  - `startDate` (string): Start Date.
  - `endDate` (string): End Date.
  - `startTime` (string): Start Time.
  - `endTime` (string): End Time.
  - `frequency` (string): Frequency. Valores: DontRepeat, Daily, Weekly, Monthly, Yearly.
  - `recurrence` (object):
    - `interval` (integer/int32) (**requerido**):
    - `occurrenceInTheMonth` (string):  Valores: FIRST, SECOND, THIRD, FOURTH, LAST.
    - `daysOfWeek` (array):
    - `specificDayOfMonth` (integer/int32):
    - `specificMonth` (string):  Valores: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC.
    - `endDate` (string):
  - `overlapsWith` (array): (Optional) Used to list the overlapping holidays.
- `holidaysCount` (integer/int64): Holidays Count.
- `createdTime` (integer/int64): This is the created time of the entity.
- `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/holiday-list' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"holidays": [], "name": "<name>"}'
```

## Respuestas correctas
**201**: Created
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): Enter a name for the holiday list. Long. max: 80.
- `description` (string): (Optional) Enter a description of the holiday list. Long. max: 255.
- `holidays` (array) (**requerido**): Holiday list.
  - `name` (string) (**requerido**): Name. Long. max: 80.
  - `startDate` (string): Start Date.
  - `endDate` (string): End Date.
  - `startTime` (string): Start Time.
  - `endTime` (string): End Time.
  - `frequency` (string): Frequency. Valores: DontRepeat, Daily, Weekly, Monthly, Yearly.
  - `recurrence` (object):
    - `interval` (integer/int32) (**requerido**):
    - `occurrenceInTheMonth` (string):  Valores: FIRST, SECOND, THIRD, FOURTH, LAST.
    - `daysOfWeek` (array):
    - `specificDayOfMonth` (integer/int32):
    - `specificMonth` (string):  Valores: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC.
    - `endDate` (string):
  - `overlapsWith` (array): (Optional) Used to list the overlapping holidays.
- `holidaysCount` (integer/int64): Holidays Count.
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