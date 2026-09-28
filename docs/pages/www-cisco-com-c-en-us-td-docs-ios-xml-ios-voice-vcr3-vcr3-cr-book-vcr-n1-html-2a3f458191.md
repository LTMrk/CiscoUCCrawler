---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr3-vcr3-cr-book-vcr-n1-html-2a3f458191
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr3/vcr3-cr-book/vcr-n1.html
retrieved_at: 2026-08-16T23:18:33.894303+00:00
---

Cisco IOS Voice Command Reference - K through R

# Cisco IOS Voice Command Reference - K through R

Updated: December 21, 2024

Chapter: N

## Chapter: N

# N

## name (dial peer cor custom)

To specify the name for a custom class of restrictions (COR), use the name command in dial peer COR custom configuration mode. To remove a specified COR, use the no form of this command.

name class-name

no name class-name

### Syntax Description

class-name

Name that describes the specific COR.

### Command Default

No default behavior or values.

### Command Modes

Dial peer COR custom configuration

## Command History

Release

Modification

12.1(3)T

This command was introduced.

### Usage Guidelines

The dial-peer cor custom and name commands define the names of capabilities on which to apply COR operation. Examples of names might include any of the following:
                              call1900, call527, call9, or call 911. You must define the capabilities before you specify the COR rules.

You can define a maximum of 64 COR names.

## Examples

The following example defines three COR names:

```
dial-peer cor custom
 name 900_call
 name 800_call
 name catchall
```

### Related Commands

Command

Description

dial-peer cor custom

Specifies that named CORs apply to dial peers.

name

Assigns a name to the internal adapter.

## nat (sip-ua)

To use the SIP Network Address Translation (NAT) global configuration, use the nat command in SIP user agent configuration mode. To disable the nat configuration, use the no or default form of this command.

nat auto { force-on | force-off }

no nat

auto

Sets the symmetric NAT endpoint role to auto. Autodetect subscriber in a remote subnet when located behind a NAT.

force-on

Sets the symmetric NAT endpoint role to force-on. Assume that all remote subscribers are behind the NAT device.

### Command Modes

SIP user agent configuration (sip-ua)

Voice class tenant configuration (config-class)

Voice service SIP configuration (conf-serv-sip)

Release

Modification

12.2(13)T

This command was introduced.

Cisco IOS XE Dublin
                                             17.10.1a

Introduced support for YANG models.

## Examples

The following example shows how to set the endpoint role in connection setup to active:

```
Router(config)# sip-ua Router(config-sip-ua)# nat auto
```

```
Router(config)# sip-ua Router(config-sip-ua)# nat force-on
```

### Related Commands

Command

Description

nat symmetric check-media-src

Enables source media checking for symmetric NAT.

## nat media-keepalive

To enable media keepalive packets transmission for the specified interval of time (in seconds) at tenant or global level,
                              use the nat media-keepalive command in voice class tenant configuration (config-class) or voice service SIP configuration (conf-serv-sip) mode. To disable
                              the nat configuration, use the no or default form of this command.

nat { auto | force-on | media-keepalive [interval] }

no nat

default nat

## Syntax Description

media-keepalive

Specifies media keepalive to subscriber if it's located behind NAT.

interval

Specifies keepalive interval configured in seconds. Range is 1—50. Default is 10.

### Command Default

If no value is specified, default interval value is set to 10.

### Command Modes

Voice class tenant configuration (config-class)

Voice service SIP configuration (conf-serv-sip)

## Command History

Cisco IOS XE 17.13.1a

Cisco IOS XE Dublin 17.12.2

This command was introduced.

## Examples

The following example shows how to configure media keepalive at global level:

```
Device(config)# voice service voip Device(config-voi-serv)# sip Device(config-serv-sip)# nat media-keepalive 20
```

## Examples

The following example shows how to configure media keepalive at tenant level:

```
Device(config)# voice class tenant 1 Device(config-class)# nat media-keepalive 35
```

## nat symmetric check-media-src

To enable the gateway, to check the media source of incoming Real-time Transport Protocol (RTP) packets in symmetric Network
                              Address Translation (NAT) environments, use the nat symmetric check-media-src command in SIP user agent configuration mode. To disable media source checking, use the no form of this command.

nat symmetric check-media-src

no nat symmetric check-media-src

### Syntax Description

This command has no arguments or keywords.

### Command Default

Media source checking is disabled.

### Command Modes

SIP user agent configuration (sip-ua)

## Command History

Release

Modification

12.2(13)T

This command was introduced.

### Usage Guidelines

This command provides the ability to enable or disable symmetric NAT settings for the Session Initiation Protocol (SIP) user
                              agent. Use the nat symmetric check-media-src command to configure the gateway to check the media source address and port of the first incoming RTP packet. Checking for media packets is automatically enabled if the gateway receives the direction role "active or both".

## Examples

The following example enables checking the media source:

```
Router(config)# sip-ua Router(config-sip-ua)# nat symmetric check-media-src
```

### Related Commands

Command

Description

nat symmetric role

Defines endpoint settings to initiate or accept a connection for symmetric.

## nat symmetric role

To define endpoint settings to initiate or accept a connection for symmetric Network Address Translation (NAT) configuration,
                              use the nat symmetric role command in SIP user agent configuration mode. To disable the nat symmetric role configuration, use the no form of this command.

nat symmetric role { active | passive }

no nat symmetric role { active | passive }

### Syntax Description

active

Sets the symmetric NAT endpoint role to active, originating an outgoing connection.

passive

Sets the symmetric NAT endpoint role to passive, accepting an incoming connection to the port number on the m=line of the
                                          Session Description Protocol (SDP) body sent from the SDP body to the other endpoint.

### Command Default

The endpoint settings to initiate or accept connections for NAT configuration are not defined..

### Command Modes

SIP user agent configuration (sip-ua)

## Command History

Release

Modification

12.2(13)T

This command was introduced.

### Usage Guidelines

This command provides the ability to specify symmetric NAT endpoint settings for the SIP user agent. If the gateway does not receive the direction role, use the nat symmetric role command to define endpoint settings to initiate or accept a connection for symmetric NAT configuration. This is achieved by setting the symmetric NAT endpoint role to active or passive , respectively. Cisco recommends that you use the nat symmetric role command under the following conditions:

Endpoints are aware of their presence inside or outside of NAT

Endpoints parse and process direction:<role> in SDP

If the endpoints conditions are not satisfied, you may not achieve the desired results when you configure the nat symmetric role command.

## Examples

The following example shows how to set the endpoint role in connection setup to active:

```
Router(config)# sip-ua Router(config-sip-ua)# nat symmetric role active
```

### Related Commands

Command

Description

nat symmetric check-media-src

Enables source media checking for symmetric NAT.

## neighbor (annex g)

To configure the neighboring border elements (BEs) that interact with
                              		  the local BE for the purpose of obtaining addressing information and aiding in
                              		  address resolution, enter the neighbor command in Annex G configuration mode. To reset the default
                              		  value, use the no form of this command.

neighbor ip-address

no neighbor

### Syntax Description

ip - address

IP address of the neighbor that is used for exchanging
                                          						Annex G messages.

### Command Default

No default behavior or values

### Command Modes

Annex G configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release
                                          						12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is not
                                          						included in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release
                                          						12.2(11)T. This command is supported on the Cisco AS5300, Cisco AS5350, Cisco
                                          						AS5400, and Cisco AS5850 in this release.

## Examples

The following example configures a neighboring BE that has an IP
                              		  address and border element ID:

