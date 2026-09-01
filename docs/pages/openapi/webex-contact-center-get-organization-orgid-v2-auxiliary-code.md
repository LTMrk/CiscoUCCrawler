---
doc_id: webex-contact-center-get-organization-orgid-v2-auxiliary-code
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/v2/auxiliary-code
operation_id: getAllConfigWithMetaData_21
tags: Auxiliary Code
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.648685+00:00
---

# GET /organization/{orgid}/v2/auxiliary-code

**API:** Webex Contact Center
**Área:** Auxiliary Code
**operationId:** `getAllConfigWithMetaData_21`

## Resumen
List Auxiliary Code(s)

## Descripción
Retrieve a list of Auxiliary Code(s) in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. All the fields are supported except: organizationId, createdTime, lastUpdatedTime, validBurnoutForWrapUpCode, validBurnoutForIdleCode   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain space, and if so kindly bound it with quotes to apply filter.
- `attributes` [query] (string/string): Specify the attributes to be returned.Default all attributes are returned along with specified columns. All Attributes are supported
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(name, description)  The examples below show some search queries - "Cisco" - field=="name";value=="Cisco" - fields=in=("name","description");value=="Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.
- `desktopProfileFilter` [query] (boolean): If set to true, the API will return only the data that the user has access to according to its Desktop Profile. If set to false, the API will not check for Desktop Profile level access. Por defecto: False.
- `supervisedUserId` [query] (string): User Id of the Agent whose Agent Profile associated Idle Codes are to be fetched.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/v2/auxiliary-code' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `meta` (object): Metadata of response with paging information
  - `orgid` (string/uuid): Organization ID. Long. max: 36.
  - `page` (integer/int32): Current page number.
  - `pageSize` (integer/int32): Page size for current data set.
  - `totalPages` (integer/int32): Number of pages.
  - `totalRecords` (integer/int32): Total number of items.
  - `links` (object): Map of pagination links with `self`, `next`, `prev`, `last`, and `first`.
- `data` (array):
  - `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) (**requerido**): A name for the code. Long. max: 80.
  - `description` (string): A short description indicating the context of the code. Long. max: 255.
  - `defaultCode` (boolean) (**requerido**): Indicates whether this is the default code(true) or not(false).  If this is the first idle or wrap-up code for your organization,it must be the default. It can be made non-default later once more codes are created.
  - `active` (boolean) (**requerido**): Indicates whether the code is active(when true) or not active(when false).   It is required only during a create or an update operation.
  - `isSystemCode` (boolean): Indicates whether this is the system default code(true) or not(false).
  - `workTypeId` (string) (**requerido**): Indicates the work type id associated with this code.
  - `workTypeCode` (string) (**requerido**): Indicates the work type associated with this code. Valores: IDLE_CODE, WRAP_UP_CODE.
  - `burnoutInclusion` (string): Indicates the idle code Inclusion status for agent burnout calculation. Default value is 'INCLUDED' for idle codes and 'NOT_APPLICABLE' for wrap up codes. Valores: NOT_APPLICABLE, EXCLUDED, INCLUDED.
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not
  - `createdTime` (integer/int64) (solo lectura): Creation time(in epoch millis) of this resource.
  - `lastUpdatedTime` (integer/int64) (solo lectura): Time(in epoch millis) when this resource was last updated.

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