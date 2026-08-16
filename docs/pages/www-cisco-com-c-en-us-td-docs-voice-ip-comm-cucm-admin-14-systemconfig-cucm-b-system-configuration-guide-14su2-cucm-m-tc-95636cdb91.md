---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-14-systemconfig-cucm-b-system-configuration-guide-14su2-cucm-m-tc-95636cdb91
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/14/systemConfig/cucm_b_system-configuration-guide-14su2/cucm_m_tcp-and-udp-port-usage-12-0.html
retrieved_at: 2026-08-16T16:34:06.895210+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# System Configuration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: August 7, 2026

Chapter: Cisco Unified Communications Manager TCP and UDP Port Usage

## Chapter: Cisco Unified Communications Manager TCP and UDP Port Usage

# Cisco Unified Communications Manager TCP and UDP Port Usage

## Cisco Unified Communications Manager TCP and UDP Port Usage Overview

Cisco Unified Communications
                              		  Manager TCP and UDP ports are organized into the following
                           		categories:

Intracluster Ports
                                 			 Between Cisco Unified Communications Manager Servers

Common Service
                                 			 Ports

Ports Between
                                 			 Cisco Unified Communications Manager and LDAP Directory

Web Requests From
                                 			 CCMAdmin or CCMUser to Cisco Unified Communications Manager

Web Requests From
                                 			 Cisco Unified Communications Manager to Phone

Signaling, Media,
                                 			 and Other Communication Between Phones and Cisco Unified Communications Manager

Signaling, Media,
                                 			 and Other Communication Between Gateways and Cisco Unified Communications
                                 			 Manager

Communication
                                 			 Between Applications and Cisco Unified Communications Manager

Communication
                                 			 Between CTL Client and Firewalls

Special Ports on
                                 			 HP Servers

See "Port Descriptions" for port details in each of the
                           		above categories.

Cisco has not
                                       		  verified all possible configuration scenarios for these ports. If you are
                                       		  having configuration problems using this list, contact Cisco technical support
                                       		  for assistance.

Port
                           		references apply specifically to Cisco Unified
                              		  Communications Manager . Some ports change from one release to
                           		another, and future releases may introduce new ports. Therefore, make sure that
                           		you are using the correct version of this document for the version of Cisco Unified
                              		  Communications Manager that is installed.

While
                           		virtually all protocols are bidirectional, directionality from the session
                           		originator perspective is presumed. In some cases, the administrator can
                           		manually change the default port numbers, though Cisco does not recommend this
                           		as a best practice. Be aware that Cisco Unified
                              		  Communications Manager opens several ports strictly for internal use.

Installing Cisco Unified
                              		  Communications Manager software automatically installs the following
                           		network services for serviceability and activates them by default. Refer to "Intracluster Ports Between Cisco Unified Communications Manager Servers" for details:

Cisco Log
                                 			 Partition Monitoring (To monitor and purge the common partition. This uses no
                                 			 custom common port.)

Cisco Trace
                                 			 Collection Service (TCTS port usage)

Cisco RIS Data
                                 			 Collector (RIS server port usage)

Cisco AMC Service
                                 			 (AMC port usage)

Configuration
                           		of firewalls, ACLs, or QoS will vary depending on topology, placement of
                           		telephony devices and services relative to the placement of network security
                           		devices, and which applications and telephony extensions are in use. Also, bear
                           		in mind that ACLs vary in format with different devices and versions.

You can also
                                       		  configure Multicast Music on Hold (MOH) ports in Cisco
                                          			 Unified Communications Manager . Port values for multicast MOH are not
                                       		  provided because the administrator specifies the actual port values.

The ephemeral port range for the system is 32768 to 61000 , and the ports needs to be open to keep the phones registered . For more information, see http://www.cisco.com/c/en/us/support/security/asa-5500-series-next-generation-firewalls/tsd-products-support-series-home.html .

Make sure that you configure your firewall so that connections to port 22 are open, and are not throttled. During the installation
                                       of IM and Presence subscriber nodes, multiple connections to the Cisco Unified Communications Manager publisher node are opened
                                       in quick succession. Throttling these connections could lead to a failed installation.

## Port Descriptions

### Intracluster Ports Between Cisco Unified Communications Manager Servers

From (Sender)

To (Listener)

Destination Port

Purpose

Endpoint

Unified Communications Manager

514 / UDP

System logging service

Unified Communications Manager

Unified Communications Manager

443 / TCP

This port is used for communication between the subscriber and publisher during COP file installation in the subscriber node.

Unified Communications Manager

RTMT

1090, 1099 / TCP

Cisco AMC Service for RTMT performance monitors, data collection, logging, and alerting

Unified Communications Manager (DB)

Unified Communications Manager (DB)

1500, 1501 / TCP

Database connection (1501 / TCP is the secondary connection)

Unified Communications Manager (DB)

Unified Communications Manager (DB)

1510 / TCP

CAR IDS DB. CAR IDS engine listens on waiting for connection requests from the clients.

Unified Communications Manager (DB)

Unified Communications Manager (DB)

1511 / TCP

CAR IDS DB. An alternate port used to bring up a second instance of CAR IDS during upgrade.

Unified Communications Manager (DB)

Unified Communications Manager (DB)

1515 / TCP

Database replication between nodes during installation.

Unified Communications Manager (DB)

Unified Communications Manager (DB)

1516 / TCP

Database replication between nodes during upgrade.

Cisco Extended Functions (QRT)

Unified Communications Manager (DB)

2552 / TCP

Allows subscribers to receive Cisco Unified Communications Manager database change notification

Unified Communications Manager

Unified Communications Manager

2551 / TCP

Intracluster communication between Cisco Extended Services for Active/Backup determination

Unified Communications Manager (RIS)

Unified Communications Manager (RIS)

2555 / TCP

Real-time Information Services (RIS) database server

Unified Communications Manager (RTMT/AMC/SOAP)

Unified Communications Manager (RIS)

2556 / TCP

Real-time Information Services (RIS) database client for Cisco RIS

Unified Communications Manager (DRS)

Unified Communications Manager (DRS)

4040 / TCP

DRS Primary Agent

Unified Communications Manager (Tomcat)

Unified Communications Manager (SOAP)

5001/TCP

This port is used by SOAP monitor for Real Time Monitoring Service.

Unified Communications Manager (Tomcat)

Unified Communications Manager (SOAP)

5002/TCP

This port is used by SOAP monitor for Performance Monitor Service.

Unified Communications Manager (Tomcat)

Unified Communications Manager (SOAP)

5003/TCP

This port is used by SOAP monitor for Control Center Service.

Unified Communications Manager (Tomcat)

Unified Communications Manager (SOAP)

5004/TCP

This port is used by SOAP monitor for Log Collection Service.

Standard CCM Admin Users / Admin

Unified Communications Manager

5005 / TCP

This port is used by SOAP CDROnDemand2 services

Unified Communications Manager (Tomcat)

Unified Communications Manager (SOAP)

5007 / TCP

SOAP monitor

Unified Communications Manager (RTMT)

Unified Communications Manager (TCTS)

Ephemeral / TCP

Cisco Trace Collection Tool Service (TCTS) -- the back end service for RTMT Trace and Log Central (TLC)

Unified Communications Manager (Tomcat)

Unified Communications Manager (TCTS)

7000, 7001, 7002 / TCP

This port is used for communication between Cisco Trace Collection Tool Service and Cisco Trace Collection servlet.

Unified Communications Manager (DB)

Unified Communications Manager (CDLM)

8001 / TCP

Client database change notification

Unified Communications Manager (SDL)

Unified Communications Manager (SDL)

8002 / TCP

Intracluster communication service

Unified Communications Manager (SDL)

Unified Communications Manager (SDL)

8003 / TCP

Intracluster communication service (to CTI)

Unified Communications Manager

CMI Manager

8004 / TCP

Intracluster communication between Cisco Unified Communications Manager and CMI Manager

Unified Communications Manager (Tomcat)

Unified Communications Manager (Tomcat)

8005 / TCP

Internal listening port used by Tomcat shutdown scripts

Unified Communications Manager (Tomcat)

Unified Communications Manager (Tomcat)

8080 / TCP

Communication between servers used for diagnostic tests

Gateway

Unified Communications Manager

8090

HTTP Port for communication between CuCM and GW (Cayuga interfae) for Gateway Recording feature.

Unified Communications Manager

Gateway

Unified Communications Manager (IPSec)

Unified Communications Manager (IPSec)

8500 / TCP and UDP

Intracluster replication of system data by IPSec Cluster Manager

Unified Communications Manager (RIS)

Unified Communications Manager (RIS)

8888 - 8889 / TCP

RIS Service Manager status request and reply

Location Bandwidth Manager (LBM)

Location Bandwidth Manager (LBM)

9004 / TCP

Intracluster communication between LBMs

Unified Communications Manager Publisher

Unified Communications Manager Subscriber

22 / TCP

Cisco SFTP service. You must open this port when installing a new subscriber.

Unified Communications Manager

Unified Communications Manager

8443 / TCP

Allows access to Control Center - Feature and Network service between nodes.

### Common Service
                           	 Ports

From (Sender)

To (Listener)

Destination Port

Purpose

Endpoint

Unified Communications Manager

7

Internet Control Message Protocol (ICMP) This protocol number carries echo-related traffic. It does not constitute a port
                                             as indicated in the column heading.

Unified Communications Manager

Endpoint

Unified Communications Manager (DRS, Call Detail Record)

SFTP server

22 / TCP

Send the backup data to the SFTP server. (DRS Local Agent)

Send the Call Detail Record data to SFTP server.

Endpoint

Unified Communications Manager (DHCP Server)

67 / UDP

Cisco Unified Communications Manager acting as a DHCP server

Cisco does not recommend running DHCP server on Cisco Unified Communications Manager.

Unified Communications Manager

DHCP Server

68 / UDP

Cisco Unified Communications Manager acting as a DHCP client

Cisco does not recommend running DHCP client on Cisco Unified Communications Manager. Configure Cisco Unified Communications
                                                         Manager with static IP addresses instead.)

Endpoint or Gateway

Unified Communications Manager

69, 6969, then Ephemeral / UDP

TFTP service to phones and gateways

Endpoint or Gateway

Unified Communications Manager

6970 / TCP

TFTP between primary and proxy servers.

HTTP service from the TFTP server to phones and gateways.

Unified Communications Manager

NTP Server

123 / UDP

Network Time Protocol (NTP)

SNMP Server

Unified Communications Manager

161 / UDP

SNMP service response (requests from management applications)

CUCM Server SNMP Primary Agent application

SNMP trap destination

162 / UDP

SNMP traps

SNMP Server

Unified Communications Manager

199 / TCP

built-in SNMP agent listening port for SMUX support

Unified Communications Manager

DHCP Server

546 / UDP

DHCPv6. DHCP port for IPv6.

Unified Communications Manager Serviceability

Location Bandwidth Manager (LBM)

5546 / TCP

Enhanced Location CAC Serviceability

Unified Communications Manager

Location Bandwidth Manager (LBM)

5547 / TCP

Call Admission requests and bandwidth deductions

Unified Communications Manager

Unified Communications Manager

6161 / UDP

Used for communication between Primary Agent and Native Agent to process Native agent MIB requests

Unified Communications Manager

Unified Communications Manager

6162 / UDP

Used for communication between Primary Agent and Native Agent to forward notifications generated from Native Agent

Centralized TFTP

Alternate TFTP

6970 / TCP

Centralized TFTP File Locator Service

Unified Communications Manager

Unified Communications Manager

7161 / TCP

Used for communication between SNMP Primary Agent and subagents

SNMP Server

Unified Communications Manager

7999 / TCP

Cisco Discovery Protocol (CDP) agent communicates with CDP executable

Endpoint

Unified Communications Manager

443, 8443 / TCP

Used for Cisco User Data Services (UDS) requests

Unified Communications Manager

Unified Communications Manager

9050 / TCP

Service CRS requests through the TAPS residing on Cisco Unified Communications Manager

Unified Communications Manager

Unified Communications Manager

61441 / UDP

Cisco Unified Communications Manager applications send out alarms to this port through UDP. Cisco Unified Communications Manager
                                             MIB agent listens on this port and generates SNMP traps per Cisco Unified Communications Manager MIB definition.

Unified Communications Manager

Unified Communications Manager

5060, 5061 / TCP

Provide trunk-based SIP services

Unified Communications Manager

Unified Communications Manager

7501

Used by Intercluster Lookup Service (ILS) for certificate based authentication.

Unified Communications Manager

Unified Communications Manager

7502

Used by ILS for password-based authentication.

Unified Communications Manager

Unified Communications Manager

8006

Used for signaling between Unified CM and ILS

Unified Communications Manager

Unified Communications Manager

9966

Used by Cisco push notification service to communicate between the nodes in the cluster when firewall is enabled.

Unified Communications Manager

Unified Communications Manager

9560

Used by Local Push Notification Service (LPNS).

--

--

8000-48200

ASR and ISR G3 platforms default port range.

16384-32766

ISR G2 platform default port range.

Endpoint

Unified Communications Manager

514 / UDP (default)

601 / TCP

6514 / TLS

Remote system logging service

### Ports Between Cisco Unified Communications Manager and LDAP Directory

From (Sender)

To (Listener)

Destination Port

Purpose

Unified Communications Manager

External Directory

389, 636, 3268, 3269 / TCP

Lightweight Directory Access Protocol (LDAP) query to external directory (Active Directory, Netscape Directory)

External Directory

Unified Communications Manager

Ephemeral

### Web Requests From CCMAdmin or CCMUser to Cisco Unified Communications Manager

From (Sender)

To (Listener)

Destination Port

Purpose

Browser

Unified Communications Manager

80, 8080 / TCP

Hypertext Transport Protocol (HTTP)

Browser

Unified Communications Manager

443, 8443 / TCP

Hypertext Transport Protocol over SSL (HTTPS)

Browser

Unified Communications Manager

9463 / TCP

Hypertext Transport Protocol over SSL (HTTPS) allows only TLS1.3 with v6.

### Web Requests From Cisco Unified Communications Manager to Phone

From (Sender)

To (Listener)

Destination Port

Purpose

Unified Communications Manager

QRT

RTMT

Find and List Phones page

Phone Configuration page

Phone

80 / TCP

Hypertext Transport Protocol (HTTP)

### Signaling, Media,
                           	 and Other Communication Between Phones and Cisco Unified Communications
                           	 Manager

From (Sender)

To (Listener)

Destination Port

Purpose

Phone

DNS server

53/ TCP

Session Initiation Protocol (SIP) phones resolve the Fully Qualified Domain Name (FQDN) using a Domain Name System (DNS)

By default, some wireless access points block TCP 53 port, which prevents wireless SIP phones from registering when CUCM
                                                         is configured using FQDN.

Phone

Unified Communications Manager (TFTP)

69, then Ephemeral / UDP

Trivial File Transfer Protocol (TFTP) used to download firmware and configuration files

Phone

Unified Communications Manager

2000 / TCP

Skinny Client Control Protocol (SCCP)

Phone

Unified Communications Manager

2443 / TCP

Secure Skinny Client Control Protocol (SCCPS)

Phone

Unified Communications Manager

2445 / TCP

Provide trust verification service to endpoints.

Phone

Unified Communications Manager (CAPF)

3804 / TCP

Certificate Authority Proxy Function (CAPF) listening port for issuing Locally Significant Certificates (LSCs) to IP phones

Phone

Unified Communications Manager

5060 / TCP and UDP

Session Initiation Protocol (SIP) phone

Unified Communications Manager

Phone

Phone

Unified Communications Manager

5061 TCP

Secure Session Initiation Protocol (SIPS) phone

Unified Communications Manager

Phone

Phone

Unified Communications Manager (TFTP)

6970 TCP

Phone

Unified Communications Manager (TFTP)

6971, 6972 / TCP

HTTPS interface to TFTP. Phones use this port to download a secure configuration file from TFTP.

Phone

Unified Communications Manager

8080 / TCP

Phone URLs for XML applications, authentication, directories, services, and so on. You can configure these ports on a per-service
                                             basis.

Phone

Unified Communications Manager

9443 / TCP

Phone use this port for authenticated contact search.

Phone

Unified Communications Manager

9444

Phones use this port number to use the Headset Management feature.

iPhone/iPad (Webex App)

Unified Communications Manager

9560/Secure WebSocket

Webex App uses this port number for the LPNS feature.

IP VMS

Phone

16384 - 32767 / UDP

Real-Time Protocol (RTP), Secure Real-Time Protocol (SRTP)

Cisco Unified Communications Manager only uses 24576-32767 although other devices use the full range.

Phone

IP VMS

### Signaling, Media, and Other Communication Between Gateways and Cisco Unified Communications Manager

From (Sender)

To (Listener)

Destination Port

Purpose

Gateway

Unified Communications Manager

47, 50, 51

Generic Routing Encapsulation (GRE), Encapsulating Security Payload (ESP), Authentication Header (AH). These protocols numbers
                                             carry encrypted IPSec traffic. They do not constitute a port as indicated in the column heading.

Unified Communications Manager

Gateway

Gateway

Unified Communications Manager

500 / UDP

Internet Key Exchange (IKE) for IP Security protocol (IPSec) establishment

Unified Communications Manager

Gateway

Gateway

Unified Communications Manager (TFTP)

69, then Ephemeral / UDP

Trivial File Transfer Protocol (TFTP)

Unified Communications Manager with Cisco Intercompany Media Engine (CIME) trunk

CIME ASA

1024-65535 / TCP

Port mapping service. Only used in the CIME off-path deployment model.

Gatekeeper

Unified Communications Manager

1719 / UDP

Gatekeeper (H.225) RAS

Gateway

Unified Communications Manager

1720 / TCP

H.225 signaling services for H.323 gateways and Intercluster Trunk (ICT)

Unified Communications Manager

Gateway

Gateway

Unified Communications Manager

Ephemeral / TCP

H.225 signaling services on gatekeeper-controlled trunk

Unified Communications Manager

Gateway

Gateway

Unified Communications Manager

Ephemeral / TCP

H.245 signaling services for establishing voice, video, and data

The H.245 port used by the remote system depends on the type of gateway.

For IOS gateways, the H.245 port range is from 11000 to 65535.

Unified Communications Manager

Gateway

Gateway

Unified Communications Manager

2000 / TCP

Skinny Client Control Protocol (SCCP)

Gateway

Unified Communications Manager

2001 / TCP

Upgrade port for 6608 gateways with Cisco Unified Communications Manager deployments

Gateway

Unified Communications Manager

2002 / TCP

Upgrade port for 6624 gateways with Cisco Unified Communications Manager deployments

Gateway

Unified Communications Manager

2427 / UDP

Media Gateway Control Protocol (MGCP) gateway control

Unified Communications Manager

Gateway

2427 / UDP

Media Gateway Control Protocol (MGCP) gateway control

Gateway

Unified Communications Manager

2428 / TCP

Media Gateway Control Protocol (MGCP)

For IOS gateways, the source MGCP backhaul TCP port range is from 11000 to 65535.

--

--

4000 - 4005 / TCP

These ports are used as phantom Real-Time Transport Protocol (RTP) and Real-Time Transport Control Protocol (RTCP) ports for
                                             audio, video and data channel when Cisco Unified Communications Manager does not have ports for these media.

Gateway

Unified Communications Manager

5060 / TCP and UDP

Session Initiation Protocol (SIP) gateway and Intercluster Trunk (ICT)

Unified Communications Manager

Gateway

Gateway

Unified Communications Manager

5061 / TCP

Secure Session Initiation Protocol (SIPS) gateway and Intercluster Trunk (ICT)

Unified Communications Manager

Gateway

Gateway

Unified Communications Manager

16384 - 32767 / UDP

Real-Time Protocol (RTP), Secure Real-Time Protocol (SRTP)

Cisco Unified Communications Manager only uses 24576-32767 although other devices use the full range.

Unified Communications Manager

Gateway

### Communication Between Applications and Cisco Unified Communications Manager

From (Sender)

To (Listener)

Destination Port

Purpose

CTL Client

Unified Communications Manager CTL Provider

2444 / TCP

Certificate Trust List (CTL) provider listening service in Cisco Unified Communications Manager

Cisco Unified Communications App

Unified Communications Manager

2748 / TCP

CTI application server

Cisco Unified Communications App

Unified Communications Manager

2749 / TCP

TLS connection between CTI applications (JTAPI/TSP) and CTIManager

Cisco Unified Communications App

Unified Communications Manager

2789 / TCP

JTAPI application server

Unified Communications Manager Assistant Console

Unified Communications Manager

2912 / TCP

Cisco Unified Communications Manager Assistant server (formerly IPMA)

Unified Communications Manager Attendant Console

Unified Communications Manager

1103 -1129 / TCP

Cisco Unified Communications Manager Attendant Console (AC) JAVA RMI Registry server

Unified Communications Manager Attendant Console

Unified Communications Manager

1101 / TCP

RMI server sends RMI callback messages to clients on these ports.

Unified Communications Manager Attendant Console

Unified Communications Manager

1102 / TCP

Attendant Console (AC) RMI server bind port -- RMI server sends RMI messages on these ports.

Unified Communications Manager Attendant Console

Unified Communications Manager

3223 / UDP

Cisco Unified Communications Manager Attendant Console (AC) server line state port receives ping and registration message
                                             from, and sends line states to, the attendant console server.

Unified Communications Manager Attendant Console

Unified Communications Manager

3224 / UDP

Cisco Unified Communications Manager Attendant Console (AC) clients register with the AC server for line and device state
                                             information.

Unified Communications ManagerAttendant Console

Unified Communications Manager

4321 / UDP

Cisco Unified Communications Manager Attendant Console (AC) clients register to the AC server for call control.

Unified Communications Manager with SAF/CCD

IOS Router running SAF image

5050 / TCP

Multi-Service IOS Router running EIGRP/SAF Protocol.

Unified Communications Manager

Cisco Intercompany Media Engine (IME) Server

5620 / TCP

Cisco recommends a value of 5620 for this port, but you can change the value by executing the add ime vapserver or set ime
                                             vapserver port CLI command on the Cisco IME server.

VAP protocol used to communicate to the Cisco Intercompany Media Engine server.

Cisco Unified Communications App

Unified Communications Manager

8443 / TCP

AXL / SOAP API for programmatic reads from or writes to the Cisco Unified Communications Manager database that third parties
                                             such as billing or telephony management applications use.

### Communication Between CTL Client and Firewalls

From (Sender)

To (Listener)

Destination Port

Purpose

CTL Client

TLS Proxy Server

2444 / TCP

Certificate Trust List (CTL) provider listening service in an ASA firewall

### Communication Between Cisco Smart Licensing Service and Cisco Smart Software Manager

Cisco Smart Licensing Service in Unified Communications Manager sets up direct communication with Cisco Smart Software Manager
                                 through Call Home.

From (Sender)

To (Listener)

Destination Port

Purpose

Unified Communications Manager (Cisco Smart Licensing Service)

Cisco Smart Software Manager (CSSM)

443 / HTTPS

Smart Licensing Service sends the license usage to CSSM to check whether Unified CM is a complaint or not.

### Special Ports on HP Servers

From (Sender)

To (Listener)

Destination Port

Purpose

Endpoint

HP SIM

2301 / TCP

HTTP port to HP agent

Endpoint

HP SIM

2381 / TCP

HTTPS port to HP agent

Endpoint

Compaq Management Agent

25375, 25376, 25393 / UDP

COMPAQ Management Agent extension (cmaX)

Endpoint

HP SIM

50000 - 50004 / TCP

HTTPS port to HP SIM

## Port References

### Firewall Application
                           	 Inspection Guides

ASA Series
                              		reference information

http://www.cisco.com/c/en/us/support/security/asa-5500-series-next-generation-firewalls/tsd-products-support-series-home.html

PIX Application Inspection Configuration Guides

http://www.cisco.com/c/en/us/support/security/pix-firewall-software/products-installation-and-configuration-guides-list.html

FWSM 3.1
                              		Application Inspection Configuration Guide

http://www-author.cisco.com/c/en/us/td/docs/security/fwsm/fwsm31/configuration/guide/fwsm_cfg/inspct_f.html

### IETF TCP/UDP Port
                           	 Assignment List

Internet
                              		Assigned Numbers Authority (IANA) IETF assigned Port List

http://www.iana.org/assignments/port-numbers

### IP Telephony
                           	 Configuration and Port Utilization Guides

Cisco CRS
                              		4.0 (IP IVR and IPCC Express) Port Utilization Guide

http://www.cisco.com/en/US/products/sw/custcosw/ps1846/products_installation_and_configuration_guides_list.html

Port
                              		Utilization Guide for Cisco ICM/IPCC Enterprise and Hosted Editions

http://www.cisco.com/en/US/products/sw/custcosw/ps1001/products_installation_and_configuration_guides_list.html

Cisco
                              		Unified Communications Manager Express Security Guide to Best Practices

http://www.cisco.com/en/US/netsol/ns340/ns394/ns165/ns391/networking_solutions_design_guidance09186a00801f8e30.html

Cisco Unity
                              		Express Security Guide to Best Practices

http://www.cisco.com/en/US/netsol/ns340/ns394/ns165/ns391/networking_solutions_design_guidance09186a00801f8e31.html#wp41149

### VMware Port
                           	 Assignment List

TCP and UDP Ports for vCenter
                                 		  Server, ESX hosts, and Other Network Components Management Access

| Note | Cisco has not
                                       		  verified all possible configuration scenarios for these ports. If you are
                                       		  having configuration problems using this list, contact Cisco technical support
                                       		  for assistance. |
|---|---|

| Note | You can also
                                       		  configure Multicast Music on Hold (MOH) ports in Cisco
                                          			 Unified Communications Manager . Port values for multicast MOH are not
                                       		  provided because the administrator specifies the actual port values. |
|---|---|

| Note | The ephemeral port range for the system is 32768 to 61000 , and the ports needs to be open to keep the phones registered . For more information, see http://www.cisco.com/c/en/us/support/security/asa-5500-series-next-generation-firewalls/tsd-products-support-series-home.html . |
|---|---|

| Note | Make sure that you configure your firewall so that connections to port 22 are open, and are not throttled. During the installation
                                       of IM and Presence subscriber nodes, multiple connections to the Cisco Unified Communications Manager publisher node are opened
                                       in quick succession. Throttling these connections could lead to a failed installation. |
|---|---|

| From (Sender) | To (Listener) | Destination Port | Purpose |
|---|---|---|---|
| Endpoint | Unified Communications Manager | 514 / UDP | System logging service |
| Unified Communications Manager | Unified Communications Manager | 443 / TCP | This port is used for communication between the subscriber and publisher during COP file installation in the subscriber node. |
| Unified Communications Manager | RTMT | 1090, 1099 / TCP | Cisco AMC Service for RTMT performance monitors, data collection, logging, and alerting |
| Unified Communications Manager (DB) | Unified Communications Manager (DB) | 1500, 1501 / TCP | Database connection (1501 / TCP is the secondary connection) |
| Unified Communications Manager (DB) | Unified Communications Manager (DB) | 1510 / TCP | CAR IDS DB. CAR IDS engine listens on waiting for connection requests from the clients. |
| Unified Communications Manager (DB) | Unified Communications Manager (DB) | 1511 / TCP | CAR IDS DB. An alternate port used to bring up a second instance of CAR IDS during upgrade. |
| Unified Communications Manager (DB) | Unified Communications Manager (DB) | 1515 / TCP | Database replication between nodes during installation. |
| Unified Communications Manager (DB) | Unified Communications Manager (DB) | 1516 / TCP | Database replication between nodes during upgrade. |
| Cisco Extended Functions (QRT) | Unified Communications Manager (DB) | 2552 / TCP | Allows subscribers to receive Cisco Unified Communications Manager database change notification |
| Unified Communications Manager | Unified Communications Manager | 2551 / TCP | Intracluster communication between Cisco Extended Services for Active/Backup determination |
| Unified Communications Manager (RIS) | Unified Communications Manager (RIS) | 2555 / TCP | Real-time Information Services (RIS) database server |
| Unified Communications Manager (RTMT/AMC/SOAP) | Unified Communications Manager (RIS) | 2556 / TCP | Real-time Information Services (RIS) database client for Cisco RIS |
| Unified Communications Manager (DRS) | Unified Communications Manager (DRS) | 4040 / TCP | DRS Primary Agent |
| Unified Communications Manager (Tomcat) | Unified Communications Manager (SOAP) | 5001/TCP | This port is used by SOAP monitor for Real Time Monitoring Service. |
| Unified Communications Manager (Tomcat) | Unified Communications Manager (SOAP) | 5002/TCP | This port is used by SOAP monitor for Performance Monitor Service. |
| Unified Communications Manager (Tomcat) | Unified Communications Manager (SOAP) | 5003/TCP | This port is used by SOAP monitor for Control Center Service. |
| Unified Communications Manager (Tomcat) | Unified Communications Manager (SOAP) | 5004/TCP | This port is used by SOAP monitor for Log Collection Service. |
| Standard CCM Admin Users / Admin | Unified Communications Manager | 5005 / TCP | This port is used by SOAP CDROnDemand2 services |
| Unified Communications Manager (Tomcat) | Unified Communications Manager (SOAP) | 5007 / TCP | SOAP monitor |
| Unified Communications Manager (RTMT) | Unified Communications Manager (TCTS) | Ephemeral / TCP | Cisco Trace Collection Tool Service (TCTS) -- the back end service for RTMT Trace and Log Central (TLC) |
| Unified Communications Manager (Tomcat) | Unified Communications Manager (TCTS) | 7000, 7001, 7002 / TCP | This port is used for communication between Cisco Trace Collection Tool Service and Cisco Trace Collection servlet. |
| Unified Communications Manager (DB) | Unified Communications Manager (CDLM) | 8001 / TCP | Client database change notification |
| Unified Communications Manager (SDL) | Unified Communications Manager (SDL) | 8002 / TCP | Intracluster communication service |
| Unified Communications Manager (SDL) | Unified Communications Manager (SDL) | 8003 / TCP | Intracluster communication service (to CTI) |
| Unified Communications Manager | CMI Manager | 8004 / TCP | Intracluster communication between Cisco Unified Communications Manager and CMI Manager |
| Unified Communications Manager (Tomcat) | Unified Communications Manager (Tomcat) | 8005 / TCP | Internal listening port used by Tomcat shutdown scripts |
| Unified Communications Manager (Tomcat) | Unified Communications Manager (Tomcat) | 8080 / TCP | Communication between servers used for diagnostic tests |
| Gateway | Unified Communications Manager | 8090 | HTTP Port for communication between CuCM and GW (Cayuga interfae) for Gateway Recording feature. |
| Unified Communications Manager | Gateway |
| Unified Communications Manager (IPSec) | Unified Communications Manager (IPSec) | 8500 / TCP and UDP | Intracluster replication of system data by IPSec Cluster Manager |
| Unified Communications Manager (RIS) | Unified Communications Manager (RIS) | 8888 - 8889 / TCP | RIS Service Manager status request and reply |
| Location Bandwidth Manager (LBM) | Location Bandwidth Manager (LBM) | 9004 / TCP | Intracluster communication between LBMs |
| Unified Communications Manager Publisher | Unified Communications Manager Subscriber | 22 / TCP | Cisco SFTP service. You must open this port when installing a new subscriber. |
| Unified Communications Manager | Unified Communications Manager | 8443 / TCP | Allows access to Control Center - Feature and Network service between nodes. |

| From (Sender) | To (Listener) | Destination Port | Purpose |
|---|---|---|---|
| Endpoint | Unified Communications Manager | 7 | Internet Control Message Protocol (ICMP) This protocol number carries echo-related traffic. It does not constitute a port
                                             as indicated in the column heading. |
| Unified Communications Manager | Endpoint |
| Unified Communications Manager (DRS, Call Detail Record) | SFTP server | 22 / TCP | Send the backup data to the SFTP server. (DRS Local Agent) Send the Call Detail Record data to SFTP server. |
| Endpoint | Unified Communications Manager (DHCP Server) | 67 / UDP | Cisco Unified Communications Manager acting as a DHCP server Note Cisco does not recommend running DHCP server on Cisco Unified Communications Manager. | Note | Cisco does not recommend running DHCP server on Cisco Unified Communications Manager. |
| Note | Cisco does not recommend running DHCP server on Cisco Unified Communications Manager. |
| Unified Communications Manager | DHCP Server | 68 / UDP | Cisco Unified Communications Manager acting as a DHCP client Note Cisco does not recommend running DHCP client on Cisco Unified Communications Manager. Configure Cisco Unified Communications
                                                         Manager with static IP addresses instead.) | Note | Cisco does not recommend running DHCP client on Cisco Unified Communications Manager. Configure Cisco Unified Communications
                                                         Manager with static IP addresses instead.) |
| Note | Cisco does not recommend running DHCP client on Cisco Unified Communications Manager. Configure Cisco Unified Communications
                                                         Manager with static IP addresses instead.) |
| Endpoint or Gateway | Unified Communications Manager | 69, 6969, then Ephemeral / UDP | TFTP service to phones and gateways |
| Endpoint or Gateway | Unified Communications Manager | 6970 / TCP | TFTP between primary and proxy servers. HTTP service from the TFTP server to phones and gateways. |
| Unified Communications Manager | NTP Server | 123 / UDP | Network Time Protocol (NTP) |
| SNMP Server | Unified Communications Manager | 161 / UDP | SNMP service response (requests from management applications) |
| CUCM Server SNMP Primary Agent application | SNMP trap destination | 162 / UDP | SNMP traps |
| SNMP Server | Unified Communications Manager | 199 / TCP | built-in SNMP agent listening port for SMUX support |
| Unified Communications Manager | DHCP Server | 546 / UDP | DHCPv6. DHCP port for IPv6. |
| Unified Communications Manager Serviceability | Location Bandwidth Manager (LBM) | 5546 / TCP | Enhanced Location CAC Serviceability |
| Unified Communications Manager | Location Bandwidth Manager (LBM) | 5547 / TCP | Call Admission requests and bandwidth deductions |
| Unified Communications Manager | Unified Communications Manager | 6161 / UDP | Used for communication between Primary Agent and Native Agent to process Native agent MIB requests |
| Unified Communications Manager | Unified Communications Manager | 6162 / UDP | Used for communication between Primary Agent and Native Agent to forward notifications generated from Native Agent |
| Centralized TFTP | Alternate TFTP | 6970 / TCP | Centralized TFTP File Locator Service |
| Unified Communications Manager | Unified Communications Manager | 7161 / TCP | Used for communication between SNMP Primary Agent and subagents |
| SNMP Server | Unified Communications Manager | 7999 / TCP | Cisco Discovery Protocol (CDP) agent communicates with CDP executable |
| Endpoint | Unified Communications Manager | 443, 8443 / TCP | Used for Cisco User Data Services (UDS) requests |
| Unified Communications Manager | Unified Communications Manager | 9050 / TCP | Service CRS requests through the TAPS residing on Cisco Unified Communications Manager |
| Unified Communications Manager | Unified Communications Manager | 61441 / UDP | Cisco Unified Communications Manager applications send out alarms to this port through UDP. Cisco Unified Communications Manager
                                             MIB agent listens on this port and generates SNMP traps per Cisco Unified Communications Manager MIB definition. |
| Unified Communications Manager | Unified Communications Manager | 5060, 5061 / TCP | Provide trunk-based SIP services |
| Unified Communications Manager | Unified Communications Manager | 7501 | Used by Intercluster Lookup Service (ILS) for certificate based authentication. |
| Unified Communications Manager | Unified Communications Manager | 7502 | Used by ILS for password-based authentication. |
| Unified Communications Manager | Unified Communications Manager | 8006 | Used for signaling between Unified CM and ILS |
| Unified Communications Manager | Unified Communications Manager | 9966 | Used by Cisco push notification service to communicate between the nodes in the cluster when firewall is enabled. |
| Unified Communications Manager | Unified Communications Manager | 9560 | Used by Local Push Notification Service (LPNS). |
| -- | -- | 8000-48200 | ASR and ISR G3 platforms default port range. |
| 16384-32766 | ISR G2 platform default port range. |
| Endpoint | Unified Communications Manager | 514 / UDP (default) 601 / TCP 6514 / TLS | Remote system logging service |

| Note | Cisco does not recommend running DHCP server on Cisco Unified Communications Manager. |
|---|---|

| Note | Cisco does not recommend running DHCP client on Cisco Unified Communications Manager. Configure Cisco Unified Communications
                                                         Manager with static IP addresses instead.) |
|---|---|

| From (Sender) | To (Listener) | Destination Port | Purpose |
|---|---|---|---|
| Unified Communications Manager | External Directory | 389, 636, 3268, 3269 / TCP | Lightweight Directory Access Protocol (LDAP) query to external directory (Active Directory, Netscape Directory) |
| External Directory | Unified Communications Manager | Ephemeral |

| From (Sender) | To (Listener) | Destination Port | Purpose |
|---|---|---|---|
| Browser | Unified Communications Manager | 80, 8080 / TCP | Hypertext Transport Protocol (HTTP) |
| Browser | Unified Communications Manager | 443, 8443 / TCP | Hypertext Transport Protocol over SSL (HTTPS) |
| Browser | Unified Communications Manager | 9463 / TCP | Hypertext Transport Protocol over SSL (HTTPS) allows only TLS1.3 with v6. |

| From (Sender) | To (Listener) | Destination Port | Purpose |
|---|---|---|---|
| Unified Communications Manager QRT RTMT Find and List Phones page Phone Configuration page | Phone | 80 / TCP | Hypertext Transport Protocol (HTTP) |

| From (Sender) | To (Listener) | Destination Port | Purpose |
|---|---|---|---|
| Phone | DNS server | 53/ TCP | Session Initiation Protocol (SIP) phones resolve the Fully Qualified Domain Name (FQDN) using a Domain Name System (DNS) Note By default, some wireless access points block TCP 53 port, which prevents wireless SIP phones from registering when CUCM
                                                         is configured using FQDN. | Note | By default, some wireless access points block TCP 53 port, which prevents wireless SIP phones from registering when CUCM
                                                         is configured using FQDN. |
| Note | By default, some wireless access points block TCP 53 port, which prevents wireless SIP phones from registering when CUCM
                                                         is configured using FQDN. |
| Phone | Unified Communications Manager (TFTP) | 69, then Ephemeral / UDP | Trivial File Transfer Protocol (TFTP) used to download firmware and configuration files |
| Phone | Unified Communications Manager | 2000 / TCP | Skinny Client Control Protocol (SCCP) |
| Phone | Unified Communications Manager | 2443 / TCP | Secure Skinny Client Control Protocol (SCCPS) |
| Phone | Unified Communications Manager | 2445 / TCP | Provide trust verification service to endpoints. |
| Phone | Unified Communications Manager (CAPF) | 3804 / TCP | Certificate Authority Proxy Function (CAPF) listening port for issuing Locally Significant Certificates (LSCs) to IP phones |
| Phone | Unified Communications Manager | 5060 / TCP and UDP | Session Initiation Protocol (SIP) phone |
| Unified Communications Manager | Phone |
| Phone | Unified Communications Manager | 5061 TCP | Secure Session Initiation Protocol (SIPS) phone |
| Unified Communications Manager | Phone |
| Phone | Unified Communications Manager (TFTP) | 6970 TCP | HTTP-based download of firmware and configuration files |
| Phone | Unified Communications Manager (TFTP) | 6971, 6972 / TCP | HTTPS interface to TFTP. Phones use this port to download a secure configuration file from TFTP. |
| Phone | Unified Communications Manager | 8080 / TCP | Phone URLs for XML applications, authentication, directories, services, and so on. You can configure these ports on a per-service
                                             basis. |
| Phone | Unified Communications Manager | 9443 / TCP | Phone use this port for authenticated contact search. |
| Phone | Unified Communications Manager | 9444 | Phones use this port number to use the Headset Management feature. |
| iPhone/iPad (Webex App) | Unified Communications Manager | 9560/Secure WebSocket | Webex App uses this port number for the LPNS feature. |
| IP VMS | Phone | 16384 - 32767 / UDP | Real-Time Protocol (RTP), Secure Real-Time Protocol (SRTP) Note Cisco Unified Communications Manager only uses 24576-32767 although other devices use the full range. | Note | Cisco Unified Communications Manager only uses 24576-32767 although other devices use the full range. |
| Note | Cisco Unified Communications Manager only uses 24576-32767 although other devices use the full range. |
| Phone | IP VMS |

| Note | By default, some wireless access points block TCP 53 port, which prevents wireless SIP phones from registering when CUCM
                                                         is configured using FQDN. |
|---|---|

| Note | Cisco Unified Communications Manager only uses 24576-32767 although other devices use the full range. |
|---|---|

| From (Sender) | To (Listener) | Destination Port | Purpose |
|---|---|---|---|
| Gateway | Unified Communications Manager | 47, 50, 51 | Generic Routing Encapsulation (GRE), Encapsulating Security Payload (ESP), Authentication Header (AH). These protocols numbers
                                             carry encrypted IPSec traffic. They do not constitute a port as indicated in the column heading. |
| Unified Communications Manager | Gateway |
| Gateway | Unified Communications Manager | 500 / UDP | Internet Key Exchange (IKE) for IP Security protocol (IPSec) establishment |
| Unified Communications Manager | Gateway |
| Gateway | Unified Communications Manager (TFTP) | 69, then Ephemeral / UDP | Trivial File Transfer Protocol (TFTP) |
| Unified Communications Manager with Cisco Intercompany Media Engine (CIME) trunk | CIME ASA | 1024-65535 / TCP | Port mapping service. Only used in the CIME off-path deployment model. |
| Gatekeeper | Unified Communications Manager | 1719 / UDP | Gatekeeper (H.225) RAS |
| Gateway | Unified Communications Manager | 1720 / TCP | H.225 signaling services for H.323 gateways and Intercluster Trunk (ICT) |
| Unified Communications Manager | Gateway |
| Gateway | Unified Communications Manager | Ephemeral / TCP | H.225 signaling services on gatekeeper-controlled trunk |
| Unified Communications Manager | Gateway |
| Gateway | Unified Communications Manager | Ephemeral / TCP | H.245 signaling services for establishing voice, video, and data Note The H.245 port used by the remote system depends on the type of gateway. For IOS gateways, the H.245 port range is from 11000 to 65535. | Note | The H.245 port used by the remote system depends on the type of gateway. For IOS gateways, the H.245 port range is from 11000 to 65535. |
| Note | The H.245 port used by the remote system depends on the type of gateway. For IOS gateways, the H.245 port range is from 11000 to 65535. |
| Unified Communications Manager | Gateway |
| Gateway | Unified Communications Manager | 2000 / TCP | Skinny Client Control Protocol (SCCP) |
| Gateway | Unified Communications Manager | 2001 / TCP | Upgrade port for 6608 gateways with Cisco Unified Communications Manager deployments |
| Gateway | Unified Communications Manager | 2002 / TCP | Upgrade port for 6624 gateways with Cisco Unified Communications Manager deployments |
| Gateway | Unified Communications Manager | 2427 / UDP | Media Gateway Control Protocol (MGCP) gateway control |
| Unified Communications Manager | Gateway | 2427 / UDP | Media Gateway Control Protocol (MGCP) gateway control |
| Gateway | Unified Communications Manager | 2428 / TCP | Media Gateway Control Protocol (MGCP) Note For IOS gateways, the source MGCP backhaul TCP port range is from 11000 to 65535. | Note | For IOS gateways, the source MGCP backhaul TCP port range is from 11000 to 65535. |
| Note | For IOS gateways, the source MGCP backhaul TCP port range is from 11000 to 65535. |
| -- | -- | 4000 - 4005 / TCP | These ports are used as phantom Real-Time Transport Protocol (RTP) and Real-Time Transport Control Protocol (RTCP) ports for
                                             audio, video and data channel when Cisco Unified Communications Manager does not have ports for these media. |
