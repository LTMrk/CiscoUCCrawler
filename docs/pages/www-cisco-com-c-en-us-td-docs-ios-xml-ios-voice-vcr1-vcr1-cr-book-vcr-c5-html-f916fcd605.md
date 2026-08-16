---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr1-vcr1-cr-book-vcr-c5-html-f916fcd605
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr1/vcr1-cr-book/vcr-c5.html
retrieved_at: 2026-08-16T23:15:48.537013+00:00
---

Cisco IOS Voice Command Reference - A through C

# Cisco IOS Voice Command Reference - A through C

Updated: April 25, 2026

Chapter: ccs connect (controller) through clear vsp statistics

## Chapter: ccs connect (controller) through clear vsp statistics

# ccs connect (controller) through clear vsp statistics

## ccs connect (controller)

To configure a common channel signaling (CCS) connection on an
                              		  interface configured to support CCS frame forwarding, use the ccs connect command in controller configuration mode.
                              		  To disable the CCS connection on the interface, use the no form of this command.

ccs
                                 				  connect { serial | atm } number [ [dlci] |
                                 						pvc vpi/vci |
                                 						pvc name ] [ cid-number ]

no ccs
                                 				  connect { serial | atm } number [ [dlci] |
                                 						pvc vpi/vci |
                                 						pvc name ] [ cid-number ]

### Syntax Description

serial

Makes a serial CCS connection for Frame Relay.

atm

Makes an ATM CCS connection.

dlci

(Optional) Specifies the data-link connection identifier
                                          						(DLCI) number.

pvc vpi / vci

(Optional) Specifies the permanent virtual circuit (PVC)
                                          						virtual path identifier (VPI) or virtual channel identifier (VCI). Range is
                                          						from 0 to 255; the slash is required.

pvc name

(Optional) Specifies the PVC string that names the PVC for
                                          						recognition.

cid-number

(Optional) If you have executed the ccs encap frf11 command, the cid-number argument allows you to
                                          						specify any channel identification (CID) number from 5 to 255.

### Command Default

No CCS connection is made.

### Command Modes

Controller configuration (config-controller)

## Command History

Release

Modification

12.0(2)T

This command was introduced on the Cisco MC3810.

12.0(7)XK

The cidnumber argument was added; the dlci keyword and vcd options were removed.

12.1(2)T

The CID syntax addition and removal of the dlci keyword and vcd options were integrated into
                                          						Cisco IOS Release 12.1(2)T.

12.1(2)XH

This command was implemented on the Cisco 2600 series,
                                          						Cisco 3600 series, Cisco 7200 series, and Cisco 7500 series.

12.1(3)T

This command was integrated into Cisco IOS Release
                                          						12.1(3)T.

### Usage Guidelines

Use this command to configure a CCS connection. If the CCS connection
                              		  is over Frame Relay, specify a serial interface and the DLCI. If the CCS
                              		  connection is over ATM, specify atm , the slot number, and the PVC.

If you have executed the ccs encap frf11 command, the cidnumber option of the ccs connect command allows you to specify any CID from
                              		  5 to 255. If you do not issue the ccs encap frf11 command, Cisco encapsulation is used, and
                              		  any CID value other than 254 is ignored.

CDP and keepalives are disabled by default on a D-channel
                                          		  interface.

## Examples

To configure a Frame Relay CCS frame-forwarding connection on DLCI
                              		  100 by using the default CID of 254, enter the following command:

```
ccs connect serial 1 100
```

or:

```
ccs connect serial 1 100 10
```

To configure a CCS frame-forwarding connection over an ATM PVC, enter
                              		  the following command:

```
ccs connect atm 0 pvc 100/10
```

or:

```
ccs connect atm 0 pvc 10/100 21
```

or:

```
ccs connect atm 0 pvc mypvc 10 21
```

To configure a Frame Relay CCS frame-forwarding connection on DLCI
                              		  100 using a CID of 110, enter the following command:

```
ccs connect serial 1 100 110
```

### Related Commands

Command

Description

ccs encap frf11

Allows the specification of the standard Annex-C FRF.11
                                          						format.

## ccs connect (interface)

To configure a common channel signaling (CCS) connection on an interface configured to support CCS frame forwarding, use
                              the ccs connect command in interface configuration mode. To disable the CCS connection on the interface, use the no form of this command.

ccs connect { serial | atm } [ dlci | pvc vpi/vci | pvc name ] [ cid-number ]

no ccs connect { serial | atm } [ dlci | pvc vpi/vci | pvc name ] [ cid-number ]

### Syntax Description

serial

Makes a serial CCS connection for Frame Relay.

atm

Makes an ATM CCS connection.

dlci

(Optional) Data-link connection identifier (DLCI) number.

pvc vpi / vci

(Optional) Permanent virtual circuit (PVC) virtual path identifier or virtual channel identifier (VCI). Range is from 0 to
                                          255; the slash is required.

pvc name

(Optional) PVC string that names the PVC for recognition.

cid - number

(Optional) If you have executed the ccs encap frf11 command, the cid-number argument allows you to specify any channel identification (CID) number from 5 to 255.

### Command Default

No CCS connection is made.

### Command Modes

Interface configuration (config-if)

## Command History

Release

Modification

12.0(2)T

This command was introduced on the Cisco MC3810.

12.0(7)XK

The cid-number argument was added; the dlci keyword and vcd options were removed.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.2(2)T

This command was implemented on the Cisco 7200 series router and integrated into Cisco IOS Release 12.2(2)T.

### Usage Guidelines

Use this command to configure a CCS connection. If the CCS connection is over Frame Relay, specify a serial interface and
                              the DLCI. If the CCS connection is over ATM, specify atm , the interface number (0), and the PVC.

If you have executed the ccs encap frf11 command, the cid - number option of the ccs connnect command allows you to specify any CID from 5 to 255. If you do not issue the ccs encap frf11 command, Cisco encapsulation is used, and any CID value other than 254 is ignored.

Cisco Discovery Protocol and keepalives are disabled by default on a D-channel interface.

## Examples

To configure a Frame Relay CCS frame-forwarding connection on DLCI 100 by using the default CID of 254, enter the following
                              command:

```
ccs connect serial 1 100
```

or

```
ccs connect serial 1 100 10
```

To configure a CCS frame-forwarding connection over an ATM PVC, enter the following command:

```
ccs connect atm 0 pvc 100/10
```

or

```
ccs connect atm 0 pvc 10/100 21
```

or

```
ccs connect atm 0 pvc mypvc 10 21
```

To configure a Frame Relay CCS frame-forwarding connection on DLCI 100 using a CID of 110, enter the following command:

```
ccs connect serial 1 100 110
```

### Related Commands

Command

Description

ccs encap frf11

Allows the specification of the standard Annex-C FRF.11 format.

## ccs encap frf11

To configure the common channel signaling (CCS) packet encapsulation format for FRF.11, use the ccs encap frf11 command in interface configuration mode. To disable CCS encapsulation for FRF11, use the no form of this command.

ccs encap frf11

no ccs encap frf11

### Syntax Description

This command has no arguments or keywords.

### Command Default

By default, the format is a Cisco packet format, using a channel ID (CID) of 254.

### Command Modes

Interface configuration (config-if)

## Command History

Release

Modification

12.0(7)XK

This command was introduced for the Cisco MC3810.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.1(2)XH

This command was implemented on the Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, and Cisco 7500 series.

12.1(3)T

This command was integrated into Cisco IOS Release 12.1(3)T.

### Usage Guidelines

This command allows the specification of the standard Annex-C format. Use this command to define the packet format for the
                              CCS packet; it places the FRF.11 Annex-C (Data Transfer Syntax) standard header on the CCS packets only.

Once the ccs encap frf11 command is executed, you can use the ccs connect command to specify a CID other than 254.

## Examples

The following example shows how to configure a serial interface for Frame Relay:

```
interface Serial1:15
 ccs encap frf11
 ccs connect Serial0 990 100
```

### Related Commands

Command

Description

mode ccs frame-forwarding

Set to forward frames on the controller.

ccs connect

Configures a CCS connection on an interface configured to support CCS frame forwarding.

## cdr-format

To select the format of the call detail records (CDRs) generated for file accounting, use the cdr-format command in gateway accounting configuration mode. To reset to the default, use the no form of this command.

cdr-format { compact | detailed }

no cdr-format

### Syntax Description

compact

Compact set of voice attributes is generated in CDRs.

detailed

Full set of voice attributes is generated in CDRs. Default value.

### Command Default

Detailed (full version of CDRs is generated).

### Command Modes

Gateway accounting file configuration (config-gw-accounting-file)

## Command History

Release

Modification

12.4(15)XY

This command was introduced.

12.4(20)T

This command was integrated into Cisco IOS Release 12.4(20)T.

### Usage Guidelines

This command determines whether the CDRs generated by the file accounting process contain the complete set of voice attributes
                              or a compact set of 17 voice attributes.

For a list of the complete set of voice attributes generated with the detailed keyword, see the "VSAs Supported by Cisco Voice Products" section in the RADIUS VSA Voice Implementation Guide .

The name and order of the attributes generated with the compact keyword are: CallLegType, ConnectionId, SetupTime, PeerAddress, PeerSubAddress, DisconnectCause, DisconnectText, ConnectTime,
                              DisconnectTime, CallOrigin, ChargedUnits, InfoType, TransmitPackets, TransmitBytes, ReceivePackets, ReceiveBytes, feature_vsa.

## Examples

The following example shows the CDR format set to compact:

```
gw-accounting file
 primary ftp server1/cdrtest1 username bob password temp
 maximum buffer-size 60
 maximum fileclose-timer 720
 cdr-format compact
```

### Related Commands

Command

Description

acct-template

Selects a group of voice vendor-specific attributes to collect in accounting records.

maximum buffer-size

Sets the maximum size of the file accounting buffer.

maximum fileclose-timer

Sets the maximum time for saving records to an accounting file before closing the file and creating a new one.

primary

Sets the primary location for storing the CDRs generated for file accounting.

## ces-clock

To configure the clock for the Circuit Emulation Services (CES) interface, use the ces - clock command in controller configuration mode. To disable the CES clock, use the no form of this command.

ces-clock { adaptive | srts | synchronous }

no ces-clock { adaptive | srts | synchronous }

### Syntax Description

adaptive

Adjusts the output clock on a received ATM adaptation layer 1 (AAL1) on a first-in, first-out basis. Use in unstructured mode.

srts

Sets the clocking mode to synchronous residual time stamp.

synchronous

Configures the timing recovery to synchronous for structured mode.

### Command Default

The default setting is synchronou.s

### Command Modes

Controller configuration (config-controller)

## Command History

Release

Modification

12.1(2)T

This command was introduced.

### Usage Guidelines

This command is used on Cisco 3600 series routers that have OC-3/STM-1 ATM CES network modules.

## Examples

The following example configures the CES clock mode for synchronous residual time stamp:

```
ces-clock srts
```

### Related Commands

Command

Description

controller

Configures the T1 or E1 controller.

## cgma-agent

To enable the Cisco Gateway Management Agent (CGMA) on the Cisco IOS gateway, use the cgma - agent command in global configuration mode. To disable the CGMA, use the no form of this command.

cgma-agent [ tcp-port number | time-period seconds ]

no cgma-agent

### Syntax Description

tcp - port number

(Optional) Specifies the TCP port number for the CGMA to use in communication with a third-party management system. Range
                                          is from 5000 to 65535. The default is 5000.

time - period s econds

(Optional) Specifies the maximum time period, in seconds ,for maintaining the link between the CGMA and the third-party management
                                          system during a period of inactivity. If twice the timeout value is met or exceeded with no message received from the client,
                                          the TCP connection is closed. Additionally, a 60-second timer is maintained in the CGMA, which closes the connection if no
                                          handshake query message is received from the third-party management system for 60 seconds. Range is from 45 to 300. The default
                                          is 45.

### Command Default

Default number value is 5000.
                              Default seconds value is 45.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.2(2)XB

This command was introduced on the Cisco 2600 series, Cisco 3600 series, Cisco AS5300, Cisco AS5350, and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5800 for Cisco IOS release 12.2(2)XB1 release only.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 2600 series, Cisco 3600 series, and
                                          Cisco 7200 series. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5800 is not included in this release.

### Usage Guidelines

Use this command to enable the CGMA on the Cisco IOS gateway. The CGMA communicates with the third-party management system
                              to provide real-time information for gateway management, including the following:

Handshake query, status query, and response messages between the CGMA and the third-party management system.

Call information such as start and end of call from call detail records (CDRs) sent using eXtensible Markup Language (XML)
                                    over TCP/IP.

Shows if T1 or E1 controllers and analog ports are up or down, and are also generated at the removal or addition of a "pri-group"
                                    or "ds0-group" under the T1 or E1 controller.

## Examples

The following example shows that the CGMA is enabled on TCP port 5300 and that the CGMA times out after 300 seconds and closes
                              its connection to the third-party management system because of inactivity in the link:

```
Router(config)# cgma-agent tcp-port 5300 time-period 300 Router# show running-config Building configuration...
Current configuration : 1797 bytes
!
version 12.2
service config
no service single-slot-reload-enable
service timestamps debug uptime
service timestamps log uptime
no service password-encryption
!
hostname gw1
!
.
.
.
resource-pool disable
!
ip subnet-zero
no ip domain-lookup
!
no ip dhcp-client network-discovery
isdn switch-type primary-ni
!
!
!
!
!
!
cgma-agent tcp-port 5300 time-period 300
fax interface-type modem
mta receive maximum-recipients 2
!
!
controller T1 0
 framing esf
 linecode b8zs
 pri-group timeslots 1-24
!
!
interface Ethernet0
 ip address 209.165.200.225 255.255.255.0
!
interface Serial0:23
 no ip address
 isdn switch-type primary-ni
 isdn protocol-emulate network
 isdn incoming-voice modem
 isdn T310 10000
 no cdp enable
!
 
voice-port 0:D
!
dial-peer voice 1213 voip
 destination-pattern 12135550100
 session target ipv4:209.165.200.229
!
dial-peer voice 1415 pots
 destination-pattern 14155550100
 direct-inward-dial
 port 0:D
!
dial-peer voice 12136 voip
 destination-pattern 12135550120
 session target ipv4:209.165.200.229
!
dial-peer voice 14156 pots
 incoming called-number .
 direct-inward-dial
!
gateway
!
end
```

## channel-group

To configure serial
                              		  WAN on a T1 or E1 interface, use the channel-group command in controller configuration mode. To clear a channel group, use the no form of this
                              		  command.

### Cisco 2600 Series

channel-group channel-group-number timeslots range [ speed { 56 | 64 }] [ aim aim-slot-number ]

no channel-group channel-group-number

### Cisco 2611 (Cisco Signaling
                              			 Link Terminal [SLT])

channel-group channel-number

no channel-group channel-number

### Cisco ASR 901 Series, Cisco
                              			 2600XM Series, Cisco 2691, Cisco 3631, Cisco 3660, Cisco 3725, and Cisco
                              			 3745

channel-group channel-group-number { timeslots range [ speed { 56 | 64 }] | unframed } [ aim aim-slot-number ]

no channel-group [ channel-group-number timeslots range ]

### Cisco AS5350 and Cisco AS5400
                              			 Series

channel-group channel-group-number

no channel-group channel-group-number

### Cisco MC3810

channel-group channel-number timeslots range [ speed { 56 | 64 }]

no channel-group [ channel-number timeslots range ]

### Syntax Description

channel-group-number

Channel-group number on the Cisco 2600 series, Cisco 2600XM, Cisco 2691, Cisco
                                          						3631, Cisco 3660, Cisco 3725, and Cisco 3745 routers. When a T1 data line is
                                          						configured, channel-group numbers can be values from 0 to 23. When an E1 data
                                          						line is configured, channel-group numbers can be values from 0 to 30.

Valid
                                          						values can be 0 or 1 on the Cisco AS5350 and Cisco AS5400.

timeslots range

Specifies one or more time slots separated by commas, and spaces or ranges of
                                          						time slots belonging to the channel group separated by a dash. The first time
                                          						slot is numbered 1.

For
                                                							 a T1 controller, the time slots range from 1 to 24.

For
                                                							 an E1 controller, the time slots range from 1 to 31.

You can
                                          						specify a time slot range (for example, 1-29), individual time slots separated
                                          						by commas (for example 1, 3, 5), or a combination of the two (for example 1-14,
                                          						15, 17-31). See the "Examples" section for samples of different timeslot
                                          						ranges.

speed { 56 | 64 }

(Optional) Specifies the speed of the underlying DS0s in kilobits per second.
                                          						Valid values are 56 and 64.

The
                                          						default line speed when configuring a T1 controller is 56 kbps on the Cisco
                                          						2600 series, Cisco 2600XM series, Cisco 2691, Cisco 3631, Cisco 3660, Cisco
                                          						3725, Cisco 3745, and Cisco MC3810.

The
                                          						default line speed when configuring an E1 controller is 64 kbps on the Cisco
                                          						2600 series, Cisco 2600XM series, Cisco 2691, Cisco 3631, Cisco 3660, Cisco
                                          						3725, Cisco 3745, and Cisco MC3810.

The
                                          						line speed controls real-time (VBR-RT) traffic shaping, and the maximum burst
                                          						size (MBS) is 255 cells.

aim aim-slot-number

(Optional) Directs HDLC traffic from the T1/E1 interface to the
                                          						AIM-ATM-VOICE-30 digital signaling processor (DSP) card on the Cisco 2600
                                          						series, Cisco 2600XM series, Cisco 2691, Cisco 3631, Cisco 3660, Cisco 3725,
                                          						and Cisco 3745.

channel-number

Number
                                          						of the channel. Valid values can be 0 or 1 on the Cisco SLT (Cisco 2611).

unframed

Specifies the use of all 32 time slots for data. None of the 32 time slots is
                                          						used for framing signals on the Cisco ASR 901 Series, Cisco 2600XM series,
                                          						Cisco 2691, Cisco 3631, Cisco 3660, Cisco 3725, and Cisco 3745. This keyword is
                                          						applicable to E1 only.

### Command Default

The T1/E1 line is
                              		  connected to the Motorola MPC-860x processor serial communication controller
                              		  (SCC) or network module with two voice or WAN interface card (VIC or WIC) slots
                              		  and 0/1/2 FastEthernet ports DSCC4 by default on Cisco 2600 series, Cisco
                              		  2600XM, Cisco 2691, Cisco 3631, Cisco 3660, Cisco 3725, and Cisco 3745 routers.

There is no
                              		  default behavior or values on the Cisco SLT (Cisco 2611).

The serial
                              		  interface object encapsulation is set to HDLC on a network access server (NAS)
                              		  (Cisco AS5350 and Cisco AS5400 series routers).

The default line
                              		  speed is 56 kbps when a T1 controller is configured on the Cisco 2600 series,
                              		  Cisco 2600XM series, Cisco 2691, Cisco 3631, Cisco 3660, Cisco 3725, Cisco
                              		  3745, and the Cisco MC3810.

The default line
                              		  speed is 64 kbps when an E1 controller is configured on the Cisco 2600 series,
                              		  Cisco 2600XM series, Cisco 2691, Cisco 3631, Cisco 3660, Cisco 3725, Cisco
                              		  3745, and the Cisco MC3810.

### Command Modes

Controller configuration (config-controller)

## Command History

Release

Modification

11.3MA

This
                                          						command was introduced on the Cisco MC3810.

12.0

This
                                          						command was integrated into Cisco IOS Release 12.0 on the Cisco MC3810.

12.0(7)XE

This
                                          						command was implemented on the Catalyst 6000 family switches.

12.1(1)E

This
                                          						command was integrated into Cisco IOS Release 12.1(1)E.

12.1(1)T

This
                                          						command was modified to accommodate two channel groups on a port on 1- and
                                          						2-port T1/E1 multiflex voice or WAN interface cards on the Cisco 2600 and Cisco
                                          						3600 series routers.

12.1(3a)E3

The
                                          						number of valid values for the kbps argument
                                          						was changed on the Cisco MC3810; see the "Usage Guidelines" section for valid
                                          						values.

12.2(11)T

This
                                          						command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(15)T

The aim keyword
                                          						was added for use on the Cisco 2600 series (including the Cisco 2691), Cisco
                                          						2600XM, Cisco 3660, Cisco 3725, and Cisco 3745.

12.3(1)

