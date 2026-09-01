---
doc_id: webex-cloud-calling-post-devices-activationcode
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /devices/activationCode
operation_id: Create a Device Activation Code
tags: Devices
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-09-01T07:56:51.669915+00:00
---

# POST /devices/activationCode

**API:** Webex Cloud Calling
**Área:** Devices
**operationId:** `Create a Device Activation Code`

## Resumen
Create a Device Activation Code

## Descripción
Generate an activation code for a device in a specific workspace by `workspaceId` or for a person by `personId`. This requires an auth token with the `spark-admin:devices_write` scope, and either `identity:placeonetimepassword_create` (allows creating activation codes for workspaces only) or `identity:one_time_password` (allows creating activation codes for workspaces or persons).

* Adding a device to a workspace with calling type `none` or `thirdPartySipCalling` will reset the workspace calling type to `freeCalling`.

* Either `workspaceId` or `personId` should be provided. If both are supplied, the request will be invalid.

* If no `model` is supplied, the `code` returned will only be accepted on RoomOS devices.

* If your device is a phone, you must provide the `model` as a field. You can get the `model` from the [supported devices](/docs/api/v1/device-call-settings/read-the-list-of-supported-devices) API.

<div><Callout type="warning">Adding a device to a person with a Webex Calling Standard license will disable Webex Calling across their Webex mobile, tablet, desktop, and browser applications.</Callout></div><br><div><Callout type="warning">When adding devices to a Webex Calling Professional licensed person or workspace, wait for each API call to finish before starting the next. This prevents race conditions that can cause errors when assigning primary versus secondary device status.</Callout></div>

## Parámetros
- `orgId` [query] (string): The organization associated with the activation code generated. If left empty, the organization associated with the caller will be used.

## Cuerpo de la petición (application/json)
- `workspaceId` (string): The ID of the workspace where the device will be activated.
- `personId` (string): The ID of the person who will own the device once activated.
- `model` (string): The model of the device being created. The corresponding device model display name sometimes called the product name, can also be used to specify the model.

### Ejemplo — petición
```json
{
  "workspaceId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS83MTZlOWQxYy1jYTQ0LTRmZWQtOGZjYS05ZGY0YjRmNDE3ZjU",
  "model": "DMS Cisco 8865"
}
```

## Ejemplo de invocación
```bash
curl -X POST '/devices/activationCode' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

## Respuestas correctas
**200**: OK
- `code` (string): The activation code.
- `expiryTime` (string): The date and time the activation code expires.

### Ejemplo — respuesta 200
```json
{
  "code": "5414011256173816",
  "expiryTime": "2017-11-16T23:38:03.215Z"
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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs