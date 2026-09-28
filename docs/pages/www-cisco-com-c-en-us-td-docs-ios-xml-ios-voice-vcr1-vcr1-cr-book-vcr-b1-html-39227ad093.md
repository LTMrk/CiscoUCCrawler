---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr1-vcr1-cr-book-vcr-b1-html-39227ad093
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr1/vcr1-cr-book/vcr-b1.html
retrieved_at: 2026-08-16T23:15:13.784292+00:00
---

Cisco IOS Voice Command Reference - A through C

# Cisco IOS Voice Command Reference - A through C

Updated: April 25, 2026

Chapter: B

## Chapter: B

# B

## backhaul-session-manager

To enter backhaul session manager configuration mode, use the backhaul-session-manager command in global configuration mode.

backhaul-session-manager

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(1)T

This command was introduced.

12.2(2)T

This command was implemented on the Cisco 7200.

12.2(4)T

This command was implemented on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)XB

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850 platform.

12.2(8)T

This command was implemented on Cisco IAD2420. Support for the Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included
                                          in this release.

12.2(11)T

This command is supported on the Cisco AS5350, Cisco AS5400, and Cisco AS5850 in this release.

### Usage Guidelines

Use the backhaul-session-manager command to switch to backhaul session manager configuration mode from global configuration mode. Use the exit command to exit backhaul session manager configuration mode and return to global configuration mode.

## Examples

The following example enters backhaul session manager configuration mode:

```
Router(config)# backhaul-session-manager Router(config-bsm)#
```

### Related Commands

Command

Description

clear backhaul-session-manager group

Resets the statistics or traffic counters for a specified session group.

clear rudpv1 statistics

Clears the RUDP statistics and failure counters.

group

Creates a session group and associates it with a specified session set.

group auto-reset

Configures the maximum auto-reset value.

group cumulative-ack

Configures maximum cumulative acknowledgments.

group out-of-sequence

Configures maximum out-of-sequence segments that are received before an EACK is sent.

group receive

Configures maximum receive segments.

group retransmit

Configures maximum retransmits.

group timer cumulative-ack

Configures cumulative acknowledgment timeout.

group timer keepalive

Configures keepalive (or null segment) timeout.

group timer retransmit

Configures retransmission timeout.

group timer transfer

Configures state transfer timeout.

isdn bind-l3

Configures the ISDN serial interface for backhaul.

session group

Associates a transport session with a specified session group.

set

Creates a fault-tolerant or non-fault-tolerant session set with the client or server option.

show backhaul-session-manager group

Displays status, statistics, or configuration of a specified or all session groups.

show backhaul-session-manager session

Displays status, statistics, or configuration of sessions.

show backhaul-session-manager set

Displays session groups associated with a specific or all session sets.

show rudpv1

Displays RUDP statistics.

## bandwidth (dial peer)

To set the maximum bandwidth on a POTS dial peer for an H.320 call, use the bandwidth command in dial peer configuration mode. To remove the bandwidth setting, use the no form of this command.

bandwidth maximum value [ maximum value ]

no bandwidth

### Syntax Description

maximum value

Sets the maximum bandwidth for an H.320 call on a POTS dial peer. The range is 64 to 1024, entered in increments of 64 kilobits
                                          per second (kbps). The default is 64.

minimum value

(Optional) Sets the minimum bandwidth. Acceptable values are 64 kbps or minimum value = maximum value .

### Command Default

No maximum bandwidth is set.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.4(11)T

This command was introduced.

### Usage Guidelines

Use this command to set the maximum and minimum bandwidth for an H.320 POTS dial-peer. Only the maximum bandwidth is required.
                              The value must be entered in increments of 64 kbps. The minimum bandwidth setting is optional, and the value must be either
                              64 kbps or equal to the maximum value setting.

## Examples

The following example shows configuration for POTS dial peer 200 with a maximum bandwidth of 1024 kbps:

```
dial-peer voice 200 pots
 bandwidth maximum 1024
```

The following example shows configuration for POTS dial peer 11 with a maximum bandwidth of 640 and a minimum of 64:

```
dial-peer voice 11 pots
 bandwidth maximum 640 minimum 64
```

### Related Commands

Command

Description

bandwidth

Specifies the maximum aggregate bandwidth for H.323 traffic and verifies the available bandwidth of the destination gatekeeper.

## bandwidth

To specify the maximum aggregate bandwidth for H.323 traffic and verify the available bandwidth of the destination gatekeeper,
                              use the bandwidth command in gatekeeper configuration mode. To disable maximum aggregate bandwidth, use the no form of this command.

bandwidth { interzone | total | session } { default | zone zone-name } bandwidth-size

no bandwidth { interzone | total | session } { default | zone zone-name }

### Syntax Description

interzone

Total amount of bandwidth for H.323 traffic from the zone to any other zone.

total

Total amount of bandwidth for H.323 traffic allowed in the zone.

session

Maximum bandwidth allowed for a session in the zone.

default

Default value for all zones.

zone

A particular zone.

zone-name

Name of the particular zone.

bandwidth-size

Maximum bandwidth, in kbps. For interzone and total , range : 1 to 10000000. For session , range:1 to 5000.

### Command Default

Maximum aggregate bandwidth is unlimited by default.

### Command Modes

Gatekeeper configuration (config-gk)

## Command History

Release

Modification

11.3(2)NA

This command was introduced on the Cisco 2500, Cisco 3600 series and the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T. The bandwidth command replaced the zone bw command.

12.1(5)XM

The bandwidth command was recognized without using the zone gatekeeper command.

12.2(2)T

The changes in Cisco IOS Release 12.1(5)XM were integrated into Cisco IOS Release 12.2(2)T.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

### Usage Guidelines

This command, in conjunction with the bandwidth remote command, replaces the zone gatekeeper command.

To specify maximum bandwidth for traffic between one zone and any other zone, use the default keyword with the interzone keyword.

To specify maximum bandwidth for traffic within one zone or for traffic between that zone and another zone (interzone or intrazone),
                              use the default keyword with the total keyword.

To specify maximum bandwidth for a single session within a specific zone, use the zone keyword with the session keyword.

To specify maximum bandwidth for a single session within any zone, use the default keyword with the session keyword.

## Examples

The following example configures the default maximum bandwidth for traffic between one zone and another zone to 5000 kbps:

```
gatekeeper
 bandwidth interzone default 5000
```

The following example configures the default maximum bandwidth for all zones to 5000 kbps:

```
gatekeeper
 bandwidth total default 5000
```

The following example configures the default maximum bandwidth for a single session within any zone to 2000 kbps:

```
gatekeeper
 bandwidth session default 2000
```

The following example configures the default maximum bandwidth for a single session with a specific zone to 1000 kbps:

```
gatekeeper
 bandwidth session zone example 1000
```

### Related Commands

Command

Description

bandwidth check-destination

Enables the gatekeeper to verify available bandwidth resources at the destination endpoint.

bandwidth remote

Specifies the total bandwidth for H.323 traffic between this gatekeeper and any other gatekeeper.

h323 interface

Defines on which port the proxy listens.

h323 t120

Enables the T.120 capabilities on the router and specifies bypass or proxy mode.

## bandwidth check-destination

To enable the gatekeeper to verify available bandwidth resources at the destination endpoint, use the bandwidth check-destination command in gatekeeper configuration mode. To disable resource verification, use the no form of this command.

bandwidth check-destination

no bandwidth check-destination

### Syntax Description

This command has no arguments or keywords.

### Command Default

Resource verification is disabled by default.

### Command Modes

Gatekeeper configuration (config-gk)

## Command History

Release

Modification

12.3(1)

This command was introduced.

## Examples

The following example activates bandwidth resource verification at the destination:

```
gatekeeper
 bandwidth check-destination
```

### Related Commands

Command

Description

bandwidth

Specifies the maximum aggregate bandwidth for H.323 traffic from a zone to another zone, within a zone, or for a session in
                                          a zone.

bandwidth remote

Specifies the total bandwidth for H.323 traffic between this gatekeeper and any other gatekeeper.

h323 interface

Defines the port on which port the proxy listens.

h323 t120

Enables the T.120 capabilities on your router and specifies bypass or proxy mode.

## bandwidth remote

To specify the total bandwidth for H.323 traffic between this gatekeeper and any other gatekeeper, use the bandwidth remote command in gatekeeper configuration mode. To disable total bandwidth specified, use the no form of this command.

bandwidth remote bandwidth-size

no bandwidth remote

### Syntax Description

bandwidth-size

Maximum bandwidth, in kbps. Range: 1 to 10000000.

### Command Default

Total bandwidth is unlimited by default.

### Command Modes

Gatekeeper configuration (config-gk)

## Command History

Release

Modification

12.1(3)XI

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco 7200 series.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

### Usage Guidelines

This command, with the bandwidth command, replaces the zone gatekeeper command.

## Examples

The following example configures the remote maximum bandwidth to 100,000 kbps:

```
gatekeeper
 bandwidth remote 100000
```

### Related Commands

Command

Description

bandwidth

Specifies the maximum aggregate bandwidth for H.323 traffic from a zone to another zone, within a zone, or for a session in
                                          a zone.

bandwidth check-destination

Enables the gatekeeper to verify available bandwidth resources at the destination endpoint.

h323 interface

Defines which port the proxy listens on.

h323 t120

Enables the T.120 capabilities on your router and specifies bypass or proxy mode.

## battery-reversal

To specify battery polarity reversal on a Foreign Exchange Office (FXO) or Foreign Exchange Station (FXS) port, use the battery-reversal command in voice-port configuration mode. To disable battery reversal, use the no form of this command.

