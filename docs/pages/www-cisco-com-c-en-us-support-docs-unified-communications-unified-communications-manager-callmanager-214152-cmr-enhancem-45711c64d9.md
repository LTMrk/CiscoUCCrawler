---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-214152-cmr-enhancem-45711c64d9
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/214152-cmr-enhancement-in-cucm-12-5.html
retrieved_at: 2026-08-21T13:58:25.998691+00:00
---

CMR Enhancement in CUCM 12.5

# CMR Enhancement in CUCM 12.5

### Download Options

Updated: December 28, 2020

Document ID: 214152

Contents

## Contents

## Introduction

This document describes the Call Management Records ( CMR) enhancements on Cisco Unified Communications Manager (CUCM) 12.5.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUCM version 12.5

- Enable Call Details Record (CDR) and CMR on CallManager

### Components Used

The information in this document is based on Cisco Call Manager version 12.5

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

CUCM produces two types of records, which store call history and diagnostic information:

- Call Detail Records- Data records contain information about each call which is processed by CallManager.

- Call Management Records - Data records contain the Quality of Service (QoS) or diagnostic information about the call, also referred to as diagnostic records.

Both CDRs and CMRs together are referred to as CDR data. CDR data provides a record of all calls that have been made or received by users of the CallManager system. CDR data is useful primarily to generate the billing records; however, it can also be used to track call activity, diagnose certain types of problems and capacity plan.

CMRs contain information about the amount of data sent and received, jitter, latency, and lost packets. Initially, CMR was generated for internal calls, now CUCM can generate CMR for calls over SIP trunk.

SIP Trunk receives the call statistics in P-RTP-Stat header in the BYE message or in the 200 OK messages (response to BYE message) from CUBE or IOS Gateway. These statistics include Real-time Transport Protocol (RTP) packets sent or received, total bytes sent or received, the total number of packets that are lost, delay jitter, round-trip delay, and call duration.

The format of P-RTP-Stat Header:

P-RTP-Stat: PS=<Packets Sent>, OS=<Octets Sent>, PR=<Packets Recd>, OR=<Octets Recd>,PL=<Packets Lost>, JI=<Jitter>, LA=<Round Trip Delay in ms>, DU=<Call Duration in seconds>

It is the format of CUBE/SIP IOS gateway RTP Statistics reporting. CUCM SIP Trunk side for CMR support is limited to that format of RTP Statistics.

- After BYE or 200OK for BYE is received, SIPCdpc parses the P-RTP-Stat header and populates the corresponding CMR fields based on Key values pairs in P-RTP-Stat header.

- SIPCdpc sends the Diagnostic record to EnvProcessCdr with populated CMR data, and EnvProcessCdr creates a flat file and dumps CMR data into it.

- No new fields are added to the CMR as part of this feature. Existing format to be maintained.

- Any fields in the CMR that are not relevant for trunk side metrics (like DirectoryNumber etc.) to be left at null, similarly for metrics not received from CUBE (e.g. varVQMetrics or video metrics) to be left at null.

- If the P-RTP-Stat header is not received from the CUBE for BYE message or 200 OK (response to BYE), there will be no CMR record written for the SIPTrunk.

Prerequisite from CUBE to support this feature / provide call statistics :

- Cisco IOS Release 15.1(3)T or a later release must be installed and should run on your Cisco Unified Border Element.

- Cisco IOS XE Release 3.3S or a later release must be installed and should run on your Cisco ASR 1000 Series Router.

## Configurations

Step 1. CMR is Enabled via Call Manager service parameters under :

- Navigate to System > Service Parameter.

- Select a server from the drop-down box and then select the Call Manager service

Step 2. Set the Call Diagnostics Enabled parameter to either:

Enabled Only When CDR Enabled Flag is True (generate CMRs only when the CDR Enabled Flag service parameter is set to True).

Enabled regardless of CDR Enabled Flag (generates CMRs without regard to the setting in the CDR Enabled Flag service parameter).

### Trace Analysis

```
** Incoming BYE from Gateway :

00802148.002 |16:17:01.297 |AppInfo  |//SIP/SIPUdp/wait_SdlDataInd: Incoming SIP UDP message size 539 from 10.106.97.143:[49193]:

[151,NET]

BYE sip:2000@10.106.97.132:5060 SIP/2.0

Via: SIP/2.0/UDP 10.106.97.143:5060;branch=z9hG4bKB41E87

From: <sip:7001@10.106.97.143>;tag=7780842C-12C9

To: <sip:2000@10.106.97.132>;tag=23~30c1033e-90ea-45e0-b1da-eec4a4bfbd�6e-21411553

Date: Tue, 05 Feb 2019 10:03:29 GMT

Call-ID: 1F09F649-286411E9-81B2A4AF-FAF6B880@10.106.97.143

User-Agent: Cisco-SIPGateway/IOS-15.5.3.M5

Max-Forwards: 70

Timestamp: 1549361022

CSeq: 103 BYE

Reason: Q.850;cause=16

P-RTP-Stat: PS=300,OS=48000,PR=365,OR=58400,PL=0,JI=0,LA=0,DU=7

Content-Length: 0

** Post SIPDisconnect Indication, SIPCdpc collects the data

00802151.000 |16:17:01.297 |SdlSig   |SIPDisconnInd                          |active                         |SIPCdpc(1,100,180,5)             |SIPD(1,100,181,1)                |1,100,255,1.62^10.106.97.143^*           |[R:N-H:0,N:0,L:0,V:0,Z:0,D:0]  CcbId= 2�3 --TransType=2 --TransSecurity=0 PeerAddr = 10.106.97.143:49193 Sip_disc_cause= 200 cause=16 isReasonHdrVal= T

00802151.001 |16:17:01.297 |AppInfo  |(isHeldOrHolding): holder=0,holdee=0,mh=0

00802151�.002 |16:17:01.297 |AppInfo  |SIPCdpc(5) - collect_proxyMetricsData: Filling the Audio diagnostic record for the CMR coming from proxy ...

00802151.003 |16:17:01.297 |AppInfo  |SIPCdpc(5) - collect_proxyMetricsData: Audio diagnostics: pktSend = 300, pktSendOct = 48000, pktRec = 365, pktRecOct = 58400, pktLoss = 0, jitter = 0, delay = 0

 

** SIPCdpc sends the data to CDR process to generate CMR

00802193.000 |16:17:01.315 |SdlSig   |DbDiagnosticsReq                       |wait                           |EnvProcessCdr(1,100,6,1)         |SIPCdpc(1,100,180,5)             |1,100,255,1.62^10.106.97.143^*           |[T:N-H:0,N:0,L:0,V:0,Z:0,D:0]  globalCallId: 5 nodeId: 1 directoryNum:  dateTime: 1549363621 numberPa�cketsSent: 300 numberOctetsSent: 48000 numberPacketsReceived: 365 numberOctetsReceived: 58400 numberPacketsLost: 0 jitter: 0 latency: 0 varVQMetrics:

00802252.001 |16:17:01.621 |AppInfo  |EnvProcessCdr::wait_DbDiagnosticsReq

00802252.002 |16:17:01.621 |AppInfo  |EnvProcessCdr::wait_DbDiagnosticsReq DETAILED Entries 2, Inserts 2, ZeroCalls 0

00802252.003 |16:17:01.621 |AppInfo  |EnvProcessCdr::outputCmrData CMR data - 2,1,5,1,"2000",21411554,1549363621,2967,59340,0,0,0,0,0,"1e44e506-9a5d-4f0a-af2c-de23a7405123","","StandAloneCluster","SEPeeeeeeeeeeee","",,"",,,,,,,,,,"","","",,,,,,,,,,"",""
```

The above CMR data is pushed into the file in below repository activelog/cm/cdr_repository/processed/<current date>/

```
admin:file list activelog cm/cdr_repository/processed/20190205/*

cmr_StandAloneCluster_01_201902051047_0

dir count = 0, file count = 1
```

## Verify

From cli, you can verify whether CMR is generated or not. For every date, there is a folder created in the format <yyyymmdd>

```
admin:file list activelog cm/cdr_repository/processed/20190205/*

cmr_StandAloneCluster_01_201902051047_0

dir count = 0, file count = 1
```

## Troubleshoot

### P-RTP-Stat header is Received in BYE/200OK, but CMR Data is not Generated

```
<Sample BYE message >

00802148.002 |16:17:01.297 |AppInfo  |//SIP/SIPUdp/wait_SdlDataInd: Incoming SIP UDP message size 539 from 10.106.97.143:[49193]:

[151,NET]

BYE sip:2000@10.106�.97.132:5060 SIP/2.0

Via: SIP/2.0/UDP 10.106.97.143:5060;branch=z9hG4bKB41E87

From: <sip:7001@10.106.97.143>;tag=7780842C-12C9

To: <sip:2000@10.106.97.132>;tag=23~30c1033e-90ea-45e0-b1da-eec4a4bfbd�6e-21411553

Date: Tue, 05 Feb 2019 10:03:29 GMT

Call-ID: 1F09F649-286411E9-81B2A4AF-FAF6B880@10.106.97.143

User-Agent: Cisco-SIPGateway/IOS-15.5.3.M5

Max-Forwards: 70

Timestamp: 1549361022

CSeq:� 103 BYE

Reason: Q.850;cause=16

P-RTP-Stat: PS=300,OS=48000,PR=365,OR=58400,PL=0,JI=0,LA=0,DU=7

Content-Length: 0
```

Workaround:

Check if Call Diagnostics Enabled SP is enabled.

### P-RTP-Stat Header is Present but CMR is not Recorded

```
<Sample BYE message >

BYE sip:45002@10.77.29.45:5062 SIP/2.0

Via: SIP/2.0/UDP 10.77.22.123:5062;branch=z9hG4bK-11920-1-7

From: sipp <sip:sipp@10.77.22.123:5062>;tag=1

To: sut <sip:45002@10.77.29.45:5062>;tag=2085~b5883d68-042a-4a73-adc3-6be8a5f9f263-24253136

Call-ID: 1-15504@10.77.22.123

CSeq: 1 BYE

Allow-Events: presence, kpml

Contact: sip:sipp@10.77.22.123:5062

Content-Length: 0

P-RTP-Stat: PS=nodata, OS=nodata, PR=nodata, OR=nodata, PL=1, JI=3, LA=0.03, DU=76
```

Reason:

Since numberPacketsSent and numberPacketsReceived both are invalid, CMR data is not dumped into the file for SIP Trunk.

### CMR Data is Generated from P-RTP-Stat header but some Values are wrongly Recorded

```
<Sample BYE message >

BYE sip:45002@10.77.29.45:5062 SIP/2.0

Via: SIP/2.0/UDP 10.77.22.123:5062;branch=z9hG4bK-11920-1-7

From: sipp <sip:sipp@10.77.22.123:5062>;tag=1

To: sut <sip:45002@10.77.29.45:5062>;tag=2085~b5883d68-042a-4a73-adc3-6be8a5f9f263-24253136

Call-ID: 1-15504@10.77.22.123

CSeq: 1 BYE

Allow-Events: presence, kpml

Contact: sip:sipp@10.77.22.123:5062

Content-Length: 0

P-RTP-Stat: PS=4294967298, OS=1234, PR=4294967298, OR=1233, PL=1, JI=3, LA=0.03, DU=76
```

Reason:

Since PS and PR values are out of range(values greater than 2^32-1), these out of range values are replaced with max value i.e. 2^32-1(4294967295).

### Allowed Keys and Range of Values in the P-RTP-Stat Header

## Feature Limitations

This feature is not supported for SME call flows:

- Upon receiving call statistics from CUBE/IOS GW on SME,CUCM will generate CMR (provided CMR is enabled) for trunk side, but it won’t be able to forward call statistics to other nodes in outgoing BYE or 200OK for BYE.

- Sample Call flow: Phone1 >> CUBE/IOS GW>> SME >> CUCM1 >> Phone2 For the above call scenario, SME will generate the CMR for trunk side pointing to CUBE . These statistics will not be forwarded to leaf node. For Phone2, CMR will be recorded on leaf node.

### Contributed by Cisco Engineers

Divya Jain

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)