---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-english-admin-guide-at9x-b-ata191-192-admin-mp-at9x-b-ata191-1-800f74bae2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/english/admin-guide/at9x_b_ata191-192-admin-mp/at9x_b_ata191-192-admin-mp_chapter_0100.html
retrieved_at: 2026-08-22T01:03:41.763790+00:00
---

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

# Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Updated: January 30, 2026

Chapter: Administration Settings

## Chapter: Administration Settings

# Administration Settings

## Management

Use the Management pages to manage web access to the ATA web page and to enable protocols for remote configuration and network
                           management.

### Web Access Management

Use the Administration > Management > Web Access Management page to configure the settings for access to the administration of the ATA.

#### Cisco ATA 191 Web Access Fields

Access to the Cisco ATA 191 web page is enabled by default. Admin Access allows you to manage the configuration from a computer
                                    in your office network, and Web Utility Access allows you to connect from a computer on a different subnet or on the Internet.

To access the ATA web page, launch a web browser and enter the URL in the address bar. The URL must include the specified
                                    protocol, the WAN IP address of the ATA, and the specified port number. For example, with the HTTPS protocol, a WAN IP address
                                    of 203.0.113.50, and port 443, you would enter: https://203.0.113.50:443

Field

Description

Admin Access

This feature controls access to the ATA web page from devices that are connected via the ETHERNET (LAN) port.

Click Enabled to enable this feature, or click Disabled to disable it.

The default setting is Enabled. If you administer and configure the ATA from a computer that is connected to the LAN, this
                                                feature must be enabled.

Web Utility Access

Select the protocol to use for access to the ATA web page from a device on the WAN. Choose HTTP , HTTPS , or both entries. For secure Internet access, select HTTPS. The default value is HTTPS.

Remote Management Port

Enter the port number to use for access to the ATA web page from a device on the WAN side of the ATA. The default port number
                                                is 443 for HTTPS, 80 for HTTP.

Include the specified port when you enter the address in your web browser. For example, with the HTTPS protocol, a WAN IP
                                                address of 203.0.113.50, and the default Remote Management Port of 443, you would enter: https://203.0.113.50:443

#### Cisco ATA 192 Web Access Fields

Access to the Cisco ATA 192 web page is enabled by default. Admin Access allows you to manage the configuration from a computer
                                    in your office network, and Web Utility Access allows you to connect from a computer on a different subnet or on the Internet.

Field

Description

Admin Access

This feature controls access to the ATA web page from devices that are connected via the ETHERNET (LAN) port.

Click Enabled to enable this feature, or click Disabled to disable it.

The default setting is Enabled. If you administer and configure the ATA from a computer that is connected to the LAN, this
                                                feature must be enabled.

Web Utility Access

Select the protocol to use for access to the ATA web page from a device on the WAN. Choose HTTP and/or HTTPS . For secure Internet access, select HTTPS. The default value is HTTPS.

#### Cisco ATA 192 Remote Access Fields

In addition to the ATA web page access, the Cisco ATA 192 provides more features of Remote Management.

Field

Description

Remote Management

Allows access to the ATA web page from a device that is on the WAN side of the ATA. For example, you could connect from another
                                                subnet in your office or from your home computer.

Click Enabled to enable this feature, or click Disabled to disable it.

The default setting is Disabled. The other fields in this section of the page are available only if you enable this feature.
                                                If you attempt to enable this feature while using the default administrator login credentials, you will be prompted to change
                                                the credentials. Click OK to acknowledge the warning message. Use the Administration > Management > User List page to change the administrator password. For more information, see User List (Password Management) .

Web Utility Access

Select the protocol to use for access to the ATA web page from a device on the WAN side of the ATA. Choose HTTP and/or HTTPS .

The default value is HTTPS .

Include the specified protocol when you enter the address in your web browser. For example, with the HTTPS protocol, a WAN
                                                IP address of 203.0.113.50, and the default Remote Management Port of 443, you would enter: https://203.0.113.50:443

