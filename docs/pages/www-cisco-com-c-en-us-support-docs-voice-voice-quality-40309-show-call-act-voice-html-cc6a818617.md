---
doc_id: www-cisco-com-c-en-us-support-docs-voice-voice-quality-40309-show-call-act-voice-html-cc6a818617
source_url: https://www.cisco.com/c/en/us/support/docs/voice/voice-quality/40309-show-call-act-voice.html
retrieved_at: 2026-08-21T07:21:16.902602+00:00
---

Using the show call active voice Command to Troubleshoot Voice Quality Issues

# Using the show call active voice Command to Troubleshoot Voice Quality Issues

Updated: July 31, 2006

Document ID: 40309

Contents

## Contents

## Introduction

This document discusses the show call active voice ( registered customers only) command output and illustrates how the command output resolves voice quality issues.

Note: The commands referenced in this document are linked to the Command Lookup Tool ( registered customers only) . Use this tool in order to search for more information on specific commands.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software and hardware versions.

### Conventions

Refer to the Cisco Technical Tips Conventions for more information on document conventions.

## show call active voice Command Output

The show call active voice command allows you to display the contents of the active call table. The information presented includes call times, dial peers, connections, quality of service parameters, and gateway handling of jitter. This information can be useful when you troubleshoot a range of voice quality problems.

The table in this document includes the output from a sample show call active voice command and a brief explanation of each parameter.

Note: The show call active voice command displays data from the plain old telephone service (POTS) and VoIP call legs on the voice gateway. Some parameters are highlighted in bold text for further discussion in the remainder of the document.

The show call active command displays values for both the Telephony and the VoIP legs of any active call. For each leg, the same generic parameters are shown followed by parameters specific to the type of call leg. In this table, these parameter sections are noted by a shaded header.

Use the show call active voice command in user EXEC or privileged EXEC mode in order to display call information for voice calls in progress.

```
show call active voice [brief [id identifier ] | compact [duration {less time | more time }] | echo-canceller call-id | id identifier | redirect {rtpvt | tbct}]
```

There are many arguments options to this command. This list describes some of the more useful arguments:

brief —(Optional) Displays a truncated version.

compact —(Optional) Displays active calls that are longer or shorter than a specified time.

duration —(Optional) Displays active calls that are longer or shorter than a specified time.

echo-canceller call-id —(Optional) Displays information about the state of the extended echo canceller (EC). In order to query the echo state, you need to know the hex ID in advance. In order to find the hex ID, enter the show call active voice brief command or use the show voice call status command. The range is from 0 to FFFFFFFF.

- When a packet is lost and there is no audio sample available to play. For example, when two or more packets are lost in sequence. This situation can result in an audible click or gap being heard by the user.

- When the playout buffer adapts to a larger value by inserting silence between buffered voice packets. This situation does not result in an audible loss in quality.

- The RTP sequence number is earlier than the RTP sequence number of the packet that currently plays out.

- The RTP sequence number is later than the packet that currently plays out but outside the available playout buffer.

## Use of the Command Output to Troubleshoot Voice Quality Issues

This section includes a discussion on the impact of voice quality of highlighted parameters in the Parameters table.

### Dial Peer Matching and Bandwidth Consumption

These parameters provide information associated with a particular VoIP leg of a call. In this particular call leg example, the call matches with dial peer 200, the codec used is G.729 with a payload size of 20 bytes, and VAD is enabled.

PeerId=200

CoderTypeRate=g729r8

CodecBytes=20

VAD = enabled

This information, when combined with information about the network configuration, such as the Layer 2 transport and the optional use of compressed RTP allows you to determine the per call bandwidth requirements for calls that match this dial peer. Refer to Voice Over IP - Per Call Bandwidth Consumption for more information.

If provisioned bandwidth is insufficient in order to support the number of calls, then the result can be choppy or synthetic voice.

Note: The command call threshold can be used as one of the methods for call admission control, but this command does not work for outgoing calls from ISDN interfaces to H323 networks.

If the characteristics of the call leg do not seem correct, review your dial peer configuration and matching. Refer to some of the dial peer related documents listed at the Call Routing / Dial Plans Technical Support page for more information.

### Garbled Voice

Garbled voice , of which choppy and synthetic voice are good examples, can occur under a number of circumstances usually associated with incorrectly provisioned WAN links. These potentially result from lack of appropriate connection admission control (CAC), or incorrectly configured voice prioritization. The show call active voice command provides visibility into these issues with these parameters:

OnTimeRvPlayout=742740