battery-reversal [ answer ]

no battery-reversal [ answer ]

### Syntax Description

answer

(Optional) Configures an FXO port to support answer supervision by detection of battery reversal.

### Command Default

Battery reversal is enabled

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.0(7)XK

This command was introduced on the Cisco 2600 series and Cisco 3600 series and on the Cisco MC3810.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.2(2)T

The answer keyword was added.

### Usage Guidelines

The battery-reversal command applies to FXO and FXS voice ports. On Cisco 2600 and 3600 series routers, only analog voice ports in VIC-2FXO-M1
                              and VIC-2FXO-M2 voice interface cards are able to detect battery reversal; analog voice ports in VIC-2FXO and VIC-2FXO-EU
                              voice interface cards do not detect battery reversal. On digital voice ports, battery reversal is supported only on E1 Mercury
                              Exchange Limited Channel Associated Signaling (MEL CAS); it is not supported in T1 channel associated signaling (CAS) or E1
                              CAS.

FXS ports normally reverse battery upon call connection. If an FXS port is connected to an FXO port that does not support
                              battery reversal detection, you can use the no battery-reversal command on the FXS port to prevent unexpected behavior.

FXO ports in loopstart mode normally disconnect calls when they detect a second battery reversal (back to normal). You can
                              use the no battery-reversal command on FXO ports to disable this action.

The battery-reversal command restores voice ports to their default battery-reversal operation.

If an FXO voice port is connected to the PSTN and supports battery reversal, use the battery-reversal command with the answer keyword to configure answer supervision. This configures the FXO voice port to detect when a call is answered in order to
                              provide correct billing information.

If the voice port, PSTN, or PBX does not support battery reversal, do not use the battery-reversal command because it prevents outgoing calls from being connected. Use the supervisory answer dualtone command instead.

If an FXO port or its peer FXS port does not support battery reversal, avoid configuring battery-reversal or battery-reversal answer on the FXO port. On FXO ports that do not support battery reversal, the battery-reversal command can cause unpredictable behavior, and the battery-reversal answer command prevents calls from being answered. To ensure that battery reversal answer is disabled on FXO ports that do not support
                              battery reversal, use the no battery-reversal command.

## Examples

The following example disables battery reversal on voice port 1/0/0 on a router:

```
voice-port 1/0/0
 no battery-reversal
```

The following example enables battery reversal to provide answer supervision on voice port 1/0/0 on a router:

```
voice-port 1/0/0
 battery-reversal answer
```

### Related Commands

Command

Description

show voice port

Displays voice port configuration information.

supervisory answer dualtone

Enables answer supervision on an FXO voice port on which battery reversal is not supported.

## battery-reversal detection-delay

To configure delay detection interval of battery-reversal signal on analog FXO voice port. Use the battery-reversal detection-delay
                              command in voice-port configuration mode. To reset to default, use the no form of this command or battery-reversal detection-delay
                              0.

This command is only applicable to analog FXO voice port.

battery-reversal detection-delay [ time ]

no battery-reversal detection-delay

### Syntax Description

time

0-800 - detection delay time in milliseconds (default to 0)

### Command Default

no battery-reversal detection-delay

or

battery-reversal detection-delay 0

### Command Modes

Voice-port configuration

## bearer-capability clear-channel

To specify the information transfer capability of the bearer capability information element (IE) in the outgoing ISDN SETUP
                              message for Session Initiation Protocol (SIP) early-media calls that negotiate the clear-channel codec, use the bearer-capability clear-channel command in SIP configuration mode. To reset the information transfer capability of the bearer capability IE to speech (default), use the no form of this command.

bearer-capability clear-channel { audio | rdi | speech | tones | udi [ bidirectional ] | video }

no bearer-capability clear-channel

### Syntax Description

audio

Specifies 3.1 kHz audio.

rdi

Specifies restricted digital information (RDI).

speech

Specifies speech as the information transfer capability. This is the default.

tones

Specifies UDI with tones and announcements.

udi

Specifies unrestricted digital information (UDI).

bidirectional

(Optional) Enables clear-channel codec to UDI bearer capability mapping and UDI bearer capability to clear-channel codec mapping.

video

Specifies video as the information transfer capability.

### Command Default

The default information transfer capability setting for the bearer-capability IE is speech .

### Command Modes

SIP configuration (conf-serv-sip)

## Command History

Release

Modification

12.4(15)T

This command was introduced.

15.2(2)T

This command was modified. The bidirectional keyword was added.

### Usage Guidelines

When a Cisco voice gateway receives a SIP early-media call and negotiates the clear-channel codec, the default for the information
                              transfer capability octet (octet 3) of the bearer capability IE in the outgoing ISDN SETUP message is set to speech . Use the bearer-capability clear-channel command to change the information transfer capability of the bearer capability IE to a different value.

Changing the information transfer capability of the bearer capability IE affects only SIP early-media calls. The information
                                          transfer capability value is always speech for SIP delayed-media calls, even when the clear-channel codec is negotiated.

You can display the current information transfer capability setting for the bearer capability IE using the show running-config command. To show only voice service configuration information, limit the display output to the section on voice service (see
                              the “Examples” section).

When the information transfer capability is set to the default value ( speech ), the output of the show running-config command does not include the bearer-capability information line.

When you configure the bearer-capability clear-channel udi bidirectional command, the ISDN UDI bearer capability is mapped only to the clear-channel codec. Non-UDI bearer capability, like speech,
                              is mapped only to the configured voice codecs. However, the configuration does not indicate the encapsulation type to be used
                              for the clear-channel codec. You can configure the encap clear-channel standard or the voice-class sip encap clear-channel standard command to use the clear-channel codec mode for negotiation.

## Examples

The following examples show how to configure the information transfer capability of the bearer capability IE to UDI to allow
                              for 64 kb/s data transfer over ISDN and how to display the current setting.

Use the following commands to change the information transfer capability setting in the bearer capability IE to UDI:

```
voice service voip
 sip
  bearer-capability clear-channel udi
```

Use the following command to display the current information transfer capability setting:

```
Router# show running-config | section voice service voice service voip
 h323
 sip
  bearer-capability clear-channel udi
```

### Related Commands

Command

Description

encap clear-channel standard

Globally enables RFC 4040-based clear-channel codec negotiation for SIP calls on a Cisco IOS voice gateway or Cisco UBE.

voice-class sip encap clear-channel standard

Enables RFC 4040-based clear-channel codec negotiation for SIP calls on an individual dial peer, overriding the global setting
                                          on a Cisco IOS voice gateway or Cisco UBE.

## billing b-channel

To enable the H.323 gateway to access B-channel information for all H.323 calls, use the billing b-channel command in H.323 voice service configuration mode. To return to the default setting, use the no form of this command.

billing b-channel

no billing b-channel

### Syntax Description

This command has no arguments or keywords.

### Command Default

B-channel information is disabled.

### Command Modes

H.323 voice service configuration

## Command History

Release

Modification

12.3(7)T

This command was introduced.

### Usage Guidelines

This command enables the H.323 application to receive B-channel information of incoming ISDN calls. The B-channel information
                              appears in H.323 ARQ / LRQ messages and can be used during call transfer or to route a call.

## Examples

The following example adds B-channel information to the H.323 gateway:

```
Router(config)# voice service voip Router(conf-voi-serv)# h323 Router(conf-serv-h323)# billing b-channel
```

### Related Commands

Command

Description

h323

Enables H.323 voice service configuration commands.

voice service

Enters voice-service configuration mode and specifies the voice encapsulation type.

## bind

To bind the source address for signaling and media packets to the IPv4 or IPv6 address of a specific interface, use the bind command in SIP configuration mode. To disable binding, use the no form of this command.

bind { control | media | all } source-interface interface-id [ ipv4-address ipv4-address | ipv6-address ipv6-address ]

no bind

### Syntax Description

control

Binds Session Initiation Protocol (SIP) signaling packets.

media

Binds only media packets.

all

Binds SIP signaling and media packets. The source address (the address that shows where the SIP request came from) of the
                                          signaling and media packets is set to the IPv4 or IPv6 address of the specified interface.

source-interface

Specifies an interface as the source address of SIP packets.

interface-id

Specifies one of the following interfaces:

Async : ATM interface

BVI : Bridge-Group Virtual Interface

CTunnel : CTunnel interface

Dialer : Dialer interface

Ethernet : IEEE 802.3

FastEthernet : Fast Ethernet

Lex : Lex interface

Loopback : Loopback interface

Multilink : Multilink-group interface

Null : Null interface

Serial : Serial interface (Frame Relay)

Tunnel : Tunnel interface

Vif : PGM Multicast Host interface

Virtual-Template : Virtual template interface

Virtual-TokenRing : Virtual token ring

ipv4-address ipv4-address

(Optional) Configures the IPv4 address. Several IPv4 addresses can be configured under one interface.

ipv6-address ipv6-address

(Optional) Configures the IPv6 address under an IPv4 interface. Several IPv6 addresses can be configured under one IPv4 interface.

### Command Default

Binding is disabled.

### Command Modes

SIP configuration (conf-serv-sip)

Voice class tenant

## Command History

Release

Modification

12.2(2)XB

This command was introduced on the Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco AS5300, Cisco AS5350, and
                                          Cisco AS5400.

12.2(2)XB2

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T. This command does not support the Cisco AS5300, Cisco AS5350,
                                          Cisco AS5850, and Cisco AS5400 in this release.

12.3(4)T

The media keyword was added.

12.4(22)T

Support for IPv6 was added.

Cisco IOS XE Release 2.5

This command was integrated into Cisco IOS XE Release 2.5

Introduced support for YANG models.

### Usage Guidelines

Async, Ethernet, FastEthernet, Loopback, and Serial (including Frame Relay) are interfaces within the SIP application.

If the bind command is not enabled, the IPv4 layer still provides the best local address.

## Examples

The following example sets up binding on a SIP network:

```
Router(config)# voice serv voip Router(config-voi-serv)# sip Router(config-serv-sip)# bind control source-interface FastEthernet 0
```

### Related Commands

Command

Description

sip

Enters SIP configuration mode from voice service VoIP configuration mode.

## bind interface

To bind an interface to a Cisco CallManager group, use the bind interface command in SCCP Cisco CallManager configuration mode. To unbind the selected interface, use the no form of this command.

bind interface { dynamic | interface-type interface-number }

no bind interface { dynamic | interface-type interface-number }

### Syntax Description

dynamic

The transcoder interface is chosen based on the remote IP address.

interface-type

Type of selected interface.

interface-number

Number of the selected interface.

### Command Default

Interfaces are not associated with any Cisco CallManager group.

### Command Modes

SCCP Cisco CallManager configuration (config-sccp-ccm)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

15.1(3)T1

This command was modified. The dynamic keyword was added.

Cisco IOS XE Amsterdam 17.2.1r

Introduced support for YANG models.

### Usage Guidelines

Normally a firewall only opens certain addresses or port combination to the outside world and those addresses can change dynamically.
                              The VoIP technology requires the use of more than one address or port combination to pass information. The bind interface command allows administrators to dictate the use of one network to transport the signaling and another network to transport
                              the media by assigning an interface to a Cisco CallManager group for a specific interface for the signaling or media application.

The selected interface is used for all calls that belong to the profiles that are associated to this Cisco CallManager group.
                              If the dynamic keyword is configured, the networking device chooses the transcoder interface based on the remote address. If the interface
                              is not configured, the Skinny Call Control Protocol (SCCP) selects the best interface IP address in the gateway. Interfaces
                              are selected according to user requirements. If there is only one group interface, configuration is not needed.

Only one interface can be selected. A given interface can be bound to more than one Cisco CallManager group.

## Examples

The following example shows how to bind the interface to a specific Cisco CallManager group:

Router(config-sccp-ccm)# bind interface fastethernet 2:1

### Related Commands

Command

Description

associate profile

Associates a DSP farm profile with a Cisco CallManager group.

sccp ccm group

Creates a Cisco CallManger group and enters SCCP Cisco CallManager configuration mode.

## block

To configure global settings to drop (not pass) specific incoming Session Initiation Protocol (SIP) provisional response
                              messages on a Cisco IOS voice gateway or Cisco Unified Border Element ( CUBE ), use the block command in voice service SIP configuration mode or voice class tenant configuration mode. To disable a global configuration
                              to drop incoming SIP provisional response messages, use the no form of this command.

block { 180 | 181 | 183 } [ sdp { absent | present } [system] ]

no block { 180 | 181 | 183 }

### Syntax Description

180

Specifies
                                          						that incoming SIP 180 Ringing messages should be dropped (not passed to the
                                          						other leg).

181

Specifies
                                          						that incoming SIP 181 Call is Being Forwarded messages should be dropped (not
                                          						passed to the other leg).

183

Specifies
                                          						that incoming SIP 183 Session in Progress messages should be dropped (not
                                          						passed to the other leg).

sdp

(Optional) Specifies that either the presence or absence of Session Description
                                          						Protocol (SDP) information in the received response determines when the
                                          						dropping of specified incoming SIP messages takes place.

absent

Configures the SDP option so that specified incoming SIP messages are dropped
                                          						only if SDP is absent from the received provisional response.

present

Configures the SDP option so that specified incoming SIP messages are dropped
                                          						only if SDP is present in the received provisional response.

system

Specifies that the block use the global forced CLI setting. This keyword is
                                          						available only for the tenant configuration mode.

### Command Default

Incoming SIP 180,
                              		  181, and 183 provisional responses are forwarded.

### Command Modes

Voice service SIP configuration (conf-serv-sip)

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.4(22)YB

This
                                          						command was introduced. Only SIP 180 and SIP 183 messages are supported on
                                          						Cisco UBEs.

15.0(1)M

This
                                          						command was integrated into Cisco IOS Release 15.0(1)M.

15.0(1)XA

This
                                          						command was modified. Support was added for SIP 181 messages on the Cisco IOS
                                          						SIP gateway, SIP-SIP Cisco UBEs, and the SIP trunk of Cisco Unified
                                          						Communications Manager Express (Cisco Unified CME).

15.1(1)T

This
                                          						command was integrated into Cisco IOS Release 15.1(1)T.

Cisco
                                          						IOS XE Release 3.1S

This
                                          						command was integrated into Cisco IOS XE Release 3.1S

Cisco
                                          						IOS 15.4(1)T

The block 183 sdp
                                                							 absent command was modified to provide support for PRACK and 18x
                                          						with SDP.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants.

Introduced support for YANG models.

### Usage Guidelines

Use the block command
                              		  in voice service SIP configuration mode to globally configure Cisco IOS voice
                              		  gateways and Cisco UBEs to drop specified SIP provisional response messages.
                              		  Additionally, you can use the sdp keyword
                              		  to further control when the specified SIP message is dropped based on either
                              		  the absence or presence of SDP information.

To configure
                              		  settings for an individual dial peer, use the voice-class sip block command
                              		  in dial peer voice configuration mode. To disable global configurations for
                              		  dropping specified incoming SIP messages on a Cisco IOS voice gateway or Cisco
                              		  UBE, use the no block command
                              		  in voice service SIP configuration mode.

## Examples

The following
                              		  example shows how to globally configure dropping of incoming SIP provisional
                              		  response messages:

```
Router> enable Router# configure terminal Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# block 181
```

The following
                              		  example shows how to globally configure dropping of incoming SIP with SDP
                              		  provisional response messages:

```
Router> enable Router# configure terminal Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# block 183 sdp present
```

The following
                              		  example shows how to globally configure dropping of incoming SIP without SDP
                              		  provisional response messages:

```
Router> enable Router# configure terminal Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# block 180 sdp absent
```

The following
                              		  example shows how to globally configure passing all specified incoming SIP
                              		  provisional response messages (except for those on individual dial peers that
                              		  are configured to override the global configuration):

```
Router> enable Router# configure terminal Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# no block 181
```

The following
                              		  example shows how to block responses in CUBE in the voice class tenant
                              		  configuration mode:

```
Router(config-class)# block 181 system
```

### Related Commands

Command

Description

map resp-code

Configures global settings on a CUBE for mapping specific incoming SIP
                                          						provisional response messages to a different SIP response message.

voice-class sip block

Configures an individual dial peer on a Cisco IOS voice gateway or CUBE to drop
                                          						specified SIP provisional response messages.

voice-class sip map resp-code

Configures a specific dial peer on a CUBE to map specific incoming SIP
                                          						provisional response messages to a different SIP response message.

## block-caller

To configure call blocking on caller ID, use the block-caller command in dial peer voice configuration mode. To disable call blocking on caller ID, use the no form of this command.

block-caller number

no block-caller number

### Syntax Description

number

Specifies the telephone number to block. You can use a period (.) as a digit wildcard. For example, the command block-caller 5.51234 blocks all numbers beginning with the digit 5, followed by any digit, and then sequentially followed by the digits 5, 1, 2,
                                          3, and 4.

### Command Default

Call blocking is disabled; the router does not block any calls for any listed directory numbers (LDNs) based on caller ID
                              numbers

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.1(2)XF

This command was introduced on the Cisco 800 series routers.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

This command is available on Cisco 800 series routers that have plain old telephone service (POTS) ports. For each dial peer,
                              you can enter up to ten caller ID numbers to block. The routers do not accept additional caller ID numbers if ten numbers
                              are already present. In that case, a number must be removed before another caller ID number can be added for blocking.

If you do not specify the block-caller command for a local directory, all voice calls to that local directory are accepted. If you specify the block-caller command for a local directory, the router verifies that the incoming calling-party number does not match any caller ID numbers
                              in that local directory before processing or accepting the voice call. Each specified caller ID number and incoming calling-party
                              number is compared from right to left, up to the number of digits in the specified caller ID number or incoming calling-party
                              number, whichever has fewer digits.

This command is effective only if you subscribe to caller ID service. If you enable call blocking on caller ID without subscribing
                              to the caller ID service, the routers do not perform the verification process on calling-party numbers and do not block any
                              calls.

## Examples

The following example configures a router to block calls from a caller whose caller ID number is 408-555-0134.

```
dial-peer voice 1 pots
 block-caller 4085550134
```

### Related Commands

Command

Description

caller-id

Identifies incoming calls with caller ID.

debug pots csm csm

Activates events from which an application can determine and display the status and progress of calls to and from POTS ports.

isdn i-number

Configures several terminal devices to use one subscriber line.

pots call-waiting

Enables local call waiting on a router.

registered-caller ring

Configures the Nariwake service registered caller ring cadence.

## bootup e-lead off

To prevent an analog ear and mouth (E&M) voice port from keying the attached radio on router boot up, use the bootup e-lead off command in voice-port configuration mode. To allow the analog E&M voice port to key the attached radio on boot up, use the no form of this command.

bootup e-lead off

no bootup e-lead off

### Syntax Description

This command has no arguments or keywords.

### Command Default

The analog E&M voice port keys the attached radio on radio boot up.

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.3(4)XD

This command was introduced.

12.3(7)T

This command was integrated into Cisco IOS Release 12.3(7)T.

12.3(14)T

This command was implemented on the Cisco 2800 series and Cisco 3800 series.

12.4(2)T

This feature was integrated into Cisco IOS Release 12.4(2)T.

### Usage Guidelines

This command configures the E-lead behavior on boot up for both voice ports on the voice interface card (VIC).

## Examples

The following example configures the analog E&M voice port to not key the attached radio on router boot up:

```
voice-port 1/0/0
 bootup e-lead off
```

## busyout forced

To force a voice port into the busyout state, use the busyout forced command in voice-port configuration mode. To remove the voice port from the busyout state, use the no form of this command.

busyout forced

no busyout forced

### Syntax Description

This command has no arguments or keywords.

### Command Default

The voice-port is not in the busyout state.

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco MC3810.

12.0(7)XK

This command was implemented on the Cisco 2600s series and Cisco 3600 series. On the Cisco MC3810, the voice-port busyout command was eliminated in favor of this command.

12.1(2)T

The command was integrated into Cisco IOS Release 12.1(2)T.

### Usage Guidelines

If a voice port is in the forced busyout state, only the no busyout forced command can restore the voice port to service.

To avoid conflicting command-line interface (CLI) commands, do not use the busyout forced command and the ds0 busyout command on the same controller.

## Examples

The following example forces analog voice port 3/1/1 on a Cisco 3600 router into the busyout state:

```
voice-port 3/1/1
 busyout forced
```

The following example forces digital voice port 0/0:12 on a Cisco 3600 router into the busyout state:

```
voice-port 0/0:12
 busyout forced
```

### Related Commands

Command

Description

busyout-monitor interface

Configures a voice port to monitor a serial interface for events that would trigger a voice-port busyout.

busyout seize

Changes the busyout seize procedure for a voice port.

show voice busyout

Displays information about the voice busyout state.

## busyout monitor

To place a voice port into the busyout monitor state, enter the busyout monitor command in voice-port configuration mode. To remove the busyout monitor state from the voice port, use the no form of this command.

busyout monitor { serial interface-number | ethernet interface-number | keepalive } [ in-service ]

no busyout monitor { serial interface-number | ethernet interface-number | keepalive }

### Syntax Description

serial

Specifies monitoring of a serial interface. More than one interface can be entered for a voice port.

ethernet

Specifies monitoring of an Ethernet interface. More than one interface can be entered for a voice port.

interface-number

The interface to be monitored for the voice port busyout function.

keepalive

In case of keepalive failures, the selected voice port or ports are busied out.

in-service

(Optional) Configures the voice port to be busied out when any monitored interface comes into service (its state changes to
                                          up). If the keyword is not entered, the voice port is busied out when all monitored interfaces go out of service (that is,
                                          the state changes to down).

### Command Default

The voice port does not monitor any interfaces.

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco MC3810.

12.0(5)XE

This command was implemented on the Cisco 7200 series.

12.0(5)XK

This command was implemented on the Cisco 2600 series and Cisco 3600 series.

12.0(7)T

This command was implemented on the Cisco 2600 series and Cisco 3600 series and integrated into Cisco IOS Release 12.0(7)T.

12.0(7)XK

The ability to monitor an Ethernet port was introduced and the in-service keyword was added. The serial keyword was first supported on the Cisco 2600 series and Cisco 3600 series.

12.1(1)T

The implementation of this command on the Cisco 7200 series was integrated into Cisco IOS Release 12.1(1)T.

12.1(2)T

The serial and ethernet keywords were added, the in-service keyword was integrated into Cisco IOS Release 12.1(2)T, and the interface-number argument was added to the serial and ethernet keywords.

12.1(3)T

The interface keyword was removed.

12.4(6)T

The keepalive keyword was added.

### Usage Guidelines

When you place a voice port in the busyout monitor state, the voice port monitors the specified interface and enters the busyout
                              state when the interface is down. This down state forces the rerouting of calls.

The busyout monitor command monitors only the up or down status of an interface--not end-to-end TCP/IP connectivity.

When an interface is operational, a busied-out voice port returns to its normal state.

This feature can monitor LAN, WAN, and virtual subinterfaces.

A voice port can monitor multiple interfaces at the same time. To configure a voice port to monitor multiple interfaces, reenter
                              the busyout monitor command for each additional interface to be monitored.

If you specify more than one monitored interface for a voice port, all the monitored interfaces must be down to trigger busyout
                              on the voice port.

You can combine in-service and out-of-service monitoring on a voice port. The following rule describes the action if monitored
                              interfaces change state. A voice port is busied out if either of the following occurs:

Any interface monitored for coming into service comes up.

All interfaces monitored for going out of service go down.

## Examples

The following example shows configuration of analog voice port 1/2 to busy out if serial port 0 or 1 comes into service:

```
voice-port 1/2
 busyout monitor serial 0 in-service
 busyout monitor serial 1 in-service
```

The following example shows configuration of digital voice port 1/2/2 on a Cisco 3600 series router to busy out if serial
                              port 0 goes out of service:

```
voice-port 1/2/2
 busyout monitor serial 0
```

The following example shows configuration of the voice port to monitor two serial interfaces and an Ethernet interface. When
                              all these interfaces are down, the voice port is busied out. When at least one interface is operating, the voice port is put
                              back into a normal state.

```
voice-port 3/0:0
 busyout monitor ethernet 0/0
 busyout monitor serial 1/0
 busyout monitor serial 2/0
```

The following example shows configuration of the voice port to be busied out in case of a keepalive failure:

```
voice-port 10
 busyout monitor keepalive
```

### Related Commands

Command

Description

busyout forced

Forces a voice port into the busyout state.

busyout monitor probe

Configures a voice port to enter busyout state if an SAA probe signal returned from a remote interface crosses a delay or
                                          loss threshold.

busyout seize

Changes the busyout seize procedure for a voice port.

show voice busyout

Displays information about the voice busyout state.

voice-port busyout

Places all voice ports associated with a serial or ATM interface into a busyout state.

## busyout monitor action

To place a voice port into graceful or shutdown busyout state when triggered by the busyout monitor, use the busyout monitor action command in voice-port configuration mode. To remove the voice port from the busyout state, use the no form of this command.

busyout monitor action { graceful | shutdown | alarm blue }

no busyout monitor action { graceful | shutdown | alarm blue }

### Syntax Description

graceful

Graceful busyout state.

shutdown

D-channel shutdown busyout state.

alarm blue

Shutdown state with a blue alarm, also known as an alarm-indication signal (AIS).

### Command Default

Default voice busyout behavior without this command is a forced busyout.

Default voice busyout behavior for PRI depends on whether or not the ISDN switch type supports service messages:

If the switch type supports service messages, default voice busyout behavior is to transmit B-channel out-of-service (OOS)
                                    messages and to keep the D channel active. D-Channel service-messages are supported on the following ISDN switch-types: NI,
                                    4ESS (User Side only), 5ESS (User Side only), DMS100.

If the switch type does not support service messages, default voice busyout behavior is to bring down the D channel.

For switch-types not specified above, the D-channel is taken down when the busyout monitor action graceful is configured.

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.2(13)T

The busyout monitor action graceful command was introduced on the following platforms: Cisco 2600 series, Cisco 2600XM, Cisco 2691, Cisco 3640, Cisco 3660, Cisco
                                          3725, and Cisco VG200.

12.3(6)

The busyout monitor action shutdown command was introduced on the following platforms: Cisco 1700 series, Cisco IAD2420 series, Cisco 2600 series, Cisco 2600XM
                                          series, Cisco 2691, Cisco 3600 series, Cisco 3700 series, Cisco 4224, Cisco 7200 series, Cisco 7301, Cisco 7400 series, Cisco
                                          MC3810, Cisco WS-X4604-GWY, and Cisco VG200.

12.3(7)T

The busyout monitor action shutdown command was integrated into Cisco IOS Release 12.3(7)T and support was added for the Cisco IAD2430 series.

12.4(6)T

The busyout monitor action graceful and busyout monitor action shutdown commands were introduced to replace the busyout action graceful and busyout action shutdown commands.

12.4(9)T

The busyout monitor action command was introduced to combine the busyout monitor action graceful and busyout monitor action shutdown commands. The shutdown alarm blue keywords were added.

### Usage Guidelines

Use this command to control busyout behavior that is triggered by the busyout monitor command.

This command with the graceful keyword busies out the voice port immediately or, if there is an active call on this voice port, waits until the call is over.

This command with the shutdown keyword has the following attributes:

Before Cisco  IOS Release 12.2(8)T, when voice busyout is triggered on a PRI voice port, the D channel is deactivated until
                                    the busyout trigger is cleared. Some ISDN switch types, however, support in-service and OOS Q.931 messages that permit B channels
                                    to be taken out of service while still keeping the D channel active. Starting in Cisco IOS Release 12.3(8)T for these ISDN
                                    switch types, OOS messages are sent and the D channel is kept active when a voice busyout is triggered.

This keyword is available only for PRI voice ports.

For switch-types not specified above, the D-channel is be taken down when the busyout monitor action graceful command is configured.

## Examples

The following example shows analog voice-port busyout state set to graceful:

```
voice-port 2/0:15
 busyout monitor action graceful
```

The following example shows E1 PRI voice-port busyout state set to shutdown:

```
voice-port 1/1:15 (E1 PRI)
 busyout monitor gatekeeper
 busyout monitor action shutdown
```

The following example shows T1 PRI voice-port busyout state set to shutdown:

```
voice-port 0/1:23 (T1 PRI)
 busyout monitor gatekeeper
 busyout monitor action shutdown
```

### Related Commands

Command

Description

busyout forced

Forces a voice port into busyout state.

busyout monitor

Configures a voice port to monitor an interface for events that would trigger voice-port busyout.

busyout monitor backhaul

Configures a voice port to enter busyout-monitor state with backhaul-L3 connectivity monitoring during a WAN failure.

busyout monitor gatekeeper

Configures a voice port to enter busyout state if connectivity to the gatekeeper is lost.

busyout monitor probe

Configures a voice port to enter busyout state if an SAA probe signal returned from a remote, IP-addressable interface crosses
                                          a specified delay or loss threshold.

busyout seize

Changes the busyout seize procedure for a voice port.

show voice busyout

Displays information about voice-busyout state.

voice-port

Enters voice-port configuration mode and identifies the voice port to be configured.

## busyout monitor backhaul

To configure a voice port to enter busyout-monitor state with backhaul-L3 connectivity monitoring during a wide-area-network
                              (WAN) failure, use the busyout monitor backhaul command in voice-port configuration mode. To disable busyout-monitor state, use the no form of this command.

busyout monitor backhaul

no busyout monitor backhaul

### Syntax Description

This command has no arguments or keywords.

### Command Default

If this command is not used, the voice port is not configured to enter busyout state during a WAN failure.

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.4(9)T

This command was introduced.

### Usage Guidelines

Use this command to implement backhaul-L3 connectivity monitoring.

## Examples

The following example configures a voice port to enter busyout-monitor state with backhaul-L3 connectivity monitoring during
                              a WAN failure:

```
Router(config-voiceport)# busyout monitor backhaul
```

### Related Commands

Command

Description

busyout monitor action

Places a voice port into busyout state.

busyout monitor

Configures a voice port to enter busyout-monitor state.

## busyout monitor gatekeeper

To configure a voice port to enter the busyout state if connectivity to the gatekeeper is lost, use the busyout monitor gatekeeper command in voice-port configuration mode. To configure the monitor to trigger a busyout when any voice port assigned to a
                              specific voice class loses connectivity to the gatekeeper, use the busyout monitor gatekeeper command in voice-class configuration mode. To disable the busyout monitoring state for the gatekeeper, use the no form of this command.

busyout monitor gatekeeper

no busyout monitor gatekeeper

### Syntax Description

This command has no arguments or keywords.

### Command Default

If this command is not used, the voice port or voice class is not configured to enter a busyout state if connectivity to the
                              gatekeeper is lost.

### Command Modes

Voice-class configuration (config-voice-class) Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.2(13)T

This command was introduced on the following platforms: Cisco 2600 series, Cisco 2600XM, Cisco 2691, Cisco 3640, Cisco 3660,
                                          Cisco 3725 and Cisco VG200.

12.4(6)T

This command was extended to include functionality in voice-class configuration mode.

### Usage Guidelines

Use this command to monitor the connection between the gateway and gatekeeper. In voice-port configuration mode, if a voice
                              port loses connectivity to the gatekeeper, the voice port enters a busyout state. In voice configuration mode, if any voice
                              port assigned to a specific voice class loses connectivity to the gatekeeper, a busyout is triggered.

## Examples

The following example shows the busyout monitor state set to busy out the port according to the state of the gatekeeper:

```
voice-port 1/1/1
 busyout monitor gatekeeper
```

The following example enters voice-class (busyout) configuration mode and creates a voice class named 33. The monitor is set
                              to busyout when any voice port in voice class 33 loses connectivity to the gatekeeper:

```
voice-class busyout 33
 busyout monitor gatekeeper
```

### Related Commands

Command

Description

busyout monitor action graceful

Places a voice port into the graceful busyout state when triggered by the busyout monitor.

busyout monitor action shutdown

Shuts down the voice port immediately, but if there is an active call it waits until the call is over.

busyout forced

Forces a voice port into the busyout state.

busyout monitor

Configures a voice port to monitor an interface for events that would trigger a voice-port busyout.

busyout monitor probe

Configures a voice port to enter the busyout state if an SAA probe signal returned from a remote, IP-addressable interface
                                          crosses a specified delay or loss threshold.

busyout seize

Changes the busyout seize procedure for a voice port.

show voice busyout

Displays information about the voice busyout state.

voice-port

Enters voice-port configuration mode and identifies the voice port to be configured.

## busyout monitor probe

To configure a voice port to enter the busyout state if a Service Assurance Agent (SAA) probe signal is returned from a remote
                              IP-addressable interface after the expiration of a specified delay or loss threshold, use the busyout monitor probe command in voice-port
                              configuration mode or voice class busyout mode. To configure a voice port not to monitor SAA probe signals, use the no form of this command.

busyout monitor probe [ icmp-ping ] ip-address [ codec codec-type | size bytes ] [ icpif number | loss percent delay milliseconds ] [ grace-period seconds ] size

no busyout monitor probe ip-address

### Syntax Description

icmp-ping

(Optional) Configures voice-port parameters to use ICMP pings to monitor IP destinations.

ip - address

The IP address of a target interface for the SAA probe signal.

codec

(Optional) Configures the profile of the SAA probe signal to mimic the packet size and interval of a specific codec type.

codec - type

(Optional) The codec type for the SAA probe signal. Available options are as follows:

g711a --G.711 a-law

g711u --G.711 mu-law (the default)

g729 --G.729

g729a --G.729 Annex A

g729b --G.729 Annex B

size bytes

(Optional) Size (in bytes) of the ping packet. Default is 32.

icpif

(Optional) Configures the busyout monitor probe to use an Impairment/Calculated Planning Impairment Factor (ICPIF) loss/delay
                                          busyout threshold, in accordance with ITU-T G.113. The ICPIF numbers represent predefined combinations of loss and delay.

number

(Optional) The ICPIF threshold for initiating a busyout condition. Range is from 0 to 30. Low numbers are equivalent to low
                                          loss and delay thresholds.

loss

(Optional) Configures the percentage-of-packets-lost threshold for initiating a busyout condition.

percent

(Optional) The loss value (expressed as a percentage) for initiating a busyout condition. Range is from 1 to 100.

delay

(Optional) Configures the average packet delay threshold for initiating a busyout condition.

milliseconds

(Optional) The delay threshold, in milliseconds, for initiating a busyout condition. Range is from 1 to 2,147,483,647.

grace-period

(Optional) Configures a time limit that the system waits before initiating a busyout condition after the loss of SAA probe
                                          connectivity.

seconds

(Optional) Number of seconds for the duration of the grace period. Range is from 30 to 300.

### Command Default

If the busyout monitor probe command is not entered, the voice port does not monitor SAA probe signals.

If the busyout monitor probe command is entered with no optional keywords or arguments, the default codec type is G.711 a-law, the default loss and delay
                              thresholds are the threshold values that are configured with the call fallback threshold delay-loss command, and the loss of SAA connectivity causes an immediate forced busyout condition.

### Command Modes

Voice-port configuration and voice class busyout

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco 2600 and Cisco 3600 series and on the Cisco MC3810.

12.3(15)

This command was integrated into Cisco IOS Release 12.3(15) and the grace-period keyword and seconds argument were added.

12.4(1)

This command was integrated into Cisco IOS Release 12.4(1).

12.4(2)T

This command was integrated into Cisco IOS Release 12.4(2)T.

### Usage Guidelines

A voice port can monitor multiple interfaces at the same time. To configure a voice port to monitor multiple interfaces, enter
                              the busyout monitor probe command for each additional interface to be monitored.

Caution

The busyout monitor probe command is effective only if the call fallback function is enabled on the source router, and the SAA responder is enabled
                                          on the target router. To enable the call fallback function, you must enter the call fallback active command for the busyout monitor probe command to work.

The SAA probe is transmitted periodically with a period determined by the call fallback function.

Low thresholds of ICPIF, loss, and delay result in early busyout when the link deteriorates, thereby raising the voice minimum
                              quality level. High thresholds prevent busyout until loss and delay are long, allowing transmission of lower-quality voice.

Caution

If thresholds are set too low, the link can alternate between in-service and out-of-service states, causing repeated interruptions
                                          of traffic.

Before the introduction of the grace-period keyword to the busyout monitor probe command, the loss of SAA probe connectivity was sufficient to immediately enforce busyout, causing service and connectivity
                              problems in some networks because busyout conditions could occur frequently and abruptly. To improve busyout monitoring via
                              SAA probes, the grace-period setting allows for an additional timer that must expire before a busyout condition is enforced. That is, the SAA probes and
                              the period of grace must both expire before a busyout condition is invoked. If the SAA IP connectivity is restored within
                              the period of grace, the busyout condition does not occur.

To disable the grace-period option, you must first enter the no busyout monitor probe command and then re-enter the busyout monitor probe command without the grace-period option.

The grace-period keyword is not available in Cisco IOS Release 12.3T.

## Examples

The following example shows how to configure analog voice port 1/1/0 to use an SAA probe with a G.711a-law profile to probe
                              the link to two remote interfaces that have IP addresses and to busy out the voice port if SAA probe connectivity is lost
                              for at least 5 seconds. Both links have a loss exceeding 25 percent or a packet delay of more than 1.5 seconds.

```
voice-port 1/1/0
 busyout monitor probe 209.165.202.128 codec g711a loss 25 delay 1500 grace-period 45
 busyout monitor probe 209.165.202.129 codec g711a loss 25 delay 1500 grace-period 45
```

