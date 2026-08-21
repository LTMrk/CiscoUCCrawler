---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-214291-implement-ge-75a2046b21
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/214291-implement-geolocation-across-cucm-cluste.html
retrieved_at: 2026-08-21T13:58:59.384672+00:00
---

Implement GeoLocation across CUCM Clusters

# Implement GeoLocation across CUCM Clusters

### Download Options

Updated: April 17, 2019

Document ID: 214291

Contents

## Contents

## Introduction

This document is about how to extend Geolocation across multi-cluster deployment with Location Conveyance. With this new information on how to get Closed User Group (CUG) working between a cluster that is regulated and not regulated cluster with minimum configuration. It also ensures how to adhere to regulatory rules.

## Terms Associated with Geolocation

### GeoLocation

By definition, the GeoLocation is a description of the physical geographical area where something currently exists. In CUCM, geolocation assigns the location details to devices like IP phone, SIP trunk, Inter CLuster trunk (ICT) Gateway etc. which could make meaning across an enterprise, across the clusters and sites.

RFC 4119 specifies 17 Civic Location elements and UCM Logical partitioning feature implemented the manual configuration of these 17 fields/elements from Administration configurations. It recommended that you fill in all 17 fields. The fields should be named logical and short.

### Geolocation filter

Geolocation Filter is a rule to select certain fields of Geolocation in order to construct Geolocation String, which can be used to match policies for Logical Partitioning feature. i.e.  it would give sets of geolocation fields for which policies must be configured

### Geolocation Identifier

An Identifier that is identifier constructed from a combination of Geolocation, Filter & Device type. This identifier is used to compare against LP and call would be allowed or denied

A Device Geolocation ∩  Geolocation Filter  + Device type = Geolocation Identifier

i.e. A SIP trunk in CUCM can be logically represented as

Border:Country:IN:A1:KAR:A2:BAN

### Geolocation Policy Record (GLP)

The policies are not configured directly between Geolocations, because Geolocations normally have all 17 fields configured and would possibly be unique for each UCM device in a cluster. So, configure policies between Geolocations may be a lot of overhead for an Administrator, given number of Geolocations.

For the purpose to make policies, Admin needs to construct records having required data for fields of Geolocation. For this purpose, the configuration provides the provision to select data from drop-downs showing geolocation fields.

These records are called GeolocationPolicy (GLP) records.

Note : The GeolocationPolicy records should be made so that data for it matches the fields selected in filters. The hierarchy of fields is important and fields should not be missed in beginning or middle but could be missed in the end.

If fields specific to filter are not in policy, the search algorithm strips field from the end and look for a possible match in policies.

Example: If I have selected a field C, A1, A2, A6 for one LP and another LP only has C, A1, A6 then the CUCM between this 2 LP only takes C, A1 even though A6 is present in both CUCM ignores it.

### Location Conveyance

- The conveyance of GeoLocation from one SIP user agent to another entity using SIP is called Location Conveyance.

- In order to support LP requirements, the UCM's implementation additionally communicates Device type information in PIDF-LO. This is based on User Agent Capability Presence Status , as per specification in SIP extension draft-ietf-simple-prescaps-ext-08.

- The UCM's SIP Trunk supports location conveyance as per these specifications.

- In order to allow ICT to be feature compatible with SIP Trunk and allow the same capabilities, the ICT/H225 Trunk also supports location conveyance across the cluster using PIDF-LO.

- The UCM supports the conveyance of location information both at call establishment as well as location changes due to change in connected party in participation to midcall joins and redirects.

#### Implement Geolocation Across CUCM Cluster

Assumption: Have a basic understanding of geolocation and why it's needed.

For this document, we have used 2 CUCM Clusters. One cluster is assumed to residing in the US and other Cluster residing in India. We are using CUCM version 11.5 and 10.5 for the purpose of demonstration. We have a SIP trunk between the Clusters. The Dial plan is set up such that only internals calls are allowed on this ICT/SIP trunk from both clusters using CSS and partition. Dial plan has been set up such that VOIP to PSTN calls use local Gateway to make PSTN calls using CSS and partition.

India Cluster is a Logical partition enabled/aware cluster. USA cluster is a Logical partition disabled/unaware cluster. Geolocation and Geolocation filter is configured and applied for all devices on both clusters. For now, configure Logical partition in India cluster only, later a limitation is encountered due to which geolocation is enabled and configures Logical partition even on US cluster as well.

India VOIP extension : 7XXX (7001, 7002)

USA VOIP extension :  5XXX (5005)

PSTN Extension : 1XXX (1005)

This is the image with Geolocation identifiers.

## Background Information

On the India Side, TRAI regulation apply. In simple terms do not mix Non-Local VOIP call with Local PSTN call. Closed User Group (CUG) calls are allowed i.e. VOIP calls within the same Enterprise network is allowed.

When you have multiple CUCM clusters in different geographical location and one of them is regulated then objective would be

- Abide by TRAI or regulatory rules

- Have CUG working

### Theory

To get CUG working, location conveyance is used to extend Logical Partitioning policy enforcement i.e. geolocation information is sent to other clusters as the Send Geolocation Data is checked on ICT  and SIP trunk on both clusters. This enables to send and receive Geolocation information of devices and along with that, you also get to know if the device is an interior or border.

For the initial set up of the call, you need a policy such that communication between IP phone A and ICT is allowed. Once the SIP INVITE is sent to other clusters it finds out the destination device B and once this device is ringing or/and answered the call, the geolocation info of device B is sent to originating cluster through a SIP INVITE/UPDATE message. Once the Originating cluster receives valid geolocation info in the INVITE/UPDATE message which overrides the local SIP trunk Geolocation configuration and replaces this with the received geolocation.

With this new geolocation information, you can have a logical partition policy configured to allow VOIP to VOIP calls and deny VOIP call from the cluster that reaches out to Border device of a different cluster.

Note : In this scenario, all clusters must have Geolocations and Geolocation Filters configured and applied to all Device Pools. Inter-cluster calls include geolocation data and whether that participant is considered interior or border. If Geolocation data is not received on an inter-cluster call then the Geolocation and Geolocation Filter on the Trunk Configuration or inherited from the trunk’s Device Pool are used instead.

### Design

In order to Design Geolocation and logical partition, think about

- How to uniquely identify the physical place of device that places the call and device that receives the call?

- Gather information on between which geolocation/physical place do I have to have call restrictions in place.

- Out of the 17 fields, which fields when selected, you are able to take a decision on whether to allow or deny the call.

In Geolocation fields you have 17 fields, which goes from A1 to A6 till zip code. To fill from A1 it's like to zoom into a map. The more details you put, more accurately the location of the device can be pinpointed, to which this geolocation is assigned. The thing to consider is, out of all the fields in geolocation which fields should a pair of devices present to CUCM with which you are able to make an effective logical partition decision.

When Logical partitions policy is configured, you have the option to select a set of geolocation fields, select those geolocation fields such that when a device places a call presents a set of geolocation identifiers to CUCM and destination device receives a call which presents a set of geolocation identifiers to CUCM. If these fields match a predefined Logical partition policy then it is able to apply restrictions to calls.

Example. If device A has a Geolocation info A1=IN,A2=BAN,NAM=BGL14 and device B has a Geolocation A1=IN,A2=MUM,NAM=BAN1. Create a geolocation policy 1 such that A=IN,A2=BAN,NAM=BGL14. Create Policy 2 A=IN,A2=MUM,NAM=BAN1. You have to allow or deny between devices that match policy 1 and 2.

If a call is made and the origination device has Geolocation info A1=IN,A2=BAN,NAM=BGL14 then CUCM know that policy 1 can be selected. If the destination device also has Geolocation info A1=IN,A2=MUM,NAM=BAN1 then CUCM know it’s a perfect match for logical partition relation between policy 1 and 2.

Note : It is recommended that geolocation Filter fields and Logical Partition policy field select have same fields selected and matched or Logical Partition policy field be a subset of geolocation Filter fields so that when a call is made you have Logical Partition policy matched in the first iteration. You should try for a perfect match when calls are being made.

