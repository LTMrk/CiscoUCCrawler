---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x12-5-exwy-b-mra-expressway-deployment-guide-exwy-b--e402e50f88
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X12-5/exwy_b_mra-expressway-deployment-guide/exwy_b_mra-expressway-deployment-guide_chapter_01.html
retrieved_at: 2026-08-16T15:35:51.031983+00:00
---

Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.5)

# Mobile and Remote Access Through Cisco Expressway Deployment Guide (X12.5)

Updated: May 1, 2019

Chapter: Limitations and Unsupported Features

## Chapter: Limitations and Unsupported Features

# Limitations and Unsupported Features

## Supported and Unsupported Features with Mobile and Remote Access

Not all features are supported in every deployment scenario when using Mobile and Remote Access (MRA). This section provides
                              information about:

Key unsupported features for clients and endpoints. Lists client and endpoint features that are known not to work in certain
                                    MRA situations.

This is not an exhaustive list and for full details please refer to the documentation for the endpoint or client concerned.

Unsupported Expressway features that are known not to work in certain MRA situations.

### Unsupported Client and Endpoint Features

This section lists some key client and endpoint features which we know do not work with MRA-connected devices.

This item applies if you have multiple IM and Presence Service clusters configured on Cisco Expressway-C , and some of them run software earlier than version 11.5 n . In this case, because Cisco Expressway-C may select any cluster (round robin approach), it might select a cluster on an older software version. If so, IM and Presence Service features that require 11.5 are unavailable for endpoints connected over MRA.

In Expressway-E systems that use dual network interfaces, XCP connections (for IM&P XMPP traffic) always use the non-external
                                       (i.e. internal) interface. So XCP connections may fail in deployments where the Expressway-E internal interface is on a separate
                                       network segment and is used for system management purposes only, and where the traversal zone on the Expressway-C connects
                                       to the Expressway-E's external interface.

For supported Cisco Jabber clients connected over MRA, the E911NotificationURL feature requires a static HTML page for the notification to ensure that
                                       the web page renders correctly. Scripts and link tags are not supported.

Directory access mechanisms other than the Cisco User Data Service (UDS) are not supported for Cisco Jabber clients over MRA.

Some Cisco Unified Contact Center Express features are not supported over MRA. Please see the Unified Contact Center Express
                                       documentation for details.

Endpoint failover behavior:

Cisco Jabber clients support IM and Presence Service failover over MRA. However, they do not support any other type of MRA-related redundancy or failover—including SIP, voicemail,
                                             and User Data Services (UDS). Clients use single UDS server only.

This also applies on premises, and not just over MRA.

If an Expressway-C or Expressway-E node fails, active MRA calls through the failed Expressway node will be lost. This applies
                                             to all device types, including Jabber clients.

SIP registration failover is supported over MRA, for Cisco IP Phones and devices running TC or CE software. This includes
                                             failure of Cisco Expressway-C , Cisco Expressway-E , or a Cisco Unified Communications Manager ( Unified CM ) node. SIP registration failover is subject to a requirement that if an Expressway node fails, another active node must be
                                             available in the Expressway cluster.

To support Unified CM failover over MRA, Cisco IP Phones need clustered Expressway-C and Expressway-E servers. Devices running
                                             TC or CE software do not need clustered Expressway servers for this case. You need at least the same number of Expressway-C
                                             and Expressway-E servers in the cluster as the number of Unified CMs in the Call Manager group configured on the IP phone.

Cisco Jabber 12.5 or later is needed if you want chat/messaging services over MRA with authentication using OAuth refresh (self-describing
                                       tokens) and configure IM and Presence Service presence redundancy groups. With this release of Expressway, user login failures will occur in this scenario if Jabber versions
                                       before 12.5 are in use.

These limitations exist for recording over MRA connections:

Recording only works for direct person-to-person calls, not for conferences. This includes Built-in-Bridge (BiB) recording.

Recording is not currently supported for the Silent Monitoring and Whisper Coaching features.

In the case of call recording for Cisco Jabber endpoints, Jabber does not support injecting recording tones into the media streams. Also, be aware that Unified CM 12.5(1)SU1
                                             or later is needed to allow Jabber mobile devices to be CTI-monitored.

The Expressway does not encrypt the iX protocol on behalf of other entities. So iX must be encrypted end to end, with the
                                       endpoints and conferencing server doing the encryption, or it must be unencrypted end to end.

For iX to work over MRA, the conferencing server must be configured with an encrypted trunk to Unified CM and the endpoints/ Jabber must be running a suitable, iX-capable software version.

Certificate provisioning to remote endpoints is not supported over MRA. For example, the Certificate Authority Proxy Function
                                       (CAPF). If you can do the first-time configuration on premises (inside the firewall) including CAPF enrolment, then these
                                       endpoints can use encrypted TFTP configuration files over MRA. But you can't do the CAPF enrolment over MRA, so you must bring
                                       the endpoints back on-premises for subsequent certificate operations.

SIP UPDATE for session refresh support over MRA has some limitations. For example, the following features that rely on the
                                       SIP UPDATE method (RFC 3311) will fail:

Request to display the security icon on MRA endpoints for end-to-end secure calls.

Request to change the caller ID to display name or number on MRA endpoints.

Peer-to-peer file transfer when using IM and Presence Service and Jabber is not supported over MRA.

Managed File Transfer (MFT) over MRA is supported when using IM and Presence Service 10.5.2 and later and Jabber 10.6 and later clients. MFT over MRA is not supported when using an unrestricted version of IM and Presence Service .

File transfer with Webex Messenger Service and Cisco Jabber is supported.

Additional Mobility features including Session Handoff are not supported over MRA.

Hunt groups (including hunt pilots and hunt lists) are supported over MRA when using Unified CM version 11.5(1)SU5, or any later version that has the relevant change.

The Cisco Unified Communications Self Care Portal is not supported over MRA.

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

| Note | This also applies on premises, and not just over MRA. |
|---|---|

| Note | For iX to work over MRA, the conferencing server must be configured with an encrypted trunk to Unified CM and the endpoints/ Jabber must be running a suitable, iX-capable software version. |
|---|---|