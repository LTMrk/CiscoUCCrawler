---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-ipv6-vtgs-b-ipv6-deployment-guide-for-cisco-vtgs-b-ipv6-deployment-cf91b517f5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/IPv6/vtgs_b_ipv6-deployment-guide-for-cisco/vtgs_b_ipv6-deployment-guide-for-cisco_chapter_01100.html
retrieved_at: 2026-08-16T18:22:39.901657+00:00
---

IPv6 Deployment Guide

# IPv6 Deployment Guide

Updated: October 18, 2024

Chapter: IP Telephony Migration Options

## Chapter: IP Telephony Migration Options

- IP Telephony Migration Options

- IP Telephony Migration Options Overview

# IP Telephony Migration Options

## IP Telephony Migration Options Overview

For first-time installations of IPv6 with Cisco Unified Communications Manager (Unified CM) or an upgrade to a traditional
                              deployment, we recommend the following guidelines:

### Deployment Models

For Cisco Unified CM IPv6 is supported for single-site deployments, multi-site deployments with distributed call processing,
                              and multi-site deployments with centralized call processing. Minimum IPv6 deployment requires the following products:

Dual-stack IPv6 Unified CM server

MTP for media interworking

IPv6-only IP Phones

All other components and interfaces can remain in IPv4. Unified CM will insert MTPs to provide media interworking for various
                              use cases.

### Campus Network and WAN

Before you enable IPv6 in the Unified CM cluster, make sure that both the campus network and the WAN support both IPv4 and
                              IPv6 traffic. Dual-stack (IPv4 and IPv6) routing is supported for Layer 3 campuses and WANs.

### Cluster-Wide IPv6 Configuration Settings

To maximize the amount of IPv6 traffic on your Unified Communications network, use the following settings for the cluster-wide
                              IPv6 Enterprise Parameters:

Enable IPv6 : True

IP Addressing Mode Preference for Media : IPv6

IP Addressing Mode Preference for Signaling : IPv6

### Common Device Configuration Profiles

Use multiple Common Device Configuration Profiles so that individual phones and trunks or groups of phones and SIP trunks
                              can be selectively configured to support IPv6.

The Common Device Configuration Profile in Unified CM Administration ( Device > Device Settings > Common Device Configuration ) contains the following IPv6 configuration information:

IP Addressing Mode

IP Addressing Mode Preference for Signaling

Allow Stateful Auto-Configuration for Phones

### DHCP

Stateless DHCP can be used with Stateless Address Auto-Configuration (SLAAC) for phones.

### MTPs

For multi-site distributed call processing deployments, you will most likely need to use Cisco IOS media termination points
                              (MTPs) for conversions between IPv4 and IPv6. These MTPs should be associated with both phone and SIP trunk media resource
                              groups (MRGs).

### IPv6 SIP Trunks

IPv6 SIP trunks should be configured as Delayed Offer without Alternative Network Address Types (ANAT) enabled. However, SIP
                              trunks configured for Early Offer (MTP Required) using an MTP resource for every call are do not support video calls or encrypted
                              calls.

### IP Phones

IPv6-only phone support is a major feature as it helps to mitigate IPv4 exhaustion. We recommend that you configure all IP
                              Phones as IPv6-only where applicable. All other IP Phones must be configured as IPv4.

### ISDN PSTN Gateway and SRST

To transition to an IPv6-only network and to reduce the MTP requirements, configure ISDN PSTN gateways and SRST with Delay
                              Offered SIP IPv6-only trunk.