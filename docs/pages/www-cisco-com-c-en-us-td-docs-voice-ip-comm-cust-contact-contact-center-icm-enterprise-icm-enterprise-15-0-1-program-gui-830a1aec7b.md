---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-830a1aec7b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_status-api_1501.html
retrieved_at: 2026-08-21T16:48:50.686620+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Status API

## Chapter: Status API

# Status API

## Configuration
                        	 Rules

These rules show the
                           		potential configuration errors and warnings for all of the machines, ESX hosts,
                           		and Gateways. Each section has a rule table that applies to all machines listed
                           		in that category, as well as a rule table for each type of machine in that
                           		category.

### CCE
                              		  Machines

These rules show the potential configuration errors and warnings for CCE machines (Unified CCE Rogger, Unified CCE PG, Unified CCE PG on Remote Data Center, Unified CCE AW-HDS-DDS, Unified CCE External HDS).

TRACE_LEVEL_NORMAL

The trace level must be set to normal to ensure performance.

CAN_RESOLVE_ADDRESS_TO_FQDN

The machine address must be resolvable to a fully qualified domain name (FQDN).

LOGGER_INSTALLED

The logger service must be installed.

LOGGER_AUTOMATIC

The logger service startup type must be set to automatic.

NO_EXTRA_SERVICES_INSTALLED_ROGGER

Only required services can be installed.

ROUTER_INSTALLED

The router service must be installed.

ROUTER_AUTOMATIC

The router service startup type must be set to automatic.

ROUTER_APPGW_MUST_BE_ENABLED

Application Gateway must be enabled on the router using Unified CCE Web Setup.

CTI_SVR_INSTALLED

The CTI Server service must be installed.

CTI_SVR_AUTOMATIC

The CTI server service startup type must be set to automatic.

DIALER_INSTALLED

If installed, the dialer service must be installed on both sides.

DIALER_AUTOMATIC

If installed, the dialer service startup type must be set to automatic.

DIALER_INSTALLED_OUTBOUND_ENABLED

The dialer services must be installed when outbound is enabled.

MR_PG_MR_PIM_CONFIGURED_FOR_MULTICHANNEL _MACHINES

A Media Routing Peripheral must be configured in Peripheral Gateway Setup for each multichannel machine in the solution inventory.
                                          Multichannel machine types include:

- EXTERNAL_SOCIAL_MINER

- EXTERNAL_ECE

- EXTERNAL_THIRD_PARTY_MULTICHANNEL

MR_PG_APPLICATION_SERVER_HOSTNAME _NO_DUPLICATES

Application Server Host Name for each peripheral must be unique.

MR_PG_MULTICHANNEL_APPLICATION_SERVER _HOSTNAME_BOTH_SIDES_MATCH

Application Server Host Name for Media Routing Peripheral Multichannel must be the same on both sides.

MR_PG_MULTICHANNEL2_APPLICATION_SERVER _HOSTNAME_BOTH_SIDES_MATCH

Application Server Host Name for Media Routing Peripheral Multichannel2 must be the same on both sides.

MR_PG_MULTICHANNEL3_APPLICATION_SERVER _HOSTNAME_BOTH_SIDES_MATCH

Application Server Host Name for Media Routing Peripheral Multichannel3 must be the same on both sides.

MR_PG_MULTICHANNEL_APPLICATION_SERVERS _HOSTNAME_FOUND_IN_INVENTORY

Application Server Host Names used in Peripheral Gateway Setup for all multichannel peripherals must be created as external
                                          machines in the solution inventory. The machine type must be one of the following:

- EXTERNAL_SOCIAL_MINER )

- EXTERNAL_ECE

- EXTERNAL_THIRD_PARTY_MULTICHANNEL

MR_PG_MR_PIM_COUNT

The number of media routing PG MR_PIM processes (mr_pim.exe) on Side A and Side B must match. Valid if 0 to 4 MR_PIMS are
                                          enabled.

MR_PG_INSTALLED

The Media Routing PG service must be installed.

MR_PG_AUTOMATIC

The Media Routing PG service must be set to automatic.

NO_EXTRA_SERVICES_INSTALLED_PG

Only required and optional services can be installed (extra services such as an additional PG or CTI Server are not permitted).

UCM_PG_APPUSER_BOTH_SIDES_MATCH

The Communications Manager PIM application user configured on Side A must be identical to the user configured on Side B.

UCM_PG_APPUSER_FOUND_ON_CUCM

The Communications Manager PIM application user must be configured on the Communications Manager as an application user.

UCM_PG_JTAPI_MATCHES_CM_SUB

The Communications Manager PIM service address configured in PG Setup must match the Communications Manager Subscriber address
                                          on the same side.

UCM_PG_JTAPI_CLIENT_VERSION _MATCH_UCM

The JTAPI Client version installed must match the JTAPI Client version available on Unified Call Manager.

UCM_PG_INSTALLED

The UCM PG service must be installed.

UCM_PG_AUTOMATIC

The UCM PG service startup type must be set to automatic.

VRU_PG_INSTALLED

The VRU PG service must be installed.

VRU_PG_AUTOMATIC

The VRU PG service startup type must be set to automatic.

When you configure Agent PG

CTI_SVR_INSTALLED

The CTI Server service must be installed.

CTI_SVR_AUTOMATIC

The CTI server service startup type must be set to automatic.

DIALER_INSTALLED

If installed, the dialer service must be installed on both sides.

DIALER_AUTOMATIC

If installed, the dialer service startup type must be set to automatic.

UCM_PG_INSTALLED

The UCM PG service must be installed.

UCM_PG_AUTOMATIC

The UCM PG service startup type must be set to automatic.

UCM_PG_JTAPI_MATCHES_CM_SUB

The Communications Manager PIM service address configured in PG Setup must match the Communications Manager Subscriber address
                                          on the same side.

When you configure MR PG

MR_PG_INSTALLED

The Media Routing PG service must be installed.

MR_PG_AUTOMATIC

The Media Routing PG service must be set to automatic.

When you configure VRU PG

VRU_PG_INSTALLED

The VRU PG service must be installed.

VRU_PG_AUTOMATIC

The VRU PG service startup type must be set to automatic.

When you configure any type of PG

NO_EXTRA_SERVICES_INSTALLED_PG

Only required and optional services can be installed (extra services such as an additional PG or CTI Server are not permitted).

SSO_COMPONENT_STATUS_MATCHES_GLOBAL

The global SSO status must be the same as component SSO status.

SSO_VALID_IDS_REFERENCE

If single sign-on is enabled, this machine must be associated with a valid Cisco Identity Service.

DISTRIBUTOR_CONAPI_MUST_BE_DISABLED

Configuration Management Service (CMS) Node and Agent Re-skilling Web Tool must be disabled using Unified CCE Web Setup.

DISTRIBUTOR_INSTALLED

The distributor service must be installed.

DISTRIBUTOR_AUTOMATIC

The distributor service startup type must be set to automatic.

NO_EXTRA_SERVICES_INSTALLED_AW

Only required services can be installed.

TASK_ROUTING_APP_PATHS_EXIST

Each Peripheral Gateway with a Communications Manager PIM must have an associated Task Routing Application Path.

SSO_COMPONENT_STATUS_MATCHES_GLOBAL

The global SSO status must be the same as component SSO status.

SSO_VALID_IDS_REFERENCE

If single sign-on is enabled, this machine must be associated with a valid Cisco Identity Service.

DISTRIBUTOR_CONAPI_MUST_BE_DISABLED

Configuration Management Service (CMS) Node and Agent Re-skilling Web Tool must be disabled using Unified CCE Web Setup.

TASK_ROUTING_APP_PATHS_EXIST

Each Peripheral Gateway with a Communications Manager PIM must have an associated Task Routing Application Path.

### Gateways

These rules show the potential configuration errors and warnings for gateways.

- voice-class codec #num

dial-peer voice #num voip (codec ).The supported voice
                                                											codecs are g711alaw, g711ulaw, g729r8, mp4a-latm and
                                                											g722-64 for the above four dial peers to CVP call
                                                											servers (if the dial peers are configured on
                                                											the voice gateway). The supported video codec is h264.
                                                											The dial peer is identified via "session target
                                                											ipaddress xxxxx". The IP address must point to the IP
                                                											address of CVP call server.

The dial peers for each CVP call server on each gateway must be configured with the supported session protocol, sipv2.

### CUIC-LD-IdS Machines

These rules show the potential configuration errors and warnings for CUIC-LD-IdS machines.

SSO_COMPONENT_STATUS_MATCHES_GLOBAL

The global SSO status must be the same as component SSO status.

SSO_VALID_IDS_REFERENCE

If single sign-on is enabled, this machine must be associated with a valid Cisco Identity Service.

CAN_RESOLVE_ADDRESS_TO_FQDN

The machine address must be resolvable to an FQDN.

CUIC_REALTIME_DS_CORRECT_HOST

The realtime datasource must be configured with the correct hosts: either the Side A and B Unified CCE AW-HDS-DDS Servers,
                                          or, if used, the External HDS.

CUIC_HISTORICAL_DS_CORRECT_HOST

The historical datasource must be configured with the correct hosts: either the Side A and B Unified CCE AW-HDS-DDS Servers,
                                          or, if used, the External HDS.

### Finesse Machines

These rules show the potential configuration errors and warnings for Finesse machines.

SSO_COMPONENT_STATUS_MATCHES_GLOBAL

The global SSO status must be the same as the component SSO status.

SSO_VALID_IDS_REFERENCE

If single sign-on is enabled, this machine must be associated with a valid Cisco Identity Service.

CAN_RESOLVE_ADDRESS_TO_FQDN

The machine address must be resolvable to an FQDN.

### Unified CVP Machines

These rules show the potential configuration errors and warnings for CVP machines.

TRACE_LEVEL_NORMAL

The trace level must be set to normal to ensure performance.

CAN_RESOLVE_ADDRESS_TO_FQDN

The machine address must be resolvable to an FQDN.

The CVP SIP Server Group names that contain Communication Manager addresses must match the Communication Manager Cluster Fully
                                          Qualified Domain Name.

The CVP SIP Server Groups that contain Communication Manager addresses cannot contain non-Communication Manager addresses
                                          (which include Communication Manager hosts that are not part of the inventory).

The Ring Tone Dialed Number configured on the CVP Call Server should match the pattern 91*.

The Error Tone Dialed Number configured on the CVP Call Server should match the pattern 92*.

### Unified CM Machines

These rules show the potential configuration errors and warnings for Unified CM machines.

TRACE_LEVEL_NORMAL

The trace level must be set to normal to ensure performance.

CAN_RESOLVE_ADDRESS_TO_FQDN

The machine address must be resolvable to an FQDN.

CUCM_FQDN_DEFINED

The Communication Manager Cluster Fully Qualified Domain Name must be defined.

CVP_SERVER_MUST_HAVE_A_CM_SIP_TRUNK

Each CVP Server must be referenced by at least one Communications Manager SIP Trunk destination.

### ESX Hosts

These rules show the potential configuration errors and warnings for ESX hosts.

VMHOST_ESXI_VERSION_MATCH

Side A and Side B VM Hosts must be on the same ESXi version.

VM_DATASTORE

Virtual machines must be deployed on the correct datastore.

### SocialMiner

These rules show the potential configuration errors and warnings for SocialMiner machines.

SOCIAL_MINER_MR_ENABLED

Multichannel routing must be enabled on SocialMiner .

CAN_RESOLVE_ADDRESS_TO_FQDN

The machine address must be resolvable to an FQDN.

### Cloud Connect Machines

These rules show the potential configuration errors and warnings for Cloud Connect machines.

CLOUD_CONNECT_REGISTRATION_STATUS

Shows the Registration Status of Cloud Service.

CLOUD_CONNECT_

WXM_SURVEY_MISSING

Shows the Call Type survey status which does not exist in Webex Experience.

CLOUD_CONNECT_

WXM_SURVEY_WRONG_MULTICHANNEL

Shows the status of the Call Types with deferred surveys which are configured in Media Routing Dialled Numbers.

CLOUD_CONNECT_

WXM_SURVEY_WRONG_CHANNEL

Shows the survey status of Webex Experience with unsupported channels.

## Operation
                        	 Rules

These rules show the
                           		potential operation errors and warnings for Unified CCE, Unified CM, Unified
                           		CVP, Gateways, Unified Intelligence Center, Finesse, and Enterprise Chat and
                           		Email. Each section has a rule table that applies to all machines listed in
                           		that category, as well as a rule table for each type of machine in that
                           		category.

### Unified CCE
                              		  Machines

These rules show
                              		  the potential operation errors and warnings for Unified CCE machines (Rogger,
                              		  PG, Unified CCE PG on Remote
                                 			 Data Center, and AW-HDS-DDS).

Rule

Description

LOGGER_CAMPAIGN_MGR_RUNNING

The logger campaign manager process (campaignmanager.exe) must be running.

LOGGER_CONFIG_LOGGER_RUNNING

The logger configuration logger process (configlogger.exe) must be running.

LOGGER_CSFS_RUNNING

The logger customer support forwarding service process (csfs.exe) must be running.

LOGGER_HIST_LOGGER_RUNNING

The logger historical logger process (histlogger.exe) must be running.

LOGGER_BA_IMPORT_RUNNING

The logger import process (baimport.exe) must be running.

LOGGER_RECOVERY_RUNNING

The logger recovery process (recovery.exe) must be running.

LOGGER_REPLICATION_RUNNING

The logger replication process (replication.exe) must be running.

LOGGER_RUNNING

The logger service must be running.

SERVER_CREDENTIALS

The Diagnostic Framework credentials entered for the Principal AW must be valid.

SERVER_CONNECTION

The Cisco ICM Diagnostic Framework service on this machine must be reachable on the network.

ROUTER_CCAGENT_INSVC_ACTIVE_ENABLE_COUNT

The router central controller agent process (ccagent.exe) must be in service for both PGs.

ROUTER_CCAGENT_RUNNING

The router central controller agent process (ccagent.exe) must be running.

ROUTER_DBAGENT_RUNNING

The router database agent process (dbagent.exe) must be running.

ROUTER_LIVE_DATA_ACTIVE_IDLE

The router Live Data connection must be active on one side and idle on the other side.

ROUTER_MDSPROC_IN_SVC_PR_ENB_DSB

The router message delivery service process (mdsproc.exe) must be enabled on one side and disabled on the other side.

ROUTER_MDSPROC_RUNNING

The router message delivery service process (mdsproc.exe) must be running.

ROUTER_ROUTER_RUNNING

The router process (router.exe) must be running.

ROUTER_RUNNING

The router service must be running.

Rule

Description

CTI_SVR_CTI_SVR_ACTIVE_ STANDBY

The CTI server process (ctisvr.exe) must be active on one side and standby/idle on the other side.

For PGs on version 12.6(1) or later, the expected state of the CTI Server on the other side is Standby . On earlier PG versions, the expected state is Idle .

CTI_SVR_CTI_SVR_RUNNING

The CTI server process (ctisvr.exe) must be running.

CTI_SVR_RUNNING

The CTI Server service must be running.

DIALER_RUNNING

If dialer is installed, then the dialer service must be running.

DIALER_BA_DIALER_SIP_ACTIVE_IDLE

The dialer process (badialer_sip.exe) must be active on one side and idle on the other side.

DIALER_BA_DIALER_SIP_RUNNING

The dialer process (badialer_sip.exe) must be running.

MR_PG_MR_PIM_ACTIVE_IDLE

Each MR_PIM process (mr_pim.exe) must be active on one side and idle on the other side.

MR_PG_MDSPROC_IN_SVC_PR_ENB_DSB

The media routing PG message delivery service process (mdsproc.exe) must be enabled on one side and disabled on the other
                                          side.

MR_PG_MDSPROC_RUNNING

The media routing PG message delivery service process (mdsproc.exe) must be running.

MR_PG_PG_AGENT_ACTIVE_IDLE

The media routing PG PG agent process (pgagent.exe) must be active on one side and idle on the other side.

MR_PG_PG_AGENT_RUNNING

The media routing PG PG agent process (pgagent.exe) must be running.

MR_PG_RUNNING

The media routing PG service must be running.

SERVER_CREDENTIALS

The Diagnostic Framework credentials entered for the Principal AW must be valid.

SERVER_CONNECTION

The Cisco ICM Diagnostic Framework service on this machine must be reachable on the network.

UCM_PG_JTAPI_ACTIVE_IDLE

The UCM PG jtapi process (jtapigw.exe) must be active on one side and idle on the other side.

UCM_PG_JTAPI_RUNNING

The UCM PG jtapi process (jtapigw.exe) must be running.

UCM_PG_LIVE_DATA_ACTIVE_IDLE

The UCM PG Live Data connection must be active on one side and idle on the other side.

UCM_PG_MDSPROC_IN_SVC_PR_ENB_DSB

The UCM PG message delivery service process (mdsproc.exe) must be enabled on one side and disabled on the other side.

UCM_PG_MDSPROC_RUNNING

The UCM PG message delivery service process (mdsproc.exe) must be running.

UCM_PG_PIM_COUNT

The number of UCM PG's PIM processes (eagtpim.exe) on Side A and Side B must match. Valid if 1 PIM is enabled.

UCM_PG_PG_AGENT_ACTIVE_IDLE

The UCM PG PG agent process (pgagent.exe) must be active on one side and idle on the other side.

UCM_PG_PG_AGENT_RUNNING

The UCM PG PG agent process (pgagent.exe) must be running.

UCM_PG_RUNNING

The UCM PG service must be running.

VRU_PG_VRU_PIM_ACTIVE_IDLE

Each VRU PIM process (vrupim.exe) must be active on one side and idle on the other side.

VRU_PG_MDSPROC_IN_SVC_PR_ENB_DSB

The VRU PG message delivery service process (mdsproc.exe) must be enabled on one side and disabled on the other side.

VRU_PG_MDSPROC_IN_SVC_PR_ENB_DSB

The VRU PG message delivery service process (mdsproc.exe) must be enabled on one side and disabled on the other side.

VRU_PG_MDSPROC_RUNNING

The VRU PG message delivery service process (mdsproc.exe) must be running.

VRU_PG_PIM_COUNT

The number of VRU PG's PIM processes (vrupim.exe) on Side A and Side B must match. Valid if 0 to 2 VRU PIMs are enabled.

VRU_PG_PG_AGENT_ACTIVE_IDLE

The VRU PG PG agent process (pgagent.exe) must be active on one side and idle on the other side.

VRU_PG_PG_AGENT_RUNNING

The VRU PG PG agent process (pgagent.exe) must be running.

VRU_PG_RUNNING

The VRU PG service must be running.

Rule

Description

When you configure Agent PG

CTI_SVR_RUNNING

The CTI Server service must be running.

CTI_SVR_CTI_SVR_RUNNING

The CTI server process (ctisvr.exe) must be running.

CTI_SVR_CTI_SVR_ACTIVE_ STANDBY

The CTI server process (ctisvr.exe) must be active on one side and standby on the other side.

DIALER_RUNNING

If dialer is installed, then the dialer service must be running.

DIALER_BA_DIALER_SIP_RUNNING

If dialer is installed, the dialer process (badialer_sip.exe) must be running.

DIALER_BA_DIALER_SIP_ACTIVE_IDLE

If dialer is installed, the dialer process (badialer_sip.exe) must be active on one side and idle on the other side.

UCM_PG_RUNNING

The UCM PG service must be running.

UCM_PG_LIVE_DATA_ACTIVE_IDLE

The UCM PG Live Data connection must be active on one side and idle on the other side.

UCM_PG_JTAPI_RUNNING

The UCM PG jtapi process (jtapigw.exe) must be running.

UCM_PG_JTAPI_ACTIVE_IDLE

The UCM PG jtapi process (jtapigw.exe) must be active on one side and idle on the other side.

UCM_PG_MDSPROC_RUNNING

The UCM PG message delivery service process (mdsproc.exe) must be running.

UCM_PG_MDSPROC_IN_SVC_PR_ENB_DSB

The UCM PG message delivery service process (mdsproc.exe) must be enabled on one side and disabled on the other side.

UCM_PG_PG_AGENT_RUNNING

The UCM PG PG agent process (pgagent.exe) must be running.

UCM_PG_PG_AGENT_ACTIVE_IDLE

The UCM PG PG agent process (pgagent.exe) must be active on one side and idle on the other side.

UCM_PG_PIM_COUNT

The number of UCM PG's PIM processes (eagtpim.exe) on Side A and Side B must match. Valid if 1 PIM is enabled.

When you configure MR PG

MR_PG_RUNNING

The media routing PG service must be running.

When you configure VRU PG

VRU_PG_RUNNING

The VRU PG service must be running.

VRU_PG_PG_AGENT_RUNNING

The VRU PG PG agent process (pgagent.exe) must be running.

VRU_PG_PG_AGENT_ACTIVE_IDLE

The VRU PG PG agent process (pgagent.exe) must be active on one side and idle on the other side.

VRU_PG_MDSPROC_RUNNING

The VRU PG message delivery service process (mdsproc.exe) must be running.

VRU_PG_MDSPROC_IN_SVC_PR_ENB_DSB

The VRU PG message delivery service process (mdsproc.exe) must be enabled on one side and disabled on the other side.

VRU_PG_PIM_COUNT

The number of VRU PG's PIM processes (vrupim.exe) on Side A and Side B must match. Valid if 0 to 2 VRU PIMs are enabled.

VRU_PG_VRU_PIM_ACTIVE_IDLE

Each VRU PIM process (vrupim.exe) must be active on one side and idle on the other side.

When you configure any type of PG

SERVER_CREDENTIALS

The Diagnostic Framework credentials entered for the Principal AW must be valid.

SERVER_CONNECTION

The Cisco ICM Diagnostic Framework service on this machine must be reachable on the network.

Rule

Description

DISTRIBUTOR_CONFIG_LOGGER_RUNNING

The distributor configuration logger process (configlogger.exe) must be running.

DISTRIBUTOR_RT_CLIENT_RUNNING

The distributor real-time client process (rtclient.exe) must be running.

DISTRIBUTOR_RT_DIST_RUNNING

The distributor real-time distributor process (rtdist.exe) must be running.

DISTRIBUTOR_RUNNING

This rule is not applicable for the external HDS

The distributor service must be running.

DISTRIBUTOR_UPDATE_AW_RUNNING

The distributor update process (updateaw.exe) must be running.

DEPLOYMENT_TASKS_PASSING

The deployment tasks must all be passing.

SERVER_CREDENTIALS

The Diagnostic Framework credentials entered for the Principal AW must be valid.

SERVER_CONNECTION

The Cisco ICM Diagnostic Framework service on this machine must be reachable on the network.

### Unified CM Machines

These rules show the potential operation errors and warnings for Unified CM machines.

SERVER_CREDENTIALS

The AXL service credentials entered for the Publisher must be valid.

SERVER_CONNECTION

The AXL service on the Publisher must be reachable on the network.

### Unified CVP Machines

These rules show the potential operation errors and warnings for CVP machines.

SERVER_CREDENTIALS

The Cisco CVP WebServicesManager credentials entered for the CVP Server must be valid.

SERVER_CONNECTION

The Cisco CVP WebServicesManager service on CVP Server must be reachable on the network.

### Gateways

These rules show the potential operation errors and warnings for gateways.

SERVER_CREDENTIALS

The service credentials entered for the gateway in Unified CVP Ops Console must be valid.

SERVER_CONNECTION

The service must be reachable on the network.

### Unified Intelligence Center Machines

These rules show the potential operation errors and warnings for Unified Intelligence Center machines.

SERVER_CREDENTIALS

The Unified Intelligence Center Administration credentials entered for the Publisher must be valid.

SERVER_CONNECTION

The SOAP service on the Publisher must be reachable on the network.

### Finesse

These rules show the potential operation errors and warnings for Finesse.

FINESSE_SYSTEM_STATUS

Finesse must be in service.

SERVER_CREDENTIALS

The Finesse Administration credentials entered for the Primary Finesse machine must be valid.

SERVER_CONNECTION

The SOAP service on the Primary Finesse machine must be reachable on the network.

FINESSE_TOMCAT_SERVICE_STARTED

The Tomcat service must be started.

### SocialMiner Machines

These rules show the potential operation errors and warnings for SocialMiner machines.

Rule

Description

SERVER_CREDENTIALS

The service credentials must be valid.

SERVER_CONNECTION

The service must be reachable on the network.

### Cloud Connect Machines

These rules show the potential operational errors and warnings for Cloud Connector machines.

CLOUD_CONNECTOR_TYPE

Cloud connect is either publisher or subscriber.

CONTACT_CENTER_AI_CALL_TYPE_CONFIG_NOT_FOUND

Some of the Contact Center AI configurations that are associated with the call types are not available in the Control Hub.

This rule is applicable only for Packaged CCE 2000 Agents deployment.

## System Health
                        	 Rules

System health data
                           		is collected on a 20 second interval. The values represent the 95th percentile
                           		calculated over the preceding 10 minute period.

### Usage Errors
                              		  and Warnings

The following
                              		  system health rules show the usage errors and warnings for all virtual
                              		  machines. The DISK_USAGE rule applies to all disks in the system.

Principal_AW_Status

To identify if the Principal AW machine is up or down.

This rule is applicable only for Packaged CCE 4000 Agents and 12000 Agents Deployments

CCE_AW

Principal_VVB_Status

To identify if the Principal VVB machine is up or down.

This rule is applicable only for Packaged CCE 4000 and 12000 Agent Deployments.

EXTERNAL_CVVB

DC_EXTERNAL_CVVB

### Datastore
                              		  Metrics

The following
                              		  system health rules apply to all VM Hosts. Each rule output in the status
                              		  detail identifies the datastore affected and the value for that particular
                              		  metric.

## VM Rules

These rules show the
                           		potential errors and warnings for virtual machines.

| Rule | Description |
|---|---|
| TRACE_LEVEL_NORMAL | The trace level must be set to normal to ensure performance. |
| CAN_RESOLVE_ADDRESS_TO_FQDN | The machine address must be resolvable to a fully qualified domain name (FQDN). |

| Rule | Description |
|---|---|
| LOGGER_INSTALLED | The logger service must be installed. |
| LOGGER_AUTOMATIC | The logger service startup type must be set to automatic. |
| NO_EXTRA_SERVICES_INSTALLED_ROGGER | Only required services can be installed. |
| ROUTER_INSTALLED | The router service must be installed. |
| ROUTER_AUTOMATIC | The router service startup type must be set to automatic. |
| ROUTER_APPGW_MUST_BE_ENABLED | Application Gateway must be enabled on the router using Unified CCE Web Setup. |

| Rule | Description |
|---|---|
| CTI_SVR_INSTALLED | The CTI Server service must be installed. |
| CTI_SVR_AUTOMATIC | The CTI server service startup type must be set to automatic. |
| DIALER_INSTALLED | If installed, the dialer service must be installed on both sides. |
| DIALER_AUTOMATIC | If installed, the dialer service startup type must be set to automatic. |
| DIALER_INSTALLED_OUTBOUND_ENABLED | The dialer services must be installed when outbound is enabled. |
| MR_PG_MR_PIM_CONFIGURED_FOR_MULTICHANNEL _MACHINES | A Media Routing Peripheral must be configured in Peripheral Gateway Setup for each multichannel machine in the solution inventory.
                                          Multichannel machine types include: EXTERNAL_SOCIAL_MINER EXTERNAL_ECE EXTERNAL_THIRD_PARTY_MULTICHANNEL |
| MR_PG_APPLICATION_SERVER_HOSTNAME _NO_DUPLICATES | Application Server Host Name for each peripheral must be unique. |
| MR_PG_MULTICHANNEL_APPLICATION_SERVER _HOSTNAME_BOTH_SIDES_MATCH | Application Server Host Name for Media Routing Peripheral Multichannel must be the same on both sides. |
| MR_PG_MULTICHANNEL2_APPLICATION_SERVER _HOSTNAME_BOTH_SIDES_MATCH | Application Server Host Name for Media Routing Peripheral Multichannel2 must be the same on both sides. |
| MR_PG_MULTICHANNEL3_APPLICATION_SERVER _HOSTNAME_BOTH_SIDES_MATCH | Application Server Host Name for Media Routing Peripheral Multichannel3 must be the same on both sides. |
| MR_PG_MULTICHANNEL_APPLICATION_SERVERS _HOSTNAME_FOUND_IN_INVENTORY | Application Server Host Names used in Peripheral Gateway Setup for all multichannel peripherals must be created as external
                                          machines in the solution inventory. The machine type must be one of the following: EXTERNAL_SOCIAL_MINER ) EXTERNAL_ECE EXTERNAL_THIRD_PARTY_MULTICHANNEL |
| MR_PG_MR_PIM_COUNT | The number of media routing PG MR_PIM processes (mr_pim.exe) on Side A and Side B must match. Valid if 0 to 4 MR_PIMS are
                                          enabled. |
| MR_PG_INSTALLED | The Media Routing PG service must be installed. |
| MR_PG_AUTOMATIC | The Media Routing PG service must be set to automatic. |
| NO_EXTRA_SERVICES_INSTALLED_PG | Only required and optional services can be installed (extra services such as an additional PG or CTI Server are not permitted). |
| UCM_PG_APPUSER_BOTH_SIDES_MATCH | The Communications Manager PIM application user configured on Side A must be identical to the user configured on Side B. |
| UCM_PG_APPUSER_FOUND_ON_CUCM | The Communications Manager PIM application user must be configured on the Communications Manager as an application user. |
| UCM_PG_JTAPI_MATCHES_CM_SUB | The Communications Manager PIM service address configured in PG Setup must match the Communications Manager Subscriber address
                                          on the same side. |
| UCM_PG_JTAPI_CLIENT_VERSION _MATCH_UCM | The JTAPI Client version installed must match the JTAPI Client version available on Unified Call Manager. |
| UCM_PG_INSTALLED | The UCM PG service must be installed. |
| UCM_PG_AUTOMATIC | The UCM PG service startup type must be set to automatic. |
| VRU_PG_INSTALLED | The VRU PG service must be installed. |
| VRU_PG_AUTOMATIC | The VRU PG service startup type must be set to automatic. |

| Rule | Description |
|---|---|
| When you configure Agent PG |
| CTI_SVR_INSTALLED | The CTI Server service must be installed. |
| CTI_SVR_AUTOMATIC | The CTI server service startup type must be set to automatic. |
| DIALER_INSTALLED | If installed, the dialer service must be installed on both sides. |
| DIALER_AUTOMATIC | If installed, the dialer service startup type must be set to automatic. |
| UCM_PG_INSTALLED | The UCM PG service must be installed. |
| UCM_PG_AUTOMATIC | The UCM PG service startup type must be set to automatic. |
| UCM_PG_JTAPI_MATCHES_CM_SUB | The Communications Manager PIM service address configured in PG Setup must match the Communications Manager Subscriber address
                                          on the same side. |
| When you configure MR PG |
| MR_PG_INSTALLED | The Media Routing PG service must be installed. |
| MR_PG_AUTOMATIC | The Media Routing PG service must be set to automatic. |
| When you configure VRU PG |
| VRU_PG_INSTALLED | The VRU PG service must be installed. |
| VRU_PG_AUTOMATIC | The VRU PG service startup type must be set to automatic. |
| When you configure any type of PG |
| NO_EXTRA_SERVICES_INSTALLED_PG | Only required and optional services can be installed (extra services such as an additional PG or CTI Server are not permitted). |

| Rule | Description |
|---|---|
| SSO_COMPONENT_STATUS_MATCHES_GLOBAL | The global SSO status must be the same as component SSO status. |
| SSO_VALID_IDS_REFERENCE | If single sign-on is enabled, this machine must be associated with a valid Cisco Identity Service. |
| DISTRIBUTOR_CONAPI_MUST_BE_DISABLED | Configuration Management Service (CMS) Node and Agent Re-skilling Web Tool must be disabled using Unified CCE Web Setup. |
| DISTRIBUTOR_INSTALLED | The distributor service must be installed. |
| DISTRIBUTOR_AUTOMATIC | The distributor service startup type must be set to automatic. |
| NO_EXTRA_SERVICES_INSTALLED_AW | Only required services can be installed. |
| TASK_ROUTING_APP_PATHS_EXIST | Each Peripheral Gateway with a Communications Manager PIM must have an associated Task Routing Application Path. |

| Rule | Description |
|---|---|
| SSO_COMPONENT_STATUS_MATCHES_GLOBAL | The global SSO status must be the same as component SSO status. |
| SSO_VALID_IDS_REFERENCE | If single sign-on is enabled, this machine must be associated with a valid Cisco Identity Service. |
| DISTRIBUTOR_CONAPI_MUST_BE_DISABLED | Configuration Management Service (CMS) Node and Agent Re-skilling Web Tool must be disabled using Unified CCE Web Setup. |
| TASK_ROUTING_APP_PATHS_EXIST | Each Peripheral Gateway with a Communications Manager PIM must have an associated Task Routing Application Path. |

| Rule | Description |
|---|---|
| GW_CODEC | The dial peers for each CVP call server on each gateway are configured with the supported codec: voice-class codec #num dial-peer voice #num voip (codec ).The supported voice
                                                											codecs are g711alaw, g711ulaw, g729r8, mp4a-latm and
                                                											g722-64 for the above four dial peers to CVP call
                                                											servers (if the dial peers are configured on
                                                											the voice gateway). The supported video codec is h264.
                                                											The dial peer is identified via "session target
                                                											ipaddress xxxxx". The IP address must point to the IP
                                                											address of CVP call server. |
| GW_SIP_PROTOCOL | The dial peers for each CVP call server on each gateway must be configured with the supported session protocol, sipv2. |

| Rule | Description |
|---|---|
| SSO_COMPONENT_STATUS_MATCHES_GLOBAL | The global SSO status must be the same as component SSO status. |
| SSO_VALID_IDS_REFERENCE | If single sign-on is enabled, this machine must be associated with a valid Cisco Identity Service. |
| CAN_RESOLVE_ADDRESS_TO_FQDN | The machine address must be resolvable to an FQDN. |

| Rule | Description |
|---|---|
| CUIC_REALTIME_DS_CORRECT_HOST | The realtime datasource must be configured with the correct hosts: either the Side A and B Unified CCE AW-HDS-DDS Servers,
                                          or, if used, the External HDS. |
| CUIC_HISTORICAL_DS_CORRECT_HOST | The historical datasource must be configured with the correct hosts: either the Side A and B Unified CCE AW-HDS-DDS Servers,
                                          or, if used, the External HDS. |

| Rule | Description |
|---|---|
| SSO_COMPONENT_STATUS_MATCHES_GLOBAL | The global SSO status must be the same as the component SSO status. |
| SSO_VALID_IDS_REFERENCE | If single sign-on is enabled, this machine must be associated with a valid Cisco Identity Service. |
| CAN_RESOLVE_ADDRESS_TO_FQDN | The machine address must be resolvable to an FQDN. |

| Rule | Description |
|---|---|
| TRACE_LEVEL_NORMAL | The trace level must be set to normal to ensure performance. |
| CAN_RESOLVE_ADDRESS_TO_FQDN | The machine address must be resolvable to an FQDN. |

| Rule | Description |
|---|---|
| CVP_CUCM_SIP_SERVER_GROUPS_MATCH _CUCM_FQDN | The CVP SIP Server Group names that contain Communication Manager addresses must match the Communication Manager Cluster Fully
                                          Qualified Domain Name. |
| CVP_CUCM_SIP_SERVER_GROUPS_ONLY _CONTAIN_CUCM_HOSTS | The CVP SIP Server Groups that contain Communication Manager addresses cannot contain non-Communication Manager addresses
                                          (which include Communication Manager hosts that are not part of the inventory). |
| CVP_RING_TONE_DN_PATTERN | The Ring Tone Dialed Number configured on the CVP Call Server should match the pattern 91*. |
| CVP_ERROR_LABEL_DN_PATTERN | The Error Tone Dialed Number configured on the CVP Call Server should match the pattern 92*. |

| Rule | Description |
|---|---|
| TRACE_LEVEL_NORMAL | The trace level must be set to normal to ensure performance. |
| CAN_RESOLVE_ADDRESS_TO_FQDN | The machine address must be resolvable to an FQDN. |

| Rule | Description |
|---|---|
| CUCM_FQDN_DEFINED | The Communication Manager Cluster Fully Qualified Domain Name must be defined. |
| CVP_SERVER_MUST_HAVE_A_CM_SIP_TRUNK | Each CVP Server must be referenced by at least one Communications Manager SIP Trunk destination. |

| Rule | Description |
|---|---|
| VMHOST_ESXI_VERSION_MATCH | Side A and Side B VM Hosts must be on the same ESXi version. |
| VM_DATASTORE | Virtual machines must be deployed on the correct datastore. |

| Rule | Description |
|---|---|
| SOCIAL_MINER_MR_ENABLED | Multichannel routing must be enabled on SocialMiner . |
| CAN_RESOLVE_ADDRESS_TO_FQDN | The machine address must be resolvable to an FQDN. |

| Rule | Description |
|---|---|
| CLOUD_CONNECT_REGISTRATION_STATUS | Shows the Registration Status of Cloud Service. |
| CLOUD_CONNECT_ WXM_SURVEY_MISSING | Shows the Call Type survey status which does not exist in Webex Experience. |
| CLOUD_CONNECT_ WXM_SURVEY_WRONG_MULTICHANNEL | Shows the status of the Call Types with deferred surveys which are configured in Media Routing Dialled Numbers. |
| CLOUD_CONNECT_ WXM_SURVEY_WRONG_CHANNEL | Shows the survey status of Webex Experience with unsupported channels. |

| Rule | Description |
|---|---|
| LOGGER_CAMPAIGN_MGR_RUNNING | The logger campaign manager process (campaignmanager.exe) must be running. |
| LOGGER_CONFIG_LOGGER_RUNNING | The logger configuration logger process (configlogger.exe) must be running. |
| LOGGER_CSFS_RUNNING | The logger customer support forwarding service process (csfs.exe) must be running. |
| LOGGER_HIST_LOGGER_RUNNING | The logger historical logger process (histlogger.exe) must be running. |
| LOGGER_BA_IMPORT_RUNNING | The logger import process (baimport.exe) must be running. |
| LOGGER_RECOVERY_RUNNING | The logger recovery process (recovery.exe) must be running. |
| LOGGER_REPLICATION_RUNNING | The logger replication process (replication.exe) must be running. |
| LOGGER_RUNNING | The logger service must be running. |
| SERVER_CREDENTIALS | The Diagnostic Framework credentials entered for the Principal AW must be valid. |
| SERVER_CONNECTION | The Cisco ICM Diagnostic Framework service on this machine must be reachable on the network. |
| ROUTER_CCAGENT_INSVC_ACTIVE_ENABLE_COUNT | The router central controller agent process (ccagent.exe) must be in service for both PGs. |
| ROUTER_CCAGENT_RUNNING | The router central controller agent process (ccagent.exe) must be running. |
| ROUTER_DBAGENT_RUNNING | The router database agent process (dbagent.exe) must be running. |
| ROUTER_LIVE_DATA_ACTIVE_IDLE | The router Live Data connection must be active on one side and idle on the other side. |
| ROUTER_MDSPROC_IN_SVC_PR_ENB_DSB | The router message delivery service process (mdsproc.exe) must be enabled on one side and disabled on the other side. |
| ROUTER_MDSPROC_RUNNING | The router message delivery service process (mdsproc.exe) must be running. |
| ROUTER_ROUTER_RUNNING | The router process (router.exe) must be running. |
| ROUTER_RUNNING | The router service must be running. |

| Rule | Description |
|---|---|
| CTI_SVR_CTI_SVR_ACTIVE_ STANDBY | The CTI server process (ctisvr.exe) must be active on one side and standby/idle on the other side. Note For PGs on version 12.6(1) or later, the expected state of the CTI Server on the other side is Standby . On earlier PG versions, the expected state is Idle . | Note | For PGs on version 12.6(1) or later, the expected state of the CTI Server on the other side is Standby . On earlier PG versions, the expected state is Idle . |
| Note | For PGs on version 12.6(1) or later, the expected state of the CTI Server on the other side is Standby . On earlier PG versions, the expected state is Idle . |
| CTI_SVR_CTI_SVR_RUNNING | The CTI server process (ctisvr.exe) must be running. |
| CTI_SVR_RUNNING | The CTI Server service must be running. |
| DIALER_RUNNING | If dialer is installed, then the dialer service must be running. |
| DIALER_BA_DIALER_SIP_ACTIVE_IDLE | The dialer process (badialer_sip.exe) must be active on one side and idle on the other side. |
| DIALER_BA_DIALER_SIP_RUNNING | The dialer process (badialer_sip.exe) must be running. |
| MR_PG_MR_PIM_ACTIVE_IDLE | Each MR_PIM process (mr_pim.exe) must be active on one side and idle on the other side. |
| MR_PG_MDSPROC_IN_SVC_PR_ENB_DSB | The media routing PG message delivery service process (mdsproc.exe) must be enabled on one side and disabled on the other
                                          side. |
| MR_PG_MDSPROC_RUNNING | The media routing PG message delivery service process (mdsproc.exe) must be running. |
| MR_PG_PG_AGENT_ACTIVE_IDLE | The media routing PG PG agent process (pgagent.exe) must be active on one side and idle on the other side. |
| MR_PG_PG_AGENT_RUNNING | The media routing PG PG agent process (pgagent.exe) must be running. |
| MR_PG_RUNNING | The media routing PG service must be running. |
| SERVER_CREDENTIALS | The Diagnostic Framework credentials entered for the Principal AW must be valid. |
| SERVER_CONNECTION | The Cisco ICM Diagnostic Framework service on this machine must be reachable on the network. |
| UCM_PG_JTAPI_ACTIVE_IDLE | The UCM PG jtapi process (jtapigw.exe) must be active on one side and idle on the other side. |
| UCM_PG_JTAPI_RUNNING | The UCM PG jtapi process (jtapigw.exe) must be running. |
| UCM_PG_LIVE_DATA_ACTIVE_IDLE | The UCM PG Live Data connection must be active on one side and idle on the other side. |
| UCM_PG_MDSPROC_IN_SVC_PR_ENB_DSB | The UCM PG message delivery service process (mdsproc.exe) must be enabled on one side and disabled on the other side. |
| UCM_PG_MDSPROC_RUNNING | The UCM PG message delivery service process (mdsproc.exe) must be running. |
| UCM_PG_PIM_COUNT | The number of UCM PG's PIM processes (eagtpim.exe) on Side A and Side B must match. Valid if 1 PIM is enabled. |
| UCM_PG_PG_AGENT_ACTIVE_IDLE | The UCM PG PG agent process (pgagent.exe) must be active on one side and idle on the other side. |
| UCM_PG_PG_AGENT_RUNNING | The UCM PG PG agent process (pgagent.exe) must be running. |
| UCM_PG_RUNNING | The UCM PG service must be running. |
| VRU_PG_VRU_PIM_ACTIVE_IDLE | Each VRU PIM process (vrupim.exe) must be active on one side and idle on the other side. |
| VRU_PG_MDSPROC_IN_SVC_PR_ENB_DSB | The VRU PG message delivery service process (mdsproc.exe) must be enabled on one side and disabled on the other side. |
| VRU_PG_MDSPROC_IN_SVC_PR_ENB_DSB | The VRU PG message delivery service process (mdsproc.exe) must be enabled on one side and disabled on the other side. |
| VRU_PG_MDSPROC_RUNNING | The VRU PG message delivery service process (mdsproc.exe) must be running. |
| VRU_PG_PIM_COUNT | The number of VRU PG's PIM processes (vrupim.exe) on Side A and Side B must match. Valid if 0 to 2 VRU PIMs are enabled. |
| VRU_PG_PG_AGENT_ACTIVE_IDLE | The VRU PG PG agent process (pgagent.exe) must be active on one side and idle on the other side. |
| VRU_PG_PG_AGENT_RUNNING | The VRU PG PG agent process (pgagent.exe) must be running. |
| VRU_PG_RUNNING | The VRU PG service must be running. |

| Note | For PGs on version 12.6(1) or later, the expected state of the CTI Server on the other side is Standby . On earlier PG versions, the expected state is Idle . |
|---|---|

