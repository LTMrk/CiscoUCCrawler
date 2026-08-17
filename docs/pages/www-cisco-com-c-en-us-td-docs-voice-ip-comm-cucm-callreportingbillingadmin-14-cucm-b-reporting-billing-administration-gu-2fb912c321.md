---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-callreportingbillingadmin-14-cucm-b-reporting-billing-administration-gu-2fb912c321
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/callReportingBillingAdmin/14/cucm_b_reporting-billing-administration-guide-14/cucm_b_reporting-and-billing-administration-guide_chapter_01101.html
retrieved_at: 2026-08-17T00:27:03.769759+00:00
---

Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: April 9, 2026

Chapter: CMR Field Descriptions

## Chapter: CMR Field Descriptions

- CMR Field Descriptions

- CMR Field Descriptions

- K-Factor Data

# CMR Field Descriptions

This chapter describes the field descriptions of the Call Management Records (CMRs).

## CMR Field Descriptions

The following table contains the fields, range of values, and field descriptions of the CMRs in the order in which they appear
                              in the CMR.

Field Name

Range of Values

Description

cdrRecordType

0, 1, or 2

Specifies the type of this specific record. The following valid values apply:

0—Start call detail record (not used)

1—End call detail record

2—CMR record

Default - For CMRs, this field always specifies 2.

globalCallID_callManagerId

Positive Integer

Specifies a unique Unified Communications Manager identity.

This field makes up half of the Global Call ID. The Global Call ID comprises the following fields:

globalCallId_callId

globalCallID_callManagerID

All records that are associated with a standard call have the same Global Call ID in them.

Default - Ensure that this field is populated.

globalCallId_callId

Positive Integer

Specifies a unique call identity value that gets assigned to each call. The system allocates this identifier independently
                                          on each call server. Values get chosen sequentially when a call begins. Each call, successful or unsuccessful, receives value
                                          assignment.

This field makes up half the Global Call ID. The Global Call ID comprises the following two fields:

globalCallId_callId

globalCallID_callManagerID

All records that are associated with a standard call have the same Global Call ID in them.

Default - Ensure that this field is populated.

nodeId

Positive Integer

Specifies the server or node within the Unified Communications Manager cluster, where this record gets generated.

Default - Ensure that this field is populated.

directoryNumber

Integer

Specifies the directory number of the device from which these diagnostics are collected.

Default - Ensure that this field is populated.

callIdentifier

Positive Integer

Identifies the call leg to which this record pertains.

Default - Ensure that this field is populated.

dateTimeStamp

Integer

Represents the approximate time that the device goes on the hook. Unified Communications Manager records the time when the phone responds to a request for diagnostic information.

Default - Ensure that this field is populated.

numberPacketsSent

Integer

Designates the total number of Routing Table Protocol (RTP) data packets that the device transmits since starting transmission
                                          on this connection. The value remains zero if the connection is set to "receive only" mode.

Default - 0

numberOctetsSent

Integer

Specifies the total number of payload octets (that is, not including header or padding) that the device transmits in RTP data
                                          packets since starting transmission on this connection. The value remains zero if the connection is set to "receive only" mode.

Default - 0

numberPacketsReceived

Integer

Specifies the total number of RTP data packets that the device has received since starting reception on this connection. The
                                          count includes packets that are received from different sources if this is a multicast call. The value remains zero if the
                                          connection is set in "send only" mode.

Default - 0

numberOctetsReceived

Integer

Specifies the total number of payload octets (that is, not including header or padding) that the device has received in RTP
                                          data packets since starting reception on this connection. The count includes packets that are received from different sources
                                          if this is a multicast call. The value remains zero if the connection is set in "send only" mode.

Default - 0

numberPacketsLost

Integer

Designates the total number of RTP data packets that have been lost since the beginning of reception. This number designates
                                          the number of packets that were expected, less the number of packets that were received, where the number of packets that
                                          were received includes any that are late or duplicates. Thus, packets that arrive late do not get counted as lost, and the
                                          loss may be negative if duplicate packets exist. The number of packets that are expected designates the extended last sequence
                                          number that was received, as defined next, less the initial sequence number that was received. The value remains zero if the
                                          connection was set in "send only" mode. For detailed information, see RFC 1889.

Default - 0

jitter

Integer

Provides an estimate of the statistical variance of the RTP data packet interarrival time that is measured in milliseconds
                                          and expressed as an unsigned integer. The interarrival jitter J specifies the mean deviation (smoothed absolute value) of
                                          the difference D in the packet spacing at the receiver, compared to the sender for a pair of packets. RFC 1889 contains detailed
                                          computation algorithms. The value remains zero if the connection was set in "send only" mode.

Default - 0

latency

Integer

Designates value that is an estimate of the network latency, expressed in milliseconds. This value represents the average
                                          value of the difference between the NTP timestamp that the RTP Control Protocol (RTCP) messages indicate and the NTP timestamp
                                          of the receivers, measured when these messages are received. Unified Communications Manager obtains the average by summing all estimates then dividing by the number of RTCP messages that have been received. For detailed
                                          information, see RFC 1889.

Default - 0

CMR records will not show latency for all phone loads. For example, for SIP 9.2.1 and 9.2.2, the latency will not show, as
                                                      it has not been implemented in these loads.

pkid

Text String

Identifies a text string that the database uses internally to uniquely identify each row. This text string provides no meaning
                                          to the call itself.

Default - The system always populates this field with a unique ID.

directoryNumberPartition

Text String

Identifies the partition of the directory number.

Default - Empty string "" . This field may remain empty if no partition exists.

globalCallId_ClusterId

Text String

Designates a unique ID that identifies a single Unified Communications Manager , or a cluster of Unified Communications Managers .

The system generates this field during installation, but Unified Communications Manager does not use it: globalCallId_ClusterId + globalCallId_callManagerId + globalCallId_callId.

Default - Ensure that this field is populated.

deviceName

Text String

Identifies the name of the device.

Default - Empty string "" . This field may remain empty if no device name exists.

varVQMetrics

Text String

Contains a variable number of voice quality metrics. This field comprises a string of voice quality metrics that are separated
                                          by a semicolon.

The format of the string follows:

fieldName=value;fieldName=value.precision

This example shows voice quality data, but the names may differ.

"MLQK=4.5000;MLQKav=4.5000; MLQKmn=4.5000;MLQKmx=4.5000;MLQKvr=0.95; CCR=0.0000;ICR=0.0000;ICRmx=0.0000; CS=0;SCS=0”

For more information on the K-Factor data that makes up the varVQMetrics record, see K-Factor Data .

duration

Integer

Specifies the duration value of audio session that is expressed in seconds. This is reported only for SIP phones.

videoContentType

Text String

Identifies the type of video stream. It can be “main”, “speaker” or “slides”. For an audio-only call, no video metrics are
                                          populated.

videoDuration

Integer

Specifies the duration value of the first video session, expressed in seconds.

numberVideoPacketsSent

Integer

Specifies the total number of RTP data packets that are transmitted by the device since starting transmission on this connection.

numberVideoOctetsSent

Integer

Specifies the total number of payload octets (that is, not including header or padding) transmitted in RTP data packets by
                                          the device since starting transmission on this connection.

numberVideoPacketsReceived

Integer

Specifies the total number of RTP data packets received by the device since starting reception on this connection.

numberVideoOctetsReceived

Integer

Specifies the total number of payload octets (that is, not including header or padding) received in RTP data packets by the
                                          device since starting reception on this connection.

numberVideoPacketsLost

Integer

Specifies the total number of RTP data packets that have been lost since the beginning of reception on this connection.

videoAverageJitter

Integer

Provides an estimate of the statistical variance of the RTP data packet interarrival time for this connection that is measured
                                          in milliseconds and expressed as an unsigned integer. For detailed information, see RFC 3550 for details.

videoRoundTripTime

Integer

This is a measure of average round trip time between the two endpoints for this connection. It is expressed in milliseconds.
                                          For detailed information, see RFC 3550 and RFC 3611 for detail

videoOneWayDelay

Text String

This is a measure of the average one-way delay (OWD) between the endpoints for this connection. This is only available if
                                          endpoints are time synchronized (same NTP source) and is measured in milli-seconds; otherwise “NA”

videoTransmissionMetrics

Text String

Contains a variable number of Cisco defined metrics that are related to RTP transmission on this connection. These metrics
                                          are delimited by a semicolon. The format of this string is:

CiscoTxVM="TxCodec=xxx; TxBw=xxx;TxBwMax=xxx; TxReso=xxx;TxFrameRate=xxx"

TxCodec identifies the type of video codec used for the transmitted video stream.

TxBw identifies the actual bandwidth that is used for the transmitted video stream.

TxBwMax identifies the maximum negotiated bandwidth for the transmitted video stream.

TxReso identifies the resolution of the transmitted video stream (for example, 640x480).

TxFrameRate identifies the average frame rate that is measured in frames per second for the transmitted video stream.

