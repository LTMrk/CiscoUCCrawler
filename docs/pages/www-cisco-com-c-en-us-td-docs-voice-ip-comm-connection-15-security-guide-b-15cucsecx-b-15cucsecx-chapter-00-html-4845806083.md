---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-security-guide-b-15cucsecx-b-15cucsecx-chapter-00-html-4845806083
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/security/guide/b_15cucsecx/b_15cucsecx_chapter_00.html
retrieved_at: 2026-08-16T18:01:04.213844+00:00
---

Security Guide for Cisco Unity Connection Release 15

# Security Guide for Cisco Unity Connection Release 15

Updated: June 11, 2025

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

Open only between servers in a Unity Connection cluster. Port 1935 is blocked and is for internal use only.

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

If this service is enabled it allows administrative read/write database connections for off-box clients.

Administrative workstations would connect to this port.

TCP: 27000

Blocked; internal use only

Connection Voice Recognizer Service

lmgrd

Nuance License Server service on Unity Connection will use port 27000 in listening mode.

Restricted to localhost only (no remote connections to this service are needed).

TCP: 22

Open

Sshd

root

Firewall must be open for TCP 22 connections for remote CLI access and serving SFTP in a Unity Connection cluster.

Administrative workstations must be able to connect to a Unity Connection server on this port.

Servers in a Unity Connection cluster must be able to connect to each other on this port.

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

Blocked; internal use only.

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

haproxy/Cisco HAProxy

haproxy

Both client and administrative workstations need to connect to
                                             					 these ports.

Servers in a Unity Connection cluster must be able to connect to
                                             					 each other on these ports for communications that use HTTP-based interactions
                                             					 like REST.

TCP: 8081, 8444

Open only between servers in HTTPS Networking

haproxy/Cisco HAProxy

haproxy

Servers in HTTPS Networking must be able to connect to each
                                             					 other on these ports for communications. Unity Connection HTTPS Directory
                                             					 Feeder service uses these ports for directory synchronization.

TCP: 5001-5004, 8005

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

TCP:
                                             					 7443

Open

jetty/Unity Connection Jetty

jetty

Secure
                                             					 Jabber and Web Inbox notifications

TCP: 7080

Open

jetty/Unity Connection Jetty

jetty

Exchange 2010 only, single inbox only: Jabber and Web Inbox
                                             					 EWS notifications of changes to Unity Connection voice messages.

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

TCP: 25,587 (SMTP)

CuSmtpSvr

cusmtpsvr

Cisco Unity Connection supports STARTTLS over port 25. With Release 14SU2 and later, STARTTLS is also supported over port
                                                            587.

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

Unity Connection uses Transport Layer Security(TLS) protocol and Secure Sockets Layer(SSL) protocol for signaling and client
                              server communication. Unity Connection supports TLS 1.0, TLS 1.1, TLS 1.2 and TLS 1.3 for secure communication across various
                              interfaces of Cisco Unity Connection.

(Applicable for Releases before 15 SU2) TLS 1.2 is the most secure and authenticated protocol for communication.

(Applicable for Release 15 SU2 and later) TLS 1.3 is the most secure and authenticated protocol for communication.

Depending upon the organization security policies and deployment capabilities, Unity Connection 11.5(1) SU3 and later allows
                              you to configure the minimum TLS version. After configuring the minimum version of TLS, Unity Connection supports the minimum
                              configured version and higher versions of TLS. For example, if you configure TLS 1.1 as a minimum version of TLS, Unity Connection
                              uses TLS 1.1 and higher versions for communication and rejects the request for a TLS version that is lower than the configured
                              value. By default, TLS 1.0 is configured.

Before configuring
                              		minimum TLS version, ensure that all the interfaces of Unity Connection must be
                              		secured and use configured minimum TLS version or higher version for
                              		communication. However, you can configure the minimum TLS version for inbound
                              		interfaces of Unity Connection.

Table 3 lists the
                              		supported interfaces for which you can configure the minimum TLS version on
                              		Unity Connection.

Executable/Service or Application

Service Account

Cisco HAProxy

haproxy

Both client and administrative workstations must connect to these ports.

Servers in a Unity Connection cluster must be able to connect to each other on these ports for communications that use HTTP-based
                                          interactions like REST.

Secure Jabber and Web Inbox notifications.

Cisco Unity Connection releases before 15 SU2, supports only TLS version 1.2 for secure communication.

Cisco Unity Connection 15 SU2 and later releases, supports TLS version 1.2 and 1.3 for secure communication.

Client workstations must be able to connect to port 993 for IMAP over SSL inbox access.

Servers delivering SMTP to Unity Connection port 25 or 587, such as other servers in a UC Digital Network.

Unity Connection SIP Control Traffic handled by conversation manager. SIP devices must be able to connect to these ports.

CuMbxSync

CuCsMgr

tomcat

cumbxsync

cucsmgr

tomcat

Unity Connection uses port 636 when you select LDAPS for the protocol used to communicate with domain controllers.

20536

Cisco HAProxy

haproxy

If this service is enabled it allows administrative secure read/write database connections for off-box clients.

For more information
                              		on supported inbound interfaces of Cisco Unity Connection, see " Service
                                 		  Ports " section.

#### TLS 1.3 (Applicable to Release 15 SU2 or later)

TLS 1.3, as defined in RFC 8446, is the highest version of the Transport Layer Security (TLS) protocol. It aims to improve
                                 upon its predecessors, particularly TLS 1.2. TLS 1.3 achieves this by addressing security vulnerabilities, enhancing performance,
                                 and streamlining the handshake process.

One of the key improvements in TLS 1.3 is the reduction in handshake latency. It significantly enhances the performance of
                                    time-sensitive applications. Moreover, TLS 1.3 also reduces round-trip times (RTT), by further optimizing the connection establishment
                                    process. TLS 1.3 has dropped support for older and less secure cryptographic algorithms.

Reduced Handshake Latency —TLS 1.3 minimizes round trips during the handshake process. Hence, it enhances performance, especially for latency-sensitive
                                          applications.

Enhanced Security —TLS 1.3 mandates the use of modern cryptographic algorithms. It includes Elliptic Curve Diffie-Hellman (ECDH) for key exchange
                                          and Authenticated Encryption with Associated Data (AEAD) for data encryption and integrity protection. This strengthens security
                                          against various attacks.

Perfect Forward Secrecy (PFS) —By default, TLS 1.3 ensures that even if long-term keys are compromised, past communications remain secure. Hence, it improves
                                          privacy and security.

Encrypted Handshake Messages —TLS 1.3 encrypts handshake messages to prevent passive eavesdropping attacks and ensures confidentiality.

Support for Stronger Algorithms —TLS 1.3 eliminates support for outdated cryptographic algorithms and cipher suites. It reduces the risk of attacks, such
                                          as downgrade attacks and cryptographic vulnerabilities.

Signature Algorithm Usage —TLS 1.3 limits the use of RSA signatures and promotes modern signature algorithms like ECDSA and DSA. However, TLS 1.2 relies
                                          more on RSA signatures.

Cipher Suite Reduction —TLS 1.3 reduces the number of supported cipher suites. It focuses on authenticated encryption algorithms like AES-GCM and
                                          ChaCha20-Poly1305. In comparison, TLS 1.2 supports a broader range of cipher suites, including some less secure options.

Security Enhancements —TLS 1.3 introduces features such as PFS by default and encrypted handshake messages. These features are absent in TLS 1.2.
                                          They enhance overall security and privacy.

Certificate Selection —In TLS 1.2, the server selects the certificate based on the key algorithm in the cipher suite negotiated during the handshake.
                                          However, in TLS 1.3, the server determines the certificate based on the supported signature algorithms advertised by the client.
                                          It ensures smoother compatibility and a more secure communication environment.

Below are the list of ciphers supported by TLS 1.3:

- TLS_AES_256_GCM_SHA384

- TLS_CHACHA20_POLY1305_SHA256

- TLS_AES_128_GCM_SHA256

Install and Upgrade Considerations

For Fresh Install, the minimum supported TLS version is 1.2. Here, the TLS versions 1.0 and 1.1 are disabled by default. Run
                                 the set tls min-version command in case you want to configure the minimum TLS version as 1.0 or 1.1.

For upgrade and/or migration scenarios, the supported TLS versions are TLS 1.0, 1.1, 1.2, and 1.3. The minimum TLS version
                                 is carried forward to the upgraded or migrated version. In case your application does not support TLS 1.3, it connects with
                                 the highest supported TLS version of the client and server applications. For e.g., if TLS 1.1 is set as minimum TLS version
                                 in Unity Connection 14 version, post upgrade or migration to Unity Connection 15 SU2 minimum TLS would be still set to TLS
                                 1.1

Migration Considerations

TLS 1.3 uses Signature algorithms to choose between RSA or ECDSA signed certificates and evaluates the certificates offered
                                 from the server side before it decides on the certificate type. TLS 1.3 does not have a separate Cipher Management settings
                                 page. It relies on the existing Enterprise parameters, HTTP Ciphers, and the TLS Cipher settings.

SIP and other non-HTTP interfaces will not have an exclusive RSA only mode for the TLS Cipher General Configuration settings. Hence, these interfaces continue to offer both the signature algorithms.

All HTTP inbound interfaces use HTTP Ciphers in the Enterprise Parameters Configuration page to load the RSA or RSA and ECDSA
                                 certificates in its context while opening the port for configured for inbound traffic. HTTP Ciphers is set to 'RSA only' as
                                 the default setting. From 15 SU2 onwards, by default, only RSA certificate will be loaded for HTTPs traffic there by limiting
                                 TLS 1.3 and/or 1.2 to use only RSA signed certificates.

Prior to Release 15SU2, while using TLS for inbound HTTPS traffic, the Cipher Management settings page takes precedence over
                                 the HTTP Cipher Enterprise parameter. Hence, to create an ECDSA only HTTPS traffic, administrators had to configure the Cipher
                                 Management page with only the ECDSA Ciphers and keep the HTTP Cipher Settings at its default configuration. Post upgrade,
                                 this HTTPS connection sends only RSA certificate along with the EC Ciphers and will be loaded in the HTTPS inbound context
                                 leading to mismatch and connection failures.

Direct Standard Upgrades—To overcome this failure during the Direct Standard Upgrades upgrade, it automatically switches the
                                       HTTP Cipher Enterprise parameter to All Supported EC and RSA Ciphers as part of the upgrade if a mismatch is detected. This loads both the RSA and ECDSA certificates.

Fresh install with Data Import—For Fresh install with Data Import migration method, you have to switch the HTTP Cipher Enterprise
                                       Parameter manually to All Supported EC and RSA Ciphers prior to upgrading to Release 15 SU2 and above.

SIP Trunk and Phone Security Profile —If you set the Device Security Mode to Authenticated , the phones will switch to a TLS version lower than 1.3. When the minimum supported TLS version on the Unity Connection is
                                          set to 1.3, phones and SIP trunks with the Authenticated Device Security Mode is not supported.

Managing HTTPS Ciphers for SMTP and Jetty

The HTTPS ciphers option previously managed ciphers for TLS 1.2 and earlier. We have now expanded its functionality to include
                                 certificate preferences based on signature algorithms, with specific implementations for both the SMTP and Jetty servers.

If “RSA Ciphers Only” is selected under the Enterprise Parameter for HTTPS Ciphers, the SMTP cache will contain only RSA certificates.

If “All Supported EC and RSA Ciphers” is selected, the cache will contain both ECDSA and RSA certificates.

When "RSA Ciphers Only" is selected, Jetty will prioritize and exclusively use RSA certificates for negotiation.

When "All Supported EC and RSA Ciphers" is selected, ECDSA certificates will take priority over RSA certificates. However,
                                             both types of certificates will be offered, and the negotiation will proceed based on the signature algorithm order specified
                                             by the client.

TLS 1.3 is not supported for below Interfaces:

- Cisco Unity Tools

- Cisco Smart Software Licensing (CSSM)

- Voice Mail for Outlook (VMO)

- Chrome Extension for Gmail

- Microsoft Exchange Server

- Microsoft Office 365

- Microsoft Outlook

- If you are using the above interfaces except CSSM, do not set TLS minimum version to 1.3. It is recommended to set it to any
                                                lower version for smooth commnication between Unity Connection and these interfaces.

- Cisco Smart Software Licensing (CSSM) will work on TLS 1.2 when minimum TLS version on Unity Connection is set as 1.3.

#### Configuring
                              	 Minimum TLS Version

To configure the
                                 		minimum TLS version in Cisco Unity Connection, execute the following CLI
                                 		command:

- set tls min-version <tls
                                       		  minVersion>

(Applicable for Releases before 15 SU2) In cluster, you must execute the CLI command on both publisher and subscriber.

(Applicable for Release 15 SU2 and later) In cluster, you must execute the CLI command only on publisher and restart the subscriber.

In addition to this,
                                 		you can execute the following CLI command to check the configured value of
                                 		minimum TLS version on Unity Connection:

- show tls min-version

For detailed
                                 		information on the CLI, see Command Line
                                    		  Interface Reference Guide for Cisco Unified Communications Solutions available at http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​products-maintenance-guides-list.html .

