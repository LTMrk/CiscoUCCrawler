---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr2-vcr2-cr-book-vcr-d2-html-0e5b697848
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr2/vcr2-cr-book/vcr-d2.html
retrieved_at: 2026-08-16T23:16:45.588921+00:00
---

Cisco IOS Voice Command Reference - D through I

# Cisco IOS Voice Command Reference - D through I

Updated: April 25, 2026

Chapter: disable-early-media through dualtone

## Chapter: disable-early-media through dualtone

# disable-early-media through dualtone

## disable-early-media
                        	 180

To specify which
                              		  call treatment, early media or local ringback, is provided for 180 responses
                              		  with 180 responses with Session Description Protocol (SDP), use the disable - early - media 180 command in sip-ua configuration mode or voice
                              		  class tenant configuration mode. To enable early media cut-through for 180
                              		  messages with SDP, use the no form of this
                              		  command.

disable-early-media 180 system

no disable-early-media 180

### Syntax Description

system

Specifies that the disable-early-media method use the global
                                          						sip-ua value. This keyword is available only for the tenant mode to allow it to
                                          						fallback to the global configurations

### Command Default

Early media
                              		  cut-through for 180 responses with SDP is enabled.

### Command Modes

SIP UA configuration (config-sip-ua)

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.2(13)T

This
                                          						command was introduced.

IOS
                                          						Release XE 2.5

This
                                          						command was integrated into Cisco IOS XE Release 2.5.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

This command
                              		  provides the ability to enable or disable early media cut-through on Cisco IOS
                              		  gateways for SIP 180 responses with SDP. Use the disable - early - media 180 command to configure the gateway to
                              		  ignore the SDP message and provide local ringback. To restore the default
                              		  treatment, early media cut-through, use the no disable-early-media 180 command .

## Examples

The following
                              		  example disables early media cut-through for SIP 180 responses with SDP:

```
Router(config-sip-ua)# disable-early-media 180
```

The following
                              		  example shows how to disable early media cut-through for SIP 180 responses in
                              		  the voice class tenant configuration mode:

```
Router(config-class)# disable-early-media 180 system
```

### Related Commands

Command

Description

show sip-ua retry

Displays
                                          						SIP retry statistics.

show sip-ua statistics

Displays
                                          						response, traffic, and retry SIP statistics.

show sip-ua timers

Displays the current settings for SIP-UA timers.

sip-ua

Enables
                                          						the SIP-UA configuration commands.

## disable service-settings

To disable the service settings configured on a Cisco Unified Communications Manager (CUCM), use the disable service-settings command in phone proxy configuration mode. To enable the service settings configured on a CUCM, use the no form of the command.

disable service-settings

no disable service-settings

### Syntax Description

This command has no arguments or keywords.

### Command Default

The service settings on a CUCM are enabled.

### Command Modes

Phone proxy configuration mode (config-phone-proxy)

## Command History

15.3(3)M

This command was introduced.

### Usage Guidelines

The disable service-setting command disables the service settings configured on a CUCM. PC Port, Gratuitous ARP, Voice VLAN access, Web access, and Span
                              to PC Port are the services enabled by default on a CUCM.

## Examples

```
Device(config)# voice-phone-proxy first-pp
Device(config-phone-proxy)# disable service-settings
```

## disc_pi_off

To enable an H.323 gateway to disconnect a call when it receives a disconnect message with a progress indicator (PI) value,
                              use the disc_pi_off command in voice-port configuration mode. To restore the default state, use the no form of this command.

disc_pi_off

no disc_pi_off

### Syntax Description

This command has no arguments or keywords.

### Command Default

The gateway does not disconnect a call when it receives a disconnect message with a PI value.

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.1(5)T

This command was introduced on the following platforms: Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco 7500
                                          series, Cisco AS5300, Cisco AS5800, and Cisco MC3810.

12.2(2)XA

This command was implemented on the Cisco AS5400 and Cisco AS5350.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into the Cisco IOS Release 12.2(11)T.

### Usage Guidelines

The disc_pi_off voice-port command is valid only if the disconnect with PI is received on the inbound call leg. For example, if this command
                              is enabled on the voice port of the originating gateway, and a disconnect message with PI is received from the terminating
                              switch, the disconnect message is converted to a disconnect message. But if this command is enabled on the voice port of the
                              terminating gateway, and a disconnect message with PI is received from the terminating switch, the disconnect message is not
                              converted to a standard disconnect message because the disconnect message is received on the outbound call leg.

The disc_pi_off voice-port configuration command is valid only for the default session application; it does not work for interactive voice
                                          response (IVR) applications.

## Examples

The following example handles a disconnect message with a PI value in the same way as a standard disconnect message for voice
                              port 0:23:

```
voice-port 0:D
 disc_pi_off
```

### Related Commands

Command

Description

isdn t306

Sets a timer for disconnect messages.

## disconnect-ack

To configure a Foreign Exchange Station (FXS) voice port to return an acknowledgment upon receipt of a disconnect signal,
                              use the disconnect - ack command in voice-port configuration mode. To disable the acknowledgment, use the no form of this command.

disconnect-ack

no disconnect-ack

### Syntax Description

This command has no arguments or keywords.

### Command Default

FXS voice ports return an acknowledgment upon receipt of a disconnect signal

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

11.3(1)MA

This command was introduced on the Cisco MC3810.

12.0(7)XK

This command was implemented on the Cisco 2600 series and Cisco 3600 series.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

### Usage Guidelines

The disconnect - ack command configures an FXS voice port to remove line power if the equipment on an FXS loop-start trunk disconnects first.

## Examples

The following example, which begins in global configuration mode, disables the disconnect acknowledgment signal on voice port
                              1/1/0:

```
voice-port 1/0/0
 no disconnect-ack
```

## Command History

Command

Description

show voice port

Displays voice port configuration information.

## dnis (DNIS group)

To add a dialed number identification service (DNIS) number to a DNIS map, use the dnis command in DNIS-map configuration mode. To delete a DNIS number, use the no form of this command.

dnis telephone-umber [ url url ]

no dnis

### Syntax Description

telephone-umber

Adds a user-selected DNIS number to a DNIS map.

url url

(Optional) URL that links a DNIS number to a specific VoiceXML document. If a URL is not entered, the DNIS number is linked
                                          to the VoiceXML application in the dial peer, which must be configured using the application command. This keyword is not valid for Tool Command Language (TCL) applications.

### Command Default

If no URL is entered, the DNIS number links to the VoiceXML application that is configured in the dial peer with the application command.

### Command Modes

DNIS-map configuration

## Command History

Release

Modification

12.2(2)XB

This command was introduced on the Cisco AS5300, Cisco AS5350, and Cisco AS5400.

12.2(11)T

This command was implemented on the Cisco 3640 and Cisco 3660.

### Usage Guidelines

To enter DNIS-map configuration mode for the dnis command, use the voice dnis-map command.

Enter the dnis command once for each telephone number that you want to map to a voice application. A separate entry must be made for each
                              telephone number in a DNIS map. Wildcards are not supported.

URLs in DNIS entries are used only by VoiceXML applications. When an incoming called number matches a DNIS entry, it loads
                              the VoiceXML document that is specified by the URL, provided that a VoiceXML application is configured in the dial peer with
                              the application command configured.

Non-VoiceXML applications, such as TCL applications, ignore the URLs in DNIS maps and link a call to the TCL application that
                              is configured in the dial peer using the application command.

For a DNIS map to be applied to an outbound dial peer, a VoiceXML application must be configured with the application out-bound command. Otherwise, the call is not handed off to the application that is specified in the URL of the DNIS map.

The number of allowable DNIS entries is limited by the amount of available configuration memory on the gateway. As a general
                              rule, DNIS maps that contain more than several hundred DNIS entries should be maintained in an external text file.

To associate a DNIS map with a dial peer, use the dnis-map command.

## Examples

The first line in the following example shows how the voice dnis-map command is used to create a DNIS map named dmap1. The last two lines show how the dnis command is used to enter DNIS entries.

The first DNIS entry specifies the location of a VoiceXML document. The second DNIS entry does not specify a URL. A DNIS number
                              without a URL is, by default, matched to the URL of the application that is configured in the dial peer by the configured
                              application command.

```
voice dnis-map dmap1
 dnis 5550105 url tftp://blue/sky/test.vxml
 dnis 5550188
```

### Related Commands

Command

Description

dnis - map

Associates a DNIS map with a dial peer.

show voice dnis - map

Displays configuration information about DNIS maps.

voice dnis - map

Enters DNIS-map configuration mode to create a DNIS map.

voice dnis - map load

Reloads a DNIS map that has changed since the previous load.

## dnis-map

To associate a dialed number identification service (DNIS) map with a dial peer, use the dnis - map command in dial peer configuration mode. To remove a DNIS map from the dial peer, use the no form of this command.

dnis-map map-name

no dnis-map

### Syntax Description

map - name

Name of the configured DNIS map.

### Command Default

No default behavior or values

### Command Modes

Dial peer configuration

## Command History

Release

Modification

12.2(2)XB

This command was introduced on the Cisco AS5300, Cisco AS5350, and Cisco AS5400.

12.2(11)T

This command was implemented on the Cisco 3640 and Cisco 3660.

### Usage Guidelines

A DNIS map is a table of destination numbers with optional URLs that link to specific VoiceXML documents. When configured
                              in a dial peer, a DNIS map enables you to link multiple called numbers to a single Tool Command Language (TCL) application
                              or to individual VoiceXML documents.

The dnis-map command must be used with the application command.

Only one DNIS map can be configured in each dial peer.

To create a DNIS map, use the voice dnis-map command to enter DNIS-map configuration mode, and then use the dnis command to add entries to the DNIS map. Or you can create an external text file of DNIS entries and link to its URL by using
                              the voice dnis - map command.

To display the configuration information for DNIS maps, use the show voice dnis-map command.

A URL configured for a DNIS number is ignored by a TCL application; the TCL script that is configured for the application
                              is used instead.

For a DNIS map to be applied to an outbound dial peer, the call application must be configured as an outbound application.
                                          That is, a VoiceXML application must be configured by with the application out-bound command. Otherwise, the call is not handed off to the application that is specified in the URL of the DNIS map.

## Examples

In the following example the DNIS map named "dmap1" is associated with the VoIP dial peer 3. The outbound application "vapptest1"
                              is associated through this dial peer with DNIS map "dmap1."

```
dial-peer voice 3 voip
 dnis-map dmap1
 application vapptest1 outbound
```

### Related Commands

Command

Description

dnis

Adds a DNIS number to a DNIS map.

show voice dnis - map

Displays configuration information about DNIS maps.

voice dnis - map

Enters DNIS-map configuration mode to create a DNIS map.

voice dnis - map load

Reloads a DNIS map that has changed since the previous load.

## dns-a-override

To skip querying
                              		  Domain Name System (DNS) IPv4 and IPv6 address records (A and AAAA) if a
                              		  service record (SRV) query times out, use the dns-a-override command in voice service SIP
                              		  configuration mode or voice class tenant configuration mode. To disable this
                              		  functionality, use the no form of
                              		  this command.

dns-a-override system

no dns-a-override

### Command Default

If an SRV query
                              		  times out, DNS IPv4 and IPv6 records are queried.

### Command Modes

Voice service SIP configuration (conf-serv-sip)

Voice class tenant configuration (config-class)

## Command History

15.3(1)T

This
                                       					 command was introduced.

15.6(2)T
                                       					 and IOS XE Denali 16.3.1

This
                                       					 command was modified to include the keyword: system . This
                                       					 command is now available under voice class tenants.

### Usage Guidelines

Use the dns-a-override command if you do not want the
                              		  Cisco Unified Border Element (Cisco UBE) to query the A and AAAA records on the
                              		  DNS server when the SRV query times out.

## Examples

The following
                              		  example shows how to skip querying the DNS A and AAAA records when an SRV query
                              		  times out:

```
Device> enable Device# configure terminal Device(config)# voice service voip Device(conf-voi-serv)# sip Device(conf-serv-sip)# dns-a-override
```

The following
                              		  example shows how to skip querying in the voice class tenant configuration
                              		  mode:

```
Router(config-class)# dns-a-override system
```

## domain-name (annex G)

To set the domain name that is reported in service relationships, use the domain name command in annex G neighbor configuration mode.
                              To remove the domain name, use the no form of this command.

domain-name id

no domain-name id

### Syntax Description

id

Domain name that is reported in service relationships.

### Command Default

No default behavior or values

### Command Modes

Annex G neighbor configuration mode

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

Use this command to set the domain name that is reported in service relationships.

## Examples

The following example shows how to set a domain name to "boston1":

```
Router(config-annexg-neigh)# domain-name sample1
```

### Related Commands

Command

Description

access - policy

Requires that a neighbor be explicitly configured.

## drop-last-conferee

To define a Feature Access Code (FAC) to access the Drop Last Conferee feature in feature mode on analog phones controlled
                              by Cisco Unified Communications Manager Express (CME), use the drop-last-conferee command in STC application feature-mode call-control configuration mode. To return the code to its default, use the no form of this command.

drop-last-conferee keypad-character

no drop-last-conferee

### Syntax Description

keypad-character

Character string of one to four characters that can be dialed on a telephone keypad (0-9, *, #). Default is #4.

### Command Default

The default value is #4.

### Command Modes

STC application feature-mode call-control configuration (config-stcapp-fmcode)

## Command History

Release

Modification

15.0(1)M

This command was introduced.

### Usage Guidelines

This command changes the value of the FAC for the Drop Last Conferee feature from the default (#4) to the specified value.

If you attempt to configure this command with a value that is already configured for another FAC in feature mode, you receive
                              a message. This message will not prevent you from configuring the feature code. If you configure a duplicate FAC, the system
                              implements the first feature it matches in the order of precedence as determined by the value for each FAC (#1 to #5).

If you attempt to configure this command with a value that precludes or is precluded by another FAC in feature mode, you receive
                              a message. If you configure a FAC to a value that precludes or is precluded by another FAC in feature mode, the system always
                              executes the call feature with the shortest code and ignores the longer code. For example, 1 will always preclude 12 and 123.
                              These messages will not prevent you from configuring the feature code. You must configure a new value for the precluded code
                              in order to enable phone user access to that feature.

This command does not change the user experience for Drop Last Conferee if the Cisco call-control system is Cisco Unified
                                          Communications Manager.

## Examples

The following example shows how to change the value of the feature code for the Drop Last Conferee feature from the default
                              (#4). With this configuration, a phone user in a three-party conference on an analog phone controlled by Cisco Unified CME
                              presses hook flash to get the feature tone and then dials 44 to drop the last active party. The conference becomes a basic
                              call to the second call party.

```
Router(config)# stcapp call-control mode feature Router(config-stcapp-fmcode)# drop-last-conferee 44 Router(config-stcapp-fmcode)# exit
```

### Related Commands

Command

Description

conference

Defines FAC in Feature Mode to initiate a three-party conference.

hangup-last-active-call

Defines FAC in feature mode to drop last active call during a three-party conferencee.

toggle-between-two-calls

Defines FAC in feature mode to toggle between two active calls.

transfer

Defines FAC in feature mode to connect a call to a third party that the phone user dials.

## ds0 busyout (voice)

To force a DS0 time slot on a controller into the busyout state, use the ds0 busyout command in controller configuration mode. To remove the DS0 time slot from the busyout state, use the no form of this command.

ds0 busyout ds0-time-slot

no ds0 busyout ds0-time-slot

### Syntax Description

ds0 - time - slot

DS0 time slots to be forced into the busyout state. Range is from 1 to 24 and can include any combination of time slots.

### Command Default

DS0 time slots are not in the busyout state.

### Command Modes

Controller configuration

## Command History

Release

Modification

12.0(7)XK

This command was introduced on the Cisco MC3810 and Cisco 2600 series and the Cisco 3600 series.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

### Usage Guidelines

The ds0 busyout command affects only DS0 time slots that are configured into a DS0 group and that function as part of a digital voice port.
                              If multiple DS0 groups are configured on a controller, any combination of DS0 time slots can be busied out, provided that
                              each DS0 time slot to be busied out is part of a DS0 group.

If a DS0 time slot is in the busyout state, only the no ds0 busyout command can restore the DS0 time slot to service.

To avoid conflicting interaction of command-line interface (CLI) commands, do not use the ds0 busyout command and the busyout forced command on the same controller.

## Examples

The following example configures DS0 time slot 6 on controller T1 0 to be forced into the busyout state:

```
controller t1 0
 ds0 busyout 6
```

The following example configures DS0 time slots 1, 3, 4, 5, 6, and 24 on controller E1 1 to be forced into the busyout state:

```
controller e1 1
 ds0 busyout 1,3-6,24
```

### Related Commands

Command

Description

busyout seize

Changes the busyout seize procedure for a voice port.

show running configuration

Displays the contents of the currently running configuration file or the configuration for a specific class map, interface,
                                          map class, policy map, or virtual circuit (VC) class.

## ds0-group (E1)

To specify the DS0 time slots that make up a logical voice port on an E1 controller, specify the signaling type by which the
                              router communicates with the PBX or PSTN, and define E1 channels for compressed voice calls and the channel-associated signaling
                              (CAS) method by which the router connects to the PBX or PSTN, use the ds0 - group command in controller configuration mode. To remove the group and signaling setting, use the no form of this command.

### Cisco IOS Release 12.2 and Later Releases-Cisco 1750 and Cisco
                              			 1751

ds0-group ds0-group-number timeslots timeslot-list { service service-type |  [ type e&m-fgb | e&m-fgd | e&m-immediate-start | fgd-eana | fgd-os | fxs-ground-start | fxs-loop-start | none | r1-itu | r1-modified | r1-turkey ]}

no ds0-group ds0-group-number

### Cisco IOS Release 12.1 and Earlier Releases- Cisco 1750 and
                              			 Cisco 1751

ds0-group ds0-group-number timeslots timeslot-list { [ service service-type ] |  [ type e&m-fgb | e&m-fgd | em-immediate-start | fgd-eana | fgd-os | fxs-ground-start | fxs-loop-start | none | r1-itu | r1-modified | r1-turkey | sas-ground-start | sas-loop-start ]}

no ds0-group ds0-group-number

### Cisco 2600 Series (Except Cisco 2691), Cisco 3600 Series (Except
                              			 Cisco 3660)

ds0-group ds0-group-number timeslots timeslot-list type { e&m-delay-dial | &em-immediate-start | e&m-melcas-delay | e&m-melcas-immed | e&m-melcas-wink | e&m-wink-start | ext-sig | fgd-eana | fxo-ground-start | fxo-loop-start | fxo-melcas | fxs-ground-start | fxs-loop-start | fxs-melcas | r2-analog | r2-digital | r2-pulse }

no ds0-group ds0-group-number

### Cisco 2691, Cisco 2600XM Series, Cisco 2800 Series (Except Cisco
                              			 2801), Cisco 3660, Cisco 3700 Series, Cisco 3800 Series

ds0-group ds0-group-number timeslots timeslot-list type { e&m-delay-dial | e&m-immediate-start | e&m-lmr | e&m-melcas-delay | e&m-melcas-immed | e&m-melcas-wink | e&m-wink-start | ext-sig | fgd-eana | fxo-ground-start | fxo-loop-start | fxo-melcas | fxs-ground-start | fxs-loop-start | fxs-melcas | r2-analog | r2-digital | r2-pulse }

no ds0-group ds0-group-number

### Cisco 7200 Series and Cisco 7500 Series Voice Ports

ds0-group ds0-group-number timeslots timeslot-list type { e&m-delay-dial | e&m-fgd | e&m-immediate-start | e&m-wink-start | fxo-ground-start | fxo-loop-start | fxs-ground-start | fxs-loop-start }

no ds0-group ds0-group-number

### Cisco 7700 Series Voice Ports

ds0-group ds0-group-number timeslots timeslot-list type { e&m-delay-dial | e&m-immediate-start | e&m-wink-start | fxs-ground-start | fxs-loop-start | fxo-ground-start | fxo-loop-start }

no ds0-group ds0-group-number

### Cisco AS5300 and Cisco AS5400

ds0-group ds0-group-number timeslots timeslot-list type { none | p7 | r2-analog | r2-digital | r2-lsv181-digital | r2-pulse }

no ds0-group ds0-group-number

### Syntax Description

ds0 - group - number

A value that identifies the DS0 group. Range is from 0 to
                                          						14 and 16 to 30; 15 is reserved.

timeslots timeslot - list

Lists time slots in the DS0 group. The timeslot-list argument is a single
                                          						time-slot number, a single range of numbers, or multiple ranges of numbers
                                          						separated by commas. Range is from 1 through 31. Examples are as follows:

2

1-15,17-24

1-23

2,4,6-12

Specifies the type of signaling for the DS0 group. The
                                          						signaling method selection for the type keyword depends on the connection that
                                          						you are making. The ear and mouth (E&M) interface allows connection for PBX
                                          						trunk lines (tie lines) and telephone equipment. The Foreign Exchange Station
                                          						(FXS) interface allows connection of basic telephone equipment and a PBX. The
                                          						Foreign Exchange Office (FXO) interface is for connecting the central office
                                          						(CO) to a standard PBX interface where permitted by local regulations; it is
                                          						often used for off-premise extensions (OPXs). Types are as follows:

e&m - delay - dial --The
                                                						  originating endpoint sends an off-hook signal and then waits for an off-hook
                                                						  signal followed by an on-hook signal from the destination.

e&m-fgb--E&M Type II Feature Group B.

e&m-fgd--E&M Type II Feature Group D.

e&m - immediate - start --E&M
                                                						  immediate start.

e&m-lmr --E&M
                                                						  Land Mobile Radio (LMR).

e&m - melcas - delay --E&M
                                                						  MELCAS delay-start signaling support.

e&m - melcas - immed --E&M
                                                						  MELCAS immediate-start signaling support.

e&m - melcas - wink --E&M MELCAS wink-start signaling support.

e&m - wink - start --The originating endpoint sends an off-hook signal and waits for a wink-start from the destination.

fgd - eana -- Feature Group D exchange access North American.

fgd-os--Feature Group D operator services.

fxo - ground - start -- FXO ground-start signaling.

fxo - loop - start -- FXO loop-start signaling.

fxo - melcas -- FXO MELCAS signaling.

fxs - ground - start -- FXS ground-start signaling.

fxs - loop - start -- FXS loop-start signaling.

fxs - melcas -- FXS MELCAS signaling.

none --Null signaling for external call control.

p7--Specifies the p7 switch type.

r1-itu--Line signaling based on international signaling standards.

r1-modified--An international signaling standard that is common to channelized T1/E1 networks.

r1 - turkey --A signaling standard used in Turkey.

r2 - analog -- R2 analog line signaling.

r2 - digital -- R2 digital line signaling.

r2-lsv181-digital--Specifies a specific R2 digital line.

r2 - pulse -- 7-pulse line signaling, a transmitted pulse that indicates a change in the line state.

sas-ground-start -- Single attachment station (SAS) ground-start.

sas-loop-start -- SAS loop-start.

service service - type

(Optional) Specifies the type of service

data --data
                                                						  service

fax --
                                                						  store-and-forward fax service

voice --voice
                                                						  service (for FGD-OS service)

mgcp --Media
                                                						  Gateway Control Protocol (MGCP) service

### Command Default

There is no DS0 group. Calls are allowed in both directions.

### Command Modes

Controller configuration (config-controller)

## Command History

Release

Modification

11.2

This command was introduced for the Cisco AS5300 as the cas - group command.

11.3(1)MA

The command was introduced as the voice-group command for
                                          						the Cisco MC3810.

12.0(1)T

This command was integrated into Cisco IOS Release
                                          						12.0(1)T, and the cas-group command was implemented on the Cisco 3600 series
                                          						routers.

12.0(5)T

The command was renamed ds0-group on the Cisco AS5300 and
                                          						Cisco 2600 series and Cisco 3600 series routers. Some keyword modifications
                                          						were implemented.

12.0(5)XE

This command was implemented on the Cisco 7200 series.

12.0(7)XK

Support for this command was implemented on the Cisco MC3810. When the ds0-group command became available on the Cisco MC3810,
                                          the voice-group command was removed and no longer supported.

12.0(7)XR

The mgcp service type was added.

12.1(2)XH

The e&m-fgd and fgd-eana keywords were added for
                                          						Feature Group D signaling.

12.1(5)XM

The sgcp keyword was removed.

12.1(3)T

This command was modified for Cisco 7500 series routers.
                                          						The fgd-os signaling type and the voice service type were added.

12.2

The command was modified to exclude sas keywords. The
                                          						Single Attachment Station (SAS) CAS options of sas-loop-start and
                                          						sas-ground-start are not supported as a type of signaling for the DS0 group.

12.2(2)XA

This command was implemented on the Cisco AS5300.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T
                                          						and implemented on the Cisco 7200 series.

12.2(4)T

Support for the Cisco AS5300, Cisco AS5350, and Cisco
                                          						AS5400 is not included in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)XM

This command was implemented on Cisco 1750 and Cisco 1751
                                          						routers. Support for other Cisco platforms is not included in this release.

12.2(2)XN

Support for the mgcp keyword was added to Cisco
                                          						CallManager Version 3.1 for the Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						VG200.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 7200 series. Support for the Cisco AS5300, Cisco
                                          						AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release.

12.2(11)T

This command was supported with Cisco IOS Release 12.2(11)T
                                          						and Cisco CallManager Version 3.2. This command is supported on the Cisco
                                          						IAD2420 series, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5850 in this
                                          						release.

12.2(13)T

This command was integrated into Cisco IOS Release
                                          						12.2(13)T. The Cisco 1750 and Cisco 1751 do not support T1 and E1 voice and
                                          						data cards in Cisco IOS Release 12.2(13)T. The Cisco 17xx platforms can support
                                          						only HC DSP firmware images in this release.

12.3(8)T

Documentation of the ds0-group command was divided into
                                          						the individual ds0-group (E1) and ds0-group (T1) commands.

12.4(2)T1

Support was added for the e&m-lmr signaling type on the
                                          						Cisco 2691, Cisco 2600XM series, Cisco 2800 series (except Cisco 2801), Cisco
                                          						3660, Cisco 3700 series, and Cisco 3800 series.

### Usage Guidelines

The ds0 - group command automatically creates a logical voice port that is numbered as follows:

This command does not support the extended echo canceller (EC)
                                          		  feature on the Cisco AS5x00 series.

Although only one voice port is created for each group, applicable
                              		  calls are routed to any channel in the group.

Be sure you take the following into account when you are configuring
                              		  DS0 groups:

Channel groups, CAS voice
                                    			 groups, DS0 groups, and time-division multiplexing (TDM) groups all use group
                                    			 numbers. All group numbers configured for channel groups, CAS voice groups, DS0
                                    			 groups, and TDM groups must be unique on the local router. For example, you
                                    			 cannot use the same group number for a channel group and for a TDM group.

The keywords available
                                    			 for the ds0-group command are dependent upon the
                                    			 Cisco IOS software release that you are using. For the most current
                                    			 information, go to the Cisco Feature Navigator home page at the following URL: http://www.cisco.com/go/fn

When you are using
                                    			 command-line interface (CLI) help, the keywords for the ds0 - group command
                                    			 are configuration specific. For example, if MGCP is configured, you see the mgcp keyword. If you are not using MGCP,
                                    			 you do not see the mgcp keyword.

Cisco IOS Releases later
                                    			 than 12.2 do not support the Single Attachment Station (SAS) CAS options of
                                    			 sas-loop-start and sas-ground-start.

## Examples

The following example shows ranges of E1 controller time slots
                              		  configured for FXS ground-start and FXO loop-start signaling:

```
E1 1/0
 framing esf
 linecode b8zs
 ds0-group 1 timeslots 1-10 type fxs-ground-start
 ds0-group 2 timeslots 11-24 type fxo-loop-start
```

The following example shows ranges of T1 controller time slots
                              		  configured for FXS ground-start signaling:

```
controller E1 1/0
 ds0-group 1 timeslots 1-4 type fxs-ground-start
```

The following example illustrates setting the E1 channels for
                              		  Signaling System 7 (SS7) service on any trunking gateway using the mgcp keyword:

```
Router(config-controller)# ds0-group 0 timeslots 1-24 type none service mgcp
```

In the following example, the time slot maximum is 12 and the time
                              		  slot is 1, so two voice-ports are created successfully.

```
controller E1 0/0
 ds0-group 0 timeslots 1-4 type e&m-immediate-start
 ds0-group 1 timeslots 6-12 type e&m-immediate-start
```

If a third DS0 group is added, the voice-port is rejected even though
                              		  the total number of voice channels is fewer than 16.

```
ds0-group 2 timeslots 17-18 type e&m-immediate-start
```

In the following example, the signaling type is set to E&M-LMR:

```
ds0-group 0 timeslots 1-10 type e&m-lmr
```

### Related Commands

Command

Description

cas-group

Configures channelized T1 time slots with robbed bit
                                          						signaling.

codec

Specifies the voice coder rate of speech for a dial peer.

codec complexity

Specifies call density and codec complexity based on the
                                          						codec standard that you are using.

## ds0-group (T1)

To specify the DS0 time slots that make up a logical voice port on a T1 controller, to specify the signaling type by which
                              the router communicates with the PBX or PSTN, and to define T1 channels for compressed voice calls and the channel-associated
                              signaling (CAS) method by which the router connects to the PBX or PSTN, use the ds0 - group command in controller configuration mode. To remove the group and signaling setting, use the no form of this command.

### Cisco IOS Release 12.2 and Later Releases- Cisco 1750 and Cisco 1751

ds0-group ds0-group-number timeslots timeslot-list [ service service-type ] type { e&m-fgb | e&m-fgd | e&m-immediate-start | fgd-eana | fgd-os | fxs-ground-start | fxs-loop-start | none | r1-itu | r1-modified | r1-turkey }

no ds0-group ds0-group-number

### Cisco IOS Release 12.1 and Earlier Releases - Cisco 1750 and Cisco 1751

ds0-group ds0-group-number timeslots timeslot-list [ service service-type ] type { e&m-fgb | e&m-fgd | e&m-immediate-start | fgd-eana | fgd-os | fxs-ground-start | fxs-loop-start | none | r1-itu | r1-modified | r1-turkey | sas-ground-start | sas-loop-start }

no ds0-group ds0-group-number

### Cisco 2600 Series (Except Cisco 2691), Cisco 3600 Series (Except Cisco 3660), and Cisco VG 200

ds0-group ds0-group-number timeslots timeslot-list type { e&m-delay-dial | em-fgd | e&m-immediate-start | e&m-wink-start | ext-sig | fgd-eana | fxo-ground-start | fxo-loop-start | fxs-ground-start | fxs-loop-start }

no ds0-group ds0-group-number

### Cisco 2691, Cisco 2600XM Series, Cisco 2800 Series (Except Cisco 2801), Cisco 3660, Cisco 3700 Series, Cisco 3800 Series

ds0-group ds0-group-number timeslots timeslot-list type { em-delay-dial | em-fgd | e&m-immediate-start | e&m-lmr | e&m-wink-start | ext-sig | fgd-eana | fgd-emf [ mf ] [ ani-pani ] [ ani ] | fxo-ground-start | fxo-loop-start | fxs-ground-start | fxs-loop-start }

no ds0-group ds0-group-number

### Cisco 7200 Series and Cisco 7500 Series

ds0-group ds0-group-number timeslots timeslot-list type { e&m-delay-dial | e&m-fgd | e&m-immediate-start | e&m-wink-start | fxo-ground-start | fxo-loop-start | fxs-ground-start | fxs-loop-start }

no ds0-group ds0-group-number

### Cisco 7700 Series Voice Ports

ds0-group ds0-group-number timeslots timeslot-list type { e&m-delay-dial | e&m-immediate-start | e&m-wink-start | fxo-ground-start | fxo-loop-start | fxs-ground-start | fxs-loop-start }

no ds0-group ds0-group-number

### Cisco IOS Release 12.2 and Later Releases for Cisco AS5300, Cisco AS5350, and Cisco AS5400

ds0-group ds0-group-number timeslots timeslot-list [ service service-type ] [ type e&m-fgd [ dtmf | mf [ dnis | ani-dnis [ info-digits-no-strip ] | fgd-emf [ ani-pani ] [ ani ] | service service-type ] | e&m-immediate-start | fxs-ground-start | fxs-loop-start | fgd-eana [ ani-dnis | mf ] | fgd-os [ dnis-ani | mf ] | none ]]

no ds0-group ds0-group-number

### Cisco AS5850

ds0-group ds0-group-number timeslots timeslot-list [ service service-type ] [ type e&m-fgd [ dtmf | mf [ dnis | ani-dnis [ info-digits-no-strip ] | fgd-emf [ ani-pani ] [ ani ] | service service-type ] | e&m-immediate-start | fxs-ground-start | fxs-loop-start | fgd-eana [ ani-dnis | mf ] | fgd-os [ dnis-ani | mf ] | r1-itu [ dnis ] | none ]]

no ds0-group ds0-group-number

### Cisco IOS Release 12.1 and Earlier Releases - Cisco AS5300, Cisco AS5350, and Cisco AS5400

ds0-group ds0-group-number timeslots timeslot-list [ service service-type ] [ type e&m-fgd [ dtmf | mf [ dnis | ani-dnis [ info-digits-no-strip ] | fgd-emf [ ani-pani ] [ ani ] | service service-type ] | e&m-immediate-start | fxs-ground-start | fxs-loop-start | fgd-eana [ ani-dnis | mf ] | fgd-os [ dnis-ani | mf ] | sas-ground-start | sas-loop-start | none ]]

no ds0-group ds0-group-number

### Cisco AS5850

ds0-group ds0-group-number timeslots timeslot-list [ service service-type ] [ type e&m-fgd [ dtmf | mf [ dnis | ani-dnis [ info-digits-no-strip ] | fgd-emf [ ani-pani ] [ ani ] | service service-type ] | e&m-immediate-start | fxs-ground-start | fxs-loop-start | fgd-eana [ ani-dnis | mf ] | fgd-os [ dnis-ani | mf ] | sas-ground-start | sas-loop-start | none ]]

no ds0-group ds0-group-number

### Syntax Description

ds0 - group - number

A value that identifies the DS0 group. Range is from 0 to 23.

timeslots timeslot-list

Lists time slots in the DS0 group. The timeslot-list argument is a single time-slot number, a single range of numbers, or multiple ranges of numbers separated by commas. Range
                                          is from 1 to 24. Examples are as follows:

2

1-15,17-24

1-23

2,4,6-12

typenone

Specifies the type of signaling for the DS0 group. The signaling method selection for the type keyword depends on the connection
                                          that you are making. The ear and mouth (E&M) interface allows connection for PBX trunk lines (tie lines) and telephone equipment.
                                          The Foreign Exchange Station (FXS) interface allows connection of basic telephone equipment and a PBX interface. The Foreign
                                          Exchange Office (FXO) interface is for connecting the central office (CO) to a standard PBX interface where permitted by local
                                          regulations; it is often used for off-premise extensions (OPXs). Types are as follows:

e&m-delay-dial --The originating endpoint sends an off-hook signal and then waits for an off-hook signal followed by an on-hook signal from
                                                the destination.

e&m-fgb --E&M Type II Feature Group B.

e&m-fgd --E&M Type II Feature Group D.

e&m-immediate-start --E&M immediate start.

e&m-lmr --E&M Land Mobile Radio (LMR).

e&m-wink-start --The originating endpoint sends an off-hook signal and waits for a wink-start from the destination.

ext-sig --The external signaling interface specifies that the signaling traffic comes from an outside source.

fgd-eana -- Feature Group D exchange access North American.

fgd-emf-- FGD Enhanced MF.

fgd-os --Feature Group D operator services.

fxo-ground-start -- FXO ground-start signaling.

fxo-loop-start -- FXO loop-start signaling.

fxs-ground-start -- FXS ground-start signaling.

fxs-loop-start -- FXS loop-start signaling.

none --Null signaling for external call control.

r1-itu --Line signaling based on international signaling standards. (This signaling type is not supported on the Cisco AS5300, Cisco
                                                AS5350, and Cisco AS5400 platforms.)

r1-modified --An international signaling standard that is common to channelized T1/E1 networks.

r1-turkey --A signaling standard used in Turkey.

sas-ground-start --Single attachment station (SAS) ground-start.

sas-loop-start --SAS loop-start.

service service - type

(Optional) Specifies the type of service:

data --Data service.

fax -- Store-and-forward fax service.

mgcp --Media Gateway Control Protocol (MGCP) service. Used only with the type none keywords on the Cisco AS5x00 platforms.

sccp --Simple Gateway Control Protocol (SCCP) service.

voice --Voice service (for FGD-OS service).

dtmf

(Optional) Specifies dual tone multifrequency (DTMF) tone signaling.

mf

(Optional) Specifies multifrequency (MF) tone signaling

ani

(Optional) Provisions ANI address information.

ani-dnis

(Optional) Specifies automatic number identification (ANI) and dialed number identification service (DNIS) address information
                                          provisioning for FGD OS.

ani-pani

(Optional) Provisions ANI and PANI address information.

dnis-ani

(Optional) Specifies ANI and DNIS address information provisioning for FGD EANA.

dnis

(Optional) Specifies DNIS address information provisioning.

info-digits-no-strip

(Optional) Retains information digits on the Cisco AS5x00 platforms.

### Command Default

There is no DS0 group. Calls are allowed in both directions.

### Command Modes

Controller configuration

## Command History

Release

Modification

11.2

This command was introduced for the Cisco AS5300 as the cas-group command.

11.3(1)MA

The command was introduced as the voice-group command for the Cisco MC3810.

12.0(1)T

This command was integrated into Cisco IOS Release 12.0(1)T, and the cas-group command was implemented on the Cisco 3600 series routers.

12.0(5)T

The command was renamed ds0-group on the Cisco AS5300 and Cisco 2600 series and Cisco 3600 series routers. Some keyword modifications were implemented.

12.0(5)XE

This command was implemented on the Cisco 7200 series.

12.0(7)XK

Support for this command was implemented on the Cisco MC3810. When the ds0-group command became available on the Cisco MC3810, the voice-group command was removed and no longer supported. The ext-sig keyword replaced the ext-sig-master and ext-sig-slave keywords that were available with the voice-group command.

12.0(7)XR

The mgcp service type was added.

12.1(2)XH

The e&m-fgd and fgd-eana keywords were added for Feature Group D signaling.

12.1(5)XM

The sgcp keyword was removed.

12.1(3)T

This command was modified for Cisco 7500 series routers. The fgd-os signaling type and the voice service type were added.

12.2(2)XA

This command was implemented on the Cisco AS5300.

12.2

The command was modified to exclude sas keywords. The Single Attachment Station (SAS) CAS options of sas-loop-start and sas-ground-start
                                          are not supported as a type of signaling for the DS0 group.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 7200 series.

12.2(4)T

Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is not included in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)XM

This command was implemented on Cisco 1750 and Cisco 1751 routers. Support for other Cisco platforms is not included in this
                                          release.

12.2(2)XN

Support for the mgcp keyword was added to Cisco CallManager Version 3.1 for the Cisco 2600 series, Cisco 3600 series, and Cisco VG200.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 7200 series. Support for the Cisco
                                          AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release.

12.2(11)T

This command was supported in Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2. This command is supported on
                                          the Cisco IAD2420 series, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5850 in this release.

12.2(13)T

This command was integrated into Cisco IOS Release 12.2(13)T. The Cisco 1750 and Cisco 1751 do not support T1 and E1 voice
                                          and data cards in Cisco IOS Release 12.2(13)T. The Cisco 17xx platforms can support only HC DSP firmware images in this release.

12.2(15)T

This command was implemented on the Cisco 2600XM, Cisco 3725, and Cisco 3745.

12.3(4)XD

This command was modified for the Cisco 3725 and Cisco 3745. The e&m-lmr signaling type was added.

12.3(7)T

This command was integrated into Cisco IOS Release 12.3(7)T.

12.3(8)T

Documentation of the ds0-group command was divided into the individual ds0-group (E1) and ds0-group (T1) commands.

12.3(10)

The info-digits-no-strip keyword was added for use on the Cisco AS5x00 platforms.

12.4(9)T

This command was integrated into Cisco IOS Release 12.4(9)T. The fgd-emf , ani-pani , and ani keywords were added for the Cisco 2800 and Cisco AS5x00 platforms.

### Usage Guidelines

The ds0-group command automatically creates a logical voice port that is numbered as follows:

- slot / port : ds0-group-number

- slot / port

- slot / port : ds0-group-number

Although only one voice port is created for each group, applicable calls are routed to any channel in the group.

Be sure that you take the following into account when you are configuring DS0 groups:

Channel groups, CAS voice groups, DS0 groups, and time-division multiplexing (TDM) groups all use group numbers. All group
                                    numbers configured for channel groups, CAS voice groups, DS0 groups, and TDM groups must be unique on the local router. For
                                    example, you cannot use the same group number for a channel group and for a TDM group.

The keywords available for the ds0-group command are dependent upon the Cisco IOS software release that you are using. For the most current information, go to the
                                    Cisco Feature Navigator home page at the following URL:

http://www.cisco.com/go/fn

When you are using command-line interface (CLI) help, the keywords for the ds0-group command are configuration specific. For example, if MGCP is configured, you see the mgcp keyword. If you are not using MGCP, you do not see the mgcp keyword.

This command does not support the extended echo canceller (EC) feature on the Cisco AS5x00 series.

The signaling type R1-ITU is not supported on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 platforms.

## Examples

The following example shows ranges of T1 controller time slots configured for FXS ground-start and FXO loop-start signaling:

```
controller T1 1/0
 framing esf
 linecode b8zs
 ds0-group 1 timeslots 1-10 type fxs-ground-start
 ds0-group 2 timeslots 11-24 type fxo-loop-start
```

The following example shows ranges of T1 controller time slots configured for FXS ground-start signaling:

```
controller T1 1/0
 ds0-group 1 timeslots 1-4 type fxs-ground-start
```

The following example illustrates setting the T1 channels for Signaling System 7 (SS7) service on any trunking gateway using
                              the mgcp keyword:

```
ds0-group 0 timeslots 1-24 service mgcp type none
```

In the following example, the time slot maximum is 12 and the time slot is 1, so two voice ports are created successfully:

```
controller T1 0/0
 ds0-group 0 timeslots 1-4 type e&m-immediate-start
 ds0-group 1 timeslots 6-12 type e&m-immediate-start
```

If a third DS0 group is added, the voice port is rejected even though the total number of voice channels is fewer than 16.

```
ds0-group 2 timeslots 17-18 type e&m-immediate-start
```

In the following example, the signaling type is set to E&M LMR:

```
ds0-group 0 timeslots 1-10 type e&m-lmr
```

You have the option to retain info digits when you are configuring E&M Type II Feature Group D with MF signaling and ANI/DNIS
                              for calls being sent over IP. Info digits denote the subscriber type, and the info-digits keyword prepends info digits to the calling number.

On inbound calls from a T1 FGD voice-port with MF ANI/DNIS, when ANI information is obtained, it is passed unaltered to the
                              next matching dial peer, either POTS or VoIP. The addition of the info-digits-no-strip keyword allows you to retain the info digits portion of the ANI information; the modified ANI is then passed to the next
                              matching dial peer. Ordinarily, info digits are not valid for calls going over IP and are, therefore, stripped off. The ability
                              to retain info digits is particularly useful for calls that are not leaving the PSTN network and are just being hairpinned
                              back.

In the following example, the E&M Type II Feature Group D is configured with MF signaling and ANI/DNIS over IP while retaining
                              info digits:

```
ds0-group 0 timeslots 1-24 type e&m-fgd mf ani-dnis info-digits-no-strip
```

The following example enables FGD EMF:

```
ds0-group 11 timeslots 11 type fgd-emf ani
 ds0-group 11 timeslots 11 type fgd-emf ani-pani
```

### Related Commands

Command

Description

cas-group

Configures channelized T1 time slots with robbed bit signaling.

codec

Specifies the voice coder rate of speech for a dial peer.

codec complexity

Specifies call density and codec complexity based on the codec standard that you are using.

## ds0-num

To add B-channel information in outgoing Session Initiation Protocol (SIP) messages, use the ds0-num command in SIP voice service configuration mode. To return to the default setting, use the no form of this command.

ds0-num

no ds0-num

### Syntax Description

This command has no arguments or keywords.

### Command Default

B channel information is disabled.

### Command Modes

SIP voice service configuration (conf-serv-sip)

## Command History

Release

Modification

12.3(7)T

This command was introduced.

### Usage Guidelines

This command enables the SIP application to receive B-channel information of incoming ISDN calls. The B-channel information
                              appears in the Via header of an Invite request. Information acquired from the Via header can be used during call transfer
                              or to route a call.

## Examples

The following example adds B-channel information to outgoing SIP messages:

```
Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# ds0-num
```

### Related Commands

Command

Description

sip

Enables SIP voice service configuration commands.

voice service voip

Specifies the voice encapsulation type as VoIP.

## dscp media

To specify the resource priority header (RPH) to differentiated services code point (DSCP) mapping, use the dscp media command in voice class configuration mode. To disable the configuration, use the no form of this command.

dscp media { audio | video } { flah-override-override | flash-override | flsh | immediate | priority | routine } { dscp-value | set-af | set-cs | ef | zero }

no dscp media { audio | video } { flah-override-override | flash-override | flsh | immediate | priority | routine } { dscp-value | set-af | set-cs | ef | zero }

### Syntax Description

audio

Applies DSCP to audio payload packets.

video

Applies DSCP to video payload packets.

flah-override-override

Applies flash-override-override RPH priority.

flash-override

Applies flash-override RPH priority.

flsh

Applies flash RPH priority.

immediate

Applies immediate RPH priority.

priority

Applies priority RPH priority.

routine

Applies routine RPH priority.

dscp-value

DSCP value. Valid values are from 0 to 63.

set-af

af11 —bit pattern 001010

af12 —bit pattern 001100

af13 —bit pattern 001110

af21 —bit pattern 010010

af22 —bit pattern 010100

af23 —bit pattern 010110

af31 —bit pattern 011010

af32 —bit pattern 011100

af33 —bit pattern 011110

af41 —bit pattern 100010

af42 —bit pattern 100100

af43 —bit pattern 100110

set-cs

cs1 —code point 1 (precedence 1)

cs2 —code point 2 (precedence 2)

cs3 —code point 3 (precedence 3)

cs4 —code point 4 (precedence 4)

cs5 —code point 5 (precedence 5)

cs6 —code point 6 (precedence 6)

cs7 —code point 7 (precedence 7)

ef

Specifies the expedited forwarding bit pattern 101110 as the DSCP value.

zero

Specifies the default bit pattern 000000 as the DSCP value.

### Command Default

See the Usage Guidelines section.

### Command Modes

Voice class configuration (config-class)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

You can use the dscp media command to configure RPH to DSCP mapping for audio and video calls.

Granular Service Class

Priority or Precedence

DSCP Base10 Value

DSCP Binary Value

Voice

Audio Call

46

101110

Flash

43

101011

Flash Override

41

101001

Flash Override Override

40

101000

Immediate

45

101101

Priority

47

101111

Routine

49

110001

Video

Flash Override

33

100001

Flash

35

100011

Flash Override Override

32

100000

Immediate

37

100101

Priority

39

100111

Routine

51

110011

Video Call

34

100111

## Examples

The following example shows how to specify RPH to DSCP mapping after you configure the DSCP profile:

```
Router> enable Router# configure terminal Router(config)# voice class dscp-profile 1 Router(config-class)# dscp media audio routine ef
```

### Related Commands

Command

Description syslog

violation

Specifies the action that needs to be performed on any violation in the DSCP policy.

## dscp-profile

To apply a
                              		  differentiated services code point (DSCP) profile globally, use the dscp-profile command in voice service SIP configuration mode or voice class tenant
                              		  configuration mode. To disable the configuration, use the no form of this
                              		  command.

dscp-profile tag

no dscp-profile

### Syntax Description

tag

DSCP
                                          						profile tag. The range is from 1 to 10000.

### Command Default

A DSCP profile is
                              		  not applied.

### Command Modes

Voice service SIP configuration (conf-serv-sip)

Voice class tenant configuration (config-class)

## Command History

Release

Modification

15.2(2)T

This
                                          						command was introduced.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command is now available under voice class tenants.

### Usage Guidelines

You can use the dscp-profile command to apply a DSCP profile that is configured
                              		  using the dscp media command at the global level.

## Examples

The following
                              		  example shows how to configure a DSCP profile at the global level:

```
Router> enable Router# configure terminal Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# dscp-profile 1
```

### Related Commands

Command

Description

dscp
                                             						  media

Specifies
                                          						the RPH to DSCP mapping.

voice service voip

Enters
                                          						voice service configuration mode.

sip

Enters
                                          						service SIP configuration mode.

## dsn

To specify that a delivery status notice (DSN) be delivered to the sender, use the dsn command in dial-peer configuration mode. To cancel a specific DSN option, use the no form of this command.

dsn { delay | failure | success }

no dsn { delay | failure | success }

### Syntax Description

delay

Defines the delay for each mailer.

failure

Requests that a failed message be sent to the FROM address. This is the default.

success

Requests that a message be sent to the FROM address saying that the mail message was delivered successfully to the recipient.

### Command Default

The default is to send a nondelivery message in the event of a failure.

### Command Modes

Dial peer configuration

## Command History

Release

Modification

12.0(4)XJ

This command was introduced.

12.1(1)T

This command was integrated into Cisco IOS Release 12.1(1)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the Cisco 1751, Cisco 2600 series and Cisco 3600 series, Cisco 3725, and Cisco 3745.

### Usage Guidelines

When the delay keyword is selected, the next-hop mailer sends a message to the FROM address saying that the mail message was
                              delayed. The definition of the delay keyword is made by each mailer and is not controlled by the sender. Each mailer in the
                              path to the recipient that supports the DSN extension receives the same request.

When the failure keyword is selected, the next-hop mailer sends a message to the FROM address that the mail message delivery
                              failed. Each mailer in the path to the recipient that supports the DSN extension receives the same request.

When the success keyword is selected, the next-hop mailer sends a message to the FROM address saying that the mail message
                              was successfully delivered to the recipient. Each mailer in the path to the recipient that supports the DSN extension receives
                              the same request.

In the absence of any other DSN settings (for example, no dsn, or a mailer in the path that does not support the DSN extension),
                                          a failure to deliver message always causes a nondelivery message to be generated. This nondelivery message is called a bounce.

This command is applicable to Multimedia Mail over Internet Protocol (MMoIP) dial peers.

DSNs are messages or responses that are automatically generated and sent to the sender or originator of an e-mail message
                              by the Simple Mail Transfer Protocol (SMTP) server, notifying the sender of the status of the e-mail message. Specifications
                              for DSN are described in RFC 1891, RFC 1892, RFC 1893, and RFC 1894.

The on-ramp DSN request is included as part of the fax-mail message sent by the on-ramp gateway when the matching MMoIP dial
                              peer has been configured. The on-ramp DSN response is generated by the SMTP server when the fax-mail message is accepted.
                              The DSN is sent back to the user defined by the mta send mail - from command. The off-ramp DSN is requested by the e-mail client. The DSN response is generated by the SMTP server when it receives
                              a request as part of the fax-mail message.

DSNs are generated only if the mail client on the SMTP server is capable of responding to a DSN request.

Because the SMTP server generates the DSNs, you need to configure both mail from: and rcpt to: on the server for the DSN feature
                              to work. For example:

```
mail from: <user@mail-server.sample.com>
rcpt to: <fax=555-0112@sample.com> NOTIFY=SUCCESS,FAILURE,DELAY
```

Three different states can be reported back to the sender:

Delay--Indicates that the message was delayed in being delivered to the recipient or mailbox.

Success--Indicates that the message was successfully delivered to the recipient or mailbox.

Failure--Indicates that the SMTP server was unable to deliver the message to the recipient or mailbox.

Because these delivery states are not mutually exclusive, you can configure store-and-forward fax to generate these messages
                              for all or any combination of these events.

DSN messages notify the sender of the status of a particular e-mail message that contains a fax TIFF image. Use the dsn command to specify which notification messages are sent to the user.

The dsn command allows you to select more than one notification option by reissuing the command and specifying a different notification
                              option each time. To discontinue a specific notification option, use the no form of the command for that specific keyword.

If the failure keyword is not included when DSN is configured, the sender receives no notification of message delivery failure. Because
                              a failure is usually significant, care should be taken to always include the f ailure keyword as part of the dsn command configuration.

This command applies to on-ramp store-and-forward fax functions.

## Examples

The following example specifies that a DSN message be returned to the sender when the e-mail message that contains the fax
                              has been successfully delivered to the recipient or if the message that contains the fax has failed to be delivered:

```
dial-peer voice 10 mmoip
 dsn success
 dsn failure
```

### Related Commands

Command

Description

mta send mail - from hostname

Specifies the originator (host-name portion) of the e-mail fax message.

mta send mail - from username

Specifies the originator (username portion) of the e-mail fax message.

## dsp allocation signaling dspid

To change the digital signal processor (DSP) selection for signaling channel allocation from the default (DSP weight-based)
                              to the DSP ID number, use the dsp allocation signaling dspid command in voice-card configuration mode. To return to the default behavior, use the no form of this command.

dsp allocation signaling dspid

no dsp allocation signaling dspid

### Syntax Description

This command has no arguments or keywords.

### Command Default

Selection of a DSP for signaling channel allocation is based on the internal weighted value assigned to the DSPs.

### Command Modes

Voice-card configuration (config-voicecard)

## Command History

Release

Modification

12.4(15)T9

This command was introduced.

### Usage Guidelines

The dsp allocation signaling dspid command takes effect only after a reload of the router. The command should be enabled and saved into the startup-config file.

The default signal channel allocation method (by weight) may not be suitable for some network implementations. The default
                              allocation method selects the DSPs based on the DSP weight, and you cannot control the selection of the DSP for specific configuration
                              even if the order of the packet voice data modules (PVDMs) is changed. Enable the dsp allocation signaling dspid command to change the selection order to the DSP ID number. This command is more useful when there is a PVDM2-8 module in
                              the network configuration.

## Examples

The following example shows how to change the default for DSP allocation from the DSP weight to the DSP ID number:

```
voice card 1
 dsp allocation signaling dspid
```

### Related Commands

Command

Description

show voice dsp

Displays the current status or selective statistics of DSP voice channels.

voice-card

Enters voice-card configuration mode.

## dsp services dspfarm

To enable digital-signal-processor (DSP) farm services for a particular voice network module, use the dsp services dspfarm command in voice card configuration mode. To disable services, use the no form of this command.

dsp services dspfarm

no dsp services dspfarm

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

Voice-card configuration (config-voicecard)

## Command History

Release

Modification

12.2(13)T

This command was introduced.

Cisco IOS XE
                                          Release 3.2S

Support for this command was added on Cisco ASR 1000 Series Routers.

### Usage Guidelines

The router must be equipped with one or more voice network modules that provide DSP resources. DSP resources are used only
                              if this command is configured under the particular voice card.

The number of voice network modules that must be enabled for DSP-farm services depends on the number of DSPs on the module
                              and on the maximum number of transcoding and conferencing sessions configured for the DSP farm.

Use this command before enabling DSP-farm services with the dspfarm command for an NM-HDV or NM-HDV-FARM.

Cisco ASR 1000 Series Router

The SPA-DSPs on a Cisco ASR 1000 Series Routers are installed in a subslot on a SIP. Hence, when referring to a SPA-DSP the voice-card command is used.

## Examples

The following example enables DSP-farm services on an NM-HDV2 or NM-HD-1V/2V/2VE:

```
Router(config)# voice-card 2 Router(config-voicecard)# dsp services dspfarm Router(config-voicecard)# exit
```

The following example enables DSP-farm services on an NM-HDV or NM-HDV-FARM:

```
Router(config)# voice-card 2 Router(config-voicecard)# dsp services dspfarm Router(config-voicecard)# exit
```

The following example enables DSP-farm services on SPA-DSP for a Cisco ASR 1000 Series Router:

```
Router(config)# voice-card 1/1 Router(config-voicecard)# dsp services dspfarm Router(config-voicecard)# exit
```

### Related Commands

Command

Description

dsp services dspfarm

Enables the DSP farm services.

dspfarm profile

Enters the DSP farm profile configuration mode, and defines a profile for the DSP farm services.

show voice dsp (SPA-DSP)

Displays the DSP current status or the selective statistics of the DSP voice channels.

## dspfarm (DSP farm)

To enable digital signal processor (DSP) farm service, use the dspfarm command in global configuration mode. To disable the service, use the no form of this command.

dspfarm

no dspfarm

### Syntax Description

This command has no arguments or keywords.

### Command Default

DSP-farm service is disabled.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(5)YH

This command was introduced on the Cisco VG200.

12.2(13)T

This command was implemented on the Cisco 2600 series, Cisco 3620, Cisco 3640, Cisco 3660, and Cisco 3700 series.

### Usage Guidelines

The router on which this command is used must be equipped with one or more digital T1/E1 packet voice trunk network modules
                              (NM-HDVs) or high-density voice (HDV) transcoding/conferencing DSP farms (NM-HDV-FARMs) to provide DSP resources.

Before enabling DSP-farm services, you must configure the NM-HDV or NM-HDV-FARM on which DSP-farm services are to be enabled
                              using the dsp services dspfarm command. You must also specify the maximum number of transcoding sessions to be supported by the DSP farm using the dspfarm transcoder maximum sessions command.

This command causes the system to download new firmware into the DSPs, start up the required subsystems, and wait for a service
                              request from the transcoding and conferencing applications.

## Examples

The following example configures an NM-HDV or NM-HDV-FARM, specifies the maximum number of transcoding sessions, and enables
                              DSP-farm services:

```
Router# configure terminal Router(config)# no dspfarm Router(config)# voice-card 2 Router(config-voicecard)# dsp services dspfarm Router(config-voicecard)# exit Router(config)# dspfarm transcoder maximum sessions 15 Router(config)# dspfarm
```

### Related Commands

Command

Description

dsp services dspfarm

Specifies the NM-HDV or NM-HDV-FARM on which DSP-farm services are to be enabled.

dspfarm transcoder maximum sessions

Specifies the maximum number of transcoding sessions to be supported by a DSP farm.

show dspfarm

Displays summary information about DSP resources.

## dspfarm (voice-card)

To add a specified voice card to those participating in a digital signal processor (DSP) resource pool, use the dspfarm command in voice-card configuration mode. To remove the specified card from participation in the DSP resource pool, use the no form of this command.

dspfarm

no dspfarm

### Syntax Description

This command has no arguments or keywords.

### Command Default

A card participates in the DSP resource pool.

### Command Modes

Voicecard configuration (config-voicecard)

## Command History

Release

Modification

12.1(5)XM

This command was introduced on the Cisco 3660.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(2)XB

This command was implemented on the Cisco 2600 series routers.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T.

12.2(15)T

This command was implemented on the Cisco 2600XM, Cisco 3725, and Cisco 3745.

### Usage Guidelines

DSP mapping occurs when DSP resources on one AIM or network module are available for processing of voice time-division multiplexing
                              (TDM) streams on a different network module or on a voice/WAN interface card (VWIC). This command is used on Cisco 3660 routers
                              with multiservice interchange (MIX) modules installed or on Cisco 2600 series routers with AIMs installed.

To reach voice-card configuration mode for a particular voice card, from global configuration mode enter the voice - card command and the slot number for the AIM or network module that you want to add to the pool. See the voice - card command page for details on slot numbering.

The assignment of DSP pool resources to particular TDM streams is based on the order in which the streams are configured
                              with the ds0 - group command for T1/E1 channel-associated signaling (CAS) or with the pri - group command for ISDN PRI.

The assignment of DSP pool resources does not occur dynamically during call signaling.

## Examples

The following example adds to the DSP resource map the DSP resources on the network module in slot 5 on a Cisco 3660 with
                              a MIX module:

```
voice-card 5
 dspfarm
```

The following example makes available the DSP resources on an AIM on a modular access router:

```
voice-card 0
 dspfarm
```

### Related Commands

Command

Description

ds0-group

Specifies the DS0 time slots that make up a logical voice port on a T1 or E1 controller, Specifies the signaling type by
                                          which the router communicates with the PBX or PSTN, Defines T1or E1 channels for compressed voice calls and the CAS method
                                          by which the router connects to the PBX or PSTN.

pri-group

Specifies ISDN PRI on a channelized T1 or E1 controller.

voice-card

Enters voice-card configuration mode.

## dspfarm confbridge maximum

To specify the maximum number of concurrent conference sessions for which digital signal processor (DSP) farm resources should
                              be allocated, use the dspfarm confbridge maximum command in global configuration mode. To reset to the default, use the no form of this command.

dspfarm confbridge maximum { mixed-mode sessions | sessions } number

no dspfarm confbridge maximum { mixed-mode sessions | sessions } number

### Syntax Description

mixed-mode

Specifies the maximum number of transcoding sessions for mixed-mode conferencing.

sessions

Specifies the conferencing maximum sessions parameter value.

number

Number of conference sessions. A single DSP supports one conference session with up to six participants.

### Command Default

No DSP farm resources are allocated for the sessions.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(5)YH

This command was introduced on the Cisco VG200.

12.2(13)T

This command was modified. This command was implemented on the Cisco 2600 series, Cisco 3620, Cisco 3640, Cisco 3660, and
                                          Cisco 3700 series.

15.0(1)M

This command was modified. The mixed-mode keyword was added.

### Usage Guidelines

The router on which this command is used must be equipped with one or more digital T1/E1 packet voice trunk network modules
                              (NM-HDVs) or high-density voice (HDV) transcoding/conferencing DSP farms (NM-HDV-FARMs) to provide DSP resources.

Before using this command, you must disable DSP-farm service using the no dspfarm command.

The maximum number of conference sessions depends upon DSP availability in the DSP farm. A single DSP supports one conference
                              session with up to six participants. However, you may need to allocate additional DSP resources for transcoding to support
                              conferences. If all participants use G.711 or G.729 codecs, you need not allocate any additional DSP resources because transcoding
                              is done in the conferencing DSP.

When you use this command, take into consideration the number of DSPs allocated for transcoding services with the dspfarm transcoder maximum sessions command.

## Examples

The following example sets the maximum number of transcoding sessions for mixed-mode conferencing to 8:

```
Router# dspfarm confbridge maximum mixed-mode sessions 8
```

### Related Commands

Command

Description

dspfarm (DSP farm)

Enables DSP-farm service.

dspfarm transcoder maximum sessions

Specifies the maximum number of transcoding sessions to be supported by a DSP farm.

show dspfarm

Displays summary information about DSP resources.

## dspfarm connection interval

To specify the time interval during which to monitor Real-Time Transport Protocol (RTP) inactivity before deleting an RTP
                              stream, use the dspfarm connection interval command in global configuration mode. To reset to the default, use the no form of this command.

dspfarm connection interval seconds

no dspfarm connection interval seconds

### Syntax Description

seconds

Interval, in seconds, during which to monitor RTP inactivity. Range is from 60 to 10800. Default is 600.

### Command Default

600 seconds

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(5)YH

This command was introduced on the Cisco VG200.

12.2(13)T

This command was implemented on the Cisco 2600 series, Cisco 3620, Cisco 3640, Cisco 3660, and Cisco 3700 series.

### Usage Guidelines

The router on which this command is used must be equipped with one or more digital T1/E1 packet voice trunk network modules
                              (NM-HDVs) or high-density voice (HDV) transcoding/conferencing DSP farms (NM-HDV-FARMs) to provide digital signal processor
                              (DSP) resources.

After each interval, RTP streams are checked for inactivity. If all RTP streams for a particular call are inactive, the RTP
                              timer, as set with the dspfarm rtp timeout command, is started. When the RTP timer expires, the call is deleted.

## Examples

The following example sets the connection interval to 60 seconds:

```
Router(config)# dspfarm connection interval 60
```

### Related Commands

Command

Description

dspfarm rtp timeout

Specifies the RTP timeout interval used to clear hanging connections.

## dspfarm profile

To enter DSP farm profile configuration mode and define a profile for digital signal processor (DSP) farm services, use the dspfarm profile command in global configuration mode. To delete a disabled profile, use the no form of this command.

### Cisco Unified Border Element

dspfarm profile profile-identifier { conference | mtp | transcode } [ security ]

no dspfarm profile profile-identifier

### Cisco Unified Border Element (Enterprise) Cisco ASR 1000 Series Router

dspfarm profile profile-identifier transcode

no dspfarm profile profile-identifier

### Cisco Integrated Services Routers Generation 2 (Cisco ISR G2)

dspfarm profile profile-identifier { conference [ video [ homogeneous | heterogeneous | guaranteed-audio ]] | mtp | transcode [ video | universal ]} [ security ]

no dspfarm profile profile-identifier

### Syntax Description

profile identifier

Number that uniquely identifies a profile. Range is 1 to 65535. There is no default.

conference

Enables a profile for conferencing.

mtp

Enables a profile for Media Termination Point (MTP).

transcode

Enables a profile for transcoding.

security

Enables a profile for secure DSP farm services.

video

(Optional) Enables a profile for video conferencing or transcoding.

homogeneous

(Optional) Specifies that all video participants use the one video format that is configured in this profile. DSP resources
                                          are reserved to support the conference at configuration time.

The homogeneous profiles only support one video codec.

heterogeneous

(Optional) Specifies that video participants can use the different video formats that are configured in the profile. You can
                                          configure up to 10 video codecs in the heterogeneous profile. DSP resources are reserved to support the different configurations
                                          at configuration time.

guaranteed-audio

(Optional) Specifies that video participants in a heterogeneous conference will at least have an audio connection. You can
                                          configure up to 10 video codecs in the guaranteed-audio profile. The DSP resources for audio streams are reserved at configuration
                                          time, but DSP resources to support video conferences are not reserved. If the video endpoint supports the video format specified
                                          in the profile and DSP resources are available when the participant joins the conference, the participant joins as a video
                                          conferee in the video conference.

### Command Default

If this command is not entered, no profiles are defined for the DSP farm services.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.4(11)XW

The security keyword was added.

12.4(20)T

This command was integrated into Cisco IOS Release 12.4(20)T.

12.4(22)T

Support for IPv6 was added.

15.0(1)M2
                                          15.1(1)T

Support was modified for the Cisco IAD 2430, IAD 2431, IAD 2432, and IAD  2435, and the Cisco VG 202, VG 204, and VG 224 platforms.

Cisco IOS XE 
                                          Release 3.2S

This command was modified. Support was added to the Cisco ASR 1000 Series Router. The conference , mtp & security keywords are not supported on the Cisco ASR 1000 Series Router in this release.

15.1(4)M

This command was modified. The video keyword was added.

Cisco IOS XE 
                                          Release 3.2S

This command was integrated into Cisco IOS XE Release 3.3S.

Cisco IOS XE Cupertino 17.7.1a

Introduced support for YANG models.

### Usage Guidelines

Use this command to create a new profile or delete a disabled profile. After you create a new profile in dspfarm profile configuration
                              mode, use the no shutdown command to enable the profile configuration, allocate resources and associate the profile with the application(s). If the
                              profile cannot be enabled due to lack of resources, the system prompts you with a message "Can not enable the profile  due
                              to insufficient resources, resources available to support X  sessions; please  modify the configuration and retry."

If the DSP farm profile is successfully created, you enter the DSP farm profile configuration mode. You can configure multiple
                              profiles for the same service.

Use the no dspfarm profile command to delete a profile from the system. If the profile is active, you cannot delete it; you must first disable it using
                              the shutdown command. To modify a DSP farm profile, use the shutdown command in dspfarm profile configuration mode before you begin configuration.

The profile identifier uniquely identifies a profile. If the service type and profile identifier are not unique, the user is prompted with a message to choose a different profile identifier.

You must use the security keyword in order to enable secure DSP farm services such as secure transcoding.

Effective with Cisco IOS Releases 15.0(1)M2 and 15.1(1)T, platform support for the Cisco IAD 2430, IAD 2431, IAD 2432, and
                              IAD 2435, and the Cisco VG 202, VG 204, and VG 225 is modified. These platforms are designed as TDM-IP devices and are not
                              expandable to install extra DSP resources. So even though the conference keyword appears in the command syntax, this DSP service is not configurable on these platforms. If you try to configure conferencing
                              on these platforms, the command-line interface displays the following message: "
                              %This platform does not support Conferencing feature.
                              "

The transcode keyword also appears in the command syntax, but this DSP service is not available on the Cisco VG 202, VG 204, and VG 224
                              platforms. If you try to configure transcoding on these platforms, the CLI displays the following message: "
                              %This platform does not support Transcoding feature.
                              "

Cisco ASR 1000 Series Router

The support for dspfarm profile command was added on Cisco ASR 1000 Series Router from Cisco IOS XE Release 3.2 and later
                              releases. The command is used to create a dspfarm profile for different services.

The secure DSP farm services is always enabled for SPA-DSP on Cisco ASR 1000 Series Router. Only transcode keyword is supported on Cisco ASR 1000 Series Router for Cisco IOS XE Release 3.2s. The conference , media , and security keywords are not supported on Cisco ASR 1000 Series Router for Cisco IOS XE Release 3.2s.

In order to configure a video dspfarm profile, you must set voice-service dsp-reservation command to be less than 100 percent.

To enable dspfarm profiles for voice services, you must use the 
                              dsp services dspfarm command under the voice-card submode.

## Examples

The following example enables DSP farm services profile 20 for conferencing:

```
Router(config)# dspfarm profile 20 conference
```

Note the response if the profile is already being used:

```
Router(config)# dspfarm profile 6 conference Profile id 6 is being used for service TRANSCODING 
 please select a different profile id
```

The following example enables DSP farm services profile 1 for transcoding:

```
Router(config)# dspfarm profile 1 transcode
```

## Examples

The following example enables DSP farm services profile 99 for homogeneous video. The conference supports four participants
                              under one format (Video codec H.263, qcif resolution, and a frame-rate of 15 f/s).

```
Router(config)# dspfarm profile 99 conference video homogeneous Router(config-dspfarm-profile)# codec h263 qcif frame-rate 15 Router(config-dspfarm-profile)# maximum conference-participant 4
```

### Related Commands

Command

Description

dsp service dspfarm

Configures the DSP farm services for a specified voice card.

shutdown (DSP farm profile)

Disables the DSP farm profile.

voice-card

Enters voice card configuration mode

voice-service dsp-reservation

Configures the percentage of DSP resources are reserved for voice services and enables video services to use the remaining
                                          DSP resources.

## dspfarm rtp timeout

To specify the Real-Time Transport Protocol (RTP) timeout interval used to clear hanging connections, use the dspfarm rtp timeout command in global configuration mode. To reset to the default, use the no form of this command.

dspfarm rtp timeout seconds

no dspfarm rtp timeout

### Syntax Description

seconds

RTP timeout interval, in seconds. Range is from 10 to 7200. Default is 1200.

### Command Default

1200 seconds (20 minutes)

### Command Modes

Global configuration

## Command History

Release

Modification

12.1(5)YH

This command was introduced on the Cisco VG200.

12.2(13)T

This command was implemented on the Cisco 2600 series, Cisco 3620, Cisco 3640, Cisco 3660, and Cisco 3700 series.

### Usage Guidelines

The router on which this command is used must be equipped with one or more digital T1/E1 packet voice trunk network modules
                              (NM-HDVs) or high-density voice (HDV) transcoding/conferencing DSP farms (NM-HDV-FARMs) to provide digital signal processor
                              (DSP) resources.

Use this command to set the RTP timeout interval for when the error condition "RTP port unreachable" occurs.

## Examples

The following example sets the RTP timeout value to 600 seconds (10 minutes):

```
Router# dspfarm rtp timeout 600
```

### Related Commands

Command

Description

dspfarm (DSP farm)

Enables DSP-farm service.

dspfarm connection interval

Specifies the time interval during which to monitor RTP inactivity before deleting an RTP stream.

show dspfarm

Displays summary information about DSP resources.

## dspfarm transcoder maximum sessions

To specify the maximum number of transcoding sessions to be supported by the digital signal processor (DSP) farm, use the dspfarm transcoder maximum sessions command in global configuration mode. To reset to the default, use the no form of this command.

dspfarm transcoder maximum sessions number

no dspfarm transcoder maximum sessions

### Syntax Description

number

Number of transcoding sessions.

### Command Default

0 sessions

### Command Modes

Global configuration

## Command History

Release

Modification

12.1(5)YH

This command was introduced on the Cisco VG200.

12.2(13)T

This command was implemented on the Cisco 2600 series, Cisco 3620, Cisco 3640, Cisco 3660, and Cisco 3700 series.

### Usage Guidelines

The router on which this command is used must be equipped with one or more digital T1/E1 packet voice trunk network modules
                              (NM-HDVs) or high-density voice (HDV) transcoding/conferencing DSP farms (NM-HDV-FARMs) to provide DSP resources.

Before using this command, you must disable DSP-farm service using the no dspfarm command.

Use this command in conjunction with the dspfarm confbridge maximum sessions commands.

The maximum number of transcoding sessions depends upon DSP availability in the DSP farm. A single DSP supports four transcoding
                              sessions transmitted to and from G.711 and G.729 codecs.

## Examples

The following example configures an NM-HDV or NM-HDV-FARM, specifies the maximum number of transcoding sessions, and enables
                              DSP-farm services:

```
Router# configure terminal Router(config)# no dspfarm Router(config)# voice-card 2 Router(config-voicecard)# dsp services dspfarm Router(config-voicecard)# exit Router(config)# dspfarm transcoder maximum sessions 15 Router(config)# dspfarm
```

### Related Commands

Command

Description

dspfarm (DSP farm)

Enables DSP-farm service.

dspfarm confbridge maximum sessions

Specifies the maximum number of conferencing sessions to be supported by a DSP farm.

dsp services dspfarm

Specifies the NM-HDV or NM-HDV-FARM on which DSP-farm services are to be enabled.

show dspfarm

Displays summary information about DSP resources.

## dspint dspfarm

To enable the digital signal processor (DSP) interface, use the dspint dspfarm command in global configuration mode.
                              		  This command does not have a no form.

dspint dspfarm slot/port

### Syntax Description

slot

Slot number of the interface.

port

Port number of the interface.

### Command Default

Enabled

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(5)XE

This command was introduced on the Cisco 7200 series
                                          						routers.

12.1(1)T

This command was integrated into Cisco IOS Release
                                          						12.1(1)T.

12.2(13)T

This command was implemented on the Cisco 7200 series.

### Usage Guidelines

DSP mapping occurs when DSP resources on one advanced interface
                              		  module (AIM) or network module are available for processing of voice
                              		  time-division multiplexing (TDM) streams on a different network module or on a
                              		  voice/WAN interface card (VWIC). This command is used on Cisco 3660 routers
                              		  with multiservice interchange (MIX) modules installed or on Cisco 2600 series
                              		  routers with AIMs installed.

To enter voice-card configuration mode for a particular voice card,
                              		  from global configuration mode enter the voice-card command and the slot number for the AIM or network module that
                              		  you want to add to the pool. See the voice-card command page for details on slot numbering.

The assignment of DSP pool resources to particular TDM streams is
                              		  based on the order in which the streams are configured using the ds0-group command for T1/E1
                              		  channel-associated signaling (CAS) or using the pri-group command for ISDN PRI.

The assignment of DSP pool resources does not occur dynamically
                              		  during call signaling.

To disable the interface use the no shutdown command.

## Examples

The following example creates a DSP farm interface with a slot number
                              		  of 1 and a port number of 0:

```
dspint dspfarm 1/0
```

To change codec complexity on the Cisco 7200 series, you must enter
                              		  the following commands:

```
Router# configure terminal Router(config)# dspint dspfarm 2/0 Router(config-dspfarm)# codec medium | high ecan-extended
```

### Related Commands

Command

Description

ds0-group

Specifies the DS0 time slots that make up a logical voice
                                          						port on a T1 or E1 controller.

no shutdown

Disables the interface.

pri-group

Specifies an ISDN PRI on a channelized T1 or E1 controller

show interfaces dspfarm dsp

Displays information about the DSP interface.

voice-card

Enters voice-card configuration mode.

## dtmf-interworking

To enable a delay between the dtmf-digit begin and dtmf-digit end events in the RFC 2833 packets sent from Cisco Unified
                              Border Element (Cisco UBE) or Cisco Unified Communications Manager Express (Cisco Unified CME) or to generate RFC 4733 compliance
                              RTP Named Telephony Event (NTE) packets from CUBE, use the dtmf-interworking command in voice service or dial peer voice configuration mode. To remove the delay interval, use the no form of this command.

dtmf-interworking { rtp-nte | standard | system }

no dtmf-interworking

### Syntax Description

rtp-nte

Enables a delay between the dtmf-digit begin and dtmf-digit end events of RTP NTE packets.

standard

Generates RTP NTE packets that are RFC 4733 compliant.

system

Specifies the default global dual tone multifrequency (DTMF) interworking configuration. This keyword is available only in
                                          dial peer voice configuration mode.

### Command Default

RFC 2833 packet is sent in a single burst of three dtmf-digit begin events, one duration equaling 50 ms, and three dtmf-digit
                              end events with a duration of 100 ms.

### Command Modes

Voice service configuration (config-voi-serv)

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.4(15)XZ

This command was introduced.

12.4(20)T

This command was integrated into Cisco IOS Release 12.4(20)T.

15.1(2)T5

This command was modified. The standard and system keywords were added.

Cisco IOS XE Cupertino 17.7.1a

Introduced support for YANG models.

### Usage Guidelines

dtmf-interworking rtp-nte —If your system is configured for RFC 2833 DTMF interworking and if the remote system cannot handle RFC 2833 packets sent
                                    in a single burst, use this command to introduce a delay between the dtmf-digit begin and end events in the RFC 2833 packet.

dtmf-interworking standard —When the remote system needs RFC 4733 packets, then use this command to generate RFC 4733 compliance. In this configuration,
                                    one dtmf-digit begin event is initiated when CUBE receives start event.

dtmf-interworking system —When this command is configured in dial peer voice configuration mode then the global level dtmf-interworking configuration
                                    is applicable. This is the default configuration under the dial peer.

## Examples

The following example shows configuration of a delay between the dtmf-digit and events:

```
Device> enable Device# configure terminal Device(config)# voice service voip Device(config-voi-serv)# dtmf-interworking rtp-nte Device(config-voi-serv)# end
```

The following example shows the generation of RTP NTE packets that are RFC 4733 compliant:

```
Device> enable Device# configure terminal Device(config)# voice service voip Device(config-voi-serv)# dtmf-interworking standard Device(config-voi-serv)# end
```

### Related Commands

Command

Description

keypad-normalize

Ensures that the delay configured for a dtmf-end event is always honored.

nte-end-digit-delay

Specifies the length of delay for each digit in a dtmf-digit end event.

## dtmf timer inter-digit

To configure the dual tone multifrequency (DTMF) interdigit timer for a DS0 group, use the dtmf timer inter - digit command in T1 controller configuration mode. To restore the timer to its default value, use the no form of this command.

dtmf timer inter-digit milliseconds

no dtmf timer inter-digit

### Syntax Description

milliseconds

DTMF interdigit timer duration, in milliseconds. Range is from 250 to 3000. The default is 3000.

### Command Default

3000 milliseconds

### Command Modes

T1 controller configuration

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco AS5300.

### Usage Guidelines

Use the dtmf timer inter - digit command to specify the duration in milliseconds the router waits to detect the end of DTMF digits. After this period, the
                              router expects no more digits to arrive and establishes the call.

## Examples

The following example, beginning in global configuration mode, sets the DTMF interdigit timer value to 250 milliseconds:

```
controller T1 2
 ds0-group 2 timeslots 4-10 type e&m-fgb dtmf dnis
 cas-custom 2
 dtmf timer inter-digit 250
```

### Related Commands

Command

Description

cas-custom

Customizes E1 R2 signaling parameters for a particular E1 channel group on a channelized E1 line.

ds0-group

Configures channelized T1 time slots, which enables a Cisco AS5300 modem to answer and send an analog call.

## dtmf-relay (Voice over Frame Relay)

To enable the generation of FRF.11 Annex A frames for a dial peer, use the dtmf - relay command in dial-peer configuration mode. To disable the generation of FRF.11 Annex A frames and return to the default handling
                              of dial digits, use the no form of this command.

dtmf-relay

no dtmf-relay

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

Dial peer configuration

## Command History

Release

Modification

12.0(3)XG

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.0(4)T

