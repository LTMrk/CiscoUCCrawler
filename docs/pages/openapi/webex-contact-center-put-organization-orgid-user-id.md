---
doc_id: webex-contact-center-put-organization-orgid-user-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PUT
path: /organization/{orgid}/user/{id}
operation_id: updateConfigUser
tags: Users
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.735768+00:00
---

# PUT /organization/{orgid}/user/{id}

**API:** Webex Contact Center
**Área:** Users
**operationId:** `updateConfigUser`

## Resumen
Update specific User by ID

## Descripción
Update an existing User by ID in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): Resource ID of the User.

## Cuerpo de la petición (application/json)
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `firstName` (string) (**requerido**): The first name of the user. Can be changed using Users Management in Cisco Webex Control Hub.
- `lastName` (string) (**requerido**): The last name of the user. Can be changed using Users Management in Cisco Webex Control Hub.
- `email` (string) (**requerido**): The email address of the user. Can be changed using Users Management in Cisco Webex Control Hub.
- `workPhone` (string): The work phone number of the user. Long. max: 20.
- `mobile` (string): The mobile phone number of the user. Long. max: 20.
- `ciUserId` (string) (**requerido**): Cisco Common Identity user Id. Existence of a CI user is a prerequisite to create a new WxCC user. It cannot be modified.
- `broadCloudUserId` (string): Broadcloud user Id. This field cannot be modified.
- `userProfileId` (string) (**requerido**): Identifier for an user profile which a Contact Center administrator has configured. Changing the profile type requires a token with `FLS:Read_Scope` scope.  As of today, changing the profile type for a user is supported only from Cisco Webex Control Hub.
- `contactCenterEnabled` (boolean) (**requerido**): The setting is for accessing the Agent Desktop to handle customer requests.
- `timezone` (string): (Optional) The time zone that you provision for your enterprise.
- `xspVersion` (string): (Optional) Used to subscribe for recording events. This field cannot be modified. Long. max: 80.
- `subscriptionId` (string): (Optional) Used to subscribe for recording events. This field cannot be modified. Long. max: 80.
- `siteId` (string): (Optional) Identifier for a site which is a physical contact center location under the control of your enterprise. This field is applicable only when contactCenterEnabled is true.
- `teamIds` (array): Specify the teams id which got assigned to this user.  Note: You can't assign this profile to a capacity-based team. This field is applicable only when contactCenterEnabled is true.
- `skillProfileId` (string): (Optional) If your enterprise uses the optional Skills-Based Routing feature, This profile overrides any skill profile at the team level that is associated with the agent.This field is applicable only when contactCenterEnabled is true.
- `agentProfileId` (string): Identifier for a Desktop Profile which is a group of permissions and Agent Desktop behaviors that you assign to specific users. This field is applicable only when contactCenterEnabled is true.
- `multimediaProfileId` (string): (Optional) If your organization administrator enables Multimedia for your enterprise, you can select a multimedia profile for this team. This field is applicable only when contactCenterEnabled is true.
- `deafultDialledNumber` (string): (Optional) The dial number of the agent. This field is applicable only when contactCenterEnabled is true.
- `externalIdentifier` (string): (Optional) Agent identification details, such as the employee number.
- `active` (boolean) (**requerido**): Indicates whether the user is active or not active. Can be changed using Users Management in Cisco Webex Control Hub.
- `imiUserCreated` (boolean): (Optional) Indicates whether this user has a corresponding user created in IMI digital channel. This field cannot be modified.
- `preferredSupervisorTeamId` (string): (Optional) Indicates the id of a preferred supervisor.
- `userLevelBurnoutInclusion` (string): User level burnout inclusion type. Used only when Agent inclusion is set to 'Specific Agents' at the org level Agent Wellbeing>Burnout config. If the value is missing in response, the consumer should assume a value as EXCLUDED. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained.This is applicable/available only when AI Assistant add-on offer/license is added to the organization. Valores: INCLUDED, EXCLUDED.
- `userLevelAutoCSATInclusion` (string) (DEPRECADO): User level AutoCSAT inclusion type. Used only when Agent inclusion is set to 'Specific Agents' at the org level Cisco AI Assistant>Auto CSAT config. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained. Valores: INCLUDED, EXCLUDED.
- `userLevelWellnessBreakReminders` (string): User level Wellness break reminder type. If top level Agent burnout config has wellness break reminders enabled, this property determines if an Agent is enabled/disabled for receiving break reminders. If the value is missing in response, the consumer should assume a value as DISABLED. This is applicable/available only when AI Assistant add-on offer/license is added to the organization. Valores: DISABLED, ENABLED.
- `userLevelSummariesInclusion` (string) (DEPRECADO): User level Generated Summaries inclusion type. Used only when Generated Summaries is set to 'Specific Agents' at the org level Cisco AI Assistant>Generated Summaries. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained. Valores: INCLUDED, EXCLUDED.
- `supervisorCapabilitiesEnabled` (boolean): Indicates whether supervisor capabilities are enabled for the user.
- `agentCapabilitiesEnabled` (boolean): Indicates whether agent capabilities are enabled for the user.
- `dynamicSkills` (array): The list of dynamic skills assigned to the user
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `skillId` (string) (**requerido**): The ID of the skill.
  - `skillName` (string): The name of the skill. Used for bulk upload operations to resolve skill by name instead of ID.
  - `textValue` (string): A short textual description that represents a skill the agent has. Long. max: 100.
  - `booleanValue` (boolean): Indicates whether the agent has this skill (True) or does not have the skill (False).
  - `proficiencyValue` (integer/int32): A number between 0 and 10 to indicate how proficient the agent is in this skill.
  - `enumValue` (string): The enum value for enum-type skills. Supports multiple values as pipe-delimited string (e.g., '30|20|10').
  - `enumSkillValues` (string): Indicates a value that represents a skill the agent has.
  - `createdTime` (integer/int64): This is the created time of the entity.
  - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
- `createdTime` (integer/int64): This is the created time of the entity.
- `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

### Ejemplo — petición
```json
{
  "firstName": "John",
  "lastName": "Wick",
  "email": "johnwick@company.com",
  "workPhone": "1234567890",
  "mobile": "1234567890",
  "ciUserId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "broadCloudUserId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "userProfileId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "contactCenterEnabled": true,
  "timezone": "America/New_York",
  "xspVersion": "xsp-24.0",
  "subscriptionId": "04d0bdf6-6d6a-4aae-8a8a-71c9152e6478",
  "siteId": "8e6bb6da-2a78-4768-bef9-7e229f92af22",
  "teamIds": [
    "f53c8b54-46ca-43f6-ba05-08426a46e23d"
  ],
  "skillProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "agentProfileId": "8e6bb6da-2a78-4768-bef9-7e229f92af22",
  "multimediaProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "deafultDialledNumber": "1234567890",
  "externalIdentifier": "121212",
  "active": true,
  "preferredSupervisorTeamId": "e27d2b54-46ca-43g6-ba65-08426e46e23d",
  "userLevelBurnoutInclusion": "INCLUDED",
  "userLevelAutoCSATInclusion": "INCLUDED",
  "userLevelWellnessBreakReminders": "DISABLED",
  "userLevelSummariesInclusion": "INCLUDED",
  "supervisorCapabilitiesEnabled": false,
  "agentCapabilitiesEnabled": true,
  "dynamicSkills": [
    {
      "skillId": "af9eecc5-0472-4549-9a83-2afdae0d4ba0",
      "proficiencyValue": 7
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PUT '/organization/<orgid>/user/<id>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"active": true, "ciUserId": "<ciUserId>", "contactCenterEnabled": true, "email": "<email>", "firstName": "<firstName>", "lastName": "<lastName>"}'
```

## Respuestas correctas
**200**: OK
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
      - `appFeatureId` (string) (**requerido**): The feature code of a Webex Contact Center module.   Please add all the following features with their respective modules and set it's featureAccessType to 'ON' or 'OFF', to specify if it is in use. Here is the complete list of Feature names and Feature Ids:   For module 'm_additional_supervisory_features' we have the following features:  Change Agent States : f_change_agent_states  Sign out Agents : f_sign_out_agents  Send Messages : f_send_messages  Re-skill Agents : f_reskill_agents  Manage agent based queues : f_manage_agent_queue_assignments  For module 'm_real_time_reports' we have the following features:  Real Time Threshold Alerts : f_realtime_threshold_alerts  Agent State Change : f_agent_state_change  Summary View : f_summary_view  Web Callback Report : f_web_callback_report   For module 'm_multimedia' we have the following features:  MM Agent Desktop : f_mm_agent_desktop  Basic Digital : f_mm_basic_digital  MM Provisioning : f_mm_provisioning  Social Channel : f_mm_social_channel   For module 'm_reporting_analytics' we have the following features:  Analyzer Data Exchange : f_analyzer_data_exchange  Business Rules : f_business_rules   For module 'm_manage_agent_states' we have the following features:  Change Agent State : f_change_agent_state  Sign Out Agent : f_sign_out_agent   For module 'm_recording_management' we have the following features:  Custom Attributes : f_custom_attributes  Manage Recordings : f_manage_recordings  Tags : f_tags  Security Keys : f_security_keys   For module 'm_routing_strategy' we have the following features:  Manage Call Flow Scripts : f_manage_call_flow_scripts  Manage Media Files : f_manage_media_files   For module 'm_provisioning' we have the following features:  Manage EntryPoints and Queues : f_manage_teams  Manage Users : f_manage_users  DN Mappings : f_dn_mappings  Manage Sites : f_manage_sites  Manage Teams : f_manage_teams  Manage User Profiles : f_manage_user_profiles  Revoke API Key : f_revoke_api_key  Manage Dial Plans : f_manage_dial_plans  Manage Tenants : f_manage_tenants  Manage Entry Points and Queues : f_manage_entrypt_queue  Portal Branding : f_portal_branding  Audit Trail : f_audit_trail  Manage Business Hours : f_manage_business_hours   For module 'm_call_monitoring' we have the following features:  Mid Call Monitoring : f_mid_call_monitor  Barge In : f_barge_in  Restricted Monitor : f_restricted_monitor_only  Whisper Coach : f_whisper_coach  View Blind Monitor Request : f_view_blind_monitor_requests
      - `appFeatureName` (string): The feature name of the Webex Contact Center module.
      - `featureAccessType` (string) (**requerido**): Indicates whether a user of this profile has access to a module feature.  It can be one of these values:  OFF — A contact center user with this profile cannot access this module feature.  ON — A contact center user with this profile can access this module feature. Valores: OFF, ON.
      - `createdTime` (integer/int64): This is the created time of the entity.
      - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
    - `createdTime` (integer/int64): This is the created time of the entity.
    - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
  - `accessAllEntryPoints` (string) (**requerido**): Allow users of this profile access to specific or all the entry points for an organization.  It can take one of these values:  ALL — A contact center user with this profile can access all the entry points for an organization.  SPECIFIC — A contact center user with this profile can access only specific entry points for an organization. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `accessAllSites` (string) (**requerido**): Allow users of this profile access to specific or all the sites for an organization.  It can take one of these values:  ALL — A contact center user with this profile can access all the sites for an organization.  SPECIFIC — A contact center user with this profile can access only specific sites for an organization. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `accessAllQueues` (string) (**requerido**): Allow users of this profile access to specific or all the contact center queues for an organization.  It can take one of these values:  ALL — A contact center user with this profile can access all the contact center queues for an organization.  SPECIFIC — A contact center user with this profile can access only specific contact center queues for an organization. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `accessAllTeams` (string) (**requerido**): Allow users of this profile access to specific or all the contact center teams for an organization.  It can take one of these values:  ALL — A contact center user with this profile can access all the contact center teams for an organization.  SPECIFIC — A contact center user with this profile can access only specific contact center teams for an organization. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `active` (boolean) (**requerido**): Specify whether the User profile is active or not.
  - `editableFolderIds` (array): Indicates the id(s) of the reporting folders a user of this profile has read and write access to.
  - `viewableFolderIds` (array): Indicates the id(s) of the reporting folders a user of this profile has read access to.
  - `nonViewableFolderIds` (array): Indicates the id(s) of the restricted reporting folders for a user of this profile.
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not

### Ejemplo — respuesta 200
```json
{
  "id": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "firstName": "John",
  "lastName": "Wick",
  "email": "johnwick@company.com",
  "workPhone": "1234567890",
  "mobile": "1234567890",
  "ciUserId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "broadCloudUserId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "timezone": "America/New_York",
  "userProfileId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "userProfileType": "PREMIUM_AGENT",
  "contactCenterEnabled": true,
  "siteId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "siteName": "bengaluru",
  "teamIds": [
    "f53c8b54-46ca-43f6-ba05-08426a46e23d"
  ],
  "skillProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "agentProfileId": "8e6bb6da-2a78-4768-bef9-7e229f92af22",
  "multimediaProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "deafultDialledNumber": "1234567890",
  "externalIdentifier": "121212",
  "active": true,
  "imiUserCreated": true,
  "systemDefault": false,
  "userLevelBurnoutInclusion": "INCLUDED",
  "userLevelAutoCSATInclusion": "INCLUDED",
  "userLevelWellnessBreakReminders": "DISABLED",
  "userLevelSummariesInclusion": "INCLUDED",
  "createdTime": 1679392200000,
  "lastModifiedTime": 1679392200000
}
```
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
      - `appFeatureId` (string) (**requerido**): The feature code of a Webex Contact Center module.   Please add all the following features with their respective modules and set it's featureAccessType to 'ON' or 'OFF', to specify if it is in use. Here is the complete list of Feature names and Feature Ids:   For module 'm_additional_supervisory_features' we have the following features:  Change Agent States : f_change_agent_states  Sign out Agents : f_sign_out_agents  Send Messages : f_send_messages  Re-skill Agents : f_reskill_agents  Manage agent based queues : f_manage_agent_queue_assignments  For module 'm_real_time_reports' we have the following features:  Real Time Threshold Alerts : f_realtime_threshold_alerts  Agent State Change : f_agent_state_change  Summary View : f_summary_view  Web Callback Report : f_web_callback_report   For module 'm_multimedia' we have the following features:  MM Agent Desktop : f_mm_agent_desktop  Basic Digital : f_mm_basic_digital  MM Provisioning : f_mm_provisioning  Social Channel : f_mm_social_channel   For module 'm_reporting_analytics' we have the following features:  Analyzer Data Exchange : f_analyzer_data_exchange  Business Rules : f_business_rules   For module 'm_manage_agent_states' we have the following features:  Change Agent State : f_change_agent_state  Sign Out Agent : f_sign_out_agent   For module 'm_recording_management' we have the following features:  Custom Attributes : f_custom_attributes  Manage Recordings : f_manage_recordings  Tags : f_tags  Security Keys : f_security_keys   For module 'm_routing_strategy' we have the following features:  Manage Call Flow Scripts : f_manage_call_flow_scripts  Manage Media Files : f_manage_media_files   For module 'm_provisioning' we have the following features:  Manage EntryPoints and Queues : f_manage_teams  Manage Users : f_manage_users  DN Mappings : f_dn_mappings  Manage Sites : f_manage_sites  Manage Teams : f_manage_teams  Manage User Profiles : f_manage_user_profiles  Revoke API Key : f_revoke_api_key  Manage Dial Plans : f_manage_dial_plans  Manage Tenants : f_manage_tenants  Manage Entry Points and Queues : f_manage_entrypt_queue  Portal Branding : f_portal_branding  Audit Trail : f_audit_trail  Manage Business Hours : f_manage_business_hours   For module 'm_call_monitoring' we have the following features:  Mid Call Monitoring : f_mid_call_monitor  Barge In : f_barge_in  Restricted Monitor : f_restricted_monitor_only  Whisper Coach : f_whisper_coach  View Blind Monitor Request : f_view_blind_monitor_requests
      - `appFeatureName` (string): The feature name of the Webex Contact Center module.
      - `featureAccessType` (string) (**requerido**): Indicates whether a user of this profile has access to a module feature.  It can be one of these values:  OFF — A contact center user with this profile cannot access this module feature.  ON — A contact center user with this profile can access this module feature. Valores: OFF, ON.
      - `createdTime` (integer/int64): This is the created time of the entity.
      - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
    - `createdTime` (integer/int64): This is the created time of the entity.
    - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
  - `accessAllEntryPoints` (string) (**requerido**): Allow users of this profile access to specific or all the entry points for an organization.  It can take one of these values:  ALL — A contact center user with this profile can access all the entry points for an organization.  SPECIFIC — A contact center user with this profile can access only specific entry points for an organization. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `accessAllSites` (string) (**requerido**): Allow users of this profile access to specific or all the sites for an organization.  It can take one of these values:  ALL — A contact center user with this profile can access all the sites for an organization.  SPECIFIC — A contact center user with this profile can access only specific sites for an organization. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `accessAllQueues` (string) (**requerido**): Allow users of this profile access to specific or all the contact center queues for an organization.  It can take one of these values:  ALL — A contact center user with this profile can access all the contact center queues for an organization.  SPECIFIC — A contact center user with this profile can access only specific contact center queues for an organization. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `accessAllTeams` (string) (**requerido**): Allow users of this profile access to specific or all the contact center teams for an organization.  It can take one of these values:  ALL — A contact center user with this profile can access all the contact center teams for an organization.  SPECIFIC — A contact center user with this profile can access only specific contact center teams for an organization. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `active` (boolean) (**requerido**): Specify whether the User profile is active or not.
  - `editableFolderIds` (array): Indicates the id(s) of the reporting folders a user of this profile has read and write access to.
  - `viewableFolderIds` (array): Indicates the id(s) of the reporting folders a user of this profile has read access to.
  - `nonViewableFolderIds` (array): Indicates the id(s) of the restricted reporting folders for a user of this profile.
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not

### Ejemplo — respuesta 200
```json
{
  "id": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "firstName": "John",
  "lastName": "Wick",
  "email": "johnwick@company.com",
  "workPhone": "1234567890",
  "mobile": "1234567890",
  "ciUserId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "broadCloudUserId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "timezone": "America/New_York",
  "userProfileId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "userProfileType": "PREMIUM_AGENT",
  "contactCenterEnabled": true,
  "siteId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
  "siteName": "bengaluru",
  "teamIds": [
    "f53c8b54-46ca-43f6-ba05-08426a46e23d"
  ],
  "skillProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "agentProfileId": "8e6bb6da-2a78-4768-bef9-7e229f92af22",
  "multimediaProfileId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "deafultDialledNumber": "1234567890",
  "externalIdentifier": "121212",
  "active": true,
  "imiUserCreated": true,
  "systemDefault": false,
  "userLevelBurnoutInclusion": "INCLUDED",
  "userLevelAutoCSATInclusion": "INCLUDED",
  "userLevelWellnessBreakReminders": "DISABLED",
  "userLevelSummariesInclusion": "INCLUDED",
  "createdTime": 1679392200000,
  "lastModifiedTime": 1679392200000
}
```

## Respuestas de error
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "400",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "400",
        "entity": "cc_user",
        "references": []
      }
    ]
  }
}
```
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
- **412**: Resource referred in other entity(s). Please get all the reference entities info by invoking Get incoming-references api.
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "412",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "412",
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