```
Router(config)# call-router h323-annexg be20 Router(config-annexg)# neighbor 121.90.10.42 Router(config-annexg-neigh)# id be30 Router(config-annexg-neigh)# exit
```

### Related Commands

Command

Description

advertise

Controls the types of descriptors that the BE advertises to
                                          						its neighbors.

call - router

Enables the Annex G border element configuration commands.

id

Configures the local ID for the neighboring BE.

port

Configures the port number of the neighbor that is used for
                                          						exchanging Annex G messages.

query - interval

Configures the interval at which the local BE will query
                                          						the neighboring BE.

## neighbor (tgrep)

To create a TGREP session with another device, use the neighbor command in TGREP configuration mode. To disable a TRIP connection,
                              use the no form of this command.

neighbor ip_address

no neighbor ip_address

### Syntax Description

ip_address

IP address of a peer device with which TGREP information will be exchanged.

### Command Default

No neighboring devices are defined

### Command Modes

TGREP configuration

## Command History

Release

Modification

12.3(1)

This command was introduced.

## Examples

The following example shows that the gateway with the IP address 192.116.56.10 is defined as a neighbor for ITAD 1234:

```
Router(config)# tgrep local-itad 1234 Router(config-tgrep)# neighbor 192.116.56.10
```

### Related Commands

Command

Description

tgrep local
                                          -
                                          itad

Enters TGREP configuration mode and defines an ITAD.

## network-clock base-rate

To configure the network clock base rate for universal I/O serial ports 0 and 1, use the network - clock base - rate command in global configuration mode. To disable the current network clock base rate, use the no form of this command.

network-clock base-rate { 56k | 64k }

no network-clock base-rate { 56k | 64k }

### Syntax Description

56k

Sets the network clock base rate to 56 kbps.

64k

Sets the network clock base rate to 64 kbps.

### Command Default

56 kbps

### Command Modes

Global configuration

## Command History

Release

Modification

11.3(1)MA

This command was introduced on the Cisco MC3810.

### Usage Guidelines

This command applies to Voice over Frame Relay and Voice over ATM.

## Examples

The following example sets the network clock base rate to 64 kbps:

```
network-clock base-rate 64k
```

### Related Commands

Command

Description

network - clock - select

Uses the network clock source to provide timing to the system backplane PCM bus.

network - clock - switch

Configures the switch delay time to the next priority network clock source when the current network clock source fails.

## network-clock-participate

To allow the ports on a specified network module or voice/WAN interface card (VWIC) to use the network clock for timing,
                              use the network - clock - participate command in global configuration mode. To restrict the device to use only its own clock signals, use the no form of this command.

network-clock-participate [ slot slot-number | wic wic-slot | aim aim-slot-number ]

no network-clock-participate [ nm slot | wic wic-slot ]

### Syntax Description

slot slot - number

(Optional) Network module slot number on the router chassis. Valid values are from 1 to 6.

wic wic - slot

Configures the WAN interface card (WIC) slot number on the router chassis. Valid values are 0 or 1.

aim aim - slot - number

Configures the Advanced Integration Module (AIM) in the specified slot. The aim-slot-number values are 0 or 1 for the Cisco
                                          3660 and 0 or 1 for the Cisco 3725, and Cisco 3745.

### Command Default

No network clocking is enabled, and interfaces are restricted to using the clocking generated on their own modules.

### Command Modes

Global configuration

## Command History

Release

Modification

12.1(5)XM

This command was introduced on the Cisco 3660.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(2)XB

The slot keyword was replaced by the nm keyword and the wic keyword and the wic-slot argument were added.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T.

12.2(15)T

This command was integrated into Cisco IOS Release 12.2(15)T with support for the Cisco 3660, Cisco 3725, and Cisco 3745.
                                          Clocks can be synchronized on two ports. The aim keyword was added. The nm keyword was replaced by the slot keyword.

12.4(15)T9

This command was integrated into Cisco IOS Release 12.4(15)T9, and support was added for the NM-CEM-4SER modules.

### Usage Guidelines

This command is used for ATM segmentation and reassembly or digital signal processing and Cisco 3660, Cisco 3725, and Cisco
                              3745 routers.

This command applies to any network module with T1/E1 controllers to provide clocks from a central source (MIX module for
                              the Cisco 3660) to the network module and to the port on the network module. Then that port can be selected as the clock source
                              with the network-clock-select command to supply clock to other ports or network modules that choose to participate in network clocking with the network-clock-participate command. This command synchronizes the clocks for two ports.

On the Cisco 3700 series, you must use the network-clock-participate command and either the wic wic-slot keyword and argument or the slot slot - number keyword and argument.

If the AIM takes its clock signals from a T1 or E1 controller, it is mandatory to use the network-clock-select and network-clock-participate commands for ATM. The clocks for the ATM and voice interfaces do not need to be synchronous, but improved voice quality may
                                          result if they are.

The only VWICs that can participate in network clocking are digital T1/E1 packet voice trunk network modules (NM-HDV), and
                                          Fast Ethernet network modules (NM-2W, NM-1FE. and NM-2FE).

Beginning with Cisco IOS Release 12.4(15)T9, the network-clock-participate command can also be used for the NM-CEM-4SER modules. When the network-clock-participate command is configured, the clock is derived from the backplane. When the no network-clock-participate command is configured, the local oscillator clock is used.

## Examples

The following example configures the network module in slot 5 to participate in network clocking on a Cisco 3660 with a MIX
                              module:

```
network-clock-participate slot 5
network-clock-select 1 e1
```

The following example on a Cisco 3700 series router specifies that the AIM participates in network clocking and selects port
                              E1 0/1 to provide the clock signals.

```
Router(config)# network-clock-participate wic 0 Router(config)# network-clock-participate aim 0 Router(config)# network-clock-select 2 E1 0/1
```

The following example on a Cisco 3660 specifies the slot number that participates in network clocking and selects port E1
                              5/0:

```
Router(config)# network-clock-participate slot 5 Router(config)# network-clock-select 1 E1 5/0
```

### Related Commands

Command

Description

network-clock-select

Specifies selection priority for the clock sources.

network-clock-source

Selects the port to be the clock source to supply clock resources to other ports or network modules.

## network-clock select

To name a source to provide timing for the network clock and to specify the selection priority for this clock source, use
                              the network - clock select command in global configuration mode. To cancel the network clock selection, use the no form of this command.

### Cisco ASR 1000 Series

network-clock select { priority [ bits [ R0 | R1 ] { e1 [ crc4 | no-crc4 | unframed ] | t1 [ esf | sf | unframed ]} | controller type number | global | interface type number | local | system ] | option { 1 | 2 }}

no network-clock select priority [ global | local ]

### Cisco 7600 Series and Cisco 10000 Series

network-clock select priority { controller type number | interface type number | slot number | system } [ global | local ]

no network-clock select priority [ global | local ]

### Syntax Description

priority

Selection priority for the clock source (1 is the highest priority). The range is 1 to 6.

The clock with the highest priority is selected to drive the system time division multiplexing (TDM) clocks. When the higher-priority
                                          clock source fails, the next-higher-priority clock source is selected.

bits

(Optional) Derives network timing from the central office (CO) Building Integrated Timing Supply (BITS) clock.

R0

(Optional) Specifies Route Processor 0 BITS as the source slot.

R1

(Optional) Specifies Route Processor 1 BITS as the source slot.

e1

(Optional) Configures the BITS interface to use an E1 connection.

crc4

