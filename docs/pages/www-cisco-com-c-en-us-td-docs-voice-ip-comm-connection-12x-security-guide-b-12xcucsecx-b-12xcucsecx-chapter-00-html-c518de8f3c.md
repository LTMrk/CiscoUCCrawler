---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-security-guide-b-12xcucsecx-b-12xcucsecx-chapter-00-html-c518de8f3c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/security/guide/b_12xcucsecx/b_12xcucsecx_chapter_00.html
retrieved_at: 2026-08-21T07:53:51.344981+00:00
---

Security Guide for Cisco Unity Connection Release 12.x

# Security Guide for Cisco Unity Connection Release 12.x

Updated: August 4, 2017

Chapter: IP Communications Required by Cisco Unity Connection

## Chapter: IP Communications Required by Cisco Unity Connection

# IP Communications Required by Cisco Unity Connection

## IP Communications Required by Cisco Unity Connection

### Service
	 Ports

Table
			 1 lists the TCP and UDP ports that are used for inbound connections to
		  the Cisco Unity Connection server, and ports that are used internally by Unity
		  Connection.

Ports and Protocols 1

Operating System Firewall Setting

Executable/Service or Application

Service Account

Comments

TCP: 20500, 20501, 20502, 19003, 1935

Open only between servers in a Unity Connection cluster

CuCsMgr/Unity Connection Conversation Manager

cucsmgr

Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports.

TCP: 21000–21512

Open

CuCsMgr/Unity Connection Conversation Manager

cucsmgr

IP phones must be able to connect to this range of ports on the
					 Unity Connection server for some phone client applications.

TCP: 5000

Open

CuCsMgr/Unity Connection Conversation Manager

cucsmgr

Opened for port-status monitoring read-only connections.
					 Monitoring must be configured in Connection Administration before any data can
					 be seen on this port (Monitoring is off by default).

Administration workstations connect to this port.

TCP and UDP ports allocated by administrator for SIP traffic.

TCP ports 5001, 5002, 5003 and 5004 are open.

Possible ports are 5060–5199

Open

CuCsMgr/Unity Connection Conversation Manager

cucsmgr

Unity Connection SIP Control Traffic handled by conversation
					 manager.

SIP devices must be able to connect to these ports.

TCP: 20055

Open only between servers in a Unity Connection cluster

CuLicSvr/Unity Connection License Server

culic

Restricted to localhost only (no remote connections to this
					 service are needed).

TCP: 1502, 1503 (“ciscounity_tcp” in /etc/services)

Open only between servers in a Unity Connection cluster

unityoninit/Unity Connection DB

root

Servers in a Unity Connection cluster must be able to connect to
					 each other on these database ports.

For external access to the database, use CuDBProxy.

TCP: 143, 993, 7993, 8143, 8993

Open

CuImapSvr/Unity Connection IMAP Server

cuimapsvr

Client workstations must be able to connect to ports 143 and 993
					 for IMAP inbox access, and IMAP over SSL inbox access.

TCP: 25, 8025

Open

CuSmtpSvr/Unity Connection SMTP Server

cusmtpsvr

Servers delivering SMTP to Unity Connection port 25, such as
					 other servers in a UC Digital Network.

TCP: 4904

Blocked; internal use only

SWIsvcMon (Nuance SpeechWorks Service Monitor)

openspeech

Restricted to localhost only (no remote connections to this
					 service are needed).

TCP: 4900:4904

Blocked; internal use only

OSServer/Unity Connection Voice Recognizer

openspeech

Restricted to localhost only (no remote connections to this
					 service are needed).

UDP: 16384–21511

Open

CuMixer/Unity Connection Mixer

cumixer

VoIP devices (phones and gateways) must be able to send traffic
					 to these UDP ports to deliver inbound audio streams.

UDP: 7774–7900

Blocked; internal use only

CuMixer/ Speech recognition RTP

cumixer

Restricted to localhost only (no remote connections to this
					 service are needed).

TCP: 22000

UDP: 22000

Open only between servers in a Unity Connection cluster

CuSrm/ Unity Connection Server Role Manager

cusrm

Cluster SRM RPC.

Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports.

TCP: 22001

UDP: 22001

Open only between servers in a Unity Connection cluster

CuSrm/ Unity Connection Server Role Manager

cusrm

Cluster SRM heartbeat.

Heartbeat event traffic is not encrypted but is MAC secured.

Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports.

TCP: 20532

Open

CuDbProxy/ Unity Connection Database Proxy

cudbproxy

If this service is enabled it allows administrative read/write
					 database connections for off-box clients. For example, some of the
					 ciscounitytools.com tools use this port.

Administrative workstations would connect to this port.

TCP: 22

Open

Sshd

root

Firewall must be open for TCP 22 connections for remote CLI
					 access and serving SFTP in a Unity Connection cluster.

Administrative workstations must be able to connect to a Unity
					 Connection server on this port.

Servers in a Unity Connection cluster must be able to connect to
					 each other on this port.

UDP: 161

Open

Snmpd Platform SNMP Service

root

—

UDP: 500

Open

Raccoon ipsec isakmp (key management) service

root

Using ipsec is optional, and off by default.

If the service is enabled, servers in a Unity Connection cluster
					 must be able to connect to each other on this port.

TCP: 8500

UDP: 8500

Open

clm/cluster management service

root

The cluster manager service is part of the Voice Operating
					 System.

Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports.

UDP: 123

Open

Ntpd Network Time Service

ntp

Network time service is enabled to keep time synchronized
					 between servers in a Unity Connection cluster.

The publisher server can use either the operating system time on
					 the publisher server or the time on a separate NTP server for time
					 synchronization. Subscriber servers always use the publisher server for time
					 synchronization.

Servers in a Unity Connection cluster must be able to connect to
					 each other on this port.

TCP: 5007

Open

Tomcat/Cisco Tomcat (SOAP Service)

tomcat

Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports.

TCP: 1500, 1501

Open only between servers in a Unity Connection cluster

cmoninit/Cisco DB

informix

These database instances contain information for LDAP integrated
					 users, and serviceability data.

Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports.

TCP: 1515

Open only between servers in a Unity Connection cluster

dblrpm/Cisco DB Replication Service

root

Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports.

TCP: 8001

Open only between servers in a Unity Connection cluster

dbmon/Cisco DB Change Notification Port

database

Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports.

TCP: 2555, 2556

Open only between servers in a Unity Connection cluster

RisDC/Cisco RIS Data Collector

ccmservice

Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports.

TCP: 1090, 1099

Open only between servers in a Unity Connection cluster

Amc/Cisco AMC Service (Alert Manager Collector)

ccmservice

Performs back-end serviceability data exchanges

1090: AMC RMI Object Port 1099: AMC RMI Registry Port

Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports.

TCP: 80, 443, 8080, 8443

Open

tomcat/Cisco Tomcat

tomcat

Both client and administrative workstations need to connect to
					 these ports.

Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports for communications that use HTTP-based interactions
					 like REST.

TCP: 8081, 8444

Open only between servers in HTTPS Networking

tomcat/Cisco Tomcat

tomcat

Servers in HTTPS Networking must be able to connect to each
					 other on these ports for communications. Unity Connection HTTPS Directory
					 Feeder service uses these ports for directory synchronization.

TCP: 5001, 8005

Blocked; internal use only

tomcat/Cisco Tomcat

tomcat

Internal tomcat service control and axis ports.

TCP: 32768–61000

UDP: 32768–61000

Open

—

—

Ephemeral port ranges, used by anything with a dynamically
					 allocated client port.

TCP: 7443

Open

jetty/Unity Connection Jetty

jetty

Exchange 2010 and above, single inbox: Jabber and Web Inbox notifications

TCP: 7080

Open

jetty/Unity Connection Jetty

jetty

Exchange 2010 only, single inbox only: EWS notifications of
					 changes to Unity Connection voice messages.

UDP: 9291

Open

CuMbxSync/ Unity Connection Mailbox Sync Service

cumbxsync

Single inbox only: WebDAV notifications of changes to Unity
					 Connection voice messages.

TCP: 6080

Open

CuCsMgr/Unity Connection Conversation Manager

cucsmgr

Video server must be able to connect to Unity Connection on this
					 port for communications.

### Outbound
	 Connections Made by Unity Connection

Table
			 1-2 lists the TCP and UDP ports that Cisco Unity Connection uses to
		  connect with other servers in the network.

Ports and Protocols

Executable

Service Account

Comments

TCP: 2000* (Default SCCP port)

Optionally TCP port 2443* if you use SCCP over TLS.

