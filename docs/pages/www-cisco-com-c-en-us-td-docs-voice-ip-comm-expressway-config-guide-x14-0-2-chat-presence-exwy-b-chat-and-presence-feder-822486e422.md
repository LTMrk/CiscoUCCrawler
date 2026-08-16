---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-2-chat-presence-exwy-b-chat-and-presence-feder-822486e422
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0-2/chat_presence/exwy_b_chat-and-presence-federation-using-expressway-X1402/exwy_m_xmpp-federation-through-im-and.html
retrieved_at: 2026-08-16T15:23:47.733198+00:00
---

Chat and Presence Federation Using Expressway Deployment Guide (X14.0.2)

# Chat and Presence Federation Using Expressway Deployment Guide (X14.0.2)

Updated: July 23, 2021

Chapter: XMPP Federation through IM and Presence Service

## Chapter: XMPP Federation through IM and Presence Service

# XMPP Federation through IM and Presence Service

## XMPP Federation through IM and Presence Service

This federation enables IM and Presence Service users in one enterprise domain to exchange presence information and Instant
                           Messaging (IM) with users in external domains. This scenario does not involve Expressway.

This section only provides summary information. For configuration information and other details about deploying XMPP federation
                                       managed by IM and Presence Service, see Interdomain Federation on IM and Presence Service for Cisco Unified Communications Manager .

### Supported Systems XMPP through IM and P

IM and Presence Service, Release 9.1.1 or later, supports XMPP federation with the following enterprises:

Cisco WebEx Messenger Release 7.x.

Cisco Unified Presence Release 8.x.

IM and Presence Service Release 9.x or later.

Any other XMPP-standards compliant server.

### Configuration Basics

IM and Presence Service does not support XMPP federation between an IM and Presence Service Release 9.x enterprise and a Cisco
                              Unified Presence Release 7.x enterprise.

If you want to enable XMPP federation with an external domain, ensure that the external domain was not previously configured
                              as a SIP federated domain on Cisco Unified Presence. An example of how to do this follows:

Example : A Cisco Unified Presence deployment with ciscoexample.com was historically configured as a SIP-based federation. But ciscoexample.com
                              has now added XMPP support, so the local administrator now wants to enable an XMPP-based federation. To allow this, the administrator
                              first deletes ciscoexample.com as a SIP-federated domain on Cisco Unified Presence.

When IM and Presence Service is federating with Cisco WebEx Enterprise, it's not possible for WebEx Connect client users to
                              invite IM and Presence Service users to temporary or persistent chat rooms. This is due to a design constraint on the WebEx
                              Connect client.

To allow the IM and Presence Service to federate over XMPP, you must enable and configure XMPP federation on IM and Presence
                              Service.

If you have multiple IM and Presence Service clusters, you must enable and configure XMPP federation on at least one node
                              per cluster. The XMPP federation configuration must be identical across clusters. The Diagnostics Troubleshooter compares the XMPP federation configuration across clusters, and reports if the XMPP federation configuration is not identical
                              across clusters.

If you deploy Cisco Adaptive Security Appliance for firewall purposes, see the following topics in Interdomain Federation on IM and Presence Service for Cisco Unified Communications Manager :

Topics related to integration preparation, for considerations on routing, scale, public IP addresses, and the Certification
                                    Authority.

Task to configure the Cisco Adaptive Security Appliance, for information on configuring prerequisite information such as hostname,
                                    timezone, clock, and so on.

### Task Flow Summary to Deploy XMPP Federation Through IM and Presence Service

Task

Configure IM and Presence Service for XMPP federation

Configure Security for XMPP federation

(Optional) Configure the email for federation feature

Turn on XMPP federation service

Configure the Cisco Adaptive Security Appliance for XMPP federation

Troubleshooting XMPP federation through IM and Presence Service

| Important | This section only provides summary information. For configuration information and other details about deploying XMPP federation
                                       managed by IM and Presence Service, see Interdomain Federation on IM and Presence Service for Cisco Unified Communications Manager . |
|---|---|

| Task |
|---|
| Configure IM and Presence Service for XMPP federation |
| Configure Security for XMPP federation |
| (Optional) Configure the email for federation feature |
| Turn on XMPP federation service |
| Configure the Cisco Adaptive Security Appliance for XMPP federation |
| Troubleshooting XMPP federation through IM and Presence Service |