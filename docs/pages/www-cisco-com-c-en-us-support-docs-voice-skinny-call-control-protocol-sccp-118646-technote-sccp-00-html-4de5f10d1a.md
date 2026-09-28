---
doc_id: www-cisco-com-c-en-us-support-docs-voice-skinny-call-control-protocol-sccp-118646-technote-sccp-00-html-4de5f10d1a
source_url: https://www.cisco.com/c/en/us/support/docs/voice/skinny-call-control-protocol-sccp/118646-technote-sccp-00.html
retrieved_at: 2026-08-20T23:29:51.541182+00:00
---

Fax Troubleshoot Guide

# Fax Troubleshoot Guide

Updated: January 15, 2015

Document ID: 118646

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

- VAD disabled on DSP

- Jitter buffer transitions from adaptive to a fixed optimum value

- Fax Terminal Identification

- Capabilities exchange and setting

- Training

- Transmission of pages

- Error detection and correction (ECM)

- End of message and page confirmation

- Call Disconnect, On-hook

This call flow includes the messages to look for when Skinny Call Control Protocol (SCCP) is the protocol identified. There are corresponding sections based on whether your endpoint is a TGW or OGW.

Note : In the table in the next section, both T.38 Relay and Passthrough were tested simultaneously and differences between G3 and SG3 have been pointed out.

## TGW - Fax Call Incoming on SCCP Leg

Note that:

- T.38 - Delay < 1000ms, Jitter < 300ms, Packet loss should be NONE unless T.38 with redundancy.

- Passthrough - Delay < 1000ms, Jitter < 30ms, Packet loss should be NONE.

- Protocol Based switchover - This is standard based.

- NSE Based switchover - This is proprietary and works only between Cisco voice gateways.

Passthrough

T.38 Relay

Protocol Based

NSE Based

Protocol Based

NSE Based

Protocol Based switchover is not supported with SCCP.

GW-----------------CUCM/GW

<--------SelectSoftKeys---------

<-------CallStateMessage------

-------OffHookMessage----->

sccp_send_offhook_v1

<---OpenReceiveChannel----

-OpenReceiveChannelAck->

<--StartMediaTransmission--

Check for VTSP shows : Fax Relay= DISABLED - SCCP Application Primary Fax Protocol= IGNORE_FAX_RELAY, Fallback Fax Protocol= IGNORE_FAX_RELAY Fax Relay CM Suppression := ENABLED, Fax Relay ANS Suppression := DISABLED Fax Parameters Set By= SCCP Call Type

Protocol Based switchover is not supported with SCCP.

GW-----------------CUCM/GW

<--------SelectSoftKeys---------

<-------CallStateMessage------

-------OffHookMessage----->

sccp_send_offhook_v1

<---OpenReceiveChannel----

-OpenReceiveChannelAck->

<-StartMediaTransmission-

GW-------------------------CUCM/GW

<========AUDIO==========>

Audio call established at this stage, but as fax machines talk they exchange tones in the audio call.

Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.)

G3 Fax:

<<<<<<<<<<CNG<<<<<<<<<<<

1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal.

>>>>>>>>>>CED>>>>>>>>>>>

2100 Hz Tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path.

SG3 Fax: <<<<<<<<<<CNG<<<<<<<<<<<

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

Audio call established at this stage, but as fax machines talk they exchange tones in the audio call.

Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.)

G3 Fax:

<<<<<<<<<<CNG<<<<<<<<<<<

1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal.

>>>>>>>>>>CED>>>>>>>>>>>

2100 Hz Tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path.

SG3 Fax: <<<<<<<<<<CNG<<<<<<<<<<<

1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal.

>>>>>>>>>>ANSAM>>>>>>>>>

2100 Hz tone as CED, but amplitude modulated by a sine wave at 15 Hz with phase reversal every 450 ms.

No V.34 Initialization (Phases 2-4) exist, the initial V.8 Phase I also does not complete. OGW squelchs the CM tone and as SG3 is backward compatible with G3 fax standard, the fax machines failover to G3.

>>>>>>>>>CED>>>>>>>>>>>

2100 Hz Tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path.

The TGW waits to detect V.21 Preamble in the tones. It finds it in CED tone (G3) or ANSAM (SG3). Once it detects the V.21 Flag, it initiates switchover.

Check for VTSP shows:

VTSP: Event=E_DSMP_DSP_FAX_TONE

Check for DSMP shows: E_DSM_CC_MC_START

One of the tasks in switchover is to make the Jitter buffer transitions from adaptive to a fixed optimum value.

T.38 uses 300 ms fixed jitter or playout buffers. Enter the playout-delay fax 100 command under voice port to reduce the buffer time if the delay is high. Enter the show voice port X/X/X in order to check the current values of playout delay.

Protocol Based

NSE Based

Protocol Based

NSE Based

G3 Fax:

GW--------------------CUCM/GW

=======NSE192========>

Upspeed Codec and Switch to Passthrough Mode.

Check for VTSP shows:

E_DSM_CC_MODIFY_ MEDIA_IND

debug voip rtp session named event :

Pt:100    Evt:192     Pkt:00 00 00  <Snd>>>

<======NSE192=========

Check for VTSP shows:

E_DSMP_DSP_REPORT_ PEER_TO_PEER

_MSG

debug voip rtp session named event :

<<<Rcv> Pt:100    Evt:192     Pkt:00 00 00

SG3 Fax:

GW--------------------CUCM/GW

=======NSE192========>

Upspeed Codec and Switch to Passthrough Mode.

Check for VTSP shows:

E_DSM_CC_MODIFY_MEDIA_IND

debug voip rtp session named event :

Pt:100    Evt:192    Pkt:00 00 00  <Snd>>>

<======NSE192=========

Check for VTSP shows:

E_DSMP_DSP_REPORT_PEER_TO_PEER

_MSG

debug voip rtp session named event :

<<<Rcv> Pt:100    Evt:192     Pkt:00 00 00

=======NSE193========>

Detect phase reversal of ANSam Disable ECAN.

Check for VTSP shows:

E_DSM_CC_MODIFY_MEDIA_IND

debug voip rtp session named event :

Pt:100    Evt:193     Pkt:00 00 00  <Snd>>>

<======NSE193=========

Check for VTSP shows:

E_DSMP_DSP_REPORT_PEER_TO_PEER

_MSG

debug voip rtp session named event :

<<<Rcv> Pt:100    Evt:193     Pkt:00 00 00

Note : NSE-194 is triggered by a local detection of 4 seconds of silence or carrier loss detection. This message instructs the remote gateway to return to voice mode. Basically, all the changes made by NSE-192 and NSE-193 are undone.

show call active voice brief shows: MODEMPASS nse

G3 Fax:

GW--------------------CUCM/GW

=======NSE200========>

Transition from voice mode to T.38

Check for VTSP shows:

E_DSM_CC_MODIFY_ MEDIA_IND

debug voip rtp session named event :

Pt:100    Evt:200     Pkt:00 00 00  <Snd>>>

<======NSE201=========

T.38 ACK received, instructs TGW to start T.38 session

Check for VTSP shows:

E_DSMP_DSP_REPORT_ PEER_TO_PEER

_MSG

debug voip rtp session named event :

<<<Rcv> Pt:100    Evt:201     Pkt:00 00 00

SG3 Fax:

As you squelch the CM tone in order to spoof SG3 to G3, there is no SG3 fax scenario in T38 relay.

Note : NSE-202 is a NACK to an NSE-200 message that signifies that the peer gateway cannot process T.38 packets for the call. The call will remain in voice mode and not switch over to T.38.

show call active voice brief shows:

t38

In Passthrough you cannot see any T.30 messages from debugs as all tones go in the RTP-like audio with G711ulaw/alaw. However, the fax tone negotiation remains the same irrespective of relay or passthrough.

GW-------------------------CUCM/GW

>>>>>>>>> CSI>>>>>>>>>>>         (optional) (called subscriber identification) >>>>>>>>> NSF>>>>>>>>>>>        (optional) (nonstandard facilities) >>>>>>>>> DIS>>>>>>>>>>> (digital identification signal) <<<<<<<<<TSI<<<<<<<<<<<         (optional) (transmitting subscriber identification) <<<<<<<<<DCS<<<<<<<<<< (digital command signal) <++++++++++TCF++++++++++ (high speed) (training check) >>>>>>>>>>>CFR>>>>>>>>>> (confirmation to receive)

If you see FTT here that means TCF, training failed, check clocking and slips on T1/E1. In packet captures, check TCF should be all 0. <++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOM<<<<<<<< (partial page sent)/(end of message)

>>>>>>>>> MCF>>>>>>>>>>> (message confirmation)

<++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOP<<<<<<<< (partial page sent)/(end of procedure)

>>>>>>>>> MCF>>>>>>>>>>> (message confirmation)

<<<<<<<<<<DCN<<<<<<<<<< (disconnect)

Note : ECM is Optional for G3, but Mandatory for SG3.  As you can achieve SG3 speeds with passthrough, make sure ECM is enabled on the fax machines for the fax to succeed. Also, TCF training signal is Required for G3, but is Not applicable for SG3.

Note : For Passthrough a common channel of 64 kbps (g711) is allocated. So, the higher and the lower speeds of the messages become irrelevant.

If T38 switchover is successful, these messages are seen in the corresponding debugs:

Check for VTSP shows:

event:E_CC_T38_START

Check for DSMP shows: E_DSM_CC_MC_LOCAL_DNLD_DONE

debug fax relay t30 all-level-1 : timestamp=1321430729 fr-msg-det NSF timestamp=1321431129 fr-msg-det CSI timestamp=1321431879 fr-msg-det DIS timestamp=1321435719 fr-msg-tx TSI timestamp=1321436329 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321436329 fr-msg-tx good crc, 0 bytes timestamp=1321436439 fr-msg-tx DCS timestamp=1321436619 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321441499 fr-msg-det CFR timestamp=1321461449 fr-msg-tx PPS timestamp=1321461639 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321463099 fr-msg-det MCF timestamp=1321466789 fr-msg-tx DCN timestamp=1321466869 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321466869 fr-msg-tx good crc, 0 bytes

GW-------------------------CUCM/GW

>>>>>>>>> CSI>>>>>>>>>>> (optional) (called subscriber identification) >>>>>>>>> NSF>>>>>>>>>>> (optional) (nonstandard facilities) >>>>>>>>> DIS>>>>>>>>>>> (digital identification signal) <<<<<<<<<TSI<<<<<<<<<<<         (optional) (transmitting subscriber identification) <<<<<<<<<DCS<<<<<<<<<< (digital command signal) <++++++++++TCF++++++++++ (high speed) (training check) >>>>>>>>>>>CFR>>>>>>>>>> (confirmation to receive)

If you see FTT here that means TCF, training failed, check clocking and slips on T1/E1. In packet captures, check TCF should be all 0. <++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOM<<<<<<<< (partial page sent)/(end of message)

>>>>>>>>> MCF>>>>>>>>>>> (message confirmation)

<++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOP<<<<<<<< (partial page sent)/(end of procedure)

>>>>>>>>> MCF>>>>>>>>>>> (message confirmation)

<<<<<<<<<<DCN<<<<<<<<<< (disconnect)

Protocol Based

NSE Based

Protocol Based

NSE Based

voice service voip level config:

## fax protocol none

## modem passthrough nse codec g711ulaw

voice service voip level config:

# # fax protocol t38 nse force version 0 ls-redundancy 0 hs-redundancy 0 fallback none

## fax-relay sg3-to-g3

## OGW - Fax Call Outgoing on SCCP Leg

Note that:

- For T.38 - Delay < 1000ms, Jitter < 300ms, Packet loss should be NONE unless T.38 with redundancy.

- For Passthrough - Delay < 1000ms, Jitter < 30ms, Packet loss should be NONE.

- Protocol Based switchover - This is standard based.

- NSE Based switchover - This is proprietary, works only between Cisco voice gateways.

Passthrough

T.38 Relay

Protocol Based

NSE Based

Protocol Based

NSE Based

Protocol Based switchover is not supported with SCCP.

GW----------------------CUCM/GW

-------OffHookMessage------->

--KeypadButtonMessage---->

<-------CallStateMessage------

<----OpenReceiveChannel-----

--OpenReceiveChannelAck-->

<--StartMediaTransmission--

<-------CallStateMessage------

CallStateMsg Info: RINGOUT

Check for VTSP shows : Fax Relay=DISABLED - SCCP Application Primary Fax Protocol=IGNORE_FAX_RELAY, Fallback Fax Protocol=IGNORE_FAX_RELAY Fax Relay CM Suppression : =ENABLED, Fax Relay ANS Suppression : =DISABLED Fax Parameters Set By= SCCP Call Type

<-------CallStateMessage------

CallStateMsg Info: CONNECTED

Protocol Based switchover is not supported with SCCP.

GW----------------------CUCM/GW

-------OffHookMessage------->

--KeypadButtonMessage---->

<-------CallStateMessage------

<----OpenReceiveChannel-----

--OpenReceiveChannelAck-->

<--StartMediaTransmission--

<-------CallStateMessage------

CallStateMsg Info: RINGOUT

Check for VTSP shows : Fax Relay=ENABLED Primary Fax Protocol=T38_FAX_RELAY, Fallback Fax Protocol=NONE_FAX_RELAY Fax Relay CM Suppression : =ENABLED , Fax Relay ANS Suppression : =DISABLED Fax Parameters Set By= SCCP Call Type

<-------CallStateMessage------

GW-------------------------CUCM/GW

<========AUDIO==========>

Audio call established at this stage, but as FAX machines talk they exchange tones in the audio call.

Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.)

G3 Fax:

>>>>>>>>>> CNG >>>>>>>>>>>

1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal.

<<<<<<<<<< CED <<<<<<<<<<<

2100 Hz Tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path.

SG3 Fax: >>>>>>>>>> CNG >>>>>>>>>>>

1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal.

<<<<<<<<<< ANSAM <<<<<<<<

2100 Hz tone as CED, but amplitude modulated by a sine wave at 15 Hz with phase reversal every 450 ms.

>>>>>>>>>> CM >>>>>>>>>>>>

<<<<<<<<<< JM <<<<<<<<<<< <

>>>>>>>>>> CJ >>>>>>>>>>>>

V.34 Initialization (Phases 2-4)

The OGW waits for the TGW to detect V.21 Preamble in the tones. Once TGW detects the V.21 Flag, it initiates switchover.

One of the tasks in switchover is to make the Jitter buffer transitions from adaptive to a fixed optimum value.

Fax passthrough uses the last voice mode setting before the switchover for jitter or playout buffers. Enter the show voice port X/X/X command in order to check the current values of playout delay.

GW-------------------------CUCM/GW

<========AUDIO==========>

Audio call established at this stage, but as fax machines talk they exchange tones in the audio call.

Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.)

G3 Fax:

>>>>>>>>>> CNG >>>>>>>>>>>

1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal.

<<<<<<<<<< CED <<<<<<<<<<<

2100 Hz Tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path.

SG3 Fax: >>>>>>>>>> CNG >>>>>>>>>>>

1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal.

<<<<<<<<<< ANSAM <<<<<<<<

2100 Hz tone as CED, but amplitude modulated by a sine wave at 15 Hz with phase reversal every 450 ms.

>>>CM>>X

No V.34 Initialization (Phases 2-4) exist, the initial V.8 Phase I also does not complete. OGW squelches the CM tone and as SG3 is backward compatible with G3 fax standard, the fax machines failover to G3.

<<<<<<<<<< CED <<<<<<<<<<<

2100 Hz Tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path.

The OGW waits for the TGW to detect V.21 Preamble in the tones. Once TGW detects the V.21 Flag, it initiates switchover.

One of the tasks in switchover is to make the Jitter buffer transitions from adaptive to a fixed optimum value.

T.38 uses 300 ms fixed jitter or playout buffers. Enter the playout-delay fax 100 command under voice port to reduce the buffer time if the delay is high. Enter the show voice port X/X/X command in order to check the current values of playout delay.

Protocol Based

NSE Based

Protocol Based

NSE Based

Protocol Based switchover is not supported with SCCP.

G3 Fax:

GW--------------------CUCM/GW

<=======NSE192========

Upspeed Codec and Switch to Passthrough Mode.

Check for VTSP shows :

E_DSMP_DSP_REPORT_ PEER_TO_PEER

_MSG

debug voip rtp session named event :

<<<Rcv> Pt:100    Evt:192     Pkt:00 00 00

======NSE192=========>

Check for VTSP shows :

debug voip rtp session named event :

Pt:100    Evt:192    Pkt:00 00 00  <Snd>>>

SG3 Fax:

GW--------------------CUCM/GW

<=======NSE192========

Upspeed Codec and Switch to Passthrough Mode.

Check for VTSP shows :

E_DSMP_DSP_REPORT_ PEER_TO_PEER

_MSG

debug voip rtp session named event

<<<Rcv> Pt:100    Evt:192     Pkt:00 00 00

======NSE192=========>

Check for VTSP shows :

debug voip rtp session named event :

Pt:100    Evt:192    Pkt:00 00 00  <Snd>>>

<=======NSE193========

Disable ECAN.

Check for VTSP shows :

E_DSMP_DSP_REPORT_ PEER_TO_PEER

_MSG

debug voip rtp session named event :

<<<Rcv> Pt:100    Evt:193     Pkt:00 00 00

======NSE193=========>

Check for VTSP shows :

debug voip rtp session named event :

Pt:100    Evt:193    Pkt:00 00 00  <Snd>>>

Note : NSE-194 is triggered by a local detection of 4 seconds of silence or carrier loss detection. This message instructs the remote gateway to return to voice mode. Basically, all the changes made by NSE-192 and NSE-193 are undone.

show call active voice brief shows: MODEMPASS nse

Protocol Based switchover is not supported with SCCP.

G3 Fax:

GW--------------------CUCM/GW

<=======NSE200========

Transition from voice mode to T.38

Check for VTSP shows :

E_DSMP_DSP_REPORT_ PEER_TO_PEER

_MSG

debug voip rtp session named event :

<<<Rcv> Pt:100    Evt:200     Pkt:00 00 00

======NSE201=========>

T.38 ACK received, instructs TGW to start T.38 session

Check for VTSP shows :

debug voip rtp session named event : Pt:100    Evt:201    Pkt:00 00 00  <Snd>>>

SG3 Fax:

As you squelch the CM tone in order to spoof SG3 to G3, there is no SG3 fax scenario in T38 relay.

Note : NSE-202 is a NACK to an NSE-200 message which signifies that the peer gateway cannot process T.38 packets for the call. The call remains in voice mode and does not switch over to T.38.

show call active voice brief shows:

t38

In Passthrough you cannot see any T.30 messages from debugs as all tones go in the RTP-like audio with G711ulaw/alaw. However, the fax tone negotiation remains the same irrespective of relay or passthrough.

GW-------------------------CUCM/GW

<<<<<<<<< CSI <<<<<<<<<<< (optional) (called subscriber identification) <<<<<<<<< NSF <<<<<<<<<<< (optional) (nonstandard facilities) <<<<<<<<< DIS <<<<<<<<<<< (digital identification signal) >>>>>>>>> TSI >>>>>>>>>>>> (optional) (transmitting subscriber identification) >>>>>>>>> DCS >>>>>>>>>>> (digital command signal) ++++++++++TCF+++++++++> (high speed) (training check) <<<<<<<<<<CFR<<<<<<<<<< (confirmation to receive)

If you see FTT here that means TCF, training failed, check clocking and slips on T1/E1. In packet captures check TCF should be all 0. ++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message)

<<<<<<<<< MCF <<<<<<<<<<< (message confirmation)

++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message)

<<<<<<<<< MCF <<<<<<<<<<< (message confirmation)

>>>>>>>>> DCN >>>>>>>>>>> (disconnect)

Note : ECM is Optional for G3 but Mandatory for SG3. As you can achieve SG3 speeds with passthrough, make sure ECM is enabled on the fax machines for the fax to succeed. Also, TCF training signal is Required for G3, but is Not applicable for SG3.

Note : For Passthrough a common channel of 64 kbps (g711) is allocated. So, the higher and the lower speeds of the messages become irrelevant.

If T38 switchover is successful, these messages are seen in the corresponding debugs:

Check for VTSP shows : event:E_CC_T38_START

Check for DSMP shows : E_DSM_CC_MC_LOCAL_DNLD_DONE

debug fax relay t30 all-level-1 : timestamp=352583286 fr-msg-tx NSF timestamp=352583686 fr-msg-tx CSI timestamp=352583736 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352583736 fr-msg-tx good crc, 0 bytes timestamp=352584426 fr-msg-tx DIS timestamp=352584456 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352584456 fr-msg-tx good crc, 0 bytes timestamp=352584906 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352587656 fr-msg-det TSI timestamp=352588376 fr-msg-det DCS timestamp=352594056 fr-msg-tx CFR timestamp=352594156 FR_GOOD_CRC_LS_DATA 0x0 bytes

timestamp=352613376 fr-msg-det PPS timestamp=352615656 fr-msg-tx MCF timestamp=352615776 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352618716 fr-msg-det DCN

GW-------------------------CUCM/GW

<<<<<<<<< CSI <<<<<<<<<<< (optional) (called subscriber identification) <<<<<<<<< NSF <<<<<<<<<<< (optional) (nonstandard facilities) <<<<<<<<< DIS <<<<<<<<<<< (digital identification signal) >>>>>>>>> TSI >>>>>>>>>>>> (optional) (transmitting subscriber identification) >>>>>>>>> DCS >>>>>>>>>>> (digital command signal) ++++++++++TCF+++++++++> (high speed) (training check) <<<<<<<<<< CFR <<<<<<<<<< (confirmation to receive)

If you see FTT here that means TCF, training failed, check clocking and slips on T1/E1. In packet captures check TCF should be all 0. ++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message)

<<<<<<<<< MCF <<<<<<<<<<< (message confirmation)

++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message)

<<<<<<<<< MCF <<<<<<<<<<< (message confirmation)

>>>>>>>>> DCN >>>>>>>>>>> (disconnect)

voice service voip level config:

## fax protocol none

## modem passthrough nse codec g711ulaw

voice service voip level config:

# # fax protocol t38 nse force version 0 ls-redundancy 0 hs-redundancy 0 fallback none

## fax-relay sg3-to-g3

## Debugs to Collect

- debug vpm all

- debug voip application stcapp all

- debug sccp packet

- debug voip vtsp all

- debug voip dsmp all

- debug voip hpi all

- debug dsp-resource flex all

- debug voip dspapi

- debug fax relay t30 all-level-1

- debug voip rtp session named-event

### Revision History

1.0

