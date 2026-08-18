---
doc_id: webex-contact-center-get-v1-orgid-functions
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /v1/{orgId}/functions
operation_id: findAll
tags: Functions
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.859226+00:00
---

# GET /v1/{orgId}/functions

**API:** Webex Contact Center
**Área:** Functions
**operationId:** `findAll`

## Resumen
List Custom Functions

## Descripción
List or search custom functions in the organization. Without filters, returns all custom functions. Supports filtering by name, language, and status, plus sorting and pagination.

Scope: `cjp:config_read`

## Parámetros
- `orgId` [path] (string) (**requerido**): Organization ID.
- `isPartialMatch` [query] (boolean): Whether to search with partial matches. If `false`, search/filter is based on exact match. Por defecto: True.
- `isCaseSensitive` [query] (boolean): Whether the search should be case-sensitive. Currently applicable only to the `name` field. Por defecto: False.
- `name` [query] (string): Filter by function name.
- `language` [query] (string): Filter by programming language. Valores: js, py.
- `status` [query] (string): Filter by one or more function statuses (comma-separated, no spaces). Case-sensitive.
- `sortBy` [query] (string): Comma-separated fields with order. Supported fields (case-sensitive): `name`, `language`, `status`, `lastModifiedDate`. Prefix a field with `-` for descending order; no prefix means ascending.
- `page` [query] (integer/int32): Zero-based page number for the paginated query. Por defecto: 0.
- `size` [query] (integer/int32): Number of results per page. Por defecto: 100.
- `ids` [query] (string): Comma-separated list of function IDs to fetch.
- `fields` [query] (string): Comma-separated list of function fields to include in the response.
- `isValidation` [query] (boolean): Used by the Tenant Management team to validate the existence of functions with given IDs regardless of the user's RBAC access. Por defecto: False.

## Ejemplo de invocación
```bash
curl -X GET '/v1/<orgId>/functions' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: Custom functions retrieved successfully.
- `data` (array): Page of custom function metadata records. Each entry carries metadata only; the source code is returned only when fetching a single function.
  - `id` (string): Function ID. Hexadecimal ObjectId.
  - `orgId` (string): Organization ID that owns the function.
  - `name` (string): Function name.
  - `description` (string): Human-readable description of the function.
  - `language` (string): Programming language. Valores: js, py.
  - `selectedRuntime` (string): Runtime identifier.
  - `status` (string): Lifecycle status. Valores: Draft, Published.
  - `timeoutInSec` (integer/int32): Maximum execution time for the function, in seconds.
  - `tagVersionMap` (object): Map of publish tag to the function version it currently points to.
  - `lockedBy` (string): User ID currently holding the edit lock, or empty if unlocked.
  - `createdBy` (string): User ID that created the function.
  - `createdDate` (string/date-time): Timestamp the function was created.
  - `lastModifiedBy` (string): User ID that last modified the function.
  - `lastModifiedDate` (string/date-time): Timestamp of the most recent modification.
- `pageInfo` (object): Pagination details for a paged list response.
  - `currentPage` (integer/int32): Zero-based index of the returned page.
  - `pageSize` (integer/int32): Page size used by the query.
  - `totalPages` (integer/int32): Total number of pages.
  - `totalRecords` (integer/int64): Total number of records matching the query, across all pages.

### Ejemplo — respuesta 200
```json
{
  "data": [
    {
      "id": "64f1b2c3d4e5f6a7b8c9d0e1",
      "orgId": "8eb7da9a-c81c-4d13-b08b-38fdeb7330d8",
      "name": "validateZipCode",
      "description": "Returns true if the supplied US zip code is in a valid 5-digit format.",
      "language": "js",
      "selectedRuntime": "nodejs22.x",
      "status": "Published",
      "timeoutInSec": 3,
      "tagVersionMap": {
        "Dev": "1",
        "Latest": "1"
      },
      "createdBy": "user@example.com",
      "createdDate": "2026-05-28T14:23:01Z",
      "lastModifiedBy": "user@example.com",
      "lastModifiedDate": "2026-05-28T14:23:01Z"
    }
  ],
  "pageInfo": {
    "currentPage": 0,
    "pageSize": 100,
    "totalPages": 1,
    "totalRecords": 1
  }
}
```

## Respuestas de error
- **400**: Bad Request. A required parameter was missing or had an invalid format.
  Ejemplo:
```json
{
  "code": "InvalidRequest",
  "message": "The campaign ID is missing"
}
```
- **401**: Unauthorized.
- **404**: No records found matching the supplied filters.
- **500**: Internal Server Error.
  Ejemplo:
```json
{
  "code": "InvalidRequest",
  "message": "The campaign ID is missing"
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs