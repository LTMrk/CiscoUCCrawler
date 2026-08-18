---
doc_id: webex-device-get-telephony-config-devices-dynamicsettings-validationschema
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
api_version: 1.0.0
method: GET
path: /telephony/config/devices/dynamicSettings/validationSchema
operation_id: getValidationSchema
tags: Beta Device Call Settings With Dynamic Device Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.203150+00:00
---

# GET /telephony/config/devices/dynamicSettings/validationSchema

**API:** Webex Device
**Área:** Beta Device Call Settings With Dynamic Device Settings
**operationId:** `getValidationSchema`

## Resumen
Get Validation Schema

## Descripción
This API returns the validation schema for `tags` of all or specific `familyOrModelDisplayName`.

The schema is used to validate the `tag` for devices in the `Webex Calling` platform. The schema includes information about the required fields, data types, and validation rules for each setting.

## Parámetros
- `orgId` [query] (string): Validation schema for devices in this organization.
- `familyOrModelDisplayName` [query] (string): Device family or model display name to filter the schema.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/devices/dynamicSettings/validationSchema' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK.
- `tags` (array): Array of device settings tags with their validation rules.
  - `familyOrModelDisplayName` (string): The family or model name of the device to which these settings apply.
  - `tag` (string): The unique identifier for the setting.
  - `friendlyName` (string): A user-friendly name for the setting. It helps to correlate the tag with the UI in settings groups.
  - `tooltip` (string): Explanatory text for the setting.
  - `alert` (string): Alert message related to this setting, if applicable.
  - `level` (array): The levels at which this setting can be configured. When fetching tags or updating tags, the tag should be allowed at the level the request is made for.
  - `validationRule` (object): Validation rules and constraints for device setting values.
    - `type` (string): The data type of the setting. Possible values are `string`, `integer`, `boolean`, `enum` , `password` or `network`.
    - `values` (array): Possible values for `enum` or `boolean` types.
    - `min` (integer): Minimum value for numeric types.
    - `max` (integer): Maximum value for numeric types.
    - `increment` (integer): Increment value for numeric types.
    - `regex` (string): Regular expression pattern for string validation.
    - `maxLength` (integer): Maximum length for string values.
    - `validationHint` (string): Hint to display to users about validation requirements.

### Ejemplo — respuesta 200
```json
{
  "tags": [
    {
      "familyOrModelDisplayName": "Poly",
      "tag": "%G711U_ORDER%",
      "friendlyName": "voice.codecPref.G711Mu",
      "tooltip": "Tag tooltip.",
      "level": [
        "location",
        "device"
      ],
      "validationRule": {
        "type": "int",
        "min": 0,
        "max": 10,
        "increment": 1
      }
    },
    {
      "familyOrModelDisplayName": "Poly",
      "tag": "%G722_ORDER%",
      "friendlyName": "voice.codecPref.G722",
      "tooltip": "Tag tooltip.",
      "level": [
        "location",
        "device"
      ],
      "validationRule": {
        "type": "int",
        "min": 0,
        "max": 10,
        "increment": 1
      }
    },
    {
      "familyOrModelDisplayName": "Poly",
      "tag": "%ENABLE_BLUETOOTH%",
      "friendlyName": "feature.bluetooth.enabled",
      "tooltip": "Tag tooltip.",
      "level": [
        "organization",
        "location",
        "device"
      ],
      "validationRule": {
        "type": "boolean",
        "values": [
          "1",
          "0"
        ]
      }
    },
    {
      "familyOrModelDisplayName": "Poly",
      "tag": "%DO_BLUETOOTH_DEVICE_NAME%",
      "friendlyName": "bluetooth.device.name",
      "tooltip": "Tag tooltip.",
      "alert": "Alert text.",
      "level": [
        "organization",
        "location",
        "device"
      ],
      "validationRule": {
        "type": "string",
        "regex": "[A-Za-z0-9]+",
        "maxLength": 255
      }
    },
   
  ... (truncado)
```

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