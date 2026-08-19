---
doc_id: webex-cloud-calling-post-telephony-config-devices-actions-previewapplylinekeytemplate-invoke
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: POST
path: /telephony/config/devices/actions/previewApplyLineKeyTemplate/invoke
operation_id: previewApplyLineKeyTemplate
tags: Device Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-19T19:15:07.996809+00:00
---

# POST /telephony/config/devices/actions/previewApplyLineKeyTemplate/invoke

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `previewApplyLineKeyTemplate`

## Resumen
Preview Apply Line Key Template

## Descripción
Preview the number of devices that will be affected by the application of a Line Key Template or when resetting devices to their factory Line Key settings.

Line Keys, also known as Programmable Line Keys (PLK), are the keys found on either side of a typical desk phone display.
A Line Key Template is a definition of actions that will be performed by each of the Line Keys for a particular device model.
This API allows users to preview the number of devices that will be affected if a customer were to apply a Line Key Template or apply factory default Line Key settings to devices.

Retrieving the number of devices affected requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Preview Line Key Template for this organization.

## Cuerpo de la petición (application/json)
- `action` (string) (**requerido**): Line key Template action to perform.  * `APPLY_TEMPLATE` - Used to apply LinekeyTemplate to devices.  * `APPLY_DEFAULT_TEMPLATES` - Used to reset devices to its default Linekey Template configurations. Valores: APPLY_TEMPLATE, APPLY_DEFAULT_TEMPLATES.
- `templateId` (string) (**requerido**): `templateId` is required for `APPLY_TEMPLATE` action.
- `locationIds` (array): Used to search for devices only in the given locations.
- `excludeDevicesWithCustomLayout` (boolean): Indicates whether to exclude devices with custom layout.
- `includeDeviceTags` (array): Include devices only with these tags.
- `excludeDeviceTags` (array): Exclude devices with these tags.
- `advisoryTypes` (object):
  - `moreSharedAppearancesEnabled` (boolean): Refine search to apply changes to devices that contain the warning "More shared/virtual line appearances than shared/virtual lines requested".
  - `fewSharedAppearancesEnabled` (boolean): Refine search to apply changes to devices that contain the warning "More shared/virtual lines requested than shared/virtual line appearances".
  - `moreMonitorAppearancesEnabled` (boolean): Refine search to apply changes to devices that contain the warning "More monitored line appearances than monitored lines in the user's monitoring list".
  - `moreCPEAppearancesEnabled` (boolean): Refine search to apply changes to devices that contain the warning "More call park extension line appearances than call park extensions in user's monitoring list".
  - `moreModeManagementAppearancesEnabled` (boolean): Refine search to apply changes to devices that contain the warning "More mode management lines configured for the device". The default value is false.

### Ejemplo — petición
```json
{
  "action": "APPLY_TEMPLATE",
  "templateId": "Y2lzY29zcGFyazovL3VzL0RFVklDRV9MSU5FX0tFWV9URU1QTEFURS81NzVhMWY3Zi03MjRkLTRmZGUtODk4NC1mNjNhNDljMzYxZmQ",
  "locationIds": [
    "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2E4Mjg5NzIyLTFiODAtNDFiNy05Njc4LTBlNzdhZThjMTA5OA"
  ],
  "excludeDevicesWithCustomLayout": true,
  "includeDeviceTags": [
    "accounting",
    "sales"
  ],
  "excludeDeviceTags": [
    "admin"
  ],
  "advisoryTypes": {
    "moreSharedAppearancesEnabled": true,
    "fewSharedAppearancesEnabled": true,
    "moreMonitorAppearancesEnabled": "true",
    "moreCPEAppearancesEnabled": "true",
    "moreModeManagementAppearancesEnabled": true
  }
}
```

## Ejemplo de invocación
```bash
curl -X POST '/telephony/config/devices/actions/previewApplyLineKeyTemplate/invoke' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"action": "<action>", "templateId": "<templateId>"}'
```

## Respuestas correctas
**200**: OK
- `deviceCount` (number) (**requerido**): Number of devices affected.

### Ejemplo — respuesta 200
```json
{
  "deviceCount": 3
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