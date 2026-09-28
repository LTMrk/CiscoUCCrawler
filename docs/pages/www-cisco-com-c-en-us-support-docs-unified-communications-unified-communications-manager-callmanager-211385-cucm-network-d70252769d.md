---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-211385-cucm-network-d70252769d
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/211385-CUCM-Network-based-recording-for-mobile.html
retrieved_at: 2026-08-21T13:55:59.653711+00:00
---

CUCM Network based Recording for Mobile Agents

# CUCM Network based Recording for Mobile Agents

### Download Options

Updated: April 9, 2018

Document ID: 211385

Contents

## Contents

## Introduction

This document describes Network Based Recording’s (NBR) different scenarios and it's troubleshoot.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communications Manager (CUCM) version 10.0(1) or later

- Phone-based recording architecture

- Network based recording architecture

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Call Manager version 10.5

- Customer Voice Portal ( CVP ) version 10.5

- Cisco Unified Contact Center Express (UCCE ) 10.5(2)

- Gateway 3925E 15.3(3)M

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

Network based recording is available as of CUCM, Release 10.0(1) and allows you to use the gateway to record calls.

The feature allows to record calls regardless of device, location, or geography such as calls extended off-network to mobile and home office phones. It automatically selects the right media source based on call flow and call participants.

It is important to understand that:

- SIP signalization is from CUCM to CUBE and from CUCM to the recording server.

- There is no direct SIP signaling between the recording server and CUBE.

- CUBE is responsible for forking the RTP stream to the recording server.

- The recorded endpoint on CUCM does not need to support Built in Bridge (BiB).

CUCM uses HTTP to initiate the call recording request to the Cisco Unified Communications (UC) Services API on CUBE. The Cisco Unified Communications (UC) Services API provides a unified web service interface for the different services in IOS gateway. One of those services is the Extended Media Forking (XMF) provider that allows applications to monitor calls and trigger media forking on Real-time Transport Protocol (RTP) and Secure RTP calls.

### How Mobile Agents Work

- Caller A on Communication manager express (CME) dials B, which points to Gateway (GW). GW dial peer points to Customer Voice Portal (CVP).

- CVP sends a route request to Intelligent Contact Manager (ICM), and ICM returns the Mobile Agent label, which is Local CTI port (LCP port ) Dialed Number (DN).

- CVP sends invite to CUCM. While the LCP port rings, the JTAPI Gateway (JGW) instructs CUCM to call agent phone from Remote CTI port (RCP ) DN .

- Once the agent answers, the agent leg is connected to Music-on-Hold (MoH).

- JGW instructs CUCM to answer the inbound call that rings on the LCP port.

- Once the LCP leg is connected, JGW instructs CUCM to retrieve the agent leg.

- JGW passes on the Real-Time Transport Protocol (RTP) IP address/port details from the customer leg to the agent leg and vice versa.

- CUCM bridges the two legs and establishes the RTP path between the agent and the customer.

### How Recording Works in Case of Mobile Agent

- In case of Mobile Agents, recording can be enabled either on LCP Port or RCP port.

- Once call is connected on LCP or RCP and recording is enabled , CUCM sends 2 Invite to recording Server for near end and far end device.

- Once signaling is completed for the near end device and the far end Device SDL HTTP request is sent to the gateway to instruct it to Start recording.

Note : There can be scenarios where CUCM does not have a direct SIP trunk with Gateway or with CVP

Note : For instance, CUCM can have a SIP Trunk with a Proxy server ( CUSP ) controlling all the traffic flow

Note : If recording is enabled on CTI port and call is landing on that port, Recording will work.

Note : In case of mobile agents, CTI ports do facilitate signaling and then are out of the RTP flow. It is the end points between which RTP will flow. But LCP and RCP port never go out of the signaling. Their Ci ‘s are never destroyed till the end of the call. This is the reason recording is successful on LCP or RCP port even if the RTP does not flow through them

### UCCE Deployment  With CUSP ( Proxy Server )

With UCCE deployed with CVP and CUSP with the so-called comprehensive model, there are no SIP trunks between CUCM and the CUBE(s). All communication between CUBE and CUCM goes via a single SIP trunk to CUSP.

CUCM needs a way to know from which CUBE the call is coming, so that it knows where to send the recording requests. This is achieved by sending the request back to the destination IP of the incoming SIP trunk that was used for the call. However, if CUCM sends the API request back to CUSP nothing will happen. To work around this limitation in environments with CUSP, the following CUCM configuration needs to be implemented:

- Create dummy SIP trunks to each CUBE. This trunks will not be used to route any calls!

- Re-classify the incoming calls on the CUSP SIP trunk to the correct dummy CUBE trunk using the Call-Info header.

Note : This setting does not affect any call processing decisions - all call processing and call class of service decisions will be done as if the call is still on the CUSP SIP trunk and no SIP messages will be sent to the destination of the newly matched trunk.

Note : The x-cisco-origIP value in the incoming INVITE must match the destination IP address a dummy trunk.

Note : To have a correct value for the x-cisco-origIP header, it must be correctly set on the originating CUBE. Setting the value can be achieved by adding the header on the CUBE, but also by adding it on CVP. The UCCE Direct agent script already uses on the Call-Info header. Therefore, a second Call-Info header with the required  x-cisco-origIP will be added after the Call-Info header for the Direct agent script. Tests showed that CUCM will still do the required re-classification when the x-cisco-origIP is contained in the second Call-Info header of the SIP INVITE.

## Configuration

Key Configuration Points for UCCE deployment with CUSP :

### Create a SIP Trunk Device for a Recorder

To provision a recorder as a SIP trunk device, a Unified CM administrator creates a SIP trunk device from the device page, and enters the device name and the IP address of the recorder in the Destination Address field.

### Create Call Recording Profiles

To provision line appearances of agents for call recording, one or more call recording profiles should be created. A recording profile is then be selected for a line appearance. To create a recording profile, a Unified CM administrator opens Device Setting page and select Call Recording Profile. In the Recording Destination Address field, the administrator enters the DN or the URL of the recorder. In the Recording Calling Search Space field, the administrator enters the partition of the SIP trunk configured for the recorder.

### Provision a Dummy SIP Trunks to each CUBE

For each gateway that needs to fork calls to the recording server a dedicated dummy trunk on CUCM must be configured. Remember that this trunk is not used for any real SIP signaling and does not influence any call decisions. The important things to configure are :

- This trunk connects to a recording-enabled gateway.

- The destination IP must be the same on which the CUBE is configured to listen in its XMF configuration

### Provision Route Pattern for the Recorder

To provision the route pattern for the recorder, the administrator opens the route pattern configuration page and enters a route pattern based on the recorder DN. The administrator selects the SIP Trunk device for the recorder, and then saves the route pattern. If the recorder address is given as a SIP URL and the RHS of the URL does not belong to Unified CM cluster, a SIP route pattern should be configured. The pattern field should be the domain or ip address of the recorder (the RHS part of the recorder URL) and the SIP Trunk field should be the SIP trunk for the recorder.

### Provision Recording Calling Notification Tone Option

To provision the cluster wide service parameter for Recording Notification Tone, the administrator opens the Unified CM Administration’s Service Parameter page and locates the entry for Play Recording Notification Tone to Observed Target . The administrator enters Yes or No . The administrator then locates the entry for Play Recording Notification Tone to Observed Connected Target . The administrator enters Yes or No .

### Provision the CUBE XMF Provider

These configuration enables the HTTP communication and the XMF provider configuration :

CUBE001 :

ip http server no ip http secure-server ip http max-connections 1000 ip http timeout-policy idle 600 life 86400 requests 86400 ip http client source-interface Port-channel20.307 uc wsapi message-exchange max-failures 2 source-address 10.106.230.20 probing interval keepalive 5 probing max-failures 5 ! provider xmf remote-url 1 http://10.106.97.140:8090/ucm_xmf remote-url 2 http://10.106.97.141:8090/ucm_xmf remote-url 3 http://10.106.97.143:8090/ucm_xmf remote-url 4 http://10.106.97.144:8090/ucm_xmf

CUBE002:

ip http server no ip http secure-server ip http max-connections 1000 ip http timeout-policy idle 600 life 86400 requests 86400 ip http client source-interface Port-channel20.307 uc wsapi message-exchange max-failures 2 source-address 10.106.230.20 probing interval keepalive 5 probing max-failures 5 ! provider xmf remote-url 1 http://10.106.97.140:8090/ucm_xmf remote-url 2 http://10.106.97.141:8090/ucm_xmf remote-url 3 http://10.106.97.143:8090/ucm_xmf remote-url 4 http://10.106.97.144:8090/ucm_xmf

### Provision the CUBE SIP Profiles for Call-Info Header

In order to have a correct value for the x-cisco-origIP header care must be taken to set it correctly on the originating CUBE. Setting the value can be achieved in multiple ways and also it is not necessary to be done on the CUBE, for example, it can also be set on CVP. This is an example SIP profile that statically sets the x-cisco-origIP value in  the outgoing INVITE from CUBE to CUSP.

--- voice class sip-profiles 666 request INVITE sip-header Call-Info add "Call-Info: <sip:10.106.242.27>;PURPOSE=x-cisco-origIP" ---

If the UCCE system already relies on the Call-Info header, then a second Call-Info header with the required xcisco- origIP. Tests showed that CUCM will still do the required re classification when the x-cisco-origIP is contained in the second Call-Info header of the SIP INVITE. The same tests showed that the other systems however stop working if the new Call-Info header is put first. That profile needs to be applied to the outbound dial-peers that point to CUSP.

For detailed Configuration, refer to this link :

## Troubleshooting

### Log analysis

#### Incoming Invite from Customer Voice Portal (CVP)

```
01382866.006 |12:52:49.858 |AppInfo |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.106.97.135 on port 53696 index 65 with 1695 bytes:
[105066,NET]
INVITE sip:9876@eu91.voip.test SIP/2.0
Via: SIP/2.0/TCP 10.106.97.135:5060;branch=z9hG4bKc7z5eWQrKkRtP5FKnbAb6w~~780271
Via: SIP/2.0/TCP 10.106.97.136:5062;branch=z9hG4bKhYyfmvtY8.fM7CSyQd9K4Q~~48611
Max-Forwards: 63
Record-Route: <sip:rr$n=cvp@10.106.97.135:5060;transport=tcp;lr>
To: <sip:9876@CVP001.eu91.lab.test;transport=tcp>
From: +1234567890 <sip:+1234567890@10.106.97.136:5062>;tag=dsf816dd0c
Contact: <sip:+1234567890@10.106.97.136:5062;transport=tcp>
Expires: 60
Diversion: <sip:+123459876@10.106.97.137>;reason=unconditional;screen=yes;privacy=off
Call-ID: 694646BC1D2311E7A8D2826ACB31D85A-149182876973312598@10.106.97.136
CSeq: 1 INVITE
Content-Length: 250
User-Agent: CVP 10.5 (1) ES-18 Build-36
Date: Mon, 10 Apr 2017 12:52:38 GMT
Min-SE: 1800
Cisco-Guid: 1766213308-0488837607-2832368234-3409041498
Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER
Allow-Events: telephone-event
P-Asserted-Identity: <sip:+1234567890@10.106.97.138>
Session-Expires: 1800
Content-Disposition: session;handling=required
History-Info: <sip:\u95>
History-Info: <sip:\u95>
Call-Info: <sip:10.106.97.138>;purpose=x-cisco-origIP
Cisco-Gucid: 694646BC1D2311E7A8D2826ACB31D85A
Supported: timer
Supported: resource-priority
Supported: replaces
Supported: sdp-anat
Content-Type: application/sdp
App-Info: <10.106.97.136:8000:8443>

v=0
o=CiscoSystemsSIP-GW-UserAgent 2790 2026 IN IP4 10.106.97.138
s=SIP Call
c=IN IP4 10.106.242.1
t=0 0
m=audio 16552 RTP/AVP 8 101
c=IN IP4 10.106.242.1
a=rtpmap:8 PCMA/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=ptime:20
```

