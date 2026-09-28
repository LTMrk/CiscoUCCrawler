---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-english-user-guide-at1x-b-ata191-ata192-user-mpp-at1x-b-ata191-1c8ddb12e8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/english/user-guide/at1x_b_ata191-ata192-user-mpp/at1x_b_ata191-ata192-user-mpp_chapter_0101.html
retrieved_at: 2026-08-22T01:04:36.076907+00:00
---

Cisco ATA 191 and ATA 192 Analog Telephone Adapter User Guide for Multiplatform Firmware

# Cisco ATA 191 and ATA 192 Analog Telephone Adapter User Guide for Multiplatform Firmware

Updated: April 10, 2025

Chapter: Configure Features

## Chapter: Configure Features

# Configure Features

## Phone Adapter Configuration Utility

You can configure or customize some phone features with the Phone Adapter Configuration Utility webpage. Your administrator
                              gives you the page URL, your user ID, and password.

In the Configuration Utility page, you can view some network and administration settings, as well as some basic information
                              about your ATA, such as firmware version, serial number, and memory use.

Most people use the Phone Adapter Configuration Utility page to set up a few basic features such as Speed dial or Call forward.
                              To set up these features, refer to the following table.

The following table describes the phone features that you configure from the Phone Adapter Configuration Utility webpage.

Feature

Description

Call forward and Selective call forward.

You specify the number that will receive calls when call forward is enabled on the phone. Use the Configuration Utility page
                                          to set up more complicated call forward functions, for example, when your line is busy.

For more information, see Call Forward Settings or Selective Call Forward Settings and Set Up Phone Features with Phone Adapter Configuration Utility .

Speed dial.

You assign phone numbers to a line so that you can quickly call that person.

For more information, see Speed Dial Settings and Set Up Phone Features with Phone Adapter Configuration Utility

Supplementary services.

Configure such features as Call waiting, Do not disturb, or Called ID.

For more information, see Supplementary Service Settings and Set Up Phone Features with Phone Adapter Configuration Utility

Distinctive ring

You can assign a specific ring to a phone number or line.

For more information, see Distinctive Ring Settings and Set Up Phone Features with Phone Adapter Configuration Utility .

Ring setting

You can assign a specific ring to a certain situation such as when a call is on hold or during a call back.

For more information, see Ring Settings and Set Up Phone Features with Phone Adapter Configuration Utility .

## Set Up Phone Features with Phone Adapter Configuration Utility

Use the Phone Adapter Configuration Utility page to set up a few basic features such as Speed dial, Call forward or Do not
                              disturb.

### Before you begin

Before you set up a feature, you should review the corresponding settings page.

Step 1

Sign into Phone Adapter Configuration Utility as an user.

Step 2

Select Voice > User

Step 3

Navigate to the feature pane and set the fields.

Step 4

Click Save .

## Call Forward Settings

You can forward calls from any line on your phone to another phone number. But call forward is phone-line specific. If a call
                              reaches you on a line where call forwarding is not enabled, the call rings as usual.

There are two ways of forwarding your calls:

Forward all calls

Forward calls in special situations, such as when the phone is busy or there is no answer.

Call forward is set up from the Voice tab of the Configuration Utility page. Use the information in the following table to
                              guide you. Once you have entered your settings, click Save to retain your revisions.

When a call is forwarded, you hear a short ring before the call is forwarded to the new number.

The following table describes the Call Forward settings that you configure from the Voice tab of the Configuration Utility
                              page.

Field Name

Description

Usage Guidelines

Cfwd All Dest

Call Forward All Destination.

Default setting: blank

Use when you want to forward all of your incoming calls to another phone number. Enter the number that will receive the forwarded
                                          call.

Cfwd No Ans Dest

Call Forward No Answer Destination.

Default setting: blank

Use with Cfwd All Dest when you want your calls forwarded to a second person, if your first choice does not answer.

Cfwd Busy Dest

Call Forward Busy Destination.

Default setting: blank

Use with Cfwd All Dest when you want your calls forwarded to a second person, if your first choice is on another call.

Cfwd No Ans Delay

Call Forward No Answer Delay.

Default setting: 20

The delay in seconds before Call Forward No Answer triggers.

## Selective Call Forward Settings

You can have a list of up to 8 phone numbers that are forwarded whenever they call you. When someone calls from one of these
                              numbers, you hear a ring and the call is forwarded to the new number.

1408*—a call is forwarded to the corresponding destination if the phone number starts with 1408

1512???1234—a call is forwarded to the corresponding destinatio if the phone number is an 11-digit number starting with 1512
                                       and ending with 1234

You can also forward the last call that you received, or block the last call.

Selective call forward is set up from the Voice tab of the Configuration Utility page. Use the information in the following
                              table to guide you. Once you have entered your settings, click Save to retain your revisions.

The following table describes the Call Forward settings that you configure from the Voice tab of the Configuration Utility
                              page.

Field Name

Description

Usage Guidelines

Cfwd Sel1-8 Caller

Call Forward Selective Caller

Default setting: blank

Enter the phone number that you want redirected.

When a phone number matches the entry, the call is forwarded to the corresponding Cfwd Selective Destination.

Cfwd Sel1-8 Dest

Call Forward Selective Destination

Default setting: blank

Enter the phone number that will receive the forwarded call.

Cfwd Last Caller

Call Forward Last Caller

Default setting: blank

Enter the last caller's phone number.

This caller is actively forwarded to the Cfwd Last Dest using Call Forward Last.

Cfwd Last Dest.

Call Forward Last Destination

Default setting: blank

The destination for the Cfwd Last Caller.

Block Last Caller

-

Default setting: blank

The number of the last caller; this caller is blocked via the Block Last Caller Service.

Accept Last Caller

-

Default setting: blank

The number of the last caller; this caller is accepted via the Accept Last Caller Service.

## Speed Dial Settings

You can use specific phone lines to speed-dial people you call often.

Speed dials are set up from the Voice tab of the Configuration Utility page. Use the information in the following table to
                              guide you. Once you have entered your settings, click Save to retain your revisions.

The following table describes the Speed Dial settings that you configure from the Voice tab of the Configuration Utility page.

Field Name

Description

Usage Guidelines

Speed Dial 2-9

-

Default setting: blank

Enter a phone number that you dial often.

## Supplementary Service Settings

In addition to your main call features, the ATA provides support for several supplementary features. All of these services
                              are optional, and may not be available to you if  your administrator has disabled them. In some cases, your service provider
                              may support similar features using means other than the ATA.

Supplementary services are set up from the Voice tab of the Configuration Utility page. Use the information in the following
                              table to guide you. Once you have entered your settings, click Save to retain your revisions.

The following table describes the Supplementary Service settings that you configure from the Voice tab of the Configuration
                              Utility page.

Field

Description

Usage Guidelines

CW Setting

Call Waiting.

Default setting: Yes

Enable if you want to be notified of an incoming call while on an call.

Block CID

Block Caller ID.

Default setting: No

Allows you to block your phone number from phones that have caller identification enabled.

Block ANC

Block Anonymous Calls.

Default setting: No

Allows you to block any calls that do not display call information.

DND  Setting

Do Not Disturb.

Default setting: No

Use Do Not Disturb (DND) to silence your phone and ignore incoming call notifications when you need to avoid distractions.

CID Setting

Caller ID Generation.

Default setting: Yes

Enable if you want your Caller identification such as a phone number, name, or other descriptive text appear on the phone
                                          display.

CWCID Setting

Call Waiting Caller ID Generation.

Default setting: Yes

This feature assigns an ID for a call that is waiting.

Dist Ring

Distinctive Ring.

Default setting: Yes

Enable this feature if you plan to configure different numbers to the same phone and want to give different ringtone for each
                                          of the numbers.

