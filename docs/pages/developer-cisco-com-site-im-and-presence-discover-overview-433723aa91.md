---
doc_id: developer-cisco-com-site-im-and-presence-discover-overview-433723aa91
source_url: https://developer.cisco.com/site/im-and-presence/discover/overview/
retrieved_at: 2026-08-25T21:05:33.144724+00:00
---

# Cisco Unified Presence Interfaces

The Cisco Unified Presence server uses standards-based Session Initiation Protocol ( SIP ) , SIP for Instant Messaging and Presence Leveraging Extensions ( SIMPLE ) , and Extensible Messaging and Presence Protocol ( XMPP ) to provide a common demarcation point for integrating clients and applications into the Cisco Unified Communications System.

Cisco Unified Presence also provides a HTTP interface that has a configuration interface through Simple Object Access Protocol ( SOAP ), a presence interface through Representational State Transfer ( REST ), and a presence, instant messaging, and roster interface through the Cisco AJAX XMPP Library ( CAXL ) . CAXL communicates to the Bidirectional-streams Over Synchronous HTTP ( BOSH ) interface on the Extensible Communications Platform within Cisco Unified Presence.

The Cisco Unified Presence server collects, aggregates, and distributes user capabilities and attributes using these standards-based  SIP/SIMPLE, XMPP, BOSH, SOAP, and REST interfaces.

Session Initiation Protocol (SIP) and SIP for Instant Messaging and Presence Leveraging Extensions (SIMPLE)

The SIP/SIMPLE based interfaces for Cisco Unified Presence provide the following functionality:

Availability (PUBLISH, SUBSCRIBE and NOTIFY interfaces)

Unified Client Change Notification (UCCN) subscription (SUBSCRIBE and NOTIFY interfaces)

Instant Messaging (Page mode MESSAGE)

For more information on SIP/SIMPLE, please click here .

eXtensible Messaging and Presence Protocol (XMPP)

The XMPP Presence and Instant Messaging protocol is the core protocol on Cisco Unified Presence.
                        This interface provides instant messaging, availability and roster management services.

For more information on XMPP, please click here .

Bidirectional-streams Over Synchronous HTTP (BOSH)

The BOSH interface allows allows integration with instant messaging, availability and roster management services from Cisco Unified Presence into your web-based applications. Cisco provide the Cisco AJAX XMPP Library (CAXL) as a JavaScript based XMPP client library that allows developers to build web applications which utilize the BOSH interface

For more information on CAXL, please click here .

Client Configuration Web Service (SOAP)

The Client Configuration Web Service is an interface to Cisco Unified Presence that allows client applications to manage user preference information such as contacts, presence rules, access control lists, and calendaring options. This web service is available via a Simple Object Access Protocol (SOAP) interface.

For more information on the Client Configuration Web Service, please click here

Presence Web Service (SOAP/REST)

The Presence Web Service is an open interface that allows client applications to share user presence information with Cisco Unified Presence. This interface is used by developers to build client applications that can send and receive user presence state updates. The web service is available via a SOAP interface and a REST (HTTP/XML) interface.

For more information on the Presence Web Service, please click here

Platform SOAP Service (SOAP)

The Platform SOAP Services facilitate upgrades and install of COP file for large scale deployments of Cisco Unified Presence, to be initiated and monitored from a single management client. This service provides a web-based SOAP interface integrated with the existing upgrade framework.

For more information on the Platform SOAP Service, please click here

# Cisco Unified Presence Architecture Highlights

Cisco Unified Presence supports the following high level functions:

Enterprise Instant Messaging

Point-to-Point Instant Messaging (CUP 1+)

Multi-Device instant Messaging (CUP 8+)

Text Conferencing (Group Chat)

Ad-hoc Group Chat (CUP 8+)

Persistent Group Chat (requires an off-board Postgres Database) (CUP 8+)

Network based Rich Presence

Cisco Unified Communications Manager Telephony Presence (CUP 1+)

Microsoft Exchange Calendar Presence:

Web-based Distributed Authoring and Versioning (WebDav) (CUP 6+)

Exchange Web Services (EWS) (CUP 8.5.1+)

Contact Management

Management of a user's roster (also referred to as buddy list) (CUP 1+)

Management of a user's non roster contacts. (also referred to "pizza guy" contacts) (CUP 7+)

Policy and User Preferences

Microsoft Exchange Calendar Presence:

Cisco Unified Presence Administration/End User GUI (CUP 6+)

Client Configuration Web Service (SOAP) interface (CUP 7+)

Extensible Messaging and Presence Protocal (XMPP) interface (CUP 8+)

Inter-Domain Federation

XMPP federation to:

IBM Sametime (CUP 8+)

Google Talk (CUP 8+)

WebEx (CUP8+)

Cisco Unified Presence 8+ (CUP 8+)

Any other server that is XMPP Standards compliant (CUP8+)

SIP federation to:

Microsoft Office Communications Server 2007 R2 (CUP 7+)

AOL AIM (CUP 8.5.1+)

Microsoft Lync Server 2010 (CUP8.5.2+)

Intra-Domain Partitioned Federation

Microsoft Live Communications Server 2005 Standard Edition and Enterprise Edition (CUP 8.6.1+)

Microsoft Office Communications Server 2007 R2 Standard Edition and Enterprise Edition (CUP 8.6.1+)

Remote Call Control

Microsoft Live Communications Server 2005 Standard or Enterprise (CUP 1+)

Microsoft Office Communications Server 2007 or 2007 R2, Standard or Enterprise (CUP 7+)

Microsoft Lync Server 2010 Standard Edition and Enterprise Edition (CUP 8.5.2+)

Open APIs

SIP for Instant Messaging and Presence Leveraging Extensions (SIMPLE) (CUP 1+)

Simple Object Access Protocol (SOAP) (CUP 7+)

Representational State Transfer (REST) (CUP 7+)

Extensible Messaging and Presence Protocol (XMPP) (CUP 8+)

Bidirectional Streams over Synchronous HTTP (BOSH) (CUP 8+)

Compliance (CUP 8+)

The options are using an ODBC-based external database connection for message archiving using native Jabber components or the customer deploying a FaceTime server which connects to CUP through the XDB interface.

High Availability (CUP 7+, CUP 8.5.1+, but not CUP 8.0.x)

Allows for users on one Cisco Unified Presence node within a subcluster to automatically fail-over to the other node within the
subcluster.

Clustering over WAN (CUP 7.0.5, CUP 8.5.1+, but not CUP 8.0.x)

A Cisco Unified Presence cluster can be deployed with one of the nodes of a subcluster deployed across the Wide Area Network (WAN). This allows for geographic redundancy of a subcluster and high availability for the users between the nodes across the sites.

File Transfer (CUP 8+)

Peer to Peer mode of file transfer using out of band signaling (SOCKS5).

Supports file transfer  for XMPP clients only. File transfer to chat rooms is not supported.

No File Transfer Proxy is supported so transfers to clients behind a firewall (including federated clients) is not supported.

# Cisco Unified Presence System Architecture

Below is a diagram which shows the overall Cisco Unified Presence system architecture.