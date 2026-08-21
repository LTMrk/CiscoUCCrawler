---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-command-reference-srstcr-srsa-n-z-html-22765bfd16
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/command/reference/srstcr/srsa_n_z.html
retrieved_at: 2026-08-21T10:07:02.077059+00:00
---

Cisco Unified SRST and Cisco Unified SIP SRST Command Reference (All Versions)

# Cisco Unified SRST and Cisco Unified SIP SRST Command Reference (All Versions)

## Results

Updated: April 21, 2026

Chapter: Command Reference:
	 N through Z

## Chapter: Command Reference:
	 N through Z

# Command Reference:
                     	 N through Z

This chapter contains commands to configure and maintain Cisco Unified Survivable Remote Site Telephony (SRST) and Cisco Unified
                        SIP SRST. The commands are presented in alphabetical order. Some commands required for configuring Cisco Unified SRST and
                        Cisco Unified SIP SRST may be found in other Cisco IOS command references. Use the command reference primary index or search
                        online to find these commands.

## name (voice emergency response location)

To describe or identify an emergency response location, use the name command in voice emergency response
                              		  location mode. To remove this definition, use the no form of this command.

name string

no name

### Syntax Description

string

String (30 characters) used to describe or identify an
                                          						ERL’s location.

### Command Default

The location is not described.

### Command Modes

Voice emergency response location configuration (cfg-emrgncy-resp-location)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to enable a word or description of the ERL for
                              		  administrative purposes. Most commonly, use this command to identify the
                              		  location for the network administrator.

## Examples

In this example, the location description is Widget Incorporated.

```
voice emergency response location 60
subnet 1 209.165.200.224 255.255.0.0
elin 1 4085550101
name Widget Incorporated,
```

### Related Commands

Command

Description

address

Specifies a comma separated text entry (up to 247
                                          						characters) of an ERL’s civic address.

elin

Specifies a PSTN number that will replace the caller’s
                                          						extension.

subnet

Defines which IP phones are part of this ERL.

voice emergency response location

Creates a tag for identifying an ERL for E911 services.

## name (voice hunt-group)

To associate a name with a called voice hunt group, use the name command in voice hunt-group
                              		  configuration mode. To dissociate the name of the called voice hunt group, use
                              		  the no form of this command.

name "primary pilot name" [secondary "secondary pilot name" ]

no name "primary pilot name " [secondary "secondary pilot name" ]

### Syntax Description

“primary pilot name”

Name of primary pilot number.

secondary “secondary pilot name”

(Optional) Name of secondary pilot number.

### Command Default

No name is associated with the called voice hunt group.

### Command Modes

Voice hunt-group configuration (config-voice-hunt-group)

## Command History

Release

Modification

15.3(2)T

This command was introduced.

### Usage Guidelines

In Cisco Unified SRST 9.5, when the secondary pilot name is not
                              		  explicitly configured, the primary pilot name is applicable to both pilot
                              		  numbers.

## Examples

The following example configures the primary pilot name for both the
                              		  primary and the secondary pilot numbers:

```
name SALES
```

The following example configures different names for the primary and
                              		  secondary pilot numbers:

```
name SALES secondary SALES-SECONDARY
```

The following example associates a two-word name for the primary
                              		  pilot number and a one-word name for the secondary pilot number:

```
name “CUSTOMER SERVICE” secondary CS
```

The following example associates a one-word name for the primary
                              		  pilot number and a two-word name for the secondary pilot number:

```
name FINANCE secondary “INTERNAL ACCOUNTING”
```

The following example associates two-word names for the primary and
                              		  secondary pilot numbers:

```
name “INTERNAL CALLER” secondary “EXTERNAL CALLER”
```

When incoming call A reaches voice hunt group B and lands on final C,
                              		  extension C does not show the name of the forwarder because the voice hunt
                              		  group is not configured to display the name. To display the name of the
                              		  forwarder and the final number, two separate names are required for the primary
                              		  and secondary pilots.

The following example shows how the primary and secondary pilot names
                              		  are configured in voice hunt-group configuration mode:

```
voice hunt-group 24 parallel
   final 097
   list 885,886,124,154
   timeout 20 
   pilot 021 secondary 621 name SALES secondary SALES-SECONDARY
```

The following is a sample output of the show voice hunt-group command when the primary and secondary pilot names are
                              		  configured in voice hunt-group configuration mode:

```
show voice hunt-group 1
Group 1
    type: parallel
    pilot number: 1000, peer-tag 2147483647
    secondary number: 2000, peer-tag 2147483646 pilot name: SALES secondary name: SALES-SECONDARY list of numbers: 2004,2005
```

### Related Commands

Command

Description

voice hunt-group

Enters voice hunt-group configuration mode and creates a
                                          						hunt group for phones in a Cisco Unified CME system.

show voice hunt-group

Displays configuration information associated with one or
                                          						all voice hunt groups in a Cisco Unified CME system.

## number (voice register pool)

To indicate the E.164 phone numbers that the registrar permits to
                              		  handle the Register message from a Cisco Unified SIP IP phone, use the number command in voice register pool
                              		  configuration mode. To disable number registration, use the no form of this command.

number tag { number-pattern [ preference value ] [ huntstop ] | dn dn-tag }

no number tag

### Syntax Description

tag

Telephone number when there are multiple number commands. Range is 1 to 114.

number-pattern

Phone numbers (including wild cards and patterns) that are
                                          						permitted by the registrar to handle the Register message from the Cisco
                                          						Unified SIP IP phone.

preference value

(Optional) Defines the number list preference order. Range
                                          						is 0 to 10. The highest preference is 0. There is no default.

huntstop

(Optional) Stops hunting when the dial peer is busy.

dn dn-tag

Identifies the directory number tag for this phone number
                                          						as defined by the voice register dn command. Range is 1 to 288.

### Command Default

Cisco Unified SIP IP phones cannot register in Cisco Unified CME.

### Command Modes

Voice register pool configuration (config-register-pool)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SIP SRST 3.0

This command was introduced.

12.3(4)T

Cisco SIP SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was added to Cisco CME and the dn keyword was added.

12.4(11)XJ

Cisco Unified CME 4.1 Cisco Unified SRST 4.1

This command was modified. The number-pattern argument and preference and huntstop keywords were removed from
                                          						Cisco Unified CME.

12.4(15)T

Cisco Unified CME 4.1 Cisco Unified SRST 4.1

The modifications to this command were integrated into
                                          						Cisco IOS Release 12.4(15)T.

15.2(4)M

Cisco Unified CME 9.1 Cisco Unified SIP SRST 9.1

This command was modified to increase the valid value of
                                          						the tag argument to 114.

### Usage Guidelines

The number command indicates the phone numbers
                              		  that are permitted by the registrar to handle the Register message from the
                              		  Cisco Unified SIP IP phone.

In Cisco Unified SRST, the keywords and arguments of this command
                              		  allow for more explicit setting of user preferences regarding what number
                              		  patterns should match the voice register pool.

## Examples

The following example shows three directory numbers assigned to Cisco
                              		  Unified SIP IP phone 1 in Cisco Unified CME:

```
!
voice register pool  1
 id mac 0017.E033.0284
 type 7961
 number 1 dn 10
 number 2 dn 12
 number 3 dn 13
 codec g711ulaw
!
```

The following example shows directory numbers 10, 12, and 13 assigned
                              		  to phone numbers 1, 2, and 55 of Cisco Unified SIP IP phone 2:

```
voice register pool 2
id mac 0017.E033.0284
type 7961
number 1 dn 10
number 2 dn 12
number 55 dn 13
codec g711ulaw
```

The following example shows a telephone number pattern set to 95...
                              		  in Cisco Unified SRST. This means all five-digit numbers beginning with 95 are
                              		  permitted by the registrar to handle the Register message.

```
voice register pool 3
 id network 10.2.161.0 mask 255.255.255.0
 number 1 95... preference 1
 cor incoming call95 1 95011
```

### Related Commands

Command

Description

id (voice register pool)

Explicitly identifies a locally available, individual Cisco
                                          						Unified SIP IP phone or, when running Cisco Unified SIP SRST, a set of Cisco
                                          						Unified SIP IP phones.

voice register dn

Enters voice register dn configuration mode to define an
                                          						extension for a phone line, intercom line, voice-mail port, or a
                                          						message-waiting indicator.

## outbound-proxy system

To specify that all Cisco Unified Communications Manager Express
                              		  (Cisco Unified CME) line-side phones connected to a Cisco IOS voice gateway use
                              		  the global settings for forwarding Session Initiation Protocol (SIP) messages
                              		  to an outbound proxy, use the outbound-proxy system command in voice register global
                              		  configuration mode. To disable the SIP outbound proxy function for Cisco
                              		  Unified CME line-side SIP phones, use the no form of this command.

outbound-proxy system

no outbound-proxy system

### Syntax Description

This command has no arguments or keywords.

### Command Default

The SIP outbound proxy function for all SIP line-side phones in Cisco
                              		  Unified CME is enabled and behavior is determined by the global setting on the
                              		  Cisco IOS gateway.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XZ

Cisco Unified CME 4.3 Cisco Unified SIP SRST 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

If global configuration for outbound proxy is enabled on the Cisco
                              		  IOS voice gateway and Cisco Unified CME receives a call, Cisco Unified CME
                              		  forwards all SIP messages to the outbound proxy causing incoming calls to
                              		  line-side SIP phones to fail. This is the default behavior.

To avoid these failed calls, use the no form of this command in voice register global configuration
                              		  mode to override global outbound proxy settings for the gateway and disable the
                              		  outbound proxy function for all line-side SIP phones connected to Cisco Unified
                              		  CME.

To configure outbound proxy settings for an individual dial peer on
                              		  the gateway, use the voice-class sip outbound-proxy command in dial peer voice
                              		  configuration mode .

## Examples

The following example shows how to disable the global outbound proxy
                              		  feature for all line-side SIP phones on a Cisco Unified CME:

```
Router> enable Router# configure terminal Router(config)# voice register global Router(config-register-global)# no outbound-proxy
```

### Related Commands

Command

Description

voice-class sip outbound-proxy

Configures SIP outbound proxy settings for an individual
                                          						dial peer that override global settings for the Cisco IOS voice gateway.

## overlap-signal

To configure overlap dialing in SCCP or SIP IP phones, use the
                              		  overlap-signal command in ephone, ephone-template, telephony-service, voice
                              		  register pool, voice register global, or voice register template configuration
                              		  mode.

overlap-signal

### Syntax Description

This command has no arguments or keywords.

### Command Default

Overlap-signal is disabled.

### Command Modes

Call-manager-fallback Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template) Telephony-service configuration (config-telephony) Voice register pool (config-register-pool) Voice register global configuration (config-register-global) Voice register template (config-register-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5 Cisco Unified SRST 8.5

This command was introduced.

### Usage Guidelines

SCCP IP phones

In SCCP IP phones, overlap dialing is enabled when the overlap signal
                              		  command is configured in ephone, ephone-template, and telephony-service
                              		  configurations modes.

SIP IP phones

In SIP IP Phones, overlap dialing is enabled when the overlap signal
                              		  command is configured in voice register pool, voice register global, and voice
                              		  register template configuration modes.

Cisco Unified SRST

In Cisco Unified SRST, overlap dialing is enabled on SCCP IP phones
                              		  when overlap signal command is configured in call-manager-fallback
                              		  configuration mode.

## Examples

The following example shows overlap-signal enabled on SCCP phones:

```
Router# show running config
!
!
telephony-service
 max-ephones 25
 max-dn 15
 load 7906 SCCP11.8-5-3S.loads
 load 7911 SCCP11.8-5-3S.loads
 load 7921 CP7921G-1.3.3.LOADS
 load 7941 SCCP41.8-5-3S.loads
 load 7942 SCCP42.8-5-3S.loads
 load 7961 SCCP41.8-5-3S.loads
 load 7962 SCCP42.8-5-3S.loads
 max-conferences 12 gain -6
 web admin system name cisco password cisco
 transfer-system full-consult
 create cnf-files version-stamp Jan 01 2002 00:00:00
 overlap-signal
!
ephone-template  1
 button-layout 1 line
 button-layout 3-6 blf-speed-dial
!
ephone-template  9
 feature-button 1 Endcall
 feature-button 3 Mobility
!
!
ephone-template  10
 feature-button 1 Park
 feature-button 2 MeetMe
 feature-button 3 CallBack
 button-layout 1 line
 button-layout 2-4 speed-dial
 button-layout 5-6 blf-speed-dial
 overlap-signal
!
ephone  10
 device-security-mode none
 mac-address 02EA.EAEA.0010
 overlap-signal
```

!

The following example shows overlap-signal configured in voice
                              		  register global and voice register pool 10:

```
Router#show running config
!
!
!
voice service voip
 ip address trusted list
  ipv4 20.20.20.1
 media flow-around
 allow-connections sip to sip
!
voice class media 10
 media flow-around
!
!
voice register global
 max-pool 10
 overlap-signal
!
voice register pool  5
 overlap-signal
!
!
!
```

The following example shows overlap-signal configured in
                              		  call-manager-fallback mode:

```
Router# show run | sec call-manager
call-manager-fallback
 max-conferences 12 gain -6
 transfer-system full-consult
 overlap-signal
```

## pattern direct (vm-integration)

To configure the dual-tone multifrequency (DTMF) digit pattern
                              		  forwarding necessary to activate the voice-mail system when the user presses
                              		  the messages button on the phone, use the pattern direct command in voice-mail integration configuration mode. To
                              		  disable DTMF digit pattern forwarding when the user presses the messages button
                              		  on the phone, use the no form of this command.

pattern direct tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

no pattern direct tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [last-tag]

### Syntax Description

tag1

Alphanumeric string fewer than four DTMF digits in length.
                                          						The alphanumeric string consists of a combination of four letters (A,B,C, and
                                          						D), two symbols (* and #), and ten digits (0 to 9). The tag numbers match the
                                          						numbers defined in the voice-mail system’s integration file, immediately
                                          						preceding either the number of the calling party, the number of the called
                                          						party, or a forwarding number.

tag2 and tag3

(Optional) See tag1.

last-tag

(Optional) See tag1 . This tag indicates the end of
                                          						the pattern.

CGN

Calling number (CGN) information is sent to the voice-mail
                                          						system.

CDN

Called number (CDN) information is sent to the voice-mail
                                          						system.

FDN

Forwarding number (FDN) information is sent to the
                                          						voice-mail system.

### Command Default

This feature is disabled.

### Command Modes

Voice-mail integration configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco SRST 2.0

This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

12.2(13)T

Cisco SRST 2.02

This command was introduced for Cisco SRST Version 2.02.

### Usage Guidelines

The pattern direct command is used to configure the sequence
                              		  of DTMF digits passed to a voice-mail system attached to the router through one
                              		  or more voice ports. When a call is placed directly from a Cisco IP phone
                              		  attached to the router, the voice-mail system expects to receive a sequence of
                              		  DTMF digits at the beginning of the call that identify the mailbox of the user
                              		  calling the voice-mail system accompanied by a string of digits indicating that
                              		  the caller is attempting to access the designated mailbox in order to retrieve
                              		  messages.

## Examples

The following example sets the DTMF pattern for a calling number
                              		  (CGN) for a direct call to the voice-mail system:

```
Router(config)# vm-integration Router(config-vm-integration)# pattern direct 2 CGN
```

### Related Commands

Command

Description

pattern ext-to-ext busy (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension attempts to connect
                                          						to a busy extension and the call is forwarded to voice mail

pattern ext-to-ext no-answer (vm- integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail.

pattern trunk-to-ext busy (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail.

pattern trunk-to-ext no-answer (vm- integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail.

vm-integration

Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and analog voice-mail systems.

## pattern ext-to-ext busy (vm-integration)

To configure the dual-tone multifrequency (DTMF) digit pattern
                              		  forwarding necessary to activate the voice-mail system once an internal
                              		  extension attempts to connect to a busy extension and the call is forwarded to
                              		  voice mail, use the pattern ext-to-ext busy command in voice-mail integration configuration mode. To
                              		  disable DTMF digit pattern forwarding when an internal extension calls a busy
                              		  extension and the call is forwarded to a voice-mail system, use the no form of this command.

pattern ext-to-ext busy tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [last-tag]

no pattern ext-to-ext busy tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [last-tag]

### Syntax Description

tag1

Alphanumeric string fewer than four DTMF digits in length.
                                          						The alphanumeric string consists of a combination of four letters (A,B,C, and
                                          						D), two symbols (* and #), and ten digits (0 to 9). The tag numbers match the
                                          						numbers defined in the voice-mail system’s integration file, immediately
                                          						preceding either the number of the calling party, the number of the called
                                          						party, or a forwarding number.

tag2 and tag3

(Optional) See tag1.

last-tag

(Optional) See tag1 . This tag indicates the end of
                                          						the pattern.

CGN

Calling number (CGN) information is sent to the voice-mail
                                          						system.

CDN

Called number (CDN) information is sent to the voice-mail
                                          						system.

FDN

Forwarding number (FDN) information is sent to the
                                          						voice-mail system.

### Command Default

This feature is disabled.

### Command Modes

Voice-mail integration configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco SRST 2.0

This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

12.2(13)T

Cisco SRST 2.02

This command was introduced for Cisco SRST Version 2.02.

### Usage Guidelines

The pattern ext-to-ext busy command is used to configure the sequence of
                              		  DTMF digits passed to a voice-mail system attached to the router through one or
                              		  more voice ports. When a call is routed to the voice-mail system by call
                              		  forward on busy from a Cisco IP phone attached to the router, the voice-mail
                              		  system expects to receive a sequence of digits identifying the mailbox
                              		  associated with the forwarding phone together with digits that identify the
                              		  extension number of the calling IP phone.

## Examples

The following example sets the DTMF pattern for a local call
                              		  forwarded on busy to the voice-mail system:

```
Router(config)# vm-integration Router(config-vm-integration)# pattern ext-to-ext busy 7 FDN * CGN *
```

### Related Commands

Command

Description

pattern direct (vm- integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the messages button on the
                                          						phone.

pattern ext-to-ext no-answer (vm- integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail.

pattern trunk-to-ext busy (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail.

pattern trunk-to-ext no-answer (vm- integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail.

vm-integration

Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and analog voice-mail systems.

## pattern ext-to-ext no-answer (vm-integration)

To configure the dual-tone multifrequency (DTMF) digit pattern
                              		  forwarding necessary to activate the voice-mail system once an internal
                              		  extension fails to connect to an extension and the call is forwarded to voice
                              		  mail, use the pattern ext-to-ext no-answer command in voice-mail integration configuration mode. To
                              		  disable DTMF digit pattern forwarding when an internal extension fails to
                              		  connect to an extension and the call is forwarded to a voice-mail system, use
                              		  the no form of this command.

pattern ext-to-ext no-answer tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [last-tag]

no pattern ext-to-ext no-answer tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [last-tag]

### Syntax Description

tag1

Alphanumeric string fewer than four DTMF digits in length.
                                          						The alphanumeric string consists of a combination of four letters (A,B,C, and
                                          						D), two symbols (* and #), and ten digits (0 to 9). The tag numbers match the
                                          						numbers defined in the voice-mail system’s integration file, immediately
                                          						preceding either the number of the calling party, the number of the called
                                          						party, or a forwarding number.

tag2 and tag3

(Optional) See tag1.

last-tag

(Optional) See tag1 . This tag indicates the end of
                                          						the pattern.

CGN

Calling number (CGN) information is sent to the voice-mail
                                          						system.

CDN

Called number (CDN) information is sent to the voice-mail
                                          						system.

FDN

Forwarding number (FDN) information is sent to the
                                          						voice-mail system.

### Command Default

This feature is disabled.

### Command Modes

Voice-mail integration configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco SRST 2.0

This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

12.2(13)T

2.02

This command was introduced for Cisco SRST Version 2.02.

### Usage Guidelines

The pattern ext-to-ext no-answer command is used to configure the
                              		  sequence of DTMF digits passed to a voice-mail system attached to the router
                              		  through one or more voice ports. When a call is routed to the voice-mail system
                              		  by call forward on no-answer from an IP phone attached to the router, the
                              		  voice-mail system expects to receive a sequence of digits identifying the
                              		  mailbox associated with the forwarding phone together with digits that identify
                              		  the extension number of the calling IP phone.

## Examples

The following example sets the DTMF pattern for a local call
                              		  forwarded on no-answer to the voice-mail system:

```
Router(config)# vm-integration Router(config-vm-integration)# pattern ext-to-ext no-answer 5 FDN * CGN *
```

### Related Commands

Command

Description

pattern direct (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the messages button on the
                                          						phone.

pattern ext-to-ext busy (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail.

pattern trunk-to-ext busy (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail.

pattern trunk-to-ext no-answer (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail.

vm-integration

Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and analog voice-mail systems.

## pattern trunk-to-ext busy (vm-integration)

To configure the dual-tone multifrequency (DTMF) digit pattern
                              		  forwarding necessary to activate the voice-mail system once an external trunk
                              		  call reaches a busy extension and the call is forwarded to voice mail, use the pattern trunk-to-ext busy command in voice-mail integration configuration mode. To
                              		  disable DTMF digit pattern forwarding when an external trunk call reaches a
                              		  busy extension and the call is forwarded to a voice-mail system, use the no form of this command.

pattern trunk-to-ext busy tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [last-tag]

no pattern trunk-to-ext busy tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [last-tag]

### Syntax Description

tag1

Alphanumeric string fewer than four DTMF digits in length.
                                          						The alphanumeric string consists of a combination of four letters (A,B,C, and
                                          						D), two symbols (* and #), and ten digits (0 to 9). The tag numbers match the
                                          						numbers defined in the voice-mail system’s integration file, immediately
                                          						preceding either the number of the calling party, the number of the called
                                          						party, or a forwarding number.

tag2 and tag3

(Optional) See tag1.

last-tag

(Optional) See tag1 . This tag indicates the end of
                                          						the pattern.

CGN

Calling number (CGN) information is sent to the voice-mail
                                          						system.

CDN

Called number (CDN) information is sent to the voice-mail
                                          						system.

FDN

Forwarding number (FDN) information is sent to the
                                          						voice-mail system.

### Command Default

This feature is disabled.

### Command Modes

Voice-mail integration configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco SRST 2.0

This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

12.2(13)T

Cisco SRST 2.02

This command was introduced for Cisco SRST Version 2.02.

### Usage Guidelines

The pattern trunk-to-ext busy command is used to configure the sequence of
                              		  DTMF digits passed to a voice-mail system attached to the router through one or
                              		  more voice ports. When a call is routed to the voice-mail system by call
                              		  forward on busy from an IP phone attached to the router, the voice-mail system
                              		  expects to receive a sequence of digits identifying the mailbox associated with
                              		  the forwarding phone together with digits indicating that the call originated
                              		  from a PSTN or VoIP caller.

## Examples

The following example sets the DTMF pattern for call forwarding when
                              		  an external trunk call reaches a busy extension and the call is forwarded to
                              		  the voice-mail system:

```
Router(config)# vm-integration Router(config-vm-integration)# pattern trunk-to-ext busy 6 FDN * CGN *
```

### Related Commands

Command

Description

pattern direct (vm- integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the messages button on the
                                          						phone.

pattern ext-to-ext busy (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension attempts to connect
                                          						to a busy extension and the call is forwarded to voice mail.

pattern ext-to-ext no-answer (vm- integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail.

pattern trunk-to-ext no-answer (vm- integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail.

vm-integration

Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and analog voice-mail systems.

## pattern trunk-to-ext no-answer (vm-integration)

To configure the dual-tone multifrequency (DTMF) digit pattern
                              		  forwarding necessary to activate the voice-mail system when an external trunk
                              		  call reaches an unanswered extension and the call is forwarded to voice mail,
                              		  use the pattern trunk-to-ext no-answer command in voice-mail integration configuration mode. To
                              		  disable DTMF digit pattern forwarding when an external trunk call reaches
                              		  another extension where the called party does not answer and the call is
                              		  forwarded to a voice-mail system, use the no form of this command.

pattern trunk-to-ext no-answer tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [last-tag]

no pattern trunk-to-ext no-answer tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [last-tag]

### Syntax Description

tag1

Alphanumeric string fewer than four DTMF digits in length.
                                          						The alphanumeric string consists of a combination of four letters (A,B,C, and
                                          						D), two symbols (* and #), and ten digits (0 to 9). The tag numbers match the
                                          						numbers defined in the voice-mail system’s integration file, immediately
                                          						preceding either the number of the calling party, the number of the called
                                          						party, or a forwarding number.

tag2 and tag3

(Optional) See tag1.

last-tag

(Optional) See tag1 . This tag indicates the end of
                                          						the pattern.

CGN

Calling number (CGN) information is sent to the voice-mail
                                          						system.

CDN

Called number (CDN) information is sent to the voice-mail
                                          						system.

FDN

Forwarding number (FDN) information is sent to the
                                          						voice-mail system.

### Command Default

This feature is disabled.

### Command Modes

Voice-mail integration configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco SRST 2.0

This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

12.2(13)T

Cisco SRST 2.02

This command was introduced for Cisco SRST Version 2.02.

### Usage Guidelines

The pattern trunk-to-ext no-answer command is used to configure the sequence of DTMF digits passed
                              		  to a voice-mail system attached to the router through one or more voice ports.
                              		  When a call is routed to the voice-mail system by call forward on no-answer
                              		  from an IP phone attached to the router, the voice-mail system expects to
                              		  receive a sequence of digits identifying the mailbox associated with the
                              		  forwarding phone together with digits indicating that the call originated from
                              		  a PSTN or VoIP caller.

## Examples

The following example sets the DTMF pattern for call forwarding when
                              		  an external trunk call reaches an unanswered extension and the call is
                              		  forwarded (FDN) to a voice-mail system:

```
Router(config)# vm-integration Router(config-vm-integration)# pattern trunk-to-ext no-answer 4 FDN * CGN *
```

### Related Commands

Command

Description

pattern direct (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the messages button on the
                                          						phone.

pattern ext-to-ext busy (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension attempts to connect
                                          						to a busy extension and the call is forwarded to voice mail.

pattern ext-to-ext no-answer (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail.

pattern trunk-to-ext busy (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail.

vm-integration

Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and analog voice-mail systems.

## phoneload

To define the phone firmware support for a phone type, use the phoneload command in ephone-type configuration mode. To remove firmware
                              		  support, use the no form of this command.

phoneload

no phoneload

### Syntax Description

This command has no arguments or keywords.

### Command Default

Phone type supports firmware configuration.

### Command Modes

Ephone-type configuration (config-ephone-type)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XZ

Cisco Unified CME 4.3 Cisco Unified SRST 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command specifies whether the phone type defined in the
                              		  phone-type template supports firmware configuration using the load command.

## Examples

The following example shows that support for phone firmware is
                              		  disabled for the Nokia E61 phone type:

```
Router(config)# ephone-type E61 Router(config-ephone-type)# no phoneload
```

### Related Commands

Command

Description

device-name

Assigns a name to a phone type in an ephone-type template.

load

Associates a type of Cisco Unified IP phone with a phone
                                          						firmware file.

## phone-display

To enable a
                              		  SIP/SCCP phone user to display hunt group related information using the
                              		  Services button on the phone, use the phone-display command in voice hunt-group configuration mode. To reset to the default value,
                              		  use the no form of this command.

phone-display

no phone-display

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

By default, this
                              		  command is enabled.

### Command Modes

Voice register template configuration (config-hunt-group)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

This command
                              		  enables the user to display hunt group information on the phone.

## Examples

The following
                              		  example shows that voice hunt group display option is disabled for phone 7:

```
Router(config)# ephone 7 Router(config-ephone-type)# no phone-ui voice-hunt-groups
```

## phone-mode
                        	 only

To enable Jabber
                              		  phone-only client suppor, use the phone-mode only command. To exit the configuration, use the no form of the command.

phone-mode phone-only

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

Privileged EXEC
                              		  mode

### Command Modes

Voice register global

Voice register pool

Voice register template

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

This command
                              		  enables Jabber client support for MAC, iPhone, iPad and android for SCCP and
                              		  SIP phones.

## Examples

The following
                              		  example shows that phone-mode is enabled:

```
Router(config)# voice register pool Router(config-telephony)# phone-mode phone-only
```

### Related Commands

Command

Description

Voice register global

Enters
                                          						voice register global configuration mode.

Voice register pool

Enters
                                          						voice register pool configuration mode.

Voice register template

Enters
                                          						voice register template configuration mode.

## pickup
                        	 (call-manager-fallback)

To enable the
                              		  PickUp soft key on all Cisco IP phones, allowing an external Direct Inward
                              		  Dialing (DID) call coming into one extension to be picked up from another
                              		  extension during SRST, use the pickup command in call-manager-fallback configuration mode. To disable
                              		  the PickUp soft key on all Cisco IP phones during SRST, use the no form of
                              		  this command.

pickup telephone-number

no pickup telephone-number

### Syntax Description

telephone-number

The
                                          						telephone number to match an incoming called number.

### Command Default

The PickUp soft
                              		  key is disabled.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.3(7)XL

Cisco
                                          						SRST 3.1.1

This
                                          						command was introduced.

12.3(11)T

Cisco
                                          						SRST 3.2

This
                                          						command was integrated into Cisco IOS Release 12.3(11)T.

### Usage Guidelines

Configuring the pickup command enables the PickUp soft key on all SRST phones. You can then press the
                              		  PickUp key and answer any currently ringing IP phone that has a DID called
                              		  number that matches the configured telephone-number . This command does not enable the
                              		  Group PickUp (GPickUp) soft key.

When a user
                              		  presses the PickUp soft key, SRST searches through all the SRST phones to find
                              		  a ringing call that has a called number that matches the configured > telephone-number . When a match is found, the call
                              		  is automatically forwarded to the extension number of the phone that requested
                              		  the call pickup.

The SRST pickup command is designed to operate in a manner compatible with
                              		  Cisco Unified Communications Manager.

## Examples

In SRST, the pickup command is best used with the alias command. The following output from the show running-config command shows the pickup command and the alias command configured to provide call routing for a pilot number
                              		  of a hunt group:

```
call-manager-fallback
 no huntstop
 alias 1 8005550100 to 5001
 alias 2 8005550100 to 5002
 alias 3 8005550100 to 5003
 alias 4 8005550100 to 5004
 pickup 8005550100
```

When a DID
                              		  incoming call to 800 555-0100 is received, the alias command routes the call at random to one of
                              		  the four extensions (5001 to 5004). Because the pickup command is configured, if the DID call rings on extension 5002, the call can be
                              		  answered from any of the other extensions (5001, 5003, 5004) by pressing the
                              		  PickUp soft key.

The pickup command works by finding a match based on the incoming DID called number. In
                              		  this example, a call from extension 5004 to extension 5001 (internal call) does
                              		  not activate the pickup command because the called number (5001) does not match the configured pickup
                              		  number (800 555-0100). Thus, the pickup command distinguishes between internal and
                              		  external calls if multiple calls are ringing simultaneously.

### Related Commands

Command

Description

alias (call-manager- fallback)

Provides a mechanism for rerouting calls to telephone numbers that are
                                          						unavailable during Cisco Unified Communications Manager fallback.

call-manager-fallback

Enables Cisco Unified SRST support and enters call-manager-fallback
                                          						configuration mode.

## preference (voice register pool)

To set the preference order for creating the VoIP dial peers created
                              		  for a number associated with a voice pool, use the preference command in voice register pool
                              		  configuration mode. To put the number in default preference order, use the no form of this command.

preference preference-order

no preference

### Syntax Description

preference-order

Preference order for the extension or telephone number
                                          						associated with a pool. Range is 0 to 10. Default is 0, which is the highest
                                          						preference.

### Command Default

0 (highest preference order)

### Command Modes

Voice register pool configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SIP SRST 3.0

This command was introduced.

12.3(4)T

Cisco SIP SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was added to Cisco Communications Manager
                                          						Express (Cisco CME).

### Usage Guidelines

When you create a voice register pool for a SIP phone or a group of
                              		  SIP phones in a Cisco Unified CME or Cisco Unified Session Initiation Protocol
                              		  (SIP) Survivable Remote Site Telephony (SRST) environemnt, you automatically
                              		  create a virtual voice port and one to four virtual dial peers to be used by
                              		  the number associated with that pool. The preference value is passed
                              		  transparently to dial peers created for the number. The preference value allows
                              		  you to control the selection of a desired dial peer when multiple dial peers
                              		  are matched on the same destination pattern (extension or phone number)
                              		  associated with the pool. In this way, the preference command can be used to establish a
                              		  hunt strategy for incoming calls.

## Examples

The following example shows how to set a preference of 2 for
                              		  extension number 3000:

```
voice register pool 1
 number 3000
 preference 2
```

In the following example, extension number 1222 under voice register
                              		  dn 4 has a higher preference than number 1222 under voice register pool 5.

```
voice register pool 4
 number 1222
 preference 0
!
!
voice register dn 5
 number 1222
 preference 1
```

### Related Commands

Command

Description

id (voice register pool)

Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## proxy (voice register pool)

To autogenerate additional VoIP dial peers to reach the main proxy
                              		  whenever a Cisco Session Initiation Protocol (SIP) IP phone registers with a
                              		  SIP Survivable Remote Site Telephony (SRST) gateway, use the proxy command in voice register pool
                              		  configuration mode. To disable a dial peer as a SIP proxy, use the no form of this command.

proxy ip-address [ preference value ] [ monitor probe { icmp-ping | rtr } [alternate-ip-address] ]

no proxy

### Syntax Description

ip-address

IP address of the SIP proxy.

preference value

(Optional) Defines the preference of the proxy dial peers
                                          						that are created. Range is from 0 to 10. The highest preference is 0. There is
                                          						no default.

monitor probe

(Optional) Enables monitoring of proxy dial peers.

- icmp-ping —Enables
                                             						  monitoring of proxy dial peers using ICMP ping.

- rtr —Enables
                                             						  monitoring of proxy dial peers using RTR probes.

- alternate-ip-address —(Optional)
                                             						  Enables monitoring of alternate IP addresses other than the proxy address. For
                                             						  example, to monitor a gateway front end to a SIP proxy.

### Command Default

Proxy dial peer is disabled.

### Command Modes

Voice register pool configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SIP SRST 3.0

This command was introduced.

12.3(4)T

Cisco SIP SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

The proxy command autogenerates additional VoIP
                              		  dial peers to reach the main proxy whenever a Cisco SIP IP phone registers with
                              		  a Cisco Unified SIP SRST gateway. This autogeneration process enables all PSTN
                              		  calls to be routed first to the main proxy before the backup dial peers for
                              		  local Cisco SIP IP phones are tried.

Proxy dial peers can be monitored using ICMP ping or RTR probes, in
                              		  case of WAN failure. If the Cisco Unified SIP SRST gateway loses probes to the
                              		  main proxy, the proxy dial peers are temporarily set to an operational down
                              		  state. Then the backup dial peers can be selected faster to lower the call
                              		  setup time. In addition, the proxy dial peers can be monitored using an
                              		  alternate location other than the main proxy to monitor the status of the WAN
                              		  link.

Only one proxy address can be set per voice register pool.

For proxy monitoring to work, the call fallback active command must be configured.

## Examples

The following partial sample output from the show running-config command shows that voice register pool 1 has defined
                              		  10.2.161.187 as the SIP proxy and that it is monitored by ICMP ping:

```
voice register pool 1
 id mac 0030.94C2.A22A
 preference 5
 cor incoming call91 1 91011
 translate-outgoing called 1
 proxy 10.2.161.187 preference 1 monitor probe icmp-ping
 alias 1 94... to 91011 preference 8
 voice-class codec 1
```

### Related Commands

Command

Description

call fallback active

Enables a call request to fall back to alternate dial peers
                                          						in case of network congestion.

id (voice register pool)

Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone or set of Cisco SIP IP phones.

voice register pool

Enables SIP SRST voice register pool configuration
                                          						commands.

## registrar server (SIP)

To enable SIP registrar functionality, use the registrar server command in SIP configuration mode. To
                              		  disable SIP registrar functionality, use the no form of the command.

registrar server [ expires [ max sec ] [ min sec ]]

no registrar server

### Syntax Description

expires

(Optional) Sets the active time for an incoming
                                          						registration.

max sec

(Optional) Maximum expires time for a registration, in
                                          						seconds. The range is from 600 to 86400. The default is 3600.

min sec

(Optional) Minimum expires time for a registration, in
                                          						seconds. The range is from 60 to 3600. The default is 60.

### Command Default

Disabled

### Command Modes

SIP configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SIP SRST 3.0

This command was introduced.

12.3(4)T

Cisco SIP SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.4(4)T

Cisco CME 3.4 and Cisco SIP SRST 3.4

This command was added to Cisco CME.

### Usage Guidelines

When this command is entered, the router accepts incoming SIP
                              		  Register messages. If SIP Register message requests are for a shorter
                              		  expiration time than what is set with this command, the SIP Register message
                              		  expiration time is used.

This command is mandatory for Cisco Unified SIP SRST or Cisco Unified
                              		  CME and must be entered before any voice register pool or voice register global commands are configured.

If the WAN is down and you reboot your Cisco Unified CME or Cisco
                              		  Unified SIP SRST router, when the router reloads it will have no database of
                              		  SIP phone registrations. The SIP phones will have to register again, which
                              		  could take several minutes, because SIP phones do not use a keepalive
                              		  functionality. To shorten the time before the phones re-register, the
                              		  registration expiry can be adjusted with this command. The default expiry is
                              		  3600 seconds; an expiry of 600 seconds is recommended.

## Examples

The following partial sample output from the show running-config command shows that SIP registrar
                              		  functionality is set:

voice service voip

allow-connections sip-to-sip

sip

registrar server expires max 1200 min 300

### Related Commands

Command

Description

sip

Enters SIP configuration mode from voice service VoIP
                                          						configuration mode.

voice register global

Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified CME
                                          						or Cisco Unified SIP SRST environment.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## reset (call-manager-fallback)

To reset Cisco IP phones, use the reset command in call-manager-fallback
                              		  configuration mode.

reset { all seconds | mac-address mac-address }

### Syntax Description

all

All Cisco IP phones.

seconds

Time interval, in seconds, that passes between each Cisco
                                          						IP phone resetting. The range is from 0 to 60.

mac-address mac-address

MAC address of a particular Cisco IP phone.

### Command Default

No default behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco SRST 1.0

This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers; Cisco IAD2420
                                          						series IADs.

12.2(2)XT

Cisco SRST 2.0

This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

### Usage Guidelines

This command does not have a no form.

## Examples

The following example resets all Cisco IP phones in 8-second
                              		  intervals:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# reset all 8
```

The following example resets the Cisco IP phone with MAC address
                              		  CFBA.321B.96FA:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# reset mac-address CFBA.321B.96FA
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode.

## secondary-dialtone (call-manager-fallback)

To enable a secondary dial tone when a Cisco Unified IP phone user
                              		  dials a defined PSTN access prefix, use the secondary-dialtone command in call-manager-fallback configuration mode. To disable
                              		  the secondary dial tone, use the no form of this command.

secondary-dialtone digit-string

no secondary-dialtone digit-string

### Syntax Description

digit-string

The number of the access prefix.

### Command Default

Secondary dial tone is disabled.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Unified Product

Modification

12.2(15)ZJ

Cisco Unified SRST 3.0

This command was introduced.

12.3(4)T

Cisco Unified SRST 3.0

This command was integrated into Cisco Unified IOS Release
                                          						12.3(4)T.

### Usage Guidelines

The secondary dial tone is turned off when the next number after the digit-string is pressed. For example, if 8
                              		  were the digit-string and a person were dialing 8
                              		  555-0100, the secondary dial tone would be turned off when the number 5 is
                              		  pressed.

The tone value for the secondary dial is the skinny
                              		  DtOutsideDialtone.

## Examples

The following enables a secondary dial tone when a Cisco Unified IP
                              		  phone users enters the number nine to get an outside line:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# secondary-dialtone 9
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified Unified SRST support and enters
                                          						call-manager-fallback configuration mode.

## security

To define whether a phone type supports security features, use the security command in ephone-type configuration
                              		  mode. To disable security support, use the no form of this command.

security

no security

### Syntax Description

This command has no arguments or keywords.

### Command Default

Enabled (phone type supports security features).

### Command Modes

Ephone-type configuration (config-ephone-type)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XZ

Cisco Unified CME 4.3 Cisco Unified SRST 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command specifies whether security features are supported by the
                              		  type of phone being added with a phone-type template.

## Examples

The following example shows that support for security is disabled for
                              		  the Nokia E61 when creating the ephone-type template:

```
Router(config)# ephone-type E61 Router(config-ephone-type)# no security
```

### Related Commands

Command

Description

device-id

Specifies the device ID for a phone type.

type

Assigns a phone type to an SCCP phone.

## security-policy (voice register global)

To define the security level of SIP phones allowed to register, use
                              		  the security-policy command in voice register global configuration mode. To
                              		  return to the default, use the no form of this command.

### Cisco IOS Release 15.0(1)XA and later releases

security-policy secure

no security-policy secure

### Syntax Description

secure

Requires SIP phones to use TLS for signaling transport.
                                          						Non-secure SIP phones are blocked from registering. Valid for Cisco Unified
                                          						SRST.

### Command Default

All levels of phone security are permitted to register, also known as
                              		  device-default mode.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified SRST 8.0

This command was introduced.

Cisco IOS XE Dublin
                                                17.10.1a

Unified Cisco SRST 14.3

Introduced support for YANG models.

### Usage Guidelines

The secure keyword configures the SIP registration security policy so
                              		  that only encrypted phones may register to the Cisco Unified SRST device in the
                              		  event of a failover from the primary call control. When this keyword is
                              		  configured, non-secure phones using TCP or UDP for signaling transport, as well
                              		  as authenticated phones using TLS/TCP for signaling transport, will be blocked
                              		  from registering.

## Examples

The following example shows that only registration requests from
                              		  encrypted SIP phones in a Cisco Unified SRST system are permitted:

```
Router(config)# voice register global Router(config-register-global)# security-policy secure
```

### Related Commands

Command

Description

crypto signaling

Identifies the trustpoint and encryption restrictions used
                                          						during the TLS handshake.

## show
                        	 call-manager-fallback all

To display the
                              		  detailed configuration of all Cisco IP phones, directory numbers, voice ports,
                              		  and dial peers in your network during Cisco Unified CallManager fallback, use
                              		  the show call-manager-fallback all command in privileged EXEC mode.

show call-manager-fallback all

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						SRST 1.0

This
                                          						command was introduced on the following platforms: Cisco 2600 series and Cisco
                                          						3600 series multiservice routers; Cisco IAD2420 series IADs.

12.2(2)XT

Cisco
                                          						SRST 2.0

This
                                          						command was implemented on Cisco 1750 and Cisco 1751 multiservice routers.

12.2(8)T

Cisco
                                          						SRST 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco
                                          						SRST 2.0

This
                                          						command was implemented on the Cisco 2600-XM and Cisco 2691 routers.

12.2(11)T

Cisco
                                          						SRST 2.01

This
                                          						command was integrated into Cisco IOS Release 12.2(11)T and implemented on the
                                          						Cisco 1760 routers.

12.3(4)T

Cisco
                                          						SRST 3.0

The
                                          						Version was added to output.

## Examples

The following is
                              		  sample output from the show call-manager-fallback all command:

```
Router # show call-manager-fallback CONFIG (Version=4.1(0))
=====================
Version 4.1(0)
For on-line documentation please see:
www.cisco.com/univercd/cc/td/doc/product/access/ip_ph/ip_ks/index.htm 
ip source-address 0.0.0.0 port 2000
max-ephones 0
max-dn 0
max-conferences 8 gain -6
dspfarm units 0
dspfarm transcode sessions 0
huntstop
cnf-file location: system:
cnf-file option: PER-PHONE-TYPE
network-locale[0] US (This is the default network locale for this box)
network-locale[1] US
network-locale[2] US
network-locale[3] US
network-locale[4] US
user-locale[0] US (This is the default user locale for this box)
user-locale[1] US 
user-locale[2] US 
user-locale[3] US 
user-locale[4] US 
srst mode auto-provision is OFF
srst ephone template is 0
srst dn template is 0
srst dn line mode is single
time-format 12
date-format mm-dd-yy
timezone 0 Greenwich Standard Time
no transfer-pattern is configured, transfer is restricted to local SCCP phones only.
keepalive 30 auxiliary 30
timeout interdigit 10
timeout busy 10
timeout ringing 180
timeout ringin-callerid 8
caller-id name-only: enable
Limit number of DNs per phone:
7910: 36
7935: 36
7936: 36
7940: 36
7960: 36
7970: 36
Log (table parameters):
max-size: 150
retain-timer: 15
transfer-system full-consult 
local directory service: enabled.
Extension-assigner tag-type ephone-tag.
========================================
```

Table 1 describes the significant fields shown in the display.

Field

Description

destination-pattern

Destination pattern (telephone number) configured for this dial peer.

dial-peer
                                          					 voice

Voice
                                          					 dial peer.

ephone-dn

Cisco IP
                                          					 phone directory number.

(no)
                                          					 huntstop

Whether
                                          					 or not huntstop is set.

ip
                                          					 source-address

IP
                                          					 address used by the Cisco IP phones to register with the router for service.

keepalive

Cisco
                                          					 IP phone keepalive period in seconds.

max-dn

Maximum
                                          					 directory numbers or virtual voice ports.

max-ephones

Maximum
                                          					 number of Cisco IP phones.

port

TCP
                                          					 port number used by the Cisco IP phones to communicate with the router.

station-id number

Number
                                          					 used for caller-ID purposes when calls are made using the line.

voice-port

(Virtual) voice port designator.

Version

SRST
                                          					 version number designation.

### Related Commands

Command

Description

show call-manager- fallback dial-peer

Displays detailed configuration output for the dial peers in your network
                                          						during Cisco Unified CallManager fallback.

show call-manager- fallback ephone-dn

Displays output for the Cisco IP phone directory numbers or virtual voice ports
                                          						during Cisco Unified CallManager fallback.

show call-manager- fallback voice-port

Displays output for the voice ports while Cisco Unified CallManager is active.

## show
                        	 call-manager-fallback dial-peer

To display
                              		  detailed configuration output for the dial peers in your network during Cisco
                              		  Unified Communications Manager fallback, use the show call-manager-fallback dial-peer command in privileged EXEC mode.

show call-manager-fallback dial-peer

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						SRST 1.0

This
                                          						command was introduced on the following platforms: Cisco 2600 series and Cisco
                                          						3600 series multiservice routers; Cisco IAD2420 series IADs.

12.2(2)XT

Cisco
                                          						SRST 2.0

This
                                          						command was implemented on Cisco 1750 and Cisco 1751 multiservice routers.

12.2(8)T

Cisco
                                          						SRST 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco
                                          						SRST 2.0

This
                                          						command was implemented on the Cisco 2600-XM and Cisco 2691 routers.

12.2(11)T

Cisco
                                          						SRST 2.01

This
                                          						command was integrated into Cisco IOS Release 12.2(11)T and implemented on the
                                          						Cisco 1760 routers.

## Examples

The following is
                              		  sample output from the show call-manager-fallback dial-peer command:

```
Router# show call-manager-fallback dial-peer dial-peer voice 20046 pots
 destination-pattern 4444
 call-forward busy 5001
 call-forward noan 5001
 port 50/0/1
dial-peer voice 20047 pots
 destination-pattern 3333
 call-forward busy 5001
 call-forward noan 5001
 port 50/0/2
dial-peer voice 20048 pots
 destination-pattern 5555
 call-forward busy 5001
 call-forward noan 5001
 port 50/0/3
dial-peer voice 20049 pots
 preference 9
 destination-pattern 3...
 call-forward busy 5001
 call-forward noan 5001
 port 50/0/3
```

Table 1 describes
                              		  the significant fields shown in the display.

Field

Description

call-forward busy

Indicates
                                          					 call forwarding when a Cisco IP phone is busy.

call-forward noan

Indicates
                                          					 call forwarding when no answer is received from a Cisco IP phone.

destination-pattern

Destination pattern (telephone number) configured for this dial peer.

dial-peer
                                          					 voice

Voice
                                          					 dial peer.

port

(Virtual)
                                          					 voice port designator.

### Related Commands

Command

Description

show call-manager- fallback all

Displays the detailed configuration of all Cisco IP phones, directory numbers,
                                          						voice ports, and dial peers in your network during Cisco Unified Communications
                                          						Manager fallback.

show call-manager- fallback ephone-dn

Displays output for the Cisco IP phone directory numbers or virtual voice ports
                                          						during Cisco Unified Communications Manager fallback.

show call-manager- fallback voice-port

Displays output for the voice ports while Cisco Unified Communications Manager
                                          						is active.

## show
                        	 call-manager-fallback ephone-dn

To display
                              		  detailed configuration output for the Cisco IP phone directory numbers or
                              		  virtual voice ports during Cisco Unified CallManager fallback, use the show call-manager-fallback ephone-dn command in privileged EXEC mode.

show call-manager-fallback ephone-dn

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						SRST 1.0

This
                                          						command was introduced on the following platforms: Cisco 2600 series and Cisco
                                          						3600 series multiservice routers; Cisco IAD2420 series IADs.

12.2(2)XT

Cisco
                                          						SRST 2.0

This
                                          						command was implemented on Cisco 1750 and Cisco 1751 multiservice routers.

12.2(8)T

Cisco
                                          						SRST 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco
                                          						SRST 2.0

This
                                          						command was implemented on the Cisco 2600-XM and Cisco 2691 routers.

12.2(11)T

Cisco
                                          						SRST 2.01

This
                                          						command was integrated into Cisco IOS Release 12.2(11)T and implemented on the
                                          						Cisco 1760 routers.

12.3(4)T

Cisco
                                          						SRST 3.0

The
                                          						Version, ephone-dn,vand voice-port was added to output.

## Examples

The following is
                              		  sample output from the show call-manager-fallback ephone-dn command:

```
Router# Router # show call-manager-fallback CONFIG (Version=4.1(0))
=====================
Version 4.1(0)
For on-line documentation please see:
www.cisco.com/univercd/cc/td/doc/product/access/ip_ph/ip_ks/index.htm 
ip source-address 0.0.0.0 port 2000
max-ephones 0
max-dn 0
max-conferences 8 gain -6
dspfarm units 0
dspfarm transcode sessions 0
huntstop
cnf-file location: system:
cnf-file option: PER-PHONE-TYPE
network-locale[0] US (This is the default network locale for this box)
network-locale[1] US
network-locale[2] US
network-locale[3] US
network-locale[4] US
user-locale[0] US (This is the default user locale for this box)
user-locale[1] US 
user-locale[2] US 
user-locale[3] US 
user-locale[4] US 
srst mode auto-provision is OFF
srst ephone template is 0
srst dn template is 0
srst dn line mode is single
time-format 12
date-format mm-dd-yy
timezone 0 Greenwich Standard Time
no transfer-pattern is configured, transfer is restricted to local SCCP phones only.
keepalive 30 auxiliary 30
timeout interdigit 10
timeout busy 10
timeout ringing 180
timeout ringin-callerid 8
caller-id name-only: enable
Limit number of DNs per phone:
7910: 36
7935: 36
7936: 36
7940: 36
7960: 36
7970: 36
Log (table parameters):
max-size: 150
retain-timer: 15
transfer-system full-consult 
local directory service: enabled.
Extension-assigner tag-type ephone-tag.
========================================
```

Table 1 describes the significant fields shown in the display.

Field

Description

ephone-dn

Cisco IP
                                          					 phone directory number.

(no)
                                          					 huntstop

Whether
                                          					 or not huntstop is set.

number

Cisco IP
                                          					 phone number.

translate
                                          					 called

The
                                          					 configured translation rule. Can be called or calling, plus the tag number by
                                          					 which the rule set is referenced.

### Related Commands

Command

Description

show call-manager- fallback all

Displays the detailed configuration of all Cisco IP phones, directory numbers,
                                          						voice ports, and dial peers in your network during Cisco Unified CallManager
                                          						fallback.

show call-manager- fallback dial-peer

Displays detailed configuration output for the dial peers in your network
                                          						during Cisco Unified CallManager fallback.

show call-manager- fallback voice-port

Displays output for the voice ports while Cisco Unified CallManager is active.

## show
                        	 call-manager-fallback voice-port

To display
                              		  detailed configuration output for the voice ports while Cisco Unified
                              		  Communications Manager is active, use the show call-manager-fallback voice-port command in privileged EXEC mode.

show call-manager-fallback voice-port

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						SRST 1.0

This
                                          						command was introduced on the following platforms: Cisco 2600 series and Cisco
                                          						3600 series multiservice routers, and Cisco IAD2420 series IADs.

12.2(2)XT

Cisco
                                          						SRST 2.0

This
                                          						command was implemented on Cisco 1750 and Cisco 1751 multiservice routers.

12.2(8)T

Cisco
                                          						SRST 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco
                                          						SRST 2.0

This
                                          						command was implemented on the Cisco 2600-XM and Cisco 2691 routers.

12.2(11)T

Cisco
                                          						SRST 2.01

This
                                          						command was integrated into Cisco IOS Release 12.2(11)T and implemented on the
                                          						Cisco 1760 routers.

## Examples

The following is
                              		  sample output from the show call-manager-fallback voice-port command:

```
Router# show call-manager-fallback voice-port voice-port 50/0/1
 station-id number 4444
 timeout ringing 8
 translate called 1
!
voice-port 50/0/2
 station-id number 3333
 timeout ringing 8
 translate called 1
!
voice-port 50/0/3
 station-id number 5555
 timeout ringing 8
 translate called 1
!
voice-port 50/0/4
 timeout ringing 8
 translate called 1
!
```

Table 1 describes
                              		  the significant fields shown in the display.

Field

Description

voice-port

(Virtual)
                                          					 voice port.

station-id number

The phone
                                          					 number used for caller-ID purposes for calls made from this voice port.

### Related Commands

Command

Description

show call-manager- fallback all

Displays the detailed configuration of all Cisco IP phones, directory numbers,
                                          						voice ports, and dial peers in your network during Cisco Unified Communications
                                          						Manager fallback.

show call-manager- fallback dial-peer

Displays detailed configuration output for the dial peers in your network
                                          						during Cisco Unified Communications Manager fallback.

show call-manager- fallback ephone-dn

Displays output for the Cisco IP phone directory numbers or virtual voice ports
                                          						during Cisco Unified Communications Manager fallback.

## show
                        	 credentials

To display the
                              		  credentials settings that have been configured for use during Cisco Unified CME
                              		  phone authentication communications or secure Cisco Unified SRST fallback, use
                              		  the show credentials command in privileged EXEC mode.

show credentials

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.3(14)T

Cisco
                                          						SRST 3.3

This
                                          						command was introduced for Cisco Unified SRST.

12.4(4)XC

Cisco
                                          						Unified CME 4.0

This
                                          						command was introduced for Cisco Unified CME.

### Usage Guidelines

Cisco Unified CME

This command
                              		  displays the credentials settings on a Cisco Unified CME router that has been
                              		  configured with a CTL provider to be used with Cisco Unified CME phone
                              		  authentication.

Cisco Unified SRST

This command
                              		  displays the credentials settings on the Cisco Unified SRST router that are
                              		  supplied to Cisco Unified Communications Manager for use during secure SRST
                              		  fallback.

## Examples

The following is
                              		  sample output from the show credentials command:

```
Router# show credentials Credentials IP: 10.1.1.22
Credentials PORT: 2445
Trustpoint: srstca
```

Table 1 describes the fields in the sample output.

Field

Description

Credentials IP

Cisco
                                          					 Unified CME—IP address where the CTL provider is configured.

Cisco
                                          					 Unified SRST—The specified IP address where certificates from Cisco Unified
                                          					 Communications Manager to the SRST router are received.

Credentials PORT

Cisco
                                          					 Unified CME—TCP port for credentials service communication. Default is 2444.

Cisco
                                          					 Unified SRST—The port to which the SRST router connects to receive messages
                                          					 from the Cisco Unified IP phones. The port number is from 2000 to 9999. The
                                          					 default port number is 2445.

Trustpoint

Cisco
                                          					 Unified CME—CTL provider trustpoint label that will be used for TLS sessions
                                          					 with the CTL client.

Cisco
                                          					 Unified SRST—The name of the trustpoint that is associated with the credentials
                                          					 service between the Cisco Unified Communications Manager client and the SRST
                                          					 router.

### Related Commands

Command

Description

credentials

Enters
                                          						credentials configuration mode to configure a Cisco Unified CME CTL provider
                                          						certificate or a Cisco Unified SRST router certificate.

ctl-service admin

Specifies a user name and password to authenticate the CTL client during the
                                          						CTL protocol.

debug credentials

Sets
                                          						debugging on the credentials service that runs between a Cisco Unified CME CTL
                                          						provider and the CTL client or between a Cisco Unified SRST router and Cisco
                                          						Unified Communications Manager.

ip source-address (credentials)

Enables the Cisco Unified CME or SRST router to receive messages through the
                                          						specified IP address and port.

trustpoint (credentials)

Specifies the name of the trustpoint to be associated with a Cisco Unified CME
                                          						CTL provider certificate or with a Cisco Unified SRST router certificate.

## show
                        	 ephone

To display
                              		  information about registered Cisco Unified IP phones, use the show ephone command in privileged EXEC mode.

show ephone [ mac-address | phone-type ]

### Syntax Description

mac-address

(Optional) Displays information for the phone with the specified MAC address.

phone-type

(Optional) Displays information for phones of the specified phone type. Valid
                                          						types are as follows:

- 7902 —Cisco Unified IP Phone 7902G.

- 7905 —Cisco Unified IP Phone 7905G.

- 7906 —Cisco Unified IP Phone 7905G.

- 7910 —Cisco Unified IP Phone 7910 and 7910G.

- 7911 —Cisco Unified IP Phone 7911G.

- 7912 — Cisco Unified IP Phone 7912G.

- 7914 — Cisco Unified IP Phone 7914 Expansion Module.

- 7920 — Cisco Unified Wireless IP Phone 7920.

- 7921 —Cisco Unified Wireless IP Phone 7921.

- 7931 — Cisco Unified Wireless IP Phone 7931G.

- 7935 — Cisco Unified IP Conference Station 7935.

- 7936 — Cisco Unified IP Conference Station 7936.

- 7940— Cisco Unified IP Phones 7940 and 7940G.

- 7941 —Cisco Unified IP Phone 7941G.

- 7941GE —Cisco Unified IP Phone 7941G-GE.

- 7942 —Cisco Unified IP Phone 7942.

- 7945 —Cisco Unified IP Phone 7945.

- 7960 — Cisco Unified IP Phones 7960 and 7960G .

- 7961 —Cisco Unified IP Phone 7961G.

- 7961GE —Cisco Unified IP Phone 7961G-GE.

- 7962 —Cisco Unified IP Phone 7962.

- 7965 —Cisco Unified IP Phone 7965.

- 7970 —Cisco Unified IP Phone 7970G.

- 7971 —Cisco Unified IP Phone 7971G-GE.

- 7975 —Cisco Unified IP Phone 7975

- 7985 —Cisco Unified IP Phone 7985.

- ata — Cisco ATA-186 or Cisco ATA-188.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						ITS 1.0 Cisco SRST 1.0

This
                                          						command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						IAD2420 series.

12.2(2)XT

Cisco
                                          						ITS 2.0 Cisco SRST 2.0

This
                                          						command was implemented on the Cisco 1750 and Cisco 1751.

12.2(8)T

Cisco
                                          						ITS 2.0 Cisco SRST 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725 and Cisco 3745.

12.2(8)T1

Cisco
                                          						ITS 2.0 Cisco SRST 2.0

This
                                          						command was implemented on the Cisco 2600XM and Cisco 2691.

12.2(11)T

Cisco
                                          						ITS 2.01 Cisco SRST 2.01

The ata keyword
                                          						was added and this command was implemented on the Cisco 1760.

12.2(11)YT

Cisco
                                          						ITS 2.1 Cisco SRST 2.1

The 7914 keyword was added.

12.2(15)ZJ

Cisco
                                          						CME 3.0 Cisco SRST 3.0

The 7902 , 7905 , and 7912 keywords were added.

12.3(7)T

Cisco
                                          						CME 3.1 Cisco SRST 3.1

The 7920 and 7936 keywords were added.

12.3(11)XL

Cisco
                                          						CME 3.2.1 Cisco SRST 3.2.1

The 7970 keyword was added.

12.3(14)T

Cisco
                                          						CME 3.3 Cisco SRST 3.3

The 7971 keyword was added, and this command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.4(4)XC

Cisco
                                          						Unified CME 4.0 Cisco Unified SRST 4.0

The 7911 , 7941 , 7941GE , 7961 , and 7961GE keywords were added.

12.4(9)T

Cisco
                                          						Unified CME 4.0 Cisco Unified SRST 4.0

The 7911 , 7941 , 7941GE , 7961 , and 7961GE keywords were integrated into Cisco IOS Release 12.4(9)T.

12.4(6)XE

Cisco
                                          						Unified CME 4.0(2)

The 7931 keyword was added for Cisco Unified CME.

12.4(4)XC4

Cisco
                                          						Unified CME 4.0(3)

The 7931 keyword was added for Cisco Unified CME.

12.4(11)T

Cisco
                                          						Unified CME 4.0(3)

The 7931 keyword for Cisco Unified CME was integrated in Cisco IOS Release 12.4(11)T.

12.4(11)XJ2

Cisco
                                          						Unified CME 4.1 Cisco Unified SRST 4.1

The 7921 and 7985 keywords were introduced.

12.4(15)T1

Cisco
                                          						Unified CME 4.1(1) Cisco Unified SRST 4.1(1)

The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced.

12.4(11)XW3

Cisco
                                          						Unified CME 4.2 Cisco Unified SRST 4.2

The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced.

12.4(15)XY

Cisco
                                          						Unified CME 4.2(1) Cisco Unified SRST 4.2(1)

Emergency response location (ERL) information displays in the output.

12.4(20)T

Cisco
                                          						Unified CME 7.0 Cisco Unified SRST 7.0

This
                                          						command was integrated into Cisco IOS Release 12.4(20)T.

## Examples

Significant
                              		  fields in the output from this command are described in Table 1 .

The following
                              		  sample output shows general information for registered phones:

```
Router# show ephone ephone-1 Mac:0003.E3E7.F627 TCP socket:[2] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:10.0.0.2 51671 Telecaster 7940 keepalive 28 max_line 2
button 1: dn 1 number 4444 
ephone-2 Mac:0030.94C3.F43A TCP socket:[1] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:10.0.0.3 50094 Telecaster 7960 keepalive 28 max_line 6
button 1: dn 3 number 5555 
ephone-3 Mac:0003.6B40.99DA TCP socket:[3] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:10.2.168.200 51879 Telecaster 7960 keepalive 28 max_line 6
button 1: dn 2 number 3333
```

The following
                              		  sample output shows general information for the phone with the MAC address
                              		  0003.E3E7.F627:

```
Router# show ephone 0003.E3E7.F627 ephone-1 Mac:0003.E3E7.F627 TCP socket:[2] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:10.0.0.2 51671 Telecaster 7940 keepalive 28 max_line 2
button 1: dn 1 number 4444 
Active Call on DN 1:3001 10.0.0.51 31808 to 10.2.159.100 22708
Tx Pkts 452 bytes 41584 Rx Pkts 452 bytes 41584 Lost 0
Jitter 0 Latency 0
```

The following
                              		  sample output shows information for a phone that has two Cisco Unified IP Phone
                              		  7914 Expansion Modules attached. The output shows this module as a subsidiary
                              		  type in addition to the main 7960 type
                              		  for the phone itself. Subtype 3 means that one Cisco Unified IP Phone 7914
                              		  Expansion Module is attached to the main Cisco Unified IP Phone 7960 or 7960G,
                              		  and subtype 4 means that two are attached.

```
Router# show ephone 7914 ephone-2 Mac:0007.0EA6.39F8 TCP socket:[2] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:10.2.205.206 49278 Telecaster 7960  sub=4 keepalive 2723 max_line 34
button 1: dn 21 number 60021 CH1 IDLE      
button 2: dn 22 number 60022 CH1 IDLE      
button 7: dn 11 number 60011 CH1 IDLE      monitor-ring 
button 8: dn 12 number 60012 CH1 IDLE      monitor-ring 
button 9: dn 13 number 60013 CH1 IDLE      monitor-ring 
button 10: dn 14 number 60014 CH1 IDLE      monitor-ring 
button 11: dn 15 number 60015 CH1 IDLE      monitor-ring 
button 12: dn 16 number 60016 CH1 IDLE      monitor-ring 
button 13: dn 17 number 60017 CH1 IDLE      monitor-ring 
button 14: dn 18 number 60018 CH1 IDLE      monitor-ring 
button 15: dn 19 number 60019 CH1 IDLE      monitor-ring 
button 16: dn 20 number 60020 CH1 IDLE      monitor-ring 
button 17: dn 39 number 60039 CH1 IDLE      CH2 IDLE      monitor-ring 
button 18: dn 40 number 60040 CH1 IDLE      CH2 IDLE      monitor-ring 
button 19: dn 23 number 60023 CH1 IDLE      monitor-ring 
button 20: dn 24 number 60024 CH1 IDLE      monitor-ring 
button 21: dn 25 number 60025 CH1 IDLE      monitor-ring 
button 22: dn 26 number 60026 CH1 IDLE      monitor-ring 
button 23: dn 27 number 60027 CH1 IDLE      monitor-ring 
button 24: dn 28 number 60028 CH1 IDLE      monitor-ring 
button 25: dn 29 number 60029 CH1 IDLE      monitor-ring 
button 26: dn 30 number 60030 CH1 IDLE      monitor-ring 
button 27: dn 31 number 60031 CH1 IDLE      CH2 IDLE      monitor-ring 
button 28: dn 32 number 60032 CH1 IDLE      CH2 IDLE      monitor-ring 
button 29: dn 33 number 60033 CH1 IDLE      CH2 IDLE      monitor-ring 
button 30: dn 34 number 60034 CH1 IDLE      CH2 IDLE      monitor-ring 
button 31: dn 35 number 60035 CH1 IDLE      CH2 IDLE      monitor-ring 
button 32: dn 36 number 60036 CH1 IDLE      CH2 IDLE      monitor-ring 
button 33: dn 37 number 60037 CH1 IDLE      CH2 IDLE      monitor-ring 
button 34: dn 38 number 60038 CH1 IDLE      CH2 IDLE      monitor-ring
```

The following
                              		  sample output shows a phone that has a paging-dn and has received a page:

```
Router# show ephone 7910 ephone-2 Mac:0087.0E76.B93C TCP socket:[4] activeLine:0 REGISTERED
mediaActive:1 offhook:0 ringing:0 reset:0 reset_sent:0 paging 1 debug:0
IP:10.50.50.20 49231 Telecaster 7910  keepalive 112 max_line 2 dual-line
button 1:dn 3  number 95021 CH1 IDLE
paging-dn 25
```

Table 1 describes significant fields in the output.

Field

Description

Active
                                          					 Call

An
                                          					 active call is in progress.

activeLine

Line
                                          					 (button) on the phone that is in use. Zero indicates that no line is in use.

auto-dial number

Intercom extension that automatically dials number .

button number : dn number

Phone
                                          					 button number and the extension (ephone-dn) dn-tag number associated with that
                                          					 button.

bytes

Total
                                          					 number of voice data bytes sent or received by the phone.

Called
                                          					 Dn, Calling Dn

Ephone-dn tag numbers of the called and calling ephone-dn. Set to -1 if the
                                          					 call is not to or from an ephone-dn, or if there is no active call.

cfa number

Call-forward-all to number is
                                          					 enabled for this extension.

CH1 CH2

Status
                                          					 of channel 1 and, if this is a dual-line ephone-dn, the status of channel 2.

debug

1
                                          					 indicates that debug for the phone is enabled. 0 indicates that debug is
                                          					 disabled.

DnD

Do Not
                                          					 Disturb is set on this phone.

DP tag

Not
                                          					 used.

ephone- number

Unique
                                          					 sequence number used to identify this phone during configuration (phone-tag).

IP

Assigned IP address of the Cisco Unified IP phone.

Jitter

Amount
                                          					 of variation (in milliseconds) of the time interval between voice packets
                                          					 received by the Cisco Unified IP phone.

keepalive

Number
                                          					 of keepalive messages received from the Cisco Unified IP phone by the router.

Latency

Estimated playout delay for voice packets received by the Cisco Unified IP
                                          					 phone.

line number

Button
                                          					 number on an IP phone. Line 1 is the button nearest the top of the phone.

Lost

Number
                                          					 of voice packets lost, as calculated by the Cisco Unified IP phone, on the
                                          					 basis of examining voice packet time-stamp and sequence numbers during playout.

Mac

MAC
                                          					 address.

Max
                                          					 Conferences

Maximum
                                          					 number of allowable conference calls and number of active conference calls.

max_line number

Maximum
                                          					 number of line buttons that can be configured on this phone.

mediaActive

1
                                          					 indicates that an active conversation is in progress. 0 indicates that no
                                          					 conversation is ongoing.

monitor-ring

This
                                          					 button is set up as a monitor button.

number

Telephone or extension number associated with the Cisco Unified IP phone button
                                          					 and its dn-tag.

offhook

1
                                          					 indicates that the phone is off-hook. 0 indicates that the phone is on-hook.

overlay

This
                                          					 button contains an overlay set. Use show ephone overlay to display the contents of overlay sets.

paging

1
                                          					 indicates that the phone has received an audio page. 0 indicates that the phone
                                          					 has not received an audio page.

paging-dn

Ephone-dn that is dedicated for receiving audio pages on this phone. The
                                          					 paging-dn number is the number of the paging set to which this phone belongs.

Password

Authentication string that the phone user types when logging in to the
                                          					 web-based Cisco Unified CME GUI.

Port

Port
                                          					 used for TAPI transmissions.

REGISTERED

The
                                          					 Cisco Unified IP phone is active and registered. Alternative states are
                                          					 UNREGISTERED (indicating that the connection to the Cisco Unified IP phone was
                                          					 closed in a normal manner) and DECEASED (indicating that the connection to the
                                          					 Cisco Unified IP phone was closed because of a keepalive timeout).

reset

Pending
                                          					 reset.

reset_sent

Request
                                          					 for reset has been sent to the Cisco Unified IP phone.

ringing

1
                                          					 indicates that the phone is ringing. 0 indicates that the phone is not ringing.

Rx Pkts

Number
                                          					 of received voice packets.

silent-ring

Silent
                                          					 ring has been set on this button and extension.

socket

TCP
                                          					 socket number used to connect to IP phone.

speed
                                          					 dial speed-tag:digit-string label-text

This
                                          					 button is a speed-dial button, assigned to the speed-dial sequence number speed-tag .
                                          					 It dials digit-string and displays the text label-text next to the button.

sub=3,
                                          					 sub=4

Subtype
                                          					 3 means that one Cisco Unified IP Phone 7914 Expansion Module is attached to
                                          					 the main Cisco Unified IP Phones 7960 and 7960G, and subtype 4 means that two
                                          					 are attached.

Tag number

Dn-tag
                                          					 number, the unique sequence number that identifies an ephone-dn during
                                          					 configuration, followed by the type of ephone-dn it is.

TAPI
                                          					 Client IP Address

IP
                                          					 address of the PC running the TAPI client.

TCP
                                          					 socket

TCP
                                          					 socket number used to communicate with the Cisco Unified IP phone. This can be
                                          					 correlated with the output of other debug and show commands.

Telecaster model-number

Type
                                          					 and model of the Cisco Unified IP phone. This information is received from the
                                          					 phone during its registration with the router.

Tx Pkts

Number
                                          					 of transmitted voice packets.

Username

Username that the phone user types when logging in to the web-based Cisco
                                          					 Unified CME GUI.

### Related Commands

Command

Description

show ephone-dn

Displays information about Cisco Unified IP phone extensions (ephone-dns).

show ephone login

Displays the login states of all local ephones.

show telephony-service all

Displays systemwide status and information for a Cisco Unified CME system.

## show ephone cfa

To display status and information on the registered phones that have
                              		  call-forward-all set on one or more of their extensions (ephone-dns), use the show ephone cfa command in privileged EXEC mode.

show ephone cfa

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

## Examples

The following is sample output from the show ephone cfa command:

```
Router# show ephone cfa ephone-1 Mac:0007.0EA6.353A TCP socket:[2] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:1.2.205.205 52491 Telecaster 7960  keepalive 14 max_line 6
button 1: dn 11 number 60011 cfa 60022 CH1 IDLE 
button 2: dn 17 number 60017 cfa 60021 CH1 IDLE
```

The show ephone command describes significant fields in
                              		  this output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone dn

To display phone information for specified dn-tag or for all dn-tags,
                              		  use the show ephone dn command in privileged EXEC mode.

show ephone dn [dn-tag]

### Syntax Description

dn-tag

(Optional) Unique sequence number that is used during
                                          						configuration to identify a particular extension (ephone-dn).

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

Use this command to identify the phone on which a particular dn-tag
                              		  has been assigned.

## Examples

The following is sample output for the two appearances of DN 5:

```
Router# show ephone dn 5 Tag 5, Normal or Intercom dn 
ephone 1, mac-address 0030.94C3.CAA2, line 2
ephone 2, mac-address 0030.94c2.9919, line 3
```

The show ephone command describes significant fields in
                              		  this output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone dnd

To display information on the registered phones that have “do not
                              		  disturb” set on one or more of their extensions (ephone-dns), use the show ephone dnd command in privileged EXEC mode.

show ephone dnd

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

This command does not apply to Cisco Unified SRST.

## Examples

The following is sample output from the show ephone dnd command:

```
Router# show ephone dnd ephone-1 Mac:0007.0EA6.353A TCP socket:[1] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:1.2.205.205 52486 Telecaster 7960  keepalive 2729 max_line 6 DnD
button 1: dn 11 number 60011 CH1 IDLE
```

The show ephone command describes significant fields in
                              		  this output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone
                        	 login

To display the
                              		  login states of all local IP phones, use the show ephone login command in privileged EXEC mode.

show ephone login

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

### Usage Guidelines

The show ephone login command displays whether an ephone has a
                              		  personal identification number (PIN) and whether its owner has logged in.

## Examples

The following is
                              		  sample output from the show ephone login command. It shows that a PIN is enabled for
                              		  ephone 1 and that its owner has not logged in. The other phones do not have
                              		  PINs associated with them.

```
Router# show ephone login ephone 1        Pin enabled:TRUE        Logged-in:FALSE
ephone 2        Pin enabled:FALSE
ephone 3        Pin enabled:FALSE
ephone 4        Pin enabled:FALSE
ephone 5        Pin enabled:FALSE
ephone 6        Pin enabled:FALSE
ephone 7        Pin enabled:FALSE
ephone 8        Pin enabled:FALSE
ephone 9        Pin enabled:FALSE
```

Table 1 describes significant fields in this output.

Field

Description

ephone phone-tag

Phone
                                          					 identified with its unique phone-tag sequence number.

Pin
                                          					 enabled

TRUE
                                          					 indicates that a PIN has been defined for this phone. FALSE indicates that no
                                          					 PIN has been defined for this phone.

Logged-in

TRUE
                                          					 indicates that a phone user is currently logged in on this phone. FALSE
                                          					 indicates that no phone user is currently logged in on this phone.

### Related Commands

Command

Description

login (telephony-service)

Defines
                                          						when users of IP phones in a Cisco Unified CME system are logged out
                                          						automatically.

pin

Sets
                                          						set a personal identification number (PIN) for an IP phone in a Cisco Unified
                                          						CME system.

show ephone

Displays statistical information about registered Cisco IP phones.

## show ephone
                        	 moh

To display
                              		  information about moh files in use, use the show ephone moh command in global configuration mode.

show ephone moh

### Syntax Description

This command has
                              		  no arguments or keywords

### Command Modes

Global Configuration mode.

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.0(1)XA

Cisco
                                          						Unified CME 8.0 Cisco Unified SRST 8.0

This
                                          						command was introduced.

15.1(1)T

Cisco
                                          						Unified CME 8.0 Cisco Unified SRST 8.0

This
                                          						command was integrated into Cisco IOS Release 15.1(1)T.

### Usage Guidelines

Use the show
                              		  ephone moh to display information about the different MOH group configured. The
                              		  following examples displays different MOH group configured.

## Examples

```
Router #show ephone moh
Skinny Music On Hold Status (moh-group 1)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/minuet.au (not cached) type AU Media_Payload_G711Ulaw64k 160 bytes
Moh multicast 239.10.16.6 port 2000
Skinny Music On Hold Status (moh-group 2)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/audio/hello.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.6 port 2000 via 0.0.0.0
Skinny Music On Hold Status (moh-group 3)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/bells.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.5 port 2000 via 0.0.0.0
Skinny Music On Hold Status (moh-group 4)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/3003.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.7 port 2000 via 0.0.0.0
Skinny Music On Hold Status (moh-group 5)
Active MOH clients 0 (max 830), Media Clients 0
File flash:/4004.au type AU Media_Payload_G711Ulaw64k  160 bytes
Moh multicast on 239.10.16.8 port 2000 via 0.0.0.0
```

### Related Commands

Command

Description

show
                                          						ephone-dn

Displays MOH group information for a phone directory number.

show
                                          						ephone summary

Displays the information about the MOH files in use

show
                                          						voice moh-group statistics

Displays the MOH subsystem statistics information

## show ephone offhook

To display information and packet counts for the phones that are
                              		  currently off hook, use the show ephone offhook command in privileged EXEC mode.

show ephone offhook

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

## Examples

The following sample output is displayed when no phone is off hook:

```
Router# show ephone offhook No ephone in specified type/condition.
```

The following sample output displays information for a phone that is
                              		  off hook:

```
Router# show ephone offhook ephone-5 Mac:000A.8A2C.8C6E TCP socket:[20] activeLine:1 REGISTERED
mediaActive:0 offhook:1 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:10.22.84.71 51228 Telecaster 7960  keepalive 43218 max_line 6
button 1:dn 9  number 59943 CH1 SIEZE     silent-ring
button 2:dn 10 number 59943 CH1 IDLE
button 3:dn 42 number A4400  auto dial A4500 CH1 IDLE
button 4:dn 96 number 69943  auto dial 95259943 CH1 IDLE
button 5:dn 75 number 49943  auto dial 49943 CH1 IDLE
speed dial 1:57514 marketing
Active Call on DN 9 chan 1 :59943 0.0.0.0 0 to 0.0.0.0 2000 via 172.30.151.1
G711Ulaw64k  160 bytes vad
Tx Pkts 0 bytes 0 Rx Pkts 0 bytes 0 Lost 0
Jitter 0 Latency 0 callingDn -1 calledDn -1
Username:user1 Password:newuser
```

The following sample output displays information for a phone that has
                              		  just completed a call:

```
Router# show ephone offhook ephone-5 Mac:000A.8A2C.8C6E TCP socket:[20] activeLine:1 REGISTERED
mediaActive:1 offhook:1 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:10.22.84.71 51228 Telecaster 7960  keepalive 43224 max_line 6
button 1:dn 9  number 59943 CH1 CONNECTED silent-ring
button 2:dn 10 number 59943 CH1 IDLE
button 3:dn 42 number A4400  auto dial A4500 CH1 IDLE
button 4:dn 96 number 69943  auto dial 95259943 CH1 IDLE
button 5:dn 75 number 49943  auto dial 49943 CH1 IDLE
speed dial 1:57514 marketing
Active Call on DN 9 chan 1 :59943 10.23.84.71 22926 to 172.30.131.129 2000 via 172.30.151.1
G711Ulaw64k  160 bytes no vad
Tx Pkts 0 bytes 0 Rx Pkts 0 bytes 0 Lost 0
Jitter 0 Latency 0 callingDn -1 calledDn -1 (media path callID 19288 srcCallID 1
9289)
Username:user1 Password:newuser
```

The show ephone command describes significant fields in
                              		  this output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone
                        	 overlay

To display
                              		  information for the registered phones that have overlay ephone-dns associated
                              		  with them, use the show ephone overlay in privileged EXEC mode.

show ephone overlay

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

### Usage Guidelines

This command does
                              		  not apply to Cisco Unified SRST.

## Examples

The following is
                              		  sample output from the show ephone overlay command:

```
Router# show ephone overlay ephone-1 Mac:0007.0EA6.353A TCP socket:[1] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:10.2.225.205 52486 Telecaster 7960  keepalive 2771 max_line 6
button 1: dn 11 number 60011 CH1 IDLE      overlay 
button 2: dn 17 number 60017 CH1 IDLE      overlay 
button 3: dn 24 number 60024 CH1 IDLE      overlay 
button 4: dn 30 number 60030 CH1 IDLE      overlay 
button 5: dn 36 number 60036 CH1 IDLE      CH2 IDLE      overlay 
button 6: dn 39 number 60039 CH1 IDLE      CH2 IDLE      overlay 
overlay 1: 11(60011) 12(60012) 13(60013) 14(60014) 15(60015) 16(60016) 
overlay 2: 17(60017) 18(60018) 19(60019) 20(60020) 21(60021) 22(60022) 
overlay 3: 23(60023) 24(60024) 25(60025) 26(60026) 27(60027) 28(60028) 
overlay 4: 29(60029) 30(60030) 31(60031) 32(60032) 33(60033) 34(60034) 
overlay 5: 35(60035) 36(60036) 37(60037) 
overlay 6: 38(60038) 39(60039) 40(60040)
```

The show ephone command describes significant fields in
                              		  this output. Table 1 describes a field that is not in that table.

Field

Description

overlay number

Displays
                                          					 the contents of an overlay set, including each dn-tag and its associated
                                          					 extension number.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP phones.

## show ephone
                        	 phone-load

To display
                              		  information about the phone firmware that is loaded on registered phones, use
                              		  the show ephone phone-load command in privileged EXEC mode.

show ephone phone-load

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

## Examples

The following is
                              		  sample output that displays the phone firmware versions for all phones in the
                              		  system:

```
Router# show ephone phone-load DeviceName        CurrentPhoneload       PreviousPhoneload      LastReset
=====================================================================
SEP0002B9AFC49F   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP003094C2D0B0   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP000C30F03707   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP003094C2999F   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP000A8A2C8C6E   3.2(2.14)              3.2(2.14)              Initialized
SEP0002B9AFBB4D   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP00075078627F   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP0002FD659E59   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP00024BCCD626   3.2(2.14)                                     CM-closed-TCP
SEP0008215F88C1   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP000C30F0390C   3.2(2.14)              3.2(2.14)              TCP-timeout
SEP003094C30143   3.2(2.14)              3.2(2.14)              TCP-timeout
```

Table 1 describes
                              		  significant fields in this output.

Field

Description

DeviceName

Device
                                          					 name.

CurrentPhoneLoad

Current
                                          					 phone firmware version.

PreviousPhoneLoad

Phone
                                          					 firmware version before last phone load.

LastReset

Reason
                                          					 for last reset of phone.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP phones.

## show ephone registered

To display the status of registered phones, use the show ephone registered command in privileged EXEC mode.

show ephone registered

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

## Examples

The following is sample output from the show ephone registered
                              		  command:

```
Router# show ephone registered ephone-2 Mac:000A.8A5C.5961 TCP socket:[1] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:192.168.0.50 50349 Telecaster 7940  keepalive 23738 max_line 2
button 1: dn 2  number 91450 CH1 IDLE      CH2 IDLE 
button 2: dn 0   -- 
button 3: dn 0   -- 
button 4: dn 0   -- 
button 5: dn 0   -- 
button 6: dn 0   --
```

The show ephone command describes significant fields in
                              		  this output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone remote

To display nonlocal phones (phones with no Address Resolution
                              		  Protocol [ARP] entry), use the show ephone remote command in privileged EXEC mode.

show ephone remote

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

Phones without ARP entries are suspected not to be on the LAN. Use
                              		  the show ephone remote command to identify phones without ARP
                              		  entries that might have operational issues.

## Examples

The following is sample output that identifies ephone 2 as not having
                              		  an ARP entry:

```
Router# show ephone remote ephone-2 Mac:0185.047C.993E TCP socket:[4] activeLine:0 REGISTERED
mediaActive:1 offhook:0 ringing:0 reset:0 reset_sent:0 paging 1 debug:0
IP:10.50.50.20 49231 Telecaster 7910  keepalive 112 max_line 2 dual-line
button 1:dn 3  number 95021 CH1 IDLE
paging-dn 25
```

The show ephone command describes significant fields in
                              		  this output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone ringing

To display information on phones that are ringing, use the show ephone ringing command in privileged EXEC mode.

show ephone ringing

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

## Examples

The following is sample output from the show ephone ringing command:

```
Router# show ephone ringing ephone-1 Mac:0005.5E37.8090 TCP socket:[1] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:1 reset:0 reset_sent:0 paging 0 debug:0
IP:10.50.50.10 49329 Telecaster 7960  keepalive 17602 max_line 6
button 1:dn 1  number 95011 CH1 RINGING   CH2 IDLE
button 2:dn 2  number 95012 CH1 IDLE
```

The show ephone command describes significant fields in
                              		  this output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone summary

To display brief information about Cisco IP phones, use the show ephone summary command in privileged EXEC mode.

show ephone summary

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco CME 1.0 Cisco SRST 1.0

This command was introduced.

12.2(8)T

Cisco CME 2.0 Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						.

15.0(1)XA

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was modified. The output was enhanced to show
                                          						IPv6 or IPv4 addresses configured on ephones.

15.1(1)T

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was modified. The output was enhanced to show
                                          						voice-class stun-usage information.

## Examples

The following is sample output from the show ephone summary command:

```
Router# show ephone summary hairpin_block:
ephone-1[0] Mac:FCAC.3BAE.0000 TCP socket:[17] activeLine:0 whisperLine:0 REGISTERED
mediaActive:0 whisper_mediaActive:0 startMedia:0 offhook:0 ringing:0 reset:0 reset_sent:0 debug:0  primary_dn: 1*
IP:10.2.1.0 * SCCP Gateway (AN)  keepalive 2966   music 0  1:1
port 0/0/0
voice-class stun is enabled
ephone-2[1] Mac:FCAC.3BAE.0001 TCP socket:[18] activeLine:0 whisperLine:0 REGISTERED
mediaActive:0 whisper_mediaActive:0 startMedia:0 offhook:0 ringing:0 reset:0 reset_sent:0 debug:0  primary_dn: 2*
IP:10.2.1.5 * SCCP Gateway (AN)  keepalive 2966   music 0  1:2
port 0/0/1
voice-class stun is enabled
ephone-4 Mac:0030.94C3.F43A TCP socket:[-1] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 debug:0
IP:10.2.1.1 Telecaster 7960  keepalive 59 
Max 48, Registered 1, Unregistered 0, Deceased 0, Sockets 1
Max Conferences 4 with 0 active (4 allowed)
Skinny Music On Hold Status
Active MOH clients 0 (max 72), Media Clients 0
No MOH file loaded
```

The show ephone command describes significant fields in
                              		  this output.

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                       						phones.

## show ephone tapiclients

To display status of ephone Telephony Application Programming
                              		  Interface (TAPI) clients, use the show ephone tapiclients command in privileged EXEC mode.

show ephone tapiclients

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

## Examples

The following is sample output from the show ephone tapiclients command:

```
Router# show ephone tapiclients ephone-4 Mac:0007.0EA6.39F8 TCP socket:[2] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:192.168.1.18 50291 Telecaster 7960  sub=3 keepalive 728 max_line 20
button 1:dn 6  number 1004 CH1 IDLE      CH2 IDLE
button 2:dn 1  number 1000 CH1 IDLE      shared
button 3:dn 2  number 1000 CH1 IDLE      shared
button 7:dn 3  number 1001 CH1 IDLE      CH2 IDLE      monitor-ring shared
button 8:dn 4  number 1002 CH1 IDLE      CH2 IDLE      monitor-ring shared
button 9:dn 5  number 1003 CH1 IDLE      CH2 IDLE      monitor-ring
button 10:dn 91 number A00  auto dial A01 CH1 IDLE
speed dial 1:2000 PAGE-STAFF
speed dial 2:2001 HUNT-STAFF
paging-dn 90
Username:userB Password:ge30qe
Tapi client information
Username:userB status:REGISTERED Socket :[5]
 Tapi Client IP address: 192.168.1.5  Port:2295
```

The show ephone command describes significant fields in
                              		  this output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone telephone-number

To display information for the phone associated with a specified
                              		  number, use the show ephone telephone-number command in privileged EXEC mode.

show ephone telephone-number number

### Syntax Description

number

Telephone number that is associated with an ephone.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

Use this command to find the phone on which a particular telephone
                              		  number appears.

## Examples

The following is sample output from the show ephone telephone-number command:

```
Router# show ephone telephone-number 91400 DP tag: 0, primary
Tag 1, Normal or Intercom dn
  ephone 1, mac-address 000A.0E51.19F0, line 1
```

The show ephone command describes significant fields in
                              		  this output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show ephone unregistered

To display information about unregistered phones, use the show ephone unregistered command in privileged EXEC mode.

show ephone unregistered

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

There are two ways that an ephone can become unregistered. The first
                              		  way is when an ephone is listed in the running configuration but no physical
                              		  device has been registered for that ephone. The second way is when an unknown
                              		  device was registered at some time after the last router reboot but has since
                              		  unregistered.

## Examples

The following is sample output from the show ephone unregistered command:

```
Router# show ephone unregistered ephone-1 Mac:0007.0E81.10F0 TCP socket:[-1] activeLine:0 UNREGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:0.0.0.0 0 Unknown 0  keepalive 0 max_line 0
```

The show ephone command describes significant fields in
                              		  this output.

### Related Commands

Command

Description

show ephone

Displays statistical information about registered Cisco IP
                                          						phones.

## show
                        	 ephone-dn

To display status
                              		  and information for a Cisco IP phone destination number or for extensions
                              		  (ephone-dns) in a Cisco Unified Communications Manager Express (Cisco Unified
                              		  CME) or Cisco Unified Survivable Remote Site Telephony (SRST) environment, use
                              		  the show ephone-dn command in privileged EXEC mode.

show ephone-dn [dn-tag]

### Syntax Description

dn-tag

(Optional) For Cisco Unified CME, a unique sequence number that is used during
                                          						configuration to identify a particular extension (ephone-dn).

(Optional) For Cisco Unified SRST, a destination number tag. The destination
                                          						number can be from 1 to 288.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						CME 1.0 Cisco SRST 1.0

This
                                          						command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						IAD2420 series.

12.2(2)XT

Cisco
                                          						CME 2.0 Cisco SRST 2.0

This
                                          						command was implemented on the Cisco 1750 and Cisco 1751.

12.2(8)T

Cisco
                                          						CME 2.0 Cisco SRST 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725 and Cisco 3745.

12.2(8)T1

Cisco
                                          						CME 2.0 Cisco SRST 2.0

This
                                          						command was implemented on the Cisco 2600XM and Cisco 2691.

12.2(11)T

Cisco
                                          						CME 2.01 Cisco SRST 2.01

This
                                          						command was implemented on the Cisco 1760.

12.3(4)T

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

## Examples

## Examples

The following
                              		  Cisco Unified CME sample output displays status and information for all
                              		  ephone-dns:

```
Router# show ephone-dn 50/0/1 CH1 DOWN 
EFXS 50/0/1 Slot is 50, Sub-unit is 0, Port is 1
 Type of VoicePort is EFXS
 Operation State is UP
 Administrative State is UP
 No Interface Down Failure
 Description is not set
 Noise Regeneration is enabled
 Non Linear Processing is enabled
 Non Linear Mute is disabled
 Non Linear Threshold is -21 dB
 Music On Hold Threshold is Set to -38 dBm
 In Gain is Set to 0 dB
 Out Attenuation is Set to 0 dB
 Echo Cancellation is enabled
 Echo Cancellation NLP mute is disabled
 Echo Cancellation NLP threshold is -21 dB
 Echo Cancel Coverage is set to 8 ms
 Playout-delay Mode is set to adaptive
 Playout-delay Nominal is set to 60 ms
 Playout-delay Maximum is set to 200 ms
 Playout-delay Minimum mode is set to default, value 40 ms 
 Playout-delay Fax is set to 300 ms
 Connection Mode is normal
 Connection Number is not set
 Initial Time Out is set to 10 s
 Interdigit Time Out is set to 10 s
 Call Disconnect Time Out is set to 60 s
 Ringing Time Out is set to 180 s
 Wait Release Time Out is set to 30 s
 Companding Type is u-law
 Region Tone is set for US
 Station name None, Station number 91400
 Caller ID Info Follows:
 Standard BELLCORE
 Translation profile (Incoming): 
 Translation profile (Outgoing): 
 Digit Duration Timing is set to 100 ms
50/0/2 CH1 IDLE      CH2 IDLE        
EFXS 50/0/2 Slot is 50, Sub-unit is 0, Port is 2
 Type of VoicePort is EFXS
 Operation State is DORMANT
 Administrative State is UP
 No Interface Down Failure
 Description is not set
 Noise Regeneration is enabled
 Non Linear Processing is enabled
 Non Linear Mute is disabled
 Non Linear Threshold is -21 dB
 Music On Hold Threshold is Set to -38 dBm
 In Gain is Set to 0 dB
 Out Attenuation is Set to 0 dB
 Echo Cancellation is enabled
 Echo Cancellation NLP mute is disabled
 Echo Cancellation NLP threshold is -21 dB
 Echo Cancel Coverage is set to 8 ms
 Playout-delay Mode is set to adaptive
 Playout-delay Nominal is set to 60 ms
 Playout-delay Maximum is set to 200 ms
 Playout-delay Minimum mode is set to default, value 40 ms 
 Playout-delay Fax is set to 300 ms
 Connection Mode is normal
 Connection Number is not set
 Initial Time Out is set to 10 s
 Interdigit Time Out is set to 10 s
 Call Disconnect Time Out is set to 60 s
 Ringing Time Out is set to 180 s
 Wait Release Time Out is set to 30 s
 Companding Type is u-law
 Region Tone is set for US
 Station name None, Station number 91450
 Caller ID Info Follows:
 Standard BELLCORE
 Translation profile (Incoming): 
 Translation profile (Outgoing): 
 Digit Duration Timing is set to 100 ms
```

## Examples

The following
                              		  SRST sample output displays status and information for all ephone-dns:

```
Router# show ephone-dn 7 50/0/7 INVALID     
EFXS 50/0/7 Slot is 50, Sub-unit is 0, Port is 7
 Type of VoicePort is EFXS
 Operation State is UP
 Administrative State is UP
 No Interface Down Failure
 Description is not set
 Noise Regeneration is enabled
 Non Linear Processing is enabled
 Non Linear Mute is disabled
 Non Linear Threshold is -21 dB
 Music On Hold Threshold is Set to -38 dBm
 In Gain is Set to 0 dB
 Out Attenuation is Set to 0 dB
 Echo Cancellation is enabled
 Echo Cancellation NLP mute is disabled
 Echo Cancellation NLP threshold is -21 dB
 Echo Cancel Coverage is set to 8 ms
 Playout-delay Mode is set to default
 Playout-delay Nominal is set to 60 ms
 Playout-delay Maximum is set to 200 ms
 Playout-delay Minimum mode is set to default, value 4 ms 
 Playout-delay Fax is set to 300 ms
 Connection Mode is normal
 Connection Number is not set
 Initial Time Out is set to 10 s
 Interdigit Time Out is set to 10 s
 Call Disconnect Time Out is set to 60 s
 Ringing Time Out is set to 8 s
 Wait Release Time Out is set to 30 s
 Companding Type is u-law
 Region Tone is set for US
 Station name None, Station number None
 Caller ID Info Follows:
 Standard BELLCORE
 Voice card specific Info Follows:
 Digit Duration Timing is set to 100 ms
```

Table 1 describes significant fields in the output from this command.

Field

Description

Administrative State

Administrative (configured) state of the voice port.

alert

The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the call alerting state (for example, because the far-end phone
                                          					 rang but was not answered and the far-end system decided to drop the call
                                          					 rather than let the phone ring for too long).

answered (incoming)

The
                                          					 number of incoming calls that were actually answered (the phone goes off hook
                                          					 when ringing).

answered (outgoing)

The
                                          					 number of outgoing call attempts that were answered by the far end.

busy

The
                                          					 number of outgoing call attempts that got a busy response.

Call
                                          					 Disconnect Time Out

Not
                                          					 applicable to the Cisco IP phone.

called,
                                          					 calling

Extension numbers of called and calling parties.

Caller
                                          					 ID Info Follows

Information about the caller ID.

Call
                                          					 Ref

A
                                          					 unique per-call identifier used by the SCCP protocol. The Call Ref values are
                                          					 assigned sequentially within the Cisco CME–SCCP interface, so this value also
                                          					 indicates the total number of SCCP calls since the router was last rebooted.

chan

Channel
                                          					 number of an ephone-dn.

CODEC

Codec
                                          					 type.

Companding Type

Not
                                          					 applicable to the Cisco IP phone.

connect

The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the call connected state.

Connection Mode

Not
                                          					 applicable to the Cisco IP phone.

Connection Number

Not
                                          					 applicable to the Cisco IP phone.

Description

Not
                                          					 applicable to the Cisco IP phone.

Digit
                                          					 Duration Timing

Not
                                          					 applicable to the Cisco IP phone.

DN
                                          					 STATE

Ephone-dn tag number and state of the phone line associated with an extension.

Echo
                                          					 Cancellation...

Not
                                          					 applicable to the Cisco IP phone.

Echo
                                          					 Cancel Coverage

Not
                                          					 applicable to the Cisco IP phone.

EFXS

Voice
                                          					 port type.

Far-end
                                          					 disconnect at...

See
                                          					 connect, alert, hold, and ring.

Final
                                          					 Jitter

The
                                          					 final voice packet receive jitter reported by the IP phone at the end of the
                                          					 call.

hold

The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the call hold state (for example, if the caller was left on hold
                                          					 for too long and got tired of waiting).

incoming

The
                                          					 number of incoming calls presented (the phone rings).

In Gain

Not
                                          					 applicable to the Cisco IP phone.

Initial
                                          					 Time Out

Amount
                                          					 of time the system waits for an initial input digit from the caller.

Interdigit Time Out

Amount
                                          					 of time the system waits for a subsequent input digit from the caller.

Last 64
                                          					 far-end disconnect cause codes

See the
                                          					 Mappings of PSTN Cause Codes to SIP Event table for a list of public switch
                                          					 telephone network (PSTN) cause codes that can be sent as an ISDN cause
                                          					 information element (IE) and the corresponding Session Interface Protocol (SIP)
                                          					 event.

Latency

The
                                          					 final voice packet receive latency reported by the IP phone at the end of the
                                          					 call.

Lost

Number
                                          					 of lost packets.

Music
                                          					 On Hold Threshold

Not
                                          					 applicable to the Cisco IP phone.

No
                                          					 Interface Down Failure

State
                                          					 of the interface.

Noise
                                          					 Regeneration

Not
                                          					 applicable to the Cisco IP phone.

Non
                                          					 Linear...

Not
                                          					 applicable to the Cisco IP phone.

Operation State

Operational state of the voice port.

Out
                                          					 Attenuation

Not
                                          					 applicable to the Cisco IP phone.

outgoing

The
                                          					 number of outgoing call attempts.

Playout-delay Maximum

Not
                                          					 applicable to the Cisco IP phone.

Playout-delay...

Not
                                          					 applicable to the Cisco IP phone.

Port

Port
                                          					 number for the interface associated with the voice interface card.

Region
                                          					 Tone

Not
                                          					 applicable to the Cisco IP phone.

ring

The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the ringing state (for example, if the call was not answered and
                                          					 the caller hung up).

Ringing
                                          					 Time Out

Duration, in seconds, for which ringing is to continue if a call is not
                                          					 answered. Set with the timeouts ringing command.

Rx
                                          					 Pkts, bytes

Number
                                          					 of packets and bytes received during the current or last call.

Signal
                                          					 Level to phone, peak

For
                                          					 G.711 calls only, this parameter indicates the most recent voice signal level
                                          					 in the voice IP packets sent from the router to the IP phone. This parameter is
                                          					 valid only for VoIP or PSTN G.711 calls to the IP phones. This parameter is not
                                          					 valid for calls between local IP phones, or calls that use codecs other than
                                          					 G.711. The peak field indicates the peak signal level seen during the entire
                                          					 call.

Slot

Slot
                                          					 used in the voice interface card for this port.

Station
                                          					 name

Station
                                          					 name.

Station
                                          					 number

Station
                                          					 number.

Sub-unit

Subunit
                                          					 used in the voice interface card for this port.

Tx
                                          					 Pkts, bytes

Number
                                          					 of packets and bytes transmitted during the current call or last call.

Type of
                                          					 VoicePort

Voice
                                          					 port type.

VAD

Voice
                                          					 activity detection.

Voice
                                          					 card specific info

Information specific to the voice card.

VPM
                                          					 STATE

State
                                          					 indication for the VPM software component.

VTSP
                                          					 STATE

State
                                          					 indication for the VTSP software component.

Wait
                                          					 Release Time Out

Time
                                          					 that a voice port stays in the call-failure state while the router sends a busy
                                          					 tone, reorder tone, or out-of-service tone to the port.

The following
                              		  table lists the PSTN cause codes that can be sent as an ISDN cause information
                              		  element (IE) and the corresponding SIP event for each. These are the far-end
                              		  disconnect cause codes listed in the output for the show ephone-dn statistics command.

PSTN
                                          					 Cause Code

Description

SIP
                                          					 Event

1

Unallocated number

410
                                          					 Gone

3

No
                                          					 route to destination

404 Not
                                          					 found

16

Normal
                                          					 call clearing

BYE

17

User
                                          					 busy

486
                                          					 Busy here

18

No user
                                          					 responding

480
                                          					 Temporarily unavailable

19

No
                                          					 answer from the user

21

Call
                                          					 rejected

603
                                          					 Decline

22

Number
                                          					 changed

302
                                          					 Moved temporarily

27

Destination out of order

404 Not
                                          					 found

28

Address
                                          					 incomplete

484
                                          					 Address incomplete

29

Facility rejected

501 Not
                                          					 implemented

31

Normal
                                          					 unspecified

404 Not
                                          					 found

34

No
                                          					 circuit available

503
                                          					 Service unavailable

38

Network
                                          					 out of order

41

Temporary failure

42

Switching equipment congestion

44

Requested channel not available

47

Resource unavailable

55

Incoming class barred within CUG

603
                                          					 Decline

57

Bearer
                                          					 capability not authorized

501 Not
                                          					 implemented

58

Bearer
                                          					 capability not presently available

63

Service
                                          					 or option unavailable

503
                                          					 Service unavailable

65

Bearer
                                          					 cap not implemented

501 Not
                                          					 implemented

79

Service
                                          					 or option not implemented

87

User
                                          					 not member of CUG

603
                                          					 Decline

88

Incompatible destination

400 Bad
                                          					 Request

95

Invalid
                                          					 message

102

Recover
                                          					 on timer expiry

408
                                          					 Request timeout

111

Protocol error

400 Bad
                                          					 request

127

Interworking unspecified

500
                                          					 Internal server error

Any
                                          					 code other than those listed above

500
                                          					 Internal server error

### Related Commands

Command

Description

show ephone-dn callback

Displays information about pending callbacks in a Cisco Unified CME or a Cisco
                                          						Unified SRST environment.

show ephone-dn loopback

Displays information about loopback ephone-dns that have been created in a
                                          						Cisco Unified CME or a Cisco Unified SRST environment.

show ephone-dn statistics

Displays display call statistics for a Cisco IP destination or for extensions
                                          						(ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST environment.

show ephone-dn summary

Displays brief information about Cisco IP phone destination numbers or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment.

## show ephone-dn
                        	 callback

To display
                              		  information about pending callbacks in a Cisco Unified Communications Manager
                              		  Express (Cisco Unified CME) or a Cisco Unified Survivable Remote Site Telephony
                              		  (Cisco Unified SRST) environment, use the show ephone-dn callback command in privileged EXEC mode.

show ephone-dn callback

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						CME 3.0 Cisco SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

## Examples

The following
                              		  sample output shows a callback placed by ephone-dn 1 against ephone-dn 3.
                              		  Ephone-dn 3 has its channel 1 on hold and has just seized dial tone on its
                              		  channel 2.

```
Router# show ephone-dn callback DN 3 (95021) CallBack pending to DN 1 (95021) for ephone-1 age 7 seconds
State for DN 3 is CH1 HOLD      CH2 SIEZE
```

The following
                              		  sample output shows a callback placed by ephone-dn 1 against ephone-dn 3.
                              		  Ephone-dn 3 has a call in progress on channel 1.

```
Router# show ephone-dn callback DN 3 (95021) CallBack pending to DN 1 (95021) for ephone-1 age 8 seconds
State for DN 3 is CH1 CONNECTED
```

Significant
                              		  fields in the output from this command are described in Table 1 .

Field

Description

DN 3
                                          					 (95021) CallBack pending to DN 1 (95021)

Callback
                                          					 originator is the extension with the dn-tag 1 (in this example), and the
                                          					 callback has been placed on the extension with the dn-tag 3 and the number
                                          					 95021.

age

Number of
                                          					 seconds since the callback was placed.

State for
                                          					 DN 3 is CH1... CH2...

Call
                                          					 states for channel 1 and channel 2, if any, of the extension that the callback
                                          					 is for.

### Related Commands

Command

Description

show ephone-dn

Displays status and information for a Cisco IP phone destination number or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment.

## show ephone-dn
                        	 loopback

To display
                              		  information about loopback ephone-dns that have been created in a Cisco Unified
                              		  Communications Manager Express (Cisco Unified CME) or a Cisco Unified
                              		  Survivable Remote Site Telephony (Cisco Unified SRST) environment, use the show ephone-dn loopback command in privileged EXEC mode.

show ephone-dn loopback

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						CME 1.0 Cisco SRST 1.0

This
                                          						command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						IAD2420 series.

12.2(2)XT

Cisco
                                          						CME 2.0 Cisco SRST 2.0

This
                                          						command was implemented on the Cisco 1750 and Cisco 1751.

12.2(8)T

Cisco
                                          						CME 2.0 Cisco SRST 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725 and Cisco 3745.

12.2(8)T1

Cisco
                                          						CME 2.0 Cisco SRST 2.0

This
                                          						command was implemented on the Cisco 2600XM and Cisco 2691.

12.2(11)T

Cisco
                                          						CME 2.01 Cisco SRST 2.01

This
                                          						command was implemented on the Cisco 1760.

## Examples

The following
                              		  example displays information for a loopback using ephone-dn 21 and ephone-dn
                              		  22:

```
Router# show ephone-dn loopback LOOPBACK DN status (min 21, max 22):
DN 21 51...  Loopback to DN 22 CH1 IDLE
CallingDn -1 CalledDn -1 Called   Calling   G711Ulaw64k
Strip NONE, Forward 2, prefix 10 retry 10 Media 0.0.0.0 0
callID 0 srcCallID 0 ssrc 0 vector 0
DN 22 11...  Loopback to DN 21 CH1 IDLE
CallingDn -1 CalledDn -1 Called   Calling   G711Ulaw64k
Strip NONE, Forward 2, prefix 50 retry 10 Media 0.0.0.0 0
callID 0 srcCallID 0 ssrc 0 vector 0
```

Significant
                              		  fields in the output from this command are described in Table 1 ,
                              		  in alphabetical order.

Field

Description

Called,
                                          					 Calling

Called
                                          					 number and calling number when there is a call present.

CalledDn,
                                          					 CallingDn

Ephone-dn
                                          					 tag numbers of the called and calling ephone-dn. Set to -1 if the call is not
                                          					 to or from an ephone-dn, or if there is no active call.

callID

Internal
                                          					 call reference. This usage is the same as in other Cisco IOS voice gateway
                                          					 commands.

DN

Ephone-dn
                                          					 tag (sequence number).

Forward

Number of
                                          					 digits in the original called number to forward to the other ephone-dn in the
                                          					 loopback-dn pair.

G711...

G711Ulaw64k indicates G.711 codec, mu-law, 64000-bit stream. G711alaw64k
                                          					 indicates G.711 codec, A-law, 64000-bit stream.

Loopback to ...

Indicates the opposite ephone-dn in the loopback pair and the status of that
                                          					 ephone-dn.

Media

IP
                                          					 destination address, if any, for any voice packets that are passing through the
                                          					 loopback DN.

min,
                                          					 max

Lowest
                                          					 and highest dn-tag numbers of ephone-dns that are configured as loopback-dns.

prefix

Digit
                                          					 string to add to the beginning of forwarded called numbers.

retry

Number
                                          					 of seconds to wait before retrying the loopback target when is it busy.

srcCallID

Internal call reference for the destination.

ssrc

Real-time transport protocol (RTP) synchronization source (SSRC) of the most
                                          					 recent RTP packet.

Strip

Number
                                          					 of leading digits to strip before forwarding to the other extension in the
                                          					 loopback-dn pair.

vector

The
                                          					 following values describe the media path for voice packets that pass through
                                          					 the loopback-dn:

- 0—No
                                             						media path or not a loopback-dn path (inactive).

- 1—Normal path. Loopback-dn has identified the final media destination as a
                                             						local IP phone. The media IP address field shows a valid, non-zero value.

- 2—Hairpin. Media packets are routed back through paired loopback-dns. The final
                                             						destination is not known. For example, this can be a VoIP-to-VoIP call path by
                                             						a loopback-dn.

- 3—Hairpin. The final destination is an ephone-dn in a special mode such as
                                             						paging.

- 4—Loopback-dn chain has been detected, in which two loopback-dn pairs have been
                                             						connected together.

- 5—Loopback-dn chain has been detected in which more than two loopback-dn pairs
                                             						are connected in series.

### Related Commands

Command

Description

loopback-dn

Creates a virtual loopback voice port (loopback-dn) to establish a demarcation
                                          						point for VoIP voice calls and supplementary services.

show ephone-dn

Displays status and information for a Cisco IP phone destination number or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment.

## show ephone-dn statistics

To display call statistics for a Cisco IP destination or for
                              		  extensions (ephone-dns) in a Cisco Unified Communications Manager Express
                              		  (Cisco Unified CME) or a Cisco Unified Survivable Remote Site Telephony (Cisco
                              		  Unified SRST) environment, use the show ephone-dn command in privileged EXEC mode.

show ephone-dn [dn-tag] statistics

### Syntax Description

dn-tag

(Optional) Unique sequence number that is used during
                                          						configuration to identify a particular extension (ephone-dn).

statistics

Displays voice quality statistics on calls for a specified
                                          						extension or for all extensions.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ1

Cisco CME 3.0 Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0 Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

## Examples

The following sample output displays statistics for all extensions
                              		  (ephone-dns) in a Cisco Unified CME system. There are two ephone-dns (DN1 and
                              		  DN3) in this example.

```
Router# show ephone-dn statistics Total Calls 103
Stats may appear to be inconsistent for conference or shared line cases
DN 1 chan 1 incoming 36 answered 21 outgoing 60 answered 30 busy 6
Far-end disconnect at:connect 29 alert 18 hold 7 ring 15
Last 64 far-end disconnect cause codes
17 17 17 17 17 17 16 16 16 16 16 16 16 16 16 16
16 16 16 16 65 16 65 65 65 65 16 65 65 65 16 16
16 16 16 16 16 16 16 16 16 16 16 16 16 65 47 65
47 47 16 16 16 16 16 16 16 16 16 16 16 16 16 16
local phone on-hook
DN 1 chan 1 (95011) voice quality statistics for last call
Call Ref 103 called 91500 calling 95011
Total Tx Pkts 0 bytes 0 Rx Pkts 0 bytes 0 Lost 0
Final Jitter 30 Latency 0 Lost 0
Signal Level to phone 0 (-78 dB) peak 0 (-78 dB)
Packets counted by router 0
DN 1 chan 2 incoming 0 answered 0 outgoing 1 answered 0 busy 0
Far-end disconnect at:connect 0 alert 0 hold 0 ring 0
Last 64 far-end disconnect cause codes
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
local phone on-hook
DN 1 chan 2 (95011) voice quality statistics for last call
Call Ref 86 called  calling
Total Tx Pkts 0 bytes 0 Rx Pkts 0 bytes 0 Lost 0
Final Jitter 0 Latency 0 Lost 0
Signal Level to phone 0 (-78 dB) peak 0 (-78 dB)
Packets counted by router 0
DN 3 chan 1 incoming 0 answered 0 outgoing 1 answered 1 busy 0
Far-end disconnect at:connect 0 alert 0 hold 0 ring 0
Last 64 far-end disconnect cause codes
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
DN 3 chan 1 (95021) voice quality statistics for current call
Call Ref 102 called 94011 calling 95021
Current Tx Pkts 241 bytes 3133 Rx Pkts 3304 bytes 515023 Lost 0
Jitter 30 Latency 0
Worst Jitter 30 Worst Latency 0
Signal Level to phone 201 (-39 dB) peak 5628 (-12 dB)
Packets counted by router 3305
```

The following sample output displays voice quality statistics for the
                              		  ephone-dn with dn-tag 2:

```
Router# show ephone-dn 2 statistics DN 2 chan 1 incoming 0 answered 0 outgoing 2 answered 0 busy 0
Far-end disconnect at: connect 0 alert 0 hold 0 ring 0
Last 64 far-end disconnect cause codes
28 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
local phone on-hook
DN 2 chan 1 (91450) voice quality statistics for last call
Call Ref 2 called  calling 
Total Tx Pkts 0 bytes 0 Rx Pkts 0 bytes 0 Lost 0
Final Jitter 0 Latency 0 Lost 0
Signal Level to phone 0 (-78 dB) peak 0 (-78 dB)
Packets counted by router 0
```

The show ephone-dn command describes significant fields in
                              		  the output from this command.

### Related Commands

Command

Description

show ephone-dn

Displays status and information for a Cisco IP phone
                                          						destination number or for extensions (ephone-dns) in a Cisco Unified CME or a
                                          						Cisco Unified SRST environment.

## show ephone-dn
                        	 summary

To display brief
                              		  information about Cisco IP phone destination numbers or for extensions
                              		  (ephone-dns) in a Cisco Unified Communications Manager Express (Cisco Unified
                              		  CME) or a Cisco Unified Survivable Remote Site Telephony (Cisco Unified SRST)
                              		  environment, use the show ephone-dn summary command in privileged EXEC mode.

show ephone-dn summary

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						CME 1.0 Cisco SRST 1.0

This
                                          						command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						IAD2420 series.

12.2(2)XT

Cisco
                                          						CME 2.0 Cisco SRST 2.0

This
                                          						command was implemented on the Cisco 1750 and Cisco 1751.

12.2(8)T

Cisco
                                          						CME 2.0 Cisco SRST 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725 and Cisco 3745.

12.2(8)T1

Cisco
                                          						CME 2.0 Cisco SRST 2.0

This
                                          						command was implemented on the Cisco 2600XM and Cisco 2691.

12.2(11)T

Cisco
                                          						CME 2.01 Cisco SRST 2.01

This
                                          						command was implemented on the Cisco 1760.

## Examples

The following is
                              		  example output from the show ephone-dn summary command:

```
Router# show ephone-dn summary PORT     DN STATE    CODEC    VAD VTSP STATE            VPM STATE
======== ==========  ======== === ===================== =========
50/0/1   DOWN        -         -  -                     EFXS_ONHOOK             
 
50/0/2   DOWN        -         -  -                     EFXS_ONHOOK             
 
50/0/3   DOWN        -         -  -                     EFXS_ONHOOK             
 
50/0/4   INVALID     -         -  -                     EFXS_INIT               
 
50/0/5   INVALID     -         -  -                     EFXS_INIT               
 
50/0/6   INVALID     -         -  -                     EFXS_INIT
```

Table 1 describes significant fields in the output from this command.

Field

Description

CODEC

Type of
                                          					 codec.

DN STATE

Status of
                                          					 the ephone-dn.

EFXS

Voice
                                          					 port type.

PORT

Port
                                          					 number (virtual) for this interface. The number that follows the last slash in
                                          					 the port number is the ephone-dn tag. For example, if the port number is
                                          					 50/0/1, the dn-tag is 1.

VAD

Voice
                                          					 activity detection status.

VPM
                                          					 STATE

State
                                          					 indication for the voice port module (VPM) software component.

VTSP
                                          					 STATE

State
                                          					 indication for the voice telephony service provider (VTSP) software component.

### Related Commands

Command

Description

show ephone-dn

Displays status and information for a Cisco IP phone destination number or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment.

## show sip-ua status
                        	 registrar

To display all
                              		  the SIP endpoints that are currently registered with the contact address, use
                              		  the show sip-ua status registrar command in privileged EXEC mode.

show sip-ua status registrar

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						SIP SRST 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						SIP SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

15.0(1)XA

Cisco
                                          						SIP SRST 8.0

This
                                          						command was updated to display the signaling transport protocol.

## Examples

The following is
                              		  a sample output from this command:

```
Router# show sip-ua status registrar Line          destination      expires(sec)  contact
transport     call-id
              peer
============  ===============  ============  ===============
3029991       10.2.30.108      388           10.2.30.108 
TLS           00120014-4ae40064-f1a3e9fe-8d301072@10.2.30.1 
            40004
3029993       10.2.30.103      382           10.2.30.103          
TCP           001bd433-1c840052-655cd596-4e992eed@10.2.30.1 
              40011
3029982       10.2.30.106       406          10.2.30.106
UDP           001d452c-dbba0056-0481d321-1f3f848d@10.2.30.1               
              40001
```

Table 1 describes the significant fields shown in this output.

Field

Description

call-id

A unique
                                          					 ID assigned for each call.

contact

The
                                          					 contact IP address provided by the Cisco SIP IP phone.

destination

The
                                          					 destination IP address.

expires
                                          					 (sec)

The
                                          					 amount of time, in seconds, until registration expires.

Line

The phone
                                          					 number that maintains registration of SIP devices.

peer

When an
                                          					 SIP IP phone registers, an associated VoIP dial peer is automatically
                                          					 generated. This dial peer contains general information on how to contact the
                                          					 phone. The information includes the directory number or numbers associated with
                                          					 the phone and the IP address and protocol of the phone.

### Related Commands

Command

Description

registrar server

Enables SIP registrar functionality.

## show sip-ua connections tcp tls detail

To display the status, port details, and negotiated ciphers for SIP OAuth.

The Conn-Id that is suffixed with * is the client connections using SIP OAuth port.

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

The command output is updated to display the status, port details, and negotiated ciphers for SIP OAuth.

Cisco IOS XE 16.10.1

The command output for show sip-ua connections tcp tls detail was updated to display the Cipher and the Curve-Size.

## Examples

```
Router#show sip-ua connections tcp tls detail 
Total active connections      : 4
No. of send failures          : 0
No. of remote closures        : 8
No. of conn. failures         : 0
No. of inactive conn. ageouts : 0
TLS client handshake failures : 0
TLS server handshake failures : 0

---------Printing Detailed Connection Report---------
Note:
 ** Tuples with no matching socket entry
    - Do 'clear sip <tcp[tls]/udp> conn t ipv4:<addr>:<port>'
      to overcome this error condition
 ++ Tuples with mismatched address/port entry
    - Do 'clear sip <tcp[tls]/udp> conn t ipv4:<addr>:<port> id <connid>'
      to overcome this error condition
 * Connections with SIP OAuth ports

Remote-Agent:10.5.10.200, Connections-Count:0

Remote-Agent:10.5.10.201, Connections-Count:0

Remote-Agent:10.5.10.202, Connections-Count:0

Remote-Agent:10.5.10.212, Connections-Count:1
  Remote-Port Conn-Id Conn-State  WriteQ-Size Local-Address TLS-Version Cipher                         Curve
  =========== ======= =========== =========== ============= =========== ============================== =====
        52248      27 Established           0            -      TLSv1.2    ECDHE-RSA-AES256-GCM-SHA384 P-256

Remote-Agent:10.5.10.213, Connections-Count:1
  Remote-Port Conn-Id Conn-State  WriteQ-Size Local-Address TLS-Version Cipher                         Curve
  =========== ======= =========== =========== ============= =========== ============================== =====
        50901     28* Established           0            -      TLSv1.2    ECDHE-RSA-AES256-GCM-SHA384 P-256

Remote-Agent:10.5.10.209, Connections-Count:1
  Remote-Port Conn-Id Conn-State  WriteQ-Size Local-Address TLS-Version Cipher                         Curve
  =========== ======= =========== =========== ============= =========== ============================== =====
        51402     29* Established           0            -      TLSv1.2    ECDHE-RSA-AES256-GCM-SHA384 P-256
          
Remote-Agent:10.5.10.204, Connections-Count:1
  Remote-Port Conn-Id Conn-State  WriteQ-Size Local-Address TLS-Version Cipher                         Curve
  =========== ======= =========== =========== ============= =========== ============================== =====
        50757     30* Established           0            -      TLSv1.2    ECDHE-RSA-AES256-GCM-SHA384 P-256
          
Remote-Agent:10.5.10.218, Connections-Count:0
          
          
-------------- SIP Transport Layer Listen Sockets ---------------
  Conn-Id               Local-Address             
 ===========    ============================= 
   0            [0.0.0.0]:5061:
   2            [0.0.0.0]:5090:
```

## show voice emergency

To display the IP address, subnet mask, and ELIN for each emergency
                              		  response location, use the show voice emergency command in user EXEC or privileged EXEC mode.

show voice emergency

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command displays the IP address, subnet mask, and ELIN for each
                              		  emergency response location.

## Examples

The following example shows a sample output which includes IP mask
                              		  and ELIN information for each ERL:

```
EEMERGENCY RESPONSE LOCATIONS
ERL               | ELIN 1     | ELIN2      | SUBNET 1        | SUBNET 2       
1                 | 6045550101 |            | 10.0.0.0        | 255.0.0.0 
2                 | 6045550102 | 6045550106 | 192.168.0.0     | 255.255.0.0 
3                 |            | 6045550107 | 172.16.0.0      | 255.255.0.0 
4                 | 6045550103 |            | 192.168.0.0     | 255.255.0.0 
5                 | 6045550105 |            | 209.165.200.224 | 255.0.0.0 
6 6045550198      |            | 6045550109 | 209.165.201.0   | 255.255.255.224
```

### Related Commands

Command

Description

voice emergency response location

Creates a tag for identifying an ERL for E911 services.

## show voice emergency addresses

To display address information for each emergency response location,
                              		  use the show emergency addresses command in user EXEC or privileged EXEC mode.

show voice emergency addresses

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command displays the physical address of each emergency response
                              		  location.

## Examples

The following example shows a sample output which includes physical
                              		  address information for the ERL:

```
Router# show voice emergency addresses 3850 Zanker Rd, San Jose,604,5550101
225 W Tasman Dr, San Jose,604,5550102
275 W Tasman Dr, San Jose,604,5550103
518 Bellew Dr,Milpitas,604,5550104
400 Tasman Dr,San Jose,604,5550105
    3675 Cisco Way,San Jose,604,5550106
```

### Related Commands

Command

Description

address

Specifies a comma separated text entry (up to 250
                                          						characters) of an ERL’s civic address.

show voice emergency all

Displays all emergency response location information.

voice emergency response location

Creates a tag for identifying an ERL for E911 services.

## show voice emergency all

To display all emergency response location information, use the show voice emergency all command in user EXEC or privileged EXEC mode.

show voice emergency all

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command displays all information configured for each emergency
                              		  response location.

## Examples

The following example shows a sample output, displaying all
                              		  ERL-related information for ERL 1 and 3.

```
VOICE EMERGENCY RESPONSE SETTINGS
   Callback Number: 6045550103
   Emergency Line ID Number: 6045550155
   Expiry: 2 minutes
   Logging Enabled
EMERGENCY RESPONSE LOCATION 1
   Name: Cisco Systems 1
   Address: 3850 Zanker Rd, San Jose,elin.1.3,elin.4.10 
   IP Address 1: 209.165.200.226 IP mask 1: 255.255.255.254
   IP Address 2: 209.165.202.129 IP mask 2: 255.255.0.0
   Emergency Line ID 1: 6045550180
   Emergency Line ID 2: 
   Last Caller:  6045550188 [Jan 30 2007 16:05.52 PM]
   Next ELIN For Emergency Call: 6045550166
EMERGENCY RESPONSE LOCATION 3
   Name: Cisco Systems 3
   Address: 225 W Tasman Dr, San Jose,elin.1.3,elin.4.10 
   IP Address 1: 209.165.202.133 IP mask 1: 255.255.0.0
   IP Address 2: 209.165.202.130 IP mask 2: 255.0.0.0
   Emergency Line ID 1: 
   Emergency Line ID 2: 6045550150
   Last Caller:  
   Next ELIN For Emergency Call: 6045550151
```

### Related Commands

Command

Description

address

Specifies a comma separated text entry (up to 250
                                          						characters) of an ERL’s civic address.

elin

Specifies a PSTN number that will replace the caller’s
                                          						extension.

name

Specifies a string (up to 32-characters) used internally to
                                          						identify or describe the emergency response location.

subnet

Defines which IP phones are part of this ERL.

voice emergency response location

Creates a tag for identifying an ERL for the E911 services.

## show voice emergency callers

To display a list of 911 calls made over the last three hours, use
                              		  the show emergency callers command in privileged EXEC mode.

show voice emergency callers

### Syntax Description

This command has no arguments or keywords.

### Command Default

No list of 911 calls is displayed.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)T

Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1

This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only.

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was added to Cisco Unified CME.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command displays a list of all 911 calls made in the past three
                              		  hours. The list shows the originating number, the ELIN used, and the time the
                              		  call was placed.

## Examples

The following example shows a sample output, which includes the
                              		  originating number, the ELIN used, and the time the call was placed:

```
router# show voice emergency callers EMERGENCY CALLS CALL BACK TABLE
ELIN                      | CALLER                     | TIME                
6045550181                | 8155550151                | Oct 12 2006 04:05:21
6045550182                | 8155550152                | Oct 12 2006 04:05:21
```

### Related Commands

Command

Description

voice emergency response location

Creates a tag for identifying an ERL for the enhanced 911
                                          						service.

## show voice emergency zone

To display each emergency response zone’s list of locations in the
                              		  order of priority, use the show voice emergency zone command in user EXEC or privileged EXEC mode.

show voice emergency zone

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command displays a list of the locations, in priority order, of
                              		  all configured emergency response zones.

## Examples

The following example shows a sample output which displays the ERL
                              		  locations for emergency response zones 90 and 100.

```
EMERGENCY RESPONSE ZONES
 zone 90
    location 4
    location 5
    location 6
    location 7
    location 2147483647
 zone 100
    location 1 priority 1
    location 2 priority 2
    location 3 priority 3
```

### Related Commands

Command

Description

location

Identifies locations within an emergency response zone.

voice emergency response location

Creates a tag for identifying an ERL for the enhanced 911
                                          						service.

voice emergency response zone

Creates an emergency response zone within which ERLs can be
                                          						grouped.

## show voice moh-group

To display information about voice moh-groups, use the show voice moh-group command in in privileged EXEC mode.

show voice moh-group

### Syntax Description

This command has no arguments or keywords

### Command Modes

Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

## Examples

The following sample output shows general information about voice
                              		  moh-groups in Cisco Unifiede CME or Cisco Unified SRST.

```
Router# show voice moh-group 
voice moh-group 1
 description this moh group is for sales
 moh hello.au
 multicast moh 239.1.1.1 port 16386 route 239.1.1.3 239.1.1.3
 extension-range 1000 to 1999
 extension-range 2000 to 2999
 extension-range 3000 to 3999
extension-range 20000 to 22000
 extension-range A1000 to A1999
voice moh-group 2
 description (not configured)
 moh minuet.au
 multicast moh 239.23.4.10 port 2000
 extension-range 7000 to 7999
 extension-range 8000 to 8999
voice moh-group 3
 description This is for marketing
 moh happy.au
 multicast moh 239.15.10.1 port 3000
 extension-range 9000 to 9999
voice moh-group 4
 description (not configured)
moh sun.au
 multicast moh 239.16.12.1 port 4000
 extension-range 10000 to 19999
voice moh-group 5
 description (not configured)
 moh flower.wav
 multicast moh 239.12.1.2 port 5000
 extension-range ABCD to DECF
 extension-range 0012 to 0024
 extension-range 0934 to 0964
=== Total of 5 voice moh-groups ===
e
```

## Examples

Command

Description

showcall-manager-fallback all

Displays the detailed configuration of all Cisco IP phones, directory numbers, voice ports, and dial peers in your network during Cisco Unified Communications Manager fallback.

show ephone summary

Displays the information about the MOH files in use

show voice moh-group statistics

Displays the MOH subsystem statistics information

## show voice moh-group statistics

To display the MOH subsystem statistics information, use the show voice moh-group command in privileged EXEC mode.

show voice moh-group statistics

### Syntax Description

This command has no arguments or keywords

### Command Modes

Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

## Examples

In the following example, the MOH Group Streaming Interval Timing
                              		  Statistics shows the media packet counts during streaming intervals.

Each packet counter is of 32 bit size and holds a count limit of
                              		  4294967296 intervals. This means that with 20 milliseconds packet interval (for
                              		  G.711), the counters restart from 0 any time after 2.72 years (2 years 8
                              		  months). You must use the e clear voice moh-group statistics once in every two
                              		  years to reset the packet counters.

MOH Group Packet Transmission Timing Statistics shows the maximum and
                              		  minimum amount of time (in microseconds) taken by the MOH groups to send out
                              		  media packets.

The MOH Group Loopback Interval Timing Statistics is available when
                              		  loopback interface is configured as part of the multicast MOH routes in Cisco
                              		  Unified SRST . These counts are loopback packet counts within certain streaming
                              		  timing intervals.

```
router# show voice moh-group statistics 
MOH Group Streaming Interval Timing Statistics:
Grp#  ~19 msec     20~39      40~59      60~99     100~199   200+ msec
==== ========== ========== ========== ========== ========== ==========
 0:       25835   17559966      45148          0          0          1
 1:       19766   17572103      39079          0          0          1
 2:       32374   17546886      51687          0          0          1
 3:       27976   17555681      47289          0          0          1
 4:       34346   17542940      53659          0          0          1
 5:       14971   17581689      34284          0          0          1
MOH Group Packet Transmission Timing Statistics:
Grp#  max(usec)  min(usec) 
==== ========== ========== 
 0:          97          7.
 1:          95          7.
 2:          97          7.
 3:          96          7.
 4:          94          7.
 5:          67          7.
 MOH Group Loopback Interval Timing Statistics:
 loopback event array: svc_index=1542, free_index=1549, max_q_depth=31
 Grp#  ~19 msec     20~39      40~59      60~99     100~199   200+ msec
 ==== ========== ========== ========== ========== ========== ==========
 0:     8918821    8721527      10023          0          1          1
 1:     9007373    8635813       7184          0          1          1
 2:     8864760    8772851      12758          0          1          1
 3:     8924447    8715457      10464          0          1          1
 4:     8858393    8778957      13017          0          1          1
 5:     9005511    8639936       4919          0          1          1
Statistics collect time: 4 days 2 hours 5 minutes 39 seconds.
```

### Related Commands

Command

Description

show ephone-dn

Displays MOH group information for a phone directory
                                          						number.

show ephone summary

Displays the information about the MOH files in use

show voice moh-group

Displays the MOH groups configured

## show voice
                        	 register all

To display all
                              		  Cisco Unified Session Initiation Protocol (SIP) Survivable Remote Site
                              		  Telephony (SRST) or Cisco Unified Communications Manager Express (Cisco Unified
                              		  CME) configurations and register information, use the show voice register all command in privileged EXEC mode.

show voice register all

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						SIP SRST 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						SIP SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

12.4(4)T

Cisco
                                          						CME 3.4 and Cisco SIP SRST 3.4

This
                                          						command was added to Cisco CME.

15.0(1)XA

Cisco
                                          						SIP SRST 8.0

This
                                          						command was updated to display the signaling transport protocol.

15.1(2)T

Cisco
                                          						Unified CME 8.1 Cisco Unified SIP SRST 8.1

This
                                          						command was modified. The output display was modified.

## Examples

## Examples

The following is
                              		  an example of show voice register all command:

```
Router# show voice register all VOICE REGISTER GLOBAL
=====================
CONFIG [Version=8.1]
========================
  Version 8.1
  Mode is srst
  Max-pool is 10
  Max-dn is 10
  Outbound-proxy is enabled and will use global configured value
  Security Policy: DEVICE-DEFAULT
  timeout interdigit 10
  network-locale[0] US    (This is the default network locale for this box)
  network-locale[1] US 
  network-locale[2] US 
  network-locale[3] US 
  network-locale[4] US 
  user-locale[0] US    (This is the default user locale for this box)
  user-locale[1] US 
  user-locale[2] US 
  user-locale[3] US 
  user-locale[4] US   Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
VOICE REGISTER DN
=================
Dn Tag 1
Config:
  Number is 45111
  Preference is 0
  Huntstop is disabled
  Pool 1    has this DN configured for line 1
Dn Tag 2
Config:
  Number is 45112
  Preference is 0
  Huntstop is disabled
  Pool 2    has this DN configured for line 1
Dn Tag 3
Config:
  Number is 45113
  Preference is 0
  Huntstop is disabled
  Pool 3    has this DN configured for line 1, 2
Dn Tag 4
Config:
Dn Tag 7
Config:
  Number is 451110
  Preference is 0
  Huntstop is disabled
  Pool 1    has this DN configured for line 4
Dn Tag 8
Config:   
  Pool 1    has this DN configured for line 3
VOICE REGISTER POOL
===================
 Pool Tag 1
Config:
  Mac address is 001B.535C.D410
  Number list 1 : DN 1
  Number list 3 : DN 8
  Number list 4 : DN 7
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  kpml signal is disabled
  Lpcor Type is none
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
 Pool Tag 2
Config:
  Mac address is 0015.C68E.6D13
  Number list 1 : DN 2
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  kpml signal is disabled
  Lpcor Type is none
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
 Pool Tag 3
Config:
  Mac address is 0021.5553.8998
  Number list 1 : DN 3
  Number list 2 : DN 3
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  kpml signal is enabled
  Lpcor Type is none
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      :
```

## Examples

The following is
                              		  an example of show voice register all command :

```
Router# show voice register all 1) show voice register all
VOICE REGISTER GLOBAL
=====================
CONFIG [Version=8.1]
========================
  Version 8.1
  Mode is cme
  Max-pool is 10
  Max-dn is 10
  Outbound-proxy is enabled and will use global configured value
  Security Policy: DEVICE-DEFAULT
  Source-address is 8.3.3.5 port 5060
  Time-format is 12
  Date-format is M/D/Y
  Time-zone is 5
  Hold-alert is disabled
  Mwi stutter is disabled
  Mwi registration for full E.164 is disabled
  Forwarding local is enabled
  Privacy is enabled
  Privacy-on-hold is disabled
  Dst auto adjust is enabled
    start at Apr week 1 day Sun time 02:00
    stop  at Oct week 8 day Sun time 02:00
  Max redirect number is 5
  IP QoS DSCP:
    ef (the MS 6 bits, 46, in ToS, 0xB8) for media
    cs3 (the MS 6 bits, 24, in ToS, 0x60) for signal
    af41 (the MS 6 bits, 34, in ToS, 0x88) for video
    default (the MS 6 bits, 0, in ToS, 0x0) for service
  Telnet Level: 0
  Tftp path is flash:
  Generate text file is disabled
  Tftp files are created, current syncinfo 0001140473454008
  OS79XX.TXT is not created
  timeout interdigit 10
  network-locale[0] US    (This is the default network locale for this box)
  network-locale[1] US 
  network-locale[2] US 
  network-locale[3] US 
  network-locale[4] US 
  user-locale[0] US    (This is the default user locale for this box)
  user-locale[1] US 
  user-locale[2] US 
  user-locale[3] US 
  user-locale[4] US   Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
VOICE REGISTER DN
=================
Dn Tag 1
Config:
  Number is 45111
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  Pool 1    has this DN configured for line 1
Dn Tag 2
Config:
  Number is 45112
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  call-forward b2bua noan 999 timeout 8
  after-hour exempt
  Pool 2    has this DN configured for line 1
  Pool 7    has this DN configured for line 1
Dn Tag 3
Config:
  Number is 45113
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  call-forward b2bua all 87687
  Pool 3    has this DN configured for line 1, 2
Dn Tag 4
Config:
  Auto answer is disabled
Dn Tag 7
Config:
  Number is 451110
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  after-hour exempt
  Pool 1    has this DN configured for line 4
Dn Tag 8
Config:
  Auto answer is disabled
  call-forward b2bua all 678
  after-hour exempt
  Pool 1    has this DN configured for line 3
VOICE REGISTER TEMPLATE
=======================
Temp Tag 1
Config:
  Attended Transfer is enabled
  Blind Transfer is enabled
  Semi-attended Transfer is enabled
  Conference is enabled
  Caller-ID block is disabled
  DnD control is enabled
  Anonymous call block is disabled
  Dialplan Tag is 1
  softkey connected  Confrn
  Lpcor type none
  Pool 4 has this template configured
VOICE REGISTER DIALPLAN
=======================
Dialplan Tag 1
Config:
  Type is 7905-7912
  Template 1 has this dialplan configured
  Pool 4 has this dialplan configured
VOICE REGISTER POOL
===================
 Pool Tag 1
Config:
  Mac address is 001B.535C.D410
  Type is 7960
  Number list 1 : DN 1
  Number list 3 : DN 8
  Number list 4 : DN 7
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  Busy trigger per button value is 0
  call-forward phone all is 4566
  call-forward b2bua all 4555
  keep-conference is enabled
  Lpcor Type is none
  Transport type is udp
  service-control mechanism is not supported
  Privacy feature is not configured.
  Privacy button is disabled
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
 Pool Tag 2
Config:
  Mac address is 0015.C68E.6D13
  Type is 7960
  Number list 1 : DN 2
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  Busy trigger per button value is 0
  call-forward phone noan is 9886, timeout 98
  keep-conference is enabled
  username pool2 password lab
  Lpcor Type is none
  Transport type is udp
  service-control mechanism is not supported
  Privacy feature is not configured.
  Privacy button is disabled
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
          
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
 Pool Tag 3
Config:
  Mac address is 0021.5553.8998
  Type is 7975
  Number list 1 : DN 3
  Number list 2 : DN 3
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is enabled
  Busy trigger per button value is 0
  call-forward phone all is 45112
  call-forward b2bua all 45111
  after-hour exempt
  keep-conference is enabled
  kpml signal is enabled
  Lpcor Type is none
  Transport type is udp
  service-control mechanism is not supported
  Privacy feature is not configured.
  Privacy button is disabled
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
 Pool Tag 4
Config:
  Mac address is 8989.9867.8769
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  Busy trigger per button value is 0
  keep-conference is enabled
  template is 1
  Lpcor Type is none
  Transport type is udp
  service-control mechanism is not supported
  Privacy feature is not configured.
  Privacy button is disabled
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      : 
 Pool Tag 7
Config:
  Mac address is 0018.BAC8.D2B1
  Number list 1 : DN 2
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  Busy trigger per button value is 0
  keep-conference is enabled
  Lpcor Type is none
  Transport type is udp
  service-control mechanism is not supported
  Privacy feature is not configured.
  Privacy button is disabled
  Reason for unregistered state: 
         No registration request since last reboot/unregister
Dialpeers created:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      :
```

Table 1 describes the significant fields shown in this output.

Field

Description

Pool Tag

Used with
                                          					 the all and pool keywords. Shows the assigned tag number of the current
                                          					 pool.

Config

Used with
                                          					 the all and pool keywords. Shows the voice register pool.

Network
                                          					 address and Mask

Used
                                          					 with the all and pool keywords. Shows network address and mask information if
                                          					 the id command is configured.

Number
                                          					 list, Pattern, and Preference

Used
                                          					 with the all and pool keywords. Shows the number command configuration.

Proxy
                                          					 IP address

Used
                                          					 with the all and pool keywords. Shows the proxy command configuration.

Default
                                          					 preference

Used
                                          					 with the all and pool keywords. Shows the default preference value of this
                                          					 pool.

Incoming called number

Used
                                          					 with the all and pool keywords. Shows the incoming called-number command configuration.

Translate outgoing called tag

Used
                                          					 with the all and pool keywords. Shows the translate-outgoing command configuration.

Class
                                          					 of Restriction List Tag

Used
                                          					 with the all and pool keywords. Shows the COR tag.

Incoming corlist name

Used
                                          					 with the all and pool keywords. Shows the cor command
                                          					 configuration.

Application

Used
                                          					 with the all and pool keywords. Shows the application command configuration for this pool.

Dialpeers created:

Used
                                          					 with the all and pool keywords. What follows is a list of all dial peers
                                          					 created and their contents. Dial-peer contents differ per application and are
                                          					 not described here.

Statistics

Used
                                          					 with the all , pool , and statistics keywords. Shows the registration statistics for this pool.

Active
                                          					 registrations

Used
                                          					 with the all , pool , and statistics keywords. Shows the current active registrations.

Total
                                          					 Registration Statistics

Used
                                          					 with the all , pool , and statistics keywords. Shows the total registration statistics for this pool.

Registration requests

Used
                                          					 with the all , pool , and statistics keywords. Shows the incoming registration requests.

Registration success

Used
                                          					 with the all , pool , and statistics keywords. Shows the successful registrations.

Registration failed

Used
                                          					 with the all , pool , and statistics keywords. Shows the failed registrations.

unRegister requests

Used
                                          					 with the all , pool , and statistics keywords. Shows the incoming unregister/registration expire requests.

unRegister success

Used
                                          					 with the all , pool , and statistics keywords. Reports the number of successful unregisters.

unRegister failed

Used
                                          					 with the all , pool , and statistics keywords. Reports the number of failed unregisters.

### Related Commands

Command

Description

show sip-ua status registrar

Displays all the SIP endpoints currently registered with the contact address.

show voice register dial-peers

Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified SIP SRST or Cisco Unified CME register event

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

## show voice register dial-peers

To display details of all dynamically created VoIP dial peers
                              		  associated with the Cisco Unified Session Initiation Protocol (SIP) Survivable
                              		  Remote Site Telephony (SRST) or Cisco Unified CallManager Express (Cisco
                              		  Unified CME) register event, use the show voice register dial-peers command in privileged EXEC mode.

show voice register dial-peers [ pool tag ]

### Syntax Description

pool tag

Number of entries in attempted registrations table. Size
                                          						range from 0 to 50.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SIP SRST 3.0

This command was introduced.

12.3(4)T

Cisco SIP SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was added to Cisco CME.

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SIP SRST 8.1

This command was modified. Pool tag keyword- argument was
                                          						added. Command output display was also modified to display dial-peers specific
                                          						to a pool.

### Usage Guidelines

Use this command to display the dial-peers associated with a pool. To
                              		  display the dynamic dial-peers associated with a specific pool, use the pool
                              		  keyword followed by the pool tag. When using the pool keyword, you must specify
                              		  the pool tag.

## Examples

## Examples

The following is a sample output from this command displaying all
                              		  dial-peers:

```
Router#show voice register dial-peers
Dial-peers for Pool 1
dial-peer voice 40001 voip
 destination-pattern 45111
 session target ipv4:8.3.3.111:5060
 session protocol sipv2
 call-fwd-all         4555           
 after-hours-exempt   FALSE          
dial-peer voice 40002 voip
  destination-pattern 45113
  session target ipv4:8.33.33.111:5060
  session protocol sipv2
  after-hours-exempt   FALSE   
Dial-peers for Pool 2
 dial-peer voice 40003 voip
 destination-pattern 45112
 session target ipv4:8.33.33.112:5060
 session protocol sipv2
 call-fwd-noan-timeou 8              
 call-fwd-noan        999            
 after-hours-exempt   TRUE
```

## Examples

The following is a sample output from this command displaying all
                              		  statistical information related to pool 1:

```
Router# show voice register dial-peers pool 1 Dial-peers for Pool 1:
dial-peer voice 40004 voip
 destination-pattern 1000
 redirect ip2ip
 session target ipv4:9.13.18.40:19633
 session protocol sipv2
 dtmf-relay rtp-nte sip-notify
 digit collect kpml
 codec  g711ulaw bytes 160
  after-hours-exempt   FALSE          
dial-peer voice 40001 voip
 destination-pattern 2000
 redirect ip2ip
 session target ipv4:9.13.18.40:19634
 session protocol sipv2
 dtmf-relay rtp-nte sip-notify
 digit collect kpml
 codec  g711ulaw bytes 160
```

## Examples

### Related Commands

Command

Description

show sip-ua status registrar

Displays all the SIP endpoints currently registered with
                                          						the contact address.

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME
                                          						configurations and register information.

show voice register pool

Displays all configuration information associated with a
                                          						particular voice register pool.

## show voice register dn

To display all configuration information associated with a specific
                              		  voice register dn, use the show voice register dn command in privileged EXEC mode.

show voice register dn { tag | all }

### Syntax Description

tag

Tag number of the voice register dn for which to display
                                          						information. Range is 1 to 750.

all

(Optional) Displays configuration information associated
                                          						with all voice register dns defined in a system.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Version

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

15.1(2)T

Cisco CME 8.1 Cisco SIP SRST 8.1

This command was modified.The display output now shows
                                          						pools that have DNs configured under them. All keyword was added to show
                                          						configuration information for all voice register dns defined in system.

### Usage Guidelines

In Cisco Unified CME 8.1 and Cisco Unified SIP SRST 8.1, the show
                              		  voice register dn command displays the pools that have the DNs configured under
                              		  them. When used with all keyword, the show voice register dn command displays
                              		  configuration information for all the DNs defined in a system.

## Examples

## Examples

The following is a sample output from this command:

```
Router# show voice register dn 1
Dn Tag 1
Config:
  Number is 11
  Preference is 10
  Huntstop is enabled
  Translation-profile incoming saaa
  Allow watch is enabled
  Pool 1    has this DN configured for line 1
```

## Examples

The following is a sample output from this command:

```
Router# show voice register dn 2 Dn Tag 1
Config:
  Number is 11
  Preference is 10
  Huntstop is enabled
  Translation-profile incoming saaa
  Allow watch is enabled
  Pool 1    has this DN configured for line 1
```

## Examples

The following is a sample output from this command displaying
                              		  information for all the dns:

```
Dn Tag 1
Config:
  Number is 11
  Preference is 10
  Huntstop is enabled
  Translation-profile incoming saaa
  Allow watch is enabled
  Pool 1    has this DN configured for line 1
Dn Tag 2
Config:
  Number is 12
  Preference is 1
  Huntstop is enabled
  Allow watch is enabled
  Pool 2    has this DN configured for line 1, 2
```

## Examples

The following is a sample output from this command displaying
                              		  information for all the dns:

```
Router# show voice register dn all Dn Tag 1
Config:
  Number is 45111
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
Dn Tag 2
Config:
  Number is 45112
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  call-forward b2bua noan 999 timeout 8
  after-hour exempt
  Pool 2    has this DN configured for line 1
  Pool 7    has this DN configured for line 1
Dn Tag 3
Config:
  Number is 45113
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  call-forward b2bua all 87687  
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  call-forward b2bua all 87687
  Pool 1    has this DN configured for line 1
  Pool 3    has this DN configured for line 1, 2
Dn Tag 4
Config:
  Auto answer is disabled
Dn Tag 7
Config:
  Number is 451110
  Preference is 0
  Huntstop is disabled
  Auto answer is disabled
  after-hour exempt
  Pool 1    has this DN configured for line 4
Dn Tag 8
Config:
  Auto answer is disabled
  call-forward b2bua all 678
  after-hour exempt
  Pool 1    has this DN configured for line 3
```

contains descriptions of significant fields shown in this
                              		  output, listed in alphabetical order.

Field

Description

Auto answer

Status of auto-answer feature defined with the auto-answer command.

Config

List of configuration options defined for this voice register
                                          					 dn.

Dn Tag

Tag number of the requested voice register dn.

Huntstop

Status of huntstop behavior defined with the huntstop command.

Number

Telephone or extension number set with the number command in voice register dn
                                          					 configuration mode.

Preference

Preference order set with the preference command in voice register dn configuration mode.

### Related Commands

Command

Description

show voice register pool

Displays all configuration information associated with a
                                          						particular voice register pool.

show voice register dn all

Displays information associated with all the dns configured
                                          						in a system.

voice register dn

Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line.

## show voice
                        	 register global

To display all
                              		  global configuration parameters associated with SIP phones, use the show voice register global command in privileged EXEC mode.

show voice register global

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

Privileged EXEC

## Command History

Cisco IOS Release

Cisco
                                          						Product

Modification

12.4(4)T

Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4

This
                                          						command was introduced.

15.0(1)XA

Cisco
                                          						SIP SRST 8.0

This
                                          						command was updated to display the signaling transport protocol.

15.1(2)T

Cisco
                                          						Unified CME 8.1 Cisco Unified SIP SRST 8.1

This
                                          						command was modified.The output display now includes global statistics.

Cisco IOS XE Amsterdam 17.2.1r

Unified SRST 12.8

This command was modified to display VRF information for Cisco 4000 Series Integrated Services Routers.

## Examples

The following is
                              		  sample output from this command:

```
Router# show voice register global CONFIG [Version=8.1]
========================
  Version 8.1
  Mode is cme
  Max-pool is 10
  Max-dn is 10
  Outbound-proxy is enabled and will use global configured value
  Security Policy: DEVICE-DEFAULT
  Source-address is 8.3.3.5 port 5060
  Time-format is 12
  Date-format is M/D/Y
  Time-zone is 5
  Hold-alert is disabled
  Mwi stutter is disabled
  Mwi registration for full E.164 is disabled
  Forwarding local is enabled
  Privacy is enabled
  Privacy-on-hold is disabled
  Dst auto adjust is enabled
    start at Apr week 1 day Sun time 02:00
    stop  at Oct week 8 day Sun time 02:00
  Max redirect number is 5
  IP QoS DSCP:
    ef (the MS 6 bits, 46, in ToS, 0xB8) for media
    cs3 (the MS 6 bits, 24, in ToS, 0x60) for signal
    af41 (the MS 6 bits, 34, in ToS, 0x88) for video
    default (the MS 6 bits, 0, in ToS, 0x0) for service
  Telnet Level: 0
  Tftp path is flash:
  Generate text file is disabled
  Tftp files are created, current syncinfo 0001140473454008
  OS79XX.TXT is not created
  timeout interdigit 10
  network-locale[0] US    (This is the default network locale for this box)
  network-locale[1] US 
  network-locale[2] US 
  network-locale[3] US 
  network-locale[4] US 
  user-locale[0] US    (This is the default user locale for this box)
  user-locale[1] US 
  user-locale[2] US 
  user-locale[3] US 
  user-locale[4] US   Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      :
```

## Examples

```
Router# show voice register global CONFIG [Version=12.8]
========================
  Version 12.8
 Mode is srst
 Max-pool is 50
 Max-dn is 50
 VRF vrf1
 Outbound-proxy is enabled and will use global configured value
 Security Policy: DEVICE-DEFAULT
 Allow-hash-in-dn is disabled
 Forced Authorization Code Refer is enabled
 timeout interdigit 10
 timeout transfer recall 0
 network-locale[0] US  (This is the default network locale for this box)
 network-locale[1] US
 network-locale[2] US
 network-locale[3] US
 network-locale[4] US
 user-locale[0] US  (This is the default user locale for this box)
 user-locale[1] US
 user-locale[2] US
 user-locale[3] US
 user-locale[4] US
 MWI unsolicited notify is disabled
 Active registrations : 0

 Total SIP phones registered: 0
 Total Registration Statistics
  Registration requests : 0
  Registration success  : 0
  Registration failed  : 0
  unRegister requests  : 0
  unRegister success   : 0
  unRegister failed   : 0
  Auto-Register requests : 0
  Attempts to register
     after last unregister : 0
  Last register request time  :
  Last unregister request time :
  Register success time    :
  Unregister success time   :
```

## Examples

```
Router# show voice register global CONFIG [Version=8.1]
========================
  Version 8.1
  Mode is srst
  Max-pool is 10
  Max-dn is 10
  Outbound-proxy is enabled and will use global configured value
  Security Policy: DEVICE-DEFAULT
  timeout interdigit 10
  network-locale[0] US    (This is the default network locale for this box)
  network-locale[1] US 
  network-locale[2] US 
  network-locale[3] US 
  network-locale[4] US 
  user-locale[0] US    (This is the default user locale for this box)
  user-locale[1] US 
  user-locale[2] US 
  user-locale[3] US 
  user-locale[4] US   Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 0
    Registration success   : 0
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : 
    Last unregister request time : 
    Register success time        : 
    Unregister success time      :
```

Table 1 contains
                              		  descriptions of significant fields shown in this output, listed in alphabetical
                              		  order.

Field

Description

Date-format

Value of date-format command.

DST auto
                                          					 adjust

Setting
                                          					 of dst auto-adjust command.

Forwarding local

Setting
                                          					 of forwarding local command.

Generate
                                          					 text file

Setting
                                          					 of text file command.

Hold-alert

Setting
                                          					 of hold-alert command.

Load

Value
                                          					 of load command.

Max-dn

Reports
                                          					 the maximum number of SIP voice register directory numbers (dns) supported by
                                          					 the Cisco Unified SIP CME or Cisco Unified SIP SRST router as configured with
                                          					 the max-dn command. The maximum possible number is
                                          					 platform-dependent.

Max-pool

Reports
                                          					 the maximum number of SIP voice register pools supported by the Cisco Unified
                                          					 SIP SRST or Cisco Unified CME router as configured with the max-pool command. The maximum possible number is platform-dependent.

Max
                                          					 redirect number

Maximum
                                          					 number of redirects set with the max-redirect command.

Mode

Reports
                                          					 the mode as configured with the mode command. Value can be either Cisco Unified CME or Cisco Unified SIP SRST.

MWI
                                          					 registration

Setting
                                          					 of mwi command.

MWI
                                          					 stutter

Setting
                                          					 of mwi stutter command.

Time-format

Value
                                          					 of time-format command.

Time-zone

Number
                                          					 of the timezone selected with the timezone command.

TFTP
                                          					 path

Directory location of provisioning files for SIP phones that is specified with
                                          					 the tftp-path command.

Version

Reports
                                          					 the Cisco Unified SIP SRST or Cisco Unified CME version number.

VRF

Displays information on the associated VRF ID.

### Related Commands

Command

Description

show sip-ua status registrar

Displays all the SIP endpoints currently registered with the contact address.

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register dial-peers

Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified SIP SRST or Cisco Unified CME register event.

voice register global

Enters voice register global configuration mode in order to set global
                                          						parameters for all supported Cisco SIP phones in a Cisco Unified CME or Cisco
                                          						Unified SIP SRST environment.

## show voice
                        	 register pool

To display all
                              		  configuration information associated with a specific voice register pool, use
                              		  the show voice register pool command in privileged EXEC mode.

show voice register pool { pool-tag | all } [ brief ]

### Syntax Description

pool-tag

Tag
                                          						number of the voice register pool for which information is displayed. Range is
                                          						1 to 262.

all

Displays the information of all the voice register pools.

brief

(Optional) Displays brief information of all voice register pools.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						SIP SRST

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						SIP SRST

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

12.4(4)T

Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4

This
                                          						command was added to Cisco CME.

12.4(15)XY

Cisco
                                          						Unified CME 4.2(1) Cisco Unified SIP SRST 4.2(1)

This
                                          						command was modified to include emergency response location information in the
                                          						output display.

12.4(20)T

Cisco
                                          						Unified CME 7.0 Cisco Unified SIP SRST 7.0

This
                                          						command was integrated into Cisco IOS Release 12.4(20)T.

15.0(1)XA

Cisco
                                          						Unified CME 8.0

This
                                          						command was modified to include logical partitioning class of restriction
                                          						(LPCOR) information in the output display.

15.1(1)T

Cisco
                                          						Unified CME 8.0

This
                                          						command was integrated into Cisco IOS Release 15.1(1)T.

15.1(2)T

Cisco
                                          						Unified CME 8.1

This
                                          						command was modified. The all and brief keywords were added. Voice-class stun-usage information is displayed in the
                                          						output.

15.2(2)T

Cisco
                                          						Unified CME 9.0

This
                                          						command was modified to include conference admin, conference add mode, and
                                          						conference drop mode in the output display.

15.2(4)M

Cisco
                                          						Unified CME 9.1 Cisco Unified SIP SRST 9.1

This
                                          						command was modified to include Key Expansion Module (KEM) data in the output
                                          						display.

Cisco IOS XE Everest 16.6.1

Unified SRST 12.0

This command was modified to include the IPv6 address in the
                                          						output display for Unified SRST.

Unified SRST 12.8

This command was modified to include VRF information for Cisco 4000 Series Integrated Services Routers:

show voice register pool all —Information for all the available configured pools.

show voice register pool pool-tag —Information specific to a specific configured pool.

Unified SRST 12.8

Introduced support for YANG models.

## Examples

## Examples

The following
                              		  is a sample output of the show voice register pool command, displaying information for voice
                              		  register pool 33 in Cisco Unified CME:

```
Router# show voice register pool 33 Pool Tag 33
Config:
 Mac address is 0009.B7F7.532E
 Type is 7960
 Number list 1 : DN 1
 Number list 2 : DN 2
 Number list 3 : DN 3
 Proxy Ip address is 0.0.0.0
 DTMF Relay is disabled
 Call Waiting is enabled
 DnD is disabled
 Busy trigger per button value is 0
 keep-conference is enabled
 template is 1
 Emergency response location 3
 Lpcor Type is local 
 Lpcor Incoming is sip_group
 Lpcor Outgoing is sip_group
 
 Transport type is udp 
 service-control mechanism is not supported 
 Privacy feature is not configured. 
 Privacy button is disabled 
 
Dialpeers created: 
 
Statistics: 
 Active registrations : 0 
 
 Total SIP phones registered: 0 
 Total Registration Statistics 
  Registration requests : 0 
  Registration success : 0 
  Registration failed : 0 
  unRegister requests : 0 
  unRegister success : 0 
  unRegister failed : 0
```

The following
                              		  is a sample output of the show voice register pool command. The output shows that a meet-me
                              		  hardware conference administrator has been assigned, the conference creator or
                              		  any of the participants can add a new participant, and the conference creator
                              		  can terminate the active video hardware conference by hanging up.

```
Router# show voice register pool 15 Pool Tag 15
Config:
  Mac address is 1C17.D340.81F0
  Type is 9951
  Number list 1 : DN 15
  Proxy Ip address is 0.0.0.0
  Current Phone load version is Cisco-CP9951/9.0.1
  DTMF Relay is enabled, sip-notify
  Call Waiting is enabled
  DnD is disabled
  Video is enabled
  Camera is enabled
  Busy trigger per button value is 0
  feature-button 5 DnD
  feature-button 6 MeetMe
  keep-conference is enabled
  registration expires timer max is 86400 and min is 60
  template is 1
  kpml signal is enabled
  Lpcor Type is none
  Transport type is udp
  service-control mechanism is supported
  registration Call ID is 1c17d340-81f00002-6c48fe8e-03013c10@1.5.40.105 
  Registration method: per line
  Privacy feature is not configured.
  Privacy button is disabled
  active primary line is: 3915
  contact IP address: 1.5.40.105 port 5060
  Phone SIS Version:  5.0.0
  GW SIS Version:  1.0.0
  conference admin: yes
  conference add mode: all
  conference drop mode: creator
  paging-dn: config 0 [multicast]  effective 0 [multicast]
...
```

The following
                              		  is an example of a partial output of the show voice register pool all command, showing KEM data with the phone type information:

```
Router# show voice register pool all Pool Tag 5
Config:
Mac address is B4A4.E328.4698
Type is 9971 addon 1 CKEM
Number list 1 : DN 2
Number list 2 : DN 3
Proxy Ip address is 0.0.0.0
DTMF Relay is disabled
Call Waiting is enabled
DnD is disabled
Video is enabled
Camera is enabled
Busy trigger per button value is 0
keep-conference is enabled
registration expires timer max is 200 and min is 60
kpml signal is enabled
Lpcor Type is none
```

The following
                              		  is a sample output of the show voice register pool all command, showing the three KEMs configured
                              		  with phone type 9971:

```
Router# show voice register pool all Pool Tag 4
Config:
Mac address is B4A4.E328.4698
Type is 9971 addon 1 CKEM 2 CKEM 3 CKEM
Number list 1 : DN 4
Number list 2 : DN 5
Number list 3 : DN 9
```

## Examples

The following
                              		  is a sample output of the show voice register pool command, displaying all information for voice register pool 1
                              		  in Cisco Unified SIP SRST:

```
Router# show voice register pool 1 Pool Tag 1
Config:
 Network address is 192.168.0.0, Mask is 255.255.0.0
 Number list 1 : Pattern is 50.., Preference is 2
 Proxy Ip address is 0.0.0.0
 Default preference is 2
 Incoming called number is 
 Translate outgoing called tag is 1
 Class of Restriction List Tag: default
 Incoming corlist name is allowall
 Application is default.new
 
Dialpeers created:
 
dial-peer voice 40007 voip
 application default.new
 corlist incoming allowall
 preference 2
 incoming called-number 5001
 destination-pattern 5001
 redirect ip2ip
 session target ipv4:192.168.0.3
 session protocol sipv2
 translate-outgoing called 1
 voice-class codec 1
 
Statistics:
 Active registrations : 2
 
 Total Registration Statistics
  Registration requests : 48
  Registration success : 48
  Registration failed : 0
  unRegister requests : 46
  unRegister success : 46
  unRegister failed : 0
 
Emergency response location 6
```

## Examples

The following is a sample output of the show voice register pool all and show voice register pool pool-tag command for Unified SRST 12.8:

```
Router# show voice register pool all Pool Tag 1
Config:
 Mac address is 9C57.ADF5.C191
 Number list 1 : DN 1
 Proxy Ip address is 0.0.0.0
 DTMF Relay is enabled, rtp-nte
 kpml signal is enabled
 Lpcor Type is none

 Reason for unregistered state:
   No registration request since last reboot/unregister

 paging-dn: config 0 [multicast] effective 0 [multicast]

VRF:
  vrf1
 
Dialpeers created:

Statistics:
 Active registrations : 0

 Total SIP phones registered: 0
 Total Registration Statistics
  Registration requests : 0
  Registration success  : 0
  Registration failed  : 0
  unRegister requests  : 0
  unRegister success   : 0
  unRegister failed   : 0
  Auto-Register requests : 0
  Attempts to register
     after last unregister : 0
  Last register request time  :
  Last unregister request time :
  Register success time    :
  Unregister success time   :

Pool Tag 2
Config:
 Mac address is 9C57.ADF5.C192
 Number list 1 : DN 2
 Proxy Ip address is 0.0.0.0
 DTMF Relay is enabled, rtp-nte
 kpml signal is enabled
 Lpcor Type is none

 Reason for unregistered state:
   No registration request since last reboot/unregister

 paging-dn: config 0 [multicast] effective 0 [multicast]

VRF:
  vrf1
 
Dialpeers created:

Statistics:
 Active registrations : 0

 Total SIP phones registered: 0
 Total Registration Statistics
  Registration requests : 0
  Registration success  : 0
  Registration failed  : 0
  unRegister requests  : 0
  unRegister success   : 0
  unRegister failed   : 0
  Auto-Register requests : 0
  Attempts to register
     after last unregister : 0
  Last register request time  :
  Last unregister request time :
  Register success time    :
  Unregister success time   :
```

```
Router# show voice register pool 1 Pool Tag 1
Config:
 Mac address is 9C57.ADF5.C191
 Number list 1 : DN 1
 Proxy Ip address is 0.0.0.0
 DTMF Relay is enabled, rtp-nte
 kpml signal is enabled
 Lpcor Type is none

 Reason for unregistered state:
   No registration request since last reboot/unregister

 paging-dn: config 0 [multicast] effective 0 [multicast]

VRF:
  vrf1
 
Dialpeers created:

Statistics:
 Active registrations : 0

 Total SIP phones registered: 0
 Total Registration Statistics
  Registration requests : 0
  Registration success  : 0
  Registration failed  : 0
  unRegister requests  : 0
  unRegister success   : 0
  unRegister failed   : 0
  Auto-Register requests : 0
  Attempts to register
     after last unregister : 0
  Last register request time  :
  Last unregister request time :
  Register success time    :
  Unregister success time   :
```

## Examples

The following is a sample output of the show voice register pool brief command, showing an IPv6 source address
                              		  configured on a Cisco SIP IP Phone:

```
Router# show voice register pool brief Pool ID                        IP Address                 Ln DN  Number     State
==== ========================  ========================== == === ========== ============
1    8.0.0.0                                                                UNREGISTERED
2    2001:420:54FF:13::312:0   2001:420:54FF:13::312:1           10001$     REGISTERED
```

## Examples

The following
                              		  is a sample output of the show voice register pool command, displaying voice-class stun-usage information for
                              		  voice register pool 51:

```
Router# show voice register pool 51 Pool Tag 51
Config:
  Mac address is 0011.209F.5D60
  Type is 7960
  Number list 1 : DN 51
  Proxy Ip address is 0.0.0.0
  Current Phone load version is Cisco-SIPGateway/IOS-12.x
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  Busy trigger per button value is 0
  keep-conference is enabled
  template is 10
  Lpcor Type is none
  
Transport type is udp
  service-control mechanism is not supported
  registration Call ID is 2BA38EE3-17D311DB-800BCD81-A9AD11F0
  Privacy feature is not configured.
  Privacy button is disabled
  active primary line is: 16263646
  contact IP address: 192.168.0.87 port 5060
  Reason for unregistered state:
         No registration request since last reboot/unregister
  voice-class stun-usage is enabled. tag is 1
Dialpeers created:
Dial-peers for Pool 51:
Statistics:
  Active registrations  : 0
  Total SIP phones registered: 0
  Total Registration Statistics
    Registration requests  : 2
    Registration success   : 2
    Registration failed    : 0
    unRegister requests    : 2
    unRegister success     : 2
    unRegister failed      : 0
    Attempts to register
           after last unregister : 0
    Last register request time   : 13:43:27.839 IST Tue Apr 20 2010
```

Table 1 contains descriptions of significant fields shown in the Cisco Unified CME and
                              		  Cisco Unified SIP SRST output, listed in alphabetical order.

Field

Description

Active
                                          					 registrations

Shows
                                          					 the current active registrations.

Application

Shows
                                          					 the application command configuration for this pool.

Call
                                          					 Waiting

Shows
                                          					 the call-waiting command configuration.

Class
                                          					 of Restriction List Tag

Shows
                                          					 the COR tag.

Conference add mode

Shows
                                          					 the current setting of the hardware conference privilege for adding
                                          					 participants.

Conference admin

Shows
                                          					 whether the Cisco Unified SIP IP phone is assigned as the hardware conference
                                          					 administrator or not.

Conference drop mode

Shows
                                          					 who can terminate an active ad-hoc hardware conference by hanging up.

Config

Shows
                                          					 the voice register pool.

Default
                                          					 preference

Shows
                                          					 the default preference value of this pool.

Dialpeers created

Lists
                                          					 all the dial peers created and their contents. Dial-peer contents differ for
                                          					 each application and are not described here.

DnD

Shows
                                          					 the setting of the dnd-control command.

DTMF
                                          					 Relay

Shows
                                          					 the setting of the dtmf-relay command.

Emergency response location

Shows
                                          					 the ephone’s emergency response location to which an emergency response team is
                                          					 dispatched when an emergency call is made.

Incoming called number

Shows
                                          					 the incoming called-number command configuration.

Incoming corlist name

Shows
                                          					 the cor command
                                          					 configuration.

keep-conference

Shows
                                          					 the status of the keep-conference command.

Lpcor
                                          					 Incoming

Shows
                                          					 the setting of the lpcor incoming command.

Lpcor
                                          					 Outgoing

Shows
                                          					 the setting of the lpcor outgoing command.

Lpcor
                                          					 Type

Shows
                                          					 the setting of the lpcor type command.

Mac
                                          					 address

Shows
                                          					 the MAC address of the Cisco Unified SIP IP phone as defined by the id command.

Network
                                          					 address and Mask

Shows
                                          					 network address and mask information when the id command is configured.

Number
                                          					 list, Pattern, and Preference

Shows
                                          					 the number command configuration.

Pool
                                          					 Tag

Shows
                                          					 the assigned tag number of the current pool.

Proxy
                                          					 IP address

Shows
                                          					 the proxy command configuration; that is, the IP address of the external SIP server.

Registration failed

Shows
                                          					 the failed registrations.

Registration requests

Shows
                                          					 the incoming registration requests.

Registration success

Shows
                                          					 the successful registrations.

Statistics

Shows
                                          					 the registration statistics for this pool.

Template

Shows
                                          					 the template-tag number for the template applied to the Cisco Unified SIP IP
                                          					 phone.

Total
                                          					 Registration Statistics

Shows
                                          					 the total registration statistics for this pool.

Translate outgoing called tag

Shows
                                          					 the translate-outgoing command configuration.

Type

Shows
                                          					 the phone type identified for the Cisco Unified SIP IP phone using the type command.

unRegister failed

Reports
                                          					 the number of failed unregisters.

unRegister requests

Shows
                                          					 the incoming unregister/registration expiry requests.

unRegister success

Reports
                                          					 the number of successful unregisters.

Username Password

Shows
                                          					 the values within the authentication credential.

VRF

Displays information on the associated VRF ID.

### Related Commands

Command

Description

application (voice register pool)

Selects the session-level application for the dial peer associated with an
                                          						individual Cisco Unified SIP IP phone in a Cisco Unified CME environment or for
                                          						a group of phones in a Cisco Unified SIP SRST environment.

call-waiting (voice register pool)

Enables the call-waiting option on a SIP phone.

cor (voice register pool)

Configures a class of restriction on the VoIP dial peers associated with
                                          						directory numbers.

dnd-control (voice register template)

Enables the Do-Not-Disturb (DND) soft key on SIP phones.

dtmf-relay (voice register pool)

Specifies the list of dual-tone multifrequency (DTMF) relay methods that can be
                                          						used to relay DTMF audio tones between SIP endpoints.

id (voice register pool)

Explicitly identifies a locally available, individual Cisco Unified SIP IP
                                          						phone or, when running Cisco Unified SIP SRST, a set of Cisco Unified SIP IP
                                          						phones.

incoming called-number (dial peer)

Specifies a digit string that can be matched by an incoming call to associate
                                          						the call with a dial peer.

keep-conference (voice register pool)

Allows IP phone conference initiators to exit from conference calls and keep
                                          						the remaining parties connected.

lpcor incoming

Associates an incoming call with a logical partitioning class of restriction
                                          						(LPCOR) resource-group policy.

lpcor outgoing

Associates an outgoing call with an LPCOR resource-group policy.

lpcor type

Specifies the LPCOR type for an IP phone.

number (voice register pool)

Indicates the E.164 phone numbers that the registrar permits to handle the
                                          						Register message from a Cisco Unified SIP IP phone.

proxy (voice register pool)

Autogenerates additional VoIP dial peers to reach the main proxy whenever a
                                          						Cisco Unified SIP IP phone registers with a Cisco Unified SIP SRST gateway.

show sip-ua status registrar

Displays all the Cisco Unified SIP IP phones registered with the contact
                                          						address.

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register dial-peer

Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified CME or Cisco Unified SIP SRST register event.

translate-outgoing (voice register pool)

Allows an explicit setting of translation rules on the VoIP dial peer to modify
                                          						a phone number dialed by any Cisco Unified IP phone user.

type (voice register pool)

Defines a phone type for a SIP phone.

voice register pool

Enters voice register pool configuration mode for Cisco Unified SIP IP phones.

## show voice register pool attempted-registrations

To display the details of phones that attempt to register with Cisco
                              		  Unified CME or Cisco Unified SRST and fail, use the show voice register pool attempted-registrations command in privileged EXEC mode.

show voice register pool attempted-registrations

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phones that attempt to
                              		  register with Cisco Unified CME or Cisco Unified SRST and fail. If the phone
                              		  registers successfully after some time, the attempted registration entry will
                              		  still show up in the attempted-registration table. Use the clear voice register
                              		  attempted-registrations command to remove the entry from the attempted
                              		  registration table.

## Examples

## Examples

The following is a sample output from this command displaying
                              		  information for show voice register pool attempted-registrations:

```
Router# show voice register pool attempted-registrations Phones that have attempted registrations and have failed:
 MAC address: 001b.535c.d410 
 IP address : 8.3.3.111 
 Attempts   : 5
 Time of first attempt : *10:49:51.542 UTC Wed Oct 14 2009
 Time of latest attempt: *10:50:00.886 UTC Wed Oct 14 2009
 Reason for failure    : 
         No pool match for the registration request
 MAC address: 0015.c68e.6d13 
 IP address : 8.33.33.112 
 Attempts   : 4
 Time of first attempt : *10:49:53.418 UTC Wed Oct 14 2009
 Time of latest attempt: *10:50:00.434 UTC Wed Oct 14 2009
 Reason for failure    : 
         No pool match for the registration request
 MAC address: 0009.43E9.0B35 
 IP address : 9.13.40.83 
 Attempts   : 1
 Time of first attempt : *10:49:57.866 UTC Wed Oct 14 2009
 Time of latest attempt: *10:49:57.866 UTC Wed Oct 14 2009
 Reason for failure    : 
         No pool match for the registration request
```

The following is a sample output from this command displaying
                              		  information for show voice register pool attempted-registrations when none of
                              		  the phones fail:

```
Router# show voice register pool attempted-registrations         
 Phones that have attempted registrations and have failed: NONE
```

### Related Commands

Command

Description

attempted-registrations size

Allows to set the size of the table that stores information
                                          						related to SIP phones that attempt to register and fail.

clear voice register attempted-registrations

Clears entries from the attempted-registration table.

## show voice register pool connected

To display the details of SIP phones that are in connected state, use
                              		  the show voice register pool connected command in privileged EXEC mode.

show voice register pool connected [ brief ]

### Syntax Description

brief

(Optional) Displays brief details of SIP phones that are in
                                          						connected state.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phone that are
                              		  currently in connected state (in conversation). The output for show voice
                              		  register pool connected command shows details of both calls originating from
                              		  the SIP phones and calls made towards SIP phones. When used with brief keyword,
                              		  the show voice register pool connected command displays a brief detail of
                              		  phones in connected state.

Cisco Unified CME and Cisco Unified SRST

The following is sample output from this command displaying all
                              		  statistical information:

```
Router# show voice register pool connected Outbound calls from SIP line phones: 
Pool tag: 1
==============
 MAC Address    : 001B.535C.D410
 Contact IP     : 8.3.3.111
 Phone Number   : 45111
 Remote Number  : 45112
Call 2
SIP Call ID                : 001b535c-d4100010-79612b5a-336b0db5@8.3.3.111
   State of the call       : STATE_ACTIVE (7)
   Substate of the call    : SUBSTATE_NONE (0)
   Calling Number          : 45111
   Called Number           : 45112
   Bit Flags               : 0xC0401C 0x100 0x4
   CC Call ID              : 7
   Source IP Address (Sig ): 8.3.3.5
   Destn SIP Req Addr:Port : [8.3.3.111]:5060
   Destn SIP Resp Addr:Port: [8.3.3.111]:50076
   Destination Name        : 8.3.3.111
   Number of Media Streams : 1
   Number of Active Streams: 1
   RTP Fork Object         : 0x0
   Media Mode              : flow-through
   Media Stream 1
     State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 7
     Stream Type              : voice-only (0)
     Stream Media Addr Type   : 1
     Negotiated Codec         : g729r8 (20 bytes)
     Codec Payload Type       : 18 
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [8.3.3.5]:17580
     Media Dest IP Addr:Port  : [8.3.3.111]:26298
Options-Ping    ENABLED:NO    ACTIVE:NO
Inbound calls to SIP line phones: 
          
Pool tag: 2
==============
 MAC Address    : 0015.C68E.6D13
 Contact IP     : 8.33.33.112
 Phone Number   : 45112
 Remote Number  : 45111
Call 3
SIP Call ID                : 4DA52F97-ADA311DE-8019803A-FF3E4CBC@8.3.3.5
   State of the call       : STATE_ACTIVE (7)
   Substate of the call    : SUBSTATE_NONE (0)
   Calling Number          : 45111
   Called Number           : 45112
   Bit Flags               : 0xC04018 0x100 0x80
   CC Call ID              : 8
   Source IP Address (Sig ): 8.3.3.5
   Destn SIP Req Addr:Port : [8.33.33.112]:5060
   Destn SIP Resp Addr:Port: [8.33.33.112]:5060
   Destination Name        : 8.33.33.112
   Number of Media Streams : 1
   Number of Active Streams: 1
   RTP Fork Object         : 0x0
   Media Mode              : flow-through
   Media Stream 1
     State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 8
     Stream Type              : voice-only (0)
     Stream Media Addr Type   : 1
     Negotiated Codec         : g729r8 (20 bytes)
     Codec Payload Type       : 18 
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [8.3.3.5]:16384
     Media Dest IP Addr:Port  : [8.33.33.112]:30040
```

The following is sample output from this command displaying brief
                              		  statistical information:

```
Router# show voice register pool connected brief Pool IP Address      Number               Remote Number
==== =============== ==================== ====================
1    8.3.3.111       45111                45112               
Inbound calls to SIP line phones: 
Pool IP Address      Number               Remote Number
==== =============== ==================== ====================
2    8.33.33.112     45112                45111
```

### Related Commands

Command

Description

show sip-ua calls

Displays active user agent client (UAC) and user agent
                                          						server (UAS) information on SIP calls

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME
                                          						configurations and register information.

show voice register pool

Displays all configuration information associated with a
                                          						particular voice register pool.

## show voice
                        	 register pool ip

To display the
                              		  details of a SIP phone with a specific IP address, use the show voice register pool ip command in privileged EXEC mode.

show voice register pool ip ip-address

### Syntax Description

ip-address

IPv4
                                          						address of the SIP phone .

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.1(2)T

Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1

This
                                          						command was introduced.

### Usage Guidelines

Use this command
                              		  to display the details of a phone with a specific IP-address. When the pool ID
                              		  is configured as a mac address or an IP address the registered pools contain
                              		  the IP address information. The pool information is displayed if the IP
                              		  addresses match.

When the pool ID
                              		  is IP and the pool is unregistered, IP address configured under pool is
                              		  compared with the input IP. When the pool ID is network contact, the IP address
                              		  of each phone that is registered is compared with the input IP address.

## Examples

## Examples

The following is
                              		  sample output from this command displaying all statistical information:

```
Router# show voice register pool ip 8.3.3.111 Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
1    001B.535C.D410  8.3.3.111       1  1   45111                REGISTERED  
                                     4  7   451110               UNREGISTERED
```

Table 1 contains descriptions of significant fields shown in this
                              		  output, listed in alphabetical order.

Field

Description

DN

Voice
                                          					 register DN tag of the line.

ID

Phone
                                          					 identification (ID) address.

IP
                                          					 Address

IP
                                          					 address of the SIP phone.

LN

Line
                                          					 number of the telephone number.

Number

Number of
                                          					 the phones that have a mac address.

Pool

Tag ID of
                                          					 the pool.

State

Registration state of the line.

### Related Commands

Command

Description

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

## show voice
                        	 register pool mac

To display the
                              		  details of voice register pool associated with a specific phone type, use the show voice register pool mac command in privileged EXEC mode.

show voice register pool mac H . H . H

### Syntax Description

H.H.H

MAC
                                          						address of the SIP phone attempting to register.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.1(2)T

Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1

This
                                          						command was introduced.

### Usage Guidelines

Use this command
                              		  to display the details of the phone with the mac address H.H.H. The command
                              		  displays only the pools that are configured with an ID as mac.

## Examples

## Examples

The following is
                              		  sample output from this command displaying all statistical information:

```
Router# show voice register pool mac 001B.535C.D410 Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
1    001B.535C.D410  8.3.3.111       1  1   45111                REGISTERED  
                                     4  7   451110               UNREGISTERED
```

Table 1 contains descriptions of significant fields shown in this output, listed in
                              		  alphabetical order.

Field

Description

DN

Voice
                                          					 register DN tag of the line.

ID

Phone
                                          					 identification (ID) address.

IP
                                          					 Address

IP
                                          					 address of the SIP phone.

LN

Line
                                          					 number of the telephone number.

Number

Number of
                                          					 the phones that have a mac address.

Pool

Tag ID of
                                          					 the pool.

State

Registration state of the line.

### Related Commands

Command

Description

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

## show voice
                        	 register pool network

To display the
                              		  details of a phone with a specific network address, use the show voice register pool network command in privileged EXEC mode.

show voice register pool network network-address

### Syntax Description

network-address

Network
                                          						address of the SIP phone.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.1(2)T

Cisco
                                          						Unified SRST 8.1

This
                                          						command was introduced.

### Usage Guidelines

Use this command
                              		  to display the details of pools that have network ID configured and whose
                              		  network address matches the specific network address provided by the user.

## Examples

The following is
                              		  sample output from this command displaying all statistical information:

```
Router# show voice register pool network 78.89.0.0 Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
7    78.89.0.0                       1  1   6576                 UNREGISTERED
```

Table 1 contains descriptions of significant fields shown in this output, listed in
                              		  alphabetical order.

Field

Description

DN

Directory
                                          					 number of the phone.

ID

Phone
                                          					 identification (ID) address.

IP
                                          					 Address

IP
                                          					 address and port number of the phones

LN

Line
                                          					 number of the phone.

Number

Number of
                                          					 the phone that have network address.

Pool

Shows the
                                          					 current pool.

State

Registration state.

### Related Commands

Command

Description

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

show voice register pool ip

Displays the voice register pool details of a phone with a specific IP address.

## show voice register pool on-hold

To display the details of phones that are currently on-hold, use the show voice register pool oh-hold command in privileged EXEC mode.

show voice register pool on-hold [ brief ]

### Syntax Description

brief

(Optional) Displays brief details of SIP phones that are
                                          						currently on-hold.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phone that are
                              		  currently on-hold. The show voice register pool on-hold command output also
                              		  displays a field to show if the hold was a locally initiated hold (initiated on
                              		  the phone) or if the hold was initiated on the remote end. When used with brief
                              		  keyword, the show voice register pool on-hold command displays a brief
                              		  information of the phones that are currently put on hold by the remote caller
                              		  or have put the remote caller on hold. The “Hold-Origin” field specifies the
                              		  type of the hold, which can be either remote or local. Local indicates that the
                              		  call is placed on hold by the local phone and remote indicates that call is
                              		  placed on hold by the remote phone. In case of double-hold, the hold origin
                              		  will display the value “Local and Remote”.

## Examples

## Examples

The following is a sample output from this command displaying
                              		  information for phones ringing in a voice register pool:

```
Router# show voice register pool on-hold brief Outbound calls from SIP line phones: 
Pool IP Address      Number               Remote Number        Hold Origin
==== =============== ==================== ==================== ==============
1    8.3.3.111       45111                45112                Remote & Local
Inbound calls to SIP line phones: 
Pool IP Address      Number               Remote Number        Hold Origin
==== =============== ==================== ==================== ==============
2    8.33.33.112     45112                45111                Remote & Local
```

## Examples

## Examples

The following is a sample output from this command displaying
                              		  information for phones on-hold:

```
Router# show voice register pool on-hold Outbound calls from SIP line phones: 
Pool tag: 1
==============
 MAC Address    : 001B.535C.D410
 Contact IP     : 8.3.3.111
 Phone Number   : 45111
 Remote Number  : 45112
 Local Hold     : CALL HOLD Pressed on SIP Phone
Call 4
SIP Call ID                : 001b535c-d4100010-79612b5a-336b0db5@8.3.3.111
   State of the call       : STATE_ACTIVE (7)
   Substate of the call    : SUBSTATE_NONE (0)
   Calling Number          : 45111
   Called Number           : 45112
   Bit Flags               : 0xC0401C 0x10100 0x4
   CC Call ID              : 7
   Source IP Address (Sig ): 8.3.3.5
   Destn SIP Req Addr:Port : [8.3.3.111]:5060
   Destn SIP Resp Addr:Port: [8.3.3.111]:50076
   Destination Name        : 8.3.3.111
   Number of Media Streams : 1
   Number of Active Streams: 1
   RTP Fork Object         : 0x0
   Media Mode              : flow-through
   Media Stream 1
     State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 7
     Stream Type              : voice-only (0)
     Stream Media Addr Type   : 1
     Negotiated Codec         : g729r8 (20 bytes)
     Codec Payload Type       : 18 
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [8.3.3.5]:17580
     Media Dest IP Addr:Port  : [8.3.3.111]:26298
Options-Ping    ENABLED:NO    ACTIVE:NO
Inbound calls to SIP line phones: 
Pool tag: 2
==============
 MAC Address    : 0015.C68E.6D13
 Contact IP     : 8.33.33.112
 Phone Number   : 45112
 Remote Number  : 45111
 Remote Hold    : SIP Phone has received CALL HOLD
Call 5
SIP Call ID                : 4DA52F97-ADA311DE-8019803A-FF3E4CBC@8.3.3.5
   State of the call       : STATE_ACTIVE (7)
   Substate of the call    : SUBSTATE_NONE (0)
   Calling Number          : 45111
   Called Number           : 45112
   Bit Flags               : 0xC04018 0x4100 0x80
   CC Call ID              : 8
   Source IP Address (Sig ): 8.3.3.5
   Destn SIP Req Addr:Port : [8.33.33.112]:5060
   Destn SIP Resp Addr:Port: [8.33.33.112]:5060
   Destination Name        : 8.33.33.112
   Number of Media Streams : 1
   Number of Active Streams: 1
   RTP Fork Object         : 0x0
   Media Mode              : flow-through
   Media Stream 1
     State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 8
     Stream Type              : voice-only (0)
     Stream Media Addr Type   : 1
     Negotiated Codec         : g729r8 (20 bytes)
     Codec Payload Type       : 18 
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [8.3.3.5]:16384
     Media Dest IP Addr:Port  : [8.33.33.112]:30040
Options-Ping    ENABLED:NO    ACTIVE:NO
```

### Related Commands

Command

Description

show voice register all

Displays all Cisco SIP SRST and Cisco CME configurations
                                          						and register information.

show sip-ua calls

Displays active user agent client (UAC) and user agent
                                          						server (UAS) information on SIP calls

show voice register pool

Displays all configuration information associated with a
                                          						particular voice register pool.

## show voice
                        	 register pool registered

To display the
                              		  details of phones that successfully register to Cisco Unified Communications
                              		  Manager Express (Cisco Unified CME), use the show voice register pool registered command in privileged EXEC mode.

show voice register pool registered

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco
                                          						IOS Release

Version

Modification

15.1(2)T

Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1

This
                                          						command was introduced.

15.2(4)M

Cisco
                                          						Unified CME 9.1 Cisco Unified SIP SRST 9.1

This
                                          						command was modified to display Key Expansion Module (KEM) details with the
                                          						phone type information.

### Usage Guidelines

Use the show voice register pool registered command to display the details of
                              		  phones that are successfully registered to Cisco Unified CME and Cisco Unified
                              		  Survivable Remote Site Telephony (Cisco Unified SRST).

## Examples

## Examples

The following is
                              		  a sample output displaying information for a registered voice register pool in
                              		  Cisco Unified CME:

```
Router# show voice register pool registered Pool Tag 1
Config:
  Mac address is 001B.535C.D410
  Type is 7960
  Number list 1 : DN 1
  Number list 3 : DN 8
  Number list 4 : DN 7
  Proxy Ip address is 0.0.0.0
  Current Phone load version is Cisco-CP7960G/8.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  Busy trigger per button value is 0
  call-forward phone all is 4566
  call-forward b2bua all 4555
  keep-conference is enabled
  Lpcor Type is none
  Transport type is udp
  service-control mechanism is supported
  registration Call ID is 001b535c-d410790d-17a6877e-5d04bbc5@8.3.3.111 
  Privacy feature is not configured.
  Privacy button is disabled
  active primary line is: 45111
  contact IP address: 8.3.3.111 port 5060
Dialpeers created:
Dial-peers for Pool 1:
dial-peer voice 40001 voip
 destination-pattern 45111
 session target ipv4:8.3.3.111:5060
 session protocol sipv2
  call-fwd-all         4555           
  after-hours-exempt   FALSE          
Statistics:
  Active registrations  : 1
  Total SIP phones registered: 1
  Total Registration Statistics
    Registration requests  : 1
    Registration success   : 1
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : *11:40:32.263 UTC Wed Oct 14 2009 
    Last unregister request time : 
    Register success time        : *11:40:32.267 UTC Wed Oct 14 2009 
    Unregister success time      :
```

The following is
                              		  a sample output displaying information for a registered voice register pool
                              		  with a Cisco Unified 9971 Session Initiation Protocol (SIP) IP phone attached
                              		  to a Cisco SIP IP Phone CKEM 36-Button Line Expansion Module:

```
Router# show voice register pool registered Pool Tag 5
Config:
Mac address is B4A4.E328.4698
Type is 9971 addon 1 CKEM
Number list 1 : DN 2
Number list 2 : DN 3
Proxy Ip address is 0.0.0.0
DTMF Relay is disabled
Call Waiting is enabled
DnD is disabled
Video is enabled
Camera is enabled
Busy trigger per button value is 0
keep-conference is enabled
registration expires timer max is 200 and min is 60
kpml signal is enabled
Lpcor Type is none
```

## Examples

```
The following is a sample output displaying information for a registered voice register pool in Cisco Unified SRST:
Router# show voice register pool registered Pool Tag 1
Config:
  Ip address is 9.13.18.40, Mask is 255.255.0.0
  Number list 1 : DN 1
  Number list 2 : DN 2
  Number list 3 : DN 3
  Number list 4 : DN 4
  Number list 5 : DN 5
  Number list 6 : DN 6
  Number list 7 : DN 7
  Proxy Ip address is 0.0.0.0
  DTMF Relay is enabled, rtp-nte, sip-notify
  kpml signal is enabled
  Lpcor Type is none
Dialpeers created:
Dial-peers for Pool 1:
dial-peer voice 40004 voip
 destination-pattern 1000
 redirect ip2ip
 session target ipv4:9.13.18.40:19633
 session protocol sipv2
 dtmf-relay rtp-nte sip-notify
 digit collect kpml
 codec  g711ulaw bytes 160
  after-hours-exempt   FALSE          
dial-peer voice 40001 voip
 destination-pattern 2000
 redirect ip2ip
 session target ipv4:9.13.18.40:19634
 session protocol sipv2
 dtmf-relay rtp-nte sip-notify
 digit collect kpml
 codec  g711ulaw bytes 160
  after-hours-exempt   FALSE          
dial-peer voice 40002 voip
 destination-pattern 3000
 redirect ip2ip
 session target ipv4:9.13.18.40:19635
 session protocol sipv2
 dtmf-relay rtp-nte sip-notify
 digit collect kpml
 codec  g711ulaw bytes 160
  after-hours-exempt   FALSE          
dial-peer voice 40003 voip
 destination-pattern 4000
 redirect ip2ip
 session target ipv4:9.13.18.40:19636
 session protocol sipv2
 dtmf-relay rtp-nte sip-notify
 digit collect kpml
 codec  g711ulaw bytes 160
  after-hours-exempt   FALSE          
Statistics:
  Active registrations  : 4
  Total SIP phones registered: 1
  Total Registration Statistics
    Registration requests  : 4
    Registration success   : 4
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : .05:22:55.604 UTC Tue Oct 6 2009 
    Last unregister request time : 
    Register success time        : .05:22:55.604 UTC Tue Oct 6 2009 
    Unregister success time      :
```

Table 1 contains descriptions of significant fields shown in the show voice register pool registered command output, listed in alphabetical
                              		  order.

Field

Description

Active
                                          					 registrations

Shows the
                                          					 current active registrations.

Application

Shows the application command configuration for this pool.

Call
                                          					 Waiting

Shows the
                                          					 setting of the call-waiting command.

Class
                                          					 of Restriction List Tag

Shows
                                          					 the COR tag.

Config

Shows
                                          					 the voice register pool.

Current
                                          					 phone-load

Shows
                                          					 the current version of the phone load.

Default
                                          					 preference

Shows
                                          					 the default preference value of this pool.

Dialpeers created

Results
                                          					 in a list of all dial peers created and their contents. Dial-peer contents
                                          					 differ for each application and are not described here.

DnD

Shows
                                          					 the setting of the dnd-control command.

DTMF
                                          					 Relay

Shows
                                          					 the setting of the dtmf-relay command.

Emergency response location

Shows
                                          					 the ephone’s emergency response location to which an emergency response team is
                                          					 dispatched when an emergency call is made.

Incoming called number

Shows
                                          					 the incoming called-number command configuration.

Incoming corlist name

Shows
                                          					 the cor command
                                          					 configuration.

keep-conference

Shows
                                          					 the status of the keep-conference command.

Lpcor
                                          					 Incoming

Shows
                                          					 the setting of the lpcor incoming command.

Lpcor
                                          					 Outgoing

Shows
                                          					 the setting of the lpcor outgoing command.

Lpcor
                                          					 Type

Shows
                                          					 the setting of the lpcor type command.

Mac
                                          					 address

Shows
                                          					 the MAC address of this SIP phone as defined by the id command.

Network
                                          					 address and Mask

Shows
                                          					 network address and mask information when the id command is configured.

Number
                                          					 list, Pattern, and Preference

Shows
                                          					 the number command configuration.

Pool
                                          					 Tag

Shows
                                          					 the assigned tag number of the current pool.

Previous phone-load

Shows
                                          					 the version of the previous phone load.

Proxy
                                          					 IP address

Shows
                                          					 the proxy command configuration; that is, the IP address of the external SIP server.

Registration failed

Shows
                                          					 the failed registrations.

Registration requests

Shows
                                          					 the incoming registration requests.

Registration success

Shows
                                          					 the successful registrations.

Statistics

Shows
                                          					 the registration statistics for this pool.

statistics time-stamps

Shows
                                          					 the registration statistics for this pool with specific time stamps.

Template

Shows
                                          					 the template-tag number for the template applied to this SIP phone.

Total
                                          					 Registration Statistics

Shows
                                          					 the total registration statistics for this pool.

Translate outgoing called tag

Shows
                                          					 the translate-outgoing command configuration.

Type

Shows
                                          					 the phone type identified for this SIP phone using the type command.

unRegister failed

Reports
                                          					 the number of failed unregisters.

unRegister requests

Shows
                                          					 the incoming unregister/registration expiry requests.

unRegister success

Reports
                                          					 the number of successful unregisters.

Username Password

Shows
                                          					 the values within the authentication credential.

### Related Commands

Command

Description

application (voice register pool)

Selects the session-level application for the dial peer associated with an
                                          						individual Cisco Unified SIP IP phone in a Cisco Unified CME environment or for
                                          						a group of phones in a Cisco Unified SIP SRST environment.

call-waiting (voice register pool)

Enables the call-waiting option on a SIP phone.

cor (voice register pool)

Configures a class of restriction on the VoIP dial peers associated with
                                          						directory numbers.

dnd-control (voice register template)

Enables the Do-Not-Disturb (DND) soft key on SIP phones.

dtmf-relay (voice register pool)

Specifies the list of dual-tone multifrequency (DTMF) relay methods that can be
                                          						used to relay DTMF audio tones between SIP endpoints.

id (voice register pool)

Explicitly identifies a locally available, individual Cisco Unified SIP IP
                                          						phone or, when running Cisco Unified SIP SRST, a set of Cisco Unified SIP IP
                                          						phones.

incoming called-number (dial peer)

Specifies a digit string that can be matched by an incoming call to associate
                                          						the call with a dial peer.

keep-conference (voice register pool)

Allows IP phone conference initiators to exit from conference calls and keep
                                          						the remaining parties connected.

lpcor incoming

Associates an incoming call with a logical partitioning class of restriction
                                          						(LPCOR) resource-group policy.

lpcor outgoing

Associates an outgoing call with an LPCOR resource-group policy.

lpcor type

Specifies the LPCOR type for an IP phone.

number (voice register pool)

Indicates the E.164 phone numbers that the registrar permits to handle the
                                          						Register message from a Cisco Unified SIP IP phone.

proxy (voice register pool)

Autogenerates additional VoIP dial peers to reach the main proxy whenever a
                                          						Cisco Unified SIP IP phone registers with a Cisco Unified SIP SRST gateway.

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register dial-peers

Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified SIP SRST or Cisco Unified CME register event.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

show voice register pool unregistered

Displays the details of voice register pools that do not have any phones
                                          						registered.

translate-outgoing (voice register pool)

Allows an explicit setting of translation rules on the VoIP dial peer to modify
                                          						a phone number dialed by any Cisco Unified IP phone user.

type (voice register pool)

Defines a phone type for a SIP phone.

voice register pool

Enters voice register pool configuration mode for SIP phones.

## show voice register pool ringing

To display the details of phones that are currently in ringing state,
                              		  use the show voice register pool ringing command in privileged EXEC mode.

show voice register pool ringing [ brief ]

### Syntax Description

brief

(Optional) Displays brief details of SIP phones that are
                                          						currently in ringing state.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the phone that are
                              		  currently in ringing state. When used with the brief keyword, the show voice
                              		  register pool ringing brief command only displays information related to calls
                              		  that are bound towards the SIP phones.

## Examples

## Examples

The following is a sample output from this command displaying
                              		  information for phones ringing in a voice register pool:

```
Router# show voice register pool ringing brief Pool IP Address      Number               Remote Number
==== =============== ==================== ====================
2    8.33.33.112     45112                45111
```

## Examples

The following is a sample output from this command displaying
                              		  information for phones ringing in a voice register pool:

```
Router# show voice register pool ringing Pool tag: 2
==============
 MAC Address    : 0015.C68E.6D13
 Contact IP     : 8.33.33.112
 Phone Number   : 45112
 Remote Number  : 45111
Call 1
SIP Call ID                : C0B5DA7-ADA311DE-8011803A-FF3E4CBC@8.3.3.5
   State of the call       : STATE_RECD_PROCEEDING (4)
   Substate of the call    : SUBSTATE_PROCEEDING_PROCEEDING (2)
   Calling Number          : 45111
   Called Number           : 45112
   Bit Flags               : 0xC00018 0x100 0x280
   CC Call ID              : 5
   Source IP Address (Sig ): 8.3.3.5
   Destn SIP Req Addr:Port : [8.33.33.112]:5060
   Destn SIP Resp Addr:Port: [8.33.33.112]:5060
   Destination Name        : 8.33.33.112
   Number of Media Streams : 1
   Number of Active Streams: 1
   RTP Fork Object         : 0x0
   Media Mode              : flow-through
   Media Stream 1
     State of the stream      : STREAM_ACTIVE
     Stream Call ID           : 5
     Stream Type              : voice+dtmf (1)
     Stream Media Addr Type   : 1
     Negotiated Codec         : No Codec    (0 bytes)
     Codec Payload Type       : 255 (None)
     Negotiated Dtmf-relay    : inband-voice
     Dtmf-relay Payload Type  : 0
     QoS ID                   : -1
     Local QoS Strength       : BestEffort
     Negotiated QoS Strength  : BestEffort
     Negotiated QoS Direction : None
     Local QoS Status         : None
     Media Source IP Addr:Port: [8.3.3.5]:16882
```

### Related Commands

Command

Description

show sip-ua calls

Displays active user agent client (UAC) and user agent
                                          						server (UAS) information on SIP calls

show voice register all

Displays all Cisco SIP SRST and Cisco CME configurations
                                          						and register information.

show voice register pool

Displays all configuration information associated with a
                                          						particular voice register pool.

## show voice
                        	 register pool telephone-number

To display the
                              		  details of a phone line with a specific telephone-number, use the show voice register pool telephone-number command in privileged EXEC mode.

show voice register pool telephone-number number

### Syntax Description

number

Number
                                          						identifying a specific phone.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.1(2)T

Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1

This
                                          						command was introduced.

### Usage Guidelines

Use this command
                              		  to display the details of the phone line with the specified telephone-number.
                              		  If the line is registered, the contact ip address will be displayed. When the
                              		  phone line is not registered and the pool ID type is network IP, the IP address
                              		  is not displayed. When the phone line is not registered but some other line is
                              		  registered for the same pool with MAC or IP address, then the IP address is
                              		  displayed.

## Examples

The following is
                              		  a sample output from this command displaying all statistical information:

```
Router# show voice register pool telephone number 45112 Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
2    0015.C68E.6D13                  1  2   45112                UNREGISTERED
7    0018.BAC8.D2B1                  1  2   45112                UNREGISTERED
```

## Examples

```
Router# show voice register pool telephone-number 1000
Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
1    9.13.18.40      9.13.18.40      1  1   1000                 REGISTERED
```

The following
                              		  table contains descriptions of significant fields shown in this output, listed
                              		  in alphabetical order.

Field

Description

DN

Directory
                                          					 number of the phone.

ID

Phone
                                          					 identification (ID) address.

IP
                                          					 Address

IP
                                          					 address and port number of the phones

LN

Line
                                          					 number of the phone.

Number

Number of
                                          					 the phones.

Pool

Shows the
                                          					 current pool.

State

Registration state.

### Related Commands

Command

Description

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

show
                                          						voice register pool detail all

Displays the details of all the pools defined in the system.

## show voice register pool unregistered

To display the details of the voice registration pools that do not
                              		  have any phones registered, use the show voice register pool unregistered command in privileged EXEC mode.

show voice register pool unregistered

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC

## Command History

Cisco IOS Release

Version

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to display the details of the pools that do not have
                              		  any active registrations. In Cisco Unified SRST, if multiple phones are trying
                              		  to register through the same pool and if one phone successfully registers and
                              		  the others do not, the pool is not considered as an unregistered pool, as it
                              		  does have an active registration of the registered phone.

## Examples

## Examples

The following is a sample output from this command displaying
                              		  information for pools with no active registeration:

```
Router# show voice register pool unregistered Pool Tag: 2
 MAC Address                : 0015.C68E.6D13
 No. of attempts to register: 0
 Unregister time            :
 Last register request time :
 Reason for state unregister: 
         No registration request since last reboot/unregister
 Pool Tag: 3
 MAC Address                : 0021.5553.8998
 No. of attempts to register: 0
 Unregister time            :
 Last register request time :
 Reason for state unregister: 
         No registration request since last reboot/unregister
 Pool Tag: 4
 MAC Address                : 8989.9867.8769
 No. of attempts to register: 0
 Unregister time            :
 Last register request time :
 Reason for state unregister: 
         No registration request since last reboot/unregister
```

### Related Commands

Command

Description

show voice register all

Displays all Cisco SIP SRST and Cisco CME configurations
                                          						and register information.

show voice register pool

Displays all configuration information associated with a
                                          						particular voice register pool.

show voice register pool registered

Displays details of phones that sucessfully register to
                                          						Cisco Unified CME or Cisco Unified SRST.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## show voip sip-oauth key-server status

To display key retrieval details for SIP OAuth from CUCM.

show voip sip-oauth key-server status

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

This command was introduced.

## Examples

```
CUBE1-1B#show voip sip-oauth key-server status
Key-server:                 10.1.10.50
Last Request Time:          11:40:58.389 UTC Fri Nov 12 2021
Last Success response Time: 11:40:58.456 UTC Fri Nov 12 2021
Current Status:             SUCCESS
Next Request Time:          11:40:58.389 UTC Sat Nov 13 2021
Total requests sent:        13
Total success responses:    3
Total failure responses:    10
```

## Examples

```
CUBE1-1B#show voip sip-oauth key-server status
Key-server:                 10.10.10.40
Last Request Time:          11:29:26.985 UTC Fri Nov 12 2021
Last Success response Time:
Current Status:             FAILURE (Timeout Error)
Next Request Time:          11:29:26.985 UTC Sat Nov 13 2021
Total requests sent:        8
Total success responses:    0
Total failure responses:    8
```

## show voice
                        	 register statistics

To display
                              		  statistics associated with the registration event, use the show voice register statistics command in privileged EXEC mode.

show voice register statistics [ global | pool tag ]

### Syntax Description

global

(Optional) Displays aggregate statistics associated with the SIP phone
                                          						registration event.

pool
                                          						tag

(Optional) Displays registration pool statistics associated with a specific
                                          						pool tag. The maximum number of pools is version and platform dependent. Type ? to display
                                          						a list of values.

### Command Modes

Privileged EXEC

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						SIP SRST 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						SIP SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

12.4(4)T

Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4

This
                                          						command was added to Cisco CME.

15.1(2)T

Cisco
                                          						CME 8.1 Cisco SIP SRST 8.1

This
                                          						command was modified. The global and pool keywords and tag argument were added.
                                          						The output display was also modified to show more information about pools in
                                          						unregistered state and time-stamps of registration event.

### Usage Guidelines

When using the show voice register statistics command, you can verify that the number of Registration and
                              		  unRegister successes for global statistics are the sum of the values in the
                              		  individual pools. Because some Registrations fail even before matching a voice
                              		  register pool, for Registration and unRegister failed statistics the value is
                              		  not the sum of the values in the individual pools. Immediate failures are
                              		  accounted in the global statistics.

In Cisco Unified
                              		  CME 8.1 and Cisco Unified SIP SRST 8.1, the time-stamps for the events is
                              		  displayed along with other registration related statistics. The command output
                              		  also displays the reason for pools in unregistered state. Use the show voice
                              		  register statistics command with pool tag keyword to display registration pool
                              		  statistics associated with a specific pool.

When using the
                              		  global keyword, the show voice register command output displays the aggregate
                              		  statistics associated with SIP phone registration. The output of this command
                              		  also displays the attempted-registrations table.

## Examples

## Examples

The following is
                              		  a sample output from this command displaying all statistical information:

```
Router# show voice register statistics Sample Output:
Global statistics
  Active registrations  : 2
  Total SIP phones registered: 2
  Total Registration Statistics
    Registration requests  : 3
    Registration success   : 2
    Registration failed    : 1
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
    after last unregister        : 1 
    Last Register Request Time   : *11:42:31.783 UTC Wed Sep 16 2009 
    Last Unregister Request Time : 
    Register Success Time        : *11:11:56.707 UTC Wed Sep 16 2009 
    Unregister Success Time      : 
Register pool 1 statistics
  Active registrations  : 1
  Total SIP phones registered: 1
  Total Registration Statistics
    Registration requests  : 1
    Registration success   : 1
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
    after last unregister        : 0 
    Last Register Request Time   : *11:11:54.615 UTC Wed Sep 16 2009 
    Last Unregister Request Time : 
    Register Success Time        : *11:11:54.623 UTC Wed Sep 16 2009 
    Unregister Success Time      : 
Register pool 2 statistics
  Active registrations  : 1
  Total SIP phones registered: 1
  Total Registration Statistics
    Registration requests  : 1
    Registration success   : 1
    Registration failed    : 0
    unRegister requests    : 0
    unRegister success     : 0
    unRegister failed      : 0
    Attempts to register 
    after last unregister        : 0 
    Last Register Request Time   : *11:11:56.707 UTC Wed Sep 16 2009 
    Last Unregister Request Time : 
    Register Success Time        : *11:11:56.707 UTC Wed Sep 16 2009 
    Unregister Success Time      :
```

## Examples

The following is
                              		  a sample output from this command displaying all statistical information:

```
Router# show voice register statistics global Global Statistics: 
  Active registrations  : 1
  Total SIP phones registered: 2
  Total Registration Statistics
    R egistration requests  : 97715
    Registration success   : 3
    Registration failed    : 97712
    unRegister requests    : 1
    unRegister success     : 1
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 97712 
    Last register request time   : *06:45:11.127 UTC Wed Oct 14 2009 
    Last unregister request time : *11:56:22.179 UTC Tue Oct 13 2009 
    Register success time        : *12:10:37.263 UTC Tue Oct 13 2009 
    Unregister success time      : *11:56:22.182 UTC Tue Oct 13 2009 
 Phones that have attempted registrations and have failed:
 MAC address: 001b.535c.d410 
 IP address : 8.3.3.111 
 Attempts   : 97712
 Time of first attempt : *12:20:32.775 UTC Tue Oct 13 2009
 Time of latest attempt: *06:46:14.815 UTC Wed Oct 14 2009
 Reason for failure    : 
         Unauthorized registration request
```

## Examples

The following
                              		  is a sample output from this command displaying all statistical information
                              		  associated with pool 1:

```
Router# show voice register statistics pool 1 Pool 1 Statistics: 
  Active registrations  : 0
  Total SIP phones registered: 1
  Total Registration Statistics
    Registration requests  : 2
    Registration success   : 2
    Registration failed    : 0
    unRegister requests    : 1
    unRegister success     : 1
    unRegister failed      : 0
    Attempts to register 
           after last unregister : 0 
    Last register request time   : *12:10:37.259 UTC Tue Oct 13 2009 
    Last unregister request time : *11:56:22.179 UTC Tue Oct 13 2009 
    Register success time        : *12:10:37.263 UTC Tue Oct 13 2009 
    Unregister success time      : *11:56:22.182 UTC Tue Oct 13 2009 
  Reason for unregistered state: 
         No registration request since last reboot/unregister
```

Table 1 describes the significant fields shown in this output.

Field

Description

Statistics:

Used
                                          					 with the all , pool , and statistics keywords. Shows the registration statistics for this pool.

Active
                                          					 registrations

Used
                                          					 with the all , pool , and statistics keywords. Shows the current active registrations.

Last
                                          					 Register Request Time

Used
                                          					 with all, pool, and statistics keywords. Shows details such as day, date, and
                                          					 time when the phones requested to register the last time.

Last
                                          					 unRegister Request Time

Used
                                          					 with all, pool, and statistics keywords. Shows details such as day, date, and
                                          					 time when the phones requested to unregister the last time.

Total
                                          					 Registration Statistics

Used
                                          					 with the all , pool , and statistics keywords. Shows the total registration statistics for this pool.

Registration requests

Used
                                          					 with the all , pool , and statistics keywords. Shows the incoming registration requests.

Registration success

Used
                                          					 with the all , pool , and statistics keywords. Shows the successful registrations.

Registration failed

Used
                                          					 with the all , pool , and statistics keywords. Shows the failed registrations.

unRegister requests

Used
                                          					 with the all , pool , and statistics keywords. Shows the incoming unregister/registration expire requests.

unRegister success

Used
                                          					 with the all , pool , and statistics keywords. Reports the number of successful unregisters.

unRegister failed

Used
                                          					 with the all , pool , and statistics keywords. Reports the number of failed unregisters.

Global
                                          					 statistics

Used
                                          					 with the statistics keyword. Details all active registrations.

Register pool number statistics

Used
                                          					 with the statistics keyword. Details specific pool statistics.

### Related Commands

Command

Description

show voice register all

Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information.

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

show
                                          						voice register pool attempted-registrations

Displays the details of phones that attempt to register with Cisco Unified CME
                                          						or Cisco Unified SRST and fail.

## srtp-crypto

To assign a previously configured crypto-suite selection preference list globally or to a voice class tenant, use the srtp-crypto command. To remove the crypto-suite selection preference and return to default preference list, use the no or default form of this command.

srtp-crypto crypto-tag

no srtp-crypto

default srtp-crypto

## Syntax Description

Unique number that is assigned to the voice class. The range is 1–10000.

This number maps to the tag created using the voice class srtp-crypto command available in global configuration mode.

### Command Default

No crypto-suite preference assigned.

### Command Modes

voice class tenant configuration (config-class)

voice service voice sip configuration (conf-serv-sip)

Voice register pool (config-register-pool).

## Command History

Cisco IOS XE Everest 16.5.1b

This command was introduced.

Implemented voice class srtp-crypto tag under voice register pool.

### Usage Guidelines

From Cisco IOS XE Cupertino
                                       17.8.1a , voice class srtp-crypto tag is implemented under voice register pool mode. This command associates SRTP crypto ciphers with the pool.

Ensure that SRTP voice-class is created using the voice class srtp-crypto crypto-tag command before executing the srtp-crypto crypto tag command to apply the crypto-tag under global or tenant configuration mode.

You can assign only one crypto-tag. If you assign another crypto-tag, the last crypto-tag that is assigned replaces the previous
                              crypto-tag.

## Examples

Example for assigning a crypto-suite preference to a voice class tenant:

```
Device> enable Device# configure terminal Device(config)# voice class tenant 100 Device(config-class)# srtp-crypto 102
```

Example for assigning a crypto-suite preference globally:

```
Device> enable Device# configure terminal Device(config)# voice service voice Device(conf-voi-serv)# sip Device(conf-serv-sip)# srtp-crypto 102
```

## Examples

The following is an example of voice class srtp-crypto tag under voice register pool mode.

```
Router(config)#voice class srtp-crypto 22
Router(config-class)#crypto ?
```

```
Router(config-class)#crypto ?
        <1-4>   Set the preference order for the cipher-suite (1 = Highest)
```

```
Router(config-class)#crypto 1 ?
	AEAD_AES_128_GCM			Allow secure calls with SRTP AEAD_AES_128_GCM 
	AEAD_AES_256_GCM			Allow secure calls with SRTP AEAD_AES_256_GCM 
	AES_CM_128_HMAC_SHA1_32		Allow secure calls with SRTP AES_CM_128_HMAC_SHA1_32 
	AES_CM_128_HMAC_SHA1_80		Allow secure calls with SRTP AES_CM_128_HMAC_SHA1_80 
Router(config-class)#crypto 1 AEAD_AES_256_GCM
```

```
Router(config-class)#do show run | sec srtp-cry
 	voice class srtp-crypto 22
 	crypto 1 AEAD_AES_256_GCM
```

```
Router(config)# voice register pool 17
Router(config-register-pool)# id network 10.1.10.217 mask 255.255.255.255
Router(config-register-pool)# dtmf-relay rtp-nte
Router(config-register-pool)# codec g711ulaw
```

When you configure srtp-crypto 23 , which is not present:

```
Router(config-register-pool)#voice-class srtp-crypto 23
ERROR: There is no voice-class srtp-crypto 23
```

When you configure srtp-crypto 22 , which is present:

```
Router(config-register-pool)#voice-class srtp-crypto 22
```

Show run output for pool:

```
Router#show running-config | sec voice register pool 17
voice register pool 17
id network 10.1.10.217 mask 255.255.255.255
dtmf-relay rtp-nte
voice-class srtp-crypto 22
codec g711ulaw
Router#
```

voice class srtp-crypto must be configured before adding to a voice register pool.

### Related Commands

Command

Description

voice class sip srtp-crypto

Enters voice class configuration mode and assigns an identification tag for a srtp-crypto voice class.

crypto

Specifies the preference for the SRTP cipher-suite that will be offered by Cisco Unified Border Element (CUBE) in the SDP
                                          in offer and answer.

show sip-ua calls

Displays active user agent client (UAC) and user agent server (UAS) information on Session Initiation Protocol (SIP) calls.

show sip-ua srtp

Displays Session Initiation Protocol (SIP) user-agent (UA) Secure Real-time Transport Protocol (SRTP) information.

## subnet

To define which IP phones are part of an emergency response location
                              		  (ERL) for the enhanced 911 service, use the subnet command in voice emergency response
                              		  location configuration mode. To remove the subnet definition, use the no form of this command.

subnet [ 1 | 2 ] IPaddress mask

no subnet [ 1 | 2 ]

### Syntax Description

IPaddress

IP address that identifies which IP phones are part of the
                                          						ERL.

mask

IP subnet mask for the network segment that is part of the
                                          						ERL.

### Command Default

No subnets are defined.

### Command Modes

V oice emergency response location configuration (cfg-emrgncy-resp-location)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)T

Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1

This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only.

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was added to Cisco Unified CME.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command defines the groups of IP phones that are part of an ERL.
                              		  You can create up to 2 different subnets. To include all phones on a single
                              		  ERL, you can set the subnet mask to 0.0.0.0 to indicate a “catch-all” subnet.

## Examples

In the following example, all IP phones with the IP address of
                              		  10.X.X.X or 192.168.X.X are automatically associated with this ERL. If one of
                              		  the phones dials 911, its extension is replaced with 408 555-0100 before it
                              		  goes to the PSAP. The PSAP will see that the caller’s number is 408 555-0100.

```
voice emergency response location 1
 elin 1 4085550100
 subnet 10.0.0.0 255.0.0.0
 subnet 2 192.168.0.0 255.255.0.0
```

### Related Commands

Command

Description

elin

Specifies a PSTN number that will replace the caller’s
                                          						extension.

## system message (call-manager-fallback)

To customize the system message text displayed on all Cisco IP phones
                              		  units in fallback mode that are connected to a Cisco Unified Survivable Remote
                              		  Site Telephony ( SRST) router, use the system message command in call-manager-fallback
                              		  configuration mode. To disable the customized message and return to the default
                              		  system message, use the no form of this command.

system message { primary primary-string | secondary secondary-string }

no system message { primary primary-string | secondary secondary-string }

### Syntax Description

primary

Sets the system message for Cisco IP phones that can
                                          						support static text messages during fallback, such as the Cisco IP Phone 7940
                                          						and the Cisco IP Phone 7960.

primary-string

Text string of less than 32 characters.

secondary

Sets the system message for Cisco IP phones that do not
                                          						support static text messages and that have a limited display space, such as the
                                          						Cisco IP Phone 7910.

secondary-string

Text string of less than 20 characters.

### Command Default

The default fallback display message for Cisco IP phones that support
                              		  static text messages is “CM Fallback Service Operating.” For Cisco IP phones
                              		  that do not support static text messages, the default message is “CM Fallback
                              		  Service.”

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

Changes to the display message configuration occur only after a phone
                              		  reset, at the end of each call, or on receipt of the next keepalive message
                              		  from an idle phone.

The normal in-service static text message is controlled by Cisco
                              		  Unified Communications Manager.

Secondary IP phones flash system messages during fallback.

## Examples

The following example sets the system message to “Customized Message”
                              		  for all Cisco IP Phone 7940 and Cisco IP Phone 7960 units connected to a Cisco
                              		  Unified SRST router:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# system message primary Customized Message
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST feature support and enters call-manager-fallback configuration
                                          						mode.

## system message (voice register global)

To define a message that displays on SIP phones in a Cisco Unified
                              		  Survivable Remote Site Telephony (Cisco Unified SRST) system, use the system message command in voice register global
                              		  configuration mode. To return to the default, use the no form of this command.

system message string

no system message

### Syntax Description

string

Message that displays on SIP phones after the phones
                                          						failover to Cisco Unified SRST. String can contain a maximum of 32 alphanumeric
                                          						characters.

### Command Default

“CM Fallback Service Operating” message from dictionary file
                              		  displays.

### Command Modes

Voice register global configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XJ

Cisco Unified SRST 4.1

This command was introduced.

12.4(15)T

Cisco Unified CME 4.1

This command was integrated into Cisco IOS Release
                                          						12.4(15)T.

Cisco Unified SIP SRST 12.8

Introduced support for YANG models.

### Usage Guidelines

The command allows you to customize the idle prompt message that
                              		  displays on the status line of SIP phones after the phones lose connection with
                              		  Cisco Unified Communications Manager and failover to Cisco Unified SRST. The
                              		  default message that displays is from the dictionary file for the phone. The
                              		  configured message displays until the phones fallback to Cisco Unified
                              		  Communications Manager. For versions earlier than Cisco Unified SRST 4.1, the
                              		  phones display the default message from the dictionary file.

This command is not supported on the Cisco Unified IP Phone 7905,
                              		  7912, 7940, or 7960.

## Examples

The following example shows that SIP phones will display the message,
                              		  “SRST service active” after the phones register to Cisco Unified SRST.

```
Router(config)# voice register global Router(config-register-global)# system message SRST service active
```

### Related Commands

Command

Description

show voice register global

Displays all global configuration parameters associated
                                          						with SIP phones.

## time-format (call-manager-fallback)

To set the time display format on all Cisco IP phones attached to a
                              		  router, use the time-format command in call-manager-fallback
                              		  configuration mode. To disable the time display format, use the no form of this command.

time-format { 12 | 24 }

no time-format { 12 | 24 }

### Syntax Description

12

Sets format to 12-hour increments.

24

Sets format to 24-hour increments.

### Command Default

12-hour format

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco SRST 2.0

This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 and Cisco 3600 series multiservice routers,
                                          						Cisco IAD2420 series IADs.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

## Examples

The following example shows the time format on the Cisco IP phones
                              		  being set to the 24-hour format:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# time-format 24
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified Survivable Remote Site Telephony
                                          						(SRST) support and enters call-manager-fallback configuration mode.

## timeouts busy (call-manager-fallback)

To set the timeout value for call transfers to busy destinations, use
                              		  the timeouts busy command in call-manager-fallback configuration mode. To return
                              		  to the default value, use the no form of this command.

timeouts busy seconds

no timeouts busy

### Syntax Description

seconds

Number of seconds after connection to a busy destination
                                          						before a transferred call is disconnected. Range is from 0 to 30 seconds.
                                          						Default is 10.

### Command Default

10 seconds

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(8)T

Cisco SRST 2.0

This command was introduced.

### Usage Guidelines

For calls that are transferred to busy destinations, this command
                              		  sets the amount of time after connection to the busy destination before the
                              		  call is disconnected.

Note that the timeout set by this command applies only to calls that
                              		  are transferred to busy destinations and not to calls that directly dial busy
                              		  destinations.

## Examples

The following example sets the ringing timeout to 10 seconds:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# timeouts busy 20
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified Survivable Remote Site Telephony
                                          						(SRST) and enters call-manager-fallback configuration mode.

## timeouts interdigit (call-manager-fallback)

To configure the interdigit timeout value for all Cisco IP phones
                              		  attached to a router, use the timeouts interdigit command in call-manager-fallback configuration mode. To return
                              		  the interdigit timeout value to its default, use the no form of this command.

timeouts interdigit seconds

no timeouts interdigit

### Syntax Description

seconds

Interdigit timeout duration, in seconds, for all Cisco IP
                                          						phones. Valid entries are integers from 2 to 120.

### Command Default

No default behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XB

Cisco SRST 1.0

This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers; Cisco IAD2420
                                          						series IADs; Cisco 7200 series routers.

12.2(2)XT

Cisco SRST 2.0

This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

### Usage Guidelines

The timeouts interdigit command specifies how long, in seconds,
                              		  the system waits after a caller enters the initial digit or a subsequent digit
                              		  of the dialed string. The interdigit timer is activated when the caller enters
                              		  a digit and is restarted each time the caller enters subsequent digits until
                              		  the destination address is identified. If the configured timeout value is
                              		  exceeded before the destination address is identified, a tone sounds and the
                              		  call is terminated.

## Examples

The following example sets the interdigit timeout value to 5 seconds
                              		  for all Cisco IP phones:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# timeouts interdigit 5
```

In this example, the 5 seconds refers to the elapsed time after which
                              		  an incompletely dialed number times out. For example, if you dial nine digits
                              		  (408555010) instead of the required ten digits (4085550100), you hear a busy
                              		  tone after the 5 “timeout” seconds have elapsed.

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified Survivable Remote Site Telephony
                                          						(SRST) support and enters call-manager-fallback configuration mode.

timeouts interdigit (voice port)

Configures the interdigit timeout value for a specified
                                          						voice port.

## timeouts ringing (call-manager-fallback)

To set the time before a disconnect code is returned on phones
                              		  without a call-forward no-answer configuration, use the timeouts ringing command in call-manager-fallback configuration mode. To disable
                              		  the time setting, use the no form of this command.

timeouts ringing seconds

no timeouts ringing

### Syntax Description

seconds

The duration, in seconds, for which a voice port allows
                                          						ringing to continue if a call is not answered. The range is from 5 to 60000.

### Command Default

No default behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

This mechanism protects against hung inbound calls through interfaces
                              		  that do not have forward disconnect supervision, such as Foreign Exchange
                              		  Office (FXO).

Expiration of the timeout causes incoming calls to return a
                              		  disconnect code to the caller.

## Examples

The following example sets the ringing timeout to 10 seconds:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# timeouts ringing 10
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified Survivable Remote Site Telephony
                                          						(SRST) and enters call-manager-fallback configuration mode.

## transfer max-length (voice register pool)

To specify the maximum length of the transfer number, use the transfer max-length command in voice register pool or voice
                              		  register template configuration mode. To disable the maximum length, use the no form of this command.

transfer max-length max-length

no transfer max-length max-length

### Syntax Description

max-length

Maximum length of the transfer number. Range is 3 to 16.

### Command Default

No maximum length is specified for the transfer number.

### Command Modes

Voice register pool configuration (config-register-pool)

Voice register template configuration ((config-register-temp)

## Command History

Release

Modification

15.3(2)T

This command was introduced.

### Usage Guidelines

The transfer max-length command is used to indicate the maximum length of the number
                              		  being dialed for a call transfer. When only a specific number of digits are to
                              		  be allowed during a call transfer, a value between 3 and 16 is configured.When
                              		  the number dialed exceeds the maximum length configured, then the call transfer
                              		  is blocked.

## Examples

The following example shows how to configure the maximum length of
                              		  the transfer number under voice register pool 1. Because the maximum length is
                              		  configured as 5, only call transfers to Cisco Unified SIP IP phones with a
                              		  five-digit directory number are allowed. All call transfers to directory
                              		  numbers with more than five digits are blocked.

```
Router# configure terminal
Router(config)# voice register pool 1
Router(config-register-pool)# transfer max-length 5
```

The following example shows how to configure the maximum length of
                              		  the transfer number for a set of phones under voice register template 2:

```
Router# configure terminal
Router(config)# voice register template 2
Router(config-register-temp)# transfer max-length 10
```

Command

Description

voice register pool

Enters voice register pool configuration mode and creates a
                                          						pool configuration for a SIP IP phone in Cisco Unified CME or for a set of SIP
                                          						phones in Cisco Unified SIP SRST

voice register template

Enters voice register template configuration mode and
                                          						defines a template of common parameters for SIP phones.

## transfer-digit-collect

To select the digit-collection method for consultative
                              		  call-transfers, use the transfer-digit-collect command in
                              		  telephony-service configuration mode for Cisco Unified CME or in
                              		  call-manager-fallback configuration mode for Cisco Unified SRST. To reset to
                              		  the default value, use the no form of this command.

transfer-digit-collect { new-call | orig-call }

no transfer-digit-collect

### Syntax Description

new-call

Dialed digits are collected from new call leg. Default
                                          						value.

orig-call

Dialed digits are collected from original call leg.

### Command Default

Digits are collected from the new consultative call-leg
                              		  ( new-call keyword).

### Command Modes

Telephony-service configuration (config-telephony)

Call-manager-fallback configuration (config-cm-fallback)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XZ

Cisco Unified CME 4.3 Cisco Unified SRST 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command specifies whether the dialed digits of the target number
                              		  are collected on the original call leg or on the new call leg that is created
                              		  when a phone user initiates a consultative call-transfer.

For consultative transfers, a local number is matched on the number command in ephone-dn configuration
                              		  mode; a PSTN number is matched on the transfer-pattern command in telephony service
                              		  mode.

The orig-call keyword selects the method used in
                              		  versions before Cisco Unified CME 4.3 and Cisco Unified SRST 4.3. After a phone
                              		  user presses the Transfer soft key, the dialed digits of the target number are
                              		  collected on the original call leg and buffered until either a local ephone-dn
                              		  or transfer-pattern is matched. When the transfer-to number is matched, the
                              		  original call is put on hold and an idle line or channel is seized to send the
                              		  dialed digits from the buffer.

The new-call keyword selects the default method
                              		  that is used in Cisco Unified CME 4.3 and later versions and Cisco Unified SRST
                              		  4.3 and later versions. The transfer-to digits are collected on a new
                              		  consultative call-leg that is created when the user presses the Transfer soft
                              		  key. The consultative call-leg is seized and the dialed digits are passed on
                              		  without being buffered until the digits are matched and the consultative
                              		  call-leg moves to the alerting state.

The new-call keyword is supported only if:

- The transfer-system full-consult command (default) is set in
                                 			 telephony-service configuration mode.

- The transfer-mode consult command (default) is set for
                                 			 transferor's directory number (ephone-dn).

- An idle line or channel is available for seizing, digit
                                 			 collection, and dialing.

A consultative transfer is one in which the transferring party either
                              		  connects the caller to a ringing phone (ringback heard) or speaks with the
                              		  third party before connecting the caller to the third party.

## Examples

The following example shows the digit-collection set to the method
                              		  used in versions before Cisco Unified CME 4.3 and Cisco Unified SRST 4.3:

```
Router(config)# telephony-service Router(config-telephony)# transfer-digit-collect orig-call
```

### Related Commands

Command

Description

transfer-mode

Specifies the type of call transfer for an individual
                                          						directory number that uses the ITU-T H.450.2 standard.

transfer-pattern (telephony-service)

Allows the transfer of calls to phones outside the local
                                          						Cisco Unified CME network.

transfer - system

Specifies the call transfer method for all IP phones on a
                                          						Cisco Unified CME router using the ITU-T H.450.2 standard.

## transfer-pattern

To allow Cisco IP
                              		  phones to transfer telephone calls from callers outside the local IP network to
                              		  another Cisco IP phone, use the transfer-pattern command in call-manager-fallback
                              		  configuration mode. To disable transfer of calls to other numbers, use the no form of
                              		  this command.

transfer-pattern transfer-pattern

no transfer-pattern

### Syntax Description

transfer-pattern

String
                                          						of digits for permitted call transfers. Wildcards are allowed.

### Command Default

This feature is
                              		  enabled.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						SRST 1.0

This
                                          						command was introduced on the following platforms: Cisco 2600 series and Cisco
                                          						3600 series multiservice routers, and Cisco IAD2420 series IADs.

12.2(2)XT

Cisco
                                          						SRST 2.0

This
                                          						command was implemented on Cisco 1750 and Cisco 1751 multiservice routers.

12.2(8)T

Cisco
                                          						SRST 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco
                                          						SRST 2.0

This
                                          						command was implemented on the Cisco 2600-XM and Cisco 2691 routers.

12.2(11)T

Cisco
                                          						SRST 2.01

This
                                          						command was integrated into Cisco IOS Release 12.2(11)T and implemented on the
                                          						Cisco 1760 routers.

### Usage Guidelines

The transfer-pattern command allows you to transfer a
                              		  call from a non-IP phone number to another Cisco IP phone on the same IP
                              		  network using the specified transfer pattern. By default, all Cisco IP phone
                              		  directory numbers or virtual voice ports are allowed as transfer targets.

When you define
                              		  transfers to nonlocal numbers, it is important to note that transfer-pattern
                              		  digit matching is performed before translation-rule operations. Therefore, you
                              		  should specify in this command the digits that are actually entered by phone
                              		  users before they are translated. For more information, see Enabling Digit
                                 			 Translation Rules section in the Cisco IOS Survivable
                                 			 Remote Site Telephony Version 3.3 System Administrator Guide .

## Examples

The following
                              		  example sets a transfer pattern:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# transfer-pattern 55501..
```

A maximum of 32
                              		  transfer patterns can be entered. In this example, 55501.. (the two decimal
                              		  points are used here as wildcards) permits transfers to any numbers in the
                              		  range from 555-0100 to 555-0199.

### Related Commands

Command

Description

call-manager-fallback

Enables
                                          						Cisco Unified Survivable Remote Site Telephony (SRST) support and enters
                                          						call-manager-fallback configuration mode.

## transfer-pattern blocked (voice register pool)

To block all call transfers for a specific Cisco Unified SIP IP phone
                              		  or a set of Cisco Unified SIP IP phone, use the transfer-pattern blocked command in voice register pool and voice
                              		  register template configuration mode. To allow call transfers, use the no form of this command.

transfer-pattern blocked

no transfer-pattern blocked

### Syntax Description

This command has no arguments or keywords.

### Command Default

Call transfers for a specific Cisco Unified SIP IP phone or a set of
                              		  Cisco Unified SIP IP phone are allowed.

### Command Modes

Voice register pool configuration (config-register-pool)

Voice register template configuration ((config-register-temp)

## Command History

Release

Modification

15.3(2)T

This command was introduced.

### Usage Guidelines

When the transfer-pattern blocked command is configured for a specific
                              		  phone, no call transfers are allowed from that phone over the trunk.

This feature forces unconditional blocking of all call transfers from
                              		  a specific phone to any other non-local numbers (external calls from one trunk
                              		  to another trunk). No call transfers from this specific phone are possible even
                              		  when a transfer pattern matches the dialed digits for transfer.

## Examples

The following example shows how to block all call transfers for voice
                              		  register pool 5:

```
Router(config)# voice register pool 5
Router(config-register-pool)# transfer-pattern ?
  blocked  global transfer pattern not allowed
Router(config-register-pool)# transfer-pattern blocked
```

The following example shows how to block all call transfers for a set
                              		  of Cisco Unified SIP IP phones defined by voice register template 9:

```
Router(config)# voice register template 9
Router(config-register-temp)# transfer-pattern ?
  blocked  global transfer pattern not allowed
Router(config-register-temp)# transfer-pattern blocked
```

### Related Commands

Command

Description

voice register pool

Enters voice register pool configuration mode and creates a
                                          						pool configuration for a Cisco Unified SIP IP phone in Cisco Unified CME or for
                                          						a set of Cisco Unified SIP IP phones in Cisco Unified SIP SRST.

voice register template

Enters voice register template configuration mode and
                                          						defines a template of common parameters for Cisco Unified SIP IP phones.

## transfer-system (call-manager-fallback)

To specify the call-transfer method for all IP phones on a Cisco
                              		  Unified Survivable Remote Site Telephony (SRST) router using the ITU-T H.450.2
                              		  standard, use the transfer-system command in
                              		  call-manager-fallback configuration mode. To disable the call-transfer method,
                              		  use the no form of this command.

transfer-system { blind | full-blind | full-consult | local-consult }

no transfer-system

### Syntax Description

blind

Transfers calls without consultation using a single phone
                                          						line and the Cisco proprietary method. The keyword blind is not recommended. Use
                                          						either the full- blind or full-consult keyword instead.

full-blind

Transfers calls without consultation using H.450.2 standard
                                          						methods.

full-consult

Transfers calls using H.450.2 with consultation using the
                                          						second phone line if available, or the calls fall back to full-blind if the
                                          						second line is unavailable.

local-consult

Transfers calls with local consultation using the second
                                          						phone line if available, or the calls fall back to blind for nonlocal
                                          						consultation or transfer target. This method is intended for use primarily in
                                          						VoFR networks because the Cisco VoFR call-transfer protocol does not support an
                                          						end-to-end transfer with consultation mechanism.

### Command Default

No default behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

Call transfers using the H.450.2 standard can be blind or
                              		  consultative. A blind transfer is one in which the transferring phone connects
                              		  the caller to a destination line before ringback begins. A consultative
                              		  transfer is one in which the transferring party either connects the caller to a
                              		  ringing phone (ringback heard) or speaks with the third party before connecting
                              		  the caller to the third party. When H.450.2 call transfer is selected using
                              		  the full-blind or full-consult keyword, the router must be configured with a Tool Command
                              		  Language (Tcl) script that supports the H.450.3 protocol. The Tcl script is
                              		  loaded on the Cisco Unified SRST router with the call application voice command.

## Examples

The following example sets full consultation as the call-transfer
                              		  method for this Cisco Unified SRST phone network:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# transfer-system full-consult
```

### Related Commands

Command

Description

call application voice

Defines an application, indicates the location of the
                                          						corresponding Tcl files that implement the application, and loads the selected
                                          						Tcl script.

call-manager-fallback

Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode.

## translate (call-manager-fallback)

To apply a translation rule to modify the phone number dialed or
                              		  received by any Cisco IP phone user during Cisco Unified Communications Manager
                              		  fallback, use the translate command in call-manager-fallback
                              		  configuration mode. To disable this feature, use the no form of this command.

translate { called | calling } translation-rule-tag

no translate { called | calling } translation-rule-tag

### Syntax Description

called

Translation rule to apply to the number called by a Cisco
                                          						IP phone.

calling

Translation rule to apply to the calling party number sent
                                          						in the call setup message for calls originated from a Cisco IP phone.

translation-rule-tag

Tag number by which the rule set is referenced. This is an
                                          						arbitrarily chosen number. The range is from 1 to 2147483647.

### Command Default

No default behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco SRST 2.0

This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, Cisco IAD2420 series IADs.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

### Usage Guidelines

The translate command allows you to apply a
                              		  previously configured number-translation rule to modify the number dialed or
                              		  received by a specific extension. Translation rules are a powerful
                              		  general-purpose number-manipulation mechanism that performs operations such as
                              		  automatically adding telephone area and prefix codes to dialed numbers.

## Examples

The following example applies translation rule 20 to the inbound
                              		  called number:

```
Router(config)# translation-rule 20 Router(config-translate)# rule 0 1234 2345 abbreviated Router(config-translate)# exit Router(config)# call-manager-fallback Router(config-cm-fallback)# translate called 20
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified Survivable Remote Site Telephony
                                          						(SRST) support and enters call-manager-fallback configuration mode.

translation-profile (call-manager-fallback)

Assigns a translation profile for incoming or outgoing call
                                          						legs on a Cisco IP phone.

translation-rule

Creates a translation name and enters translation-rule
                                          						configuration mode.

## translate-outgoing (voice register pool)

To allow an explicit setting of translation rules on the VoIP dial
                              		  peer in order to modify a phone number dialed by any Cisco IP phone user, use
                              		  the translate-outgoing command in voice register
                              		  pool configuration mode. To disable translation rules, use the no form of this command.

translate-outgoing { called | calling } rule-tag

no translate-outgoing { called | calling }

### Syntax Description

called

Called party requires translation.

calling

Calling party requires translation.

rule-tag

The rule-tag is an arbitrarily chosen number by which the
                                          						rule set is

referenced. The range is from 1 to 2147483.

### Command Default

None

### Command Modes

Voice register pool configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SIP SRST 3.0

This command was introduced.

12.3(4)T

Cisco SIP SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was added to Cisco CME.

### Usage Guidelines

Translation rules are a powerful general-purpose number-manipulation
                              		  mechanism that perform operations such as automatically adding telephone area
                              		  and prefix codes to dialed numbers. The translation rules are applied to VoIP
                              		  dial peers created by Cisco Unified Session Initiation Protocol (SIP)
                              		  Survivable Remote Site Telephony (SRST) or Cisco Unified Communications Manager
                              		  Express (Cisco Unified CME)

.

During registration, a dial peer is created, and that dial peer
                              		  includes a default translation rule. The translate-outgoing command allows you to
                              		  change the translation rule, if desired. The translate-outgoing command allows you to
                              		  select a preconfigured number translation rule to modify the number dialed by a
                              		  specific extension.

Translation rules must be set by using the translate-outgoing command before the alias command is configured in Cisco Unified
                              		  SIP SRST.

Configure the id (voice register pool) command before any other voice register
                              		  pool commands, including the translate-outgoing command. The id command identifies a locally available
                              		  individual SIP phone or set of SIP phones.

## Examples

## Examples

The following is partial sample output from the show running-config command showing that called-party 1
                              		  requires translation.

```
voice register pool 1
 id mac 0030.94C2.A22A
 preference 5
 cor incoming call91 1 91011
 translate-outgoing called 1
```

## Examples

The following is partial sample output from the show running-config command showing that called-party 1 requires translation.

```
voice register pool 1
 id mac 0030.94C2.A22A
 preference 5
 cor incoming call91 1 91011
 translate-outgoing called 1
 proxy 10.2.161.187 preference 1 monitor probe icmp-ping
 alias 1 94... to 91011 preference 8
 voice-class codec 1
```

### Related Commands

Command

Description

alias (voice register pool)

Allows Cisco SIP IP phones to handle inbound PSTN calls to
                                          						telephone numbers that are unavailable when the main proxy is not available.

id (voice register pool)

Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones.

translate-outgoing (dial-peer)

Applies a translation rule to manipulate dialed digits on
                                          						an outbound POTS or VoIP call leg.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## translation-profile (call-manager-fallback)

To assign a translation profile for incoming or outgoing call legs on
                              		  a Cisco IP phone, use the translation-profile command in
                              		  call-manager-fallback configuration mode. To delete the translation profile
                              		  from the voice port, use the no form of this command.

translation-profile { incoming | outgoing } name

no translation-profile { incoming | outgoing } name

### Syntax Description

incoming

Specifies that this translation profile handles incoming
                                          						calls.

outgoing

Specifies that this translation profile handles outgoing
                                          						calls.

name

Name of the translation profile.

### Command Default

No default behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)T

Cisco SRST 3.2

This command was introduced.

### Usage Guidelines

Cisco Unified Survivable Remote Site Telephony (SRST) 3.2 and later versions support
                              				translation profiles. Translation profiles allow you to group translation rules
                              				together and to associate translation rules with the following:

Called numbers

Calling numbers

Redirected called numbers

Use the translation-profile command to assign a global predefined translation profile to an
                              		  incoming or outgoing call leg. For example, a company number can be assigned to
                              		  overwrite an individual caller’s phone number. That is, the translation-profile command modifies the phone number dialed or received by a Cisco
                              		  IP phone user while in Communications Manager fallback mode.

Cisco IP phones support one incoming and one outgoing translation
                              		  profile when in SRST mode.

## Examples

The following example shows a configuration in which a translation
                              		  profile called name1 is created with two voice translation rules. Rule1
                              		  consists of associated calling numbers, and rule2 consists of redirected called
                              		  numbers. The Cisco IP phones in SRST mode are configured with name1.

```
voice translation-profile name1
 translation calling rule1
 translation called-direct rule2
call-manager-fallback
 translation-profile incoming name1
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco SRST support and enters call-manager-fallback
                                          						configuration mode.

show voice translation-profile

Displays the configuration of a translation profile.

translate (call-manager- fallback)

Applies a translation rule to modify the phone number
                                          						dialed or received by any Cisco IP phone user during Communications Manager
                                          						fallback.

translation-rule

Creates a translation name and enters translation-rule
                                          						configuration mode to apply rules to the translation name.

voice translation-profile

Defines a translation profile for voice calls.

## translation-profile (voice register)

To apply a translation profile to incoming or outgoing call legs on a
                              		  SIP phone in a Cisco Unified SRST system, use the translation - profile command in voice register dn or voice register pool configuration mode. To
                              		  remove the translation profile, use the no form of this command.

translation-profile { incoming | outgoing } name

no translation-profile { incoming | outgoing }

### Syntax Description

incoming

Specifies that this translation profile handles incoming
                                          						calls.

outgoing

Specifies that this translation profile handles outgoing
                                          						calls.

name

Name of the translation profile.

### Command Default

Translation profile is not assigned to call legs on the phone.

### Command Modes

Voice register dn configuration (config-register-dn) Voice register pool configuration (config-register-pool)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(22)YB

Cisco Unified SIP SRST 7.1

This command was introduced.

12.4(24)T

Cisco Unified SIP SRST 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

Cisco IOS XE Dublin
                                                17.10.1a

Unified SRST 14.3

Introduced support for YANG models.

### Usage Guidelines

This command assigns a predefined translation profile to incoming or
                              		  outgoing call legs to and from the Cisco Unified SRST router. Use this command
                              		  to apply the translation profile to a specific directory number or to all
                              		  directory numbers on a SIP phone. The translation profile that you assign is
                              		  created by using the voice translation-profile command.

## Examples

The following example assigns the translation profile named
                              		  “profile1” to handle translation of outgoing calls from SIP phone 21:

```
Router(config)# voice register pool 21 Router(config-register-pool)# translation-profile outgoing profile1
```

The following example assigns the translation profile named
                              		  “profile2” to handle translation of incoming calls to extension 1200:

```
Router(config)# voice register dn 12 Router(config-register-pool)# number 1200 Router(config-register-pool)# translation-profile incoming profile2
```

### Related Commands

Command

Description

show voice translation-profile

Displays the configuration of a translation profile.

translate (translation profiles)

Assigns a translation rule to a translation profile.

voice translation-profile

Defines a translation profile for voice calls.

## transport-tcp-tls
                        	 (call-manager-fallback)

To configure a specific TLS version for Unified Secure SCCP SRST, use the transport-tcp-tls command in call-manager-fallback configuration mode. To enable the default command configuration, use the no form of this command.

To set default value which supports all TLS versions, use the default form of this command.

transport-tcp-tls { v1.0 | v1.1 | v1.2 [ sha2 ]
                              							
                              							 | v1.3 [ sha2 ]
                              							
                              						}

no transport-tcp-tls { v1.0 | v1.1 | v1.2 [ sha2 ]
                              							
                              							 | v1.3 [ sha2 ]
                              							
                              						}

default transport-tcp-tls

## Syntax Description

Enables TLS version 1.0.

In the Cisco IOS XE 17.18.2 release, a security warning message appears for configurations using TLS versions below 1.2 and associated weaker ciphers.
                                                   For secure configurations, we recommend configuring stronger ciphers with TLS version 1.2 or higher.

Starting from Cisco IOS XE 26.1.1 release, the insecure TLS versions (1.0, 1.1) and associated ciphers are not supported in default configurations. However,
                                       insecure configurations are supported in system mode insecure operation-mode.

Enables TLS version 1.1.

In the Cisco IOS XE 17.18.2 release, a security warning message appears for configurations using TLS versions below 1.2 and associated weaker ciphers.
                                                   For secure configurations, we recommend configuring stronger ciphers with TLS version 1.2 or higher.

Starting from Cisco IOS XE 26.1.1 release, the insecure TLS versions (1.0, 1.1) and associated ciphers are not supported in default configurations. However,
                                       insecure configurations are supported in system mode insecure operation-mode.

Enables TLS version 1.2.

Enables TLS version 1.3.

Enables SHA2 ciphers with TLS version 1.2 or 1.3.

### Command Default

In the default form, all the TLS versions except TLS 1.0 are supported for this CLI command.

### Command Modes

call-manager-fallback Configuration (config-cm-fallback)

## Command History

Cisco IOS XE 26.1.1

Unified SRST 15.0

The insecure TLS versions (1.0, 1.1) and associated ciphers are not supported in default configurations. However, insecure
                                       configurations are supported in system mode insecure operation-mode.

Cisco IOS XE 17.18.2

Unified SRST 15.0

Security warnings for usage of legacy TLS and associated weaker ciphers.

Cisco IOS XE 17.14.1a

Unified SRST 14.4

This command is enhanced to support TLS version 1.3 ciphers. In addition, SHA2 cipher support for TLS version 1.3 is introduced.

Introduced support for YANG model.

Cisco IOS XE Cupertino
                                             17.8.1a

Unified SRST 14.2

This command is enhanced to limit TLS1.2 to using SHA2 ciphers only.

Cisco IOS XE Fuji 16.9.1

Unified SRST 12.3

This command was introduced.

### Usage Guidelines

Use the transport-tcp-tls command to define the version of transport layer security for the Secure SCCP Unified SRST.

From Unified SRST 12.3 and later releases, TLS versions 1.1 and 1.2 are supported for Analog Voice Gateways on Unified SRST.
                              SCCP phones only support TLS version 1.0.

Starting from Unified SCCP SRST 14.4 release, TLS version 1.3 is supported for Cisco VG400, VG410, VG420, and VG450 Analog
                              Voice Gateways.

When transport-tcp-tls is configured without specifying a version, the default behavior of the CLI command is enabled. In the default form, all
                              the TLS versions (1.3, 1.2, and 1.1) are supported.

For Secure SIP and Secure SCCP endpoints that do not support TLS version 1.2, you need to configure TLS 1.0 for the endpoints
                              to register to Unified Secure SRST 12.3 (Cisco IOS XE Fuji Release 16.9.1). This also means that endpoints which support 1.2
                              will also use the 1.0 suites.

For TLS 1.0 support on Cisco IOS XE Fuji Release 16.9.1 for SCCP endpoints, you need to specifically configure:

transport-tcp-tls v1.0 under call-manager-fallback configuration mode

From Cisco IOS XE Cupertino
                                    17.8.1a onwards, the transport-tcp-tls v1.2 command is enhanced to allow only SHA2 ciphers by using the additional "sha2" keyword.

Starting from Cisco IOS XE 17.14.1a , TLS version 1.3 is supported in addition to TLS versions 1.0, 1.1 and 1.2. It is recommended that TLS version 1.2 or 1.3
                              is used wherever possible to ensure security or compliance. To configure exclusivity, use the transport-tcp-tls version command.

Also from Cisco IOS XE 17.14.1a , the transport-tcp-tls v1.3 command supports SHA2 ciphers by using the additional "sha2" keyword. If SHA2 ciphers are configured, media packets are encrypted
                              and sent using the AEAD_AES_256_GCM SRTP cipher suite.

Starting from Cisco IOS XE 17.18.2 release, a security warning message appears for configurations using TLS versions below 1.2 and associated weaker ciphers.
                              For secure configurations, we recommend configuring stronger ciphers with TLS version 1.2 or higher. The security warning
                              message is displayed for the no form of the command configuration as it sets to default value which supports all TLS versions.

Starting from Cisco IOS XE 26.1.1 release, the insecure TLS versions (1.0, 1.1) and associated ciphers are not supported in default configurations. However,
                              insecure configurations re supported in system mode insecure operation-mode.

## Examples

The following example shows how to specify a TLS version for a secure SCCP phone using the transport-tcp-tls command:

```
Device(config)# call-manager-fallback Device(config-cm-fallback)# transport-tcp-tls ? v1.0  Enable TLS Version 1.0
  v1.1  Enable TLS Version 1.1
  v1.2  Enable TLS Version 1.2
  v1.3  Enable TLS Version 1.3
```

## Examples

```
Device(config-cm-fallback)#transport-tcp-tls v1.2 ?
  sha2  Allow SHA2 ciphers only
  <cr>  <cr>
Device(config-cm-fallback)#transport-tcp-tls v1.2 sha2 ?
  <cr>  <cr>
```

## Examples

```
Device(config-cm-fallback)#transport-tcp-tls v1.3 ?
  sha2  Allow SHA2 ciphers only
  <cr>  <cr>
Device(config-cm-fallback)#transport-tcp-tls v1.3 sha2 ?
  <cr>  <cr>
```

## Examples

The following example shows command configuration in insecure mode displaying warning message:

```
Device# configure terminal Device(config)# system insecure mode Device(config)# call-manager-fallback Device(config-cm-fallback)# transport-tcp-tls v1.0 SECURITY WARNING - Module: CALLMANAGER, Command: transport-tcp-tls v1.0 , Reason: Weak tls version, 
Description: Call manager fallback configured with weak TLS version 1.0 or 1.1 - deprecated and vulnerable, 
Remediation: Use stronger tls version to enhance security
Router(config-cm-fallback)#
```

## Examples

The following example shows command configuration in secure mode displaying error message:

```
Device(config-cm-fallback)# transport-tcp-tls v1.1 %Error:Insecure configurations are not permitted in secure mode. To proceed, set the system mode to 
insecure using the command system mode insecure, and then try again.
Module: CALLMANAGER, Command: transport-tcp-tls v1.1 , Reason: Weak tls version, Remediation: Use stronger 
tls version to enhance security
%ERROR: Security policy check failed, configuration can't be applied
```

## Examples

The following example illustrates a security warning message display for configurations using TLS versions below 1.2 and associated
                              weaker ciphers:

```
Device(config-cm-fallback)# transport-tcp-tls v1.0 SECURITY WARNING - Module: CALLMANAGER, Command: transport-tcp-tls v1.0 , Reason: Weak tls version, 
Remediation: Use stronger tls version to enhance security

Device(config-cm-fallback)# do sh run | sec call-manager-fallback call-manager-fallback
 transport-tcp-tls v1.0
 max-conferences 8 gain -6
 transfer-system full-consult
 ip source-address 10.10.10.239 port 2000
 max-ephones 30
 max-dn 30
```

## Examples

The following example illustrates a security warning message display for default configurations:

```
CSR_CUBE(config-cm-fallback)# no transport-tcp-tls removing transport-tcp-tls  will set to default value which supports all tls versions

SECURITY WARNING - Module: CALLMANAGER, Command: no transport-tcp-tls , Reason: Weak tls version, 
Remediation: Use stronger tls version to enhance security

CSR_CUBE(config-cm-fallback)# do sh run all | sec call-manager-fallback call-manager-fallback
 encrypt password
 transport-tcp-tls
 max-conferences 8 gain -6
 transfer-digit-collect new-call
 transfer-system full-consult
 log table retain-timer 15
 log table max-size 150
 user-locale US
 user-locale 1 US
 user-locale 2 US
 user-locale 3 US
 user-locale 4 US
 limit-dn 7914 76
 limit-dn 7915-12 76
 limit-dn 7915-24 76
 limit-dn 7916-12 76
 limit-dn 7916-24 76
 limit-dn 12SP 76
 limit-dn 7902 76
 limit-dn 7905 76
 limit-dn 7906 76
 limit-dn 7910 76
```

### Related Commands

Command

Description

Defines
                                          						the default transport type supported by a new phone.

## trustpoint (credentials)

To specify the name of the trustpoint to be associated with a Cisco
                              		  Unified Communications Manager Express (Cisco Unified CME) CTL provider
                              		  certificate or with the Cisco Unified Survivable Remote Site Telephony (SRST)
                              		  router certificate, use the trustpoint command in credentials configuration mode. To change the
                              		  specified trustpoint, use the no form of this command.

trustpoint trustpoint-name

no trustpoint

### Syntax Description

trustpoint-name

Name of the trustpoint to be associated with the Cisco
                                          						Unified CME CTL provider certificate or the Cisco Unified SRST device
                                          						certificate.

### Command Default

No default behavior or values.

### Command Modes

Credentials configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco SRST 3.3

This command was introduced for Cisco Unified SRST.

12.3(14)T

Cisco Unified CME 4.0

This command was introduced for Cisco Unified CME.

### Usage Guidelines

Cisco Unified CME

This command is used with Cisco Unified CME phone authentication to
                              		  define the trustpoint for the CTL provider. This trustpoint will be used for
                              		  TLS sessions with the CTL client.

Cisco Unified SRST

The name of the trustpoint must be consistent with the trustpoint
                              		  name of the Cisco Unified SRST router.

## Examples

## Examples

The following example sets up a CTL provider on the Cisco Unified CME
                              		  router with the IP address 172.19.245.1.

```
Router(config)# credentials Router(config-credentials)# ip source-address 172.19.245.1 port 2444 Router(config-credentials)# trustpoint ctlpv Router(config-credentials)# ctl-service admin user4 secret 0 c89L8o
```

## Examples

The following example enters credentials configuration mode, sets the
                              		  IP source address and port, and specifies the trustpoint:

```
Router(config)# credentials Router(config-credentials)# ip source-address 10.6.21.4 port 2445 Router(config-credentials)# trustpoint srstca
```

### Related Commands

Command

Description

credentials

Provides the Cisco Unified CME CTL provider certificate or
                                          						the Cisco Unified SRST router certificate and enters credentials configuration
                                          						mode.

ctl-service admin

Specifies a user name and password to authenticate the CTL
                                          						client during the CTL protocol.

debug credentials

Sets debugging on the credentials service.

ip source-address (credentials)

Enables the router to receive messages through the
                                          						specified IP address and port.

show credentials

Displays the credentials settings.

## user-locale (call-manager-fallback)

To set the language by country for displays on the Cisco Unified IP
                              		  Phone 7905G, Cisco Unified IP Phone 7912G, Cisco UnifiedIP Phone 7940G and
                              		  Cisco UnifiedIP Phone 7960G, use the user-locale command in call-manager-fallback
                              		  configuration mode. To disable the country selection and use the default
                              		  country (United States), use the no form of this command.

user-locale country-code

no user-locale country-code

### Syntax Description

country-code

The following ISO-3166 codes are available to Cisco Unified
                                          						Survivable Remote Site Telephony (SRST) systems running under Cisco Unified
                                          						Communications Manager V3.2 or later:

- DE —German.

- DK —Danish.

- ES —Spanish.

- FR —French.

- IT —Italian.

- JP —Japanese Katakana (available
                                             						  under Cisco Unified Communications Manager V4.0 or later).

- NL —Dutch.

- NO —Norwegian.

- PT —Portuguese.

- RU —Russian.

- SE —Swedish.

- US —United States English
                                             						  (default).

### Command Default

The default country code is US (United States).

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(11)YT

Cisco SRST 2.1

This command was introduced for use on the Cisco IP Phone
                                          						7940 and Cisco IP Phone 7960 for Cisco SRST systems running Cisco
                                          						Communications Manager V3.2. Support includes country codes for France,
                                          						Germany, Italy, Portugal, Spain, and the United States (default).

12.3(4)T

Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.3(7)XL

Cisco SRST 3.1.1

The JP keyword was added, providing support
                                          						for Japanese Katakana.

12.3(11)T

Cisco SRST 3.2

This command was integrated into Cisco IOS Release
                                          						12.3(11)T and support was increased to include the Cisco Unified IP Phone 7905G
                                          						and Cisco Unified IP Phone 7912G.

### Usage Guidelines

Japanese Katakana is now supported with the JP keyword and is available to Cisco
                              		  Unified SRST systems running under Cisco Unified Communications Manager V4.0.
                              		  All other country-code options are available to Cisco
                              		  Unified SRST systems running under Cisco Unified Communications Manager V3.2.
                              		  Systems running Cisco Unified Communications Manager prior to V3.2 can use only
                              		  the default country, United States ( US ).

## Examples

The following example shows how to set the user locale to the
                              		  ISO-3166 code for Spain:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# user-locale ES
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode.

## url-button

To configure
                              		  service url feature button on a line key, use the url-button command in ephone-template mode. To disable the service url
                              		  feature button configuration on a line key, use the no form of
                              		  this command.

{ url-button index type | url [ name ]}

{ no url-button index type | url [ name ]}

### Syntax Description

index

Unique
                                          						index number. Range: 1 to 8.

type

Type of
                                          						service url button. Following types of url service buttons are available:

- myphoneapp: My phone
                                             						  application configured under phone user interface.

- em: Extension Mobility

- snr: Single Number Reach

- voicehuntgroups: Voice Hunt
                                             						  Groups

- park-list: Displays list of
                                             						  parked calls

url
                                          						name

Service
                                          						url with maximum length of 31 characters.

### Command Default

By default,
                              		  URL-button configuration on a line key is disabled.

### Command Modes

Ephone template configuration (config-ephone-template)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.1(3)T

Cisco
                                          						Unified Enhanced SRST 8.5

This
                                          						command was introduced.

15.4(3)M

Cisco
                                          						Unified Enhanced SRST 10.5

This
                                          						command was modified.

### Usage Guidelines

Use this command
                              		  to configure a url-button on a phone’s line key.You can configure a line key to
                              		  function as one of the following url-button types: extension mobility (EM), My
                              		  Phone Apps, or single number reach (SNR). You can also configure a line button
                              		  to function as a service url by configuring a url name of a maximum length of
                              		  31 characters.

## Examples

The following
                              		  examples shows three url buttons configured as line keys:

```
!
telephony-service
 max-ephones 25
 max-conferences 12 gain -6
 transfer-system full-consult
!
!
ephone-template  5
 url-button 1 em
 url-button 2 mphoneapp 
 url-button 3 snr
!
ephone-template 6
conference drop-mode never
conference add-mode all
conference admin: No
max-calls-per-button 8
busy-trigger-per-button 0
privacy default
url-button 1 em
url-button 2 www.cisco.com www.cisco.com
url-button 3 snr
url-button 4 help help
url-button 7 myphoneapp
!
!
```

### Related Commands

Command

Description

show telephony-service ephone-template

Displays the contents of all the ephone-templates defined.

## utf8

To define Unicode UTF-8 support for a phone type, use the utf8 command in ephone-type configuration mode. To reset to the
                              		  default value, use the no form of this command.

utf8

no utf8

### Syntax Description

This command has no arguments or keywords.

### Command Default

Phone type supports Unicode UTF-8.

### Command Modes

Ephone-type configuration (config-ephone-type)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XZ

Cisco Unified CME 4.3 Cisco Unified SRST 4.3

This command was introduced.

### Usage Guidelines

This command specifies whether Unicode UTF-8 is supported by the type
                              		  of phone that is being added with the phone-type template.

## Examples

The following example shows that UTF-8 support is set to disabled for
                              		  the Nokia E61 when creating the ephone-type template:

```
Router(config)# ephone-type E61 Router(config-ephone-type)# no utf8
```

### Related Commands

Command

Description

device-id

Specifies the device ID for a phone type.

type

Assigns the phone type to an SCCP phone.

## vad (voice register pool)

To enable voice activity detection (VAD) on a VoIP dial peer, use the vad command in voice register pool
                              		  configuration mode. To disable VAD, use the no form of this command.

vad

no vad

### Syntax Description

This command has no arguments or keywords.

### Command Default

Enabled

### Command Modes

Voice register pool configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

### Usage Guidelines

VAD detects periods of silence in the voice signal and temporarily
                              		  discontinues transmission of the signal during these periods to save bandwidth.
                              		  Because VAD is enabled by default, there is no comfort noise during periods of
                              		  silence. As a result, the call may seem to be disconnected and you may prefer
                              		  to set no vad on the SIP phone pool.

## Examples

The following example shows how to disable VAD for pool 1:

```
Router(config)# voice register pool 1 Router(config-register-pool)# no vad
```

### Related Commands

Command

Description

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## video (call-manager-fallback)

To enter video configuration mode for a Cisco Unified SRST router,
                              		  use the video command in call-manager-fallback
                              		  configuration mode. To reset global video parameters, use the no form of this command.

video

no video

### Syntax Description

This command has no arguments or keywords.

### Command Default

Global video parameters are configured.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified SRST 4.0

This command was introduced.

### Usage Guidelines

Use the video command to enter video configuration
                              		  mode and set video parameters for all applicable Cisco IP phones in a Cisco
                              		  Unified SRST system.

## Examples

The following example shows how to enter video configuration mode for
                              		  a Cisco Unified SRST system. You must enter video configuration mode to set
                              		  video parameters, such as maximum bit rate.

```
Router(config)# call-manager-fallback Router(config-call-manager-fallback)# video Router(conf-cm-fallback-video)# maximum bit-rate 256
```

### Related Commands

Command

Description

show call active video

Displays call information for SCCP video calls in progress.

show call history video

Displays call history information for SCCP video calls.

video (telephony-service)

Enters video configuration mode to set video parameters for
                                          						all applicable Cisco IP phones associated with a Cisco Unified CME router.

## vm-integration

To enter voice-mail integration configuration mode and enable
                              		  voice-mail integration with dual tone multifrequency (DTMF) and analog
                              		  voice-mail systems, use the vm-integration command in global configuration mode. To disable voice-mail
                              		  integration, use the no form of this command.

vm-integration

no vm-integration

### Syntax Description

This command has no arguments or keywords.

### Command Default

No voice-mail integration is defined.

### Command Modes

Global configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(11)YT

Cisco SRST 2.1

This command was introduced for Cisco Survivable Remote
                                          						Site Telephony (SRST).

12.2(2)XT

Cisco CME 2.0

This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series, Cisco 3600 series, and Cisco IAD2420
                                          						series.

12.2(8)T

Cisco CME 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745.

12.2(8)T1

Cisco CME 2.0

This command was implemented on the Cisco 2600XM and Cisco
                                          						2691.

12.2(11)T

Cisco CME 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760.

### Usage Guidelines

The vm-integration command is used to enter
                              		  voice-mail integration configuration mode. Use voice-mail integration
                              		  configuration mode to integrate a Cisco Unified Communications Manager Express
                              		  (Cisco Unified CME) system with an analog voice-mail system.

## Examples

The following example shows how to enter the voice-mail integration
                              		  configuration mode:

```
Router(config) vm-integration Router(config-vm-integration) pattern direct 2 CGN *
```

### Related Commands

Command

Description

pattern direct (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when a user presses the Messages button on a
                                          						phone.

pattern ext-to-ext busy (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension reaches a busy
                                          						extension and the call is forwarded to voice mail.

pattern ext-to-ext no-answer (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail.

pattern trunk-to-ext busy (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail.

pattern trunk-to-ext no-answer (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail.

## voice class tls-cipher

To configure an ordered set of TLS cipher suites, use the voice class tls-cipher command. To disable this command or revert to default, use the no form of this command.

voice class tls-cipher tag

no voice class tls-cipher tag

tag

Voice class tls-cipher tag.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config).

Release

Modification

Cisco IOS XE Cupertino
                                             17.8.1a

Introduced voice class tls-cipher command.

Cisco IOS XE Dublin
                                             17.10.1a

Introduced support for YANG models.

### Usage Guidelines

The voice class tls-cipher command enables voice class configuration mode on the router, allowing you to configure an ordered list of TLS cipher suites.

## Examples

```
Router(config)#voice class tls-cipher 123
Router(config-class)# cipher ?
    <1-10>  Set the preference order for the cipher-suite (1 = Highest)
	
Router(config-class)#cipher 1 ?
DHE_RSA_AES128_GCM_SHA256      supported in TLS 1.2 & above
DHE_RSA_AES256_GCM_SHA384      supported in TLS 1.2 & above
DHE_RSA_WITH_AES_128_CBC_SHA   supported in TLS 1.0 & above
DHE_RSA_WITH_AES_256_CBC_SHA   supported in TLS 1.0 & above
ECDHE_ECDSA_AES128_GCM_SHA256  supported in TLS 1.2 & above
ECDHE_ECDSA_AES256_GCM_SHA384  supported in TLS 1.2 & above
ECDHE_RSA_AES128_GCM_SHA256    supported in TLS 1.2 & above
ECDHE_RSA_AES256_GCM_SHA384    supported in TLS 1.2 & above
RSA_WITH_AES_128_CBC_SHA       supported in TLS 1.0 & above
RSA_WITH_AES_256_CBC_SHA       supported in TLS 1.0 & above

Router(config-class)# cipher 1 CIPHER_SUITE_ECDHE_RSA_AES256_GCM_SHA384 ?
<cr>   <cr>
Router(config-class)#
```

## voice class tls-profile

To enable voice class configuration mode, and assign an identification tag for a TLS profile, use the command voice class tls-profile in global cofiguration mode. To remove a tls-profile, use the no form of this command.

no voice class tls-profile tag

### Syntax Description

tag

A number used to identify voice class tls profile.

The range is 1-10000.

There is no default value.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

Cisco IOS XE Cupertino
                                                17.8.1a

tls-profile command is enhanced to include <tag>.

This command was introduced.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

The command voice class tls-profile enables voice class configuration mode on the router and provides you sub-options to configure commands required for a TLS
                              session. This command allows you to configure under voice class, the options that can be configured at the global level via
                              sip-ua.

The tag associates all the voice class configurations that are made through the command voice class tls-profile tag to the command crypto signaling . Following is the crypto signaling command with tls-profile tag :

crypto signaling { remote-addr ip address subnet mask | default } tls-profile tag

For more information on the updates to the command crypto signaling , see crypto signaling .

## Examples

The following example configures the voice class tls-profile with tag '2' and enables voice class cofiguration mode:

```
Router(config)#voice class tls-profile 2
Router(config-class)#
```

The following section provides details of the sub-commands that can be configured under the command voice class tls-profile tag .

The following example configures CUBE to use the trustpoint trustpoint-name keyword and argument when it establishes or accepts the TLS connection with a remote device:

```
Router(config-class)#trustpoint CUBETP
```

The following example configures client verification trustpoint:

```
Router(config-class)#client-vtp TPname
```

The following example indicates the description for the TLS profile group:

```
Router(config-class)#description tlsgroupname
```

The following example configures the specific size of elliptic curves to be used for a TLS session:

```
Router(config-class)#cipher ecdsa-cipher curve-size 384
```

The following example configures CUBE to perform server identity validation through Common Name (CN) and Subject Alternate Name (SAN) fields in the server certificate:

```
Router(config-class)#cn-san-validate server
```

The following example enables Server Name Indication (SNI) required during the initial TLS handshake process:

```
Router(config-class)#sni send
```

The following example shows cipher command. The command associates a TLS cipher list with this profile.

tls-cipher should be created before adding to tls-profile .

To configure tls-cipher :

```
Router#configure terminal 
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#voice class tls-cipher 1122
Router(config-class)#? 
VOICECLASS configuration commands:
  cipher  Configure a TLS cipher-suite
  exit    Exit from voice class configuration mode
  help    Description of the interactive help system
  no      Negate a command or set its defaults

Router(config-class)#cipher ?
  <1-10>  Set the preference order for the TLS cipher-suite (1 = Highest)

Router(config-class)#cipher 1 ?
  DHE_RSA_AES128_GCM_SHA256        supported in TLS 1.2 & above
  DHE_RSA_AES256_GCM_SHA384        supported in TLS 1.2 & above
  DHE_RSA_WITH_AES_128_CBC_SHA     supported in TLS 1.0 & above
  DHE_RSA_WITH_AES_256_CBC_SHA     supported in TLS 1.0 & above
  ECDHE_ECDSA_AES128_GCM_SHA256    supported in TLS 1.2 & above
  ECDHE_ECDSA_AES256_GCM_SHA384    supported in TLS 1.2 & above
  ECDHE_RSA_AES128_GCM_SHA256      supported in TLS 1.2 & above
  ECDHE_RSA_AES256_GCM_SHA384      supported in TLS 1.2 & above
  RSA_WITH_AES_128_CBC_SHA         supported in TLS 1.0 & above
  RSA_WITH_AES_256_CBC_SHA         supported in TLS 1.0 & above

Router(config-class)#cipher 1 ECDHE_RSA_AES256_GCM_SHA384 ?
  <cr>  <cr>

GW1-2A(config-class)#cipher 1 ECDHE_RSA_AES256_GCM_SHA384 
GW1-2A(config-class)#
```

To configure tls-profile :

```
Router(config-class)#
Router(config-class)#voice class tls-profile 3344
Router(config-class)#?
VOICECLASS configuration commands:
  cipher       Configure a cipher-suite
  client-vtp   Assign a client verification trustpoint
  cn-san       Configure CN/SAN certificate options
  description  Description of the tls-profile group
  exit         Exit from voice class configuration mode
  help         Description of the interactive help system
  no           Negate a command or set its defaults
  sni          Enable TLS SNI (Server Name Indication) Extension
  trustpoint   Associate a trustpoint
Router(config-class)#ciph
Router(config-class)#cipher ?
  <1-10000>      Specify tls-cipher list tag
  ecdsa-cipher   Configure ECDSA ciphers
  strict-cipher  Configure ciphers mandated by SIP standards

Router(config-class)#cipher 1122 ?
  <cr>  <cr>

Router(config-class)#cipher 1122
```

To show tls-profile :

```
Router#show run | sec voice class tls-profile 3344
voice class tls-profile 3344
 cipher 1122
```

To show tls-cipher :

```
Router#show run | sec voice class tls-cipher 1122
voice class tls-cipher 1122
 cipher 1 ECDHE_RSA_AES256_GCM_SHA384
```

To show tls-profile under sip-ua :

```
Router# configure terminal 
Router(config)# sip-ua
Router (config-sip-ua)#
 crypto signaling default tls-profile 3344
```

### Related Commands

Command

Description

trustpoint

Creates a trustpoint to store the devices certificate that is generated as part of the enrollment process using Cisco IOS
                                          public-key infrastructure (PKI) commands.

Provides a description for the TLS profile group.

client-vtp

Assigns a client verification trustpoint.

cipher

Configures cipher setting.

cn-san

Enables server identity validation through Common Name (CN) and Subject Alternate Name (SAN) fields in the server certificate
                                          during client-side SIP /TLS connections

sni send

Enables TLS Server Name Indication (SNI) during the initial TLS handshake process.

crypto signaling

Identifies the trustpoint or the tls-profile tag that is used during the TLS handshake process.

## voice emergency response location

To create a tag for identifying an emergency response location (ERL)
                              		  for E911 services, use the voice emergency response location command in global configuration mode. To
                              		  remove the ERL tag, use the no form of this command.

voice emergency response location tag

no voice emergency response location tag

### Syntax Description

tag

Unique number that identifies this ERL tag.

### Command Default

No ERL tag is created.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)T

Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1

This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only.

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

Address and name commands introduced under voice emergency response location command. This command was added
                                          						for Cisco Unified CME.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command creates an ERL that identifies an area where emergency
                              		  teams can quickly locate a 911 caller. The ERL definition optionally includes
                              		  which ELINs are associated with the ERL and which IP phones are located in the
                              		  ERL. You can define two or fewer unique IP subnets and two or fewer ELINs. If
                              		  you define one ELIN, this ELIN is always used for phones calling from this ERL.
                              		  If you define two ELINs, the system alternates between using each ELIN. If you
                              		  define zero ELINs and phones use this ERL, the outbound calls do not have their
                              		  calling numbers translated. The PSAP sees the original calling numbers for
                              		  these 911 calls. You can optionally add the civic address using the address command and an address description
                              		  using the name command.

## Examples

In the following example, all IP phones with the IP address of
                              		  10.X.X.X or 192.168.X.X are automatically associated with this ERL. If one of
                              		  the phones dials 911, its extension is replaced with 408 555-0100 before it
                              		  goes to the PSAP. The PSAP will see that the caller’s number is 408 555-0100.
                              		  The civic address, 410 Main St, Tooly, CA, and a descriptive identifier, Bldg 3
                              		  are included.

```
voice emergency response location 1
 elin 1 4085550100
 subnet 1 10.0.0.0 255.0.0.0
 subnet 2 192.168.0.0 255.255.0.0
 address 1,408,5550100,410,Main St.,Tooly,CA
 name Bldg 3
```

### Related Commands

Command

Description

address

Specifies a comma separated text entry (up to 250
                                          						characters) of an ERL’s civic address.

elin

Specifies a PSTN number that will replace the caller’s
                                          						extension.

name

Specifies a string (up to 32-characters) used internally to
                                          						identify or describe the emergency response location.

subnet

Defines which IP phones are part of this ERL.

## voice emergency response settings

To define 911 call behavior settings, use the voice emergency response settings command in global configuration mode. To
                              		  remove the settings, use the no form of this command.

voice emergency response settings

no voice emergency response settings

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command enables definition of several 911 of the following call
                              		  behavior settings:

- elin : Default ELIN to use if a 911
                                 			 caller’s IP phone’s address does not match the subnet of any location in any
                                 			 zone.

- expiry : Number of minutes a 911 call is
                                 			 associated to an ELIN in case of a call back from the 911 operator.

- callback : Default number to contact if a
                                 			 911 call back cannot find the last 911 caller.

- logging : Syslog informational message
                                 			 that is printed to the console each time an emergency call is made. This
                                 			 feature is enabled by default, however you can disable this feature by entering
                                 			 the no form of this command.

## Examples

In the following example, if the 911 caller’s IP phone address does
                              		  not match any of the voice emergency response locations, the ELIN defined in
                              		  the voice emergency response settings configuration (4085550101) is used. After
                              		  the 911 call is placed to the PSAP, the PSAP has 120 minutes (2 hours) to call
                              		  back 408 555-0101 to reach the 911 caller. If during a call back, the last
                              		  caller’s extension number cannot be found, the call is routed to extension
                              		  7500. The outbound 911 calls do not cause a syslog message to the logging
                              		  facility (for example, to the local buffer, console, or remote host).

```
voice emergency response settings
callback 7500
elin 4085550101
expiry 120
no logging
```

### Related Commands

Command

Description

callback

Default phone number to contact if a 911 callback cannot
                                          						find the last 911 caller from the ERL.

elin

E.164 number used as the default ELIN if no matching ERL to
                                          						the 911 caller’s IP phone address is found.

expiry

Number of minutes a 911 call is associated to an ELIN in
                                          						case of a callback from the 911 operator.

logging

Syslog informational message printed to the console every
                                          						time an emergency call is made.

## voice emergency response zone

To create an emergency response zone, use the voice emergency response zone command in global configuration mode. To
                              		  remove the defined voice emergency response zone, use the no form of this command.

voice emergency response zone tag

no voice emergency response zone tag

### Syntax Description

tag

Identifier (1-100) for the voice emergency response zone.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command creates voice emergency response zones that allow
                              		  routing of 911 calls to different PSAPs.

## Examples

The following example shows an assignment of ERLs to a voice
                              		  emergency response zone. The calls have an ELIN from ERLs 8, 9, and 10. The
                              		  locations for ERLs in zone 10 are searched in the order each CLI was entered
                              		  for a phone address match because no priority order is assigned.

```
voice emergency response zone 10
location 8
location 9
location 10
```

### Related Commands

Command

Description

location

Identifies locations within an emergency response zone and
                                          						optionally assigns a priority order to the location.

## voice hunt-group

To create a hunt group for phones in a Cisco Unified Communications
                              		  Manager Express (Cisco Unified CME) or Cisco Unified Session Initiation
                              		  Protocol (SIP) Survivable Remote Site Telephony (SRST) system, use the voice hunt-group command in global configuration mode.
                              		  To delete a hunt group, use the no form of this command.

voice hunt-group hunt-tag { longest-idle | parallel | peer | sequential }

no voice hunt-group hunt-tag

### Syntax Description

hunt-tag

Unique sequence number that identifies the hunt group.
                                          						Range is 1 to 100.

longest-idle

Allows an incoming call to go first to the number that has
                                          						been idle the longest for the number of hops specified when the hunt group was
                                          						defined. The longest-idle time is determined from the last time that a phone
                                          						registered, reregistered, or went on-hook.

parallel

Allows an incoming call to simultaneously ring all the
                                          						numbers in the hunt group member list.

peer

Allows a round-robin selection of the first extension to
                                          						ring. Ringing proceeds in a circular manner from left to right. The round-robin
                                          						selection starts with the number left of the number that answered when the
                                          						hunt-group was last called.

sequential

Allows an incoming call to ring all the numbers in the
                                          						left-to-right order in which they were listed when the hunt group was defined.

### Command Default

No voice hunt group is created.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

12.4(15)XZ

Cisco Unified CME 4.3

This command was modified to add support for Cisco Unified
                                          						SCCP IP phones.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

15.2(4)M

Cisco Unified SIP SRST 9.1

This command was introduced in Cisco Unified SIP SRST 9.1.

### Usage Guidelines

The voice hunt-group command enters voice hunt-group
                              		  configuration mode to define a hunt group. A hunt group is a list of phone
                              		  numbers that take turns receiving incoming calls to a specific number (pilot
                              		  number), which is defined with the pilot command. The specific extensions
                              		  included in the hunt group and the order and maximum number of extensions
                              		  allowed in the list are defined with the list command.

If a number in the list is busy or does not answer, the call is
                              		  redirected to the next number in the list. The last number tried is the final
                              		  number, which is defined with the final command. If the number of times that a
                              		  call is redirected to a new number exceeds 5, you must use the max-redirect command to increase the allowable number of redirects in the
                              		  Cisco Unified CME or Cisco Unified SIP SRST system.

To configure a new hunt group, you must specify the longest-idle , parallel , peer , or sequential keyword. To change an existing hunt group configuration, the
                              		  keyword is not required. To change the type of hunt group, for instance from
                              		  peer to sequential or sequential to peer, you must remove the existing hunt
                              		  group first by using the no form of this command and then re-create
                              		  it.

The parallel keyword creates a dial peer to allow
                              		  an incoming call to ring multiple phones simultaneously. The use of parallel
                              		  hunt groups is also referred to as application-level forking because it enables
                              		  the forking of a call to multiple destinations. A pilot dial peer cannot be
                              		  used as a voice hunt group and a hunt group at the same time.

While ephone hunt groups only support Cisco Unified SCCP IP phones, a
                              		  voice hunt group supports either a Cisco Unified SCCP IP phone or a Cisco
                              		  Unified SIP IP phone.

With the voice hunt group feature preconfigured in the Cisco Unified
                              		  SIP SRST router, voice hunt groups continue to be supported after phones
                              		  fallback from a Cisco Unified Communications Manager (Cisco Unified CM) to a
                              		  Cisco Unified SIP SRST router.

## Examples

The following example shows how to define longest-idle hunt group 1
                              		  with pilot number 7501, final number 8000, and nine numbers in the list. After
                              		  a call is redirected six times (makes 6 hops), it is redirected to the final
                              		  number 8000.

```
Router(config)# voice hunt-group 1 longest-idle Router(config-voice-hunt-group)# pilot 7501 Router(config-voice-hunt-group)# list 7001, 7002, 7023, 7028, 7045, 7062, 7067, 7072, 7079 Router(config-voice-hunt-group)# final 8000 Router(config-voice-hunt-group)# hops 6 Router(config-voice-hunt-group)# timeout 20 Router(config-voice-hunt-group)# exit
```

The following example shows how to define peer hunt group number 2.
                              		  Callers dial the pilot number 5610 to reach the hunt group. The first extension
                              		  to ring the first time that this hunt group is called is 5601. If 5601 does not
                              		  answer, the hunt proceeds from left to right, beginning with the extension
                              		  directly to the right. If none of those extensions answer, the call is
                              		  forwarded to extension 6000, which is the number for the voice-mail service.

The second time someone calls the hunt group, the first extension to
                              		  ring is 5602 if 5601 was answered during the previous call.

```
Router(config)# voice hunt-group 2 peer Router(config-voice-hunt-group)# pilot 5610 Router(config-voice-hunt-group)# list 5601, 5602, 5617, 5633 Router(config-voice-hunt-group)# final 6000 Router(config-voice-hunt-group)# timeout 30 Router(config-voice-hunt-group)# exit
```

The following example shows how to define sequential hunt group
                              		  number 3. When callers dial extension 5601, the first phone to ring is 5001,
                              		  then 5002, 5017, and 5028. If none of those extensions answer, the call is
                              		  forwarded to extension 6000, which is the number for the voice-mail service.

```
Router(config)# voice hunt-group 3 sequential Router(config-voice-hunt-group)# pilot 5601 Router(config-voice-hunt-group)# list 5001, 5002, 5017, 5028 Router(config-voice-hunt-group)# final 6000 Router(config-voice-hunt-group)# timeout 30 Router(config-voice-hunt-group)# exit
```

The following example shows how to define a parallel hunt group. When
                              		  callers dial extension 1000, extensions 1001, 1002, and so forth ring
                              		  simultaneously. The first extension to answer is connected. All other call legs
                              		  are disconnected. If none of the extensions answer, the call is forwarded to
                              		  extension 2000, which is the number for the voice-mail service.

```
Router(config)# voice hunt-group 4 parallel Router(config-voice-hunt-group)# pilot 1000 Router(config-voice-hunt-group)# list 1001, 1002, 1003, 1004 Router(config-voice-hunt-group)# final 2000 Router(config-voice-hunt-group)# timeout 20 Router(config-voice-hunt-group)# exit
```

### Related Commands

Command

Description

final (voice hunt-group)

Defines the last extension in a voice hunt group.

hops (voice hunt-group)

Defines the number of times that a call is redirected to
                                          						the next phone number in a peer voice hunt-group list before proceeding to the
                                          						final phone number.

list (voice hunt-group)

Defines the phone numbers that participate in a voice hunt
                                          						group.

max-redirect

Changes the number of times that a call can be redirected
                                          						by call forwarding or transfer within a Cisco Unified CME system.

pilot (voice hunt-group)

Defines the phone number that callers dial to reach a voice
                                          						hunt group.

timeout (voice hunt-group)

Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the hunt-group list and defines
                                          						the last phone number in the hunt group.

## voice hunt-group
                        	 login

To authorize an
                              		  voice register dn or ephone-dn, use the voice-hunt-groups login command in voice register-dn configuration
                              		  mode. To disable this capability, use the no form of
                              		  this command.

voice hunt-groups login

no voice hunt-groups login

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

A voice
                              		  register-dn is not allowed to dynamically join and leave voice hunt groups.

### Command Modes

voice register dn configuration (config-voice-register-dn)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.4(3)M

Cisco
                                          						Unified Enhanced SRST 10.5

This
                                          						command was introduced.

### Usage Guidelines

Use the show voice
                                    				hunt-groups command to display current hunt group members,
                              		  including those who joined the group dynamically.

## Examples

The following
                              		  example creates five voice-register-dns and a hunt group that includes the
                              		  first two voice-register-dn and two wildcard slots. The last three
                              		  voice-register-dns are enabled for group hunt dynamic membership. Each of them
                              		  can join and leave the hunt group whenever one of the slots is available.

```
voice-register-dn 22
 number 4566
voice-register-dn 23
 number 4567
voice-register-dn 24
 number 4568
 voice-hunt login
voice-register-dn 25
 number 4569
 voice-hunt login
voice-register-dn 26
 number 4570
 voice-hunt-groups login
voice-hunt-groups 1 peer
 list 4566,4567,*,*
 final 7777
```

### Related Commands

Command

Description

show voice hunt-groups

Displays voice-hunt group configuration, current status, and statistics.

## voice moh-group

To enter voice-moh-group configuration mode and set up music on hold
                              		  (MOH) group parameters, use the voice moh-group command in global configuration mode. To remove the music on
                              		  hold (MOH) group parameters from the configuration for SCCP IP phones, use the no form of this command.

voice moh-group moh-group tag

no voice moh-group tag

### Syntax Description

tag

Specifies a moh-group number tag (1-5) to be used for music
                                          						on hold group parameters.

### Command Default

No voice-moh-group is enabled.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was introduced.

### Usage Guidelines

This command enters the voice-moh-group configuration mode for
                              		  configuring music on hold (MOH) group parameters for SCCP IP phones in Cisco
                              		  Unified CME or in Cisco Unified SRST.

## Examples

The following example shows how to enter voice-moh-group
                              		  configuration mode for configuring a moh group in Cisco Unified CME. This
                              		  example also includes the command to configure a music on hold (MOH) flash file
                              		  for this voice-moh- group.

```
Router(config)# voice-moh-group 1 Router(config-voice-moh-group)#moh minuet.wav
```

### Related Commands

moh

Enables music on hold from a flash audio feed.

multicast moh

Enables multicast of the music-on-hold audio stream.

extension-range

Defines extension range for a clients calling a
                                          						voice-moh-group.

## voice register global

To enter voice register global configuration mode in order to set
                              		  global parameters for all supported Cisco SIP IP phones in a Cisco Unified CME
                              		  or Cisco Unified Session Initiation Protocol (SIP) Survivable Remote Site
                              		  Telephony (SRST) environment, use the voice register global command in global configuration mode. To
                              		  automatically remove the existing DNs, pools, and global dialplan patterns, use
                              		  the no form of this command.

voice register global

no voice register global

### Syntax Description

This command has no arguments or keywords.

### Command Default

There are no system-level parameters that are configured for SIP IP phones.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

15.0(1)XA

Cisco SIP SRST 8.0

This command was updated to display the signaling transport
                                          						protocol.

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

The no form of the command was modified.

Cisco Unified SIP SRST 12.8

Introduced support for YANG models.

Cisco IOS XE Cupertino
                                                17.8.1a

Cisco Unified SIP SRST 12.8

Added the new CLI commands key-server , and key-server source-interface <options> under sip-oauth for voice register global mode.

### Usage Guidelines

Cisco Unified CME

Use this command to set provisioning parameters for all supported SIP
                              		  phones in a Cisco Unified CME system.

Cisco Unified SIP SRST

Use this command to set provisioning parameters for multiple pools;
                              		  that is, all supported Cisco SIP IP phones in a SIP SRST environment.

Cisco Unified CME 8.1 enhances the no form of voice register global
                              		  command. The no voice register global command clears global configuration along
                              		  with pools and DN configuration and also removes the configurations for voice
                              		  register template, voice register dialplan, and voice register session-server.
                              		  A confirmation is sought before the cleanup is made.

In Cisco Unified SRST 8.1 and later versions, the no voice register
                              		  global command removes pools and DNs along with the global configuration.

From Cisco IOS XE Cupertino
                                    17.8.1a onwards, the voice register global command is enhanced to support the following:

Key server IP and credentials on SRST to retrieve keys from CUCM and interface specification of source address for OAuth key
                                    server.

```
Router#show running-config | section voice register global
voice register global
 sip-oauth     SIP OAuth parameters for Unified SRST
  key-server source-interface GigabitEthernet 1
  key-server ipv4:2.2.2.2 username admin password 6 Ada_SWISQW^TYSN\ZREeFHJTZPCgMMAAB
```

## Examples

The following is partial sample output from the show voice register global command. All of the parameters listed were set under voice register global configuration mode:

```
Router# show voice register global CONFIG [Version=4.0(0)]
========================
Version 4.0(0)
Mode is cme
Max-pool is 48
Max-dn is 48
Source-address is 10.0.2.4 port 5060
Load 7960-40 is P0S3-07-4-07
Time-format is 12
Date-format is M/D/Y
Time-zone is 5
Hold-alert is disabled
Mwi stutter is disabled
Mwi registration for full E.164 is disabled
Dst auto adjust is enabled
 start at Apr week 1 day Sun time 02:00
 stop  at Oct week 8 day Sun time 02:00
```

## Examples

## Examples

The following is a sample output from no voice register global
                              		  command:

```
Router(config)# no voice register global
This will remove all the existing DNs, Pools, Templates,
Dialplan-Patterns, Dialplans and Feature Servers on the system.
Are you sure you want to proceed? Yes/No? [no]:
```

### Related Commands

Command

Description

allow connections sip to sip

Allows connections between SIP endpoints in a Cisco
                                          						multiservice IP-to-IP gateway.

application (voice register global)

Selects the session-level application for all dial peers
                                          						associated with SIP phones.

mode (voice register global)

Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified system.

## voice register pool

To enter voice register pool configuration mode for SIP phones, use
                              		  the voice register pool command in global configuration mode. To
                              		  remove the pool configuration, use the no form of this command.

voice register pool pool-tag

no voice register pool pool-tag

### Syntax Description

pool-tag

Unique number assigned to the pool. Range is 1 to 100.

### Command Default

No default behavior or values

### Command Modes

Global configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SIP SRST 3.0

This command was introduced.

12.3(4)T

Cisco SIP SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was added to Cisco CME.

Cisco IOS XE Amsterdam 17.2.1r

Cisco Unified SIP SRST 12.8

Introduced support for YANG models.

Cisco IOS XE Cupertino
                                                17.8.1a

Cisco Unified SIP SRST 14.2

Added a new CLI command sip-oauth for voice register pool mode.

### Usage Guidelines

Cisco Unified CME

Use this command to set phone-specific parameters for SIP phones in a Cisco Unified CME system. Before using this command,
                              enable the mode cme command and set the maximum number of SIP phones supported in your system by using the max-pool command.

Cisco Unified SIP SRST

Use this command to enable user control on which registrations are to be accepted or rejected by a SIP SRST device. The voice
                              register pool command mode can be used for specialized functions and to restrict registrations on the basis of MAC, IP subnet,
                              and number range parameters.

From Cisco IOS XE Cupertino
                                    17.8.1a onwards, you can enable or disable SIP OAuth based authentication under voice register pool.

For example:

```
Router# voice register pool  1
	sip-oauth
```

## Examples

The following example shows how to enter voice register pool
                              		  configuration mode and forward calls to extension 9999 when extension 2001 is
                              		  busy:

```
Router(config)# voice register pool 10 Router(config-register-pool)# type 7960 Router(config-register-pool)# number 1 2001 Router(config-register-pool)# call-forward busy 9999 mailbox 1234
```

## Examples

The following partial sample output from the show running-config command shows that several voice register pool commands are
                              		  configured within voice register pool 3:

```
voice register pool 3
 id network 10.2.161.0 mask 255.255.255.0
 number 1 95... preference 1
 cor outgoing call95 1 95011
 max registrations 5
 voice-class codec 1
```

## Examples

The following is a partial sample output showing SIP OAuth enabled.

```
2055Router#show voice register pool all
 Pool Tag 20
Config:
  Device ID Name is test
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  kpml signal is enabled
  Lpcor Type is none

  SIP-OAuth is enabled
  Reason for unregistered state: 
       No registration request since last reboot/unregister

  paging-dn: config 0 [multicast]  effective 0 [multicast] 

VRF:
  NA
```

### Related Commands

Command

Description

max-pool (voice register global)

Sets the maximum number of SIP phones that are supported by
                                          						a Cisco Unified CME system.

mode (voice register global)

Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CME system.

number (voice register pool)

Configures a valid number for a SIP phone.

type (voice register pool)

Defines a Cisco IP phone type.

voice register dn

Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line.

voice register global

Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified CME
                                          						or Cisco Unified SIP SRST environment.

## voice sip oauth get-keys

To retrieve OAuth keys from the CUCM on demand, use the voice sip oauth get-keys command.

### Command Default

Disabled by default.

### Command Modes

Global configuration mode.

## Command History

Cisco IOS XE Cupertino
                                             17.8.1a

This command was introduced.

### Usage Guidelines

Use the voice sip oauth get-keys command on SRST to get keys from the call manager.

Key server should be configured under voice register .

Keys are fetched every 24 hours or within 24 hours of last command execution.

To get the keys using the voice sip oauth get-keys command, key server should be configured first.

## Examples

```
Router#voice sip oauth get-keys
Successfully triggered http request to fetch sip-oauth keys
Router#
```

## voice vrf

To configure a voice VRF, use the voice vrf command in global configuration mode. To remove the voice VRF configuration, use the no form of this command.

voice vrf vrfname

no voice vrf vrfname

### Syntax Description

vrfname

A name assigned to the voice vrf.

### Command Default

No voice VRF is configured.

### Command Modes

Global configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

Unified SRST 12.8

This command was introduced as part of VRF functionality support on Cisco 4000 Series Integrated Services Router for Unified
                                          SRST.

### Usage Guidelines

You must create a VRF using the vrf definition vrf-name command before you can configure it as a voice VRF. This configuration is both for trunk side and Unified SRST line side.

## Examples

The following is a sample configuration for voice vrf in Unified SRST line side:

```
vrf definition vrf1
 rd 100:101
 !
 address-family ipv4
 exit-address-family
voice vrf vrf1
interface GigabitEthernet0/0/0
 vrf forwarding vrf1
 ip address 8.44.22.77 255.255.0.0
ip route vrf vrf1 8.0.0.0 255.0.0.0 8.44.0.1
```

### Related Commands

Command

Description

vrf definition vrf-name

Creates a VRF with the specified name.

## voice-class codec (voice register pool)

To assign a previously configured codec selection preference list,
                              		  use the voice-class codec command in voice register pool configuration
                              		  mode. To remove the codec preference assignment from the voice register pool,
                              		  use the no form of this command.

voice-class codec tag

no voice-class codec

### Syntax Description

tag

Unique number assigned to the voice class. Range is from 1
                                          						to 10000. The tag number maps to the tag number created by using the voice class codec command in dial-peer configuration mode.

### Command Default

None

### Command Modes

Voice register pool configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SIP SRST 3.0

This command was introduced.

12.3(4)T

Cisco SIP SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was added to Cisco CME.

Cisco Unified SIP SRST 12.8

Introduced support for YANG models.

### Usage Guidelines

During Cisco Unified Session Initiation Protocol (SIP) Survivable
                              		  Remote Site Telephony (SRST) or Cisco Unified Communications Manager Express
                              		  (Cisco Unified CME) registration, a dial peer is created, and that dial peer
                              		  includes codec g729r8 by default. The voice-class codec command allows you to change the automatically selected default
                              		  codec, if desired.

You can assign one voice class to each voice register pool. If you
                              		  assign another voice class to a pool, the last voice class assigned replaces
                              		  the previous voice class.

## Examples

The following partial sample output from the show running-config command shows that voice register pool 1 has been set up to use
                              		  the previously configured codec voice class 1:

```
voice register pool 1
 id mac 0030.94C2.A22A
 preference 5
 cor incoming call91 1 91011
 translate-outgoing called 1
 proxy 10.2.161.187 preference 1 monitor probe icmp-ping
 alias 1 94... to 91011 preference 8
 voice-class codec 1
```

### Related Commands

Command

Description

codec (voice register pool)

Specifies the codec supported by a single Cisco SIP phone
                                          						or a VoIP dial peer in a Cisco Unified SIP SRST or a Cisco Unified CME
                                          						environment.

id (voice register pool)

Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

voice class codec (dial-peer)

Assigns a previously configured codec selection preference
                                          						list (codec voice class) to a VoIP dial peer.

## voicemail (call-manager-fallback)

To configure the telephone number that is speed-dialed when the
                              		  messages button on a Cisco IP phone is pressed, use the voicemail command in call-manager-fallback
                              		  configuration mode. To disable the messages button, use the no form of this command.

voicemail phone-number

no voicemail

### Syntax Description

phone-number

Phone number configured as a speed-dial number for
                                          						retrieving messages.

### Command Default

No phone number is configured, and the messages button is
                              		  ineffective.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco SRST 1.0

This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs.

12.2(2)XT

Cisco SRST 2.0

This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

### Usage Guidelines

The voicemail command configures the telephone
                              		  number that is speed-dialed when the messages button on a Cisco IP phone is
                              		  pressed. The same voice-mail telephone number is configured for all Cisco IP
                              		  phones connected to the router.

## Examples

The following example specifies 4085550100 as the speed-dial number
                              		  that is dialed to retrieve messages when the messages button is pressed:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# voicemail 914085550100
```

The number 914085550100 is called when the Cisco IP phone messages
                              		  button is pressed to retrieve messages.

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified Survivable Remote Site Telephony
                                          						(SRST) support and enters call-manager-fallback configuration mode.

## vrf definition

To configure a VRF with a specified name, use the vrf definition command in global configuration mode. To remove the VRF configuration, use the no form of this command.

vrf definition vrf-name

no vrf definition vrf-name

### Syntax Description

vrf-name

A name assigned to the configured vrf.

### Command Default

No VRF is configured.

### Command Modes

Global configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

Unified SRST 12.8

This command was introduced as part of VRF functionality support on Cisco 4000 Series Integrated Services Router for Unified
                                          SRST.

### Usage Guidelines

You can create a VRF with a specified name using the vrf definition vrf-name command. Space is not allowed in the VRF name. For example, vrf 1 is not a valid name for a VRF. However, vrf1 as shown in the example below is a valid name.

## Examples

The following is a sample configuration for vrf definition in Unified SRST line side:

```
vrf definition vrf1
 rd 100:101
 !
 address-family ipv4
 exit-address-family
```

### Related Commands

Command

Description

voice vrf vrfname

Configures a Voice VRF in global configuration mode.

## vrf forwarding

To associate a VRF instance with the tunnel, use the vrf forwarding command in interface configuration mode. To remove the association of VRF instance with the tunnel, use the no form of this command.

vrf forwarding customer-vrf-name

no vrf forwarding customer-vrf-name

### Syntax Description

customer-vrf-name

A name assigned to the customer vrf.

### Command Default

No VRF is forwarded.

### Command Modes

Interface configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

Unified SRST 12.8

This command was introduced as part of VRF functionality support on Cisco 4000 Series Integrated Services Router for Unified
                                          SRST.

### Usage Guidelines

You can associate the customer VRF instance with the tunnel using the vrf forwarding customer-vrf-name command. Packets exiting the tunnel are forwarded to this VRF (inner IP packet routing).

## Examples

The following is a sample configuration for vrf forwarding for Unified SRST:

```
voice vrf vrf1
interface GigabitEthernet0/0/0
 vrf forwarding vrf1
 ip address 8.44.22.77 255.255.0.0
ip route vrf vrf1 8.0.0.0 255.0.0.0 8.44.0.1
```

### Related Commands

Command

Description

voice vrf vrfname

Configures a Voice VRF in global configuration mode.

vrf definition vrf-name

Creates a VRF with the specified name.

## xmlschema (call-manager-fallback)

To specify the URL for a Cisco Unified Survivable Remote Site
                              		  Telephony (SRST) eXtensible Markup Language (XML) application program interface
                              		  (API) schema, use the xmlschema command in call-manager-fallback configuration mode. To set the
                              		  URL for the XML API schema to the default, use the no form of this command.

xmlschema schema-url

no xmlschema

### Syntax Description

schema-url

Local or remote URL as defined in RFC 2396.

### Command Default

srst-its.xsd

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)T

Cisco SRST 3.2

This command was introduced.

## Examples

The following example specifies a URL for an XML API schema:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# xmlschema http://server2.example.com/schema/schema1.xsd
```

### Related Commands

Command

Description

call-manager-fallback

Enable Cisco Unified SRST configuration mode.

| string | String (30 characters) used to describe or identify an
                                          						ERL’s location. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| address | Specifies a comma separated text entry (up to 247
                                          						characters) of an ERL’s civic address. |
| elin | Specifies a PSTN number that will replace the caller’s
                                          						extension. |
| subnet | Defines which IP phones are part of this ERL. |
| voice emergency response location | Creates a tag for identifying an ERL for E911 services. |

| “primary pilot name” | Name of primary pilot number. |
|---|---|
| secondary “secondary pilot name” | (Optional) Name of secondary pilot number. |

| Release | Modification |
|---|---|
| 15.3(2)T | This command was introduced. |

| Note | Use quotes (") when input strings have spaces in between. |
|---|---|

| Command | Description |
|---|---|
| voice hunt-group | Enters voice hunt-group configuration mode and creates a
                                          						hunt group for phones in a Cisco Unified CME system. |
| show voice hunt-group | Displays configuration information associated with one or
                                          						all voice hunt groups in a Cisco Unified CME system. |

| tag | Telephone number when there are multiple number commands. Range is 1 to 114. |
|---|---|
| number-pattern | Phone numbers (including wild cards and patterns) that are
                                          						permitted by the registrar to handle the Register message from the Cisco
                                          						Unified SIP IP phone. |
| preference value | (Optional) Defines the number list preference order. Range
                                          						is 0 to 10. The highest preference is 0. There is no default. |
| huntstop | (Optional) Stops hunting when the dial peer is busy. |
| dn dn-tag | Identifies the directory number tag for this phone number
                                          						as defined by the voice register dn command. Range is 1 to 288. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco CME and the dn keyword was added. |
| 12.4(11)XJ | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 | This command was modified. The number-pattern argument and preference and huntstop keywords were removed from
                                          						Cisco Unified CME. |
| 12.4(15)T | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 | The modifications to this command were integrated into
                                          						Cisco IOS Release 12.4(15)T. |
| 15.2(4)M | Cisco Unified CME 9.1 Cisco Unified SIP SRST 9.1 | This command was modified to increase the valid value of
                                          						the tag argument to 114. |

| Note | Configure the id (voice register pool) command before any other voice register pool
                                       		  commands, including the number command. The id command identifies a locally available,
                                       		  individual Cisco Unified SIP IP phone or a set of Cisco Unified SIP IP phones. |
|---|---|

| Command | Description |
|---|---|
| id (voice register pool) | Explicitly identifies a locally available, individual Cisco
                                          						Unified SIP IP phone or, when running Cisco Unified SIP SRST, a set of Cisco
                                          						Unified SIP IP phones. |
| voice register dn | Enters voice register dn configuration mode to define an
                                          						extension for a phone line, intercom line, voice-mail port, or a
                                          						message-waiting indicator. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 Cisco Unified SIP SRST 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| voice-class sip outbound-proxy | Configures SIP outbound proxy settings for an individual
                                          						dial peer that override global settings for the Cisco IOS voice gateway. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 Cisco Unified SRST 8.5 | This command was introduced. |

| tag1 | Alphanumeric string fewer than four DTMF digits in length.
                                          						The alphanumeric string consists of a combination of four letters (A,B,C, and
                                          						D), two symbols (* and #), and ten digits (0 to 9). The tag numbers match the
                                          						numbers defined in the voice-mail system’s integration file, immediately
                                          						preceding either the number of the calling party, the number of the called
                                          						party, or a forwarding number. |
|---|---|
| tag2 and tag3 | (Optional) See tag1. |
| last-tag | (Optional) See tag1 . This tag indicates the end of
                                          						the pattern. |
| CGN | Calling number (CGN) information is sent to the voice-mail
                                          						system. |
| CDN | Called number (CDN) information is sent to the voice-mail
                                          						system. |
| FDN | Forwarding number (FDN) information is sent to the
                                          						voice-mail system. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco SRST 2.0 | This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |
| 12.2(13)T | Cisco SRST 2.02 | This command was introduced for Cisco SRST Version 2.02. |

| Note | Although it is unlikely that you will use multiple instances of
                                       		  the CGN , CDN , or FDN keyword in a single command line, it is
                                       		  permissible to do so. |
|---|---|

| Command | Description |
|---|---|
| pattern ext-to-ext busy (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension attempts to connect
                                          						to a busy extension and the call is forwarded to voice mail |
| pattern ext-to-ext no-answer (vm- integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext busy (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext no-answer (vm- integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail. |
| vm-integration | Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and analog voice-mail systems. |

| tag1 | Alphanumeric string fewer than four DTMF digits in length.
                                          						The alphanumeric string consists of a combination of four letters (A,B,C, and
                                          						D), two symbols (* and #), and ten digits (0 to 9). The tag numbers match the
                                          						numbers defined in the voice-mail system’s integration file, immediately
                                          						preceding either the number of the calling party, the number of the called
                                          						party, or a forwarding number. |
|---|---|
| tag2 and tag3 | (Optional) See tag1. |
| last-tag | (Optional) See tag1 . This tag indicates the end of
                                          						the pattern. |
| CGN | Calling number (CGN) information is sent to the voice-mail
                                          						system. |
| CDN | Called number (CDN) information is sent to the voice-mail
                                          						system. |
| FDN | Forwarding number (FDN) information is sent to the
                                          						voice-mail system. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco SRST 2.0 | This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |
| 12.2(13)T | Cisco SRST 2.02 | This command was introduced for Cisco SRST Version 2.02. |

| Note | Although it is unlikely that you will use multiple instances of
                                       		  the CGN , CDN , or FDN keyword in a single command line, it is
                                       		  permissible to do so. |
|---|---|

| Command | Description |
|---|---|
| pattern direct (vm- integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the messages button on the
                                          						phone. |
| pattern ext-to-ext no-answer (vm- integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext busy (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext no-answer (vm- integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail. |
| vm-integration | Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and analog voice-mail systems. |

| tag1 | Alphanumeric string fewer than four DTMF digits in length.
                                          						The alphanumeric string consists of a combination of four letters (A,B,C, and
                                          						D), two symbols (* and #), and ten digits (0 to 9). The tag numbers match the
                                          						numbers defined in the voice-mail system’s integration file, immediately
                                          						preceding either the number of the calling party, the number of the called
                                          						party, or a forwarding number. |
|---|---|
| tag2 and tag3 | (Optional) See tag1. |
| last-tag | (Optional) See tag1 . This tag indicates the end of
                                          						the pattern. |
| CGN | Calling number (CGN) information is sent to the voice-mail
                                          						system. |
| CDN | Called number (CDN) information is sent to the voice-mail
                                          						system. |
| FDN | Forwarding number (FDN) information is sent to the
                                          						voice-mail system. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco SRST 2.0 | This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |
| 12.2(13)T | 2.02 | This command was introduced for Cisco SRST Version 2.02. |

| Note | Although it is unlikely that you will use multiple instances of
                                       		  the CGN , CDN , or FDN keyword in a single command line, it is
                                       		  permissible to do so. |
|---|---|

| Command | Description |
|---|---|
| pattern direct (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the messages button on the
                                          						phone. |
| pattern ext-to-ext busy (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext busy (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext no-answer (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail. |
| vm-integration | Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and analog voice-mail systems. |

| tag1 | Alphanumeric string fewer than four DTMF digits in length.
                                          						The alphanumeric string consists of a combination of four letters (A,B,C, and
                                          						D), two symbols (* and #), and ten digits (0 to 9). The tag numbers match the
                                          						numbers defined in the voice-mail system’s integration file, immediately
                                          						preceding either the number of the calling party, the number of the called
                                          						party, or a forwarding number. |
|---|---|
| tag2 and tag3 | (Optional) See tag1. |
| last-tag | (Optional) See tag1 . This tag indicates the end of
                                          						the pattern. |
| CGN | Calling number (CGN) information is sent to the voice-mail
                                          						system. |
| CDN | Called number (CDN) information is sent to the voice-mail
                                          						system. |
| FDN | Forwarding number (FDN) information is sent to the
                                          						voice-mail system. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco SRST 2.0 | This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |
| 12.2(13)T | Cisco SRST 2.02 | This command was introduced for Cisco SRST Version 2.02. |

| Note | Although it is unlikely that you will use multiple instances of
                                       		  the CGN , CDN , or FDN keyword in a single command line, it is
                                       		  permissible to do so. |
|---|---|

| Command | Description |
|---|---|
| pattern direct (vm- integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the messages button on the
                                          						phone. |
| pattern ext-to-ext busy (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension attempts to connect
                                          						to a busy extension and the call is forwarded to voice mail. |
| pattern ext-to-ext no-answer (vm- integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext no-answer (vm- integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail. |
| vm-integration | Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and analog voice-mail systems. |

| tag1 | Alphanumeric string fewer than four DTMF digits in length.
                                          						The alphanumeric string consists of a combination of four letters (A,B,C, and
                                          						D), two symbols (* and #), and ten digits (0 to 9). The tag numbers match the
                                          						numbers defined in the voice-mail system’s integration file, immediately
                                          						preceding either the number of the calling party, the number of the called
                                          						party, or a forwarding number. |
|---|---|
| tag2 and tag3 | (Optional) See tag1. |
| last-tag | (Optional) See tag1 . This tag indicates the end of
                                          						the pattern. |
| CGN | Calling number (CGN) information is sent to the voice-mail
                                          						system. |
| CDN | Called number (CDN) information is sent to the voice-mail
                                          						system. |
| FDN | Forwarding number (FDN) information is sent to the
                                          						voice-mail system. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco SRST 2.0 | This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |
| 12.2(13)T | Cisco SRST 2.02 | This command was introduced for Cisco SRST Version 2.02. |

| Note | Although it is unlikely that you will use multiple instances of
                                       		  the CGN , CDN , or FDN keyword in a single command line, it is
                                       		  permissible to do so. |
|---|---|

| Command | Description |
|---|---|
| pattern direct (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the messages button on the
                                          						phone. |
| pattern ext-to-ext busy (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension attempts to connect
                                          						to a busy extension and the call is forwarded to voice mail. |
| pattern ext-to-ext no-answer (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext busy (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail. |
| vm-integration | Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and analog voice-mail systems. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 Cisco Unified SRST 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| device-name | Assigns a name to a phone type in an ephone-type template. |
| load | Associates a type of Cisco Unified IP phone with a phone
                                          						firmware file. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified Enhanced SRST 10.5 | This
                                       					 command was introduced. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified Enhanced SRST 10.5 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| Voice register global | Enters
                                          						voice register global configuration mode. |
| Voice register pool | Enters
                                          						voice register pool configuration mode. |
| Voice register template | Enters
                                          						voice register template configuration mode. |

| telephone-number | The
                                          						telephone number to match an incoming called number. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.3(7)XL | Cisco
                                          						SRST 3.1.1 | This
                                          						command was introduced. |
| 12.3(11)T | Cisco
                                          						SRST 3.2 | This
                                          						command was integrated into Cisco IOS Release 12.3(11)T. |

| Note | The default
                                       		  phone load on Cisco Unified Communications Manager, Release 4.0(1), for the
                                       		  Cisco 7905 and Cisco 7912 IP phones does not enable the PickUp soft key during
                                       		  fallback. To enable the PickUp soft key on Cisco 7905 and Cisco 7912 IP phones,
                                       		  upgrade your default phone load to Cisco Unified Communications Manager,
                                       		  Release 4.0(1) Sr2. Alternatively, you can upgrade the phone load to cmterm-7905g-sccp.3-3-8.exe or cmterm-7912g-sccp.3-3-8.exe , respectively. |
|---|---|

| Command | Description |
|---|---|
| alias (call-manager- fallback) | Provides a mechanism for rerouting calls to telephone numbers that are
                                          						unavailable during Cisco Unified Communications Manager fallback. |
| call-manager-fallback | Enables Cisco Unified SRST support and enters call-manager-fallback
                                          						configuration mode. |

| preference-order | Preference order for the extension or telephone number
                                          						associated with a pool. Range is 0 to 10. Default is 0, which is the highest
                                          						preference. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco Communications Manager
                                          						Express (Cisco CME). |

| Note | Configure the id (voice register pool) command before any other voice register
                                       		  pool commands, including the preference command. The id command identifies a
                                       		  locally available individual SIP phone or set of Cisco SIP phones. |
|---|---|

| Command | Description |
|---|---|
| id (voice register pool) | Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| ip-address | IP address of the SIP proxy. |
|---|---|
| preference value | (Optional) Defines the preference of the proxy dial peers
                                          						that are created. Range is from 0 to 10. The highest preference is 0. There is
                                          						no default. |
| monitor probe | (Optional) Enables monitoring of proxy dial peers. icmp-ping —Enables
                                             						  monitoring of proxy dial peers using ICMP ping. rtr —Enables
                                             						  monitoring of proxy dial peers using RTR probes. alternate-ip-address —(Optional)
                                             						  Enables monitoring of alternate IP addresses other than the proxy address. For
                                             						  example, to monitor a gateway front end to a SIP proxy. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Note | The id (voice register pool) command must be configured before any
                                       		  other voice register pool commands, including the proxy command. The id command identifies a locally available
                                       		  individual Cisco SIP IP phone or sets of Cisco SIP IP phones. |
|---|---|

| Command | Description |
|---|---|
| call fallback active | Enables a call request to fall back to alternate dial peers
                                          						in case of network congestion. |
| id (voice register pool) | Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone or set of Cisco SIP IP phones. |
| voice register pool | Enables SIP SRST voice register pool configuration
                                          						commands. |

| expires | (Optional) Sets the active time for an incoming
                                          						registration. |
|---|---|
| max sec | (Optional) Maximum expires time for a registration, in
                                          						seconds. The range is from 600 to 86400. The default is 3600. |
| min sec | (Optional) Minimum expires time for a registration, in
                                          						seconds. The range is from 60 to 3600. The default is 60. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 and Cisco SIP SRST 3.4 | This command was added to Cisco CME. |

| Command | Description |
|---|---|
| sip | Enters SIP configuration mode from voice service VoIP
                                          						configuration mode. |
| voice register global | Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified CME
                                          						or Cisco Unified SIP SRST environment. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| all | All Cisco IP phones. |
|---|---|
| seconds | Time interval, in seconds, that passes between each Cisco
                                          						IP phone resetting. The range is from 0 to 60. |
| mac-address mac-address | MAC address of a particular Cisco IP phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco SRST 1.0 | This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers; Cisco IAD2420
                                          						series IADs. |
| 12.2(2)XT | Cisco SRST 2.0 | This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode. |

| digit-string | The number of the access prefix. |
|---|---|

| Cisco IOS Release | Cisco Unified Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco Unified SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco Unified SRST 3.0 | This command was integrated into Cisco Unified IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified Unified SRST support and enters
                                          						call-manager-fallback configuration mode. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 Cisco Unified SRST 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| device-id | Specifies the device ID for a phone type. |
| type | Assigns a phone type to an SCCP phone. |

| Note | The security-policy command only works with SRST. While it is
                                       		  possible to configure this command when in CME mode, TLS-based connections from
                                       		  Cisco Unified IP Phones will fail. This failure will occur even if using the
                                       		  "CME-as-SRST" failover model. |
|---|---|

| secure | Requires SIP phones to use TLS for signaling transport.
                                          						Non-secure SIP phones are blocked from registering. Valid for Cisco Unified
                                          						SRST. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified SRST 8.0 | This command was introduced. |
| Cisco IOS XE Dublin
                                                17.10.1a | Unified Cisco SRST 14.3 | Introduced support for YANG models. |

| Command | Description |
|---|---|
| crypto signaling | Identifies the trustpoint and encryption restrictions used
                                          						during the TLS handshake. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						SRST 1.0 | This
                                          						command was introduced on the following platforms: Cisco 2600 series and Cisco
                                          						3600 series multiservice routers; Cisco IAD2420 series IADs. |
| 12.2(2)XT | Cisco
                                          						SRST 2.0 | This
                                          						command was implemented on Cisco 1750 and Cisco 1751 multiservice routers. |
| 12.2(8)T | Cisco
                                          						SRST 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco
                                          						SRST 2.0 | This
                                          						command was implemented on the Cisco 2600-XM and Cisco 2691 routers. |
| 12.2(11)T | Cisco
                                          						SRST 2.01 | This
                                          						command was integrated into Cisco IOS Release 12.2(11)T and implemented on the
                                          						Cisco 1760 routers. |
| 12.3(4)T | Cisco
                                          						SRST 3.0 | The
                                          						Version was added to output. |

| Field | Description |
|---|---|
| destination-pattern | Destination pattern (telephone number) configured for this dial peer. |
| dial-peer
                                          					 voice | Voice
                                          					 dial peer. |
| ephone-dn | Cisco IP
                                          					 phone directory number. |
| (no)
                                          					 huntstop | Whether
                                          					 or not huntstop is set. |
| ip
                                          					 source-address | IP
                                          					 address used by the Cisco IP phones to register with the router for service. |
| keepalive | Cisco
                                          					 IP phone keepalive period in seconds. |
| max-dn | Maximum
                                          					 directory numbers or virtual voice ports. |
| max-ephones | Maximum
                                          					 number of Cisco IP phones. |
| port | TCP
                                          					 port number used by the Cisco IP phones to communicate with the router. |
| station-id number | Number
                                          					 used for caller-ID purposes when calls are made using the line. |
| voice-port | (Virtual) voice port designator. |
| Version | SRST
                                          					 version number designation. |

| Command | Description |
|---|---|
| show call-manager- fallback dial-peer | Displays detailed configuration output for the dial peers in your network
                                          						during Cisco Unified CallManager fallback. |
| show call-manager- fallback ephone-dn | Displays output for the Cisco IP phone directory numbers or virtual voice ports
                                          						during Cisco Unified CallManager fallback. |
| show call-manager- fallback voice-port | Displays output for the voice ports while Cisco Unified CallManager is active. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						SRST 1.0 | This
                                          						command was introduced on the following platforms: Cisco 2600 series and Cisco
                                          						3600 series multiservice routers; Cisco IAD2420 series IADs. |
| 12.2(2)XT | Cisco
                                          						SRST 2.0 | This
                                          						command was implemented on Cisco 1750 and Cisco 1751 multiservice routers. |
| 12.2(8)T | Cisco
                                          						SRST 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco
                                          						SRST 2.0 | This
                                          						command was implemented on the Cisco 2600-XM and Cisco 2691 routers. |
| 12.2(11)T | Cisco
                                          						SRST 2.01 | This
                                          						command was integrated into Cisco IOS Release 12.2(11)T and implemented on the
                                          						Cisco 1760 routers. |

| Field | Description |
|---|---|
| call-forward busy | Indicates
                                          					 call forwarding when a Cisco IP phone is busy. |
| call-forward noan | Indicates
                                          					 call forwarding when no answer is received from a Cisco IP phone. |
| destination-pattern | Destination pattern (telephone number) configured for this dial peer. |
| dial-peer
                                          					 voice | Voice
                                          					 dial peer. |
| port | (Virtual)
                                          					 voice port designator. |

| Command | Description |
|---|---|
| show call-manager- fallback all | Displays the detailed configuration of all Cisco IP phones, directory numbers,
                                          						voice ports, and dial peers in your network during Cisco Unified Communications
                                          						Manager fallback. |
| show call-manager- fallback ephone-dn | Displays output for the Cisco IP phone directory numbers or virtual voice ports
                                          						during Cisco Unified Communications Manager fallback. |
| show call-manager- fallback voice-port | Displays output for the voice ports while Cisco Unified Communications Manager
                                          						is active. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						SRST 1.0 | This
                                          						command was introduced on the following platforms: Cisco 2600 series and Cisco
                                          						3600 series multiservice routers; Cisco IAD2420 series IADs. |
| 12.2(2)XT | Cisco
                                          						SRST 2.0 | This
                                          						command was implemented on Cisco 1750 and Cisco 1751 multiservice routers. |
| 12.2(8)T | Cisco
                                          						SRST 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco
                                          						SRST 2.0 | This
                                          						command was implemented on the Cisco 2600-XM and Cisco 2691 routers. |
| 12.2(11)T | Cisco
                                          						SRST 2.01 | This
                                          						command was integrated into Cisco IOS Release 12.2(11)T and implemented on the
                                          						Cisco 1760 routers. |
| 12.3(4)T | Cisco
                                          						SRST 3.0 | The
                                          						Version, ephone-dn,vand voice-port was added to output. |

| Field | Description |
|---|---|
| ephone-dn | Cisco IP
                                          					 phone directory number. |
| (no)
                                          					 huntstop | Whether
                                          					 or not huntstop is set. |
| number | Cisco IP
                                          					 phone number. |
| translate
                                          					 called | The
                                          					 configured translation rule. Can be called or calling, plus the tag number by
                                          					 which the rule set is referenced. |

| Command | Description |
|---|---|
| show call-manager- fallback all | Displays the detailed configuration of all Cisco IP phones, directory numbers,
                                          						voice ports, and dial peers in your network during Cisco Unified CallManager
                                          						fallback. |
| show call-manager- fallback dial-peer | Displays detailed configuration output for the dial peers in your network
                                          						during Cisco Unified CallManager fallback. |
| show call-manager- fallback voice-port | Displays output for the voice ports while Cisco Unified CallManager is active. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						SRST 1.0 | This
                                          						command was introduced on the following platforms: Cisco 2600 series and Cisco
                                          						3600 series multiservice routers, and Cisco IAD2420 series IADs. |
| 12.2(2)XT | Cisco
                                          						SRST 2.0 | This
                                          						command was implemented on Cisco 1750 and Cisco 1751 multiservice routers. |
| 12.2(8)T | Cisco
                                          						SRST 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco
                                          						SRST 2.0 | This
                                          						command was implemented on the Cisco 2600-XM and Cisco 2691 routers. |
| 12.2(11)T | Cisco
                                          						SRST 2.01 | This
                                          						command was integrated into Cisco IOS Release 12.2(11)T and implemented on the
                                          						Cisco 1760 routers. |

| Field | Description |
|---|---|
| voice-port | (Virtual)
                                          					 voice port. |
| station-id number | The phone
                                          					 number used for caller-ID purposes for calls made from this voice port. |

| Command | Description |
|---|---|
| show call-manager- fallback all | Displays the detailed configuration of all Cisco IP phones, directory numbers,
                                          						voice ports, and dial peers in your network during Cisco Unified Communications
                                          						Manager fallback. |
| show call-manager- fallback dial-peer | Displays detailed configuration output for the dial peers in your network
                                          						during Cisco Unified Communications Manager fallback. |
| show call-manager- fallback ephone-dn | Displays output for the Cisco IP phone directory numbers or virtual voice ports
                                          						during Cisco Unified Communications Manager fallback. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco
                                          						SRST 3.3 | This
                                          						command was introduced for Cisco Unified SRST. |
| 12.4(4)XC | Cisco
                                          						Unified CME 4.0 | This
                                          						command was introduced for Cisco Unified CME. |

| Field | Description |
|---|---|
| Credentials IP | Cisco
                                          					 Unified CME—IP address where the CTL provider is configured. Cisco
                                          					 Unified SRST—The specified IP address where certificates from Cisco Unified
                                          					 Communications Manager to the SRST router are received. |
| Credentials PORT | Cisco
                                          					 Unified CME—TCP port for credentials service communication. Default is 2444. Cisco
                                          					 Unified SRST—The port to which the SRST router connects to receive messages
                                          					 from the Cisco Unified IP phones. The port number is from 2000 to 9999. The
                                          					 default port number is 2445. |
| Trustpoint | Cisco
                                          					 Unified CME—CTL provider trustpoint label that will be used for TLS sessions
                                          					 with the CTL client. Cisco
                                          					 Unified SRST—The name of the trustpoint that is associated with the credentials
                                          					 service between the Cisco Unified Communications Manager client and the SRST
                                          					 router. |

| Command | Description |
|---|---|
| credentials | Enters
                                          						credentials configuration mode to configure a Cisco Unified CME CTL provider
                                          						certificate or a Cisco Unified SRST router certificate. |
| ctl-service admin | Specifies a user name and password to authenticate the CTL client during the
                                          						CTL protocol. |
| debug credentials | Sets
                                          						debugging on the credentials service that runs between a Cisco Unified CME CTL
                                          						provider and the CTL client or between a Cisco Unified SRST router and Cisco
                                          						Unified Communications Manager. |
| ip source-address (credentials) | Enables the Cisco Unified CME or SRST router to receive messages through the
                                          						specified IP address and port. |
| trustpoint (credentials) | Specifies the name of the trustpoint to be associated with a Cisco Unified CME
                                          						CTL provider certificate or with a Cisco Unified SRST router certificate. |

| mac-address | (Optional) Displays information for the phone with the specified MAC address. |
|---|---|
| phone-type | (Optional) Displays information for phones of the specified phone type. Valid
                                          						types are as follows: 7902 —Cisco Unified IP Phone 7902G. 7905 —Cisco Unified IP Phone 7905G. 7906 —Cisco Unified IP Phone 7905G. 7910 —Cisco Unified IP Phone 7910 and 7910G. 7911 —Cisco Unified IP Phone 7911G. 7912 — Cisco Unified IP Phone 7912G. 7914 — Cisco Unified IP Phone 7914 Expansion Module. 7920 — Cisco Unified Wireless IP Phone 7920. 7921 —Cisco Unified Wireless IP Phone 7921. 7931 — Cisco Unified Wireless IP Phone 7931G. 7935 — Cisco Unified IP Conference Station 7935. 7936 — Cisco Unified IP Conference Station 7936. 7940— Cisco Unified IP Phones 7940 and 7940G. 7941 —Cisco Unified IP Phone 7941G. 7941GE —Cisco Unified IP Phone 7941G-GE. 7942 —Cisco Unified IP Phone 7942. 7945 —Cisco Unified IP Phone 7945. 7960 — Cisco Unified IP Phones 7960 and 7960G . 7961 —Cisco Unified IP Phone 7961G. 7961GE —Cisco Unified IP Phone 7961G-GE. 7962 —Cisco Unified IP Phone 7962. 7965 —Cisco Unified IP Phone 7965. 7970 —Cisco Unified IP Phone 7970G. 7971 —Cisco Unified IP Phone 7971G-GE. 7975 —Cisco Unified IP Phone 7975 7985 —Cisco Unified IP Phone 7985. ata — Cisco ATA-186 or Cisco ATA-188. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						ITS 1.0 Cisco SRST 1.0 | This
                                          						command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						IAD2420 series. |
| 12.2(2)XT | Cisco
                                          						ITS 2.0 Cisco SRST 2.0 | This
                                          						command was implemented on the Cisco 1750 and Cisco 1751. |
| 12.2(8)T | Cisco
                                          						ITS 2.0 Cisco SRST 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725 and Cisco 3745. |
| 12.2(8)T1 | Cisco
                                          						ITS 2.0 Cisco SRST 2.0 | This
                                          						command was implemented on the Cisco 2600XM and Cisco 2691. |
| 12.2(11)T | Cisco
                                          						ITS 2.01 Cisco SRST 2.01 | The ata keyword
                                          						was added and this command was implemented on the Cisco 1760. |
| 12.2(11)YT | Cisco
                                          						ITS 2.1 Cisco SRST 2.1 | The 7914 keyword was added. |
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | The 7902 , 7905 , and 7912 keywords were added. |
| 12.3(7)T | Cisco
                                          						CME 3.1 Cisco SRST 3.1 | The 7920 and 7936 keywords were added. |
| 12.3(11)XL | Cisco
                                          						CME 3.2.1 Cisco SRST 3.2.1 | The 7970 keyword was added. |
| 12.3(14)T | Cisco
                                          						CME 3.3 Cisco SRST 3.3 | The 7971 keyword was added, and this command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.4(4)XC | Cisco
                                          						Unified CME 4.0 Cisco Unified SRST 4.0 | The 7911 , 7941 , 7941GE , 7961 , and 7961GE keywords were added. |
| 12.4(9)T | Cisco
                                          						Unified CME 4.0 Cisco Unified SRST 4.0 | The 7911 , 7941 , 7941GE , 7961 , and 7961GE keywords were integrated into Cisco IOS Release 12.4(9)T. |
| 12.4(6)XE | Cisco
                                          						Unified CME 4.0(2) | The 7931 keyword was added for Cisco Unified CME. |
| 12.4(4)XC4 | Cisco
                                          						Unified CME 4.0(3) | The 7931 keyword was added for Cisco Unified CME. |
| 12.4(11)T | Cisco
                                          						Unified CME 4.0(3) | The 7931 keyword for Cisco Unified CME was integrated in Cisco IOS Release 12.4(11)T. |
| 12.4(11)XJ2 | Cisco
                                          						Unified CME 4.1 Cisco Unified SRST 4.1 | The 7921 and 7985 keywords were introduced. |
| 12.4(15)T1 | Cisco
                                          						Unified CME 4.1(1) Cisco Unified SRST 4.1(1) | The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced. |
| 12.4(11)XW3 | Cisco
                                          						Unified CME 4.2 Cisco Unified SRST 4.2 | The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced. |
| 12.4(15)XY | Cisco
                                          						Unified CME 4.2(1) Cisco Unified SRST 4.2(1) | Emergency response location (ERL) information displays in the output. |
| 12.4(20)T | Cisco
                                          						Unified CME 7.0 Cisco Unified SRST 7.0 | This
                                          						command was integrated into Cisco IOS Release 12.4(20)T. |

| Field | Description |
|---|---|
| Active
                                          					 Call | An
                                          					 active call is in progress. |
| activeLine | Line
                                          					 (button) on the phone that is in use. Zero indicates that no line is in use. |
| auto-dial number | Intercom extension that automatically dials number . |
| button number : dn number | Phone
                                          					 button number and the extension (ephone-dn) dn-tag number associated with that
                                          					 button. |
| bytes | Total
                                          					 number of voice data bytes sent or received by the phone. |
| Called
                                          					 Dn, Calling Dn | Ephone-dn tag numbers of the called and calling ephone-dn. Set to -1 if the
                                          					 call is not to or from an ephone-dn, or if there is no active call. |
| cfa number | Call-forward-all to number is
                                          					 enabled for this extension. |
| CH1 CH2 | Status
                                          					 of channel 1 and, if this is a dual-line ephone-dn, the status of channel 2. |
| debug | 1
                                          					 indicates that debug for the phone is enabled. 0 indicates that debug is
                                          					 disabled. |
| DnD | Do Not
                                          					 Disturb is set on this phone. |
| DP tag | Not
                                          					 used. |
| ephone- number | Unique
                                          					 sequence number used to identify this phone during configuration (phone-tag). |
| IP | Assigned IP address of the Cisco Unified IP phone. |
| Jitter | Amount
                                          					 of variation (in milliseconds) of the time interval between voice packets
                                          					 received by the Cisco Unified IP phone. |
| keepalive | Number
                                          					 of keepalive messages received from the Cisco Unified IP phone by the router. |
| Latency | Estimated playout delay for voice packets received by the Cisco Unified IP
                                          					 phone. |
| line number | Button
                                          					 number on an IP phone. Line 1 is the button nearest the top of the phone. |
| Lost | Number
                                          					 of voice packets lost, as calculated by the Cisco Unified IP phone, on the
                                          					 basis of examining voice packet time-stamp and sequence numbers during playout. |
| Mac | MAC
                                          					 address. |
| Max
                                          					 Conferences | Maximum
                                          					 number of allowable conference calls and number of active conference calls. |
| max_line number | Maximum
                                          					 number of line buttons that can be configured on this phone. |
| mediaActive | 1
                                          					 indicates that an active conversation is in progress. 0 indicates that no
                                          					 conversation is ongoing. |
| monitor-ring | This
                                          					 button is set up as a monitor button. |
| number | Telephone or extension number associated with the Cisco Unified IP phone button
                                          					 and its dn-tag. |
| offhook | 1
                                          					 indicates that the phone is off-hook. 0 indicates that the phone is on-hook. |
| overlay | This
                                          					 button contains an overlay set. Use show ephone overlay to display the contents of overlay sets. |
| paging | 1
                                          					 indicates that the phone has received an audio page. 0 indicates that the phone
                                          					 has not received an audio page. |
| paging-dn | Ephone-dn that is dedicated for receiving audio pages on this phone. The
                                          					 paging-dn number is the number of the paging set to which this phone belongs. |
| Password | Authentication string that the phone user types when logging in to the
                                          					 web-based Cisco Unified CME GUI. |
| Port | Port
                                          					 used for TAPI transmissions. |
| REGISTERED | The
                                          					 Cisco Unified IP phone is active and registered. Alternative states are
                                          					 UNREGISTERED (indicating that the connection to the Cisco Unified IP phone was
                                          					 closed in a normal manner) and DECEASED (indicating that the connection to the
                                          					 Cisco Unified IP phone was closed because of a keepalive timeout). |
| reset | Pending
                                          					 reset. |
| reset_sent | Request
                                          					 for reset has been sent to the Cisco Unified IP phone. |
| ringing | 1
                                          					 indicates that the phone is ringing. 0 indicates that the phone is not ringing. |
| Rx Pkts | Number
                                          					 of received voice packets. |
| silent-ring | Silent
                                          					 ring has been set on this button and extension. |
| socket | TCP
                                          					 socket number used to connect to IP phone. |
| speed
                                          					 dial speed-tag:digit-string label-text | This
                                          					 button is a speed-dial button, assigned to the speed-dial sequence number speed-tag .
                                          					 It dials digit-string and displays the text label-text next to the button. |
| sub=3,
                                          					 sub=4 | Subtype
                                          					 3 means that one Cisco Unified IP Phone 7914 Expansion Module is attached to
                                          					 the main Cisco Unified IP Phones 7960 and 7960G, and subtype 4 means that two
                                          					 are attached. |
| Tag number | Dn-tag
                                          					 number, the unique sequence number that identifies an ephone-dn during
                                          					 configuration, followed by the type of ephone-dn it is. |
| TAPI
                                          					 Client IP Address | IP
                                          					 address of the PC running the TAPI client. |
| TCP
                                          					 socket | TCP
                                          					 socket number used to communicate with the Cisco Unified IP phone. This can be
                                          					 correlated with the output of other debug and show commands. |
| Telecaster model-number | Type
                                          					 and model of the Cisco Unified IP phone. This information is received from the
                                          					 phone during its registration with the router. |
| Tx Pkts | Number
                                          					 of transmitted voice packets. |
| Username | Username that the phone user types when logging in to the web-based Cisco
                                          					 Unified CME GUI. |

| Command | Description |
|---|---|
| show ephone-dn | Displays information about Cisco Unified IP phone extensions (ephone-dns). |
| show ephone login | Displays the login states of all local ephones. |
| show telephony-service all | Displays systemwide status and information for a Cisco Unified CME system. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| dn-tag | (Optional) Unique sequence number that is used during
                                          						configuration to identify a particular extension (ephone-dn). |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |

| Field | Description |
|---|---|
| ephone phone-tag | Phone
                                          					 identified with its unique phone-tag sequence number. |
| Pin
                                          					 enabled | TRUE
                                          					 indicates that a PIN has been defined for this phone. FALSE indicates that no
                                          					 PIN has been defined for this phone. |
| Logged-in | TRUE
                                          					 indicates that a phone user is currently logged in on this phone. FALSE
                                          					 indicates that no phone user is currently logged in on this phone. |

| Command | Description |
|---|---|
| login (telephony-service) | Defines
                                          						when users of IP phones in a Cisco Unified CME system are logged out
                                          						automatically. |
| pin | Sets
                                          						set a personal identification number (PIN) for an IP phone in a Cisco Unified
                                          						CME system. |
| show ephone | Displays statistical information about registered Cisco IP phones. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco
                                          						Unified CME 8.0 Cisco Unified SRST 8.0 | This
                                          						command was introduced. |
| 15.1(1)T | Cisco
                                          						Unified CME 8.0 Cisco Unified SRST 8.0 | This
                                          						command was integrated into Cisco IOS Release 15.1(1)T. |

| Command | Description |
|---|---|
| show
                                          						ephone-dn | Displays MOH group information for a phone directory number. |
| show
                                          						ephone summary | Displays the information about the MOH files in use |
| show
                                          						voice moh-group statistics | Displays the MOH subsystem statistics information |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |

| Field | Description |
|---|---|
| overlay number | Displays
                                          					 the contents of an overlay set, including each dn-tag and its associated
                                          					 extension number. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP phones. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |

| Field | Description |
|---|---|
| DeviceName | Device
                                          					 name. |
| CurrentPhoneLoad | Current
                                          					 phone firmware version. |
| PreviousPhoneLoad | Phone
                                          					 firmware version before last phone load. |
| LastReset | Reason
                                          					 for last reset of phone. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco CME 1.0 Cisco SRST 1.0 | This command was introduced. |
| 12.2(8)T | Cisco CME 2.0 Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						. |
| 15.0(1)XA | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was modified. The output was enhanced to show
                                          						IPv6 or IPv4 addresses configured on ephones. |
| 15.1(1)T | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was modified. The output was enhanced to show
                                          						voice-class stun-usage information. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                       						phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| number | Telephone number that is associated with an ephone. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone | Displays statistical information about registered Cisco IP
                                          						phones. |

| dn-tag | (Optional) For Cisco Unified CME, a unique sequence number that is used during
                                          						configuration to identify a particular extension (ephone-dn). (Optional) For Cisco Unified SRST, a destination number tag. The destination
                                          						number can be from 1 to 288. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						CME 1.0 Cisco SRST 1.0 | This
                                          						command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						IAD2420 series. |
| 12.2(2)XT | Cisco
                                          						CME 2.0 Cisco SRST 2.0 | This
                                          						command was implemented on the Cisco 1750 and Cisco 1751. |
| 12.2(8)T | Cisco
                                          						CME 2.0 Cisco SRST 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725 and Cisco 3745. |
| 12.2(8)T1 | Cisco
                                          						CME 2.0 Cisco SRST 2.0 | This
                                          						command was implemented on the Cisco 2600XM and Cisco 2691. |
| 12.2(11)T | Cisco
                                          						CME 2.01 Cisco SRST 2.01 | This
                                          						command was implemented on the Cisco 1760. |
| 12.3(4)T | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |

| Field | Description |
|---|---|
| Administrative State | Administrative (configured) state of the voice port. |
| alert | The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the call alerting state (for example, because the far-end phone
                                          					 rang but was not answered and the far-end system decided to drop the call
                                          					 rather than let the phone ring for too long). |
| answered (incoming) | The
                                          					 number of incoming calls that were actually answered (the phone goes off hook
                                          					 when ringing). |
| answered (outgoing) | The
                                          					 number of outgoing call attempts that were answered by the far end. |
| busy | The
                                          					 number of outgoing call attempts that got a busy response. |
| Call
                                          					 Disconnect Time Out | Not
                                          					 applicable to the Cisco IP phone. |
| called,
                                          					 calling | Extension numbers of called and calling parties. |
| Caller
                                          					 ID Info Follows | Information about the caller ID. |
| Call
                                          					 Ref | A
                                          					 unique per-call identifier used by the SCCP protocol. The Call Ref values are
                                          					 assigned sequentially within the Cisco CME–SCCP interface, so this value also
                                          					 indicates the total number of SCCP calls since the router was last rebooted. |
| chan | Channel
                                          					 number of an ephone-dn. |
| CODEC | Codec
                                          					 type. |
| Companding Type | Not
                                          					 applicable to the Cisco IP phone. |
| connect | The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the call connected state. |
| Connection Mode | Not
                                          					 applicable to the Cisco IP phone. |
| Connection Number | Not
                                          					 applicable to the Cisco IP phone. |
| Description | Not
                                          					 applicable to the Cisco IP phone. |
| Digit
                                          					 Duration Timing | Not
                                          					 applicable to the Cisco IP phone. |
| DN
                                          					 STATE | Ephone-dn tag number and state of the phone line associated with an extension. |
| Echo
                                          					 Cancellation... | Not
                                          					 applicable to the Cisco IP phone. |
| Echo
                                          					 Cancel Coverage | Not
                                          					 applicable to the Cisco IP phone. |
| EFXS | Voice
                                          					 port type. |
| Far-end
                                          					 disconnect at... | See
                                          					 connect, alert, hold, and ring. |
| Final
                                          					 Jitter | The
                                          					 final voice packet receive jitter reported by the IP phone at the end of the
                                          					 call. |
| hold | The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the call hold state (for example, if the caller was left on hold
                                          					 for too long and got tired of waiting). |
| incoming | The
                                          					 number of incoming calls presented (the phone rings). |
| In Gain | Not
                                          					 applicable to the Cisco IP phone. |
| Initial
                                          					 Time Out | Amount
                                          					 of time the system waits for an initial input digit from the caller. |
| Interdigit Time Out | Amount
                                          					 of time the system waits for a subsequent input digit from the caller. |
| Last 64
                                          					 far-end disconnect cause codes | See the
                                          					 Mappings of PSTN Cause Codes to SIP Event table for a list of public switch
                                          					 telephone network (PSTN) cause codes that can be sent as an ISDN cause
                                          					 information element (IE) and the corresponding Session Interface Protocol (SIP)
                                          					 event. |
| Latency | The
                                          					 final voice packet receive latency reported by the IP phone at the end of the
                                          					 call. |
| Lost | Number
                                          					 of lost packets. |
| Music
                                          					 On Hold Threshold | Not
                                          					 applicable to the Cisco IP phone. |
| No
                                          					 Interface Down Failure | State
                                          					 of the interface. |
| Noise
                                          					 Regeneration | Not
                                          					 applicable to the Cisco IP phone. |
| Non
                                          					 Linear... | Not
                                          					 applicable to the Cisco IP phone. |
| Operation State | Operational state of the voice port. |
| Out
                                          					 Attenuation | Not
                                          					 applicable to the Cisco IP phone. |
| outgoing | The
                                          					 number of outgoing call attempts. |
| Playout-delay Maximum | Not
                                          					 applicable to the Cisco IP phone. |
| Playout-delay... | Not
                                          					 applicable to the Cisco IP phone. |
| Port | Port
                                          					 number for the interface associated with the voice interface card. |
| Region
                                          					 Tone | Not
                                          					 applicable to the Cisco IP phone. |
| ring | The
                                          					 number of calls that were disconnected by the far-end device when the local IP
                                          					 phone was in the ringing state (for example, if the call was not answered and
                                          					 the caller hung up). |
| Ringing
                                          					 Time Out | Duration, in seconds, for which ringing is to continue if a call is not
                                          					 answered. Set with the timeouts ringing command. |
| Rx
                                          					 Pkts, bytes | Number
                                          					 of packets and bytes received during the current or last call. |
| Signal
                                          					 Level to phone, peak | For
                                          					 G.711 calls only, this parameter indicates the most recent voice signal level
                                          					 in the voice IP packets sent from the router to the IP phone. This parameter is
                                          					 valid only for VoIP or PSTN G.711 calls to the IP phones. This parameter is not
                                          					 valid for calls between local IP phones, or calls that use codecs other than
                                          					 G.711. The peak field indicates the peak signal level seen during the entire
                                          					 call. |
| Slot | Slot
                                          					 used in the voice interface card for this port. |
| Station
                                          					 name | Station
                                          					 name. |
| Station
                                          					 number | Station
                                          					 number. |
| Sub-unit | Subunit
                                          					 used in the voice interface card for this port. |
| Tx
                                          					 Pkts, bytes | Number
                                          					 of packets and bytes transmitted during the current call or last call. |
| Type of
                                          					 VoicePort | Voice
                                          					 port type. |
| VAD | Voice
                                          					 activity detection. |
| Voice
                                          					 card specific info | Information specific to the voice card. |
| VPM
                                          					 STATE | State
                                          					 indication for the VPM software component. |
| VTSP
                                          					 STATE | State
                                          					 indication for the VTSP software component. |
| Wait
                                          					 Release Time Out | Time
                                          					 that a voice port stays in the call-failure state while the router sends a busy
                                          					 tone, reorder tone, or out-of-service tone to the port. |

| PSTN
                                          					 Cause Code | Description | SIP
                                          					 Event |
|---|---|---|
| 1 | Unallocated number | 410
                                          					 Gone |
| 3 | No
                                          					 route to destination | 404 Not
                                          					 found |
| 16 | Normal
                                          					 call clearing | BYE |
| 17 | User
                                          					 busy | 486
                                          					 Busy here |
| 18 | No user
                                          					 responding | 480
                                          					 Temporarily unavailable |
| 19 | No
                                          					 answer from the user |
| 21 | Call
                                          					 rejected | 603
                                          					 Decline |
| 22 | Number
                                          					 changed | 302
                                          					 Moved temporarily |
| 27 | Destination out of order | 404 Not
                                          					 found |
| 28 | Address
                                          					 incomplete | 484
                                          					 Address incomplete |
| 29 | Facility rejected | 501 Not
                                          					 implemented |
| 31 | Normal
                                          					 unspecified | 404 Not
                                          					 found |
| 34 | No
                                          					 circuit available | 503
                                          					 Service unavailable |
| 38 | Network
                                          					 out of order |
| 41 | Temporary failure |
| 42 | Switching equipment congestion |
| 44 | Requested channel not available |
| 47 | Resource unavailable |
| 55 | Incoming class barred within CUG | 603
                                          					 Decline |
| 57 | Bearer
                                          					 capability not authorized | 501 Not
                                          					 implemented |
| 58 | Bearer
                                          					 capability not presently available |
| 63 | Service
                                          					 or option unavailable | 503
                                          					 Service unavailable |
| 65 | Bearer
                                          					 cap not implemented | 501 Not
                                          					 implemented |
| 79 | Service
                                          					 or option not implemented |
| 87 | User
                                          					 not member of CUG | 603
                                          					 Decline |
| 88 | Incompatible destination | 400 Bad
                                          					 Request |
| 95 | Invalid
                                          					 message |
| 102 | Recover
                                          					 on timer expiry | 408
                                          					 Request timeout |
| 111 | Protocol error | 400 Bad
                                          					 request |
| 127 | Interworking unspecified | 500
                                          					 Internal server error |
| Any
                                          					 code other than those listed above | 500
                                          					 Internal server error |

| Command | Description |
|---|---|
| show ephone-dn callback | Displays information about pending callbacks in a Cisco Unified CME or a Cisco
                                          						Unified SRST environment. |
| show ephone-dn loopback | Displays information about loopback ephone-dns that have been created in a
                                          						Cisco Unified CME or a Cisco Unified SRST environment. |
| show ephone-dn statistics | Displays display call statistics for a Cisco IP destination or for extensions
                                          						(ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST environment. |
| show ephone-dn summary | Displays brief information about Cisco IP phone destination numbers or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						CME 3.0 Cisco SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |

| Field | Description |
|---|---|
| DN 3
                                          					 (95021) CallBack pending to DN 1 (95021) | Callback
                                          					 originator is the extension with the dn-tag 1 (in this example), and the
                                          					 callback has been placed on the extension with the dn-tag 3 and the number
                                          					 95021. |
| age | Number of
                                          					 seconds since the callback was placed. |
| State for
                                          					 DN 3 is CH1... CH2... | Call
                                          					 states for channel 1 and channel 2, if any, of the extension that the callback
                                          					 is for. |

| Command | Description |
|---|---|
| show ephone-dn | Displays status and information for a Cisco IP phone destination number or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						CME 1.0 Cisco SRST 1.0 | This
                                          						command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						IAD2420 series. |
| 12.2(2)XT | Cisco
                                          						CME 2.0 Cisco SRST 2.0 | This
                                          						command was implemented on the Cisco 1750 and Cisco 1751. |
| 12.2(8)T | Cisco
                                          						CME 2.0 Cisco SRST 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725 and Cisco 3745. |
| 12.2(8)T1 | Cisco
                                          						CME 2.0 Cisco SRST 2.0 | This
                                          						command was implemented on the Cisco 2600XM and Cisco 2691. |
| 12.2(11)T | Cisco
                                          						CME 2.01 Cisco SRST 2.01 | This
                                          						command was implemented on the Cisco 1760. |

| Field | Description |
|---|---|
| Called,
                                          					 Calling | Called
                                          					 number and calling number when there is a call present. |
| CalledDn,
                                          					 CallingDn | Ephone-dn
                                          					 tag numbers of the called and calling ephone-dn. Set to -1 if the call is not
                                          					 to or from an ephone-dn, or if there is no active call. |
| callID | Internal
                                          					 call reference. This usage is the same as in other Cisco IOS voice gateway
                                          					 commands. |
| DN | Ephone-dn
                                          					 tag (sequence number). |
| Forward | Number of
                                          					 digits in the original called number to forward to the other ephone-dn in the
                                          					 loopback-dn pair. |
| G711... | G711Ulaw64k indicates G.711 codec, mu-law, 64000-bit stream. G711alaw64k
                                          					 indicates G.711 codec, A-law, 64000-bit stream. |
| Loopback to ... | Indicates the opposite ephone-dn in the loopback pair and the status of that
                                          					 ephone-dn. |
| Media | IP
                                          					 destination address, if any, for any voice packets that are passing through the
                                          					 loopback DN. |
| min,
                                          					 max | Lowest
                                          					 and highest dn-tag numbers of ephone-dns that are configured as loopback-dns. |
| prefix | Digit
                                          					 string to add to the beginning of forwarded called numbers. |
| retry | Number
                                          					 of seconds to wait before retrying the loopback target when is it busy. |
| srcCallID | Internal call reference for the destination. |
| ssrc | Real-time transport protocol (RTP) synchronization source (SSRC) of the most
                                          					 recent RTP packet. |
| Strip | Number
                                          					 of leading digits to strip before forwarding to the other extension in the
                                          					 loopback-dn pair. |
| vector | The
                                          					 following values describe the media path for voice packets that pass through
                                          					 the loopback-dn: 0—No
                                             						media path or not a loopback-dn path (inactive). 1—Normal path. Loopback-dn has identified the final media destination as a
                                             						local IP phone. The media IP address field shows a valid, non-zero value. 2—Hairpin. Media packets are routed back through paired loopback-dns. The final
                                             						destination is not known. For example, this can be a VoIP-to-VoIP call path by
                                             						a loopback-dn. 3—Hairpin. The final destination is an ephone-dn in a special mode such as
                                             						paging. 4—Loopback-dn chain has been detected, in which two loopback-dn pairs have been
                                             						connected together. 5—Loopback-dn chain has been detected in which more than two loopback-dn pairs
                                             						are connected in series. |

| Command | Description |
|---|---|
| loopback-dn | Creates a virtual loopback voice port (loopback-dn) to establish a demarcation
                                          						point for VoIP voice calls and supplementary services. |
| show ephone-dn | Displays status and information for a Cisco IP phone destination number or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment. |

| dn-tag | (Optional) Unique sequence number that is used during
                                          						configuration to identify a particular extension (ephone-dn). |
|---|---|
| statistics | Displays voice quality statistics on calls for a specified
                                          						extension or for all extensions. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ1 | Cisco CME 3.0 Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show ephone-dn | Displays status and information for a Cisco IP phone
                                          						destination number or for extensions (ephone-dns) in a Cisco Unified CME or a
                                          						Cisco Unified SRST environment. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						CME 1.0 Cisco SRST 1.0 | This
                                          						command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						IAD2420 series. |
| 12.2(2)XT | Cisco
                                          						CME 2.0 Cisco SRST 2.0 | This
                                          						command was implemented on the Cisco 1750 and Cisco 1751. |
| 12.2(8)T | Cisco
                                          						CME 2.0 Cisco SRST 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725 and Cisco 3745. |
| 12.2(8)T1 | Cisco
                                          						CME 2.0 Cisco SRST 2.0 | This
                                          						command was implemented on the Cisco 2600XM and Cisco 2691. |
| 12.2(11)T | Cisco
                                          						CME 2.01 Cisco SRST 2.01 | This
                                          						command was implemented on the Cisco 1760. |

| Field | Description |
|---|---|
| CODEC | Type of
                                          					 codec. |
| DN STATE | Status of
                                          					 the ephone-dn. |
| EFXS | Voice
                                          					 port type. |
| PORT | Port
                                          					 number (virtual) for this interface. The number that follows the last slash in
                                          					 the port number is the ephone-dn tag. For example, if the port number is
                                          					 50/0/1, the dn-tag is 1. |
| VAD | Voice
                                          					 activity detection status. |
| VPM
                                          					 STATE | State
                                          					 indication for the voice port module (VPM) software component. |
| VTSP
                                          					 STATE | State
                                          					 indication for the voice telephony service provider (VTSP) software component. |

| Command | Description |
|---|---|
| show ephone-dn | Displays status and information for a Cisco IP phone destination number or for
                                          						extensions (ephone-dns) in a Cisco Unified CME or a Cisco Unified SRST
                                          						environment. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						SIP SRST 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						SIP SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 15.0(1)XA | Cisco
                                          						SIP SRST 8.0 | This
                                          						command was updated to display the signaling transport protocol. |

| Field | Description |
|---|---|
| call-id | A unique
                                          					 ID assigned for each call. |
| contact | The
                                          					 contact IP address provided by the Cisco SIP IP phone. |
| destination | The
                                          					 destination IP address. |
| expires
                                          					 (sec) | The
                                          					 amount of time, in seconds, until registration expires. |
| Line | The phone
                                          					 number that maintains registration of SIP devices. |
| peer | When an
                                          					 SIP IP phone registers, an associated VoIP dial peer is automatically
                                          					 generated. This dial peer contains general information on how to contact the
                                          					 phone. The information includes the directory number or numbers associated with
                                          					 the phone and the IP address and protocol of the phone. |

| Command | Description |
|---|---|
| registrar server | Enables SIP registrar functionality. |

| Note | The Conn-Id that is suffixed with * is the client connections using SIP OAuth port. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Cupertino
                                          17.8.1a | The command output is updated to display the status, port details, and negotiated ciphers for SIP OAuth. |
| Cisco IOS XE 16.10.1 | The command output for show sip-ua connections tcp tls detail was updated to display the Cipher and the Curve-Size. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| voice emergency response location | Creates a tag for identifying an ERL for E911 services. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| address | Specifies a comma separated text entry (up to 250
                                          						characters) of an ERL’s civic address. |
| show voice emergency all | Displays all emergency response location information. |
| voice emergency response location | Creates a tag for identifying an ERL for E911 services. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| address | Specifies a comma separated text entry (up to 250
                                          						characters) of an ERL’s civic address. |
| elin | Specifies a PSTN number that will replace the caller’s
                                          						extension. |
| name | Specifies a string (up to 32-characters) used internally to
                                          						identify or describe the emergency response location. |
| subnet | Defines which IP phones are part of this ERL. |
| voice emergency response location | Creates a tag for identifying an ERL for the E911 services. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)T | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1 | This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was added to Cisco Unified CME. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| voice emergency response location | Creates a tag for identifying an ERL for the enhanced 911
                                          						service. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| location | Identifies locations within an emergency response zone. |
| voice emergency response location | Creates a tag for identifying an ERL for the enhanced 911
                                          						service. |
| voice emergency response zone | Creates an emergency response zone within which ERLs can be
                                          						grouped. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| showcall-manager-fallback all | Displays the detailed configuration of all Cisco IP phones, directory numbers, voice ports, and dial peers in your network during Cisco Unified Communications Manager fallback. |
| show ephone summary | Displays the information about the MOH files in use |
| show voice moh-group statistics | Displays the MOH subsystem statistics information |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| show ephone-dn | Displays MOH group information for a phone directory
                                          						number. |
| show ephone summary | Displays the information about the MOH files in use |
| show voice moh-group | Displays the MOH groups configured |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						SIP SRST 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						SIP SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.4(4)T | Cisco
                                          						CME 3.4 and Cisco SIP SRST 3.4 | This
                                          						command was added to Cisco CME. |
| 15.0(1)XA | Cisco
                                          						SIP SRST 8.0 | This
                                          						command was updated to display the signaling transport protocol. |
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 Cisco Unified SIP SRST 8.1 | This
                                          						command was modified. The output display was modified. |

| Field | Description |
|---|---|
| Pool Tag | Used with
                                          					 the all and pool keywords. Shows the assigned tag number of the current
                                          					 pool. |
| Config | Used with
                                          					 the all and pool keywords. Shows the voice register pool. |
| Network
                                          					 address and Mask | Used
                                          					 with the all and pool keywords. Shows network address and mask information if
                                          					 the id command is configured. |
| Number
                                          					 list, Pattern, and Preference | Used
                                          					 with the all and pool keywords. Shows the number command configuration. |
| Proxy
                                          					 IP address | Used
                                          					 with the all and pool keywords. Shows the proxy command configuration. |
| Default
                                          					 preference | Used
                                          					 with the all and pool keywords. Shows the default preference value of this
                                          					 pool. |
| Incoming called number | Used
                                          					 with the all and pool keywords. Shows the incoming called-number command configuration. |
| Translate outgoing called tag | Used
                                          					 with the all and pool keywords. Shows the translate-outgoing command configuration. |
| Class
                                          					 of Restriction List Tag | Used
                                          					 with the all and pool keywords. Shows the COR tag. |
| Incoming corlist name | Used
                                          					 with the all and pool keywords. Shows the cor command
                                          					 configuration. |
| Application | Used
                                          					 with the all and pool keywords. Shows the application command configuration for this pool. |
| Dialpeers created: | Used
                                          					 with the all and pool keywords. What follows is a list of all dial peers
                                          					 created and their contents. Dial-peer contents differ per application and are
                                          					 not described here. |
| Statistics | Used
                                          					 with the all , pool , and statistics keywords. Shows the registration statistics for this pool. |
| Active
                                          					 registrations | Used
                                          					 with the all , pool , and statistics keywords. Shows the current active registrations. |
| Total
                                          					 Registration Statistics | Used
                                          					 with the all , pool , and statistics keywords. Shows the total registration statistics for this pool. |
| Registration requests | Used
                                          					 with the all , pool , and statistics keywords. Shows the incoming registration requests. |
| Registration success | Used
                                          					 with the all , pool , and statistics keywords. Shows the successful registrations. |
| Registration failed | Used
                                          					 with the all , pool , and statistics keywords. Shows the failed registrations. |
| unRegister requests | Used
                                          					 with the all , pool , and statistics keywords. Shows the incoming unregister/registration expire requests. |
| unRegister success | Used
                                          					 with the all , pool , and statistics keywords. Reports the number of successful unregisters. |
| unRegister failed | Used
                                          					 with the all , pool , and statistics keywords. Reports the number of failed unregisters. |

| Command | Description |
|---|---|
| show sip-ua status registrar | Displays all the SIP endpoints currently registered with the contact address. |
| show voice register dial-peers | Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified SIP SRST or Cisco Unified CME register event |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |

| pool tag | Number of entries in attempted registrations table. Size
                                          						range from 0 to 50. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco CME. |
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SIP SRST 8.1 | This command was modified. Pool tag keyword- argument was
                                          						added. Command output display was also modified to display dial-peers specific
                                          						to a pool. |

| Command | Description |
|---|---|
| show sip-ua status registrar | Displays all the SIP endpoints currently registered with
                                          						the contact address. |
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME
                                          						configurations and register information. |
| show voice register pool | Displays all configuration information associated with a
                                          						particular voice register pool. |

| tag | Tag number of the voice register dn for which to display
                                          						information. Range is 1 to 750. |
|---|---|
| all | (Optional) Displays configuration information associated
                                          						with all voice register dns defined in a system. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |
| 15.1(2)T | Cisco CME 8.1 Cisco SIP SRST 8.1 | This command was modified.The display output now shows
                                          						pools that have DNs configured under them. All keyword was added to show
                                          						configuration information for all voice register dns defined in system. |

| Field | Description |
|---|---|
| Auto answer | Status of auto-answer feature defined with the auto-answer command. |
| Config | List of configuration options defined for this voice register
                                          					 dn. |
| Dn Tag | Tag number of the requested voice register dn. |
| Huntstop | Status of huntstop behavior defined with the huntstop command. |
| Number | Telephone or extension number set with the number command in voice register dn
                                          					 configuration mode. |
| Preference | Preference order set with the preference command in voice register dn configuration mode. |

| Command | Description |
|---|---|
| show voice register pool | Displays all configuration information associated with a
                                          						particular voice register pool. |
| show voice register dn all | Displays information associated with all the dns configured
                                          						in a system. |
| voice register dn | Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line. |

| Cisco IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4 | This
                                          						command was introduced. |
| 15.0(1)XA | Cisco
                                          						SIP SRST 8.0 | This
                                          						command was updated to display the signaling transport protocol. |
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 Cisco Unified SIP SRST 8.1 | This
                                          						command was modified.The output display now includes global statistics. |
| Cisco IOS XE Amsterdam 17.2.1r | Unified SRST 12.8 | This command was modified to display VRF information for Cisco 4000 Series Integrated Services Routers. |

| Field | Description |
|---|---|
| Date-format | Value of date-format command. |
| DST auto
                                          					 adjust | Setting
                                          					 of dst auto-adjust command. |
| Forwarding local | Setting
                                          					 of forwarding local command. |
| Generate
                                          					 text file | Setting
                                          					 of text file command. |
| Hold-alert | Setting
                                          					 of hold-alert command. |
| Load | Value
                                          					 of load command. |
| Max-dn | Reports
                                          					 the maximum number of SIP voice register directory numbers (dns) supported by
                                          					 the Cisco Unified SIP CME or Cisco Unified SIP SRST router as configured with
                                          					 the max-dn command. The maximum possible number is
                                          					 platform-dependent. |
| Max-pool | Reports
                                          					 the maximum number of SIP voice register pools supported by the Cisco Unified
                                          					 SIP SRST or Cisco Unified CME router as configured with the max-pool command. The maximum possible number is platform-dependent. |
| Max
                                          					 redirect number | Maximum
                                          					 number of redirects set with the max-redirect command. |
| Mode | Reports
                                          					 the mode as configured with the mode command. Value can be either Cisco Unified CME or Cisco Unified SIP SRST. |
| MWI
                                          					 registration | Setting
                                          					 of mwi command. |
| MWI
                                          					 stutter | Setting
                                          					 of mwi stutter command. |
| Time-format | Value
                                          					 of time-format command. |
| Time-zone | Number
                                          					 of the timezone selected with the timezone command. |
| TFTP
                                          					 path | Directory location of provisioning files for SIP phones that is specified with
                                          					 the tftp-path command. |
| Version | Reports
                                          					 the Cisco Unified SIP SRST or Cisco Unified CME version number. |
| VRF | Displays information on the associated VRF ID. |

| Command | Description |
|---|---|
| show sip-ua status registrar | Displays all the SIP endpoints currently registered with the contact address. |
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register dial-peers | Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified SIP SRST or Cisco Unified CME register event. |
| voice register global | Enters voice register global configuration mode in order to set global
                                          						parameters for all supported Cisco SIP phones in a Cisco Unified CME or Cisco
                                          						Unified SIP SRST environment. |

| pool-tag | Tag
                                          						number of the voice register pool for which information is displayed. Range is
                                          						1 to 262. Note The
                                                   						maximum number of pools is version and platform dependent. | Note | The
                                                   						maximum number of pools is version and platform dependent. |
|---|---|---|---|
| Note | The
                                                   						maximum number of pools is version and platform dependent. |
| all | Displays the information of all the voice register pools. |
| brief | (Optional) Displays brief information of all voice register pools. |

| Note | The
                                                   						maximum number of pools is version and platform dependent. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						SIP SRST | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						SIP SRST | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.4(4)T | Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4 | This
                                          						command was added to Cisco CME. |
| 12.4(15)XY | Cisco
                                          						Unified CME 4.2(1) Cisco Unified SIP SRST 4.2(1) | This
                                          						command was modified to include emergency response location information in the
                                          						output display. |
| 12.4(20)T | Cisco
                                          						Unified CME 7.0 Cisco Unified SIP SRST 7.0 | This
                                          						command was integrated into Cisco IOS Release 12.4(20)T. |
| 15.0(1)XA | Cisco
                                          						Unified CME 8.0 | This
                                          						command was modified to include logical partitioning class of restriction
                                          						(LPCOR) information in the output display. |
| 15.1(1)T | Cisco
                                          						Unified CME 8.0 | This
                                          						command was integrated into Cisco IOS Release 15.1(1)T. |
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 | This
                                          						command was modified. The all and brief keywords were added. Voice-class stun-usage information is displayed in the
                                          						output. |
| 15.2(2)T | Cisco
                                          						Unified CME 9.0 | This
                                          						command was modified to include conference admin, conference add mode, and
                                          						conference drop mode in the output display. |
| 15.2(4)M | Cisco
                                          						Unified CME 9.1 Cisco Unified SIP SRST 9.1 | This
                                          						command was modified to include Key Expansion Module (KEM) data in the output
                                          						display. |
| Cisco IOS XE Everest 16.6.1 | Unified SRST 12.0 | This command was modified to include the IPv6 address in the
                                          						output display for Unified SRST. |
| Cisco IOS XE Amsterdam 17.2.1r | Unified SRST 12.8 | This command was modified to include VRF information for Cisco 4000 Series Integrated Services Routers: show voice register pool all —Information for all the available configured pools. show voice register pool pool-tag —Information specific to a specific configured pool. |
| Cisco IOS XE Amsterdam 17.2.1r | Unified SRST 12.8 | Introduced support for YANG models. |

| Field | Description |
|---|---|
| Active
                                          					 registrations | Shows
                                          					 the current active registrations. |
| Application | Shows
                                          					 the application command configuration for this pool. |
| Call
                                          					 Waiting | Shows
                                          					 the call-waiting command configuration. |
| Class
                                          					 of Restriction List Tag | Shows
                                          					 the COR tag. |
| Conference add mode | Shows
                                          					 the current setting of the hardware conference privilege for adding
                                          					 participants. |
| Conference admin | Shows
                                          					 whether the Cisco Unified SIP IP phone is assigned as the hardware conference
                                          					 administrator or not. |
| Conference drop mode | Shows
                                          					 who can terminate an active ad-hoc hardware conference by hanging up. |
| Config | Shows
                                          					 the voice register pool. |
| Default
                                          					 preference | Shows
                                          					 the default preference value of this pool. |
| Dialpeers created | Lists
                                          					 all the dial peers created and their contents. Dial-peer contents differ for
                                          					 each application and are not described here. |
| DnD | Shows
                                          					 the setting of the dnd-control command. |
| DTMF
                                          					 Relay | Shows
                                          					 the setting of the dtmf-relay command. |
| Emergency response location | Shows
                                          					 the ephone’s emergency response location to which an emergency response team is
                                          					 dispatched when an emergency call is made. |
| Incoming called number | Shows
                                          					 the incoming called-number command configuration. |
| Incoming corlist name | Shows
                                          					 the cor command
                                          					 configuration. |
| keep-conference | Shows
                                          					 the status of the keep-conference command. |
| Lpcor
                                          					 Incoming | Shows
                                          					 the setting of the lpcor incoming command. |
| Lpcor
                                          					 Outgoing | Shows
                                          					 the setting of the lpcor outgoing command. |
| Lpcor
                                          					 Type | Shows
                                          					 the setting of the lpcor type command. |
| Mac
                                          					 address | Shows
                                          					 the MAC address of the Cisco Unified SIP IP phone as defined by the id command. |
| Network
                                          					 address and Mask | Shows
                                          					 network address and mask information when the id command is configured. |
| Number
                                          					 list, Pattern, and Preference | Shows
                                          					 the number command configuration. |
| Pool
                                          					 Tag | Shows
                                          					 the assigned tag number of the current pool. |
| Proxy
                                          					 IP address | Shows
                                          					 the proxy command configuration; that is, the IP address of the external SIP server. |
| Registration failed | Shows
                                          					 the failed registrations. |
| Registration requests | Shows
                                          					 the incoming registration requests. |
| Registration success | Shows
                                          					 the successful registrations. |
| Statistics | Shows
                                          					 the registration statistics for this pool. |
| Template | Shows
                                          					 the template-tag number for the template applied to the Cisco Unified SIP IP
                                          					 phone. |
| Total
                                          					 Registration Statistics | Shows
                                          					 the total registration statistics for this pool. |
| Translate outgoing called tag | Shows
                                          					 the translate-outgoing command configuration. |
| Type | Shows
                                          					 the phone type identified for the Cisco Unified SIP IP phone using the type command. |
| unRegister failed | Reports
                                          					 the number of failed unregisters. |
| unRegister requests | Shows
                                          					 the incoming unregister/registration expiry requests. |
| unRegister success | Reports
                                          					 the number of successful unregisters. |
| Username Password | Shows
                                          					 the values within the authentication credential. |
| VRF | Displays information on the associated VRF ID. |

| Command | Description |
|---|---|
| application (voice register pool) | Selects the session-level application for the dial peer associated with an
                                          						individual Cisco Unified SIP IP phone in a Cisco Unified CME environment or for
                                          						a group of phones in a Cisco Unified SIP SRST environment. |
| call-waiting (voice register pool) | Enables the call-waiting option on a SIP phone. |
| cor (voice register pool) | Configures a class of restriction on the VoIP dial peers associated with
                                          						directory numbers. |
| dnd-control (voice register template) | Enables the Do-Not-Disturb (DND) soft key on SIP phones. |
| dtmf-relay (voice register pool) | Specifies the list of dual-tone multifrequency (DTMF) relay methods that can be
                                          						used to relay DTMF audio tones between SIP endpoints. |
| id (voice register pool) | Explicitly identifies a locally available, individual Cisco Unified SIP IP
                                          						phone or, when running Cisco Unified SIP SRST, a set of Cisco Unified SIP IP
                                          						phones. |
| incoming called-number (dial peer) | Specifies a digit string that can be matched by an incoming call to associate
                                          						the call with a dial peer. |
| keep-conference (voice register pool) | Allows IP phone conference initiators to exit from conference calls and keep
                                          						the remaining parties connected. |
| lpcor incoming | Associates an incoming call with a logical partitioning class of restriction
                                          						(LPCOR) resource-group policy. |
| lpcor outgoing | Associates an outgoing call with an LPCOR resource-group policy. |
| lpcor type | Specifies the LPCOR type for an IP phone. |
| number (voice register pool) | Indicates the E.164 phone numbers that the registrar permits to handle the
                                          						Register message from a Cisco Unified SIP IP phone. |
| proxy (voice register pool) | Autogenerates additional VoIP dial peers to reach the main proxy whenever a
                                          						Cisco Unified SIP IP phone registers with a Cisco Unified SIP SRST gateway. |
| show sip-ua status registrar | Displays all the Cisco Unified SIP IP phones registered with the contact
                                          						address. |
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register dial-peer | Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified CME or Cisco Unified SIP SRST register event. |
| translate-outgoing (voice register pool) | Allows an explicit setting of translation rules on the VoIP dial peer to modify
                                          						a phone number dialed by any Cisco Unified IP phone user. |
| type (voice register pool) | Defines a phone type for a SIP phone. |
| voice register pool | Enters voice register pool configuration mode for Cisco Unified SIP IP phones. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| attempted-registrations size | Allows to set the size of the table that stores information
                                          						related to SIP phones that attempt to register and fail. |
| clear voice register attempted-registrations | Clears entries from the attempted-registration table. |

| brief | (Optional) Displays brief details of SIP phones that are in
                                          						connected state. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| show sip-ua calls | Displays active user agent client (UAC) and user agent
                                          						server (UAS) information on SIP calls |
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME
                                          						configurations and register information. |
| show voice register pool | Displays all configuration information associated with a
                                          						particular voice register pool. |

| ip-address | IPv4
                                          						address of the SIP phone . |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1 | This
                                          						command was introduced. |

| Field | Description |
|---|---|
| DN | Voice
                                          					 register DN tag of the line. |
| ID | Phone
                                          					 identification (ID) address. |
| IP
                                          					 Address | IP
                                          					 address of the SIP phone. |
| LN | Line
                                          					 number of the telephone number. |
| Number | Number of
                                          					 the phones that have a mac address. |
| Pool | Tag ID of
                                          					 the pool. |
| State | Registration state of the line. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |

| H.H.H | MAC
                                          						address of the SIP phone attempting to register. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1 | This
                                          						command was introduced. |

| Field | Description |
|---|---|
| DN | Voice
                                          					 register DN tag of the line. |
| ID | Phone
                                          					 identification (ID) address. |
| IP
                                          					 Address | IP
                                          					 address of the SIP phone. |
| LN | Line
                                          					 number of the telephone number. |
| Number | Number of
                                          					 the phones that have a mac address. |
| Pool | Tag ID of
                                          					 the pool. |
| State | Registration state of the line. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |

| network-address | Network
                                          						address of the SIP phone. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco
                                          						Unified SRST 8.1 | This
                                          						command was introduced. |

| Field | Description |
|---|---|
| DN | Directory
                                          					 number of the phone. |
| ID | Phone
                                          					 identification (ID) address. |
| IP
                                          					 Address | IP
                                          					 address and port number of the phones |
| LN | Line
                                          					 number of the phone. |
| Number | Number of
                                          					 the phone that have network address. |
| Pool | Shows the
                                          					 current pool. |
| State | Registration state. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |
| show voice register pool ip | Displays the voice register pool details of a phone with a specific IP address. |

| brief | (Optional) Displays brief details of SIP phones that are
                                          						currently on-hold. |
|---|---|

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco SIP SRST and Cisco CME configurations
                                          						and register information. |
| show sip-ua calls | Displays active user agent client (UAC) and user agent
                                          						server (UAS) information on SIP calls |
| show voice register pool | Displays all configuration information associated with a
                                          						particular voice register pool. |

| Cisco
                                          						IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1 | This
                                          						command was introduced. |
| 15.2(4)M | Cisco
                                          						Unified CME 9.1 Cisco Unified SIP SRST 9.1 | This
                                          						command was modified to display Key Expansion Module (KEM) details with the
                                          						phone type information. |

| Field | Description |
|---|---|
| Active
                                          					 registrations | Shows the
                                          					 current active registrations. |
| Application | Shows the application command configuration for this pool. |
| Call
                                          					 Waiting | Shows the
                                          					 setting of the call-waiting command. |
| Class
                                          					 of Restriction List Tag | Shows
                                          					 the COR tag. |
| Config | Shows
                                          					 the voice register pool. |
| Current
                                          					 phone-load | Shows
                                          					 the current version of the phone load. |
| Default
                                          					 preference | Shows
                                          					 the default preference value of this pool. |
| Dialpeers created | Results
                                          					 in a list of all dial peers created and their contents. Dial-peer contents
                                          					 differ for each application and are not described here. |
| DnD | Shows
                                          					 the setting of the dnd-control command. |
| DTMF
                                          					 Relay | Shows
                                          					 the setting of the dtmf-relay command. |
| Emergency response location | Shows
                                          					 the ephone’s emergency response location to which an emergency response team is
                                          					 dispatched when an emergency call is made. |
| Incoming called number | Shows
                                          					 the incoming called-number command configuration. |
| Incoming corlist name | Shows
                                          					 the cor command
                                          					 configuration. |
| keep-conference | Shows
                                          					 the status of the keep-conference command. |
| Lpcor
                                          					 Incoming | Shows
                                          					 the setting of the lpcor incoming command. |
| Lpcor
                                          					 Outgoing | Shows
                                          					 the setting of the lpcor outgoing command. |
| Lpcor
                                          					 Type | Shows
                                          					 the setting of the lpcor type command. |
| Mac
                                          					 address | Shows
                                          					 the MAC address of this SIP phone as defined by the id command. |
| Network
                                          					 address and Mask | Shows
                                          					 network address and mask information when the id command is configured. |
| Number
                                          					 list, Pattern, and Preference | Shows
                                          					 the number command configuration. |
| Pool
                                          					 Tag | Shows
                                          					 the assigned tag number of the current pool. |
| Previous phone-load | Shows
                                          					 the version of the previous phone load. |
| Proxy
                                          					 IP address | Shows
                                          					 the proxy command configuration; that is, the IP address of the external SIP server. |
| Registration failed | Shows
                                          					 the failed registrations. |
| Registration requests | Shows
                                          					 the incoming registration requests. |
| Registration success | Shows
                                          					 the successful registrations. |
| Statistics | Shows
                                          					 the registration statistics for this pool. |
| statistics time-stamps | Shows
                                          					 the registration statistics for this pool with specific time stamps. |
| Template | Shows
                                          					 the template-tag number for the template applied to this SIP phone. |
| Total
                                          					 Registration Statistics | Shows
                                          					 the total registration statistics for this pool. |
| Translate outgoing called tag | Shows
                                          					 the translate-outgoing command configuration. |
| Type | Shows
                                          					 the phone type identified for this SIP phone using the type command. |
| unRegister failed | Reports
                                          					 the number of failed unregisters. |
| unRegister requests | Shows
                                          					 the incoming unregister/registration expiry requests. |
| unRegister success | Reports
                                          					 the number of successful unregisters. |
| Username Password | Shows
                                          					 the values within the authentication credential. |

| Command | Description |
|---|---|
| application (voice register pool) | Selects the session-level application for the dial peer associated with an
                                          						individual Cisco Unified SIP IP phone in a Cisco Unified CME environment or for
                                          						a group of phones in a Cisco Unified SIP SRST environment. |
| call-waiting (voice register pool) | Enables the call-waiting option on a SIP phone. |
| cor (voice register pool) | Configures a class of restriction on the VoIP dial peers associated with
                                          						directory numbers. |
| dnd-control (voice register template) | Enables the Do-Not-Disturb (DND) soft key on SIP phones. |
| dtmf-relay (voice register pool) | Specifies the list of dual-tone multifrequency (DTMF) relay methods that can be
                                          						used to relay DTMF audio tones between SIP endpoints. |
| id (voice register pool) | Explicitly identifies a locally available, individual Cisco Unified SIP IP
                                          						phone or, when running Cisco Unified SIP SRST, a set of Cisco Unified SIP IP
                                          						phones. |
| incoming called-number (dial peer) | Specifies a digit string that can be matched by an incoming call to associate
                                          						the call with a dial peer. |
| keep-conference (voice register pool) | Allows IP phone conference initiators to exit from conference calls and keep
                                          						the remaining parties connected. |
| lpcor incoming | Associates an incoming call with a logical partitioning class of restriction
                                          						(LPCOR) resource-group policy. |
| lpcor outgoing | Associates an outgoing call with an LPCOR resource-group policy. |
| lpcor type | Specifies the LPCOR type for an IP phone. |
| number (voice register pool) | Indicates the E.164 phone numbers that the registrar permits to handle the
                                          						Register message from a Cisco Unified SIP IP phone. |
| proxy (voice register pool) | Autogenerates additional VoIP dial peers to reach the main proxy whenever a
                                          						Cisco Unified SIP IP phone registers with a Cisco Unified SIP SRST gateway. |
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register dial-peers | Displays details of all dynamically created VoIP dial peers associated with the
                                          						Cisco Unified SIP SRST or Cisco Unified CME register event. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |
| show voice register pool unregistered | Displays the details of voice register pools that do not have any phones
                                          						registered. |
| translate-outgoing (voice register pool) | Allows an explicit setting of translation rules on the VoIP dial peer to modify
                                          						a phone number dialed by any Cisco Unified IP phone user. |
| type (voice register pool) | Defines a phone type for a SIP phone. |
| voice register pool | Enters voice register pool configuration mode for SIP phones. |

| brief | (Optional) Displays brief details of SIP phones that are
                                          						currently in ringing state. |
|---|---|

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| show sip-ua calls | Displays active user agent client (UAC) and user agent
                                          						server (UAS) information on SIP calls |
| show voice register all | Displays all Cisco SIP SRST and Cisco CME configurations
                                          						and register information. |
| show voice register pool | Displays all configuration information associated with a
                                          						particular voice register pool. |

| number | Number
                                          						identifying a specific phone. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 Cisco Unified SRST 8.1 | This
                                          						command was introduced. |

| Field | Description |
|---|---|
| DN | Directory
                                          					 number of the phone. |
| ID | Phone
                                          					 identification (ID) address. |
| IP
                                          					 Address | IP
                                          					 address and port number of the phones |
| LN | Line
                                          					 number of the phone. |
| Number | Number of
                                          					 the phones. |
| Pool | Shows the
                                          					 current pool. |
| State | Registration state. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |
| show
                                          						voice register pool detail all | Displays the details of all the pools defined in the system. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco SIP SRST and Cisco CME configurations
                                          						and register information. |
| show voice register pool | Displays all configuration information associated with a
                                          						particular voice register pool. |
| show voice register pool registered | Displays details of phones that sucessfully register to
                                          						Cisco Unified CME or Cisco Unified SRST. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| Release | Modification |
|---|---|
| Cisco IOS XE Cupertino
                                          17.8.1a | This command was introduced. |

| global | (Optional) Displays aggregate statistics associated with the SIP phone
                                          						registration event. |
|---|---|
| pool
                                          						tag | (Optional) Displays registration pool statistics associated with a specific
                                          						pool tag. The maximum number of pools is version and platform dependent. Type ? to display
                                          						a list of values. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						SIP SRST 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						SIP SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.4(4)T | Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4 | This
                                          						command was added to Cisco CME. |
| 15.1(2)T | Cisco
                                          						CME 8.1 Cisco SIP SRST 8.1 | This
                                          						command was modified. The global and pool keywords and tag argument were added.
                                          						The output display was also modified to show more information about pools in
                                          						unregistered state and time-stamps of registration event. |

| Field | Description |
|---|---|
| Statistics: | Used
                                          					 with the all , pool , and statistics keywords. Shows the registration statistics for this pool. |
| Active
                                          					 registrations | Used
                                          					 with the all , pool , and statistics keywords. Shows the current active registrations. |
| Last
                                          					 Register Request Time | Used
                                          					 with all, pool, and statistics keywords. Shows details such as day, date, and
                                          					 time when the phones requested to register the last time. |
| Last
                                          					 unRegister Request Time | Used
                                          					 with all, pool, and statistics keywords. Shows details such as day, date, and
                                          					 time when the phones requested to unregister the last time. |
| Total
                                          					 Registration Statistics | Used
                                          					 with the all , pool , and statistics keywords. Shows the total registration statistics for this pool. |
| Registration requests | Used
                                          					 with the all , pool , and statistics keywords. Shows the incoming registration requests. |
| Registration success | Used
                                          					 with the all , pool , and statistics keywords. Shows the successful registrations. |
| Registration failed | Used
                                          					 with the all , pool , and statistics keywords. Shows the failed registrations. |
| unRegister requests | Used
                                          					 with the all , pool , and statistics keywords. Shows the incoming unregister/registration expire requests. |
| unRegister success | Used
                                          					 with the all , pool , and statistics keywords. Reports the number of successful unregisters. |
| unRegister failed | Used
                                          					 with the all , pool , and statistics keywords. Reports the number of failed unregisters. |
| Global
                                          					 statistics | Used
                                          					 with the statistics keyword. Details all active registrations. |
| Register pool number statistics | Used
                                          					 with the statistics keyword. Details specific pool statistics. |

| Command | Description |
|---|---|
| show voice register all | Displays all Cisco Unified SIP SRST and Cisco Unified CME configurations and
                                          						register information. |
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |
| show
                                          						voice register pool attempted-registrations | Displays the details of phones that attempt to register with Cisco Unified CME
                                          						or Cisco Unified SRST and fail. |

| crypto-tag | Unique number that is assigned to the voice class. The range is 1–10000. This number maps to the tag created using the voice class srtp-crypto command available in global configuration mode. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Everest 16.5.1b | This command was introduced. |
| Cisco IOS XE Cupertino
                                             17.8.1a | Implemented voice class srtp-crypto tag under voice register pool. |

| Note | Ensure that SRTP voice-class is created using the voice class srtp-crypto crypto-tag command before executing the srtp-crypto crypto tag command to apply the crypto-tag under global or tenant configuration mode. |
|---|---|

| Note | voice class srtp-crypto must be configured before adding to a voice register pool. |
|---|---|

| Command | Description |
|---|---|
| voice class sip srtp-crypto | Enters voice class configuration mode and assigns an identification tag for a srtp-crypto voice class. |
| crypto | Specifies the preference for the SRTP cipher-suite that will be offered by Cisco Unified Border Element (CUBE) in the SDP
                                          in offer and answer. |
| show sip-ua calls | Displays active user agent client (UAC) and user agent server (UAS) information on Session Initiation Protocol (SIP) calls. |
| show sip-ua srtp | Displays Session Initiation Protocol (SIP) user-agent (UA) Secure Real-time Transport Protocol (SRTP) information. |

| IPaddress | IP address that identifies which IP phones are part of the
                                          						ERL. |
|---|---|
| mask | IP subnet mask for the network segment that is part of the
                                          						ERL. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)T | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1 | This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was added to Cisco Unified CME. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| elin | Specifies a PSTN number that will replace the caller’s
                                          						extension. |

| primary | Sets the system message for Cisco IP phones that can
                                          						support static text messages during fallback, such as the Cisco IP Phone 7940
                                          						and the Cisco IP Phone 7960. |
|---|---|
| primary-string | Text string of less than 32 characters. |
| secondary | Sets the system message for Cisco IP phones that do not
                                          						support static text messages and that have a limited display space, such as the
                                          						Cisco IP Phone 7910. |
| secondary-string | Text string of less than 20 characters. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST feature support and enters call-manager-fallback configuration
                                          						mode. |

| string | Message that displays on SIP phones after the phones
                                          						failover to Cisco Unified SRST. String can contain a maximum of 32 alphanumeric
                                          						characters. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified SRST 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |
| Cisco IOS XE Amsterdam 17.2.1r | Cisco Unified SIP SRST 12.8 | Introduced support for YANG models. |

| Command | Description |
|---|---|
| show voice register global | Displays all global configuration parameters associated
                                          						with SIP phones. |

| 12 | Sets format to 12-hour increments. |
|---|---|
| 24 | Sets format to 24-hour increments. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco SRST 2.0 | This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 and Cisco 3600 series multiservice routers,
                                          						Cisco IAD2420 series IADs. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified Survivable Remote Site Telephony
                                          						(SRST) support and enters call-manager-fallback configuration mode. |

| seconds | Number of seconds after connection to a busy destination
                                          						before a transferred call is disconnected. Range is from 0 to 30 seconds.
                                          						Default is 10. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(8)T | Cisco SRST 2.0 | This command was introduced. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified Survivable Remote Site Telephony
                                          						(SRST) and enters call-manager-fallback configuration mode. |

| seconds | Interdigit timeout duration, in seconds, for all Cisco IP
                                          						phones. Valid entries are integers from 2 to 120. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XB | Cisco SRST 1.0 | This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers; Cisco IAD2420
                                          						series IADs; Cisco 7200 series routers. |
| 12.2(2)XT | Cisco SRST 2.0 | This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified Survivable Remote Site Telephony
                                          						(SRST) support and enters call-manager-fallback configuration mode. |
| timeouts interdigit (voice port) | Configures the interdigit timeout value for a specified
                                          						voice port. |

| seconds | The duration, in seconds, for which a voice port allows
                                          						ringing to continue if a call is not answered. The range is from 5 to 60000. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified Survivable Remote Site Telephony
                                          						(SRST) and enters call-manager-fallback configuration mode. |

| max-length | Maximum length of the transfer number. Range is 3 to 16. |
|---|---|

| Release | Modification |
|---|---|
| 15.3(2)T | This command was introduced. |

| Command | Description |
|---|---|
| voice register pool | Enters voice register pool configuration mode and creates a
                                          						pool configuration for a SIP IP phone in Cisco Unified CME or for a set of SIP
                                          						phones in Cisco Unified SIP SRST |
| voice register template | Enters voice register template configuration mode and
                                          						defines a template of common parameters for SIP phones. |

| new-call | Dialed digits are collected from new call leg. Default
                                          						value. |
|---|---|
| orig-call | Dialed digits are collected from original call leg. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 Cisco Unified SRST 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| transfer-mode | Specifies the type of call transfer for an individual
                                          						directory number that uses the ITU-T H.450.2 standard. |
| transfer-pattern (telephony-service) | Allows the transfer of calls to phones outside the local
                                          						Cisco Unified CME network. |
| transfer - system | Specifies the call transfer method for all IP phones on a
                                          						Cisco Unified CME router using the ITU-T H.450.2 standard. |

| transfer-pattern | String
                                          						of digits for permitted call transfers. Wildcards are allowed. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						SRST 1.0 | This
                                          						command was introduced on the following platforms: Cisco 2600 series and Cisco
                                          						3600 series multiservice routers, and Cisco IAD2420 series IADs. |
| 12.2(2)XT | Cisco
                                          						SRST 2.0 | This
                                          						command was implemented on Cisco 1750 and Cisco 1751 multiservice routers. |
| 12.2(8)T | Cisco
                                          						SRST 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco
                                          						SRST 2.0 | This
                                          						command was implemented on the Cisco 2600-XM and Cisco 2691 routers. |
| 12.2(11)T | Cisco
                                          						SRST 2.01 | This
                                          						command was integrated into Cisco IOS Release 12.2(11)T and implemented on the
                                          						Cisco 1760 routers. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables
                                          						Cisco Unified Survivable Remote Site Telephony (SRST) support and enters
                                          						call-manager-fallback configuration mode. |

| Release | Modification |
|---|---|
| 15.3(2)T | This command was introduced. |

| Command | Description |
|---|---|
| voice register pool | Enters voice register pool configuration mode and creates a
                                          						pool configuration for a Cisco Unified SIP IP phone in Cisco Unified CME or for
                                          						a set of Cisco Unified SIP IP phones in Cisco Unified SIP SRST. |
| voice register template | Enters voice register template configuration mode and
                                          						defines a template of common parameters for Cisco Unified SIP IP phones. |

| blind | Transfers calls without consultation using a single phone
                                          						line and the Cisco proprietary method. The keyword blind is not recommended. Use
                                          						either the full- blind or full-consult keyword instead. |
|---|---|
| full-blind | Transfers calls without consultation using H.450.2 standard
                                          						methods. |
| full-consult | Transfers calls using H.450.2 with consultation using the
                                          						second phone line if available, or the calls fall back to full-blind if the
                                          						second line is unavailable. |
| local-consult | Transfers calls with local consultation using the second
                                          						phone line if available, or the calls fall back to blind for nonlocal
                                          						consultation or transfer target. This method is intended for use primarily in
                                          						VoFR networks because the Cisco VoFR call-transfer protocol does not support an
                                          						end-to-end transfer with consultation mechanism. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Note | Note: The keyword blind is not recommended. Use either the full- blind or full-consult keyword instead. |
|---|---|

| Command | Description |
|---|---|
| call application voice | Defines an application, indicates the location of the
                                          						corresponding Tcl files that implement the application, and loads the selected
                                          						Tcl script. |
| call-manager-fallback | Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode. |

| called | Translation rule to apply to the number called by a Cisco
                                          						IP phone. |
|---|---|
| calling | Translation rule to apply to the calling party number sent
                                          						in the call setup message for calls originated from a Cisco IP phone. |
| translation-rule-tag | Tag number by which the rule set is referenced. This is an
                                          						arbitrarily chosen number. The range is from 1 to 2147483647. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco SRST 2.0 | This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, Cisco IAD2420 series IADs. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified Survivable Remote Site Telephony
                                          						(SRST) support and enters call-manager-fallback configuration mode. |
| translation-profile (call-manager-fallback) | Assigns a translation profile for incoming or outgoing call
                                          						legs on a Cisco IP phone. |
| translation-rule | Creates a translation name and enters translation-rule
                                          						configuration mode. |

| called | Called party requires translation. |
|---|---|
| calling | Calling party requires translation. |
| rule-tag | The rule-tag is an arbitrarily chosen number by which the
                                          						rule set is referenced. The range is from 1 to 2147483. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco CME. |

| Command | Description |
|---|---|
| alias (voice register pool) | Allows Cisco SIP IP phones to handle inbound PSTN calls to
                                          						telephone numbers that are unavailable when the main proxy is not available. |
| id (voice register pool) | Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones. |
| translate-outgoing (dial-peer) | Applies a translation rule to manipulate dialed digits on
                                          						an outbound POTS or VoIP call leg. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| incoming | Specifies that this translation profile handles incoming
                                          						calls. |
|---|---|
| outgoing | Specifies that this translation profile handles outgoing
                                          						calls. |
| name | Name of the translation profile. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)T | Cisco SRST 3.2 | This command was introduced. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco SRST support and enters call-manager-fallback
                                          						configuration mode. |
| show voice translation-profile | Displays the configuration of a translation profile. |
| translate (call-manager- fallback) | Applies a translation rule to modify the phone number
                                          						dialed or received by any Cisco IP phone user during Communications Manager
                                          						fallback. |
| translation-rule | Creates a translation name and enters translation-rule
                                          						configuration mode to apply rules to the translation name. |
| voice translation-profile | Defines a translation profile for voice calls. |

| incoming | Specifies that this translation profile handles incoming
                                          						calls. |
|---|---|
| outgoing | Specifies that this translation profile handles outgoing
                                          						calls. |
| name | Name of the translation profile. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified SIP SRST 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified SIP SRST 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |
| Cisco IOS XE Dublin
                                                17.10.1a | Unified SRST 14.3 | Introduced support for YANG models. |

| Command | Description |
|---|---|
| show voice translation-profile | Displays the configuration of a translation profile. |
| translate (translation profiles) | Assigns a translation rule to a translation profile. |
| voice translation-profile | Defines a translation profile for voice calls. |

| v1.0 | Enables TLS version 1.0. Note In the Cisco IOS XE 17.18.2 release, a security warning message appears for configurations using TLS versions below 1.2 and associated weaker ciphers.
                                                   For secure configurations, we recommend configuring stronger ciphers with TLS version 1.2 or higher. Starting from Cisco IOS XE 26.1.1 release, the insecure TLS versions (1.0, 1.1) and associated ciphers are not supported in default configurations. However,
                                       insecure configurations are supported in system mode insecure operation-mode. | Note | In the Cisco IOS XE 17.18.2 release, a security warning message appears for configurations using TLS versions below 1.2 and associated weaker ciphers.
                                                   For secure configurations, we recommend configuring stronger ciphers with TLS version 1.2 or higher. |
|---|---|---|---|
| Note | In the Cisco IOS XE 17.18.2 release, a security warning message appears for configurations using TLS versions below 1.2 and associated weaker ciphers.
                                                   For secure configurations, we recommend configuring stronger ciphers with TLS version 1.2 or higher. |
| v1.1 | Enables TLS version 1.1. Note In the Cisco IOS XE 17.18.2 release, a security warning message appears for configurations using TLS versions below 1.2 and associated weaker ciphers.
                                                   For secure configurations, we recommend configuring stronger ciphers with TLS version 1.2 or higher. Starting from Cisco IOS XE 26.1.1 release, the insecure TLS versions (1.0, 1.1) and associated ciphers are not supported in default configurations. However,
                                       insecure configurations are supported in system mode insecure operation-mode. | Note | In the Cisco IOS XE 17.18.2 release, a security warning message appears for configurations using TLS versions below 1.2 and associated weaker ciphers.
                                                   For secure configurations, we recommend configuring stronger ciphers with TLS version 1.2 or higher. |
| Note | In the Cisco IOS XE 17.18.2 release, a security warning message appears for configurations using TLS versions below 1.2 and associated weaker ciphers.
                                                   For secure configurations, we recommend configuring stronger ciphers with TLS version 1.2 or higher. |
| v1.2 | Enables TLS version 1.2. |
| v1.3 | Enables TLS version 1.3. |
| sha2 | Enables SHA2 ciphers with TLS version 1.2 or 1.3. |

| Note | In the Cisco IOS XE 17.18.2 release, a security warning message appears for configurations using TLS versions below 1.2 and associated weaker ciphers.
                                                   For secure configurations, we recommend configuring stronger ciphers with TLS version 1.2 or higher. |
|---|---|

| Note | In the Cisco IOS XE 17.18.2 release, a security warning message appears for configurations using TLS versions below 1.2 and associated weaker ciphers.
                                                   For secure configurations, we recommend configuring stronger ciphers with TLS version 1.2 or higher. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| Cisco IOS XE 26.1.1 | Unified SRST 15.0 | The insecure TLS versions (1.0, 1.1) and associated ciphers are not supported in default configurations. However, insecure
                                       configurations are supported in system mode insecure operation-mode. |
| Cisco IOS XE 17.18.2 | Unified SRST 15.0 | Security warnings for usage of legacy TLS and associated weaker ciphers. |
| Cisco IOS XE 17.14.1a | Unified SRST 14.4 | This command is enhanced to support TLS version 1.3 ciphers. In addition, SHA2 cipher support for TLS version 1.3 is introduced. Introduced support for YANG model. |
| Cisco IOS XE Cupertino
                                             17.8.1a | Unified SRST 14.2 | This command is enhanced to limit TLS1.2 to using SHA2 ciphers only. |
| Cisco IOS XE Fuji 16.9.1 | Unified SRST 12.3 | This command was introduced. |

| Command | Description |
|---|---|
| transport (voice-register-pool) | Defines
                                          						the default transport type supported by a new phone. |

| trustpoint-name | Name of the trustpoint to be associated with the Cisco
                                          						Unified CME CTL provider certificate or the Cisco Unified SRST device
                                          						certificate. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco SRST 3.3 | This command was introduced for Cisco Unified SRST. |
| 12.3(14)T | Cisco Unified CME 4.0 | This command was introduced for Cisco Unified CME. |

| Command | Description |
|---|---|
| credentials | Provides the Cisco Unified CME CTL provider certificate or
                                          						the Cisco Unified SRST router certificate and enters credentials configuration
                                          						mode. |
| ctl-service admin | Specifies a user name and password to authenticate the CTL
                                          						client during the CTL protocol. |
| debug credentials | Sets debugging on the credentials service. |
| ip source-address (credentials) | Enables the router to receive messages through the
                                          						specified IP address and port. |
| show credentials | Displays the credentials settings. |

| country-code | The following ISO-3166 codes are available to Cisco Unified
                                          						Survivable Remote Site Telephony (SRST) systems running under Cisco Unified
                                          						Communications Manager V3.2 or later: DE —German. DK —Danish. ES —Spanish. FR —French. IT —Italian. JP —Japanese Katakana (available
                                             						  under Cisco Unified Communications Manager V4.0 or later). NL —Dutch. NO —Norwegian. PT —Portuguese. RU —Russian. SE —Swedish. US —United States English
                                             						  (default). |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(11)YT | Cisco SRST 2.1 | This command was introduced for use on the Cisco IP Phone
                                          						7940 and Cisco IP Phone 7960 for Cisco SRST systems running Cisco
                                          						Communications Manager V3.2. Support includes country codes for France,
                                          						Germany, Italy, Portugal, Spain, and the United States (default). |
| 12.3(4)T | Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(7)XL | Cisco SRST 3.1.1 | The JP keyword was added, providing support
                                          						for Japanese Katakana. |
| 12.3(11)T | Cisco SRST 3.2 | This command was integrated into Cisco IOS Release
                                          						12.3(11)T and support was increased to include the Cisco Unified IP Phone 7905G
                                          						and Cisco Unified IP Phone 7912G. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode. |

| index | Unique
                                          						index number. Range: 1 to 8. |
|---|---|
| type | Type of
                                          						service url button. Following types of url service buttons are available: myphoneapp: My phone
                                             						  application configured under phone user interface. em: Extension Mobility snr: Single Number Reach voicehuntgroups: Voice Hunt
                                             						  Groups park-list: Displays list of
                                             						  parked calls |
| url
                                          						name | Service
                                          						url with maximum length of 31 characters. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco
                                          						Unified Enhanced SRST 8.5 | This
                                          						command was introduced. |
| 15.4(3)M | Cisco
                                          						Unified Enhanced SRST 10.5 | This
                                          						command was modified. |

| Command | Description |
|---|---|
| show telephony-service ephone-template | Displays the contents of all the ephone-templates defined. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 Cisco Unified SRST 4.3 | This command was introduced. |

| Command | Description |
|---|---|
| device-id | Specifies the device ID for a phone type. |
| type | Assigns the phone type to an SCCP phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified SRST 4.0 | This command was introduced. |

| Command | Description |
|---|---|
| show call active video | Displays call information for SCCP video calls in progress. |
| show call history video | Displays call history information for SCCP video calls. |
| video (telephony-service) | Enters video configuration mode to set video parameters for
                                          						all applicable Cisco IP phones associated with a Cisco Unified CME router. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(11)YT | Cisco SRST 2.1 | This command was introduced for Cisco Survivable Remote
                                          						Site Telephony (SRST). |
| 12.2(2)XT | Cisco CME 2.0 | This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series, Cisco 3600 series, and Cisco IAD2420
                                          						series. |
| 12.2(8)T | Cisco CME 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745. |
| 12.2(8)T1 | Cisco CME 2.0 | This command was implemented on the Cisco 2600XM and Cisco
                                          						2691. |
| 12.2(11)T | Cisco CME 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760. |

| Command | Description |
|---|---|
| pattern direct (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when a user presses the Messages button on a
                                          						phone. |
| pattern ext-to-ext busy (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension reaches a busy
                                          						extension and the call is forwarded to voice mail. |
| pattern ext-to-ext no-answer (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext busy (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext no-answer (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail. |

| tag | Voice class tls-cipher tag. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Cupertino
                                             17.8.1a | Introduced voice class tls-cipher command. |
| Cisco IOS XE Dublin
                                             17.10.1a | Introduced support for YANG models. |

| tag | A number used to identify voice class tls profile. The range is 1-10000. There is no default value. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Cupertino
                                                17.8.1a | tls-profile command is enhanced to include <tag>. |
| Cisco IOS XE Amsterdam 17.3.1a | This command was introduced. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Note | tls-cipher should be created before adding to tls-profile . |
|---|---|

| Command | Description |
|---|---|
| trustpoint | Creates a trustpoint to store the devices certificate that is generated as part of the enrollment process using Cisco IOS
                                          public-key infrastructure (PKI) commands. |
| description | Provides a description for the TLS profile group. |
| client-vtp | Assigns a client verification trustpoint. |
| cipher | Configures cipher setting. |
| cn-san | Enables server identity validation through Common Name (CN) and Subject Alternate Name (SAN) fields in the server certificate
                                          during client-side SIP /TLS connections |
| sni send | Enables TLS Server Name Indication (SNI) during the initial TLS handshake process. |
| crypto signaling | Identifies the trustpoint or the tls-profile tag that is used during the TLS handshake process. |

| tag | Unique number that identifies this ERL tag. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)T | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1 | This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | Address and name commands introduced under voice emergency response location command. This command was added
                                          						for Cisco Unified CME. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| address | Specifies a comma separated text entry (up to 250
                                          						characters) of an ERL’s civic address. |
| elin | Specifies a PSTN number that will replace the caller’s
                                          						extension. |
| name | Specifies a string (up to 32-characters) used internally to
                                          						identify or describe the emergency response location. |
| subnet | Defines which IP phones are part of this ERL. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| callback | Default phone number to contact if a 911 callback cannot
                                          						find the last 911 caller from the ERL. |
| elin | E.164 number used as the default ELIN if no matching ERL to
                                          						the 911 caller’s IP phone address is found. |
| expiry | Number of minutes a 911 call is associated to an ELIN in
                                          						case of a callback from the 911 operator. |
| logging | Syslog informational message printed to the console every
                                          						time an emergency call is made. |

| tag | Identifier (1-100) for the voice emergency response zone. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| location | Identifies locations within an emergency response zone and
                                          						optionally assigns a priority order to the location. |

| hunt-tag | Unique sequence number that identifies the hunt group.
                                          						Range is 1 to 100. |
|---|---|
| longest-idle | Allows an incoming call to go first to the number that has
                                          						been idle the longest for the number of hops specified when the hunt group was
                                          						defined. The longest-idle time is determined from the last time that a phone
                                          						registered, reregistered, or went on-hook. |
| parallel | Allows an incoming call to simultaneously ring all the
                                          						numbers in the hunt group member list. |
| peer | Allows a round-robin selection of the first extension to
                                          						ring. Ringing proceeds in a circular manner from left to right. The round-robin
                                          						selection starts with the number left of the number that answered when the
                                          						hunt-group was last called. |
| sequential | Allows an incoming call to ring all the numbers in the
                                          						left-to-right order in which they were listed when the hunt group was defined. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was modified to add support for Cisco Unified
                                          						SCCP IP phones. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |
| 15.2(4)M | Cisco Unified SIP SRST 9.1 | This command was introduced in Cisco Unified SIP SRST 9.1. |

| Command | Description |
|---|---|
| final (voice hunt-group) | Defines the last extension in a voice hunt group. |
| hops (voice hunt-group) | Defines the number of times that a call is redirected to
                                          						the next phone number in a peer voice hunt-group list before proceeding to the
                                          						final phone number. |
| list (voice hunt-group) | Defines the phone numbers that participate in a voice hunt
                                          						group. |
| max-redirect | Changes the number of times that a call can be redirected
                                          						by call forwarding or transfer within a Cisco Unified CME system. |
| pilot (voice hunt-group) | Defines the phone number that callers dial to reach a voice
                                          						hunt group. |
| timeout (voice hunt-group) | Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the hunt-group list and defines
                                          						the last phone number in the hunt group. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco
                                          						Unified Enhanced SRST 10.5 | This
                                          						command was introduced. |

| Command | Description |
|---|---|
| show voice hunt-groups | Displays voice-hunt group configuration, current status, and statistics. |

| tag | Specifies a moh-group number tag (1-5) to be used for music
                                          						on hold group parameters. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was introduced. |

| moh | Enables music on hold from a flash audio feed. |
|---|---|
| multicast moh | Enables multicast of the music-on-hold audio stream. |
| extension-range | Defines extension range for a clients calling a
                                          						voice-moh-group. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |
| 15.0(1)XA | Cisco SIP SRST 8.0 | This command was updated to display the signaling transport
                                          						protocol. |
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | The no form of the command was modified. |
| Cisco IOS XE Cupertino 17.7.1a | Cisco Unified SIP SRST 12.8 | Introduced support for YANG models. |
| Cisco IOS XE Cupertino
                                                17.8.1a | Cisco Unified SIP SRST 12.8 | Added the new CLI commands key-server , and key-server source-interface <options> under sip-oauth for voice register global mode. |

| Command | Description |
|---|---|
| allow connections sip to sip | Allows connections between SIP endpoints in a Cisco
                                          						multiservice IP-to-IP gateway. |
| application (voice register global) | Selects the session-level application for all dial peers
                                          						associated with SIP phones. |
| mode (voice register global) | Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified system. |

| pool-tag | Unique number assigned to the pool. Range is 1 to 100. Note For Cisco Unified Communications Manager Express (Cisco
                                                   						Unified CME) systems, the upper limit for this argument is defined by the max-pool command. | Note | For Cisco Unified Communications Manager Express (Cisco
                                                   						Unified CME) systems, the upper limit for this argument is defined by the max-pool command. |
|---|---|---|---|
| Note | For Cisco Unified Communications Manager Express (Cisco
                                                   						Unified CME) systems, the upper limit for this argument is defined by the max-pool command. |

| Note | For Cisco Unified Communications Manager Express (Cisco
                                                   						Unified CME) systems, the upper limit for this argument is defined by the max-pool command. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco CME. |
| Cisco IOS XE Amsterdam 17.2.1r | Cisco Unified SIP SRST 12.8 | Introduced support for YANG models. |
| Cisco IOS XE Cupertino
                                                17.8.1a | Cisco Unified SIP SRST 14.2 | Added a new CLI command sip-oauth for voice register pool mode. |

| Command | Description |
|---|---|
| max-pool (voice register global) | Sets the maximum number of SIP phones that are supported by
                                          						a Cisco Unified CME system. |
| mode (voice register global) | Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CME system. |
| number (voice register pool) | Configures a valid number for a SIP phone. |
| type (voice register pool) | Defines a Cisco IP phone type. |
| voice register dn | Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line. |
| voice register global | Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified CME
                                          						or Cisco Unified SIP SRST environment. |

| Release | Modification |
|---|---|
| Cisco IOS XE Cupertino
                                             17.8.1a | This command was introduced. |

| Note | Key server should be configured under voice register . |
|---|---|

| vrfname | A name assigned to the voice vrf. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| Cisco IOS XE Amsterdam 17.2.1r | Unified SRST 12.8 | This command was introduced as part of VRF functionality support on Cisco 4000 Series Integrated Services Router for Unified
                                          SRST. |

| Command | Description |
|---|---|
| vrf definition vrf-name | Creates a VRF with the specified name. |

| tag | Unique number assigned to the voice class. Range is from 1
                                          						to 10000. The tag number maps to the tag number created by using the voice class codec command in dial-peer configuration mode. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco CME. |
| Cisco IOS XE Amsterdam 17.2.1r | Cisco Unified SIP SRST 12.8 | Introduced support for YANG models. |

| Note | The id (voice register pool) command is required
                                       		  and must be configured before any other voice register pool commands. The id command identifies a locally available
                                       		  individual Cisco SIP IP phone or set of Cisco SIP IP phones. |
|---|---|

| Command | Description |
|---|---|
| codec (voice register pool) | Specifies the codec supported by a single Cisco SIP phone
                                          						or a VoIP dial peer in a Cisco Unified SIP SRST or a Cisco Unified CME
                                          						environment. |
| id (voice register pool) | Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |
| voice class codec (dial-peer) | Assigns a previously configured codec selection preference
                                          						list (codec voice class) to a VoIP dial peer. |

| phone-number | Phone number configured as a speed-dial number for
                                          						retrieving messages. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco SRST 1.0 | This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs. |
| 12.2(2)XT | Cisco SRST 2.0 | This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified Survivable Remote Site Telephony
                                          						(SRST) support and enters call-manager-fallback configuration mode. |

| vrf-name | A name assigned to the configured vrf. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| Cisco IOS XE Amsterdam 17.2.1r | Unified SRST 12.8 | This command was introduced as part of VRF functionality support on Cisco 4000 Series Integrated Services Router for Unified
                                          SRST. |

| Command | Description |
|---|---|
| voice vrf vrfname | Configures a Voice VRF in global configuration mode. |

| customer-vrf-name | A name assigned to the customer vrf. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| Cisco IOS XE Amsterdam 17.2.1r | Unified SRST 12.8 | This command was introduced as part of VRF functionality support on Cisco 4000 Series Integrated Services Router for Unified
                                          SRST. |

| Command | Description |
|---|---|
| voice vrf vrfname | Configures a Voice VRF in global configuration mode. |
| vrf definition vrf-name | Creates a VRF with the specified name. |

| schema-url | Local or remote URL as defined in RFC 2396. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)T | Cisco SRST 3.2 | This command was introduced. |

| Command | Description |
|---|---|
| call-manager-fallback | Enable Cisco Unified SRST configuration mode. |