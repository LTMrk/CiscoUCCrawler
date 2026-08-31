---
doc_id: webex-contact-center-get-organization-orgid-v2-user
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/v2/user
operation_id: getAllConfigWithPagedMetaDataUser
tags: Users
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.738353+00:00
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
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. All the fields are supported except: organizationId, xspVersion, createdTime, lastUpdatedTime   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `attributes` [query] (string/string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported.
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(firstName, lastName, email)  The examples below show some search queries - "Cisco" - field=="firstName";value=="Cisco" - fields=in=("firstName","lastName");value=="Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.
- `supervisorManagedAgentsOnly` [query] (boolean): If set to true, the API will return contact center enabled users based on the invoking supervisor user's user profile access rights to sites and teams. Por defecto: False.
- `singleObjectResponse` [query] (boolean): Specify whether to include array fields in the response. This query parameter should be used only when the response contains a single record. It is not supported for responses with multiple objects and throws an exception. Por defecto: False.
- `buddyTeamAgentsOnly` [query] (boolean): If set to true, returns only users who are part of buddy teams without PBAC check. Por defecto: False.
- `userInQueue` [query] (string): Can be either assigned or unassigned. If passed, returns the users who are assigned or not assigned to an agent based queue managed by the supervisor.
- `queueId` [query] (string): Contact Service Queue ID for which the list of assigned or unassigned agents must be fetched.
- `includeAIMappingCount` [query] (boolean): If set to true, the API response will include the count of each AI feature mapped to the entity. Por defecto: False.
- `includeDynamicSkillsLimitReached` [query] (boolean): If true, includes whether each user has reached the dynamic skills assignment limit. Por defecto: False.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/v2/user' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `meta` (object): Meta Data Paged User schema.
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
  - `actualBurnoutInclusionCount` (integer/int64): Indicates the actual count of Agents selected for Agent burnout detection, including restricted agents that are not visible to requesting user.
  - `actualAutoCSATCount` (integer/int64): Indicates the actual count of Agents selected for Auto CSAT scores, including restricted agents that are not visible to requesting user.
  - `actualSummariesCount` (integer/int64): Indicates the actual count of Agents selected for Generated Summaries, including restricted agents that are not visible to requesting user.
- `data` (array):
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
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
  - `active` (boolean): Specify whether the user is active or not active.
  - `dbId` (string): Legacy identifier for migrated users.
  - `userProfileData` (object): User profile data transfer object that defines access permissions and resource scope for contact center users
    - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string) (**requerido**): The name of the user profile. Long. max: 80.
    - `description` (string): An optional description of the profile. Long. max: 255.
    - `profileType` (string) (**requerido**): The type determines the privileges applicable for a profile.  It can take one of these values:  STANDARD_AGENT — Has access to Agent Desktop[m_agent_desktop] module.  PREMIUM_AGENT — Has access to Agent Desktop[m_agent_desktop] and Multimedia[m_multimedia] module.  SUPERVISOR — Has access to all modules except to manage tenants in the Provisioning[m_provisioning] module.  ADMINISTRATOR — Has access to all modules.  ADMINISTRATOR_ONLY — Has access to Provisioning[m_provisioning], Real Time Reports[m_real_time_reports], Call Recording[m_call_recording], IMI Digital Channels[m_imi_digital_channels], and Routing Strategy[m_routing_strategy] modules.  It is required only during a create operation.   The profile type cannot be changed for an existing user profile. Valores: ADMINISTRATOR, ADMINISTRATOR_ONLY, SUPERVISOR, PREMIUM_AGENT, STANDARD_AGENT, ANALYZER_ADMINISTRATOR, ANALYZER_SUPERVISOR, ANALYZER_USER.
    - `accessAllModules` (string) (**requerido**): This can be used to allow users of this profile access to specific or all the Webex Contact Center modules.  It can take one of these values:  ALL — A contact center user with this profile can access all Contact Center modules.  SPECIFIC — A contact center user with this profile can access only specific modules. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
    - `userProfileAppModules` (array): Specifies the module(s) a user of this profile has access to.  It should be chosen when module access is SPECIFIC.  Please specify all the following modules and their respective access type.
      - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
      - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
      - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
      - `appModuleId` (string) (**requerido**): The code of a Webex Contact Center module.   Please specify descriptions for each of these modules:  m_provisioning - Refers to the provisioning module. Has access to Manage EntryPoints and Queues[f_manage_entrypt_queue], Revoke API Key[f_revoke_api_key], DN Mappings[f_dn_mappings], Manage User Profiles[f_manage_user_profiles], Manage Tenants[f_manage_tenants], Manage Users[f_manage_users], Portal Branding[f_portal_branding], Audit Trail[f_audit_trail], Manage Sites[f_manage_sites], Manage Teams[f_manage_teams], and Manage Dial Plans[f_manage_dial_plans] features.  m_real_time_reports - Refers to the real time reporting module. Has access to Summary View[f_summary_view], Agent State Change[f_agent_state_change], Real Time Threshold Alerts[f_realtime_threshold_alerts], and Web CallBack Report[f_web_callback_report] features.  m_historical_reports - Refers to the historical reporting module.  m_routing_strategy - Refers to the routing strategy module. Has access to Manage Media Files[f_manage_media_files] and Manage Call Flow Scripts[f_manage_call_flow_scripts] features.  m_call_recording - Refers to the call recording module.  m_call_monitoring - Refers to the call monitoring module. Has access to Barge In[f_barge_in], View Blind Monitor Request[f_view_blind_monitor_requests], Whisper Coach[f_whisper_coach], Mid Call Monitor[f_mid_call_monitor], and Restricted Monitor[f_restricted_monitor_only] features.  m_reporting_analytics - Refers to the reporting analytics module. Has access to Analyzer Data Exchange[f_analyzer_data_exchange] and Business Rules[f_business_rules] features.   m_recording_management - Refers to the recording management module. Has access to Tags[f_tags], Security Keys[f_security_keys], Manage Recordings[f_manage_recordings], and Custom Attributes[f_custom_attributes] features.  m_agent_desktop - Refers to the agent desktop module.  m_logout_agents - Refers to the agent logout module.  m_manage_agent_states - Refers to the agent state module. Has access to Sign Out Agent[f_sign_out_agent] and Change Agent State[f_change_agent_state] features.  m_additional_supervisory_features - Refers to the additional supervisory features module. Has access to Sign Out Agents[f_sign_out_agents], Change Agent States[f_change_agent_states] and Send Messages[f_send_messages] features.  m_multimedia - Refers to the multimedia module. Has access to Provisioning[f_mm_provisioning], Basic Digital[f_mm_basic_digital], Social Channel[f_mm_social_channel] and Agent Desktop[f_mm_agent_desktop] features.  m_agent_wellbeing - Refers to the Agent Wellbeing module. Has access to Agent Wellbeing provisioning features.  m_auto_csat - Refers to the Auto Csat module.  m_generated_summaries - Refers to the Generated Summaries module.  m_agent_personal_greetings - Refers to the Agent Personal Greetings module.  m_functions - Refers to the Functions in flow module.  m_realtime_transcripts - Refers to the Realtime Transcripts module.  m_suggested_responses - Refers to the Suggested Responses module.
      - `moduleAccessType` (string) (**requerido**): Indicates the access rights for a user of this profile for a Webex Contact Center module.  It can take be one of these values:  VIEW — A contact center user with this profile has read only access to a Contact Center module.  EDIT — A contact center user with this profile has read and write access to a Contact Center module.  NONE — A contact center user with this profile cannot access the module. Valores: NONE, VIEW, EDIT.
      - `userProfileAppFeature` (array): Specifies the module features(s) a user of this profile has access to.
        - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
        - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
        - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.

### Ejemplo — respuesta 200
```json
{
  "data": [
    {
      "imiUserCreated": false,
      "lastName": "Wick",
      "userLevelSummariesInclusion": "INCLUDED",
      "supervisorCapabilitiesEnabled": false,
      "timezone": "America/New_York",
      "preferredSupervisorTeamId": "2f9eecc5-0472-4549-9a83-2afdae0d4ba1",
      "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
      "broadCloudUserId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
      "externalIdentifier": "121212",
      "createdTime": 123456789,
      "lastUpdatedTime": 123456789,
      "id": "93912f11-6017-404b-bf14-5331890b1797",
      "contactCenterEnabled": true,
      "email": "johnwick@company.com",
      "ciUserId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
      "xspVersion": "xsp-24.0",
      "userLevelAutoCSATInclusion": "INCLUDED",
      "mobile": "1234567890",
      "active": true,
      "version": 1,
      "skillProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
      "firstName": "John",
      "userLevelWellnessBreakReminders": "DISABLED",
      "agentProfileId": "8e6bb6da-2a78-4768-bef9-7e229f92af22",
      "siteId": "8e6bb6da-2a78-4768-bef9-7e229f92af22",
      "userLevelBurnoutInclusion": "INCLUDED",
      "workPhone": "1234567890",
      "userProfileId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
      "multimediaProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
      "subscriptionId": "04d0bdf6-6d6a-4aae-8a8a-71c9152e6478",
      "agentCapabilitiesEnabled": false,
      "deafultDialledNumber": "1234567890"
    }
  ],
  "meta
  ... (truncado)
```
- `meta` (object): Meta Data Paged User schema.
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
  - `actualBurnoutInclusionCount` (integer/int64): Indicates the actual count of Agents selected for Agent burnout detection, including restricted agents that are not visible to requesting user.
  - `actualAutoCSATCount` (integer/int64): Indicates the actual count of Agents selected for Auto CSAT scores, including restricted agents that are not visible to requesting user.
  - `actualSummariesCount` (integer/int64): Indicates the actual count of Agents selected for Generated Summaries, including restricted agents that are not visible to requesting user.
- `data` (array):
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
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
  - `active` (boolean): Specify whether the user is active or not active.
  - `dbId` (string): Legacy identifier for migrated users.
  - `userProfileData` (object): User profile data transfer object that defines access permissions and resource scope for contact center users
    - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string) (**requerido**): The name of the user profile. Long. max: 80.
    - `description` (string): An optional description of the profile. Long. max: 255.
    - `profileType` (string) (**requerido**): The type determines the privileges applicable for a profile.  It can take one of these values:  STANDARD_AGENT — Has access to Agent Desktop[m_agent_desktop] module.  PREMIUM_AGENT — Has access to Agent Desktop[m_agent_desktop] and Multimedia[m_multimedia] module.  SUPERVISOR — Has access to all modules except to manage tenants in the Provisioning[m_provisioning] module.  ADMINISTRATOR — Has access to all modules.  ADMINISTRATOR_ONLY — Has access to Provisioning[m_provisioning], Real Time Reports[m_real_time_reports], Call Recording[m_call_recording], IMI Digital Channels[m_imi_digital_channels], and Routing Strategy[m_routing_strategy] modules.  It is required only during a create operation.   The profile type cannot be changed for an existing user profile. Valores: ADMINISTRATOR, ADMINISTRATOR_ONLY, SUPERVISOR, PREMIUM_AGENT, STANDARD_AGENT, ANALYZER_ADMINISTRATOR, ANALYZER_SUPERVISOR, ANALYZER_USER.
    - `accessAllModules` (string) (**requerido**): This can be used to allow users of this profile access to specific or all the Webex Contact Center modules.  It can take one of these values:  ALL — A contact center user with this profile can access all Contact Center modules.  SPECIFIC — A contact center user with this profile can access only specific modules. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
    - `userProfileAppModules` (array): Specifies the module(s) a user of this profile has access to.  It should be chosen when module access is SPECIFIC.  Please specify all the following modules and their respective access type.
      - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
      - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
      - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
      - `appModuleId` (string) (**requerido**): The code of a Webex Contact Center module.   Please specify descriptions for each of these modules:  m_provisioning - Refers to the provisioning module. Has access to Manage EntryPoints and Queues[f_manage_entrypt_queue], Revoke API Key[f_revoke_api_key], DN Mappings[f_dn_mappings], Manage User Profiles[f_manage_user_profiles], Manage Tenants[f_manage_tenants], Manage Users[f_manage_users], Portal Branding[f_portal_branding], Audit Trail[f_audit_trail], Manage Sites[f_manage_sites], Manage Teams[f_manage_teams], and Manage Dial Plans[f_manage_dial_plans] features.  m_real_time_reports - Refers to the real time reporting module. Has access to Summary View[f_summary_view], Agent State Change[f_agent_state_change], Real Time Threshold Alerts[f_realtime_threshold_alerts], and Web CallBack Report[f_web_callback_report] features.  m_historical_reports - Refers to the historical reporting module.  m_routing_strategy - Refers to the routing strategy module. Has access to Manage Media Files[f_manage_media_files] and Manage Call Flow Scripts[f_manage_call_flow_scripts] features.  m_call_recording - Refers to the call recording module.  m_call_monitoring - Refers to the call monitoring module. Has access to Barge In[f_barge_in], View Blind Monitor Request[f_view_blind_monitor_requests], Whisper Coach[f_whisper_coach], Mid Call Monitor[f_mid_call_monitor], and Restricted Monitor[f_restricted_monitor_only] features.  m_reporting_analytics - Refers to the reporting analytics module. Has access to Analyzer Data Exchange[f_analyzer_data_exchange] and Business Rules[f_business_rules] features.   m_recording_management - Refers to the recording management module. Has access to Tags[f_tags], Security Keys[f_security_keys], Manage Recordings[f_manage_recordings], and Custom Attributes[f_custom_attributes] features.  m_agent_desktop - Refers to the agent desktop module.  m_logout_agents - Refers to the agent logout module.  m_manage_agent_states - Refers to the agent state module. Has access to Sign Out Agent[f_sign_out_agent] and Change Agent State[f_change_agent_state] features.  m_additional_supervisory_features - Refers to the additional supervisory features module. Has access to Sign Out Agents[f_sign_out_agents], Change Agent States[f_change_agent_states] and Send Messages[f_send_messages] features.  m_multimedia - Refers to the multimedia module. Has access to Provisioning[f_mm_provisioning], Basic Digital[f_mm_basic_digital], Social Channel[f_mm_social_channel] and Agent Desktop[f_mm_agent_desktop] features.  m_agent_wellbeing - Refers to the Agent Wellbeing module. Has access to Agent Wellbeing provisioning features.  m_auto_csat - Refers to the Auto Csat module.  m_generated_summaries - Refers to the Generated Summaries module.  m_agent_personal_greetings - Refers to the Agent Personal Greetings module.  m_functions - Refers to the Functions in flow module.  m_realtime_transcripts - Refers to the Realtime Transcripts module.  m_suggested_responses - Refers to the Suggested Responses module.
      - `moduleAccessType` (string) (**requerido**): Indicates the access rights for a user of this profile for a Webex Contact Center module.  It can take be one of these values:  VIEW — A contact center user with this profile has read only access to a Contact Center module.  EDIT — A contact center user with this profile has read and write access to a Contact Center module.  NONE — A contact center user with this profile cannot access the module. Valores: NONE, VIEW, EDIT.
      - `userProfileAppFeature` (array): Specifies the module features(s) a user of this profile has access to.
        - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
        - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
        - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.

### Ejemplo — respuesta 200
```json
{
  "data": [
    {
      "imiUserCreated": false,
      "lastName": "Wick",
      "userLevelSummariesInclusion": "INCLUDED",
      "supervisorCapabilitiesEnabled": false,
      "timezone": "America/New_York",
      "preferredSupervisorTeamId": "2f9eecc5-0472-4549-9a83-2afdae0d4ba1",
      "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
      "broadCloudUserId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
      "externalIdentifier": "121212",
      "createdTime": 123456789,
      "lastUpdatedTime": 123456789,
      "id": "93912f11-6017-404b-bf14-5331890b1797",
      "contactCenterEnabled": true,
      "email": "johnwick@company.com",
      "ciUserId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
      "xspVersion": "xsp-24.0",
      "userLevelAutoCSATInclusion": "INCLUDED",
      "mobile": "1234567890",
      "active": true,
      "version": 1,
      "skillProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
      "firstName": "John",
      "userLevelWellnessBreakReminders": "DISABLED",
      "agentProfileId": "8e6bb6da-2a78-4768-bef9-7e229f92af22",
      "siteId": "8e6bb6da-2a78-4768-bef9-7e229f92af22",
      "userLevelBurnoutInclusion": "INCLUDED",
      "workPhone": "1234567890",
      "userProfileId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
      "multimediaProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
      "subscriptionId": "04d0bdf6-6d6a-4aae-8a8a-71c9152e6478",
      "agentCapabilitiesEnabled": false,
      "deafultDialledNumber": "1234567890"
    }
  ],
  "meta
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