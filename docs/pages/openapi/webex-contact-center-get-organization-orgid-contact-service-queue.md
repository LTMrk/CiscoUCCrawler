---
doc_id: webex-contact-center-get-organization-orgid-contact-service-queue
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/contact-service-queue
operation_id: getAllFilteredConfigContactServiceQueue
tags: Contact Service Queue
deprecated: true
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T15:03:57.650215+00:00
---

# GET /organization/{orgid}/contact-service-queue

> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.

**API:** Webex Contact Center
**Área:** Contact Service Queue
**operationId:** `getAllFilteredConfigContactServiceQueue`

## Resumen
List Contact Service Queues

## Descripción
Retrieve a list of Contact Service Queues in a given organization.
 Note: Returning array fields in the List (Get All) API response is deprecated. To retrieve the complete resource with all fields, please use the Get-by-ID API instead. Deprecated. Use GET /v2/contact-service-queue instead.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. Supported filterable fields:  id.   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `channelTypes` [query] (array): [DEPRECATED] Channel type(s) allowed by the system.Separate values with commas.Use uppercase. By default, there is no channel type filtering.
- `attributes` [query] (string/string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported. except (callDistributionGroups,queueSkillRequirements,links)
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.
- `singleObjectResponse` [query] (boolean): Specify whether to include array fields in the response. This query parameter should be used only when the response contains a single record. It is not supported for responses with multiple objects and throws an exception. Por defecto: False.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/contact-service-queue' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- (array de:)
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string): Name of the Contact Service Queue
  - `description` (string): (Optional) A short description of the queue.
  - `queueType` (string): This can be the following  INBOUND  OUTBOUND Valores: INBOUND, OUTBOUND.
  - `checkAgentAvailability` (boolean): This setting specifies whether the system can exclude teams with no logged in agents for the relevant routing strategies. It does not support Social Channel Type.
  - `channelType` (string): Setting to indicate the channel type. Use uppercase. Supported channel types are:    TELEPHONY, EMAIL, SOCIAL_CHANNEL, and CHAT.   For TELEPHONY channelType, the following fields are mandatory - recordingPermitted, ivrRequeueUrl, recordingAllCallsPermitted, monitoringPermitted, parkingPermitted, pauseRecordingPermitted, controlFlowScriptUrl, defaultMusicInQueueMediaFileId. Valores: TELEPHONY, EMAIL, FAX, CHAT, VIDEO, OTHERS, SOCIAL_CHANNEL, WORK_ITEM, CUSTOM_MESSAGING.
  - `socialChannelType` (string): This can be the following  MESSAGEBIRD  MESSENGER Valores: MESSAGEBIRD, MESSENGER, WHATSAPP, APPLE_BUSINESS_CHAT, GOOGLE_BUSINESS_MESSAGES.
  - `serviceLevelThreshold` (integer/int32): The time in seconds that a customer request can be in a queue before the system flags it as outside the service level. It does not support Social Channel Type.
  - `maxActiveContacts` (integer/int32): The maximum number of simultaneous contacts allowed for this queue. It does not support Social Channel Type.
  - `maxTimeInQueue` (integer/int32): The time in seconds after which the system distributes the queued customer request to the overflow number that you provision for this queue.
  - `defaultMusicInQueueMediaFileId` (string): Identifies the default audio file which will be played for calls when they arrive or are waiting in queue.  This setting is available only for the Telephony channel type.
  - `timezone` (string): (Optional) Any routing strategy for this queue uses the time zone that you select here.
  - `active` (boolean): Specify whether the queue is active or not active
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
  - `routingType` (string): This can be one of the following  LONGEST_AVAILABLE_AGENT  SKILLS_BASED(skillBasedRoutingType is mandatory to define) Valores: LONGEST_AVAILABLE_AGENT, SKILLS_BASED, CIRCULAR, LINEAR.
  - `skillBasedRoutingType` (string): This can be the following  LONGEST_AVAILABLE_AGENT  BEST_AVAILABLE_AGENT Valores: LONGEST_AVAILABLE_AGENT, BEST_AVAILABLE_AGENT.
  - `queueRoutingType` (string): This can be the following  TEAM_BASED  QUEUE_BASED Valores: TEAM_BASED, SKILL_BASED, AGENT_BASED.
  - `xspVersion` (string): (Optional) Used to subscribe for recording events. Long. max: 80.
  - `subscriptionId` (string): (Optional) Used to subscribe for recording events. Long. max: 80.
  - `assistantSkill` (object): Assistant skill related properties associated with the queue. This is applicable/available only when AI Assistant add-on offer/license is added to the organization.
    - `assistantSkillId` (string): Id of an Assistant Skill mapped to the Contact Service Queue. If the value is missing in response, the consumer should assume a value as null.
    - `assistantSkillUpdatedTime` (integer/int64) (solo lectura): Time(in epoch milliseconds) when assistant skill mapping was last updated.  If the value is missing in response, the consumer should assume a value as null.
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not
  - `manuallyAssignable` (boolean): If `true`, the queue can be manually assigned.
  - `agentsLastUpdatedByUserName` (string): The name of the user who last modified the agents list.
  - `agentsLastUpdatedByUserEmailPrefix` (string): The email of the user who last modified the agents list.
  - `agentsLastUpdatedTime` (integer/int64): The date when the agents list was last modified (epoch timestamp in milliseconds).
  - `queueLevelSummariesInclusion` (string): Queue level summaries inclusion type. Used only when Queue inclusion for summaries is set to 'Specific Queues' at the org level AI Assistant->Summaries configuration. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained.This is applicable/available only when AI Assistant add-on offer/license is added to the organization. If the value is missing in response, the consumer should assume a value as EXCLUDED.
  - `queueLevelSentimentAnalysisInclusion` (string): Queue level sentiment analysis inclusion type. Used only when Queue inclusion for sentiment analysis is set to 'Specific Queues' at the org level AI Assistant->Quality Management configuration. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained.This is applicable/available when either AI Assistant/AI Quality Management add-on offer/license is added to the organization. If the value is missing in response, the consumer should assume a value as EXCLUDED.
  - `queueLevelPredictedWaitTimeInclusion` (string): Queue level predicted wait time inclusion type. Used only when Queue inclusion for predicted wait time is set to 'Specific Queues' at the org level AI Assistant->Predicted Wait Time configuration. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained. If the value is missing in response, the consumer should assume a value as EXCLUDED.
  - `queueLevelAutoCsatInclusion` (string): Queue level auto CSAT inclusion type. Used only when Queue inclusion for auto CSAT is set to 'Specific Queues' at the org level AI Assistant->Auto CSAT configuration. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained.This is applicable/available when either AI Assistant/AI Quality Management add-on offer/license is added to the organization. If the value is missing in response, the consumer should assume a value as EXCLUDED.
  - `queueLevelRealTimeTranscriptionsInclusion` (string): Queue level real time transcriptions inclusion type. Used only when Queue inclusion for real time transcriptions is set to 'Specific Queues' at the org level AI Assistant->Real Time Transcriptions configuration. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained.This is applicable/available when either AI Assistant/AI Quality Management add-on offer/license is added to the organization. If the value is missing in response, the consumer should assume a value as EXCLUDED.
  - `personalizedAIRouting` (object): Queue-level Personalized AI Routing configuration. Enables intelligent agent routing based on AI/ML predictions.
    - `aiRoutingMode` (string): AI Routing mode. Valid transitions: NONE → EVALUATION; EVALUATION → ACTIVE or NONE; ACTIVE → NONE. NONE: AI routing disabled (default). EVALUATION: Shadow mode - AI predictions are generated but not used for routing (for testing/validation). ACTIVE: AI routing enabled - contacts are routed based on AI predictions. Valores: NONE, EVALUATION, ACTIVE. Por defecto: NONE.
    - `aiRoutingKPIId` (string): AI Routing KPI ID - the performance metric used by AI to optimize routing decisions. This should reference a valid KPI configured in the AI routing system. Required when aiRoutingMode is EVALUATION or ACTIVE.
    - `evaluationModeStartTime` (integer/int64) (solo lectura): Timestamp (epoch milliseconds) when EVALUATION mode was activated. Automatically set by the system when transitioning from NONE to EVALUATION. Used to track evaluation duration and readiness for ACTIVE mode transition.
  - `pauseAndResume` (object): Pause and resume configuration for EMAIL and SOCIAL channels only
    - `enabled` (boolean): Indicates whether pause and resume is enabled for this queue
    - `pauseTimeout` (object): Pause timeout configuration. Required when enabled is true.
      - `days` (integer/int32): Number of days for pause timeout. Channel-specific maximum is enforced at the service layer based on configured limits.
      - `hours` (integer/int32): Number of hours for pause timeout (0-23)
      - `minutes` (integer/int32): Number of minutes for pause timeout (0-59)
  - `createdTime` (integer/int64): This is the created time of the entity.
  - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.

