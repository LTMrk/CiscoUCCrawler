---
doc_id: webex-contact-center-put-organization-orgid-auxiliary-code-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PUT
path: /organization/{orgid}/auxiliary-code/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.932613+00:00
---

# PUT /organization/{orgid}/auxiliary-code/{id}

**API:** Webex Contact Center
**Área:** Auxiliary Code
**operationId:** `updateConfig_24`

## Resumen
Update specific Auxiliary Code by ID

## Descripción
Update an existing Auxiliary Code by ID in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Auxiliary Code.

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
- **200**: OK
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
- **404**: Resource not found or URI is invalid
- **412**: Resource referred in other entity(s). Please get all the reference entities info by invoking Get incoming-references api.
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