* Many devices and applications allow configurable RTP port
					 allocations.

CuCsMgr

cucsmgr

Unity Connection SCCP client connection to Cisco Unified CM when
					 they are integrated using SCCP.

UDP: 16384–32767* (RTP)

* Many devices and applications allow configurable RTP port
					 allocations.

CuMixer

cumixer

Unity Connection outbound audio-stream traffic.

UDP: 69

CuCsMgr

cucsmgr

When you are configuring encrypted SCCP, encrypted SIP, or
					 encrypted media streams, Unity Connection makes a TFTP client connection to
					 Cisco Unified CM to download security certificates.

TCP:
					 6972

CuCsMgr

cucsmgr

When you
					 are configuring encrypted SIP or encrypted media streams, Unity Connection
					 makes the HTTPS client connection with Cisco Unified CM to download ITL
					 security certificates.

TCP: 53

UDP: 53

any

any

Used by any process that needs to perform DNS name resolution.

TCP: 53, and either 389 or 636

CuMbxSync

CuCsMgr

tomcat

cumbxsync

cucsmgr

tomcat

Used when Unity Connection is configured for unified messaging
					 with Exchange and one or more unified messaging services are configured to
					 search for Exchange servers.

Unity Connection uses port 389 when you select LDAP for the
					 protocol used to communicate with domain controllers.

Unity Connection uses port 636 when you select LDAPS for the
					 protocol used to communicate with domain controllers.

TCP: 80, 443 (HTTP and HTTPS)

CuMbxSync

CuCsMgr

tomcat

cumbxsync

cucsmgr

tomcat

TCP: 80, 443, 8080, and 8443 (HTTP and HTTPS)

CuCsMgr

tomcat

cucsmgr

tomcat

Unity Connection makes HTTP and HTTPS client connections to:

Other Unity Connection servers for Digital Networking automatic
						  joins.

Cisco Unified CM for AXL user synchronization.

TCP: 143, 993 (IMAP and IMAP over SSL)

CuCsMgr

cucsmgr

Unity Connection makes IMAP connections to Microsoft Exchange
					 servers to perform text-to-speech conversions of email messages in a Unity
					 Connection user’s Exchange mailbox.

TCP: 25 (SMTP)

CuSmtpSvr

cusmtpsvr

Unity Connection makes client connections to SMTP servers and
					 smart hosts, or to other Unity Connection servers for features such as VPIM
					 networking or Unity Connection Digital Networking.

TCP: 21 (FTP)

ftp

root

The installation framework performs FTP connections to download
					 upgrade media when an FTP server is specified.

TCP: 22 (SSH/SFTP)

CiscoDRFMaster

sftp

drf

root

The Disaster Recovery Framework performs SFTP connections to
					 network backup servers to perform backups and retrieve backups for restoration.

The installation framework performs SFTP connections to download
					 upgrade media when an SFTP server is specified.

UDP: 67 (DHCP/BootP)

dhclient

root

Client connections made for obtaining DHCP addressing.

Although DHCP is supported, Cisco highly recommends that you
					 assign static IP addresses to Unity Connection servers.

TCP: 123

UDP: 123 (NTP)

Ntpd

root

Client connections made for NTP clock synchronization.

UDP: 514

TCP: 601

Syslog/Cisco Syslog Server

syslog

Unity
					 Connection server must be able to send audit logs to remote syslog server
					 through these ports

### Securing Transport
	 Layer

Unity Connection
		uses Transport Layer Security(TLS) protocol and Secure Sockets Layer(SSL)
		protocol for signaling and client server communication. Unity Connection
		supports TLS 1.0, TLS 1.1 and TLS 1.2 for secure communication across various
		interfaces of Cisco Unity Connection. TLS 1.2 is the most secure and
		authenticated protocol for communication.

Depending upon the
		organization security policies and deployment capabilities, Unity Connection
		12.0(1) and later allows you to configure the minimum TLS version. After
		configuring the minimum version of TLS, Unity Connection supports the minimum
		configured version and higher versions of TLS. For example, if you configure
		TLS 1.1 as a minimum version of TLS, Unity Connection uses TLS 1.1 and higher
		versions for communication and rejects the request for a TLS version that is
		lower than the configured value. By default, TLS 1.0 is configured.

