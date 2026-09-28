---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr4-vcr4-cr-book-vcr-s4-html-793908d205
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr4/vcr4-cr-book/vcr-s4.html
retrieved_at: 2026-08-16T23:14:09.610108+00:00
---

Cisco IOS Voice Command Reference - S commands

# Cisco IOS Voice Command Reference - S commands

Updated: December 20, 2025

Chapter: show call history fax through show debug condition

## Chapter: show call history fax through show debug condition

# show call history fax through show debug condition

## show call history fax

To display the call
                              		  history table for fax transmissions, use the show call history fax command in user EXEC or privileged
                              		  EXEC mode.

show call history fax [ brief [ id identifier ] | compact [ duration { less | more } time ] | id identifier | last number ]

### Syntax Description

brief

(Optional) Displays a truncated version of the call history table.

id identifier

(Optional) Displays only the call with the specified identifier. Range is a hex
                                          						value from 1 to FFFF.

compact

(Optional) Displays a compact version.

duration time

(Optional) Displays history information for calls that are longer or shorter
                                          						than a specified time value. The arguments and keywords are as follows:

less--Displays calls shorter than the value in the time argument.

more--Displays calls longer than the value in the time argument.

time --Elapsed time, in seconds. Range is from 1 to
                                                							 2147483647.

last number

(Optional) Displays the last calls connected, where the number of calls that
                                          						appear is defined by the number argument . Range is from 1 to 100 .

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

11.3(1)T

This
                                          						command was introduced on the Cisco 3600 series.

12.0(3)XG

This
                                          						command was implemented for Voice over Frame Relay (VoFR) on the Cisco 2600
                                          						series and Cisco 3600 series.

12.0(4)XJ

This
                                          						command was modified for store-and-forward fax.

12.0(4)T

This
                                          						command was modified. The brief keyword
                                          						was added, and the command was implemented on the Cisco 7200 series.

12.0(7)XK

This
                                          						command was modified. The brief keyword
                                          						was implemented on the Cisco MC3810.

12.1(2)T

This
                                          						command was integrated into Cisco IOS Release 12.1(2)T.

12.1(5)XM

This
                                          						command was implemented on the Cisco AS5800.

12.1(5)XM2

This
                                          						command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XA

This
                                          						command was modified. The output of this command was modified to indicate
                                          						whether the call in question has been established using Annex E.

12.2(4)T

This
                                          						command was integrated into Cisco IOS Release 12.2(4)T.

12.2(2)XB1

This
                                          						command was implemented on the Cisco AS5850.

12.2(8)T

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco
                                          						AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 was not included in this
                                          						release.

12.2(11)T

This
                                          						command was implemented on the Cisco AS5350, Cisco AS5400, Cisco AS5800, and
                                          						Cisco AS5850.

12.3(1)

This
                                          						command was modified. The following fields were added:
                                          						FaxRelayMaxJitterBufDepth, FaxRelayJitterBufOverFlow, FaxRelayHSmodulation, and
                                          						FaxRelayNumberOfPages.

12.3(14)T

This
                                          						command was modified. T.38 fax relay call statistics were made available to
                                          						Call Detail Records (CDRs) through vendor-specific attributes (VSAs) and added
                                          						to the call log.

12.4(15)T

This
                                          						command was modified. The Port and BearerChannel display fields were added to
                                          						the TELE call leg record of the command output.

12.4(16)

This
                                          						command was modified. The Port and BearerChannel display fields were added to
                                          						the TELE call leg record of the command output.

12.4(22)T

This
                                          						command was modified. Command output was updated to show IPv6 information.

### Usage Guidelines

This command
                              		  displays a call-history table that contains a list of fax calls connected
                              		  through the router in descending time order. The maximum number of calls
                              		  contained in the table can be set to a number from 0 to 500 using the dial-control-mib command in global configuration
                              		  mode. The default maximum number of table entries is 50. Each call record is
                              		  aged out of the table after a configurable number of minutes has elapsed, also
                              		  specified by the dial-control-mib command. The default timer value
                              		  is 15 minutes.

You can display
                              		  subsets of the call history table by using specific keywords. To display the
                              		  last calls connected through this router, use the keyword last , and
                              		  define the number of calls to be displayed with the number argument.

To display a
                              		  truncated version of the call history table, use the brief keyword.

This command
                              		  applies to both on-ramp and off-ramp store-and-forward fax functions.

## Examples

The following is
                              		  sample output from the show call history fax command:

```
Router# show call history fax Telephony call-legs: 1
SIP call-legs: 0
H323 call-legs: 0
MGCP call-legs: 0
Total call-legs: 1
GENERIC:
SetupTime=590180 ms
Index=2
PeerAddress=4085452930
PeerSubAddress=
PeerId=81
PeerIfIndex=221
LogicalIfIndex=145
DisconnectCause=10  
DisconnectText=normal call clearing (16)
ConnectTime=59389
DisconnectTime=68204
CallDuration=00:01:28
CallOrigin=2
ReleaseSource=1
ChargedUnits=0
InfoType=fax
TransmitPackets=295
TransmitBytes=5292
ReceivePackets=2967
ReceiveBytes=82110
TELE:
ConnectionId=[0xD9ACDFF1 0x9F5D11D7 0x8002CF18 0xB9C3632]
IncomingConnectionId=[0xD9ACDFF1 0x9F5D11D7 0x8002CF18 0xB9C3632]
CallID=2
Port=3/0/0 (2)
BearerChannel=3/0/0.1
TxDuration=28960 ms
VoiceTxDuration=0 ms
FaxTxDuration=28960 ms
FaxRate=voice bps
FaxRelayMaxJitterBufDepth  = 0 ms
FaxRelayJitterBufOverFlow = 0
FaxRelayHSmodulation = 0
FaxRelayNumberOfPages = 0
NoiseLevel=-120
ACOMLevel=127
SessionTarget=
ImgPages=0
CallerName=
CallerIDBlocked=False
OriginalCallingNumber=4085550130
OriginalCallingOctet=0x0
OriginalCalledNumber=52930
OriginalCalledOctet=0xE9
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0xFF
TranslatedCallingNumber=4085550130
TranslatedCallingOctet=0x0
TranslatedCalledNumber=52930
TranslatedCalledOctet=0xE9
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0xFF
GwReceivedCalledNumber=52930
GwReceivedCalledOctet3=0xE9
GwReceivedCallingNumber=4085550130
GwReceivedCallingOctet3=0x0
GwReceivedCallingOctet3a=0x80
```

The table below
                              		  provides an alphabetical listing of the fields displayed in the output of the show call history fax command and a description of each
                              		  field.

Field

Description

ACOM
                                          					 Level

Current
                                          					 ACOM level for this call. ACOM is the combined loss achieved by the echo
                                          					 canceler, which is the sum of the Echo Return Loss, Echo Return Loss
                                          					 Enhancement, and nonlinear processing loss for the call.

BearerChannel

Identification of the bearer channel carrying the call.

Buffer
                                          					 Drain Events

Total
                                          					 number of jitter buffer drain events.

Buffer
                                          					 Fill Events

Total
                                          					 number of jitter buffer fill events.

CallDuration

Length of
                                          					 the call, in hours, minutes, and seconds, hh:mm:ss.

CallerName

Voice
                                          					 port station name string.

CallOrigin

Call
                                          					 origin: answer or originate.

CallState

Current
                                          					 state of the call.

ChargedUnits

Total
                                          					 number of charging units that apply to this peer since system startup. The unit
                                          					 of measure for this field is hundredths of second.

CodecBytes

Payload
                                          					 size, in bytes, for the codec used.

CoderTypeRate

Negotiated coder rate. This value specifies the send rate of voice or fax
                                          					 compression to its associated call leg for this call.

ConnectionId

Global
                                          					 call identifier for this gateway call.

ConnectTime

Time, in
                                          					 milliseconds (ms), at which the call was connected.

Consecutive-packets-lost Events

Total
                                          					 number of consecutive (two or more) packet-loss events.

Corrected
                                          					 packet-loss Events

Total
                                          					 number of packet-loss events that were corrected using the RFC 2198 method.

Dial-Peer

Tag of
                                          					 the dial peer sending this call.

DisconnectCause

Cause
                                          					 code for the reason this call was disconnected.

DisconnectText

Descriptive text explaining the reason for the disconnect.

DisconnectTime

Time, in
                                          					 ms, when this call was disconnected.

EchoCancellerMaxReflector=64

The
                                          					 location of the largest reflector, in ms. The reflector size does not exceed
                                          					 the configured echo path capacity. For example, if 32 ms is configured, the
                                          					 reflector does not report beyond 32 ms.

ERLLevel

Current
                                          					 Echo Return Loss (ERL) level for this call.

FaxTxDuration

Duration
                                          					 of fax transmission from this peer to the voice gateway for this call. You can
                                          					 derive the Fax Utilization Rate by dividing the FaxTxDuration value by the
                                          					 TxDuration value.

FaxRelayJitterBufOverFlow

Count of
                                          					 number of network jitter buffer overflows (number of packets). These packets
                                          					 are equivalent to lost packets.

FaxRelayMaxJitterBufDepth

Maximum
                                          					 depth of jitter buffer (in ms).

FaxRelayHSmodulation

Most
                                          					 recent high-speed modulation used.

FaxRelayNumberOfPages

Number of
                                          					 pages transmitted.

GapFillWithInterpolation

Duration
                                          					 of a voice signal played out with a signal synthesized from parameters, or
                                          					 samples of data preceding and following in time because voice data was lost or
                                          					 not received in time from the voice gateway for this call.

GapFillWithRedundancy

Duration
                                          					 of a voice signal played out with a signal synthesized from available
                                          					 redundancy parameters because voice data was lost or not received in time from
                                          					 the voice gateway for this call.

GapFillWithPrediction

Duration
                                          					 of the voice signal played out with signal synthesized from parameters, or
                                          					 samples of data preceding in time, because voice data was lost or not received
                                          					 in time from the voice gateway for this call. Examples of such pullout are
                                          					 frame-eraser and frame-concealment strategies in G.729 and G.723.1 compression
                                          					 algorithms.

GapFillWithSilence

Duration
                                          					 of a voice signal replaced with silence because voice data was lost or not
                                          					 received in time for this call.

GENERIC

Generic
                                          					 or common parameters, that is, parameters that are common for VoIP and
                                          					 telephony call legs.

GwReceivedCalledNumber, GwReceivedCalledOctet3, GwReceivedCallingNumber,
                                          					 GwReceivedCallingOctet3, GwReceivedCallingOctet3a

Call
                                          					 information received at the gateway.

H323
                                          					 call-legs

Total
                                          					 H.323 call legs for which call records are available.

HiWaterPlayoutDelay

High-water-mark Voice Playout FIFO Delay during this call.

ImgPages

The fax
                                          					 pages that have been processed.

Incoming
                                          					 ConnectionId

The
                                          					 incoming_GUID. It can be different with ConnectionId (GUID) when there is a
                                          					 long_pound or blast_call feature involved. In those cases, incoming_GUID is
                                          					 unique for all the subcalls that have been generated, and GUID is different for
                                          					 each subcall.

Index

Dial peer
                                          					 identification number.

InfoActivity

Active
                                          					 information transfer activity state for this call.

InfoType

Information type for this call; for example, voice or fax.

InSignalLevel

Active
                                          					 input signal level from the telephony interface used by this call.

Last
                                          					 Buffer Drain/Fill Event

Elapsed
                                          					 time since the last jitter buffer drain or fill event, in seconds.

Local UUID

Unique
                                          					 identifier generated from the originating user agent.

LogicalIfIndex

Index
                                          					 number of the logical interface for this call.

LoWaterPlayoutDelay

Low-water-mark Voice Playout FIFO Delay during this call.

LowerIFName

Physical
                                          					 lower interface information. Appears only if the medium is ATM, Frame Relay
                                          					 (FR), or High-Level Data Link Control (HDLC).

Media

Medium
                                          					 over which the call is carried. If the call is carried over the (telephone)
                                          					 access side, the entry is TELE. If the call is carried over the voice network
                                          					 side, the entry is either ATM, FR, or HDLC.

Modem
                                          					 passthrough signaling method in use

Indicates
                                          					 that this is a modem pass-through call and that named signaling events
                                          					 (NSEs)--a Cisco-proprietary version of named telephone events in RFC 2833--are
                                          					 used for signaling codec upspeed. The upspeed method is the method used to
                                          					 dynamically change the codec type and speed to meet network conditions. This
                                          					 means that you might move to a faster codec when you have both voice and data
                                          					 calls and then slow down when there is only voice traffic.

NoiseLevel

Active
                                          					 noise level for this call.

OnTimeRvPlayout

Duration
                                          					 of voice playout from data received on time for this call. Derive the Total
                                          					 Voice Playout Duration for Active Voice by adding the OnTimeRvPlayout value to
                                          					 the GapFill values.

OriginalCallingNumber, OriginalCalling Octet, OriginalCalledNumber,
                                          					 OriginalCalledOctet, OriginalRedirectCalledNumber, OriginalRedirectCalledOctet

Original
                                          					 call information regarding calling, called, and redirect numbers, as well as
                                          					 octet-3s. Octet-3s are information elements (IEs) of Q.931 that include type of
                                          					 number, numbering plan indicator, presentation indicator, and redirect reason
                                          					 information.

OutSignalLevel

Active
                                          					 output signal level to the telephony interface used by this call.

PeerAddress

Destination pattern or number associated with this peer.

PeerId

ID value
                                          					 of the peer table entry to which this call was made.

PeerIfIndex

Voice
                                          					 port index number for this peer. For ISDN media, this would be the index number
                                          					 of the B channel used for this call.

PeerSubAddress

Subaddress when this call is connected.

Percent
                                          					 Packet Loss

Total
                                          					 percent packet loss.

Port

Identification of the voice port carrying the call.

ReceiveBytes

Number of
                                          					 bytes received by the peer during this call.

ReceiveDelay

Average
                                          					 Playout FIFO Delay plus the Decoder Delay during this voice call.

ReceivePackets

Number of
                                          					 packets received by this peer during this call.

ReleaseSource

Number
                                          					 value of the release source.

RemoteIPAddress

Remote
                                          					 system IP address for the VoIP call.

RemoteUDPPort

Remote
                                          					 system User Datagram Protocol (UDP) listener port to which voice packets are
                                          					 sent.

Remote
                                          					 UUID

Unique
                                          					 identifier generated from the terminating user agent.

RoundTripDelay

Voice
                                          					 packet round-trip delay between the local and remote systems on the IP backbone
                                          					 for this call.

SelectedQoS

Selected
                                          					 Resource Reservation Protocol (RSVP) quality of service (QoS) for this call.

SessionProtocol

Session
                                          					 protocol used for an Internet call between the local and remote routers through
                                          					 the IP backbone.

SessionTarget

Session
                                          					 target of the peer used for this call.

SetupTime

Value of
                                          					 the system UpTime, in ms, when the call associated with this entry was started.

SignalingType

Signaling
                                          					 type for this call; for example, channel-associated signaling (CAS) or
                                          					 common-channel signaling (CCS).

SIP
                                          					 call-legs

Total SIP
                                          					 call legs for which call records are available.

Telephony
                                          					 call-legs

Total
                                          					 telephony call legs for which call records are available.

Time
                                          					 between Buffer Drain/Fills

Minimum
                                          					 and maximum durations between jitter buffer drain or fill events, in seconds.

TranslatedCallingNumber, TranslatedCallingOctet, TranslatedCalledNumber,
                                          					 TranslatedCalledOctet, TranslatedRedirectCalled Number,
                                          					 TranslatedRedirectCalledOctet

Translated call information.

TransmitBytes

Number of
                                          					 bytes sent by this peer during this call.

TransmitPackets

Number of
                                          					 packets sent by this peer during this call.

TxDuration

The
                                          					 length of the call. Appears only if the medium is TELE.

VAD

Whether
                                          					 voice activation detection (VAD) was enabled for this call.

VoiceTxDuration

Duration
                                          					 of voice transmission from this peer to the voice gateway for this call. Derive
                                          					 the Voice Utilization Rate by dividing the VoiceTxDuration value by the
                                          					 TxDuration value.

The following is
                              		  sample output from the show call history fax brief command:

```
Router# show call history fax brief <ID>: <start>hs.<index> +<connect> +<disc> pid:<peer_id> <direction> <addr>
 tx:<packets>/<bytes> rx:<packets>/<bytes> <disc-cause>(<text>)
 IP <ip>:<udp> rtt:<time>ms pl:<play>/<gap>ms lost:<lost>/<early>/<late>
  delay:<last>/<min>/<max>ms <codec>
 Telephony <int>: tx:<tot>/<voice>/<fax>ms <codec> noise:<lvl>dBm acom:<lvl>dBm
2    : 5996450hs.25 +-1 +3802 pid:100 Answer 408
 tx:0/0 rx:0/0 1F  (T30 T1 EOM timeout)
 Telephony : tx:38020/38020/0ms g729r8 noise:0dBm acom:0dBm
2    : 5996752hs.26 +-1 +3500 pid:110 Originate uut1@linux2.allegro.com
 tx:0/0 rx:0/0 3F  (The e-mail was not sent correctly. Remote SMTP server said: 354 )
 IP 14.0.0.1 AcceptedMime:0 DiscardedMime:0
3    : 6447851hs.27 +1111 +3616 pid:310 Originate 576341.
 tx:11/14419 rx:0/0 10  (Normal connection)
 Telephony : tx:36160/11110/25050ms g729r8 noise:115dBm acom:-14dBm
3    : 6447780hs.28 +1182 +4516 pid:0 Answer
 tx:0/0 rx:0/0 10  (normal call clearing.)
 IP 0.0.0.0 AcceptedMime:0 DiscardedMime:0
4    : 6464816hs.29 +1050 +3555 pid:310 Originate 576341.
 tx:11/14413 rx:0/0 10  (Normal connection)
 Telephony : tx:35550/10500/25050ms g729r8 noise:115dBm acom:-14dBm
4    : 6464748hs.30 +1118 +4517 pid:0 Answer
 tx:0/0 rx:0/0 10  (normal call clearing.)
 IP 0.0.0.0 AcceptedMime:0 DiscardedMime:0
5    : 6507900hs.31 +1158 +2392 pid:100 Answer 4085763413
 tx:0/0 rx:3/3224 10  (Normal connection)
 Telephony : tx:23920/11580/12340ms g729r8 noise:0dBm acom:0dBm
5    : 6508152hs.32 +1727 +2140 pid:110 Originate uut1@linux2.allegro.com
 tx:0/2754 rx:0/0 3F  (service or option not available, unspecified)
 IP 14.0.0.4 AcceptedMime:0 DiscardedMime:0
6    : 6517176hs.33 +1079 +3571 pid:310 Originate 576341.
 tx:11/14447 rx:0/0 10  (Normal connection)
 Telephony : tx:35710/10790/24920ms g729r8 noise:115dBm acom:-14dBm
6    : 6517106hs.34 +1149 +4517 pid:0 Answer
 tx:0/0 rx:0/0 10  (normal call clearing.)
 IP 0.0.0.0 AcceptedMime:0 DiscardedMime:0
7    : 6567382hs.35 +1054 +3550 pid:310 Originate 576341.
 tx:11/14411 rx:0/0 10  (Normal connection)
 Telephony : tx:35500/10540/24960ms g729r8 noise:115dBm acom:-14dBm
7    : 6567308hs.36 +1128 +4517 pid:0 Answer
tx:0/0 rx:0/0 10  (normal call clearing.)
 IP 0.0.0.0 AcceptedMime:0 DiscardedMime:0
```

The following
                              		  example shows output for the show call history fax command with the T.38 Fax Relay statistics:

```
Router# show call history fax Telephony call-legs: 1
SIP call-legs: 0
H323 call-legs: 0
MGCP call-legs: 0
Total call-legs: 1
GENERIC:
SetupTime=9872460 ms
Index=8
PeerAddress=41023
PeerSubAddress=
PeerId=1
PeerIfIndex=242
LogicalIfIndex=180
DisconnectCause=10  
DisconnectText=normal call clearing (16)
ConnectTime=9875610 ms
DisconnectTime=9936000 ms
CallDuration=00:01:00 sec
CallOrigin=2
ReleaseSource=1
ChargedUnits=0
InfoType=fax
TransmitPackets=268
TransmitBytes=4477
ReceivePackets=1650
ReceiveBytes=66882
TELE:
ConnectionId=[0xD6635DD5 0x9FA411D8 0x8005000A 0xF4107CA0]
IncomingConnectionId=[0xD6635DD5 0x9FA411D8 0x8005000A 0xF4107CA0]
CallID=7
Port=3/0/0:0 (7)
BearerChannel=3/0/0.8
TxDuration=6170 ms
VoiceTxDuration=0 ms
FaxTxDuration=0 ms
FaxRate=disable bps
FaxRelayMaxJitterBufDepth=560 ms
FaxRelayJitterBufOverFlow=0
FaxRelayMostRecentHSmodulation=V.17/short/14400
FaxRelayNumberOfPages=1
FaxRelayInitHSmodulation=V.17/long/14400
FaxRelayDirection=Transmit
FaxRelayPktLossConceal=0
FaxRelayEcmStatus=ENABLED
FaxRelayEncapProtocol=T.38 (UDPTL)
FaxRelayNsfCountryCode=Japan
FaxRelayNsfManufCode=0031B8EE80C48511DD0D0000DDDD0000DDDD000000000000000022ED00B0A400
FaxRelayFaxSuccess=Success
NoiseLevel=0
ACOMLevel=0
SessionTarget=
ImgPages=0
CallerName=Analog 41023
CallerIDBlocked=False
OriginalCallingNumber=
OriginalCallingOctet=0x80
OriginalCalledNumber=41021
OriginalCalledOctet=0xA1
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0xFF
TranslatedCallingNumber=41023
TranslatedCallingOctet=0x80
TranslatedCalledNumber=41021
TranslatedCalledOctet=0xA1
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0xFF
GwReceivedCalledNumber=41021
GwReceivedCalledOctet3=0xA1
```

The table below
                              		  describes the fields not shown in the table above.

Field

Description

FaxRelayDirection

Direction
                                          					 of fax relay.

FaxRelayEcmStatus

Fax relay
                                          					 error correction mode status.

FaxRelayEncapProtocol

Fax relay
                                          					 encapsulation protocol.

FaxRelayFaxSuccess

Fax relay
                                          					 success.

FaxRelayInitHSmodulation

Fax relay
                                          					 initial high speed modulation.

FaxRelayMostRecentHSmodulation

Fax relay
                                          					 most recent high speed modulation.

FaxRelayNsfCountryCode

Fax relay
                                          					 Nonstandard Facilities (NSF) country code.

FaxRelayNsfManufCode

Fax relay
                                          					 NSF manufacturers code.

FaxRelayPktLossConceal

Fax relay
                                          					 packet loss conceal.

### Related Commands

Command

Description

dial-control-mib

Specifies attributes for the call history table.

show call active fax

Displays call information for fax transmissions that are in progress.

show call active voice

Displays call information for voice calls that are in progress.

show call history voice

Displays the call history table for voice calls.

show dial-peer voice

Displays configuration information for dial peers.

show num-exp

Displays how the number expansions are configured in VoIP.

show voice port

Displays configuration information about a specific voice port.

## show call history media

To display the call history table for media calls, use the show call history media command in user EXEC or privileged EXEC mode.

show call history media [ [ brief ] [ id identifier ] | compact [ duration { less | more } seconds ] | last number ]

### Syntax Description

brief

(Optional) Displays a truncated version of the call history table.

id identifier

(Optional) Displays only the call with the specified identifier . The range is from 1 to FFFF.

compact

(Optional) Displays a compact version of the call history table.

duration

(Optional) Displays the call history for the specified time duration.

less

Displays the call history for shorter duration calls.

more

Displays the call history for longer duration calls.

seconds

Time, in seconds. The range is from 1 to 2147483647.

last number

(Optional) Displays the last calls connected, where the number of calls that appear is defined by the number argument . The range is from 1 to 100 .

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

12.4(15)T

This command was introduced.

### Usage Guidelines

This command displays a call-history table that contains a list of media calls connected through the router in descending
                              time order. The maximum number of calls contained in the table can be set to a number from 0 to 500 using the dial-control-mib command in global configuration mode. The default maximum number of table entries is 50. Each call record is aged out of
                              the table after a configurable number of minutes has elapsed, also specified by the dial-control-mib command. The default timer value is 15 minutes.

You can display subsets of the call history table by using specific keywords. To display the last calls connected through
                              this router, use the last keyword, and define the number of calls to be displayed with the number argument.

To display a truncated version of the call history table, use the brief keyword.

When a media call is active, you can display its statistics by using the show call active media command.

## Examples

The following is sample output from the show call history media command:

