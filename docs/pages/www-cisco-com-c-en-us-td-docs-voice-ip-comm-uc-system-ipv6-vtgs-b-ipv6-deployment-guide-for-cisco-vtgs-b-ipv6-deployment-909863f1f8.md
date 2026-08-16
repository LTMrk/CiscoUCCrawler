---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-ipv6-vtgs-b-ipv6-deployment-guide-for-cisco-vtgs-b-ipv6-deployment-909863f1f8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/IPv6/vtgs_b_ipv6-deployment-guide-for-cisco/vtgs_b_ipv6-deployment-guide-for-cisco_chapter_0110.html
retrieved_at: 2026-08-16T18:22:14.656040+00:00
---

IPv6 Deployment Guide

# IPv6 Deployment Guide

Updated: October 18, 2024

Chapter: Trunks

## Chapter: Trunks

# Trunks

## Trunks Overview

Cisco Unified Communications Manager (Unified CM) supports several different types of IP trunks for connectivity with external
                           devices:

H.225 (H.323)

SIP

Intercluster trunks

Only SIP trunks and SIP intercluster trunks can support IPv6. This chapter describes the new IPv6 features and capabilities
                           of these trunks. For information on the general capabilities and functions of Unified CM trunks, refer to the Cisco Collaboration
                           System Solution Reference Network Design (SRND), available at Link .

There are several possible configurations for Unified CM SIP trunks:

Inbound and outbound SIP Early Offer trunk calls

Inbound and outbound SIP Delayed Offer trunk calls (This chapter focuses on this supported option)

## IPv6 SIP Trunks Configuration

To configure SIP trunks to gateways and Unified CM SIP intercluster trunks, select Devices > Trunks > SIP Trunk in Unified CM Administration .

The SIP trunk configuration settings discussed in this section are applied through the Common Device Configuration profile
                           that is created and assigned to the SIP trunk ( IP Addressing Mode and IP Addressing Mode Preference for Signaling ), and through the SIP Profile configuration assigned to the SIP trunk ( ANAT is not enabled ). The IPv4 to IPv6 media interworking is supported by Unified CM inserting MTPs.

### Common Device Configuration Settings for SIP Trunks

This section describes the configuration settings for SIP trunks.

#### SIP Trunk IP Addressing Mode

You can configure the IP Addressing Mode to one of the following settings:

IPv4

In this mode, the SIP trunk uses the Unified CM IPv4 address for signaling and either an MTP or phone IPv4 address for media.

IPv6

In this mode, the SIP trunk uses the Unified CM IPv6 address for signaling and either an MTP or phone IPv6 address for media.

IPv4 and IPv6

The SIP trunk uses either the Unified CM IPv4 address or the Unified CM IPv6 address for signaling, and an MTP or other trunk
                                          address for media.

#### SIP Trunk IP Addressing Mode Preference for Signaling

You can configure the IP Addressing Mode Preference for Signaling to one of the following settings:

IPv4

In this mode, the SIP trunk uses the Unified CM IPv4 server address as its source address for SIP signaling.

IPv6

In this mode, the SIP trunk uses the Unified CM IPv6 server address as its source address for SIP signaling.

Use System Default

In this mode, the SIP trunk uses the cluster-wide Enterprise Parameter configuration value for its IP addressing mode for
                                          signaling.

If IPv6 is enabled in the Unified CM cluster, the default SIP trunk setting for the IP Addressing Mode for Signaling is Use System Default . With this setting, the SIP trunk adopts the cluster-wide setting for its IP addressing mode for signaling, if the trunk
                                    is configured with a destination address of that type. All IPv4 trunks ignore this setting.

The SIP trunk's IP Addressing Mode Preference for Signaling is used only for outbound calls. Unified CM listens for incoming
                                    SIP signaling on both the IPv4 and IPv6 address.

##### Allow Auto-Configuration for Phones

The setting of Allow Stateful Auto-Configuration for Phones is not used by SIP trunks.

## Supported IPv6 SIP Trunk Configurations and Associated Call Flows

How you configure your Unified CM IPv6 SIP trunk will, to some extent, depend upon the capabilities of the far-end SIP trunk
                              device. Usually this far-end SIP trunk device is another Unified CM cluster, IPv6 SIP gateway, or third-party IPv6 SIP call
                              agent.

Some general guidance on IPv6 SIP trunk configuration:

IPv6 SIP trunks should be configured with an IP addressing mode of IPv4 and IPv6.

SIP Early Offer and SIP Delayed Offer are supported, both in symmetric and asymmetric configurations, as follows:

Outbound and inbound SIP Early Offer ( Supported option)

Outbound and inbound SIP Delayed Offer

Outbound SIP Early Offer and inbound SIP Delayed Offer

Outbound SIP Delayed Offer and inbound SIP Early Offer

### Early Offer and SIP Trunk Calls

For all Unified CM SIP trunks, you must check the MTP required check box on the trunk configuration page to enable SIP Early Offer in IPv4 (IPv6 does not support Early Offer). When MTP required is checked, a media termination point (MTP) is used in the media path for all inbound and outbound calls. This statically
                                 assigned MTP affects all calls in the following ways:

Because the MTP is placed in the media path for all calls, rather than having one call leg from the calling phone to the called
                                       phone, the insertion of the MTP creates two legs: one from the calling phone to the MTP, and the other from the MTP to the
                                       called phone. For signaling purposes, this can be considered to be two calls. The calling phone and MTP negotiate media capabilities
                                       (such as codec, IP addresses, and UDP port numbers to be used), as do the MTP and the called phone at the far end of the SIP
                                       trunk.

The statically assigned MTP ( MTP required checked) must be configured to use one codec type (G711 or G729). Assigning a single voice codec to this statically assigned
                                       MTP disables the use of the pass-through codec. This, in turn, prevents the negotiation of the pass-through codec that is
                                       required for video calls or encrypted calls. (T.38 fax calls are supported with statically assigned MTPs.) Therefore, if support
                                       for video or encryption is required over the SIP trunk, SIP Delayed Offer (no statically assigned MTP) must be used.

The pass-through codec should be configured on all dynamically inserted MTPs. To enable the use of the pass-through codec,
                                                   configure the MTP with both a standard codec and the pass-through codec.

If SIP Early Offer is required for dual-stack SIP Unified CM trunks, then you must configure the Cisco IOS MTP to use both
                                 an IPv6 and IPv4 address. For details, see Media Resources and Music on Hold Overview .

### Delayed Offer and SIP Trunks

Delayed Offer trunks do not have a statically assigned MTP and therefore MTP resources are not used for every call. For Delayed
                                 Offer calls, Unified CM attempts to set up the call using a single call leg between the calling and called device, and in
                                 doing so must consider the IP addressing mode configuration of both the Unified CM trunk and the IP phone registered with
                                 Unified CM. In certain calls where there are IP addressing mode mismatches between the Unified CM trunk and the registered
                                 phone, Unified CM dynamically inserts an MTP to resolve this mismatch. The pass-through codec is supported by this dynamically
                                 inserted MTP, and video calls and encrypted calls can be established with this MTP in the call path. The pass-through codec
                                 should be configured on all dynamically inserted MTPs. To enable the use of the pass-through codec, configure the MTP with
                                 both a standard codec and the pass-through codec.

### Unified CM SIP Trunk Signaling

The following factors affect which IP addressing version is used for signaling on Unified CM SIP trunks:

Call direction

IP addressing mode of the trunk

Configured destination addresses of the trunk

Trunk's IP addressing mode preference for signaling

Cluster-wide IP addressing mode preference for signaling

#### IP Addressing Version Used for SIP Signaling for Outbound

The IP addressing version for signaling is determined by the following factors, in the order listed here:

The IP Addressing Mode of the SIP trunk (IPv4 or IPv6)

The configured destination addresses of the SIP trunk (IPv4 or IPv6)

If only one destination address is configured (IPv4 or IPv6), the IP addressing version must match the IP Addressing Mode
                                                of the trunk. If these two values do not match, the SIP trunk connection is not established.

If two trunk destination addresses are configured (IPv4 and IPv6), then the IP addressing version is determined by the SIP
                                                trunk's IP Addressing Mode Preference for Signaling (IPv4, IPv6, or Use System Default). If the Use System Default setting is used, then the IP addressing version is determined by the cluster-wide IP Addressing Mode Preference for Signaling
                                                (IPv4 or IPv6).

#### IP Addressing Version Used for SIP Signaling for Inbound

For inbound calls, the IP addressing version used for signaling is based on the trunk destination addresses and port numbers
                                    configured in Unified CM. If the signaling source address and port number received from the calling device match a configured
                                    destination address and port number on the SIP trunk, then the signaling connection is established.

Unified CM provides the following configuration setting options for the SIP trunk destination address:

One IPv4 address configured

One IPv6 address configured

One IPv4 and one IPv6 address configured

If IPv6 is enabled in the cluster, Unified CM servers listen for incoming SIP trunk calls destined to their configured IPv4
                                    and IPv6 addresses and source port number.

## Media Address Selection for Calls over Dual-Stack SIP Trunks

Many configuration options are possible for SIP trunks. Trunks may be single or dual stack and use SIP Early Offer or SIP
                              Delayed Offer. This chapter, while not exhaustive, discusses the significant configuration options and their outcomes in terms
                              of the addresses that are exchanged and used for media. Early Offer call scenarios are considered first, followed by Delayed
                              Offer call scenarios.

Depending on the call scenario, media address selection for calls over dual-stack SIP trunks can be based on:

Call direction

Whether Delayed Offer or Early Offer is used

The IP Addressing Mode of the trunk

The cluster-wide IP Addressing Mode Preference for Media

The IP Addressing Mode of the phone

The remaining sections of this chapter review media selection for the following Unified CM call flows:

SIP Early Offer calls

Outbound Early Offer calls without ANAT

Inbound Early Offer calls without ANAT

SIP Delayed Offer calls

Outbound Delayed Offer calls without ANAT

Inbound Delayed Offer calls without ANAT

### Media Selection for Outbound IPv6 Early Offer Calls Without ANAT

SIP Early Offer calls involve two call legs: one from the phone to trunk MTP, and the other from the trunk MTP to the SIP
                                 voice gateway. The Cisco IOS MTP is configured to support both IPv4 and IPv6 addresses. ANAT has not been enabled on the SIP
                                 trunk in the following figure, so as with a standard SIP trunk, only a single IP addressing version is exchanged.

#### Call Leg from Phone to Trunk MTP: Standard Unified CM In-Cluster Negotiation

The MTP is dual-stacked and can match the media addressing type of the phone if it is set to IPv4-only or IPv6-only. If the
                                 phone is also dual-stacked, the cluster-wide IP Addressing Mode Preference for Media (IPv4 or IPv6) determines which IP addressing
                                 version is used for media.

#### Call Leg from MTP Trunk to Voice Gateway: ANAT Not Enabled, and One Media Address Is Sent in SDP (IPv4 or IPv6)

For outbound Early Offer calls where ANAT is not enabled, the IP Addressing Mode of the SIP trunk determines what is sent
                                 in the SDP body of the SIP Offer, as follows:

IP Addressing Mode = IPv4 only—The IPv4 address of the MTP is sent in the SDP body.

IP Addressing Mode = IPv6 only—The IPv6 address of the MTP is sent in the SDP body.

IP Addressing Mode = IPv4 and IPv6—The cluster-wide IP Addressing Mode Preference for Media (IPv4 or IPv6) is used to determine
                                       which MTP address is sent in the SDP body.

### Media Selection for Inbound Early Offer Calls Without ANAT (IPv6 Not Supported)

IPv6 is not supported.

SIP Early Offer calls involve two call legs: one from the phone to the trunk MTP, and the other from the trunk MTP to the
                                 SIP voice gateway. The Cisco IOS MTP is configured to support both IPv4 and IPv6 addresses. ANAT has not been enabled on the
                                 SIP trunk in Figure 7-6, so as with a standard SIP trunk, only a single IP addressing version is exchanged in the SIP Offer
                                 and Answer.

#### Call Leg from Trunk MTP to Phone: Standard Unified CM In-Cluster Negotiation

The MTP is dual-stacked and can match the media addressing type of the phone if it is set to IPv4 only or IPv6 only. If the
                                 phone is also dual-stacked, the cluster-wide IP Addressing Mode Preference for Media (IPv4 or IPv6) determines which IP addressing
                                 version is used for media.

#### Call Leg from Voice Gateway to Trunk MTP: ANAT Not Enabled, and One Media Address Is Received in SDP

For inbound Early Offer calls where ANAT is not enabled, the IP Addressing Mode of the SIP trunk determines whether the address
                                 received in the SDP body of the SIP Offer is accepted or rejected, as follows:

IP Addressing Mode = IPv4 only:

If an IPv4 address is received in the SDP body, proceed with the call.

If an IPv6 address is received in the SDP body, reject the call.

IP Addressing Mode = IPv6 only:

If an IPv6 address is received in the SDP body, proceed with the call.

If an IPv4 address is received in the SDP body, reject the call.

For these trunk calls, Unified CM does not insert an MTP to resolve a media addressing version mismatch between the two voice
                                                   devices.

IP Addressing Mode = IPv4 and IPv6:

If an IPv4 address is received in the SDP body, proceed with the call.

If an IPv6 address is received in the SDP body, proceed with the call.

## SIP Trunks Using Delayed Offer

With Delayed Offer, SIP trunks do not use a statically assigned MTP, and typically only one call leg is created between the
                              calling phone and called phone or device. From the perspective of Unified CM, this makes the selection of which IP addressing
                              version to use a little more involved because in this case both the trunk's settings and the phone's settings must be taken
                              into account.

### Media Selection for Outbound Delayed Offer Calls Over Unified CM SIP Trunks Without ANAT

As shown in the following figure, SIP Delayed Offer calls typically involve a single call leg from the phone to the SIP voice
                                 gateway. ANAT has not been enabled on this SIP trunk, so as with a standard SIP trunk, only a single IP addressing version
                                 is exchanged in the SIP Offer and Answer.

For outbound Delayed Offer calls, the IP Addressing Mode settings of both the trunk and the phone influence the call setup
                                 in the following ways:

The IP Addressing Mode setting of the trunk determines whether the received SIP Offer is accepted or rejected.

The IP Addressing Mode setting of the phone determines which address (phone or MTP) is returned in the SIP Answer from Unified
                                       CM.

In this scenario, Unified CM can dynamically insert an MTP, if needed, into the call to convert the IP addressing version
                                 of the voice media stream between the calling and called devices. As mentioned previously, dynamically inserted MTPs support
                                 the pass-through codec, allowing video calls and encrypted calls to be established.

#### IP Addressing Mode of the Trunk

IP Addressing Mode = IPv4 only:

If an IPv4 address is received in the SDP body, proceed with the call.

If an IPv6 address is received in the SDP body, reject the call.

IP Addressing Mode = IPv6 only:

If an IPv6 address is received in the SDP body, proceed with the call.

If an IPv4 address is received in the SDP body, reject the call.

For trunk call signaling, Unified CM does not insert an MTP to resolve a media addressing version mismatch.

IP Addressing Mode = IPv4 and IPv6 (Supported configuration):

If an IPv4 address is received in the SDP body, proceed with the call.

If an IPv6 address is received in the SDP body, proceed with the call.

For SIP trunks using Delayed Offer and not using ANAT, the supported trunk IP Addressing Mode setting is IPv4 and IPv6 because both IPv6 calls and IPv4 calls are accepted by the trunk.

#### IP Addressing Mode of the Phone

IP Addressing Mode = IPv4 only:

If an IPv4 address is received in the SDP body, proceed with the call and return the IPv4 address of the phone in the SDP
                                             body of the SIP answer.

If an IPv6 address is received in the SDP body, dynamically insert an MTP into the media path to convert IP addressing versions,
                                             then proceed with the call. Return the IPv6 address of the MTP in the SDP body of the SIP answer.

IP Addressing Mode = IPv6 only:

If an IPv6 address is received in the SDP body, proceed with the call and return the IPv6 address of the phone in the SDP
                                             body of the SIP answer.

If an IPv4 address is received in the SDP body, dynamically insert an MTP into the media path to convert IP addressing versions,
                                             then proceed with the call. Return the IPv4 address of the MTP in the SDP body of the SIP answer.

IP Addressing Mode = IPv4 and IPv6:

If an IPv4 address is received in the SDP body, proceed with the call and return the IPv4 address of the phone in the SDP
                                             body of the SIP answer.

If an IPv6 address is received in the SDP body, proceed with the call and return the IPv6 address of the phone in the SDP
                                             body of the SIP answer.

#### When an MTP Is Required, Will the MTP of the Phone or the Trunk Be Used?

The cluster-wide IP Addressing Mode Preference for Media determines whether the MTP of the phone or of the trunk is used to
                                 convert the voice media stream between IPv4 and IPv6. This preference is used to select an MTP so that the longest Real-Time
                                 Transport Protocol (RTP) call leg in the cluster matches the cluster-wide preference.

#### Deployment Considerations for Delayed Offer Calls over Trunks without ANAT