Before configuring
		minimum TLS version, ensure that all the interfaces of Unity Connection must be
		secured and use configured minimum TLS version or higher version for
		communication. However, you can configure the minimum TLS version for inbound
		interfaces of Unity Connection.

Table 3 lists the
		supported interfaces for which you can configure the minimum TLS version on
		Unity Connection.

Executable/Service or Application

Service
				  Account

Both client
				  and administrative workstations must connect to these ports.

Servers in a
				  Unity Connection cluster must be able to connect to each other on these ports
				  for communications that use HTTP-based interactions like REST.

Exchange
				  2010 and above, single inbox: Jabber and Web Inbox notifications

Client
				  workstations must be able to connect to port 993 for IMAP over SSL inbox
				  access.

Servers
				  delivering SMTP to Unity Connection port 25, such as other servers in a UC
				  Digital Network.

Unity
				  Connection SIP Control Traffic handled by conversation manager. SIP devices
				  must be able to connect to these ports.

CuMbxSync

CuCsMgr

tomcat

cumbxsync

cucsmgr

tomcat

Unity
				  Connection uses port 636 when you select LDAPS for the protocol used to
				  communicate with domain controllers.

For more information
		on supported inbound interfaces of Cisco Unity Connection, see " Service
		  Ports " section.

- Configuring
	 Minimum TLS Version

#### Configuring
	 Minimum TLS Version

To configure the
		minimum TLS version in Cisco Unity Connection, execute the following CLI
		command:

- set tls min-version <tls
		  minVersion>

In cluster, you must
		execute the CLI command on both publisher and subscriber.

In addition to this,
		you can execute the following CLI command to check the configured value of
		minimum TLS version on Unity Connection:

- show tls min-version

For detailed
		information on the CLI, see Command Line
		  Interface Reference Guide for Cisco Unified Communications Solutions available at http:/​​/​​www.cisco.com/​​c/​​en/​​us/​​support/​​unified-communications/​​unified-communications-manager-callmanager/​​products-maintenance-guides-list.html .

| Ports and Protocols 1 | Operating System Firewall Setting | Executable/Service or Application | Service Account | Comments |
|---|---|---|---|---|
| TCP: 20500, 20501, 20502, 19003, 1935 | Open only between servers in a Unity Connection cluster | CuCsMgr/Unity Connection Conversation Manager | cucsmgr | Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports. |
| TCP: 21000–21512 | Open | CuCsMgr/Unity Connection Conversation Manager | cucsmgr | IP phones must be able to connect to this range of ports on the
					 Unity Connection server for some phone client applications. |
| TCP: 5000 | Open | CuCsMgr/Unity Connection Conversation Manager | cucsmgr | Opened for port-status monitoring read-only connections.
					 Monitoring must be configured in Connection Administration before any data can
					 be seen on this port (Monitoring is off by default). Administration workstations connect to this port. |
| TCP and UDP ports allocated by administrator for SIP traffic. TCP ports 5001, 5002, 5003 and 5004 are open. Possible ports are 5060–5199 | Open | CuCsMgr/Unity Connection Conversation Manager | cucsmgr | Unity Connection SIP Control Traffic handled by conversation
					 manager. SIP devices must be able to connect to these ports. |
| TCP: 20055 | Open only between servers in a Unity Connection cluster | CuLicSvr/Unity Connection License Server | culic | Restricted to localhost only (no remote connections to this
					 service are needed). |
| TCP: 1502, 1503 (“ciscounity_tcp” in /etc/services) | Open only between servers in a Unity Connection cluster | unityoninit/Unity Connection DB | root | Servers in a Unity Connection cluster must be able to connect to
					 each other on these database ports. For external access to the database, use CuDBProxy. |
| TCP: 143, 993, 7993, 8143, 8993 | Open | CuImapSvr/Unity Connection IMAP Server | cuimapsvr | Client workstations must be able to connect to ports 143 and 993
					 for IMAP inbox access, and IMAP over SSL inbox access. |
| TCP: 25, 8025 | Open | CuSmtpSvr/Unity Connection SMTP Server | cusmtpsvr | Servers delivering SMTP to Unity Connection port 25, such as
					 other servers in a UC Digital Network. |
| TCP: 4904 | Blocked; internal use only | SWIsvcMon (Nuance SpeechWorks Service Monitor) | openspeech | Restricted to localhost only (no remote connections to this
					 service are needed). |
| TCP: 4900:4904 | Blocked; internal use only | OSServer/Unity Connection Voice Recognizer | openspeech | Restricted to localhost only (no remote connections to this
					 service are needed). |
| UDP: 16384–21511 | Open | CuMixer/Unity Connection Mixer | cumixer | VoIP devices (phones and gateways) must be able to send traffic
					 to these UDP ports to deliver inbound audio streams. |
| UDP: 7774–7900 | Blocked; internal use only | CuMixer/ Speech recognition RTP | cumixer | Restricted to localhost only (no remote connections to this
					 service are needed). |
| TCP: 22000 UDP: 22000 | Open only between servers in a Unity Connection cluster | CuSrm/ Unity Connection Server Role Manager | cusrm | Cluster SRM RPC. Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports. |
| TCP: 22001 UDP: 22001 | Open only between servers in a Unity Connection cluster | CuSrm/ Unity Connection Server Role Manager | cusrm | Cluster SRM heartbeat. Heartbeat event traffic is not encrypted but is MAC secured. Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports. |
| TCP: 20532 | Open | CuDbProxy/ Unity Connection Database Proxy | cudbproxy | If this service is enabled it allows administrative read/write
					 database connections for off-box clients. For example, some of the
					 ciscounitytools.com tools use this port. Administrative workstations would connect to this port. |
| TCP: 22 | Open | Sshd | root | Firewall must be open for TCP 22 connections for remote CLI
					 access and serving SFTP in a Unity Connection cluster. Administrative workstations must be able to connect to a Unity
					 Connection server on this port. Servers in a Unity Connection cluster must be able to connect to
					 each other on this port. |
| UDP: 161 | Open | Snmpd Platform SNMP Service | root | — |
| UDP: 500 | Open | Raccoon ipsec isakmp (key management) service | root | Using ipsec is optional, and off by default. If the service is enabled, servers in a Unity Connection cluster
					 must be able to connect to each other on this port. |
| TCP: 8500 UDP: 8500 | Open | clm/cluster management service | root | The cluster manager service is part of the Voice Operating
					 System. Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports. |
| UDP: 123 | Open | Ntpd Network Time Service | ntp | Network time service is enabled to keep time synchronized
					 between servers in a Unity Connection cluster. The publisher server can use either the operating system time on
					 the publisher server or the time on a separate NTP server for time
					 synchronization. Subscriber servers always use the publisher server for time
					 synchronization. Servers in a Unity Connection cluster must be able to connect to
					 each other on this port. |
| TCP: 5007 | Open | Tomcat/Cisco Tomcat (SOAP Service) | tomcat | Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports. |
| TCP: 1500, 1501 | Open only between servers in a Unity Connection cluster | cmoninit/Cisco DB | informix | These database instances contain information for LDAP integrated
					 users, and serviceability data. Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports. |
| TCP: 1515 | Open only between servers in a Unity Connection cluster | dblrpm/Cisco DB Replication Service | root | Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports. |
| TCP: 8001 | Open only between servers in a Unity Connection cluster | dbmon/Cisco DB Change Notification Port | database | Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports. |
| TCP: 2555, 2556 | Open only between servers in a Unity Connection cluster | RisDC/Cisco RIS Data Collector | ccmservice | Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports. |
| TCP: 1090, 1099 | Open only between servers in a Unity Connection cluster | Amc/Cisco AMC Service (Alert Manager Collector) | ccmservice | Performs back-end serviceability data exchanges 1090: AMC RMI Object Port 1099: AMC RMI Registry Port Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports. |
| TCP: 80, 443, 8080, 8443 | Open | tomcat/Cisco Tomcat | tomcat | Both client and administrative workstations need to connect to
					 these ports. Servers in a Unity Connection cluster must be able to connect to
					 each other on these ports for communications that use HTTP-based interactions
					 like REST. Note These ports support both
					 the IPv4 and IPv6 addresses. However, the IPv6 address works only when
					 Connection platform is configured in Dual (IPv4/IPv6) mode. Cisco Unity
					 Connection Survivable Remote Site Voicemail SRSV supports these ports for IP
					 communication. | Note | These ports support both
					 the IPv4 and IPv6 addresses. However, the IPv6 address works only when
					 Connection platform is configured in Dual (IPv4/IPv6) mode. Cisco Unity
					 Connection Survivable Remote Site Voicemail SRSV supports these ports for IP
					 communication. |