This command was integrated into Cisco IOS Release 12.0(4)T, and implemented on the Cisco 7200 series router.

### Usage Guidelines

Cisco recommends that this command be used with low bit-rate codecs.

When dtmf - relay (VoFR) is enabled, the digital signal processor (DSP) generates Annex A frames instead of passing a dual tone multifrequency
                              (DTMF) tone through the network as a voice sample. For information about the payload format of FRF.11 Annex A frames, see
                              the Cisco IOS Wide-Area Networking Configuration Guide.

## Examples

The following example shows how to enable FRF.11 Annex A frames for VoFR dial peer 200, starting from global configuration
                              mode:

```
dial-peer voice 200 vofr
 dtmf-relay
```

### Related Commands

Command

Description

called-number (dial peer)

Enables an incoming VoFR call leg to get bridged to the correct POTS call leg when using a static FRF.11 trunk connection.

codec (dial peer)

Specifies the voice coder rate of speech for a VoFR dial peer.

connection

Specifies a connection mode for a voice port.

cptone

Specifies a regional analog voice interface-related tone, ring, and cadence setting.

destination-pattern

Specifies the prefix, the full E.164 telephone number, or an ISDN directory number (depending on the dial plan) to be used
                                          for a dial peer.

preference

Indicates the preferred order of a dial peer within a rotary hunt group.

session protocol

Establishes a session protocol for calls between the local and remote routers via the packet network.

session target

Specifies a network-specific address for a specified dial peer or destination gatekeeper.

signal-type

Sets the signaling type to be used when connecting to a dial peer.

## dtmf-relay (Voice over IP)

To specify how an H.323 or Session Initiation Protocol (SIP) gateway relays dual tone multifrequency (DTMF) tones between
                              telephony interfaces and an IP network, use the dtmf-relay command in dial peer voice configuration mode. To remove all signaling options and send the DTMF tones as part of the audio
                              stream, use the no form of this command.

dtmf-relay [ cisco-rtp ] [ h245-alphanumeric ] [ h245-signal ] [ rtp-nte [ digit-drop ]] [ sip-notify ] [ sip-info ] [ sip-kpml ]

no dtmf-relay

### Syntax Description

cisco - rtp

Forwards DTMF tones by using Real-Time Transport Protocol (RTP) with a Cisco proprietary payload type.

h245 - alphanumeric

Forwards DTMF tones by using the H.245 "alphanumeric" User Input Indication method. Supports tones from 0 to 9, *, #, and
                                          from A to D.

h245 - signal

Forwards DTMF tones by using the H.245 "signal" User Input Indication method. Supports tones from 0 to 9, *, #, and from A
                                          to D.

rtp - nte

Forwards DTMF tones by using RTP with the Named Telephone Event (NTE) payload type.

digit-drop

Passes digits out-of-band and drops in-band digits.

The digit-drop keyword is only available when the rtp - nte keyword is configured.

sip-info

Forwards DTMF tones using SIP INFO messages. This keyword is available only if the VoIP dial peer is configured for SIP.

sip-kpml

Forwards DTMF tones using SIP KPML over SIP SUBSCRIBE/NOTIFY messages. This keyword is available only if the VoIP dial peer
                                          is configured for SIP.

sip-notify

Forwards DTMF tones using SIP NOTIFY messages. This keyword is available only if the VoIP dial peer is configured for SIP.

### Command Default

DTMF tones are disabled and sent in-band. That is, they are left in the audio stream.

### Command Modes

Dial peer voice configuration

## Command History

Release

Modification

11.3(2)NA

This command was introduced on the Cisco AS5300.

12.0(2)XH

The cisco - rtp , h245 - alphanumeric , and h245 - signal keywords were added.

12.0(5)T

This command was integrated into Cisco IOS Release 12.0(5)T.

12.0(7)XK

This command was first supported for VoIP on the MC3810.

12.1(2)T

Changes made in Cisco IOS Release 12.0(7)XK were integrated into Cisco IOS Release 12.1(2)T.

12.2(8)T

This command was implemented on the Cisco 1751, Cisco 2600 series and Cisco 3600 series, Cisco 3725, and Cisco 3745.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          was not included in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850 platform.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

12.2(15)ZJ

The sip-notify keyword was added.

12.3(4)T

This command was integrated into Cisco IOS Release 12.3(4)T.

12.3(11)T

The digit - drop keyword was added.

15.3(3)M

Introduced support for YANG models.

### Usage Guidelines

DTMF is the tone generated when you press a button on a touch-tone phone. This tone is compressed at one end of a call; when
                              the tone is decompressed at the other end, it can become distorted, depending on the codec used. The DTMF relay feature transports
                              DTMF tones generated after call establishment out-of-band using either a standard H.323 out-of-band method or a proprietary
                              RTP-based mechanism. For SIP calls, the most appropriate method to transport DTMF tones is RTP-NTE or SIP-NOTIFY.

This command specifies how an H.323 or SIP gateway relays DTMF tones between telephony interfaces and an IP network.

You must include one or more keywords when using this command.

To avoid sending both in-band and out-of band tones to the outgoing leg when sending IP-to-IP gateway calls in-band (rtp-nte)
                              to out-of band (h245-alphanumeric), configure the dtmf-relay command using the rtp-nte and digit-drop keywords on the incoming SIP dial peer. On the H.323 side, and for H.323 to SIP calls, configure this command using either
                              the h245-alphanumeric or h245-signal keyword.

The SIP-NOTIFY method sends NOTIFY messages bidirectionally between the originating and terminating gateways for a DTMF event
                              during a call. If multiple DTMF relay mechanisms are enabled on a SIP dial peer and are negotiated successfully, the SIP-NOTIFY
                              method takes precedence.

SIP NOTIFY messages are advertised in an invite message to the remote end only if the dtmf-relay command is set.

You can configure dtmf-relay sip-info only if the allow-connections sip to sip command is enabled at the global level.

For SIP, the gateway chooses the format according to the following priority:

sip-notify (highest priority)

rtp-nte

None--DTMF sent in-band

The gateway sends DTMF tones only in the format that you specify if the remote device supports it. If the H.323 remote device
                              supports multiple formats, the gateway chooses the format according to the following priority:

cisco-rtp (highest priority)

h245-signal

h245-alphanumeric

rtp-nte

None--DTMF sent in-band

The principal advantage of the dtmf-relay command is that it sends DTMF tones with greater fidelity than is possible in-band for most low-bandwidth codecs, such as
                              G.729 and G.723. Without the use of DTMF relay, calls established with low-bandwidth codecs may have trouble accessing automated
                              DTMF-based systems, such as voice mail, menu-based Automatic Call Distributor (ACD) systems, and automated banking systems.

The cisco - rtp keyword supports a proprietary Cisco implementation and operates only between two Cisco 2600 series or Cisco 3600 series
                                          routers running Cisco IOS Release 12.0(2)XH or later. Otherwise, the DTMF relay feature does not function, and the gateway
                                          sends DTMF tones in-band.

The cisco-rtp keyword is supported on Cisco 7200 series routers.

The sip-notify keyword is available only if the VoIP dial peer is configured for SIP.

The digit-drop keyword is available only when the rtp-nte keyword is configured.

## Examples

The following example configures DTMF relay with the cisco - rtp keyword when DTMF tones are sent to dial peer 103:

```
dial-peer voice 103 voip
 dtmf-relay cisco-rtp
```

The following example configures DTMF relay with the cisco - rtp and h245 - signal keywords when DTMF tones are sent to dial peer 103:

```
dial-peer voice 103 voip
 dtmf-relay cisco-rtp h245-signal
```

The following example configures the gateway to send DTMF in-band (the default) when DTMF tones to are sent dial peer 103:

```
dial-peer voice 103 voip
 no dtmf-relay
```

The following example configures DTMF relay with the digit - drop keyword to avoid both in-band and out-of band tones being sent to the outgoing leg on H.323 to H.323 or H.323 to SIP calls:

```
dial-peer voice 1 voip
 session protocol sipv2
 dtmf-relay h245-alphanumeric rtp-nte digit-drop
```

The following example configures DTMF relay with the rtp-nte keyword when DTMF tones are sent to dial peer 103:

```
dial-peer voice 103 voip
 dtmf-relay rtp-nte
```

The following example configures the gateway to send DTMF tones using SIP NOTIFY messages to dial peer 103:

```
dial-peer voice 103 voip
 session protocol sipv2
 dtmf-relay sip-notify
```

The following example configures the gateway to send DTMF tones using SIP INFO messages to dial peer 10:

```
dial-peer voice 10 voip
  dtmf-relay sip-info
```

### Related Commands

Command

Description

notify telephone-event

Configures the maximum interval between two consecutive NOTIFY messages for a particular telephone event.

## dualtone

To enter cp-dualtone configuration mode for specifying a custom call-progress tone, use the dualtone command in custom-cpto
                              ne voice-class 
                              configuration mode. To configure the custom-cptone voice class not to detect a call-progress tone, use the no form of this command.

dualtone { busy | conference | disconnect | number-unobtainable | out-of-service | reorder | ringback }

no dualtone { busy | conference | disconnect | number-unobtainable | out-of-service | reorder | ringback }

### Syntax Description

busy

Configure busy tone.

conference

Configure conference join and leave tones.

disconnect

Configure disconnect tone.

number - unobtainable

Configure number-unavailable tone.

out - of - service

Configure out-of-service tone.

reorder

Configure reorder tone.

ringback

Configure ringback tone.

### Command Default

No call-progress tones are defined within the custom-cptone voice class.

### Command Modes

Custom-cptone voice-class configuration

## Command History

Release

Modification

12.1(5)XM

This command was introduced on the Cisco 2600 and Cisco 3600 series and on the Cisco MC3810.

12.2(2)T

This command was implemented on the Cisco 1750 router and integrated into Cisco IOS Release 12.2(2)T.

12.4(11)XJ2

The conference keyword was added.

12.4(15)T

This command was integrated into Cisco IOS Release 12.4(15)T.

### Usage Guidelines

The dualtone command enters cp-dualtone configuration mode and specifies a call-progress tone to be detected. You can specify additional
                              call-progress tones without exiting cp-dualtone configuration mode.

Any call-progress tones that are not specified are not detected.

To delete a call-progress tone from this custom-cptone voice class, use the no form of this command and the keyword for the tone that should not be detected; for example, no dualtone busy .

You must associate the class of custom call-progress tones with a voice port for this command to affect tone detection.

Use the dualtone conference command to define custom join and leave tones for hardware conferences.

## Examples

The following example enters cp-dualtone configuration mode and specifies busy tone and ringback tone in the custom-cptone
                              voice class country-x:

```
Router(config)# voice class custom-cptone country-x Router(cfg-cptone)# dualtone busy Router(cfg-cp-dualtone)# frequency 440 480 Router(cfg-cp-dualtone)# cadence 500 500 Router(cfg-cp-dualtone)# exit Router(cfg-cptone)# dualtone ringback Router(cfg-cp-dualtone)# frequency 400 440 Router(cfg-cp-dualtone)# cadence 2000 4000
```

The following example deletes ringback tone from the custom-cptone voice class country-x:

```
Router(config)# voice class custom-cptone country-x Router(cfg-cptone)# no dualtone ringback
```

The following example configures a conference leave tone. The configured leave tone must be associated with a digital signal
                              processor (DSP) farm profile:

```
Router(config)# voice class custom-cptone leavetone Router(cfg-cptone)# dualtone conference Router(cfg-cp-dualtone)# frequency 500 500 Router(cfg-cp-dualtone)# cadence 100 100 100 100 100
```

### Related Commands

Command

Description

cadence

Defines the tone on and off durations for a call-progress tone.

conference-join custom-cptone

Defines a custom call-progress tone to indicate joining a conference.

conference-leave custom-cptone

Defines a custom call-progress tone to indicate leaving a conference.

dspfarm profile

Enters DSP farm profile configuration mode and defines a profile for DSP farm services.

frequency

Defines the frequency components for a call-progress tone.

supervisory custom-cptone

Associates a class of custom call-progress tones with a voice port.

voice class custom-cptone

Creates a voice class for defining custom call-progress tones.

| system | Specifies that the disable-early-media method use the global
                                          						sip-ua value. This keyword is available only for the tenant mode to allow it to
                                          						fallback to the global configurations |
|---|---|

| Release | Modification |
|---|---|
| 12.2(13)T | This
                                          						command was introduced. |
| IOS
                                          						Release XE 2.5 | This
                                          						command was integrated into Cisco IOS XE Release 2.5. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| show sip-ua retry | Displays
                                          						SIP retry statistics. |
| show sip-ua statistics | Displays
                                          						response, traffic, and retry SIP statistics. |
| show sip-ua timers | Displays the current settings for SIP-UA timers. |
| sip-ua | Enables
                                          						the SIP-UA configuration commands. |

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |

| Release | Modification |
|---|---|
| 12.1(5)T | This command was introduced on the following platforms: Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco 7500
                                          series, Cisco AS5300, Cisco AS5800, and Cisco MC3810. |
| 12.2(2)XA | This command was implemented on the Cisco AS5400 and Cisco AS5350. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into the Cisco IOS Release 12.2(11)T. |

| Note | The disc_pi_off voice-port configuration command is valid only for the default session application; it does not work for interactive voice
                                          response (IVR) applications. |
|---|---|

| Command | Description |
|---|---|
| isdn t306 | Sets a timer for disconnect messages. |

| Release | Modification |
|---|---|
| 11.3(1)MA | This command was introduced on the Cisco MC3810. |
| 12.0(7)XK | This command was implemented on the Cisco 2600 series and Cisco 3600 series. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |

| Command | Description |
|---|---|
| show voice port | Displays voice port configuration information. |

| telephone-umber | Adds a user-selected DNIS number to a DNIS map. |
|---|---|
| url url | (Optional) URL that links a DNIS number to a specific VoiceXML document. If a URL is not entered, the DNIS number is linked
                                          to the VoiceXML application in the dial peer, which must be configured using the application command. This keyword is not valid for Tool Command Language (TCL) applications. |

| Release | Modification |
|---|---|
| 12.2(2)XB | This command was introduced on the Cisco AS5300, Cisco AS5350, and Cisco AS5400. |
| 12.2(11)T | This command was implemented on the Cisco 3640 and Cisco 3660. |

| Command | Description |
|---|---|
| dnis - map | Associates a DNIS map with a dial peer. |
| show voice dnis - map | Displays configuration information about DNIS maps. |
| voice dnis - map | Enters DNIS-map configuration mode to create a DNIS map. |
| voice dnis - map load | Reloads a DNIS map that has changed since the previous load. |

| map - name | Name of the configured DNIS map. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XB | This command was introduced on the Cisco AS5300, Cisco AS5350, and Cisco AS5400. |
| 12.2(11)T | This command was implemented on the Cisco 3640 and Cisco 3660. |

| Note | For a DNIS map to be applied to an outbound dial peer, the call application must be configured as an outbound application.
                                          That is, a VoiceXML application must be configured by with the application out-bound command. Otherwise, the call is not handed off to the application that is specified in the URL of the DNIS map. |
|---|---|

| Command | Description |
|---|---|
| dnis | Adds a DNIS number to a DNIS map. |
| show voice dnis - map | Displays configuration information about DNIS maps. |
| voice dnis - map | Enters DNIS-map configuration mode to create a DNIS map. |
| voice dnis - map load | Reloads a DNIS map that has changed since the previous load. |

| Release | Modification |
|---|---|
| 15.3(1)T | This
                                       					 command was introduced. |
| 15.6(2)T
                                       					 and IOS XE Denali 16.3.1 | This
                                       					 command was modified to include the keyword: system . This
                                       					 command is now available under voice class tenants. |

| id | Domain name that is reported in service relationships. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| access - policy | Requires that a neighbor be explicitly configured. |

