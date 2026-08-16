---
doc_id: webex-contact-center-get-v1-orgid-functions
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /v1/{orgId}/functions
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.967822+00:00
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
- `orgId` [path] (string) **(requerido)**: Organization ID.
- `isPartialMatch` [query] (boolean): Whether to search with partial matches. If `false`, search/filter is based on exact match.
- `isCaseSensitive` [query] (boolean): Whether the search should be case-sensitive. Currently applicable only to the `name` field.
- `name` [query] (string): Filter by function name.
- `language` [query] (string): Filter by programming language.
- `status` [query] (string): Filter by one or more function statuses (comma-separated, no spaces). Case-sensitive.
- `sortBy` [query] (string): Comma-separated fields with order. Supported fields (case-sensitive): `name`, `language`, `status`, `lastModifiedDate`. Prefix a field with `-` for descending order; no prefix means ascending.
- `page` [query] (integer): Zero-based page number for the paginated query.
- `size` [query] (integer): Number of results per page.
- `ids` [query] (string): Comma-separated list of function IDs to fetch.
- `fields` [query] (string): Comma-separated list of function fields to include in the response.
- `isValidation` [query] (boolean): Used by the Tenant Management team to validate the existence of functions with given IDs regardless of the user's RBAC access.

## Respuestas
- **200**: Custom functions retrieved successfully.
  - `data` (array): Page of custom function metadata records. Each entry carries metadata only; the source code is returned only when fetching a single function.
    - `id` (string): Function ID. Hexadecimal ObjectId.
    - `orgId` (string): Organization ID that owns the function.
    - `name` (string): Function name.
    - `description` (string): Human-readable description of the function.
    - `language` (string): Programming language. Valores: js, py.
    - `selectedRuntime` (string): Runtime identifier.
    - `status` (string): Lifecycle status. Valores: Draft, Published.
    - `timeoutInSec` (integer): Maximum execution time for the function, in seconds.
    - `tagVersionMap` (object): Map of publish tag to the function version it currently points to.
    - `lockedBy` (string): User ID currently holding the edit lock, or empty if unlocked.
    - `createdBy` (string): User ID that created the function.
    - `createdDate` (string): Timestamp the function was created.
    - `lastModifiedBy` (string): User ID that last modified the function.
    - `lastModifiedDate` (string): Timestamp of the most recent modification.
  - `pageInfo` (object): Pagination details for a paged list response.
    - `currentPage` (integer): Zero-based index of the returned page.
    - `pageSize` (integer): Page size used by the query.
    - `totalPages` (integer): Total number of pages.
    - `totalRecords` (integer): Total number of records matching the query, across all pages.
- **400**: Bad Request. A required parameter was missing or had an invalid format.
- **401**: Unauthorized.
- **404**: No records found matching the supplied filters.
- **500**: Internal Server Error.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