Remote Upgrade

If you enabled Remote Management, choose whether or not to allow firmware upgrades from a device on the WAN side of the ATA.
                                                Click Enabled to enable this feature, or click Disabled to disable it. The default value is Disabled.

You can change this setting only when your computer is connected to the configuration utility from the LAN.

Allowed Remote IP Address

You can use this feature to limit access to the ATA web page based on the IP address of a device. Choose Any IP Address to allow access from any external IP address. To specify an external IP address or range of IP addresses, select the second
                                                radio button and then enter the desired IP address or range. The default setting is Any IP Address.

Remote Management Port

Enter the port number to use for access to the ATA web page from a device on the WAN side of the ATA. The default port number
                                                is 443 for HTTPS, 80 for HTTP.

Include the specified port when you enter the address in your web browser. For example, with the HTTPS protocol, a WAN IP
                                                address of 203.0.113.50, and the default Remote Management Port of 443, you would enter: https://203.0.113.50:443

### TR-069

Use the Administration > Management > TR-069 page to configure communication with an Auto-Configuration Server (ACS) via TR-069 CPE WAN Management Protocol (CWMP). TR-069
                                 (Technical Report 069) provides a common platform to manage all voice devices and other customer-premises equipment (CPE)
                                 in large-scale deployments. It provides the communication between the CPE and the ACS.

Enter the settings as described below. After making changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings.

Field

Description

Status

Click Enabled to enable remote provisioning, or click Disabled to disable this feature. The default setting is Disabled.

ACS URL

The URL for the ACS. The format should be http(s)://xxx.xxx.xxx.xxx:port or xxx.xxx.xxx.xxx:port. The xxx.xxx.xxx.xxx is the
                                             domain name or IP address of the ACS server.

Both the IP address and the port number are required.

ACS Username

The username for the ACS. The default username is the Organization Unit Identifier (OUI). This value is required and must
                                             match the username configured on the ACS.

ACS Password

The password for the ACS. This value is required and must match the password configured on the ACS.

Connection Request Port

The port to use for connection requests

Connection Request Username

The username for connection requests. This value must match the Connection Request Username configured on the ACS.

Connection Request Password

The password for connection requests. This value must match the Connection Request Password configured on the ACS.

Periodic Inform Interval

If Periodic Inform is enabled, the duration, in seconds, between CPE attempts to connect to the ACS. The default value is
                                             86400 seconds.

Periodic Inform Enable

Click Enabled to enable CPE connection requests to the ACS, or click Disabled to disable this feature.

Request Download

If applied, ACS may call the Download RPC after it receives the request from the ATA.

### SNMP

Use the Administration > Management > SNMP page to set up Simple Network Management Protocol (SNMP) for the ATA.

SNMP is a network protocol that allows network administrators to manage, monitor, and receive notifications of critical events
                                 as they occur on the network. The ATA supports SNMPv2 and SNMPv3.

It acts as an SNMP agent that replies to SNMP commands from SNMP Network Management Systems. It supports the standard SNMP
                                 get, next, and set commands. It also generates SNMP traps to notify the SNMP manager when configured alarm conditions occur.
                                 Examples include reboots, power cycles, and INTERNET (WAN) events.

Enter the settings as described below. After making changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings.

#### SNMP Settings

Field

Description

Enabled, Disabled

Click Enabled to enable this feature, or click Disabled to disable it. The default setting is Disabled.

Trusted IPv4

Choose Any to allow access from any IPv4 address (not recommended).

Click Address to specify the IPv4 address and subnet mask of a single SNMP manager or trap agent that can access the ATA through SNMP.

Trusted IPv6

Choose Any to allow access from any IPv6 address (not recommended).

Click Address to specify the IPv6 address and prefix length of a single SNMP manager or trap agent that can access the ATA through SNMP.

Get/Trap Community

Enter a community string for authentication for SNMP GET commands. The default value is public.

