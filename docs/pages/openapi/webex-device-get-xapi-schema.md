---
doc_id: webex-device-get-xapi-schema
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
api_version: 1.0.0
method: GET
path: /xapi/schema
operation_id: Query Schema
tags: xAPI
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-18T23:45:44.213959+00:00
---

# GET /xapi/schema

**API:** Webex Device
**Área:** xAPI
**operationId:** `Query Schema`

## Resumen
Query Schema

## Descripción
Query the schema for statuses and commands of Webex RoomOS Devices. You specify the target devices in the `deviceId` parameter in the URI. Querying command schemas requires the `spark:xapi_commands` scope and querying status schemas requires the `spark:xapi_statuses` scope.

If no `status` or `command` expressions are specified, the full schema is returned, including both status and command schemas. If you specify any expression, the response is limited to only the types you queried for. For example, if you provide a `status` expression but no `command` expression, only status schemas will be included in the result.

See the [xAPI section of the Device Developers Guide](/docs/api/guides/device-developers-guide#xapi) or the [xAPI Command Reference](https://roomos.cisco.com/xapi) for a description of status and command expressions.

## Parámetros
- `deviceId` [query] (array) (**requerido**): A list of device IDs to query schemas from. A request can contain at most 5 device IDs.
- `status` [query] (array): A list of status key expressions to query schemas for. Supports patterns. Requires the `spark:xapi_statuses` scope.
- `command` [query] (array): A list of command key expressions to query schemas for. Supports patterns. Requires the `spark:xapi_commands` scope.

## Ejemplo de invocación
```bash
curl -X GET '/xapi/schema?deviceId=<deviceId>' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- (array de:)
  - `deviceId` (string): The unique identifier for the Webex RoomOS Device.
  - `status` (object): Status schemas keyed by status name.
  - `commands` (object): Command schemas keyed by command name.

### Ejemplo — respuesta 200
```json
[
  {
    "deviceId": "Y2lzY29zcGFyazovL3VzL0RFVklDRS8wNTVkYThiNy02NWI2LTQ5NjgtOTg1ZC02ZmFjODcwOWMyMDM",
    "status": {
      "Conference.HideNonVideo.Active": {
        "schema": {
          "enum": [
            "True",
            "False"
          ],
          "type": "string"
        }
      },
      "Network[1..n].Wifi.Noise": {
        "schema": {
          "type": "integer"
        }
      }
    },
    "commands": {
      "UserInterface.Extensions.Icon.Upload": {
        "arguments": {
          "Id": {
            "required": false,
            "schema": {
              "type": "string",
              "maxLength": 128,
              "minLength": 0
            }
          }
        },
        "resultSchema": {
          "type": [
            "object",
            "null"
          ]
        },
        "bodySchema": {
          "schema": {
            "type": [
              "object",
              "string"
            ],
            "maxLength": 4194304
          }
        }
      }
    }
  }
]
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