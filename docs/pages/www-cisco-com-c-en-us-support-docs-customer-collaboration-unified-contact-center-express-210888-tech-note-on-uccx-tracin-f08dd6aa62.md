---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-express-210888-tech-note-on-uccx-tracin-f08dd6aa62
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-express/210888-Tech-Note-on-UCCX-Tracing-Levels.html
retrieved_at: 2026-08-16T15:07:06.487570+00:00
---

Understand UCCX Tracing Levels

# Understand UCCX Tracing Levels

### Download Options

Updated: November 21, 2023

Document ID: 210888

Contents

## Contents

## Introduction

This document provides the list of relevant logs and also the tracing levels for some of the common issues seen in the field. The aim of the document is to ensure that the reader is in the position to collect the right set of logs when the issue is occuring so that the resolution time is reduced and the chance of a root cause is increased.

## Administration

Installation and Upgrade

- Fresh Install

system-history.log

uccx-install.log

hostname_date-time_install.log

Installation and Upgrade

- Switch version failure

- Upgrade failures

system-history.log

uccx-install.log

hostname_date-time_install.log

CLI Location: file list install *

Install and Upgrade

Cisco Unified CCX Database

DRF Backup and Restore

- Backup failure

- Restore failure

- Check status or validity of a backup

After each Backup or Restore ,the logs are displayed on DRFGUI for immediate reference

CLI Location : file list activelog platform/drf/log/*

UCCX Licensing

- License installation failure

- License package verification

MIVR

CLI Location : file list activelog uccx/log/MIVR/*

Cisco Unified CCX Engine

MADM

CLI Location : file list activelog uccx/log/MADM/*

MCVD (if 2 node cluster)

CLI Location : file list activelog uccx/log/MCVD/*

Cisco Unified CCX Cluster View Daemon

High Availability

- UCCX Failover

- Island mode

MCVD

Cisco Unified CCX Cluster View Daemon

MIVR

Cisco Unified CCX Engine

MADM

ADM_CFG: XDebug2

LIB_AXL: XDebug2

MADM

ADM_CFD: XDebug2

LIB_CFG:XDebug2

Issues with configuration of agents, CSQs or teams

- Team asignment failure

- Reskilling failure

- Updated configuration not being used by the system

MIVR

SS_RM: XDebug1

LIB_CFG: XDebug1

ICD_RTDM: XDebug1

Cisco Unified CCX Engine

MADM

MADM

ADM_CFD: XDebug2

LIB_DATABASE: XDebug2

FILE_MGR: XDebug2

MCLI

CLI Location : file list activelog uccx/log/MCLI/*

(OR)

CLI Location : file list activelog platform/cli/*

Default log level

## Inbound voice calls

Core ICD

- Call drops

- Call routing to wrong destination

- Call completion failure

ICD_CTI - Xdebug1

SS_CM: XDebug1

SS_RM: XDebug1

Cisco Unified CCX Engine

CTI Manager

Call Manager

(connect RTMT to CUCM cluster)

SS_CM: XDebug1

SS_RM: XDebug1

SS_TEL: XDebug1

ICD_RTDM: XDebug1

Finesse client side logs

Finesse Webservices

Realm logs

Instruct agent to click on Send Error Report

SS_CM: XDebug1

SS_RM: Xdebug1-4

SS_TEL: XDebug1

ICD_CTI: XDebug1

SS_CM: XDebug1

SS_RM: XDebug1

SS_TEL: XDebug1

ICD_CTI: XDebug1

Check/Enable WARNING, INFORMATIONAL, DEBUG, JTAPI_DEBUGGING, JTAPIIMPL_DEBUGGING, CTI_DEBUGGING, CTIIMPL_DEBUGGING

Call failures

Abandoned calls

Note:This is the case when the reason for abandoned calls is to be investigated, not just to check why you see abandoned calls on the CUIC report.

SS_CM: XDebug1

SS_RM: XDebug1

SS_TEL: XDebug1

Check/Enable WARNING, INFORMATIONAL, DEBUG, JTAPI_DEBUGGING, JTAPIIMPL_DEBUGGING, CTI_DEBUGGING, CTIIMPL_DEBUGGING

SS_CM: XDebug3

SS_TEL: XDebug3

ENG: XDebug5

STEP_ICD: XDebug4

SS_CM: XDebug3

SS_TEL: XDebug3

ENG: XDebug5

STEP_ICD: XDebug4

SS_VB: XDebug5

UCCX Engine

Packet capture on the UCCX server, capturing traffic between UCCX and the VXML server

LIB_MEDIA: Debug, Xdebug1

UCCX Engine

On the CLI, run the command 'show media streams count 5 sleep 5 trace' when the issue is occuring

These can be viewed using:"file view activelog /platform/log/mediainfo.txt"

N/A

Syslog

## Outbound voice calls

Outbound campaign dialling issues:

- Calls not dialed out as expected

- Agents not receiving calls as expected

SS_OB: Debug, XDebug2

SS_RM: Debug, XDebug1

UCCX Engine

Dialing list upload/modification failure

UCCX Engine

Agent seeing incorrect information

UCCX Engine

Finesse/CAD specific agent side logs

## UCCX Scripting

UCCX Script Editor behavioral issues (not when working in Anonymous mode)

that involves interaction with the UCCX server

UCCX Unified CCX Editor

EDT: Debugging

Generic: Debugging

If issue is specific to a step, set the debug level for that step to Debugging

UCCX Engine

UCCX Engine

ENG: Debugging, XDebug1

EXPR_MGR: Debugging, XDebug1

If issue is specific to a step, set the debug level for that step to Debugging

Issues with script execution:

- Get information on the logic of script execution

- Script execution failures

SS_CM: XDebug1

SS_RM: XDebug1

SS_TEL: Debugging

ENG: XDebug1

UCCX Engine

## Agent Desktop

### Finesse

Agent login failure

Agent state change issues

SS_CM: Debugging, XDebug1

SS_RM: Upto XDebug4

Eng: Debugging

SS_TEL: Debugging, XDebug1

SS_RMCM: Debugging, XDebug1

ICD_CTI: Debugging, XDebug1

UCCX Engine

LIB_AXL: Debugging

REST_CLIENT: Debugging

LIB_CFG: Debugging

ADM_CFG: Debugging

For 11.0:

SS_RM: Upto XDebug5

For 11.5:

SS_ROUTENQUEUE: Upto XDebug5

UCCX Engine

For all agent side issues such as Finesse client losing connectivity, collect Finesse client logs and also use local logging as shown in here:

### Cisco Agent Desktop (CAD/CSD)

CAD client side issues:

- Installation and upgrade failure

- Agent state change issues

- Unable to see right information on the agent desktop

- Other errors on the screen

Open C:\Program Files\Cisco\Desktop\config\ Agent.cfg

Set the following:

[Program Log]

Size=10MB

Files=10

Threshold= TRACE

CSD client side issues:

- Installation and upgrade failure

- Unable to see right information on the  desktop

- Other errors on the screen

Open C:\Program Files\Cisco\Desktop\config\Supervisor.cfg

Set the following:

[Program Log]

Size=10MB

Files=10

Threshold= TRACE

Cisco Desktop Administrator (thick client)

Open C:\Program Files\Cisco\Desktop\config

Administrator.cfg and SplkView.cfg

Files=10

Size=10000000

More information about the logs and the information that needs to be collected can be found under the Configuration Files and Logs section: http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_8_5/troubleshooting/guide/cad85ccxtg-cm.pdf

## Reporting and Database

Database related issues:

- Replication failure

- UCCX Database corruption

- UCCX Database start-up message

Historical Reports missing data

- Calls not being written into the database

- Data missing for a few days

CRA_HRDM: Debuging, XDebug1

ICD_CTI: Debugging, XDebug1

SS_RM: Debuging, XDebug1

SS_CM: Debuging, XDebug1

SS_TEL: Debuging, XDebug1

SS_RMCM: Debuging, XDebug1

UCCX Engine

CRA_HRDM: Debuging, XDebug1

ICD_CTI: Debugging, XDebug1

SS_RM: Debuging, XDebug1

SS_CM: Debuging, XDebug1

SS_TEL: Debuging, XDebug1

SS_RMCM: Debuging, XDebug1

UCCX Engine

## Chat/Email

## SocialMiner Logs

#

Module

File Pattern

Path/URL

1

SocialMiner Runtime

- Getting social contacts from facebook/twitter/RSS etc

- Running Filters

- Triggering notification rules (HTTP/XMPP/Email/CCE)

- Interaction with MR PG (CCE)

CCBU-runtime.*.startup.log Error-runtime.*.startup.log

https://<SocialMiner Server IP/Host>/ccp-webapp/logs/runtime/

2

SocialMiner API

- Rest APIs

- Reply Templates

- XMPP Event publishing

CCBU-ccpapi.*.startup.log Error-ccpapi.*.startup.log

https://<SocialMiner Server IP/Host>/ccp-webapp/logs/ccpapi/

3

SocialMiner Public Apps

- Public facing proxy to reach SocialMiner

- Exposes restricted set of Rest APIs

- Typically used by Chat and Callback

CCBU-ccppublicapps.*.startup.log Error-ccppublicapps.*.startup.log

https://<SocialMiner Server IP/Host>/ccp-webapp/logs/ccppublicapps/

4

SocialMiner Datastore (Cassandra)

- Contact Storage

ccp-ds-storage.startup.log

https://<SocialMiner Server IP/Host>/ccp-webapp/logs/ccp-ds-storage/

5

SocialMiner Indexer (Solr)

- Contact search and query performance

ccp-ds-indexer.request.*.log

https://<SocialMiner Server IP/Host>/ccp-webapp/logs/ccp-ds-indexer/

6

SocialMiner XMPP Server

- XMPP eventing

- Chatrooms for chat contacts

*.log

https://<SocialMiner Server IP/Host>/ccp-webapp/logs/ccp-xmpp-server/

7

SocialMiner ORM

- Interact with Informix DB

- Manage configurations like feeds, filters, notifications, campaigns, etc

- Historical reporting record for CUIC

CCBU-orm.*.startup.log Error-orm.*.startup.log

https://<SocialMiner Server IP/Host>/ccp-webapp/logs/orm/

8

Cisco Tomcat

- General Tomcat logging

*.log

https://<SocialMiner Server IP/Host>/ccp-webapp/logs/tomcat/

Cisco Tomcat (System Services)

9

Cisco Tomcat (Token Authentication)

- Token Authentication related details - used by the chat reply template

localhost.*.log

https://<SocialMiner Server IP/Host>/ccp-webapp/logs/tomcat/

Cisco Tomcat (System Services)

10

SocialMiner System Health Snapshot

Can be accessed via SocialMiner's Administration tab > System Administration > System Logs > System Health Snapshot

Direct URL : http://<socialminer_hostname>/ccp-webapp/ccp/serviceability/SocialMinerSystemHealth.xml?category=all

### Revision History

2.0

21-Nov-2023

Initial Release

1.0

15-May-2017

Initial Release

| Component/Issue | Log files | Log levels | Component to select in RTMT |
|---|---|---|---|
| Installation and Upgrade Fresh Install | system-history.log uccx-install.log hostname_date-time_install.log | Default log level | Install and Upgrade |
| Installation and Upgrade Switch version failure Upgrade failures | system-history.log uccx-install.log hostname_date-time_install.log CLI Location: file list install * | Default log level | Install and Upgrade Cisco Unified CCX Database |
| DRF Backup and Restore Backup failure Restore failure Check status or validity of a backup | After each Backup or Restore ,the logs are displayed on DRFGUI for immediate reference CLI Location : file list activelog platform/drf/log/* | Default log level | Cisco UCCX DRF and Cisco DRF Master and Cisco DRF local |
| UCCX Licensing License installation failure License package verification | MIVR CLI Location : file list activelog uccx/log/MIVR/* | LIB_LICENSE enabled upto XDebug3 | Cisco Unified CCX Engine |
| MADM CLI Location : file list activelog uccx/log/MADM/* | Cisco Unified CCX Administration |
| MCVD (if 2 node cluster) CLI Location : file list activelog uccx/log/MCVD/* | Cisco Unified CCX Cluster View Daemon |
| High Availability UCCX Failover Island mode | MCVD | Default log level | Cisco Unified CCX Cluster View Daemon |
| MIVR | Cisco Unified CCX Engine |
| Application Administration login issues | MADM | ADM_CFG: XDebug2 LIB_AXL: XDebug2 | Cisco Unified CCX Administration |
| Application Administration Configuration issues | MADM | ADM_CFD: XDebug2 LIB_CFG:XDebug2 | Cisco Unified CCX Administration |
| Issues with configuration of agents, CSQs or teams Team asignment failure Reskilling failure Updated configuration not being used by the system | MIVR | SS_RM: XDebug1 LIB_CFG: XDebug1 ICD_RTDM: XDebug1 | Cisco Unified CCX Engine |
| MADM |  | Cisco Unified CCX Administration |
| File manager related issues: upload of prompts, documents etc. from the application administration page | MADM | ADM_CFD: XDebug2 LIB_DATABASE: XDebug2 FILE_MGR: XDebug2 | Cisco Unified CCX Administration |
| Command Line Interface related issues | MCLI CLI Location : file list activelog uccx/log/MCLI/* (OR) CLI Location : file list activelog platform/cli/* | Default log level | Cisco Unified CCX CLI / Cisco ControlCenter CLI / IPT Platform CLI |

| Component/Issue | Log files | Log levels | Component to select in RTMT |
|---|---|---|---|
| Core ICD Call drops Call routing to wrong destination Call completion failure | MIVR | ICD_CTI - Xdebug1 SS_CM: XDebug1 SS_RM: XDebug1 | Cisco Unified CCX Engine |
| JTAPI | Check/Enable WARNING, INFORMATIONAL, DEBUG, JTAPI_DEBUGGING, JTAPIIMPL_DEBUGGING, CTI_DEBUGGING, CTIIMPL_DEBUGGING | Cisco Unified CCX JTAPI Client |
| CTI(SDI & SDL) and CCM (SDI & SDL) logs from the correct Call Manager node that has the logs for the specific call that has issue | Detailed | CTI Manager Call Manager (connect RTMT to CUCM cluster) |
| RmCm subsystem stuck in a state apart from IN_SERVICE | MIVR | SS_RMCM: XDebug4 | UCCX Engine |
| Call stuck in queue | MIVR | SS_CM: XDebug1 SS_RM: XDebug1 SS_TEL: XDebug1 ICD_RTDM: XDebug1 | UCCX Engine |
| Agent stuck in any state | Finesse client side logs Finesse Webservices Realm logs | Instruct agent to click on Send Error Report | Cisco Finesse |
| MIVR | SS_CM: XDebug1 SS_RM: Xdebug1-4 SS_TEL: XDebug1 ICD_CTI: XDebug1 | UCCX Engine |
| Transfer and Conference failure of an ICD call | MIVR | SS_CM: XDebug1 SS_RM: XDebug1 SS_TEL: XDebug1 ICD_CTI: XDebug1 | UCCX Engine |
| JTAPI | Check/Enable WARNING, INFORMATIONAL, DEBUG, JTAPI_DEBUGGING, JTAPIIMPL_DEBUGGING, CTI_DEBUGGING, CTIIMPL_DEBUGGING | Cisco Unified JTAPI Client |
| Call failures Abandoned calls Note:This is the case when the reason for abandoned calls is to be investigated, not just to check why you see abandoned calls on the CUIC report. | MIVR | SS_CM: XDebug1 SS_RM: XDebug1 SS_TEL: XDebug1 | UCCX Engine |
| JTAPI | Check/Enable WARNING, INFORMATIONAL, DEBUG, JTAPI_DEBUGGING, JTAPIIMPL_DEBUGGING, CTI_DEBUGGING, CTIIMPL_DEBUGGING | Cisco Unified JTAPI Client |
| Call failure during script execution | MIVR | SS_CM: XDebug3 SS_TEL: XDebug3 ENG: XDebug5 STEP_ICD: XDebug4 | UCCX Engine |
| Call errors involving VXML document interaction | MIVR | SS_CM: XDebug3 SS_TEL: XDebug3 ENG: XDebug5 STEP_ICD: XDebug4 SS_VB: XDebug5 | UCCX Engine Packet capture on the UCCX server, capturing traffic between UCCX and the VXML server |
| Media related issues with call. Example: choppy audio, prompt garbled | MIVR | LIB_MEDIA: Debug, Xdebug1 | UCCX Engine |
| IPVMS | On the CLI, run the command 'show media streams count 5 sleep 5 trace' when the issue is occuring | These can be viewed using:"file view activelog /platform/log/mediainfo.txt" |
| Syslog messages | N/A | Syslog |
| Call issues related to ASR/TTS |  |  |  |

| Component/Issue | Log files | Log levels | Component to select in RTMT |
|---|---|---|---|
| Outbound campaign dialling issues: Calls not dialed out as expected Agents not receiving calls as expected | MIVR | SS_OB: Debug, XDebug2 SS_RM: Debug, XDebug1 | UCCX Engine |
| Dialing list upload/modification failure | MIVR | CFG_MGR: XDebug1 | UCCX Engine |
| Agent seeing incorrect information | MIVR | ICD_CTI: Xdebug1 | UCCX Engine Finesse/CAD specific agent side logs |

| Component/Issue | Log files | Log levels | Component to select in RTMT |
|---|---|---|---|
| UCCX Script Editor behavioral issues (not when working in Anonymous mode) that involves interaction with the UCCX server | MIVR | UCCX Unified CCX Editor EDT: Debugging Generic: Debugging If issue is specific to a step, set the debug level for that step to Debugging | UCCX Engine |
| UCCX Engine ENG: Debugging, XDebug1 EXPR_MGR: Debugging, XDebug1 If issue is specific to a step, set the debug level for that step to Debugging |
| Issues with script execution: Get information on the logic of script execution Script execution failures | MIVR | SS_CM: XDebug1 SS_RM: XDebug1 SS_TEL: Debugging ENG: XDebug1 | UCCX Engine |
| Script editor installation failure (client side issues) |  |  |  |

| Component/Issue | Log files | Log levels | Component to select in RTMT |
|---|---|---|---|
| Agent login failure Agent state change issues | MIVR | SS_CM: Debugging, XDebug1 SS_RM: Upto XDebug4 Eng: Debugging SS_TEL: Debugging, XDebug1 SS_RMCM: Debugging, XDebug1 ICD_CTI: Debugging, XDebug1 | UCCX Engine |
| MADM | LIB_AXL: Debugging REST_CLIENT: Debugging LIB_CFG: Debugging ADM_CFG: Debugging | Cisco Unified CCX Administration |
| Cisco Finesse: webservices/realm/openfire/localhostaccess logs | Default logging | Cisco Finesse |
| Live Data isses on the Finesse Desktop | SocketIO Debugs | Service, Data Processing, Communication: Debug | Cisco Unified CCX Socket IO |
| MIVR | For 11.0: SS_RM: Upto XDebug5 For 11.5: SS_ROUTENQUEUE: Upto XDebug5 | UCCX Engine |

| Component/Issue | Log files | Log levels | Component to select in RTMT |
|---|---|---|---|
| CAD client side issues: Installation and upgrade failure Agent state change issues Unable to see right information on the agent desktop Other errors on the screen | Client logs from C:\Program Files\Cisco\Desktop\log | Open C:\Program Files\Cisco\Desktop\config\ Agent.cfg Set the following: [Program Log] Size=10MB Files=10 Threshold= TRACE | Logs from the Agent' PC |
| CSD client side issues: Installation and upgrade failure Unable to see right information on the  desktop Other errors on the screen | Client logs from C:\Program Files\Cisco\Desktop\log | Open C:\Program Files\Cisco\Desktop\config\Supervisor.cfg Set the following: [Program Log] Size=10MB Files=10 Threshold= TRACE | Logs from the Supervisor's PC |
| Cisco Desktop Administrator (thick client) | Client logs from C:\Program Files\Cisco\Desktop\log | Open C:\Program Files\Cisco\Desktop\config Administrator.cfg and SplkView.cfg Files=10 Size=10000000 | Logs from the Administrator's PC |

| Component/Issue | Log files | Log levels | Component to select in RTMT |
|---|---|---|---|
| Database related issues: Replication failure UCCX Database corruption UCCX Database start-up message | Database logs | Default log levels | Cisco Unified CCX Database |
| Historical Reports missing data - Calls not being written into the database - Data missing for a few days | MIVR | CRA_HRDM: Debuging, XDebug1 ICD_CTI: Debugging, XDebug1 SS_RM: Debuging, XDebug1 SS_CM: Debuging, XDebug1 SS_TEL: Debuging, XDebug1 SS_RMCM: Debuging, XDebug1 | UCCX Engine |
| Real Time Reporting (the one on the AppAdmin page) | MIVR | CRA_HRDM: Debuging, XDebug1 ICD_CTI: Debugging, XDebug1 SS_RM: Debuging, XDebug1 SS_CM: Debuging, XDebug1 SS_TEL: Debuging, XDebug1 SS_RMCM: Debuging, XDebug1 | UCCX Engine |

| Component/Issue | Log files | Log Level | Component in RTMT |
|---|---|---|---|
| Email/Chat Issues | MIVR and MADM | MIVR: SS_CHAT and SS_ROUTEANDQUEUE to Xdebugging MADM:UCCX_WEBSERVICESxdebug2                                                    SM : Runtime/CCPAPI/CCPPUBLICAPPS at default level | Cisco Unified CCX Administration /Cisco Unified CCX engine |

| # | Module | Role/Responsibility | File Pattern | Path/URL | RTMT Choice |
|---|---|---|---|---|---|
| 1 | SocialMiner Runtime | Getting social contacts from facebook/twitter/RSS etc Running Filters Triggering notification rules (HTTP/XMPP/Email/CCE) Interaction with MR PG (CCE) | CCBU-runtime.*.startup.log Error-runtime.*.startup.log | https://<SocialMiner Server IP/Host>/ccp-webapp/logs/runtime/ | Socialminer Runtime Service |
| 2 | SocialMiner API | Rest APIs Reply Templates XMPP Event publishing | CCBU-ccpapi.*.startup.log Error-ccpapi.*.startup.log | https://<SocialMiner Server IP/Host>/ccp-webapp/logs/ccpapi/ | Socialminer Rest API |
| 3 | SocialMiner Public Apps | Public facing proxy to reach SocialMiner Exposes restricted set of Rest APIs Typically used by Chat and Callback | CCBU-ccppublicapps.*.startup.log Error-ccppublicapps.*.startup.log | https://<SocialMiner Server IP/Host>/ccp-webapp/logs/ccppublicapps/ | Socialminer Public Rest API |
| 4 | SocialMiner Datastore (Cassandra) | Contact Storage | ccp-ds-storage.startup.log | https://<SocialMiner Server IP/Host>/ccp-webapp/logs/ccp-ds-storage/ | SocialMiner Datastore Service |
| 5 | SocialMiner Indexer (Solr) | Contact search and query performance | ccp-ds-indexer.request.*.log | https://<SocialMiner Server IP/Host>/ccp-webapp/logs/ccp-ds-indexer/ | SocialMiner Indexer Service |
| 6 | SocialMiner XMPP Server | XMPP eventing Chatrooms for chat contacts | *.log | https://<SocialMiner Server IP/Host>/ccp-webapp/logs/ccp-xmpp-server/ | Socialminer XMPP Service |
| 7 | SocialMiner ORM | Interact with Informix DB Manage configurations like feeds, filters, notifications, campaigns, etc Historical reporting record for CUIC | CCBU-orm.*.startup.log Error-orm.*.startup.log | https://<SocialMiner Server IP/Host>/ccp-webapp/logs/orm/ | Socialminer ORM Service |
| 8 | Cisco Tomcat | General Tomcat logging | *.log | https://<SocialMiner Server IP/Host>/ccp-webapp/logs/tomcat/ | Cisco Tomcat (System Services) |
| 9 | Cisco Tomcat (Token Authentication) | Token Authentication related details - used by the chat reply template | localhost.*.log | https://<SocialMiner Server IP/Host>/ccp-webapp/logs/tomcat/ | Cisco Tomcat (System Services) |
| 10 | SocialMiner System Health Snapshot | Can be accessed via SocialMiner's Administration tab > System Administration > System Logs > System Health Snapshot |  | Direct URL : http://<socialminer_hostname>/ccp-webapp/ccp/serviceability/SocialMinerSystemHealth.xml?category=all |  |

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 21-Nov-2023 | Initial Release |
| 1.0 | 15-May-2017 | Initial Release |