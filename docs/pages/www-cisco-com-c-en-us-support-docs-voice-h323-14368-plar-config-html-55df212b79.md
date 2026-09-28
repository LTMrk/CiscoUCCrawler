---
doc_id: www-cisco-com-c-en-us-support-docs-voice-h323-14368-plar-config-html-55df212b79
source_url: https://www.cisco.com/c/en/us/support/docs/voice/h323/14368-plar-config.html
retrieved_at: 2026-08-21T07:17:35.547624+00:00
---

Configuring Connection PLAR for VoIP Gateways

# Configuring Connection PLAR for VoIP Gateways

### Download Options

Updated: February 2, 2006

Document ID: 14368

Contents

## Contents

## Introduction

This document provides a sample configuration for connecting Private-line automatic ringdown (PLAR) for VoIP gateways.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This configuration was developed and tested with a Cisco 2610 router and a Cisco 3600 router running Cisco IOS® Software Release 12.1(1) with IP Plus feature set.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

### Conventions

For more information on document conventions, refer to Cisco Technical Tips Conventions .

## Background Theory

PLAR circuits have statically configured endpoints and do not require the user dialing to connect calls. The connection plar command provides a mechanism to create a switched Voice over IP (VoIP) call without digit dialing. PLAR connections are often referred to as a "bat-phone" type of application. This is when a phone (or DS0) goes off-hook and a remote phone rings (or remote DS0 goes off-hook) without digits being dialed. This is a useful tool for customer requirements such as:

The provision of an Off-Premises eXtension (OPX) from a private branch exchange (PBX). Connection PLAR allows remote users on Foreign Exchange Station (FXS) ports to look to a central PBX like physical extensions.

The provision of dial-tone from a remote PBX. Many customers want to offer toll-bypass VoIP services without having the routers provide dial-tone or change their existing dialplan. This allows stations at remote sites to look like they are physically connected stations to a PBX.

Connection PLAR mode is available for VoIP on these platforms:

Cisco 2600 and 3600

Cisco 7200/7500

Cisco MC3810

## Connection Modes: PLAR Vs Trunk

These are the main similarities and differences between connection PLAR mode and connection trunk mode:

Connection trunk mode is a permanent connection. The VoIP call is always connected independently of the plain old telephone service (POTS) port being on-hook or off-hook.

Connection PLAR mode is a switched VoIP call. The call is setup on an as-needed basis. With connection PLAR, no bandwidth is consumed while the phone is on hook. When a phone connected to a POTS dial peer is taken off-hook, the call is automatically connected and the remote phone begins to ring.

Both Connection Trunk and Connection PLAR modes have statically configured endpoints and do not require the user dialing to connect calls.

Connection trunk mode allows supplemental call signaling such as hookflash or point-to-point hoot-n-holler to be passed over the IP network between the two Telephony devices.

Note: Connection PLAR can now support hookflash signaling by configuring hookflash relay.

A hookflash indication is a brief on-hook condition that occurs during a call. It is created by a quick press and release of the hook on your telephone. PBXs and telephone switches are frequently programmed to intercept hookflash indications and use them as a way to allow a user to invoke supplemental services.

For more information on hookflash relay refer to Cisco H.323 Version 2 Phase 2 and H.323 Version 2 Support .

For more information on hoot-n-holler refer to Cisco Hoot & Holler over IP Solution and Cisco Hoot and Holler over IP .

## Connection PLAR Mode Design Considerations and Limitations

A connection PLAR is a switched VoIP call. A switched VoIP call is like a Switched Virtual Circuit (SVC). It is setup on an as-needed basis.

A connection PLAR can work between any type of signaling (recEive and transMit (E&M), Foreign Exchange Office (FXO), and/or FXS), and between any combination of analog and digital interfaces.

A connection PLAR for VoIP supports PLAR-OPX (such as what is used on the MC3810) after Cisco IOS Software Release 12.0(7)XK, 12.1(2)T or later. This feature is used to roll-over the call to voicemail if the remote phone does not answer.

A connection PLAR does not collect digits from the connected Telephony device. This is so it can be deployed without changes to the existing dialplan.

A connection PLAR can be configured for a single direction (calling in one direction), or in both directions of the VoIP call legs.

A connection PLAR is defined per voice-port. This means that the voice-port is unable to operate both in Connection Trunk mode and Collect Dialed-digits mode.

## Configure

In this section, you are presented with the information to configure the features described in this document.

Note: To find additional information on the commands used in this document, use the Command Lookup Tool ( registered customers only) .

### Network Diagram

This document uses the network setup shown in the diagram below.

### Configurations

This configuration shows a typical configuration using the Connection PLAR mode between two routers with a digital T1 interface connected to a PBX at one end and a remote router configured with a analog FXS interface connected to a Telephony device at the other end. Also, the Connection PLAR is only configured to call in one direction (from maui-slt-01 to maui-vgw-01).

```
version 12.1
service timestamps debug datetime msec
service timestamps log datetime msec

!
hostname maui-slt-01
!
voice-card 1
!

controller T1 1/0
 framing esf
 linecode b8zs ds0-group 1 timeslots 1 type fxo-loop-start
 ds0-group 2 timeslots 2 type fxo-loop-start !--- These two commands create two logical voice-ports: !--- voice-port 1/0:1 and voice-port 1/0:2. ! voice-port 1/0:1
 connection plar 2000 !--- This command starts a PLAR switched !--- VoIP call that uses digits (2000) !--- to match a VoIP dial-peer when the voice-port 1/0:1 goes off-hook. ! voice-port 1/0:2
 connection plar 2001 !--- The digits are generated internally by the router !--- and are not received from the voice-port. ! dial-peer voice 1 pots
 destination-pattern 1000
 port 1/0:1 ! dial-peer voice 2 pots
 destination-pattern 1001
 port 1/0:2 !
dial-peer voice 3 voip
 destination-pattern 200. !--- Matches the connection plar strings !--- 2000 and 2001. dtmf-relay h245-alphanumeric
 session target ipv4:192.168.100.1 !
interface Serial0/1
 ip address 192.168.100.2 255.255.255.0
```

```
version 12.1
service timestamps debug datetime msec
service timestamps log datetime msec

!
hostname maui-vgw-01
!

voice-card 3

! voice-port 1/1/0 !--- This is an FXS port. ! voice-port 1/1/1 !--- This is an FXS port. ! dial-peer voice 1 pots
 destination-pattern 2000
 port 1/1/0 !--- This dial-peer terminates the connection PLAR !--- from maui-slt-01's voice-port 1/0:1 . When the !--- router receives digits 2000 in a call-setup, it !--- takes port 1/1/0 off-hook and completes the call. !
dial-peer voice 3 pots
 destination-pattern 2001
 port 1/1/1
!
dial-peer voice 2 voip
 destination-pattern 100. dtmf-relay h245-alphanumeric
 session target ipv4:192.168.100.2 !--- When the router receives digits from a !--- POTS peer that starts with 100 and follows one more !--- string of characters (0-9, A-Z,*,# or .), !--- it creates a VoIP call to the router !--- with IP address 192.168.100.2. !
interface Serial0/0
 ip address 192.168.100.1 255.255.255.0
 clockrate 256000
```

## Verify

This section provides information you can use to confirm your configuration is working properly.

### Command Summary

connection plar - Use this command to specify a PLAR connection. PLAR is handled by associating a peer directly with an interface. When an interface goes off-hook, the peer is used to set up the second call leg and conference them together without the caller having to dial any digits. Configure this command at the voice-port configuration mode.

dtmf-relay [cisco-rtp] [h245-signal] [h245-alphanumeric] - Since the router does not interpret digits from a Telephony device, by default, all digits are passed through the compressed VoIP audio-path. Low-bitrate coder-decoders (CODECs) such as G.729 and G.723.1 are highly optimized for voice patterns, and tend to distort dual tone multifrequency (DTMF) tones. The dtmf relay command solves this problem by transporting DTMF tones out of band, or separate from the encoded voice stream. For more information on dtmf-relay and its options refer to: H.323 Version 2 Support .

### Debug and Show Commands

Certain show commands are supported by the Output Interpreter Tool ( registered customers only) , which allows you to view an analysis of show command output.

show voice port - Displays information about the voice port configuration. Use this command to verify that the port is up, connection PLAR is enabled, and the connection PLAR string is correct.

show call active voice - Displays the contents of the active call table, which shows all of the calls currently connected through the router.

debug voip ccapi inout - This command is useful to troubleshoot end-to-end VoIP calls.

