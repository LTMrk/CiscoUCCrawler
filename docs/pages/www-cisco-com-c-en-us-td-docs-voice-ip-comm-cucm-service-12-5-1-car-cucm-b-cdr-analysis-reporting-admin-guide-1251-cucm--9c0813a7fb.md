---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--9c0813a7fb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_011100.html
retrieved_at: 2026-08-21T01:37:20.186941+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: CDR Search

## Chapter: CDR Search

# CDR Search

This chapter describes CDR search results.

## CDR Search Results

The CDR search allows users to view the CDR/CMR fields as
                              		  described in the table. The CDR search retrieves the CDR/CMR files from the
                              		  tbl_billing_data and tbl_billing_error tables of the CAR database.

See the following table.

Field

Description

Sl No

This field specifies the serial or record number.

Call Type

This field specifies the type of call: simple,
                                          					 transfer, forward, pickup, conference, refer, replaces, or redirection.

GCID_CMIdGCID_CallId

This field specifies the call identifiers that are
                                          					 associated with all the records for the entire call.

Orig Node IdDest Node Id

This field specifies the server where the call
                                          					 originator/destination was registered at the time of the call.

Orig Leg IdDest Leg Id

This field specifies the unique identifiers to the
                                          					 originating/destination leg of a call.

Calling NoCalling No Partition

The calling number specifies the directory number
                                          					 where the call originated. The calling partition specifies the partition that
                                          					 is associated with the calling party.

Called NoCalled No Partition

The called number specifies the directory number from
                                          					 which the call was initially placed and is the same as the Dest No when the
                                          					 call is not transferred or forwarded. The called partition specifies the
                                          					 partition that is associated with the called party.

Dest NoDest No Partition

The destination number specifies the directory number
                                          					 where the call finally terminated and is the same as the called number when the
                                          					 call is not transferred or forwarded. The destination number partition
                                          					 specifies the partition that is associated with the destination number.

Last Rd NoLast Rd No Partition

The last redirected number specifies the directory
                                          					 number from which the call was finally redirected. The last redirected number
                                          					 partition specifies the partition that is associated with the last redirected
                                          					 number.

Media InfoOrig Pkts Rcd Dest Pkts Rcd Orig Pkts Lost
                                          					 Dest Pkts Lost

This field specifies the packets that were received
                                          					 or lost for the origination or destination leg of a call and a link to the
                                          					 media information.

CDR - CMR Dump

This field specifies a link to the CDR and CDR dump
                                          					 tables. This link allows the users to view the values in the CDR/CMR fields.

## Media Information

The media information table provides the following
                              		  information. See the table.

Field

Description

Origination Leg

A unique identifier for the originating leg of a
                                          					 call.

Destination Leg

A unique identifier for the destination leg of a
                                          					 call.

Parameter

The media parameters MediaTransportAdd_Ip,
                                          					 PayLoadCapability, MediaCap_g723BitRate, Packets Sent, Octets Sent, Packets
                                          					 Received, Octets Received, Packets Lost, Jitter, Latency, QoS, VideoCap_Codec,
                                          					 VideoCap_Bandwidth, VideoCap_Resolution, VideoTransportAddress_IP, and
                                          					 VideoTransportAddress_Port

Origination

The value for all the preceding parameters for the
                                          					 origination leg of the call.

Destination

The value for all the preceding parameters for the
                                          					 destination leg of the call.

## CDR and CMR Dump Tables

The CDR and CMR dump tables provide the following
                              		  information. See the following table.

You can view the content of the voice quality metrics field,
                                          			 varVQMetrics, in the Origination CMR and Destination CMR fields.

Field

Description

CDR

This field specifies the call detail record fields.

Origination CMR

Only a single set of fields for origination and
                                          					 destination exists. You can find the origination or destination CMR by using
                                          					 the leg IDs. If the leg IDs of the CMR match the Orig/Dest leg ID of the CDR,
                                          					 the following record represents Orig/Dest CMR.

Destination CMR

Only a single set of fields for origination and
                                          					 destination exists. You can find the origination or destination CMR by using
                                          					 the leg IDs. If the leg IDs of the CMR match the Orig/Dest leg ID of the CDR,
                                          					 the following record represents Orig/Dest CMR.

The following example displays output from a CDR dump file:

### Sample CDR Dump File Output

cdrRecordType, globalCallID_callManagerId,
                              		  globalCallID_callId, origLegCallIdentifier, dateTimeOrigination, origNodeId,
                              		  origSpan, origIpAddr, callingPartyNumber, callingPartyUnicodeLoginUserID,
                              		  origCause_location, origCause_value, origPrecedenceLevel,
                              		  origMediaTransportAddress_IP, origMediaTransportAddress_Port,
                              		  origMediaCap_payloadCapability, origMediaCap_maxFramesPerPacket,
                              		  origMediaCap_g723BitRate, origVideoCap_Codec, origVideoCap_Bandwidth,
                              		  origVideoCap_Resolution, origVideoTransportAddress_IP,
                              		  origVideoTransportAddress_Port, origRSVPAudioStat, origRSVPVideoStat,
                              		  destLegIdentifier, destNodeId, destSpan, destIpAddr, originalCalledPartyNumber,
                              		  finalCalledPartyNumber, finalCalledPartyUnicodeLoginUserID, destCause_location,
                              		  destCause_value, destPrecedenceLevel, destMediaTransportAddress_IP,
                              		  destMediaTransportAddress_Port, destMediaCap_payloadCapability,
                              		  destMediaCap_maxFramesPerPacket, destMediaCap_g723BitRate, destVideoCap_Codec,
                              		  destVideoCap_Bandwidth, destVideoCap_Resolution, destVideoTransportAddress_IP,
                              		  destVideoTransportAddress_Port, destRSVPAudioStat, destRSVPVideoStat,
                              		  dateTimeConnect, dateTimeDisconnect, lastRedirectDn, pkid,
                              		  originalCalledPartyNumberPartition, callingPartyNumberPartition,
                              		  finalCalledPartyNumberPartition, lastRedirectDnPartition, duration,
                              		  origDeviceName, destDeviceName, origCallTerminationOnBehalfOf,
                              		  destCallTerminationOnBehalfOf, origCalledPartyRedirectOnBehalfOf,
                              		  lastRedirectRedirectOnBehalfOf, origCalledPartyRedirectReason,
                              		  lastRedirectRedirectReason, destConversationId, globalCallId_ClusterID,
                              		  joinOnBehalfOf, comment, authCodeDescription, authorizationLevel,
                              		  clientMatterCode, origDTMFMethod, destDTMFMethod, callSecuredStatus,
                              		  origConversationId, origMediaCap_Bandwidth, destMediaCap_Bandwidth,
                              		  authorizationCodeValue, outpulsedCallingPartyNumber,
                              		  outpulsedCalledPartyNumber, origIpv4v6Addr, destIpv4v6Addr,
                              		  origVideoCap_Codec_Channel2, origVideoCap_Bandwidth_Channel2,
                              		  origVideoCap_Resolution_Channel2, origVideoTransportAddress_IP_Channel2,
                              		  origVideoTransportAddress_Port_Channel2, origVideoChannel_Role_Channel2,
                              		  destVideoCap_Codec_Channel2, destVideoCap_Bandwidth_Channel2,
                              		  destVideoCap_Resolution_Channel2, destVideoTransportAddress_IP_Channel2,
                              		  destVideoTransportAddress_Port_Channel2, destVideoChannel_Role_Channel2,
                              		  IncomingProtocolID, IncomingProtocolCallRef, OutgoingProtocolID,
                              		  OutgoingProtocolCallRef, currentRoutingReason, origRoutingReason,
                              		  lastRedirectingRoutingReason, huntPilotPartition, huntPilotDN

INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER,
                              		  INTEGER, INTEGER, VARCHAR(50), VARCHAR(128), INTEGER, INTEGER, INTEGER,
                              		  INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER,
                              		  INTEGER, INTEGER, VARCHAR(64), VARCHAR(64), INTEGER, INTEGER, INTEGER, INTEGER,
                              		  VARCHAR(50), VARCHAR(50), VARCHAR(128), INTEGER, INTEGER, INTEGER, INTEGER,
                              		  INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER,
                              		  INTEGER, VARCHAR(64), VARCHAR(64), INTEGER, INTEGER, VARCHAR(50),
                              		  UNIQUEIDENTIFIER, VARCHAR(50), VARCHAR(50), VARCHAR(50), VARCHAR(50), INTEGER,
                              		  VARCHAR(129), VARCHAR(129), INTEGER, INTEGER, INTEGER, INTEGER, INTEGER,
                              		  INTEGER, INTEGER, VARCHAR(50), INTEGER, VARCHAR(2048), VARCHAR(50), INTEGER,
                              		  VARCHAR(32), INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, VARCHAR(32),
                              		  VARCHAR(50), VARCHAR(50), VARCHAR(64), VARCHAR(64), INTEGER, INTEGER, INTEGER,
                              		  INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER,
                              		  INTEGER, INTEGER, VARCHAR(32), INTEGER, VARCHAR(32), INTEGER, INTEGER, INTEGER,
                              		  VARCHAR(50), VARCHAR(50)

1, 1, 37, 29654625, 1258090294, 1, 0, 136269066, 1001,
                              		  caruser2, 0, 16, 4, 136269066, 16790, 4, 20, 0, 0, 0, 0, 0, 0, 0, 0, 29654626,
                              		  1, 0, 85937418, 5555, 1002, caruser1, 0, 0, 4, 85937418, 30844, 4, 20, 0, 0, 0,
                              		  0, 0, 0, 0, 0, 1258090296, 1258090383, 5555,
                              		  dcf0b5c9-7d57-475b-b166-d207a6617f34, , , , , 87, SEP003094C3CCB0,
                              		  SEP0002FD3BA528, 12, 0, 0, 0, 0, 0, 0, StandAloneCluster, 0, , , 0, , 3, 3, 0,
                              		  0, 64, 64, , , , 10.77.31.8, 10.77.31.5,
                              		  101,0,5,0,0,1,100,0,3,0,0,1,3,0000000000000108012BB4AE00000002,3,0000000000000108012BB4B200000000,2,5,7,1000,
                              		  5555

## Related Topics

Generate CDR Analysis and Reporting

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records Administration Guide

| Field | Description |
|---|---|
| Sl No | This field specifies the serial or record number. |
| Call Type | This field specifies the type of call: simple,
                                          					 transfer, forward, pickup, conference, refer, replaces, or redirection. |
| GCID_CMIdGCID_CallId | This field specifies the call identifiers that are
                                          					 associated with all the records for the entire call. |
| Orig Node IdDest Node Id | This field specifies the server where the call
                                          					 originator/destination was registered at the time of the call. |
| Orig Leg IdDest Leg Id | This field specifies the unique identifiers to the
                                          					 originating/destination leg of a call. |
| Calling NoCalling No Partition | The calling number specifies the directory number
                                          					 where the call originated. The calling partition specifies the partition that
                                          					 is associated with the calling party. |
| Called NoCalled No Partition | The called number specifies the directory number from
                                          					 which the call was initially placed and is the same as the Dest No when the
                                          					 call is not transferred or forwarded. The called partition specifies the
                                          					 partition that is associated with the called party. |
| Dest NoDest No Partition | The destination number specifies the directory number
                                          					 where the call finally terminated and is the same as the called number when the
                                          					 call is not transferred or forwarded. The destination number partition
                                          					 specifies the partition that is associated with the destination number. |
| Last Rd NoLast Rd No Partition | The last redirected number specifies the directory
                                          					 number from which the call was finally redirected. The last redirected number
                                          					 partition specifies the partition that is associated with the last redirected
                                          					 number. |
| Media InfoOrig Pkts Rcd Dest Pkts Rcd Orig Pkts Lost
                                          					 Dest Pkts Lost | This field specifies the packets that were received
                                          					 or lost for the origination or destination leg of a call and a link to the
                                          					 media information. |
| CDR - CMR Dump | This field specifies a link to the CDR and CDR dump
                                          					 tables. This link allows the users to view the values in the CDR/CMR fields. |

| Field | Description |
|---|---|
| Origination Leg | A unique identifier for the originating leg of a
                                          					 call. |
| Destination Leg | A unique identifier for the destination leg of a
                                          					 call. |
| Parameter | The media parameters MediaTransportAdd_Ip,
                                          					 PayLoadCapability, MediaCap_g723BitRate, Packets Sent, Octets Sent, Packets
                                          					 Received, Octets Received, Packets Lost, Jitter, Latency, QoS, VideoCap_Codec,
                                          					 VideoCap_Bandwidth, VideoCap_Resolution, VideoTransportAddress_IP, and
                                          					 VideoTransportAddress_Port |
| Origination | The value for all the preceding parameters for the
                                          					 origination leg of the call. |
| Destination | The value for all the preceding parameters for the
                                          					 destination leg of the call. |

| Note | You can view the content of the voice quality metrics field,
                                          			 varVQMetrics, in the Origination CMR and Destination CMR fields. |
|---|---|

| Field | Description |
|---|---|
| CDR | This field specifies the call detail record fields. |
| Origination CMR | Only a single set of fields for origination and
                                          					 destination exists. You can find the origination or destination CMR by using
                                          					 the leg IDs. If the leg IDs of the CMR match the Orig/Dest leg ID of the CDR,
                                          					 the following record represents Orig/Dest CMR. |
| Destination CMR | Only a single set of fields for origination and
                                          					 destination exists. You can find the origination or destination CMR by using
                                          					 the leg IDs. If the leg IDs of the CMR match the Orig/Dest leg ID of the CDR,
                                          					 the following record represents Orig/Dest CMR. |