GapFillWithSilence=0 ms

GapFillWithPrediction=0 ms

HiWaterPlayoutDelay=70 ms

LoWaterPlayoutDelay=69 ms

ReceiveDelay=69 ms

LostPackets=0 ms

EarlyPackets=1 ms

LatePackets=0 ms

The OnTimeRvPlayout command provides a good general view of the health of the call when it is compared to the Total Voice Playout Duration. The Total Voice Playout Duration can be derived with the addition of the gap fill durations to the OnTimeRvPlayout duration. If the proportion of on time voice playout time is high then the call is likely to be healthy.

Packets dropped or delayed too long in the packet network can cause voice quality issues.

On receipt of packets that are delayed for so long that they cannot be used, or when packets are dropped in the network and not received at all, an IP phone or voice gateway attempts to reconstruct the voice stream as best it can by the prediction of the voice signal.

Repeatedly issue the show call active voice command on an IOS gateway in order to provide visibility into this issue:

LatePackets —The number of packets that arrive outside the de-jitter buffer playback delay period. These packets are discarded.

LostPackets —The number of packets that never arrive at the receiving IP phone or gateway.

GapFillWithPrediction —The amount of packet prediction in a call. Divide this number by the packet sample time in order to determine the number of packets affected.

GapFillWithSilence —The amount of silence insertion in the call.

Note: The show port voice active command on a Catalyst gateway gives you an indication of jitter for a call ( Hi/Low water playout delay ) though it does not differentiate between predictive and silence insertion.

Synthetic voice

A small amount of predictive insertion is undetectable to the human ear. However, a large amount probably causes a garbled quality in the voice that can be described as synthetic or robotic voice.

Choppy voice

If packets are dropped or arrive late, then it is not possible for the receiving codec decoder to predict the voice signal. In this case, the signal is replaced with silence inserted into speech.

In addition, if delay is variable (jitter), packets that arrive late but within the playout delay period of the receiving de-jitter buffer, are played out but can cause an underrun of the de-jitter buffer. An underrun occurs when there are no packets left held in the buffer and the speech is delayed when the buffer waits for the next packet to arrive. Audible gap in speech can result.

A small amount of silence insertion or jitter is undetectable to the human ear. However, a large amount probably causes a quality in the voice that can be described as choppy voice or broken voice.

Note: If the network delay is variable enough, it is likely that the resulting sound of the speech is both synthetic and choppy.

Resolve Garbled Voice Problems

Determine the cause of the delay and (if possible) eliminate it.

Causes of drops or delays in a packet Telephony network can be many and varied. Some common examples include:

Misconfigured Low Latency Queuing

Misconfigured fragmentation for low speed links

Misconfigured traffic shaping and/or frame relay CIR ( registered customers only) exceeded

Links with over-committed bandwidth in the path of the call. For example, poor CAC for voice calls. An example is a G.711 call with no cRTP or VAD across a 64 Kbps link.

Duplex mismatches in an Ethernet environment

CPU intensive operations on a router in the path of the call. For example, debugs to a console or saving the router configuration can cause high CPU utilization that delays packets that traverse it.

It is also possible to tune the gateway de-jitter buffers for better voice performance in sub-optimal data networks. However, the results are limited to the degree to which the data network behaves correctly. For more information, refer to Troubleshooting QoS Choppy Voice Issues or a number of the documents listed at the Voice Quality Technical Support page.

### Hissing, Static, and Clipping

These parameters identify whether VAD is used for this call and what dial peer is used:

VAD = enabled

PeerId=200

NoiseLevel=-59

Resolve Hissing and Clipping Problems

In order to resolve hissing and some front-end clipping issues, adjust music-threshold or vad-time values (or disable VAD) before you troubleshoot other possible problems.

Test by disabling comfort-noise ( registered customers only) or disabling VAD entirely. If the symptom stops, then comfort noise generation is the likely cause of the problem. Reduction of the music-threshold ( registered customers only) at which voice is detected or increase in the vad-time ( registered customers only) values on the gateway can make the hissing or clipping less noticeable without the need to disable VAD permanently. These techniques essentially disable VAD at low volume levels and/or during small gaps, respectively. It is not practical to just disable comfort noise since that action causes other voice quality symptoms such as clicking and/or gaps of absolute silence between sentences.

Refer to Troubleshooting Hissing and Static for more information. If these tuning techniques do not solve the problem, then disable VAD. This results in a loss of bandwidth savings.

Resolve Hissing and Clipping Problems in One Direction

