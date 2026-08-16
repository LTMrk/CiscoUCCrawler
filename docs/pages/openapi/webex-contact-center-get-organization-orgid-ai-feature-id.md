---
doc_id: webex-contact-center-get-organization-orgid-ai-feature-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/ai-feature/{id}
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.922499+00:00
---

# GET /organization/{orgid}/ai-feature/{id}

**API:** Webex Contact Center
**Área:** AI Feature
**operationId:** `getConfigAiFeature`

## Resumen
Get specific AI Feature resource by ID

## Descripción
Retrieve an existing AI Feature resource by ID in a given organization.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) **(requerido)**: Resource ID of the AI Feature resource.

## Respuestas
- **200**: OK
  - `organizationId` (string): ID of the contact center organization. This field is required for all bulk save operations.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `realtimeTranscripts` (object): This is applicable/available when either AI Assistant/AI Quality Management add-on offer/license is added to the organization.
    - `enable` (boolean) **(requerido)**: Used to toggle the state of the AI feature sub feature  configuration from active to inactive and vice-versa. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
    - `agentInclusionType` (string): Provides information whether all or specific agents are selected for realtime transcripts. Valores: ALL, SPECIFIC.
    - `queuesInclusionType` (string): Provides information whether all or specific queues are selected for Real time transcription. If the value is missing in response, the consumer should assume a value as ALL. Valores: ALL, SPECIFIC.
  - `suggestedResponses` (object): This is applicable/available only when AI Assistant add-on offer/license is added to the organization.
    - `enable` (boolean) **(requerido)**: Used to toggle the state of the AI feature sub feature  configuration from active to inactive and vice-versa. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
  - `generatedSummaries` (object): This is applicable/available only when AI Assistant add-on offer/license is added to the organization.
    - `callDropSummariesEnabled` (boolean): Used to toggle the enable/disable call drop summaries for Generated Summaries configuration. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
    - `virtualAgentTransferSummariesEnabled` (boolean): Used to toggle the enable/disable virtual agent transfer summaries for Generated Summaries configuration. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
    - `consultTransferSummariesEnabled` (boolean): Used to toggle the enable/disable mid call consult/transfer summaries in Generated Summaries configuration. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
    - `wrapUpSummariesEnabled` (boolean): Used to toggle the enable/disable post call summaries in Generated Summaries configuration. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
    - `queuesInclusionType` (string): Provides information whether all or specific queues are selected for Generated Summaries resource. If the value is missing in response, the consumer should assume a value as ALL. Valores: ALL, SPECIFIC.
  - `agentWellbeing` (object): This is applicable/available only when AI Assistant add-on offer/license is added to the organization.
    - `enable` (boolean) **(requerido)**: Used to toggle the state of the AI feature sub feature  configuration from active to inactive and vice-versa. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
    - `agentInclusionType` (string) **(requerido)**: Provides information whether all or specific agents are selected for Agent Wellbeing. If the value is missing in response, the consumer should assume a value as ALL. Valores: ALL, SPECIFIC.
    - `wellnessBreakReminders` (string): Provides information whether Wellness break reminders are enabled or disabled. If the value is missing in response, the consumer should assume a value as DISABLED. Valores: DISABLED, ENABLED.
  - `autoCSAT` (object): This is applicable/available when either AI Assistant/AI Quality Management add-on offer/license is added to the organization.
    - `enable` (boolean) **(requerido)**: Used to toggle the state of the AI feature sub feature  configuration from active to inactive and vice-versa. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
    - `queuesInclusionType` (string): Provides information whether all or specific queues are selected for Auto CSAT. If the value is missing in response, the consumer should assume a value as ALL. Valores: ALL, SPECIFIC.
    - `selectedGlobalVariableId` (string): Selected Global Variable ID for Auto CSAT. If the value is missing in response, the consumer should assume a value as null.
    - `surveyDataSource` (string): Survey Data Source Type for Auto CSAT. If the value is missing in response, the consumer should assume a value as EXPERIENCE_MANAGEMENT. Valores: EXPERIENCE_MANAGEMENT, GLOBAL_VARIABLE.
  - `coachingInsights` (object): This is applicable/available only when AI Quality Management add-on offer/license is added to the organization.
    - `enable` (boolean) **(requerido)**: Used to toggle the state of the Coaching Insights  configuration from active to inactive and vice-versa. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
  - `evaluationsAndAnalytics` (object): This is applicable/available only when AI Quality Management add-on offer/license is added to the organization.
    - `enable` (boolean) **(requerido)**: Used to toggle the state of the Evaluations and Analytics  configuration from active to inactive and vice-versa. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
  - `sentimentAnalysis` (object): This is applicable/available when either AI Assistant/AI Quality Management add-on offer/license is added to the organization.
    - `enable` (boolean) **(requerido)**: Used to toggle the state of the Sentiment Analysis  configuration from active to inactive and vice-versa. Mandatory for create/update operation. If the value is missing in response, the consumer should assume a value as false.
    - `queuesInclusionType` (string): Provides information whether all or specific queues are selected for Sentiment Analysis. If the value is missing in response, the consumer should assume a value as ALL. Valores: ALL, SPECIFIC.
  - `predictedWaitTime` (object): AI wait time feature configuration
    - `enable` (boolean) **(requerido)**: Used to toggle the state of the Predicted Wait Time  configuration from active to inactive and vice-versa. Mandatory for create/update operation.
    - `queuesInclusionType` (string): Provides information whether all or specific queues are selected for Predicted Wait Time. Valores: ALL, SPECIFIC.
  - `personalizedAIRouting` (object):
    - `enable` (boolean): Used to toggle the state of the Personalized AI Routing  configuration from active to inactive and vice-versa. Mandatory for create/update operation.
    - `cjdsWorkspaceId` (string): Id of the CJDS workspace id to be used for model training.
    - `cjdsProfileTemplateId` (string): Id of the CJDS Profile template to be used for model training.
  - `createdTime` (integer): This is the created time of the entity.
  - `lastUpdatedTime` (integer): This is the updated time of the entity.
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
