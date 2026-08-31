---
doc_id: webex-contact-center-post-organization-orgid-contact-service-queue-bulk
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: POST
path: /organization/{orgid}/contact-service-queue/bulk
operation_id: saveAllConfigContactServiceQueue
tags: Contact Service Queue
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T18:15:55.073261+00:00
---

# POST /organization/{orgid}/contact-service-queue/bulk

**API:** Webex Contact Center
**Área:** Contact Service Queue
**operationId:** `saveAllConfigContactServiceQueue`

## Resumen
Bulk save Contact Service Queues

## Descripción
Create, Update or delete Contact Service Queues in bulk in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `items` (array): List of items in the bulk request.
  - `itemIdentifier` (integer/int32): Unique item identifier for a bulk operation.
  - `item` (object): Contact Service Queue schema.
    - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `name` (string) (**requerido**): Name of the Contact Service Queue
    - `description` (string): (Optional) A short description of the queue.
    - `queueType` (string) (**requerido**): This can be the following  INBOUND  OUTBOUND Valores: INBOUND, OUTBOUND.
    - `checkAgentAvailability` (boolean) (**requerido**): This setting specifies whether the system can exclude teams with no logged in agents for the relevant routing strategies. It does not support Social Channel Type.
    - `channelType` (string) (**requerido**): Setting to indicate the channel type. Use uppercase. Supported channel types are:    TELEPHONY, EMAIL, SOCIAL_CHANNEL, and CHAT.   For TELEPHONY channelType, the following fields are mandatory - recordingPermitted, ivrRequeueUrl, recordingAllCallsPermitted, monitoringPermitted, parkingPermitted, pauseRecordingPermitted, controlFlowScriptUrl, defaultMusicInQueueMediaFileId. Valores: TELEPHONY, EMAIL, FAX, CHAT, VIDEO, OTHERS, SOCIAL_CHANNEL, WORK_ITEM, CUSTOM_MESSAGING.
    - `socialChannelType` (string): This can be the following  MESSAGEBIRD  MESSENGER Valores: MESSAGEBIRD, MESSENGER, WHATSAPP, APPLE_BUSINESS_CHAT, GOOGLE_BUSINESS_MESSAGES.
    - `serviceLevelThreshold` (integer/int32) (**requerido**): The time in seconds that a customer request can be in a queue before the system flags it as outside the service level. It does not support Social Channel Type.
    - `maxActiveContacts` (integer/int32) (**requerido**): The maximum number of simultaneous contacts allowed for this queue. It does not support Social Channel Type.
    - `maxTimeInQueue` (integer/int32) (**requerido**): The time in seconds after which the system distributes the queued customer request to the overflow number that you provision for this queue.
    - `defaultMusicInQueueMediaFileId` (string): Identifies the default audio file which will be played for calls when they arrive or are waiting in queue.  This setting is available only for the Telephony channel type.
    - `timezone` (string): (Optional) Any routing strategy for this queue uses the time zone that you select here.
    - `active` (boolean) (**requerido**): Specify whether the queue is active or not active
    - `outdialCampaignEnabled` (boolean): Should be specified only for outdial queues; if enabled, then Call Distribution and Queue Routing Type can be specified.
    - `monitoringPermitted` (boolean): Indicates whether or not monitoring is permitted.  This setting is available only for the Telephony channel type.
    - `parkingPermitted` (boolean): Indicates whether or not parking is permitted.  This setting is available only for the Telephony channel type.
    - `recordingPermitted` (boolean): Indicates whether or not recording is permitted.  This setting is available only for the Telephony channel type.
    - `recordingAllCallsPermitted` (boolean): Indicates whether or not recording all calls is permitted.  This setting is available only for the Telephony channel type.
    - `pauseRecordingPermitted` (boolean): Indicates whether or not pausing the recording is permitted.  This setting is available only for the Telephony channel type.
    - `recordingPauseDuration` (integer/int32): The duration in seconds of pause in recording.  This setting is available only for the Telephony channel type.
    - `controlFlowScriptUrl` (string): The URL for the queue or the default control script of the queue. If you do not use the routing strategy module to configure the control script, the system automatically populates the URL. This setting is available only for the Telephony channel type.
    - `ivrRequeueUrl` (string): This setting is available only for the Telephony channel type.
    - `overflowNumber` (string): The destination phone number to which the system distributes the customer calls when they exceed the Maximum Time in Queue that you have set in the routing strategy. This setting is applicable only for the Telephony channel type and it is optional.
    - `vendorId` (string): The unique alphanumeric string that maps this queue to the vendor. This setting is available only for the Telephony channel type and it is optional.
    - `routingType` (string) (**requerido**): This can be one of the following  LONGEST_AVAILABLE_AGENT  SKILLS_BASED(skillBasedRoutingType is mandatory to define) Valores: LONGEST_AVAILABLE_AGENT, SKILLS_BASED, CIRCULAR, LINEAR.
    - `skillBasedRoutingType` (string): This can be the following  LONGEST_AVAILABLE_AGENT  BEST_AVAILABLE_AGENT Valores: LONGEST_AVAILABLE_AGENT, BEST_AVAILABLE_AGENT.
    - `queueRoutingType` (string) (**requerido**): This can be the following  TEAM_BASED  QUEUE_BASED Valores: TEAM_BASED, SKILL_BASED, AGENT_BASED.
    - `queueSkillRequirements` (array): List of Queue Skill Requirements.
      - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
      - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
      - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
      - `skillId` (string) (**requerido**): Skill ID reference
      - `skillName` (string): Indicates the name of the skill. Once created, name cannot be modified.
      - `skillType` (string): This can be of the following types  PROFICIENCY: id = 0  BOOLEAN: id = 1  TEXT: id = 2  ENUM: id = 3  Once created, skillType cannot be modified.
      - `condition` (string) (**requerido**): Indicates a value that represents a skill the agent has.
      - `skillValue` (string) (**requerido**): A short textual description that represents a skill the agent has.
      - `weight` (integer/int32): Weight for proficiency skill requirement
      - `dynamicSkill` (boolean): Indicates whether the skill is a dynamic skill or not. Default value is false.
      - `createdTime` (integer/int64): This is the created time of the entity.
      - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
    - `agents` (array): The list of agents for AgentBased queue
      - `id` (string) (**requerido**): Id of an agent in WxCC
      - `ciUserId` (string): Id of an agent in Common Identity
    - `callDistributionGroups` (array) (**requerido**): List of Call Distribution Groups.
      - `agentGroups` (array): List of Agent Groups.
        - `teamId` (string): ID of a team
      - `order` (integer/int32): The order of this call distribution group.
      - `duration` (integer/int32): (Optional)The duration in seconds after which a contact in queue will be distributed to this group. Por defecto: 0.
    - `xspVersion` (string): (Optional) Used to subscribe for recording events. Long. max: 80.
    - `subscriptionId` (string): (Optional) Used to subscribe for recording events. Long. max: 80.
    - `assistantSkill` (object): Assistant skill related properties associated with the queue. This is applicable/available only when AI Assistant add-on offer/license is added to the organization.
      - `assistantSkillId` (string): Id of an Assistant Skill mapped to the Contact Service Queue. If the value is missing in response, the consumer should assume a value as null.
      - `assistantSkillUpdatedTime` (integer/int64) (solo lectura): Time(in epoch milliseconds) when assistant skill mapping was last updated.  If the value is missing in response, the consumer should assume a value as null.
    - `systemDefault` (boolean): Indicates whether the created resource is system created or not
    - `manuallyAssignable` (boolean): If `true`, the queue can be manually assigned.

## Ejemplo de invocación
```bash
curl -X POST '/organization/<orgid>/contact-service-queue/bulk' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**207**: Multi-Status
- `items` (array):
  - `itemIdentifier` (integer/int32): Unique item identifier for a bulk operation.
  - `status` (integer/int32): Indicates the error status code.
  - `operationType` (string): The kind of operation desired of an entity. Valores: CREATE, UPDATE, DELETE, GET.
  - `href` (string): The resource URI of an entity.
  - `apiError` (object): Response body for an API error.
    - `trackingId` (string): An opaque identifier for mapping protocol failures to service internal codes.   When specified in a request, it can be used for co-relating events across services
    - `error` (object): Details of an error.
      - `key` (string): An application defined error code.
      - `message` (array): A message providing details about the error.
        - `description` (string): A human readable explanation for the occurrence of an error.

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
- **409**: Similar entity is already present
  Ejemplo:
```json
{
  "trackingId": "ccconfig_af9eecc5-0472-4549-9a83-2afdae0d4ba0",
  "error": {
    "key": "409",
    "reason": "Test reason",
    "message": [
      {
        "description": "Test error",
        "code": "409",
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