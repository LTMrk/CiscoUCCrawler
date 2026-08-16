---
doc_id: webex-contact-center-get-organization-orgid-v2-ai-feature
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/v2/ai-feature
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.922899+00:00
---

# GET /organization/{orgid}/v2/ai-feature

**API:** Webex Contact Center
**Área:** AI Feature
**operationId:** `getAllConfigWithPagedMetaDataAiFeature`

## Resumen
List AI Feature resource(s)

## Descripción
Retrieve a list of AI Feature resource(s) in a given organization.Only one entry per organization can exist for AI Feature resource.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. Supported filterable fields:  id.   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `attributes` [query] (string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported.
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.

## Respuestas
- **200**: OK
  - `meta` (object): Metadata of response with paging information
    - `orgid` (string): Organization ID.
    - `page` (integer): Current page number.
    - `pageSize` (integer): Page size for current data set.
    - `totalPages` (integer): Number of pages.
    - `totalRecords` (integer): Total number of items.
    - `links` (object): Map of pagination links with `self`, `next`, `prev`, `last`, and `first`.
  - `data` (array):
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
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
