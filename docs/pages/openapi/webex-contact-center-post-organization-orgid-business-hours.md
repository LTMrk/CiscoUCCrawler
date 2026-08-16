---
doc_id: webex-contact-center-post-organization-orgid-business-hours
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/business-hours
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.924460+00:00
---

# POST /organization/{orgid}/business-hours

**API:** Webex Contact Center
**Área:** Business Hour
**operationId:** `createConfigBusinessHours`

## Resumen
Create a new Business Hours resource

## Descripción
Create a new Business Hours resource in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) **(requerido)**: Enter a name for the agent profile.
- `description` (string): (Optional) Enter a description of the profile.
- `timezone` (string) **(requerido)**: The time zone that you provision for your business hour.
- `workingHours` (array) **(requerido)**: Working hours
  - `name` (string) **(requerido)**: Name.
  - `days` (array) **(requerido)**: List of Days.
  - `startTime` (string): Start Time.
  - `endTime` (string): End Time.
- `holidaysId` (string): Holidays Id.
- `overridesId` (string): Overrides Id.
- `workingHoursCount` (integer): Working Hours Count.
- `createdTime` (integer): This is the created time of the entity.
- `lastUpdatedTime` (integer): This is the updated time of the entity.

## Respuestas
- **201**: Created
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: Enter a name for the agent profile.
  - `description` (string): (Optional) Enter a description of the profile.
  - `timezone` (string) **(requerido)**: The time zone that you provision for your business hour.
  - `workingHours` (array) **(requerido)**: Working hours
    - `name` (string) **(requerido)**: Name.
    - `days` (array) **(requerido)**: List of Days.
    - `startTime` (string): Start Time.
    - `endTime` (string): End Time.
  - `holidaysId` (string): Holidays Id.
  - `overridesId` (string): Overrides Id.
  - `workingHoursCount` (integer): Working Hours Count.
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
