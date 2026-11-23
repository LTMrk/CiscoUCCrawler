---
doc_id: webex-cloud-calling-get-telephony-config-devices-deviceid-layout
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/devices/{deviceId}/layout
operation_id: getDeviceLayoutByDeviceId
tags: Device Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-23T14:21:15.783832+00:00
---

# GET /telephony/config/devices/{deviceId}/layout

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `getDeviceLayoutByDeviceId`

## Resumen
Get Device Layout by Device ID

## Descripción
Get layout information of a device by device ID in an organization.

Device layout customizes a user’s programmable line keys (PLK) on the phone and any attached Key Expansion Modules (KEM) with the existing configured line members and the user’s monitoring list.

**Note:** When `layoutMode` is DEFAULT, the response includes only `layoutMode` and `userReorderEnabled`. The `lineKeys` field is omitted as the device uses system-assigned default line-key assignments. When `layoutMode` is CUSTOM, the response includes the `lineKeys` array with the custom line-key configuration.

This API requires a full or location administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `deviceId` [path] (string) (**requerido**): Get device layout for this device ID.
- `orgId` [query] (string): Retrieve a device layout for the device in this organization.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/devices/<deviceId>/layout' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `layoutMode` (object) (**requerido**): Defines the layout mode of the device, i.e. DEFAULT or CUSTOM.
- `userReorderEnabled` (boolean): If `true`, user customization is enabled.
- `lineKeys` (array): Contains a mapping of Line Keys and their corresponding actions. This field is required when `layoutMode` is CUSTOM. When `layoutMode` is DEFAULT, this field is not returned in GET responses and should not be included in PUT requests, as the system uses the default line-key assignments.
  - `lineKeyIndex` (number) (**requerido**): An index representing a Line Key. Index starts from 1 representing the first key on the left side of the phone.
  - `lineKeyType` (object) (**requerido**): The action that would be performed when the Line Key is pressed.
  - `lineKeyLabel` (string): This is applicable only when the lineKeyType is `SPEED_DIAL`.
  - `lineKeyValue` (string): Applicable only when the `lineKeyType` is `SPEED_DIAL`. Value must be a valid telephone number, ext, or SIP URI (format: `user@host` using A-Z,a-z,0-9,-_ .+ for `user` and `host`).
  - `sharedLineIndex` (number) (**requerido**): Shared line index is the line label number of the shared or virtual line assigned in the configured lines. Since you can add multiple appearances of the same shared or virtual line on a phone, entering the index number assigns the respective line to a line key. This is applicable only when the `lineKeyType` is SHARED_LINE. `sharedLineIndex` starts at 1 and increments by one for each shared line.
- `kemModuleType` (object): Type of KEM module.
- `kemKeys` (array): Contains a mapping of KEM Keys and their corresponding actions. For KEM keys not included in the request, they will be set to OPEN.
  - `kemModuleIndex` (number) (**requerido**): An index representing a KEM Module. The Index starts from 1 representing the first KEM Module.
  - `kemKeyIndex` (number) (**requerido**): An index representing a KEM Key. The Index starts from 1 representing the first key on the left side of the phone.
  - `kemKeyType` (object) (**requerido**): The action that would be performed when the KEM Key is pressed.
  - `kemKeyLabel` (string): Applicable only when the kemKeyType is `SPEED_DIAL`.
  - `kemKeyValue` (string): Applicable only when the `lineKeyType` is `SPEED_DIAL`. Value must be a valid telephone number, ext, or SIP URI (format: `user@host` using A-Z,a-z,0-9,-_ .+ for `user` and `host`).
  - `sharedLineIndex` (number) (**requerido**): Shared line index is the line label number of the shared or virtual line assigned in the configured lines. Since you can add multiple appearances of the same shared or virtual line on a phone, entering the index number assigns the respective line to a line key. This is applicable only when the `lineKeyType` is SHARED_LINE. `sharedLineIndex` starts at 1 and increments by one for each shared line.

### Ejemplo — respuesta 200
```json
{
  "layoutMode": "CUSTOM",
  "userReorderEnabled": true,
  "lineKeys": [
    {
      "lineKeyIndex": 1,
      "lineKeyType": "PRIMARY_LINE"
    },
    {
      "lineKeyIndex": 2,
      "lineKeyType": "SPEED_DIAL",
      "lineKeyLabel": "Home",
      "lineKeyValue": "213456"
    }
  ],
  "kemModuleType": "KEM_14_KEYS",
  "kemKeys": [
    {
      "kemModuleIndex": 1,
      "kemKeyIndex": 1,
      "kemKeyType": "CLOSED"
    },
    {
      "kemModuleIndex": 1,
      "kemKeyIndex": 2,
      "kemKeyType": "SPEED_DIAL",
      "kemKeyLabel": "Office",
      "kemKeyValue": "213457"
    },
    {
      "kemModuleIndex": 1,
      "kemKeyIndex": 3,
      "kemKeyType": "SHARED_LINE",
      "sharedLineIndex": 1
    }
  ]
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