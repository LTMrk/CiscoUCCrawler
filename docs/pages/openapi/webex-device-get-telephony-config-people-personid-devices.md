---
doc_id: webex-device-get-telephony-config-people-personid-devices
source: webex-openapi-specs/public-spec/webex-device.json
api: Webex Device
api_version: 1.0.0
method: GET
path: /telephony/config/people/{personId}/devices
operation_id: getPersonDevices
tags: Device Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-16T12:36:51.326567+00:00
---

# GET /telephony/config/people/{personId}/devices

**API:** Webex Device
**Área:** Device Call Settings
**operationId:** `getPersonDevices`

## Resumen
Get Person Devices

## Descripción
Get all devices for a person.

This requires a full or read-only administrator or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `personId` [path] (string) (**requerido**): Person for whom to retrieve devices.
- `orgId` [query] (string): Organization to which the person belongs.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/people/<personId>/devices' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `devices` (array) (**requerido**): Array of devices available to person.
  - `id` (string) (**requerido**): Unique identifier for a device.
  - `description` (array): Comma separated array of tags used to describe device.
  - `model` (string) (**requerido**): Identifier for device model.
  - `modelType` (object): Identifier for device model type.
  - `mac` (string): MAC address of device.
  - `ipAddress` (string): IP address of device.
  - `primaryOwner` (boolean) (**requerido**): Indicates whether the person or the workspace is the owner of the device, and points to a primary Line/Port of the device.
  - `type` (object) (**requerido**): Indicates if the line is acting as a primary line or a shared line for this device.
  - `hoteling` (object) (**requerido**): Hoteling login settings, which are available when the device is the owner's primary device and device type is PRIMARY. Hoteling login settings are set at the owner level.
  - `owner` (object) (**requerido**): Owner of device.
  - `activationState` (object) (**requerido**): Activation state of device.
- `maxDeviceCount` (number) (**requerido**): Maximum number of devices a person can be assigned to.
- `maxOwnedDeviceCount` (number) (**requerido**): Maximum number of devices a person can own.

### Ejemplo — respuesta 200
```json
{
  "devices": [
    {
      "id": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMV9pbnQxMy9DQUxMSU5HX0RFVklDRS8zMDAyZWJiZi1iMTVmLTQ1ODktYWNiZS1kZjY3OTA3MTU5NWE=",
      "descriptions": [
        "Your tag",
        "John Doe (Cisco 8875)"
      ],
      "model": "DMS Cisco 8875",
      "modelType": "MPP",
      "mac": "52EAD324FD21",
      "ipAddress": "10.201.128.187",
      "displayName": "Cisco 8875",
      "primaryOwner": true,
      "type": "PRIMARY",
      "hoteling": {
        "enabled": true,
        "limitGuestUse": true,
        "guestHoursLimit": 5
      },
      "owner": {
        "id": "Y2lzY29zcGFyazovL3VzL1BFUlNPTi81NzU2YWE1Yy03YjQ0LTQ3MjQtOGQ3ZS03NDE1MGVjODc4YmQ",
        "type": "PEOPLE",
        "firstName": "John",
        "lastName": "Doe"
      }
    }
  ],
  "maxDeviceCount": 1,
  "maxOwnedDeviceCount": 1
}
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