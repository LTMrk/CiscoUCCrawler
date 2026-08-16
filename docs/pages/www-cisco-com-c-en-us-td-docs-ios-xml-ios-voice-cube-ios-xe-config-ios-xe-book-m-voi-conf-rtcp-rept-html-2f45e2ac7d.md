---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-conf-rtcp-rept-html-2f45e2ac7d
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-conf-rtcp-rept.html
retrieved_at: 2026-08-16T15:51:27.857153+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Configure Report Generation

## Chapter: Configure Report Generation

# Configure Report Generation

## Overview

The assisted Real-time Transport Control Protocol (RTCP) feature adds the ability for Cisco Unified Border Element (CUBE) to generate standard RTCP keepalive reports on behalf of endpoints. RTCP reports determine the liveliness of a media session
                           during prolonged periods of silence, such as call hold or mute. Therefore, it is important for the CUBE to generate RTCP reports irrespective of whether the endpoints send or receive media.

H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Assisted RTCP

Baseline Functionality

The following commands were introduced or modified in this release: rtcp keepalive , debug voip rtcp , debug voip rtp , debug ip rtp protocol , and ip rtcp report interval .

## Prerequisites

### Cisco Unified Border Element

Cisco IOS Release 15.1(2)T or a later release must be installed and running on your Cisco Unified Border Element.

### Cisco Unified Border Element (Enterprise)

Cisco IOS XE Release 3.17S or a later release must be installed and running on your Cisco ASR 1000 Series Router and Cisco
                                    ISR 4000 Series Router.

## Restrictions

RTCP report generation over IPv6 is not supported.

RTCP report generation is not supported for Secure Real-time Transport Protocol (SRTP) or SRT Control Protocol (SRTCP) pass-through
                                 as CUBE is not aware of the media encryption or decryption keys.

RTCP report generation is not supported for loopback calls, T.38 fax, and modem relay calls.

RTCP or SRTCP report generation is not supported when CUBE inserts a Digital Signal Processor (DSP) for RTP-SRTP interworking on RTP and SRTP call legs.

RTCP report generation is not supported when there is a call hold with an invalid media address such as 0.0.0.0 in Session
                                 Description Protocol (SDP) or Open Logical Channel (OLC).

RTCP report generation is not supported for RTCP multiplexed with RTP on the same address and port.

RTCP report generation is not supported on enterprise aggregation services routers (ASRs) and 4000 series integrated services
                                 routers (ISRs) when Media Termination Points are collocated with the CUBE . It affects RFC2833 and RFC4733 DTMF generation when MTP is used for DTMF conversion from Out-of-Band (OOB) to RFC2833 or
                                 RFC4733.

## Configure RTCP Report Generation

RTCP keepalive packets indicate session liveliness. When configured on CUBE , RTCP keepalive packets are sent on both inbound and outbound SIP call legs.

Perform this task to configure RTCP report generation on CUBE .

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- allow-connections from-type to to-type

- rtcp keepalive

- end

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

voice service voip

### Example:

```
Router(config)# voice service voip
```

Enters voice service configuration mode.

Step 4

allow-connections from-type to to-type

### Example:

```
Router(conf-voi-serv)# allow-connections sip to sip
```

Allows connections between SIP endpoints in a VoIP network.

Step 5

rtcp keepalive

### Example:

```
Router(conf-voi-serv)# rtcp keepalive
```

Configures RTCP keepalive report generation.

Step 6

end

### Example:

```
Router(conf-voi-serv)# end
```

Exits voice service configuration mode and returns to privileged EXEC mode.

## Troubleshooting Tips

Use the following debug commands for debugging related to RTCP keepalive packets:

debug voip rtcp packet --Shows details related to RTCP keepalive packets such as RTCP sending and receiving paths, Call ID, Globally Unique Identifier
                                 (GUID), packet header, and so on.

```
Router# debug voip rtcp packet 01:06:27.450: //6/xxxxxxxxxxxx/RTP//Event/voip_rtp_send_rtcp_keepalive: Generate RTCP Keepalive
*Mar 17 01:06:27.450: rtcp_send_report: Attributes
        (src ip=192.168.30.3, src port=17101, dst ip=192.168.30.4, dst port=18619
         bye=0, initial=1, ssrc=0x07111E02, keepalive=1)
*Mar 17 01:06:27.450: rtcp_construct_keepalive_report: Constructed Report
        (rtcp=0x2E5AF214, ssrc=0x07111E02, source->ssrc=0x00001E03, total_len=36)
2E5AF210:          80C90001 07111E02 81CA0006      .I.......J..
2E5AF220: 07111E02 010F302E 302E3040 392E3435  ......0.0.0@9.45
2E5AF230: 2E33302E 33000000 00                 .30.3....
```

Caution

Under moderate traffic loads, the debug voip rtp packet command produces a high volume of output and the command should be enabled only when the call volume is very low.

debug voip rtp packet --Shows details about VoIP RTP packet debugging trace.

```
Router# debug voip rtp packet VOIP RTP All Packets debugging is on
```

debug voip rtp session --Shows all RTP session debug information.

```
Router# debug voip rtp session VOIP RTP All Events debugging is on
```

debug voip rtp error --Shows details about debugging trace for RTP packet error cases.

```
Router# debug voip rtp error VOIP RTP Errors debugging is on
```

debug ip rtp protocol --Shows details about RTP protocol debugging trace.

```
Router# debug ip rtp protocol RTP protocol debugging is on
```

debug voip rtcp session --Shows all RTCP session debug information.

```
Router# debug voip rtcp session VOIP RTCP Events debugging is on
```

debug voip rtcp error -- Shows details about debugging trace for RTCP packet error cases.

```
Router# debug voip rtcp error VOIP RTCP Errors debugging is on
```

| Note | H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications. |
|---|---|

| Feature Name | Releases | Feature Information |
|---|---|---|
| Assisted RTCP | Baseline Functionality | The following commands were introduced or modified in this release: rtcp keepalive , debug voip rtcp , debug voip rtp , debug ip rtp protocol , and ip rtcp report interval . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service configuration mode. |
| Step 4 | allow-connections from-type to to-type Example: Router(conf-voi-serv)# allow-connections sip to sip | Allows connections between SIP endpoints in a VoIP network. |
| Step 5 | rtcp keepalive Example: Router(conf-voi-serv)# rtcp keepalive | Configures RTCP keepalive report generation. |
| Step 6 | end Example: Router(conf-voi-serv)# end | Exits voice service configuration mode and returns to privileged EXEC mode. |

| Caution | Under moderate traffic loads, the debug voip rtp packet command produces a high volume of output and the command should be enabled only when the call volume is very low. |
|---|---|