(Optional) Configures the E1 BITS interface framing with Cyclic Redundancy Check 4 (CRC4).

no-crc4

(Optional) Configures the E1 BITS interface framing with no CRC4.

unframed

(Optional) Configures the BITS interface with clear channel.

t1

(Optional) Configures the BITS interface to use a T1 connection.

esf

(Optional) Configures the T1 BITS interface with the Extended Super Frame (ESF) framing standard.

sf

(Optional) Configures the T1 BITS interface with the Super Frame (SF) framing standard.

controller type number

Specifies the controller to be the clock source.

interface type number

Specifies the interface to be the clock source.

slot number

Specifies the slot to be the clock source. The range is 1 to 6.

global

(Optional) Configures the source as global.

local

(Optional) Configures the source as local.

system

Specifies the system clock as the clock source.

option

Specifies the standards for the network option. The applicable values are as follows:

- 1—Network option I is the ITU G-813 standard.

- 2—Network option II (Gen1) is the Bellcore GR-1244/GR-253 (stratum 3) and ITU G-813 standard. This is the default value.

### Command Default

The router uses the system clock (also called free-running mode).

### Command Modes

Global configuration (config)

## Command History

Release

Modification

11.3 MA

This command was introduced on the Cisco MC3810.

12.0(3)XG

The BVM as a possible network clock source was added.

12.1(5)XM

This command was implemented on the Cisco 3660. The keywords t1 and e1 were introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(2)XB

This command was implemented on the Cisco 2600 series and Cisco 3660 with AIMs installed.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T.

12.2(15)T

This command was implemented on the Cisco 2600XM, Cisco 2691, Cisco 3725, and Cisco 3745.

12.3(8)T4

This command was integrated into Cisco IOS Release 12.3(8)T4 and the bri keyword was added. Support was also added for the Cisco 2800 series.

12.3(11)T

This command was integrated into Cisco IOS Release 12.3(11)T and the atm keyword was added. Support was also added for the Cisco 3800 series.

Cisco IOS XE Release 2.1

This command was introduced in a release earlier than Cisco IOS Release 2.1.

15.0(1)S

This command was integrated into a release earlier than Cisco IOS Release 15.0(1)S.

Cisco IOS XE Release 3.1

This command was modified. This command was implemented on the Cisco ASR 1000 platform. The option keyword was added.

### Usage Guidelines

When an active clock source fails, the system chooses the next-lower-priority clock source that is specified by this command.
                                 When a higher-priority clock source becomes available, the system automatically reselects it.

You can specify up to five clock priorities. The highest-priority active interface in the router supplies the primary reference
                              source to all other interfaces that require network clock synchronization services.

For timing sources, the Route Processor can receive timing information through its BITS interface or through a TDM-based
                              Shared Port Adapter (SPA). For some telecommunications deployments, BITS clocking is required to provide global clocking synchronization
                              of network equipment in the end-to-end data path. A BITS clock can be supplied to the network clock module using a T1 or E1
                              connection.

If a controller is specified in the clock source hierarchy, you must configure that controller for line timing (by using
                              the appropriate clock source line command for the controller). Any controller that is not currently acting as the clock source will automatically operate in
                              loop timing mode. Both controllers can be given different clock source priority values. For more information, see the Cisco IOS Interface and Hardware Component Command Reference .

Use the show network-clocks command to display clock priorities that are configured on the router.

## Examples

The following example shows how to configure the network clock as revertive and assign clock sources to two priorities:

```
Router> enable Router# configure terminal Router(config)# network-clock revertive Router(config)# network-clock select 1 bits R0 e1 Router(config)# network-clock select 2 interface GigabitEthernet 0/0/1
```

The following example shows how to configure the network option for network clock.

Router(config)# network-clock select option 1

### Related Commands

Command

Description

network-clock-participate

Configures a network module to participate in network clocking.

network-clock-switch

Configures the switch delay time to the next-priority network clock source when the current network clock source fails or
                                          a higher-priority clock source is up and available.

show network-clocks

Displays the network clock configuration and current primary clock source.

## network-clock-switch

To configure the switch delay time to the next priority network clock source when the current network clock source fails,
                              use the network - clock - switch command in global configuration mode. To cancel the network clock delay time selection, use the no form of this command.

network-clock-switch [ switch-delay | never ] [ restore-delay | never ]

no network-clock-switch

### Syntax Description

switch - delay

(Optional) Delay time, in seconds, before the next-priority network clock source is used when the current network clock source
                                          fails. Range is from 0 to 99. Default is 10.

never

(Optional) No delay time before the current network clock source recovers.

restore - delay

(Optional) Delay time, in seconds, before the current network clock source recovers. Range is from 0 to 99.

never

(Optional) No delay time before the next-priority network clock source is used when the current network clock source fails.

### Command Default

10 seconds

### Command Modes

Global configuration

## Command History

Release

Modification

11.3(1)MA

This command was introduced on the Cisco MC3810.

### Usage Guidelines

This command applies to Voice over Frame Relay and Voice over ATM.

## Examples

The following example switches the network clock source after 20 seconds and sets the delay time before the current network
                              clock source recovers to 20 seconds:

```
network-clock-switch 20 20
```

### Related Commands

Command

Description

network - clock - select

Uses the network clock source to provide timing to the system backplane PCM bus.

## noisefloor

To configure the noise level, in dBm, above which noise reduction (NR) will operate, use the noisefloor command in media profile configuration mode. To disable the configuration, use the no form of this command.

noisefloor level

no noisefloor level

### Syntax Description

level

Minimum noise level in dBm. The range is from -58 to -20.

### Command Default

The default value is -48 dBm.

### Command Modes

Media profile configuration (cfg-mediaprofile)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

15.2(3)T

This command was modified. Support for the Cisco Unified Border Element (Cisco UBE) was added.

### Usage Guidelines

Use the noisefloor command to configure the noise level, in dBm, above which noise reduction (NR) will operate. NR will allow noises quieter
                              than this level to pass without processing. You must create a media profile for noise reduction and then configure the noise
                              level. Signal levels start at 0 dBm (extremely loud) and quieter levels are more negative. The default value of -48 dBm is
                              very quiet.

## Examples

The following example shows how to create a media profile to configure noise reduction parameters:

```
Device> enable Device# configure terminal Device(config)# media profile nr 200 Device(cfg-mediaprofile)# noisefloor -50 Device(cfg-mediaprofile)# end
```

### Related Commands

Command

Description

intensity

The intensity or depth of the noise reduction process.

media profile nr

Creates a media profile to configure noise reduction parameters.

## non-linear

To enable nonlinear processing (NLP) in the echo canceller and set its threshold or comfort-noise attenuation, use the non - linear command in voice-port configuration mode. To disable nonlinear processing, use the no form of this command.

non-linear [ comfort-noise attenuation { 0db | 3db | 6db | 9db } | threshold dB ]

no non-linear [ comfort-noise attenuation | threshold ]

### Syntax Description

0db | 3db | 6db | 9db

(Optional) Attenuation level of the comfort noise in dB. Default is 0db , which means that comfort noise is not attenuated.

threshold dB

(Optional) Sets the threshold in dB. Range is -15 to -45. Default is -21.

This keyword is not supported when using the extended G.168 echo canceller.

### Command Default

NLP is enabled; comfort-noise attenuation is disabled; threshold is -21 dB.

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced.

12.2(11)T

The threshold keyword was added.

12.2(13)T

This command was implemented on routers that support the extended G.168 echo canceller.

12.3(6)

The comfort-noise keyword was added.

12.4

The default setting for comfort-noise attenuation was changed from 0db to 6db.

### Usage Guidelines

This command enables functionality that is also generally known as residual echo suppression. Use this command to shut off
                              any signal if no near-end speech is detected. Enabling this command normally improves performance, although some users might
                              perceive truncation of consonants at the end of sentences when this command is enabled.

Use the comfort-noise keyword if the comfort noise generated by the NLP sounds like hissing. Using this keyword makes the hissing sound less audible.
                              The default setting for comfort-noise attenuation is 6db to achieve the highest satisfaction in voice quality.

The echo - cancel enable command must be enabled for this command to take effect.

## Examples

The following example enables nonlinear call processing on a Cisco 3600 series router:

```
voice-port 1/0/0
 non-linear
```

The following example sets the attenuation level to 9 dB on a Cisco 3600 series router:

```
voice-port 1/0/0
 non-linear comfort-noise attenuation 9db
```

### Related Commands

Command

Description

echo - cancel enable

Enables echo cancellation for voice that is sent and received on the same interface.

## notify (MGCP profile)

To specify the order in which automatic number identification (ANI) and dialed number identification service (DNIS) digits
                              are reported to the Media Gateway Control Protocol (MGCP) call agent, use the notify command in MGCP profile configuration mode. To revert to the default, use the no form of this command.

notify { ani-dnis | dnis-ani }

no notify { ani-dnis | dnis-ani }

### Syntax Description

ani-dnis

ANI digits are sent in the first notify message, followed by DNIS. This is the default.

dnis-ani

DNIS digits are sent in the first notify message, followed by ANI.

### Command Default

The default order is ANI first and DNIS second.

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.4(4)T

This command was introduced.

### Usage Guidelines

This command controls the order of ANI and DNIS when using the Feature Group D (FGD) Exchange Access North American (EANA)
                              protocol on a T1 interface. Selecting the ani-dnis keyword causes the ANI digits to be sent in the first NTFY message to the MGCP call agent and the DNIS digits to be sent
                              in a second NTFY message. Selecting the dnis-ani keyword causes the DNIS digits to be sent in the first NTFY message to the MGCP call agent and the ANI digits to be sent
                              in a second NTFY message.

## Examples

The following example sets the digit order to DNIS first and ANI second for the default MGCP profile:

```
Router(config)# mgcp profile default Router(config-mgcp-profile)# notify dnis-ani
```

### Related Commands

Command

Description

mgcp package-capability

Specifies an MGCP package capability type for a media gateway.

mgcp profile

Defines an MGCP profile to be associated with one or more MGCP endpoints

show mgcp

Displays MGCP configuration information.

show mgcp profile

Displays information for MGCP profiles.

## notify redirect

To enable application handling of redirect requests for all VoIP dial peers on a Cisco IOS voice gateway, use the notify redirect command in voice service VoIP configuration mode. To disable application handling of redirect requests on the gateway, use
                              the no form of this command. To return the gateway to the default notify redirect command settings, use the default form of this command.

notify redirect { ip2ip | ip2pots }

no notify redirect { ip2ip | ip2pots }

default notify redirect { ip2ip | ip2pots }

### Syntax Description

ip2ip

Enables notify redirection for IP-to-IP calls.

ip2pots

Enables notify redirection for IP-to-IP calls for IP-to-POTS calls.

### Command Default

Notify redirection for IP-to-IP calls is enabled.

Notify redirection for IP-to-POTS calls is disabled.

Notify redirection for Session Initiation Protocol (SIP) phones registered to Cisco Unified Communications Manager Express
                              (Cisco Unified CME) is enabled.

### Command Modes

Voice service VoIP configuration (conf-voi-serv)

## Command History

Release

Modification

12.4(4)T

This command was introduced.

15.1(1)T

This command was integrated into Cisco IOS Release 15.1(1)T. The following default behavior was added: Notify redirection
                                          for SIP phones registered to Cisco Unified CME is enabled.

Cisco IOS XE Cupertino 17.7.1a

Introduced support for YANG models.

### Usage Guidelines

Use this command to enable notify redirection globally on a gateway. Use the notify redirect command in dial peer voice configuration mode to configure notify redirection settings for IP-to-IPand IP-to-POTS calls on
                              a specific inbound dial peer on a gateway.

This command is supported on Cisco Unified Communications Manager Express (Cisco Unified CME), release 3.4 and later releases
                                          and on Cisco Unified Session Initiation Protocol (SIP) Survivable Remote Site Telephony (SRST) release 3.4 and later releases.
                                          However, to use the notify redirect command in voice service VoIP configuration mode on compatible Cisco Unified SIP SRST devices, you must first use the allow-connections command to enable the corresponding call flows on the SRST gateway.

## Examples

The following is partial sample output from the show running-config command showing that notify redirection has been set up globally for both IP-to-IP and IP-to-POTS calling (because support
                              of IP-to-IP calls is enabled by default, the ip2ip setting does not appear in the output).

```
voice service voip 
 notify redirect ip2pots
 allow-connections h323 to h323
 allow-connections h323 to sip
 allow-connections sip to sip
 no supplementary-service h450.2
 no supplementary-service h450.3
 sip
 registrar server expires max 600 min 60
```

### Related Commands

Command

Description

allow-connections

Allows connections between specific endpoint types in a VoIP network.

notify redirect (dial peer)

Enables application handling of redirect requests on a specific VoIP dial peer on a Cisco IOS voice gateway.

## notify redirect (dial peer)

To enable application handling of redirect requests on a specific VoIP dial peer on a Cisco IOS voice gateway, use the notify redirect command in dial peer voice configuration mode. To disable notify redirection on the gateway, use the no form of this command. To return the gateway to the default notify redirection settings, use the default form of this command.

notify redirect { ip2ip | ip2pots }

no notify redirect { ip2ip | ip2pots }

default notify redirect { ip2ip | ip2pots }

### Syntax Description

ip2ip

Specifies that the notify redirect command is applied to IP-to-IP calls.

ip2pots

Specifies that the notify redirect command is applied to IP-to-POTS calls.

### Command Default

Notify redirection for IP-to-IP is enabled.
                              Notify redirection for IP-to-POTS is disabled.

Notify redirection for Session Initiation Protocol (SIP) phones registered to Cisco Unified Communications Manager Express
                              (Cisco Unified CME) is enabled.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.4(4)T

This command was introduced.

15.1(1)T

This command was integrated into Cisco IOS Release 15.1(1)T. The following default behavior was added: Notify redirection
                                          for SIP phones registered to Cisco Unified CME is enabled.

### Usage Guidelines

Use this command in dial peer configuration mode to configure IP-to-IP and IP-to-POTS calls on an inbound dial peer on a Cisco
                              IOS voice gateway. This command configures notify redirection settings on a per-dial-peer basis.

When notify redirect is enabled in dial peer voice configuration mode, the configuration for the specific dial peer is activated
                              only if the dial peer is an inbound dial peer. To enable notify redirect globally on a Cisco IOS voice gateway, use the notify redirect command in voice service VoIP configuration mode.

This command is supported on Cisco Unified Communications Manager Express (Cisco Unified CME), release 3.4 and later releases
                                          and Cisco Unified Session Initiation Protocol (SIP) Survivable Remote Site Telephony (SRST) release 3.4 and later releases.
                                          However, to use the notify redirect command in voice service VoIP configuration mode on compatible Cisco Unified SIP SRST devices, you must first use the allow-connections command to enable the corresponding call flows on the SRST gateway.

## Examples

