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
retrieved_at: 2026-08-18T23:45:43.269209+00:00
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
- `layoutMode` (string) (**requerido**): * `DEFAULT` - Default layout mode when a new device is added.  * `CUSTOM` - Enables a device to have its custom layout. Valores: DEFAULT, CUSTOM.
- `userReorderEnabled` (boolean): If `true`, user customization is enabled.
- `lineKeys` (array) (**requerido**): Contains a mapping of Line Keys and their corresponding actions.
  - `lineKeyIndex` (number) (**requerido**): An index representing a Line Key. Index starts from 1 representing the first key on the left side of the phone.
  - `lineKeyType` (string) (**requerido**): * `PRIMARY_LINE` - PRIMARY_LINE is the user's primary extension. This is the default assignment for Line Key Index 1 and cannot be modified.  * `SHARED_LINE` - Shows the appearance of other users on the owner's phone.  * `MONITOR` - Enables User and Call Park monitoring.  * `CALL_PARK_EXTENSION` - Enables the configure layout feature in Control Hub to set call park extension implicitly.  * `SPEED_DIAL` - Allows users to reach a telephone number, extension or a SIP URI.  * `OPEN` - An open key will automatically take the configuration of a monitor button starting with the first open key. These buttons are also usable by the user to configure speed dial numbers on these keys.  * `CLOSED` - Button not usable but reserved for future features.  * `MODE_MANAGEMENT` - Allows users to manage call forwarding for features via schedule-based routing. Valores: PRIMARY_LINE, SHARED_LINE, MONITOR, CALL_PARK_EXTENSION, SPEED_DIAL, OPEN, CLOSED, MODE_MANAGEMENT.
  - `lineKeyLabel` (string): This is applicable only when the lineKeyType is `SPEED_DIAL`.
  - `lineKeyValue` (string): Applicable only when the `lineKeyType` is `SPEED_DIAL`. Value must be a valid telephone number, ext, or SIP URI (format: `user@host` using A-Z,a-z,0-9,-_ .+ for `user` and `host`).
  - `sharedLineIndex` (number) (**requerido**): Shared line index is the line label number of the shared or virtual line assigned in the configured lines. Since you can add multiple appearances of the same shared or virtual line on a phone, entering the index number assigns the respective line to a line key. This is applicable only when the `lineKeyType` is SHARED_LINE. `sharedLineIndex` starts at 1 and increments by one for each shared line.
- `kemModuleType` (string): * `KEM_14_KEYS` - Extension module has 14 line keys that can be configured.  * `KEM_18_KEYS` - Extension module has 18 line keys that can be configured.  * `KEM_20_KEYS` - Extension module has 20 line keys that can be configured. Valores: KEM_14_KEYS, KEM_18_KEYS, KEM_20_KEYS.
- `kemKeys` (array): Contains a mapping of KEM Keys and their corresponding actions. For KEM keys not included in the request, they will be set to OPEN.
  - `kemModuleIndex` (number) (**requerido**): An index representing a KEM Module. The Index starts from 1 representing the first KEM Module.
  - `kemKeyIndex` (number) (**requerido**): An index representing a KEM Key. The Index starts from 1 representing the first key on the left side of the phone.
  - `kemKeyType` (string) (**requerido**): * `PRIMARY_LINE` - PRIMARY_LINE is the user's primary extension. This is the default assignment for Line Key Index 1 and cannot be modified.  * `SHARED_LINE` - Shows the appearance of other users on the owner's phone.  * `MONITOR` - Enables User and Call Park monitoring.  * `CALL_PARK_EXTENSION` - Enables the configure layout feature in Control Hub to set call park extension implicitly.  * `SPEED_DIAL` - Allows users to reach a telephone number, extension or a SIP URI.  * `OPEN` - An open key will automatically take the configuration of a monitor button starting with the first open key. These buttons are also usable by the user to configure speed dial numbers on these keys.  * `CLOSED` - Button not usable but reserved for future features.  * `MODE_MANAGEMENT` - Allows users to manage call forwarding for features via schedule-based routing. Valores: PRIMARY_LINE, SHARED_LINE, MONITOR, CALL_PARK_EXTENSION, SPEED_DIAL, OPEN, CLOSED, MODE_MANAGEMENT.
  - `kemKeyLabel` (string): Applicable only when the kemKeyType is `SPEED_DIAL`.
  - `kemKeyValue` (string): Applicable only when the `lineKeyType` is `SPEED_DIAL`. Value must be a valid telephone number, ext, or SIP URI (format: `user@host` using A-Z,a-z,0-9,-_ .+ for `user` and `host`).
  - `sharedLineIndex` (number) (**requerido**): Shared line index is the line label number of the shared or virtual line assigned in the configured lines. Since you can add multiple appearances of the same shared or virtual line on a phone, entering the index number assigns the respective line to a line key. This is applicable only when the `lineKeyType` is SHARED_LINE. `sharedLineIndex` starts at 1 and increments by one for each shared line.

### Ejemplo — respuesta 200
```json
{
  "layoutMode": "CUSTOM",
  "userReorderEnabled": "true",
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