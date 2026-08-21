---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-200788-call-recordi-76e7861bad
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200788-Call-Recording-Basic-Configuration-and-T.html
retrieved_at: 2026-08-21T13:57:56.778336+00:00
---

Configure and Troubleshoot Basic Call Recording

# Configure and Troubleshoot Basic Call Recording

### Download Options

Updated: August 20, 2026

Document ID: 200788

Contents

## Contents

## Introduction

This document describes the basics of call recording within Cisco Unified Communications Manager (CUCM).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of CUCM integrated with a third-party recording server.

### Components Used

The information in this document is based on these software and hardware versions:

- CUCM

- Cisco Internet Protocol (IP)

- Phone Call Recording Server

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

This document also discusses the expected media flow, the expected call flows for Session Initiation Protocol (SIP) and Skinny Client Control Protocol (SCCP) devices, and an example of a common type of call recording setup failure.

## Types of Call Recording

### Automatic

The key elements of automatic call recording are as follows:

- Uses Built-In-Bridge (BIB) of IP phone in order to fork audio to the recording destination.

- Initiated every time the IP phone places a call or receives a call.

- Requires only a SIP trunk between CUCM and recording destination. Some recording vendors require Computer Telephony Integration (CTI).

- Does not allow recording of phones that are located outside of the managed network (must have access to send RTP directly to recording server and be a Cisco IP phone capable of allocating a BIB).

In this diagram, the solid lines represent the expected media flow and the dashed lines represent the expected signaling flow:

### Application Invoked

The key elements of application invoked call recording are as follows:

- Uses BIB of IP phone in order to fork audio to the recording destination.

- Initiated when the application (recorder) dictates that it must be initiated.

- Requires SIP trunk and CTI with recording application.

- CTI application user must have access to endpoints that need to be recorded.

- Does not allow recording of phones that are located outside of the managed network (must have access to send RTP directly to recording server).

In the diagram here, the solid lines represent the expected media flow and the dashed lines represent the expected signaling flow. The solid line between CUCM and the recording server denotes a CTI connection between CUCM and the application.

### Selective

The key elements of selective call recording are as follows:

- Uses BIB of IP phone in order to fork audio to the recording destination.

- Initiated every time the IP phone user selects the recording option on their IP phone (CUCM 9.x+) or on an application like in this image

- Typically requires only a SIP trunk between CUCM and recording destination (which depends on recording application vendor).

- Does not allow recording of phones that lie outside of the managed network (must have access to send RTP directly to recording server).

As you can see in this diagram here, the media and signaling path is very similar to automatic call recording:

### Gateway-Based

The key elements of gateway-based call recording are as follows:

- Voice gateway forks the media towards the recording destination.

- CUCM registers with gateway as an application.

- CUCM uses HTTP in order to instruct Gateway (GW) to stream media to recording destination.

- CUCM integrates with recording destination via SIP trunk.

- Allows recording of calls that simply pass through managed network (for instance, to mobile users) or for phones that do not support the BIB.

As you can see from the diagram here, the media flow is quite different from the other types of call recording:

## Automatic Call Recording Configuration for SIP only Integration

This section describes how to setup the SIP integration of a recording server.

### Create SIP Trunk to Recording Destination

- Navigate to Device > Trunk , select Add New .

- Create a SIP trunk with the settings as shown in the image.

- Input the appropriate Device Name , Device Pool , MRGL , SIP trunk security profile , and SIP profile .

- The destination address configured is the address of the recording application server.

### Create Recording Profile

- Navigate to Device > Device Settings > Recording Profile .

- Recording destination address is where the recording calls are sent as shown in the image.

### Create Route Pattern to Route Recording Calls

- Create a route pattern that matches the recording destination address configured in the previous Step.

- You can point to a route list instead of directly at the SIP trunk, if you wish to configure redundant SIP trunks.

Note : The partition assigned to this Route Pattern must be associated with the RecordingCallingSearch Space and as shown in the image.

### Assign Recording Profile to Phone Line

- On an already created phone with an existing extension, assign the recording profile created.

- Assign the type of call recording in this location as well.

- The example shows automatic recording, as shown in the image.

### Set BIB to On and Privacy to Off on Phone Configuration Page

While on the device configuration page, navigate to the section titled Device Information . Set Built In Bridge to On and Privacy to Off as shown in the image.

## Verify

Use this section in order to confirm that your configuration works properly.

Here are the expected behaviors in the Call Manager traces for SCCP and SIP phones with the given configuration. These examples are for a phone that calls another phone on the same cluster while one of the phones is set up for call recording.

Note : The logs to collect from CUCM are CTIManger, CallManager, Event Viewer App/Sys, and pcaps can be needed in some scenarios.

Note : The logs to collect from phones are console logs and pcaps. You can get pcaps from the recording server at the same time as you get the pcaps from the phone.

### SCCP

```
~~~~~~~~~~~~~~~~~~~~~~
Normal CCM Traces for SCCP phone to SCCP phone with SIP Integrated Call Recording
~~~~~~~~~~~~~~~~~~~~~~

### Calling phone places call

03796977.001 |20:21:08.055 |AppInfo  |StationInit: (0000109) SoftKeyEvent softKeyEvent=1(Redial) lineInstance=0 callReference=0.
```

```
### CUCM performs digit analysis against the dialed digits (dd="9110001")

03797017.001 |20:21:08.057 |AppInfo  |Digit Analysis: star_DaReq: daReq.partitionSearchSpace(), filteredPartitionSearchSpaceString(), partitionSearchSpaceString()
03797017.002 |20:21:08.057 |AppInfo  |Digit Analysis: star_DaReq: Matching Legacy Numeric, digits=9110001
03797017.003 |20:21:08.057 |AppInfo  |Digit Analysis: getDaRes data&colon; daRes.ssType=[0] Intercept DAMR.sstype=[0], TPcount=[0], DAMR.NotifyCount=[0], DaRes.NotifyCount=[0]
03797017.004 |20:21:08.057 |AppInfo  |Digit Analysis: getDaRes - Remote Destination [] isURI[1]
03797017.005 |20:21:08.057 |AppInfo  |Digit analysis: patternUsage=2
03797017.006 |20:21:08.057 |AppInfo  |Digit analysis: match(pi="2", fqcn="9110006", cn="9110006",plv="5", pss="", TodFilteredPss="", dd="9110001",dac="0")
03797017.007 |20:21:08.057 |AppInfo  |Digit analysis: analysis results
03797017.008 |20:21:08.057 |AppInfo  ||PretransformCallingPartyNumber=9110006
|CallingPartyNumber=9110006
|DialingPartition=
|DialingPattern=9110001
|FullyQualifiedCalledPartyNumber=9110001
|DialingPatternRegularExpression=(9110001)
|DialingWhere=
|PatternType=Enterprise
|PotentialMatches=NoPotentialMatchesExist
|DialingSdlProcessId=(0,0,0)
|PretransformDigitString=9110001
|PretransformTagsList=SUBSCRIBER
|PretransformPositionalMatchList=9110001
|CollectedDigits=9110001
```

```
### CUCM determines call must stay on same node; go to LineControl (PID=LineControl(2,100,174,137))

03797019.001 |20:21:08.058 |AppInfo  |Digit analysis: wait_DmPidRes- Partition=[] Pattern=[9110001] Where=[],cmDeviceType=[UserDevice], OutsideDialtone =[0], DeviceOverride=[0], PID=LineControl(2,100,174,137),CI=[38960749],Sender=Cdcc(2,100,219,29)
```

```
### CUCM extends call to phone

03797036.003 |20:21:08.058 |AppInfo  |StationD:    (0000114) DEBUG whatToDo: line=1 calls=0 limit=4, busy=2. GCI=(2, 5033), cm_PL=(5, 0).
03797036.004 |20:21:08.058 |AppInfo  |StationD:    (0000114) DEBUG  whatToDo: busy trigger not hit... send to open appearance
03797036.005 |20:21:08.058 |AppInfo  |preFilterCapCount =[11], preFilterCaps :: (Cap)= (25) (6) (4) (2) (7) (8) (15) (16) (11) (12) (257) Filtering Caps due to Service Parameter Configuration postFilterCapCount =[8], postFilterCaps :: (Cap)= (25) (4) (2) (15) (16) (11) (12) (257)
03797036.006 |20:21:08.058 |AppInfo  |preFilterCapCount =[0], preFilterCaps :: (Cap)= Filtering Caps due to Service Parameter Configuration postFilterCapCount =[0], postFilterCaps :: (Cap)=
03797036.007 |20:21:08.058 |Created  |                                       |                               |StationCdpc(2,100,64,22)         |StationD(2,100,63,114)           |                                         |NumOfCurrentInstances: 2
03797036.008 |20:21:08.058 |AppInfo  |StationD:    (0000114) DEBUG- getLineRingSetting: retVal=4.
03797036.009 |20:21:08.058 |AppInfo  |StationD:    (0000114) DEBUG- saveRinger for: ci=38960750, line=1, mode=2, cm_precedence=5, callPhase=5.
03797036.010 |20:21:08.058 |AppInfo  |StationD:    (0000114) DEBUG- saveRinger: ci=38960750, line=1, mode=2, cm_precedence=5, callPhase=5, modifier=0
03797036.011 |20:21:08.058 |AppInfo  |StationD:    (0000114) INFO  sendCallAcceptReq: Try to send StationLineCallAccept to cdpc=22 .
03797036.012 |20:21:08.058 |AppInfo  |StationD:    (0000114) playRinger for: ci=38960750.
03797036.013 |20:21:08.058 |AppInfo  |StationD:    (0000114) DEBUG- getLineRingSetting: retVal=4.
03797036.014 |20:21:08.058 |AppInfo  |StationD:    (0000114) DEBUG- getLineRingSetting: retVal=4.
03797036.015 |20:21:08.058 |AppInfo  |StationD:    (0000114) DEBUG- getLineRingSetting: retVal=4.
```

```
### Called (recorded) phone goes off hook

03797089.001 |20:21:09.335 |AppInfo  |StationD:    (0000114) restart0_StationOffHook - INFO: CI=38960750 on line=1, SPKMode=0, alwaysPrimeLine=0, alwaysUsePrimeLineForVM=0, fid=0, offHookTrigger=0.
```

```
### CUCM Tells the calling phone to open the logical channel

03797153.001 |20:21:09.337 |AppInfo  |StationD:    (0000109) SEP0018195AA209 , star_MediaExchangeAgenaOpenLogicalChannel packetSize=20, codec=4, ci=38960749
```

```
### CUCM Tells the called (recorded party) phone to open the logical channel

03797156.001 |20:21:09.337 |AppInfo  |StationD:    (0000114) SEP001795BDD16B , star_MediaExchangeAgenaOpenLogicalChannel packetSize=20, codec=4, ci=38960750
```

```
### CUCM Tells the calling phone to open the receive channel

03797164.002 |20:21:09.337 |AppInfo  |StationD:    (0000109) OpenReceiveChannel conferenceID=38960749 passThruPartyID=33554450 millisecondPacketSize=20 compressionType=4(Media_Payload_G711Ulaw64k) RFC2833PayloadType=0 qualifierIn=? sourceIpAddr=IpAddr.type:0 ipAddr:0x0e302021000000000000000000000000(10.48.32.33). myIP: IpAddr.type:0 ipv4Addr:0x0e30201c(10.48.32.28)
```

```
### CUCM Tells the called (recorded party) phone to open the receive channel

03797168.002 |20:21:09.337 |AppInfo  |StationD:    (0000114) OpenReceiveChannel conferenceID=38960750 passThruPartyID=33554451 millisecondPacketSize=20 compressionType=4(Media_Payload_G711Ulaw64k) RFC2833PayloadType=0 qualifierIn=? sourceIpAddr=IpAddr.type:0 ipAddr:0x0e30201c000000000000000000000000(10.48.32.28). myIP: IpAddr.type:0 ipv4Addr:0x0e302021(10.48.32.33)
```

```
### CUCM allocates BIB on called (recorded) phone

03797210.000 |20:21:09.338 |SdlSig   |MrmAllocateUcbResourceReq              |waiting                        |MediaResourceManager(2,100,138,1) |Cc(2,100,220,1)                  |2,100,14,8384.91^10.48.32.33^SEP001795BDD16B |[R:N-H:0,N:1,L:0,V:0,Z:0,D:0]  CI=38960751 SsType=33554461 SsKey=9 BridgeType=0 MRGLPkid= NumStream=1 Bib=89cdb152-4ef2-4d60-9e6b-ab8c77c22618 BibTgCi=38960750 FeatId=159 PL=5 PLDmn=0 DeviceCapability=0 NumVideoCapable=0 requestDeviceType=0 requestDeviceLocale=64 forkingDevicePosition=2 playToneDir=3
```

```
### BiB places first call to recording destination address (cn is calling party which is the BiB cn="b00223908001" and it is dialing the recordingdestination dd="8675309")

03797269.001 |20:21:09.340 |AppInfo  |Digit Analysis: star_DaReq: daReq.partitionSearchSpace(), filteredPartitionSearchSpaceString(), partitionSearchSpaceString()
03797269.002 |20:21:09.340 |AppInfo  |Digit Analysis: star_DaReq: Matching Legacy Numeric, digits=8675309
03797269.003 |20:21:09.340 |AppInfo  |Digit Analysis: getDaRes data: daRes.ssType=[0] Intercept DAMR.sstype=[0], TPcount=[0], DAMR.NotifyCount=[0], DaRes.NotifyCount=[0]
03797269.004 |20:21:09.340 |AppInfo  |Digit Analysis: getDaRes - Remote Destination [8675309] isURI[0]
03797269.005 |20:21:09.340 |AppInfo  |CMUtility routeCallThroughCTIRD: no matching RemDestDynamic record exists for remdest [8675309]
03797269.006 |20:21:09.340 |AppInfo  |DbMobility: getMatchedRemDest starts: cnumber = 8675309
03797269.007 |20:21:09.340 |AppInfo  |DbMobility: getMatchedRemDest: full match case
03797269.008 |20:21:09.340 |AppInfo  |DbMobility SelectByDestination: no matching RemDestDynamic record exists for remdest [8675309]
03797269.009 |20:21:09.340 |AppInfo  |DbMobility: can't find remdest 8675309 in map
03797269.010 |20:21:09.340 |AppInfo  |Digit analysis: patternUsage=5
03797269.011 |20:21:09.340 |AppInfo  |Digit analysis: match(pi="1", fqcn="", cn="b00223908001",plv="5", pss="E911_PT:Phones_PT:EMERGENCY_PT:INTERNAL_PT:INFORMACAST_PT", TodFilteredPss="E911_PT:Phones_PT:EMERGENCY_PT:INTERNAL_PT:INFORMACAST_PT", dd="8675309",dac="0")
03797269.012 |20:21:09.340 |AppInfo  |Digit analysis: analysis results
03797269.013 |20:21:09.340 |AppInfo  ||PretransformCallingPartyNumber=b00223908001
|CallingPartyNumber=b00223908001
|DialingPartition=
|DialingPattern=8675309
|FullyQualifiedCalledPartyNumber=8675309
|DialingPatternRegularExpression=(8675309)
|DialingWhere=
|PatternType=Enterprise
|PotentialMatches=NoPotentialMatchesExist
|DialingSdlProcessId=(0,0,0)
|PretransformDigitString=8675309
|PretransformTagsList=SUBSCRIBER
|PretransformPositionalMatchList=8675309
|CollectedDigits=8675309
```

```
### CUCM sends INVITE #1 to configured recording server (10.48.32.170)

03797320.001 |20:21:09.343 |AppInfo  |//SIP/SIPUdp/wait_SdlSPISignal: Outgoing SIP UDP message to 10.48.32.170:[5060]:
[212231,NET]
INVITE sip:8675309@10.48.32.170:5060 SIP/2.0
Via: SIP/2.0/UDP 10.48.32.90:5060;branch=z9hG4bK204d520fedb3
From: <sip:9110001@10.48.32.90;x-nearend;x-refci=38960750;x-nearendclusterid=glenscucm10-5;x-nearenddevice=sep001795bdd16b;x-nearendaddr=9110001;x-farendrefci=38960749;x-farendclusterid=glenscucm10-5;x-farenddevice=sep0018195aa209;x-farendaddr=9110006>;tag=73601~713e2333-4032-45f1-b1f5-e33cf471acec-38960754
To: <sip:8675309@10.48.32.170>
Date: Tue, 30 Sep 2014 00:21:09 GMT
Call-ID: abbb8e00-4291f775-204c-5a20300e@10.48.32.90
Supported: timer,resource-priority,replaces
Min-SE:  1800
User-Agent: Cisco-CUCM10.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence, kpml
Supported: X-cisco-srtp-fallback
Supported: Geolocation
Call-Info: ;method="NOTIFY;Event=telephone-event;Duration=500"
Cisco-Guid: 2881195520-0000065536-0000000011-1512058894
Session-Expires:  1800
P-Asserted-Identity: <sip:9110001@10.48.32.90>
Remote-Party-ID: <sip:9110001@10.48.32.90>;party=calling;screen=yes;privacy=off
Contact: <sip:9110001@10.48.32.90:5060>;isFocus
Max-Forwards: 70
Content-Length: 0
```

```
### BiB places second call to recording destination address (cn is calling party which is the BiB cn="b00223908001" and it is dialing the recordingdestination dd="8675309")
Note that the BiB number stayed the same (b00223908001) and so did the recordingdestination number

03797367.010 |20:21:09.344 |AppInfo  |Digit analysis: patternUsage=5
03797367.011 |20:21:09.344 |AppInfo  |Digit analysis: match(pi="1", fqcn="", cn="b00223908001",plv="5", pss="E911_PT:Phones_PT:EMERGENCY_PT:INTERNAL_PT:INFORMACAST_PT", TodFilteredPss="E911_PT:Phones_PT:EMERGENCY_PT:INTERNAL_PT:INFORMACAST_PT", dd="8675309",dac="0")
03797367.012 |20:21:09.344 |AppInfo  |Digit analysis: analysis results
03797367.013 |20:21:09.344 |AppInfo  ||PretransformCallingPartyNumber=b00223908001
|CallingPartyNumber=b00223908001
|DialingPartition=
|DialingPattern=8675309
|FullyQualifiedCalledPartyNumber=8675309
|DialingPatternRegularExpression=(8675309)
|DialingWhere=
|PatternType=Enterprise
|PotentialMatches=NoPotentialMatchesExist
|DialingSdlProcessId=(0,0,0)
|PretransformDigitString=8675309
|PretransformTagsList=SUBSCRIBER
|PretransformPositionalMatchList=8675309
|CollectedDigits=8675309
```

```
### CUCM receives 200 OK in response to INVITE #1

03797390.001 |20:21:09.345 |AppInfo  |//SIP/SIPUdp/wait_SdlDataInd: Incoming SIP UDP message size 737 from 10.48.32.170:[5060]:
[212232,NET]
SIP/2.0 200 OK
Via: SIP/2.0/UDP 10.48.32.90:5060;branch=z9hG4bK204d520fedb3
From: <sip:9110001@10.48.32.90;x-nearend;x-refci=38960750;x-nearendclusterid=glenscucm10-5;x-nearenddevice=sep001795bdd16b;x-nearendaddr=9110001;x-farendrefci=38960749;x-farendclusterid=glenscucm10-5;x-farenddevice=sep0018195aa209;x-farendaddr=9110006>;tag=73601~713e2333-4032-45f1-b1f5-e33cf471acec-38960754
To: <sip:8675309@10.48.32.170>;tag=1
Call-ID: abbb8e00-4291f775-204c-5a20300e@10.48.32.90
CSeq: 101 INVITE
Contact: <sip:10.48.32.170:5060;transport=udp>
Content-Type: application/sdp
Content-Length:   135

v=0
o=user1 53655765 2353687637 IN IP4 10.48.32.170
s=-
c=IN IP4 10.48.32.170
t=0 0
m=audio 6000 RTP/AVP 0
a=rtpmap:0 PCMU/8000
```

```
### CUCM sends INVITE #2 to recording server (10.48.32.170)

03797445.001 |20:21:09.348 |AppInfo  |//SIP/SIPUdp/wait_SdlSPISignal: Outgoing SIP UDP message to 10.48.32.170:[5060]:
[212233,NET]
INVITE sip:8675309@10.48.32.170:5060 SIP/2.0
Via: SIP/2.0/UDP 10.48.32.90:5060;branch=z9hG4bK204e754eaeae
From: <sip:9110001@10.48.32.90;x-farend;x-refci=38960750;x-nearendclusterid=glenscucm10-5;x-nearenddevice=sep001795bdd16b;x-nearendaddr=9110001;x-farendrefci=38960749;x-farendclusterid=glenscucm10-5;x-farenddevice=sep0018195aa209;x-farendaddr=9110006>;tag=73602~713e2333-4032-45f1-b1f5-e33cf471acec-38960757
To: <sip:8675309@10.48.32.170>
Date: Tue, 30 Sep 2014 00:21:09 GMT
Call-ID: abbb8e00-4291f775-204d-5a20300e@10.48.32.90
Supported: timer,resource-priority,replaces
Min-SE:  1800
User-Agent: Cisco-CUCM10.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence, kpml
Supported: X-cisco-srtp-fallback
Supported: Geolocation
Call-Info: ;method="NOTIFY;Event=telephone-event;Duration=500"
Cisco-Guid: 2881195520-0000065536-0000000012-1512058894
Session-Expires:  1800
P-Asserted-Identity: <sip:9110001@10.48.32.90>
Remote-Party-ID: <sip:9110001@10.48.32.90>;party=calling;screen=yes;privacy=off
Contact: <sip:9110001@10.48.32.90:5060>;isFocus
Max-Forwards: 70
Content-Length: 0
```

```
### CUCM receives 200 OK in response to INVITE #2

03797498.001 |20:21:09.350 |AppInfo  |//SIP/SIPUdp/wait_SdlDataInd: Incoming SIP UDP message size 736 from 10.48.32.170:[5060]:
[212235,NET]
SIP/2.0 200 OK
Via: SIP/2.0/UDP 10.48.32.90:5060;branch=z9hG4bK204e754eaeae
From: <sip:9110001@10.48.32.90;x-farend;x-refci=38960750;x-nearendclusterid=glenscucm10-5;x-nearenddevice=sep001795bdd16b;x-nearendaddr=9110001;x-farendrefci=38960749;x-farendclusterid=glenscucm10-5;x-farenddevice=sep0018195aa209;x-farendaddr=9110006>;tag=73602~713e2333-4032-45f1-b1f5-e33cf471acec-38960757
To: <sip:8675309@10.48.32.170>;tag=2
Call-ID: abbb8e00-4291f775-204d-5a20300e@10.48.32.90
CSeq: 101 INVITE
Contact: <sip:10.48.32.170:5060;transport=udp>
Content-Type: application/sdp
Content-Length:   135

v=0
o=user1 53655765 2353687637 IN IP4 10.48.32.170
s=-
c=IN IP4 10.48.32.170
t=0 0
m=audio 6000 RTP/AVP 0
a=rtpmap:0 PCMU/8000
```

```
### CUCM sends outbound ACK in response to 200 OK #1

03797500.001 |20:21:09.351 |AppInfo  |//SIP/SIPUdp/wait_SdlSPISignal: Outgoing SIP UDP message to 10.48.32.170:[5060]:
[212236,NET]
ACK sip:10.48.32.170:5060;transport=UDP SIP/2.0
Via: SIP/2.0/UDP 10.48.32.90:5060;branch=z9hG4bK204f50bef815
From: <sip:9110001@10.48.32.90;x-nearend;x-refci=38960750;x-nearendclusterid=glenscucm10-5;x-nearenddevice=sep001795bdd16b;x-nearendaddr=9110001;x-farendrefci=38960749;x-farendclusterid=glenscucm10-5;x-farenddevice=sep0018195aa209;x-farendaddr=9110006>;tag=73601~713e2333-4032-45f1-b1f5-e33cf471acec-38960754
To: <sip:8675309@10.48.32.170>;tag=1
Date: Tue, 30 Sep 2014 00:21:09 GMT
Call-ID: abbb8e00-4291f775-204c-5a20300e@10.48.32.90
User-Agent: Cisco-CUCM10.5
Max-Forwards: 70
CSeq: 101 ACK
Allow-Events: presence, kpml
Content-Type: application/sdp
Content-Length: 254

v=0
o=CiscoSystemsCCM-SIP 73601 1 IN IP4 10.48.32.90
s=SIP Call
c=IN IP4 10.48.32.33
b=TIAS:64000
b=CT:64
b=AS:64
t=0 0
m=audio 4000 RTP/AVP 0 101
a=ptime:20
a=rtpmap:0 PCMU/8000
a=sendonly
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
```

```
### CUCM sends startMediaTransmission to the called (recorded) phone telling the phone to send RTP to recording server (10.48.32.170)

03797479.001 |20:21:09.350 |AppInfo  |StationD:    (0000114) startMediaTransmission conferenceID=38960750 passThruPartyID=33554452 remoteIpAddress=IpAddr.type:0 ipAddr:0x0e3020aa000000000000000000000000(10.48.32.170) remotePortNumber=6000 milliSecondPacketSize=20 compressType=4(Media_Payload_G711Ulaw64k) RFC2833PayloadType=0 qualifierOut=?. myIP: IpAddr.type:0 ipv4Addr:0x0e302021(10.48.32.33)
```

```
### CUCM sends startMediaTransmission #2 to the called (recorded) phone telling the phone to send RTP to recording server (10.48.32.170)

03797596.001 |20:21:09.354 |AppInfo  |StationD:    (0000114) startMediaTransmission conferenceID=38960750 passThruPartyID=33554453 remoteIpAddress=IpAddr.type:0 ipAddr:0x0e3020aa000000000000000000000000(10.48.32.170) remotePortNumber=6000 milliSecondPacketSize=20 compressType=4(Media_Payload_G711Ulaw64k) RFC2833PayloadType=0 qualifierOut=?. myIP: IpAddr.type:0 ipv4Addr:0x0e302021(10.48.32.33)
```

```
### CUCM sends outbound ACK in response to 200 OK #2

03797615.001 |20:21:09.354 |AppInfo  |//SIP/SIPUdp/wait_SdlSPISignal: Outgoing SIP UDP message to 10.48.32.170:[5060]:
[212237,NET]
ACK sip:10.48.32.170:5060;transport=UDP SIP/2.0
Via: SIP/2.0/UDP 10.48.32.90:5060;branch=z9hG4bK2050183495f1
From: <sip:9110001@10.48.32.90;x-farend;x-refci=38960750;x-nearendclusterid=glenscucm10-5;x-nearenddevice=sep001795bdd16b;x-nearendaddr=9110001;x-farendrefci=38960749;x-farendclusterid=glenscucm10-5;x-farenddevice=sep0018195aa209;x-farendaddr=9110006>;tag=73602~713e2333-4032-45f1-b1f5-e33cf471acec-38960757
To: <sip:8675309@10.48.32.170>;tag=2
Date: Tue, 30 Sep 2014 00:21:09 GMT
Call-ID: abbb8e00-4291f775-204d-5a20300e@10.48.32.90
User-Agent: Cisco-CUCM10.5
Max-Forwards: 70
CSeq: 101 ACK
Allow-Events: presence, kpml
Content-Type: application/sdp
Content-Length: 254

v=0
o=CiscoSystemsCCM-SIP 73602 1 IN IP4 10.48.32.90
s=SIP Call
c=IN IP4 10.48.32.33
b=TIAS:64000
b=CT:64
b=AS:64
t=0 0
m=audio 4000 RTP/AVP 0 101
a=ptime:20
a=rtpmap:0 PCMU/8000
a=sendonly
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
```

```
### Calling phone sends CUCM the ORC ACK

03797634.001 |20:21:09.385 |AppInfo  |StationInit: (0000109) OpenReceiveChannelAck Status=0, IpAddr=IpAddr.type:0 ipAddr:0x0e30201c000000000000000000000000(10.48.32.28), Port=17996, PartyID=33554450
```

```
### CUCM sends startMediaTransmission to the called (recorded) phone telling the phone to send RTP to the calling phone (10.48.32.28)

03797642.001 |20:21:09.385 |AppInfo  |StationD:    (0000114) startMediaTransmission conferenceID=38960750 passThruPartyID=33554451 remoteIpAddress=IpAddr.type:0 ipAddr:0x0e30201c000000000000000000000000(10.48.32.28) remotePortNumber=17996 milliSecondPacketSize=20 compressType=4(Media_Payload_G711Ulaw64k) RFC2833PayloadType=0 qualifierOut=?. myIP: IpAddr.type:0 ipv4Addr:0x0e302021(10.48.32.33)
```

```
### Called (recorded) phone sends CUCM the ORC ACK

03797643.001 |20:21:09.454 |AppInfo  |StationInit: (0000114) OpenReceiveChannelAck Status=0, IpAddr=IpAddr.type:0 ipAddr:0x0e302021000000000000000000000000(10.48.32.33), Port=32588, PartyID=33554451
```

