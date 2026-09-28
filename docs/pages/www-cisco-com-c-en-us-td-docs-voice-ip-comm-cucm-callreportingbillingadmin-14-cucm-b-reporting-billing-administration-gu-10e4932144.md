---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-callreportingbillingadmin-14-cucm-b-reporting-billing-administration-gu-10e4932144
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/callReportingBillingAdmin/14/cucm_b_reporting-billing-administration-guide-14/cucm_b_reporting-and-billing-administration-guide_chapter_01100.html
retrieved_at: 2026-08-17T00:26:59.510410+00:00
---

Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: April 9, 2026

Chapter: Call Management Records

## Chapter: Call Management Records

# Call Management Records

This chapter describes the format and logic of the call management records (CMRs) that the Unified Communications Manager
                           system generates, and how to access the CMR files.

## Call Management Records Overview

The Unified Communications Manager system generates call management records (CMRs). You can use this information for post-processing activities such as generating
                              billing records and network analysis.

When you install your system, CMRs remain disabled by default, you can enable or disable CMRs at any time that the system
                              is in operation. You do not need to restart Unified Communications Manager for the change to take the effect. The system responds to all changes within a few seconds. The system enables CMR or diagnostic
                              data separately from CDR data.

## CMR Processing

The CMR records store information about the quality of the streamed audio and video of the call.

When Unified Communications Manager places or receives a call, the system generates a CDR record when the call terminates. The system writes the CDR to a flat
                              file (text file). Inside the Unified Communications Manager , the call control process generates CDR records. The system writes records when significant changes occur to a given call,
                              such as ending the call, transferring the call, redirecting the call, splitting the call, joining a call, and so forth.

When CMR records are enabled, the number of records that are written varies by type of call and the call scenario. When Diagnostics
                              are enabled, the device generates CMR records for each call. The system writes one CMR record for each IP phone that is involved
                              in the call or for each Media Gateway Control Protocol (MGCP) gateway. The system sends these records to EnvProcessCdr where
                              they get written to flat files.

For Hold and Resume calls on SCCP devices, multiple CMR Records are generated based on the number of times the call is put
                                          on hold.

The Unified Communications Manager generates CMR records but does not perform any post processing on the records. The system writes the records to comma-delimited
                              flat files and periodically passes them to the CDR Repository. The CMR files represent a specific filename format within the
                              flat file.

### Filename Format

The following example shows the full format of the filename: tag_clusterId_nodeId_datetime_seqNumber

tag—Identifies the type of file, either CDR or CMR.

clusterId—Identifies the cluster or server where the Unified Communications Manager database exists.

nodeId—Identifies the node.

datetime—Specifies UTC time in yyyymmddhhmm format.

seqnumber—Specifies sequence number.

An example of the filename follows:

cmr_Cluster1_02_200404061011_6125

### Flat File Format

The CMR flat files have the following format:

Line 1—List of field names in comma separated format.

Line 2—List of field types in comma separated format.

Line 3—Data in comma separated format.

Line 4—Data in comma separated format.

The following example shows a flat file:

```
Line1- "cmrRecordType" , "globalCallID_callManagerId" , "globalCallID_callId" , "origLegCallIdentifier" ,...
Line2-INTEGER,INTEGER,INTEGER,INTEGER,...
Line3-1,1,388289,17586046,...
Line4-1,1,388293,17586054,...
```

## CMRs for SIP Trunks

Unified Communications Manager stores end-of-call video and audio information and metrics in Call Management Records (CMRs)
                              for incoming and outgoing SIP trunk calls through Cisco Unified Border Element (CUBE) or SIP IOS gateways.

CUBE sends the call statistics in a P-RTP-Stat header either in a BYE message or a 200 OK response to BYE message to update
                              the CMRs in Unified Communications Manager.

When the call is routed through a Session Manager Edition (SME), call statistics sent by CUBE are recorded in the CMRs generated
                              on the SME than the LEAF cluster.

CMRs are generated by Unified Communications Manager when Call Diagnostics Enabled service parameter is enabled.

### P-RTP Stat Format

The format of P-RTP-Stat is as follows:

