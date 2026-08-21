---
doc_id: webex-contact-center-get-organization-orgid-multimedia-profile-bulk-export
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/multimedia-profile/bulk-export
operation_id: bulkExport_10
tags: Multimedia Profile
deprecated: true
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.758172+00:00
---

# GET /organization/{orgid}/multimedia-profile/bulk-export

> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.

**API:** Webex Contact Center
**Área:** Multimedia Profile
**operationId:** `bulkExport_10`

## Resumen
Bulk export Multimedia Profile(s)

## Descripción
Export all Multimedia Profile(s) in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/multimedia-profile/bulk-export' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `totalResources` (integer/int32): Total number of items
- `pageNumber` (integer/int32): Current page number
- `pageSize` (integer/int32): Page size for current data set
- `rel` (string): Indicates whether more pages exist. When 'next' there are more pages available, otherwise 'last'.
- `resources` (array):
  - `name` (string):
  - `description` (string):
  - `chat` (integer/int32):
  - `email` (integer/int32):
  - `fax` (integer/int32):
  - `telephony` (integer/int32):
  - `video` (integer/int32):
  - `social` (integer/int32):
  - `others` (integer/int32):
  - `active` (boolean):
  - `blendingModeEnabled` (boolean):
  - `blendingMode` (string):
  - `manuallyAssignable` (object):
    - `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `telephony` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should be either 0 or 1.
    - `chat` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should range from 0 to 5.
    - `email` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should range from 0 to 10.
    - `social` (integer/int32) (**requerido**): Define the upper limits for this channel type. It should range from 0 to 5.
    - `createdTime` (integer/int64) (solo lectura): Creation time(in epoch millis) of this resource.
    - `lastUpdatedTime` (integer/int64) (solo lectura): Time(in epoch millis) when this resource was last updated.

## Respuestas de error
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs