---
doc_id: webex-contact-center-get-organization-orgid-overrides
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/overrides
operation_id: getAllConfig_4
tags: Overrides
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.058655+00:00
---

# GET /organization/{orgid}/overrides

**API:** Webex Contact Center
**Área:** Overrides
**operationId:** `getAllConfig_4`

## Resumen
List Overrides resource(s)

## Descripción
Retrieve a list of Overrides resource(s) in a given organization.
 Note: Returning array fields in the List (Get All) API response is deprecated. To retrieve the complete resource with all fields, please use the Get-by-ID API instead.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. Supported filterable fields:  id.   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `attributes` [query] (string/string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported. except (overrides)
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.
- `singleObjectResponse` [query] (boolean): Specifiy whether to include array fields in the response, This query param should use only if the response contain single record, if we are using for multiple objects response query param not supported and throws an exception. Por defecto: False.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/overrides' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- (array de:)
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string): Enter a name for the agent profile. Long. max: 80.
  - `description` (string): (Optional) Enter a description of the profile. Long. max: 255.
  - `timezone` (string): The time zone that you provision for your overrides.
  - `latestOverride` (object):
    - `name` (string) (**requerido**):  Long. max: 80.
    - `startDateTime` (string):
    - `endDateTime` (string):
    - `workingHours` (boolean) (**requerido**):
    - `frequency` (string):  Valores: DontRepeat, Daily, Weekly, Monthly, Yearly.
    - `recurrence` (object):
      - `interval` (integer/int32) (**requerido**):
      - `occurrenceInTheMonth` (string):  Valores: FIRST, SECOND, THIRD, FOURTH, LAST.
      - `daysOfWeek` (array):
      - `specificDayOfMonth` (integer/int32):
      - `specificMonth` (string):  Valores: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC.
      - `endDate` (string):
  - `overridesCount` (integer/int64): Number of overrides configured for this resource.
  - `createdTime` (integer/int64): This is the created time of the entity.
  - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

### Ejemplo — respuesta 200
```json
[
  {
    "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
    "latestOverride": {
      "name": "Fire Drill",
      "startDateTime": "2022-05-26T14:30",
      "endDateTime": "2022-05-26T16:30",
      "workingHours": false
    },
    "timezone": "America/New_York",
    "overridesCount": 2,
    "name": "My Overrides",
    "description": "My Overrides Desc",
    "createdTime": 123456789,
    "lastUpdatedTime": 123456789,
    "id": "93912f11-6017-404b-bf14-5331890b1797",
    "version": 1
  }
]
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