P-RTP-Stat: PS=<Packets Sent>, OS=<Octets Sent>, PR=<Packets Recd>, OR=<Octets Recd>, PL=<Packets Lost>, JI=<Jitter>, LA=<Round
                              Trip Delay in ms>, DU=<Call Duration in seconds>

The following table describes the P-RTP-Stat header fields:

Field

Description

PS

Packets Sent

OS

Octets Sent

PR

Packets Received

OR

Octets Received

PL

Packets Lost

JI

Jitter

LA

Round-Trip Delay in milliseconds (ms)

DU

Call Duration in seconds

### Example

The following example shows the sample BYE message with a P-RTP-Stat header.

Sample BYE Message

```
BYE sip:45002@209.165.201.1:5060;transport=tcp SIP/2.0
Via: SIP/2.0/TCP 209.165.200.225:5060;branch=z9hG4bK1a2f5c92d361
From:<sip:1006@209.165.200.225>;tag=12734~95fd5a73-11ac-4642-9308-401b17a658fb-17711590
To:<sip:45002@209.165.201.1;tag=445~b5883d68-042a-4a73-adc3-6be8a5f9f263-25068153
Date: Fri, 13 Oct 2017 04:29:38 GMT
Call-ID: 1e4d2a80-9e014132-6e2-e11f4d0a@209.165.200.225
User-Agent: Cisco-CUCM12.5
P-Asserted-Identity: <sip:1006@209.165.200.225>
CSeq: 102 BYE
Reason: Q.850;cause=16
Session-ID: 97173553334349d0a9391305caa12733;remote=49fd996b345a4745b9db7f242ddaa446
Content-Length: 0 P-RTP-Stat: PS=3775,OS=649300,PR=3775,OR=604000,PL=0,JI=0,LA=4,DU=98
```

Corresponding Sample Call Management Records

```
"cdrRecordType","globalCallID_callManagerId","globalCallID_callId","nodeId","directoryNum",
"callIdentifier","dateTimeStamp","numberPacketsSent","numberOctetsSent","numberPacketsReceived"
"numberOctetsReceived","numberPacketsLost","jitter","latency","pkid","directoryNumPartition",
"globalCallId_ClusterID","deviceName","varVQMetrics","duration","videoContentType","videoDuration",
"numberVideoPacketsSent","numberVideoOctetsSent","numberVideoPacketsReceived","numberVideoOctetsReceived",
"numberVideoPacketsLost","videoAverageJitter","videoRoundTripTime","videoOneWayDelay","videoReceptionMetrics",
"videoTransmissionMetrics","videoContentType_channel2","videoDuration_channel2","numberVideoPacketsSent_channel2",
"numberVideoOctetsSent_channel2","numberVideoPacketsReceived_channel2","numberVideoOctetsReceived_channel2",
"numberVideoPacketsLost_channel2","videoAverageJitter_channel2","videoRoundTripTime_channel2","videoOneWayDelay_channel2",
"videoReceptionMetrics_channel2","videoTransmissionMetrics_channel2" INTEGER,INTEGER,INTEGER,INTEGER,VARCHAR(50),
INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,UNIQUEIDENTIFIER,VARCHAR(50),VARCHAR(50),
VARCHAR(129),VARCHAR(600),INTEGER,VARCHAR(10),INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,
INTEGER,VARCHAR(600),VARCHAR(600),VARCHAR(10),INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,INTEGER,
VARCHAR(600),VARCHAR(600) 2,1,48553,1,"",29258891,1515145049, 3775,649300,3775,604000,0,0,4 ,"50870a6d-193d-478f-8971-0dc641a6058a",
"","StandAloneCluster","sip_trunk3_to_camserv_2_DO","", 98 ,"",,,,,,,,,,"","","",,,,,,,,,,"",""
2,1,48553,1,"11011",29258890,1515145049,8900,7676700,8998,7676767,0,2,0,"7526cf73-ae78-48b1-9640-7ea19b546321","",
"StandAloneCluster","SEPCD1111000011","",98,"main",0,0,0,0,0,0,0,0,0,"","TxFrameRate=0","",,,,,,,,,,"",""
```

In the preceding example, Unified Communications Manager inserts the call statistics into the CMRs per the communicated information
                              in the P-RTP-Stat header. If a P-RTP-Stat header comprises partial field values or any field is absent, Unified Communications
                              Manager generates CMRs with available field values.

Some of the fields in the CMRs are not populated due to fields unrelated to SIP trunk or if no call statistics are received
                                          from CUBE.

In the following scenarios, there are no CMRs written for the SIP trunk:

P-RTP-Stat header is present without any fields in an incoming BYE message or 200 OK response to BYE message from CUBE.

P-RTP-Stat header is not present in an incoming BYE message or 200 OK response to BYE message from CUBE.

P-RTP-Stat header and fields are present in an incoming BYE message or 200 OK response to BYE message from CUBE but corresponding
                                    field values are empty.

## CMRs for Headsets

Unified Communications Manager stores the call diagnostics details for Headsets. The details include call quality, packets
                           lost, packets received, jitter, delay, and so on. Whenever there is a call between two phones using headsets, the diagnostics
                           records for both the headsets populates separately in a column ‘Headset-Stat’. You can view the Serial Number and Metrics
                           of the particular Headset used.

### Example

The following example shows the sample BYE message for Headsets:

```
BYE sip:1@10.77.29.46:5060;transport=tcp SIP/2.0
RTP-TxStat: Dur=13,Pkt=658,Oct=105280
Date: Thu, 10 Jan 2019 06:22:08 GMT
From: "1020" <sip:1020@10.77.29.46>;tag=e0899d9508fc00064e7fc5d0-264cc0f8
Content-Length: 0
User-Agent: Cisco-CP9971/9.4.2
User-Agent: Cisco-CP9971/9.4.2
To: <sip:1@10.77.29.46>;tag=38869~03b645d3-522f-428d-a380-425f3fdaed66-28473124
Call-ID: e0899d95-08fc0003-44f9a213-39b10eeb@10.77.36.21
Via: SIP/2.0/TCP 10.77.36.21:51918;branch=z9hG4bK7a47320e
CSeq: 102 BYE Headset-Stat: SN=AAA111BBB222, Metrics="Key=value;Key1=Value1Key=value;" Max-Forwards: 70
RTP-RxStat: 
Dur=13,Pkt=657,Oct=113004,LatePkt=0,LostPkt=0,AvgJit=1,VQMetrics="MLQK=4.5000;MLQKav=4.5000;
MLQKmn=4.5000;MLQKmx=4.5000;MLQKvr=0.95;CCR=0.0000;ICR=0.0000;ICRmx=0.0000;CS=0;SCS=0"
```

## CMRs for Headsets

Unified Communications Manager stores the call diagnostics details for Headsets. The details include call quality, packets
                           lost, packets received, jitter, delay, and so on. Whenever there is a call between two phones using headsets, the diagnostics
                           records for both the headsets populates separately in a column ‘Headset-Stat’. You can view the Serial Number and Metrics
                           of the particular Headset used.

### Example

The following example shows the sample BYE message for Headsets:

```
BYE sip:1@10.77.29.46:5060;transport=tcp SIP/2.0
RTP-TxStat: Dur=13,Pkt=658,Oct=105280
Date: Thu, 10 Jan 2019 06:22:08 GMT
From: "1020" <sip:1020@10.77.29.46>;tag=e0899d9508fc00064e7fc5d0-264cc0f8
Content-Length: 0
User-Agent: Cisco-CP9971/9.4.2
User-Agent: Cisco-CP9971/9.4.2
To: <sip:1@10.77.29.46>;tag=38869~03b645d3-522f-428d-a380-425f3fdaed66-28473124
Call-ID: e0899d95-08fc0003-44f9a213-39b10eeb@10.77.36.21
Via: SIP/2.0/TCP 10.77.36.21:51918;branch=z9hG4bK7a47320e
CSeq: 102 BYE Headset-Stat: SN=AAA111BBB222, Metrics="Key=value;Key1=Value1Key=value;" Max-Forwards: 70
RTP-RxStat: 
Dur=13,Pkt=657,Oct=113004,LatePkt=0,LostPkt=0,AvgJit=1,VQMetrics="MLQK=4.5000;MLQKav=4.5000;
MLQKmn=4.5000;MLQKmx=4.5000;MLQKvr=0.95;CCR=0.0000;ICR=0.0000;ICRmx=0.0000;CS=0;SCS=0"
```

## Set Up CMRs

You can configure CMRs on the Service Parameters Configuration window in Cisco Unified CM Administration .

To access the Service Parameters Configuration window, open Cisco Unified CM Administration and choose System > Service Parameters .

Choose Advanced button.

Select the Call Diagnostics Enabled parameter.

This parameter determines whether the system generates CMRs, also called call diagnostic records. Valid values specify Disabled
                              (do not generate CMRs), Enabled Only When CDR Enabled Flag is True (generate CMRs only when the CDR Enabled Flag service parameter
                              is set to True), or Enabled Regardless of CDR Enabled Flag (generates CMRs without regard to the setting in the CDR Enabled
                              Flag service parameter). This represents a required field. The default value specifies Disabled.

### Feature Limitations

This feature is not supported for SME call flows:

On receiving call statistics from CUBE/IOS GW on SME, Unified Communications Manager generates CMR (provided CMR is enabled)
                                    for the trunk side, but it won’t be able to forward call statistics to other nodes in outgoing BYE or 200OK for BYE.

Sample Call flow:

Phone1 > CUBE/IOS GW > SME > CUCM1 > Phone2

For the above call scenario, SME generates the CMR for trunk side pointing to CUBE. These statistics are not forwarded to
                                    a leaf node. For Phone2, CMR is recorded on a leaf node.

## CPU Utilization

Cisco has performed basic testing to measure CPU utilization when CDRs and/or CMRs are enabled. The CPU utilization testing
                              was measured on subscribers and was not measured on the publishers. Your actual results can vary because of the CDR Loader
                              settings and the CDR Management settings for external billing servers. The following table displays the results of these tests.

These tests were performed with Unified Communications Manager Release 8.0(1).

CDRs and CMRs Enabled/Disabled

Average % Increase in Cisco Unified CM CPU Utilization

Average % Increase in Total CPU Utilization

% Increase in Cisco Unified CM CPU

% Increase in Total CPU

CDRs disabled, CMRs disabled

6.17

11.15

-

-

CDRs enabled, CMRs disabled

6.99

12.10

13.18

8.57

CDRs disabled, CMRs enabled

6.38

11.24

3.43

0.86

CDRs enabled, CMRs enabled

7.71

13.04

24.92

17.02

| Note | For Hold and Resume calls on SCCP devices, multiple CMR Records are generated based on the number of times the call is put
                                          on hold. |
|---|---|

| Note | CMRs are generated by Unified Communications Manager when Call Diagnostics Enabled service parameter is enabled. |
|---|---|

| Field | Description |
|---|---|
| PS | Packets Sent |
| OS | Octets Sent |
| PR | Packets Received |
| OR | Octets Received |
| PL | Packets Lost |
| JI | Jitter |
| LA | Round-Trip Delay in milliseconds (ms) |
| DU | Call Duration in seconds |

| Note | Some of the fields in the CMRs are not populated due to fields unrelated to SIP trunk or if no call statistics are received
                                          from CUBE. |
|---|---|

| Note | These tests were performed with Unified Communications Manager Release 8.0(1). |
|---|---|

| CDRs and CMRs Enabled/Disabled | Average % Increase in Cisco Unified CM CPU Utilization | Average % Increase in Total CPU Utilization | % Increase in Cisco Unified CM CPU | % Increase in Total CPU |
|---|---|---|---|---|
| CDRs disabled, CMRs disabled | 6.17 | 11.15 | - | - |
| CDRs enabled, CMRs disabled | 6.99 | 12.10 | 13.18 | 8.57 |
| CDRs disabled, CMRs enabled | 6.38 | 11.24 | 3.43 | 0.86 |
| CDRs enabled, CMRs enabled | 7.71 | 13.04 | 24.92 | 17.02 |