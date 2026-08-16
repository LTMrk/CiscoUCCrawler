---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x12-6-exwy-b-mra-expressway-deployment-guide-exwy-b--763a391db1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X12-6/exwy_b_mra-expressway-deployment-guide/exwy_b_mra-expressway-deployment-guide_chapter_00.html
retrieved_at: 2026-08-16T15:34:38.890750+00:00
---

Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.6)

# Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.6)

Updated: June 3, 2020

Chapter: Mobile and Remote Access Overview

## Chapter: Mobile and Remote Access Overview

# Mobile and Remote Access Overview

## About Mobile and Remote Access

Cisco Unified Communications Mobile and Remote Access (MRA) is part of the Cisco Collaboration Edge Architecture. MRA allows
                           endpoints such as Cisco Jabber to have their registration, call control, provisioning, messaging and presence services provided by Cisco Unified Communications Manager ( Unified CM ) when the endpoint is outside the enterprise network. The Expressway provides secure firewall traversal and line-side support
                           for Unified CM registrations.

The MRA solution provides the following functions:

Off-premises access : a consistent experience outside the network for Jabber and EX/MX/SX Series clients

Security : secure business-to-business communications

Cloud services : enterprise grade flexibility and scalable solutions providing rich Cisco Webex integration and service provider offerings

Gateway and interoperability services : media and signaling normalization, and support for nonstandard endpoints

Third-party SIP or H.323 devices can register to the Expressway-C and, if necessary, interoperate with Unified CM -registered devices over a SIP trunk.

Unified CM provides call control for both mobile and on-premises endpoints. Signaling traverses the Expressway solution between the
                           mobile endpoint and Unified CM . Media traverses the Expressway solution, which relays the media between the endpoints directly. All media is encrypted between
                           the Expressway-C and the mobile endpoint.

### Core Components

Any MRA solution requires Expressway and Unified CM, with MRA-compatible soft clients and/or fixed endpoints. The solution
                                 can optionally include the IM and Presence Service and Unity Connection. This guide assumes that you have already set up the
                                 following:

A basic Expressway-C and Expressway-E configuration, as specified in the Expressway Basic Configuration (Expressway-C with Expressway-E) Deployment Guide (The document describes the networking options for deploying Expressway-E in the DMZ.)

Unified CM and IM and Presence Service are configured as specified in the configuration and management guides for your version, at Cisco Unified Communications Manager Configuration Guides .

If used, IM and Presence Service and/or Unity Connection are similarly configured as specified in the relevant Cisco Unified Communications Manager Configuration Guides .

### Mobile and Remote Access Ports

For MRA port information, go to the Cisco Expressway IP Port Usage Configuration Guide at Cisco Expressway Series Configuration Guides . The guide describes the ports that you can use between Expressway-C in the internal network, Expressway-E in the DMZ, and
                                 the public internet.

### Protocol Summary

The following table lists the protocols and associated services used in the Unified Communications solution.

Protocol

Security

Services

SIP

TLS

Session establishment – Register, Invite etc.

HTTPS

TLS

Logon, provisioning, configuration, directory, Visual Voicemail

Media

SRTP

Media - audio, video, content sharing

XMPP

TLS

Instant Messaging, Presence, Federation

### Jabber Client Connectivity Without VPN

The MRA solution supports a hybrid on-premises and cloud-based service model, providing a consistent experience inside and
                                 outside the enterprise. MRA provides a secure connection for Jabber application traffic and other devices with the required capabilities to communicate without having to connect to the corporate
                                 network over a VPN. It is a device and operating system agnostic solution for Cisco Jabber clients on Windows, Mac, iOS and Android platforms.

MRA allows Jabber clients that are outside the enterprise to do the following:

Use Instant Messaging and Presence services

Make voice and video calls

Search the corporate directory

Share content

Launch a web conference

Access visual voicemail

Cisco Jabber Video for TelePresence ( Jabber Video ) does not work with MRA.

## Capacity Information

For details on MRA registration limits and other capacity information, refer to "Cluster License Usage and Capacity Guidelines" in Cisco Expressway Cluster Creation and Maintenance Deployment Guide . You can find this guide on the Expressway configuration guides page.

| Note | Third-party SIP or H.323 devices can register to the Expressway-C and, if necessary, interoperate with Unified CM -registered devices over a SIP trunk. |
|---|---|

| Protocol | Security | Services |
|---|---|---|
| SIP | TLS | Session establishment – Register, Invite etc. |
| HTTPS | TLS | Logon, provisioning, configuration, directory, Visual Voicemail |
| Media | SRTP | Media - audio, video, content sharing |
| XMPP | TLS | Instant Messaging, Presence, Federation |

| Note | Cisco Jabber Video for TelePresence ( Jabber Video ) does not work with MRA. |
|---|---|