For more information on troubleshooting VoIP calls refer to: Troubleshoot & Debug VoIP Calls - the Basics and VoIP Debug Commands .

### Sample show Output

```
maui-slt-01# show voice port 1/0:1 Foreign Exchange Office
 Type of VoicePort is FXO
 Operation State is DORMANT
 Administrative State is UP
 The Last Interface Down Failure Cause is Administrative Shutdown
 Description is not set
 Noise Regeneration is enabled
 Non Linear Processing is enabled
 Music On Hold Threshold is Set to -38 dBm
 In Gain is Set to 0 dB
 Out Attenuation is Set to 0 dB
 Echo Cancellation is enabled
 Echo Cancel Coverage is set to 8 ms Connection Mode is plar
 Connection Number is 2000 Initial Time Out is set to 10 s
 Interdigit Time Out is set to 10 s
 Call-Disconnect Time Out is set to 60 s
 Ringing Time Out is set to 180 s
 Region Tone is set for US

 Analog Info Follows:
 Currently processing Voice
 Maintenance Mode Set to None (not in mtc mode)
 Number of signaling protocol errors are 0
 Impedance is set to 600r Ohm

 Voice card specific Info Follows:
 Signal Type is loopStart
 Number Of Rings is set to 1
 Supervisory Disconnect active
 Hook Status is On Hook
 Ring Detect Status is inactive
 Ring Ground Status is inactive
 Tip Ground Status is inactive
 Dial Type is dtmf
 Digit Duration Timing is set to 100 ms
 InterDigit Duration Timing is set to 100 ms
 Pulse Rate Timing is set to 10 pulses/second
 InterDigit Pulse Duration Timing is set to 750 ms
```

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

## Related Information

### Revision History

1.0

02-Feb-2006

Initial Release

| maui-slt-01 (2600) |
|---|
| version 12.1
service timestamps debug datetime msec
service timestamps log datetime msec

!
hostname maui-slt-01
!
voice-card 1
!

controller T1 1/0
 framing esf
 linecode b8zs ds0-group 1 timeslots 1 type fxo-loop-start
 ds0-group 2 timeslots 2 type fxo-loop-start !--- These two commands create two logical voice-ports: !--- voice-port 1/0:1 and voice-port 1/0:2. ! voice-port 1/0:1
 connection plar 2000 !--- This command starts a PLAR switched !--- VoIP call that uses digits (2000) !--- to match a VoIP dial-peer when the voice-port 1/0:1 goes off-hook. ! voice-port 1/0:2
 connection plar 2001 !--- The digits are generated internally by the router !--- and are not received from the voice-port. ! dial-peer voice 1 pots
 destination-pattern 1000
 port 1/0:1 ! dial-peer voice 2 pots
 destination-pattern 1001
 port 1/0:2 !
dial-peer voice 3 voip
 destination-pattern 200. !--- Matches the connection plar strings !--- 2000 and 2001. dtmf-relay h245-alphanumeric
 session target ipv4:192.168.100.1 !
interface Serial0/1
 ip address 192.168.100.2 255.255.255.0 |

| maui-vgw-01 (3600) |
|---|
| version 12.1
service timestamps debug datetime msec
service timestamps log datetime msec

!
hostname maui-vgw-01
!

voice-card 3

! voice-port 1/1/0 !--- This is an FXS port. ! voice-port 1/1/1 !--- This is an FXS port. ! dial-peer voice 1 pots
 destination-pattern 2000
 port 1/1/0 !--- This dial-peer terminates the connection PLAR !--- from maui-slt-01's voice-port 1/0:1 . When the !--- router receives digits 2000 in a call-setup, it !--- takes port 1/1/0 off-hook and completes the call. !
dial-peer voice 3 pots
 destination-pattern 2001
 port 1/1/1
!
dial-peer voice 2 voip
 destination-pattern 100. dtmf-relay h245-alphanumeric
 session target ipv4:192.168.100.2 !--- When the router receives digits from a !--- POTS peer that starts with 100 and follows one more !--- string of characters (0-9, A-Z,*,# or .), !--- it creates a VoIP call to the router !--- with IP address 192.168.100.2. !
interface Serial0/0
 ip address 192.168.100.1 255.255.255.0
 clockrate 256000 |

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 02-Feb-2006 | Initial Release |