---
doc_id: webex-contact-center-get-organization-orgid-user
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/user
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.953816+00:00
---

# GET /organization/{orgid}/user

**API:** Webex Contact Center
**Área:** Users
**operationId:** `getAllConfigUser`

## Resumen
List Users

## Descripción
Retrieve a list of Users in a given organization. Note: Returning array fields in the List (Get All) API response is deprecated. To retrieve the complete resource with all fields, please use the Get-by-ID API instead. Deprecated. Use GET /v2/user instead.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. Supported filterable fields:  id.   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `attributes` [query] (string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.
- `singleObjectResponse` [query] (boolean): Specify whether to include array fields in the response. This query parameter should be used only when the response contains a single record. It is not supported for responses with multiple objects and throws an exception.

## Respuestas
- **200**: OK
  - (array de:)
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
    - `active` (boolean): Specify whether the user is active or not active.
    - `dbId` (string): Legacy identifier for migrated users.
    - `userProfileData` (object): User profile data transfer object that defines access permissions and resource scope for contact center users
      - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
      - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
      - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
      - `name` (string) **(requerido)**: The name of the user profile.
      - `description` (string): An optional description of the profile.
      - `profileType` (string) **(requerido)**: The type determines the privileges applicable for a profile.  It can take one of these values:  STANDARD_AGENT — Has access to Agent Desktop[m_agent_desktop] module.  PREMIUM_AGENT — Has access to Agent Desktop[m_agent_desktop] and Multimedia[m_multimedia] module.  SUPERVISOR — Has access to all modules except to manage tenants in the Provisioning[m_provisioning] module.  ADMINISTRATOR — Has access to all modules.  ADMINISTRATOR_ONLY — Has access to Provisioning[m_provisioning], Real Time Reports[m_real_time_reports], Call Recording[m_call_recording], IMI Digital Channels[m_imi_digital_channels], and Routing Strategy[m_routing_strategy] modules.  It is required only during a create operation.   The profile type cannot be changed for an existing user profile. Valores: ADMINISTRATOR, ADMINISTRATOR_ONLY, SUPERVISOR, PREMIUM_AGENT, STANDARD_AGENT, ANALYZER_ADMINISTRATOR, ANALYZER_SUPERVISOR, ANALYZER_USER.
      - `accessAllModules` (string) **(requerido)**: This can be used to allow users of this profile access to specific or all the Webex Contact Center modules.  It can take one of these values:  ALL — A contact center user with this profile can access all Contact Center modules.  SPECIFIC — A contact center user with this profile can access only specific modules. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
      - `userProfileAppModules` (array): Specifies the module(s) a user of this profile has access to.  It should be chosen when module access is SPECIFIC.  Please specify all the following modules and their respective access type.
        - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
        - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
        - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
        - `appModuleId` (string) **(requerido)**: The code of a Webex Contact Center module.   Please specify descriptions for each of these modules:  m_provisioning - Refers to the provisioning module. Has access to Manage EntryPoints and Queues[f_manage_entrypt_queue], Revoke API Key[f_revoke_api_key], DN Mappings[f_dn_mappings], Manage User Profiles[f_manage_user_profiles], Manage Tenants[f_manage_tenants], Manage Users[f_manage_users], Portal Branding[f_portal_branding], Audit Trail[f_audit_trail], Manage Sites[f_manage_sites], Manage Teams[f_manage_teams], and Manage Dial Plans[f_manage_dial_plans] features.  m_real_time_reports - Refers to the real time reporting module. Has access to Summary View[f_summary_view], Agent State Change[f_agent_state_change], Real Time Threshold Alerts[f_realtime_threshold_alerts], and Web CallBack Report[f_web_callback_report] features.  m_historical_reports - Refers to the historical reporting module.  m_routing_strategy - Refers to the routing strategy module. Has access to Manage Media Files[f_manage_media_files] and Manage Call Flow Scripts[f_manage_call_flow_scripts] features.  m_call_recording - Refers to the call recording module.  m_call_monitoring - Refers to the call monitoring module. Has access to Barge In[f_barge_in], View Blind Monitor Request[f_view_blind_monitor_requests], Whisper Coach[f_whisper_coach], Mid Call Monitor[f_mid_call_monitor], and Restricted Monitor[f_restricted_monitor_only] features.  m_reporting_analytics - Refers to the reporting analytics module. Has access to Analyzer Data Exchange[f_analyzer_data_exchange] and Business Rules[f_business_rules] features.   m_recording_management - Refers to the recording management module. Has access to Tags[f_tags], Security Keys[f_security_keys], Manage Recordings[f_manage_recordings], and Custom Attributes[f_custom_attributes] features.  m_agent_desktop - Refers to the agent desktop module.  m_logout_agents - Refers to the agent logout module.  m_manage_agent_states - Refers to the agent state module. Has access to Sign Out Agent[f_sign_out_agent] and Change Agent State[f_change_agent_state] features.  m_additional_supervisory_features - Refers to the additional supervisory features module. Has access to Sign Out Agents[f_sign_out_agents], Change Agent States[f_change_agent_states] and Send Messages[f_send_messages] features.  m_multimedia - Refers to the multimedia module. Has access to Provisioning[f_mm_provisioning], Basic Digital[f_mm_basic_digital], Social Channel[f_mm_social_channel] and Agent Desktop[f_mm_agent_desktop] features.  m_agent_wellbeing - Refers to the Agent Wellbeing module. Has access to Agent Wellbeing provisioning features.  m_auto_csat - Refers to the Auto Csat module.  m_generated_summaries - Refers to the Generated Summaries module.  m_agent_personal_greetings - Refers to the Agent Personal Greetings module.  m_functions - Refers to the Functions in flow module.  m_realtime_transcripts - Refers to the Realtime Transcripts module.  m_suggested_responses - Refers to the Suggested Responses module.
  - (array de:)
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
    - `active` (boolean): Specify whether the user is active or not active.
    - `dbId` (string): Legacy identifier for migrated users.
    - `userProfileData` (object): User profile data transfer object that defines access permissions and resource scope for contact center users
      - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
      - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
      - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
      - `name` (string) **(requerido)**: The name of the user profile.
      - `description` (string): An optional description of the profile.
      - `profileType` (string) **(requerido)**: The type determines the privileges applicable for a profile.  It can take one of these values:  STANDARD_AGENT — Has access to Agent Desktop[m_agent_desktop] module.  PREMIUM_AGENT — Has access to Agent Desktop[m_agent_desktop] and Multimedia[m_multimedia] module.  SUPERVISOR — Has access to all modules except to manage tenants in the Provisioning[m_provisioning] module.  ADMINISTRATOR — Has access to all modules.  ADMINISTRATOR_ONLY — Has access to Provisioning[m_provisioning], Real Time Reports[m_real_time_reports], Call Recording[m_call_recording], IMI Digital Channels[m_imi_digital_channels], and Routing Strategy[m_routing_strategy] modules.  It is required only during a create operation.   The profile type cannot be changed for an existing user profile. Valores: ADMINISTRATOR, ADMINISTRATOR_ONLY, SUPERVISOR, PREMIUM_AGENT, STANDARD_AGENT, ANALYZER_ADMINISTRATOR, ANALYZER_SUPERVISOR, ANALYZER_USER.
      - `accessAllModules` (string) **(requerido)**: This can be used to allow users of this profile access to specific or all the Webex Contact Center modules.  It can take one of these values:  ALL — A contact center user with this profile can access all Contact Center modules.  SPECIFIC — A contact center user with this profile can access only specific modules. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
      - `userProfileAppModules` (array): Specifies the module(s) a user of this profile has access to.  It should be chosen when module access is SPECIFIC.  Please specify all the following modules and their respective access type.
        - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
        - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
        - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
        - `appModuleId` (string) **(requerido)**: The code of a Webex Contact Center module.   Please specify descriptions for each of these modules:  m_provisioning - Refers to the provisioning module. Has access to Manage EntryPoints and Queues[f_manage_entrypt_queue], Revoke API Key[f_revoke_api_key], DN Mappings[f_dn_mappings], Manage User Profiles[f_manage_user_profiles], Manage Tenants[f_manage_tenants], Manage Users[f_manage_users], Portal Branding[f_portal_branding], Audit Trail[f_audit_trail], Manage Sites[f_manage_sites], Manage Teams[f_manage_teams], and Manage Dial Plans[f_manage_dial_plans] features.  m_real_time_reports - Refers to the real time reporting module. Has access to Summary View[f_summary_view], Agent State Change[f_agent_state_change], Real Time Threshold Alerts[f_realtime_threshold_alerts], and Web CallBack Report[f_web_callback_report] features.  m_historical_reports - Refers to the historical reporting module.  m_routing_strategy - Refers to the routing strategy module. Has access to Manage Media Files[f_manage_media_files] and Manage Call Flow Scripts[f_manage_call_flow_scripts] features.  m_call_recording - Refers to the call recording module.  m_call_monitoring - Refers to the call monitoring module. Has access to Barge In[f_barge_in], View Blind Monitor Request[f_view_blind_monitor_requests], Whisper Coach[f_whisper_coach], Mid Call Monitor[f_mid_call_monitor], and Restricted Monitor[f_restricted_monitor_only] features.  m_reporting_analytics - Refers to the reporting analytics module. Has access to Analyzer Data Exchange[f_analyzer_data_exchange] and Business Rules[f_business_rules] features.   m_recording_management - Refers to the recording management module. Has access to Tags[f_tags], Security Keys[f_security_keys], Manage Recordings[f_manage_recordings], and Custom Attributes[f_custom_attributes] features.  m_agent_desktop - Refers to the agent desktop module.  m_logout_agents - Refers to the agent logout module.  m_manage_agent_states - Refers to the agent state module. Has access to Sign Out Agent[f_sign_out_agent] and Change Agent State[f_change_agent_state] features.  m_additional_supervisory_features - Refers to the additional supervisory features module. Has access to Sign Out Agents[f_sign_out_agents], Change Agent States[f_change_agent_states] and Send Messages[f_send_messages] features.  m_multimedia - Refers to the multimedia module. Has access to Provisioning[f_mm_provisioning], Basic Digital[f_mm_basic_digital], Social Channel[f_mm_social_channel] and Agent Desktop[f_mm_agent_desktop] features.  m_agent_wellbeing - Refers to the Agent Wellbeing module. Has access to Agent Wellbeing provisioning features.  m_auto_csat - Refers to the Auto Csat module.  m_generated_summaries - Refers to the Generated Summaries module.  m_agent_personal_greetings - Refers to the Agent Personal Greetings module.  m_functions - Refers to the Functions in flow module.  m_realtime_transcripts - Refers to the Realtime Transcripts module.  m_suggested_responses - Refers to the Suggested Responses module.
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
