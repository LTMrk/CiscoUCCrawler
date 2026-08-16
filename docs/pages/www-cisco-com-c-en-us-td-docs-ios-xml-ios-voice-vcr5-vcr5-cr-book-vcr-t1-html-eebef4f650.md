---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr5-vcr5-cr-book-vcr-t1-html-eebef4f650
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr5/vcr5-cr-book/vcr-t1.html
retrieved_at: 2026-08-16T23:15:58.865147+00:00
---

Cisco IOS Voice Command Reference - T through Z

# Cisco IOS Voice Command Reference - T through Z

Updated: April 25, 2026

Chapter: target carrier-id through timeout tsmax

## Chapter: target carrier-id through timeout tsmax

# target carrier-id through timeout tsmax

## target carrier-id

The documentation set for this product strives to use bias-free language. For purposes of this documentation set, bias-free
                                          is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity,
                                          sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language
                                          that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that
                                          is used by a referenced third-party product.

To configure debug filtering for the target carrier ID, use the target carrier-id command in call filter match list configuration mode. To disable, use the no form of this command.

target carrier-id string

no target carrier-id string

### Syntax Description

string

Alphanumeric identifier for the carrier ID.

### Command Default

No default behavior or values

### Command Modes

Call filter match list configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example shows the voice call debug filter set to match target carrier ID 4321:

```
call filter match-list 1 voice
 target carrier-id 4321
```

### Related Commands

Command

Description

call filter match-list voice

Create a call filter match list for debugging voice calls.

debug condition match-list

Run a filtered debug on a voice call.

show call filter match-list

Display call filter match lists.

source carrier-id

Configure debug filtering for the source carrier ID.

source trunk-group-label

Configure debug filtering for a source trunk group.

target trunk-group-label

Configure debug filtering for a target trunk group.

## target trunk-group-label

To configure debug filtering for a target trunk group, use the target trunk-group-label command in call filter match list configuration mode. To disable, use the no form of this command.

target trunk-group-label group-number

no target trunk-group-label group-number

### Syntax Description

group-number

A value from 0 to 23 that identifies the trunk group.

### Command Default

No default behavior or values

### Command Modes

Call filter match list configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example shows the voice call debug filter set to match target trunk group 21:

```
call filter match-list 1 voice
 target trunk-group-label 21
```

### Related Commands

Command

Description

call filter match-list voice

Create a call filter match list for debugging voice calls.

debug condition match-list

Run a filtered debug on a voice call.

show call filter match-list

Display call filter match lists.

source carrier-id

Configure debug filtering for the source carrier ID.

source trunk-group-label

Configure debug filtering for a source trunk group.

target carrier-id

Configure debug filtering for the target carrier ID.

## tbct clear call

To terminate billing statistics for one or more active Two B-Channel Transfer (TBCT) calls, use the tbct clear call command in privileged EXEC mode.

tbct clear call { all | interface [call-tag] }

### Syntax Description

all

Active TBCT calls on all interfaces.

interface

Active TBCT calls on a specified interface. Range is platform-dependent.

call - tag

(Optional) A specific active TBCT call on the specified interface, as identified by the unique call tag number. Range is 1
                                          to 4,294,967,295.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

Use this command to manually clear a specific active call or a group of active calls, if, for instance, the ISDN switch goes
                                    down. You should not have to manually clear calls with this command unless there is a problem with the switch.

This command terminates billing information that is being sent to the RADIUS server if, for some reason, the gateway did not
                                    receive a notify message from the switch that a call has cleared.

To automatically clear calls after a specified duration, use the tbct max call-duration command.

To determine the interface and call - tag arguments to use with this command, use the show call active voice redirect command.

## Examples

The following example clears calls on T1 interface 6/0:

```
Router# tbct clear call T1-6/0
```

### Related Commands

Command

Description

isdn supp - service tbct

Enables ISDN TBCT on PRI trunks.

show call active voice redirect

Displays information about active calls that are being redirected using RTPvt or TBCT.

tbct max call - duration

Sets the maximum duration allowed for a call that is redirected using TBCT.

tbct max calls

Sets the maximum number of active calls that can use TBCT.

## tbct max call-duration

To set the maximum duration allowed for a call that is redirected using Two B-Channel Transfer (TBCT), use the tbct max call - duration command in global configuration mode. To reset to the default, use the no form of this command.

tbct max call-duration minutes

no tbct max call-duration

### Syntax Description

minutes

Maximum duration, in minutes, allowed for a single TBCT call. Range is 1 to 9999, in recommended increments of 5 minutes.
                                          Default is no limit.

### Command Default

No limit

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

Use this command to automatically clear stale calls, for instance if the PRI trunk goes down. To manually clear calls, use
                                    the tbct clear call command.

Cisco recommends that you set the call duration in increments of 5 minutes.

The call duration limit set by this command is not precisely enforced; calls may not be cleared after the exact number of
                                          minutes specified by this command.

## Examples

The following example clears TBCT calls that last longer than 10 minutes:

```
tbct max call-duration 10
```

### Related Commands

Command

Description

isdn supp - service tbct

Enables ISDN TBCT on PRI trunks.

show call active voice redirect

Displays information about active calls that are being redirected using RTPvt or TBCT.

tbct clear call

Terminates billing statistics for one or more active TBCT calls.

tbct max calls

Sets the maximum number of active calls that can use TBCT.

## tbct max calls

To set the maximum number of active calls that can use Two B-Channel Transfer (TBCT), use the tbct max calls command in global configuration mode. To reset to the default, use the no form of this command.

tbct max calls number

no tbct max calls

### Syntax Description

number

Maximum number of currently active calls that can invoke TBCT at any one time. Range is 1 to 1,000,00. Default is no limit.

### Command Default

No limit, except as allowed by memory resources

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

Use this command to control memory resources on the gateway by limiting the amount of memory consumed by TBCT calls.

## Examples

The following example sets the maximum number of calls using TBCT to 500:

```
tbct max calls 500
```

### Related Commands

Command

Description

isdn supp - service tbct

Enables ISDN TBCT on PRI trunks.

show call active voice redirect

Displays information about active calls that are being redirected using RTPvt or TBCT.

tbct clear call

Terminates billing statistics for one or more active TBCT calls.

tbct max call - duration

Sets the maximum duration allowed for a call that is redirected using TBCT.

## tcp-retry

To configure the maximum number of retry attempts for sending
                              		  messages from the SIP-TCP connection, use the tcp-retry command in SIP user-agent
                              		  configuration mode. To reset to the default value, use the no form of this command.

tcp-retry { count close-connection | | nolimit }

no tcp-retry

### Syntax Description

count

Count range is 100-2000. Default retry count is 200.

close-connection

(Optional) Closes the connections after the configured
                                          						number of retries.

nolimit

Retry value is set to unlimited.

### Command Default

TCP retry count is 200.

### Command Modes

SIP user-agent configuration (config-sip-ua)

## Command History

Release

Modification

15.6(1)T

This command was introduced.

### Usage Guidelines

Use this command to configure the maximum number of attempts to be
                              		  tried while trying to send out messages from the SIP-TCP connection. Once the
                              		  retry attempts are exhausted, all the pending messages on that TCP connection
                              		  are deleted. If the close-connection keyword is used, the TCP
                              		  connection is closed.

## Examples

The following example sets the maximum number of retry attempts to
                              		  500:

```
Router (config-sip-ua)# tcp-retry 500
```

The following example sets the maximum number of retry attempts to
                              		  100, and also the configuration to close the connection after all the retry
                              		  attempts are exhausted:

```
Router (config-sip-ua)# tcp-retry 100 close-connection
```

The following example shows that CUBE is configured to retry
                              		  unlimitedly until the message goes out or until the connection is closed:

```
Router (config-sip-ua)# tcp-retry nolimit
```

## tdm-group

To configure a list of time slots for creating clear channel groups
                              		  (pass-through) for time-division multiplexing (TDM) cross-connect, use the tdm - group command
                              		  in controller configuration mode. To delete a clear channel group, use the no form of this command.

tdm-group tdm-group-no timeslot timeslot-list [ type { em | fxs [ loop-start | ground-start ] | fxo [ loop-start | ground-start ] | fxs-melcas | fxo-melcas | e&m-melcas }]

no tdm-group tdm-group-no timeslot timeslot-list [ type { em | fxs [ loop-start | ground-start ] | fxo [ loop-start | ground-start ] | fxs-melcas | fxo-melcas | e&m-melcas }]

### Syntax Description

tdm - group - no

TDM group number.

timeslot

Time-slot number.

timeslot - list

Time-slot list. T1 range is 1 to 24. E1 range is 1 to 15
                                          						and 17 to 31.

type

(Optional) (Valid only when the mode cas command is
                                          						enabled.) Voice signaling type of the voice port. If configuring a TDM group
                                          						for data traffic only, do not specify the type keyword.

Choose from one of the following options:

e&m--E&M signaling

fxs--Foreign
                                                						  Exchange Station signaling (optionally, you can also specify loop-start or
                                                						  ground-start)

fxo--Foreign
                                                						  Exchange Office signaling (optionally, you can also specify loop-start or
                                                						  ground-start)

fxs-melcas--Foreign Exchange Station MEL CAS

fxo-melcas--Foreign Exchange Office MEL CAS

e&m-melcas--E&M Mercury Exchange Limited Channel-Associated signaling
                                                						  (MEL CAS)

The MELCAS options apply only to E1 lines and are used
                                          						primarily in the United Kingdom.

### Command Default

No TDM group is configured.

### Command Modes

Controller configuration

## Command History

Release

Modification

11.3(1)MA

This command was introduced on Cisco MC38310.

12.1(1)T

This command was modified to include voice WAN interface
                                          						cards (VWICs) for Cisco 2600 series and Cisco 3600 series.

12.1(2)T

This command was modified for the OC-3/STM-1 ATM Circuit
                                          						Emulation Service network module on Cisco 2600 series and Cisco 3600 series.

### Usage Guidelines

The tdm - group command
                              		  allows specific timeslots to switch from port 0 to port 1 and vice versa. This
                              		  command is similar to the channel - group command, but it does not create a serial interface to terminate the specified
                              		  channels.

Channel groups, CAS voice groups, DS0 groups, and TDM groups all
                                          		  use group numbers. All group numbers configured for channel groups, CAS voice
                                          		  groups, DS0 groups, and TDM groups must be unique on the local router. For
                                          		  example, you cannot use the same group number for a channel group and for a TDM
                                          		  group.

## Examples

The following example configures TDM group 1 to include timeslots 13
                              		  through 20:

```
controller T1 1
 tdm-group 1 timeslots 13-20
```

