---
doc_id: webex-contact-center-get-organization-orgid-v2-cad-variable
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/v2/cad-variable
operation_id: getAllConfigWithMetaData_31
tags: Global Variables
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.697767+00:00
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
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. All the fields are supported except: organizationId, createdTime, lastUpdatedTime   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain space, and if so kindly bound it with quotes to apply filter.
- `attributes` [query] (string/string): Specify the attributes to be returned.Default all attributes are returned along with specified columns. All Attributes are supported
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(name)  The examples below show some search queries - "Cisco" - field=="name";value=="Cisco" - fields=in=("name");value=="Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/v2/cad-variable' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `meta` (object):
- `data` (array):
  - `organizationId` (string/uuid): ID of the contact center organization. It is required to define for the following operations - All bulk save operations Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) (**requerido**): A name for the Global Variable. Long. max: 80.
  - `description` (string): A the description for the Global Variable created. Long. max: 256.
  - `active` (boolean) (**requerido**): Indicates whether the Global Variable is active or not.
  - `agentEditable` (boolean) (**requerido**): Indicates whether the Global Variable is editable in the Agent Desktop by the agent or not.
  - `variableType` (string) (**requerido**): A valid Global Variable Type. The valid types are: String, Integer, DateTime, Boolean, Decimal. Valores: STRING, INTEGER, DATE_TIME, BOOLEAN, DECIMAL, String, Integer, DateTime, Boolean, Decimal.
  - `defaultValue` (string) (**requerido**): A default value for the Global Variable. Long. max: 256.
  - `reportable` (boolean) (**requerido**): Indicates whether the Global Variable is reportable or not.
  - `agentViewable` (boolean) (**requerido**): Indicates whether the agent can view the Global Variable in Agent Desktop or not.
  - `sensitive` (boolean): Indicates whether the Global Variable is sensitive or not.
  - `desktopLabel` (string): A desktop label for the Global Variable created. Long. max: 50.
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