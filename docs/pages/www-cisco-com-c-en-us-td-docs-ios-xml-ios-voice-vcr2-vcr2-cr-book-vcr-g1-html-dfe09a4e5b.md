---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr2-vcr2-cr-book-vcr-g1-html-dfe09a4e5b
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr2/vcr2-cr-book/vcr-g1.html
retrieved_at: 2026-08-16T23:13:00.028343+00:00
---

Cisco IOS Voice Command Reference - D through I

# Cisco IOS Voice Command Reference - D through I

Updated: April 25, 2026

Chapter: G

## Chapter: G

# G

## g729 annexb-all

To configure Cisco
                              		  IOS Session Initiation Protocol (SIP) gateway to treat the G.729br8 codec as
                              		  superset of G.729r8 and G.729br8 codecs to interoperate with the Cisco Unified
                              		  Communications Manager, use the g729 annexb-all command in voice service SIP
                              		  configuration mode or voice class tenant configuration mode. To return to the
                              		  default global setting for the gateway, where G.729br8 codec represents only
                              		  the G.729br8 codec, use the no form of this
                              		  command.

g729 annexb-all system

no g729 annexb-all system

### Syntax Description

annexb-all

Specifies
                                          						that the G.729br8 codec is treated as a superset of G.729r8 and G.729br8 codecs
                                          						to communicate with Cisco Unified Communications Manager.

system

Specifies that the codec use the global sip-ua value. This
                                          						keyword is available only for the tenant mode to allow it to fallback to the
                                          						global configurations

### Command Default

G.729br8 codec is
                              		  not viewed as superset of G.729r8 and G.729br8 codecs.

### Command Modes

Voice service SIP configuration (conf-serv-sip)

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.4(15)XZ

This
                                          						command was introduced.

12.4(20)T

This
                                          						command was integrated into Cisco IOS Release 12.4(20)T.

15.6(2)T and IOS XE Denali 16.3.1

This command was modified to include the keyword: system .

Introduced support for YANG models.

### Usage Guidelines

There are four
                              		  variations of the G.729 coder-decoder (codec), which fall into two categories:

High
                                 			 Complexity

G.729
                                    				(g729r8)--a high complexity algorithm codec on which all other G.729 codec
                                    				variations are based.

G.729 Annex-B
                                    				(g729br8 or G.729B)--a variation of the G.729 codec that allows the DSP to
                                    				detect and measure voice activity and convey suppressed noise levels for
                                    				re-creation at the other end. Additionally, the Annex-B codec includes Internet
                                    				Engineering Task Force (IETF) voice activity detection (VAD) and comfort noise
                                    				generation (CNG) functionality.

Medium
                                 			 Complexity

G.729 Annex-A
                                    				(g729ar8 or G.729A)--a variation of the G.729 codec that sacrifices some voice
                                    				quality to lessen the load on the DSP. All platforms that support G.729 also
                                    				support G.729A.

G.729A Annex-B
                                    				(g729abr8 or G.729AB)--a variation of the G.729 Annex-B codec that, like
                                    				G.729B, sacrifices voice quality to lessen the load on the DSP. Additionally,
                                    				the G.729AB codec also includes IETF VAD and CNG functionality.

The VAD and CNG
                              		  functionality is what causes the instability during communication attempts
                              		  between two DSPs where one DSP is configured with Annex-B (G.729B or G.729AB)
                              		  and the other without (G.729 or G.729A). All other combinations interoperate.
                              		  To configure a Cisco IOS SIP gateway for interoperation with Cisco Unified
                              		  Communications Manager (formerly known as the Cisco CallManager, or CCM), use
                              		  the g729-annexb-all command in voice service SIP configuration mode to allow connection of calls
                              		  between two DSPs with incompatible G.729 codecs. Use the voice-class sip g729 annexb-all command in dial peer voice
                              		  configuration mode to configure G.729 codec interoperation settings for a dial
                              		  peer that override global settings for the Cisco IOS SIP gateway.

## Examples

The following
                              		  example configures a Cisco IOS SIP gateway (globally) to be able to connect
                              		  calls between otherwise incompatible G.729 codecs:

```
Router> enable Router# configure terminal Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# g729 annexb-all
```

The following
                              		  example configures a Cisco IOS SIP gateway (globally) to be able to connect
                              		  calls between otherwise incompatible G.729 codecs in the voice class tenant
                              		  configuration mode:

```
Router(config-class)# g729 annexb-all system
```

### Related Commands

Command

Description

voice-class sip g729 annexb-all

Configures an individual dial peer on a Cisco IOS SIP gateway to view a
                                          						G.729br8 codec as superset of G.729r8 and G.729br8 codecs.

## g729-annexb override

To configure settings for G729 codec interoperability and override the default value if annexb attribute is not present. Use
                              the no form of this command to disable this feature.

g729-annexb override

no g729-annexb override

### Syntax Description

override

Overrides the default value, if annexb attribute is not present in g729 codec.

### Command Default

Not enabled by default.

### Command Modes

SIP UA configuration (config-sip-ua).

Voice class tenant configuration (config-class)

## Command History

Release

Modification

Cisco IOS XE 3.11S

Cisco IOS XE Cupertino 17.7.1a

Introduced support for YANG models.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models under voice class tenant configuration
                                          mode.

### Usage Guidelines

The default value of g729-annexb is set to YES. When g729-annexb override is configured under sip-ua mode, the default value
                              of g729-annexb will be set to NO. So, g729-annexb is not negotiated when G729 codec is selected for the call.

## Examples

```
SATYA_2070(config-sip-ua)#g729-annexb override 
SATYA_2070(config-sip-ua)#
```

## g732 ber

To enable G.732 processing and reporting for the E1 controller, use the g732 ber command in controller configuration mode. To disable processing and reporting, use the no form of this command.

g732 ber

no g732 ber

### Syntax Description

This command has no arguments or keywords.

### Command Default

G.732 is disabled.

### Command Modes

Controller configuration (config-controller)

## Command History

Release

Modification

12.2(2)T

This command was introduced on the Cisco 2611.

12.2(15)T

This command was implemented on the Cisco AS5350 and Cisco AS5400 network access server (NAS) platforms.

### Usage Guidelines

By default, G.732 reporting is disabled to prevent a change in E1 behavior for sites that do not want G.732 reporting.

Once ITU-T G.732 is enabled, the E1 controller is placed in the DOWN state if the bit error rate (BER) on the line is greater
                              than 10e-3. The controller is restored to the UP state if the BER drops below 10e-4 for longer than two seconds. When the
                              G.732 alarm is declared, the transmitter sends a remote alarm indication (RAI) yellow alarm.

You can restore ITU-T G.732 functionality by performing a power cycle or a software reload.

## Examples

The following example applies to a Cisco 2611 and shows enabled G.732 processing and reporting for E1 controller 0/0:

```
controller e1 0/0
 g732 ber
```

The following example applies to a Cisco AS5400 with an 8-PRI E1 dial feature card (DFC) in slot 4:

