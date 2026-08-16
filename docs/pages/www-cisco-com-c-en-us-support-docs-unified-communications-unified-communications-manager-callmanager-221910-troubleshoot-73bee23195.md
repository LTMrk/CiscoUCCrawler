---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-221910-troubleshoot-73bee23195
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/221910-troubleshoot-memory-allocation-failed-du.html
retrieved_at: 2026-08-16T18:00:30.190639+00:00
---

Troubleshoot Memory Allocation Failed during Query Processing after SIP Trunk Fails to Be Added

# Troubleshoot Memory Allocation Failed during Query Processing after SIP Trunk Fails to Be Added

### Download Options

Updated: January 26, 2025

Document ID: 221910

Contents

## Contents

## Introduction

This document describes how to troubleshoot the error message "Memory allocation failed during query processing" on CUCM when a SIP Trunk fails to be added.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- VOS (Voice Operating System)

- CUCM (Cisco Unified Communications Manager).

- SIP (Session Interface Protocol).

- Informix Database.

- CLI (Command Line Interface).

### Components Used

This document is intended for CUCM and is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

When you add a SIP trunk to the CUCM server, there are times when the error shown in the image is displayed.

Perform the next steps before you reproduce the issue.

Step 1 . Set the logs to detailed level in all the CUCM nodes

- CM Trace - DB Layer Monitor - CCMAdmin Web Service - CCMUser Web Service

Note : Keep in mind that some traces are already set to detailed level, this configuration depends on the version of CUCM that you have installed.

Step 2. Reproduce the issue. Attempt to add the SIP trunk and mark down the time when it fails to accomplish the task

## Troubleshoot

Navigate to the RTMT (Real-Time Monitor Tool) and get these traces:

- CM Trace - DB Layer Monitor - CCMAdmin Web Service - CCMUser Web Service

- Event-Viewer Application Logs

- Event-Viewer System Logs

### Log Analysis

From the CCMAdmin Web Service Logs

The SIP Trunk is inserted into the database

```
2024-03-14 09:51:12,487 DEBUG [http-nio-1027-exec-7] formhandlers.TrunkFormHandler - Insert Trunk 2024-03-14 09:51:12,570 DEBUG [http-nio-1027-exec-7] utilities.DbRead - reading from cache... 2024-03-14 09:51:12,573 DEBUG [http-nio-1027-exec-7] utilities.DbRead - reading from cache...
```

The SIP Trunk Device is updated with a unique ID

```
2024-03-14 09:51:12,590 DEBUG [http-nio-1027-exec-7] formhandlers.TrunkFormHandler - Updating SIP - devicePkid = e277a39a-1437-84ba-5047-57adddc75a43 ... The SP Trunk starts to be configured within the database 2024-03-14 09:51:12,618 DEBUG [http-nio-1027-exec-7] formhandlers.Device - update initiated 2024-03-14 09:51:12,620 DEBUG [http-nio-1027-exec-7] formhandlers.Device - Insert/update device ... 2024-03-14 09:51:13,449 DEBUG [http-nio-1027-exec-7] utilities.DbRelatedUtil - 1 row(s) affected. ... 2024-03-14 09:51:13,910 DEBUG [http-nio-1027-exec-7] utilities.DbRelatedUtil - 1 row(s) affected. 2024-03-14 09:51:13,913 INFO  [http-nio-1027-exec-7] utilities.SIPDeviceUtil - Entering checkSecurityProfilePortDuplicates ...
```

The insertion of the device fails, and the configuration commences its rollback

```
2024-03-14 09:51:14,294 ERROR [http-nio-1027-exec-7] formhandlers.Device - insert/update failed.  Rollback changes
```

Handle Exception is thrown by the Database

