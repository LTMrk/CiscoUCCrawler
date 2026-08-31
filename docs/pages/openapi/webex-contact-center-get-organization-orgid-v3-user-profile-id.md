---
doc_id: webex-contact-center-get-organization-orgid-v3-user-profile-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/v3/user-profile/{id}
operation_id: getConfigUserProfileGranularAccess
tags: User Profiles
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.119929+00:00
---

# GET /organization/{orgid}/v3/user-profile/{id}

**API:** Webex Contact Center
**Área:** User Profiles
**operationId:** `getConfigUserProfileGranularAccess`

## Resumen
Get specific User Profile by ID

## Descripción
Retrieve an existing user profile by ID in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): Resource ID of the User Profile.
- `includeNames` [query] (boolean): Flag to include resource names in the response.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/v3/user-profile/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): The name of the user profile. Long. max: 80.
- `description` (string): An optional description of the profile. Long. max: 255.
- `profileType` (string) (**requerido**): The type determines the privileges applicable for a profile.  It can take one of these values:  STANDARD_AGENT — Has access to Agent Desktop[m_agent_desktop] module.  PREMIUM_AGENT — Has access to Agent Desktop[m_agent_desktop] and Multimedia[m_multimedia] module.  SUPERVISOR — Has access to all modules except to manage tenants in the Provisioning[m_provisioning] module.  ADMINISTRATOR — Has access to all modules.  ADMINISTRATOR_ONLY — Has access to Provisioning[m_provisioning], Real Time Reports[m_real_time_reports], Call Recording[m_call_recording], IMI Digital Channels[m_imi_digital_channels], and Routing Strategy[m_routing_strategy] modules.  It is required only during a create operation.   The profile type cannot be changed for an existing user profile. Valores: ADMINISTRATOR, ADMINISTRATOR_ONLY, SUPERVISOR, PREMIUM_AGENT, STANDARD_AGENT, ANALYZER_ADMINISTRATOR, ANALYZER_SUPERVISOR, ANALYZER_USER.
- `active` (boolean) (**requerido**): Specify whether the User profile is active or not.
- `permissionAccessLevel` (string) (**requerido**): This can be used to allow users of this profile access to specific or all the Webex Contact Center permissions.  It can take one of these values:  ALL — A contact center user with this profile can access all Contact Center permissions.  SPECIFIC — A contact center user with this profile can access only specific permissions. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
- `resourceAccessLevel` (string) (**requerido**): This can be used to allow users of this profile access to specific or all the Webex Contact Center resources.  It can take one of these values:  ALL — A contact center user with this profile can access all Contact Center resources.  SPECIFIC — A contact center user with this profile can access only specific resources. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
- `permissions` (array): Specifies the permissions(s) a user of this profile has access to.  It should be chosen when permission access is SPECIFIC.  Please specify all the following permissions and their respective access type.
  - `id` (string): The id of the user profile permission.
  - `name` (string) (**requerido**): The name of the user profile permission.audio-prompt — Has access to Audio Prompt[audio_prompt] permission.  agent-personalized-greeting — Has access to Agent Personalized Greeting[agent_personalized_greeting] permission.  holiday-list — Has access to Holiday List[holiday_list] permission.  override — Has access to Override[override] permission.  working-hour — Has access to Working Hour[working_hour] permission.  call-recording-schedule — Has access to Call Recording Schedule[call_recording_schedule] permission.  channel — Has access to Channel[channel] permission.  entry-point — Has access to Entry Point[entry_point] permission.  custom-channel — Has access to Custom Channel[custom_channel] permission.  support-number — Has access to Support Number[support_number] permission.  flow-settings-override — Has access to Flow Settings Override[flow_settings_override] permission.  queue — Has access to Queue[queue] permission.  flow — Has access to Flow[flow] permission.  function — Has access to Function[function] permission.  global-variable — Has access to Global Variable[global_variable] permission.  asset — Has access to Asset[asset] permission.  web-chat-asset — Has access to Web Chat Asset[web_chat_asset] permission.  resource-collection — Has access to Resource Collection[resource_collection] permission.  user-profile — Has access to User Profile[user_profile] permission.  user — Has access to User[user] permission.  site — Has access to Site[site] permission.  skill-profile — Has access to Skill Profile[skill_profile] permission.  skill-definition — Has access to Skill Definition[skill_definition] permission.  team — Has access to Team[team] permission.  address-book — Has access to Address Book[address_book] permission.  agent-wellbeing — Has access to Agent Wellbeing[agent_wellbeing] permission.This is applicable/available only when AI Assistant add-on offer/license is added to the organization.  auto-csat — Has access to Auto CSAT[auto_csat] permission.This is applicable/available when either AI Assistant/AI Quality Management add-on offer/license is added to the organization.  generated-summary — Has access to Generated Summary[generated_summary] permission.This is applicable/available only when AI Assistant add-on offer/license is added to the organization.  real-time-transcription — Has access to Real Time Transcription[real_time_transcription] permission.This is applicable/available when either AI Assistant/AI Quality Management add-on offer/license is added to the organization.  suggested-response — Has access to Suggested Response[suggested_response] permission.This is applicable/available only when AI Assistant add-on offer/license is added to the organization.  desktop-layout — Has access to Desktop Layout[desktop_layout] permission.  desktop-profile — Has access to Desktop Profile[desktop_profile] permission.  dial-plan — Has access to Dial Plan[dial_plan] permission.  multimedia-profile — Has access to Multimedia Profile[multimedia_profile] permission.  idle-wrapup-code — Has access to Idle Wrap-Up Code[idle_wrapup_code] permission.  outdial-ani — Has access to Outdial ANI[outdial_ani] permission.  quick-reply — Has access to Quick Reply[quick_reply] permission.  api-key — Has access to API Key[api_key] permission.  audit-trail — Has access to Audit Trail[audit_trail] permission.  business-rules-engine — Has access to Business Rules Engine[business_rules_engine] permission.  campaign-manager — Has access to Campaign Manager[campaign_manager] permission.  routing-strategy — Has access to Routing Strategy[routing_strategy] permission.  tenant-setting — Has access to Tenant Setting[tenant_setting] permission.  audio-recording-transcript — Has access to Audio Recording Transcript[audio_recording_transcript] permission.  tag — Has access to Tag[tag] permission.  additional-supervisory — Has access to Additional Supervisory[additional_supervisory] permission.  change-agent-state — Has access to Change Agent State[change_agent_state] permission.  manage-agent-queues-assignment — Has access to Manage Agent Queues Assignment[manage_agent_queues_assignment] permission.  reskill-agent — Has access to Reskill Agent[reskill_agent] permission.  send-message — Has access to Send Message[send_message] permission.  sign-out-agent — Has access to Sign Out Agent[sign_out_agent] permission.  analyzer — Has access to Analyzer[analyzer] permission.  call-monitoring — Has access to Call Monitoring[call_monitoring] permission.  barge-in — Has access to Barge-In[barge_in] permission.  whisper-coach — Has access to Whisper Coach[whisper_coach] permission.  restricted-monitor-only — Has access to Restricted Monitor Only[restricted_monitor_only] permission.  view-blind-monitor-request — Has access to View Blind Monitor Request[view_blind_monitor_request] permission.  mid-call-monitor — Has access to Mid-Call Monitor[mid_call_monitor] permission.  threshold-rule — Has access to Threshold Rule[threshold_rule] permission.  multimedia — Has access to Multimedia[multimedia] permission.  basic-digital — Has access to Basic Digital[basic_digital] permission.  social-channel — Has access to Social Channel[social_channel] permission.  coaching-insights — Has access to Coaching Insights[coaching-insights] permission.This is applicable/available only when AI Quality Management add-on offer/license is added to the organization.  sentiment-analysis — Has access to Sentiment Analysis[sentiment-analysis] permission.This is applicable/available when either AI Assistant/AI Quality Management add-on offer/license is added to the organization.  evaluations-analytics — Has access to Evaluations Analytics[evaluations-analytics] permission.This is applicable/available only when AI Quality Management add-on offer/license is added to the organization.  coaching-insights-assignment — Has access to Coaching Insights Assignment[coaching-insights-assignment] permission.This is applicable/available only when AI Quality Management add-on offer/license is added to the organization.  evaluation-forms-assignment — Has access to Evaluation Forms Assignment[evaluation-forms-assignment] permission.This is applicable/available only when AI Quality Management add-on offer/license is added to the organization.  evaluation-forms-manage — Has access to Evaluation Forms Manage[evaluation-forms-manage] permission.This is applicable/available only when AI Quality Management add-on offer/license is added to the organization.  evaluation-forms-calibrate-questions — Has access to Evaluation Forms Calibrate Questions[evaluation-forms-calibrate-questions] permission.This is applicable/available only when AI Quality Management add-on offer/license is added to the organization.  predicted-wait-time — Has access to Predicted Wait Time[predicted-wait-time] permission.  personalized-ai-routing — Has access to Personalized AI Routing[personalized-ai-routing] permission.  play — Has access to Play[play] permission.  download — Has access to Download[download] permission.  delete-recording-transcript — Has access to Delete[delete-recording-transcript] permission.  schedule-listening — Has access to Schedule Listening[schedule-listening] permission. This permission is available only for Supervisor profiles and controls access to manage Schedule Listening feature in ESD.
  - `access` (string): Indicates the access rights for a user of this profile for a Webex Contact Center module.  It can take be one of these values:  VIEW — A contact center user with this profile has read only access to a Contact Center module.  EDIT — A contact center user with this profile has read and write access to a Contact Center module.  NONE — A contact center user with this profile cannot access the module. Valores: EDIT, VIEW, NONE, ENABLED, DISABLED.
