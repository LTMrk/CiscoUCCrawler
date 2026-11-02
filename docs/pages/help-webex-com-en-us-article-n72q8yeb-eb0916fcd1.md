---
doc_id: help-webex-com-en-us-article-n72q8yeb-eb0916fcd1
source_url: https://help.webex.com/en-us/article/n72q8yeb
retrieved_at: 2026-11-02T13:06:56.474602+00:00
---

## Configure phones at organization level

Configure settings for all phones deployed within your organization to improve efficiency and reduce administrative overhead.

The configuration follows a hierarchical structure; therefore, if you configure a setting for an individual device or at the location level, it takes precedence over the same setting configured at the organization level.

From the customer view in Control Hub , go to Devices and select Settings .

Go to the Configuration Defaults tab and select Open org-wide defaults .

Search for an existing configuration or add a new one.

- To change an existing configuration, enter the parameter name in the search bar and open the configuration.

- To add a configuration, select Add configurations . Search for the configuration by product name or by parameter name and open it.

See the supported phone parameters in Parameters for phone settings in Control Hub .

Change the settings.

Click Next after you finish the configurations.

Review your change and click Apply changes .

## Configure phones at location level

You can configure your phones based on a physical location, allowing for flexible adjustments that won’t affect settings in other areas of the organization.

The configuration follows a hierarchical structure; therefore, if you configure a setting for an individual device, it takes precedence over the same setting configured at the location level.

From the customer view in Control Hub , go to Devices and select Settings .

Go to the Configuration Defaults tab.

If the desired location is available in the location list, select the Edit icon on it to open the configuration. Otherwise, select Set defaults on location and search for the location.

Search for the configuration by product name or by parameter name and open it.

See the supported phone parameters in Parameters for phone settings in Control Hub .

Change the settings.

Select Next after you finish the configurations.

Review your change and select Apply changes .

## Configure settings for multiple phones

You can configure settings for multiple phones at once to save time.

From the customer view in Control Hub , go to Devices , and then select the phones that you want to configure.

Click Edit in the top right of the device list.

Click All configurations .

All the configurations that are applicable to the selected devices are displayed.

Modify the configurations that you want to apply to the selected devices.

Expand a configuration to view its supported devices. Certain configurations allow you to customize values by device type.

Click Next .

Review your changes and click Apply .

The results show the successfully applied settings and unsupported configuration items.

Click Close to close the page.

## Configure settings for an individual phone

The configuration follows a hierarchical structure; therefore, if you configure a setting for an individual device, it takes precedence over the same setting configured at the location or organization level.

From the customer view in Control Hub , go to Devices , and then select your phone.

Select All configurations .

Set the desired parameters in the respective sections. For more information about these parameters, see Parameters for phone settings in Control Hub .

Select Next .

Review your changes and select Apply .

Select Close to close the page.

## Configure phones with a configuration template

A configuration template is a collection of custom settings for devices or a location.
        Administrators can create and use configuration templates to apply collections of settings
        to groups of devices. These templates help to simplify the management of devices in your
        organization.

### Create a configuration template for phones

You can add configurations for either a specific device type or multiple device types. When the template is applied, the system only implements compatible settings and skips those that don't apply.

From the customer view in Control Hub , go to Devices > Templates .

Click Create template .

Enter the unique template name and optionally provide a description for the template.

Select the configurations to add to your template.

By default, the configuration list displays all available settings for all device types. You can search for specific configurations.

- To search for applicable configurations for your device, select your device model in the Filter by device type drop-down list.

- To search for a specific configuration, enter the parameter name in the search bar.

See the supported phone parameters in Parameters for phone settings in Control Hub .

Change the configuration values.

Expand a configuration to view its supported devices. Certain settings allow you to customize values by device type.

Continue adding more configurations to the template.

To go back to the configuration list, use the breadcrumb on the page.

When finished, click Next and review your configurations.

You can edit or remove configurations as needed.

Click Create to complete the template.

What to do next

Apply the template to devices.

### Apply a configuration template to devices

You can apply a template to either a group of devices or an individual device.

Before you begin

You have a configuration template that is created for your devices.

From the customer view in Control Hub , go to Devices .

Select one or more devices by ticking the check box on each device entry.

Click Edit in the upper right of the list.

Click Configuration templates in the Configurations section.

Select the template in the drop-down list.

The configurations included in the template display.

Click Next and review the configurations.

Only the supported configurations will be applied to the selected devices.

Click Apply .

The results show the successfully applied settings and unsupported configuration items.

### Apply a configuration template to an individual device

Before you begin

You have a configuration template that is created for your device.

From the customer view in Control Hub , go to Devices .

Search for your device and open the device details.

Click Configuration templates in the Configurations section.

Select the template in the drop-down list.

The configurations included in the template display.

Click Next and review the configurations.

Only the supported configurations will be applied to the selected device.

Click Apply .

The results show the successfully applied settings and unsupported configuration items.

## Parameters for phone settings in Control Hub

This section includes a diversity of parameters available under All Configurations on Control Hub, catering to a wide range of needs and functionalities.

Parameter

Default and options

Description

Maximum Lines on Phone with KEM

(For 9800 Series only)

Default: 4

Options: 4, 8

This parameter is available only when a KEM(s) is connected to the phone.

For more information about KEM settings, see Cisco Desk Phone 9800 Key Expansion Module .

If you configure SCEP on the phone web page before the phone's onboarding process, the configuration will be kept and synchronized to Control Hub after the onboarding.

Default: Empty

Specifies the Common Name (CN) used as the identity for the phone that requests the Custom Device Certificate (CDC). The CN is used for Certificate Signing Request (CSR) in the Simple Certificate Enrollment Protocol (SCEP) process.

This parameter also supports macro variables, see Macro variables supported in XML URLs for details.

Default: Empty

Specifies an SHA256 or SHA1 fingerprint of the Root CA for validation during the SCEP process.

Default: Empty

Country Name

Default: Empty

String of 0 to 2 characters.

Default: Empty

Specifies the organization's state or province for the CSR Subject Name.

String of 0 to 64 characters.

Locality Name

Default: Empty

Specifies the locality name for the certificate subject for the CSR Subject Name.

String of 0 to 64 characters.

Organization Name

Default: Empty

Specifies the organization name for the CSR Subject Name.

String of 0 to 64 characters.

Organizational Unit

Default: Empty

Specifies the organizational unit names for the Certificate Signing Request (CSR) subject name. Phone will add up to 5 "/OU=" parameters to the CSR Subject Name.

Each entry is a string array of 0 to 64 characters separated by a comma, with a maximum length of 512 characters. Up to 5 units can be specified.

Reuse Pwd For Renewal

Default: No

Options: Yes, No

Specifies whether to allow reusing the challenge password for validation on certificate renewal.

When set to Yes , the phone stores the SCEP enrollment challenge password (in TAMS) and reuses it in the certificate renewal request (needed by SCEP servers such as EJBCA that require challenge-password validation on renewal).

When set to No , the provided challenge password is used only for initial enrollment. The phone uses the existing certificate for renewal.

SAN DNS

Default: Empty

Specifies the Domain Name Server (DNS) parameters for the Certificate Signing Request (CSR) Subject Alternative Name (SAN). Phone will add up to five DNS parameters to the CSR SAN.

Each entry is a string array of 0 to 64 characters separated by a comma, with a maximum length of 512 characters. Up to five DNS parameters can be specified.

SAN IP

Default: Empty

You can add maximum up to 5 entries. Each entry supports up to 64 characters, separated by commas. Maximum length of 512 characters is supported.

Each entry is a string array of 0 to 64 characters separated by a comma, with a maximum length of 512 characters. Up to five IP parameters can be specified.

Default: Empty

Specifies the Email parameters for the Certificate Signing Request (CSR) Subject Alternative Name (SAN). Phone will add up to five Email parameters to the CSR SAN.

Each entry is a string array of 0 to 64 characters separated by a comma, with a maximum length of 512 characters. Up to five Email parameters can be specified.

Default: Empty

Specifies the URI parameters for the Certificate Signing Request (CSR) Subject Alternative Name (SAN). Phone will add up to five URI parameters to the CSR SAN.

Each entry is a string array of 0 to 64 characters separated by a comma, with a maximum length of 512 characters. Up to five URI parameters can be specified.

Missed Call Notification

Default: Yes

Options: Yes, No

Enables or disables visual notifications for missed calls on the line.

Ringtone

Default: 1

Options: No Ring, 1- 15, Custom 1-10

Specifies a ring tone for the line. If No Ring is selected, the phone doesn't ring for incoming calls on that line.

See the ringtone list for the mapping between the available options and their corresponding ringtone names.

For more information about ringtones, see Configure ringtones for 9800 Series and 8875 phones .

Action Button

(For 9800 Series only)

See Configure the Action button for 9800 for details.

Call History

Default: Phone

Options: Phone, Webex

Sets call history to either use the local history or the Webex unified call history from all of the end user's devices. This setting currently only applies to user devices and doesn't apply to workspace devices.

Enable Directory Search For Offhook Dial

Default: No

Options: Yes, No

Display Name

Line Key Label

Line Key Secondary Label

See Configure line key labels on Control Hub for details.

Help Desk

(For 9800 Series only)

See Configure Help Desk for 9800 Series for details.

Always Use Multiline Mode

(For 9841, 9851, and 9861)

Default: Disabled

Options: Disabled, Enabled

Enables or disables the phone to always use multi-line layout. When enabled, the phone always displays the multie-line interface, even if only a single line is configured. This ensures a consistent user experience, regardless of how many lines the phone has.

Call Appearances Per Line

Default: 2

Options: 1 - 10

Sets the maximum number of calls allowed on a line.

Opens the menu item list, where you can customize the Settings menu by hiding items that you don't want users to access. By default, all menu items are visible to phone users.

The availability of menu items may vary by phone model. If all child items are hidden, the parent menu is also hidden. As a result, the index number of the remaining menu items will adjust automatically.

Group Paging Script[n]

Default: Empty

Specifies the multicast paging scripts.

See Group paging script syntax for details.

Office Hours

For the details, see Configure Office Hours for 9800/8875 .

Peer Firmware Sharing

Default: Yes

Options: Yes, No

Enables or disables the Peer Firmware Sharing (PFS) feature. The PFS feature adds support for image upgrade optimization for the phones. When enabled on a root phone, PFS designates the phone to make a request for an image file. This establishes a transfer hierarchy and transfers the firmware image file from the root phone, down to the other phones in the hierarchy.

Programmable Softkeys

See Configure the Programmable Softkeys for 9800/8875 for details.

For more information about ringtones, see Configure ringtones for 9800 Series and 8875 phones .

Default: Yes

Options: Yes, No

Default: No

Options: Yes, No

Default: Yes

Options: Yes, No

Enables or disables Webex Personal Contacts directory service for the phone. When enabled, users on the phone can access and search for the contacts stored in the Webex Personal Contacts directory.

XML Application Service Name

Default : Empty

Defines the name of the XML application. The name displays on the phone as a web application.

XML Application Service URL

Default : Empty

Enters the URL where the XML application is located.

Macro variables are supported in XML URLs. For the valid macro variables, see Macro variables supported in XML URLs .

Default: No

Options: Yes, No

Default: 10

Options: 0 - 65535

Default: 3

Options: 0 - 65535

Default: English-US

For all supported languages, see Change language for your phone .

SIP

ICE

Default: No

Options: Yes, No

Controls whether to allow SIP Media streams to go directly between phones on the same local network.

RegStartRandomDelay

User Preferred Offhook Timer

Default: Empty

Options: 0 - 30

This timer starts when the phone goes off hook. If no digits are dialed within the specified number of seconds, the timer expires and the null entry is evaluated. Unless you have a special dial plan string to allow a null entry, the call is rejected.

Software

Upgrade Channel

Default: Stable

Options: Stable, Stable_Delay, Preview

Sets the channel for the phone to get firmware updates.

Bluetooth Enabled

(For 8875, 9861, and 9871 only)

Options: Yes, No

When enabled, phone users can connect their Bluetooth headsets to the phone.

Disable Speakerphone

Options: Yes, No

When enabled, phone users can change the audio path to headset or handset to use lines, speed dials, and softkeys for calling features.

You can configure the feature on the location or device level. The configurations on the location level will overwrite the existing configurations of the feature during the phone's onoarding process.

If you configure the HTTP proxy on the phone UI or phone web page before the phone's onboarding process, the configuration will be kept and synchronized to the Control Hub after the onboarding.

If you set the Proxy Mode to Auto and Web Proxy Auto Discovery to No , you must configure this parameter.

Options: Yes, No

If you set the parameter to Yes , you must configure Username .

The parameter configuration takes effect when Proxy Mode is set to Manual .

The scheme ( http:// or https:// ) is not required.

If you set the Proxy Mode to Manual , you must configure this parameter.

Options: Auto, Manual, Off

Auto—The phone automatically retrieves a Proxy Auto-Configuration (PAC) file to select a proxy server. In this mode, you can determine whether to use Web Proxy Auto Discovery (WPAD) protocol to retrieve a PAC file or manually enter a valid URL of the PAC file.

Off—You disable the HTTP proxy feature on the phone.

If you set the Proxy Mode to Manual , you must configure this parameter.

If Proxy Mode is set to Manual and Proxy Authentication is set to Yes , you must configure the parameter.

Options: Yes, No

WPAD protocol uses DHCP or DNS, or both network protocols to locate a Proxy Auto Configuration (PAC) file automatically. PAC file is used to select a proxy server for a given URL. This file can be hosted locally or on a network.

- The parameter configuration takes effect when Proxy Mode is set to Auto .

- If you set the parameter to No , you must specify a PAC URL.

System > IEEE802.1X

If you configure the 802.1X authentication on the phone UI or phone web page before the phone's onboarding process, the configuration will be kept and synchronized to Control Hub after the onboarding.

IEEE802.1X

Default: No

Options: Yes, No

Enables or disables Port Based Network Access Control for devices.

Setting this option incorrectly may cause devices to become disconnected from the network and require a local factory reset of the device to bring it back online.

IEEE802.1X Certificate Select

Default: Manufacturing installed

Options: Manufacturing installed, Custom installed

Sets which certificate (MIC or Custom) is used for the 802.1X authentication.

IEEE802.1X User ID

Default: Empty

Customizes the User ID for the 802.1X authentication in the wired network.

This parameter also supports macro variables, see Macro variables supported in XML URLs for details.

- Ensure that IEEE802.1X Certificate Select is set to Custom Installed . Otherwise, the Common Name in MIC/SUDI will always be used as the identity for 802.1X.

- For wired 802.1X, this parameter takes precedence over the Common Name (in Certificate > SCEP Configuration ). If both are configured, User ID will be the identity for wired 802.1X.

System > Optional Network Configuration

Debug Level

Default: NOTICE

Options: EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFO, DEBUG

Sets the logging level for troubleshooting.

The debugging level may affect the performance of the phone and it’s advisable to use it during troubleshooting.

Passthrough Port

Default: Yes

Options: Yes, No

Enables or disables the PC port on the phone. When enabled, the phone can share the network connection with the device that connects to the PC port.

Use Config TOS

Default: No

Options: Yes, No

Controls whether the phone uses the Time of Service (TOS) configurations.

System > Security

Default: Enabled

Options: Disabled, Enabled

Online Certificate Status Protocol (OCSP) helps prevent connections that use revoked certificates during the TLS handshake. With OCSP stapling enforcement enabled, the phone requests and validates a stapled OCSP response. The phone rejects the connection if the response is invalid or reports that the certificate is revoked. It rejects a missing response or a valid OCSP response with an UNKNOWN status only when the server certificate requires OCSP stapling (that is, has the must-staple extension). Regular certificate validation still applies.

Disable Back USB

(For 8875, 9851, 9861, and 9871)

Default: No

Options: Yes, No

Enables or disables the USB-C port located at the back of the phone. When disabled, the port doesn't work when you connect a headset as audio channel or for charging.

Disable Side USB

Default: No

Options: Yes, No

Enables or disables the USB-A port located on the right side of the phone. When disabled, the port doesn't work when you connect a headset as audio channel or for charging.

CDP

Default: Yes

Options: Yes, No

Enables or disables Cisco Discovery Protocol (CDP) for local devices.

When enabled, the phone discovers and advertises information about directly connected Cisco devices on a local area network (LAN).

Setting this option incorrectly may cause devices to become disconnected from the network and require a local factory reset of the device to bring it back online.

LLDP

Default: Yes

Options: Yes, No

Enables or disables Link Layer Discovery Protocol (LLDP) for the phone.

When enabled, the phone discovers and advertises information about directly connected network devices on a local area network (LAN).

Setting this option incorrectly may cause devices to become disconnected from the network and require a local factory reset of the device to bring it back online.

PC Port VLAN ID

Default: 1

Options: 0 - 4095

Enter a value of the VLAN ID that is used to tag communications from the PC port on the phone.

The phone tags all the untagged frames coming from the PC (it does not tag any frames with an existing tag).

VLAN ID

Default: 1

Options: 0 - 4095

Enter a VLAN ID for the phone when you use a VLAN without CDP (VLAN enabled and CDP disabled).

Only voice packets are tagged with the VLAN ID. Don't use the 1 value for the VLAN ID. If VLAN ID is 1, you cannot tag voice packets with the VLAN ID.

Web Access

Default: Yes

Options: Yes, No

Enables or disables access to the phone’s web interface and remote
                  management using xAPI.

When set to Yes , users and administrators can access the phone's web interface using the its IP address. Authorized administrators can also use xAPIs to remotely manage the phone.

Contact Cisco Technical Assistance Center (TAC) to request or create xAPI administrator credentials. To check the xAPI admin account status, go to Info > Status > Phone Status in the phone's web interface.

For information about the supported xAPIs and the related documentation, see https://phoneos.cisco.com .

WiFi Enabled

(For 8875, 9861, and 9871 only)

Options: Yes, No

When enabled, the phone can connect to the network through Wi-Fi.

Connection string

(For 9861 and 9871 only)

Abbreviated Dial 2-9

(For 9861, 9871, and 8875 only)

Options: Enabled, Disabled

When enabled, it protects users' hearing from sudden loud sounds and the incoming audio options are hidden from the phone's Setting menu.

When enabled, this setting overrides the Incoming Audio setting.

Bluetooth Volume

(For 8875, 9861, and 9871 only)

Default: 10

Options: 0 - 15

Handset Volume

Default: 9

Options: 0 - 15

Headset Volume

Default: 9

Options: 0 - 15

Ringer Volume

Default: 9

Options: 0 - 15

Speaker Volume

Default: 9

Options: 0 - 15

Auto Collapse Into Line Key

(For 9800 Series only)

Default: No

Options: Yes, No

Enables or disables the inline call label/session feature. When enabled, a call window (such as, incoming call, single call, all calls list) will be minimized to an inline call label/session. The users can view the current call session information through the inline call label. Because the call window is minimized, the status of other lines and BLF/SD features are visible (not blocked by the full call window) for the users.

This feature is available only on Cisco Desk Phone 9841, 9851, and 9861 with multiple lines.

Supported device types

(For 9861, 9871, and 8875 only)

Default: Optimize for voice

Options: Optimize for voice, Original

Enables or disables the Incoming Audio feature on 8875, 9861, or 9871. The users on the phone can enable this setting through:

- 9861: Settings > User perferences > Audio > Smart audio > Incoming audio

- 9871 and 8875: Settings > Audio > Smart audio > Incoming audio

When enabled, the incoming audio is optimized.

Microphone Audio

(For 9800 Series only)

Default: Noise removal

Options: Original, Noise removal, Optimize for my voice

Enables or disables the Noise Removal feature. There're three options available:

- Original —Turns off the Noise Removal feature

- Noise removal —Removes all background noise

- Optimize for my voice —Removes all background noise and background speech

Appearance

Custom Wallpaper

Logo Enable

Logo URL

Display Brightness

(For 9851, 9861, 9871, and 8875 only)

Default: 12

Options: 2-15

Sets the display brightness. The users on the phone can change the settings with:

- 9851 and 9861: the left and right navigation key or the "<" and ">" softkeys

- 9871 and 8875: the slider on the screen directly

Screen Brightness

(For 9841 only)

Default: 3

Options: 1-4

Sets the screen brightness. The users on the phone can change the settings with the left and right navigation key or the "<" and ">" softkeys on the phone.

DND Setting

Default: Yes

Options: Yes, No

When enabled, the users on the phone can turn DND on or off.

Default: month/day

Options: month/day, day/month

(For 9800 Series only)

Default: Top LED

Front Arc LED

Both

Sets the LED alert type for the phones of a same group. If the parameter is set to Both , for an incoming call, both the front arc LED and the top LED of the phones that are in the same call pickup group flashes.

This parameter is completely unrelated to the notification type in the group. Even if the notification type in the group is set to Audio only , the LED still blinks.

Default: Disabled

Options: Enabled, Disabled

Turns on or off LED indicators for missed calls. This parameter controls the Top 360 LED indicator on 9800 Series and the handset LED on 8875.

When disabled, no LEDs light up for missed calls.

Default: 12hr

Options: 12hr, 24hr

Default: No

Options; Yes, No

Default: No

Options; Yes, No

Default: Normal

Options: Slowest, Slower, Normal, Faster, Fastest

Default: Normal

Options: Lowest, Low, Normal, High, Highest

## References

### Ringtone list

The following table is the mapping between the ringtone names and the available options for
        the Ringtone setting at All configurations > Lines > Line[n] Call Feature Settings .

### Paging script syntax

Enter a string to configure the phone to listen for and initiate multicast paging. You can add a phone to up to 10 paging groups. Enter the script in this format:

pggrp=<multicast-address>:<port>;<name=group_name>;<num=multicast_number>; <listen=boolean_value>;<pri=priority_level>;<codec=codec_name>;

Example script :

pggrp=224.168.168.168:34560;name=Group_1;num=800;listen=yes;pri=1;

pggrp=<multicast-address>:<port>;<name=group_name>;<num=multicast_number>; <listen=boolean_value>;<pri=priority_level>;<codec=codec_name>;<xmlapp=boolean_value>;<timeout=seconds>

Example script :

pggrp=224.168.168.168:34560;name=Group_1;num=800;listen=yes;pri=1;xmlap- p=yes;timeout=3600;

Make sure that you set the same multicast IP address and port for all the phones within a paging group. Otherwise, the phones can't receive paging.

- Paging group name (name)—Optionally enter the name of the paging group. The name helps you identify the paging group the phone is in when you have multiple paging groups.

- Multicast number (num)—Specify the number for the phone to listen for multicast paging and initiate a multicast paging session. Assign the same multicast number to all the phones within the group. The number must comply to the dial plan specified for the line to initiate a multicast.

- Listen status (listen)—Specify whether the phone listens for paging from this group. Set this parameter to yes to make the phone listen for the paging. Otherwise, set it to no , or don't include this parameter in the script.

0: Paging takes precedent over phone call. When the phone is on an active call, an incoming paging places the active call on hold. The call resumes when the paging ends.

1 : When the phone receives an incoming paging on an active call, the user hears the mix of the paging and the call.

2 : The user is alerted with the paging tone when receiving an incoming paging on an active line. The incoming paging isn't answered unless the active call is put on hold or ends.

3 : The phone ignores the incoming paging without any alert when the phone is on an active call.

- Audio codec (codec)—Optionally specify the audio codec for the multicast paging to use. The supported codecs are G711a, G711u, G722, and G729. If you don't specify the codec or don't include the codec parameter in the script, the phone uses G711u codec.

Make sure that the parameter XML Application Service URL in XML services is configured, see Macro variables supported in XML URLs for details.

In the XML URL, the macro MCASTADDR must be configured to distinguish it from the normal multicast paging. For example, http(s)://<url>?mcast=$MCASTADDR

Typically, the XML application ends after the timeout is reached, in regardless of the paging call. If the paging call is still active, only the XML application ends.

A new paging closes the XML application of the last paging, if the XML application is not closed when the last paging ended.

### Macro variables supported in XML URLs

You can use macro variables in XML URLs. The following macro variables are supported:

User ID—UID1, UID2 to UIDn

Display name—DISPLAYNAME1, DISPLAYNAME2 to DISPLAYNAMEn

Auth ID—AUTHID1, AUTHID2 to AUTHIDn

Proxy—PROXY1, PROXY2 to PROXYn

MAC Address using lowercase hex digits—MA

Product Name—PN

Product Series Number—PSN

Serial Number—SERIAL_NUMBER

$SA through $SD are recognized as arguments to the optional resync URL
                    qualifier, --key.

SWVER

Software version string. For example,

PHONEOS.3-2-1-0104-37

HWVER

Hardware version string. For example, 2.0.1

PRVST

Provisioning State (a numeric string):

-1 = explicit resync request

0 = power-up resync

1 = periodic resync

2 = resync failed, retry attempt

UPGST

Upgrade State (a numeric string):

1 = first upgrade attempt

2 = upgrade failed, retry attempt

UPGERR

Result message (ERR) of previous upgrade attempt; for example http_get failed.

PRVTMR

Seconds since last resync attempt.

UPGTMR

Seconds since last upgrade attempt.

REGTMR1

Seconds since Line 1 lost registration with SIP server.

REGTMR2

Seconds since Line 2 lost registration with SIP server.

UPGCOND

Legacy macro name.

SCHEME

File access scheme, one of TFTP, HTTP, or HTTPS, as obtained after parsing resync or upgrade URL.

SERV

Request target server host name, as obtained after parsing resync or upgrade URL.

SERVIP

Request target server IP address, as obtained after parsing resync or upgrade URL, possibly following DNS lookup.

PORT

Request target UDP/TCP port, as obtained after parsing resync or upgrade URL.

PATH

Request target file path, as obtained after parsing resync or upgrade URL.

ERR

Result message of resync or upgrade attempt. Only useful in generating result syslog messages. The value is preserved in the UPGERR variable in the case of upgrade attempts.

UIDn

The contents of the Line n UserID configuration parameter.

If unit is customized, value=1, otherwise 0.

Customization status is viewable on Web UI Info page.

Phone number of first connected, ringing, or inbound call. If there are multiple calls, the data associated with the first call found is provided.

| 1 | From the customer view in Control Hub , go to Devices and select Settings . |
|---|---|
| 2 | Go to the Configuration Defaults tab and select Open org-wide defaults . |
| 3 | Search for an existing configuration or add a new one. To change an existing configuration, enter the parameter name in the search bar and open the configuration. To add a configuration, select Add configurations . Search for the configuration by product name or by parameter name and open it. See the supported phone parameters in Parameters for phone settings in Control Hub . |
| 4 | Change the settings. |
| 5 | Click Next after you finish the configurations. |
| 6 | Review your change and click Apply changes . |

| 1 | From the customer view in Control Hub , go to Devices and select Settings . |
|---|---|
| 2 | Go to the Configuration Defaults tab. |
| 3 | If the desired location is available in the location list, select the Edit icon on it to open the configuration. Otherwise, select Set defaults on location and search for the location. |
| 4 | Search for the configuration by product name or by parameter name and open it. See the supported phone parameters in Parameters for phone settings in Control Hub . |
| 5 | Change the settings. |
| 6 | Select Next after you finish the configurations. |
| 7 | Review your change and select Apply changes . |

| 1 | From the customer view in Control Hub , go to Devices , and then select the phones that you want to configure. |
|---|---|
| 2 | Click Edit in the top right of the device list. |
| 3 | Click All configurations . All the configurations that are applicable to the selected devices are displayed. |
| 4 | Modify the configurations that you want to apply to the selected devices. Expand a configuration to view its supported devices. Certain configurations allow you to customize values by device type. |
| 5 | Click Next . |
| 6 | Review your changes and click Apply . The results show the successfully applied settings and unsupported configuration items. |
| 7 | Click Close to close the page. |

| 1 | From the customer view in Control Hub , go to Devices , and then select your phone. |
|---|---|
| 2 | Select All configurations . |
| 3 | Set the desired parameters in the respective sections. For more information about these parameters, see Parameters for phone settings in Control Hub . |
| 4 | Select Next . |
| 5 | Review your changes and select Apply . |
| 6 | Select Close to close the page. |

| 1 | From the customer view in Control Hub , go to Devices > Templates . |
|---|---|
| 2 | Click Create template . |
| 3 | Enter the unique template name and optionally provide a description for the template. |
| 4 | Select the configurations to add to your template. By default, the configuration list displays all available settings for all device types. You can search for specific configurations. To search for applicable configurations for your device, select your device model in the Filter by device type drop-down list. To search for a specific configuration, enter the parameter name in the search bar. See the supported phone parameters in Parameters for phone settings in Control Hub . |
| 5 | Change the configuration values. Expand a configuration to view its supported devices. Certain settings allow you to customize values by device type. |
| 6 | Continue adding more configurations to the template. To go back to the configuration list, use the breadcrumb on the page. |
| 7 | When finished, click Next and review your configurations. You can edit or remove configurations as needed. |
| 8 | Click Create to complete the template. |

| 1 | From the customer view in Control Hub , go to Devices . |
|---|---|
| 2 | Select one or more devices by ticking the check box on each device entry. |
| 3 | Click Edit in the upper right of the list. |
| 4 | Click Configuration templates in the Configurations section. |
| 5 | Select the template in the drop-down list. The configurations included in the template display. |
| 6 | Click Next and review the configurations. Only the supported configurations will be applied to the selected devices. |
| 7 | Click Apply . The results show the successfully applied settings and unsupported configuration items. |

| 1 | From the customer view in Control Hub , go to Devices . |
|---|---|
| 2 | Search for your device and open the device details. |
| 3 | Click Configuration templates in the Configurations section. |
| 4 | Select the template in the drop-down list. The configurations included in the template display. |
| 5 | Click Next and review the configurations. Only the supported configurations will be applied to the selected device. |
| 6 | Click Apply . The results show the successfully applied settings and unsupported configuration items. |

| Parameter | Default and options | Description |
|---|---|---|
| Att Console |
| Maximum Lines on Phone with KEM (For 9800 Series only) | Default: 4 Options: 4, 8 | Specifies whether to retain 4 or 8 lines on the phone and move the additional lines to the attached key expansion module (KEM). This parameter is available only when a KEM(s) is connected to the phone. For more information about KEM settings, see Cisco Desk Phone 9800 Key Expansion Module . |
| Certificate > SCEP Configuration If you configure SCEP on the phone web page before the phone's onboarding process, the configuration will be kept and synchronized to Control Hub after the onboarding. |
| Common Name | Default: Empty | Specifies the Common Name (CN) used as the identity for the phone that requests the Custom Device Certificate (CDC). The CN is used for Certificate Signing Request (CSR) in the Simple Certificate Enrollment Protocol (SCEP) process. This parameter also supports macro variables, see Macro variables supported in XML URLs for details. |
| Root CA Fingerprint | Default: Empty | Specifies an SHA256 or SHA1 fingerprint of the Root CA for validation during the SCEP process. |
| Server | Default: Empty | Specifies the an SCEP server address (URL or IP address), which is used to install CDC on the phone. Note that the HTTPS scheme isn't supported. |
| Country Name | Default: Empty | Specifies the organization's country for the CSR Subject Name. String of 0 to 2 characters. |
| State or Province Name | Default: Empty | Specifies the organization's state or province for the CSR Subject Name. String of 0 to 64 characters. |
| Locality Name | Default: Empty | Specifies the locality name for the certificate subject for the CSR Subject Name. String of 0 to 64 characters. |
| Organization Name | Default: Empty | Specifies the organization name for the CSR Subject Name. String of 0 to 64 characters. |
| Organizational Unit | Default: Empty | Specifies the organizational unit names for the Certificate Signing Request (CSR) subject name. Phone will add up to 5 "/OU=" parameters to the CSR Subject Name. Each entry is a string array of 0 to 64 characters separated by a comma, with a maximum length of 512 characters. Up to 5 units can be specified. |
| Reuse Pwd For Renewal | Default: No Options: Yes, No | Specifies whether to allow reusing the challenge password for validation on certificate renewal. When set to Yes , the phone stores the SCEP enrollment challenge password (in TAMS) and reuses it in the certificate renewal request (needed by SCEP servers such as EJBCA that require challenge-password validation on renewal). When set to No , the provided challenge password is used only for initial enrollment. The phone uses the existing certificate for renewal. |
| SAN DNS | Default: Empty | Specifies the Domain Name Server (DNS) parameters for the Certificate Signing Request (CSR) Subject Alternative Name (SAN). Phone will add up to five DNS parameters to the CSR SAN. Each entry is a string array of 0 to 64 characters separated by a comma, with a maximum length of 512 characters. Up to five DNS parameters can be specified. |
| SAN IP | Default: Empty | You can add maximum up to 5 entries. Each entry supports up to 64 characters, separated by commas. Maximum length of 512 characters is supported. Each entry is a string array of 0 to 64 characters separated by a comma, with a maximum length of 512 characters. Up to five IP parameters can be specified. |
| SAN Email | Default: Empty | Specifies the Email parameters for the Certificate Signing Request (CSR) Subject Alternative Name (SAN). Phone will add up to five Email parameters to the CSR SAN. Each entry is a string array of 0 to 64 characters separated by a comma, with a maximum length of 512 characters. Up to five Email parameters can be specified. |
| SAN URI | Default: Empty | Specifies the URI parameters for the Certificate Signing Request (CSR) Subject Alternative Name (SAN). Phone will add up to five URI parameters to the CSR SAN. Each entry is a string array of 0 to 64 characters separated by a comma, with a maximum length of 512 characters. Up to five URI parameters can be specified. |
| Lines > Line[n] Call Feature Settings |
| Missed Call Notification | Default: Yes Options: Yes, No | Enables or disables visual notifications for missed calls on the line. |
| Ringtone | Default: 1 Options: No Ring, 1- 15, Custom 1-10 | Specifies a ring tone for the line. If No Ring is selected, the phone doesn't ring for incoming calls on that line. See the ringtone list for the mapping between the available options and their corresponding ringtone names. For more information about ringtones, see Configure ringtones for 9800 Series and 8875 phones . |
| Phone > Action Button |
| Action Button (For 9800 Series only) |  | See Configure the Action button for 9800 for details. |
| Phone > Call History |
| Call History | Default: Phone Options: Phone, Webex | Sets call history to either use the local history or the Webex unified call history from all of the end user's devices. This setting currently only applies to user devices and doesn't apply to workspace devices. |
| Phone > Directory Service |
| Enable Directory Search For Offhook Dial | Default: No Options: Yes, No | Enables or disables contact searching in directories during a call to transfer, park, or start a conference. |
| Phone > Display Name |
| Display Name Line Key Label Line Key Secondary Label |  | See Configure line key labels on Control Hub for details. |
| Phone > Help Desk |
| Help Desk (For 9800 Series only) |  | See Configure Help Desk for 9800 Series for details. |
| Phone > Line Key Settings |
| Always Use Multiline Mode (For 9841, 9851, and 9861) | Default: Disabled Options: Disabled, Enabled | Enables or disables the phone to always use multi-line layout. When enabled, the phone always displays the multie-line interface, even if only a single line is configured. This ensures a consistent user experience, regardless of how many lines the phone has. |
| Call Appearances Per Line | Default: 2 Options: 1 - 10 | Sets the maximum number of calls allowed on a line. |
| Phone > Menu Customization Opens the menu item list, where you can customize the Settings menu by hiding items that you don't want users to access. By default, all menu items are visible to phone users. The availability of menu items may vary by phone model. If all child items are hidden, the parent menu is also hidden. As a result, the index number of the remaining menu items will adjust automatically. |
| Phone > Multicast Paging Group |
| Group Paging Script[n] | Default: Empty | Specifies the multicast paging scripts. See Group paging script syntax for details. |
| Phone > Office Hours |
| Office Hours |  | For the details, see Configure Office Hours for 9800/8875 . |
| Phone > Peer Firmware Sharing |
| Peer Firmware Sharing | Default: Yes Options: Yes, No | Enables or disables the Peer Firmware Sharing (PFS) feature. The PFS feature adds support for image upgrade optimization for the phones. When enabled on a root phone, PFS designates the phone to make a request for an image file. This establishes a transfer hierarchy and transfers the firmware image file from the root phone, down to the other phones in the hierarchy. |
| Phone > Programmable Softkeys |
| Programmable Softkeys |  | See Configure the Programmable Softkeys for 9800/8875 for details. |
| Phone > Ringtone |
| Custom Ringtone URL [1] to [10] | Default: Empty | Specifies the location of the custom ringtone file. When a valid URL is specified, the custom ringtone becomes available in the ringtone list on the phone, allowing users to assign it to a line. For more information about ringtones, see Configure ringtones for 9800 Series and 8875 phones . |
| Phone > Webex |
| Calendar Enable | Default: Yes Options: Yes, No | Enables or disables Webex calendar. When enabled, the phone loads Webex calendar to enable phone users to view the calendar events. |
| Directory Enable | Default: No Options: Yes, No | Enables or disables Webex directory service for the phone. When enabled, users on the phone can access and search for the contacts stored in the directory. |
| Directory Name | Default: Empty | Sets the display name for the directory. |
| Personal Contact Enable | Default: Yes Options: Yes, No | Enables or disables Webex Personal Contacts directory service for the phone. When enabled, users on the phone can access and search for the contacts stored in the Webex Personal Contacts directory. |
| Phone > XML Service |
| XML Application Service Name | Default : Empty | Defines the name of the XML application. The name displays on the phone as a web application. |
| XML Application Service URL | Default : Empty | Enters the URL where the XML application is located. Macro variables are supported in XML URLs. For the valid macro variables, see Macro variables supported in XML URLs . |
| Phone > XSI Phone Service |
| Directory Enable | Default: No Options: Yes, No | Enables or disables BroadSoft XSI directory service for the phone. When enabled, users on the phone can access and search for the contacts stored in the directory. |
| Directory Name | Default: Empty | Sets the display name for the directory. |
| Regional > Control Timer Values |
| Interdigit Long Timer | Default: 10 Options: 0 - 65535 | Defines the amount of time that the phone will wait when no digit patterns match before the phone dials the number. A smaller time value causes unmatched dialed digits to be dialed quickly. |
| Interdigit Short Timer | Default: 3 Options: 0 - 65535 | Defines the amount of time that the phone waits for the user to enter a digit. A smaller timer value requires digits to be dialed quickly. |
| Regional > Phone Language |
| Phone Language | Default: English-US | Sets the display language for the phone. This value will override the default value derived from its provisioned Location. For all supported languages, see Change language for your phone . |
| SIP |
| ICE | Default: No Options: Yes, No | Controls whether to allow SIP Media streams to go directly between phones on the same local network. |
| RegStartRandomDelay |  |  |
| User Preferred Offhook Timer | Default: Empty Options: 0 - 30 | This timer starts when the phone goes off hook. If no digits are dialed within the specified number of seconds, the timer expires and the null entry is evaluated. Unless you have a special dial plan string to allow a null entry, the call is rejected. |
| Software |
| Upgrade Channel | Default: Stable Options: Stable, Stable_Delay, Preview | Sets the channel for the phone to get firmware updates. |
| System > Bluetooth Enabled |
| Bluetooth Enabled (For 8875, 9861, and 9871 only) | Default: No Options: Yes, No | Enables or disables the Bluetooth ® function on the phone. When enabled, phone users can connect their Bluetooth headsets to the phone. |
| System > Disable Speakerphone |
| Disable Speakerphone | Default: No Options: Yes, No | Enables or disables the speakerphone functionality on the phone. When enabled, phone users can change the audio path to headset or handset to use lines, speed dials, and softkeys for calling features. |
| System > HTTP Proxy Settings You can configure the feature on the location or device level. The configurations on the location level will overwrite the existing configurations of the feature during the phone's onoarding process. If you configure the HTTP proxy on the phone UI or phone web page before the phone's onboarding process, the configuration will be kept and synchronized to the Control Hub after the onboarding. |
| PAC URL | Default: Empty | Specifies a PAC file URL. TFTP, HTTP, and HTTPS are supported. If you set the Proxy Mode to Auto and Web Proxy Auto Discovery to No , you must configure this parameter. |
| Proxy Authentication | Default: No Options: Yes, No | Determines whether the user needs to provide the username that the proxy server requires. This parameter is configured according to the actual behavior of the proxy server. If you set the parameter to Yes , you must configure Username . The parameter configuration takes effect when Proxy Mode is set to Manual . |
| Proxy Host | Default: Empty | IP address or hostname of the proxy host server for the phone to access. The scheme ( http:// or https:// ) is not required. If you set the Proxy Mode to Manual , you must configure this parameter. |
| Proxy Mode | Default: Off Options: Auto, Manual, Off | Specifies the HTTP proxy mode that the phone uses, or disables the HTTP proxy feature. Auto—The phone automatically retrieves a Proxy Auto-Configuration (PAC) file to select a proxy server. In this mode, you can determine whether to use Web Proxy Auto Discovery (WPAD) protocol to retrieve a PAC file or manually enter a valid URL of the PAC file. Manual—You must manually specify a server (hostname or IP address) and a port of a proxy server. Off—You disable the HTTP proxy feature on the phone. |
| Proxy Port | Default: 3128 | Specifies a port number of the proxy host server. If you set the Proxy Mode to Manual , you must configure this parameter. |
| Username | Default: Empty | Specifies a username for a credential user on the proxy server. If Proxy Mode is set to Manual and Proxy Authentication is set to Yes , you must configure the parameter. |
| Web Proxy Auto Discovery | Default: Yes Options: Yes, No | Determines whether the phone uses the Web Proxy Auto Discovery (WPAD) protocol to retrieve a PAC file. WPAD protocol uses DHCP or DNS, or both network protocols to locate a Proxy Auto Configuration (PAC) file automatically. PAC file is used to select a proxy server for a given URL. This file can be hosted locally or on a network. The parameter configuration takes effect when Proxy Mode is set to Auto . If you set the parameter to No , you must specify a PAC URL. |
| System > IEEE802.1X If you configure the 802.1X authentication on the phone UI or phone web page before the phone's onboarding process, the configuration will be kept and synchronized to Control Hub after the onboarding. |
| IEEE802.1X | Default: No Options: Yes, No | Enables or disables Port Based Network Access Control for devices. Setting this option incorrectly may cause devices to become disconnected from the network and require a local factory reset of the device to bring it back online. |
| IEEE802.1X Certificate Select | Default: Manufacturing installed Options: Manufacturing installed, Custom installed | Sets which certificate (MIC or Custom) is used for the 802.1X authentication. |
| IEEE802.1X User ID | Default: Empty | Customizes the User ID for the 802.1X authentication in the wired network. This parameter also supports macro variables, see Macro variables supported in XML URLs for details. Ensure that IEEE802.1X Certificate Select is set to Custom Installed . Otherwise, the Common Name in MIC/SUDI will always be used as the identity for 802.1X. For wired 802.1X, this parameter takes precedence over the Common Name (in Certificate > SCEP Configuration ). If both are configured, User ID will be the identity for wired 802.1X. |
| System > Optional Network Configuration |
| Debug Level | Default: NOTICE Options: EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFO, DEBUG | Sets the logging level for troubleshooting. The debugging level may affect the performance of the phone and it’s advisable to use it during troubleshooting. |
| Passthrough Port | Default: Yes Options: Yes, No | Enables or disables the PC port on the phone. When enabled, the phone can share the network connection with the device that connects to the PC port. |
| Use Config TOS | Default: No Options: Yes, No | Controls whether the phone uses the Time of Service (TOS) configurations. |
| System > Security |
| OCSP Stapling Enforcement | Default: Enabled Options: Disabled, Enabled | Online Certificate Status Protocol (OCSP) helps prevent connections that use revoked certificates during the TLS handshake. With OCSP stapling enforcement enabled, the phone requests and validates a stapled OCSP response. The phone rejects the connection if the response is invalid or reports that the certificate is revoked. It rejects a missing response or a valid OCSP response with an UNKNOWN status only when the server certificate requires OCSP stapling (that is, has the must-staple extension). Regular certificate validation still applies. |
| System > USB Settings |
| Disable Back USB (For 8875, 9851, 9861, and 9871) | Default: No Options: Yes, No | Enables or disables the USB-C port located at the back of the phone. When disabled, the port doesn't work when you connect a headset as audio channel or for charging. |
| Disable Side USB | Default: No Options: Yes, No | Enables or disables the USB-A port located on the right side of the phone. When disabled, the port doesn't work when you connect a headset as audio channel or for charging. |
| System > VLAN Settings |
| CDP | Default: Yes Options: Yes, No | Enables or disables Cisco Discovery Protocol (CDP) for local devices. When enabled, the phone discovers and advertises information about directly connected Cisco devices on a local area network (LAN). Setting this option incorrectly may cause devices to become disconnected from the network and require a local factory reset of the device to bring it back online. |
| LLDP | Default: Yes Options: Yes, No | Enables or disables Link Layer Discovery Protocol (LLDP) for the phone. When enabled, the phone discovers and advertises information about directly connected network devices on a local area network (LAN). Setting this option incorrectly may cause devices to become disconnected from the network and require a local factory reset of the device to bring it back online. |
| PC Port VLAN ID | Default: 1 Options: 0 - 4095 | Enter a value of the VLAN ID that is used to tag communications from the PC port on the phone. The phone tags all the untagged frames coming from the PC (it does not tag any frames with an existing tag). |
| VLAN ID | Default: 1 Options: 0 - 4095 | Enter a VLAN ID for the phone when you use a VLAN without CDP (VLAN enabled and CDP disabled). Only voice packets are tagged with the VLAN ID. Don't use the 1 value for the VLAN ID. If VLAN ID is 1, you cannot tag voice packets with the VLAN ID. |
| System > Web Access |
| Web Access | Default: Yes Options: Yes, No | Enables or disables access to the phone’s web interface and remote
                  management using xAPI. When set to Yes , users and administrators can access the phone's web interface using the its IP address. Authorized administrators can also use xAPIs to remotely manage the phone. Contact Cisco Technical Assistance Center (TAC) to request or create xAPI administrator credentials. To check the xAPI admin account status, go to Info > Status > Phone Status in the phone's web interface. For information about the supported xAPIs and the related documentation, see https://phoneos.cisco.com . |
| System > Wifi Enabled |
| WiFi Enabled (For 8875, 9861, and 9871 only) | Default: Yes Options: Yes, No | Enables or disables the Wi-Fi feature on Cisco Desk Phone 8875, 9861, or 9871. When enabled, the phone can connect to the network through Wi-Fi. |
| Thousand Eyes |
| Connection string (For 9861 and 9871 only) | Default: Empty | Available only when ThousandEyes is activated at organization level. For more details, see ThousandEyes integration for 9800 . |
| User > Abbreviated Dial |
| Abbreviated Dial 2-9 | Default: Empty | Specifies the name and number for the abbreviated dial entry. |
| User > Acoustic Shock Protection |
| (For 9861, 9871, and 8875 only) | Default: Disabled Options: Enabled, Disabled | Enables or disables the acoustic shock protection on Cisco Desk Phone 8875, 9861, or 9871. When enabled, it protects users' hearing from sudden loud sounds and the incoming audio options are hidden from the phone's Setting menu. When enabled, this setting overrides the Incoming Audio setting. |
| User > Audio Volume |
| Bluetooth Volume (For 8875, 9861, and 9871 only) | Default: 10 Options: 0 - 15 | Sets the Bluetooth headset volume. The users on the phone can change the settings with the Volume key on the phone or the Volume button on the headset. |
| Handset Volume | Default: 9 Options: 0 - 15 | Sets the handset volume. The users on the phone can change the settings with the Volume key on the phone. |
| Headset Volume | Default: 9 Options: 0 - 15 | Sets the headset volume. The users on the phone can change the settings with the Volume key on the phone or on their headset. |
| Ringer Volume | Default: 9 Options: 0 - 15 | Sets the ringer volume. The users on the phone can change the settings with the Volume key on the phone. |
| Speaker Volume | Default: 9 Options: 0 - 15 | Sets the speaker volume. The users on the phone can change the settings with the Volume key on the phone. |
| Call Preferences > Auto Collapse Into Line Key |
| Auto Collapse Into Line Key (For 9800 Series only) | Default: No Options: Yes, No | Enables or disables the inline call label/session feature. When enabled, a call window (such as, incoming call, single call, all calls list) will be minimized to an inline call label/session. The users can view the current call session information through the inline call label. Because the call window is minimized, the status of other lines and BLF/SD features are visible (not blocked by the full call window) for the users. This feature is available only on Cisco Desk Phone 9841, 9851, and 9861 with multiple lines. |
| User > Incoming Audio |
| Supported device types (For 9861, 9871, and 8875 only) | Default: Optimize for voice Options: Optimize for voice, Original | Enables or disables the Incoming Audio feature on 8875, 9861, or 9871. The users on the phone can enable this setting through: 9861: Settings > User perferences > Audio > Smart audio > Incoming audio 9871 and 8875: Settings > Audio > Smart audio > Incoming audio When enabled, the incoming audio is optimized. |
| User > Microphone Audio |
| Microphone Audio (For 9800 Series only) | Default: Noise removal Options: Original, Noise removal, Optimize for my voice | Enables or disables the Noise Removal feature. There're three options available: Original —Turns off the Noise Removal feature Noise removal —Removes all background noise Optimize for my voice —Removes all background noise and background speech |
| User > Screen |
| Appearance Custom Wallpaper Logo Enable Logo URL |  | See Configure the custom wallpaper and logo for details. For more details, see Custom wallpaper and logo for 9800/8875 . |
| Display Brightness (For 9851, 9861, 9871, and 8875 only) | Default: 12 Options: 2-15 | Sets the display brightness. The users on the phone can change the settings with: 9851 and 9861: the left and right navigation key or the "<" and ">" softkeys 9871 and 8875: the slider on the screen directly |
| Screen Brightness (For 9841 only) | Default: 3 Options: 1-4 | Sets the screen brightness. The users on the phone can change the settings with the left and right navigation key or the "<" and ">" softkeys on the phone. |
| User > Supplementary Services |
| DND Setting | Default: Yes Options: Yes, No | Enables or disables Do Not Disturb (DND) capability on the phone. When enabled, the users on the phone can turn DND on or off. |
| Date Format | Default: month/day Options: month/day, day/month | Defines the date format. |
| Group Call Pickup LED Alert (For 9800 Series only) | Default: Top LED Front Arc LED Both | Sets the LED alert type for the phones of a same group. If the parameter is set to Both , for an incoming call, both the front arc LED and the top LED of the phones that are in the same call pickup group flashes. This parameter is completely unrelated to the notification type in the group. Even if the notification type in the group is set to Audio only , the LED still blinks. |
| Missed Call Led Alert | Default: Disabled Options: Enabled, Disabled | Turns on or off LED indicators for missed calls. This parameter controls the Top 360 LED indicator on 9800 Series and the handset LED on 8875. When disabled, no LEDs light up for missed calls. |
| Time Format | Default: 12hr Options: 12hr, 24hr | Sets the display format for time. |
| User > Voice Feedback |
| Enable | Default: No Options; Yes, No | Enables or disables the voice feedback feature. The users on the phone can change the setting through Settings > Accessibility > Voice feedback . |
| For Password Enable | Default: No Options; Yes, No | Enables or disables the voice feedback when entering a password. The users on the phone can change the setting through Settings > Accessibility > Voice feedback > Voice feedback for password . |
| Voice Speed | Default: Normal Options: Slowest, Slower, Normal, Faster, Fastest | Sets the speed rate of voice feedback. The users on the phone can change the setting through Settings > Accessibility > Voice feedback > Voice speed . |
| Voice Volume | Default: Normal Options: Lowest, Low, Normal, High, Highest | Sets the voice volume. The users on the phone can change the voice volume through Settings > Accessibility > Voice feedback > Voice volume . |

| Ringtone setting option | Ringtone name |
|---|---|
| 1 (Default) | Bellcore-dr1 |
| 2 | Bellcore-dr2 |
| 3 | Bellcore-dr3 |
| 4 | Sunrise |
| 5 | Chirp 1 |
| 6 | Delight |
| 7 | Evolve |
| 8 | Mellow |
| 9 | Mischief |
| 10 | Reflections |
| 11 | Ringer |
| 12 | Ascent |
| 13 | Chirp 2 |
| 14 | Incoming_EQ |
| 15 | Vibes |
| Custom 1 - 10 | Depending on custom ringtone file specified at All configurations > Phone > Ringtone . |

| Macro Name | Macro Expansion |
|---|---|
| $ | The form $$ expands to a single $ character. |
| A through P | Replaced by general-purpose parameters GPP_A through GPP_P. |
| SA through SD | Replaced by special purpose parameters GPP_SA through GPP_SD. These parameters
                hold keys or passwords used in provisioning. $SA through $SD are recognized as arguments to the optional resync URL
                    qualifier, --key. |
| MA | MAC address using lowercase hex digits (000e08aabbcc). |
| MAU | MAC address using uppercase hex digits (000E08AABBCC). |
| MAC | MAC address using lowercase hex digits with a colon to separate hex digit pairs (00:0e:08:aa:bb:cc). |
| PN | Product Name; for example, Video Phone 8875, Desk Phone 9851. |
| PSN | Product Series Number; for example, 8875, 9841, 9861 |
| SN | Serial Number string; for example, 88012BA01234. |
| CCERT | SSL Client Certificate status, installed or not installed. |
| IP | IP address of the phone within its local subnet; for example, 192.168.1.100. |
| EXTIP | External IP of the phone, as seen on the internet; for example, 66.43.16.52. |
| SWVER | Software version string. For example, PHONEOS.3-2-1-0104-37 |
| HWVER | Hardware version string. For example, 2.0.1 |
| PRVST | Provisioning State (a numeric string): -1 = explicit resync request 0 = power-up resync 1 = periodic resync 2 = resync failed, retry attempt |
| UPGST | Upgrade State (a numeric string): 1 = first upgrade attempt 2 = upgrade failed, retry attempt |
| UPGERR | Result message (ERR) of previous upgrade attempt; for example http_get failed. |
| PRVTMR | Seconds since last resync attempt. |
| UPGTMR | Seconds since last upgrade attempt. |
| REGTMR1 | Seconds since Line 1 lost registration with SIP server. |
| REGTMR2 | Seconds since Line 2 lost registration with SIP server. |
| UPGCOND | Legacy macro name. |
| SCHEME | File access scheme, one of TFTP, HTTP, or HTTPS, as obtained after parsing resync or upgrade URL. |
| SERV | Request target server host name, as obtained after parsing resync or upgrade URL. |
| SERVIP | Request target server IP address, as obtained after parsing resync or upgrade URL, possibly following DNS lookup. |
| PORT | Request target UDP/TCP port, as obtained after parsing resync or upgrade URL. |
| PATH | Request target file path, as obtained after parsing resync or upgrade URL. |
| ERR | Result message of resync or upgrade attempt. Only useful in generating result syslog messages. The value is preserved in the UPGERR variable in the case of upgrade attempts. |
| UIDn | The contents of the Line n UserID configuration parameter. |
| ISCUST | If unit is customized, value=1, otherwise 0. Customization status is viewable on Web UI Info page. |
| INCOMINGNAME | Name associated with first connected, ringing, or inbound call. |
| REMOTENUMBER | Phone number of first connected, ringing, or inbound call. If there are multiple calls, the data associated with the first call found is provided. |
| DISPLAYNAMEn | The contents of the Line N Display Name configuration parameter. |
| AUTHIDn | The contents of the Line N auth ID configuration parameter. |