```
### CUCM sends startMediaTransmission to the calling phone telling the phone to send RTP to the called phone (10.48.32.33)

03797655.001 |20:21:09.454 |AppInfo  |StationD:    (0000109) startMediaTransmission conferenceID=
38960749 passThruPartyID=33554450 remoteIpAddress=IpAddr.type:0 ipAddr:0x0e302021000000000000000000000000(10.48.32.33) remotePortNumber=32588 milliSecondPacketSize=20 compressType=4(Media_Payload_G711Ulaw64k) RFC2833PayloadType=0 qualifierOut=?. myIP: IpAddr.type:0 ipv4Addr:0x0e30201c(10.48.32.28)
```

### SIP

```
~~~~~~~~~~~~~~~~~~~~~~
Normal CCM Traces for SIP phone to SIP phone with SIP Integrated Call Recording
~~~~~~~~~~~~~~~~~~~~~~

##### Calling phone places call

04241111.002 |11:27:41.232 |AppInfo  |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.48.38.102 on port 50147 index 32 with 1946 bytes:
[286938,NET]
INVITE sip:1001@10.48.38.5;user=phone SIP/2.0
Via: SIP/2.0/TCP 10.48.38.102:50147;branch=z9hG4bK598c2eb2
From: "SJ User 1" <sip:1000@10.48.38.5>;tag=38ed18552a12296c00ff41e8-5fb7856e
To: <sip:1001@10.48.38.5>
Call-ID: 38ed1855-2a120006-78c34baf-1b81d864@10.48.38.102
Max-Forwards: 70
Session-ID: 1001532000105000a00038ed18552a12;remote=00000000000000000000000000000000
Date: Tue, 27 Aug 2019 15:27:42 GMT
CSeq: 101 INVITE
User-Agent: Cisco-CP7861/12.1.1
Contact: <sip:ab17ea6e-8072-927d-aad0-d10273906106@10.48.38.102:50147;transport=tcp>;+u.sip!devicename.ccm.cisco.com="SEP38ED18552A12"
Expires: 180
Accept: application/sdp
Allow: ACK,BYE,CANCEL,INVITE,NOTIFY,OPTIONS,REFER,REGISTER,UPDATE,SUBSCRIBE,INFO
Remote-Party-ID: "SJ User 1" <sip:1000@10.48.38.5>;party=calling;id-type=subscriber;privacy=off;screen=yes
Supported: replaces,join,sdp-anat,norefersub,resource-priority,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-7.0.0,X-cisco-xsi-8.5.1
Allow-Events: kpml,dialog
Recv-Info: conference
Recv-Info: x-cisco-conference
Content-Length: 687
Content-Type: application/sdp
Content-Disposition: session;handling=optional

v=0
o=Cisco-SIPUA 15384 0 IN IP4 10.48.38.102
s=SIP Call
b=AS:4064
t=0 0
m=audio 17904 RTP/AVP 114 9 113 115 0 8 116 18 101
c=IN IP4 10.48.38.102
b=TIAS:64000
a=rtpmap:114 opus/48000/2
a=fmtp:114 maxplaybackrate=16000;sprop-maxcapturerate=16000;maxaveragebitrate=64000;stereo=0;sprop-stereo=0;usedtx=0
a=rtpmap:9 G722/8000
a=rtpmap:113 AMR-WB/16000
a=fmtp:113 octet-align=0;mode-change-capability=2
a=rtpmap:115 AMR-WB/16000
a=fmtp:115 octet-align=1;mode-change-capability=2
a=rtpmap:0 PCMU/8000
a=rtpmap:8 PCMA/8000
a=rtpmap:116 iLBC/8000
a=fmtp:116 mode=20
a=rtpmap:18 G729/8000
a=fmtp:18 annexb=yes
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=sendrecv
```

```
##### CUCM performs digit analysis against the dialed digits (dd="1000")

04241138.007 |11:27:41.238 |AppInfo  |Digit analysis: match(pi="2", fqcn="+14085251000", cn="1000",plv="5", pss="EMERGENCY_PT:INTERNAL_PT:SJ_LOCAL_PT:LD_PT:GLOBALIZED_PT", TodFilteredPss="EMERGENCY_PT:INTERNAL_PT:SJ_LOCAL_PT:LD_PT:GLOBALIZED_PT", dd="1001",dac="0")
04241138.008 |11:27:41.238 |AppInfo  |Digit analysis: analysis results
04241138.009 |11:27:41.238 |AppInfo  ||PretransformCallingPartyNumber=1000
|CallingPartyNumber=1000
|DialingPartition=INTERNAL_PT
|DialingPattern=1001
|FullyQualifiedCalledPartyNumber=+14085251001
|DialingPatternRegularExpression=(1001)
|DialingWhere=
|PatternType=Enterprise
|PotentialMatches=NoPotentialMatchesExist
|DialingSdlProcessId=(0,0,0)
|PretransformDigitString=1001
|PretransformTagsList=SUBSCRIBER
|PretransformPositionalMatchList=1001
|CollectedDigits=1001
```

```
##### CUCM determines call must stay on same node and go to LineControl (PID=LineControl(1,100,178,34))

04241140.001 |11:27:41.238 |AppInfo  |Digit analysis: wait_DmPidRes- Partition=[a067f454-fb26-2d1f-59da-a3f946a442c4] Pattern=[1001] Where=[],cmDeviceType=[UserDevice], OutsideDialtone =[0], DeviceOverride=[0], PID=LineControl(1,100,178,34),CI=[19301624],Sender=Cdcc(1,100,224,37)
```

```
##### CUCM sends outbound INVITE to called (recorded) phone

04241178.001 |11:27:41.242 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.48.38.107 on port 51902 index 52 
[286940,NET]
INVITE sip:91a43f66-ca58-9cd3-b0e5-588aa61a72bc@10.48.38.107:51902;transport=tcp SIP/2.0
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32e829c48246
From: "SJ User 1" <sip:1000@10.48.38.5>;tag=104952~e650e088-60ba-4195-8387-3dcc0127efdc-19301625
To: <sip:1001@10.48.38.5>
Date: Tue, 27 Aug 2019 15:27:41 GMT
Call-ID: 34241a00-d6514bed-327f-526300e@10.48.38.5
Supported: timer,resource-priority,replaces
Min-SE:  1800
User-Agent: Cisco-CUCM11.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence
Call-Info: <urn:x-cisco-remotecc:callinfo>; security= Unknown; orientation= from; gci= 1-2029; isVoip; call-instance= 1
Send-Info: conference, x-cisco-conference
Alert-Info: <file://Bellcore-dr1/>
Session-ID: 1001532000105000a00038ed18552a12;remote=00000000000000000000000000000000
Remote-Party-ID: "SJ User 1" <sip:1000@10.48.38.5;x-cisco-callback-number=1000>;party=calling;screen=yes;privacy=off
Contact: <sip:1000@10.48.38.5:5060;transport=tcp>;+u.sip!devicename.ccm.cisco.com="SEP38ED18552A12"
Max-Forwards: 69
Content-Length: 0
```

```
##### Called (recorded) phone returns 200 OK
 
04241233.002 |11:27:43.614 |AppInfo  |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.48.38.107 on port 51902 index 52 with 1902 bytes:
[286947,NET]
SIP/2.0 200 OK
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32e829c48246
From: "SJ User 1" <sip:1000@10.48.38.5>;tag=104952~e650e088-60ba-4195-8387-3dcc0127efdc-19301625
To: <sip:1001@10.48.38.5>;tag=6c416a369525006f33cf6f38-43c38ad2
Call-ID: 34241a00-d6514bed-327f-526300e@10.48.38.5
Session-ID: 4313758700105000a0006c416a369525;remote=1001532000105000a00038ed18552a12
Date: Tue, 27 Aug 2019 15:27:42 GMT
CSeq: 101 INVITE
Server: Cisco-CP7841/12.1.1
Contact: <sip:91a43f66-ca58-9cd3-b0e5-588aa61a72bc@10.48.38.107:51902;transport=tcp>;+u.sip!devicename.ccm.cisco.com="SEP6C416A369525"
Allow: ACK,BYE,CANCEL,INVITE,NOTIFY,OPTIONS,REFER,REGISTER,UPDATE,SUBSCRIBE,INFO
Remote-Party-ID: "SJ User 2" <sip:1001@10.48.38.5>;party=called;id-type=subscriber;privacy=off;screen=yes
Supported: replaces,join,sdp-anat,norefersub,resource-priority,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-7.0.0,X-cisco-xsi-8.5.1
Allow-Events: kpml,dialog
Recv-Info: conference
Recv-Info: x-cisco-conference
Content-Length: 685
Content-Type: application/sdp
Content-Disposition: session;handling=optional

v=0
o=Cisco-SIPUA 899 0 IN IP4 10.48.38.107
s=SIP Call
b=AS:4064
t=0 0
m=audio 20394 RTP/AVP 114 9 113 115 0 8 116 18 101
c=IN IP4 10.48.38.107
b=TIAS:64000
a=rtpmap:114 opus/48000/2
a=fmtp:114 maxplaybackrate=16000;sprop-maxcapturerate=16000;maxaveragebitrate=64000;stereo=0;sprop-stereo=0;usedtx=0
a=rtpmap:9 G722/8000
a=rtpmap:113 AMR-WB/16000
a=fmtp:113 octet-align=0;mode-change-capability=2
a=rtpmap:115 AMR-WB/16000
a=fmtp:115 octet-align=1;mode-change-capability=2
a=rtpmap:0 PCMU/8000
a=rtpmap:8 PCMA/8000
a=rtpmap:116 iLBC/8000
a=fmtp:116 mode=20
a=rtpmap:18 G729/8000
a=fmtp:18 annexb=yes
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=sendrec
```

```
### CUCM sends ACK to called (recorded) phone telling the called phone to send media to the calling phone (10.48.32.28) 

01314344.001 |11:18:48.652 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.48.32.17 on port 50841 index 17 
[106320,NET]
ACK sip:56ce4d7f-d3a2-40fd-a8b3-3f93c8832b9d@10.48.32.17:50841;transport=tcp SIP/2.0
Via: SIP/2.0/TCP 10.48.32.90:5060;branch=z9hG4bK203c2831c118
From: <sip:9110006@10.48.32.90>;tag=38244~713e2333-4032-45f1-b1f5-e33cf471acec-47601638
To: <sip:9110011@10.48.32.90>;tag=b000b4d9e8cb0bba73e445ee-3cc7e650
Date: Tue, 14 Oct 2014 15:18:44 GMT
Call-ID: 6198e780-43d13ed4-203c-5a20300e@10.48.32.90
User-Agent: Cisco-CUCM10.5
Max-Forwards: 70
CSeq: 101 ACK
Allow-Events: presence
Content-Type: application/sdp
Content-Length: 243

v=0
o=CiscoSystemsCCM-SIP 38244 1 IN IP4 10.48.32.90
s=SIP Call
c=IN IP4 10.48.32.28
b=TIAS:64000
b=CT:64
b=AS:64
t=0 0
m=audio 17260 RTP/AVP 0 101
a=ptime:20
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15### CUCM allocates BiB on called (recorded) phone

01314383.000 |11:18:48.675 |SdlSig   |MrmAllocateUcbResourceReq              |waiting                        |MediaResourceManager(2,100,138,1) |Cc(2,100,220,1)                  |2,100,14,20.16735^10.48.32.28^SEP0018195AA209 |[R:N-H:0,N:3,L:1,V:0,Z:0,D:0]  CI=47601639 SsType=33554461 SsKey=1 BridgeType=0 MRGLPkid= NumStream=1 Bib=c32d6714-48bd-43d7-b96f-91363aff3aa0 BibTgCi=47601638 FeatId=159 PL=5 PLDmn=0 DeviceCapability=0 NumVideoCapable=0 requestDeviceType=0 requestDeviceLocale=64 forkingDevicePosition=2 playToneDir=3
```

```
##### CUCM forwards the 200 OK to the calling phone

04241368.001 |11:27:43.624 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.48.38.102 on port 50147 index 32 
[286949,NET]
SIP/2.0 200 OK
Via: SIP/2.0/TCP 10.48.38.102:50147;branch=z9hG4bK598c2eb2
From: "SJ User 1" <sip:1000@10.48.38.5>;tag=38ed18552a12296c00ff41e8-5fb7856e
To: <sip:1001@10.48.38.5>;tag=104951~e650e088-60ba-4195-8387-3dcc0127efdc-19301624
Date: Tue, 27 Aug 2019 15:27:41 GMT
Call-ID: 38ed1855-2a120006-78c34baf-1b81d864@10.48.38.102
CSeq: 101 INVITE
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
Allow-Events: presence
Supported: replaces
Server: Cisco-CUCM11.5
Call-Info: <urn:x-cisco-remotecc:callinfo>; security= NotAuthenticated; orientation= to; gci= 1-2029; isVoip; call-instance= 1
Send-Info: conference, x-cisco-conference
Remote-Party-ID: "SJ User 2" <sip:1001@10.48.38.5>;party=called;screen=yes;privacy=off
Session-ID: 4313758700105000a0006c416a369525;remote=1001532000105000a00038ed18552a12
Remote-Party-ID: "SJ User 2" <sip:1001@10.48.38.5;user=phone>;party=x-cisco-original-called;privacy=off
Contact: <sip:1001@10.48.38.5:5060;transport=tcp>;+u.sip!devicename.ccm.cisco.com="SEP6C416A369525"
Content-Type: application/sdp
Content-Length: 223

v=0
o=CiscoSystemsCCM-SIP 104951 1 IN IP4 10.48.38.5
s=SIP Call
c=IN IP4 10.48.38.107
b=AS:64
t=0 0
m=audio 20394 RTP/AVP 0 101
b=TIAS:64000
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
```

```
##### BiB allocation request on called (recorded) phone

04241393.000 |11:27:43.629 |SdlSig   |SIPAllocateBibResourceReq              |restart0                       |SIPBuiltInBridgeControl(1,100,86,15) |SIPStationCdfc(1,100,77,21)      |1,100,14,83.39^10.48.38.107^*            |[R:N-H:0,N:1,L:0,V:0,Z:0,D:0]  CI=19301626 NumStream=1 BridgeType=0 SsType=16777246 SsKey=5 JccbId=104952 PeerAddr = 10.48.38.107:51902
```

```
##### BiB allocated on called (recorded) phone

04241400.000 |11:27:43.630 |SdlSig   |MrmAllocateSharedResourceRes           |wait                           |Cc(1,100,225,1)                  |MediaResourceManager(1,100,142,1) |1,100,14,83.39^10.48.38.107^*            |[R:N-H:0,N:4,L:0,V:0,Z:0,D:0]  CI=19301626 SsType=16777246 SsKey=5 DN=b0018615001 Name=1b802aa4-863d-879c-f003-9b6de9a1fae5 Pid=1,100,76,27 BibFlag=T DeviceCapability=256 mPrimaryPartition=
```

```
##### DA for first call to activate BiB

04241418.006 |11:27:43.631 |AppInfo  |Digit analysis: match(pi="1", fqcn="", cn="",plv="5", pss="", TodFilteredPss="", dd="b0018615001",dac="0")
04241418.007 |11:27:43.631 |AppInfo  |Digit analysis: analysis results
04241418.008 |11:27:43.631 |AppInfo  ||PretransformCallingPartyNumber=
|CallingPartyNumber=
|DialingPartition=
|DialingPattern=b0018615001
|FullyQualifiedCalledPartyNumber=b0018615001
|DialingPatternRegularExpression=(b0018615001)
|DialingWhere=
|PatternType=Enterprise
|PotentialMatches=NoPotentialMatchesExist
|DialingSdlProcessId=(1,86,15)
|PretransformDigitString=b0018615001
|PretransformTagsList=SUBSCRIBER
|PretransformPositionalMatchList=b0018615001
|CollectedDigits=b0018615001
```

```
##### CUCM sends INVITE #1 to called (recorded) phone with record-invoker=auto in Call-Info field and original Call-ID in Join field
 Notice the SDP has a=inactive - even though there is no media established on the Bib yet.

04241449.001 |11:27:43.633 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.48.38.107 on port 51902 index 52 
[286950,NET]
INVITE sip:91a43f66-ca58-9cd3-b0e5-588aa61a72bc@10.48.38.107:51902;transport=tcp SIP/2.0
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32ea2a115cd6
From: "Call Manager" <sip:10.48.38.5>;tag=104956~e650e088-60ba-4195-8387-3dcc0127efdc-19301628
To: <sip:1001@10.48.38.5>
Date: Tue, 27 Aug 2019 15:27:43 GMT
Call-ID: 35554700-d6514bef-3280-526300e@10.48.38.5
Supported: timer,resource-priority,replaces
Min-SE:  1800
User-Agent: Cisco-CUCM11.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence
Call-Info: <urn:x-cisco-remotecc:callinfo>; isVoip; record-invoker=auto
Join: 34241a00-d6514bed-327f-526300e@10.48.38.5;from-tag=6c416a369525006f33cf6f38-43c38ad2;to-tag=104952~e650e088-60ba-4195-8387-3dcc0127efdc-19301625
Session-ID: 00000000000000000000000000000000;remote=00000000000000000000000000000000
Remote-Party-ID: "Call Manager" <sip:10.48.38.5>;party=calling;screen=yes;privacy=off
Contact: <sip:10.48.38.5:5060;transport=tcp>
Max-Forwards: 70
Content-Type: application/sdp
Content-Length: 187

v=0
o=CiscoSystemsCCM-SIP 104956 1 IN IP4 10.48.38.5
s=SIP Call
c=IN IP4 10.48.38.5
t=0 0
m=audio 4000 RTP/AVP 0
a=label:X-relay-nearend
a=rtpmap:0 PCMU/8000
a=inactive
a=mid:1
```

```
##### Calling phone sends CUCM an ACK in response to the 200 OK which was from when the user at the called phone answered the phone
 
04241455.002 |11:27:43.697 |AppInfo  |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.48.38.102 on port 50147 index 32 with 706 bytes:
[286951,NET]
ACK sip:1001@10.48.38.5:5060;transport=tcp SIP/2.0
Via: SIP/2.0/TCP 10.48.38.102:50147;branch=z9hG4bK688db3c1
From: "SJ User 1" <sip:1000@10.48.38.5>;tag=38ed18552a12296c00ff41e8-5fb7856e
To: <sip:1001@10.48.38.5>;tag=104951~e650e088-60ba-4195-8387-3dcc0127efdc-19301624
Call-ID: 38ed1855-2a120006-78c34baf-1b81d864@10.48.38.102
Max-Forwards: 70
Session-ID: 1001532000105000a00038ed18552a12;remote=4313758700105000a0006c416a369525
Date: Tue, 27 Aug 2019 15:27:45 GMT
CSeq: 101 ACK
User-Agent: Cisco-CP7861/12.1.1
Remote-Party-ID: "SJ User 1" <sip:1000@10.48.38.5>;party=calling;id-type=subscriber;privacy=off;screen=yes
Content-Length: 0
Recv-Info: conference
Recv-Info: x-cisco-conference
```

```
##### Called (recorded) phone returns 200 OK in response to the invite with "record-invoker=auto"
 Notice the SDP has a=inactive - even though there is no media established on the Bib yet.
 
04241466.002 |11:27:43.901 |AppInfo  |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.48.38.107 on port 51902 index 52 with 1433 bytes:
[286953,NET]
SIP/2.0 200 OK
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32ea2a115cd6
From: "Call Manager" <sip:10.48.38.5>;tag=104956~e650e088-60ba-4195-8387-3dcc0127efdc-19301628
To: <sip:1001@10.48.38.5>;tag=6c416a369525007019bf48f9-5901eb85
Call-ID: 35554700-d6514bef-3280-526300e@10.48.38.5
Session-ID: 0848153900105000a0006c416a369525;remote=00000000000000000000000000000000
Date: Tue, 27 Aug 2019 15:27:42 GMT
CSeq: 101 INVITE
Server: Cisco-CP7841/12.1.1
Contact: <sip:91a43f66-ca58-9cd3-b0e5-588aa61a72bc@10.48.38.107:51902;transport=tcp>;+u.sip!devicename.ccm.cisco.com="SEP6C416A369525"
Allow: ACK,BYE,CANCEL,INVITE,NOTIFY,OPTIONS,REFER,REGISTER,UPDATE,SUBSCRIBE,INFO
Remote-Party-ID: "SJ User 2" <sip:1001@10.48.38.5>;party=called;id-type=subscriber;privacy=off;screen=yes
Supported: replaces,join,sdp-anat,norefersub,resource-priority,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-7.0.0,X-cisco-xsi-8.5.1
Allow-Events: kpml,dialog
Recv-Info: conference
Recv-Info: x-cisco-conference
Content-Length: 218
Content-Type: application/sdp
Content-Disposition: session;handling=optional

v=0
o=Cisco-SIPUA 2684 0 IN IP4 10.48.38.107
s=SIP Call
t=0 0
m=audio 26396 RTP/AVP 0 101
c=IN IP4 10.48.38.107
b=TIAS:64000
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=inactive
```

```
##### CUCM responds to called (recorded) phone with ACK 04241469.001 |11:27:43.901 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.48.38.107 on port 51902 index 52 
[286954,NET]
ACK sip:91a43f66-ca58-9cd3-b0e5-588aa61a72bc@10.48.38.107:51902;transport=tcp SIP/2.0
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32eb34decb69
From: "Call Manager" <sip:10.48.38.5>;tag=104956~e650e088-60ba-4195-8387-3dcc0127efdc-19301628
To: <sip:1001@10.48.38.5>;tag=6c416a369525007019bf48f9-5901eb85
Date: Tue, 27 Aug 2019 15:27:43 GMT
Call-ID: 35554700-d6514bef-3280-526300e@10.48.38.5
User-Agent: Cisco-CUCM11.5
Max-Forwards: 70
CSeq: 101 ACK
Allow-Events: presence
Content-Length: 0
```

```
##### BiB places first call to recording destination address (cn is calling party which is the BiB cn="b0018615001" and it is dialing the recordingdestination dd="7878")
 
04241501.011 |11:27:43.905 |AppInfo  |Digit analysis: match(pi="1", fqcn="", cn="b0018615001",plv="5", pss="EMERGENCY_PT:INTERNAL_PT", TodFilteredPss="EMERGENCY_PT:INTERNAL_PT", dd="7878",dac="0")
04241501.012 |11:27:43.905 |AppInfo  |Digit analysis: analysis results
04241501.013 |11:27:43.905 |AppInfo  ||PretransformCallingPartyNumber=b0018615001
|CallingPartyNumber=b0018615001
|DialingPartition=INTERNAL_PT
|DialingPattern=7878
|FullyQualifiedCalledPartyNumber=7878
|DialingPatternRegularExpression=(7878)
|DialingWhere=
|PatternType=Enterprise
|PotentialMatches=NoPotentialMatchesExist
|DialingSdlProcessId=(0,0,0)
|PretransformDigitString=7878
|PretransformTagsList=SUBSCRIBER
|PretransformPositionalMatchList=7878
|CollectedDigits=7878
```

```
##### DA for to activate BiB for the other person's side of the call
 
04241545.006 |11:27:43.907 |AppInfo  |Digit analysis: match(pi="1", fqcn="", cn="",plv="5", pss="", TodFilteredPss="", dd="b0018615001",dac="0")
04241545.007 |11:27:43.907 |AppInfo  |Digit analysis: analysis results
04241545.008 |11:27:43.907 |AppInfo  ||PretransformCallingPartyNumber=
|CallingPartyNumber=
|DialingPartition=
|DialingPattern=b0018615001
|FullyQualifiedCalledPartyNumber=b0018615001
|DialingPatternRegularExpression=(b0018615001)
|DialingWhere=
|PatternType=Enterprise
|PotentialMatches=NoPotentialMatchesExist
|DialingSdlProcessId=(1,86,15)
|PretransformDigitString=b0018615001
|PretransformTagsList=SUBSCRIBER
|PretransformPositionalMatchList=b0018615001
|CollectedDigits=b0018615001
```

```
##### CUCM sends INVITE #1 to configured recording server (10.48.38.30)
 
04241555.001 |11:27:43.908 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.48.38.30 on port 5060 index 50 
[286955,NET]
INVITE sip:7878@10.48.38.30:5060 SIP/2.0
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32ecc2c802c
From: "SJ User 2" <sip:1001@10.48.38.5;x-nearend;x-refci=19301625;x-nearendclusterid=StandAloneCluster;x-nearenddevice=SEP6C416A369525;x-nearendaddr=1001;x-farendrefci=19301624;x-farendclusterid=StandAloneCluster;x-farenddevice=SEP38ED18552A12;x-farendaddr=1000>;tag=104958~e650e088-60ba-4195-8387-3dcc0127efdc-19301629
To: <sip:7878@10.48.38.30>
Date: Tue, 27 Aug 2019 15:27:43 GMT
Call-ID: 35554700-d6514bef-3281-526300e@10.48.38.5
Supported: timer,resource-priority,replaces
Min-SE:  1800
User-Agent: Cisco-CUCM11.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence, kpml
Supported: X-cisco-srtp-fallback
Supported: Geolocation
Call-Info: <sip:10.48.38.5:5060>;method="NOTIFY;Event=telephone-event;Duration=500"
Call-Info: <urn:x-cisco-remotecc:callinfo>;x-cisco-video-traffic-class=DESKTOP
Session-ID: 0848153900105000a0006c416a369525;remote=00000000000000000000000000000000
Cisco-Guid: 0894781184-0000065536-0000000022-0086388750
Session-Expires:  1800
P-Asserted-Identity: "SJ User 2" <sip:1001@10.48.38.5>
Remote-Party-ID: "SJ User 2" <sip:1001@10.48.38.5>;party=calling;screen=yes;privacy=off
Contact: <sip:1001@10.48.38.5:5060;transport=tcp>;isFocus;+u.sip!devicename.ccm.cisco.com="SEP6C416A369525"
Max-Forwards: 70
Content-Length: 0
```

```
##### CUCM sends INVITE #2 to called (recorded) phone with record-invoker=auto in Call-Info field and original Call-ID in Join field
 Notice the SDP has a=inactive - even though there is no media established on the Bib yet.
 
04241590.001 |11:27:43.910 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.48.38.107 on port 51902 index 52 
[286956,NET]
INVITE sip:91a43f66-ca58-9cd3-b0e5-588aa61a72bc@10.48.38.107:51902;transport=tcp SIP/2.0
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32ed62f39668
From: "Call Manager" <sip:10.48.38.5>;tag=104959~e650e088-60ba-4195-8387-3dcc0127efdc-19301631
To: <sip:1001@10.48.38.5>
Date: Tue, 27 Aug 2019 15:27:43 GMT
Call-ID: 35554700-d6514bef-3282-526300e@10.48.38.5
Supported: timer,resource-priority,replaces
Min-SE:  1800
User-Agent: Cisco-CUCM11.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence
Call-Info: <urn:x-cisco-remotecc:callinfo>; isVoip; record-invoker=auto
Join: 34241a00-d6514bed-327f-526300e@10.48.38.5;from-tag=6c416a369525006f33cf6f38-43c38ad2;to-tag=104952~e650e088-60ba-4195-8387-3dcc0127efdc-19301625
Session-ID: 00000000000000000000000000000000;remote=00000000000000000000000000000000
Remote-Party-ID: "Call Manager" <sip:10.48.38.5>;party=calling;screen=yes;privacy=off
Contact: <sip:10.48.38.5:5060;transport=tcp>
Max-Forwards: 70
Content-Type: application/sdp
Content-Length: 186

v=0
o=CiscoSystemsCCM-SIP 104959 1 IN IP4 10.48.38.5
s=SIP Call
c=IN IP4 10.48.38.5
t=0 0
m=audio 4000 RTP/AVP 0
a=label:X-relay-farend
a=rtpmap:0 PCMU/8000
a=inactive
a=mid:1
```

```
##### Called (recorded) phone returns 200 OK in response to INVITE #2 to invoke BiB
Notice the SDP has a=inactive - even though there is no media established on the Bib yet.
 
04241614.002 |11:27:44.197 |AppInfo  |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.48.38.107 on port 51902 index 52 with 1434 bytes:
[286959,NET]
SIP/2.0 200 OK
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32ed62f39668
From: "Call Manager" <sip:10.48.38.5>;tag=104959~e650e088-60ba-4195-8387-3dcc0127efdc-19301631
To: <sip:1001@10.48.38.5>;tag=6c416a369525007145d433c8-062b13d7
Call-ID: 35554700-d6514bef-3282-526300e@10.48.38.5
Session-ID: 56a8a95e00105000a0006c416a369525;remote=00000000000000000000000000000000
Date: Tue, 27 Aug 2019 15:27:42 GMT
CSeq: 101 INVITE
Server: Cisco-CP7841/12.1.1
Contact: <sip:91a43f66-ca58-9cd3-b0e5-588aa61a72bc@10.48.38.107:51902;transport=tcp>;+u.sip!devicename.ccm.cisco.com="SEP6C416A369525"
Allow: ACK,BYE,CANCEL,INVITE,NOTIFY,OPTIONS,REFER,REGISTER,UPDATE,SUBSCRIBE,INFO
Remote-Party-ID: "SJ User 2" <sip:1001@10.48.38.5>;party=called;id-type=subscriber;privacy=off;screen=yes
Supported: replaces,join,sdp-anat,norefersub,resource-priority,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-7.0.0,X-cisco-xsi-8.5.1
Allow-Events: kpml,dialog
Recv-Info: conference
Recv-Info: x-cisco-conference
Content-Length: 219
Content-Type: application/sdp
Content-Disposition: session;handling=optional

v=0
o=Cisco-SIPUA 13977 0 IN IP4 10.48.38.107
s=SIP Call
t=0 0
m=audio 17904 RTP/AVP 0 101
c=IN IP4 10.48.38.107
b=TIAS:64000
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=inactive
```

```
##### CUCM responds with ACK for 200 OK for INVITE #2 to invoke the BiB
 
04241618.001 |11:27:44.199 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.48.38.107 on port 51902 index 52 
[286960,NET]
ACK sip:91a43f66-ca58-9cd3-b0e5-588aa61a72bc@10.48.38.107:51902;transport=tcp SIP/2.0
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32ee41b380b1
From: "Call Manager" <sip:10.48.38.5>;tag=104959~e650e088-60ba-4195-8387-3dcc0127efdc-19301631
To: <sip:1001@10.48.38.5>;tag=6c416a369525007145d433c8-062b13d7
Date: Tue, 27 Aug 2019 15:27:43 GMT
Call-ID: 35554700-d6514bef-3282-526300e@10.48.38.5
User-Agent: Cisco-CUCM11.5
Max-Forwards: 70
CSeq: 101 ACK
Allow-Events: presence
Content-Length: 0
```

```
##### BiB places second call to recording destination address (cn is calling party which is the BiB cn="b0018615001" and it is dialing the recordingdestination dd="7878")
 
04241651.011 |11:27:44.201 |AppInfo  |Digit analysis: match(pi="1", fqcn="", cn="b0018615001",plv="5", pss="EMERGENCY_PT:INTERNAL_PT", TodFilteredPss="EMERGENCY_PT:INTERNAL_PT", dd="7878",dac="0")
04241651.012 |11:27:44.202 |AppInfo  |Digit analysis: analysis results
04241651.013 |11:27:44.202 |AppInfo  ||PretransformCallingPartyNumber=b0018615001
|CallingPartyNumber=b0018615001
|DialingPartition=INTERNAL_PT
|DialingPattern=7878
|FullyQualifiedCalledPartyNumber=7878
|DialingPatternRegularExpression=(7878)
|DialingWhere=
|PatternType=Enterprise
|PotentialMatches=NoPotentialMatchesExist
|DialingSdlProcessId=(0,0,0)
|PretransformDigitString=7878
|PretransformTagsList=SUBSCRIBER
|PretransformPositionalMatchList=7878
|CollectedDigits=7878
```

```
##### CUCM sends INVITE #2 to configured recording server
 
04241698.001 |11:27:44.205 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.48.38.30 on port 5060 index 50 
[286961,NET]
INVITE sip:7878@10.48.38.30:5060 SIP/2.0
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32ef2867938b
From: "SJ User 2" <sip:1001@10.48.38.5;x-farend;x-refci=19301625;x-nearendclusterid=StandAloneCluster;x-nearenddevice=SEP6C416A369525;x-nearendaddr=1001;x-farendrefci=19301624;x-farendclusterid=StandAloneCluster;x-farenddevice=SEP38ED18552A12;x-farendaddr=1000>;tag=104961~e650e088-60ba-4195-8387-3dcc0127efdc-19301632
To: <sip:7878@10.48.38.30>
Date: Tue, 27 Aug 2019 15:27:44 GMT
Call-ID: 35eddd80-d6514bf0-3283-526300e@10.48.38.5
Supported: timer,resource-priority,replaces
Min-SE:  1800
User-Agent: Cisco-CUCM11.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence, kpml
Supported: X-cisco-srtp-fallback
Supported: Geolocation
Call-Info: <sip:10.48.38.5:5060>;method="NOTIFY;Event=telephone-event;Duration=500"
Call-Info: <urn:x-cisco-remotecc:callinfo>;x-cisco-video-traffic-class=DESKTOP
Session-ID: 56a8a95e00105000a0006c416a369525;remote=00000000000000000000000000000000
Cisco-Guid: 0904781184-0000065536-0000000023-0086388750
Session-Expires:  1800
P-Asserted-Identity: "SJ User 2" <sip:1001@10.48.38.5>
Remote-Party-ID: "SJ User 2" <sip:1001@10.48.38.5>;party=calling;screen=yes;privacy=off
Contact: <sip:1001@10.48.38.5:5060;transport=tcp>;isFocus;+u.sip!devicename.ccm.cisco.com="SEP6C416A369525"
Max-Forwards: 70
Content-Length: 0
```

```
##### CUCM receives a 200 OK from recording server for INVITE #2
 
04241723.002 |11:27:44.324 |AppInfo  |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.48.38.30 on port 5060 index 50 with 1205 bytes:
[286963,NET]
SIP/2.0 200 Ok
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32ef2867938b
To: <sip:7878@10.48.38.30>;tag=ds1a1d776c
From: "SJ User 2" <sip:1001@10.48.38.5;x-farend;x-refci=19301625;x-nearendclusterid=StandAloneCluster;x-nearenddevice=SEP6C416A369525;x-nearendaddr=1001;x-farendrefci=19301624;x-farendclusterid=StandAloneCluster;x-farenddevice=SEP38ED18552A12;x-farendaddr=1000>;tag=104961~e650e088-60ba-4195-8387-3dcc0127efdc-19301632
Call-ID: 35eddd80-d6514bf0-3283-526300e@10.48.38.5
CSeq: 101 INVITE
Content-Length: 475
Contact: <sip:7878@10.48.38.30:5060;transport=TCP>
Content-Type: application/sdp
Allow: INVITE, BYE, CANCEL, ACK, NOTIFY, INFO, UPDATE
Supported: X-cisco-srtp-fallback
Server: MediaSense/11.x

v=0
o=CiscoORA 707 1 IN IP4 10.48.38.30
s=SIP Call
c=IN IP4 10.48.38.30
t=0 0
m=audio 56512 RTP/SAVP 102 0 8 9 18
a=rtpmap:102 MP4A-LATM/90000
a=fmtp:102 profile-level-id=24;object=23;bitrate=64000
a=rtpmap:0 PCMU/8000
a=rtpmap:8 PCMA/8000
a=rtpmap:9 G722/8000
a=rtpmap:18 G729/8000
a=recvonly
a=crypto:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
a=crypto:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

```
##### CUCM receives 200 OK from the recording server in response to INVITE #1
 
04241743.002 |11:27:44.326 |AppInfo  |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.48.38.30 on port 5060 index 50 with 1205 bytes:
[286964,NET]
SIP/2.0 200 Ok
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32ecc2c802c
To: <sip:7878@10.48.38.30>;tag=ds2c967644
From: "SJ User 2" <sip:1001@10.48.38.5;x-nearend;x-refci=19301625;x-nearendclusterid=StandAloneCluster;x-nearenddevice=SEP6C416A369525;x-nearendaddr=1001;x-farendrefci=19301624;x-farendclusterid=StandAloneCluster;x-farenddevice=SEP38ED18552A12;x-farendaddr=1000>;tag=104958~e650e088-60ba-4195-8387-3dcc0127efdc-19301629
Call-ID: 35554700-d6514bef-3281-526300e@10.48.38.5
CSeq: 101 INVITE
Content-Length: 475
Contact: <sip:7878@10.48.38.30:5060;transport=TCP>
Content-Type: application/sdp
Allow: INVITE, BYE, CANCEL, ACK, NOTIFY, INFO, UPDATE
Supported: X-cisco-srtp-fallback
Server: MediaSense/11.x

v=0
o=CiscoORA 708 1 IN IP4 10.48.38.30
s=SIP Call
c=IN IP4 10.48.38.30
t=0 0
m=audio 59058 RTP/SAVP 102 0 8 9 18
a=rtpmap:102 MP4A-LATM/90000
a=fmtp:102 profile-level-id=24;object=23;bitrate=64000
a=rtpmap:0 PCMU/8000
a=rtpmap:8 PCMA/8000
a=rtpmap:9 G722/8000
a=rtpmap:18 G729/8000
a=recvonly
a=crypto:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
a=crypto:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

```
##### CUCM sends re-INVITE #2 to called (recorded) phone (notice there is no SDP - this is so CUCM can identify the codec the BiB is locked to)
 Notice there is no SDP
 
04241825.001 |11:27:44.330 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.48.38.107 on port 51902 index 52 
[286965,NET]
INVITE sip:91a43f66-ca58-9cd3-b0e5-588aa61a72bc@10.48.38.107:51902;transport=tcp SIP/2.0
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32f014677161
From: "Call Manager" <sip:10.48.38.5>;tag=104959~e650e088-60ba-4195-8387-3dcc0127efdc-19301631
To: <sip:1001@10.48.38.5>;tag=6c416a369525007145d433c8-062b13d7
Date: Tue, 27 Aug 2019 15:27:44 GMT
Call-ID: 35554700-d6514bef-3282-526300e@10.48.38.5
Supported: timer,resource-priority,replaces
User-Agent: Cisco-CUCM11.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, SUBSCRIBE, NOTIFY
CSeq: 102 INVITE
Max-Forwards: 70
Expires: 180
Allow-Events: presence
Call-Info: <urn:x-cisco-remotecc:callinfo>; isVoip; record-invoker=auto
Min-SE:  1800
Session-ID: 00000000000000000000000000000000;remote=56a8a95e00105000a0006c416a369525
Remote-Party-ID: "Call Manager" <sip:10.48.38.5>;party=calling;screen=yes;privacy=off
Contact: <sip:10.48.38.5:5060;transport=tcp>
Content-Length: 0
```

```
##### CUCM sends re-INVITE #1 to called (recorded) phone (notice there is no SDP - this is so CUCM can identify the codec the BiB is locked to)
 
04241866.001 |11:27:44.332 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.48.38.107 on port 51902 index 52 
[286966,NET]
INVITE sip:91a43f66-ca58-9cd3-b0e5-588aa61a72bc@10.48.38.107:51902;transport=tcp SIP/2.0
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32f11da4ce39
From: "Call Manager" <sip:10.48.38.5>;tag=104956~e650e088-60ba-4195-8387-3dcc0127efdc-19301628
To: <sip:1001@10.48.38.5>;tag=6c416a369525007019bf48f9-5901eb85
Date: Tue, 27 Aug 2019 15:27:44 GMT
Call-ID: 35554700-d6514bef-3280-526300e@10.48.38.5
Supported: timer,resource-priority,replaces
User-Agent: Cisco-CUCM11.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, SUBSCRIBE, NOTIFY
CSeq: 102 INVITE
Max-Forwards: 70
Expires: 180
Allow-Events: presence
Call-Info: <urn:x-cisco-remotecc:callinfo>; isVoip; record-invoker=auto
Min-SE:  1800
Session-ID: 00000000000000000000000000000000;remote=0848153900105000a0006c416a369525
Remote-Party-ID: "Call Manager" <sip:10.48.38.5>;party=calling;screen=yes;privacy=off
Contact: <sip:10.48.38.5:5060;transport=tcp>
Content-Length: 0
```

```
##### Called (recorded) phone returns 200 OK for re-INVITE #2
 
04241872.002 |11:27:44.541 |AppInfo  |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.48.38.107 on port 51902 index 52 with 1434 bytes:
[286969,NET]
SIP/2.0 200 OK
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32f014677161
From: "Call Manager" <sip:10.48.38.5>;tag=104959~e650e088-60ba-4195-8387-3dcc0127efdc-19301631
To: <sip:1001@10.48.38.5>;tag=6c416a369525007145d433c8-062b13d7
Call-ID: 35554700-d6514bef-3282-526300e@10.48.38.5
Session-ID: 56a8a95e00105000a0006c416a369525;remote=00000000000000000000000000000000
Date: Tue, 27 Aug 2019 15:27:43 GMT
CSeq: 102 INVITE
Server: Cisco-CP7841/12.1.1
Contact: <sip:91a43f66-ca58-9cd3-b0e5-588aa61a72bc@10.48.38.107:51902;transport=tcp>;+u.sip!devicename.ccm.cisco.com="SEP6C416A369525"
Allow: ACK,BYE,CANCEL,INVITE,NOTIFY,OPTIONS,REFER,REGISTER,UPDATE,SUBSCRIBE,INFO
Remote-Party-ID: "SJ User 2" <sip:1001@10.48.38.5>;party=called;id-type=subscriber;privacy=off;screen=yes
Supported: replaces,join,sdp-anat,norefersub,resource-priority,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-7.0.0,X-cisco-xsi-8.5.1
Allow-Events: kpml,dialog
Recv-Info: conference
Recv-Info: x-cisco-conference
Content-Length: 219
Content-Type: application/sdp
Content-Disposition: session;handling=optional

v=0
o=Cisco-SIPUA 13977 1 IN IP4 10.48.38.107
s=SIP Call
t=0 0
m=audio 17904 RTP/AVP 0 101
c=IN IP4 10.48.38.107
b=TIAS:64000
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=sendrecv
```

```
##### Called (recorded) phone returns 200 OK to re-INVITE #1
 
04241885.002 |11:27:44.550 |AppInfo  |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.48.38.107 on port 51902 index 52 with 1433 bytes:
[286970,NET]
SIP/2.0 200 OK
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32f11da4ce39
From: "Call Manager" <sip:10.48.38.5>;tag=104956~e650e088-60ba-4195-8387-3dcc0127efdc-19301628
To: <sip:1001@10.48.38.5>;tag=6c416a369525007019bf48f9-5901eb85
Call-ID: 35554700-d6514bef-3280-526300e@10.48.38.5
Session-ID: 0848153900105000a0006c416a369525;remote=00000000000000000000000000000000
Date: Tue, 27 Aug 2019 15:27:43 GMT
CSeq: 102 INVITE
Server: Cisco-CP7841/12.1.1
Contact: <sip:91a43f66-ca58-9cd3-b0e5-588aa61a72bc@10.48.38.107:51902;transport=tcp>;+u.sip!devicename.ccm.cisco.com="SEP6C416A369525"
Allow: ACK,BYE,CANCEL,INVITE,NOTIFY,OPTIONS,REFER,REGISTER,UPDATE,SUBSCRIBE,INFO
Remote-Party-ID: "SJ User 2" <sip:1001@10.48.38.5>;party=called;id-type=subscriber;privacy=off;screen=yes
Supported: replaces,join,sdp-anat,norefersub,resource-priority,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-7.0.0,X-cisco-xsi-8.5.1
Allow-Events: kpml,dialog
Recv-Info: conference
Recv-Info: x-cisco-conference
Content-Length: 218
Content-Type: application/sdp
Content-Disposition: session;handling=optional

v=0
o=Cisco-SIPUA 2684 1 IN IP4 10.48.38.107
s=SIP Call
t=0 0
m=audio 26396 RTP/AVP 0 101
c=IN IP4 10.48.38.107
b=TIAS:64000
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=sendrecv
```

```
##### CUCM sends ACK to called (recorded) phone for re-INVITE #2
 
04241903.001 |11:27:44.552 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.48.38.107 on port 51902 index 52 
[286971,NET]
ACK sip:91a43f66-ca58-9cd3-b0e5-588aa61a72bc@10.48.38.107:51902;transport=tcp SIP/2.0
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32f252b587f6
From: "Call Manager" <sip:10.48.38.5>;tag=104959~e650e088-60ba-4195-8387-3dcc0127efdc-19301631
To: <sip:1001@10.48.38.5>;tag=6c416a369525007145d433c8-062b13d7
Date: Tue, 27 Aug 2019 15:27:44 GMT
Call-ID: 35554700-d6514bef-3282-526300e@10.48.38.5
User-Agent: Cisco-CUCM11.5
Max-Forwards: 70
CSeq: 102 ACK
Allow-Events: presence
Session-ID: 00000000000000000000000000000000;remote=56a8a95e00105000a0006c416a369525
Content-Type: application/sdp
Content-Length: 192

v=0
o=CiscoSystemsCCM-SIP 104959 3 IN IP4 10.48.38.5
s=SIP Call
c=IN IP4 10.48.38.30
b=TIAS:64000
b=AS:64
t=0 0
m=audio 56512 RTP/AVP 0
b=TIAS:64000
a=rtpmap:0 PCMU/8000
a=recvonly
```

```
##### CUCM sends ACK to the recording server in response to 200 OK #2
 
04241917.001 |11:27:44.555 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.48.38.30 on port 5060 index 50 
[286972,NET]
ACK sip:7878@10.48.38.30:5060;transport=TCP SIP/2.0
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32f373e69393
From: "SJ User 2" <sip:1001@10.48.38.5;x-farend;x-refci=19301625;x-nearendclusterid=StandAloneCluster;x-nearenddevice=SEP6C416A369525;x-nearendaddr=1001;x-farendrefci=19301624;x-farendclusterid=StandAloneCluster;x-farenddevice=SEP38ED18552A12;x-farendaddr=1000>;tag=104961~e650e088-60ba-4195-8387-3dcc0127efdc-19301632
To: <sip:7878@10.48.38.30>;tag=ds1a1d776c
Date: Tue, 27 Aug 2019 15:27:44 GMT
Call-ID: 35eddd80-d6514bf0-3283-526300e@10.48.38.5
User-Agent: Cisco-CUCM11.5
Max-Forwards: 70
CSeq: 101 ACK
Allow-Events: presence, kpml
Session-ID: 56a8a95e00105000a0006c416a369525;remote=c83405810147c69016c38634ab104961
Content-Type: application/sdp
Content-Length: 235

v=0
o=CiscoSystemsCCM-SIP 104961 1 IN IP4 10.48.38.5
s=SIP Call
c=IN IP4 10.48.38.107
b=TIAS:64000
b=AS:64
t=0 0
m=audio 17904 RTP/AVP 0 101
a=rtpmap:0 PCMU/8000
a=sendonly
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
```

```
##### CUCM sends ACK to called (recorded) phone for re-INVITE #1
 
04241947.001 |11:27:44.559 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.48.38.107 on port 51902 index 52 
[286973,NET]
ACK sip:91a43f66-ca58-9cd3-b0e5-588aa61a72bc@10.48.38.107:51902;transport=tcp SIP/2.0
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32f45d25b711
From: "Call Manager" <sip:10.48.38.5>;tag=104956~e650e088-60ba-4195-8387-3dcc0127efdc-19301628
To: <sip:1001@10.48.38.5>;tag=6c416a369525007019bf48f9-5901eb85
Date: Tue, 27 Aug 2019 15:27:44 GMT
Call-ID: 35554700-d6514bef-3280-526300e@10.48.38.5
User-Agent: Cisco-CUCM11.5
Max-Forwards: 70
CSeq: 102 ACK
Allow-Events: presence
Session-ID: 00000000000000000000000000000000;remote=0848153900105000a0006c416a369525
Content-Type: application/sdp
Content-Length: 192

v=0
o=CiscoSystemsCCM-SIP 104956 3 IN IP4 10.48.38.5
s=SIP Call
c=IN IP4 10.48.38.30
b=TIAS:64000
b=AS:64
t=0 0
m=audio 59058 RTP/AVP 0
b=TIAS:64000
a=rtpmap:0 PCMU/8000
a=recvonly
```

```
##### CUCM sends ACK to the recording server in response to 200 OK #1
 
04241948.001 |11:27:44.559 |AppInfo  |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.48.38.30 on port 5060 index 50 
[286974,NET]
ACK sip:7878@10.48.38.30:5060;transport=TCP SIP/2.0
Via: SIP/2.0/TCP 10.48.38.5:5060;branch=z9hG4bK32f573871bbb
From: "SJ User 2" <sip:1001@10.48.38.5;x-nearend;x-refci=19301625;x-nearendclusterid=StandAloneCluster;x-nearenddevice=SEP6C416A369525;x-nearendaddr=1001;x-farendrefci=19301624;x-farendclusterid=StandAloneCluster;x-farenddevice=SEP38ED18552A12;x-farendaddr=1000>;tag=104958~e650e088-60ba-4195-8387-3dcc0127efdc-19301629
To: <sip:7878@10.48.38.30>;tag=ds2c967644
Date: Tue, 27 Aug 2019 15:27:43 GMT
Call-ID: 35554700-d6514bef-3281-526300e@10.48.38.5
User-Agent: Cisco-CUCM11.5
Max-Forwards: 70
CSeq: 101 ACK
Allow-Events: presence, kpml
Session-ID: 0848153900105000a0006c416a369525;remote=c83405810147c69016c38634ab104958
Content-Type: application/sdp
Content-Length: 235

v=0
o=CiscoSystemsCCM-SIP 104958 1 IN IP4 10.48.38.5
s=SIP Call
c=IN IP4 10.48.38.107
b=TIAS:64000
b=AS:64
t=0 0
m=audio 26396 RTP/AVP 0 101
a=rtpmap:0 PCMU/8000
a=sendonly
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
```

## Troubleshoot

This section provides information you can use in order to troubleshoot your configuration.

### Codec Negotiation

This is an example of one of the most common types of call recording failures - codec mismatch between the recorded phone and the recording server:

```
~~~~~~~~~~~~~~~~~~~~~~~~~~
Codec Negotiation Failure
~~~~~~~~~~~~~~~~~~~~~~~~~~

### Calling phone places call

00019629.001 |12:48:34.510 |AppInfo  |StationInit: (0000005) EnblocCall calledParty=9110001.
```

```
### CUCM performs digit analysis against the dialed digits (dd="9110001")

00019638.001 |12:48:34.511 |AppInfo  |Digit Analysis: star_DaReq: daReq.partitionSearchSpace(), filteredPartitionSearchSpaceString(), partitionSearchSpaceString()
00019638.002 |12:48:34.511 |AppInfo  |Digit Analysis: star_DaReq: Matching Legacy Numeric, digits=9110001
00019638.003 |12:48:34.522 |AppInfo  |Digit Analysis: getDaRes data: daRes.ssType=[0] Intercept DAMR.sstype=[0], TPcount=[0], DAMR.NotifyCount=[0], DaRes.NotifyCount=[0]
00019638.004 |12:48:34.522 |AppInfo  |Digit Analysis: getDaRes - Remote Destination [] isURI[1]
00019638.005 |12:48:34.522 |AppInfo  |Digit analysis: patternUsage=2
00019638.006 |12:48:34.522 |AppInfo  |Digit analysis: match(pi="2", fqcn="9110006", cn="9110006",plv="5", pss="", TodFilteredPss="", dd="9110001",dac="1")
00019638.007 |12:48:34.522 |AppInfo  |Digit analysis: analysis results
00019638.008 |12:48:34.522 |AppInfo  ||PretransformCallingPartyNumber=9110006
|CallingPartyNumber=9110006
|DialingPartition=
|DialingPattern=9110001
|FullyQualifiedCalledPartyNumber=9110001
|DialingPatternRegularExpression=(9110001)
|DialingWhere=
|PatternType=Enterprise
|PotentialMatches=NoPotentialMatchesExist
|DialingSdlProcessId=(0,0,0)
|PretransformDigitString=9110001
|PretransformTagsList=SUBSCRIBER
|PretransformPositionalMatchList=9110001
|CollectedDigits=9110001
```

```
### CUCM determines call must stay on same node and go to LineControl (PID=LineControl(2,100,174,19))

00019640.001 |12:48:34.522 |AppInfo  |Digit analysis: wait_DmPidRes- Partition=[] Pattern=[9110001] Where=[],cmDeviceType=[UserDevice], OutsideDialtone =[0], DeviceOverride=[0], PID=LineControl(2,100,174,7),CI=[49613637],Sender=Cdcc(2,100,219,1)
```

```
### CUCM extends the call to the called phone

00019657.003 |12:48:34.560 |AppInfo  |StationD:    (0000007) DEBUG whatToDo: line=1 calls=0 limit=4, busy=2. GCI=(2, 7001), cm_PL=(5, 0).
00019657.004 |12:48:34.560 |AppInfo  |StationD:    (0000007) DEBUG  whatToDo: busy trigger not hit... send to open appearance
00019657.005 |12:48:34.560 |AppInfo  |preFilterCapCount =[11], preFilterCaps :: (Cap)= (25) (6) (4) (2) (7) (8) (15) (16) (11) (12) (257) Filtering Caps due to Service Parameter Configuration postFilterCapCount =[8], postFilterCaps :: (Cap)= (25) (4) (2) (15) (16) (11) (12) (257)
00019657.006 |12:48:34.560 |AppInfo  |preFilterCapCount =[0], preFilterCaps :: (Cap)= Filtering Caps due to Service Parameter Configuration postFilterCapCount =[0], postFilterCaps :: (Cap)=
00019657.007 |12:48:34.560 |Created  |                                       |                               |StationCdpc(2,100,64,2)          |StationD(2,100,63,7)             |                                         |NumOfCurrentInstances: 2
00019657.008 |12:48:34.560 |AppInfo  |StationD:    (0000007) DEBUG- getLineRingSetting: retVal=4.
00019657.009 |12:48:34.560 |AppInfo  |StationD:    (0000007) DEBUG- saveRinger for: ci=49613638, line=1, mode=2, cm_precedence=5, callPhase=5.
00019657.010 |12:48:34.560 |AppInfo  |StationD:    (0000007) DEBUG- saveRinger: ci=49613638, line=1, mode=2, cm_precedence=5, callPhase=5, modifier=0
00019657.011 |12:48:34.560 |AppInfo  |StationD:    (0000007) INFO  sendCallAcceptReq: Try to send StationLineCallAccept to cdpc=2 .
00019657.012 |12:48:34.560 |AppInfo  |StationD:    (0000007) playRinger for: ci=49613638.
00019657.013 |12:48:34.560 |AppInfo  |StationD:    (0000007) DEBUG- getLineRingSetting: retVal=4.
00019657.014 |12:48:34.560 |AppInfo  |StationD:    (0000007) DEBUG- getLineRingSetting: retVal=4.
00019657.015 |12:48:34.560 |AppInfo  |StationD:    (0000007) DEBUG- getLineRingSetting: retVal=4.
```

```
### The Called (recorded) phone goes off hook

00019709.001 |12:48:36.042 |AppInfo  |StationD:    (0000007) restart0_StationOffHook - INFO: CI=49613638 on line=1, SPKMode=0, alwaysPrimeLine=0, alwaysUsePrimeLineForVM=0, fid=9999, offHookTrigger=1.
```

```
### CUCM Tells the calling phone to open the logical channel

00019773.001 |12:48:36.061 |AppInfo  |StationD:    (0000005) SEP0018195AA209 , star_MediaExchangeAgenaOpenLogicalChannel packetSize=20, codec=4, ci=49613637
```

```
### CUCM Tells the called (recorded) to open the logical channel

00019776.001 |12:48:36.061 |AppInfo  |StationD:    (0000007) SEP001795BDD16B , star_MediaExchangeAgenaOpenLogicalChannel packetSize=20, codec=4, ci=49613638
```

```
### CUCM Tells the calling phone to open the receive channel

00019784.002 |12:48:36.062 |AppInfo  |StationD:    (0000005) OpenReceiveChannel conferenceID=49613637 passThruPartyID=33554433 millisecondPacketSize=20 compressionType=4(Media_Payload_G711Ulaw64k) RFC2833PayloadType=0 qualifierIn=? sourceIpAddr=IpAddr.type:0 ipAddr:0x0e302021000000000000000000000000(10.48.32.33). myIP: IpAddr.type:0 ipv4Addr:0x0e30201c(10.48.32.28)
```

```
### Codec locked due to recording on called (recorded) phone

00019785.003 |12:48:36.062 |AppInfo  | StationCdpc: star_MediaExchangeAgenaQueryCapability - Device SEP001795BDD16B, codec locked due to recording, codecType=4
```

```
### CUCM Tells the called (recorded) phone to open the receive channel

00019788.002 |12:48:36.062 |AppInfo  |StationD:    (0000007) OpenReceiveChannel conferenceID=49613638 passThruPartyID=33554434 millisecondPacketSize=20 compressionType=4(Media_Payload_G711Ulaw64k) RFC2833PayloadType=0 qualifierIn=? sourceIpAddr=IpAddr.type:0 ipAddr:0x0e30201c000000000000000000000000(10.48.32.28). myIP: IpAddr.type:0 ipv4Addr:0x0e302021(10.48.32.33)
```

```
### CUCM allocates the BiB on the called (recorded) phone

00019830.000 |12:48:36.074 |SdlSig   |MrmAllocateUcbResourceReq              |waiting                        |MediaResourceManager(2,100,138,1) |Cc(2,100,220,1)                  |2,100,14,19.206^10.48.32.33^SEP001795BDD16B |[R:N-H:0,N:1,L:0,V:0,Z:0,D:0]  CI=49613639 SsType=33554461 SsKey=1 BridgeType=0 MRGLPkid= NumStream=1 Bib=89cdb152-4ef2-4d60-9e6b-ab8c77c22618 BibTgCi=49613638 FeatId=159 PL=5 PLDmn=0 DeviceCapability=0 NumVideoCapable=0 requestDeviceType=0 requestDeviceLocale=64 forkingDevicePosition=2 playToneDir=3
```

```
### BiB places it's first call to recording destination address (cn is calling number which is the BiB cn="b00223906001" and it is dialing the recordingdestination dd="8675309")

00019889.001 |12:48:36.100 |AppInfo  |Digit Analysis: star_DaReq: daReq.partitionSearchSpace(), filteredPartitionSearchSpaceString(), partitionSearchSpaceString()
00019889.002 |12:48:36.100 |AppInfo  |Digit Analysis: star_DaReq: Matching Legacy Numeric, digits=8675309
00019889.003 |12:48:36.100 |AppInfo  |Digit Analysis: getDaRes data: daRes.ssType=[0] Intercept DAMR.sstype=[0], TPcount=[0], DAMR.NotifyCount=[0], DaRes.NotifyCount=[0]
00019889.004 |12:48:36.100 |AppInfo  |Digit Analysis: getDaRes - Remote Destination [8675309] isURI[0]
00019889.005 |12:48:36.100 |AppInfo  |CMUtility routeCallThroughCTIRD: no matching RemDestDynamic record exists for remdest [8675309]
00019889.006 |12:48:36.100 |AppInfo  |DbMobility: getMatchedRemDest starts: cnumber = 8675309
00019889.007 |12:48:36.100 |AppInfo  |DbMobility: getMatchedRemDest: full match case
00019889.008 |12:48:36.100 |AppInfo  |DbMobility SelectByDestination: no matching RemDestDynamic record exists for remdest [8675309]
00019889.009 |12:48:36.100 |AppInfo  |DbMobility: can't find remdest 8675309 in map
00019889.010 |12:48:36.100 |AppInfo  |Digit analysis: patternUsage=5
00019889.011 |12:48:36.100 |AppInfo  |Digit analysis: match(pi="1", fqcn="", cn="b00223906001",plv="5", pss="E911_PT:Phones_PT:EMERGENCY_PT:INTERNAL_PT:INFORMACAST_PT", TodFilteredPss="E911_PT:Phones_PT:EMERGENCY_PT:INTERNAL_PT:INFORMACAST_PT", dd="8675309",dac="1")
00019889.012 |12:48:36.100 |AppInfo  |Digit analysis: analysis results
00019889.013 |12:48:36.100 |AppInfo  ||PretransformCallingPartyNumber=b00223906001
|CallingPartyNumber=b00223906001
|DialingPartition=
|DialingPattern=8675309
|FullyQualifiedCalledPartyNumber=8675309
|DialingPatternRegularExpression=(8675309)
|DialingWhere=
|PatternType=Enterprise
|PotentialMatches=NoPotentialMatchesExist
|DialingSdlProcessId=(0,0,0)
|PretransformDigitString=8675309
|PretransformTagsList=SUBSCRIBER
|PretransformPositionalMatchList=8675309
|CollectedDigits=8675309
```

```
### Calling phone sends CUCM the ORC ACK

00019912.001 |12:48:36.139 |AppInfo  |StationInit: (0000005) OpenReceiveChannelAck Status=0, IpAddr=IpAddr.type:0 ipAddr:0x0e30201c000000000000000000000000(10.48.32.28), Port=31678, PartyID=33554433
```

```
### CUCM sends startMediaTransmission to the called (recorded) phone telling the phone to send RTP to the calling phone (10.48.32.28)

00019920.001 |12:48:36.139 |AppInfo  |StationD:    (0000007) startMediaTransmission conferenceID=49613638 passThruPartyID=33554434 remoteIpAddress=IpAddr.type:0 ipAddr:0x0e30201c000000000000000000000000(10.48.32.28) remotePortNumber=31678 milliSecondPacketSize=20 compressType=4(Media_Payload_G711Ulaw64k) RFC2833PayloadType=0 qualifierOut=?. myIP: IpAddr.type:0 ipv4Addr:0x0e302021(10.48.32.33)
```

```
### Called (recorded) phone sends CUCM the ORC ACK

00019959.001 |12:48:36.145 |AppInfo  |StationInit: (0000007) OpenReceiveChannelAck Status=0, IpAddr=IpAddr.type:0 ipAddr:0x0e302021000000000000000000000000(10.48.32.33), Port=28360, PartyID=33554434
```

```
### CUCM sends startMediaTransmission to the calling phone telling the phone to send RTP to the called phone (10.48.32.33)

00019977.001 |12:48:36.146 |AppInfo  |StationD:    (0000005) startMediaTransmission conferenceID=49613637 passThruPartyID=33554433 remoteIpAddress=IpAddr.type:0 ipAddr:0x0e302021000000000000000000000000(10.48.32.33) remotePortNumber=28360 milliSecondPacketSize=20 compressType=4(Media_Payload_G711Ulaw64k) RFC2833PayloadType=0 qualifierOut=?. myIP: IpAddr.type:0 ipv4Addr:0x0e30201c(10.48.32.28)
```

```
### BiB places second call to recording destination address (cn is calling number which is the BiB cn="b00223906001" and it is dialing the recordingdestination dd="8675309") Note that the BiB number stayed the same (b00223906001) and so did the recordingdestination number

00020002.001 |12:48:36.147 |AppInfo  |Digit Analysis: star_DaReq: daReq.partitionSearchSpace(), filteredPartitionSearchSpaceString(), partitionSearchSpaceString()
00020002.002 |12:48:36.147 |AppInfo  |Digit Analysis: star_DaReq: Matching Legacy Numeric, digits=8675309
00020002.003 |12:48:36.147 |AppInfo  |Digit Analysis: getDaRes data: daRes.ssType=[0] Intercept DAMR.sstype=[0], TPcount=[0], DAMR.NotifyCount=[0], DaRes.NotifyCount=[0]
00020002.004 |12:48:36.147 |AppInfo  |Digit Analysis: getDaRes - Remote Destination [8675309] isURI[0]
00020002.005 |12:48:36.147 |AppInfo  |CMUtility routeCallThroughCTIRD: no matching RemDestDynamic record exists for remdest [8675309]
00020002.006 |12:48:36.147 |AppInfo  |DbMobility: getMatchedRemDest starts: cnumber = 8675309
00020002.007 |12:48:36.147 |AppInfo  |DbMobility: getMatchedRemDest: full match case
00020002.008 |12:48:36.147 |AppInfo  |DbMobility SelectByDestination: no matching RemDestDynamic record exists for remdest [8675309]
00020002.009 |12:48:36.147 |AppInfo  |DbMobility: can't find remdest 8675309 in map
00020002.010 |12:48:36.147 |AppInfo  |Digit analysis: patternUsage=5
00020002.011 |12:48:36.147 |AppInfo  |Digit analysis: match(pi="1", fqcn="", cn="b00223906001",plv="5", pss="E911_PT:Phones_PT:EMERGENCY_PT:INTERNAL_PT:INFORMACAST_PT", TodFilteredPss="E911_PT:Phones_PT:EMERGENCY_PT:INTERNAL_PT:INFORMACAST_PT", dd="8675309",dac="1")
00020002.012 |12:48:36.147 |AppInfo  |Digit analysis: analysis results
00020002.013 |12:48:36.147 |AppInfo  ||PretransformCallingPartyNumber=b00223906001
|CallingPartyNumber=b00223906001
|DialingPartition=
|DialingPattern=8675309
|FullyQualifiedCalledPartyNumber=8675309
|DialingPatternRegularExpression=(8675309)
|DialingWhere=
|PatternType=Enterprise
|PotentialMatches=NoPotentialMatchesExist
|DialingSdlProcessId=(0,0,0)
|PretransformDigitString=8675309
|PretransformTagsList=SUBSCRIBER
|PretransformPositionalMatchList=8675309
|CollectedDigits=8675309
|UnconsumedDigits=
|TagsList=SUBSCRIBER
|PositionalMatchList=8675309
```

```
### CUCM sends INVITE #1 to configured recording server (10.48.32.170)

00020086.001 |12:48:36.156 |AppInfo  |//SIP/SIPUdp/wait_SdlSPISignal: Outgoing SIP UDP message to 10.48.32.170:[5060]:
[901,NET]
INVITE sip:8675309@10.48.32.170:5060 SIP/2.0
Via: SIP/2.0/UDP 10.48.32.90:5060;branch=z9hG4bK4f2a857d3d
From: <sip:9110001@10.48.32.90;x-nearend;x-refci=49613638;x-nearendclusterid=glenscucm10-5;x-nearenddevice=sep001795bdd16b;x-nearendaddr=9110001;x-farendrefci=49613637;x-farendclusterid=glenscucm10-5;x-farenddevice=sep0018195aa209;x-farendaddr=9110006>;tag=351~713e2333-4032-45f1-b1f5-e33cf471acec-49613642
To: <sip:8675309@10.48.32.170>
Date: Tue, 14 Oct 2014 16:48:36 GMT
Call-ID: ef7acf80-43d153e4-50-5a20300e@10.48.32.90
Supported: timer,resource-priority,replaces
Min-SE:  1800
User-Agent: Cisco-CUCM10.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence, kpml
Supported: X-cisco-srtp-fallback
Supported: Geolocation
Call-Info: ;method="NOTIFY;Event=telephone-event;Duration=500"
Cisco-Guid: 4017803136-0000065536-0000000001-1512058894
Session-Expires:  1800
P-Asserted-Identity: <sip:9110001@10.48.32.90>
Remote-Party-ID: <sip:9110001@10.48.32.90>;party=calling;screen=yes;privacy=off
Contact: <sip:9110001@10.48.32.90:5060>;isFocus
Max-Forwards: 70
Content-Length: 0
```

```
### CUCM sends INVITE #2 to configured recording server (10.48.32.170)

00020088.001 |12:48:36.157 |AppInfo  |//SIP/SIPUdp/wait_SdlSPISignal: Outgoing SIP UDP message to 10.48.32.170:[5060]:
[902,NET]
INVITE sip:8675309@10.48.32.170:5060 SIP/2.0
Via: SIP/2.0/UDP 10.48.32.90:5060;branch=z9hG4bK5014378d0b
From: <sip:9110001@10.48.32.90;x-farend;x-refci=49613638;x-nearendclusterid=glenscucm10-5;x-nearenddevice=sep001795bdd16b;x-nearendaddr=9110001;x-farendrefci=49613637;x-farendclusterid=glenscucm10-5;x-farenddevice=sep0018195aa209;x-farendaddr=9110006>;tag=352~713e2333-4032-45f1-b1f5-e33cf471acec-49613645
To: <sip:8675309@10.48.32.170>
Date: Tue, 14 Oct 2014 16:48:36 GMT
Call-ID: ef7acf80-43d153e4-51-5a20300e@10.48.32.90
Supported: timer,resource-priority,replaces
Min-SE:  1800
User-Agent: Cisco-CUCM10.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence, kpml
Supported: X-cisco-srtp-fallback
Supported: Geolocation
Call-Info: ;method="NOTIFY;Event=telephone-event;Duration=500"
Cisco-Guid: 4017803136-0000065536-0000000002-1512058894
Session-Expires:  1800
P-Asserted-Identity: <sip:9110001@10.48.32.90>
Remote-Party-ID: <sip:9110001@10.48.32.90>;party=calling;screen=yes;privacy=off
Contact: <sip:9110001@10.48.32.90:5060>;isFocus
Max-Forwards: 70
Content-Length: 0
```

```
### CUCM receives a 200 OK from recording server for INVITE #1

00020089.001 |12:48:36.161 |AppInfo  |//SIP/SIPUdp/wait_SdlDataInd: Incoming SIP UDP message size 731 from 10.48.32.170:[5060]:
[903,NET]
SIP/2.0 200 OK
Via: SIP/2.0/UDP 10.48.32.90:5060;branch=z9hG4bK4f2a857d3d
From: <sip:9110001@10.48.32.90;x-nearend;x-refci=49613638;x-nearendclusterid=glenscucm10-5;x-nearenddevice=sep001795bdd16b;x-nearendaddr=9110001;x-farendrefci=49613637;x-farendclusterid=glenscucm10-5;x-farenddevice=sep0018195aa209;x-farendaddr=9110006>;tag=351~713e2333-4032-45f1-b1f5-e33cf471acec-49613642
To: <sip:8675309@10.48.32.170>;tag=1
Call-ID: ef7acf80-43d153e4-50-5a20300e@10.48.32.90
CSeq: 101 INVITE
Contact: <sip:10.48.32.170:5060;transport=udp>
Content-Type: application/sdp
Content-Length:   135

v=0
o=user1 53655765 2353687637 IN IP4 10.48.32.170
s=-
c=IN IP4 10.48.32.170
t=0 0
m=audio 6000 RTP/AVP 0
a=rtpmap:0 PCMU/8000
```

```
### CUCM receives a 200 OK from recording server for INVITE #2

00020092.001 |12:48:36.161 |AppInfo  |//SIP/SIPUdp/wait_SdlDataInd: Incoming SIP UDP message size 730 from 10.48.32.170:[5060]:
[905,NET]
SIP/2.0 200 OK
Via: SIP/2.0/UDP 10.48.32.90:5060;branch=z9hG4bK5014378d0b
From: <sip:9110001@10.48.32.90;x-farend;x-refci=49613638;x-nearendclusterid=glenscucm10-5;x-nearenddevice=sep001795bdd16b;x-nearendaddr=9110001;x-farendrefci=49613637;x-farendclusterid=glenscucm10-5;x-farenddevice=sep0018195aa209;x-farendaddr=9110006>;tag=352~713e2333-4032-45f1-b1f5-e33cf471acec-49613645
To: <sip:8675309@10.48.32.170>;tag=2
Call-ID: ef7acf80-43d153e4-51-5a20300e@10.48.32.90
CSeq: 101 INVITE
Contact: <sip:10.48.32.170:5060;transport=udp>
Content-Type: application/sdp
Content-Length:   135

v=0
o=user1 53655765 2353687637 IN IP4 10.48.32.170
s=-
c=IN IP4 10.48.32.170
t=0 0
m=audio 6000 RTP/AVP 0
a=rtpmap:0 PCMU/8000
```