- `editableFolderIds` (array): Indicates the id(s) of the reporting folders a user of this profile has read and write access to.
- `viewableFolderIds` (array): Indicates the id(s) of the reporting folders a user of this profile has read access to.
- `nonViewableFolderIds` (array): Indicates the id(s) of the restricted reporting folders for a user of this profile.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `defaultResourceCollectionId` (string): Specifies the default resource collection for this profile
- `resourceCollections` (array): Specifies the resource collection(s) a user of this profile has access to.  resource collection(s) needs to be specified when resourceAccessLevel is SPECIFIC
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
- `createdTime` (integer/int64): This is the created time of the entity.
- `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

### Ejemplo — respuesta 200
```json
{
  "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "id": "93912f11-6017-404b-bf14-5331890b1797",
  "version": 1,
  "name": "Contact Center Admin Profile",
  "description": "This profile should be applied only to contact center admins.",
  "profileType": "PREMIUM_AGENT",
  "active": true,
  "permissionAccessLevel": "ALL",
  "resourceAccessLevel": "ALL",
  "permissions": [
    {
      "id": "00734874-4732-43bb-bfff-d1e75d309eb1",
      "name": "sites",
      "access": "NONE"
    }
  ],
  "editableFolderIds": [
    1,
    2
  ],
  "viewableFolderIds": [
    1,
    2
  ],
  "nonViewableFolderIds": [
    1,
    2
  ],
  "systemDefault": false,
  "defaultResourceCollectionId": "80f49a6e-11d7-4651-b730-99ed2f726f61",
  "resourceCollections": [
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
  ],
  "createdTime": 0,
  "lastUpdatedTime": 0
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