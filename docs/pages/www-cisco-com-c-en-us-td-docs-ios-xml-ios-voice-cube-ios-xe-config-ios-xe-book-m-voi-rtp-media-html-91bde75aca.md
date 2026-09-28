---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-rtp-media-html-91bde75aca
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-rtp-media.html
retrieved_at: 2026-08-16T15:51:53.117823+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Configuring RTP Media Loopback for SIP Calls

## Chapter: Configuring RTP Media Loopback for SIP Calls

# Configuring RTP Media Loopback for SIP Calls

RTP packets are looped back toward the source device when the RTP Media Loopback for SIP Calls feature is configured on a
                        dial peer. The SIP RTP media loopback can be used during Cisco UBE deployments to make test calls to verify the media path
                        between the endpoints and Cisco UBE. In a voice loopback call, an echo is heard at the device originating the call. In a video
                        loopback call, the locally captured video and the audio echo must be rendered at the source device.

## Feature Information for RTP Media Loopback for SIP Calls

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

RTP Media Loopback for SIP Calls

Baseline Functionality

RTP packets are looped back toward the source when the RTP Media Loopback for SIP Calls feature is configured on a dial peer.
                                          SIP RTP media loopback helps in verifying the media path between the device originating the call and the intermediate device.

## Prerequisites

Media packets must be enabled to pass through the gateway.

Use the media flow-through command in dial peer voice or voice service configuration mode to enable the media packets.

Cisco Unified Border Element

Cisco IOS Release 15.1(4)M or a later release must be installed and running on your Cisco Unified Border Element.

Cisco Unified Border Element (Enterprise)

Cisco IOS XE Release 3.3S or a later release must be installed and running on your Cisco ASR 1000 Series Router.

## Restrictions

SRTP, DTLS, and STUN are not supported in loopback mode.

Fax (midcall transmit function change) is not supported.

RSVP is not supported.

Call transfer is not supported.

## Information About RTP Media Loopback for SIP Calls

Digital Signal Processors (DSP) generate and transmit Real-time Transport Protocol (RTP) media packets from a source to a
                           destination transport address during a SIP call session. However, when a SIP call is put on hold the DSP stops generating
                           the RTP media packets and resumes generating and transmitting these media packets after the SIP call is resumed. This ensures
                           that the RTP sequence number is continuous from the time of the origin to the end of a SIP call.

## How to Configure RTP Media Loopback for SIP Calls

RTP packets are looped back toward the source device when the RTP Media Loopback for SIP Calls feature is configured on a
                              dial peer. Perform this task to enable the RTP Media Loopback for SIP Calls feature on a dial peer.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- destination-pattern string

- session protocol sipv2

- session target loopback:rtp

- incoming called-number string

- exit

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

dial-peer voice tag voip

### Example:

```
Router(config)# dial-peer voice 77 voip
```

Specifies that the dial peer is a VoIP peer and enters dial peer voice configuration mode.

Step 4

destination-pattern string

### Example:

```
Router(config-dial-peer)# destination-pattern 77
```

Specifies the prefix or the full E.164 number for the dial peer.

Step 5

session protocol sipv2

### Example:

```
Router(config-dial-peer)# session protocol sipv2
```

Specifies the session protocol for calls with the SIP option.

Step 6

session target loopback:rtp

### Example:

```
Router(config-dial-peer)# session target loopback:rtp
```

Designates a network-specific address to receive calls from a VoIP dial peer and configures all voice data to loop back to
                                          the source.

Step 7

incoming called-number string

### Example:

```
Router(config-dial-peer)# incoming called-number 77
```

Specifies a digit string that can be matched by an incoming call to associate the call with the dial peer.

Step 8

exit

### Example:

```
Router(config-dial-peer)# exit
```

Exits dial peer voice configuration mode and enters global configuration mode.

## Configuration Examples for RTP Media Loopback

### Example: Configuring Video Loopback with Cisco Telepresence System

The following sample output shows Media Loopback for SIP Calls configured on a Cisco Telepresence System (CTS).

```
!
codec profile 1 aacld 
 fmtp "fmtp:96 profile-level-id=16;streamtype=5;mode=AAChbr;config=B98C00;sizeLength=13;indexLength=3;indexDeltaLength=3;constantDura
tion=480"
!
codec profile 2 h264
 fmtp "fmtp:112 profile-level-id=4D0028;sprop-parametersets=
R00AKAmWUgDwBDyA,SGE7jyA=;packetization-mode=1"
!
voice class codec 4
 codec preference 1 aacld profile 1
 video codec h264 profile 2
!
dial-peer voice 2000 voip
 destination-pattern 2000
 rtp payload-type cisco-codec-fax-ind 110
 rtp payload-type cisco-codec-aacld 96
 rtp payload-type cisco-codec-video-h264 112
 session protocol sipv2
 session target loopback:rtp
 incoming called-number 2000
 voice-class codec 4
 voice-class sip bandwidth audio tias-modifier 64000
 voice-class sip bandwidth video tias-modifier 4500000
!
```

### Example: Configuring Video Loopback with Cisco Unified Video Advantage

The following sample output shows Media Loopback for SIP Calls configured on a Cisco Unified Video Advantage (CUVA).

```
!
codec profile 3 h264
 fmtp "fmtp:98 profile-level-id=420015"
 !
voice class codec 6
 codec preference 1 g711ulaw
 video codec h264 profile 3
 !
dial-peer voice 5000 voip
 description CUVA
 destination-pattern 5000
 rtp payload-type cisco-codec-video-h264 98
 session protocol sipv2
 session target loopback:rtp
 incoming called-number 5000
 voice-class codec 6
 voice-class sip bandwidth video tias-modifier 384000
```

| Feature Name | Releases | Feature Information |
|---|---|---|
| RTP Media Loopback for SIP Calls | Baseline Functionality | RTP packets are looped back toward the source when the RTP Media Loopback for SIP Calls feature is configured on a dial peer.
                                          SIP RTP media loopback helps in verifying the media path between the device originating the call and the intermediate device. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Router(config)# dial-peer voice 77 voip | Specifies that the dial peer is a VoIP peer and enters dial peer voice configuration mode. |
| Step 4 | destination-pattern string Example: Router(config-dial-peer)# destination-pattern 77 | Specifies the prefix or the full E.164 number for the dial peer. |
| Step 5 | session protocol sipv2 Example: Router(config-dial-peer)# session protocol sipv2 | Specifies the session protocol for calls with the SIP option. |
| Step 6 | session target loopback:rtp Example: Router(config-dial-peer)# session target loopback:rtp | Designates a network-specific address to receive calls from a VoIP dial peer and configures all voice data to loop back to
                                          the source. |
| Step 7 | incoming called-number string Example: Router(config-dial-peer)# incoming called-number 77 | Specifies a digit string that can be matched by an incoming call to associate the call with the dial peer. |
| Step 8 | exit Example: Router(config-dial-peer)# exit | Exits dial peer voice configuration mode and enters global configuration mode. |