| keypad-character | Character string of one to four characters that can be dialed on a telephone keypad (0-9, *, #). Default is #4. |
|---|---|

| Release | Modification |
|---|---|
| 15.0(1)M | This command was introduced. |

| Note | This command does not change the user experience for Drop Last Conferee if the Cisco call-control system is Cisco Unified
                                          Communications Manager. |
|---|---|

| Command | Description |
|---|---|
| conference | Defines FAC in Feature Mode to initiate a three-party conference. |
| hangup-last-active-call | Defines FAC in feature mode to drop last active call during a three-party conferencee. |
| toggle-between-two-calls | Defines FAC in feature mode to toggle between two active calls. |
| transfer | Defines FAC in feature mode to connect a call to a third party that the phone user dials. |

| ds0 - time - slot | DS0 time slots to be forced into the busyout state. Range is from 1 to 24 and can include any combination of time slots. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(7)XK | This command was introduced on the Cisco MC3810 and Cisco 2600 series and the Cisco 3600 series. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |

| Command | Description |
|---|---|
| busyout seize | Changes the busyout seize procedure for a voice port. |
| show running configuration | Displays the contents of the currently running configuration file or the configuration for a specific class map, interface,
                                          map class, policy map, or virtual circuit (VC) class. |

| ds0 - group - number | A value that identifies the DS0 group. Range is from 0 to
                                          						14 and 16 to 30; 15 is reserved. |
|---|---|
| timeslots timeslot - list | Lists time slots in the DS0 group. The timeslot-list argument is a single
                                          						time-slot number, a single range of numbers, or multiple ranges of numbers
                                          						separated by commas. Range is from 1 through 31. Examples are as follows: 2 1-15,17-24 1-23 2,4,6-12 |
| type | Specifies the type of signaling for the DS0 group. The
                                          						signaling method selection for the type keyword depends on the connection that
                                          						you are making. The ear and mouth (E&M) interface allows connection for PBX
                                          						trunk lines (tie lines) and telephone equipment. The Foreign Exchange Station
                                          						(FXS) interface allows connection of basic telephone equipment and a PBX. The
                                          						Foreign Exchange Office (FXO) interface is for connecting the central office
                                          						(CO) to a standard PBX interface where permitted by local regulations; it is
                                          						often used for off-premise extensions (OPXs). Types are as follows: e&m - delay - dial --The
                                                						  originating endpoint sends an off-hook signal and then waits for an off-hook
                                                						  signal followed by an on-hook signal from the destination. e&m-fgb--E&M Type II Feature Group B. e&m-fgd--E&M Type II Feature Group D. e&m - immediate - start --E&M
                                                						  immediate start. e&m-lmr --E&M
                                                						  Land Mobile Radio (LMR). e&m - melcas - delay --E&M
                                                						  MELCAS delay-start signaling support. e&m - melcas - immed --E&M
                                                						  MELCAS immediate-start signaling support. |
|  | e&m - melcas - wink --E&M MELCAS wink-start signaling support. e&m - wink - start --The originating endpoint sends an off-hook signal and waits for a wink-start from the destination. fgd - eana -- Feature Group D exchange access North American. fgd-os--Feature Group D operator services. fxo - ground - start -- FXO ground-start signaling. fxo - loop - start -- FXO loop-start signaling. fxo - melcas -- FXO MELCAS signaling. fxs - ground - start -- FXS ground-start signaling. fxs - loop - start -- FXS loop-start signaling. fxs - melcas -- FXS MELCAS signaling. none --Null signaling for external call control. p7--Specifies the p7 switch type. r1-itu--Line signaling based on international signaling standards. r1-modified--An international signaling standard that is common to channelized T1/E1 networks. r1 - turkey --A signaling standard used in Turkey. r2 - analog -- R2 analog line signaling. r2 - digital -- R2 digital line signaling. r2-lsv181-digital--Specifies a specific R2 digital line. r2 - pulse -- 7-pulse line signaling, a transmitted pulse that indicates a change in the line state. sas-ground-start -- Single attachment station (SAS) ground-start. sas-loop-start -- SAS loop-start. |
| service service - type | (Optional) Specifies the type of service data --data
                                                						  service fax --
                                                						  store-and-forward fax service voice --voice
                                                						  service (for FGD-OS service) mgcp --Media
                                                						  Gateway Control Protocol (MGCP) service |

| Release | Modification |
|---|---|
| 11.2 | This command was introduced for the Cisco AS5300 as the cas - group command. |
| 11.3(1)MA | The command was introduced as the voice-group command for
                                          						the Cisco MC3810. |
| 12.0(1)T | This command was integrated into Cisco IOS Release
                                          						12.0(1)T, and the cas-group command was implemented on the Cisco 3600 series
                                          						routers. |
| 12.0(5)T | The command was renamed ds0-group on the Cisco AS5300 and
                                          						Cisco 2600 series and Cisco 3600 series routers. Some keyword modifications
                                          						were implemented. |
| 12.0(5)XE | This command was implemented on the Cisco 7200 series. |
| 12.0(7)XK | Support for this command was implemented on the Cisco MC3810. When the ds0-group command became available on the Cisco MC3810,
                                          the voice-group command was removed and no longer supported. |
| 12.0(7)XR | The mgcp service type was added. |
| 12.1(2)XH | The e&m-fgd and fgd-eana keywords were added for
                                          						Feature Group D signaling. |
| 12.1(5)XM | The sgcp keyword was removed. |
| 12.1(3)T | This command was modified for Cisco 7500 series routers.
                                          						The fgd-os signaling type and the voice service type were added. |
| 12.2 | The command was modified to exclude sas keywords. The
                                          						Single Attachment Station (SAS) CAS options of sas-loop-start and
                                          						sas-ground-start are not supported as a type of signaling for the DS0 group. |
| 12.2(2)XA | This command was implemented on the Cisco AS5300. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T
                                          						and implemented on the Cisco 7200 series. |
| 12.2(4)T | Support for the Cisco AS5300, Cisco AS5350, and Cisco
                                          						AS5400 is not included in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)XM | This command was implemented on Cisco 1750 and Cisco 1751
                                          						routers. Support for other Cisco platforms is not included in this release. |
| 12.2(2)XN | Support for the mgcp keyword was added to Cisco
                                          						CallManager Version 3.1 for the Cisco 2600 series, Cisco 3600 series, and Cisco
                                          						VG200. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 7200 series. Support for the Cisco AS5300, Cisco
                                          						AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command was supported with Cisco IOS Release 12.2(11)T
                                          						and Cisco CallManager Version 3.2. This command is supported on the Cisco
                                          						IAD2420 series, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5850 in this
                                          						release. |
| 12.2(13)T | This command was integrated into Cisco IOS Release
                                          						12.2(13)T. The Cisco 1750 and Cisco 1751 do not support T1 and E1 voice and
                                          						data cards in Cisco IOS Release 12.2(13)T. The Cisco 17xx platforms can support
                                          						only HC DSP firmware images in this release. |
| 12.3(8)T | Documentation of the ds0-group command was divided into
                                          						the individual ds0-group (E1) and ds0-group (T1) commands. |
| 12.4(2)T1 | Support was added for the e&m-lmr signaling type on the
                                          						Cisco 2691, Cisco 2600XM series, Cisco 2800 series (except Cisco 2801), Cisco
                                          						3660, Cisco 3700 series, and Cisco 3800 series. |

| Note | This command does not support the extended echo canceller (EC)
                                          		  feature on the Cisco AS5x00 series. |
|---|---|

| Command | Description |
|---|---|
| cas-group | Configures channelized T1 time slots with robbed bit
                                          						signaling. |
| codec | Specifies the voice coder rate of speech for a dial peer. |
| codec complexity | Specifies call density and codec complexity based on the
                                          						codec standard that you are using. |

| ds0 - group - number | A value that identifies the DS0 group. Range is from 0 to 23. |
|---|---|
| timeslots timeslot-list | Lists time slots in the DS0 group. The timeslot-list argument is a single time-slot number, a single range of numbers, or multiple ranges of numbers separated by commas. Range
                                          is from 1 to 24. Examples are as follows: 2 1-15,17-24 1-23 2,4,6-12 |
| typenone | Specifies the type of signaling for the DS0 group. The signaling method selection for the type keyword depends on the connection
                                          that you are making. The ear and mouth (E&M) interface allows connection for PBX trunk lines (tie lines) and telephone equipment.
                                          The Foreign Exchange Station (FXS) interface allows connection of basic telephone equipment and a PBX interface. The Foreign
                                          Exchange Office (FXO) interface is for connecting the central office (CO) to a standard PBX interface where permitted by local
                                          regulations; it is often used for off-premise extensions (OPXs). Types are as follows: e&m-delay-dial --The originating endpoint sends an off-hook signal and then waits for an off-hook signal followed by an on-hook signal from
                                                the destination. e&m-fgb --E&M Type II Feature Group B. e&m-fgd --E&M Type II Feature Group D. e&m-immediate-start --E&M immediate start. e&m-lmr --E&M Land Mobile Radio (LMR). e&m-wink-start --The originating endpoint sends an off-hook signal and waits for a wink-start from the destination. ext-sig --The external signaling interface specifies that the signaling traffic comes from an outside source. fgd-eana -- Feature Group D exchange access North American. fgd-emf-- FGD Enhanced MF. fgd-os --Feature Group D operator services. fxo-ground-start -- FXO ground-start signaling. fxo-loop-start -- FXO loop-start signaling. fxs-ground-start -- FXS ground-start signaling. fxs-loop-start -- FXS loop-start signaling. none --Null signaling for external call control. r1-itu --Line signaling based on international signaling standards. (This signaling type is not supported on the Cisco AS5300, Cisco
                                                AS5350, and Cisco AS5400 platforms.) r1-modified --An international signaling standard that is common to channelized T1/E1 networks. |
|  | r1-turkey --A signaling standard used in Turkey. sas-ground-start --Single attachment station (SAS) ground-start. sas-loop-start --SAS loop-start. |
| service service - type | (Optional) Specifies the type of service: data --Data service. fax -- Store-and-forward fax service. mgcp --Media Gateway Control Protocol (MGCP) service. Used only with the type none keywords on the Cisco AS5x00 platforms. sccp --Simple Gateway Control Protocol (SCCP) service. voice --Voice service (for FGD-OS service). |
| dtmf | (Optional) Specifies dual tone multifrequency (DTMF) tone signaling. |
| mf | (Optional) Specifies multifrequency (MF) tone signaling |
| ani | (Optional) Provisions ANI address information. |
| ani-dnis | (Optional) Specifies automatic number identification (ANI) and dialed number identification service (DNIS) address information
                                          provisioning for FGD OS. |
| ani-pani | (Optional) Provisions ANI and PANI address information. |
| dnis-ani | (Optional) Specifies ANI and DNIS address information provisioning for FGD EANA. |
| dnis | (Optional) Specifies DNIS address information provisioning. |
| info-digits-no-strip | (Optional) Retains information digits on the Cisco AS5x00 platforms. |

| Release | Modification |
|---|---|
| 11.2 | This command was introduced for the Cisco AS5300 as the cas-group command. |
| 11.3(1)MA | The command was introduced as the voice-group command for the Cisco MC3810. |
| 12.0(1)T | This command was integrated into Cisco IOS Release 12.0(1)T, and the cas-group command was implemented on the Cisco 3600 series routers. |
| 12.0(5)T | The command was renamed ds0-group on the Cisco AS5300 and Cisco 2600 series and Cisco 3600 series routers. Some keyword modifications were implemented. |
| 12.0(5)XE | This command was implemented on the Cisco 7200 series. |
| 12.0(7)XK | Support for this command was implemented on the Cisco MC3810. When the ds0-group command became available on the Cisco MC3810, the voice-group command was removed and no longer supported. The ext-sig keyword replaced the ext-sig-master and ext-sig-slave keywords that were available with the voice-group command. |
| 12.0(7)XR | The mgcp service type was added. |
| 12.1(2)XH | The e&m-fgd and fgd-eana keywords were added for Feature Group D signaling. |
| 12.1(5)XM | The sgcp keyword was removed. |
| 12.1(3)T | This command was modified for Cisco 7500 series routers. The fgd-os signaling type and the voice service type were added. |
| 12.2(2)XA | This command was implemented on the Cisco AS5300. |
| 12.2 | The command was modified to exclude sas keywords. The Single Attachment Station (SAS) CAS options of sas-loop-start and sas-ground-start
                                          are not supported as a type of signaling for the DS0 group. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 7200 series. |
| 12.2(4)T | Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is not included in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)XM | This command was implemented on Cisco 1750 and Cisco 1751 routers. Support for other Cisco platforms is not included in this
                                          release. |
| 12.2(2)XN | Support for the mgcp keyword was added to Cisco CallManager Version 3.1 for the Cisco 2600 series, Cisco 3600 series, and Cisco VG200. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 7200 series. Support for the Cisco
                                          AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command was supported in Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2. This command is supported on
                                          the Cisco IAD2420 series, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5850 in this release. |
| 12.2(13)T | This command was integrated into Cisco IOS Release 12.2(13)T. The Cisco 1750 and Cisco 1751 do not support T1 and E1 voice
                                          and data cards in Cisco IOS Release 12.2(13)T. The Cisco 17xx platforms can support only HC DSP firmware images in this release. |
| 12.2(15)T | This command was implemented on the Cisco 2600XM, Cisco 3725, and Cisco 3745. |
| 12.3(4)XD | This command was modified for the Cisco 3725 and Cisco 3745. The e&m-lmr signaling type was added. |
| 12.3(7)T | This command was integrated into Cisco IOS Release 12.3(7)T. |
| 12.3(8)T | Documentation of the ds0-group command was divided into the individual ds0-group (E1) and ds0-group (T1) commands. |
| 12.3(10) | The info-digits-no-strip keyword was added for use on the Cisco AS5x00 platforms. |
| 12.4(9)T | This command was integrated into Cisco IOS Release 12.4(9)T. The fgd-emf , ani-pani , and ani keywords were added for the Cisco 2800 and Cisco AS5x00 platforms. |

| Note | This command does not support the extended echo canceller (EC) feature on the Cisco AS5x00 series. |
|---|---|

| Note | The signaling type R1-ITU is not supported on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 platforms. |
|---|---|

| Command | Description |
|---|---|
| cas-group | Configures channelized T1 time slots with robbed bit signaling. |
| codec | Specifies the voice coder rate of speech for a dial peer. |
| codec complexity | Specifies call density and codec complexity based on the codec standard that you are using. |

| Release | Modification |
|---|---|
| 12.3(7)T | This command was introduced. |

| Command | Description |
|---|---|
| sip | Enables SIP voice service configuration commands. |
| voice service voip | Specifies the voice encapsulation type as VoIP. |

| audio | Applies DSCP to audio payload packets. |
|---|---|
| video | Applies DSCP to video payload packets. |
| flah-override-override | Applies flash-override-override RPH priority. |
| flash-override | Applies flash-override RPH priority. |
| flsh | Applies flash RPH priority. |
| immediate | Applies immediate RPH priority. |
| priority | Applies priority RPH priority. |
| routine | Applies routine RPH priority. |
| dscp-value | DSCP value. Valid values are from 0 to 63. |
| set-af | An assured forwarding bit pattern as the DSCP value: af11 —bit pattern 001010 af12 —bit pattern 001100 af13 —bit pattern 001110 af21 —bit pattern 010010 af22 —bit pattern 010100 af23 —bit pattern 010110 af31 —bit pattern 011010 af32 —bit pattern 011100 af33 —bit pattern 011110 af41 —bit pattern 100010 af42 —bit pattern 100100 af43 —bit pattern 100110 |
| set-cs | Class-selector code point as the DSCP value: cs1 —code point 1 (precedence 1) cs2 —code point 2 (precedence 2) cs3 —code point 3 (precedence 3) cs4 —code point 4 (precedence 4) cs5 —code point 5 (precedence 5) cs6 —code point 6 (precedence 6) cs7 —code point 7 (precedence 7) |
| ef | Specifies the expedited forwarding bit pattern 101110 as the DSCP value. |
| zero | Specifies the default bit pattern 000000 as the DSCP value. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Granular Service Class | Priority or Precedence | DSCP Base10 Value | DSCP Binary Value |
|---|---|---|---|
| Voice | Audio Call | 46 | 101110 |
| Flash | 43 | 101011 |
| Flash Override | 41 | 101001 |
| Flash Override Override | 40 | 101000 |
| Immediate | 45 | 101101 |
| Priority | 47 | 101111 |
| Routine | 49 | 110001 |
| Video | Flash Override | 33 | 100001 |
| Flash | 35 | 100011 |
| Flash Override Override | 32 | 100000 |
| Immediate | 37 | 100101 |
| Priority | 39 | 100111 |
| Routine | 51 | 110011 |
| Video Call | 34 | 100111 |

