---
doc_id: webex-contact-center-get-organization-orgid-v2-contact-service-queue-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/v2/contact-service-queue/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.936781+00:00
---

# GET /organization/{orgid}/v2/contact-service-queue/{id}

**API:** Webex Contact Center
**Área:** Contact Service Queue
**operationId:** `getConfigContactServiceQueue_1`

## Resumen
Get specific Contact Service Queue by ID

## Descripción
Retrieve an existing Contact Service Queue by ID in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the Contact Service Queue.
- `agentsUpdatedInfo` [query] (boolean): If `true`, returns the user details who has last updated the agents list in an agent based queue.

## Respuestas
- **200**: OK
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
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
