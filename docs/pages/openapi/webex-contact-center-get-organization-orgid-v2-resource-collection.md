---
doc_id: webex-contact-center-get-organization-orgid-v2-resource-collection
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/v2/resource-collection
operation_id: getAllResourceCollections
tags: Resource Collection
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:43.816983+00:00
---

# GET /organization/{orgid}/v2/resource-collection

**API:** Webex Contact Center
**Área:** Resource Collection
**operationId:** `getAllResourceCollections`

## Resumen
List Resource Collections

## Descripción
Retrieve a list of resource collections in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. All the fields are supported except: organizationId, createdTime, lastUpdatedTime   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `attributes` [query] (string/string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported.
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(name)  The examples below show some search queries - "Cisco" - field=="name";value=="Cisco" - fields=in=("name");value=="Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/v2/resource-collection' \
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
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) (**requerido**): The name of the resource collection. Long. max: 80.
  - `description` (string): An optional description of the resource collection. Long. max: 255.
  - `resources` (array): The name of the resource and Type of resource list.
    - `name` (string) (**requerido**): The name of the resource.multimedia-profile - Has access to multimedia profile[multimedia-profile] resource name.  queue - Has access to queue[queue] resource name.  override - Has access to override[override] resource name.  holiday-list - Has access to holiday list[holiday-list] resource name.  audio-prompt - Has access to audio prompt[audio-prompt] resource name.  flow - Has access to flow[flow] resource name.  skill-profile - Has access to skill profile[skill-profile] resource name.  team - Has access to team[team] resource name.  skill-definition - Has access to skill definition[skill-definition] resource name.  site - Has access to site[site] resource name.  outdial-ani - Has access to outdial ani[outdial-ani] resource name.  channel - Has access to channel[channel] resource name.  sub-flow - Has access to sub flow[sub-flow] resource name.  desktop-layout - Has access to desktop layout[desktop-layout] resource name.  working-hour - Has access to working hour[working-hour] resource name.  function - Has access to function[function] resource name.  desktop-profile - Has access to desktop profile[desktop-profile] resource name.  idle-wrapup-code - Has access to idle wrap-up code[idle-wrapup-code] resource name.  cad-variable - Has access to cad variable[cad-variable] resource name.  address-book - Has access to address book[address-book] resource name.
    - `accessLevel` (string) (**requerido**): This can be used to allow users to access specific, none or all resources. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
    - `ids` (array): The id of the resource can be used to allow users to access specific, of resources.
  - `resourceCount` (integer/int64): The total count of resources in this collection
  - `createdTime` (integer/int64): This is the created time of the entity.
  - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

### Ejemplo — respuesta 200
```json
{
  "meta": {
    "orgid": "2f9eecc5-0472-4549-9a83-2afdae0d4ba1",
    "page": 1,
    "pageSize": 100,
    "totalPages": 1,
    "totalRecords": 1000,
    "links": {
      "next": "/organization/bde75a64-f4d5-4ffc-a239-feb607c17ef8/resource-collection?page=2&pageSize=10",
      "last": "/organization/bde75a64-f4d5-4ffc-a239-feb607c17ef8/resource-collection?page=3&pageSize=10",
      "prev": "/organization/bde75a64-f4d5-4ffc-a239-feb607c17ef8/resource-collection?page=0&pageSize=10",
      "self": "/organization/bde75a64-f4d5-4ffc-a239-feb607c17ef8/resource-collection?page=1&pageSize=10",
      "first": "/organization/bde75a64-f4d5-4ffc-a239-feb607c17ef8/resource-collection?page=0&pageSize=10"
    }
  },
  "data": [
    {
      "id": "80f49a6e-11d7-4651-b730-99ed2f726f61",
      "name": "Department1",
      "description": "Department1 description.",
      "resources": [
        {
          "name": "team",
          "accessLevel": "SPECIFIC",
          "ids": [
            "00734874-4732-43bb-bfff-d1e75d309eb1",
            "00734874-4732-43bb-bfff-d1e75d309eb2"
          ]
        },
        {
          "name": "desktop-profile",
          "accessLevel": "ALL"
        },
        {
          "name": "desktop-layout",
          "accessLevel": "NONE"
        }
      ],
      "resourceCount": 2
    }
  ]
}
```

## Respuestas de error
- **401**: Unauthorized Operation
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "401",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "401",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **403**: Operation is forbidden
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "403",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "403",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **404**: Resource not found or URI is invalid
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "404",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "404",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "429",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "429",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
- **500**: An Unexpected Error Occurred
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "500",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "500",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```

## Contexto de la API
The Webex Contact Center APIs allow developers to deeply integrate, configure, and manage cloud-based contact center solutions. These APIs cover agent lifecycle management, queue and routing configuration, customer journey tracking, and access to real-time and historical analytics. Use cases include embedding agent controls in custom UIs, automating workforce management, integrating with CRM and ticketing systems, and building custom reporting dashboards. The APIs empower organizations to deliver personalized, efficient customer experiences and optimize contact center operations.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs