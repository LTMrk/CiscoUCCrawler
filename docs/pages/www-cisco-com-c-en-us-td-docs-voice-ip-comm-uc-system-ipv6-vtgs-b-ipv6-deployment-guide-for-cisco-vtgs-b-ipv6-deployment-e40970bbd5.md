---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-ipv6-vtgs-b-ipv6-deployment-guide-for-cisco-vtgs-b-ipv6-deployment-e40970bbd5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/IPv6/vtgs_b_ipv6-deployment-guide-for-cisco/vtgs_b_ipv6-deployment-guide-for-cisco_chapter_0111.html
retrieved_at: 2026-08-16T18:22:18.690306+00:00
---

IPv6 Deployment Guide

# IPv6 Deployment Guide

Updated: October 18, 2024

Chapter: Media Resources and Music on Hold

## Chapter: Media Resources and Music on Hold

# Media Resources and Music on Hold

## Media Resources and Music on Hold Overview

A media resource is a software-based or hardware-based entity that performs media processing functions on the data streams
                           to which it is connected. Media processing functions include mixing multiple streams to create one output stream (conferencing),
                           passing the stream from one connection to another (media termination point), converting the data stream from one compression
                           type to another (transcoding), echo cancellation, signaling, termination of a voice stream from a TDM circuit (coding and
                           decoding), packetization of a stream, streaming audio (Annunciator and Music on Hold), and so forth.

This chapter focuses on new media termination point (MTP) functionality introduced to support IPv6 Collaboration deployments:
                           namely, the capability of Cisco IOS MTPs to convert a voice media stream from IPv4 to IPv6 and conversely. Other media resources
                           such as conferencing and transcoding are also discussed in context with this new MTP functionality. For all other media resource
                           and Music on Hold (MoH) design guidance, refer to the Cisco Collaboration System Solution Reference Network Design (SRND),
                           available at Link .

## Media Termination Point (MTP)

The following Cisco Integrated Services Router (ISR) MTPs support media conversion between IPv4 and IPv6 for devices with
                              mismatched media IP address versions:

Cisco IOS hardware MTPs—Digital signal processors (DSPs) on the Cisco ISR Motherboard and NM-HDV2 with PVDM2 DSPs

Cisco IOS software MTPs

Cisco IOS Release IOS XE Everest 16.6.1 and above supports these MTPs.

### Address Conversion Between IPv4 and IPv6

When a mismatch exists between the IP addressing versions supported by two devices, Unified CM dynamically inserts an MTP
                              resource to convert the voice media stream from IPv4 to IPv6 and conversely. Dynamically inserted MTPs support the pass-through
                              codec, which allows the MTP to support not only voice calls but also video calls and encrypted calls. The pass-through codec
                              should be configured on all dynamically inserted MTPs. To enable the use of the pass-through codec, configure the MTP with
                              both a standard codec and the pass-through codec.

Unified CM trunks can also be configured with a statically assigned MTP ( MTP Required check box checked). The trunk's statically defined MTP does not support the pass-through codec and supports only a single
                              configured codec (G.711 or G.729), which limits all calls that use this trunk to either G.711 or G.729 voice calls and T.38
                              Fax calls only. This statically assigned MTP also has the capability to convert the voice media stream from IPv4 to IPv6 and
                              conversely.

To be dynamically or statically inserted into a call path, the Cisco IOS MTPs must be associated with the media resource group
                              (MRG) for each device (phone or trunk).

The following Cisco IOS configuration is an example of a software MTP. The sccp local GigabitEthernet0/0 command associates the IPv4 and IPv6 addresses on this interface with the MTP for both SCCP signaling and media addresses.

```
interface GigabitEthernet0/0
ip address 192.168.1.5 255.255.255.0
! MTP's IPv4 address
ipv6 address 2001:0db8:101:1:1::5/64
! MTP's IPv6 address
!
sccp local GigabitEthernet0/0
sccp ccm 192.168.0.15 identifier 1 version 7.0
! Unified CM's IPv4 address
sccp ccm 2001: 0db8:101:1::15 identifier 2 version 7.0
! Unified CM's IPv6 address
sccp
!
sccp ccm group 1
associate ccm 1 priority 1
associate ccm 2 priority 2
associate profile 1 register MTP-1
!
dspfarm profile 1 mtp
codec g711ulaw
codec pass-through
maximum sessions software 100
associate application SCCP
!
```

The following figure shows when an MTP is inserted between two devices to convert from IPv4 to IPv6, and conversely. However,
                              both devices can have MTP resources available in their media resource groups, and Unified CM must decide which MTP to use.
                              Unified CM uses the cluster-wide setting of IP Addressing Mode Preference for Media to determine which MTP to use for conversions
                              between IPv4 and IPv6.

If the cluster-wide IP Addressing Mode Preference for Media is set to IPv6, Unified CM chooses the MTP associated with the
                              IPv4 device.

Conversely, if the cluster-wide IP Addressing Mode Preference for Media is set to IPv4, Unified CM chooses the MTP associated
                              with the IPv6 device.

By choosing the device whose addressing mode does not match the cluster-wide IP Addressing Mode Preference for Media, Unified
                              CM selects the cluster-wide media preference value that matches the longest call leg between the two devices in the cluster.

If the preferred device's MTP is not available, the other device's MTP is used as a last resort. If no MTPs are available,
                                          the call fails.

Transcoder DSP resources can also be used as hardware MTPs. If both transcoding resources and software MTPs exist in the same
                              media resource group, Unified CM uses these media resources in a round-robin fashion for conversions between IPv4 and IPv6.
                              To prioritize transcoding DSP resources for transcoding purposes only, place the software MTP and hardware MTPs in a separate
                              media resource group (MRG) and give this MRG precedence (a higher order) over the transcoder MRG in the media resource group
                              list (MRGL).

The number of MTPs required is based on the traffic that requires media header addressing conversation from IPv4 to IPv6.
                              In the worst case, the number of MTPs required is the same as the number of IPv6-only devices that are in service. The MTPs
                              should be located in a site where IPv4-only phones are deployed. For IPv6-only sites, the MTPs should be located where servers
                              are deployed, for example, in a data center. MTPs should be located where IPv4 and IPv6 addresses are available. Quicker transition
                              to IPv6- only devices is supported to phase out MTPs from a network.

## IPv6 and Other Media Resources

The following media resources do not support IPv6 for voice. If these resources are invoked, an MTP resource is required to
                              convert the voice stream between IPv6 and IPv4, as shown in the following figure.

Video conferencing

Video Transcoding

IPv6 Music on Hold (MoH)

Voice conferencing resources and hardware MTP resources can reside on the same DSP. Similarly, voice transcoding resources
                              and hardware MTP resources can reside on the same DSP.

IPv6-only devices do not support multicast music on hold.

### Cisco IOS RSVP Agent and IPv6

The Cisco IOS Resource Reservation Protocol (RSVP) agent does not support IPv6, and RSVPv4 cannot be used within the cluster
                              for call admission control. For SIP trunks and intercluster trunks, locations-based call admission control must be used.

### IPv4 to IPv6 Conversion When Multiple MTPs Exist Within a Media Resource Group (MRG)

Unified CM server-based MTPs do not support the pass-through codec. If Cisco IOS MTPs (which support the pass-through codec)
                              and Unified CM MTPs (which do not support the pass-through codec) are listed in the same media resource group, Unified CM
                              requests an MTP with pass-through codec support for conversions between IPv4 and IPv6.

If an MTP is statically assigned to the SIP trunk (Early Offer), then conversions between IPv4 an dIPv6 can occur only for
                              the codec specified on the MTP (G.711 or G.729).

| Note | If the preferred device's MTP is not available, the other device's MTP is used as a last resort. If no MTPs are available,
                                          the call fails. |
|---|---|