```
### Region information for connecting audio for recording call, both appear to support G.711. Note that the bandwidth capabilities printed is kbps=8 meaning the region relationship between the two regions is limitted to codecs using 8kbps or less.

00020160.005 |12:48:36.190 |AppInfo  |DET-RegionsServer::matchCapabilities-- savedOption=3, PREF_NONE, regionA=(null) regionB=(null) latentCaps(A=0, B=0) kbps=8, capACount=1, capBCount=1
00020160.006 |12:48:36.190 |AppInfo  |DET-MediaManager-(2)::checkAudioPassThru, param(bPostMTPAllocation=0,chkTrp=1), capCount(1,1), mtpPT=1, aPT=2
00020160.007 |12:48:36.190 |AppInfo  |DET-MediaManager-(2)::preCheckCapabilities, region1=Default , region2=RecordingTrunk , Pty1 capCount=1 (Cap,ptime)= (4,20) , Pty2 capCount=1 (Cap,ptime)= (4,20) 00020160.008 |12:48:36.190 |AppInfo  |DET-RegionsServer::matchCapabilities-- savedOption=0, PREF_NONE, regionA=(null) regionB=(null) latentCaps(A=0, B=0) kbps=8 , capACount=1, capBCount=1
```

```
### CUCM determines 2 transcoders are required and attempts to allocate

00020160.011 |12:48:36.190 |AppInfo  |DET-MediaManager-(2)::preCheckCapabilities, caps mismatch! Xcoder Reqd. kbps(8) , filtered A[capCount=0 (Cap,ptime)=], B[capCount=0 (Cap,ptime)=] allowMTP=0 numXcoderRequired=2 xcodingSide=0
```

```
### No transcoder is configured which can cause this call to fail

00020162.003 |12:48:36.190 |AppInfo  |MediaResourceManager::sendAllocationResourceErr - ERROR - no transcoder device configured
```

```
### CUCM sendt the ACK and BYE to the recording server in response to INVITE #1
Note the Q.850 cause code

00020210.001 |12:48:36.216 |AppInfo  |//SIP/SIPUdp/wait_SdlSPISignal: Outgoing SIP UDP message to 10.48.32.170:[5060]:
[906,NET]
ACK sip:10.48.32.170:5060;transport=UDP SIP/2.0
Via: SIP/2.0/UDP 10.48.32.90:5060;branch=z9hG4bK51257b2b47
From: <sip:9110001@10.48.32.90;x-nearend;x-refci=49613638;x-nearendclusterid=glenscucm10-5;x-nearenddevice=sep001795bdd16b;x-nearendaddr=9110001;x-farendrefci=49613637;x-farendclusterid=glenscucm10-5;x-farenddevice=sep0018195aa209;x-farendaddr=9110006>;tag=351~713e2333-4032-45f1-b1f5-e33cf471acec-49613642
To: <sip:8675309@10.48.32.170>;tag=1
Date: Tue, 14 Oct 2014 16:48:36 GMT
Call-ID: ef7acf80-43d153e4-50-5a20300e@10.48.32.90
User-Agent: Cisco-CUCM10.5
Max-Forwards: 70
CSeq: 101 ACK
Allow-Events: presence, kpml
Content-Length: 0 00020211.001 |12:48:36.216 |AppInfo |//SIP/SIPUdp/wait_SdlSPISignal: Outgoing SIP UDP message to 10.48.32.170:[5060]: [907,NET] BYE sip:10.48.32.170:5060;transport=UDP SIP/2.0 Via: SIP/2.0/UDP 10.48.32.90:5060;branch=z9hG4bK526f3d2afa From: <sip:9110001@10.48.32.90;x-nearend;x-refci=49613638;x-nearendclusterid=GlensCUCM10-5;x-nearenddevice=SEP001795BDD16B;x-nearendaddr=9110001;x-farendrefci=49613637;x-farendclusterid=GlensCUCM10-5;x-farenddevice=SEP0018195AA209;x-farendaddr=9110006>;tag=351~713e2333-4032-45f1-b1f5-e33cf471acec-49613642 To: <sip:8675309@10.48.32.170>;tag=1 Date: Tue, 14 Oct 2014 16:48:36 GMT Call-ID: ef7acf80-43d153e4-50-5a20300e@10.48.32.90 User-Agent: Cisco-CUCM10.5 Max-Forwards: 70 P-Asserted-Identity: <sip:9110001@10.48.32.90> CSeq: 102 BYE Reason: Q.850;cause=47 Content-Length: 0
```

```
### CUCM sendt the ACK and BYE to the recording server in response to INVITE #2
Note the Q.850 cuase code in the BYE

00020248.001 |12:48:36.218 |AppInfo  |//SIP/SIPUdp/wait_SdlSPISignal: Outgoing SIP UDP message to 10.48.32.170:[5060]:
[908,NET]
ACK sip:10.48.32.170:5060;transport=UDP SIP/2.0
Via: SIP/2.0/UDP 10.48.32.90:5060;branch=z9hG4bK531df920a6
From: <sip:9110001@10.48.32.90;x-farend;x-refci=49613638;x-nearendclusterid=glenscucm10-5;x-nearenddevice=sep001795bdd16b;x-nearendaddr=9110001;x-farendrefci=49613637;x-farendclusterid=glenscucm10-5;x-farenddevice=sep0018195aa209;x-farendaddr=9110006>;tag=352~713e2333-4032-45f1-b1f5-e33cf471acec-49613645
To: <sip:8675309@10.48.32.170>;tag=2
Date: Tue, 14 Oct 2014 16:48:36 GMT
Call-ID: ef7acf80-43d153e4-51-5a20300e@10.48.32.90
User-Agent: Cisco-CUCM10.5
Max-Forwards: 70
CSeq: 101 ACK
Allow-Events: presence, kpml
Content-Length: 0 00020249.001 |12:48:36.218 |AppInfo  |//SIP/SIPUdp/wait_SdlSPISignal: Outgoing SIP UDP message to 10.48.32.170:[5060]:
[909,NET]
BYE sip:10.48.32.170:5060;transport=UDP SIP/2.0
Via: SIP/2.0/UDP 10.48.32.90:5060;branch=z9hG4bK5462aba807
From: <sip:9110001@10.48.32.90;x-farend;x-refci=49613638;x-nearendclusterid=glenscucm10-5;x-nearenddevice=sep001795bdd16b;x-nearendaddr=9110001;x-farendrefci=49613637;x-farendclusterid=glenscucm10-5;x-farenddevice=sep0018195aa209;x-farendaddr=9110006>;tag=352~713e2333-4032-45f1-b1f5-e33cf471acec-49613645
To: <sip:8675309@10.48.32.170>;tag=2
Date: Tue, 14 Oct 2014 16:48:36 GMT
Call-ID: ef7acf80-43d153e4-51-5a20300e@10.48.32.90
User-Agent: Cisco-CUCM10.5
Max-Forwards: 70
P-Asserted-Identity: <sip:9110001@10.48.32.90>
CSeq: 102 BYE Reason: Q.850;cause=47 Content-Length: 0
```

### Misconfiguration which Includes CSS and PT Issues

The commands here allow the majority of the recording configurations to be reviewed quickly with only the known MAC address of a phone that is not recording calls. Simply replace the part of the command MAC_of_Phone with the actual MAC address of the phone as in the examples seen here.

This gives you the DN (all of them if there is more than one) for the MAC you search on, the MAC of the phone just for confirmation, the BIB setting, the privacy setting, the recording type (reference the values listed in the examples from the lab), the recording profile in use by the phone, the name of the recording Call Search Spaces (CSS), the recording destination for that recording profile, and the partition that recording destination is associated with based on the MAC you search on:

```
run sql select n1.dnorpattern as phone_dn, dev.name as phone_mac, CASE dev.tkstatus_builtinbridge WHEN '1' THEN 'BiB is on' WHEN '0' THEN 'BiB is off' ELSE 'NA' END as is_bib_on, CASE dev.resettoggle WHEN 't' THEN 'Privacy is on' WHEN 'f' THEN 'Privacy is off' ELSE 'NA' END as is_privacy_on, CASE recordynam.tkrecordingflag WHEN '0' THEN 'Recording Disabled' WHEN '1' THEN 'Automatic' WHEN '2' THEN 'Selective' ELSE 'NA' END as recording_type, CASE devnumplanmap.tkpreferredmediasource WHEN '1' THEN 'Gateway Preferred' WHEN '2' THEN 'Phone Preferred' ELSE 'NA' END as Recording_Media_Source, rcrdpro.name as recording_profile_name, css.name as css_used_by_recording_profile, rcrdpro.recorderdestination as recording_route_pattern, rp.name as required_partition_for_css_used_by_recording_profile from recordingprofile as rcrdpro inner join callingsearchspace as css on rcrdpro.fkcallingsearchspace_callrecording = css.pkid inner join numplan as n on n.dnorpattern = rcrdpro.recorderdestination inner join routepartition as rp on rp.pkid = n.fkroutepartition inner join devicenumplanmap as devnumplanmap on rcrdpro.pkid = devnumplanmap.fkrecordingprofile inner join recordingdynamic as recordynam on devnumplanmap.pkid = recordynam.fkdevicenumplanmap inner join device as dev on devnumplanmap.fkdevice = dev.pkid inner join numplan as n1 on devnumplanmap.fknumplan = n1.pkid where css.pkid = rcrdpro.fkcallingsearchspace_callrecording and dev.name='MAC_of_Phone'
```

This gives you the list of partitions that are associated with the recording CSS on the recording profile that is associated with the MAC of the phone you search against.

```
run sql select css.name as name_of_the_recording_css, rp.name as partitions_in_recording_css, csm.sortorder from callingsearchspace as css inner join callingsearchspacemember as csm on csm.fkcallingsearchspace = css.pkid inner join routepartition as rp on csm.fkroutepartition = rp.pkid inner join recordingprofile as rcrdpro on rcrdpro.fkcallingsearchspace_callrecording = css.pkid inner join devicenumplanmap as devnumplanmap on rcrdpro.pkid = devnumplanmap.fkrecordingprofile inner join device as dev on devnumplanmap.fkdevice = dev.pkid where css.pkid = rcrdpro.fkcallingsearchspace_callrecording and dev.name='MAC_of_Phone'
```

Here are examples of the output from the lab for a phone with MAC address SEPC80084AA8743:

In this command, you can see the phone has only one DN on it which is 2003, we also see the BIB is On, privacy is Off, the recording type is automatic, the preferred source is phone, the recording profile is Test Recording Profile, the recording calling search space is INTERNAL_CSS, the route pattern for recorded calls is 8675309 and that pattern is associated with the partition INTERNAL_PT.

```
run sql select n1.dnorpattern as phone_dn, dev.name as phone_mac, CASE dev.tkstatus_builtinbridge WHEN '1' THEN 'BiB is on' WHEN '0' THEN 'BiB is off' ELSE 'NA' END as is_bib_on, CASE dev.resettoggle WHEN 't' THEN 'Privacy is on' WHEN 'f' THEN 'Privacy is off' ELSE 'NA' END as is_privacy_on, CASE recordynam.tkrecordingflag WHEN '0' THEN 'Recording Disabled' WHEN '1' THEN 'Automatic' WHEN '2' THEN 'Selective' ELSE 'NA' END as recording_type, CASE devnumplanmap.tkpreferredmediasource WHEN '1' THEN 'Gateway Preferred' WHEN '2' THEN 'Phone Preferred' ELSE 'NA' END as Recording_Media_Source, rcrdpro.name as recording_profile_name, css.name as css_used_by_recording_profile, rcrdpro.recorderdestination as recording_route_pattern, rp.name as required_partition_for_css_used_by_recording_profile from recordingprofile as rcrdpro inner join callingsearchspace as css on rcrdpro.fkcallingsearchspace_callrecording = css.pkid inner join numplan as n on n.dnorpattern = rcrdpro.recorderdestination inner join routepartition as rp on rp.pkid = n.fkroutepartition inner join devicenumplanmap as devnumplanmap on rcrdpro.pkid = devnumplanmap.fkrecordingprofile inner join recordingdynamic as recordynam on devnumplanmap.pkid = recordynam.fkdevicenumplanmap inner join device as dev on devnumplanmap.fkdevice = dev.pkid inner join numplan as n1 on devnumplanmap.fknumplan = n1.pkid where css.pkid = rcrdpro.fkcallingsearchspace_callrecording and dev.name='SEPC80084AA8743' phone_dn phone_mac       is_bib_on  is_privacy_on  recording_type     recording_media_source recording_profile_name css_used_by_recording_profile recording_route_pattern required_partition_for_css_used_by_recording_profile ======== =============== ========== ============== ================== ====================== ====================== ============================= ======================= ==================================================== 2003     SEPC80084AA8743 BiB is on  Privacy is off Automatic          Phone Preferred        Test Recording Profile INTERNAL_CSS                  8675309                 INTERNAL_PT
```

With the output of this command, you can check all the partitions of the recording CSS and of the recording profile associated with the phone of interest. You can see here that the partition INTERNAL_PT is one of the partitions associated with the calling search space INTERNAL_CSS. This means there must be no issues with the BIB of the phone that is able to call the recording route pattern.

```
run sql select css.name as name_of_the_recording_css, rp.name as partitions_in_recording_css, csm.sortorder from callingsearchspace as css inner join callingsearchspacemember as csm on csm.fkcallingsearchspace = css.pkid inner join routepartition as rp on csm.fkroutepartition = rp.pkid inner join recordingprofile as rcrdpro on rcrdpro.fkcallingsearchspace_callrecording = css.pkid inner join devicenumplanmap as devnumplanmap on rcrdpro.pkid = devnumplanmap.fkrecordingprofile inner join device as dev on devnumplanmap.fkdevice = dev.pkid where css.pkid = rcrdpro.fkcallingsearchspace_callrecording and dev.name=' SEPC80084AA8743 '
name_of_the_recording_css partitions_in_recording_css sortorder
========================= =========================== =========
INTERNAL_CSS              E911_PT                     1
INTERNAL_CSS              Phones_PT                   2
INTERNAL_CSS              EMERGENCY_PT                3 INTERNAL_CSS              INTERNAL_PT 4
INTERNAL_CSS              INFORMACAST_PT              5
```

## Related Information

- Cisco Collaboration System 11.x Solution Reference Network Designs (SRND)

### Revision History

4.0

20-Aug-2026

Recertification

3.0

18-Jan-2024

Updated SEO and Formatting.

2.0

05-Dec-2022

Removed PII.
Updated Alt Text, Introduction, machine translation, style requirements, gerunds and fomatting.

1.0

31-Oct-2016

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 4.0 | 20-Aug-2026 | Recertification |
| 3.0 | 18-Jan-2024 | Updated SEO and Formatting. |
| 2.0 | 05-Dec-2022 | Removed PII.
Updated Alt Text, Introduction, machine translation, style requirements, gerunds and fomatting. |
| 1.0 | 31-Oct-2016 | Initial Release |