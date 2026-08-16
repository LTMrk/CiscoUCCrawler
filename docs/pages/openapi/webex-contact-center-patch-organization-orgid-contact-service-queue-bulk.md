---
doc_id: webex-contact-center-patch-organization-orgid-contact-service-queue-bulk
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: PATCH
path: /organization/{orgid}/contact-service-queue/bulk
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.934332+00:00
---

# PATCH /organization/{orgid}/contact-service-queue/bulk

**API:** Webex Contact Center
**Área:** Contact Service Queue
**operationId:** `patchAllConfigContactServiceQueue`

## Resumen
Bulk partial update Contact Service Queues

## Descripción
Update some or all properties for multiple Contact Service Queues in bulk in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `items` (array): List of items in the bulk request.
  - `itemIdentifier` (integer): Unique item identifier for a bulk operation.
  - `item` (object): Contact Service Queue schema.
    - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string) **(requerido)**: Name of the Contact Service Queue
    - `description` (string): (Optional) A short description of the queue.
    - `queueType` (string) **(requerido)**: This can be the following  INBOUND  OUTBOUND Valores: INBOUND, OUTBOUND.
    - `checkAgentAvailability` (boolean) **(requerido)**: This setting specifies whether the system can exclude teams with no logged in agents for the relevant routing strategies. It does not support Social Channel Type.
    - `channelType` (string) **(requerido)**: Setting to indicate the channel type. Use uppercase. Supported channel types are:    TELEPHONY, EMAIL, SOCIAL_CHANNEL, and CHAT.   For TELEPHONY channelType, the following fields are mandatory - recordingPermitted, ivrRequeueUrl, recordingAllCallsPermitted, monitoringPermitted, parkingPermitted, pauseRecordingPermitted, controlFlowScriptUrl, defaultMusicInQueueMediaFileId. Valores: TELEPHONY, EMAIL, FAX, CHAT, VIDEO, OTHERS, SOCIAL_CHANNEL, WORK_ITEM, CUSTOM_MESSAGING.
    - `socialChannelType` (string): This can be the following  MESSAGEBIRD  MESSENGER Valores: MESSAGEBIRD, MESSENGER, WHATSAPP, APPLE_BUSINESS_CHAT, GOOGLE_BUSINESS_MESSAGES.
    - `serviceLevelThreshold` (integer) **(requerido)**: The time in seconds that a customer request can be in a queue before the system flags it as outside the service level. It does not support Social Channel Type.
    - `maxActiveContacts` (integer) **(requerido)**: The maximum number of simultaneous contacts allowed for this queue. It does not support Social Channel Type.
    - `maxTimeInQueue` (integer) **(requerido)**: The time in seconds after which the system distributes the queued customer request to the overflow number that you provision for this queue.
    - `defaultMusicInQueueMediaFileId` (string): Identifies the default audio file which will be played for calls when they arrive or are waiting in queue.  This setting is available only for the Telephony channel type.
    - `timezone` (string): (Optional) Any routing strategy for this queue uses the time zone that you select here.
    - `active` (boolean) **(requerido)**: Specify whether the queue is active or not active
    - `outdialCampaignEnabled` (boolean): Should be specified only for outdial queues; if enabled, then Call Distribution and Queue Routing Type can be specified.
    - `monitoringPermitted` (boolean): Indicates whether or not monitoring is permitted.  This setting is available only for the Telephony channel type.
    - `parkingPermitted` (boolean): Indicates whether or not parking is permitted.  This setting is available only for the Telephony channel type.
    - `recordingPermitted` (boolean): Indicates whether or not recording is permitted.  This setting is available only for the Telephony channel type.
    - `recordingAllCallsPermitted` (boolean): Indicates whether or not recording all calls is permitted.  This setting is available only for the Telephony channel type.
    - `pauseRecordingPermitted` (boolean): Indicates whether or not pausing the recording is permitted.  This setting is available only for the Telephony channel type.
    - `recordingPauseDuration` (integer): The duration in seconds of pause in recording.  This setting is available only for the Telephony channel type.
    - `controlFlowScriptUrl` (string): The URL for the queue or the default control script of the queue. If you do not use the routing strategy module to configure the control script, the system automatically populates the URL. This setting is available only for the Telephony channel type.
    - `ivrRequeueUrl` (string): This setting is available only for the Telephony channel type.
    - `overflowNumber` (string): The destination phone number to which the system distributes the customer calls when they exceed the Maximum Time in Queue that you have set in the routing strategy. This setting is applicable only for the Telephony channel type and it is optional.
    - `vendorId` (string): The unique alphanumeric string that maps this queue to the vendor. This setting is available only for the Telephony channel type and it is optional.
    - `routingType` (string) **(requerido)**: This can be one of the following  LONGEST_AVAILABLE_AGENT  SKILLS_BASED(skillBasedRoutingType is mandatory to define) Valores: LONGEST_AVAILABLE_AGENT, SKILLS_BASED, CIRCULAR, LINEAR.
    - `skillBasedRoutingType` (string): This can be the following  LONGEST_AVAILABLE_AGENT  BEST_AVAILABLE_AGENT Valores: LONGEST_AVAILABLE_AGENT, BEST_AVAILABLE_AGENT.
    - `queueRoutingType` (string) **(requerido)**: This can be the following  TEAM_BASED  QUEUE_BASED Valores: TEAM_BASED, SKILL_BASED, AGENT_BASED.
    - `queueSkillRequirements` (array): List of Queue Skill Requirements.
      - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
      - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
      - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
      - `skillId` (string) **(requerido)**: Skill ID reference
      - `skillName` (string): Indicates the name of the skill. Once created, name cannot be modified.
      - `skillType` (string): This can be of the following types  PROFICIENCY: id = 0  BOOLEAN: id = 1  TEXT: id = 2  ENUM: id = 3  Once created, skillType cannot be modified.
      - `condition` (string) **(requerido)**: Indicates a value that represents a skill the agent has.
      - `skillValue` (string) **(requerido)**: A short textual description that represents a skill the agent has.
      - `weight` (integer): Weight for proficiency skill requirement
      - `dynamicSkill` (boolean): Indicates whether the skill is a dynamic skill or not. Default value is false.
      - `createdTime` (integer): This is the created time of the entity.
      - `lastUpdatedTime` (integer): This is the updated time of the entity.
    - `agents` (array): The list of agents for AgentBased queue
      - `id` (string) **(requerido)**: Id of an agent in WxCC
      - `ciUserId` (string): Id of an agent in Common Identity
    - `callDistributionGroups` (array) **(requerido)**: List of Call Distribution Groups.
      - `agentGroups` (array): List of Agent Groups.
        - `teamId` (string): ID of a team
      - `order` (integer): The order of this call distribution group.
      - `duration` (integer): (Optional)The duration in seconds after which a contact in queue will be distributed to this group.
    - `xspVersion` (string): (Optional) Used to subscribe for recording events.
    - `subscriptionId` (string): (Optional) Used to subscribe for recording events.
    - `assistantSkill` (object): Assistant skill related properties associated with the queue. This is applicable/available only when AI Assistant add-on offer/license is added to the organization.
      - `assistantSkillId` (string): Id of an Assistant Skill mapped to the Contact Service Queue. If the value is missing in response, the consumer should assume a value as null.
      - `assistantSkillUpdatedTime` (integer): Time(in epoch milliseconds) when assistant skill mapping was last updated.  If the value is missing in response, the consumer should assume a value as null.
    - `systemDefault` (boolean): Indicates whether the created resource is system created or not
    - `manuallyAssignable` (boolean): If `true`, the queue can be manually assigned.
    - `agentsLastUpdatedByUserName` (string): The name of the user who last modified the agents list.
    - `agentsLastUpdatedByUserEmailPrefix` (string): The email of the user who last modified the agents list.
    - `agentsLastUpdatedTime` (integer): The date when the agents list was last modified (epoch timestamp in milliseconds).
    - `queueLevelSummariesInclusion` (string): Queue level summaries inclusion type. Used only when Queue inclusion for summaries is set to 'Specific Queues' at the org level AI Assistant->Summaries configuration. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained.This is applicable/available only when AI Assistant add-on offer/license is added to the organization. If the value is missing in response, the consumer should assume a value as EXCLUDED.
    - `queueLevelSentimentAnalysisInclusion` (string): Queue level sentiment analysis inclusion type. Used only when Queue inclusion for sentiment analysis is set to 'Specific Queues' at the org level AI Assistant->Quality Management configuration. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained.This is applicable/available when either AI Assistant/AI Quality Management add-on offer/license is added to the organization. If the value is missing in response, the consumer should assume a value as EXCLUDED.
    - `queueLevelPredictedWaitTimeInclusion` (string): Queue level predicted wait time inclusion type. Used only when Queue inclusion for predicted wait time is set to 'Specific Queues' at the org level AI Assistant->Predicted Wait Time configuration. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained. If the value is missing in response, the consumer should assume a value as EXCLUDED.
    - `queueLevelAutoCsatInclusion` (string): Queue level auto CSAT inclusion type. Used only when Queue inclusion for auto CSAT is set to 'Specific Queues' at the org level AI Assistant->Auto CSAT configuration. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained.This is applicable/available when either AI Assistant/AI Quality Management add-on offer/license is added to the organization. If the value is missing in response, the consumer should assume a value as EXCLUDED.
    - `queueLevelRealTimeTranscriptionsInclusion` (string): Queue level real time transcriptions inclusion type. Used only when Queue inclusion for real time transcriptions is set to 'Specific Queues' at the org level AI Assistant->Real Time Transcriptions configuration. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained.This is applicable/available when either AI Assistant/AI Quality Management add-on offer/license is added to the organization. If the value is missing in response, the consumer should assume a value as EXCLUDED.
    - `personalizedAIRouting` (object): Queue-level Personalized AI Routing configuration. Enables intelligent agent routing based on AI/ML predictions.
      - `aiRoutingMode` (string): AI Routing mode. Valid transitions: NONE → EVALUATION; EVALUATION → ACTIVE or NONE; ACTIVE → NONE. NONE: AI routing disabled (default). EVALUATION: Shadow mode - AI predictions are generated but not used for routing (for testing/validation). ACTIVE: AI routing enabled - contacts are routed based on AI predictions. Valores: NONE, EVALUATION, ACTIVE.
      - `aiRoutingKPIId` (string): AI Routing KPI ID - the performance metric used by AI to optimize routing decisions. This should reference a valid KPI configured in the AI routing system. Required when aiRoutingMode is EVALUATION or ACTIVE.
      - `evaluationModeStartTime` (integer): Timestamp (epoch milliseconds) when EVALUATION mode was activated. Automatically set by the system when transitioning from NONE to EVALUATION. Used to track evaluation duration and readiness for ACTIVE mode transition.
    - `pauseAndResume` (object): Pause and resume configuration for EMAIL and SOCIAL channels only
      - `enabled` (boolean): Indicates whether pause and resume is enabled for this queue
      - `pauseTimeout` (object): Pause timeout configuration. Required when enabled is true.
        - `days` (integer): Number of days for pause timeout. Channel-specific maximum is enforced at the service layer based on configured limits.
        - `hours` (integer): Number of hours for pause timeout (0-23)
        - `minutes` (integer): Number of minutes for pause timeout (0-59)
    - `createdTime` (integer): This is the created time of the entity.
    - `lastUpdatedTime` (integer): This is the updated time of the entity.
  - `requestAction` (string): Identifier for action type. Possible values are `SAVE` and `DELETE`.

### Ejemplo de petición
```json
{
  "items": [
    {
      "item": {
        "id": "26e2df70-0f77-41b8-8e8f-1d76e92c9638",
        "assistantSkill": {
          "assistantSkillId": "26e2df70-0f77-41b8-8e8f-1d76e92c9639"
        }
      },
      "itemIdentifier": 0,
      "requestAction": "SAVE"
    }
  ]
}
```

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
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
