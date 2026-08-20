---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-configurati-35236e8220
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/configuration/guide/ucce_b_port_utilization_12_6_2/rcct_m_1262_cisco-cloud-connect-port-utilization.html
retrieved_at: 2026-08-20T18:33:40.218566+00:00
---

Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.6(2)

# Port Utilization Guide for Cisco Unified Contact Center Solutions, Release 12.6(2)

Updated: November 30, 2025

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

Dataconn Service

TCP 2551

Dataconn Service on the other node in the same cluster.

—

Bidirectional (between two nodes in the same cluster)

Services use this port for secure cluster management.

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

Digital Routing Service (Redis Service)

TCP 6379

Digital Routing Service on the other node in the same cluster.

—

Bidirectional

Default Redis service port that is used by Digital Routing Service to connect locally, and for Redis instances on Publisher
                                          and Subscriber to replicate data between both the nodes.

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

Dataconn Service

—

Webex Engage API endpoints for user sync.

US region— https://api-us-site-1.imiengage.io , https://api-us-site-1.us.webexengage.com , and https://engage-api.produs1.ciscoccservice.com

London / UK— https://api-uk-site-1.imiengage.io , https://api-uk-site-1.uk.webexengage.com , and https://engage-api.prodeu1.ciscoccservice.com

EU region Ireland— https://api-eu-site-1.imiengage.io , https://api-eu-site-1.eu.webexengage.com , and https://engage-api.prodeu2.ciscoccservice.com

ANZ region— https://api-syd-site-1.imiengage.com.au , https://api-syd-site-1.anz.webexengage.com , and https://engage-api.prodanz1.ciscoccservice.com

Canada region— https://api-ca-site-1.imiengage.io , https://api-ca-site-1.ca.webexengage.com , and https://engage-api.prodca1.ciscoccservice.com

India region— https://engage-api.prodin1.ciscoccservice.com 1

TCP 443

Outbound traffic

—

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

Digital Routing

—

Webex Connect tenant specific Webhook endpoint

TCP 443

Outbound traffic

Asynchronous Webhook notifications sent from Digital Routing service to Webex Connect to invoke flows

Digital Routing

—

Region-specific OAuth access token URL of Webex Connect. For the list of URLs based on the location of Webex Connect data
                                          center, see the Integrate Cloud Connect with Webex Connect section in the Cisco Unified Contact Center Enterprise Features Guide

TCP 443

Outbound traffic

Used to generate tokens for Webhook notifications.

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
| Dataconn Service | TCP 2551 | Dataconn Service on the other node in the same cluster. | — | Bidirectional (between two nodes in the same cluster) | Services use this port for secure cluster management. |
| CherryPoint Service | TCP 3551 | CherryPoint Service on the other node in the same cluster. | — | Bidirectional | CherryPoint services use this port for secure cluster management. |
| Inventory Service | TCP 5551 | Inventory Service on the other node in the same cluster. | — | Bidirectional | Inventory services use this port for secure cluster
                                          management. |
| CloudConnectMgmt Service | TCP 6551 | CloudConnectMgmt Service on the other node in the same
                                          cluster. | — | Bidirectional | CloudConnectMgmt services use this port for secure cluster
                                          management. |
| Digital Routing Service (Redis Service) | TCP 6379 | Digital Routing Service on the other node in the same cluster. | — | Bidirectional | Default Redis service port that is used by Digital Routing Service to connect locally, and for Redis instances on Publisher
                                          and Subscriber to replicate data between both the nodes. |
| Ansible Controller | — | SSH Server on Orchestration target node | TCP 22 | Outward from Ansible Controller to SSH Server on Orchestration target node | Used for connecting to target node for Orchestration. |
| Ansible Controller | — | SMTP Relay Server | TCP 25 | Outward from Ansible Controller to SMTP Relay Server | Used for sending email notification. |

| Note | When using a proxy for Cloud Connect integration, ensure the domains and URLs listed in the table below are added to the proxy
                                          allowlist. |
|---|---|

| (Process or Application Protocol) | Protocol and Port | Remote Device (Process or Application Protocol) | Remote Port | Traffic Direction | Notes |
|---|---|---|---|---|---|
| Dataconn Service | — | Webex Engage API endpoints for user sync. US region— https://api-us-site-1.imiengage.io , https://api-us-site-1.us.webexengage.com , and https://engage-api.produs1.ciscoccservice.com London / UK— https://api-uk-site-1.imiengage.io , https://api-uk-site-1.uk.webexengage.com , and https://engage-api.prodeu1.ciscoccservice.com EU region Ireland— https://api-eu-site-1.imiengage.io , https://api-eu-site-1.eu.webexengage.com , and https://engage-api.prodeu2.ciscoccservice.com ANZ region— https://api-syd-site-1.imiengage.com.au , https://api-syd-site-1.anz.webexengage.com , and https://engage-api.prodanz1.ciscoccservice.com Canada region— https://api-ca-site-1.imiengage.io , https://api-ca-site-1.ca.webexengage.com , and https://engage-api.prodca1.ciscoccservice.com India region— https://engage-api.prodin1.ciscoccservice.com 1 | TCP 443 | Outbound traffic | — |
| CloudConnectMgmt | — | Fusion Management Service https://hercules-a.wbx2.com , https://hercules-k.wbx2.com , https://hercules-r.wbx2.com | TCP 443 | — | — |
| CloudConnectMgmt | — | WxCC Services https://*.ciscoservice.com | TCP 443 | — | — |
| CloudConnectMgmt | — | Webex Identity https://idbroker.webex.com https://idbroker-eu.webex.com https://idbroker-b-us.webex.com | TCP 443 | — | — |
| CherryPoint | — | Webex Experience Management | TCP 443 | — | Get remote host address from the Webex Experience Management |
| Digital Routing | — | Webex Connect tenant specific Webhook endpoint | TCP 443 | Outbound traffic | Asynchronous Webhook notifications sent from Digital Routing service to Webex Connect to invoke flows |
| Digital Routing | — | Region-specific OAuth access token URL of Webex Connect. For the list of URLs based on the location of Webex Connect data
                                          center, see the Integrate Cloud Connect with Webex Connect section in the Cisco Unified Contact Center Enterprise Features Guide | TCP 443 | Outbound traffic | Used to generate tokens for Webhook notifications. |
| Ansible Controller | — | Cisco Devhub Artifactory | TCP 443 | Outward from Ansible Controller to Cisco Devhub Artifactory | Used for communicating with Cisco Devhub Artifactory. |
| Feature Flag Mgmt | — | Split.io | Both | Outbound traffic | — |