---
doc_id: webex-contact-center-post-organization-orgid-auxiliary-code
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/auxiliary-code
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.931888+00:00
---

# POST /organization/{orgid}/auxiliary-code

**API:** Webex Contact Center
**Área:** Auxiliary Code
**operationId:** `createConfig_23`

## Resumen
Create a new Auxiliary Code

## Descripción
Create a new Auxiliary Code in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) **(requerido)**: A name for the code.
- `description` (string): A short description indicating the context of the code.
- `defaultCode` (boolean) **(requerido)**: Indicates whether this is the default code(true) or not(false).  If this is the first idle or wrap-up code for your organization,it must be the default. It can be made non-default later once more codes are created.
- `active` (boolean) **(requerido)**: Indicates whether the code is active(when true) or not active(when false).   It is required only during a create or an update operation.
- `isSystemCode` (boolean): Indicates whether this is the system default code(true) or not(false).
- `workTypeId` (string) **(requerido)**: Indicates the work type id associated with this code.
- `workTypeCode` (string) **(requerido)**: Indicates the work type associated with this code. Valores: IDLE_CODE, WRAP_UP_CODE.
- `burnoutInclusion` (string): Indicates the idle code Inclusion status for agent burnout calculation. Default value is 'INCLUDED' for idle codes and 'NOT_APPLICABLE' for wrap up codes. Valores: NOT_APPLICABLE, EXCLUDED, INCLUDED.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `createdTime` (integer): Creation time(in epoch millis) of this resource.
- `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.

## Respuestas
- **201**: Created
  - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: A name for the code.
  - `description` (string): A short description indicating the context of the code.
  - `defaultCode` (boolean) **(requerido)**: Indicates whether this is the default code(true) or not(false).  If this is the first idle or wrap-up code for your organization,it must be the default. It can be made non-default later once more codes are created.
  - `active` (boolean) **(requerido)**: Indicates whether the code is active(when true) or not active(when false).   It is required only during a create or an update operation.
  - `isSystemCode` (boolean): Indicates whether this is the system default code(true) or not(false).
  - `workTypeId` (string) **(requerido)**: Indicates the work type id associated with this code.
  - `workTypeCode` (string) **(requerido)**: Indicates the work type associated with this code. Valores: IDLE_CODE, WRAP_UP_CODE.
  - `burnoutInclusion` (string): Indicates the idle code Inclusion status for agent burnout calculation. Default value is 'INCLUDED' for idle codes and 'NOT_APPLICABLE' for wrap up codes. Valores: NOT_APPLICABLE, EXCLUDED, INCLUDED.
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not
  - `createdTime` (integer): Creation time(in epoch millis) of this resource.
  - `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
