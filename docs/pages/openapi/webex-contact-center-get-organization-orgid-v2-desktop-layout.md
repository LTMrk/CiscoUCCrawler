---
doc_id: webex-contact-center-get-organization-orgid-v2-desktop-layout
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/v2/desktop-layout
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.938327+00:00
---

# GET /organization/{orgid}/v2/desktop-layout

**API:** Webex Contact Center
**Área:** Desktop Layout
**operationId:** `getAllConfigWithMetaData_14`

## Resumen
List Desktop Layout(s)

## Descripción
Retrieve a list of Desktop Layout(s) in a given organization. Json file content field won't be avalible in get all even though it is showing in sample response structure. and it will be avialable only in get by id.
 Note: Returning array fields in the List (Get All) API response is deprecated. To retrieve the complete resource with all fields, please use the Get-by-ID API instead.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. All the fields are supported except: organizationId, validatedTime, defaultJsonModifiedTime, modifiedTime, teamIds, createdTime, lastUpdatedTime   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `attributes` [query] (string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported.
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(name)  The examples below show some search queries - "Cisco" - field=="name";value=="Cisco" - fields=in=("name");value=="Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.
- `singleObjectResponse` [query] (boolean): Specifiy whether to include array fields in the response, This query param should use only if the response contain single record, if we are using for multiple objects response query param not supported and throws an exception.
- `provisioningView` [query] (boolean): If set to true, the API will only return data that user has access to, according to User Profile.

## Respuestas
- **200**: OK
  - `meta` (object):
  - `data` (array):
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string) **(requerido)**: A name for the Desktop Layout.
    - `description` (string): A short description indicating the context of the Desktop Layout.
    - `editedBy` (string) **(requerido)**: Indicates who modified the Desktop Layout.
    - `jsonFileName` (string) **(requerido)**: Enter the name of the file.
    - `jsonFileContent` (string) **(requerido)**: Enter the Desktop Layout json.
    - `global` (boolean) **(requerido)**: Indicates if the Desktop Layout is a global layout or a custom layout.
    - `status` (boolean) **(requerido)**: Indicates if the Desktop Layout is in active state or inactive.
    - `defaultJsonModified` (boolean) **(requerido)**: Indicates if the default Desktop Layout is modified.
    - `validated` (boolean) **(requerido)**: Indicates if the Desktop Layout is validated.
    - `validatedTime` (integer): Validated time(in epoch milliseconds) of this resource.
    - `defaultJsonModifiedTime` (integer): Default Json Modified time(in epoch milliseconds) of this resource.
    - `modifiedTime` (integer): Modified time(in epoch milliseconds) of this resource.
    - `teamIds` (array): Specify the teams id to assign to this Desktop Layout.
    - `systemDefault` (boolean): Indicates whether the created resource is system created or not
    - `createdTime` (integer): This is the created time of the entity.
    - `lastUpdatedTime` (integer): This is the updated time of the entity.
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