```
controller e1 4/0
 g732 ber
```

### Related Commands

Command

Description

show controllers e1

Displays information about E1 links.

## gatekeeper

To enter gatekeeper configuration mode, use the gatekeeper command in global configuration mode.

gatekeeper

### Syntax Description

This command has no arguments or keywords.

### Command Default

Disabled

### Command Modes

Global configuration (config)

## Command History

Release

Modification

11.3(2)NA

This command was introduced on the Cisco 2500 series and Cisco 3600 series.

12.0(3)T

This command was integrated into Cisco IOS Release 12.0(3)T and implemented on the Cisco MC3810.

### Usage Guidelines

Press Ctrl-Z or use the exit command to exit gatekeeper configuration mode.

## Examples

The following example brings the gatekeeper online:

```
gatekeeper
 no shutdown
```

## gateway

To enable the H.323 VoIP gateway, use the gateway command in global configuration mode. To disable the gateway, use the no form of this command.

gateway

no gateway

### Syntax Description

This command has no arguments or keywords.

### Command Default

The gateway is unregistered

### Command Modes

Global configuration (config)

## Command History

Release

Modification

11.3(6)NA2

This command was introduced on the following platforms: Cisco 3600 series, Cisco AS5300, and Cisco AS5800.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

### Usage Guidelines

Use this command to enable H.323 VoIP gateway functionality. After you enable the gateway, it attempts to discover a gatekeeper
                              by using the H.323 RAS GRQ message. If you enter no gateway voip , the VoIP gateway unregisters with the gatekeeper via the H.323 RAS URQ message.

## Examples

The following example enables the gateway:

```
gateway
```

## gcid

To enable Global Call ID (Gcid) for every call on an outbound leg of a VoIP dial peer for a SIP endpoint, use the gcid command in voice-service configuration mode. To return to the default, use the no form of this command.

gcid

no gcid

### Syntax Description

This command has no arguments or keywords.

### Command Default

Gcid is disabled.

### Command Modes

Voice service configuration (config-voi-serve)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XW2

Cisco Unified CME 4.2

This command was introduced.

12.4(15)XY

Cisco Unified CME 4.2(1)

This command was introduced.

12.4(15)XZ

Cisco Unified CME 4.3

This command was introduced.

12.4(20)T

--

This command was integrated into Cisco IOS Release 12.4(20)T.

Cisco IOS XE Cupertino 17.7.1a

--

Introduced support for YANG models.

### Usage Guidelines

This command in voice-service configuration mode enables Global Call ID (Gcid) in the SIP header for every call on an outbound
                              leg of a VoIP dial peer for a SIP endpoint.

When a call moves around and between the SIP endpoint and the target on a VoIP network because of redirect, transfer, and
                              conference, the SIP Call-ID continues to change. For call control purposes, a unique Gcid is issued for every outbound call
                              leg. A single Gcid remains the same for the same call in the system, and is valid for redirect, transfer, and conference events,
                              including 3-party conferencing when a call center phone acts as a conference host. A SIP header, Cisco_GCID, is added into
                              SIP Invite and REFER requests and to certain other responses to pass the Gcid to the target.

## Examples

The following partial output shows the configuration for the gcid command:

```
router# show running-configuration !
!
!
voice service voip 
 gcid
 callmonitor
 allow-connections h323 to h323
 allow-connections h323 to sip
 allow-connections sip to h323
 allow-connections sip to sip
 no supplementary-service sip moved-temporarily
 sip      
 registrar server expires max 120 min 60
```

## global (application configuration)

To enter application configuration global mode, use the global command in application configuration mode.

global

### Syntax Description

No arguments or keywords

### Command Default

No default behavior or values

### Command Modes

Application configuration

## Command History

Release

Modification

12.3(14)T

This command was introduced.

### Usage Guidelines

Use this command to enter application configuration global mode. You can then configure applications for a dial peer to use
                              for incoming calls when it does not have an explicit application configured.

If an application is defined on the dial peer, that application always takes precedence over the global application configured
                              in application configuration global mode. The applications configured in this mode execute only when a dial peer has no application
                              configured.

## Examples

The following example shows the clid_authen_collect application is configured as the default global application for all inbound
                              dial peers that do not have a specific application configured:

```
application
global
service default clid_authen_collect
```

### Related Commands

Command

Description

call application global

Configures an application to use for incoming calls whose incoming dial peer does not have an explicit application configured.

## groundstart auto-tip

To configure a timing delay on an FXO groundstart voice port, use the groundstart auto-tip command in voice-port configuration mode. To disable the configured timeout, use the no form of this command.

groundstart auto-tip [ delay timer ]

no groundstart auto-tip [ delay timer ]

### Syntax Description

delay

Indicates that a specific delay time will be configured.

timer

Specifies the wait time in milliseconds that the FXO groundstart voice port will wait for a tip ground acknowledgment.

### Command Default

This command is disabled by default. If the command is used without the optional keyword, the default time of 200 ms is activated.

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.3(11)T2

This command was introduced into Cisco IOS Release 12.3(11)T2. This command is not supported on the Cisco 1700 series platform.

### Usage Guidelines

This command should only be used after you encounter call setup problems involving FXO groundstart analog voice ports. If
                              these problems occur, first load the latest image for your Cisco IOS Release (for example, if you are running Release 12.3(11)T,
                              you should replace this image with Release 12.3(11)T2. Upgrading the software image should eliminate the problem. If not,
                              then use this command as a troubleshooting measure--it should be enabled in a configuration only if you encounter problems
                              in connecting outgoing calls. After the groundstart auto-tip command is configured, the problem should not occur again.

Use the groundstart auto-tip command only for voice ports configured for FXO groundstart signaling.

The following example sets the delay wait time for tip ground acknowledgment to 250 ms:

```
Router# configure terminal Router(config)# voice-port 2/0/0 Router(config-voiceport)# shutdown Router(config-voiceport)# groundstart auto-tip delay 250 Router(config-voiceport)# no shutdown Router(config-voiceport)# exit
```

### Related Commands

Command

Description

voice-port

Specifies that a voice port will be used in the connection.

## group

To configure the maximum number of segments that are received in a
                              		  session group or to associate the group with a specified session set, use the group command in backhaul-session-manager configuration mode. To
                              		  restore the default number, use the no form of this command.

group { group-name cumulative ack count | out-of-sequence count | receive count | retransmit count | set set-name }

no group { group-name cumulative ack | out-of-sequence | receive | retransmit | set }

### Syntax Description

group - name

Session-group name.

cumulative ack count

Maximum number of segments received before acknowledgment.
                                          						Range is from 0 to 255. Default is 3 segments.

out - of - sequence count

Maximum number of out-of-sequence segments that can be
                                          						received in a session group before an ACK is sent. Range is from 0 to 255.
                                          						Default is 3 segments.

receive count

Maximum number of segments in the receive window of the
                                          						media gateway. This is the maximum number of segments the media gateway is
                                          						allowed to receive before it sends an ACK. Range is from 1 to 64. Default is 32
                                          						segments.

retransmit count

Maximum number of retransmits allowed in a session group.
                                          						Range is from 0 to 255. Default is 2 retransmits.

set set - name

Session-set name.

### Command Default

For the cumulative ack and out - of - sequence keywords, the default is 3 segments. For the receive keyword, the default is 32 segments. For the retransmit keyword, the default is 2 retransmits. The set keyword has no default behavior or values.

### Command Modes

Backhaul-session-manager configuration (config-bsm)

Caution

Do not change this command or the keywords unless instructed to do so by Cisco technical support. There are relationships
                                          between group parameters that can cause sessions to fail if not set correctly.

## Command History

Release

Modification

12.1(1)T

This command was introduced.

12.2(2)T

This command was implemented on the Cisco 7200 series.

12.2(4)T

This command was implemented on the following platforms:
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release
                                          						12.2(8)T. This command was implemented on the Cisco IAD2420 series. This
                                          						command does not support the access servers in this release.

12.2(11)T

This command was implemented on the following platforms:
                                          						Cisco AS5350, Cisco AS5400, and Cisco AS5850.

## Examples

The following example configures the session group named group5 to
                              		  send an acknowledgment after four segments have been received:

```
group group5 cumulative-ack 4
```

The following example configures the session group named group5 to
                              		  send an acknowledgment after four out-of-sequence segments have been received:

```
group group5 out-of-sequence 4
```

The following example configures the session group named group5 to
                              		  receive a maximum of 10 segments:

```
group group5 receive 10
```

The following example configures the session group named group5 to
                              		  allow as many as 3 retransmits:

```
group group5 retransmit 3
```

The following example associates the session group named group5 with
                              		  the session set named set1:

```
group group5 set set1
```

### Related Commands

Command

Description

group auto-reset

Specifies the maximum number of auto-resets for a session
                                          						group.

group cumulative-ack

Specifies maximum cumulative acknowledgments.

group out-of-sequence

Specifies maximum out-of-sequence segments that are
                                          						received before an EACK is sent.

group receive

Specifies maximum receive segments.

group retransmit

Specifies maximum retransmits.

group timer

Specifies timeouts.

## group auto-reset

To specify the maximum number of auto-resets for a session group, use
                              		  the group auto - reset command in backhaul session manager configuration mode. To
                              		  restore the default number, use the no form of this command.

group group-name auto-reset count

no group group-name auto-reset

### Syntax Description

group - name

Name of session group.

count

Maximum number of auto-resets before the connection is
                                          						considered failed. Range is from 0 to 255. The default is 5.

### Command Default

5 auto-resets

### Command Modes

Backhaul session manager configuration (config-bsm)

## Command History

Release

Modification

12.1(1)T

This command was introduced.

12.2(2)T

This command was implemented on the Cisco 7200.

12.2(4)T

This command was implemented on the following platforms:
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and was implemented on the Cisco IAD2420 series.

12.2(11)T

This command was implemented on the following platforms:
                                          						Cisco AS5350, Cisco AS5400, and Cisco AS5850.

Caution

Do not change the auto-reset number unless instructed to do so by
                                          			 Cisco technical support. There are relationships between group parameters that
                                          			 can cause sessions to fail if not set correctly.

## Examples

The following example specifies a maximum of six auto-resets for the
                              		  session group named "group5":

```
Router(config-bsm)# group group5 auto-reset 6
```

### Related Commands

Command

Description

group cumulative-ack

Configures the maximum number of segments that are received
                                          						in a session group before an acknowledgment is sent.

group out-of-sequence

Configures the maximum out-of-sequence segments that are
                                          						received before an EACK is sent.

group receive

Configures the maximum number of segments in the receive
                                          						window of a session group.

group retransmit

Configures the maximum number of retransmits.

## group cumulative-ack

To configure the maximum number of segments that are received before
                              		  an acknowledgment is sent, use the group cumulative - ack command
                              		  in backhaul session manager configuration mode. To set the value to the
                              		  default, use the no form of this command.

group group-name cumulative-ack count

no group group-name cumulative-ack count

### Syntax Description

group - name

Name of session group.

count

Maximum number of segments that are received before
                                          						acknowledgment. Range is from 0 to 255. The default is 3.

### Command Default

3 segments

### Command Modes

Backhaul session manager configuration (config-bsm)

## Command History

Release

Modification

12.1(1)T

This command was introduced.

12.2(2)T

This command was implemented on the Cisco 7200 series.

12.2(4)T

This command was implemented on the following platforms:
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series.

12.2(8)T

This command was implemented on the Cisco IAD2420 series.

12.2(11)T

This command was implemented on the following platforms:
                                          						Cisco AS5350, Cisco AS5400, and Cisco AS5850.

Caution

Do not change this parameter unless instructed to do so by Cisco
                                          			 technical support. Incorrectly set parameters can cause sessions to fail.

## Examples

The following example sets the cumulative acknowledgment maximum to 4
                              		  for the group named "group1":

```
Router(config-bsm)# group group5 cumulative-ack 4
```

### Related Commands

Command

Description

group auto-reset

Configures the maximum auto-reset value.

group out-of-sequence

Configures the maximum number of out-of-sequence segments
                                          						that are received before an EACK is sent.

group receive

Configures the maximum number of receive segments.

group retransmit

Configures the maximum number of retransmits.

## group out-of-sequence

To configure the maximum number of out-of-sequence segments that are
                              		  received before an error acknowledgement (EACK) is sent, use the group out - of - sequence command in backhaul session manager configuration mode. To set the value to the
                              		  default, use the no form of this command.

group group-name out-of-sequence count

no group group-name out-of-sequence count

### Syntax Description

group-name

Name of the session group.

count

Maximum number of out-of-sequence segments. Range is from 0
                                          						to 255. The default is 3.

### Command Default

3 segments

### Command Modes

Backhaul session manager configuration (config-bsm)

## Command History

Release

Modification

12.1(1)T

This command was introduced.

12.2(2)T

This command was implemented on the Cisco 7200 series.

12.2(4)T

This command was implemented on the following platforms:
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series.

12.2(8)T

This command was implemented on the Cisco IAD2420 series.

12.2(11)T

This command was implemented on the following platforms:
                                          						Cisco AS5350, Cisco AS5400, and Cisco AS5850.

Caution

Do not change this parameter unless instructed to do so by Cisco
                                          			 technical support. Incorrectly set parameters can cause sessions to fail.

## Examples

The following example sets the out-of-sequence maximum to 4 for the
                              		  group named "group5":

```
Router(config-bsm)# group group5 out-of-sequence 4
```

### Related Commands

Command

Description

group auto-reset

Configures the maximum auto-reset value.

group cumulative-ack

Configures the maximum number of cumulative
                                          						acknowledgments.

group receive

Configures the maximum number of receive segments.

group retransmit

Configures the maximum number of retransmits.

## group receive

To configure the maximum number of receive segments, use the group receive command in backhaul session manager
                              		  configuration mode. To set the value to the default, use the no form of this command.

group group-name receive count

no group group-name receive count

### Syntax Description

group - name

Name of the session group.

count

Maximum number of segments in a receive window. The far end
                                          						should send no more than this number of segments before receiving an
                                          						acknowledgment for the oldest outstanding segment. Range is 1 to 64. The
                                          						default is 32.

### Command Default

32 segments

### Command Modes

Backhaul session manager configuration

Caution

Do not change this parameter unless instructed to do so by Cisco
                                          			 technical support. Incorrectly set parameters can cause sessions to fail.

## Command History

Release

Modification

12.1(1)T

This command was introduced.

12.2(2)T

This command was implemented on the Cisco 7200 series.

12.2(4)T

This command was implemented on the following platforms:
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series.

12.2(8)T

This command was implemented on the Cisco IAD2420 series.

12.2(11)T

This command was implemented on the following platforms:
                                          						Cisco AS5350, Cisco AS5400, and Cisco AS5850.

## Examples

The following example sets the receive maximum to 10 for the group
                              		  named "group5":

```
Router(config-bsm)# group group5 receive 10
```

### Related Commands

Command

Description

group auto-reset

Configures the maximum auto-reset value.

group cumulative-ack

Configures the maximum number of cumulative
                                          						acknowledgments.

group out-of-sequence

Configures the maximum number of out-of-sequence segments
                                          						that are received before an EACK is sent.

group retransmit

Configures the maximum number of retransmits.

## group retransmit

To configure the maximum number of retransmits, use the group retransmit command in backhaul session manager
                              		  configuration mode. To set the value to the default, use the no form of this command.

group group-name retransmit count

no group group-name retransmit count

### Syntax Description

group - name

Name of the session group.

count

Maximum number of retransmits. Range is 0 to 255. The
                                          						default is 2.

### Command Modes

2 retransmits

### Command Modes

Backhaul session manager configuration (config-bsm)

## Command History

Release

Modification

12.1(1)T

This command was introduced.

12.2(2)T

This command was implemented on the Cisco 7200 series.

12.2(4)T

This command was implemented on the following platforms:
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series.

12.2(8)T

This command was implemented on the Cisco IAD2420 series.

12.2(11)T

This command was implemented on the following platforms:
                                          						Cisco AS5350, Cisco AS5400, and Cisco AS5850.

Caution

Do not change this parameter unless instructed to do so by Cisco
                                          			 technical support. Incorrectly set parameters can cause sessions to fail.

## Examples

The following example sets the retransmit maximum to 3 for the group
                              		  named "group5":

```
Router(config-bsm)# group group5 retrans 3
```

### Related Commands

Command

Description

group auto-reset

Configures the maximum auto-reset value.

group cumulative-ack

Configures the maximum number of cumulative
                                          						acknowledgments.

group out-of-sequence

Configures the maximum number of out-of-sequence segments
                                          						that are received before an EACK is sent.

group receive

Configures the maximum number of receive segments.

## group set

To create a session group and associate it with a specified session set, use the group command in backhaul session manager configuration mode. To delete the group, use the no form of this command.

group grp-name set set-name

no group grp-name

### Syntax Description

grp - name

Name of the session group.

set - name

Name of the session set.

### Command Default

No default behavior or values

### Command Modes

Backhaul session manager configuration

## Command History

Release

Modification

12.1(1)T

This command was introduced on the Cisco AS5300.

12.2(4)T

This command was implemented on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and was implemented on the Cisco IAD2420 series.

## Examples

The following example shows session group group5 being associated with session set set1 :

```
Router(config-bsm)# group group5 set set1
```

### Related Commands

Command

Description

group auto-reset

Specifies the maximum number of auto-resets for a session group.

group cumulative-ack

Configures the maximum number of segments that are received in a session group before an acknowledgment is sent.

group out-of-sequence

Configures the maximum out-of-sequence segments that are received before an EACK is sent.

group receive

Configures the maximum number of segments in the receive window of a session group.

group retransmit

Configures the maximum number of retransmits.

group timer cumulative-ack

Configures cumulative acknowledgment timeout.

group timer keepalive

Configures keepalive (or null segment) timeout.

group timer retransmit

Configures retransmission timeout.

group timer transfer

Configures state transfer timeout.

## group timer

To configure the maximum number of milliseconds for which the
                              		  Reliable User Datagram Protocol (RUDP) delays before sending an acknowledgment
                              		  for a received segment, sending a keepalive segment, retransmitting a segment,
                              		  or transferring a segment, use the group timer command in backhaul-session-manager configuration mode. To
                              		  restore the default values, use the no form of this command.

group group-name timer { cumulative ack time | keepalive time | retransmit t ime | transfer time }

no group group-name timer cumulative ack

### Syntax Description

group - name

Name of session group.

cumulative ack time

Number of milliseconds for which RUDP delays before sending
                                          						an acknowledgment for a received segment. Range is 100 to 65535. The default is
                                          						100.

keepalive time

Number of milliseconds before RUDP sends a keepalive
                                          						segment when no RUDP packets are received or sent. Range is 100 to 65535. The
                                          						default is 1000.

retransmit time

Number of milliseconds for which RUDP waits before
                                          						retransmitting the segment. Range is 100 to 65535. The default is 300.

transfer time

Number of milliseconds for which RUDP waits to receive a
                                          						selection of a new session from the application during a transfer state. Range
                                          						is 0 to 65535. The default is 2000.

### Command Default

cumulative ack : 100
                              		  milliseconds keepalive : 1000
                              		  milliseconds retransmit: 300 milliseconds transfer : 2000
                              		  milliseconds

### Command Modes

Backhaul-session-manager configuration (config-bsm)

Caution

Do not change the group timer parameters unless instructed to do so
                                          			 by Cisco technical support. There are relationships between group parameters
                                          			 that can cause sessions to fail if not set correctly.

## Command History

Release

Modification

12.1(1)T

This command was introduced.

12.2(2)T

This command was implemented on the Cisco 7200 series.

12.2(4)T

This command was implemented on the following platforms:
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and was implemented on the Cisco IAD2420 series.

12.2(11)T

This command was implemented on the following platforms:
                                          						Cisco AS5350, Cisco AS5400, and Cisco AS5850.

### Usage Guidelines

The retransmit timer must be greater than the cumulative-ack timer.

Cumulative acknowledgment timeout is the maximum number of
                              		  milliseconds for which RUDP delays before sending an acknowledgment for a
                              		  received segment.

## Examples

The following example specifies 325 milliseconds as the maximum
                              		  acknowledgment delay for the session group named "group5":

```
group group5 timer cumulative-ack 325
```

The following example configures RUDP to send keepalive segments if
                              		  no RUDP packets are received or sent for 2.5 seconds (2500 milliseconds) in the
                              		  session group named "group5".

```
group group5 timer keepalive 2500
```

The following example sets a retransmit time of 650 milliseconds for
                              		  the session group named "group5":

```
group group5 timer retransmit 650
```

### Related Commands

Command

Description

group

Specifies the maximum number of segments that are received
                                          						in a session group.

## group-params

To define groups of parameters that can be used by applications, use the group-params command in application configuration mode. There is no no form of the command.

group-params groupname

### Syntax Description

groupname

Name of the parameter group that you are creating.

### Command Default

No default behavior or values

### Command Modes

Application configuration

## Command History

Release

Modification

12.3(14)T

This command was introduced.

### Usage Guidelines

This command allows you to define groups of parameters so that a group of parameters can be used by multiple services or packages
                              (applications). Parameter groups are defined globally and once a group is defined, it is available for another service or
                              package to use. Groups can contain parameters under multiple parameterspaces. In cases where a parameter is defined individually
                              and in a parameter group, the individual parameter definition is given precedence.

## Examples

The following example shows a parameter group named "fax," that contains two parameters:

```
application
group-params fax
  paramspace fax_detect2 pin-len 9
  paramspace fax_detect1 retry-count 9
```

## gw-accounting

To enable an accounting method for collecting call detail records (CDRs), use the gw-accounting command in global configuration mode. To disable an accounting method, use the no form of this command.

gw-accounting { aaa | file | syslog [ stats ]}

no gw-accounting { aaa | file | syslog [ stats ]}

### Syntax Description

aaa

Enables accounting through the AAA system and sends call detail records to the RADIUS server in the form of vendor-specific
                                          attributes (VSAs).

file

Enables the file accounting method to store call detail records in .csv format.

syslog

Enables the system logging facility to output accounting information in the form of a system log message.

stats

(Optional) Enables voice quality statistics to be sent to the system log.

voip

Enables generic gateway-specific accounting.

### Command Default

No accounting method is enabled.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

11.3(6)NA2

This command was introduced.

12.0(7)T

This command was integrated into Cisco IOS Release 12.0(7)T. The vsa keyword was added.

12.1(1)T

The voip keyword was added.

12.2(11)T

The h323 , vsa , and voip keywords were replaced by the aaa keyword.

12.4(11)XW

The stats keyword was added.

12.4(15)XY

The file keyword was added.

12.4(20)T

This command was integrated into Cisco IOS Release 12.4(20)T.

Cisco IOS XE Cupertino
                                                17.9.1a

Allows transfer of CUBE CDRs using SFTP.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

This command enables you to output accounting data in one of the following ways:

Using RADIUS Vendor-Specific Attributes

The IETF draft standard specifies a method for communicating vendor-specific information between the network access server
                              and the RADIUS server by using the vendor-specific attribute (attribute 26). Vendor-specific attributes (VSAs) allow vendors
                              to support their own extended attributes not appropriate for general use. The Cisco RADIUS implementation supports one vendor-specific
                              option using the format recommended in the specification. The Cisco vendor ID is 9, and the supported option has vendor-type
                              1, which is named "cisco-avpair." The value is a string of the format:

```
protocol: attribute sep value *
```

"Protocol" is a value of the Cisco "protocol" attribute for a particular type of authorization. "Attribute" and "value" are
                              an appropriate attribute-value (AV) pair defined in the Cisco TACACS+ specification, and "sep" is "=" for mandatory attributes
                              and "*" for optional attributes. This allows the full set of features available for TACACS+ authorization to also be used
                              for RADIUS. For a list of VSA fields and their ASCII values, see the >Cisco IOS Security Configuration Guide for your Cisco IOS release.

Use the gw-accounting aaa command to enable the VSA method of accounting.

Using File Format

This method stores CDRs in comma separated values (CSV) format. These CDR records can be stored in a file on external or
                              internal flash or on a file on a FTP or SFTP server.

Each CDR has a fixed number of fields whose names and position order are predefined. Ten generic fields capture feature-related
                              information. The CDR has feature fields representing the basic feature and feature fields representing the supplementary services.

Use the gw-accounting file command to enable the .csv file method of accounting.

Using syslog Records

The syslog accounting option exports the information elements associated with each call leg through a system log message,
                              which can be captured by a syslog daemon on the network. The syslog output consists of the following:

```
<server timestamp> <gateway id> <message number> : <message label> : <list of AV pairs>
```

Use the gw-accounting syslog command to enable the syslog method of gathering accounting data.

The table below describes the syslog message fields.

Field

Description

server timestamp

Time stamp created by the server when it receives the message to log.

gateway id

Name of the gateway that sends the message.

message number

Number assigned to the message by the gateway.

message label

String used to identify the message category.

list of AV pairs

String that consists of <attribute name> <attribute value> pairs separated by commas.

You can enable aaa , file , or syslog simultaneously; call detail records are generated using all methods that you enable.

Overloading the Acct-Session-ID field

Attributes that cannot be mapped to standard RADIUS are packed into the Acct-Session-ID field as ASCII strings separated
                              by the character "/". The Acct-Session-ID attribute definition contains the RADIUS account session ID, which is a unique identifier
                              that links accounting records associated with the same login session for a user. To support additional fields, the following
                              string format is defined for this field:

```
<session id>/<call leg setup time>/<gateway id>/<connection id>/<call origin>/
<call type>/<connect time>/<disconnect time>/<disconnect cause>/<remote ip address>
```

The table below describes the field attributes that are used with the overloaded acct-session-ID method.

Field Attribute

Description

Session-Id

Standard RADIUS account session ID.

Setup-Time

Q.931 setup time for this connection in Network Time Protocol (NTP) format: hour, minutes, seconds, milliseconds, time zone,
                                          day of week, month, day of month, and year.

Gateway-Id

Name of the underlying gateway in the form "gateway.domain_name."

Call-Origin

Origin of the call relative to the gateway. Possible values are originate and answer .

Call-Type

Call leg type. Possible values are telephony and VoIP .

Connection-Id

Unique global identifier used to correlate call legs that belong to the same end-to-end call. The field consists of 4 long
                                          words (128 bits). Each long word displays as a hexadecimal value separated by a space character.

Connect-Time

Q.931 connect time for this call leg, in NTP format.

Disconnect-Time

Q.931 disconnect time for this call leg, in NTP format.

Disconnect-Cause

Reason that a call was taken offline as defined in the Q.931 specification.

Remote-Ip-Address

Address of the remote gateway port where the call is connected.

Because of the limited size of the Acct-Session-ID string, it is impossible to include many information elements in it. Therefore,
                              this feature supports only a limited set of accounting information elements.

Use the attribute acct-session-id overloaded command to configure the overloaded session ID method of applying H.323 gateway-specific accounting.

## Examples

The following example shows accounting enabled using RADIUS VSA attributes:

```
gw-accounting aaa
```

The following example shows accounting enabled using the syslog method:

```
gw-accounting syslog
```

The following example shows accounting enabled using the file method.

From Cisco IOS XE Cupertino
                                    17.9.1a onwards, CUBE allows CDR transfer using SFTP:

```
Router# show running-config | section gw-accounting
gw-accounting file
 primary sftp [2001:420:54ff:13::312:175]//cdrtest username bob password 6 P^AV^_3
 secondary ifs flash:cdrtest2
 maximum buffer-size 15
 maximum retry-count 3
 maximum fileclose-timer 300
 maximum cdrflush-timer 245
 cdr-format compact
```

### Related Commands

Command

Description

acct-template

Selects a group of voice accounting attributes to collect.

attribute acct-session-id overloaded

Overloads the acct-session-id attribute with call detail records.

radius-server vsa send

Enables the voice gateway to recognize and use VSAs.

## gw-type-prefix

To configure a technology prefix in the gatekeeper, use the gw-type-prefix command in gatekeeper configuration mode. To remove the technology prefix, use the no form of this command.

gw-type-prefix type-prefix [ [ hopoff gkid1 ] [ hopoff gkid2 ] [ hopoff gkidn ] [ seq | blast ]] [ default-technology ] [ gw ipaddr ipaddr [port] ]

no gw-type-prefix type-prefix [ [ hopoff gkid1 ] [ hopoff gkid2 ] [ hopoff gkidn ] [ seq | blast ]] [ default-technology ] [ gw ipaddr ipaddr [port] ]

### Syntax Description

type - prefix

A technology prefix is recognized and is stripped before checking for the zone prefix. It is strongly recommended that you
                                          select technology prefixes that do not lead to ambiguity with zone prefixes. Do this by using the # character to terminate
                                          technology prefixes, for example, 3#.

hopoff gkid

(Optional) Use this option to specify the gatekeeper where the call is to hop off, regardless of the zone prefix in the destination
                                          address. The gkid argument refers to a gatekeeper previously configured using the zone local or zone remote comment. You can enter this keyword
                                          and argument multiple times to configure redundant gatekeepers for a given technology prefix.

seq | blast

(Optional) If you list multiple hopoffs, this indicates that the LRQs should be sent sequentially or simultaneously (blast)
                                          to the gatekeepers according to the order in which they were listed. The default is to send them sequentially.

default-technology

(Optional) Gateways registering with this prefix option are used as the default for routing any addresses that are otherwise
                                          unresolved.

gw ipaddr ipaddr [ port ]

(Optional) Use this option to indicate that the gateway is incapable of registering technology prefixes. When it registers,
                                          it adds the gateway to the group for this type prefix, just as if it had sent the technology prefix in its registration. This
                                          parameter can be repeated to associate more than one gateway with a technology prefix.

### Command Default

By default, no technology prefix is defined, and LRQs are sent sequentially to all the gatekeepers listed.

### Command Modes

Gatekeeper configuration (config-gk)

## Command History

Release

Modification

11.3(6)NA2

This command was introduced on the following platforms: Cisco 2500 series, Cisco 3600 series, and Cisco AS5300.

12.1(1)T

This command was integrated into Cisco IOS Release 12.1(1)T. This command was modified to allow the user to specify multiple
                                          hopoffs.

12.1(2)T

This command was modified to allow the user to specify whether LRQs should be sent simultaneously or sequentially to the gatekeepers.

12.2(11)T

This command was implemented on the following platforms: Cisco 2600 series, Cisco MC3810, and Cisco 7200 series.

### Usage Guidelines

More than one gateway can register with the same technology prefix. In such cases, a random selection is made of one of them.

You do not have to define a technology prefix to a gatekeeper if there are gateways configured to register with that prefix
                              and if there are no special flags ( hopoff gkid or default-technology ) that you want to associate with that prefix.

You need to configure the gateway type prefix of all remote technology prefixes that are routed through this gatekeeper.

## Examples

The following example defines two gatekeepers for technology zone 3:

```
gw-type-prefix 3#* hopoff c2600-1-gk hopoff c2514-1-gk
```

### Related Commands

Command

Description

show gatekeeper gw-type-prefix

Displays the list of currently defined technology zones and the gatekeepers responsible for each.

zone prefix

Configures the gatekeeper with knowledge of its own prefix and the prefix of any remote zone.

| annexb-all | Specifies
                                          						that the G.729br8 codec is treated as a superset of G.729r8 and G.729br8 codecs
                                          						to communicate with Cisco Unified Communications Manager. |
|---|---|
| system | Specifies that the codec use the global sip-ua value. This
                                          						keyword is available only for the tenant mode to allow it to fallback to the
                                          						global configurations |

| Release | Modification |
|---|---|
| 12.4(15)XZ | This
                                          						command was introduced. |
| 12.4(20)T | This
                                          						command was integrated into Cisco IOS Release 12.4(20)T. |
| 15.6(2)T and IOS XE Denali 16.3.1 | This command was modified to include the keyword: system . |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Command | Description |
|---|---|
| voice-class sip g729 annexb-all | Configures an individual dial peer on a Cisco IOS SIP gateway to view a
                                          						G.729br8 codec as superset of G.729r8 and G.729br8 codecs. |

| override | Overrides the default value, if annexb attribute is not present in g729 codec. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE 3.11S | The command was introduced. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models under voice class tenant configuration
                                          mode. |

| Release | Modification |
|---|---|
| 12.2(2)T | This command was introduced on the Cisco 2611. |
| 12.2(15)T | This command was implemented on the Cisco AS5350 and Cisco AS5400 network access server (NAS) platforms. |

| Command | Description |
|---|---|
| show controllers e1 | Displays information about E1 links. |

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced on the Cisco 2500 series and Cisco 3600 series. |
| 12.0(3)T | This command was integrated into Cisco IOS Release 12.0(3)T and implemented on the Cisco MC3810. |

| Release | Modification |
|---|---|
| 11.3(6)NA2 | This command was introduced on the following platforms: Cisco 3600 series, Cisco AS5300, and Cisco AS5800. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XW2 | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | -- | This command was integrated into Cisco IOS Release 12.4(20)T. |
| Cisco IOS XE Cupertino 17.7.1a | -- | Introduced support for YANG models. |

| Release | Modification |
|---|---|
| 12.3(14)T | This command was introduced. |

| Command | Description |
|---|---|
| call application global | Configures an application to use for incoming calls whose incoming dial peer does not have an explicit application configured. |

| delay | Indicates that a specific delay time will be configured. |
|---|---|
| timer | Specifies the wait time in milliseconds that the FXO groundstart voice port will wait for a tip ground acknowledgment. |

| Release | Modification |
|---|---|
| 12.3(11)T2 | This command was introduced into Cisco IOS Release 12.3(11)T2. This command is not supported on the Cisco 1700 series platform. |

| Command | Description |
|---|---|
| voice-port | Specifies that a voice port will be used in the connection. |

| group - name | Session-group name. |
|---|---|
| cumulative ack count | Maximum number of segments received before acknowledgment.
                                          						Range is from 0 to 255. Default is 3 segments. |
| out - of - sequence count | Maximum number of out-of-sequence segments that can be
                                          						received in a session group before an ACK is sent. Range is from 0 to 255.
                                          						Default is 3 segments. |
| receive count | Maximum number of segments in the receive window of the
                                          						media gateway. This is the maximum number of segments the media gateway is
                                          						allowed to receive before it sends an ACK. Range is from 1 to 64. Default is 32
                                          						segments. |
| retransmit count | Maximum number of retransmits allowed in a session group.
                                          						Range is from 0 to 255. Default is 2 retransmits. |
| set set - name | Session-set name. |

| Caution | Do not change this command or the keywords unless instructed to do so by Cisco technical support. There are relationships
                                          between group parameters that can cause sessions to fail if not set correctly. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced. |
| 12.2(2)T | This command was implemented on the Cisco 7200 series. |
| 12.2(4)T | This command was implemented on the following platforms:
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. This command was implemented on the Cisco IAD2420 series. This
                                          						command does not support the access servers in this release. |
| 12.2(11)T | This command was implemented on the following platforms:
                                          						Cisco AS5350, Cisco AS5400, and Cisco AS5850. |

| Command | Description |
|---|---|
| group auto-reset | Specifies the maximum number of auto-resets for a session
                                          						group. |
| group cumulative-ack | Specifies maximum cumulative acknowledgments. |
| group out-of-sequence | Specifies maximum out-of-sequence segments that are
                                          						received before an EACK is sent. |
| group receive | Specifies maximum receive segments. |
| group retransmit | Specifies maximum retransmits. |
| group timer | Specifies timeouts. |

| group - name | Name of session group. |
|---|---|
| count | Maximum number of auto-resets before the connection is
                                          						considered failed. Range is from 0 to 255. The default is 5. |

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced. |
| 12.2(2)T | This command was implemented on the Cisco 7200. |
| 12.2(4)T | This command was implemented on the following platforms:
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and was implemented on the Cisco IAD2420 series. |
| 12.2(11)T | This command was implemented on the following platforms:
                                          						Cisco AS5350, Cisco AS5400, and Cisco AS5850. |

| Caution | Do not change the auto-reset number unless instructed to do so by
                                          			 Cisco technical support. There are relationships between group parameters that
                                          			 can cause sessions to fail if not set correctly. |
|---|---|

| Command | Description |
|---|---|
| group cumulative-ack | Configures the maximum number of segments that are received
                                          						in a session group before an acknowledgment is sent. |
| group out-of-sequence | Configures the maximum out-of-sequence segments that are
                                          						received before an EACK is sent. |
| group receive | Configures the maximum number of segments in the receive
                                          						window of a session group. |
| group retransmit | Configures the maximum number of retransmits. |

| group - name | Name of session group. |
|---|---|
| count | Maximum number of segments that are received before
                                          						acknowledgment. Range is from 0 to 255. The default is 3. |

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced. |
| 12.2(2)T | This command was implemented on the Cisco 7200 series. |
| 12.2(4)T | This command was implemented on the following platforms:
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series. |
| 12.2(8)T | This command was implemented on the Cisco IAD2420 series. |
| 12.2(11)T | This command was implemented on the following platforms:
                                          						Cisco AS5350, Cisco AS5400, and Cisco AS5850. |

| Caution | Do not change this parameter unless instructed to do so by Cisco
                                          			 technical support. Incorrectly set parameters can cause sessions to fail. |
|---|---|

| Command | Description |
|---|---|
| group auto-reset | Configures the maximum auto-reset value. |
| group out-of-sequence | Configures the maximum number of out-of-sequence segments
                                          						that are received before an EACK is sent. |
| group receive | Configures the maximum number of receive segments. |
| group retransmit | Configures the maximum number of retransmits. |

| group-name | Name of the session group. |
|---|---|
| count | Maximum number of out-of-sequence segments. Range is from 0
                                          						to 255. The default is 3. |

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced. |
| 12.2(2)T | This command was implemented on the Cisco 7200 series. |
| 12.2(4)T | This command was implemented on the following platforms:
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series. |
| 12.2(8)T | This command was implemented on the Cisco IAD2420 series. |
| 12.2(11)T | This command was implemented on the following platforms:
                                          						Cisco AS5350, Cisco AS5400, and Cisco AS5850. |

| Caution | Do not change this parameter unless instructed to do so by Cisco
                                          			 technical support. Incorrectly set parameters can cause sessions to fail. |
|---|---|

| Command | Description |
|---|---|
| group auto-reset | Configures the maximum auto-reset value. |
| group cumulative-ack | Configures the maximum number of cumulative
                                          						acknowledgments. |
| group receive | Configures the maximum number of receive segments. |
| group retransmit | Configures the maximum number of retransmits. |

| group - name | Name of the session group. |
|---|---|
| count | Maximum number of segments in a receive window. The far end
                                          						should send no more than this number of segments before receiving an
                                          						acknowledgment for the oldest outstanding segment. Range is 1 to 64. The
                                          						default is 32. |

| Caution | Do not change this parameter unless instructed to do so by Cisco
                                          			 technical support. Incorrectly set parameters can cause sessions to fail. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced. |
| 12.2(2)T | This command was implemented on the Cisco 7200 series. |
| 12.2(4)T | This command was implemented on the following platforms:
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series. |
| 12.2(8)T | This command was implemented on the Cisco IAD2420 series. |
| 12.2(11)T | This command was implemented on the following platforms:
                                          						Cisco AS5350, Cisco AS5400, and Cisco AS5850. |

| Command | Description |
|---|---|
| group auto-reset | Configures the maximum auto-reset value. |
| group cumulative-ack | Configures the maximum number of cumulative
                                          						acknowledgments. |
| group out-of-sequence | Configures the maximum number of out-of-sequence segments
                                          						that are received before an EACK is sent. |
| group retransmit | Configures the maximum number of retransmits. |

| group - name | Name of the session group. |
|---|---|
| count | Maximum number of retransmits. Range is 0 to 255. The
                                          						default is 2. |

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced. |
| 12.2(2)T | This command was implemented on the Cisco 7200 series. |
| 12.2(4)T | This command was implemented on the following platforms:
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series. |
| 12.2(8)T | This command was implemented on the Cisco IAD2420 series. |
| 12.2(11)T | This command was implemented on the following platforms:
                                          						Cisco AS5350, Cisco AS5400, and Cisco AS5850. |

| Caution | Do not change this parameter unless instructed to do so by Cisco
                                          			 technical support. Incorrectly set parameters can cause sessions to fail. |
|---|---|

| Command | Description |
|---|---|
| group auto-reset | Configures the maximum auto-reset value. |
| group cumulative-ack | Configures the maximum number of cumulative
                                          						acknowledgments. |
| group out-of-sequence | Configures the maximum number of out-of-sequence segments
                                          						that are received before an EACK is sent. |
| group receive | Configures the maximum number of receive segments. |

| grp - name | Name of the session group. |
|---|---|
| set - name | Name of the session set. |

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced on the Cisco AS5300. |
| 12.2(4)T | This command was implemented on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and was implemented on the Cisco IAD2420 series. |

| Command | Description |
|---|---|
| group auto-reset | Specifies the maximum number of auto-resets for a session group. |
| group cumulative-ack | Configures the maximum number of segments that are received in a session group before an acknowledgment is sent. |
| group out-of-sequence | Configures the maximum out-of-sequence segments that are received before an EACK is sent. |
| group receive | Configures the maximum number of segments in the receive window of a session group. |
| group retransmit | Configures the maximum number of retransmits. |
| group timer cumulative-ack | Configures cumulative acknowledgment timeout. |
| group timer keepalive | Configures keepalive (or null segment) timeout. |
| group timer retransmit | Configures retransmission timeout. |
| group timer transfer | Configures state transfer timeout. |

| group - name | Name of session group. |
|---|---|
| cumulative ack time | Number of milliseconds for which RUDP delays before sending
                                          						an acknowledgment for a received segment. Range is 100 to 65535. The default is
                                          						100. |
| keepalive time | Number of milliseconds before RUDP sends a keepalive
                                          						segment when no RUDP packets are received or sent. Range is 100 to 65535. The
                                          						default is 1000. |
| retransmit time | Number of milliseconds for which RUDP waits before
                                          						retransmitting the segment. Range is 100 to 65535. The default is 300. |
| transfer time | Number of milliseconds for which RUDP waits to receive a
                                          						selection of a new session from the application during a transfer state. Range
                                          						is 0 to 65535. The default is 2000. |

| Caution | Do not change the group timer parameters unless instructed to do so
                                          			 by Cisco technical support. There are relationships between group parameters
                                          			 that can cause sessions to fail if not set correctly. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced. |
| 12.2(2)T | This command was implemented on the Cisco 7200 series. |
| 12.2(4)T | This command was implemented on the following platforms:
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and was implemented on the Cisco IAD2420 series. |
| 12.2(11)T | This command was implemented on the following platforms:
                                          						Cisco AS5350, Cisco AS5400, and Cisco AS5850. |

| Command | Description |
|---|---|
| group | Specifies the maximum number of segments that are received
                                          						in a session group. |

| groupname | Name of the parameter group that you are creating. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(14)T | This command was introduced. |

| aaa | Enables accounting through the AAA system and sends call detail records to the RADIUS server in the form of vendor-specific
                                          attributes (VSAs). |
|---|---|
| file | Enables the file accounting method to store call detail records in .csv format. |
| syslog | Enables the system logging facility to output accounting information in the form of a system log message. |
| stats | (Optional) Enables voice quality statistics to be sent to the system log. |
| voip | Enables generic gateway-specific accounting. |

| Release | Modification |
|---|---|
| 11.3(6)NA2 | This command was introduced. |
| 12.0(7)T | This command was integrated into Cisco IOS Release 12.0(7)T. The vsa keyword was added. |
| 12.1(1)T | The voip keyword was added. |
| 12.2(11)T | The h323 , vsa , and voip keywords were replaced by the aaa keyword. |
| 12.4(11)XW | The stats keyword was added. |
| 12.4(15)XY | The file keyword was added. |
| 12.4(20)T | This command was integrated into Cisco IOS Release 12.4(20)T. |
| Cisco IOS XE Cupertino
                                                17.9.1a | Allows transfer of CUBE CDRs using SFTP. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Field | Description |
|---|---|
| server timestamp | Time stamp created by the server when it receives the message to log. |
| gateway id | Name of the gateway that sends the message. |
| message number | Number assigned to the message by the gateway. |
| message label | String used to identify the message category. |
| list of AV pairs | String that consists of <attribute name> <attribute value> pairs separated by commas. |

| Field Attribute | Description |
|---|---|
| Session-Id | Standard RADIUS account session ID. |
| Setup-Time | Q.931 setup time for this connection in Network Time Protocol (NTP) format: hour, minutes, seconds, milliseconds, time zone,
                                          day of week, month, day of month, and year. |
| Gateway-Id | Name of the underlying gateway in the form "gateway.domain_name." |
| Call-Origin | Origin of the call relative to the gateway. Possible values are originate and answer . |
| Call-Type | Call leg type. Possible values are telephony and VoIP . |
| Connection-Id | Unique global identifier used to correlate call legs that belong to the same end-to-end call. The field consists of 4 long
                                          words (128 bits). Each long word displays as a hexadecimal value separated by a space character. |
| Connect-Time | Q.931 connect time for this call leg, in NTP format. |
| Disconnect-Time | Q.931 disconnect time for this call leg, in NTP format. |
| Disconnect-Cause | Reason that a call was taken offline as defined in the Q.931 specification. |
| Remote-Ip-Address | Address of the remote gateway port where the call is connected. |

| Command | Description |
|---|---|
| acct-template | Selects a group of voice accounting attributes to collect. |
| attribute acct-session-id overloaded | Overloads the acct-session-id attribute with call detail records. |
| radius-server vsa send | Enables the voice gateway to recognize and use VSAs. |

| type - prefix | A technology prefix is recognized and is stripped before checking for the zone prefix. It is strongly recommended that you
                                          select technology prefixes that do not lead to ambiguity with zone prefixes. Do this by using the # character to terminate
                                          technology prefixes, for example, 3#. |
|---|---|
| hopoff gkid | (Optional) Use this option to specify the gatekeeper where the call is to hop off, regardless of the zone prefix in the destination
                                          address. The gkid argument refers to a gatekeeper previously configured using the zone local or zone remote comment. You can enter this keyword
                                          and argument multiple times to configure redundant gatekeepers for a given technology prefix. |
| seq \| blast | (Optional) If you list multiple hopoffs, this indicates that the LRQs should be sent sequentially or simultaneously (blast)
                                          to the gatekeepers according to the order in which they were listed. The default is to send them sequentially. |
| default-technology | (Optional) Gateways registering with this prefix option are used as the default for routing any addresses that are otherwise
                                          unresolved. |
| gw ipaddr ipaddr [ port ] | (Optional) Use this option to indicate that the gateway is incapable of registering technology prefixes. When it registers,
                                          it adds the gateway to the group for this type prefix, just as if it had sent the technology prefix in its registration. This
                                          parameter can be repeated to associate more than one gateway with a technology prefix. |

| Release | Modification |
|---|---|
| 11.3(6)NA2 | This command was introduced on the following platforms: Cisco 2500 series, Cisco 3600 series, and Cisco AS5300. |
| 12.1(1)T | This command was integrated into Cisco IOS Release 12.1(1)T. This command was modified to allow the user to specify multiple
                                          hopoffs. |
| 12.1(2)T | This command was modified to allow the user to specify whether LRQs should be sent simultaneously or sequentially to the gatekeepers. |
| 12.2(11)T | This command was implemented on the following platforms: Cisco 2600 series, Cisco MC3810, and Cisco 7200 series. |

| Command | Description |
|---|---|
| show gatekeeper gw-type-prefix | Displays the list of currently defined technology zones and the gatekeepers responsible for each. |
| zone prefix | Configures the gatekeeper with knowledge of its own prefix and the prefix of any remote zone. |