videoReceptionMetrics

TextString

Contains a variable number of Cisco defined metrics that are related to RTP reception on this connection. These metrics are
                                          delimited by a semicolon. The format of this string is:

CiscoRxVM="CS=xxx; SCS=xxx;DSCP=xxx; DSCPunad=xxx; RxFramesLost=xxx;RxCodec=xxx; RxBw=xxx;RxBwMax=xxx; RxReso=xxx;RxFrameRate=xxx"

CS identifies the concealed seconds metrics for the received video stream.

SCS identifies the severely concealed seconds for the received video stream.

DSCP is useful in verifying the DSCP value of the received video stream marked by endpoint.

DSCPunad is useful in verifying the DSCP value of the received video stream marked by endpoint.

RxCodec identifies the type of video codec used for received video stream.

RxBw identifies the actual bandwidth used for the received video stream.

RxBwMax identifies the maximum negotiated bandwidth for the received video stream.

RxReso identifies the resolution of the received video stream (for example, 640x480).

RxFrameRate identifies the average frame rate measured in frames per second for the received video stream.

videoContentType_channel2

Text String

Identifies the type of second video stream if it exists. If it does not exist, the remaining metrics for the second video
                                          stream will not be populated.

videoDuration_channel2

Integer

Specifies the duration of the second video session, expressed in seconds.

numberVideoPacketsSent_channel2

Integer

Specifies the total number of RTP data packets that are transmitted by the device since starting transmission on this connection.

numberVideoOctetsSent_channel2

Integer

Specifies the total number of payload octets (that is, not including header or padding) transmitted in RTP data packets by
                                          the device since starting transmission on this connection.

numberVideoPacketsReceived_channel2

Integer

Specifies the total number of RTP data packets received by the device since starting reception on this connection.

numberVideoOctetsReceived_channel2

Integer

Specifies the total number of payload octets (that is, not including header or padding) received in RTP data packets by the
                                          device since starting reception on this connection.

numberVideoPacketsLost_channel2

Integer

The total number of RTP data packets that have been lost since the beginning of reception on this connection.

videoAverageJitter_channel2

Integer

Provides an estimate of the statistical variance of the RTP data packet interarrival time for this connection that is measured
                                          in milliseconds and expressed as an unsigned integer. For more information, see RFC 3550.

videoRoundTripTime_channel2

Integer

This is a measure of average round trip time between the two endpoints for this connection. It is expressed in milliseconds.
                                          For more information, see RFC 3550 and RFC 3611 for details.

videoOneWayDelay_channel2

Integer

This is a measure of the average one-way delay (OWD) between the endpoints for this connection. This is only available if
                                          endpoints are time synchronized (same NTP source) and is measured in milli-seconds; otherwise “NA”.

videoReceptionMetrics_channel2

Text String

Contains a variable number of Cisco defined metrics that are related to RTP transmission on this connection. These metrics
                                          are delimited by a semicolon. The format of this string is:

CiscoTxVM="TxCodec=xxx; TxBw=xxx ;TxBwMax=xxx; TxReso=xxx;TxFrameRate=xxx"

TxCodec identifies the type of video codec used for the transmitted video stream.

TxBw identifies the actual bandwidth used for the transmitted video stream.

TxBwMax identifies the maximum negotiated bandwidth for the transmitted video stream.

TxReso identifies the resolution of the transmitted video stream (for example, 640x480).

TxFrameRate identifies the average frame rate measured in frames per second for the transmitted video stream.

videoTransmissionMetrics_channel2

Text String

Contains a variable number of Cisco defined metrics that are related to RTP reception on this connection. These metrics are
                                          delimited by a semicolon. The format of this string is:

CiscoRxVM="CS=xxx; SCS=xxx;DSCP=xxx; DSCPunad=xxx; RxFramesLost=xxx;RxCodec=xxx; RxBw=xxx;RxBwMax=xxx; RxReso=xxx;RxFrameRate=xxx"

CS identifies the concealed seconds metrics for the received video stream.

SCS identifies the severely concealed seconds for the received video stream.

DSCP is useful in verifying the DSCP value of the received video stream that is marked by endpoint.

DSCPunad is useful in verifying the DSCP value of the received video stream marked by endpoint.

RxCodec identifies the type of video codec used for the received video stream.

RxBw identifies the actual bandwidth that is used for the received video stream.

RxBwMax identifies the maximum negotiated bandwidth for the received video stream.

RxReso identifies the resolution of the received video stream (for example, 640x480).

RxFrameRate identifies the average frame rate that is measured in frames per second for the received video stream.

localSessionID

Text String

Indicates call Session ID of the local device.

The system generates a CMR record for each call leg when the user disconnects the call from the user device. This field is
                                          populated with the local device Session ID of the particular call.

The maximum length of this field is restricted to 127 characters. For example, localSessionlD = ab303 l 7fla784dc48fl824d0d3715d86

remoteSessionID

Text String

Indicates call Session ID of the remote device.

The system generates a CMR record for each call leg when the user disconnects the call from the user device. This field is
                                          populated with the remote device Session ID of the particular call.

The maximum length of this field is restricted to 127 characters. For example, remoteSessionID = 47755a9de7794ba387653f2099600ef2

SN

Integer

Indicates the serial number of the headset used.

The system generates a CMR record for the headset used with the phone and this field is populated with the serial number of
                                          the headset.

The maximum length of this field is restricted to 129 characters. For example, SN=AAA111BBB222

SN

Integer

Indicates the serial number of the headset used.

The system generates a CMR record for the headset used with the phone and this field is populated with the serial number of
                                          the headset.

The maximum length of this field is restricted to 129 characters. For example, SN=AAA111BBB222

Metrics

Text String

Indicates the metrics of the particular headset used.

The system generates a CMR record for the headset used with the phone and this field is populated with the diagnostics records
                                          of the headset.

The maximum length of this field is restricted to 600 characters. For example, Metrics="Key=value;Key1=Value1Key=value;"

The sub-fields within the Metrics field are not validated.

Metrics

Text String

Indicates the metrics of the particular headset used.

The system generates a CMR record for the headset used with the phone and this field is populated with the diagnostics records
                                          of the headset.

The maximum length of this field is restricted to 600 characters. For example, Metrics="Key=value;Key1=Value1Key=value;"

The sub-fields within the Metrics field are not validated.

## K-Factor Data

K-factor represents an endpoint mean opinion score (MOS) estimation algorithm that is defined in ITU standard P.VTQ. It represents
                              a general estimator that is used to estimate the mean value of a perceptual evaluation of speech quality (PESQ) population
                              for a specific impairment pattern.

MOS relates to the output of a well designed listening experiment. All MOS experiments use a five-point PESQ scale as defined
                              in ITU standard P.862.1, which describes the PESQ as an objective method for end-to-end speech quality assessment of narrow-band
                              telephone networks and speech codecs.

The MOS estimate provides a number that is inversely proportional to frame loss density. Clarity decreases as more frames
                              are lost or discarded at the receiving end. Consider the loss or discarding of these frames as concealment. Concealment statistics
                              measure packet (frame) loss and its effect on voice quality in an impaired network.

K-factor represents a weighted estimate of average user annoyance due to distortions that are caused by effective packet loss
                              such as dropouts and warbles. It does not estimate the impact of delay-related impairments such as echo. It provides an estimate
                              of listening quality (MOS-LQO) rather than conversational quality (MOS-CQO), and measurements of average user annoyance range
                              from 1 (poor voice quality) to 5 (very good voice quality).

K-factor gets trained or conditioned by speech samples from numerous speech databases, where each training sentence or network
                              condition that is associated with a P.862.1 value has a duration of 8 seconds. For more accurate scores, the system generates
                              k-factor estimates for every 8 seconds of active speech.

Consider K-factor and other MOS estimators to be secondary or derived statistics because they warn a network operator of frame
                              loss only after the problem becomes significant. Packet counts, concealment ratios, and concealment second counters represent
                              primary statistics because they alert the network operator before network impairment has an audible impact or is visible through
                              MOS.

The following table displays the K-factor date that is stored in the Unified Communications Manager CMRs.

Field Name

Phone Display Name

D&I User Interface Text and Description

CCR

Cum Conceal Ratio

Cumulative Conceal Ratio represents the cumulative ratio of concealment time over speech time that is observed after starting
                                          a call.

ICR

Interval Conceal Ratio

Interval Conceal Ratio represents an interval-based average concealment rate that is the ratio of concealment time over speech
                                          time for the last 3 seconds of active speech.

ICRmx

Max Conceal Ratio

Interval Conceal Ratio Max represents the maximum concealment ratio that is observed during the call.

CS

Conceal Secs

Conceal Secs represents the time during which some concealment is observed during a call.

SCS

Severely Conceal Secs

Severely Conceal Secs represents the time during which a significant amount of concealment is observed. If the concealment
                                          that is observed is usually greater than 50 milliseconds or approximately 5 percent, the speech probably does not seem very
                                          audible.

MLQK

MOS LQK

MOS Listening Quality K-factor provides an estimate of the MOS score of the last 8 seconds of speech on the reception signal
                                          path.

MLQKmn

Min MOS LQK

MOS Listening Quality K-factor Min represents the minimum score that is observed since the beginning of a call and represents
                                          the worst sounding 8-second interval.

MLQKmx

Max MOS LQK

MOS Listening Quality K-factor Max represents the maximum score that is observed since the beginning of a call and represents
                                          the best sounding 8-second interval.

MLQKav

Avg MOS LQK

MOS Listening Quality K-factor Avg8 represents the running average of scores that are observed since the beginning of a call.

| Field Name | Range of Values | Description |
|---|---|---|
| cdrRecordType | 0, 1, or 2 | Specifies the type of this specific record. The following valid values apply: 0—Start call detail record (not used) 1—End call detail record 2—CMR record Default - For CMRs, this field always specifies 2. |
| globalCallID_callManagerId | Positive Integer | Specifies a unique Unified Communications Manager identity. This field makes up half of the Global Call ID. The Global Call ID comprises the following fields: globalCallId_callId globalCallID_callManagerID All records that are associated with a standard call have the same Global Call ID in them. Default - Ensure that this field is populated. |
| globalCallId_callId | Positive Integer | Specifies a unique call identity value that gets assigned to each call. The system allocates this identifier independently
                                          on each call server. Values get chosen sequentially when a call begins. Each call, successful or unsuccessful, receives value
                                          assignment. This field makes up half the Global Call ID. The Global Call ID comprises the following two fields: globalCallId_callId globalCallID_callManagerID All records that are associated with a standard call have the same Global Call ID in them. Default - Ensure that this field is populated. |
| nodeId | Positive Integer | Specifies the server or node within the Unified Communications Manager cluster, where this record gets generated. Default - Ensure that this field is populated. |
| directoryNumber | Integer | Specifies the directory number of the device from which these diagnostics are collected. Default - Ensure that this field is populated. |
| callIdentifier | Positive Integer | Identifies the call leg to which this record pertains. Default - Ensure that this field is populated. |
| dateTimeStamp | Integer | Represents the approximate time that the device goes on the hook. Unified Communications Manager records the time when the phone responds to a request for diagnostic information. Default - Ensure that this field is populated. |
| numberPacketsSent | Integer | Designates the total number of Routing Table Protocol (RTP) data packets that the device transmits since starting transmission
                                          on this connection. The value remains zero if the connection is set to "receive only" mode. Default - 0 |
| numberOctetsSent | Integer | Specifies the total number of payload octets (that is, not including header or padding) that the device transmits in RTP data
                                          packets since starting transmission on this connection. The value remains zero if the connection is set to "receive only" mode. Default - 0 |
| numberPacketsReceived | Integer | Specifies the total number of RTP data packets that the device has received since starting reception on this connection. The
                                          count includes packets that are received from different sources if this is a multicast call. The value remains zero if the
                                          connection is set in "send only" mode. Default - 0 |
| numberOctetsReceived | Integer | Specifies the total number of payload octets (that is, not including header or padding) that the device has received in RTP
                                          data packets since starting reception on this connection. The count includes packets that are received from different sources
                                          if this is a multicast call. The value remains zero if the connection is set in "send only" mode. Default - 0 |
| numberPacketsLost | Integer | Designates the total number of RTP data packets that have been lost since the beginning of reception. This number designates
                                          the number of packets that were expected, less the number of packets that were received, where the number of packets that
                                          were received includes any that are late or duplicates. Thus, packets that arrive late do not get counted as lost, and the
                                          loss may be negative if duplicate packets exist. The number of packets that are expected designates the extended last sequence
                                          number that was received, as defined next, less the initial sequence number that was received. The value remains zero if the
                                          connection was set in "send only" mode. For detailed information, see RFC 1889. Default - 0 |
| jitter | Integer | Provides an estimate of the statistical variance of the RTP data packet interarrival time that is measured in milliseconds
                                          and expressed as an unsigned integer. The interarrival jitter J specifies the mean deviation (smoothed absolute value) of
                                          the difference D in the packet spacing at the receiver, compared to the sender for a pair of packets. RFC 1889 contains detailed
                                          computation algorithms. The value remains zero if the connection was set in "send only" mode. Default - 0 |
| latency | Integer | Designates value that is an estimate of the network latency, expressed in milliseconds. This value represents the average
                                          value of the difference between the NTP timestamp that the RTP Control Protocol (RTCP) messages indicate and the NTP timestamp
                                          of the receivers, measured when these messages are received. Unified Communications Manager obtains the average by summing all estimates then dividing by the number of RTCP messages that have been received. For detailed
                                          information, see RFC 1889. Default - 0 Note CMR records will not show latency for all phone loads. For example, for SIP 9.2.1 and 9.2.2, the latency will not show, as
                                                      it has not been implemented in these loads. | Note | CMR records will not show latency for all phone loads. For example, for SIP 9.2.1 and 9.2.2, the latency will not show, as
                                                      it has not been implemented in these loads. |
| Note | CMR records will not show latency for all phone loads. For example, for SIP 9.2.1 and 9.2.2, the latency will not show, as
                                                      it has not been implemented in these loads. |
| pkid | Text String | Identifies a text string that the database uses internally to uniquely identify each row. This text string provides no meaning
                                          to the call itself. Default - The system always populates this field with a unique ID. |
| directoryNumberPartition | Text String | Identifies the partition of the directory number. Default - Empty string "" . This field may remain empty if no partition exists. |
| globalCallId_ClusterId | Text String | Designates a unique ID that identifies a single Unified Communications Manager , or a cluster of Unified Communications Managers . The system generates this field during installation, but Unified Communications Manager does not use it: globalCallId_ClusterId + globalCallId_callManagerId + globalCallId_callId. Default - Ensure that this field is populated. |
| deviceName | Text String | Identifies the name of the device. Default - Empty string "" . This field may remain empty if no device name exists. |
| varVQMetrics | Text String | Contains a variable number of voice quality metrics. This field comprises a string of voice quality metrics that are separated
                                          by a semicolon. The format of the string follows: fieldName=value;fieldName=value.precision This example shows voice quality data, but the names may differ. "MLQK=4.5000;MLQKav=4.5000; MLQKmn=4.5000;MLQKmx=4.5000;MLQKvr=0.95; CCR=0.0000;ICR=0.0000;ICRmx=0.0000; CS=0;SCS=0” Note For more information on the K-Factor data that makes up the varVQMetrics record, see K-Factor Data . | Note | For more information on the K-Factor data that makes up the varVQMetrics record, see K-Factor Data . |
| Note | For more information on the K-Factor data that makes up the varVQMetrics record, see K-Factor Data . |
| duration | Integer | Specifies the duration value of audio session that is expressed in seconds. This is reported only for SIP phones. |
| videoContentType | Text String | Identifies the type of video stream. It can be “main”, “speaker” or “slides”. For an audio-only call, no video metrics are
                                          populated. |
| videoDuration | Integer | Specifies the duration value of the first video session, expressed in seconds. |
| numberVideoPacketsSent | Integer | Specifies the total number of RTP data packets that are transmitted by the device since starting transmission on this connection. |
| numberVideoOctetsSent | Integer | Specifies the total number of payload octets (that is, not including header or padding) transmitted in RTP data packets by
                                          the device since starting transmission on this connection. |
| numberVideoPacketsReceived | Integer | Specifies the total number of RTP data packets received by the device since starting reception on this connection. |
| numberVideoOctetsReceived | Integer | Specifies the total number of payload octets (that is, not including header or padding) received in RTP data packets by the
                                          device since starting reception on this connection. |
| numberVideoPacketsLost | Integer | Specifies the total number of RTP data packets that have been lost since the beginning of reception on this connection. |
| videoAverageJitter | Integer | Provides an estimate of the statistical variance of the RTP data packet interarrival time for this connection that is measured
                                          in milliseconds and expressed as an unsigned integer. For detailed information, see RFC 3550 for details. |
| videoRoundTripTime | Integer | This is a measure of average round trip time between the two endpoints for this connection. It is expressed in milliseconds.
                                          For detailed information, see RFC 3550 and RFC 3611 for detail |
| videoOneWayDelay | Text String | This is a measure of the average one-way delay (OWD) between the endpoints for this connection. This is only available if
                                          endpoints are time synchronized (same NTP source) and is measured in milli-seconds; otherwise “NA” |
| videoTransmissionMetrics | Text String | Contains a variable number of Cisco defined metrics that are related to RTP transmission on this connection. These metrics
                                          are delimited by a semicolon. The format of this string is: CiscoTxVM="TxCodec=xxx; TxBw=xxx;TxBwMax=xxx; TxReso=xxx;TxFrameRate=xxx" TxCodec identifies the type of video codec used for the transmitted video stream. TxBw identifies the actual bandwidth that is used for the transmitted video stream. TxBwMax identifies the maximum negotiated bandwidth for the transmitted video stream. TxReso identifies the resolution of the transmitted video stream (for example, 640x480). TxFrameRate identifies the average frame rate that is measured in frames per second for the transmitted video stream. |
| videoReceptionMetrics | TextString | Contains a variable number of Cisco defined metrics that are related to RTP reception on this connection. These metrics are
                                          delimited by a semicolon. The format of this string is: CiscoRxVM="CS=xxx; SCS=xxx;DSCP=xxx; DSCPunad=xxx; RxFramesLost=xxx;RxCodec=xxx; RxBw=xxx;RxBwMax=xxx; RxReso=xxx;RxFrameRate=xxx" CS identifies the concealed seconds metrics for the received video stream. SCS identifies the severely concealed seconds for the received video stream. DSCP is useful in verifying the DSCP value of the received video stream marked by endpoint. DSCPunad is useful in verifying the DSCP value of the received video stream marked by endpoint. RxCodec identifies the type of video codec used for received video stream. RxBw identifies the actual bandwidth used for the received video stream. RxBwMax identifies the maximum negotiated bandwidth for the received video stream. RxReso identifies the resolution of the received video stream (for example, 640x480). RxFrameRate identifies the average frame rate measured in frames per second for the received video stream. |
| videoContentType_channel2 | Text String | Identifies the type of second video stream if it exists. If it does not exist, the remaining metrics for the second video
                                          stream will not be populated. |
| videoDuration_channel2 | Integer | Specifies the duration of the second video session, expressed in seconds. |
| numberVideoPacketsSent_channel2 | Integer | Specifies the total number of RTP data packets that are transmitted by the device since starting transmission on this connection. |
| numberVideoOctetsSent_channel2 | Integer | Specifies the total number of payload octets (that is, not including header or padding) transmitted in RTP data packets by
                                          the device since starting transmission on this connection. |
| numberVideoPacketsReceived_channel2 | Integer | Specifies the total number of RTP data packets received by the device since starting reception on this connection. |
| numberVideoOctetsReceived_channel2 | Integer | Specifies the total number of payload octets (that is, not including header or padding) received in RTP data packets by the
                                          device since starting reception on this connection. |
| numberVideoPacketsLost_channel2 | Integer | The total number of RTP data packets that have been lost since the beginning of reception on this connection. |
| videoAverageJitter_channel2 | Integer | Provides an estimate of the statistical variance of the RTP data packet interarrival time for this connection that is measured
                                          in milliseconds and expressed as an unsigned integer. For more information, see RFC 3550. |
| videoRoundTripTime_channel2 | Integer | This is a measure of average round trip time between the two endpoints for this connection. It is expressed in milliseconds.
                                          For more information, see RFC 3550 and RFC 3611 for details. |
| videoOneWayDelay_channel2 | Integer | This is a measure of the average one-way delay (OWD) between the endpoints for this connection. This is only available if
                                          endpoints are time synchronized (same NTP source) and is measured in milli-seconds; otherwise “NA”. |
| videoReceptionMetrics_channel2 | Text String | Contains a variable number of Cisco defined metrics that are related to RTP transmission on this connection. These metrics
                                          are delimited by a semicolon. The format of this string is: CiscoTxVM="TxCodec=xxx; TxBw=xxx ;TxBwMax=xxx; TxReso=xxx;TxFrameRate=xxx" TxCodec identifies the type of video codec used for the transmitted video stream. TxBw identifies the actual bandwidth used for the transmitted video stream. TxBwMax identifies the maximum negotiated bandwidth for the transmitted video stream. TxReso identifies the resolution of the transmitted video stream (for example, 640x480). TxFrameRate identifies the average frame rate measured in frames per second for the transmitted video stream. |
| videoTransmissionMetrics_channel2 | Text String | Contains a variable number of Cisco defined metrics that are related to RTP reception on this connection. These metrics are
                                          delimited by a semicolon. The format of this string is: CiscoRxVM="CS=xxx; SCS=xxx;DSCP=xxx; DSCPunad=xxx; RxFramesLost=xxx;RxCodec=xxx; RxBw=xxx;RxBwMax=xxx; RxReso=xxx;RxFrameRate=xxx" CS identifies the concealed seconds metrics for the received video stream. SCS identifies the severely concealed seconds for the received video stream. DSCP is useful in verifying the DSCP value of the received video stream that is marked by endpoint. DSCPunad is useful in verifying the DSCP value of the received video stream marked by endpoint. RxCodec identifies the type of video codec used for the received video stream. RxBw identifies the actual bandwidth that is used for the received video stream. RxBwMax identifies the maximum negotiated bandwidth for the received video stream. RxReso identifies the resolution of the received video stream (for example, 640x480). RxFrameRate identifies the average frame rate that is measured in frames per second for the received video stream. |
