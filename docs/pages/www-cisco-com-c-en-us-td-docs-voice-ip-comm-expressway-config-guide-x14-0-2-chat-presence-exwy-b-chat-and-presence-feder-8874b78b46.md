---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-2-chat-presence-exwy-b-chat-and-presence-feder-8874b78b46
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0-2/chat_presence/exwy_b_chat-and-presence-federation-using-expressway-X1402/exwy_m_introduction.html
retrieved_at: 2026-08-16T15:23:39.467391+00:00
---

Chat and Presence Federation Using Expressway Deployment Guide (X14.0.2)

# Chat and Presence Federation Using Expressway Deployment Guide (X14.0.2)

Updated: July 23, 2021

Chapter: Introduction

## Chapter: Introduction

# Introduction

## Introduction

This Expressway guide also now applies to VCS. Any VCS-specific information is noted where necessary in the guide. (Older
                           VCS guides on Cisco.com are still valid for the VCS versions they apply to-as specified on the title page of each guide.)

The guide describes how to configure external XMPP federation from an on-premise IM and Presence Service server through Cisco
                           Expressway or through the IM and Presence Service. It also summarizes how to federate an IM and Presence Service deployment,
                           using SIP, with organizations that have Microsoft as their UC/collaboration solution. In the context of this guide, "federation" means to connect users in two or more organizations using collaboration technologies.

### Expressway or IM and Presence Service for XMPP Federation - How to Decide

The table outlines which features are supported by Expressway and IM and Presence Service respectively. It may help you to
                              decide which is the most suitable XMPP federation deployment option.

If you deploy external XMPP federation through Expressway, do not activate XMPP federation on IM and Presence Service. Or
                                          if you opt for XMPP federation through IM and Presence Service, do not activate XMPP federation on Expressway.

Feature

Expressway

IM and Presence Service

Email address translation

No

Yes

Multiple clusters

No (single cluster only)

Yes

Static routes

Yes

No

Internal federation

No

Yes

External federation terminated from DMZ

Yes

No

Dual federation (internal and external)

No

Yes (external federation not terminated from DMZ)

Managed file transfer and peer-to- peer file transfer

No

Yes

### Terminology

Do not use the domain names and other example values from this document in your test or production deployments. You must change
                                          the example values to represent your own environment.

Federation : Connecting users in two or more organizations using collaboration technologies.

Our organization : An organization using on-premises collaboration infrastructure to federate with other organizations.

Traversal server / client zones : Special zones on the Expressway-E and Expressway-C that enable the pair to traverse calls across firewalls. You can use
                                                Unified Communications zones instead.

Outbound and Inbound : Generally, calls initiated from inside our organization's network to another organization or remote user are Outbound. Calls
                                                initiated from outside our organization's network, to users or spaces in our network, are Inbound.

### Where to Find Information

For instructions about configuring XMPP federation on IM and Presence Service through Cisco Expressway, use this guide.

For instructions about configuring XMPP federation through the IM and Presence Service, use the Interdomain Federation for IM and Presence Service on Cisco Unified Communications Manager guide.

For information on "IM and Presence Service Configuration for SIP Open Federation" feature support, see " IM and Presence Service Configuration for SIP Open Federation " chapter of the Interdomain Federation Guide for the IM and Presence Service, Release 14 .

If you deploy IM and Presence Service federation with Microsoft-based organizations, Microsoft documentation on Skype for
                              Business PowerShell cmdlets is available here: https://docs.microsoft.com/en-us/

| Caution | If you deploy external XMPP federation through Expressway, do not activate XMPP federation on IM and Presence Service. Or
                                          if you opt for XMPP federation through IM and Presence Service, do not activate XMPP federation on Expressway. |
|---|---|

| Feature | Expressway | IM and Presence Service |
|---|---|---|
| Email address translation | No | Yes |
| Multiple clusters | No (single cluster only) | Yes |
| Static routes | Yes | No |
| Internal federation | No | Yes |
| External federation terminated from DMZ | Yes | No |
| Dual federation (internal and external) | No | Yes (external federation not terminated from DMZ) |
| Managed file transfer and peer-to- peer file transfer | No | Yes |

| Note | Do not use the domain names and other example values from this document in your test or production deployments. You must change
                                          the example values to represent your own environment. Federation : Connecting users in two or more organizations using collaboration technologies. Our organization : An organization using on-premises collaboration infrastructure to federate with other organizations. Traversal server / client zones : Special zones on the Expressway-E and Expressway-C that enable the pair to traverse calls across firewalls. You can use
                                                Unified Communications zones instead. Outbound and Inbound : Generally, calls initiated from inside our organization's network to another organization or remote user are Outbound. Calls
                                                initiated from outside our organization's network, to users or spaces in our network, are Inbound. |
|---|---|