| Note | These ports support both
					 the IPv4 and IPv6 addresses. However, the IPv6 address works only when
					 Connection platform is configured in Dual (IPv4/IPv6) mode. Cisco Unity
					 Connection Survivable Remote Site Voicemail SRSV supports these ports for IP
					 communication. |
| TCP: 8081, 8444 | Open only between servers in HTTPS Networking | tomcat/Cisco Tomcat | tomcat | Servers in HTTPS Networking must be able to connect to each
					 other on these ports for communications. Unity Connection HTTPS Directory
					 Feeder service uses these ports for directory synchronization. Note Unity Connection HTTPS
					 Directory Feeder service supports only IPv4 mode. | Note | Unity Connection HTTPS
					 Directory Feeder service supports only IPv4 mode. |
| Note | Unity Connection HTTPS
					 Directory Feeder service supports only IPv4 mode. |
| TCP: 5001, 8005 | Blocked; internal use only | tomcat/Cisco Tomcat | tomcat | Internal tomcat service control and axis ports. |
| TCP: 32768–61000 UDP: 32768–61000 | Open | — | — | Ephemeral port ranges, used by anything with a dynamically
					 allocated client port. |
| TCP: 7443 | Open | jetty/Unity Connection Jetty | jetty | Exchange 2010 and above, single inbox: Jabber and Web Inbox notifications Note You
						can open the port using CLI command. | Note | You
						can open the port using CLI command. |
| Note | You
						can open the port using CLI command. |
| TCP: 7080 | Open | jetty/Unity Connection Jetty | jetty | Exchange 2010 only, single inbox only: EWS notifications of
					 changes to Unity Connection voice messages. |
| UDP: 9291 | Open | CuMbxSync/ Unity Connection Mailbox Sync Service | cumbxsync | Single inbox only: WebDAV notifications of changes to Unity
					 Connection voice messages. |
| TCP: 6080 | Open | CuCsMgr/Unity Connection Conversation Manager | cucsmgr | Video server must be able to connect to Unity Connection on this
					 port for communications. |

| Note | These ports support both
					 the IPv4 and IPv6 addresses. However, the IPv6 address works only when
					 Connection platform is configured in Dual (IPv4/IPv6) mode. Cisco Unity
					 Connection Survivable Remote Site Voicemail SRSV supports these ports for IP
					 communication. |
|---|---|

| Note | Unity Connection HTTPS
					 Directory Feeder service supports only IPv4 mode. |
|---|---|

| Note | You
						can open the port using CLI command. |
|---|---|

| Ports and Protocols | Executable | Service Account | Comments |
|---|---|---|---|
| TCP: 2000* (Default SCCP port) Optionally TCP port 2443* if you use SCCP over TLS. * Many devices and applications allow configurable RTP port
					 allocations. | CuCsMgr | cucsmgr | Unity Connection SCCP client connection to Cisco Unified CM when
					 they are integrated using SCCP. |
| UDP: 16384–32767* (RTP) * Many devices and applications allow configurable RTP port
					 allocations. | CuMixer | cumixer | Unity Connection outbound audio-stream traffic. |
| UDP: 69 | CuCsMgr | cucsmgr | When you are configuring encrypted SCCP, encrypted SIP, or
					 encrypted media streams, Unity Connection makes a TFTP client connection to
					 Cisco Unified CM to download security certificates. |
| TCP:
					 6972 | CuCsMgr | cucsmgr | When you
					 are configuring encrypted SIP or encrypted media streams, Unity Connection
					 makes the HTTPS client connection with Cisco Unified CM to download ITL
					 security certificates. |
| TCP: 53 UDP: 53 | any | any | Used by any process that needs to perform DNS name resolution. |
| TCP: 53, and either 389 or 636 | CuMbxSync CuCsMgr tomcat | cumbxsync cucsmgr tomcat | Used when Unity Connection is configured for unified messaging
					 with Exchange and one or more unified messaging services are configured to
					 search for Exchange servers. Unity Connection uses port 389 when you select LDAP for the
					 protocol used to communicate with domain controllers. Unity Connection uses port 636 when you select LDAPS for the
					 protocol used to communicate with domain controllers. |