| Gateway | Unified Communications Manager | 5060 / TCP and UDP | Session Initiation Protocol (SIP) gateway and Intercluster Trunk (ICT) |
| Unified Communications Manager | Gateway |
| Gateway | Unified Communications Manager | 5061 / TCP | Secure Session Initiation Protocol (SIPS) gateway and Intercluster Trunk (ICT) |
| Unified Communications Manager | Gateway |
| Gateway | Unified Communications Manager | 16384 - 32767 / UDP | Real-Time Protocol (RTP), Secure Real-Time Protocol (SRTP) Note Cisco Unified Communications Manager only uses 24576-32767 although other devices use the full range. | Note | Cisco Unified Communications Manager only uses 24576-32767 although other devices use the full range. |
| Note | Cisco Unified Communications Manager only uses 24576-32767 although other devices use the full range. |
| Unified Communications Manager | Gateway |

| Note | The H.245 port used by the remote system depends on the type of gateway. For IOS gateways, the H.245 port range is from 11000 to 65535. |
|---|---|

| Note | For IOS gateways, the source MGCP backhaul TCP port range is from 11000 to 65535. |
|---|---|

| Note | Cisco Unified Communications Manager only uses 24576-32767 although other devices use the full range. |
|---|---|

| From (Sender) | To (Listener) | Destination Port | Purpose |
|---|---|---|---|
| CTL Client | Unified Communications Manager CTL Provider | 2444 / TCP | Certificate Trust List (CTL) provider listening service in Cisco Unified Communications Manager |
| Cisco Unified Communications App | Unified Communications Manager | 2748 / TCP | CTI application server |
| Cisco Unified Communications App | Unified Communications Manager | 2749 / TCP | TLS connection between CTI applications (JTAPI/TSP) and CTIManager |
| Cisco Unified Communications App | Unified Communications Manager | 2789 / TCP | JTAPI application server |
| Unified Communications Manager Assistant Console | Unified Communications Manager | 2912 / TCP | Cisco Unified Communications Manager Assistant server (formerly IPMA) |
| Unified Communications Manager Attendant Console | Unified Communications Manager | 1103 -1129 / TCP | Cisco Unified Communications Manager Attendant Console (AC) JAVA RMI Registry server |
| Unified Communications Manager Attendant Console | Unified Communications Manager | 1101 / TCP | RMI server sends RMI callback messages to clients on these ports. |
| Unified Communications Manager Attendant Console | Unified Communications Manager | 1102 / TCP | Attendant Console (AC) RMI server bind port -- RMI server sends RMI messages on these ports. |
| Unified Communications Manager Attendant Console | Unified Communications Manager | 3223 / UDP | Cisco Unified Communications Manager Attendant Console (AC) server line state port receives ping and registration message
                                             from, and sends line states to, the attendant console server. |
| Unified Communications Manager Attendant Console | Unified Communications Manager | 3224 / UDP | Cisco Unified Communications Manager Attendant Console (AC) clients register with the AC server for line and device state
                                             information. |
| Unified Communications ManagerAttendant Console | Unified Communications Manager | 4321 / UDP | Cisco Unified Communications Manager Attendant Console (AC) clients register to the AC server for call control. |
| Unified Communications Manager with SAF/CCD | IOS Router running SAF image | 5050 / TCP | Multi-Service IOS Router running EIGRP/SAF Protocol. |
| Unified Communications Manager | Cisco Intercompany Media Engine (IME) Server | 5620 / TCP Cisco recommends a value of 5620 for this port, but you can change the value by executing the add ime vapserver or set ime
                                             vapserver port CLI command on the Cisco IME server. | VAP protocol used to communicate to the Cisco Intercompany Media Engine server. |
| Cisco Unified Communications App | Unified Communications Manager | 8443 / TCP | AXL / SOAP API for programmatic reads from or writes to the Cisco Unified Communications Manager database that third parties
                                             such as billing or telephony management applications use. |

| From (Sender) | To (Listener) | Destination Port | Purpose |
|---|---|---|---|
| CTL Client | TLS Proxy Server | 2444 / TCP | Certificate Trust List (CTL) provider listening service in an ASA firewall |

| From (Sender) | To (Listener) | Destination Port | Purpose |
|---|---|---|---|
| Unified Communications Manager (Cisco Smart Licensing Service) | Cisco Smart Software Manager (CSSM) | 443 / HTTPS | Smart Licensing Service sends the license usage to CSSM to check whether Unified CM is a complaint or not. |

| From (Sender) | To (Listener) | Destination Port | Purpose |
|---|---|---|---|
| Endpoint | HP SIM | 2301 / TCP | HTTP port to HP agent |
| Endpoint | HP SIM | 2381 / TCP | HTTPS port to HP agent |
| Endpoint | Compaq Management Agent | 25375, 25376, 25393 / UDP | COMPAQ Management Agent extension (cmaX) |
| Endpoint | HP SIM | 50000 - 50004 / TCP | HTTPS port to HP SIM |