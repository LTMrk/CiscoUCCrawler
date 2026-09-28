---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-191-english-admin-guide-at91-b-ata191-admin-guide-at91-b-ata191-admin-g-ee46e5d722
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/191/english/admin-guide/at91_b_ata191-admin-guide/at91_b_ata191-admin-guide_chapter_011.html
retrieved_at: 2026-08-21T20:39:42.896012+00:00
---

Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

# Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

Updated: August 15, 2025

Chapter: Configure the ATA 191

## Chapter: Configure the ATA 191

# Configure the ATA 191

## Telephony Features

The following table lists the supported telephony features. Use Cisco Unified Communications Manager Administration to configure
                           many of these features.

Feature

Description

Configuration Reference

Audible Message Waiting Indicator

A stutter tone from the handset or speakerphone indicates that a user has one or more new voice messages on a line.

The stutter tone is line-specific. You hear it only when using the line with the waiting messages.

For more information, refer to:

Administration Guide for Cisco Unified Communications Manager and IM and Presence Service and IM and Presence Service , “Administration Overview” chapter

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Feature Configuration Guide for Cisco Unified Communications Manager, “ Audible Message Waiting Indicator ” chapter

cBarge

Allows a user to join a nonprivate call on a shared phone line. cBarge adds a user to a call and converts it into a conference,
                                       allowing the user and other parties to access conference features.

Your ATA supports Barge on a conference bridge.

For more information, refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Feature Configuration Guide for Cisco Unified Communications Manager, “ Barge ” chapter

Call forward

Allows users to redirect incoming calls to another number. Call forward options include Call Forward All, Call Forward Busy,
                                       and Call Forward No Answer.

For more information, refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Feature Configuration Guide for Cisco Unified Communications Manager, “ Call Forwarding ” chapter

Call pickup

Allows users to redirect a call that is ringing on another phone within their pickup group to their phone.

For more information, refer to:

Feature Configuration Guide for Cisco Unified Communications Manager, “ Call Pickup ” chapter

Call waiting

Indicates (and allows users to answer) an incoming call that rings while on another call. Displays incoming call information
                                       on the phone screen.

For more information, refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Caller ID

Displays caller identification such as a phone number, name, or other descriptive text on the phone screen.

For more information, refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Administration Guide for Cisco Unified Communications Manager and IM and Presence Service and IM and Presence Service, Cisco Unified IP Phone Configurations.

Conference

Allows a user to talk simultaneously with multiple parties by calling each participant individually. Conference features include
                                             Adhoc Conference, cBarge, and Meet-Me.

Allows a noninitiator in a standard (ad hoc) conference to add or remove participants.

For more information, refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Feature Configuration Guide for Cisco Unified Communications Manager, “ Conferencing Features ” chapter

Direct transfer

Allows users to connect two calls to each other (without remaining on the line).

For more information, refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Feature Configuration Guide for Cisco Unified Communications Manager, “ Call Transfer ” chapter

Forced authorization codes (FAC)

Controls the types of calls that certain users can place.

For more information, refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Feature Configuration Guide for Cisco Unified Communications Manager, “ Speed Dial and Abbreviated Dial ” chapter

Group call pickup

Allows a user to answer a call that is ringing on a directory number in another group.

For more information, refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Feature Configuration Guide for Cisco Unified Communications Manager, “ Call Pickup ” chapter

Hold/Resume

Allows the user to move a connected call between an active state and a held state.

No support for resuming a call from a shared line party.

For more information, refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Feature Configuration Guide for Cisco Unified Communications Manager, “ Secure Tone ” chapter

Meet–Me conference

Allows a user to host a Meet-Me conference in which other participants call a predetermined number at a scheduled time.

For more information, refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Feature Configuration Guide for Cisco Unified Communications Manager, “ Meet-Me Conferencing ” chapter

Message Waiting

Defines directory numbers for message-waiting on and message-waiting off indicator. A directly connected voice-messaging system
                                       uses the specified directory number to set or to clear a message-waiting indication for a particular Cisco Unified IP Phone.

For more information refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Feature Configuration Guide for Cisco Unified Communications Manager, “ Audible Message Waiting Indicator ” chapter

Music on hold

Plays music while callers are on hold.

For more information, refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Feature Configuration Guide for Cisco Unified Communications Manager, “ Music On Hold ” chapter

Privacy

Prevents users who share a line from adding themselves to a call.

For more information refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Feature Configuration Guide for Cisco Unified Communications Manager, “ Privacy ” chapter

Redial

Allows users to call the most recently dialed phone number by pressing the *# feature code.

Requires no configuration.

Shared line

Allows a user to have several devices that share the same phone number or allows a user to share a phone number with a coworker.

For more information, refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Feature Configuration Guide for Cisco Unified Communications Manager, “ Manager Assistant ” chapter

Speed dialing

Allows users to speed dial a phone number by entering * and an assigned index code (1 to 199) on the phone keypad.

Example: Press *199 to dial the phone number with index code 199.

Users assign index codes on Line configuration from the Cisco Unified Communications Manager Device window.

For more information, refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Feature Configuration Guide for Cisco Unified Communications Manager, “ Speed Dial and Abbreviated Dial ” chapter

Time Zone Update

Updates the device with time zone changes.

For more information, refer to:

System Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

Voice-messaging system

Enables callers to leave messages if calls are unanswered.

For more information refer to:

System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter

## Product-Specific Configuration Parameters

Cisco Unified Communications Manager Administration allows you to set some product-specific configuration parameters for the
                              ATA 191. The following table lists the configuration windows and their paths to configure the parameters.

Configuration Window

Path

Phone Configuration window

Device > Phone ; Product Specific Configuration portion of window

The following table lists the configuration parameters you can set using Cisco Unified Communications Manager Administration.
                              You can set the configuration parameters using the Phone configuration window. Options with an asterisk in the window are
                              required.

Set the following ATA 191 parameters from port 1 only: IVR Password, CDP, Impedance, Input/Output Audio Level, Timers, Call
                                          Sequence, Ring1 Cadence, Ring2 Cadence, CPC Delay, CPC Duration, and MTU Size. Setting these parameters from port 2 has no
                                          effect.

Parameter

Description

Default: Enabled

Web Access

Enable the ATA 191 to accept web connections or an HTTP client. If this option is disabled, then access to the ATA 191's internal
                                          web page is blocked. In addition, the Problem Report Tool (PRT) is disabled.

Default: Disabled

HTTPS Server

Enable both HTTPS and HTTP connections to the ATA 191, or restrict connections to HTTPS only.

Default: HTTPS and HTTP

Admin Password*

Set the password to access the Web Administrator interface.

The password can be from 8 to 127 characters.

SSH Access

Set whether the ATA 191 accepts SSH connections. If you block SSH connections, then access to the ATA 191 is blocked.

Default: Disabled

Cisco Discovery Protocol (CDP)

Enable or disable the CDP function of the ATA 191.

Default: Enabled

Link Layer Discovery Protocol (LLDP)

Enable or disable LLDP on the ATA 191.

Default: Enabled

LLDP Asset ID

Set the Asset ID from LLDP. The maximum length is 32.

802.1x Authentication

Enable or disable the 802.1x authentication.

Default: User Controlled

If the parameter is set to User Controlled, the feature is disabled on the ATA. User needs to enable it through the IVR setting
                                          on the phone that is connected to the ATA. For other values (Enabled or Disabled), the setting in CUCM takes preference.

Log Server

If using IPv4, specify an IP address and port of a remote system where log messages are sent.

IPv6 Log Server

If using IPv6, specify an IP address and port of a remote system where log messages are sent.

Remote Log

Specify where to send the log data by serviceability. If enabled, log data is copied to the location specified by the Log
                                          Server or IPv6 Log Server parameters. If disabled, log data is not copied to the log server location.

Default: Disabled

Log Profile

Default—Resets the debug level to default.

Preset—Use log module settings on Phone Adapter Configuration Utility for debug flags.

Telephony—Turn on debug flag for provisioning (including auto upgrade) and call features.

SIP—Turn on debug flag for SIP messages.

UI—Turn on debug flag for key event such as DTMF, PRT, and reset button.

Network—Turn on debug flag for network events, such as DHCP, VLAN, link status change.

Media—Turn on debug flags for RTP, Fax, Tone, and SLIC-related issues.

System—Turn on debug flag for system events, such as reboot, or factory reset.

Web—Turn on debug flag for web operation and event logs.

NTP—Turn on debug flag for NTP related logs.

CDPLLDP—Turn on debug flag for CDP and LLDP logs.

Security—Turn on debug flag for security related logs.

Load Server

If using IPv4, the ATA uses an alternative server to obtain firmware loads and upgrades, rather than the defined TFTP server.

IPv6 Load Server

If using IPv6, the ATA uses an alternate server to obtain firmware loads and upgrades, rather than the defined TFTP server.

Auto Barge

Auto Barge adds a user to an active call. An offhook phone automatically adds the user (initiator) to the shared line call
                                          (target), and the users currently on the call receive a tone (if configured). Barge supports conference bridges.

Echo Cancellation

Enable or Disable the use of echo canceler.

Fax Mode

The Cisco ATA 191 supports these fax modes:

Fax Pass-Through–Allows fax and modem traffic to pass through a voice port using the re-INVITE method (codec can be g711ulaw
                                                or g711alaw).

NSE Fax Pass-through g711ulaw–Allows fax traffic to pass through a voice port using the NSE method by codec g711ulaw.

NSE Fax Pass-through g711alaw–Allows fax traffic to pass through a voice port using the NSE method by codec g711alaw.

T.38 Fax Relay–Allows for a quicker protocol for fax transmission over packet networks.

Fax Error Correction Mode Override

You can set the fax error correction mode override values to one of the following settings:

Default

On

Off

FAX Disable ECAN

Set this parameter to yes to automatically disable Echo Canceler when FAX tone is detected.

Modem Line

If you set this parameter to yes , the call is treated as a modem call. The ATA191 tunes VAD, Jitter buffer, and echo canceler automatically.

Fax T38 Return To Voice

Set this parameter yes if voice callback is needed after the T.38 fax is completed.

Fax Tone Detect Mode

This option controls which side detects fax tone (trigger fax):

Caller Or Callee

Caller Only

Callee Only

The default is Caller Or Callee.

IVR Password

ATA 191 IVR password.

Input Audio Level

Gain value of Network-to-Phone

Output Audio Level

Gain value of Phone-to-Network

Impedance

The ATA 191 provides multiple impedance values, such as 600ohm for use in the United States.

Caller Connect Polarity

Control the line polarity of the Cisco ATA FXS ports when Cisco ATA is the caller and a call is connected.

Default: User forward polarity

Caller Disconnect Polarity

Control the line polarity of the Cisco ATA FXS ports when Cisco ATA is the caller and a call is disconnected.

Default: User forward polarity

Callee Connect Polarity

Control the line polarity of the Cisco ATA FXS ports when Cisco ATA is the callee and a call is connected.

Default: User forward polarity

Callee Disconnect Polarity

Control the line polarity of the Cisco ATA FXS ports when Cisco ATA is the callee and a call is disconnected.

Default: User forward polarity

Caller ID

BT FSK

Bellcore FSK

ETSI FSK

Call Sequence

Bellcore FSK

ETSI FSK

Mute Progress Tone

Set this parameter to On to mute all progress tones on the Cisco ATA 191 during call establishment.

Default setting: Off.

Ring1 Cadence

Cadence script for distinctive ring pattern.

Default setting: 60(2/4).

Ring2 Cadence

Cadence script for the alternative ring pattern triggered by SIP message.

Default setting: 60(.8/.4,.8/4).

CPC Delay (0-255s)

CPC(Calling Party Control) delay time in seconds after caller hangs up when the ATA 191 starts removing the tip-and-ring voltage
                                          to the attached equipment of the called party.

When remote party hangs up, without CPC enabled, reorder tone will be played after a configurable delay. If CPC is enabled,
                                                      dial tone will be played when tip-to-ring voltage is restored.

Value range: 0–255(s).

Default setting: 2(s)

CPC Duration (0-1.000s)

CPC(Calling Party Control) duration time in seconds for which the tip-to-ring voltage is removed after the caller hangs up.
                                          After that, the tip-to-ring voltage is restored and dial tone will apply if the attached equipment is still off hook. CPC
                                          is disabled if this value is set to 0.

When remote party hangs up, without CPC enabled, reorder tone will be played after a configurable delay. If CPC is enabled,
                                                      dial tone will be played when tip-to-ring voltage is restored.

Value range: 0-1.000(s).

Default setting: 0(s)

MTU Size (576-1500)

Maximum Transmission Unit (MTU) size that can be communicated in a single network layer transaction. For IPv4 only mode case,
                                          the MTU size can be set from 576 to 1500; for dual mode case, the MTU size can be set from 1281 to 1500.

Value range: 576–1500

Default setting: 1500

Ring and Call Waiting Tone Specs

Ring Waveform

Waveform for the ringing signal.

Choices are Sinusoid or Trapezoid.

Default setting: Trapezoid.

Ring Frequency(15-50Hz)

Frequency of the ringing signal.

Value range: 15-50 (Hz).

Default setting: 20.

Ring Voltage(60-90V)

Voltage of the ringing signal.

Value range: 60-90 (V).

Default setting: 85.

Timers

Offhook Validation Timer

(50-1000ms)

Indicates the time to validate an offhook event.