| Ports and Protocols 1 | Operating System Firewall Setting | Executable/Service or Application | Service Account | Comments |
|---|---|---|---|---|
| TCP: 20500, 20501, 20502, 19003, 1935 | Open only between servers in a Unity Connection cluster. Port 1935 is blocked and is for internal use only. | CuCsMgr/Unity Connection Conversation Manager | cucsmgr | Servers in a Unity Connection cluster must be able to connect to
                                             					 each other on these ports. |
| TCP: 21000–21512 | Open | CuCsMgr/Unity Connection Conversation Manager | cucsmgr | IP phones must be able to connect to this range of ports on the
                                             					 Unity Connection server for some phone client applications. |
| TCP: 5000 | Open | CuCsMgr/Unity Connection Conversation Manager | cucsmgr | Opened for port-status monitoring read-only connections.
                                             					 Monitoring must be configured in Connection Administration before any data can
                                             					 be seen on this port (Monitoring is off by default). Administration workstations connect to this port. |
| TCP and UDP ports allocated by administrator for SIP traffic. Possible ports are 5060–5199 | Open | CuCsMgr/Unity Connection Conversation Manager | cucsmgr | Unity Connection SIP Control Traffic handled by conversation
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
| TCP: 20532 | Open | CuDbProxy/ Unity Connection Database Proxy | cudbproxy | If this service is enabled it allows administrative read/write database connections for off-box clients. Administrative workstations would connect to this port. Note (Applicable for Release 15 SU2 and later) Only Cisco Unity Connection tools are supported to use this port. Any third-party tools, connecting to this port are recommended
                                                      to use port 20536. | Note | (Applicable for Release 15 SU2 and later) Only Cisco Unity Connection tools are supported to use this port. Any third-party tools, connecting to this port are recommended
                                                      to use port 20536. |
| Note | (Applicable for Release 15 SU2 and later) Only Cisco Unity Connection tools are supported to use this port. Any third-party tools, connecting to this port are recommended
                                                      to use port 20536. |
| TCP: 27000 | Blocked; internal use only | Connection Voice Recognizer Service | lmgrd | Nuance License Server service on Unity Connection will use port 27000 in listening mode. Restricted to localhost only (no remote connections to this service are needed). |
| TCP: 22 | Open | Sshd | root | Firewall must be open for TCP 22 connections for remote CLI access and serving SFTP in a Unity Connection cluster. Administrative workstations must be able to connect to a Unity Connection server on this port. Servers in a Unity Connection cluster must be able to connect to each other on this port. |
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
| TCP: 5007 | Blocked; internal use only. | Tomcat/Cisco Tomcat (SOAP Service) | tomcat | Servers in a Unity Connection cluster must be able to connect to
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
| TCP: 80, 443, 8080, 8443 | Open | haproxy/Cisco HAProxy | haproxy | Both client and administrative workstations need to connect to
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
| TCP: 8081, 8444 | Open only between servers in HTTPS Networking | haproxy/Cisco HAProxy | haproxy | Servers in HTTPS Networking must be able to connect to each
                                             					 other on these ports for communications. Unity Connection HTTPS Directory
                                             					 Feeder service uses these ports for directory synchronization. Note Unity Connection HTTPS
                                                      					 Directory Feeder service supports only IPv4 mode. | Note | Unity Connection HTTPS
                                                      					 Directory Feeder service supports only IPv4 mode. |
| Note | Unity Connection HTTPS
                                                      					 Directory Feeder service supports only IPv4 mode. |
| TCP: 5001-5004, 8005 | Blocked; internal use only | tomcat/Cisco Tomcat | tomcat | Internal tomcat service control and axis ports. |
| TCP: 32768–61000 UDP: 32768–61000 | Open | — | — | Ephemeral port ranges, used by anything with a dynamically
                                             					 allocated client port. |
| TCP:
                                             					 7443 | Open | jetty/Unity Connection Jetty | jetty | Secure
                                             					 Jabber and Web Inbox notifications Note You
                                                         						can enable the port using "utils cuc jetty ssl enable" CLI command. | Note | You
                                                         						can enable the port using "utils cuc jetty ssl enable" CLI command. |
| Note | You
                                                         						can enable the port using "utils cuc jetty ssl enable" CLI command. |
| TCP: 7080 | Open | jetty/Unity Connection Jetty | jetty | Exchange 2010 only, single inbox only: Jabber and Web Inbox
                                             					 EWS notifications of changes to Unity Connection voice messages. |