15-Jan-2015

Initial Release

### Contributed by Cisco Engineers

Diya Mathew and Karan Moudgil

Cisco TAC Engineers.

### Customers Also Viewed

- CUCM Auto Configuration for SCCP Gateways

| Passthrough | T.38 Relay |
|---|---|
| Protocol Based | NSE Based | Protocol Based | NSE Based |
| Protocol Based switchover is not supported with SCCP. | GW-----------------CUCM/GW <--------SelectSoftKeys--------- <-------CallStateMessage------ CallStateMsg Info: RINGIN -------OffHookMessage-----> sccp_send_offhook_v1 <---OpenReceiveChannel---- -OpenReceiveChannelAck-> <--StartMediaTransmission-- Check for VTSP shows : Fax Relay= DISABLED - SCCP Application Primary Fax Protocol= IGNORE_FAX_RELAY, Fallback Fax Protocol= IGNORE_FAX_RELAY Fax Relay CM Suppression := ENABLED, Fax Relay ANS Suppression := DISABLED Fax Parameters Set By= SCCP Call Type | Protocol Based switchover is not supported with SCCP. | GW-----------------CUCM/GW <--------SelectSoftKeys--------- <-------CallStateMessage------ CallStateMsg Info: RINGIN -------OffHookMessage-----> sccp_send_offhook_v1 <---OpenReceiveChannel---- -OpenReceiveChannelAck-> <-StartMediaTransmission- Check for VTSP shows: Fax Relay=ENABLED Primary Fax Protocol= T38_FAX_RELAY, Fallback Fax Protocol= NONE_FAX_RELAY Fax Relay CM Suppression := ENABLED, Fax Relay ANS Suppression := DISABLED Fax Parameters Set By= SCCP Call Type |
| GW-------------------------CUCM/GW <========AUDIO==========> Audio call established at this stage, but as fax machines talk they exchange tones in the audio call. Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.) G3 Fax: <<<<<<<<<<CNG<<<<<<<<<<< 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. >>>>>>>>>>CED>>>>>>>>>>> 2100 Hz Tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path. SG3 Fax: <<<<<<<<<<CNG<<<<<<<<<<< 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. >>>>>>>>>>ANSAM>>>>>>>>> 2100 Hz tone as CED, but amplitude modulated by a sine wave at 15 Hz with phase reversal every 450 ms. <<<<<<<<<< CM <<<<<<<<<<<< >>>>>>>>>> JM >>>>>>>>>>>> <<<<<<<<<< CJ <<<<<<<<<<<< V.34 Initialization (Phases 2-4) The TGW waits to detect V.21 Preamble in the tones. It finds it in CED tone (G3) or ANSAM (SG3). Once it detects the V.21 Flag, it initiates switchover. Check for VTSP shows: Event=E_DSMP_DSP_MODEM_TONE One of the tasks in switchover is to make the Jitter buffer transitions from adaptive to a fixed optimum value. Fax passthrough uses the last voice mode setting before the switchover for jitter or playout buffers. Enter the show voice port X/X/X command in order to check the current values of playout delay. | GW-------------------------CUCM/GW <========AUDIO==========> Audio call established at this stage, but as fax machines talk they exchange tones in the audio call. Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.) G3 Fax: <<<<<<<<<<CNG<<<<<<<<<<< 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. >>>>>>>>>>CED>>>>>>>>>>> 2100 Hz Tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path. SG3 Fax: <<<<<<<<<<CNG<<<<<<<<<<< 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. >>>>>>>>>>ANSAM>>>>>>>>> 2100 Hz tone as CED, but amplitude modulated by a sine wave at 15 Hz with phase reversal every 450 ms. Cisco gateways only support G3 fax calls with T.38. In order to properly handle the higher speeds of SG3 calls, modem passthrough must be used. No V.34 Initialization (Phases 2-4) exist, the initial V.8 Phase I also does not complete. OGW squelchs the CM tone and as SG3 is backward compatible with G3 fax standard, the fax machines failover to G3. >>>>>>>>>CED>>>>>>>>>>> 2100 Hz Tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path. The TGW waits to detect V.21 Preamble in the tones. It finds it in CED tone (G3) or ANSAM (SG3). Once it detects the V.21 Flag, it initiates switchover. Check for VTSP shows: VTSP: Event=E_DSMP_DSP_FAX_TONE Check for DSMP shows: E_DSM_CC_MC_START One of the tasks in switchover is to make the Jitter buffer transitions from adaptive to a fixed optimum value. T.38 uses 300 ms fixed jitter or playout buffers. Enter the playout-delay fax 100 command under voice port to reduce the buffer time if the delay is high. Enter the show voice port X/X/X in order to check the current values of playout delay. |
| Protocol Based | NSE Based | Protocol Based | NSE Based |
| Protocol Based switchover is not supported with SCCP. | G3 Fax: GW--------------------CUCM/GW =======NSE192========> Upspeed Codec and Switch to Passthrough Mode. Check for VTSP shows: E_DSM_CC_MODIFY_ MEDIA_IND debug voip rtp session named event : Pt:100    Evt:192     Pkt:00 00 00  <Snd>>> <======NSE192========= Check for VTSP shows: E_DSMP_DSP_REPORT_ PEER_TO_PEER _MSG debug voip rtp session named event : <<<Rcv> Pt:100    Evt:192     Pkt:00 00 00 SG3 Fax: GW--------------------CUCM/GW =======NSE192========> Upspeed Codec and Switch to Passthrough Mode. Check for VTSP shows: E_DSM_CC_MODIFY_MEDIA_IND debug voip rtp session named event : Pt:100    Evt:192    Pkt:00 00 00  <Snd>>> <======NSE192========= Check for VTSP shows: E_DSMP_DSP_REPORT_PEER_TO_PEER _MSG debug voip rtp session named event : <<<Rcv> Pt:100    Evt:192     Pkt:00 00 00 =======NSE193========> Detect phase reversal of ANSam Disable ECAN. Check for VTSP shows: E_DSM_CC_MODIFY_MEDIA_IND debug voip rtp session named event : Pt:100    Evt:193     Pkt:00 00 00  <Snd>>> <======NSE193========= Check for VTSP shows: E_DSMP_DSP_REPORT_PEER_TO_PEER _MSG debug voip rtp session named event : <<<Rcv> Pt:100    Evt:193     Pkt:00 00 00 Note : NSE-194 is triggered by a local detection of 4 seconds of silence or carrier loss detection. This message instructs the remote gateway to return to voice mode. Basically, all the changes made by NSE-192 and NSE-193 are undone. show call active voice brief shows: MODEMPASS nse | Protocol Based switchover is not supported with SCCP. | G3 Fax: GW--------------------CUCM/GW =======NSE200========> Transition from voice mode to T.38 Check for VTSP shows: E_DSM_CC_MODIFY_ MEDIA_IND debug voip rtp session named event : Pt:100    Evt:200     Pkt:00 00 00  <Snd>>> <======NSE201========= T.38 ACK received, instructs TGW to start T.38 session Check for VTSP shows: E_DSMP_DSP_REPORT_ PEER_TO_PEER _MSG debug voip rtp session named event : <<<Rcv> Pt:100    Evt:201     Pkt:00 00 00 SG3 Fax: As you squelch the CM tone in order to spoof SG3 to G3, there is no SG3 fax scenario in T38 relay. Note : NSE-202 is a NACK to an NSE-200 message that signifies that the peer gateway cannot process T.38 packets for the call. The call will remain in voice mode and not switch over to T.38. show call active voice brief shows: t38 |
| In Passthrough you cannot see any T.30 messages from debugs as all tones go in the RTP-like audio with G711ulaw/alaw. However, the fax tone negotiation remains the same irrespective of relay or passthrough. GW-------------------------CUCM/GW >>>>>>>>> CSI>>>>>>>>>>>         (optional) (called subscriber identification) >>>>>>>>> NSF>>>>>>>>>>>        (optional) (nonstandard facilities) >>>>>>>>> DIS>>>>>>>>>>> (digital identification signal) <<<<<<<<<TSI<<<<<<<<<<<         (optional) (transmitting subscriber identification) <<<<<<<<<DCS<<<<<<<<<< (digital command signal) <++++++++++TCF++++++++++ (high speed) (training check) >>>>>>>>>>>CFR>>>>>>>>>> (confirmation to receive) If you see FTT here that means TCF, training failed, check clocking and slips on T1/E1. In packet captures, check TCF should be all 0. <++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOM<<<<<<<< (partial page sent)/(end of message) >>>>>>>>> MCF>>>>>>>>>>> (message confirmation) <++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOP<<<<<<<< (partial page sent)/(end of procedure) >>>>>>>>> MCF>>>>>>>>>>> (message confirmation) <<<<<<<<<<DCN<<<<<<<<<< (disconnect) Note : ECM is Optional for G3, but Mandatory for SG3.  As you can achieve SG3 speeds with passthrough, make sure ECM is enabled on the fax machines for the fax to succeed. Also, TCF training signal is Required for G3, but is Not applicable for SG3. Note : For Passthrough a common channel of 64 kbps (g711) is allocated. So, the higher and the lower speeds of the messages become irrelevant. | If T38 switchover is successful, these messages are seen in the corresponding debugs: Check for VTSP shows: event:E_CC_T38_START Check for DSMP shows: E_DSM_CC_MC_LOCAL_DNLD_DONE debug fax relay t30 all-level-1 : timestamp=1321430729 fr-msg-det NSF timestamp=1321431129 fr-msg-det CSI timestamp=1321431879 fr-msg-det DIS timestamp=1321435719 fr-msg-tx TSI timestamp=1321436329 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321436329 fr-msg-tx good crc, 0 bytes timestamp=1321436439 fr-msg-tx DCS timestamp=1321436619 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321441499 fr-msg-det CFR timestamp=1321461449 fr-msg-tx PPS timestamp=1321461639 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321463099 fr-msg-det MCF timestamp=1321466789 fr-msg-tx DCN timestamp=1321466869 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=1321466869 fr-msg-tx good crc, 0 bytes GW-------------------------CUCM/GW >>>>>>>>> CSI>>>>>>>>>>> (optional) (called subscriber identification) >>>>>>>>> NSF>>>>>>>>>>> (optional) (nonstandard facilities) >>>>>>>>> DIS>>>>>>>>>>> (digital identification signal) <<<<<<<<<TSI<<<<<<<<<<<         (optional) (transmitting subscriber identification) <<<<<<<<<DCS<<<<<<<<<< (digital command signal) <++++++++++TCF++++++++++ (high speed) (training check) >>>>>>>>>>>CFR>>>>>>>>>> (confirmation to receive) If you see FTT here that means TCF, training failed, check clocking and slips on T1/E1. In packet captures, check TCF should be all 0. <++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOM<<<<<<<< (partial page sent)/(end of message) >>>>>>>>> MCF>>>>>>>>>>> (message confirmation) <++++Partial Page RX+++++++ (high speed) <<<<<<<<PPS/EOP<<<<<<<< (partial page sent)/(end of procedure) >>>>>>>>> MCF>>>>>>>>>>> (message confirmation) <<<<<<<<<<DCN<<<<<<<<<< (disconnect) |
| Protocol Based | NSE Based | Protocol Based | NSE Based |
| N/A | voice service voip level config: ## fax protocol none ## modem passthrough nse codec g711ulaw | N/A | voice service voip level config: # # fax protocol t38 nse force version 0 ls-redundancy 0 hs-redundancy 0 fallback none ## fax-relay sg3-to-g3 |

| Passthrough | T.38 Relay |
|---|---|
| Protocol Based | NSE Based | Protocol Based | NSE Based |
| Protocol Based switchover is not supported with SCCP. | GW----------------------CUCM/GW -------OffHookMessage-------> --KeypadButtonMessage----> <-------CallStateMessage------ CallStateMsg Info: PROCEED <----OpenReceiveChannel----- --OpenReceiveChannelAck--> <--StartMediaTransmission-- <-------CallStateMessage------ CallStateMsg Info: RINGOUT Check for VTSP shows : Fax Relay=DISABLED - SCCP Application Primary Fax Protocol=IGNORE_FAX_RELAY, Fallback Fax Protocol=IGNORE_FAX_RELAY Fax Relay CM Suppression : =ENABLED, Fax Relay ANS Suppression : =DISABLED Fax Parameters Set By= SCCP Call Type <-------CallStateMessage------ CallStateMsg Info: CONNECTED | Protocol Based switchover is not supported with SCCP. | GW----------------------CUCM/GW -------OffHookMessage-------> --KeypadButtonMessage----> <-------CallStateMessage------ CallStateMsg Info: PROCEED <----OpenReceiveChannel----- --OpenReceiveChannelAck--> <--StartMediaTransmission-- <-------CallStateMessage------ CallStateMsg Info: RINGOUT Check for VTSP shows : Fax Relay=ENABLED Primary Fax Protocol=T38_FAX_RELAY, Fallback Fax Protocol=NONE_FAX_RELAY Fax Relay CM Suppression : =ENABLED , Fax Relay ANS Suppression : =DISABLED Fax Parameters Set By= SCCP Call Type <-------CallStateMessage------ CallStateMsg Info: CONNECTED |
| GW-------------------------CUCM/GW <========AUDIO==========> Audio call established at this stage, but as FAX machines talk they exchange tones in the audio call. Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.) G3 Fax: >>>>>>>>>> CNG >>>>>>>>>>> 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. <<<<<<<<<< CED <<<<<<<<<<< 2100 Hz Tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path. SG3 Fax: >>>>>>>>>> CNG >>>>>>>>>>> 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. <<<<<<<<<< ANSAM <<<<<<<< 2100 Hz tone as CED, but amplitude modulated by a sine wave at 15 Hz with phase reversal every 450 ms. >>>>>>>>>> CM >>>>>>>>>>>> <<<<<<<<<< JM <<<<<<<<<<< < >>>>>>>>>> CJ >>>>>>>>>>>> V.34 Initialization (Phases 2-4) The OGW waits for the TGW to detect V.21 Preamble in the tones. Once TGW detects the V.21 Flag, it initiates switchover. One of the tasks in switchover is to make the Jitter buffer transitions from adaptive to a fixed optimum value. Fax passthrough uses the last voice mode setting before the switchover for jitter or playout buffers. Enter the show voice port X/X/X command in order to check the current values of playout delay. | GW-------------------------CUCM/GW <========AUDIO==========> Audio call established at this stage, but as fax machines talk they exchange tones in the audio call. Initial T.30 tones (Cannot be seen in debugs as these are always sent in RTP.) G3 Fax: >>>>>>>>>> CNG >>>>>>>>>>> 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. <<<<<<<<<< CED <<<<<<<<<<< 2100 Hz Tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path. SG3 Fax: >>>>>>>>>> CNG >>>>>>>>>>> 1100 Hz, every 3 seconds for .5 seconds. Indicates a calling nonspeech terminal. <<<<<<<<<< ANSAM <<<<<<<< 2100 Hz tone as CED, but amplitude modulated by a sine wave at 15 Hz with phase reversal every 450 ms. >>>CM>>X Cisco gateways only support G3 fax calls with T.38. In order to properly handle the higher speeds of SG3 calls, modem passthrough must be used. No V.34 Initialization (Phases 2-4) exist, the initial V.8 Phase I also does not complete. OGW squelches the CM tone and as SG3 is backward compatible with G3 fax standard, the fax machines failover to G3. <<<<<<<<<< CED <<<<<<<<<<< 2100 Hz Tone that lasts between 2.6 - 4.0 seconds. Disables echo suppressors in the transmission path. The OGW waits for the TGW to detect V.21 Preamble in the tones. Once TGW detects the V.21 Flag, it initiates switchover. One of the tasks in switchover is to make the Jitter buffer transitions from adaptive to a fixed optimum value. T.38 uses 300 ms fixed jitter or playout buffers. Enter the playout-delay fax 100 command under voice port to reduce the buffer time if the delay is high. Enter the show voice port X/X/X command in order to check the current values of playout delay. |
| Protocol Based | NSE Based | Protocol Based | NSE Based |
| Protocol Based switchover is not supported with SCCP. | G3 Fax: GW--------------------CUCM/GW <=======NSE192======== Upspeed Codec and Switch to Passthrough Mode. Check for VTSP shows : E_DSMP_DSP_REPORT_ PEER_TO_PEER _MSG debug voip rtp session named event : <<<Rcv> Pt:100    Evt:192     Pkt:00 00 00 ======NSE192=========> Check for VTSP shows : E_DSM_CC_MODIFY_MEDIA_IND debug voip rtp session named event : Pt:100    Evt:192    Pkt:00 00 00  <Snd>>> SG3 Fax: GW--------------------CUCM/GW <=======NSE192======== Upspeed Codec and Switch to Passthrough Mode. Check for VTSP shows : E_DSMP_DSP_REPORT_ PEER_TO_PEER _MSG debug voip rtp session named event <<<Rcv> Pt:100    Evt:192     Pkt:00 00 00 ======NSE192=========> Check for VTSP shows : E_DSM_CC_MODIFY_MEDIA_IND debug voip rtp session named event : Pt:100    Evt:192    Pkt:00 00 00  <Snd>>> <=======NSE193======== Disable ECAN. Check for VTSP shows : E_DSMP_DSP_REPORT_ PEER_TO_PEER _MSG debug voip rtp session named event : <<<Rcv> Pt:100    Evt:193     Pkt:00 00 00 ======NSE193=========> Check for VTSP shows : E_DSM_CC_MODIFY_MEDIA_IND debug voip rtp session named event : Pt:100    Evt:193    Pkt:00 00 00  <Snd>>> Note : NSE-194 is triggered by a local detection of 4 seconds of silence or carrier loss detection. This message instructs the remote gateway to return to voice mode. Basically, all the changes made by NSE-192 and NSE-193 are undone. show call active voice brief shows: MODEMPASS nse | Protocol Based switchover is not supported with SCCP. | G3 Fax: GW--------------------CUCM/GW <=======NSE200======== Transition from voice mode to T.38 Check for VTSP shows : E_DSMP_DSP_REPORT_ PEER_TO_PEER _MSG debug voip rtp session named event : <<<Rcv> Pt:100    Evt:200     Pkt:00 00 00 ======NSE201=========> T.38 ACK received, instructs TGW to start T.38 session Check for VTSP shows : E_DSM_CC_MODIFY_MEDIA_IND debug voip rtp session named event : Pt:100    Evt:201    Pkt:00 00 00  <Snd>>> SG3 Fax: As you squelch the CM tone in order to spoof SG3 to G3, there is no SG3 fax scenario in T38 relay. Note : NSE-202 is a NACK to an NSE-200 message which signifies that the peer gateway cannot process T.38 packets for the call. The call remains in voice mode and does not switch over to T.38. show call active voice brief shows: t38 |
| In Passthrough you cannot see any T.30 messages from debugs as all tones go in the RTP-like audio with G711ulaw/alaw. However, the fax tone negotiation remains the same irrespective of relay or passthrough. GW-------------------------CUCM/GW <<<<<<<<< CSI <<<<<<<<<<< (optional) (called subscriber identification) <<<<<<<<< NSF <<<<<<<<<<< (optional) (nonstandard facilities) <<<<<<<<< DIS <<<<<<<<<<< (digital identification signal) >>>>>>>>> TSI >>>>>>>>>>>> (optional) (transmitting subscriber identification) >>>>>>>>> DCS >>>>>>>>>>> (digital command signal) ++++++++++TCF+++++++++> (high speed) (training check) <<<<<<<<<<CFR<<<<<<<<<< (confirmation to receive) If you see FTT here that means TCF, training failed, check clocking and slips on T1/E1. In packet captures check TCF should be all 0. ++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message) <<<<<<<<< MCF <<<<<<<<<<< (message confirmation) ++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message) <<<<<<<<< MCF <<<<<<<<<<< (message confirmation) >>>>>>>>> DCN >>>>>>>>>>> (disconnect) Note : ECM is Optional for G3 but Mandatory for SG3. As you can achieve SG3 speeds with passthrough, make sure ECM is enabled on the fax machines for the fax to succeed. Also, TCF training signal is Required for G3, but is Not applicable for SG3. Note : For Passthrough a common channel of 64 kbps (g711) is allocated. So, the higher and the lower speeds of the messages become irrelevant. | If T38 switchover is successful, these messages are seen in the corresponding debugs: Check for VTSP shows : event:E_CC_T38_START Check for DSMP shows : E_DSM_CC_MC_LOCAL_DNLD_DONE debug fax relay t30 all-level-1 : timestamp=352583286 fr-msg-tx NSF timestamp=352583686 fr-msg-tx CSI timestamp=352583736 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352583736 fr-msg-tx good crc, 0 bytes timestamp=352584426 fr-msg-tx DIS timestamp=352584456 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352584456 fr-msg-tx good crc, 0 bytes timestamp=352584906 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352587656 fr-msg-det TSI timestamp=352588376 fr-msg-det DCS timestamp=352594056 fr-msg-tx CFR timestamp=352594156 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352613376 fr-msg-det PPS timestamp=352615656 fr-msg-tx MCF timestamp=352615776 FR_GOOD_CRC_LS_DATA 0x0 bytes timestamp=352618716 fr-msg-det DCN GW-------------------------CUCM/GW <<<<<<<<< CSI <<<<<<<<<<< (optional) (called subscriber identification) <<<<<<<<< NSF <<<<<<<<<<< (optional) (nonstandard facilities) <<<<<<<<< DIS <<<<<<<<<<< (digital identification signal) >>>>>>>>> TSI >>>>>>>>>>>> (optional) (transmitting subscriber identification) >>>>>>>>> DCS >>>>>>>>>>> (digital command signal) ++++++++++TCF+++++++++> (high speed) (training check) <<<<<<<<<< CFR <<<<<<<<<< (confirmation to receive) If you see FTT here that means TCF, training failed, check clocking and slips on T1/E1. In packet captures check TCF should be all 0. ++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message) <<<<<<<<< MCF <<<<<<<<<<< (message confirmation) ++++Partial Page RX++++++> (high speed) >>>>>>>>> PPS/EOM >>>>>>> (partial page sent)/(end of message) <<<<<<<<< MCF <<<<<<<<<<< (message confirmation) >>>>>>>>> DCN >>>>>>>>>>> (disconnect) |
| Protocol Based | NSE Based | Protocol Based | NSE Based |
| N/A | voice service voip level config: ## fax protocol none ## modem passthrough nse codec g711ulaw | N/A | voice service voip level config: # # fax protocol t38 nse force version 0 ls-redundancy 0 hs-redundancy 0 fallback none ## fax-relay sg3-to-g3 |

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 15-Jan-2015 | Initial Release |