### Related Commands

Command

Description

busyout monitor

Places a voice port into the busyout monitor state.

call fallback active

Enables the ICMP-ping or SAA (formerly RTR) probe mechanism for use with the dial-peer monitor probe or voice-port busyout monitor probe commands.

call fallback threshold delay-loss

Forces a voice port into the busyout state.

show voice busyout

Displays information about the voice busyout state.

voice class busyout

Creates a voice class for local voice busyout functions.

## busyout seize

To change the busyout action for a Foreign Exchange Office (FXO) or Foreign Exchange Station (FXS) voice port, use the busyout seize command in voice-port configuration mode. To restore the default busyout action, use the no form of this command.

busyout seize { ignore | repeat }

no busyout seize

### Syntax Description

ignore

Specifies the type of ignore procedure, depending on the type of voice port signaling. See the table below for more information.

repeat

Specifies the type of repeat procedure, depending on the type of voice port signaling. See the table below for more information.

### Command Default

See the table below for the default actions for different voice ports and signaling types

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco MC3810.

12.0(7)XK

This command was implemented on the Cisco 2600 and Cisco 3600 series.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

### Usage Guidelines

The busyout seize command is valid for both analog and digital voice ports. On digital voice ports, the busyout actions are valid whether the
                              busyout results from a voice-port busyout event or from the ds0-busyout command.

The voice port returns to an idle state when the event that triggered the busyout disappears.

The table below describes the busyout actions for the busyout seize settings on each voice port type.

The busyout action for E and M voice ports is to seize the far end by setting lead busy.

Voice Port Signaling Type

Procedure Setting

(busyout-option command)

Busyout Actions

FXS loop start

Default

Removes the power from the loop. For analog voice ports, this is equivalent to removing the ground from the tip lead. For
                                          digital voice ports, the port generates the bit pattern equivalent to removing the ground from the tip lead, or it busies
                                          out if the bit pattern exists.

FXS loop start

Ignore

Ignores the ground on the ring lead.

FXS ground start

Default

Grounds the tip lead and stays at this state.

FXS ground start

Ignore

Leaves the tip lead open.

Ignores the ground on the ring lead.

FXS ground start

Repeat

Grounds the tip lead.

Waits for the far end to close the loop.

The far end closes the loop.

If the far end then opens the loop, FXS removes the ground from the tip lead.

FXS waits for several seconds before returning to Step 1.

FXO loop start

Default

Closes the loop and stays at this state.

FXO loop start

Ignore

Leaves the loop open.

Ignores the ringing current on the ring level.

FXO loop start

Repeat

Closes the loop.

After the detected far end starts the power denial procedure, FXO opens the loop.

After the detected far end has completed the power denial procedure, FXO waits for several seconds before returning to Step
                                                   1.

FXO ground start

Default

Grounds the tip lead.

FXO ground start

Ignore

Leaves the loop open.

Ignores the running current on the ring lead, or the ground current on the tip lead.

FXO ground start

Repeat

Grounds the ring lead.

Removes the ground from the ring lead and closes the loop after the detected far end grounds the tip lead.

When the detected far end removes the ground from tip lead, FXO opens the loop.

FXO waits for several seconds before returning to Step 1.

## Examples

The following example shows configuration of analog voice port 1/1 to perform the ignore actions when busied out:

```
voice-port 1/1
 busyout seize ignore
```

The following example shows configuration of digital voice port 0:2 to perform the repeat actions when busied out:

```
voice-port 0:2
 busyout seize repeat
```

### Related Commands

Command

Description

busyout forced

Forces a voice port into the busyout state.

busyout-monitor interface

Configures a voice port to monitor an interface for events that would trigger a voice port busyout.

ds0 busyout

Forces a DS0 time slot on a controller into the busyout state.

show voice busyout

Displays information about the voice busyout state.

voice-port busyout

Places all voice ports associated with a serial or ATM interface into a busyout state.

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced. |
| 12.2(2)T | This command was implemented on the Cisco 7200. |
| 12.2(4)T | This command was implemented on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)XB | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850 platform. |
| 12.2(8)T | This command was implemented on Cisco IAD2420. Support for the Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included
                                          in this release. |
| 12.2(11)T | This command is supported on the Cisco AS5350, Cisco AS5400, and Cisco AS5850 in this release. |

| Command | Description |
|---|---|
| clear backhaul-session-manager group | Resets the statistics or traffic counters for a specified session group. |
| clear rudpv1 statistics | Clears the RUDP statistics and failure counters. |
| group | Creates a session group and associates it with a specified session set. |
| group auto-reset | Configures the maximum auto-reset value. |
| group cumulative-ack | Configures maximum cumulative acknowledgments. |
| group out-of-sequence | Configures maximum out-of-sequence segments that are received before an EACK is sent. |
| group receive | Configures maximum receive segments. |
| group retransmit | Configures maximum retransmits. |
| group timer cumulative-ack | Configures cumulative acknowledgment timeout. |
| group timer keepalive | Configures keepalive (or null segment) timeout. |
| group timer retransmit | Configures retransmission timeout. |
| group timer transfer | Configures state transfer timeout. |
| isdn bind-l3 | Configures the ISDN serial interface for backhaul. |
| session group | Associates a transport session with a specified session group. |
| set | Creates a fault-tolerant or non-fault-tolerant session set with the client or server option. |
| show backhaul-session-manager group | Displays status, statistics, or configuration of a specified or all session groups. |
| show backhaul-session-manager session | Displays status, statistics, or configuration of sessions. |
| show backhaul-session-manager set | Displays session groups associated with a specific or all session sets. |
| show rudpv1 | Displays RUDP statistics. |

| maximum value | Sets the maximum bandwidth for an H.320 call on a POTS dial peer. The range is 64 to 1024, entered in increments of 64 kilobits
                                          per second (kbps). The default is 64. |
|---|---|
| minimum value | (Optional) Sets the minimum bandwidth. Acceptable values are 64 kbps or minimum value = maximum value . |

| Release | Modification |
|---|---|
| 12.4(11)T | This command was introduced. |

| Command | Description |
|---|---|
| bandwidth | Specifies the maximum aggregate bandwidth for H.323 traffic and verifies the available bandwidth of the destination gatekeeper. |

| interzone | Total amount of bandwidth for H.323 traffic from the zone to any other zone. |
|---|---|
| total | Total amount of bandwidth for H.323 traffic allowed in the zone. |
| session | Maximum bandwidth allowed for a session in the zone. |
| default | Default value for all zones. |
| zone | A particular zone. |
| zone-name | Name of the particular zone. |
| bandwidth-size | Maximum bandwidth, in kbps. For interzone and total , range : 1 to 10000000. For session , range:1 to 5000. |

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced on the Cisco 2500, Cisco 3600 series and the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. The bandwidth command replaced the zone bw command. |
| 12.1(5)XM | The bandwidth command was recognized without using the zone gatekeeper command. |
| 12.2(2)T | The changes in Cisco IOS Release 12.1(5)XM were integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |

| Command | Description |
|---|---|
| bandwidth check-destination | Enables the gatekeeper to verify available bandwidth resources at the destination endpoint. |
| bandwidth remote | Specifies the total bandwidth for H.323 traffic between this gatekeeper and any other gatekeeper. |
| h323 interface | Defines on which port the proxy listens. |
| h323 t120 | Enables the T.120 capabilities on the router and specifies bypass or proxy mode. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| bandwidth | Specifies the maximum aggregate bandwidth for H.323 traffic from a zone to another zone, within a zone, or for a session in
                                          a zone. |
| bandwidth remote | Specifies the total bandwidth for H.323 traffic between this gatekeeper and any other gatekeeper. |
| h323 interface | Defines the port on which port the proxy listens. |
| h323 t120 | Enables the T.120 capabilities on your router and specifies bypass or proxy mode. |

| bandwidth-size | Maximum bandwidth, in kbps. Range: 1 to 10000000. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)XI | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco 7200 series. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |

| Command | Description |
|---|---|
| bandwidth | Specifies the maximum aggregate bandwidth for H.323 traffic from a zone to another zone, within a zone, or for a session in
                                          a zone. |
| bandwidth check-destination | Enables the gatekeeper to verify available bandwidth resources at the destination endpoint. |
| h323 interface | Defines which port the proxy listens on. |
| h323 t120 | Enables the T.120 capabilities on your router and specifies bypass or proxy mode. |

| answer | (Optional) Configures an FXO port to support answer supervision by detection of battery reversal. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(7)XK | This command was introduced on the Cisco 2600 series and Cisco 3600 series and on the Cisco MC3810. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.2(2)T | The answer keyword was added. |

| Command | Description |
|---|---|
| show voice port | Displays voice port configuration information. |
| supervisory answer dualtone | Enables answer supervision on an FXO voice port on which battery reversal is not supported. |

| time | 0-800 - detection delay time in milliseconds (default to 0) |
|---|---|

| audio | Specifies 3.1 kHz audio. |
|---|---|
| rdi | Specifies restricted digital information (RDI). |
| speech | Specifies speech as the information transfer capability. This is the default. |
| tones | Specifies UDI with tones and announcements. |
| udi | Specifies unrestricted digital information (UDI). |
| bidirectional | (Optional) Enables clear-channel codec to UDI bearer capability mapping and UDI bearer capability to clear-channel codec mapping. |
| video | Specifies video as the information transfer capability. |

| Release | Modification |
|---|---|
| 12.4(15)T | This command was introduced. |
| 15.2(2)T | This command was modified. The bidirectional keyword was added. |

| Note | Changing the information transfer capability of the bearer capability IE affects only SIP early-media calls. The information
                                          transfer capability value is always speech for SIP delayed-media calls, even when the clear-channel codec is negotiated. |
|---|---|

| Note | When the information transfer capability is set to the default value ( speech ), the output of the show running-config command does not include the bearer-capability information line. |
|---|---|

| Command | Description |
|---|---|
| encap clear-channel standard | Globally enables RFC 4040-based clear-channel codec negotiation for SIP calls on a Cisco IOS voice gateway or Cisco UBE. |
| voice-class sip encap clear-channel standard | Enables RFC 4040-based clear-channel codec negotiation for SIP calls on an individual dial peer, overriding the global setting
                                          on a Cisco IOS voice gateway or Cisco UBE. |

| Release | Modification |
|---|---|
| 12.3(7)T | This command was introduced. |

| Command | Description |
|---|---|
| h323 | Enables H.323 voice service configuration commands. |
| voice service | Enters voice-service configuration mode and specifies the voice encapsulation type. |

| control | Binds Session Initiation Protocol (SIP) signaling packets. |
|---|---|
| media | Binds only media packets. |
| all | Binds SIP signaling and media packets. The source address (the address that shows where the SIP request came from) of the
                                          signaling and media packets is set to the IPv4 or IPv6 address of the specified interface. |
| source-interface | Specifies an interface as the source address of SIP packets. |
| interface-id | Specifies one of the following interfaces: Async : ATM interface BVI : Bridge-Group Virtual Interface CTunnel : CTunnel interface Dialer : Dialer interface Ethernet : IEEE 802.3 FastEthernet : Fast Ethernet Lex : Lex interface Loopback : Loopback interface Multilink : Multilink-group interface Null : Null interface Serial : Serial interface (Frame Relay) Tunnel : Tunnel interface Vif : PGM Multicast Host interface Virtual-Template : Virtual template interface Virtual-TokenRing : Virtual token ring |
| ipv4-address ipv4-address | (Optional) Configures the IPv4 address. Several IPv4 addresses can be configured under one interface. |
| ipv6-address ipv6-address | (Optional) Configures the IPv6 address under an IPv4 interface. Several IPv6 addresses can be configured under one IPv4 interface. |

| Release | Modification |
|---|---|
| 12.2(2)XB | This command was introduced on the Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco AS5300, Cisco AS5350, and
                                          Cisco AS5400. |
| 12.2(2)XB2 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T. This command does not support the Cisco AS5300, Cisco AS5350,
                                          Cisco AS5850, and Cisco AS5400 in this release. |
| 12.3(4)T | The media keyword was added. |
| 12.4(22)T | Support for IPv6 was added. |
| Cisco IOS XE Release 2.5 | This command was integrated into Cisco IOS XE Release 2.5 |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Command | Description |
|---|---|
| sip | Enters SIP configuration mode from voice service VoIP configuration mode. |

| dynamic | The transcoder interface is chosen based on the remote IP address. |
|---|---|
| interface-type | Type of selected interface. |
| interface-number | Number of the selected interface. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 15.1(3)T1 | This command was modified. The dynamic keyword was added. |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Note | Only one interface can be selected. A given interface can be bound to more than one Cisco CallManager group. |
|---|---|

| Command | Description |
|---|---|
| associate profile | Associates a DSP farm profile with a Cisco CallManager group. |
| sccp ccm group | Creates a Cisco CallManger group and enters SCCP Cisco CallManager configuration mode. |

| 180 | Specifies
                                          						that incoming SIP 180 Ringing messages should be dropped (not passed to the
                                          						other leg). |
|---|---|
| 181 | Specifies
                                          						that incoming SIP 181 Call is Being Forwarded messages should be dropped (not
                                          						passed to the other leg). |
| 183 | Specifies
                                          						that incoming SIP 183 Session in Progress messages should be dropped (not
                                          						passed to the other leg). |
| sdp | (Optional) Specifies that either the presence or absence of Session Description
                                          						Protocol (SDP) information in the received response determines when the
                                          						dropping of specified incoming SIP messages takes place. |
| absent | Configures the SDP option so that specified incoming SIP messages are dropped
                                          						only if SDP is absent from the received provisional response. |
| present | Configures the SDP option so that specified incoming SIP messages are dropped
                                          						only if SDP is present in the received provisional response. |
| system | Specifies that the block use the global forced CLI setting. This keyword is
                                          						available only for the tenant configuration mode. |

| Release | Modification |
|---|---|
| 12.4(22)YB | This
                                          						command was introduced. Only SIP 180 and SIP 183 messages are supported on
                                          						Cisco UBEs. |
| 15.0(1)M | This
                                          						command was integrated into Cisco IOS Release 15.0(1)M. |
| 15.0(1)XA | This
                                          						command was modified. Support was added for SIP 181 messages on the Cisco IOS
                                          						SIP gateway, SIP-SIP Cisco UBEs, and the SIP trunk of Cisco Unified
                                          						Communications Manager Express (Cisco Unified CME). |
| 15.1(1)T | This
                                          						command was integrated into Cisco IOS Release 15.1(1)T. |
| Cisco
                                          						IOS XE Release 3.1S | This
                                          						command was integrated into Cisco IOS XE Release 3.1S |
| Cisco
                                          						IOS 15.4(1)T | The block 183 sdp
                                                							 absent command was modified to provide support for PRACK and 18x
                                          						with SDP. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Note | This command is supported only on outbound dial peers--it is nonoperational if configured on inbound dial peers. You should
                                       configure this command on the outbound SIP leg that sends out the initial INVITE message. Additionally, this feature applies
                                       only to SIP-to-SIP calls and will have no effect on H.323-to-SIP calls. |
|---|---|

| Note | When the block 183 sdp absent command is enabled, the Require: rel1xx header is not disabled, thus supporting for PRACK and 18x with SDP. |
|---|---|

| Command | Description |
|---|---|
| map resp-code | Configures global settings on a CUBE for mapping specific incoming SIP
                                          						provisional response messages to a different SIP response message. |
| voice-class sip block | Configures an individual dial peer on a Cisco IOS voice gateway or CUBE to drop
                                          						specified SIP provisional response messages. |
| voice-class sip map resp-code | Configures a specific dial peer on a CUBE to map specific incoming SIP
                                          						provisional response messages to a different SIP response message. |

| number | Specifies the telephone number to block. You can use a period (.) as a digit wildcard. For example, the command block-caller 5.51234 blocks all numbers beginning with the digit 5, followed by any digit, and then sequentially followed by the digits 5, 1, 2,
                                          3, and 4. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(2)XF | This command was introduced on the Cisco 800 series routers. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |

| Command | Description |
|---|---|
| caller-id | Identifies incoming calls with caller ID. |
| debug pots csm csm | Activates events from which an application can determine and display the status and progress of calls to and from POTS ports. |
| isdn i-number | Configures several terminal devices to use one subscriber line. |
| pots call-waiting | Enables local call waiting on a router. |
| registered-caller ring | Configures the Nariwake service registered caller ring cadence. |

| Release | Modification |
|---|---|
| 12.3(4)XD | This command was introduced. |
| 12.3(7)T | This command was integrated into Cisco IOS Release 12.3(7)T. |
| 12.3(14)T | This command was implemented on the Cisco 2800 series and Cisco 3800 series. |
| 12.4(2)T | This feature was integrated into Cisco IOS Release 12.4(2)T. |

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco MC3810. |
| 12.0(7)XK | This command was implemented on the Cisco 2600s series and Cisco 3600 series. On the Cisco MC3810, the voice-port busyout command was eliminated in favor of this command. |
| 12.1(2)T | The command was integrated into Cisco IOS Release 12.1(2)T. |

| Command | Description |
|---|---|
| busyout-monitor interface | Configures a voice port to monitor a serial interface for events that would trigger a voice-port busyout. |
| busyout seize | Changes the busyout seize procedure for a voice port. |
| show voice busyout | Displays information about the voice busyout state. |

| serial | Specifies monitoring of a serial interface. More than one interface can be entered for a voice port. |
|---|---|
| ethernet | Specifies monitoring of an Ethernet interface. More than one interface can be entered for a voice port. |
| interface-number | The interface to be monitored for the voice port busyout function. |
| keepalive | In case of keepalive failures, the selected voice port or ports are busied out. |
| in-service | (Optional) Configures the voice port to be busied out when any monitored interface comes into service (its state changes to
                                          up). If the keyword is not entered, the voice port is busied out when all monitored interfaces go out of service (that is,
                                          the state changes to down). |

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco MC3810. |
| 12.0(5)XE | This command was implemented on the Cisco 7200 series. |
| 12.0(5)XK | This command was implemented on the Cisco 2600 series and Cisco 3600 series. |
| 12.0(7)T | This command was implemented on the Cisco 2600 series and Cisco 3600 series and integrated into Cisco IOS Release 12.0(7)T. |
| 12.0(7)XK | The ability to monitor an Ethernet port was introduced and the in-service keyword was added. The serial keyword was first supported on the Cisco 2600 series and Cisco 3600 series. |
| 12.1(1)T | The implementation of this command on the Cisco 7200 series was integrated into Cisco IOS Release 12.1(1)T. |
| 12.1(2)T | The serial and ethernet keywords were added, the in-service keyword was integrated into Cisco IOS Release 12.1(2)T, and the interface-number argument was added to the serial and ethernet keywords. |
| 12.1(3)T | The interface keyword was removed. |
| 12.4(6)T | The keepalive keyword was added. |

