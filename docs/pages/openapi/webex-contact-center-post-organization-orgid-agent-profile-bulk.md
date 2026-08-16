---
doc_id: webex-contact-center-post-organization-orgid-agent-profile-bulk
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: POST
path: /organization/{orgid}/agent-profile/bulk
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.938871+00:00
---

# POST /organization/{orgid}/agent-profile/bulk

**API:** Webex Contact Center
**Área:** Desktop Profile
**operationId:** `saveAllConfigDesktopProfile`

## Resumen
Bulk save Desktop Profiles

## Descripción
Create, Update or delete Desktop Profiles in bulk in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `items` (array): List of items in the bulk request.
  - `itemIdentifier` (integer): Unique item identifier for a bulk operation.
  - `item` (object): Agent Profile schema.
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string) **(requerido)**: Enter a name for the agent profile.
    - `description` (string): (Optional) Enter a description of the profile.
    - `parentType` (string) **(requerido)**: This can be the following  ORGANIZATION: The agent profile is available to all sites at your enterprise.  SITE: The agent profile is available to a specific site. Valores: ORGANIZATION, SITE.
    - `siteId` (string): Identifier for a site which is a physical contact center location under the control of your enterprise.
    - `screenPopup` (boolean): Indicates whether to allow external pop-up screens(true) or not(false).
    - `lastAgentRouting` (boolean): This setting use only if your administrator enables the Last Agent Routing feature for your enterprise. Indicates whether to allow Last Agent Routing check box on the Agent Desktop during wrap-up(true) or not(false).
    - `scheduleAndManageCallBack` (boolean): Indicates whether to allow agents to schedule and manage callbacks(true) or not(false).
    - `autoWrapUp` (boolean): Indicates whether to allow auto wrap-up(true) or not(false).
    - `autoAnswer` (boolean): Indicates whether incoming calls on the Agent Desktop need to be answered automatically(true) or not(false).
    - `agentPersonalGreeting` (boolean): Indicates whether an agent can record a personal greeting(true) or not(false) from the agent desktop.
    - `autoWrapAfterSeconds` (integer): This setting allows auto wrap-up after seconds
    - `agentAvailableAfterOutdial` (boolean): Enabled if you want the agent to go into the Available state after completing and wrapping up an outdial call. The agent can also manually select an Idle state from the STATUS NOW drop-down list before selecting a wrap-up code.
    - `allowAutoWrapUpExtension` (boolean): Indicates whether to allow auto wrap-up extension(true) or not(false).
    - `accessWrapUpCode` (string) **(requerido)**: Specify the wrap-up codes that the agents can select when they wrap up a contact.It can take one of these values:  ALL — To make all wrap-up codes available.  SPECIFIC — To make specific codes available. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
    - `wrapUpCodes` (array): Specify the wrap-up codes list that the agents can select when they wrap up a contact.
    - `accessIdleCode` (string) **(requerido)**: Specify the Idle codes that the agents can select in Agent Desktop.It can take one of these values:  ALL — To make all idle codes available.  SPECIFIC — To make specific codes available. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
    - `idleCodes` (array): Specify the Idle codes list that the agents can select in Agent Desktop.
    - `accessQueue` (string) **(requerido)**: Specify the queues that the agents can select from the Queue drop-down list on the Agent Desktop.It can take one of these values:  ALL — To make all queues available.  SPECIFIC — To make specific queues available  NONE — If you do not want to make any queues available as transfer targets. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
    - `queues` (array): Specify the queues list that the agents can select from the Queue drop-down list on the Agent Desktop.
    - `accessEntryPoint` (string) **(requerido)**: Specify the entry points that the agents can select from the Entry Point drop-down list on the Agent Desktop.It can take one of these values:  ALL — To make all entry points available.  SPECIFIC — To make specific entry points available  NONE — If you do not want to make any entry points available as transfer targets. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
    - `entryPoints` (array): Specify the entry points list that the agents can select from the Entry Point drop-down list on the Agent Desktop.
    - `accessBuddyTeam` (string) **(requerido)**: Specify the teams that the agents can select from the Agent drop-down list on the Agent Desktop. It can take one of these values:  ALL —  To make the agents on all teams available.  SPECIFIC — To make agents on specific teams available, then select teams from the drop-down list  NONE — If you do not want to make any teams available for consultation, conference, or call transfer. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
    - `buddyTeams` (array): Specify the teams list that the agents can select from the Agent drop-down list on the Agent Desktop.
    - `consultToQueue` (boolean): Indicates whether you  want the agent to be able to select a queue in the Queue drop-down list as a target for a consultation or not.
    - `outdialEnabled` (boolean): Indicates whether you want the agent to be able to make outdial calls(true) or not(false).
    - `outdialEntryPointId` (string): If you enabled Outdial, specify the entry point id that the agent can use to make outdial calls.
    - `outdialANIId` (string): This setting occurs only if you enabled Outdial. Specify the Outdial ANI id that the agent can use to make outdial calls.
    - `addressBookId` (string): Specify the address book id that includes the speed-dial numbers that the agent can select to make outdial and consult calls.
    - `dialPlanEnabled` (boolean): Indicates whether you want the agent to be able to make ad-hoc outdial calls(true) or not(false).
    - `dialPlans` (array): **Deprecated** as of 2026.06; will be removed after consumers migrate. This setting appears only if Dial Plan is enabled. select the dial plans that determine the inputs that the system accepts in the Start a new call field.
    - `agentDNValidation` (string) **(requerido)**: Specifies the validation applied when an agent logs in with a DN.  **Supported values going forward:** `ALL` (Unrestricted — agents may use any DN) and  `PROVISIONED_VALUE` (login DN restricted to the value provisioned for the agent).  **Note:** `SPECIFIC` (Validation Criteria) is no longer supported and must not be used  for new or updated profiles. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
    - `agentDNValidationCriteria` (string): **Deprecated** as of 2026.06; will be removed after consumers migrate. This setting occurs only if you select Validation Criteria in the Validation For Agent DN. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
    - `agentDNValidationCriterions` (array): **Deprecated** as of 2026.06; will be removed after consumers migrate. This setting specify the list that occurs only if you select Validation Criteria in the Validation For Agent DN.
    - `loginVoiceOptions` (array): Login voice options.
    - `viewableStatistics` (object) **(requerido)**: Specifies the Statistics that agent of this profile can view.
      - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
      - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
      - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
      - `agentStats` (boolean): Indicates whether you want the agents to view their personal statistics in Agent Desktop or not.
      - `accessQueueStats` (string) **(requerido)**: This setting controls whether the agent can view statistics for all or some queues in the Agent Personal Statistics tab.It can take one of these values:  ALL —  To enable the agent to display statistics for all queues.  SPECIFIC — Select Queues drop-down list to enable the agent to display statistics for specific queues.  NONE — To prevent the agent from displaying queue statistics. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
      - `contactServiceQueues` (array): This setting should be specified when Access Queue Statistics is SPECIFIC.
      - `loggedInTeamStats` (boolean): Indicates whether the agent can view statistics for the team or not.
      - `accessTeamStats` (string) **(requerido)**: This setting controls whether the agent can view statistics for all or some teams in the Agent Personal Statistics tab.It can take one of these values:  ALL —  To enable the agent to display statistics for all teams.  SPECIFIC — Select Teams drop-down list to enable the agent to display statistics for specific teams.  NONE — To prevent the agent from displaying teams statistics. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
      - `teams` (array): This setting should be specified when Access Team Statistics is SPECIFIC.
      - `createdTime` (integer): This is the created time of the entity.
      - `lastUpdatedTime` (integer): This is the updated time of the entity.
    - `thresholdRules` (array): The Agent Thresholds page appears only if your enterprise uses the Threshold Alerts feature. If your enterprise uses the Agent Threshold Alerts feature, the page also provides settings to specify the thresholds associated with the agent.
    - `active` (boolean) **(requerido)**: Specify whether the agent profile is active or not Active.
    - `timeoutDesktopInactivityCustomEnabled` (boolean): This setting enabled time out desktop inactivity feature.
    - `showUserDetailsMS` (boolean): Specify whether the show user details of microsoft account user enabled or not
    - `stateSynchronizationMS` (boolean): Specify whether the state synchronization of microsoft account user enabled or not
    - `showUserDetailsWebex` (boolean): Specify whether the show user details of webex account user enabled or not
    - `stateSynchronizationWebex` (boolean): Specify whether the state synchronization of webex account user enabled or not
    - `manageChannelAvailability` (boolean): Indicates whether the agent can manage channel availability(true) or not(false).
    - `timeoutDesktopInactivityMins` (integer): This setting occurs only if you enabled time out desktop inactivity feature. Specify time in minute(s).
    - `systemDefault` (boolean): Indicates whether the created resource is system created or not
    - `createdTime` (integer): This is the created time of the entity.
    - `lastUpdatedTime` (integer): This is the updated time of the entity.
    - `autoAcceptDigitalInteractions` (boolean): Automatically accept digital interactions when agent becomes available
  - `requestAction` (string): Identifier for action type. Possible values are `SAVE` and `DELETE`.

## Respuestas
- **207**: Multi-Status
  - `items` (array):
    - `itemIdentifier` (integer): Unique item identifier for a bulk operation.
    - `status` (integer): Indicates the error status code.
    - `operationType` (string): The kind of operation desired of an entity. Valores: CREATE, UPDATE, DELETE, GET.
    - `href` (string): The resource URI of an entity.
    - `apiError` (object): Response body for an API error.
      - `trackingId` (string): An opaque identifier for mapping protocol failures to service internal codes.   When specified in a request, it can be used for co-relating events across services
      - `error` (object): Details of an error.
        - `key` (string): An application defined error code.
        - `message` (array): A message providing details about the error.
          - `description` (string): A human readable explanation for the occurrence of an error.
- **400**: The request was invalid and cannot be served. An accompanying error message will explain further
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **409**: Similar entity is already present
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