| Command | Description syslog |
|---|---|
| violation | Specifies the action that needs to be performed on any violation in the DSCP policy. |

| tag | DSCP
                                          						profile tag. The range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(2)T | This
                                          						command was introduced. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command is now available under voice class tenants. |

| Command | Description |
|---|---|
| dscp
                                             						  media | Specifies
                                          						the RPH to DSCP mapping. |
| voice service voip | Enters
                                          						voice service configuration mode. |
| sip | Enters
                                          						service SIP configuration mode. |

| delay | Defines the delay for each mailer. |
|---|---|
| failure | Requests that a failed message be sent to the FROM address. This is the default. |
| success | Requests that a message be sent to the FROM address saying that the mail message was delivered successfully to the recipient. |

| Release | Modification |
|---|---|
| 12.0(4)XJ | This command was introduced. |
| 12.1(1)T | This command was integrated into Cisco IOS Release 12.1(1)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the Cisco 1751, Cisco 2600 series and Cisco 3600 series, Cisco 3725, and Cisco 3745. |

| Note | In the absence of any other DSN settings (for example, no dsn, or a mailer in the path that does not support the DSN extension),
                                          a failure to deliver message always causes a nondelivery message to be generated. This nondelivery message is called a bounce. |
|---|---|

| Note | DSNs are generated only if the mail client on the SMTP server is capable of responding to a DSN request. |
|---|---|

| Command | Description |
|---|---|
| mta send mail - from hostname | Specifies the originator (host-name portion) of the e-mail fax message. |
| mta send mail - from username | Specifies the originator (username portion) of the e-mail fax message. |

| Release | Modification |
|---|---|
| 12.4(15)T9 | This command was introduced. |

| Command | Description |
|---|---|
| show voice dsp | Displays the current status or selective statistics of DSP voice channels. |
| voice-card | Enters voice-card configuration mode. |

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced. |
| Cisco IOS XE
                                          Release 3.2S | Support for this command was added on Cisco ASR 1000 Series Routers. |

| Note | Use this command before enabling DSP-farm services with the dspfarm command for an NM-HDV or NM-HDV-FARM. |
|---|---|

| Command | Description |
|---|---|
| dsp services dspfarm | Enables the DSP farm services. |
| dspfarm profile | Enters the DSP farm profile configuration mode, and defines a profile for the DSP farm services. |
| show voice dsp (SPA-DSP) | Displays the DSP current status or the selective statistics of the DSP voice channels. |

| Release | Modification |
|---|---|
| 12.1(5)YH | This command was introduced on the Cisco VG200. |
| 12.2(13)T | This command was implemented on the Cisco 2600 series, Cisco 3620, Cisco 3640, Cisco 3660, and Cisco 3700 series. |

| Command | Description |
|---|---|
| dsp services dspfarm | Specifies the NM-HDV or NM-HDV-FARM on which DSP-farm services are to be enabled. |
| dspfarm transcoder maximum sessions | Specifies the maximum number of transcoding sessions to be supported by a DSP farm. |
| show dspfarm | Displays summary information about DSP resources. |

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced on the Cisco 3660. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(2)XB | This command was implemented on the Cisco 2600 series routers. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T. |
| 12.2(15)T | This command was implemented on the Cisco 2600XM, Cisco 3725, and Cisco 3745. |

| Command | Description |
|---|---|
| ds0-group | Specifies the DS0 time slots that make up a logical voice port on a T1 or E1 controller, Specifies the signaling type by
                                          which the router communicates with the PBX or PSTN, Defines T1or E1 channels for compressed voice calls and the CAS method
                                          by which the router connects to the PBX or PSTN. |
| pri-group | Specifies ISDN PRI on a channelized T1 or E1 controller. |
| voice-card | Enters voice-card configuration mode. |

| mixed-mode | Specifies the maximum number of transcoding sessions for mixed-mode conferencing. |
|---|---|
| sessions | Specifies the conferencing maximum sessions parameter value. |
| number | Number of conference sessions. A single DSP supports one conference session with up to six participants. |

| Release | Modification |
|---|---|
| 12.1(5)YH | This command was introduced on the Cisco VG200. |
| 12.2(13)T | This command was modified. This command was implemented on the Cisco 2600 series, Cisco 3620, Cisco 3640, Cisco 3660, and
                                          Cisco 3700 series. |
| 15.0(1)M | This command was modified. The mixed-mode keyword was added. |

| Command | Description |
|---|---|
| dspfarm (DSP farm) | Enables DSP-farm service. |
| dspfarm transcoder maximum sessions | Specifies the maximum number of transcoding sessions to be supported by a DSP farm. |
| show dspfarm | Displays summary information about DSP resources. |

| seconds | Interval, in seconds, during which to monitor RTP inactivity. Range is from 60 to 10800. Default is 600. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(5)YH | This command was introduced on the Cisco VG200. |
| 12.2(13)T | This command was implemented on the Cisco 2600 series, Cisco 3620, Cisco 3640, Cisco 3660, and Cisco 3700 series. |

| Command | Description |
|---|---|
| dspfarm rtp timeout | Specifies the RTP timeout interval used to clear hanging connections. |

| profile identifier | Number that uniquely identifies a profile. Range is 1 to 65535. There is no default. |
|---|---|
| conference | Enables a profile for conferencing. |
| mtp | Enables a profile for Media Termination Point (MTP). |
| transcode | Enables a profile for transcoding. |
| security | Enables a profile for secure DSP farm services. |
| video | (Optional) Enables a profile for video conferencing or transcoding. |
| homogeneous | (Optional) Specifies that all video participants use the one video format that is configured in this profile. DSP resources
                                          are reserved to support the conference at configuration time. Note The homogeneous profiles only support one video codec. | Note | The homogeneous profiles only support one video codec. |
| Note | The homogeneous profiles only support one video codec. |
| heterogeneous | (Optional) Specifies that video participants can use the different video formats that are configured in the profile. You can
                                          configure up to 10 video codecs in the heterogeneous profile. DSP resources are reserved to support the different configurations
                                          at configuration time. |
| guaranteed-audio | (Optional) Specifies that video participants in a heterogeneous conference will at least have an audio connection. You can
                                          configure up to 10 video codecs in the guaranteed-audio profile. The DSP resources for audio streams are reserved at configuration
                                          time, but DSP resources to support video conferences are not reserved. If the video endpoint supports the video format specified
                                          in the profile and DSP resources are available when the participant joins the conference, the participant joins as a video
                                          conferee in the video conference. |

| Note | The homogeneous profiles only support one video codec. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.4(11)XW | The security keyword was added. |
| 12.4(20)T | This command was integrated into Cisco IOS Release 12.4(20)T. |
| 12.4(22)T | Support for IPv6 was added. |
| 15.0(1)M2
                                          15.1(1)T | Support was modified for the Cisco IAD 2430, IAD 2431, IAD 2432, and IAD  2435, and the Cisco VG 202, VG 204, and VG 224 platforms. |
| Cisco IOS XE 
                                          Release 3.2S | This command was modified. Support was added to the Cisco ASR 1000 Series Router. The conference , mtp & security keywords are not supported on the Cisco ASR 1000 Series Router in this release. |
| 15.1(4)M | This command was modified. The video keyword was added. |
| Cisco IOS XE 
                                          Release 3.2S | This command was integrated into Cisco IOS XE Release 3.3S. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Note | The secure DSP farm services is always enabled for SPA-DSP on Cisco ASR 1000 Series Router. Only transcode keyword is supported on Cisco ASR 1000 Series Router for Cisco IOS XE Release 3.2s. The conference , media , and security keywords are not supported on Cisco ASR 1000 Series Router for Cisco IOS XE Release 3.2s. |
|---|---|

| Command | Description |
|---|---|
| dsp service dspfarm | Configures the DSP farm services for a specified voice card. |
| shutdown (DSP farm profile) | Disables the DSP farm profile. |
| voice-card | Enters voice card configuration mode |
| voice-service dsp-reservation | Configures the percentage of DSP resources are reserved for voice services and enables video services to use the remaining
                                          DSP resources. |

| seconds | RTP timeout interval, in seconds. Range is from 10 to 7200. Default is 1200. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(5)YH | This command was introduced on the Cisco VG200. |
| 12.2(13)T | This command was implemented on the Cisco 2600 series, Cisco 3620, Cisco 3640, Cisco 3660, and Cisco 3700 series. |

| Command | Description |
|---|---|
| dspfarm (DSP farm) | Enables DSP-farm service. |
| dspfarm connection interval | Specifies the time interval during which to monitor RTP inactivity before deleting an RTP stream. |
| show dspfarm | Displays summary information about DSP resources. |

| number | Number of transcoding sessions. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(5)YH | This command was introduced on the Cisco VG200. |
| 12.2(13)T | This command was implemented on the Cisco 2600 series, Cisco 3620, Cisco 3640, Cisco 3660, and Cisco 3700 series. |

| Command | Description |
|---|---|
| dspfarm (DSP farm) | Enables DSP-farm service. |
| dspfarm confbridge maximum sessions | Specifies the maximum number of conferencing sessions to be supported by a DSP farm. |
| dsp services dspfarm | Specifies the NM-HDV or NM-HDV-FARM on which DSP-farm services are to be enabled. |
| show dspfarm | Displays summary information about DSP resources. |

| slot | Slot number of the interface. |
|---|---|
| port | Port number of the interface. |

| Release | Modification |
|---|---|
| 12.0(5)XE | This command was introduced on the Cisco 7200 series
                                          						routers. |
| 12.1(1)T | This command was integrated into Cisco IOS Release
                                          						12.1(1)T. |
| 12.2(13)T | This command was implemented on the Cisco 7200 series. |

| Command | Description |
|---|---|
| ds0-group | Specifies the DS0 time slots that make up a logical voice
                                          						port on a T1 or E1 controller. |
| no shutdown | Disables the interface. |
| pri-group | Specifies an ISDN PRI on a channelized T1 or E1 controller |
| show interfaces dspfarm dsp | Displays information about the DSP interface. |
| voice-card | Enters voice-card configuration mode. |

| rtp-nte | Enables a delay between the dtmf-digit begin and dtmf-digit end events of RTP NTE packets. |
|---|---|
| standard | Generates RTP NTE packets that are RFC 4733 compliant. |
| system | Specifies the default global dual tone multifrequency (DTMF) interworking configuration. This keyword is available only in
                                          dial peer voice configuration mode. |

| Release | Modification |
|---|---|
| 12.4(15)XZ | This command was introduced. |
| 12.4(20)T | This command was integrated into Cisco IOS Release 12.4(20)T. |
| 15.1(2)T5 | This command was modified. The standard and system keywords were added. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| keypad-normalize | Ensures that the delay configured for a dtmf-end event is always honored. |
| nte-end-digit-delay | Specifies the length of delay for each digit in a dtmf-digit end event. |

| milliseconds | DTMF interdigit timer duration, in milliseconds. Range is from 250 to 3000. The default is 3000. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco AS5300. |

| Command | Description |
|---|---|
| cas-custom | Customizes E1 R2 signaling parameters for a particular E1 channel group on a channelized E1 line. |
| ds0-group | Configures channelized T1 time slots, which enables a Cisco AS5300 modem to answer and send an analog call. |

| Release | Modification |
|---|---|
| 12.0(3)XG | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.0(4)T | This command was integrated into Cisco IOS Release 12.0(4)T, and implemented on the Cisco 7200 series router. |

| Command | Description |
|---|---|
| called-number (dial peer) | Enables an incoming VoFR call leg to get bridged to the correct POTS call leg when using a static FRF.11 trunk connection. |
| codec (dial peer) | Specifies the voice coder rate of speech for a VoFR dial peer. |
| connection | Specifies a connection mode for a voice port. |
| cptone | Specifies a regional analog voice interface-related tone, ring, and cadence setting. |
| destination-pattern | Specifies the prefix, the full E.164 telephone number, or an ISDN directory number (depending on the dial plan) to be used
                                          for a dial peer. |
| preference | Indicates the preferred order of a dial peer within a rotary hunt group. |
| session protocol | Establishes a session protocol for calls between the local and remote routers via the packet network. |
| session target | Specifies a network-specific address for a specified dial peer or destination gatekeeper. |
| signal-type | Sets the signaling type to be used when connecting to a dial peer. |

| cisco - rtp | Forwards DTMF tones by using Real-Time Transport Protocol (RTP) with a Cisco proprietary payload type. |
|---|---|
| h245 - alphanumeric | Forwards DTMF tones by using the H.245 "alphanumeric" User Input Indication method. Supports tones from 0 to 9, *, #, and
                                          from A to D. |
| h245 - signal | Forwards DTMF tones by using the H.245 "signal" User Input Indication method. Supports tones from 0 to 9, *, #, and from A
                                          to D. |
| rtp - nte | Forwards DTMF tones by using RTP with the Named Telephone Event (NTE) payload type. |
| digit-drop | Passes digits out-of-band and drops in-band digits. Note The digit-drop keyword is only available when the rtp - nte keyword is configured. | Note | The digit-drop keyword is only available when the rtp - nte keyword is configured. |
| Note | The digit-drop keyword is only available when the rtp - nte keyword is configured. |
| sip-info | Forwards DTMF tones using SIP INFO messages. This keyword is available only if the VoIP dial peer is configured for SIP. |
| sip-kpml | Forwards DTMF tones using SIP KPML over SIP SUBSCRIBE/NOTIFY messages. This keyword is available only if the VoIP dial peer
                                          is configured for SIP. |
| sip-notify | Forwards DTMF tones using SIP NOTIFY messages. This keyword is available only if the VoIP dial peer is configured for SIP. |

| Note | The digit-drop keyword is only available when the rtp - nte keyword is configured. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced on the Cisco AS5300. |
| 12.0(2)XH | The cisco - rtp , h245 - alphanumeric , and h245 - signal keywords were added. |
| 12.0(5)T | This command was integrated into Cisco IOS Release 12.0(5)T. |
| 12.0(7)XK | This command was first supported for VoIP on the MC3810. |
| 12.1(2)T | Changes made in Cisco IOS Release 12.0(7)XK were integrated into Cisco IOS Release 12.1(2)T. |
| 12.2(8)T | This command was implemented on the Cisco 1751, Cisco 2600 series and Cisco 3600 series, Cisco 3725, and Cisco 3745. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          was not included in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850 platform. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |
| 12.2(15)ZJ | The sip-notify keyword was added. |
| 12.3(4)T | This command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.3(11)T | The digit - drop keyword was added. |
| 15.3(3)M | This command was modified. The sip-info and sip-kpml keywords were added. |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Note | The cisco - rtp keyword supports a proprietary Cisco implementation and operates only between two Cisco 2600 series or Cisco 3600 series
                                          routers running Cisco IOS Release 12.0(2)XH or later. Otherwise, the DTMF relay feature does not function, and the gateway
                                          sends DTMF tones in-band. |
|---|---|

| Command | Description |
|---|---|
| notify telephone-event | Configures the maximum interval between two consecutive NOTIFY messages for a particular telephone event. |

| busy | Configure busy tone. |
|---|---|
| conference | Configure conference join and leave tones. |
| disconnect | Configure disconnect tone. |
| number - unobtainable | Configure number-unavailable tone. |
| out - of - service | Configure out-of-service tone. |
| reorder | Configure reorder tone. |
| ringback | Configure ringback tone. |

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced on the Cisco 2600 and Cisco 3600 series and on the Cisco MC3810. |
| 12.2(2)T | This command was implemented on the Cisco 1750 router and integrated into Cisco IOS Release 12.2(2)T. |
| 12.4(11)XJ2 | The conference keyword was added. |
| 12.4(15)T | This command was integrated into Cisco IOS Release 12.4(15)T. |

| Command | Description |
|---|---|
| cadence | Defines the tone on and off durations for a call-progress tone. |
| conference-join custom-cptone | Defines a custom call-progress tone to indicate joining a conference. |
| conference-leave custom-cptone | Defines a custom call-progress tone to indicate leaving a conference. |
| dspfarm profile | Enters DSP farm profile configuration mode and defines a profile for DSP farm services. |
| frequency | Defines the frequency components for a call-progress tone. |
| supervisory custom-cptone | Associates a class of custom call-progress tones with a voice port. |
| voice class custom-cptone | Creates a voice class for defining custom call-progress tones. |