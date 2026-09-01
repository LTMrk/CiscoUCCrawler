---
doc_id: help-webex-com-en-us-article-wbx000028782-c9b4168b12
source_url: https://help.webex.com/en-us/article/WBX000028782
retrieved_at: 2026-09-01T21:39:24.117819+00:00
---

Network Requirements for Webex Services

*The revision history is located at the end of the document. Please subscribe to be notified of changes. This article is intended for network administrators, particularly firewall and proxy security administrators, who want to use the Webex Suite of cloud collaboration services within their organization. The primary focus of this document is on the network requirements of Webex Meetings and Webex Messaging, and the document also provides links to documents that describe the network requirements for Webex Calling. This article will help you configure network access to the Webex suite of services used by: Cloud registered Webex app clients for Meetings, Messaging, and Calling Cloud registered Webex Meetings Centre app clients Cloud registered Cisco Video devices, Cisco IP Phones, Cisco video devices, and third-party devices that use SIP to connect to the Webex Suite services. This document primarily focuses on the network requirements of Webex cloud registered products that use HTTPS signaling to communicate with Webex Suite services but also separately describes the network requirements for products that use SIP signaling to the Webex cloud. These differences are summarized below:

Summary of device types and protocols supported by Webex

#### Summary of device types and protocols supported by Webex

All cloud registered Webex apps and devices use HTTPS to communicate with Webex messaging and meetings services:

- The Webex app uses HTTPS signaling for Webex messaging and meeting services. The Webex app can also use the SIP protocol to join Webex meetings, but this is subject to the user either being called via their SIP address or choosing to dial a SIP URL to join a meeting (rather than use the meeting functionality native to the Webex app).

- Cloud registered Cisco Video devices use HTTPS signaling for all Webex services, including requests to activation.webex.com which sets the system time.