## Configuration on the CUCM

India Cluster configuration can be divided into these parts:

### Configure Geolocation

For this case, three Geolocations are created.

- For devices in India: India_GL

- For SIP trunk in ICT: India_ICT_GL

- For Devices in the US: US_GL

Note : In India cluster, an Empty_GL is configured and this is given as default geolocation. This is done so that in case you forget to add geolocation to any device through device pool then this geolocation is used to deny calls to any border device.

This image shows India_GL Configuration.

This image shows the India_ICT_GL configuration.

This image shows the US_GL configuration.

As shown in the image, for geolocation filter, Country, A1, A2, NAM fields are used.

### Enable Geolocation

Enable Logical Partitioning in the enterprise parameter, set a default policy to Deny, apply default Geolocation as Empty_GL .

### Assign Geolocation to Devices

- On the CUCM Device pool for IP phone assign India_GL.

- On the ICT SIP Trunk assign India_ICT_GL and check to send geolocation information.

Once this is done, move on to the UC cluster. You need to create a US geolocation policy and associate this with devices in the US cluster.  Ensure that Send Geolocation Information checkbox checked on SIP Trunk or ICT between US and India Cluster.

After the configuration on the US cluster is done, move back to India Cluster.

### Configure Logical Partition Policies

Three logical policies are created.

- ICT Policy : Country=IN,A1=KAR,A2=BAN,NAM=ICT

- India Policy : Country=IN,A1=KAR,A2=BAN,NAM=BGL14

- US policy : Country=US,A1=TEX,A2=SAN,NAM=BGL1

### Configure Relations between Logical Partition Policies

Once the Logical partition is configured, populate relations between the two policies.

#### ICT Logical Policy

Device type, policy and its relation with other policy tables.

Device type

Policy

Device Type

Policy

Result

Border

Country=IN,A1=KAR,A2=BAN,NAM=ICT(ICT Policy)

Border

Country=IN,A1=KAR,A2=BAN,NAM=ICT(ICT Policy)

Allow

Border

Country=IN,A1=KAR,A2=BAN,NAM=ICT(ICT Policy)

Interior

Country=IN,A1=KAR,A2=BAN,NAM=BGL14(India Policy)

Allow

- Internal IP phone is needed to reach out to ICT before you get the update of the device from US side so you have Border:Country=IN,A1=KAR,A2=BAN,NAM=ICT (ICT SIP trunk) to Interior:Country=IN,A1=KAR,A2=BAN,NAM=BGL14 (IP Phones in India) as Allow.

- In case you need to hairpin the call back to the US Then you need ICT to ICT calls as allowed so you have the relation Border:Country=IN,A1=KAR,A2=BAN,NAM=ICT to  Border:Country=IN,A1=KAR,A2=BAN,NAM=ICT  as Allow.

#### India Logical Policy

Device type, policy and its relation with other policy tables.

Device type

Policy

Device Type

Policy

Result

Interior

Country=IN,A1=KAR,A2=BAN,NAM=BGL14(India Policy)

Border

Country=IN,A1=KAR,A2=BAN,NAM=BGL14(India Policy)

Allow

With this configuration, you have Logical partition configured on India cluster only and have location conveyance between US and India clusters. You should be able to block calls between US and India cluster from mixing with PSTN and get CUG working. Test this config out by making a few calls.

## Scenarios

- IP Phone in India calls IP phone in the US.

- IP Phone in India calls IP phone in the US, India IP phone Transfers call to PSTN User.

- IP Phone in India calls IP phone in the US, India IP phone Conferences PSTN User.

- IP phone in India calls IP phone in the US, US Ext transfers this to PSTN User.

- IP phone in India calls IP phone in the US, US Ext Conferences PSTN user.

### Scenario 1: IP Phone in India calls IP phone in the US

Expected behavior: Allow the call

Observed behavior: Call is allowed

India IP phone Ext 7001 calls Us Ext 5005.

Here is the SIP trunk ladder diagram

You can split the call into two parts.

- Before you got the geolocation information from US cluster.

- After you got the geolocation information from US cluster.

If you notice there are first 200 OK and ACK for initial SIP invite. If you look closer at the 200 OK that you got from US cluster, it is noticed that the RTP port is dummy port i.e. 4000

```
SIP/2.0 200 OK Via: SIP/2.0/UDP 10.106.97.137:5060;branch=z9hG4bK68935124bc7a From: <sip:7001@10.106.97.137>;tag=26724~771bfd92-7ded-4e46-8bd8-6830680e49b2-18365227 To: <sip:5005@10.106.97.135>;tag=16120~7e829a6c-a04d-4a5f-8048-8b0b0ec17d7b-18364848 Date: Sat, 16 Mar 2019 19:52:55 GMT Call-ID: 15e0cb00-c8d15417-6828-89616a0a@10.106.97.137 CSeq: 101 INVITE Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY Allow-Events: presence, kpml Supported: replaces Server: Cisco-CUCM10.5 Supported: X-cisco-srtp-fallback Supported: Geolocation Session-Expires:  1800;refresher=uas Require:  timer P-Asserted-Identity: <sip:5005@10.106.97.135> Remote-Party-ID: <sip:5005@10.106.97.135>;party=called;screen=yes;privacy=off Remote-Party-ID: <sip:5005@10.106.97.135;user=phone>;party=x-cisco-original-called;privacy=off Contact: <sip:5005@10.106.97.135:5060> Content-Type: application/sdp Content-Length: 340 v=0 o=CiscoSystemsCCM-SIP 16120 1 IN IP4 10.106.97.135 s=SIP Call c=IN IP4 10.65.43.112 b=TIAS:64000 b=AS:64 t=0 0 m=audio 4000 RTP/AVP 9 0 8 116 3 18 a=rtpmap:9 G722/8000 a=rtpmap:0 PCMU/8000 a=rtpmap:8 PCMA/8000 a=rtpmap:116 iLBC/8000 a=maxptime:60 a=fmtp:116 mode=20 a=rtpmap:3 GSM/8000 a=rtpmap:18 G729/8000 a=sendonly
```

RTP has not started to flow yet. After the ACK you see one more SIP INVITE and in this, you have Geolocation info sent out to yourself.

```
INVITE sip:7001@10.106.97.137:5060 SIP/2.0 Via: SIP/2.0/UDP 10.106.97.135:5060;branch=z9hG4bK11f6de9436 From: <sip:5005@10.106.97.135>;tag=16120~7e829a6c-a04d-4a5f-8048-8b0b0ec17d7b-18364848 To: <sip:7001@10.106.97.137>;tag=26724~771bfd92-7ded-4e46-8bd8-6830680e49b2-18365227 Date: Sat, 16 Mar 2019 19:53:00 GMT Call-ID: 15e0cb00-c8d15417-6828-89616a0a@10.106.97.137 Supported: timer,resource-priority,replaces Cisco-Guid: 0367053568-0000065536-0000000033-2304862730 User-Agent: Cisco-CUCM10.5 Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY CSeq: 101 INVITE Max-Forwards: 70 Expires: 180 Allow-Events: presence, kpml Supported: X-cisco-srtp-fallback Supported: Geolocation Session-Expires:  1800;refresher=uac Min-SE:  1800 Geolocation: <cid:5005@10.106.97.135>;inserted-by="10.106.97.135" P-Asserted-Identity: <sip:5005@10.106.97.135> Remote-Party-ID: <sip:5005@10.106.97.135>;party=calling;screen=yes;privacy=off Contact: <sip:5005@10.106.97.135:5060> Content-Type: multipart/mixed;boundary=uniqueBoundary Mime-Version: 1.0 Content-Length: 1219 --uniqueBoundary Content-Type: application/sdp v=0 o=CiscoSystemsCCM-SIP 16120 2 IN IP4 10.106.97.135 s=SIP Call c=IN IP4 10.65.43.112 b=TIAS:64000 b=AS:64 t=0 0 m=audio 25344 RTP/AVP 9 a=ptime:30 a=rtpmap:9 G722/8000 --uniqueBoundary Content-Type: application/pidf+xml Content-ID: <5005@10.106.97.135> <?xml version="1.0" encoding="UTF-8"?> <presence xmlns="urn:ietf:params:xml:ns:pidf" xmlns:gp="urn:ietf:params:xml:ns:pidf:geopriv10" xmlns:cl=" urn:ietf:params:xml:ns:pidf:geopriv10:civicLoc" xmlns:dm="urn:ietf:params:xml:ns:pidf:data-model" xmlns:caps="urn:ietf:params:xml:ns:pidf:caps" xmlns:cisco="http://www.cisco.com" entity="pres:geotarget@example.com"> <dm:device id="sg89ae"> <caps:devcaps> <cisco:gateway>false</cisco:gateway> </caps:devcaps> <gp:geopriv> <gp:location-info> <cl:civicAddress> <cl:country>US</cl:country> <cl:A1>TEX</cl:A1> <cl:A2>SAN</cl:A2> <cl:NAM>BGL1</cl:NAM> </cl:civicAddress> </gp:location-info> <gp:usage-rules> <gp:retransmission-allowed>yes</gp:retransmission-allowed> <gp:retention-expiry>2019-03-17T19:53:00Z</gp:retention-expiry> </gp:usage-rules> </gp:geopriv> <timestamp>2019-03-16T19:53:00Z</timestamp> </dm:device> </presence> --uniqueBoundary--
```

In this Invite, you see the RTP port number that the US IP phone will use. The Geolocation info of the IP phone and info on whether this is a gateway or not is sent over to India cluster. With this new Geolocation info, once again logical partitions are matched in India cluster to see if the call should be allowed or denied. As these are interior to interior calls, the logical partition is not applied and the call is allowed

### Scenario 2: IP Phone in India calls IP Phone in the US, India IP Phone Transfers Call to PSTN User

Expected behavior: Deny the call

Observed behavior: Call is Denied

India IP phone Ext 7001 calls Us Ext 5005, hits transfer softkey first time, dials PSTN number 1005, presses transfer key but nothing happens.

In the CUCM traces, you see.

```
01192372.012 |01:51:49.984 |AppInfo  |LPPolicyManager -getLogicalPartitionPolicy, devtypeA[Border] , devtypeB[Interior] 01192372.013 |01:51:49.984 |AppInfo  |LogicalPolicyTree -searchPolicy devTypeA[Border], devTypeB[Interior] 01192372.014 |01:51:49.984 |AppInfo  |GeolocNamValPair -printList: country = IN, A1 = KAR, A2 = BAN, NAM = BGL14, 01192372.015 |01:51:49.984 |AppInfo  |GeolocNamValPair -printList: country = US, A1 = TEX, A2 = SAN, NAM = BGL1, 01192372.074 |01:51:49.984 |AppInfo  |LPPolicyManager -findLogicalPartitionPolicyUsingVals, DEFAULT POLICY found is [2] 01192372.075 |01:51:49.984 |AppInfo  |LPPolicyManager -findLogicalPartitionPolicyUsingVals, POLICY found is [9] 01192372.076 |01:51:49.984 |AppInfo  |Transferring - LPPolicy Result [9] 01192372.077 |01:51:49.984 |AppInfo  |LPPolicyManager -incLogicalPPerfmon, perfMon[0] 01192372.078 |01:51:49.984 |AppInfo  |Transferring - handleTransferErrorPreStart, ERROR fid=[4], Retaining Calls, xferring[1, 18365238], xferred[1, 18365239]. infoCause=53, clearCause=63 01192668.001 |01:51:56.765 |AppInfo  |StationD:    (0000019) DisplayNotify timeOutValue=10 notify='a' content='External Transfer Restricted' ver=8560000c.
```

On the India cluster party, A is going to a PSTN device i.e. border element. You have not set any allow between India border and US interior so you use the default policy set to deny and call is blocked.

### Scenario 3: IP Phone in India calls IP Phone in the US, India IP Phone Conferences PSTN User

Expected behavior : Deny the call

Observed behavior : Call is Denied

India IP phone Ext 7001 calls Us Ext 5005, India IP phone Ext 7001 clicks Confrn softkey the first time, dials PSTN number 1005, clicks Confrn softkey, as shown in the image. However,  you see Conference is unavailable.

In the CUCM logs, you see this:

```
01213687.146 |02:00:35.806 |AppInfo  |LogicalPolicyTree -searchPolicy devTypeA[Border], devTypeB[Interior] 01213687.147 |02:00:35.806 |AppInfo  |GeolocNamValPair -printList: country = IN, A1 = KAR, A2 = BAN, NAM = BGL14, 01213687.148 |02:00:35.806 |AppInfo  |GeolocNamValPair -printList: country = US, A1 = TEX, A2 = SAN, NAM = BGL1, 01213687.207 |02:00:35.806 |AppInfo  |LPPolicyManager -findLogicalPartitionPolicyUsingVals, DEFAULT POLICY found is [2] 01213687.208 |02:00:35.806 |AppInfo  |LPPolicyManager -findLogicalPartitionPolicyUsingVals, POLICY found is [9] 01213687.209 |02:00:35.806 |AppInfo  |Conference: processGeoLocationResultListForConfRequest:ci=18365306,status=9
```

On the India cluster party, A is going to a PSTN device i.e. border element. You have not set any allow between India border and US interior so you use the default policy that is set to deny and call is blocked.

### Scenario 4: IP Phone in India calls IP Phone in the US, US Ext Transfers this to PSTN User

Expected behavior: Deny the call

Observed behavior: Call is Denied

India IP phone Ext 7001 calls US IP phone Ext 5005,  US IP phone Ext 5005 clicks transfer softkey first time, dials PSTN number 1005, clicks transfer key again.

When the US extension transfers the call to PSTN, you get an update from the US cluster.

```
UPDATE sip:7001@10.106.97.137:5060 SIP/2.0 Via: SIP/2.0/UDP 10.106.97.135:5060;branch=z9hG4bKbe39bb25ad From: <sip:5005@10.106.97.135>;tag=6376~7e829a6c-a04d-4a5f-8048-8b0b0ec17d7b-18364784 To: <sip:7001@10.106.97.137>;tag=9968~771bfd92-7ded-4e46-8bd8-6830680e49b2-18365199 Date: Wed, 13 Mar 2019 10:57:03 GMT Call-ID: b6619180-c881e1f8-26cd-89616a0a@10.106.97.137 User-Agent: Cisco-CUCM10.5 Max-Forwards: 70 Supported: timer,resource-priority,replaces Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY CSeq: 103 UPDATE Call-Info: <urn:x-cisco-remotecc:callinfo>;x-cisco-video-traffic-class=MIXED Supported: X-cisco-srtp-fallback Supported: Geolocation Session-Expires:  1800;refresher=uac Min-SE:  1800 Geolocation: <cid:1005@10.106.97.135>;inserted-by="10.106.97.135" P-Asserted-Identity: <sip:1005@10.106.97.135> Remote-Party-ID: <sip:1005@10.106.97.135> ;party=calling;screen=yes;privacy=off Contact: <sip:1005@10.106.97.135:5060> Content-Type: application/pidf+xml Content-ID: 1005@10.106.97.135 Content-Length: 872 <?xml version="1.0" encoding="UTF-8"?> <presence xmlns="urn:ietf:params:xml:ns:pidf" xmlns:gp="urn:ietf:params:xml:ns:pidf:geopriv10" xmlns:cl=" urn:ietf:params:xml:ns:pidf:geopriv10:civicLoc" xmlns:dm="urn:ietf:params:xml:ns:pidf:data-model" xmlns:caps="urn:ietf:params:xml:ns:pidf:caps" xmlns:cisco="http://www.cisco.com" entity="pres:geotarget@example.com"> <dm:device id="sg89ae"> <caps:devcaps> <cisco:gateway>true</cisco:gateway> </caps:devcaps> <gp:geopriv> <gp:location-info> <cl:civicAddress> <cl:country>US</cl:country> <cl:A1>TEX</cl:A1> <cl:A2>SAN</cl:A2> <cl:NAM>BGL1</cl:NAM> </cl:civicAddress> </gp:location-info> <gp:usage-rules> <gp:retransmission-allowed>yes</gp:retransmission-allowed> <gp:retention-expiry>2019-03-14T10:57:14Z</gp:retention-expiry> </gp:usage-rules> </gp:geopriv> <timestamp>2019-03-13T10:57:14Z</timestamp> </dm:device> </presence>
```

In the update, you see that the device that it interacts with is a border element. With this info, CUCM on India side now once again applies a logical partition on this call and the result is deny the call .

In the CUCM logs, you see this:

```
00443670.032 |16:27:14.830 |AppInfo  |LPPolicyManager -getLogicalPartitionPolicy, devtypeA[Interior], devtypeB[Border] 00443670.033 |16:27:14.830 |AppInfo  |LogicalPolicyTree -searchPolicy devTypeA[Interior], devTypeB[Border] 00443670.034 |16:27:14.830 |AppInfo  |GeolocNamValPair -printList: country = IN, A1 = KAR, A2 = BAN, NAM = BGL14, 00443670.035 |16:27:14.830 |AppInfo  |GeolocNamValPair -printList: country = US, A1 = TEX, A2 = SAN, NAM = BGL1, 00443670.064 |16:27:14.830 |AppInfo  |LPPolicyManager -findLogicalPartitionPolicyUsingVals, DEFAULT POLICY found is [2] 00443670.065 |16:27:14.830 |AppInfo  |LPPolicyManager -findLogicalPartitionPolicyUsingVals, POLICY found is [9]
```

Party B i.e. the device from the US is now updated from Internal to border element. The default policy is matched and the default policy in India cluster is Deny .

### Scenario 5: IP Phone in India calls IP Phone in the US, US Ext Conferences PSTN User

Expected behavior: Deny the call

Observed behavior: Call is allowed

This Last scenario the call works, just with Location conveyance we will not be able to block the conference call that is initiated in the US by the logical partitions configured in India cluster. This is a Limitation of this configuration. In order to overcome this limitation, you then have to configure Logical Partition on the UC cluster as well.

The next section of config has to be done on the US CLuster side.

## US Cluster Configuration

US Cluster configuration can be divided into these parts.

- Configuring Geolocation

- Enabling Geolocation

- Assigning Geolocation to devices

- Configuring Logical partition policies

- Configuring relation between Logical partition policies

### Configure Geolocation

For this case, three Geolocations are created.

- For devices in India: India_GL

- For SIP trunk in ICT: US_ICT_GL

- For Devices in the US: US_GL

This image shows the US_GL Configuration.

This image shows the US_ICT_GL Configuration.

This image shows the India_GL Configuration.

For filter, Country A1, A2, NAM fields are used, as shown in the image.

### Enable Geolocation

Enable Logical Partition on enterprise parameter, Default policy as Allow.

### Assign Geolocation to devices

Note : By now you would have already configured device pool of US IP phone with geolocation US_GL.

Assign US_ICT_GL to ICT SIP trunk in the US cluster.

### Configure Logical partition policies

Two logical policies are created in the US Cluster.

- India Policy :  Country=IN,A1=KAR,A2=BAN,NAM=BGL14

- US Policy : Country=US,A1=TEX,A2=SAN,NAM=BGL1

#### US Logical Policy

Device type, policy and its relation with other policy tables.

Device type

Policy

Device Type

Policy

Result

Border

Country=US,A1=TEX,A2=SAN,NAM=BGL1(US Policy)

Interior

Country=IN,A1=KAR,A2=BAN,NAM=BGL14(India Policy)

Deny

This config in place the case of IP phone in India calls IP phone in the US, US IP phone Conferences PSTN user is now blocked.

You see this error message on the US IP phone when we try to conference US PSTN user with India IP phone.

Once Geolocation has been configured in the US cluster, the behavior for Scenario 2 and 4 are the same. The India cluster does not have to wait for a SIP UPDATE/INVITE from US cluster as the deny of calls will happen on the US cluster itself due to logical partition coming into effect on US side.

With this, you should have CUG working between India and US cluster and ensure that you do not mix VOIP call of one cluster with PSTN call of another cluster.