| Command | Description |
|---|---|
| busyout forced | Forces a voice port into the busyout state. |
| busyout monitor probe | Configures a voice port to enter busyout state if an SAA probe signal returned from a remote interface crosses a delay or
                                          loss threshold. |
| busyout seize | Changes the busyout seize procedure for a voice port. |
| show voice busyout | Displays information about the voice busyout state. |
| voice-port busyout | Places all voice ports associated with a serial or ATM interface into a busyout state. |

| graceful | Graceful busyout state. |
|---|---|
| shutdown | D-channel shutdown busyout state. |
| alarm blue | Shutdown state with a blue alarm, also known as an alarm-indication signal (AIS). |

| Release | Modification |
|---|---|
| 12.2(13)T | The busyout monitor action graceful command was introduced on the following platforms: Cisco 2600 series, Cisco 2600XM, Cisco 2691, Cisco 3640, Cisco 3660, Cisco
                                          3725, and Cisco VG200. |
| 12.3(6) | The busyout monitor action shutdown command was introduced on the following platforms: Cisco 1700 series, Cisco IAD2420 series, Cisco 2600 series, Cisco 2600XM
                                          series, Cisco 2691, Cisco 3600 series, Cisco 3700 series, Cisco 4224, Cisco 7200 series, Cisco 7301, Cisco 7400 series, Cisco
                                          MC3810, Cisco WS-X4604-GWY, and Cisco VG200. |
| 12.3(7)T | The busyout monitor action shutdown command was integrated into Cisco IOS Release 12.3(7)T and support was added for the Cisco IAD2430 series. |
| 12.4(6)T | The busyout monitor action graceful and busyout monitor action shutdown commands were introduced to replace the busyout action graceful and busyout action shutdown commands. |
| 12.4(9)T | The busyout monitor action command was introduced to combine the busyout monitor action graceful and busyout monitor action shutdown commands. The shutdown alarm blue keywords were added. |

| Command | Description |
|---|---|
| busyout forced | Forces a voice port into busyout state. |
| busyout monitor | Configures a voice port to monitor an interface for events that would trigger voice-port busyout. |
| busyout monitor backhaul | Configures a voice port to enter busyout-monitor state with backhaul-L3 connectivity monitoring during a WAN failure. |
| busyout monitor gatekeeper | Configures a voice port to enter busyout state if connectivity to the gatekeeper is lost. |
| busyout monitor probe | Configures a voice port to enter busyout state if an SAA probe signal returned from a remote, IP-addressable interface crosses
                                          a specified delay or loss threshold. |
| busyout seize | Changes the busyout seize procedure for a voice port. |
| show voice busyout | Displays information about voice-busyout state. |
| voice-port | Enters voice-port configuration mode and identifies the voice port to be configured. |

| Release | Modification |
|---|---|
| 12.4(9)T | This command was introduced. |

| Command | Description |
|---|---|
| busyout monitor action | Places a voice port into busyout state. |
| busyout monitor | Configures a voice port to enter busyout-monitor state. |

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced on the following platforms: Cisco 2600 series, Cisco 2600XM, Cisco 2691, Cisco 3640, Cisco 3660,
                                          Cisco 3725 and Cisco VG200. |
| 12.4(6)T | This command was extended to include functionality in voice-class configuration mode. |

| Command | Description |
|---|---|
| busyout monitor action graceful | Places a voice port into the graceful busyout state when triggered by the busyout monitor. |
| busyout monitor action shutdown | Shuts down the voice port immediately, but if there is an active call it waits until the call is over. |
| busyout forced | Forces a voice port into the busyout state. |
| busyout monitor | Configures a voice port to monitor an interface for events that would trigger a voice-port busyout. |
| busyout monitor probe | Configures a voice port to enter the busyout state if an SAA probe signal returned from a remote, IP-addressable interface
                                          crosses a specified delay or loss threshold. |
| busyout seize | Changes the busyout seize procedure for a voice port. |
| show voice busyout | Displays information about the voice busyout state. |
| voice-port | Enters voice-port configuration mode and identifies the voice port to be configured. |

| icmp-ping | (Optional) Configures voice-port parameters to use ICMP pings to monitor IP destinations. |
|---|---|
| ip - address | The IP address of a target interface for the SAA probe signal. |
| codec | (Optional) Configures the profile of the SAA probe signal to mimic the packet size and interval of a specific codec type. |
| codec - type | (Optional) The codec type for the SAA probe signal. Available options are as follows: g711a --G.711 a-law g711u --G.711 mu-law (the default) g729 --G.729 g729a --G.729 Annex A g729b --G.729 Annex B |
| size bytes | (Optional) Size (in bytes) of the ping packet. Default is 32. |
| icpif | (Optional) Configures the busyout monitor probe to use an Impairment/Calculated Planning Impairment Factor (ICPIF) loss/delay
                                          busyout threshold, in accordance with ITU-T G.113. The ICPIF numbers represent predefined combinations of loss and delay. |
| number | (Optional) The ICPIF threshold for initiating a busyout condition. Range is from 0 to 30. Low numbers are equivalent to low
                                          loss and delay thresholds. |
| loss | (Optional) Configures the percentage-of-packets-lost threshold for initiating a busyout condition. |
| percent | (Optional) The loss value (expressed as a percentage) for initiating a busyout condition. Range is from 1 to 100. |
| delay | (Optional) Configures the average packet delay threshold for initiating a busyout condition. |
| milliseconds | (Optional) The delay threshold, in milliseconds, for initiating a busyout condition. Range is from 1 to 2,147,483,647. |
| grace-period | (Optional) Configures a time limit that the system waits before initiating a busyout condition after the loss of SAA probe
                                          connectivity. |
| seconds | (Optional) Number of seconds for the duration of the grace period. Range is from 30 to 300. |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco 2600 and Cisco 3600 series and on the Cisco MC3810. |
| 12.3(15) | This command was integrated into Cisco IOS Release 12.3(15) and the grace-period keyword and seconds argument were added. |
| 12.4(1) | This command was integrated into Cisco IOS Release 12.4(1). |
| 12.4(2)T | This command was integrated into Cisco IOS Release 12.4(2)T. |

| Caution | The busyout monitor probe command is effective only if the call fallback function is enabled on the source router, and the SAA responder is enabled
                                          on the target router. To enable the call fallback function, you must enter the call fallback active command for the busyout monitor probe command to work. |
|---|---|

| Caution | If thresholds are set too low, the link can alternate between in-service and out-of-service states, causing repeated interruptions
                                          of traffic. |
|---|---|

| Note | To disable the grace-period option, you must first enter the no busyout monitor probe command and then re-enter the busyout monitor probe command without the grace-period option. |
|---|---|

| Command | Description |
|---|---|
| busyout monitor | Places a voice port into the busyout monitor state. |
| call fallback active | Enables the ICMP-ping or SAA (formerly RTR) probe mechanism for use with the dial-peer monitor probe or voice-port busyout monitor probe commands. |
| call fallback threshold delay-loss | Forces a voice port into the busyout state. |
| show voice busyout | Displays information about the voice busyout state. |
| voice class busyout | Creates a voice class for local voice busyout functions. |

| ignore | Specifies the type of ignore procedure, depending on the type of voice port signaling. See the table below for more information. |
|---|---|
| repeat | Specifies the type of repeat procedure, depending on the type of voice port signaling. See the table below for more information. |

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco MC3810. |
| 12.0(7)XK | This command was implemented on the Cisco 2600 and Cisco 3600 series. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |

| Voice Port Signaling Type | Procedure Setting (busyout-option command) | Busyout Actions |
|---|---|---|
| FXS loop start | Default | Removes the power from the loop. For analog voice ports, this is equivalent to removing the ground from the tip lead. For
                                          digital voice ports, the port generates the bit pattern equivalent to removing the ground from the tip lead, or it busies
                                          out if the bit pattern exists. |
| FXS loop start | Ignore | Ignores the ground on the ring lead. |
| FXS ground start | Default | Grounds the tip lead and stays at this state. |
| FXS ground start | Ignore | Leaves the tip lead open. Ignores the ground on the ring lead. |
| FXS ground start | Repeat | Grounds the tip lead. Waits for the far end to close the loop. The far end closes the loop. If the far end then opens the loop, FXS removes the ground from the tip lead. FXS waits for several seconds before returning to Step 1. |
| FXO loop start | Default | Closes the loop and stays at this state. |
| FXO loop start | Ignore | Leaves the loop open. Ignores the ringing current on the ring level. |
| FXO loop start | Repeat | Closes the loop. After the detected far end starts the power denial procedure, FXO opens the loop. After the detected far end has completed the power denial procedure, FXO waits for several seconds before returning to Step
                                                   1. |
| FXO ground start | Default | Grounds the tip lead. |
| FXO ground start | Ignore | Leaves the loop open. Ignores the running current on the ring lead, or the ground current on the tip lead. |
| FXO ground start | Repeat | Grounds the ring lead. Removes the ground from the ring lead and closes the loop after the detected far end grounds the tip lead. When the detected far end removes the ground from tip lead, FXO opens the loop. FXO waits for several seconds before returning to Step 1. |

| Command | Description |
|---|---|
| busyout forced | Forces a voice port into the busyout state. |
| busyout-monitor interface | Configures a voice port to monitor an interface for events that would trigger a voice port busyout. |
| ds0 busyout | Forces a DS0 time slot on a controller into the busyout state. |
| show voice busyout | Displays information about the voice busyout state. |
| voice-port busyout | Places all voice ports associated with a serial or ATM interface into a busyout state. |