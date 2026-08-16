---
doc_id: webex-contact-center-post-organization-orgid-outdial-ani-outdialaniid-entry
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/outdial-ani/{outDialAniId}/entry
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.946415+00:00
---

# POST /organization/{orgid}/outdial-ani/{outDialAniId}/entry

**API:** Webex Contact Center
**Área:** Outdial ANI
**operationId:** `createConfigOutDialANIEntry`

## Resumen
Create a new Outdial ANI Entry

## Descripción
Create a new Outdial ANI Entry in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `outDialAniId` [path] (string) **(requerido)**: Resource ID of the Outdial ANI

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) **(requerido)**: Enter a name for the outdial ANI entry.
- `number` (string) **(requerido)**: Enter a valid phone number or valid SIP URI.
- `defaultANIEntry` (boolean): Indicates whether this is the default Outdial ANI Entry(true) or not(false).
- `createdTime` (integer): This is the created time of the entity.
- `lastUpdatedTime` (integer): This is the updated time of the entity.

## Respuestas
- **201**: Created
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: Enter a name for the outdial ANI entry.
  - `number` (string) **(requerido)**: Enter a valid phone number or valid SIP URI.
  - `defaultANIEntry` (boolean): Indicates whether this is the default Outdial ANI Entry(true) or not(false).
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