| TCP: 80, 443 (HTTP and HTTPS) | CuMbxSync CuCsMgr tomcat | cumbxsync cucsmgr tomcat | Note These ports support both the IPv4 and IPv6 addresses. | Note | These ports support both the IPv4 and IPv6 addresses. |
| Note | These ports support both the IPv4 and IPv6 addresses. |
| TCP: 80, 443, 8080, and 8443 (HTTP and HTTPS) | CuCsMgr tomcat | cucsmgr tomcat | Unity Connection makes HTTP and HTTPS client connections to: Other Unity Connection servers for Digital Networking automatic
						  joins. Cisco Unified CM for AXL user synchronization. Note These ports support both the IPv4 and IPv6 addresses. Note Cisco Unity Connection Survivable Remote Site Voicemail SRSV
						  supports these ports for IP communication. | Note | These ports support both the IPv4 and IPv6 addresses. | Note | Cisco Unity Connection Survivable Remote Site Voicemail SRSV
						  supports these ports for IP communication. |
| Note | These ports support both the IPv4 and IPv6 addresses. |
| Note | Cisco Unity Connection Survivable Remote Site Voicemail SRSV
						  supports these ports for IP communication. |
| TCP: 143, 993 (IMAP and IMAP over SSL) | CuCsMgr | cucsmgr | Unity Connection makes IMAP connections to Microsoft Exchange
					 servers to perform text-to-speech conversions of email messages in a Unity
					 Connection user’s Exchange mailbox. |
| TCP: 25 (SMTP) | CuSmtpSvr | cusmtpsvr | Unity Connection makes client connections to SMTP servers and
					 smart hosts, or to other Unity Connection servers for features such as VPIM
					 networking or Unity Connection Digital Networking. |
| TCP: 21 (FTP) | ftp | root | The installation framework performs FTP connections to download
					 upgrade media when an FTP server is specified. |
| TCP: 22 (SSH/SFTP) | CiscoDRFMaster sftp | drf root | The Disaster Recovery Framework performs SFTP connections to
					 network backup servers to perform backups and retrieve backups for restoration. The installation framework performs SFTP connections to download
					 upgrade media when an SFTP server is specified. |
| UDP: 67 (DHCP/BootP) | dhclient | root | Client connections made for obtaining DHCP addressing. Although DHCP is supported, Cisco highly recommends that you
					 assign static IP addresses to Unity Connection servers. |
| TCP: 123 UDP: 123 (NTP) | Ntpd | root | Client connections made for NTP clock synchronization. |
| UDP: 514 TCP: 601 | Syslog/Cisco Syslog Server | syslog | Unity
					 Connection server must be able to send audit logs to remote syslog server
					 through these ports |

| Note | These ports support both the IPv4 and IPv6 addresses. |
|---|---|

| Note | These ports support both the IPv4 and IPv6 addresses. |
|---|---|

| Note | Cisco Unity Connection Survivable Remote Site Voicemail SRSV
						  supports these ports for IP communication. |
|---|---|

| Ports | Executable/Service or Application | Service
				  Account | Comments |
|---|---|---|---|
| 8443, 443, 8444 | tomcat/Cisco Tomcat | tomcat | Both client
				  and administrative workstations must connect to these ports. Servers in a
				  Unity Connection cluster must be able to connect to each other on these ports
				  for communications that use HTTP-based interactions like REST. |
| 7443 | jetty/Unity Connection Jetty | jetty | Exchange
				  2010 and above, single inbox: Jabber and Web Inbox notifications |
| 993 | CuImapSvr/Unity Connection IMAP Server | cuimapsvr | Client
				  workstations must be able to connect to port 993 for IMAP over SSL inbox
				  access. |
| 25 | CuSmtpSvr/Unity Connection SMTP Server | cusmtpsvr | Servers
				  delivering SMTP to Unity Connection port 25, such as other servers in a UC
				  Digital Network. |
| 5061-5199 | CuCsMgr/Unity Connection Conversation Manager | cucsmgr | Unity
				  Connection SIP Control Traffic handled by conversation manager. SIP devices
				  must be able to connect to these ports. |
| LDAP (outbound interface) | CuMbxSync CuCsMgr tomcat | cumbxsync cucsmgr tomcat | Unity
				  Connection uses port 636 when you select LDAPS for the protocol used to
				  communicate with domain controllers. |

| Caution | After configuring minimum TLS version, the Cisco Unity
		  Connection server restart automatically. |
|---|---|