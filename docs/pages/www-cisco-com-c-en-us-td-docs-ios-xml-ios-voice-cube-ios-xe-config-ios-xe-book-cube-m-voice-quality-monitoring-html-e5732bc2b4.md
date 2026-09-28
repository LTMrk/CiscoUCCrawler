---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-cube-m-voice-quality-monitoring-html-e5732bc2b4
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/cube_m_voice-quality-monitoring.html
retrieved_at: 2026-08-16T15:54:15.541466+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Monitor Voice Quality

## Chapter: Monitor Voice Quality

# Monitor Voice Quality

## Overview

Call quality statistics in CUBE , such as packet loss, jitter, and round trip delay can be added to the call detail record (CDR), and these voice metrics
                           can be calculated in IOS. For more information, refer to Voice Quality Enhancements on Cisco Unified Border Element .

The call quality statistics feature is enhanced to provide the
                           		following capabilities:

Enable or disable Quality of Service (QoS) for CUBE .

Enable or disable Real-time Transport Protocol (RTP) Control
                                 			 Protocol (RTCP) passthrough.

Configure call quality criteria parameters.

Call quality configuration parameters include max_dropout, max_reorder, and clock_rate. A maximum of three codecs (codec_number,
                           payload_type, clock_rate) per media flow is collected by the PI and sent to CPP, which uses these values in statistics calculation.
                           Calculated statistics such as Jitter, Packet Loss, and Delay are then fetched from the CPP to the CDR. These statistics can
                           be viewed in the command line interface.

The CDR has the following data per call leg of the call:

Packet Loss-Calculated based on methods shown in RFC3550. The RTCP sender/receiver reports are recalculated, and not just
                                 copied from the inbound leg to the outbound leg.

Delay-Calculated based on timestamp received or timestamp of packets sent.

Jitter-Variation of delay.

For more information on how to calculate the voice quality metrics related to media(voice) quality, such as conversational
                           mean opinion score (MOS), jitter, and so on, see http://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/configuration/cube-book/voi-cube-call-monitoring.html .

The VQM (Voice Quality Monitor) gives information on the voice quality metrics. The VQM on Cisco IOS XE platforms enables
                           statistics gathering based on the received RTCP packets. From these statistics, a voice quality measurement is developed to
                           show the quality of the call. The output is in a simple format, using a system of good, poor, and bad types of ratings.

The following metrics exists in Call Detail Record (CDR) and Management Information Base (MIB) in CUBE, indicating voice quality:

MOSQe (conversational quality MOS)

Round-trip-delay.

Receive-delay (current jitter buffer size).

Packet-Loss-Rate.

The CDR is sent at the end of a call if AAA accounting is configured.

A CDR example is as follows:

<MOS-Con>4.4072</MOS-Con>

<round-trip-delay>1 ms</round-trip-delay>

<receive-delay>64 ms</receive-delay>

<voice-quality-total-packet-loss>0.0000 %</ voice-quality-total-packet-loss>

### VQM
                           	 Metrics

The following are
                              		the metrics exported by VQM:

IOS VQM,
                                          					 Voice/Audio Description Quality Metric

Description

MOS-Con

The
                                          					 conversational quality MOS. Conversational quality indicates the impact of the
                                          					 quality of the transmission on the dynamics of conversational exchanges between
                                          					 two parties; such metrics take into account delay, echo, and recency.

round-trip-delay

The
                                          					 instantaneous round-trip delay. This may be obtained from the RTCP SR reports.

receive-delay

The
                                          					 minimum delay that will be applied to the packets received when using an
                                          					 adaptive jitter buffer.

voice-quality-total-packet-loss

The total
                                          					 number of packets lost by the jitter buffer in the RTP stream.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature
                                          				  Information

Voice Quality Statistics

Cisco IOS XE Everest 16.5.1b

Voice quality statistics provides information about the quality of the voice TDM-IP call. This feature is already implemented
                                          on ISR-G2, and the feature gap is filled in ISR 4000 series.

Voice
                                          				  Quality Monitoring

Cisco IOS XE
                                          				  Denali 16.3.1

