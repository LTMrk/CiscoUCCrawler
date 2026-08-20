---
doc_id: webex-contact-center-post-organization-orgid-address-book-addressbookid-entry-bulk
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/address-book/{addressBookId}/entry/bulk
operation_id: saveAllConfig_24
tags: Address Book
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.667505+00:00
---

# POST /organization/{orgid}/address-book/{addressBookId}/entry/bulk

**API:** Webex Contact Center
**Área:** Address Book
**operationId:** `saveAllConfig_24`

## Resumen
Bulk save Address Book Entry(s)

## Descripción
Create, Update or delete Address Book Entry(s) in bulk for an Address Book in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `addressBookId` [path] (string) (**requerido**): Resource ID of the Address Book

## Cuerpo de la petición (application/json)
- `items` (array):
  - `itemIdentifier` (integer/int32): Unique item identifier for a bulk operation.
  - `item` (object):
    - `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string) (**requerido**): A name for the address book entry. Long. max: 80.
    - `number` (string) (**requerido**): The phone number for the entry.
    - `createdTime` (integer/int64) (solo lectura): Creation time(in epoch millis) of this resource.
    - `lastUpdatedTime` (integer/int64) (solo lectura): Time(in epoch millis) when this resource was last updated.
  - `requestAction` (string): Identifier for action type. Possible values can be SAVE and DELETE.

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/address-book/<addressBookId>/entry/bulk' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**207**: Multi-Status
- `items` (array):
  - `itemIdentifier` (integer/int32): Unique item identifier for a bulk operation.
  - `status` (integer/int32): Indicates the error status code.
  - `operationType` (string): The kind of operation desired of an entity. Valores: CREATE, UPDATE, DELETE, GET.
  - `href` (string): The resource URI of an entity.
  - `apiError` (object): Response body for an API error.
    - `trackingId` (string): An opaque identifier for mapping protocol failures to service internal codes.   When specified in a request, it can be used for co-relating events across services
    - `error` (object): Details of an error.
      - `key` (string): An application defined error code.
      - `message` (array): A message providing details about the error.
        - `description` (string): A human readable explanation for the occurrence of an error.

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