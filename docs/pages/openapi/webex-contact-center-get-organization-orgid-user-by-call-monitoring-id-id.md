---
doc_id: webex-contact-center-get-organization-orgid-user-by-call-monitoring-id-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/user/by-call-monitoring-id/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.954334+00:00
---

# GET /organization/{orgid}/user/by-call-monitoring-id/{id}

**API:** Webex Contact Center
**Área:** Users
**operationId:** `getUsersByCallMonitoringIdUser`

## Resumen
List users by call monitoring id

## Descripción
Fetch paginated users associated to the selected call monitoring team filters while enforcing team ACL.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the call monitoring.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.

## Respuestas
- **200**: OK
  - `meta` (object): Meta Data Paged User schema.
    - `orgid` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `page` (integer): Current page number.
    - `pageSize` (integer): Page size for current data set.
    - `totalPages` (integer): Number of pages.
    - `totalRecords` (integer): Total number of items.
    - `links` (object):
      - `self` (string) **(requerido)**: Link to the current page.
      - `first` (string): Link to the first page.
      - `last` (string): Link to the last page.
      - `next` (string): Link to the next page.
      - `prev` (string): Link to the previous page.
    - `actualBurnoutInclusionCount` (integer): Indicates the actual count of Agents selected for Agent burnout detection, including restricted agents that are not visible to requesting user.
    - `actualAutoCSATCount` (integer): Indicates the actual count of Agents selected for Auto CSAT scores, including restricted agents that are not visible to requesting user.
    - `actualSummariesCount` (integer): Indicates the actual count of Agents selected for Generated Summaries, including restricted agents that are not visible to requesting user.
  - `data` (array):
    - `id` (string): Unique ID of the user
    - `firstName` (string): First name of the user
    - `lastName` (string): Last name of the user
    - `email` (string): Email address of the user
  - `meta` (object): Meta Data Paged User schema.
    - `orgid` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `page` (integer): Current page number.
    - `pageSize` (integer): Page size for current data set.
    - `totalPages` (integer): Number of pages.
    - `totalRecords` (integer): Total number of items.
    - `links` (object):
      - `self` (string) **(requerido)**: Link to the current page.
      - `first` (string): Link to the first page.
      - `last` (string): Link to the last page.
      - `next` (string): Link to the next page.
      - `prev` (string): Link to the previous page.
    - `actualBurnoutInclusionCount` (integer): Indicates the actual count of Agents selected for Agent burnout detection, including restricted agents that are not visible to requesting user.
    - `actualAutoCSATCount` (integer): Indicates the actual count of Agents selected for Auto CSAT scores, including restricted agents that are not visible to requesting user.
    - `actualSummariesCount` (integer): Indicates the actual count of Agents selected for Generated Summaries, including restricted agents that are not visible to requesting user.
  - `data` (array):
    - `id` (string): Unique ID of the user
    - `firstName` (string): First name of the user
    - `lastName` (string): Last name of the user
    - `email` (string): Email address of the user
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
