---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-213864-configure-business-to-business-audio-and-htm-0fd846cc0d
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/213864-configure-business-to-business-audio-and.html
retrieved_at: 2026-08-16T15:41:58.869228+00:00
---

Configure Business to Business Audio/Video Calls through Expressway

# Configure Business to Business Audio/Video Calls through Expressway

### Download Options

Updated: March 6, 2024

Document ID: 213864

Contents

## Contents

## Introduction

This document describes how to integrate/configure Business to Business (B2B) deployment for audio/video calls through Expressway integrated with CUCM.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Expressway-C (Exp-C)

- Expressway-E (Exp-E)

- Cisco Unified Call Manager (CUCM)

- Cisco Unity Connection (CUC)

- Telepresence Video Communication Server-C (VCS-C)

- Jabber phone

- Cisco Telepresence System (CTS)

- EX phone

- Session Initiation Protocol (SIP)

- Hypertext Transfer Protocol (HTTP)

- eXtensible Messaging and Presence Protocol (XMPP)

- Cisco Unified IM and Presence (IM&P)

- Certificates

### Components Used

The information in this document is based on these software and hardware versions:

- Expressway C and E X8.1.1 or later

- Unified Communications Manager (CUCM) 10.0 or later

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

These steps explain in detail how to integrate/configure B2B deployment for audio and video calls through Expressway integrated with CUCM to be able to make and receive calls from other companies (domains).

Expressway with the Mobile Remote Access (MRA) feature provides seamless registration of Jabber and TC endpoints located outside the enterprise network as is shown in the network diagram.

The same architecture also provides seamless integration/calls between different enterprises (Business to Business integration), and this for Audio, Video, and IM&P (B2B).

This document does not cover the IM&P part and neither does it cover H.323 integration.

Prior to continuing, you need to ensure you have the relevant DNS Service (SRV) created for your domain. These records are used by other companies to find the location of your Expressway.

## Configure

### Network Diagram

This image provides an example of a network diagram

### Step 1. SIP Trunk Between CUCM and Expressway-C

After CUCM discovery is done by Expressway-C, Neighboring zone(s) are automatically configured for each node, and the transport protocol is discovered.

When the CUCM cluster is configured in mixed mode, there is one zone for Transmission Control Protocol (TCP) for non-secure traffic with destination port 5060 and 1 zone for TLS (Transport Layer Security) for secure traffic with destination port 5061. These ports cannot be changed.

The two zones are used for all edge calls to and from the edge endpoints.

Inbound calls from the edge endpoints take the route of these auto-added zones and hence target TCP 5060 or TLS 5061 on CUCM.

Through the established sockets, edge endpoints register and place/receive calls.

For B2B calls, configure a SIP trunk in CUCM that points to Expressway-C where typically CUCM listens on port 5060 or 5061 for inbound traffic from this gateway.

Since edge traffic comes from the same source IP with port 5060/5061, you need to use a different listening port for this trunk in CUCM. Otherwise, edge traffic is routed to the SIP trunk device in CUCM and not to the endpoint device (CSF or EX).

For Expressway-C side, use ports 5060 and 5061 for Session Initiation Protocol (SIP) TCP/TLS.

An example where CUCM listens on port 6060/6061 for inbound traffic on this trunk is shown in the image

These are the different configuration steps documented for this deployment. Both for secure and non-secure deployments.

#### a. Add a New SIP Trunk Security Profile

From the CUCM Administration page , navigate to Device > Trunk .

Configure a different Incoming port than 5060/5061, here use 6060 for TCP and 6061 for TLS Non Secure SIP Trunk Profile Secure SIP Trunk Profile

For TLS, you also need to configure the X.509 Subject name that matches the CN of the certificate presented by the Expressway-c. In addition, also upload the Expressway-C or the CA certificate (which issued the Expressway-C certificate) to the CUCM certificate trust store.

#### b. Configure the SIP Trunk on CUCM

Through this trunk, all B2B calls flow to and from CUCM.

The SIP trunk configuration parameters are standard for CUCM with VCS deployments.

Ensure you associate the security profile created in step 1.

#### c. Configure a Neighbor Zone on Expressway-C

A neighbor zone needs to be configured on Expressway-C to target CUCM.

This zone is used to route inbound B2B traffic to CUCM.

The configuration is standard except that you must ensure to configure the destination port that corresponds to the listening port configured on the SIP Trunk Security profile assigned to the SIP trunk on CUCM. In this example, the destination port used is 6060 for SIP/TCP and 6061 for SIP/TLS. Refer to step one as shown in the image.

From the Expressway Administration page, navigate to Configuration > Dial Plan > Transforms y Configuration .

Neighbor zone for SIP TCP: Neighbor zone for SIP TLS - with TLS verify mode on.

