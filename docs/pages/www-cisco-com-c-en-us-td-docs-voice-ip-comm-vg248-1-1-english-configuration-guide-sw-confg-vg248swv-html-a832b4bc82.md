---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-vg248-1-1-english-configuration-guide-sw-confg-vg248swv-html-a832b4bc82
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/vg248/1_1/english/configuration/guide/sw_confg/vg248swv.html
retrieved_at: 2026-08-22T01:19:33.669263+00:00
---

Software Configuration Guide (Version 1.1)

# Software Configuration Guide (Version 1.1)

Updated: March 17, 2015

Chapter: Configuring the Telephony Settings on the VG248

## Chapter: Configuring the Telephony Settings on the VG248

## Configuring the Telephony Settings on the VG248

The telephony settings on the VG248 determine the functionality of the analog phones connected to it. However, before configuring these settings, ensure that you have completed the basic network configuration described in "Getting Started with the VG248."

After verifying connectivity to the network, review these sections to customize the telephony settings:

• Identifying the Cisco CallManager TFTP Server

• Changing the Cisco CallManager Device Name

• Disabling Cisco Fax Relay

• Reverting to Previous Configuration

• Choosing the Call Control Mode

• Assigning Feature Codes

• Identifying the Country Code for VG248

• Changing the Hook Flash Timer for Analog Phones

• Setting the Port Enable Policy

• Configuring Port Parameters

## Identifying the Cisco CallManager TFTP Server

The VG248 uses the TFTP server to identify the correct Cisco CallManager system. If you are using DHCP, the VG248 attempts to obtain the TFTP server address from the DHCP server. Or, you can select a different TFTP server by modifying this setting. If you are not using DHCP, or if your DHCP server is not configured with a TFTP server address, you should identify the TFTP server using this setting.

To assign a TFTP server, perform these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose CallManager TFTP server .

Step 4 Enter the IP address or host name of the TFTP server.

## Changing the Cisco CallManager Device Name

The VG248 uses the Cisco CallManager device name when registering ports with Cisco CallManager. The actual device name used is the value shown for this menu option followed by the port number. By default, this is set to "VGC" followed by 10 digits of the VG248's MAC address. For example, port one would use VCGxxxxxxxxxx01 as its device name, where xxxxxxxxxx are the last 10 digits of the MAC address.

You can change the default device name, but you must use the standard format described in the "Using Auto-Registration" section .

Step 1 .From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose CallManager device name .

Step 4 Enter the new device name.

## Disabling Cisco Fax Relay

The VG248 supports Cisco fax relay. Cisco fax relay provides a more reliable method of transporting fax data over the IP network rather than sending the fax information as a voice call. However, the terminating device must also support Cisco fax relay.

By default, Cisco fax relay is enabled on the VG248. However, follow these steps to disable it:

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose Fax relay .

Step 4 Choose one of the following:

• Enabled

• Disabled

## Reverting to Previous Configuration

By default, the VG48 ports identify their configuration using TFTP. This configuration determines the Cisco CallManager system to which these ports connect.

If persistent TFTP problems prevent the VG248 from retrieving this configuration, the VG248 ports can revert to their previous configuration. This enables the ports to connect to the Cisco CallManager system with which they were previously registered.

By default, the VG248 automatically reverts to the previous configuration if the ports fail to connect via TFTP. To disable this functionality, follow these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose Allow last good configuration .

Step 4 Choose one of the following:

• yes

• no

## Choosing the Call Control Mode

The call control mode determines how users interact with their analog phones to access features such as speed dialing, call transfer, conference, call waiting, and so on.

For assistance determining which call control mode best meets your needs, see the "Understanding Call Control Modes" section .

Follow these steps to set the call control mode:

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose Call control mode .

Step 4 Choose one of the following:

• Basic

• Standard

• Feature

Step 5 Restart the VG248.

## Assigning Feature Codes

Many of the telephony features available in standard and feature mode are activated by feature codes, which end users indicate using the dial pad on their telephones.

