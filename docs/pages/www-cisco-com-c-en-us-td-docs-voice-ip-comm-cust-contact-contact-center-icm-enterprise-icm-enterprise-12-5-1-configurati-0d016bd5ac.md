---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-configurati-0d016bd5ac
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/configuration/guide/ucce_b_port-utilization_12_5/ucce_b_port-utilization_12_5_chapter_01000.html
retrieved_at: 2026-08-16T14:52:06.014276+00:00
---

Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.5(1)

# Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.5(1)

Updated: June 20, 2022

Chapter: Port Utilization in Finesse

## Chapter: Port Utilization in Finesse

- Port Utilization in Finesse

- Port Utilization Table Columns

- Finesse Port Utilization

# Port Utilization in Finesse

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

The operating system dynamically assigns the source port that the local application or service uses to connect to the destination
                                                port of a remote device. In most cases, this port is assigned randomly from unused ports in the ephemeral port range 1024 - 65535 .

For security reasons, keep open only the ports mentioned in this guide and those required by your application. Keep the rest
                                                of the ports blocked.

## Finesse Port Utilization

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

Cisco Unified Web Proxy Service (HTTPS)

TCP 443, 8445

Browser and third-party REST clients

—

Bidirectional

Secure port used for Finesse administration console, Finesse agent and supervisor desktop, Finesse Desktop Modules (gadgets)
                                          with the Finesse desktop and Finesse IP Phone Agent.

Finesse desktop uses specific ports for communication between Finesse servers for intra-cluster traffic. For the complete
                                          list of the ports that are used, see System Services Port Utilization .

The Manage Digital Channel gadget uses HTTPS Port 443 to access the internet. The URI used will vary depending on the region.
                                          For more information on region-specific URI, see Manage Digital Channels gadget section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html .

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote  Port

Traffic Direction

Notes

XMPP

TCP 5223

Browser and agent desktop

—

Bidirectional

Secure XMPP connection between the Finesse server and custom third-party applications.

BOSH (HTTPS)

TCP 7443

Browser and agent desktop

—

Bidirectional

Secure BOSH connection between the Finesse server and agent and supervisor desktops for communication over HTTPS.

A network connection is required to open between the Finesse Server and the ECE Web server.

Finesse desktop uses specific ports on CUIC and Live Data to render Live Data gadgets and reports. For the complete list of
                                                the ports that can be used, see Unified Intelligence Center Port Utilization .

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

XMPP

TCP 5222

—

—

Bidirectional

The primary and secondary Finesse servers use this XMPP connection to communicate with each other to monitor connectivity.

### Third-Party (External) Web Server

Gadgets hosted on a third-party (external) web server are fetched through the Finesse server on the port exposed by said web
                                          server.

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote  Port

Traffic Direction

Notes

Administration & Data Server settings

JDBC (SQL)

—

—

TCP 1433 1

Bidirectional

Connection to the AWDB for authentication and authorization of agents and supervisors

CTI Server settings (Side A and B)

GED-188

—

—

Side A:

TCP 42027 1

Side B:

TCP 43027 1

Bidirectional

Connection to the Agent PG for CTI Server events (such as Agents, Teams, Queues, and Call events)

1 The ports listed are the default ports for these connections. You can use different ports than the ones specified in this
                              table.

| Note | The operating system dynamically assigns the source port that the local application or service uses to connect to the destination
                                                port of a remote device. In most cases, this port is assigned randomly from unused ports in the ephemeral port range 1024 - 65535 . For security reasons, keep open only the ports mentioned in this guide and those required by your application. Keep the rest
                                                of the ports blocked. |
|---|---|

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| Cisco Unified Web Proxy Service (HTTPS) | TCP 443, 8445 | Browser and third-party REST clients | — | Bidirectional | Secure port used for Finesse administration console, Finesse agent and supervisor desktop, Finesse Desktop Modules (gadgets)
                                          with the Finesse desktop and Finesse IP Phone Agent. |

| Note | Finesse desktop uses specific ports for communication between Finesse servers for intra-cluster traffic. For the complete
                                          list of the ports that are used, see System Services Port Utilization . The Manage Digital Channel gadget uses HTTPS Port 443 to access the internet. The URI used will vary depending on the region.
                                          For more information on region-specific URI, see Manage Digital Channels gadget section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html . |
|---|---|

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote  Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| XMPP | TCP 5223 | Browser and agent desktop | — | Bidirectional | Secure XMPP connection between the Finesse server and custom third-party applications. |
| BOSH (HTTPS) | TCP 7443 | Browser and agent desktop | — | Bidirectional | Secure BOSH connection between the Finesse server and agent and supervisor desktops for communication over HTTPS. Note In Cisco Finesse Release 12.5(1) and later, BOSH (long polling) notifications are disabled by default. Applications must use
                                                   either WebSocket-based notifications (over 8445 port) or direct XMPP notifications (over TCP). Support for port 7443 (BOSH)
                                                   is planned for removal in a future release. | Note | In Cisco Finesse Release 12.5(1) and later, BOSH (long polling) notifications are disabled by default. Applications must use
                                                   either WebSocket-based notifications (over 8445 port) or direct XMPP notifications (over TCP). Support for port 7443 (BOSH)
                                                   is planned for removal in a future release. |
| Note | In Cisco Finesse Release 12.5(1) and later, BOSH (long polling) notifications are disabled by default. Applications must use
                                                   either WebSocket-based notifications (over 8445 port) or direct XMPP notifications (over TCP). Support for port 7443 (BOSH)
                                                   is planned for removal in a future release. |

| Note | In Cisco Finesse Release 12.5(1) and later, BOSH (long polling) notifications are disabled by default. Applications must use
                                                   either WebSocket-based notifications (over 8445 port) or direct XMPP notifications (over TCP). Support for port 7443 (BOSH)
                                                   is planned for removal in a future release. |
|---|---|

| Note | A network connection is required to open between the Finesse Server and the ECE Web server. Finesse desktop uses specific ports on CUIC and Live Data to render Live Data gadgets and reports. For the complete list of
                                                the ports that can be used, see Unified Intelligence Center Port Utilization . |
|---|---|

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| XMPP | TCP 5222 | — | — | Bidirectional | The primary and secondary Finesse servers use this XMPP connection to communicate with each other to monitor connectivity. |

| Note | Gadgets hosted on a third-party (external) web server are fetched through the Finesse server on the port exposed by said web
                                          server. |
|---|---|

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote  Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| Administration & Data Server settings |
| JDBC (SQL) | — | — | TCP 1433 1 | Bidirectional | Connection to the AWDB for authentication and authorization of agents and supervisors |
| CTI Server settings (Side A and B) |
| GED-188 | — | — | Side A: TCP 42027 1 Side B: TCP 43027 1 | Bidirectional | Connection to the Agent PG for CTI Server events (such as Agents, Teams, Queues, and Call events) |