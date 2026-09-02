---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-express-211258-configure-and-troubleshoot-cue-mwi-mecha--50612c15b4
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-express/211258-Configure-and-Troubleshoot-CUE-MWI-Mecha.html
retrieved_at: 2026-09-02T01:43:18.587825+00:00
---

Configure and Troubleshoot CUE MWI Mechanisms

# Configure and Troubleshoot CUE MWI Mechanisms

### Download Options

Updated: May 23, 2017

Document ID: 211258

Contents

## Contents

## Introduction

This document describres the different methods available to enable and disable the Message Waiting Indicator (MWI) on an Internet Protocol (IP) Phone, along with how to troubleshoot problems that arise when Cisco Unity Express (CUE) is integrated with Cisco Unified Communications Manager Express (CUCME).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Call Manager Express (CME) or CUCME

- Cisco Unity Express

- Skinny Call Control Protocol (SCCP)

- Session Initiation Protocol (SIP)

### Components Used

The information in this document is based on these software and hardware versions:

- CUE 7.x and 8.x. Sample configurations and screen captures are taken from CUE 7.0.6 and 8.6.2, installed on a NME-CUE module

- CUCME 7.1 and 8.5

- Cisco IP Phone 7965 registered with CUCME, with SCCP

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

### Related Products

This document can also be used with these hardware and software versions:

- Any CUE and CME version can be used

- Any CUE module or CME Router can be used

## Background Information

MWI is used to indicate a new message is left in the voice mailbox. To indicate a new message, the red lamp on the IP Phones is turned on along with the envelop icon next to the line display.

Note : This document is based on a CUCME server integrated with a CUE module.

There are three MWI Mechanisms available when CUE integrates with CUCME:

- Outcall

- SIP Subscribe-Notify

- SIP Unsolicited

There is one MWI mechanism available when CUE integrates with CUCM:

- Java Telephony API ( JTAPI)/ Computer Telephony Integration (CTI)

Note : The CUE JTAPI Issues and Case Studies document provides information on how to enable JTAPI Traces in CUE and how to troubleshoot MWI via JTAPI.

## Configure

### SIP Outcall Method

Outcall is the default method used in CUE in order to provide backward compatibility for available systems. Although it is recommended to use Subscribe-Notify or Unsolicited for the MWI notification, the Outcall method is used in several network environments to configure and enable MWI for SCCP IP Phones registered to CME.

Note : The Outcall mechanism does not work in Cisco Survivable Remote Site Telephony (SRST) deployments.  SIP endpoints are not supported.

In this mechanism, CUE sends an INVITE to CUCME when a user has a new voicemail.

Configure two ephone-dns on CUCME. The two DNs represent the extensions CUE must dial to enable or disable the MWI for a given extension.

```
ephone-dn 3 mwi on
 number 3999.... !
ephone-dn 4 mwi off
 number 3998....
```

Note : The number of dots at the end of the DN must match the extension length used by the phones registered to CUCME.

Ensure CUCME configuration is completed and then proceed to CUE configuration. In the intial configuration of CUE, the MWI DN's are automatically populated in the Call Handling section of the Initialization Wizard .

Note : To access the Initialization Wizard, CME must be integrated with CUE for Graphical User Interface (GUI) access. On a production system, the DN information is synchronized with CUE. Navigate to Voice Mail > Message Waiting Indicators > Settings to view the DNs.

Example MWI settings page after the DN's are configured and synchronized with CUE:

Note : Here Subscribe-Notify is also enabled. This is not required but it is supported to have Subscribe-Notify and Outcalling configured at the same time. CUE sends two notifications, one for each method, in order to turn on or off the MWI.

Note : Configuration of Outcall and Unsolicited Notify is not supported at the same time.

Sample CUE configuration:

```
ccn application ciscomwiapplication aa
  description "ciscomwiapplication"
  enabled
  maxsessions 6
  script "setmwi.aef" parameter "strMWI_OFF_DN" "3999"
  parameter "strMWI_ON_DN" "3998" end application
 
ccn subsystem sip mwi sip outcall
```

Use the show ccn subsystem sip command in order to determine the current MWI configuration.

```
CUE# sh ccn subsystem sip
SIP Gateway:                              10.10.202.1
SIP Port Number:                        5060
DTMF Relay:                               sip-notify,sub-notify MWI Notification:                                outcall MWI Envelope Info:                     disabled
Transfer Mode:                            bye-also
SIP RFC Compliance:                   Pre-RFC3261
```

Note : In the sample configuration, the MWI extensions are defined without dots. Dots are defined only in CME to indicate the phone DN extension length. The show ccn subsystem sip command output can vary based on CUE version.

Changes to dial-peer, used for CUE, are necessary in order to ensure the correct inbound dial-peer is matched for the Outcall SIP INVITE. A new dial-peer can also be created to act as the inbound dial-peer:

```
dial-peer voice 3600 voip 
destination-pattern 3600 
session protocol sipv2 
session target ipv4:10.10.202.50 incoming called-number 399[89].... dtmf-relay sip-notify 
codec g711ulaw 
no vad 
!
```

Or

```
dial-peer voice 3999 voip 
session protocol sipv2 incoming called-number 399[89].... dtmf-relay sip-notify 
codec g711ulaw 
no vad 
!
```

### SIP Subscribe Notify

In the Subscribe-Notify mechanism, the DNs initially Subscribe with the CUE. After subscription, the NOTIFY message from CUE is accepted for MWI notification.

Note :This method is recommended for SRST and CUCME deployments.

Enable Subscriber Notify inorder to use this notification method:

Alternatively, the Subscriber Notify method can be enabled on the Command Line Interface (CLI):

```
ccn subsystem sip
 gateway address "10.10.202.1" mwi envelope-info
 mwi sip sub-notify end subsystem
```

Configure the CME with the MWI server (CUE) IP address in the sip-ua section. You can confirm the IP address of the CUE from the Interface configuration of the Service Module on which the CUE is hosted with the show run interface command.

```
interface Integrated-Service-Engine1/0
 ip unnumbered Vlan400 service-module ip address 10.10.202.50 255.255.255.0 sip-ua mwi-server ipv4:10.10.202.50 expires 3600 port 5060 transport udp
```

The command mwi-server ipv4:10.10.202.50 under sip-ua is sufficient to support Subscribe-Notify events for MWI. The Expires , Port and Transport are automatically included in the configuration with the default settings.

Configure the DNs to Subscribe with the CUE in order to receive MWI notification event. This method can be used for SCCP and SIP IP Phones registered to the CME Router.

```
voice register dn 1
 number 3005 mwi !
ephone-dn  1 
 number 3001 mwi sip
```

Once the command is entered, the phone sends a SUBSCRIBE message to CUE in order to request a MWI Update and the CUE responds with a 202 Accepted SIP message:

```
Sent:
SUBSCRIBE sip:3001@10.10.202.50:5060 SIP/2.0 Via: SIP/2.0/UDP 10.10.202.1:5060;branch=z9hG4bK4812E5
From: <sip:3001@10.10.202.1>;tag=CC5F60-3EC
To: <sip:3001@10.10.202.50>
Call-ID: AE09C597-E3FE11E2-80F3BB44-39D4A3CF@10.10.202.1
CSeq: 101 SUBSCRIBE
Max-Forwards: 70
Date: Thu, 04 Jul 2013 16:36:15 GMT
User-Agent: Cisco-SIPGateway/IOS-12.x Event: message-summary Expires: 3600 Contact: <sip:3001@10.10.202.1:5060> Accept: application/simple-message-summary
Content-Length: 0 Received:
SIP/2.0 202 Accepted Via: SIP/2.0/UDP 10.10.202.1:5060;branch=z9hG4bK4812E5
To: <sip:3001@10.10.202.50>;tag=217fce13-1101
From: <sip:3001@10.10.202.1>;tag=CC5F60-3EC
Call-ID: AE09C597-E3FE11E2-80F3BB44-39D4A3CF@10.10.202.1
CSeq: 101 SUBSCRIBE
Content-Length: 0 Expires: 3600 Contact: sip:3001@10.10.202.50
Allow-Events: refer
Allow-Events: telephone-event Allow-Events: message-summary
```

Once the subscription is accepted, CUE sends a NOTIFY message with the current status of the MWI for that specific DN. In this example, the MWI Notification is set to Yes:

```
Received:
NOTIFY sip:3001@10.10.202.1:5060 SIP/2.0 Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~30
Max-Forwards: 70
To: <sip:3001@10.10.202.1>;tag=CC5F60-3EC
From: <sip:3001@10.10.202.50>;tag=217fce13-1101
Call-ID: AE09C597-E3FE11E2-80F3BB44-39D4A3CF@10.10.202.1
CSeq: 1 NOTIFY
Content-Length: 113 Contact: sip:3001@10.10.202.50 Event: message-summary Allow-Events: refer
Allow-Events: telephone-event
Allow-Events: message-summary Subscription-State: active Content-Type: application/simple-message-summary Messages-Waiting: yes
Message-Account: sip:3001@10.10.202.50 Voice-Message: 1/0 (0/0)
Fax-Message: 0/0 (0/0)
 
Sent:
SIP/2.0 200 OK
Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~30
From: <sip:3001@10.10.202.50>;tag=217fce13-1101
To: <sip:3001@10.10.202.1>;tag=CC5F60-3EC
Date: Thu, 04 Jul 2013 16:36:15 GMT
Call-ID: AE09C597-E3FE11E2-80F3BB44-39D4A3CF@10.10.202.1
CSeq: 1 NOTIFY
Content-Length: 0
```

On the CUE GUI, notice the Currently active subscriptions increments by 1 for each Subscribe message it receives:

Use show ccn sip subscription mwi command to view the subscription status.

```
DN                          Subscription Time                            Expires 
-------------------------------------------------------------------------------
 
3001                Mon Sep 22 13:40:02 EDT 2008                  3600
```

#### MWI Subscribe-Notifiy in SRST:

Configure mwi relay either under call-manager-fallback, for legacy SRST, or telephony-service for CME-SRST deployments.

```
call-manager-fallback mwi relay telephony-service mwi relay
```

### SIP Unsolicited-Notify

The SIP Unsolicited-Notify method supports both CUCME and SRST. This method uses a SIP NOTIFY message in order to toggle MWI on or off. Unlike with Subscribe-Notify there is no subscription maintaned by CUE.

Configure mwi relay command under call-manager-fallback or CME-SRST in order to support SRST deployments, along with the sip-ua MWI configuration command.

Enable the Unsolicited Notify option:

Alternatively Unsolicited Notify can be enabled on the CUE CLI:

```
ccn subsystem sip mwi sip unsolicited
```

Enable unsolicited notify on the CME CLI:

```
sip-ua
 mwi-server ipv4:10.10.202.50 expires 3600 port 5060 transport udp unsolicited
```

Warning : Unless unsolicited is configured on the mwi-server command, the CME continues to use Subscribe-Notify and MWI does not work since the configuration on CME does not match with the configuration on CUE.

Note : You cannot use the Unsolicitied-Notify mechanism along with any other mechanism at the same time.

### MWI with Cisco Unified Communications Manager (CUCM)

When CUE is integrated with CUCM the JTAPI protocol uses the setMessageWaiting message to toggle MWI on/off. The CTI Ports controlled by JTAPI are assigned with a Calling Search Space (CSS) that has the parition of the phone's Directory Number. In later releases of CUE, you can configure a dedicated CTI Port in order to provide MWI Notifications. In the event the port is not available, the CUE uses any available port configured that is controlled by JTAPI.

Since JTAPI uses the setMessageWaiting message for MWI events, MWI extensions are not configured in CUCM. If the extensions are configured, they are ignored and cause no interoperability issues with JTAPI.

In CUE versions 7.x and higher, you can configure the CUCME Router and CUE to use the Unsolicited-Notify method in order to maintain full MWI functionality while in SRST.

## Troubleshoot

This section provides information you can use in order to troubleshoot your configuration.

### Debugs and Traces

#### CUCME

In order to troubleshoot MWI issues, use these debugs:

```
debug ccsip messages
debug voice ccapi inout
```

In order to troubleshoot MWI issues with SCCP Phones registered to a CUCME Router with MWI outcall method, use these debugs:

```
debug ccsip messages
debug voice ccapi inout debug ephone mwi mac <mac address> debug ephone detail mac <mac address>
```

The show ephone reg command is used to confirm the status of MWI regardless of the mechanism used. This is a useful command when the phone is located in a remote site.

```
#show ephone reg
ephone-1[0] Mac:0023.5E18.23EC TCP socket:[1] activeLine:0 whisperLine:0 REGISTERED in SCCP ver 17/12 max_streams=5
mediaActive:0 whisper_mediaActive:0 startMedia:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:1 caps:9 privacy:1
IP:10.10.202.2 22856 7965  keepalive 186 max_line 6 available_line 6
button 1: dn 1  number 3001 CH1   IDLE         CH2   IDLE         CH3   IDLE         CH4   IDLE         CH5   IDLE         CH6   IDLE         CH7   IDLE         CH8   IDLE mwi Preferred Codec: g711ulaw
Username: MWI1 Password: cisco
```

#### CUE

In CUE you can use these show commands in order to verify your configuration:

```
show ccn application
show ccn subsystem sip
```

CUE also provides traces in order to troubleshoot any issues related to MWI. You can either use the default traces already enabled in CUE or use a specific trace which is easier to collect and read.

The specific trace you can enable in CUE is:

```
trace ccn stacksip dbug
```

This trace provides SIP signaling information useful in order to determine if the SIP Outcall or Notify message is sent correctly for MWI.

You can also enable the trace voicemail all in combination with the stacksip trace in order to get more information about the call and MWI events, or at a minimum enable the trace voicemail vxml all and trace voicemail mwi all.

Note : For more information about MWI Problems refer to the Troubleshooting Unity Express Message Waiting Indication (MWI) Problems .

### CUE Licensing

In CUE, ensure licenses are installed in order to support the correct call agent (CUCME or CUCM) and voicemail ports.

In CUE version 7.0.x  the command is show software licenses.

```
CUE# show software licenses
Installed license files:
 - voicemail_lic.sig : 25 MAILBOX LICENSE
 - ivr_lic.sig : 4 PORT IVR BASE LICENSE - port_lic.sig : 24 PORT BASE LICENSE Core:
 - Application mode: CCME
 - Total usable system ports: 24 Voicemail/Auto Attendant:
 - Max system mailbox capacity time: 18000
 - Default # of general delivery mailboxes: 10
 - Default # of personal mailboxes: 25
 
 - Max # of configurable mailboxes: 35
 
Interactive Voice Response:
 - Max # of IVR sessions: 4
 
Languages:
 - Max installed languages: 5
 - Max enabled languages: 5
```

In CUE 7.1.x and later the commands are show license status application and show call-agent

```
CUE# show license status application voicemail enabled: 10 ports , 10 sessions, 30 mailboxes
ivr disabled, ivr session activation count has been set to zero
 
CUE# show call-agent Call-agent:         CUCME
```

You can also use the show license all which provides detailed information about the licenses. This show command is useful in order to determine if the CUE has evaluation licenses and how much time is left before it expires or if the licenses installed are permanent:

```
CUE# show license all License Store: Primary License Storage
StoreIndex:  0  Feature: VMIVR-VM-MBX                      Version: 1.0
        License Type: Permanent
        License State: Active, In Use
        License Count: 65 /30
        License Priority: Medium
License Store: Primary License Storage
StoreIndex:  1  Feature: VMIVR-IVR-SESS                    Version: 1.0
        License Type: Permanent
        License State: Active, Not in Use
        License Count: 10 / 0
        License Priority: Medium
License Store: Primary License Storage
StoreIndex:  2  Feature: TCV-USER                          Version: 1.0
        License Type: Permanent
        License State: Active, Not in Use
        License Count: 60 / 0
        License Priority: Medium
License Store: Primary License Storage StoreIndex:  3  Feature: VMIVR-PORT Version: 1.0 License Type: Permanent License State: Active, In Use License Count: 20 /10 License Priority: Medium
License Store: Evaluation License Storage
```

