---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-ipv6-vtgs-b-ipv6-deployment-guide-for-cisco-vtgs-b-ipv6-deployment-3e37478842
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/IPv6/vtgs_b_ipv6-deployment-guide-for-cisco/vtgs_b_ipv6-deployment-guide-for-cisco_chapter_0101.html
retrieved_at: 2026-08-16T18:22:10.377872+00:00
---

IPv6 Deployment Guide

# IPv6 Deployment Guide

Updated: October 18, 2024

Chapter: Gateways

## Chapter: Gateways

- Gateways

- Gateways Overview

# Gateways

## Gateways Overview

Gateways provide a number of methods for connecting an IP telephony network to the public switched telephone network (PSTN),
                           legacy PBX systems, key systems, or analogue devices. Gateways range from specialized, entry-level and standalone voice gateways
                           to high-end, feature-rich integrated routers and Cisco Catalyst gateways. For general guidance on gateway selection and features,
                           refer to the Cisco Collaboration System Solution Reference Network Design (SRND), available at Link .

IPv4-only stack supported gateways with SIP protocol as shown in: Supported IPv6 Addressing Modes .

Software and hardware media termination points (MTPs) for conversion between IPv4 and IPv6 use SCCP IPv4 signaling to Unified
                                 CM.

All other gateway connections that use SCCP, H.323, and MGCP signaling protocols between Unified CM and the gateway have been
                                 deprecated.

You can combine ISDN gateways, Unified SRST analog port, and MTP functionality on a single Cisco Integrated Services Router
                                 (ISR) platform. Unified SRST and CUBE cannot co-exist in the same router.

Cisco 2800 and 3800 Series Integrated Services Routers and Cisco VG Series Gateways must be configured as IPv4-only stack
                                 gateway.