Message Waiting

-

Default setting: no

Enable if you want to be notified of voicemail messages.

CONFCID Setting

Default setting: Yes

-

## Distinctive Ring Settings

You can customize how your phone indicates an incoming call by selecting different ringtones. But this feature requires a
                              specific type of computer code called a script. Contact your admistrator to have this feature enabled.

## Ring Settings

You can customize your ring tones to bst suit your needs. For example, you can have one ringtone for your incoming calls,
                              and another ring for your callback notifications.

Ring settings are set up from the Voice tab of the Configuration Utility page. Use the information in the following table
                              to guide you. Once you have entered your settings, click Save to retain your revisions.

The following table describes the Ring settings that you configure from the Voice tab of the Configuration Utility page.

Field Name

Description

Usage Guidelines

Default Ring

-

Default setting: 1

Allows you to select from one of 8 different ringtones for your incoming calls.

Default CWT

-

Default setting: 1

Allows you to select from one of 8 different ringtones for call waiting.

Hold Reminder Ring

-

Default setting: 8

Allows you to select from one of 8 different ringtones or none for calls on hold.

Call Back Ring

-

Default setting: 7

Allows you to select from one of 8 different ringtones for call back notifications

Cfwd Ring Splash Len

-

Default setting: 0

Enter the length of the ring when a call is forwarded, from 0 – 10 seconds.

Cblk Ring Splash Len

-

Default setting: 0

Enter the length of the ring for the call back notifications, from 0 – 10 seconds.

VMWI Ring Splash Len:

-

Default setting: 0

Enter the length of the ring for your voicemail notifications, from 0 – 10 seconds.

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

##### Before you begin

ATA registers successfully.

Step 1

Sign into Phone Adapter Configuration Utility.

Step 2

Select Administration > Log > PRT Viewer .

Step 3

Configure the PRT Upload URL parameter to specify the server to which you want to send the problem report. For example: http://10.74.133.94:9090 .

For more information about the PRT related parameters, see PRT Viewer .

Step 4

Click Submit .

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

| Feature | Description |
|---|---|
| Call forward and Selective call forward. | You specify the number that will receive calls when call forward is enabled on the phone. Use the Configuration Utility page
                                          to set up more complicated call forward functions, for example, when your line is busy. For more information, see Call Forward Settings or Selective Call Forward Settings and Set Up Phone Features with Phone Adapter Configuration Utility . |
| Speed dial. | You assign phone numbers to a line so that you can quickly call that person. For more information, see Speed Dial Settings and Set Up Phone Features with Phone Adapter Configuration Utility |
| Supplementary services. | Configure such features as Call waiting, Do not disturb, or Called ID. For more information, see Supplementary Service Settings and Set Up Phone Features with Phone Adapter Configuration Utility |
| Distinctive ring | You can assign a specific ring to a phone number or line. For more information, see Distinctive Ring Settings and Set Up Phone Features with Phone Adapter Configuration Utility . |
| Ring setting | You can assign a specific ring to a certain situation such as when a call is on hold or during a call back. For more information, see Ring Settings and Set Up Phone Features with Phone Adapter Configuration Utility . |

| Step 1 | Sign into Phone Adapter Configuration Utility as an user. |
|---|---|
| Step 2 | Select Voice > User |
| Step 3 | Navigate to the feature pane and set the fields. |
| Step 4 | Click Save . |

| Field Name | Description | Usage Guidelines |
|---|---|---|
| Cfwd All Dest | Call Forward All Destination. Default setting: blank | Use when you want to forward all of your incoming calls to another phone number. Enter the number that will receive the forwarded
                                          call. |
| Cfwd No Ans Dest | Call Forward No Answer Destination. Default setting: blank | Use with Cfwd All Dest when you want your calls forwarded to a second person, if your first choice does not answer. |
| Cfwd Busy Dest | Call Forward Busy Destination. Default setting: blank | Use with Cfwd All Dest when you want your calls forwarded to a second person, if your first choice is on another call. |
| Cfwd No Ans Delay | Call Forward No Answer Delay. Default setting: 20 | The delay in seconds before Call Forward No Answer triggers. |

