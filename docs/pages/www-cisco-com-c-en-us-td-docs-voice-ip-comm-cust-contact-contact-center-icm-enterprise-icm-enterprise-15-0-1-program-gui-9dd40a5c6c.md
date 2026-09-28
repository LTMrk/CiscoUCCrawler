---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-9dd40a5c6c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce_m_status-api_1501.html
retrieved_at: 2026-08-16T20:19:02.808249+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: December 10, 2025

Chapter: Status API

## Chapter: Status API

- Status API

- Configuration Rules

- Operation                              	 Rules

# Status API

## Configuration Rules

### Unified CCE AW, Unified Intelligence Center, CUIC-LD-IdS, and Finesse
                              		  Machines

These rules show
                              		  the potential configuration errors and warnings for Unified CCE  AW, Unified Intelligence Center, CUIC-LD-IdS, and Finesse
                              machines.

SSO_COMPONENT_STATUS_MATCHES_GLOBAL

The  global SSO status must be the same as component SSO status.

SSO_VALID_IDS_REFERENCE

If single sign-on is enabled, this machine must be associated with a valid Cisco Identity Service.

TASK_ROUTING_APP_PATHS_EXIST

Each Peripheral Gateway with a Communications Manager PIM must have an associated Task Routing Application Path.

### Customer Collaboration Platform Machines

These rules show the potential configuration errors and warnings for  Customer Collaboration
                              				Platform machines.

Multichannel routing must be enabled on Customer Collaboration Platform.

### Cloud Connect Machines

These rules show the potential configuration errors and warnings for all of the
                              				machines, ESX hosts, and Gateways. Each section has a rule table that applies to all
                              				machines listed in that category, as well as a rule table for each type of machine
                              				in that category.

These rules show the potential configuration errors and warnings for Cloud Connect
                              				machines.

CLOUD_CONNECT_STATUS

Shows the sync status of Cloud Connect Machine.

## Operation
                        	 Rules

### Common Operation Rules

These rules show the potential operation errors and warnings for Unified CCE, Unified
                              				CM, Unified CVP, Gateways, Unified Intelligence Center, Finesse, and Enterprise Chat
                              				and Email. Each section has a rule table that applies to all machines listed in that
                              				category, as well as a rule table for each type of machine in that category.

These rules show the potential operation errors and warnings for the following
                              				machines:

All Unified CCE components

Unified Intelligence Center

CUIC-LD-IdS

Finesse

Live Data

Identity Service

Customer Collaboration Platform

The Diagnostic Portal, AXL, REST, or SOAP service on this machine
                                          									must be in service. The status you see varies according to the
                                          									product type, as follows:

Unified CCE: The Cisco ICM Diagnostic Framework service
                                                											on the Principal AW must be reachable on the network.

CUIC-LD-IdS: The SOAP service on the Publisher must be
                                                											reachable on the network.

Finesse: The SOAP service on the Primary Finesse machine
                                                											must be reachable on the network.

IdS: The REST service on the Primary Identity Server must
                                                											be reachable on the network

Customer Collaboration Platform : The service must be reachable on the network.

The inventory's credentials for the machine must be valid. The
                                          									status you see varies according to the product type, as follows:

Unified CCE: The Diagnostic Framework credentials entered
                                                											for the Principal AW must be valid for all CCE
                                                											components in the solution.

CUIC-LD-IdS: The Unified Intelligence Center
                                                											Administration credentials entered for the Publisher
                                                											must be valid

Finesse: The Finesse Administration credentials entered
                                                											for the Primary Finesse machine must be valid.

IdS: The Identity Service Administration credentials
                                                											entered for the Primary Identity Server must be valid

Customer Collaboration Platform : The service credentials must be valid.

This rule does not apply to a standalone Live Data machine.

### Cloud Connect Machines

These rules show the potential operational errors and
                           			warnings for Cloud Connector machines.

CLOUD_CONNECTOR_TYPE

Cloud connect is either publisher or subscriber.

CONTACT_CENTER_AI_CALL_TYPE_CONFIG_NOT_FOUND

Some of the Contact Center AI configurations that are associated
                                          									with the call types are not available in the Control Hub.

| Rule | Description |
|---|---|
| SSO_COMPONENT_STATUS_MATCHES_GLOBAL | The  global SSO status must be the same as component SSO status. |
| SSO_VALID_IDS_REFERENCE | If single sign-on is enabled, this machine must be associated with a valid Cisco Identity Service. |

| Rule | Description |
|---|---|
| TASK_ROUTING_APP_PATHS_EXIST | Each Peripheral Gateway with a Communications Manager PIM must have an associated Task Routing Application Path. |

| Rule | Description |
|---|---|
| SOCIAL_MINER_MR_ENABLED | Multichannel routing must be enabled on Customer Collaboration Platform. |

| Rule | Description |
|---|---|
| CLOUD_CONNECT_STATUS | Shows the sync status of Cloud Connect Machine. |

| Rule | Description |
|---|---|
| SERVER_CONNECTION | The Diagnostic Portal, AXL, REST, or SOAP service on this machine
                                          									must be in service. The status you see varies according to the
                                          									product type, as follows: Unified CCE: The Cisco ICM Diagnostic Framework service
                                                											on the Principal AW must be reachable on the network. CUIC-LD-IdS: The SOAP service on the Publisher must be
                                                											reachable on the network. Finesse: The SOAP service on the Primary Finesse machine
                                                											must be reachable on the network. IdS: The REST service on the Primary Identity Server must
                                                											be reachable on the network Customer Collaboration Platform : The service must be reachable on the network. |
| SERVER_CREDENTIALS | The inventory's credentials for the machine must be valid. The
                                          									status you see varies according to the product type, as follows: Unified CCE: The Diagnostic Framework credentials entered
                                                											for the Principal AW must be valid for all CCE
                                                											components in the solution. CUIC-LD-IdS: The Unified Intelligence Center
                                                											Administration credentials entered for the Publisher
                                                											must be valid Finesse: The Finesse Administration credentials entered
                                                											for the Primary Finesse machine must be valid. IdS: The Identity Service Administration credentials
                                                											entered for the Primary Identity Server must be valid Customer Collaboration Platform : The service credentials must be valid. Note This rule does not apply to a standalone Live Data machine. | Note | This rule does not apply to a standalone Live Data machine. |
| Note | This rule does not apply to a standalone Live Data machine. |

| Note | This rule does not apply to a standalone Live Data machine. |
|---|---|

| Rule | Description |
|---|---|
| CLOUD_CONNECTOR_TYPE | Cloud connect is either publisher or subscriber. |
| CONTACT_CENTER_AI_CALL_TYPE_CONFIG_NOT_FOUND | Some of the Contact Center AI configurations that are associated
                                          									with the call types are not available in the Control Hub. |