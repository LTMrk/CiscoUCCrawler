---
doc_id: webex-contact-center-post-organization-orgid-holiday-list
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/holiday-list
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.925398+00:00
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
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) **(requerido)**: Enter a name for the holiday list.
- `description` (string): (Optional) Enter a description of the holiday list.
- `holidays` (array) **(requerido)**: Holiday list.
  - `name` (string) **(requerido)**: Name.
  - `startDate` (string): Start Date.
  - `endDate` (string): End Date.
  - `startTime` (string): Start Time.
  - `endTime` (string): End Time.
  - `frequency` (string): Frequency. Valores: DontRepeat, Daily, Weekly, Monthly, Yearly.
  - `recurrence` (object):
    - `interval` (integer) **(requerido)**:
    - `occurrenceInTheMonth` (string):  Valores: FIRST, SECOND, THIRD, FOURTH, LAST.
    - `daysOfWeek` (array):
    - `specificDayOfMonth` (integer):
    - `specificMonth` (string):  Valores: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC.
    - `endDate` (string):
  - `overlapsWith` (array): (Optional) Used to list the overlapping holidays.
- `holidaysCount` (integer): Holidays Count.
- `createdTime` (integer): This is the created time of the entity.
- `lastUpdatedTime` (integer): This is the updated time of the entity.

## Respuestas
- **201**: Created
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: Enter a name for the holiday list.
  - `description` (string): (Optional) Enter a description of the holiday list.
  - `holidays` (array) **(requerido)**: Holiday list.
    - `name` (string) **(requerido)**: Name.
    - `startDate` (string): Start Date.
    - `endDate` (string): End Date.
    - `startTime` (string): Start Time.
    - `endTime` (string): End Time.
    - `frequency` (string): Frequency. Valores: DontRepeat, Daily, Weekly, Monthly, Yearly.
    - `recurrence` (object):
      - `interval` (integer) **(requerido)**:
      - `occurrenceInTheMonth` (string):  Valores: FIRST, SECOND, THIRD, FOURTH, LAST.
      - `daysOfWeek` (array):
      - `specificDayOfMonth` (integer):
      - `specificMonth` (string):  Valores: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC.
      - `endDate` (string):
    - `overlapsWith` (array): (Optional) Used to list the overlapping holidays.
  - `holidaysCount` (integer): Holidays Count.
  - `createdTime` (integer): This is the created time of the entity.
  - `lastUpdatedTime` (integer): This is the updated time of the entity.
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
