---
doc_id: webex-cloud-calling-get-telephony-config-devices-settings
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: GET
path: /telephony/config/devices/settings
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.584113+00:00
---

# GET /telephony/config/devices/settings

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `readDeviceOverrideSettingsForOrganization`

## Resumen
Read the device override settings for a organization

## Descripción
Get device override settings for an organization.

Retrieving this list requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_read`.

## Parámetros
- `orgId` [query] (string): List supported devices for an organization.

## Respuestas
- **200**: OK
  - `customizations` (object) **(requerido)**:
    - `ata` (object):
      - `audioCodecPriority` (object) **(requerido)**:
        - `selection` (string) **(requerido)**: * `REGIONAL` - Indicates the regional selection type for audio codec priority.  * `CUSTOM` - Indicates the custom selection type for audio codec priority. Valores: REGIONAL, CUSTOM.
        - `primary` (string) **(requerido)**: Indicates the primary Audio Codec.
        - `secondary` (string) **(requerido)**: Indicates the secondary Audio Codec.
        - `tertiary` (string) **(requerido)**: Indicates the tertiary Audio Codec.
      - `ataDtmfMode` (string) **(requerido)**: * `STRICT` - A DTMF digit requires an extra hold time after detection and the DTMF level threshold is raised to -20 dBm.  * `NORMAL` - Normal threshold mode. Valores: STRICT, NORMAL.
      - `ataDtmfMethod` (string) **(requerido)**: * `INBAND` - Sends DTMF by using the audio path.  * `AVT` - Audio video transport. Sends DTMF as AVT events.  * `AUTO` - Uses InBand or AVT based on the outcome of codec negotiation. Valores: INBAND, AVT, AUTO.
      - `cdpEnabled` (boolean) **(requerido)**: Enable/disable Cisco Discovery Protocol for local devices.
      - `lldpEnabled` (boolean) **(requerido)**: Enable/disable Link Layer Discovery Protocol for local devices.
      - `qosEnabled` (boolean) **(requerido)**: Enable/disable quality of service tagging of packets from the local device to the Webex Calling platform.
      - `vlan` (object) **(requerido)**:
        - `enabled` (boolean) **(requerido)**: Denotes whether the VLAN object of an ATA is enabled.
        - `value` (number) **(requerido)**: The value of the VLAN Object of an ATA object.
      - `webAccessEnabled` (boolean) **(requerido)**: Enable/disable user level web access to the local device.
      - `nightlyResyncEnabled` (boolean) **(requerido)**: Enable/disable the automatic nightly configuration resync of the MPP device.
      - `snmp` (object) **(requerido)**:
        - `enabled` (boolean) **(requerido)**: Denotes whether the Simple Network Management Protocol of an ATA is enabled.
        - `trustedIP` (string) **(requerido)**: Trusted IPv4 address and subnet mask in this order: 0.0.0.0/0.0.0.0.
        - `getCommunity` (string) **(requerido)**: Read-only community string that allows/denies access to other device's statistics. Default value is `public`.
        - `setCommunity` (string) **(requerido)**: Read-write community string that protects the device against unauthorized changes. Must never be set to `public`.
        - `snmpV3Enabled` (boolean) **(requerido)**: Denotes whether the SNMPv3 security is enabled.
    - `dect` (object):
      - `audioCodecPriority` (object) **(requerido)**:
        - `selection` (string) **(requerido)**: * `REGIONAL` - Indicates the regional selection type for audio codec priority.  * `CUSTOM` - Indicates the custom selection type for audio codec priority. Valores: REGIONAL, CUSTOM.
        - `primary` (string) **(requerido)**: Indicates the primary Audio Codec.
        - `secondary` (string) **(requerido)**: Indicates the secondary Audio Codec.
        - `tertiary` (string) **(requerido)**: Indicates the tertiary Audio Codec.
      - `cdpEnabled` (boolean) **(requerido)**: Enable/disable Cisco Discovery Protocol for local devices.
      - `dect6825HandsetEmergencyNumber` (string) **(requerido)**: Specify the destination number to be dialled from the DECT Handset top button when pressed.
      - `lldpEnabled` (boolean) **(requerido)**: Enable/disable Link Layer Discovery Protocol for local devices.
      - `multicast` (string) **(requerido)**: Specify up to 3 multicast group URLs each with a unique listening port.
      - `qosEnabled` (boolean) **(requerido)**: Enable/disable quality of service tagging of packets from the local device to the Webex Calling platform.
      - `vlan` (object) **(requerido)**:
        - `enabled` (boolean) **(requerido)**: Denotes whether the VLAN object of DECT is enabled.
        - `value` (number) **(requerido)**: Value of the VLAN Object of DECT.
      - `webAccessEnabled` (boolean) **(requerido)**: Enable/disable user level web access to the local device.
      - `nightlyResyncEnabled` (boolean) **(requerido)**: Enable/disable phone's default behavior regarding the nightly maintenance synchronization with the Webex Calling platform.
    - `mpp` (object):
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

---
> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.
> https://github.com/webex/webex-openapi-specs