When TLS verify mode is set to on, you must ensure the peer address matches the CN or SAN from the certificate presented by CUCM. Typically, with TLS verify mode on, you configure the Fully Qualified Domain Name (FQDN) of the CUCM node for peer address.

From the Expressway Administration page, navigate to Configuration > Dial Plan > Transforms y Configuration . Neighbor zone for SIP TLS - with TLS verify mode off.

When TLS verify mode is set to off, the peer address can be either the IP address, hostname, or FQDN of the CUCM node.

From the Expressway Administration page, navigate to Configuration > Dial Plan > Transforms y Configuration .

#### d. Check Certificates

For TLS, ensure that:

- Expressway-C server certificate or CA root (used to sign certificate) is uploaded to the CUCMTrust store on all servers in the CUCM cluster.

- CallManager certificate or CA root (used to sign certificate) is uploaded to the Trusted CA Certificate list on the Expressway-C server.

### Step 2. Configure Traversal Zone Between Expressway-C and Expressway-E

A separate traversal zone has to be configured to route the B2B traffic between Expressway-C and Expressway-E.

This is a standard traversal zone configuration, but similar as with the SIP trunk on CUCM a different port then the port used by the UC Traversal zone for Edge traffic must be configured.

The standard port for the UC Traversal zone is 7001. For the B2B Traversal zone, you can e.g configure 7003.

UC Traversal Zone for edge traffic as shown in the image

Traversal Zone for B2B traffic as shown in the image

#### a. Traversal Zone Configuration for B2B traffic on Expressway-C

Expressway-C is the traversal zone client. In this example, the destination port is 7003.

With TLS verify mode set to On, ensure the Peer Address configured matches the CN or SAN of the presented certificate by Expressway-E

From the Expressway Administration page, navigate to Configuration > Dial Plan > Transforms y Configuration .

#### b. Traversal Zone Configuration for B2B Traffic on Expressway-E

Expressway-E is the traversal zone server, in this example, the listening port is 7003.

With TLS verify mode set to On, ensure the TLS verify subject name configured matches the CN or SAN of the presented certificate by Expressway-C

From the Expressway Administration page, navigate to Configuration > Dial Plan > Transforms y Configuration .

### Step 3. Configure DNS Zone on Expressway-E

To route the B2B traffic, configure a DNS zone on Expressway-E.

Expressway-E, for traffic destined to this zone, performs a DNS SRV lookup for ether _sip or _sips and this for the domain derived from the domain portion of the SIP URI.

The SRV target returned by the DNS server used to route the SIP call to.

The configuration is a standard DNS zone configuration.

From the Expressway Administration page, navigate to Configuration > Zones .

### Step 4. Configure Dialplan

#### a.Transforms and/or Search Rules on Expressway-C and E

From Expressway Administration page, navigate to Configuration > Dial Plan > Transforms y Configuration > Dial Plan > Transform or Search Rules .

For more information, consult the VCS Deployment guides (Control with Expressway), the chapter on Routing Configuration:

#### b. SIP Route Pattern(s) in CUCM

For more information,consult the CUCM System and Administration guide (Dialplan Deployment guide).

#### c. For SIP Call Routing, SRV records must be Created on the Public DNS Servers

As shown in the image, it lists the required SRV records, as well as H323 B2B calls which have not been discussed in this document. Also, note that SIP UDP by default is disabled on Expressway.

#### d. Configure the Cluster Fully Qualified Domain Name in CUCM.

You can enter multiple entries separated by a comma.

#### e. Create a Transform on Expressway-C which Removes the Port from the URI Received in the Invite from CUCM

For more info, refer to Calls from CUCM to DNS Zone on VCS Expressway Sent to Wrong IP Address

From Expressway Administration page, navigate to Configuration > Dial Plan > Transforms y Configuration > Dial Plan > Transform .

The SRND also contains an extensive chapter on dialplan.

### Step 5. Upload Rich Media Licenses to Expressway

Rich media licenses (Traversal Zone licenses) must be uploaded to each Expressway Server.

In case these are missed, or due to improper configuration calls are released with this error message:  "Call license limit reached: You have reached your license limit of  concurrent traversal call licenses"

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

For further B2B troubleshoot information, refer to Troubleshoot Most Common Issues for Business to Business Calls Through Expressway

## Related Information

- Cisco TelePresence Video Communication Server (VCS)

- Technical Support & Documentation - Cisco Systems

### Revision History

2.0

06-Mar-2024

Updated Title, Introduction, SEO, Alt Text, Machine Translation and Formatting.

1.0

05-Oct-2021

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 06-Mar-2024 | Updated Title, Introduction, SEO, Alt Text, Machine Translation and Formatting. |
| 1.0 | 05-Oct-2021 | Initial Release |