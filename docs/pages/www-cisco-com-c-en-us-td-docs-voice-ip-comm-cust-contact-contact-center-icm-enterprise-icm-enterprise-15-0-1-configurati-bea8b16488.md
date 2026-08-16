---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-configurati-bea8b16488
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/configuration/guide/ucce_b_1501_port-utilization/rcct_m_1501_system-services.html
retrieved_at: 2026-08-16T14:34:28.309894+00:00
---

Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 15.0(1)

# Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 15.0(1)

Updated: April 30, 2025

Chapter: Port Utilization in System Services

## Chapter: Port Utilization in System Services

- Port Utilization in System Services

- Port Utilization Table Columns

- System Services                              	 Port Utilization

# Port Utilization in System Services

## Port Utilization Table Columns

The columns in the
                              		port utilization tables in this document describe the following:

A value
                                    				representing the server or application and where applicable, the open or
                                    				proprietary application protocol.

An identifier
                                    				for the TCP or UDP port that the server or application is listening on, along
                                    				with the IP address for incoming connection requests when acting as a server.

The remote application or device making a connection to the server or service specified by the protocol.

The remote port is used to make an outgoing connection to the corresponding listener port.

The direction that traffic flows through the port: Inbound, Bidirectional, Outbound.

Note

The operating system dynamically assigns the source port that the local application or service uses to connect to the destination
                                                port of a remote device. In most cases, this port is assigned randomly from unused ports in the ephemeral port range 1024 - 65535 .

For security reasons, keep open only the ports mentioned in this guide and those required by your application. Keep the rest
                                                of the ports blocked.

Note

The preceding column descriptions apply to all the tables in this Port Utilization guide.

## System Services
                        	 Port Utilization

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic direction

Purpose

System Service

TCP 7

Editor

—

Bidirectional

- Echo for Editor

- ICM Controller

System Service

TCP 22

—

—

Bidirectional

SFTP and SSH access

Tomcat (HTTP)

TCP 80

—

—

Bidirectional

- Web access

- Call recording server

- Unified CCMP Web server and AXL provisioning

- CRM Connector server

- Default port for voice browsers to fetch media and "external VXML" files from media server

System Service

UDP 123

—

—

Bidirectional

NTP, network time sync

SNMP Agent

UDP 161

—

—

Bidirectional

Provide services for SNMP-based management applications

IIS

TCP 443

Client Browser

Unified CCE Admin (AW-HDS)

Web Setup

—

Bidirectional

Web access for CCE Web Administration, Web Setup, and Internet Script Editor

- Unified CCMP clients

- Default port for voice browsers to fetch media and "external VXML" files from media server

AON Management Console (AMC) Service

TCP 1090

Intracluster communication

—

Bidirectional

Provide RTMT data collecting, logging and alerting functionalities (AMC RMI Object Port)

AON Management Console (AMC) Service

TCP 1099

Intracluster communication

—

Bidirectional

Provide RTMT data collecting, logging and alerting functionalities (AMC RMI Registry Port)

DBMON

TCP 1500

—

—

Bidirectional

This is the port where the IDS engine listens for DB clients

DBMON

TCP 1501

—

—

Bidirectional

- This is an alternate port to bring up a second instance of IDS during upgrade.

- Localhost traffic only

DBL RPC

TCP 1515

Intracluster communication

—

Bidirectional

DBL RPC, this is used during installation to set up IDS replication between nodes

Real-Time Information Server (RIS) Data Collector service (RISDC)

TCP 2555

Intracluster communication

—

Bidirectional

Used by the RISDC platform service. The Real-time Information Server (RIS) maintains real-time Cisco Unified CM information
                                          such as device registration status, performance counter statistics, critical alarms generated, and so on. The Cisco RISDC
                                          service provides an interface for applications, such as RTMT, SOAP applications, Cisco Unified CM Administration and AMC to
                                          retrieve the information that is stored in all RIS nodes in the cluster.

RISDC

TCP 2556

Intracluster communication

—

Bidirectional

Allowed RIS client connection to retrieve real-time information

Disaster Recovery System (DRS)

TCP 4040

—

—

Bidirectional

Real-time service

Real-time service

TCP 5001

—

—

Bidirectional

SOAP Monitor

Used by SOAP to monitor the Real Time Monitoring Service and fetch the Server information for selection of specific CM devices
                                          and other such activities.

Perfmon service

TCP 5002

—

—

Bidirectional

SOAP Monitor

Used by SOAP to monitor the Performance Monitor Service for opening and closing sessions, collecting session data and fetching
                                          various other data.

Control center service

TCP 5003

—

—

Bidirectional

SOAP Monitor

Used by SOAP to monitor the Control Center Service for activities like getting the Service Status and performing service deployment.

Log Collection Service

TCP 5004

—

—

Bidirectional

SOAP Monitor

System Service

TCP 5007

—

—

Bidirectional

SOAP Monitor - a troubleshooting tool for SOAP infrastructure

Cisco Identity Service Data Grid

TCP 5702

Intra-cluster communication

5702

Note: The Cisco IdS server node in the cluster connects to this port.

Bidirectional

Data or Service grid to manage Cisco IdS cluster nodes.

DBMON (CN)

TCP 8001

Intracluster communication

—

Bidirectional

DB change notification port.

Tomcat

TCP 8005

—

—

—

Used for receiving shutdown requests, which would halt all applications within Tomcat

Tomcat (HTTP)

TCP 8080

Client Browser

—

Bidirectional

- Client browser trying to access any of the Administration interfaces or User Options interface.

- Web services client using RTMT, configuration APIs, and mobile supervisor applications.

- Data replication for call recording server

- OAMP for Live Data

- CRM Connector for SAP (adjustable through registry)

Tomcat (HTTPS)

TCP 8443

Client Browser

—

Bidirectional

- Client browser trying to access any of the Administration interfaces or User Options interface.

- Web services client using RTMT, configuration APIs, and mobile supervisor applications.

- DB access via SOAP; Tomcat forwards the SOAP request to AXL.

IPSec Manager daemon

TCP 8500

—

—

Bidirectional

Connectivity testing. Uses a proprietary protocol.

IPSec Manager daemon

UDP 8500

—

—

Bidirectional

Cluster replication of platform data (hosts) certificates etc. Uses a proprietary protocol.

Cisco Identity Service ( Cisco IdS )

TCP 8553

—

—

—

HTTPS for Cisco IdS

### SOAP Port Considerations

The following considerations apply to the Simple Object Access Protocol (SOAP) ports:

SOAP monitor uses specific ports to send the corresponding SOAP API requests.

Access to the ports are always authenticated with the Username and Password authentication.

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

| Note | The operating system dynamically assigns the source port that the local application or service uses to connect to the destination
                                                port of a remote device. In most cases, this port is assigned randomly from unused ports in the ephemeral port range 1024 - 65535 . For security reasons, keep open only the ports mentioned in this guide and those required by your application. Keep the rest
                                                of the ports blocked. |
|---|---|

