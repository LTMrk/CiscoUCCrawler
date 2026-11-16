---
doc_id: webex-cloud-calling-put-telephony-config-devices-deviceid-settings
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: PUT
path: /telephony/config/devices/{deviceId}/settings
operation_id: updateDeviceSettings
tags: Device Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:50.629038+00:00
---

# PUT /telephony/config/devices/{deviceId}/settings

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `updateDeviceSettings`

## Resumen
Update device settings

## Descripción
Modify override settings for a device.

Device settings list all the applicable settings for an MPP and an ATA devices at the device level. Admins can also modify the settings. NOTE: DECT devices do not support settings at the device level.

Updating settings on the device requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `deviceId` [path] (string) (**requerido**): Unique identifier for the device.
- `orgId` [query] (string): Organization in which the device resides..
- `deviceModel` [query] (string): The model type of the device. The corresponding device model display name sometimes called the product name, can also be used to specify the model.

## Cuerpo de la petición (application/json)
- `customizations` (object) (**requerido**): Indicates the customization object of the device settings.
- `customEnabled` (boolean) (**requerido**): Indicates if customization is allowed at a device level. If true, customized at a device level. If false, not customized; uses customer-level configuration.

### Ejemplo — petición
```json
{
  "customizations": {
    "mpp": {
      "pnacEnabled": true,
      "audioCodecPriority": {
        "primary": "OPUS",
        "secondary": "G722",
        "tertiary": "G711u",
        "selection": "CUSTOM"
      },
      "backlightTimerOldModel": "THIRTY_SECONDS",
      "background": {
        "customUrl": "",
        "image": "WEBEX_DARK_BLUE"
      },
      "displayNameFormat": "PERSON_FIRST_THEN_LAST_NAME",
      "cdpEnabled": false,
      "defaultLoggingLevel": "DEBUGGING",
      "dndServicesEnabled": true,
      "acd": {
        "enabled": true,
        "displayCallqueueAgentSoftkeys": "LAST_PAGE"
      },
      "shortInterdigitTimer": 14,
      "longInterdigitTimer": 16,
      "lineKeyLabelFormat": "PERSON_EXTENSION",
      "lineKeyLEDPattern": "DEFAULT",
      "lldpEnabled": false,
      "mppUserWebAccessEnabled": true,
      "multicast": [
        "192.86.108.226:2223"
      ],
      "enhancedMulticast": {
        "xmlAppUrl": "http://127.0.0.1:8080/",
        "multicastList": [
          {
            "hostAndPort": "224.0.0.0:22",
            "hasXmlAppUrl": true,
            "xmlAppTimeout": 10
          }
        ]
      },
      "offHookTimer": 30,
      "phoneLanguage": "RUSSIAN",
      "poeMode": "MAXIMUM",
      "qosEnabled": true,
      "screenTimeout": {
        "enabled": true,
        "value": 400
      },
      "usbPortsEnabled": true,
      "vlan": {
        "enabled": false,
        "value": 1,
        "pcPort": 1
      },
      "wifiNetwork": {
    
  ... (truncado)
```

## Ejemplo de invocación
```bash
curl -X PUT '/telephony/config/devices/<deviceId>/settings' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"customizations": "<customizations>", "customEnabled": true}'
```

## Respuestas correctas
**204**: No Content

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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs