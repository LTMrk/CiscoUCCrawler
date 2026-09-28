---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-configurati-fe3060d49f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/configuration/guide/ucce_b_port_utilization_12_6_2/ucce_b_port-utilization_12_5_chapter_0111.html
retrieved_at: 2026-08-20T18:34:09.630645+00:00
---

Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.6(2)

# Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.6(2)

Updated: November 30, 2025

Chapter: Port Utilization in Unified Intelligence Center

## Chapter: Port Utilization in Unified Intelligence Center

- Port Utilization in Unified Intelligence Center

- Unified Intelligence Center Port Utilization

# Port Utilization in Unified Intelligence Center

## Unified Intelligence Center Port Utilization

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

Web Proxy for Unified Intelligence Center

TCP 8444 /TCP 443

Browser

Random

Bi-Directional

HTTPS - Unified Intelligence Center Online Help and Unified Intelligence Center.

TCP 8447

Browser

Random

Bi-Directional

HTTPS - Unified Intelligence Center - Online Help

OAMP

TCP 8080

Browser

Random

Bi-Directional

HTTP - OAMP

TCP 8443 /TCP 443

Browser

Random

Bi-Directional

HTTPS - OAMP

The port 8447 is deprecated and will be removed in future releases. Unified Intelligence Center Online Help will be available
                                          on Port 8444.

Listener (Process or Application Protocol)

Listener Protocol and port

Remote Device (Process or Application protocol)

Remote Port

Traffic Direction

Notes

CCE Live Data Cassandra Service

TCP 12000

CCE Live Data Cassandra Service (other side)

Random

Bi-Directional

Used for replicating Cassandra data

CCE Live Data Zookeeper Service

TCP 2181

CCE Live Data Zookeeper Service (other side)

Random

Bi-Directional

Used for replicating zookeeper data

Web Proxy for CCE Live Data Web Service

TCP 12005

Browser

Random

Bi-Directional

Live Data web service

Web Proxy for CCE Live Data Socket IO Service

TCP 12008

Browser

Random

Bi-Directional

Live Data Socket.IO listening port

CCE Live Data Active MQ Service

TCP 61616

Random

Bi-Directional

Live Data ActiveMQ Openwire transport connector port

CCE Live Data Active MQ Service

TCP 61612

CCE Live Data Active MQ Service (other side)

Random

Bi-Directional

Live Data ActiveMQ Stomp transport connector port

Web Proxy for CCE Live Data Web Service and Web Proxy for CCE Live Data Socket IO Service

TCP 443

Browser

Random

Bi-Directional

Live Data Web Service and Live Data Socket.IO listening port.

The ports 12005 and 12008 are deprecated and will be removed in future releases. The port 443 will be used for Live Data Web
                                          Service and Live Data Socket.IO Service.

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

CUIC Reporting Process

UDP 54327 (Multicast)

Unified Intelligence Center node

—

—

Hazelcast Discovery

CUIC Reporting Process

TCP 57011

Unified Intelligence Center Node

—

—

Hazelcast

Cisco Unified Intelligence Center, which runs on the Cisco VOS operating system uses the following ports: TCP 5001, TCP 5002,
                              and TCP 5003 for SOAP monitoring. For more information on these ports, see Port Utilization for System Services section.

For more information on other port usages, see: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| Web Proxy for Unified Intelligence Center | TCP 8444 /TCP 443 | Browser | Random | Bi-Directional | HTTPS - Unified Intelligence Center Online Help and Unified Intelligence Center. |
| TCP 8447 | Browser | Random | Bi-Directional | HTTPS - Unified Intelligence Center - Online Help |
| OAMP | TCP 8080 | Browser | Random | Bi-Directional | HTTP - OAMP |
| TCP 8443 /TCP 443 | Browser | Random | Bi-Directional | HTTPS - OAMP |

| Note | The port 8447 is deprecated and will be removed in future releases. Unified Intelligence Center Online Help will be available
                                          on Port 8444. |
|---|---|

| Listener (Process or Application Protocol) | Listener Protocol and port | Remote Device (Process or Application protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| CCE Live Data Cassandra Service | TCP 12000 | CCE Live Data Cassandra Service (other side) | Random | Bi-Directional | Used for replicating Cassandra data |
| CCE Live Data Zookeeper Service | TCP 2181 | CCE Live Data Zookeeper Service (other side) | Random | Bi-Directional | Used for replicating zookeeper data |
| Web Proxy for CCE Live Data Web Service | TCP 12005 | Browser | Random | Bi-Directional | Live Data web service |
| Web Proxy for CCE Live Data Socket IO Service | TCP 12008 | Browser | Random | Bi-Directional | Live Data Socket.IO listening port |
| CCE Live Data Active MQ Service | TCP 61616 | CCE Live Data Active MQ Service (other side) | Random | Bi-Directional | Live Data ActiveMQ Openwire transport connector port |
| CCE Live Data Active MQ Service | TCP 61612 | CCE Live Data Active MQ Service (other side) | Random | Bi-Directional | Live Data ActiveMQ Stomp transport connector port |
| Web Proxy for CCE Live Data Web Service and Web Proxy for CCE Live Data Socket IO Service | TCP 443 | Browser | Random | Bi-Directional | Live Data Web Service and Live Data Socket.IO listening port. |

| Note | The ports 12005 and 12008 are deprecated and will be removed in future releases. The port 443 will be used for Live Data Web
                                          Service and Live Data Socket.IO Service. |
|---|---|

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| CUIC Reporting Process | UDP 54327 (Multicast) | Unified Intelligence Center node | — | — | Hazelcast Discovery |
| CUIC Reporting Process | TCP 57011 | Unified Intelligence Center Node | — | — | Hazelcast |