The Voice
                                          				  Quality Monitoring (VQM) feature provides information on the voice quality
                                          				  metrics related to media (voice) quality, such as conversational mean opinion
                                          				  score (MOS), packet loss rate, and so on. VQM enables you to monitor the
                                          				  quality of calls traversing your VoIP network, and you can diagnose the cause
                                          				  of voice quality issues and troubleshoot them.

## Prerequisites

The following
                           		commands must be executed to configure the voice quality metrics:

callmonitor

rtcp
                                 			 all-pass-through

media statistics

media bulk-stats

call-quality

max-dropout
                                       				  2

max-reorder
                                       				  2

## Restrictions

Only SIP-to-SIP
                                 			 call quality statistics calculation is supported.

The RTCP field
                                 			 is not recalculated, as it is end-to-end statistics.

The round trip
                                 			 delay is only retrieved by RTCP, which means the round trip delay is not
                                 			 calculated if there is no related RTCP.

Only three
                                 			 codec types are supported for one media flow to calculate the jitter;
                                 			 considering the data path performance, these three codecs would be the maximum
                                 			 number in one cache line.

Only one RTP
                                 			 synchronization source (SSRC) is supported concurrently per media flow, which
                                 			 is indicated in the m-line of the session description protocol (SDP).

Round trip
                                 			 delay calculation for transcoding calls is not supported.

VQM MOS values are not calculated for DSP based calls.

MOS value shows 0 if endpoint does not send RTCP packets.

The voice quality statistics covers only the TDM-IP call. The implementation focuses on filling the following statistics based
                                 on query response from DSP for TDM-SIP and TDM-H323 call:

RoundTripDelay

GapFillWithSilence

GapFillWithPrediction

GapFillWithInterpolation

GapFillWithRedundancy

HiWaterPlayoutDelay

LoWaterPlayoutDelay

PlayDelayJitter

## Configure Voice Quality Monitoring

### Enable Media Statistics Globally

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- media statistics

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

voice service voip

#### Example:

```
Device(config)# voice service voip
```

Enters  voice service VoIP configuration mode.

Step 4

media statistics

#### Example:

```
Device(conf-voi-serv)# media statistics
```

Enables media statistics to estimate the values of packet loss, jitter, and Round Trip Time
                                             (RTT) statistics.

The statistics are displayed using the show voice history and show call active voice commands.

If the media statistics command is disabled, the values will be zero.

Step 5

end

#### Example:

```
Device(conf-voi-serv)# end
```

Returns to privileged EXEC mode.

#### Example: Configuring Media Statistics Globally

```
Device> enable Device# configure terminal Device(config)# voice service voip Device(conf-voi-serv)# media statistics Device(conf-voi-serv)# end
```

#### Example: CDR
                              	 Enabled MOS Output

At the end of a
                                 		call, the MOSQe output is displayed in CDR only if the debug radius
                                       			 accounting is enabled.

The show log | sec
                                       			 MOS-Con command displays the MOS-Con value as shown below:

```
Device# show log | sec MOS-Con *Jan 21 22:31:42.313: RADIUS:   Cisco AVpair       [1]   16  " MOS-Con=4.2312 "
*Jan 21 22:31:42.313: RADIUS:   Cisco AVpair       [1]   16  " MOS-Con=4.2312 "
```

### Report End-of-Call Statistics

The reporting End-of-Call statistics in Session Initiation Protocol (SIP) BYE message feature enables you to send call statistics
                              to a remote end when a call terminates. The call statistics are sent as a new header in the BYE message or in the 200 OK message
                              (response to BYE message). The statistics include Real-time Transport Protocol (RTP) packets sent or received, total bytes
                              sent or received, total number of packets that are lost, delay jitter, round-trip delay, and call duration.

This feature enables Cisco Unified Border Element (Cisco UBE) to use the call statistics to update the call data records in
                              Cisco Unified Communications Manager (Cisco UCM) or Cisco Unified Communications Manager Express (Cisco UCME).

Use the media bulk-stats and media stats-disconnect commands in voice service voip configuration mode to enable reporting of RTP statistics during call disconnect in SIP BYE message feature on Cisco Unified
                              Border Element.

To disable reporting End-of-Call statistics in SIP BYE message at the global level, see Disabling Reporting End-of-Call Statistics in SIP BYE Message .