VAD is the cause of most hissing problems. Therefore, it is important to identify whether it is enabled. One of the first steps to troubleshoot hissing or front-end clipping of sentences is to disable VAD. It is therefore important to be able to identify whether it is disabled.

If hissing or clipping only occurs in one direction, the outbound direction, then it can be due to VAD being enabled in this direction even though you have tried to disable it in the VoIP dial peer. In this case, the show call active voice command shows VAD enabled and the PeerID in use being 0. In order to overcome this issue, configure the incoming called-number <number_dialed> ( registered customers only) command on the VoIP dial peer to ensure that calls to the PSTN match this peer at the gateway. Otherwise, calls in this direction match with the default dial peer that has VAD enabled by default.

### Echo

These parameters are important to troubleshoot echo:

ACOMLevel=20

OutSignalLevel=-64

InSignalLevel=-58

ERLLevel=20

The test tone output is -15 and is looped back with 0 dB loss. Therefore, it comes back at -15 dB. The ERL value here has no significance at this point since the echo canceller does not consider the input signal to be echo.

Note: The OutSignalLevel shows the value of the level after the output attenuation is applied to the signal. The InSignalLevel shows the value of the level after the input gain is applied.

If the ERL value is too low, the echo signal that returns to the gateway might be too loud (within 6 db of the talker signal). This causes the echo canceller to consider it as voice (double-talk) instead of echo. Therefore, the echo canceller does not cancel the echo. ERL should be between 6 db and 20 db in order for the echo canceller to engage.

Refer to Troubleshooting Echo Problems between IP Phones and Cisco IOS Gateways and Troubleshooting Echo in IP Telephony Networks (Audio on Demand) for information on troubleshooting echo problems.

### Jitter and Typical Voice Quality Symptoms

This section explains how to use the show call active voice command in order to identify jitter and typical voice quality symptoms.

A general idea of jitter in the network can be determined by repeatedly issuing the show call active voice command while a call is in progress. Ideally, these parameters should stay relatively steady. If they do, that is an indication of smooth packet flow. However, if jitter is present, there are sharp, short term spikes such as those shown in these two sample outputs:

```
GapFillWithSilence=950 ms GapFillWithPrediction=1980 ms GapFillWithInterpolation=0 ms 
GapFillWithRedundancy=0 ms 
HiWaterPlayoutDelay=350 ms 
LoWaterPlayoutDelay=25 ms ReceiveDelay=29 ms LostPackets=0 
EarlyPackets=0 LatePackets=83
```

```
. 
. GapFillWithSilence=1040 ms 
GapFillWithPrediction=2350 ms GapFillWithInterpolation=0 ms 
GapFillWithRedundancy=0 ms 
HiWaterPlayoutDelay=40 ms 
LoWaterPlayoutDelay=28 ms ReceiveDelay=35 ms LostPackets=0 
EarlyPackets=0 LatePackets=99
```

The incrementing number of late packets in these sample outputs reveal a degree of jitter. The silence insertion indicated by an increase in the GapFillWithSilence value manifests itself as choppy voice. The predictive insertion, indicated by an increase in the GapFillWithPrediction value, tends to manifest itself as synthetic voice.

In order to alter the amount of voice signal that is buffered to avoid jitter buffer under-runs or over-runs, issue the playout-delay command.

The two modes of configuration for playout delay are adaptive and fixed:

Adaptive allows the jitter buffer to grow and shrink for the duration of the call within a configured range when you issue the playout-delay {nominal value | maximum value | minimum {default | low | high}} command.

Fixed is set at the beginning of a call when you issue the playout-delay mode {adaptive | fixed [no-timestamps]} command.

Refer to Playout Delay Enhancements for more information on VoIP.

## Related Information

### Revision History

1.0

18-Sep-2013

Initial Release

| show call active voice Parameter | Explanation of Parameter |
|---|---|
| GENERIC: | Generic stats for the POTS call leg that follows |
| SetupTime=866793 ms | The clock time in 100 ms increments when the POTS leg is initiated. For incoming ISDN POTS calls, this is the time when the Q.931 call setup message is received. |
| Index=1 |  |
| PeerAddress=100 | The Destination-Pattern that matches this POTS peer. For an incoming POTS call leg, this is the calling number or Automatic Number Identification (ANI). |
| PeerSubAddress= |  |
| PeerId=100 | The dial peer ID used for this call leg. In this case, although unnecessary, the PeerID and the PeerAddress are the same. |
| PeerIfIndex=9 | The voice port index number for this peer. For ISDN media, this is the index number of the B-channel used for this call. |
| LogicalIfIndex=5 | The index used internally in order to identify the logical interface for the call. |
| ConnectTime=867030 | The clock time in 100 ms increments when the POTS leg connects. For an incoming ISDN POTS call leg, this is the time when the Q.931 call connect message is sent. |
| CallDuration=00:12:26 | The time in hh:mm:ss for which the call establishes. |
| CallState=4 | The call state for the call leg (4=active,3=connected,2=connecting). The call state is active. |
| CallOrigin=2 | Originate vs. answer (1=originate, 2=answer) for the call leg. This gateway answers this (POTS) call leg. |
| ChargedUnits=0 | The total number of charging units that apply to this peer since system startup. The unit of measure for this field is hundredths of a second. |
| InfoType=2 | The information type for this call (1=fax, 2=voice). This is a voice call. |
| TransmitPackets=37291 | The number of packets that transmit from the digital signal processor (DSP) to the Telephony interface. |
| TransmitBytes=725552 | The byte count equivalent of the POTS TransmitPackets value. |
| ReceivePackets=1689 | The number of packets received by the DSP from the Telephony interface. |
| ReceiveBytes=33780 | The byte count equivalent of the POTS ReceivePacketsPackets value. |
| TELE: | POTS call leg |
| ConnectionId=[0xC59FE183 0xB1700D7 0x0 0x84431C] | This is the connection identification number that the gateway gives in order to uniquely represent this call. It matches across all call legs of the call on this gateway. |
| TxDuration=746070 ms | The duration of call (ms) = 12 min 26 seconds = 746 seconds = 746070 ms. |
| VoiceTxDuration=33780 ms | The cumulative time in ms when voice packets are sent from the Telephony POTS peer to the VoIP gateway. |
| FaxTxDuration=0 ms | The cumulative time in ms when the router is in fax mode. |
| CoderTypeRate=g729r8 | The codec used for the call. |
| NoiseLevel=-59 | The active noise level for this call. This value is calculated in the comfort noise generation module and is used to generate comfort noise when voice activity detection (VAD) is enabled. |
| ACOMLevel=20 | The current ACOM level for this call. ACOM is the combined loss achieved by the echo canceler. This value is the sum of the Echo Return Loss (ERL), Echo Return Loss Enhancement (ERLE), and Non-Linear Processing (NLP) loss for the call. |
| OutSignalLevel=-64 | The output signal level in Decibels Per Milliwatt (dBm). |
| InSignalLevel=-58 | The input signal level in dBm. |
| InfoActivity=2 | The active information transfer activity state for this call. |
| ERLLevel=20 | The ERL for this call. |
| SessionTarget= | This value applies to VoIP call legs. This value is specified in the VoIP dial peer. There is no session target for POTS call legs. |
| ImgPages=0 |  |
|  |  |
| GENERIC: | Generic statistics for VOIP call leg to follow: |
| SetupTime=866928 ms | The clock time in 100 ms increments when the VoIP call leg is initiated. For outgoing H.323 VoIP calls, this is the time when the H.323 call setup message is sent. |
| Index=1 |  |
| PeerAddress=200 | The destination-Pattern of the peer. For an outbound VoIP call leg, this is the called number or dialed number identification service (DNIS). |
| PeerSubAddress= |  |
| PeerId=200 | The peerID that the DNIS matches. In this case, although unnecessary, the peerID and the DNIS are the same. |
| PeerIfIndex=11 |  |
| LogicalIfIndex=0 |  |
| ConnectTime=867029 | The clock time in 100 ms increments at which the VoIP leg connects. For an outgoing H.323 VoIP call leg, this is the time when the H.323 call connect message is received. |
| CallDuration=00:12:27 | The duration in hh:mm:ss of a call. |
| CallState=4 | The call state for call leg (4=active,3=connected,2=connecting). The call state is active. |
| CallOrigin=1 | Originate vs. answer (1=originate, 2=answer) for call leg. This gateway originates this (VoIP) call leg. |
| ChargedUnits=0 |  |
| InfoType=2 |  |
| TransmitPackets=1689 | The number of VoIP packets transmitted by this gateway on this call leg. |
| TransmitBytes=33780 | The byte count equivalent of the VoIP TransmitPackets value. This needs to match VoiceTxDuration from the Telephony call leg since with G.729, one Byte is sent per 1 ms. |
| ReceivePackets=37343 | The number of VoIP packets received by this gateway on this call leg. |
| ReceiveBytes=746860 | The byte count equivalent of the VoIP ReceivePackets value. |
| VOIP: | VoIP call leg |
| ConnectionId[0xC59FE183 0xB1700D7 0x0 0x84431C] | This is the connection identification number that the gateway gives in order to uniquely represent this call. It matches across all call legs of the call on this gateway. |
| RemoteIPAddress=10.1.1.2 | The remote IP address for the call. |
| RemoteUDPPort=18280 | The remote User Datagram Protocol (UDP) port for the call. |
| RoundTripDelay=53 ms | The round trip delay as measured by the gateway. |
| SelectedQoS=best-effort | The Resource Reservation Protocol (RSVP) is not selected in the dial peer for this call. |
| tx_DtmfRelay=cisco-rtp | The form of DTMF RELAY used for the call (if any). |
| SessionProtocol=cisco | The Session Protocol for the call. Protocol "cisco" is the default, using H.323 signaling and RTP packets for the voice traffic. Session Intitiation Protocol (SIP) is the other VoIP signaling protocol that can be specified with the help of the session protocol ( registered customers only) dial peer command. Non-VoIP protocols such as AAL2 for VoATM or the Cisco proprietary Voice over Frame Relay (VoFR) protocol and FRFll for VoFR can also be specified. |
| SessionTarget=ipv4:10.1.1.2 | The session-target from the dial peer. The session target is RAS if a gatekeeper is used. |
| OnTimeRvPlayout=742740 | The duration in ms of the voice playout from the data received on time for this call. The Total Voice Playout Duration can be derived by adding the gap fill durations to the OnTimeRvPlayout duration. |
| GapFillWithSilence=0 ms | Time (ms) Gateway (GW) played silence. Silence plays out in these situations: When a packet is lost and there is no audio sample available to play. For example, when two or more packets are lost in sequence. This situation can result in an audible click or gap being heard by the user. When the playout buffer adapts to a larger value by inserting silence between buffered voice packets. This situation does not result in an audible loss in quality. |
| GapFillWithPrediction=0 ms | The duration in ms of the voice signal played out with the signal synthesized from parameters, or samples of data that precede it in time. This gap fill occurs because voice data is lost or not received in time from the voice gateway for this call. Examples of such pullout are frame-eraser and frame-concealment strategies in G.729 and G.723.1 compression algorithms. |
| GapFillWithInterpolation=0 ms | As for GapFillWithPrediction but taking into consideration samples received after the missing voice traffic and stored in the de-jitter buffer. Not currently used. |
| GapFillWithRedundancy=0 ms | If a redundant encoding scheme is used by the transmitter, then the payload of lost or late packets can be partially or fully recovered and played out with a reduced impact on voice quality. This technique is not currently supported. |
| HiWaterPlayoutDelay=70 ms | The First-In, First-Out (FIFO) jitter buffer high mark that indicates the maximum depth to which the de-jitter buffer adapts for this call. |
| LoWaterPlayoutDelay=69 ms | The FIFO jitter buffer low mark that indicates the minimum depth to which the de-jitter buffer adapts for this call. |
| ReceiveDelay=69 ms | The current playout FIFO delay plus the decoder delay for the call. |
| LostPackets=0 ms | The lost RTP packets represented in ms. Any positive jump in the sequence number adds to the LostPackets counter. For example, if a gateway receives packets with a sequence of numbers in the order of N-1, N, N+1, N+3, N+2, N+4, then the LostPackets counter increments. The size of the dejitter buffer and when the "lost" packet arrives determines if the packet can play. |
| EarlyPackets=1 ms | The number of early RTP packets represented in ms. RTP packets are timestamped as they are transmitted and the RTP timestamp value is included in the packet. The time at which the packet is received is also timed by the local clock of the gateway. If the local clock time difference (time received) of two adjacent packets is smaller than their RTP timestamps difference (time sent) then the second packet is considered early. An early packet can occur when network utilization drops suddenly. This results in lower network delay for a particular packet. |
| LatePackets=0 ms | The number of late RTP packets represented in ms. This value is incremented when a packet is received with an RTP sequence number in either of these circumstances: The RTP sequence number is earlier than the RTP sequence number of the packet that currently plays out. The RTP sequence number is later than the packet that currently plays out but outside the available playout buffer. |
| VAD = enabled | VAD is enabled for this call leg. |
| CoderTypeRate=g729r8 | The codec type used for this call. |
| CodecBytes=20 | The payload size, in bytes, for the codec used. |
| SignalingType=cas | The signaling type for the call. This is only for permanent calls. |

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 18-Sep-2013 | Initial Release |