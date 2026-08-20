---
doc_id: webex-contact-center-get-organization-orgid-agent-profile-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/agent-profile/{id}
operation_id: getConfigDesktopProfile
tags: Desktop Profile
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.688176+00:00
---

# GET /organization/{orgid}/agent-profile/{id}

**API:** Webex Contact Center
**Área:** Desktop Profile
**operationId:** `getConfigDesktopProfile`

## Resumen
Get specific Desktop Profile by ID

## Descripción
Retrieve an existing Desktop Profile by ID in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): Resource ID of the Desktop Profile.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/agent-profile/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `name` (string) (**requerido**): Enter a name for the agent profile. Long. max: 80.
- `description` (string): (Optional) Enter a description of the profile. Long. max: 255.
- `parentType` (string) (**requerido**): This can be the following  ORGANIZATION: The agent profile is available to all sites at your enterprise.  SITE: The agent profile is available to a specific site. Valores: ORGANIZATION, SITE.
- `siteId` (string): Identifier for a site which is a physical contact center location under the control of your enterprise.
- `screenPopup` (boolean): Indicates whether to allow external pop-up screens(true) or not(false).
- `lastAgentRouting` (boolean): This setting use only if your administrator enables the Last Agent Routing feature for your enterprise. Indicates whether to allow Last Agent Routing check box on the Agent Desktop during wrap-up(true) or not(false).
- `scheduleAndManageCallBack` (boolean): Indicates whether to allow agents to schedule and manage callbacks(true) or not(false).
- `autoWrapUp` (boolean): Indicates whether to allow auto wrap-up(true) or not(false).
- `agentPersonalGreeting` (boolean): Indicates whether an agent can record a personal greeting(true) or not(false) from the agent desktop.
- `autoAnswer` (boolean): Indicates whether incoming calls on the Agent Desktop need to be answered automatically(true) or not(false).
- `autoWrapAfterSeconds` (integer/int32): This setting allows auto wrap-up after seconds
- `agentAvailableAfterOutdial` (boolean): Enabled if you want the agent to go into the Available state after completing and wrapping up an outdial call. The agent can also manually select an Idle state from the STATUS NOW drop-down list before selecting a wrap-up code.
- `allowAutoWrapUpExtension` (boolean): Indicates whether to allow auto wrap-up extension(true) or not(false).
- `accessWrapUpCode` (string) (**requerido**): Specify the wrap-up codes that the agents can select when they wrap up a contact.It can take one of these values:  ALL — To make all wrap-up codes available.  SPECIFIC — To make specific codes available. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
- `wrapUpCodes` (array): Specify the wrap-up codes list that the agents can select when they wrap up a contact.
- `accessIdleCode` (string) (**requerido**): Specify the Idle codes that the agents can select in Agent Desktop.It can take one of these values:  ALL — To make all idle codes available.  SPECIFIC — To make specific codes available. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
- `idleCodes` (array): Specify the Idle codes list that the agents can select in Agent Desktop.
- `accessQueue` (string) (**requerido**): Specify the queues that the agents can select from the Queue drop-down list on the Agent Desktop.It can take one of these values:  ALL — To make all queues available.  SPECIFIC — To make specific queues available  NONE — If you do not want to make any queues available as transfer targets. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
- `queues` (array): Specify the queues list that the agents can select from the Queue drop-down list on the Agent Desktop.
- `accessEntryPoint` (string) (**requerido**): Specify the entry points that the agents can select from the Entry Point drop-down list on the Agent Desktop.It can take one of these values:  ALL — To make all entry points available.  SPECIFIC — To make specific entry points available  NONE — If you do not want to make any entry points available as transfer targets. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
- `entryPoints` (array): Specify the entry points list that the agents can select from the Entry Point drop-down list on the Agent Desktop.
- `accessBuddyTeam` (string) (**requerido**): Specify the teams that the agents can select from the Agent drop-down list on the Agent Desktop. It can take one of these values:  ALL —  To make the agents on all teams available.  SPECIFIC — To make agents on specific teams available, then select teams from the drop-down list  NONE — If you do not want to make any teams available for consultation, conference, or call transfer. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
- `buddyTeams` (array): Specify the teams list that the agents can select from the Agent drop-down list on the Agent Desktop.
- `consultToQueue` (boolean): Indicates whether you  want the agent to be able to select a queue in the Queue drop-down list as a target for a consultation or not.
- `outdialEnabled` (boolean): Indicates whether you want the agent to be able to make outdial calls(true) or not(false).
- `outdialEntryPointId` (string): If you enabled Outdial, specify the entry point id that the agent can use to make outdial calls.
- `outdialANIId` (string): This setting occurs only if you enabled Outdial. Specify the Outdial ANI id that the agent can use to make outdial calls.
- `addressBookId` (string): Specify the address book id that includes the speed-dial numbers that the agent can select to make outdial and consult calls.
- `dialPlanEnabled` (boolean): Indicates whether you want the agent to be able to make ad-hoc outdial calls(true) or not(false).
- `dialPlans` (array) (DEPRECADO): **Deprecated** as of 2026.06; will be removed after consumers migrate. This setting appears only if Dial Plan is enabled. select the dial plans that determine the inputs that the system accepts in the Start a new call field.
- `timeoutDesktopInactivityCustomEnabled` (boolean): This setting enabled time out desktop inactivity feature.
- `showUserDetailsMS` (boolean): Specify whether the show user details of microsoft account user enabled or not
- `stateSynchronizationMS` (boolean): Specify whether the state synchronization of microsoft account user enabled or not
- `showUserDetailsWebex` (boolean): Specify whether the show user details of webex account user enabled or not
- `stateSynchronizationWebex` (boolean): Specify whether the state synchronization of webex account user enabled or not
- `manageChannelAvailability` (boolean): Indicates whether the agent can manage channel availability(true) or not(false).
- `timeoutDesktopInactivityMins` (integer/int32): This setting occurs only if you enabled time out desktop inactivity feature. Specify time in minute(s).
- `agentDNValidation` (string) (**requerido**): Specifies the validation applied when an agent logs in with a DN.  **Supported values going forward:** `ALL` (Unrestricted — agents may use any DN) and  `PROVISIONED_VALUE` (login DN restricted to the value provisioned for the agent).  **Note:** `SPECIFIC` (Validation Criteria) is no longer supported and must not be used  for new or updated profiles. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
- `agentDNValidationCriteria` (string) (DEPRECADO): **Deprecated** as of 2026.06; will be removed after consumers migrate. This setting occurs only if you select Validation Criteria in the Validation For Agent DN. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
- `agentDNValidationCriterions` (array) (DEPRECADO): **Deprecated** as of 2026.06; will be removed after consumers migrate. This setting specify the list that occurs only if you select Validation Criteria in the Validation For Agent DN.
- `loginVoiceOptions` (array): List of Login Voice Options.
- `viewableStatistics` (object): Viewable Statistics schema.
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `agentStats` (boolean): Indicates whether you want the agents to view their personal statistics in Agent Desktop or not.
  - `accessQueueStats` (string) (**requerido**): This setting controls whether the agent can view statistics for all or some queues in the Agent Personal Statistics tab.It can take one of these values:  ALL —  To enable the agent to display statistics for all queues.  SPECIFIC — Select Queues drop-down list to enable the agent to display statistics for specific queues.  NONE — To prevent the agent from displaying queue statistics. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `contactServiceQueues` (array): This setting should be specified when Access Queue Statistics is SPECIFIC.
  - `loggedInTeamStats` (boolean): Indicates whether the agent can view statistics for the team or not.
  - `accessTeamStats` (string) (**requerido**): This setting controls whether the agent can view statistics for all or some teams in the Agent Personal Statistics tab.It can take one of these values:  ALL —  To enable the agent to display statistics for all teams.  SPECIFIC — Select Teams drop-down list to enable the agent to display statistics for specific teams.  NONE — To prevent the agent from displaying teams statistics. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `teams` (array): This setting should be specified when Access Team Statistics is SPECIFIC.
  - `createdTime` (integer/int64): This is the created time of the entity.
  - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
- `thresholdRules` (array): The Agent Thresholds page appears only if your enterprise uses the Threshold Alerts feature. If your enterprise uses the Agent Threshold Alerts feature, the page also provides settings to specify the thresholds associated with the agent.
- `active` (boolean) (**requerido**): Specify whether the agent profile is active or not Active.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not
- `createdTime` (integer/int64): This is the created time of the entity.

### Ejemplo — respuesta 200
```json
{
  "accessBuddyTeam": "ALL",
  "accessEntryPoint": "ALL",
  "accessIdleCode": "ALL",
  "accessQueue": "ALL",
  "accessWrapUpCode": "ALL",
  "active": true,
  "addressBookId": "3b20a52a-44c9-4c7f-9ccc-61379f1feb6a",
  "agentAvailableAfterOutdial": false,
  "agentDnCheck": true,
  "agentDNValidation": "ALL",
  "agentDNValidationCriteria": "ALL",
  "agentDNValidationCriterions": [],
  "agentPersonalGreeting": true,
  "allowAutoWrapUpExtension": false,
  "autoAnswer": false,
  "autoWrapAfterSeconds": 0,
  "autoWrapUp": false,
  "browserCheck": true,
  "buddyTeams": [],
  "consultToQueue": false,
  "createdTime": 1776695809000,
  "description": "",
  "dialPlanEnabled": false,
  "dialPlans": [
    "US",
    "Any Format"
  ],
  "entryPoints": [
    "apim_entry_516789",
    "apim_entry_6123456"
  ],
  "extensionCheck": true,
  "id": "a270c618-df2f-4ca5-a29b-2e8321f78f94",
  "idleCodes": [
    "aux_code_sale",
    "aux_code2"
  ],
  "lastAgentRouting": false,
  "lastUpdatedTime": 1782305047122,
  "loginVoiceOptions": [
    "AGENT_DN",
    "EXTENSION",
    "BROWSER"
  ],
  "name": "Test New DP",
  "organizationId": "694f5d79-680a-4dd0-bc92-436908174db9",
  "outdialANIId": "3ac3657b-cedd-424b-a584-2f9182b8fe47",
  "outdialEnabled": true,
  "outdialEntryPointId": "5ca51368-9ed8-4f01-bff2-33ffe56fbb08",
  "parentType": "ORGANIZATION",
  "queues": [
    "apim_queue_516789",
    "apim_queue_6123456"
  ],
  "scheduleAndManageCallBack": true,
  "screenPopup": false,
  "showUserDetailsMS": fa
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