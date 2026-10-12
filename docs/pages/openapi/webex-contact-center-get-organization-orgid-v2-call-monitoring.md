---
doc_id: webex-contact-center-get-organization-orgid-v2-call-monitoring
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/v2/call-monitoring
operation_id: getAllConfigWithPagedMetaDataCallMonitoring
tags: Call Monitoring Request
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-10-12T11:51:20.906585+00:00
---

# GET /organization/{orgid}/v2/call-monitoring

**API:** Webex Contact Center
**Área:** Call Monitoring Request
**operationId:** `getAllConfigWithPagedMetaDataCallMonitoring`

## Resumen
List Call Monitoring Configurations

## Descripción
Retrieve a list of Call Monitoring Configurations in a given organization. Note: Returning array fields in the List (Get All) API response is deprecated. To retrieve the complete resource with all fields, please use the Get-by-ID API instead.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. All the fields are supported except: organizationId, teams, agents, contactServiceQueues, createdTime, lastUpdatedTime   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `attributes` [query] (string/string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported. except  teams, agents, contactServiceQueues  The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(name)  The examples below show some search queries - "Cisco" - field=="name";value=="Cisco" - fields=in=("name");value=="Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.
- `includeUserDetails` [query] (boolean): If set to true, the API response will include user details (firstName, lastName, email) for the userId field. Por defecto: False.
- `includeFiltersCount` [query] (boolean): If set to true, the API response will include the count of specific agents, teams, and contact service queues associated with the call monitoring schedule. Por defecto: False.
- `includeTotalCallMonitoringCountInOrg` [query] (boolean): If set to true, the API response will include the total number of call monitoring schedules for the organization in the metadata. Por defecto: False.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/v2/call-monitoring' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `meta` (object): Pagination metadata for paged API responses
  - `orgid` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `page` (integer/int32): Current page number.
  - `pageSize` (integer/int32): Page size for current data set.
  - `totalPages` (integer/int32): Number of pages.
  - `totalRecords` (integer/int64): Total number of items.
  - `links` (object):
    - `self` (string) (**requerido**): Link to the current page.
    - `first` (string): Link to the first page.
    - `last` (string): Link to the last page.
    - `next` (string): Link to the next page.
    - `prev` (string): Link to the previous page.
- `data` (array):
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string): Name of the call monitoring schedule Long. max: 80.
  - `timezone` (string): (Optional) The time zone that you provision for your enterprise.
  - `recurrence` (boolean): Indicates if this is a recurring schedule
  - `daysOfWeek` (array): Days of the week when the schedule is active
  - `agentsAccessType` (string): Access type for agents - ALL or SPECIFIC
  - `startTimestamp` (integer/int64): Start timestamp of the schedule in epoch milliseconds (UTC)
  - `endTimestamp` (integer/int64): End timestamp of the schedule in epoch milliseconds (UTC)
  - `userId` (string): User ID of the supervisor who created/owns this schedule
  - `userDetails` (object): User details containing name and email
    - `firstName` (string): First name of the user
    - `lastName` (string): Last name of the user
    - `email` (string): Email of the user
  - `paused` (boolean): Indicates if the schedule is paused
  - `filtersCount` (object): Count of specific agents, teams, and contact service queues
    - `specificAgents` (integer/int32): Count of specific agents
    - `specificCsqs` (integer/int32): Count of specific contact service queues
    - `specificTeams` (integer/int32): Count of specific teams
  - `createdTime` (integer/int64): This is the created time of the entity.
  - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

### Ejemplo — respuesta 200
```json
{
  "data": [
    {
      "paused": false,
      "timezone": "America/New_York",
      "filtersCount": "string",
      "daysOfWeek": [
        "MON",
        "TUE",
        "WED",
        "THU",
        "FRI"
      ],
      "version": 1,
      "userId": "cbad1d19-9904-433e-9af6-04d4a013ed1e",
      "userDetails": "string",
      "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
      "recurrence": true,
      "name": "Morning Shift Monitoring",
      "agentsAccessType": "SPECIFIC",
      "createdTime": 123456789,
      "lastUpdatedTime": 123456789,
      "id": "93912f11-6017-404b-bf14-5331890b1797",
      "endTimestamp": 1772244000000,
      "startTimestamp": 1772169240000
    }
  ],
  "meta": {
    "additionalProp2": "string",
    "additionalProp3": "string",
    "additionalProp1": "string"
  }
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