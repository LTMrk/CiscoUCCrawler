---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cube-call-quality-statistics-html-c2526e2b0e
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-cube-call-quality-statistics.html
retrieved_at: 2026-08-16T15:54:11.460104+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Call Quality Statistics

## Chapter: Call Quality Statistics

# Call Quality Statistics

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

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Call Quality Statistics Enhancement

Cisco IOS XE 3.14S

Call quality statistics in CUBE, such as packet loss, jitter,
                                             					 and round trip delay can be added to the call detail record (CDR), and these
                                             					 voice metrics can be calculated in IOS. For more information, refer to Voice Quality Enhancements on Cisco Unified Border
                                                						Element .

The call quality statistics feature is enhanced to provide
                                             					 the following capabilities:

Enable or disable Quality of Service (QoS) for CUBE.

Enable or disable Real-time Transport Protocol (RTP)
                                                   						  Control Protocol (RTCP) passthrough.

Configure call quality criteria parameters.

## Restrictions

Only SIP-to-SIP call quality
                                 			 statistics calculation is supported.

The RTCP field is not recalculated, as it is end-to-end statistics.

The round trip delay is only retrieved by RTCP, which means the
                                 			 round trip delay is not calculated if there is no related RTCP.

Only three codec types are supported for one media flow to
                                 			 calculate the jitter; considering the data path performance, these three codecs
                                 			 would be the maximum number in one cache line.

Only one RTP synchronization source (SSRC) is supported
                                 			 concurrently per media flow, which is indicated in the m-line of the session
                                 			 description protocol (SDP).

Round trip delay calculation for transcoding calls is not
                                 			 supported.

## Configure Call Quality Parameters

### Configure Call Quality Criteria Parameters

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- call-quality

- max-dropout number-of-packets

- max-reorder number-of-packets

- clock-rate payload-type-number frequency

- clock-rate dynamic-default frequency

- exit

- rtcp all-pass-through

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables
                                             				privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice service voip

#### Example:

```
Device(config)# voice service voip
```

Enters global
                                             				VoIP configuration mode.

Step 4

call-quality

#### Example:

```
Device(conf-voi-serv)# call-quality
```

Enters call
                                             				quality configuration mode; this is the global call quality of service setup.

Step 5

max-dropout number-of-packets

#### Example:

```
Device(conf-serv-call-quality)# max-dropout 300
```

Configures the
                                             				acceptable out of sequence future packets to drop. The range is from 2 to 2000
                                             				packets. The default value is 100.

Step 6

max-reorder number-of-packets

#### Example:

```
Device(conf-serv-call-quality)# max-reorder 500
```

Configures the
                                             				acceptable out of sequence late packets. The range is from 2 to 2000 packets.
                                             				The default value is 100.

Step 7

clock-rate payload-type-number frequency

#### Example:

```
Device(conf-serv-call-quality)# clock-rate 5 1500
```

Sets the
                                             				payload type number and frequency. Clock rate is the RTP timestamp field's
                                             				sampling frequency.

Step 8

clock-rate dynamic-default frequency

#### Example:

```
Device(conf-serv-call-quality)# clock-rate dynamic-default 10000
```

(Optional)
                                             				Changes the default clock rate for all the dynamic payload types. The frequency
                                             				range (in Hz) is from 1000 to 192000.

You have
                                                   					 several options to set the clock rate, such as for the different codecs.

Step 9

exit

#### Example:

```
Device(conf-serv-call-quality)# exit
```

Exits to
                                             				global VoIP configuration mode.

Step 10

rtcp all-pass-through

#### Example:

```
Device(conf-voi-serv)# rtcp all-pass-through
```

(Optional)
                                             				Passes through all RTCP in data path.

Step 11

end

#### Example:

```
Device(conf-voi-serv)# end
```

Returns to
                                             				privileged EXEC mode.

### Tips to Troubleshoot

Use the following debug and show commands
                              		to enable the logs, which helps in debugging:

debug ccsip verbose

debug voip fpi all

debug platform hardware qfp
                                       				active feature sbc dbe datapath all

debug platform hard qfp act
                                       				feature sbc dbe client all

debug ccsip message

debug ccsip info

show call active voice

show platform hardware qfp
                                       				active feature sbc data path call call-id

The following are some show command outputs that would be useful in
                              		troubleshooting:

Device# show call active voice | include
                                       				LostPackets

LostPackets=0

LostPackets=36 ---->// Lost packets detail present in show call active voice output. View the complete command output
                                 		  based on the filters such as call-id to check the packet loss for a particular
                                 		  call leg. //

Device# show call active voice | include
                                       				PlayDelayJitter

PlayDelayJitter=0

PlayDelayJitter=38 ----->// Jitter detail present in show call active voice output. View the complete command output
                                 		  based on the filters such as call-id to check the Jitter for a particular call
                                 		  leg. //

## Configuration
                        	 Example for Call Quality Statistics

```
voice service voip
 no ip address trusted authenticate
 callmonitor
 rtcp all-pass-through
 media statistics
 media bulk-stats
 allow-connections sip to sip
 call-quality
  max-dropout 2
  max-reorder 2
 sip
  g729 annexb-all
  no call service stop
```

| Feature Name | Releases | Feature Information |
|---|---|---|
| Call Quality Statistics Enhancement | Cisco IOS XE 3.14S | Call quality statistics in CUBE, such as packet loss, jitter,
                                             					 and round trip delay can be added to the call detail record (CDR), and these
                                             					 voice metrics can be calculated in IOS. For more information, refer to Voice Quality Enhancements on Cisco Unified Border
                                                						Element . The call quality statistics feature is enhanced to provide
                                             					 the following capabilities: Enable or disable Quality of Service (QoS) for CUBE. Enable or disable Real-time Transport Protocol (RTP)
                                                   						  Control Protocol (RTCP) passthrough. Configure call quality criteria parameters. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice service voip Example: Device(config)# voice service voip | Enters global
                                             				VoIP configuration mode. |
| Step 4 | call-quality Example: Device(conf-voi-serv)# call-quality | Enters call
                                             				quality configuration mode; this is the global call quality of service setup. |
| Step 5 | max-dropout number-of-packets Example: Device(conf-serv-call-quality)# max-dropout 300 | Configures the
                                             				acceptable out of sequence future packets to drop. The range is from 2 to 2000
                                             				packets. The default value is 100. |
| Step 6 | max-reorder number-of-packets Example: Device(conf-serv-call-quality)# max-reorder 500 | Configures the
                                             				acceptable out of sequence late packets. The range is from 2 to 2000 packets.
                                             				The default value is 100. |
| Step 7 | clock-rate payload-type-number frequency Example: Device(conf-serv-call-quality)# clock-rate 5 1500 | Sets the
                                             				payload type number and frequency. Clock rate is the RTP timestamp field's
                                             				sampling frequency. |
| Step 8 | clock-rate dynamic-default frequency Example: Device(conf-serv-call-quality)# clock-rate dynamic-default 10000 | (Optional)
                                             				Changes the default clock rate for all the dynamic payload types. The frequency
                                             				range (in Hz) is from 1000 to 192000. You have
                                                   					 several options to set the clock rate, such as for the different codecs. |
| Step 9 | exit Example: Device(conf-serv-call-quality)# exit | Exits to
                                             				global VoIP configuration mode. |
| Step 10 | rtcp all-pass-through Example: Device(conf-voi-serv)# rtcp all-pass-through | (Optional)
                                             				Passes through all RTCP in data path. |
| Step 11 | end Example: Device(conf-voi-serv)# end | Returns to
                                             				privileged EXEC mode. |