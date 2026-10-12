---
doc_id: webex-contact-center-get-organization-orgid-organization-setting-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/organization-setting/{id}
operation_id: getConfigOrganizationSetting
tags: Organization Setting
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-10-12T11:51:20.953136+00:00
---

# GET /organization/{orgid}/organization-setting/{id}

**API:** Webex Contact Center
**Área:** Organization Setting
**operationId:** `getConfigOrganizationSetting`

## Resumen
Get specific Organization Setting by ID

## Descripción
Retrieve an existing Organization Setting by ID in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): ID of this contact center resource.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/organization-setting/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. User-token updates are not permitted for this field. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `tenantXmlUrl` (string) (**requerido**): Tenant Xml Url. User-token updates are not permitted for this field.
- `ivrParkUrl` (string) (**requerido**): Ivr Park Url. User-token updates are not permitted for this field.
- `wfoEnabled` (boolean) (**requerido**): Wfo Enabled. User-token updates are not permitted for this field.
- `campaignManagerEnabled` (boolean) (**requerido**): Campaign Manager Enabled. User-token updates are not permitted for this field.
- `configureSpeechEnabledIVREnabled` (boolean) (**requerido**): Configure Speech Enabled IVREnabled. User-token updates are not permitted for this field.
- `shortCallThreshold` (integer/int32) (**requerido**): Short Call Threshold. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `lostCallThreshold` (integer/int32) (**requerido**): Lost Call Threshold. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `concurrentVoiceContactEntitlement` (integer/int32): Concurrent Voice Contact Entitlement. User-token updates are not permitted for this field.
- `voiceContactSurgeFactor` (number/double) (**requerido**): Voice Contact Surge Factor. User-token updates are not permitted for this field.
- `concurrentDigitalContactEntitlement` (integer/int32): Concurrent Digital Contact Entitlement. User-token updates are not permitted for this field.
- `digitalContactSurgeFactor` (number/double) (**requerido**): Digital Contact Surge Factor. User-token updates are not permitted for this field.
- `basicNativeVirtualAgentQuantity` (integer/int32): Basic Native Virtual Agent Quantity. User-token updates are not permitted for this field.
- `maximumActiveCalls` (integer/int32) (**requerido**): Maximum Active Calls. User-token updates are not permitted for this field.
- `inboundMaximumActiveCalls` (integer/int32) (**requerido**): Inbound Maximum Active Calls. User-token updates are not permitted for this field.
- `outdialMaximumActiveCalls` (integer/int32) (**requerido**): Outdial Maximum Active Calls. User-token updates are not permitted for this field.
- `maximumThresholdRules` (integer/int32): Maximum Threshold Rules. User-token updates are not permitted for this field.
- `allowAgentThresholds` (boolean) (**requerido**): Allow Agent Thresholds. User-token updates are not permitted for this field.
- `pauseResumeEnabled` (boolean) (**requerido**): Pause Resume Enabled. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `recordingPauseDuration` (integer/int32) (**requerido**): Recording Pause Duration. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `recordAllCalls` (boolean) (**requerido**): Record All Calls. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `recordingMode` (string): Recording Mode. User-token updates are permitted for this field when authorized by the required scope and User Profile permission. Valores: AUDIO_ONLY, AUDIO_AND_SCREEN, DISABLED.
- `webexManagementEnabled` (boolean) (**requerido**): Webex Management Enabled. User-token updates are not permitted for this field.
- `webexManagementUrl` (string): Webex Management Url. User-token updates are not permitted for this field.
- `licenseVersion` (string): License Version. User-token updates are not permitted for this field. Long. max: 50.
- `adapterId` (string): Adapter Id. User-token updates are not permitted for this field. Long. max: 36.
- `otgId` (string): Otg Id. User-token updates are not permitted for this field. Long. max: 80.
- `retryCallbackInterval` (integer/int32) (**requerido**): Retry Callback Interval. User-token updates are not permitted for this field.
- `maximumCallbackAttempts` (integer/int32) (**requerido**): Maximum Callback Attempts. User-token updates are not permitted for this field.
- `cccEnabled` (boolean) (**requerido**): Ccc Enabled. User-token updates are not permitted for this field.
- `sbrEnabled` (boolean) (**requerido**): Sbr Enabled. User-token updates are not permitted for this field.
- `maximumTextSkills` (integer/int32) (**requerido**): Maximum Text Skills. User-token updates are not permitted for this field.
- `maximumSkills` (integer/int32) (**requerido**): Maximum Skills. User-token updates are not permitted for this field.
- `multiMediaEnabled` (boolean) (**requerido**): Multi Media Enabled. User-token updates are not permitted for this field.
- `maxChannels` (integer/int32) (**requerido**): Max Channels. User-token updates are not permitted for this field.
- `voiceCallBackEnabled` (boolean) (**requerido**): Voice Call Back Enabled. User-token updates are not permitted for this field.
- `jukeboxEnabled` (boolean) (**requerido**): Jukebox Enabled. User-token updates are not permitted for this field.
- `pruningStrategy` (string) (**requerido**): Pruning Strategy. User-token updates are not permitted for this field. Valores: NONE, TIME_BASED, STORAGE_BASED, AGENT_MINUTES.
- `pruningValue` (integer/int32) (**requerido**): Pruning Value. User-token updates are not permitted for this field.
- `analyticsEnabled` (boolean) (**requerido**): Analytics Enabled. User-token updates are not permitted for this field.
- `maximumVirtualTeams` (integer/int32) (**requerido**): Maximum Virtual Teams. User-token updates are not permitted for this field.
- `maximumAddressBooks` (integer/int32) (**requerido**): Maximum Address Books. User-token updates are not permitted for this field.
- `numberOfCadVariables` (integer/int32) (**requerido**): Number Of Cad Variables. User-token updates are not permitted for this field.
- `externalId` (string): External Id. User-token updates are not permitted for this field. Long. max: 120.
- `thresholdAlertsEnabled` (boolean) (**requerido**): Threshold Alerts Enabled. User-token updates are not permitted for this field.
- `lastAgentRouting` (boolean) (**requerido**): Last Agent Routing. User-token updates are not permitted for this field.
- `legRecordingEnabled` (boolean) (**requerido**): Leg Recording Enabled. User-token updates are not permitted for this field.
- `multipleTimeZoneEnabled` (boolean) (**requerido**): Multiple Time Zone Enabled. User-token updates are not permitted for this field.
- `voicePrefix` (string): Voice Prefix. User-token updates are not permitted for this field. Long. max: 40.
- `steeringDigitsEnabled` (boolean) (**requerido**): Steering Digits Enabled. User-token updates are not permitted for this field.
- `socialChannel` (boolean) (**requerido**): Social Channel. User-token updates are not permitted for this field.
- `flowBuilderEnabled` (boolean) (**requerido**): Flow Builder Enabled. User-token updates are not permitted for this field.
- `resourcesCreated` (boolean) (**requerido**): Resources Created. User-token updates are not permitted for this field.
- `wfoAnalyticsWithTranscription` (boolean) (**requerido**): Wfo Analytics With Transcription. User-token updates are not permitted for this field.
- `wfoBundleAgents` (integer/int32): Wfo Bundle Agents. User-token updates are not permitted for this field.
- `wfoBundle` (boolean) (**requerido**): Wfo Bundle. User-token updates are not permitted for this field.
- `speechEnabledIVRPorts` (integer/int32): Speech Enabled IVRPorts. User-token updates are not permitted for this field.
- `qualityManagement` (boolean) (**requerido**): Quality Management. User-token updates are not permitted for this field.