The unframed keyword was added for use on the Cisco 2600XM series, Cisco 2691, Cisco 3631,
                                          						Cisco 3660, Cisco 3725, and Cisco 3745.

12.2SX

This
                                          						command is supported in the Cisco IOS Release 12.2SX train. Support in a
                                          						specific 12.2SX release of this train depends on your feature set, platform,
                                          						and platform hardware.

15.4(3)S

This command was implemented on the Cisco ASR 901 Series
                                          						Aggregation Services Router.

### Usage Guidelines

Use this command
                              		  to direct HDLC traffic from the T1/E1 interface to the AIM-ATM-VOICE-30 DSP
                              		  card. A channel group is created using Advanced Integration Module (AIM) HDLC
                              		  resources when a channel-group command with the aim keyword
                              		  is parsed during system initialization or when the command is entered during
                              		  configuration. You must specify the aim keyword
                              		  under a T1/E1 controller port to direct HDLC traffic from the T1/E1 interface
                              		  to the AIM-ATM-VOICE-30 DSP card on the Cisco 2600 series, Cisco 2600XM series,
                              		  Cisco 2691, Cisco 3631, Cisco 3660, Cisco 3725, and Cisco 3745.

Neither the
                                          			 Cisco AS5400 series NAS nor the Cisco MC3810 is supported with the integrated
                                          			 voice and data WAN on T1/E1 interfaces using the AIM-ATM-VOICE-30 module.

If previous channel-group commands are configured with the aim keyword,
                              		  subsequent channel-group commands without the aim keyword
                              		  are rejected. Similarly, if a regular channel-group command is followed by another channel-group command with the aim keyword
                              		  implemented, the second command is rejected on the Cisco 2600 and Cisco 2600XM.

A channel group
                              		  using AIM HDLC resources is deleted only when a no channel-group command is entered.

By default,
                              		  the channel-group command on a NAS sets the serial
                              		  interface object encapsulation to HDLC. You must override the default by
                              		  entering the encapsulation ss7 command
                              		  for that serial interface object. Once you override the default, encapsulation
                              		  cannot be changed again for that object. The SS7 encapsulation option is new to
                              		  the Integrated Signaling Link Terminal feature and is available only for
                              		  interface serial objects created by the channel-group command. The Integrated Signaling
                              		  Link Terminal feature added SLT functionality on Cisco AS5350 and Cisco AS5400
                              		  platforms.

A digital SS7
                              		  link can be deleted by entering the no channel-group channel-group-number command on the associated
                              		  T1/E1 controller. The link must first be stopped using the no shutdown command. It is not necessary to remove the channel ID association first.

Use the channel-group command in configurations where the router or access server must communicate
                              		  with a T1 or E1 fractional data line. The channel group number may be
                              		  arbitrarily assigned and must be unique for the controller. The time-slot range
                              		  must match the time slots assigned to the channel group. The service provider
                              		  defines the time slots that comprise a channel group.

Channel groups,
                                          			 channel-associated signaling (CAS) voice groups, DS0 groups, and time-division
                                          			 multiplexing (TDM) groups all use group numbers. All group numbers configured
                                          			 for channel groups, CAS voice groups, and TDM groups must be unique on the
                                          			 local Cisco MC3810 concentrator. For example, you cannot use the same group
                                          			 number for a channel group and for a TDM group. Furthermore, on the Cisco
                                          			 MC3810, only one channel group can be configured on a controller.

The channel group
                              		  number can be 0 or 1 on the Cisco SLT (Cisco 2611).

The channel-group command also applies to Voice over Frame Relay, Voice over ATM, and Voice over
                              		  HDLC on the Cisco MC3810.

## Examples

The following
                              		  example shows basic configuration directing HDLC traffic from the T1/E1
                              		  interface to the AIM-ATM-VOICE-30 DSP card, starting in global configuration
                              		  mode:

```
Router(config)# controller e1 1/0 Router(config-controller)# clock source internal Router(config-controller)# channel-group 0 timeslots 1-31 aim 0
```

The following
                              		  example explicitly sets the encapsulation type to PPP to override the HDLC
                              		  default:

```
Router# configure terminal Router(config)# controller t1 6/0 Router(config-controller)# channel-group 2 timeslots 3 aim 0 Router(config-controller)# exit Router(config)# interface serial 6/0:2 Router(config-if)# encapsulation ppp Router(config-if)# ip address 10.0.0.1 255.0.0.0 Router(config-if)# no shutdown Router(config-if)# end
```

The following
                              		  example shows how to explicitly set the encapsulation type to SS7 to override
                              		  the HDLC default using the Integrated Signaling Link Terminal feature. This
                              		  example uses an 8PRI DFC card inserted into slot 7, and DS0-timeslot 3 on trunk
                              		  5 of that card is used as an SS7 link:

```
Router# configure terminal Router(config)# controller t1 7/5 Router(config-controller)# channel-group 2 timeslots 3 Router(config-controller)# exit Router(config)# interface serial 7/5:2 Router(config-if)# encapsulation ss7 Router(config-if)# channel-id 0 Router(config-if)# no shutdown Router(config-if)# end
```

The following
                              		  example defines three channel groups. Channel-group 0 consists of a single time
                              		  slot, channel-group 8 consists of seven time slots and runs at a speed of 64
                              		  kbps per time slot, and channel-group 12 consists of two time slots.

```
Router(config-controller)# channel-group 0 timeslots 1 Router(config-controller)# channel-group 8 timeslots 5,7,12-15,20 speed 64 Router(config-controller)# channel-group 12 timeslots 2
```

The following
                              		  example configures a channel group on controller T1 0 on a Cisco MC3810:

```
Router(config)# controller T1 0 Router(config-controller)# channel-group 10 timeslots 10-64
```

The following
                              		  example configures a channel group on controller E1 1 and specifies that all
                              		  time slots are used for data:

```
controller e1 1
channel-group 1 unframed
```

SS7 digital
                                          			 F-link support for the 8PRI line card requires use of a third onboard TDM
                                          			 stream to route trunk DS0 messages to the onboard MGCs.

### Related Commands

Command

Description

framing

Specifies the frame type for the T1 or E1 data line.

invert data

Enables
                                          						channel inversion.

linecode

Specifies the line code type for the T1 or E1 line.

voice-card

Configures a card with voice processing resources and enters voice card
                                          						configuration mode.

encapsulation

Sets
                                          						the encapsulation type.

## channel-id

To assign a session channel ID to a SS7 serial link or assign an SS7 link to an SS7 session set on a Cisco AS5350 or Cisco
                              AS5400, use the channel-id command in interface configuration mode. To disable a session channel ID link, use the no form of this command.

channel-id channel-id [ session-set session-set-id ]

no channel-id

### Syntax Description

channel - id

A unique session channel ID. This session channel ID is needed when the link with a Reliable User Datagram Protocol (RUDP)
                                          session to the Media Gateway Controller (MGC) is associated.

session - set session - set - id

(Optional) Creates an SS7-link-to-SS7-session-set association on the Cisco AS5350- and Cisco AS5400-based Cisco Signaling
                                          Link Terminals (SLTs).

The session-set-id argument represents the SS7 session ID. Valid values are 0 or 1. Default is 0.

### Command Default

No default behavior or values

### Command Modes

Interface configuration (config-if)

## Command History

Release

Modification

12.2(11)T

This command was introduced on the Cisco AS5350 and Cisco AS5400.

12.2(15)T

The session-set session-set-id keyword and argument were added.

### Usage Guidelines

The channel-id command is visible only if the object’s encapsulation type is changed to SS7.

Before an SS7 serial link can be enabled using the no shutdown command, you must enter the channel-id command in interface configuration mode to assign a session channel ID to the SS7 serial link. This ID is unique to the Cisco
                              AS5350 and Cisco AS5400, and the command is visible only for provisioned objects whose encapsulation type is the new SS7 value.

The channel identifier is reserved when you explicitly assign an ID using the channel-id command for the associated serial interface object. This fails if the selected channel identifier is currently assigned to
                              another link or if all channel identifiers are already assigned.

A channel identifier is released when the no channel-id command is entered. The link must first be shut down to do this. If the no channel-id command is used with the Mulitple OPC Support for the Cisco Signaling Link Terminal feature, the associated SS7 link has
                              no channel ID. In this state the link is not fully configured and is incapable of supporting signaling traffic.

If the session - set keyword is omitted, the command is applied to SS7 session set 0, which is the default. Reissuing the session - set keyword with a different SS7 session ID is sufficient to remove the associated SS7 link from its existing SS7 session set
                              and add it to the new one.

## Examples

The following example shows a unique session channel ID zero being assigned to the Cisco AS5350 or Cisco AS5400:

```
Router(config-if)# channel-id 0
```

The following example assigns an SS7 link to an SS7 session set on a Cisco AS5350 or Cisco AS5400:

```
Router(config-if)# channel-id 0 session-set 1
```

### Related Commands

Command

Description

channel-group

Assigns a channel group and selects the DS0 timeslot desired for SS7 links.

encapsulation ss7

Sets the encapsulation type to SS7.

no shutdown

Changes the administrative state of a port from out-of-service to in-service .

session-set

Creates an SS7-link-to-SS7-session-set association or to associate an SS7 link with an SS7 session set on the Cisco 2600-based
                                          SLT.

ss7 mtp2 variant bellcore

Configures the device for Telcordia (formerly Bellcore) standards.

## cipher (voice class)

To configure the cipher settings, and associate it to a TLS profile, use the cipher command in voice class configuration mode. To delete the cipher configuration, use the no form of this command.

cipher { ecdsa-cipher [ curve-size 384 ] | strict-cipher }]

no cipher

### Syntax Description

ecdsa-cipher

(Optional) When the ecdsa-cipher keyword is not specified, the SIP TLS process uses larger set of ciphers depending on the support at the Secure Socket Layer
                                          (SSL).

Following are the cipher suites that are supported:

TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256

TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384

TLS13_AES128_GCM_SHA256

TLS13_AES256_GCM_SHA384

TLS13_CHACHA20_POLY1305_SHA256

Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                                      within the system settings, they are no longer negotiable and will not be used for secure connections.

CHACHA20_POLY1305_SHA256

DHE_RSA_WITH_AES_256_CBC_SHA

curve-size 384

(Optional) Configures specific size of elliptic curves to be used for a TLS session. You can configure an elliptic curve of
                                          size 384 bit.

strict-cipher

(Optional) The strict-cipher keyword supports only the TLS Rivest, Shamir, and Adelman (RSA) encryption with the Advanced Encryption Standard-128 (AES-128)
                                          cipher suite.

Following are the cipher suites that are supported:

TLS_RSA_WITH_AES_128_CBC_SHA

TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256

TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA256

TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

TLS13_AES128_GCM_SHA256

TLS13_AES256_GCM_SHA384

TLS13_CHACHA20_POLY1305_SHA256

Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                                      within the system settings, they are no longer negotiable and will not be used for secure connections.

CHACHA20_POLY1305_SHA256

DHE_RSA_WITH_AES_256_CBC_SHA

When the strict-cipher keyword is
                                                      not specified, the SIP TLS process uses the default set of
                                                      ciphers depending on the support at the Secure Socket Layer
                                                      (SSL).

In the Cisco IOS XE 17.18.2 release, a security warning message appears for strict-cipher configurations. The strict-cipher includes weaker ciphers such as:

DHE_RSA_WITH_AES_128_CBC_SHA

DHE_RSA_WITH_AES_256_CBC_SHA

RSA_WITH_AES_128_CBC_SHA

RSA_WITH_AES_256_CBC_SHA

### Command Default

No default behavior or values

### Command Modes

Voice class configuration (config-class)

## Command History

Release

Modification

Cisco IOS XE 26.1.1

The command is modified to indicate that the following non-compliant ciphers are not supported:

CHACHA20_POLY1305_SHA256

DHE_RSA_WITH_AES_256_CBC_SHA

Cisco IOS XE 17.18.2

This command is modified to display security warnings for usage of legacy TLS and associated weaker ciphers.

Cisco IOS XE 17.14.1a

This command is modified to support TLS version 1.3 ciphers.

Introduced support for TLS version 1.3 ciphers Yang Model.

Cisco IOS XE Amsterdam 17.3.1a

This command was introduced under voice class configuration mode.

Introduced support for Yang Model.

### Usage Guidelines

The cipher configuration is associated to a TLS profile through the command voice class tls-profile tag . The tag associates the cipher configuration to the command crypto signaling .

By default, the Secure Socket Layer (SSL) on CUBE supports the following cipher suites:

TLS_ECDHE_ECDSA_AES256_GCM_SHA384

TLS_ECDHE_ECDSA_AES128_GCM_SHA256

TLS_ECDHE_RSA_AES128_GCM_SHA256

TLS_ECDHE_RSA_AES256_GCM_SHA384

TLS_DHE_RSA_AES256_GCM_SHA384

TLS_DHE_RSA_AES128_GCM_SHA256

TLS_DHE_RSA_AES256_CBC_SHA256

TLS_DHE_RSA_AES128_CBC_SHA256

TLS_RSA_WITH_AES_128_CBC_SHA

TLS_RSA_WITH_AES_256_CBC_SHA

TLS_DHE_RSA_WITH_AES_128_CBC_SHA

TLS_DHE_RSA_WITH_AES_256_CBC_SHA

TLS_1_3_AES128_GCM_SHA256

TLS_1_3_AES256_GCM_SHA384

TLS_1_3_CHACHA20_POLY1305_SHA256

Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                          within the system settings, they are no longer negotiable and will not be used for secure connections.

CHACHA20_POLY1305_SHA256

DHE_RSA_WITH_AES_256_CBC_SHA

## Examples

The following example illustrates how to create a voice class tls-profile and associate elliptic curve settings required for a TLS session:

```
Router(config)#voice class tls-profile 2
Router(config-class)#cipher ecdsa-cipher curve-size 384
```

## Examples

The following example illustrates a security warning message display for strict-cipher configurations, for Cisco IOS XE 17.18.2 release:

```
Router(config)# voice class tls-profile 2 Router(config-class)# cipher strict-cipher SECURITY WARNING - Module: VOICE, Command: cipher strict-cipher, Reason: strict-cipher includes weak ciphers 
like RSA_WITH_AES_128_CBC_SHA, Remediation: Use stronger cipher(s) to enhance security
Router(config-class)# end

Router# sh run | sec tls-profile 2 voice class tls-profile 2
 cipher strict-cipher
```

### Related Commands

Command

Description

voice class tls-profile

Provides sub-options to configure the commands that are required for a TLS session.

crypto signaling

Identifies the trustpoint or the tls-profile tag that is used during the TLS handshake process.

## cipher (voice class tls-cipher)

To configure TLS cipher suite from the supported cipher-list, use the cipher cipher-list command in voice class configuration mode. To delete the cipher, use the no form of this command.

cipher cipher-list cipher-name

no cipher cipher-list

## Syntax Description

Specifies list of 13 supported ciphers.

The following lists the names of the cipher suite:

AES128_GCM_SHA256

AES256_GCM_SHA384

CHACHA20_POLY1305_SHA256

DHE_RSA_AES128_GCM_SHA256

DHE_RSA_AES256_GCM_SHA384

DHE_RSA_WITH_AES_128_CBC_SHA

DHE_RSA_WITH_AES_256_CBC_SHA

ECDHE_RSA_AES128_GCM_SHA256

ECDHE_RSA_AES256_GCM_SHA384

RSA_WITH_AES_128_CBC_SHA

RSA_WITH_AES_256_CBC_SHA

ECDHE_ECDSA_AES128_GCM_SHA256

ECDHE_ECDSA_AES256_GCM_SHA384

Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                                   within the system settings, they are no longer negotiable and will not be used for secure connections.

CHACHA20_POLY1305_SHA256

DHE_RSA_WITH_AES_256_CBC_SHA

### Command Default

No default behavior or values

### Command Modes

voice class configuration (config-class)

## Command History

Release

Modification

Cisco IOS XE 26.1.1

The command is modified to indicate that the following non-compliant ciphers are not supported:

CHACHA20_POLY1305_SHA256

DHE_RSA_WITH_AES_256_CBC_SHA

Cisco IOS XE 17.18.2

The command is modified to display security warnings for usage of legacy TLS and associated weaker ciphers.

Cisco IOS XE 17.14.1a

Introduced support for TLS version 1.3 ciphers. Following are the three ciphers supported with TLS version 1.3:

AES128_GCM_SHA256

AES256_GCM_SHA384

CHACHA20_POLY1305_SHA256

Cisco IOS XE Cupertino
                                             17.8.1a

This command was introduced.

### Usage Guidelines

Use the cipher cipher-list command in voice class configuration mode.

In the Cisco IOS XE 17.18.2 release, a security warning message appears for configurations using TLS versions below 1.2 and associated weaker ciphers.
                              For secure configurations, we recommend configuring stronger ciphers with TLS version 1.2 or higher.

Following are the weaker ciphers, configuring which the warning message is displayed:

DHE_RSA_WITH_AES_128_CBC_SHA

DHE_RSA_WITH_AES_256_CBC_SHA

RSA_WITH_AES_128_CBC_SHA

RSA_WITH_AES_256_CBC_SHA

Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                          within the system settings, they are no longer negotiable and will not be used for secure connections.

CHACHA20_POLY1305_SHA256

DHE_RSA_WITH_AES_256_CBC_SHA

## Examples

The following example illustrates how to create a voice class cipher-list:

```
Device(config)# voice class tls-cipher 100 Device(config-class)# cipher 1 DHE_RSA_AES128_GCM_SHA256
```

## Examples

The following example illustrates a security warning message display for configurations using TLS versions below 1.2 and associated
                              weaker ciphers:

```
Device(config)#voice class tls-cipher 10
Device(config-class)# cipher 1 DHE_RSA_WITH_AES_128_CBC_SHA SECURITY WARNING - Module: VOICE, Command: cipher 1 DHE_RSA_WITH_AES_128_CBC_SHA, 
Reason: Weak cipher(s) are present in the command, Remediation: Use stronger cipher(s) to enhance security
```

### Related Commands

Command

Description

Configures an ordered set of TLS cipher suites

Identifies the trustpoint or the tls-profile tag that is used during the TLS handshake process.

## clear backhaul-session-manager group stats

To reset the statistics or traffic counters for a specified session group, use the clear backhaul-session-manager group stats command in privileged EXEC mode.

clear backhaul-session-manager group stats { all | name group-name }

### Syntax Description

all

All available session groups.

name group - name

A specified session group.

### Command Default

The statistical information accumulates.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(1)T

This command was introduced.

12.2(2)T

This command was implemented on the Cisco 7200.

12.2(4)T

This command was implemented on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco IAD2420 series.

12.2(11)T

This command was implemented on the Cisco AS5350, Cisco AS5400, and Cisco AS5850.

### Usage Guidelines

A session is the connection between a client and a server, and a session group is a collection of sessions in a group to implement
                              switchover in case of a session failure. This command clears all statistics that pertain to the backhaul session manager group.

## Examples

The following example clears all statistics for all available session groups:

```
Router(config)# clear backhaul-session-manager group stats all
```

### Related Commands

Command

Description

show backhaul-session-manager group

Displays status, statistics, or configuration of a specified group or all session groups.

## clear call application interface

To clear application interface statistics and event logs, use the clear call application interface command in privileged EXEC mode.

clear call application interface [ [ { aaa | asr | flash | http | ram | rtsp | smtp | tftp | tts } [ server server ]] [ event-log | stats ]]

### Syntax Description

aaa

Authentication, authorization, and accounting (AAA) interface type.

asr

Automatic speech recognition (ASR) interface type.

flash

Flash memory of the Cisco gateway.

http

HTTP interface type.

ram

Memory of the Cisco gateway.

rtsp

Real-Time Streaming Protocol (RTSP) interface type.

smtp

Simple Mail Transfer Protocol (SMTP) interface type.

tftp

TFTP interface type.

tts

Text-to-speech (TTS) interface type.

server server

(Optional) Clears statistics or event logs for the specified server.

event-log

(Optional) Clears event logs.

stats

(Optional) Clears statistic counters.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

### Usage Guidelines

This command resets statistic counters to zero and clears event logs for application interfaces. If you do not use any keywords
                              or arguments, this command clears statistics and event logs for all application interfaces.

## Examples

The following example clears statistics and event logs for all application interfaces:

```
Router# clear call application interface
```

### Related Commands

Command

Description

call application interface event-log

Enables event logging for external interfaces used by voice applications.

