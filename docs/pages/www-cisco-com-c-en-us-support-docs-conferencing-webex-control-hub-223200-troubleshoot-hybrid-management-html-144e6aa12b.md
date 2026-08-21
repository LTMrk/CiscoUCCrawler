---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-223200-troubleshoot-hybrid-management-html-144e6aa12b
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/223200-troubleshoot-hybrid-management.html
retrieved_at: 2026-08-21T06:32:23.412419+00:00
---

Troubleshoot Hybrid Management Connector Stopped Status

# Troubleshoot Hybrid Management Connector Stopped Status

### Download Options

Updated: July 3, 2025

Document ID: 223200

Contents

## Contents

## Introduction

This document describes how to identify and fix the failed status on Management Connector unable to affect Hybrid Services hosted on an Expressway.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- A Webex Organization.

- Webex Hybrid Calendar.

- Cisco Expressways.

### Components Used

The information in this document is based on these software and hardware versions:

Webex Control Hub b uild 20250626-0fe1785 .

- Hybrid Calendar with Exchange 2019.

- Cisco Expressway-C X15.0

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background

It is being found that after upgrading Expressway firmware the management Connector is unable to start leaving the Management Connector and all Hybrid Services hosted Offline from Control Hub.

## Error from Control Hub

WIth an Administrator account, log into admin.webex.com > Services > Hybrid > Hybrid Calendar with Exchange> Resources > View All .

Control Hub error

Select the affected Cluster and Node and confirm the Offline status.

Offline status

## Error from Expressway GUI

Go to Expressway login > Status > Alarms . Locate Application failed alarm for mgmt service.

Alarm

```
"Several unexpected software errors were detected in /opt/c_mgmt/bin/c_mgmt.sh /var/run/c_mgmt/c_mgmt.pid: 1. This service will not be restarted automatically."
```

Alarm extracted from loggingsnapshot...txt

```
2025-06-30T21:53:48.354-04:00 ccnp-expressway-hybrid1 supervisor: Level="ERROR" Event="Alarm Raised" Id="15019" UUID="1a18bfa6-f822-11e1-b0db-c35cb1b8e3e5" Severity="error" Detail="Application failed: Several unexpected software errors were detected in /opt/c_mgmt/bin/c_mgmt.sh /var/run/c_mgmt/c_mgmt.pid: 1. This service will not be restarted automatically." UTCTime="2025-07-01 01:53:48,353"
```

## Troubleshooting

There are 3 known ways to collect Expressway logs, for this alarm the best option is Diagnostic Logging. Go to Expressway login > Maintenance > Diagnostics > Hybrid Services Log Levels . Make sure Hybrid Services Log Levels are set to DEBUG .

Log Levels

### Enable Diagnostic Logging while issue is replicated.

Go to Expressway login > Maintenance > Diagnostics > Diagnostic logging > Start new log . Once logs are collected, open loggingsnapshot...txt file and search for Permission Denied .

```
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt:   File "./cafedynamic/cafemanager.py", line 128, in _initialise_filesystem_to_full
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt:   File "./cafedynamic/cafemanager.py", line 187, in _create_template_dir
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt:   File "./cafedynamic/cafemanager.py", line 181, in _create_template_dir
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt:   File "./cafedynamic/cafexutil.py", line 387, in make_path
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt:   File "./cafedynamic/cafexutil.py", line 401, in makedirs
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt:   File "<frozen os>", line 225, in makedirs
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt: PermissionError: [Errno 13] Permission denied: '/mnt/harddisk/current/fusion/template'
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt: 
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt: During handling of the above exception, another exception occurred:
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt: 
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt: Traceback (most recent call last):
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt:   File "<string>", line 11, in <module>
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt:   File "./managementconnector/managementconnectormain.py", line 40, in main
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt:   File "./managementconnector/applicationrunner.py", line 41, in launch
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt:   File "./managementconnector/mgmtconnector.py", line 98, in start
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt:   File "./cafedynamic/cafemanager.py", line 98, in start
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt:   File "./cafedynamic/cafemanager.py", line 73, in _initialise_filesystem
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt:   File "./cafedynamic/cafemanager.py", line 138, in _initialise_filesystem_to_full
2025-06-30T21:53:09.102-04:00 ccnp-expressway-hybrid1 _c_mgmt: Exception: [Errno 13] Permission denied: '/mnt/harddisk/current/fusion/template'
```

### Create Full System Snapshot.

Go to Expressway login > Maintenance > Diagnostics > System snapshot > Create full snapshot . Open hybrid_services...log file and search for Permission Denied .

### Send Logs to Webex.

Go to Expressway login > Applications > Hybrid Services > Connector Logging > Send .

Warning : Option not available since Connector is Offline.

## Solution

### Login via SSH

Log in via SSH into the affected node with root account. Type:

```
ls -la /mnt/harddisk/current/
```

SSH

A healthy and working Connector have these filesystem permissions:

```
drwxr-xr-x  8 root root 4096 Apr 29 21:53 .
drwxr-xr-x 13 root root 4096 Jun 30 21:52 ..
drw-------  3 root root 4096 Apr 29 21:05 clusterdb
drwxr-xr-x  2 root root 4096 Apr 29 21:06 debug
drwxr-xr-x  6 root root 4096 Apr 29 21:54 fusion
drwxr-xr-x  7 root root 4096 Apr 29 21:54 opt
drwxr-xr-x  5 root root 4096 Apr 29 21:09 persistent
drwxr-xr-x  3 root root 4096 Jun  8 08:07 tbl
```

The modes are read ( r ), write ( w ), or execute ( x ). The first field contains 10 characters referring to these characteristics:

```
Character    What it means
        1               "d" if a directory, "-" if a file
        2               "r" if file is readable to user, "-" if not
        3               "w" if file is writable to user, "-" if not
        4               "x" if file is executable to user, "-" if not
        5-7             same as 2-4, with reference to group
        8-10            same as 2-4, with reference to everyone on the system
```

The affected node do not have the correct permission set for fusion filesystem.

```
drwxr-x---  6 root root 4096 Apr 29 21:54 fusion
```

To change the permissions of a file, one uses the chmod command (short for change mode ), with this syntax:

```
chmod 755 /mnt/harddisk/current/fusion
```

fusion

The Unix representation drwxr-xr-x translates to the numeric notation: 755

Note : Make sure to check correct permissions for all the directories since not only fusion could be affected.

## Validate Connector Management

### Expressway GUI

Go to Expressway login > Applications > Hybrid Services > Connector Management > Restart connector button.

Restart connector

Connector Management successfully start.

Successful

## Root Cause

One or more filesystem permission used for Hybrid Services was modified affecting the ability to start correctly to the Hybrid Management Connector, Cisco is still investigating to conclude the reason.

## Related Information

N/A

### Revision History

1.0

03-Jul-2025

Initial Release

### Contributed by Cisco Engineers

Josue Jonathan Vizcaino Huape

Technical Consulting Engineer

### This Document Applies to These Products

- Webex Control Hub

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 03-Jul-2025 | Initial Release |