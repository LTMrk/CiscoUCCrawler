---
doc_id: webex-contact-center-get-organization-orgid-work-type-bulk-export
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/work-type/bulk-export
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.958338+00:00
---

# GET /organization/{orgid}/work-type/bulk-export

**API:** Webex Contact Center
**Área:** Work Types
**operationId:** `bulkExport`

## Resumen
Bulk export Work Type(s)

## Descripción
Export all Work Type(s) in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.

## Respuestas
- **200**: OK
  - `totalResources` (integer): Total number of items
  - `pageNumber` (integer): Current page number
  - `pageSize` (integer): Page size for current data set
  - `rel` (string): Indicates whether more pages exist. When 'next' there are more pages available, otherwise 'last'.
  - `resources` (array):
    - `name` (string): A name for the Work Type.
    - `description` (string): A description for the Work type code created.
    - `workTypeCode` (string): Identifier for the Work Type being created. Can be 'WRAP_UP_CODE' or 'IDLE_CODE'.
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