You can change these feature codes from their default values using these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose Feature codes .

Step 4 Choose the code to configure.

Step 5 Enter the setting for the code.

The default settings for the feature codes are as follows:

#1

Feature

#2

Feature

#3

Feature

**0

All

**1

All

**2

All

**3

All

*#

All

*0

All

*1

All

*2

All

*3

All

*4

All

*5

All

*6

All

*7

All

*8

All

*9

All

1 When forward all is activated, users hear a distinctive dial tone to indicate that all incoming calls are currently being forwarded to a different directory number.

Tip • If you set a feature code to a blank string, users cannot use that feature.

• You cannot disable transfer or conference in standard mode because those features are activated by hanging up or using the hook flash, rather than by feature codes.

• If you have two feature codes assigned to the same setting, one of the features does not work.

• If one feature code setting masks another, you cannot use the masked setting (such as if transfer is * and conference is **, conference does not work).

## Identifying the Country Code for VG248

The country code identifies the country in which you are using the VG248. It automatically sets country-specific settings, such as the sound of the tones, the cadence of the rings, impedance, hook flash timer, and gain, for example.

Follow these steps to set the country code,

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose Country .

Step 4 Choose the country name in which you are using the VG248.

If your country is not available, select a country that uses the same telephony standards.

Step 5 Restart the VG248.

## Changing the Hook Flash Timer for Analog Phones

The hook flash timer is the length of time before the hook flash indicates a time-out (or call disconnect). The hook flash timer setting is based on the country of origin of the analog phones. When you set the country code on the VG248, the hook flash timer is automatically set to the default for that country.

However, you can modify this setting, if desired.

To change the hook flash timer, follow these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose Hook flash timer .

Step 4 Choose the appropriate hook flash timer value for your analog phones.

## Setting the Port Enable Policy

To configure the ports on the VG248 and the features required for the analog devices connected to the ports, you must add them to the Cisco CallManager database.

The port enable policy on the VG248 determines whether the VG248 can enable a port and register the phone in Cisco CallManager.

Before You Begin

The port enable policy interacts with the auto-registration settings in Cisco CallManager. Review the following explanations before choosing a port enable policy:

auto

auto-registration enabled

1. User picks up the phone to use for first time.

2. VG248 attempts to register in Cisco CallManager

3. Cisco CallManager adds phone to database.

4. User makes call.

auto

auto-registration disabled

1. User picks up the phone to use for first time.

2. VG248 attempts to register in Cisco CallManager

3. Cisco CallManager refuses registration.

4. If phone is not registered, user cannot make call.

If the phone has already been manually added and configured in Cisco CallManager, Cisco CallManager recognizes this, and the phone works.

manual

auto-registration enabled or disabled

1. User picks up the phone to use for first time.

2. VG248 does not attempt to register with Cisco CallManager.

3. User cannot make call.

You can enable the specific port that is connected to this phone. The VG248 will then attempt to register this port with Cisco CallManager. See the "Enabling a Specific Port" section for details.

To set the port enable policy on the VG248, follow these steps:

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose Port enable policy .

Step 4 Choose one of these options:

• auto (default setting)

• manual

## Configuring Port Parameters

You must configure the VG248 ports using Cisco CallManager. Each of the ports are entered in the Cisco CallManager database as a "VGC" phone type. See the "Configuring the VG248 Analog Ports" section for details.

These sections provide details of the parameters that you configure on a per port basis:

• Enabling a Specific Port

• Enabling Caller ID

• Choosing Message Waiting Indicator Type

• Enabling Disconnect Supervision

• Setting the Output Gain

• Setting the Input Gain

Although these procedures describe how to make changes to individual ports, you can configure a range of ports to use the same settings. To do this, choose Telephony > Port specific parameters , and then press R on the keyboard. Then enter a port range (such as 1-10, or 1, 2,3) and apply changes to all of those ports at once.

### Enabling a Specific Port

