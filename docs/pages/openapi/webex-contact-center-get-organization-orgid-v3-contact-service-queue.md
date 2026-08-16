---
doc_id: webex-contact-center-get-organization-orgid-v3-contact-service-queue
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
method: GET
path: /organization/{orgid}/v3/contact-service-queue
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.937416+00:00
---

# GET /organization/{orgid}/v3/contact-service-queue

**API:** Webex Contact Center
**Área:** Contact Service Queue
**operationId:** `getAllFilteredConfigWithMetaDataV3ContactServiceQueue`

## Resumen
List Contact Service Queues

## Descripción
Retrieve a list of Contact Service Queues in a given organization.
 Note: Returning array fields in the List (Get All) API response is deprecated. To retrieve the complete resource with all fields, please use the Get-by-ID API instead. Deprecated. Use GET /v2/contact-service-queue instead.

## Parámetros
- `orgid` [path] (string) **(requerido)**: Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. All the fields are supported except: organizationId, queueSkillRequirements, xspVersion, createdTime, lastUpdatedTime   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `attributes` [query] (string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported. except (callDistributionGroups,queueSkillRequirements,links)
- `search` [query] (string): Filter data based on the search keyword.Supported search columns(name, description)  The examples below show some search queries - "Cisco" - field=="name";value=="Cisco" - fields=in=("name","description");value=="Cisco"
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size.
- `desktopProfileFilter` [query] (boolean): If set to true, the API will return only the data that the user has access to according to its Desktop Profile. If unspecified, the default value is false.
- `provisioningView` [query] (boolean): If set to true, the API will only return data that the user has access to, according to the User Profile. This query parameter is applicable only when desktopProfileFilter query parameter is false.
- `singleObjectResponse` [query] (boolean): Specify whether to include array fields in the response. This query parameter should be used only when the response contains a single record. It is not supported for responses with multiple objects and throws an exception.

## Respuestas
- **200**: OK
  - `meta` (object): Pagination metadata for paged API responses
    - `orgid` (string): ID of the contact center organization. This field is required for all bulk save operations.
    - `page` (integer): Current page number.
    - `pageSize` (integer): Page size for current data set.
    - `totalPages` (integer): Number of pages.
    - `totalRecords` (integer): Total number of items.
    - `links` (object):
      - `self` (string) **(requerido)**: Link to the current page.
      - `first` (string): Link to the first page.
      - `last` (string): Link to the last page.
      - `next` (string): Link to the next page.
      - `prev` (string): Link to the previous page.
  - `data` (array): List of items matching the entity type.
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
- **401**: Unauthorized Operation
- **403**: Operation is forbidden
- **404**: Resource not found or URI is invalid
- **429**: Too many requests have been sent in a given amount of time and the request has been rate limited
- **500**: An Unexpected Error Occurred

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
