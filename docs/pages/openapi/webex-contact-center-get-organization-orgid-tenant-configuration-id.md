---
doc_id: webex-contact-center-get-organization-orgid-tenant-configuration-id
source: webex-openapi-specs/public-spec/webex-contact-center.json
api: Webex Contact Center
api_version: 1.0.0
method: GET
path: /organization/{orgid}/tenant-configuration/{id}
operation_id: getConfigTenantConfiguration
tags: Tenant Configuration
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-10-12T11:51:20.980626+00:00
---

# GET /organization/{orgid}/tenant-configuration/{id}

**API:** Webex Contact Center
**Área:** Tenant Configuration
**operationId:** `getConfigTenantConfiguration`

## Resumen
Get specific Tenant Configuration by ID

## Descripción
Retrieve an existing Tenant Configuration by ID in a given organization.

## Parámetros
- `orgid` [path] (string) (**requerido**): Organization ID to be used for this operation. The specified security token must have permission to interact with the organization.
- `id` [path] (string) (**requerido**): ID of this contact center resource.

## Ejemplo de invocación
```bash
curl -X GET '/organization/<orgid>/tenant-configuration/<id>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `organizationId` (string/uuid): ID of the contact center organization. This field is required for all bulk save operations. User-token updates are not permitted for this field. Long. max: 36.
- `id` (string): ID of this contact center resource. It should not be specified when creating a new resource. However, it is mandatory when updating a resource.
- `version` (integer/int32): The version of this resource. For a newly created resource, it will be 0 unless specified otherwise.
- `outdialEnabled` (boolean): Outdial Enabled. User-token updates are not permitted for this field.
- `centralLogLevel` (string): Central Log Level. User-token updates are not permitted for this field.
- `autoWrapUpInterval` (integer/int64): Auto Wrap Up Interval. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `localDiskLogLevel` (string): Local Disk Log Level. User-token updates are not permitted for this field.
- `dnOtherDescription` (string): Dn Other Description. User-token updates are not permitted for this field.
- `dnDefaultDescription` (string): Dn Default Description. User-token updates are not permitted for this field.
- `notRespondingToAvailableTimeout` (integer/int64): Not Responding To Available Timeout. User-token updates are not permitted for this field.
- `heartBeatInterval` (integer/int64): Heart Beat Interval. User-token updates are not permitted for this field.
- `callVariablesSuppressed` (string): Call Variables Suppressed. User-token updates are not permitted for this field.
- `endCallEnabled` (boolean): End Call Enabled. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `incidentReportingEnabled` (boolean): Incident Reporting Enabled. User-token updates are not permitted for this field.
- `watsonAnalyticsPassword` (string): Watson Analytics Password. User-token updates are not permitted for this field.
- `systemRecoveryMsg` (string): System Recovery Msg. User-token updates are not permitted for this field.
- `watsonAnalyticsBaseUrl` (string): Watson Analytics Base Url. User-token updates are not permitted for this field.
- `dnTargetStripChars` (string): Dn Target Strip Chars. User-token updates are not permitted for this field.
- `watsonAnalyticsUserName` (string): Watson Analytics User Name. User-token updates are not permitted for this field.
- `dnOtherRegex` (string): Dn Other Regex. User-token updates are not permitted for this field.
- `configurationVersion` (number/double): Configuration Version. User-token updates are not permitted for this field.
- `callVariablesBaseUrl` (string): Call Variables Base Url. User-token updates are not permitted for this field.
- `lostConnectionRecoveryTimeout` (integer/int64): Lost Connection Recovery Timeout. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `diagnosticsPostUrl` (string): Diagnostics Post Url. User-token updates are not permitted for this field.
- `dnDefaultRegex` (string): Dn Default Regex. User-token updates are not permitted for this field.
- `apsUrl` (string): Aps Url. User-token updates are not permitted for this field.
- `endConsultEnabled` (boolean): End Consult Enabled. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `rejectDuplicateDn` (boolean): Reject Duplicate Dn. User-token updates are not permitted for this field.
- `dnTargetRegex` (string): Dn Target Regex. User-token updates are not permitted for this field.
- `forceDefaultDn` (boolean): Force Default Dn. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `dnDefaultPrefix` (string): Dn Default Prefix. User-token updates are not permitted for this field.
- `privacyShieldVisible` (boolean): Privacy Shield Visible. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `consoleLogLevel` (string): Console Log Level. User-token updates are not permitted for this field.
- `dnTargetPrefix` (string): Dn Target Prefix. User-token updates are not permitted for this field.
- `autoBaseUrl` (boolean): Auto Base Url. User-token updates are not permitted for this field.
- `dnOtherPrefix` (string): Dn Other Prefix. User-token updates are not permitted for this field.
- `dnDefaultStripChars` (string): Dn Default Strip Chars. User-token updates are not permitted for this field.
- `missedHeartBeatsAllowed` (integer/int64): Missed Heart Beats Allowed. User-token updates are not permitted for this field.
- `dnOtherStripChars` (string): Dn Other Strip Chars. User-token updates are not permitted for this field.
- `apsEnabled` (boolean): Aps Enabled. User-token updates are not permitted for this field.
- `timeoutDesktopInactivityEnabled` (boolean): Timeout Desktop Inactivity Enabled. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `timeoutDesktopInactivityMins` (integer/int32): Timeout Desktop Inactivity Mins. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `timeoutRonaTelephonySeconds` (integer/int32) (**requerido**): Timeout Rona Telephony Seconds. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `timeoutRonaSocialSeconds` (integer/int32) (**requerido**): Timeout Rona Social Seconds. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `timeoutRonaChatSeconds` (integer/int32) (**requerido**): Timeout Rona Chat Seconds. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `timeoutRonaEmailSeconds` (integer/int32) (**requerido**): Timeout Rona Email Seconds. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `timeoutRonaWorkItemSeconds` (integer/int32): RONA timeout for work items in seconds. Valid range: 1-6000. Only applicable when wxcc_digital_work_item feature flag is enabled. User-token updates are permitted for this field when authorized by the required scope and User Profile permission.
- `timeoutRonaCustomMessagingSeconds` (integer/int32): RONA timeout for custom messaging in seconds. Valid range: 1-6000. Only applicable when wxcc_digital_byoc feature flag is enabled. User-token updates are not permitted for this field.
- `systemDefault` (boolean): Indicates whether the created resource is system created or not User-token updates are not permitted for this field.
- `createdTime` (integer/int64): This is the created time of the entity. User-token updates are not permitted for this field.
- `lastUpdatedTime` (integer/int64): This is the updated time of the entity. User-token updates are not permitted for this field.

### Ejemplo — respuesta 200
```json
{
  "id": "93912f11-6017-404b-bf14-5331890b1797",
  "organizationId": "f53c8b54-46ca-43f6-ba05-08426a46e23d",
  "centralLogLevel": "INFO",
  "autoWrapUpInterval": 30000,
  "localDiskLogLevel": "INFO",
  "dnOtherDescription": "Other DN",
  "dnDefaultDescription": "Default DN",
  "notRespondingToAvailableTimeout": 300000,
  "heartBeatInterval": 30000,
  "callVariablesSuppressed": "false",
  "watsonAnalyticsPassword": "example-only",
  "systemRecoveryMsg": "System is recovering",
  "watsonAnalyticsBaseUrl": "https://example.com/analytics",
  "dnTargetStripChars": "",
  "watsonAnalyticsUserName": "example-user",
  "dnOtherRegex": "",
  "configurationVersion": 1,
  "callVariablesBaseUrl": "https://example.com/call-variables",
  "lostConnectionRecoveryTimeout": 60000,
  "diagnosticsPostUrl": "https://example.com/diagnostics",
  "dnDefaultRegex": "",
  "apsUrl": "https://example.com/aps",
  "dnTargetRegex": "",
  "dnDefaultPrefix": "",
  "consoleLogLevel": "INFO",
  "dnTargetPrefix": "",
  "dnOtherPrefix": "",
  "dnDefaultStripChars": "",
  "missedHeartBeatsAllowed": 3,
  "dnOtherStripChars": "",
  "timeoutDesktopInactivityMins": 30,
  "timeoutRonaTelephonySeconds": 30,
  "timeoutRonaSocialSeconds": 30,
  "timeoutRonaChatSeconds": 30,
  "timeoutRonaEmailSeconds": 30,
  "timeoutRonaWorkItemSeconds": 6000,
  "timeoutRonaCustomMessagingSeconds": 6000,
  "outdialEnabled": false,
  "endCallEnabled": false,
  "incidentReportingEnabled": false,
  "endConsultEnabled": false,
  "rejectDuplic
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