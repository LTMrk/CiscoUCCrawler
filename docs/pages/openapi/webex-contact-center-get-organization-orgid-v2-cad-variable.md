---
doc_id: webex-contact-center-get-organization-orgid-v2-cad-variable
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/v2/cad-variable
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.944161+00:00
---

# GET /organization/{orgid}/v2/cad-variable

**API:** Webex Contact Center
**Área:** Global Variables
**operationId:** `getAllConfigWithMetaData_31`

## Resumen
List Global Variable(s)

## Descripción
Retrieve a list of Global Variable(s) in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. All the fields are supported except: organizationId, createdTime, lastUpdatedTime   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain space, and if so kindly bound it with quotes to apply filter.
- `attributes` [query] (string): Specify the attributes to be returned.Default all attributes are returned along with specified columns. All Attributes are supported
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(name)  The examples below show some search queries - "Cisco" - field=="name";value=="Cisco" - fields=in=("name");value=="Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.

## Respuestas
- **200**: OK
  - `meta` (object):
  - `data` (array):
    - `organizationId` (string): ID of the contact center organization. It is required to define for the following operations - All bulk save operations
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string) **(requerido)**: A name for the Global Variable.
    - `description` (string): A the description for the Global Variable created.
    - `active` (boolean) **(requerido)**: Indicates whether the Global Variable is active or not.
    - `agentEditable` (boolean) **(requerido)**: Indicates whether the Global Variable is editable in the Agent Desktop by the agent or not.
    - `variableType` (string) **(requerido)**: A valid Global Variable Type. The valid types are: String, Integer, DateTime, Boolean, Decimal. Valores: STRING, INTEGER, DATE_TIME, BOOLEAN, DECIMAL, String, Integer, DateTime, Boolean, Decimal.
    - `defaultValue` (string) **(requerido)**: A default value for the Global Variable.
    - `reportable` (boolean) **(requerido)**: Indicates whether the Global Variable is reportable or not.
    - `agentViewable` (boolean) **(requerido)**: Indicates whether the agent can view the Global Variable in Agent Desktop or not.
    - `sensitive` (boolean): Indicates whether the Global Variable is sensitive or not.
    - `desktopLabel` (string): A desktop label for the Global Variable created.
    - `systemDefault` (boolean): Indicates whether the created resource is system created or not
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
