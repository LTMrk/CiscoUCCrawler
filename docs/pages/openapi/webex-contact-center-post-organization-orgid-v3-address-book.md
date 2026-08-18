---
doc_id: webex-contact-center-post-organization-orgid-v3-address-book
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/v3/address-book
operation_id: createConfig_2
tags: Address Book
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.771022+00:00
---

# POST /organization/{orgid}/v3/address-book

**API:** Webex Contact Center
**Área:** Address Book
**operationId:** `createConfig_2`

## Resumen
Create a new Address Book

## Descripción
Create a new Address Book in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): A name for the address book. Long. max: 80.
- `description` (string): A short description indicating the context of the address book. Long. max: 255.
- `parentType` (string) (**requerido**): A parent type which indicates whether the address book is accessible for all sites or a specific site.  Once created, parentType cannot be modified. Valores: ORGANIZATION, SITE.
- `siteId` (string): The specific site id where the address book is accessible.
- `createdTime` (integer/int64) (solo lectura): Creation time(in epoch millis) of this resource.
- `lastUpdatedTime` (integer/int64) (solo lectura): Time(in epoch millis) when this resource was last updated.

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/v3/address-book' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name": "<name>", "parentType": "<parentType>"}'
```

## Respuestas correctas
**201**: Created
- `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): A name for the address book. Long. max: 80.
- `description` (string): A short description indicating the context of the address book. Long. max: 255.
- `parentType` (string) (**requerido**): A parent type which indicates whether the address book is accessible for all sites or a specific site.  Once created, parentType cannot be modified. Valores: ORGANIZATION, SITE.
- `siteId` (string): The specific site id where the address book is accessible.
- `createdTime` (integer/int64) (solo lectura): Creation time(in epoch millis) of this resource.
- `lastUpdatedTime` (integer/int64) (solo lectura): Time(in epoch millis) when this resource was last updated.

## Respuestas de error
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs