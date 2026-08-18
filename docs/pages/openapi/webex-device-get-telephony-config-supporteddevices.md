---
doc_id: webex-device-get-telephony-config-supporteddevices
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
api_version: 1.0.0
method: GET
path: /telephony/config/supportedDevices
operation_id: readTheListOfSupportedDevices
tags: Device Call Settings With Device Dynamic Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.194027+00:00
---

# GET /telephony/config/supportedDevices

**API:** Webex Device
**Área:** Device Call Settings With Device Dynamic Settings
**operationId:** `readTheListOfSupportedDevices`

## Resumen
Read the List of Supported Devices

## Descripción
Gets the list of supported devices for an organization.

Retrieving this list requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List supported devices for an organization.
- `allowConfigureLayoutEnabled` [query] (boolean): List supported devices that allow the user to configure the layout.
- `type` [query] (string): List supported devices of a specific type. To excluded device types from a request or query, add `type=not:DEVICE_TYPE`. For example, `type=not:MPP`.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/supportedDevices' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `upgradeChannelList` (array) (**requerido**): List of available upgrade channels.  * `STABLE` - These are standard stable releases.  * `STABLE_DELAY` - These are delayed stable releases.  * `PREVIEW` - These are Preview/pre-release versions.  * `BETA` - These are Beta testing versions.  * `TESTING` - These are testing versions.
- `devices` (array) (**requerido**): List of supported devices.
  - `model` (string) (**requerido**): Model name of the device.
  - `displayName` (string) (**requerido**): Display name of the device.
  - `familyDisplayName` (string): The display name of the device family.
  - `type` (string) (**requerido**): * `MPP` - Cisco Multiplatform Phone  * `ATA` - Analog Telephone Adapters  * `GENERIC_SIP` - GENERIC Session Initiation Protocol  * `ESIM` - Esim Supported Webex Go  * `DESK_PHONE` - Desk Phone Valores: MPP, ATA, GENERIC_SIP, ESIM, DESK_PHONE.
  - `manufacturer` (string) (**requerido**): * `CISCO` - Devices manufactured by Cisco.  * `THIRD_PARTY` - Devices manufactured by a third-party that are approved by a Cisco account manager to be enabled for provisioning in the control hub. Valores: CISCO, THIRD_PARTY.
  - `managedBy` (string) (**requerido**): * `CISCO` - Devices managed by Cisco.  * `CUSTOMER` - Devices managed by a customer that are approved by a Cisco account manager to be enabled for provisioning in the control hub. Valores: CISCO, CUSTOMER.
  - `supportedFor` (array) (**requerido**): List of places the device is supported for.
  - `onboardingMethod` (array) (**requerido**): Onboarding method.
  - `allowConfigureLayoutEnabled` (boolean) (**requerido**): Enables / Disables layout configuration for devices.
  - `numberOfLinePorts` (number) (**requerido**): Number of port lines.
  - `kemSupportEnabled` (boolean) (**requerido**): Indicates whether Kem support is enabled or not.
  - `kemModuleCount` (number): Module count.
  - `kemLinesSupportEnabled` (boolean) (**requerido**): Enables / disables Kem lines support.
  - `kemModuleType` (array): Key expansion module type of the device.
  - `upgradeChannelEnabled` (boolean) (**requerido**): Enables / Disables the upgrade channel.
  - `defaultUpgradeChannel` (string): The default upgrade channel.
  - `additionalPrimaryLineAppearancesEnabled` (boolean) (**requerido**): Enables / disables the additional primary line appearances.
  - `basicEmergencyNomadicEnabled` (boolean) (**requerido**): Enables / disables Basic emergency nomadic.
  - `customizedBehaviorsEnabled` (boolean) (**requerido**): Enables / disables customized behavior support on devices.
  - `allowConfigurePortsEnabled` (boolean) (**requerido**): Enables / disables configuring port support on device.
  - `customizableLineLabelEnabled` (boolean) (**requerido**): Enables / disables customizable line label.
  - `supportsLinePortReorderingEnabled` (boolean) (**requerido**): Enables / disables support line port reordering.
  - `portNumberSupportEnabled` (boolean) (**requerido**): Enables / disables port number support.
  - `t38Enabled` (boolean) (**requerido**): Enables / disables T.38.
  - `callDeclinedEnabled` (boolean) (**requerido**): Enables / disables call declined.
  - `touchScreenPhone` (boolean) (**requerido**): Supports touch screen on device.
  - `numberOfLineKeyButtons` (number) (**requerido**): Number of line key buttons for a device.
  - `deviceSettingsConfiguration` (string): * `WEBEX_CALLING_DEVICE_CONFIGURATION` - Devices which supports Webex Calling Device Settings Configuration.  * `WEBEX_DEVICE_CONFIGURATION` - Devices which supports Webex Device Settings Configuration.  * `WEBEX_CALLING_DYNAMIC_DEVICE_CONFIGURATION` - Devices which supports Webex Calling dynamic Settings Configuration.  * `NONE` - Devices does not support any configuration. Valores: WEBEX_CALLING_DEVICE_CONFIGURATION, WEBEX_DEVICE_CONFIGURATION, WEBEX_CALLING_DYNAMIC_DEVICE_CONFIGURATION, NONE.
  - `allowHotelingHostEnabled` (boolean) (**requerido**): Enables / disables hoteling host.
  - `supportsLogCollection` (string): * `NONE` - Devices which does not support log collection.  * `CISCO_PRT` - Devices which supports Cisco PRT log collection.  * `CISCO_ROOMOS` - Devices which supports Cisco RoomOS log collection. Valores: NONE, CISCO_PRT, CISCO_ROOMOS.
  - `supportsApplyChangesEnabled` (boolean) (**requerido**): Enables / disables apply changes.
  - `allowConfigureLinesEnabled` (boolean) (**requerido**): Enables / disables configure lines.
  - `allowConfigurePhoneSettingsEnabled` (boolean) (**requerido**): Enables / disables configure phone settings.
  - `supportsHotlineEnabled` (boolean) (**requerido**): Enables / disables hotline support.
  - `maxNumberOfLineAppearances` (number): Maximum number of line appearances available on the device.

### Ejemplo — respuesta 200
```json
{
  "upgradeChannelList": [
    "STABLE",
    "STABLE_DELAY",
    "PREVIEW",
    "BETA",
    "TESTING"
  ],
  "devices": [
    {
      "model": "2N Customer Managed",
      "displayName": "2N Customer Managed",
      "type": "GENERIC_SIP",
      "manufacturer": "THIRD_PARTY",
      "managedBy": "CUSTOMER",
      "supportedFor": [
        "PEOPLE",
        "PLACE"
      ],
      "onboardingMethod": [
        "MAC_ADDRESS"
      ],
      "allowConfigureLayoutEnabled": false,
      "numberOfLinePorts": 20,
      "kemSupportEnabled": true,
      "kemModuleCount": 1,
      "kemModuleType": [
        "KEM_20_KEYS"
      ],
      "upgradeChannelEnabled": false,
      "additionalPrimaryLineAppearancesEnabled": false,
      "basicEmergencyNomadicEnabled": false,
      "customizedBehaviorsEnabled": false,
      "allowConfigurePortsEnabled": false,
      "customizableLineLabelEnabled": false,
      "supportsLinePortReorderingEnabled": false,
      "kemLinesSupportEnabled": false,
      "portNumberSupportEnabled": false,
      "numberOfLineKeyButtons": 0,
      "t38Enabled": false,
      "callDeclinedEnabled": false,
      "touchScreenPhone": false,
      "deviceSettingsConfiguration": "NONE",
      "allowHotelingHostEnabled": false,
      "supportsLogCollection": "NONE",
      "supportsApplyChangesEnabled": false,
      "allowConfigureLinesEnabled": true,
      "allowConfigurePhoneSettingsEnabled": false,
      "supportsHotlineEnabled": false
    },
    {
      "model": "DMS Polycom EE4
  ... (truncado)
```
- Cabecera `Link`: 

## Respuestas de error
- **400**: Bad Request: The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
- **401**: Unauthorized: Authentication credentials were missing or incorrect.
- **403**: Forbidden: The request is understood, but it has been refused or access is not allowed.
- **404**: Not Found: The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
- **405**: Method Not Allowed: The request was made to a resource using an HTTP request method that is not supported.
- **409**: Conflict: The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
- **410**: Gone: The requested resource is no longer available.
- **415**: Unsupported Media Type: The request was made to a resource without specifying a media type or used a media type that is not supported.
- **423**: Locked: The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
- **428**: Precondition Required: File(s) cannot be scanned for malware and need to be force downloaded.
- **429**: Too Many Requests: Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
- **500**: Internal Server Error: Something went wrong on the server. If the issue persists, feel free to contact the [Webex Developer Support team](/explore/support).
- **502**: Bad Gateway: The server received an invalid response from an upstream server while processing the request. Try again later.
- **503**: Service Unavailable: Server is overloaded with requests. Try again later.
- **504**: Gateway Timeout: An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.

## Contexto de la API
The Webex Device APIs provide endpoints for managing and monitoring Webex devices, including registration, configuration, status retrieval, workspace assignment, and firmware management. These APIs support automation of device onboarding, health monitoring, remote troubleshooting, and bulk configuration updates. Integration scenarios include custom device dashboards, proactive alerting, and seamless workspace management for meeting rooms and shared spaces. The APIs are essential for IT teams managing large fleets of Webex devices across distributed environments.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs