---
doc_id: webex-contact-center-get-organization-orgid-v3-dial-number
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/v3/dial-number
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.940933+00:00
---

# GET /organization/{orgid}/v3/dial-number

**API:** Webex Contact Center
**Área:** Dial Number
**operationId:** `getAllConfigWithMetaDataV3`

## Resumen
List Dialed Number Mapping(s)

## Descripción
Retrieve a list of Dialed Number Mapping(s) in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. All the fields are supported except: organizationId, createdTime, lastUpdatedTime   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `attributes` [query] (string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported. except (links)
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(dialledNumber)  The examples below show some search queries - "Cisco" - field=="dialledNumber";value=="Cisco" - fields=in=("dialledNumber");value=="Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.
- `includeEntryPointName` [query] (boolean): If includeEntryPointName is set to true and entryPointName is in the attributes, the API will return entryPointName in the Get All response, and filtering, searching, and sorting on entryPointName will also be enabled.

## Respuestas
- **200**: OK
  - `meta` (object):
  - `data` (array):
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `dialledNumber` (string): The dialed number(DN) used to map to entry points.
    - `extension` (string): The extension used to map to entry points.
    - `routingPrefix` (string): The routing prefix is mapped to a location and can be prefixed with an extension
    - `esn` (string): The esn is routing prefix with extension
    - `routePointId` (string): The identifier of a route point of WxC which is similar to entry point of WxCC
    - `entryPointId` (string) **(requerido)**: The identifier of an entry point to which you want to map the DN.
    - `entryPointName` (string) **(requerido)**: The entryPoint name of the entryPointId.
    - `defaultAni` (boolean): The default dial number for the tenant to make outdial calls. The default dial number is displayed in the customer's caller ID, if an agent does not select a specific outdial ANI (Automatic Number Identification) for an outdial call.  A default value is automatically set once and entry point mapping is created
    - `location` (string): The ID of the location as configured on Webex Calling(applicable only for Webex Calling).
    - `regionId` (string): Specify the telephony region id.  You can pass id for one of these regions:  US (USA), CA (Canada), MX (Mexico), AU (Australia), SG (Singapore), GB (United Kingdom), DE (Germany)  You can retrieve it by calling /api/global/telephony-region API.
    - `createdTime` (integer): This is the created time of the entity.
    - `lastUpdatedTime` (integer): This is the updated time of the entity.
    - `dialledNumberDigits` (string):
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
