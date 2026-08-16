---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-program-gui-0817042d85
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/program/guide/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5_chapter_011100.html
retrieved_at: 2026-08-16T20:29:22.556411+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

Updated: February 6, 2020

Chapter: Status API

## Chapter: Status API

- Status API

- Configuration Rules

- Operation                              	 Rules

# Status API

The Status API
                        		retrieves information about the state of rules that  collectively determine if the system is working correctly.

The system
                        		periodically checks the state of the rules. To force the status to be updated, refer to the Scan API .

## URL

## Operations

get :
                                 				Returns the status rule results, using the URL https://<server>/unifiedconfig/config/status .

## Response
                           		  Parameters

name: The name of the status. See the Configuration Rules and Operation Rules .

category: The
                                 				status category of Configuration or Operation.

level: The
                                 				severity of the condition. Values include: OK, ERROR, and
                                 				BLOCKED. The BLOCKED level indicates that the rule has not been processed yet
                                 				or that the failure of another rule prevents this rule from running.

machine: A collection for the machine ( Machine Inventory API )
                                 				including the machine's name, type, and refURL. See References .

## Example Get
                           		  Response

```
<results>
    <statuses>
        <status>
            <name>CUSTOMER_COLLABORATION_PLATFORM_MR_ENABLED</name>
	           <category>CONFIGURATION</category>
	           <level>BLOCKED</level>
	           <machines>
                <machine>
                    <refURL>/unifiedconfig/config/
                     machineinventory/6110</refURL>
                     <machineType>EXTERNAL_CUSTOMER_COLLABORATION_PLATFORM
                     </machineType>
                     <name>Machine_2563_00002</name>
                </machine>
             </machines>
         </status>
         <status>
             <name>SERVER_CONNECTION</name>
             <category>OPERATION</category>
             <level>OK</level>
             <machines>
                 <machine>
                     <refURL>/unifiedconfig/config/
                      machineinventory/6110</refURL>
                     <machineType>EXTERNAL_CUSTOMER_COLLABORATION_PLATFORM
                     </machineType>
                     <name>Machine_2563_00002</name>
                  </machine>
             </machines>
          </status>
          <status>
              <name>SERVER_CREDENTIALS</name>
              <category>OPERATION</category>
              <level>OK</level>
              <machines>
                  <machine>
                      <refURL>/unifiedconfig/config/
                      machineinventory/6110</refURL>
                      <machineType>EXTERNAL_CUSTOMER_COLLABORATION_PLATFORM
                      </machineType>
                      <name>Machine_2563_00002</name>
                  </machine>
              </machines>
           </status>
    </statuses>
</results>
```

## Configuration Rules

### Common Rules for All Machines

These rules show the potential configuration errors and warnings for all machines.

CAN_RESOLVE_ADDRESS_TO_FQDN

Machine address must be resolvable to a fully qualified domain
                                          									name (FQDN).

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

CONTACT_CENTER_AI_GLOBAL_CONFIG_NOT_FOUND

The Contact Center AI configuration that is associated as a
                                          									Global configuration is not available in the Control Hub.

| Rule | Description |
|---|---|
| CAN_RESOLVE_ADDRESS_TO_FQDN | Machine address must be resolvable to a fully qualified domain
                                          									name (FQDN). |

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
| CONTACT_CENTER_AI_GLOBAL_CONFIG_NOT_FOUND | The Contact Center AI configuration that is associated as a
                                          									Global configuration is not available in the Control Hub. |