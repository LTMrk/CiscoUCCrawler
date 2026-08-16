---
doc_id: webex-contact-center-get-organization-orgid-team
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/team
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.951136+00:00
---

# GET /organization/{orgid}/team

**API:** Webex Contact Center
**Área:** Team
**operationId:** `getAllConfigTeam`

## Resumen
List Teams

## Descripción
Retrieve a list of Teams in a given organization. Note: Returning array fields in the List (Get All) API response is deprecated. To retrieve the complete resource with all fields, please use the Get-by-ID API instead.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. Supported filterable fields:  id.   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `attributes` [query] (string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported. except (userIds, queueRankings)
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.
- `singleObjectResponse` [query] (boolean): Specify whether to include array fields in the response. This query parameter should be used only when the response contains a single record. It is not supported for responses with multiple objects and throws an exception.

## Respuestas
- **200**: OK
  - (array de:)
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string): Indicates the name of the team such as Billing or Customer Support
    - `teamType` (string): Team type can be the following:  AGENT: A specific number of agents are assigned to the team.  CAPACITY: Specific number of agents not assigned to the team. Capacity-based teams for voice mailboxes or agent groups that are not managed by the Webex Contact Center system. Valores: AGENT, CAPACITY.
    - `teamStatus` (string): Indicates whether the team is available to handle customer contacts. Can be one of: IN_SERVICE/NOT_AVAILABLE. Valores: IN_SERVICE, NOT_AVAILABLE.
    - `dialedNumber` (string): The dial number where the system distributes the calls for this team.  This setting is applicable only for capacity-based teams.
    - `capacity` (integer): The maximum number of simultaneous contacts that this team can handle. This setting is applicable only for capacity-based teams.
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
      - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
      - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
      - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
      - `queueId` (string) **(requerido)**: Queue Id.
      - `rank` (integer) **(requerido)**: Rank.
      - `createdTime` (integer): This is the created time of the entity.
      - `lastUpdatedTime` (integer): This is the updated time of the entity.
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
