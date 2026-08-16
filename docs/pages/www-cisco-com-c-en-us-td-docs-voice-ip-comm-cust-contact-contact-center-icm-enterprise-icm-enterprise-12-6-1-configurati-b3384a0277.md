---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-configurati-b3384a0277
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/configuration/guide/ucce_b_port_utilization_12_6_1/ucce_b_port-utilization_12_5_chapter_0110.html
retrieved_at: 2026-08-16T14:43:32.803969+00:00
---

Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.6(1)

# Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.6(1)

Updated: May 14, 2021

Chapter: Port Utilization in CVP

## Chapter: Port Utilization in CVP

- Port Utilization in CVP

- Unified CVP Port Utilization

# Port Utilization in CVP

## Unified CVP Port Utilization

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

TCP

2000-2002

Bi-directional

Call Manager and gateway interface communication

Call Server JMX

2098

JConsole

Random

Bi-directional

JMX access by JConsole into Call Server

Call Server JMX RMI port

2097

JConsole

Random

Bi-directional

JMX access by JConsole into Call Server

WSM JMX

TCP 10002

JConsole

Random

Bi-directional

JMX access by JConsole into WSM

WSM JMX RMI

TCP 10003

JConsole

Random

Bi-directional

JMX access by JConsole into WSM

OAMP JMX

TCP 10001

JConsole

Random

Bi-directional

JMX access by JConsole into OAMP

OAMP JMX RMI

TCP 10000

JConsole

Random

Bi-directional

JMX access by JConsole into OAMP

CVP Messaging Layer

TCP 23000 - 28000 (First available)

CVP Subsystem

Bi-directional

CVP Message Bus communications

7960-CUVA Video

UDP 5445

7960-CUVA

Bi-directional

Cisco 7960-CUVA Video Phone

CVP SIP Subsystem, SIP Proxy Server, Gateway, Unified CM: SIP (Session Initiation Protocol)

UDP 5060

TCP 5060

TLS 5061

SIP endpoints

Local / Remote between CVP components

Bi-directional

Listen port for incoming SIP requests. Port is configurable.

SIP Heartbeat Local Listen Port

UDP 5067

TCP 5067

Note

SIP endpoints

Random

Bi-directional

Listen port for incoming Heartbeat.

VXML Server: HTTP

TCP 7000

IOS VXML gateways/VVB

Random

Bi-directional

VXML over HTTP. Calls/sessions answered on port 7000 by HTTP server which relays request to WAS on local system port 9080.

VXML Server: HTTPS

TCP 7443

IOS VXML gateways/VVB

Random

Bi-directional

VXML over HTTPS. Calls/sessions answered on port 7443 by HTTPS server.

VXML Server with Tomcat

TCP 7005

Local machine

Bi-directional

Port restricted to local access only

TCP 7009

Bi-directional

AJP/1.3 Connector

VXML Server JMX

TCP 9696

JConsole

Bi-directional

JMX access by JConsole into VXML Server

VXML Server JMX RMI port

TCP 9697

JConsole

Random

Bi-directional

JMX access by JConsole into VXML Server

VXML Server

TCP 10100

Local VXML Server Administration Scripts

Bi-directional

Port restricted to local access only

CVP Call Server Tomcat: HTTP

TCP 8000

Browser

Random

Bi-directional

HTTP

CVP Call Server Tomcat: HTTPS

TCP 8443

Browser

Local / Remote Random

Bi-directional

HTTPS

CVP IVR Server

TCP 8002

VXML Server

Bi-directional

Message over TCP

CVP Call Server: HTTP

TCP 8005

Bi-directional

Port restricted to local access only

CVP OPSConsole: HTTP

TCP 9000

Web Browser

Random

Bi-directional

Web-based interface for configuring CVP components

CVP OPSConsole: HTTPS

TCP 9443

Web Browser

Random

Bi-directional

Web based interface for configuring CVP components with SSL

CVP OPSConsole

TCP 9005

Local machine

Bi-directional

Port restricted to local access only

CVP OPSConsole

TCP 9009

Bi-directional

AJP/1.3 Connector

CVP OPSConsole

TCP 1529

Local machine

Bi-directional

Port restricted to local access only

CVP Resource Manager FTP Server

TCP 21

Content Services Switch

Random

Bi-directional

Only opened by Resource Manager residing on the same machine as the CVP OPSConsole

CVP Resource Manager

TCP 2099

CVP OPSConsole

Random

Bi-directional

JMX communication from OPSConsole to CVP Resource Manager on remote device

CVP Resource Manager RMI Port

TCP 3000

CVP OPSConsole

Random

Bi-directional

JMX communication from OPSConsole to CVP Resource Manager on remote device

CVP Resource Manager Java Service Wrapper

TCP 32000 - 32999 (first available)

JVM instance launched by wrapper

Random

Bi-directional

CVP Resource Manager Service Wrapper will no longer accept connections after the first JVM instance is connected.

MRCP V1 (RTSP)

TCP 554

VXML gateway

MRCP session between gateway voice browser and MRCP server. This is the signaling path; the media path uses RTP.

Also, Helix streaming audio/ ASR/TTS (MRCP/RTSP)

MCRP V2 (SIP)

TCP 5060

VXML gateway

MRCP session between gateway voice browser and MRCP server. This is the signaling path; the media path uses RTP.

CVP SNMP SubAgent

UDP 5517, 5519, 5521, 5523, 5525, 5527, 5529, 5531, 5533, 5535, 5537, 5539, 5541, 5543, 5545, 5547, 5549, 5551, 5553, 5555

CVP SNMP subsystem

Bi-directional

CVP SNMP SubAgent services local requests from CVP SNMP subsystem

CVP SNMP subsystem

UDP 5516, 5518, 5520, 5522, 5524, 5526, 5528, 5530, 5532, 5534, 5536, 5538, 5540, 5542, 5544, 5546, 5548, 5550, 5552, 5554

CVP SNMP SubAgent

Bi-directional

CVP SNMP subsystem services local requests from CVP SNMP SubAgent

CVP ICM Subsystem

TCP 5000

IPCC Enterprise VRU CTI (ICM/IVR message interface)

Random

Bi-directional

Between CVP ICM Subsystem (Call Server) and Unified CCE /ICM VRU PG. Port is configurable.

Web Server: HTTP

TCP 80

Voice Browsers

Random

Bi- directional

Voice browsers fetches media and "External VXML" files from media server.

This port is configurable.

Web Server: HTTPS

TCP 443

Voice Browsers

Random

Bi- directional

Voice browsers fetches media and "External VXML" files from media server.

This port is configurable.

IBM Informix

TCP 1526

CVP Reporting Subsystem

Random

Bi-directional

Database Connection

IBM Informix Storage Manager

TCP 7939 - 7942 TCP 111

IBM Informix

Bi-directional

IBM Informix Storage Manager Services

IBM WAS Console

TCP 9043, 9060

IBM Informix

Random for remote desktop

Bi-directional

CVP Web Services Manager: HTTP/HTTPS

TCP 8101, 8110, 8111

TCP 10000, 10001, 10002, 10003

Unified System CLI, Diagnostic Portal, Custom Agent Desktop

Random

Bi-directional

REST Web Services

TCP 10000, 10001, 10002, 10003 OAMP ports are used for transferring data related to the configuration and administration of
                                          VXML Server and Call Server.

CVP OPSConsole

TCP 443

Hybrid Services on Cloud

Random

Bidirectional

Following URLs must be included in the allowed list of network :

*.wbx2.com

*.ciscoccservice.com

Listener
                                          					 (Process or Application Protocol)

Listener
                                          					 Protocol and Port

Remote
                                          					 Device (Process or Application Protocol)

Remote Port

Traffic
                                          					 Direction

Notes

SNMP Primary Agent

TCP 7161

Local
                                          					 SNMP subagents

Bi-directional

SNMP Primary Agent listens for TCP connections from local SNMP subagents.

SNMP–Trap

UDP 162

SNMP Primary Agent

Random

Bi-directional

SNMP Primary Agent sends SNMP traps to SNMP management application.

Syslog

UDP 514

Random

Bi-directional

Syslog
                                          					 protocol provides a transport to allow a machine to send event notification
                                          					 messages across IP network to event message collectors. Port is configurable.

Telnet

TCP 23

RDP
                                          					 (Terminal Services)

TCP 3389

Random

Bi-directional

pcAnywhere

TCP 5631

UDP 5632

VNC

TCP 5900

TCP 5800

Listener (Process or Application Protocol)

Listener Protocol and Port

Notes

RPC

TCP 135

NetBIOS Session

TCP 139

NetBIOS NameResolution

TCP 137

UDP 137

NetBIOS Netlogon/Browsing

UDP 138

SMB

TCP 445

UDP 445

Microsoft CIFS

DNS

TCP 53

UDP 53

optima-vnet

TCP 1051

TCP Optima VNET

optima-vnet

UDP 1051

UDP Optima VNET

Note

Ephemeral loopback client ports may be opened locally for CVP services to talk to port 1529 for communications with Derby
                                                database.

Similarly, ephemeral loopback client/server ports may be opened locally by CVP services for internal calls.

Ephemeral loopback client ports may also be opened by local subagents for talking to the SNMP primary agent running on port
                                                7161.

The above ports are closed when the services concerned are shut down.

From a security perspective, it is recommended to review the ports opened by the underlying Windows operating system or other
                                          services running on a machine and close all ports except those required for system operation.

Note

For more information on Windows authentication and remote administration ports,
                                          					see Service overview and network port requirements for the Windows Server in
                                          					Microsoft documentation.

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| TCP | 2000-2002 |  |  | Bi-directional | Call Manager and gateway interface communication |
| Call Server JMX | 2098 | JConsole | Random | Bi-directional | JMX access by JConsole into Call Server |
| Call Server JMX RMI port | 2097 | JConsole | Random | Bi-directional | JMX access by JConsole into Call Server |
| WSM JMX | TCP 10002 | JConsole | Random | Bi-directional | JMX access by JConsole into WSM |
| WSM JMX RMI | TCP 10003 | JConsole | Random | Bi-directional | JMX access by JConsole into WSM |
| OAMP JMX | TCP 10001 | JConsole | Random | Bi-directional | JMX access by JConsole into OAMP |
| OAMP JMX RMI | TCP 10000 | JConsole | Random | Bi-directional | JMX access by JConsole into OAMP |
| CVP Messaging Layer | TCP 23000 - 28000 (First available) | CVP Subsystem |  | Bi-directional | CVP Message Bus communications |
| 7960-CUVA Video | UDP 5445 | 7960-CUVA |  | Bi-directional | Cisco 7960-CUVA Video Phone |
| CVP SIP Subsystem, SIP Proxy Server, Gateway, Unified CM: SIP (Session Initiation Protocol) | UDP 5060 TCP 5060 TLS 5061 | SIP endpoints | Local / Remote between CVP components | Bi-directional | Listen port for incoming SIP requests. Port is configurable. |
| SIP Heartbeat Local Listen Port | UDP 5067 TCP 5067 Note This port must be different from the default SIP port which is 5060/5061 (see aforementioned row). | Note | This port must be different from the default SIP port which is 5060/5061 (see aforementioned row). | SIP endpoints | Random | Bi-directional | Listen port for incoming Heartbeat. |
| Note | This port must be different from the default SIP port which is 5060/5061 (see aforementioned row). |
| VXML Server: HTTP | TCP 7000 | IOS VXML gateways/VVB | Random | Bi-directional | VXML over HTTP. Calls/sessions answered on port 7000 by HTTP server which relays request to WAS on local system port 9080. |
| VXML Server: HTTPS | TCP 7443 | IOS VXML gateways/VVB | Random | Bi-directional | VXML over HTTPS. Calls/sessions answered on port 7443 by HTTPS server. |
| VXML Server with Tomcat | TCP 7005 | Local machine |  | Bi-directional | Port restricted to local access only |
| TCP 7009 |  |  | Bi-directional | AJP/1.3 Connector |
| VXML Server JMX | TCP 9696 | JConsole |  | Bi-directional | JMX access by JConsole into VXML Server |
| VXML Server JMX RMI port | TCP 9697 | JConsole | Random | Bi-directional | JMX access by JConsole into VXML Server |
| VXML Server | TCP 10100 | Local VXML Server Administration Scripts |  | Bi-directional | Port restricted to local access only |
| CVP Call Server Tomcat: HTTP | TCP 8000 | Browser | Random | Bi-directional | HTTP |
| CVP Call Server Tomcat: HTTPS | TCP 8443 | Browser | Local / Remote Random | Bi-directional | HTTPS |
| CVP IVR Server | TCP 8002 | VXML Server |  | Bi-directional | Message over TCP |
| CVP Call Server: HTTP | TCP 8005 |  |  | Bi-directional | Port restricted to local access only |
| CVP OPSConsole: HTTP | TCP 9000 | Web Browser | Random | Bi-directional | Web-based interface for configuring CVP components |
| CVP OPSConsole: HTTPS | TCP 9443 | Web Browser | Random | Bi-directional | Web based interface for configuring CVP components with SSL |
| CVP OPSConsole | TCP 9005 | Local machine |  | Bi-directional | Port restricted to local access only |
| CVP OPSConsole | TCP 9009 |  |  | Bi-directional | AJP/1.3 Connector |
| CVP OPSConsole | TCP 1529 | Local machine |  | Bi-directional | Port restricted to local access only |
| CVP Resource Manager FTP Server | TCP 21 | Content Services Switch | Random | Bi-directional | Only opened by Resource Manager residing on the same machine as the CVP OPSConsole |
| CVP Resource Manager | TCP 2099 | CVP OPSConsole | Random | Bi-directional | JMX communication from OPSConsole to CVP Resource Manager on remote device |
| CVP Resource Manager RMI Port | TCP 3000 | CVP OPSConsole | Random | Bi-directional | JMX communication from OPSConsole to CVP Resource Manager on remote device |
| CVP Resource Manager Java Service Wrapper | TCP 32000 - 32999 (first available) | JVM instance launched by wrapper | Random | Bi-directional | CVP Resource Manager Service Wrapper will no longer accept connections after the first JVM instance is connected. |
| MRCP V1 (RTSP) | TCP 554 | VXML gateway |  |  | MRCP session between gateway voice browser and MRCP server. This is the signaling path; the media path uses RTP. Also, Helix streaming audio/ ASR/TTS (MRCP/RTSP) |
| MCRP V2 (SIP) | TCP 5060 | VXML gateway |  |  | MRCP session between gateway voice browser and MRCP server. This is the signaling path; the media path uses RTP. |
| CVP SNMP SubAgent | UDP 5517, 5519, 5521, 5523, 5525, 5527, 5529, 5531, 5533, 5535, 5537, 5539, 5541, 5543, 5545, 5547, 5549, 5551, 5553, 5555 | CVP SNMP subsystem |  | Bi-directional | CVP SNMP SubAgent services local requests from CVP SNMP subsystem |
| CVP SNMP subsystem | UDP 5516, 5518, 5520, 5522, 5524, 5526, 5528, 5530, 5532, 5534, 5536, 5538, 5540, 5542, 5544, 5546, 5548, 5550, 5552, 5554 | CVP SNMP SubAgent |  | Bi-directional | CVP SNMP subsystem services local requests from CVP SNMP SubAgent |
| CVP ICM Subsystem | TCP 5000 | IPCC Enterprise VRU CTI (ICM/IVR message interface) | Random | Bi-directional | Between CVP ICM Subsystem (Call Server) and Unified CCE /ICM VRU PG. Port is configurable. |
| Web Server: HTTP | TCP 80 | Voice Browsers | Random | Bi- directional | Voice browsers fetches media and "External VXML" files from media server. This port is configurable. |
| Web Server: HTTPS | TCP 443 | Voice Browsers | Random | Bi- directional | Voice browsers fetches media and "External VXML" files from media server. This port is configurable. |
| IBM Informix | TCP 1526 | CVP Reporting Subsystem | Random | Bi-directional | Database Connection |
| IBM Informix Storage Manager | TCP 7939 - 7942 TCP 111 | IBM Informix |  | Bi-directional | IBM Informix Storage Manager Services |
| IBM WAS Console | TCP 9043, 9060 | IBM Informix | Random for remote desktop | Bi-directional |  |
| CVP Web Services Manager: HTTP/HTTPS | TCP 8101, 8110, 8111 TCP 10000, 10001, 10002, 10003 | Unified System CLI, Diagnostic Portal, Custom Agent Desktop | Random | Bi-directional | REST Web Services TCP 10000, 10001, 10002, 10003 OAMP ports are used for transferring data related to the configuration and administration of
                                          VXML Server and Call Server. |
