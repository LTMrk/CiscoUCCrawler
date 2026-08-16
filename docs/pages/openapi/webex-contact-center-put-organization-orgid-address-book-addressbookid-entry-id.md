---
doc_id: webex-contact-center-put-organization-orgid-address-book-addressbookid-entry-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PUT
path: /organization/{orgid}/address-book/{addressBookId}/entry/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.928085+00:00
---

# PUT /organization/{orgid}/address-book/{addressBookId}/entry/{id}

**API:** Webex Contact Center
**Área:** Address Book
**operationId:** `updateConfig_31`

## Resumen
Update specific Address Book Entry by ID

## Descripción
Update an existing Address Book Entry by ID in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `addressBookId` [path] (string) **(requerido)**: Resource ID of the Address Book
- `id` [path] (string) **(requerido)**: Resource ID of the Address Book Entry

## Cuerpo de la petición (application/json)
- `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) **(requerido)**: A name for the address book entry.
- `number` (string) **(requerido)**: The phone number for the entry.
- `createdTime` (integer): Creation time(in epoch millis) of this resource.
- `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) **(requerido)**: A name for the address book entry.
  - `number` (string) **(requerido)**: The phone number for the entry.
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
