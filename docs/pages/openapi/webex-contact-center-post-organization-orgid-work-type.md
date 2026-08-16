---
doc_id: webex-contact-center-post-organization-orgid-work-type
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/work-type
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.958118+00:00
---

# POST /organization/{orgid}/work-type

**API:** Webex Contact Center
**Área:** Work Types
**operationId:** `createConfig`

## Resumen
Create a new Work Type

## Descripción
Create a new Work Type in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) **(requerido)**: A name for the Work Type.
- `description` (string): A description for the Work type code created.
- `workTypeCode` (string) **(requerido)**: Identifier for the Work Type being created. Can be 'WRAP_UP_CODE' or 'IDLE_CODE'.
- `active` (boolean) **(requerido)**: Indicates whether the work type is active or not.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `createdTime` (integer): Creation time(in epoch millis) of this resource.
- `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: A name for the Work Type.
  - `description` (string): A description for the Work type code created.
  - `workTypeCode` (string) **(requerido)**: Identifier for the Work Type being created. Can be 'WRAP_UP_CODE' or 'IDLE_CODE'.
  - `active` (boolean) **(requerido)**: Indicates whether the work type is active or not.
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