The following example configures TDM group number 20 on controller T1
                              		  1 to support Foreign Exchange Office (FXO) ground-start:

```
controller T1 1
 tdm-group 20 timeslot 20 type fxs ground-start
```

### Related Commands

Command

Description

connect

Starts passage of data between ports for cross-connect TDM.

## tech-prefix

To specify that a particular technology prefix be prepended to the destination pattern of a specific dial peer, use the tech - prefix command in dial peer configuration mode. To disable the defined technology prefix for this dial peer, use the no form of this command.

tech-prefix number

no tech-prefix

### Syntax Description

number

Defines the numbers used as the technology prefix. Each technology prefix can contain up to 11 characters. Although not strictly
                                          necessary, a pound (#) symbol is frequently used as the last character in a technology prefix. Valid characters are 0 though
                                          9, the pound (#) symbol, and the asterisk (*).

### Command Default

No technology prefix is defined.

### Command Modes

Dial peer configuration

## Command History

Release

Modification

11.3(6)NA2

This command was introduced on Cisco 2600 series and Cisco 3600 series.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

### Usage Guidelines

Technology prefixes are used to distinguish between gateways that have specific capabilities within a given zone. In the exchange
                              between the gateway and the gatekeeper, the technology prefix is used to select a gateway after the zone has been selected.
                              Use the tech - prefix command to define technology prefixes.

Technology prefixes can be used as a discriminator so that the gateway can tell the gatekeeper that a certain technology is
                              associated with a particular call (for example, 15# could mean a fax transmission), or a technology prefix can be used like
                              an area code for more generic routing. No standard defines what the numbers in a technology prefix mean; by convention, technology
                              prefixes are designated by a pound (#) symbol as the last character.

In most cases, there is a dynamic protocol exchange between the gateway and the gatekeeper that enables the gateway to inform
                              the gatekeeper about technology prefixes and where to forward calls. If, for some reason, that dynamic registry feature is
                              not in effect, you can statically configure the gatekeeper to query the gateway for this information by configuring the gw-type-prefix command on the gatekeeper. Use the show gatekeeper gw-type-prefix command to display how the gatekeeper has mapped the technology prefixes to local gateways.

Cisco gatekeepers use the asterisk (*) as a reserved character. If you are using Cisco gatekeepers, do not use the asterisk
                                          as part of the technology prefix.

## Examples

The following example defines a technology prefix of 14# for the specified dial peer. In this example, the technology prefix
                              means that the H.323 gateway asks the RAS gatekeeper to direct calls using the technology prefix of 14#.

```
dial-peer voice 10 voip
 destination-pattern 14...
 tech-prefix 14#
```

### Related Commands

Command

Description

gw - type - prefix

Configures a technology prefix in the gatekeeper.

show gatekeeper gw - type - prefix

Displays the gateway technology prefix table.

## tel-config to-hdr

To configure the
                              		  To: Header (to hdr) Request URI to telephone (TEL) format for VoIP Session
                              		  Initiation Protocol (SIP) calls, use the tel-config to-hdr command in SIP configuration mode or voice
                              		  class tenant configuration mode. To reset to the default, use the no form of this
                              		  command.

tel-config to-hdr [ phone-context ] [system]

no tel-config to-hdr

### Syntax Description

phone-context

(Optional) Appends the phone context parameter to the TEL URL.

system

(Optional) Specifies that the To: Header (to hdr) Request URI to
                                          						telephone (TEL) format use the global sip-ua value. This keyword is available
                                          						only for the tenant mode to allow it to fallback to the global configurations.

### Command Default

The To: Header
                              		  Request Line URIs are not configured to telephone format.

### Command Modes

SIP configuration (conf-serv-sip)

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.4(22)YB

This
                                          						command was introduced.

15.0(1)M

This
                                          						command was integrated into Cisco IOS Release 15.0(1)M.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants.

### Usage Guidelines

The voice-class tel-config to-hdr command takes precedence over the tel-config to-hdr command configured in SIP configuration
                              		  mode. However, if the voice-class tel-config to-hdr command is configured with the system keyword,
                              		  the gateway uses the global settings configured by the tel-config to-hdr command.

Enter SIP
                              		  configuration mode after entering voice-service VoIP configuration mode, as
                              		  shown in the "Examples" section.

## Examples

The following
                              		  example configures the To: header in TEL format, and appends the phone-context
                              		  parameter to the header:

```
voice service voip
sip
 tel-config to-hdr phone-context
```

The following
                              		  example configures the To: header in TEL format in the voice class tenant
                              		  configuration mode:

```
Router(config-class)# tel-config to-hdr system
```

### Related Commands

Command

Description

sip

Enters
                                          						SIP configuration mode from voice-service VoIP configuration mode.

voice - class tel-config to-hdr

Configures the To: Header request URI to telephone format for dial-peer VoIP
                                          						SIP calls.

## telephony-service

To enter telephony-service configuration mode for configuring Cisco Unified CME, use the telephony-service command in global configuration mode. To remove the entire Cisco Unified CME configuration for SCCP IP phones, use the no form of this command.

telephony-service [ setup ]

no telephony-service

### Syntax Description

setup

(Optional) Interactive setup tool for configuring Cisco Unified IP Phone 7910s, 7940s, and 7960s in Cisco Unified CME.

This interactive Cisco CME setup tool is restricted to generating basic configuration files for Cisco Unified IP Phone 7910s,
                                                      7940s, and 7960s running SCCP protocol only.

### Command Default

No Cisco Unified CME configuration for SCCP IP phones is present.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco ITS 1.0

This command was introduced.

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release 12.2(8)T.

12.2(15)ZJ

Cisco CME 3.0

The setup keyword was added.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release 12.3(4)T.

### Usage Guidelines

This command enters the telephony-service configuration mode for configuring system wide parameters for SCCP IP phones in
                              Cisco Unified CME.

The voice-gateway system is tied to the telephony service. The telephony-service command must be configured before the voice-gateway system is configured; otherwise, the voice gateway is hidden from the
                                          user.

Use the setup keyword to start the interactive setup tool to automatically configure only Cisco Unified IP Phone 7910s, 7940s, and 7960s
                              in Cisco Unified CME.

For alternate methods of automatically configuring Cisco Unified CME, including Cisco Unified IP Phone 7910s, 7940s, and
                              7960s and other Cisco Unified IP phones, see the Cisco Unified CME Administrator Guide.

The setup keyword is not stored in the router nonvolatile random-access memory (NVRAM).

If you attempt to use the setup option for a system that already has a telephony-service configuration, the command is rejected. To use the setup option after an existing telephony-service configuration has been created, first remove the existing configuration using
                              the no telephony-service command.

The table below shows a sample dialog with the Cisco CME setup tool and explains possible responses to the Cisco CME setup
                              tool prompts.

Cisco CME Setup Tool Prompt

Description

```
Do you want to setup DHCP service for your IP phones? [yes/no]:
```

```
IP network for telephony-service DHCP  Pool:
Subnet mask for DHCP network : 
TFTP Server IP address (Option 150) :
Default Router for DHCP Pool :
```

Yes--Configures the Cisco Unified CME router to act as a Dynamic Host Configuration Protocol (DHCP) server, automatically
                                                   providing IP addresses to your IP phones and provisioning the default gateway and TFTP IP addresses to be used by the phones.
                                                   This method creates a single pool of IP addresses. If you need a pool for non-IP phones or if the Cisco router cannot act
                                                   as the DHCP router, answer no and manually define the DHCP server.

No--Indicates that you have already configured DHCP or static IP addresses for the IP phones.

```
Do you want to start telephony-service setup? [yes/no]:
```

Yes-- Starts the interactive setup tool for configuring Cisco Unified IP Phone 7910s, 7940s, and 7960s.

No --Terminates the Cisco CME setup tool.

```
Enter the IP source address for Cisco CallManager Express:
Enter the Skinny Port for Cisco CallManager Express:  [2000]:
```

IP address on which the router provides Cisco Unified CME services, usually the default gateway for the IP subnet that you
                                          are using for the IP phones, and the port for Skinny Client Control Protocol (SCCP) messages.

```
How many IP phones do you want to configure : [0]:
```

Enter the maximum number of IP phones that this Cisco Unified CME system will support. This number can be increased later,
                                          to the maximum allowed for this version and your router.

The Cisco CME setup tool associates one number with each newly registering phone. You can manually add additional numbers
                                                      on a phone at a later time.

```
Do you want dual-line extensions assigned to phones? [yes for dual-line / no for single-line]:
```

Yes --Each newly registering IP phones is assigned a single number that is associated with a single phone button. The system generates
                                                   a dual-line ephone-dn entry for each ephone-dn.

No --IP phones are linked directly to one or more PSTN trunk lines. Using keyswitch mode requires manual configuration in addition
                                                   to using the Cisco CME setup tool. The system generates two ephone-dn entries for each ephone-dn, and they are both assigned
                                                   to a single phone.

```
What language do you want on IP phones?
      0  English
      1  French
      2  German
      3  Russian
      4  Spanish
      5  Italian
      6  Dutch
      7  Norwegian
      8  Portuguese
      9  Danish
      10  Swedish
 [0]:
```

Language for IP phone displays, selected from the list.

Default is 0, English.

```
Which Call Progress tone set do you want on IP phones :     
      0  United States
      1  France
      2  Germany
      3  Russia
      4  Spain
      5  Italy
      6  Netherlands
      7  Norway
      8  Portugal
      9  UK
    10  Denmark
    11  Switzerland
    12  Sweden
    13  Austria
    14  Canada
[0]:
```

Locale for the tone set used to indicate call status or progress, selected from the list.

Default is 0, United States.

```
What is the first extension number you want to configure :[0]:
```

First number in pool of extension numbers to be created for IP phones connected to the Cisco router to be configured.

Starting with this number, remaining extension numbers are automatically configured in a contiguous manner.

This number must be compatible with your telephone number plan, and, if you use Direct Inward Dialing (DID) service, with
                                                public switched telephone network (PSTN) numbering requirements.

```
Do you have Direct-Inward-Dial service for all your phones? [yes/no]:
```

Yes--If you have trunk access to public telephone service by ISDN or VoIP for all extension numbers. The system creates an
                                                   appropriate dial plan.

No--If you have simple analog phone lines only (for example, foreign exchange office [FXO] interfaces) or if you have trunk
                                                   access for some lines but not all lines.

If you answer yes to the previous question, you see the following prompt:

```
Enter the full E.164 number for the first phone:
```

Complete 10-digit telephone number, including area code, that corresponds to the first extension number.

```
Do you want to forward calls to a voice message service? [yes/no]:
```

Yes--To forward calls to a single voice message service number when an IP phone is busy or does not answer. All phone extensions
                                                   forward their calls to the same voice message service pilot number.

No--Not to forward calls to a single voice message service number. Answer no if you do not have a voice message system or
                                                   if you want to customize call-forwarding behavior for each extension.

If you answer yes to the previous question, you see the following prompt:

```
Enter the extension or pilot number of the voice message service:
```

Voice message service pilot number.

This step can be ignored during the setup dialog and manually configured later.

```
Call forward No Answer Timeout: [18]:
```

Timeout, in seconds, after which to forward calls to voice mail if they are not answered.

Default is 18.

```
Do you wish to change any of the above information? [yes/no]:
```

Yes --Starts the dialog over again without implementing any of the answers that you previously gave.

No --Uses specified values to automatically build basic configuration for Cisco Unified IP Phone 7910s, 7940s, and 7960s in Cisco
                                                   Unified CME.

## Examples

The following example shows how to enter telephony-service configuration mode for manually configuring Cisco Unified CME.
                              This example also configures the maximum number of phones to 12:

```
Router(config)# telephony-service Router(config-telephony)# max-ephones 12
```

The following example shows how to start the Cisco CME setup tool:

```
Router(config)# telephony-service setup
```

## telephony-service ccm-compatible (H.323 voice-class)

To enable, for an individual dial peer, the detection of a Cisco CallManager system in the network and allow the exchange
                              of calls, use the telephony-service ccm-compatible command in voice-class configuration mode. To disable the detection capability and the exchange of calls on an individual
                              dial peer, use the no form of this command.

telephony-service ccm-compatible

no telephony-service ccm-compatible

### Syntax Description

This command has no arguments or keywords.

### Command Default

Detection of Cisco CallManager systems is enabled.

### Command Modes

Voice-class configuration

## Command History

Release

Modification

12.3(7)T

This command was introduced.

### Usage Guidelines

This command is used with Cisco CallManager Express (Cisco CME) 3.1 or a later version.

When a voice class that contains this command is applied to a dial peer, this command enables detection of and call exchange
                              with Cisco CallManager for all calls from that dial peer. Use the telephony-service ccm-compatible command in H.323 voice-service configuration mode to create a voice class to apply this capability globally. If the capability
                              is specified at both the global and dial-peer level, the dial-peer setting has precedence for that dial peer.

## Examples

The following example globally enables detection of Cisco CallManager systems in the network, creates voice class 4 to disable
                              the capability on individual dial peers, and applies voice class 4 to dial peer 36. Although the telephony-service ccm-compatible command in H.323 voice-service configuration mode is not required because this condition is the default, the command is shown
                              here for illustration purposes.

```
Router(config)# voice service voip Router(config-voi-serv)# h323 Router(conf-serv-h323)# telephony-service ccm-compatible Router(conf-serv-h323)# exit Router(config-voi-serv)# exit Router(config)# voice class h323 4 Router(config-class)# no telephony-service ccm-compatible Router(config-class)# exit Router(config)# dial-peer voice 36 voip Router(config-dial-peer)# destination-pattern 555.... Router(config-dial-peer)# session target ipv4:10.5.6.7 Router(config-dial-peer)# voice-class h323 4
```

### Related Commands

Command

Description

telephony-service ccm-compatible (H.323 voice-service)

Globally enables detection of Cisco CallManager in a network for all dial peers.

voice class h323

Creates an H.323 voice class to apply to a dial peer.

voice-class h323

Applies an H.323 voice class to a dial peer.

## telephony-service ccm-compatible (H.323 voice-service)

To globally enable the detection of a Cisco CallManager system in the network and allow the exchange of calls, use the telephony-service ccm-compatible command in H.323 voice-service configuration mode. To disable the detection capability and the exchange of calls globally,
                              use the no form of this command.

telephony-service ccm-compatible

no telephony-service ccm-compatible

### Syntax Description

This command has no arguments or keywords.

### Command Default

Detection of Cisco CallManager systems is enabled.

### Command Modes

H.323 voice-service configuration

## Command History

Release

Modification

12.3(7)T

This command was introduced.

### Usage Guidelines

This command is used with Cisco CallManager Express (Cisco CME) 3.1 or a later version.

This command globally enables call exchange with Cisco CallManager for all calls from this router. Use the telephony-service ccm-compatible command in voice-class configuration mode to create a voice class in order to apply this capability to an individual dial
                              peer. If the capability is specified at both the global and dial-peer level, the dial-peer setting has precedence for that
                              dial peer.

## Examples

The following example globally enables detection of Cisco CallManager systems in the network, creates voice class 4 to disable
                              the capability on individual dial peers, and applies voice class 4 to dial peer 36. Although the telephony-service ccm-compatible command in H.323 voice-service configuration mode is not required because this condition is the default, the command is shown
                              here for illustration purposes.

```
Router(config)# voice service voip Router(config-voi-serv)# h323 Router(conf-serv-h323)# telephony-service ccm-compatible Router(conf-serv-h323)# exit Router(config-voi-serv)# exit Router(config)# voice class h323 4 Router(config-class)# no telephony-service ccm-compatible Router(config-class)# exit Router(config)# dial-peer voice 36 voip Router(config-dial-peer)# destination-pattern 555.... Router(config-dial-peer)# session target ipv4:10.5.6.7 Router(config-dial-peer)# voice-class h323 4
```

### Related Commands

Command

Description

h323

Enters H.323 voice-service configuration mode.

telephony-service ccm-compatible (H.323 voice-class)

Enables Cisco CallManager detection in a network by individual dial peers.

voice service voip

Enters voice-service configuration mode.

## test dsmp
                        	 delete-stream

To clear one or more inactive Distributed Stream Media Processor
                              		  (DSMP) media stream sessions that are hung and is not cleared, use the test dsmp delete-stream command in the
                              		  privileged EXEC mode.

test dsmp delete-stream stream-id

### Syntax Description

stream-id

The specific stream-id that is hung and should be deleted.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

15.4(3)M

This command was introduced.

## Examples

The following example shows the voice :

```
Router #test dsmp delete-stream 7973
test_dsmp: id is 7973
% Stream 7973 does not exist
```

## test voice
                        	 mos-calc

To test the MOS computation algorithm voice quality metrics related
                              		  to media (voice) quality, such as conversational mean opinion score (MOS),
                              		  packet loss rate, and so on, use the test voice mos-calc command in the privileged EXEC
                              		  mode.

test voice mos-calc Packet Loss RTT Jitter

### Syntax Description

Packet Loss

Enter the packet loss, in percentage. Range is from 0 to
                                          						100.

RTT

Enter the round trip time, in ms (range 0 - 5000).

Jitter

Enter the jitter value caused by switches in the WAN, in ms
                                          						(range 0 - 2000).

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

Cisco IOS XE Denali 16.3.1

This command was introduced.

## Examples

The following example shows the voice :

```
Router#test voice mos-calc ?
  <0-100>  Packet Loss in percentage

Router#test voice mos-calc 5 ?
  <0-5000>  RTT in milliseconds

Router#test voice mos-calc 5 16 ?
  <0-2000>  Jitter in milliseconds

Router#test voice mos-calc 5 16 6 ?
  Mean Opinion Score= 3.7841
  <cr>
```

## text relay modulation

To configure the teletype text phone (TTY) modulation used on the gateway for Cisco text relay for Baudot text phones, use
                              the text relay modulation command in dial peer voice configuration mode or voice service configuration mode. To disable text relay modulation, use the no form of this command.

text relay modulation { baudot45 . 45 | baudot50 } { autobaud-on | autobaud-off }

no text relay modulation

### Syntax Description

baudot45.45

Configures baudot 45.45 TTY modulation. This is the default baud rate.

baudot50

Configures baudot 50 TTY modulation.

autobaud-on

Enables the digital signal processors (DSPs) to autodetect the baud rate. This is the default autobaud setting.

autobaud-off

Disables the DSP capability to autodetect the baud rate.

### Command Default

The TTY modulation is baudot45.45 autobaud-on .

### Command Modes

Dial peer voice configuration Voice service configuration

## Command History

Release

Modification

12.4(6)T

This command was introduced.

### Usage Guidelines

You must select a baud rate and enable or disable the autobaud functionality on the DSP.

Use this command in voice service configuration mode to set the TTY modulation globally. A global configuration is the system-wide
                              configuration that is applied to any VoIP call on the gateway.

Use this command in dial peer voice configuration mode to set the TTY modulation for calls that match a specific dial peer.
                              The dial peer voice configuration takes precedence over the global configuration.

## Examples

The following example shows how to globally set the text relay TTY modulation to Baudot 50:

```
Router(config)# voice service voip Router(config-voi-serv)# text relay modulation baudot50 autobaud-off
```

The following example shows how to set the text relay TTY modulation to Baudot 50 for calls that match a specific dial peer:

```
Router(config)# dial-peer voice 2000 voip Router(config-dial-peer)# text relay modulation baudot50 autobaud-off
```

### Related Commands

Command

Description

text relay protocol

Configures the system-wide protocol type for text packets transmitted between gateways.

text relay rtp

Configures the RTP payload type and redundancy level.

## text relay protocol

To enable Cisco text relay for Baudot text phones, use the text relay protocol command in dial peer voice configuration mode or voice service configuration mode. To disable text relay capabilities, use
                              the no form of this command.

text relay protocol [ cisco | system ]

no text relay protocol

### Syntax Description

cisco

(Optional) Uses the Cisco proprietary text relay protocol.

system

(Optional; dial peer voice configuration only) Uses the global configuration settings.

### Command Default

The text relay protocol is disabled.

### Command Modes

Dial-peer configuration Voice-service configuration

## Command History

Release

Modification

12.4(6)T

This command was introduced.

### Usage Guidelines

Use this command in voice-service configuration mode to enable text relay globally for H.323, Session Initiation Protocol
                              (SIP), Skinny Client Control Protocol (SCCP), and Media Gateway Control Protocol (MGCP). A global configuration is the system-wide
                              configuration that is applied to any VoIP call on the gateway.

Use this command in dial peer voice configuration mode to enable text relay for calls that match a specific dial peer. The
                              dial peer voice configuration takes precedence over the global configuration.

## Examples

The following example shows how to enable text relay for all VoIP calls on the gateway:

```
Router(config)# voice service voip Router(config-voi-serv)# text relay protocol cisco
```

The following example shows how to enable text relay for calls that match a specific dial peer:

```
Router(config)# dial-peer voice 2000 voip Router(config-dial-peer)# text relay protocol cisco
```

### Related Commands

Command

Description

text relay modulation

Configures the TTY modulation on the gateway.

text relay rtp

Configures the RTP payload type and redundancy level.

## text relay rtp

To configure the Real-Time Transport Protocol (RTP) payload type and redundancy level for Cisco text relay for Baudot text
                              phones, use the text relay rtp command in dial peer voice configuration mode or voice service configuration mode. To disable the text relay RTP payload type
                              and redundancy level, use the no form of this command.

text relay rtp { [ payload-type { value | default }] [ redundancy level ] | redundancy level }

no text relay rtp

### Syntax Description

payload-type
                                                { value | default }

The RTP payload is the data transported by RTP in a packet.

The value range is 98 to 117 for dynamic RTP payload types.

The default value is 119, which is a static payload type.

redundancy level

Use the redundancy option to repeat data for redundancy and to lower the risk of packet loss. The redundancy level is the
                                          number of redundant text packets sent across the VoIP network. The range is 1 to 3. The default value is 2.

### Command Default

Text relay RTP is disabled.

### Command Modes

Dial peer voice configuration Voice service configuration

## Command History

Release

Modification

12.4(6)T

This command was introduced.

### Usage Guidelines

When using the text relay rtp command, you can either configure the payload-type , or the redundancy level, or both.

Use this command in voice service configuration mode to set the RTP payload type and redundancy level globally for H.323,
                                    Session Initiation Protocol (SIP), Skinny Client Control Protocol (SCCP), and Media Gateway Control Protocol (MGCP). A global
                                    configuration is the system-wide configuration that is applied to any VoIP call on the gateway.

Use this command in dial-peer configuration mode to set the RTP payload type and redundancy level for calls that match a specific
                                    dial peer. The dial peer voice configuration takes precedence over the global configuration.

## Examples

The following example shows how to globally configure text relay RTP payload type 117 and redundancy level 2:

```
Router(config)# voice service voip Router(config-voi-serv)# text relay rtp payload-type 117 redundancy 2
```

The following example shows how to configure the default text relay RTP payload type and redundancy level 1 for calls that
                              match a specific dial peer:

```
Router(config)# dial-peer voice 2000 voip Router(config-dial-peer)# text relay rtp payload-type default redundancy 1
```

### Related Commands

Command

Description

text relay modulation

Configures the TTY modulation on the gateway.

text relay protocol

Configures the system-wide protocol type for text packets transmitted between gateways.

## tftp-server address

To specify the address of the TFTP servers in a Cisco Unified Communications Manager
                              (CUCM) cluster use the tftp-server address command in phone proxy configuration mode. To remove the  address of the TFTP server from the phone proxy configuration,
                              use the no form of the command.

tftp-server address [ ipv4 server-ip-address | domain-name ] local-addr ipv4 local-ip-address acc-addr ipv4 access-ip-address

no tftp-server address [ ipv4 server-ip-address | domain-name ] local-addr ipv4 local-ip-address [ acc-addr ipv4 access-ip-address ]

## Syntax Description

Domain name of the TFTP server.

Specifies the local interface IPv4
                                       address to connect to the core side
                                       server.

Specifies the access side local
                                       interface IPv4 address.

### Command Default

No TFTP server addresses are specified.

### Command Modes

Phone proxy configuration mode (config-phone-proxy)

## Command History

15.3(3)M

This command was introduced.

### Usage Guidelines

## Examples

The following example shows how to  command to specify the TFTP server addresses for the phone proxy configuration:

```
Device(config)# voice-phone-proxy first-pp
Device(config-phone-proxy)# tftp-server address ipv4 198.51.100.101 local-addr ipv4 192.168.0.109 acc-addr 198.51.100.1
```

## tgrep address-family

To set the address family to be used on a local dial peer, use the tgrep address-family command in dial peer configuration
                              mode. To return to the global setting, use the no form of this command.

tgrep address family { e164 | decimal | penta-decimal }

no tgrep address family { e164 | decimal | penta-decimal }

### Syntax Description

e164

E.164 address family.

decimal

Decimal address family

penta-decimal

Penta-decimal address family

### Command Default

No default behavior or values.

### Command Modes

Dial peer configuration

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

The E. 164 address family is used if the telephony network is a public telephony network. Decimal and pentadecimal options
                              can be used to advertise private dial plans. For example if a company wants to use TRIP in within their enterprise telephony
                              network using 5-digit extensions, then the gateway would advertise the beginning digits of their private numbers as a decimal
                              address family. These calls cannot be sent out of the company’s private telephony network because they are not E.164-compliant.

The pentadecimal family allows numbers 0 through 9 and alphabetic characters A through E and can be used in countries where
                              letters are also carried in the called number.

## Examples

The following example shows that POTS dial peer 10 has the address family set for E.164 addresses:

```
Router(config)# dial-peer voice pots 10 Router(config-dial-peer)# tgrep address family e164
```

### Related Commands

Command

Description

dial-peer voice

Enters dial-peer configuration mode and specifies the method of voice-related encapsulation.

## tgrep advertise (dial peer)

To set the attributes for advertisement of the prefix on this dial peer or to disable advertisement on this dial peer altogether,
                              use the tgrep advertise command in dial peer configuration mode. To return to using the global setting, use the no form of this command.

tgrep advertise [ csr ] [ ac ] [ tc ] [ carrier | trunk-group ] [ disable ]

no tgrep advertise [ csr ] [ ac ] [ tc ] [ carrier | trunk-group ] [ disable ]

### Syntax Description

csr

Call success rate.

ac

Available circuits.

tc

Total circuits.

carrier

Carrier-code address family.

trunk-group

Trunk-group address family.

disable

Disables advertisement of this dial peer.

### Command Default

Prefix advertisement is not sent.

### Command Modes

Dial peer configuration

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

When only tgrep advertise is entered, the dial peer is advertised without any other attribute.

When no tgrep advertise is used on the dial peer, the dial peer inherits the attributes set in the global advertise command.

When the global no advertise command is used, it forbids advertisement of that particular address family altogether. The tgrep advertise command has no effect until the advertisement of the address family is enabled globally.

## Examples

The following example shows a TGREP advertisement that sends call success rate, available circuits, total circuits, and carrier
                              address family attribute information:

```
Router(config)# dial-peer voice pots 10 Router(config-dial-peer)# tgrep advertise csr ac tc carrier
```

### Related Commands

Command

Description

dial-peer voice

Enters dial-peer configuration mode and specifies the method of voice-related encapsulation.

## tgrep advertise (trunk group)

To turn on the advertisement of this trunk group for resource availability and other carrier information, use the tgrep advertise
                              command in trunk group configuration mode. To turn off local trunk group advertisement and use the global setting, use the no form of this command.

tgrep advertise [ csr ] [ ac ] [ tc ] [ disable ]

no tgrep advertise [ csr ] [ ac ] [ tc ] [ disable ]

### Syntax Description

csr

Call success rate.

ac

Available circuits.

tc

Total circuits.

disable

Disables advertisement on the trunk group.

### Command Default

Trunk group advertisement is not sent

### Command Modes

Trunk group configuration

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

When only tgrep advertise is entered, the trunk group is advertised without any other attribute. When no tgrep advertise is
                              used, the trunk group uses the global setting configured with the advertise command in TGREP configuration mode. To turn off
                              advertisement of this trunk group, the disable keyword should be used.

There is a subtle difference between the no form of this command and the no form of the global advertise command. When no
                              tgrep advertise is used on the trunk group, the trunk group inherits the attributes set in the global advertise command.

When the global no advertise command is used, it forbids advertisement of that particular address family altogether. The tgrep advertise command has no effect until the advertisement of the address family is enabled globally.

When the carrier keyword is used, the carrier defined under the trunk group assumes the configuration. Because multiple trunk groups can have
                              the same carrier defined, the same configuration will show up under all trunk groups that have the same carrier defined. When
                              the no tgrep advertise carrier command is used to revert to the global carrier configuration for the carrier under this trunk group, the same will happen
                              to all the trunk groups who have the same carrier defined under them.

This command overrides the attributes set for advertisement using the global 
                                          advertise (tgrep)
                                          command.

## Examples

The following example shows that trunk group 101 has been configured to send a TGREP advertisement that sends call success
                              rate, available circuits, total circuits, and prefix attribute information:

```
Router(config)# trunk group 101 Router(config-dial-peer)# tgrep advertise csr ac tc carrier
```

### Related Commands

Command

Description

advertise (tgrep)

Turns on reporting for a specified address family.

trunk group

Defines the trunk group and enters trunk group configuration mode.

## tgrep local-itad

To enable Telephony Gateway Registration Protocol (TGREP) on the gateway and enter TGREP configuration mode, use the tgrep local-itad command in global configuration mode. To disable the configuration on the gateway, use the no form of this command.

tgrep local-itad [itad-number]

no tgrep local-itad [itad-number]

### Syntax Description

itad-number

(Optional) IP Telephony Administrative Domain (ITAD) number associated with the gateway. The range is from 1 to 4294967295.

### Command Default

TGREP is disabled on the gateway.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(1)

This command was introduced.

## Examples

The following example shows how to enable TGREP for ITAD number 1234:

```
Router# enable Router(config)# tgrep local-itad 1234
```

### Related Commands

Command

Description

address-family

Sets the global address family to be used on all dial peers.

advertise (tgrep)

Turns on reporting for a specified address family.

neighbor

Creates a TGREP session with another device.

## threshold noise

To configure a noise threshold for incoming calls, use the threshold noise command in voice-port configuration mode. To restore the default, use the no form of this command.

threshold noise value

no threshold noise value

### Syntax Description

value

Number that establishes a noise threshold. Valid values are from -30 to -90 decibels (dBs). The default is -62 dB.

### Command Default

-62 dB

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.2(13b)

This command was introduced on the following platforms: Cisco 1700 Cisco 1751, Cisco 2600 (with and without the NM-HDA), Cisco
                                          3600 (with and without the NM-HDA), Cisco 7200 (with and without the NM-HDA), Cisco AS5300, Cisco AS5800, and Cisco MC3810.

12.2(16)

This command was integrated into Cisco IOS Release 12.2(16).

### Usage Guidelines

Cisco voice activity detection (VAD) has two layers: application programming interface (API) layer and processing layer. There
                              are 3 states that the processing layer classifies incoming signals: speech, unknown, and silence. The state of the incoming
                              signals is determined by the noise threshold.

In earlier Cisco IOS releases, the noise threshold is fixed between -62 dB and -78 dB. If the voice level is below the noise
                              threshold, then the signal is classified as silence. If the incoming signal cannot be classified, the variable thresholds
                              that are computed with the statistics of speech and noise that VAD gathers is used to make a determination. If the signal
                              still cannot be classified, then it is marked as unknown. The final decision is made by the API. For applications such as
                              hoot-n-holler, you could have the noise create unwanted spurious packets (for example, a voice stream) taking up bandwidth.

With Cisco IOS Release 12.2(16), the noise threshold is configurable using the threshold noise command.

## Examples

The following sample configuration shows a noise threshold level of -50 dB:

```
voice-port 1/0/0
 threshold noise -50
```

## timeout (auto-config application)

To configure the download timeout value for an auto-configuration application, use the timeout command in auto-config application configuration mode. To reset to the default, use the no form of this command.

timeout time-in-seconds

no timeout

### Syntax Description

time - in - seconds

Specifies the download timeout value in seconds. The range is from 0 to 3600. The default is 180.

### Command Default

The default value is 180 seconds.

### Command Modes

Auto-config application configuration

## Command History

Release

Modification

12.3(8)XY

This command was introduced on the Communication Media Module.

12.3(14)T

This command was integrated into Cisco IOS Release 12.3(14)T.

### Usage Guidelines

A value of 0 specifies continuous download retry.

## Examples

The following example shows the timeout command used to specify continuous retry for downloading an auto-configuration application:

```
Router(auto-config-app)# timeout 0
```

### Related Commands

Command

Description

auto - config

Enables auto-configuration or enters auto-config application configuration mode for the SCCPapplication.

show auto - config

Displays the current status of auto-configuration applications.

## timeout leg3

To set the timeout value for a leg 3 AAA preauthentication request, use the timeout leg3 command in AAA preauthentication configuration mode. To return the timeout value to its default, use the no form of this command.

timeout leg3 milliseconds

no timeout leg3 milliseconds

### Syntax Description

milliseconds

Timeout value for leg 3 preauthentication, in milliseconds. Range is from 100 to 1000. The default is 100.

### Command Default

100 milliseconds.

### Command Modes

AAA preauthentication configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

If the timeout timer expires before AAA has responded to a preauthentication request, the call is rejected.

The term leg 3 refers to a call segment from the IP network to a terminating (outgoing) gateway that takes traffic from an IP network to
                              a PSTN network.

## Examples

The following example sets the timeout for a leg 3 AAA preauthentication request to 250 milliseconds:

```
Router(config)# aaa preauth Router(config-preauth)# timeout leg3 250
```

### Related Commands

Command

Description

aaa preauth

Enters AAA preauthentication configuration mode.

## timeout ptt

To specify a maximum time for transmitting or receiving a voice packet, use the timeout ptt command in voice-port configuration mode. To return to the default, use the no form of this command.

timeout ptt { rcv | xmt } minutes

no timeout ptt { rcv | xmt } minutes

### Syntax Description

rcv

Applies the specified time limit to the reception of voice packets.

xmt

Applies the specified time limit to the transmission of voice packets.

minutes

Maximum time, in minutes, allowed for transmitting or receiving a voice packet. Range is integers from 1 to 30.

### Command Default

minutes : 0 minutes

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.3(4)XD

This command was introduced.

12.3(7)T

This command was integrated into Cisco IOS Release 12.3(7)T.

### Usage Guidelines

The timeout ptt command is available on an ear and mouth (E&M) analog or digital voice port only if the signal type for that port is Land
                              Mobile Radio (LMR). The purpose of this command is to limit extended radio transmission. When the time limit configured with
                              this command expires, the radio transmitter unkeys, so that listeners on the channel cannot hear the speaker, even if the
                              speaker continues to talk. When the speaker unkeys the radio, the timer is reactivated.

## Examples

The following example specifies a maximum time of 10 minutes for transmitting a voice packet:

```
voice-port 1/0/0
 timeout ptt xmt 10
```

## timeout tcrit

To configure the critical timeout value, T(critical), for the interdigit timer used in digit map matching, use the timeout tcrit command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tcrit tcrit-value

no timeout tcrit

### Syntax Description

tcrit - value

Critical timeout value, T(critical), in seconds. Range is from 1 to 600. Default is 4.

### Command Default

4 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

The interdigit timer is used when matching a digit map, which is a representation of the number and type of digits that a
                              gateway can expect to collect in a buffer, based on the network dial plan. The interdigit timer is started when the first
                              digit is entered and is restarted after each new digit is entered, until a digit map match or mismatch occurs.

The interdigit timer takes on one of two values, T(partial) or T(critical). When at least one more digit is required to make
                              a match to any of the patterns in the digit map, the value of T(partial) is used for the timer. If a timer is all that is
                              required to produce a match according to the digit map, T(critical) is used for the timer.

When the interdigit timer is used without a digit map, it takes on the value T(critical). It is started immediately and is
                              simply canceled (but not restarted) as soon as a digit is entered.

## Examples

The following example sets the T(critical) value to 15 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tcrit 15
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

timeout tpar

Configures the MGCP partial timeout value, T(partial), for the interdigit timer used in digit map matching.

## timeout tdinit

To configure the initial waiting delay value (Tdinit) for the disconnected procedure, use the timeout tdinit command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tdinit tdinit-value

no timeout tdinit

### Syntax Description

tdinit - value

Initial waiting delay (Tdinit) for the disconnected procedure, in seconds. The disconnected timer is initialized to a randomly
                                          selected value between 0 and Tdinit. Range is from 1 to 30. Default is 15.

### Command Default

15 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

When a gateway recognizes that an endpoint has lost its communication with the call agent (has become disconnected) , a timer known as the disconnected timer is initialized to a random value between 0 and the disconnected initial waiting
                              delay (Tdinit), which is configured with the timeout tdinit command. The gateway then waits for one of three things: the end of this timer, the reception of a command from the call
                              agent, or the detection of local user activity for the endpoint, such as an off-hook transition. When one of the first two
                              cases occurs, the gateway initiates the disconnected procedure for that endpoint. In the third case, the detection of local user activity, a minimum waiting delay (Tdmin) also must have
                              elapsed. This value is configured with the timeout tdmin command.

The disconnected procedure consists of the endpoint sending a RestartInProgress (RSIP) message to the call agent, stating
                              that it was disconnected and is now trying to reestablish connectivity.

If the disconnected procedure is unsuccessful and the endpoint is still disconnected, the disconnected timer is doubled;
                              this process is repeated until the timer value reaches the maximum waiting delay (Tdmax), which is configured with the timeout tdmax command.

## Examples

The following example sets the initial waiting delay value (Tdinit) to 25 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tdinit 25
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

timeout tdmax

Configures the maximum timeout for the MGCP disconnected procedure.

timeout tdmin

Configures the minimum timeout for the MGCP disconnected procedure.

## timeout tdmax

To configure the maximum timeout value (Tdmax) for the disconnected procedure, use the timeout tdmax command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tdmax tdmax-value

no timeout tdmax

### Syntax Description

tdmax - value

Maximum timeout value (Tdmax) for the disconnected procedure, in seconds. Range is from 300 to 600. The default is 600.

### Command Default

600 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

When a gateway recognizes that an endpoint has lost its communication with the call agent (has become disconnected) , a timer known as the disconnected timer is initialized to a random value between 0 and the disconnected initial waiting
                              delay (Tdinit), which is configured with the timeout tdinit command. The gateway then waits for one of three things: the end of this timer, the reception of a command from the call
                              agent, or the detection of local user activity for the endpoint, such as an off-hook transition. When one of the first two
                              cases occurs, the gateway initiates the disconnected procedure for that endpoint. In the third case, the detection of local user activity, a minimum waiting delay (Tdmin) also must have
                              elapsed. This value is configured with the timeout tdmin command.

The disconnected procedure consists of the endpoint sending a RestartInProgress (RSIP) message to the call agent, stating
                              that it was disconnected and is now trying to reestablish connectivity.

If the disconnected procedure is unsuccessful and the endpoint is still disconnected, the disconnected timer is doubled;
                              this process is repeated until the timer value reaches the maximum waiting delay (Tdmax), which is configured with the timeout tdmax command.

## Examples

The following example sets the maximum timeout value (Tdmax) to 450 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tdmax 450
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

timeout tdinit

Configures the initial timeout for the MGCP disconnected procedure.

timeout tdmin

Configures the minimum timeout for the MGCP disconnected procedure.

## timeout tdmin

To configure the minimum timeout value (Tdmin) for the disconnected procedure, use the timeout tdmin command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tdmin tdmin-value

no timeout tdmin

### Syntax Description

tdmin - value

Minimum timeout (Tdmin) for the disconnected procedure, in seconds. Range is from 1 to 30. The default is 15.

### Command Default

15 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

When a gateway recognizes that an endpoint has lost its communication with the call agent (has become disconnected) , a timer known as the disconnected timer is initialized to a random value between 0 and the disconnected initial waiting
                              delay (Tdinit), which is configured with the timeout tdinit command. The gateway then waits for one of three things: the end of this timer, the reception of a command from the call agent,
                              or the detection of local user activity for the endpoint, such as an off-hook transition. When one of the first two cases
                              occurs, the gateway initiates the disconnected procedure for that endpoint. In the third case, the detection of local user activity, a minimum waiting delay (Tdmin) also must have
                              elapsed. This value is configured with the timeout tdmin command.

The disconnected procedure consists of the endpoint sending a RestartInProgress (RSIP) message to the call agent, stating
                              that it was disconnected and is now trying to reestablish connectivity.

If the disconnected procedure is unsuccessful and the endpoint is still disconnected, the disconnected timer is doubled;
                              this process is repeated until the timer value reaches the maximum waiting delay (Tdmax), which is configured with the timeout tdmax command.

## Examples

The following example sets the minimum timeout value (Tdmin) to 20 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tdmin 20
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

timeout tdinit

Configures the initial timeout for the MGCP disconnected procedure.

timeout tdmax

Configures the maximum timeout for the MGCP disconnected procedure.

## timeout thist

To configure the packet storage timeout value (Thist), use the timeout thist command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout thist thist-value

no timeout thist

### Syntax Description

thist - value

Package storage timeout (Thist), in seconds. Range is from 1 to 60. The default is 30.

### Command Default

30 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

MGCP messages are carried over User Datagram Protocol (UDP), and are therefore subject to packet loss. When a response to
                              a message is not received promptly, the sender retransmits the message. The gateway keeps in memory a list of the responses
                              it has sent for the number of seconds in the Thist timeout value. The gateway also keeps a list of the messages currently
                              being processed, with their transaction identifiers, to prevent processing or acknowledging the same message more than once.

## Examples

The following example sets the packet storage timeout value (Thist) to 15 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout thist 15
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints, or to configure
                                          the default profile.

## timeout tone busy

To configure the busy-tone timeout value, use the timeout tone busy command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tone busy busy-tone-value

no timeout tone busy

### Syntax Description

busy - tone - value

Busy-tone timeout, in seconds. Range is from 1 to 600. The default is 30.

### Command Default

30 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

The gateway uses the busy-tone timeout value when the call agent does not provide a timeout value associated with the request
                              to generate a busy tone signal.

## Examples

The following example sets the busy tone timeout value to 45 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tone busy 45
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

## timeout tone cot1

To configure the continuity1 (cot1) tone timeout value, use the timeout tone cot1 command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tone cot1 cot1-tone-value

no timeout tone cot1

### Syntax Description

cot1 - tone - value

Continuity1 (cot1) tone timeout, in seconds. Range is from 1 to 600. The default is 3.

### Command Default

3 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

The gateway uses the continuity1 (cot1) tone timeout value when the call agent does not provide a timeout value associated
                              with the request to generate a cot1 tone signal.

Continuity1 and continuity2 tone signals are used in Integrated Services Digital Networks User Part (ISUP) calls to determine
                              that a call path has been established before connecting a call. The call agent is provisioned to know which test to apply
                              to a given endpoint.

## Examples

The following example sets the continuity1 tone timeout value to 25 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tone cot1 25
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

timeout tone cot2

Sets the continuity2 tone timeout value for MGCP.

## timeout tone cot2

To configure the continuity2 (cot2) tone timeout value, use the timeout tone cot2 command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tone cot2 cot2-tone-value

no timeout tone cot2

### Syntax Description

cot2 - tone - value

Continuity2 (cot2) tone timeout, in seconds. Range is from 1 to 600. The default is 3.

### Command Default

3 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

The gateway uses the continuity2 (cot2) tone timeout value when the call agent does not provide a timeout value associated
                              with the request to generate a cot2 tone signal.

Continuity1 and continuity2 tone signals are used in Integrated Services Digital Networks User Part (ISUP) calls to determine
                              that a call path has been established before connecting a call. The call agent is provisioned to know which test to apply
                              to a given endpoint.

## Examples

The following example sets the continuity2 tone timeout value to 50 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tone cot2 50
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

timeout tone cot1

Sets the continuity1 tone timeout value for MGCP.

## timeout tone dial

To configure the dial tone timeout value, use the timeout tone dial command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tone dial dial-tone-value

no timeout tone dial

### Syntax Description

dial - tone - value

Dial tone timeout value, in seconds. Range is from 1 to 600. The default is 16.

### Command Default

16 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

The gateway uses the dial tone timeout value when the call agent does not provide a timeout value associated with the request
                              to generate a dial tone signal.

## Examples

The following example sets the dial tone timeout value to 25 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tone dial 25
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

## timeout tone dial stutter

To configure the stutter dial tone timeout value, use the timeout tone dial stutter command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tone dial stutter stutter-value

no timeout tone dial stutter

### Syntax Description

stutter - value

Timeout value for the stutter dial tone, in seconds. Range is from1 to 600. The default is 16.

### Command Default

16 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

The gateway uses the stutter dial tone timeout value when the call agent does not provide a timeout value associated with
                              the request to generate a stutter dial tone signal.

## Examples

The following example sets the stutter dial tone timeout value to 25 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tone dial stutter 25
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

## timeout tone mwi

To configure the timeout value for the message-waiting indicator tone, use the timeout tone mwi command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tone mwi mwi-tone-value

no timeout tone mwi

### Syntax Description

mwi - tone - value

Message-waiting-indicator (MWI) tone timeout value, in seconds. Range is from 1 to 600. The default is 16.

### Command Default

16 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

The gateway uses the mwi - tone - value when the call agent does not provide a timeout value for a request to generate the message-waiting indicator tone signal.

## Examples

The following example sets the timeout value for the message-waiting indicator tone to 100 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tone mwi 100
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

## timeout tone network

To configure the network congestion tone timeout value, use the timeout tone network command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tone network { congestion | busy } tone-value

no timeout tone network

### Syntax Description

congestion

Timeout for network congestion.

busy

Timeout for network busy.

tone - value

Tone timeout value, in seconds. Range is from 1 to 600. The default is 180.

### Command Default

180 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

12.4(9)T

The busy keyword was introduced.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

The gateway uses the tone timeout value when the call agent does not provide a timeout value associated with the request
                              to generate a network congestion or network busy tone signal.

## Examples

The following example sets the network congestion tone timeout value to 240 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tone network congestion 240
```

The following example shows the network busy timeout value being set to 300 seconds.

Router(config)# mgcp profile sample

```
Router(config-mgcp-profile)# timeout tone network busy 300
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

## timeout tone reorder

To configure the reorder tone timeout value, use the timeout tone reorder command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tone reorder reorder-tone-value

no timeout tone reorder

### Syntax Description

reorder - tone - value

Reorder-tone timeout value, in seconds. Range is from 1 to 600. The default is 30.

### Command Default

30 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

The gateway uses the reorder tone timeout value when the call agent does not provide a timeout value associated with the
                              request to generate a reorder tone signal.

## Examples

The following example sets the reorder tone timeout value to 60 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tone reorder 60
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

## timeout tone ringback

To configure the ringback tone timeout value, use the timeout tone ringback command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tone ringback ringback-tone-value

no timeout tone ringback

### Syntax Description

ringback - tone - value

Ringback-tone timeout value, in seconds. Range is from 1 to 600. The default is 180.

### Command Default

180 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

The gateway uses the ringback tone timeout value when the call agent does not provide a timeout value associated with the
                              request to generate a ringback tone signal.

## Examples

The following example sets the ringback tone timeout value to 120 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tone ringback 120
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

## timeout tone ringback connection

To configure the timeout value for the ringback tone on connection, use the timeout tone ringback connection command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tone ringback connection connect-tone-value

no timeout tone ringback connection

### Syntax Description

connect - tone - value

Timeout value for the ringback tone on connection, in seconds. Range is from 1 to 600. The default is 180.

### Command Default

180 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

The gateway uses this value when the call agent does not provide a timeout value associated with the request to generate
                              the ringback tone signal on connection.

## Examples

The following example sets the timeout value for the ringback tone on connection to 120 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tone ringback connection 120
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

## timeout tone ringing

To configure the ringing tone timeout value, use the timeout tone ringing command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tone ringing ringing-tone-value

no timeout tone ringing

### Syntax Description

ringing - tone - value

Ringing tone timeout value, in seconds. Range is from 1 to 600. The default is 180.

### Command Default

180 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

The gateway uses the ringing tone timeout value when the call agent does not provide a timeout value associated with the
                              request to generate a ringing tone signal.

## Examples

The following example sets the ringing tone timeout value to 240 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tone ringing 240
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

## timeout tone ringing distinctive

To configure the distinctive ringing tone timeout value, use the timeout tone ringing distinctive command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tone ringing distinctive distinct-tone-value

no timeout tone ringing distinctive

### Syntax Description

distinct - tone - value

Distinctive-ringing tone timeout value, in seconds. Range is from 1 to 600. the default is 180.

### Command Default

180 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

The gateway uses the distinctive ringing tone timeout value when the call agent does not provide a timeout value associated
                              with the request to generate a signal for distinctive ringing.

## Examples

The following example sets the distinctive ringing tone timeout value to 240 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tone ringing distinctive 240
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

## timeout tpar

To configure the partial timeout value, T(partial), for the interdigit timer used in digit map matching, use the timeout tpar command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tpar tpar-value

no timeout tpar

### Syntax Description

tpar - value

Partial timeout value, T(partial), in seconds. Range is from 1 to 60. The default is 16.

### Command Default

16 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

The interdigit timer is used when matching digit maps. It is started when the first digit is entered, and is restarted after
                              each new digit is entered, until a digit map match or mismatch occurs.

The interdigit timer takes on one of two values, T(partial) or T(critical). When at least one more digit is required to make
                              a match to any of the patterns in the digit map, the value of T(partial) is used for the timer. If a timer is all that is
                              required to produce a match according to the digit map, T(critical) is used for the timer.

When the interdigit timer is used without a digit map, it takes on the value T(critical). It is started immediately and is
                              simply canceled (but not restarted) as soon as a digit is entered.

## Examples

The following example sets the partial timeout value to 15 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tpar 15
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

timeout tcrit

Configures the MGCP critical timeout value, T(critical), for the interdigit timer used in digit map matching.

## timeout tsmax

To configure the maximum timeout value after which MGCP messages are removed from the retransmission queue, use the timeout tsmax command in MGCP profile configuration mode. To reset to the default, use the no form of this command.

timeout tsmax tsmax-value

no timeout tsmax

### Syntax Description

tsmax - value

Timeout value for MGCP messages to be removed from the retransmission queue, in seconds. Range is from 1 to 100. The default
                                          is 20.

### Command Default

20 seconds

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for a Media Gateway Control Protocol (MGCP) profile.

The gateway uses the tsmax-value argument to determine how long to store MGCP messages before they are removed from the retransmission queue.

## Examples

The following example sets the timeout value for the maximum retransmission of MGCP messages to 45 seconds:

```
Router(config)# mgcp profile nyc-ca Router(config-mgcp-profile)# timeout tsmax 45
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

| Note | The documentation set for this product strives to use bias-free language. For purposes of this documentation set, bias-free
                                          is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity,
                                          sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language
                                          that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that
                                          is used by a referenced third-party product. |
|---|---|

| string | Alphanumeric identifier for the carrier ID. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| call filter match-list voice | Create a call filter match list for debugging voice calls. |
| debug condition match-list | Run a filtered debug on a voice call. |
| show call filter match-list | Display call filter match lists. |
| source carrier-id | Configure debug filtering for the source carrier ID. |
| source trunk-group-label | Configure debug filtering for a source trunk group. |
| target trunk-group-label | Configure debug filtering for a target trunk group. |

| group-number | A value from 0 to 23 that identifies the trunk group. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| call filter match-list voice | Create a call filter match list for debugging voice calls. |
| debug condition match-list | Run a filtered debug on a voice call. |
| show call filter match-list | Display call filter match lists. |
| source carrier-id | Configure debug filtering for the source carrier ID. |
| source trunk-group-label | Configure debug filtering for a source trunk group. |
| target carrier-id | Configure debug filtering for the target carrier ID. |

| all | Active TBCT calls on all interfaces. |
|---|---|
| interface | Active TBCT calls on a specified interface. Range is platform-dependent. |
| call - tag | (Optional) A specific active TBCT call on the specified interface, as identified by the unique call tag number. Range is 1
                                          to 4,294,967,295. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| isdn supp - service tbct | Enables ISDN TBCT on PRI trunks. |
| show call active voice redirect | Displays information about active calls that are being redirected using RTPvt or TBCT. |
| tbct max call - duration | Sets the maximum duration allowed for a call that is redirected using TBCT. |
| tbct max calls | Sets the maximum number of active calls that can use TBCT. |

| minutes | Maximum duration, in minutes, allowed for a single TBCT call. Range is 1 to 9999, in recommended increments of 5 minutes.
                                          Default is no limit. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Note | The call duration limit set by this command is not precisely enforced; calls may not be cleared after the exact number of
                                          minutes specified by this command. |
|---|---|

| Command | Description |
|---|---|
| isdn supp - service tbct | Enables ISDN TBCT on PRI trunks. |
| show call active voice redirect | Displays information about active calls that are being redirected using RTPvt or TBCT. |
| tbct clear call | Terminates billing statistics for one or more active TBCT calls. |
| tbct max calls | Sets the maximum number of active calls that can use TBCT. |

| number | Maximum number of currently active calls that can invoke TBCT at any one time. Range is 1 to 1,000,00. Default is no limit. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| isdn supp - service tbct | Enables ISDN TBCT on PRI trunks. |
| show call active voice redirect | Displays information about active calls that are being redirected using RTPvt or TBCT. |
| tbct clear call | Terminates billing statistics for one or more active TBCT calls. |
| tbct max call - duration | Sets the maximum duration allowed for a call that is redirected using TBCT. |

| count | Count range is 100-2000. Default retry count is 200. |
|---|---|
| close-connection | (Optional) Closes the connections after the configured
                                          						number of retries. |
| nolimit | Retry value is set to unlimited. |

| Release | Modification |
|---|---|
| 15.6(1)T | This command was introduced. |

| tdm - group - no | TDM group number. |
|---|---|
| timeslot | Time-slot number. |
| timeslot - list | Time-slot list. T1 range is 1 to 24. E1 range is 1 to 15
                                          						and 17 to 31. |
| type | (Optional) (Valid only when the mode cas command is
                                          						enabled.) Voice signaling type of the voice port. If configuring a TDM group
                                          						for data traffic only, do not specify the type keyword. Choose from one of the following options: e&m--E&M signaling fxs--Foreign
                                                						  Exchange Station signaling (optionally, you can also specify loop-start or
                                                						  ground-start) fxo--Foreign
                                                						  Exchange Office signaling (optionally, you can also specify loop-start or
                                                						  ground-start) fxs-melcas--Foreign Exchange Station MEL CAS fxo-melcas--Foreign Exchange Office MEL CAS e&m-melcas--E&M Mercury Exchange Limited Channel-Associated signaling
                                                						  (MEL CAS) The MELCAS options apply only to E1 lines and are used
                                          						primarily in the United Kingdom. |

| Release | Modification |
|---|---|
| 11.3(1)MA | This command was introduced on Cisco MC38310. |
| 12.1(1)T | This command was modified to include voice WAN interface
                                          						cards (VWICs) for Cisco 2600 series and Cisco 3600 series. |
| 12.1(2)T | This command was modified for the OC-3/STM-1 ATM Circuit
                                          						Emulation Service network module on Cisco 2600 series and Cisco 3600 series. |

| Note | Channel groups, CAS voice groups, DS0 groups, and TDM groups all
                                          		  use group numbers. All group numbers configured for channel groups, CAS voice
                                          		  groups, DS0 groups, and TDM groups must be unique on the local router. For
                                          		  example, you cannot use the same group number for a channel group and for a TDM
                                          		  group. |
|---|---|

| Command | Description |
|---|---|
| connect | Starts passage of data between ports for cross-connect TDM. |

| number | Defines the numbers used as the technology prefix. Each technology prefix can contain up to 11 characters. Although not strictly
                                          necessary, a pound (#) symbol is frequently used as the last character in a technology prefix. Valid characters are 0 though
                                          9, the pound (#) symbol, and the asterisk (*). |
|---|---|

| Release | Modification |
|---|---|
| 11.3(6)NA2 | This command was introduced on Cisco 2600 series and Cisco 3600 series. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Note | Cisco gatekeepers use the asterisk (*) as a reserved character. If you are using Cisco gatekeepers, do not use the asterisk
                                          as part of the technology prefix. |
|---|---|

| Command | Description |
|---|---|
| gw - type - prefix | Configures a technology prefix in the gatekeeper. |
| show gatekeeper gw - type - prefix | Displays the gateway technology prefix table. |

| phone-context | (Optional) Appends the phone context parameter to the TEL URL. |
|---|---|
| system | (Optional) Specifies that the To: Header (to hdr) Request URI to
                                          						telephone (TEL) format use the global sip-ua value. This keyword is available
                                          						only for the tenant mode to allow it to fallback to the global configurations. |

| Release | Modification |
|---|---|
| 12.4(22)YB | This
                                          						command was introduced. |
| 15.0(1)M | This
                                          						command was integrated into Cisco IOS Release 15.0(1)M. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants. |

| Command | Description |
|---|---|
| sip | Enters
                                          						SIP configuration mode from voice-service VoIP configuration mode. |
| voice - class tel-config to-hdr | Configures the To: Header request URI to telephone format for dial-peer VoIP
                                          						SIP calls. |

| setup | (Optional) Interactive setup tool for configuring Cisco Unified IP Phone 7910s, 7940s, and 7960s in Cisco Unified CME. Note This interactive Cisco CME setup tool is restricted to generating basic configuration files for Cisco Unified IP Phone 7910s,
                                                      7940s, and 7960s running SCCP protocol only. | Note | This interactive Cisco CME setup tool is restricted to generating basic configuration files for Cisco Unified IP Phone 7910s,
                                                      7940s, and 7960s running SCCP protocol only. |
|---|---|---|---|
| Note | This interactive Cisco CME setup tool is restricted to generating basic configuration files for Cisco Unified IP Phone 7910s,
                                                      7940s, and 7960s running SCCP protocol only. |

| Note | This interactive Cisco CME setup tool is restricted to generating basic configuration files for Cisco Unified IP Phone 7910s,
                                                      7940s, and 7960s running SCCP protocol only. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T. |
| 12.2(15)ZJ | Cisco CME 3.0 | The setup keyword was added. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release 12.3(4)T. |

| Note | The voice-gateway system is tied to the telephony service. The telephony-service command must be configured before the voice-gateway system is configured; otherwise, the voice gateway is hidden from the
                                          user. |
|---|---|

| Cisco CME Setup Tool Prompt | Description |
|---|---|
| Do you want to setup DHCP service for your IP phones? [yes/no]: If you respond yes, you see the following prompts: IP network for telephony-service DHCP  Pool:
Subnet mask for DHCP network : 
TFTP Server IP address (Option 150) :
Default Router for DHCP Pool : | Yes--Configures the Cisco Unified CME router to act as a Dynamic Host Configuration Protocol (DHCP) server, automatically
                                                   providing IP addresses to your IP phones and provisioning the default gateway and TFTP IP addresses to be used by the phones.
                                                   This method creates a single pool of IP addresses. If you need a pool for non-IP phones or if the Cisco router cannot act
                                                   as the DHCP router, answer no and manually define the DHCP server. No--Indicates that you have already configured DHCP or static IP addresses for the IP phones. |
| Do you want to start telephony-service setup? [yes/no]: | Yes-- Starts the interactive setup tool for configuring Cisco Unified IP Phone 7910s, 7940s, and 7960s. No --Terminates the Cisco CME setup tool. |
| Enter the IP source address for Cisco CallManager Express:
Enter the Skinny Port for Cisco CallManager Express:  [2000]: | IP address on which the router provides Cisco Unified CME services, usually the default gateway for the IP subnet that you
                                          are using for the IP phones, and the port for Skinny Client Control Protocol (SCCP) messages. |
| How many IP phones do you want to configure : [0]: | Enter the maximum number of IP phones that this Cisco Unified CME system will support. This number can be increased later,
                                          to the maximum allowed for this version and your router. Note The Cisco CME setup tool associates one number with each newly registering phone. You can manually add additional numbers
                                                      on a phone at a later time. | Note | The Cisco CME setup tool associates one number with each newly registering phone. You can manually add additional numbers
                                                      on a phone at a later time. |
| Note | The Cisco CME setup tool associates one number with each newly registering phone. You can manually add additional numbers
                                                      on a phone at a later time. |
| Do you want dual-line extensions assigned to phones? [yes for dual-line / no for single-line]: | Yes --Each newly registering IP phones is assigned a single number that is associated with a single phone button. The system generates
                                                   a dual-line ephone-dn entry for each ephone-dn. No --IP phones are linked directly to one or more PSTN trunk lines. Using keyswitch mode requires manual configuration in addition
                                                   to using the Cisco CME setup tool. The system generates two ephone-dn entries for each ephone-dn, and they are both assigned
                                                   to a single phone. |
| What language do you want on IP phones?
      0  English
      1  French
      2  German
      3  Russian
      4  Spanish
      5  Italian
      6  Dutch
      7  Norwegian
      8  Portuguese
      9  Danish
      10  Swedish
 [0]: | Language for IP phone displays, selected from the list. Default is 0, English. |
| Which Call Progress tone set do you want on IP phones :     
      0  United States
      1  France
      2  Germany
      3  Russia
      4  Spain
      5  Italy
      6  Netherlands
      7  Norway
      8  Portugal
      9  UK
    10  Denmark
    11  Switzerland
    12  Sweden
    13  Austria
    14  Canada
[0]: | Locale for the tone set used to indicate call status or progress, selected from the list. Default is 0, United States. |
| What is the first extension number you want to configure :[0]: | First number in pool of extension numbers to be created for IP phones connected to the Cisco router to be configured. Starting with this number, remaining extension numbers are automatically configured in a contiguous manner. This number must be compatible with your telephone number plan, and, if you use Direct Inward Dialing (DID) service, with
                                                public switched telephone network (PSTN) numbering requirements. |
| Do you have Direct-Inward-Dial service for all your phones? [yes/no]: | Yes--If you have trunk access to public telephone service by ISDN or VoIP for all extension numbers. The system creates an
                                                   appropriate dial plan. No--If you have simple analog phone lines only (for example, foreign exchange office [FXO] interfaces) or if you have trunk
                                                   access for some lines but not all lines. |
| If you answer yes to the previous question, you see the following prompt: Enter the full E.164 number for the first phone: | Complete 10-digit telephone number, including area code, that corresponds to the first extension number. |
| Do you want to forward calls to a voice message service? [yes/no]: | Yes--To forward calls to a single voice message service number when an IP phone is busy or does not answer. All phone extensions
                                                   forward their calls to the same voice message service pilot number. No--Not to forward calls to a single voice message service number. Answer no if you do not have a voice message system or
                                                   if you want to customize call-forwarding behavior for each extension. |
| If you answer yes to the previous question, you see the following prompt: Enter the extension or pilot number of the voice message service: | Voice message service pilot number. This step can be ignored during the setup dialog and manually configured later. |
| Call forward No Answer Timeout: [18]: | Timeout, in seconds, after which to forward calls to voice mail if they are not answered. Default is 18. |
| Do you wish to change any of the above information? [yes/no]: | Yes --Starts the dialog over again without implementing any of the answers that you previously gave. No --Uses specified values to automatically build basic configuration for Cisco Unified IP Phone 7910s, 7940s, and 7960s in Cisco
                                                   Unified CME. |

| Note | The Cisco CME setup tool associates one number with each newly registering phone. You can manually add additional numbers
                                                      on a phone at a later time. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(7)T | This command was introduced. |

| Command | Description |
|---|---|
| telephony-service ccm-compatible (H.323 voice-service) | Globally enables detection of Cisco CallManager in a network for all dial peers. |
| voice class h323 | Creates an H.323 voice class to apply to a dial peer. |
| voice-class h323 | Applies an H.323 voice class to a dial peer. |

| Release | Modification |
|---|---|
| 12.3(7)T | This command was introduced. |

| Command | Description |
|---|---|
| h323 | Enters H.323 voice-service configuration mode. |
| telephony-service ccm-compatible (H.323 voice-class) | Enables Cisco CallManager detection in a network by individual dial peers. |
| voice service voip | Enters voice-service configuration mode. |

| stream-id | The specific stream-id that is hung and should be deleted. |
|---|---|

| Release | Modification |
|---|---|
| 15.4(3)M | This command was introduced. |

| Packet Loss | Enter the packet loss, in percentage. Range is from 0 to
                                          						100. |
|---|---|
| RTT | Enter the round trip time, in ms (range 0 - 5000). |
| Jitter | Enter the jitter value caused by switches in the WAN, in ms
                                          						(range 0 - 2000). |

| Release | Modification |
|---|---|
| Cisco IOS XE Denali 16.3.1 | This command was introduced. |

| baudot45.45 | Configures baudot 45.45 TTY modulation. This is the default baud rate. |
|---|---|
| baudot50 | Configures baudot 50 TTY modulation. |
| autobaud-on | Enables the digital signal processors (DSPs) to autodetect the baud rate. This is the default autobaud setting. |
| autobaud-off | Disables the DSP capability to autodetect the baud rate. |

| Release | Modification |
|---|---|
| 12.4(6)T | This command was introduced. |

| Command | Description |
|---|---|
| text relay protocol | Configures the system-wide protocol type for text packets transmitted between gateways. |
| text relay rtp | Configures the RTP payload type and redundancy level. |

| cisco | (Optional) Uses the Cisco proprietary text relay protocol. |
|---|---|
| system | (Optional; dial peer voice configuration only) Uses the global configuration settings. |

| Release | Modification |
|---|---|
| 12.4(6)T | This command was introduced. |

| Command | Description |
|---|---|
| text relay modulation | Configures the TTY modulation on the gateway. |
| text relay rtp | Configures the RTP payload type and redundancy level. |

| payload-type
                                                { value \| default } | The RTP payload is the data transported by RTP in a packet. The value range is 98 to 117 for dynamic RTP payload types. The default value is 119, which is a static payload type. |
|---|---|---|
| redundancy level | Use the redundancy option to repeat data for redundancy and to lower the risk of packet loss. The redundancy level is the
                                          number of redundant text packets sent across the VoIP network. The range is 1 to 3. The default value is 2. |

| Release | Modification |
|---|---|
| 12.4(6)T | This command was introduced. |

| Command | Description |
|---|---|
| text relay modulation | Configures the TTY modulation on the gateway. |
| text relay protocol | Configures the system-wide protocol type for text packets transmitted between gateways. |

| domain-name | Domain name of the TFTP server. |
|---|---|
| local-addr ipv4 local-ip-address | Specifies the local interface IPv4
                                       address to connect to the core side
                                       server. |
| acc-addr ipv4 access-ip-address | Specifies the access side local
                                       interface IPv4 address. |

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |

| e164 | E.164 address family. |
|---|---|
| decimal | Decimal address family |
| penta-decimal | Penta-decimal address family |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| dial-peer voice | Enters dial-peer configuration mode and specifies the method of voice-related encapsulation. |

| csr | Call success rate. |
|---|---|
| ac | Available circuits. |
| tc | Total circuits. |
| carrier | Carrier-code address family. |
| trunk-group | Trunk-group address family. |
| disable | Disables advertisement of this dial peer. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| dial-peer voice | Enters dial-peer configuration mode and specifies the method of voice-related encapsulation. |

| csr | Call success rate. |
|---|---|
| ac | Available circuits. |
| tc | Total circuits. |
| disable | Disables advertisement on the trunk group. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Note | This command overrides the attributes set for advertisement using the global 
                                          advertise (tgrep)
                                          command. |
|---|---|

| Command | Description |
|---|---|
| advertise (tgrep) | Turns on reporting for a specified address family. |
| trunk group | Defines the trunk group and enters trunk group configuration mode. |

| itad-number | (Optional) IP Telephony Administrative Domain (ITAD) number associated with the gateway. The range is from 1 to 4294967295. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| address-family | Sets the global address family to be used on all dial peers. |
| advertise (tgrep) | Turns on reporting for a specified address family. |
| neighbor | Creates a TGREP session with another device. |

| value | Number that establishes a noise threshold. Valid values are from -30 to -90 decibels (dBs). The default is -62 dB. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(13b) | This command was introduced on the following platforms: Cisco 1700 Cisco 1751, Cisco 2600 (with and without the NM-HDA), Cisco
                                          3600 (with and without the NM-HDA), Cisco 7200 (with and without the NM-HDA), Cisco AS5300, Cisco AS5800, and Cisco MC3810. |
| 12.2(16) | This command was integrated into Cisco IOS Release 12.2(16). |

| time - in - seconds | Specifies the download timeout value in seconds. The range is from 0 to 3600. The default is 180. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)XY | This command was introduced on the Communication Media Module. |
| 12.3(14)T | This command was integrated into Cisco IOS Release 12.3(14)T. |

| Command | Description |
|---|---|
| auto - config | Enables auto-configuration or enters auto-config application configuration mode for the SCCPapplication. |
| show auto - config | Displays the current status of auto-configuration applications. |

| milliseconds | Timeout value for leg 3 preauthentication, in milliseconds. Range is from 100 to 1000. The default is 100. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| aaa preauth | Enters AAA preauthentication configuration mode. |

| rcv | Applies the specified time limit to the reception of voice packets. |
|---|---|
| xmt | Applies the specified time limit to the transmission of voice packets. |
| minutes | Maximum time, in minutes, allowed for transmitting or receiving a voice packet. Range is integers from 1 to 30. |

| Release | Modification |
|---|---|
| 12.3(4)XD | This command was introduced. |
| 12.3(7)T | This command was integrated into Cisco IOS Release 12.3(7)T. |

| tcrit - value | Critical timeout value, T(critical), in seconds. Range is from 1 to 600. Default is 4. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |
| timeout tpar | Configures the MGCP partial timeout value, T(partial), for the interdigit timer used in digit map matching. |

| tdinit - value | Initial waiting delay (Tdinit) for the disconnected procedure, in seconds. The disconnected timer is initialized to a randomly
                                          selected value between 0 and Tdinit. Range is from 1 to 30. Default is 15. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |
| timeout tdmax | Configures the maximum timeout for the MGCP disconnected procedure. |
| timeout tdmin | Configures the minimum timeout for the MGCP disconnected procedure. |

| tdmax - value | Maximum timeout value (Tdmax) for the disconnected procedure, in seconds. Range is from 300 to 600. The default is 600. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |
| timeout tdinit | Configures the initial timeout for the MGCP disconnected procedure. |
| timeout tdmin | Configures the minimum timeout for the MGCP disconnected procedure. |

| tdmin - value | Minimum timeout (Tdmin) for the disconnected procedure, in seconds. Range is from 1 to 30. The default is 15. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |
| timeout tdinit | Configures the initial timeout for the MGCP disconnected procedure. |
| timeout tdmax | Configures the maximum timeout for the MGCP disconnected procedure. |

| thist - value | Package storage timeout (Thist), in seconds. Range is from 1 to 60. The default is 30. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints, or to configure
                                          the default profile. |

| busy - tone - value | Busy-tone timeout, in seconds. Range is from 1 to 600. The default is 30. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |

| cot1 - tone - value | Continuity1 (cot1) tone timeout, in seconds. Range is from 1 to 600. The default is 3. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |
| timeout tone cot2 | Sets the continuity2 tone timeout value for MGCP. |

| cot2 - tone - value | Continuity2 (cot2) tone timeout, in seconds. Range is from 1 to 600. The default is 3. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |
| timeout tone cot1 | Sets the continuity1 tone timeout value for MGCP. |

| dial - tone - value | Dial tone timeout value, in seconds. Range is from 1 to 600. The default is 16. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |

| stutter - value | Timeout value for the stutter dial tone, in seconds. Range is from1 to 600. The default is 16. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |

| mwi - tone - value | Message-waiting-indicator (MWI) tone timeout value, in seconds. Range is from 1 to 600. The default is 16. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |

| congestion | Timeout for network congestion. |
|---|---|
| busy | Timeout for network busy. |
| tone - value | Tone timeout value, in seconds. Range is from 1 to 600. The default is 180. |

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |
| 12.4(9)T | The busy keyword was introduced. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |

| reorder - tone - value | Reorder-tone timeout value, in seconds. Range is from 1 to 600. The default is 30. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |

| ringback - tone - value | Ringback-tone timeout value, in seconds. Range is from 1 to 600. The default is 180. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |

| connect - tone - value | Timeout value for the ringback tone on connection, in seconds. Range is from 1 to 600. The default is 180. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |

| ringing - tone - value | Ringing tone timeout value, in seconds. Range is from 1 to 600. The default is 180. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |

| distinct - tone - value | Distinctive-ringing tone timeout value, in seconds. Range is from 1 to 600. the default is 180. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |

| tpar - value | Partial timeout value, T(partial), in seconds. Range is from 1 to 60. The default is 16. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |
| timeout tcrit | Configures the MGCP critical timeout value, T(critical), for the interdigit timer used in digit map matching. |

| tsmax - value | Timeout value for MGCP messages to be removed from the retransmission queue, in seconds. Range is from 1 to 100. The default
                                          is 20. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |