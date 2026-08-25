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
retrieved_at: 2026-08-25T10:28:32.397569+00:00
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
- `customizations` (object) (**requerido**):
  - `ata` (object):
    - `audioCodecPriority` (object) (**requerido**):
      - `selection` (string) (**requerido**): * `REGIONAL` - Indicates the regional selection type for audio codec priority.  * `CUSTOM` - Indicates the custom selection type for audio codec priority. Valores: REGIONAL, CUSTOM.
      - `primary` (string) (**requerido**): Indicates the primary Audio Codec.
      - `secondary` (string) (**requerido**): Indicates the secondary Audio Codec.
      - `tertiary` (string) (**requerido**): Indicates the tertiary Audio Codec.
    - `ataDtmfMode` (string) (**requerido**): * `STRICT` - A DTMF digit requires an extra hold time after detection and the DTMF level threshold is raised to -20 dBm.  * `NORMAL` - Normal threshold mode. Valores: STRICT, NORMAL.
    - `ataDtmfMethod` (string) (**requerido**): * `INBAND` - Sends DTMF by using the audio path.  * `AVT` - Audio video transport. Sends DTMF as AVT events.  * `AUTO` - Uses InBand or AVT based on the outcome of codec negotiation. Valores: INBAND, AVT, AUTO.
    - `cdpEnabled` (boolean) (**requerido**): Enable/disable Cisco Discovery Protocol for local devices.
    - `lldpEnabled` (boolean) (**requerido**): Enable/disable Link Layer Discovery Protocol for local devices.
    - `qosEnabled` (boolean) (**requerido**): Enable/disable quality of service tagging of packets from the local device to the Webex Calling platform.
    - `vlan` (object) (**requerido**):
      - `enabled` (boolean) (**requerido**): Denotes whether the VLAN object of an ATA is enabled.
      - `value` (number) (**requerido**): The value of the VLAN Object of an ATA object.
    - `webAccessEnabled` (boolean) (**requerido**): Enable/disable user level web access to the local device.
    - `nightlyResyncEnabled` (boolean) (**requerido**): Enable/disable the automatic nightly configuration resync of the MPP device.
    - `snmp` (object) (**requerido**):
      - `enabled` (boolean) (**requerido**): Denotes whether the Simple Network Management Protocol of an ATA is enabled.
      - `trustedIP` (string) (**requerido**): Trusted IPv4 address and subnet mask in this order: 0.0.0.0/0.0.0.0.
      - `getCommunity` (string) (**requerido**): Read-only community string that allows/denies access to other device's statistics. Default value is `public`.
      - `setCommunity` (string) (**requerido**): Read-write community string that protects the device against unauthorized changes. Must never be set to `public`.
      - `snmpV3Enabled` (boolean) (**requerido**): Denotes whether the SNMPv3 security is enabled.
  - `mpp` (object):
    - `pnacEnabled` (boolean) (**requerido**): Indicates whether the PNAC of MPP object is enabled or not.
    - `audioCodecPriority` (object) (**requerido**):
      - `selection` (string) (**requerido**): Indicates the selection of the Audio Codec Priority Object for an MPP object.
      - `primary` (string) (**requerido**): Indicates the primary Audio Codec for an MPP object.
      - `secondary` (string) (**requerido**): Indicates the secondary Audio Codec for an MPP object.
      - `tertiary` (string) (**requerido**): Indicates the tertiary Audio Codec for an MPP object.
    - `backlightTimer` (string) (**requerido**): * `ONE_MIN` - Set the phone's backlight to be on for one minute.  * `FIVE_MIN` - Set the phone's backlight to be on for five minutes.  * `THIRTY_MIN` - Set the phone's backlight to be on for thirty minutes.  * `ALWAYS_ON` - Keep the phone's backlight always on. Valores: ONE_MIN, FIVE_MIN, THIRTY_MIN, ALWAYS_ON.
    - `background` (object) (**requerido**):
      - `image` (string): * `NONE` - Indicates that there will be no background image set for the devices.  * `DARK_BLUE` - Indicates that dark blue background image will be set for the devices.  * `CISCO_DARK_BLUE` - Indicates that Cisco themed dark blue background image will be set for the devices.  * `WEBEX_DARK_BLUE` - Indicates that Cisco Webex dark blue background image will be set for the devices.  * `CUSTOM_BACKGROUND` - Indicates that a custom background image will be set for the devices.  * `customUrl` - When this option is selected, a field 'Custom Background URL' needs to be added with the image url. URLs provided must link directly to an image file and be in HTTP, HTTPS, or filepath format. Valores: NONE, DARK_BLUE, CISCO_DARK_BLUE, WEBEX_DARK_BLUE, CUSTOM_BACKGROUND.
      - `customUrl` (string):
    - `displayNameFormat` (string): * `PERSON_NUMBER` - Indicates that devices will display the person's phone number, or if a person doesn't have a phone number, the location number will be displayed.  * `PERSON_FIRST_THEN_LAST_NAME` - Indicates that devices will display the name in first name then last name format.  * `PERSON_LAST_THEN_FIRST_NAME` - Indicates that devices will display the name in last name then first name format. Valores: PERSON_NUMBER, PERSON_FIRST_THEN_LAST_NAME, PERSON_LAST_THEN_FIRST_NAME.
    - `cdpEnabled` (boolean) (**requerido**): Allows you to enable/disable CDP for local devices.
    - `defaultLoggingLevel` (string) (**requerido**): * `STANDARD` - Enables standard logging.  * `DEBUGGING` - Enables detailed debugging logging. Valores: STANDARD, DEBUGGING.
    - `dndServicesEnabled` (boolean) (**requerido**): Enable/disable Do-Not-Disturb capabilities for Multi-Platform Phones.
    - `acd` (object) (**requerido**):
      - `enabled` (boolean) (**requerido**): Indicates whether the ACD object is enabled.
      - `displayCallqueueAgentSoftkeys` (string) (**requerido**):  Valores: FRONT_PAGE, LAST_PAGE.
    - `shortInterdigitTimer` (number) (**requerido**): Indicates the short inter digit timer value.
    - `longInterdigitTimer` (number) (**requerido**): Indicates the long inter digit timer value..
    - `lineKeyLabelFormat` (string) (**requerido**): * `PERSON_EXTENSION` - This will display the person extension, or if a person doesn't have an extension, the person's first name will be displayed.  * `PERSON_FIRST_THEN_LAST_NAME` - Indicates that devices will display the name in first name then last name format.  * `PERSON_LAST_THEN_FIRST_NAME` - Indicates that devices will display the name in last name then first name format. Valores: PERSON_EXTENSION, PERSON_FIRST_THEN_LAST_NAME, PERSON_LAST_THEN_FIRST_NAME.
    - `lineKeyLEDPattern` (string) (**requerido**):  Valores: DEFAULT, PRESET_1.
    - `lldpEnabled` (boolean) (**requerido**): Enable/disable Link Layer Discovery Protocol for local devices.
    - `mppUserWebAccessEnabled` (boolean) (**requerido**): Enable/disable user-level access to the web interface of Multi-Platform Phones.
    - `multicast` (array) (**requerido**): Select up to 10 Multicast Group URLs (each with a unique Listening Port).
    - `enhancedMulticast` (object) (**requerido**):
      - `xmlAppUrl` (string): Specify the URL for the XML application.
      - `multicastList` (array) (**requerido**): Specify up to 10 multicast group URLs each with a unique listening port, an XML application URL, and a timeout.
        - `hostAndPort` (string) (**requerido**): Specify the multicast group URL and listening port.
        - `hasXmlAppUrl` (boolean) (**requerido**): Specify whether the multicast group URL has an XML application URL.
        - `xmlAppTimeout` (number): Specify the timeout for the XML application.
    - `offHookTimer` (number) (**requerido**): Specify the amount of time (in seconds) that a phone can remain off-hook.
    - `phoneLanguage` (string) (**requerido**): * `PERSON_LANGUAGE` - Indicates a person's announcement language. Valores: PERSON_LANGUAGE, ARABIC, BULGARIAN, CATALAN, CHINESE_SIMPLIFIED, CHINESE_TRADITIONAL, CROATIAN, CZECH, DANISH, DUTCH, ENGLISH_UNITED_STATES, ENGLISH_UNITED_KINGDOM, FINNISH, FRENCH_CANADA, FRENCH_FRANCE.
    - `poeMode` (string) (**requerido**): * `NORMAL` - Use normal power consumption.  * `MAXIMUM` - Use maximum power consumption. Valores: NORMAL, MAXIMUM.
    - `qosEnabled` (boolean) (**requerido**): Allows you to enable/disable tagging of packets from the local device to the Webex Calling platform.
    - `screenTimeout` (object) (**requerido**):
      - `enabled` (boolean) (**requerido**): Indicates whether the Screen Time object is enabled.

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