| Note | The preceding column descriptions apply to all the tables in this Port Utilization guide. |
|---|---|

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic direction | Purpose |
|---|---|---|---|---|---|
| System Service | TCP 7 | Editor | — | Bidirectional | - Echo for Editor - ICM Controller |
| System Service | TCP 22 | — | — | Bidirectional | SFTP and SSH access |
| Tomcat (HTTP) | TCP 80 | — | — | Bidirectional | - Web access - Call recording server - Unified CCMP Web server and AXL provisioning - CRM Connector server - Default port for voice browsers to fetch media and "external VXML" files from media server |
| System Service | UDP 123 | — | — | Bidirectional | NTP, network time sync |
| SNMP Agent | UDP 161 | — | — | Bidirectional | Provide services for SNMP-based management applications |
| IIS | TCP 443 | Client Browser Unified CCE Admin (AW-HDS) Web Setup | — | Bidirectional | Web access for CCE Web Administration, Web Setup, and Internet Script Editor - Unified CCMP clients - Default port for voice browsers to fetch media and "external VXML" files from media server |
| AON Management Console (AMC) Service | TCP 1090 | Intracluster communication | — | Bidirectional | Provide RTMT data collecting, logging and alerting functionalities (AMC RMI Object Port) |
| AON Management Console (AMC) Service | TCP 1099 | Intracluster communication | — | Bidirectional | Provide RTMT data collecting, logging and alerting functionalities (AMC RMI Registry Port) |
| DBMON | TCP 1500 | — | — | Bidirectional | This is the port where the IDS engine listens for DB clients |
| DBMON | TCP 1501 | — | — | Bidirectional | - This is an alternate port to bring up a second instance of IDS during upgrade. - Localhost traffic only |
| DBL RPC | TCP 1515 | Intracluster communication | — | Bidirectional | DBL RPC, this is used during installation to set up IDS replication between nodes |
| Real-Time Information Server (RIS) Data Collector service (RISDC) | TCP 2555 | Intracluster communication | — | Bidirectional | Used by the RISDC platform service. The Real-time Information Server (RIS) maintains real-time Cisco Unified CM information
                                          such as device registration status, performance counter statistics, critical alarms generated, and so on. The Cisco RISDC
                                          service provides an interface for applications, such as RTMT, SOAP applications, Cisco Unified CM Administration and AMC to
                                          retrieve the information that is stored in all RIS nodes in the cluster. |
| RISDC | TCP 2556 | Intracluster communication | — | Bidirectional | Allowed RIS client connection to retrieve real-time information |
| Disaster Recovery System (DRS) | TCP 4040 | — | — | Bidirectional | Real-time service |
| Real-time service | TCP 5001 | — | — | Bidirectional | SOAP Monitor Used by SOAP to monitor the Real Time Monitoring Service and fetch the Server information for selection of specific CM devices
                                          and other such activities. |
| Perfmon service | TCP 5002 | — | — | Bidirectional | SOAP Monitor Used by SOAP to monitor the Performance Monitor Service for opening and closing sessions, collecting session data and fetching
                                          various other data. |
| Control center service | TCP 5003 | — | — | Bidirectional | SOAP Monitor Used by SOAP to monitor the Control Center Service for activities like getting the Service Status and performing service deployment. |
| Log Collection Service | TCP 5004 | — | — | Bidirectional | SOAP Monitor |
| System Service | TCP 5007 | — | — | Bidirectional | SOAP Monitor - a troubleshooting tool for SOAP infrastructure |
| Cisco Identity Service Data Grid | TCP 5702 | Intra-cluster communication | 5702 Note: The Cisco IdS server node in the cluster connects to this port. | Bidirectional | Data or Service grid to manage Cisco IdS cluster nodes. |
| DBMON (CN) | TCP 8001 | Intracluster communication | — | Bidirectional | DB change notification port. |
| Tomcat | TCP 8005 | — | — | — | Used for receiving shutdown requests, which would halt all applications within Tomcat |
| Tomcat (HTTP) | TCP 8080 | Client Browser | — | Bidirectional | - Client browser trying to access any of the Administration interfaces or User Options interface. - Web services client using RTMT, configuration APIs, and mobile supervisor applications. - Data replication for call recording server - OAMP for Live Data - CRM Connector for SAP (adjustable through registry) |
| Tomcat (HTTPS) | TCP 8443 | Client Browser | — | Bidirectional | - Client browser trying to access any of the Administration interfaces or User Options interface. - Web services client using RTMT, configuration APIs, and mobile supervisor applications. - DB access via SOAP; Tomcat forwards the SOAP request to AXL. |
| IPSec Manager daemon | TCP 8500 | — | — | Bidirectional | Connectivity testing. Uses a proprietary protocol. |
| IPSec Manager daemon | UDP 8500 | — | — | Bidirectional | Cluster replication of platform data (hosts) certificates etc. Uses a proprietary protocol. |
| Cisco Identity Service ( Cisco IdS ) 1 | TCP 8553 | — | — | — | HTTPS for Cisco IdS |