- On-premises SIP registered Webex devices can also use HTTPS signaling if the Webex Edge for devices feature is enabled. This feature allows Webex devices to be administered via Webex Control Hub and to participate in Webex Meetings using HTTPS signaling (for details, see https://help.webex.com/en-us/cy2l2z/Webex-Edge-for-Devices).

Transport protocols and encryption ciphers for cloud registered Webex apps and devices

#### Transport protocols and encryption ciphers for cloud registered Webex apps and devices

All cloud registered Webex apps and Cisco Video devices initiate outbound connections only. Cisco’s Webex Cloud never initiates outbound connections to cloud registered Webex apps and Cisco Video devices, but can make outbound calls to SIP devices. Webex services for meetings and messaging are hosted in globally distributed data centers that are either Cisco owned (e.g. Webex data centers for identity services, meeting services, and media servers) or hosted in a Cisco Virtual Private Cloud (VPC) on the Amazon AWS platform (e.g. Webex messaging micro-services, messaging storage services). Webex services also reside in Microsoft Azure data centers for Video Interop with Microsoft Teams (VIMT).

Types of Traffic:

Webex app and Cisco Video devices establish signaling and media connections to the Webex cloud. Signaling traffic Webex app and Cisco Video devices use HTTP as HTTP over TLS (HTTPS) and Secure Web Sockets (WSS) over TLS for REST based signaling to the Webex cloud. Signaling connections are outbound only and use URLs for session establishment to Webex services. TLS signaling connections to Webex services use TLS version 1.2 or 1.3. The cipher selection is based on the Webex server TLS preference. Using either TLS 1.2 or 1.3, Webex prefers ciphers suites using:

- ECDHE for key negotiation

- RSA-based certificates (3072-bit key size)

- SHA2 authentication (SHA384 or SHA256)

- Strong encryption ciphers using 128 or 256 bits (for example, AES_256_GCM)

Webex supports cipher suites in the following preference order for TLS version 1.2 connections*: TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 Note - CBC mode encryption is supported for older browsers without more secure GCM mode encryption. Webex supports cipher suites in the following preference order for TLS version 1.3 connections*: TLS_AES_256_GCM_SHA384 TLS_CHACHA_POLY1305_SHA256 TLS_AES_128_GCM_SHA256 Note – With TLS 1.3, ECDHE key negotiation and RSA-based certificates are a mandatory part of the specification and this detail is therefore omitted in the cipher suite description. *The cipher suites and cipher suite preference order may vary for some Webex services Establishing signaling connections to Webex services using URLs If you have deployed proxies, or firewalls to filter traffic leaving your enterprise network, the list of destination URLs that need to be allowed to access the Webex service can be found in the section " Domains and URLs that need to be accessed for Webex Services ". Webex strongly recommends that you do not alter or delete HTTP header values as they pass through your proxy/ firewall unless permitted in these guidelines https://www.w3.org/TR/ct-guidelines/#sec-altering-header-values . Modification or deleting of HTTP headers outside of these guidelines can impact access to Webex Services, including loss of access to Webex services by Webex apps and Cisco Video devices. Filtering Webex signaling traffic by IP address is not supported as the IP addresses used by Webex are dynamic and may change at any time. Media traffic The Webex app and Cisco Video devices encrypt real-time media for audio, video, and content sharing streams using the following encryption ciphers:

- AES-256-GCM cipher

- AES-CM-128-HMAC-SHA1-80 cipher

Webex traffic through Proxies and Firewalls

Most customers deploy an internet firewall, or internet proxy and firewall, to restrict and control the HTTP based traffic that leaves and enters their network. Follow the firewall and proxy guidance below to enable access to Webex services from your network. If you are using a firewall only, note that filtering Webex signaling traffic using IP addresses is not supported, as the IP addresses used by Webex signaling services are dynamic and may change at any time. If your firewall supports URL filtering, configure the firewall to allow the Webex destination URLs listed in the section " Domains and URLs that need to be accessed for Webex Services".

Webex Services – Port Numbers and Protocols

#### Webex Services – Port Numbers and Protocols

The following table describes ports and protocols that need to be opened on your firewall to allows cloud registered Webex apps and Cisco Video devices to communicate with Webex cloud signaling and media services. The Webex apps, devices, and services covered in this table include: The Webex app, Cisco Video devices, Video Mesh Node, Hybrid Data Security node, Directory Connector, Calendar Connector, Management Connector, Serviceability Connector. For guidance on ports and protocols for devices and Webex services using SIP can be found in the section "Network requirements for SIP based Webex services" .

Destination Port

Protocol

Description

Devices using this rule

- If you are using NTP and DNS services within your enterprise network, then ports 53 and 123 do not need to be opened through your firewall.

MTU size for Webex IPv4 and IPv6 Traffic

#### MTU size for Webex IPv4 and IPv6 Traffic

Webex supports both IPv4 and IPv6 for signaling and media services. For most customers, supporting Webex over IPv4 and IPv6 should not present any issues. Still, issues can arise if your network's Maximum Transmissible Unit (MTU) is set to non-default values. The Maximum Transmissible Unit (MTU) is the maximum size of the IP packet that can be transmitted over a network link without fragmentation. The IPv6 RFC mandates a minimum MTU size of 1280 bytes. Most routing and switching devices support a default maximum MTU size of 1500 bytes on all interfaces. IPv6 adds additional overhead to IP packets, which increases packet size compared to IPv4 traffic. The IPv6 RFC mandates a minimum MTU size of 1280 bytes. Webex recommends keeping the default maximum transmission unit (MTU) size of 1500 bytes for all IP packets received and sent on your network. If you need to reduce the MTU size in your network, Webex recommends reducing this to no less than 1300 bytes.

IP subnets for Webex media services

#### IP subnets for Webex media services

The majority of Webex media services are hosted in Cisco data centers. Cisco also supports Webex media services in Microsoft Azure data centers for Video Integration with Microsoft Teams (VIMT). Microsoft has reserved its IP subnets for Cisco's sole use, and media services located in these subnets are secured within Microsoft Azure virtual network instances. For guidance on VIMT deployment, see https://help.webex.com/en-us/article/nffx8kj/Deploy-the-Webex-video-integration-for-Microsoft-Teams . Configure your firewall to allow access to these destinations, Webex IP subnets, and transport protocol ports for media streams from Webex apps and devices. Webex apps and Cisco Video devices support UDP, TCP, and TLS as media transport protocols. If UDP ports are blocked by your firewall, Webex apps and Cisco Video devices will fall back to TCP. If TCP ports are blocked, Webex apps and Cisco Video devices will fall back to TLS. UDP is Cisco’s preferred transport protocol for media, and we strongly recommend using only UDP to transport media. Webex apps and Cisco Video devices also support TCP and TLS as transport protocols for media, but these are not recommended in production environments as the connection-orientated nature of these protocols can seriously affect media quality over lossy networks. Note: The IP subnets listed below are for Webex media services. Filtering Webex signaling traffic by IP address is not supported as the IP addresses used by Webex are dynamic and may change at any time. HTTP signaling traffic to Webex services can be filtered by URL/domain in your Enterprise Proxy server before being forwarded to your firewall.

IPv4 Subnets for Media Services

IPv6 Address Ranges for Media Services

* Azure data centers – used to host Video Integration for Microsoft Teams (aka Microsoft Cloud Video Interop) services Webex apps and Cisco Video Devices perform tests to detect the reachability of, and round-trip time to, a subset of nodes in each media cluster available to your organization. Media node reachability is tested over UDP, TCP, and TLS transport protocols and occurs on start-up, a network change, and periodically while the app or device is running. The results of these tests are stored and sent to the Webex cloud prior to joining a meeting or a call. The Webex cloud uses these reachability test results to assign the Webex app/ Webex device the best media server for the call based on transport protocol (UDP preferred), round trip time, and media server resource availability. Cisco does not support or recommend filtering a subset of IP addresses based on a particular geographic region or cloud service provider. Filtering by region can cause serious degradation to the meeting experience, up to and including the inability to join meetings entirely. If you have configured your firewall to allow traffic to only a subset of the IP subnets above, you may still see reachability test traffic traversing your network, in an attempt to reach media nodes in these blocked IP subnets. Media nodes on IP subnets that are blocked by your firewall will not be used by Webex apps and Cisco Video devices.

Webex signaling traffic and Enterprise Proxy Configuration

Most organizations use proxy servers to inspect and control the HTTP traffic that leaves their network. Proxies can be used to perform several security functions such as allowing or blocking access to specific URLs, user authentication, IP address/domain/hostname/URI reputation lookup, and traffic decryption and inspection. Proxy servers are also commonly used as the only path that can forward HTTP-based internet destined traffic to the enterprise firewall, allowing the firewall to limit outbound internet traffic to that originating from the Proxy server(s) only. Your Proxy server must be configured to allow Webex signaling traffic to access the domains/ URLs listed in the section below: Webex strongly recommends that you do not alter or delete HTTP header values as they pass through your proxy/ firewall unless permitted in these guidelines https://www.w3.org/TR/ct-guidelines/#sec-altering-header-values . Modification or deleting of HTTP headers outside of these guidelines can impact access to Webex Services, including loss of access to Webex services by Webex apps and Cisco Video devices.

Domains and URLs that need to be accessed for Webex Services

#### Domains and URLs that need to be accessed for Webex Services

Cisco Webex Services URLs

Domain / URL

Description

Webex Apps and devices using these domains / URLs

For example : Webex Meetings services Messaging services File management service Key management service Software upgrade service Profile picture service Whiteboarding service Proximity service Presence service Registration service Calendaring service Search service Identity services Authentication OAuth services Device onboarding Cloud Connected UC

Additional Webex related services - Cisco Owned domains

URL

Description

Webex Apps and devices using these domains / URLs

Additional Webex Related Services – Third Party Domains

URL

Description

Webex Apps and devices using these domains / URLs

*.walkme.com s3.walkmeusercontent.com

(1) Webex uses third parties for diagnostic and troubleshooting data collection; and the collection of crash and usage metrics. Data that may be sent to these third party sites is described in the Webex Privacy datasheets. For details, see:

- https://trustportal.cisco.com/c/dam/r/ctp/docs/privacydatasheet/collaboration/cisco-webex-meetings-privacy-data-sheet.pdf

- https://trustportal.cisco.com/c/r/ctp/trust-portal.html?doctype=Privacy%20Data%20Sheet|Privacy%20Data%20Map&search_keyword=webex#/1552559092865176

*.cloudfront.net

*.akamaiedge.net *.akamaitechnologies.com

*.akamai.net

*.fastly.net

Additional URLs for Webex Hybrid Services

#### Additional URLs for Webex Hybrid Services

Cisco Webex Hybrid services URLs

URL

Description

Used by:

(1) We plan to phase out the use of *.docker.com and *.docker.io for Hybrid Services Containers, eventually replacing them with subdomains in *.amazonaws.com. Note: If you use a Cisco Web Security Appliance (WSA) Proxy and want to automatically update the URLs used by Webex services, please refer to the WSA Webex Services configuration document for guidance on how to deploy a Webex External Feed-in AsyncOS for Cisco Web Security. For a CSV file containing the list of Webex Services URIs, see: Webex Services CSV File

Proxy Features

#### Proxy Features

Proxy Authentication Support

Proxies can be used as access control devices, blocking access to external resources until the user/device provides valid access permission credentials to the proxy. Several authentication methods are supported by Proxies, such as Basic Authentication, Digest Authentication (Windows-based) NTLM, Kerberos, and Negotiate (Kerberos with NTLM fallback). For the “No Authentication” case in the table below, the device can be configured with a Proxy address but does not support authentication. When Proxy Authentication is being used, valid credentials must be configured and stored in the OS of Webex App or Cisco Video Device. For Cisco Video devices and the Webex App, Proxy addresses can be configured manually via the platform OS, or device UI, or automatically discovered using mechanisms such as: Web Proxy Auto Discovery (WPAD) and/or Proxy Auto Config (PAC) files:

- https://www.cisco.com/c/en/us/td/docs/security/web_security/connector/connector3000/WPADAP.html

- https://www.cisco.com/c/en/us/td/docs/security/web_security/connector/connector2972/PACAP.html

Product

Authentication Type

Proxy Configuration

(1): Mac NTLM Auth - Machine need not be logged onto the domain, user prompted for a password (2): Windows NTLM Auth - Supported only if a machine is logged onto the domain Guidance on Proxy settings for Windows OS Microsoft Windows supports two network libraries for HTTP traffic (WinINet and WinHTTP) that allow Proxy configuration. WinInet was designed for single-user, desktop client applications only; WinHTTP was designed primarily for multi-user, server-based applications. WinINet is a superset of WinHTTP; when selecting between the two, you should use WinINet for your Proxy configuration settings. For more info, see https://docs.microsoft.com/en-us/windows/win32/wininet/wininet-vs-winhttp

Proxy Inspection and Certificate Pinning

The Webex app and Cisco Video devices validate the certificates of the servers they establish TLS sessions with. Certificate checks such as, the certificate issuer and digital signature, rely upon verifying the chain of certificates up to the root certificate. To perform these validation checks, the app or device uses a set of trusted root CA certificates installed in the operating system trust store. If you have deployed a TLS-inspecting Proxy to intercept, decrypt, and inspect Webex traffic, ensure that the certificate the Proxy presents (in lieu of the Webex service certificate) has been signed by a certificate authority whose root certificate is installed in the trust store of your Webex App or Webex device. For the Webex App, the CA certificate used to sign the certificate used by the Proxy needs to be installed into the operating system of the device. For Cisco Video devices, open a service request with TAC to install this CA certificate into the RoomOS software. The table below shows the Webex app and Webex device support for TLS inspection by Proxy servers:

Product

Supports Custom Trusted CAs for TLS inspection

Note - The Webex app does not support Proxy server decryption and inspection of TLS sessions for Webex Meetings media services. If you wish to inspect traffic sent to services in the webex.com domain, you must create a TLS inspection exemption for traffic sent to *mcs*.webex.com, *cb*.webex.com and *mcc*.webex.com.

Note - The Webex app does not support SNI extension for TLS based media connections. Connection failure to the Webex audio and video services will occur if a proxy server requires the presence of SNI.

802.1X – Port based Network Access control

#### 802.1X – Port based Network Access control

Product

Supports 802.1X

Notes

Network requirements for SIP based Webex services

#### Network requirements for SIP based Webex services

The Webex cloud supports inbound and outbound calls using SIP as the call control protocol for Webex Meetings and for direct (1:1) calls from/to cloud registered Webex apps and Cisco Video devices. SIP calls for Webex Meetings Webex Meetings allows participants with SIP apps and devices to join a meeting by either:

- Calling the SIP URI for the meeting (e.g. meetingnumber@webex.com), or

- The Webex cloud calling the participant’s specified SIP URI (e.g. my-device@customer.com )

Calls between SIP apps/devices and cloud registered the Webex app/Cisco Video devices The Webex cloud allows users of SIP apps and devices to:

- Be called by cloud registered Webex apps and Cisco Video devices

- Call cloud registered Webex apps and Cisco Video devices

In both of the above cases, SIP apps and devices need to establish a session to/from the Webex cloud. The SIP app or device will be registered to a SIP based call control application (such as Unified CM), which typically has a SIP Trunk connection to Expressway C and E that allows inbound and outbound calls (over the internet) to the Webex Cloud. SIP apps and devices may be:

- Cisco Video device using SIP to register to Unified CM

- Cisco IP Phones using SIP to register to Unified CM, or the Webex Calling service

- A third party SIP app or device using a third party SIP call control application

Note * If a router or SIP firewall is SIP Aware, meaning it has SIP Application Layer Gateway (ALG) or something similar enabled, we recommend that you turn off this functionality to maintain the correct operation of service. See the relevant manufacturer’s documentation for information about how to disable SIP ALG on specific devices

The following table describes the ports and protocols required for access to Webex SIP services:

The SIP connection between Expressway E and the Webex cloud supports unencrypted signaling using TCP, and encrypted signaling using TLS, or MTLS. Encrypted SIP signaling is preferred as the certificates exchanged between the Webex cloud and Expressway E can be validated before proceeding with the connection. Expressway is commonly used to enable SIP calls to the Webex cloud and B2B SIP calls to other organizations. Configure your firewall to allow:

- All outbound SIP signaling traffic from Expressway E nodes

- All inbound SIP signaling traffic to your Expressway E nodes

If you wish to limit inbound and outbound SIP signaling and related media traffic to and from the Webex cloud. Configure your firewall to allow SIP signaling and medial traffic to access the IP subnets for Webex media services (refer to the section "IP subnets for Webex media services") and the following AWS regions: us-east-1, us-east-2, eu-central-1, us-gov-west-2, us-west-2. The IP address ranges for these AWS regions can be found here: https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html * This webpage is not instantaneously updated, as AWS makes regular changes to the IP address ranges in their subnets. To dynamically track AWS IP address range changes, Amazon recommends subscribing to the following notification service: https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html#subscribe-notifications Media for SIP based Webex services uses the same destination IP subnets for Webex Media (listed here)

Network Requirements for Webex Edge Audio

#### Network Requirements for Webex Edge Audio

A summary of other Webex Hybrid Services and documentation

#### A summary of other Webex Hybrid Services and documentation

Cisco Webex Video Mesh

Cisco Webex Video Mesh provides a local media service in your network. Instead of all media going to Webex Cloud, it can remain on your network, for reduced Internet bandwidth usage and increased media quality. For details, see the Cisco Webex Video Mesh Deployment Guide .

Hybrid Calendar Service

The Hybrid Calendar service connects Microsoft Exchange, Office 365 or Google Calendar to Webex, making it easier to schedule and join meetings, especially when mobile. For details, see: Deployment Guide for Webex Hybrid Calendar Service

Hybrid Directory Service

Cisco Directory Connector is an on-premises application for identity synchronization into the Webex cloud. It offers a simple administrative process that automatically and securely extends enterprise directory contacts to the cloud and keeps them in sync for accuracy and consistency. For details, see: Deployment Guide for Cisco Directory Connector

Preferred Architecture for Webex Hybrid Services

The Preferred Architecture for Cisco Webex Hybrid Services describes the overall hybrid architecture, its components, and general design best practices. See: Preferred Architecture for Webex Hybrid Services

Webex Calling - Network Requirements

#### Webex Calling - Network Requirements

If you are also deploying Webex Calling with Webex Meetings and Messaging services, the network requirements for the Webex Calling service can be found here: https://help.webex.com/b2exve/Port-Reference-Information-for-Cisco-Webex-Calling

Webex Events - Network Requirements

#### Webex Events - Network Requirements

If you are also deploying Webex Events with Webex Meetings and Messaging services, the network requirements for the Webex Events service can be found here: https://help.socio.events/en/articles/4796797-what-domains-emails-should-be-allowlisted-by-my-attendees-network-admins

Webex Services for FedRAMP customers

#### Webex Services for FedRAMP customers

For customers who require the list of IP address ranges and ports for Webex FedRAMP services This information can be found here : https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/cloudCollaboration/WebexforGovernment/FedRAMP_Meetings_Ports_IP_Ranges_Quick_Reference.pdf

Document Revision History - Network Requirements for Webex Services

#### Document Revision History - Network Requirements for Webex Services

Revision Date

New and Changed Information

In the IPv4 Subnets for Media Services section, updated the incorrect IP address range from 163.129.0.0/16 to 163.129.0.0/17.

Corrected previous change (2/18) to reflect correct wording - 'Cloud registered Cisco Video devices use HTTPS signaling for all Webex services, including requests to activation.webex.com which sets the system time.'

Added note on cloud registered devices using the URL 'activation.webex.com' to get NTP to the 'Summary of device types and protocols supported by Webex' section.

Added 'WxC Voicemail to mail notifications' to description for *.sparkpostmail entry in to the 'Additional Webex Related Services - Third Party Domains' section.

Removed Webex Android App from *.amplitude.com list in the Cisco Webex Service URLs table.

Added *livestreaming.webex.com to new Webex Webcast entry in the Cisco Webex Service URLs table under the third-party domain section.

Added ajax.aspnetcdn.com to Webex Scheduler URLs in the Cisco Webex Service URLs table under the third-party domain section.

Updated broken link for Google Firebase Cloud Messaging (FCM) service. Added *.akamaitechnologies.com to CDN list (used by Webex RoomOS Endpoints)

Removed the row (starting with speech.googleapis.com and texttospeech.googleapis.com ). All traffic related to the service now goes exclusively to domains under the already documented *. webex.com and *. wbx2.com domains.

- Updated linked .CSV file for Webex Teams to show revised links shown above

| Webex Services - Port Numbers and Protocols |
|---|
| Destination Port | Protocol | Description | Devices using this rule |
| 443 | TLS | Webex HTTPS signaling. Session establishment to Webex services is based on defined URLs, rather than IP addresses. If you are using a proxy server, or your firewall supports DNS resolution; refer to the section "Domains and URLs that need to be accessed for Webex Services" to allow signaling access to Webex services. | All |
| 123 (1) | UDP | Network Time Protocol (NTP) | All |
| 53 (1) | UDP TCP | Domain Name System (DNS) Used for DNS lookups to discover the IP addresses of services in the Webex cloud. Most DNS queries are made over UDP; however, DNS queries may use TCP as well. | All |
| 5004 and 9000 | SRTP over UDP | Encrypted audio, video, and content sharing on the Webex App and Cisco Video devices For a list of destination IP subnets refer to the section "IP subnets for Webex media services" . | Webex App Cisco Video Devices Video Mesh Nodes |
| 50,000 – 53,000 | SRTP over UDP | Encrypted audio, video, and content sharing – Video Mesh Node only | Video Mesh Node |
| 5004 | SRTP over TCP | TCP also serves as a fallback transport protocol for encrypted audio, video and content sharing if UDP cannot be used. For a list of destination IP subnets refer to the section "IP subnets for Webex media services" . | Webex App Cisco Video Devices Video Mesh Nodes |
| 443 | SRTP over TLS | Used as a fallback transport protocol for encrypted audio, video and content sharing if UDP and TCP cannot be used. Media over TLS is not recommended in production environments For a list of destination IP subnets refer to the section "IP subnets for Webex media services" . | Webex App Cisco Video Devices |

| IPv4 Subnets for Media Services |
|---|
| 4.152.214.0/24* | 66.163.32.0/19 |
| 4.158.208.0/24* | 69.26.160.0/19 |
| 4.175.120.0/24* | 114.29.192.0/19 |
| 4.152.180.0/24* | 144.196.0.0/16 |
| 20.50.235.0/24* | 150.253.128.0/17 |
| 20.53.87.0/24* | 163.129.0.0/17 |
| 20.57.87.0/24* | 170.72.0.0/16 |
| 20.68.154.0/24* | 170.133.128.0/18 |
| 20.76.127.0/24* | 173.39.224.0/19 |
| 20.108.99.0/24* | 173.243.0.0/20 |
| 20.120.238.0/23* | 207.182.160.0/19 |
| 23.89.0.0/16 | 209.197.192.0/19 |
| 40.119.234.0/24* | 210.4.192.0/20 |
| 44.234.52.192/26 | 216.151.128.0/19 |
| 52.232.210.0/24* | 4.144.190.0/24* |
| 62.109.192.0/18 |  |
| 64.68.96.0/19 |  |

| IPv6 Address Ranges for Media Services |
|---|
| 2402:2500::/34 |
| 2607:fcf0::/34 |
| 2a00:a640::/34 |

| Cisco Webex Services URLs |
|---|
| Domain / URL | Description | Webex Apps and devices using these domains / URLs |
| *.webex.com *.cisco.com *.wbx2.com *.ciscospark.com *.webexapis.com | Webex micro-services. For example : Webex Meetings services Messaging services File management service Key management service Software upgrade service Profile picture service Whiteboarding service Proximity service Presence service Registration service Calendaring service Search service Identity services Authentication OAuth services Device onboarding Cloud Connected UC | All |
| *.webexcontent.com (1) | Webex storage for user-generated content and logs, including: Shared files, Transcoded files, Images, Screenshots, Whiteboard content, Client & device logs, Profile pictures, Branding logos, images Log files Bulk CSV export files & import files (Control Hub) | All |
| Additional Webex related services - Cisco Owned domains |
| URL | Description | Webex Apps and devices using these domains / URLs |
| *.accompany.com | People Insights Integration | Webex Apps |
| Additional Webex Related Services – Third Party Domains |
| URL | Description | Webex Apps and devices using these domains / URLs |
| *.sparkpostmail1.com *.sparkpostmail.com | Email service for newsletters, registration info, announcements, WxC Voicemail to mail notifications | All |
| *.giphy.com | Allows users to share GIF images. This feature is on by default but can be disabled in Control Hub | Webex App |
| safebrowsing.googleapis.com | Used to perform safety checks on URLs before unfurling them in the message stream. This feature is on by default, but can be disabled in Control Hub | Webex App |
| *.walkme.com s3.walkmeusercontent.com | Webex User Guidance client. Provides onboarding and usage tours for new users For more info, see https://support.walkme.com/knowledge-base/access-requirements-for-walkme/ | Webex web based apps |
| msftncsi.com/ncsi.txt captive.apple.com/hotspot-detect.html | Third-party internet connectivity checks to identify cases where there is a network connection but no connection to the Internet. The Webex app performs its own internet connectivity checks but can also use these 3rd party URLs as a fallback. | Webex App |
| *.appdynamics.com *.eum-appdynamics.com | Performance tracking, error and crash capture, session metrics (1) | Webex App Webex Web App |
| *.amplitude.com | A/B testing & metrics (1) | Webex Web App |
| *.livestream.webex.com *.vbrickrev.com | These domains are used by attendees viewing Webex Events | Webex Events |
| *.livestreaming.webex.com | This domain is used by attendees for viewing Webex Webcasts | Webex Webcasts |
| *.slido.com *.sli.do *.data.logentries.com slido-assets-production.s3.eu-west-1.amazonaws.com | Used for Slido PPT add-in and to allow Slido webpages to create polls/quizzes in pre-meeting Used for exporting questions and answers, poll results, etc, from Slido | All |
| *.quovadisglobal.com *.digicert.com *.godaddy.com *.globalsign.com *.identrust.com *.lencr.org | Used to request Certificate Revocation Lists from these Certificate Authorities Note - Webex supports both CRL and OCSP stapling to determine the revocation status of certificates. With OCSP stapling, Webex apps and devices do not need to contact these Certificate Authorities | All |
| *.intel.com | Used to request Certificate Revocation Lists and check the certificate status with Intel’s OCSP service, for certificates sent with background images used by Webex apps and devices | All |
| *.google.com *.googleapis.com | Notifications to Webex apps on mobile devices (e.g. new message) Google Firebase Cloud Messaging (FCM) service https://firebase.google.com/docs/cloud-messaging Apple Push Notification Service (APNS) https://support.apple.com/en-us/HT203609 Note - For APNS, Apple only list the IP subnets for this service | Webex App |
| cdnjs.cloudflare.com cdn.jsdelivr.net static2.sharepointonline.com appsforoffice.microsoft.com ajax.aspnetcdn.com | URLs for Webex Scheduler for Microsoft Outlook Microsoft Outlook users can use the Webex Scheduler to schedule Webex meetings or Webex Personal Room meetings directly from Microsoft Outlook in any browser. For details see: Click here | All |
| Core Webex services being deprecated |
| URL | Description | Webex Apps and devices using these domains / URLs |
| *.clouddrive.com | Webex storage for user generated content and logs File storage on clouddrive.com was replaced by webexcontent.com in Oct 2019 Organizations with long retention periods for user generated content may still be using cloudrive.com to store older files | All |
| *.ciscosparkcontent.com | Log file uploads The log file storage service now uses the *.webexcontent.com domain | Webex App |
| *.rackcdn.com | Content Delivery Network (CDN) for the *.clouddrive.com domain | All |

| Cisco Webex Hybrid services URLs |
|---|
| URL | Description | Used by: |
| *.docker.com (1) *.docker.io (1) *dkr.ecr.us-east-1.amazonaws.com | Hybrid Services Containers | Video Mesh Node Hybrid Data Security Node |
| *s3.amazonaws.com (1) | Log File uploads | Video Mesh Node Hybrid Data Security Node |
| *.cloudconnector.webex.com | User Synchronization | Hybrid Services Directory Connector |

| Product | Authentication Type | Proxy Configuration |
|---|---|---|
| Webex for Mac | No Auth, Basic, NTLM (1) | Manual, WPAD, PAC |
| Webex for Windows | No Auth, Basic, NTLM (2) | Manual, WPAD, PAC, GPO |
| Webex for iOS | No Auth, Basic, Digest, NTLM | Manual, WPAD, PAC |
| Webex for Android | No Auth, Basic, Digest, NTLM | Manual, PAC |
| Webex Web App | No Auth, Basic, Digest, NTLM, Negotiate | Supported via OS |
| Cisco Video devices | No Auth, Basic, Digest | WPAD, PAC, or Manual |
| Webex Video Mesh Node | No Auth, Basic, Digest, NTLM | Manual |
| Hybrid Data Security Node | No Auth, Basic, Digest | Manual |
| Hybrid Services Host Management Connector | No Auth, Basic | Manual Configuration Expressway C: Applications > Hybrid Services > Connector Proxy |
| Hybrid Services: Directory Connector | No Auth, Basic, NTLM | Supported via Windows OS |
| Hybrid Services Expressway C: Calendar connector | No Auth, Basic, NTLM | Manual Configuration Expressway C: Applications > Hybrid Services > Connector Proxy : Username Password Expressway C: Applications > Hybrid Services > Calendar Connector > Microsoft Exchange> Basic and/or NTLM |
| Hybrid Services Expressway C: Call connector | No Auth, Basic | Manual Configuration Expressway C: Applications > Hybrid Services > Connector Proxy |

| Product | Supports Custom Trusted CAs for TLS inspection |
|---|---|
| Webex App (Windows, Mac, iOS, Android, Web) | Yes* |
| Cisco Video Devices | Yes |
| Cisco Webex Video Mesh | Yes |
| Hybrid Data Security Service | Yes |
| Hybrid Services – Directory, Calendar, Management Connectors | No |

| Product | Supports 802.1X | Notes |
|---|---|---|
| Webex App (Windows, Mac, iOS, Android, Web) | Yes | Supported via OS |
| Cisco Video Devices | Yes | EAP-FAST EAP-MD5 EAP-PEAP EAP-TLS EAP-TTLS Configure 802.1X via GUI or Touch 10 Upload Certs via HTTP interface |
| Video Mesh Node | No | Use MAC address bypass |
| Hybrid Data Security Service | No | Use MAC address bypass |
| Hybrid Services – Directory, Calendar, Management Connectors | No | Use MAC address bypass |

| Ports and Protocols for Webex SIP Services |
|---|
| Source Port | Destination Port | Protocol | Description |
| Expressway Ephemeral ports | Webex cloud 5060 - 5070 | SIP over TCP/TLS/MTLS | SIP signaling from Expressway E to the Webex cloud Transport protocols: TCP/TLS/MTLS |
| Webex Cloud Ephemeral ports | Expressway 5060 - 5070 | SIP over TCP/TLS/MTLS | SIP signaling from the Webex cloud to Expressway E Transport protocols: TCP/TLS/MTLS |
| Expressway 36000 - 59999 | Webex cloud 49152 -59999 | RTP/SRTP over UDP | Unencrypted/ Encrypted media from Expressway E to the Webex cloud Media Transport protocol: UDP |
| Webex cloud 49152 - 59999 | Expressway 36000 - 59999 | RTP/SRTP over UDP | Unencrypted/ Encrypted media from the Webex cloud to Expressway E Media Transport protocol: UDP |

| Protocol | Port Number(s) | Direction | Access Type | Comments |
|---|---|---|---|---|
| TCP | 5061, 5062 | Inbound | SIP Signalling | Inbound SIP signaling for Webex Edge Audio |
| TCP | 5061, 5065 | Outbound | SIP Signalling | Outbound SIP signaling for Webex Edge Audio |
| TCP/UDP | Ephemeral Ports 8000 - 59999 | Inbound | Media Ports | On an enterprise firewall, pinholes need to be opened up for incoming traffic to Expressway with a port range from 8000 - 59999 |

| Revision Date | New and Changed Information |
|---|---|
| 3/16/2026 | In the IPv4 Subnets for Media Services section, updated the incorrect IP address range from 163.129.0.0/16 to 163.129.0.0/17. |
| 2/19/2026 | Corrected previous change (2/18) to reflect correct wording - 'Cloud registered Cisco Video devices use HTTPS signaling for all Webex services, including requests to activation.webex.com which sets the system time.' |
| 2/18/2026 | Added note on cloud registered devices using the URL 'activation.webex.com' to get NTP to the 'Summary of device types and protocols supported by Webex' section. |
| 2/11/2026 | Added 'WxC Voicemail to mail notifications' to description for *.sparkpostmail entry in to the 'Additional Webex Related Services - Third Party Domains' section. |
| 12/15/2025 | Removed Webex Android App from *.amplitude.com list in the Cisco Webex Service URLs table. Added *livestreaming.webex.com to new Webex Webcast entry in the Cisco Webex Service URLs table under the third-party domain section. Added ajax.aspnetcdn.com to Webex Scheduler URLs in the Cisco Webex Service URLs table under the third-party domain section. |
| 11/10/2025 | Updated broken link for Google Firebase Cloud Messaging (FCM) service. Added *.akamaitechnologies.com to CDN list (used by Webex RoomOS Endpoints) |
| 06/30/2025 | Removed the row (starting with speech.googleapis.com and texttospeech.googleapis.com ). All traffic related to the service now goes exclusively to domains under the already documented *. webex.com and *. wbx2.com domains. |
| 6/24/2025 | New subnet added to IPv4 Subnets for Media Services section - 4.144.190.0/24* (this range will be used starting July 8, 2025) |
| 4/8/2025 | New subnet added to IPv4 Subnets for Media Services section - 4.152.180.0/24 |
| 4/4/2025 | Addition of Globalsign.com domain Root CA for timestamp server |
| 4/4/2025 | Removal of unused IP subnet 66.114.160.0/20 |
| 1/6/2025 | IP Address Ranges added to support IPv6 traffic |
| 10/17/2024 10/21/2024 | Updated 08/19/2024 revision history. Changed (*.webexconnect.com) to the correct entry of (*.webexcontent.com) |
| 08/19/2024 | Included images with Branding logos for the (*.webexcontent.com) Domains and URLs section |
| 08/02/2024 | Webex IPv6 Support section - Changed text to emphasize the MTU size for IPv4 and IPv6 traffic. |
| 07/26/2024 | Added new subdomain *dkr.ecr.us-east-1.amazonaws.com under Additional URLs for Webex Hybrid Services |
| 07/26/2024 | Guidance on recommended IP packet Maximum Transmissible Unit (MTU) size for IPv6 traffic to Webex Services |
| 04/08/2024 | Added a missing period before (*webex.com and *cisco.com) under the Cisco Webex Servers URLs subdomain |
| 12/06/2023 | Revised introduction with a focus on the Webex Suite of Services |
| 12/06/2023 | Revision of section: Transport protocols and encryption ciphers for cloud registered Webex apps and devices. Updated information on the TLS versions and Cipher Suites in use and preferred by Webex Suite Services Additional details and guidance on media transport protocols Cisco Video devices now support sending media over TLS through a Proxy server, aligning behavior with that of the Webex app. Addition of guidance on Proxy configuration (Webex strongly recommends that you do not alter or delete HTTP header values as they pass through your proxy/ firewall unless permitted…) |
| 12/06/2023 | Revision of IP subnets for Webex media services section Media services no longer reside in AWS, only in Webex Data Centres and Microsoft Azure Data Centres for VIMT. Additional text on media transport protocols and preferences |
| 12/06/2023 | Webex signaling traffic and Enterprise Proxy Configuration section Addition of guidance on Proxy configuration (Webex strongly recommends that you do not alter or delete HTTP header values as they pass through your proxy/ firewall unless permitted…) |
| 12/06/2023 | Cisco Webex Services URLs table: Rows 1 and 2 merged (*.webex.com, *.cisco.com, *.wbx2.com etc) The text is to be revised to reflect that the Webex suite uses common services for meetings and messaging. *.livestream.webex.com added for Webex Webcasts A section on Core Webex services being deprecated: Text simplified |
| 10/09/2023 | A link to VIMT doc has been included |
| 8/29/2023 | Removed port 444 TLS for Video Mesh Node (no longer used). |
| 5/24/2023 | Added Webex Events – Network Requirements |
| 2/23/2023 | New IP subnets for media added (144.196.0.0/16 and 163.129.0.0/16)  These IP subnets will be activated 30 days or more after publication here. |
| 2/9/2023 | Republished (fixed non clickable tabs) |
| 1/23/2023 | Republished with duplicated subnets removed (66.114.169.0 and 66.163.32.0) |
| 1/11/2023 | Webex Web App and SDK - TLS added as a fallback transport protocol for encrypted audio, video and content sharing if UDP and TCP cannot be used |
| 1/11/2023 | New IP subnets for media added: 4.152.214.0/24, 4.158.208.0/24, 4.175.120.0/24 (Azure Data Centres for VIMT) |
| 10/14/2022 | New slido URL added : *.slido-assets-production.s3.eu-west-1.amazonaws.com |
| 9/15/2022 | New IP subnet for media added : 20.120.238.0/23 (Azure Data Centre for VIMT) |
| 9/12/2022 | URLs for Webex Scheduler for Microsoft Outlook added. |
| 8/12/2022 | A note was added in Port Number and Protocols section. RoomOS devices do not send media transported over TLS to a configured Proxy server. |
| 8/12/2022 | The IP subnets for Webex media – AWS IP subnet 18.230.160.0/25 have been removed from the IP subnets table. These media nodes now used Cisco-owned IP addresses in subnets already listed in the table. |
| 8/12/2022 | A note was added to emphasize that access to all domains and subdomains is required for the listed URLs under the Domains and URLs for Webex services section. |
| 6//25/2022 | Requirements for Google and Apple notification services added |
| 6/25/2022 | New webex URL *.webexapis.com added to the domains and URLs table |
| 6/22/2022 | Additional guidance added for SIP deployments with Cisco Unified CM |
| 4/5/2022 | Removal of AWS IP subnets for media services - these subnets are obsolete |
| 12/14/2021 | New media UDP port ranges (50,000 – 53,000) added for Video Mesh Node Port 9000 for media over TCP removed – Use of this destination port for media over TCP will be deprecated in January 2022 Port 33434 for media over UDP and TCP removed – Use of the destination port for media over UDP and TCP will be deprecated in January 2022 |
| 11/11/2021 | Updated Webex Services-Port Numbers and Protocols & Cisco Webex Services URLs table. |
| 10/27/2021 | Added *.walkme.com and s3.walkmeusercontent.com in the domains table. |
| 10/26/2021 | Added Guidance on Proxy settings for Windows OS |
| 10/20/2021 | Added CDN URLs to the domain allow list in your firewall |
| 10/19/2021 | The Webex app uses AES-256-GCM or AES-128-GCM to encrypt content for all Webex Meeting types. |
| 10/18/2021 | Added new IP subnets (20.57.87.0/24*, 20.76.127.0/24* and 20.108.99.0/24*) used to host Video Integration for Microsoft Teams (aka Microsoft Cloud Video Interop) services, and the domains (*.cloudfront.net, *.akamaiedge.net, *.akamai.net and *.fastly.net) that we have added for Content Delivery Networks used by Webex services |
| 10/11/2021 | Updated the Trust Portal link in Domain and URL section. |
| 10/04/2021 | Removed *.walkme.com and s3.walkmeusercontent.com from domains table as they are no longer needed. |
| 07/30/2021 | Updated the Note in Proxy Features section |
| 07/13/2021 | Updated the Note in Proxy Features section |
| 07/02/2021 | Changed *.s3.amazonaws.com to *s3.amazonaws.com |
| 06/30/2021 | Updated the Additional URLs for Webex Hybrid Services list. |
| 06/25/2021 | Added *.appdynamics.com domain to the list |
| 06/21/2021 | Added *.lencr.org domain to the list. |
| 06/17/2021 | Updated Ports and Protocols for Webex SIP Services table |
| 06/14/2021 | Updated Ports and Protocols for Webex SIP Services table |
| 05/27/2021 | Updated the table in Additional URLs for Webex Hybrid Services section. |
| 04/28/2021 | Added domains for Slido PPT add-in and to allow Slido webpages to create polls/quizzes in pre-meeting |
| 04/27/2021 | Added 23.89.0.0/16 IP range for Webex Edge Audio |
| 04/26/2021 | Added 20.68.154.0/24* as it is an Azure Subnet |
| 04/21/2021 | Updated the Webex Services CSV file under Additional URLs for Webex Hybrid Services |
| 04/19/2021 | Added 20.53.87.0/24* as it is an Azure DC for VIMT/CVI |
| 04/15/2021 | Added domain *.vbrickrev.com for Webex Events Webcasts. |
| 03/30/2021 | Substantial document layout revision. |
| 03/30/2021 | Details of Webex web-based app and Webex SDK media support added (No media over TLS). |
| 03/29/2021 | Webex Edge for devices features listed with a link to the documentation. |
| 03/15/2021 | Added domain *.identrust.com |
| 02/19/2021 | Added section for Webex Services for FedRAMP customer |
| 01/27/2021 | *.cisco.com domain added for Cloud Connected UC service, and Webex Calling onboarding IP subnets for Video Integration for Microsoft Teams (aka Microsoft Cloud Video Interop) indicated by * |
| 01/05/2021 | New document that describes the network requirements for the Webex app Meetings and Messaging services |
| 11/13/20 | Removed subnet https://155.190.254.0/23 from the IP subnets for media table |
| 10/7/2020 | Removed *.cloudfront.net row from Additional URLs for Webex Teams Hybrid Services |
| 9/29/2020 | New IP subnet (20.53.87.0/24) added for Webex Teams Media services |
| 9/29/2020 | Webex devices renamed to Webex Room devices |
| 9/29/2020 | *.core-os.net URL removed from table : Additional URLs for Webex Teams Hybrid Services |
| 9/7/2020 | Updated AWS regions link |
| 08/25/20 | Simplification of the table and text for Webex Teams IP subnets for media |
| 8/10/20 | Additional details added on how reachability to media nodes is tested and Cisco IP subnet usage with Webex Edge Connect |
| 7/31/20 | Added new IP subnets for media services in AWS and Azure data centers |
| 7/31/20 | Added new UDP destination media ports for SIP calls to the Webex Teams cloud |
| 7/27/20 | Added 170.72.0.0/16 (CIDR) or 170.72.0.0 - 170.72.255.255 (net range) |
| 5/5/20 | Added sparkpostmail.com in Third Party domains table |
| 4/22/20 | Added new IP range 150.253.128.0/17 |
| 03/13/20 | New URL added for the walkme.com service TLS media transport for Room OS devices added New section added : Network Requirements for Hybrid Calling SIP Signalling Link added for the Webex Calling network requirements document |
| 12/11/19 | Minor text changes, Update of the Webex Teams Apps and Devices – Port Numbers and Protocols table, Update and reformat of the Webex Teams URLs tables. Remove NTLM Proxy Auth support for Management Connector and Call Connector hybrid services |
| 10/14/19 | TLS Inspection support for Room Devices added |
| 9/16/2019 | Addition of TCP support requirement for DNS systems using TCP as a transport protocol. Addition of the URL *.walkme.com – This service provides onboarding and usage tours for new users. Amendments to the service URLs used by Web Assistant. |
| 8/28/2019 | *.sparkpostmail1.com URL added e-mail service for newsletters, registration info, announcements |
| 8/20/2019 | Proxy support added for Video Mesh Node and Hybrid Data Security service |
| 8/15/2019 | Overview of Cisco and AWS data centre used for Webex Teams Service. *.webexcontent.com URL added for file storage Note on deprecation of clouddrive.com for file storage *.walkme.com URL added for metrics and testing |
| 7/12/2019 | *.activate.cisco.com and *.webapps.cisco.com URLs added Text to Speech URLs updated to *.speech-googleapis.wbx2.com and *.texttospeech-googleapis.wbx2.com *.quay.io URL removed Hybrid Services Containers URL updated to *.amazonaws.com |
| 6/27/2019 | Added *.accompany.com allowed list requirement for People Insights feature |
| 4/25/2019 | Added 'Webex Teams services' for line about TLS version support. Added 'Webex Teams' to media streams line under Media traffic. Added 'geographic' before region in Webex Teams IP subnets for media section. Made other minor edits to wording. Edited Webex Teams URLs table, by updating URL for A/B testing & metrics, and adding new row for Google Speech Services. In 'Additional URLs for Webex Teams Hybrid Services' section, removed '10.1' version info after AsyncOS. Updated text in 'Proxy Authentication Support' section. |
| 3/26/2019 | Changed the URL linked here "please refer to the WSA Webex Teams configuration document for guidance" from https://www.cisco.com/c/dam/en/us/products/collateral/security/web-security-appliance/guide-c07-739977.pdf to https://www.cisco.com/c/en/us/td/docs/security/wsa/wsa11-5/user_guide/b_WSA_UserGuide_11_5_1.html Changed the URL "api.giphy.com" to *.giphy.com |
| 2/21/2019 | Updated 'Webex Calling' to read "Webex Calling (formerly Spark Calling) as requested by John Costello, due to upcoming product launch of same name - Webex Calling through BroadCloud. |
| 2/6/2019 | Updated text 'Hybrid Media Node' to read 'Webex Video Mesh Node' |
| 1/11/2019 | Updated text 'End to End encrypted files uploaded to Webex Teams spaces and Avatar storage' to now read 'End to End encrypted files uploaded to Webex Teams spaces, Avatar storage, Webex Teams branding Logos' |
| 1/9/2019 | Updated to remove following line: '*In order for Webex Room devices to obtain the CA certificate necessary to validate communication through your TLS-inspecting proxy, please contact your CSM, or open a case with the Cisco TAC.' |
| 5th December 2018 | Updated URLs: Removed 'https://' from 4 entries in the Webex Teams URLs table: https://api.giphy.com                           ->  api.giphy.com https://safebrowsing.googleapis.com             ->  safebrowsing.googleapis.com http://www.msftncsi.com/ncsi.txt                ->  msftncsi.com/ncsi.txt https://captive.apple.com/hotspot-detect.html   ->  captive.apple.com/hotspot-detect.html Updated linked .CSV file for Webex Teams to show revised links shown above |
| 30th November 2018 | New URLs : *.ciscosparkcontent.com, *.storage101.ord1.clouddrive.com, *.storage101.dfw1.clouddrive.com, *.storage101.iad3.clouddrive.com, https://api.giphy.com, https://safebrowsing.googleapis.com, http://www.msftncsi.com/ncsi.txt, https://captive.apple.com/hotspot-detect.html, *.segment.com, *.segment.io, *.amplitude.com,*.eum-appdynamics.com, *.docker.io, *.core-os.net, *.s3.amazonaws.com, *.identity.api.rackspacecloud.com |
| Support for additional Proxy Authentication Methods for Windows, iOS and Android |
| Webex Board adopts Room Device OS and features ; Proxy features shared by Room Devices: SX, DX, MX, Room Kit series and Webex Board |
| Support for TLS Inspection by iOS and Android Apps |
| Removal of support for TLS Inspection removed on Room Devices: SX, DX, MX, Room Kit series and Webex Board |
| Webex Board adopts Room Device OS and features ; 802.1X support |
| 21st November 2018 | Following Note added to IP Subnets for media section : The above IP range list for cloud media resources is not exhaustive, and there may be other IP ranges used by Webex Teams which are not included in the above list. However, the Webex Teams app and devices will be able to function normally without being able to connect to the unlisted media IP addresses. |
| 19th October 2018 | Note added : Webex Teams use of third parties for diagnostic and troubleshooting data collection; and the collection of crash and usage metrics. The data that may be sent to these third party sites is described in the Webex Privacy datasheet. For details see : https://www.cisco.com/c/dam/en_us/about/doing_business/trust-center/docs/cisco-webex-privacy-data-sheet.pdf |
| Separate table for Additional URLs used by Hybrid Services : *.cloudfront.net, *.docker.com, *.quay.io, *.cloudconnector.cisco.com, *.clouddrive.com |
| 7th August 2018 | Note added to Ports and Protocols table : If you configure a local NTP and DNS server in the Video Mesh Node’s OVA, then ports 53 and 123 are not required to be opened through the firewall. |