The following is partial sample output from the show running-config command showing that notify redirection is enabled for both IP-to-IP and IP-to-POTS calls on VoIP dial peer 8000 (because
                              support of IP-to-IP calls is enabled by default, the ip2ip setting does not appear in the output):

```
dial-peer voice 8000 voip
 destination-pattern 80..
 notify redirect ip2pots
 session protocol sipv2
 session target ipv4:209.165.201.15
 dtmf-relay rtp-nte
 codec g711ulaw
!
```

### Related Commands

Command

Description

allow-connections

Allows connections between specific endpoint types in a VoIP network.

notify redirect

Enables application handling of redirect requests for all VoIP dial peers on a Cisco IOS voice gateway.

## notify
                        	 telephone-event

To configure the
                              		  maximum interval between two consecutive NOTIFY messages for a particular
                              		  telephone event, use the notify telephone-event command in SIP UA configuration
                              		  mode or voice class tenant configuration mode. To reset the interval to the
                              		  default value, use the no form of this
                              		  command.

notify telephone-event max-duration milliseconds [system]

no notify telephone-event

### Syntax Description

max-duration milliseconds

Time
                                          						interval between consecutive NOTIFY messages for a single DTMF event, in
                                          						milliseconds. Range is from 40 to 3000. Default is 2000.

system

Specifies that the NOTIFY messages for a particular telephone
                                          						event use the global sip-ua value. This keyword is available only for the
                                          						tenant mode to allow it to fallback to the global configurations

### Command Default

2000 milliseconds

### Command Modes

SIP UA configuration (config-sip-ua)

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.2(15)ZJ

This
                                          						command was introduced.

12.3(4)T

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

15.0(1)M

This
                                          						command was modified. The acceptable value range for the milliseconds argument was expanded (the lower end of the range was changed from 500 to 40).

12.4(24)T3

This
                                          						command was modified. The acceptable value range for the milliseconds argument was expanded (the lower end of the range was changed from 500 to 40).

15.6(2)T and IOS XE Denali 16.3.1

This command was modified to include the keyword: system .

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

The notify telephone-event command works with the dtmf-relay sip-notify command. The dtmf-relay sip-notify command forwards out-of-band DTMF
                              		  tones by using SIP NOTIFY messages. The notify telephone-event command sets the maximum time
                              		  interval between consecutive NOTIFY messages for a single DTMF event. The
                              		  maximum time is negotiated between two SIP endpoints and the lowest duration
                              		  value is the one selected. This duration is negotiated during call
                              		  establishment as part of negotiating the SIP-NOTIFY DTMF relay.

The originating
                              		  gateway sends an indication of DTMF relay in an Invite message using the SIP
                              		  Call-Info header. The terminating gateway acknowledges the message with an
                              		  18x/200 Response message, also using the Call-Info header. The set duration
                              		  appears in the Call-Info header in the following way:

```
Call-Info: <sip: address>; method="Notify;Event=telephone-event;Duration=msec"
```

For example, if the
                              		  maximum duration of gateway A is set to 1000 ms, and gateway B is set to 700
                              		  ms, the resulting negotiated duration would be 700 ms. Both A and B would use
                              		  the value 700 in all of their NOTIFY messages for DTMF events.

## Examples

The following
                              		  example sets the maximum duration for a DTMF event to 40 ms.

```
Router(config)# sip-ua Router(config-sip-ua)# notify telephone-event max-duration 40
```

The following
                              		  example sets the maximum duration for a DTMF event in the voice class tenant
                              		  configuration mode:

```
Router(config-class)# notify telephone-event max-duration system
```

### Related Commands

Command

Description

dtmf-relay sip-notify

Forwards DTMF tones using SIP NOTIFY messages.

## notify ignore substate

To ignore the Subscription-State header, use the notify ignore substae command in SIP UA configuration mode or voice class tenant configuration mode. To reset the interval to the default value,
                              use the no form of this command.

notify ignore substate

no notify ignore substate

### Command Modes

SIP UA configuration (config-sip-ua)

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.2(15)ZJ

This command was introduced.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

## Examples

The following is an example:

```
Router(config)# sip-ua Router(config-sip-ua)# notify ignore substate
```

## nsap

To specify the network service access point (NSAP) address for a local video dial peer, use the nsap command in dial-peer configuration mode. To remove any configured NSAP address from the dial peer, use the no form of this command.

nsap nsap-address

no nsap

### Syntax Description

nsap - address

A 40-digit hexadecimal number; the number must be unique on the device.

### Command Default

No NSAP address for a video dial peer is configured

### Command Modes

Dial-peer configuration

## Command History

Release

Modification

12.0(5)XK

This command was introduced for ATM video dial-peer configuration on the Cisco MC3810.

12.0(7)T

This command was integrated into Cisco IOS Release 12.0(9)T.

### Usage Guidelines

The address must be unique on the router.

## Examples

The following example sets up an NSAP address for the local video dial peer designated as 10:

```
dial-peer video 10 videocodec
 nsap 47.0091810000000002F26D4901.333333333332.02
```

### Related Commands

Command

Description

dial - peer video

Defines a video ATM dial peer for a local or remote video codec, specifies video-related encapsulation, and enters dial-peer
                                          configuration mode.

show dial - peer video

Displays dial-peer configuration.

## null-called-number

To substitute a user-defined number as the called number IE when an incoming H.323 setup message does not contain a called
                              number IE, use the null-called-number command in voice service H.323 configuration mode. To disable the addition of the number used as the called number IE, use
                              the no form of this command.

null-called-number override string

no null-called-number

### Syntax Description

override string

Specifies the user-defined series of digits for the E.164 or private dialing plan telephone number when the called number
                                          IE is missing from the H.323 setup message. Valid entries are the digits 0 through 9.

### Command Default

The command behavior is disabled. H.323 setup messages missing the called number IE are disconnected.

### Command Modes

Voice service h323 configuration (conf-serv-h323)

## Command History

Release

Modification

12.4(22)YB

This command was introduced.

15.0(1)M

This command was integrated into Cisco IOS Release 15.0(1)M.

### Usage Guidelines

For a call connection to be completed the incoming H.323 setup messages must include the called number IE and the E.164 destination
                              address. Calls lacking called number IE are disconnected. The null-called-number is a user-defined number used when the called
                              number IE is missing to complete the call.

## Examples

The following example shows the number 4567 configured as the user-defined number used to complete a call when the H.323 setup
                              message is missing the called number IE:

```
Router(conf-serv-h323)# null-called-number override 4567
```

## numbering-type

To match on a number type for a dial-peer call leg, use the numbering - type command in dial-peer configuration mode. To remove the numbering type for a dial-peer call leg, use the no form of this command.

numbering-type { international | abbreviated | national | network | reserved | subscriber | unknown }

no numbering-type { international | abbreviated | national | network | reserved | subscriber | unknown }

### Syntax Description

international

International numbering type.

abbreviated

Abbreviated numbering type.

national

National numbering type.

network

Network numbering type.

reserved

Reserved numbering type.

subscriber

Subscriber numbering type.

unknown

Numbering type unknown.

### Command Default

No default behaviors or values

### Command Modes

Dial-peer configuration

## Command History

Release

Modification

12.0(7)XR1

This command was introduced on the Cisco AS5300.

12.0(7)XK

This command was implemented as follows:

VoIP: Cisco 2600 series, Cisco 3600 series, Cisco MC3810

VoFR: Cisco 2600 series, Cisco 3600 series, Cisco MC3810

VoATM: Cisco 3600 series, Cisco MC3810

12.1(1)T

This command was integrated into Cisco IOS Release 12.1(1)T and implemented as follows:

VoIP: Cisco 1750, Cisco 2600 series, Cisco 3600 series, Cisco AS5300, Cisco 7200 series, Cisco 7500 series

12.1(2)T

This command was implemented as follows:

VoIP: Cisco MC3810

VoFR: Cisco 2600 series, Cisco 3600 series, Cisco MC3810

VoATM: Cisco 3600 series, Cisco MC3810

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

### Usage Guidelines

This command is supported for POTS, VoIP, VoFR, and VoATM dial peers. The numbering type options are implemented as defined by
                              the ITU Q.931 specification.

## Examples

The following example shows how to configure a POTS dial peer for network usage:

```
dial-peer voice 100 pots
 numbering-type network
```

The following example shows how to configure a VoIP dial peer for subscriber usage:

```
dial-peer voice 200 voip
 numbering-type subscriber
```

### Related Commands

Command

Description

rule

Applies a translation rule to a calling party number or a called party number for both incoming and outgoing calls.

show translation - rule

Displays the contents of all the rules that have been configured for a specific translation name.

test translation - rule

Tests the execution of the translation rules on a specific name-tag.

translate

Applies a translation rule to a calling party number or a called party number for incoming calls.

translate - outgoing

Applies a translation rule to a calling party number or a called party number for outgoing calls.

translation - rule

Creates a translation name and enters translation-rule configuration mode.

voip - incoming translation - rule

Captures calls that originate from H.323-compatible clients.

## num-exp

To define how to expand a telephone extension number into a particular destination pattern, use the num - exp command in global configuration mode. To remove the configured number expansion, use the no form of this command.

num-exp extension-number expanded-number

no num-exp extension-number

### Syntax Description

extension - number

One or more digits that define an extension number for a particular dial peer.

expanded - number

One or more digits that define the expanded telephone number or destination pattern for the extension number listed.

### Command Default

No number expansion is defined.

### Command Modes

Global configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 3600 series.

12.0(3)T

This command was implemented on the Cisco AS5300.

12.0(4)XL

This command was implemented on the Cisco AS5800.

12.0(7)T

This command was integrated into Cisco IOS Release 12.0(7)T.

12.0(7)XK

This command was implemented on the Cisco MC3810.

12.1(2)T

This command was modified. It was integrated into Cisco IOS Release 12.1(2)T.

Introduced support for YANG models.

### Usage Guidelines

Use this
                              command to
                              define how to expand a particular set of numbers (for example, a telephone extension number) into a particular destination
                              pattern. With this command, you can bind specific extensions and expanded numbers together by explicitly defining each number,
                              or you can define extensions and expanded numbers using variables. You can also use this command to convert seven-digit numbers
                              to numbers containing fewer than seven digits.

You can configure a maximum of 250 number extensions before the router sends an error message stating that the limit has been
                              reached.

Use a period (.) as a variable or wildcard, representing a single number. Use a separate period for each number that you want
                              to represent with a wildcard--for example, if you want to replace four numbers in an extension with wildcards, type in four
                              periods.

Translation of a number in +E.164 format is not supported if you use the CLI command num-exp , although the plus symbol (+) is displayed as a configurable option for the command. As a workaround, it is recommended that
                              you use translation rule to support the +E.164 dial pattern that contains the plus (+) symbol. For a sample of the configuration,
                              see Example .

## Examples

```
router(config)#show num-exp
Dest Digit Pattern = '1001'     Translation =
                                '+4001'
router(config)#num-exp 1001 ?
  WORD  Substitution Pattern to Translate Dialed Pat
        to E.164
```

The following example expands the extension number 50145 to the number 14085550145:

```
num-exp 50145 14085550145
```

The following example expands all five-digit extensions beginning with 5 such that the 5 is replaced with the digits 1408555
                              at the beginning of the extension number:

```
num-exp 5.... 1408555....
```

### Related Commands

Command

Description

dial - peer terminator

Designates a special character to be used as a terminator for variable length dialed numbers.

forward - digits

Specifies which digits to forward for voice calls.

prefix

Specifies a prefix for a dial peer.

| class-name | Name that describes the specific COR. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced. |

| Command | Description |
|---|---|
| dial-peer cor custom | Specifies that named CORs apply to dial peers. |
| name | Assigns a name to the internal adapter. |

| auto | Sets the symmetric NAT endpoint role to auto. Autodetect subscriber in a remote subnet when located behind a NAT. |
|---|---|
| force-on | Sets the symmetric NAT endpoint role to force-on. Assume that all remote subscribers are behind the NAT device. |

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced. |
| Cisco IOS XE Dublin
                                             17.10.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| nat symmetric check-media-src | Enables source media checking for symmetric NAT. |

| media-keepalive | Specifies media keepalive to subscriber if it's located behind NAT. |
|---|---|
| interval | Specifies keepalive interval configured in seconds. Range is 1—50. Default is 10. |

| Release | Modification |
|---|---|
| Cisco IOS XE 17.13.1a Cisco IOS XE Dublin 17.12.2 | This command was introduced. |

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced. |

| Command | Description |
|---|---|
| nat symmetric role | Defines endpoint settings to initiate or accept a connection for symmetric. |

| active | Sets the symmetric NAT endpoint role to active, originating an outgoing connection. |
|---|---|
| passive | Sets the symmetric NAT endpoint role to passive, accepting an incoming connection to the port number on the m=line of the
                                          Session Description Protocol (SDP) body sent from the SDP body to the other endpoint. |

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced. |

| Command | Description |
|---|---|
| nat symmetric check-media-src | Enables source media checking for symmetric NAT. |

| ip - address | IP address of the neighbor that is used for exchanging
                                          						Annex G messages. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release
                                          						12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is not
                                          						included in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release
                                          						12.2(11)T. This command is supported on the Cisco AS5300, Cisco AS5350, Cisco
                                          						AS5400, and Cisco AS5850 in this release. |

| Command | Description |
|---|---|
| advertise | Controls the types of descriptors that the BE advertises to
                                          						its neighbors. |
| call - router | Enables the Annex G border element configuration commands. |
| id | Configures the local ID for the neighboring BE. |
| port | Configures the port number of the neighbor that is used for
                                          						exchanging Annex G messages. |
| query - interval | Configures the interval at which the local BE will query
                                          						the neighboring BE. |

| ip_address | IP address of a peer device with which TGREP information will be exchanged. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| tgrep local
                                          -
                                          itad | Enters TGREP configuration mode and defines an ITAD. |

| 56k | Sets the network clock base rate to 56 kbps. |
|---|---|
| 64k | Sets the network clock base rate to 64 kbps. |

| Release | Modification |
|---|---|
| 11.3(1)MA | This command was introduced on the Cisco MC3810. |

| Command | Description |
|---|---|
| network - clock - select | Uses the network clock source to provide timing to the system backplane PCM bus. |
| network - clock - switch | Configures the switch delay time to the next priority network clock source when the current network clock source fails. |

| slot slot - number | (Optional) Network module slot number on the router chassis. Valid values are from 1 to 6. |
|---|---|
| wic wic - slot | Configures the WAN interface card (WIC) slot number on the router chassis. Valid values are 0 or 1. |
| aim aim - slot - number | Configures the Advanced Integration Module (AIM) in the specified slot. The aim-slot-number values are 0 or 1 for the Cisco
                                          3660 and 0 or 1 for the Cisco 3725, and Cisco 3745. |

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced on the Cisco 3660. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(2)XB | The slot keyword was replaced by the nm keyword and the wic keyword and the wic-slot argument were added. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T. |
| 12.2(15)T | This command was integrated into Cisco IOS Release 12.2(15)T with support for the Cisco 3660, Cisco 3725, and Cisco 3745.
                                          Clocks can be synchronized on two ports. The aim keyword was added. The nm keyword was replaced by the slot keyword. |
| 12.4(15)T9 | This command was integrated into Cisco IOS Release 12.4(15)T9, and support was added for the NM-CEM-4SER modules. |

| Note | If the AIM takes its clock signals from a T1 or E1 controller, it is mandatory to use the network-clock-select and network-clock-participate commands for ATM. The clocks for the ATM and voice interfaces do not need to be synchronous, but improved voice quality may
                                          result if they are. |
|---|---|

| Note | The only VWICs that can participate in network clocking are digital T1/E1 packet voice trunk network modules (NM-HDV), and
                                          Fast Ethernet network modules (NM-2W, NM-1FE. and NM-2FE). |
|---|---|

| Note | Beginning with Cisco IOS Release 12.4(15)T9, the network-clock-participate command can also be used for the NM-CEM-4SER modules. When the network-clock-participate command is configured, the clock is derived from the backplane. When the no network-clock-participate command is configured, the local oscillator clock is used. |
|---|---|

| Command | Description |
|---|---|
| network-clock-select | Specifies selection priority for the clock sources. |
| network-clock-source | Selects the port to be the clock source to supply clock resources to other ports or network modules. |

| priority | Selection priority for the clock source (1 is the highest priority). The range is 1 to 6. The clock with the highest priority is selected to drive the system time division multiplexing (TDM) clocks. When the higher-priority
                                          clock source fails, the next-higher-priority clock source is selected. |
|---|---|
| bits | (Optional) Derives network timing from the central office (CO) Building Integrated Timing Supply (BITS) clock. |
| R0 | (Optional) Specifies Route Processor 0 BITS as the source slot. |
| R1 | (Optional) Specifies Route Processor 1 BITS as the source slot. |
| e1 | (Optional) Configures the BITS interface to use an E1 connection. |
| crc4 | (Optional) Configures the E1 BITS interface framing with Cyclic Redundancy Check 4 (CRC4). |
| no-crc4 | (Optional) Configures the E1 BITS interface framing with no CRC4. |
| unframed | (Optional) Configures the BITS interface with clear channel. |
| t1 | (Optional) Configures the BITS interface to use a T1 connection. |
| esf | (Optional) Configures the T1 BITS interface with the Extended Super Frame (ESF) framing standard. |
| sf | (Optional) Configures the T1 BITS interface with the Super Frame (SF) framing standard. |
| controller type number | Specifies the controller to be the clock source. |
| interface type number | Specifies the interface to be the clock source. |
| slot number | Specifies the slot to be the clock source. The range is 1 to 6. |
| global | (Optional) Configures the source as global. |
| local | (Optional) Configures the source as local. |
| system | Specifies the system clock as the clock source. |
| option | Specifies the standards for the network option. The applicable values are as follows: 1—Network option I is the ITU G-813 standard. 2—Network option II (Gen1) is the Bellcore GR-1244/GR-253 (stratum 3) and ITU G-813 standard. This is the default value. Note The network options are available only in the RP2 platform. | Note | The network options are available only in the RP2 platform. |
| Note | The network options are available only in the RP2 platform. |

| Note | The network options are available only in the RP2 platform. |
|---|---|

| Note | Because default clock values are derived from an external source, they can fall outside the configurable range. |
|---|---|

| Release | Modification |
|---|---|
| 11.3 MA | This command was introduced on the Cisco MC3810. |
| 12.0(3)XG | The BVM as a possible network clock source was added. |
| 12.1(5)XM | This command was implemented on the Cisco 3660. The keywords t1 and e1 were introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(2)XB | This command was implemented on the Cisco 2600 series and Cisco 3660 with AIMs installed. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T. |
| 12.2(15)T | This command was implemented on the Cisco 2600XM, Cisco 2691, Cisco 3725, and Cisco 3745. |
| 12.3(8)T4 | This command was integrated into Cisco IOS Release 12.3(8)T4 and the bri keyword was added. Support was also added for the Cisco 2800 series. |
| 12.3(11)T | This command was integrated into Cisco IOS Release 12.3(11)T and the atm keyword was added. Support was also added for the Cisco 3800 series. |
| Cisco IOS XE Release 2.1 | This command was introduced in a release earlier than Cisco IOS Release 2.1. |
| 15.0(1)S | This command was integrated into a release earlier than Cisco IOS Release 15.0(1)S. |
| Cisco IOS XE Release 3.1 | This command was modified. This command was implemented on the Cisco ASR 1000 platform. The option keyword was added. |

| Note | To minimize backplane clock shifts, the no network-clock select command does not take effect until you return to EXEC mode by entering exit or end . This process minimizes the number of times that clock sources are configured. |
|---|---|

| Command | Description |
|---|---|
| network-clock-participate | Configures a network module to participate in network clocking. |
| network-clock-switch | Configures the switch delay time to the next-priority network clock source when the current network clock source fails or
                                          a higher-priority clock source is up and available. |
| show network-clocks | Displays the network clock configuration and current primary clock source. |

| switch - delay | (Optional) Delay time, in seconds, before the next-priority network clock source is used when the current network clock source
                                          fails. Range is from 0 to 99. Default is 10. |
|---|---|
| never | (Optional) No delay time before the current network clock source recovers. |
| restore - delay | (Optional) Delay time, in seconds, before the current network clock source recovers. Range is from 0 to 99. |
| never | (Optional) No delay time before the next-priority network clock source is used when the current network clock source fails. |

| Release | Modification |
|---|---|
| 11.3(1)MA | This command was introduced on the Cisco MC3810. |

| Command | Description |
|---|---|
| network - clock - select | Uses the network clock source to provide timing to the system backplane PCM bus. |

| level | Minimum noise level in dBm. The range is from -58 to -20. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |
| 15.2(3)T | This command was modified. Support for the Cisco Unified Border Element (Cisco UBE) was added. |

| Command | Description |
|---|---|
| intensity | The intensity or depth of the noise reduction process. |
| media profile nr | Creates a media profile to configure noise reduction parameters. |

| 0db \| 3db \| 6db \| 9db | (Optional) Attenuation level of the comfort noise in dB. Default is 0db , which means that comfort noise is not attenuated. |
|---|---|---|---|---|
| threshold dB | (Optional) Sets the threshold in dB. Range is -15 to -45. Default is -21. Note This keyword is not supported when using the extended G.168 echo canceller. | Note | This keyword is not supported when using the extended G.168 echo canceller. |
| Note | This keyword is not supported when using the extended G.168 echo canceller. |

| Note | This keyword is not supported when using the extended G.168 echo canceller. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced. |
| 12.2(11)T | The threshold keyword was added. |
| 12.2(13)T | This command was implemented on routers that support the extended G.168 echo canceller. |
| 12.3(6) | The comfort-noise keyword was added. |
| 12.4 | The default setting for comfort-noise attenuation was changed from 0db to 6db. |

| Note | The echo - cancel enable command must be enabled for this command to take effect. |
|---|---|

| Command | Description |
|---|---|
| echo - cancel enable | Enables echo cancellation for voice that is sent and received on the same interface. |

| ani-dnis | ANI digits are sent in the first notify message, followed by DNIS. This is the default. |
|---|---|
| dnis-ani | DNIS digits are sent in the first notify message, followed by ANI. |

| Release | Modification |
|---|---|
| 12.4(4)T | This command was introduced. |

| Command | Description |
|---|---|
| mgcp package-capability | Specifies an MGCP package capability type for a media gateway. |
| mgcp profile | Defines an MGCP profile to be associated with one or more MGCP endpoints |
| show mgcp | Displays MGCP configuration information. |
| show mgcp profile | Displays information for MGCP profiles. |

| ip2ip | Enables notify redirection for IP-to-IP calls. |
|---|---|
| ip2pots | Enables notify redirection for IP-to-IP calls for IP-to-POTS calls. |

| Release | Modification |
|---|---|
| 12.4(4)T | This command was introduced. |
| 15.1(1)T | This command was integrated into Cisco IOS Release 15.1(1)T. The following default behavior was added: Notify redirection
                                          for SIP phones registered to Cisco Unified CME is enabled. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Note | This command is supported on Cisco Unified Communications Manager Express (Cisco Unified CME), release 3.4 and later releases
                                          and on Cisco Unified Session Initiation Protocol (SIP) Survivable Remote Site Telephony (SRST) release 3.4 and later releases.
                                          However, to use the notify redirect command in voice service VoIP configuration mode on compatible Cisco Unified SIP SRST devices, you must first use the allow-connections command to enable the corresponding call flows on the SRST gateway. |
|---|---|

| Command | Description |
|---|---|
| allow-connections | Allows connections between specific endpoint types in a VoIP network. |
| notify redirect (dial peer) | Enables application handling of redirect requests on a specific VoIP dial peer on a Cisco IOS voice gateway. |

| ip2ip | Specifies that the notify redirect command is applied to IP-to-IP calls. |
|---|---|
| ip2pots | Specifies that the notify redirect command is applied to IP-to-POTS calls. |

| Release | Modification |
|---|---|
| 12.4(4)T | This command was introduced. |
| 15.1(1)T | This command was integrated into Cisco IOS Release 15.1(1)T. The following default behavior was added: Notify redirection
                                          for SIP phones registered to Cisco Unified CME is enabled. |

| Note | This command is supported on Cisco Unified Communications Manager Express (Cisco Unified CME), release 3.4 and later releases
                                          and Cisco Unified Session Initiation Protocol (SIP) Survivable Remote Site Telephony (SRST) release 3.4 and later releases.
                                          However, to use the notify redirect command in voice service VoIP configuration mode on compatible Cisco Unified SIP SRST devices, you must first use the allow-connections command to enable the corresponding call flows on the SRST gateway. |
|---|---|

| Command | Description |
|---|---|
| allow-connections | Allows connections between specific endpoint types in a VoIP network. |
| notify redirect | Enables application handling of redirect requests for all VoIP dial peers on a Cisco IOS voice gateway. |

| max-duration milliseconds | Time
                                          						interval between consecutive NOTIFY messages for a single DTMF event, in
                                          						milliseconds. Range is from 40 to 3000. Default is 2000. |
|---|---|
| system | Specifies that the NOTIFY messages for a particular telephone
                                          						event use the global sip-ua value. This keyword is available only for the
                                          						tenant mode to allow it to fallback to the global configurations |

| Release | Modification |
|---|---|
| 12.2(15)ZJ | This
                                          						command was introduced. |
| 12.3(4)T | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 15.0(1)M | This
                                          						command was modified. The acceptable value range for the milliseconds argument was expanded (the lower end of the range was changed from 500 to 40). |
| 12.4(24)T3 | This
                                          						command was modified. The acceptable value range for the milliseconds argument was expanded (the lower end of the range was changed from 500 to 40). |
| 15.6(2)T and IOS XE Denali 16.3.1 | This command was modified to include the keyword: system . |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| dtmf-relay sip-notify | Forwards DTMF tones using SIP NOTIFY messages. |

| Release | Modification |
|---|---|
| 12.2(15)ZJ | This command was introduced. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| nsap - address | A 40-digit hexadecimal number; the number must be unique on the device. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(5)XK | This command was introduced for ATM video dial-peer configuration on the Cisco MC3810. |
| 12.0(7)T | This command was integrated into Cisco IOS Release 12.0(9)T. |

| Command | Description |
|---|---|
| dial - peer video | Defines a video ATM dial peer for a local or remote video codec, specifies video-related encapsulation, and enters dial-peer
                                          configuration mode. |
| show dial - peer video | Displays dial-peer configuration. |

| override string | Specifies the user-defined series of digits for the E.164 or private dialing plan telephone number when the called number
                                          IE is missing from the H.323 setup message. Valid entries are the digits 0 through 9. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(22)YB | This command was introduced. |
| 15.0(1)M | This command was integrated into Cisco IOS Release 15.0(1)M. |

| international | International numbering type. |
|---|---|
| abbreviated | Abbreviated numbering type. |
| national | National numbering type. |
| network | Network numbering type. |
| reserved | Reserved numbering type. |
| subscriber | Subscriber numbering type. |
| unknown | Numbering type unknown. |

| Release | Modification |
|---|---|
| 12.0(7)XR1 | This command was introduced on the Cisco AS5300. |
| 12.0(7)XK | This command was implemented as follows: VoIP: Cisco 2600 series, Cisco 3600 series, Cisco MC3810 VoFR: Cisco 2600 series, Cisco 3600 series, Cisco MC3810 VoATM: Cisco 3600 series, Cisco MC3810 |
| 12.1(1)T | This command was integrated into Cisco IOS Release 12.1(1)T and implemented as follows: VoIP: Cisco 1750, Cisco 2600 series, Cisco 3600 series, Cisco AS5300, Cisco 7200 series, Cisco 7500 series |
| 12.1(2)T | This command was implemented as follows: VoIP: Cisco MC3810 VoFR: Cisco 2600 series, Cisco 3600 series, Cisco MC3810 VoATM: Cisco 3600 series, Cisco MC3810 |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Command | Description |
|---|---|
| rule | Applies a translation rule to a calling party number or a called party number for both incoming and outgoing calls. |
| show translation - rule | Displays the contents of all the rules that have been configured for a specific translation name. |
| test translation - rule | Tests the execution of the translation rules on a specific name-tag. |
| translate | Applies a translation rule to a calling party number or a called party number for incoming calls. |
| translate - outgoing | Applies a translation rule to a calling party number or a called party number for outgoing calls. |
| translation - rule | Creates a translation name and enters translation-rule configuration mode. |
| voip - incoming translation - rule | Captures calls that originate from H.323-compatible clients. |

| extension - number | One or more digits that define an extension number for a particular dial peer. |
|---|---|
| expanded - number | One or more digits that define the expanded telephone number or destination pattern for the extension number listed. |

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 3600 series. |
| 12.0(3)T | This command was implemented on the Cisco AS5300. |
| 12.0(4)XL | This command was implemented on the Cisco AS5800. |
| 12.0(7)T | This command was integrated into Cisco IOS Release 12.0(7)T. |
| 12.0(7)XK | This command was implemented on the Cisco MC3810. |
| 12.1(2)T | This command was modified. It was integrated into Cisco IOS Release 12.1(2)T. |
| Cisco IOS XE Bengaluru 17.6.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| dial - peer terminator | Designates a special character to be used as a terminator for variable length dialed numbers. |
| forward - digits | Specifies which digits to forward for voice calls. |
| prefix | Specifies a prefix for a dial peer. |