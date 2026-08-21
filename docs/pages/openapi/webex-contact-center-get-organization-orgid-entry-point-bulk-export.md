---
doc_id: webex-contact-center-get-organization-orgid-entry-point-bulk-export
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/entry-point/bulk-export
operation_id: bulkExport_12
tags: Entry Point
deprecated: true
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-21T15:48:41.754286+00:00
---

# GET /organization/{orgid}/entry-point/bulk-export

> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.

**API:** Webex Contact Center
**Área:** Entry Point
**operationId:** `bulkExport_12`

## Resumen
Bulk export Entry Point(s)

## Descripción
Export all Entry Point(s) in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `type` [query] (string) (**requerido**): Indicates the type of Entrypoint; can be INBOUND or OUTBOUND. Valores: INBOUND, OUTBOUND.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 50.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/entry-point/bulk-export?type=<type>' \
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