call application interface stats

Enables statistics collection for application interfaces.

clear call application stats

Clears application-level statistics in history and subtracts the statistics from the gateway-level statistics.

show call application interface

Displays event logs and statistics for application interfaces.

## clear call application stats

To clear application-level statistics in history and subtract the statistics from the gateway-level statistics, use the clear call application stats command in privileged EXEC mode.

clear call application [ app-tag application-name ] stats

### Syntax Description

app-tag application-name

(Optional) Clears statistics for the specified voice application.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

### Usage Guidelines

This command resets application-level counters in history to zero and subtracts the counters from the gateway-level history.
                              If you do not specify an application name, this command clears statistics for all applications at the application level and
                              gateway level.

Statistic counters are automatically cleared for an application if the application is deleted with the no call application voice command or the script is reloaded with the call application voice load command.

## Examples

The following example clears statistics for the application named sample_app:

```
Router# clear call application app-tag sample_app stats
```

### Related Commands

Command

Description

call application stats

Enables statistics collection for voice applications.

call application voice load

Reloads the designated Tcl script.

clear call application interface

Clears application interface statistics and event logs.

call application voice

Reloads the designated Tcl script or VoiceXML document.

show call application app-level

Displays application-level statistics for voice applications.

show call application gateway-level

Displays gateway-level statistics for voice application instances.

## clear call fallback cache

To clear the cache of the current Calculated Planning Impairment Factor (ICPIF) loss/delay busyout threshold estimates for
                              all IP addresses or a specific IP address, use the clear call fallback cache command in privileged EXEC mode.

clear call fallback cache [ip-address] [ codec codec-type ]

### Syntax Description

ip - address

(Optional) The target IP address. If no IP address is specified, all IP addresses are cleared.

codec codec-type

(Optional) Specifies the associated codec type.

### Command Default

If no IP address is specified, all IP addresses are cleared.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series routers.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)T

This command was modified. The Public Switching Telephone Network (PSTN) Fallback feature and enhancements were implemented
                                          on the Cisco 7200 series routers and integrated into Cisco IOS Release 12.2(4)T.

12.2(4)T2

This command was implemented on the Cisco 7500 series routers.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

15.0(1)M

This command was modified in a release earlier than Cisco IOS Release 15.0(1)M. The codec keyword and codec-type argument were added.

### Usage Guidelines

If no IP address is specified, the clear call fallback cache command clears the cache of all CPIF estimates for all IP addresses. The available codec types are, g711alaw, g711ulaw, g723ar53,
                              g723ar63, g723r53, g723r63, g726r16, g726r24, g726r32, g728, g729abr8, g729ar8, g729br8, g729r8, g729r8 pre-ietf, gsmamr-nb,
                              gsmefr, gsmfr, and None.

## Examples

The following example clears the cache of the ICPIF estimate for IP address 10.0.0.0:

```
Router# clear call fallback cache 10.0.0.0
```

### Related Commands

Command

Description

show call fallback cache

Displays the current ICPIF estimates for all IP addresses in the call fallback cache.

## clear call fallback stats

To clear the call fallback statistics, use the clear call fallback stats command in privileged EXEC mode.

clear call fallback stats

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)XB1

This command was implemented on the Cisco AS5850 platform.

12.2(4)T

The PSTN Fallback feature and enhancements were implemented on the Cisco 7200 series and integrated into Cisco IOS Release
                                          12.2(4)T.

12.2(4)T2

This command was implemented on the Cisco 7500 series.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

## Examples

The following example clears the call fallback statistics:

```
Router# clear call fallback stats
```

### Related Commands

Command

Description

show call fallback stats

Displays the call fallback statistics.

## clear callmon

To clear call monitor logs, use the clear callmon command in privileged EXEC mode.

clear callmon { dead-memory | trace }

### Syntax Description

dead-memory

Clears unreleased Communication Media Module (CMM) line card memory.

trace

Clears CMM trace buffers.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

15.0(1)M

This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M.

## Examples

The following example shows how to clear unreleased CMM memory:

```
Router# clear callmon dead-memory
```

The following example shows how to clear CMM trace buffers:

```
Router# clear callmon trace
```

### Related Commands

Command

Description

clear tgrep neighbor

Clears TGREP counters and sessions.

## clear call threshold

To clear enabled call threshold statistics, use the clear call threshold command in privileged EXEC mode.

clear call threshold interface type number { stats | total-calls [value] | int-calls [value] }

### Syntax Description

interface -

Specifies the interface through which calls arrive. Types of interfaces and their numbers depends upon the configured interfaces.

type

Interface type. Values include:

ethernet

fastethernet

GigabitEthernet

serial

number

Interface or subinterface number. For more information about the numbering syntax for your networking device, use the question
                                          mark (?) online help function.

stats

Resets all call threshold statistics.

total - calls value

Resets the counter when the call volume reaches the specified number. The value argument represents call volume. Range is from 0 to 10000 calls. The default is 0.

int-calls value

Number of calls transmitted through the interface. The value argument clears calls when they reach a specified volume through the interface. Range is from 0 to 10000 calls. The default
                                          is 0.

### Command Default

The default setting of 0 for the total - calls and int-calls keywords reset all threshold statistics immediately. stats is the default keyword.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

The command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          is not included in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)XM

This command was implemented on the Cisco 1750 and Cisco 1751 routers. Support for other Cisco platforms is not included
                                          in this release.

12.2(8)T

This command was integrated into the Cisco IOS Release 12.2(8)T and implemented on the Cisco 7200 series routers. Support
                                          for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release.

12.2(11)T

This command was implemented on the Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850.

## Examples

The following example resets all call threshold statistics:

```
clear call threshold stats
```

The following example resets the counter for all call volume in the gateway:

```
clear call threshold total-calls
```

The following example resets the counter when the call volume on Ethernet interface 0/1 reaches 5000 calls:

```
clear call threshold interface ethernet 0/1 int-calls 5000
```

The following example resets the counter for all call threshold statistics on a GigabitEthernet interface:

```
Device# clear call threshold interface GigabitEthernet stats
```

### Related Commands

Command

Description

call threshold

Enables the global resources of a gateway.

call threshold poll-interval

Enables a polling interval threshold for CPU or memory.

show call treatment

Displays the call treatment configuration and statistics for handling the calls on the basis of resource availability.

## clear call treatment stats

To clear call treatment statistics, use the clear call treatment stats command in privileged EXEC mode.

clear call treatment stats

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

The command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 series
                                          is not included in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)XM

This command was implemented on the Cisco 1750 and Cisco 1751 routers. Support for other Cisco platforms is not included in
                                          this release.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 7200 series routers. Support for
                                          the Cisco AS5300, 
                                          Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release.

12.2(11)T

This feature was integrated into Cisco IOS Release 12.2(11)T and support was added for the Cisco AS5300, Cisco AS5350, Cisco
                                          AS5400, and Cisco AS5800.

## Examples

The following example clears the call treatment statistics:

```
clear call treatment stats
```

### Related Commands

Command

Description

call treatment on

Enables call treatment to process calls when local resources are unavailable.

call treatment action

Configures the action that the router takes when local resources are unavailable.

call treatment cause-code

Specifies the reason for the disconnection to the caller when local resources are unavailable.

call treatment isdn-reject

Specifies the rejection cause-code for ISDN calls when local resources are unavailable.

show call treatment

Displays the call treatment configuration and statistics for handling calls on the basis of resource availability.

## clear call voice

To clear one or more voice calls detected as inactive because there is no RTP or RTCP activity, use the clear call voice command in User EXEC or privileged EXEC mode.

clear call voice { stale-entry | causecode identifier { id identifier | media-inactive | calling-number number | called-number number | fpi-correlator correlator-id | fpi-stale | long-dur-call }
                              							
                              						}

### Syntax Description

stale-entry

Clears entries of active calls that are deemed stale or invalid from the call table.

causecode

Specifies a Q.850 disconnect cause code.

identifier

Numeric cause code identifier; a number 1 through 127.

id identifier

Clears one specific call with the ID specified. The identifier argument is the call identifier as shown in brief format.

media-inactive

Clears calls wherever a status of media inactive is detected and notified.

calling-number number

Clears a call with a specific calling number pattern. The number argument is the specific call number pattern of the calling number.

called-number number

Clears a call with a specific called number pattern. The number argument is the specific call number pattern of a called number.

fpi-correlator correlator-id

Clears calls based on VoIP FPI correlator.

fpi-stale

Clears all hung FPI call.

long-dur-call

Clears only call with long-duration being detected and notified.

### Command Default

This command is disabled, and no calls are cleared.

### Command Modes

User EXEC (>)

