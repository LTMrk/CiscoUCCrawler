---
doc_id: webex-contact-center-get-orgid-project-projectid-flows-search
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /{orgId}/project/{projectId}/flows:search
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.966136+00:00
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
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `projectId` [path] (string) **(requerido)**: Project ID. System generated value which is the same across orgs and environments. Always use: 5e5c9ad6d61f870d6d778c1b.
- `query` [query] (string) **(requerido)**: Searches for flows with the given query. The search is case-sensitive.
- `flowType` [query] (string): Either of 'FLOW' or 'SUBFLOW' or 'ALL'. Default value is 'ALL'.
- `page` [query] (integer): Defines the number of the displayed page. The page number starts from 0.
- `size` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.
- `keyValueFilter` [query] (string): Filters results based on key-value pairs. Format: 'key1|value1,key2|value2'. This will add a filter on normalizedFlow collection directly instead of running query on atlas.

## Respuestas
- **200**: OK
  - `pageInfo` (object): Pagination metadata for a flow search response.
    - `currentPage` (integer): Zero-based index of the current page.
    - `totalRecords` (integer): Total number of flows matching the search criteria across all pages.
    - `pageSize` (integer): Number of items on the current page.
    - `totalPages` (integer): Total number of pages available for the search criteria.
  - `data` (array): Flows matching the search criteria for the current page.
    - `orgId` (string): Organization ID.
    - `id` (string): Flow ID.
    - `name` (string): Name of the flow.
    - `flowType` (string): Either of 'FLOW' or 'SUBFLOW'.
    - `lastModifiedDate` (string): Date the flow was last modified.
- **400**: Bad request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **500**: Internal Server Error

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
