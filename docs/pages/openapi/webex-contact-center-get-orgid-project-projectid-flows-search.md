---
doc_id: webex-contact-center-get-orgid-project-projectid-flows-search
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /{orgId}/project/{projectId}/flows:search
operation_id: searchFlows
tags: Flows
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.147252+00:00
---

# GET /{orgId}/project/{projectId}/flows:search

**API:** Webex Contact Center
**Área:** Flows
**operationId:** `searchFlows`

## Resumen
Search Flows

## Descripción
Returns a list of flows in response. The search is case-sensitive.

Scope: `cjp:config_read`. Roles: [`Organizational Full Admin`, `Supervisor`, `Contact Center Service Admin`, `User Admin`]

## Parámetros
- `orgId` [path] (string) (**requerido**): Organization ID.
- `projectId` [path] (string) (**requerido**): Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `query` [query] (string) (**requerido**): Searches for flows with the given query. The search is case-sensitive.
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW' or 'ALL'. Default value is 'ALL'. Por defecto: ALL.
- `page` [query] (integer/int32): Defines the number of the displayed page. The page number starts from 0. Por defecto: 0.
- `size` [query] (integer/int32): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.
- `keyValueFilter` [query] (string): Filters results based on key-value pairs. Format: 'key1|value1,key2|value2'. This will add a filter on normalizedFlow collection directly instead of running query on atlas. Por defecto: .

## Ejemplo de invocación
```bash
curl -X GET '/<orgId>/project/<projectId>/flows:search?query=<query>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `pageInfo` (object): Pagination metadata for a flow search response.
  - `currentPage` (integer/int32): Zero-based index of the current page.
  - `totalRecords` (integer/int32): Total number of flows matching the search criteria across all pages.
  - `pageSize` (integer/int32): Number of items on the current page.
  - `totalPages` (integer/int32): Total number of pages available for the search criteria.
- `data` (array): Flows matching the search criteria for the current page.
  - `orgId` (string): Organization ID.
  - `id` (string): Flow ID.
  - `name` (string): Name of the flow.
  - `flowType` (string): Either of 'FLOW' or 'SUBFLOW'.
  - `lastModifiedDate` (string/date-time): Date the flow was last modified.

### Ejemplo — respuesta 200
```json
{
  "pageInfo": {
    "currentPage": 0,
    "totalRecords": 8,
    "pageSize": 3,
    "totalPages": 3
  },
  "data": [
    {
      "orgId": "8eb7da9a-c81c-4d13-b08b-38fdeb7330d8",
      "id": "6501eae8d7974a1c1d4c25d3",
      "name": "Test_Flow",
      "flowType": "FLOW",
      "lastModifiedDate": "2026-02-10T01:59:02.213Z"
    }
  ]
}
```

## Respuestas de error
- **400**: Bad request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **500**: Internal Server Error

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs