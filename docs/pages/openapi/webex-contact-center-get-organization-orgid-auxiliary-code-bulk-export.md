---
doc_id: webex-contact-center-get-organization-orgid-auxiliary-code-bulk-export
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/auxiliary-code/bulk-export
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.932289+00:00
---

# GET /organization/{orgid}/auxiliary-code/bulk-export

**API:** Webex Contact Center
**Área:** Auxiliary Code
**operationId:** `bulkExport_20`

## Resumen
Bulk export Auxiliary Code(s)

## Descripción
Export all Auxiliary Code(s) in a given organization.

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
    - `name` (string) **(requerido)**: A name for the code.
    - `description` (string): A short description indicating the context of the code.
    - `defaultCode` (string): Indicates the default work code for your organization.
    - `workTypeName` (string): Indicates the work type associated with this code.
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
