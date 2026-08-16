---
doc_id: webex-contact-center-post-organization-orgid-address-book
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/address-book
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.927538+00:00
---

# POST /organization/{orgid}/address-book

**API:** Webex Contact Center
**Área:** Address Book
**operationId:** `createConfigWithEntries`

## Resumen
Create a new Address Book

## Descripción
Create a new Address Book in a given organization. To create address book having large entries use latest apis.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) **(requerido)**: A name for the address book.
- `description` (string): A short description indicating the context of the address book.
- `parentType` (string) **(requerido)**: A parent type which indicates whether the address book is accessible for all sites or a specific site.  Once created, parentType cannot be modified. Valores: ORGANIZATION, SITE.
- `siteId` (string): The specific site id where the address book is accessible.
- `addressBookEntries` (array):
  - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: A name for the address book entry.
  - `number` (string) **(requerido)**: The phone number for the entry.
  - `createdTime` (integer): Creation time(in epoch millis) of this resource.
  - `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.
- `createdTime` (integer): Creation time(in epoch millis) of this resource.
- `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.

## Respuestas
- **201**: Created
  - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: A name for the address book.
  - `description` (string): A short description indicating the context of the address book.
  - `parentType` (string) **(requerido)**: A parent type which indicates whether the address book is accessible for all sites or a specific site.  Once created, parentType cannot be modified. Valores: ORGANIZATION, SITE.
  - `siteId` (string): The specific site id where the address book is accessible.
  - `addressBookEntries` (array):
    - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string) **(requerido)**: A name for the address book entry.
    - `number` (string) **(requerido)**: The phone number for the entry.
    - `createdTime` (integer): Creation time(in epoch millis) of this resource.
    - `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.
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