Set Community

Enter a community string for authentication for SNMP SET commands. The default value is private.

#### SNMPv3 Settings

Field

Description

Enabled, Disabled

Click Enabled to enable this feature, or click Disabled to disable it. The default setting is Disabled.

R/W User

Enter the user name for SNMPv3 authentication. The default value is v3rwuser.

Auth-Protocol

Choose the SNMPv3 authentication protocol from the drop-down list ( HMAC-MD5 , HMAC-SHA , HMAC-SHA256 , or HMAC-SHA512 ).

If FIPS mode is enabled, HMAC-MD5 and HMAC-SHA are disabled on the ATA. In this case, it's recommended to use HMAC-SHA256 or HMAC-SHA512 .

Auth-Password

Enter the authentication password.

PrivProtocol

Choose a privacy authentication protocol from the drop-down list ( None , CBC-DES , or AES ). If you select CBC-DES, the privKey encrypts the data portion of the message that is being sent.

If FIPS mode is enabled, DES is disabled on the ATA. In this case, it's recommended to use AES .

Privacy Password

Enter the key for the authentication protocol to use.

#### Trap Configuration

Field

Description

IP Address

The IP Address of the SNMP manager or trap agent.

Port

The SNMP trap port used by the SNMP manager or trap agent to receive the trap messages. Valid entries are 162 or 1025–65535.
                                                The default value is162.

SNMP Version

The SNMP version in use by the SNMP manager or trap agent. Choose a version from the list.

### User List (Password Management)

Use the Administration > Management > User List page to manage the two user accounts for the ATA web page. The user-level account has access to modify a limited set of features.

For the IVR, you can configure these passwords on the System page.

#### Update a Password

Step 1

In the User List table, click the pencil icon for the account that you want to update.

Step 2

On the User Account page, enter the username and password, as described below.

Username—Enter a username.

Old Password (administrator account only)—Enter the existing password.

New Password—Enter your new password. The password must contain 8 to 32 characters.

Confirm New Password—Enter the new password again, to confirm.

Step 3

After making changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings.

### Bonjour

Use the Administration > Management > Bonjour page to enable or disable Bonjour. Bonjour is a service discovery protocol that locates network devices such as computers
                                 and servers on your LAN. It may be required by network management systems that you use. When this feature is enabled, the
                                 ATA periodically multicasts Bonjour service records to its entire local network to advertise its existence.

Click Enabled to enable this feature, or click Disabled to disable it. The default setting is Enabled.

After making changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings.

### Reset Button

Click Enabled to enable the reset button, or click Disabled to disable it. The default setting is Enabled.

After making changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings.

### SSH

Use the Administration > Management > SSH to configure SSH related setting.

Field

Description

User Name

Set SSH login user name.

Password

Set SSH login password.

SSH Access

Set the SSH access to enable or disable.

## Log

The ATA allows you to record incoming, outgoing, and DHCP lists for various events that occur on your network. The Incoming
                           Log displays a temporary list of the source IP addresses and destination port numbers for the incoming Internet traffic. The
                           Outgoing Log displays a temporary list of the local IP addresses, destination URLs/IP addresses, and service/port numbers
                           for the outgoing Internet traffic.

### Debug Log Module

Use the Administration > Log > Debug Log Module page to enable and configure logging.

As a best practice, we recommend that you enable logging only when needed, and disable logging when you finish the investigation.
                                       Logging consumes resources and can impact system performance.

In this page, you can select the modules which you want to see debug messages in all severity levels.

### Debug Log Setting

If Debug Log Server is enabled on the Administration > Log > Debug Log Server page, the ATA will send the debug messages to one server.

Enter the settings as described below. After making changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings.

Field

Description

Debug Log Size

Enter the maximum size of the log file in kilobytes. Valid values are from 128 to 1024.

IPv4 Address

Enter the IPv4 address of the debug log server where the messages will be sent.

IPv6 Address

