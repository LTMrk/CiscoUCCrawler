---
doc_id: webex-contact-center-post-organization-orgid-user-fetch-user-details-by-ids
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/user/fetch-user-details-by-ids
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.955120+00:00
---

# POST /organization/{orgid}/user/fetch-user-details-by-ids

**API:** Webex Contact Center
**Área:** Users
**operationId:** `getUserdataByIdsUser`

## Resumen
List Users with details

## Descripción
Retrieve an existing User's first name, last name and email by list of IDs in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.

## Cuerpo de la petición (application/json)
- `userIds` (array): List of valid user IDs. Provide this only when both `search` and `queueId` are not provided.
- `search` (string): Text used to search for users (e.g., by firstName, lastName or email of the user). If provided, `queueId` is **required**. Cannot be used in combination with `userIds`.
- `queueId` (string): Agent Based Queue ID to filter users . Required if `search` is provided. Cannot be used with `userIds`.

## Respuestas
- **200**: OK
  - `meta` (object): Metadata of response with paging information. Includes orgId, page, pageSize, totalPages, totalRecords, and pagination links.
  - `data` (array): List of Data.
    - `id` (string): Unique ID of the user
    - `firstName` (string): First name of the user
    - `lastName` (string): Last name of the user
    - `email` (string): Email address of the user
  - `meta` (object): Metadata of response with paging information. Includes orgId, page, pageSize, totalPages, totalRecords, and pagination links.
  - `data` (array): List of Data.
    - `id` (string): Unique ID of the user
    - `firstName` (string): First name of the user
    - `lastName` (string): Last name of the user
    - `email` (string): Email address of the user
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