Onhook Validation Timer

(50-1000ms)

Indicates the time to validate an onhook event.

Hookflash Timer

(100 to 1500ms)

Indicates the time to validate a hookflash event.

Onhook Delay Timer

(0 to 155ms)

Indicates the time to delay an onhook event.

Reorder Delay (0-30s)

Delay after far end hangs up before reorder tone is played.

RTP Packet Time (10-90ms)

Packet size in milliseconds for RTP.

Default setting: 20.

You can access the ATA 191 web page and perform limited configuration. In Admin mode, most information and settings are available.

## Add Users to Cisco Unified Communications Manager

Adding users to Cisco Unified Communications Manager allows you to display and maintain information about users. Each added
                           user can perform these tasks:

Access the corporate directory and other customized directories from an ATA 191.

Create a personal directory.

Set up speed dial and call forwarding numbers.

Subscribe to services that are accessible from an ATA 191.

You can add users to Cisco Unified Communications Manager using this method:

To add users individually, choose User Management > End User from Cisco Unified Communications Manager Administration.

Refer to the Administration Guide for Cisco Unified Communications Manager and IM and Presence Service for more information about adding users. Refer to the System Configuration Guide for Cisco Unified Communications Manager for details about the user information.

## Emergency Call Support Background

Emergency call service providers can register an ATA's location for each IP-based phone in a company. The location information
                              server (LIS) transfers the emergency response location (ERL) to the ATA. The ATA stores its location during registration,
                              after the ATA restarts. The location entry can specify the street address, building number, floor, room, and other office
                              location information.

When you place an emergency call, the ATA transfers the location to the call server. The call server forwards the call and
                              the location to the emergency call service provider. The emergency call service provider forwards the call and a unique call-back
                              number (ELIN) to the emergency services. The emergency service or public safety answering point (PSAP) receives the ATA's
                              location. The PSAP also receives a number to call you back, if the call disconnects.

See Emergency Call Support Terminology for the terms used to describe emergency calls from the phone.

The phone requests new location information for the following activities:

You register the ATA with the call server.

You or the user restarts the ATA and the ATA was previously registered with the call server.

You change the network interface used in the SIP registration.

You change the IP address of the ATA.

If both of the location servers do not send a location response, the phone resends the location request every two minutes.

### Emergency Call Support Terminology

The following terms describe emergency call support for the ATA.

Emergency Location ID Number (ELIN)–A number used to represent one or more ATA lines that locate the person who dialed emergency
                                       services.

Emergency Response Location (ERL)–A logical location that groups a set of ATA lines.

HTTP Enabled Location Delivery (HELD)–An encrypted protocol that obtains the PIDF-LO location for the ATA from a location
                                       information server (LIS).

Location Information Server (LIS)–A server that responds to a SIP-based ATA HELD request and provides the ATA location using
                                       a HELD XML response.