If a call from an IPv4-only phone receives a SIP Offer that contains an IPv6 address, or if a call from an IPv6-only phone
                                 receives a SIP Offer that contains an IPv4 address, Unified CM dynamically inserts an MTP to convert between IPv4 and IPv6.
                                 In deployments with large numbers of IPv4-only phones, any SIP trunk call to or from an IPv6-only device requires an MTP for
                                 conversion between IPv4 and IPv6. Therefore, we recommend that you provide MTP resources for IPv4-only and IPv6-only devices
                                 in the Unified CM cluster.

### Media Selection for Inbound Delayed Offer Calls Over Unified CM SIP Trunks Without ANAT

As shown in the following figure, SIP Delayed Offer calls typically involve a single call leg from the phone to the SIP voice
                                 gateway. ANAT has not been enabled on this SIP trunk, so as with a standard SIP trunk, only a single IP addressing version
                                 is exchanged in the SIP Offer and Answer.

For inbound Delayed Offer calls, the combined settings of the IP Addressing Mode of both the trunk and the phone determine
                                 which IP addressing version and which device's IP address is sent in the SDP body of the SIP Offer.

For inbound Delayed Offer calls, if a mismatch exists between the IP addressing modes of the phone and the trunk, Unified
                                 CM can dynamically insert an MTP into the call path to convert the IP addressing version of the voice media stream from the
                                 IP phone, so that it matches that configured on the trunk. In this case, the address of the MTP is sent in the SDP body of
                                 Unified CM's SIP Offer.

For SIP trunks using Delayed Offer and not using ANAT, the supported IP Addressing Mode setting for the trunk is IPv4 and IPv6 . With this setting, Unified CM does not need to insert MTPs for inbound SIP Delayed Offer calls.

#### When an MTP Is Required, Will the MTP of the Phone or the Trunk Be Used?

The cluster-wide IP Addressing Mode Preference for Media determines whether the MTP of the phone or of the trunk is used to
                                 convert the voice media stream between IPv4 and IPv6. See the following table for details. This preference is used to select
                                 an MTP so that the longest Real-Time Transport Protocol (RTP) call leg in the cluster matches the cluster-wide preference.

As mentioned previously, dynamically inserted MTPs do support the pass-through codec, allowing video calls and encrypted calls
                                 to be established.

IP Addressing Mode of Phone

IP Addressing Mode of Trunk

Address Sent in SIP Offer by Unified CM

IPv4 Only

IPv4 Only

IPv4 address of phone

IPv4 Only

IPv4 and IPv6

IPv4 address of phone

IPv6 Only

IPv6 Only

IPv6 address of phone

IPv6 Only

IPv4 and IPv6

IPv6 address of phone

IPv4 Only

IPv6 Only

Insert an MTP and use its IPv6 address.

IPv6 Only

IPv4 Only

Insert an MTP and use its IPv4 address.

IPv4 and IPv6

IPv4 Only

IPv4 address of phone

IPv4 and IPv6

IPv6 Only

IPv6 address of phone

IPv4 and IPv6

IPv4 and IPv6 Only

IPv4 or IPv6 address of phone 1

| Note | The pass-through codec should be configured on all dynamically inserted MTPs. To enable the use of the pass-through codec,
                                                   configure the MTP with both a standard codec and the pass-through codec. |
|---|---|

| Note | IPv6 is not supported. |
|---|---|

| Note | For these trunk calls, Unified CM does not insert an MTP to resolve a media addressing version mismatch between the two voice
                                                   devices. |
|---|---|

| Note | For trunk call signaling, Unified CM does not insert an MTP to resolve a media addressing version mismatch. |
|---|---|

| IP Addressing Mode of Phone | IP Addressing Mode of Trunk | Address Sent in SIP Offer by Unified CM |
|---|---|---|
| IPv4 Only | IPv4 Only | IPv4 address of phone |
| IPv4 Only | IPv4 and IPv6 | IPv4 address of phone |
| IPv6 Only | IPv6 Only | IPv6 address of phone |
| IPv6 Only | IPv4 and IPv6 | IPv6 address of phone |
| IPv4 Only | IPv6 Only | Insert an MTP and use its IPv6 address. |
| IPv6 Only | IPv4 Only | Insert an MTP and use its IPv4 address. |
| IPv4 and IPv6 | IPv4 Only | IPv4 address of phone |
| IPv4 and IPv6 | IPv6 Only | IPv6 address of phone |
| IPv4 and IPv6 | IPv4 and IPv6 Only | IPv4 or IPv6 address of phone 1 |