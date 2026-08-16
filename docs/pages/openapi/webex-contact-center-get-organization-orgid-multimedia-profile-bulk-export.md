---
doc_id: webex-contact-center-get-organization-orgid-multimedia-profile-bulk-export
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/multimedia-profile/bulk-export
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.944751+00:00
---

# GET /organization/{orgid}/multimedia-profile/bulk-export

**API:** Webex Contact Center
**Área:** Multimedia Profile
**operationId:** `bulkExport_10`

## Resumen
Bulk export Multimedia Profile(s)

## Descripción
Export all Multimedia Profile(s) in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
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
    - `chat` (integer):
    - `email` (integer):
    - `fax` (integer):
    - `telephony` (integer):
    - `video` (integer):
    - `social` (integer):
    - `others` (integer):
    - `active` (boolean):
    - `blendingModeEnabled` (boolean):
    - `blendingMode` (string):
    - `manuallyAssignable` (object):
      - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
      - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
      - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
      - `telephony` (integer) **(requerido)**: Define the upper limits for this channel type. It should be either 0 or 1.
      - `chat` (integer) **(requerido)**: Define the upper limits for this channel type. It should range from 0 to 5.
      - `email` (integer) **(requerido)**: Define the upper limits for this channel type. It should range from 0 to 10.
      - `social` (integer) **(requerido)**: Define the upper limits for this channel type. It should range from 0 to 5.
      - `createdTime` (integer): Creation time(in epoch millis) of this resource.
      - `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