#### Digit Analysis for the Incoming Call

```
01382890.009 |12:52:49.861 |AppInfo ||PretransformCallingPartyNumber=+1234567890
|CallingPartyNumber=+1234567890
|DialingPartition=SYS-DN-PlainE164-PT
|DialingPattern=9876
|FullyQualifiedCalledPartyNumber=9876
|DialingPatternRegularExpression=(9876)
|DialingWhere=
```

#### Call Identifier ( CI ) Association for Calling no and Local CTI Port (LCP)

```
01382897.001 |12:52:49.862 |AppInfo  |LBMIF: CI: 43358624 ASSOC    43358625
01382897.002 |12:52:49.862 |AppInfo  |LBMIF: CI: 43358625 ASSOC'   43358624
```

#### LCP is Selected

```
01382902.001 |12:52:49.862 |AppInfo  |LineCdpc(135): -dispatchToAllDevices-, sigName=CcSetupReq, device=LCP_47483708
01382905.002 |12:52:49.862 |AppInfo  |StationCdpc(59): StationCtiCdpc-CtiEnableReq CH=0|0 DevName=LCP_47483708 DN=442086180755 Lock=0 FId=0 Side=0 LineFilter=1111111011011111111111010011111111111101110111111 for DN=442086180755
```

#### 180 Ringing Sent to CVP

```
01382949.001 |12:52:49.865 |AppInfo |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.106.97.135 on port 53696 index 65
[105068,NET]
SIP/2.0 180 Ringing
Via: SIP/2.0/TCP 10.106.97.135:5060;branch=z9hG4bKc7z5eWQrKkRtP5FKnbAb6w~~780271,SIP/2.0/TCP 10.106.97.136:5062;branch=z9hG4bKhYyfmvtY8.fM7CSyQd9K4Q~~48611
From: +1234567890 <sip:+1234567890@10.106.97.136:5062>;tag=dsf816dd0c
To: <sip:9876@CVP001.eu91.lab.test;transport=tcp>;tag=46359~8c66ebf6-153f-456b-a6e8-0bf5f687ce1f-43358624
Date: Mon, 10 Apr 2017 12:52:49 GMT
Call-ID: 694646BC1D2311E7A8D2826ACB31D85A-149182876973312598@10.106.97.136
CSeq: 1 INVITE
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
Allow-Events: presence
Record-Route: <sip:rr$n=cvp@10.106.97.135:5060;transport=tcp;lr>
Server: Cisco-CUCM10.5
Supported: X-cisco-srtp-fallback
Supported: Geolocation
P-Asserted-Identity: <sip:9876@10.107.28.14>
Remote-Party-ID: <sip:9876@10.107.28.14>;party=called;screen=yes;privacy=off
Contact: <sip:9876@10.107.28.14:5060;transport=tcp>
Content-Length: 0
```

#### RCP Extends Call to the Called Number

LCP and the Calling Number Rings and Remote CTI Port (RCP) Extends call to called number i.e., the agent.

```
01382957.000 |12:52:49.882 |SdlSig   |CtiEnableReq                           |null0                          |StationCdpc(2,100,64,60)         |StationD(2,100,63,245)           |2,200,13,85.12075^10.241.240.197^RCP_47483708 |[R:N-H:0,N:4,L:0,V:0,Z:0,D:0]  mDataCount=1 LH=2|431 mbMore=T bConsultWithoutMedia=F mediaTerm=2
01382957.001 |12:52:49.882 |AppInfo  |StationCdpc(2,100,64,60): StationCtiCdpc::StationCtiCdpc
01382957.002 |12:52:49.882 |AppInfo  |StationCdpc(60): StationCtiCdpc-CtiEnableReq CH=0|0 DevName=RCP_47483708 DN=442086180755 Lock=0 FId=0 Side=0 LineFilter=1111111011011111111111010011111111111101110111111 for DN=442086180755
01382958.000 |12:52:49.882 |SdlSig   |StationOutputSetRinger                 |restart0                       |StationD(2,100,63,245)           |StationD(2,100,63,245)           |2,200,13,85.12075^10.241.240.197^RCP_47483708 |[R:N-H:0,N:3,L:0,V:0,Z:0,D:0] Mode=RingOff Duration=Normal Line=0 CI=0
01382958.001 |12:52:49.882 |AppInfo  |StationD:    (0000245) SetRinger ringMode=1(RingOff).
```

#### DIgit Analysis  for RCP Calling Agent

```
01383005.013 |12:52:49.885 |AppInfo ||PretransformCallingPartyNumber=9876
|CallingPartyNumber=9876
|DialingPartition=TE-PSTNInternational-PT
|DialingPattern=+.[1-9]!
|FullyQualifiedCalledPartyNumber=+1122334455
|DialingPatternRegularExpression=(+)([1-9][0-9]+)
```

#### Call Identifier (CI) Association for RCP and the Agent

```
01383012.001 |12:52:49.885 |AppInfo  |LBMIF: CI: 43358626 ASSOC    43358627
01383012.002 |12:52:49.885 |AppInfo  |LBMIF: CI: 43358627 ASSOC'   43358626
```

#### Invite is Sent out for Agent:

```
01383048.001 |12:52:49.888 |AppInfo |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.241.242.99 on port 5060 index 55
[105069,NET]
INVITE sip:1122334455@10.106.22.199:5060 SIP/2.0
Via: SIP/2.0/TCP 10.107.28.14:5060;branch=z9hG4bK6b0870d07a53
From: <sip:9876@10.107.28.14>;tag=46360~8c66ebf6-153f-456b-a6e8-0bf5f687ce1f-43358627
To: <sip:1122334455@10.106.22.199>
Date: Mon, 10 Apr 2017 12:52:49 GMT
Call-ID: 98b4ac00-8eb18021-67f3-c2e4110a@10.107.28.14
Supported: timer,resource-priority,replaces
Min-SE: 1800
User-Agent: Cisco-CUCM10.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence, kpml
Supported: X-cisco-srtp-fallback,X-cisco-original-called
Call-Info: <sip:10.107.28.14:5060>;method="NOTIFY;Event=telephone-event;Duration=500"
Call-Info: <urn:x-cisco-remotecc:callinfo>;x-cisco-video-traffic-class=VIDEO_UNSPECIFIED
Cisco-Guid: 2561977344-0000065536-0000000138-3269726474
Session-Expires: 1800
P-Asserted-Identity: <sip:9876@10.107.28.14>
Remote-Party-ID: <sip:9876@10.107.28.14>;party=calling;screen=yes;privacy=off
Contact: <sip:9876@10.107.28.14:5060;transport=tcp>;DeviceName="RCP_47483708"
Max-Forwards: 70
Content-Length: 0
 
 
 
01383182.002 |12:53:00.624 |AppInfo |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.106.22.199 on port 5060 index 55 with 1204 bytes:
[105079,NET]
SIP/2.0 200 OK
Via: SIP/2.0/TCP 10.107.28.14:5060;branch=z9hG4bK6b0870d07a53
Record-Route: <sip:rr$n=cube-pool-int@10.106.22.199:5060;transport=tcp;lr>
To: <sip:1122334455@10.106.22.199>;tag=AD1038-15B8
From: <sip:9876@10.107.28.14>;tag=46360~8c66ebf6-153f-456b-a6e8-0bf5f687ce1f-43358627
Contact: <sip:1122334455@10.106.97.138:5060;transport=tcp>
Require: timer
Remote-Party-ID: <sip:+1122334455@10.106.97.138>;party=called;screen=no;privacy=off
Call-ID: 98b4ac00-8eb18021-67f3-c2e4110a@10.107.28.14
CSeq: 101 INVITE
Content-Length: 250
Date: Mon, 10 Apr 2017 12:52:49 GMT
Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER
Allow-Events: telephone-event
Supported: replaces
Supported: sdp-anat
Supported: timer
Server: Cisco-SIPGateway/IOS-15.4.3.M5
Session-Expires: 1800;refresher=uac
Content-Type: application/sdp
Content-Disposition: session;handling=required

v=0
o=CiscoSystemsSIP-GW-UserAgent 6311 9012 IN IP4 10.106.97.138
s=SIP Call
c=IN IP4 10.106.242.1
t=0 0
m=audio 16554 RTP/AVP 8 101
c=IN IP4 10.106.242.1
a=rtpmap:8 PCMA/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=ptime:20
```

#### RCP goes on Hold and LCP and Calling Party is Connected

```
01383470.004 |12:53:00.650 |AppInfo |StationD: (0000388) INFO- sendSignalNow, sigName=StationOffHook, cdpc=59
01383471.000 |12:53:00.651 |SdlSig-O |CtiLineCallAnswerRes |NA RemoteSignal |UnknownProcessName(2,200,25,1) |StationD(2,100,63,388) |2,200,13,85.12078^10.241.240.197^LCP_47483708 |[R:N-H:0,N:3,L:1,V:0,Z:0,D:0] AsyncResponse=29664 mResult=0x0
01383472.000 |12:53:00.651 |SdlSig |StationOutputSetRinger |restart0 |StationD(2,100,63,388) |StationD(2,100,63,388) |2,200,13,85.12078^10.241.240.197^LCP_47483708 |[R:N-H:0,N:2,L:1,V:0,Z:0,D:0] Mode=RingOff Duration=Normal Line=0 CI=0
01383472.001 |12:53:00.651 |AppInfo |StationD: (0000388) SetRinger ringMode=1(RingOff).
```

#### Media Connect Request for Calling Party and LCP

```
01383497.001 |12:53:00.651 |AppInfo  |ARBTRY-ConnectionManager-wait_MediaConnectRequest(43358624,43358625)
01383497.002 |12:53:00.651 |AppInfo  |ARBTRY-ConnectionManager- storeMediaInfo(CI=43358624): ADD NEW ENTRY, size=3
01383497.003 |12:53:00.651 |AppInfo  |ARBTRY-ConnectionManager- storeMediaInfo(CI=43358625): ADD NEW ENTRY, size=4
```

#### Media Termination Point (MTP)  is Allocated for LCP and Calling Party

```
01383508.002 |12:53:00.652 |AppInfo  |MediaResourceCdpc(185)::waiting_MrmAllocateMtpResourceReq - CI=43358630 Count=1 TryPassThru=1
```

#### Recording is enabled on LCP Port

```
01383607.002 |12:53:00.655 |AppInfo | StationCdpc: startRecordingIfNeeded - Device LCP_47483708, startedByCti=0, RecordingType=1. Cannot start -- not in active state yet. haveCodec=1, inActiveStat=0

01383614.016 |12:53:00.655 |AppInfo | StationCdpc: startRecordingIfNeeded - Device LCP_47483708, locking codec, codecType=2
01383614.017 |12:53:00.655 |AppInfo | StationCdpc: star_MediaExchangeAgenaQueryCapability - Device LCP_47483708, codec locked due to recording, codecType=2
01383614.018 |12:53:00.655 |AppInfo | StationCdpc: startRecordingIfNeeded - Device LCP_47483708, startedByCti=0, RecordingType=1. haveCodec=1, inActiveStat=1
01383614.019 |12:53:00.655 |AppInfo |StatiopnCdpc::StartRecordingIfNeeded DeviceName =LCP_47483708 RecordinngMethod =1
01383614.020 |12:53:00.655 |AppInfo | StationCdpc: startRecordingIfNeeded - Device LCP_47483708. FinalToneDir=3, initial=3, svc:ToObserved=0, svc:toConnected=0 recorderDestination=123456789
```

#### Siganling for  Recording Initiates

```
01383640.003 |12:53:00.657 |AppInfo |RecordManager::- await_SsDataInd lParties=(43358624,43358625)
01383641.000 |12:53:00.657 |SdlSig |SsDataInd |await_recordingFeatureData |Recording(2,100,100,77) |RecordManager(2,100,101,1) |2,200,13,85.12078^10.241.240.197^LCP_47483708 |[R:N-H:0,N:0,L:1,V:0,Z:0,D:0] SsType=33554461 SsKey=0 SsNode=2 SsParty=43358625 DevId=(0,0,0) BCC=9 OtherParty=43358624 NodeOtherParty=2 clearType = 0 CSS=587b40f7-bead-433d-9ddf-a99ca36b0753 CNumInfo = 0 CNameInfo = 0 ssDevType=4 ssOtherDevType=8 FDataType=16opId=-2147483643ssType=0 SsKey=0invokeId=0resultExp=Fbpda=F ssCause = 0 ssUserState = 2 ssOtherUserState = 2 PL=5 PLDmn=0 networkDomain= delayAPTimer=F geolocInfo={geolocPkid=, filterPkid=, geolocVal=, devType=4} cfwdTimerAction=0 matchInterceptPartition= matchInterceptPattern=
01383641.001 |12:53:00.657 |AppInfo |Recording::- (0000077) -await_recordingFeatureData_SsDataInd: mRecordingMethod=[1]
01383641.002 |12:53:00.657 |AppInfo |Recording::- (0000077) -await_recordingFeatureData_SsDataInd: Trigger started. mRecordingMethod=[1]

01383645.001 |12:53:00.657 |AppInfo |Recording::- (0000077) -processGWPreferred ....
01383645.002 |12:53:00.657 |AppInfo |Recording::- (0000077) -getRecordingAnchorMode: PeerBib=[1];peerCMDevType=[8];qSigApduSupported=[0]
01383645.003 |12:53:00.657 |AppInfo |Recording::- (0000077) -processGWPreferred: GW Recording - sideABibEnabled=[1]
```

#### Digit Analysis for Built in Bridge (Bib)

```
1383671.008 |12:53:00.658 |AppInfo ||PretransformCallingPartyNumber=
|CallingPartyNumber=
|DialingPartition=
|DialingPattern=b0026901001
|FullyQualifiedCalledPartyNumber=b0026901001
|DialingPatternRegularExpression=(b0026901001)
```

#### Here SIPBIB creates SIPBIBCDPC Process for Recording

```
01383681.000 |12:53:00.658 |SdlSig |CcSetupReq |restart0 |SIPvBIB(2,100,69,1) |Cdcc(2,100,219,295) 
01383681.001 |12:53:00.658 |AppInfo |SIPvBIB::restart0_CcSetupReq: primCallCi=43358624 primCallBranch=0.
01383682.000 |12:53:00.658 |SdlSig |CcSetupReq |restart0 |SIPvBIBCdpc(2,100,68,55) |SIPvBIB(2,100,69,1) |2,200,13,85.12078^10.241.240.197^LCP_47483708 |[R:N-H:0,N:0,L:1,V:0,Z:0,D:0] CI=43358633 CI.branch=0 sBPL.plid=65 sBPL.l=0 sBPL.pl=5 sBPL.msd=0 01383682.001 |12:53:00.658 |AppInfo |CcSetupReq onBehalfOf=Recording refCI=43358624, CI=43358633
```

#### 200 OK for LCP and Calling Party

```
01383761.001 |12:53:00.668 |AppInfo |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.106.97.135 on port 53696 index 65
[105082,NET]
SIP/2.0 200 OK
Via: SIP/2.0/TCP 10.106.97.135:5060;branch=z9hG4bKc7z5eWQrKkRtP5FKnbAb6w~~780271,SIP/2.0/TCP 10.106.97.136:5062;branch=z9hG4bKhYyfmvtY8.fM7CSyQd9K4Q~~48611
From: +1234567890 <sip:+1234567890@10.106.97.136:5062>;tag=dsf816dd0c
To: <sip:9876@CVP001.eu91.lab.test;transport=tcp>;tag=46359~8c66ebf6-153f-456b-a6e8-0bf5f687ce1f-43358624
Date: Mon, 10 Apr 2017 12:52:49 GMT
Call-ID: 694646BC1D2311E7A8D2826ACB31D85A-149182876973312598@10.106.97.136
CSeq: 1 INVITE
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
Allow-Events: presence, kpml
Record-Route: <sip:rr$n=cvp@10.106.97.135:5060;transport=tcp;lr>
Supported: replaces
Server: Cisco-CUCM10.5
Supported: X-cisco-srtp-fallback
Supported: Geolocation
Session-Expires: 1800;refresher=uas
Require: timer
P-Asserted-Identity: <sip:9876@10.107.28.14>
Remote-Party-ID: <sip:9876@10.107.28.14>;party=called;screen=yes;privacy=off
Contact: <sip:9876@10.107.28.14:5060;transport=tcp>;DeviceName="LCP_47483708"
Content-Type: application/sdp
Content-Length: 246

v=0
o=CiscoSystemsCCM-SIP 46359 1 IN IP4 10.107.28.14
s=SIP Call
c=IN IP4 10.17.229.27
b=TIAS:64000
b=CT:64
b=AS:64
t=0 0
m=audio 23304 RTP/AVP 8 101
a=ptime:20
a=rtpmap:8 PCMA/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
```

