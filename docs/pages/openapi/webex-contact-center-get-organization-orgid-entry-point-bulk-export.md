---
doc_id: webex-contact-center-get-organization-orgid-entry-point-bulk-export
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/entry-point/bulk-export
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.942361+00:00
---

# GET /organization/{orgid}/entry-point/bulk-export

**API:** Webex Contact Center
**Área:** Entry Point
**operationId:** `bulkExport_12`

## Resumen
Bulk export Entry Point(s)

## Descripción
Export all Entry Point(s) in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `type` [query] (string) **(requerido)**: Indicates the type of Entrypoint; can be INBOUND or OUTBOUND.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.

## Respuestas
- **200**: OK
  - `totalResources` (integer): Total number of items
  - `pageNumber` (integer): Current page number
  - `pageSize` (integer): Page size for current data set
  - `rel` (string): Indicates whether more pages exist. When 'next' there are more pages available, otherwise 'last'.
  - `resources` (array):
    - `name` (string):
    - `description` (string):
    - `serviceLevelThreshold` (string):
    - `timezone` (string):
    - `channelType` (string):
    - `socialChannelType` (string):
    - `entryPointType` (string):
    - `assetId` (string):
    - `flowId` (string):
    - `flowTag` (string):
    - `musicOnHoldId` (string):
    - `outdialQueueId` (string):
    - `callbackEnabled` (boolean):
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
