---
doc_id: webex-contact-center-get-organization-orgid-v2-team
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/v2/team
operation_id: getAllConfigWithMetaDataTeam
tags: Team
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.714301+00:00
---

# GET /organization/{orgid}/v2/team

**API:** Webex Contact Center
**Área:** Team
**operationId:** `getAllConfigWithMetaDataTeam`

## Resumen
List Teams

## Descripción
Retrieve a list of Teams in a given organization. Note: Returning array fields in the List (Get All) API response is deprecated. To retrieve the complete resource with all fields, please use the Get-by-ID API instead.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. All the fields are supported except: organizationId, userIds, queueRankings, createdTime, lastUpdatedTime   Use the userId field to filter teams associated with the provided user.  The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `attributes` [query] (string/string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported. except (userIds, queueRankings)
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(name, description)  The examples below show some search queries - "Cisco" - field=="name";value=="Cisco" - fields=in=("name","description");value=="Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.
- `supervisorView` [query] (boolean): If set to true, the API will only return data that the user has access to, according to the User Profile. Por defecto: False.
- `provisioningView` [query] (boolean): If set to true, the API will only return data that the user has access to, according to the User Profile. Por defecto: False.
- `singleObjectResponse` [query] (boolean): Specify whether to include array fields in the response. This query parameter should be used only when the response contains a single record. It is not supported for responses with multiple objects and throws an exception. Por defecto: False.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/v2/team' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `meta` (object): Additional properties for Meta.
- `data` (array): List of Data.
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string): Indicates the name of the team such as Billing or Customer Support
  - `teamType` (string): Team type can be the following:  AGENT: A specific number of agents are assigned to the team.  CAPACITY: Specific number of agents not assigned to the team. Capacity-based teams for voice mailboxes or agent groups that are not managed by the Webex Contact Center system. Valores: AGENT, CAPACITY.
  - `teamStatus` (string): Indicates whether the team is available to handle customer contacts. Can be one of: IN_SERVICE/NOT_AVAILABLE. Valores: IN_SERVICE, NOT_AVAILABLE.
  - `dialedNumber` (string): The dial number where the system distributes the calls for this team.  This setting is applicable only for capacity-based teams.
  - `capacity` (integer/int32): The maximum number of simultaneous contacts that this team can handle. This setting is applicable only for capacity-based teams.
  - `active` (boolean): Indicates whether the team is active(when true) or not active(when false).
  - `siteId` (string): Identifier for a site which is a physical contact center location under the control of your enterprise.
  - `desktopLayoutId` (string): Identifier for an agent desktop layout which  a Contact Center administrator has configured.
  - `siteName` (string): The name of the site this team belongs to.
  - `skillProfileId` (string): Id of the skill profile for this team if your enterprise uses the optional Skills-Based Routing feature.
  - `multiMediaProfileId` (string): Id of the multimedia profile for this team.
  - `userIds` (array): Indicates the agents id(s) who are part of this team.
  - `description` (string): Indicates the team
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not
  - `rankQueuesForTeam` (boolean): Rank Queues For Team.
  - `queueRankings` (array): List of Queue Rankings.
    - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `queueId` (string) (**requerido**): Queue Id.
    - `rank` (integer/int32) (**requerido**): Rank.
    - `createdTime` (integer/int64): This is the created time of the entity.
    - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
  - `createdTime` (integer/int64): This is the created time of the entity.
  - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

### Ejemplo — respuesta 200
```json
{
  "data": [
    {
      "active": true,
      "description": "string",
      "version": 1,
      "skillProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
      "capacity": 1,
      "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
      "dialedNumber": "+14085550123",
      "systemDefault": false,
      "rankQueuesForTeam": true,
      "multiMediaProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
      "name": "inline-pcs-team",
      "siteId": "8e6bb6da-2a78-4768-bef9-7e229f92af22",
      "createdTime": 123456789,
      "lastUpdatedTime": 123456789,
      "id": "93912f11-6017-404b-bf14-5331890b1797",
      "teamType": "AGENT",
      "teamStatus": "IN_SERVICE",
      "desktopLayoutId": "f53c8b54-46ca-43f6-ba05-08426a46e23d"
    }
  ],
  "meta": {
    "additionalProp3": "string",
    "additionalProp2": "string",
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