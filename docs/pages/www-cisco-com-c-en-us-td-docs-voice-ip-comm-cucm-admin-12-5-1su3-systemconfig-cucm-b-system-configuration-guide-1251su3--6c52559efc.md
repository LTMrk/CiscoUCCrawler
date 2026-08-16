---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su3-systemconfig-cucm-b-system-configuration-guide-1251su3--6c52559efc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU3/systemConfig/cucm_b_system-configuration-guide-1251su3/cucm_m_port-usage-information-for-imp-12-0.html
retrieved_at: 2026-08-16T17:43:13.251139+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: July 31, 2025

Chapter: Port Usage Information for the IM and Presence Service

## Chapter: Port Usage Information for the IM and Presence Service

# Port Usage Information for the IM and Presence Service

## IM and Presence Service Port Usage Overview

This document provides a list of the TCP and UDP ports that
                              		  the IM and Presence Service uses for intracluster connections and for
                              		  communications with external applications or devices. It provides important
                              		  information for the configuration of firewalls, Access Control Lists (ACLs),
                              		  and quality of service (QoS) on a network when an IP Communications solution is
                              		  implemented.

Cisco has not verified all possible configuration scenarios for
                                          			 these ports. If you are having configuration problems using this list, contact
                                          			 Cisco technical support for assistance.

While virtually all protocols are bidirectional, this
                              		  document gives directionality from the session originator perspective. In some
                              		  cases, the administrator can manually change the default port numbers, though
                              		  Cisco does not recommend this as a best practice. Be aware that the IM and Presence Service opens several ports strictly for internal use.

Ports in this document apply specifically to the IM and Presence Service . Some ports change from one release to another, and future
                              		  releases may introduce new ports. Therefore, make sure that you are using the
                              		  correct version of this document for the version of IM and Presence Service that
                              		  is installed.

Configuration of firewalls, ACLs, or QoS will vary depending
                              		  on topology, placement of devices and services relative to the placement of
                              		  network security devices, and which applications and telephony extensions are
                              		  in use. Also, bear in mind that ACLs vary in format with different devices and
                              		  versions.

## Information Collated in Table

This table defines the information collated in each of the tables in this document.

Table Heading

Description

From

The client sending requests to this port

To

The client receiving requests on this port

Role

A client or server application or process

Protocol

Either a Session-layer protocol used for establishing and ending communications, or an Application-layer protocol used for
                                          request and response transactions

Transport Protocol

A Transport-layer protocol that is connection-oriented (TCP) or connectionless (UDP)

Destination / Listener

The port used for receiving requests

Source / Sender

The port used for sending requests

## IM and Presence Service Port List

The
                              		  following tables show the ports that the IM and
                                 			 Presence Service uses for intracluster and intercluster traffic.

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

SIP
                                          					 Gateway

--------------

IM and Presence

IM and Presence

--------------

SIP
                                          					 Gateway

SIP

TCP/UDP

5060

Ephemeral

Default
                                          					 SIP Proxy UDP and TCP Listener

SIP
                                          					 Gateway

IM and Presence

SIP

TLS

5061

Ephemeral

TLS Server
                                          					 Authentication listener port

IM and Presence

IM and Presence

SIP

TLS

5062

Ephemeral

TLS Mutual
                                          					 Authentication listener port

IM and Presence

IM and Presence

SIP

UDP / TCP

5049

Ephemeral

Internal
                                          					 port. Localhost traffic only.

IM and Presence

IM and Presence

HTTP

TCP

8081

Ephemeral

Used for
                                          					 HTTP requests from the Config Agent to indicate a change in configuration.

Third-party Client

IM and Presence

HTTP

TCP

8082

Ephemeral

Default IM
                                             						and Presence HTTP Listener. Used for Third-Party Clients to connect

Third-party Client

IM and Presence

HTTPS

TLS / TCP

8083

Ephemeral

Default IM
                                             						and Presence HTTPS Listener. Used for Third-Party Clients to connect

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence

IM and Presence (Presence Engine)

SIP

UDP / TCP

5080

Ephemeral

Default
                                          					 SIP UDP/TCP Listener port

IM and Presence (Presence Engine)

IM and Presence (Presence Engine)

Livebus

UDP

50000

Ephemeral

Internal
                                          					 port. Localhost traffic only. LiveBus messaging port. The IM
                                             						and Presence Service uses this port for cluster communication.

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

Browser

IM and Presence

HTTPS

TCP

8080

Ephemeral

Used for
                                          					 web access

Browser

IM and Presence

AXL /
                                          					 HTTPS

TLS / TCP

8443

Ephemeral

Provides
                                          					 database and serviceability access via SOAP

Browser

IM and Presence

HTTPS

TLS / TCP

8443

Ephemeral

Provides
                                          					 access to Web administration

Browser

IM and Presence

HTTPS

TLS / TCP

8443

Ephemeral

Provides
                                          					 access to User option pages

Browser

IM and Presence

SOAP

TLS / TCP

8443

Ephemeral

Provides
                                          					 access to Cisco Unified Personal Communicator, Cisco Unified Mobility
                                          					 Advantage, and third-party API clients via SOAP

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence

--------------

External
                                          					 Corporate Directory

External
                                          					 Corporate Directory

--------------

IM and Presence

LDAP

TCP

389

Ephemeral

Allows the Directory protocol to integrate with the external Corporate Directory. The LDAP port depends on the Corporate Directory
                                          (389 is the default). In case of Netscape Directory, customer can configure different port to accept LDAP traffic.

IM and Presence

External
                                          					 Corporate Directory

LDAPS

TCP

636

Ephemeral

Allows the
                                          					 Directory protocol to integrate with the external Corporate Directory. LDAP
                                          					 port depends on the Corporate Directory (636 is the default).

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence (Config Agent)

IM and Presence (Config Agent)

TCP

TCP

8600

Ephemeral

Config
                                          					 Agent heartbeat port

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence

Certificate Manager

TCP

TCP

7070

Ephemeral

Internal
                                          					 port - Localhost traffic only

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence (Database)

IM and Presence (Database)

TCP

TCP

1500

Ephemeral

Internal
                                          					 IDS port for Database clients. Localhost traffic only.

IM and Presence (Database)

IM and Presence (Database)

TCP

TCP

1501

Ephemeral

Internal
                                          					 port - this is an alternate port to bring up a second instance of IDS during
                                          					 upgrade. Localhost traffic only.

IM and Presence (Database)

IM and Presence (Database)

XML

TCP

1515

Ephemeral

Internal
                                          					 port. Localhost traffic only. DB replication port

From Sender

To (Listener)

Protocol

Transport Protocol

Destination / Listener

Source / Sender

Remarks

IM and Presence (IPSec)

IM and Presence (IPSec)

Proprietary

UDP/TCP

8500

8500

Internal port - cluster manager port used by the ipsec_mgr daemon for cluster replication of platform data (hosts) certs

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence (DRF)

IM and Presence (DRF)

TCP

TCP

4040

Ephemeral

DRF Master Agent server port, which accepts connections from Local Agent, GUI, and CLI

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence (RIS)

IM and Presence (RIS)

TCP

TCP

2555

Ephemeral

Real-time
                                          					 Information Services (RIS) database server. Connects to other RISDC services in
                                          					 the cluster to provide clusterwide real-time information

IM and Presence (RTMT/AMC/

SOAP)

IM and Presence (RIS)

TCP

TCP

2556

Ephemeral

Real-time
                                          					 Information Services (RIS) database client for Cisco RIS. Allows RIS client
                                          					 connection to retrieve real-time information

IM and Presence (RIS)

IM and Presence (RIS)

TCP

TCP

8889

8888

Internal
                                          					 port. Localhost traffic only. Used by RISDC (System Access) to link to servM
                                          					 via TCP for service status request and reply

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

SNMP
                                          					 Server

IM and Presence

SNMP

UDP

161, 8161

Ephemeral

Provides
                                          					 services for SNMP-based management applications

IM and Presence

IM and Presence

SNMP

UDP

6162

Ephemeral

Native SNMP agent that listens for requests forwarded by SNMP master agents

IM and Presence

IM and Presence

SNMP

UDP

6161

Ephemeral

SNMP Master agent that listens for traps from the native SNMP agent, and forwards to management applications

SNMP
                                          					 Server

IM and Presence

TCP

TCP

7999

Ephemeral

Used as a
                                          					 socket for the cdp agent to communicate with the cdp binary

IM and Presence

IM and Presence

TCP

TCP

7161

Ephemeral

Used for communication between the SNMP Master agent and subagents

IM and Presence

SNMP Trap
                                          					 Monitor

SNMP

UDP

162

Ephemeral

Sends SNMP
                                          					 traps to management applications

IM and Presence

IM and Presence

SNMP

UDP

Configurable

61441

Internal
                                          					 SNMP trap receiver

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

Gateway

--------------

IM and Presence

IM and Presence

--------------

Gateway

Ipsec

UDP

500

Ephemeral

Enables
                                          					 Internet Security Association and the KeyManagement Protocol

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence (RIS)

IM and Presence (RIS)

XML

TCP

8888 and
                                          					 8889

Ephemeral

Internal
                                          					 port. Localhost traffic only. Used to listen to clients communicating with the
                                          					 RIS Service Manager (servM).

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence

DNS Server

DNS

UDP

53

Ephemeral

The port
                                          					 that DNS server listen on for IM
                                             						and Presence DNS queries.

To: DNS
                                          					 Server | From: IM
                                             						and Presence

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence

Endpoint

SSH / SFTP

TCP

22

Ephemeral

Used by
                                          					 many applications to get command line access to the server. Also used between
                                          					 nodes for certificate and other file exchanges (sftp)

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence

--------------

Cisco
                                          					 Unified Communications Manager

Cisco
                                          					 Unified Communications Manager

--------------

IM and Presence

ICMP

IP

Not
                                          					 Applicable

Ephemeral

Internet
                                          					 Control Message Protocol (ICMP). Used to communicate with the Cisco Unified
                                          					 Communications Manager server

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence

NTP Server

NTP

UDP

123

Ephemeral

Cisco
                                          					 Unified Communications Manager is the acting NTP server. Used by subscriber
                                          					 nodes to synchronize time with the publisher node.

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

Microsoft
                                          					 Exchange

IM and Presence

HTTP
                                          					 (HTTPu)

) WebDAV -
                                          					 HTTP /UDP/IP notifications

2) EWS -
                                          					 HTTP/TCP /IP SOAP notifications

IM and Presence server port (default 50020)

Ephemeral

Microsoft
                                          					 Exchange uses this port to send notifications (using NOTIFY message) to
                                          					 indicate a change to a particular subscription identifier for calendar events.
                                          					 Used to integrate with any Exchange server in the network configuration. Both
                                          					 ports are created. The kind of messages that are sent depend on the type of
                                          					 Calendar Presence Backend gateway(s) that are configured.

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence (Tomcat)

IM and Presence (SOAP)

TCP

TCP

5007

Ephemeral

SOAP
                                          					 monitor port

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence

RTMT

TCP

TCP

1090

Ephemeral

AMC RMI
                                          					 Object port. Cisco AMC Service for RTMT performance monitors, data collection,
                                          					 logging, and alerting.

IM and Presence

RTMT

TCP

TCP

1099

Ephemeral

AMC RMI
                                          					 Registry port. Cisco AMC Service for RTMT performance monitors, data
                                          					 collection, logging, and alerting.

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

XMPP
                                          					 Client

IM and Presence

TCP

TCP

5222

Ephemeral

Client
                                          					 access port

IM and Presence

IM and Presence

TCP

TCP

5269

Ephemeral

Server to
                                          					 Server connection (S2S) port

Third-party BOSH client

IM and Presence

TCP

TCP

5280

Ephemeral

HTTP
                                          					 listening port used by the XCP Web Connection Manager for BOSH third-party API
                                          					 connections

IM and Presence (XCP Services)