Privileged EXEC (#)

## Command History

Release

Modification

12.1(3)T

This command was introduced.

12.2

This command was integrated into Cisco IOS Release 12.2.

12.3(4)T

The voice keyword was added.

12.4(4)T

The calling-number and called-number keywords were added.

15.5(2)T

The fpi-correlator keyword was added.

### Usage Guidelines

Use the clear call voice command to clear call resources at all the layers if there is a hung call. There is no no form of this command.

You can obtain the FPI correlator ID by executing the show voip fpi calls command.

## Examples

The following example clears inactive voice calls with the cause code ID 16:

```
Router# clear call voice causecode 16 fpi-correlator 2
```

## Examples

The following example shows that there are no stale entries to be cleared:

```
Router# clear call voice stale-entry No stale entry found
```

### Related Commands

Command

Description

show call active voice

Displays active voice calls, based on specified parameters.

## clear call-router routes

To remove the dynamic routes cached in the border element (BE), use the clear call - router routes command in privileged EXEC mode.

clear call-router routes

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          is not included in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T. and implemented on the Cisco AS5300, Cisco AS5350, Cisco AS5400,
                                          and Cisco AS5850.

## Examples

The following example shows how to remove dynamic routes cached in the BE:

```
Router# clear call-router routes
```

### Related Commands

Command

Description

call-router

Enables the Annex G BE configuration commands.

show call history

Displays the fax history table for a fax transmission.

## clear controller call-counters

To clear the system DS0 high water marks (HWMs) and all individual controller statistics, use the clear controller call-counters command in privileged EXEC mode.

clear controller call-counters { system-hwm | all }

### Syntax Description

system - hwm

Clears the system HWMs only.

all

Clears all controller call counters including the individual controller time slots in use and the number of calls on those
                                          time slots since the last reset was done. The HWMs are set to 0.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(1)T

This command was introduced.

12.1(1)T

This command was implemented on the voice/WAN interface cards (VWICs) for the Cisco 2600 series and Cisco 3600 series.

12.1(2)T

This command was implemented on the Cisco AS5300, Cisco AS5400, and Cisco AS5800.

### Usage Guidelines

The clear controller call-counters all command clears the system DS0 HWMs and all individual controller statistics, including TotalCalls and Total Duration. The clear controller call-counters system-hwm command clears the system DS0 HWMs and leaves all other call-counter statistics untouched.

Refer to the following comments for the meaning of call counters displayed before and after executing the clear controller call-counters and clear controller t1 call-counters related commands:

The numbers displayed under TotalCalls for each time slot represent total calls that were connected successfully. If a call
                                    comes into time slot 10, then the show controllers t1 call-counters command displays 1 under the TotalCalls column for time slot 10. A value of 20 displayed under TotalCalls for time slot 10
                                    indicates a total of 20 calls connected on time slot 10 since the last time call counters were cleared.

The DS0s Active field indicates the number of active calls on the specified controller. This number indicates the current
                                    number of calls on the controller at any given time.

The DS0s Active High Water Mark field indicates the peak number of calls on the controller since the last time HWMs or calls
                                    were cleared. If the number of active calls "DS0s Active" is less than the DS0s HWM, then the HWM remains untouched. If new
                                    calls come in and the active DS0s are more than the HWM, then the HWM is incremented to reflect the new peak number of calls
                                    on that controller.

This value is reset to the current and active DS0s when call counters are cleared. For example, initially the HWM is 0. When
                              a new call comes in, the HWM is 1. When the next call comes in, the HWM is 2.

If 20 calls come in, the HWM is 20 and the active DS0s are 20. If 5 calls get disconnected, the DS0 active is 15, but the
                              HWM is 20. When a clear controller command is input for the specified controller, the HWM is reset to 15, which is the current and active DS0s also. If 10 calls
                              get disconnected, the Active DS0s is set to 5 and the HWM remains at 15 until another clear controller command is input. If Active DS0s exceed 15, then the HWM is updated.

The System DS0s High Water Mark field reflects the HWM at a system level including all DS0s controllers.

## Examples

The following sample output shows what happens after the HWMs are cleared:

```
Router# clear controller call-counters system-hwm !
Router# show controllers t1 call-counters T1 1/3/0:3:
  DS0's Active: 2
  DS0's Active High Water Mark: 2
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           1       00:08:51
     23       pri           1       00:09:21
T1 1/3/0:8:
  DS0's Active: 1
  DS0's Active High Water Mark: 1
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           0       00:01:39
     23       pri           0       00:00:00
System's DS0's Active High Water Mark: 3
```

In the example above, the system HWM is reset to the total number of active calls in the system, which is 3. The number was
                              4. When a call goes down, HWM values are untouched. Only the DS0 Active value changes. Above, there is only one call on 1/3/0:3.
                              Observe the HWM for individual controllers. Total number of active calls is 1.

The following is sample output when the clear controller call-counters system-hwm command is used:

```
Router# clear controller call-counters system-hwm !
Router# show controllers t1 call-counters T1 1/3/0:3:
  DS0's Active: 1
  DS0's Active High Water Mark: 2
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           1       00:12:16
     23       pri           1       00:10:20
T1 1/3/0:8:
  DS0's Active: 0
  DS0's Active High Water Mark: 1
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           0       00:02:50
     23       pri           0       00:00:00
System's DS0's Active High Water Mark: 1
```

In the preceding example, only the system HWM is reset to active. For controllers 1/3/0:3 and 1/3/0:8, the HWMs are untouched.

The following is sample output when the all keyword is used, clearing at the system level:

```
Router# clear controller call-counters all !
Router# show controllers t1 call-counters T1 1/3/0:3:
  DS0's Active: 0
  DS0's Active High Water Mark: 0 
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           0       00:00:00
     23       pri           0       00:00:00
T1 1/3/0:8:
  DS0's Active: 0
  DS0's Active High Water Mark: 0
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           0       00:00:00
     23       pri           0       00:00:00
System's DS0's Active High Water Mark: 0
```

In the preceding example, clearing at the system level using the clear controller call-counters command clears all DS0 controllers in the system and also clears the system HWMs.

### Related Commands

Command

Description

clear controller t1 call-counters

Clears call statistics on a specific T1 controller.

controller

Enters controller configuration mode.

show controllers t1 call-counters

Displays the total number of calls and call durations on a T1 controller.

## clear controller t1

To clear the system DS0 high water marks (HWM) and all individual controller statistics, use the clear controller t1 command in privileged EXEC mode.

clear controller t1 [slot] call-counters timeslots firmware-status

### Syntax Description

slot

(Optional) Clears an individual T1 controller.

call - counters timeslots

Clears the call counters in the specified T1 time slots.

firmware - status

Clears the Neat crash history.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(1)T

This command was introduced.

12.1(1)T

This command was implemented on the voice and WAN interface cards (VWICs) for the Cisco 2600 series and Cisco 3600 series.

12.1(2)T

This command was implemented on the Cisco AS5300, Cisco AS5400, and Cisco AS5800.

### Usage Guidelines

Refer to the following comments for the meaning of call counters displayed before and after executing clear controller t1 related commands:

The numbers displayed under TotalCalls for each time slot represent total calls that were connected successfully. If a call
                                    comes into time slot 10, then the show controllers t1 call-counters command displays 1 under the TotalCalls column for time slot 10. A value of 20 displayed under TotalCalls for time slot 10
                                    indicates a total of 20 calls connected on time slot 10 since the last time call counters were cleared.

If a time slot or time slot range is specified, only the counters for those channels are cleared. The TotalCalls field shows
                              the time slots that have calls connected since the last clear was done and does not show the number of active calls in the
                              controller. The TotalDuration field shows the same information as the TotalCalls field.

The DS0’s Active field indicates the number of active calls on the specified controller. This number indicates the current
                                    number of calls on the controller at any given time.

The DS0’s Active High Water Mark field indicates the peak number of calls on the controller since the last clear controller t1 1/0/0 call-counters command was entered. If the number of active calls "DS0’s Active" is less than DS0s HWM, then HWM remains untouched. If new
                                    calls come in and the active DS0s are more than the HWM, then the HWM is incremented to reflect the new peak number of calls
                                    on that controller.

This value is reset to the current and active DS0s when the clear controller t1 1/3/0 call-counters command is entered. For example, initially the HWM is 0. When a new call comes in, the HWM is 1. When the next call comes
                              in, the HWM is 2.

If 20 calls come in, the HWM is 20 and the active DS0s are 20. If 5 calls get disconnected, the DS0 active is 15, but the
                              HWM is 20. When a clear controller command is input for the specified controller, the HWM is reset to 15, which is the current and active DS0s also. If 10 calls
                              get disconnected, the Active DS0s value is set to 5 and the HWM remains at 15 until another clear controller command is input. If Active DS0s exceed 15, then the HWM is updated.

The System DS0s High Water Mark field reflects the HWM at a system level including all DS0s controllers.

## Examples

The following is sample output that shows two controllers numbered 1/3/0:3 and 1/3/0:8. Note the differences in the output
                              shown by the show controllers t1 call-counters command and how the clear controller t1 call-counters command affects the output:

```
Router# show controllers t1 call-counters T1 1/3/0:3:
  DS0's Active: 0
  DS0's Active High Water Mark: 0
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           0       00:00:00
     23       pri           0       00:00:00
T1 1/3/0:8:
  DS0's Active: 0
  DS0's Active High Water Mark: 0
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           0       00:00:00
     23       pri           0       00:00:00
System's DS0's Active High Water Mark: 0
```

In the preceding example, all the fields are zero, indicating that no calls have come in since system startup or since the
                                          last clear was made by the clear controller command.

The following is sample output that shows that four calls have been initiated on the 1/5/12, 1/5/13, 1/5/14, and 1/5/15 controllers:

```
Router# show users Line       User       Host(s)              Idle       Location
*  0 con 0                idle                 00:00:00   
  tty 1/5/12   Router Async interface      00:01:05   PPP: 55.61.1.1
  tty 1/5/13   Router Async interface      00:00:48   PPP: 55.62.1.1
  tty 1/5/14   Router Async interface      00:00:33   PPP: 55.54.1.1
  tty 1/5/15   Router Async interface      00:00:19   PPP: 55.52.1.1
  Interface  User      Mode                     Idle Peer Address
Router# show controllers t1 call-counters T1 1/3/0:3:
  DS0's Active: 2
  DS0's Active High Water Mark: 2
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           1       00:01:58
     23       pri           1       00:02:27
T1 1/3/0:8:
  DS0's Active: 2
  DS0's Active High Water Mark: 2
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           1       00:02:14
     23       pri           1       00:02:46
System's DS0's Active High Water Mark: 4
```

In the preceding example , if a clear controller command is entered for a controller that has active calls, which have been connected during the last 30 minutes, the TotalCalls
                              and TotalDuration fields are reset to zero.

The following is sample output that shows controller 1/3/0:3, with time slots 22 and 23 connected and active. When the clear controller t1 1/3/0:3 call-counters command is entered, the corresponding fields are set to zero.

```
Router# clear controller t1 1/3/0:3 call-counters !
Router# show controllers t1 call-counters T1 1/3/0:3:
  DS0's Active: 2
  DS0's Active High Water Mark: 2
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           1       00:29:14
     23       pri           1       00:29:47
Router# clear controller t1 1/3/0:3 call-counters Router# show controllers t1 call-counters T1 1/3/0:3:
  DS0's Active: 2
  DS0's Active High Water Mark: 2
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           0       00:00:10   <<<<<<
     23       pri           0       00:00:10   <<<<<<
```

The following is sample output when a call is cleared on 1/5/12:

```
Router# clear line 1/5/12 [confirm]
 [OK]
!
Router# show users Line       User       Host(s)              Idle       Location
*  0 con 0                idle                 00:00:00   
  tty 1/5/13   Router Async interface      00:03:04   PPP: 55.62.1.1
  tty 1/5/14   Router Async interface      00:02:49   PPP: 55.54.1.1
  tty 1/5/15   Router Async interface      00:02:35   PPP: 55.52.1.1
  Interface  User      Mode                     Idle Peer Address
Router# show controllers t1 call-counters T1 1/3/0:3:
  DS0's Active: 2
  DS0's Active High Water Mark: 2
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           1       00:03:44
     23       pri           1       00:04:14
T1 1/3/0:8:
  DS0's Active: 1
  DS0's Active High Water Mark: 2
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           1       00:04:00
     23       pri           1       00:03:34
System's DS0's Active High Water Mark: 4
```

After a call gets disconnected, only the DS0 Active field changes to reflect the current active call on the controller. In
                              the above example, 1/3/0:8 DS0 Active is changed to 1.

The following is sample output that shows call counters are cleared for an individual controller on 1/3/0:8:

```
Router# clear controller t1 1/3/0:8 call-counters !
Router# show controllers t1 call-counters T1 1/3/0:3:
  DS0's Active: 2
  DS0's Active High Water Mark: 2
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           1       00:07:46
     23       pri           1       00:08:15
T1 1/3/0:8:
  DS0's Active: 1
  DS0's Active High Water Mark: 1
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           0       00:00:35
     23       pri           0       00:00:00
System's DS0's Active High Water Mark: 4
```

In the previous example, after clearing call counters for controller 1/3/0:8, TotalCalls and TotalDuration reset. In addition
                              the DS0 HWM is also cleared to the number of active DS0s. Whenever the DS0 HWM is cleared, it does not reset to zero, but
                              rather it is set to Active DS0s. For 1/3/0:8, the HWM is 1 after clearing because DS0 Active is 1 (1 active call). TotalDuration
                              is 35 seconds for time slot 22, and TotalCall is 0 because they got reset when the clear controller call-counters command was entered. Total calls on this time slot is incremented when a new call comes in on this time slot.

The following is sample output when controller 1/5/15 is cleared:

```
Router# clear line 1/5/15 [confirm]
 [OK]
Router# show controllers t1 call-counters T1 1/3/0:3:
  DS0's Active: 0
  DS0's Active High Water Mark: 2
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           1       00:12:40
     23       pri           1       00:10:20
T1 1/3/0:8:
  DS0's Active: 0
  DS0's Active High Water Mark: 1
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           0       00:02:50
     23       pri           0       00:00:00
System's DS0's Active High Water Mark: 1
```

The following is sample output showing four active calls:

```
Router# show users Line       User       Host(s)              Idle       Location
*  0 con 0                idle                 00:00:00   
  tty 1/5/16   Router Async interface      00:01:01   PPP: 55.1.1.1
  tty 1/5/17   Router Async interface      00:00:47   PPP: 55.2.1.1
  tty 1/5/18   Router Async interface      00:00:28   PPP: 55.3.1.1
  tty 1/5/19   Router Async interface      00:00:14   PPP: 55.4.1.1
  Interface  User      Mode                     Idle Peer Address
Router# show controllers t1 call-counters T1 1/3/0:3:
  DS0's Active: 2
  DS0's Active High Water Mark: 2
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           1       00:00:57
     23       pri           1       00:01:30
T1 1/3/0:8:
  DS0's Active: 2
  DS0's Active High Water Mark: 2
  TimeSlot   Type   TotalCalls   TotalDuration
      1       pri           0       00:00:00
      2       pri           0       00:00:00
      3       pri           0       00:00:00
      4       pri           0       00:00:00
      5       pri           0       00:00:00
      6       pri           0       00:00:00
      7       pri           0       00:00:00
      8       pri           0       00:00:00
      9       pri           0       00:00:00
     10       pri           0       00:00:00
     11       pri           0       00:00:00
     12       pri           0       00:00:00
     13       pri           0       00:00:00
     14       pri           0       00:00:00
     15       pri           0       00:00:00
     16       pri           0       00:00:00
     17       pri           0       00:00:00
     18       pri           0       00:00:00
     19       pri           0       00:00:00
     20       pri           0       00:00:00
     21       pri           0       00:00:00
     22       pri           1       00:01:12
     23       pri           1       00:01:45
System's DS0's Active High Water Mark: 4
```

### Related Commands

Command

Description

clear controller call-counters

Clears all call statistics or system HWMs on a router.

controller

Enters controller configuration mode.

show controllers t1 call-counters

Displays the total number of calls and call durations on a T1 controller.

## clear csm-statistics modem

To clear the call switching module (CSM) statistics for a modem or
                              		  group of modems, use the clear csm - statistics modem command in privileged EXEC mode.

clear csm-statistics modem [ slot/port | modem-group-number ]

### Syntax Description

slot / port

(Optional) Identifies the location (and thereby the
                                          						identity) of a specific modem.

modem - group - number

(Optional) Designates a defined modem group.

### Command Default

No default behaviors or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

11.3NA

This command was introduced.

### Usage Guidelines

Use the clear csm - statistics modem command to clear CSM statistics for a particular modem or group
                              		  of modems. If the slot / port argument
                              		  is specified, the CSM call statistics for calls using the identified modem is
                              		  cleared. If a modem group number is specified, then the CSM call statistics for
                              		  calls using the modems associated with that group are cleared. If no argument
                              		  is specified, all CSM call statistics for all modems are cleared.

## Examples

The following example clears CSM call statistics for calls coming in
                              		  on modems associated with modem group 2:

```
Router# clear csm-statistics modem 2
```

### Related Commands

Command

Description

clear csm-statistics voice

Clears the CSM statistics for a particular or for all DSP
                                          						channels.

## clear csm-statistics voice

To clear the call switching module (CSM) statistics for a particular channel or for all digital signal processor (DSP) channels,
                              use the clear csm - statistics voice command in privileged EXEC mode.

clear csm-statistics voice [ slot/dspm/dsp/dsp-channel ]

### Syntax Description

slot / dspm / dsp / dsp - channel

(Optional) Identifies the location of a particular DSP channel.

### Command Default

No default behaviors or values

### Command Modes

Privileged EXEC

## Command History

Release

Modification

11.3NA

This command was introduced.

### Usage Guidelines

Use the clear csm - statistics voice command to clear CSM statistics for a particular DSP channel. If the slot / dspm / dsp / dsp - channel argument is specified, the CSM call statistics for calls using the identified DSP channel are cleared. If no argument is
                              specified, all CSM call statistics for all DSP channels are cleared.

## Examples

The following example clears CSM call statistics for calls coming in on all DSP channels:

```
Router# clear csm-statistics voice
```

### Related Commands

Command

Description

clear csm - statistics modem

Clears the CSM statistics for a modem or group of modems.

## clear h323 gatekeeper call

To force the disconnection of a specific call or of all calls active on a particular gatekeeper, use the clear h323 gatekeeper call command in privileged EXEC mode.

clear h323 gatekeeper call { all | local-callID local-callID }

### Syntax Description

all

Forces all active calls currently associated with this gatekeeper to be disconnected.

local - callID

Forces a single active call associated with this gatekeeper to be disconnected.

local-callID

Specifies the local call identification number (CallID) that identifies the call to be disconnected.

### Command Default

No default behaviors or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(5)T

This command was introduced on the Cisco 2600 series, the Cisco 3600 series, and on the Cisco MC3810.

12.1(5)XM2

The command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco AS5300. Support for the Cisco AS5350
                                          and Cisco AS5400 is not included in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

### Usage Guidelines

If you want to force a particular call to be disconnected (as opposed to all active calls on the gatekeeper), use the CallID
                              number to identify that specific call. You can find the local CallID number for a specific call by using the show gatekeeper calls command; the ID number is displayed in the LocalCallID column.

## Examples

The following example shows that an active call on the gatekeeper is being forced to disconnect. The local ID number of the
                              active call is 12-3339.

```
Router# clear h323 gatekeeper call local-callID 12-3339
```

The following example shows that all active calls on the gatekeeper are being forced to disconnect:

```
Router# clear h323 gatekeeper call all
```

The following sample output from the show gatekeeper calls command displays information about a specific active call having a call ID of 12-3339:

```
Router# show gatekeeper calls Total number of active calls =1
                    Gatekeeper Call Info
                    ====================
LocalCallID                    Age (secs)      BW
12-3339                        94              768 (Kbps)
 Endpt(s): Alias    E.164Addr     CallSignalAddr   Port   RASSignalAddr    Port
   src EP: epA                    10.0.0.11        1720   10.0.0.11        1700
   dst EP: epB2zoneB.com
   src PX: pxA                    10.0.0.1         1720   10.0.0.11        24999
   dst PX: pxB                    172.21.139.90    1720   172.21.139.90    24999
```

### Related Commands

Command

Description

show gatekeeper calls

Displays the status of each ongoing call of which a gatekeeper is aware.

## clear h323 gatekeeper endpoint

To unregister endpoints, use the clear h323 gatekeeper endpoint command in privileged EXEC mode.

clear h323 gatekeeper endpoint { alias e164 digits | alias h323id name | all | id number | ipaddr address [port] }

### Syntax Description

alias e164 digits

E.164 alphanumeric address that is specified in the local alias table.

alias h323id name

H.323 ID name that is specified in the local alias table and is an alternate way to reach an endpoint.

all

All endpoints.

id number

ID of the endpoint.

ipaddr address [ port ]

Call signaling address and port (optional) of the endpoint. If a value for the port argument is not specified, the default is 1720.

### Command Default

No default behavior or values.

### Command Modes

Privileged EXEC

## Command History

Release

Modification

12.2(11)T

This command was introduced 12.2(11)T on the Cisco 3660 and Cisco MC3810.

### Usage Guidelines

Using this command forces the gatekeeper to send an unregistration request (URQ) message to the specified endpoint or all
                              endpoints and removes the endpoint from the gatekeeper registration database.

For gatekeeper cluster configurations, this command must be entered on the gatekeeper where the endpoint is registered. Use
                              the show gatekeeper endpoints command to locate the endpoint in a gatekeeper cluster.

The endpoint that was unregistered using this command can come back if it sends the registration request (RRQ) back to the
                                          gatekeeper after the unregistration.

## Examples

The following example shows how to unregister all endpoints:

```
Router# clear h323 gatekeeper endpoint all Router# show gatekeeper endpoints GATEKEEPER ENDPOINT REGISTRATION
                    ================================
CallSignalAddr  Port  RASSignalAddr   Port  Zone Name         Type    Flags
--------------- ----- --------------- ----- ---------         ----    -----
Total number of active registrations = 0
```

### Related Commands

Command

Description

show gatekeeper endpoints

Locates the endpoint in a gatekeeper cluster.

## clear h323 gatekeeper stats

To clear statistics about gatekeeper performance, use the clear h323 gatekeeper stats command in privileged EXEC mode.

clear h323 gatekeeper stats

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(5)XM

This command was introduced.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

### Usage Guidelines

The clear h323 gatekeeper stats command resets the gatekeeper performance counters to zero and records the time at which the last clear was performed.

## Examples

The following is sample output from the show gatekeeper performance stats command that shows the counters have been reset to zero after entering the clear h323 gatekeeper stats command.

```
clear h323 gatekeeper stats
show gatekeeper performance stats
RAS inbound message counters:
Originating ARQ: 0 Terminating ARQ: 0 LRQ: 0
RAS outbound message counters:
ACF: 2  ARJ: 0 LCF: 2  LRJ: 0
ARJ due to overload: 0
LRJ due to overload: 0
Load balancing events: 0
Real endpoints: 2
```

### Related Commands

Command

Description

show gatekeeper performance statistics

Displays information about the number of calls accepted and rejected by the gatekeeper.

## clear h323 gateway

To clear the H.323 gateway counters, use the clear h323 gateway command in privileged EXEC mode.

clear h323 gateway [ cause-codes | h225 | ras ]

### Syntax Description

cause - codes

(Optional) Clears only the disconnected cause code counters.

h225

(Optional) Clears only the H.225 counters.

ras

(Optional) Clears only the Registration, Admission, and Status (RAS) counters.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(4)T

This command was introduced on all Cisco H.323 platforms except for the Cisco AS5300, Cisco AS5350, and Cisco AS5400.

### Usage Guidelines

To clear all H.323 counters, use the clear h323 gateway command without any optional keywords. After you have used the clear h323 gateway command, the respective counters are set to zero.

## Examples

In the following example from a Cisco 3640 router, the clear h323 gateway command is used without keywords to clear all H.323 counters:

```
Router# clear h323 gateway All H.323 stats cleared at 01:54:38
```

In the following example from a Cisco 3640 router, the clear h323 gateway command is used with the cause-codes keyword to clear the disconnect cause code counters:

```
Router# clear h323 gateway cause-codes Cause code stats cleared at 01:54:08
```

In the following example from a Cisco 3640 router, the clear h323 gateway command is used with the h225 keyword to clear the H.225 counters:

```
Router# clear h323 gateway h225 H.225 stats cleared at 01:53:18
```

In the following example from a Cisco 3640 router, the clear h323 gateway command is used with the ras keyword to clear the RAS counters:

```
Router# clear h323 gateway ras RAS stats cleared at 01:53:25
```

### Related Commands

Command

Description

debug cch323

Provides debug output for various components within the H.323 subsystem.

show h323 gateway

Displays the statistics for H.323 gateway messages that have been sent and received and displays the reasons for which H.323
                                          calls have been disconnected.

## clear http client statistics

To reset to zero all the counters that collect the information about the communication between the HTTP server and the client
                              displayed in the output from the show http client statistics command, use the clear http client statistics command in user EXEC or privileged EXEC mode.

clear http client statistics

### Syntax Description

This command has no arguments or keywords.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

12.4(15)T

This command was introduced.

### Usage Guidelines

Use the show http client statistics command to display the data collected by the counters the clear http client statistics command resets to zero.

## Examples

The following example resets the counters to zero:

```
Router# clear http client statistics
```

### Related Commands

Command

Description

show http client statistics

Displays information about the communication between the HTTP server and the client.

## clear interface cable-modem

To reset the controller for a specified cable modem daughter card, use the clear interface cable-modem command in privileged EXEC mode. This command does not have a no version.

clear interface cable-modem

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.4(11)T

This command was introduced.

## Examples

The following example shows how the clear interface cable-modem command clears the interface on the selected slot and port:

```
Router# clear interface cable-modem *May 17 16:36:57.344: %CABLE_MODEM_HWIC-6-RESET: Interface Cable-Modem0/2/0 has been reset: clear command
*May 17 16:37:05.348: %LINK-3-UPDOWN: Interface Cable-Modem0/2/0, changed state to down
*May 17 16:37:06.348: %LINEPROTO-5-UPDOWN: Line protocol on Interface Cable-Modem0/2/0, changed state to down
*May 17 16:37:19.740: %LINK-3-UPDOWN: Interface Cable-Modem0/2/0, changed state to up
*May 17 16:37:27.996: %LINEPROTO-5-UPDOWN: Line protocol on Interface Cable-Modem0/2/0, changed state to up
```

### Related Commands

Command

Description

show interfaces

Displays statistics for all interfaces configured.

show interfaces cable-modem

Displays statistics for all interfaces configured on the port.

## clear media-proxy sessions summary history

To clear the history data for CUBE Media Proxy recording sessions, use the clear media-proxy sessions summary history command in privileged EXEC mode.

clear media-proxy sessions summary history

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

IOS XE 16.10.1

This command was introduced.

### Usage Guidelines

Use the command clear media-proxy sessions summary history to clear the history data for CUBE Media Proxy recording sessions, that are displayed by the command show media-proxy sessions summary history .

## Examples

```
Device# clear media-proxy sessions summary history
```

### Related Commands

Command

Description

show media-proxy sessions summary history

Displays the summary of the completed CUBE MediaProxy SIP recording sessions.

## clear mgcp src-stats

To clear the statistics gathered for Media Gateway Control Protocol (MGCP) System Resource Check (SRC) Call Admission Control
                              (CAC) on an MGCP gateway, use the clear mgcp src - stats command in privileged EXEC mode.

clear mgcp src-stats

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(2)XB

This command was introduced.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T.

12.2(11)T

This command was implemented on the Cisco AS5350, Cisco AS5400, and Cisco AS5850.

### Usage Guidelines

Use the clear mgcp src - stats command to clear the MGCP gateway buffer that holds SRC CAC statistics gathered during the most recent inspection interval.

## Examples

The following example clears MGCP VoIP SRC CAC statistics:

```
Router# clear mgcp src-stats
```

### Related Commands

Command

Description

show mgcp statistics

Displays MGCP statistics regarding received and transmitted network messages.

## clear mgcp statistics

To reset the Media Gateway Control Protocol (MGCP) statistical counters, use the clear mgcp statistics command in privileged EXEC mode.

clear mgcp statistics

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(1)T

This command was introduced on the Cisco AS5300.

12.1(3)T

This command was implemented on the Cisco 3660, Cisco UBR924, and Cisco 2600 series.

12.2(11)T

This command was implemented on the Cisco AS5850.

## Examples

The following is an example shows the MGCP statistical counters being reset:

```
Router# clear mgcp statistics
```

### Related Commands

Command

Description

mgcp

Starts the MGCP daemon.

show mgcp statistics

Displays statistics for received and transmitted packets.

## clear mrcp client statistics

To clear all Media Resource Control Protocol (MRCP) statistics, use the clear mrcp client statistics command in privileged EXEC mode.

clear mrcp client statistics { all | hostname { hostname | ip-address }}

### Syntax Description

all

Clears the accumulated MRCP session statistics for all hosts.

hostname

Clears the accumulated MRCP session statistics for the specified host.

hostname

Host name of the MRCP server. Format uses host name only or hostname : port .

ip - address

IP address of the MRCP server.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(11)T

This command was introduced on the Cisco 3640, Cisco 3660, Cisco AS5300, Cisco AS5350, and Cisco AS5400.

### Usage Guidelines

This command resets all MRCP session statistics to 0. Use the show mrcp client statistics hostname command to display the current statistics.

## Examples

The following example resets the statistics for the host called "asr_server":

```
Router# clear mrcp client statistics hostname asr_server
```

### Related Commands

Command

Description

show mrcp client statistics hostname

Displays cumulative information about MRCP sessions.

## clear rlm group

To reset all Redundant Link Manager (RLM) time stamps to zero, use the clear rlm group command in privileged EXEC mode.

clear rlm group [group-number] [ link | statistics ]

### Syntax Description

group-number

(Optional) RLM group number. Range is from 0 to 255. There is no default value.

link

(Optional) Specifies the RLM group link.

statistics

(Optional) Specifies the RLM group statistics.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

11.3(7)

This command was introduced.

15.0(1)M

This command was modified in a release earlier than Cisco IOS Release 15.0(1)M. The statistics keyword was added.

## Examples

The following example resets the time stamps on RLM group 1:

```
Router# clear rlm group 1 link !
02:48:17: rlm 1: [State_Up, rx ACTIVE_LINK_BROKEN] over link [10.1.1.1(Loopback1), 10.1.4.1]
02:48:17: rlm 1: link [10.1.1.2(Loopback2), 10.1.4.2] requests activation
02:48:17: rlm 1: link [10.1.1.1(Loopback1), 10.1.4.1] is deactivated
02:48:17: rlm 1: [State_Recover, rx LINK_BROKEN] over link [10.1.1.2(Loopback2), 10.1.4.2]
02:48:17: rlm 1: link [10.1.1.1(Loopback1), 10.1.4.1] = socket[10.1.1.1, 10.1.4.1]
02:48:17: rlm 1: [State_Recover, rx USER_SOCKET_OPENED] over link [10.1.1.1(Loopback1), 10.1.4.1] for user RLM_MGR
02:48:17: rlm 1: link [10.1.1.1(Loopback1), 10.1.4.1] is opened
02:48:17: rlm 1: link [10.1.1.2(Loopback2), 10.1.4.2] = socket[10.1.1.2, 10.1.4.2]
02:48:17: rlm 1: [State_Recover, rx USER_SOCKET_OPENED] over link [10.1.1.2(Loopback2), 10.1.4.2] for user RLM_MGR
02:48:17: rlm 1: link [10.1.1.2(Loopback2), 10.1.4.2] is opened
02:48:17: rlm 1: link [10.1.1.1(Loopback1), 10.1.5.1] = socket[10.1.1.1, 10.1.5.1]
02:48:17: rlm 1: [State_Recover, rx USER_SOCKET_OPENED] over link [10.1.1.1(Loopback1), 10.1.5.1] for user RLM_MGR
02:48:17: rlm 1: link [10.1.1.1(Loopback1), 10.1.5.1] is opened
02:48:17: rlm 1: link [10.1.1.2(Loopback2), 10.1.5.2] = socket[10.1.1.2, 10.1.5.2]
02:48:17: rlm 1: [State_Recover, rx USER_SOCKET_OPENED] over link [10.1.1.2(Loopback2), 10.1.5.2] for user RLM_MGR
02:48:17: rlm 1: link [10.1.1.2(Loopback2), 10.1.5.2] is opened
02:48:17: rlm 1: [State_Recover, rx LINK_OPENED] over link [10.1.1.1(Loopback1), 10.1.4.1]
02:48:17: rlm 1: link [10.1.1.1(Loopback1), 10.1.4.1] requests activation
02:48:17: rlm 1: [State_Recover, rx LINK_OPENED] over link [10.1.1.2(Loopback2), 10.1.4.2]
02:48:17: rlm 1: [State_Recover, rx START_ACK] over link [10.1.1.1(Loopback1), 10.1.4.1]
02:48:17: rlm 1: link [10.1.1.1(Loopback1), 10.1.4.1] is activated
```

### Related Commands

Command

Description

clear interface

Resets the hardware logic on an interface.

interface

Defines the IP addresses of the server, configures an interface type, and enters interface configuration mode.

link (RLM)

Specifies the link preference.

protocol rlm port

Reconfigures the port number for the basic RLM connection for the whole RLM group.

retry keepalive

Allows consecutive keepalive failures a certain amount of time before the link is declared down.

server (RLM)

Defines the IP addresses of the server.

show rlm group statistics

Displays the network latency of the RLM group.

show rlm group status

Displays the status of the RLM group.

show rlm group timer

Displays the current RLM group timer values.

timer

Overwrites the default setting of timeout values.

## clear rpms-proc counters

To clear Resource Policy Management System (RPMS) statistics counters for the number of leg 3 authentication, authorization,
                              and accounting (AAA) preauthentication requests, successes, and rejects, use the clear rpms - proc counters command in privileged EXEC mode.

clear rpms-proc counters

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

## Examples

The following example clears statistics counters for leg 3 AAA preauthentication requests, successes, and rejects:

```
Router# clear rpms-proc counters
```

### Related Commands

Command

Description

show rpms-proc counters

Displays statistics for the number of leg 3 AAA preauthentication requests, successes, and rejects.

## clear rudpv0 statistics

To clear the counters that track Reliable User Datagram Protocol (RUDP) statistics, enter the clear rudpv0 statistics command in privileged EXEC mode.

clear rudpv0 statistics

### Syntax Description

This command has no arguments or keywords.

### Command Default

The statistical information accumulates.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(7)XR

This command was introduced.

12.1(1)T

This command was integrated into Cisco IOS Release 12.1(1)T.

## Examples

The following example shows how to clear RUDP statistics on a Cisco 2611:

```
Router(config)# clear rudpv0 statistics
```

### Related Commands

Command

Description

show rudpv0 failures

Displays RUDP information about failed connections and the reasons for them.

show rudpv0 statistics

Displays RUDP information about number of packets sent, received, and so forth.

## clear rudpv1 statistics

To clear the counters that track Reliable User Datagram Protocol (RUDP) statistics, use the clear rudpv1 statistics command in privileged EXEC mode.

clear rudpv1 statistics

### Syntax Description

This command has no arguments or keywords.

### Command Default

The statistical information accumulates.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(1)T

This command was introduced.

12.2(2)T

This command was implemented on Cisco 7200.

12.2(4)T

This command was implemented on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco IAD2420 series.

12.2(11)T

This command was implemented on the Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 in this release.

## Examples

The following example clears all RUDP statistics for all available session groups:

```
Router# clear rudpv1 statistics
```

### Related Commands

Command

Description

debug rudpv1

Displays debugging information for RUDP.

show rudpv1

Displays RUDP information.

## clear sccp server statistics

To clear the counts displayed under the show sccp server statistics command, use the clear sccp server statistics command in privileged EXEC mode.

clear sccp server statistics

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.4(15)XY

This command was introduced.

15.0(1)M

This command was integrated into a release earlier than Cisco IOS Release 15.0(1)M.

## Examples

The following example shows the Skinny Client Control Protocol (SCCP) server statistics counts being cleared, followed by
                              verification that the counters are reset to zero with the show sccp server statistics command. The field descriptions are self-explanatory.

```
Router# show sccp server statistics Failure type              Error count
------------------------  -----------
Send queue enqueue        0
Socket send               0
Msg discarded upon error  0
```

### Related Commands

Command

Description

show sccp server statistics

Displays the number of SCCP messages sent and received by the SCCP server.

## clear sdspfarm counters

To reset the server counts of the digital signal processor farms that are registered to the Skinny Client Control Protocol
                              (sdspfarm) displayed under the server show sdspfarm message statistics command to zero, use the clear sdspfarm counters command in privileged EXEC mode.

clear sdspfarm counters

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.4(15)XY

This command was introduced.

## Examples

The following example shows the sdspfarm counters being cleared and verification that the counters are reset to zero with
                              the show sdspfarm sessions state command:

```
Router# clear sdspfarm counters Router# show sdspfarm sessions state Call state      Num of sessions
----------      ---------------
IDLE            1022
ALERTING        0  
SEIZE           0  
PROGRESS        0  
CONNECTED       0  
DIGITS          0  
BUSY            0  
RINGING         0  
ERROR           0  
HOLD            0  
END             0  
STOP            0  
START           2  
RESTART         0  
UNKNOWN         0  
DELAYED-SMT     0
```

Field descriptions should be self-explanatory.

### Related Commands

Command

Description

show sdspfarm message statistics

Displays the number of SCCP messages sent and received by the SCCP server.

show sdspfarm sessions state

Displays the number of sessions in each SCCP call state.

## clear sgcp statistics

To clear all Simple Gateway Control Protocol (SGCP) statistics, use the clear sgcp statistics command in privileged EXEC mode.

clear sgcp statistics

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(5)T

This command was introduced in a private release on the Cisco AS5300 only and was not generally available.

12.0(7)XK

This command was implemented on the Cisco MC3810 and the Cisco 3600 series (except for the Cisco 3620) in a private release
                                          that was not generally available.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

## Examples

The following example shows all SGCP statistics being cleared:

```
Router# clear sgcp statistics
```

### Related Commands

Command

Description

show sgcp statistics

Displays global statistics for SGCP packet counts.

## clear sip-ua registration

To clear the registration records of SIP user agents, use the clear sip-ua registration command in privileged EXEC mode.

clear sip-ua registration passthrough { all | call-id call-id | dial-peer dial-peer | dn dn }

### Syntax Description

passthrough

Clears SIP registration passthrough status

all

Clears SIP registration records of all user agents

call-id call-id

Clears SIP registration records of the user agent with the specified call ID

dial-peer dial-peer

Clears SIP registration records of user agents on the specified dial peer

dn dn

Clears SIP registration records of user agents on the specified directory number

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

IOS XE Fuji Release 16.8.1

This command was introduced.

### Usage Guidelines

This command clears registration records of SIP User Agents based on the call-id, dial-peer, and directory number. If you
                              use the keyword “all”, this command clears the registration records of all SIP user agents.

## Examples

The following example clears registration records of the SIP user agent with call-id 2147483647:

```
Router# clear sip-ua registration passthrough call-id 2147483647
```

### Related Commands

clear sip ua-statistics

Clears all SIP statistics counters.

show sip-ua registration passthrough status

Displays the SIP user agent pass-through status information .

## clear sip-ua statistics

To reset the Session Initiation Protocol (SIP) user-agent (UA) statistical counters, use the clear sip-ua statistics command in privileged EXEC mode.

clear sip-ua statistics { dial-peer } tag

### Syntax Description

Specifies the unique dial-peer identifier (tag) for the peer.

Value Range: 1-2147483647

Clears the unique dial-peer identifier statistics.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

Cisco IOS XE 17.18.2

This command is modified to clear SIP global error counters for dial-peer.

12.2(13)T

This command was introduced.

### Usage Guidelines

Use the clear sip-ua statistics command to clear all SIP statistics counters that are displayed by the show sip-ua statistics command.

## Examples

The following example shows all SIP-UA statistics being cleared:

```
Router# clear sip-ua statistics
```

## Examples

The following example shows SIP global error counters cleared for the dial-peer 100:

```
Router# clear sip-ua statistics dial-peer 100 Router#
```

### Related Commands

Command

Description

Displays response, traffic, and retry SIP statistics.

## clear sip-ua tcp connection

To clear a session initiation protocol (SIP) TCP connection, use the clear sip-ua tcp connection command in privileged EXEC mode.

clear sip-ua tcp
                                 				  connection { id connection-id [ target
                                 							 ipv4 :address:port |
                                 							 id connection-id ]} target
                                 				  ipv4 :address:port

### Syntax Description

id connection-id

Specifies the ID of the connection that needs to be closed
                                          						in the SIP TCP process. The connection-id argument represents the connection ID. The range is
                                          						from 1 to 2048.

target ipv4: address : port

Specifies the target address for the connection that needs
                                          						to be closed in the SIP transport layer.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.4(6)T

This command was replaced by the clear sip-ua command.

### Usage Guidelines

Inappropriate usage of the clear sip-ua tcp connection command can lead to erroneous call
                              		  behavior, inappropriate usage of connections, and failure of calls.

## Examples

To cear the connection entry only at the upper transport layer,
                              		  assign the target IP address and port:

```
Router# clear sip-ua tcp connection target ipv4:172.18.194.183:5060
```

To clear the connection entry only at the lower TCP or User Datagram
                              		  Protocol (UDP) layer, specify the connection:

```
Router# clear sip-ua tcp connection id 1
```

To completely clear a valid connection to target 172.18.194.183, port
                              		  5060, consider the following output example from the show sip-ua connections command:

```
Router# show sip-ua connections tcp detail Total active connections : 1 
No. of send failures : 0 
No. of remote closures : 0 
No. of conn. failures : 0 
No. of inactive conn. ageouts : 0 
Max. tcp send msg queue size of 1, recorded for 172.18.194.183:5060
---------Printing Detailed Connection Report--------- 
Note: 
** Tuples with no matching socket entry 
- Do 'clear sip <tcp/udp> conn t ipv4:<addr>:<port>' 
to overcome this error condition 
++ Tuples with mismatched address/port entry 
- Do 'clear sip <tcp/udp> conn t ipv4:<addr>:<port> id <connid>' 
to overcome this error condition
Remote-Agent:172.18.194.183, Connections-Count:1 
Remote-Port Conn-Id Conn-State WriteQ-Size 
=========== ======= =========== =========== 
5060 1 Established 0
```

Then execute the clear sip-ua tcp connection command:

```
Router# clear sip-ua tcp connection id 1 target ipv4:172.18.194.183:5060 Purging the entry from sip tcp process 
Purging the entry from reusable global connection table
```

The result is that all connections are cleared after inputting the clear sip-ua tcp connection command:

```
Router# show sip-ua connections tcp detail Total active connections : 0 
No. of send failures : 0 
No. of remote closures : 0 
No. of conn. failures : 0 
No. of inactive conn. ageouts : 0 
Max. tcp send msg queue size of 1, recorded for 172.18.194.183:5060
---------Printing Detailed Connection Report--------- 
Note: 
** Tuples with no matching socket entry 
- Do 'clear sip <tcp/udp> conn t ipv4:<addr>:<port>' 
to overcome this error condition 
++ Tuples with mismatched address/port entry 
- Do 'clear sip <tcp/udp> conn t ipv4:<addr>:<port> id <connid>' 
to overcome this error condition
Remote-Agent:172.18.194.183, Connections-Count:0
```

### Related Commands

Command

Description

clear sip-ua udp connection

Clears a SIP UDP connection.

show sip-ua connections

Displays SIP UA transport connection tabless.

timers connection aging

Sets the time before the SIP UA ages out a TCP and UDP
                                          						connection.

## clear sip-ua tcp tls connection

To clear a session initiation protocol (SIP) TCP connection, use the clear sip-ua tcp tls connection command in privileged EXEC mode.

clear sip-ua tcp tls
                                 				  connection { id connection-id [ target
                                 							 ipv4 :address:port |
                                 							 id connection-id ]} target
                                 				  ipv4 :address:port

### Syntax Description

id connection-id

Specifies the ID of the connection that needs to be closed
                                          						in the SIP TCP process. The connection-id argument represents the connection ID. The range is
                                          						from 1 to 2048.

target ipv4: address : port

Specifies the target address for the connection that needs
                                          						to be closed in the SIP transport layer.

### Command Modes

Privileged EXEC

## Command History

Release

Modification

12.4(6)T

This command was replaced by the clear sip-ua command.

### Usage Guidelines

Inappropriate usage of the clear sip-ua tcp tls connection command can lead to erroneous call
                              		  behavior, inappropriate usage of connections, and failure of calls.

## Examples

To cear the connection entry only at the upper transport layer,
                              		  assign the target IP address and port:

```
Router# clear sip-ua tcp tls connection target ipv4:172.18.194.183:5060
```

To clear the connection entry only at the lower TCP or User Datagram
                              		  Protocol (UDP) layer, specify the connection:

```
Router# clear sip-ua tcp tls connection id 1
```

To completely clear a valid connection to target 172.18.194.183, port
                              		  5060, consider the following output example from the show sip-ua connections command:

```
Router# show sip-ua connections tcp tls detail Total active connections : 1 
No. of send failures : 0 
No. of remote closures : 0 
No. of conn. failures : 0 
No. of inactive conn. ageouts : 0 
Max. tcp send msg queue size of 1, recorded for 172.18.194.183:5060
---------Printing Detailed Connection Report--------- 
Note: 
** Tuples with no matching socket entry 
- Do 'clear sip <tcp/udp> conn t ipv4:<addr>:<port>' 
to overcome this error condition 
++ Tuples with mismatched address/port entry 
- Do 'clear sip <tcp/udp> conn t ipv4:<addr>:<port> id <connid>' 
to overcome this error condition
Remote-Agent:172.18.194.183, Connections-Count:1 
Remote-Port Conn-Id Conn-State WriteQ-Size 
=========== ======= =========== =========== 
5060 1 Established 0
```

Then execute the clear sip-ua tcp connection command:

```
Router# clear sip-ua tcp tls connection id 1 target ipv4:172.18.194.183:5060 Purging the entry from sip tcp process 
Purging the entry from reusable global connection table
```

The result is that all connections are cleared after inputting the clear sip-ua tcp connection command:

```
Router# show sip-ua connections tcp tls detail Total active connections : 0 
No. of send failures : 0 
No. of remote closures : 0 
No. of conn. failures : 0 
No. of inactive conn. ageouts : 0 
Max. tcp send msg queue size of 1, recorded for 172.18.194.183:5060
---------Printing Detailed Connection Report--------- 
Note: 
** Tuples with no matching socket entry 
- Do 'clear sip <tcp/udp> conn t ipv4:<addr>:<port>' 
to overcome this error condition 
++ Tuples with mismatched address/port entry 
- Do 'clear sip <tcp/udp> conn t ipv4:<addr>:<port> id <connid>' 
to overcome this error condition
Remote-Agent:172.18.194.183, Connections-Count:0
```

### Related Commands

Command

Description

clear sip-ua udp connection

Clears a SIP UDP connection.

show sip-ua connections

Displays SIP UA transport connection tabless.

timers connection aging

Sets the time before the SIP UA ages out a TCP and UDP
                                          						connection.

## clear sip-ua udp connection

To clear a SIP UDP connection, use the clear sip-ua udp connection command in privileged EXEC mode.

clear sip-ua udp connection { id value [ target ip-address ] |  [ id value ] target ip-address }

### Syntax Description

id value

Specifies the ID of the connection that needs to be closed in the SIP UDP process. The value argument represents the value of the connection ID. The range is from 1 to 2048.

target ip - address

Specifies the target address for the connection that needs to be closed in the SIP transport layer. The ip-address argument is the target address in the form of ipv4: address : port .

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

12.4(6)T

This command was replaced by the clear sip-ua command.

### Usage Guidelines

Inappropriate usage of the clear sip-ua udp connection command without understanding the issue or the implications can lead to erroneous call behavior, inappropriate usage of connections,
                              and failure of calls.

## Examples

To purge the connection entry only at the upper transport layer, assign the target IP address and port.

```
Router# clear sip-ua udp connection target ipv4:172.18.194.183:5060
```

To purge the connection entry only at the lower TCP/UDP layer, assign the connection ID.

```
Router# clear sip-ua udp connection id 1
```

Inappropriate usage of the clear command without understanding the issue or the implications would lead to erroneous call behavior, inappropriate usage of
                                          connections, and failure of calls.

To completely purge a valid connection to target 172.18.194.183, port 5060, consider the following example.

Before executing the clear sip-ua udp connection command, running the show sip-ua connections command gave the following output.

```
Router# show sip-ua connections udp detail Total active connections : 1 
No. of send failures : 0 
No. of remote closures : 0 
No. of conn. failures : 0 
No. of inactive conn. ageouts : 0 
Max. udp send msg queue size of 1, recorded for 172.18.194.183:5060
---------Printing Detailed Connection Report--------- 
Note: 
** Tuples with no matching socket entry 
- Do 'clear sip <tcp/udp> conn t ipv4:<addr>:<port>' 
to overcome this error condition 
++ Tuples with mismatched address/port entry 
- Do 'clear sip <tcp/udp> conn t ipv4:<addr>:<port> id <connid>' 
to overcome this error condition
Remote-Agent:172.18.194.183, Connections-Count:1 
Remote-Port Conn-Id Conn-State WriteQ-Size 
=========== ======= =========== =========== 
5060 1 Established 0
```

Then execute the clear sip-ua udp connection command:

```
Router# clear sip-ua udp connection id 1 target ipv4:172.18.194.183:5060 Purging the entry from sip udp process 
Purging the entry from reusable global connection table
```

The final result is that all connections are cleared after executing the clear sip-ua udp connection command:

```
Router# show sip-ua connections udp detail Total active connections : 0 
No. of send failures : 0 
No. of remote closures : 0 
No. of conn. failures : 0 
No. of inactive conn. ageouts : 0 
Max. udp send msg queue size of 1, recorded for 172.18.194.183:5060
---------Printing Detailed Connection Report--------- 
Note: 
** Tuples with no matching socket entry 
- Do 'clear sip <tcp/udp> conn t ipv4:<addr>:<port>' 
to overcome this error condition 
++ Tuples with mismatched address/port entry 
- Do 'clear sip <tcp/udp> conn t ipv4:<addr>:<port> id <connid>' 
to overcome this error condition
Remote-Agent:172.18.194.183, Connections-Count:0
```

### Related Commands

Command

Description

clear sip-ua tcp connection

Clears a SIP TCP connection.

show sip-ua connections

Displays SIP UA transport connections.

timers connection aging

Sets the time before the SIP UA ages out a TCP and UDP connection.

## clear ss7 sm-stats

To clear the counters that track session manager statistics, use the clear ss7 sm-stats command in privileged EXEC mode.

clear ss7 sm-stats [ session-set number ]

### Syntax Description

session-set

(Optional) Specifies the session set.

number

(Optional) Specifies the session-set number. The range is from 0 to 3.

### Command Default

The statistical information accumulates.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(7)XR

This command was introduced.

12.1(1)T

This command was integrated into Cisco IOS Release 12.1(1)T.

15.0(1)M

This command was modified in a release earlier than Cisco IOS Release 15.0(1)M. The session-set keyword and number argument were added.

## Examples

The following example shows how to clear session manager statistics:

```
Router# clear ss7 sm-stats session-set 2
```

### Related Commands

Command

Description

show ss7 sm stats

Displays session manager information about number of packets queued, received, and so forth.

## clear statistics dial-peer voice

To reset voice call counters and recent call details stored in a dial
                              		  peer, use the clear statistics dial - peer voice command in privileged EXEC mode.

clear statistics dial-peer
                                 				  voice { tag | busy-trigger-counter }

### Syntax Description

tag

(Optional) Identification tag number of a specific dial
                                          						peer. A valid entry is any integer that identifies a specific dial peer. Range
                                          						is from 1 to 2147483647.

busy-trigger-counter

(Optional) Specifies to clear the dial peer busy trigger
                                          						call counter.

### Command Default

If the tag argument is not used, counters in all the
                              		  configured voice dial peers are cleared.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(8)T

This command was introduced on the Cisco AS5300.

15.0(1)M

This command was modified in a release earlier than Cisco
                                          						IOS Release 15.0(1)M. The busy-trigger-counter keyword was
                                          						added.

Cisco IOS XE Release 2.1

This command was integrated into Cisco IOS XE Release 2.1
                                          						and implemented on the Cisco ASR 1000 Series Aggregation Services Routers.

### Usage Guidelines

The clear statistics dial - peer voice command resets the following statistical
                              		  information about calls:

Time elapsed since last
                                    			 clearing of statistics

Connect time

Charged units

Accepted calls

Refused calls

Successful calls

Failed calls

Incomplete calls

Last disconnect cause

Last disconnect text

Last setup time

## Examples

The following example shows how to clear voice dial peer statistics
                              		  using tag 1234:

```
Router# clear statistics dial-peer voice 1234 Clear voice call statistics stored in this voice dial-peer [confirm]y
```

The following example shows how to clear statistics in all the
                              		  configured voice dial peers:

```
Router# clear statistics dial-peer voice Clear voice call statistics stored in all voice dial-peers [confirm]y
```

### Related Commands

Command

Description

dial-peer voice

Enters dial peer configuration mode and specifies the
                                          						method of voice encapsulation.

show call history voice record

Displays CDR events in the call history table.

show dial-peer voice

Displays configuration information for dial peers.

## clear stcapp statistics

To clear SCCP Telephony Control Application (STCAPP) statistics, use the clear stcapp statistics command in privileged EXEC mode.

clear stcapp statistics { all | port slot-number }

### Syntax Description

all

Clears all STCAPP statistics.

port

Clears port-level STCAPP statistics.

slot-number

Voice interface slot number. The range is from 0 to 2147483647.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

15.0(1)M

This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M.

## Examples

The following example show how to clear all STCAPP statistics:

```
Router# clear stcapp statistics all
```

### Related Commands

Command

Description

stcapp

Enables the STCAPP.

## clear subscription

To clear all active subscriptions or a specific subscription, use the clear subscription command in privileged EXEC mode.

clear subscription { all | session-id session-id | statistics }

### Syntax Description

all

All active subscriptions.

session-id session-id

Subscription session to be cleared.

statistics

Global subscription statistics and all subscription history records.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

To cancel a specific subscription, use the session-id argument. The session ID can be found in the display frm from the show subscriptions command. When this command is used, the applications associated with subscriptions receive the ev_subscribe_cleanup event.
                              On receiving this event, the script closes the subscription.

## Examples

The following example shows global statistics and history records being cleared:

```
Router# clear subscription statistics
```

### Related Commands

Command

Description

retry subscribe

Configures the number of retries for SUBSCRIBE messages.

show subscription sip

Displays active SIP subscriptions.

subscription maximum

Specifies the maximum number of outstanding subscriptions to be accepted or originated by the gateway.

## clear tgrep counters

To clear Telephony Gateway Registration Protocol (TGREP) counters, use the clear tgrep counters command in privileged EXEC mode.

clear tgrep counters { * | carrier string | csr | dial-peer tag | trunk-group label } [ csr ] [ ac ]

### Syntax Description

*

Clears all TGREP counters.

carrier

Clears available circuit counters.

string

Carrier ID.

dial-peer

Clears dial-peer.

tag

Dial peer tag. The range is from 1 to 2147483647.

trunk-group label

Clears the trunk-group counters.

csr

(Optional) Clears the call success rate counters.

ac

(Optional) Clears all the available circuit counters.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

15.0(1)M

This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M.

## Examples

The following example show how to clear all tgrep counter information:

```
Router# clear tgrep counters *
```

### Related Commands

Command

Description

clear tgrep neighbor

Clears all neighbor sessions.

## clear tgrep neighbor

To clear Telephony Gateway Registration Protocol (TGREP) neighbor sessions, use the clear tgrep neighbor command in privileged EXEC mode.

clear tgrep neighbor { * | ip-address }

### Syntax Description

*

Clears all neighbor sessions.

ip-address

IP addresses of neighbor sessions.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

15.0(1)M

This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M.

## Examples

The following example shows how to clear neighbor sessions:

```
Router# clear tgrep neighbor *
```

### Related Commands

Command

Description

clear tgrep counters

Clears TGREP counters.

## clear voice accounting method

To clear VoIP AAA accounting statistics for a specific accounting method on the gateway, use the clear voice accounting method command in privileged EXEC mode.

clear voice accounting method method-list-name

### Syntax Description

method-list-name

Name of the method list.

### Command Modes

Privileged EXEC

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example clears accounting statistics for method list "h323":

```
Router# clear voice accounting method h323
```

### Related Commands

Command

Description

voice statistics type csr

Configures the collection of signaling and VoIP AAA accounting statistics.

## clear voice dsp

To "cold-start" one or more digital signal processor (DSP) voice
                              		  channels, use the clear voice dsp command in privileged EXEC mode.

clear voice
                                 				  dsp { channels | error } [ [slot] ] [ /dsp ] { /channel }

channels

Clears DSP calls on a specific channel or a range of
                                       					 channels.

error

Clears DSP error statistics.

slot

(Optional) Specifies either a single slot or the first slot
                                       					 in a range. To specify a range of slots, you can enter a second slot in the syntax of this argument. The second slot specifies the end of the range. All slots in the range are affected
                                       					 by the command.

/ dsp

(Optional) Specifies either a single DSP on the slot or the
                                       					 first DSP in a range. To specify a range of DSPs, you can enter a second DSP in the syntax of this argument. The second DSP specifies the end of the range. All DSPs in the range are affected
                                       					 by the command.

/ channel

(Optional) Specifies either a single channel on the DSP or
                                       					 the first channel in a range. To specify a range of channels, you can enter a second channel in the syntax of this argument. The second channel specifies the end of the range. All channels in the range are
                                       					 affected by the command.

### Command Default

If this command is not used, active calls continue on the DSP voice
                              		  channels.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.4(4)XC

This command was introduced.

12.4(9)T

This command was integrated into Cisco IOS Release
                                          						12.4(9)T.

### Usage Guidelines

The clear voice dsp command allows you to cold-start DSPs.
                              		  Execution of this command causes the configured firmware to be downloaded to
                              		  the specified DSP or a range of DSPs. This command can be executed irrespective
                              		  of the state of the DSPs. All the active channels of the DSPs are prematurely
                              		  terminated.

## Examples

The following example clears all active calls on slot 2, DSP 1:

```
Router# clear voice dsp 2/1
```

The following example clears the active calls on slot 2, DSP 1,
                              		  channel 1:

```
Router# clear voice dsp 2/1/1
```

### Related Commands

Command

Description

show voice dsp

Displays the current status or selective statistics of DSP
                                          						voice channels

## clear voice phone-proxy all-sessions

To clear all phone-proxy sessions use the clear voice phone-proxy all-sessions command in privileged EXEC mode.

clear voice phone-proxy all-sessions

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

15.3(3)M

This command was introduced.

## Examples

The following example shows how to clear all phone-proxy sessions:

```
Device# clear voice phone-proxy all-sessions
```

## clear voice statistics

To clear voice-statistic collection settings on the gateway to reset the statistics collection, use the clear voice statistics command in privileged EXEC mode.

{ clear voice statistics [ csr [ accounting | signaling ]] |  [ iec ]}

### Syntax Description

csr

(Optional) All accounting and signaling statistics are cleared, but Cisco VoIP internal error codes (IECs) are not cleared.

accounting

(Optional) Only accounting statistics are cleared.

signaling

(Optional) Only signaling statistics are cleared.

iec

(Optional) Only Cisco VoIP IECs are cleared.

### Command Default

If no keywords are specified, all accounting and signaling statistics, and all IECs are cleared.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example clears all accounting and signaling statistics, and all Cisco VoIP IECs:

```
Router# clear voice statistics
```

The following example clears all accounting and signaling statistics:

```
Router# clear voice statistics csr
```

The following example clears only accounting statistics:

```
Router# clear voice statistics csr accounting
```

The following example clears only signaling statistics:

```
Router# clear voice statistics csr signaling
```

The following example clears only Cisco VoIP IECs:

```
Router# clear voice statistics iec
```

### Related Commands

Command

Description

voice statistics type csr

Configures the collection of signaling and VoIP AAA accounting statistics.

## clear voip fpi rtts

To clear the Voice over IP (VoIP) forwarding plane interface (FPI) round-trip time counter, use the clear voip fpi rtts command in privileged EXEC mode.

clear voip fpi rtts

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco IOS XE Release 3.9S

This command was introduced.

## Examples

The following example shows how to clear the VoIP FPI round-trip time counter.

```
Router# clear voip fpi rtts
```

## clear voip fpi stats

To clear the Voice over IP (VoIP) forwarding plane interface (FPI) statistics counter, use the clear voip fpi stats command in privileged EXEC mode.

clear voip fpi stat

### Syntax Description

This command has no arguments or keywords.

## Command History

Cisco IOS XE Release 3.9S

This command was introduced.

## Examples

The following example shows how to clear the VoIP FPI statistics counter.

```
Router# clear voip fpi stats
```

## clear voip rtp port

In some cases, Voice over IP (VoIP) Real Time Protocol (RTP) ports can remain assigned after a call ends. Use this command
                              to clear such hung ports.

clear voip rtp port table-id ports

### Syntax Description

Use the 'show voip rtp stats' command to establish the table identifier for the hung port that needs to be cleared.

List of up to 32 comma separated port numbers in the range 5500 to 65498.

### Command Modes

Privileged EXEC (#)

## Command History

This command is introduced.

## Examples

When you try to clear a hung port, the following confirmation message is displayed:

```
Router#clear voip rtp port 1 8002
Any port(s) associated with an active call will not be cleared.[confirm]
Cleared port 8002
```

If you try to clear a port associated with an active call, the following error is displayed:

```
Router#clear voip rtp port 2 9020,9022
Any port(s) associated with an active call will not be cleared.[confirm]
The following port(s) are associated with active calls and have not been cleared: 
9020 9022
An active call may be cleared using the "clear call voice" command.
```

If you try to clear multiple invalid ports (odd port, out of range, not allocated from table), the following error is displayed:

```
Router#clear voip rtp port 1 9008,9009,9010,9011
Any port(s) associated with an active call will not be cleared.[confirm]
Error: Port(s) 9008 9009 9010 9011  invalid for table 1.
Use 'show voip rtp stats' command to view the ports allocated to each table
```

If more than 32 ports are specified, the following error is displayed:

```
Router# clear voip rtp port 1 8000, 8002, 8004 ,8006 ,8008 , 8010, 8012, 8014, 8016, 8018, 8020, 8022, 8024, 8026, 8028, 8030, 8032, 8034, 8036, 8038, 8040, 8042, 8044, 8046, 8048, 8050, 8052, 8054, 8056, 8058, 8060, 8062, 8064
Any port(s) associated with an active call will not be cleared.[confirm]
Error: A maximum of 32 ports may be cleared.
```

If you want to clear an active call, use the 'clear call voice' command.

## clear voip stream-service connection

To delete a WebSocket connection in CUBE, use the clear voip stream-service connection id forced command in User EXEC or privileged EXEC mode.

clear voip stream-service connection id forced

### Syntax Description

id

The ID associated with a WebSocket connection.

### Command Default

This command is not enabled, and no connections are cleared.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

Cisco IOS XE Bengaluru 17.6.1a

This command was introduced.

### Usage Guidelines

Use this command to send close message on the WebSocket associated with the WebSocket ID. There are two versions of this command:

clear voip stream-service connection id —The command configuration for a scenario in which there are no active calls on the WebSocket connection.

clear voip stream-service connection id forced —The command configuration for a scenario in which there are active calls on the WebSocket connection.

If there are active calls on the WebSocket connection, the command clear voip stream-service connection id displays an error message that the connection cannot be cleared.

## Examples

The following is a sample output for clearing the WebSocket connection with ID 17 which has an active call.

To verify if there are active calls:

```
router#show voip stream-service connection 
ID   Local IP:Port        Remote IP:Port     Active Calls   Total Calls 
17   10.65.125.206:22377  10.64.86.215:8066  1              1
```

To clear the WebSocket connection:

```
router#clear voip stream-service connection 17
WARNING: There are active fork sessions on this WebSocket connection. 
Use clear voip stream-service connection <id> forced to delete this WebSocket connection.

router#clear voip stream-service connection 17 forced
1 active fork sessions will be deleted. Continue? [confirm]
```

To verify if the WebSocket connection with active calls is cleared:

```
router#show voip stream-service conn history
ID  Local IP:Port        Remote IP:Port     Total Calls  Disconnect Cause
6   10.65.125.206:21811  10.64.86.215:8062  0            WS_ACTIVE
8   10.65.125.206:29867  10.64.86.215:8063  1            WS_IDLE_TIMEOUT_CLOSURE
11  10.65.125.206:51108  10.64.86.215:8064  1            WS_IDLE_TIMEOUT_CLOSURE
14  10.65.125.206:29918  10.64.86.215:8065  1            WS_IDLE_TIMEOUT_CLOSURE
17  10.65.125.206:22377  10.64.86.215:8066  1            WS_CLEAR_COMMAND_CLOSURE
```

### Related Commands

Command

Description

show voip stream-service connection

Displays information about the active WebSocket connections in Unified Border Element.

show voip stream-service connection history

Displays information about all the closed WebSocket connections in Unified Border Element.

Displays information about the WebSocket connection based on WebSocket server IP and port.

## clear voip stream-service statistics

To reset the global WebSocket statistics on your CUBE, use the clear voip stream-service statistics command in User EXEC or privileged EXEC mode.

clear voip stream-service statistics

### Command Default

This command is not enabled by default, and no statistics are cleared.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

Cisco IOS XE Bengaluru 17.6.1a

This command was introduced.

### Usage Guidelines

Use this command to clear the global WebSocket statistics on a CUBE router.

## Examples

The following is a sample output for show voip stream-service statistics after the statistics are cleared by clear voip stream-service statistics .

```
router#clear voip stream-service statistics
router#show voip stream-service statistics
Active connections:             0 
Active forked calls:            0 
Total connections created:      0 
Total forked calls:             0 

Connection failures:
HTTP failures:                  0 
TCP failures:                   0 
Remote WebSocket closures:      0 
Remote TCP closures:            0 
Idle age-outs:                  0 

Message statistics:
WS_CREATE_REQ:                  0 
WS_CREATE_RSP_OK:               0 
WS_CREATE_RSP_FAIL:             0 
WS_CLOSE_REQ:                   0 
WS_CLOSE_RSP:                   0 
WS_DOWN:                        0 
WS_STATS_REQ:                   0 
WS_STATS_RSP:                   0
```

### Related Commands

Command

Description

show voip stream-service statistics

Displays statistical information about WebSocket connections in Unified Border Element.

show voip stream-service connection history

Displays information about all the closed WebSocket connections in Unified Border Element.

Displays information about the WebSocket connection based on WebSocket server IP and port.

## clear vsp statistics

To clear all Voice Streaming Processing (VSP) statistics that are displayed when the show vsp command is used, use the clear vsp statistics command in privileged EXEC mode.

clear vsp statistics

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(11)T

This command was introduced on the Cisco 3640, Cisco 3660, Cisco AS5300, Cisco AS5350, and Cisco AS5400.

### Usage Guidelines

This command resets all cumulative VSP statistics to 0. Use the show vsp statistics command to display the current statistics.

## Examples

The following example resets the statistics for VSP sessions:

```
Router# clear vsp statistics
```

### Related Commands

Command

Description

show vsp

Displays cumulative information about VSP sessions.

| serial | Makes a serial CCS connection for Frame Relay. |
|---|---|
| atm | Makes an ATM CCS connection. |
| dlci | (Optional) Specifies the data-link connection identifier
                                          						(DLCI) number. |
| pvc vpi / vci | (Optional) Specifies the permanent virtual circuit (PVC)
                                          						virtual path identifier (VPI) or virtual channel identifier (VCI). Range is
                                          						from 0 to 255; the slash is required. |
| pvc name | (Optional) Specifies the PVC string that names the PVC for
                                          						recognition. |
| cid-number | (Optional) If you have executed the ccs encap frf11 command, the cid-number argument allows you to
                                          						specify any channel identification (CID) number from 5 to 255. |

| Release | Modification |
|---|---|
| 12.0(2)T | This command was introduced on the Cisco MC3810. |
| 12.0(7)XK | The cidnumber argument was added; the dlci keyword and vcd options were removed. |
| 12.1(2)T | The CID syntax addition and removal of the dlci keyword and vcd options were integrated into
                                          						Cisco IOS Release 12.1(2)T. |
| 12.1(2)XH | This command was implemented on the Cisco 2600 series,
                                          						Cisco 3600 series, Cisco 7200 series, and Cisco 7500 series. |
| 12.1(3)T | This command was integrated into Cisco IOS Release
                                          						12.1(3)T. |

| Note | CDP and keepalives are disabled by default on a D-channel
                                          		  interface. |
|---|---|

| Command | Description |
|---|---|
| ccs encap frf11 | Allows the specification of the standard Annex-C FRF.11
                                          						format. |

| serial | Makes a serial CCS connection for Frame Relay. |
|---|---|
| atm | Makes an ATM CCS connection. |
| dlci | (Optional) Data-link connection identifier (DLCI) number. |
| pvc vpi / vci | (Optional) Permanent virtual circuit (PVC) virtual path identifier or virtual channel identifier (VCI). Range is from 0 to
                                          255; the slash is required. |
| pvc name | (Optional) PVC string that names the PVC for recognition. |
| cid - number | (Optional) If you have executed the ccs encap frf11 command, the cid-number argument allows you to specify any channel identification (CID) number from 5 to 255. |

| Release | Modification |
|---|---|
| 12.0(2)T | This command was introduced on the Cisco MC3810. |
| 12.0(7)XK | The cid-number argument was added; the dlci keyword and vcd options were removed. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.2(2)T | This command was implemented on the Cisco 7200 series router and integrated into Cisco IOS Release 12.2(2)T. |

| Note | Cisco Discovery Protocol and keepalives are disabled by default on a D-channel interface. |
|---|---|

| Command | Description |
|---|---|
| ccs encap frf11 | Allows the specification of the standard Annex-C FRF.11 format. |

| Release | Modification |
|---|---|
| 12.0(7)XK | This command was introduced for the Cisco MC3810. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.1(2)XH | This command was implemented on the Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, and Cisco 7500 series. |
| 12.1(3)T | This command was integrated into Cisco IOS Release 12.1(3)T. |

| Command | Description |
|---|---|
| mode ccs frame-forwarding | Set to forward frames on the controller. |
| ccs connect | Configures a CCS connection on an interface configured to support CCS frame forwarding. |

| compact | Compact set of voice attributes is generated in CDRs. |
|---|---|
| detailed | Full set of voice attributes is generated in CDRs. Default value. |

| Release | Modification |
|---|---|
| 12.4(15)XY | This command was introduced. |
| 12.4(20)T | This command was integrated into Cisco IOS Release 12.4(20)T. |

| Command | Description |
|---|---|
| acct-template | Selects a group of voice vendor-specific attributes to collect in accounting records. |
| maximum buffer-size | Sets the maximum size of the file accounting buffer. |
| maximum fileclose-timer | Sets the maximum time for saving records to an accounting file before closing the file and creating a new one. |
| primary | Sets the primary location for storing the CDRs generated for file accounting. |

| adaptive | Adjusts the output clock on a received ATM adaptation layer 1 (AAL1) on a first-in, first-out basis. Use in unstructured mode. |
|---|---|
| srts | Sets the clocking mode to synchronous residual time stamp. |
| synchronous | Configures the timing recovery to synchronous for structured mode. |

| Release | Modification |
|---|---|
| 12.1(2)T | This command was introduced. |

| Command | Description |
|---|---|
| controller | Configures the T1 or E1 controller. |

| tcp - port number | (Optional) Specifies the TCP port number for the CGMA to use in communication with a third-party management system. Range
                                          is from 5000 to 65535. The default is 5000. |
|---|---|
| time - period s econds | (Optional) Specifies the maximum time period, in seconds ,for maintaining the link between the CGMA and the third-party management
                                          system during a period of inactivity. If twice the timeout value is met or exceeded with no message received from the client,
                                          the TCP connection is closed. Additionally, a 60-second timer is maintained in the CGMA, which closes the connection if no
                                          handshake query message is received from the third-party management system for 60 seconds. Range is from 45 to 300. The default
                                          is 45. |

| Release | Modification |
|---|---|
| 12.2(2)XB | This command was introduced on the Cisco 2600 series, Cisco 3600 series, Cisco AS5300, Cisco AS5350, and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5800 for Cisco IOS release 12.2(2)XB1 release only. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 2600 series, Cisco 3600 series, and
                                          Cisco 7200 series. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5800 is not included in this release. |

| channel-group-number | Channel-group number on the Cisco 2600 series, Cisco 2600XM, Cisco 2691, Cisco
                                          						3631, Cisco 3660, Cisco 3725, and Cisco 3745 routers. When a T1 data line is
                                          						configured, channel-group numbers can be values from 0 to 23. When an E1 data
                                          						line is configured, channel-group numbers can be values from 0 to 30. Valid
                                          						values can be 0 or 1 on the Cisco AS5350 and Cisco AS5400. |
|---|---|
| timeslots range | Specifies one or more time slots separated by commas, and spaces or ranges of
                                          						time slots belonging to the channel group separated by a dash. The first time
                                          						slot is numbered 1. For
                                                							 a T1 controller, the time slots range from 1 to 24. For
                                                							 an E1 controller, the time slots range from 1 to 31. You can
                                          						specify a time slot range (for example, 1-29), individual time slots separated
                                          						by commas (for example 1, 3, 5), or a combination of the two (for example 1-14,
                                          						15, 17-31). See the "Examples" section for samples of different timeslot
                                          						ranges. |
| speed { 56 \| 64 } | (Optional) Specifies the speed of the underlying DS0s in kilobits per second.
                                          						Valid values are 56 and 64. The
                                          						default line speed when configuring a T1 controller is 56 kbps on the Cisco
                                          						2600 series, Cisco 2600XM series, Cisco 2691, Cisco 3631, Cisco 3660, Cisco
                                          						3725, Cisco 3745, and Cisco MC3810. The
                                          						default line speed when configuring an E1 controller is 64 kbps on the Cisco
                                          						2600 series, Cisco 2600XM series, Cisco 2691, Cisco 3631, Cisco 3660, Cisco
                                          						3725, Cisco 3745, and Cisco MC3810. The
                                          						line speed controls real-time (VBR-RT) traffic shaping, and the maximum burst
                                          						size (MBS) is 255 cells. |
| aim aim-slot-number | (Optional) Directs HDLC traffic from the T1/E1 interface to the
                                          						AIM-ATM-VOICE-30 digital signaling processor (DSP) card on the Cisco 2600
                                          						series, Cisco 2600XM series, Cisco 2691, Cisco 3631, Cisco 3660, Cisco 3725,
                                          						and Cisco 3745. |
| channel-number | Number
                                          						of the channel. Valid values can be 0 or 1 on the Cisco SLT (Cisco 2611). |
| unframed | Specifies the use of all 32 time slots for data. None of the 32 time slots is
                                          						used for framing signals on the Cisco ASR 901 Series, Cisco 2600XM series,
                                          						Cisco 2691, Cisco 3631, Cisco 3660, Cisco 3725, and Cisco 3745. This keyword is
                                          						applicable to E1 only. |

| Release | Modification |
|---|---|
| 11.3MA | This
                                          						command was introduced on the Cisco MC3810. |
| 12.0 | This
                                          						command was integrated into Cisco IOS Release 12.0 on the Cisco MC3810. |
| 12.0(7)XE | This
                                          						command was implemented on the Catalyst 6000 family switches. |
| 12.1(1)E | This
                                          						command was integrated into Cisco IOS Release 12.1(1)E. |
| 12.1(1)T | This
                                          						command was modified to accommodate two channel groups on a port on 1- and
                                          						2-port T1/E1 multiflex voice or WAN interface cards on the Cisco 2600 and Cisco
                                          						3600 series routers. |
| 12.1(3a)E3 | The
                                          						number of valid values for the kbps argument
                                          						was changed on the Cisco MC3810; see the "Usage Guidelines" section for valid
                                          						values. |
| 12.2(11)T | This
                                          						command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(15)T | The aim keyword
                                          						was added for use on the Cisco 2600 series (including the Cisco 2691), Cisco
                                          						2600XM, Cisco 3660, Cisco 3725, and Cisco 3745. |
| 12.3(1) | The unframed keyword was added for use on the Cisco 2600XM series, Cisco 2691, Cisco 3631,
                                          						Cisco 3660, Cisco 3725, and Cisco 3745. |
| 12.2SX | This
                                          						command is supported in the Cisco IOS Release 12.2SX train. Support in a
                                          						specific 12.2SX release of this train depends on your feature set, platform,
                                          						and platform hardware. |
| 15.4(3)S | This command was implemented on the Cisco ASR 901 Series
                                          						Aggregation Services Router. |

| Note | Neither the
                                          			 Cisco AS5400 series NAS nor the Cisco MC3810 is supported with the integrated
                                          			 voice and data WAN on T1/E1 interfaces using the AIM-ATM-VOICE-30 module. |
|---|---|

| Note | Channel groups,
                                          			 channel-associated signaling (CAS) voice groups, DS0 groups, and time-division
                                          			 multiplexing (TDM) groups all use group numbers. All group numbers configured
                                          			 for channel groups, CAS voice groups, and TDM groups must be unique on the
                                          			 local Cisco MC3810 concentrator. For example, you cannot use the same group
                                          			 number for a channel group and for a TDM group. Furthermore, on the Cisco
                                          			 MC3810, only one channel group can be configured on a controller. |
|---|---|

| Note | SS7 digital
                                          			 F-link support for the 8PRI line card requires use of a third onboard TDM
                                          			 stream to route trunk DS0 messages to the onboard MGCs. |
|---|---|

| Command | Description |
|---|---|
| framing | Specifies the frame type for the T1 or E1 data line. |
| invert data | Enables
                                          						channel inversion. |
| linecode | Specifies the line code type for the T1 or E1 line. |
| voice-card | Configures a card with voice processing resources and enters voice card
                                          						configuration mode. |
| encapsulation | Sets
                                          						the encapsulation type. |

| channel - id | A unique session channel ID. This session channel ID is needed when the link with a Reliable User Datagram Protocol (RUDP)
                                          session to the Media Gateway Controller (MGC) is associated. |
|---|---|
| session - set session - set - id | (Optional) Creates an SS7-link-to-SS7-session-set association on the Cisco AS5350- and Cisco AS5400-based Cisco Signaling
                                          Link Terminals (SLTs). The session-set-id argument represents the SS7 session ID. Valid values are 0 or 1. Default is 0. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced on the Cisco AS5350 and Cisco AS5400. |
| 12.2(15)T | The session-set session-set-id keyword and argument were added. |

| Command | Description |
|---|---|
| channel-group | Assigns a channel group and selects the DS0 timeslot desired for SS7 links. |
| encapsulation ss7 | Sets the encapsulation type to SS7. |
| no shutdown | Changes the administrative state of a port from out-of-service to in-service . |
| session-set | Creates an SS7-link-to-SS7-session-set association or to associate an SS7 link with an SS7 session set on the Cisco 2600-based
                                          SLT. |
| ss7 mtp2 variant bellcore | Configures the device for Telcordia (formerly Bellcore) standards. |

| ecdsa-cipher | (Optional) When the ecdsa-cipher keyword is not specified, the SIP TLS process uses larger set of ciphers depending on the support at the Secure Socket Layer
                                          (SSL). Following are the cipher suites that are supported: TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 TLS13_AES128_GCM_SHA256 TLS13_AES256_GCM_SHA384 TLS13_CHACHA20_POLY1305_SHA256 Note Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                                      within the system settings, they are no longer negotiable and will not be used for secure connections. CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA | Note | Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                                      within the system settings, they are no longer negotiable and will not be used for secure connections. CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA |
|---|---|---|---|
| Note | Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                                      within the system settings, they are no longer negotiable and will not be used for secure connections. CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA |
| curve-size 384 | (Optional) Configures specific size of elliptic curves to be used for a TLS session. You can configure an elliptic curve of
                                          size 384 bit. |
| strict-cipher | (Optional) The strict-cipher keyword supports only the TLS Rivest, Shamir, and Adelman (RSA) encryption with the Advanced Encryption Standard-128 (AES-128)
                                          cipher suite. Following are the cipher suites that are supported: TLS_RSA_WITH_AES_128_CBC_SHA TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA256 TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 TLS13_AES128_GCM_SHA256 TLS13_AES256_GCM_SHA384 TLS13_CHACHA20_POLY1305_SHA256 Note Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                                      within the system settings, they are no longer negotiable and will not be used for secure connections. CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA Note When the strict-cipher keyword is
                                                      not specified, the SIP TLS process uses the default set of
                                                      ciphers depending on the support at the Secure Socket Layer
                                                      (SSL). Note In the Cisco IOS XE 17.18.2 release, a security warning message appears for strict-cipher configurations. The strict-cipher includes weaker ciphers such as: DHE_RSA_WITH_AES_128_CBC_SHA DHE_RSA_WITH_AES_256_CBC_SHA RSA_WITH_AES_128_CBC_SHA RSA_WITH_AES_256_CBC_SHA | Note | Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                                      within the system settings, they are no longer negotiable and will not be used for secure connections. CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA | Note | When the strict-cipher keyword is
                                                      not specified, the SIP TLS process uses the default set of
                                                      ciphers depending on the support at the Secure Socket Layer
                                                      (SSL). | Note | In the Cisco IOS XE 17.18.2 release, a security warning message appears for strict-cipher configurations. The strict-cipher includes weaker ciphers such as: DHE_RSA_WITH_AES_128_CBC_SHA DHE_RSA_WITH_AES_256_CBC_SHA RSA_WITH_AES_128_CBC_SHA RSA_WITH_AES_256_CBC_SHA |
| Note | Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                                      within the system settings, they are no longer negotiable and will not be used for secure connections. CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA |
| Note | When the strict-cipher keyword is
                                                      not specified, the SIP TLS process uses the default set of
                                                      ciphers depending on the support at the Secure Socket Layer
                                                      (SSL). |
| Note | In the Cisco IOS XE 17.18.2 release, a security warning message appears for strict-cipher configurations. The strict-cipher includes weaker ciphers such as: DHE_RSA_WITH_AES_128_CBC_SHA DHE_RSA_WITH_AES_256_CBC_SHA RSA_WITH_AES_128_CBC_SHA RSA_WITH_AES_256_CBC_SHA |

| Note | Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                                      within the system settings, they are no longer negotiable and will not be used for secure connections. CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA |
|---|---|

| Note | Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                                      within the system settings, they are no longer negotiable and will not be used for secure connections. CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA |
|---|---|

| Note | When the strict-cipher keyword is
                                                      not specified, the SIP TLS process uses the default set of
                                                      ciphers depending on the support at the Secure Socket Layer
                                                      (SSL). |
|---|---|

| Note | In the Cisco IOS XE 17.18.2 release, a security warning message appears for strict-cipher configurations. The strict-cipher includes weaker ciphers such as: DHE_RSA_WITH_AES_128_CBC_SHA DHE_RSA_WITH_AES_256_CBC_SHA RSA_WITH_AES_128_CBC_SHA RSA_WITH_AES_256_CBC_SHA |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE 26.1.1 | The command is modified to indicate that the following non-compliant ciphers are not supported: CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA |
| Cisco IOS XE 17.18.2 | This command is modified to display security warnings for usage of legacy TLS and associated weaker ciphers. |
| Cisco IOS XE 17.14.1a | This command is modified to support TLS version 1.3 ciphers. Introduced support for TLS version 1.3 ciphers Yang Model. |
| Cisco IOS XE Amsterdam 17.3.1a | This command was introduced under voice class configuration mode. Introduced support for Yang Model. |

| Note | Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                          within the system settings, they are no longer negotiable and will not be used for secure connections. CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA |
|---|---|

| Command | Description |
|---|---|
| voice class tls-profile | Provides sub-options to configure the commands that are required for a TLS session. |
| crypto signaling | Identifies the trustpoint or the tls-profile tag that is used during the TLS handshake process. |

| cipher-list | Specifies list of 13 supported ciphers. |
|---|---|
| cipher-name | The following lists the names of the cipher suite: AES128_GCM_SHA256 AES256_GCM_SHA384 CHACHA20_POLY1305_SHA256 DHE_RSA_AES128_GCM_SHA256 DHE_RSA_AES256_GCM_SHA384 DHE_RSA_WITH_AES_128_CBC_SHA DHE_RSA_WITH_AES_256_CBC_SHA ECDHE_RSA_AES128_GCM_SHA256 ECDHE_RSA_AES256_GCM_SHA384 RSA_WITH_AES_128_CBC_SHA RSA_WITH_AES_256_CBC_SHA ECDHE_ECDSA_AES128_GCM_SHA256 ECDHE_ECDSA_AES256_GCM_SHA384 Note Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                                   within the system settings, they are no longer negotiable and will not be used for secure connections. CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA | Note | Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                                   within the system settings, they are no longer negotiable and will not be used for secure connections. CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA |
| Note | Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                                   within the system settings, they are no longer negotiable and will not be used for secure connections. CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA |

| Note | Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                                   within the system settings, they are no longer negotiable and will not be used for secure connections. CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE 26.1.1 | The command is modified to indicate that the following non-compliant ciphers are not supported: CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA |
| Cisco IOS XE 17.18.2 | The command is modified to display security warnings for usage of legacy TLS and associated weaker ciphers. |
| Cisco IOS XE 17.14.1a | Introduced support for TLS version 1.3 ciphers. Following are the three ciphers supported with TLS version 1.3: AES128_GCM_SHA256 AES256_GCM_SHA384 CHACHA20_POLY1305_SHA256 |
| Cisco IOS XE Cupertino
                                             17.8.1a | This command was introduced. |

| Note | Starting from Cisco IOS XE 26.1.1 release, support for the following non-compliant ciphers has been discontinued. While these ciphers may remain configurable
                                          within the system settings, they are no longer negotiable and will not be used for secure connections. CHACHA20_POLY1305_SHA256 DHE_RSA_WITH_AES_256_CBC_SHA |
|---|---|

| Command | Description |
|---|---|
| voice class tls-cipher | Configures an ordered set of TLS cipher suites |
| crypto signaling | Identifies the trustpoint or the tls-profile tag that is used during the TLS handshake process. |

| all | All available session groups. |
|---|---|
| name group - name | A specified session group. |

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced. |
| 12.2(2)T | This command was implemented on the Cisco 7200. |
| 12.2(4)T | This command was implemented on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco IAD2420 series. |
| 12.2(11)T | This command was implemented on the Cisco AS5350, Cisco AS5400, and Cisco AS5850. |

| Command | Description |
|---|---|
| show backhaul-session-manager group | Displays status, statistics, or configuration of a specified group or all session groups. |

| aaa | Authentication, authorization, and accounting (AAA) interface type. |
|---|---|
| asr | Automatic speech recognition (ASR) interface type. |
| flash | Flash memory of the Cisco gateway. |
| http | HTTP interface type. |
| ram | Memory of the Cisco gateway. |
| rtsp | Real-Time Streaming Protocol (RTSP) interface type. |
| smtp | Simple Mail Transfer Protocol (SMTP) interface type. |
| tftp | TFTP interface type. |
| tts | Text-to-speech (TTS) interface type. |
| server server | (Optional) Clears statistics or event logs for the specified server. |
| event-log | (Optional) Clears event logs. |
| stats | (Optional) Clears statistic counters. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |

| Command | Description |
|---|---|
| call application interface event-log | Enables event logging for external interfaces used by voice applications. |
| call application interface stats | Enables statistics collection for application interfaces. |
| clear call application stats | Clears application-level statistics in history and subtracts the statistics from the gateway-level statistics. |
| show call application interface | Displays event logs and statistics for application interfaces. |

| app-tag application-name | (Optional) Clears statistics for the specified voice application. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |

| Note | Statistic counters are automatically cleared for an application if the application is deleted with the no call application voice command or the script is reloaded with the call application voice load command. |
|---|---|

| Command | Description |
|---|---|
| call application stats | Enables statistics collection for voice applications. |
| call application voice load | Reloads the designated Tcl script. |
| clear call application interface | Clears application interface statistics and event logs. |
| call application voice | Reloads the designated Tcl script or VoiceXML document. |
| show call application app-level | Displays application-level statistics for voice applications. |
| show call application gateway-level | Displays gateway-level statistics for voice application instances. |

| ip - address | (Optional) The target IP address. If no IP address is specified, all IP addresses are cleared. |
|---|---|
| codec codec-type | (Optional) Specifies the associated codec type. |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810 series routers. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)T | This command was modified. The Public Switching Telephone Network (PSTN) Fallback feature and enhancements were implemented
                                          on the Cisco 7200 series routers and integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(4)T2 | This command was implemented on the Cisco 7500 series routers. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |
| 15.0(1)M | This command was modified in a release earlier than Cisco IOS Release 15.0(1)M. The codec keyword and codec-type argument were added. |

| Command | Description |
|---|---|
| show call fallback cache | Displays the current ICPIF estimates for all IP addresses in the call fallback cache. |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850 platform. |
| 12.2(4)T | The PSTN Fallback feature and enhancements were implemented on the Cisco 7200 series and integrated into Cisco IOS Release
                                          12.2(4)T. |
| 12.2(4)T2 | This command was implemented on the Cisco 7500 series. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Command | Description |
|---|---|
| show call fallback stats | Displays the call fallback statistics. |

| dead-memory | Clears unreleased Communication Media Module (CMM) line card memory. |
|---|---|
| trace | Clears CMM trace buffers. |

| Release | Modification |
|---|---|
| 15.0(1)M | This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M. |

| Command | Description |
|---|---|
| clear tgrep neighbor | Clears TGREP counters and sessions. |

| interface - | Specifies the interface through which calls arrive. Types of interfaces and their numbers depends upon the configured interfaces. |
|---|---|
| type | Interface type. Values include: ethernet fastethernet GigabitEthernet serial |
| number | Interface or subinterface number. For more information about the numbering syntax for your networking device, use the question
                                          mark (?) online help function. |
| stats | Resets all call threshold statistics. |
| total - calls value | Resets the counter when the call volume reaches the specified number. The value argument represents call volume. Range is from 0 to 10000 calls. The default is 0. |
| int-calls value | Number of calls transmitted through the interface. The value argument clears calls when they reach a specified volume through the interface. Range is from 0 to 10000 calls. The default
                                          is 0. |

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | The command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          is not included in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)XM | This command was implemented on the Cisco 1750 and Cisco 1751 routers. Support for other Cisco platforms is not included
                                          in this release. |
| 12.2(8)T | This command was integrated into the Cisco IOS Release 12.2(8)T and implemented on the Cisco 7200 series routers. Support
                                          for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command was implemented on the Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850. |

| Command | Description |
|---|---|
| call threshold | Enables the global resources of a gateway. |
| call threshold poll-interval | Enables a polling interval threshold for CPU or memory. |
| show call treatment | Displays the call treatment configuration and statistics for handling the calls on the basis of resource availability. |

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | The command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 series
                                          is not included in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)XM | This command was implemented on the Cisco 1750 and Cisco 1751 routers. Support for other Cisco platforms is not included in
                                          this release. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 7200 series routers. Support for
                                          the Cisco AS5300, 
                                          Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release. |
| 12.2(11)T | This feature was integrated into Cisco IOS Release 12.2(11)T and support was added for the Cisco AS5300, Cisco AS5350, Cisco
                                          AS5400, and Cisco AS5800. |

| Command | Description |
|---|---|
| call treatment on | Enables call treatment to process calls when local resources are unavailable. |
| call treatment action | Configures the action that the router takes when local resources are unavailable. |
| call treatment cause-code | Specifies the reason for the disconnection to the caller when local resources are unavailable. |
| call treatment isdn-reject | Specifies the rejection cause-code for ISDN calls when local resources are unavailable. |
| show call treatment | Displays the call treatment configuration and statistics for handling calls on the basis of resource availability. |

| stale-entry | Clears entries of active calls that are deemed stale or invalid from the call table. |
|---|---|
| causecode | Specifies a Q.850 disconnect cause code. |
| identifier | Numeric cause code identifier; a number 1 through 127. |
| id identifier | Clears one specific call with the ID specified. The identifier argument is the call identifier as shown in brief format. |
| media-inactive | Clears calls wherever a status of media inactive is detected and notified. |
| calling-number number | Clears a call with a specific calling number pattern. The number argument is the specific call number pattern of the calling number. |
| called-number number | Clears a call with a specific called number pattern. The number argument is the specific call number pattern of a called number. |
| fpi-correlator correlator-id | Clears calls based on VoIP FPI correlator. |
| fpi-stale | Clears all hung FPI call. |
| long-dur-call | Clears only call with long-duration being detected and notified. |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced. |
| 12.2 | This command was integrated into Cisco IOS Release 12.2. |
| 12.3(4)T | The voice keyword was added. |
| 12.4(4)T | The calling-number and called-number keywords were added. |
| 15.5(2)T | The fpi-correlator keyword was added. |

| Command | Description |
|---|---|
| show call active voice | Displays active voice calls, based on specified parameters. |

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          is not included in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. and implemented on the Cisco AS5300, Cisco AS5350, Cisco AS5400,
                                          and Cisco AS5850. |

