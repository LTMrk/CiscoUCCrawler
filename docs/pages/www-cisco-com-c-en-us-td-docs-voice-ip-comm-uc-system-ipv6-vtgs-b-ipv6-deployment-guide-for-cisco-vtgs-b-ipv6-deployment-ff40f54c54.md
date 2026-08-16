---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-uc-system-ipv6-vtgs-b-ipv6-deployment-guide-for-cisco-vtgs-b-ipv6-deployment-ff40f54c54
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/IPv6/vtgs_b_ipv6-deployment-guide-for-cisco/vtgs_b_ipv6-deployment-guide-for-cisco_chapter_01011.html
retrieved_at: 2026-08-16T18:22:35.764121+00:00
---

IPv6 Deployment Guide

# IPv6 Deployment Guide

Updated: October 18, 2024

Chapter: IP Video Telephony

## Chapter: IP Video Telephony

- IP Video Telephony

- IP Video Telephony Overview

# IP Video Telephony

## IP Video Telephony Overview

IPv6 transition will follow Cisco Preferred Architecture deployment recommendations of IPv4. Cisco Unified Communications
                              Manager (Unified CM) is the call control server for the Cisco Preferred Architecture for Enterprise Collaboration deployment. Cisco IP Phones, Cisco Jabber clients, and Cisco TelePresence video endpoints use SIP to register directly to
                              Unified CM. The Unified CM cluster’s failover mechanism provides endpoint registration redundancy. If a WAN failure occurs
                              and endpoints at remote locations cannot register to Unified CM, they use SRST functionality for local and PSTN calls, but
                              some services such as voicemail and presence might not be available.