---
doc_id: webex-cloud-calling-get-telephony-config-locations-locationid-devices-settings
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
api_version: 1.0.0
method: GET
path: /telephony/config/locations/{locationId}/devices/settings
operation_id: getLocationDeviceSettings
tags: Device Call Settings
deprecated: false
scopes: 
license: CC-BY-4.0
retrieved_at: 2026-11-23T14:21:15.773485+00:00
---

# GET /telephony/config/locations/{locationId}/devices/settings

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `getLocationDeviceSettings`

## Resumen
Get Location Device Settings

## Descripción
Get device override settings for a location.

This requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `locationId` [path] (string) (**requerido**): Unique identifier for the location.
- `orgId` [query] (string): Organization in which the device resides.

## Ejemplo de invocación
```bash
curl -X GET '/telephony/config/locations/<locationId>/devices/settings' \
  -H 'Authorization: Bearer <TOKEN>'
```

## Respuestas correctas
**200**: OK
- `customizations` (object) (**requerido**): Indicates the customization object of the device settings.
- `customEnabled` (boolean) (**requerido**): Indicates if customization is allowed at a location level. If `true`, customized at a location level. If `false`, not customized; uses customer-level configuration.
- `updateInProgress` (boolean) (**requerido**): Customer devices setting update status. If `true`, an update is in progress (no further changes are allowed). `If false`, no update in progress (changes are allowed).
- `deviceCount` (number) (**requerido**): Number of devices that will be updated.
- `lastUpdateTime` (number) (**requerido**): Indicates the last updated time.

### Ejemplo — respuesta 200
```json
{
  "customizations": {
    "ata": {
      "audioCodecPriority": {
        "selection": "REGIONAL",
        "primary": "G711a",
        "secondary": "G711u",
        "tertiary": "G729a"
      },
      "ataDtmfMode": "STRICT",
      "ataDtmfMethod": "AVT",
      "cdpEnabled": true,
      "lldpEnabled": true,
      "qosEnabled": true,
      "vlan": {
        "enabled": true,
        "value": 1
      },
      "webAccessEnabled": true,
      "nightlyResyncEnabled": true,
      "snmp": {
        "enabled": false,
        "trustedIP": "0.0.0.0/0.0.0.0",
        "getCommunity": "public",
        "setCommunity": "private",
        "snmpV3Enabled": false
      }
    },
    "mpp": {
      "pnacEnabled": true,
      "audioCodecPriority": {
        "selection": "CUSTOM",
        "primary": "OPUS",
        "secondary": "G722",
        "tertiary": "G711u"
      },
      "backlightTimer": "ONE_M",
      "background": {
        "customUrl": "",
        "image": "WEBEX_DARK_BLUE"
      },
      "displayNameFormat": "PERSON_FIRST_THEN_LAST_NAME",
      "cdpEnabled": false,
      "defaultLoggingLevel": "STANDARD",
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
        "1
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
The Webex Cloud Calling APIs enable comprehensive management of cloud-based calling services, including user provisioning, device assignment, call routing, feature configuration, and number management. These APIs facilitate integration with enterprise directories, automation of telephony workflows, and centralized management of global calling infrastructure. Use cases include automated onboarding, self-service portals, integration with CRM/ERP systems, and real-time monitoring of call quality and usage.

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs