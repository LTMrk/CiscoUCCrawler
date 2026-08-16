---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-configuration-guide-rcct--30e11da787
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/configuration/guide/rcct_b_1251su1_port-utilization-guide-ccx/rcct_b_1251port-utilization-guide-ccx_chapter_010.html
retrieved_at: 2026-08-16T15:02:24.133810+00:00
---

Port Utilization Guide for Cisco Unified Contact Center Express Solution, Release 12.5(1) SU1

# Port Utilization Guide for Cisco Unified Contact Center Express Solution, Release 12.5(1) SU1

Updated: January 31, 2021

Chapter: Port Utilization in Customer Collaboration Platform

## Chapter: Port Utilization in Customer Collaboration Platform

- Port Utilization in Customer Collaboration Platform

- Port Utilization Table Columns

- Customer Collaboration Platform Port Utilization

# Port Utilization in Customer Collaboration Platform

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

The identifier for the TCP or UDP port that the remote service or application is listening on, along with the IP address
                                    for incoming connection requests when acting as the server.

The direction that traffic flows through the port: Inbound, Bidirectional, Outbound.

The operating system dynamically assigns the source port that the local application or service uses to connect to the destination
                                                port of a remote device. In most cases, this port is assigned randomly above TCP/UDP 1024 .

For security reasons, keep open only the ports mentioned in this guide and those required by your application. Keep the rest
                                                of the ports blocked.

## Customer Collaboration Platform Port Utilization

Listener (Process or Application Protocol)

Listener Protocol and Port

Destination Port

Remote Device (Process or Application Protocol)

Remote Protocol and Port

Traffic Direction

Purpose

Email notifications

25

—

—

—

Outward, from Customer Collaboration Platform to the
                                       								configured email server.

Customer Collaboration Platform communicates with
                                       								the configured email server (that can be in the corporate intranet
                                       								or on the internet) to send email notifications.

HTTP

80

—

—

—

Bidirectional

Used for unsecure (HTTP) traffic:

From the Customer Collaboration Platform user
                                             										interface (browser) or APIs to the Customer Collaboration Platform server.

From the Customer Collaboration Platform server
                                             										to the internet. Customer Collaboration Platform communicates outward to the internet to fetch social contact
                                             										information (such as Facebook posts and tweets) over HTTP.

From the internet or corporate website to the Customer Collaboration Platform server. Customer Collaboration Platform receives
                                             										incoming chat and callback requests from the internet or
                                             										corporate website over HTTP.

HTTPS

Port 443

—

—

—

Bidirectional

Used for secure (HTTPS) traffic

From the Customer Collaboration Platform user
                                             										interface (browser) or APIs to the Customer Collaboration Platform server.

From the Customer Collaboration Platform server
                                             										to the internet. Customer Collaboration Platform communicates outward to the internet to fetch social contact
                                             										information (such as Facebook posts and tweets) over HTTPS.

From the internet or corporate website to the Customer Collaboration Platform server. Customer Collaboration Platform receives
                                             										incoming chat and callback requests from the internet or
                                             										corporate website over HTTPS.

Email
                                       								notifications SSL/TLS

Port 465
                                       								(configurable)

—

—

Outward, from Customer Collaboration Platform to the
                                       								configured email server.

Customer Collaboration Platform communicates
                                       								with the configured email server (that can be in the corporate
                                       								intranet or on the internet) to send email notifications.

Email (SMTP)

Port 587 (configurable in Unified CCX Administration)

—

—

Outward, from Customer Collaboration Platform to the Exchange
                                       								Server.

Used by the Email
                                       								Reply API to send email.

The Email Reply
                                       								API uses SMTP to send a response to a customer email message.

Email (secure
                                       								IMAP/IMAPS)

Port 993
                                       								(configurable in Unified CCX Administration)

—

—

Outward, from Customer Collaboration Platform to the Exchange
                                       								Server.

Used by email
                                       								feeds to retrieve email.

IMAPS allows
                                       								email feeds to fetch email from the Exchange Servers and allows the
                                       								Email Reply API to retrieve email and save draft email messages.

Customer Collaboration Platform Chat Gateway
                                       								webhook interface (HTTPS)

Port
                                       								10443

—

—

Unidirectional, Inward from the Internet to Cisco Customer Collaboration Platform server.

This TCP port
                                       								is enabled for public access to the Customer Collaboration Platform Chat Gateway
                                       								webhook interface.

XMPP (IM)
                                       								notifications using an external XMPP server

Port 5222
                                       								(configurable)

—

—

Bidirectional

Customer Collaboration Platform communicates
                                       								with the configured XMPP Notifications server (that can be in the
                                       								corporate intranet or on the internet) to send XMPP (IM)
                                       								notifications.

Outward, from Customer Collaboration Platform to the
                                       								configured XMPP Notifications server.

Notification
                                       								Service (XMPP eventing over TCP sockets)

Port 5222

—

—

Bidirectional

Customer Collaboration Platform listens for
                                       								incoming TCP socket connections to register and send XMPP events.
                                       								Unified CCX uses this port to receive social contact events.

Inward, from
                                       								CCX to the Customer Collaboration Platform server.

Eventing and
                                       								chat (BOSH)

Port 7071

—

