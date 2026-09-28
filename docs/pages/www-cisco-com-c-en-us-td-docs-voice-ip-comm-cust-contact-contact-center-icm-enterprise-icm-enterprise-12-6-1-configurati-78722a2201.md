---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-configurati-78722a2201
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/configuration/guide/ucce_b_port_utilization_12_6_1/rcct_m_cloud_connect_port_utilization.html
retrieved_at: 2026-08-20T18:10:57.322286+00:00
---

Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.6(1)

# Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.6(1)

Updated: May 14, 2021

Chapter: Port Utilization in Cisco Cloud Connect

## Chapter: Port Utilization in Cisco Cloud Connect

- Port Utilization in Cisco Cloud Connect

- Port Utilization in Cisco Cloud Connect

# Port Utilization in Cisco Cloud Connect

## Port Utilization in Cisco Cloud Connect

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote  Port

Traffic Direction

Notes

Cisco Unified Web Proxy Service (HTTPS)

TCP 8445

Applications

—

Inward from applications to Cloud Connect Services.

—

Listener (Process or Application Protocol)

Listener Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

CherryPoint Service

TCP 3551

CherryPoint Service on the other node in the same cluster.

—

Bidirectional

CherryPoint services use this port for secure cluster management.

Inventory Service

TCP 5551

Inventory Service on the other node in the same cluster.

—

Bidirectional

Inventory services use this port for secure cluster
                                          management.

CloudConnectMgmt Service

TCP 6551

CloudConnectMgmt Service on the other node in the same
                                          cluster.

—

Bidirectional

CloudConnectMgmt services use this port for secure cluster
                                          management.

Ansible Controller

—

SSH Server on Orchestration target node

TCP 22

Outward from Ansible Controller to SSH Server on Orchestration target node

Used for connecting to target node for Orchestration.

Ansible Controller

—

SMTP Relay Server

TCP 25

Outward from Ansible Controller to SMTP Relay Server

Used for sending email notification.

When using a proxy for Cloud Connect integration, ensure the domains and URLs listed in the table below are added to the proxy
                                          allowlist.

(Process or Application Protocol)

Protocol and Port

Remote Device (Process or Application Protocol)

Remote Port

Traffic Direction

Notes

CloudConnectMgmt

—

Fusion Management Service

https://hercules-a.wbx2.com ,

https://hercules-k.wbx2.com ,

https://hercules-r.wbx2.com

TCP 443

—

—

CloudConnectMgmt

—

WxCC Services

https://*.ciscoservice.com

TCP 443

—

—

CloudConnectMgmt

—

Webex Identity

https://idbroker.webex.com

https://idbroker-eu.webex.com

https://idbroker-b-us.webex.com

TCP 443

—

—

CherryPoint

—

Webex Experience Management

TCP 443

—

Get remote host address from the Webex Experience Management

Ansible Controller

—

Cisco Devhub Artifactory

TCP 443

Outward from Ansible Controller to Cisco Devhub Artifactory

Used for communicating with Cisco Devhub Artifactory.

Feature Flag Mgmt

—

Split.io

Both

Outbound traffic

—

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote  Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| Cisco Unified Web Proxy Service (HTTPS) | TCP 8445 | Applications | — | Inward from applications to Cloud Connect Services. | — |

| Listener (Process or Application Protocol) | Listener Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| CherryPoint Service | TCP 3551 | CherryPoint Service on the other node in the same cluster. | — | Bidirectional | CherryPoint services use this port for secure cluster management. |
| Inventory Service | TCP 5551 | Inventory Service on the other node in the same cluster. | — | Bidirectional | Inventory services use this port for secure cluster
                                          management. |
| CloudConnectMgmt Service | TCP 6551 | CloudConnectMgmt Service on the other node in the same
                                          cluster. | — | Bidirectional | CloudConnectMgmt services use this port for secure cluster
                                          management. |
| Ansible Controller | — | SSH Server on Orchestration target node | TCP 22 | Outward from Ansible Controller to SSH Server on Orchestration target node | Used for connecting to target node for Orchestration. |
| Ansible Controller | — | SMTP Relay Server | TCP 25 | Outward from Ansible Controller to SMTP Relay Server | Used for sending email notification. |

| Note | When using a proxy for Cloud Connect integration, ensure the domains and URLs listed in the table below are added to the proxy
                                          allowlist. |
|---|---|

| (Process or Application Protocol) | Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| CloudConnectMgmt | — | Fusion Management Service https://hercules-a.wbx2.com , https://hercules-k.wbx2.com , https://hercules-r.wbx2.com | TCP 443 | — | — |
| CloudConnectMgmt | — | WxCC Services https://*.ciscoservice.com | TCP 443 | — | — |
| CloudConnectMgmt | — | Webex Identity https://idbroker.webex.com https://idbroker-eu.webex.com https://idbroker-b-us.webex.com | TCP 443 | — | — |
| CherryPoint | — | Webex Experience Management | TCP 443 | — | Get remote host address from the Webex Experience Management |
| Ansible Controller | — | Cisco Devhub Artifactory | TCP 443 | Outward from Ansible Controller to Cisco Devhub Artifactory | Used for communicating with Cisco Devhub Artifactory. |
| Feature Flag Mgmt | — | Split.io | Both | Outbound traffic | — |