| CVP OPSConsole | TCP 443 | Hybrid Services on Cloud | Random | Bidirectional | Following URLs must be included in the allowed list of network : *.wbx2.com *.ciscoccservice.com |

| Note | This port must be different from the default SIP port which is 5060/5061 (see aforementioned row). |
|---|---|

| Listener
                                          					 (Process or Application Protocol) | Listener
                                          					 Protocol and Port | Remote
                                          					 Device (Process or Application Protocol) | Remote Port | Traffic
                                          					 Direction | Notes |
|---|---|---|---|---|---|
| SNMP Primary Agent | TCP 7161 | Local
                                          					 SNMP subagents |  | Bi-directional | SNMP Primary Agent listens for TCP connections from local SNMP subagents. |
| SNMP–Trap | UDP 162 | SNMP Primary Agent | Random | Bi-directional | SNMP Primary Agent sends SNMP traps to SNMP management application. |
| Syslog | UDP 514 |  | Random | Bi-directional | Syslog
                                          					 protocol provides a transport to allow a machine to send event notification
                                          					 messages across IP network to event message collectors. Port is configurable. |
| Telnet | TCP 23 |  |  |  |  |
| RDP
                                          					 (Terminal Services) | TCP 3389 |  | Random | Bi-directional |  |
| pcAnywhere | TCP 5631 UDP 5632 |  |  |  |  |
| VNC | TCP 5900 TCP 5800 |  |  |  |  |

| Listener (Process or Application Protocol) | Listener Protocol and Port | Notes |
|---|---|---|
| RPC | TCP 135 |  |
| NetBIOS Session | TCP 139 |  |
| NetBIOS NameResolution | TCP 137 UDP 137 |  |
| NetBIOS Netlogon/Browsing | UDP 138 |  |
| SMB | TCP 445 UDP 445 | Microsoft CIFS |
| DNS | TCP 53 UDP 53 |  |
| optima-vnet | TCP 1051 | TCP Optima VNET |
| optima-vnet | UDP 1051 | UDP Optima VNET |

| Note | Ephemeral loopback client ports may be opened locally for CVP services to talk to port 1529 for communications with Derby
                                                database. Similarly, ephemeral loopback client/server ports may be opened locally by CVP services for internal calls. Ephemeral loopback client ports may also be opened by local subagents for talking to the SNMP primary agent running on port
                                                7161. The above ports are closed when the services concerned are shut down. From a security perspective, it is recommended to review the ports opened by the underlying Windows operating system or other
                                          services running on a machine and close all ports except those required for system operation. |
|---|---|

| Note | For more information on Windows authentication and remote administration ports,
                                          					see Service overview and network port requirements for the Windows Server in
                                          					Microsoft documentation. |
|---|---|