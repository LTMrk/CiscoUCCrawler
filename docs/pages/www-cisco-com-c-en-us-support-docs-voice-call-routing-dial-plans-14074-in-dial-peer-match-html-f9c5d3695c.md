---
doc_id: www-cisco-com-c-en-us-support-docs-voice-call-routing-dial-plans-14074-in-dial-peer-match-html-f9c5d3695c
source_url: https://www.cisco.com/c/en/us/support/docs/voice/call-routing-dial-plans/14074-in-dial-peer-match.html
retrieved_at: 2026-08-19T00:12:25.199916+00:00
---

Understand Matching Inbound/Outbound Dial Peers on IOS Platforms

# Understand Matching Inbound/Outbound Dial Peers on IOS Platforms

### Download Options

Updated: August 18, 2026

Document ID: 14074

Contents

## Contents

## Introduction

This document describes how the inbound and outbound dial peers are matched to traditional telephone services (POTS) and to Voice-Network call legs.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

Voice - Understanding Dial Peers and Call Legs on Cisco IOS® Platforms

Voice - Understanding Inbound and Outbound Dial Peers on Cisco IOS Platforms

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Matching Inbound Dial Peers

### Inbound Dial Peers Elements and Attributes

Three information elements sent in the call setup message and four configurable dial peer command attributes are used to match dial peers as follows:

Inbound POTS dial peers are associated to incoming POTS call legs on the initial router or gateway.

Inbound  Voice-Network dial peers are associated to incoming Voice-Network call legs of the terminating router or gateway. Examples of Voice-Network calls legs are Voice over IP (VoIP), Voice over Frame Relay (VoFR), Voice over ATM (VoATM), and Multimedia Mail over IP (MMoIP).

The four configurable Cisco IOS dial peer attributes and related call setup elements are shown here:

Note : For outbound dial peers, this command is matched against the called number or DNIS strings.

The three call setup elements are:

### Inbound Dial Peers Matching Process

When the Cisco IOS® router or gateway receives a call setup request, a dial peer match is made for the incoming call in order to facilitate routing the call to different session applications. This is not a digit-by-digit match, rather the full digit string received in the setup request is used to match against configured dial peers.

Note : The maximum number of dial peers that can be configured on a Cisco IOS gateway depends on the available memory (DRAM). Each dial peer consumes approximately 6KB of memory. Make sure that you have at least 20% of the total memory reserved for other CPU processes. If the dial peers are used for call routing, a larger number of dial peers can add to the delay to route a call. This can be significant as the Cisco IOS voice stack looks through dial peers from the top down, similar to an Access Control List.

The router or gateway matches the information elements in the setup message with the dial peer attributes to select an inbound dial peer. The router or gateway matches these items in this order:

Called number (DNIS) with the incoming called-number command:

First, the router or gateway attempts to match the called number of the call setup request with the configured incoming called-number of each dial peer. Because call setups always include DNIS information, it is recommended to use the incoming called-number command for inbound dial peer matching. This attribute has matching priority over the answer-address and destination-pattern commands.

Calling Number (ANI) with the answer-address command:

If no match is found in step 1, the router or gateway attempts to match the calling number of the call setup request with the answer-address of each dial peer. This attribute can be useful in situations where you want to match calls based on the calling number (initial).

Calling Number (ANI) with the destination-pattern command:

If no match is found in step 2, the router or gateway attempts to match the calling number of the call setup request to the destination-pattern of each dial peer. For more information about this, see the first bullet in the Dial Peer Additional Information section of this document.

Voice-port (associated with the incoming call setup request) with configured dial peer port (applicable for inbound POTS call legs):

If no match is found in the step 3, the router or gateway attempts to match the configured dial peer port to the voice-port associated with the incoming call. If multiple dial peers have the same port configured, the dial peer first added in the configuration is matched.

If no match is found in the first four steps, then the default dial peer 0 (pid:0) command is used.

Note : Step 4 is not applicable to voice or dial platforms such as AS5300, AS5350, AS5400, AS5800 and AS5850. If any one of the first three steps is not used, then match dial peer 0, and the call is treated as a dial modem call. This means that customers can get modem tones as opposed to dial tones for inbound calls.

The Cisco IOS router or gateway matches only one of these conditions. It is not necessary for all the attributes to be configured in the dial peer or that every attribute match the call setup information. Only one condition must be met for the router or gateway to select a dial peer. The router or gateway stop to search as soon as one dial peer is matched.

The longest prefix matching criteria applies while each step is performed. At each step, if multiple matches are found, the one with the longest explicit match is chosen. This example helps clarify this concept:

Assume the incoming called number (DNIS) is 81690 . Dial peer 2 is matched.

```
dial-peer voice 1 pots
 incoming called-number 8....
 direct-inward-dial
!

dial-peer voice 2 pots
 incoming called-number 816..
 direct-inward-dial
```

Note : For inbound dial peers, the session target command is ignored.

### The Default Dial-Peer 0 peer_tag=0, pid:0

If no incoming dial peer is matched by the router or gateway, the inbound call leg is automatically routed to a default dial peer (POTS or Voice-Network). This default dial peer is referred to as dial-peer 0 or pid:0.

Note : There is an exception to this statement. Cisco voice and dial platforms, such as the AS53xx and AS5800, require that a configured inbound dial peer is matched for incoming POTS calls to be accepted as voice calls. If there is no inbound dial peer match, the call is treated and processed as a dial-up (modem) call.

Dial-peer 0 (pid:0) has a default configuration that cannot be changed. The default dial-peer 0 fails to negotiate non-default capabilities, services, and applications such as:

Non-default Voice-Network capabilities: dtmf-relay, no vad, and so forth.

Direct Inward Dial (DID)

TCL Applications

Dial-peer 0 for inbound VoIP peers has this configuration:

any codec

vad enabled

no rsvp support

fax-rate voice

Note : The default DSCP for voice is EF codepoint 101110 (RFC 2598), and the default DSCP for signaling is AF31 codepoint 011010 (RFC 2597). The default dial peer does not mark packets to DSCP 0. All voice packets on the routers are marked by default (this can be overridden by the dial peer), signaling with AF31 and media with EF. Calls that match the default dial peer 0 must also have this behavior.

Dial-peer 0 (pid:0) for inbound POTS peers has this configuration:

no ivr application

For further explanation of this concept, see the Case Study: Understand Inbound Matching and Default Dial-Peer 0 section of this document.

### Special Note on ISDN Overlap-receiving

There are implications for inbound dial peer matching when the isdn overlap-receiving command is configured on ISDN interfaces. After every digit is received at the ISDN layer, dial peers are checked for matches. If a full match is made, the call is routed immediately (to the session app in this case) before additional digits are routed. The T terminator can be used to suspend this digit-by-digit matching and force the router or gateway to wait until all digits are received. The T refers to the T302 interdigit timer at the ISDN level, configurable under the serial interface associated with the ISDN interface. ISDN also provides other mechanisms to indicate the end of digits, such as the Sending Complete Information Element (IE) in Q.931 information messages that it sets.

### Special Note on POTS Calls with Empty Calling Number Field

Assume this configuration:

```
dial-peer voice 1 pots
   destination-pattern 9T
   port 1/0:1
```

Assume that an incoming call arrives with no calling number information and is matched with the POTS dial peer based on the destination-pattern 9T command. In this case, the Cisco IOS router or gateway uses the 9 digit as the calling number and forwards the call to the related device, such as CallManager or the .Cisco IOS Gateway. In order to not replace the empty calling number field, create a dummy POTS dial peer with just the incoming called-number command configured. Because the incoming called-number< /strong> statement has higher priority than destination pattern for inbound POTS matching, dial-peer voice 2 becomes the POTS dial peer used.

```
dial-peer voice 1 pots 
    destination-pattern 9T
    port 1/0:1
!
dial-peer voice 2 pots
    incoming called-number .
```

### Special Note on Empty Called Number

The Warning message shown here, which displays when dial-peer is configured with incoming called-number T, can raise questions in regard to the dial-peer selection with an empty called number from an actual router.

```
RTR(config)# dial-peer voice 1 pots RTR(config-dial-peer)# incoming called-number T Warning: Pattern T defines a match with zero or more digits and hence could 
match with an empty number.  If this is not the desired behaviour please 
configure pattern .T instead to match on one or more digits
RTR(config-dial-peer)#
```

Incoming dial-peer match with an empty called number:

A null called-number is considered less qualified compared to a port number and/or in some cases answer-address. Therefore, a match based on a null called number can occur ONLY if there is no match based on either answer-address or port-number.

In case of overlap dialing, a null called number cannot match incoming called-number T because timeout has not occurred.

A null called-number can match incoming called-number T only in case of ENBLOCK and there is no match either because of answer-address and port-number. The warning you see when you configure incoming called-number T refers to this specific case.

## Matching Outbound Dial Peers

In order to match outbound dial peers, the router or gateway uses the dial peer destination-pattern called_number command.

On POTS dial peers, the port command is then used to forward the call.

On Voice-Network dial peers, the session target command is then used to forward the call.

Also, when outbound peers are matched, there are two cases to consider: DID case and non-DID.

### Direct Inward Dial (DID) Case

An incoming dial peer configured with DID direct-inward-dial looks like this:

```
dial-peer voice 1 pots
  incoming called-number 81690
  voice-port 0:D
  direct-inward-dial
```

On DID calls, also referred to as one-stage dialing, the setup message contains all the digits necessary to route the call, and the router or gateway must not do subsequent digit collection. When the router or gateway searches for an outbound dial peer, the device uses the entire incoming dial string. This matching is variable-length by default. This match is not done digit-by-digit because by DID definition, all digits have been received. This example helps clarify this concept:

Assume the DID dial-string is 81690. In this case, the router matches dial peer 4 and forwards the complete dial-string 81690.

```
dial-peer voice 3 voip
 destination-pattern 816
 session target ipv4:172.22.10.1
!
dial-peer voice 4 voip
 destination-pattern 81690
 session target ipv4:172.22.10.1
```

For more information on DID, refer to Voice - Understanding Direct-Inward-Dial (DID) on Cisco IOS Digital (T1/E1) Interfaces .

### Non-DID Case

This case is also referred to as two-stage dialing. If DID is not configured on the matched incoming dial peer, the router or gateway enters the digit collection mode (digits are collected inbound). Outbound dial peer matching is done on a digit-by-digit basis. The router or gateway checks for dial peer matches after the device has received each digit and then routes the call when a full match is made. These examples help clarify this concept:

Assume the dial-string is 81690. Immediately after the router receives the digit 6, the router matches dial peer 3 and routes the call (forwarding only the digits 816).

```
dial-peer voice 3 voip
 destination-pattern 816
 session target ipv4:172.22.10.1
!
dial-peer voice 4 voip
 destination-pattern 81690
 session target ipv4:172.22.10.1
```

Now, assume dial peer 3 is configured for wild-card matching:

```
dial-peer voice 3 voip
 destination-pattern 816..
 session target ipv4:172.22.10.1 
!
dial-peer voice 4 voip
 destination-pattern 81690
 session target ipv4:172.22.10.1
```

In this case, the longest-prefix rule applies, and dial peer 4 is matched for the outbound call leg.

### Special Note on Variable-Length Dial Plans

There are situations where expected dial-strings do not have a set number of digits. In such cases, Cisco recommends you configure the T terminator on the dial peer destination-pattern command in order to use variable-length dial-peers.

The T terminator forces the router or gateway to wait until the full dial-string is received. In order to achieve this, the T terminator forces the router or gateway to wait until the full dial-string is received. The router or gateway:

Waits for a set interdigit timeout before the device routes the call.

Routes the call once the device receives the # termination character in the dial-string. For example, if you dialed 5551212#, the # indicates to the router that you dialed all the digits and that all digits prior to the # must be used to match a dial peer.

This example helps clarify this concept:

Assume the router in this example receives a call setup with dial-string 95551212 from the network. Dial peer 2 then forwards to the PSTN the digits 5551212:

```
dial-peer voice 2 pots destination-pattern 9T port 2/0:23
```

Assume the dial-string from an inbound POTS interface is 81690:

```
dial-peer voice 3 voip
 destination-pattern 8T
 session target ipv4:172.22.10.1
!
dial-peer voice 4 voip
 destination-pattern 81690T
 session target ipv4:172.22.10.1
```

In this case, the longest-prefix rule applies, and dial peer 4 is matched for the outbound call leg.

The default interdigit timeout is set for 10 seconds. In order to modify this value, issue the timeouts interdigit seconds voice-port command.

Anytime the T is used, T must be preceded by a full stop (.) or digits (T or 555T for example). If you use T alone, the dial peers act improperly and effect how calls are handled by the router.

## Dial Peer Operational Status

A dial peer operational status must be administratively set up and valid for the dial peer to be matched. In order to be considered operational, dial peers must meet one of these conditions:

Destination-pattern is configured, and a voice-port or session target is also configured.

Incoming called-number is configured.

Answer-address is configured.

There are other conditions, but these are the main ones.

For more information, refer to Voice - Understanding the Operational Status of Dial-Peers on Cisco IOS Platforms .

## Dial Peer Additional Information

The dial peer attribute destination-pattern has different behavior when applied to inbound or outbound call legs:

For inbound dial peers, the destination-pattern is matched against the calling number (ANI string).

For outbound dial peers, the destination-pattern is matched against called number (DNIS string).

Therefore, a dial peer with the destination-pattern attribute can work for both outbound and inbound< /i> matching .

## Case Study: Understand Inbound Matching and Default Dial-Peer 0

Every dial plan needs an outgoing and an inbound dial peer. In this example, there is a PSTN T1 connection coming as inbound to the maui-gwy-04 router. In this case, when an incoming call is received from the PSTN the router tries to find the called number. When the call is received the caller gives the caller ID with the Automatic Number Identification (ANI). In this example, there is a Direct inward dial (DID) range that starts from 8. DNIS is the number that the person on the PSTN dials. The number could be an 11 digit or 10 digit number. If it matches the incoming dial peer configured with the direct-inward-dial, only 4 numbers after 8 are forwarded and the rest are stripped of in order for the call to be reached directly without the help of a receptionist.

If you do not have an inbound dial peer configured, Dial-peer 0 is matched and takes care of the call. The Dial-peer 0 has these attributes:

Works for any Codec

Has Voice Activity Detection (VAD) enabled

Marks traffic as IP Precedence 0

Has no RSVP support

Supports FAX-RATE service

Note : The IP Precedence command is set to a default value of 0 , which causes the IP Precedence to be passed as-is.

### Configurations

```
!--- <some output omitted> !
version 12.0
service timestamps debug datetime
! hostname maui-gwy-04 !
isdn switch-type primary-ni
!
controller T1 0
 framing esf
 clock source line primary
 linecode b8zs
 pri-group timeslots 1-24
!
voice-port 0:D
! !--- This dial peer is used for !--- inbound DID calls. Dial-peer voice 1 pots
 incoming called-number 8....
 direct-inward-dial ! dial-peer voice 3 voip
 destination-pattern 8....
 DTMF-relay cisco-rtp
 session target ipv4:172.22.10.1 !
dial-peer voice 2 pots
 destination-pattern 9T
 port 0:D
!
interface Ethernet0
 ip address 172.22.10.2 255.255.255.0
 no ip directed-broadcast
!
interface Serial0:23
 no ip address
 no ip directed-broadcast
 isdn switch-type primary-ni
 isdn incoming-voice modem
 fair-queue 64 256 0
 no cdp enable
```

```
!
version 12.2
service timestamps debug datetime
! hostname maui-gwy-06 !
interface Ethernet0/0
 ip address 172.22.10.1 255.255.255.0
 half-duplex
! !--- FXS port voice-port 1/0/0
! dial-peer voice 1 pots
 destination-pattern 81560
 port 1/0/0 ! dial-peer voice 2 voip
 destination-pattern 9.....
 session target ipv4:172.22.10.2
 DTMF-relay cisco-rtp
```

In this case study, these show and debug commands are used:

show call active voice {brief} This command displays the contents of the active call table, which shows all of the calls currently connected through the router. In this case, the command is useful in order to display dial peers and capabilities associated to an active call.

debug voip ccapi inout This command is useful in order to troubleshoot end-to-end VoIP calls.

```
!--- Action: Call is placed from the PSTN through maui-gwy-04 !--- and terminated on an FXS port of maui-gwy-06 (called number: "81560") !--- Notes: !--- 1)On maui-gwy-04, the incoming call is received on the POTS dial-peer 1, !--- which is configured for DID. !--- 2)On maui-gwy-06, no inbound VoIP dial-peer is matched and default !--- dial-peer=0 is used. Therefore, the DTMF-relay cisco-rtp negotiation !--- fails. !----------------------------------------------------------------------------- !--- Output on maui-gwy-04 (Originating Gateway) !-----------------------------------------------------------------------------

maui-gwy-04# show call active voice brief !--- This information was captured on the call originating gateway !--- once the call was placed and active. !--- !--- <some output omitted> ! <ID>: <start>hs.<index> +<connect> pid:<peer_id> <dir> <addr> <state>
  dur hh:mm:ss tx:<packets>/<bytes> rx:<packets>/<bytes> <state>
 IP <ip>:<udp> rtt:<time>ms pl:<play>/<gap>ms lost:<lost>/<early>/<late>
  delay:<last>/<min>/<max>ms <codec>
Tele <int>: tx:<tot>/<v>/<fax>ms <codec> noise:<1> acom:<1> i/o:<1>/<1> dBm !--- POTS (keyword Tele) dial-peer 1 is matched inbound (keyword Answer). !--- This dial-peer was matched based on condition 1 of the Matching Inbound !--- Dial Peers section of this document. 87   : 415666267hs.1 +107 pid:1 Answer active
 dur 00:00:20 tx:101/791 rx:100/3200 Tele 0:D:93: tx:20600/2000/0ms g729r8 noise:-56 acom:0  i/0:-55/-70 dBm !--- VoIP (keyword IP) dial-peer 3 is matched outbound (keyword Originate). !--- This dial-peer was matched based on the destination-pattern command. 87   : 415666268hs.1 +106 pid:3 Originate 81560 active
 dur 00:00:20 tx:100/2000 rx:101/1991 IP 172.22.10.1:18160 rtt:2ms pl:1990/40ms lost:0/1/0 delay:69/69/70ms g729r8

maui-gwy-04# show call active voice !--- <some output omitted> !--- With the show call active voice command, you see that DTMF-relay Cisco !--- RTP was partially negotiated. VOIP:
RemoteIPAddress=172.22.10.1
RemoteUDPPort=18160
RoundTripDelay=4 ms
SelectedQoS=best-effort tx_DtmfRelay=cisco-rtp SessionProtocol=cisco
SessionTarget=ipv4:172.22.10.1
VAD = enabled
CoderTypeRate=g729r8
CodecBytes=20
SignalingType=cas !----------------------------------------------------------------------------- !--- Output on maui-gwy-06 (Terminating Gateway) !----------------------------------------------------------------------------- maui-gwy-06# show call active voice brief !--- This information was captured once the call was placed and active. !--- !--- <some output omitted> !--- Notice that in this case, default VoIP(keyword IP) dial-peer 0 was !--- matched inbound. Total call-legs: 2
87   : 257583579hs.1 +105 pid:0 Answer active
 dur 00:10:03 tx:1938/37069 rx:26591/531820 IP 172.22.10.2:18988 rtt:1ms pl:528740/160ms lost:0/1/0 delay:50/50/70ms
 g729r8

87   : 257583580hs.1 +104 pid:1 Originate 81560 active
 dur 00:10:05 tx:26648/532960 rx:1938/37069 Tele 1/0/0 (96): tx:605710/37690/0ms g729r8 noise:-46 acom:
0  i/0:-46/-61 dBm

maui-gwy-06# show call active voice !--- <some output omitted> !--- Notice that DTMF-relay cisco rtp was NOT negotiated on this end. Total call-legs: 2
VOIP:
RemoteIPAddress=172.22.10.2
RoundTripDelay=2 ms
SelectedQoS=best-effort tx_DtmfRelay=inband-voice FastConnect=FALSE
Separate H245 Connection=FALSE
H245 Tunneling=FALSE
SessionProtocol=cisco
VAD = enabled
CoderTypeRate=g729r8
CodecBytes=20
SignalingType=ext-signal !--- Output from debug voip ccapi inout. !--- <Only relevant output has been captured> !--- Inbound VoIP call leg is matched to default dial-peer 0. !--- In this case, notice that maui-gwy-06 did not receive the calling !--- number (ANI). Therefore, voip dial-peer 2 was not matched based on !--- condition 3 of the Matching Inbound Dial Peers section of this document. *Mar 30 19:30:35: cc_api_call_setup_ind (vdbPtr=0x620AA230, callInfo={called=81560, called_oct3=0 calling =,calling_oct3=0x0,calling_oct3a=0x0,
calling_xlated=false,
     subscriber_type_str=Unknown, fde, peer_tag=0 , prog_ind=0},
callID=0x62343650) *Mar 30 19:30:35: cc_api_call_setup_ind (vdbPtr=0x620AA230,
callInfo={called=81560,
     calling=, fd1 peer_tag=0}, callID=0x62343650) *Mar 30 19:30:35: >>>>CCAPI handed cid 95 with tag 0 to app "DEFAULT" ..... !--- Outbound POTS dial-peer 1 is matched. *Mar 30 19:30:35: ssaSetupPeer cid(95) peer list: tag(1) called number (81560) *Mar 30 19:30:35: ccCallSetupRequest (Inbound call = 0x5F, outbound peer =1 , dest=,
        params=0x621D4570 mode=0, *callID=0x621D48D8, prog_ind = 0) *Mar 30 19:30:35: peer_tag=1
```

Now, to match the inbound VoIP dial-peer 2 on maui-gwy-06 add this command:

