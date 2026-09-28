---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-monitoring-guide-9-0-1-cucm-bk-m2f290d8-00-monitoring-cucm--6ba91c62b4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/monitoring_guide/9_0_1/CUCM_BK_M2F290D8_00_monitoring-cucm-presence-guide-90/CUCM_BK_M2F290D8_00_monitoring-cucm-presence-guide-90_chapter_010.html
retrieved_at: 2026-08-21T01:27:07.160147+00:00
---

Monitoring Cisco Unified Communications Manager IM and Presence, Release 9.0(1)

# Monitoring Cisco Unified Communications Manager IM and Presence, Release 9.0(1)

Updated: February 19, 2013

Chapter: High CPU and virtual memory issues

## Chapter: High CPU and virtual memory issues

# High CPU and virtual memory issues

## Monitor high CPU and virtual memory issues using Unified Operations Manager

Unified Operations Manager 8.6 and 8.7 provides an overview of CPU and virtual memory usage on your IM and Presence Service node. If usage is high, debug further using Unified RTMT.

- Cisco Tomcat

- Cisco Presence Engine

- Cisco SIP Proxy

- Cisco XCP Router

- Cisco XCP Connection Manager

- Cisco XCP Web Connection Manager

- Cisco XCP SIP Federation Connection Manager

- Cisco XCP XMPP Federation Connection Manager

## Monitor high CPU and virtual memory issues using Unified RTMT

Unified RTMT provides an overview of CPU and Virtual Memory usage using the CPU and Memory tool. This provides overall system usage statistics for all nodes in an IM and Presence cluster.

## High CPU issues

On IM and Presence Service , when you experience high overall CPU usage, Cisco recommends that you check the usage of the following processes that have historically caused high CPU on IM and Presence :

The cmoninit and sipd processes will both have 20+ individual instances, any one of which could be responsible for high CPU usage.

If the process consuming CPU is not in the preceding table, consult the following table for a list of other processes and their corresponding services. If the process causing high CPU is not in either table, the problem may reside with a system or platform service. Consult Cisco TAC for further assistance.

## High virtual memory issues

- tomcat

- jabberd

- pe

- all of the Connection Manager processes (cm, cm_web, cm_sip_fed & cm_xmpp_fed)

- all of the sipd processes

- all of the cmoninit processes

| Process | Service |
|---|---|
| tomcat | Cisco Tomcat |
| jabberd | Cisco XCP Router |
| pe | Cisco Presence Engine |
| cm | Cisco XCP Connection Manager |
| cm_web | Cisco XCP Web Connection Manager |
| cm_sip_fed | Cisco XCP SIP Federation Connection Manager |
| cm_xmpp_fed | Cisco XCP XMPP Federation Connection Manager |
| cmoninit | A Cisco DB |
| sipd | Cisco SIP Proxy |

| Note | The cmoninit and sipd processes will both have 20+ individual instances, any one of which could be responsible for high CPU usage. |
|---|---|

| Process | Service |
|---|---|
| amc | Cisco AMC Service |
| AuditLog | Cisco Audit Event Service |
| auth | Cisco XCP Authentication Service |
| BPS | Cisco Bulk Provisioning Service |
| cdpd | Cisco CDP |
| cdpAgt | Cisco CDP Agent |
| certM | Cisco Certificate Expiry Monitor |
| CiscoDRFLocal | Cisco DRF Local |
| CiscoDRFMaster | Cisco DRF Master |
| CiscoLicenseMgr | Cisco License Manager |
| CiscoSyslogSubAgt | Cisco Syslog Agent |
| dblrpc | A Cisco DB Replicator |
| dbmon | Cisco Database Layer Monitor |
| EspConfigAgent | Cisco Config Agent |
| hostagt | Host Resources Agent |
| interClusterSyncAgent | Cisco Intercluster Sync Agent |
| jds | Cisco XCP Directory Service |
| LpmTool | Cisco Log Partition Monitoring Tool |
| ma | Cisco XCP Message Archiver |
| Mib2agt | MIB2 Agent |
| oamagent | Cisco OAM Agent |
| replWatcher | Cisco Replication Watcher |
| RisDC | Cisco RIS Data Collector |
| rtmtreporter | Cisco Serviceability Reporter |
| sappagt | System Application Agent |
| snmpdm | SNMP Master Agent |
| srm | Cisco Server Recovery Manager |
| syncAgent | Cisco Sync Agent |
| tc | Cisco XCP Text Conference Manager |
| tracecollectionservice | Cisco Trace Collection Service |
| ttlogin | Cisco Login Datastore |
| ttreg | Cisco SIP Registration Datastore |
| ttroute | Cisco Route Datastore |
| ttsoft | Cisco Presence Datastore |
| xcpConfigManager | Cisco XCP Config Manager |