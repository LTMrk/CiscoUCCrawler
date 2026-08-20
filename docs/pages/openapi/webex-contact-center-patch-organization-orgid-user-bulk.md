---
doc_id: webex-contact-center-patch-organization-orgid-user-bulk
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: PATCH
path: /organization/{orgid}/user/bulk
operation_id: patchAllConfigUser
tags: Users
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-20T13:57:48.718254+00:00
---

# PATCH /organization/{orgid}/user/bulk

**API:** Webex Contact Center
**Área:** Users
**operationId:** `patchAllConfigUser`

## Resumen
Bulk partial update Users

## Descripción
Update some or all properties for multiple users in bulk for a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.

## Cuerpo de la petición (application/json)
- `items` (array): List of items in the bulk request.
  - `itemIdentifier` (integer/int32): Unique item identifier for a bulk operation.
  - `item` (object): User data transfer object for creating and updating user information in the contact center system
    - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
    - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
    - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
    - `firstName` (string) (**requerido**): The first name of the user. Can be changed using Users Management in Cisco Webex Control Hub.
    - `lastName` (string) (**requerido**): The last name of the user. Can be changed using Users Management in Cisco Webex Control Hub.
    - `email` (string) (**requerido**): The email address of the user. Can be changed using Users Management in Cisco Webex Control Hub.
    - `workPhone` (string): The work phone number of the user. Long. max: 20.
    - `mobile` (string): The mobile phone number of the user. Long. max: 20.
    - `ciUserId` (string) (**requerido**): Cisco Common Identity user Id. Existence of a CI user is a prerequisite to create a new WxCC user. It cannot be modified.
    - `broadCloudUserId` (string): Broadcloud user Id. This field cannot be modified.
    - `userProfileId` (string) (**requerido**): Identifier for an user profile which a Contact Center administrator has configured. Changing the profile type requires a token with `FLS:Read_Scope` scope.  As of today, changing the profile type for a user is supported only from Cisco Webex Control Hub.
    - `contactCenterEnabled` (boolean) (**requerido**): The setting is for accessing the Agent Desktop to handle customer requests.
    - `timezone` (string): (Optional) The time zone that you provision for your enterprise.
    - `xspVersion` (string): (Optional) Used to subscribe for recording events. This field cannot be modified. Long. max: 80.
    - `subscriptionId` (string): (Optional) Used to subscribe for recording events. This field cannot be modified. Long. max: 80.
    - `siteId` (string): (Optional) Identifier for a site which is a physical contact center location under the control of your enterprise. This field is applicable only when contactCenterEnabled is true.
    - `teamIds` (array): Specify the teams id which got assigned to this user.  Note: You can't assign this profile to a capacity-based team. This field is applicable only when contactCenterEnabled is true.
    - `skillProfileId` (string): (Optional) If your enterprise uses the optional Skills-Based Routing feature, This profile overrides any skill profile at the team level that is associated with the agent.This field is applicable only when contactCenterEnabled is true.
    - `agentProfileId` (string): Identifier for a Desktop Profile which is a group of permissions and Agent Desktop behaviors that you assign to specific users. This field is applicable only when contactCenterEnabled is true.
    - `multimediaProfileId` (string): (Optional) If your organization administrator enables Multimedia for your enterprise, you can select a multimedia profile for this team. This field is applicable only when contactCenterEnabled is true.
    - `deafultDialledNumber` (string): (Optional) The dial number of the agent. This field is applicable only when contactCenterEnabled is true.
    - `externalIdentifier` (string): (Optional) Agent identification details, such as the employee number.
    - `active` (boolean) (**requerido**): Indicates whether the user is active or not active. Can be changed using Users Management in Cisco Webex Control Hub.
    - `imiUserCreated` (boolean): (Optional) Indicates whether this user has a corresponding user created in IMI digital channel. This field cannot be modified.
    - `preferredSupervisorTeamId` (string): (Optional) Indicates the id of a preferred supervisor.
    - `userLevelBurnoutInclusion` (string): User level burnout inclusion type. Used only when Agent inclusion is set to 'Specific Agents' at the org level Agent Wellbeing>Burnout config. If the value is missing in response, the consumer should assume a value as EXCLUDED. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained.This is applicable/available only when AI Assistant add-on offer/license is added to the organization. Valores: INCLUDED, EXCLUDED.
    - `userLevelAutoCSATInclusion` (string) (DEPRECADO): User level AutoCSAT inclusion type. Used only when Agent inclusion is set to 'Specific Agents' at the org level Cisco AI Assistant>Auto CSAT config. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained. Valores: INCLUDED, EXCLUDED.
    - `userLevelWellnessBreakReminders` (string): User level Wellness break reminder type. If top level Agent burnout config has wellness break reminders enabled, this property determines if an Agent is enabled/disabled for receiving break reminders. If the value is missing in response, the consumer should assume a value as DISABLED. This is applicable/available only when AI Assistant add-on offer/license is added to the organization. Valores: DISABLED, ENABLED.
    - `userLevelSummariesInclusion` (string) (DEPRECADO): User level Generated Summaries inclusion type. Used only when Generated Summaries is set to 'Specific Agents' at the org level Cisco AI Assistant>Generated Summaries. During entity creation(single or bulk), if this parameter is not provided or null, default will be set to 'EXCLUDED' During entity update(single or bulk), if this parameter is not provided or null, the previous value will be retained. Valores: INCLUDED, EXCLUDED.
    - `supervisorCapabilitiesEnabled` (boolean): Indicates whether supervisor capabilities are enabled for the user.
    - `agentCapabilitiesEnabled` (boolean): Indicates whether agent capabilities are enabled for the user.
    - `dynamicSkills` (array): The list of dynamic skills assigned to the user
      - `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. Long. max: 36.
      - `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
      - `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
      - `skillId` (string) (**requerido**): The ID of the skill.
      - `skillName` (string): The name of the skill. Used for bulk upload operations to resolve skill by name instead of ID.
      - `textValue` (string): A short textual description that represents a skill the agent has. Long. max: 100.
      - `booleanValue` (boolean): Indicates whether the agent has this skill (True) or does not have the skill (False).
      - `proficiencyValue` (integer/int32): A number between 0 and 10 to indicate how proficient the agent is in this skill.
      - `enumValue` (string): The enum value for enum-type skills. Supports multiple values as pipe-delimited string (e.g., '30|20|10').
      - `enumSkillValues` (string): Indicates a value that represents a skill the agent has.
      - `createdTime` (integer/int64): This is the created time of the entity.
      - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
    - `createdTime` (integer/int64): This is the created time of the entity.
    - `lastUpdatedTime` (integer/int64): This is the updated time of the entity.
  - `requestAction` (string): Identifier for action type. Possible values are `SAVE` and `DELETE`.

### Ejemplo — petición
```json
{
  "items": [
    {
      "item": {
        "id": "26e2df70-0f77-41b8-8e8f-1d76e92c9638",
        "firstName": "John14",
        "lastName": "Wick14",
        "email": "john.wick14@company.com",
        "ciUserId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
        "userProfileId": "1dq21e23-1234-5578-9a83-2afdae0d4ba1",
        "contactCenterEnabled": true,
        "userLevelBurnoutInclusion": "INCLUDED",
        "active": true
      },
      "itemIdentifier": 0,
      "requestAction": "SAVE"
    }
  ]
}
```

## Ejemplo de invocación
```bash
curl -X PATCH '/organization/<orgid>/user/bulk' \
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