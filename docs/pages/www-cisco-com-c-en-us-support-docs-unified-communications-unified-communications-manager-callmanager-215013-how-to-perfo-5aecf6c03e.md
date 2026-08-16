---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-215013-how-to-perfo-5aecf6c03e
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/215013-how-to-perform-a-health-check-of-cucm-da.html
retrieved_at: 2026-08-16T17:59:14.254674+00:00
---

Perform a Health Check of CUCM Database Replication

# Perform a Health Check of CUCM Database Replication

### Download Options

Updated: July 17, 2025

Document ID: 215013

Contents

## Contents

## Introduction

This document describes important commands to verify Cisco Unified Communications Manager (CUCM) database replication, and its expected outputs.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of this topics:

- Cisco Unified Communications Manager

### Components Used

The information in this document is based on this software versions:

- Cisco Unified Communications Manager version 10.5.2.15900-8

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Database in CUCM is a fully meshed topology which means that the publisher and each subscriber connect logically to every server in the cluster; and all of them have the ability to update the data between them.

In order to verify database status in CUCM, access from Command Line Interface (CLI) must be granted in each of the nodes in the cluster. If Graphic User Interface (GUI) is available, a Database Status Report must be generated.

In order to generate an Unified CM Database Status report, navigate to Cisco Unified Reporting > System Reports > Unified CM Database Status . Select Generate a new report .

## Connectivity Verification

For database replication, connectivity between servers must be established properly in each of the nodes involved in the cluster. These commands allow you to know the status of each of them.

show network cluster

Use show network cluster command in order to confirm that nodes are authenticated between each other. The output from the publisher contains processnode table entries. However, all of the nodes must be authenticated (ensure that the security password is same on all of the nodes).

Publisher:

```
admin:show network cluster 10.1.89.30 CUCMv10SUB.alegarc2.lab CUCMv10SUB Subscriber callmanager DBSub authenticated using TCP since Mon Jul 1 13:44:09 2019 10.1.89.20 CUCM10.alegarc2.lab CUCM10 Publisher callmanager DBPub authenticated Server Table (processnode) Entries ---------------------------------- 10.1.89.20 10.1.89.30
```

Subscriber:

```
admin:show network cluster 10.1.89.30 CUCMv10SUB.alegarc2.lab CUCMv10SUB Subscriber callmanager DBSub authenticated 10.1.89.20 CUCM10.alegarc2.lab CUCM10 Publisher callmanager DBPub authenticated using TCP since Mon Jul 1 13:44:19 2019
```

run sql select * from processnode

Processnode table must list all nodes in the cluster.

```
admin:run sql select * from processnode pkid                                 name               mac systemnode description isactive nodeid tknodeusage ipv6name fklbmhubgroup tkprocessnoderole tkssomode ==================================== ================== === ========== =========== ======== ====== =========== ======== ============= ================= ========= 00000000-1111-0000-0000-000000000000 EnterpriseWideData     t                      t        1      1                    NULL          1                 0 68b56caa-d320-4c94-9c5a-43c3ba6cb4b8 10.1.89.20 f          10.1.89.20  t        2      0                    NULL          1                 0 a6a92a62-8e66-cdfc-80fa-56a688d3dd58 10.1.89.30 f                      t        3      1                    NULL          1                 0
```

utils network connectivity <IP/hostname>

Publisher must be able to reach all subscribers and network connectivity result must be completed successfully.

```
admin:utils network connectivity 10.1.89.30 This command can take up to 3 minutes to complete. Continue (y/n)?y Running test, please wait ... ...... Network connectivity test with 10.1.89.30 completed successfully .
```

Each subscriber must reach Publisher, and other subscribers included in the cluster network connectivity result must be completed successfully.

```
admin:utils network connectivity 10.1.89.20 This command can take up to 3 minutes to complete. Continue (y/n)?y Running test, please wait ... . Network connectivity test with 10.1.89.20 completed successfully .
```

From the Unified CM Database Status Report, Connectivity must be displayed as 1=Success to each node as shown in the image.

utils diagnose test

It checks all the components and returns passed/failed value. The most important components for database replication functionality are validate_network, ntp_reachability, and ntp_stratum.

```
admin:utils diagnose test Log file: platform/log/diag1.log Starting diagnostic test(s) =========================== test - disk_space : Passed (available: 1753 MB, used: 12413 MB) skip - disk_files : This module must be run directly and off hours test - service_manager : Passed test - tomcat : Passed test - tomcat_deadlocks : Passed test - tomcat_keystore : Passed test - tomcat_connectors : Passed test - tomcat_threads : Passed test - tomcat_memory : Passed test - tomcat_sessions : Passed skip - tomcat_heapdump : This module must be run directly and off hours test - validate_network : Passed test - raid : Passed test - system_info : Passed (Collected system information in diagnostic log) test - ntp_reachability : Passed test - ntp_clock_drift : Passed test - ntp_stratum : Passed skip - sdl_fragmentation : This module must be run directly and off hours skip - sdi_fragmentation : This module must be run directly and off hours Diagnostics Completed The final output will be in Log file: platform/log/diag1.log Please use 'file view activelog platform/log/diag1.log' command to see the output
```

utils ntp status