#### Enable End-of-Call Statistics Reporting in SIP BYE Message at the Global Level

Perform this task to enable the support for reporting End-of-Call statistics in SIP BYE message feature at the global level.

The support for reporting End-of-Call statistics in SIP BYE message feature is enabled by default on Cisco UBE. Hence, to
                                    disable the feature, you must modify the SIP profiles to remove the P-RTP-Stat SIP header from the request and the response
                                    messages and then configure the modified SIP profile on the Cisco UBE.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- media bulk-stats

- media stats-disconnect

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router>enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

##### Example:

```
Router#configure terminal
Router(config)#
```

Enters global configuration mode.

Step 3

voice service voip

##### Example:

```
Router(config)# voice servive voip
Router(conf-voi-serv)#
```

Specifies VoIP as the voice encapsulation method and enters voice-service configuration mode.

Step 4

media bulk-stats

##### Example:

```
Router(conf-voi-serv)#media bulk-stats
Router(conf-voi-serv)#
```

Enables a periodic process to retrieve bulk call statistics.

Step 5

media stats-disconnect

##### Example:

```
Router(conf-voi-serv)#media stats-disconnect
Router(conf-voi-serv)#
```

Enables RTP statistics reporting during call disconnect.

##### Example: Enable End-of-Call Statistics Reporting

```
Router>enable
Router#configure terminal
Router(config)# voice servive voip
Router(conf-voi-serv)#media bulk-stats
Router(conf-voi-serv)#media stats-disconnect
Router(conf-voi-serv)#
```

## Verify

Perform this task
                              		  to verify the configuration for voice quality monitoring. The show commands
                              		  can be entered in any order.

### SUMMARY STEPS

- enable

- show call active voice | include LostPackets

- show call active voice | include ReceiveDelay

- show call active voice brief | sec RTT

- show call active voice stats | sec MC

### DETAILED STEPS

Step 1

enable

Enables
                                          				privileged EXEC mode.

### Example:

```
Device> enable
```

Step 2

show call active voice | include LostPackets

Displays
                                          				statistics on the CUBE if the Voice Quality Metrics feature is configured.

### Example:

```
Device# show call active voice | include LostPackets LostPackets=0
LostPackets=0
```

Step 3

show call active voice | include ReceiveDelay

Displays
                                          				statistics on the CUBE if the Voice Quality Metrics feature is configured.

### Example:

```
Device# show call active voice | include ReceiveDelay ReceiveDelay=0
ReceiveDelay=0
```

Step 4

show call active voice brief | sec RTT

Displays a truncated version of call information for voice calls in CUBE if the Voice Quality Metrics feature is configured.

This command is not applicable for TDM-IP voice calls.

### Example:

```
Device# show call active voice brief | sec RTT IP 173.39.65.81:7078     SRTP: off  rtt:12ms pl:0/0ms  lost:0/0/0  delay:0/0/0ms   g711ulaw   TextRelay: off   Transcoded: No   ICE: Off
 IP 10.127.17.141:18920   SRTP: off  rtt:12ms pl:0/0ms  lost:0/0/0  delay:0/0/0ms   g711ulaw   TextRelay: off   Transcoded: No   ICE: Off
```

Step 5

show call active voice stats | sec MC

Displays
                                          				R-Factor Statistics (G.107 MOS) on the CUBE if the Voice Quality Metrics
                                          				feature is configured. A sample output is provided below for a voice call using
                                          				G.711ulaw, VAD on, and at 5 percent packet loss rate.

### Example:

```
Device# show call active voice stats | sec MC DSP/RF: ML=, MC=, R1=, R2=, IF=, ID=, IE=, BL=, R0=, VR=
DSP/RF: ML=4.2346, MC=4.2346 , R1=92, R2=92, IF=0, ID=0, IE=0, BL=0, R0=93, VR=2.0
DSP/RF: ML=4.2346, MC=4.2346 , R1=92, R2=92, IF=0, ID=0, IE=0, BL=0, R0=93, VR=2.0

The following is an example output for the SNMP MIB: cmqVoIPCallActiveRxPred107RMosConv.8520964.1 = 423 (MC)
```

For more
                                          				information on the SNMP MIB " cmqVoIPCallActiveRxPred107RMosConv ", see SNMP Object Navigator .

In the
                                          				sample output, the following can be noted:

ML for codec G.711ulaw is 4.2346.

MC for codec G.711ulaw is 4.2346.

IE for codec G.711 is 0.

R0 is 93.

The
                                          				following table defines the abbreviations used in the sample output.

Type

## Tips to Troubleshoot

Use the following debug commands to troubleshoot the Voice Quality
                           		Monitoring feature:

debug voip rtp packets

debug performance monitor

debug radius accounting

debug aaa accounting

| IOS VQM,
                                          					 Voice/Audio Description Quality Metric | Description |
|---|---|
| MOS-Con | The
                                          					 conversational quality MOS. Conversational quality indicates the impact of the
                                          					 quality of the transmission on the dynamics of conversational exchanges between
                                          					 two parties; such metrics take into account delay, echo, and recency. |
| round-trip-delay | The
                                          					 instantaneous round-trip delay. This may be obtained from the RTCP SR reports. |
| receive-delay | The
                                          					 minimum delay that will be applied to the packets received when using an
                                          					 adaptive jitter buffer. |
| voice-quality-total-packet-loss | The total
                                          					 number of packets lost by the jitter buffer in the RTP stream. |

| Feature Name | Releases | Feature
                                          				  Information |
|---|---|---|
| Voice Quality Statistics | Cisco IOS XE Everest 16.5.1b | Voice quality statistics provides information about the quality of the voice TDM-IP call. This feature is already implemented
                                          on ISR-G2, and the feature gap is filled in ISR 4000 series. |
| Voice
                                          				  Quality Monitoring | Cisco IOS XE
                                          				  Denali 16.3.1 | The Voice
                                          				  Quality Monitoring (VQM) feature provides information on the voice quality
                                          				  metrics related to media (voice) quality, such as conversational mean opinion
                                          				  score (MOS), packet loss rate, and so on. VQM enables you to monitor the
                                          				  quality of calls traversing your VoIP network, and you can diagnose the cause
                                          				  of voice quality issues and troubleshoot them. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Device(config)# voice service voip | Enters  voice service VoIP configuration mode. |
| Step 4 | media statistics Example: Device(conf-voi-serv)# media statistics | Enables media statistics to estimate the values of packet loss, jitter, and Round Trip Time
                                             (RTT) statistics. The statistics are displayed using the show voice history and show call active voice commands. If the media statistics command is disabled, the values will be zero. |
| Step 5 | end Example: Device(conf-voi-serv)# end | Returns to privileged EXEC mode. |

| Note | To disable reporting End-of-Call statistics in SIP BYE message at the global level, see Disabling Reporting End-of-Call Statistics in SIP BYE Message . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router>enable | Enables privileged EXEC mode. Note Enter your password if prompted. | Note | Enter your password if prompted. |
| Note | Enter your password if prompted. |
| Step 2 | configure terminal Example: Router#configure terminal
Router(config)# | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice servive voip
Router(conf-voi-serv)# | Specifies VoIP as the voice encapsulation method and enters voice-service configuration mode. |
| Step 4 | media bulk-stats Example: Router(conf-voi-serv)#media bulk-stats
Router(conf-voi-serv)# | Enables a periodic process to retrieve bulk call statistics. |
| Step 5 | media stats-disconnect Example: Router(conf-voi-serv)#media stats-disconnect
Router(conf-voi-serv)# | Enables RTP statistics reporting during call disconnect. |

| Note | Enter your password if prompted. |
|---|---|

| Step 1 | enable Enables
                                          				privileged EXEC mode. Example: Device> enable |
|---|---|
| Step 2 | show call active voice \| include LostPackets Displays
                                          				statistics on the CUBE if the Voice Quality Metrics feature is configured. Example: Device# show call active voice \| include LostPackets LostPackets=0
LostPackets=0 |
| Step 3 | show call active voice \| include ReceiveDelay Displays
                                          				statistics on the CUBE if the Voice Quality Metrics feature is configured. Example: Device# show call active voice \| include ReceiveDelay ReceiveDelay=0
ReceiveDelay=0 |
| Step 4 | show call active voice brief \| sec RTT Displays a truncated version of call information for voice calls in CUBE if the Voice Quality Metrics feature is configured. Note This command is not applicable for TDM-IP voice calls. Example: Device# show call active voice brief \| sec RTT IP 173.39.65.81:7078     SRTP: off  rtt:12ms pl:0/0ms  lost:0/0/0  delay:0/0/0ms   g711ulaw   TextRelay: off   Transcoded: No   ICE: Off
 IP 10.127.17.141:18920   SRTP: off  rtt:12ms pl:0/0ms  lost:0/0/0  delay:0/0/0ms   g711ulaw   TextRelay: off   Transcoded: No   ICE: Off | Note | This command is not applicable for TDM-IP voice calls. |
| Note | This command is not applicable for TDM-IP voice calls. |
| Step 5 | show call active voice stats \| sec MC Displays
                                          				R-Factor Statistics (G.107 MOS) on the CUBE if the Voice Quality Metrics
                                          				feature is configured. A sample output is provided below for a voice call using
                                          				G.711ulaw, VAD on, and at 5 percent packet loss rate. Example: Device# show call active voice stats \| sec MC DSP/RF: ML=, MC=, R1=, R2=, IF=, ID=, IE=, BL=, R0=, VR=
DSP/RF: ML=4.2346, MC=4.2346 , R1=92, R2=92, IF=0, ID=0, IE=0, BL=0, R0=93, VR=2.0
DSP/RF: ML=4.2346, MC=4.2346 , R1=92, R2=92, IF=0, ID=0, IE=0, BL=0, R0=93, VR=2.0

The following is an example output for the SNMP MIB: cmqVoIPCallActiveRxPred107RMosConv.8520964.1 = 423 (MC) For more
                                          				information on the SNMP MIB " cmqVoIPCallActiveRxPred107RMosConv ", see SNMP Object Navigator . In the
                                          				sample output, the following can be noted: ML for codec G.711ulaw is 4.2346. MC for codec G.711ulaw is 4.2346. IE for codec G.711 is 0. R0 is 93. The
                                          				following table defines the abbreviations used in the sample output. Table 3. Router Output Definitions for the show call active voice stats command Type Abbreviation Definition DSP/RF: R-Factor Statistics (G.107 MOS) ML R-factor MOS listening quality objective MC R-factor MOS-CQE R1 R-factor for LQ profile1 R2 R-factor for LQ IF Effective codec impairment (IeEff ) ID Delay factors IE Codec baseline score (Ie) BL Codec baseline (Bpl) R0 Nominal value for R0 (default) VR R-Factor version | Type | Abbreviation | Definition | DSP/RF: R-Factor Statistics (G.107 MOS) | ML | R-factor MOS listening quality objective | MC | R-factor MOS-CQE | R1 | R-factor for LQ profile1 | R2 | R-factor for LQ | IF | Effective codec impairment (IeEff ) | ID | Delay factors | IE | Codec baseline score (Ie) | BL | Codec baseline (Bpl) | R0 | Nominal value for R0 (default) | VR | R-Factor version |
| Type | Abbreviation | Definition |
| DSP/RF: R-Factor Statistics (G.107 MOS) | ML | R-factor MOS listening quality objective |
| MC | R-factor MOS-CQE |
| R1 | R-factor for LQ profile1 |
| R2 | R-factor for LQ |
| IF | Effective codec impairment (IeEff ) |
| ID | Delay factors |
| IE | Codec baseline score (Ie) |
| BL | Codec baseline (Bpl) |
| R0 | Nominal value for R0 (default) |
| VR | R-Factor version |

| Note | This command is not applicable for TDM-IP voice calls. |
|---|---|

| Type | Abbreviation | Definition |
|---|---|---|
| DSP/RF: R-Factor Statistics (G.107 MOS) | ML | R-factor MOS listening quality objective |
| MC | R-factor MOS-CQE |
| R1 | R-factor for LQ profile1 |
| R2 | R-factor for LQ |
| IF | Effective codec impairment (IeEff ) |
| ID | Delay factors |
| IE | Codec baseline score (Ie) |
| BL | Codec baseline (Bpl) |
| R0 | Nominal value for R0 (default) |
| VR | R-Factor version |