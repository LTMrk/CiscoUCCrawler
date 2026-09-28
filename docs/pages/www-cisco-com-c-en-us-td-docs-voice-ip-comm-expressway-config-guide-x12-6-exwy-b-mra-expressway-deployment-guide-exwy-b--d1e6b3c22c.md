---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x12-6-exwy-b-mra-expressway-deployment-guide-exwy-b--d1e6b3c22c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X12-6/exwy_b_mra-expressway-deployment-guide/exwy_b_mra-expressway-deployment-guide_chapter_01.html
retrieved_at: 2026-08-16T15:34:47.226311+00:00
---

Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.6)

# Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.6)

Updated: June 3, 2020

Chapter: Limitations and Unsupported Features

## Chapter: Limitations and Unsupported Features

# Limitations and Unsupported Features

## Supported and Unsupported Features with Mobile and Remote Access

MRA supports different features in different deployment scenarios, and when different clients and endpoints are used. This
                              section provides information about:

Key unsupported features for clients and endpoints

Unsupported Expressway features that don't work in certain MRA situations

### Unsupported Client and Endpoint Features

This section lists some key client and endpoint features that we know don't work with MRA-connected devices.

If you have multiple IM and Presence Service clusters configured on Cisco Expressway-C , and some of them run pre-11.5 software, MRA endpoints may not be able to use features that require 11.5. The reason is that,
                                       using a round robin approach, Cisco Expressway-C may select a cluster on an older software version.

In Expressway-E systems that use dual network interfaces, XCP connections (for IM and Presence Service XMPP traffic) always
                                       use the internal interface. XCP connections may fail if the Expressway-E internal interface is on a separate network segment
                                       and is used for system management only, and where the Expressway-C traversal zone connects to the Expressway-E external interface.

If you deploy Cisco Jabber clients over MRA with the E911NotificationURL feature, configure a static HTML page for the notification. MRA does not support
                                       scripts and link tags for the web page.

MRA supports Cisco Jabber directory access using the Cisco User Data Services (UDS). MRA doesn't support other directory access methods for Jabber.

MRA doesn't support some Cisco Unified Contact Center Express features. For details, refer to the Unified Contact Center Express
                                       documentation.

Endpoint failover behavior:

Cisco Jabber clients support IM and Presence Service failover over MRA. However, they don't support any other type of MRA-related redundancy or failover—including SIP, voicemail,
                                             and User Data Services (UDS). Clients use a single UDS server only.

If an Expressway-C or Expressway-E node fails, active MRA calls through the failed Expressway node also fail. This behavior
                                             applies to all device types, including Jabber clients.

MRA supports SIP registration failover for Cisco IP Phones and devices running TC or CE software. This support includes failure
                                             of Cisco Expressway-C , Cisco Expressway-E , or a Cisco Unified Communications Manager ( Unified CM ) node. Note that if an Expressway node fails, another active Expressway node must be available in the cluster.

For Unified CM failover over MRA, Cisco IP Phones need clustered Expressway-C and Expressway-E servers. IP Phones need at
                                             least the same number of Expressway-C and Expressway-E servers in the cluster as the number of Unified CMs in the Call Manager
                                             group configured on the IP phone. Note that devices running TC or CE software don't need clustered Expressway servers for
                                             Unified CM failover.

Cisco Jabber 12.5 or later is needed if you want chat/messaging services over MRA with OAuth Refresh Authentication (self-describing tokens)
                                       and with IM and Presence Service presence redundancy groups. With pre-12.5 Jabber, user login fails in this scenario.

MRA call recording includes the following limitations:

Recording works for direct person-to-person calls only—call recording doesn't work for conferences.

This limitation includes Built-in-Bridge (BiB) recording.

As of X12.6.1, MRA supports call recording with Silent Monitoring. For earlier releases, call recording is not supported with
                                             Silent Monitoring.

MRA doesn't support call recording with the Whisper Coaching feature.

MRA doesn't support recording tones for Cisco Jabber clients. Also note that CTI monitoring of Jabber mobile devices requires Unified CM 12.5(1)SU1 or later.

The Expressway doesn't encrypt the iX protocol on behalf of other entities. As a result, iX must be encrypted end to end,
                                       or unencrypted end to end. When iX is encrypted, the endpoints and conferencing server must handle encryption.

For iX to work over MRA, configure the conferencing server with an encrypted trunk to Unified CM and make sure that the endpoints/ Jabber are running a suitable, iX-capable software version.

MRA doesn't support certificate provisioning for remote endpoints. This limitation includes the Certificate Authority Proxy
                                       Function (CAPF). To use CAPF, complete the first-time configuration, including CAPF enrollment, on premises (inside the firewall).
                                       To complete subsequent certificate operations, you must bring the endpoints back on-premises.

