---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-configurati-0704a9377f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/configuration/guide/ucce_b_port_utilization_12_6_1/ucce_b_port-utilization_12_5_chapter_01000.html
retrieved_at: 2026-08-16T14:43:41.009384+00:00
---

Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.6(1)

# Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.6(1)

Updated: May 14, 2021

Chapter: Port Utilization in Finesse

## Chapter: Port Utilization in Finesse

- Port Utilization in Finesse

- Finesse Port Utilization

# Port Utilization in Finesse

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

Note

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

Note

Note

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

Note

Gadgets hosted on a third-party (external) web server are fetched through the Finesse server on the port exposed by said web
                                          server.

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

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