| UDP: 9291 | Open | CuMbxSync/ Unity Connection Mailbox Sync Service | cumbxsync | Single inbox only: WebDAV notifications of changes to Unity
                                             					 Connection voice messages. |
| TCP: 6080 | Open | CuCsMgr/Unity Connection Conversation Manager | cucsmgr | Video server must be able to connect to Unity Connection on this
                                             					 port for communications. |

| Note | (Applicable for Release 15 SU2 and later) Only Cisco Unity Connection tools are supported to use this port. Any third-party tools, connecting to this port are recommended
                                                      to use port 20536. |
|---|---|

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
                                                         						can enable the port using "utils cuc jetty ssl enable" CLI command. |
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
| TCP: 25,587 (SMTP) | CuSmtpSvr | cusmtpsvr | Unity Connection makes client connections to SMTP servers and smart hosts, or to other Unity Connection servers for features
                                             such as VPIM networking or Unity Connection Digital Networking. Note Cisco Unity Connection supports STARTTLS over port 25. With Release 14SU2 and later, STARTTLS is also supported over port
                                                            587. | Note | Cisco Unity Connection supports STARTTLS over port 25. With Release 14SU2 and later, STARTTLS is also supported over port
                                                            587. |
| Note | Cisco Unity Connection supports STARTTLS over port 25. With Release 14SU2 and later, STARTTLS is also supported over port
                                                            587. |
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

| Note | Cisco Unity Connection supports STARTTLS over port 25. With Release 14SU2 and later, STARTTLS is also supported over port
                                                            587. |
|---|---|

| Ports | Executable/Service or Application | Service Account | Comments |
|---|---|---|---|
| 8443, 443, 8444 | Cisco HAProxy | haproxy | Both client and administrative workstations must connect to these ports. Servers in a Unity Connection cluster must be able to connect to each other on these ports for communications that use HTTP-based
                                          interactions like REST. |
| 7443 | jetty/Unity Connection Jetty | jetty | Secure Jabber and Web Inbox notifications. Cisco Unity Connection releases before 15 SU2, supports only TLS version 1.2 for secure communication. Cisco Unity Connection 15 SU2 and later releases, supports TLS version 1.2 and 1.3 for secure communication. |
| 993 | CuImapSvr/Unity Connection IMAP Server | cuimapsvr | Client workstations must be able to connect to port 993 for IMAP over SSL inbox access. |
| 25,587 | CuSmtpSvr/Unity Connection SMTP Server | cusmtpsvr | Servers delivering SMTP to Unity Connection port 25 or 587, such as other servers in a UC Digital Network. |
| 5061-5199 | CuCsMgr/Unity Connection Conversation Manager | cucsmgr | Unity Connection SIP Control Traffic handled by conversation manager. SIP devices must be able to connect to these ports. |
| LDAP (outbound interface) | CuMbxSync CuCsMgr tomcat | cumbxsync cucsmgr tomcat | Unity Connection uses port 636 when you select LDAPS for the protocol used to communicate with domain controllers. |
| 20536 | Cisco HAProxy | haproxy | If this service is enabled it allows administrative secure read/write database connections for off-box clients. Note (Applicable for Release 15 SU2 and later) Third-party clients connecting to Cisco Unity Connection for ODBC connections are recommended to use this port. | Note | (Applicable for Release 15 SU2 and later) Third-party clients connecting to Cisco Unity Connection for ODBC connections are recommended to use this port. |
| Note | (Applicable for Release 15 SU2 and later) Third-party clients connecting to Cisco Unity Connection for ODBC connections are recommended to use this port. |

| Note | (Applicable for Release 15 SU2 and later) Third-party clients connecting to Cisco Unity Connection for ODBC connections are recommended to use this port. |
|---|---|

| Note | TLS_CHACHA20_POLY1305_SHA256 is not supported in FIPS mode. |
|---|---|

| Note | If you want to use the Phone Security Profile, consider changing it to use an encrypted mode. |
|---|---|

| Note | After modifying the HTTPS ciphers, make sure to restart Tomcat service,Connection SMTP Server and Connection Jetty service
                                          on all the nodes for the changes to take effect. |
|---|---|

| Note | If you are using the above interfaces except CSSM, do not set TLS minimum version to 1.3. It is recommended to set it to any
                                                lower version for smooth commnication between Unity Connection and these interfaces. Cisco Smart Software Licensing (CSSM) will work on TLS 1.2 when minimum TLS version on Unity Connection is set as 1.3. |
|---|---|