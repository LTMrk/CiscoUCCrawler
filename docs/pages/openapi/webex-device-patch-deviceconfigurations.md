---
doc_id: webex-device-patch-deviceconfigurations
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
api_version: 1.0.0
method: PATCH
path: /deviceConfigurations
operation_id: Update Device Configurations
tags: Device Configurations
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.205758+00:00
---

# PATCH /deviceConfigurations

**API:** Webex Device
**Área:** Device Configurations
**operationId:** `Update Device Configurations`

## Resumen
Update Device Configurations

## Descripción
Edit configurations for the device specified by device ID.

## Parámetros
- `deviceId` [query] (string) (**requerido**): Update device configurations by device ID.

## Cuerpo de la petición (application/json-patch+json)
- `op` (string): * `remove` - Remove the configured value and revert back to the default from schema, if present.  * `replace` - Set the configured value. Valores: remove, replace.
- `path` (string): Only paths ending in `/sources/configured/value` are supported.

### Ejemplo — petición
```json
[
  {
    "op": "replace",
    "path": "Audio.Ultrasound.MaxVolume/sources/configured/value",
    "value": 50
  },
  {
    "op": "remove",
    "path": "Conference.MaxReceiveCallRate/sources/configured/value"
  }
]
```

## Ejemplo de invocación
```bash
curl -X PATCH '/deviceConfigurations?deviceId=<deviceId>' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**201**: Created
- `deviceId` (string) (**requerido**): ID of the device that the configurations are for.
- `items` (object):
  - `configuration_key` (object): Key of the configuration.
    - `source` (string): The source of the current value that is applied to the device.  * `default` - Current value comes from the schema default.  * `configured` - Current value comes from configuredValue. Valores: default, configured.
    - `sources` (object):
      - `default` (object):
        - `editability` (object):
      - `configured` (object):
        - `editability` (object):
    - `valueSpace` (object): [JSON Schema](http://json-schema.org/) describing the data format of the configuration as specified by the device.

### Ejemplo — respuesta 201
```json
{
  "deviceId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hL0RFVklDRS9hNmYwYjhkMi01ZjdkLTQzZDItODAyNi0zM2JkNDg3NjYzMTg=",
  "items": {
    "Audio.Ultrasound.MaxVolume": {
      "value": 50,
      "source": "configured",
      "sources": {
        "default": {
          "value": 70,
          "editability": {
            "isEditable": false,
            "reason": "FACTORY_DEFAULT"
          }
        },
        "configured": {
          "value": 50,
          "editability": {
            "isEditable": true
          }
        }
      },
      "valueSpace": {
        "type": "integer",
        "maximum": 100,
        "minimum": 0
      }
    },
    "FacilityService.Service[1].Name": {
      "value": "Live Support",
      "source": "default",
      "sources": {
        "default": {
          "value": "Live Support",
          "editability": {
            "isEditable": false,
            "reason": "FACTORY_DEFAULT"
          }
        },
        "configured": {
          "value": null,
          "editability": {
            "isEditable": true
          }
        }
      },
      "valueSpace": {
        "type": "string",
        "maxLength": 1024,
        "minLength": 0
      }
    },
    "Conference.MaxReceiveCallRate": {
      "value": 6000,
      "source": "default",
      "sources": {
        "default": {
          "value": 6000,
          "editability": {
            "isEditable": false,
            "reason": "FACTORY_DEFAULT"
          }
        },
        "configured": {

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