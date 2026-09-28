---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-express-200764-uccx-call-back-feature-a-3757899202
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-express/200764-UCCX-Call-Back-Feature-as-seen-on-CUCM-a.html
retrieved_at: 2026-08-16T21:15:51.337470+00:00
---

UCCX Call Back Feature as seen on CUCM and UCCX

# UCCX Call Back Feature as seen on CUCM and UCCX

### Download Options

Updated: October 19, 2016

Document ID: 200764

Contents

## Contents

## Introduction

This document describes how the CallBack UCCX (Cisco Unified Contact Center Express) feature works. This document focuses on the analysis of a good working call with the use of the UCCX and CUCM (Cisco Unified Communications Manager) traces and spots the key moments in the call flow with the help of log analysis.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUCM configuration

- UCCX configuration

- Reading basic CUCM SDI/SDL traces

- Reading basic UCCX logs

### Components Used

The information in this document is based on these software versions:

- CUCM verion :  10.5.2.12900-14

- UCCX Version :  10.6.1.11001-31

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

Note : A Base Script is avaliabe at UCCX script repository at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-implementation-design-guides-list.html. You will find a Zip file. In that ZIP-file there is a folder called BaseLineAdvQueuing that contains a script that you can use as a base script. There is also a Word document that describes how the script works.

## Background Information

When a customer calls in to a UCCX Queue and if at that time all available agents are busy and cannot take the call, then at a preset Timeout, a prompt is played. This is to ask the customer if he/she wishes for a call back. The customer can choose a call back or leave a message.

- If the customer chooses to leave a message then the message is recorded and the call is disconnected. The system inturn turn calls another CTI (Cisco Computer Telephony Integration) trigger or Ghost trigger and keeps the call there till an agent is free and then plays the recored message to him.

- If the customer chooses call back, then he/she is prompted to enter the call back number. After the confirmation of the number, the call is disconnected. The system inturn turn calls another CTI trigger or Ghost trigger and keeps the call there till an agent is free, takes inout from the agent to connect the agent to call back to the number of the customer.

## Flow Diagram

## CUCM Perspective

The callback feature can be broken down into 3 stages

Stage 1. User Input

Stage 2. Place Call

Stage 3. Call Redirect

### Stage 1. User Input

In this stage the customer Calls in the UCCX queue and all agents are busy. Customer is given an option for a call back. Once the customer selects it, he/she is prompted to enter the call back number and record a message. A confirmation message is played after which the call is disconnected.

### Stage 2. Place Call Stage

In this stage UCCX retains the callback number and initiates a new call to CTI trigger which has the normal ICD (Interactive Call Distribution) routing and keeps the ghost call here till an agent is free to take a call.

This call is a Ghost call since the Place call step uses completely different set of CTI ports (Call Control Group ID is different) and new Media Channel Group, configured on the UCCX and in the script itself.

### Stage 3. Call Redirect Stage

In this stage, the agent has answered the call, the agent listens to the message that the caller left as much as he or she wants and presses a key to have the system call back the caller from the number the caller left initially. The UCCX system will now initiate a Call Redirect. this is used to transfer the call between the system and the agent to the caller at the callback number entered.

## UCCX Perspective

The callback feature is broken down into 2 scripts which have 2 different applications and 2 triggers to reach these scripts.

### Script 1.

Customer calls into this script (mainline number), where if agents are busy is prompted for a callback.

This script is configured with a Place call step to another number called the callback number which is another trigger with a simple ICD script.

### Script 2.

A simple ICD script for the callback trigger having a select resource into a CSQ containing pool of agents to be selected for the callback. The customer's call is dropped after he enters the callback number and a Ghost call is  redirected to this script and kept in waiting.

When an Agent is available for the callback to initiate this call is bridged to the customer's callback number provided with a Call Redirect script.

There must be 2 different Call Control Groups used for these scripts under Subsystems > CM Telephony > Call Control Group .

There must be 2 different Media Channels defined under Subsystems > Cisco Media .

For example :

Script 1 : Inbound call to this script will come through Call Control Group ID 1 and Media Channel Group 1.

The place call step in this script will use Call Control Group ID 2 and Media Channel Group 2.

Script 2 : This script must have a trigger using a different media channel from script 1. For example; Media channel ID 2 and Call Control Group ID 2.

## Call Details Used in Lab

Initial Customer Calling Number : 2161

UCCX Mainline Queue Number : 9999

UCCX Call back trigger : 3999

Callback number left: 08062131

Agent Number : 62151 (SIP Phone)

## CUCM Log Analysis

### Stage 1. User Input

Incoming invite from Customer IP Phone:

```
###$ Invite for UCCX trigger $### 02302874.002 |10:14:27.152 |AppInfo  |SIPTcp - wait_SdlReadRsp: Incoming SIP TCP message from 10.106.87.161 on port 52035 index 19 with 1475 bytes: [83471,NET] INVITE sip:9@10.106.87.135;user=phone SIP/2.0 Via: SIP/2.0/TCP 10.106.87.161:52035;branch=z9hG4bK0593f26a From: "2161" <sip:2161@10.106.87.135>;tag=e8ba7006276f00792818f1b2-6550ea32 To: <sip:9@10.106.87.135> Call-ID: e8ba7006-276f0004-3895b0cc-3fda7fb1@10.106.87.161 Max-Forwards: 70 Date: Fri, 08 Apr 2016 04:44:25 GMT CSeq: 101 INVITE User-Agent: Cisco-CP8961/9.4.2 Contact: <sip:849fe75d-ae74-8e22-d48e-c11feccbecf2@10.106.87.161:52035;transport=tcp> Expires: 180 Accept: application/sdp Allow: ACK,BYE,CANCEL,INVITE,NOTIFY,OPTIONS,REFER,REGISTER,UPDATE,SUBSCRIBE,INFO Remote-Party-ID: "2161" <sip:2161@10.106.87.135>;party=calling;id-type=subscriber;privacy=off;screen=yes Supported: replaces,join,sdp-anat,norefersub,resource-priority,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-7.0.0,X-cisco-xsi-8.0.1 Allow-Events: kpml,dialog Recv-Info: conference Recv-Info: x-cisco-conference Content-Length: 354 Content-Type: application/sdp Content-Disposition: session;handling=optional v=0 o=Cisco-SIPUA 23877 0 IN IP4 10.106.87.161 s=SIP Call t=0 0 m=audio 17818 RTP/AVP 102 0 8 116 18 101 c=IN IP4 10.106.87.161 a=rtpmap:102 L16/16000 a=rtpmap:0 PCMU/8000 a=rtpmap:8 PCMA/8000 a=rtpmap:116 iLBC/8000 a=fmtp:116 mode=20 a=rtpmap:18 G729/8000 a=fmtp:18 annexb=no a=rtpmap:101 telephone-event/8000 a=fmtp:101 0-15 a=sendrecv
```

You see that a Digit Analysis happens for UCCX number 9999:

```
###$ Digit Analysis happens for UCCX number 9999 $### 02302962.007 |10:14:27.832 |AppInfo  |Digit analysis: match(pi="2", fqcn="2161", cn="2161",plv="5", pss="", TodFilteredPss="", dd="9999",dac="0") 02302962.008 |10:14:27.832 |AppInfo  |Digit analysis: analysis results 02302962.009 |10:14:27.832 |AppInfo  ||PretransformCallingPartyNumber=2161 |CallingPartyNumber=2161 |DialingPartition= |DialingPattern=9999 |FullyQualifiedCalledPartyNumber=9999 |DialingPatternRegularExpression=(9999) |DialingWhere= |PatternType=Enterprise
```

In response to the find out where 9999 number should be routed, you get the Linecontroller and this is the next process that handles the call:

```
02302964.000 |10:14:27.832 |SdlSig   |DmPidRes                               |wait                           |Da(1,100,211,1)                  |DeviceManager(1,100,205,1)       |1,100,14,94509.144^10.106.87.161^*       |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0]  Cepn=4eebaf05-990d-7980-a79f-e4488fb75cec Id=3836477808 ccmType=4 DeviceName=9999: Pid=1,100,174,555,ad243d17-98b4-4118-8feb-5ff2e1b781ac ###$ PID=LineControl(1,100,174,555) is the response 02302964.001 |10:14:27.832 |AppInfo  |Digit analysis: wait_DmPidRes- Partition=[] Pattern=[9999] Where=[],cmDeviceType=[UserDevice], OutsideDialtone =[0], DeviceOverride=[0], PID=LineControl(1,100,174,555),CI=[31614358],Sender=Cdcc(1,100,219,249)
```

This leads us to the Linecontroller:

```
02302975.001 |10:14:27.833 |AppInfo  |LineControl(555) - 0 calls, 0 CiReq, busyTrigger=10000, maxCall=10000 02302975.002 |10:14:27.833 |Created  |                                       |                               |LineCdpc(1,100,175,269)          |LineControl(1,100,174,555)       |                                         |NumOfCurrentInstances: 2 02302975.003 |10:14:27.833 |AppInfo  |LineControl(555) - Get call instance=1 for CI=31614359 02302975.004 |10:14:27.833 |AppInfo  |LineControl(555): restart0_CcSetupReq update State of cdpc (269) to receive7
```

Linecontroller now leads us to device (CTI Port):

```
02302979.000 |10:14:27.834 |SdlSig   |CcSetupReq                             |null0                          |LineCdpc(1,100,175,269)          |LineControl(1,100,174,555)       |1,100,14,94509.144^10.106.87.161^*       |[R:N-H:0,N:1,L:0,V:0,Z:0,D:0] CI=31614359 CI.branch=0  sBPL.plid=65 sBPL.l=1 sBPL.pl=5 sBPL.msd=0  FDataType=0opId=0ssType=0 SsKey=0invokeId=0resultExp=Fbpda=F pi.piid=30 pi.l=0 pi2.piid=30 pi2.l=0 pi3.piid=30 pi3.l=0 FQCGPN=ti=1nd=2161pi=0si1 preXCgpn=tn=0npi=0ti=1nd=2161pi=0si1 cgPart= cgPat=2161 cgpn=tn=0npi=0ti=1nd=2161pi=1si1 cgpnVM= unXCgpn=tn=0npi=0ti=1nd=2161pi=1si1 cName=locale: 1 Name:  UnicodeName:  pi: 1 DD=tn=0npi=1ti=1nd=9999User=9999Host=10.106.87.135Port=5060PassWord=Madder=Transport=4mDisplayName=RawUrl=sip:9@10.106.87.135;user=phoneOrigPort=0pi=0si1 origDD=tn=0npi=1ti=1nd=9999User=9999Host=10.106.87.135Port=5060PassWord=Madder=Transport=4mDisplayName=RawUrl=sip:9@10.106.87.135;user=phoneOrigPort=0pi=0si1 preXCdpn=tn=0npi=0ti=1nd=9999pi=0si0 preXTagsList=SUBSCRIBER preXPosMatchList=9999 cdPart= cdPat=9999 cdpn=tn=0npi=0ti=1nd=9999pi=1si1 cdpnVMbox= localPatternUsage=2 connectedPatternUsage=2 itrPart= itrPat= LRPart= LRPat=9999 LR=tn=0npi=0ti=1nd=9999pi=0si1 LRVM= LRName=locale: 1 Name:  UnicodeName:  pi: 0 FQOCpdn=ti=1nd=9999pi=0si1 fFQLRNum=ti=1nd=9999pi=0si1 oPart= oPat=9999 oCpdn=tn=0npi=0ti=1nd=9999pi=0si1 oCdpnVM= oRFR=0 oName=locale: 1 Name:  UnicodeName:  pi: 0 ts=SUBSCRIBER posMatches=9999 withTags= withValues= rdn.l=0IpAddrMode=0 ipAddrType=0 ipv4=10.106.87.161:52035 region=Default capCount=5 ctiActive=F ctiFarEndDev=1 ctiCCMId=1 cgPtyDev=SEPE8BA7006276F callInst=1 confCallInst=0 OLF=1Supp DTMF=3DTMF Cfg=1DTMF Payload=101isOffNetDev=F bc.l=3 bc.itr=1 bc.itc=0 bc.trm=0 bc.tm=16 maxForwards=69 cgpnMaskedByRedirect=F callingDP=1b1b9eb6-7803-11d3-bdf0-00108302ead1 featCallType=0 callingUserId= UnicodeName:  muteEnabled=0 associatedCallCI=0 featurePriority=1 nonTargetPolicy=0 unconsumedDigits= suppressMOH=F numPlanPkid =4eebaf05-990d-7980-a79f-e4488fb75cec networkDomain= bitMask=0 SetupReason=0 routeClass=1 sideACmDeviceType=4 protected=1 ControlProcessType=0 tokens=0 isPresent=F transitCount=0 geolocInfo={geolocPkid=, filterPkid=, geolocVal=, devType=4} locPkid=29c5c1c4-8871-4d1e-8394-0b9181e8c54d locName=Hub_None deductBW=F fateShareId=StandAloneCluster:31614358 videoTrafficClass=Desktop oFromAnalogDvc=F bridgeParticipantID= callingUsr= remoteClusterID= isEMCCDevice=F lHPMemCEPN= cHPMemCEPN= uri=ti=1User=Host=Port=0PassWord=Madder=Transport=4mDisplayName=RawUrl=<sip:849fe75d-ae74-8e22-d48e-c11feccbecf2@10.106.87.161:52035;transport=tcp>OrigPort=0pi=0si1 isParamSet=T M=Unknown ;rc=0 Hdrs= CanSupportSIPTandN=true TransId=0 AllowBitMask=0x7bf UserAgentOrServer=Cisco-CP8961/9.4.2 OrigDDName=locale: 1 Name:  UnicodeName:  pi: 0 mCallerId= mCallerName=LatentCaps=null icidVal= icidGenAddr= oioi= tioi= ptParams= receivedPAID= routeHdr= routeCepn= requestURI= PCVFlag=F originallyHadISUP=F isIMSFinalRoute=F IMSMode=0 SideABibEnabled= 3 isCgpnNonPreemptable=F isCdpnNonPreemptable=F origDP=1b1b9eb6-7803-11d3-bdf0-00108302ead1 lastRedirectingDP=1b1b9eb6-7803-11d3-bdf0-00108302ead1 originalLRG= lastRedirectingLRG= nwLoc=0 rstr= FarEndDeviceName=SEPE8BA7006276F hdrMOH=0 CAL={v=ffffffff, m=ffffffff, tDev=F, res=F, devType=0} 02302979.001 |10:14:27.834 |AppInfo  |LineCdpc(269): -dispatchToAllDevices-, sigName=CcSetupReq, device=TRG2
```

The call is now presented to the CTI port and the Port answers the call:

```
02303167.000 |10:14:27.874 |SdlSig-I |CtiLineCallAnswerReq                   |restart0                       |StationD(1,100,63,520)           |CTIDeviceLineMgr(1,200,25,1)     |1,200,13,273912.572^10.106.87.133^TEST_543210 |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0]  mAsyncResponse=6043 CH=1|31614360 LH=1|1063 MediaDeviceName =  MediaDevicePid = (0,0,0,0) resource ID=0 02303167.001 |10:14:27.874 |AppInfo  |StationD(520): StationCtiD-CtiLineCallAnswerReq LH=1|1063 02303167.002 |10:14:27.874 |AppInfo  |StationD(520): StationCtiD-CtiLineCallAnswerReq LH=1|1063 02303168.000 |10:14:27.874 |SdlSig   |StationOffHook                         |restart0                       |StationD(1,100,63,520)           |StationD(1,100,63,520)           |1,200,13,273912.572^10.106.87.133^TEST_543210 |[R:N-H:0,N:1,L:0,V:0,Z:0,D:0] Line=1 CI=31614360 GCI.node=0 GCI.ci=0 mDialedDigits= mPrimaryCi=0 cgpn= cgpnVMBx= trigger=0 mSpoofCgp=F fp=1 fid=9999 FDataType=0opId=0ssType=0 SsKey=0invokeId=0resultExp=Fbpda=F ###$ CTI Port Answered the call or Call is now in Queue $### 02303168.001 |10:14:27.874 |AppInfo  |StationD:    (0000520) restart0_StationOffHook - INFO: CI=31614360 on line=1, SPKMode=0, alwaysPrimeLine=0, alwaysUsePrimeLineForVM=0, fid=9999, offHookTrigger=0. 02303168.002 |10:14:27.874 |AppInfo  |StationD:    (0000520) restart0_StationOffHook - INFO: CI=31614360 on line=1, SPKMode=0. Answer. 02303168.003 |10:14:27.874 |AppInfo  |StationD:    (0000520) preProcessing - INFO: Please Send the signal now. 02303168.004 |10:14:27.874 |AppInfo  |StationD:    (0000520) INFO- sendSignalNow, sigName=StationOffHook, cdpc=240
```

At this point the caller is in the Queue and the announcemet is played. After a preset time, the customer chooses the call back feature and starts to enter the call back number as DTMF digits  0,8,0,6,2,1,3,1,#.

```
###$ Digit 0 $### 02303407.000 |10:14:46.625 |SdlSig-O |CtiDTMFNotify                          |NA RemoteSignal                |UnknownProcessName(1,200,25,1)   |StationCdpc(1,100,64,240)        |1,100,14,94509.150^10.106.87.161^*       |[R:N-H:0,N:1,L:0,V:0,Z:0,D:0]  LH=1|1063 CH=1|31614360 GCH=1|29124 02303408.000 |10:14:46.625 |SdlSig   |StationOutputKeypadButton              |restart0                       |StationD(1,100,63,520)           |StationCdpc(1,100,64,240)        |1,100,14,94509.150^10.106.87.161^*       |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] Digit=0 CI=31614360Line=1
```

```
###$ Digit 8 $### 02303430.000 |10:14:47.243 |SdlSig-O |CtiDTMFNotify                          |NA RemoteSignal                |UnknownProcessName(1,200,25,1)   |StationCdpc(1,100,64,240)        |1,100,14,94509.151^10.106.87.161^*       |[R:N-H:0,N:1,L:0,V:0,Z:0,D:0]  LH=1|1063 CH=1|31614360 GCH=1|29124 02303431.000 |10:14:47.243 |SdlSig   |StationOutputKeypadButton              |restart0                       |StationD(1,100,63,520)           |StationCdpc(1,100,64,240)        |1,100,14,94509.151^10.106.87.161^*       |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] Digit=8 CI=31614360Line=1
```

```
###$ Digit 0 $### 02303446.000 |10:14:47.791 |SdlSig-O |CtiDTMFNotify                          |NA RemoteSignal                |UnknownProcessName(1,200,25,1)   |StationCdpc(1,100,64,240)        |1,100,14,94509.152^10.106.87.161^*       |[R:N-H:0,N:1,L:0,V:0,Z:0,D:0]  LH=1|1063 CH=1|31614360 GCH=1|29124 02303447.000 |10:14:47.791 |SdlSig   |StationOutputKeypadButton              |restart0                       |StationD(1,100,63,520)           |StationCdpc(1,100,64,240)        |1,100,14,94509.152^10.106.87.161^*       |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] Digit=0 CI=31614360Line=
```

```
###$ Digit 6 $### 02303465.000 |10:14:48.962 |SdlSig-O |CtiDTMFNotify                          |NA RemoteSignal                |UnknownProcessName(1,200,25,1)   |StationCdpc(1,100,64,240)        |1,100,14,94509.153^10.106.87.161^*       |[R:N-H:0,N:1,L:0,V:0,Z:0,D:0]  LH=1|1063 CH=1|31614360 GCH=1|29124 02303466.000 |10:14:48.962 |SdlSig   |StationOutputKeypadButton              |restart0                       |StationD(1,100,63,520)           |StationCdpc(1,100,64,240)        |1,100,14,94509.153^10.106.87.161^*       |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] Digit=6 CI=31614360Line=1
```

```
###$ Digit 2 $### 02303481.000 |10:14:49.520 |SdlSig-O |CtiDTMFNotify                          |NA RemoteSignal                |UnknownProcessName(1,200,25,1)   |StationCdpc(1,100,64,240)        |1,100,14,94509.154^10.106.87.161^*       |[R:N-H:0,N:1,L:0,V:0,Z:0,D:0]  LH=1|1063 CH=1|31614360 GCH=1|29124 02303482.000 |10:14:49.520 |SdlSig   |StationOutputKeypadButton              |restart0                       |StationD(1,100,63,520)           |StationCdpc(1,100,64,240)        |1,100,14,94509.154^10.106.87.161^*       |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] Digit=2 CI=31614360Line=1
```

```
###$ Digit 1 $### 02303499.000 |10:14:50.014 |SdlSig-O |CtiDTMFNotify                          |NA RemoteSignal                |UnknownProcessName(1,200,25,1)   |StationCdpc(1,100,64,240)        |1,100,14,94509.155^10.106.87.161^*       |[R:N-H:0,N:1,L:0,V:0,Z:0,D:0]  LH=1|1063 CH=1|31614360 GCH=1|29124 02303500.000 |10:14:50.014 |SdlSig   |StationOutputKeypadButton              |restart0                       |StationD(1,100,63,520)           |StationCdpc(1,100,64,240)        |1,100,14,94509.155^10.106.87.161^*       |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] Digit=1 CI=31614360Line=1
```

```
###$ Digit 3 $### 02303516.000 |10:14:50.431 |SdlSig-O |CtiDTMFNotify                          |NA RemoteSignal                |UnknownProcessName(1,200,25,1)   |StationCdpc(1,100,64,240)        |1,100,14,94509.156^10.106.87.161^*       |[R:N-H:0,N:1,L:0,V:0,Z:0,D:0]  LH=1|1063 CH=1|31614360 GCH=1|29124 02303517.000 |10:14:50.431 |SdlSig   |StationOutputKeypadButton              |restart0                       |StationD(1,100,63,520)           |StationCdpc(1,100,64,240)        |1,100,14,94509.156^10.106.87.161^*       |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] Digit=3 CI=31614360Line=1
```

```
###$ Digit 1 $### 02303532.000 |10:14:50.858 |SdlSig-O |CtiDTMFNotify                          |NA RemoteSignal                |UnknownProcessName(1,200,25,1)   |StationCdpc(1,100,64,240)        |1,100,14,94509.157^10.106.87.161^*       |[R:N-H:0,N:1,L:0,V:0,Z:0,D:0]  LH=1|1063 CH=1|31614360 GCH=1|29124 02303533.000 |10:14:50.858 |SdlSig   |StationOutputKeypadButton              |restart0                       |StationD(1,100,63,520)           |StationCdpc(1,100,64,240)        |1,100,14,94509.157^10.106.87.161^*       |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] Digit=1 CI=31614360Line=1
```

```
###$ Digit # pressed to confirm the call back  $### 02303549.000 |10:14:51.558 |SdlSig-O |CtiDTMFNotify                          |NA RemoteSignal                |UnknownProcessName(1,200,25,1)   |StationCdpc(1,100,64,240)        |1,100,14,94509.158^10.106.87.161^*       |[R:N-H:0,N:1,L:0,V:0,Z:0,D:0]  LH=1|1063 CH=1|31614360 GCH=1|29124 02303550.000 |10:14:51.558 |SdlSig   |StationOutputKeypadButton              |restart0                       |StationD(1,100,63,520)           |StationCdpc(1,100,64,240)        |1,100,14,94509.158^10.106.87.161^*       |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] Digit=# CI=31614360Line=1
```

```
###$ CTI/UCCX disconnect the call $### 02303553.000 |10:14:51.561 |SdlSig-I |CtiLineCallDisconnectReq               |restart0                       |StationD(1,100,63,520)           |CTIDeviceLineMgr(1,200,25,1)     |1,200,13,273912.574^10.106.87.133^TEST_543210 |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0]  mAsyncResponse=6045 CH=1|31614360 LH=1|1063 02303553.001 |10:14:51.561 |AppInfo  |StationD(520): StationCtiD-CtiLineCallDisconnectReq LH=1|1063 02303553.002 |10:14:51.561 |AppInfo  |StationD(520): StationCtiD-CtiLineCallDisconnectReq LH=1|1063
```

With this message, the call with PSTN (Public Switched Telephone Network) is disconnected and Stage 1 or User Input stage is completed.

### Stage 2. Place Call

You see that the system initates a call to callback CTI trigger 3999.

```
###$ CTI redirect to Call back trigger (Stage 2 ) 02303675.000 |10:14:51.772 |SdlSig-I |CtiLineCallInitiateReq                 |restart0                       |StationD(1,100,63,520)           |CTIDeviceLineMgr(1,200,25,1)     |1,200,13,273912.576^10.106.87.133^TEST_543210 |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] AsyncResponse=6046 LH=1|1063 GCH=1|29125 CalledPartyInfo=3999 MediaDeviceName =  MediaDevicePid = (0,0,0,0) resource ID=0 FetaurePriority=1
```

```
###$ Digit Analysis  for CTI call back number $### 02303722.006 |10:14:51.778 |AppInfo  |Digit analysis: match(pi="2", fqcn="543210", cn="543210",plv="5", pss="", TodFilteredPss="", dd="3999",dac="0") 02303722.007 |10:14:51.778 |AppInfo  |Digit analysis: analysis results 02303722.008 |10:14:51.778 |AppInfo  ||PretransformCallingPartyNumber=543210 |CallingPartyNumber=543210 |DialingPartition= |DialingPattern=3999 |FullyQualifiedCalledPartyNumber=3999 |DialingPatternRegularExpression=(3999)
```

```
###$ Call is offered to CTI Ports (This is the Queue for Busy application) 02303783.006 |10:14:51.803 |AppInfo  |Digit analysis: match(pi="1", fqcn="543210", cn="543210",plv="5", pss="", TodFilteredPss="", dd="4003",dac="0") 02303783.007 |10:14:51.803 |AppInfo  |Digit analysis: analysis results 02303783.008 |10:14:51.803 |AppInfo  ||PretransformCallingPartyNumber=543210 |CallingPartyNumber=543210 |DialingPartition= |DialingPattern=4003 |FullyQualifiedCalledPartyNumber=4003
```

```
###$ CTI port accepts the call or Answers the call 02303916.000 |10:14:51.855 |SdlSig   |StationOffHook                         |call_received7                 |StationCdpc(1,100,64,243)        |StationD(1,100,63,509)           |1,200,13,273912.579^10.106.87.133^ICD_4003 |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] Line=1 CI=31614363 GCI.node=0 GCI.ci=0 mDialedDigits= mPrimaryCi=0 cgpn= cgpnVMBx= trigger=0 mSpoofCgp=F fp=1 fid=0 FDataType=0opId=0ssType=0 SsKey=0invokeId=0resultExp=Fbpda=F 02303916.001 |10:14:51.855 |AppInfo  |StationCdpc(243): StationCtiCdpc-StationOffHook CH=1|31614363 02303916.002 |10:14:51.855 |AppInfo  |StationCdpc(243): StationCtiCdpc-StationOffHook CH=1|31614363
```

CTI now does a transfer to agent once an agent is free to accept the call:

```
###$ CTI Initating Transfer to Agent is now avaliabe to take the call 02304085.000 |10:14:53.429 |SdlSig-I |CtiLineCallTransferSetupReq            |restart0                       |StationD(1,100,63,509)           |CTIDeviceLineMgr(1,200,25,1)     |1,200,13,273912.583^10.106.87.133^ICD_4003 |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0] AsyncResponse=6054 LH=1|1041 CH=1|31614363 DN=62151 ConsultWithoutMedia=T 02304085.001 |10:14:53.429 |AppInfo  |StationD(509): StationCtiD-CtiLineCallTransferSetupReq CH=1|31614363 cdpn=62151 02304085.002 |10:14:53.429 |AppInfo  |StationD(509): StationCtiD-CtiLineCallTransferSetupReq CH=1|31614363 cdpn=62151
```

```
###$ DD for Agent 02304237.006 |10:14:53.440 |AppInfo  |Digit analysis: match(pi="2", fqcn="4003", cn="4003",plv="5", pss="", TodFilteredPss="", dd="62151",dac="0") 02304237.007 |10:14:53.440 |AppInfo  |Digit analysis: analysis results 02304237.008 |10:14:53.440 |AppInfo  ||PretransformCallingPartyNumber=4003 |CallingPartyNumber=4003 |DialingPartition= |DialingPattern=62151 |FullyQualifiedCalledPartyNumber=62151 |DialingPatternRegularExpression=(62151)
```

```
###$ Invite for the Agent INVITE sip:b16b6893-445d-6407-2a23-83e6ff6fb4f7@10.106.87.164:52242;transport=tcp SIP/2.0 Via: SIP/2.0/TCP 10.106.87.135:5060;branch=z9hG4bK3fc859136cc1 From: "Busy Application" <sip:4003@10.106.87.135>;tag=32711~54aff7a7-042a-4733-9a99-8a2f7027a30d-31614366 To: <sip:62151@10.106.87.135> Date: Fri, 08 Apr 2016 04:44:53 GMT Call-ID: a13f5600-70713745-3da4-87576a0a@10.106.87.135 Supported: timer,resource-priority,replaces Min-SE:  1800 User-Agent: Cisco-CUCM10.5 Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY CSeq: 101 INVITE Expires: 180 Allow-Events: presence Call-Info: <urn:x-cisco-remotecc:callinfo>; security= Unknown; orientation= from; gci= 1-29126; isVoip; call-instance= 1 Send-Info: conference, x-cisco-conference Alert-Info: <file://Bellcore-dr1/> Remote-Party-ID: "Busy Application" <sip:4003@10.106.87.135;x-cisco-callback-number=4003>;party=calling;screen=yes;privacy=off Contact: <sip:4003@10.106.87.135:5060;transport=tcp> Max-Forwards: 70 Content-Length: 0
```

After this the agent is connected by the busy to busy script and Stage 3 Call Redirect starts.

### Stage 3. Call Redirect

The agent listens to options that are present. Option 1 accepts the call and calls back the customer.

The agent presses digit 1 in the soft key pad:

```
###$ Digit 1 pressed by the agent NOTIFY sip:10.106.87.135:5060 SIP/2.0 Via: SIP/2.0/TCP 10.106.87.164:52242;branch=z9hG4bK187640df To: "Busy Application" <sip:4003@10.106.87.135>;tag=32711~54aff7a7-042a-4733-9a99-8a2f7027a30d-31614366 From: <sip:62151@10.106.87.135>;tag=e8ba70fb6e0a20544386b963-4947235a Call-ID: a13f5600-70713745-3da4-87576a0a@10.106.87.135 Date: Fri, 08 Apr 2016 04:45:01 GMT CSeq: 102 NOTIFY Event: kpml Subscription-State: active; expires=7200 Max-Forwards: 70 Contact: <sip:b16b6893-445d-6407-2a23-83e6ff6fb4f7@10.106.87.164:52242;transport=tcp> Allow: ACK,BYE,CANCEL,INVITE,NOTIFY,OPTIONS,REFER,REGISTER,UPDATE,SUBSCRIBE Content-Length: 201 Content-Type: application/kpml-response+xml Content-Disposition: session;handling=required <?xml version="1.0" encoding="UTF-8"?> <kpml-response xmlns="urn:ietf:params:xml:ns:kpml-response" version="1.0" code="200" text="OK" suppressed="false" forced_flush="false" digits="1" tag="dtmf"/>
```

At this Point system will now initiate a “Call Redirect”. It is used to transfer the call between the system and the agent to the caller at the callback number entered.

```
###$ CfRedirectingDestinationRegister 02305081.000 |10:15:07.835 |SdlSig   | CfRedirectingDestinationRegister |tcc_idle0                      |Cdcc(1,100,219,256)              |Cdcc(1,100,219,251)              |1,100,14,94475.134^10.106.87.164^*       |[R:N-H:0,N:5,L:0,V:0,Z:0,D:0]  orphanedCI= 31614361 collectCodeIfNeeded= 0 02305082.000 |10:15:07.835 |SdlSig   |CcOrphanPauseReq                       |call_active10                  |LineCdpc(1,100,175,271)          |LineControl(1,100,174,554)       |1,100,14,94475.134^10.106.87.164^*       |[R:N-H:0,N:5,L:0,V:0,Z:0,D:0] CI= 31614361 02305082.001 |10:15:07.835 |AppInfo  |LineCdpc(271): -dispatchToOnlySCCPSIPDevices-, sigName=CcOrphanPauseReq, device=TEST_543210 02305083.000 |10:15:07.835 |SdlSig   |CcNotifyReq                            |newpaused                      |LineCdpc(1,100,175,271)          |LineControl(1,100,174,554)       |1,100,14,94475.134^10.106.87.164^*       |[R:N-H:0,N:5,L:0,V:0,Z:0,D:0] CI=31614361 CI.branch=0  lPart= lPatt= lModNum=pi=0si1 lName=locale: 1 Name:  UnicodeName:  pi: 0 cName=locale: 1 Name:  UnicodeName:  pi: 0 cn:pi=0si1 cVMbox= localPatternUsage=2 connectedPatternUsage=2 lCnPart= lCnPatt= rn:pi=0si1 lLRPart= lLRPatt= lOCdpnPart= lOCdpnPatt= oCdpn:pi=0si1 oRFR =0 lBridgePartID= lCnBridgePartID= lHPMemCEPN= cHPMemCEPN= onBehalf=CCtiLine whichSide=0 holdFlag=0 notifyMsg=locale: 1 Name:  UnicodeName:  promptMsg=locale: 1 Name:  UnicodeName:  apply Instr=0 s.sv=0 promptMsg.userLocale=1 cgDevName=TEST_543210 ctiActive=F ctiFarEndDev=0 ctiCCMId=0 CTI event not set. secureStatus=(T,0) callState=5 media=1 bitMask=4000000 Supp DTMF=3DTMF Cfg=1DTMF Payload=101 notifiedDName= connType=0 connStatus=0newPL=5newPLDmn=0 networkDomain= suppressMOH=F triggerByJoin=F NotifInd= ni.niid=39 ni.l=0 ni.nnd=0deviceCepn= partitionSearchSpace= geolocInfo={geolocPkid=, filterPkid=, geolocVal=, devType=4} locPkid= locName= deductBW=F fateShareId= videoTrafficClass=Desktop dtmMcNodeId=0 dtmCurrentCi=0 isOffNetDevice=F ignCntH=F cmDeviceType=4 ssCause=0TransparentData=null CanSupportSIPTandN=false TransId=0 AllowBitMask=0x0 UserAgentOrServer= OrigDDName=locale: 1 Name:  UnicodeName:  pi: 0 mCallerId= mCallerName= FDataType=0opId=0ssType=0 SsKey=0invokeId=0resultExp=Fbpda=F isParamSet=F mobilityEventType=0x0 BibEnabled = 3 MMCap=0x1 CAL={v=-1, m=-1, tDev=F, res=F, devType=0} CAL={v=-10, m=-1, tDev=F, res=F, devType=0} CallInstanceNumber=0 farEndDevName=SEPE8BA70FB6E0A hdrMOH=0 02305083.001 |10:15:07.835 |AppInfo  |LineCdpc(271): -dispatchToAllDevices-, sigName=CcNotifyReq, device=TEST_543210 02305084.000 |10:15:07.835 |SdlSig   |CcNotifyReq                            |call_active10                  |LineCdpc(1,100,175,275)          |LineControl(1,100,174,577)       |1,100,14,94475.134^10.106.87.164^*       |[R:N-H:0,N:5,L:0,V:0,Z:0,D:0] CI=31614366 CI.branch=0  lPart= lPatt= lModNum=pi=0si1 lName=locale: 1 Name:  UnicodeName:  pi: 0 cName=locale: 1 Name:  UnicodeName:  pi: 0 cn:pi=0si1 cVMbox= localPatternUsage=2 connectedPatternUsage=2 lCnPart= lCnPatt= rn:pi=0si1 lLRPart= lLRPatt= lOCdpnPart= lOCdpnPatt= oCdpn:pi=0si1 oRFR =0 lBridgePartID= lCnBridgePartID= lHPMemCEPN= cHPMemCEPN= onBehalf=CCtiLine whichSide=0 holdFlag=0 notifyMsg=locale: 1 Name:  UnicodeName:  promptMsg=locale: 1 Name:  UnicodeName:  apply Instr=0 s.sv=0 promptMsg.userLocale=1 cgDevName=TEST_543210 ctiActive=F ctiFarEndDev=0 ctiCCMId=0 CTI event not set. secureStatus=(T,0) callState=5 media=1 bitMask=4000000 Supp DTMF=1DTMF Cfg=1DTMF Payload=0 notifiedDName= connType=0 connStatus=0newPL=5newPLDmn=0 networkDomain= suppressMOH=F triggerByJoin=F NotifInd= ni.niid=39 ni.l=0 ni.nnd=0deviceCepn= partitionSearchSpace= geolocInfo={geolocPkid=, filterPkid=, geolocVal=, devType=4} locPkid=29c5c1c4-8871-4d1e-8394-0b9181e8c54d locName=Hub_None deductBW=F fateShareId=StandAloneCluster:31614361 videoTrafficClass=Unspecified dtmMcNodeId=0 dtmCurrentCi=0 isOffNetDevice=F ignCntH=F cmDeviceType=4 ssCause=0TransparentData=null CanSupportSIPTandN=false TransId=0 AllowBitMask=0x0 UserAgentOrServer= OrigDDName=locale: 1 Name:  UnicodeName:  pi: 0 mCallerId= mCallerName= FDataType=0opId=0ssType=0 SsKey=0invokeId=0resultExp=Fbpda=F isParamSet=F mobilityEventType=0x0 BibEnabled = 0 MMCap=0x1 CAL={v=-1, m=-1, tDev=F, res=F, devType=0} CAL={v=-10, m=-1, tDev=F, res=F, devType=0} CallInstanceNumber=0 farEndDevName=TEST_543210 hdrMOH=0 02305084.001 |10:15:07.835 |AppInfo  |LineCdpc(275): -dispatchToAllDevices-, sigName=CcNotifyReq, device=SEPE8BA70FB6E0A 02305085.000 |10:15:07.836 |SdlSig   |RSVPSplitSessionReq                    |wait                           |RSVPSession(1,100,107,251)       |ReservationMgr(1,100,110,1)      |1,100,14,94475.134^10.106.87.164^*       |[R:N-H:0,N:5,L:0,V:0,Z:0,D:0] CI= 31614361  aCI=31614361 bCI=31614366 isASerCI=F isBSerCI=F aNodeId=0 bNodeId=0 callState=5 aCacSpecificInfo= CAC_PT_CONNECTED bCacSpecificInfo= CAC_PT_CONNECTED 02305086.000 |10:15:07.836 |SdlSig   |LBMSplitSessionReq                     |active                         |LBMInterface(1,100,176,1)        |ReservationMgr(1,100,110,1)      |1,100,14,94475.134^10.106.87.164^*       |[T:N-H:0,N:0,L:0,V:0,Z:0,D:0] CI= 31614361  aCI=31614361 bCI=31614366 isASerCI=F isBSerCI=F aNodeId=0 bNodeId=0 callState=5 aCacSpecificInfo= CAC_PT_CONNECTED bCacSpecificInfo= CAC_PT_CONNECTED
```

```
###$ DD Happens for Callback number 02305087.006 |10:15:07.836 |AppInfo  |Digit analysis: match(pi="1", fqcn="62151", cn="62151",plv="5", pss="", TodFilteredPss="", dd="08062131",dac="0") 02305087.007 |10:15:07.837 |AppInfo  |Digit analysis: analysis results 02305087.008 |10:15:07.837 |AppInfo  ||PretransformCallingPartyNumber=62151 |CallingPartyNumber=62151 |DialingPartition= |DialingPattern=08062131 |FullyQualifiedCalledPartyNumber=08062131 |DialingPatternRegularExpression=(08062131)
```

After this stage PSTN user or Customer who let a call back number is connected with Agent

## UCCX Log Analysis

Logs analyzed - CCX Engine logs (MIVR) from RTMT.

Call is received on the Trigger 9999 from Customer 2161.

```
### Call received on UCCX trigger 9999 -  Mainline number ### 51269: Apr 08 10:14:27.842 IST %MIVR-SS_TEL-7-UNK:Call.received() JTAPICallContact[id=11,type=Cisco JTAPI Call,implId=29124/1,active=true,state=CALL_RECEIVED,inbound=true,handled=false,locale=en_US,aborting=false,app=App[name=AA,type=Cisco Script Application,id=4,desc=AA, enabled=true,max=4,valid=true,cfg=[ApplicationConfig[schema=ApplicationConfig,time=2016-04-07 07:10:40.0,recordId=53,desc=AA,name=AA,type=Cisco Script Application,id=4,enabled=true,sessions=4,script=SCRIPT[callback.aef],defaultScript=,vars=[<java.lang.String CSQ>,<java.lang.Integer DelayWhileQueued>,<java.lang.String Triggy>],defaultVars=null]]], task=null,session=null,seqNum=-1,time=1460090667841,cn=9999,dn=9999,cgn=2161,ani=null,dnis=null,clid=null,atype=DIRECT,lrd=null,ocn=9999,odn=null,uui=null,aniii=null, ced=null,OrigProtocolCallRef=00000000000071C401E2659700000000,DestProtocolCallRef=null,route=RP[num=9999],port=null,aborting=false,transferring=false,disconnecting=false]
```

The callback script is a simple script that has an accept, select resource step to one of the Callback Agent Queues (from which the agents are selected for the Callback calls).

The call hits the callback mainline number.

Script  1 execution begins.

IMPL ID = 29125, Task ID = 34000000019

```
51338: Apr 08 10:14:27.869 IST %MIVR-ENG-7-UNK:Execute step of Task 34000000019 : Start /* Simple Queuing Template ... */ 51339: Apr 08 10:14:27.869 IST %MIVR-ENG-7-UNK:Execute step of Task 34000000019 : Accept (--Triggering Contact--) 51340: Apr 08 10:14:27.869 IST %MIVR-SS_CM-7-UNK:Making Monitoring flag=true  old flag value =false
```

Call is attributed and the agent is selected for the callback:

```
51349: Apr 08 10:14:27.872 IST %MIVR-SS_TEL-7-UNK:Call.attributed() JTAPICallContact[id=11,type=Cisco JTAPI Call,implId=29124/1,active=true,state=CALL_RECEIVED,inbound=true,handled=false,locale=en_CA,aborting=false,app=App[name=AA,type=Cisco Script Application,id=4,desc=AA,enabled=true,max=4,valid=true,cfg=[ApplicationConfig[schema=ApplicationConfig,time=2016-04-07 07:10:40.0,recordId=53,desc=AA,name=AA,type=Cisco Script Application,id=4,enabled=true,sessions=4,script=SCRIPT[callback.aef],defaultScript=,vars=[<java.lang.String CSQ>,<java.lang.Integer DelayWhileQueued>,<java.lang.String Triggy>],defaultVars=null]]],task=34000000019,session=Session[id=001-0xbdfd63e0c,parent=null,active=true,state=SESSION_IN_USE,time=1460090667843],seqNum=0,time=1460090667841,cn=9999,dn=9999,cgn=2161,ani=null,dnis=null,clid=null,atype=DIRECT,lrd=null,ocn=9999,odn=null,uui=null,aniii=null,ced=null,OrigProtocolCallRef=00000000000071C401E2659800000000,DestProtocolCallRef=null,route=RP[num=9999],port=TP[type=Cisco CTI Port,id=0,implId=543210,active=true,state=IN_USE],aborting=false,transferring=false,disconnecting=false] 51350: Apr 08 10:14:27.872 IST %MIVR-SS_TEL-7-UNK:CallID:11 MediaId:29124/1 Task: associated with Task ID: 34000000019
```

Customer is prompted to enter the Callback number. Here you see that the Prompt Manager plays the prompt to the customer:

```
51498: Apr 08 10:14:29.409 IST %MIVR-LIB_MEDIA-7-UNK:PrPl: appId=4, confId=9, parId=0, channelId=7, channelImplId=7, contactId=11, contactImplId=29124/1 -> PromptPlayer.initializeDataSource() 51499: Apr 08 10:14:29.409 IST %MIVR-LIB_MEDIA-7-UNK:PrPl: appId=4, confId=9, parId=0, channelId=7, channelImplId=7, contactId=11, contactImplId=29124/1 -> play() promptQ.size=1 51501: Apr 08 10:14:29.409 IST %MIVR-LIB_MEDIA-7-UNK:PrPl: appId=4, confId=9, parId=0, channelId=7, channelImplId=7, contactId=11, contactImplId=29124/1 -> startOutput() 51504: Apr 08 10:14:29.415 IST %MIVR-LIB_MEDIA-7-UNK:PrPl: appId=4, confId=9, parId=0, channelId=7, channelImplId=7, contactId=11, contactImplId=29124/1 -> play(). StartOutput() called. 51574: Apr 08 10:14:39.505 IST %MIVR-LIB_MEDIA-7-UNK:PrPl: appId=4, confId=9, parId=0, channelId=7, channelImplId=7, contactId=11, contactImplId=29124/1 -> fileSendDone(), finished=false
```

### Input Stage

Customer then enters the Callback number. Digit received messages in the script.

```
Line 4103: 51617: Apr 08 10:14:46.625 IST %MIVR-SS_TEL-7-UNK:CallID:11 MediaId:29124/1 Task:34000000019 Digit received: 0 Line 4113: 51627: Apr 08 10:14:47.244 IST %MIVR-SS_TEL-7-UNK:CallID:11 MediaId:29124/1 Task:34000000019 Digit received: 8 Line 4118: 51632: Apr 08 10:14:47.793 IST %MIVR-SS_TEL-7-UNK:CallID:11 MediaId:29124/1 Task:34000000019 Digit received: 0 Line 4125: 51639: Apr 08 10:14:48.963 IST %MIVR-SS_TEL-7-UNK:CallID:11 MediaId:29124/1 Task:34000000019 Digit received: 6 Line 4132: 51646: Apr 08 10:14:49.521 IST %MIVR-SS_TEL-7-UNK:CallID:11 MediaId:29124/1 Task:34000000019 Digit received: 2 Line 4137: 51651: Apr 08 10:14:50.017 IST %MIVR-SS_TEL-7-UNK:CallID:11 MediaId:29124/1 Task:34000000019 Digit received: 1 Line 4146: 51660: Apr 08 10:14:50.432 IST %MIVR-SS_TEL-7-UNK:CallID:11 MediaId:29124/1 Task:34000000019 Digit received: 3 Line 4151: 51665: Apr 08 10:14:50.859 IST %MIVR-SS_TEL-7-UNK:CallID:11 MediaId:29124/1 Task:34000000019 Digit received: 1 Line 4158: 51672: Apr 08 10:14:51.559 IST %MIVR-SS_TEL-7-UNK:CallID:11 MediaId:29124/1 Task:34000000019 Digit received: #
```

```
Line 4161: 51675: Apr 08 10:14:51.560 IST %MIVR-STEP_MEDIA_CONTROL-7-UNK:Task:34000000019 GetDigitStringStep (ParseInputStep)(or Extended): Normal Keys collected: 08062131
```

Caller is then disconnected from the UCCX. The call is terminated in the script.

```
Line 4162: 51676: Apr 08 10:14:51.560 IST %MIVR-ENG-7-UNK:Execute step of Task 34000000019 : Terminate (--Triggering Contact--) Line 4165: 51679: Apr 08 10:14:51.566 IST %MIVR-SS_TEL-7-UNK:CallID:11 MediaId:29124/1 Task:34000000019 com.cisco.jtapi.CiscoRTPInputStoppedEvImpl received
```

### Place Call Stage

Call is placed to the trigger (callback ICD script)

```
### makecall() is called with the new CTI port (543210) in a different call control group ### ### trigger 3999 (callback trigger) ### 51700: Apr 08 10:14:51.570 IST %MIVR-ENG-7-UNK:Execute step of Task 34000000019 : cOutbound = Place Call (to Triggy) 51704: Apr 08 10:14:51.570 IST %MIVR-STEP_CALL_CONTROL-7-UNK:Task:34000000019 CreateCall Step Execution 51723: Apr 08 10:14:51.772 IST %MIVR-SS_TEL-7-UNK:CallID:12 MediaId:29125/1 Task:34000000019 makeCall(543210,3999,10000) 51744: Apr 08 10:14:51.778 IST %MIVR-SS_TEL-7-UNK:CallID:12 MediaId:29125/1 Task:34000000019 Got CallActiveEv, ConnCreatedEv 543210::1, ConnConnectedEv 543210::1, CallCtlConnInitiatedEv 543210::1, TermConnCreatedEv TEST_543210, TermConnActiveEv TEST_543210, CallCtlTermConnTalkingEv TEST_543210,  events on the AddressCallObserver. 51752: Apr 08 10:14:51.779 IST %MIVR-SS_TEL-7-UNK:CallID:12 MediaId:29125/1 Task:34000000019 Got CallCtlConnDialingEv 543210::1,  events on the AddressCallObserver. 51758: Apr 08 10:14:51.783 IST %MIVR-SS_TEL-7-UNK:CallID:12 MediaId:29125/1 Task:34000000019 Got CallCtlConnEstablishedEv 543210::1,  events on the AddressCallObserver. 51763: Apr 08 10:14:51.787 IST %MIVR-SS_TEL-7-UNK:CallID:12 MediaId:29125/1 Task:34000000019 connect returns
```

Place call is successful with different media channel group and different call control group from source call.

```
52006: Apr 08 10:14:51.886 IST %MIVR-LIB_MEDIA-7-UNK:PromptPlayer.setTxDestination() Inside set Tx Destination 52007: Apr 08 10:14:51.886 IST %MIVR-LIB_MEDIA-7-RTP_PROPERTIES_REASSIGNED:RTP Properties Reassigned: Method Name=setTxDestination(),HOST NAME=10.106.87.133,PORT NUMBER=24694,PACKET SIZE=20 52008: Apr 08 10:14:51.886 IST %MIVR-LIB_MEDIA-7-UNK:PrPl: appId=4, confId=10, parId=0, channelId=1, channelImplId=1, contactId=12, contactImplId=29125/1 -> setTxDestination: payloadType=4 52009: Apr 08 10:14:51.886 IST %MIVR-SS_TEL-7-UNK:CallID:12 MediaId:29125/1 Task:34000000019 makeCall is SUCCESSFUL, Conns length =2
```

Script 2 execution begins. This is a ghost call.

IMPL ID = 29125, TASK ID = 34000000023

CTI port in accept step = 4003

```
51917: Apr 08 10:14:51.853 IST %MIVR-SS_TEL-7-UNK:Call.attributed() JTAPICallContact[id=13,type=Cisco JTAPI Call,implId=29125/1,active=true,state=CALL_RECEIVED,inbound=true,handled=false,locale=en,aborting=false,app=App[name=ICD,type=Cisco Script Application,id=0,desc=ICD,enabled=true,max=10,valid=true,cfg=[ApplicationConfig[schema=ApplicationConfig,time=2016-03-22 17:58:01.0,recordId=43,desc=ICD,name=ICD,type=Cisco Script Application,id=0,enabled=true,sessions=10,script=SSCRIPT[icd.aef],defaultScript=,vars=[<java.lang.String CSQ>],defaultVars=null]]],task=34000000023,session=Session[id=001-0xbdfd63e0d,parent=null,active=true,state=SESSION_IN_USE,time=1460090691771],seqNum=1,time=1460090691790,cn=3999,dn=3999,cgn=543210,ani=null,dnis=null,clid=null,atype=DIRECT,lrd=null,ocn=3999,odn=null,uui=null,aniii=null,ced=null,OrigProtocolCallRef=00000000000071C501E2659B00000000,DestProtocolCallRef=null,route=RP[num=3999],port=TP[type=Cisco CTI Port,id=5,implId=4003,active=true,state=IN_USE],aborting=false,transferring=false,disconnecting=false] 51918: Apr 08 10:14:51.853 IST %MIVR-SS_TEL-7-UNK:CallID:13 MediaId:29125/1 Task:34000000023 associated with Task ID: 34000000023
```

Agent agent5 is in ready state and ready to accept the call. Consult transfer to agent's phone 62151.

```
Line 4544: 52028: Apr 08 10:14:51.889 IST %MIVR-ENG-7-UNK:Execute step of Task 34000000023 : Play Prompt (--Triggering Contact--, WelcomePrompt) Line 4545: 52029: Apr 08 10:14:51.890 IST %MIVR-STEP_MEDIA_CONTROL-7-UNK:Task:34000000023 Executing OutputStep Line 4546: 52030: Apr 08 10:14:51.890 IST %MIVR-STEP_MEDIA_CONTROL-7-UNK:Task:34000000023 OutputStep: myExecute Line 4577: 52061: Apr 08 10:14:53.397 IST %MIVR-ENG-7-UNK:Execute step of Task 34000000023 : Select Resource (--Triggering Contact-- from CSQ) Line 4648: 52087: Apr 08 10:14:53.403 IST %MIVR-SS_TEL-7-UNK:CallID:13 MediaId:29125/1 Task:34000000023, transfer(62151, 12000, ACKNOWLEDGED)
```

Agent gets the call from CTI port 4003. The agent phone is 62151.

```
52165: Apr 08 10:14:53.447 IST %MIVR-SS_RM-7-UNK:RIMgrAddressCallObserver: CallCtlConnEstablishedEv received for call:16806342 [29126/1], address 4003, calling party 4003, and called party 62151 52166: Apr 08 10:14:53.447 IST %MIVR-SS_RM-7-UNK:RIMgrAddressCallObserver: CallCtlConnEstablishedEv received for call 16806342 [29126/1] and agent null being ignored because orig isn't a logged in agent
```

```
Line 4953: 52392: Apr 08 10:14:59.245 IST %MIVR-SS_TEL-7-UNK:OrigCall=CallID:13 MediaId:29125/1 Task:34000000023, ConsultEvent= CallObservationEndedEv Line 4955: 52394: Apr 08 10:14:59.245 IST %MIVR-SS_TEL-7-UNK:CallID:13 MediaId:29125/1 Task:34000000023, transfer(62151, consultCall)
```

```
52678: Apr 08 10:14:59.325 IST %MIVR-SS_TEL-7-UNK: Call.transferred(62151) - transferring JTAPICallContact[id=13,type=Cisco JTAPI Call,implId=29125/1,active=false,state=CALL_CONNECTED,inbound=true,handled=false,locale=en,aborting=false,app=App[name=ICD,type=Cisco Script Application,id=0,desc=ICD,enabled=true,max=10,valid=true,cfg=[ApplicationConfig[schema=ApplicationConfig,time=2016-03-22 17:58:01.0,recordId=43,desc=ICD,name=ICD,type=Cisco Script Application,id=0,enabled=true,sessions=10,script=SSCRIPT[icd.aef],defaultScript=,vars=[<java.lang.String CSQ>],defaultVars=null]]],task=34000000023,session=null,seqNum=-1,time=1460090691790,cn=3999,dn=3999,cgn=543210,ani=null,dnis=null,clid=null,atype=DIRECT,lrd=null,ocn=3999,odn=null,uui=null,aniii=null,ced=null,OrigProtocolCallRef=00000000000071C501E2659E00000000,DestProtocolCallRef=null,route=RP[num=3999],port=TP[type=Cisco CTI Port,id=5,implId=4003,active=false,state=IDLE],aborting=false,transferring=true,disconnecting=false] 52679: Apr 08 10:14:59.326 IST %MIVR-SS_TEL-7-UNK:CallID:13 MediaId:29125/1 Task:34000000023, released TP[type=Cisco CTI Port,id=5,implId=4003,active=false,state=IDLE] from 3999, and releasing udpPort 24694 52680: Apr 08 10:14:59.326 IST %MIVR-SS_TEL-7-UNK:CallID:13 MediaId:29125/1 Task:34000000023 com.cisco.jtapi.TermObservationEndedEvImpl received
```

At this point, the agent is connected to the ghost CTI port 543210 now and the Script 1 is waiting for the Agent to press any key to make the call to the customer. The agent is in a talking state with the CTI port at this point.

Optionally at this stage, the script can also play a message back to the agent about the customer. However, script 1 is waiting for a digit to be pressed to perform a call redirect to the Caller's Callback number entered and saved .

Script 1 waiting for digit to be entered:

```
52014: Apr 08 10:14:51.887 IST %MIVR-ENG-7-UNK:Execute step of Task 34000000019 : AnyDigit = Get Digit String (cOutbound) 52015: Apr 08 10:14:51.887 IST %MIVR-STEP_MEDIA_CONTROL-7-UNK:Task:34000000019 Executing GetDigitStringStep (ParseInputStep) 52016: Apr 08 10:14:51.887 IST %MIVR-STEP_MEDIA_CONTROL-7-UNK:Task:34000000019 GetDigitStringStep (ParseInputStep): myExecute
```

Agent presses a key. Presses digit 1 to confirm callback initiate:

```
52820: Apr 08 10:15:07.375 IST %MIVR-SS_TEL-7-UNK:CallID:12 MediaId:29125/1 Task:34000000019 Digit received: 1 52821: Apr 08 10:15:07.375 IST %MIVR-LIB_MEDIA-7-UNK:PrPl: appId=4, confId=10, parId=0, channelId=1, channelImplId=1, contactId=12, contactImplId=29125/1 -> stopPlay() called. 52825: Apr 08 10:15:07.785 IST %MIVR-SS_CMT-7-UNK:process digit 1 52826: Apr 08 10:15:07.786 IST %MIVR-SS_CMT-7-UNK:MediaDialogChannel id=1,state=IN_USE MDC::clear com.cisco.wf.cmt.dialogs.CMTSimpleDigitStringDialogImpl@2a90df abortWaiting=false 52827: Apr 08 10:15:07.786 IST %MIVR-STEP_MEDIA_CONTROL-7-UNK:Task:34000000019 GetDigitStringStep (ParseInputStep)(or Extended): Normal Keys collected: 1
```

Call is redirected to the callback number:

```
52828: Apr 08 10:15:07.786 IST %MIVR-ENG-7-UNK:Execute step of Task 34000000019 : Call Redirect (cOutbound to Callbacknumber) 52829: Apr 08 10:15:07.786 IST %MIVR-STEP_CALL_CONTROL-7-UNK:Task:34000000019 Executing RedirectStep (CallRedirect), reset:true 52830: Apr 08 10:15:07.787 IST %MIVR-SS_TEL-7-UNK:CallID:12 MediaId:29125/1 Task:34000000019, Redirecting to: 08062131, Unconditional: false, ResetOrigCalledAddr:false, OrigCalledAddr:08062131, CallingSearchSpace:redirecting.party 52831: Apr 08 10:15:07.794 IST %MIVR-SS_TEL-7-UNK:Received Event :com.cisco.jtapi.CiscoRTPInputStoppedEvImpl 52832: Apr 08 10:15:07.795 IST %MIVR-SS_TEL-7-UNK:CallID:12 MediaId:29125/1 Task:34000000019 com.cisco.jtapi.CiscoRTPInputStoppedEvImpl received
```

Agent phone and Callback number are connected to one another:

```
Line 5474: 52884: Apr 08 10:15:08.048 IST %MIVR-SS_TEL-7-UNK:Call.abandoned() - transferring JTAPICallContact[id=12,type=Cisco JTAPI Call,implId=29125/1,active=true,state=CALL_ANSWERED,inbound=false,handled=false,locale=en_US,aborting=false,app=App[name=AA,type=Cisco Script Application,id=4,desc=AA,enabled=true,max=4,valid=true,cfg=[ApplicationConfig[schema=ApplicationConfig,time=2016-04-07 07:10:40.0,recordId=53,desc=AA,name=AA,type=Cisco Script Application,id=4,enabled=true,sessions=4,script=SCRIPT[callback.aef],defaultScript=,vars=[<java.lang.String CSQ>,<java.lang.Integer DelayWhileQueued>,<java.lang.String Triggy>],defaultVars=null]]],task=34000000019,session=Session[id=001-0xbdfd63e0d,parent=null,active=true,state=SESSION_IN_USE,time=1460090691771],seqNum=0,time=1460090691577,cn=3999,dn=null,cgn=543210,ani=null,dnis=null,clid=null,atype=OUTBOUND,lrd=null,ocn=3999,odn=null,uui=null,aniii=null,ced=null,OrigProtocolCallRef=null,DestProtocolCallRef=00000000000071C501E2659900000000,route=RP[num=0000],... Line 5479: 52889: Apr 08 10:15:08.051 IST %MIVR-STEP_CALL_CONTROL-7-UNK:Task:34000000019 RedirectStep (CallRedirect): OriginalCalledAddressExpr Selected: Destination
```

```
Line 5510: 52898: Apr 08 10:15:08.053 IST %MIVR-SS_TEL-7-UNK:Call.transferred(08062131) - transferring JTAPICallContact[id=12,type=Cisco JTAPI Call,implId=29125/1,active=false,state=CALL_TRANSFERRED,inbound=false,handled=false,locale=en_US,aborting=false,app=App[name=AA,type=Cisco Script Application,id=4,desc=AA,enabled=true,max=4,valid=true,cfg=[ApplicationConfig[schema=ApplicationConfig,time=2016-04-07 07:10:40.0,recordId=53,desc=AA,name=AA,type=Cisco Script Application,id=4,enabled=true,sessions=4,script=SCRIPT[callback.aef],defaultScript=,vars=[<java.lang.String CSQ>,<java.lang.Integer DelayWhileQueued>,<java.lang.String Triggy>],defaultVars=null]]],task=34000000019,session=Session[id=001-0xbdfd63e0d,parent=null,active=true,state=SESSION_IN_USE,time=1460090691771],seqNum=0,time=1460090691577,cn=3999,dn=null,cgn=543210,ani=null,dnis=null,clid=null,atype=OUTBOUND,lrd=null,ocn=3999,odn=null,uui=null,aniii=null,ced=null,OrigProtocolCallRef=null,DestProtocolCallRef=00000000000071C501E2659900000000,route...
```

```
Line 5511: 52899: Apr 08 10:15:08.053 IST %MIVR-SS_TEL-7-UNK:CallID:12 MediaId:29125/1 Task:34000000019, released TP[type=Cisco CTI Port,id=0,implId=543210,active=false,state=IDLE] from 0000, and releasing udpPort 24692
```