Emergency Call Service Provider–The company that responds to an ATA HELD request with the ATA's location. When you make an
                                       emergency call (which carries the ATA's location), a call server routes the call to this company. The emergency call service
                                       provider adds an ELIN and routes the call to the emergency services (PSAP). If the call is disconnected, the PSAP uses the
                                       ELIN to reconnect with the ATA used to make the emergency call.

Public Safety Answering Point (PSAP)–Any emergency service (for example, fire, police, or ambulance) joined to the Emergency
                                       Services IP Network.

Universally Unique Identifier (UUID)–A 128-bit number used to uniquely identify a company using emergency call support.

### Configure the ATA to Make Emergency Calls

#### Before you begin

Obtain an E911 location URL and a company ID for the ATA from your emergency calling service provider (for example, Redsky
                                 admin). You can use the same location URL and company ID for PHONE1 and PHONE2.

Step 1

Sign into On Cisco Communication Manager Administration as an administrator.

Step 2

Configure a service profile:

Select User Management > > User Settings > Service Profile .

Create a new service profile with a unique name. For example, "Emergency Calling Profile".

Configure the fields in the section Emergency Calling Profile .

The Organization ID , Secret , and Location Url are provided by your emergency calling service provider.

For Emergency Numbers , enter the emergency service numbers, separated by commas. For example, 911,933

Click Save .

Step 3

Associate an end user with the created service profile:

Select User Management > End User .

Create a new user or modify an existing user.

In the Service Settings section, select the service profile that you created from the UC Service Profile drop-down list.

Click Save .

Step 4

Associate a phone with the created or modified user:

Select Device > Phone to find an existing phone.

In the Device Information section, select User for the Owner field, and then select the user from the Owner User ID drop-down list.

Click Save .

Step 5

Create or modify an SIP dial rule for the emergency number:

Select Call Routing > Dial Rules > SIP Dial Rules .

Create a new SIP dial rule or modify an existing one.

If you choose to create a new SIP dial rule, select 7940_7960_OTHER from the Dial Pattern drop-down list.

Enter a name and relevant descriptions for the SIP dial rule.

In the Pattern Information section, add patterns of the emergency number (such as, "911" and "933").

Click Save .

Step 6

Associate a phone with the created or modified SIP dial rule:

Select Device > Phone .

In the Protocol Specific Information section, select the SIP dial rule from the SIP Dial Rules drop-down list.

Click Save .

Step 7

Verify the E911 configurations on the ATA web page:

Select Voice > Line <n> .

Go to the section Call Feature Settings , check whether the parameter Emergency Number is configured as expected.

Go to the section E911 Geolocation Configuration , check whether the parameters are configured as expected.

Go to the section Dial Plan , chech whether the parameter is configured as expected.

| Feature | Description | Configuration Reference |
|---|---|---|
| Audible Message Waiting Indicator | A stutter tone from the handset or speakerphone indicates that a user has one or more new voice messages on a line. Note The stutter tone is line-specific. You hear it only when using the line with the waiting messages. | Note | The stutter tone is line-specific. You hear it only when using the line with the waiting messages. | For more information, refer to: Administration Guide for Cisco Unified Communications Manager and IM and Presence Service and IM and Presence Service , “Administration Overview” chapter System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter Feature Configuration Guide for Cisco Unified Communications Manager, “ Audible Message Waiting Indicator ” chapter |
| Note | The stutter tone is line-specific. You hear it only when using the line with the waiting messages. |
| cBarge | Allows a user to join a nonprivate call on a shared phone line. cBarge adds a user to a call and converts it into a conference,
                                       allowing the user and other parties to access conference features. Your ATA supports Barge on a conference bridge. | For more information, refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter Feature Configuration Guide for Cisco Unified Communications Manager, “ Barge ” chapter |
| Call forward | Allows users to redirect incoming calls to another number. Call forward options include Call Forward All, Call Forward Busy,
                                       and Call Forward No Answer. | For more information, refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter Feature Configuration Guide for Cisco Unified Communications Manager, “ Call Forwarding ” chapter |
| Call pickup | Allows users to redirect a call that is ringing on another phone within their pickup group to their phone. | For more information, refer to: Feature Configuration Guide for Cisco Unified Communications Manager, “ Call Pickup ” chapter |
| Call waiting | Indicates (and allows users to answer) an incoming call that rings while on another call. Displays incoming call information
                                       on the phone screen. | For more information, refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter |
| Caller ID | Displays caller identification such as a phone number, name, or other descriptive text on the phone screen. | For more information, refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter Administration Guide for Cisco Unified Communications Manager and IM and Presence Service and IM and Presence Service, Cisco Unified IP Phone Configurations. |
| Conference | Allows a user to talk simultaneously with multiple parties by calling each participant individually. Conference features include
                                             Adhoc Conference, cBarge, and Meet-Me. Allows a noninitiator in a standard (ad hoc) conference to add or remove participants. | For more information, refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter Feature Configuration Guide for Cisco Unified Communications Manager, “ Conferencing Features ” chapter |
| Direct transfer | Allows users to connect two calls to each other (without remaining on the line). | For more information, refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter Feature Configuration Guide for Cisco Unified Communications Manager, “ Call Transfer ” chapter |
| Forced authorization codes (FAC) | Controls the types of calls that certain users can place. | For more information, refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter Feature Configuration Guide for Cisco Unified Communications Manager, “ Speed Dial and Abbreviated Dial ” chapter |
| Group call pickup | Allows a user to answer a call that is ringing on a directory number in another group. | For more information, refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter Feature Configuration Guide for Cisco Unified Communications Manager, “ Call Pickup ” chapter |
| Hold/Resume | Allows the user to move a connected call between an active state and a held state. Note No support for resuming a call from a shared line party. | Note | No support for resuming a call from a shared line party. | For more information, refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter Feature Configuration Guide for Cisco Unified Communications Manager, “ Secure Tone ” chapter |
| Note | No support for resuming a call from a shared line party. |
| Meet–Me conference | Allows a user to host a Meet-Me conference in which other participants call a predetermined number at a scheduled time. | For more information, refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter Feature Configuration Guide for Cisco Unified Communications Manager, “ Meet-Me Conferencing ” chapter |
| Message Waiting | Defines directory numbers for message-waiting on and message-waiting off indicator. A directly connected voice-messaging system
                                       uses the specified directory number to set or to clear a message-waiting indication for a particular Cisco Unified IP Phone. | For more information refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter Feature Configuration Guide for Cisco Unified Communications Manager, “ Audible Message Waiting Indicator ” chapter |
| Music on hold | Plays music while callers are on hold. | For more information, refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter Feature Configuration Guide for Cisco Unified Communications Manager, “ Music On Hold ” chapter |
| Privacy | Prevents users who share a line from adding themselves to a call. | For more information refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter Feature Configuration Guide for Cisco Unified Communications Manager, “ Privacy ” chapter |
| Redial | Allows users to call the most recently dialed phone number by pressing the *# feature code. | Requires no configuration. |
| Shared line | Allows a user to have several devices that share the same phone number or allows a user to share a phone number with a coworker. | For more information, refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter Feature Configuration Guide for Cisco Unified Communications Manager, “ Manager Assistant ” chapter |
| Speed dialing | Allows users to speed dial a phone number by entering * and an assigned index code (1 to 199) on the phone keypad. Example: Press *199 to dial the phone number with index code 199. Users assign index codes on Line configuration from the Cisco Unified Communications Manager Device window. | For more information, refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter Feature Configuration Guide for Cisco Unified Communications Manager, “ Speed Dial and Abbreviated Dial ” chapter |
| Time Zone Update | Updates the device with time zone changes. | For more information, refer to: System Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter |
| Voice-messaging system | Enables callers to leave messages if calls are unanswered. | For more information refer to: System Configuration Guide for Cisco Unified Communications Manager, “ Configure Analog Telephone Adapters ” chapter |

| Note | The stutter tone is line-specific. You hear it only when using the line with the waiting messages. |
|---|---|

| Note | No support for resuming a call from a shared line party. |
|---|---|

| Configuration Window | Path |
|---|---|
| Phone Configuration window | Device > Phone ; Product Specific Configuration portion of window |

| Note | Set the following ATA 191 parameters from port 1 only: IVR Password, CDP, Impedance, Input/Output Audio Level, Timers, Call
                                          Sequence, Ring1 Cadence, Ring2 Cadence, CPC Delay, CPC Duration, and MTU Size. Setting these parameters from port 2 has no
                                          effect. |
|---|---|

| Parameter | Description |
|---|---|
| Line 2 Support | Enable and disable the Phone 2 port on the ATA 191. Default: Enabled |
| Web Access | Enable the ATA 191 to accept web connections or an HTTP client. If this option is disabled, then access to the ATA 191's internal
                                          web page is blocked. In addition, the Problem Report Tool (PRT) is disabled. Default: Disabled |
| HTTPS Server | Enable both HTTPS and HTTP connections to the ATA 191, or restrict connections to HTTPS only. Default: HTTPS and HTTP |
| Admin Password* | Set the password to access the Web Administrator interface. The password can be from 8 to 127 characters. |
| SSH Access | Set whether the ATA 191 accepts SSH connections. If you block SSH connections, then access to the ATA 191 is blocked. Default: Disabled |
| Cisco Discovery Protocol (CDP) | Enable or disable the CDP function of the ATA 191. Default: Enabled |
| Link Layer Discovery Protocol (LLDP) | Enable or disable LLDP on the ATA 191. Default: Enabled |
| LLDP Asset ID | Set the Asset ID from LLDP. The maximum length is 32. |
| 802.1x Authentication | Enable or disable the 802.1x authentication. Default: User Controlled If the parameter is set to User Controlled, the feature is disabled on the ATA. User needs to enable it through the IVR setting
                                          on the phone that is connected to the ATA. For other values (Enabled or Disabled), the setting in CUCM takes preference. |
| Log Server | If using IPv4, specify an IP address and port of a remote system where log messages are sent. |
| IPv6 Log Server | If using IPv6, specify an IP address and port of a remote system where log messages are sent. |
| Remote Log | Specify where to send the log data by serviceability. If enabled, log data is copied to the location specified by the Log
                                          Server or IPv6 Log Server parameters. If disabled, log data is not copied to the log server location. Default: Disabled |
| Log Profile | Run the pre-defined debug command remotely: Default—Resets the debug level to default. Preset—Use log module settings on Phone Adapter Configuration Utility for debug flags. Telephony—Turn on debug flag for provisioning (including auto upgrade) and call features. SIP—Turn on debug flag for SIP messages. UI—Turn on debug flag for key event such as DTMF, PRT, and reset button. Network—Turn on debug flag for network events, such as DHCP, VLAN, link status change. Media—Turn on debug flags for RTP, Fax, Tone, and SLIC-related issues. System—Turn on debug flag for system events, such as reboot, or factory reset. Web—Turn on debug flag for web operation and event logs. NTP—Turn on debug flag for NTP related logs. CDPLLDP—Turn on debug flag for CDP and LLDP logs. Security—Turn on debug flag for security related logs. |
| Customer support upload URL | Provides the URL for the Problem Report Tool (PRT). |
| Load Server | If using IPv4, the ATA uses an alternative server to obtain firmware loads and upgrades, rather than the defined TFTP server. |
| IPv6 Load Server | If using IPv6, the ATA uses an alternate server to obtain firmware loads and upgrades, rather than the defined TFTP server. |
| Auto Barge | Auto Barge adds a user to an active call. An offhook phone automatically adds the user (initiator) to the shared line call
                                          (target), and the users currently on the call receive a tone (if configured). Barge supports conference bridges. |
| Echo Cancellation | Enable or Disable the use of echo canceler. |
| Fax Mode | The Cisco ATA 191 supports these fax modes: Fax Pass-Through–Allows fax and modem traffic to pass through a voice port using the re-INVITE method (codec can be g711ulaw
                                                or g711alaw). NSE Fax Pass-through g711ulaw–Allows fax traffic to pass through a voice port using the NSE method by codec g711ulaw. NSE Fax Pass-through g711alaw–Allows fax traffic to pass through a voice port using the NSE method by codec g711alaw. T.38 Fax Relay–Allows for a quicker protocol for fax transmission over packet networks. |
| Fax Error Correction Mode Override | You can set the fax error correction mode override values to one of the following settings: Default On Off |
| FAX Disable ECAN | Set this parameter to yes to automatically disable Echo Canceler when FAX tone is detected. |
| Modem Line | If you set this parameter to yes , the call is treated as a modem call. The ATA191 tunes VAD, Jitter buffer, and echo canceler automatically. |
| Fax T38 Return To Voice | Set this parameter yes if voice callback is needed after the T.38 fax is completed. |
| Fax Tone Detect Mode | This option controls which side detects fax tone (trigger fax): Caller Or Callee Caller Only Callee Only The default is Caller Or Callee. |
| IVR Password | ATA 191 IVR password. |
| Input Audio Level | Gain value of Network-to-Phone |
| Output Audio Level | Gain value of Phone-to-Network |
| Impedance | The ATA 191 provides multiple impedance values, such as 600ohm for use in the United States. |
| Caller Connect Polarity | Control the line polarity of the Cisco ATA FXS ports when Cisco ATA is the caller and a call is connected. Default: User forward polarity |
| Caller Disconnect Polarity | Control the line polarity of the Cisco ATA FXS ports when Cisco ATA is the caller and a call is disconnected. Default: User forward polarity |
| Callee Connect Polarity | Control the line polarity of the Cisco ATA FXS ports when Cisco ATA is the callee and a call is connected. Default: User forward polarity |
| Callee Disconnect Polarity | Control the line polarity of the Cisco ATA FXS ports when Cisco ATA is the callee and a call is disconnected. Default: User forward polarity |
| Caller ID | BT FSK Bellcore FSK ETSI FSK |
| Call Sequence | Bellcore FSK ETSI FSK |
| Mute Progress Tone | Set this parameter to On to mute all progress tones on the Cisco ATA 191 during call establishment. Default setting: Off. |
| Ring1 Cadence | Cadence script for distinctive ring pattern. Default setting: 60(2/4). |
| Ring2 Cadence | Cadence script for the alternative ring pattern triggered by SIP message. Default setting: 60(.8/.4,.8/4). |
| CPC Delay (0-255s) | CPC(Calling Party Control) delay time in seconds after caller hangs up when the ATA 191 starts removing the tip-and-ring voltage
                                          to the attached equipment of the called party. Note When remote party hangs up, without CPC enabled, reorder tone will be played after a configurable delay. If CPC is enabled,
                                                      dial tone will be played when tip-to-ring voltage is restored. Value range: 0–255(s). Default setting: 2(s) | Note | When remote party hangs up, without CPC enabled, reorder tone will be played after a configurable delay. If CPC is enabled,
                                                      dial tone will be played when tip-to-ring voltage is restored. |
| Note | When remote party hangs up, without CPC enabled, reorder tone will be played after a configurable delay. If CPC is enabled,
                                                      dial tone will be played when tip-to-ring voltage is restored. |
| CPC Duration (0-1.000s) | CPC(Calling Party Control) duration time in seconds for which the tip-to-ring voltage is removed after the caller hangs up.
                                          After that, the tip-to-ring voltage is restored and dial tone will apply if the attached equipment is still off hook. CPC
                                          is disabled if this value is set to 0. Note When remote party hangs up, without CPC enabled, reorder tone will be played after a configurable delay. If CPC is enabled,
                                                      dial tone will be played when tip-to-ring voltage is restored. Value range: 0-1.000(s). Default setting: 0(s) | Note | When remote party hangs up, without CPC enabled, reorder tone will be played after a configurable delay. If CPC is enabled,
                                                      dial tone will be played when tip-to-ring voltage is restored. |
| Note | When remote party hangs up, without CPC enabled, reorder tone will be played after a configurable delay. If CPC is enabled,
                                                      dial tone will be played when tip-to-ring voltage is restored. |
| MTU Size (576-1500) | Maximum Transmission Unit (MTU) size that can be communicated in a single network layer transaction. For IPv4 only mode case,
                                          the MTU size can be set from 576 to 1500; for dual mode case, the MTU size can be set from 1281 to 1500. Value range: 576–1500 Default setting: 1500 |
| Ring and Call Waiting Tone Specs |
| Ring Waveform | Waveform for the ringing signal. Choices are Sinusoid or Trapezoid. Default setting: Trapezoid. |
| Ring Frequency(15-50Hz) | Frequency of the ringing signal. Value range: 15-50 (Hz). Default setting: 20. |
| Ring Voltage(60-90V) | Voltage of the ringing signal. Value range: 60-90 (V). Default setting: 85. |
| Timers |
| Offhook Validation Timer (50-1000ms) | Indicates the time to validate an offhook event. |
| Onhook Validation Timer (50-1000ms) | Indicates the time to validate an onhook event. |
| Hookflash Timer (100 to 1500ms) | Indicates the time to validate a hookflash event. |
| Onhook Delay Timer (0 to 155ms) | Indicates the time to delay an onhook event. |
| Reorder Delay (0-30s) | Delay after far end hangs up before reorder tone is played. |
| RTP Packet Time (10-90ms) | Packet size in milliseconds for RTP. Default setting: 20. |

| Note | When remote party hangs up, without CPC enabled, reorder tone will be played after a configurable delay. If CPC is enabled,
                                                      dial tone will be played when tip-to-ring voltage is restored. |
|---|---|

| Note | When remote party hangs up, without CPC enabled, reorder tone will be played after a configurable delay. If CPC is enabled,
                                                      dial tone will be played when tip-to-ring voltage is restored. |
|---|---|

| Step 1 | Sign into On Cisco Communication Manager Administration as an administrator. |
|---|---|
| Step 2 | Configure a service profile: Select User Management > > User Settings > Service Profile . Create a new service profile with a unique name. For example, "Emergency Calling Profile". Configure the fields in the section Emergency Calling Profile . The Organization ID , Secret , and Location Url are provided by your emergency calling service provider. For Emergency Numbers , enter the emergency service numbers, separated by commas. For example, 911,933 Click Save . |
| Step 3 | Associate an end user with the created service profile: Select User Management > End User . Create a new user or modify an existing user. In the Service Settings section, select the service profile that you created from the UC Service Profile drop-down list. Click Save . |
| Step 4 | Associate a phone with the created or modified user: Select Device > Phone to find an existing phone. In the Device Information section, select User for the Owner field, and then select the user from the Owner User ID drop-down list. Click Save . |
| Step 5 | Create or modify an SIP dial rule for the emergency number: Select Call Routing > Dial Rules > SIP Dial Rules . Create a new SIP dial rule or modify an existing one. If you choose to create a new SIP dial rule, select 7940_7960_OTHER from the Dial Pattern drop-down list. Enter a name and relevant descriptions for the SIP dial rule. In the Pattern Information section, add patterns of the emergency number (such as, "911" and "933"). Click Save . |
| Step 6 | Associate a phone with the created or modified SIP dial rule: Select Device > Phone . In the Protocol Specific Information section, select the SIP dial rule from the SIP Dial Rules drop-down list. Click Save . |
| Step 7 | Verify the E911 configurations on the ATA web page: Select Voice > Line <n> . Go to the section Call Feature Settings , check whether the parameter Emergency Number is configured as expected. Go to the section E911 Geolocation Configuration , check whether the parameters are configured as expected. Go to the section Dial Plan , chech whether the parameter is configured as expected. |