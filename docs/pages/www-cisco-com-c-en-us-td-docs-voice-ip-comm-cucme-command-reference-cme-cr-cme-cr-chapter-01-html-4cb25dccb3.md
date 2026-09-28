---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-01-html-4cb25dccb3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_01.html
retrieved_at: 2026-08-21T22:55:44.914442+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: B

## Chapter: Cisco Unified CME Commands: B

# Cisco Unified CME Commands: B

## b2bua

To configure a dial peer associated with an individual Session
                              		  Initiation Protocol (SIP) phone in Cisco Unified CME or a group of phones in a
                              		  Cisco Unified SIP Survivable Remote Site Telephony (SRST) environment to point
                              		  to Cisco Unity Express, use the b2bua command in dial-peer configuration mode. To disable B2BUA call
                              		  flow on the dial peer, use the no form of this command.

b2bua

no b2bua

### Syntax Description

This command has no arguments or keywords.

### Command Default

B2BUA callflow is disabled.

### Command Modes

Dial-peer configuration (config-dial-peer)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

### Usage Guidelines

Use the b2bua command to set the Cisco Unified CME source
                              		  address as the 302 redirect contact address for all calls forwarded to Cisco
                              		  Unity Express.

## Examples

The following example shows b2bua included in the configuration for
                              		  voice dial peer 1:

```
dial-peer voice 1 voip
 destination-pattern 4...
 session target ipv4:10.5.49.80
 session protocol sipv2
 dtmf-relay sip-notify
 b2bua
```

### Related Commands

Command

Description

allow-connections

Enables calls between SIP endpoints in a VoIP network.

dial-peer voice

Defines a dial peer and enters dial-peer configuration
                                          						mode.

mode (voice register global)

Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CME system.

show dial-peer voice

Displays information for dial peers.

source-address (voice register global)

Identifies the IP address and port through which SIP phones
                                          						communicate with a Cisco Unified CME router.

voice register global

Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified CME
                                          						or Cisco Unified SIP SRST environment.

## background save interval

To set the interval of the background save process, use the
                              		  background save interval command in telephony-service configuration mode.

background save interval interval minutes

### Syntax Description

interval minutes

Interval value in minutes. Range:1 to 1440. Must be in
                                          						increments of 10.

### Command Default

The default interval is 10 minutes.

### Command Modes

Telephony-service configuration mode

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(4)M

Cisco Unified CME 8.6

This command was introduced.

### Usage Guidelines

Use this command to define the background saving interval. The
                              		  configured interval value should be in increments of 10 minutes. If 0 is
                              		  configured as the interval, no backup will be created. The default interval is
                              		  10 minutes.

## Examples

The following example shows background save interval command
                              		  configured under telephony-service configuration:

```
(config-telephony)#background
(config-telephony)#background save
(config-telephony)#background save interval
(config-telephony)#background save interval 20 (config-telephony)#background save interval 20 minutes
```

## bandwidth video tias-modifier

To set the maximum video bandwidth bytes per second (bps) for SIP IP
                              		  phones, use the bandwidth video tias-modifier command in voice register global
                              		  configuration mode. To reset the maximum video bandwidth for SIP phones, use
                              		  the no form of this command.

bandwidth video tias-modifier bandwidth value [ negotiate end-to-end ]

no bandwidth video tias-modifier

### Syntax Description

bandwidth value

Bandwidth value in bps. Range:1 to 99999999.

negotiate end-to-end

Negotiate the minimum SIP-line video bandwidth in SDP
                                          						end-to-end.

### Command Default

No default bandwidth is set.

### Command Modes

Voice register global

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(4)M

Cisco Unified CME 8.6

This command was introduced.

### Usage Guidelines

Use this command to set the maximum video bandwidth for SIP IP
                              		  phones. Video calls require much higher bandwidth usage than audio only
                              		  calls.When there is a limitation of resources, video call bandwidth control
                              		  becomes very crucial for the system. Using the bandwidth video tias-modifier
                              		  command, video calls on Cisco Unified IP Phones 9951 and 9971 can use up to
                              		  1Mbps for VGA quality video.

## Examples

The following example shows bandwidth video tias modifier command
                              		  configured under voice register global:

```
Router#show run
!
!
!
voice service voip
 allow-connections sip to sip
!
!
voice register global
 mode cme
 source-address 10.100.109.10 port 5060
 bandwidth video tias-modifier 256 negotiate end-to-end
 max-dn 200
 max-pool 42
 create profile sync 0004625832149157
!
voice register pool  1
 id mac 1111.1111.1111
 camera
```

### Related Commands

Command

Description

video

Enables video capability on Cisco Unified SIP IP Phones
                                          						9951 and 9971.

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

Voice class tenant.

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

## blf-speed-dial

To enable Busy Lamp Field (BLF) monitoring for a speed-dial number on
                              		  a phone registered to Cisco Unified CME, use the blf-speed-dial command in ephone or voice
                              		  register pool configuration mode. To disable BLF monitoring for speed-dial, use
                              		  the no form of this command.

blf-speed-dial tag number label string [ device ]

no blf-speed-dial tag

### Syntax Description

tag

Number that identifies the speed-dial index. Range is 1 to
                                          						75 (Skinny Client Control Protocol, SCCP); 1 to 113 (Session Initiation
                                          						Protocol, SIP).

number

Telephone number to speed dial.

label string

Alphanumeric label that identifies the speed-dial button.
                                          						The string can contain up to 30 characters.

device

(Optional) Enables phone-based monitoring.

### Command Default

BLF monitoring is disabled.

### Command Modes

Ephone configuration (config-ephone) Voice register pool configuration (config-register-pool)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XJ

Cisco Unified CME 4.1

This command was introduced.

12.4(15)T

Cisco Unified CME 4.1

This command was integrated into Cisco IOS Release
                                          						12.4(15)T.

12.4(22)YB

Cisco Unified CME 7.1

This command was modified to add the device keyword.

12.4(24)T

Cisco Unified CME 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

15.2(4)M

Cisco Unified CME 9.1

This command was modified to increase the BLF speed-dial
                                          						index for Cisco Unified SIP phones to 113.

### Usage Guidelines

This command enables a phone to monitor the status of a line
                              		  associated with a speed-dial button. The device keyword enables BLF monitoring of the
                              		  phone for which the watched directory number is the primary line. This allows
                              		  watchers to monitor whether a user is on the phone, not just on an individual
                              		  line on the phone.

The directory number associated with the speed-dial number must have
                              		  presence enabled with the allow watch command. For device-level monitoring, all
                              		  directory numbers associated with the monitored phone require the allow watch command. If any of the directory numbers is
                              		  missing this configuration, the device status reported to the watcher could be
                              		  inconsistent.

After using the blf-speed-dial command for Cisco Unified SIP IP phones, you must generate a
                              		  new configuration profile using the create profile command and then restart the phones with the restart command.

For information on the BLF status indicators that display on specific
                              		  types of phones in Cisco Unified CME, see the Cisco
                                 			 Unified IP Phone documentation for your phone model.

## Examples

The following example shows BLF speed-dial monitoring enabled on
                              		  phone 1 for individual directory numbers. The line status of extensions 51212
                              		  and 51214 displays on phone 1 show that presence is enabled for those directory
                              		  numbers.

```
Router(config)# ephone 1 Router(config-ephone)# blf-speed-dial 1 51212 label sales Router(config-ephone)# blf-speed-dial 2 51214 label payroll Router(config)# voice register pool 1 Router(config-register-pool)# blf-speed-dial 1 51212 label sales Router(config-register-pool)# blf-speed-dial 2 51214 label payroll
```

The following example shows phone-based BLF speed-dial monitoring
                              		  enabled on phone 2. The line status of all extensions on the phone for which
                              		  51212 is the primary number display shows that presence is enabled for those
                              		  directory numbers.

```
Router(config)# ephone 2 Router(config-ephone)# blf-speed-dial 1 51212 label sales device Router(config)# voice register pool 2 Router(config-register-pool)# blf-speed-dial 1 51212 label sales device
```

The following example shows BLF speed-dial monitoring enabled on key
                              		  13 of phone 3:

```
Router(config)# voice register pool 3 Router(config-register-pool)# blf-speed-dial 13 51212 label sales device
```

### Related Commands

Command

Description

allow watch

Allows a directory number on a phone registered to Cisco
                                          						Unified CME to be watched in a presence service.

create profile

Generates the configuration profile files required for
                                          						Cisco Unified SIP IP phones.

presence

Enables presence service and enters presence configuration
                                          						mode.

presence call-list

Enables BLF monitoring for call lists and directories on
                                          						phones registered to a Cisco Unified CME router.

restart (voice register)

Performs a fast restart of one or all Cisco Unified SIP IP
                                          						phones associated with a Cisco Unified CME router.

## bnea

To specify the audio file used for the busy station not equipped for
                              		  preemption announcement, use the bnea command in voice MLPP configuration mode. To disable use of
                              		  this audio file, use the no form of this command.

bnea audio-url

no bnea

### Syntax Description

audio-url

Location of the announcement audio file in URL format.
                                          						Valid storage locations are TFTP, FTP, HTTP, and flash memory.

### Command Default

No announcement is played.

### Command Modes

Voice MLPP configuration (config-voice-mlpp)

## Command History

Release

Cisco Products

Modification

12.4(22)YB

Cisco Unified CME 7.1

This command was introduced.

12.4(24)T

Cisco Unified CME 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

This command specifies the G.711 a-law or u-law 8-KHz encoded audio
                              		  file (.wav or. au format) for the announcement that is played to the caller
                              		  when the dialed number is not preemptable.

The mlpp indication command must be enabled (default) for a
                              		  phone to play preemption announcements.

This command is not supported by Cisco IOS help. If you type ? , Cisco IOS help does not display a list of
                              		  valid entries.

## Examples

The following example shows the busy station not equipped for
                              		  preemption announcement is set to the file named bnea.au located in flash:

```
Router(config)# voice mlpp Router(config-voice-mlpp)# bnea flash:bnea.au
```

### Related Commands

Command

Description

access-digit

Defines the access digit that phone users dial to request a
                                          						precedence call.

bpa

Specifies the audio file used for the blocked precedence
                                          						announcement.

mlpp indication

Enables MLPP indication on an SCCP phone or analog FXS
                                          						port.

mlpp preemption

Enables preemption capability on an SCCP phone or analog
                                          						FXS port.

## bpa

To specify the audio file used for the blocked precedence
                              		  announcement, use the bpa command in voice MLPP configuration mode. To disable use of
                              		  this audio file, use the no form of this command.

bpa audio-url

no bpa

### Syntax Description

audio-url

Location of the announcement audio file in URL format.
                                          						Valid storage locations are TFTP, FTP, HTTP, and flash memory.

### Command Default

No announcement is played.

### Command Modes

Voice MLPP configuration (config-voice-mlpp)

## Command History

Release

Cisco Products

Modification

12.4(22)YB

Cisco Unified CME 7.1

This command was introduced.

12.4(24)T

Cisco Unified CME 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

This command specifies the G.711 a-law or u-law 8-KHz encoded audio
                              		  file (.wav or .au format) for the announcement that is played to the caller in
                              		  the following situations:

- Destination party for the precedence call is off hook.

- Destination party is busy with a precedence call of an equal or
                                 			 higher precedence and the destination party does not have Call Waiting or Call
                                 			 Forward configured, and does not have an attendant-console service configured.

The mlpp indication command must be enabled (default) for a
                              		  phone to play precedence announcements.

This command is not supported by Cisco IOS help. If you type ? , Cisco IOS help does not display a list of
                              		  valid entries.

## Examples

The following example shows the blocked precedence announcement is
                              		  set to the file named bpa.au located in flash:

```
Router(config)# voice mlpp Router(config-voice-mlpp)# bpa flash:bpa.au
```

### Related Commands

Command

Description

attendant-console

Specifies the phone number of the MLPP attendant-console
                                          						service.

bnea

Specifies the audio file used for the busy station not
                                          						equipped for preemption announcement.

mlpp indication

Enables MLPP indication on an SCCP phone or analog FXS
                                          						port.

mlpp preemption

Enables preemption capability on an SCCP phone or analog
                                          						FXS port.

## bulk

To set bulk registration for E.164 numbers that will register with
                              		  SIP proxy server, use the bulk command in voice register global
                              		  configuration mode. To disable bulk registration, use the no form of this command.

bulk number-pattern

no bulk

### Syntax Description

number-pattern

A sequence of digits including wild card character.

### Command Default

Bulk registration is disabled.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

This command allows you to configure bulk registration for
                              		  registering a block of phone numbers with an external registrar so that calls
                              		  can be routed to Cisco CME from the SIP network.

Numbers that match the number pattern defined by using
                              		  the bulk command register with the external registrar.
                              		  The block of numbers that is registered can include any phone that is attached
                              		  to Cisco CME using SIP or SCCP, or any analog phone that is directly attached
                              		  to a Cisco router FXS port.

A number can contain one or more periods (.) as wildcard characters
                              		  that will match any dialed number in that position. For example, 51.. rings
                              		  when 5100 is dialed, when 5101 is dialed, and so forth.

The external registrar is configured by using the registrar server command under the SIP user-agent
                              		  configuration mode.

## Examples

The following example shows how to specify that numbers matching 1235
                              		  and any other dialed number in the next four positions, be routed to the Cisco
                              		  CME from the SIP network.

```
Router(config)# voice register global Router(conf-register-global)# mode cme Router(conf-register-global)# bulk 1235...
```

### Related Commands

Command

Description

mode (voice register global)

Enables the mode for provisioning SIP phones in a Cisco
                                          						CallManager Express (Cisco CME) system.

no reg (voice register dn)

Specifies that a directory number in a SIP Cisco
                                          						CallManager Express (Cisco CME) system not register with an external proxy
                                          						server

no reg (voice hunt-group)

Specifies that a pilot number for a voice hunt group not
                                          						register with an external proxy server

registrar

Enables SIP registrar functionality.

## bulk-speed-dial prefix

To set the prefix code that phone users dial to access speed-dial
                              		  numbers from a global bulk speed-dial list, use the bulk-speed-dial prefix command in telephony-service configuration
                              		  mode. To return the prefix code to the default, use the no form of this command.

bulk-speed-dial prefix prefix-code

no bulk-speed-dial-prefix

### Syntax Description

prefix-code

One to four-character access code for speed dial. Default
                                          						is #.

### Command Default

The default prefix code (number sign [#]) is used.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS 12.4(9)T.

### Usage Guidelines

This command changes the prefix code that a phone user must dial to
                              		  access speed-dial numbers from a speed-dial list that is enabled using the bulk-speed-dial list command in telephony-service configuration mode. The default
                              		  prefix is # (number sign).

If a bulk speed-dial list is enabled using this command in
                              		  telephony-service configuration mode and is also enable using this command in
                              		  ephone configuration mode, the list enabled in ephone configuration mode takes
                              		  precedence over the list at the global level for a given prefix. However, if
                              		  the prefix used at the global level is different than the prefix used at the
                              		  phone level, the lists are treated as separate lists - each list being
                              		  associated with a different prefix, and at the phone level, you can access both
                              		  lists.

Use the show telephony-service bulk-speed-dial to display information about bulk
                              		  speed-dial lists that are configured in Cisco Unified CME.

## Examples

The following example changes the default bulk speed-dial prefix to
                              		  #7 and enables global bulk speed-dial list number 6 for all phones. It also
                              		  enables a personal bulk speed-dial list for ephone 2. In this example, ephone 2
                              		  can access all of the numbers in both lists because each list is assigned a
                              		  different prefix (# and #7).

```
telephony-service
 bulk-speed-dial list 6 flash:sd_dept_01_1_87.txt
 bulk-speed-dial prefix #7
ephone-dn 3
 number 2555
ephone-dn 4
 number 2557
ephone 2
 button 1:3 2:4
 bulk-speed-dial list 7 flash:lmi_sd_list_08_24_95.csv
```

### Related Commands

Command

Description

bulk-speed-dial list

Enables a bulk speed-dial list.

show telephony-service bulk-speed-dial

Displays information about bulk speed-dial lists that are
                                          						configured in Cisco Unified CME.

## busy-trigger-per-button

To set the maximum number of calls allowed on an octo-line directory
                              		  number before activating Call Forward Busy or a busy tone, use the busy-trigger-per-button command in ephone or
                              		  ephone-template configuration mode. To reset to the default, use the no form of this command.

busy-trigger-per-button number-of-calls

no busy-trigger-per-button

### Syntax Description

number-of-calls

Maximum number of calls. Range: 1 to 8. Default: 0
                                          						(disabled).

### Command Default

Disabled (busy trigger is 0).

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XZ

Cisco Unified CME 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command limits the calls to an octo-line on the specified phone
                              		  by triggering Call Forward Busy or a busy tone. After the number of active
                              		  calls, incoming and outgoing, on an octo-line directory number reaches the
                              		  limit set with this command, the next incoming call to the directory number is
                              		  forwarded to the Call Forward Busy destination. If Call Forward Busy is not
                              		  configured, Cisco Unified CME rejects the call and plays a busy tone.

This command applies to each octo-line directory number on the phone.

If a directory number is shared among different phones, the busy
                              		  trigger is initiated after the number of existing calls exceeds the limit set
                              		  on any of the phones that share the directory number.

This command must be set to a value that is less than or equal to the
                              		  value set with the max-calls-per-button command.

If you use an ephone template to apply a command to an ephone and you
                              		  also use the same command in ephone configuration mode for the same ephone, the
                              		  value that you set in ephone configuration mode has priority.

## Examples

The following example shows that after an octo-line on ephone 1
                              		  receives four calls, the fifth incoming call triggers Call Forward Busy or a
                              		  busy tone.

```
Router(config)# ephone 1 Router(config-ephone)# busy-trigger-per-button 4
```

### Related Commands

Command

Description

call-forward busy

Enables call forwarding so that incoming calls to a busy
                                          						extension are forwarded to another extension.

ephone-dn

Configures a directory number for SCCP phones.

max-calls-per-button

Sets the maximum number of calls allowed on an octo-line
                                          						directory number on an SCCP phone.

## busy-trigger-per-button (voice register pool)

To set the maximum number of calls allowed on a SIP directory number
                              		  before activating Call Forward Busy or a busy tone, use the busy-trigger-per-button command in voice
                              		  register pool configuration mode. To reset to the default, use the no form of this command.

busy-trigger-per-button number

no busy-trigger-per-button

### Syntax Description

number

Maximum number of calls. Range: 1 to 50.

### Command Default

no busy-trigger-per-button

### Command Modes

Voice register pool configuration (config-register-pool)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(22)YB

Cisco Unified CME 7.1

This command was introduced.

12.4(24)T

Cisco Unified CME 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

This command limits the number of calls to each directory number on
                              		  the specified phone by triggering Call Forward Busy or a busy tone. After the
                              		  number of active calls, both incoming and outgoing, reaches the number of calls
                              		  set with this command, Cisco Unified CME forwards the next incoming call to the
                              		  Call Forward Busy destination. Cisco Unified CME rejects the call and plays a
                              		  busy tone if Call Forward Busy is not configured.

If a directory number is shared among different phones, the busy
                              		  trigger is initiated after the number of existing calls exceeds the limit set
                              		  on all of the phones that share the directory number.

This command must be set to a value that is less than or equal to the
                              		  value set with the max-calls-per-button command.

## Examples

The following example shows that after a shared-line on phone 1
                              		  receives four calls, the fifth incoming call triggers Call Forward Busy or a
                              		  busy tone.

```
Router(config)# voice register pool 1 Router(config-register-pool)# busy-trigger-per-button 4
```

### Related Commands

Command

Description

huntstop (voice register dn)

Disables call hunting behavior for a directory number on a
                                          						SIP phone.

max-calls-per-button

Sets the maximum number of calls allowed on an octo-line
                                          						directory number on an SCCP phone.

shared-line

Creates a directory number to be shared by multiple SIP
                                          						phones.

## button

To associate
                              		  ephone-dns with individual buttons on a Cisco Unified IP phone and to specify
                              		  line type or ring behavior, use the button command in ephone configuration mode. To remove an ephone-dn association from a
                              		  button, use the no form of
                              		  this command.

button button-number {separator} dn-tag [,dn-tag...]
                                 				  [button-number{x}overlay-button-number] [button-number...]

no button button-number {separator} dn-tag [,dn-tag...]
                                 				  [button-number{x}overlay-button-number] [button-number...]

### Syntax Description

button-number

Number
                                          						of a line button on a Cisco Unified IP phone that is to be associated with an
                                          						extension (ephone-dn).

The
                                          						maximum number of button–ephone-dn pairs is determined by the phone type.

separator

Single
                                          						character that denotes the characteristics to be associated with this phone
                                          						button. Valid entries are as follows:

- : (colon)—Normal ring. For incoming calls on this
                                             						  extension, the phone produces audible ringing, a flashing icon in the phone
                                             						  display, and a flashing red light on the handset. On the Cisco IP Phone 7914
                                             						  Expansion Module, a flashing yellow light also accompanies incoming calls.

- b —Beep but no ring. Audible ring is suppressed for
                                             						  incoming calls, but call-waiting beeps are allowed. Visible cues are the same
                                             						  as those described for a normal ring.

- c —Call waiting. Provides call waiting for
                                             						  secondary calls to an overlaid ephone-dn. See also the o keyword.

- f —Feature ring. Differentiates incoming calls on a
                                             						  special line from incoming calls on other lines on the phone. The feature-ring
                                             						  cadence is a triple pulse, as opposed to a single pulse for normal internal
                                             						  calls and a double pulse for normal external calls.

- m —Monitor mode for a shared line. Visible line
                                             						  status indicates whether the line is in-use or not. Monitored lines cannot be
                                             						  used on this phone for incoming or outgoing calls.

- o —Overlay line. Multiple ephone-dns share a single
                                             						  button, up to a maximum of 25 on a button. See also the c keyword.

- s —Silent ring. Audible ring and call-waiting beep
                                             						  are suppressed for incoming calls. The only visible cue is a flashing ((<
                                             						  icon in the phone display.

- w —Watch mode
                                             						  for all lines on the phone for which this directory number is the primary line.
                                             						  Visible line status indicates whether watched phone is idle or not.

dn-tag

Ephone-dn tag that was previously defined using the ephone-dn command. When used with the c and o keywords, the dn-tag argument can contain up to 25 individual dn-tags,
                                          						separated by commas.

x

Separator that creates an overlay rollover button. When the overlay button
                                          						specified in this command is occupied by an active call, a second call to one
                                          						of its ephone-dns will appear on this button. This button is also known as an
                                          						overlay expansion button.

overlay-button-number

Number
                                          						of the overlay button that should overflow to this button.

### Command Default

No buttons are
                              		  defined for an ephone.

### Command Modes

Ephone configuration (config-ephone)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						ITS 1.0

This
                                          						command was introduced

12.2(8)T

Cisco
                                          						ITS 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T.

12.2(11)YT

Cisco
                                          						ITS 2.1

The b and s keywords were added.

12.2(15)ZJ

Cisco
                                          						CME 3.0

The f , m , and o keywords
                                          						were added.

12.3(4)T

Cisco
                                          						CME 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

12.3(11)XL

Cisco
                                          						CME 3.2.1

The c keyword
                                          						was added and the ability to use the m keyword
                                          						to monitor call-park slots was added.

12.3(14)T

Cisco
                                          						CME 3.3

This
                                          						command was integrated into Cisco IOS Release 12.3(14)T.

12.4(4)XC

Cisco
                                          						Unified CME 4.0

The x keyword was added and the number of ephone-dns
                                          						that can be overlaid on a single button with the o or c keyword
                                          						was increased from 10 to 25. The interaction between the keyword and night
                                          						service was modified; silent ringing is overridden when night service is
                                          						active.

12.4(9)T

Cisco
                                          						Unified CME 4.0

The
                                          						modifications made to this command were integrated into Cisco IOS Release
                                          						12.4(9)T.

12.4(11)XJ3

Cisco
                                          						Unified CME 4.1

The w keyword
                                          						was added.

12.4(15)T

Cisco
                                          						Unified CME 4.1

This
                                          						command with the w keyword
                                          						was integrated into Cisco IOS Release 12.4(15)T.

### Usage Guidelines

The button command assigns telephone extensions to Cisco Unified IP phones by associating
                              		  a button number with one or more directory numbers (ephone-dns).

Telephone
                              		  services such as call waiting and three-party conferences require a minimum of
                              		  two phone lines (ephone-dns defined with the ephone-dn command) to be available and configured on a Cisco IP phone.

The Cisco
                              		  Unified IP Phone 7910G has only one physical line button. To support call
                              		  waiting and three-party conferences on a Cisco Unified IP Phone 7910G, a second
                              		  (hidden) line is required. This line cannot be selected directly using a line
                              		  button. You can access the second line when you press the Conference button.
                              		  You can also support multiple-call services using the ephone-dn dual-line configuration option.

Feature Ring (f)

A feature ring
                              		  is a third type of ring cadence, in addition to the internal call and external
                              		  call ring cadences. For example, an internal call in the United States rings
                              		  for 2 seconds on and 4 seconds off (single-pulse ring), and an external call
                              		  rings for 0.4 seconds on, 0.2 seconds off, 0.4 seconds on, and 0.2 seconds off
                              		  (double-pulse ring). A feature ring is a triple-pulse ring. The purpose of
                              		  associating a feature ring with a line button is to be able to identify from a
                              		  distance a special line that is ringing on a multiline phone.

Monitor Mode (m)

A line button
                              		  set in monitor mode on one phone displays visual line status for a line that
                              		  also appears on another phone. When monitor mode is set for a button with a
                              		  shared line, the line status indicates that the shared line is either idle or
                              		  in use. The line and line button are available in monitor mode for visual
                              		  status only. Calls cannot be made or received using a line button that has been
                              		  set in monitor mode. Incoming calls on a line button that is in monitor mode do
                              		  not ring and do not display caller ID or call-waiting caller ID.

Monitor mode is
                              		  intended for use only in the context of shared lines so that a receptionist can
                              		  visually monitor the in-use status of several users’ phone extensions (for
                              		  example, as a busy-lamp field). To monitor all lines on an individual phone so
                              		  that a receptionist can visually monitor the in-use status of that phone, see
                              		  the Watch Mode (w) section.

The line button
                              		  for a monitored line can also be used as a direct-station-select for a call
                              		  transfer when the monitored line is in an idle state. In this case, the
                              		  receptionist who transfers a call from a normal line can press the Transfer
                              		  button and then press the line button of the monitored line, causing the call
                              		  to be transferred to the phone number of the monitored line.

Overlay (o)

Overlay lines
                              		  are ephone-dns that share a single button on a multibutton phone. When more
                              		  than one incoming call arrives on lines that are set on a single button, the
                              		  line (ephone-dn) that is the leftmost in the button command list is the primary line and is given the highest priority. If this
                              		  call is answered by another phone or if the caller hangs up, the phone selects
                              		  the next line in its overlay set to present as the ringing call. The caller ID
                              		  display updates to show the caller ID for the currently presented call.

Ephone-dns that
                              		  are part of an overlay set can be single-line ephone-dns or dual-line
                              		  ephone-dns, but the set must contain either all single-line ephone-dns or all
                              		  dual-line ephone-dns, and not a mixture of the two.

The primary
                              		  ephone-dn on each phone in a shared-line overlay set should be unique to the
                              		  phone being configured to guarantee that there is a line available for outgoing
                              		  calls, and to ensure that the phone user can obtain dial-tone even when there
                              		  are no idle lines available in the rest of the shared-line overlay set. Use a
                              		  unique ephone-dn in this manner to provide for a unique calling party identity
                              		  on outbound calls made by the phone so that the called user can see which
                              		  specific phone is calling.

The name of the
                              		  first ephone-dn in the overlay set is not displayed because it is the default
                              		  ephone-dn for calls to the phone, and the name or number is permanently
                              		  displayed next to the phone’s button. For example, if there are ten ephone-dns
                              		  in an overlay set, only the last nine ephone-dns are displayed when calls are
                              		  made to them.

Overlay Ephone-dns with
                                 			 Call Waiting (c)

The
                              		  configuration for the overlaid ephone-dns with call waiting (keyword c ) and
                              		  without call waiting (keyword o ) is the
                              		  same.

Ephone-dns
                              		  accept call interruptions, such as call waiting, by default. For call waiting
                              		  to work, the default must be active. To ensure thatthe default is active,
                              		  remove the no call-waiting beep accept command from the configurations of
                              		  ephone-dns for which you want to use call waiting.

In Cisco
                              		  Unified CME 4.0(3), the Cisco Unified IP Phone 7931G cannot support overlays
                              		  that contain ephone-dn configured for dual-line mode.

Silent Ring (s)

You can
                              		  configure silent ring on any type of phone. However, you typically set silent
                              		  ring only on buttons of a phone with multiple lines, such as a Cisco Unified IP
                              		  Phone 7940, Cisco Unified IP Phones 7960 and 7960G, or a Cisco Unified IP Phone
                              		  7914 Expansion Module. The only visible cue is a flashing ((< icon in the
                              		  phone display.

If you
                              		  configure a button to have a silent ring, you will not hear a call-waiting beep
                              		  or call-waiting ring regardless of whether the ephone-dn associated with the
                              		  button is configured to generate a call-waiting beep or call-waiting ring.

In Cisco IOS
                              		  Release 12.4(4)XC and later releases, the silent ringing behavior is overridden
                              		  during active night-service periods. Silent ringing does not apply during
                              		  designated night-service periods when the s keyword
                              		  is used.

Watch Mode (w)

A line button
                              		  that is configured for watch mode on one phone provides visual line status for
                              		  all lines on another phone (watched phone) for which the watched directory
                              		  number is the primary line. Watched mode allows a phone user, such as a
                              		  receptionist, to visually monitor the in-use status of an individual phone. The
                              		  line and line button on the watching phone are available in watch mode for
                              		  visual status only. Calls cannot be made or received using a line button that
                              		  has been set in watch mode. Incoming calls on a line button that is in watch
                              		  mode do not ring and do not display caller ID or call-waiting caller ID.

If any of the
                              		  following conditions are true, the status of the line button in watch mode is
                              		  that the watched phone is in-use:

- Watched
                                 			 phone is off-hook

- Watched
                                 			 phone is not registered

- Watched
                                 			 phone is in the do-not-disturb (DND) mode

- Watched
                                 			 directory number is not idle

If the watched
                              		  directory number is a shared line and the shared line is not idle on any phone
                              		  with which it is associated, then in the context of watch mode, the status of
                              		  the line button indicates that the watched
                                 			 phone is in use.

For best
                              		  results in terms of monitoring the status of an individual phone based on a
                              		  watched directory number, the directory number to be configured for watch mode
                              		  should not be a shared line. To monitor a shared line so that a receptionist
                              		  can visually monitor the in-use status of several users’ phone extensions, see
                              		  the Monitor Mode (m) section.

If the watched
                              		  directory number is associated with several phones, then the watched phone is
                              		  the one on which the watched directory number is on button 1 or the one on
                              		  which the watched directory number is on the button that is configured by using
                              		  the auto-line command, with auto-line having priority.

If more than
                              		  one phone meets the criteria for primary line as described above, then the
                              		  watched phone is the first phone that that meets the criteria. Typically, that
                              		  is the phone with the lowest ephone tag value. However, if the watched
                              		  directory number is configured on button 1 of ephone 1 and the same directory
                              		  number is also configured on button 3 with “auto-line 3” of ephone 24, then
                              		  ephone 24 is the watched phone because the auto-line configuration has
                              		  priority.

The line button
                              		  for a watched phone can also be used as a direct-station-select for a call
                              		  transfer when the watched phone is idle. In this case, the phone user who
                              		  transfers a call from a normal line can press the Transfer button and then
                              		  press the line button of the watched directory number, causing the call to be
                              		  transferred to the phone number associated with the watched directory number.

Expansion Buttons for
                                 			 Overlay Ephone-dns (x)

This feature
                              		  works to expand coverage for an overlay button that has been configured using
                              		  the o separator
                              		  in the button command. Overlay buttons with call waiting that use the c separator
                              		  in the button command are not eligible for overlay rollover.

## Examples

The following
                              		  example assigns four button numbers on the phone to ephone-dn tags. Button 4 is
                              		  configured for a silent ring:

```
ephone-dn 1
 number 233
ephone-dn 4
 number 234
ephone-dn 16
 number 235
ephone-dn 19
 number 236
ephone 1
 button 1:1 2:4 3:16 4s19
```

The following
                              		  example shows three phones that each have three instances of extension number
                              		  1001 overlaid onto a single button, which allows three simultaneous calls to
                              		  extension 1001. The first call arrives on ephone-dn 1 and rings button 1 on all
                              		  three phones. The call is answered on ephone 10. A second call for 1001 hunts
                              		  onto ephone-dn 2 and rings on the remaining two ephones, ephones 11 and 12, and
                              		  is answered by ephone 12. A third call to 1001 hunts onto ephone-dn 3 and rings
                              		  on ephone 12, where it is answered. This configuration creates a three-way
                              		  shared line across three IP phones and can handle three simultaneous calls to
                              		  the same telephone number. Note that if ephone 12 is busy, the third call will
                              		  go to voice mail (7000). Note also that if you want to configure call waiting,
                              		  you can use the same configuration, except use the c keyword
                              		  instead of the o keyword.
                              		  Ephone 10 uses call waiting.

```
ephone-dn 1
 number 1001
 no huntstop
!
ephone-dn 2
 number 1001
 no huntstop
 preference 1
!
ephone-dn 3
 number 1001
 preference 2
 call-forward busy 7000
!
! The next ephone configuration includes the first instance of shared line 1001.
ephone 10
 mac-address 1111.2222.3333
 button 1c1,2,3
!
! The next ephone configuration includes the second instance of shared line 1001.
ephone 11
 mac-address 1111.2222.4444
 button 1o1,2,3
!
! The next ephone configuration includes the third instance of shared line 1001.
ephone 12
 mac-address 1111.2222.555
 button 1o1,2,3
```

The following
                              		  is an example of a unique ephone-dn as the primary dn in a simple shared-line
                              		  overlay configuration. The no huntstop command is configured for all the
                              		  ephone-dns except ephone-dn 12, the last one in the overlay set. Because the
                              		  ephone-dns are dual-line dns, the huntstop-channel command is also configured
                              		  to ensure that the second channel remains free for outgoing calls and for
                              		  conferencing.

```
ephone-dn 1 dual-line
 number 101
 huntstop-channel
!
ephone-dn 2 dual-line
 number 102
 huntstop-channel
!
ephone-dn 10 dual-line
 number 201
 no hunsttop
 huntstop-channel
!
ephone-dn 11 dual-line
 number 201
 no hunsttop
 huntstop-channel
!
ephone-dn 12 dual-line
number 201
huntstop-channel
!
!The next ephone configuration includes (unique) ephone-dn 1 as the primary line in a shared-line overlay
ephone 1
mac-address 1111.1111.1111
button 1o1,10,11,12
!
!The next ephone configuration includes (unique) ephone-dn 2 as the primary line in another shared-line overlay
ephone 2
mac-address 2222.2222.2222
button 1o2,10,11,12
```

Shared-line
                              		  overlays can be constructed using the “button o” or “button c” formats,
                              		  depending on whether call-waiting is desired. The following example shows an
                              		  ephone configuration that enables call waiting (c) in a shared-line overlay:

```
ephone 1
 mac-address 1111.1111.1111
 button 1c1,10,11,12
!
 ephone 2
 mac-address 2222.2222.2222
 button 1c2,10,11,12
```

The following
                              		  example configures a “3x3” shared-line setup for three ephones and nine shared
                              		  lines (ephone-dns 20 through 28). Each ephone has a unique ephone-dn for each
                              		  of its three buttons (ephone-dns 1 to 3, ephone-dns 4 to 6, and ephone-dns 7 to
                              		  9). The remaining ephone-dns are shared among the three phones. Three phones
                              		  with three buttons each can take nine calls. The overflow buttons provide the
                              		  ability for an incoming call to ring on the first available button on each
                              		  phone.

```
ephone 1
 button 1o1,2,3,20,21,22,23,24,25,26,27,28 2x1 3x1
ephone 2
 button 1o4,5,6,20,21,22,23,24,25,26,27,28 2x1 3x1
ephone 3
 button 1o7,8,9,20,21,22,23,24,25,26,27,28 2x1 3x1
```

### Related Commands

Command

Description

call-waiting beep

Allows phone buttons to accept or generate call-waiting beeps.

restart (ephone)

Performs a fast reboot of a single phone associated with a Cisco Unified CME
                                          						router.

restart (telephony-service)

Performs a fast reboot of one or all phones associated with a Cisco Unified CME
                                          						router.

show ephone

Displays information about ephones and the corresponding Cisco Unified IP
                                          						phones.

show ephone overlay

Displays the configuration and current status of registered overlay ephone-dns.

## button-layout (voice register template)

To organize the order of the display of all buttons including line,
                              		  speed dial, blf speed dial, feature buttons, and url buttons on a Cisco Unified
                              		  SIP IP phone, use the button-layout command in voice register template configuration mode. To
                              		  disable the feature button set and change the action of the buttons on IP
                              		  phones, use the no form of this command.

button-layout [button-string] [button-type]

no button-layout

### Syntax Description

button-string

(Optional) Specifies a comma-separated list of physical
                                          						button number or ranges of button numbers.

button-type

(Optional) Specifies one of the following button types:
                                          						Line, Speed-Dial, BLF-Speed-Dial, Feature, URL.

### Command Default

No fixed set of line or feature buttons are defined.

### Command Modes

Voice register template configuration (config-register-temp)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use the button-layout command to assign physical button numbers or
                              		  ranges of numbers with button types such as line, feature, url, speed-dial, and
                              		  blf-speed-dIal. After creating a voice register template and applying the
                              		  template to the voice register pool you can assign the button-layout
                              		  configuration to a Cisco Unified IP Phone.

## Examples

The following example shows button-layout configured on voice
                              		  register template 2 and voice register template 5.

```
Router# show voice register template all
!
voice register dn  65
 number 3065
 name SIP-7965
 label SIP3065
!
voice register template  5 
 button-layout 1 line
 button-layout 2,5 speed-dial
 button-layout 3,6 blf-speed-dial
 button-layout 4,7,9 feature-button
 button-layout 8,11 url-button
!
voice register template  2
 button-layout 1,5 line
 button-layout 4 speed-dial
 button-layout 3,6 blf-speed-dial
 button-layout 7,9 feature-button
 button-layout 8,10-11 url-button
!
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies template to an ephone.

show voice register template

Displays all configuration information associated with a
                                          						SIP phone template.

## button-layout

To configure a fixed set of line or feature buttons in an
                              		  ephone-template which can then be applied to a supported IP phone in Cisco
                              		  Unified CME, use the button-layout set command in ephone-template configuration mode. To disable the
                              		  feature buttons set and change the action of the buttons on IP phones, use the no form of this command.

button-layout [ phone-type { 1 | 2 } | button-string | button-type ]

no button-layout

### Syntax Description

phone-type

Type of IP phone. The following choices are valid:

- 7931 —Cisco Unified IP Phone
                                             						  7931.

1

Number of fixed line or feature set containing the
                                          						following buttons:

- Button 24—Menu.

- Button 23—Headset.

2

Number of fixed line or feature set containing the
                                          						following buttons:

- Button 24—Menu.

- Button 23—Headset.

- Button 22—Directories.

- Button 21—Messages.

button-string

(Optional) Specifies a coma separated list of physical
                                          						button number or ranges of button numbers.

button-type

(Optional) Specifies one of the following button types:
                                          						Line, Speed-Dial, BLF-Speed-Dial, Feature, URL

### Command Default

No fixed set of line or feature buttons are defined.

### Command Modes

Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(6)XE

Cisco Unified CME 4.0(2)

This command was introduced.

12.4(4)XC4

Cisco Unified CME 4.0(3)

This command was introduced.

12.4(11)T

Cisco Unified CME 4.0(3)

This command was integrated into Cisco IOS Release
                                          						12.4(11)T.

15.1(3)T

Cisco Unified CME 8.5

This command was modified. Button String and Button Type
                                          						arguments were added.

### Usage Guidelines

Use this command to configure either Set 1 or Set 2 in an
                              		  ephone-template which can then be applied to an individual Cisco Unified IP
                              		  Phone 7931G in Cisco Unified CME.

After a template has been created, you can apply it to an ephone
                              		  using the ephone-template command in ephone
                              		  configuration mode. You cannot apply more than one ephone template to an
                              		  ephone.

To view your ephone-template configurations, use the show telephony-service ephone-template command.

In Cisco Unified CME 8.5 and later versions, the button-layout
                              		  command allows you to assign physical button numbers or ranges of numbers with
                              		  button types such as Line, Feature, URL, Speed-Dial, BLF-Speed-DIal. After
                              		  creating an ephone-template you can apply the button-layout configuration to a
                              		  Cisco Unified IP Phone.

## Examples

- The following example shows how to create ephone-template 12,
                                 			 containing set 2 feature buttons, and apply the template to ephone 36.

```
Router(config)# ephone-template 12 Router(config-ephone-template)# button-layout set 2 Router(config-ephone-template)# exit Router(config)# ephone 36 Router(config-ephone)# ephone-template 12 Router(config-ephone)# exit Router(config)# telephony-service Router(config-telephony)# create cnf-files
```

- The following example shows ephone-template 10, containing line
                                 			 button, speed-dial button, blf-speed-dial button, feature button, and url
                                 			 button.

```
Router# show telephony-service ephone-template
ephone-template  10
 button-layout 1 line
 button-layout 2,5 speed-dial
 button-layout 3,6 blf-speed-dial
 button-layout 4,7,9 feature
 button-layout 8,11 url
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies template to an ephone.

show telephony-service ephone-template

Displays ephone-template configurations.

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |

| Note | Use the b2bua command to configure Cisco SIP SRST 3.4
                                       		  only after using the allow-connections command to enable B2BUA
                                       		  call flow on the SRST gateway. |
|---|---|

| Command | Description |
|---|---|
| allow-connections | Enables calls between SIP endpoints in a VoIP network. |
| dial-peer voice | Defines a dial peer and enters dial-peer configuration
                                          						mode. |
| mode (voice register global) | Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CME system. |
| show dial-peer voice | Displays information for dial peers. |
| source-address (voice register global) | Identifies the IP address and port through which SIP phones
                                          						communicate with a Cisco Unified CME router. |
| voice register global | Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified CME
                                          						or Cisco Unified SIP SRST environment. |

| interval minutes | Interval value in minutes. Range:1 to 1440. Must be in
                                          						increments of 10. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(4)M | Cisco Unified CME 8.6 | This command was introduced. |

| bandwidth value | Bandwidth value in bps. Range:1 to 99999999. |
|---|---|
| negotiate end-to-end | Negotiate the minimum SIP-line video bandwidth in SDP
                                          						end-to-end. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(4)M | Cisco Unified CME 8.6 | This command was introduced. |

| Command | Description |
|---|---|
| video | Enables video capability on Cisco Unified SIP IP Phones
                                          						9951 and 9971. |

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

| tag | Number that identifies the speed-dial index. Range is 1 to
                                          						75 (Skinny Client Control Protocol, SCCP); 1 to 113 (Session Initiation
                                          						Protocol, SIP). |
|---|---|
| number | Telephone number to speed dial. |
| label string | Alphanumeric label that identifies the speed-dial button.
                                          						The string can contain up to 30 characters. |
| device | (Optional) Enables phone-based monitoring. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was modified to add the device keyword. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |
| 15.2(4)M | Cisco Unified CME 9.1 | This command was modified to increase the BLF speed-dial
                                          						index for Cisco Unified SIP phones to 113. |

| Command | Description |
|---|---|
| allow watch | Allows a directory number on a phone registered to Cisco
                                          						Unified CME to be watched in a presence service. |
| create profile | Generates the configuration profile files required for
                                          						Cisco Unified SIP IP phones. |
| presence | Enables presence service and enters presence configuration
                                          						mode. |
| presence call-list | Enables BLF monitoring for call lists and directories on
                                          						phones registered to a Cisco Unified CME router. |
| restart (voice register) | Performs a fast restart of one or all Cisco Unified SIP IP
                                          						phones associated with a Cisco Unified CME router. |

| audio-url | Location of the announcement audio file in URL format.
                                          						Valid storage locations are TFTP, FTP, HTTP, and flash memory. |
|---|---|

| Release | Cisco Products | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| access-digit | Defines the access digit that phone users dial to request a
                                          						precedence call. |
| bpa | Specifies the audio file used for the blocked precedence
                                          						announcement. |
| mlpp indication | Enables MLPP indication on an SCCP phone or analog FXS
                                          						port. |
| mlpp preemption | Enables preemption capability on an SCCP phone or analog
                                          						FXS port. |

| audio-url | Location of the announcement audio file in URL format.
                                          						Valid storage locations are TFTP, FTP, HTTP, and flash memory. |
|---|---|

| Release | Cisco Products | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| attendant-console | Specifies the phone number of the MLPP attendant-console
                                          						service. |
| bnea | Specifies the audio file used for the busy station not
                                          						equipped for preemption announcement. |
| mlpp indication | Enables MLPP indication on an SCCP phone or analog FXS
                                          						port. |
| mlpp preemption | Enables preemption capability on an SCCP phone or analog
                                          						FXS port. |

| number-pattern | A sequence of digits including wild card character. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| mode (voice register global) | Enables the mode for provisioning SIP phones in a Cisco
                                          						CallManager Express (Cisco CME) system. |
| no reg (voice register dn) | Specifies that a directory number in a SIP Cisco
                                          						CallManager Express (Cisco CME) system not register with an external proxy
                                          						server |
| no reg (voice hunt-group) | Specifies that a pilot number for a voice hunt group not
                                          						register with an external proxy server |
| registrar | Enables SIP registrar functionality. |

| prefix-code | One to four-character access code for speed dial. Default
                                          						is #. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS 12.4(9)T. |

| Command | Description |
|---|---|
| bulk-speed-dial list | Enables a bulk speed-dial list. |
| show telephony-service bulk-speed-dial | Displays information about bulk speed-dial lists that are
                                          						configured in Cisco Unified CME. |

| number-of-calls | Maximum number of calls. Range: 1 to 8. Default: 0
                                          						(disabled). |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| call-forward busy | Enables call forwarding so that incoming calls to a busy
                                          						extension are forwarded to another extension. |
| ephone-dn | Configures a directory number for SCCP phones. |
| max-calls-per-button | Sets the maximum number of calls allowed on an octo-line
                                          						directory number on an SCCP phone. |

| number | Maximum number of calls. Range: 1 to 50. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| huntstop (voice register dn) | Disables call hunting behavior for a directory number on a
                                          						SIP phone. |
| max-calls-per-button | Sets the maximum number of calls allowed on an octo-line
                                          						directory number on an SCCP phone. |
| shared-line | Creates a directory number to be shared by multiple SIP
                                          						phones. |

| button-number | Number
                                          						of a line button on a Cisco Unified IP phone that is to be associated with an
                                          						extension (ephone-dn). The
                                          						maximum number of button–ephone-dn pairs is determined by the phone type. Note The
                                                   						Cisco Unified IP Phone 7910G has only one physical line button, but you can
                                                   						assign it two button–ephone-dn pairs. | Note | The
                                                   						Cisco Unified IP Phone 7910G has only one physical line button, but you can
                                                   						assign it two button–ephone-dn pairs. |
|---|---|---|---|
| Note | The
                                                   						Cisco Unified IP Phone 7910G has only one physical line button, but you can
                                                   						assign it two button–ephone-dn pairs. |
| separator | Single
                                          						character that denotes the characteristics to be associated with this phone
                                          						button. Valid entries are as follows: : (colon)—Normal ring. For incoming calls on this
                                             						  extension, the phone produces audible ringing, a flashing icon in the phone
                                             						  display, and a flashing red light on the handset. On the Cisco IP Phone 7914
                                             						  Expansion Module, a flashing yellow light also accompanies incoming calls. b —Beep but no ring. Audible ring is suppressed for
                                             						  incoming calls, but call-waiting beeps are allowed. Visible cues are the same
                                             						  as those described for a normal ring. c —Call waiting. Provides call waiting for
                                             						  secondary calls to an overlaid ephone-dn. See also the o keyword. f —Feature ring. Differentiates incoming calls on a
                                             						  special line from incoming calls on other lines on the phone. The feature-ring
                                             						  cadence is a triple pulse, as opposed to a single pulse for normal internal
                                             						  calls and a double pulse for normal external calls. |
|  | m —Monitor mode for a shared line. Visible line
                                             						  status indicates whether the line is in-use or not. Monitored lines cannot be
                                             						  used on this phone for incoming or outgoing calls. o —Overlay line. Multiple ephone-dns share a single
                                             						  button, up to a maximum of 25 on a button. See also the c keyword. s —Silent ring. Audible ring and call-waiting beep
                                             						  are suppressed for incoming calls. The only visible cue is a flashing ((<
                                             						  icon in the phone display. Note In
                                                   						Cisco IOS Release 12.4(4)XC and later releases, the silent ringing behavior is
                                                   						overridden during active night-service periods. Silent ringing does not apply
                                                   						during designated night-service periods when the s keyword is
                                                   						used. w —Watch mode
                                             						  for all lines on the phone for which this directory number is the primary line.
                                             						  Visible line status indicates whether watched phone is idle or not. | Note | In
                                                   						Cisco IOS Release 12.4(4)XC and later releases, the silent ringing behavior is
                                                   						overridden during active night-service periods. Silent ringing does not apply
                                                   						during designated night-service periods when the s keyword is
                                                   						used. |
| Note | In
                                                   						Cisco IOS Release 12.4(4)XC and later releases, the silent ringing behavior is
                                                   						overridden during active night-service periods. Silent ringing does not apply
                                                   						during designated night-service periods when the s keyword is
                                                   						used. |
| dn-tag | Ephone-dn tag that was previously defined using the ephone-dn command. When used with the c and o keywords, the dn-tag argument can contain up to 25 individual dn-tags,
                                          						separated by commas. |
| x | Separator that creates an overlay rollover button. When the overlay button
                                          						specified in this command is occupied by an active call, a second call to one
                                          						of its ephone-dns will appear on this button. This button is also known as an
                                          						overlay expansion button. |
| overlay-button-number | Number
                                          						of the overlay button that should overflow to this button. |

| Note | The
                                                   						Cisco Unified IP Phone 7910G has only one physical line button, but you can
                                                   						assign it two button–ephone-dn pairs. |
|---|---|

| Note | In
                                                   						Cisco IOS Release 12.4(4)XC and later releases, the silent ringing behavior is
                                                   						overridden during active night-service periods. Silent ringing does not apply
                                                   						during designated night-service periods when the s keyword is
                                                   						used. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						ITS 1.0 | This
                                          						command was introduced |
| 12.2(8)T | Cisco
                                          						ITS 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. |
| 12.2(11)YT | Cisco
                                          						ITS 2.1 | The b and s keywords were added. |
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 | The f , m , and o keywords
                                          						were added. |
| 12.3(4)T | Cisco
                                          						CME 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.3(11)XL | Cisco
                                          						CME 3.2.1 | The c keyword
                                          						was added and the ability to use the m keyword
                                          						to monitor call-park slots was added. |
| 12.3(14)T | Cisco
                                          						CME 3.3 | This
                                          						command was integrated into Cisco IOS Release 12.3(14)T. |
| 12.4(4)XC | Cisco
                                          						Unified CME 4.0 | The x keyword was added and the number of ephone-dns
                                          						that can be overlaid on a single button with the o or c keyword
                                          						was increased from 10 to 25. The interaction between the keyword and night
                                          						service was modified; silent ringing is overridden when night service is
                                          						active. |
| 12.4(9)T | Cisco
                                          						Unified CME 4.0 | The
                                          						modifications made to this command were integrated into Cisco IOS Release
                                          						12.4(9)T. |
| 12.4(11)XJ3 | Cisco
                                          						Unified CME 4.1 | The w keyword
                                          						was added. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | This
                                          						command with the w keyword
                                          						was integrated into Cisco IOS Release 12.4(15)T. |

| Note | After adding
                                       		  or changing a phone button configuration using this command, you must perform a
                                       		  quick reboot of the phone using the restart command. |
|---|---|

| Note | In general,
                                       		  all the ephone-dns within an overlay must be of the same type (dual-line or
                                       		  single line mode). |
|---|---|

| Command | Description |
|---|---|
| call-waiting beep | Allows phone buttons to accept or generate call-waiting beeps. |
| restart (ephone) | Performs a fast reboot of a single phone associated with a Cisco Unified CME
                                          						router. |
| restart (telephony-service) | Performs a fast reboot of one or all phones associated with a Cisco Unified CME
                                          						router. |
| show ephone | Displays information about ephones and the corresponding Cisco Unified IP
                                          						phones. |
| show ephone overlay | Displays the configuration and current status of registered overlay ephone-dns. |

| button-string | (Optional) Specifies a comma-separated list of physical
                                          						button number or ranges of button numbers. |
|---|---|
| button-type | (Optional) Specifies one of the following button types:
                                          						Line, Speed-Dial, BLF-Speed-Dial, Feature, URL. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Note | The first button needs to be the line button so that the phone can
                                       		  complete provisioning. |
|---|---|

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies template to an ephone. |
| show voice register template | Displays all configuration information associated with a
                                          						SIP phone template. |

| phone-type | Type of IP phone. The following choices are valid: 7931 —Cisco Unified IP Phone
                                             						  7931. |
|---|---|
| 1 | Number of fixed line or feature set containing the
                                          						following buttons: Button 24—Menu. Button 23—Headset. |
| 2 | Number of fixed line or feature set containing the
                                          						following buttons: Button 24—Menu. Button 23—Headset. Button 22—Directories. Button 21—Messages. |
| button-string | (Optional) Specifies a coma separated list of physical
                                          						button number or ranges of button numbers. |
| button-type | (Optional) Specifies one of the following button types:
                                          						Line, Speed-Dial, BLF-Speed-Dial, Feature, URL |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(6)XE | Cisco Unified CME 4.0(2) | This command was introduced. |
| 12.4(4)XC4 | Cisco Unified CME 4.0(3) | This command was introduced. |
| 12.4(11)T | Cisco Unified CME 4.0(3) | This command was integrated into Cisco IOS Release
                                          						12.4(11)T. |
| 15.1(3)T | Cisco Unified CME 8.5 | This command was modified. Button String and Button Type
                                          						arguments were added. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies template to an ephone. |
| show telephony-service ephone-template | Displays ephone-template configurations. |