### Ejemplo — respuesta 200
```json
[
  {
    "recordingPermitted": true,
    "ivrRequeueUrl": "https://www.youtube.com",
    "agentsLastUpdatedByUserEmailPrefix": "string",
    "personalizedAIRouting": "string",
    "timezone": "America/New_York",
    "socialChannelType": "MESSENGER",
    "controlFlowScriptUrl": "https://flow-control.produs1.ciscoccservice.com/31f1c57f-4fa1-417b-b5c5-6feb6abea062/royal-enfield",
    "description": "Queue created by system",
    "monitoringPermitted": true,
    "vendorId": "AB123CSDR",
    "queueLevelRealTimeTranscriptionsInclusion": "INCLUDED",
    "channelType": "TELEPHONY",
    "queueRoutingType": "TEAM_BASED",
    "recordingAllCallsPermitted": true,
    "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
    "recordingPauseDuration": 2,
    "systemDefault": false,
    "defaultMusicInQueueMediaFileId": "defaultmusic_on_hold.wav",
    "queueLevelPredictedWaitTimeInclusion": "INCLUDED",
    "queueLevelAutoCsatInclusion": "INCLUDED",
    "serviceLevelThreshold": 0,
    "routingType": "SKILLS_BASED",
    "skillBasedRoutingType": "BEST_AVAILABLE_AGENT",
    "pauseAndResume": "string",
    "createdTime": 123456789,
    "lastUpdatedTime": 123456789,
    "id": "93912f11-6017-404b-bf14-5331890b1797",
    "maxTimeInQueue": 2,
    "xspVersion": "xsp-24.0",
    "maxActiveContacts": 5,
    "pauseRecordingPermitted": true,
    "checkAgentAvailability": true,
    "outdialCampaignEnabled": true,
    "assistantSkill": "string",
    "parkingPermitted": true,
    "agentsLastUpdatedByUser
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