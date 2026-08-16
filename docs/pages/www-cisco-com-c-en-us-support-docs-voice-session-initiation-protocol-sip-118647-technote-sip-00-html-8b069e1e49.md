---
doc_id: www-cisco-com-c-en-us-support-docs-voice-session-initiation-protocol-sip-118647-technote-sip-00-html-8b069e1e49
source_url: https://www.cisco.com/c/en/us/support/docs/voice/session-initiation-protocol-sip/118647-technote-sip-00.html
retrieved_at: 2026-08-16T23:25:00.665326+00:00
---

Fax-SIP Troubleshoot Guide

# Fax-SIP Troubleshoot Guide

Updated: January 14, 2015

Document ID: 118647

Contents

## Contents

## Introduction

This document describes one of the most effective approaches to troubleshoot fax, which includes these steps:

- Split the call into two legs.

- Identify the protocol (SIP/H.323/SCCP/MGCP) on each leg.

- Choose a leg and then check if the call is incoming or outgoing on that leg and if the gateway/endpoint associated is a terminating gateway (TGW) or originating gateway (OGW) correspondingly.

You can split a fax call into four parts:

- Off-hook, Dial, Ring, Answer

- Calling (CNG) and Called Equipment Identification (CED) Tones

- Codec upspeed/correction

- Voice Activation Detection (VAD) disabled on DSP

- Jitter buffer transitions from adaptive to a fixed optimum value

- Fax Terminal Identification

- Capabilities exchange and setting

- Training

- Transmission of pages

- Error detection and correction (ECM)

- End of message and page confirmation

- Call Disconnect, On-hook

This call flow includes the messages to look for when Session Initiation Protocol (SIP) is the protocol identified. There are corresponding sections based on whether your endpoint is a TGW or OGW.

Note : In the table in the next section, both T.38 Relay and Passthrough were tested simultaneously and differences between G3 and SG3 have been pointed out.

## TGW - Fax Call Incoming on SIP Leg

Note that:

- T.38 - Delay<1000ms, Jitter<300ms, Packet loss should be NONE unless T.38 with redundancy.

- Passthrough - Delay<1000ms, Jitter<30ms, Packet loss should be NONE.

- Protocol Based switchover - This is standard based.

- NSE Based switchover - This is proprietary and works only between Cisco voice gateways.

GW-------------------------CUCM/GW <-------------INVITE-------------------- ------------100TRYING--------------> ------------180RINGING------------>

Check for VTSP shows :

Fax Relay=DISABLED - 'fax rate disabled' set (dial-peer) Primary Fax Protocol=IGNORE_FAX_RELAY, Fallback Fax Protocol=IGNORE_FAX_RELAY Fax Relay CM Suppression :=ENABLED , Fax Relay ANS Suppression :=DISABLED

GW-------------------------CUCM/GW <-------------INVITE-------------------- ------------100TRYING--------------> ------------180RINGING------------>

Check for VTSP shows:

Fax Relay=ENABLED Primary Fax Protocol=T38_FAX_RELAY, Fallback Fax Protocol=NONE_FAX_RELAY Fax Relay CM Suppression :=ENABLED, Fax Relay ANS Suppression :=DISABLED

Protocol Based

NSE Based

Protocol Based

NSE Based

GW------CUCM/GW

---200OK+SDP----->

v=0 o=CiscoSystemsSIP-GW-UserAgent 0 6060 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 17924 RTP/AVP 0 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=ptime:20

<----ACK+SDP-----

v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=ptime:20

Note : In case of EO, a similar SDP would have been received with INVITE.

GW---------CUCM/GW

------200OK+SDP------>

v=0 o=CiscoSystemsSIP- GW-UserAgent 5944 7031 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 18806 RTP/AVP 0 100 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194,200-202 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap:100 X-NSE/8000 a=X-cpar: a=fmtp:100 192-194,200-202 a=X-cap: 2 image udptl t38

<------ACK+SDP--------

v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.4 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194,200-202 a=rtpmap:101 telephone-event/8000 a=fmtp:101 0-16 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap:100 X-NSE/8000 a=X-cpar: a=fmtp:100 192-194,200-202 a=X-cap: 2 image udptl t38

Note : In case of EO, a similar SDP would have been received with INVITE.

GW------------CUCM/GW

-------200OK+SDP-------->

<-------ACK+SDP---------

v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=ptime:20

Note : In case of EO, a similar SDP would have been received with INVITE.

GW------CUCM/GW

-----200OK+SDP---->

v=0 o=CiscoSystemsSIP- GW-UserAgent 5944 7031 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 18806 RTP/AVP 0 100 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194, 200-202 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap:100 X-NSE/8000 a=X-cpar: a=fmtp:100 192-194,200-202 a=X-cap: 2 image udptl t38

<-----ACK+SDP------

v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194, 200-202 a=rtpmap:101 telephone-event/8000 a=fmtp:101 0-16 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap:100 X-NSE/8000 a=X-cpar: a=fmtp:100 192-194,200-202 a=X-cap: 2 image udptl t38

Note : In case of EO, a similar SDP would have been received with INVITE.

GW-------------------------CUCM/GW

<========AUDIO==========>

Audio call established at this stage, but as the fax machines talk they start to exchange tones in the audio call.

Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.)

G3 FAX:

<<<<<<<<<<CNG<<<<<<<<<<<

1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal.

>>>>>>>>>>CED>>>>>>>>>>>

2100 Hz tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path.

SG3 FAX: <<<<<<<<<<CNG<<<<<<<<<<<

1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal.

>>>>>>>>>>ANSAM>>>>>>>>>

2100 Hz tone as CED, but amplitude modulated by a sine wave at 15 Hz with phase reversal every 450 ms.

<<<<<<<<<< CM <<<<<<<<<<<<

>>>>>>>>>> JM >>>>>>>>>>>>

<<<<<<<<<< CJ <<<<<<<<<<<<

V.34 Initialization (Phases 2-4)

The TGW waits to detect V.21 Preamble in the tones. It finds it in CED tone (G3) or ANSAM (SG3). Once it detects the V.21 Flag, it initiates switchover.

Check for VTSP shows:

Event=E_DSMP_DSP_MODEM_TONE

One of the tasks in switchover is to make the Jitter buffer transitions from adaptive to a fixed optimum value.

Fax passthrough uses the last voice mode setting before the switchover for jitter or playout buffers. Enter the show voice port X/X/X command in order to check the current values of playout delay.

GW-------------------------CUCM/GW

<========AUDIO==========>

Audio call established at this stage, but as the fax machines talk they start to exchange tones in the audio call.

Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.)

G3 FAX:

<<<<<<<<<<CNG<<<<<<<<<<<

1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal.

>>>>>>>>>>CED>>>>>>>>>>>

2100 Hz tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path.

SG3 FAX: <<<<<<<<<<CNG<<<<<<<<<<<

1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal.

>>>>>>>>>>ANSAM>>>>>>>>>

2100 Hz tone as CED, but amplitude modulated by a sine wave at 15 Hz with phase reversal every 450 ms.

No V.34 Initialization (Phases 2-4) exists, the initial V.8 Phase I also does not complete. OGW squelchs the CM tone and as SG3 is backward compatible with G3 fax standard, the FAX machines failover to G3.

>>>>>>>>>CED>>>>>>>>>>>

2100 Hz tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path.

The TGW waits to detect V.21 Preamble in the tones. It finds it in CED tone (G3) or ANSAM (SG3). Once it detects the V.21 Flag, it initiates switchover.

Check for VTSP shows:

VTSP: Event=E_DSMP_DSP_FAX_TONE

Check for DSMP shows: E_DSM_CC_MC_START

Check for CCAPI shows: CCAPI:Caps(Codec=T38Fax(0x10000), Fax Rate=FAX_RATE_14400(0x80),Fax Version:=0, Vad=OFF(0x1),

One of the tasks in switchover is to make the Jitter buffer transitions from adaptive to a fixed optimum value.

T.38 uses 300 ms fixed jitter or playout buffers. Enter the playout-delay fax 100 command under voice port in order to reduce the buffer time if the delay is high. Enter the show voice port X/X/X command in order to check the current values of playout delay.

Protocol Based

NSE Based

Protocol Based

NSE Based

GW------CUCM/GW

---INVITE+SDP---->

v=0 o=CiscoSystemsSIP-GW-UserAgent 0 6060 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 17924 RTP/AVP 0 c=IN IP4 209.165.201.2

a=rtpmap:0 PCMU/8000 a=silenceSupp:off - - - -

<----100TRYING----

<--200OK+SDP-----

v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=silenceSupp:off - - - -

--------ACK---------->

show call active voice brief will not show change

G3 FAX:

GW----------CUCM/GW

====NSE192======>

Upspeed Codec and Switch to Passthrough Mode.

Check for VTSP shows:

E_DSM_CC_MODIFY _MEDIA_IND

debug voip rtp session named event :

Pt:100    Evt:192     Pkt:00 00 00  <Snd>>>

<====NSE192=======

Check for VTSP shows:

E_DSMP_DSP_REPORT _PEER_TO_PEER

_MSG

debug voip rtp session named event :

<<<Rcv> Pt:100    Evt:192     Pkt:00 00 00

SG3 FAX:

GW----------CUCM/GW

====NSE192=====>

Upspeed Codec and Switch to Passthrough Mode.

Check for VTSP shows:

E_DSM_CC_MODIFY _MEDIA_IND

debug voip rtp session named event :

Pt:100    Evt:192    Pkt:00 00 00  <Snd>>>

<====NSE192======

Check for VTSP shows:

E_DSMP_DSP_REPORT _PEER_TO_PEER

_MSG

debug voip rtp session named event :

<<<Rcv> Pt:100    Evt:192     Pkt:00 00 00

=====NSE193=====>

Detect phase reversal of ANSam Disable ECAN.

Check for VTSP shows:

E_DSM_CC_MODIFY_ MEDIA_IND

debug voip rtp session named event :

Pt:100    Evt:193     Pkt:00 00 00  <Snd>>>

<====NSE193======

Check for VTSP shows:

E_DSMP_DSP_REPORT _PEER_TO_PEER

_MSG

debug voip rtp session named event :

<<<Rcv> Pt:100    Evt:193     Pkt:00 00 00

Note : NSE-194 is triggered by a local detection of 4 seconds of silence or carrier loss detection. This message instructs the remote gateway to return to voice mode. Basically, all the changes made by NSE-192 and NSE-193 are undone.

show call active voice brief shows: MODEMPASS nse

GW-------------CUCM/GW

-------INVITE+SDP------>

v=0 o=CiscoSystemsSIP-GW-UserAgent 0 6061 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=image 17924 udptl t38 c=IN IP4 209.165.201.2 a=T38FaxVersion:0 a=T38MaxBitRate:14400 a=T38FaxFillBitRemoval:0 a=T38FaxTranscoding MMR:0 a=T38FaxTranscodingJ BIG:0 a=T38FaxRate Management: transferredTCF a=T38FaxMaxBuffer:200 a=T38FaxMax Datagram:320 a=T38FaxUdpEC: t38UDPRedundancy

<--------100TRYING------

<-----200OK+SDP---------

v=0 o=CiscoSystemsCCM -SIP 2000 2 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=image 16384 udptl t38

-----------ACK------------->

show call active voice brief shows: t38

G3 FAX:

GW------CUCM/GW

====NSE200====>

Transition from voice mode to T.38

Check for VTSP shows

E_DSM_CC_ MODIFY _MEDIA_IND

debug voip rtp session named event :

Pt:100    Evt:200     Pkt:00 00 00  <Snd>>>

<===NSE201=====

T.38 ACK received, instructs TGW to start T.38 session.

Check for VTSP shows:

E_DSMP_DSP_ REPORT_PEER_ TO_PEER

_MSG

debug voip rtp session named event :

<<<Rcv> Pt:100    Evt:201     Pkt:00 00 00

SG3 FAX:

As you spoof SG3 to G3 by squelching the CM tone, there is no SG3 FAX scenario in T38 relay.

Note : NSE-202 is a NACK to an NSE-200 message that signifies that the peer gateway cannot process T.38 packets for the call. The call remains in voice mode and does not switch over to T.38.

show call active voice brief shows:

t38

In Passthrough you cannot see any T.30 messages from debugs as all tones go in the RTP-like audio with G711ulaw/alaw. However, the fax tone negotiation remains the same irrespective of relay or passthrough.

GW-------------------------CUCM/GW

>>>>>>>>> CSI>>>>>>>>>>>         (optional) (called subscriber identification) >>>>>>>>> NSF>>>>>>>>>>>        (optional) (nonstandard facilities) >>>>>>>>> DIS>>>>>>>>>>> (digital identification signal) <<<<<<<<<TSI<<<<<<<<<<<         (optional) (transmitting subscriber identification) <<<<<<<<<DCS<<<<<<<<<< (digital command signal) <++++++++++TCF++++++++++ (high speed) (training check) >>>>>>>>>>>CFR>>>>>>>>>> (confirmation to receive)

If you see FTT here that means TCF training failed. Check the clocking and slips on T1/E1. In packet captures, check TCF should be all 0. <++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOM<<<<<<<< (partial page sent)/(end of message)

>>>>>>>>> MCF>>>>>>>>>>> (message confirmation)

<++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOP<<<<<<<< (partial page sent)/(end of procedure)

>>>>>>>>> MCF>>>>>>>>>>> (message confirmation)

<<<<<<<<<<DCN<<<<<<<<<< (disconnect)

Note : ECM is Optional for G3, but Mandatory for SG3.  As you can achieve SG3 speeds with passthrough, make sure ECM is enabled on the fax machines for the fax to succeed. Also, TCF training signal is Required for G3, but is not applicable for SG3.

Note : For Passthrough, a common channel of 64kbps (g711) is allocated. So, the higher and the lower speeds of the messages becomes irrelevant.

If T38 switchover is successful, these messages are seen in the corresponding debugs:

Check for VTSP shows: event:E_CC_T38_START

Check for DSMP shows: E_DSM_CC_MC_LOCAL_DNLD_DONE

Check for CCAPI shows: Caps(Codec=T38Fax(0x10000), Fax Rate=FAX_RATE_14400(0x80), Fax Version:=0, Vad=OFF(0x1),

debug fax relay t30 all-level-1 : timestamp=1321430729 fr-msg-det NSF timestamp=1321431129 fr-msg-det CSI timestamp=1321431879 fr-msg-det DIS timestamp=1321435719 fr-msg-tx TSI timestamp=1321436329 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321436329 fr-msg-tx good crc, 0 bytes timestamp=1321436439 fr-msg-tx DCS timestamp=1321436619 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321441499 fr-msg-det CFR timestamp=1321461449 fr-msg-tx PPS timestamp=1321461639 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321463099 fr-msg-det MCF timestamp=1321466789 fr-msg-tx DCN timestamp=1321466869 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321466869 fr-msg-tx good crc, 0 bytes

GW-------------------------CUCM/GW

>>>>>>>>> CSI>>>>>>>>>>>         (optional) (called subscriber identification) >>>>>>>>> NSF>>>>>>>>>>>        (optional) (nonstandard facilities) >>>>>>>>> DIS>>>>>>>>>>> (digital identification signal) <<<<<<<<<TSI<<<<<<<<<<<         (optional) (transmitting subscriber identification) <<<<<<<<<DCS<<<<<<<<<< (digital command signal) <++++++++++TCF++++++++++ (high speed) (training check) >>>>>>>>>>>CFR>>>>>>>>>> (confirmation to receive)

If you see FTT here that means TCF, training failed, check clocking and slips on T1/E1. In packet captures check TCF should be all 0. <++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOM<<<<<<<< (partial page sent)/(end of message)

>>>>>>>>> MCF>>>>>>>>>>> (message confirmation)

<++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOP<<<<<<<< (partial page sent)/(end of procedure)

>>>>>>>>> MCF>>>>>>>>>>> (message confirmation)

<<<<<<<<<<DCN<<<<<<<<<< (disconnect)

Protocol Based

NSE Based

Protocol Based

NSE Based

DP level config:

## fax protocol pass-through g711ulaw/g711alaw

## fax rate disable

## fax nsf 000000

DP level config:

## modem passthrough nse codec g711ulaw/g711alaw

## fax rate disable

## fax nsf 000000

DP level config:

## fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback none

## fax nsf 000000 ## fax-relay ecm disable ## fax-relay sg3-to-g3 system ## fax rate 14400

DP level config:

## fax protocol t38 nse force version 0 ls-redundancy 0 hs-redundancy 0 fallback none

## OGW - FAX Call Outgoing on SIP Leg

Note that:

- T.38 - Delay<1000ms, Jitter<300ms, Packet loss should be NONE unless T.38 with redundancy.

- Passthrough - Delay<1000ms, Jitter<30ms, Packet loss should be NONE.

- Protocol Based switchover - This is standard based.

- NSE Based switchover - This is proprietary and works only between Cisco voice gateways.

Passthrough

T.38 Relay

GW-------------------------CUCM/GW -------------INVITE--------------------> <------------100TRYING-------------- <------------180RINGING-------------

Check for VTSP shows: Fax Relay=DISABLED - 'fax rate disabled' set (dial-peer) Primary Fax Protocol=IGNORE_FAX_RELAY, Fallback Fax Protocol=IGNORE_FAX_RELAY Fax Relay CM Suppression :=ENABLED, Fax Relay ANS Suppression :=DISABLED

GW-------------------------CUCM/GW -------------INVITE--------------------> <------------100TRYING-------------- <------------180RINGING-------------

Check for VTSP shows: Fax Relay=ENABLED Primary Fax Protocol=T38_FAX_RELAY, Fallback Fax Protocol=NONE_FAX_RELAY Fax Relay CM Suppression :=ENABLED, Fax Relay ANS Suppression :=DISABLED

Protocol Based

NSE Based

Protocol Based

NSE Based

GW------CUCM/GW

<----200OK+SDP----

v=0 o=CiscoSystemsSIP-GW-UserAgent 0 6060 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 17924 RTP/AVP 0 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=ptime:20

-----ACK+SDP----->

v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=ptime:20

Note : In case of EO, a similar SDP would have been sent in INVITE.

GW----------CUCM/GW

<-----200OK+SDP------

v=0 o=CiscoSystemsSIP -GW-UserAgent 5944 7031 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 18806 RTP/AVP 0 100 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194, 200-202 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap: 100 X-NSE/8000 a=X-cpar: a=fmtp:100 192-194, 200-202 a=X-cap: 2 image udptl t38

-------ACK+SDP------->

v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.4 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194, 200-202 a=rtpmap:101 telephone-event/8000 a=fmtp:101 0-16 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap:100 X-NSE/8000 a=X-cpar: a=fmtp:100 192-194,200-202 a=X-cap: 2 image udptl t38

Note : In case of EO, a similar SDP would have been sent in INVITE.

GW----------CUCM/GW

<------200OK+SDP------

--------ACK+SDP------>

v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=ptime:20

Note : In case of EO, a similar SDP would have been sent in INVITE.

GW--------CUCM/GW

<-----200OK+SDP-----

v=0 o=CiscoSystemsSIP -GW-UserAgent 5944 7031 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 18806 RTP/AVP 0 100 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194, 200-202 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap:100 X-NSE/8000 a=X-cpar: a=fmtp:100 192-194,200-202 a=X-cap: 2 image udptl t38

-------ACK+SDP------>

v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194, 200-202 a=rtpmap:101 telephone-event/8000 a=fmtp:101 0-16 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap: 100 X-NSE/8000 a=X-cpar: a=fmtp: 100 192-194,200-202 a=X-cap: 2 image udptl t38

Note : In case of EO, a similar SDP would have been sent in INVITE.

GW-------------------------CUCM/GW

<========AUDIO==========>

Audio call established at this stage, but as FAX machines talk, they exchange tones in the audio call.

Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.)

G3 FAX:

>>>>>>>>>> CNG >>>>>>>>>>>

1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal.

<<<<<<<<<< CED <<<<<<<<<<<

2100 Hz tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path.

SG3 FAX: >>>>>>>>>> CNG >>>>>>>>>>>

1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal.

<<<<<<<<<< ANSAM <<<<<<<<

2100 Hz tone as CED, but amplitude modulated by a sine wave at 15Hz with phase reversal every 450 ms.

>>>>>>>>>> CM >>>>>>>>>>>>

<<<<<<<<<< JM <<<<<<<<<<< <

>>>>>>>>>> CJ >>>>>>>>>>>>

V.34 Initialization (Phases 2-4)

The OGW waits for the terminating gateway to detect V.21 Preamble in the tones. Once TGW detects the V.21 Flag, it initiates switchover.

One of the tasks in switchover is to make the Jitter buffer transitions from adaptive to a fixed optimum value.

Fax passthrough uses the last voice mode setting before the switchover for jitter or playout buffers. Enter the show voice port X/X/X command in order to check the current values of playout delay.

GW-------------------------CUCM/GW

<========AUDIO==========>

Audio call established at this stage, but as FAX machines talk, they exchange tones in the audio call.

Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.)

G3 FAX:

>>>>>>>>>> CNG >>>>>>>>>>>

1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal.

<<<<<<<<<< CED <<<<<<<<<<<

2100 Hz tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path.

SG3 FAX: >>>>>>>>>> CNG >>>>>>>>>>>

1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal.

<<<<<<<<<< ANSAM <<<<<<<<

2100 Hz tone as CED, but amplitude modulated by a sine wave at 15Hz with phase reversal every 450 ms.

>>>CM>>X

No V.34 Initialization (Phases 2-4) exist, the initial V.8 Phase I also does not complete. OGW squelchs the CM tone and as SG3 is backward compatible with G3 fax standard, the FAX machines failover to G3.

<<<<<<<<<< CED <<<<<<<<<<<

2100 Hz tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path.

The OGW waits for the TGW to detect V.21 Preamble in the tones. Once TGW detects the V.21 Flag, it initiates switchover.

One of the tasks in switchover is to make the Jitter buffer transitions from adaptive to a fixed optimum value.

T.38 uses 300 ms fixed jitter or playout buffers. Enter the playout-delay fax 100 command under voice port to reduce the buffer time if the delay is high. Enter the show voice port X/X/X command in order to check the current values of playout delay.

Protocol Based

NSE Based

Protocol Based

NSE Based

GW------CUCM/GW

<---INVITE+SDP----

v=0 o=CiscoSystemsSIP-GW-UserAgent 0 6060 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 17924 RTP/AVP 0 c=IN IP4 209.165.201.2

a=rtpmap:0 PCMU/8000 a=silenceSupp:off - - - -

----100TRYING---->

----200OK+SDP---->

v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=silenceSupp:off - - - -

<------ACK---------

show call active voice brief will not show change

G3 FAX:

GW---------CUCM/GW

<====NSE192====

Upspeed Codec and Switch to Passthrough Mode.

Check for VTSP shows:

E_DSMP_DSP_REPORT _PEER_TO_PEER

_MSG

debug voip rtp session named event :

<<<Rcv> Pt:100    Evt:192     Pkt:00 00 00

====NSE192=====>

Check for VTSP shows:

debug voip rtp session named event :

Pt:100    Evt:192    Pkt:00 00 00  <Snd>>>

SG3 FAX:

GW----------CUCM/GW

<====NSE192======

Upspeed Codec and Switch to Passthrough Mode.

Check for VTSP shows:

E_DSMP_DSP_ REPORT _PEER_TO_PEER

_MSG

debug voip rtp session named event :

<<<Rcv> Pt:100    Evt:192     Pkt:00 00 00

====NSE192======>

Check for VTSP shows:

debug voip rtp session named event :

Pt:100    Evt:192    Pkt:00 00 00  <Snd>>>

<====NSE193=====

Disable ECAN.

Check for VTSP shows:

E_DSMP_DSP_REPORT _PEER_TO_PEER

_MSG

debug voip rtp session named event :

<<<Rcv> Pt:100    Evt:193     Pkt:00 00 00

====NSE193=====>

Check for VTSP shows:

debug voip rtp session named event :

Pt:100    Evt:193    Pkt:00 00 00  <Snd>>>

Note : NSE-194 is triggered by a local detection of 4 seconds of silence or carrier loss detection. This message instructs the remote gateway to return to voice mode. Basically, all the changes made by NSE-192 and NSE-193 are undone.

show call active voice brie " shows MODEMPASS nse

GW---------CUCM/GW

<-----INVITE+SDP------

v=0 o=CiscoSystemsSIP-GW -UserAgent 0 6061 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=image 17924 udptl t38 c=IN IP4 209.165.201.2 a=T38FaxVersion:0 a=T38MaxBitRate:14400 a=T38FaxFillBit Removal:0 a=T38FaxTranscoding MMR:0 a=T38FaxTranscoding JBIG:0 a=T38FaxRate Management: transferredTCF a=T38FaxMaxBuffer:200 a=T38FaxMax Datagram:320 a=T38FaxUdpEC: t38UDPRedundancy

--------100TRYING----->

-------200OK+SDP------>

v=0 o=CiscoSystemsCCM-SIP 2000 2 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=image 16384 udptl t38

<--------ACK------------

show call active voice brief will show: t38

Note : Whenever CUCM is involved, for the RE_INVITE in these topologies: Fax--GW---(h323)--CUCM--- (sip)---GW---FAX Fax--GW---(mgcp)--CUCM--- (sip)---GW---FAX Fax--GW---(sccp)---CUCM--- (sip)---GW---FAX The SDP in the RE-INVITE will have: ... m=image 17218 udptl t38 c=IN IP4 0.0.0.0 ... It will always first send 0.0.0.0/t38, and then later send another t38 invite with a real IP. Such behavior is not seen in this topology since CUCM handles media differently for this scenario: Fax--GW---(sip)---CUCM--- (sip)---GW---FAX Specially when CUBE is involved, keep in mind this: CSCtj50993, CSCtx83833

G3 FAX:

GW---------CUCM/GW

<====NSE200=====

Transition from voice mode to T.38

Check for VTSP shows:

E_DSMP_DSP_ REPORT _PEER_TO_PEER

_MSG

debug voip rtp session named event :

<<<Rcv> Pt:100    Evt:200     Pkt:00 00 00

====NSE201=====>

T.38 ACK received, instructs TGW to start T.38 session

Check for VTSP shows:

debug voip rtp session named event : Pt:100    Evt:201    Pkt:00 00 00  <Snd>>>

SG3 FAX:

As you spoof SG3 to G3 by squelching the CM tone, there is no SG3 FAX scenario in T38 relay.

Note : NSE-202 is a NACK to an NSE-200 message that signifes that the peer gateway cannot process T.38 packets for the call. The call will remain in voice mode and not switch over to T.38.

show call active voice brief shows:

t38

In Passthrough you cannot see any T.30 messages from debugs as all tones go in the RTP-like audio with G711ulaw/alaw. However, the FAX tone negotiation remains the same irrespective of relay or passthrough.

GW-------------------------CUCM/GW

<<<<<<<<< CSI <<<<<<<<<<< (optional) (called subscriber identification) <<<<<<<<< NSF <<<<<<<<<<< (optional) (nonstandard facilities) <<<<<<<<< DIS <<<<<<<<<<< (digital identification signal) >>>>>>>>> TSI >>>>>>>>>>>> (optional) (transmitting subscriber identification) >>>>>>>>> DCS >>>>>>>>>>> (digital command signal) ++++++++++TCF+++++++++> (high speed) (training check) <<<<<<<<<<CFR<<<<<<<<<< (confirmation to receive)

If you see FTT here that means TCF training failed, check clocking and slips on T1/E1. In packet captures check TCF should be all 0. ++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message)

<<<<<<<<< MCF <<<<<<<<<<< (message confirmation)

++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message)

<<<<<<<<< MCF <<<<<<<<<<< (message confirmation)

>>>>>>>>> DCN >>>>>>>>>>> (disconnect)

Note : ECM is Optional for G3, but Mandatory for SG3.  As you can achieve SG3 speeds with passthrough, make sure ECM is enabled on the fax machines for the fax to succeed. Also, TCF training signal is Required for G3, but is Not applicable for SG3.

Note : For Passthrough a common channel of 64kbps (g711) is allocated. So, the higher and the lower speeds of the messages becomes irrelevant.

If T38 switchover is successful, these messages are seen in the corresponding debugs:

Check for VTSP shows:

event:E_CC_T38_START

Check for DSMP shows: E_DSM_CC_MC_LOCAL_DNLD_DONE

Check for CCAPI shows: Caps(Codec=T38Fax(0x10000), Fax Rate=FAX_RATE_14400(0x80),Fax Version:=0, Vad=OFF(0x1),

debug fax relay t30 all-level-1 : timestamp=352583286 fr-msg-tx NSF timestamp=352583686 fr-msg-tx CSI timestamp=352583736 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352583736 fr-msg-tx good crc, 0 bytes timestamp=352584426 fr-msg-tx DIS timestamp=352584456 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352584456 fr-msg-tx good crc, 0 bytes timestamp=352584906 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352587656 fr-msg-det TSI timestamp=352588376 fr-msg-det DCS timestamp=352594056 fr-msg-tx CFR timestamp=352594156 FR_GOOD_CRC_LS_DATA 0x0 bytes

timestamp=352613376 fr-msg-det PPS timestamp=352615656 fr-msg-tx MCF timestamp=352615776 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352618716 fr-msg-det DCN

GW-------------------------CUCM/GW

<<<<<<<<< CSI <<<<<<<<<<< (optional) (called subscriber identification) <<<<<<<<< NSF <<<<<<<<<<< (optional) (nonstandard facilities) <<<<<<<<< DIS <<<<<<<<<<< (digital identification signal) >>>>>>>>> TSI >>>>>>>>>>>> (optional) (transmitting subscriber identification) >>>>>>>>> DCS >>>>>>>>>>> (digital command signal) ++++++++++TCF+++++++++> (high speed) (training check) <<<<<<<<<<CFR<<<<<<<<<< (confirmation to receive)

If you see FTT here that means TCF training failed, check clocking and slips on T1/E1. In packet captures check TCF should be all 0. ++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message)

<<<<<<<<< MCF <<<<<<<<<<< (message confirmation)

++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message)

<<<<<<<<< MCF <<<<<<<<<<< (message confirmation)

>>>>>>>>> DCN >>>>>>>>>>> (disconnect)

Protocol Based

NSE Based

Protocol Based

NSE Based

DP level config:

## fax protocol pass-through g711ulaw/g711alaw

## fax rate disable

## fax nsf 000000

DP level config:

## modem passthrough nse codec g711ulaw/g711alaw

## fax rate disable

## fax nsf 000000

DP level config:

## fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback none

## fax nsf 000000 ## fax-relay ecm disable ## fax-relay sg3-to-g3 system ## fax rate 14400

DP level config:

## fax protocol t38 nse force version 0 ls-redundancy 0 hs-redundancy 0 fallback none

## Debugs to Collect

- debug vpm all (in case of FXS)

- debug isdn q931 (in case of PRI)

- debug voice ccapi inout

- debug ccsip all/messages/verbos

- debug voip vtsp all

- debug voip dsmp all

- debug voip hpi all

- debug dsp-resource flex all

- debug voip dspapi

- debug fax relay t30 all-level-1

- debug voip rtp session named-event (in case of NSE based switchover)

### Revision History

1.0

14-Jan-2015

Initial Release

| Passthrough | T.38 Relay |
|---|---|
| GW-------------------------CUCM/GW <-------------INVITE-------------------- ------------100TRYING--------------> ------------180RINGING------------> Check for VTSP shows : Fax Relay=DISABLED - 'fax rate disabled' set (dial-peer) Primary Fax Protocol=IGNORE_FAX_RELAY, Fallback Fax Protocol=IGNORE_FAX_RELAY Fax Relay CM Suppression :=ENABLED , Fax Relay ANS Suppression :=DISABLED | GW-------------------------CUCM/GW <-------------INVITE-------------------- ------------100TRYING--------------> ------------180RINGING------------> Check for VTSP shows: Fax Relay=ENABLED Primary Fax Protocol=T38_FAX_RELAY, Fallback Fax Protocol=NONE_FAX_RELAY Fax Relay CM Suppression :=ENABLED, Fax Relay ANS Suppression :=DISABLED |
| Protocol Based | NSE Based | Protocol Based | NSE Based |
| GW------CUCM/GW ---200OK+SDP-----> v=0 o=CiscoSystemsSIP-GW-UserAgent 0 6060 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 17924 RTP/AVP 0 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=ptime:20 <----ACK+SDP----- v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=ptime:20 Note : In case of EO, a similar SDP would have been received with INVITE. | GW---------CUCM/GW ------200OK+SDP------> v=0 o=CiscoSystemsSIP- GW-UserAgent 5944 7031 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 18806 RTP/AVP 0 100 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194,200-202 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap:100 X-NSE/8000 a=X-cpar: a=fmtp:100 192-194,200-202 a=X-cap: 2 image udptl t38 <------ACK+SDP-------- v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.4 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194,200-202 a=rtpmap:101 telephone-event/8000 a=fmtp:101 0-16 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap:100 X-NSE/8000 a=X-cpar: a=fmtp:100 192-194,200-202 a=X-cap: 2 image udptl t38 Note : In case of EO, a similar SDP would have been received with INVITE. | GW------------CUCM/GW -------200OK+SDP--------> v=0 o=CiscoSystemsSIP-GW-UserAgent 0 6060 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 17924 RTP/AVP 0 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=ptime:20 <-------ACK+SDP--------- v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=ptime:20 Note : In case of EO, a similar SDP would have been received with INVITE. | GW------CUCM/GW -----200OK+SDP----> v=0 o=CiscoSystemsSIP- GW-UserAgent 5944 7031 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 18806 RTP/AVP 0 100 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194, 200-202 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap:100 X-NSE/8000 a=X-cpar: a=fmtp:100 192-194,200-202 a=X-cap: 2 image udptl t38 <-----ACK+SDP------ v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194, 200-202 a=rtpmap:101 telephone-event/8000 a=fmtp:101 0-16 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap:100 X-NSE/8000 a=X-cpar: a=fmtp:100 192-194,200-202 a=X-cap: 2 image udptl t38 Note : In case of EO, a similar SDP would have been received with INVITE. |
| GW-------------------------CUCM/GW <========AUDIO==========> Audio call established at this stage, but as the fax machines talk they start to exchange tones in the audio call. Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.) G3 FAX: <<<<<<<<<<CNG<<<<<<<<<<< 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. >>>>>>>>>>CED>>>>>>>>>>> 2100 Hz tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path. SG3 FAX: <<<<<<<<<<CNG<<<<<<<<<<< 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. >>>>>>>>>>ANSAM>>>>>>>>> 2100 Hz tone as CED, but amplitude modulated by a sine wave at 15 Hz with phase reversal every 450 ms. <<<<<<<<<< CM <<<<<<<<<<<< >>>>>>>>>> JM >>>>>>>>>>>> <<<<<<<<<< CJ <<<<<<<<<<<< V.34 Initialization (Phases 2-4) The TGW waits to detect V.21 Preamble in the tones. It finds it in CED tone (G3) or ANSAM (SG3). Once it detects the V.21 Flag, it initiates switchover. Check for VTSP shows: Event=E_DSMP_DSP_MODEM_TONE One of the tasks in switchover is to make the Jitter buffer transitions from adaptive to a fixed optimum value. Fax passthrough uses the last voice mode setting before the switchover for jitter or playout buffers. Enter the show voice port X/X/X command in order to check the current values of playout delay. | GW-------------------------CUCM/GW <========AUDIO==========> Audio call established at this stage, but as the fax machines talk they start to exchange tones in the audio call. Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.) G3 FAX: <<<<<<<<<<CNG<<<<<<<<<<< 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. >>>>>>>>>>CED>>>>>>>>>>> 2100 Hz tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path. SG3 FAX: <<<<<<<<<<CNG<<<<<<<<<<< 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. >>>>>>>>>>ANSAM>>>>>>>>> 2100 Hz tone as CED, but amplitude modulated by a sine wave at 15 Hz with phase reversal every 450 ms. Cisco gateways only support G3 fax calls with T.38. In order to properly handle the higher speeds of SG3 calls, modem passthrough must be used. No V.34 Initialization (Phases 2-4) exists, the initial V.8 Phase I also does not complete. OGW squelchs the CM tone and as SG3 is backward compatible with G3 fax standard, the FAX machines failover to G3. >>>>>>>>>CED>>>>>>>>>>> 2100 Hz tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path. The TGW waits to detect V.21 Preamble in the tones. It finds it in CED tone (G3) or ANSAM (SG3). Once it detects the V.21 Flag, it initiates switchover. Check for VTSP shows: VTSP: Event=E_DSMP_DSP_FAX_TONE Check for DSMP shows: E_DSM_CC_MC_START Check for CCAPI shows: CCAPI:Caps(Codec=T38Fax(0x10000), Fax Rate=FAX_RATE_14400(0x80),Fax Version:=0, Vad=OFF(0x1), One of the tasks in switchover is to make the Jitter buffer transitions from adaptive to a fixed optimum value. T.38 uses 300 ms fixed jitter or playout buffers. Enter the playout-delay fax 100 command under voice port in order to reduce the buffer time if the delay is high. Enter the show voice port X/X/X command in order to check the current values of playout delay. |
| Protocol Based | NSE Based | Protocol Based | NSE Based |
| GW------CUCM/GW ---INVITE+SDP----> v=0 o=CiscoSystemsSIP-GW-UserAgent 0 6060 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 17924 RTP/AVP 0 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=silenceSupp:off - - - - <----100TRYING---- <--200OK+SDP----- v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=silenceSupp:off - - - - --------ACK----------> show call active voice brief will not show change | G3 FAX: GW----------CUCM/GW ====NSE192======> Upspeed Codec and Switch to Passthrough Mode. Check for VTSP shows: E_DSM_CC_MODIFY _MEDIA_IND debug voip rtp session named event : Pt:100    Evt:192     Pkt:00 00 00  <Snd>>> <====NSE192======= Check for VTSP shows: E_DSMP_DSP_REPORT _PEER_TO_PEER _MSG debug voip rtp session named event : <<<Rcv> Pt:100    Evt:192     Pkt:00 00 00 SG3 FAX: GW----------CUCM/GW ====NSE192=====> Upspeed Codec and Switch to Passthrough Mode. Check for VTSP shows: E_DSM_CC_MODIFY _MEDIA_IND debug voip rtp session named event : Pt:100    Evt:192    Pkt:00 00 00  <Snd>>> <====NSE192====== Check for VTSP shows: E_DSMP_DSP_REPORT _PEER_TO_PEER _MSG debug voip rtp session named event : <<<Rcv> Pt:100    Evt:192     Pkt:00 00 00 =====NSE193=====> Detect phase reversal of ANSam Disable ECAN. Check for VTSP shows: E_DSM_CC_MODIFY_ MEDIA_IND debug voip rtp session named event : Pt:100    Evt:193     Pkt:00 00 00  <Snd>>> <====NSE193====== Check for VTSP shows: E_DSMP_DSP_REPORT _PEER_TO_PEER _MSG debug voip rtp session named event : <<<Rcv> Pt:100    Evt:193     Pkt:00 00 00 Note : NSE-194 is triggered by a local detection of 4 seconds of silence or carrier loss detection. This message instructs the remote gateway to return to voice mode. Basically, all the changes made by NSE-192 and NSE-193 are undone. show call active voice brief shows: MODEMPASS nse | GW-------------CUCM/GW -------INVITE+SDP------> v=0 o=CiscoSystemsSIP-GW-UserAgent 0 6061 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=image 17924 udptl t38 c=IN IP4 209.165.201.2 a=T38FaxVersion:0 a=T38MaxBitRate:14400 a=T38FaxFillBitRemoval:0 a=T38FaxTranscoding MMR:0 a=T38FaxTranscodingJ BIG:0 a=T38FaxRate Management: transferredTCF a=T38FaxMaxBuffer:200 a=T38FaxMax Datagram:320 a=T38FaxUdpEC: t38UDPRedundancy <--------100TRYING------ <-----200OK+SDP--------- v=0 o=CiscoSystemsCCM -SIP 2000 2 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=image 16384 udptl t38 -----------ACK-------------> show call active voice brief shows: t38 | G3 FAX: GW------CUCM/GW ====NSE200====> Transition from voice mode to T.38 Check for VTSP shows E_DSM_CC_ MODIFY _MEDIA_IND debug voip rtp session named event : Pt:100    Evt:200     Pkt:00 00 00  <Snd>>> <===NSE201===== T.38 ACK received, instructs TGW to start T.38 session. Check for VTSP shows: E_DSMP_DSP_ REPORT_PEER_ TO_PEER _MSG debug voip rtp session named event : <<<Rcv> Pt:100    Evt:201     Pkt:00 00 00 SG3 FAX: As you spoof SG3 to G3 by squelching the CM tone, there is no SG3 FAX scenario in T38 relay. Note : NSE-202 is a NACK to an NSE-200 message that signifies that the peer gateway cannot process T.38 packets for the call. The call remains in voice mode and does not switch over to T.38. show call active voice brief shows: t38 |
| In Passthrough you cannot see any T.30 messages from debugs as all tones go in the RTP-like audio with G711ulaw/alaw. However, the fax tone negotiation remains the same irrespective of relay or passthrough. GW-------------------------CUCM/GW >>>>>>>>> CSI>>>>>>>>>>>         (optional) (called subscriber identification) >>>>>>>>> NSF>>>>>>>>>>>        (optional) (nonstandard facilities) >>>>>>>>> DIS>>>>>>>>>>> (digital identification signal) <<<<<<<<<TSI<<<<<<<<<<<         (optional) (transmitting subscriber identification) <<<<<<<<<DCS<<<<<<<<<< (digital command signal) <++++++++++TCF++++++++++ (high speed) (training check) >>>>>>>>>>>CFR>>>>>>>>>> (confirmation to receive) If you see FTT here that means TCF training failed. Check the clocking and slips on T1/E1. In packet captures, check TCF should be all 0. <++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOM<<<<<<<< (partial page sent)/(end of message) >>>>>>>>> MCF>>>>>>>>>>> (message confirmation) <++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOP<<<<<<<< (partial page sent)/(end of procedure) >>>>>>>>> MCF>>>>>>>>>>> (message confirmation) <<<<<<<<<<DCN<<<<<<<<<< (disconnect) Note : ECM is Optional for G3, but Mandatory for SG3.  As you can achieve SG3 speeds with passthrough, make sure ECM is enabled on the fax machines for the fax to succeed. Also, TCF training signal is Required for G3, but is not applicable for SG3. Note : For Passthrough, a common channel of 64kbps (g711) is allocated. So, the higher and the lower speeds of the messages becomes irrelevant. | If T38 switchover is successful, these messages are seen in the corresponding debugs: Check for VTSP shows: event:E_CC_T38_START Check for DSMP shows: E_DSM_CC_MC_LOCAL_DNLD_DONE Check for CCAPI shows: Caps(Codec=T38Fax(0x10000), Fax Rate=FAX_RATE_14400(0x80), Fax Version:=0, Vad=OFF(0x1), debug fax relay t30 all-level-1 : timestamp=1321430729 fr-msg-det NSF timestamp=1321431129 fr-msg-det CSI timestamp=1321431879 fr-msg-det DIS timestamp=1321435719 fr-msg-tx TSI timestamp=1321436329 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321436329 fr-msg-tx good crc, 0 bytes timestamp=1321436439 fr-msg-tx DCS timestamp=1321436619 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321441499 fr-msg-det CFR timestamp=1321461449 fr-msg-tx PPS timestamp=1321461639 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321463099 fr-msg-det MCF timestamp=1321466789 fr-msg-tx DCN timestamp=1321466869 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321466869 fr-msg-tx good crc, 0 bytes GW-------------------------CUCM/GW >>>>>>>>> CSI>>>>>>>>>>>         (optional) (called subscriber identification) >>>>>>>>> NSF>>>>>>>>>>>        (optional) (nonstandard facilities) >>>>>>>>> DIS>>>>>>>>>>> (digital identification signal) <<<<<<<<<TSI<<<<<<<<<<<         (optional) (transmitting subscriber identification) <<<<<<<<<DCS<<<<<<<<<< (digital command signal) <++++++++++TCF++++++++++ (high speed) (training check) >>>>>>>>>>>CFR>>>>>>>>>> (confirmation to receive) If you see FTT here that means TCF, training failed, check clocking and slips on T1/E1. In packet captures check TCF should be all 0. <++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOM<<<<<<<< (partial page sent)/(end of message) >>>>>>>>> MCF>>>>>>>>>>> (message confirmation) <++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOP<<<<<<<< (partial page sent)/(end of procedure) >>>>>>>>> MCF>>>>>>>>>>> (message confirmation) <<<<<<<<<<DCN<<<<<<<<<< (disconnect) |
| Protocol Based | NSE Based | Protocol Based | NSE Based |
| DP level config: ## fax protocol pass-through g711ulaw/g711alaw ## fax rate disable ## fax nsf 000000 | DP level config: ## modem passthrough nse codec g711ulaw/g711alaw ## fax rate disable ## fax nsf 000000 | DP level config: ## fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback none ## fax nsf 000000 ## fax-relay ecm disable ## fax-relay sg3-to-g3 system ## fax rate 14400 | DP level config: ## fax protocol t38 nse force version 0 ls-redundancy 0 hs-redundancy 0 fallback none ## fax nsf 000000 ## fax-relay ecm disable ## fax-relay sg3-to-g3 system ## fax rate 14400 |

| Passthrough | T.38 Relay |
|---|---|
| GW-------------------------CUCM/GW -------------INVITE--------------------> <------------100TRYING-------------- <------------180RINGING------------- Check for VTSP shows: Fax Relay=DISABLED - 'fax rate disabled' set (dial-peer) Primary Fax Protocol=IGNORE_FAX_RELAY, Fallback Fax Protocol=IGNORE_FAX_RELAY Fax Relay CM Suppression :=ENABLED, Fax Relay ANS Suppression :=DISABLED | GW-------------------------CUCM/GW -------------INVITE--------------------> <------------100TRYING-------------- <------------180RINGING------------- Check for VTSP shows: Fax Relay=ENABLED Primary Fax Protocol=T38_FAX_RELAY, Fallback Fax Protocol=NONE_FAX_RELAY Fax Relay CM Suppression :=ENABLED, Fax Relay ANS Suppression :=DISABLED |
| Protocol Based | NSE Based | Protocol Based | NSE Based |
| GW------CUCM/GW <----200OK+SDP---- v=0 o=CiscoSystemsSIP-GW-UserAgent 0 6060 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 17924 RTP/AVP 0 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=ptime:20 -----ACK+SDP-----> v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=ptime:20 Note : In case of EO, a similar SDP would have been sent in INVITE. | GW----------CUCM/GW <-----200OK+SDP------ v=0 o=CiscoSystemsSIP -GW-UserAgent 5944 7031 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 18806 RTP/AVP 0 100 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194, 200-202 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap: 100 X-NSE/8000 a=X-cpar: a=fmtp:100 192-194, 200-202 a=X-cap: 2 image udptl t38 -------ACK+SDP-------> v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.4 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194, 200-202 a=rtpmap:101 telephone-event/8000 a=fmtp:101 0-16 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap:100 X-NSE/8000 a=X-cpar: a=fmtp:100 192-194,200-202 a=X-cap: 2 image udptl t38 Note : In case of EO, a similar SDP would have been sent in INVITE. | GW----------CUCM/GW <------200OK+SDP------ v=0 o=CiscoSystems SIP-GW-UserAgent 0 6060 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 17924 RTP/AVP 0 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=ptime:20 --------ACK+SDP------> v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=ptime:20 Note : In case of EO, a similar SDP would have been sent in INVITE. | GW--------CUCM/GW <-----200OK+SDP----- v=0 o=CiscoSystemsSIP -GW-UserAgent 5944 7031 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 18806 RTP/AVP 0 100 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194, 200-202 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap:100 X-NSE/8000 a=X-cpar: a=fmtp:100 192-194,200-202 a=X-cap: 2 image udptl t38 -------ACK+SDP------> v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=rtpmap:100 X-NSE/8000 a=fmtp:100 192-194, 200-202 a=rtpmap:101 telephone-event/8000 a=fmtp:101 0-16 a=ptime:20 a=X-sqn:0 a=X-cap: 1 audio RTP/AVP 100 a=X-cpar: a=rtpmap: 100 X-NSE/8000 a=X-cpar: a=fmtp: 100 192-194,200-202 a=X-cap: 2 image udptl t38 Note : In case of EO, a similar SDP would have been sent in INVITE. |
| GW-------------------------CUCM/GW <========AUDIO==========> Audio call established at this stage, but as FAX machines talk, they exchange tones in the audio call. Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.) G3 FAX: >>>>>>>>>> CNG >>>>>>>>>>> 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. <<<<<<<<<< CED <<<<<<<<<<< 2100 Hz tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path. SG3 FAX: >>>>>>>>>> CNG >>>>>>>>>>> 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. <<<<<<<<<< ANSAM <<<<<<<< 2100 Hz tone as CED, but amplitude modulated by a sine wave at 15Hz with phase reversal every 450 ms. >>>>>>>>>> CM >>>>>>>>>>>> <<<<<<<<<< JM <<<<<<<<<<< < >>>>>>>>>> CJ >>>>>>>>>>>> V.34 Initialization (Phases 2-4) The OGW waits for the terminating gateway to detect V.21 Preamble in the tones. Once TGW detects the V.21 Flag, it initiates switchover. One of the tasks in switchover is to make the Jitter buffer transitions from adaptive to a fixed optimum value. Fax passthrough uses the last voice mode setting before the switchover for jitter or playout buffers. Enter the show voice port X/X/X command in order to check the current values of playout delay. | GW-------------------------CUCM/GW <========AUDIO==========> Audio call established at this stage, but as FAX machines talk, they exchange tones in the audio call. Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.) G3 FAX: >>>>>>>>>> CNG >>>>>>>>>>> 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. <<<<<<<<<< CED <<<<<<<<<<< 2100 Hz tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path. SG3 FAX: >>>>>>>>>> CNG >>>>>>>>>>> 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. <<<<<<<<<< ANSAM <<<<<<<< 2100 Hz tone as CED, but amplitude modulated by a sine wave at 15Hz with phase reversal every 450 ms. >>>CM>>X Cisco gateways only support G3 fax calls with T.38. In order to properly handle the higher speeds of SG3 calls, modem passthrough must be used. No V.34 Initialization (Phases 2-4) exist, the initial V.8 Phase I also does not complete. OGW squelchs the CM tone and as SG3 is backward compatible with G3 fax standard, the FAX machines failover to G3. <<<<<<<<<< CED <<<<<<<<<<< 2100 Hz tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path. The OGW waits for the TGW to detect V.21 Preamble in the tones. Once TGW detects the V.21 Flag, it initiates switchover. One of the tasks in switchover is to make the Jitter buffer transitions from adaptive to a fixed optimum value. T.38 uses 300 ms fixed jitter or playout buffers. Enter the playout-delay fax 100 command under voice port to reduce the buffer time if the delay is high. Enter the show voice port X/X/X command in order to check the current values of playout delay. |
| Protocol Based | NSE Based | Protocol Based | NSE Based |
| GW------CUCM/GW <---INVITE+SDP---- v=0 o=CiscoSystemsSIP-GW-UserAgent 0 6060 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=audio 17924 RTP/AVP 0 c=IN IP4 209.165.201.2 a=rtpmap:0 PCMU/8000 a=silenceSupp:off - - - - ----100TRYING----> ----200OK+SDP----> v=0 o=CiscoSystemsCCM-SIP 2000 1 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=audio 16724 RTP/AVP 0 a=rtpmap:0 PCMU/8000 a=silenceSupp:off - - - - <------ACK--------- show call active voice brief will not show change | G3 FAX: GW---------CUCM/GW <====NSE192==== Upspeed Codec and Switch to Passthrough Mode. Check for VTSP shows: E_DSMP_DSP_REPORT _PEER_TO_PEER _MSG debug voip rtp session named event : <<<Rcv> Pt:100    Evt:192     Pkt:00 00 00 ====NSE192=====> Check for VTSP shows: E_DSM_CC_MODIFY _MEDIA_IND debug voip rtp session named event : Pt:100    Evt:192    Pkt:00 00 00  <Snd>>> SG3 FAX: GW----------CUCM/GW <====NSE192====== Upspeed Codec and Switch to Passthrough Mode. Check for VTSP shows: E_DSMP_DSP_ REPORT _PEER_TO_PEER _MSG debug voip rtp session named event : <<<Rcv> Pt:100    Evt:192     Pkt:00 00 00 ====NSE192======> Check for VTSP shows: E_DSM_CC_MODIFY _MEDIA_IND debug voip rtp session named event : Pt:100    Evt:192    Pkt:00 00 00  <Snd>>> <====NSE193===== Disable ECAN. Check for VTSP shows: E_DSMP_DSP_REPORT _PEER_TO_PEER _MSG debug voip rtp session named event : <<<Rcv> Pt:100    Evt:193     Pkt:00 00 00 ====NSE193=====> Check for VTSP shows: E_DSM_CC_MODIFY _MEDIA_IND debug voip rtp session named event : Pt:100    Evt:193    Pkt:00 00 00  <Snd>>> Note : NSE-194 is triggered by a local detection of 4 seconds of silence or carrier loss detection. This message instructs the remote gateway to return to voice mode. Basically, all the changes made by NSE-192 and NSE-193 are undone. show call active voice brie " shows MODEMPASS nse | GW---------CUCM/GW <-----INVITE+SDP------ v=0 o=CiscoSystemsSIP-GW -UserAgent 0 6061 IN IP4 209.165.201.2 s=SIP Call c=IN IP4 209.165.201.2 t=0 0 m=image 17924 udptl t38 c=IN IP4 209.165.201.2 a=T38FaxVersion:0 a=T38MaxBitRate:14400 a=T38FaxFillBit Removal:0 a=T38FaxTranscoding MMR:0 a=T38FaxTranscoding JBIG:0 a=T38FaxRate Management: transferredTCF a=T38FaxMaxBuffer:200 a=T38FaxMax Datagram:320 a=T38FaxUdpEC: t38UDPRedundancy --------100TRYING-----> -------200OK+SDP------> v=0 o=CiscoSystemsCCM-SIP 2000 2 IN IP4 209.165.201.3 s=SIP Call c=IN IP4 209.165.201.1 t=0 0 m=image 16384 udptl t38 <--------ACK------------ show call active voice brief will show: t38 Note : Whenever CUCM is involved, for the RE_INVITE in these topologies: Fax--GW---(h323)--CUCM--- (sip)---GW---FAX Fax--GW---(mgcp)--CUCM--- (sip)---GW---FAX Fax--GW---(sccp)---CUCM--- (sip)---GW---FAX The SDP in the RE-INVITE will have: ... m=image 17218 udptl t38 c=IN IP4 0.0.0.0 ... It will always first send 0.0.0.0/t38, and then later send another t38 invite with a real IP. Such behavior is not seen in this topology since CUCM handles media differently for this scenario: Fax--GW---(sip)---CUCM--- (sip)---GW---FAX Specially when CUBE is involved, keep in mind this: CSCtj50993, CSCtx83833 | G3 FAX: GW---------CUCM/GW <====NSE200===== Transition from voice mode to T.38 Check for VTSP shows: E_DSMP_DSP_ REPORT _PEER_TO_PEER _MSG debug voip rtp session named event : <<<Rcv> Pt:100    Evt:200     Pkt:00 00 00 ====NSE201=====> T.38 ACK received, instructs TGW to start T.38 session Check for VTSP shows: E_DSM_CC_MODIFY_ MEDIA_IND debug voip rtp session named event : Pt:100    Evt:201    Pkt:00 00 00  <Snd>>> SG3 FAX: As you spoof SG3 to G3 by squelching the CM tone, there is no SG3 FAX scenario in T38 relay. Note : NSE-202 is a NACK to an NSE-200 message that signifes that the peer gateway cannot process T.38 packets for the call. The call will remain in voice mode and not switch over to T.38. show call active voice brief shows: t38 |
| In Passthrough you cannot see any T.30 messages from debugs as all tones go in the RTP-like audio with G711ulaw/alaw. However, the FAX tone negotiation remains the same irrespective of relay or passthrough. GW-------------------------CUCM/GW <<<<<<<<< CSI <<<<<<<<<<< (optional) (called subscriber identification) <<<<<<<<< NSF <<<<<<<<<<< (optional) (nonstandard facilities) <<<<<<<<< DIS <<<<<<<<<<< (digital identification signal) >>>>>>>>> TSI >>>>>>>>>>>> (optional) (transmitting subscriber identification) >>>>>>>>> DCS >>>>>>>>>>> (digital command signal) ++++++++++TCF+++++++++> (high speed) (training check) <<<<<<<<<<CFR<<<<<<<<<< (confirmation to receive) If you see FTT here that means TCF training failed, check clocking and slips on T1/E1. In packet captures check TCF should be all 0. ++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message) <<<<<<<<< MCF <<<<<<<<<<< (message confirmation) ++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message) <<<<<<<<< MCF <<<<<<<<<<< (message confirmation) >>>>>>>>> DCN >>>>>>>>>>> (disconnect) Note : ECM is Optional for G3, but Mandatory for SG3.  As you can achieve SG3 speeds with passthrough, make sure ECM is enabled on the fax machines for the fax to succeed. Also, TCF training signal is Required for G3, but is Not applicable for SG3. Note : For Passthrough a common channel of 64kbps (g711) is allocated. So, the higher and the lower speeds of the messages becomes irrelevant. | If T38 switchover is successful, these messages are seen in the corresponding debugs: Check for VTSP shows: event:E_CC_T38_START Check for DSMP shows: E_DSM_CC_MC_LOCAL_DNLD_DONE Check for CCAPI shows: Caps(Codec=T38Fax(0x10000), Fax Rate=FAX_RATE_14400(0x80),Fax Version:=0, Vad=OFF(0x1), debug fax relay t30 all-level-1 : timestamp=352583286 fr-msg-tx NSF timestamp=352583686 fr-msg-tx CSI timestamp=352583736 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352583736 fr-msg-tx good crc, 0 bytes timestamp=352584426 fr-msg-tx DIS timestamp=352584456 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352584456 fr-msg-tx good crc, 0 bytes timestamp=352584906 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352587656 fr-msg-det TSI timestamp=352588376 fr-msg-det DCS timestamp=352594056 fr-msg-tx CFR timestamp=352594156 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352613376 fr-msg-det PPS timestamp=352615656 fr-msg-tx MCF timestamp=352615776 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352618716 fr-msg-det DCN GW-------------------------CUCM/GW <<<<<<<<< CSI <<<<<<<<<<< (optional) (called subscriber identification) <<<<<<<<< NSF <<<<<<<<<<< (optional) (nonstandard facilities) <<<<<<<<< DIS <<<<<<<<<<< (digital identification signal) >>>>>>>>> TSI >>>>>>>>>>>> (optional) (transmitting subscriber identification) >>>>>>>>> DCS >>>>>>>>>>> (digital command signal) ++++++++++TCF+++++++++> (high speed) (training check) <<<<<<<<<<CFR<<<<<<<<<< (confirmation to receive) If you see FTT here that means TCF training failed, check clocking and slips on T1/E1. In packet captures check TCF should be all 0. ++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message) <<<<<<<<< MCF <<<<<<<<<<< (message confirmation) ++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message) <<<<<<<<< MCF <<<<<<<<<<< (message confirmation) >>>>>>>>> DCN >>>>>>>>>>> (disconnect) |
| Protocol Based | NSE Based | Protocol Based | NSE Based |
| DP level config: ## fax protocol pass-through g711ulaw/g711alaw ## fax rate disable ## fax nsf 000000 | DP level config: ## modem passthrough nse codec g711ulaw/g711alaw ## fax rate disable ## fax nsf 000000 | DP level config: ## fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback none ## fax nsf 000000 ## fax-relay ecm disable ## fax-relay sg3-to-g3 system ## fax rate 14400 | DP level config: ## fax protocol t38 nse force version 0 ls-redundancy 0 hs-redundancy 0 fallback none ## fax nsf 000000 ## fax-relay ecm disable ## fax-relay sg3-to-g3 system ## fax rate 14400 |

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 14-Jan-2015 | Initial Release |