By enabling a specific port on the VG248, you are allowing it to be registered with Cisco CallManager. When used in conjunction with the port enable policy (see the "Setting the Port Enable Policy" section ), you can determine whether an analog phone can simply be plugged into a port connected to the VG248 and be ready to use.

Before You Begin

Before changing the port enable status for a specific port, review these guidelines to understand how this setting interacts with the port enable policy.

auto

enabled

You have used this phone and registered this port in Cisco CallManager.

auto

disabled

You have either manually disabled the specific port using the Telephony > Port specific parameters menu, or no one has attempted to use a phone connected to this port.

This is the default setting.

After someone attempts to use a phone connected to this port, the port enable status will change to enabled.

manual

enabled

You have manually enabled the specific port using the Telephony > Port specific parameters menu. By doing this, you are overriding the manual setting on the port enable policy.

When the VG248 starts up, the port will attempt to register with Cisco CallManager.

manual

disabled

The port cannot be enabled by picking up the phone. To use the phone, you must manually change the port from disabled to enabled using the Telephony > Port specific parameters menu.

Follow these steps to enable a specific port:

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose Port specific parameters .

Step 4 Use the arrow keys to select the port to configure and press Enter.

Step 5 Choose Status .

Step 6 Choose enabled or disabled .

### Enabling Caller ID

You can enable caller ID on a per-port basis. This allows caller ID information to be passed to some, all, or none of the analog phones connected to the VG248.

Enabling caller ID determines how the VG248 handles any caller ID instructions received from Cisco CallManager. If you are not using caller ID on Cisco CallManager, then the VG248 does not receive any caller information to pass on to the analog ports, regardless how you set the VG248.

To enable caller ID for a specific port on the VG248, follow these instructions:

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose Port specific parameters .

Step 4 Use the arrow keys to select the port to configure and press Enter.

Step 5 Choose Caller ID .

Step 6 Choose from the following options:

• enabled

• not with call waiting— Caller ID displays only if no other calls are currently active

• disabled .

### Choosing Message Waiting Indicator Type

The VG248 supports several types of methods for sending MWI messages to analog phones. Because you might have different types of analog phones connected to the VG248, you can modify the MWI type on a per-port basis. So, if you have some analog phones that have MWI lamps on them, you can notify users of awaiting messages using the lamp. Or, you can choose to play a tone when users pick up their phones.

Keep in mind that the VG248 only sends this information to the phones if it is received from Cisco CallManager. If Cisco CallManager is not integrated with your voice mail system, it does not send this information to the VG248.

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose Port specific parameters .

Step 4 Use the arrow keys to select the port to configure and press Enter.

Step 5 Choose MWI type .

Step 6 Choose from the following options:

• Lamp —illuminates lamp on phone

• Caller ID —uses caller ID mechanism to send MWI messages to the LCD screen on phone

• Stutter —plays tones when user picks up the phone

• Lamp + stutter —illuminates lamp and plays tone

• Caller ID + stutter —sends message to LCD screen and plays tone

• None —does not send MWI information

### Enabling Disconnect Supervision

Disconnect supervision indicates to an analog device that the remote caller has hung up. For example, if a user calls someone with an answering machine, leaves a message, and hangs up, disconnect supervision is the electrical state that briefly drops the loop current and indicates to the answering machine that the caller has hung up.

Follow these steps to enable disconnect supervision on a per port basis:

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose Port specific parameters .

Step 4 Use the arrow keys to select the port to configure and press Enter.

Step 5 Choose Disconnect supervision .

Step 6 Choose from enabled or disabled .

### Setting the Output Gain

The output gain specifies, in decibels, the amount of gain from the VG248 to the analog phone.

The country option you set on the VG248 determines the default output gain. However, you might need to modify it to account for different cable lengths (longer cables might require more gain), to make the signal louder or quieter, or to use a phone from a different country.

Follow these steps to modify the input gain. The default setting is based on the country code you set (see the "Identifying the Country Code for VG248" section ).

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose Port specific parameters .