#### Recording Details

Here recording is gateway preferred :

```
01383780.001 |12:53:00.669 |AppInfo |Recording::- (0000077) -setMetaDataWithLocalPhoneOrGWForking: forkingPos=[2];forkingGuid=[694646BC1D2311E7A8D2826ACB31D85A];resDevNum=[+1234567890]
01383780.002 |12:53:00.669 |AppInfo |Recording::- (0000077) -buildOtherParm: OtherParm=[x-nearend;x-refci=43358625;x-nearendclusterid=eu91;x-nearenddevice=LCP_47483708;x-nearendaddr=9876;x-farendrefci=43358624;x-farendclusterid=eu91;x-farenddevice=EU91BCUBE002-Trk;x-farendaddr=+1234567890;x-farendguid=694646BC1D2311E7A8D2826ACB31D85A].
```

#### Digit Analysis for Recording Number

```
01383793.012 |12:53:00.669 |AppInfo |Digit analysis: analysis results
01383793.013 |12:53:00.669 |AppInfo ||PretransformCallingPartyNumber=b0026901001
|CallingPartyNumber=b0026901001
|DialingPartition=SYS-NiceRecording-PT
|DialingPattern=123456789
|FullyQualifiedCalledPartyNumber=123456789
|DialingPatternRegularExpression=(123456789)
```

#### Call Extended to a Route List

```
01383807.001 |12:53:00.670 |AppInfo  |RouteListControl::idle_CcSetupReq - RouteList(NICERecording-01-RL), numberSetup=0 numberMember=1 vmEnabled=0
```

#### Invite Sent to Recording Server for Near End Device

```
01383831.001 |12:53:00.671 |AppInfo |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.17.230.4 on port 5060 index 1
[105083,NET]
INVITE sip:123456789@10.17.230.4:5060 SIP/2.0
Via: SIP/2.0/TCP 10.107.28.14:5060;branch=z9hG4bK6b0d30bfa6ec
From: <sip:+1234567890@10.107.28.14;x-nearend;x-refci=43358625;x-nearendclusterid=eu91;x-nearenddevice=LCP_47483708;x-nearendaddr=9876;x-farendrefci=43358624;x-farendclusterid=eu91;x-farenddevice=EU91BCUBE002-Trk;x-farendaddr=+1234567890;x-farendguid=694646BC1D2311E7A8D2826ACB31D85A>;tag=46365~8c66ebf6-153f-456b-a6e8-0bf5f687ce1f-43358634
To: <sip:123456789@10.17.230.4>
Date: Mon, 10 Apr 2017 12:53:00 GMT
Call-ID: 9f432380-8eb1802c-67f6-c2e4110a@10.107.28.14
Supported: timer,resource-priority,replaces
Min-SE: 1800
User-Agent: Cisco-CUCM10.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence
Supported: X-cisco-srtp-fallback
Supported: Geolocation
Cisco-Guid: 2671977344-0000065536-0000000139-3269726474
Session-Expires: 1800
P-Asserted-Identity: <sip:+1234567890@10.107.28.14>
Remote-Party-ID: <sip:+1234567890@10.107.28.14>;party=calling;screen=yes;privacy=off
Contact: <sip:+1234567890@10.107.28.14:5060;transport=tcp>;isFocus
Max-Forwards: 70
Content-Length: 0
```

#### 200 Ok Received from the Recording Server

```
SIP/2.0 200 OK
From: <sip:+1234567890@10.107.28.14;x-nearend;x-refci=43358625;x-nearendclusterid=eu91;x-nearenddevice=LCP_47483708;x-nearendaddr=9876;x-farendrefci=43358624;x-farendclusterid=eu91;x-farenddevice=EU91BCUBE002-Trk;x-farendaddr=+1234567890;x-farendguid=694646BC1D2311E7A8D2826ACB31D85A>;tag=46365~8c66ebf6-153f-456b-a6e8-0bf5f687ce1f-43358634
To: <sip:123456789@10.17.230.4>;tag=ea1fb60-0-13c4-5506-90037-9c2acf-90037
Call-ID: 9f432380-8eb1802c-67f6-c2e4110a@10.107.28.14
CSeq: 101 INVITE
Via: SIP/2.0/TCP 10.107.28.14:5060;branch=z9hG4bK6b0d30bfa6ec
Supported: timer
Contact: <sip:123456789@10.17.230.4:5060;transport=TCP>
Session-Expires: 1800;refresher=uas
Content-Type: application/sdp
Content-Length: 119

v=0
o=VRSP 0 0 IN IP4 127.0.0.1
s=NICE VRSP
c=IN IP4 127.0.0.1
t=0 0
m=audio 1000 RTP/AVP 0 4 8 9 18
a=recvonly 
 
 
01383896.001 |12:53:00.673 |AppInfo |Recording::- (0000077) -setMetaDataWithLocalPhoneOrGWForking: forkingPos=[2];forkingGuid=[694646BC1D2311E7A8D2826ACB31D85A];resDevNum=[+1234567890]
01383896.002 |12:53:00.673 |AppInfo |Recording::- (0000077) -buildOtherParm: OtherParm=[x-farend;x-refci=43358625;x-nearendclusterid=eu91;x-nearenddevice=LCP_47483708;x-nearendaddr=9876;x-farendrefci=43358624;x-farendclusterid=eu91;x-farenddevice=EU91BCUBE002-Trk;x-farendaddr=+1234567890;x-farendguid=694646BC1D2311E7A8D2826ACB31D85A].
```

#### Acknowledgement (ACK) sent  from CUCM

```
01384017.001 |12:53:00.678 |AppInfo |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.17.230.4 on port 5060 index 1
[105086,NET]
ACK sip:123456789@10.17.230.4:5060;transport=TCP SIP/2.0
Via: SIP/2.0/TCP 10.107.28.14:5060;branch=z9hG4bK6b0e716815d6
From: <sip:+1234567890@10.107.28.14;x-nearend;x-refci=43358625;x-nearendclusterid=eu91;x-nearenddevice=LCP_47483708;x-nearendaddr=9876;x-farendrefci=43358624;x-farendclusterid=eu91;x-farenddevice=EU91BCUBE002-Trk;x-farendaddr=+1234567890;x-farendguid=694646BC1D2311E7A8D2826ACB31D85A>;tag=46365~8c66ebf6-153f-456b-a6e8-0bf5f687ce1f-43358634
To: <sip:123456789@10.17.230.4>;tag=ea1fb60-0-13c4-5506-90037-9c2acf-90037
Date: Mon, 10 Apr 2017 12:53:00 GMT
Call-ID: 9f432380-8eb1802c-67f6-c2e4110a@10.107.28.14
User-Agent: Cisco-CUCM10.5
Max-Forwards: 70
CSeq: 101 ACK
Allow-Events: presence
Content-Type: application/sdp
Content-Length: 232

v=0
o=CiscoSystemsCCM-SIP 46365 1 IN IP4 10.107.28.14
s=SIP Call
c=IN IP4 10.106.242.1
b=TIAS:0
b=AS:0
t=0 0
m=audio 7000 RTP/AVP 8 101
a=rtpmap:8 PCMA/8000
a=sendonly
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
```

#### CUCM sends Invite sent for Far End Device to Recording Server

```
01384043.001 |12:53:00.679 |AppInfo |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.17.230.4 on port 5060 index 1
[105087,NET]
INVITE sip:123456789@10.17.230.4:5060 SIP/2.0
Via: SIP/2.0/TCP 10.107.28.14:5060;branch=z9hG4bK6b0f5120dbe5
From: <sip:+1234567890@10.107.28.14;x-farend;x-refci=43358625;x-nearendclusterid=eu91;x-nearenddevice=LCP_47483708;x-nearendaddr=9876;x-farendrefci=43358624;x-farendclusterid=eu91;x-farenddevice=EU91BCUBE002-Trk;x-farendaddr=+1234567890;x-farendguid=694646BC1D2311E7A8D2826ACB31D85A>;tag=46366~8c66ebf6-153f-456b-a6e8-0bf5f687ce1f-43358637
To: <sip:123456789@10.17.230.4>
Date: Mon, 10 Apr 2017 12:53:00 GMT
Call-ID: 9f432380-8eb1802c-67f7-c2e4110a@10.107.28.14
Supported: timer,resource-priority,replaces
Min-SE: 1800
User-Agent: Cisco-CUCM10.5
Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY
CSeq: 101 INVITE
Expires: 180
Allow-Events: presence
Supported: X-cisco-srtp-fallback
Supported: Geolocation
Cisco-Guid: 2671977344-0000065536-0000000140-3269726474
Session-Expires: 1800
P-Asserted-Identity: <sip:+1234567890@10.107.28.14>
Remote-Party-ID: <sip:+1234567890@10.107.28.14>;party=calling;screen=yes;privacy=off
Contact: <sip:+1234567890@10.107.28.14:5060;transport=tcp>;isFocus
Max-Forwards: 70
Content-Length: 0
```

#### 200 OK from Recording Server

```
SIP/2.0 200 OK
From: <sip:+1234567890@10.107.28.14;x-farend;x-refci=43358625;x-nearendclusterid=eu91;x-nearenddevice=LCP_47483708;x-nearendaddr=9876;x-farendrefci=43358624;x-farendclusterid=eu91;x-farenddevice=EU91BCUBE002-Trk;x-farendaddr=+1234567890;x-farendguid=694646BC1D2311E7A8D2826ACB31D85A>;tag=46366~8c66ebf6-153f-456b-a6e8-0bf5f687ce1f-43358637
To: <sip:123456789@10.17.230.4>;tag=ea1f830-0-13c4-5506-90037-22ea55b6-90037
Call-ID: 9f432380-8eb1802c-67f7-c2e4110a@10.107.28.14
CSeq: 101 INVITE
Via: SIP/2.0/TCP 10.107.28.14:5060;branch=z9hG4bK6b0f5120dbe5
Supported: timer
Contact: <sip:123456789@10.17.230.4:5060;transport=TCP>
Session-Expires: 1800;refresher=uas
Content-Type: application/sdp
Content-Length: 119

v=0
o=VRSP 0 0 IN IP4 10.10.1.10
s=NICE VRSP
c=IN IP4 127.0.0.1
t=0 0
m=audio 1000 RTP/AVP 0 4 8 9 18
a=recvonly
```

#### ACK sent  from CUCM

```
01384207.001 |12:53:00.882 |AppInfo |SIPTcp - wait_SdlSPISignal: Outgoing SIP TCP message to 10.17.230.4 on port 5060 index 1
[105091,NET]
ACK sip:123456789@10.17.230.4:5060;transport=TCP SIP/2.0
Via: SIP/2.0/TCP 10.107.28.14:5060;branch=z9hG4bK6b1013a924b6
From: <sip:+1234567890@10.107.28.14;x-farend;x-refci=43358625;x-nearendclusterid=eu91;x-nearenddevice=LCP_47483708;x-nearendaddr=9876;x-farendrefci=43358624;x-farendclusterid=eu91;x-farenddevice=EU91BCUBE002-Trk;x-farendaddr=+1234567890;x-farendguid=694646BC1D2311E7A8D2826ACB31D85A>;tag=46366~8c66ebf6-153f-456b-a6e8-0bf5f687ce1f-43358637
To: <sip:123456789@10.17.230.4>;tag=ea1f830-0-13c4-5506-90037-22ea55b6-90037
Date: Mon, 10 Apr 2017 12:53:00 GMT
Call-ID: 9f432380-8eb1802c-67f7-c2e4110a@10.107.28.14
User-Agent: Cisco-CUCM10.5
Max-Forwards: 70
CSeq: 101 ACK
Allow-Events: presence
Content-Type: application/sdp
Content-Length: 232

v=0
o=CiscoSystemsCCM-SIP 46366 1 IN IP4 10.107.28.14
s=SIP Call
c=IN IP4 10.106.242.1
b=TIAS:0
b=AS:0
t=0 0
m=audio 7000 RTP/AVP 8 101
a=rtpmap:8 PCMA/8000
a=sendonly
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
```

#### Agent Finally Calling the Number

RCP Port   listens to MOH , then later on disconnects from MOH and connect back to agent to connect the agent finally to calling number.

```
01384484.001 |12:53:04.609 |AppInfo  |ARBTRY-ConnectionManager-wait_MediaConnectRequest(43358626,43358627)
01384484.002 |12:53:04.609 |AppInfo  |ARBTRY-ConnectionManager- storeMediaInfo(CI=43358626): EXISTING ENTRY DISCOVERED, size=9
01384484.003 |12:53:04.609 |AppInfo  |ARBTRY-ConnectionManager- storeMediaInfo(CI=43358627): EXISTING ENTRY DISCOVERED, size=9
```

#### CUCM send SDL HTTP Request

Only after 200 OK happens for the near end and the far end device Invite, CUCM sends SDL Http request to initiate recording

#### SDL HTTP Request for LCP Recording

```
01384808.000 |12:53:04.672 |SdlSig |SdlHTTPReq |wait |SdlHTTPService(2,100,6,1) |CayugaInterface(2,100,34,1) |2,100,14,283.3^10.17.230.4^* |[T:N-H:0,N:0,L:0,V:0,Z:0,D:0] method: 3 url: http://10.106.97.138:8090/cisco_xmf data: <?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope">
<soapenv:Body>
<RequestXmfConnectionMediaForking xmlns="http://www.cisco.com/schema/cisco_xmf/v1_0">
<msgHeader>
<transactionID>Cisco:UCM:CayugaIf:1:69</transactionID>
<registrationID>C094:XMF:Unified CM 10.5.2.12901-1:1</registrationID>
</msgHeader>
<callID>42</callID>
<connID>554</connID>
<action>
<enableMediaForking>
<nearEndAddr>
<ipv4>10.17.230.5</ipv4>
<port>42095</port>
</nearEndAddr>
<farEndAddr>
<ipv4>10.17.230.5</ipv4>
<port>42094</port>
</farEndAddr>
<preserve>true</preserve>
</enableMediaForking>
</action>
</RequestXmfConnectionMediaForking>
</soapenv:Body>
</soapenv:Envelope>
```

```
01384843.001 |12:53:04.674 |AppInfo |Recording::- (0000077) - Media Setup Complete: mRecordingCallInfo
01384843.002 |12:53:04.674 |AppInfo |RCD_RecordingCallInfo::print: resourceInfo
01384843.003 |12:53:04.674 |AppInfo |RCD_ResourceInfo::print: nodeId=2
01384843.004 |12:53:04.674 |AppInfo |RCD_ResourceInfo::print: bNum
01384843.005 |12:53:04.674 |AppInfo |RCD_Utility::printCcPtyNum: CcPtyNum contains only Directory Number (b0026901001)
01384843.006 |12:53:04.674 |AppInfo |RCD_RecordingCallInfo::print: recordedPartyInfo
01384843.007 |12:53:04.674 |AppInfo |RCD_RecordedPartyInfo::print: ssAe
01384843.008 |12:53:04.674 |AppInfo |RCD_Utility::printSsAe: ss=43358625, nodeId=2
01384843.009 |12:53:04.674 |AppInfo |RCD_RecordedPartyInfo::print: partyNum
01384843.010 |12:53:04.674 |AppInfo |RCD_Utility::printCcPtyNum: CcPtyNum contains only Directory Number (+1234567890)
01384843.011 |12:53:04.674 |AppInfo |RCD_RecordedPartyInfo::print: deviceName = LCP_47483708

01384843.023 |12:53:04.674 |AppInfo |RCD_Utility::printCcPtyNum: CcPtyNum contains only Directory Number (123456789)
01384843.024 |12:53:04.674 |AppInfo |RCD_RecorderPartyInfo::print: partition = 812fe5de-3a9b-4d67-9fdd-023582e18388, deviceName = NICERecording-01
```

## Related Information

- http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/mediasense/10/srnd/CUMS_BK_MC36D963_00_mediasense-srnd/CUMS_BK_MC36D963_00_mediasense-srnd_chapter_0111.html

- http://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/configuration/cube-book/voi-cube-uc-gateway-services.html

- http://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/configuration/cube-book/voi-ntwk-based.html

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

23-Jun-2017

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 23-Jun-2017 | Initial Release |