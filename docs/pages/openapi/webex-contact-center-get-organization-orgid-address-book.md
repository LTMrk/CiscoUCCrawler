---
doc_id: webex-contact-center-get-organization-orgid-address-book
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/address-book
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.927411+00:00
---

# GET /organization/{orgid}/address-book

**API:** Webex Contact Center
**Área:** Address Book
**operationId:** `getAllConfigWithEntries`

## Resumen
List Address Book(s)

## Descripción
Retrieve a list of Address Book(s) in a given organization. To get address book having large entries use latest apis.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. Supported filterable fields:  id.   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain space, and if so kindly bound it with quotes to apply filter.
- `attributes` [query] (string): Specify the attributes to be returned.Default all attributes are returned along with specified columns. All Attributes are supported
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.

## Respuestas
- **200**: OK
  - (array de:)
    - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string) **(requerido)**: A name for the address book.
    - `description` (string): A short description indicating the context of the address book.
    - `parentType` (string) **(requerido)**: A parent type which indicates whether the address book is accessible for all sites or a specific site.  Once created, parentType cannot be modified. Valores: ORGANIZATION, SITE.
    - `siteId` (string): The specific site id where the address book is accessible.
    - `addressBookEntries` (array):
      - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
      - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
      - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
      - `name` (string) **(requerido)**: A name for the address book entry.
      - `number` (string) **(requerido)**: The phone number for the entry.
      - `createdTime` (integer): Creation time(in epoch millis) of this resource.
      - `lastUpdatedTime` (integer): Time(in epoch millis) when this resource was last updated.
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