Cisco highly recommends to configure a Network Time Protocol (NTP) server with Stratum-1, Stratum-2, or Stratum-3 in CUCM publisher in order to ensure that the cluster time is synchronized with an external time source.

```
admin:utils ntp status ntpd (pid 8609) is running... remote           refid      st t when poll reach   delay   offset  jitter ============================================================================== *10.1.89.1       LOCAL(1)         2 u  935 1024  377    0.262    2.591   3.260 synchronised to NTP server (10.1.89.1) at stratum 3 time correct to within 32 ms polling server every 1024 s Current time in UTC is : Wed Jul 3 12:40:36 UTC 2019 Current time in America/Mexico_City is : Wed Jul 3 07:40:36 CDT 2019
```

NTP for subscribers is publisher server and must be visible as synchronized.

```
admin:utils ntp status ntpd (pid 30854) is running... remote           refid      st t when poll reach  delay   offset   jitter ============================================================================== *10.1.89.20       10.1.89.1       3 u  179 1024  377   0.524   -1.793    1.739 synchronized to NTP server (10.1.89.20) at stratum 4 time correct to within 50 ms polling server every 1024 s Current time in UTC is : Wed Jul 3 12:41:46 UTC 2019 Current time in America/Mexico_City is : Wed Jul 3 07:41:46 CDT 2019
```

## Services Verification

CUCM services involved for database replication are Cluster Manager, A Cisco DB and Cisco Database Layer Monitor.

utils service list

Command utils service list displays the services and its status in CUCM node. These services must be displayed as STARTED.

- Cluster Manager [STARTED]

- A Cisco DB [STARTED]

- A Cisco DB Replicator [STARTED]

- Cisco Database Layer Monitor [STARTED]

## Database Commands

Database replication commands must be run from the publisher.

utils dbreplication status

This command only triggers the check of the database status. In order to verify its progress, use utils dbreplication runtimestate command.

```
admin:utils dbreplication status Replication status check is now running in background . Use command 'utils dbreplication runtimestate' to check its progress The final output will be in file cm/trace/dbl/sdi/ReplicationStatus.2019_07_03_07_54_21.out Please use "file view activelog cm/trace/dbl/sdi/ReplicationStatus.2019_07_03_07_54_21.out " command to see the output
```

utils dbreplication runtimestate

Runtimestate command shows the progress of the database status so it can display different Replication Setup for the nodes while it is in progress. Once that command is COMPLETED, outputs can be verified and it shows the current database status.

```
admin:utils dbreplication runtimestate Server Time: Wed Jul 3 09:11:03 CDT 2019 Cluster Replication State: Replication status command started at: 2019-07-03-07-54 Replication status command COMPLETED 681 tables checked out of 681 Last Completed Table: devicenumplanmapremdestmap No Errors or Mismatches found. Use 'file view activelog cm/trace/dbl/sdi/ReplicationStatus.2019_07_03_07_54_21.out' to see the details DB Version: ccm10_5_2_15900_8 Repltimeout set to: 300s PROCESS option set to: 1 Cluster Detailed View from CUCM10 (2 Servers): PING      DB/RPC/   REPL.    Replication REPLICATION SETUP SERVER-NAME         IP ADDRESS        (msec)    DbMon?    QUEUE    Group ID    (RTMT) & Details -----------         ----------        ------    -------   -----    ----------- ------------------ CUCM10              10.1.89.20        0.013     Y/Y/Y     0        (g_2) (2) Setup Completed CUCMv10SUB          10.1.89.30        0.230     Y/Y/Y     0        (g_3) (2) Setup Completed
```

Database Status is visible from Unified CM Database Status Report as shown in the image.

## Hosts/Rhosts/Sqlhosts Files

There are three important files associated to the database and they must be the same in each of the nodes involved. In order to verify them from CLI, root access is required. However, Unified CM Database Status Report also displays this information as shown in the image.

## System History Log File

Database replication can be damaged due to ungraceful shutdowns and they are visible in System-history log.

Ungraceful shutdown example:

```
09/13/2019 15:29:01 | root: Boot 10.5.2.15900-8 Start 09/13/2019 16:55:24 | root: Boot 10.5.2.15900-8 Start
```

Graceful shutdown example:

```
09/03/2019 14:51:51 | root: Restart 10.5.2.15900-8 Start 09/03/2019 14:52:27 | root: Boot 10.5.2.15900-8 Start
```

Rebuild of the server is suggested when system suffered an ungraceful shutdown and it is documented in Cisco bug ID CSCth53322

## Verify

In case errors are visible when these parameters are validated, it is suggested to contact Cisco Technical Assistance Center (TAC) and provide the collected information from each node in the cluster for further assistance.

## Related Information

- Unified CM NTP Time Synchronization

- Procedure to Shut Down or Restart the System, version 12.5(1)

- Recover from Ungraceful Shutdown

### Revision History

3.0

17-Jul-2025

Recertification

2.0

25-Apr-2024

Updated Formatting to conform with Cisco's guidelines.

1.0

23-Oct-2020

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 3.0 | 17-Jul-2025 | Recertification |
| 2.0 | 25-Apr-2024 | Updated Formatting to conform with Cisco's guidelines. |
| 1.0 | 23-Oct-2020 | Initial Release |