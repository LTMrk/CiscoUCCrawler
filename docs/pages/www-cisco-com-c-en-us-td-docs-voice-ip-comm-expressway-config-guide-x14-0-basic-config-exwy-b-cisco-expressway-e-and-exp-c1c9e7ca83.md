---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-basic-config-exwy-b-cisco-expressway-e-and-exp-c1c9e7ca83
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/basic_config/exwy_b_cisco-expressway-e-and-expressway-c-basic-configuration-deployment-guide-x14-0/exwy_m_prerequisites.html
retrieved_at: 2026-08-16T15:27:28.141054+00:00
---

Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

# Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

Updated: April 14, 2021

Chapter: Prerequisites

## Chapter: Prerequisites

- Prerequisites

- Prerequisites

# Prerequisites

## Prerequisites

Before you begin any of the tasks in this guide, make sure that the following prerequisites are complete.

General prerequisites

We recommend that you use the Expressway web user interface to do the system configuration. This guide assumes that you are
                                 using a web browser running on a PC. The PC needs an Ethernet connection to a LAN which can route HTTP(S) traffic to the Expressway.

Review the relevant release notes on the Expressway Release Notes page.

Have the Expressway Administrator Guide on the Expressway Maintenance and Operation Guides page available for reference before you start.

IP address and password prerequisites

This guide also assumes that you have already configured a static IP address and changed the default passwords, as described
                           in the appropriate installation guide:

Cisco Expressway Virtual Machine Installation Guide on the Expressway Installation Guides page.

Cisco Expressway CExxxx Appliance Installation Guide on the Expressway Installation Guides page.

Expressway requires a static IP address. It doesn't use DHCP/SLAAC to get an IP address.

Do not use a shared address for the Expressway-E and the Expressway-C, as the firewall cannot distinguish between them. If
                           you use static NAT for IP addressing on the Expressway-E, make sure that any NAT operation on the Expressway-C does not resolve
                           to the same traffic IP address. We do not support shared NAT addresses between Expressway-E and Expressway-C.

DNS, NAT/firewall, and DHCP prerequisites

The following non-Expressway system configuration needs to be in place before you start:

Internal and external DNS records. See Appendix 2: DNS Records .

NAT & firewall configuration. See Appendix 3: Firewall and NAT Settings .

DHCP server configuration (not described in this document).

| Note | Expressway requires a static IP address. It doesn't use DHCP/SLAAC to get an IP address. |
|---|---|