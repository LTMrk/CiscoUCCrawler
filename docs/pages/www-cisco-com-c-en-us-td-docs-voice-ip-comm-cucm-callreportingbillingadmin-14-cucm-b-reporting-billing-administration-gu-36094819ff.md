---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-callreportingbillingadmin-14-cucm-b-reporting-billing-administration-gu-36094819ff
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/callReportingBillingAdmin/14/cucm_b_reporting-billing-administration-guide-14/cucm_b_reporting-and-billing-administration-guide_chapter_01110.html
retrieved_at: 2026-08-17T00:27:07.649824+00:00
---

Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: April 9, 2026

Chapter: CMR Examples

## Chapter: CMR Examples

- CMR Examples

- CMR Examples

# CMR Examples

This chapter provides examples of call management records (CMRs).

## CMR Examples

The following examples of CMRs get generated during a normal call (IP phone to IP phone). Normal calls log three records per
                              call: one CDR and two CMRs (one for each endpoint).

These examples represent a call between directory number 1010 and 1014. See related topics for a sample of the CDR that gets
                              generated during a normal call.

### Example 1: SCCP to SCCP Phone

A successful call between two Cisco IP Phones generates 2 CMRs at the end of the call, one for each endpoint. This example
                              has both endpoints as SCCP phones that do not support the new video metrics. They are left at default.

Field Names

Values

cdrRecordType

2

globalCallID_callManagerId

1

globalCallID_callId

96004

nodeId

1

directoryNum

1010

callIdentifier

28141535

dateTimeStamp

1202412060

numberPacketsSent

358

numberOctetsSent

61576

numberPacketsReceived

351

numberOctetsReceived

60372

numberPacketsLost

1

jitter

0

latency

0

pkid

e95df5b1-2914-4a03-befb-0f58bf16392d

directoryNumPartition

globalCallIdClusterID

StandAloneCluster

deviceName

SEP003094C39BE7

varVQMetrics

MLQK=0.0000;MLQKav=0.0000; MLQKmn=0.0000;MLQKmx=0.0000;MLQKvr=0.95; CCR=0.0000;ICR=0.0000;ICRmx=0.0000;CS=0; SCS=0

duration

videoContentType

videoDuration

numberVideoPacketsSent

numberVideoOctetsSent

numberVideoPacketsReceived

numberVideoOctetsReceived

numberVideoPacketsLost

videoAverageJitter

videoRoundTripTime

videoOneWayDelay

videoReceptionMetrics

videoTransmissionMetrics

videoContentType_channel2

videoDuration_channel2

numberVideoPacketsSent_channel2

numberVideoOctetsSent_channel2

numberVideoPacketsReceived_channel2

numberVideoOctetsReceived_channel2

numberVideoPacketsLost_channel2

videoAverageJitter_channel2

videoRoundTripTime_channel2

videoOneWayDelay_channel2

videoReceptionMetrics_channel2

videoTransmissionMetrics_channel2

Field Name

Values

cdrRecordType

2

globalCallID_callManagerId

1

globalCallID_callId

96004

nodeId

1

directoryNum

1004

callIdentifier

28141536

dateTimeStamp

1202412060

numberPacketsSent

352

numberOctetsSent

60544

numberPacketsReceived

356

numberOctetsReceived

61232

numberPacketsLost

1

jitter

0

latency

0

pkid

545ff25a-5475-4882-af09-c7b714802703

directoryNumPartition

globalCallIdClusterID

StandAloneCluster

deviceName

SEP0007EBBA6376

varVQMetrics

MLQK=0.0000;MLQKav=0.0000; MLQKmn=0.0000; MLQKmx=0.0000;MLQKvr=0.95; CCR=0.0000; ICR=0.0000;ICRmx=0.0000;CS=0; SCS=0

duration

videoContentType

videoDuration

numberVideoPacketsSent

numberVideoOctetsSent

numberVideoPacketsReceived

numberVideoOctetsReceived

numberVideoPacketsLost

videoAverageJitter

videoRoundTripTime

videoOneWayDelay

videoReceptionMetrics

videoTransmissionMetrics

videoContentType_channel2

videoDuration_channel2

numberVideoPacketsSent_channel2

numberVideoOctetsSent_channel2

numberVideoPacketsReceived_channel2

numberVideoOctetsReceived_channel2

numberVideoPacketsLost_channel2

videoAverageJitter_channel2

videoRoundTripTime_channel2

videoOneWayDelay_channel2

videoReceptionMetrics_channel2

videoTransmissionMetrics_channel2

### Example 2: SIP to SIP Phone That Supports Main Video Metrics

The following CMR flat file is an example of SIP to SIP phone that supports video metrics.

Field Name

Values

cdrRecordType

2

globalCallID_callManagerId

1

globalCallID_callId

17001

nodeId

1

directoryNum

139098

callIdentifier

32216238

dateTimeStamp

1379591701

numberPacketsSent

170

numberOctetsSent

10370

numberPacketsReceived

169

numberOctetsReceived

12337

numberPacketsLost

0

jitter

2

latency

0

pkid

ea0cddd0-7ddd-4a4e-a697-ca405e39292c

directoryNumPartition

globalCallId_ClusterID

StandAloneCluster

deviceName

SEPD0C7891411C3

varVQMetrics

MLQK=0.0000;MLQKav=0.0000;MLQKmn=0.0000; MLQKmx=0.0000;MLQKvr=;CCR=0.0000;ICR=0.0000; ICRmx=0.0000;CS=0;SCS=0

duration

3

videoContentType

main

videoDuration

3

numberVideoPacketsSent

140

numberVideoOctetsSent

126355

numberVideoPacketsReceived

141

numberVideoOctetsReceived

128214

numberVideoPacketsLost

0

videoAverageJitter

7

videoRoundTripTime

0

videoOneWayDelay

0

videoReceptionMetrics

RxCodec=H264;RxBw=377;RxReso=640x360; RxFrameRate=31;RxFramesLost=0

videoTransmissionMetrics

TxCodec=H264;TxBw=368;TxReso=640x360; TxFrameRate=30

videoContentType_channel2

videoDuration_channel2

numberVideoPacketsSent_channel2

numberVideoOctetsSent_channel2

numberVideoPacketsReceived_channel2

numberVideoOctetsReceived_channel2

numberVideoPacketsLost_channel2

videoAverageJitter_channel2

videoRoundTripTime_channel2

videoOneWayDelay_channel2

videoReceptionMetrics_channel2

videoTransmissionMetrics_channel2

| Note | "Duration" field in CMR is filled only for SIP phones. |
|---|---|

| Field Names | Values |
|---|---|
| cdrRecordType | 2 |
| globalCallID_callManagerId | 1 |
| globalCallID_callId | 96004 |
| nodeId | 1 |
| directoryNum | 1010 |
| callIdentifier | 28141535 |
| dateTimeStamp | 1202412060 |
| numberPacketsSent | 358 |
| numberOctetsSent | 61576 |
| numberPacketsReceived | 351 |
| numberOctetsReceived | 60372 |
| numberPacketsLost | 1 |
| jitter | 0 |
| latency | 0 |
| pkid | e95df5b1-2914-4a03-befb-0f58bf16392d |
| directoryNumPartition |  |
| globalCallIdClusterID | StandAloneCluster |
| deviceName | SEP003094C39BE7 |
| varVQMetrics | MLQK=0.0000;MLQKav=0.0000; MLQKmn=0.0000;MLQKmx=0.0000;MLQKvr=0.95; CCR=0.0000;ICR=0.0000;ICRmx=0.0000;CS=0; SCS=0 |
| duration |  |
| videoContentType |  |
| videoDuration |  |
| numberVideoPacketsSent |  |
| numberVideoOctetsSent |  |
| numberVideoPacketsReceived |  |
| numberVideoOctetsReceived |  |
| numberVideoPacketsLost |  |
| videoAverageJitter |  |
| videoRoundTripTime |  |
| videoOneWayDelay |  |
| videoReceptionMetrics |  |
| videoTransmissionMetrics |  |
| videoContentType_channel2 |  |
| videoDuration_channel2 |  |
| numberVideoPacketsSent_channel2 |  |
| numberVideoOctetsSent_channel2 |  |
| numberVideoPacketsReceived_channel2 |  |
| numberVideoOctetsReceived_channel2 |  |
| numberVideoPacketsLost_channel2 |  |
| videoAverageJitter_channel2 |  |
| videoRoundTripTime_channel2 |  |
| videoOneWayDelay_channel2 |  |
| videoReceptionMetrics_channel2 |  |
| videoTransmissionMetrics_channel2 |  |

| Field Name | Values |
|---|---|
| cdrRecordType | 2 |
| globalCallID_callManagerId | 1 |
| globalCallID_callId | 96004 |
| nodeId | 1 |
| directoryNum | 1004 |
| callIdentifier | 28141536 |
| dateTimeStamp | 1202412060 |
| numberPacketsSent | 352 |
| numberOctetsSent | 60544 |
| numberPacketsReceived | 356 |
| numberOctetsReceived | 61232 |
| numberPacketsLost | 1 |
| jitter | 0 |
| latency | 0 |
| pkid | 545ff25a-5475-4882-af09-c7b714802703 |
| directoryNumPartition |  |
| globalCallIdClusterID | StandAloneCluster |
| deviceName | SEP0007EBBA6376 |
| varVQMetrics | MLQK=0.0000;MLQKav=0.0000; MLQKmn=0.0000; MLQKmx=0.0000;MLQKvr=0.95; CCR=0.0000; ICR=0.0000;ICRmx=0.0000;CS=0; SCS=0 |
| duration |  |
| videoContentType |  |
| videoDuration |  |
| numberVideoPacketsSent |  |
| numberVideoOctetsSent |  |
| numberVideoPacketsReceived |  |
| numberVideoOctetsReceived |  |
| numberVideoPacketsLost |  |
| videoAverageJitter |  |
| videoRoundTripTime |  |
| videoOneWayDelay |  |
| videoReceptionMetrics |  |
| videoTransmissionMetrics |  |
| videoContentType_channel2 |  |
| videoDuration_channel2 |  |
| numberVideoPacketsSent_channel2 |  |
| numberVideoOctetsSent_channel2 |  |
| numberVideoPacketsReceived_channel2 |  |
| numberVideoOctetsReceived_channel2 |  |
| numberVideoPacketsLost_channel2 |  |
| videoAverageJitter_channel2 |  |
| videoRoundTripTime_channel2 |  |
| videoOneWayDelay_channel2 |  |
| videoReceptionMetrics_channel2 |  |
| videoTransmissionMetrics_channel2 |  |

| Field Name | Values |
|---|---|
| cdrRecordType | 2 |
| globalCallID_callManagerId | 1 |
| globalCallID_callId | 17001 |
| nodeId | 1 |
| directoryNum | 139098 |
| callIdentifier | 32216238 |
| dateTimeStamp | 1379591701 |
| numberPacketsSent | 170 |
| numberOctetsSent | 10370 |
| numberPacketsReceived | 169 |
| numberOctetsReceived | 12337 |
| numberPacketsLost | 0 |
| jitter | 2 |
| latency | 0 |
| pkid | ea0cddd0-7ddd-4a4e-a697-ca405e39292c |
| directoryNumPartition |  |
| globalCallId_ClusterID | StandAloneCluster |
| deviceName | SEPD0C7891411C3 |
| varVQMetrics | MLQK=0.0000;MLQKav=0.0000;MLQKmn=0.0000; MLQKmx=0.0000;MLQKvr=;CCR=0.0000;ICR=0.0000; ICRmx=0.0000;CS=0;SCS=0 |
| duration | 3 |
| videoContentType | main |
| videoDuration | 3 |
| numberVideoPacketsSent | 140 |
| numberVideoOctetsSent | 126355 |
| numberVideoPacketsReceived | 141 |
| numberVideoOctetsReceived | 128214 |
| numberVideoPacketsLost | 0 |
| videoAverageJitter | 7 |
| videoRoundTripTime | 0 |
| videoOneWayDelay | 0 |
| videoReceptionMetrics | RxCodec=H264;RxBw=377;RxReso=640x360; RxFrameRate=31;RxFramesLost=0 |
| videoTransmissionMetrics | TxCodec=H264;TxBw=368;TxReso=640x360; TxFrameRate=30 |
| videoContentType_channel2 |  |
| videoDuration_channel2 |  |
| numberVideoPacketsSent_channel2 |  |
| numberVideoOctetsSent_channel2 |  |
| numberVideoPacketsReceived_channel2 |  |
| numberVideoOctetsReceived_channel2 |  |
| numberVideoPacketsLost_channel2 |  |
| videoAverageJitter_channel2 |  |
| videoRoundTripTime_channel2 |  |
| videoOneWayDelay_channel2 |  |
| videoReceptionMetrics_channel2 |  |
| videoTransmissionMetrics_channel2 |  |