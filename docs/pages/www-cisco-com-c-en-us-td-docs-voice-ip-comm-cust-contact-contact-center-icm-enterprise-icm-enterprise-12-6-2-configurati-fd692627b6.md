---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-configurati-fd692627b6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/configuration/guide/ucce_b_port_utilization_12_6_2/ucce_b_port-utilization_12_5_chapter_011.html
retrieved_at: 2026-08-16T14:39:22.801339+00:00
---

Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.6(2)

# Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.6(2)

Updated: November 30, 2025

Chapter: Port Utilization in Cisco VVB

## Chapter: Port Utilization in Cisco VVB

- Port Utilization in Cisco VVB

- Cisco VVB Port Utilization

# Port Utilization in Cisco VVB

## Cisco VVB Port Utilization

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

VBONINIT

TCP 1504

External process such as External DB clients (like Squirrel or others for custom reporting) can connect

—

Bidirectional

Cisco VVB database port

VVB_ Engine

SIP over TCP, SIP over UDP 5060

SIP

—

Bidirectional

Communicates with SIP gateway

VVB_ Engine

SIP over TLS 5061

SIP

—

Bidirectional

Communicates with SIP gateway

VVB_CVD

TCP 6161

Internal

6161

Bidirectional

Publishes JMS events across JMS network connectors in the cluster

CVD

TCP 6295

CVD of other node in cluster

—

Bidirectional

Bootstrap HTTPD service port

VVB_CVD

TCP 6999

Engine, Tomcat, CVD, and Editor

—

Bidirectional

RMI Port

VVB_Engine

TCP 9080

—

—

Bidirectional

- Clients trying to access HTTP triggers, documents, prompts, or grammars

- Tomcat instance used by Cisco VVB engine

Cisco IP Voice Media Streaming application

UDP 24576 ~ 32767

—

—

Bidirectional

- Audio media streaming.

- Kernel streaming device driver

Ephemeral (Process or Application Protocol)

Ephemeral Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

Generic Ports

TCP, UDP 32768 ~ 61000

—

—

Bidirectional

Generic ephemeral TCP and UDP ports

Note

SIP signalling is possible over TCP or TLS. For RTP, underlying protocol is UDP always (not configurable). If TLS is used
                                          for SIP signalling, then the same exchanged keys will be used to encrypt and decrypt the RTP packets - for SRTP

To view the system services for port utilization for Cisco Virtualized Voice Browser, see System Services Port Utilization

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| VBONINIT | TCP 1504 | External process such as External DB clients (like Squirrel or others for custom reporting) can connect | — | Bidirectional | Cisco VVB database port |
| VVB_ Engine | SIP over TCP, SIP over UDP 5060 | SIP | — | Bidirectional | Communicates with SIP gateway |
| VVB_ Engine | SIP over TLS 5061 | SIP | — | Bidirectional | Communicates with SIP gateway |
| VVB_CVD | TCP 6161 | Internal | 6161 | Bidirectional | Publishes JMS events across JMS network connectors in the cluster |
| CVD | TCP 6295 | CVD of other node in cluster | — | Bidirectional | Bootstrap HTTPD service port |
| VVB_CVD | TCP 6999 | Engine, Tomcat, CVD, and Editor | — | Bidirectional | RMI Port |
| VVB_Engine | TCP 9080 | — | — | Bidirectional | - Clients trying to access HTTP triggers, documents, prompts, or grammars - Tomcat instance used by Cisco VVB engine |
| Cisco IP Voice Media Streaming application | UDP 24576 ~ 32767 | — | — | Bidirectional | - Audio media streaming. - Kernel streaming device driver |

| Ephemeral (Process or Application Protocol) | Ephemeral Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| Generic Ports | TCP, UDP 32768 ~ 61000 | — | — | Bidirectional | Generic ephemeral TCP and UDP ports |

| Note | SIP signalling is possible over TCP or TLS. For RTP, underlying protocol is UDP always (not configurable). If TLS is used
                                          for SIP signalling, then the same exchanged keys will be used to encrypt and decrypt the RTP packets - for SRTP |
|---|---|