Enter the IPv6 address of the debug log server where the messages will be sent.

Port

Enter the port to use on the server. Valid values are from 1 to 65535.

### Debug Log Viewer

If logging is enabled on the Administration > Log > Debug Log Viewer page, you can use the Log Viewer page view the logs online and to download the system log file to your computer. You can
                                 limit the contents of the log by choosing the types of entries to include and by specifying keywords.

For information about enabling and configuring logging, see Debug Log Module .

Field

Description

Download Log

Click this button to download the contents of the log as a file on your computer. In the dialog box, you can open the file
                                             or save it. The file can be opened in a text editor such as Notepad.

Clear Log

Click this button to remove all entries from the log.

Filter

Enter a keyword to filter the log entries that appear in the viewer. The page will display only the entries that include the
                                             keyword.

### Event Log Setting

Use the Administration > Log > Event Log Setting page to collect required event logs. Event log messages are sent via SYSLOG protocol using UDP transport type.

Use the Event Log Setting when troubleshooting. Four event categories are defined:

DEV—Device information. A message is sent once device boot-up and network connectivity are ready.

SYS—System-related information. A message is sent once while device boot-up and network connectivity are ready.

CFG—Status of provision and configuration file change. A message is sent every time the provision service restarts due to
                                       configuration or network status change.

REG—Registration status for each line. A message is sent every time registration status changes.

Enter the settings as described below. After making changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings.

Field

Description

Address

Set the Event log server address.

Port

Set the Event log server port.

Default value: 514

Flag

Set the Event log flag, it’s a bitwise value. Setting list is as below:

<Dev>:1(0x01)

<SYS>:2(0x01<<1)

<CFG>:4(0x01<<2)

<REG>:8(0x01<<3)

Default value: 15 (All events)

### PRT Viewer

Use the Administration > Log > PRT Viewer to generate and download Problem Report Tools (PRT) files.

To generate a problem report remotely, see Generate a Problem Report Remotely .

After making your changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings.

Field

Description

PRT Upload URL

Set the PRT log upload URL

PRT Upload Method

Set the PRT log upload method, POST or PUT .

Default: POST

PRT Max Timer

Set the PRT max timer, valid range is 15-1440 minutes

Disabled: 0

Default: 0

Problem Report Tools Logs

List the PRT file which is generated by user on ATA.

Generate PRT

Click this button to generate and download the contents of the PRT as a file on your computer. In the dialog box, you can
                                             open the file or save it.

#### Generate a Problem Report Remotely

You can initiate a problem report remotely. To do this, initiate a SIP-NOTIFY message from the server to the ATA, with the Event specified as prt-gen .  and ATA response 200 OK to the server. Then

The server sends NOTIFY to the ATA.

ATA response 200 OK to the server, and sends PRT file to the upload server.

The PRT upload server response 200 OK to the ATA.

##### Before you begin

ATA registers successfully

PRT Upload URL is configured

Step 1

In the Administration > Log > PRT Viewer section, enter the PRT Upload URL parameter to specifiy the server to which you want to send the PRT. For example: http://10.74.133.94:9090 .

The line is provisioned correctly with a valid SIP account.

Step 2

Click Submit All Changes .

### PCM Viewer

Use the Administration > Log > PCM Viewer to download and view PCM.

The ATA allows you to capture the PCM log file while a user offhook to start a call.

After making your changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings.

Field

Description

PCM Capture Enable

Enable or disable capture PCM.

Duration

Enter the PCM capture duration in seconds. The valid range is 20 to 300.

PCM File List

List the PCM file which is captured by user.

Click Refresh to refresh the PCM Memory Dump File. Click Download to download the dump file on your computer.

### CSS Dump

Use the Administration > Log > CSS Dump page to set and download CSS dump file.

Field

Description

Auto Crash Dump

Set whether the ATA creates a crash dump file automatically when it occurs an error.

Click Enabled to enable the feature, click Disabled to disable it.