| Field Name | Description | Usage Guidelines |
|---|---|---|
| Cfwd Sel1-8 Caller | Call Forward Selective Caller Default setting: blank | Enter the phone number that you want redirected. When a phone number matches the entry, the call is forwarded to the corresponding Cfwd Selective Destination. |
| Cfwd Sel1-8 Dest | Call Forward Selective Destination Default setting: blank | Enter the phone number that will receive the forwarded call. |
| Cfwd Last Caller | Call Forward Last Caller Default setting: blank | Enter the last caller's phone number. This caller is actively forwarded to the Cfwd Last Dest using Call Forward Last. |
| Cfwd Last Dest. | Call Forward Last Destination Default setting: blank | The destination for the Cfwd Last Caller. |
| Block Last Caller | - Default setting: blank | The number of the last caller; this caller is blocked via the Block Last Caller Service. |
| Accept Last Caller | - Default setting: blank | The number of the last caller; this caller is accepted via the Accept Last Caller Service. |

| Field Name | Description | Usage Guidelines |
|---|---|---|
| Speed Dial 2-9 | - Default setting: blank | Enter a phone number that you dial often. |

| Field | Description | Usage Guidelines |
|---|---|---|
| CW Setting | Call Waiting. Default setting: Yes | Enable if you want to be notified of an incoming call while on an call. |
| Block CID | Block Caller ID. Default setting: No | Allows you to block your phone number from phones that have caller identification enabled. |
| Block ANC | Block Anonymous Calls. Default setting: No | Allows you to block any calls that do not display call information. |
| DND  Setting | Do Not Disturb. Default setting: No | Use Do Not Disturb (DND) to silence your phone and ignore incoming call notifications when you need to avoid distractions. |
| CID Setting | Caller ID Generation. Default setting: Yes | Enable if you want your Caller identification such as a phone number, name, or other descriptive text appear on the phone
                                          display. |
| CWCID Setting | Call Waiting Caller ID Generation. Default setting: Yes | This feature assigns an ID for a call that is waiting. |
| Dist Ring | Distinctive Ring. Default setting: Yes | Enable this feature if you plan to configure different numbers to the same phone and want to give different ringtone for each
                                          of the numbers. |
| Message Waiting | - Default setting: no | Enable if you want to be notified of voicemail messages. |
| CONFCID Setting | Default setting: Yes | - |

| Field Name | Description | Usage Guidelines |
|---|---|---|
| Default Ring | - Default setting: 1 | Allows you to select from one of 8 different ringtones for your incoming calls. |
| Default CWT | - Default setting: 1 | Allows you to select from one of 8 different ringtones for call waiting. |
| Hold Reminder Ring | - Default setting: 8 | Allows you to select from one of 8 different ringtones or none for calls on hold. |
| Call Back Ring | - Default setting: 7 | Allows you to select from one of 8 different ringtones for call back notifications |
| Cfwd Ring Splash Len | - Default setting: 0 | Enter the length of the ring when a call is forwarded, from 0 – 10 seconds. |
| Cblk Ring Splash Len | - Default setting: 0 | Enter the length of the ring for the call back notifications, from 0 – 10 seconds. |
| VMWI Ring Splash Len: | - Default setting: 0 | Enter the length of the ring for your voicemail notifications, from 0 – 10 seconds. |

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

| Step 1 | Sign into Phone Adapter Configuration Utility. |
|---|---|
| Step 2 | Select Administration > Log > PRT Viewer . |
| Step 3 | Configure the PRT Upload URL parameter to specify the server to which you want to send the problem report. For example: http://10.74.133.94:9090 . For more information about the PRT related parameters, see PRT Viewer . |
| Step 4 | Click Submit . |

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