```
Router# show call history media Telephony call-legs: 0
SIP call-legs: 0
H323 call-legs: 0
Call agent controlled call-legs: 0
Media call-legs: 4
Total call-legs: 4
GENERIC:
SetupTime=308530 ms
Index=4
PeerAddress=sip:mrcpv2ASRServer@10.5.18.224:5060
PeerSubAddress=
PeerId=2234
PeerIfIndex=184
LogicalIfIndex=0
DisconnectCause=10  
DisconnectText=normal call clearing (16)
ConnectTime=309440 ms
DisconnectTime=320100 ms
CallDuration=00:00:10 sec
CallOrigin=1
ReleaseSource=7
ChargedUnits=0
InfoType=speech
TransmitPackets=237
TransmitBytes=37920
ReceivePackets=0
ReceiveBytes=0
VOIP:
ConnectionId[0x2FB5B737 0xC3511DB 0x8005000B 0x5FDA0EF4]
IncomingConnectionId[0x2FB5B737 0xC3511DB 0x8005000B 0x5FDA0EF4]
CallID=14
RemoteIPAddress=10.5.18.224
RemoteUDPPort=10002
RemoteSignallingIPAddress=10.5.18.224
RemoteSignallingPort=5060
RemoteMediaIPAddress=10.5.18.224
RemoteMediaPort=10002
SRTP = off
TextRelay = off
Fallback Icpif=0
Fallback Loss=0
Fallback Delay=0
RoundTripDelay=0 ms
SelectedQoS=best-effort
tx_DtmfRelay=rtp-nte
FastConnect=FALSE
AnnexE=FALSE
Separate H245 Connection=FALSE
H245 Tunneling=FALSE
SessionProtocol=sipv2
ProtocolCallId=2FBDA670-C3511DB-8015C48C-6A894889@10.5.14.2
SessionTarget=10.5.18.224
OnTimeRvPlayout=3000
GapFillWithSilence=0 ms
GapFillWithPrediction=0 ms
GapFillWithInterpolation=2740 ms
GapFillWithRedundancy=0 ms
HiWaterPlayoutDelay=100 ms
LoWaterPlayoutDelay=40 ms
Source tg label=test5
ReceiveDelay=90 ms
LostPackets=0
EarlyPackets=0
LatePackets=0
VAD = disabled
CoderTypeRate=g711ulaw
CodecBytes=160
cvVoIPCallHistoryIcpif=16
MediaSetting=flow-around
CallerName=
CallerIDBlocked=False
OriginalCallingNumber=
OriginalCallingOctet=0x0
OriginalCalledNumber=
OriginalCalledOctet=0x0
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0x0
TranslatedCallingNumber=555-0100
TranslatedCallingOctet=0x21
TranslatedCalledNumber=
TranslatedCalledOctet=0xC1
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0xFF
GwOutpulsedCallingNumber=555-0101
GwOutpulsedCallingOctet3=0x21
GwOutpulsedCallingOctet3a=0x81
MediaInactiveDetected=no
MediaInactiveTimestamp=
MediaControlReceived=
LongDurationCallDetected=no
LongDurationCallTimerStamp=
LongDurationCallDuration=
Username=
GENERIC:
SetupTime=308520 ms
Index=5
PeerAddress=sip:mrcpv2TTSServer@10.5.18.224:5060
PeerSubAddress=
PeerId=2235
PeerIfIndex=185
LogicalIfIndex=0
DisconnectCause=10  
DisconnectText=normal call clearing (16)
ConnectTime=309370 ms
DisconnectTime=320100 ms
CallDuration=00:00:10 sec
CallOrigin=1
ReleaseSource=7
ChargedUnits=0
InfoType=speech
TransmitPackets=0
TransmitBytes=0
ReceivePackets=551
ReceiveBytes=88160
VOIP:
ConnectionId[0x2FB5B737 0xC3511DB 0x8005000B 0x5FDA0EF4]
IncomingConnectionId[0x2FB5B737 0xC3511DB 0x8005000B 0x5FDA0EF4]
CallID=13
RemoteIPAddress=10.5.18.224
RemoteUDPPort=10000
RemoteSignallingIPAddress=10.5.18.224
RemoteSignallingPort=5060
RemoteMediaIPAddress=10.5.18.224
RemoteMediaPort=10000
SRTP = off
TextRelay = off
Fallback Icpif=0
Fallback Loss=0
Fallback Delay=0
RoundTripDelay=0 ms
SelectedQoS=best-effort
tx_DtmfRelay=rtp-nte
FastConnect=FALSE
AnnexE=FALSE
Separate H245 Connection=FALSE
H245 Tunneling=FALSE
SessionProtocol=sipv2
ProtocolCallId=2FBC6E20-C3511DB-8013C48C-6A894889@10.5.14.2
SessionTarget=10.5.18.224
OnTimeRvPlayout=7000
GapFillWithSilence=0 ms
GapFillWithPrediction=0 ms
GapFillWithInterpolation=2740 ms
GapFillWithRedundancy=0 ms
HiWaterPlayoutDelay=100 ms
LoWaterPlayoutDelay=40 ms
Source tg label=test5
ReceiveDelay=95 ms
LostPackets=0
EarlyPackets=0
LatePackets=0
VAD = disabled
CoderTypeRate=g711ulaw
CodecBytes=160
cvVoIPCallHistoryIcpif=16
MediaSetting=flow-around
CallerName=
CallerIDBlocked=False
OriginalCallingNumber=
OriginalCallingOctet=0x0
OriginalCalledNumber=
OriginalCalledOctet=0x0
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0x0
TranslatedCallingNumber=555-0102
TranslatedCallingOctet=0x21
TranslatedCalledNumber=
TranslatedCalledOctet=0xC1
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0xFF
GwOutpulsedCallingNumber=555-0103
GwOutpulsedCallingOctet3=0x21
GwOutpulsedCallingOctet3a=0x81
MediaInactiveDetected=no
MediaInactiveTimestamp=
MediaControlReceived=
LongDurationCallDetected=no
LongDurationCallTimerStamp=
LongDurationCallDuration=
Username=
GENERIC:
SetupTime=408050 ms
Index=7
PeerAddress=sip:mrcpv2ASRServer@10.5.18.224:5060
PeerSubAddress=
PeerId=2234
PeerIfIndex=184
LogicalIfIndex=0
DisconnectCause=10  
DisconnectText=normal call clearing (16)
ConnectTime=408160 ms
DisconnectTime=426260 ms
CallDuration=00:00:18 sec
CallOrigin=1
ReleaseSource=7
ChargedUnits=0
InfoType=speech
TransmitPackets=598
TransmitBytes=95680
ReceivePackets=0
ReceiveBytes=0
VOIP:
ConnectionId[0x6B02FC0C 0xC3511DB 0x8006000B 0x5FDA0EF4]
IncomingConnectionId[0x6B02FC0C 0xC3511DB 0x8006000B 0x5FDA0EF4]
CallID=19
RemoteIPAddress=10.5.18.224
RemoteUDPPort=10002
RemoteSignallingIPAddress=10.5.18.224
RemoteSignallingPort=5060
RemoteMediaIPAddress=10.5.18.224
RemoteMediaPort=10002
SRTP = off
TextRelay = off
Fallback Icpif=0
Fallback Loss=0
Fallback Delay=0
RoundTripDelay=0 ms
SelectedQoS=best-effort
tx_DtmfRelay=rtp-nte
FastConnect=FALSE
AnnexE=FALSE
Separate H245 Connection=FALSE
H245 Tunneling=FALSE
SessionProtocol=sipv2
ProtocolCallId=6B0E94CD-C3511DB-801DC48C-6A894889@10.5.14.2
SessionTarget=10.5.18.224
OnTimeRvPlayout=11000
GapFillWithSilence=0 ms
GapFillWithPrediction=0 ms
GapFillWithInterpolation=9560 ms
GapFillWithRedundancy=0 ms
HiWaterPlayoutDelay=100 ms
LoWaterPlayoutDelay=55 ms
Source tg label=test5
ReceiveDelay=100 ms
LostPackets=0
EarlyPackets=0
LatePackets=0
VAD = disabled
CoderTypeRate=g711ulaw
CodecBytes=160
cvVoIPCallHistoryIcpif=16
MediaSetting=flow-around
CallerName=
CallerIDBlocked=False
OriginalCallingNumber=
OriginalCallingOctet=0x0
OriginalCalledNumber=
OriginalCalledOctet=0x0
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0x0
TranslatedCallingNumber=555-0100
TranslatedCallingOctet=0x21
TranslatedCalledNumber=
TranslatedCalledOctet=0xC1
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0xFF
GwOutpulsedCallingNumber=555-0101
GwOutpulsedCallingOctet3=0x21
GwOutpulsedCallingOctet3a=0x81
MediaInactiveDetected=no
MediaInactiveTimestamp=
MediaControlReceived=
LongDurationCallDetected=no
LongDurationCallTimerStamp=
LongDurationCallDuration=
Username=
GENERIC:
SetupTime=408040 ms
Index=8
PeerAddress=sip:mrcpv2TTSServer@10.5.18.224:5060
PeerSubAddress=
PeerId=2235
PeerIfIndex=185
LogicalIfIndex=0
DisconnectCause=10  
DisconnectText=normal call clearing (16)
ConnectTime=408130 ms
DisconnectTime=426260 ms
CallDuration=00:00:18 sec
CallOrigin=1
ReleaseSource=7
ChargedUnits=0
InfoType=speech
TransmitPackets=0
TransmitBytes=0
ReceivePackets=911
ReceiveBytes=145760
VOIP:
ConnectionId[0x6B02FC0C 0xC3511DB 0x8006000B 0x5FDA0EF4]
IncomingConnectionId[0x6B02FC0C 0xC3511DB 0x8006000B 0x5FDA0EF4]
CallID=18
RemoteIPAddress=10.5.18.224
RemoteUDPPort=10000
RemoteSignallingIPAddress=10.5.18.224
RemoteSignallingPort=5060
RemoteMediaIPAddress=10.5.18.224
RemoteMediaPort=10000
SRTP = off
TextRelay = off
Fallback Icpif=0
Fallback Loss=0
Fallback Delay=0
RoundTripDelay=0 ms
SelectedQoS=best-effort
tx_DtmfRelay=rtp-nte
FastConnect=FALSE
AnnexE=FALSE
Separate H245 Connection=FALSE
H245 Tunneling=FALSE
SessionProtocol=sipv2
ProtocolCallId=6B0CC055-C3511DB-801BC48C-6A894889@10.5.14.2
SessionTarget=10.5.18.224
OnTimeRvPlayout=9000
GapFillWithSilence=0 ms
GapFillWithPrediction=0 ms
GapFillWithInterpolation=9560 ms
GapFillWithRedundancy=0 ms
HiWaterPlayoutDelay=100 ms
LoWaterPlayoutDelay=55 ms
Source tg label=test5
ReceiveDelay=100 ms
LostPackets=0
EarlyPackets=0
LatePackets=0
VAD = disabled
CoderTypeRate=g711ulaw
CodecBytes=160
cvVoIPCallHistoryIcpif=16
MediaSetting=flow-around
CallerName=
CallerIDBlocked=False
OriginalCallingNumber=
OriginalCallingOctet=0x0
OriginalCalledNumber=
OriginalCalledOctet=0x0
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0x0
TranslatedCallingNumber=555-0100
TranslatedCallingOctet=0x21
TranslatedCalledNumber=
TranslatedCalledOctet=0xC1
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0xFF
GwOutpulsedCallingNumber=555-0101
GwOutpulsedCallingOctet3=0x21
GwOutpulsedCallingOctet3a=0x81
MediaInactiveDetected=no
MediaInactiveTimestamp=
MediaControlReceived=
LongDurationCallDetected=no
LongDurationCallTimerStamp=
LongDurationCallDuration=
Username=
```

The table below describes the significant fields shown in the display, in alphabetical order.

Field

Description

CallDuration

Length of the call, in hours, minutes, and seconds, hh:mm:ss.

CallOrigin

Call origin: not answer or originate.

ChargedUnits

Total number of charging units that apply to this peer since system startup. The unit of measure for this field is hundredths
                                          of second.

CodecBytes

Payload size, in bytes, for the codec used.

CoderTypeRate

Negotiated coder rate. This value specifies the send rate of voice or fax compression to its associated call leg for this
                                          call.

ConnectionId

Global call identifier for this gateway call.

ConnectTime

Time, in ms, during which the call was connected.

GapFillWithInterpolation

Duration, in ms, of a voice signal played out with a signal synthesized from parameters, or samples of data preceding and
                                          following in time because voice data was lost or not received in time from the voice gateway for this call.

GapFillWithRedundancy

Duration, in ms, of a voice signal played out with a signal synthesized from available redundancy parameters because voice
                                          data was lost or not received in time from the voice gateway for this call.

GapFillWithPrediction

Duration, in ms, of the voice signal played out with a signal synthesized from parameters, or samples of data preceding in
                                          time, because voice data was lost or not received in time from the voice gateway for this call. Examples of such pullout are
                                          frame-eraser and frame-concealment strategies in G.729 and G.723.1 compression algorithms.

GapFillWithSilence

Duration, in ms, of a voice signal replaced with silence because voice data was lost or not received in time for this call.

GENERIC

Generic or common parameters; that is, parameters that are common for VoIP and telephony call legs.

H323 call-legs

Total H.323 call legs for which call records are available.

HiWaterPlayoutDelay

High-water-mark voice playout first in first out (FIFO) Delay during this call, in ms.

Index

Dial peer identification number.

InfoType

Information type for this call; for example, voice, speech, or fax.

LogicalIfIndex

Index number of the logical interface for this call.

LoWaterPlayoutDelay

Low-water-mark voice playout FIFO delay during this call, in ms.

OnTimeRvPlayout

Duration of voice playout from data received on time for this call. Derive the Total Voice Playout Duration for Active Voice
                                          by adding the OnTimeRvPlayout value to the GapFill values.

PeerAddress

Destination pattern or number associated with this peer.

PeerId

ID value of the peer table entry to which this call was made.

PeerIfIndex

Voice port index number for this peer. For ISDN media, this would be the index number of the B channel used for this call.

PeerSubAddress

Subaddress when this call is connected.

ReceiveBytes

Number of bytes received by the peer during this call.

ReceiveDelay

Average playout FIFO delay plus the decoder delay during this voice call, in ms.

ReceivePackets

Number of packets received by this peer during this call.

ReleaseSource

Number value of the release source.

RemoteIPAddress

Remote system IP address for the VoIP call.

RemoteUDPPort

Remote system User Datagram Protocol (UDP) listener port to which voice packets are sent.

RoundTripDelay

Voice packet round-trip delay, in ms, between the local and remote systems on the IP backbone for this call.

SelectedQoS

Selected Resource Reservation Protocol (RSVP) quality of service (QoS) for this call.

SessionProtocol

Session protocol used for an Internet call between the local and remote routers through the IP backbone.

SessionTarget

Session target of the peer used for this call.

SetupTime

Value of the system UpTime, in ms, when the call associated with this entry was started.

SIP call-legs

Total Session Initiation Protocol (SIP) call legs for which call records are available.

Telephony call-legs

Total telephony call legs for which call records are available.

TransmitBytes

Number of bytes sent by this peer during this call.

TransmitPackets

Number of packets sent by this peer during this call.

VAD

Whether voice activation detection (VAD) was enabled for this call.

### Related Commands

Command

Description

dial-control-mib

Sets the maximum number of calls contained in the table.

show call active media

Displays call information for media calls in progress.

## show call history stats

To display the statistics of call history, use show call history stats command in privileged EXEC mode.

show call history stats { connected table | cps { details | table } | short-duration

## Syntax Description

Displays call statistics for connected calls.

(Optional) Displays call statistics for connected calls in tabular format.

Displays call statistics in calls handled per second format.

Displays call statistics in calls handled per second format including call-leg rate.

Displays call statistics in calls handled per second format including call-leg rate in tabular format

Displays the call statistics for short-duration calls. By default, any call with total duration less than 5 seconds is considered
                                       as a short duration call. You can change the default value using Management Information Base (MIB).

### Command Modes

Privileged EXEC (#)

## Command History

Cisco IOS XE Release 3.8

This command was introduced.

### Usage Guidelines

Use show call history stats connected command to display statistics of connected calls in graphical format.

```
Device#show call history stats connected 

                                                                
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          Connected Calls (last 60 seconds)
          # = Connected calls handled by the module

                                                                  
                                                                  
                                                     369963146641 
                                                    8880000440044 
                                                    8880077990066 
  910                                                  **         
  820                                                  #*         
  730                                                 *##         
  640                                                 *##*   **   
  550                                                 ###*   ##   
  460                                                 ####  *##*  
  370                                                *####  *##*  
  280                                                #####* ####  
  190                                                ######*####* 
  100                                               *######*####* 
   10                                               ############# 
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          Connected Calls (last 60 minutes)
          * = maximum Connected calls    # = average Connected calls

                                                                              
                                                                              
      9                                                                       
      0                                                                       
      0                                                                       
  970                                                                         
  890 *                                                                       
  810 *                                                                       
  730 *                                                                       
  650 *                                                                       
  570 *                                                                       
  490 *                                                                       
  410 *                                                                       
  330 *                                                                       
  250 *                                                                       
  170 #                                                                       
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          Connected Calls (last 72 hours)
          * = maximum Connected calls    # = average Connected calls
```

The following section describes how to interpret the graphical data:

Connected calls for the last 60 seconds —The graph displays the number of connected calls in the last 60 seconds. X-axis represents the time in seconds and Y-axis
                                    represents the number of connected calls. # represents the number of connected calls.

For example, in the following graph, 15 calls were connected at the 2nd second.

```
1                  
       1122334455667788990998877665544332211                        
       5050505050505061505050505050505050505                       
  100                   ###                                         
   90                 #######                                       
   80               ###########                                     
   70             ###############                                   
   60           ###################                                 
   50         #######################                               
   40       ###########################                             
   30     ###############################                           
   20    ##################################                         
   10  #####################################                       
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
```

Connected calls for the last 60 minutes —The graph displays the number of connected calls in the last 60 minutes. X-axis represents the time in minutes and Y-axis
                                    represents the number of connected calls. The values on the Y-axis vary based on the number of connected calls. * represents the maximum number of connected calls. # represents the average number of connected calls. The maximum number of connected calls over a minute is calculated by taking
                                    the average of 3 maximum values of connected calls over the 60 seconds in that minute.

For example, in the following graph, on the 48th minute, a maximum of 383 calls were connected and average calls were 10.

```
369863146641 
                                                    8880900440044 
                                                    3330922440011 
  910                                                  **         
  820                                                  #*         
  730                                                  ##         
  640                                                 *##*   **   
  550                                                 ###*   ##   
  460                                                 ####  *##*  
  370                                                *####  *##*  
  280                                                #####* ####  
  190                                                ###### ####  
  100                                               *######*####* 
   10                                               ############# 
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          Connected Cube Calls (last 60 minutes)
          * = maximum Connected calls    # = average Connected calls
```

Connected calls for the last 72 hours —The graph displays the number of connected calls in the last 72 hours. X-axis represents the time in hours and Y-axis represents
                                    the number of connected calls. The values on the Y-axis vary based on the number of connected calls. * represents the maximum number of connected calls. # represents the average number of connected calls. The maximum connected calls over each hour are the same as the maximum
                                    connected calls over the minutes in that hour.

For example, in the following graph, during the first hour, a maximum of 900 calls were connected and average calls were 170.

```
9                                                                       
      0                                                                       
      0                                                                       
  970                                                                         
  890 *                                                                       
  810 *                                                                       
  730 *                                                                       
  650 *                                                                       
  570 *                                                                       
  490 *                                                                       
  410 *                                                                       
  330 *                                                                       
  250 *                                                                       
  170 #                                                                       
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          Connected Cube Calls (last 72 hours)
          * = maximum Connected calls    # = average Connected calls
```

Use table keyword to display the connected call statistics in tabular format. The output includes the following tables:

Connected calls for the last 60 seconds

Connected calls for the last 60 minutes

Connected calls for the last 72 hours

## Examples

```
Device#show call history stats connected table 

   11:01:44 AM Thursday Aug 29 2019 IST

Connected Calls  (last 60 seconds)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0

Connected Calls  (last 60 minutes)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50        324        900
51-55        343        900
56-60        292        600

          
Connected Calls  (last 72 hours)
Period     Average       Max
----------------------------
 1-5          35        900
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0
61-65          0          0
66-70          0          0
71-72          0          0
```

## Examples

```
Device#show call history stats cps

   10:26:05 AM Wednesday Sep 25 2019 UTC

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          Call switching rate / CPS (last 60 seconds)
          # = calls handled by the module per second

                                                                  
                                                                  
                                                                  
                                                                  
                                   11                             
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                              **                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          Call switching rate / CPS  (last 60 minutes)
          * = maximum calls/s    # = average calls/s

                                                                              
                                                                              
                                                                              
                                                                              
      1                                                                       
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1 *                                                                       
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          Call switching rate / CPS (last 72 hours)
          * = maximum calls/s    # = average calls/s
```

## Examples

```
Device#show call history stats cps detail 

   10:23:27 AM Wednesday Sep 25 2019 UTC

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          Call switching rate / CPS (last 60 seconds)
          # = calls handled by the module per second

                                                                  
                                                                  
                                                                  
                                                                  
                                 11                               
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                            **                               
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          Call switching rate / CPS  (last 60 minutes)
          * = maximum calls/s    # = average calls/s

                                                                              
                                                                              
                                                                              
                                                                              
      1                                                                       
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1 *                                                                       
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          Call switching rate / CPS (last 72 hours)
          * = maximum calls/s    # = average calls/s

   10:23:27 AM Wednesday Sep 25 2019 UTC

                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                                                             
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          Call-leg switching rate (last 60 seconds)
          # = call legs handled by the module per second

                                                                  
                                                                  
                                                                  
                                                                  
                                 11                               
   10                                                             
    9                                                             
    8                                                             
    7                                                             
    6                                                             
    5                                                             
    4                                                             
    3                                                             
    2                                                             
    1                            **                               
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
          Call-leg switching rate (last 60 minutes)
          * = maximum call-legs/s    # = average call-legs/s

                                                                              
                                                                              
                                                                              
                                                                              
      1                                                                       
   10                                                                         
    9                                                                         
    8                                                                         
    7                                                                         
    6                                                                         
    5                                                                         
    4                                                                         
    3                                                                         
    2                                                                         
    1 *                                                                       
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
          Call-leg switching rate (last 72 hours)
          * = maximum call-legs/s    # = average call-legs/s
```

## Examples

```
Device#show call history stats cps table

 10:26:50 AM Wednesday Sep 25 2019 UTC

Call switching rate / CPS (last 60 seconds)
Period     Actual     Average
-----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0

Call switching rate / CPS (last 60 minutes)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          1
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0

Call switching rate / CPS (last 72 hours)
Period     Average       Max
----------------------------
 1-5           0          1
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0
61-65          0          0
66-70          0          0
71-72          0          0
```

## show call history video

To display call history information for signaling connection control protocol (SCCP) video calls, use the show call history video command in user EXEC or privileged EXEC mode.

show call history video [ [ brief ] [ id identifier ] | compact [ duration { less | more } seconds ] | last number ]

### Syntax Description

brief

(Optional) Displays a truncated version of video call history information.

id identifier

(Optional) Displays only the video call history with the specified identifier. Range is a hexadecimal value from 1 to FFFF.

compact

(Optional) Displays a compact version of video call history information.

duration

(Optional) Displays the call history for the specified time duration.

less

Displays the call history for shorter duration calls.

more

Displays the call history for longer duration calls.

seconds

Time, in seconds. The range is from 1 to 2147483647.

last number

(Optional) Displays the last calls connected, where the number of calls that appear is defined by the number argument . The range is from 1 to 100 .

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release 12.4(9)T.

12.4(16); 12.4(15)T

Cisco Unified CME 4.0

This command was modified. The Port and BearerChannel display fields were added to the TELE call leg record of the command
                                          output.

## Examples

The following is sample output from the show call history video command with the compact option:

```
Router# show call history video compact <callID>  A/O FAX T<sec> Codec       type        Peer Address       IP R<ip>:<udp>
Total call-legs: 2
       241      ANS     T17    g729r8      VOIP        P555-0100          192.0.2.0:16926
       242      ORG     T17    g729r8      TELE-VIDEO  P555-0101
```

The table below describes the significant fields shown in the display.

Field

Description

callID

Unique identifier for the call leg.

A/O

Call leg was an answer (ANS) or an originator (ORG).

FAX

Fax number for the call leg.

T<sec>

Duration in seconds.

Codec

Codec used for this call leg.

type

Call type for this call leg.

Peer Address

Called or calling number of the remote peer.

IP R<ip>:<udp>

IP address and port number

Total call-legs

Total number of call legs for this call.

### Related Commands

Command

Description

show call active video

Displays call information for SCCP video calls in progress.

## show call history video record

To display information about incoming and outgoing video calls, use the s how call history video record command in privileged EXEC mode.

show call history video record

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(5)XK

This command was introduced on the Cisco MC3810.

12.0(7)T

This command was integrated into Cisco IOS Release 12.0(7)T.

## Examples

The following example displays information about two video calls:

```
Router# show call history video record CallId = 4
CalledNumber = 221
CallDuration = 39006 seconds
DisconnectText = remote hangup
SVC: call ID = 8598630
Remote NSAP = 47.0091810000000002F26D4901.00107B09C645.C8
Local NSAP = 47.0091810000000002F26D4901.00107B4832E1.C8
vcd = 414, vpi = 0, vci = 158
SerialPort = Serial0
VideoSlot = 1, VideoPort = 0
CallId = 3
CalledNumber = 221
CallDuration = 557 seconds
DisconnectText = local hangup
SVC: call ID = 8598581
Remote NSAP = 47.0091810000000002F26D4901.00107B09C645.C8
Local NSAP = 47.0091810000000002F26D4901.00107B4832E1.C8
vcd = 364, vpi = 0, vci = 108
SerialPort = Serial0
VideoSlot = 1, VideoPort = 0
```

## show call history voice

To display the call history table for voice calls, use the show call history voice command in user EXEC or privileged EXEC mode.

show call history voice [ brief [ id identifier ] | compact [ duration { less | more } seconds ] | dest-route-string tag | id identifier | last number | redirect { rtpvt | tbct } | stats ]

### Syntax Description

brief

(Optional) Displays a truncated version of the call history table.

id identifier

(Optional) Displays only the call with the specified identifier. Range is from 1 to FFFF.

compact

(Optional) Displays a compact version of the call history table.

dest-route-string tag

(Optional) Displays only the call with the specified destination route tag value. The range is from 1 to 10000.

duration seconds

(Optional) Displays history information for calls that are longer or shorter than the value of the specified seconds argument. The arguments and keywords are as follows:

less --Displays calls shorter than the seconds value.

more --Displays calls longer than the seconds value.

seconds --Elapsed time, in seconds. Range is from 1 to 2147483647.

last number

(Optional) Displays the last calls connected, where the number of calls that appear is defined by the number argument . Range is from 1 to 100 .

redirect

(Optional) Displays information about calls that were redirected using Release-to-Pivot (RTPvt) or Two B-Channel Transfer
                                          (TBCT). The keywords are as follows:

rtpvt --Displays information about RTPvt calls.

tbct --Displays information about TBCT calls.

stats

(Optional) Displays information about digital signal processing (DSP) voice quality metrics.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 3600 series.

12.0(3)XG

Support was added for Voice over Frame Relay (VoFR) on the Cisco 2600 series and Cisco 3600 series.

12.0(4)XJ

This command was modified for store-and-forward fax.

12.0(4)T

The brief keyword was added, and the command was implemented on the Cisco 7200 series.

12.0(5)XK

This command was implemented on the Cisco MC3810.

12.0(7)XK

The brief keyword was implemented on the Cisco MC3810.

12.0(7)T

This command was integrated into Cisco IOS Release 12.0(7)T.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.1(5)XM

This command was implemented on the Cisco AS5800.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XA

The output of this command was modified to indicate whether a specified call has been established using Annex E.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T. Support was not included for the Cisco AS5350, Cisco AS5400,
                                          Cisco AS5800, and Cisco AS5850.

12.2(11)T

Support was added for Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850.

12.2(13)T

The ReleaseSource field was added to the Field Description table, and the record keyword was deleted from the command name.

12.3(1)

The redirect keyword was added.

12.4(2)T

The LocalHostname display field was added to the VoIP call leg record.

12.4(11)XW

The stats keyword was added.

12.4(15)T

The Port and BearerChannel display fields were added to the TELE call leg record of the command output.

12.4(16)

The Port and BearerChannel display fields were added to the TELE call leg record of the command output.

12.4(22)T

Command output was updated to show IPv6 information.

15.3(3)M

This command was modified. The dest-route-string keyword was added.

Cisco IOS XE Release 3.10S

This command was integrated into Cisco IOS XE Release 3.10S.

### Usage Guidelines

This command displays a call-history table that contains a list of voice calls connected through the router in descending
                              time order. The maximum number of calls contained in the table can be set to a number from 0 to 500 using the dial-control-mib command in global configuration mode. The default maximum number of table entries is 50. Each call record is aged out of the
                              table after a configurable number of minutes has elapsed. The timer value is also specified by the dial-control-mib command. The default timer value is 15 minutes.

You can display subsets of the call history table by using specific keywords. To display the last calls connected through
                              this router, use the last keyword, and define the number of calls to be displayed with the number argument.

To display a truncated version of the call history table, use the brief keyword.

Use the show call active voice redirect command to review records for calls that implemented RTPvt or TBCT.

When a call is active, you can display its statistics by using the show call active voice command.

Use the show call active voice dest-route-string command to display only the active voice calls with call routing configured using specified destination-route-string globally
                              and at the dial-peer level.

## Examples

The following is sample output from the show call history voice command:

```
Router# show call history voice GENERIC:
SetupTime=104648 ms
Index=1
PeerAddress=55240
PeerSubAddress=
PeerId=2
PeerIfIndex=105
LogicalIfIndex=0
DisconnectCause=10
DisconnectText=normal call clearing.
ConnectTime=104964
DisconectTime=143329
CallDuration=00:06:23
CallOrigin=1
ChargedUnits=0
InfoType=speech
TransmitPackets=37668
TransmitBytes=6157536
ReceivePackets=37717
ReceiveBytes=6158452
VOIP:
ConnectionId[0x4B091A27 0x3EDD0003 0x0 0xFEFD4]
CallID=2
RemoteIPAddress=10.14.82.14
RemoteUDPPort=18202
RoundTripDelay=2 ms
SelectedQoS=best-effort
tx_DtmfRelay=inband-voice
FastConnect=TRUE
SessionProtocol=cisco
SessionTarget=ipv4:10.14.82.14
OnTimeRvPlayout=40
GapFillWithSilence=0 ms
GapFillWithPrediction=0 ms
GapFillWithInterpolation=0 ms
GapFillWithRedundancy=0 ms
HiWaterPlayoutDelay=67 ms
LoWaterPlayoutDelay=67 ms
ReceiveDelay=67 ms
LostPackets=0 ms
EarlyPackets=0 ms
LatePackets=0 ms
VAD = enabled
CoderTypeRate=g729r8
CodecBytes=20
cvVoIPCallHistoryIcpif=0
SignalingType=cas
Modem passthrough signaling method is nse
Buffer Fill Events = 0
Buffer Drain Events = 0
Percent Packet Loss = 0
Consecutive-packets-lost Events = 0
Corrected packet-loss Events = 0
Last Buffer Drain/Fill Event = 373sec
Time between Buffer Drain/Fills = Min 0sec Max 0sec
GENERIC:
SetupTime=104443 ms
Index=2
PeerAddress=50110
PeerSubAddress=
PeerId=100
PeerIfIndex=104
LogicalIfIndex=10
DisconnectCause=10
DisconnectText=normal call clearing.
ConnectTime=104964
DisconectTime=143330
CallDuration=00:06:23
CallOrigin=2
ChargedUnits=0
InfoType=speech
TransmitPackets=37717
TransmitBytes=5706436
ReceivePackets=37668
ReceiveBytes=6609552
TELE:
ConnectionId=[0x4B091A27 0x3EDD0003 0x0 0xFEFD4]
CallID=3
Port=3/0/0 (3)
BearerChannel=3/0/0.1
TxDuration=375300 ms
VoiceTxDuration=375300 ms
FaxTxDuration=0 ms
CoderTypeRate=g711ulaw
NoiseLevel=-75
ACOMLevel=11
SessionTarget=
ImgPages=0
```

The following example from a Cisco AS5350 router displays a sample of voice call history records showing release source information:

```
Router# show call history voice Telephony call-legs: 1
SIP call-legs: 0
H323 call-legs: 1
Total call-legs: 2
GENERIC:
SetupTime=85975291 ms
.
.
.
DisconnectCause=10  
DisconnectText=normal call clearing (16)
ConnectTime=85975335
DisconnectTime=85979339
CallDuration=00:00:40
CallOrigin=1
ReleaseSource=1
.
.
.
DisconnectCause=10  
DisconnectText=normal call clearing (16)
ConnectTime=85975335
DisconnectTime=85979339
CallDuration=00:00:40
CallOrigin=1
ReleaseSource=1
.
.
.
VOIP:
ConnectionId[0x2868AD84 0x375B11D4 0x8012F7A5 0x74DE971E]
CallID=1
.
.
.
GENERIC:
SetupTime=85975290 ms
.
.
.
DisconnectCause=10  
DisconnectText=normal call clearing (16)
ConnectTime=85975336
DisconnectTime=85979340
CallDuration=00:00:40
CallOrigin=2
ReleaseSource=1
.
.
.
TELE:
ConnectionId=[0x2868AD84 0x375B11D4 0x8012F7A5 0x74DE971E]
CallID=2
Port=3/0/0 (2)
BearerChannel=3/0/0.1
```

The following is sample output from the show call history voice brief command:

```
Router# show call history voice brief <ID>: <CallID> <start>hs.<index> +<connect> +<disc> pid:<peer_id> <direction> <addr> 
dur hh:mm:ss tx:<packets>/<bytes> rx:<packets>/<bytes> <disc-cause>(<text>)
IP <ip>:<udp> rtt:<time>ms pl:<play>/<gap>ms lost:<lost>/<early>/<late>
delay:<last>/<min>/<max>ms <codec>
media inactive detected:<y/n> media cntrl rcvd:<y/n> timestamp:<time>
MODEMPASS <method> buf:<fills>/<drains> loss <overall%> <multipkt>/<corrected>
last <buf event time>s dur:<Min>/<Max>s
FR <protocol> [int dlci cid] vad:<y/n> dtmf:<y/n> seq:<y/n>
<codec> (payload size)
ATM <protocol> [int vpi/vci cid] vad:<y/n> dtmf:<y/n> seq:<y/n>
<codec> (payload size)
Telephony <int> (callID) [channel_id] tx:<tot>/<voice>/<fax>ms <codec> noise:<lvl>dBm acom:<lvl>dBm
MODEMRELAY info:<rcvd>/<sent>/<resent> xid:<rcvd>/<sent> total:<rcvd>/<sent>/<drops> disc:<cause code>
speeds(bps): local <rx>/<tx> remote <rx>/<tx>
Proxy <ip>:<audio udp>,<video udp>,<tcp0>,<tcp1>,<tcp2>,<tcp3> endpt: <type>/<manf>
bw: <req>/<act> codec: <audio>/<video>
tx: <audio pkts>/<audio bytes>,<video pkts>/<video bytes>,<t120 pkts>/<t120 bytes>
rx: <audio pkts>/<audio bytes>,<video pkts>/<video bytes>,<t120 pkts>/<t120 bytes>
```

The following is sample output from the show call history voice redirect command:

```
Router# show call history voice redirect tbct index=2, xfr=tbct-notify, status=redirect_success, start_time=*00:12:25.981 UTC Mon Mar 1 1993, ctrl name=T1-2/0,  tag=13
index=3, xfr=tbct-notify, status=redirect_success, start_time=*00:12:25.981 UTC Mon Mar 1 1993, ctrl name=T1-2/0,  tag=13
index=4, xfr=tbct-notify, status=redirect_success, start_time=*00:13:07.091 UTC Mon Mar 1 1993, ctrl name=T1-2/0,  tag=12
index=5, xfr=tbct-notify, status=redirect_success, start_time=*00:13:07.091 UTC Mon Mar 1 1993, ctrl name=T1-2/0,  tag=12
Number of call-legs redirected using tbct with notify:4
```

The table below describes the significant fields shown in the show call history voice redirect tbct display.

Field

Description

index

Index number of the record in the history file.

xfr

Whether TBCT or TBCT with notify has been invoked.

status

Status of the redirect request.

start_time

Time, in hours, minutes, and seconds when the redirected call began.

ctrl name

Name of the T1 controller where the call originated.

tag

Call tag number that identifies the call.

Number of call-legs redirected using tbct with notify

Total number of call legs that were redirected using TBCT with notify.

### Related Commands

Command

Description

dial-control-mib

Set the maximum number of calls contained in the table.

show call active fax

Displays call information for fax transmissions that are in progress.

show call active voice

Displays call information for voice calls that are in progress.

show call history fax

Displays the call history table for fax transmissions.

show dial-peer voice

Displays configuration information for dial peers.

show num-exp

Displays how the number expansions are configured in VoIP.

show voice port

Displays configuration information about a specific voice port.

## show call history watermark connected table

To display the last n high watermark that is achieved by number of connected call rates per second in various periods, use the show call history watermark connected table command. The periods are seconds, minutes, and hours since the last reload. The size of the table is variable and is configurable.

show call history watermark connected table [ [ brief ] [ id identifier ] | compact [ duration { less | more } seconds ] | last number ]

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

Cisco IOS Release

Modification

15.3(1)T

This command was introduced.

## Examples

The following is a sample output in the show call history watermark connected table command:

The output displays a tabular format of call rate per second for the last 1 minute, 1 hour, and all time.

```
Device# show call history watermark connected table Device   01:48:05 AM Thursday Mar 14 2019 UTC
===============================================
Connected Calls
------- The WaterMark Table for Second --------
Value : 0, ts : [Thu, 14 Mar 2019 01:48:01 GMT]
Value : 0, ts : [Thu, 14 Mar 2019 01:48:02 GMT]
Value : 0, ts : [Thu, 14 Mar 2019 01:48:03 GMT]
Value : 0, ts : [Thu, 14 Mar 2019 01:48:04 GMT]
Value : 0, ts : [Thu, 14 Mar 2019 01:48:05 GMT]
------- The WaterMark Table for Minute-------
Value : 0, ts : [Wed, 13 Mar 2019 05:33:06 GMT]
Value : 0, ts : [Wed, 13 Mar 2019 05:33:06 GMT]
Value : 0, ts : [Wed, 13 Mar 2019 05:33:06 GMT]
Value : 0, ts : [Wed, 13 Mar 2019 05:33:06 GMT]
Value : 0, ts : [Wed, 13 Mar 2019 05:33:06 GMT]
------- The WaterMark Table for Hour --------
Value : 0, ts : [Wed, 13 Mar 2019 05:16:05 GMT]
Value : 0, ts : [Wed, 13 Mar 2019 05:16:05 GMT]
Value : 0, ts : [Wed, 13 Mar 2019 05:16:05 GMT]
Value : 1, ts : [Wed, 13 Mar 2019 00:12:05 GMT]
Value : 1, ts : [Wed, 13 Mar 2019 05:16:05 GMT]
------- The WaterMark Table for Alltime------
Value : 1, ts : [Sun, 10 Mar 2019 01:39:05 GMT]
Value : 1, ts : [Sun, 10 Mar 2019 23:06:05 GMT]
Value : 1, ts : [Wed, 13 Mar 2019 00:12:05 GMT]
Value : 1, ts : [Wed, 13 Mar 2019 05:16:05 GMT]
Value : 2, ts : [Sun, 10 Mar 2019 23:57:05 GMT]
Device#
```

### Usage Guidelines

This command displays the last n high watermark that is achieved by number of connected call rates per second in various
                              periods. The periods are seconds, minutes, and hours since the last reload.

### Related Commands

Command

Description

show call history stats connected

Display connected or active call histogram for 3 periods (Seconds, Minutes, and Hours).

show call history stats connected table

Displays concurrent call table for max and average value of active calls per second.

## show call language voice

To display a summary of languages configured and the URLs of the corresponding Tool Command Language (TCL) modules for the
                              languages that are not built-in languages, use the show call language voice command in EXEC mode.

show call language voice [ language | summary ]

### Syntax Description

language

(Optional) Two-character prefix configured with the call language voice command in global configuration mode, either for a prefix for a built-in language or one that you have defined; for example,
                                          "en" for English or "ru" for Russian.

summary

(Optional) Summary of all the languages configured and the URLs for the TCL modules other than built-in languages.

### Command Modes

EXEC (#)

## Command History

Release

Modification

12.2(2)T

This command was introduced.

### Usage Guidelines

This command is similar to the show call application voice command. If a language is built in, the URL listed reads "fixed." If you decide to overwrite the built-in language with your
                              own language, the word "fixed" in the URL column changes to the actual URL where your new application lives.

## Examples

The following command displays a summary of the configured languages:

```
Router# show call language voice summary
name       url
sp         fixed
ch         fixed
en         fixed
ru         tftp://dirt/fwarlau/scripts/multilag/ru_translate.tcl
```

The following command displays information about Russian-language configuration:

```
Router# show call language voice ru
ru_translate.tcl
ru_translate.tcl~
singapore.cfg
test.tcl
people% more ru_translate.tcl
# Script Locked by: farmerj
# Script Version: 1.1.0.0
# Script Lock Date: Sept 24 2000
# ca_translate.tcl
#------------------------------------------------------------------
# Sept 24, 2000 Farmer Joe
#
# Copyright (c) 2000 by Cisco Systems, Inc.
# All rights reserved.
#------------------------------------------------------------------
#<snip>...
...set prefix ""
#puts "argc"
#foreach arg $argv {
#puts "$arg"
#    translates $arg
#    puts "\t\t**** $prompt RETURNED"
#}
```

Field descriptions should be self-explanatory.

### Related Commands

Command

Description

call language voice

Configures a TCL module.

call language voice load

Loads or reloads a TCL module from the configured URL location.

debug voip ivr

Specifies the type of VoIP IVR debug output that you want to view.

show call application voice

Shows and describes applications.

## show call leg

To display event logs and statistics for voice call legs, use the show call leg command in privileged EXEC mode.

show call leg { active | history } [ summary |  [ last number | leg-id leg-id ] [ event-log | info ]]

### Syntax Description

active

Statistics or event logs for active call legs.

history

Statistics or event logs for terminated call legs.

summary

(Optional) A summary of each call leg.

last number

(Optional) Selected number of most recent call legs. Not available with active keyword.

leg-id leg-id

(Optional) A specific call leg. Output displays event logs or statistics for that call leg.

event-log

(Optional) Event logs for call legs.

info

(Optional) Statistics for call legs.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

### Usage Guidelines

If you use the leg-id keyword, only statistics or event logs for that call leg display. To display event logs with this command, you must enable
                              event logging with the call leg event-log command.

## Examples

The following is sample output from the show call leg command using different keywords:

```
Router# show call leg active summary G<id>  L<id>     Elog A/O FAX T<sec> Codec       type  Peer Address       IP R<ip>:<udp>
G11DC  L A        Y   ANS     T2     None        TELE  P4085550198
Total call-legs: 1
Router# show call leg active event-log Event log for call leg ID: A        Connection ID: 11DC 
buf_size=4K, log_lvl=INFO
<ctx_id>:<timestamp>:<seq_no>:<severity>:<msg_body>
A:1057277701:71:INFO: Call setup indication received, called = 4085550198,  calling = 52927, echo canceller = enable, direct inward dialing
A:1057277701:72:INFO: Dialpeer = 1
A:1057277701:77:INFO: Digit collection
A:1057277701:78:INFO: Call connected using codec None
Total call-legs: 1
Router# show call leg active info Information for call leg ID: A        Connection ID: 11DC 
 GENERIC:
SetupTime=3012940 ms
Index=1
PeerAddress=4085550198
PeerSubAddress=
PeerId=1
PeerIfIndex=329
LogicalIfIndex=253
ConnectTime=301295
CallDuration=00:00:20
CallState=4
CallOrigin=2
ChargedUnits=0
InfoType=2
TransmitPackets=412
TransmitBytes=98880
ReceivePackets=0
ReceiveBytes=0
TELE:
ConnectionId=[0x632D2CAB 0xACEB11D7 0x80050030 0x96F8006E]
IncomingConnectionId=[0x632D2CAB 0xACEB11D7 0x80050030 0x96F8006E]
TxDuration=20685 ms
VoiceTxDuration=0 ms
FaxTxDuration=0 ms
CoderTypeRate=None
NoiseLevel=-120
ACOMLevel=90
OutSignalLevel=-50
InSignalLevel=-41
InfoActivity=0
ERLLevel=38
EchoCancellerMaxReflector=16685
SessionTarget=
ImgPages=0
CallerName=
CallerIDBlocked=False
OriginalCallingNumber=4085550198
OriginalCallingOctet=0x0
OriginalCalledNumber=52927
OriginalCalledOctet=0xE9
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0xFF
TranslatedCallingNumber=4085550198
TranslatedCallingOctet=0x0
TranslatedCalledNumber=52927
TranslatedCalledOctet=0xE9
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0xFF
GwReceivedCalledNumber=52927
GwReceivedCalledOctet3=0xE9
GwReceivedCallingNumber=4085550198
GwReceivedCallingOctet3=0x0
GwReceivedCallingOctet3a=0x81
Total call-legs: 1
```

For a description of the call leg statistics, see the description for the show call active voice command.

```
Router# show call leg active leg-id A Call Information - Connection ID: 11DC , Call Leg ID: A
 GENERIC:
SetupTime=3012940 ms
Index=1
PeerAddress=4085550198
PeerSubAddress=
PeerId=1
PeerIfIndex=329
LogicalIfIndex=253
ConnectTime=301295
CallDuration=00:00:40
CallState=4
CallOrigin=2
ChargedUnits=0
InfoType=2
TransmitPackets=824
TransmitBytes=197760
ReceivePackets=0
ReceiveBytes=0
TELE:
ConnectionId=[0x632D2CAB 0xACEB11D7 0x80050030 0x96F8006E]
IncomingConnectionId=[0x632D2CAB 0xACEB11D7 0x80050030 0x96F8006E]
TxDuration=20685 ms
VoiceTxDuration=0 ms
FaxTxDuration=0 ms
CoderTypeRate=None
NoiseLevel=-120
ACOMLevel=90
OutSignalLevel=-50
InSignalLevel=-41
InfoActivity=0
ERLLevel=38
EchoCancellerMaxReflector=16685
SessionTarget=
ImgPages=0
CallerName=
CallerIDBlocked=False
OriginalCallingNumber=4085550198
OriginalCallingOctet=0x0
OriginalCalledNumber=52927
OriginalCalledOctet=0xE9
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0xFF
TranslatedCallingNumber=4085550198
TranslatedCallingOctet=0x0
TranslatedCalledNumber=52927
TranslatedCalledOctet=0xE9
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0xFF
GwReceivedCalledNumber=52927
GwReceivedCalledOctet3=0xE9
GwReceivedCallingNumber=4085550198
GwReceivedCallingOctet3=0x0
GwReceivedCallingOctet3a=0x81
Call Event Log - Connection ID: 11DC , Call Leg ID: A       
buf_size=4K, log_lvl=INFO
<ctx_id>:<timestamp>:<seq_no>:<severity>:<msg_body>
A:1057277701:71:INFO: Call setup indication received, called = 4085550198,  calling = 52927, echo canceller = enable, direct inward dialing
A:1057277701:72:INFO: Dialpeer = 1
A:1057277701:77:INFO: Digit collection
A:1057277701:78:INFO: Call connected using codec None
Call-leg found: 1
Router# show call leg active leg-id A event-log Call Event Log - Connection ID: 11DC , Call Leg ID: A       
buf_size=4K, log_lvl=INFO
<ctx_id>:<timestamp>:<seq_no>:<severity>:<msg_body>
A:1057277701:71:INFO: Call setup indication received, called = 4085550198,  calling = 52927, echo canceller = enable, direct inward dialing
A:1057277701:72:INFO: Dialpeer = 1
A:1057277701:77:INFO: Digit collection
A:1057277701:78:INFO: Call connected using codec None
Call-leg found: 1
Router# show call leg history summary G<id>  L<id>     Elog A/O FAX T<sec> Codec       type  Peer Address       IP R<ip>:<udp> disc-cause
G11DB  L 7        Y   ANS     T24    None        TELE  P4085550198 D10  
G11DC  L A        Y   ANS     T159   None        TELE  P4085550198 D10  
Total call-legs: 2
Router# show call leg history last 1 Call Information - Connection ID: 11DC , Call Leg ID: A
GENERIC:
SetupTime=3012940 ms
Index=4
PeerAddress=4085550198
PeerSubAddress=
PeerId=1
PeerIfIndex=329
LogicalIfIndex=253
DisconnectCause=10  
DisconnectText=normal call clearing (16)
ConnectTime=301295
DisconnectTime=317235
CallDuration=00:02:39
CallOrigin=2
ReleaseSource=1
ChargedUnits=0
InfoType=speech
TransmitPackets=2940
TransmitBytes=705600
ReceivePackets=0
ReceiveBytes=0
TELE:
ConnectionId=[0x632D2CAB 0xACEB11D7 0x80050030 0x96F8006E]
IncomingConnectionId=[0x632D2CAB 0xACEB11D7 0x80050030 0x96F8006E]
TxDuration=20685 ms
VoiceTxDuration=0 ms
FaxTxDuration=0 ms
CoderTypeRate=None
NoiseLevel=-120
ACOMLevel=90
SessionTarget=
ImgPages=0
CallerName=
CallerIDBlocked=False
OriginalCallingNumber=4085550198
OriginalCallingOctet=0x0
OriginalCalledNumber=52927
OriginalCalledOctet=0xE9
OriginalRedirectCalledNumber=
OriginalRedirectCalledOctet=0xFF
TranslatedCallingNumber=4085550198
TranslatedCallingOctet=0x0
TranslatedCalledNumber=52927
TranslatedCalledOctet=0xE9
TranslatedRedirectCalledNumber=
TranslatedRedirectCalledOctet=0xFF
GwReceivedCalledNumber=52927
GwReceivedCalledOctet3=0xE9
GwReceivedCallingNumber=4085550198
GwReceivedCallingOctet3=0x0
GwReceivedCallingOctet3a=0x81
Call Event Log - Connection ID: 11DC , Call Leg ID: A       
buf_size=4K, log_lvl=INFO
<ctx_id>:<timestamp>:<seq_no>:<severity>:<msg_body>
A:1057277701:71:INFO: Call setup indication received, called = 4085550198,  calling = 52927, echo canceller = enable, direct inward dialing
A:1057277701:72:INFO: Dialpeer = 1
A:1057277701:77:INFO: Digit collection
A:1057277701:78:INFO: Call connected using codec None
A:1057277860:150:INFO: Inform application call disconnected (cause = normal call clearing (16))
A:1057277860:154:INFO: Call disconnected (cause = normal call clearing (16))
A:1057277860:155:INFO: Call released
Total call-legs: 1
Total call-legs with event log: 1
Router# show call leg history leg-id A event-log Call Event Log - Connection ID: 11DC , Call Leg ID: A       
buf_size=4K, log_lvl=INFO
<ctx_id>:<timestamp>:<seq_no>:<severity>:<msg_body>
A:1057277701:71:INFO: Call setup indication received, called = 4085550198,  calling = 52927, echo canceller = enable, direct inward dialing
A:1057277701:72:INFO: Dialpeer = 1
A:1057277701:77:INFO: Digit collection
A:1057277701:78:INFO: Call connected using codec None
A:1057277860:150:INFO: Inform application call disconnected (cause = normal call clearing (16))
A:1057277860:154:INFO: Call disconnected (cause = normal call clearing (16))
A:1057277860:155:INFO: Call released
Call-leg matched ID found: 1
Call-legs matched ID with event log: 1
```

Field descriptions should be self-explanatory.

### Related Commands

Command

Description

call leg event-log

Enables event logging for voice, fax, and modem call legs.

call leg event-log dump ftp

Enables the voice gateway to write the contents of the call-leg event log buffer to an external file.

call leg event-log error-only

Restricts event logging to error events only for voice call legs.

call leg event-log max-buffer-size

Sets the maximum size of the event log buffer for each call leg.

call leg history event-log save-exception-only

Saves to history only event logs for call legs that had at least one error.

monitor call leg event-log

Displays the event log for an active call leg in real-time.

## show call media forking

To display currently active media forking sessions, use the show call
                                    						media forking command in user EXEC or privileged EXEC mode.

show call media forking

### Syntax Description

This command has no arguments or keywords.

### Command Modes

User EXEC (>) Privileged EXEC (#)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

Use this command to verify that media forking was successful for relevant anchor
                              				legs.

## Examples

The following example is a sample output from the s how call media
                                    						forking command..

```
Router# show call media forking Warning: Output may be truncated if sessions are added/removed concurrently!
Session Call n/f Destination (port address)
7 6 far 1234 1.5.35.254
8 6 near 5678 1.5.35.254
```

The table below describes the fields that are displayed in the output.

Field

Description

Session

Session Identifier.

Call

Call Leg identifier in hexadecimal. It must
                                          									match the Call ID from the show call leg active command.

n/f

Direction (Near End or Far End) of the voice
                                          									stream that was forked.

Destination (port address)

Destination for the forked packets. It consists of the
                                          									folllowing:

RTP Port

IP Address

## show callmon

To display call monitor information, use the show callmon command in user EXEC or privileged EXEC mode.

show callmon { call | gcid | subscription | trace { all | event { all | call | connection } | exec | server | subscription | trigger }}

### Syntax Description

call

Displays the active call monitor calls.

gcid

Displays the active global call ID information.

subscription

Displays the subscription information.

trace

Displays the trace information.

all

Displays all types of traces based on time.

event

Displays the event trace information.

all --Displays all event traces.

call --Displays event traces related to a call.

connection --Displays the event traces related to a connection.

exec

Displays all critical execution traces.

server

Displays all session server up or down traces.

subscription

Displays all subscription traces.

trigger

Displays the entire trigger structure by index.

### Command Modes

User EXEC (>) Privileged EXEC (#))

## Command History

Release

Modification

12.4(22)T

This command was introduced.

## Examples

The following sample output from the show callmon call command shows active call monitor calls:

```
Router# show callmon call line dn     sub_id   number of call instance
6401,     1
      callID 2038(19D7),  *cg = 6401, cd = 6601
6601,     1
      callID 2039(19D7),  cg = 6401, *cd = 6601
```

The table below describes the significant fields shown in the display.

Field

Description

dn

Directory number.

number of call

Number of call instances.

instance

Contents of the call instance.

The following sample output from the show callmon gcid command shows the active global call ID information:

```
Router# show callmon gcid GCID                              callIDs(active_entry_id)
AE48ECBC-D89311DB-87FC996E-115FF692
 isConfGcid:FALSE        gcid_conf:00000000-00000000-00000000-00000000
, 2038(19D7), 2039(19D7)
```

The table below describes the significant fields shown in the display.

Field

Description

GCID

Global call ID.

CallIDs

Active call IDs.

### Related Commands

Command

Description

callmonitor

Enables call monitoring messaging functionality on a SIP endpoint in a VoIP network.

## show call prompt-mem-usage

To display the amount of memory used by prompts, use the show call prompt-mem-usage command in privileged EXEC mode.

show call prompt-mem-usage [ detail ]

### Syntax Description

detail

(Optional) Displays details about memory usage and names of tones used.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(15)T

This command was introduced.

12.3(7)T

The detail keyword was added.

### Usage Guidelines

Use this command to display the number of prompts loaded into the gateway, the amount of memory used by the prompts, the
                              number of prompts currently being played, and the status of prompt loads.

For calls transferred by a Cisco CallManager Express (Cisco CME) system, the ringback tone generation for commit-at-alerting
                              uses an interactive voice response (IVR) prompt playback mechanism. Ringback tone is played to the transferred party by the
                              Cisco CME system associated with the transferring party.

The system automatically generates tone prompts as needed on the basis of the network-locale setting made in the Cisco CME
                              system.

## Examples

The following sample output shows details about the memory usage of the prompts that are used.

```
Router# show call prompt-mem-usage Prompt memory usage:
             config’d      wait    active      free     mc total    ms total
    file(s)      0200      0010      0001     00189        00011      00002
    memory   02097152  00081259  00055536  01960357     00136795
 Prompt load counts: (counters reset 0)
    success 11(1st try) 0(2nd try), failure 0
 Other mem block usage:
            mcDynamic   mcReader
    gauge       00001      00001
Number of prompts playing: 1 
Number of start delays   : 0
MCs in the ivr MC sharing table
===============================
Media Content: NoPrompt (0x83C64554)
  URL: 
  cid=0, status=MC_READY size=24184 coding=g711ulaw refCount=0
Media Content: tone://GB_g729_tone_ringback (0x83266EC8)
  URL: tone://GB_g729_tone_ringback
```

The table below describes the significant fields shown in the display.

Field

Description

file(s)

Number of prompts in different queues.

file(s) - config’d

Maximum number of configured prompts that can be simultaneously available in memory. In the sample output, the value of 200
                                          in this field means that loading the 201st prompt results in the oldest prompts being removed.

file(s) -wait

Number of prompts in the wait queue that are not being used in any call and are ready to be deleted when there is no space
                                          for a new prompt. This field lists older prompts that can be deleted.

file(s) - active

Number of prompts that are being used in active calls. These prompts cannot be deleted.

file(s) - free

Number of prompts that can be loaded without deleting any prompt from the wait queue. This is the number of configured prompts
                                          (listed under config’d) minus the total number of prompts in the wait and active states.

file(s) - mc total

Total number of prompts in the wait and active states.

ms total

Number of media streams that are currently active. One media stream is used for playing INBOX prompts. A prompt is considered
                                          an INBOX prompt if its URL is either flash:, http:, ram:, or tftp:.

memory

Displays the memory used by prompts, in bytes.

memory - config’d

Maximum amount of memory configured to be available for prompts.

memory - wait

Total amount of memory used by prompts in the wait list.

memory - active

Total amount of memory used by prompts in the active list.

memory - free

Amount of available memory. This is the amount of configured prompts (listed under config’d) memory minus the total amount
                                          of memory used by the prompts in the wait and active lists.

memory - mc total

Total amount of memory used by prompts in the wait and active lists.

Prompt load counts

Number of successful attempts to load a prompt on the first try and on the second try, and the number of attempts to load
                                          a prompt that failed.

mcDynamic

Number of dynamic element queues that are active. A dynamic element queue is a list of prompts that are played together.

mcReader

Number of mcReaders that are active. An mcReader is used for playing one mcDynamic queue of prompts. An mcReader is used
                                          only if the mcDynamic contains prompts that are associated with one of the following types of URL: flash:, http:, ram:, or
                                          tftp:.

Number of prompts playing

Number of prompts that are currently playing.

Number of start delays

Number of times that prompts failed to start and have subsequently restarted.

MCs in the ivr MC sharing table

The fields below this line of text refer to each media content (prompt) currently cached in memory. In the sample output,
                                          the only cached prompt is the built-in default prompt named "NoPrompt."

Media Content

Name of the prompt, which is derived from the audio file URL (the characters after the last "/" in the URL). The address
                                          in parentheses is the memory location of the prompt.

URL

Location of the file for the prompt that is playing. In the case of the default prompt, NoPrompt, no URL is given.

cid

Call identification number of the call that initiated the loading of the prompt.

status

Status of the media content. The following values are possible:

MC_NOT_READY--Initial status for media content. When the media content is successfully loaded, the status will change to
                                                MC_READY.

MC_READY--Media content is loaded into memory and ready for use.

MC_LOAD_FAIL--Media content failed to load.

size

Size of the media content, in bytes.

coding

Type of encoding used by the media content.

refCount=0

Number of calls to which this media content is currently being streamed.

## show call resource voice stats

To display resource statistics for an H.323 gateway, use the show call resource voice stats command in privileged EXEC mode.

show call resource voice stats [ ds0 | dsp ]

### Syntax Description

ds0

(Optional) Specifies the voice digital signal level zero (DS0) resource statistics information.

dsp

(Optional) Specifies the voice digital signal processor (DSP) resource statistics information.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(5)T

This command was introduced.

12.1(5)XM2

This command was integrated into Cisco IOS Release 12.1(5)XM2

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(2)XB1

This command was integrated into Cisco IOS Release into 12.2(2)XB1.

12.2(8)T

This command was modified. Support for the Cisco AS5300,Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 series
                                          routers is not included in this release.

12.4(22)T

This command was modified. The ds0 and dsp keywords were added.

### Usage Guidelines

The show call resource voice stats command displays the H.323 resources that are monitored when the resource threshold command is used to configure resource threshold reporting.

## Examples

The following is sample output from the show call resource voice stats command, which shows the resource statistics for an
                              H.323 gateway:

```
Router# show call resource voice stats Resource Monitor -  Dial-up Resource Statistics Information:
DSP Statistics:
Utilization: 0 percent
Total channels: 48
Inuse channels: 0
Disabled channels 0:
Pending channels: 0
Free channels: 48
DS0 Statistics:
Total channels: 0
Addressable channels: 0
Inuse channels: 0
Disabled channels: 0
Free channels: 0
```

The table below describes significant fields shown in this output.

Statistic

Definition

Total channels

Number of channels physically configured for the resource.

Inuse channels

Number of addressable channels that are in use. This value includes all channels that either have active calls or have been
                                          reserved for testing.

Disabled channels

Number of addressable channels that are physically down or that have been disabled administratively with the shutdown or busyout command.

Pending channels

Number of addressable channels that are pending in loadware download.

Free channels

Number of addressable channels that are free.

Addressable channels

Number of channels that can be used for a specific type of dialup service, such as H.323, which includes all the DS0 resources
                                          that have been associated with a voice plain old telephone service (POTS) dial plan profile.

### Related Commands

Command

Description

resource threshold

Configures a gateway to report H.323 resource availability to the gatekeeper of the gateway.

show call resource voice threshold

Displays the threshold configuration settings and status for an H.323 gateway.

## show call resource voice threshold

To display the threshold configuration settings and status for an H.323 gateway, use the show call resource voice threshold command in privileged EXEC mode.

show call resource voice threshold [ ds0 | dsp ]

### Syntax Description

ds0

(Optional) Specifies the voice digital signal level zero (DS0) resource statistics information.

dsp

(Optional) Specifies the voice digital signal processor (DSP) resource statistics information.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(5)T

This command was introduced.

12.1(5)XM2

This command was integrated into Cisco IOS Release 12.1(5)XM2

12.2(2)XB1

This command was integrated into Cisco IOS Release into 12.2(2)XB1.

12.4(22)T

This command was modified. The ds0 and dsp keywords were added.

### Usage Guidelines

The show call resource voice threshold command displays the H.323 resource thresholds that are configured with the resource threshold command.

## Examples

The following is sample output from the show call resource voice threshold command, which shows the resource threshold settings
                              and status for an H.323 gateway:

```
Router# show call resource voice threshold Resource Monitor -  Dial-up Resource Threshold Information:
DS0 Threshold:
Client Type: h323
High Water Mark: 70
Low Water Mark: 60
Threshold State: init
DSP Threshold:
Client Type: h323
High Water Mark: 70
Low Water Mark: 60
Threshold State: low_threshold_hit
```

The table below describes the significant fields shown in the display.

Field

Description

High Water Mark

Resource-utilization level that triggers a message indicating that H.323 resource use is high. The range is 1 to 100. A value
                                          of 100 indicates that the resource is unavailable.The default is 90.

Low Water Mark

Resource-utilization level that triggers a message indicating that H.323 resource use has dropped below the high-usage level.
                                          The range is 1 to 100. The default is 90.

### Related Commands

Command

Description

resource threshold

Configures a gateway to report H.323 resource availability to the gatekeeper of the gateway.

show call resource voice stats

Displays resource statistics for an H.323 gateway.

## show call rsvp-sync conf

To display the configuration settings for Resource Reservation Protocol (RSVP) synchronization, use the show call rsvp - sync conf command in privileged EXEC mode.

show call rsvp-sync conf

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(3)XI1

This command was introduced on the Cisco 2600 series, Cisco 3600 series, Cisco 7200, Cisco MC3810, Cisco AS5300, and Cisco
                                          AS5800.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

Support for the Cisco AS5300,Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 is not included in this release.

12.2(11)T

This command is supported on the Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 in this release.

## Examples

The following example shows sample output from this command:

```
Router# show call rsvp-sync conf VoIP QoS: RSVP/Voice Signaling Synchronization config:
Overture Synchronization is ON
Reservation Timer is set to 10 seconds
```

The table below describes significant fields shown in this output.

Field

Description

Overture Synchronization is ON

Indicates whether RSVP synchronization is enabled.

Reservation Timer is set to xx seconds

Number of seconds for which the RSVP reservation timer is configured.

### Related Commands

Command

Description

call rsvp - sync

Enables synchronization between RSVP and the H.323 voice signaling protocol.

call rsvp - sync resv - timer

Sets the timer for RSVP reservation setup.

debug call rsvp - sync events

Displays the events that occur during RSVP synchronization.

show call rsvp - sync stats

Displays statistics for calls that attempted RSVP reservation.

## show call rsvp-sync stats

To display statistics for calls that attempted Resource Reservation Protocol (RSVP) reservation, use the show call rsvp - sync stats command in privileged EXEC mode.

show call rsvp-sync stats

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(3)XI1

This command was introduced.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

## Examples

The following example shows sample output from this command:

```
Router# show call rsvp-sync stats VoIP QoS:Statistics Information:
Number of calls for which QoS was initiated   : 18478
Number of calls for which QoS was torn down   : 18478
Number of calls for which Reservation Success was notified : 0
Total Number of PATH Errors encountered : 0
Total Number of RESV Errors encountered : 0
Total Number of Reservation Timeouts encountered : 0
```

The table below describes significant fields shown in this output.

Field

Description

Number of calls for which QoS was initiated

Number of calls for which RSVP setup was attempted.

Number of calls for which QoS was torn down

Number of calls for which an established RSVP reservation was released.

Number of calls for which Reservation Success was notified

Number of calls for which an RSVP reservation was successfully established.

Total Number of PATH Errors encountered

Number of path errors that occurred.

Total Number of RESV Errors encountered

Number of reservation errors that occurred.

Total Number of Reservation Timeouts encountered

Number of calls in which the reservation setup was not complete before the reservation timer expired.

### Related Commands

Command

Description

call rsvp - sync

Enables synchronization between RSVP and the H.323 voice signaling protocol.

call rsvp - sync resv - timer

Sets the timer for RSVP reservation setup.

debug call rsvp - sync events

Displays the events that occur during RSVP synchronization.

show call rsvp - sync conf

Displays the RSVP synchronization configuration.

## show call spike status

To display the configured call spike threshold and statistics for incoming calls, use the show call spike status command in privileged EXEC mode.

show call spike status [ dial-peer tag ]

### Syntax Description

dial-peer

(Optional) Displays configuration information for a dial peer.

tag

(Optional) Specifies the dial peer identifying number. Range is from 1 to 2147483647.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T. This command was not supported on the Cisco AS5300, Cisco AS5350,
                                          and Cisco AS5400 in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)XM

This command was implemented on the Cisco 1750 and Cisco 1751. This command was not supported on any other platforms in this
                                          release.

12.2(8)T

This command was implemented on the Cisco 7200 series. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco
                                          AS5850 was not included in this release.

12.2(11)T

Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 was added in this release.

15.1(3)T

This command was modified. The output fields of the command were modified to include the output at the dial peer level.

## Examples

The following is sample output from this command:

```
Router# show call spike status Call Spiking:Configured
 Call spiking :NOT TRIGGERED
 total call count in sliding window ::20
```

The table below describes the significant fields shown in the display.

Field

Description

Call Spiking

Current enabled state of call spiking.

Call Spiking

Details if the call spiking limit has been triggered.

total call count in sliding window

Number of calls during the spiking interval.

```
Router# show call spike status dial-peer 400 TAG        CONFIG    SPIKED TOTAL REJECTED CALLS    REJECTED CALLS
400        YES       NO        4                       0
```

The table below describes the significant fields shown in the display.

Field

Description

TAG

Dial peer tag.

CONFIG

Displays if the call spike command has been configured.

SPIKED

Details if the call spiking limit has been triggered.

TOTAL REJECTED CALLS

Displays the number of calls rejected due to a call spike in the dial peer.

REJECTED CALLS

Displays the number of calls rejected when the call spike was triggered until the call spike control was released.

### Related Commands

Command

Description

call spike

Configures the limit for the number of incoming calls in a short period of time.

## show call threshold

To display enabled triggers, current values for configured triggers, and the number of application programming interface
                              (API) calls that were made to global and interface resources, use the show call threshold command in privileged EXEC mode.

show call threshold { config | status [ unavailable ] | stats }

### Syntax Description

config

Displays the current threshold configuration.

status

Displays the status of all configured triggers and whether or not the CPU is available.

unavailable

(Optional) Displays the status for all unavailable resources.

stats

Displays statistics for API calls; that is, the resource-based measurement.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T. This command is not supported on the Cisco AS5300, Cisco AS5350,
                                          and Cisco AS5400 platforms in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)XM

This command was implemented on the Cisco 1750 and Cisco 1751. This command is not supported on any other platforms in this
                                          release.

12.2(8)T

This command was implemented on the Cisco 7200 series. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco
                                          AS5850 is not included in this release.

12.2(11)T

This command was implemented on the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850.

15.2(2)T

This command was modified. The output was modified to display the configured bandwidth threshold, bandwidth availability,
                                          and call admission control statistics.

## Examples

The following is sample output from the show call threshold config command:

```
Router# show call threshold config Some resource polling interval:
  CPU_AVG interval: 60
  Memory interval:  5
IF              Type            Value   Low     High    Enable
-----           ----            -----   ----    ----    ------
Serial3/1:23    int-calls       0       107     107     N/A
N/A             cpu-avg         0        70      90     busy&treat
```

The following is sample output from the show call threshold status command:

```
Router# show call threshold status Status  IF              Type            Value   Low     High    Enable
------  ---             ------          ----    ----    ----    -----
Avail   N/A             total-calls     0       5       5000    busyout
Avail   N/A             cpu-avg         0       5       65      busyout
```

The following is sample output from the show call threshold status unavailable command:

```
Router# show call threshold status unavailable Unavailable configured resources at the current time:
IF              Type            Value   Low     High    Enable
----            -----           -----   ----    ----    -----
```

The following is sample output from the show call threshold stats command:

```
Router# show call threshold stats Total resource check: 0
 successful: 0
 failed:   0
```

The table below describes significant fields shown in this output.

Field

Description

CPU_AVG interval

Interval of configured trigger CPU_AVG.

Memory interval

Interval of configured trigger Memory.

IF

Interface type and number.

Type

Type of resource.

Value

Value of a call that is to be matched against low and high thresholds.

Low

Low threshold.

High

High threshold.

Enable

Shows if busyout and the call treatment command are enabled.

### Related Commands

Command

Description

call threshold

Enables a resource and defines associated parameters.

call threshold poll-interval

Enables a polling interval threshold for CPU or memory.

clear call threshold

Clears enabled triggers and their associated parameters.

## show call treatment

To display the call-treatment configuration and statistics for handling the calls on the basis of resource availability,
                              use the show call treatment command in privileged EXEC mode.

show call treatment { config | stats }

### Syntax Description

config

Displays the call treatment configuration.

stats

Displays statistics for handling the calls on the basis of resource availability.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T. This command was not supported on the Cisco AS5300, Cisco AS5350,
                                          and Cisco AS5400 in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(4)XM

This command was implemented on the Cisco 1750 and Cisco 1751. This command was not supported on any other platforms in this
                                          release.

12.2(8)T

This command was implemented on the Cisco 7200 series. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco
                                          AS5850 is not included in this release.

12.2(11)T

This command is supported on the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 in this release.

## Examples

The following is sample output from this command:

```
Router# show call treatment config Call Treatment Config
---------------------
Call treatment is OFF.
Call treatment action is: Reject
Call treatment disconnect cause is: no-resource
Call treatment ISDN reject cause-code is: 41
```

The table below describes significant fields shown in this output.

Field

Description

Call treatment is:

State of call treatment, either ON or OFF.

Call treatment action is:

Action trigger assigned for call treatment.

Call treatment disconnect cause is:

Reason for disconnect.

Call treatment ISDN reject cause-code is:

Reject code number assigned.

The following is sample output from the show call treatment command:

```
Router# show call treatment stats
Call Treatment Statistics
-------------------------
Total Calls by call treatment: 0
Calls accepted by call treatment: 0
Calls rejected by call treatment: 0
Reason          Num. of calls rejected
------          ----------------------
cpu-5sec:       0
cpu-avg:        0
total-mem:      0
io-mem:         0
proc-mem:       0
total-calls:    0
```

The table below describes significant fields shown in this output.

Field

Description

Total Calls by call treatment:

Number of calls received and treated.

Calls accepted by call treatment:

Calls that passed treatment parameters.

Calls rejected by call treatment:

Calls that failed treatment parameters.

cpu-5sec

Number of calls rejected for failing the cpu-5sec parameter.

cpu-avg

Number of calls rejected for failing the cpu-avg parameter.

total-mem

Number of calls rejected for failing the total-mem parameter.

io-mem

Number of calls rejected for failing the io-mem parameter.

proc-mem

Number of calls rejected for failing the proc-mem parameter.

total-calls

Number of calls rejected for failing the total-calls parameter.

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

clear call treatment stats

Clears the call-treatment statistics.

## show call-router routes

To display the routes cached in the current border element (BE), use the show call-router routes in EXEC mode.

show call-router routes [ static | dynamic | all ]

### Syntax Description

static

Descriptors provisioned on the border element.

dynamic

Dynamically learned descriptors.

all

Both static and dynamic descriptors.

### Command Default

All

### Command Modes

EXEC (#)

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

## Examples

The following example is sample output from this command.

```
Router# show call-router routes Static Routes:
==============
  DescriptorID= 6561676C65000000000000000000000A
  lastChanged = 19930301063311
   IP addr         :port       Prefix
   172.18.195.64   :2099       5553122
Dynamic Routes:
===============
  DescriptorID= 506174726F6E6F757300000000000002
  lastChanged = 19930228190012
   IP addr         :port       Prefix
   172.18.195.65   :2099       310
  DescriptorID= 506174726F6E6F757300000000000003
  lastChanged = 19930228190012
   IP addr         :port       Prefix
   172.18.195.65   :2099       555301
  DescriptorID= 506174726F6E6F757300000000000004
  lastChanged = 19930228190012
   IP addr         :port       Prefix
   172.18.195.65   :2099       555302
DescriptorID= 506174726F6E6F757300000000000005
  lastChanged = 19930228190012
   IP addr         :port       Prefix
   172.18.195.65   :2099       818
  DescriptorID= 506174726F6E6F757300000000000001
  lastChanged = 19930228190012
   IP addr         :port       Prefix
   172.18.195.65   :2099       1005
```

Field descriptions should be self-explanatory.

### Related Commands

Command

Description

show call-router active

Displays active call information for a voice call in progress.

show call-router history

Displays the VoIP call-history table.

show call-router status

Displays the Annex G BE status.

show dial-peer voice

Displays configuration information for dial peers.

show num-exp

Displays how the number expansions are configured in VoIP.

show voice port

Displays configuration information about a specific voice port.

## show call-router status

To display the Annex G border element status, use the show call - router status command in user EXEC mode.

show call-router status [ neighbors ]

### Syntax Description

neighbors

(Optional) Displays the neighbor border element status.

### Command Modes

User EXEC (#)

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T and modified to add the neighbors keyword.

## Examples

The following example displays the Annex G border element status. Note that the example shows the status for two neighbors.:

```
Router# show call-router status neighbors ANNEX-G CALL ROUTER STATUS:
  ===========================
    Border Element ID Tag   : Celine
    Domain Name             : Celine-Domain
    Border Element State    : UP
    Border Element Local IP : 172.18.193.31:2099
    Advertise Policy        : STATIC descriptors
    Hopcount Value          : 7
    Descriptor TTL          : 3180
    Access Policy           : Neighbors only
    Current Active Calls    : 0
    Current Calls in Cache  : 0
    Cumulative Active Calls : 0
    Usage Ind Messages Sent : 0
    Usage Ind Cfm Rcvd      : 0
    IRRs Received           : 0
    DRQs Received           : 0
    Usage Ind Send Retrys   : 0
  NEIGHBOR INFORMATION:
  =====================
    Local Neighbor ID : (none)
    Remote Element ID : (unknown)
    Remote Domain ID  : (unknown)
    IP Addr           : 1.2.3.4:2099
    Status            : DOWN
    Caching           : OFF
    Query Interval    : 30 MIN (querying disabled)
    Usage Indications :
      Current Active Calls : 0
      Retry Period         : 600 SEC
      Retry Window         : 3600 MIN
    Service Relationship Status: ACTIVE
      Inbound Service Relationship  : DOWN
        Service ID     : (none)
        TTL            : 1200 SEC
      Outbound Service Relationship : DOWN
        Service ID     : (none)
        TTL            : (none)
        Retry interval : 120 SEC (0 until next attempt)
```

The table below describes significant fields shown in this output.

Field

Description

Border Element ID Tag

Identifier for the border element.

Border Element State

Indicates if the border element is running.

Border Element Local IP

Local IP address of the border element.

Advertise Policy

Type of descriptors that the border element advertises to its neighbors. Default is static . Other values are dynamic and all .

Hopcount Value

Maximum number of border element hops through which an address resolution request can be forwarded. Default is 7.

Descriptor TTL

Time-to-live value, or the amount of time, in seconds, for which a route from a neighbor is considered valid. Range is from
                                          1 to 2147483647. Default is 1800 (30 minutes).

Access Policy

Requires that a neighbor be explicitly configured for requests to be accepted.

Local Neighbor ID

Domain name reported in service relationships.

Service Relationship Status

Service relationship between two border elements is active.

Inbound Service Relationship

Inbound time-to-Live (TTL) value in number of seconds. Range is from 1 to 4294967295.

Outbound Service Relationship

Specifies the amount of time, in seconds, to establish the outbound relationship. Range is from 1 to 65535.

Retry interval

Retry value between delivery attempts, in number of seconds. Range is from 1 to 3600.

### Related Commands

Command

Description

advertise

Controls the type of descriptors that the border element advertises to its neighbors.

call - router

Enables the Annex G border element configuration commands.

hopcount

Specifies the maximum number of border element hops through which an address resolution request can be forwarded.

local

Defines the local domain, including the IP address and port border elements that the border element should use for interacting
                                          with remote border elements.

shutdown

Shuts down the Annex G border element.

ttl

Sets the expiration timer for advertisements.

## show ccm-manager

To display a list
                              		  of Cisco CallManager servers and their current status and availability, use the show ccm - manager command
                              		  in privileged EXEC mode.

show ccm-manager [ backhaul | config-download | fallback-mgcp | hosts | music-on-hold | redundancy | download-tones [ c1 | c2 ]]

### Syntax Description

backhaul

(Optional) Displays information about the backhaul link.

config-download

(Optional) Displays information about the status of Media Gateway Control
                                          						Protocol (MGCP) and Skinny Client Control Protocol (SCCP) configuration
                                          						download.

fallback-mgcp

(Optional) Displays the status of the MGCP gateway fallback feature.

hosts

(Optional) Displays a list of each configured Cisco CallManager server in the
                                          						network, together with its operational status and host IP address.

music-on-hold

(Optional) Displays information about all the multicast music-on-hold (MOH)
                                          						sessions in the gateway at any given point in time.

redundancy

(Optional) Displays failover mode and status information for hosts, including
                                          						the redundant link port, failover interval, keepalive interval, MGCP traffic
                                          						time, switchover time, and switchback mode.

download-tones c1 | c2

(Optional) Displays custom tones downloaded to the gateway. The custom tone
                                          						value of c1 or c2 specifies which tone information to display.

### Command Default

If none of the
                              		  optional keywords is specified, information related to all keywords is
                              		  displayed.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(3)T

This
                                          						command was introduced on the Cisco CallManager Version 3.0 and Cisco VG200.

12.2(2)XA

This
                                          						command was implemented on the Cisco 2600 series and Cisco 3600 series.

12.2(2)XN

This
                                          						command was modified to provide enhanced MGCP voice gateway interoperability to
                                          						Cisco CallManager Version 3.1 for the Cisco 2600 series, Cisco 3600 series, and
                                          						Cisco VG200.

12.2(11)T

This
                                          						command was integrated into Cisco IOS Release 12.2(11) and the Cisco
                                          						CallManager Version 3.2. It was implemented on the Cisco IAD2420 series.

12.2(15)ZJ

The
                                          						download-tones [ c1 | c2 ] keywords were added for the following platforms:
                                          						Cisco 2610XM, Cisco 2611XM, Cisco 2620XM, Cisco 2621XM, Cisco 2650XM, Cisco
                                          						2651XM, Cisco 2691, Cisco 3640A, Cisco 3660, Cisco 3725, and Cisco 3745.

12.3(4)T

The
                                          						keywords were integrated into Cisco IOS Release 12.3(4)T.

12.3(14)T

New
                                          						output was added relating to SCCP autoconfiguration.

12.4(15)XY

The
                                          						display output was modified to include the number of TFTP download failures
                                          						allowed.

### Usage Guidelines

Use the show ccm-manager config-download command to determine the status of
                              		  Cisco Unified Communications Manager servers and the automatic download
                              		  information and statistics.

## Examples

The following
                              		  sample output shows the configured amplitudes, frequencies, and cadences of
                              		  custom tone 1, Hong Kong:

```
Router# show ccm-manager download-tones c1 !
Custom Tone 1 : Hong Kong
Pulse dial:normal, Percent make:35%, DTMF low Amp.= 65424, high Amp.= 65446, Pcm:u-Law
                                      FXS  FXO  E&M  FXS  FXO  E&M
Dual Tone DR NF FOF FOS AOF AOF AOF AOS AOS AOS ONTF OFTF ONTS OFTS ONTT OFTT ONT4 OFT4
(optional) FOF2 FOS2 FOF3 FOS3 FOF4 FOS4 FOT FO4 AOT AO4 RCT1 RCT2 RCT3 RCT4
BUSY 0  2 480 620 -120 -120 -120 -120 -120 -120 500 500 0 0 0 0 0 0
RING_BACK           0  2   440   520 -120 -120 -120 -120 -120 -120   400   200   400  3000 
CONGESTION          0  2   480   620 -200 -200 -200 -240 -240 -240   250   250     0     0 
NUMBER_UNOBTAINABLE 0  2   480   620 -120 -120 -120 -120 -120 -120 65535     0     0     0 
DIAL_TONE           0  2   350   440 -150 -150 -150 -150 -150 -150 65535     0     0     0 
DIAL_TONE2          0  2   350   440 -150 -150 -150 -150 -150 -150 65535     0     0     0 
OUT_OF_SERVICE      0  1   950     0 -150 -150 -150    0    0    0   330   330     0     0 
ADDR_ACK            0  1   600     0 -240 -240 -240    0    0    0   125   125   125 65535 
DISCONNECT          0  1   600     0 -150 -150 -150    0    0    0   330   330   330 65535 
OFF_HOOK_NOTICE     0  2  1400  2040 -240 -240 -240 -240 -240 -240   100   100     0     0 
OFF_HOOK_ALERT      0  2  1400  2040 -240 -240 -240 -240 -240 -240   100   100     0     0 
WAITING             0  0     0     0    0    0    0    0    0    0     0     0     0     0 
CONFIRM             0  0     0     0    0    0    0    0    0    0     0     0     0     0 
CNFWRN_J            0  1   950     0 -170 -170 -190    0    0    0   100   100   100 65535 
CNFWRN_D            0  1   600     0 -170 -170 -190    0    0    0   100   100   100 65535 
STUTT_DIALTONE      0  2   350   440 -150 -150 -150 -150 -150 -150   100   100   100   100   100   100 65535     0
PERM_SIG_TONE       0  1   480     0 -170 -170 -170    0    0    0 65535     0     0     0
WAITING1            0  0     0     0    0    0    0    0    0    0     0     0     0     0 
WAITING2            0  0     0     0    0    0    0    0    0    0     0     0     0     0 
WAITING3            0  0     0     0    0    0    0    0    0    0     0     0     0     0 
WAITING4            0  0     0     0    0    0    0    0    0    0     0     0     0     0 
MSGWAIT_IND         0  0     0     0    0    0    0    0    0    0     0     0     0     0 
OFF_HOOK_WARN       0  0     0     0    0    0    0    0    0    0     0     0     0     0 
Sequence Tone       DR NF F1C1  F2C1   AOF   AOS  C1ONT C1OFT C2ONT C2OFT C3ONT C3OFT C4ONT C4OFT  F1C2  F2C2  F1C3  F2C3  F1C4  F2C4
INTERCEPT           0  0     0     0     0     0      0     0     0     0     0     0 
TONE_ON_HOLD        0  0     0     0     0     0      0     0     0     0     0     0 
NO_CIRCUIT          0  0     0     0     0     0      0     0     0     0     0     0 
Legend:
DR: direction NF: number of frequency FO<F,S,T,4>: frequency of<1st,2nd,3rd,4th>  AO<F,S,T,4>: amplitude of<1st,2nd,3rd,4th>
FOF<1-4>: frequency of 1st, cadence<1-4> FOS<1-4>: frequency of 2nd, cadence<1-4>
RCT<1-4>: repeat count for cadence<l-4>  F(1-4>C<1-4> : frequency<1-4> of cadence<1-4>
C<1-4>ONT: cadence<1-4> on time C<1-4>OFT: cadence<1-4> off time
```

The three tables
                              		  below and give descriptions of significant fields once the tones are
                              		  automatically downloaded to the gateway.

Field

Description

Percent
                                          					 make

Pulse
                                          					 ratio in percentage of make.

DTMF low
                                          					 Amp.

Low
                                          					 frequency level.

high Amp.

High
                                          					 frequency level.

Pcm

Pulse
                                          					 Code Modulation (mu-law or a-law).

Field of
                                          					 Dual Tone

Description

DR

Direction
                                          					 to PSTN (0) or Packet Network (1).

NF

Number of
                                          					 Frequency (from 1 to 4).

FOF

Frequency
                                          					 of First component (in Hz).

FXS AOF

Amplitude
                                          					 of First component (from 1 to 65535 = +3 dBm0) for the foreign exchange station
                                          					 (FXS).

FXO AOF

Amplitude
                                          					 of First component (from 1 to 65535 = +3 dBm0) for the foreign exchange office
                                          					 (FXO).

E&M
                                          					 AOF

Amplitude
                                          					 of First component (from 1 to 65535 = +3 dBm0) for the recEive and transMit
                                          					 (E&M).

FXS AOS

Amplitude
                                          					 of Second component (from 1 to 65535 = +3 dBm0) for the FXS.

FXO AOS

Amplitude
                                          					 of Second component (from 1 to 65535 = +3 dBm0) for the FXO.

E&M
                                          					 AOS

Amplitude
                                          					 of Second component (from 1 to 65535 = +3 dBm0) for the E&M.

ONTF

On time;
                                          					 time the tone is generated (milliseconds) for the first frequency.

OFTF

Off time;
                                          					 silence time (milliseconds) for the first frequency.

ONTS

On time;
                                          					 time the tone is generated (milliseconds) for the second frequency.

OFTS

Off time;
                                          					 silence time (milliseconds) for the second frequency.

ONTT

On time;
                                          					 time the tone is generated (milliseconds) for the third frequency.

OFTT

Off time;
                                          					 silence time (milliseconds) for the third frequency.

ONT4

On time;
                                          					 time the tone is generated (milliseconds) for the fourth frequency.

OFT4

Off time;
                                          					 silence time (milliseconds) for the fourth frequency.

FOF2

Frequency
                                          					 of First component for the second cadence.

FOS2

Frequency
                                          					 of Second component for the second cadence.

FOF3

Frequency
                                          					 of First component for the third cadence.

FOS3

Frequency
                                          					 of Second component for the third cadence.

FOF4

Frequency
                                          					 of First component for the fourth cadence.

FOS4

Frequency
                                          					 of Second component for the fourth cadence.

FOT

Frequency
                                          					 of Third component (in Hertz).

FO4

Frequency
                                          					 of Fourth component (in Hertz).

AOT

Amplitude
                                          					 of Third component (from 1 to 65535 = +3 dBm0).

AO4

Amplitude
                                          					 of Fourth component (from 1 to 65535 = +3 dBm0).

RCT1

Number of
                                          					 repeat for the first cadence.

RCT2

Number of
                                          					 repeat for the second cadence.

RCT3

Number of
                                          					 repeat for the third cadence.

RCT4

Number of
                                          					 repeat for the fourth cadence.

Field of
                                          					 Sequence Tone

Description

DR

Direction
                                          					 to PSTN (0) or Packet Network (1).

NF

Number of
                                          					 Frequency (from 1 to 4).

F1C1

Frequency
                                          					 1 of Cadence 1.

F2C1

Frequency
                                          					 2 of Cadence 1.

AOF

Amplitude
                                          					 of First component (from 1 to 65535).

AOS

Amplitude
                                          					 of Second component (from 1 to 65535).

C1ONT

Cadence 1
                                          					 On Time.

C1OFT

Cadence 1
                                          					 Off Time.

C2ONT

Cadence 2
                                          					 On Time.

C2OFT

Cadence 2
                                          					 Off Time.

C3ONT

Cadence 3
                                          					 On Time.

C3OFT

Cadence 3
                                          					 Off Time.

C4ONT

Cadence 4
                                          					 On Time.

C4OFT

Cadence 4
                                          					 Off Time.

F1C2

Frequency
                                          					 1 of Cadence 2.

F2C2

Frequency
                                          					 2 of Cadence 2.

F1C3

Frequency
                                          					 1 of Cadence 3.

F2C3

Frequency
                                          					 2 of Cadence 3.

F1C4

Frequency
                                          					 1 of Cadence 4.

F2C4

Frequency
                                          					 2 of Cadence 4.

The following is
                              		  sample output from the show ccm - manager command for displaying the status and
                              		  availability of both the primary and the backup Cisco Unified Communications
                              		  Manager server:

```
Router# show ccm-manager MGCP Domain Name: Router2821.cisco.com
Priority        Status                   Host
============================================================
Primary         Registered               10.78.236.222
First Backup    None                     
Second Backup   None                     
Current active Call Manager:    10.78.236.222
Backhaul/Redundant link port:   2428
Failover Interval:              30 seconds
Keepalive Interval:             15 seconds
Last keepalive sent:            21:48:37 UTC Nov 4 2007 (elapsed time: 00:00:15)
Last MGCP traffic time:         21:48:51 UTC Nov 4 2007 (elapsed time: 00:00:02)
Last failover time:             None
Last switchback time:           None
Switchback mode:                Graceful
MGCP Fallback mode:             Not Selected
Last MGCP Fallback start time:  None
Last MGCP Fallback end time:    None
MGCP Download Tones:            Disabled 
TFTP retry count to shut Ports: 3
PRI Backhaul Link info:
    Link Protocol:      TCP
    Remote Port Number: 2428
    Remote IP Address:  172.20.71.38
    Current Link State: OPEN
    Statistics:
        Packets recvd:   1
        Recv failures:   0
        Packets xmitted: 3
        Xmit failures:   0
    PRI Ports being backhauled:
       Slot 1, port 1
MGCP Download Tones:             Enabled
Configuration Auto-Download Information
=======================================
Current version-id: {1645327B-F59A-4417-8E01-7312C61216AE}
Last config-downloaded:00:00:49
Current state: Waiting for commands
Configuration Download statistics:
        Download Attempted             : 6
          Download Successful          : 6
          Download Failed              : 0
        Configuration Attempted        : 1
          Configuration Successful     : 1
          Configuration Failed(Parsing): 0
          Configuration Failed(config) : 0
Last config download command: New Registration
Configuration Error History:
FAX mode: cisco
```

The table below
                              		  describes the significant fields shown in the display.

Field

Description

MGCP
                                          					 Domain Name (system)

System
                                          					 used in the Internet for translating domain names of network nodes into IP
                                          					 addresses.

Priority

Priority
                                          					 of the Cisco CallManager servers present in the network. Possible priorities
                                          					 are primary, first backup, and second backup.

Status

Current
                                          					 usage of the Cisco Unified Communications Manager server. Values are
                                          					 Registered, Idle, Backup Polling, and Undefined.

Host

Host IP
                                          					 address of the Cisco CallManager server.

Current
                                          					 active Call Manager

IP
                                          					 address of the active Cisco Communications Manager server. This field can be
                                          					 the IP address of any one of the following Cisco Communications Manager
                                          					 servers: Primary, First Backup, and Second Backup.

Backhaul/Redundant link port

Port that
                                          					 the Cisco CallManager server is to use.

Failover
                                          					 Interval

Maximum
                                          					 amount of time that can elapse without the gateway receiving messages from the
                                          					 currently active Cisco Call Manager before the gateway switches to the backup
                                          					 Cisco Call Manager.

Keepalive
                                          					 Interval

Interval
                                          					 following which, if the gateway has not received any messages from the
                                          					 currently active Cisco Communications Manager server within the specified
                                          					 amount of time, the gateway sends a keepalive message to the Cisco
                                          					 Communications Manager server to determine if it is operational.

Last
                                          					 keepalive sent

Time in
                                          					 hours (military format), minutes and seconds at which the last keepalive
                                          					 message was sent.

Last MGCP
                                          					 traffic time

Time in
                                          					 hours (military format), minutes and seconds at which the last MGCP traffic
                                          					 message was sent.

Switchback mode

Displays
                                          					 the switchback mode configuration that determines when the primary Cisco
                                          					 CallManager server is used if it becomes available again while a backup Cisco
                                          					 CallManager server is being used.

Values
                                          					 that can appear in this field are Graceful, Immediate, Schedule - time, and Uptime-delay.

MGCP
                                          					 Fallback mode

Displays
                                          					 the MGCP fallback mode configuration. If "Not Selected" displays, then fallback
                                          					 is not configured. If "Enabled/OFF" displays, then fallback is configured but
                                          					 not in effect. If "Enabled/ON" displays, then fallback is configured and in
                                          					 effect.

Last MGCP
                                          					 Fallback start time

Start
                                          					 time stamp in hours (military format), minutes and seconds of the last
                                          					 fallback.

Lasts
                                          					 MGCP Fallback end time

End time
                                          					 stamp in hours (military format), minutes and seconds of the last fallback.

MGCP
                                          					 Download Tones

Displays
                                          					 if the customized tone download is enabled.

TFTP
                                          					 retry count to shut Ports

Number of
                                          					 TFTP download failures allowed before endpoints are shutdown.

The following is
                              		  sample output from the show ccm-manager config-download command showing the status of the
                              		  SCCP download:

```
Router# show ccm-manager config-download Configuration Auto-Download Information
=======================================
Current version-id:{4171F93A-D8FC-49D8-B1C4-CE33FA8095BF}
Last config-downloaded:00:00:47
Current state:Waiting for commands
Configuration Download statistics:
        Download Attempted             :6
          Download Successful          :6
          Download Failed              :0
        Configuration Attempted        :1
          Configuration Successful     :1
          Configuration Failed(Parsing):0
          Configuration Failed(config) :0
Last config download command:New Registration
SCCP auto-configuration status
===============================================================
Registered with Call Manager: No
Local interface: FastEthernet0/0 (000c.8522.6910)
Current version-id: {D3A886A2-9BC9-41F8-9DB2-0E565CF51E5A}
Current config applied at: 04:44:45 EST Jan 9 2003
Gateway downloads succeeded: 1
Gateway download attempts: 1
Last gateway download attempt:  04:44:45 EST Jan 9 2003
Last successful gateway download: 04:44:45 EST Jan 9 2003
Current TFTP server: 10.2.6.101
Gateway resets: 0
Gateway restarts: 0
Managed endpoints: 6
Endpoint downloads succeeded: 6
Endpoint download attempts: 6
Last endpoint download attempt:  04:44:45 EST Jan 9 2003
Last successful endpoint download: 04:44:45 EST Jan 9 2003
Endpoint resets: 0
Endpoint restarts: 0
Configuration Error History:
sccp ccm CCM-PUB7 identifier 1
end
controller T1 2/0no shut
controller T1 2/0no shut
controller T1 2/0no shut
isdn switch-type primary-ni
end
```

The table below
                              		  describes the significant fields shown in the display.

Field

Description

Current
                                          					 state

Current
                                          					 configuration state.

Download
                                          					 Attempted

Number of
                                          					 times the gateway has tried to download the configuration file. The number of
                                          					 successes and failures is displayed.

Configuration Attempted

Number of
                                          					 times the gateway has tried to configure the gateway based on the configuration
                                          					 file. The number of successes and failures is displayed.

Managed
                                          					 endpoints

Number of
                                          					 SSCP-controlled endpoints (analog and BRI phones).

Endpoint
                                          					 downloads succeeded

Number of
                                          					 times the gateway has successfully downloaded the configuration files for
                                          					 SCCP-controlled endpoints.

Endpoint
                                          					 download attempts

Number of
                                          					 times the gateway has tried to download the configuration files for
                                          					 SCCP-controlled endpoints.

Endpoint
                                          					 resets

Number of
                                          					 SCCP gateway resets.

Endpoint
                                          					 restarts

Number of
                                          					 SCCP gateway restarts.

Configuration Error History

Displays
                                          					 SCCP autoconfiguration errors.

The following is
                              		  sample output from the show ccm-manager fallback-mgcp command:

```
Router# show ccm-manager fallback-mgcp Current active Call Manager:   172.20.71.38
MGCP Fallback mode:            Enabled/OFF
Last MGCP Fallback start time: 00:14:35
Last MGCP Fallback end time:   00:17:25
```

The table below
                              		  displays te mode. Modes are as follows:

Field

Description

MGCP
                                          					 Fallback mode

The
                                          					 following are displayed:

Not
                                                						  Selected--Fallback is not configured.

Enabled/OFF--Fallback is configured but not in effect.

Enabled/ON--Fallback is configured and in effect.

Last MGCP
                                          					 Fallback start time

Start
                                          					 time stamp in hh:mm:ss of the last fallback.

Last MGCP
                                          					 Fallback end time

End time
                                          					 stamp in hh:mm:ss of the last fallback.

The following is
                              		  sample output from the show ccm-manager music-on-hold command:

```
Router# show ccm-manager music-on-hold Current active multicast sessions :1
 Multicast       RTP port   Packets       Call   Codec    Incoming
 Address         number     in/out        id              Interface
===================================================================
172.20.71.38     2428        5/5          99      g711
```

The table below
                              		  describes the significant fields shown in the display.

Field

Description

Current
                                          					 active multicast sessions

Number of
                                          					 active calls on hold.

Multicast
                                          					 Address

Valid
                                          					 class D address from which the gateway is getting the RTP streams.

RTP port
                                          					 number

Valid RTP
                                          					 port number on which the gateway receives the RTP packets.

Packets
                                          					 in/out

Number of
                                          					 RTP packets received and sent to the digital signal processor (DSP).

Call id

Call ID
                                          					 of the call that is on hold.

Codec

Codec
                                          					 number.

Incoming
                                          					 Interface

Interface
                                          					 through which the gateway is receiving the RTP stream.

### Related Commands

Command

Description

ccm-manager config

Supplies the local MGCP voice gateway with the IP address or logical name of
                                          						the TFTP server from which to download XML configuration files and enable the
                                          						download of the configuration.

debug ccm-manager

Displays debugging information about the Cisco CallManager.

show ccm-manager

Displays a list of Cisco CallManager servers, their current status, and their
                                          						availability.

show ccm-manager fallback-mgcp

Displays the status of the MGCP gateway fallback feature.

show isdn status

Displays the Cisco IOS gateway ISDN interface status.

show mgcp

Displays the MGCP configuration information.

## show cdapi

To display the Call Distributor Application Programming Interface (CDAPI), use the show cdapi command in privileged EXEC mode.

show cdapi

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(7)T

This command was introduced on the Cisco AS5300.

12.3(4)T

This command was enhanced to display V.120 call types registering with the modem.

### Usage Guidelines

CDAPI is the internal application programming interface (API) that provides an interface between signaling stacks and applications.

## Examples

The following is sample output from the show cdapi command. The output displays the following information:

Signaling stacks that register with CDAPI

Applications that register with CDAPI

Active calls

Call type of each active call

Message buffers in use

```
Router# show cdapi Registered CDAPI Applications/Stacks
====================================
Signaling Stack: ISDN
        Interface: Se6/0:23
Application: TSP CDAPI Application Voice
        Application Type(s) : Voice Data Facility Signaling V110 V120
        Application Level   : Tunnel
        Application Mode    : Enbloc
Application: TSP CDAPI Application COT
        Application Type(s) : Cot
        Application Level   : Tunnel
        Application Mode    : Enbloc
Application: CSM
        Application Type(s) : Modem V110 V120
        Application Level   : Basic
        Application Mode    : Enbloc
Signaling Stack: XCSP
Application: dialer
        Application Type(s) : Data
        Application Level   : Basic
        Application Mode    : Enbloc
Active CDAPI Calls
==================
        Se7/7:23 Call ID = 0x7717, Call Type = V.120, Application = CSM
CDAPI Message Buffers
=====================
Free Msg Buffers: 320
Free Raw Buffers: 320
Free Large-Raw Buffers: 120
```

Field descriptions should be self-explanatory. However, the following information may be of help:

Enbloc is the mode where all call-establishment information is sent in the setup message (opposite of overlap mode, where
                                    additional messages are needed to establish the call).

Cot is the Continuity Test (COT) subsystem that supports the continuity test required by the Signaling System 7 (SS7) network
                                    to conduct loopback and tone check testing on the path before a circuit is established.

### Related Commands

Command

Description

debug cdapi

Displays information about the CDAPI.

## show ces clock-select

To display the setting of the network clock for the specified port,
                              		  use the show ces clock - select command in privileged EXEC mode.

show ces slot / port clock-select

### Syntax Description

slot

Backplane slot number.

/port

Interface port number. The slash must be entered.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.1(2)T

This command was introduced on the Cisco 3600 series.

## Examples

The following is sample output from this command for slot 1, port 0:

```
Router# show ces 1/0 clock-select Priority 1 clock source:not configured
Priority 2 clock source:not configured
Priority 3 clock source:ATM1/0 UP
Priority 4 clock source:Local oscillator
Current clock source:ATM1/0, priority:3
```

Field descriptions should be self-explanatory.

### Related Commands

Command

Description

clock-select

Establishes the sources and priorities of the requisite
                                          						clocking signals for the OC-3/STM-1 ATM Circuit Emulation Service network
                                          						module.

## show connect

To display configuration information about drop-and-insert
                              		  connections that have been configured on a router, use the show connect command in privileged EXEC mode.

show connect { all | elements | name | id | port { T1 | E1 } slot / port }

### Syntax Description

all

Information for all configured connections.

elements

Information for registered hardware or software
                                          						interworking elements.

name

Information for a connection that has been named by using
                                          						the connect global configuration
                                          						command. The name you enter is case sensitive and must match the configured
                                          						name exactly.

id

Information for a connection that you specify by an
                                          						identification number or range of identification numbers. The router assigns
                                          						these IDs automatically in the order in which they were created, beginning with
                                          						1. The show connect all command displays these IDs.

port

Information for a connection that you specify by indicating
                                          						the type of controller (T1 or E1) and location of the interface.

T1

T1 controller.

E1

E1 controller.

slot/port

Location of the T1 or E1 controller port whose connection
                                          						status you want to see. Valid values for slot and port are 0 and 1 . The slash must be entered.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(5)XK

This command was introduced on the Cisco 2600 series and
                                          						Cisco 3600 series.

12.0(7)T

This command was integrated into Cisco IOS Release
                                          						12.0(7)T.

### Usage Guidelines

This command shows drop-and-insert connections on modular access
                              		  routers that support drop-and-insert. It displays different information in
                              		  different formats, depending on the keyword that you use.

## Examples

The following examples show how the same tabular information appears
                              		  when you enter different keywords:

```
Router# show connect all ID   Name               Segment 1            Segment 2           State
========================================================================
1    Test              -T1 1/0 01           -T1 1/1 02           ADMIN UP
2    Test2             -T1 1/0 03           -T1 1/1 04           ADMIN UP
Router# show connect id 1-2 ID   Name               Segment 1            Segment 2           State
========================================================================
1    Test              -T1 1/0 01           -T1 1/1 02           ADMIN UP
2    Test2             -T1 1/0 03           -T1 1/1 04           ADMIN UP
Router# show connect port t1 1/1 ID   Name               Segment 1            Segment 2           State
========================================================================
1    Test              -T1 1/0 01           -T1 1/1 02           ADMIN UP
2    Test2             -T1 1/0 03           -T1 1/1 04           ADMIN UP
```

The following examples show details about specific connections,
                              		  including the number of time slots in use and the switching elements:

```
Router# show connect id 2 Connection: 2 - Test2
 Current State: ADMIN UP
 Segment 1: -T1 1/0 03
  TDM timeslots in use: 14-18 (5 total)
 Segment 2: -T1 1/1 04
  TDM timeslots in use: 14-18
Internal Switching Elements: VIC TDM Switch
Router# show connect name Test Connection: 1 - Test
 Current State: ADMIN UP
 Segment 1: -T1 1/0 01
  TDM timeslots in use: 1-13 (13 total)
 Segment 2: -T1 1/1 02
  TDM timeslots in use: 1-13
Internal Switching Elements: VIC TDM Switch
```

Field descriptions should be self-explanatory.

### Related Commands

Command

Description

connect

Defines connections between T1 or E1 controller ports for
                                          						Drop and Insert.

tdm-group

Configures a list of time slots for creating clear channel
                                          						groups (pass-through) for TDM cross-connect.

## show controllers rs366

To display information about the RS-366 video interface on the video dialing module (VDM), use the show controllers rs366 command in privileged EXEC mode.

show controllers rs366 slot port

### Syntax Description

slot

Slot location of the VDM module. Valid entries are 1 or 2.

port

Port location of the EIA/TIA-366 interface in the VDM module.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(5)XK

This command was introduced on the Cisco MC3810.

12.0(7)T

This command was integrated into Cisco IOS Release 12.0(7)T.

## Examples

The following example displays information about the RS-366 controller:

```
Router# show controllers rs366 0 1 RS366:driver is initialized in slot 1, port 0:
STATUS STATE LSR  LCR  ICSR EXT  T1     T2     T3     T4     T5
0x02   0x01  0x00 0x50 0xE0 0x00 5000   5000   5000   20000  10000
Dial string:
121C
```

The table below describes significant fields shown in this output.

Field

Description

STATUS

Last interrupt status.

STATE

Current state of the state machine.

LSR

Line status register of the VDM.

LCR

Line control register of the VDM.

ICSR

Interrupt control and status register of the VDM.

EXT

Extended register of the VDM.

T1 through T5

Timeouts 1 through 5 of the watchdog timer, in milliseconds.

Dial string

Most recently dialed number collected by the driver. 0xC at the end of the string indicates the EON (end of number) character.

## show controllers timeslots

To display the channel-associated signaling (CAS) and ISDN PRI state
                              		  in detail, use the show controllers timeslots command in privileged EXEC mode.

show controllers t1/e1 controller-number timeslots timeslot-range

### Syntax Description

tl/e1 controller - number

Controller number of CAS or ISDN PRI time slot. Range is
                                          						from 0 to 7.

timeslots timeslot - range

Timeslot. E1 range is from 1 to 31. T1 range is from 1 to
                                          						24.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

10.0

This command was introduced.

12.1(3)T

The timeslots keyword was added.

12.1(5)T

This command was implemented on the Cisco AS5400.

### Usage Guidelines

Use this command to display the CAS and ISDN PRI channel state in
                              		  detail. The command shows whether the DS0 channels of a controller are in idle,
                              		  in-service, maintenance, or busyout states. Use the show controllers e1 or show controllers t1 command to display statistics about the E1 or
                              		  T1 links.

## Examples

The following example shows that the CAS state is enabled on the
                              		  Cisco AS5300 with a T1 PRI card:

```
Router# show controllers timeslots T1 1 is up:
Loopback: NONE
DS0  Type       Modem    <->     Service       Channel       Rx          Tx
                                 State         State        A B C D      A B C D
-----------------------------------------------------------------------------------------
  1    cas-modem   1       in     insvc       connected    1  1  1  1    1  1  1  1
  2    cas         -       -      insvc       idle         0  0  0  0    0  0  0  0
  3    cas         -       -      insvc       idle         0  0  0  0    0  0  0  0
  4    cas         -       -      insvc       idle         0  0  0  0    0  0  0  0
  5    cas         -       -      insvc       idle         0  0  0  0    0  0  0  0
  6    cas         -       -      insvc       idle         0  0  0  0    0  0  0  0
  7    cas         -       -      insvc       idle         0  0  0  0    0  0  0  0
  8    cas         -       -      insvc       idle         0  0  0  0    0  0  0  0
  9    cas         -       -      insvc       idle         0  0  0  0    0  0  0  0
  10   cas         -       -      maint      static-bo     0  0  0  0    1  1  1  1
  11   cas         -       -      maint      static-bo     0  0  0  0    1  1  1  1
  12   cas         -       -      maint      static-bo     0  0  0  0    1  1  1  1
  13   cas         -       -      maint      static-bo     0  0  0  0    1  1  1  1
  14   cas         -       -      maint      static-bo     0  0  0  0    1  1  1  1
  15   cas         -       -      maint      static-bo     0  0  0  0    1  1  1  1
  16   cas         -       -      maint      static-bo     0  0  0  0    1  1  1  1
  17   cas         -       -      maint      static-bo     0  0  0  0    1  1  1  1
  18   cas         -       -      maint      static-bo     0  0  0  0    1  1  1  1
  19   cas         -       -      maint      dynamic-bo    0  0  0  0    1  1  1  1
  20   cas         -       -      maint      dynamic-bo    0  0  0  0    1  1  1  1
  21   cas         -       -      maint      dynamic-bo    0  0  0  0    1  1  1  1
  22   unused
  23   unused
  24   unused
```

The following example shows that the ISDN PRI state is enabled on the
                              		  Cisco AS5300 with a T1 PRI card:

```
T1 2 is up:
Loopback: NONE
DS0 Type         Modem    <->  Service   Channel     Rx        Tx
                               State     State       A B C D   A B C D
---------------------------------------------------------------------------
 1  pri          -        -    insvc     idle
 2  pri          -        -    insvc     idle
 3  pri          -        -    insvc     idle
 4  pri          -        -    insvc     idle
 5  pri          -        -    insvc     idle
 6  pri          -        -    insvc     idle
 7  pri          -        -    insvc     idle
 8  pri          -        -    insvc     idle
 9  pri          -        -    insvc     idle
10  pri          -        -    insvc     idle
11  pri          -        -    insvc     idle
12  pri          -        -    insvc     idle
13  pri          -        -    insvc     idle
14  pri          -        -    insvc     idle
15  pri          -        -    insvc     idle
16  pri          -        -    insvc     idle
17  pri          -        -    insvc     idle
18  pri          -        -    insvc     idle
19  pri          -        -    insvc     idle
20  pri          -        -    insvc     idle
21  pri-modem    2        in   insvc     busy
22  pri-modem    1        out  insvc     busy
23  pri-digi     -        in   insvc     busy
24  pri-sig      -        -    outofsvc  reserved
```

Field descriptions should be self-explanatory.

### Related Commands

Command

Description

show controllers e1

Displays information about E1 links.

show controllers t1

Displays information about T1 links.

## show controllers voice

To display information about voice-related hardware, use the show controllers voice command in privileged EXEC mode.

show controllers voice

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.0(5)XQ

This command was introduced on the Cisco 1750.

### Usage Guidelines

This command displays interface status information that is specific to voice-related hardware, such as the registers of the
                              TDM switch, the host port interface of the digital signal processor (DSP), and the DSP firmware versions. The information
                              displayed is generally useful only for diagnostic tasks performed by technical support.

## Examples

The following is sample output from this command:

```
Router# show controllers voice EPIC Switch registers:
STDA 0xFF STDB 0xFF SARA 0xAD SARB 0xFF SAXA 0xFF SAXB 0x0 STCR 0x3F
MFAIR 0x3F
STAR 0x65 OMDR 0xE2 VNSR 0x0 PMOD 0x4C PBNR 0xFF POFD 0xF0 POFU 0x18
PCSR 0x1 PICM 0x0 CMD1 0xA0 CMD2 0x70 CBNR 0xFF CTAR 0x2 CBSR 0x20 CSCR
0x0
DSP 0 Host Port Interface:
HPI Control Register 0x202
InterfaceStatus 0x2A MaxMessageSize 0x80
RxRingBufferSize 0x6 TxRingBufferSize 0x9
pInsertRx 0x4 pRemoveRx 0x4 pInsertTx 0x6 pRemoveTx 0x6
Rx Message 0:
packet_length 100 channel_id 2 packet_id 0 process id 0x1
0000:   0000 4AC7 5F08 91D1 0000 0000 7DF1 69E5 63E1 63E2
0020:   6E7C ED67 DE5D DB5C DC60 EC7E 6BE1 58D3 50CD 4DCE
0040:   50D2 5AE5 7868 DA52 CE4A C746 C647 C94B D25A EAF4
0060:   5DD7 4FCD 4ACA 4ACC 4FD3 5DE8 F769 DC58 D352 D253
0080:   D65B E573 6CDF 59D3 4ECF 4FD0
Rx Message 1:
packet_length 100 channel_id 1 packet_id 0 process id 0x1
0000:   0000 1CDD 3E48 3B74 0000 0000 3437 3D4C F0C8 BBB5
0020:   B2B3 B7BF D25B 4138 3331 3339 435F CFBD B6B2 B1B4
0040:   BBC8 7E48 3B34 3131 363D 4FDE C3B9 B3B1 B3B8 C2DB
0060:   533F 3833 3235 3B48 71CC BDB7 B4B5 B8BF CF67 483D
0080:   3836 383C 455B DAC6 BDB9 B9BB
Rx Message 2:
packet_length 100 channel_id 2 packet_id 0 process id 0x1
0000:   0000 4AC8 5F08 9221 0000 0000 54DA 61F5 EF60 DA53
0020:   CF4F CD4E D256 DB63 FCEE 5FDA 55D1 50CF 4FD3 56D8
0040:   5DE1 6E7C EC60 DC59 D655 D456 D85D DF6A F4F4 69E2
0060:   5CDD 5BDC 5BDE 61E9 6DF1 FF76 F16D E96A E566 EA6A
0080:   EB6F F16D EF79 F776 F5F5 73F0
Rx Message 3:
packet_length 100 channel_id 1 packet_id 0 process id 0x1
0000:   0000 1CDE 3E48 3BC4 0000 0000 C0CC EC54 453E 3C3C
0020:   3F47 56F3 D1C7 C1BF C0C6 CEE1 6752 4A46 4648 4E59
0040:   6FE4 D6CF CDCE D2DA E57E 675E 5B5B 5E62 6B76 FCF6
0060:   F6FA 7D75 7373 7BF5 EAE1 DCDA DADD E6FE 6559 514D
0080:   4D4E 5563 EFD9 CDC8 C5C6 CAD1
Rx Message 4:
packet_length 100 channel_id 2 packet_id 0 process id 0x1
0000:   0000 4AC6 5F08 9181 0000 0000 DD5B DC5E E161 E468
0020:   FAFD 6CE1 5AD3 53D1 53D7 61EC EA59 CF4A C644 C344
0040:   CA4E D86C 60D0 48C2 3EBD 3CBD 3EC0 47CF 5976 DF4F
0060:   C945 C242 C146 C94E D668 73DB 54CE 4DCC 4DCE 53DB
0080:   64F9 ED63 DC59 DA58 DC5D E46C
Rx Message 5:
packet_length 100 channel_id 1 packet_id 0 process id 0x1
0000:   0000 1CDC 3E48 3B24 0000 0000 5B5B 5D62 6A76 FCF5
0020:   F5F9 7D78 7374 7CF5 EAE1 DDDA DBDD E7FE 6559 514E
0040:   4D4F 5663 EFD8 CDC8 C6C6 CAD1 E760 4E46 403F 4047
0060:   5173 D5C7 BFBC BCBE C5D4 6D4C 3F3B 3939 3D46 5ADB
0080:   C5BC B7B6 B8BD C8E8 4F3F 3835
Tx Message 0:
packet_length 100 channel_id 1 packet_id 0 process id 0x1
0000:   0000 4AC6 5F08 9181 0000 003C DD5B DC5E E161 E468
0020:   FAFD 6CE1 5AD3 53D1 53D7 61EC EA59 CF4A C644 C344
0040:   CA4E D86C 60D0 48C2 3EBD 3CBD 3EC0 47CF 5976 DF4F
0060:   C945 C242 C146 C94E D668 73DB 54CE 4DCC 4DCE 53DB
0080:   64F9 ED63 DC59 DA58 DC5D E46C
Tx Message 1:
packet_length 100 channel_id 2 packet_id 0 process id 0x1
0000:   0000 1CDC 3E48 3B24 0000 003C 5B5B 5D62 6A76 FCF5
0020:   F5F9 7D78 7374 7CF5 EAE1 DDDA DBDD E7FE 6559 514E
0040:   4D4F 5663 EFD8 CDC8 C6C6 CAD1 E760 4E46 403F 4047
0060:   5173 D5C7 BFBC BCBE C5D4 6D4C 3F3B 3939 3D46 5ADB
0080:   C5BC B7B6 B8BD C8E8 4F3F 3835
Tx Message 2:
packet_length 100 channel_id 1 packet_id 0 process id 0x1
0000:   0000 4AC7 5F08 91D1 0000 003C 7DF1 69E5 63E1 63E2
0020:   6E7C ED67 DE5D DB5C DC60 EC7E 6BE1 58D3 50CD 4DCE
0040:   50D2 5AE5 7868 DA52 CE4A C746 C647 C94B D25A EAF4
0060:   5DD7 4FCD 4ACA 4ACC 4FD3 5DE8 F769 DC58 D352 D253
0080:   D65B E573 6CDF 59D3 4ECF 4FD0
Tx Message 3:
packet_length 100 channel_id 2 packet_id 0 process id 0x1
0000:   0000 1CDD 3E48 3B74 0000 003C 3437 3D4C F0C8 BBB5
0020:   B2B3 B7BF D25B 4138 3331 3339 435F CFBD B6B2 B1B4
0040:   BBC8 7E48 3B34 3131 363D 4FDE C3B9 B3B1 B3B8 C2DB
0060:   533F 3833 3235 3B48 71CC BDB7 B4B5 B8BF CF67 483D
0080:   3836 383C 455B DAC6 BDB9 B9BB
Tx Message 4:
packet_length 100 channel_id 1 packet_id 0 process id 0x1
0000:   0000 4AC8 5F08 9221 0000 003C 54DA 61F5 EF60 DA53
0020:   CF4F CD4E D256 DB63 FCEE 5FDA 55D1 50CF 4FD3 56D8
0040:   5DE1 6E7C EC60 DC59 D655 D456 D85D DF6A F4F4 69E2
0060:   5CDD 5BDC 5BDE 61E9 6DF1 FF76 F16D E96A E566 EA6A
0080:   EB6F F16D EF79 F776 F5F5 73F0
Tx Message 5:
packet_length 100 channel_id 2 packet_id 0 process id 0x1
0000:   0000 1CDE 3E48 3BC4 0000 003C C0CC EC54 453E 3C3C
0020:   3F47 56F3 D1C7 C1BF C0C6 CEE1 6752 4A46 4648 4E59
0040:   6FE4 D6CF CDCE D2DA E57E 675E 5B5B 5E62 6B76 FCF6
0060:   F6FA 7D75 7373 7BF5 EAE1 DCDA DADD E6FE 6559 514D
0080:   4D4E 5563 EFD9 CDC8 C5C6 CAD1
Tx Message 6:
packet_length 100 channel_id 2 packet_id 0 process id 0x1
0000:   0000 1CDA 3E48 3A84 0000 003C E75F 4E46 403F 4147
0020:   5174 D5C7 BFBC BCBE C5D4 6C4C 3F3B 3939 3D46 5BDA
0040:   C5BC B7B6 B8BD C8E9 4F3F 3834 3437 3D4C EEC8 BBB5
0060:   B2B3 B8BF D35A 4138 3331 3339 435F CEBD B6B1 B1B4
0080:   BBC9 7C48 3B34 3131 363D 4FDE
Tx Message 7:
packet_length 100 channel_id 1 packet_id 0 process id 0x1
0000:   0000 4AC5 5F08 9131 0000 003C 66DE 66EB 67EE FE6E
0020:   F7E7 6B68 E068 EE6A DF5C DF62 EDF1 6FF2 7A78 67DC
0040:   5EDF 62E7 64E6 66E0 7071 EA69 F86E E260 DE5D E665
0060:   EB75 F0FB 6DE9 64E4 69E3 66EA 67E9 6DF9 F177 EC6E
0080:   EB6E F876 F875 7D6E E966 E05D
Tx Message 8:
packet_length 100 channel_id 2 packet_id 0 process id 0x1
0000:   0000 1CDB 3E48 3AD4 0000 003C C2B9 B3B1 B3B8 C2DC
0020:   523F 3733 3235 3C49 72CB BDB7 B4B5 B8BF CF67 483C
0040:   3836 373C 455C DAC6 BDB9 B9BB C0CC EE54 453E 3C3C
0060:   3F47 56F1 D1C7 C1BF C0C6 CEE1 6651 4A46 4648 4D59
0080:   70E3 D6CF CDCE D2D9 E67E 675E
Bootloader 1.8, Appn 3.1
Application firmware 3.1.8, Built by claux on Thu Jun 17 11:00:05 1999
VIC Interface Foreign Exchange Station 0/0, DSP instance (0x19543C0)
Singalling channel num 128 Signalling proxy 0x0 Signaling dsp 0x19543C0
tx outstanding 0, max tx outstanding 32
ptr 0x0, length 0x0, max length 0x0
dsp_number 0, Channel ID 1
received 0 packets, 0 bytes, 0 gaint packets
0 drops, 0 no buffers, 0 input errors 0 input overruns
650070 bytes output, 4976 frames output, 0 output errors, 0 output
underrun
0 unaligned frames
VIC Interface Foreign Exchange Station 0/1, DSP instance (0x1954604)
Singalling channel num 129 Signalling proxy 0x0 Signaling dsp 0x1954604
tx outstanding 0, max tx outstanding 32
ptr 0x0, length 0x0, max length 0x0
dsp_number 0, Channel ID 2
received 0 packets, 0 bytes, 0 gaint packets
0 drops, 0 no buffers, 0 input errors 0 input overruns
393976 bytes output, 3982 frames output, 0 output errors, 0 output
underrun
0 unaligned frames
```

Field descriptions are hardware-dependent and are meant for use by trained technical support.

### Related Commands

Command

Description

show dial-peer voice

Displays configuration information and call statistics for dial peers.

show interface dspfarm

Displays hardware information including DRAM, SRAM, and the revision-level information on the line card.

show voice dsp

Displays the current status of all DSP voice channels.

show voice port

Displays configuration information about a specific voice port.

## show crm

To display the carrier call capacities statistics, use the show crm command in privileged EXEC mode.

show crm

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

This command was introduced.

### Usage Guidelines

Both the show trunk group command and the show crm command display values for the maximum number of calls. These values originate from different configuration procedures:

In the show trunk group command, the Max Calls value originates from the max - calls command in the trunk group configuration.

In the show crm command, Max calls indicates the maximum number of available channels after the carrier ID or trunk group label is assigned
                                    to an interface using the trunk - group (interface) command.

## Examples

The following example illustrates the carrier call capacities statistics:

```
Router# show crm Carrier:1411
    Max calls:4
    Max Voice (in) :      4    Cur Voice (in) :      0
    Max Voice (out):      4    Cur Voice (out):      0
    Max Data (in)  :      4    Cur Data (in)  :      0
    Max Data (out) :      4    Cur Data (out) :      0
Trunk Group Label: 100
    Max calls:6
    Max Voice (in) :      6    Cur Voice (in) :      0
    Max Voice (out):      6    Cur Voice (out):      0
    Max Data (in)  :      6    Cur Data (in)  :      0
    Max Data (out) :      6    Cur Data (out) :      0
```

The table below describes the fields shown in this output, in alphabetical order.

Field

Description

Carrier

ID of the carrier that handles the calls.

Cur Data (in)

Current number of incoming data calls that are handled by the carrier or trunk group.

Cur Data (out)

Current number of outgoing data calls that are handled by the carrier or trunk group.

Cur Voice (in)

Current number of incoming voice calls that are handled by the carrier or trunk group.

Cur Voice (out)

Current number of outgoing voice calls that are handled by the carrier or trunk group.

Max Calls

Maximum number of calls that are handled by the carrier or trunk group.

Max Data (in)

Maximum number of incoming data calls that are handled by the carrier or trunk group.

Max Data (out)

Maximum number of outgoing data calls that are handled by the carrier or trunk group.

Max Voice (in)

Maximum number of incoming voice calls that are handled by the carrier or trunk group.

Max Voice (out)

Maximum number of outgoing voice calls that are handled by the carrier or trunk group.

Trunk Group Label

Label of the trunk group that handles the calls.

### Related Commands

Command

Description

carrier-id (dial-peer)

Specifies the carrier associated with VoIP calls.

max-calls

Specifies the maximum number of calls handled by a trunk group.

show trunk group

Displays the configuration parameters for one or more trunk groups.

trunk-group (interface)

Assigns an interface to a trunk group.

trunk-group-label (dial-peer)

Specifies the trunk group associated with VoIP calls.

## show csm

To display the call switching module (CSM) statistics for a particular digital signal processor (DSP) channel, all DSP channels,
                              or a specific modem or DSP channel, use the show csm command in privileged EXEC mode.

### Cisco AS5300 Universal Access Server

show csm { call-rate [ table ] | callre-source | modem [ slot / port | group modem-group-number ] | signaling-channel }

### Cisco AS5400Series Router

show csm { call rate [ table ] | call-resource | modem [ slotport | group modem-group-number ] | signaling-channel | voice slot / port }

### Syntax Description

call-rate

Displays the incoming and outgoing call switching rate.

table

(Optional) Displays the incoming and outgoing call switching rate in the form of numerical table.

call-resource

Displays statistics about the CSM call resource.

modem

Displays CSM call statistics for modems.

slot / port

(Optional) Location (and thereby identity) of a specific modem.

group

(Optional) Displays modem group information.

modem - group - number

(Optional) Location of a particular dial peer. Range: 1 to 32767.

signaling-channel

Displays CSM signaling channel Information.

voice

Displays CSM call statistics for DSP channels.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

11.3 NA

This command was introduced.

12.0(3)T

This command was modified. Port-specific values for the Cisco AS5300 were added.

12.0(7)T

This command was modified. Port-specific values for the Cisco AS5800 were added.

### Usage Guidelines

This command shows the information related to CSM, which includes the DSP channel, the start time of the call, the end time
                              of the call, and the channel on the controller used by the call.

Use the show csm modem command to display the CSM call statistics for a specific modem, for a group of modems, or for all modems. If a slot / port argument is specified, then CSM call statistics are displayed for the specified modem. If the modem-group-number argument is specified, the CSM call statistics for all of the modems associated with that modem group are displayed. If no
                              keyword is specified, CSM call statistics for all modems on the Cisco AS5300 universal access server are displayed.

Use the show csm voice command to display CSM statistics for a particular DSP channel. If the slot / dspm / dsp / dsp-channel or shelf / slot / port argument is specified, the CSM call statistics for calls using the identified DSP channel are displayed. If no argument is specified,
                              all CSM call statistics for all DSP channels are displayed.

## Examples

The following is sample output from the show csm command for the Cisco AS5300 universal access server:

```
Router# show csm voice 2/4/4/0 slot 2, dspm 4, dsp 4, dsp channel 0,
 slot 2, port 56, tone, device_status(0x0002): VDEV_STATUS_ACTIVE_CALL.
csm_state(0x0406)=CSM_OC6_CONNECTED, csm_event_proc=0x600E2678, current call thru PRI line
invalid_event_count=0, wdt_timeout_count=0
wdt_timestamp_started is not activated
wait_for_dialing:False, wait_for_bchan:False
pri_chnl=TDM_PRI_STREAM(s0, u0, c22), tdm_chnl=TDM_DSP_STREAM(s2, c27)
dchan_idb_start_index=0, dchan_idb_index=0, call_id=0xA003, bchan_num=22
csm_event=CSM_EVENT_ISDN_CONNECTED, cause=0x0000
ring_no_answer=0, ic_failure=0, ic_complete=0
dial_failure=0, oc_failure=0, oc_complete=3
oc_busy=0, oc_no_dial_tone=0, oc_dial_timeout=0
remote_link_disc=0, stat_busyout=0
oobp_failure=0
call_duration_started=00:06:53, call_duration_ended=00:00:00, total_call_duration=00:00:44
The calling party phone number = 408
The called party phone number  = 5271086
total_free_rbs_timeslot = 0, total_busy_rbs_timeslot = 0, total_dynamic_busy_rbs_timeslot = 0, total_static_busy_rbs_timeslot = 0,
total_sw56_rbs_timeslot = 0, total_sw56_rbs_static_bo_ts = 0,
total_free_isdn_channels = 21, total_busy_isdn_channels = 0,total_auto_busy_isdn_channels = 0,
min_free_device_threshold = 0
```

The table below describes the significant fields shown in the display.

Field

Description

slot

Slot where the VFC resides.

dsp

DSP through which this call is established.

slot/port

Logical port number for the device. This is equivalent to the DSP channel number. The port number is derived as follows:

(max_number_of_dsp_channels per dspm=12) * the dspm # (0-based) +

(max_number_of_dsp_channels per dsp=2) * the dsp # (0-based) + the dsp channel number (0-based).

tone

Which signaling tone is being used (DTMF, MF, R2). This only applies to CAS calls. Possible values are as follows:

mf

dtmf

r2-compelled

r2-semi-compelled

r2-non-compelled

device_status

Status of the device. Possible values are as follows:

VDEV_STATUS_UNLOCKED--Device is unlocked (meaning that it is available for new calls).

VDEV_STATUS_ACTIVE_WDT--Device is allocated for a call and the watchdog timer is set to time the connection response from
                                                the central office.

VDEV_STATUS_ACTIVE_CALL--Device is engaged in an active, connected call.

VDEV_STATUS_BUSYOUT_REQ--Device is requested to busyout; does not apply to voice devices.

VDEV_STATUS_BAD--Device is marked as bad and not usable for processing calls.

VDEV_STATUS_BACK2BACK_TEST--Modem is performing back-to-back testing (for modem calls only).

VDEV_STATUS_RESET--Modem needs to be reset (for modem only).

VDEV_STATUS_DOWNLOAD_FILE--Modem is downloading a file (for modem only).

VDEV_STATUS_DOWNLOAD_FAIL--Modem has failed during downloading a file (for modem only).

VDEV_STATUS_SHUTDOWN--Modem is not powered up (for modem only).

VDEV_STATUS_BUSY--Modem is busy (for modem only).

VDEV_STATUS_DOWNLOAD_REQ--Modem is requesting connection (for modem only).

csm_state

CSM call state of the current call (PRI line) associated with this device. Possible values are as follows:

CSM_IDLE_STATE--Device is idle.

CSM_IC_STATE--A device has been assigned to an incoming call.

CSM_IC1_COLLECT_ADDR_INFO--A device has been selected to perform ANI/DNIS address collection for this call. ANI/DNIS address
                                                information collection is in progress. The ANI/DNIS is used to decide whether the call should be processed by a modem or a
                                                voice DSP.

CSM_IC2_RINGING--The device assigned to this incoming call has been told to get ready for the call.

CSM_IC3_WAIT_FOR_SWITCH_OVER--A new device is selected to take over this incoming call from the device collecting the ANI/DNIS
                                                address information.

CSM_IC4_WAIT_FOR_CARRIER--This call is waiting for the CONNECT message from the carrier.

CSM_IC5_CONNECTED--This incoming call is connected to the central office.

CSM_IC6_DISCONNECTING--This incoming call is waiting for a DISCONNECT message from the VTSP module to complete the disconnect
                                                process.

CSM_OC_STATE --An outgoing call is initiated.

CSM_OC1_REQUEST_DIGIT--The device is requesting the first digit for the dial-out number.

CSM_OC2_COLLECT_1ST_DIGIT--The first digit for the dial-out number has been collected.

CSM_OC3_COLLECT_ALL_DIGIT--All the digits for the dial-out number have been collected.

CSM_OC4_DIALING--This call is waiting for a dsx0 (B channel) to be available for dialing out.

CSM_OC5_WAIT_FOR_CARRIER--This (outgoing) call is waiting for the central office to connect.

CSM_OC6_CONNECTED--This (outgoing) call is connected.

CSM_OC7_BUSY_ERROR--A busy tone has been sent to the device (for VoIP call, no busy tone is sent; just a DISCONNECT INDICATION
                                                message is sent to the VTSP module), and this call is waiting for a DISCONNECT message from the VTSP module (or ONHOOK message
                                                from the modem) to complete the disconnect process.

CSM_OC8_DISCONNECTING--The central office has disconnected this (outgoing) call, and the call is waiting for a DISCONNECT
                                                message from the VTSP module to complete the disconnect process.

csm_state: invalid_event_count

Number of invalid events received by the CSM state machine.

wdt_timeout_count

Number of times the watchdog timer is activated for this call.

wdt_timestamp_started

Whether the watchdog timer is activated for this call.

wait_for_dialing

Whether this (outgoing) call is waiting for a free digit collector to become available to dial out the outgoing digits.

wait_for_bchan

Whether this (outgoing) call is waiting for a B channel to send the call out on.

pri_chnl

Which type of TDM stream is used for the PRI connection. For PRI and CAS calls, it is always TDM_PRI_STREAM.

tdm_chnl

Which type of TDM stream is used for the connection to the device used to process this call. In the case of a VoIP call,
                                          this is always set to TDM_DSP_STREAM.

dchan_idb_start_index

First index to use when searching for the next IDB of a free D channel.

dchan_idb_index

Index of the currently available IDB of a free D channel.

csm_event

Event just passed to the CSM state machine.

cause

Event cause.

ring_no_answer

Number of times a call failed because there was no response.

ic_failure

Number of failed incoming calls.

ic_complete

Number of successful incoming calls.

dial_failure

Number of times a connection failed because there was no dial tone.

oc_failure

Number of failed outgoing calls.

oc_complete

Number of successful outgoing calls.

oc_busy

Number of outgoing calls whose connection failed because there was a busy signal.

oc_no_dial_tone

Number of outgoing calls whose connection failed because there was no dial tone.

oc_dial_timeout

Number of outgoing calls whose connection failed because the timeout value was exceeded.

call_duration_started

Start of this call.

call_duration_ended

End of this call.

total_call_duration

Duration of this call.

The calling party phone number

Calling party number as given to CSM by ISDN.

The called party phone number

Called party number as given to CSM by ISDN.

total_free_rbs_time slot

Total number of free RBS (CAS) time slots available for the whole system.

total_busy_rbs_time slot

Total number of RBS (CAS) time slots that have been busied-out. This includes both dynamically and statically busied out
                                          RBS time slots.

total_dynamic_busy_rbs_time slot

Total number of RBS (CAS) time slots that have been dynamically busied out.

total_static_busy_rbs_time slot

Total number of RBS (CAS) time slots that have been statically busied out (that is, they are busied out using the CLI command).

total_free_isdn_channels

Total number of free ISDN channels.

total_busy_isdn_channels

Total number of busy ISDN channels.

total_auto_busy_isdn_channels

Total number of ISDN channels that are automatically busied out.

### Related Commands

Command

Description

show call active voice

Displays the contents of the active call table.

show call history voice

Displays the contents of the call history table.

show num-exp

Displays how number expansions are configured.

show voice port

Displays configuration information about a specific voice port.

## show csm call

To view the call switching module (CSM) call statistics, use the show csm call command in privileged EXEC mode

show csm call { failed | rate | total }

### Syntax Description

failed

CSM call fail/reject rate for the last 60 seconds, 60 minutes, and 72 hours.

rate

CSM call rate for the last 60 seconds, 60 minutes, and 72 hours.

total

Total number of CSM calls for the last 60 seconds, 60 minutes, and 72 hours.

### Command Default

No default behavior or values.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3(2)T

This command was introduced on the Cisco AS5850.

### Usage Guidelines

Use this command to understand CSM call volume.

## Examples

The following examples show the CSM call statistics for the last 60 seconds:

```
Router# show csm call rate 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0....5....1....1....2....2....3....3....4....4....5....5.... 0    5    0    5    0    5    0    5    0    5 CSM call switching rate per second (last 60 seconds) # = calls entering the module per second Router# show csm call failed 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0....5....1....1....2....2....3....3....4....4....5....5.... 0    5    0    5    0    5    0    5    0    5 CSM call fail/reject rate per second (last 60 seconds) # = calls failing per second Router# sh csm call total 1344 1244 1144 1044 944 844 744 644 544 444 344 244 144 44 0....5....1....1....2....2....3....3....4....4....5....5.... 0    5    0    5    0    5    0    5    0    5 CSM total calls (last 60 seconds)
```

# = number of calls

Field descriptions should be self-explanatory.

## show cube debug category codes

To display Cisco Unified Border Element debug category code information, use the show cube debug category codes command in user EXEC or privileged EXEC mode.

show cube debug category codes

### Syntax Description

This command has no arguments or keywords.

### Command Modes

User EXEC (>)

Privileged EXEC (#)

## Command History

15.3(3)M

This command was introduced.

## Examples

```
Device# show cube debug category codes |-----------------------------------------------
| show cube debug category codes values.
|-----------------------------------------------
| Indx |  Debug Name           |   Value
|-----------------------------------------------
|  01  |  SDP Debugs           |   1
|  02  |  Audio Debugs         |   2
|  03  |  Video Debugs         |   4
|  04  |  Fax Debugs           |   8
|  05  |  SRTP Debugs          |   16
|  06  |  DTMF Debugs          |   32
|  07  |  SIP Profiles Debugs  |   64
|  08  |  SDP Passthrough Deb  |   128
|  09  |  Transcoder Debugs    |   256
|  10  |  SIP Transport Debugs |   512
|  11  |  Parse Debugs         |   1024
|  12  |  Config Debugs        |   2048
|  13  |  Control Debugs       |   4096
|  14  |  Miscellaneous Debugs |   8192
|  15  |  Supp Service Debugs  |   16384
|  16  |  Misc  Features Debugs|   32768
|  17  |  SIP Line-side Debugs |   65536
|  18  |  CAC Debugs           |   131072
|  19  |  Registration Debugs  |   262144
|-----------------------------------------------
```

## show cube status

To display the Cisco Unified Border Element ( CUBE ) status, the software version, the license capacity, the image version, and the platform name of the device, use the show cube status command in user EXEC or privileged EXEC mode.

show cube status

### Syntax Description

This command has no arguments or keywords.

### Command Default

In releases before Cisco IOS XE Amsterdam 17.2.1r , CUBE status is not displayed unless license capacity is configured using mode border-element command.

Effective from Cisco IOS XE Amsterdam 17.2.1r , the dependency on configuring license capacity is removed.

### Command Modes

User EXEC (>)

Privileged EXEC (#)

## Command History

Release

Modification

Cisco IOS XE Amsterdam 17.3.2 and Cisco IOS XE Bengaluru 17.4.1a

This command was modified to support Cisco Smart Licensing Using Policy.

Cisco IOS XE Amsterdam 17.2.1r

The dependency on mode border-element license capacity sessions command was removed. Licensed-Capacity and blocked call information was excluded from output.

15.1(3)S1

This command was modified.

The output was modified to have only token characters (an alphanumeric character, hyphen [-], dot [.], exclamation mark [!],
                                          percent [%], asterisk [*], underscore [_], plus sign [+], grave [`], apostrophe ['], or a tilde [~]) in server and user-agent
                                          Session Initiation Protocol (SIP) headers. The nontoken characters present in the image name is replaced by a dot[.].

15.2(1)T

This command was introduced.

### Usage Guidelines

In releases before Cisco IOS XE Amsterdam 17.2.1r , the CUBE status display is enabled only if the mode border-element command is configured with call license capacity. The show cube status command displays the following message if the license capacity is not configured

```
Cisco Unified Border Element (CUBE) application is not enabled
```

Effective from Cisco IOS XE Amsterdam 17.2.1r , CUBE status display is enabled without configuring mode border-element license capacity sessions command. Licensed-Capacity and blocked call information is excluded from output.

CUBE status information is also available using Simple Network Management Protocol (SNMP) with the CISCO-UBE-MIB MIB.

## Examples

Example - Releases before Cisco IOS XE Amsterdam 17.2.1r

The following example configures the mode border-element command with call license capacity and enables the display of CUBE status on the Cisco 3845 router:

```
Device(config)# voice service voip Device(conf-voi-serv)# mode border-element license capacity 200
```

After saving the configuration and reloading the device:

```
Device> show cube status CUBE-Version : 11.0.0
SW-Version : 15.5(2)T, Platform 3845
HA-Type : none
Licensed-Capacity : 200
```

In Cisco IOS Release 15.1(3)S1 and later releases, the output is as follows:

```
Device> show cube status CUBE-Version : 8.8
SW-Version : 15.2.1.T, Platform 3845
HA-Type : none
Licensed-Capacity : 200
```

Example - Release Cisco IOS XE Amsterdam 17.2.1r and later

From Cisco IOS XE Amsterdam 17.2.1r onwards, the output is displayed as follows:

```
Device> show cube status CUBE-Version : 12.7.0
SW-Version : 16.12.20191014.105214, Platform CSR1000V
HA-Type : hot-standby-chassis-to-chassis
```

## Examples

The table below describes the fields shown in the display.

Field

Description

CUBE-Version

Version of the CUBE application running on the device.

SW-Version

Image version and platform name of the device running the CUBE application. This matches the image version and platform name returned by the show version command.

HA-Type

The type of High Availability (HA) feature configured and running on the device. The following HA types are supported:

none: CUBE does not support HA.

cold-standby-chassis-to-chassis: Device-to-device cold standby support.

hot-standby-chassis-to-chassis: Device-to-device hot standby support.

Licensed-Capacity

Effective from Cisco IOS XE Amsterdam 17.2.1r , Licensed-Capacity and blocked call information is no longer included in the output.

Number of SIP call legs that CUBE is licensed to use. The range is from 0 through 999999. This number matches the number of licenses configured using the mode border-element license capacity command.

The number of SIP call legs that CUBE can use is platform-dependent and is not affected by the specified value for the capacity keyword in Cisco IOS Release 15.2(1)T.

### Related Commands

Command

Description

mode border-element

Enables the set of commands used in the border-element configuration on the Cisco 2900 and Cisco 3900 series platforms.

## show debug condition

To display the debugging filters that have been enabled for VoiceXML applications, ATM-enabled interfaces, or Frame Relay
                              interfaces, use the show debug condition command in privileged EXEC mode.

show debug condition

### Syntax Description

This command has no arguments or keywords.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(11)T

This command was introduced on the Cisco 3640, Cisco 3660, Cisco AS5300, Cisco AS5350, and Cisco AS5400.

12.0(28)S

This command was integrated into Cisco IOS Release 12.0(28)S and was enhanced to include debugging for ATM-enabled and Frame
                                          Relay-enabled interfaces.

12.2(25)S

This command was integrated into Cisco IOS Release 12.2(25)S.

12.2(27)SBC

This command was integrated into Cisco IOS Release 12.2(27)SBC.

12.2(28)SB

This command was integrated into Cisco IOS Release 12.2(28)SB.

12.4(9)T

This command was enhanced to include debugging for ATM-enabled and Frame Relay-enabled interfaces.

### Usage Guidelines

This command displays the debugging filter conditions that have been set for VoiceXML applications by using the debug condition application voice command.

## Examples

The following is sample output from this command when it is used with the VoiceXML application:

```
Router# show debug condition Condition 1: application voice vmail (1 flags triggered)
       Flags: vmail
Condition 2: application voice myapp1 (1 flags triggered)
       Flags: myapp1
```

The following is sample output from this command when an ATM interface is being debugged:

```
Router# show debug condition Condition 1: atm-vc 0/56784 AT2/0 (0 flags triggered)
Condition 2: atm-vc 255/45546 AT2/0 (0 flags triggered)
Condition 3: atm-vc 0/266 AT6/0 (1 flags triggered)
```

The table below describes the significant fields shown in the display.

Field

Description

Condition 1

Sequential number identifying the filter condition that was set for the specified command.

Flags

Name of the voice application for which the condition was set.

at2/0

Interface number of the ATM interface that has the debug condition applied.

atm-vc 0/56784

Virtual channel identifier (VCI). Alternatively, virtual path identifier/virtual channel identifier (VCI/VPI) pair.

### Related Commands

Command

Description

debug condition application voice

Filters out debugging messages for all VoiceXML applications except the specified application.

debug http client

Displays debugging messages for the HTTP client.

debug vxml

Displays debugging messages for VoiceXML features.

| brief | (Optional) Displays a truncated version of the call history table. |
|---|---|
| id identifier | (Optional) Displays only the call with the specified identifier. Range is a hex
                                          						value from 1 to FFFF. |
| compact | (Optional) Displays a compact version. |
| duration time | (Optional) Displays history information for calls that are longer or shorter
                                          						than a specified time value. The arguments and keywords are as follows: less--Displays calls shorter than the value in the time argument. more--Displays calls longer than the value in the time argument. time --Elapsed time, in seconds. Range is from 1 to
                                                							 2147483647. |
| last number | (Optional) Displays the last calls connected, where the number of calls that
                                          						appear is defined by the number argument . Range is from 1 to 100 . |

| Release | Modification |
|---|---|
| 11.3(1)T | This
                                          						command was introduced on the Cisco 3600 series. |
| 12.0(3)XG | This
                                          						command was implemented for Voice over Frame Relay (VoFR) on the Cisco 2600
                                          						series and Cisco 3600 series. |
| 12.0(4)XJ | This
                                          						command was modified for store-and-forward fax. |
| 12.0(4)T | This
                                          						command was modified. The brief keyword
                                          						was added, and the command was implemented on the Cisco 7200 series. |
| 12.0(7)XK | This
                                          						command was modified. The brief keyword
                                          						was implemented on the Cisco MC3810. |
| 12.1(2)T | This
                                          						command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.1(5)XM | This
                                          						command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | This
                                          						command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XA | This
                                          						command was modified. The output of this command was modified to indicate
                                          						whether the call in question has been established using Annex E. |
| 12.2(4)T | This
                                          						command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(2)XB1 | This
                                          						command was implemented on the Cisco AS5850. |
| 12.2(8)T | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco
                                          						AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 was not included in this
                                          						release. |
| 12.2(11)T | This
                                          						command was implemented on the Cisco AS5350, Cisco AS5400, Cisco AS5800, and
                                          						Cisco AS5850. |
| 12.3(1) | This
                                          						command was modified. The following fields were added:
                                          						FaxRelayMaxJitterBufDepth, FaxRelayJitterBufOverFlow, FaxRelayHSmodulation, and
                                          						FaxRelayNumberOfPages. |
| 12.3(14)T | This
                                          						command was modified. T.38 fax relay call statistics were made available to
                                          						Call Detail Records (CDRs) through vendor-specific attributes (VSAs) and added
                                          						to the call log. |
| 12.4(15)T | This
                                          						command was modified. The Port and BearerChannel display fields were added to
                                          						the TELE call leg record of the command output. |
| 12.4(16) | This
                                          						command was modified. The Port and BearerChannel display fields were added to
                                          						the TELE call leg record of the command output. |
| 12.4(22)T | This
                                          						command was modified. Command output was updated to show IPv6 information. |

| Field | Description |
|---|---|
| ACOM
                                          					 Level | Current
                                          					 ACOM level for this call. ACOM is the combined loss achieved by the echo
                                          					 canceler, which is the sum of the Echo Return Loss, Echo Return Loss
                                          					 Enhancement, and nonlinear processing loss for the call. |
| BearerChannel | Identification of the bearer channel carrying the call. |
| Buffer
                                          					 Drain Events | Total
                                          					 number of jitter buffer drain events. |
| Buffer
                                          					 Fill Events | Total
                                          					 number of jitter buffer fill events. |
| CallDuration | Length of
                                          					 the call, in hours, minutes, and seconds, hh:mm:ss. |
| CallerName | Voice
                                          					 port station name string. |
| CallOrigin | Call
                                          					 origin: answer or originate. |
| CallState | Current
                                          					 state of the call. |
| ChargedUnits | Total
                                          					 number of charging units that apply to this peer since system startup. The unit
                                          					 of measure for this field is hundredths of second. |
| CodecBytes | Payload
                                          					 size, in bytes, for the codec used. |
| CoderTypeRate | Negotiated coder rate. This value specifies the send rate of voice or fax
                                          					 compression to its associated call leg for this call. |
| ConnectionId | Global
                                          					 call identifier for this gateway call. |
| ConnectTime | Time, in
                                          					 milliseconds (ms), at which the call was connected. |
| Consecutive-packets-lost Events | Total
                                          					 number of consecutive (two or more) packet-loss events. |
| Corrected
                                          					 packet-loss Events | Total
                                          					 number of packet-loss events that were corrected using the RFC 2198 method. |
| Dial-Peer | Tag of
                                          					 the dial peer sending this call. |
| DisconnectCause | Cause
                                          					 code for the reason this call was disconnected. |
| DisconnectText | Descriptive text explaining the reason for the disconnect. |
| DisconnectTime | Time, in
                                          					 ms, when this call was disconnected. |
| EchoCancellerMaxReflector=64 | The
                                          					 location of the largest reflector, in ms. The reflector size does not exceed
                                          					 the configured echo path capacity. For example, if 32 ms is configured, the
                                          					 reflector does not report beyond 32 ms. |
| ERLLevel | Current
                                          					 Echo Return Loss (ERL) level for this call. |
| FaxTxDuration | Duration
                                          					 of fax transmission from this peer to the voice gateway for this call. You can
                                          					 derive the Fax Utilization Rate by dividing the FaxTxDuration value by the
                                          					 TxDuration value. |
| FaxRelayJitterBufOverFlow | Count of
                                          					 number of network jitter buffer overflows (number of packets). These packets
                                          					 are equivalent to lost packets. |
| FaxRelayMaxJitterBufDepth | Maximum
                                          					 depth of jitter buffer (in ms). |
| FaxRelayHSmodulation | Most
                                          					 recent high-speed modulation used. |
| FaxRelayNumberOfPages | Number of
                                          					 pages transmitted. |
| GapFillWithInterpolation | Duration
                                          					 of a voice signal played out with a signal synthesized from parameters, or
                                          					 samples of data preceding and following in time because voice data was lost or
                                          					 not received in time from the voice gateway for this call. |
| GapFillWithRedundancy | Duration
                                          					 of a voice signal played out with a signal synthesized from available
                                          					 redundancy parameters because voice data was lost or not received in time from
                                          					 the voice gateway for this call. |
| GapFillWithPrediction | Duration
                                          					 of the voice signal played out with signal synthesized from parameters, or
                                          					 samples of data preceding in time, because voice data was lost or not received
                                          					 in time from the voice gateway for this call. Examples of such pullout are
                                          					 frame-eraser and frame-concealment strategies in G.729 and G.723.1 compression
                                          					 algorithms. |
| GapFillWithSilence | Duration
                                          					 of a voice signal replaced with silence because voice data was lost or not
                                          					 received in time for this call. |
| GENERIC | Generic
                                          					 or common parameters, that is, parameters that are common for VoIP and
                                          					 telephony call legs. |
| GwReceivedCalledNumber, GwReceivedCalledOctet3, GwReceivedCallingNumber,
                                          					 GwReceivedCallingOctet3, GwReceivedCallingOctet3a | Call
                                          					 information received at the gateway. |
| H323
                                          					 call-legs | Total
                                          					 H.323 call legs for which call records are available. |
| HiWaterPlayoutDelay | High-water-mark Voice Playout FIFO Delay during this call. |
| ImgPages | The fax
                                          					 pages that have been processed. |
| Incoming
                                          					 ConnectionId | The
                                          					 incoming_GUID. It can be different with ConnectionId (GUID) when there is a
                                          					 long_pound or blast_call feature involved. In those cases, incoming_GUID is
                                          					 unique for all the subcalls that have been generated, and GUID is different for
                                          					 each subcall. |
| Index | Dial peer
                                          					 identification number. |
| InfoActivity | Active
                                          					 information transfer activity state for this call. |
| InfoType | Information type for this call; for example, voice or fax. |
| InSignalLevel | Active
                                          					 input signal level from the telephony interface used by this call. |
| Last
                                          					 Buffer Drain/Fill Event | Elapsed
                                          					 time since the last jitter buffer drain or fill event, in seconds. |
| Local UUID | Unique
                                          					 identifier generated from the originating user agent. |
| LogicalIfIndex | Index
                                          					 number of the logical interface for this call. |
| LoWaterPlayoutDelay | Low-water-mark Voice Playout FIFO Delay during this call. |
| LowerIFName | Physical
                                          					 lower interface information. Appears only if the medium is ATM, Frame Relay
                                          					 (FR), or High-Level Data Link Control (HDLC). |
| Media | Medium
                                          					 over which the call is carried. If the call is carried over the (telephone)
                                          					 access side, the entry is TELE. If the call is carried over the voice network
                                          					 side, the entry is either ATM, FR, or HDLC. |
| Modem
                                          					 passthrough signaling method in use | Indicates
                                          					 that this is a modem pass-through call and that named signaling events
                                          					 (NSEs)--a Cisco-proprietary version of named telephone events in RFC 2833--are
                                          					 used for signaling codec upspeed. The upspeed method is the method used to
                                          					 dynamically change the codec type and speed to meet network conditions. This
                                          					 means that you might move to a faster codec when you have both voice and data
                                          					 calls and then slow down when there is only voice traffic. |
| NoiseLevel | Active
                                          					 noise level for this call. |
| OnTimeRvPlayout | Duration
                                          					 of voice playout from data received on time for this call. Derive the Total
                                          					 Voice Playout Duration for Active Voice by adding the OnTimeRvPlayout value to
                                          					 the GapFill values. |
| OriginalCallingNumber, OriginalCalling Octet, OriginalCalledNumber,
                                          					 OriginalCalledOctet, OriginalRedirectCalledNumber, OriginalRedirectCalledOctet | Original
                                          					 call information regarding calling, called, and redirect numbers, as well as
                                          					 octet-3s. Octet-3s are information elements (IEs) of Q.931 that include type of
                                          					 number, numbering plan indicator, presentation indicator, and redirect reason
                                          					 information. |
| OutSignalLevel | Active
                                          					 output signal level to the telephony interface used by this call. |
| PeerAddress | Destination pattern or number associated with this peer. |
| PeerId | ID value
                                          					 of the peer table entry to which this call was made. |
| PeerIfIndex | Voice
                                          					 port index number for this peer. For ISDN media, this would be the index number
                                          					 of the B channel used for this call. |
| PeerSubAddress | Subaddress when this call is connected. |
| Percent
                                          					 Packet Loss | Total
                                          					 percent packet loss. |
| Port | Identification of the voice port carrying the call. |
| ReceiveBytes | Number of
                                          					 bytes received by the peer during this call. |
| ReceiveDelay | Average
                                          					 Playout FIFO Delay plus the Decoder Delay during this voice call. |
| ReceivePackets | Number of
                                          					 packets received by this peer during this call. |
| ReleaseSource | Number
                                          					 value of the release source. |
| RemoteIPAddress | Remote
                                          					 system IP address for the VoIP call. |
| RemoteUDPPort | Remote
                                          					 system User Datagram Protocol (UDP) listener port to which voice packets are
                                          					 sent. |
| Remote
                                          					 UUID | Unique
                                          					 identifier generated from the terminating user agent. |
| RoundTripDelay | Voice
                                          					 packet round-trip delay between the local and remote systems on the IP backbone
                                          					 for this call. |
| SelectedQoS | Selected
                                          					 Resource Reservation Protocol (RSVP) quality of service (QoS) for this call. |
| SessionProtocol | Session
                                          					 protocol used for an Internet call between the local and remote routers through
                                          					 the IP backbone. |
| SessionTarget | Session
                                          					 target of the peer used for this call. |
| SetupTime | Value of
                                          					 the system UpTime, in ms, when the call associated with this entry was started. |
| SignalingType | Signaling
                                          					 type for this call; for example, channel-associated signaling (CAS) or
                                          					 common-channel signaling (CCS). |
| SIP
                                          					 call-legs | Total SIP
                                          					 call legs for which call records are available. |
| Telephony
                                          					 call-legs | Total
                                          					 telephony call legs for which call records are available. |
| Time
                                          					 between Buffer Drain/Fills | Minimum
                                          					 and maximum durations between jitter buffer drain or fill events, in seconds. |
| TranslatedCallingNumber, TranslatedCallingOctet, TranslatedCalledNumber,
                                          					 TranslatedCalledOctet, TranslatedRedirectCalled Number,
                                          					 TranslatedRedirectCalledOctet | Translated call information. |
| TransmitBytes | Number of
                                          					 bytes sent by this peer during this call. |
| TransmitPackets | Number of
                                          					 packets sent by this peer during this call. |
| TxDuration | The
                                          					 length of the call. Appears only if the medium is TELE. |
| VAD | Whether
                                          					 voice activation detection (VAD) was enabled for this call. |
| VoiceTxDuration | Duration
                                          					 of voice transmission from this peer to the voice gateway for this call. Derive
                                          					 the Voice Utilization Rate by dividing the VoiceTxDuration value by the
                                          					 TxDuration value. |

| Field | Description |
|---|---|
| FaxRelayDirection | Direction
                                          					 of fax relay. |
| FaxRelayEcmStatus | Fax relay
                                          					 error correction mode status. |
| FaxRelayEncapProtocol | Fax relay
                                          					 encapsulation protocol. |
| FaxRelayFaxSuccess | Fax relay
                                          					 success. |
| FaxRelayInitHSmodulation | Fax relay
                                          					 initial high speed modulation. |
| FaxRelayMostRecentHSmodulation | Fax relay
                                          					 most recent high speed modulation. |
| FaxRelayNsfCountryCode | Fax relay
                                          					 Nonstandard Facilities (NSF) country code. |
| FaxRelayNsfManufCode | Fax relay
                                          					 NSF manufacturers code. |
| FaxRelayPktLossConceal | Fax relay
                                          					 packet loss conceal. |

| Command | Description |
|---|---|
| dial-control-mib | Specifies attributes for the call history table. |
| show call active fax | Displays call information for fax transmissions that are in progress. |
| show call active voice | Displays call information for voice calls that are in progress. |
| show call history voice | Displays the call history table for voice calls. |
| show dial-peer voice | Displays configuration information for dial peers. |
| show num-exp | Displays how the number expansions are configured in VoIP. |
| show voice port | Displays configuration information about a specific voice port. |

| brief | (Optional) Displays a truncated version of the call history table. |
|---|---|
| id identifier | (Optional) Displays only the call with the specified identifier . The range is from 1 to FFFF. |
| compact | (Optional) Displays a compact version of the call history table. |
| duration | (Optional) Displays the call history for the specified time duration. |
| less | Displays the call history for shorter duration calls. |
| more | Displays the call history for longer duration calls. |
| seconds | Time, in seconds. The range is from 1 to 2147483647. |
| last number | (Optional) Displays the last calls connected, where the number of calls that appear is defined by the number argument . The range is from 1 to 100 . |

| Release | Modification |
|---|---|
| 12.4(15)T | This command was introduced. |

| Field | Description |
|---|---|
| CallDuration | Length of the call, in hours, minutes, and seconds, hh:mm:ss. |
| CallOrigin | Call origin: not answer or originate. |
| ChargedUnits | Total number of charging units that apply to this peer since system startup. The unit of measure for this field is hundredths
                                          of second. |
| CodecBytes | Payload size, in bytes, for the codec used. |
| CoderTypeRate | Negotiated coder rate. This value specifies the send rate of voice or fax compression to its associated call leg for this
                                          call. |
| ConnectionId | Global call identifier for this gateway call. |
| ConnectTime | Time, in ms, during which the call was connected. |
| GapFillWithInterpolation | Duration, in ms, of a voice signal played out with a signal synthesized from parameters, or samples of data preceding and
                                          following in time because voice data was lost or not received in time from the voice gateway for this call. |
| GapFillWithRedundancy | Duration, in ms, of a voice signal played out with a signal synthesized from available redundancy parameters because voice
                                          data was lost or not received in time from the voice gateway for this call. |
| GapFillWithPrediction | Duration, in ms, of the voice signal played out with a signal synthesized from parameters, or samples of data preceding in
                                          time, because voice data was lost or not received in time from the voice gateway for this call. Examples of such pullout are
                                          frame-eraser and frame-concealment strategies in G.729 and G.723.1 compression algorithms. |
| GapFillWithSilence | Duration, in ms, of a voice signal replaced with silence because voice data was lost or not received in time for this call. |
| GENERIC | Generic or common parameters; that is, parameters that are common for VoIP and telephony call legs. |
| H323 call-legs | Total H.323 call legs for which call records are available. |
| HiWaterPlayoutDelay | High-water-mark voice playout first in first out (FIFO) Delay during this call, in ms. |
| Index | Dial peer identification number. |
| InfoType | Information type for this call; for example, voice, speech, or fax. |
| LogicalIfIndex | Index number of the logical interface for this call. |
| LoWaterPlayoutDelay | Low-water-mark voice playout FIFO delay during this call, in ms. |
| OnTimeRvPlayout | Duration of voice playout from data received on time for this call. Derive the Total Voice Playout Duration for Active Voice
                                          by adding the OnTimeRvPlayout value to the GapFill values. |
| PeerAddress | Destination pattern or number associated with this peer. |
| PeerId | ID value of the peer table entry to which this call was made. |
| PeerIfIndex | Voice port index number for this peer. For ISDN media, this would be the index number of the B channel used for this call. |
| PeerSubAddress | Subaddress when this call is connected. |
| ReceiveBytes | Number of bytes received by the peer during this call. |
| ReceiveDelay | Average playout FIFO delay plus the decoder delay during this voice call, in ms. |
| ReceivePackets | Number of packets received by this peer during this call. |
| ReleaseSource | Number value of the release source. |
| RemoteIPAddress | Remote system IP address for the VoIP call. |
| RemoteUDPPort | Remote system User Datagram Protocol (UDP) listener port to which voice packets are sent. |
| RoundTripDelay | Voice packet round-trip delay, in ms, between the local and remote systems on the IP backbone for this call. |
| SelectedQoS | Selected Resource Reservation Protocol (RSVP) quality of service (QoS) for this call. |
| SessionProtocol | Session protocol used for an Internet call between the local and remote routers through the IP backbone. |
| SessionTarget | Session target of the peer used for this call. |
| SetupTime | Value of the system UpTime, in ms, when the call associated with this entry was started. |
| SIP call-legs | Total Session Initiation Protocol (SIP) call legs for which call records are available. |
| Telephony call-legs | Total telephony call legs for which call records are available. |
| TransmitBytes | Number of bytes sent by this peer during this call. |
| TransmitPackets | Number of packets sent by this peer during this call. |
| VAD | Whether voice activation detection (VAD) was enabled for this call. |

| Command | Description |
|---|---|
| dial-control-mib | Sets the maximum number of calls contained in the table. |
| show call active media | Displays call information for media calls in progress. |

| connected | Displays call statistics for connected calls. |
|---|---|
| table | (Optional) Displays call statistics for connected calls in tabular format. |
| cps | Displays call statistics in calls handled per second format. |
| details | Displays call statistics in calls handled per second format including call-leg rate. |
| table | Displays call statistics in calls handled per second format including call-leg rate in tabular format |
| short-duration | Displays the call statistics for short-duration calls. By default, any call with total duration less than 5 seconds is considered
                                       as a short duration call. You can change the default value using Management Information Base (MIB). |

| Release | Modification |
|---|---|
| Cisco IOS XE Release 3.8 | This command was introduced. |

| brief | (Optional) Displays a truncated version of video call history information. |
|---|---|
| id identifier | (Optional) Displays only the video call history with the specified identifier. Range is a hexadecimal value from 1 to FFFF. |
| compact | (Optional) Displays a compact version of video call history information. |
| duration | (Optional) Displays the call history for the specified time duration. |
| less | Displays the call history for shorter duration calls. |
| more | Displays the call history for longer duration calls. |
| seconds | Time, in seconds. The range is from 1 to 2147483647. |
| last number | (Optional) Displays the last calls connected, where the number of calls that appear is defined by the number argument . The range is from 1 to 100 . |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release 12.4(9)T. |
| 12.4(16); 12.4(15)T | Cisco Unified CME 4.0 | This command was modified. The Port and BearerChannel display fields were added to the TELE call leg record of the command
                                          output. |

| Field | Description |
|---|---|
| callID | Unique identifier for the call leg. |
| A/O | Call leg was an answer (ANS) or an originator (ORG). |
| FAX | Fax number for the call leg. |
| T<sec> | Duration in seconds. |
| Codec | Codec used for this call leg. |
| type | Call type for this call leg. |
| Peer Address | Called or calling number of the remote peer. |
| IP R<ip>:<udp> | IP address and port number |
| Total call-legs | Total number of call legs for this call. |

| Command | Description |
|---|---|
| show call active video | Displays call information for SCCP video calls in progress. |

| Release | Modification |
|---|---|
| 12.0(5)XK | This command was introduced on the Cisco MC3810. |
| 12.0(7)T | This command was integrated into Cisco IOS Release 12.0(7)T. |

| brief | (Optional) Displays a truncated version of the call history table. |
|---|---|
| id identifier | (Optional) Displays only the call with the specified identifier. Range is from 1 to FFFF. |
| compact | (Optional) Displays a compact version of the call history table. |
| dest-route-string tag | (Optional) Displays only the call with the specified destination route tag value. The range is from 1 to 10000. |
| duration seconds | (Optional) Displays history information for calls that are longer or shorter than the value of the specified seconds argument. The arguments and keywords are as follows: less --Displays calls shorter than the seconds value. more --Displays calls longer than the seconds value. seconds --Elapsed time, in seconds. Range is from 1 to 2147483647. |
| last number | (Optional) Displays the last calls connected, where the number of calls that appear is defined by the number argument . Range is from 1 to 100 . |
| redirect | (Optional) Displays information about calls that were redirected using Release-to-Pivot (RTPvt) or Two B-Channel Transfer
                                          (TBCT). The keywords are as follows: rtpvt --Displays information about RTPvt calls. tbct --Displays information about TBCT calls. |
| stats | (Optional) Displays information about digital signal processing (DSP) voice quality metrics. |

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 3600 series. |
| 12.0(3)XG | Support was added for Voice over Frame Relay (VoFR) on the Cisco 2600 series and Cisco 3600 series. |
| 12.0(4)XJ | This command was modified for store-and-forward fax. |
| 12.0(4)T | The brief keyword was added, and the command was implemented on the Cisco 7200 series. |
| 12.0(5)XK | This command was implemented on the Cisco MC3810. |
| 12.0(7)XK | The brief keyword was implemented on the Cisco MC3810. |
| 12.0(7)T | This command was integrated into Cisco IOS Release 12.0(7)T. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.1(5)XM | This command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XA | The output of this command was modified to indicate whether a specified call has been established using Annex E. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T. Support was not included for the Cisco AS5350, Cisco AS5400,
                                          Cisco AS5800, and Cisco AS5850. |
| 12.2(11)T | Support was added for Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850. |
| 12.2(13)T | The ReleaseSource field was added to the Field Description table, and the record keyword was deleted from the command name. |
| 12.3(1) | The redirect keyword was added. |
| 12.4(2)T | The LocalHostname display field was added to the VoIP call leg record. |
| 12.4(11)XW | The stats keyword was added. |
| 12.4(15)T | The Port and BearerChannel display fields were added to the TELE call leg record of the command output. |
| 12.4(16) | The Port and BearerChannel display fields were added to the TELE call leg record of the command output. |
| 12.4(22)T | Command output was updated to show IPv6 information. |
| 15.3(3)M | This command was modified. The dest-route-string keyword was added. |
| Cisco IOS XE Release 3.10S | This command was integrated into Cisco IOS XE Release 3.10S. |

| Field | Description |
|---|---|
| index | Index number of the record in the history file. |
| xfr | Whether TBCT or TBCT with notify has been invoked. |
| status | Status of the redirect request. |
| start_time | Time, in hours, minutes, and seconds when the redirected call began. |
| ctrl name | Name of the T1 controller where the call originated. |
| tag | Call tag number that identifies the call. |
| Number of call-legs redirected using tbct with notify | Total number of call legs that were redirected using TBCT with notify. |

| Command | Description |
|---|---|
| dial-control-mib | Set the maximum number of calls contained in the table. |
| show call active fax | Displays call information for fax transmissions that are in progress. |
| show call active voice | Displays call information for voice calls that are in progress. |
| show call history fax | Displays the call history table for fax transmissions. |
| show dial-peer voice | Displays configuration information for dial peers. |
| show num-exp | Displays how the number expansions are configured in VoIP. |
| show voice port | Displays configuration information about a specific voice port. |

| Cisco IOS Release | Modification |
|---|---|
| 15.3(1)T | This command was introduced. |

| Command | Description |
|---|---|
| show call history stats connected | Display connected or active call histogram for 3 periods (Seconds, Minutes, and Hours). |
| show call history stats connected table | Displays concurrent call table for max and average value of active calls per second. |

| language | (Optional) Two-character prefix configured with the call language voice command in global configuration mode, either for a prefix for a built-in language or one that you have defined; for example,
                                          "en" for English or "ru" for Russian. |
|---|---|
| summary | (Optional) Summary of all the languages configured and the URLs for the TCL modules other than built-in languages. |

| Release | Modification |
|---|---|
| 12.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| call language voice | Configures a TCL module. |
| call language voice load | Loads or reloads a TCL module from the configured URL location. |
| debug voip ivr | Specifies the type of VoIP IVR debug output that you want to view. |
| show call application voice | Shows and describes applications. |

| active | Statistics or event logs for active call legs. |
|---|---|
| history | Statistics or event logs for terminated call legs. |
| summary | (Optional) A summary of each call leg. |
| last number | (Optional) Selected number of most recent call legs. Not available with active keyword. |
| leg-id leg-id | (Optional) A specific call leg. Output displays event logs or statistics for that call leg. |
| event-log | (Optional) Event logs for call legs. |
| info | (Optional) Statistics for call legs. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |

| Command | Description |
|---|---|
| call leg event-log | Enables event logging for voice, fax, and modem call legs. |
| call leg event-log dump ftp | Enables the voice gateway to write the contents of the call-leg event log buffer to an external file. |
| call leg event-log error-only | Restricts event logging to error events only for voice call legs. |
| call leg event-log max-buffer-size | Sets the maximum size of the event log buffer for each call leg. |
| call leg history event-log save-exception-only | Saves to history only event logs for call legs that had at least one error. |
| monitor call leg event-log | Displays the event log for an active call leg in real-time. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Field | Description |
|---|---|
| Session | Session Identifier. |
| Call | Call Leg identifier in hexadecimal. It must
                                          									match the Call ID from the show call leg active command. |
| n/f | Direction (Near End or Far End) of the voice
                                          									stream that was forked. |
| Destination (port address) | Destination for the forked packets. It consists of the
                                          									folllowing: RTP Port IP Address |

| call | Displays the active call monitor calls. |
|---|---|
| gcid | Displays the active global call ID information. |
| subscription | Displays the subscription information. |
| trace | Displays the trace information. |
| all | Displays all types of traces based on time. |
| event | Displays the event trace information. all --Displays all event traces. call --Displays event traces related to a call. connection --Displays the event traces related to a connection. |
| exec | Displays all critical execution traces. |
| server | Displays all session server up or down traces. |
| subscription | Displays all subscription traces. |
| trigger | Displays the entire trigger structure by index. |

| Release | Modification |
|---|---|
| 12.4(22)T | This command was introduced. |

| Field | Description |
|---|---|
| dn | Directory number. |
| number of call | Number of call instances. |
| instance | Contents of the call instance. |

| Field | Description |
|---|---|
| GCID | Global call ID. |
| CallIDs | Active call IDs. |

| Command | Description |
|---|---|
| callmonitor | Enables call monitoring messaging functionality on a SIP endpoint in a VoIP network. |

| detail | (Optional) Displays details about memory usage and names of tones used. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(15)T | This command was introduced. |
| 12.3(7)T | The detail keyword was added. |

| Field | Description |
|---|---|
| file(s) | Number of prompts in different queues. |
| file(s) - config’d | Maximum number of configured prompts that can be simultaneously available in memory. In the sample output, the value of 200
                                          in this field means that loading the 201st prompt results in the oldest prompts being removed. |
| file(s) -wait | Number of prompts in the wait queue that are not being used in any call and are ready to be deleted when there is no space
                                          for a new prompt. This field lists older prompts that can be deleted. |
| file(s) - active | Number of prompts that are being used in active calls. These prompts cannot be deleted. |
| file(s) - free | Number of prompts that can be loaded without deleting any prompt from the wait queue. This is the number of configured prompts
                                          (listed under config’d) minus the total number of prompts in the wait and active states. |
| file(s) - mc total | Total number of prompts in the wait and active states. |
| ms total | Number of media streams that are currently active. One media stream is used for playing INBOX prompts. A prompt is considered
                                          an INBOX prompt if its URL is either flash:, http:, ram:, or tftp:. |
| memory | Displays the memory used by prompts, in bytes. |
| memory - config’d | Maximum amount of memory configured to be available for prompts. |
| memory - wait | Total amount of memory used by prompts in the wait list. |
| memory - active | Total amount of memory used by prompts in the active list. |
| memory - free | Amount of available memory. This is the amount of configured prompts (listed under config’d) memory minus the total amount
                                          of memory used by the prompts in the wait and active lists. |
| memory - mc total | Total amount of memory used by prompts in the wait and active lists. |
| Prompt load counts | Number of successful attempts to load a prompt on the first try and on the second try, and the number of attempts to load
                                          a prompt that failed. |
| mcDynamic | Number of dynamic element queues that are active. A dynamic element queue is a list of prompts that are played together. |
| mcReader | Number of mcReaders that are active. An mcReader is used for playing one mcDynamic queue of prompts. An mcReader is used
                                          only if the mcDynamic contains prompts that are associated with one of the following types of URL: flash:, http:, ram:, or
                                          tftp:. |
| Number of prompts playing | Number of prompts that are currently playing. |
| Number of start delays | Number of times that prompts failed to start and have subsequently restarted. |
| MCs in the ivr MC sharing table | The fields below this line of text refer to each media content (prompt) currently cached in memory. In the sample output,
                                          the only cached prompt is the built-in default prompt named "NoPrompt." |
| Media Content | Name of the prompt, which is derived from the audio file URL (the characters after the last "/" in the URL). The address
                                          in parentheses is the memory location of the prompt. |
| URL | Location of the file for the prompt that is playing. In the case of the default prompt, NoPrompt, no URL is given. |
| cid | Call identification number of the call that initiated the loading of the prompt. |
| status | Status of the media content. The following values are possible: MC_NOT_READY--Initial status for media content. When the media content is successfully loaded, the status will change to
                                                MC_READY. MC_READY--Media content is loaded into memory and ready for use. MC_LOAD_FAIL--Media content failed to load. |
| size | Size of the media content, in bytes. |
| coding | Type of encoding used by the media content. |
| refCount=0 | Number of calls to which this media content is currently being streamed. |

| ds0 | (Optional) Specifies the voice digital signal level zero (DS0) resource statistics information. |
|---|---|
| dsp | (Optional) Specifies the voice digital signal processor (DSP) resource statistics information. |

| Release | Modification |
|---|---|
| 12.0(5)T | This command was introduced. |
| 12.1(5)XM2 | This command was integrated into Cisco IOS Release 12.1(5)XM2 |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(2)XB1 | This command was integrated into Cisco IOS Release into 12.2(2)XB1. |
| 12.2(8)T | This command was modified. Support for the Cisco AS5300,Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 series
                                          routers is not included in this release. |
| 12.4(22)T | This command was modified. The ds0 and dsp keywords were added. |

| Statistic | Definition |
|---|---|
| Total channels | Number of channels physically configured for the resource. |
| Inuse channels | Number of addressable channels that are in use. This value includes all channels that either have active calls or have been
                                          reserved for testing. |
| Disabled channels | Number of addressable channels that are physically down or that have been disabled administratively with the shutdown or busyout command. |
| Pending channels | Number of addressable channels that are pending in loadware download. |
| Free channels | Number of addressable channels that are free. |
| Addressable channels | Number of channels that can be used for a specific type of dialup service, such as H.323, which includes all the DS0 resources
                                          that have been associated with a voice plain old telephone service (POTS) dial plan profile. |

| Command | Description |
|---|---|
| resource threshold | Configures a gateway to report H.323 resource availability to the gatekeeper of the gateway. |
| show call resource voice threshold | Displays the threshold configuration settings and status for an H.323 gateway. |

| ds0 | (Optional) Specifies the voice digital signal level zero (DS0) resource statistics information. |
|---|---|
| dsp | (Optional) Specifies the voice digital signal processor (DSP) resource statistics information. |

| Release | Modification |
|---|---|
| 12.0(5)T | This command was introduced. |
| 12.1(5)XM2 | This command was integrated into Cisco IOS Release 12.1(5)XM2 |
| 12.2(2)XB1 | This command was integrated into Cisco IOS Release into 12.2(2)XB1. |
| 12.4(22)T | This command was modified. The ds0 and dsp keywords were added. |

| Field | Description |
|---|---|
| High Water Mark | Resource-utilization level that triggers a message indicating that H.323 resource use is high. The range is 1 to 100. A value
                                          of 100 indicates that the resource is unavailable.The default is 90. |
| Low Water Mark | Resource-utilization level that triggers a message indicating that H.323 resource use has dropped below the high-usage level.
                                          The range is 1 to 100. The default is 90. |

| Command | Description |
|---|---|
| resource threshold | Configures a gateway to report H.323 resource availability to the gatekeeper of the gateway. |
| show call resource voice stats | Displays resource statistics for an H.323 gateway. |

| Release | Modification |
|---|---|
| 12.1(3)XI1 | This command was introduced on the Cisco 2600 series, Cisco 3600 series, Cisco 7200, Cisco MC3810, Cisco AS5300, and Cisco
                                          AS5800. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | Support for the Cisco AS5300,Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command is supported on the Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850 in this release. |

| Field | Description |
|---|---|
| Overture Synchronization is ON | Indicates whether RSVP synchronization is enabled. |
| Reservation Timer is set to xx seconds | Number of seconds for which the RSVP reservation timer is configured. |

| Command | Description |
|---|---|
| call rsvp - sync | Enables synchronization between RSVP and the H.323 voice signaling protocol. |
| call rsvp - sync resv - timer | Sets the timer for RSVP reservation setup. |
| debug call rsvp - sync events | Displays the events that occur during RSVP synchronization. |
| show call rsvp - sync stats | Displays statistics for calls that attempted RSVP reservation. |

| Release | Modification |
|---|---|
| 12.1(3)XI1 | This command was introduced. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Field | Description |
|---|---|
| Number of calls for which QoS was initiated | Number of calls for which RSVP setup was attempted. |
| Number of calls for which QoS was torn down | Number of calls for which an established RSVP reservation was released. |
| Number of calls for which Reservation Success was notified | Number of calls for which an RSVP reservation was successfully established. |
| Total Number of PATH Errors encountered | Number of path errors that occurred. |
| Total Number of RESV Errors encountered | Number of reservation errors that occurred. |
| Total Number of Reservation Timeouts encountered | Number of calls in which the reservation setup was not complete before the reservation timer expired. |

| Command | Description |
|---|---|
| call rsvp - sync | Enables synchronization between RSVP and the H.323 voice signaling protocol. |
| call rsvp - sync resv - timer | Sets the timer for RSVP reservation setup. |
| debug call rsvp - sync events | Displays the events that occur during RSVP synchronization. |
| show call rsvp - sync conf | Displays the RSVP synchronization configuration. |

| dial-peer | (Optional) Displays configuration information for a dial peer. |
|---|---|
| tag | (Optional) Specifies the dial peer identifying number. Range is from 1 to 2147483647. |

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. This command was not supported on the Cisco AS5300, Cisco AS5350,
                                          and Cisco AS5400 in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)XM | This command was implemented on the Cisco 1750 and Cisco 1751. This command was not supported on any other platforms in this
                                          release. |
| 12.2(8)T | This command was implemented on the Cisco 7200 series. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco
                                          AS5850 was not included in this release. |
| 12.2(11)T | Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 was added in this release. |
| 15.1(3)T | This command was modified. The output fields of the command were modified to include the output at the dial peer level. |

| Field | Description |
|---|---|
| Call Spiking | Current enabled state of call spiking. |
| Call Spiking | Details if the call spiking limit has been triggered. |
| total call count in sliding window | Number of calls during the spiking interval. |

| Field | Description |
|---|---|
| TAG | Dial peer tag. |
| CONFIG | Displays if the call spike command has been configured. |
| SPIKED | Details if the call spiking limit has been triggered. |
| TOTAL REJECTED CALLS | Displays the number of calls rejected due to a call spike in the dial peer. |
| REJECTED CALLS | Displays the number of calls rejected when the call spike was triggered until the call spike control was released. |

| Command | Description |
|---|---|
| call spike | Configures the limit for the number of incoming calls in a short period of time. |

| config | Displays the current threshold configuration. |
|---|---|
| status | Displays the status of all configured triggers and whether or not the CPU is available. |
| unavailable | (Optional) Displays the status for all unavailable resources. |
| stats | Displays statistics for API calls; that is, the resource-based measurement. |

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. This command is not supported on the Cisco AS5300, Cisco AS5350,
                                          and Cisco AS5400 platforms in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)XM | This command was implemented on the Cisco 1750 and Cisco 1751. This command is not supported on any other platforms in this
                                          release. |
| 12.2(8)T | This command was implemented on the Cisco 7200 series. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco
                                          AS5850 is not included in this release. |
| 12.2(11)T | This command was implemented on the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850. |
| 15.2(2)T | This command was modified. The output was modified to display the configured bandwidth threshold, bandwidth availability,
                                          and call admission control statistics. |

| Field | Description |
|---|---|
| CPU_AVG interval | Interval of configured trigger CPU_AVG. |
| Memory interval | Interval of configured trigger Memory. |
| IF | Interface type and number. |
| Type | Type of resource. |
| Value | Value of a call that is to be matched against low and high thresholds. |
| Low | Low threshold. |
| High | High threshold. |
| Enable | Shows if busyout and the call treatment command are enabled. |

| Command | Description |
|---|---|
| call threshold | Enables a resource and defines associated parameters. |
| call threshold poll-interval | Enables a polling interval threshold for CPU or memory. |
| clear call threshold | Clears enabled triggers and their associated parameters. |

| config | Displays the call treatment configuration. |
|---|---|
| stats | Displays statistics for handling the calls on the basis of resource availability. |

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. This command was not supported on the Cisco AS5300, Cisco AS5350,
                                          and Cisco AS5400 in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(4)XM | This command was implemented on the Cisco 1750 and Cisco 1751. This command was not supported on any other platforms in this
                                          release. |
| 12.2(8)T | This command was implemented on the Cisco 7200 series. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco
                                          AS5850 is not included in this release. |
| 12.2(11)T | This command is supported on the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 in this release. |

| Field | Description |
|---|---|
| Call treatment is: | State of call treatment, either ON or OFF. |
| Call treatment action is: | Action trigger assigned for call treatment. |
| Call treatment disconnect cause is: | Reason for disconnect. |
| Call treatment ISDN reject cause-code is: | Reject code number assigned. |

| Field | Description |
|---|---|
| Total Calls by call treatment: | Number of calls received and treated. |
| Calls accepted by call treatment: | Calls that passed treatment parameters. |
| Calls rejected by call treatment: | Calls that failed treatment parameters. |
| cpu-5sec | Number of calls rejected for failing the cpu-5sec parameter. |
| cpu-avg | Number of calls rejected for failing the cpu-avg parameter. |
| total-mem | Number of calls rejected for failing the total-mem parameter. |
| io-mem | Number of calls rejected for failing the io-mem parameter. |
| proc-mem | Number of calls rejected for failing the proc-mem parameter. |
| total-calls | Number of calls rejected for failing the total-calls parameter. |

| Command | Description |
|---|---|
| call treatment on | Enables call treatment to process calls when local resources are unavailable. |
| call treatment action | Configures the action that the router takes when local resources are unavailable. |
| call treatment cause-code | Specifies the reason for the disconnection to the caller when local resources are unavailable. |
| call treatment isdn-reject | Specifies the rejection cause-code for ISDN calls when local resources are unavailable. |
| clear call treatment stats | Clears the call-treatment statistics. |

| static | Descriptors provisioned on the border element. |
|---|---|
| dynamic | Dynamically learned descriptors. |
| all | Both static and dynamic descriptors. |

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Command | Description |
|---|---|
| show call-router active | Displays active call information for a voice call in progress. |
| show call-router history | Displays the VoIP call-history table. |
| show call-router status | Displays the Annex G BE status. |
| show dial-peer voice | Displays configuration information for dial peers. |
| show num-exp | Displays how the number expansions are configured in VoIP. |
| show voice port | Displays configuration information about a specific voice port. |

| neighbors | (Optional) Displays the neighbor border element status. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T and modified to add the neighbors keyword. |

| Field | Description |
|---|---|
| Border Element ID Tag | Identifier for the border element. |
| Border Element State | Indicates if the border element is running. |
| Border Element Local IP | Local IP address of the border element. |
| Advertise Policy | Type of descriptors that the border element advertises to its neighbors. Default is static . Other values are dynamic and all . |
| Hopcount Value | Maximum number of border element hops through which an address resolution request can be forwarded. Default is 7. |
| Descriptor TTL | Time-to-live value, or the amount of time, in seconds, for which a route from a neighbor is considered valid. Range is from
                                          1 to 2147483647. Default is 1800 (30 minutes). |
| Access Policy | Requires that a neighbor be explicitly configured for requests to be accepted. |
| Local Neighbor ID | Domain name reported in service relationships. |
| Service Relationship Status | Service relationship between two border elements is active. |
| Inbound Service Relationship | Inbound time-to-Live (TTL) value in number of seconds. Range is from 1 to 4294967295. |
| Outbound Service Relationship | Specifies the amount of time, in seconds, to establish the outbound relationship. Range is from 1 to 65535. |
| Retry interval | Retry value between delivery attempts, in number of seconds. Range is from 1 to 3600. |

| Command | Description |
|---|---|
| advertise | Controls the type of descriptors that the border element advertises to its neighbors. |
| call - router | Enables the Annex G border element configuration commands. |
| hopcount | Specifies the maximum number of border element hops through which an address resolution request can be forwarded. |
| local | Defines the local domain, including the IP address and port border elements that the border element should use for interacting
                                          with remote border elements. |
| shutdown | Shuts down the Annex G border element. |
| ttl | Sets the expiration timer for advertisements. |

| backhaul | (Optional) Displays information about the backhaul link. |
|---|---|
| config-download | (Optional) Displays information about the status of Media Gateway Control
                                          						Protocol (MGCP) and Skinny Client Control Protocol (SCCP) configuration
                                          						download. |
| fallback-mgcp | (Optional) Displays the status of the MGCP gateway fallback feature. |
| hosts | (Optional) Displays a list of each configured Cisco CallManager server in the
                                          						network, together with its operational status and host IP address. |
| music-on-hold | (Optional) Displays information about all the multicast music-on-hold (MOH)
                                          						sessions in the gateway at any given point in time. |
| redundancy | (Optional) Displays failover mode and status information for hosts, including
                                          						the redundant link port, failover interval, keepalive interval, MGCP traffic
                                          						time, switchover time, and switchback mode. |
| download-tones c1 \| c2 | (Optional) Displays custom tones downloaded to the gateway. The custom tone
                                          						value of c1 or c2 specifies which tone information to display. |

| Release | Modification |
|---|---|
| 12.1(3)T | This
                                          						command was introduced on the Cisco CallManager Version 3.0 and Cisco VG200. |
| 12.2(2)XA | This
                                          						command was implemented on the Cisco 2600 series and Cisco 3600 series. |
| 12.2(2)XN | This
                                          						command was modified to provide enhanced MGCP voice gateway interoperability to
                                          						Cisco CallManager Version 3.1 for the Cisco 2600 series, Cisco 3600 series, and
                                          						Cisco VG200. |
| 12.2(11)T | This
                                          						command was integrated into Cisco IOS Release 12.2(11) and the Cisco
                                          						CallManager Version 3.2. It was implemented on the Cisco IAD2420 series. |
| 12.2(15)ZJ | The
                                          						download-tones [ c1 \| c2 ] keywords were added for the following platforms:
                                          						Cisco 2610XM, Cisco 2611XM, Cisco 2620XM, Cisco 2621XM, Cisco 2650XM, Cisco
                                          						2651XM, Cisco 2691, Cisco 3640A, Cisco 3660, Cisco 3725, and Cisco 3745. |
| 12.3(4)T | The
                                          						keywords were integrated into Cisco IOS Release 12.3(4)T. |
| 12.3(14)T | New
                                          						output was added relating to SCCP autoconfiguration. |
| 12.4(15)XY | The
                                          						display output was modified to include the number of TFTP download failures
                                          						allowed. |

| Field | Description |
|---|---|
| Percent
                                          					 make | Pulse
                                          					 ratio in percentage of make. |
| DTMF low
                                          					 Amp. | Low
                                          					 frequency level. |
| high Amp. | High
                                          					 frequency level. |
| Pcm | Pulse
                                          					 Code Modulation (mu-law or a-law). |

| Field of
                                          					 Dual Tone | Description |
|---|---|
| DR | Direction
                                          					 to PSTN (0) or Packet Network (1). |
| NF | Number of
                                          					 Frequency (from 1 to 4). |
| FOF | Frequency
                                          					 of First component (in Hz). |
| FXS AOF | Amplitude
                                          					 of First component (from 1 to 65535 = +3 dBm0) for the foreign exchange station
                                          					 (FXS). |
| FXO AOF | Amplitude
                                          					 of First component (from 1 to 65535 = +3 dBm0) for the foreign exchange office
                                          					 (FXO). |
| E&M
                                          					 AOF | Amplitude
                                          					 of First component (from 1 to 65535 = +3 dBm0) for the recEive and transMit
                                          					 (E&M). |
| FXS AOS | Amplitude
                                          					 of Second component (from 1 to 65535 = +3 dBm0) for the FXS. |
| FXO AOS | Amplitude
                                          					 of Second component (from 1 to 65535 = +3 dBm0) for the FXO. |
| E&M
                                          					 AOS | Amplitude
                                          					 of Second component (from 1 to 65535 = +3 dBm0) for the E&M. |
| ONTF | On time;
                                          					 time the tone is generated (milliseconds) for the first frequency. |
| OFTF | Off time;
                                          					 silence time (milliseconds) for the first frequency. |
| ONTS | On time;
                                          					 time the tone is generated (milliseconds) for the second frequency. |
| OFTS | Off time;
                                          					 silence time (milliseconds) for the second frequency. |
| ONTT | On time;
                                          					 time the tone is generated (milliseconds) for the third frequency. |
| OFTT | Off time;
                                          					 silence time (milliseconds) for the third frequency. |
| ONT4 | On time;
                                          					 time the tone is generated (milliseconds) for the fourth frequency. |
| OFT4 | Off time;
                                          					 silence time (milliseconds) for the fourth frequency. |
| FOF2 | Frequency
                                          					 of First component for the second cadence. |
| FOS2 | Frequency
                                          					 of Second component for the second cadence. |
| FOF3 | Frequency
                                          					 of First component for the third cadence. |
| FOS3 | Frequency
                                          					 of Second component for the third cadence. |
| FOF4 | Frequency
                                          					 of First component for the fourth cadence. |
| FOS4 | Frequency
                                          					 of Second component for the fourth cadence. |
| FOT | Frequency
                                          					 of Third component (in Hertz). |
| FO4 | Frequency
                                          					 of Fourth component (in Hertz). |
| AOT | Amplitude
                                          					 of Third component (from 1 to 65535 = +3 dBm0). |
| AO4 | Amplitude
                                          					 of Fourth component (from 1 to 65535 = +3 dBm0). |
| RCT1 | Number of
                                          					 repeat for the first cadence. |
| RCT2 | Number of
                                          					 repeat for the second cadence. |
| RCT3 | Number of
                                          					 repeat for the third cadence. |
| RCT4 | Number of
                                          					 repeat for the fourth cadence. |

| Field of
                                          					 Sequence Tone | Description |
|---|---|
| DR | Direction
                                          					 to PSTN (0) or Packet Network (1). |
| NF | Number of
                                          					 Frequency (from 1 to 4). |
| F1C1 | Frequency
                                          					 1 of Cadence 1. |
| F2C1 | Frequency
                                          					 2 of Cadence 1. |
| AOF | Amplitude
                                          					 of First component (from 1 to 65535). |
| AOS | Amplitude
                                          					 of Second component (from 1 to 65535). |
| C1ONT | Cadence 1
                                          					 On Time. |
| C1OFT | Cadence 1
                                          					 Off Time. |
| C2ONT | Cadence 2
                                          					 On Time. |
| C2OFT | Cadence 2
                                          					 Off Time. |
| C3ONT | Cadence 3
                                          					 On Time. |
| C3OFT | Cadence 3
                                          					 Off Time. |
| C4ONT | Cadence 4
                                          					 On Time. |
| C4OFT | Cadence 4
                                          					 Off Time. |
| F1C2 | Frequency
                                          					 1 of Cadence 2. |
| F2C2 | Frequency
                                          					 2 of Cadence 2. |
| F1C3 | Frequency
                                          					 1 of Cadence 3. |
| F2C3 | Frequency
                                          					 2 of Cadence 3. |
| F1C4 | Frequency
                                          					 1 of Cadence 4. |
| F2C4 | Frequency
                                          					 2 of Cadence 4. |

| Field | Description |
|---|---|
| MGCP
                                          					 Domain Name (system) | System
                                          					 used in the Internet for translating domain names of network nodes into IP
                                          					 addresses. |
| Priority | Priority
                                          					 of the Cisco CallManager servers present in the network. Possible priorities
                                          					 are primary, first backup, and second backup. |
| Status | Current
                                          					 usage of the Cisco Unified Communications Manager server. Values are
                                          					 Registered, Idle, Backup Polling, and Undefined. |
| Host | Host IP
                                          					 address of the Cisco CallManager server. |
| Current
                                          					 active Call Manager | IP
                                          					 address of the active Cisco Communications Manager server. This field can be
                                          					 the IP address of any one of the following Cisco Communications Manager
                                          					 servers: Primary, First Backup, and Second Backup. |
| Backhaul/Redundant link port | Port that
                                          					 the Cisco CallManager server is to use. |
| Failover
                                          					 Interval | Maximum
                                          					 amount of time that can elapse without the gateway receiving messages from the
                                          					 currently active Cisco Call Manager before the gateway switches to the backup
                                          					 Cisco Call Manager. |
| Keepalive
                                          					 Interval | Interval
                                          					 following which, if the gateway has not received any messages from the
                                          					 currently active Cisco Communications Manager server within the specified
                                          					 amount of time, the gateway sends a keepalive message to the Cisco
                                          					 Communications Manager server to determine if it is operational. |
| Last
                                          					 keepalive sent | Time in
                                          					 hours (military format), minutes and seconds at which the last keepalive
                                          					 message was sent. |
| Last MGCP
                                          					 traffic time | Time in
                                          					 hours (military format), minutes and seconds at which the last MGCP traffic
                                          					 message was sent. |
| Switchback mode | Displays
                                          					 the switchback mode configuration that determines when the primary Cisco
                                          					 CallManager server is used if it becomes available again while a backup Cisco
                                          					 CallManager server is being used. Values
                                          					 that can appear in this field are Graceful, Immediate, Schedule - time, and Uptime-delay. |
| MGCP
                                          					 Fallback mode | Displays
                                          					 the MGCP fallback mode configuration. If "Not Selected" displays, then fallback
                                          					 is not configured. If "Enabled/OFF" displays, then fallback is configured but
                                          					 not in effect. If "Enabled/ON" displays, then fallback is configured and in
                                          					 effect. |
| Last MGCP
                                          					 Fallback start time | Start
                                          					 time stamp in hours (military format), minutes and seconds of the last
                                          					 fallback. |
| Lasts
                                          					 MGCP Fallback end time | End time
                                          					 stamp in hours (military format), minutes and seconds of the last fallback. |
| MGCP
                                          					 Download Tones | Displays
                                          					 if the customized tone download is enabled. |
| TFTP
                                          					 retry count to shut Ports | Number of
                                          					 TFTP download failures allowed before endpoints are shutdown. |

| Field | Description |
|---|---|
| Current
                                          					 state | Current
                                          					 configuration state. |
| Download
                                          					 Attempted | Number of
                                          					 times the gateway has tried to download the configuration file. The number of
                                          					 successes and failures is displayed. |
| Configuration Attempted | Number of
                                          					 times the gateway has tried to configure the gateway based on the configuration
                                          					 file. The number of successes and failures is displayed. |
| Managed
                                          					 endpoints | Number of
                                          					 SSCP-controlled endpoints (analog and BRI phones). |
| Endpoint
                                          					 downloads succeeded | Number of
                                          					 times the gateway has successfully downloaded the configuration files for
                                          					 SCCP-controlled endpoints. |
| Endpoint
                                          					 download attempts | Number of
                                          					 times the gateway has tried to download the configuration files for
                                          					 SCCP-controlled endpoints. |
| Endpoint
                                          					 resets | Number of
                                          					 SCCP gateway resets. |
| Endpoint
                                          					 restarts | Number of
                                          					 SCCP gateway restarts. |
| Configuration Error History | Displays
                                          					 SCCP autoconfiguration errors. |

| Field | Description |
|---|---|
| MGCP
                                          					 Fallback mode | The
                                          					 following are displayed: Not
                                                						  Selected--Fallback is not configured. Enabled/OFF--Fallback is configured but not in effect. Enabled/ON--Fallback is configured and in effect. |
| Last MGCP
                                          					 Fallback start time | Start
                                          					 time stamp in hh:mm:ss of the last fallback. |
| Last MGCP
                                          					 Fallback end time | End time
                                          					 stamp in hh:mm:ss of the last fallback. |

| Field | Description |
|---|---|
| Current
                                          					 active multicast sessions | Number of
                                          					 active calls on hold. |
| Multicast
                                          					 Address | Valid
                                          					 class D address from which the gateway is getting the RTP streams. |
| RTP port
                                          					 number | Valid RTP
                                          					 port number on which the gateway receives the RTP packets. |
| Packets
                                          					 in/out | Number of
                                          					 RTP packets received and sent to the digital signal processor (DSP). |
| Call id | Call ID
                                          					 of the call that is on hold. |
| Codec | Codec
                                          					 number. |
| Incoming
                                          					 Interface | Interface
                                          					 through which the gateway is receiving the RTP stream. |

| Command | Description |
|---|---|
| ccm-manager config | Supplies the local MGCP voice gateway with the IP address or logical name of
                                          						the TFTP server from which to download XML configuration files and enable the
                                          						download of the configuration. |
| debug ccm-manager | Displays debugging information about the Cisco CallManager. |
| show ccm-manager | Displays a list of Cisco CallManager servers, their current status, and their
                                          						availability. |
| show ccm-manager fallback-mgcp | Displays the status of the MGCP gateway fallback feature. |
| show isdn status | Displays the Cisco IOS gateway ISDN interface status. |
| show mgcp | Displays the MGCP configuration information. |

| Release | Modification |
|---|---|
| 12.0(7)T | This command was introduced on the Cisco AS5300. |
| 12.3(4)T | This command was enhanced to display V.120 call types registering with the modem. |

| Command | Description |
|---|---|
| debug cdapi | Displays information about the CDAPI. |

| slot | Backplane slot number. |
|---|---|
| /port | Interface port number. The slash must be entered. |

| Release | Modification |
|---|---|
| 12.1(2)T | This command was introduced on the Cisco 3600 series. |

| Command | Description |
|---|---|
| clock-select | Establishes the sources and priorities of the requisite
                                          						clocking signals for the OC-3/STM-1 ATM Circuit Emulation Service network
                                          						module. |

| all | Information for all configured connections. |
|---|---|
| elements | Information for registered hardware or software
                                          						interworking elements. |
| name | Information for a connection that has been named by using
                                          						the connect global configuration
                                          						command. The name you enter is case sensitive and must match the configured
                                          						name exactly. |
| id | Information for a connection that you specify by an
                                          						identification number or range of identification numbers. The router assigns
                                          						these IDs automatically in the order in which they were created, beginning with
                                          						1. The show connect all command displays these IDs. |
| port | Information for a connection that you specify by indicating
                                          						the type of controller (T1 or E1) and location of the interface. |
| T1 | T1 controller. |
| E1 | E1 controller. |
| slot/port | Location of the T1 or E1 controller port whose connection
                                          						status you want to see. Valid values for slot and port are 0 and 1 . The slash must be entered. |

| Release | Modification |
|---|---|
| 12.0(5)XK | This command was introduced on the Cisco 2600 series and
                                          						Cisco 3600 series. |
| 12.0(7)T | This command was integrated into Cisco IOS Release
                                          						12.0(7)T. |

| Command | Description |
|---|---|
| connect | Defines connections between T1 or E1 controller ports for
                                          						Drop and Insert. |
| tdm-group | Configures a list of time slots for creating clear channel
                                          						groups (pass-through) for TDM cross-connect. |

| slot | Slot location of the VDM module. Valid entries are 1 or 2. |
|---|---|
| port | Port location of the EIA/TIA-366 interface in the VDM module. |

| Release | Modification |
|---|---|
| 12.0(5)XK | This command was introduced on the Cisco MC3810. |
| 12.0(7)T | This command was integrated into Cisco IOS Release 12.0(7)T. |

| Field | Description |
|---|---|
| STATUS | Last interrupt status. |
| STATE | Current state of the state machine. |
| LSR | Line status register of the VDM. |
| LCR | Line control register of the VDM. |
| ICSR | Interrupt control and status register of the VDM. |
| EXT | Extended register of the VDM. |
| T1 through T5 | Timeouts 1 through 5 of the watchdog timer, in milliseconds. |
| Dial string | Most recently dialed number collected by the driver. 0xC at the end of the string indicates the EON (end of number) character. |

| tl/e1 controller - number | Controller number of CAS or ISDN PRI time slot. Range is
                                          						from 0 to 7. |
|---|---|
| timeslots timeslot - range | Timeslot. E1 range is from 1 to 31. T1 range is from 1 to
                                          						24. |

| Release | Modification |
|---|---|
| 10.0 | This command was introduced. |
| 12.1(3)T | The timeslots keyword was added. |
| 12.1(5)T | This command was implemented on the Cisco AS5400. |

| Command | Description |
|---|---|
| show controllers e1 | Displays information about E1 links. |
| show controllers t1 | Displays information about T1 links. |

| Release | Modification |
|---|---|
| 12.0(5)XQ | This command was introduced on the Cisco 1750. |

| Command | Description |
|---|---|
| show dial-peer voice | Displays configuration information and call statistics for dial peers. |
| show interface dspfarm | Displays hardware information including DRAM, SRAM, and the revision-level information on the line card. |
| show voice dsp | Displays the current status of all DSP voice channels. |
| show voice port | Displays configuration information about a specific voice port. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Field | Description |
|---|---|
| Carrier | ID of the carrier that handles the calls. |
| Cur Data (in) | Current number of incoming data calls that are handled by the carrier or trunk group. |
| Cur Data (out) | Current number of outgoing data calls that are handled by the carrier or trunk group. |
| Cur Voice (in) | Current number of incoming voice calls that are handled by the carrier or trunk group. |
| Cur Voice (out) | Current number of outgoing voice calls that are handled by the carrier or trunk group. |
| Max Calls | Maximum number of calls that are handled by the carrier or trunk group. |
| Max Data (in) | Maximum number of incoming data calls that are handled by the carrier or trunk group. |
| Max Data (out) | Maximum number of outgoing data calls that are handled by the carrier or trunk group. |
| Max Voice (in) | Maximum number of incoming voice calls that are handled by the carrier or trunk group. |
| Max Voice (out) | Maximum number of outgoing voice calls that are handled by the carrier or trunk group. |
| Trunk Group Label | Label of the trunk group that handles the calls. |

| Command | Description |
|---|---|
| carrier-id (dial-peer) | Specifies the carrier associated with VoIP calls. |
| max-calls | Specifies the maximum number of calls handled by a trunk group. |
| show trunk group | Displays the configuration parameters for one or more trunk groups. |
| trunk-group (interface) | Assigns an interface to a trunk group. |
| trunk-group-label (dial-peer) | Specifies the trunk group associated with VoIP calls. |

| call-rate | Displays the incoming and outgoing call switching rate. |
|---|---|
| table | (Optional) Displays the incoming and outgoing call switching rate in the form of numerical table. |
| call-resource | Displays statistics about the CSM call resource. |
| modem | Displays CSM call statistics for modems. |
| slot / port | (Optional) Location (and thereby identity) of a specific modem. |
| group | (Optional) Displays modem group information. |
| modem - group - number | (Optional) Location of a particular dial peer. Range: 1 to 32767. |
| signaling-channel | Displays CSM signaling channel Information. |
| voice | Displays CSM call statistics for DSP channels. |

| Release | Modification |
|---|---|
| 11.3 NA | This command was introduced. |
| 12.0(3)T | This command was modified. Port-specific values for the Cisco AS5300 were added. |
| 12.0(7)T | This command was modified. Port-specific values for the Cisco AS5800 were added. |

| Field | Description |
|---|---|
| slot | Slot where the VFC resides. |
| dsp | DSP through which this call is established. |
| slot/port | Logical port number for the device. This is equivalent to the DSP channel number. The port number is derived as follows: (max_number_of_dsp_channels per dspm=12) * the dspm # (0-based) + (max_number_of_dsp_channels per dsp=2) * the dsp # (0-based) + the dsp channel number (0-based). |
| tone | Which signaling tone is being used (DTMF, MF, R2). This only applies to CAS calls. Possible values are as follows: mf dtmf r2-compelled r2-semi-compelled r2-non-compelled |
| device_status | Status of the device. Possible values are as follows: VDEV_STATUS_UNLOCKED--Device is unlocked (meaning that it is available for new calls). VDEV_STATUS_ACTIVE_WDT--Device is allocated for a call and the watchdog timer is set to time the connection response from
                                                the central office. VDEV_STATUS_ACTIVE_CALL--Device is engaged in an active, connected call. VDEV_STATUS_BUSYOUT_REQ--Device is requested to busyout; does not apply to voice devices. VDEV_STATUS_BAD--Device is marked as bad and not usable for processing calls. VDEV_STATUS_BACK2BACK_TEST--Modem is performing back-to-back testing (for modem calls only). VDEV_STATUS_RESET--Modem needs to be reset (for modem only). VDEV_STATUS_DOWNLOAD_FILE--Modem is downloading a file (for modem only). VDEV_STATUS_DOWNLOAD_FAIL--Modem has failed during downloading a file (for modem only). VDEV_STATUS_SHUTDOWN--Modem is not powered up (for modem only). VDEV_STATUS_BUSY--Modem is busy (for modem only). VDEV_STATUS_DOWNLOAD_REQ--Modem is requesting connection (for modem only). |
| csm_state | CSM call state of the current call (PRI line) associated with this device. Possible values are as follows: CSM_IDLE_STATE--Device is idle. CSM_IC_STATE--A device has been assigned to an incoming call. CSM_IC1_COLLECT_ADDR_INFO--A device has been selected to perform ANI/DNIS address collection for this call. ANI/DNIS address
                                                information collection is in progress. The ANI/DNIS is used to decide whether the call should be processed by a modem or a
                                                voice DSP. CSM_IC2_RINGING--The device assigned to this incoming call has been told to get ready for the call. CSM_IC3_WAIT_FOR_SWITCH_OVER--A new device is selected to take over this incoming call from the device collecting the ANI/DNIS
                                                address information. CSM_IC4_WAIT_FOR_CARRIER--This call is waiting for the CONNECT message from the carrier. CSM_IC5_CONNECTED--This incoming call is connected to the central office. CSM_IC6_DISCONNECTING--This incoming call is waiting for a DISCONNECT message from the VTSP module to complete the disconnect
                                                process. CSM_OC_STATE --An outgoing call is initiated. CSM_OC1_REQUEST_DIGIT--The device is requesting the first digit for the dial-out number. CSM_OC2_COLLECT_1ST_DIGIT--The first digit for the dial-out number has been collected. CSM_OC3_COLLECT_ALL_DIGIT--All the digits for the dial-out number have been collected. CSM_OC4_DIALING--This call is waiting for a dsx0 (B channel) to be available for dialing out. CSM_OC5_WAIT_FOR_CARRIER--This (outgoing) call is waiting for the central office to connect. CSM_OC6_CONNECTED--This (outgoing) call is connected. CSM_OC7_BUSY_ERROR--A busy tone has been sent to the device (for VoIP call, no busy tone is sent; just a DISCONNECT INDICATION
                                                message is sent to the VTSP module), and this call is waiting for a DISCONNECT message from the VTSP module (or ONHOOK message
                                                from the modem) to complete the disconnect process. CSM_OC8_DISCONNECTING--The central office has disconnected this (outgoing) call, and the call is waiting for a DISCONNECT
                                                message from the VTSP module to complete the disconnect process. |
| csm_state: invalid_event_count | Number of invalid events received by the CSM state machine. |
| wdt_timeout_count | Number of times the watchdog timer is activated for this call. |
| wdt_timestamp_started | Whether the watchdog timer is activated for this call. |
| wait_for_dialing | Whether this (outgoing) call is waiting for a free digit collector to become available to dial out the outgoing digits. |
| wait_for_bchan | Whether this (outgoing) call is waiting for a B channel to send the call out on. |
| pri_chnl | Which type of TDM stream is used for the PRI connection. For PRI and CAS calls, it is always TDM_PRI_STREAM. |
| tdm_chnl | Which type of TDM stream is used for the connection to the device used to process this call. In the case of a VoIP call,
                                          this is always set to TDM_DSP_STREAM. |
| dchan_idb_start_index | First index to use when searching for the next IDB of a free D channel. |
| dchan_idb_index | Index of the currently available IDB of a free D channel. |
| csm_event | Event just passed to the CSM state machine. |
| cause | Event cause. |
| ring_no_answer | Number of times a call failed because there was no response. |
| ic_failure | Number of failed incoming calls. |
| ic_complete | Number of successful incoming calls. |
| dial_failure | Number of times a connection failed because there was no dial tone. |
| oc_failure | Number of failed outgoing calls. |
| oc_complete | Number of successful outgoing calls. |
| oc_busy | Number of outgoing calls whose connection failed because there was a busy signal. |
| oc_no_dial_tone | Number of outgoing calls whose connection failed because there was no dial tone. |
| oc_dial_timeout | Number of outgoing calls whose connection failed because the timeout value was exceeded. |
| call_duration_started | Start of this call. |
| call_duration_ended | End of this call. |
| total_call_duration | Duration of this call. |
| The calling party phone number | Calling party number as given to CSM by ISDN. |
| The called party phone number | Called party number as given to CSM by ISDN. |
| total_free_rbs_time slot | Total number of free RBS (CAS) time slots available for the whole system. |
| total_busy_rbs_time slot | Total number of RBS (CAS) time slots that have been busied-out. This includes both dynamically and statically busied out
                                          RBS time slots. |
| total_dynamic_busy_rbs_time slot | Total number of RBS (CAS) time slots that have been dynamically busied out. |
| total_static_busy_rbs_time slot | Total number of RBS (CAS) time slots that have been statically busied out (that is, they are busied out using the CLI command). |
| total_free_isdn_channels | Total number of free ISDN channels. |
| total_busy_isdn_channels | Total number of busy ISDN channels. |
| total_auto_busy_isdn_channels | Total number of ISDN channels that are automatically busied out. |

| Command | Description |
|---|---|
| show call active voice | Displays the contents of the active call table. |
| show call history voice | Displays the contents of the call history table. |
| show num-exp | Displays how number expansions are configured. |
| show voice port | Displays configuration information about a specific voice port. |

| failed | CSM call fail/reject rate for the last 60 seconds, 60 minutes, and 72 hours. |
|---|---|
| rate | CSM call rate for the last 60 seconds, 60 minutes, and 72 hours. |
| total | Total number of CSM calls for the last 60 seconds, 60 minutes, and 72 hours. |

| Release | Modification |
|---|---|
| 12.3(2)T | This command was introduced on the Cisco AS5850. |

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |

| Release | Modification |
|---|---|
| Cisco IOS XE Amsterdam 17.3.2 and Cisco IOS XE Bengaluru 17.4.1a | This command was modified to support Cisco Smart Licensing Using Policy. |
| Cisco IOS XE Amsterdam 17.2.1r | The dependency on mode border-element license capacity sessions command was removed. Licensed-Capacity and blocked call information was excluded from output. |
| 15.1(3)S1 | This command was modified. The output was modified to have only token characters (an alphanumeric character, hyphen [-], dot [.], exclamation mark [!],
                                          percent [%], asterisk [*], underscore [_], plus sign [+], grave [`], apostrophe ['], or a tilde [~]) in server and user-agent
                                          Session Initiation Protocol (SIP) headers. The nontoken characters present in the image name is replaced by a dot[.]. |
| 15.2(1)T | This command was introduced. |

| Field | Description |
|---|---|
| CUBE-Version | Version of the CUBE application running on the device. |
| SW-Version | Image version and platform name of the device running the CUBE application. This matches the image version and platform name returned by the show version command. |
| HA-Type | The type of High Availability (HA) feature configured and running on the device. The following HA types are supported: none: CUBE does not support HA. cold-standby-chassis-to-chassis: Device-to-device cold standby support. hot-standby-chassis-to-chassis: Device-to-device hot standby support. |
| Licensed-Capacity | Note Effective from Cisco IOS XE Amsterdam 17.2.1r , Licensed-Capacity and blocked call information is no longer included in the output. Number of SIP call legs that CUBE is licensed to use. The range is from 0 through 999999. This number matches the number of licenses configured using the mode border-element license capacity command. Note The number of SIP call legs that CUBE can use is platform-dependent and is not affected by the specified value for the capacity keyword in Cisco IOS Release 15.2(1)T. | Note | Effective from Cisco IOS XE Amsterdam 17.2.1r , Licensed-Capacity and blocked call information is no longer included in the output. | Note | The number of SIP call legs that CUBE can use is platform-dependent and is not affected by the specified value for the capacity keyword in Cisco IOS Release 15.2(1)T. |
| Note | Effective from Cisco IOS XE Amsterdam 17.2.1r , Licensed-Capacity and blocked call information is no longer included in the output. |
| Note | The number of SIP call legs that CUBE can use is platform-dependent and is not affected by the specified value for the capacity keyword in Cisco IOS Release 15.2(1)T. |

| Note | Effective from Cisco IOS XE Amsterdam 17.2.1r , Licensed-Capacity and blocked call information is no longer included in the output. |
|---|---|

| Note | The number of SIP call legs that CUBE can use is platform-dependent and is not affected by the specified value for the capacity keyword in Cisco IOS Release 15.2(1)T. |
|---|---|

| Command | Description |
|---|---|
| mode border-element | Enables the set of commands used in the border-element configuration on the Cisco 2900 and Cisco 3900 series platforms. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced on the Cisco 3640, Cisco 3660, Cisco AS5300, Cisco AS5350, and Cisco AS5400. |
| 12.0(28)S | This command was integrated into Cisco IOS Release 12.0(28)S and was enhanced to include debugging for ATM-enabled and Frame
                                          Relay-enabled interfaces. |
| 12.2(25)S | This command was integrated into Cisco IOS Release 12.2(25)S. |
| 12.2(27)SBC | This command was integrated into Cisco IOS Release 12.2(27)SBC. |
| 12.2(28)SB | This command was integrated into Cisco IOS Release 12.2(28)SB. |
| 12.4(9)T | This command was enhanced to include debugging for ATM-enabled and Frame Relay-enabled interfaces. |

| Field | Description |
|---|---|
| Condition 1 | Sequential number identifying the filter condition that was set for the specified command. |
| Flags | Name of the voice application for which the condition was set. |
| at2/0 | Interface number of the ATM interface that has the debug condition applied. |
| atm-vc 0/56784 | Virtual channel identifier (VCI). Alternatively, virtual path identifier/virtual channel identifier (VCI/VPI) pair. |

| Command | Description |
|---|---|
| debug condition application voice | Filters out debugging messages for all VoiceXML applications except the specified application. |
| debug http client | Displays debugging messages for the HTTP client. |
| debug vxml | Displays debugging messages for VoiceXML features. |