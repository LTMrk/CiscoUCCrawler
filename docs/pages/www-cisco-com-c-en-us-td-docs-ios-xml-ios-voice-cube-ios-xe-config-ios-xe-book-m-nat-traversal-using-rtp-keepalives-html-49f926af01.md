---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-nat-traversal-using-rtp-keepalives-html-49f926af01
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m-nat-traversal-using-rtp-keepalives.html
retrieved_at: 2026-08-16T15:51:23.744831+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: NAT Traversal using RTP Keepalive

## Chapter: NAT Traversal using RTP Keepalive

# NAT Traversal using RTP Keepalive

## Information about NAT Traversal using Media Keepalives

Network Address Translation (NAT) allows multiple hosts to connect to the internet using a single public IP address. However,
                           for voice calls, NAT bindings must be constantly maintained to ensure uninterrupted media transmission using a keepalive mechanism.
                           Therefore, establishing communication between hosts with NAT-based routers can become challenging. In certain call scenarios,
                           when calls are redirected back to the IP-based Public Switched Telephone Network (PSTN), it's possible that no audio or media
                           is detected. This occurs when both parties involved in the call are located outside of the NAT environment.

Using the media keepalive feature, CUBE deployed behind NAT can send empty media keepalive packets. An empty media keepalive
                           packet refers to a media packet that doesn't contain any payload but only includes the RTP headers. These packets serve the
                           purpose of maintaining the NAT bindings and allowing the peer entity outside of the NAT to perform the media latching required
                           to establish bidirectional media flow. Media latching refers to the method of using the Natted IP address and port of incoming
                           packets as the destination for the packets transmitted in the reverse direction. This feature enables media latching as a
                           solution for NAT traversal without the need for STUN.

CUBE sends periodic media keepalive packets in separate and independent streams, without merging with the negotiated media
                           streams. This approach ensures that the keepalive packets don't interfere with the existing media stream established during
                           the call, allowing for reliable detection of connectivity and end to end media integrity.

Periodic media keepalive packets keep pinholes open to allow media communication between the calling party and the connected
                           party. CUBE sends keepalive packets at regular intervals to maintain the NAT bindings for the media. When initially receiving
                           packets from the NAT router, the external network associates the public IP address with the source IP and port. Subsequent
                           media packets are then sent to this associated IP and port. CUBE triggers media keepalive packets without altering the media
                           stream, ensuring the flow of media communication.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

NAT Traversal using Media Keepalives

Cisco IOS XE Dublin 17.12.2

Cisco IOS XE  17.13.1a

This feature enables the CUBE to periodically send media keepalive packets, which helps maintain open pinholes and ensures
                                          the necessary network bindings for media transmission in a NAT environment.

### Media Keepalive Characteristics

The following are the CUBE characteristics for NAT traversal functionality using media keepalive:

CUBE sends media keepalive packets for each media stream, irrespective of the stream's activity status (inactive, send only,
                                    recv only, or sendrecv)

CUBE triggers RTP and RTCP keepalive packets for the negotiated media streams.

Supports only audio and video media types

Supports media keepalive feature with High Availability (HA) deployments

## Restrictions

The following are not supported with NAT media keepalive feature:

Not supported for IPv6 destinations.

Not supported for image or application m-lines.

## Configure NAT Traversal using Media Keepalive

NAT traversal media keepalive configuration is applicable to the three configurations, listed here in order of preference:

Dial-peer configuration

Tenant configuration

Global configuration

### Configure NAT Media Keepalive at the Dial Peer Level

### SUMMARY STEPS

- configure terminal

- dial-peer voice tag voip

- voice-class sip nat media-keepalive interval

- exit

### DETAILED STEPS

Step 1

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 2

dial-peer voice tag voip

#### Example:

```
Device(config)# dial-peer voice 999 voip
```

Defines a particular dial peer, specifies the method of voice encapsulation, and enters dial peer configuration mode.

Step 3

voice-class sip nat media-keepalive interval

#### Example:

```
Device(config-dial-peer)# voice-class sip nat media-keepalive 40
```

#### Example:

```
Device(config-dial-peer)# voice-class sip nat media-keepalive
```

Enables media keepalive allowing media keepalive packets to be transmitted for the specified interval of time (in seconds).
                                             Range is 1–50. Default value is 10.

In the default configuration, no value is specified and keepalive interval is set to 10.

Step 4

exit

#### Example:

```
Device(config-dial-peer)# exit
```

Exits dial peer configuration mode and returns to global configuration mode.

### Configure NAT Media Keepalive at the Tenant Level

### SUMMARY STEPS

- configure terminal

- voice class tenant tag

- nat media-keepalive interval

- end

### DETAILED STEPS

Step 1

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 2

voice class tenant tag

#### Example:

```
Device(config)# voice class tenant 1
```

Associates a dial-peer with a specific tenant configuration.

Step 3

nat media-keepalive interval

#### Example:

```
Device(config-class)# nat media-keepalive 35
```

Enables media keepalive packets transmission for the specified interval of time (in seconds) at tenant level. Range is 1–50.
                                             Default value is 10.

Step 4

end

#### Example:

```
Device(config-dial-peer)# end
```

Returns to privileged EXEC mode.

### Configure NAT Media Keepalive at the Global Level

### SUMMARY STEPS

- configure terminal

- voice service voip

- sip

- nat media-keepalive interval

- end

### DETAILED STEPS

Step 1

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 2

voice service voip

#### Example:

```
Device(config)# voice service voip
```

Enters voice-service configuration mode and Voice over IP (VoIP) encapsulation type.

Step 3

sip

#### Example:

```
Device(config-voi-serv)# sip
```

Enters the Session Initiation Protocol (SIP) configuration mode.

Step 4

nat media-keepalive interval

#### Example:

```
Device(config-serv-sip)# nat media-keepalive 20
```

Enables media keepalive packets transmission for the specified interval of time (in seconds) at global level. Range is 1–50.
                                             Default value is 10.

Step 5

end

#### Example:

```
Device(config-serv-sip)# end
```

Returns to privileged EXEC mode.

## Verify NAT Traversal using Media Keepalive Configuration

Use the following show commands to verify NAT media keepalive configurations at dial-peer level, tenant level, and global level configurations.
                              You can enter the show commands in any order.

### SUMMARY STEPS

- show run | sec dial-peer voice tag voip

- show run | sec voice class tenant tag

- show run | sec voice service voip

- show running-config all | sec media-keepalive

### DETAILED STEPS

Step 1

show run | sec dial-peer voice tag voip

### Example:

```
Device# show run | sec dial-peer voice 999 voip

dial-peer voice 999 voip
 voice-class sip nat media-keepalive 40
```

The following sample output displays the NAT media keepalive for dial-peer configuration:

Step 2

show run | sec voice class tenant tag

### Example:

```
Device# show run | sec voice class tenant 1

voice class tenant 1
 nat media-keepalive 45
```

The following sample output displays the NAT media keepalive for tenant configuration:

Step 3

show run | sec voice service voip

### Example:

```
Device# show run | sec voice service voip

voice service voip
 sip
  nat media-keepalive 30
```

The following sample output displays NAT media keepalive for global configuration:

Step 4

show running-config all | sec media-keepalive

### Example:

```
Device# show running-config all | sec media-keepalive
 nat media-keepalive 45
 nat media-keepalive 30
 voice-class sip nat media-keepalive 40
```

The following sample output displays the NAT media keepalive for all the configurations:

## Configuration Example

### Dial-peer level configuration

```
dial-peer voice 644 voip
 session protocol sipv2 voice-class sip nat media-keepalive codec g711ulaw
```

### Global level configuration

```
voice service voip
 sip nat media-keepalive
```

### Tenant level configuration

```
voice class tenant 1 nat media-keepalive !
dial-peer voice 645 voip
 session protocol sipv2 voice-class sip tenant 1 codec g711ulaw
```

| Feature Name | Releases | Feature Information |
|---|---|---|
| NAT Traversal using Media Keepalives | Cisco IOS XE Dublin 17.12.2 Cisco IOS XE  17.13.1a | This feature enables the CUBE to periodically send media keepalive packets, which helps maintain open pinholes and ensures
                                          the necessary network bindings for media transmission in a NAT environment. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 2 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 999 voip | Defines a particular dial peer, specifies the method of voice encapsulation, and enters dial peer configuration mode. |
| Step 3 | voice-class sip nat media-keepalive interval Example: Device(config-dial-peer)# voice-class sip nat media-keepalive 40 Example: Device(config-dial-peer)# voice-class sip nat media-keepalive | Enables media keepalive allowing media keepalive packets to be transmitted for the specified interval of time (in seconds).
                                             Range is 1–50. Default value is 10. Note In the default configuration, no value is specified and keepalive interval is set to 10. | Note | In the default configuration, no value is specified and keepalive interval is set to 10. |
| Note | In the default configuration, no value is specified and keepalive interval is set to 10. |
| Step 4 | exit Example: Device(config-dial-peer)# exit | Exits dial peer configuration mode and returns to global configuration mode. |

| Note | In the default configuration, no value is specified and keepalive interval is set to 10. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 2 | voice class tenant tag Example: Device(config)# voice class tenant 1 | Associates a dial-peer with a specific tenant configuration. |
| Step 3 | nat media-keepalive interval Example: Device(config-class)# nat media-keepalive 35 | Enables media keepalive packets transmission for the specified interval of time (in seconds) at tenant level. Range is 1–50.
                                             Default value is 10. |
| Step 4 | end Example: Device(config-dial-peer)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 2 | voice service voip Example: Device(config)# voice service voip | Enters voice-service configuration mode and Voice over IP (VoIP) encapsulation type. |
| Step 3 | sip Example: Device(config-voi-serv)# sip | Enters the Session Initiation Protocol (SIP) configuration mode. |
| Step 4 | nat media-keepalive interval Example: Device(config-serv-sip)# nat media-keepalive 20 | Enables media keepalive packets transmission for the specified interval of time (in seconds) at global level. Range is 1–50.
                                             Default value is 10. |
| Step 5 | end Example: Device(config-serv-sip)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | show run \| sec dial-peer voice tag voip Example: Device# show run \| sec dial-peer voice 999 voip

dial-peer voice 999 voip
 voice-class sip nat media-keepalive 40 | The following sample output displays the NAT media keepalive for dial-peer configuration: |
| Step 2 | show run \| sec voice class tenant tag Example: Device# show run \| sec voice class tenant 1

voice class tenant 1
 nat media-keepalive 45 | The following sample output displays the NAT media keepalive for tenant configuration: |
| Step 3 | show run \| sec voice service voip Example: Device# show run \| sec voice service voip

voice service voip
 sip
  nat media-keepalive 30 | The following sample output displays NAT media keepalive for global configuration: |
| Step 4 | show running-config all \| sec media-keepalive Example: Device# show running-config all \| sec media-keepalive
 nat media-keepalive 45
 nat media-keepalive 30
 voice-class sip nat media-keepalive 40 | The following sample output displays the NAT media keepalive for all the configurations: |