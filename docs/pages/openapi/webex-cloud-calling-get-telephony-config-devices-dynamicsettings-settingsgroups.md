---
doc_id: webex-cloud-calling-get-telephony-config-devices-dynamicsettings-settingsgroups
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/devices/dynamicSettings/settingsGroups
operation_id: getSettingsGroups
tags: Device Call Settings With Device Dynamic Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-08-31T10:47:27.236982+00:00
---

# GET /telephony/config/devices/dynamicSettings/settingsGroups

**API:** Webex Cloud Calling
**Área:** Device Call Settings With Device Dynamic Settings
**operationId:** `getSettingsGroups`

## Resumen
Get Settings Groups

## Descripción
This API returns the `settingsGroups` that define the structure and association of tags for device dynamic settings.

 The `settingsGroups` are used to organize the tags into logical groups, making it easier to manage and configure device dynamic settings.

## Parámetros
- `orgId` [query] (string): Settings groups for devices in this organization.
- `familyOrModelDisplayName` [query] (string): Device family or model display name to filter the `settingsGroups`.
- `includeSettingsType` [query] (string): To show groups or tabs or both. Query param is case insensitive. Default is `ALL`. Valores: TABS, GROUPS, ALL.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/devices/dynamicSettings/settingsGroups' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK.
- `settingsGroups` (array): Array of settings groups defining structure and association of tags.
  - `path` (string): Path of the settings group. Creates an easily navigable settings hierarchy.
  - `friendlyName` (string): Friendly name of the settings group.
  - `tab` (string): Tab name associated with the settings group.
  - `familyOrModelDisplayName` (string): Family or model display name associated with the settings group.
  - `tags` (array): List of `tagBlock` objects associated with the settings group.
    - `tagBlock` (array): Array of tags associated with the settings group.
- `settingsTabs` (array): Array of settings tabs names. Can be filtered using the `includeSettingsType` parameter.

### Ejemplo — respuesta 200
```json
{
  "settingsGroups": [
    {
      "path": "Voice.Codec Preferences",
      "friendlyName": "voice.codecPref.G711Mu",
      "tab": "Poly",
      "familyOrModelDisplayName": "Poly",
      "tags": [
        {
          "tagBlock": [
            "%G711U_ORDER%"
          ]
        }
      ]
    },
    {
      "path": "Feature.Bluetooth",
      "friendlyName": "feature.bluetooth.enabled",
      "tab": "Poly",
      "familyOrModelDisplayName": "Poly",
      "tags": [
        {
          "tagBlock": [
            "%ENABLE_BLUETOOTH%"
          ]
        }
      ]
    },
    {
      "path": "User Interface.Menu",
      "friendlyName": "ui.menu.background",
      "tab": "Poly",
      "familyOrModelDisplayName": "Poly",
      "tags": [
        {
          "tagBlock": [
            "%DO_UI_MENU_BACKGROUND%"
          ]
        }
      ]
    }
  ],
  "settingsTabs": [
    "Poly",
    "MPP"
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