Default setting: Disabled

Manual Trigger Key(**##)

Set whether the user can manually trigger the creation of the CSS dump by pressing **## on the phone keypad.

Click Enabled to enable the feature, click Disabled to disable it.

Default setting: Disabled

CSS Dump List

List the CSS file which is captured by user.

Click Refresh to refresh the CSS Memory Dump File. Click Download to download the dump file on your computer.

### Crash Dump

Use the Administration > Log > Crash Dump page to set and download crash dump file.

Field

Description

Runtime log to flash

Set whether the runtime log can be stored in the flash memory.

Click Enabled to enable the feature, click Disabled to disable it.

Default setting: Disabled

Crash Dump File

Display the captured crash dump file.

Click the file name to download it on your computer.

Click Refresh to refresh the crash  dump file.

## Factory Defaults

Use the Administration > Factory Defaults ATA web page to reset the ATA to the default configuration.

Alternatively, press and hold the RESET button for 10 seconds.

After the factory reset is performed successfully, all LEDs are fast flashing green.

All user-changeable non-default settings will be lost. This may include network and service provider data.

You can perform the following tasks:

Restore Router Factory Defaults: Choose Yes to remove any custom data (router) settings that you have configured. The default settings will be restored when you click Submit .

Restore Voice Factory Defaults: Choose Yes to remove any custom settings that you configured on the Voice pages of the ATA web page. The default settings will be restored
                                    when you click Submit .

## Firmware Upgrade

Use the Administration > Firmware Upgrade page to upgrade the firmware on the ATA. It is not necessary to upgrade unless you are experiencing problems with the ATA
                              or if the new firmware has a feature that you want to use.

Caution

Upgrading the firmware may take several minutes. Until the process is complete, DO NOT turn off the power, press the hardware
                                          reset button, or click the Back button in your current browser.

### Before you begin

Before upgrading the firmware, download the firmware upgrade file for the ATA.

Step 1

Click Browse and select the location of the upgrade file that you downloaded.

Step 2

Click the Upgrade button to upgrade the firmware.

### ATA with Firmware Release 11.1.0MSR3-9 and Older Doesn't Upgrade

ATA with firmware version 11.1.0MSR3-9 and older fails to upgrade to the later releases if the server is implemented as HTTP
                                 chunk mode and the chunk-size is greater than 16K.

To bypass this upgrade failure, we recomment you to use this external HTTP server.

## Configuration Management

Use the Administration > Config Management pages to backup and restore the configuration settings for the ATA.

### Backup Configuration

Use the Administration > Config Management > Backup Configuration page to back up the ATA configuration settings to a file. You can then later restore these same settings to the ATA.

Click the Backup button to save the configuration information of the ATA. When the dialog box appears, choose a location where you want to
                                 save the .cfg file.

Tip: Rename the file with a name that includes the date and time when you did the backup.

### Restore Configuration

Use the Administration > Config Management > Restore Configuration page to restore the ATA configuration settings from a previous backup. We recommend that you back up your current configuration
                                 settings before you restore a configuration.

Step 1

Click Browse to locate the .cfg file on your computer.

Step 2

Click Restore to restore the settings from the selected file.

## Reboot

Use the Administration > Reboot page to power cycle the ATA from the ATA web page. Another way to do it is by pressing the Reset > Reboot button.

Click the Reboot button to power cycle the ATA. When the warning message appears, read the information, and then click OK to reboot the ATA, or click Cancel to abandon the operation. The ATA and any connected devices will lose network connectivity during this operation.

| Field | Description |
|---|---|
| Admin Access | This feature controls access to the ATA web page from devices that are connected via the ETHERNET (LAN) port. Click Enabled to enable this feature, or click Disabled to disable it. The default setting is Enabled. If you administer and configure the ATA from a computer that is connected to the LAN, this
                                                feature must be enabled. |
| Web Utility Access | Select the protocol to use for access to the ATA web page from a device on the WAN. Choose HTTP , HTTPS , or both entries. For secure Internet access, select HTTPS. The default value is HTTPS. |
| Remote Management Port | Enter the port number to use for access to the ATA web page from a device on the WAN side of the ATA. The default port number
                                                is 443 for HTTPS, 80 for HTTP. Include the specified port when you enter the address in your web browser. For example, with the HTTPS protocol, a WAN IP
                                                address of 203.0.113.50, and the default Remote Management Port of 443, you would enter: https://203.0.113.50:443 |

| Field | Description |
|---|---|
| Admin Access | This feature controls access to the ATA web page from devices that are connected via the ETHERNET (LAN) port. Click Enabled to enable this feature, or click Disabled to disable it. The default setting is Enabled. If you administer and configure the ATA from a computer that is connected to the LAN, this
                                                feature must be enabled. |
| Web Utility Access | Select the protocol to use for access to the ATA web page from a device on the WAN. Choose HTTP and/or HTTPS . For secure Internet access, select HTTPS. The default value is HTTPS. |

| Field | Description |
|---|---|
| Remote Management | Allows access to the ATA web page from a device that is on the WAN side of the ATA. For example, you could connect from another
                                                subnet in your office or from your home computer. Click Enabled to enable this feature, or click Disabled to disable it. The default setting is Disabled. The other fields in this section of the page are available only if you enable this feature.
                                                If you attempt to enable this feature while using the default administrator login credentials, you will be prompted to change
                                                the credentials. Click OK to acknowledge the warning message. Use the Administration > Management > User List page to change the administrator password. For more information, see User List (Password Management) . |
| Web Utility Access | Select the protocol to use for access to the ATA web page from a device on the WAN side of the ATA. Choose HTTP and/or HTTPS . The default value is HTTPS . Include the specified protocol when you enter the address in your web browser. For example, with the HTTPS protocol, a WAN
                                                IP address of 203.0.113.50, and the default Remote Management Port of 443, you would enter: https://203.0.113.50:443 |
| Remote Upgrade | If you enabled Remote Management, choose whether or not to allow firmware upgrades from a device on the WAN side of the ATA.
                                                Click Enabled to enable this feature, or click Disabled to disable it. The default value is Disabled. You can change this setting only when your computer is connected to the configuration utility from the LAN. |
| Allowed Remote IP Address | You can use this feature to limit access to the ATA web page based on the IP address of a device. Choose Any IP Address to allow access from any external IP address. To specify an external IP address or range of IP addresses, select the second
                                                radio button and then enter the desired IP address or range. The default setting is Any IP Address. |
| Remote Management Port | Enter the port number to use for access to the ATA web page from a device on the WAN side of the ATA. The default port number
                                                is 443 for HTTPS, 80 for HTTP. Include the specified port when you enter the address in your web browser. For example, with the HTTPS protocol, a WAN IP
                                                address of 203.0.113.50, and the default Remote Management Port of 443, you would enter: https://203.0.113.50:443 |

| Field | Description |
|---|---|
| Status | Click Enabled to enable remote provisioning, or click Disabled to disable this feature. The default setting is Disabled. |
| ACS URL | The URL for the ACS. The format should be http(s)://xxx.xxx.xxx.xxx:port or xxx.xxx.xxx.xxx:port. The xxx.xxx.xxx.xxx is the
                                             domain name or IP address of the ACS server. Both the IP address and the port number are required. |
| ACS Username | The username for the ACS. The default username is the Organization Unit Identifier (OUI). This value is required and must
                                             match the username configured on the ACS. |
| ACS Password | The password for the ACS. This value is required and must match the password configured on the ACS. |
| Connection Request Port | The port to use for connection requests |
| Connection Request Username | The username for connection requests. This value must match the Connection Request Username configured on the ACS. |
| Connection Request Password | The password for connection requests. This value must match the Connection Request Password configured on the ACS. |
| Periodic Inform Interval | If Periodic Inform is enabled, the duration, in seconds, between CPE attempts to connect to the ACS. The default value is
                                             86400 seconds. |
| Periodic Inform Enable | Click Enabled to enable CPE connection requests to the ACS, or click Disabled to disable this feature. |
| Request Download | If applied, ACS may call the Download RPC after it receives the request from the ATA. |

| Field | Description |
|---|---|
| Enabled, Disabled | Click Enabled to enable this feature, or click Disabled to disable it. The default setting is Disabled. |
| Trusted IPv4 | Choose Any to allow access from any IPv4 address (not recommended). Click Address to specify the IPv4 address and subnet mask of a single SNMP manager or trap agent that can access the ATA through SNMP. |
| Trusted IPv6 | Choose Any to allow access from any IPv6 address (not recommended). Click Address to specify the IPv6 address and prefix length of a single SNMP manager or trap agent that can access the ATA through SNMP. |
| Get/Trap Community | Enter a community string for authentication for SNMP GET commands. The default value is public. |
| Set Community | Enter a community string for authentication for SNMP SET commands. The default value is private. |

| Field | Description |
|---|---|
| Enabled, Disabled | Click Enabled to enable this feature, or click Disabled to disable it. The default setting is Disabled. |
| R/W User | Enter the user name for SNMPv3 authentication. The default value is v3rwuser. |
| Auth-Protocol | Choose the SNMPv3 authentication protocol from the drop-down list ( HMAC-MD5 , HMAC-SHA , HMAC-SHA256 , or HMAC-SHA512 ). Note If FIPS mode is enabled, HMAC-MD5 and HMAC-SHA are disabled on the ATA. In this case, it's recommended to use HMAC-SHA256 or HMAC-SHA512 . | Note | If FIPS mode is enabled, HMAC-MD5 and HMAC-SHA are disabled on the ATA. In this case, it's recommended to use HMAC-SHA256 or HMAC-SHA512 . |
| Note | If FIPS mode is enabled, HMAC-MD5 and HMAC-SHA are disabled on the ATA. In this case, it's recommended to use HMAC-SHA256 or HMAC-SHA512 . |
| Auth-Password | Enter the authentication password. |
| PrivProtocol | Choose a privacy authentication protocol from the drop-down list ( None , CBC-DES , or AES ). If you select CBC-DES, the privKey encrypts the data portion of the message that is being sent. Note If FIPS mode is enabled, DES is disabled on the ATA. In this case, it's recommended to use AES . | Note | If FIPS mode is enabled, DES is disabled on the ATA. In this case, it's recommended to use AES . |
| Note | If FIPS mode is enabled, DES is disabled on the ATA. In this case, it's recommended to use AES . |
| Privacy Password | Enter the key for the authentication protocol to use. |

| Note | If FIPS mode is enabled, HMAC-MD5 and HMAC-SHA are disabled on the ATA. In this case, it's recommended to use HMAC-SHA256 or HMAC-SHA512 . |
|---|---|

| Note | If FIPS mode is enabled, DES is disabled on the ATA. In this case, it's recommended to use AES . |
|---|---|

| Field | Description |
|---|---|
| IP Address | The IP Address of the SNMP manager or trap agent. |
| Port | The SNMP trap port used by the SNMP manager or trap agent to receive the trap messages. Valid entries are 162 or 1025–65535.
                                                The default value is162. |
| SNMP Version | The SNMP version in use by the SNMP manager or trap agent. Choose a version from the list. |

| Step 1 | In the User List table, click the pencil icon for the account that you want to update. |
|---|---|
| Step 2 | On the User Account page, enter the username and password, as described below. Username—Enter a username. Old Password (administrator account only)—Enter the existing password. New Password—Enter your new password. The password must contain 8 to 32 characters. Confirm New Password—Enter the new password again, to confirm. |
| Step 3 | After making changes, click Submit to save your settings, or click Cancel to redisplay the page with the saved settings. |

| Field | Description |
|---|---|
| User Name | Set SSH login user name. |
| Password | Set SSH login password. |
| SSH Access | Set the SSH access to enable or disable. |

| Field | Description |
|---|---|
| Debug Log Size | Enter the maximum size of the log file in kilobytes. Valid values are from 128 to 1024. |
| IPv4 Address | Enter the IPv4 address of the debug log server where the messages will be sent. |
| IPv6 Address | Enter the IPv6 address of the debug log server where the messages will be sent. |
| Port | Enter the port to use on the server. Valid values are from 1 to 65535. |

| Field | Description |
|---|---|
| Download Log | Click this button to download the contents of the log as a file on your computer. In the dialog box, you can open the file
                                             or save it. The file can be opened in a text editor such as Notepad. |
| Clear Log | Click this button to remove all entries from the log. |
| Filter | Enter a keyword to filter the log entries that appear in the viewer. The page will display only the entries that include the
                                             keyword. |

| Field | Description |
|---|---|
| Address | Set the Event log server address. |
| Port | Set the Event log server port. Default value: 514 |
| Flag | Set the Event log flag, it’s a bitwise value. Setting list is as below: <Dev>:1(0x01) <SYS>:2(0x01<<1) <CFG>:4(0x01<<2) <REG>:8(0x01<<3) Default value: 15 (All events) |

| Field | Description |
|---|---|
| PRT Upload URL | Set the PRT log upload URL |
| PRT Upload Method | Set the PRT log upload method, POST or PUT . Default: POST |
| PRT Max Timer | Set the PRT max timer, valid range is 15-1440 minutes Disabled: 0 Default: 0 |
| Problem Report Tools Logs | List the PRT file which is generated by user on ATA. |
| Generate PRT | Click this button to generate and download the contents of the PRT as a file on your computer. In the dialog box, you can
                                             open the file or save it. |

| Step 1 | In the Administration > Log > PRT Viewer section, enter the PRT Upload URL parameter to specifiy the server to which you want to send the PRT. For example: http://10.74.133.94:9090 . The line is provisioned correctly with a valid SIP account. |
|---|---|
| Step 2 | Click Submit All Changes . |

| Field | Description |
|---|---|
| PCM Capture Enable | Enable or disable capture PCM. |
| Duration | Enter the PCM capture duration in seconds. The valid range is 20 to 300. |
| PCM File List | List the PCM file which is captured by user. Click Refresh to refresh the PCM Memory Dump File. Click Download to download the dump file on your computer. |

| Field | Description |
|---|---|
| Auto Crash Dump | Set whether the ATA creates a crash dump file automatically when it occurs an error. Click Enabled to enable the feature, click Disabled to disable it. Default setting: Disabled |
| Manual Trigger Key(**##) | Set whether the user can manually trigger the creation of the CSS dump by pressing **## on the phone keypad. Click Enabled to enable the feature, click Disabled to disable it. Default setting: Disabled |
| CSS Dump List | List the CSS file which is captured by user. Click Refresh to refresh the CSS Memory Dump File. Click Download to download the dump file on your computer. |

| Field | Description |
|---|---|
| Runtime log to flash | Set whether the runtime log can be stored in the flash memory. Click Enabled to enable the feature, click Disabled to disable it. Default setting: Disabled |
| Crash Dump File | Display the captured crash dump file. Click the file name to download it on your computer. Click Refresh to refresh the crash  dump file. |

| Caution | Upgrading the firmware may take several minutes. Until the process is complete, DO NOT turn off the power, press the hardware
                                          reset button, or click the Back button in your current browser. |
|---|---|

| Step 1 | Click Browse and select the location of the upgrade file that you downloaded. |
|---|---|
| Step 2 | Click the Upgrade button to upgrade the firmware. |

| Step 1 | Click Browse to locate the .cfg file on your computer. |
|---|---|
| Step 2 | Click Restore to restore the settings from the selected file. |