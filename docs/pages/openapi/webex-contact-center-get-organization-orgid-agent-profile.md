---
doc_id: webex-contact-center-get-organization-orgid-agent-profile
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/agent-profile
operation_id: getAllConfigDesktopProfile
tags: Desktop Profile
deprecated: true
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.686802+00:00
---

# GET /organization/{orgid}/agent-profile

> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.

**API:** Webex Contact Center
**Área:** Desktop Profile
**operationId:** `getAllConfigDesktopProfile`

## Resumen
List Desktop Profiles

## Descripción
Retrieve a list of Desktop Profiles in a given organization.
 Note: Returning array fields in the List (Get All) API response is deprecated. To retrieve the complete resource with all fields, please use the Get-by-ID API instead. Deprecated. Use GET /v2/agent-profile instead.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `filter` [query] (string): Specify a filter based on which the results will be fetched. Supported filterable fields:  id.   The examples below show some search queries - id=="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id!="57efb0e6-5af0-4245-a67d-d3c5045cdb6e" - id=in=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") - id=out=("57efb0e6-5af0-4245-a67d-d3c5045cdb6e","a421e0b2-732e-46f3-a057-39160a53afb9") This parameter uses the RSQL query syntax, a URI-friendly format for expressing criteria for filtering REST entities. For more information about RSQL in general, see  <a href="https://www.here.com/docs/bundle/data-client-library-developer-guide-java-scala/page/client/rsql.html">this reference</a>. For a list of supported operators, see <a href="https://github.com/perplexhub/rsql-jpa-specification#rsql-syntax-reference">this syntax guide</a>.  Note: values to be used in the filter syntax should not contain spaces. If they do, please enclose them in quotes to apply the filter.
- `attributes` [query] (string/string): Specify the attributes to be returned. By default, all attributes are returned along with the specified columns. All attributes are supported. except ( wrapUpCodes,queues, idleCodes,entryPoints, buddyTeams, dialPlans, loginVoiceOptions, viewableStatistics, thresholdRules,agentDNValidationCriterions )
- `page` [query] (integer): Defines the number of displayed page. The page number starts from 0. Por defecto: 0.
- `pageSize` [query] (integer): Defines the number of items to be displayed on a page. If the number specified is more than allowed max page size, the API will automatically adjust the page size to the max page size. Por defecto: 100.
- `singleObjectResponse` [query] (boolean): Specify whether to include array fields in the response. This query parameter should be used only when the response contains a single record. It is not supported for responses with multiple objects and throws an exception. Por defecto: False.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/agent-profile' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- (array de:)
  - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
  - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
  - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
  - `name` (string): Enter a name for the agent profile. Long. max: 80.
  - `description` (string): (Optional) Enter a description of the profile. Long. max: 255.
  - `parentType` (string): This can be the following  ORGANIZATION: The agent profile is available to all sites at your enterprise.  SITE: The agent profile is available to a specific site. Valores: ORGANIZATION, SITE.
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
  - `accessWrapUpCode` (string): Specify the wrap-up codes that the agents can select when they wrap up a contact.It can take one of these values:  ALL — To make all wrap-up codes available.  SPECIFIC — To make specific codes available. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `wrapUpCodes` (array): Specify the wrap-up codes list that the agents can select when they wrap up a contact.
  - `accessIdleCode` (string): Specify the Idle codes that the agents can select in Agent Desktop.It can take one of these values:  ALL — To make all idle codes available.  SPECIFIC — To make specific codes available. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `idleCodes` (array): Specify the Idle codes list that the agents can select in Agent Desktop.
  - `accessQueue` (string): Specify the queues that the agents can select from the Queue drop-down list on the Agent Desktop.It can take one of these values:  ALL — To make all queues available.  SPECIFIC — To make specific queues available  NONE — If you do not want to make any queues available as transfer targets. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `accessEntryPoint` (string): Specify the entry points that the agents can select from the Entry Point drop-down list on the Agent Desktop.It can take one of these values:  ALL — To make all entry points available.  SPECIFIC — To make specific entry points available  NONE — If you do not want to make any entry points available as transfer targets. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `accessBuddyTeam` (string): Specify the teams that the agents can select from the Agent drop-down list on the Agent Desktop. It can take one of these values:  ALL —  To make the agents on all teams available.  SPECIFIC — To make agents on specific teams available, then select teams from the drop-down list  NONE — If you do not want to make any teams available for consultation, conference, or call transfer. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
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
  - `agentDNValidation` (string): Specifies the validation applied when an agent logs in with a DN.  **Supported values going forward:** `ALL` (Unrestricted — agents may use any DN) and  `PROVISIONED_VALUE` (login DN restricted to the value provisioned for the agent).  **Note:** `SPECIFIC` (Validation Criteria) is no longer supported and must not be used  for new or updated profiles. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `agentDNValidationCriteria` (string) (DEPRECADO): **Deprecated** as of 2026.06; will be removed after consumers migrate. This setting occurs only if you select Validation Criteria in the Validation For Agent DN. Valores: SPECIFIC, ALL, PROVISIONED_VALUE, NONE.
  - `agentDNValidationCriterions` (array) (DEPRECADO): **Deprecated** as of 2026.06; will be removed after consumers migrate. This setting specify the list that occurs only if you select Validation Criteria in the Validation For Agent DN.
  - `loginVoiceOptions` (array): List of Login Voice Options.
  - `active` (boolean): Specify whether the agent profile is active or not Active.
  - `systemDefault` (boolean): Indicates whether the created resource is system created or not
  - `createdTime` (integer/int64): This is the created time of the entity.
  - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
  - `autoAcceptDigitalInteractions` (boolean): Automatically accept digital interactions when agent becomes available

### Ejemplo — respuesta 200
```json
[
  {
    "timeoutDesktopInactivityMins": 5,
    "showUserDetailsMS": true,
    "manageChannelAvailability": true,
    "buddyTeams": [
      "5_Jan_Testing",
      "7_Feb_Testing"
    ],
    "scheduleAndManageCallBack": true,
    "timeoutDesktopInactivityCustomEnabled": true,
    "wrapUpCodes": [
      "WrapUp_Sale",
      "WrapUp_Field"
    ],
    "description": "This profile allows agent to auto wrap-up time and extend the wrap-up time.",
    "agentDNValidation": "ALL",
    "autoAcceptDigitalInteractions": false,
    "agentDNValidationCriterions": [
      "DN_5_Sept",
      "DN_7_Jan"
    ],
    "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
    "systemDefault": false,
    "outdialANIId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
    "stateSynchronizationMS": true,
    "outdialEnabled": true,
    "allowAutoWrapUpExtension": true,
    "idleCodes": [
      "aux_code_sale",
      "aux_code2"
    ],
    "accessIdleCode": "ALL",
    "createdTime": 123456789,
    "lastUpdatedTime": 123456789,
    "id": "93912f11-6017-404b-bf14-5331890b1797",
    "showUserDetailsWebex": true,
    "dialPlans": [
      "US",
      "Any Format"
    ],
    "accessWrapUpCode": "ALL",
    "dialPlanEnabled": true,
    "autoAnswer": true,
    "accessBuddyTeam": "ALL",
    "active": true,
    "outdialEntryPointId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
    "version": 1,
    "loginVoiceOptions": [
      "AGENT_DN",
      "EXTENSION",
      "BROWSER"
    ],
    "parentType": "SITE",
    "addressBo
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