## Scale up in Future

### Adding a new cluster to the enterprise network

To scale up and accommodate new clusters, Assume you have 2 new clusters to add. UK Cluster and France Cluster.

In terms of config with the existing setup, you add these

In The India Side

- You just need to add a UK Geolocation and France Geolocation in the India Cluster.

- Assign ICT Geolocation to SIP trunk going to UK and France.

- Ensure that Send Geolocation Information checkbox is checked on SIP Trunk or ICT.

The UK Cluster

- Create Geolocation for UK, ICT and India with the same filter as other clusters (Similar to US cluster config).

- Keep the default policy as allow.

- Ensure that Send Geolocation Information checkbox is checked on SIP Trunk or ICT.

- Assign Geolocation and Geolocation filter to SIP trunk/ICT as ICT.

- Create 2 logical policy UK policy and India Policy.

- In the UK policy configure logical partition relation between UK border to India interior as deny.

The France Cluster

- Create Geolocation for France, ICT and India with the same filter as other clusters (Similar to US cluster config).

- Keep the default policy as allow.

- Ensure that Send Geolocation Information checkbox is checked on SIP Trunk or ICT.

- Assign Geolocation and Geolocation filter to SIP trunk/ICT as ICT.

- Create 2 logical policy, France policy and India Policy.

- In France, policy configures logical partition relation between France border to India interior as deny.

Adding any new cluster from a different county would be following the above steps. This keeps the configuration to a minimum and is able to scale if you add more clusters

### What to Do if You Have an SME?

SME acts as a carrier of geolocation information without participating in any logical partitioning on the SME cluster.

- Check to Send Geolocation Information checkbox on SIP Trunk or ICT.

- No need for geolocation config on SME.

.

All Geolocation config and logical partitioning are done on the leaf node only. The configuration on the leaf node is similar to a geolocation configuration between 2 clusters over ICT. The SME simply passes on the geolocation information that it receives on one trunk to another trunk as it acts as a proxy.

Note : The List is by no means exhaustive. As an admin you have to test call park and Callpick up(Local and remote), SNR, EM, EMCC, Huntpilot, CTI related transfer and conference, Adhoc, Meet-Me Conference on both the cluster and test it out.

## Limitation

Conference chaining - e.g MeetMe & Adhoc chained conference can have participants which are LP denied but can't be prevented to be in communication.

Recommendation - Disable Conference chaining from its Service parameter.

Corner case of CBarge/Barge - When the connected party is a conference bridge due to an active feature, such as Conference or Meet-Me, and an active shared-line device associates with geolocation that is allowed for all the devices in the Conference, the remote-in-use shared-line device shows call instance information. In this case, the remote-in-use phone can always perform the cBarge/Barge feature even if a disallowed participant participates in the conference. For the participants in cBarge/Barge, no logical partitioning policy checking exists and logical-partitioning-denied scenarios cannot be prevented.

## Related Information

- Technical Support & Documentation - Cisco Systems

| Device type | Policy | Device Type | Policy | Result |
|---|---|---|---|---|
| Border | Country=IN,A1=KAR,A2=BAN,NAM=ICT(ICT Policy) | Border | Country=IN,A1=KAR,A2=BAN,NAM=ICT(ICT Policy) | Allow |
| Border | Country=IN,A1=KAR,A2=BAN,NAM=ICT(ICT Policy) | Interior | Country=IN,A1=KAR,A2=BAN,NAM=BGL14(India Policy) | Allow |

| Device type | Policy | Device Type | Policy | Result |
|---|---|---|---|---|
| Interior | Country=IN,A1=KAR,A2=BAN,NAM=BGL14(India Policy) | Border | Country=IN,A1=KAR,A2=BAN,NAM=BGL14(India Policy) | Allow |

| Device type | Policy | Device Type | Policy | Result |
|---|---|---|---|---|
| Border | Country=US,A1=TEX,A2=SAN,NAM=BGL1(US Policy) | Interior | Country=IN,A1=KAR,A2=BAN,NAM=BGL14(India Policy) | Deny |