—

Bidirectional

The unsecure
                                       								BOSH connection supports eventing and chat communication between the Customer Collaboration Platform user interface
                                       								and the Customer Collaboration Platform server.

Eventing and
                                       								chat (secure BOSH)

Port 7443 is
                                       								used for secure BOSH connections to the XMPP eventing server.

—

—

—

Bidirectional

The secure BOSH
                                       								connection supports eventing and chat communication between the Customer Collaboration Platform user interface
                                       								and the Customer Collaboration Platform server.

| Note | The operating system dynamically assigns the source port that the local application or service uses to connect to the destination
                                                port of a remote device. In most cases, this port is assigned randomly above TCP/UDP 1024 . For security reasons, keep open only the ports mentioned in this guide and those required by your application. Keep the rest
                                                of the ports blocked. |
|---|---|

| Listener (Process or Application Protocol) | Listener Protocol and Port | Destination Port | Remote Device (Process or Application Protocol) | Remote Protocol and Port | Traffic Direction | Purpose |
|---|---|---|---|---|---|---|
| Email notifications | 25 | — | — | — | Outward, from Customer Collaboration Platform to the
                                       								configured email server. | Customer Collaboration Platform communicates with
                                       								the configured email server (that can be in the corporate intranet
                                       								or on the internet) to send email notifications. |
| HTTP | 80 | — | — | — | Bidirectional | Used for unsecure (HTTP) traffic: From the Customer Collaboration Platform user
                                             										interface (browser) or APIs to the Customer Collaboration Platform server. From the Customer Collaboration Platform server
                                             										to the internet. Customer Collaboration Platform communicates outward to the internet to fetch social contact
                                             										information (such as Facebook posts and tweets) over HTTP. From the internet or corporate website to the Customer Collaboration Platform server. Customer Collaboration Platform receives
                                             										incoming chat and callback requests from the internet or
                                             										corporate website over HTTP. |
| HTTPS | Port 443 | — | — | — | Bidirectional | Used for secure (HTTPS) traffic From the Customer Collaboration Platform user
                                             										interface (browser) or APIs to the Customer Collaboration Platform server. From the Customer Collaboration Platform server
                                             										to the internet. Customer Collaboration Platform communicates outward to the internet to fetch social contact
                                             										information (such as Facebook posts and tweets) over HTTPS. From the internet or corporate website to the Customer Collaboration Platform server. Customer Collaboration Platform receives
                                             										incoming chat and callback requests from the internet or
                                             										corporate website over HTTPS. |
| Email
                                       								notifications SSL/TLS | Port 465
                                       								(configurable) |  | — | — | Outward, from Customer Collaboration Platform to the
                                       								configured email server. | Customer Collaboration Platform communicates
                                       								with the configured email server (that can be in the corporate
                                       								intranet or on the internet) to send email notifications. |
| Email (SMTP) | Port 587 (configurable in Unified CCX Administration) |  | — | — | Outward, from Customer Collaboration Platform to the Exchange
                                       								Server. | Used by the Email
                                       								Reply API to send email. The Email Reply
                                       								API uses SMTP to send a response to a customer email message. |
| Email (secure
                                       								IMAP/IMAPS) | Port 993
                                       								(configurable in Unified CCX Administration) |  | — | — | Outward, from Customer Collaboration Platform to the Exchange
                                       								Server. | Used by email
                                       								feeds to retrieve email. IMAPS allows
                                       								email feeds to fetch email from the Exchange Servers and allows the
                                       								Email Reply API to retrieve email and save draft email messages. |
| Customer Collaboration Platform Chat Gateway
                                       								webhook interface (HTTPS) | Port
                                       								10443 |  | — | — | Unidirectional, Inward from the Internet to Cisco Customer Collaboration Platform server. | This TCP port
                                       								is enabled for public access to the Customer Collaboration Platform Chat Gateway
                                       								webhook interface. |
| XMPP (IM)
                                       								notifications using an external XMPP server | Port 5222
                                       								(configurable) |  | — | — | Bidirectional | Customer Collaboration Platform communicates
                                       								with the configured XMPP Notifications server (that can be in the
                                       								corporate intranet or on the internet) to send XMPP (IM)
                                       								notifications. Outward, from Customer Collaboration Platform to the
                                       								configured XMPP Notifications server. |
| Notification
                                       								Service (XMPP eventing over TCP sockets) | Port 5222 |  | — | — | Bidirectional | Customer Collaboration Platform listens for
                                       								incoming TCP socket connections to register and send XMPP events.
                                       								Unified CCX uses this port to receive social contact events. Inward, from
                                       								CCX to the Customer Collaboration Platform server. |
| Eventing and
                                       								chat (BOSH) | Port 7071 |  | — | — | Bidirectional | The unsecure
                                       								BOSH connection supports eventing and chat communication between the Customer Collaboration Platform user interface
                                       								and the Customer Collaboration Platform server. |
| Eventing and
                                       								chat (secure BOSH) | Port 7443 is
                                       								used for secure BOSH connections to the XMPP eventing server. | — | — | — | Bidirectional | The secure BOSH
                                       								connection supports eventing and chat communication between the Customer Collaboration Platform user interface
                                       								and the Customer Collaboration Platform server. |