IM and Presence (XCP Router

TCP

TCP

7400

Ephemeral

XCP Router Master Accept Port. XCP services that connect to the router from an Open Port Configuration (for example XCP Authentication
                                          Component Service) typically connect on this port.

IM and Presence (XCP Router

IM and Presence (XCP Router

UDP

UDP

5353

Ephemeral

MDNS port.
                                          					 XCP routers in a cluster use this port to discover each other.

IM and Presence (XCP Router

IM and Presence (XCP Router

TCP

TCP

7336

HTTPS

MFT File transfer (On-Premises only).

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence

PostgreSQL database

TCP

TCP

5432 1

Ephemeral

PostgreSQL
                                          					 database listening port

IM and Presence

Oracle database

TCP

TCP

1521

Ephemeral

Oracle database listening port

IM and Presenc

MSSQL database

TCP

TCP

1433

Ephemeral

MSSQL database listening port

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence (Server Recovery Manager)

IM and Presence (Server Recovery Manager)

TCP

TCP

20075

Ephemeral

The port
                                          					 that Cisco Server Recovery Manager uses to provide admin rpc requests.

IM and Presence (Server Recovery Manager)

IM and Presence (Server Recovery Manager)

UDP

UDP

21999

Ephemeral

The port
                                          					 that Cisco Server Recovery Manager uses to communicate with its peer.

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence

IM and Presence

Proprietary

TCP

9003

Ephemeral

Cisco Presence Datastore
                                          					 dual node subcluster replication.

IM and Presence

IM and Presence

Proprietary

TCP

9004

Ephemeral

Cisco Login Datastore dual
                                          					 node subcluster replication.

IM and Presence

IM and Presence

Proprietary

TCP

9005

Ephemeral

Cisco SIP Registration
                                          					 Datastore dual node subcluster replication.

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence

IM and Presence

Proprietary

TCP

6603

Ephemeral

Cisco
                                          					 Presence Datastore SQL Queries.

IM and Presence

IM and Presence

Proprietary

TCP

6604

Ephemeral

Cisco
                                          					 Login Datastore SQL Queries.

IM and Presence

IM and Presence

Proprietary

TCP

6605

Ephemeral

Cisco SIP
                                          					 Registration Datastore SQL Queries.

IM and Presence

IM and Presence

Proprietary

TCP

6606

Ephemeral

Cisco
                                          					 Route Datastore SQL Queries.

From
                                          					 (Sender)

To
                                          					 (Listener)

Protocol

Transport
                                          					 Protocol

Destination / Listener

Source /
                                          					 Sender

Remarks

IM and Presence

IM and Presence

Proprietary

TCP

6607

Ephemeral

Cisco
                                          					 Presence Datastore XML-based change notification.

IM and Presence

IM and Presence

Proprietary

TCP

6608

Ephemeral

Cisco
                                          					 Login Datastore XML-based change notification.

IM and Presence

IM and Presence

Proprietary

TCP

6609

Ephemeral

Cisco SIP
                                          					 Registration Datastore XML-based change notification.

IM and Presence

IM and Presence

Proprietary

TCP

6610

Ephemeral

Cisco
                                          					 Route Datastore XML-based change notification.

From (Sender)

To (Listener)

Protocol

Transport Protocol

Destination / Listener

Source / Sender

Remarks

IM and Presence (Intercluster Sync Agent)

IM and Presence (Intercluster Sync Agent)

TCP

TCP

37239

Ephemeral

Cisco Intercluster Sync Agent service uses this port to establish a socket connection for handling commands.

From (Sender)

To (Listener)

Destination Port

Purpose

Endpoint/IM and Presence

IM and Presence

7

Internet Control Message Protocol (ICMP) This protocol number carries echo-related traffic. It does not constitute a port
                                          as indicated in the column heading.

IM and Presence

Endpoint/IM and Presence

From (Sender)

To (Listener)

Transport Protocol

Destination / Listener

Source / Sender

Remarks

Cisco Unified Communications Manager

IM and Presence Publisher

TCP

1500

Bi-directional

Internal ID port for Database clients. Localhost traffic only.

Cisco Unified Communications Manager

IM and Presence Publisher

TCP

8443

Bi-directional

Provides access to Web administration.

Cisco Unified Communications Manager

IM and Presence Publisher

TCP

1090

Bi-directional

AMC RMI Object port. Cisco AMC Service for RTMT performance monitors, data collection, logging, and alerting.

Cisco Unified Communications Manager

IM and Presence Publisher

TCP

2555

Bi-directional

Bi-directional Real-time Information Services (RIS) database server. Connects to other RISDC services in the cluster to provide
                                          clusterwide real-time information.

Cisco Unified Communications Manager

IM and Presence Publisher

TCP

8500

Bi-directional

Internal port - cluster manager port used by the ipsec_mgr daemon for cluster replication of platform data (hosts) certificates.

Cisco Unified Communications Manager

IM and Presence Publisher

TCP

8600

Bi-directional

Config Agent heartbeat port

Cisco Unified Communications Manager

IM and Presence Publisher

UDP

123

Bi-directional

Network Time Protocol(NTP) used for time synchronization.

IM and Presence Publisher

IM and Presence Subscriber

UDP

50000

Bi-directional

Internal port. Localhost traffic only. LiveBus messaging port. TheIM and PresenceService uses this port for cluster communication.

IM and Presence Publisher

IM and Presence Subscriber

UDP

21999

Bi-directional

The port that Cisco Server Recovery Manager uses to communicate with its peer.

IM and Presence Publisher

Cisco Unified Communications Manager

TCP

4040

Bi-directional

DRF Master Agent server port that accepts connections from Local Agent, GUI, and CLI.

IM and Presence Publisher

Cisco Unified Communications Manager

TCP

8001

Bi-directional

Used while configuring persistent chat.

IM and Presence Publisher

Cisco Unified Communications Manager

TCP

6379

Bi-directional

Used while configuring managed file transfer (MFT).

IM and Presence Publisher

IM and Presence Subscriber

TCP

7

Bi-directional

Used while configuring external database (MSSQL).

IM and Presence Publisher

IM and Presence Subscriber

TCP

20075

Bi-directional

The port that Cisco Server Recovery Manager uses to provide admin RPC requests.

IM and Presence Publisher

IM and Presence Subscriber

TCP

8600

Bi-directional

Config Agent heartbeat port

IM and Presence Subscriber

IM and Presence Publisher

TCP

9005

Bi-directional

Cisco SIP Registration Datastore dual node presence redundancy group replication.

IM and Presence Subscriber

IM and Presence Publisher

TCP

9003

Bi-directional

Cisco Presence Datastore dual node presence redundancy group replication.

IM and Presence Subscriber

IM and Presence Publisher

TCP

20075

Bi-directional

The port that Cisco Server Recovery Manager uses to provide admin RPC requests.

IM and Presence Subscriber

IM and Presence Publisher

TCP

9004

Bi-directional

Cisco Login Datastore dual node presence redundancy group replication.

Cisco Unified Communications Manager

IM and Presence Publisher

TCP

5070

Bi-directional

Used on a call configuration

IM and Presence Publisher

IM and Presence Subscriber

TCP

44000

Bi-directional

Used on a call configuration

From (Sender)

To (Listener)

Source Port

Destination Port

Protocol

Remarks

Cisco Unified Communications Manager

IM and Presence Publisher

[37240 – 61000]

5070

TCP

IM and Presence Publisher

XMPP client (Jabber)

5222

64846

TCP

Client Access Port

IM and Presence Publisher

XMPP client (Jabber)

5222

56361

TCP

Client Access Port

From (Sender)

To (Listener)

Source Port

Destination Port

Protocol

IM and Presence Publisher

Database

[37240 – 61000]

7

TCP

From (Sender)

To (Listener)

Source Port

Destination Port

Protocol

IM and Presence Publisher

Database

37240 – 61000

1433

TCP

From (Sender)

To (Listener)

Source Port

Destination Port

Protocol

IM and Presence Publisher

External File Server

37240 – 61000

7

TCP

IM and Presence Publisher

External File Server

37240 – 61000

22

TCP

IM and Presence Publisher

External File Server

37240 – 61000

5432

TCP

IM and Presence Publisher

Database

54288 - 54292

5432

TCP

See the Cisco Unified
                                 			 Serviceability Administration Guide for information about SNMP.

| Note | Cisco has not verified all possible configuration scenarios for
                                          			 these ports. If you are having configuration problems using this list, contact
                                          			 Cisco technical support for assistance. |
|---|---|

| Table Heading | Description |
|---|---|
| From | The client sending requests to this port |
| To | The client receiving requests on this port |
| Role | A client or server application or process |
| Protocol | Either a Session-layer protocol used for establishing and ending communications, or an Application-layer protocol used for
                                          request and response transactions |
| Transport Protocol | A Transport-layer protocol that is connection-oriented (TCP) or connectionless (UDP) |
| Destination / Listener | The port used for receiving requests |
| Source / Sender | The port used for sending requests |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| SIP
                                          					 Gateway -------------- IM and Presence | IM and Presence -------------- SIP
                                          					 Gateway | SIP | TCP/UDP | 5060 | Ephemeral | Default
                                          					 SIP Proxy UDP and TCP Listener |
| SIP
                                          					 Gateway | IM and Presence | SIP | TLS | 5061 | Ephemeral | TLS Server
                                          					 Authentication listener port |
| IM and Presence | IM and Presence | SIP | TLS | 5062 | Ephemeral | TLS Mutual
                                          					 Authentication listener port |
| IM and Presence | IM and Presence | SIP | UDP / TCP | 5049 | Ephemeral | Internal
                                          					 port. Localhost traffic only. |
| IM and Presence | IM and Presence | HTTP | TCP | 8081 | Ephemeral | Used for
                                          					 HTTP requests from the Config Agent to indicate a change in configuration. |
| Third-party Client | IM and Presence | HTTP | TCP | 8082 | Ephemeral | Default IM
                                             						and Presence HTTP Listener. Used for Third-Party Clients to connect |
| Third-party Client | IM and Presence | HTTPS | TLS / TCP | 8083 | Ephemeral | Default IM
                                             						and Presence HTTPS Listener. Used for Third-Party Clients to connect |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence | IM and Presence (Presence Engine) | SIP | UDP / TCP | 5080 | Ephemeral | Default
                                          					 SIP UDP/TCP Listener port |
| IM and Presence (Presence Engine) | IM and Presence (Presence Engine) | Livebus | UDP | 50000 | Ephemeral | Internal
                                          					 port. Localhost traffic only. LiveBus messaging port. The IM
                                             						and Presence Service uses this port for cluster communication. |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| Browser | IM and Presence | HTTPS | TCP | 8080 | Ephemeral | Used for
                                          					 web access |
| Browser | IM and Presence | AXL /
                                          					 HTTPS | TLS / TCP | 8443 | Ephemeral | Provides
                                          					 database and serviceability access via SOAP |
| Browser | IM and Presence | HTTPS | TLS / TCP | 8443 | Ephemeral | Provides
                                          					 access to Web administration |
| Browser | IM and Presence | HTTPS | TLS / TCP | 8443 | Ephemeral | Provides
                                          					 access to User option pages |
| Browser | IM and Presence | SOAP | TLS / TCP | 8443 | Ephemeral | Provides
                                          					 access to Cisco Unified Personal Communicator, Cisco Unified Mobility
                                          					 Advantage, and third-party API clients via SOAP |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence -------------- External
                                          					 Corporate Directory | External
                                          					 Corporate Directory -------------- IM and Presence | LDAP | TCP | 389 | Ephemeral | Allows the Directory protocol to integrate with the external Corporate Directory. The LDAP port depends on the Corporate Directory
                                          (389 is the default). In case of Netscape Directory, customer can configure different port to accept LDAP traffic. |
| IM and Presence | External
                                          					 Corporate Directory | LDAPS | TCP | 636 | Ephemeral | Allows the
                                          					 Directory protocol to integrate with the external Corporate Directory. LDAP
                                          					 port depends on the Corporate Directory (636 is the default). |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence (Config Agent) | IM and Presence (Config Agent) | TCP | TCP | 8600 | Ephemeral | Config
                                          					 Agent heartbeat port |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence | Certificate Manager | TCP | TCP | 7070 | Ephemeral | Internal
                                          					 port - Localhost traffic only |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence (Database) | IM and Presence (Database) | TCP | TCP | 1500 | Ephemeral | Internal
                                          					 IDS port for Database clients. Localhost traffic only. |
| IM and Presence (Database) | IM and Presence (Database) | TCP | TCP | 1501 | Ephemeral | Internal
                                          					 port - this is an alternate port to bring up a second instance of IDS during
                                          					 upgrade. Localhost traffic only. |
| IM and Presence (Database) | IM and Presence (Database) | XML | TCP | 1515 | Ephemeral | Internal
                                          					 port. Localhost traffic only. DB replication port |

| From Sender | To (Listener) | Protocol | Transport Protocol | Destination / Listener | Source / Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence (IPSec) | IM and Presence (IPSec) | Proprietary | UDP/TCP | 8500 | 8500 | Internal port - cluster manager port used by the ipsec_mgr daemon for cluster replication of platform data (hosts) certs |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence (DRF) | IM and Presence (DRF) | TCP | TCP | 4040 | Ephemeral | DRF Master Agent server port, which accepts connections from Local Agent, GUI, and CLI |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence (RIS) | IM and Presence (RIS) | TCP | TCP | 2555 | Ephemeral | Real-time
                                          					 Information Services (RIS) database server. Connects to other RISDC services in
                                          					 the cluster to provide clusterwide real-time information |
| IM and Presence (RTMT/AMC/ SOAP) | IM and Presence (RIS) | TCP | TCP | 2556 | Ephemeral | Real-time
                                          					 Information Services (RIS) database client for Cisco RIS. Allows RIS client
                                          					 connection to retrieve real-time information |
| IM and Presence (RIS) | IM and Presence (RIS) | TCP | TCP | 8889 | 8888 | Internal
                                          					 port. Localhost traffic only. Used by RISDC (System Access) to link to servM
                                          					 via TCP for service status request and reply |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| SNMP
                                          					 Server | IM and Presence | SNMP | UDP | 161, 8161 | Ephemeral | Provides
                                          					 services for SNMP-based management applications |
| IM and Presence | IM and Presence | SNMP | UDP | 6162 | Ephemeral | Native SNMP agent that listens for requests forwarded by SNMP master agents |
| IM and Presence | IM and Presence | SNMP | UDP | 6161 | Ephemeral | SNMP Master agent that listens for traps from the native SNMP agent, and forwards to management applications |
| SNMP
                                          					 Server | IM and Presence | TCP | TCP | 7999 | Ephemeral | Used as a
                                          					 socket for the cdp agent to communicate with the cdp binary |
| IM and Presence | IM and Presence | TCP | TCP | 7161 | Ephemeral | Used for communication between the SNMP Master agent and subagents |
| IM and Presence | SNMP Trap
                                          					 Monitor | SNMP | UDP | 162 | Ephemeral | Sends SNMP
                                          					 traps to management applications |
| IM and Presence | IM and Presence | SNMP | UDP | Configurable | 61441 | Internal
                                          					 SNMP trap receiver |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| Gateway -------------- IM and Presence | IM and Presence -------------- Gateway | Ipsec | UDP | 500 | Ephemeral | Enables
                                          					 Internet Security Association and the KeyManagement Protocol |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence (RIS) | IM and Presence (RIS) | XML | TCP | 8888 and
                                          					 8889 | Ephemeral | Internal
                                          					 port. Localhost traffic only. Used to listen to clients communicating with the
                                          					 RIS Service Manager (servM). |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence | DNS Server | DNS | UDP | 53 | Ephemeral | The port
                                          					 that DNS server listen on for IM
                                             						and Presence DNS queries. To: DNS
                                          					 Server \| From: IM
                                             						and Presence |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence | Endpoint | SSH / SFTP | TCP | 22 | Ephemeral | Used by
                                          					 many applications to get command line access to the server. Also used between
                                          					 nodes for certificate and other file exchanges (sftp) |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence -------------- Cisco
                                          					 Unified Communications Manager | Cisco
                                          					 Unified Communications Manager -------------- IM and Presence | ICMP | IP | Not
                                          					 Applicable | Ephemeral | Internet
                                          					 Control Message Protocol (ICMP). Used to communicate with the Cisco Unified
                                          					 Communications Manager server |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence | NTP Server | NTP | UDP | 123 | Ephemeral | Cisco
                                          					 Unified Communications Manager is the acting NTP server. Used by subscriber
                                          					 nodes to synchronize time with the publisher node. |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| Microsoft
                                          					 Exchange | IM and Presence | HTTP
                                          					 (HTTPu) | ) WebDAV -
                                          					 HTTP /UDP/IP notifications 2) EWS -
                                          					 HTTP/TCP /IP SOAP notifications | IM and Presence server port (default 50020) | Ephemeral | Microsoft
                                          					 Exchange uses this port to send notifications (using NOTIFY message) to
                                          					 indicate a change to a particular subscription identifier for calendar events.
                                          					 Used to integrate with any Exchange server in the network configuration. Both
                                          					 ports are created. The kind of messages that are sent depend on the type of
                                          					 Calendar Presence Backend gateway(s) that are configured. |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence (Tomcat) | IM and Presence (SOAP) | TCP | TCP | 5007 | Ephemeral | SOAP
                                          					 monitor port |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence | RTMT | TCP | TCP | 1090 | Ephemeral | AMC RMI
                                          					 Object port. Cisco AMC Service for RTMT performance monitors, data collection,
                                          					 logging, and alerting. |
| IM and Presence | RTMT | TCP | TCP | 1099 | Ephemeral | AMC RMI
                                          					 Registry port. Cisco AMC Service for RTMT performance monitors, data
                                          					 collection, logging, and alerting. |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| XMPP
                                          					 Client | IM and Presence | TCP | TCP | 5222 | Ephemeral | Client
                                          					 access port |
| IM and Presence | IM and Presence | TCP | TCP | 5269 | Ephemeral | Server to
                                          					 Server connection (S2S) port |
| Third-party BOSH client | IM and Presence | TCP | TCP | 5280 | Ephemeral | HTTP
                                          					 listening port used by the XCP Web Connection Manager for BOSH third-party API
                                          					 connections |
| IM and Presence (XCP Services) | IM and Presence (XCP Router | TCP | TCP | 7400 | Ephemeral | XCP Router Master Accept Port. XCP services that connect to the router from an Open Port Configuration (for example XCP Authentication
                                          Component Service) typically connect on this port. |
| IM and Presence (XCP Router | IM and Presence (XCP Router | UDP | UDP | 5353 | Ephemeral | MDNS port.
                                          					 XCP routers in a cluster use this port to discover each other. |
| IM and Presence (XCP Router | IM and Presence (XCP Router | TCP | TCP | 7336 | HTTPS | MFT File transfer (On-Premises only). |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence | PostgreSQL database | TCP | TCP | 5432 1 | Ephemeral | PostgreSQL
                                          					 database listening port |
| IM and Presence | Oracle database | TCP | TCP | 1521 | Ephemeral | Oracle database listening port |
| IM and Presenc | MSSQL database | TCP | TCP | 1433 | Ephemeral | MSSQL database listening port |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence (Server Recovery Manager) | IM and Presence (Server Recovery Manager) | TCP | TCP | 20075 | Ephemeral | The port
                                          					 that Cisco Server Recovery Manager uses to provide admin rpc requests. |
| IM and Presence (Server Recovery Manager) | IM and Presence (Server Recovery Manager) | UDP | UDP | 21999 | Ephemeral | The port
                                          					 that Cisco Server Recovery Manager uses to communicate with its peer. |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence | IM and Presence | Proprietary | TCP | 9003 | Ephemeral | Cisco Presence Datastore
                                          					 dual node subcluster replication. |
| IM and Presence | IM and Presence | Proprietary | TCP | 9004 | Ephemeral | Cisco Login Datastore dual
                                          					 node subcluster replication. |
| IM and Presence | IM and Presence | Proprietary | TCP | 9005 | Ephemeral | Cisco SIP Registration
                                          					 Datastore dual node subcluster replication. |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence | IM and Presence | Proprietary | TCP | 6603 | Ephemeral | Cisco
                                          					 Presence Datastore SQL Queries. |
| IM and Presence | IM and Presence | Proprietary | TCP | 6604 | Ephemeral | Cisco
                                          					 Login Datastore SQL Queries. |
| IM and Presence | IM and Presence | Proprietary | TCP | 6605 | Ephemeral | Cisco SIP
                                          					 Registration Datastore SQL Queries. |
| IM and Presence | IM and Presence | Proprietary | TCP | 6606 | Ephemeral | Cisco
                                          					 Route Datastore SQL Queries. |

| From
                                          					 (Sender) | To
                                          					 (Listener) | Protocol | Transport
                                          					 Protocol | Destination / Listener | Source /
                                          					 Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence | IM and Presence | Proprietary | TCP | 6607 | Ephemeral | Cisco
                                          					 Presence Datastore XML-based change notification. |
| IM and Presence | IM and Presence | Proprietary | TCP | 6608 | Ephemeral | Cisco
                                          					 Login Datastore XML-based change notification. |
| IM and Presence | IM and Presence | Proprietary | TCP | 6609 | Ephemeral | Cisco SIP
                                          					 Registration Datastore XML-based change notification. |
| IM and Presence | IM and Presence | Proprietary | TCP | 6610 | Ephemeral | Cisco
                                          					 Route Datastore XML-based change notification. |

| From (Sender) | To (Listener) | Protocol | Transport Protocol | Destination / Listener | Source / Sender | Remarks |
|---|---|---|---|---|---|---|
| IM and Presence (Intercluster Sync Agent) | IM and Presence (Intercluster Sync Agent) | TCP | TCP | 37239 | Ephemeral | Cisco Intercluster Sync Agent service uses this port to establish a socket connection for handling commands. |

| From (Sender) | To (Listener) | Destination Port | Purpose |
|---|---|---|---|
| Endpoint/IM and Presence | IM and Presence | 7 | Internet Control Message Protocol (ICMP) This protocol number carries echo-related traffic. It does not constitute a port
                                          as indicated in the column heading. |
| IM and Presence | Endpoint/IM and Presence |

| From (Sender) | To (Listener) | Transport Protocol | Destination / Listener | Source / Sender | Remarks |
|---|---|---|---|---|---|
| Cisco Unified Communications Manager | IM and Presence Publisher | TCP | 1500 | Bi-directional | Internal ID port for Database clients. Localhost traffic only. |
| Cisco Unified Communications Manager | IM and Presence Publisher | TCP | 8443 | Bi-directional | Provides access to Web administration. |
| Cisco Unified Communications Manager | IM and Presence Publisher | TCP | 1090 | Bi-directional | AMC RMI Object port. Cisco AMC Service for RTMT performance monitors, data collection, logging, and alerting. |
| Cisco Unified Communications Manager | IM and Presence Publisher | TCP | 2555 | Bi-directional | Bi-directional Real-time Information Services (RIS) database server. Connects to other RISDC services in the cluster to provide
                                          clusterwide real-time information. |
| Cisco Unified Communications Manager | IM and Presence Publisher | TCP | 8500 | Bi-directional | Internal port - cluster manager port used by the ipsec_mgr daemon for cluster replication of platform data (hosts) certificates. |
| Cisco Unified Communications Manager | IM and Presence Publisher | TCP | 8600 | Bi-directional | Config Agent heartbeat port |
| Cisco Unified Communications Manager | IM and Presence Publisher | UDP | 123 | Bi-directional | Network Time Protocol(NTP) used for time synchronization. |
| IM and Presence Publisher | IM and Presence Subscriber | UDP | 50000 | Bi-directional | Internal port. Localhost traffic only. LiveBus messaging port. TheIM and PresenceService uses this port for cluster communication. |
| IM and Presence Publisher | IM and Presence Subscriber | UDP | 21999 | Bi-directional | The port that Cisco Server Recovery Manager uses to communicate with its peer. |
| IM and Presence Publisher | Cisco Unified Communications Manager | TCP | 4040 | Bi-directional | DRF Master Agent server port that accepts connections from Local Agent, GUI, and CLI. |
| IM and Presence Publisher | Cisco Unified Communications Manager | TCP | 8001 | Bi-directional | Used while configuring persistent chat. |
| IM and Presence Publisher | Cisco Unified Communications Manager | TCP | 6379 | Bi-directional | Used while configuring managed file transfer (MFT). |
| IM and Presence Publisher | IM and Presence Subscriber | TCP | 7 | Bi-directional | Used while configuring external database (MSSQL). |
| IM and Presence Publisher | IM and Presence Subscriber | TCP | 20075 | Bi-directional | The port that Cisco Server Recovery Manager uses to provide admin RPC requests. |
| IM and Presence Publisher | IM and Presence Subscriber | TCP | 8600 | Bi-directional | Config Agent heartbeat port |
| IM and Presence Subscriber | IM and Presence Publisher | TCP | 9005 | Bi-directional | Cisco SIP Registration Datastore dual node presence redundancy group replication. |
| IM and Presence Subscriber | IM and Presence Publisher | TCP | 9003 | Bi-directional | Cisco Presence Datastore dual node presence redundancy group replication. |
| IM and Presence Subscriber | IM and Presence Publisher | TCP | 20075 | Bi-directional | The port that Cisco Server Recovery Manager uses to provide admin RPC requests. |
| IM and Presence Subscriber | IM and Presence Publisher | TCP | 9004 | Bi-directional | Cisco Login Datastore dual node presence redundancy group replication. |
| Cisco Unified Communications Manager | IM and Presence Publisher | TCP | 5070 | Bi-directional | Used on a call configuration |
| IM and Presence Publisher | IM and Presence Subscriber | TCP | 44000 | Bi-directional | Used on a call configuration |

| From (Sender) | To (Listener) | Source Port | Destination Port | Protocol | Remarks |
|---|---|---|---|---|---|
| Cisco Unified Communications Manager | IM and Presence Publisher | [37240 – 61000] | 5070 | TCP |  |
| IM and Presence Publisher | XMPP client (Jabber) | 5222 | 64846 | TCP | Client Access Port |
| IM and Presence Publisher | XMPP client (Jabber) | 5222 | 56361 | TCP | Client Access Port |

| From (Sender) | To (Listener) | Source Port | Destination Port | Protocol |
|---|---|---|---|---|
| IM and Presence Publisher | Database | [37240 – 61000] | 7 | TCP |

| From (Sender) | To (Listener) | Source Port | Destination Port | Protocol |
|---|---|---|---|---|
| IM and Presence Publisher | Database | 37240 – 61000 | 1433 | TCP |

| From (Sender) | To (Listener) | Source Port | Destination Port | Protocol |
|---|---|---|---|---|
| IM and Presence Publisher | External File Server | 37240 – 61000 | 7 | TCP |
| IM and Presence Publisher | External File Server | 37240 – 61000 | 22 | TCP |
| IM and Presence Publisher | External File Server | 37240 – 61000 | 5432 | TCP |
| IM and Presence Publisher | Database | 54288 - 54292 | 5432 | TCP |