```
maui-gwy-06# config t Enter configuration commands, one per line.  End with CNTL/Z.
maui-gwy-06(config)# dial-peer voice 2 voip !--- This command uses the DNIS(called number)to match the inbound call leg !--- to the dial-peer. maui-gwy-06(config-dial-peer)# incoming called-number 8....
```

This is a snapshot of the maui-gwy-06 configuration after additional configuration:

```
!--- <Some output omitted> dial-peer voice 1 pots
 destination-pattern 81560
 port 1/0/0
!
dial-peer voice 2 voip incoming called-number 8 ....
 destination-pattern 9.....
 session target ipv4:172.22.10.2
 dtmf-relay cisco-rtp
!
```

```
!--- Action: Call is placed from the PSTN through maui-gwy-04 !--- and terminated in an FXS port of maui-gwy-06 (called number: "81560"). !--- Notes: !--- 1)On maui-gwy-04, the incoming call is received on the POTS dial-peer 1, !--- which is configured for DID. !--- 2)On maui-gwy-06, dial-peer 2 voip is matched inbound, and dtmf-relay !--- Cisco RTP is negotiated. !----------------------------------------------------------------------------- !--- Output on maui-gwy-06 (Terminating Gateway) !-----------------------------------------------------------------------------

maui-gwy-06# show call active voice brief !--- <some output omitted> Total call-legs: 2 !--- Notice that in this case, the inbound VoIP call leg is matched to !--- dial-peer 2 VOIP. 8B   : 258441268hs.1 +176 pid:2 Answer active
 dur 00:01:01 tx:485/8768 rx:2809/56180 IP 172.22.10.2:16762 rtt:2ms pl:52970/120ms lost:0/1/0 delay:
60/60/70ms g729r8

8B   : 258441269hs.1 +175 pid:1 Originate 81560 active
 dur 00:01:02 tx:2866/57320 rx:512/9289
 Tele 1/0/0 (98): tx:64180/9640/0ms g729r8 noise:-46 acom:
0  i/0:-46/-61 dBm

maui-gwy-06# show call active voice !--- <some output omitted> !--- Notice that dtmf-relay cisco rtp was successfully negotiated. VOIP:
RemoteIPAddress=172.22.10.2
RoundTripDelay=1 ms
SelectedQoS=best-effort tx_DtmfRelay=cisco-rtp FastConnect=FALSE
Separate H245 Connection=FALSE
H245 Tunneling=FALSE
SessionProtocol=cisco
SessionTarget=
VAD = enabled
CoderTypeRate=g729r8
CodecBytes=20
SignalingType=cas
```

## Related Information

### Revision History

3.0

18-Aug-2026

Recertification - Updatted Formatting.

2.0

19-May-2025

Updated and Recertification, reformatting.

1.0

11-Dec-2001

Initial Release

| Dial Peer Attribute | Description | Call Setup Element (See the next table) |
|---|---|---|
| gwy(config-dial-peer)# incoming called-number DNIS_string | This dial peer command defines the called number destination or dialed number identification service (DNIS) string. When properly configured, this dial peer command uses the called number to match the incoming call leg to an inbound dial peer. | Called number (DNIS) |
| gwy(config-dial-peer)# answer-address ANI_string | This dial peer command defines the initial calling number or automatic number identification (ANI) string. When properly configured, this dial peer command uses the calling number to match the incoming call leg to an inbound dial peer. | Calling Number (ANI) |
| gwy(config-dial-peer)# destination-pattern string | When inbound call legs are matched, this command uses the calling number (initial or ANI string) to match the incoming call leg to an inbound dial peer. | Calling Number (ANI) for inbound or the Called number (DNIS) strings for outbound |
| gwy(config-dial-peer)# port port | This dial peer command defines the POTS voice port through which calls to this dial peer are placed. | Voice Port |

| Call Setup Element | Description |
|---|---|
| Called number (DNIS) | This is the call destination dial string and is derived from the ISDN setup message or channel associated signaling (CAS) DNIS. |
| Calling Number (ANI) | This is a number string that represents the origin and is derived from the ISDN setup message or CAS ANI. The ANI is also referred to as Calling Line Identification (CLID). |
| Voice Port | This represents the POTS physical voice port. |

| maui-gwy-04 | maui-gwy-06 |
|---|---|
| !--- <some output omitted> !
version 12.0
service timestamps debug datetime
! hostname maui-gwy-04 !
isdn switch-type primary-ni
!
controller T1 0
 framing esf
 clock source line primary
 linecode b8zs
 pri-group timeslots 1-24
!
voice-port 0:D
! !--- This dial peer is used for !--- inbound DID calls. Dial-peer voice 1 pots
 incoming called-number 8....
 direct-inward-dial ! dial-peer voice 3 voip
 destination-pattern 8....
 DTMF-relay cisco-rtp
 session target ipv4:172.22.10.1 !
dial-peer voice 2 pots
 destination-pattern 9T
 port 0:D
!
interface Ethernet0
 ip address 172.22.10.2 255.255.255.0
 no ip directed-broadcast
!
interface Serial0:23
 no ip address
 no ip directed-broadcast
 isdn switch-type primary-ni
 isdn incoming-voice modem
 fair-queue 64 256 0
 no cdp enable | !
version 12.2
service timestamps debug datetime
! hostname maui-gwy-06 !
interface Ethernet0/0
 ip address 172.22.10.1 255.255.255.0
 half-duplex
! !--- FXS port voice-port 1/0/0
! dial-peer voice 1 pots
 destination-pattern 81560
 port 1/0/0 ! dial-peer voice 2 voip
 destination-pattern 9.....
 session target ipv4:172.22.10.2
 DTMF-relay cisco-rtp |

| !--- Action: Call is placed from the PSTN through maui-gwy-04 !--- and terminated on an FXS port of maui-gwy-06 (called number: "81560") !--- Notes: !--- 1)On maui-gwy-04, the incoming call is received on the POTS dial-peer 1, !--- which is configured for DID. !--- 2)On maui-gwy-06, no inbound VoIP dial-peer is matched and default !--- dial-peer=0 is used. Therefore, the DTMF-relay cisco-rtp negotiation !--- fails. !----------------------------------------------------------------------------- !--- Output on maui-gwy-04 (Originating Gateway) !-----------------------------------------------------------------------------

maui-gwy-04# show call active voice brief !--- This information was captured on the call originating gateway !--- once the call was placed and active. !--- !--- <some output omitted> ! <ID>: <start>hs.<index> +<connect> pid:<peer_id> <dir> <addr> <state>
  dur hh:mm:ss tx:<packets>/<bytes> rx:<packets>/<bytes> <state>
 IP <ip>:<udp> rtt:<time>ms pl:<play>/<gap>ms lost:<lost>/<early>/<late>
  delay:<last>/<min>/<max>ms <codec>
Tele <int>: tx:<tot>/<v>/<fax>ms <codec> noise:<1> acom:<1> i/o:<1>/<1> dBm !--- POTS (keyword Tele) dial-peer 1 is matched inbound (keyword Answer). !--- This dial-peer was matched based on condition 1 of the Matching Inbound !--- Dial Peers section of this document. 87   : 415666267hs.1 +107 pid:1 Answer active
 dur 00:00:20 tx:101/791 rx:100/3200 Tele 0:D:93: tx:20600/2000/0ms g729r8 noise:-56 acom:0  i/0:-55/-70 dBm !--- VoIP (keyword IP) dial-peer 3 is matched outbound (keyword Originate). !--- This dial-peer was matched based on the destination-pattern command. 87   : 415666268hs.1 +106 pid:3 Originate 81560 active
 dur 00:00:20 tx:100/2000 rx:101/1991 IP 172.22.10.1:18160 rtt:2ms pl:1990/40ms lost:0/1/0 delay:69/69/70ms g729r8

maui-gwy-04# show call active voice !--- <some output omitted> !--- With the show call active voice command, you see that DTMF-relay Cisco !--- RTP was partially negotiated. VOIP:
RemoteIPAddress=172.22.10.1
RemoteUDPPort=18160
RoundTripDelay=4 ms
SelectedQoS=best-effort tx_DtmfRelay=cisco-rtp SessionProtocol=cisco
SessionTarget=ipv4:172.22.10.1
VAD = enabled
CoderTypeRate=g729r8
CodecBytes=20
SignalingType=cas !----------------------------------------------------------------------------- !--- Output on maui-gwy-06 (Terminating Gateway) !----------------------------------------------------------------------------- maui-gwy-06# show call active voice brief !--- This information was captured once the call was placed and active. !--- !--- <some output omitted> !--- Notice that in this case, default VoIP(keyword IP) dial-peer 0 was !--- matched inbound. Total call-legs: 2
87   : 257583579hs.1 +105 pid:0 Answer active
 dur 00:10:03 tx:1938/37069 rx:26591/531820 IP 172.22.10.2:18988 rtt:1ms pl:528740/160ms lost:0/1/0 delay:50/50/70ms
 g729r8

87   : 257583580hs.1 +104 pid:1 Originate 81560 active
 dur 00:10:05 tx:26648/532960 rx:1938/37069 Tele 1/0/0 (96): tx:605710/37690/0ms g729r8 noise:-46 acom:
0  i/0:-46/-61 dBm

maui-gwy-06# show call active voice !--- <some output omitted> !--- Notice that DTMF-relay cisco rtp was NOT negotiated on this end. Total call-legs: 2
VOIP:
RemoteIPAddress=172.22.10.2
RoundTripDelay=2 ms
SelectedQoS=best-effort tx_DtmfRelay=inband-voice FastConnect=FALSE
Separate H245 Connection=FALSE
H245 Tunneling=FALSE
SessionProtocol=cisco
VAD = enabled
CoderTypeRate=g729r8
CodecBytes=20
SignalingType=ext-signal !--- Output from debug voip ccapi inout. !--- <Only relevant output has been captured> !--- Inbound VoIP call leg is matched to default dial-peer 0. !--- In this case, notice that maui-gwy-06 did not receive the calling !--- number (ANI). Therefore, voip dial-peer 2 was not matched based on !--- condition 3 of the Matching Inbound Dial Peers section of this document. *Mar 30 19:30:35: cc_api_call_setup_ind (vdbPtr=0x620AA230, callInfo={called=81560, called_oct3=0 calling =,calling_oct3=0x0,calling_oct3a=0x0,
calling_xlated=false,
     subscriber_type_str=Unknown, fde, peer_tag=0 , prog_ind=0},
callID=0x62343650) *Mar 30 19:30:35: cc_api_call_setup_ind (vdbPtr=0x620AA230,
callInfo={called=81560,
     calling=, fd1 peer_tag=0}, callID=0x62343650) *Mar 30 19:30:35: >>>>CCAPI handed cid 95 with tag 0 to app "DEFAULT" ..... !--- Outbound POTS dial-peer 1 is matched. *Mar 30 19:30:35: ssaSetupPeer cid(95) peer list: tag(1) called number (81560) *Mar 30 19:30:35: ccCallSetupRequest (Inbound call = 0x5F, outbound peer =1 , dest=,
        params=0x621D4570 mode=0, *callID=0x621D48D8, prog_ind = 0) *Mar 30 19:30:35: peer_tag=1 |
|---|

| !--- Action: Call is placed from the PSTN through maui-gwy-04 !--- and terminated in an FXS port of maui-gwy-06 (called number: "81560"). !--- Notes: !--- 1)On maui-gwy-04, the incoming call is received on the POTS dial-peer 1, !--- which is configured for DID. !--- 2)On maui-gwy-06, dial-peer 2 voip is matched inbound, and dtmf-relay !--- Cisco RTP is negotiated. !----------------------------------------------------------------------------- !--- Output on maui-gwy-06 (Terminating Gateway) !-----------------------------------------------------------------------------

maui-gwy-06# show call active voice brief !--- <some output omitted> Total call-legs: 2 !--- Notice that in this case, the inbound VoIP call leg is matched to !--- dial-peer 2 VOIP. 8B   : 258441268hs.1 +176 pid:2 Answer active
 dur 00:01:01 tx:485/8768 rx:2809/56180 IP 172.22.10.2:16762 rtt:2ms pl:52970/120ms lost:0/1/0 delay:
60/60/70ms g729r8

8B   : 258441269hs.1 +175 pid:1 Originate 81560 active
 dur 00:01:02 tx:2866/57320 rx:512/9289
 Tele 1/0/0 (98): tx:64180/9640/0ms g729r8 noise:-46 acom:
0  i/0:-46/-61 dBm

maui-gwy-06# show call active voice !--- <some output omitted> !--- Notice that dtmf-relay cisco rtp was successfully negotiated. VOIP:
RemoteIPAddress=172.22.10.2
RoundTripDelay=1 ms
SelectedQoS=best-effort tx_DtmfRelay=cisco-rtp FastConnect=FALSE
Separate H245 Connection=FALSE
H245 Tunneling=FALSE
SessionProtocol=cisco
SessionTarget=
VAD = enabled
CoderTypeRate=g729r8
CodecBytes=20
SignalingType=cas |
|---|

| Revision | Publish Date | Comments |
|---|---|---|
| 3.0 | 18-Aug-2026 | Recertification - Updatted Formatting. |
| 2.0 | 19-May-2025 | Updated and Recertification, reformatting. |
| 1.0 | 11-Dec-2001 | Initial Release |