| Command | Description |
|---|---|
| call-router | Enables the Annex G BE configuration commands. |
| show call history | Displays the fax history table for a fax transmission. |

| system - hwm | Clears the system HWMs only. |
|---|---|
| all | Clears all controller call counters including the individual controller time slots in use and the number of calls on those
                                          time slots since the last reset was done. The HWMs are set to 0. |

| Release | Modification |
|---|---|
| 12.0(1)T | This command was introduced. |
| 12.1(1)T | This command was implemented on the voice/WAN interface cards (VWICs) for the Cisco 2600 series and Cisco 3600 series. |
| 12.1(2)T | This command was implemented on the Cisco AS5300, Cisco AS5400, and Cisco AS5800. |

| Command | Description |
|---|---|
| clear controller t1 call-counters | Clears call statistics on a specific T1 controller. |
| controller | Enters controller configuration mode. |
| show controllers t1 call-counters | Displays the total number of calls and call durations on a T1 controller. |

| slot | (Optional) Clears an individual T1 controller. |
|---|---|
| call - counters timeslots | Clears the call counters in the specified T1 time slots. |
| firmware - status | Clears the Neat crash history. |

| Release | Modification |
|---|---|
| 12.0(1)T | This command was introduced. |
| 12.1(1)T | This command was implemented on the voice and WAN interface cards (VWICs) for the Cisco 2600 series and Cisco 3600 series. |
| 12.1(2)T | This command was implemented on the Cisco AS5300, Cisco AS5400, and Cisco AS5800. |

| Note | In the preceding example, all the fields are zero, indicating that no calls have come in since system startup or since the
                                          last clear was made by the clear controller command. |
|---|---|

| Command | Description |
|---|---|
| clear controller call-counters | Clears all call statistics or system HWMs on a router. |
| controller | Enters controller configuration mode. |
| show controllers t1 call-counters | Displays the total number of calls and call durations on a T1 controller. |

| slot / port | (Optional) Identifies the location (and thereby the
                                          						identity) of a specific modem. |
|---|---|
| modem - group - number | (Optional) Designates a defined modem group. |

| Release | Modification |
|---|---|
| 11.3NA | This command was introduced. |

| Command | Description |
|---|---|
| clear csm-statistics voice | Clears the CSM statistics for a particular or for all DSP
                                          						channels. |

| slot / dspm / dsp / dsp - channel | (Optional) Identifies the location of a particular DSP channel. |
|---|---|

| Release | Modification |
|---|---|
| 11.3NA | This command was introduced. |

| Command | Description |
|---|---|
| clear csm - statistics modem | Clears the CSM statistics for a modem or group of modems. |

| all | Forces all active calls currently associated with this gatekeeper to be disconnected. |
|---|---|
| local - callID | Forces a single active call associated with this gatekeeper to be disconnected. |
| local-callID | Specifies the local call identification number (CallID) that identifies the call to be disconnected. |

| Release | Modification |
|---|---|
| 12.0(5)T | This command was introduced on the Cisco 2600 series, the Cisco 3600 series, and on the Cisco MC3810. |
| 12.1(5)XM2 | The command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco AS5300. Support for the Cisco AS5350
                                          and Cisco AS5400 is not included in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |

| Command | Description |
|---|---|
| show gatekeeper calls | Displays the status of each ongoing call of which a gatekeeper is aware. |

| alias e164 digits | E.164 alphanumeric address that is specified in the local alias table. |
|---|---|
| alias h323id name | H.323 ID name that is specified in the local alias table and is an alternate way to reach an endpoint. |
| all | All endpoints. |
| id number | ID of the endpoint. |
| ipaddr address [ port ] | Call signaling address and port (optional) of the endpoint. If a value for the port argument is not specified, the default is 1720. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced 12.2(11)T on the Cisco 3660 and Cisco MC3810. |

| Note | The endpoint that was unregistered using this command can come back if it sends the registration request (RRQ) back to the
                                          gatekeeper after the unregistration. |
|---|---|

| Command | Description |
|---|---|
| show gatekeeper endpoints | Locates the endpoint in a gatekeeper cluster. |

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |

| Command | Description |
|---|---|
| show gatekeeper performance statistics | Displays information about the number of calls accepted and rejected by the gatekeeper. |

| cause - codes | (Optional) Clears only the disconnected cause code counters. |
|---|---|
| h225 | (Optional) Clears only the H.225 counters. |
| ras | (Optional) Clears only the Registration, Admission, and Status (RAS) counters. |

| Release | Modification |
|---|---|
| 12.2(4)T | This command was introduced on all Cisco H.323 platforms except for the Cisco AS5300, Cisco AS5350, and Cisco AS5400. |

| Command | Description |
|---|---|
| debug cch323 | Provides debug output for various components within the H.323 subsystem. |
| show h323 gateway | Displays the statistics for H.323 gateway messages that have been sent and received and displays the reasons for which H.323
                                          calls have been disconnected. |

| Release | Modification |
|---|---|
| 12.4(15)T | This command was introduced. |

| Command | Description |
|---|---|
| show http client statistics | Displays information about the communication between the HTTP server and the client. |

| Release | Modification |
|---|---|
| 12.4(11)T | This command was introduced. |

| Command | Description |
|---|---|
| show interfaces | Displays statistics for all interfaces configured. |
| show interfaces cable-modem | Displays statistics for all interfaces configured on the port. |

| Release | Modification |
|---|---|
| IOS XE 16.10.1 | This command was introduced. |

| Command | Description |
|---|---|
| show media-proxy sessions summary history | Displays the summary of the completed CUBE MediaProxy SIP recording sessions. |

| Release | Modification |
|---|---|
| 12.2(2)XB | This command was introduced. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5350, Cisco AS5400, and Cisco AS5850. |

| Command | Description |
|---|---|
| show mgcp statistics | Displays MGCP statistics regarding received and transmitted network messages. |

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced on the Cisco AS5300. |
| 12.1(3)T | This command was implemented on the Cisco 3660, Cisco UBR924, and Cisco 2600 series. |
| 12.2(11)T | This command was implemented on the Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts the MGCP daemon. |
| show mgcp statistics | Displays statistics for received and transmitted packets. |

| all | Clears the accumulated MRCP session statistics for all hosts. |
|---|---|
| hostname | Clears the accumulated MRCP session statistics for the specified host. |
| hostname | Host name of the MRCP server. Format uses host name only or hostname : port . |
| ip - address | IP address of the MRCP server. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced on the Cisco 3640, Cisco 3660, Cisco AS5300, Cisco AS5350, and Cisco AS5400. |

| Command | Description |
|---|---|
| show mrcp client statistics hostname | Displays cumulative information about MRCP sessions. |

| group-number | (Optional) RLM group number. Range is from 0 to 255. There is no default value. |
|---|---|
| link | (Optional) Specifies the RLM group link. |
| statistics | (Optional) Specifies the RLM group statistics. |

| Release | Modification |
|---|---|
| 11.3(7) | This command was introduced. |
| 15.0(1)M | This command was modified in a release earlier than Cisco IOS Release 15.0(1)M. The statistics keyword was added. |

| Command | Description |
|---|---|
| clear interface | Resets the hardware logic on an interface. |
| interface | Defines the IP addresses of the server, configures an interface type, and enters interface configuration mode. |
| link (RLM) | Specifies the link preference. |
| protocol rlm port | Reconfigures the port number for the basic RLM connection for the whole RLM group. |
| retry keepalive | Allows consecutive keepalive failures a certain amount of time before the link is declared down. |
| server (RLM) | Defines the IP addresses of the server. |
| show rlm group statistics | Displays the network latency of the RLM group. |
| show rlm group status | Displays the status of the RLM group. |
| show rlm group timer | Displays the current RLM group timer values. |
| timer | Overwrites the default setting of timeout values. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| show rpms-proc counters | Displays statistics for the number of leg 3 AAA preauthentication requests, successes, and rejects. |

| Release | Modification |
|---|---|
| 12.0(7)XR | This command was introduced. |
| 12.1(1)T | This command was integrated into Cisco IOS Release 12.1(1)T. |

| Command | Description |
|---|---|
| show rudpv0 failures | Displays RUDP information about failed connections and the reasons for them. |
| show rudpv0 statistics | Displays RUDP information about number of packets sent, received, and so forth. |

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced. |
| 12.2(2)T | This command was implemented on Cisco 7200. |
| 12.2(4)T | This command was implemented on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco IAD2420 series. |
| 12.2(11)T | This command was implemented on the Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 in this release. |

| Command | Description |
|---|---|
| debug rudpv1 | Displays debugging information for RUDP. |
| show rudpv1 | Displays RUDP information. |

| Release | Modification |
|---|---|
| 12.4(15)XY | This command was introduced. |
| 15.0(1)M | This command was integrated into a release earlier than Cisco IOS Release 15.0(1)M. |

| Command | Description |
|---|---|
| show sccp server statistics | Displays the number of SCCP messages sent and received by the SCCP server. |

| Release | Modification |
|---|---|
| 12.4(15)XY | This command was introduced. |

| Command | Description |
|---|---|
| show sdspfarm message statistics | Displays the number of SCCP messages sent and received by the SCCP server. |
| show sdspfarm sessions state | Displays the number of sessions in each SCCP call state. |

| Release | Modification |
|---|---|
| 12.0(5)T | This command was introduced in a private release on the Cisco AS5300 only and was not generally available. |
| 12.0(7)XK | This command was implemented on the Cisco MC3810 and the Cisco 3600 series (except for the Cisco 3620) in a private release
                                          that was not generally available. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |

| Command | Description |
|---|---|
| show sgcp statistics | Displays global statistics for SGCP packet counts. |

| passthrough | Clears SIP registration passthrough status |
|---|---|
| all | Clears SIP registration records of all user agents |
| call-id call-id | Clears SIP registration records of the user agent with the specified call ID |
| dial-peer dial-peer | Clears SIP registration records of user agents on the specified dial peer |
| dn dn | Clears SIP registration records of user agents on the specified directory number |

| Release | Modification |
|---|---|
| IOS XE Fuji Release 16.8.1 | This command was introduced. |

| clear sip ua-statistics | Clears all SIP statistics counters. |
|---|---|
| show sip-ua registration passthrough status | Displays the SIP user agent pass-through status information . |

| tag | Specifies the unique dial-peer identifier (tag) for the peer. Value Range: 1-2147483647 |
|---|---|
| dial-peer | Clears the unique dial-peer identifier statistics. |

| Release | Modification |
|---|---|
| Cisco IOS XE 17.18.2 | This command is modified to clear SIP global error counters for dial-peer. |
| 12.2(13)T | This command was introduced. |

| Command | Description |
|---|---|
| show sip-ua statistics | Displays response, traffic, and retry SIP statistics. |

| id connection-id | Specifies the ID of the connection that needs to be closed
                                          						in the SIP TCP process. The connection-id argument represents the connection ID. The range is
                                          						from 1 to 2048. |
|---|---|
| target ipv4: address : port | Specifies the target address for the connection that needs
                                          						to be closed in the SIP transport layer. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.4(6)T | This command was replaced by the clear sip-ua command. |

| Command | Description |
|---|---|
| clear sip-ua udp connection | Clears a SIP UDP connection. |
| show sip-ua connections | Displays SIP UA transport connection tabless. |
| timers connection aging | Sets the time before the SIP UA ages out a TCP and UDP
                                          						connection. |

| id connection-id | Specifies the ID of the connection that needs to be closed
                                          						in the SIP TCP process. The connection-id argument represents the connection ID. The range is
                                          						from 1 to 2048. |
|---|---|
| target ipv4: address : port | Specifies the target address for the connection that needs
                                          						to be closed in the SIP transport layer. |

| Release | Modification |
|---|---|
| 12.4(6)T | This command was replaced by the clear sip-ua command. |

| Command | Description |
|---|---|
| clear sip-ua udp connection | Clears a SIP UDP connection. |
| show sip-ua connections | Displays SIP UA transport connection tabless. |
| timers connection aging | Sets the time before the SIP UA ages out a TCP and UDP
                                          						connection. |

| id value | Specifies the ID of the connection that needs to be closed in the SIP UDP process. The value argument represents the value of the connection ID. The range is from 1 to 2048. |
|---|---|
| target ip - address | Specifies the target address for the connection that needs to be closed in the SIP transport layer. The ip-address argument is the target address in the form of ipv4: address : port . |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| 12.4(6)T | This command was replaced by the clear sip-ua command. |

| Note | Inappropriate usage of the clear command without understanding the issue or the implications would lead to erroneous call behavior, inappropriate usage of
                                          connections, and failure of calls. |
|---|---|

| Command | Description |
|---|---|
| clear sip-ua tcp connection | Clears a SIP TCP connection. |
| show sip-ua connections | Displays SIP UA transport connections. |
| timers connection aging | Sets the time before the SIP UA ages out a TCP and UDP connection. |

| session-set | (Optional) Specifies the session set. |
|---|---|
| number | (Optional) Specifies the session-set number. The range is from 0 to 3. |

| Release | Modification |
|---|---|
| 12.0(7)XR | This command was introduced. |
| 12.1(1)T | This command was integrated into Cisco IOS Release 12.1(1)T. |
| 15.0(1)M | This command was modified in a release earlier than Cisco IOS Release 15.0(1)M. The session-set keyword and number argument were added. |

| Command | Description |
|---|---|
| show ss7 sm stats | Displays session manager information about number of packets queued, received, and so forth. |

| tag | (Optional) Identification tag number of a specific dial
                                          						peer. A valid entry is any integer that identifies a specific dial peer. Range
                                          						is from 1 to 2147483647. |
|---|---|
| busy-trigger-counter | (Optional) Specifies to clear the dial peer busy trigger
                                          						call counter. |

| Release | Modification |
|---|---|
| 12.2(8)T | This command was introduced on the Cisco AS5300. |
| 15.0(1)M | This command was modified in a release earlier than Cisco
                                          						IOS Release 15.0(1)M. The busy-trigger-counter keyword was
                                          						added. |
| Cisco IOS XE Release 2.1 | This command was integrated into Cisco IOS XE Release 2.1
                                          						and implemented on the Cisco ASR 1000 Series Aggregation Services Routers. |

| Command | Description |
|---|---|
| dial-peer voice | Enters dial peer configuration mode and specifies the
                                          						method of voice encapsulation. |
| show call history voice record | Displays CDR events in the call history table. |
| show dial-peer voice | Displays configuration information for dial peers. |

| all | Clears all STCAPP statistics. |
|---|---|
| port | Clears port-level STCAPP statistics. |
| slot-number | Voice interface slot number. The range is from 0 to 2147483647. |

| Release | Modification |
|---|---|
| 15.0(1)M | This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M. |

| Command | Description |
|---|---|
| stcapp | Enables the STCAPP. |

| all | All active subscriptions. |
|---|---|
| session-id session-id | Subscription session to be cleared. |
| statistics | Global subscription statistics and all subscription history records. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| retry subscribe | Configures the number of retries for SUBSCRIBE messages. |
| show subscription sip | Displays active SIP subscriptions. |
| subscription maximum | Specifies the maximum number of outstanding subscriptions to be accepted or originated by the gateway. |

| * | Clears all TGREP counters. |
|---|---|
| carrier | Clears available circuit counters. |
| string | Carrier ID. |
| dial-peer | Clears dial-peer. |
| tag | Dial peer tag. The range is from 1 to 2147483647. |
| trunk-group label | Clears the trunk-group counters. |
| csr | (Optional) Clears the call success rate counters. |
| ac | (Optional) Clears all the available circuit counters. |

| Release | Modification |
|---|---|
| 15.0(1)M | This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M. |

| Command | Description |
|---|---|
| clear tgrep neighbor | Clears all neighbor sessions. |

| * | Clears all neighbor sessions. |
|---|---|
| ip-address | IP addresses of neighbor sessions. |

| Release | Modification |
|---|---|
| 15.0(1)M | This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M. |

| Command | Description |
|---|---|
| clear tgrep counters | Clears TGREP counters. |

| method-list-name | Name of the method list. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| voice statistics type csr | Configures the collection of signaling and VoIP AAA accounting statistics. |

| channels | Clears DSP calls on a specific channel or a range of
                                       					 channels. |
|---|---|
| error | Clears DSP error statistics. |
| slot | (Optional) Specifies either a single slot or the first slot
                                       					 in a range. To specify a range of slots, you can enter a second slot in the syntax of this argument. The second slot specifies the end of the range. All slots in the range are affected
                                       					 by the command. |
| / dsp | (Optional) Specifies either a single DSP on the slot or the
                                       					 first DSP in a range. To specify a range of DSPs, you can enter a second DSP in the syntax of this argument. The second DSP specifies the end of the range. All DSPs in the range are affected
                                       					 by the command. |
| / channel | (Optional) Specifies either a single channel on the DSP or
                                       					 the first channel in a range. To specify a range of channels, you can enter a second channel in the syntax of this argument. The second channel specifies the end of the range. All channels in the range are
                                       					 affected by the command. |

| Release | Modification |
|---|---|
| 12.4(4)XC | This command was introduced. |
| 12.4(9)T | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| show voice dsp | Displays the current status or selective statistics of DSP
                                          						voice channels |

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |

| csr | (Optional) All accounting and signaling statistics are cleared, but Cisco VoIP internal error codes (IECs) are not cleared. |
|---|---|
| accounting | (Optional) Only accounting statistics are cleared. |
| signaling | (Optional) Only signaling statistics are cleared. |
| iec | (Optional) Only Cisco VoIP IECs are cleared. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| voice statistics type csr | Configures the collection of signaling and VoIP AAA accounting statistics. |

| Release | Modification |
|---|---|
| Cisco IOS XE Release 3.9S | This command was introduced. |

| Release | Modification |
|---|---|
| Cisco IOS XE Release 3.9S | This command was introduced. |

| table-id | Use the 'show voip rtp stats' command to establish the table identifier for the hung port that needs to be cleared. |
|---|---|
| ports | List of up to 32 comma separated port numbers in the range 5500 to 65498. |

| Release | Modification |
|---|---|
| Cisco IOS XE Bengaluru 17.4.1a | This command is introduced. |

| Note | If you want to clear an active call, use the 'clear call voice' command. |
|---|---|

| id | The ID associated with a WebSocket connection. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Bengaluru 17.6.1a | This command was introduced. |

| Note | If there are active calls on the WebSocket connection, the command clear voip stream-service connection id displays an error message that the connection cannot be cleared. |
|---|---|

| Command | Description |
|---|---|
| show voip stream-service connection | Displays information about the active WebSocket connections in Unified Border Element. |
| show voip stream-service connection history | Displays information about all the closed WebSocket connections in Unified Border Element. |
| show voip stream-service server <ip:port> | Displays information about the WebSocket connection based on WebSocket server IP and port. |

| Release | Modification |
|---|---|
| Cisco IOS XE Bengaluru 17.6.1a | This command was introduced. |

| Command | Description |
|---|---|
| show voip stream-service statistics | Displays statistical information about WebSocket connections in Unified Border Element. |
| show voip stream-service connection history | Displays information about all the closed WebSocket connections in Unified Border Element. |
| show voip stream-service server <ip:port> | Displays information about the WebSocket connection based on WebSocket server IP and port. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced on the Cisco 3640, Cisco 3660, Cisco AS5300, Cisco AS5350, and Cisco AS5400. |

| Command | Description |
|---|---|
| show vsp | Displays cumulative information about VSP sessions. |