| localSessionID | Text String | Indicates call Session ID of the local device. The system generates a CMR record for each call leg when the user disconnects the call from the user device. This field is
                                          populated with the local device Session ID of the particular call. The maximum length of this field is restricted to 127 characters. For example, localSessionlD = ab303 l 7fla784dc48fl824d0d3715d86 |
| remoteSessionID | Text String | Indicates call Session ID of the remote device. The system generates a CMR record for each call leg when the user disconnects the call from the user device. This field is
                                          populated with the remote device Session ID of the particular call. The maximum length of this field is restricted to 127 characters. For example, remoteSessionID = 47755a9de7794ba387653f2099600ef2 |
| SN | Integer | Indicates the serial number of the headset used. The system generates a CMR record for the headset used with the phone and this field is populated with the serial number of
                                          the headset. The maximum length of this field is restricted to 129 characters. For example, SN=AAA111BBB222 |
| SN | Integer | Indicates the serial number of the headset used. The system generates a CMR record for the headset used with the phone and this field is populated with the serial number of
                                          the headset. The maximum length of this field is restricted to 129 characters. For example, SN=AAA111BBB222 |
| Metrics | Text String | Indicates the metrics of the particular headset used. The system generates a CMR record for the headset used with the phone and this field is populated with the diagnostics records
                                          of the headset. The maximum length of this field is restricted to 600 characters. For example, Metrics="Key=value;Key1=Value1Key=value;" Note The sub-fields within the Metrics field are not validated. | Note | The sub-fields within the Metrics field are not validated. |
| Note | The sub-fields within the Metrics field are not validated. |
| Metrics | Text String | Indicates the metrics of the particular headset used. The system generates a CMR record for the headset used with the phone and this field is populated with the diagnostics records
                                          of the headset. The maximum length of this field is restricted to 600 characters. For example, Metrics="Key=value;Key1=Value1Key=value;" Note The sub-fields within the Metrics field are not validated. | Note | The sub-fields within the Metrics field are not validated. |
| Note | The sub-fields within the Metrics field are not validated. |

| Note | CMR records will not show latency for all phone loads. For example, for SIP 9.2.1 and 9.2.2, the latency will not show, as
                                                      it has not been implemented in these loads. |
|---|---|

| Note | For more information on the K-Factor data that makes up the varVQMetrics record, see K-Factor Data . |
|---|---|

| Note | The sub-fields within the Metrics field are not validated. |
|---|---|

| Note | The sub-fields within the Metrics field are not validated. |
|---|---|

| Field Name | Phone Display Name | D&I User Interface Text and Description |
|---|---|---|
| CCR | Cum Conceal Ratio | Cumulative Conceal Ratio represents the cumulative ratio of concealment time over speech time that is observed after starting
                                          a call. |
| ICR | Interval Conceal Ratio | Interval Conceal Ratio represents an interval-based average concealment rate that is the ratio of concealment time over speech
                                          time for the last 3 seconds of active speech. |
| ICRmx | Max Conceal Ratio | Interval Conceal Ratio Max represents the maximum concealment ratio that is observed during the call. |
| CS | Conceal Secs | Conceal Secs represents the time during which some concealment is observed during a call. |
| SCS | Severely Conceal Secs | Severely Conceal Secs represents the time during which a significant amount of concealment is observed. If the concealment
                                          that is observed is usually greater than 50 milliseconds or approximately 5 percent, the speech probably does not seem very
                                          audible. |
| MLQK | MOS LQK | MOS Listening Quality K-factor provides an estimate of the MOS score of the last 8 seconds of speech on the reception signal
                                          path. |
| MLQKmn | Min MOS LQK | MOS Listening Quality K-factor Min represents the minimum score that is observed since the beginning of a call and represents
                                          the worst sounding 8-second interval. |
| MLQKmx | Max MOS LQK | MOS Listening Quality K-factor Max represents the maximum score that is observed since the beginning of a call and represents
                                          the best sounding 8-second interval. |
| MLQKav | Avg MOS LQK | MOS Listening Quality K-factor Avg8 represents the running average of scores that are observed since the beginning of a call. |