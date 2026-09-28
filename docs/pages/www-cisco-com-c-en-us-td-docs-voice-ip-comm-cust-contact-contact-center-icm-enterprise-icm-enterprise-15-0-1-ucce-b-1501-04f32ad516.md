---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-ucce-b-1501-04f32ad516
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/ucce_b_1501_features-guide/rcct_m_150_fg_vpn-less-access-to-finesse-desktop.html
retrieved_at: 2026-08-16T20:10:00.825999+00:00
---

Cisco Unified Contact Center Enterprise Features Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Features Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: VPN-less Access to Finesse Desktop

## Chapter: VPN-less Access to Finesse Desktop

- VPN-less Access to Finesse Desktop

- Overview

# VPN-less Access to Finesse Desktop

## Overview

VPN-less Access to Finesse Desktop is a deployment model that allows users to access the Finesse desktop and its features
                           directly from the internet without using a VPN. To enable this capability, you can use the Cisco-provided Reverse Proxy Automated
                           Installer, which includes a built-in reverse proxy based on the OpenResty® Nginx proxy.

This VPN-less access supports all standard functions on the desktop, including Real Time and Historical Reports, as well as
                           SSO authentication. It also includes the mechanism to tunnel ADFS access through the same proxy to facilitate SSO authentications.

In reverse proxy deployments, media access remains unchanged. Agents and supervisors can connect to the media using Cisco
                           Jabber over the Mobile and Remote Access (MRA) solution or the Mobile Agent feature of Cisco Contact Center Enterprise with
                           a PSTN or mobile endpoint.

For more details on how to configure the VPN-less Access to Finesse Desktop feature, refer to the Cisco Contact Center Enterprise Reverse Proxy Installation and Upgrade Guide .