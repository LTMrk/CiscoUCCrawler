---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-configurati-9986a64b3f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/configuration/guide/ucce_b_1501_port-utilization/ucce_m_1501_contact-center-enterprise.html
retrieved_at: 2026-08-20T18:55:22.888069+00:00
---

Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 15.0(1)

# Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 15.0(1)

Updated: April 30, 2025

Chapter: Port Utilization in Contact Center Enterprise

## Chapter: Port Utilization in Contact Center Enterprise

# Port Utilization in Contact Center Enterprise

## Unified CCE and Packaged CCE Port Utilization

This table includes information for Unified CCE.

Some port definitions use a formula. For example:

In this example, instance 0 uses port 40007, instance 1 uses port 40047, instance 2 uses port 40087, and so on.

In the following table, PG1, PG2, and PG3 are not specific PG numbers or DMP IDs. They are the order in which the PGs get
                                          installed.

This document does not include the Enterprise Chat and Email (ECE) port details. For more information on ECE ports, see the
                                          ECE documentation at: https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/tsd-products-support-series-home.html .

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

Router (side B) (MDS)

Private low:

TCP 41004 + (instance number * 40)

Private medium:

TCP 41016 + (instance number * 40)

Private high:

TCP 41005 + (instance number * 40)

State Xfer for CIC:

TCP 41022 + (instance number * 40)

State Xfer for HLGR:

TCP 41021 + (instance number * 40)

TCP 41032 + (instance number * 40)

State Xfer for RTR:

TCP 41020 + (instance number * 40)

UDP 39500–39999

State Xfer for DBAgent:

TCP 41033 + (instance number * 40)

Router (side A) (MDS)

Bi-directional

Private network at the central controller site

UDP ports are not used, if QoS is enabled on the router private interface.

Router (side B) (MDS)

MDS process port

TCP 41000

MDS process client

Bi-directional

Router (side B) (MDS)

MDS state transfer port

TCP 41001

MDS process client (synchronized)

Bi-directional

Router (side A and B) (DB Worker)

DB Worker process port

UDP 445

DB Worker process client

Bi-directional

ICM PG1 (side A and B) (pgagent)

TCP 43006 + (instance number * 40)

ICM PG1 (Opposite Side: A or B) (pgagent)

Bi-directional

Public network (test-other-side)

ICM PG2 (side A and B) (pgagent)

TCP 45006 + (instance number * 40)

ICM PG2 (Opposite Side: A or B) (pgagent)

Bi-directional

Public network (test-other-side)

ICM PG3 (side A and B) (pgagent)

TCP 47506 + (instance number * 40)

ICM PG3 (Opposite Side: A or B) (pgagent)

Bi-directional

Public network (test-other-side)

ICM PG1 (side A and B) (MDS)

Private low:

TCP 43004 + (instance number * 40)

Private medium:

TCP 43016 + (instance number * 40)

Private high:

TCP 43005 + (instance number * 40)

State Xfer for OPC:

TCP 43023 + (instance number * 40)

UDP 39500–39999

ICM PG1 (Opposite Side: A or B)

Bi-directional

Private network

UDP ports are not used, if QoS is enabled on the ICM PG private interface.

ICM PG2 (side A and B) (MDS)

Private low:

TCP 45004 + (instance number * 40)

Private medium:

TCP 45016 + (instance number * 40)

Private high:

TCP 45005 + (instance number * 40)

State Xfer for OPC:

TCP 45023 + (instance number * 40)

UDP 39500–39999

ICM PG2 (Opposite Side: A or B)

Bi-directional

Private network

UDP ports are not used if QoS is enabled on the ICM PG private interface.

ICM PG3 (side A and B) (MDS)

Private low:

TCP 47504 + (instance number * 40)

Private medium:

TCP 47516 + (instance number * 40)

Private high:

TCP 47505 + (instance number * 40)

State Xfer for OPC:

TCP 47523 + (instance number * 40)

UDP 39500–39999

ICM PG3 (Opposite Side: A or B)

Bi-directional

Private network

UDP ports are not used if QoS is enabled on the ICM PG private interface.

ICM PG1 (side B) (MDS)

MDS process port

TCP 43000

MDS process client

Bi-directional

ICM PG1 (side B) (MDS)

MDS state transfer port

TCP 43001

MDS process client (synchronized)

Bi-directional

ICM PG2 (side B) (MDS)

MDS process port

TCP 45000

MDS process client

Bi-directional

ICM PG2 (side B) (MDS)

MDS state transfer port

TCP 45001

MDS process client (synchronized)

Bi-directional

ICM PG3 (side B) (MDS)

MDS process port

TCP 47500

MDS process client

Bi-directional

ICM PG3 (side B) (MDS)

MDS state transfer port

TCP 47501

MDS process client (synchronized)

Bi-directional

Router (side A) (MDS)

Private low:

TCP 41004 + (instance number * 40)

Private medium:

TCP 41016 + (instance number * 40)

Private high:

TCP 41005 + (instance number * 40)

State Xfer for CIC:

TCP 41022 + (instance number * 40)

State Xfer for HLGR:

TCP 41021 + (instance number * 40)

TCP 41032 + (instance number * 40)

State Xfer for RTR:

TCP 41020 + (instance number * 40)

UDP 39500–39999

State Xfer for DBAgent:

TCP 41033 + (instance number * 40)

Router (side B) (MDS)

Bi-directional

Private network at the central controller site

UDP ports are not used if QoS is enabled on the router private interface.

Router (side A) (MDS)

MDS process port

TCP 40000

MDS process client

Bi-directional

Router (side A) (MDS)

MDS state transfer port

TCP 40001

MDS process client (synchronized)

Bi-directional

ICM PG1 (side A) (MDS)

MDS process port

TCP 42000

MDS process client

Bi-directional

ICM PG1 (side A) (MDS)

MDS state transfer port

TCP 42001

MDS process client (synchronized)

Bi-directional

ICM PG2 (side A) (MDS)

MDS process port

TCP 44000

MDS process client

Bi-directional

ICM PG2 (side A) (MDS)

MDS state transfer port

TCP 44001

MDS process client (synchronized)

Bi-directional

ICM PG3 (side A) (MDS)

MDS process port

TCP 46000

MDS process client

Bi-directional

ICM PG3 (side A) (MDS)

MDS state transfer port

TCP 46001

MDS process client (synchronized)

Bi-directional

Router (side A) DMP (ccagent)

Secure mode enabled

Public low:

TCP 40014 + (instance number * 40)

Public medium:

TCP 40018 + (instance number * 40)

Public high:

TCP 40011 + (instance number * 40)

UDP 39500–39999

Secure mode disabled

Public low:

TCP 40002 + (instance number * 40)

Public medium:

TCP 40017 + (instance number * 40)

Public high:

TCP 40003 + (instance number * 40)

UDP 39500–39999

ICM PG (pgagent)

Bi-directional

Public network connecting the PG to the central controller

Router to pre-5.0 PG communication.

UDP ports are not used if QoS is enabled on the ICM PG private interface.

Router (side B) DMP (ccagent)

Secure mode enabled

Public low:

TCP 41014 + (Instance Number * 40)

Public medium:

TCP 41018 + (instance number * 40)

Public high:

TCP 41011 + (instance number * 40)

UDP 39500–39999

Secure mode disabled

Public low:

TCP 41002 + (Instance Number * 40)

Public medium:

TCP 41017 + (instance number * 40)

Public high:

TCP 41003 + (instance number * 40)

UDP 39500–39999

ICM PG (pgagent)

Bi-directional

Public network connecting the PG to the central controller

Router to pre-5.0 PG communication.

UDP ports are not used if QoS is enabled on the ICM PG private interface.

Router A (rtfeed)

Secure mode enabled

TCP 40037 + (instance number * 40)

Secure mode disabled

TCP 40007 + (instance number * 40)

Administration & Data Server

Bi-directional

Real-time feed

Router B (rtfeed)

Secure mode enabled

TCP 41037 + (instance number * 40)

Secure mode disabled

TCP 41007 + (instance number * 40)

Administration & Data Server

Bi-directional

Real-time feed

Router A (DB Agent)

TCP 40019 + (instance number * 40)

Administration & Data Server

Bi-directional

Secure EMT port to DB Agent

Router B (DB Agent)

TCP 41019 + (instance number * 40)

Administration & Data Server

Bi-directional

Secure EMT port to DB Agent

Router A (DB Agent)

TCP 40019 + (instance number * 40)

Administration client

Bi-directional

Secure EMT port to DB Agent

Router B (DB Agent)

TCP 41019 + (instance number * 40)

Administration client

Bi-directional

Secure EMT port to DB Agent

Logger (side A)

Secure mode enabled

TCP 40023 + (instance number * 40)

TCP 40038 + (instance number * 40)

Secure mode disabled

TCP 40026 + (instance number * 40)

TCP 40028 + (instance number * 40)

Administration & Data Server Historical Data Server (HDS)

Bi-directional

Replication

Logger (side A)

Secure mode enabled

TCP 40039 + (instance number * 40)

Secure mode disabled

TCP 40032 + (instance number * 40)

Dialer and Import

Bi-directional

Campaign Manager EMT port to Dialer

Logger (side B)

Secure mode enabled

TCP 41023 + (instance number * 40)

TCP 41038 + (instance number * 40)

Secure mode disabled

TCP 41026 + (instance number * 40)

TCP 41028 + (instance number * 40)

Administration & Data Server Historical Data Server (HDS)

Bi-directional

Replication

Logger (side B)

Secure mode enabled

TCP 41039 + (instance number * 40)

Secure mode disabled

TCP 41036 + (instance number * 40)

Dialer and Import

Bi-directional

Campaign Manager EMT port to Dialer

Logger (side A)

TCP 40024 + (instance number * 40)

Logger (side B)

Bi-directional

Secure Campaign Manager EMT port to other side of Campaign Manager

Logger (side B)

TCP 41024 + (instance number * 40)

Logger (side A)

Bi-directional

Secure Campaign Manager EMT port to other side of Campaign Manager

Primary Administration & Data Server (rtfeed)

TCP 48008 + (instance number * 40)

Administration client

Bi-directional

Real-time feed

Secondary Administration & Data Server (rtfeed)

TCP 49008 + (instance number * 40)

Administration client

Bi-directional

Real-time feed

Primary Administration & Data Server (rtfeed)

TCP 48007 + (instance number * 40)

Administration client

Bi-directional

RTD to RTC secure port

Secondary Administration & Data Server (rtfeed)

TCP 48007 + (instance number * 40)

Administration client

Bi-directional

RTD to RTC secure port

Administration & Data Server

TCP 48010 + (instance number * 40)

Administration client

Bi-directional

Secure EMT port to Update AW

Contact Sharing

TCP 61616

Active MQ for Live Data

TCP 61616

Bidirectional

Server ICM Router (side A)

UDP 40025 + (instance number * 40)

Client ICM Router

Bi-directional

Public network connecting the Client ICM Router to the Server ICM Router

Server ICM Router (side B)

UDP 41025 + (instance number * 40)

Client ICM Router

Bi-directional

Public network connecting the Client ICM Router to the Server ICM Router

CSFS

TCP 40015

CSFS duplexed peer

Bi-directional

CSFS event synchronization link

Logger Recovery Process (side A)

41013 + (instance number *40)

Bi-directional

Logger Recovery Process (side B)

40013 + (instance number *40)

Bi-directional

Diagnostic framework

TCP 7890

Any client that is requesting information from the diagnostic service.

Bi-directional

This serviceability component is installed on major CCE component servers (e.g. router, logger, PG, and Administration and
                                          Data Servers)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

MSSQL

TCP 1433(Default)

Logger

Distributor

Bi-directional

Ensure the chosen custom SQL Server port does not overlap with the reserved ports used by CCE services as defined in this
                                          document.

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

Dialer

58800 + instNum

Voice Gateway

UDP 58800

Bi-directional

Set in the SIPDialerPortBaseNumber registry key.

RTP for SIP

UDP ports in a range based on these formulas:

RangeStart = RTPPortRangeStart + ( instNum * 2000)

RangeEnd = RangeStart + 2000

You can set RTPPortRangeStart in the registry key: RTPPortRangeStart .

Voice gateway

Bi-directional

Receive ports for reservation calls.

Use the following registry key to select and configure UDP ports: RTPPortRangeStart

MR PG

TCP 38001+ (instance number)

Dialer

Bi-directional

The MR PG connects to the SIP Dialer using this port.

Dialer (SIP)

5060 and "SIPDialerPortBaseNumber + instance number"

Voice Gateway or SIP Proxy

Bi-directional

Set in the SIPServerPortNumber registry key.

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

GED-188 (CTI Server) unsecured

Side A

TCP 42027 + (instance number * 40)

Side B

TCP 43027 + (instance number * 40)

Finesse

Cisco Outbound Dialer

ARM Interface

Bi-directional

GED-188 (CTI Server) secured

Side A

TCP 42030 + (instance number * 40)

Side B

TCP 43030 + (instance number * 40)

Finesse

Cisco Outbound Dialer

ARM Interface

Bi-directional

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

IP Process Communications

CTI/QBE

TCP 2748

Bi-directional

JTAPI

Customer Voice Portal — Call Server

Cisco Unified IP-IVR

PG, VRU PIM (GED-125)

TCP 5000–5001

Bi-directional

Unified CCE /IVR message interface, VRU PIM

CCE PG

TCP 2789

Unified CM

Bi-directional

JTAPI application server

Media Routing process

MR PIM

TCP 38001

Bi-directional

For port utilization information about Network Interface Controllers (NICs), refer to the TCP/IP-based NIC System Management
                                          Guide Supplements and setup parameters of the NIC or SCP connections.

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

RPC

TCP 135

UDP 135

Bi-directional

NetBIOS Session

TCP 139

Bi-directional

NetBIOS Name Resolution

TCP 137

UDP 137

Bi-directional

NetBIOS Netlogon/ Browsing

UDP 138

Bi-directional

SMB

TCP 445

UDP 445 1

Bi-directional

LDAP

TCP 389

UDP 389

Bi-directional

LDAP SSL

TCP 636

Bi-directional

LDAP GC

TCP 3268

Bi-directional

LDAP GC SSL

TCP 3269

Bi-directional

Active Directory Web Services

TCP 9389

UDP 9389

Bi-directional

Powershell uses this port.

DNS

TCP 53

UDP 53

Bi-directional

Kerberos

TCP 88

UDP 88

Bi-directional

For more information on Windows authentication, see Service overview and network port requirements for the Windows in Microsoft
                                          documentation.

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

SNMP–Trap

UDP 162

Bi-directional

Syslog

UDP 514

Bi-directional

Telnet

TCP 23

Bi-directional

RDP (Terminal Services)

TCP 3389

Bi-directional

pcAnywhere

TCP 5631

UDP 5632

Bi-directional

VNC

TCP 5900

TCP 5800 (Java HTTP)

Bi-directional

RealVNC

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Protocol and Port

Traffic Direction

Notes

Router (side A and B) (TIP Event)

Router A: 40034 + (instance number * 40)

Router B: 41034 + (instance number * 40)

CUIC/Live Data

Bi-directional

Public network Live Data Events.

Router (side A and B) (TIP TOS)

Router A: 40035 + (instance number * 40)

Router B: 41035 + (instance number * 40)

CUIC/Live Data

Bi-directional

Public network Live Data Test Other Side.

ICM PG1 (side A and B) (TIP Event) 2

Side A: 42034 + (instance number * 40)

Side B: 43034 + (instance number * 40)

CUIC/Live Data

Bi-directional

Public network Live Data Events.

ICM PG2 (side A and B) (TIP Event)

Side A: 44034 + (instance number * 40)

Side B: 45034 + (instance number * 40)

CUIC/Live Data

Bi-directional

Public network Live Data Events.

ICM PG1 (side A and B) (TIP TOS)

Side A: 42035 + (instance number * 40)

Side B: 43035 + (instance number * 40)

CUIC/Live Data

Bi-directional

Public network Live Data Test Other Side.

ICM PG2 (side A and B) (TIP TOS)

Side A: 44035 + (instance number * 40)

Side B: 45035 + (instance number * 40)

CUIC/Live Data

Bi-directional

Public network Live Data Test Other Side.

Protocol and Port

Remote Device

Remote Port

Traffic Direction

Notes

—

Following URLs must be included in the allowed list of network:

*.wbx2.com

*.ciscoccservice.com

## Unified CCMP Port Utilization

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

CCMP Web/Application server A/B

LDAP (Domain Controller)

UDP 389

TCP 389

Integrated Configuration Environment (ICE)

Used to read AD account information for supervisor provisioning

CCMP Database server A/B

SQL

TCP 1433(Default)

CCMP DB server A/B

Standard SQL Connection and for SQL replication

TCP 1433(Default)

CCE /CCH Administration and Data server side A/B

For import of CCE /CCH dimension data

*MSDTC

TCP 135

CCMP DB sever A/B

TCP 1024-5000

For the CCMP audit archive job

SMB over IP (CVP Media Server)

UDP 445*

TCP 445

Integrated Configuration Environment

For CVP file upload file replication

* Also used for named pipes connectivity.

These assume the Server Name field in ICE is configured with either a TCP/IP address or DNS name (hence no NETBIOS port requirements).

Ports are also required to access all Unified Contact Center Management Portal servers for support reasons (either pcAnywhere
                              or terminal services).

This list does not include standard Windows ports such as DNS and Kerberos.

* MSDTC response ports by default use a dynamically allocated port in the range of 1024 to 5000. You can configure this range
                              creating the HKEY_LOCAL_MACHINE\Software\Microsoft\Rpc\Internet location registry key and adding the following registry values:

Ports (REG_MULTI_SZ) - specify one port range per line, for example, 3000-3005

PortsInternetAvailable (REG_SZ) - always set this value to "Y" (do not include the quotes)

UseInternetPorts (REG_SZ) - always set this value to "Y" (do not include the quotes)

## Unified CRM Connectors Port Utilization

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Protocol and Port

Traffic Direction

Notes

CRM DataStore for SAP

TCP 42029

CRM Connector for SAP

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Protocol and Port

Traffic Direction

Notes

MSCRM Server

TCP 81

MSCRM Client

MSCRM only.

CRM Connector Server

TCP 5666

CRM Adapters

Configurable in \Program Files\Cisco\CRM Connector\MCIS\Config.ini

.NET Adapter

TCP 5558

Agent Desktop

Remoting Port.

CRM Connector Server

TCP 42027

Cisco CTI Server

Default port for side A. Configurable in the Config.ini file [CTIModule Setting] Port_A.

CRM Connector Server

TCP 44027

Cisco CTI Server

Default port for side B. Configurable in the Config.ini file [CTIModule Setting] Port_B.

CRM Connector Server

TCP 65372

Server Administration Tool

Configurable under \Program Files\Cisco\CRM Connector\MCIS\Config.ini and \Program Files\Cisco\CRM Connector\ Server Administration
                                          Tool\WebComponent\ server.config

### Customers Also Viewed

- Configure Webex AI Agent for CCE

| Note | In the following table, PG1, PG2, and PG3 are not specific PG numbers or DMP IDs. They are the order in which the PGs get
                                          installed. |
|---|---|

| Note | This document does not include the Enterprise Chat and Email (ECE) port details. For more information on ECE ports, see the
                                          ECE documentation at: https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/tsd-products-support-series-home.html . |
|---|---|

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| Router (side B) (MDS) | Private low: TCP 41004 + (instance number * 40) Private medium: TCP 41016 + (instance number * 40) Private high: TCP 41005 + (instance number * 40) State Xfer for CIC: TCP 41022 + (instance number * 40) State Xfer for HLGR: TCP 41021 + (instance number * 40) TCP 41032 + (instance number * 40) State Xfer for RTR: TCP 41020 + (instance number * 40) UDP 39500–39999 State Xfer for DBAgent: TCP 41033 + (instance number * 40) | Router (side A) (MDS) |  | Bi-directional | Private network at the central controller site Note UDP ports are not used, if QoS is enabled on the router private interface. | Note | UDP ports are not used, if QoS is enabled on the router private interface. |
| Note | UDP ports are not used, if QoS is enabled on the router private interface. |
| Router (side B) (MDS) | MDS process port TCP 41000 | MDS process client |  | Bi-directional |  |
| Router (side B) (MDS) | MDS state transfer port TCP 41001 | MDS process client (synchronized) |  | Bi-directional |  |
| Router (side A and B) (DB Worker) | DB Worker process port UDP 445 | DB Worker process client |  | Bi-directional |  |
| ICM PG1 (side A and B) (pgagent) | TCP 43006 + (instance number * 40) | ICM PG1 (Opposite Side: A or B) (pgagent) |  | Bi-directional | Public network (test-other-side) |
| ICM PG2 (side A and B) (pgagent) | TCP 45006 + (instance number * 40) | ICM PG2 (Opposite Side: A or B) (pgagent) |  | Bi-directional | Public network (test-other-side) |
| ICM PG3 (side A and B) (pgagent) | TCP 47506 + (instance number * 40) | ICM PG3 (Opposite Side: A or B) (pgagent) |  | Bi-directional | Public network (test-other-side) |
| ICM PG1 (side A and B) (MDS) | Private low: TCP 43004 + (instance number * 40) Private medium: TCP 43016 + (instance number * 40) Private high: TCP 43005 + (instance number * 40) State Xfer for OPC: TCP 43023 + (instance number * 40) UDP 39500–39999 | ICM PG1 (Opposite Side: A or B) |  | Bi-directional | Private network Note UDP ports are not used, if QoS is enabled on the ICM PG private interface. | Note | UDP ports are not used, if QoS is enabled on the ICM PG private interface. |
| Note | UDP ports are not used, if QoS is enabled on the ICM PG private interface. |
| ICM PG2 (side A and B) (MDS) | Private low: TCP 45004 + (instance number * 40) Private medium: TCP 45016 + (instance number * 40) Private high: TCP 45005 + (instance number * 40) State Xfer for OPC: TCP 45023 + (instance number * 40) UDP 39500–39999 | ICM PG2 (Opposite Side: A or B) |  | Bi-directional | Private network Note UDP ports are not used if QoS is enabled on the ICM PG private interface. | Note | UDP ports are not used if QoS is enabled on the ICM PG private interface. |
| Note | UDP ports are not used if QoS is enabled on the ICM PG private interface. |
| ICM PG3 (side A and B) (MDS) | Private low: TCP 47504 + (instance number * 40) Private medium: TCP 47516 + (instance number * 40) Private high: TCP 47505 + (instance number * 40) State Xfer for OPC: TCP 47523 + (instance number * 40) UDP 39500–39999 | ICM PG3 (Opposite Side: A or B) |  | Bi-directional | Private network Note UDP ports are not used if QoS is enabled on the ICM PG private interface. | Note | UDP ports are not used if QoS is enabled on the ICM PG private interface. |
| Note | UDP ports are not used if QoS is enabled on the ICM PG private interface. |
| ICM PG1 (side B) (MDS) | MDS process port TCP 43000 | MDS process client |  | Bi-directional |  |
| ICM PG1 (side B) (MDS) | MDS state transfer port TCP 43001 | MDS process client (synchronized) |  | Bi-directional |  |
| ICM PG2 (side B) (MDS) | MDS process port TCP 45000 | MDS process client |  | Bi-directional |  |
| ICM PG2 (side B) (MDS) | MDS state transfer port TCP 45001 | MDS process client (synchronized) |  | Bi-directional |  |
| ICM PG3 (side B) (MDS) | MDS process port TCP 47500 | MDS process client |  | Bi-directional |  |
| ICM PG3 (side B) (MDS) | MDS state transfer port TCP 47501 | MDS process client (synchronized) |  | Bi-directional |  |
| Router (side A) (MDS) | Private low: TCP 41004 + (instance number * 40) Private medium: TCP 41016 + (instance number * 40) Private high: TCP 41005 + (instance number * 40) State Xfer for CIC: TCP 41022 + (instance number * 40) State Xfer for HLGR: TCP 41021 + (instance number * 40) TCP 41032 + (instance number * 40) State Xfer for RTR: TCP 41020 + (instance number * 40) UDP 39500–39999 State Xfer for DBAgent: TCP 41033 + (instance number * 40) | Router (side B) (MDS) |  | Bi-directional | Private network at the central controller site Note UDP ports are not used if QoS is enabled on the router private interface. | Note | UDP ports are not used if QoS is enabled on the router private interface. |
| Note | UDP ports are not used if QoS is enabled on the router private interface. |
| Router (side A) (MDS) | MDS process port TCP 40000 | MDS process client |  | Bi-directional |  |
| Router (side A) (MDS) | MDS state transfer port TCP 40001 | MDS process client (synchronized) |  | Bi-directional |  |
| ICM PG1 (side A) (MDS) | MDS process port TCP 42000 | MDS process client |  | Bi-directional |  |
| ICM PG1 (side A) (MDS) | MDS state transfer port TCP 42001 | MDS process client (synchronized) |  | Bi-directional |  |
| ICM PG2 (side A) (MDS) | MDS process port TCP 44000 | MDS process client |  | Bi-directional |  |
| ICM PG2 (side A) (MDS) | MDS state transfer port TCP 44001 | MDS process client (synchronized) |  | Bi-directional |  |
| ICM PG3 (side A) (MDS) | MDS process port TCP 46000 | MDS process client |  | Bi-directional |  |
| ICM PG3 (side A) (MDS) | MDS state transfer port TCP 46001 | MDS process client (synchronized) |  | Bi-directional |  |
| Router (side A) DMP (ccagent) | Secure mode enabled Public low: TCP 40014 + (instance number * 40) Public medium: TCP 40018 + (instance number * 40) Public high: TCP 40011 + (instance number * 40) UDP 39500–39999 Secure mode disabled Public low: TCP 40002 + (instance number * 40) Public medium: TCP 40017 + (instance number * 40) Public high: TCP 40003 + (instance number * 40) UDP 39500–39999 | ICM PG (pgagent) |  | Bi-directional | Public network connecting the PG to the central controller Router to pre-5.0 PG communication. Note UDP ports are not used if QoS is enabled on the ICM PG private interface. | Note | UDP ports are not used if QoS is enabled on the ICM PG private interface. |
| Note | UDP ports are not used if QoS is enabled on the ICM PG private interface. |
| Router (side B) DMP (ccagent) | Secure mode enabled Public low: TCP 41014 + (Instance Number * 40) (instance number Public medium: TCP 41018 + (instance number * 40) Public high: TCP 41011 + (instance number * 40) UDP 39500–39999 Secure mode disabled Public low: TCP 41002 + (Instance Number * 40) (instance number Public medium: TCP 41017 + (instance number * 40) Public high: TCP 41003 + (instance number * 40) UDP 39500–39999 | ICM PG (pgagent) |  | Bi-directional | Public network connecting the PG to the central controller Router to pre-5.0 PG communication. Note UDP ports are not used if QoS is enabled on the ICM PG private interface. | Note | UDP ports are not used if QoS is enabled on the ICM PG private interface. |
| Note | UDP ports are not used if QoS is enabled on the ICM PG private interface. |
| Router A (rtfeed) | Secure mode enabled TCP 40037 + (instance number * 40) Secure mode disabled TCP 40007 + (instance number * 40) | Administration & Data Server |  | Bi-directional | Real-time feed |
| Router B (rtfeed) | Secure mode enabled TCP 41037 + (instance number * 40) Secure mode disabled TCP 41007 + (instance number * 40) | Administration & Data Server |  | Bi-directional | Real-time feed |
| Router A (DB Agent) | TCP 40019 + (instance number * 40) | Administration & Data Server |  | Bi-directional | Secure EMT port to DB Agent |
| Router B (DB Agent) | TCP 41019 + (instance number * 40) | Administration & Data Server |  | Bi-directional | Secure EMT port to DB Agent |
| Router A (DB Agent) | TCP 40019 + (instance number * 40) | Administration client |  | Bi-directional | Secure EMT port to DB Agent |
| Router B (DB Agent) | TCP 41019 + (instance number * 40) | Administration client |  | Bi-directional | Secure EMT port to DB Agent |
| Logger (side A) | Secure mode enabled TCP 40023 + (instance number * 40) TCP 40038 + (instance number * 40) Secure mode disabled TCP 40026 + (instance number * 40) TCP 40028 + (instance number * 40) | Administration & Data Server Historical Data Server (HDS) |  | Bi-directional | Replication |
| Logger (side A) | Secure mode enabled TCP 40039 + (instance number * 40) Secure mode disabled TCP 40032 + (instance number * 40) | Dialer and Import |  | Bi-directional | Campaign Manager EMT port to Dialer |
| Logger (side B) | Secure mode enabled TCP 41023 + (instance number * 40) TCP 41038 + (instance number * 40) Secure mode disabled TCP 41026 + (instance number * 40) TCP 41028 + (instance number * 40) | Administration & Data Server Historical Data Server (HDS) |  | Bi-directional | Replication |
| Logger (side B) | Secure mode enabled TCP 41039 + (instance number * 40) Secure mode disabled TCP 41036 + (instance number * 40) | Dialer and Import |  | Bi-directional | Campaign Manager EMT port to Dialer |
| Logger (side A) | TCP 40024 + (instance number * 40) | Logger (side B) |  | Bi-directional | Secure Campaign Manager EMT port to other side of Campaign Manager |
| Logger (side B) | TCP 41024 + (instance number * 40) | Logger (side A) |  | Bi-directional | Secure Campaign Manager EMT port to other side of Campaign Manager |
| Primary Administration & Data Server (rtfeed) | TCP 48008 + (instance number * 40) | Administration client |  | Bi-directional | Real-time feed |
| Secondary Administration & Data Server (rtfeed) | TCP 49008 + (instance number * 40) | Administration client |  | Bi-directional | Real-time feed |
| Primary Administration & Data Server (rtfeed) | TCP 48007 + (instance number * 40) | Administration client |  | Bi-directional | RTD to RTC secure port |
| Secondary Administration & Data Server (rtfeed) | TCP 48007 + (instance number * 40) | Administration client |  | Bi-directional | RTD to RTC secure port |
| Administration & Data Server | TCP 48010 + (instance number * 40) | Administration client |  | Bi-directional | Secure EMT port to Update AW |
| Contact Sharing | TCP 61616 | Active MQ for Live Data | TCP 61616 | Bidirectional |  |
| Server ICM Router (side A) | UDP 40025 + (instance number * 40) | Client ICM Router |  | Bi-directional | Public network connecting the Client ICM Router to the Server ICM Router |
| Server ICM Router (side B) | UDP 41025 + (instance number * 40) | Client ICM Router |  | Bi-directional | Public network connecting the Client ICM Router to the Server ICM Router |
| CSFS | TCP 40015 | CSFS duplexed peer |  | Bi-directional | CSFS event synchronization link |
| Logger Recovery Process (side A) | 41013 + (instance number *40) |  |  | Bi-directional |  |
| Logger Recovery Process (side B) | 40013 + (instance number *40) |  |  | Bi-directional |  |
| Diagnostic framework | TCP 7890 | Any client that is requesting information from the diagnostic service. |  | Bi-directional | This serviceability component is installed on major CCE component servers (e.g. router, logger, PG, and Administration and
                                          Data Servers) |

| Note | UDP ports are not used, if QoS is enabled on the router private interface. |
|---|---|

| Note | UDP ports are not used, if QoS is enabled on the ICM PG private interface. |
|---|---|

| Note | UDP ports are not used if QoS is enabled on the ICM PG private interface. |
|---|---|

| Note | UDP ports are not used if QoS is enabled on the ICM PG private interface. |
|---|---|

| Note | UDP ports are not used if QoS is enabled on the router private interface. |
|---|---|

| Note | UDP ports are not used if QoS is enabled on the ICM PG private interface. |
|---|---|

| Note | UDP ports are not used if QoS is enabled on the ICM PG private interface. |
|---|---|

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| MSSQL | TCP 1433(Default) | Logger Distributor |  | Bi-directional | Ensure the chosen custom SQL Server port does not overlap with the reserved ports used by CCE services as defined in this
                                          document. |

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| Dialer | 58800 + instNum instNum is the instance number for the Dialer. | Voice Gateway | UDP 58800 | Bi-directional | Set in the SIPDialerPortBaseNumber registry key. |
| RTP for SIP | UDP ports in a range based on these formulas: RangeStart = RTPPortRangeStart + ( instNum * 2000) RangeEnd = RangeStart + 2000 You can set RTPPortRangeStart in the registry key: RTPPortRangeStart . | Voice gateway |  | Bi-directional | Receive ports for reservation calls. Use the following registry key to select and configure UDP ports: RTPPortRangeStart |
| MR PG | TCP 38001+ (instance number) | Dialer |  | Bi-directional | The MR PG connects to the SIP Dialer using this port. |
| Dialer (SIP) | 5060 and "SIPDialerPortBaseNumber + instance number" | Voice Gateway or SIP Proxy |  | Bi-directional | Set in the SIPServerPortNumber registry key. |

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| GED-188 (CTI Server) unsecured | Side A TCP 42027 + (instance number * 40) Side B TCP 43027 + (instance number * 40) | Finesse Cisco Outbound Dialer ARM Interface |  | Bi-directional |  |
| GED-188 (CTI Server) secured | Side A TCP 42030 + (instance number * 40) Side B TCP 43030 + (instance number * 40) | Finesse Cisco Outbound Dialer ARM Interface |  | Bi-directional |  |

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| IP Process Communications |
| CTI/QBE |  |  | TCP 2748 | Bi-directional | JTAPI |
| Customer Voice Portal — Call Server Cisco Unified IP-IVR |  | PG, VRU PIM (GED-125) | TCP 5000–5001 | Bi-directional | Unified CCE /IVR message interface, VRU PIM |
| CCE PG | TCP 2789 | Unified CM |  | Bi-directional | JTAPI application server |
| Media Routing process |  | MR PIM | TCP 38001 | Bi-directional |  |

| Note | For port utilization information about Network Interface Controllers (NICs), refer to the TCP/IP-based NIC System Management
                                          Guide Supplements and setup parameters of the NIC or SCP connections. |
|---|---|

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| RPC | TCP 135 UDP 135 |  |  | Bi-directional |  |
| NetBIOS Session | TCP 139 |  |  | Bi-directional |  |
| NetBIOS Name Resolution | TCP 137 UDP 137 |  |  | Bi-directional |  |
| NetBIOS Netlogon/ Browsing | UDP 138 |  |  | Bi-directional |  |
| SMB | TCP 445 UDP 445 1 |  |  | Bi-directional |  |
| LDAP | TCP 389 UDP 389 |  |  | Bi-directional |  |
| LDAP SSL | TCP 636 |  |  | Bi-directional |  |
| LDAP GC | TCP 3268 |  |  | Bi-directional |  |
| LDAP GC SSL | TCP 3269 |  |  | Bi-directional |  |
| Active Directory Web Services | TCP 9389 UDP 9389 |  |  | Bi-directional | Powershell uses this port. |
| DNS | TCP 53 UDP 53 |  |  | Bi-directional |  |
| Kerberos | TCP 88 UDP 88 |  |  | Bi-directional |  |

| Note | For more information on Windows authentication, see Service overview and network port requirements for the Windows in Microsoft
                                          documentation. |
|---|---|

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| SNMP–Trap | UDP 162 |  |  | Bi-directional |  |
| Syslog | UDP 514 |  |  | Bi-directional |  |
| Telnet | TCP 23 |  |  | Bi-directional |  |
| RDP (Terminal Services) | TCP 3389 |  |  | Bi-directional |  |
| pcAnywhere | TCP 5631 UDP 5632 |  |  | Bi-directional |  |
| VNC | TCP 5900 TCP 5800 (Java HTTP) |  |  | Bi-directional | RealVNC |

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Protocol and Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| Router (side A and B) (TIP Event) | Router A: 40034 + (instance number * 40) Router B: 41034 + (instance number * 40) | CUIC/Live Data |  | Bi-directional | Public network Live Data Events. |
| Router (side A and B) (TIP TOS) | Router A: 40035 + (instance number * 40) Router B: 41035 + (instance number * 40) | CUIC/Live Data |  | Bi-directional | Public network Live Data Test Other Side. |
| ICM PG1 (side A and B) (TIP Event) 2 | Side A: 42034 + (instance number * 40) Side B: 43034 + (instance number * 40) | CUIC/Live Data |  | Bi-directional | Public network Live Data Events. |
| ICM PG2 (side A and B) (TIP Event) | Side A: 44034 + (instance number * 40) Side B: 45034 + (instance number * 40) | CUIC/Live Data |  | Bi-directional | Public network Live Data Events. |
| ICM PG1 (side A and B) (TIP TOS) | Side A: 42035 + (instance number * 40) Side B: 43035 + (instance number * 40) | CUIC/Live Data |  | Bi-directional | Public network Live Data Test Other Side. |
| ICM PG2 (side A and B) (TIP TOS) | Side A: 44035 + (instance number * 40) Side B: 45035 + (instance number * 40) | CUIC/Live Data |  | Bi-directional | Public network Live Data Test Other Side. |

| Process or Application Protocol | Protocol and Port | Remote Device | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| AW Tomcat | — | Hybrid Services on cloud | 443 | Bi-directional | Following URLs must be included in the allowed list of network: *.wbx2.com *.ciscoccservice.com |

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| CCMP Web/Application server A/B |
| LDAP (Domain Controller) | UDP 389 TCP 389 | Integrated Configuration Environment (ICE) |  |  | Used to read AD account information for supervisor provisioning |
| CCMP Database server A/B |
| SQL | TCP 1433(Default) | CCMP DB server A/B |  |  | Standard SQL Connection and for SQL replication |
| TCP 1433(Default) | CCE /CCH Administration and Data server side A/B |  |  | For import of CCE /CCH dimension data |
| *MSDTC | TCP 135 | CCMP DB sever A/B | TCP 1024-5000 |  | For the CCMP audit archive job |
| SMB over IP (CVP Media Server) | UDP 445* TCP 445 | Integrated Configuration Environment |  |  | For CVP file upload file replication |
| * Also used for named pipes connectivity. |

| Note | This list does not include standard Windows ports such as DNS and Kerberos. |
|---|---|

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Protocol and Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| CRM DataStore for SAP | TCP 42029 | CRM Connector for SAP |  |  |  |

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Protocol and Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| MSCRM Server | TCP 81 | MSCRM Client |  |  | MSCRM only. |
| CRM Connector Server | TCP 5666 | CRM Adapters |  |  | Configurable in \Program Files\Cisco\CRM Connector\MCIS\Config.ini |
| .NET Adapter | TCP 5558 | Agent Desktop |  |  | Remoting Port. |
| CRM Connector Server | TCP 42027 | Cisco CTI Server |  |  | Default port for side A. Configurable in the Config.ini file [CTIModule Setting] Port_A. |
| CRM Connector Server | TCP 44027 | Cisco CTI Server |  |  | Default port for side B. Configurable in the Config.ini file [CTIModule Setting] Port_B. |
| CRM Connector Server | TCP 65372 | Server Administration Tool |  |  | Configurable under \Program Files\Cisco\CRM Connector\MCIS\Config.ini and \Program Files\Cisco\CRM Connector\ Server Administration
                                          Tool\WebComponent\ server.config |