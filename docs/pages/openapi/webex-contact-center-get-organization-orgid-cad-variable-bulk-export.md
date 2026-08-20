---
doc_id: webex-contact-center-get-organization-orgid-cad-variable-bulk-export
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/cad-variable/bulk-export
operation_id: bulkExport_18
tags: Global Variables
deprecated: true
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.696753+00:00
---

# GET /organization/{orgid}/cad-variable/bulk-export

> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.

**API:** Webex Contact Center
**Área:** Global Variables
**operationId:** `bulkExport_18`

## Resumen
Bulk export Global Variable(s)

## Descripción
Export all Global Variable(s) in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 50.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/cad-variable/bulk-export' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `totalResources` (integer/int32): Total number of items
- `pageNumber` (integer/int32): Current page number
- `pageSize` (integer/int32): Page size for current data set
- `rel` (string): Indicates whether more pages exist. When 'next' there are more pages available, otherwise 'last'.
- `resources` (array):
  - `name` (string): A name for the Global Variable.
  - `description` (string): A the description for the Global Variable created.
  - `agentEditable` (boolean): Indicates whether the Global Variable is editable in the Agent Desktop by the agent or not.
  - `variableType` (string): A valid Global Variable Type. The valid types are: String, Integer, DateTime, Boolean, Decimal. Valores: STRING, INTEGER, DATE_TIME, BOOLEAN, DECIMAL, String, Integer, DateTime, Boolean, Decimal.
  - `defaultValue` (string): A default value for the Global Variable.
  - `reportable` (boolean): Indicates whether the Global Variable is reportable or not.
  - `sensitive` (boolean): Indicates whether the Global Variable is sensitive or not.
  - `agentViewable` (boolean): Indicates whether the agent can view the Global Variable in Agent Desktop or not.
  - `desktopLabel` (string): A desktop label for the Global Variable created.

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