---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-configurati-cf5611a55a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/configuration/guide/ucce_b_port-utilization_12_5/ucce_b_port-utilization_12_5_chapter_01001.html
retrieved_at: 2026-08-16T14:52:09.787307+00:00
---

Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.5(1)

# Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.5(1)

Updated: June 20, 2022

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

The remote port is used to make an outgoing connection to the corresponding listener port.

The direction that traffic flows through the port: Inbound, Bidirectional, Outbound.

The operating system dynamically assigns the source port that the local application or service uses to connect to the destination
                                                port of a remote device. In most cases, this port is assigned randomly from unused ports in the ephemeral port range 1024 - 65535 .

For security reasons, keep open only the ports mentioned in this guide and those required by your application. Keep the rest
                                                of the ports blocked.

## Customer Collaboration Platform Port Utilization

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

HTTP

Port 80

Bidirectional

Used for unsecure (HTTP) traffic:

From the Customer Collaboration Platform user interface (browser) or APIs to the Customer Collaboration Platform server.

From the internet or corporate website to the Customer Collaboration Platform server. Customer Collaboration Platform receives incoming chat and callback requests from the internet or corporate website over HTTP.

HTTPS

Port 443

Bidirectional

Used for secure (HTTPS) traffic:

From the Customer Collaboration Platform user interface (browser) or APIs to the Customer Collaboration Platform server.

From the internet or corporate website to the Customer Collaboration Platform server. Customer Collaboration Platform receives incoming chat and callback requests from the internet or corporate website over HTTPS.

XMPP (IM) notifications using an external XMPP server

Port 5222 (configurable)

Outward, from Customer Collaboration Platform to the configured XMPP Notifications server.

Customer Collaboration Platform communicates with the configured XMPP Notifications server (that can be in the corporate intranet or on the internet) to
                                          send XMPP (IM) notifications.

Eventing and chat (BOSH)

Port 7071

Bidirectional

The unsecure BOSH connection supports eventing and chat communication between the Customer Collaboration Platform user interface and the Customer Collaboration Platform server.

Eventing and chat (secure BOSH)

Port 7443 is used for secure BOSH connections to the XMPP eventing server.

Bidirectional

The secure BOSH connection supports eventing and chat communication between the Customer Collaboration Platform user interface and the Customer Collaboration Platform server.

Media routing (in CCE deployments)

Port 38001 (configurable)

Inward, from the CCE MR PG to the Customer Collaboration Platform server.

The CCE Media Routing Peripheral Gateway (MR PG) communicates over a socket connection to Customer Collaboration Platform to support the media routing connection.

| Note | The operating system dynamically assigns the source port that the local application or service uses to connect to the destination
                                                port of a remote device. In most cases, this port is assigned randomly from unused ports in the ephemeral port range 1024 - 65535 . For security reasons, keep open only the ports mentioned in this guide and those required by your application. Keep the rest
                                                of the ports blocked. |
|---|---|

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| HTTP | Port 80 |  |  | Bidirectional | Used for unsecure (HTTP) traffic: From the Customer Collaboration Platform user interface (browser) or APIs to the Customer Collaboration Platform server. From the internet or corporate website to the Customer Collaboration Platform server. Customer Collaboration Platform receives incoming chat and callback requests from the internet or corporate website over HTTP. |
| HTTPS | Port 443 |  |  | Bidirectional | Used for secure (HTTPS) traffic: From the Customer Collaboration Platform user interface (browser) or APIs to the Customer Collaboration Platform server. From the internet or corporate website to the Customer Collaboration Platform server. Customer Collaboration Platform receives incoming chat and callback requests from the internet or corporate website over HTTPS. |
| XMPP (IM) notifications using an external XMPP server | Port 5222 (configurable) |  |  | Outward, from Customer Collaboration Platform to the configured XMPP Notifications server. | Customer Collaboration Platform communicates with the configured XMPP Notifications server (that can be in the corporate intranet or on the internet) to
                                          send XMPP (IM) notifications. |
| Eventing and chat (BOSH) | Port 7071 |  |  | Bidirectional | The unsecure BOSH connection supports eventing and chat communication between the Customer Collaboration Platform user interface and the Customer Collaboration Platform server. |
| Eventing and chat (secure BOSH) | Port 7443 is used for secure BOSH connections to the XMPP eventing server. |  |  | Bidirectional | The secure BOSH connection supports eventing and chat communication between the Customer Collaboration Platform user interface and the Customer Collaboration Platform server. |
| Media routing (in CCE deployments) | Port 38001 (configurable) |  |  | Inward, from the CCE MR PG to the Customer Collaboration Platform server. | The CCE Media Routing Peripheral Gateway (MR PG) communicates over a socket connection to Customer Collaboration Platform to support the media routing connection. |