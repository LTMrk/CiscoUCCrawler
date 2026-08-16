---
doc_id: webex-cloud-calling-put-telephony-config-devices-deviceid-settings
source: webex-openapi-specs/public-spec/webex-cloud-calling.json
api: Webex Cloud Calling
method: PUT
path: /telephony/config/devices/{deviceId}/settings
license: CC-BY-4.0
retrieved_at: 2026-08-16T11:30:32.582560+00:00
---

# PUT /telephony/config/devices/{deviceId}/settings

**API:** Webex Cloud Calling
**Área:** Device Call Settings
**operationId:** `updateDeviceSettings`

## Resumen
Update device settings

## Descripción
Modify override settings for a device.

Device settings list all the applicable settings for an MPP and an ATA devices at the device level. Admins can also modify the settings. NOTE: DECT devices do not support settings at the device level.

Updating settings on the device requires a full administrator auth token with a scope of `spark-admin:telephony_config_write`.

## Parámetros
- `deviceId` [path] (string) **(requerido)**: Unique identifier for the device.
- `orgId` [query] (string): Organization in which the device resides..
- `deviceModel` [query] (string): The model type of the device. The corresponding device model display name sometimes called the product name, can also be used to specify the model.

## Cuerpo de la petición (application/json)
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
  - `mpp` (object):
    - `pnacEnabled` (boolean) **(requerido)**: Indicates whether the PNAC of MPP object is enabled or not.
    - `audioCodecPriority` (object) **(requerido)**:
      - `selection` (string) **(requerido)**: * `REGIONAL` - Indicates the regional selection type for audio codec priority.  * `CUSTOM` - Indicates the custom selection type for audio codec priority. Valores: REGIONAL, CUSTOM.
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
    - `usbPorts` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: New Control to Enable/Disable the side USB port.
      - `sideUsbEnabled` (boolean) **(requerido)**: Enable/disable use of the side USB port on the MPP device. Enabled by default.
      - `rearUsbEnabled` (boolean) **(requerido)**: Enable/disable use of the rear USB port on the MPP device.
    - `vlan` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: Indicates whether the VLAN object of an MPP is enabled.
      - `value` (number): Indicates the value of a VLAN object for an MPP object.
      - `pcPort` (number): Indicates the PC port value of a VLAN object for an MPP object.
    - `wifiNetwork` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: Indicates whether the wifi network is enabled.
      - `authenticationMethod` (string) **(requerido)**: * `NONE` - No authentication.  * `EAP_FAST` - Extensible Authentication Protocol-Flexible Authentication via Secure Tunneling. Requires username and password authentication.  * `PEAP_GTC` - Protected Extensible Authentication Protocol - Generic Token Card. Requires username and password authentication.  * `PEAP_MSCHAPV2` - Protected Extensible Authentication Protocol - Microsoft Challenge Handshake Authentication Protocol version 2. Requires username and password authentication.  * `PSK` - Pre-Shared Key. Requires shared passphrase for authentication.  * `WEP` - Wired Equivalent Privacy. Requires encryption key for authentication. Valores: NONE, EAP_FAST, PEAP_GTC, PEAP_MSCHAPV2, PSK, WEP.
      - `ssidName` (string) **(requerido)**: SSID name of the wifi network.
      - `userId` (string) **(requerido)**: User ID for the WiFi network.
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
      - `host` (string): Specify the host URL if the HTTP mode is set to `MANUAL`.
      - `port` (string): Specify the port if the HTTP mode is set to `MANUAL`.
      - `packUrl` (string): Specify PAC URL if auto discovery is disabled.
      - `authSettingsEnabled` (boolean): Enable/disable authentication settings.
      - `username` (string): Specify a username if authentication settings are enabled.
      - `password` (string): Specify a password if authentication settings are enabled.
    - `bluetooth` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: Enable/disable Bluetooth.
      - `mode` (string): Select a Bluetooth mode. Valores: PHONE, HANDS_FREE, BOTH.
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
      - `selection` (string) **(requerido)**: Indicates the selection of the Audio Codec Priority Object for an WiFi object.
      - `primary` (string) **(requerido)**: Indicates the primary Audio Codec for an WiFi object.
      - `secondary` (string) **(requerido)**: Indicates the secondary Audio Codec for an WiFi object.
      - `tertiary` (string) **(requerido)**: Indicates the tertiary Audio Codec for an WiFi object.
    - `ldap` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: Sets the values needed to enable use of the LDAP service on the phone.
      - `serverAddress` (string): Sets the values needed to enable use of the LDAP service on the phone.
      - `serverPort` (number): Sets the values needed to enable use of the LDAP service on the phone.
      - `commSecurityType` (string): * `NONE` - Sets the LDAP server security protocol to None.  * `SSL` - Sets the LDAP server security protocol to SSL.  * `STARTTLS` - Sets the LDAP server security protocol to STARTTLS. Valores: NONE, SSL, STARTTLS.
      - `bindDn` (string): Sets the values needed to enable use of the LDAP service on the phone.
      - `bindPw` (string): Sets the values needed to enable use of the LDAP service on the phone.
      - `baseDn` (string): Sets the values needed to enable use of the LDAP service on the phone.
      - `primaryEmailAttribute` (string): Sets the values needed to enable use of the LDAP service on the phone.
      - `alternateEmailAttribute` (string): Sets the values needed to enable use of the LDAP service on the phone.
    - `webAccess` (object) **(requerido)**:
      - `enabled` (boolean) **(requerido)**: Ability to enable or disable the web browser access for the 840/860.
      - `password` (string) **(requerido)**: Ability to set a Web Server Password.
    - `phoneSecurityPwd` (string) **(requerido)**: Set the local security password on an 840/860 WiFi phone.
