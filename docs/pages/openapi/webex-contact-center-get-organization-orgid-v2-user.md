---
doc_id: webex-contact-center-get-organization-orgid-v2-user
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/v2/user
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.957904+00:00
---

# GET /organization/{orgid}/v2/user

**API:** Webex Contact Center
**Área:** Users
**operationId:** `getAllConfigWithPagedMetaDataUser`

## Resumen
List Users

## Descripción
Retrieve a list of Users in a given organization. Note: Returning array fields in the List (Get All) API response is deprecated. To retrieve the complete resource with all fields, please use the Get-by-ID API instead.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. All the fields are supported except: organizationId, xspVersion, createdTime, lastUpdatedTime   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `attributes` [query] (string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported.
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(firstName, lastName, email)  The examples below show some search queries - "Cisco" - field=="firstName";value=="Cisco" - fields=in=("firstName","lastName");value=="Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.
- `supervisorManagedAgentsOnly` [query] (boolean): If set to true, the API will return contact center enabled users based on the invoking supervisor user's user profile access rights to sites and teams.
- `singleObjectResponse` [query] (boolean): Specify whether to include array fields in the response. This query parameter should be used only when the response contains a single record. It is not supported for responses with multiple objects and throws an exception.
- `buddyTeamAgentsOnly` [query] (boolean): If set to true, returns only users who are part of buddy teams without PBAC check.
- `userInQueue` [query] (string): Can be either assigned or unassigned. If passed, returns the users who are assigned or not assigned to an agent based queue managed by the supervisor.
- `queueId` [query] (string): Contact Service Queue ID for which the list of assigned or unassigned agents must be fetched.
- `includeAIMappingCount` [query] (boolean): If set to true, the API response will include the count of each AI feature mapped to the entity.
- `includeDynamicSkillsLimitReached` [query] (boolean): If true, includes whether each user has reached the dynamic skills assignment limit.

## Respuestas
- **200**: OK
  - `meta` (object): Meta Data Paged User schema.
    - `orgid` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `page` (integer): Current page number.
    - `pageSize` (integer): Page size for current data set.
    - `totalPages` (integer): Number of pages.
    - `totalRecords` (integer): Total number of items.
    - `links` (object):
      - `self` (string) **(requerido)**: Link to the current page.
      - `first` (string): Link to the first page.
      - `last` (string): Link to the last page.
      - `next` (string): Link to the next page.
      - `prev` (string): Link to the previous page.
    - `actualBurnoutInclusionCount` (integer): Indicates the actual count of Agents selected for Agent burnout detection, including restricted agents that are not visible to requesting user.
    - `actualAutoCSATCount` (integer): Indicates the actual count of Agents selected for Auto CSAT scores, including restricted agents that are not visible to requesting user.
    - `actualSummariesCount` (integer): Indicates the actual count of Agents selected for Generated Summaries, including restricted agents that are not visible to requesting user.
  - `data` (array):
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `firstName` (string): The first name of the user.
    - `lastName` (string): The last name of the user.
    - `email` (string): The email address of the user.
    - `workPhone` (string): The work phone number of the user.
    - `mobile` (string): The mobile phone number of the user.
    - `ciUserId` (string): Cisco Common Identity user Id
    - `broadCloudUserId` (string): Broadcloud user Id
    - `timezone` (string): (Optional) The time zone that you provision for your enterprise.
    - `xspVersion` (string): (Optional) Used to subscribe for recording events.
    - `subscriptionId` (string): (Optional) Used to subscribe for recording events.
    - `userProfileId` (string): Identifier for an user profile which a Contact Center administrator has configured.
    - `userProfileType` (string): Type of the user profile associated to this user. This is an optional response parameter based on the query parameter includeUserProfileType.
    - `contactCenterEnabled` (boolean): The setting is for accessing Desktop to handle customer requests.
    - `siteId` (string): Details of site which a Contact Center administrator has configured for the user.
    - `siteName` (string): site name that user is associated with
    - `teamIds` (array): Specify the teams id which got assigned to this user.  Note: You can’t assign this profile to a capacity-based team.
    - `skillProfileId` (string): (Optional) If your enterprise uses the optional Skills-Based Routing feature, This profile overrides any skill profile at the team level that is associated with the agent
    - `agentProfileId` (string): Identifier for a Desktop Profile which is a group of permissions and Agent Desktop behaviors that you assign to specific users.
    - `multimediaProfileId` (string): (Optional) If your organization administrator enables Multimedia for your enterprise, you can select a multimedia profile for this team.
    - `deafultDialledNumber` (string): (Optional) The dial number of the agent.
    - `externalIdentifier` (string): (Optional) Agent identification details, such as the employee number.
  - `meta` (object): Meta Data Paged User schema.
    - `orgid` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `page` (integer): Current page number.
    - `pageSize` (integer): Page size for current data set.
    - `totalPages` (integer): Number of pages.
    - `totalRecords` (integer): Total number of items.
    - `links` (object):
      - `self` (string) **(requerido)**: Link to the current page.
      - `first` (string): Link to the first page.
      - `last` (string): Link to the last page.
      - `next` (string): Link to the next page.
      - `prev` (string): Link to the previous page.
    - `actualBurnoutInclusionCount` (integer): Indicates the actual count of Agents selected for Agent burnout detection, including restricted agents that are not visible to requesting user.
    - `actualAutoCSATCount` (integer): Indicates the actual count of Agents selected for Auto CSAT scores, including restricted agents that are not visible to requesting user.
    - `actualSummariesCount` (integer): Indicates the actual count of Agents selected for Generated Summaries, including restricted agents that are not visible to requesting user.
  - `data` (array):
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `firstName` (string): The first name of the user.
    - `lastName` (string): The last name of the user.
    - `email` (string): The email address of the user.
    - `workPhone` (string): The work phone number of the user.
    - `mobile` (string): The mobile phone number of the user.
    - `ciUserId` (string): Cisco Common Identity user Id
    - `broadCloudUserId` (string): Broadcloud user Id
    - `timezone` (string): (Optional) The time zone that you provision for your enterprise.
    - `xspVersion` (string): (Optional) Used to subscribe for recording events.
    - `subscriptionId` (string): (Optional) Used to subscribe for recording events.
    - `userProfileId` (string): Identifier for an user profile which a Contact Center administrator has configured.
    - `userProfileType` (string): Type of the user profile associated to this user. This is an optional response parameter based on the query parameter includeUserProfileType.
    - `contactCenterEnabled` (boolean): The setting is for accessing Desktop to handle customer requests.
    - `siteId` (string): Details of site which a Contact Center administrator has configured for the user.
    - `siteName` (string): site name that user is associated with
    - `teamIds` (array): Specify the teams id which got assigned to this user.  Note: You can’t assign this profile to a capacity-based team.
    - `skillProfileId` (string): (Optional) If your enterprise uses the optional Skills-Based Routing feature, This profile overrides any skill profile at the team level that is associated with the agent
    - `agentProfileId` (string): Identifier for a Desktop Profile which is a group of permissions and Agent Desktop behaviors that you assign to specific users.
    - `multimediaProfileId` (string): (Optional) If your organization administrator enables Multimedia for your enterprise, you can select a multimedia profile for this team.
    - `deafultDialledNumber` (string): (Optional) The dial number of the agent.
    - `externalIdentifier` (string): (Optional) Agent identification details, such as the employee number.
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
