---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-configurati-19f1bf26af
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/configuration/guide/ucce_b_port-utilization_12_5/ucce_b_port-utilization_12_5_chapter_0111.html
retrieved_at: 2026-08-16T14:52:14.191913+00:00
---

Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.5(1)

# Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.5(1)

Updated: June 20, 2022

Chapter: Port Utilization in Unified Intelligence Center

## Chapter: Port Utilization in Unified Intelligence Center

- Port Utilization in Unified Intelligence Center

- Port Utilization Table Columns

- Unified Intelligence Center Port Utilization

# Port Utilization in Unified Intelligence Center

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

## Unified Intelligence Center Port Utilization

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

Unified Intelligence Center

TCP 8444

Browser

Random

Bi-Directional

HTTPS - Unified Intelligence Center

TCP 8447

Browser

Random

Bi-Directional

HTTPS - Unified Intelligence Center - Online Help

TCP 8081

Browser

Random

Bi-Directional

HTTP - Unified Intelligence Center

OAMP

TCP 8080

Browser

Random

Bi-Directional

HTTP - OAMP

TCP 8443

Browser

Random

Bi-Directional

HTTPS - OAMP

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

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

Storm DRPC service

TCP 3772

—

—

—

Live Data DRPC port

Storm DRPC service

TCP 3773

—

—

—

Live Data DRPC invocation port

CCE Live Data Cassandra Service

TCP 12000

Random

Bi-Directional

Used for replicating Cassandra data

CCE Live Data Cassandra Service

TCP 12001

—

—

—

Live Data Cassandra SSL port for encrypted communication. (Unused unless enabled in encryption_options.)

CCE Live Data Zookeeper Service

TCP 2181

CCE Live Data Zookeeper Service (other side)

Random

Bi-Directional

CCE Live Data ActiveMQ Service

TCP 12002

—

—

—

ActiveMQ JMX connector port

CCE Live Data ActiveMQ Service

TCP 12003

—

—

—

ActiveMQ JMX rmi port

CCE Live Data Web Service

TCP 12004 - 12005

Browser

Random

Bi-Directional

Live Data web service

CCE Live Data Active MQ Service

TCP 61616

CCE Live Data Active MQ Service (other side)

Random

Bi-Directional

ive Data ActiveMQ Openwire transport connector port

CCE Live Data Active MQ Service

TCP 61612

CCE Live Data Active MQ Service (other side)

Random

Bi-Directional

Live Data ActiveMQ Stomp transport connector port

CCE Live Data Socket.IO Service

TCP 12007 - 12008

Browser

Live Data Socket.IO listening port

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

| Note | The operating system dynamically assigns the source port that the local application or service uses to connect to the destination
                                                port of a remote device. In most cases, this port is assigned randomly from unused ports in the ephemeral port range 1024 - 65535 . For security reasons, keep open only the ports mentioned in this guide and those required by your application. Keep the rest
                                                of the ports blocked. |
|---|---|

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| Unified Intelligence Center | TCP 8444 | Browser | Random | Bi-Directional | HTTPS - Unified Intelligence Center |
| TCP 8447 | Browser | Random | Bi-Directional | HTTPS - Unified Intelligence Center - Online Help |
| TCP 8081 | Browser | Random | Bi-Directional | HTTP - Unified Intelligence Center |
| OAMP | TCP 8080 | Browser | Random | Bi-Directional | HTTP - OAMP |
| TCP 8443 | Browser | Random | Bi-Directional | HTTPS - OAMP |

| Listener (Process or Application Protocol) | Listener Protocol and port | Remote Device (Process or Application protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| CCE Live Data Cassandra Service | TCP 12000 | CCE Live Data Cassandra Service (other side) | Random | Bi-Directional | Used for replicating Cassandra data |
| CCE Live Data Zookeeper Service | TCP 2181 | CCE Live Data Zookeeper Service (other side) | Random | Bi-Directional | Used for replicating zookeeper data |
| Web Proxy for CCE Live Data Web Service | TCP 12005 | Browser | Random | Bi-Directional | Live Data web service |
| Web Proxy for CCE Live Data Socket IO Service | TCP 12008 | Browser | Random | Bi-Directional | Live Data Socket.IO listening port |
| CCE Live Data Active MQ Service | TCP 61616 | CCE Live Data Active MQ Service (other side) | Random | Bi-Directional | Live Data ActiveMQ Openwire transport connector port |
| CCE Live Data Active MQ Service | TCP 61612 | CCE Live Data Active MQ Service (other side) | Random | Bi-Directional | Live Data ActiveMQ Stomp transport connector port |

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| Storm DRPC service | TCP 3772 | — | — | — | Live Data DRPC port |
| Storm DRPC service | TCP 3773 | — | — | — | Live Data DRPC invocation port |
| CCE Live Data Cassandra Service | TCP 12000 | CCE Live Data Cassandra Service (other side) | Random | Bi-Directional | Used for replicating Cassandra data |
| CCE Live Data Cassandra Service | TCP 12001 | — | — | — | Live Data Cassandra SSL port for encrypted communication. (Unused unless enabled in encryption_options.) |
| CCE Live Data Zookeeper Service | TCP 2181 | CCE Live Data Zookeeper Service (other side) | Random | Bi-Directional | Used for replicating zookeeper data |
| CCE Live Data ActiveMQ Service | TCP 12002 | — | — | — | ActiveMQ JMX connector port |
| CCE Live Data ActiveMQ Service | TCP 12003 | — | — | — | ActiveMQ JMX rmi port |
| CCE Live Data Web Service | TCP 12004 - 12005 | Browser | Random | Bi-Directional | Live Data web service |
| CCE Live Data Active MQ Service | TCP 61616 | CCE Live Data Active MQ Service (other side) | Random | Bi-Directional | ive Data ActiveMQ Openwire transport connector port |
| CCE Live Data Active MQ Service | TCP 61612 | CCE Live Data Active MQ Service (other side) | Random | Bi-Directional | Live Data ActiveMQ Stomp transport connector port |
| CCE Live Data Socket.IO Service | TCP 12007 - 12008 | Browser | Random | Bi-Directional | Live Data Socket.IO listening port |

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| CUIC Reporting Process | UDP 54327 (Multicast) | Unified Intelligence Center node | — | — | Hazelcast Discovery |
| CUIC Reporting Process | TCP 57011 | Unified Intelligence Center Node | — | — | Hazelcast |