MRA supports encrypted TFTP configuration files over MRA when the CAPF enrollment has already been completed on-premises.

The following session refresh features that rely on the SIP UPDATE method (RFC 3311) fail over MRA:

Request to display the security icon on MRA endpoints for end-to-end secure calls

Request to change the caller ID to display name or number on MRA endpoints

MRA doesn't support peer-to-peer file transfer when using IM and Presence Service and Jabber .

MRA supports Managed File Transfer (MFT) over MRA when using IM and Presence Service 10.5.2 and later (restricted version) and Jabber 10.6 and later clients. MRA doesn't support MFT with an unrestricted version of IM and Presence Service .

MRA supports file transfer with Webex Messenger Service and Cisco Jabber .

MRA doesn't support additional Mobility features, including Session Handoff.

MRA supports hunt groups (including hunt pilots and hunt lists) when using Unified CM version 11.5(1)SU5, or any later version that has the relevant change.

MRA doesn't support the Cisco Unified Communications Self Care Portal.

Key Expansion Module (KEM) Support for Compatible Phones—We have not officially tested and verified support over MRA for the
                                       KEM accessory for Cisco IP Phone 8800 Series devices. However, we have observed under lab conditions that KEMs with multiple
                                       DNs work satisfactorily over MRA.

This feature is available as a preview feature, but is not officially supported. To deploy the feature, SIP path headers must
                                       be enabled on Expressway, and you need a Unified CM software version that supports path headers (Release 11.5(1)SU4 or later
                                       is recommended).

### Unsupported Expressway Features and Limitations

Currently, if one Expressway node in a clustered deployment fails or loses network connectivity for any reason (including
                                       if the Unified CM restarts or fails), all active calls going through the affected node will fail. The calls are not handed
                                       over to another cluster peer. Bug ID CSCtr39974 refers. This is not an MRA-specific issue and applies to all call types.

We don’t support third-party network load balancers between MRA clients and Expressway-E.

The Expressway cannot be used for Jabber Guest when it's used for Mobile and Remote Access (MRA).

The Expressway-C used for MRA cannot also be used for Microsoft gateway service. Microsoft gateway service requires a dedicated
                                       Expressway-C.

Maintenance mode is not supported over MRA for endpoints running CE software. The Expressway drops MRA calls from these endpoints
                                       when you enable maintenance mode.

As Expressway only supports IPv4 mode for MRA connections, the IP configuration settings "IPv6 only" or "Both" are not supported.
                                       In the case of "Both", as Expressway does not proxy IPv6 MRA traffic from clients, intermittent issues may arise if clients
                                       send IPv6 instead of IPv4.

Endpoint management capability (SNMP, SSH/HTTP access) is not supported.

Multidomain and multicustomer support is limited as follows:

Before X8.5, each Expressway deployment supported only one IM&P domain. (Even though IM and Presence Service 10.0 and later supports Multiple Presence Domains.)

As of X8.5, you can create multiple deployments on the Expressway-C, but this feature is still limited to one domain per deployment.

As of X8.5.1, a deployment can have Multiple Presence Domains. However, this feature is in preview status only, and we currently
                                             recommend that you do not exceed 50 domains.

Deployments on Large VM servers are limited to 2500 proxied registrations to Unified CM.

The Expressway does not support some Cisco Unified Contact Center Express features for contact center agents or other users
                                       who connect over MRA. Jabber for Mac and Jabber for Windows cannot provide deskphone control over MRA, because the Expressway pair does not traverse the CTI-QBE protocol.

However, if these Jabber applications, or other CTI applications, can connect to Unified CM CTIManager (directly or through the VPN) they can provide deskphone control of MRA-connected clients.

For ICE passthrough calls, if Host and Server-reflexive addresses cannot negotiate successfully, endpoints can utilize relay
                                       address of the TURN server to establish optimized media path. However, when Expressway is used as a TURN server and if static
                                       NAT is configured on the Expressway-E, the media cannot be passed using the relay address (CDETS CSCvf85709 refers). In this
                                       case, default traversal path is used to traverse the media. That is, the media passes through Expressway-C and Expressway-E.

The Expressway-E does not support TURN relay over TCP for ICE passthrough calls.

### Partial Support for Cisco Jabber SDK

You can use the following supported Cisco Jabber SDK features over MRA:

Sign in, sign out

Register phone services

Make or receive audio/video calls

Hold and resume, mute/unmute, and call transfer

For more information, see the Getting Started Guide for Cisco Jabber SDK .

| Note | Refer to your endpoint or client documentation for more information. The following list isn't exhaustive. |
|---|---|

| Note | For iX to work over MRA, configure the conferencing server with an encrypted trunk to Unified CM and make sure that the endpoints/ Jabber are running a suitable, iX-capable software version. |
|---|---|