Step 4 Use the arrow keys to select the port to configure and press Enter.

Step 5 Choose Output gain .

Step 6 Choose from the available options (ranging from -14dB through 0db)

Keep in mind that the value you are choosing is a delta value and does not reflect the actual gain value. For example, if the base value is -3dB, you might choose +1dB as the delta value. Therefore, the actual gain value for that port is -2dB overall.

### Setting the Input Gain

The input gain specifies, in decibels, the amount of gain from the analog phone to the VG248.

The country option you set on the VG248 determines the default input gain. However, you might need to modify it to account for different cable lengths, to make the signal louder or quieter, or to use a phone from a different country.

Follow these steps to modify the input gain. The default setting is based on the country code you set (see the "Identifying the Country Code for VG248" section ).

Step 1 From the main menu, choose Configure .

Step 2 Choose Telephony .

Step 3 Choose Port specific parameters .

Step 4 Use the arrow keys to select the port to configure and press Enter .

Step 5 Choose Input gain .

Step 6 Choose from the available options (ranging from -6dB through + 14db)I

Keep in mind that the value you are choosing is a delta value and does not reflect the actual gain value. For example, if the base value is -3dB, you might choose +1dB as the delta value. Therefore, the actual gain value for that port is -2dB overall.

| Code | Default Setting | Call Mode |
|---|---|---|
| Hang up last call | #1 | Feature |
| Transfer | #2 | Feature |
| Conference | #3 | Feature |
| Forward all to voice mail | **0 | All |
| Call forward all 1 | **1 | All |
| Cancel call forward | **2 | All |
| Pickup | **3 | All |
| Redial | *# | All |
| SpeedDial Voicemail | *0 | All |
| SpeedDial 1 | *1 | All |
| SpeedDial 2 | *2 | All |
| SpeedDial 3 | *3 | All |
| SpeedDial 4 | *4 | All |
| SpeedDial 5 | *5 | All |
| SpeedDial 6 | *6 | All |
| SpeedDial 7 | *7 | All |
| SpeedDial 8 | *8 | All |
| SpeedDial 9 | *9 | All |

| 1 When forward all is activated, users hear a distinctive dial tone to indicate that all incoming calls are currently being forwarded to a different directory number. |
|---|

| VG248 | Cisco CallManager | Analog Phone Behavior | Tips |
|---|---|---|---|
| auto | auto-registration enabled | 1. User picks up the phone to use for first time. 2. VG248 attempts to register in Cisco CallManager 3. Cisco CallManager adds phone to database. 4. User makes call. |  |
| auto | auto-registration disabled | 1. User picks up the phone to use for first time. 2. VG248 attempts to register in Cisco CallManager 3. Cisco CallManager refuses registration. 4. If phone is not registered, user cannot make call. | If the phone has already been manually added and configured in Cisco CallManager, Cisco CallManager recognizes this, and the phone works. |
| manual | auto-registration enabled or disabled | 1. User picks up the phone to use for first time. 2. VG248 does not attempt to register with Cisco CallManager. 3. User cannot make call. | You can enable the specific port that is connected to this phone. The VG248 will then attempt to register this port with Cisco CallManager. See the "Enabling a Specific Port" section for details. |

| Port Enable Policy | Port Enable Status | Explanation |
|---|---|---|
| auto | enabled | You have used this phone and registered this port in Cisco CallManager. |
| auto | disabled | You have either manually disabled the specific port using the Telephony > Port specific parameters menu, or no one has attempted to use a phone connected to this port. This is the default setting. After someone attempts to use a phone connected to this port, the port enable status will change to enabled. |
| manual | enabled | You have manually enabled the specific port using the Telephony > Port specific parameters menu. By doing this, you are overriding the manual setting on the port enable policy. When the VG248 starts up, the port will attempt to register with Cisco CallManager. |
| manual | disabled | The port cannot be enabled by picking up the phone. To use the phone, you must manually change the port from disabled to enabled using the Telephony > Port specific parameters menu. |