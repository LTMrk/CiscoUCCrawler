---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-ipv6-vtgs-b-ipv6-deployment-guide-for-cisco-vtgs-b-ipv6-deployment-2d4c3964d6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/IPv6/vtgs_b_ipv6-deployment-guide-for-cisco/vtgs_b_ipv6-deployment-guide-for-cisco_chapter_01111.html
retrieved_at: 2026-08-16T18:22:52.144543+00:00
---

IPv6 Deployment Guide

# IPv6 Deployment Guide

Updated: October 18, 2024

Chapter: Appendix

## Chapter: Appendix

# Appendix

## Product Configuration Resources for IPv6

To configure products for IPv6, refer to the product configuration guides.

Endpoint (SIP)

IPv6 Configuration Resources

Cisco IP Phone 7800 Series

Administration Guides

Cisco IP Phone 8800 Series

Administration Guides

Cisco Jabber

On-Premises Deployment Guide

Cisco DX70 and DX80 (CE endpoints)

Support

Cisco TelePresence MX Series (CE endpoints)

Support

Cisco TelePresence SX Series (CE endpoints)

Support

Cisco TelePresence EX Series (CE endpoints)

Support

Gateway

IPv6 Configuration Resources

Cisco Integrated Services Routers (ISR)

Configuration Guides

Cisco 2900 and 3900 Series Integrated Services Routers (ISR) (For CUBE)

CUBE Configuration Guide

Application or Interface

IPv6 Configuration Resources

Cisco Unified Communications Manager (Unified CM)

System Configuration Guide

Unified CM IM and Presence Service (IM and Presence Service)

Configuration and Administration Guide

Cisco Unified Survivable Remote Site Telephony (Unified SRST)

Administration Guides

Solution Design Guide

Cisco Unified Contact Center Express (Unified CCX)

Solution Design Guide

Cisco Emergency Responder

Administration Guide

Cisco Unity Connection

System Administration Guide

Integration Guide

Cisco Meeting Server

Support

Cisco TelePresence Management Suite

Support

Cisco Prime Collaboration

Support

## Document Direction

We recommend deploying IPv6-only device configuration where applicable, typically endpoints and PSTN gateways. All applications
                              servers need IPv4 address and IPv6 address (dual-stack) to support all traditional IPv4 devices until all devices are IPv6-only
                              capable including third-party products and applications.

To reduce dependency on IPv4 addresses, you can upgrade the following on-premise deployment modes to IPv6: single-site call
                              processing deployments; multi-site distributed call-processing deployments; and multi-site deployments with centralized call
                              processing. We recommend that you upgrade and configure:

IPv6-only stack SIP phones, SIP gateways, and SIP trunks.

IPv4-only stack and IPv6-only stack (dual-stack) Unified CM clusters and other application servers.

All third-party products and applications in IPv4-only.

## Deprecation of ANAT SIP SDP Attributes

Department of Defense (DoD) certification requirements drove the development of Alternative Network Address Types (ANAT) RFC
                              4091 and 4092. ANAT allows a set of network addresses to establish a media stream is useful in environments with both IPv4-only
                              hosts and IPv6-only hosts. For this functionality, all the devices need IPv4 address and IPv6 address assignment. ANAT was
                              also implemented in Cisco Unified Communication System Release 7.1.2. However, since all device need both IPv4 and IPv6 addresses,
                              ANAT does not help to reduce dependency on the now depleted number of IPv4 addresses. Based on large enterprise customer feedback,
                              and their need for new IP addresses, ANAT SIP SDP attributes have since been deprecated by Internet Engineering Task Force
                              (IETF).

We recommend deploying IPv6-only device configuration where applicable (typically endpoints). All servers, third-party products,
                              and applications need IPv4 addresses and IPv6 addresses to support all traditional IPv4 devices until all devices are IPv6-only
                              capable.

| Endpoint (SIP) | IPv6 Configuration Resources |
|---|---|
| Cisco IP Phone 7800 Series | Administration Guides |
| Cisco IP Phone 8800 Series | Administration Guides |
| Cisco Jabber | On-Premises Deployment Guide |
| Cisco DX70 and DX80 (CE endpoints) | Support |
| Cisco TelePresence MX Series (CE endpoints) | Support |
| Cisco TelePresence SX Series (CE endpoints) | Support |
| Cisco TelePresence EX Series (CE endpoints) | Support |

| Gateway | IPv6 Configuration Resources |
|---|---|
| Cisco Integrated Services Routers (ISR) | Configuration Guides |
| Cisco 2900 and 3900 Series Integrated Services Routers (ISR) (For CUBE) | CUBE Configuration Guide |

| Application or Interface | IPv6 Configuration Resources |
|---|---|
| Cisco Unified Communications Manager (Unified CM) | System Configuration Guide |
| Unified CM IM and Presence Service (IM and Presence Service) | Configuration and Administration Guide |
| Cisco Unified Survivable Remote Site Telephony (Unified SRST) | Administration Guides |
| Cisco Unified Contact Center Enterprise (Unified CCE) | Solution Design Guide |
| Cisco Unified Contact Center Express (Unified CCX) | Solution Design Guide |
| Cisco Emergency Responder | Administration Guide |
| Cisco Unity Connection | System Administration Guide Integration Guide |
| Cisco Meeting Server | Support |
| Cisco TelePresence Management Suite | Support |
| Cisco Prime Collaboration | Support |