| Rule | Description |
|---|---|
| When you configure Agent PG |
| CTI_SVR_RUNNING | The CTI Server service must be running. |
| CTI_SVR_CTI_SVR_RUNNING | The CTI server process (ctisvr.exe) must be running. |
| CTI_SVR_CTI_SVR_ACTIVE_ STANDBY | The CTI server process (ctisvr.exe) must be active on one side and standby on the other side. |
| DIALER_RUNNING | If dialer is installed, then the dialer service must be running. |
| DIALER_BA_DIALER_SIP_RUNNING | If dialer is installed, the dialer process (badialer_sip.exe) must be running. |
| DIALER_BA_DIALER_SIP_ACTIVE_IDLE | If dialer is installed, the dialer process (badialer_sip.exe) must be active on one side and idle on the other side. |
| UCM_PG_RUNNING | The UCM PG service must be running. |
| UCM_PG_LIVE_DATA_ACTIVE_IDLE | The UCM PG Live Data connection must be active on one side and idle on the other side. |
| UCM_PG_JTAPI_RUNNING | The UCM PG jtapi process (jtapigw.exe) must be running. |
| UCM_PG_JTAPI_ACTIVE_IDLE | The UCM PG jtapi process (jtapigw.exe) must be active on one side and idle on the other side. |
| UCM_PG_MDSPROC_RUNNING | The UCM PG message delivery service process (mdsproc.exe) must be running. |
| UCM_PG_MDSPROC_IN_SVC_PR_ENB_DSB | The UCM PG message delivery service process (mdsproc.exe) must be enabled on one side and disabled on the other side. |
| UCM_PG_PG_AGENT_RUNNING | The UCM PG PG agent process (pgagent.exe) must be running. |
| UCM_PG_PG_AGENT_ACTIVE_IDLE | The UCM PG PG agent process (pgagent.exe) must be active on one side and idle on the other side. |
| UCM_PG_PIM_COUNT | The number of UCM PG's PIM processes (eagtpim.exe) on Side A and Side B must match. Valid if 1 PIM is enabled. |
| When you configure MR PG |
| MR_PG_RUNNING | The media routing PG service must be running. |
| When you configure VRU PG |
| VRU_PG_RUNNING | The VRU PG service must be running. |
| VRU_PG_PG_AGENT_RUNNING | The VRU PG PG agent process (pgagent.exe) must be running. |
| VRU_PG_PG_AGENT_ACTIVE_IDLE | The VRU PG PG agent process (pgagent.exe) must be active on one side and idle on the other side. |
| VRU_PG_MDSPROC_RUNNING | The VRU PG message delivery service process (mdsproc.exe) must be running. |
| VRU_PG_MDSPROC_IN_SVC_PR_ENB_DSB | The VRU PG message delivery service process (mdsproc.exe) must be enabled on one side and disabled on the other side. |
| VRU_PG_PIM_COUNT | The number of VRU PG's PIM processes (vrupim.exe) on Side A and Side B must match. Valid if 0 to 2 VRU PIMs are enabled. |
| VRU_PG_VRU_PIM_ACTIVE_IDLE | Each VRU PIM process (vrupim.exe) must be active on one side and idle on the other side. |
| When you configure any type of PG |
| SERVER_CREDENTIALS | The Diagnostic Framework credentials entered for the Principal AW must be valid. |
| SERVER_CONNECTION | The Cisco ICM Diagnostic Framework service on this machine must be reachable on the network. |

| Rule | Description |
|---|---|
| DISTRIBUTOR_CONFIG_LOGGER_RUNNING | The distributor configuration logger process (configlogger.exe) must be running. |
| DISTRIBUTOR_RT_CLIENT_RUNNING | The distributor real-time client process (rtclient.exe) must be running. |
| DISTRIBUTOR_RT_DIST_RUNNING | The distributor real-time distributor process (rtdist.exe) must be running. |
| DISTRIBUTOR_RUNNING Note This rule is not applicable for the external HDS | Note | This rule is not applicable for the external HDS | The distributor service must be running. |
| Note | This rule is not applicable for the external HDS |
| DISTRIBUTOR_UPDATE_AW_RUNNING | The distributor update process (updateaw.exe) must be running. |
| DEPLOYMENT_TASKS_PASSING | The deployment tasks must all be passing. |
| SERVER_CREDENTIALS | The Diagnostic Framework credentials entered for the Principal AW must be valid. |
| SERVER_CONNECTION | The Cisco ICM Diagnostic Framework service on this machine must be reachable on the network. |

| Note | This rule is not applicable for the external HDS |
|---|---|

| Rule | Description |
|---|---|
| SERVER_CREDENTIALS | The AXL service credentials entered for the Publisher must be valid. |
| SERVER_CONNECTION | The AXL service on the Publisher must be reachable on the network. |

| Rule | Description |
|---|---|
| SERVER_CREDENTIALS | The Cisco CVP WebServicesManager credentials entered for the CVP Server must be valid. |
| SERVER_CONNECTION | The Cisco CVP WebServicesManager service on CVP Server must be reachable on the network. |

| Rule | Description |
|---|---|
| SERVER_CREDENTIALS | The service credentials entered for the gateway in Unified CVP Ops Console must be valid. |
| SERVER_CONNECTION | The service must be reachable on the network. |

| Rule | Description |
|---|---|
| SERVER_CREDENTIALS | The Unified Intelligence Center Administration credentials entered for the Publisher must be valid. |
| SERVER_CONNECTION | The SOAP service on the Publisher must be reachable on the network. |

| Rule | Description |
|---|---|
| FINESSE_SYSTEM_STATUS | Finesse must be in service. |
| SERVER_CREDENTIALS | The Finesse Administration credentials entered for the Primary Finesse machine must be valid. |
| SERVER_CONNECTION | The SOAP service on the Primary Finesse machine must be reachable on the network. |
| FINESSE_TOMCAT_SERVICE_STARTED | The Tomcat service must be started. |

| Rule | Description |
|---|---|
| SERVER_CREDENTIALS | The service credentials must be valid. |
| SERVER_CONNECTION | The service must be reachable on the network. |

| Rule | Description |
|---|---|
| CLOUD_CONNECTOR_TYPE | Cloud connect is either publisher or subscriber. |
| CONTACT_CENTER_AI_CALL_TYPE_CONFIG_NOT_FOUND | Some of the Contact Center AI configurations that are associated with the call types are not available in the Control Hub. Note This rule is applicable only for Packaged CCE 2000 Agents deployment. | Note | This rule is applicable only for Packaged CCE 2000 Agents deployment. |
| Note | This rule is applicable only for Packaged CCE 2000 Agents deployment. |

| Note | This rule is applicable only for Packaged CCE 2000 Agents deployment. |
|---|---|

| Rule | Description | Machine Type |
|---|---|---|
| CPU_USAGE | CPU usage must be below 80%. | All |
| MEMORY_USAGE | Memory usage must be below 80%. | All |
| DISK_USAGE | Disk usage must be below 90%. If any disk value is over the
                                       					 threshold, then the highest error level is reported. | All |
| Principal_AW_Status | To identify if the Principal AW machine is up or down. This rule is applicable only for Packaged CCE 4000 Agents and 12000 Agents Deployments | CCE_AW |
| Principal_VVB_Status | To identify if the Principal VVB machine is up or down. This rule is applicable only for Packaged CCE 4000 and 12000 Agent Deployments. | EXTERNAL_CVVB DC_EXTERNAL_CVVB |

| Rule | Description |
|---|---|
| DATASTORE_DISK_COMMANDS_ABORTED_SUMMATION | Number of commands stopped or canceled per datastore. |
| DATASTORE_DISK_BUS_RESETS_SUMMATION | Number of bus resets per datastore. |
| DATASTORE_DISK_TOTAL_LATENCY_AVERAGE | Total latency in milliseconds per datastore. |

| Rule | Description | Machine Type |
|---|---|---|
| VMWARE_TOOLS | VMware tools must be
                                    				  up-to-date. | VM Host |
| VMWARE_GUEST_OS | The operating system
                                    				  setting on each Virtual Machine (VM) must match the operating system installed
                                    				  on the Guest. | All |