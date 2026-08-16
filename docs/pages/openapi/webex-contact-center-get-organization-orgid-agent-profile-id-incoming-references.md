---
doc_id: webex-contact-center-get-organization-orgid-agent-profile-id-incoming-references
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/agent-profile/{id}/incoming-references
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.939506+00:00
---

# GET /organization/{orgid}/agent-profile/{id}/incoming-references

**API:** Webex Contact Center
**Área:** Desktop Profile
**operationId:** `getIncomingReferencesDesktopProfile`

## Resumen
List references for a specific Desktop Profile

## Descripción
Retrieve a list of all entities that have reference to an existing Desktop Profile by ID in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: ID of this contact center resource.
- `type` [query] (string): Entity type of the other entity that has a reference to this specific entity.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.

## Respuestas
- **200**: OK
  - `description` (string): Description about reference info.
  - `meta` (object): Metadata of response for references with paging information
    - `orgid` (string): Org ID
    - `page` (integer): Current page number
    - `pageSize` (integer): Page size for current data set
    - `totalPages` (integer): Number of pages
    - `totalRecords` (integer): Total number of items
    - `links` (object): Map of pagination links with self, next, prev, last and first
    - `referencedEntities` (array): List of referenced entities
    - `currentEntity` (string): Name of current entity
  - `data` (array):
    - `id` (string): id
    - `name` (string): name
    - `additionalAttributes` (object): A map containing additional attributes of entity where both the key and value are Strings.
    - `createdDate` (string):
    - `lastModifiedDate` (string):
    - `version` (integer):
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