```
2024-03-14 09:51:14,338 ERROR [http-nio-1027-exec-7] formhandlers.TrunkFormHandler - Exception: Memory allocation failed during query processing. java.sql.SQLException: Memory allocation failed during query processing. 2024-03-14 09:51:14,360 INFO  [http-nio-1027-exec-7] actions.BaseAction - SQLException :: -208::java.sql.SQLException: Memory allocation failed during query processing. 2024-03-14 09:51:14,363 DEBUG [http-nio-1027-exec-7] actions.BaseAction - Db Error :: Memory allocation failed during query processing. 2024-03-14 09:51:14,365 DEBUG [http-nio-1027-exec-7] actions.BaseAction - Error could not be mapped using zero :: Memory allocation failed during query processing. java.lang.NumberFormatException: For input string: "Memory allocation failed during query processing." 2024-03-14 09:51:14,370 DEBUG [http-nio-1027-exec-7] actions.BaseAction - Error Code :: 0 2024-03-14 09:51:14,410 DEBUG [http-nio-1027-exec-7] actions.BaseAction - DBE Error code was not set :: java.sql.SQLException: Memory allocation failed during query processing. 2024-03-14 09:51:14,412 DEBUG [http-nio-1027-exec-7] actions.BaseAction - Parsing Database Specific Error :: java.sql.SQLException: Memory allocation failed during query processing. :: error.add 2024-03-14 09:51:14,414 ERROR [http-nio-1027-exec-7] actions.BaseAction - Caller Specified DatabaseException [error.add] :: java.sql.SQLException: Memory allocation failed during query processing.
```

In the CCM Informix logs it is possible to see several of these errors

```
ERROR Estimate FAILED for table 'ccm12_5_1_16900_48:"informix".
```

There are certain scenarios when you can see an NTP error

```
Mar 14 09:51:23 FXSDCWCMFPUB user 4 platform: Response from 'ntpdate -q': server X.X.X.X, stratum 0, offset 0.000000, delay 0.00000#01214 Mar 09:51:23 ntpdate[8646]: no server suitable for synchronization found.
```

## Solution

Warning: To clear the Memory Allocation, you need to restart the services off business hours as the restart of the services listed can impact the performance of your voice system.

Note : This process requires to be done only in CUCM Publisher node.

Step 1. Restart the Cisco Tomcat service (utils service restart Cisco Tomcat) through the CLI.

The Cisco Tomcat restart  implies that features such as Extension Mobility, the Self-Care portal, the CUCM GUI and the log in of the users  cannot be accessible while the service is down.

The GUI takes around 5 minutes to be available after the service restart, thus seen a 404 Not Found error is expected.

Step 2. Add the SIP Trunk device to the CUCM.

Step 3. If step 2 does not complete successfully, restart the A Cisco DB service in the CUCM publisher node via the CLI (utils service restart A Cisco DB),

Keep in mind that when you restart A Cisco DB in the publisher, all the databases are restarted, so you cannot configure or add features and configurations into the CUCM servers, and the attempt to add or configure anything in the servers can get lost after the service has come back and all the databases have set up again because all  the subscribers' databases get into Read-Only while the A Cisco DB service is in restart mode.

However, you can make phone calls, since this information is stored in the In-Memory Database as Read-Only, you can configure Call Manager Groups specifically for failover purposes, which depends on the node you want to restart, so the phones are kept registered.

Step 4. Once you have restarted the A Cisco DB service in all the nodes, wait around 15 to 20 minutes and then add the SIP Trunk.

Step 5. If the problem persists after the restart of the Cisco Tomcat and A Cisco DB on the Publisher, restart those services on the Subscriber nodes that are meant for call-processing.

Note :

This issue can be also seen in these scenarios.

1. When the System has experienced or is still experiencing High CPU.

2. When the Network Time Protocol (NTP) is not synchronised , which then provokes an unsynchronization between all the nodes' databases.

3. When there are certificates expired.

### Revision History

1.0

27-Jan-2025

Initial Release

### Contributed by Cisco Engineers

Miguel E Castillo Torres

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 27-Jan-2025 | Initial Release |