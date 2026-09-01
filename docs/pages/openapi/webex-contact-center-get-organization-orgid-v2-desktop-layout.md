---
doc_id: webex-contact-center-get-organization-orgid-v2-desktop-layout
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/v2/desktop-layout
operation_id: getAllConfigWithMetaData_14
tags: Desktop Layout
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.659920+00:00
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
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. All the fields are supported except: organizationId, validatedTime, defaultJsonModifiedTime, modifiedTime, teamIds, createdTime, lastUpdatedTime   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `attributes` [query] (string/string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported.
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(name)  The examples below show some search queries - "Cisco" - field=="name";value=="Cisco" - fields=in=("name");value=="Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.
- `singleObjectResponse` [query] (boolean): Specifiy whether to include array fields in the response, This query param should use only if the response contain single record, if we are using for multiple objects response query param not supported and throws an exception. Por defecto: False.
- `provisioningView` [query] (boolean): If set to true, the API will only return data that user has access to, according to User Profile. Por defecto: False.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/v2/desktop-layout' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `meta` (object):
- `data` (array):
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string) (**requerido**): A name for the Desktop Layout. Long. max: 255.
  - `description` (string): A short description indicating the context of the Desktop Layout. Long. max: 255.
  - `editedBy` (string) (**requerido**): Indicates who modified the Desktop Layout. Long. max: 255.
  - `jsonFileName` (string) (**requerido**): Enter the name of the file. Long. max: 255.
  - `jsonFileContent` (string) (**requerido**): Enter the Desktop Layout json.
  - `global` (boolean) (**requerido**): Indicates if the Desktop Layout is a global layout or a custom layout.
  - `status` (boolean) (**requerido**): Indicates if the Desktop Layout is in active state or inactive.
  - `defaultJsonModified` (boolean) (**requerido**): Indicates if the default Desktop Layout is modified.
  - `validated` (boolean) (**requerido**): Indicates if the Desktop Layout is validated.
  - `validatedTime` (integer/int64): Validated time(in epoch milliseconds) of this resource.
  - `defaultJsonModifiedTime` (integer/int64): Default Json Modified time(in epoch milliseconds) of this resource.
  - `modifiedTime` (integer/int64): Modified time(in epoch milliseconds) of this resource.
  - `teamIds` (array): Specify the teams id to assign to this Desktop Layout.
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not
  - `createdTime` (integer/int64): This is the created time of the entity.
  - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

### Ejemplo — respuesta 200
```json
{
  "data": [
    {
      "modifiedTime": 1617536244000,
      "defaultJsonModifiedTime": 1617536244000,
      "editedBy": "System",
      "jsonFileName": "Desktop Layout.json",
      "description": "This is the global layout",
      "validatedTime": 1617536244000,
      "global": true,
      "version": 1,
      "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
      "systemDefault": false,
      "validated": false,
      "defaultJsonModified": true,
      "name": "New Desktop Layout",
      "createdTime": 123456789,
      "lastUpdatedTime": 123456789,
      "id": "93912f11-6017-404b-bf14-5331890b1797",
      "jsonFileContent": {
        "version": "0.0.6",
        "appTitle": "Contact Center Desktop",
        "logo": "",
        "dragDropEnabled": false,
        "notificationTimer": 8,
        "maximumNotificationCount": 3,
        "browserNotificationTimer": 8,
        "wxmConfigured": false,
        "area": {
          "headless": {
            "id": "dw-headless",
            "widgets": {
              "comp1": {
                "comp": "div"
              }
            },
            "layout": {
              "areas": [
                [
                  "comp1"
                ]
              ],
              "size": {
                "cols": [
                  1
                ],
                "rows": [
                  1
                ]
              }
            }
          }
        }
      },
      "status": true
    }
  ],
  "meta": {
    "additio
  ... (truncado)
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