- `customEnabled` (boolean) **(requerido)**: Indicates if customization is allowed at a device level. If true, customized at a device level. If false, not customized; uses customer-level configuration.

### Ejemplo de petición
```json
{
  "customizations": {
    "mpp": {
      "pnacEnabled": true,
      "audioCodecPriority": {
        "primary": "OPUS",
        "secondary": "G722",
        "tertiary": "G711u",
        "selection": "CUSTOM"
      },
      "backlightTimerOldModel": "THIRTY_SECONDS",
      "background": {
        "customUrl": "",
        "image": "WEBEX_DARK_BLUE"
      },
      "displayNameFormat": "PERSON_FIRST_THEN_LAST_NAME",
      "cdpEnabled": false,
      "defaultLoggingLevel": "DEBUGGING",
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
        "192.86.108.226:2223"
      ],
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
      "phoneLanguage": "RUSSIAN",
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
        "ssidName": "my_wifi_network",
        "userId": "test-user"
      },
      "backlightTimer": "FIVE_MIN",
      "callHistory": "LOCAL_CALL_HISTORY",
      "contacts": "WEBEX_DIRECTORY",
      "webexMeetingsEnabled": false,
      "usbPorts": {
        "enabled": true,
        "sideUsbEnabled": true,
        "rearUsbEnabled": true
      },
      "volumeSettings": {
        "ringerVolume": 9,
        "speakerVolume": 9,
        "handsetVolume": 9,
        "headsetVolume": 9,
        "eHookEnabled": false,
        "allowEndUserOverrideEnabled": false
      },
      "httpProxy": {
        "mode": "OFF",
        "autoDiscoveryEnabled": false,
        "host": "localhost",
        "port": "8080",
        "packUrl": "www.webex.com",
        "authSettingsEnabled": true,
        "username": "usernamecpi"
      },
      "bluetooth": {
        "enabled": true,
        "mode": "PHONE"
      },
      "passThroughPortEnabled": true,
      "userPasswordOverrideEnabled": true,
      "activeCallFocusEnabled": true,
      "peerFirmwareEnabled": true,
      "noiseCancellation": {
        "enabled": false,
        "allowEndUserOverrideEnabled": false
      },
      "dialAssistEnabled": true,
      "callsPerLine": 8,
      "nightlyResyncEnabled": true,
      "missedCallNotificationEnabled": false,
      "softKeyLayout": {
        "softKeyMenu": {
          "idleKeyList": "abcdefgh",
          "offHookKeyList": "nmhsdjs",
          "dialingInputKeyList": "djsks",
          "progressingKeyList": "sdsd",
          "connectedKeyList": "ssdds",
          "connectedVideoKeyList": "hold;endcall;xfer;conf;xferLx;confLx;bxfer;phold;redial;dir;park;crdstart;crdstop;crdpause;crdresume",
          "startTransferKeyList": "abcdef",
          "startConferenceKeyList": "abcdef",
          "conferencingKeyList": "abcdef",
          "releasingKeyList": "abcdef",
          "holdKeyList": "abcdef",
          "ringingKeyList": "abcdef",
          "sharedActiveKeyList": "abcdef",
          "sharedHeldKeyList": "abcdef"
        },
        "psk": {
          "psk1": "abcdef",
          "psk2": "abcdef",
          "psk3": "abcdef",
          "psk4": "abcdef",
          "psk5": "abcdef",
          "psk6": "abcdef",
          "psk7": "abcdef",
          "psk8": "abcdef",
          "psk9": "abcdef",
          "psk10": "abcdef",
          "psk11": "abcdef",
          "psk12": "abcdef",
          "psk13": "abcdef",
          "psk14": "abcdef",
          "psk15": "abcdef",
          "psk16": "veeresh"
        },
        "softKeyMenuDefaults": {
          "idleKeyList": "guestin|;guestout|;acd_login|;acd_logout|;astate|;redial|;newcall|;cfwd|;recents|;dnd|;unpark|;psk1|;gpickup|;pickup|;dir|4;miss|5;selfview|;messages",
          "offHookKeyList": "endcall|1;redial|2;dir|3;lcr|4;unpark|5;pickup|6;gpickup|7",
          "dialingInputKeyList": "dial|1;cancel|2;delchar|3;left|5;right|6",
          "progressingKeyList": "endcall|2",
          "connectedKeyList": "hold;endcall;xfer;conf;xferLx;confLx;bxfer;phold;redial;dir;park;crdstart;crdstop;crdpause;crdresume",
          "connectedVideoKeyList": "hold;endcall;xfer;conf;xferLx;confLx;bxfer;phold;redial;dir;park;crdstart;crdstop;crdpause;crdresume",
          "startTransferKeyList": "endcall|2;xfer|3",
          "startConferenceKeyList": "endcall|2;conf|3",
          "conferencingKeyList": "endcall;join;crdstart;crdstop;crdpause;crdresume",
          "releasingKeyList": "endcall|2",
          "holdKeyList": "resume|1;endcall|2;newcall|3;redial|4;dir|5",
          "ringingKeyList": "answer|1;ignore|2",
          "sharedActiveKeyList": "newcall|1;psk1|2;dir|3;back|4",
          "sharedHeldKeyList": "resume|1;dir|4"
        },
        "pskDefaults": {
          "psk1": "fnc=sd;ext=*11;nme=Call Pull"
        }
      },
      "backgroundImage8875": "BLUE_LIGHT",
      "backlightTimer68XX78XX": "THIRTY_SEC",
      "allowMonitorLinesEnabled": false,
      "voiceFeedbackAccessibilityEnabled": false,
      "iceEnabled": true,
      "cfExpandedSoftKey": "ONLY_THE_CALL_FORWARD_ALL"
    },
    "wifi": {
      "audioCodecPriority": {
        "selection": "REGIONAL",
        "primary": "OPUS",
        "secondary": "G722",
        "tertiary": "G711u"
      },
      "ldap": {},
      "webAccess": {
        "enabled": false
      }
    }
  },
  "customEnabled": true,
  "updateInProgress": true,
  "deviceCount": 9,
  "lastUpdateTime": 1659624763665
}
```

## Respuestas
- **204**: No Content
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
