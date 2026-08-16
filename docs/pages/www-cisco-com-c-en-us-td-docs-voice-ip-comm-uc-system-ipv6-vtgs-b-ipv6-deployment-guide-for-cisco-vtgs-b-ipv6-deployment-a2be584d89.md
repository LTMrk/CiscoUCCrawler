---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-ipv6-vtgs-b-ipv6-deployment-guide-for-cisco-vtgs-b-ipv6-deployment-a2be584d89
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/IPv6/vtgs_b_ipv6-deployment-guide-for-cisco/vtgs_b_ipv6-deployment-guide-for-cisco_chapter_01010.html
retrieved_at: 2026-08-16T18:22:31.372743+00:00
---

IPv6 Deployment Guide

# IPv6 Deployment Guide

Updated: October 18, 2024

Chapter: Applications

## Chapter: Applications

- Applications

- Applications Overview

# Applications

## Applications Overview

All Cisco applications that can terminate voice media support IPv4-only. For these applications, if a call is extended from
                              an IPv6-only device to the IPv4-only application, Cisco Unified Communications Manager (Unified CM) inserts a media termination
                              point (MTP) to convert the voice media from IPv6 to IPv4, as shown in the following figure.

### Voicemail

Cisco Unity Connection supports IPv6 for all interfaces, and Cisco Unity Express supports IPv4 only.

### LDAP Directory Integration

Unified CM supports IPv4 with Lightweight Directory Access Protocol (LDAP) for directory sync. IP Phones 8800/7800 exercise
                              UDS (http). IP Phones use CCMPD and CCMCIP services for Personal and Corporate Directory. These services are IPv6 compliant.
                              Back-end interfaces from Unified CM to AD are not validated for IPv6, and should be IPv4-only.

### Native Unified CM Applications

Cluster-wide Extension Mobility, IP Phones Services, Cisco Unified Communications Manager Assistant, Cisco Unified Communications
                              Attendant Console, MRA, and Web Dialer support IPv4-only.

### Video Conferencing

Cisco Meeting Server and Cisco TelePresence Management Suite (TMS) for video conference support is in a traditional IPv4 stack.
                              IPv4 or IPv6 endpoints are supported in a cluster. Any IPv6-only endpoint can join Cisco Meeting Server video conference service.
                              Additional MTP is required in Unified CM to provide media inter-working IPv4 to IPv6.

### Multistream Video

Multistream video that allows an IPv4 or IPv6 endpoint to send multiple resolution video streams is supported. The bridge
                              passes the most appropriate streams to the far-end video units that can be IPv4 or IPv6 stack. The far end video unit receives
                              a full resolution stream of the active speakers.

### Device Mobility

Device Mobility is supported only for IPv4-only, IPv6-only, and dual-stack devices.

### Unified CM IM and Presence Service

Cisco Unified Communications Manager IM and Presence Service (IM and Presence Service), Cisco IM and Presence Service Client,
                              and Cisco IP Phone Messenger support dual-stack or IPv6-only.

### Cisco Mobility Applications

Mobility applications support IPv6-only.

### Cisco Jabber Applications

Cisco Jabber applications support IPv6-only for desktop on-premise application deployments only. For MRA, Jabber should be
                              configured for dual-stack (with IPv4 preferred) because of the IPv6-only support limitation in Cisco Expressway. In this dual-stack,
                              ANAT as media is not applicable; it is for applications server interface only based on RFC 6555 . Jabber applications in Android and iOS 3G/4G mobile networks will support IPv6 because of a NAT64 solution developed by
                              mobile network service providers. In an off-premise deployment, we recommend Jabber dual-stack due to users roaming in various
                              service provider networks.

### Cisco Unified Survivable Remote Site Telephony

Cisco Unified Survivable Remote Site Telephony (Unified SRST) functions as a dual-stack application server that supports the
                              following devices, which have IP phone line side feature such as: Hold/Resume, Forwarding, 3WC, Transfer, MOH, ATA Fax in
                              IPv4 mode:

Unified SRST supports the following Cisco IP Phones for voice only services in IPv6-only addressing mode using SIP signaling
                                    based on the Routers:

Support for Cisco IP Phone 7811, 7821, 7841 and 7861

Support for Cisco IP Phones 8811, 8841, 8845, 8851, 8861, and 8865

Not supported endpoints: Jabber and SCCP IP Phones

Unified SRST will not support SCCP signaling and SIP SDP ANAT dual-stack attributes to support media selection that can be
                                    IPv4 or IPv6.

All the legacy dual-stack phones default to IPv4-only SIP mode in Unified CM.

PSTN gateways are configurable to SIP IPv4-only or IPv6-only. This gateway supports incoming, outgoing, and emergency calls
                                          to service provider PSTN.

Media Inter-working: Unified SRST provides IPv4 to IPv6 RTP media inter-working for voice and video endpoints. This media
                                    inter-working is required when using IPv6-only endpoints, or when gateways are configured to IPv4-only mode.

For more information, refer to the Cisco Unified SCCP and SIP SRST System Administrator Guide .