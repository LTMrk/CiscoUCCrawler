---
doc_id: webex-cloud-calling-post-telephony-config-jobs-devices-calldevicesettings
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: POST
path: /telephony/config/jobs/devices/callDeviceSettings
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.586193+00:00
---

# POST /telephony/config/jobs/devices/callDeviceSettings

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `changeDeviceSettingsAcrossOrganizationOrLocationJob`

## Resumen
Change Device Settings Across Organization Or Location Job

## Descripción
Change device settings across organization or locations jobs.

Performs bulk and asynchronous processing for all types of device settings initiated by organization and system admins in a stateful persistent manner. This job will modify the requested device settings across all the devices. Whenever a location ID is specified in the request, it will modify the requested device settings only for the devices that are part of the provided location within an organization.

Returns a unique job ID which can then be utilized further to retrieve status and errors for the same.

Only one job per customer can be running at any given time within the same organization. An attempt to run multiple jobs at the same time will result in a 409 error response.

Running a job requires a full or read-only administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `orgId` [query] (string): Apply change device settings for all the devices under this organization.

## Cuerpo de la petición (application/json)
- `locationId` (string): Location within an organization where changes of device setings will be applied to all the devices within it.
- `locationCustomizationsEnabled` (boolean): Indicates if all the devices within this location will be customized with new requested customizations(if set to `true`) or will be overridden with the one at organization level (if set to `false` or any other value). This field has no effect when the job is being triggered at organization level.
- `customizations` (object):
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
    - `pnacEnabled` (boolean) **(requerido)**: Indicates whether the PNAC of MPP object is enabled or not.
    - `audioCodecPriority` (object) **(requerido)**:
      - `selection` (string) **(requerido)**: Indicates the selection of the Audio Codec Priority Object for an MPP object.
      - `primary` (string) **(requerido)**: Indicates the primary Audio Codec for an MPP object.
      - `secondary` (string) **(requerido)**: Indicates the secondary Audio Codec for an MPP object.
      - `tertiary` (string) **(requerido)**: Indicates the tertiary Audio Codec for an MPP object.
    - `backlightTimer` (string) **(requerido)**: * `ONE_MIN` - Set the phone's backlight to be on for one minute.  * `FIVE_MIN` - Set the phone's backlight to be on for five minutes.  * `THIRTY_MIN` - Set the phone's backlight to be on for thirty minutes.  * `ALWAYS_ON` - Keep the phone's backlight always on. Valores: ONE_MIN, FIVE_MIN, THIRTY_MIN, ALWAYS_ON.
    - `background` (object) **(requerido)**:
      - `image` (string): * `NONE` - Indicates that there will be no background image set for the devices.  * `DARK_BLUE` - Indicates that dark blue background image will be set for the devices.  * `CISCO_DARK_BLUE` - Indicates that Cisco themed dark blue background image will be set for the devices.  * `WEBEX_DARK_BLUE` - Indicates that Cisco Webex dark blue background image will be set for the devices.  * `CUSTOM_BACKGROUND` - Indicates that a custom background image will be set for the devices.  * `customUrl` - When this option is selected, a field 'Custom Background URL' needs to be added with the image url. URLs provided must link directly to an image file and be in HTTP, HTTPS, or filepath format. Valores: NONE, DARK_BLUE, CISCO_DARK_BLUE, WEBEX_DARK_BLUE, CUSTOM_BACKGROUND.
      - `customUrl` (string):
    - `displayNameFormat` (string): * `PERSON_NUMBER` - Indicates that devices will display the person's phone number, or if a person doesn't have a phone number, the location number will be displayed.  * `PERSON_FIRST_THEN_LAST_NAME` - Indicates that devices will display the name in first name then last name format.  * `PERSON_LAST_THEN_FIRST_NAME` - Indicates that devices will display the name in last name then first name format. Valores: PERSON_NUMBER, PERSON_FIRST_THEN_LAST_NAME, PERSON_LAST_THEN_FIRST_NAME.
    - `cdpEnabled` (boolean) **(requerido)**: Allows you to enable/disable CDP for local devices.
    - `defaultLoggingLevel` (string) **(requerido)**: * `STANDARD` - Enables standard logging.  * `DEBUGGING` - Enables detailed debugging logging. Valores: STANDARD, DEBUGGING.
    - `dndServicesEnabled` (boolean) **(requerido)**: Enable/disable Do-Not-Disturb capabilities for Multi-Platform Phones.
    - `acd` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: Indicates whether the ACD object is enabled.
      - `displayCallqueueAgentSoftkeys` (string) **(requerido)**:  Valores: FRONT_PAGE, LAST_PAGE.
    - `shortInterdigitTimer` (number) **(requerido)**: Indicates the short inter digit timer value.
    - `longInterdigitTimer` (number) **(requerido)**: Indicates the long inter digit timer value..
    - `lineKeyLabelFormat` (string) **(requerido)**: * `PERSON_EXTENSION` - This will display the person extension, or if a person doesn't have an extension, the person's first name will be displayed.  * `PERSON_FIRST_THEN_LAST_NAME` - Indicates that devices will display the name in first name then last name format.  * `PERSON_LAST_THEN_FIRST_NAME` - Indicates that devices will display the name in last name then first name format. Valores: PERSON_EXTENSION, PERSON_FIRST_THEN_LAST_NAME, PERSON_LAST_THEN_FIRST_NAME.
    - `lineKeyLEDPattern` (string) **(requerido)**:  Valores: DEFAULT, PRESET_1.
    - `lldpEnabled` (boolean) **(requerido)**: Enable/disable Link Layer Discovery Protocol for local devices.
    - `mppUserWebAccessEnabled` (boolean) **(requerido)**: Enable/disable user-level access to the web interface of Multi-Platform Phones.
    - `multicast` (array) **(requerido)**: Select up to 10 Multicast Group URLs (each with a unique Listening Port).
    - `enhancedMulticast` (object) **(requerido)**:
      - `xmlAppUrl` (string): Specify the URL for the XML application.
      - `multicastList` (array) **(requerido)**: Specify up to 10 multicast group URLs each with a unique listening port, an XML application URL, and a timeout.
        - `hostAndPort` (string) **(requerido)**: Specify the multicast group URL and listening port.
        - `hasXmlAppUrl` (boolean) **(requerido)**: Specify whether the multicast group URL has an XML application URL.
        - `xmlAppTimeout` (number): Specify the timeout for the XML application.
    - `offHookTimer` (number) **(requerido)**: Specify the amount of time (in seconds) that a phone can remain off-hook.
    - `phoneLanguage` (string) **(requerido)**: * `PERSON_LANGUAGE` - Indicates a person's announcement language. Valores: PERSON_LANGUAGE, ARABIC, BULGARIAN, CATALAN, CHINESE_SIMPLIFIED, CHINESE_TRADITIONAL, CROATIAN, CZECH, DANISH, DUTCH, ENGLISH_UNITED_STATES, ENGLISH_UNITED_KINGDOM, FINNISH, FRENCH_CANADA, FRENCH_FRANCE, GERMAN, GREEK, HEBREW, HUNGARIAN, ITALIAN, JAPANESE, KOREAN, NORWEGIAN, POLISH, PORTUGUESE_PORTUGAL, RUSSIAN, SPANISH_COLOMBIA, SPANISH_SPAIN, SLOVAK, SWEDISH, SLOVENIAN, TURKISH, UKRAINE.
    - `poeMode` (string) **(requerido)**: * `NORMAL` - Use normal power consumption.  * `MAXIMUM` - Use maximum power consumption. Valores: NORMAL, MAXIMUM.
    - `qosEnabled` (boolean) **(requerido)**: Allows you to enable/disable tagging of packets from the local device to the Webex Calling platform.
    - `screenTimeout` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: Indicates whether the Screen Time object is enabled.
      - `value` (number) **(requerido)**: Indicates the value of screen timeout.
    - `usbPortsEnabled` (boolean) **(requerido)**: Enable/disable the use of the USB ports on Multi-Platform phones.
    - `vlan` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: Indicates whether the VLAN object of an MPP is enabled.
      - `value` (number): Indicates the value of a VLAN object for an MPP object.
      - `pcPort` (number): Indicates the PC port value of a VLAN object for an MPP object.
    - `wifiNetwork` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: Indicates whether the wifi network is enabled.
      - `authenticationMethod` (string) **(requerido)**: * `NONE` - No authentication.  * `EAP_FAST` - Extensible Authentication Protocol-Flexible Authentication via Secure Tunneling. Requires username and password authentication.  * `PEAP_GTC` - Protected Extensible Authentication Protocol - Generic Token Card. Requires username and password authentication.  * `PEAP_MSCHAPV2` - Protected Extensible Authentication Protocol - Microsoft Challenge Handshake Authentication Protocol version 2. Requires username and password authentication.  * `PSK` - Pre-Shared Key. Requires shared passphrase for authentication.  * `WEP` - Wired Equivalent Privacy. Requires encryption key for authentication. Valores: NONE, EAP_FAST, PEAP_GTC, PEAP_MSCHAPV2, PSK, WEP.
      - `ssidName` (string) **(requerido)**: SSID name of the wifi network.
      - `userId` (string) **(requerido)**: User Id of the wifi network.
    - `callHistory` (string) **(requerido)**: * `WEBEX_UNIFIED_CALL_HISTORY` - Set call history to use the unified call history from all of the end user's devices.  * `LOCAL_CALL_HISTORY` - Set call history to use local device information only. Valores: WEBEX_UNIFIED_CALL_HISTORY, LOCAL_CALL_HISTORY.
    - `contacts` (string) **(requerido)**: * `XSI_DIRECTORY` - Set directory services to use standard XSI query method from the device.  * `WEBEX_DIRECTORY` - Set directory services to use the Webex Enterprise directory. Valores: XSI_DIRECTORY, WEBEX_DIRECTORY.
    - `webexMeetingsEnabled` (boolean) **(requerido)**: Enable/disable the availability of the webex meetings functionality from the phone.
    - `volumeSettings` (object) **(requerido)**:
      - `ringerVolume` (number) **(requerido)**: Specify a ringer volume level through a numeric value between 0 and 15.
      - `speakerVolume` (number) **(requerido)**: Specify a speaker volume level through a numeric value between 0 and 15.
      - `handsetVolume` (number) **(requerido)**: Specify a handset volume level through a numeric value between 0 and 15.
      - `headsetVolume` (number) **(requerido)**: Specify a headset volume level through a numeric value between 0 and 15.
      - `eHookEnabled` (boolean) **(requerido)**: Enable/disable the wireless headset hookswitch control.
      - `allowEndUserOverrideEnabled` (boolean) **(requerido)**: Enable/disable to preserve the existing values on the phone and not the values defined for the device settings.
    - `cfExpandedSoftKey` (string) **(requerido)**: * `ONLY_THE_CALL_FORWARD_ALL` - Set the default call forward expanded soft key behavior to single option.  * `ALL_CALL_FORWARDS` - Set the default call forward expanded soft key behavior to multiple menu option. Valores: ONLY_THE_CALL_FORWARD_ALL, ALL_CALL_FORWARDS.
    - `httpProxy` (object) **(requerido)**:
      - `mode` (string) **(requerido)**: Mode of the HTTP proxy. Valores: OFF, AUTO, MANUAL.
      - `autoDiscoveryEnabled` (boolean) **(requerido)**: Enable/disable auto discovery of the URL.
      - `host` (string) **(requerido)**: Specify the host URL if the HTTP mode is set to `MANUAL`.
      - `port` (string) **(requerido)**: Specify the port if the HTTP mode is set to `MANUAL`.
      - `packUrl` (string) **(requerido)**: Specify PAC URL if auto discovery is disabled.
      - `authSettingsEnabled` (boolean) **(requerido)**: Enable/disable authentication settings.
      - `username` (string) **(requerido)**: Specify a username if authentication settings are enabled.
      - `password` (string) **(requerido)**: Specify a password if authentication settings are enabled.
    - `bluetooth` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: Enable/disable Bluetooth.
      - `mode` (string) **(requerido)**: Select a Bluetooth mode. Valores: PHONE.
      - `PHONE` (string):
      - `HANDS_FREE` (string):
      - `BOTH` (string):
    - `passThroughPortEnabled` (boolean) **(requerido)**: Enable/disable the use of the PC passthrough ethernet port on supported phone models.
    - `userPasswordOverrideEnabled` (boolean) **(requerido)**: Enable/disable the ability for an end user to set a local password on the phone to restrict local access to the device.
    - `activeCallFocusEnabled` (boolean) **(requerido)**: Enable/disable the default screen behavior when inbound calls are received.
    - `peerFirmwareEnabled` (boolean) **(requerido)**: Enable/disable peer firmware sharing.
    - `noiseCancellation` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: Enable/disable the Noise Cancellation.
      - `allowEndUserOverrideEnabled` (boolean) **(requerido)**: Enable/disable to preserve the existing values on the phone and not the value defined for the device setting.
    - `voiceFeedbackAccessibilityEnabled` (boolean) **(requerido)**: Enable/disable visibility of the Accessibility Voice Feedback menu on the MPP device.
    - `dialAssistEnabled` (boolean) **(requerido)**: Enable/disable availability of dial assist feature on the phone.
    - `callsPerLine` (number) **(requerido)**: Specify the number of calls per unique line appearance on the phone.
    - `nightlyResyncEnabled` (boolean) **(requerido)**: Enable/disable automatic nightly configuration resync of the MPP device.
    - `missedCallNotificationEnabled` (boolean) **(requerido)**: Enable/disable the visual indication of missed calls.
    - `softKeyLayout` (object) **(requerido)**:
      - `softKeyMenu` (object) **(requerido)**:
        - `idleKeyList` (string) **(requerido)**: Specify the idle key list.
        - `offHookKeyList` (string) **(requerido)**: Specify the off hook key list.
        - `dialingInputKeyList` (string) **(requerido)**: Specify the dialing input key list.
        - `progressingKeyList` (string) **(requerido)**: Specify the progressing key list.
        - `connectedKeyList` (string) **(requerido)**: Specify the connected key list.
        - `connectedVideoKeyList` (string) **(requerido)**: Specify the connected video key list.
        - `startTransferKeyList` (string) **(requerido)**: Start the transfer key list.
        - `startConferenceKeyList` (string) **(requerido)**: Start the conference key list.
        - `conferencingKeyList` (string) **(requerido)**: Specify the conferencing key list.
        - `releasingKeyList` (string) **(requerido)**: Specify the releasing key list.
        - `holdKeyList` (string) **(requerido)**: Specify the hold key list.
        - `ringingKeyList` (string) **(requerido)**: Specify the ringing key list.
        - `sharedActiveKeyList` (string) **(requerido)**: Specify the shared active key list.
        - `sharedHeldKeyList` (string) **(requerido)**: Specify the shared held key list.
      - `psk` (object) **(requerido)**:
        - `psk1` (string) **(requerido)**: Specify PSK1.
        - `psk2` (string): Specify PSK2.
        - `psk3` (string): Specify PSK3.
        - `psk4` (string) **(requerido)**: Specify PSK4.
        - `psk5` (string): Specify PSK5.
        - `psk6` (string): Specify PSK6.
        - `psk7` (string): Specify PSK7.
        - `psk8` (string): Specify PSK8.
        - `psk9` (string): Specify PSK9.
        - `psk10` (string): Specify PSK10.
        - `psk11` (string): Specify PSK11.
        - `psk12` (string): Specify PSK12.
        - `psk13` (string): Specify PSK13.
        - `psk14` (string): Specify PSK14.
        - `psk15` (string): Specify PSK15.
        - `psk16` (string): Specify PSK16.
      - `softKeyMenuDefaults` (object) **(requerido)**:
        - `idleKeyList` (string) **(requerido)**: Specify the idle key list.
        - `offHookKeyList` (string) **(requerido)**: Specify the off hook key list.
        - `dialingInputKeyList` (string) **(requerido)**: Specify the dialing input key list.
        - `progressingKeyList` (string) **(requerido)**: Specify the progressing key list.
        - `connectedKeyList` (string) **(requerido)**: Specify the connected key list.
        - `connectedVideoKeyList` (string) **(requerido)**: Specify the connected video key list.
        - `startTransferKeyList` (string) **(requerido)**: Start the transfer key list.
        - `startConferenceKeyList` (string) **(requerido)**: Start the conference key list.
        - `conferencingKeyList` (string) **(requerido)**: Specify the conferencing key list.
        - `releasingKeyList` (string) **(requerido)**: Specify the releasing key list.
        - `holdKeyList` (string) **(requerido)**: Specify the hold key list.
        - `ringingKeyList` (string) **(requerido)**: Specify the ringing key list.
        - `sharedActiveKeyList` (string) **(requerido)**: Specify the shared active key list.
        - `sharedHeldKeyList` (string) **(requerido)**: Specify the shared held key list.
      - `pskDefaults` (object) **(requerido)**:
        - `psk1` (string) **(requerido)**: Specify PSK1.
        - `psk2` (string): Specify PSK2.
        - `psk3` (string): Specify PSK3.
        - `psk4` (string) **(requerido)**: Specify PSK4.
        - `psk5` (string): Specify PSK5.
        - `psk6` (string): Specify PSK6.
        - `psk7` (string): Specify PSK7.
        - `psk8` (string): Specify PSK8.
        - `psk9` (string): Specify PSK9.
        - `psk10` (string): Specify PSK10.
        - `psk11` (string): Specify PSK11.
        - `psk12` (string): Specify PSK12.
        - `psk13` (string): Specify PSK13.
        - `psk14` (string): Specify PSK14.
        - `psk15` (string): Specify PSK15.
        - `psk16` (string): Specify PSK16.
    - `backgroundImage8875` (string) **(requerido)**: * `CYAN_DARK` - Indicates that dark cyan background image will be set for the devices.  * `PURPLE_DARK` - Indicates the dark purple background image will be set for the devices.  * `BLUE_DARK` - Indicates the dark blue background image will be set for the devices.  * `VIOLET_DARK` - Indicates the dark violet background image will be set for the devices.  * `BLUE_LIGHT` - Indicates the light blue background image will be set for the devices.  * `VIOLET_LIGHT` - Indicates the light violet background image will be set for the devices. Valores: CYAN_DARK, PURPLE_DARK, BLUE_DARK, VIOLET_DARK, BLUE_LIGHT, VIOLET_LIGHT.
    - `backlightTimer68XX78XX` (string) **(requerido)**: * `ALWAYS_ON` - Keep the phone's backlight always on.  * `TEN_SEC` - Set the phone's backlight to be on for ten seconds.  * `TWENTY_SEC` - Set the phone's backlight to be on for twenty seconds.  * `THIRTY_SEC` - Set the phone's backlight to be on for thirty seconds.  * `OFF` - Keep the phone's backlight off. Valores: ALWAYS_ON, TEN_SEC, TWENTY_SEC, THIRTY_SEC, OFF.
    - `allowMonitorLinesEnabled` (boolean) **(requerido)**: Enable/disable monitoring for MPP non-primary device.
    - `iceEnabled` (boolean): Enable/disable SIP media streams to go directly between phones on the same local network.
  - `wifi` (object):
    - `audioCodecPriority` (object) **(requerido)**:
      - `selection` (string) **(requerido)**: * `REGIONAL` - Indicates the regional selection type for audio codec priority.  * `CUSTOM` - Indicates the custom selection type for audio codec priority. Valores: REGIONAL, CUSTOM.
      - `primary` (string) **(requerido)**: Indicates the primary Audio Codec for an WiFi object.
      - `secondary` (string) **(requerido)**: Indicates the secondary Audio Codec for an WiFi object.
      - `tertiary` (string) **(requerido)**: Indicates the tertiary Audio Codec for an WiFi object.
    - `ldap` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: Sets the values needed to enable use of the LDAP service on the phone.
      - `serverAddress` (string) **(requerido)**: Sets the values needed to enable use of the LDAP service on the phone.
      - `serverPort` (number) **(requerido)**: Sets the values needed to enable use of the LDAP service on the phone.
      - `commSecurityType` (string) **(requerido)**: * `NONE` - Sets the LDAP server security protocol to None.  * `SSL` - Sets the LDAP server security protocol to SSL.  * `STARTTLS` - Sets the LDAP server security protocol to STARTTLS. Valores: NONE, SSL, STARTTLS.
      - `bindDn` (string) **(requerido)**: Sets the values needed to enable use of the LDAP service on the phone.
      - `bindPw` (string) **(requerido)**: Sets the values needed to enable use of the LDAP service on the phone.
      - `baseDn` (string) **(requerido)**: Sets the values needed to enable use of the LDAP service on the phone.
      - `primaryEmailAttribute` (string) **(requerido)**: Sets the values needed to enable use of the LDAP service on the phone.
      - `alternateEmailAttribute` (string) **(requerido)**: Sets the values needed to enable use of the LDAP service on the phone.
    - `webAccess` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: Ability to enable or disable the web browser access for the 840/860.
      - `password` (string) **(requerido)**: Ability to set a Web Server Password.
    - `phoneSecurityPwd` (string) **(requerido)**: Set the local security password on an 840/860 WiFi phone.

### Ejemplo de petición
```json
{
  "locationId": "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2E4Mjg5NzIyLTFiODAtNDFiNy05Njc4LTBlNzdhZThjMTA5OA",
  "locationCustomizationsEnabled": true,
  "customizations": {
    "ata": {
      "audioCodecPriority": {
        "primary": "G711a",
        "secondary": "G711u",
        "tertiary": "G729a",
        "selection": "REGIONAL"
      },
      "ataDtmfMode": "NORMAL",
      "ataDtmfMethod": "AVT",
      "cdpEnabled": true,
      "lldpEnabled": true,
      "qosEnabled": true,
      "vlan": {
        "enabled": true,
        "value": 1
      }
    },
    "dect": {
      "audioCodecPriority": {
        "primary": "G729",
        "secondary": "G711u",
        "tertiary": "G711a",
        "selection": "REGIONAL"
      },
      "cdpEnabled": true,
      "lldpEnabled": false,
      "multicast": [],
      "qosEnabled": true,
      "vlan": {
        "enabled": false,
        "value": null
      }
    },
    "mpp": {
      "pnacEnabled": true,
      "audioCodecPriority": {
        "primary": "OPUS",
        "secondary": "G722",
        "tertiary": "G711u",
        "selection": "CUSTOM"
      },
      "backlightTimer": "FIVE_M",
      "background": {
        "customUrl": "",
        "image": "NONE"
      },
      "displayNameFormat": "PERSON_FIRST_THEN_LAST_NAME",
      "cdpEnabled": false,
      "dndServicesEnabled": true,
      "acd": {
        "enabled": false,
        "displayCallqueueAgentSoftkeys": "LAST_PAGE"
      },
      "shortInterdigitTimer": 14,
      "longInterdigitTimer": 16,
      "lineKeyLabelFormat": "PERSON_FIRST_THEN_LAST_NAME",
      "lineKeyLEDPattern": "DEFAULT",
      "lldpEnabled": false,
      "mppUserWebAccessEnabled": true,
      "multicast": [],
      "enhancedMulticast": {
        "xmlAppUrl": "http://127.0.0.1:8080/",
        "multicastList": [
          {
            "hostAndPort": "224.0.0.0:22",
            "hasXmlAppUrl": true,
            "xmlAppTimeout": 10
          }
        ]
      },
      "offHookTimer": 30,
      "phoneLanguage": "DANISH",
      "poeMode": "MAXIMUM",
      "qosEnabled": true,
      "screenTimeout": {
        "enabled": true,
        "value": 400
      },
      "usbPortsEnabled": true,
      "vlan": {
        "enabled": false,
        "value": 1,
        "pcPort": 1
      },
      "wifiNetwork": {
        "enabled": false,
        "authenticationMethod": "PSK",
        "ssidName": "test_wifi_network",
        "userId": "test"
      },
      "allowMonitorLinesEnabled": false,
      "iceEnabled": true,
      "cfExpandedSoftKey": "ONLY_THE_CALL_FORWARD_ALL"
    }
  }
}
```

## Respuestas
- **200**: OK
  - `name` (string) **(requerido)**: Job name.
  - `id` (string) **(requerido)**: Unique identifier of the job.
  - `jobType` (string) **(requerido)**: Job type.
  - `trackingId` (string) **(requerido)**: Unique identifier to track the flow of HTTP requests.
  - `sourceUserId` (string) **(requerido)**: Unique identifier to identify which user has run the job.
  - `sourceCustomerId` (string) **(requerido)**: Unique identifier of the organization that initiated the job.
  - `targetCustomerId` (string) **(requerido)**: Unique identifier of the organization for which the job was run.
  - `instanceId` (integer) **(requerido)**: Unique identifier to identify the instance of the job.
  - `jobExecutionStatus` (array): Displays the most recent step's execution status. Contains execution statuses of all the steps involved in the execution of the job.
    - `id` (integer) **(requerido)**: Unique identifier that identifies each instance of the job.
    - `lastUpdated` (string) **(requerido)**: Last updated time (in UTC format) post one of the step execution completion.
    - `statusMessage` (string) **(requerido)**: Displays status for overall steps that are part of the job.  * `STARTING` - Job has started.  * `STARTED` - Job is in progress.  * `COMPLETED` - Job has completed.  * `FAILED` - Job has failed.  * `UNKNOWN` - Job status is unknown.  * `ABANDONED` - Job has been abandoned (manually stopped). Valores: STARTING, STARTED, COMPLETED, FAILED, UNKNOWN, ABANDONED.
    - `exitCode` (string): Exit Code for a job.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors.  * `COMPLETED_WITH_PENDING_ORDERS` - Job has completed with pending number orders. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS, COMPLETED_WITH_PENDING_ORDERS.
    - `createdTime` (string) **(requerido)**: Job creation time in UTC format.
    - `timeElapsed` (string) **(requerido)**: Time lapsed since the job execution started.
  - `latestExecutionStatus` (string) **(requerido)**: Most recent status of the job at the time of invocation.  * `STARTING` - Job has started.  * `STARTED` - Job is in progress.  * `COMPLETED` - Job has completed.  * `FAILED` - Job has failed.  * `UNKNOWN` - Job status is unknown.  * `ABANDONED` - Job has been abandoned (manually stopped). Valores: STARTING, STARTED, COMPLETED, FAILED, UNKNOWN, ABANDONED.
  - `latestExecutionExitCode` (string): Most recent exit code of the job at the time of invocation.  * `UNKNOWN` - Job is in progress.  * `COMPLETED` - Job has completed successfully.  * `FAILED` - Job has failed.  * `STOPPED` - Job has been stopped.  * `COMPLETED_WITH_ERRORS` - Job has completed with errors.  * `COMPLETED_WITH_PENDING_ORDERS` - Job has completed with pending number orders. Valores: UNKNOWN, COMPLETED, FAILED, STOPPED, COMPLETED_WITH_ERRORS, COMPLETED_WITH_PENDING_ORDERS.
  - `operationType` (string) **(requerido)**: The operation type that was carried out.
  - `sourceLocationId` (string) **(requerido)**: Unique location identifier for which the job was run.
  - `targetLocationId` (string) **(requerido)**: Unique location identifier for which the numbers have been moved.
  - `counts` (object) **(requerido)**:
    - `totalMoves` (number) **(requerido)**: Total number of user moves requested.
    - `moved` (number) **(requerido)**: Total number of user moves completed successfully.
    - `failed` (number) **(requerido)**: Total number of user moves that were completed with failures.
    - `pending` (number) **(requerido)**: Total number of user moves that were pending with number orders.
    - `skipped` (number) **(requerido)**: Total number of user moves that were skipped.
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