### Ejemplo — respuesta 200
```json
{
  "id": "93912f11-6017-404b-bf14-5331890b1797",
  "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "tenantXmlUrl": "https://example.com/tenant.xml",
  "ivrParkUrl": "https://example.com/ivr-park",
  "shortCallThreshold": 5,
  "lostCallThreshold": 5,
  "concurrentVoiceContactEntitlement": 100,
  "voiceContactSurgeFactor": 1,
  "concurrentDigitalContactEntitlement": 100,
  "digitalContactSurgeFactor": 1,
  "basicNativeVirtualAgentQuantity": 0,
  "maximumActiveCalls": 100,
  "inboundMaximumActiveCalls": 100,
  "outdialMaximumActiveCalls": 100,
  "maximumThresholdRules": 100,
  "recordingPauseDuration": 30,
  "licenseVersion": "1.0",
  "adapterId": "adapter-example",
  "otgId": "otg-example",
  "retryCallbackInterval": 5,
  "maximumCallbackAttempts": 3,
  "maximumTextSkills": 100,
  "maximumSkills": 100,
  "maxChannels": 10,
  "pruningStrategy": "NONE",
  "pruningValue": 0,
  "maximumVirtualTeams": 100,
  "maximumAddressBooks": 100,
  "numberOfCadVariables": 100,
  "externalId": "external-example",
  "voicePrefix": "9",
  "wfoBundleAgents": 0,
  "speechEnabledIVRPorts": 0,
  "offerCode": "CJPPRM",
  "orderId": "order-example",
  "license": "license-example",
  "serviceProvisioningId": "provisioning-example",
  "orderSubscriptionId": "subscription-example",
  "billingGroupId": "billing-example",
  "outboundSipDomain": "example.com",
  "purgeInactiveEntitiesInterval": 1,
  "inactivateEntitiesPurgedOn": "2024-01-01T00:00:00Z",
  "aiAssistantQuantity": 0,
  "routingToSam
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