### Troubleshoot SIP Outcall

The SIP Outcall method generates a SIP call event to CUCME in order to toggle on or off the MWI for one specific extension. CUE waits for the 180 Ringing message. Once it is received, then it can disconnect the call.

In CUE:

```
CUE# no trace all #trace ccn StackSip dbug # clear trace
#mwi refresh telephonenumber 3001
#show trace buff tail
Press <CTRL-C> to exit...
4524 07/04 09:35:16.484 ACCN STGN 0 Task: 263000000018 GetListMember: output string:outcall 4524 07/04 09:35:16.489 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTINGenter connect
4524 07/04 09:35:16.489 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTINGenter createInvitation
4524 07/04 09:35:16.489 ACCN SIPL 0 SDPBody : v=0
o=CiscoSystemsSIP-Workflow-App-UserAgent 3337 3337 IN IP4 10.10.202.50
s=SIP Call
c=IN IP4 10.10.202.50
t=0 0
m=audio 16910 RTP/AVP 0
a=rtpmap:0 pcmu/8000
a=ptime:20
 
4524 07/04 09:35:16.489 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTINGbefore invitationmanager.createInvitation. body : v=0
o=CiscoSystemsSIP-Workflow-App-UserAgent 3337 3337 IN IP4 10.10.202.50
s=SIP Call
c=IN IP4 10.10.202.50
t=0 0
m=audio 16910 RTP/AVP 0
a=rtpmap:0 pcmu/8000
a=ptime:20
body type : application/sdp toNA : <sip:39993001@10.10.202.1:5060;user=phone> fromNA : <sip:3602@10.10.202.50:5060> from tag : cue5aa7689b
4524 07/04 09:35:16.489 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTINGafter invitationmanager.createInvitation
4524 07/04 09:35:16.489 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTING added ciscogcid
4524 07/04 09:35:16.489 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTING getDTMFHeader: Enter
4524 07/04 09:35:16.489 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTING getDTMFHeader: getting the headers
4524 07/04 09:35:16.490 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTING getDTMFHeader: before adding headers to message
4524 07/04 09:35:16.490 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTING getDTMFHeader: after adding headers to message : INVITE sip:39993001@10.10.202.1:5060;user=phone SIP/2.0 Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~10
Max-Forwards: 70
To: <sip:39993001@10.10.202.1:5060;user=phone>
From: <sip:3602@10.10.202.50:5060>;tag=cue5aa7689b
Call-ID: 137295211648821@10.10.202.50
CSeq: 1 INVITE
Content-Length: 178
Contact: <sip:3602@10.10.202.50:5060>
Content-Type: application/sdp
Cisco-Gcid: AA52BD08-013F-1000-4000-001125CUCE68
Call-Info: <sip:10.10.202.50:5060>;method="NOTIFY;Event=telephone-event;Duration=2000"
Allow-Events: telephone-event
 
v=0
o=CiscoSystemsSIP-Workflow-App-UserAgent 3337 3337 IN IP4 10.10.202.50
s=SIP Call
c=IN IP4 10.10.202.50
t=0 0
m=audio 16910 RTP/AVP 0
a=rtpmap:0 pcmu/8000
a=ptime:20
 
4524 07/04 09:35:16.490 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTINGinvite message : INVITE sip:39993001@10.10.202.1:5060;user=phone SIP/2.0
Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~10
Max-Forwards: 70
To: <sip:39993001@10.10.202.1:5060;user=phone>
From: <sip:3602@10.10.202.50:5060>;tag=cue5aa7689b
Call-ID: 137295211648821@10.10.202.50
CSeq: 1 INVITE
Content-Length: 178
Contact: <sip:3602@10.10.202.50:5060>
Content-Type: application/sdp
Cisco-Gcid: AA52BD08-013F-1000-4000-001125CUCE68
Call-Info: <sip:10.10.202.50:5060>;method="NOTIFY;Event=telephone-event;Duration=2000"
Allow-Events: telephone-event
 
v=0
o=CiscoSystemsSIP-Workflow-App-UserAgent 3337 3337 IN IP4 10.10.202.50
s=SIP Call
c=IN IP4 10.10.202.50
t=0 0
m=audio 16910 RTP/AVP 0
a=rtpmap:0 pcmu/8000
a=ptime:20
 
4524 07/04 09:35:16.490 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTINGreturning invitation
4524 07/04 09:35:16.490 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTINGgot Invitation
4524 07/04 09:35:16.490 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTINGbefore Invitation start
4524 07/04 09:35:16.491 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTINGafter Invitation start
4846 07/04 09:35:16.509 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTING InvitationCallback.proceeding
4846 07/04 09:35:16.509 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTING SIP/2.0 100 Trying Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~10
To: <sip:39993001@10.10.202.1:5060;user=phone>
From: <sip:3602@10.10.202.50:5060>;tag=cue5aa7689b
Call-ID: 137295211648821@10.10.202.50
CSeq: 1 INVITE
Content-Length: 0
Date: Thu, 04 Jul 2013 15:50:11 GMT
Allow-Events: telephone-event
Server: Cisco-SIPGateway/IOS-12.x
 
 
4846 07/04 09:35:16.515 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTING--- InvitationCallback.proceeding (dialog)
4846 07/04 09:35:16.515 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTING SIP/2.0 180 Ringing Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~10
To: <sip:39993001@10.10.202.1:5060;user=phone>;tag=A233D8-2382
From: <sip:3602@10.10.202.50:5060>;tag=cue5aa7689b
Call-ID: 137295211648821@10.10.202.50
CSeq: 1 INVITE
Content-Length: 0
Date: Thu, 04 Jul 2013 15:50:11 GMT
Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER
Allow-Events: telephone-event
Remote-Party-ID: <sip:39990000@10.10.202.1>;party=called;screen=no;privacy=off
Contact: <sip:39993001@10.10.202.1:5060>
Server: Cisco-SIPGateway/IOS-12.x
 
 
4524 07/04 09:35:21.489 ACCN SIPL 0 sip-ltp17: 3602, State=CONTACTING terminating dialog in contacting state 20
4524 07/04 09:35:21.491 ACCN SIPL 0 sip-ltp17: 3602, State=TERMINATEDcontacting state hangup
4524 07/04 09:35:21.492 ACCN SIPL 0 sip-ltp17: 3602, State=TERMINATEDAfter contacting state hangup
4846 07/04 09:35:21.507 ACCN SIPL 0 sip-ltp17: 3602, State=TERMINATED InvitationDialogCallback.rejected
4846 07/04 09:35:21.508 ACCN SIPL 0 sip-ltp17: 3602, State=TERMINATED SIP/2.0 487 Request Cancelled Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~10
To: <sip:39993001@10.10.202.1:5060;user=phone>;tag=A233D8-2382
From: <sip:3602@10.10.202.50:5060>;tag=cue5aa7689b
Call-ID: 137295211648821@10.10.202.50
CSeq: 1 INVITE
Content-Length: 0
Date: Thu, 04 Jul 2013 15:50:16 GMT
Allow-Events: telephone-event
Server: Cisco-SIPGateway/IOS-12.x
Reason: Q.850;cause=16
```

In CUCME:

```
Received: INVITE sip:39983001@10.10.202.1:5060;user=phone SIP/2.0 Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~3
Max-Forwards: 70
To: <sip:39983001@10.10.202.1:5060;user=phone>
From: <sip:3602@10.10.202.50:5060>;tag=cue9c19e76c
Call-ID: 13729499207617@10.10.202.50
CSeq: 1 INVITE
Content-Length: 178
Contact: <sip:3602@10.10.202.50:5060>
Content-Type: application/sdp
Cisco-Gcid: AA313BF9-013F-1000-4000-001125CUCE68
Call-Info: <sip:10.10.202.50:5060>;method="NOTIFY;Event=telephone-event;Duration=2000"
Allow-Events: telephone-event
 
v=0
o=CiscoSystemsSIP-Workflow-App-UserAgent 3068 3068 IN IP4 10.10.202.50
s=SIP Call
c=IN IP4 10.10.202.50
t=0 0
m=audio 16928 RTP/AVP 0
a=rtpmap:0 pcmu/8000
a=ptime:20
 
  //-1/21F6E0878040/CCAPI/cc_api_display_ie_subfields: cc_api_call_setup_ind_common:
   cisco-username=3602
   ----- ccCallInfo IE subfields ----- cisco-ani=3602 cisco-anitype=0
   cisco-aniplan=0
   cisco-anipi=0
   cisco-anisi=0 dest=39983001 //-1/21F6E0878040/CCAPI/cc_api_call_setup_ind_common:
   Interface=0x49432FE0, Call Info(
   Calling Number=3602,(Calling Name=)(TON=Unknown, NPI=Unknown, Screening=Not Screened, Presentation=Allowed),
   Called Number=39983001(TON=Unknown, NPI=Unknown),
   Calling Translated=FALSE, Subscriber Type Str=Unknown, FinalDestinationFlag=TRUE, Incoming Dial-peer=3600 , Progress Indication=NULL(0), Calling IE Present=TRUE,
   Source Trkgrp Route Label=, Target Trkgrp Route Label=, CLID Transparent=FALSE), Call Id=22
…
 
//22/21F6E0878040/CCAPI/cc_api_display_ie_subfields:
   ccCallSetupRequest:
   cisco-username=3602
   ----- ccCallInfo IE subfields ----- cisco-ani=3602 cisco-anitype=0
   cisco-aniplan=0
   cisco-anipi=0
   cisco-anisi=0 dest=39983001 //22/21F6E0878040/CCAPI/ccIFCallSetupRequestPrivate:
   Interface=0x4A492188, Interface Type=6, Destination=, Mode=0x0,
   Call Params(Calling Number=3602,(Calling Name=)(TON=Unknown, NPI=Unknown, Screening=Not Screened, Presentation=Allowed),
   Called Number=39983001(TON=Unknown, NPI=Unknown), Calling Translated=FALSE,
   Subscriber Type Str=Unknown, FinalDestinationFlag=TRUE, Outgoing Dial-peer=20004, Call Count On=FALSE,
   Source Trkgrp Route Label=, Target Trkgrp Route Label=, tg_label_flag=0, Application Call Id=) Sent:
SIP/2.0 100 Trying Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~3
From: <sip:3602@10.10.202.50:5060>;tag=cue9c19e76c
To: <sip:39983001@10.10.202.1:5060;user=phone>
Date: Thu, 04 Jul 2013 15:13:36 GMT
Call-ID: 13729499207617@10.10.202.50
CSeq: 1 INVITE
Allow-Events: telephone-event
Server: Cisco-SIPGateway/IOS-12.x
Content-Length: 0 Sent:
SIP/2.0 180 Ringing Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~3
From: <sip:3602@10.10.202.50:5060>;tag=cue9c19e76c
To: <sip:39983001@10.10.202.1:5060;user=phone>;tag=80B2C0-1CF
Date: Thu, 04 Jul 2013 15:13:36 GMT
Call-ID: 13729499207617@10.10.202.50
CSeq: 1 INVITE
Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER
Allow-Events: telephone-event
Remote-Party-ID: <sip:39980000@10.10.202.1>;party=called;screen=no;privacy=off
Contact: <sip:39983001@10.10.202.1:5060>
Server: Cisco-SIPGateway/IOS-12.x
Content-Length: 0 Received:
CANCEL sip:39983001@10.10.202.1:5060;user=phone SIP/2.0 Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~3
Max-Forwards: 70
To: <sip:39983001@10.10.202.1:5060;user=phone>
From: <sip:3602@10.10.202.50:5060>;tag=cue9c19e76c
Call-ID: 13729499207617@10.10.202.50
CSeq: 1 CANCEL
Content-Length: 0 //22/21F6E0878040/CCAPI/cc_api_call_disconnected:
   Cause Value=16, Interface=0x49432FE0, Call Id=22 Sent:
SIP/2.0 200 OK Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~3
From: <sip:3602@10.10.202.50:5060>;tag=cue9c19e76c
To: <sip:39983001@10.10.202.1:5060;user=phone>
Date: Thu, 04 Jul 2013 15:13:41 GMT
Call-ID: 13729499207617@10.10.202.50
CSeq: 1 CANCEL
Content-Length: 0 Sent:
SIP/2.0 487 Request Cancelled Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~3
From: <sip:3602@10.10.202.50:5060>;tag=cue9c19e76c
To: <sip:39983001@10.10.202.1:5060;user=phone>;tag=80B2C0-1CF
Date: Thu, 04 Jul 2013 15:13:41 GMT
Call-ID: 13729499207617@10.10.202.50
CSeq: 1 INVITE
Allow-Events: telephone-event
Server: Cisco-SIPGateway/IOS-12.x
Reason: Q.850;cause=16
Content-Length: 0 Received:
ACK sip:39983001@10.10.202.1:5060;user=phone SIP/2.0 Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~3
Max-Forwards: 70
To: <sip:39983001@10.10.202.1:5060;user=phone>;tag=80B2C0-1CF
From: <sip:3602@10.10.202.50:5060>;tag=cue9c19e76c
Call-ID: 13729499207617@10.10.202.50
CSeq: 1 ACK
Content-Length: 0 Debug ephone mwi: 000922: Jul  4 10:23:22.654: SetCallInfo MODE 1 calling dn -1 chan 1 dn 3 chan 1 000923: Jul  4 10:23:22.654: alling [3602] called [39993001] 000924: Jul  4 10:23:22.654: SkinnyTryCall to 3001 instance 1 start at 0SkinnyTryCall to 3001 instance 1 match DN 1 000925: Jul  4 10:23:22.654: ephone-1[1]:Set MWI line 1 to ON count 0 000926: Jul  4 10:23:22.654: ephone-1[1]:Set MWI line 0 to ON count 0 Debug ephone detailed: 001231: Jul  4 10:25:37.899: Phone 0 DN 1 MWI on 0 messages 001232: Jul  4 10:25:37.899: ephone-1[1]:Set MWI line 1 to ON count 0 001233: Jul  4 10:25:37.899: ephone-1[1]:Set MWI line 0 to ON count 0
```

### Troubleshoot SIP Subscribe-Notify

After the initial subscription of the DNs, CUE sends a Notify Message towards CUCME in order to inform which extension needs to have the MWI toggle on or off.

In CUE:

```
CUE#no trace all CUE#trace ccn stacksip dbug
CUE#trace voicemail all CUE# clear trace
CUE#mwi refresh telephonenumber 3001
CUE#show trace buff tail
Press <CTRL-C> to exit...

4430 07/04 10:43:39.263 VMSS dbug 1 com.cisco.aesop.voicemail.LdapAgent : getAttributeValue: /sw/local/users/MWI1/TelephoneNumbers/primaryExtension
4430 07/04 10:43:39.264 VMSS vmwi 0x00000000000f1206 2 3001,true
4430 07/04 10:43:39.264 VMSS dbug 1 com.cisco.aesop.voicemail.Mailbox : setMessageWaiting: 3001,true 4430 07/04 10:43:39.264 VMSS vmdb 0 Request connection: inUse: 1, active: 2
4430 07/04 10:43:39.264 VMSS dbug 1 com.cisco.aesop.voicemail.VMDatabase : Request connection: inUse: 1, active: 2
4430 07/04 10:43:39.264 VMSS vmdb 0 Got connection: 1, inUse: 2, active: 2
4430 07/04 10:43:39.264 VMSS dbug 1 com.cisco.aesop.voicemail.VMDatabase : Got connection: 1, inUse: 2, active: 2
4430 07/04 10:43:39.264 VMSS vmdb 7 select uid from vm_message   where vm_message.messageid='FTX1242A3S6-NME-FOC12394L3Y-1372949852538' ;
4430 07/04 10:43:39.264 VMSS dbug 1 com.cisco.aesop.voicemail.VMDatabase : select uid from vm_message   where vm_message.messageid='FTX1242A3S6-NME-FOC12394L3Y-1372949852538' ;
4430 07/04 10:43:39.273 VMSS vmdb 3 PERSONAL_00000000000000000000000
4430 07/04 10:43:39.273 VMSS dbug 1 com.cisco.aesop.voicemail.VMDatabase : PERSONAL_00000000000000000000000
4430 07/04 10:43:39.273 VMSS dbug 1 com.cisco.aesop.voicemail.VMUser : getMailboxInfo: personalMailboxId=PERSONAL_00000000000000000000000
4430 07/04 10:43:39.273 VMSS vmdb 0 Freed connection: 1, inUse: 1, active: 2
4430 07/04 10:43:39.273 VMSS dbug 1 com.cisco.aesop.voicemail.VMDatabase : Freed connection: 1, inUse: 1, active: 2
4430 07/04 10:43:39.273 VMSS vmsg 8 populateSenderDetails: sender entity: id=MW2,type=1,ext=3002,cn=MW2,desc=
4430 07/04 10:43:39.273 VMSS vmsg 8 populateSenderDetails: localPart=MW2
4430 07/04 10:43:39.273 VMSS vmsg 8 populateSenderDetails: imapSender="MW2 \(MW2\)" <MW2@localdomain>, mwiFrom="MW2" <sip:3002@sip.invalid>, subjectLine=3002
4430 07/04 10:43:39.273 VMSS dbug 1 com.cisco.aesop.voicemail.Message : getLengthMillisec(): msgid: FTX1242A3S6-NME-FOC12394L3Y-1372949852538 totalMsgLength: 14287
4430 07/04 10:43:39.273 VMSS dbug 1 com.cisco.aesop.voicemail.Message : getLengthMillisec(): msgid: FTX1242A3S6-NME-FOC12394L3Y-1372949852538 totalMsgLength: 14287
4430 07/04 10:43:39.274 VMSS vmwi 4 MessageWaitingThread.addJob: Messages-Waiting: yes
Message-Account: sip:3001@10.10.202.50 Voice-Message: 1/0 (0/0)
Fax-Message: 0/0 (0/0)
 
X-Cisco-Message-State: new
X-Cisco-Message-Type: normal
From: "MW2" <sip:3002@sip.invalid>
To: <sip:3001@sip.invalid>
Date: Thu, 4 Jul 2013 16:43:39 GMT
Message-ID: FTX1242A3S6-NME-FOC12394L3Y-1372949852538
Message-Context: voice-message
Content-Duration: 14
 
4430 07/04 10:43:39.274 VMSS vmwi 4 MessageWaitingThread.addJob: numJobs=1
4430 07/04 10:43:39.274 VMSS dbug 1 MessageWaitingThread : adding job
4430 07/04 10:43:39.274 VMSS vmdb 0x00000000000f1206 7 update vm_message set mwion=true where messageid='FTX1242A3S6-NME-FOC12394L3Y-1372949852538'; 4430 07/04 10:43:39.274 VMSS dbug 1 com.cisco.aesop.voicemail.VMDatabase : taskId: 987654(0xf1206): update vm_message set mwion=true where messageid='FTX1242A3S6-NME-FOC12394L3Y-1372949852538';
4430 07/04 10:43:39.274 VMSS dbug 1 com.cisco.aesop.voicemail.VMDatabase : connection 0: execute: update vm_message set mwion=true where messageid='FTX1242A3S6-NME-FOC12394L3Y-1372949852538';
3450 07/04 10:43:39.274 VMSS vmwi 4 MessageWaitingThread.run: extn=3001, numJobs=0
3450 07/04 10:43:39.274 VMSS vmwi 4 http://localhost:8080/mwiapp?extn=3001&state=1
3450 07/04 10:43:39.274 VMSS dbug 1 com.cisco.aesop.voicemail.MessageWaitingThread : http://localhost:8080/mwiapp?extn=3001&state=1 4522 07/04 10:43:39.289 ACCN STGN 0 Task: 263000000053GetListMember: output string:sub-notify
```

In CUCME:

```
Received: NOTIFY sip:3001@10.10.202.1:5060 SIP/2.0 Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~26
Max-Forwards: 70
To: <sip:3001@10.10.202.1>;tag=C253E4-7B4
From: <sip:3001@10.10.202.50>;tag=a4c2d6ba-1099
Call-ID: 25A81829-E3FD11E2-80C3BB44-39D4A3CF@10.10.202.1
CSeq: 5 NOTIFY
Content-Length: 113 Contact: sip:3001@10.10.202.5 0
Event: message-summary
Allow-Events: refer
Allow-Events: telephone-event Allow-Events: message-summary Subscription-State: active Content-Type: application/simple-message-summary Messages-Waiting: yes
Message-Account: sip:3001@10.10.202.50 Voice-Message: 1/0 (0/0)
Fax-Message: 0/0 (0/0)
 
Sent:
SIP/2.0 200 OK
Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~26
From: <sip:3001@10.10.202.50>;tag=a4c2d6ba-1099
To: <sip:3001@10.10.202.1>;tag=C253E4-7B4
Date: Thu, 04 Jul 2013 16:33:26 GMT
Call-ID: 25A81829-E3FD11E2-80C3BB44-39D4A3CF@10.10.202.1
CSeq: 5 NOTIFY
Content-Length: 0
```

### Troubleshoot SIP Unsolicited

CUE sends a NOTIFY message to CUCME. No prior subscription is required.

In CUE:

```
2922 07/04 11:07:59.028 VMSS vmwi 0x00000000000f1206 2 3001,true
2922 07/04 11:07:59.028 VMSS dbug 1 com.cisco.aesop.voicemail.Mailbox : setMessageWaiting: 3001,true 2922 07/04 11:07:59.029 VMSS vmwi 4 MessageWaitingThread.addJob: Messages-Waiting: yes
Message-Account: sip:3001@10.10.202.50 Voice-Message: 2/0 (0/0)
Fax-Message: 0/0 (0/0)
 
2922 07/04 11:07:59.029 VMSS vmwi 4 MessageWaitingThread.addJob: numJobs=1
2922 07/04 11:07:59.029 VMSS dbug 1 MessageWaitingThread : adding job
3450 07/04 11:07:59.029 VMSS vmwi 4 MessageWaitingThread.run: extn=3001, numJobs=0
3450 07/04 11:07:59.029 VMSS vmwi 4 http://localhost:8080/mwiapp?extn=3001&state=1
3450 07/04 11:07:59.029 VMSS dbug 1 com.cisco.aesop.voicemail.MessageWaitingThread : http://localhost:8080/mwiapp?extn=3001&state=1
2924 07/04 11:07:59.037 VMSS sydb 1 MailboxNode: PERSONAL_00000000000000000000000,ownerDn
2924 07/04 11:07:59.037 VMSS dbug 1 com.cisco.aesop.voicemail.VMSysdbMailboxNode : Get attribute: ownerDn Mailbox: PERSONAL_00000000000000000000000
2921 07/04 11:07:59.039 VMSS sydb 1 MailboxNode: PERSONAL_00000000000000000000000,mailboxDesc
2921 07/04 11:07:59.039 VMSS dbug 1 com.cisco.aesop.voicemail.VMSysdbMailboxNode : Get attribute: mailboxDesc Mailbox: PERSONAL_00000000000000000000000
4524 07/04 11:07:59.041 ACCN STGN 0 Task: 263000000060GetListMember: output string:unsolicited
4524 07/04 11:07:59.041 ACCN STGN 0 Task: 263000000060GetListMember: Position variable is beyond the string list: number of tokens in the list:1
4524 07/04 11:07:59.041 ACCN SIPL 0 SubscriptionLineImpl: Unsolicited Notify Message being sent:NOTIFY sip:3001@10.10.202.1:5060;transport=udp SIP/2.0
Max-Forwards: 70
To: <sip:3001@10.10.202.1:5060>
From: <sip:3001@10.10.202.50:5060>;tag=ds9b9149a8
Call-ID: a5244b0b-1105@sip:3001@10.10.202.50:5060
CSeq: 1 NOTIFY
Content-Length: 113
Contact: <sip:3001@10.10.202.50:5060>
Content-Type: application/simple-message-summary
Event: message-summary Messages-Waiting: yes
Message-Account: sip:3001@10.10.202.50 Voice-Message: 2/0 (0/0)
Fax-Message: 0/0 (0/0) 4524 07/04 11:07:59.052 ACCN SIPL 0 SubscriptionLineImpl: Unsolicited Notify Message sent, result:true
4524 07/04 11:08:09.053 ACCN SIPL 0 SubscriptionLineImpl: Unsolicited Notify Message sent, result:true
```

In CUCME:

```
Received: NOTIFY sip:3001@10.10.202.1:5060;transport=udp SIP/2.0 Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~44
Max-Forwards: 70
To: <sip:3001@10.10.202.1:5060>
From: <sip:3001@10.10.202.50:5060>;tag=ds3f77b499
Call-ID: 7364fb7c-1104@sip:3001@10.10.202.50:5060
CSeq: 1 NOTIFY
Content-Length: 113
Contact: <sip:3001@10.10.202.50:5060>
Content-Type: application/simple-message-summary
Event: message-summary Messages-Waiting: yes
Message-Account: sip:3001@10.10.202.50 Voice-Message: 1/0 (0/0)
Fax-Message: 0/0 (0/0)
 
Sent:
SIP/2.0 200 OK
Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bKkuJtPQPUKbreuy0GkQBlQw~~44
From: <sip:3001@10.10.202.50:5060>;tag=ds3f77b499
To: <sip:3001@10.10.202.1:5060>;tag=F07F98-117C
Date: Thu, 04 Jul 2013 17:15:43 GMT
Call-ID: 7364fb7c-1104@sip:3003@10.10.202.50:5060
CSeq: 1 NOTIFY
Content-Length: 0
```

### Common Issues

#### Issue 1. MWI does not work after SIP bind Commands

SIP Bind commands are configured under voice service voip to an interface that is not the one used for CUE. This is a very common issue and tricky to detect with the troubleshoot tools inside CME. From a CME point of view there are no SIP messages shown.

In CME if you run debug ip udp you can notice packets from CUE but no messages shown in debug ccsip messages or debug ccsip all:

```
000186: *Jul  8 17:30:48.843: UDP: rcvd src=10.10.202.50(32777), dst=10.10.202.1(5060), length=748
000187: *Jul  8 17:30:49.343: UDP: rcvd src=10.10.202.50(32777), dst=10.10.202.1(5060), length=748
000188: *Jul  8 17:30:50.347: UDP: rcvd src=10.10.202.50(32777), dst=10.10.202.1(5060), length=748
000189: *Jul  8 17:30:52.351: UDP: rcvd src=10.10.202.50(32777), dst=10.10.202.1(5060), length=748
000190: *Jul  8 17:30:56.351: UDP: rcvd src=10.10.202.50(32777), dst=10.10.202.1(5060), length=748
000191: *Jul  8 17:31:04.355: UDP: rcvd src=10.10.202.50(32777), dst=10.10.202.1(5060), length=748
```

If a packet capture is collected directly from the CUE interface with ip traffic export you can notice the INVITE is indeed received by CUCME:

In CUE the INVITE is shown as sent, although since there is no response from CUCME, it continues to send INVITEs until the retry count is reached, then the connection is terminated due to no response:

```
4480 07/08 10:30:59.377 ACCN HTTS 0 -> AInvoker.doGet() (/mwiapp) EXIT
4901 07/08 10:31:01.858 DSSP LWRE 0 Sending UDP packet on 10.10.202.50:32775, destination 10.10.202.1:5060 INVITE sip:39993001@10.10.202.1:5060;user=phone SIP/2.0 Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bK51VhKqo+pUDrDt5LgLS2yA~~5
Max-Forwards: 70
To: <sip:39993001@10.10.202.1:5060;user=phone>
From: <sip:3@10.10.202.50:5060>;tag=cuefb95dbea
Call-ID: 137330105434811@10.10.202.50
CSeq: 1 INVITE
Content-Length: 178
Contact: <sip:3@10.10.202.50:5060>
Content-Type: application/sdp
Cisco-Gcid: BF1F1B8C-013F-1000-4000-001125CUCE68
Call-Info: <sip:10.10.202.50:5060>;method="NOTIFY;Event=telephone-event;Duration=2000"
Allow-Events: telephone-event
 
v=0
o=CiscoSystemsSIP-Workflow-App-UserAgent 2956 2956 IN IP4 10.10.202.50
s=SIP Call
c=IN IP4 10.10.202.50
t=0 0
m=audio 16926 RTP/AVP 0
a=rtpmap:0 pcmu/8000
a=ptime:20
 
4488 07/08 10:31:04.355 ACCN ENGN 0 Record 544481396 enqueued. Queue size=0 total number of writes=10
4863 07/08 10:31:04.359 ACCN ENGN 0 Insert Record 544481396 took 3ms finish at 1373301064359
4903 07/08 10:31:09.860 DSSP LWRE 0 Sending UDP packet on 10.10.202.50:32775, destination 10.10.202.1:5060 INVITE sip:39993001@10.10.202.1:5060;user=phone SIP/2.0 Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bK51VhKqo+pUDrDt5LgLS2yA~~5
Max-Forwards: 70
To: <sip:39993001@10.10.202.1:5060;user=phone>
From: <sip:3@10.10.202.50:5060>;tag=cuefb95dbea
Call-ID: 137330105434811@10.10.202.50
CSeq: 1 INVITE
Content-Length: 178
Contact: <sip:3@10.10.202.50:5060>
Content-Type: application/sdp
Cisco-Gcid: BF1F1B8C-013F-1000-4000-001125CUCE68
Call-Info: <sip:10.10.202.50:5060>;method="NOTIFY;Event=telephone-event;Duration=2000"
Allow-Events: telephone-event
 
v=0
o=CiscoSystemsSIP-Workflow-App-UserAgent 2956 2956 IN IP4 10.10.202.50
s=SIP Call
c=IN IP4 10.10.202.50
t=0 0
m=audio 16926 RTP/AVP 0
a=rtpmap:0 pcmu/8000
a=ptime:20
 
2882 07/08 10:36:30.909 VMSS dbug 1 com.cisco.aesop.voicemail.Mailbox : refreshMWI: 3001
2882 07/08 10:36:30.909 VMSS dbug 1 com.cisco.aesop.voicemail.LdapAgent : getUserByPhoneNo: 3001
2882 07/08 10:36:30.918 VMSS dbug 1 com.cisco.aesop.voicemail.LdapAgent : getUserByPhoneNo: id  MWIOne
2882 07/08 10:36:30.918 VMSS dbug 1 com.cisco.aesop.voicemail.VMDatabase : connection 0: query: select mailboxid from vm_mbxusers where owner=true and userdn='/sw/local/users/MWIOne';
2882 07/08 10:36:30.919 VMSS dbug 1 com.cisco.aesop.voicemail.VMUser : getMailboxInfo: personalMailboxId=PERSONAL_00000000000000000000000
2882 07/08 10:36:30.920 VMSS dbug 1 com.cisco.aesop.voicemail.VMDatabase : connection 1: query: select messageid from vm_message where messagetype=50 and starttime<=1373301390920 and endtime>=1373301390920 and private='false' except select vm_bcst_heard.messageid from vm_message, vm_bcst_heard where vm_message.messageid=vm_bcst_heard.messageid  and vm_bcst_heard.mailboxid='PERSONAL_00000000000000000000000';
2882 07/08 10:36:30.922 VMSS dbug 1 com.cisco.aesop.voicemail.LdapAgent : getAttributeValue: /sw/local/users/MWIOne/TelephoneNumbers/primaryExtension
2882 07/08 10:36:30.923 VMSS dbug 1 com.cisco.aesop.voicemail.Mailbox : setMessageWaiting: 3001,true 2882 07/08 10:36:30.923 VMSS dbug 1 MessageWaitingThread : adding job
3400 07/08 10:36:30.923 VMSS dbug 1 com.cisco.aesop.voicemail.MessageWaitingThread : http://localhost:8080/mwiapp?extn=3001&state=1
4481 07/08 10:36:30.935 ACCN STGN 0 Task: 265000000011 GetListMember: output string:outcall 4481 07/08 10:36:30.937 ACCN SIPL 0 sip-ltp10: 3, State=CONTACTINGenter connect
4481 07/08 10:36:30.937 ACCN SIPL 0 sip-ltp10: 3, State=CONTACTINGenter createInvitation
4481 07/08 10:36:30.937 ACCN SIPL 0 SDPBody : v=0
o=CiscoSystemsSIP-Workflow-App-UserAgent 3673 3673 IN IP4 10.10.202.50
s=SIP Call
c=IN IP4 10.10.202.50
t=0 0
m=audio 16924 RTP/AVP 0
a=rtpmap:0 pcmu/8000
a=ptime:20
 
4481 07/08 10:36:30.937 ACCN SIPL 0 sip-ltp10: 3, State=CONTACTINGbefore invitationmanager.createInvitation. body : v=0
o=CiscoSystemsSIP-Workflow-App-UserAgent 3673 3673 IN IP4 10.10.202.50
s=SIP Call
c=IN IP4 10.10.202.50
t=0 0
m=audio 16924 RTP/AVP 0
a=rtpmap:0 pcmu/8000
a=ptime:20
body type : application/sdp toNA : <sip:39993001@10.10.202.1:5060;user=phone> fromNA : <sip:3@10.10.202.50:5060> from tag : cue9d5cfebc
4481 07/08 10:36:30.937 ACCN SIPL 0 sip-ltp10: 3, State=CONTACTINGafter invitationmanager.createInvitation
4481 07/08 10:36:30.937 ACCN SIPL 0 sip-ltp10: 3, State=CONTACTING added ciscogcid
4481 07/08 10:36:30.937 ACCN SIPL 0 sip-ltp10: 3, State=CONTACTING getDTMFHeader: Enter
4481 07/08 10:36:30.937 ACCN SIPL 0 sip-ltp10: 3, State=CONTACTING getDTMFHeader: getting the headers
4481 07/08 10:36:30.937 ACCN SIPL 0 sip-ltp10: 3, State=CONTACTING getDTMFHeader: before adding headers to message
4481 07/08 10:36:30.938 ACCN SIPL 0 sip-ltp10: 3, State=CONTACTING getDTMFHeader: after adding headers to message : INVITE sip:39993001@10.10.202.1:5060;user=phone SIP/2.0 Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bK51VhKqo+pUDrDt5LgLS2yA~~6
Max-Forwards: 70
To: <sip:39993001@10.10.202.1:5060;user=phone>
From: <sip:3@10.10.202.50:5060>;tag=cue9d5cfebc
Call-ID: 137330139093613@10.10.202.50
CSeq: 1 INVITE
Content-Length: 178
Contact: <sip:3@10.10.202.50:5060>
Content-Type: application/sdp
Cisco-Gcid: BF243E58-013F-1000-4000-001125CUCE68
Call-Info: <sip:10.10.202.50:5060>;method="NOTIFY;Event=telephone-event;Duration=2000"
Allow-Events: telephone-event
 
v=0
o=CiscoSystemsSIP-Workflow-App-UserAgent 3673 3673 IN IP4 10.10.202.50
s=SIP Call
c=IN IP4 10.10.202.50
t=0 0
m=audio 16924 RTP/AVP 0
a=rtpmap:0 pcmu/8000
a=ptime:20
 
4481 07/08 10:36:30.938 ACCN SIPL 0 sip-ltp10: 3, State=CONTACTING invite message : INVITE sip:39993001@10.10.202.1:5060;user=phone SIP/2.0 Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bK51VhKqo+pUDrDt5LgLS2yA~~6
Max-Forwards: 70
To: <sip:39993001@10.10.202.1:5060;user=phone>
From: <sip:3@10.10.202.50:5060>;tag=cue9d5cfebc
Call-ID: 137330139093613@10.10.202.50
CSeq: 1 INVITE
Content-Length: 178
Contact: <sip:3@10.10.202.50:5060>
Content-Type: application/sdp
Cisco-Gcid: BF243E58-013F-1000-4000-001125CUCE68
Call-Info: <sip:10.10.202.50:5060>;method="NOTIFY;Event=telephone-event;Duration=2000"
Allow-Events: telephone-event
 
v=0
o=CiscoSystemsSIP-Workflow-App-UserAgent 3673 3673 IN IP4 10.10.202.50
s=SIP Call
c=IN IP4 10.10.202.50
t=0 0
m=audio 16924 RTP/AVP 0
a=rtpmap:0 pcmu/8000
a=ptime:20
 
4481 07/08 10:36:30.938 ACCN SIPL 0 sip-ltp10: 3, State=CONTACTINGreturning invitation
4481 07/08 10:36:30.938 ACCN SIPL 0 sip-ltp10: 3, State=CONTACTINGgot Invitation
4481 07/08 10:36:30.938 ACCN SIPL 0 sip-ltp10: 3, State=CONTACTINGbefore Invitation start
4481 07/08 10:36:30.939 ACCN SIPL 0 sip-ltp10: 3, State=CONTACTINGafter Invitation start 4481 07/08 10:36:35.938 ACCN SIPL 0 sip-ltp10: 3, State=CONTACTING terminating dialog in contacting state 20 4481 07/08 10:36:35.939 ACCN SIPL 0 sip-ltp10: 3, State=TERMINATEDcontacting state hangup
4481 07/08 10:36:35.939 ACCN SIPL 0 sip-ltp10: 3, State=TERMINATEDAfter contacting state hangup
```

##### Solution:

The bind interface command allows you to configure the source IP address of signaling and media packets to a specific interface's IP address. Thus, the address that goes out on the packet is bound to the IP address of the interface specified with the bind command. Packets that are not destined to the bound address are discarded.

- Check the interface used to configure CUE.

- It is recommended that the interface used in CUCME inside the ip source-address is the same used for CUE.

- Make proper adjustments in order to accept SIP Traffic sourced from CUE interface:

3.1 You can remove the bind commands from voice service voip . This allows the Gateway to accept SIP Traffic from any interface.

```
voice service voip
 sip no bind control source-interface [interface]
  no bind media source-interface [interface]
```

3.2 You can configure SIP bind commands on a dial-peer basis. This is commonly used when you have a SIP Trunk to your Carrier or Firewalls that requires specific IP Addresses to allow:

```
dial-peer voice tag voip 
 session protocol sipv2 voice-class sip bind {control | media} source interface interface-id[ipv6-address ipv6-address] exit
```

#### Issue 2. Proper Extension length not defined in ephone-dn

MWI DN configuration in CUCME for the Outcall Method is not properly provisioned with the correct extension length used in the CUCME Dial Plan for MWI.

Possible Cause #1

If ephoned-dn is configured with only the MWI extension and no dots ('.') CUE synchronization fails :

Navigate to Administration > Synchronize Information

Possible Cause #2

Extension Length does not match the right amount of digits for the users extensions.

In CUCME you can use the debug ccsip messages and the messages are present, but the MWI does not work:

```
Received: INVITE sip:39993001@10.10.202.1:5060;user=phone SIP/2.0 Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bK51VhKqo+pUDrDt5LgLS2yA~~20
Max-Forwards: 70
To: <sip:39993001@10.10.202.1:5060;user=phone>
From: <sip:3@10.10.202.50:5060>;tag=cue5d4ca12d
Call-ID: 137330470927141@10.10.202.50
CSeq: 1 INVITE
Content-Length: 176
Contact: <sip:3@10.10.202.50:5060>
Content-Type: application/sdp
Cisco-Gcid: BF56E097-013F-1000-4000-001125CUCE68
Call-Info: <sip:10.10.202.50:5060>;method="NOTIFY;Event=telephone-event;Duration=2000"
Allow-Events: telephone-event
 
v=0
o=CiscoSystemsSIP-Workflow-App-UserAgent 151 151 IN IP4 10.10.202.50
s=SIP Call
c=IN IP4 10.10.202.50
t=0 0
m=audio 16932 RTP/AVP 0
a=rtpmap:0 pcmu/8000
a=ptime:20
 
000815: *Jul  8 18:26:07.215: SetCallInfo MODE 1 calling dn -1 chan 1 dn 3 chan 1 000816: *Jul  8 18:26:07.215: alling [3] called [39993001]
000817: *Jul  8 18:26:07.215: SkinnyTryCall to 1 instance 1 start at 0
000818: *Jul  8 18:26:07.215: MWI-on non-local target 1
000819: *Jul  8 18:26:07.215: MWI-on has no non-local target 1 CME#show ephone reg ephone-1[0] Mac:0023.5E18.23EC TCP socket:[2] activeLine:0 whisperLine:0 REGISTERED in SCCP ver 17/12 max_streams=5
mediaActive:0 whisper_mediaActive:0 startMedia:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:1 caps:9
IP:10.10.202.2 31984 7965  keepalive 4 max_line 6 available_line 6
button 1: dn 1  number 3001 CH1   IDLE         CH2   IDLE
Preferred Codec: g711ulaw
Username: MWIOne Password: cisco
```

##### Solution:

Ensure the proper amount of dots ('.') are configured after the MWI extension number in order to match the length of the extensions used in CUCME for the users:

```
ephone-dn 3
 mwi on
 number 3999 … .
!
ephone-dn 4
 mwi off
 number 3998 … .
```

#### Issue 3. Subscribe-Notify with no Subscription

When SIP Subscribe-Notify method is used and no prior Subscription of the Directory Numbers has taken place, MWI does not work and no SIP Notify is sent for MWI events.

In CUCME after leaving or retrieving voicemails, no SIP Notify is sent from CUE in order to turn on/off MWI:

```
Sent:
BYE sip:3600@10.10.202.50:5060 SIP/2.0
Via: SIP/2.0/UDP 10.10.202.1:5060;branch=z9hG4bK601067
From: <sip:3001@10.10.202.1>;tag=716F18-152D
To: <sip:3600@10.10.202.50>;tag=cue861dc350
Date: Mon, 08 Jul 2013 18:35:00 GMT
Call-ID: EE5026C6-E73311E2-80DE96BA-2150599@10.10.202.1
User-Agent: Cisco-SIPGateway/IOS-12.x
Max-Forwards: 70
Timestamp: 1373308519
CSeq: 102 BYE
Reason: Q.850;cause=16
Content-Length: 0
 
 
Received:
SIP/2.0 200 Ok
Via: SIP/2.0/UDP 10.10.202.1:5060;branch=z9hG4bK601067
To: <sip:3600@10.10.202.50>;tag=cue861dc350
From: <sip:3001@10.10.202.1>;tag=716F18-152D
Call-ID: EE5026C6-E73311E2-80DE96BA-2150599@10.10.202.1
CSeq: 102 BYE
Content-Length: 0
```

##### Solution:

Configure the proper MWI Subscription commands in order to get the DNs Subscribe with CUE for MWI events:

```
voice register dn 1
 number 3005 mwi !
ephone-dn  1 
 number 3001 mwi sip Sent:
SUBSCRIBE sip:3001@10.10.202.50:5060 SIP/2.0
Via: SIP/2.0/UDP 10.10.202.1:5060;branch=z9hG4bK61210
From: <sip:3001@10.10.202.1>;tag=728524-1B54
To: <sip:3001@10.10.202.50>
Call-ID: 18BDF708-E73411E2-80DF96BA-2150599@10.10.202.1
CSeq: 101 SUBSCRIBE
Max-Forwards: 70
Date: Mon, 08 Jul 2013 18:36:11 GMT
User-Agent: Cisco-SIPGateway/IOS-12.x
Event: message-summary
Expires: 3600
Contact: <sip:3001@10.10.202.1:5060>
Accept: application/simple-message-summary
Content-Length: 0
 
Received:
SIP/2.0 202 Accepted
Via: SIP/2.0/UDP 10.10.202.1:5060;branch=z9hG4bK61210
To: <sip:3001@10.10.202.50>;tag=591a1296-1099
From: <sip:3001@10.10.202.1>;tag=728524-1B54
Call-ID: 18BDF708-E73411E2-80DF96BA-2150599@10.10.202.1
CSeq: 101 SUBSCRIBE
Content-Length: 0
Expires: 3600
Contact: sip:3001@10.10.202.50
Allow-Events: refer
Allow-Events: telephone-event
Allow-Events: message-summary
 
Received:
NOTIFY sip:3001@10.10.202.1:5060 SIP/2.0
Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bK51VhKqo+pUDrDt5LgLS2yA~~27
Max-Forwards: 70
To: <sip:3001@10.10.202.1>;tag=728524-1B54
From: <sip:3001@10.10.202.50>;tag=591a1296-1099
Call-ID: 18BDF708-E73411E2-80DF96BA-2150599@10.10.202.1
CSeq: 1 NOTIFY
Content-Length: 113
Contact: sip:3001@10.10.202.50
Event: message-summary
Allow-Events: refer
Allow-Events: telephone-event
Allow-Events: message-summary
Subscription-State: active
Content-Type: application/simple-message-summary
 
Messages-Waiting: yes
Message-Account: sip:3001@10.10.202.50
Voice-Message: 1/0 (0/0)
Fax-Message: 0/0 (0/0)
 
Sent:
SIP/2.0 200 OK
Via: SIP/2.0/UDP 10.10.202.50:5060;branch=z9hG4bK51VhKqo+pUDrDt5LgLS2yA~~27
From: <sip:3001@10.10.202.50>;tag=591a1296-1099
To: <sip:3001@10.10.202.1>;tag=728524-1B54
Date: Mon, 08 Jul 2013 18:36:11 GMT
Call-ID: 18BDF708-E73411E2-80DF96BA-2150599@10.10.202.1
CSeq: 1 NOTIFY
Content-Length: 0
 
000963: *Jul  8 18:36:12.255: %SYS-5-CONFIG_I: Configured from console by jovalver on vty0 (10.10.100.6)
000964: *Jul  8 18:36:12.599: ephone-1[2]:Set MWI line 1 to ON count 1
000965: *Jul  8 18:36:12.599: ephone-1[2]:Set MWI line 0 to ON count 1
```

#### Issue 4. 488 Not Acceptable Media

CUCME sends 488 Not Acceptable Media when CUE sends an Outcall INVITE for MWI.

```
Sent: SIP/2.0 488 Not Acceptable Media Via: SIP/2.0/UDP 172.18.106.88:5060
From: "Cisco SIP Channel1" <sip:outbound-0@172.18.106.66>;tag=75b5194d-133
To: <sip:1109811043@172.18.106.66;user=phone>;tag=23F1578C-252
Date: Fri, 11 Mar 2005 15:09:13 GMT
Call-ID: e34bafcc-131@172.18.106.88:5060
Server: Cisco-SIPGateway/IOS-12.x
CSeq: 51 INVITE
Allow-Events: telephone-event
Content-Length: 0
```

##### Solution:

CUE only supports G711ulaw

Ensure the proper incoming dial-peer is match that supports codec G711ulaw. You can either create a new dial-peer or use the pre-existing dial-peer for voicemail access:

```
dial-peer voice 3600 voip 
destination-pattern 3600 
session protocol sipv2 
session target ipv4:10.10.202.2 incoming called-number 399[89].... dtmf-relay sip-notify codec g711ulaw no vad 
!
```

## Related Information

### Revision History

1.0

23-May-2017

Initial Release

### Contributed by Cisco Engineers

Jose Valverde

Cisco TAC Engineer

Michael Mendoza

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager Express

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 23-May-2017 | Initial Release |