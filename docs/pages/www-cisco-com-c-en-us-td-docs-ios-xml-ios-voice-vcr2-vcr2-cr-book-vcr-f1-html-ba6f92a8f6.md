---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr2-vcr2-cr-book-vcr-f1-html-ba6f92a8f6
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr2/vcr2-cr-book/vcr-f1.html
retrieved_at: 2026-08-16T23:16:57.312359+00:00
---

Cisco IOS Voice Command Reference - D through I

# Cisco IOS Voice Command Reference - D through I

Updated: April 25, 2026

Chapter: F

## Chapter: F

# F

## fax interface-type

To specify the interface to be used for a fax call, use the fax interface - type command in global configuration mode. To reset to the default fax protocol, use the no form of this command.

fax interface-type { fax-mail | modem | vfc }

no fax interface-type { fax-mail | modem | vfc }

### Syntax Description

fax - mail

Specifies that voice digital signal processors (DSPs) process fax store-and-forward data. This keyword replaces the vfc keyword for DSPs.

modem

(Cisco AS5300 only) Specifies that modem cards process fax store-and-forward data.

This keyword is not supported except for instances documented in the "Usage Guidelines" section.

vfc

(Cisco AS5300 only) Specifies that voice feature cards (VFCs) process fax store-and-forward data. This keyword has been superseded
                                          by the fax - mail keyword and is retained for backward compatibility only.

### Command Default

Cisco AS5300: See the "Usage Guidelines" section
                              All other platforms: fax - mail

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(3)XI

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.1(5)XM

The command was implemented on the Cisco AS5800.

12.1(5)XM2

The command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T and implemented on Cisco 1750 and the fax-mail keyword was added.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the following platforms: Cisco 1751, Cisco
                                          2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745.

12.2(11)T

This command was implemented on the following platforms: Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850.

### Usage Guidelines

When using this command to change the interface type for store-and-forward fax, you must reload (reboot or reset) the router.

On the Cisco AS5300 access server, the keyword vfc maps internally to the fax-mail keyword. If you use the vfc keyword with the fax interface-type command, the output from the show running-config command displays fax-mail as the option that was set.

The Cisco AS5300 defaults for the fax interface-type command are as follows:

If the Cisco AS5300 has voice cards only, the default is the fax-mail keyword. The modem keyword is unavailable.

If the Cisco AS5300 has modem cards only, the default is the modem keyword.

If the Cisco AS5300 has both modem and voice cards, the default is the modem keyword.

## Examples

The following example specifies the use of voice DSPs to process fax store-and-forward data:

```
Router(config)# fax interface-type fax-mail
```

The following example specifies the use of modems to process fax store-and-forward data on a Cisco AS5300:

```
Router(config)# fax interface-type modem
```

## fax protocol (dial peer)

To specify the fax protocol to be used for a specific VoIP dial peer, use the fax protocol command in dial peer configuration mode. To return to the global default fax protocol, use the system keyword or the no form of this command.

### Cisco AS5350, Cisco AS5400, Cisco AS5850

fax protocol { none | system | pass-through { g711ulaw | g711alaw }}

no fax protocol

### All Other Platforms

fax protocol { cisco | none | system | pass-through { g711ulaw | g711alaw }}

no fax protocol

### Syntax Description

cisco

Cisco-proprietary fax protocol.

none

No fax pass-through is attempted. All special fax handling is disabled, except for modem pass-through if configured with the modem pass-through command.

system

Uses the global configuration that was set using the fax protocol command in voice-service configuration mode.

pass - through

The fax stream uses one of the following high-bandwidth codecs:

g711ulaw --Uses the G.711 u-law codec.

g711alaw --Uses the G.711 a-law codec.

### Command Default

system

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.1(3)XI

This command was implemented on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.1(5)XM

This command was implemented on the Cisco AS5800. The none keyword was introduced.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco 1750.

12.2(11)T

This command was implemented on the Cisco AS5350, Cisco AS5400, Cisco  AS5800, and Cisco AS5850.

12.2(13)T

This command was integrated into Cisco IOS Release 12.2(13)T. The t.38 keyword and its options were moved to two new commands: fax protocol t38 (dial peer) and fax protocol t38 (voice-service).

### Usage Guidelines

Use the fax protocol command in dial-peer configuration mode to configure the type of fax relay capability for a specific dial peer. Note the
                              following command behavior:

fax protocol none --Disables all fax handling.

no fax protocol --Sets the fax protocol for the dial peer to the default, which is system .

If the fax protocol (voice-service) command is used to set fax relay options for all dial peers and the fax protocol (dial peer) command is used on a specific dial peer, the dial-peer configuration takes precedence over the global configuration
                              for that dial peer.

## Examples

The following example specifies that the fax stream use fax pass-through for VoIP dial peer 99:

```
dial-peer voice 99 voip
 fax protocol pass-through g711ulaw
```

### Related Commands

Command

Description

fax protocol (voice-service)

Specifies the global default fax protocol to be used for all VoIP dial peers.

fax protocol t38 (dial peer)

Specifies the ITU-T T.38 standard fax protocol to be used for a specific VoIP dial peer.

fax protocol t38 (voice-service)

Specifies the global default ITU-T T.38 standard fax protocol to be used for all VoIP dial peers.

## fax protocol (voice-service)

To specify the global default fax protocol to be used for all VoIP dial peers, use the fax protocol command in voice-service configuration mode. To return to the default fax protocol, use the no form of this command.

### Cisco AS5350, Cisco AS5400, Cisco AS5850

fax protocol { none | pass-through { g711ulaw | g711alaw }}

no fax protocol

### All Other Platforms

fax protocol { cisco | none | pass-through { g711ulaw | g711alaw }}

no fax protocol

### Syntax Description

none

No fax pass-through is attempted. All special fax handling is disabled, except for modem pass-through (if configured with
                                          the modem pass-through command).

pass-through

The fax stream uses one of the following high-bandwidth codecs:

g711alaw --Uses the G.711 A-law codec.

g711ulaw --Uses the G.711 mu-law codec.

cisco

Cisco-proprietary fax protocol. The cisco keyword is the default for all platforms except the Cisco AS5350, Cisco AS5400, and Cisco AS5850.

This is the only valid option when you are using Cisco Unified CME 4.0(3) or a later version on Skinny Call Control Protocol
                                                (SCCP)-controlled FXS ports.

### Command Default

If no fax protocol is specified, the cisco protocol is the default for all platforms except the Cisco AS5350, Cisco AS5400, and Cisco AS5850. For these three platforms, none is the default, so no fax pass-through is attempted.

### Command Modes

Voice-service configuration (config-voi-serv)

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.1(3)XI

This command was implemented on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.1(5)XM

This command was implemented on the Cisco AS5800.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco 1750.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

12.2(13)T

This command was integrated into Cisco IOS Release 12.2(13)T. The t.38 keyword and its options were removed and added to two new commands: fax protocol t38 (dial peer) and fax protocol t38 (voice-service) .

12.4(11)T

Support for SCCP-controlled FXS ports was added.

### Usage Guidelines

Use the fax protocol command with the voice service voip command to configure the fax relay capability for all VoIP dial peers.

Note the following command behavior:

fax protocol none -- Disables all fax handling.

no fax protocol --Sets the fax protocol to the default.

If the fax protocol (voice-service) command is used to set fax relay options for all dial peers and the fax protocol (dial peer) command is used on a specific dial peer, the dial-peer configuration takes precedence over the global configuration
                              for that dial peer. When the system keyword is used in the dial-peer configuration of the fax protocol command, it specifies that the global default fax protocol set with this command is used by that dial peer.

In Cisco Unified CME 4.0(3) and later, the fax protocol cisco (voice-service) command is the only supported fax protocol option for SCCP-controlled FXS ports. G.711 fax pass-through is
                              not supported for Cisco VG 224 and FXS ports.

The modem passthrough protocol and fax protocol commands cannot be configured at the same time. If you enter either one of these commands when the other is already configured,
                                          the command-line interface returns an error message. The error message serves as a confirmation notice because the modem passthrough protocol command is internally treated the same as the fax protocol passthrough command by the Cisco IOS software. For example, no other mode of fax protocol (for example, fax protocol T.38) can operate
                                          if the modem passthrough protocol command is configured.

Even though the modem passthrough protocol and fax protocol passthrough commands are treated the same internally, be aware that if you change the configuration from the modem passthrough protocol command to the modem passthrough ns e command, the configured fax protocol passthrough command is not automatically reset to the default. If default settings are required for the fax protocol command, you have to specifically configure the fax protocol command.

## Examples

The following example specifies that the fax stream for all VoIP dial peers use fax pass-through:

```
voice service voip
 fax protocol pass-through g711ulaw
```

### Related Commands

Command

Description

fax protocol (dial peer)

Specifies the fax protocol for a specific VoIP dial peer.

fax protocol t38 (dial peer)

Specifies the ITU-T T.38 standard fax protocol to be used for a specific VoIP dial peer.

fax protocol t38 (voice-service)

Specifies the global default ITU-T T.38 standard fax protocol to be used for all VoIP dial peers.

modem passthrough

Enables fax or modem pass-through over VoIP globally for all dial peers.

voice service voip

Enters voice-service configuration mode.

## fax protocol t38 (dial peer)

To specify the ITU-T T.38 standard fax protocol to be used for a specific VoIP dial peer, use the fax protocol t38 command in dial-peer configuration mode. To return to the default fax protocol, use the no form of this command.

### Cisco AS5350, Cisco AS5400, Cisco AS5850 Platforms

fax protocol t38 [ nse [ force ]] [ ls-redundancy value [ hs-redundancy value ]] [ fallback { none | pass-through { g711ulaw | g711alaw }}]

no fax protocol t38

### All Other Platforms

fax protocol t38 [ nse [ force ]] [ version { 0 | 3 }] [ ls-redundancy value [ hs-redundancy value ]] [ fallback { cisco | none | pass-through { g711ulaw | g711alaw }}]

no fax protocol t38

### Syntax Description

nse

(Optional) Uses NSEs to switch to T.38 fax relay.

force

(Optional) Unconditionally, uses Cisco network services engines (NSE) to switch to T.38 fax relay. This option allows T.38
                                          fax relay to be used between Cisco H.323 or Session Initiation Protocol (SIP) gateways and Media Gateway Control Protocol
                                          (MGCP) gateways.

version { 0 | 3 }

(Optional) Specifies a version for configuring fax speed:

0 --Configures version 0, which uses T.38 version 0 (1998--G3 faxing)

3 --Configures version 3, which uses T.38 version 3 (2004--V.34 or SG3 faxing)

ls - redundancy value

(Optional) (T.38 fax relay only) Specifies the number of redundant T.38 fax packets to be sent for the low-speed V.21-based
                                          T.30 fax machine protocol. Range varies by platform from 0 (no redundancy) to 5 or 7. For details, see to command-line interface
                                          (CLI) help. Default is 0.

hs - redundancy value

(Optional) (T.38 fax relay only) Specifies the number of redundant T.38 fax packets to be sent for high-speed V.17, V.27,
                                          and V.29 T.4 or T.6 fax machine image data. Range varies by platform from 0 (no redundancy) to 2 or 3. For details, see the
                                          command-line interface (CLI) help. Default is 0.

fallback

(Optional) A fallback mode is used to transfer a fax across a VoIP network if T.38 fax relay could not be successfully negotiated
                                          at the time of the fax transfer.

cisco

(Optional) Cisco-proprietary fax protocol.

none

(Optional) No fax pass-through or T.38 fax relay is attempted. All special fax handling is disabled, except for modem pass-through
                                          if configured with the modem pass-through command.

pass - through

(Optional) The fax stream uses one of the following high-bandwidth codecs:

g711ulaw --Uses the G.711 mu-law codec.

g711alaw --Uses the G.711 a-law codec.

### Command Default

ls-redundancy 0 hs-redundancy 0 fallback none for the Cisco AS5350, Cisco AS5400, and Cisco AS5850 platforms ls-redundancy 0 hs-redundancy 0 fallback cisco for all other platforms

### Command Modes

Dial-peer configuration (config-dial-peer)

## Command History

Release

Modification

12.2(13)T

This command was introduced.

15.1(1)T

This command was modified. The version keyword was added with the 0 and 3 keywords to specify fax speed as G3 or SG3.

### Usage Guidelines

Use this command in dial-peer configuration mode to configure the type of fax relay capability for a specific dial peer. If
                              the fax protocol t38 (voice-service) command is used to set fax relay options for all dial peers and the fax protocol t38 (dial peer) command is used on a specific dial peer, the dial-peer configuration takes precedence over the global configuration for that
                              dial peer.

If you specify version 3 in the fax protocol t38 command and negotiate T.38 version 3, the fax rate is automatically set to 33600.

The ls-redundancy and hs-redundancy keywords are used to send redundant T.38 fax packets. Setting the hs-redundancy keyword to a value greater than 0 causes a significant increase in the network bandwidth consumed by the fax call.

Use the nse force option when the H.323 or SIP gateway is interoperating with a Cisco MGCP gateway and the call agent does not support the
                              interworking and negotiation of T.38 fax relay and NSE attributes at the time of call setup. When the corresponding option
                              is configured on the MGCP gateway, the nse force option allows T.38 fax relay to be used between Cisco H.323 or SIP gateways and MGCP gateways.

## Examples

The following example show how to configure T.38 fax relay for VoIP:

```
dial-peer voice 99 voip
 fax protocol t38
```

The following example shows how to use NSEs to enter T.38 fax relay mode:

```
dial-peer voice 99 voip
 fax protocol t38 nse
```

The following example shows how to specify the T.38 fax protocol for this dial peer, set low-speed redundancy to a value of
                              1, and set high-speed redundancy to a value of 0:

```
dial-peer voice 99 voip
 fax protocol t38 ls-redundancy 1 hs-redundancy 0
```

### Related Commands

Command

Description

fax protocol (dial peer)

Specifies the fax protocol for a specific VoIP dial peer.

fax protocol (voice-service)

Specifies the global default fax protocol to be used for all VoIP dial peers.

fax protocol t38 (voice-service)

Specifies the global default ITU-T T.38 standard fax protocol to be used for all VoIP dial peers.

## fax protocol t38 (voice-service)

To specify the global default ITU-T T.38 standard fax protocol to be used for all VoIP dial peers, use the fax protocol t38 command in voice-service configuration mode. To return to the default fax protocol, use the no form of this command.

### Cisco AS5350, Cisco AS5400, Cisco AS5850 Platforms

fax protocol t38 [ nse [ force ]] [ version { 0 | 3 }] [ ls-redundancy value [ hs-redundancy value ]] [ fallback { none | pass-through { g711ulaw | g711alaw }}]

no fax protocol t38

### All Other Platforms

fax protocol t38 [ nse [ force ]] [ version { 0 | 3 }] [ ls-redundancy value [ hs-redundancy value ]] [ fallback { cisco | none | pass-through { g711ulaw | g711alaw }}]

no fax protocol t38

### Syntax Description

nse

(Optional) Uses network services engines (NSE) to switch to T.38 fax relay.

force

(Optional) Unconditionally, uses Cisco NSEs to switch to T.38 fax relay. This option allows T.38 fax relay to be used between
                                          Cisco H.323 or Session Initiation Protocol (SIP) gateways and Media Gateway Control Protocol (MGCP) gateways.

version { 0 | 3 }

(Optional) Specifies a version for configuring fax speed:

0 --Configures version 0, which uses T.38 version 0 (1998--G3 faxing)

3 --Configures version 3, which uses T.38 version 3 (2004--V.34 or SG3 faxing)

ls - redundancy value

(Optional) (T.38 fax relay only) Specifies the number of redundant T.38 fax packets to be sent for the low-speed V.21-based
                                          T.30 fax machine protocol. Range varies by platform from 0 (no redundancy) to 5 or 7. For details, refer to command-line interface
                                          (CLI) help. Default is 0.

hs - redundancy value

(Optional) (T.38 fax relay only) Specifies the number of redundant T.38 fax packets to be sent for high-speed V.17, V.27,
                                          and V.29 T.4 or T.6 fax machine image data. Range varies by platform from 0 (no redundancy) to 2 or 3. For details, refer
                                          to the command-line interface (CLI) help. Default is 0.

fallback

(Optional) A fallback mode is used to transfer a fax across a VoIP network if T.38 fax relay could not be successfully negotiated
                                          at the time of the fax transfer.

cisco

(Optional) Cisco-proprietary fax protocol.

none

(Optional) No fax pass-through or T.38 fax relay is attempted. All special fax handling is disabled, except for modem pass-through
                                          if configured with the modem pass-through command.

pass - through

(Optional) The fax stream uses one of the following high-bandwidth codecs:

g711ulaw --Uses the G.711 mu-law codec.

g711alaw --Uses the G.711 a-law codec.

### Command Default

ls-redundancy 0 hs-redundancy 0 fallback none for the Cisco AS5350, Cisco AS5400, and Cisco AS5850 platforms ls-redundancy 0 hs-redundancy 0 fallback cisco for all other platforms

### Command Modes

Voice-service configuration (config-voi-srv)

## Command History

Release

Modification

12.2(13)T

This command was introduced.

15.1(1)T

This command was Modified. The version keyword was added with the 0 and 3 keywords to specify fax speed.

Introduced support for YANG models.

### Usage Guidelines

Use the fax protocol t38 command and the voice service voip command to configure T.38 fax relay capability for all VoIP dial peers. If the fax protocol t38 (voice-service) command is used to set fax relay options for all dial peers and the fax protocol t38 (dial-peer) command is used on a specific dial peer, the dial-peer configuration takes precedence over the global configuration
                              for that dial peer.

If you specify version 3 in the fax protocol t38 command and negotiate T.38 version 3, the fax rate is automatically set to 33600.

The ls - redundancy and hs - redundancy keywords are used to send redundant T.38 fax packets. Setting the hs - redundancy keyword to a value greater than 0 causes a significant increase in the network bandwidth consumed by the fax call.

Use the nse force option when the H.323 or SIP gateway is interoperating with a Cisco MGCP gateway and the call agent does not support the
                              interworking and negotiation of T.38 fax relay and NSE attributes at the time of call setup. When the corresponding option
                              is configured on the MGCP gateway, the nse force option allows T.38 fax relay to be used between Cisco H.323 or SIP gateways and MGCP gateways.

Do not use the cisco keyword for the fallback option if you specified version 3 for SG3 fax transmission.

## Examples

The following example shows how to configure the T.38 fax protocol for VoIP:

```
voice service voip
 fax protocol t38
```

The following example shows how to use NSEs to unconditionally enter T.38 fax relay mode:

```
voice service voip
 fax protocol t38 nse
```

The following example shows how to specify the T.38 fax protocol for all VoIP dial peers, set low-speed redundancy to a value
                              of 1, and set high-speed redundancy to a value of 0:

```
voice service voip
 fax protocol t38 ls-redundancy 1 hs-redundancy 0
```

### Related Commands

Command

Description

fax protocol (dial peer)

Specifies the fax protocol for a specific VoIP dial peer.

fax protocol (voice-service)

Specifies the global default fax protocol to be used for all VoIP dial peers.

fax protocol t38 (dial peer)

Specifies the ITU-T T.38 standard fax protocol to be used for a specific VoIP dial peer.

voice service voip

Enters voice-service configuration mode.

## fax rate (dial peer)

To establish the rate at which a fax is sent to a specified dial peer, use the fax rate command in dial-peer configuration mode. To reset the dial peer for voice calls, use the no form of this command.

fax rate { 2400 | 4800 | 7200 | 9600 | 12000 | 14400 } { disable | voice } [ bytes milliseconds ]

no fax rate

### Syntax Description

2400

2400 bits per second (bps) fax transmission speed.

4800

4800 bps fax transmission speed.

7200

7200 bps fax transmission speed.

9600

9600 bps fax transmission speed.

12000

12000 bps fax transmission speed.

14400

14400 bps fax transmission speed.

disable

Disables fax relay transmission capability.

voice

Highest possible transmission speed allowed by the voice rate.

bytes milliseconds

(Optional) Specifies fax packetization rate, in milliseconds. Range is 20 to 48. Default is 20.

For Cisco fax relay, this keyword-argument pair is valid only on Cisco 2600 series, Cisco 3600 series, Cisco AS5300, and Cisco
                                                7200 series routers.

For T.38 fax relay, this keyword-argument pair is valid only on Cisco AS5350, Cisco AS5400, and Cisco AS5850 routers. For
                                                other routers, the packetization rate for T.38 fax relay is fixed at 40 ms and cannot be changed.

### Command Default

Voice rate

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

11.3(1)T

This command was introduced as the fax - rate command on the Cisco 3600.

12.0(2)XH

The 12000 keyword was added.

12.0(4)T

This command was integrated into Cisco IOS Release 12.0(4)T and implemented on the Cisco MC3810.

12.1(3)T

The command name changed from fax - rate to fax rate (nonhyphenated).

12.1(3)XI

This command was implemented on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.1(5)XM

This command was implemented on the Cisco AS5800.

12.1(5)XM2

The command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the following platforms: Cisco 1751, Cisco
                                          2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745.

12.2(11)T

This command was implemented on the following platforms: Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850.

### Usage Guidelines

Use this command to specify the fax transmission rate to the specified dial peer.

The values for this command apply only to the fax transmission speed and do not affect the quality of the fax itself. The
                              higher transmission speed values (14,400 bps) provide a faster transmission speed but monopolize a significantly large portion
                              of the available bandwidth. The lower transmission speed values (2400 bps) provide a slower transmission speed and use a relatively
                              smaller portion of the available bandwidth.

The fax call is not compressed using the ip rtp header-compression command because User Datagram Protocol (UDP) is being used and not Real-Time Transport Protocol (RTP). For example, a 9600
                                          bps fax call takes approximately 24 kbps.

If the fax rate transmission speed is set higher than the codec rate in the same dial peer, the data sent over the network
                              for fax transmission is above the bandwidth reserved for Resource Reservation Protocol (RSVP).

Tip

Because a large portion of the available network bandwidth is monopolized by the fax transmission, Cisco does not recommend
                                          setting the fax rate value higher than the value of the selected codec. If the fax rate value is set lower than the codec
                                          value, faxes take longer to send but use less bandwidth.

The voice keyword specifies the highest possible transmission speed allowed by the voice rate. For example, if the voice codec is G.711,
                              the fax transmission may occur at a rate up to 14,400 bps because 14,400 bps is less than the 64k voice rate. If the voice
                              codec is G.729 (8k), the fax transmission speed is 7200 bps.

## Examples

The following example configures a fax rate transmission speed of 9600 bps for faxes sent using a dial peer:

```
dial-peer voice 100 voip
 fax rate 9600 voice
```

The following example sets a fax rate transmission speed at 12,000 bps and the packetization rate at 20 milliseconds:

fax rate 12000 bytes 20

### Related Commands

Command

Description

codec (dial peer)

Specifies the voice coder rate of speech for a dial peer.

fax protocol (dial peer)

Specifies the fax protocol for a specific VoIP dial peer.

## fax rate (pots)

To establish the rate at which a fax is sent to the specified plain old telephone service (POTS) dial peer, use the fax rate command in dial-peer configuration mode. To reset the dial peer to handle only voice calls, use the no form of this command.

fax rate { disable | system | voice }

no fax rate

### Syntax Description

disable

Disables fax-relay transmission capability.

system

Uses rate choice specified in global fax rate CLI under the voice service pots command.

voice

Highest possible transmission speed allowed by the voice rate for this dial peer. For example, if the voice codec is G.711,
                                          fax transmission may occur at a rate of up to 14,400 bps.

### Command Default

System

### Command Modes

dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.2(8)T

This command was introduced on the following platforms: Cisco 1700 series, Cisco 3600 series, and Cisco ICS 7750.

### Usage Guidelines

This implementation of the fax rate command is only applicable to POTS dial peers.

## Examples

The following example shows a fax rate transmission set to voice on POTS dial peer 1:

```
dial-peer voice 1 pots
 fax rate voice
```

### Related Commands

Command

Description

codec (dial peer)

Specifies the voice coder rate of speech for a dial peer.

fax rate (voip)

Establishes the rate at which a fax is sent to the specified VoIP dial peer.

## fax rate (voice-service)

To establish the rate at which a fax is sent for POTS-to-POTS voice calls, use the f ax rate command in voice-service configuration mode. To reset for voice only calls, use the no form of this command.

fax rate { disable | voice }

no fax rate

### Syntax Description

disable

Disables fax relay transmission capability.

voice

Highest possible transmission speed allowed by the voice rate. For example, if the voice codec is G.711, fax transmission
                                          may occur at a rate of up to 14400 bps.

### Command Default

fax rate voice command behavior is enabled by default

### Command Modes

Voice service configuration (config-voi-serv)

## Command History

Release

Modification

12.2(8)T

This command was introduced on the following platforms: Cisco 1700 series, Cisco 3600 series, and Cisco ICS 7750.

12.3(4)T

This command was modified so that the "fax rate voice" setting is the default setting for the fax rate command in voice-service configuration mode and, hence, will no longer be displayed in the running configuration.

### Usage Guidelines

This implementation of the fax rate command applies only when voice service is set to POTS. Although fax rate voice command behavior is the default setting, you must specify this functionality in voice-service configuration mode in order
                              to establish the rate at which a fax is sent for POTS-to-POTS voice calls. If you do not configure fax rate voice functionality and you do not specify fax rate disable command behavior, fax calls are processed as a regular voice calls and their completion is subject to line quality just like
                              any other form of voice communication.

Because the fax rate voice command has been reclassified as a default setting, it will no longer automatically generate an entry in your gateway router’s
                                          running configuration in NVRAM. If your gateway configuration requires fax rate voice command functionality, you must reconfigure your gateway after loading a Cisco IOS image earlier than Cisco IOS Release 12.3(4)T.

## Examples

The following example shows voice service fax rate transmission set to disable :

```
voice service pots
 fax rate disable
```

### Related Commands

Command

Description

fax protocol (voice - service)

Specifies the global default fax protocol for all VoIP dial peers.

voice service

Specifies the voice encapsulation type.

## fax receive called-subscriber

To define the called subscriber identification (CSI), use the fax receive called - subscriber command in global configuration mode. To disable the configured CSI, use
                              		  the no form of this command.

fax receive
                                 				  called-subscriber { $d$ | telephone-number }

no fax receive
                                 				  called-subscriber { $d$ | telephone-number }

### Syntax Description

$d$

Wildcard that indicates that the information displayed is
                                          						captured from the configured destination pattern.

telephone-number

Destination telephone number. Valid entries are the plus
                                          						sign (+), numerals from 0 through 9, and the space character. This string can
                                          						specify an E.164 telephone number; if you choose to configure an E.164
                                          						telephone number, you must use the plus sign as the first character.

### Command Default

Enabled with a null string

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(4)XJ

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release
                                          						12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on following platforms: Cisco
                                          						1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745.

### Usage Guidelines

Use this command to define the number displayed in the liquid crystal
                              		  display (LCD) of the sending fax device when you are sending a fax to a
                              		  recipient. Typically, with a standard Group 3 fax device, this is the telephone
                              		  number associated with the receiving fax device. The command defines the CSI.

This command applies to on-ramp store-and-forward fax functions.

## Examples

The following example configures the number 555-0134 as the called
                              		  subscriber number:

```
fax receive called-subscriber 5550134
```

## fax-relay (dial peer)

To enable the suppression of call menu (CM) tones or answer (ANS) tones from reaching the Super Group 3 (SG3) fax machines,
                              thereby forcing the SG3 fax machines to train down and negotiate to G3 speeds, to enable ANS tone treatment, or to disable
                              fax-relay Error Correction Mode (ECM) on a VoIP dial peer, use the fax-relay command in dial peer configuration mode. To disable these functions, use the no form of this command.

fax-relay { ans-disable | ans-treatment | ecm-disable | sg3-to-g3 [system] }

no fax-relay { ans-disable | ans-treatment | ecm-disable | sg3-to-g3 [system] }

### Syntax Description

ans-disable

Suppresses ANS tones at originating SG3 fax machines so that the SG3 fax machines can operate at G3 speeds using fax relay.

ans-treatment

Enables modem and fax answer tone treatment.

ecm-disable

Disables fax-relay ECM on a VoIP dial peer.

sg3-to-g3

Enables SG3 machines to negotiate to G3 speeds using fax relay.

system

(Optional) The protocol set to be used in the voice-service configuration mode.

### Command Default

Modem upspeed occurs when ANS tones are detected. Fax-relay ECM is enabled.

ANS tone treatment is not enabled.

SG3 machines negotiate to G3 speeds using fax relay.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.1(3)T

This command was introduced as the fax-relay ecm-disable command.

12.1(5)XM

This command was integrated into Cisco IOS Release 12.1(5)XM and implemented on the Cisco AS5800 Series Universal Gateways.

12.1(5)XM2

This command was integrated into Cisco IOS Release 12.1(5)XM2 and implemented on the Cisco AS5350 and Cisco AS5400 Series
                                          Universal Gateways.

12.2(2)XB1

This command was integrated into Cisco IOS Release 12.2(2)XB1 and implemented on the Cisco AS5850 Series Universal Gateways.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

12.4(4)T

This command was modified. The sg3-to-g3 system keyword and argument pair was added.

12.4(6)T

This command was integrated into Cisco IOS Release 12.4(6)T and implemented on Cisco 1700 and Cisco 2800 Series routers.

12.4(20)T1

This command was modified. The ans-disable keyword was added to support the suppression of ANS tones from reaching the SG3 fax machines, thereby enabling the SG3 fax
                                          machines to negotiate to G3 speeds.

15.1(4)M

This command was modified. The ans-treatment keyword was added to support the modem and fax ANS tone treatment.

### Usage Guidelines

The ans-disable keyword helps to ensure that modem upspeed does not occur when ANS tones are detected. When the fax-relay ans-disable command is enabled, modem-related sessions fail because the ANS tones are squelched at the digital signal processor (DSP)
                              level by the TI C5510 DSP.

When the fax-relay ans-treatment command is enabled, the modem and fax ANS tone treatment is enabled. An ANS tone is a modem answer tone of 2100 Hz. Occasionally,
                              the ANS tone is followed by a phase reversal. ANS tone treatment is a mechanism to handle ANS tones with or without phase
                              reversal and to generate/transmit RFC 2833 modem tone events on detection of ANS tones. For ANS tone treatment to be triggered,
                              the dtmf-relay rtp-nte command has to be enabled in dial peer configuration mode and the RFC 2833 Dual Tone Multifrequency (DTMF) relay has to be
                              negotiated for the audio session.

When the fax-relay ecm-disable command is enabled, the DSP fax-relay firmware disables ECM by modifying the Digital Information Signal (DIS) T.30 message
                              when the DSP channel starts the fax relay and cannot be changed during the fax relay. ECM disable is performed on DIS signals
                              in both directions so that ECM is disabled in both directions even if only one gateway is configured with ECM disabled. This
                              setting is provisioned when the DSP channel starts fax relay and cannot be changed during the fax relay session.

When the fax-relay sg3-to-g3 command is enabled, the DSP fax-relay firmware suppresses the V.8 CM tone and the fax machines negotiate down to G3 speeds
                              for the fax stream. Modem communication is impacted if the session does not negotiate either modem passthrough or relay. Use
                              this command for H.323 and Session Initiation Protocol (SIP) signaling types.

The fax-relay command is also available in voice-service configuration mode, but the ecm-disable system keyword and argument pair is not available in voice-service configuration mode.

## Examples

The following example shows how to disable ECM on the voice dial peer:

```
Device> enable Device(config)# dial-peer voice 25 voip Device(config-dial-peer)# fax-relay ecm-disable
```

The following example shows how to enable SG3 V.8 fax CM message suppression on the voice dial peer for H.323 and SIP signaling
                              types:

```
Device> enable Device(config)# dial-peer voice 25 voip Device(config-dial-peer)# fax-relay sg3-to-g3
```

The following dial-peer configuration shows how to enable ANS tone squelching at the DSP level for all VoIP dial peers:

```
Device> enable Device(config)# dial-peer voice 25 voip Device(config-dial-peer)# fax-relay ans-disable
```

The following example shows how to enable ANS tone treatment:

```
Device> enable Device# configure terminal Device(config)# dial-peer voice 25 voip Device(config-dial-peer)# dtmf-relay rtp-nte Device(config-dial-peer)# modem passthrough nse codec g711ulaw redundancy maximum-session 5 Device(config-dial-peer)# fax-relay ans-treatment Device(config-dial-peer)# exit
```

### Related Commands

Command

Description

dtmf-relay (Voice over IP)

Forwards dual tone multifrequency tones by using RTP with the NTE payload type.

fax-relay (voice-service)

Allows ANS tones to be disabled for SG3 machines to operate at G3 speeds using fax relay, enables ANS tone treatment, or
                                          enables the fax stream between two SG3 fax machines to negotiate to G3 speeds on a VoIP dial peer.

mgcp fax-relay

Allows ANS tones to be disabled for SG3 machines to operate at G3 speeds for MGCP fax relay or enables the fax stream between
                                          two SG3 fax machines to negotiate down to G3 speeds for MGCP fax relay.

modem passthrough (Dial-peer)

Enables fax or modem pass-through over VoIP for a specific dial peer.

## fax-relay (voice-service)

To enable the suppression of call menu (CM) tones or answer (ANS) tones from reaching the Super Group 3 (SG3) fax machines,
                              thereby forcing the SG3 fax machines to train down and negotiate to G3 speeds, or to enable answer (ANS) tone treatment, use
                              the fax-relay command in voice-service configuration mode. To disable these functions, use the no form of this command.

fax-relay { ans-disable | ans-treatment | sg3-to-g3 }

no fax-relay { ans-disable | ans-treatment | sg3-to-g3 }

### Syntax Description

ans-disable

Suppresses ANS tones at originating SG3 fax machines so that the SG3 fax machines can operate at G3 speeds using fax relay.

ans-treatment

Enables modem and fax answer tone treatment.

sg3-to-g3

Enables SG3 machines to negotiate to G3 speeds using fax relay.

### Command Default

Modem upspeed occurs when ANS tones are detected.

ANS tone treatment is not enabled.

SG3 machines negotiate to G3 speeds using fax relay.

### Command Modes

Voice-service configuration (conf-voi-serv)

## Command History

Release

Modification

12.4(4)T

This command was introduced as the fax-relay sg3-to-g3 command.

12.4(6)T

This command was integrated into Cisco IOS Release 12.4(6)T and implemented on Cisco 1700 and Cisco 2800 Series routers.

12.4(20)T

This command was modified. The ans-disable keyword was added to support the suppression of ANS tones from reaching the SG3 fax machines, thereby enabling the SG3 fax
                                          machines to negotiate to G3 speeds.

15.1(4)M

This command was modified. The ans-treatment keyword was added to support the modem and fax ANS tone treatment.

### Usage Guidelines

The ans-disable keyword helps to ensure that modem upspeed does not occur when ANS tones are detected. When the fax-relay ans-disable command is enabled, modem-related sessions fail because the ANS tones are squelched at the digital signal processor (DSP)
                              level by the TI C5510 DSP.

When the fax-relay ans-treatment command is enabled, the modem and fax ANS tone treatment is enabled. An ANS tone is a modem answer tone of 2100 Hz. Occasionally,
                              the ANS tone is followed by a phase reversal. ANS tone treatment is a mechanism to handle ANS tones with or without phase
                              reversal and to generate/transmit RFC 2833 modem tone events on detection of ANS tones. For ANS tone treatment to be triggered,
                              the dtmf-relay rtp-nte command has to be enabled in voice-service configuration mode and the RFC 2833 Dual Tone Multifrequency (DTMF) relay has
                              to be negotiated for the audio session.

When the fax-relay sg3-to-g3 command is enabled, the DSP fax-relay firmware suppresses the V.8 CM tone and the fax machines negotiate down to G3 speeds
                              for the fax stream. Modem communication is impacted if the session does not negotiate either modem passthrough or relay. Use
                              this command for H.323 and Session Initiation Protocol (SIP) signaling types.

## Examples

The following example shows how to enable SG3 V.8 fax CM message suppression for all VoIP dial peers:

```
Device> enable Device# configure terminal Device(config)# voice service voip Device(conf-voi-serv)# fax-relay sg3-to-g3
```

The following example shows how to enable ANS tone squelching at DSP level for all VoIP dial peers:

```
Device> enable Device# configure terminal Device(config)# voice service voip Device(conf-voi-serv)# fax-relay ans-disable
```

The following example shows how to enable ANS tone treatment:

```
Device> enable Device# configure terminal Device(config)# voice service voip Device(conf-voi-serv)# dtmf-relay rtp-nte Device(conf-voi-serv)# modem passthrough nse codec g711ulaw redundancy maximum-session 5 Device(conf-voi-serv)# fax-relay ans-treatment Device(conf-voi-serv)# exit
```

### Related Commands

Command

Description

dtmf-relay (Voice over IP)

Forwards dual tone multifrequency tones by using RTP with the NTE payload type.

fax-relay (dial-peer)

Allows ANS tones to be disabled for SG3 machines to operate at G3 speeds using fax relay, enables ANS tone treatment, disables
                                          fax-relay ECM on a VoIP dial peer, or enables the fax stream between two SG3 fax machines to negotiate to G3 speeds on a VoIP
                                          dial peer.

mgcp fax-relay

Allows ANS tones to be disabled for SG3 machines to operate at G3 speeds for MGCP fax relay or enables the fax stream between
                                          two SG3 fax machines to negotiate to G3 speeds for MGCP fax relay.

modem passthrough (Voice-service)

Enables fax or modem pass-through over VoIP globally for all dial peers.

## fax send center-header

To specify the data that appears in the center position of the fax
                              		  header information, use the fax send center - header command in global configuration mode. To remove the selected options, use
                              		  the no form of this command.

fax send
                                 				  center-header { $a | $d$ | $p$ | $s$ | $t$ } string

no fax send
                                 				  center-header { $a | $d$ | $p$ | $s$ | $t$ } string

### Syntax Description

$a$

Wildcard that inserts the date in the selected position.

$d$

Wildcard that inserts the destination address in the
                                          						selected position.

$p$

Wildcard that inserts the page count in the selected
                                          						position.

$s$

Wildcard that inserts the sender’s address in the selected
                                          						position.

$t$

Wildcard that inserts the transmission time in the selected
                                          						position.

string

Text string that provides personalized information. Valid
                                          						characters are any text plus wildcards--for example, Time:$t$. There is no
                                          						default.

### Command Default

Disabled

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(4)XJ

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release
                                          						12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the following platforms:
                                          						Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745.

### Usage Guidelines

Mail messages that contain only text or contain text attachments
                              		  (text of the MIME media type) can be converted by the off-ramp gateway into a
                              		  format understood by a fax machine’s text-to-fax converter. When this
                              		  conversion is performed, this command indicates what header information is
                              		  added to the center top position of those pages.

Mail messages with TIFF attachments (MIME media image type and TIFF
                              		  subtype) are expected to include their own per-page headers.

Faxed header information cannot be converted from TIFF files to
                                          		  standard fax transmissions.

This command lets you configure several options by combining one or
                              		  more wildcards with text string information to customize your fax header
                              		  information.

If the information you have selected for the fax send center - header command
                                          		  exceeds the space allocated for the center fax header, the information is
                                          		  truncated.

This command applies to off-ramp store-and-forward fax functions.

## Examples

The following example selects the fax transmission time as the
                              		  centered fax header:

```
fax send center-header $t$
```

The following example configures the company name "widget" and its
                              		  address as the centered fax header:

```
fax send center-header widget $s$
```

### Related Commands

Command

Description

fax send left - header

Specifies the data that appears on the left in the fax
                                          						header.

fax send right - header

Specifies the data that appears on the right in the fax
                                          						header.

## fax send coverpage comment

To define customized text for the title field of a fax cover sheet, use the fax send coverpage comment command in global configuration mode. To disable the defined comment, use the no form of this command.

fax send coverpage comment string

no fax send coverpage comment string

### Syntax Description

string

Text string that adds customized text in the title field of the fax cover sheet. Valid characters are any ASCII characters.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(4)XJ

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the following platforms: Cisco 1751, Cisco
                                          2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745.

### Usage Guidelines

This command can be overridden by the fax send coverpage e-mail-controllable command.

This command applies to off-ramp store-and-forward fax functions.

## Examples

The following example configures an individualized title comment of "XYZ Fax Services" for generated fax cover sheets:

```
fax send coverpage enable
fax send coverpage comment XYZ Fax Services
```

### Related Commands

Command

Description

fax send coverpage e - mail - controllable

Controls the cover page generation on a per-recipient basis, based on the information contained in the destination address
                                          of the e-mail message.

fax send coverpage enable

Generates fax cover sheets.

fax send coverpage show - detail

Prints all of the e-mail header information as part of the fax cover sheet.

## fax send coverpage e-mail-controllable

To defer to the cover page setting in the e-mail header to generate a standard fax cover sheet, use the fax send coverpage e - mail - controllable command in global configuration mode. To disable standard fax sheet generation, use the no form of this command.

fax send coverpage e-mail-controllable

no fax send coverpage e-mail-controllable

### Syntax Description

This command has no arguments or keywords.

### Command Default

Disabled

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(4)XJ

This command was introduced on the Cisco AS5300 universal access server.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750 access router.

12.2(8)T

This command was implemented on the following platforms: Cisco 1751, Cisco 2600, Cisco 3600 series, Cisco 3725, and Cisco
                                          3745.

### Usage Guidelines

You can also use the destination address of an e-mail message to control the cover page generation on a per-recipient basis.
                              Use this command to configure the router to defer to the cover page setting in the e-mail header.

In essence, the off-ramp router defers to the setting configured in the e-mail address itself. For example, if the address
                              has a parameter set to cover=no, this parameter overrides the setting for the fax send coverpage enable command, and the off-ramp gateway does not generate and send a fax cover page. If the address has a parameter set to cover=yes,
                              the off-ramp gateway defers to this parameter setting to generate and send a fax cover page.

The table below shows examples of what the user would enter in the To: field of the e-mail message.

To: Field Entries

Description

FAX=+1-312-555-3260@fax.com

Fax sent to an E.164-compliant long distance telephone number in the United States. If the fax coverpage enable command is entered, store-and-forward fax generate a fax cover page.

FAX=+1-312-555-3260/cover=no@fax.com

Fax sent to an E.164-compliant long distance telephone number in the United States. In this example, the fax send coverpage enable command is superseded by the cover=no statement. No cover page is generated.

FAX=+1-312-555-3260/cover=yes@fax.com

Fax sent to an E.164-compliant long distance telephone number in the United States. In this example, the fax send coverpage enable command is superseded by the cover=yes statement. Store-and-forward fax generates a fax cover page.

This command applies to off-ramp store-and-forward fax functions.

## Examples

The following example enables standard generated fax cover sheets:

```
fax send coverpage enable
fax send coverpage e-mail-controllable
```

### Related Commands

Command

Description

fax send coverpage comment

Defines customized text for the title field of a fax cover sheet.

fax send coverpage enable

Generates fax cover sheets.

fax send coverpage show - detail

Prints all the e-mail header information as part of the fax cover sheet.

## fax send coverpage enable

To generate fax cover sheets for faxes that were converted into e-mail messages, use the fax send coverpage enable command in global configuration mode. To disable fax cover sheet generation, use the no form of this command.

fax send coverpage enable

no fax send coverpage enable

### Syntax Description

This command has no arguments or keywords.

### Command Default

Disabled

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(4)XJ

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the following platforms: Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and
                                          Cisco 3745.

### Usage Guidelines

This command applies to off-ramp store-and-forward fax functions.

This command is applicable only to faxes that were converted to e-mail messages. The Cisco AS5300 universal access server
                                          does not alter fax TIFF attachments. Therefore you cannot use this command to enable the Cisco AS5300 to generate fax cover
                                          pages for faxes that are converted from TIFF files to standard fax transmissions.

## Examples

The following example enables the generation of fax cover sheets:

```
fax send coverpage enable
```

### Related Commands

Command

Description

fax send coverpage comment

Defines customized text for the title field of a fax cover sheet.

fax send coverpage e - mail - controllable

Defers to the cover page setting in the e-mail header to generate a standard fax cover sheet

fax send coverpage show - detail

Prints all the e-mail header information as part of the fax cover sheet.

## fax send coverpage show-detail

To display all e-mail header information as part of the fax cover sheet, use the fax send coverpage show - detail command in global configuration mode. To prevent the e-mail header information from being displayed, use the no form of this command.

fax send coverpage show-detail

no fax send coverpage show-detail

### Syntax Description

This command has no arguments or keywords.

### Command Default

Disabled

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(4)XJ

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the following platforms: Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and
                                          Cisco 3745.

### Usage Guidelines

This command applies to off-ramp store-and-forward fax functions.

This command is applicable only to faxes that are converted to e-mail messages. The Cisco AS5300 universal access server does
                                          not alter fax TIFF attachments. Therefore, you cannot use this command to enable the Cisco AS5300 to display additional fax
                                          cover page information for faxes that are converted from TIFF files to standard fax transmissions.

## Examples

The following example configures an individualized generated fax cover sheet that contains the e-mail header text:

```
fax send coverpage enable
no fax send coverpage e-mail-controllable
fax send coverpage show-detail
```

### Related Commands

Command

Description

fax send coverpage comment

Defines customized text for the title field of a fax cover sheet.

fax send coverpage e - mail - controllable

Defers to the cover page setting in the e-mail header to generate a standard fax cover sheet.

fax send coverpage enable

Generates fax cover sheets.

## fax send left-header

To specify the data that appears on the left in the fax header, use
                              		  the fax send left - header command in global configuration mode. To disable the selected
                              		  options, use the no form of this command.

fax send
                                 				  left-header { $a | $d$ | $p$ | $s$ | $t$ } string

no fax send
                                 				  left-header { $a | $d$ | $p$ | $s$ | $t$ } string

### Syntax Description

$a$

Wildcard that inserts the date in the selected position.

$d$

Wildcard that inserts the destination address in the
                                          						selected position.

$p$

Wildcard that inserts the page count in the selected
                                          						position.

$s$

Wildcard that inserts the sender’s address in the selected
                                          						position.

$t$

Wildcard that inserts the transmission time in the selected
                                          						position.

string

Text string that provides customized information. Valid
                                          						characters are any combination of ASCII characters and the wildcards listed
                                          						above.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(4)XJ

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release
                                          						12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the following platforms:
                                          						Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745.

### Usage Guidelines

Mail messages that contain only text or text attachments (text of
                              		  MIME media type) can be converted by the off-ramp device into a format
                              		  understood by fax machines using a text-to-fax converter. When this conversion
                              		  is performed, the fax send left-header command is used to indicate what
                              		  header information should be added to the top left of those pages.

Mail messages with TIFF attachments (MIME media image type and TIFF
                              		  subtype) are expected to include their own per-page headers, and the Cisco IOS
                              		  software does not modify TIFF attachments.

This command lets you configure several options at once by combining
                              		  one or more wildcards with text string information to customize your fax header
                              		  information.

If the information you select for the fax send left-header command exceeds the space allocated
                              		  for the left fax header, the information is truncated.

This command applies to off-ramp store-and-forward fax functions.

## Examples

The following example puts the fax transmission time on the left side
                              		  of the fax header:

```
fax send left-header $t$
```

The following example puts the company name "widget" and its address
                              		  on the left side of the fax header:

```
fax send left-header widget $s$
```

### Related Commands

Command

Description

fax send center-header

Specifies the data that appears in the center of the fax
                                          						header.

fax send right-header

Specifies the data that appears on the right in the fax
                                          						header.

## fax send max-speed

To specify the maximum speed at which an outbound fax is transmitted, use the fax send max - speed command in global configuration mode. To disable the selected speed, use the no form of this command.

fax send max-speed { 2400 | 4800 | 7200 | 9600 | 12000 | 14400 }

no fax send max-speed { 2400 | 4800 | 7200 | 9600 | 12000 | 14400 }

### Syntax Description

2400

Transmission speed of 2400 bits per second (bps).

4800

Transmission speed of 4800 bps.

7200

Transmission speed of 7200 bps.

9600

Transmission speed of 9600 bps.

12000

Transmission speed of 12,000 bps.

14400

Transmission speed of 14,400 bps. This is the default.

### Command Default

14,400 bps

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(4)XJ

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the following platforms: Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and
                                          Cisco 3745.

### Usage Guidelines

This command applies to off-ramp store-and-forward fax functions.

## Examples

The following example sets the outbound fax transmission rate at 2400 bps:

```
fax send max-speed 2400
```

## fax send right-header

To specify the data that appears on the right in the fax header
                              		  information, use the fax send right - header command in global configuration mode. To disable the selected options, use
                              		  the no form of this command.

fax send
                                 				  right-header { $a | $d$ | $p$ | $s$ | $t$ } string

no fax send
                                 				  right-header { $a | $d$ | $p$ | $s$ | $t$ } string

### Syntax Description

$a$

Wildcard that inserts the date in the selected position.

$d$

Wildcard that inserts the destination address in the
                                          						selected position.

$p$

Wildcard that inserts the page count in the selected
                                          						position.

$s$

Wildcard that inserts the sender address in the selected
                                          						position.

$t$

Wildcard that inserts the transmission time in the selected
                                          						position.

string

Text string that provides customized information. Valid
                                          						characters are any combination of ASCII characters and the wildcards listed
                                          						above.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(4)XJ

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release
                                          						12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the following platforms:
                                          						Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745.

### Usage Guidelines

Mail messages that contain only text or text attachments (text of
                              		  MIME media type) can be converted by the off-ramp device into a format
                              		  understood by fax machines using the text-to-fax converter. When this
                              		  conversion is performed, this command is used to indicate what header
                              		  information should be added to top right of those pages.

Mail messages with TIFF attachments (MIME media image type and TIFF
                              		  subtype) are expected to include their own per-page headers, and the Cisco IOS
                              		  software does not modify TIFF attachments.

This command lets you configure several options at once by combining
                              		  one or more wildcards with text string information to customize your fax header
                              		  information.

If the information you select for the fax send right - header command exceeds the space allocated for the right fax header,
                                          		  the information is truncated.

This command applies to off-ramp store-and-forward fax functions.

## Examples

The following example puts the fax date in the right-hand side of the
                              		  fax header:

```
fax send right-header $a$
```

The following example puts the company name "XYZ" and its address in
                              		  the right-hand side of the fax header:

```
fax send right-header XYZ $s$
```

### Related Commands

Command

Description

fax send center - header

Specifies the data that appears in the center in the fax
                                          						header.

fax send left - header

Specifies the data that appears on the left in the fax
                                          						header.

## fax send transmitting-subscriber

To define the transmitting subscriber information (TSI), use the fax send transmitting - subscriber command in global configuration mode. To disable the configured
                              		  value, use the no form of this command.

fax send
                                 				  transmitting-subscriber { $s$ | string }

no fax send
                                 				  transmitting-subscriber { $s$ | string }

### Syntax Description

$s$

Wildcard that inserts the sender name from the RFC 822
                                          						header (captured by the on-ramp device from the sending fax machine) in the
                                          						selected position.

string

Originating telephone number. Valid entries are the plus
                                          						sign (+), numerals from 0 through 9, and the space character. This string can
                                          						specify an E.164 telephone number; if you choose to configure an E.164
                                          						telephone number, you must use the plus sign as the first character.

### Command Default

Disabled

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(4)XJ

This command was introduced on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release
                                          						12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the following platforms:
                                          						Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745.

### Usage Guidelines

The transmitting subscriber number is the number of the originating
                              		  fax and is displayed in the LCD of the receiving fax device. Typically, with a
                              		  standard Group 3 fax device, this number is the telephone number associated
                              		  with the transmitting or sending fax device. This command defines the TSI.

This command applies to off-ramp store-and-forward fax functions.

## Examples

The following example configures the company number as captured by
                              		  the on-ramp device from the sending fax machine:

```
fax send transmitting-subscriber +14085550134
```

## file-acct flush

To manually flush call detail records (CDRs) from the buffer to the accounting file, use the file-acct flush command in privileged EXEC mode.

file-acct flush { with-close | without-close }

### Syntax Description

with-close

Call records are appended to the accounting file and the file is closed.

without-close

Call records are appended to the accounting file and the file remains open.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.4(15)XY

This command was introduced.

12.4(20)T

This command was integrated into Cisco IOS Release 12.4(20)T.

### Usage Guidelines

Use this command if you need to manually flush the buffer, for example, if flash becomes full or you do not want to wait until
                              the buffer is automatically flushed. This command immediately flushes the buffer and appends all CDRs in the buffer to the
                              current accounting file. CDRs are automatically flushed from the buffer and written to the file whenever there is enough data
                              based on the maximum buffer-size command or after the timer set with the maximum cdrflush-timer command expires.

Using the with-close keyword closes the current file and opens a new file after appending the records. Using the without-close keyword leaves the current file open after appending the records.

## Examples

The following example appends the records to the accounting file and closes the file:

```
file-acct flush with-close
```

### Related Commands

Command

Description

gw-accounting

Enables an accounting method for collecting CDRs.

maximum buffer-size

Sets the maximum size of the file accounting buffer.

maximum cdrflush-timer

Sets the maximum time to hold call records in the buffer before appending the records to the accounting file.

maximum fileclose-timer

Sets the maximum time for saving records to an accounting file before closing the file and creating a new one.

primary

Sets the primary location for storing the CDRs generated for file accounting.

secondary

Sets the backup location for storing CDRs if the primary location becomes unavailable.

## file-acct reset

To manually switch back to the primary device for file accounting, use the file-acct reset command in privileged EXEC mode.

file-acct reset

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.4(15)XY

This command was introduced.

12.4(20)T

This command was integrated into Cisco IOS Release 12.4(20)T.

### Usage Guidelines

This command allows you to switch back to the primary device when it becomes available if the backup device is currently being
                              used because the primary device failed.

If the file transfer to the primary device fails, the file accounting process retries the primary device up to the number
                              of times defined by the maximum retry-count command and then switches to the secondary device defined with the secondary command. This command flushes the buffer and writes the call detail records (CDRs) to the currently active file before resetting
                              to the primary device and opening a new file.

If the secondary device also fails, the accounting process ends and the system logs an error. New CDRs are dropped until one
                              device comes back online and you use this command. The system then immediately resets to the primary device, if available.

## Examples

The following example shows how to switch back to the primary device:

```
Router# file-acct reset
```

### Related Commands

Command

Description

gw-accounting

Enables an accounting method for collecting CDRs.

maximum retry-count

Sets the maximum number of times the router attempts to connect to the primary file device before switching to the secondary
                                          device

primary

Sets the primary location for storing the CDRs generated for file accounting.

secondary

Sets the backup location for storing CDRs if the primary location becomes unavailable.

## filter voice

To specify that voice calls bypass authentication, authorization, and accounting (AAA) preauthentication, use the filter voice command in AAA preauthentication configuration mode. To disable AAA bypass, use the no form of this command.

filter voice

no filter voice

### Syntax Description

This command has no arguments or keywords.

### Command Default

Disabled

### Command Modes

AAA preauthentication configuration (config-preauth)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

## Examples

The following example specifies that voice calls bypass AAA preauthentication:

```
Router(config)# aaa preauth Router(config-preauth)# filter voice
```

### Related Commands

Command

Description

aaa preauth

Enters AAA preauthentication configuration mode.

## flush

To enable file mode accounting flush options, use the flush command in privileged EXEC mode.

flush { with-close | without-close }

### Syntax Description

with-close

Enables file accounting flush pending accounting to the file, and closes the file when the process is complete.

without-close

Enables file accounting flush pending accounting to file.

### Command Default

File mode accounting flush options are not enabled.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

15.0(1)M

This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M.

### Usage Guidelines

The flush command flushes pending accounting records to the file.

## Examples

In the following example, the flush with-close command enables file accounting flush pending accounting to the file, and closes the file when the process is complete:

```
Router# flush with-close
```

### Related Commands

Command

Description

maximum cdrflush-timer

Sets the maximum time to hold call records in the buffer before appending the records to the accounting file.

## fmtp

To set a format-specific string for a codec, use the fmtp command in codec-profile configuration mode. To disable the format string, use the no form of this command.

fmtp string

no fmtp

### Syntax Description

string

fmtp:payload type name1= val1; name2 = val2...

For Cisco Unified Customer Voice Portal (Cisco Unified CVP), the dynamic payload number is in the range of 96 to 127 for H.263+.
                              For H263, it is always 34. For H.263+, this number must be entered but it is not used. Cisco Unified CVP uses either the default
                              value for H.263+ (118) or the value defined for the VoIP dial peer using the command rtp payload-type cisco-codec-video-h263+ , a number in the range 96 to 127.

Other parameters can be the following:

SQCIF = 1 - 32

QCIF = 1 - 32

CIF = 1 - 32

4CIF = 1 - 32

16CIF = 1 - 32

MAXBR (max bitrate) = Value in 100 bits per second (500 = 50000 bits per second). This value is another that is not used.
                                    Always set H.324 to 50K.

D--1 (Enable H.263 Annex D)

F--1 (Enable H.263 Annex F)

I--1 (Enable H.263 Annex I)

J--1 (Enable H.263 Annex J)

- 1--Slices In Order, Nonrectangular

- 2--Slices In Order, Rectangular

- 3--Slices Not Ordered, Nonrectangular

- 4--Slices Not Ordered, Rectangular

- 1--NEITHER: No back-channel data is returned from the decoder to the encoder.

- 2--ACK: The decoder returns only acknowledgment messages.

- 3--NACK: The decoder returns only nonacknowledgment messages.

- 4--ACK+NACK: The decoder returns both acknowledgment and nonacknowledgment messages.

- 1--dynamicPictureResizingByFour

- 2--dynamicPictureResizingBySixteenthPel

- 3--dynamicWarpingHalfPel

- 4--dynamicWarpingSixteenthPel.

The valid combinations are:

- 1

- 1,3

- 2

- 2, 3

- 2, 4

- 3

T=1 (Enable H.263 Annex T)

CUSTOM = x, y, MPI -- Defines a custom picture format, where X is the X-axis size in pixels, Y is the Y-axis size in pixels,
                                    and MPI is the frame rate (30/(1.001*MPI)). X and Y must be divisible by 4, and MPI has a value of 1to 32.

### Command Default

No string is configured.

### Command Modes

Codec-profile configuration (config-codec-profile)

## Command History

Release

Modification

12.4(22)T

This command was introduced.

### Usage Guidelines

The profile is selected by entering the command:

video codec h263/h263+ profile 1000

The video codec h263/h263+ profile can be used in a voip dial peer or as a voice class codec entry.

## Examples

The following example shows an fmtp string for video codec profile 116:

```
codec profile 116 H263
	clockrate 90000
	fmtp "fmtp:120 SQCIF=1;QCIF=1;CIF=1;CIF4=2;MAXBR=3840;I=1"
```

### Related Commands

Command

Description

clock-rate

Sets the clock rate for the codec.

## forward-alarms

To turn on alarm forwarding so that alarms that arrive on one T1/E1 port are sent to the other port on dual-mode multiflex
                              trunk interface cards, use the forward-alarms command in controller configuration mode on the one port. To reset to the default so that no alarms are forwarded, use the no form of this command.

forward-alarms

no forward-alarms

### Syntax Description

This command has no arguments or keywords.

### Command Default

Alarm forwarding is disabled

### Command Modes

Controller configuration (config-controller)

## Command History

Release

Modification

12.0(7)XR

This command was introduced.

12.1(1)T

This command was integrated into Cisco IOS Release 12.1(1)T.

### Usage Guidelines

When you enter this command, physical-layer alarms on the configured port are forwarded to the other port on dual-port cards,
                              simulating a one-way repeater operations. The system forwards RAIs (remote alarm indications, or Yellow Alarms), alarm indication
                              signals (AIS, or Blue Alarms), losses of frame (LOF alarms, or Red Alarms), and losses of signaling (LOS alarms, or Red Alarms).

## Examples

The following example turns on alarm forwarding on controller E1 0/0:

```
controller e1 0/0
 forward-alarms
```

## forward-digits

To specify which digits to forward for voice calls, use the forward - digits command in dial peer configuration mode. To specify that any digits not matching the destination-pattern are not to be forwarded,
                              use the no form of this command.

forward-digits { num-digit | all | extra }

no forward-digits

### Syntax Description

num - digit

The number of digits to be forwarded. If the number of digits is greater than the length of a destination phone number, the
                                          length of the destination number is used. Range is 0 to 32. Setting the value to 0 is equivalent to entering the no forward - digits command.

all

Forwards all digits. If all is entered, the full length of the destination pattern is used.

extra

If the length of the dialed digit string is greater than the length of the dial-peer destination pattern, the extra right-justified
                                          digits are forwarded. However, if the dial-peer destination pattern is variable length ending with the character "T" (for
                                          example: T, 123T, 123...T), extra digits are not forwarded.

### Command Default

Dialed digits not matching the destination pattern are forwarded

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

11.3(1)MA

This command was introduced on the Cisco MC3810.

12.0(2)T

This command was integrated into Cisco IOS Release 12.0(2)T. The implicit option keyword was added.

12.0(4)T

This command was modified to support ISDNBF PRI QSIG signaling calls.

12.0(7)XK

This command was implemented on the Cisco 2600 series and Cisco 3600 series. The implicit keyword was removed and the extra keyword was added.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

### Usage Guidelines

This command applies only to POTS dial peers. Forwarded digits are always right justified so that extra leading digits are
                              stripped. The destination pattern includes both explicit digits and wildcards if present.

For QSIG ISDN connections, entering the forward - digits all command implies that all the digits of the called party number are sent to the ISDN connection. When the forward - digits num-digit command and a number from 1 to 32 are entered, the number of digits of the called party number specified (right justified)
                              are sent to the ISDN connection.

## Examples

The following example shows that all digits in the destination pattern of a POTS dial peer are forwarded:

```
dial-peer voice 1 pots
 destination-pattern 8...
 forward-digits all
```

The following example shows that four of the digits in the destination pattern of a POTS dial peer are forwarded:

```
dial-peer voice 1 pots
 destination-pattern 555....
 forward-digits 4
```

The following example shows that the extra right-justified digits that exceed the length of the destination pattern of a POTS
                              dial peer are forwarded:

```
dial-peer voice 1 pots
 destination-pattern 555....
 forward-digits extra
```

### Related Commands

Command

Description

destination-pattern

Defines the prefix or the full E.164 telephone number to be used for a dial peer.

show dial-peer voice

Displays configuration information for dial peers.

## frame-relay voice bandwidth

To specify how much bandwidth should be reserved for voice traffic on a specific data-link connection identifier (DLCI),
                              use the frame - relay voice bandwidth command in map-class configuration mode. To release the bandwidth previously reserved for voice traffic, use the no form of this command.

frame-relay voice bandwidth bits-per-second

no frame-relay voice bandwidth bits-per-second

### Syntax Description

bits-per-second

Bandwidth, in bits per second (bps), reserved for voice traffic for the specified map class. Range is from 8000 to 45000000.
                                          Default is 0, which disables voice calls.

### Command Default

Disabled (zero)

### Command Modes

Map-class configuration (config-map-class)

## Command History

Release

Modification

12.0(3)XG

This command was introduced on the following platforms: Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, and Cisco
                                          MC3810.

12.0(4)T

This command was integrated into Cisco IOS Release 12.0(4)T.

12.0(5)T

The queue depth keyword and argument were added.

12.2(1)

The queue depth keyword and argument were removed.

### Usage Guidelines

To use this command, you must first associate a Frame Relay map class with a specific DLCI and then enter map-class configuration
                              mode and set the amount of bandwidth to be reserved for voice traffic for that map class.

If a call is attempted and there is not enough remaining bandwidth reserved for voice to handle the additional call, the
                              call is rejected. For example, if 64 kbps is reserved for voice traffic and a codec and payload size is being used that requires
                              10 kbps of bandwidth for each call, the first six calls attempted are accepted, but the seventh call is rejected.

Reserve queues are not required for Voice over Frame Relay (VoFR).

Cisco strongly recommends that you set voice bandwidth to a value less than the committed information rate (CIR) if Frame
                                          Relay traffic shaping is configured. Cisco also strongly recommends that you set the minimum CIR (using the frame - relay mincir command) to be at least equal to or greater than the voice bandwidth.

Calculating Required Bandwidth

The bandwidth required for a voice call depends on the bandwidth of the codec, the voice packetization overhead, and the
                              voice frame payload size. The smaller the voice frame payload size, the higher the bandwidth required for the call. To make
                              the calculation, use the following formula:

required_bandwidth = codec_bandwidth x (1 + overhead / payload_size)

As an example, the overhead for a VoFR voice packet is between 6 and 8 bytes: a 2-byte Frame Relay header, a 1- or 2-byte
                              FRF.11 header (depending on the CID value), a 2-byte cyclic redundancy check (CRC), and a 1-byte trailing flag. If voice sequence
                              numbers are enabled in the voice packets, there is an additional 1-byte sequence number. The table below shows the required
                              voice bandwidth for the G.729 8000-bps speech coder for various payload sizes.

Codec

Codec Bandwidth

Voice Frame Payload Size

Required Bandwidth per Call (6-Byte OH)

Required Bandwidth per Call (8-Byte OH)

G.729

8000 bps

120 bytes

8400 bps

8534 bps

G.729

8000 bps

80 bytes

8600 bps

8800 bps

G.729

8000 bps

40 bytes

9200 bps

9600 bps

G.729

8000 bps

30 bytes

9600 bps

10134 bps

G.729

8000 bps

20 bytes

10400 bps

11200 bps

To configure the payload size for the voice frames, use the codec command from dial-peer configuration mode.

## Examples

The following example shows how to reserve 64 kbps for voice traffic for the "vofr" Frame Relay map class:

```
interface serial 1/1
 frame-relay interface-dlci 100
  class vofr
  exit
map-class frame-relay vofr
 frame-relay voice bandwidth 64000
```

### Related Commands

Command

Description

codec (dial-peer)

Specifies the voice coder rate of speech for a VoFR dial peer.

frame-relay fair-queue

Enables weighted fair queueing for one or more Frame Relay PVCs.

frame-relay fragment

Enables fragmentation for a Frame Relay map class.

frame-relay interface-dlci

Assigns a DLCI to a specified Frame Relay subinterface on the router or access server.

frame-relay mincir

Assigns the minimum CIR for Frame Relay traffic shaping.

map-class frame-relay

Specifies a map class to define QoS values for an SVC.

## freq-max-delay

To specify the maximum timing difference allowed between the two frequencies for detection of a tone, use the freq - max - delay command in 
                              voice-class 
                              configuration mode. To reset to the default allowed timing difference, use the no form of this command.

freq-max-delay time

no freq-max-delay

### Syntax Description

time

Maximum number of 10-millisecond time intervals by which the two frequencies in a tone may differ from each other and be detected.
                                          Range is from 10 to 100 (100 milliseconds to 1 second). Default is 10 (100 milliseconds).

### Command Default

10 (100 milliseconds)

### Command Modes

Voice-class configuration (config-voice-class)

## Command History

Release

Modification

12.1(5)XM

This command was implemented on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 1750.

### Usage Guidelines

This command creates a detection limit for one parameter within a voice class that you can apply to any voice port.

You must specify a time value greater than the timing difference expected in the tone to be detected.

## Examples

The following example configures a maximum timing difference of 200 milliseconds for voice class 100:

```
voice class dualtone 100
 freq-max-delay 20
```

The following example configures a maximum timing difference of 160 milliseconds for voice class 70:

```
voice class dualtone-detect-params 70
 freq-max-delay 160
```

### Related Commands

Command

Description

dualtone

Defines the tone and cadence for a custom call-progress tone.

freq-pair

Specifies the frequency components of a tone to be detected.

supervisory answer dualtone

Enables answer supervision on a voice port.

voice class dualtone

Creates a voice class for FXO tone detection parameters.

## freq-max-deviation

To specify the maximum frequency deviation allowed in a tone, use the freq - max - deviation command in voice-class 
                              configuration mode. To reset to the default maximum frequency deviation, use the no form of this command.

freq-max-deviation hertz

no freq-max-deviation

### Syntax Description

hertz

Maximum cycles per second (Hz) by which tone frequencies may deviate from the configured frequencies and be detected. The
                                          value applies to both frequencies of a dual tone. Range is from 10 to 125. The default is 10.

### Command Default

10 Hz

### Command Modes

Voice-class configuration (config-voice-class)

## Command History

Release

Modification

12.1(5)XM

This command was implemented on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 1750.

### Usage Guidelines

This command creates a detection limit for one parameter within a voice class that you can apply to any voice port.

Be sure that the frequency deviation is less than the smallest frequency difference between any two call-progress tones to
                              prevent overlapping of detectable frequencies. If detectable frequencies overlap, one of the call-progress tones is not detected.

You must specify a time value greater than the expected frequency deviation in the tone to be detected.

## Examples

The following example configures a maximum frequency deviation of 20 Hz for voice class 100:

```
voice class dualtone 100
 freq-max-deviation 20
```

The following example configures a maximum frequency deviation of 20 Hz for voice class 70:

```
voice class dualtone-detect-params 70
 freq-max-deviation 20
```

### Related Commands

Command

Description

dualtone

Defines the tone and cadence for a custom call-progress tone.

freq-pair

Specifies the frequency components of a tone to be detected.

supervisory answer dualtone

Enables answer supervision on a voice port.

supervisory dualtone-detect-params

Assigns the boundary and detection tolerance parameters to a voice port.

voice class dualtone

Creates a voice class for FXO tone detection parameters.

## freq-max-power

To specify the upper limit of tone power allowed in a tone, use the freq - max - power command in voice-class configuration mode. To reset to the default maximum tone power, use the no form of this command.

freq-max-power dBm0

no freq-max-power

### Syntax Description

dBm0

Upper limit of the tone power that is detected, in dBm0 (where dBm0 is decibels referred to one milliwatt and corrected to
                                          a 0-dBm effective power level). Range is from 0 to -20. The default is -10.

### Command Default

-10 dBm0

### Command Modes

Voice-class configuration

## Command History

Release

Modification

12.1(5)XM

This command was implemented on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 1750.

### Usage Guidelines

This command creates a detection limit for one parameter within a voice class that you can apply to any voice port.

You must specify a power value greater than the expected maximum power of a tone to be detected.

## Examples

The following example configures a maximum tone power of -20 dBm0 for voice class 100:

```
voice class dualtone 100
 freq-max-power -20
```

The following example configures a maximum tone power of -6 dBm0 for voice class 70:

```
voice class dualtone-detect-params 70
 freq-max-power -6
```

### Related Commands

Command

Description

dualtone

Defines the tone and cadence for a custom call-progress tone.

freq-pair

Specifies the frequency components of a tone to be detected.

supervisory answer dualtone

Enables answer supervision on a voice port.

supervisory dualtone-detect-params

Assigns the boundary and detection tolerance parameters defined by the voice class dualtone - detect - params command to a voice port.

voice class dualtone

Creates a voice class for FXO tone detection parameters.

## freq-min-power

To specify the lower limit of tone power allowed in a tone, use the freq - min - power command in voice-class configuration mode. To reset to the default minimum tone power, use the no form of this command.

freq-min-power dBm0

no freq-min-power

### Syntax Description

dBm0

Lower limit of tone power that is detected, in dBm0 (where dBm0 is decibels referred to one milliwatt and corrected to a 0-dBm
                                          effective power level). Range is from -10 to -35. The default is -30.

### Command Default

-30 dBm0

### Command Modes

Voice-class configuration

## Command History

Release

Modification

12.1(5)XM

This command was implemented on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 1750.

### Usage Guidelines

This command creates a detection limit for one parameter within a voice class that you can apply to any voice port.

You must specify a power value less than the expected minimum power of a tone to be detected.

## Examples

The following example configures a tone-power lower limit of -15 dBm0 for voice class 100:

```
voice class dualtone 100
 freq-min-power -15
```

The following example configures a tone-power lower limit of -25 dBm0 for voice class 70:

```
voice class dualtone-detect-params 70
 freq-min-power -25
```

### Related Commands

Command

Description

dualtone

Defines the tone and cadence for a custom call-progress tone.

freq-pair

Specifies the frequency components of a tone to be detected.

supervisory answer dualtone

Enables answer supervision on a voice port.

supervisory dualtone-detect-params

Assigns the boundary and detection tolerance parameters to a voice port.

voice class dualtone

Creates a voice class for FXO tone detection parameters.

## freq-pair

To specify the frequency components of a tone to be detected, use the freq - pair command in voice-class
                              
                              configuration mode. To cancel detection of a tone, use the no form of this command.

freq-pair tone-id frequency-1 frequency-2

no freq-pair tone-id

### Syntax Description

tone-id

Tag identifier for a tone to be detected. Range is from 1 to 16. There is no default.

frequency-1

One frequency component of the tone to be detected, in Hz. Range is from 300 to 3600. There is no default.

frequency-2

A second frequency component of the tone to be detected, in Hz. Range is frm 300 to 3600, or you can specify 0. There is no
                                          default.

### Command Default

No tone is specified for detection

### Command Modes

Voice-class configuration (config-voice-class)

## Command History

Release

Modification

12.1(3)T

This command was introduced on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

### Usage Guidelines

To detect a tone with two frequency components (a dualtone), configure frequencies for frequency-1 and frequency-2 .

To detect a tone with only one frequency component, configure a frequency for frequency-1 and enter 0 for frequency-2 .

You can configure a router to detect up to 16 tones.

## Examples

The following example configures tone number 1 (tone-id 1) with frequency components of 480 Hz and 2400 Hz:

```
voice class dualtone 100
 freq-pair 1 480 2400
 exit
```

The following example configures tone number 1 (tone-id 1) with frequency components of 480 Hz and 2400 Hz and tone number
                              2 (tone-id 2) with frequency components of 560 Hz and 880 Hz:

```
voice class dualtone 50
 freq-pair 1 480 2400
 freq-pair 2 560 880
 exit
```

### Related Commands

Command

Description

frag-pre-queuing

Specifies the maximum timing difference allowed between the two frequencies for detection of a tone.

freq-max-deviation

Specifies the maximum frequency deviation allowed in a tone.

freq-max-power

Specifies the upper limit of the tone power allowed in a tone.

freq-min-power

Specifies the lower limit of the tone power allowed in a tone.

freq-power-twist

Specifies the power difference allowed between the two frequencies of a tone.

voice class dualtone

Creates a voice class for FXO tone detection parameters.

## freq-power-twist

To specify the power difference allowed between the two frequencies of a tone, use the freq - power - twist command in 
                              voice
                              -
                              class 
                              configuration mode. To reset to the default power difference allowed, use the no form of this command.

freq-power-twist dBm0

no freq-power-twist

### Syntax Description

dBm0

Maximum power difference allowed between the two frequencies of a tone, in dBm0 (where dBm0 is decibels referred to one milliwatt
                                          and corrected to a 0-dBm effective power level). Range is from 0 to 15. The default is 6.

### Command Default

6 dBm0

### Command Modes

Voice-class configuration (config-voice-class)

## Command History

Release

Modification

12.1(5)XM

This command was implemented on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 1750.

### Usage Guidelines

This command creates a detection limit for one parameter within a voice class that you can apply to any voice port.

You must specify a power value greater than the expected maximum power difference of the two frequencies in the tone to be
                              detected.

## Examples

The following example configures a maximum allowed power difference of 3 dBm0 between the two tone frequencies for voice class
                              100:

```
voice class dualtone 100
 freq-power-twist 3
```

The following example configures a maximum allowed power difference of 15 dBm0 between the two tone frequencies in voice class
                              70:

```
voice class dualtone-detect-params 70
 freq-power-twist 15
```

### Related Commands

Command

Description

dualtone

Defines the tone and cadence for a custom call-progress tone.

freq-pair

Specifies the frequency components of a tone to be detected.

supervisory answer dualtone

Enables answer supervision on a voice port.

supervisory dualtone-detect-params

Assigns the boundary and detection tolerance parameters defined by the voice class dualtone-detect-params command to a voice port.

voice class dualtone

Creates a voice class for FXO tone detection parameters.

## frequency (cp-dualtone)

To define the frequency components for a call-progress tone, use the frequency command in cp-
                              dualtone 
                              configuration mode. To reset to the default frequency components, use the no form of this command.

frequency frequency-1 [frequency-2]

no frequency

### Syntax Description

frequency - 1

One frequency component of the tone to be detected, in Hz. Range is from 300 to 3600. The default is 300.

frequency - 2

(Optional) A second frequency component of the tone to be detected, in Hz. Range is from 300 to 3600 or you can specify 0.
                                          The default is that no second frequency component is detected.

### Command Default

300-Hz single tone

### Command Modes

cp-dualtone configuration

## Command History

Release

Modification

12.1(5)XM

This command was introduced on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 1750.

### Usage Guidelines

This command specifies the frequency component for a class of custom call-progress tones.

You need to define the frequency that you want a voice port to detect. Reenter the command for each additional frequency to
                              be detected.

You need to associate the class of custom call-progress tones with a voice port for this command to affect tone detection.

## Examples

The following example defines the frequency components for the busy tone in custom-cptone voice class country-x.

```
voice class custom-cptone country-x
 dualtone busy frequency 480 620
```

### Related Commands

Command

Description

supervisory custom-cptone

Associates a class of custom call-progress tones with a voice port.

voice class custom-cptone

Creates a voice class for defining custom call-progress tones.

voice class dualtone-detect-params

Modifies the boundaries and limits for custom call-progress tones defined by the voice class custom-cptone command.

| fax - mail | Specifies that voice digital signal processors (DSPs) process fax store-and-forward data. This keyword replaces the vfc keyword for DSPs. |
|---|---|
| modem | (Cisco AS5300 only) Specifies that modem cards process fax store-and-forward data. Note This keyword is not supported except for instances documented in the "Usage Guidelines" section. | Note | This keyword is not supported except for instances documented in the "Usage Guidelines" section. |
| Note | This keyword is not supported except for instances documented in the "Usage Guidelines" section. |
| vfc | (Cisco AS5300 only) Specifies that voice feature cards (VFCs) process fax store-and-forward data. This keyword has been superseded
                                          by the fax - mail keyword and is retained for backward compatibility only. |

| Note | This keyword is not supported except for instances documented in the "Usage Guidelines" section. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)XI | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.1(5)XM | The command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | The command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T and implemented on Cisco 1750 and the fax-mail keyword was added. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the following platforms: Cisco 1751, Cisco
                                          2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745. |
| 12.2(11)T | This command was implemented on the following platforms: Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850. |

| cisco | Cisco-proprietary fax protocol. |
|---|---|
| none | No fax pass-through is attempted. All special fax handling is disabled, except for modem pass-through if configured with the modem pass-through command. |
| system | Uses the global configuration that was set using the fax protocol command in voice-service configuration mode. |
| pass - through | The fax stream uses one of the following high-bandwidth codecs: g711ulaw --Uses the G.711 u-law codec. g711alaw --Uses the G.711 a-law codec. |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.1(3)XI | This command was implemented on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.1(5)XM | This command was implemented on the Cisco AS5800. The none keyword was introduced. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco 1750. |
| 12.2(11)T | This command was implemented on the Cisco AS5350, Cisco AS5400, Cisco  AS5800, and Cisco AS5850. |
| 12.2(13)T | This command was integrated into Cisco IOS Release 12.2(13)T. The t.38 keyword and its options were moved to two new commands: fax protocol t38 (dial peer) and fax protocol t38 (voice-service). |

| Command | Description |
|---|---|
| fax protocol (voice-service) | Specifies the global default fax protocol to be used for all VoIP dial peers. |
| fax protocol t38 (dial peer) | Specifies the ITU-T T.38 standard fax protocol to be used for a specific VoIP dial peer. |
| fax protocol t38 (voice-service) | Specifies the global default ITU-T T.38 standard fax protocol to be used for all VoIP dial peers. |

| none | No fax pass-through is attempted. All special fax handling is disabled, except for modem pass-through (if configured with
                                          the modem pass-through command). |
|---|---|
| pass-through | The fax stream uses one of the following high-bandwidth codecs: g711alaw --Uses the G.711 A-law codec. g711ulaw --Uses the G.711 mu-law codec. |
| cisco | Cisco-proprietary fax protocol. The cisco keyword is the default for all platforms except the Cisco AS5350, Cisco AS5400, and Cisco AS5850. This is the only valid option when you are using Cisco Unified CME 4.0(3) or a later version on Skinny Call Control Protocol
                                                (SCCP)-controlled FXS ports. |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.1(3)XI | This command was implemented on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.1(5)XM | This command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T and implemented on the Cisco 1750. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |
| 12.2(13)T | This command was integrated into Cisco IOS Release 12.2(13)T. The t.38 keyword and its options were removed and added to two new commands: fax protocol t38 (dial peer) and fax protocol t38 (voice-service) . |
| 12.4(11)T | Support for SCCP-controlled FXS ports was added. |

| Note | The modem passthrough protocol and fax protocol commands cannot be configured at the same time. If you enter either one of these commands when the other is already configured,
                                          the command-line interface returns an error message. The error message serves as a confirmation notice because the modem passthrough protocol command is internally treated the same as the fax protocol passthrough command by the Cisco IOS software. For example, no other mode of fax protocol (for example, fax protocol T.38) can operate
                                          if the modem passthrough protocol command is configured. |
|---|---|

| Note | Even though the modem passthrough protocol and fax protocol passthrough commands are treated the same internally, be aware that if you change the configuration from the modem passthrough protocol command to the modem passthrough ns e command, the configured fax protocol passthrough command is not automatically reset to the default. If default settings are required for the fax protocol command, you have to specifically configure the fax protocol command. |
|---|---|

| Command | Description |
|---|---|
| fax protocol (dial peer) | Specifies the fax protocol for a specific VoIP dial peer. |
| fax protocol t38 (dial peer) | Specifies the ITU-T T.38 standard fax protocol to be used for a specific VoIP dial peer. |
| fax protocol t38 (voice-service) | Specifies the global default ITU-T T.38 standard fax protocol to be used for all VoIP dial peers. |
| modem passthrough | Enables fax or modem pass-through over VoIP globally for all dial peers. |
| voice service voip | Enters voice-service configuration mode. |

| nse | (Optional) Uses NSEs to switch to T.38 fax relay. |
|---|---|
| force | (Optional) Unconditionally, uses Cisco network services engines (NSE) to switch to T.38 fax relay. This option allows T.38
                                          fax relay to be used between Cisco H.323 or Session Initiation Protocol (SIP) gateways and Media Gateway Control Protocol
                                          (MGCP) gateways. |
| version { 0 \| 3 } | (Optional) Specifies a version for configuring fax speed: 0 --Configures version 0, which uses T.38 version 0 (1998--G3 faxing) 3 --Configures version 3, which uses T.38 version 3 (2004--V.34 or SG3 faxing) |
| ls - redundancy value | (Optional) (T.38 fax relay only) Specifies the number of redundant T.38 fax packets to be sent for the low-speed V.21-based
                                          T.30 fax machine protocol. Range varies by platform from 0 (no redundancy) to 5 or 7. For details, see to command-line interface
                                          (CLI) help. Default is 0. |
| hs - redundancy value | (Optional) (T.38 fax relay only) Specifies the number of redundant T.38 fax packets to be sent for high-speed V.17, V.27,
                                          and V.29 T.4 or T.6 fax machine image data. Range varies by platform from 0 (no redundancy) to 2 or 3. For details, see the
                                          command-line interface (CLI) help. Default is 0. |
| fallback | (Optional) A fallback mode is used to transfer a fax across a VoIP network if T.38 fax relay could not be successfully negotiated
                                          at the time of the fax transfer. |
| cisco | (Optional) Cisco-proprietary fax protocol. |
| none | (Optional) No fax pass-through or T.38 fax relay is attempted. All special fax handling is disabled, except for modem pass-through
                                          if configured with the modem pass-through command. |
| pass - through | (Optional) The fax stream uses one of the following high-bandwidth codecs: g711ulaw --Uses the G.711 mu-law codec. g711alaw --Uses the G.711 a-law codec. |

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced. |
| 15.1(1)T | This command was modified. The version keyword was added with the 0 and 3 keywords to specify fax speed as G3 or SG3. |

| Command | Description |
|---|---|
| fax protocol (dial peer) | Specifies the fax protocol for a specific VoIP dial peer. |
| fax protocol (voice-service) | Specifies the global default fax protocol to be used for all VoIP dial peers. |
| fax protocol t38 (voice-service) | Specifies the global default ITU-T T.38 standard fax protocol to be used for all VoIP dial peers. |

| nse | (Optional) Uses network services engines (NSE) to switch to T.38 fax relay. |
|---|---|
| force | (Optional) Unconditionally, uses Cisco NSEs to switch to T.38 fax relay. This option allows T.38 fax relay to be used between
                                          Cisco H.323 or Session Initiation Protocol (SIP) gateways and Media Gateway Control Protocol (MGCP) gateways. |
| version { 0 \| 3 } | (Optional) Specifies a version for configuring fax speed: 0 --Configures version 0, which uses T.38 version 0 (1998--G3 faxing) 3 --Configures version 3, which uses T.38 version 3 (2004--V.34 or SG3 faxing) |
| ls - redundancy value | (Optional) (T.38 fax relay only) Specifies the number of redundant T.38 fax packets to be sent for the low-speed V.21-based
                                          T.30 fax machine protocol. Range varies by platform from 0 (no redundancy) to 5 or 7. For details, refer to command-line interface
                                          (CLI) help. Default is 0. |
| hs - redundancy value | (Optional) (T.38 fax relay only) Specifies the number of redundant T.38 fax packets to be sent for high-speed V.17, V.27,
                                          and V.29 T.4 or T.6 fax machine image data. Range varies by platform from 0 (no redundancy) to 2 or 3. For details, refer
                                          to the command-line interface (CLI) help. Default is 0. |
| fallback | (Optional) A fallback mode is used to transfer a fax across a VoIP network if T.38 fax relay could not be successfully negotiated
                                          at the time of the fax transfer. |
| cisco | (Optional) Cisco-proprietary fax protocol. |
| none | (Optional) No fax pass-through or T.38 fax relay is attempted. All special fax handling is disabled, except for modem pass-through
                                          if configured with the modem pass-through command. |
| pass - through | (Optional) The fax stream uses one of the following high-bandwidth codecs: g711ulaw --Uses the G.711 mu-law codec. g711alaw --Uses the G.711 a-law codec. |

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced. |
| 15.1(1)T | This command was Modified. The version keyword was added with the 0 and 3 keywords to specify fax speed. |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Note | Do not use the cisco keyword for the fallback option if you specified version 3 for SG3 fax transmission. |
|---|---|

| Command | Description |
|---|---|
| fax protocol (dial peer) | Specifies the fax protocol for a specific VoIP dial peer. |
| fax protocol (voice-service) | Specifies the global default fax protocol to be used for all VoIP dial peers. |
| fax protocol t38 (dial peer) | Specifies the ITU-T T.38 standard fax protocol to be used for a specific VoIP dial peer. |
| voice service voip | Enters voice-service configuration mode. |

| 2400 | 2400 bits per second (bps) fax transmission speed. |
|---|---|
| 4800 | 4800 bps fax transmission speed. |
| 7200 | 7200 bps fax transmission speed. |
| 9600 | 9600 bps fax transmission speed. |
| 12000 | 12000 bps fax transmission speed. |
| 14400 | 14400 bps fax transmission speed. |
| disable | Disables fax relay transmission capability. |
| voice | Highest possible transmission speed allowed by the voice rate. |
| bytes milliseconds | (Optional) Specifies fax packetization rate, in milliseconds. Range is 20 to 48. Default is 20. For Cisco fax relay, this keyword-argument pair is valid only on Cisco 2600 series, Cisco 3600 series, Cisco AS5300, and Cisco
                                                7200 series routers. For T.38 fax relay, this keyword-argument pair is valid only on Cisco AS5350, Cisco AS5400, and Cisco AS5850 routers. For
                                                other routers, the packetization rate for T.38 fax relay is fixed at 40 ms and cannot be changed. |

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced as the fax - rate command on the Cisco 3600. |
| 12.0(2)XH | The 12000 keyword was added. |
| 12.0(4)T | This command was integrated into Cisco IOS Release 12.0(4)T and implemented on the Cisco MC3810. |
| 12.1(3)T | The command name changed from fax - rate to fax rate (nonhyphenated). |
| 12.1(3)XI | This command was implemented on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.1(5)XM | This command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | The command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the following platforms: Cisco 1751, Cisco
                                          2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745. |
| 12.2(11)T | This command was implemented on the following platforms: Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850. |

| Note | The fax call is not compressed using the ip rtp header-compression command because User Datagram Protocol (UDP) is being used and not Real-Time Transport Protocol (RTP). For example, a 9600
                                          bps fax call takes approximately 24 kbps. |
|---|---|

| Tip | Because a large portion of the available network bandwidth is monopolized by the fax transmission, Cisco does not recommend
                                          setting the fax rate value higher than the value of the selected codec. If the fax rate value is set lower than the codec
                                          value, faxes take longer to send but use less bandwidth. |
|---|---|

| Command | Description |
|---|---|
| codec (dial peer) | Specifies the voice coder rate of speech for a dial peer. |
| fax protocol (dial peer) | Specifies the fax protocol for a specific VoIP dial peer. |

| disable | Disables fax-relay transmission capability. |
|---|---|
| system | Uses rate choice specified in global fax rate CLI under the voice service pots command. |
| voice | Highest possible transmission speed allowed by the voice rate for this dial peer. For example, if the voice codec is G.711,
                                          fax transmission may occur at a rate of up to 14,400 bps. |

| Release | Modification |
|---|---|
| 12.2(8)T | This command was introduced on the following platforms: Cisco 1700 series, Cisco 3600 series, and Cisco ICS 7750. |

| Command | Description |
|---|---|
| codec (dial peer) | Specifies the voice coder rate of speech for a dial peer. |
| fax rate (voip) | Establishes the rate at which a fax is sent to the specified VoIP dial peer. |

| disable | Disables fax relay transmission capability. |
|---|---|
| voice | Highest possible transmission speed allowed by the voice rate. For example, if the voice codec is G.711, fax transmission
                                          may occur at a rate of up to 14400 bps. |

| Release | Modification |
|---|---|
| 12.2(8)T | This command was introduced on the following platforms: Cisco 1700 series, Cisco 3600 series, and Cisco ICS 7750. |
| 12.3(4)T | This command was modified so that the "fax rate voice" setting is the default setting for the fax rate command in voice-service configuration mode and, hence, will no longer be displayed in the running configuration. |

| Note | Because the fax rate voice command has been reclassified as a default setting, it will no longer automatically generate an entry in your gateway router’s
                                          running configuration in NVRAM. If your gateway configuration requires fax rate voice command functionality, you must reconfigure your gateway after loading a Cisco IOS image earlier than Cisco IOS Release 12.3(4)T. |
|---|---|

| Command | Description |
|---|---|
| fax protocol (voice - service) | Specifies the global default fax protocol for all VoIP dial peers. |
| voice service | Specifies the voice encapsulation type. |

| $d$ | Wildcard that indicates that the information displayed is
                                          						captured from the configured destination pattern. |
|---|---|
| telephone-number | Destination telephone number. Valid entries are the plus
                                          						sign (+), numerals from 0 through 9, and the space character. This string can
                                          						specify an E.164 telephone number; if you choose to configure an E.164
                                          						telephone number, you must use the plus sign as the first character. |

| Release | Modification |
|---|---|
| 12.0(4)XJ | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release
                                          						12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on following platforms: Cisco
                                          						1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745. |

| ans-disable | Suppresses ANS tones at originating SG3 fax machines so that the SG3 fax machines can operate at G3 speeds using fax relay. |
|---|---|
| ans-treatment | Enables modem and fax answer tone treatment. |
| ecm-disable | Disables fax-relay ECM on a VoIP dial peer. |
| sg3-to-g3 | Enables SG3 machines to negotiate to G3 speeds using fax relay. |
| system | (Optional) The protocol set to be used in the voice-service configuration mode. |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced as the fax-relay ecm-disable command. |
| 12.1(5)XM | This command was integrated into Cisco IOS Release 12.1(5)XM and implemented on the Cisco AS5800 Series Universal Gateways. |
| 12.1(5)XM2 | This command was integrated into Cisco IOS Release 12.1(5)XM2 and implemented on the Cisco AS5350 and Cisco AS5400 Series
                                          Universal Gateways. |
| 12.2(2)XB1 | This command was integrated into Cisco IOS Release 12.2(2)XB1 and implemented on the Cisco AS5850 Series Universal Gateways. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |
| 12.4(4)T | This command was modified. The sg3-to-g3 system keyword and argument pair was added. |
| 12.4(6)T | This command was integrated into Cisco IOS Release 12.4(6)T and implemented on Cisco 1700 and Cisco 2800 Series routers. |
| 12.4(20)T1 | This command was modified. The ans-disable keyword was added to support the suppression of ANS tones from reaching the SG3 fax machines, thereby enabling the SG3 fax
                                          machines to negotiate to G3 speeds. |
| 15.1(4)M | This command was modified. The ans-treatment keyword was added to support the modem and fax ANS tone treatment. |

| Command | Description |
|---|---|
| dtmf-relay (Voice over IP) | Forwards dual tone multifrequency tones by using RTP with the NTE payload type. |
| fax-relay (voice-service) | Allows ANS tones to be disabled for SG3 machines to operate at G3 speeds using fax relay, enables ANS tone treatment, or
                                          enables the fax stream between two SG3 fax machines to negotiate to G3 speeds on a VoIP dial peer. |
| mgcp fax-relay | Allows ANS tones to be disabled for SG3 machines to operate at G3 speeds for MGCP fax relay or enables the fax stream between
                                          two SG3 fax machines to negotiate down to G3 speeds for MGCP fax relay. |
| modem passthrough (Dial-peer) | Enables fax or modem pass-through over VoIP for a specific dial peer. |

| ans-disable | Suppresses ANS tones at originating SG3 fax machines so that the SG3 fax machines can operate at G3 speeds using fax relay. |
|---|---|
| ans-treatment | Enables modem and fax answer tone treatment. |
| sg3-to-g3 | Enables SG3 machines to negotiate to G3 speeds using fax relay. |

| Release | Modification |
|---|---|
| 12.4(4)T | This command was introduced as the fax-relay sg3-to-g3 command. |
| 12.4(6)T | This command was integrated into Cisco IOS Release 12.4(6)T and implemented on Cisco 1700 and Cisco 2800 Series routers. |
| 12.4(20)T | This command was modified. The ans-disable keyword was added to support the suppression of ANS tones from reaching the SG3 fax machines, thereby enabling the SG3 fax
                                          machines to negotiate to G3 speeds. |
| 15.1(4)M | This command was modified. The ans-treatment keyword was added to support the modem and fax ANS tone treatment. |

| Command | Description |
|---|---|
| dtmf-relay (Voice over IP) | Forwards dual tone multifrequency tones by using RTP with the NTE payload type. |
| fax-relay (dial-peer) | Allows ANS tones to be disabled for SG3 machines to operate at G3 speeds using fax relay, enables ANS tone treatment, disables
                                          fax-relay ECM on a VoIP dial peer, or enables the fax stream between two SG3 fax machines to negotiate to G3 speeds on a VoIP
                                          dial peer. |
| mgcp fax-relay | Allows ANS tones to be disabled for SG3 machines to operate at G3 speeds for MGCP fax relay or enables the fax stream between
                                          two SG3 fax machines to negotiate to G3 speeds for MGCP fax relay. |
| modem passthrough (Voice-service) | Enables fax or modem pass-through over VoIP globally for all dial peers. |

| $a$ | Wildcard that inserts the date in the selected position. |
|---|---|
| $d$ | Wildcard that inserts the destination address in the
                                          						selected position. |
| $p$ | Wildcard that inserts the page count in the selected
                                          						position. |
| $s$ | Wildcard that inserts the sender’s address in the selected
                                          						position. |
| $t$ | Wildcard that inserts the transmission time in the selected
                                          						position. |
| string | Text string that provides personalized information. Valid
                                          						characters are any text plus wildcards--for example, Time:$t$. There is no
                                          						default. |

| Release | Modification |
|---|---|
| 12.0(4)XJ | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release
                                          						12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the following platforms:
                                          						Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745. |

| Note | Faxed header information cannot be converted from TIFF files to
                                          		  standard fax transmissions. |
|---|---|

| Note | If the information you have selected for the fax send center - header command
                                          		  exceeds the space allocated for the center fax header, the information is
                                          		  truncated. |
|---|---|

| Command | Description |
|---|---|
| fax send left - header | Specifies the data that appears on the left in the fax
                                          						header. |
| fax send right - header | Specifies the data that appears on the right in the fax
                                          						header. |

| string | Text string that adds customized text in the title field of the fax cover sheet. Valid characters are any ASCII characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(4)XJ | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and implemented on the following platforms: Cisco 1751, Cisco
                                          2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745. |

| Command | Description |
|---|---|
| fax send coverpage e - mail - controllable | Controls the cover page generation on a per-recipient basis, based on the information contained in the destination address
                                          of the e-mail message. |
| fax send coverpage enable | Generates fax cover sheets. |
| fax send coverpage show - detail | Prints all of the e-mail header information as part of the fax cover sheet. |

| Release | Modification |
|---|---|
| 12.0(4)XJ | This command was introduced on the Cisco AS5300 universal access server. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750 access router. |
| 12.2(8)T | This command was implemented on the following platforms: Cisco 1751, Cisco 2600, Cisco 3600 series, Cisco 3725, and Cisco
                                          3745. |

| To: Field Entries | Description |
|---|---|
| FAX=+1-312-555-3260@fax.com | Fax sent to an E.164-compliant long distance telephone number in the United States. If the fax coverpage enable command is entered, store-and-forward fax generate a fax cover page. |
| FAX=+1-312-555-3260/cover=no@fax.com | Fax sent to an E.164-compliant long distance telephone number in the United States. In this example, the fax send coverpage enable command is superseded by the cover=no statement. No cover page is generated. |
| FAX=+1-312-555-3260/cover=yes@fax.com | Fax sent to an E.164-compliant long distance telephone number in the United States. In this example, the fax send coverpage enable command is superseded by the cover=yes statement. Store-and-forward fax generates a fax cover page. |

| Note | This command applies to off-ramp store-and-forward fax functions. |
|---|---|

| Command | Description |
|---|---|
| fax send coverpage comment | Defines customized text for the title field of a fax cover sheet. |
| fax send coverpage enable | Generates fax cover sheets. |
| fax send coverpage show - detail | Prints all the e-mail header information as part of the fax cover sheet. |

| Release | Modification |
|---|---|
| 12.0(4)XJ | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the following platforms: Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and
                                          Cisco 3745. |

| Note | This command is applicable only to faxes that were converted to e-mail messages. The Cisco AS5300 universal access server
                                          does not alter fax TIFF attachments. Therefore you cannot use this command to enable the Cisco AS5300 to generate fax cover
                                          pages for faxes that are converted from TIFF files to standard fax transmissions. |
|---|---|

| Command | Description |
|---|---|
| fax send coverpage comment | Defines customized text for the title field of a fax cover sheet. |
| fax send coverpage e - mail - controllable | Defers to the cover page setting in the e-mail header to generate a standard fax cover sheet |
| fax send coverpage show - detail | Prints all the e-mail header information as part of the fax cover sheet. |

| Release | Modification |
|---|---|
| 12.0(4)XJ | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the following platforms: Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and
                                          Cisco 3745. |

| Note | This command is applicable only to faxes that are converted to e-mail messages. The Cisco AS5300 universal access server does
                                          not alter fax TIFF attachments. Therefore, you cannot use this command to enable the Cisco AS5300 to display additional fax
                                          cover page information for faxes that are converted from TIFF files to standard fax transmissions. |
|---|---|

| Command | Description |
|---|---|
| fax send coverpage comment | Defines customized text for the title field of a fax cover sheet. |
| fax send coverpage e - mail - controllable | Defers to the cover page setting in the e-mail header to generate a standard fax cover sheet. |
| fax send coverpage enable | Generates fax cover sheets. |

| $a$ | Wildcard that inserts the date in the selected position. |
|---|---|
| $d$ | Wildcard that inserts the destination address in the
                                          						selected position. |
| $p$ | Wildcard that inserts the page count in the selected
                                          						position. |
| $s$ | Wildcard that inserts the sender’s address in the selected
                                          						position. |
| $t$ | Wildcard that inserts the transmission time in the selected
                                          						position. |
| string | Text string that provides customized information. Valid
                                          						characters are any combination of ASCII characters and the wildcards listed
                                          						above. |

| Release | Modification |
|---|---|
| 12.0(4)XJ | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release
                                          						12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the following platforms:
                                          						Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745. |

| Command | Description |
|---|---|
| fax send center-header | Specifies the data that appears in the center of the fax
                                          						header. |
| fax send right-header | Specifies the data that appears on the right in the fax
                                          						header. |

| 2400 | Transmission speed of 2400 bits per second (bps). |
|---|---|
| 4800 | Transmission speed of 4800 bps. |
| 7200 | Transmission speed of 7200 bps. |
| 9600 | Transmission speed of 9600 bps. |
| 12000 | Transmission speed of 12,000 bps. |
| 14400 | Transmission speed of 14,400 bps. This is the default. |

| Release | Modification |
|---|---|
| 12.0(4)XJ | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the following platforms: Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and
                                          Cisco 3745. |

| $a$ | Wildcard that inserts the date in the selected position. |
|---|---|
| $d$ | Wildcard that inserts the destination address in the
                                          						selected position. |
| $p$ | Wildcard that inserts the page count in the selected
                                          						position. |
| $s$ | Wildcard that inserts the sender address in the selected
                                          						position. |
| $t$ | Wildcard that inserts the transmission time in the selected
                                          						position. |
| string | Text string that provides customized information. Valid
                                          						characters are any combination of ASCII characters and the wildcards listed
                                          						above. |

| Release | Modification |
|---|---|
| 12.0(4)XJ | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release
                                          						12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the following platforms:
                                          						Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745. |

| Note | If the information you select for the fax send right - header command exceeds the space allocated for the right fax header,
                                          		  the information is truncated. |
|---|---|

| Command | Description |
|---|---|
| fax send center - header | Specifies the data that appears in the center in the fax
                                          						header. |
| fax send left - header | Specifies the data that appears on the left in the fax
                                          						header. |

| $s$ | Wildcard that inserts the sender name from the RFC 822
                                          						header (captured by the on-ramp device from the sending fax machine) in the
                                          						selected position. |
|---|---|
| string | Originating telephone number. Valid entries are the plus
                                          						sign (+), numerals from 0 through 9, and the space character. This string can
                                          						specify an E.164 telephone number; if you choose to configure an E.164
                                          						telephone number, you must use the plus sign as the first character. |

| Release | Modification |
|---|---|
| 12.0(4)XJ | This command was introduced on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release
                                          						12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the following platforms:
                                          						Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745. |

| with-close | Call records are appended to the accounting file and the file is closed. |
|---|---|
| without-close | Call records are appended to the accounting file and the file remains open. |

| Release | Modification |
|---|---|
| 12.4(15)XY | This command was introduced. |
| 12.4(20)T | This command was integrated into Cisco IOS Release 12.4(20)T. |

| Command | Description |
|---|---|
| gw-accounting | Enables an accounting method for collecting CDRs. |
| maximum buffer-size | Sets the maximum size of the file accounting buffer. |
| maximum cdrflush-timer | Sets the maximum time to hold call records in the buffer before appending the records to the accounting file. |
| maximum fileclose-timer | Sets the maximum time for saving records to an accounting file before closing the file and creating a new one. |
| primary | Sets the primary location for storing the CDRs generated for file accounting. |
| secondary | Sets the backup location for storing CDRs if the primary location becomes unavailable. |

| Release | Modification |
|---|---|
| 12.4(15)XY | This command was introduced. |
| 12.4(20)T | This command was integrated into Cisco IOS Release 12.4(20)T. |

| Command | Description |
|---|---|
| gw-accounting | Enables an accounting method for collecting CDRs. |
| maximum retry-count | Sets the maximum number of times the router attempts to connect to the primary file device before switching to the secondary
                                          device |
| primary | Sets the primary location for storing the CDRs generated for file accounting. |
| secondary | Sets the backup location for storing CDRs if the primary location becomes unavailable. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| aaa preauth | Enters AAA preauthentication configuration mode. |

| with-close | Enables file accounting flush pending accounting to the file, and closes the file when the process is complete. |
|---|---|
| without-close | Enables file accounting flush pending accounting to file. |

| Release | Modification |
|---|---|
| 15.0(1)M | This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M. |

| Command | Description |
|---|---|
| maximum cdrflush-timer | Sets the maximum time to hold call records in the buffer before appending the records to the accounting file. |

| string | fmtp:payload type name1= val1; name2 = val2... |
|---|---|

| Release | Modification |
|---|---|
| 12.4(22)T | This command was introduced. |

| Command | Description |
|---|---|
| clock-rate | Sets the clock rate for the codec. |

| Release | Modification |
|---|---|
| 12.0(7)XR | This command was introduced. |
| 12.1(1)T | This command was integrated into Cisco IOS Release 12.1(1)T. |

| num - digit | The number of digits to be forwarded. If the number of digits is greater than the length of a destination phone number, the
                                          length of the destination number is used. Range is 0 to 32. Setting the value to 0 is equivalent to entering the no forward - digits command. |
|---|---|
| all | Forwards all digits. If all is entered, the full length of the destination pattern is used. |
| extra | If the length of the dialed digit string is greater than the length of the dial-peer destination pattern, the extra right-justified
                                          digits are forwarded. However, if the dial-peer destination pattern is variable length ending with the character "T" (for
                                          example: T, 123T, 123...T), extra digits are not forwarded. |

| Release | Modification |
|---|---|
| 11.3(1)MA | This command was introduced on the Cisco MC3810. |
| 12.0(2)T | This command was integrated into Cisco IOS Release 12.0(2)T. The implicit option keyword was added. |
| 12.0(4)T | This command was modified to support ISDNBF PRI QSIG signaling calls. |
| 12.0(7)XK | This command was implemented on the Cisco 2600 series and Cisco 3600 series. The implicit keyword was removed and the extra keyword was added. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |

| Command | Description |
|---|---|
| destination-pattern | Defines the prefix or the full E.164 telephone number to be used for a dial peer. |
| show dial-peer voice | Displays configuration information for dial peers. |

| bits-per-second | Bandwidth, in bits per second (bps), reserved for voice traffic for the specified map class. Range is from 8000 to 45000000.
                                          Default is 0, which disables voice calls. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(3)XG | This command was introduced on the following platforms: Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, and Cisco
                                          MC3810. |
| 12.0(4)T | This command was integrated into Cisco IOS Release 12.0(4)T. |
| 12.0(5)T | The queue depth keyword and argument were added. |
| 12.2(1) | The queue depth keyword and argument were removed. |

| Note | Cisco strongly recommends that you set voice bandwidth to a value less than the committed information rate (CIR) if Frame
                                          Relay traffic shaping is configured. Cisco also strongly recommends that you set the minimum CIR (using the frame - relay mincir command) to be at least equal to or greater than the voice bandwidth. |
|---|---|

| Codec | Codec Bandwidth | Voice Frame Payload Size | Required Bandwidth per Call (6-Byte OH) | Required Bandwidth per Call (8-Byte OH) |
|---|---|---|---|---|
| G.729 | 8000 bps | 120 bytes | 8400 bps | 8534 bps |
| G.729 | 8000 bps | 80 bytes | 8600 bps | 8800 bps |
| G.729 | 8000 bps | 40 bytes | 9200 bps | 9600 bps |
| G.729 | 8000 bps | 30 bytes | 9600 bps | 10134 bps |
| G.729 | 8000 bps | 20 bytes | 10400 bps | 11200 bps |

| Command | Description |
|---|---|
| codec (dial-peer) | Specifies the voice coder rate of speech for a VoFR dial peer. |
| frame-relay fair-queue | Enables weighted fair queueing for one or more Frame Relay PVCs. |
| frame-relay fragment | Enables fragmentation for a Frame Relay map class. |
| frame-relay interface-dlci | Assigns a DLCI to a specified Frame Relay subinterface on the router or access server. |
| frame-relay mincir | Assigns the minimum CIR for Frame Relay traffic shaping. |
| map-class frame-relay | Specifies a map class to define QoS values for an SVC. |

| time | Maximum number of 10-millisecond time intervals by which the two frequencies in a tone may differ from each other and be detected.
                                          Range is from 10 to 100 (100 milliseconds to 1 second). Default is 10 (100 milliseconds). |
|---|---|

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was implemented on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 1750. |

| Command | Description |
|---|---|
| dualtone | Defines the tone and cadence for a custom call-progress tone. |
| freq-pair | Specifies the frequency components of a tone to be detected. |
| supervisory answer dualtone | Enables answer supervision on a voice port. |
| voice class dualtone | Creates a voice class for FXO tone detection parameters. |

| hertz | Maximum cycles per second (Hz) by which tone frequencies may deviate from the configured frequencies and be detected. The
                                          value applies to both frequencies of a dual tone. Range is from 10 to 125. The default is 10. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was implemented on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 1750. |

| Command | Description |
|---|---|
| dualtone | Defines the tone and cadence for a custom call-progress tone. |
| freq-pair | Specifies the frequency components of a tone to be detected. |
| supervisory answer dualtone | Enables answer supervision on a voice port. |
| supervisory dualtone-detect-params | Assigns the boundary and detection tolerance parameters to a voice port. |
| voice class dualtone | Creates a voice class for FXO tone detection parameters. |

| dBm0 | Upper limit of the tone power that is detected, in dBm0 (where dBm0 is decibels referred to one milliwatt and corrected to
                                          a 0-dBm effective power level). Range is from 0 to -20. The default is -10. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was implemented on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 1750. |

| Command | Description |
|---|---|
| dualtone | Defines the tone and cadence for a custom call-progress tone. |
| freq-pair | Specifies the frequency components of a tone to be detected. |
| supervisory answer dualtone | Enables answer supervision on a voice port. |
| supervisory dualtone-detect-params | Assigns the boundary and detection tolerance parameters defined by the voice class dualtone - detect - params command to a voice port. |
| voice class dualtone | Creates a voice class for FXO tone detection parameters. |

| dBm0 | Lower limit of tone power that is detected, in dBm0 (where dBm0 is decibels referred to one milliwatt and corrected to a 0-dBm
                                          effective power level). Range is from -10 to -35. The default is -30. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was implemented on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 1750. |

| Command | Description |
|---|---|
| dualtone | Defines the tone and cadence for a custom call-progress tone. |
| freq-pair | Specifies the frequency components of a tone to be detected. |
| supervisory answer dualtone | Enables answer supervision on a voice port. |
| supervisory dualtone-detect-params | Assigns the boundary and detection tolerance parameters to a voice port. |
| voice class dualtone | Creates a voice class for FXO tone detection parameters. |

| tone-id | Tag identifier for a tone to be detected. Range is from 1 to 16. There is no default. |
|---|---|
| frequency-1 | One frequency component of the tone to be detected, in Hz. Range is from 300 to 3600. There is no default. |
| frequency-2 | A second frequency component of the tone to be detected, in Hz. Range is frm 300 to 3600, or you can specify 0. There is no
                                          default. |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |

| Command | Description |
|---|---|
| frag-pre-queuing | Specifies the maximum timing difference allowed between the two frequencies for detection of a tone. |
| freq-max-deviation | Specifies the maximum frequency deviation allowed in a tone. |
| freq-max-power | Specifies the upper limit of the tone power allowed in a tone. |
| freq-min-power | Specifies the lower limit of the tone power allowed in a tone. |
| freq-power-twist | Specifies the power difference allowed between the two frequencies of a tone. |
| voice class dualtone | Creates a voice class for FXO tone detection parameters. |

| dBm0 | Maximum power difference allowed between the two frequencies of a tone, in dBm0 (where dBm0 is decibels referred to one milliwatt
                                          and corrected to a 0-dBm effective power level). Range is from 0 to 15. The default is 6. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was implemented on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 1750. |

| Command | Description |
|---|---|
| dualtone | Defines the tone and cadence for a custom call-progress tone. |
| freq-pair | Specifies the frequency components of a tone to be detected. |
| supervisory answer dualtone | Enables answer supervision on a voice port. |
| supervisory dualtone-detect-params | Assigns the boundary and detection tolerance parameters defined by the voice class dualtone-detect-params command to a voice port. |
| voice class dualtone | Creates a voice class for FXO tone detection parameters. |

| frequency - 1 | One frequency component of the tone to be detected, in Hz. Range is from 300 to 3600. The default is 300. |
|---|---|
| frequency - 2 | (Optional) A second frequency component of the tone to be detected, in Hz. Range is from 300 to 3600 or you can specify 0.
                                          The default is that no second frequency component is detected. |

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced on the following platforms: Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 1750. |

| Command | Description |
|---|---|
| supervisory custom-cptone | Associates a class of custom call-progress tones with a voice port. |
| voice class custom-cptone | Creates a voice class for defining custom call-progress tones. |
| voice class dualtone-detect-params | Modifies the boundaries and limits for custom call-progress tones defined by the voice class custom-cptone command. |