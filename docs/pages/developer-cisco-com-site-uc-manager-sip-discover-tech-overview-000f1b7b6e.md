---
doc_id: developer-cisco-com-site-uc-manager-sip-discover-tech-overview-000f1b7b6e
source_url: https://developer.cisco.com/site/uc-manager-sip/discover/tech-overview/
retrieved_at: 2026-08-25T21:11:29.522660+00:00
---

# Cisco Unified Presence Developer Guide

Session Initiation Protocol(SIP) is a Internet Engineering Task Force (IETF) standard for multimedia communication and conferencing over IP: telephone calls, video, instant messaging/presence, etc. can be supported. SIP is an ASCII-based, application-layer control (defined in RFC 3261) that can be used to establish, maintain, and terminate calls between two or more endpoints. Like other VoIP protocols, SIP is designed to address the functions of signaling and session management within a packet telephony network.

A SIP network may be composed of:

- User Agent (UA)- UA comprises a combination of user agent client (UAC) and user agent server (UAS) that initiates and receives calls. A UAC initiates a SIP request. A UAS, a server application, contacts the user when it receives a SIP request. The UAS then responds on behalf of the user. Cisco SIP phones and SIP gateways act as client UAs.

- Back-to-Back-User -Agent(B2BUA)- A B2BU can act as both UAC and UAS, both initiating and receiving SIP requests on behalf of UACs, acting as a feature provider and protocol translator. Cisco Unified CallManager and CallManager Express can act as B2BUAs.

- SIP Proxy Server - The proxy server works as an intermediate device that receives SIP requests from a client and then forwards the requests on the client's behalf. Proxy servers can provide functions such as authentication, authorization, network access control, routing, reliable request retransmission, and security. Cisco Unified CallManager and CallManager Express SIP trunk features can connect to a SIP Proxy.

- Registrar Server - The registrar server processes requests from user agent clients for registration of their current location. Proxy servers often contain registrar servers. Cisco Unified CallManager SIP Line features can act as a Registrar server to SIP endpoints/phones.

SIP Trunk - Cisco Unified CallManager SIP Trunk signaling interfaces connect CallManager clusters with external SIP User Agents, such as SIP gateways, applications, and SIP proxy servers. Applications which handle SIP calls, but do not need to register SIP endpoints or use line-specific SIP features can be implemented using SIP trunks. SIP presence subscription (SIP/SIMPLE) is also supported via SIP trunks.

SIP Line - Cisco Unified CallManager SIP Line features provide SIP registration services, as well as SIP feature support for additional capabilities required by desktop phones/soft-phones.

# Overview for SIP Connection Pack for Unified CM Business Edition 3000

Cisco BE 3000 is a Unified Communication solution targeted at small and medium businesses with less than 300 users. The solution provides communication experience for your employees and customers with competitive price, productive features and easy to maintain management interfaces. It is built based on the proven technology of Cisco Call manager. For more information on Cisco BE3000 product information, please visit

http://www.cisco.com/go/be3000

Cisco Business Edition 3000 SIP trunk provides SIP interface to connect BE3000 with service provider SIP network via session border elements for PSTN access. BE 3000 leverages a subset of SIP signaling functionality of Cisco Call Manager SIP trunk, and provides a simpler and easier way to provision SIP trunk. For the details of BE 3000 SIP trunk capability and configuration guide, please refer to the documentation section for BE 3000 SIP trunk.