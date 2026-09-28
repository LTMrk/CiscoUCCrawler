---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-225943-guide-for-upgrading-from-broadworks-html-1869ca64e7
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks/225943-guide-for-upgrading-from-broadworks.html
retrieved_at: 2026-09-07T13:01:33.861512+00:00
---

Guide for Upgrading from BroadWorks 25.0

# Guide for Upgrading from BroadWorks 25.0

### Download Options

Updated: February 13, 2025

Document ID: 225943

Contents

## Contents

## Introduction

This document describes considerations and requirements for planning a Cisco BroadWorks system upgrade from the source release 20.0.

## Overview

All servers upgrade to the latest release Independent version available (consult the Software Compatibility Matrix section titled 'Supported Upgrade Maps').

## Operating System Requirements

Verify that the source Operating System (OS) is supported by the Target release.

Supported Operating Systems are Red Hat Enterprise Linux, Oracle Linux, and CentOS 7. CentOS 8 , CentOS Stream, Rocky Linux, and Alma Linux are not supported.

Linux 7 support ended on June 20th, 2024 with 2024.07 .

Linux 9 support is available from 2024.04+.

### Supported Linux Versions

2020.07+: 6.5+, 7, 8 2023.05+: 7, 8

2023.10+: 7, 8, 9 (Linux 9 is not supported on the Application Servers (AS) until 2024.04)

2024.04+: 7, 8, 9 2024.07+: 8, 9

### Database Server (DBS) Supported Linux Versions

2020.11 to 2022.06: 7.5+ only 2022.07+: 7.5+, 8.5+

2024.07+: 8.5+

2024.09: Final Release/End of Life

### OS Upgrades

BroadWorks has not historically supported in-place upgrades between major Linux versions. Historically, the recommendation was to perform a hardware swap, build a new server on the target Linux version, and migrate the existing server to the new server. Starting with release 2023.12, in-place Linux upgrades are supported from Linux 7 to 8 and 8 to 9. In order to perform an in-place Linux upgrade, servers must first be upgraded to 2023.12 or later.

For documentation on in-place Linux upgrades, refer to section 9 of the Software Management Guide . For documentation on the hardware swap process, refer to section 5.2.6 of the Software Management Guide and section 12.2 of the Maintenance Guide .

It is not recommended to use a hardware swap in order to upgrade BroadWorks at the same time or to perform a hardware swap or in-place Linux upgrade and a BroadWorks upgrade in the same maintenance window. Servers with a database must go through the upgrade process; a database from one version of BroadWorks cannot be imported into another version of BroadWorks.

## Upgrade Limitations and Server-Specific Notes

### DBS

The DBS must upgrade in multiple jumps in order to upgrade to the latest RI release due to OS restrictions. DBS 22.0 supports Linux 5 and 6. If running Linux 5 the DBS cannot upgrade beyond 22.0. Release Independent builds of the DBS do not support Linux 5. If running Linux 6 the DBS can upgrade to 2020.08. The DBS must then hardware swap to Linux 7 where it can upgrade again. When upgrading the DBS and Profile Server (PS) the versions of DBManagement and DBSObserver must match the version of the DBS in order to ensure that the underlying Oracle version matches for compatibility.

#### DBS Release and Oracle Release Alignment

22.0: Oracle 11 2018.11 to 2020.08: Oracle 12 2020.11+: Oracle 19

#### Skipping the DBS Upgrade

There is an option to skip the DBS upgrade and import the Database (DB) from 22.0 directly into the DBS 2022.03+. However, this process is not quick and ought to be tested in the lab to verify the timing expected for production. Refer to the DBS Release Notes section 6, BWKS-3069, and the DBS Configuration Guide section 6.5.7.3.

### Enhanced Call Logs

Enhanced Call Logs (ECL) is end of life on the DBS after DBS 2020.08. The ECL database must be migrated to a Network Database Server (NDS) for continued use, the migration is not automatic. Refer to the Enhanced Call Logs Solution Guide and the NDS Enhanced Call Logs Feature Description for more information. Refer to the Network Database Server Configuration Guide for setting up an NDS and the ECL Migration From DBS to NDS Feature Description for the migration procedure. The migration must be performed before the upgrade.

### Collaborate Servers

The End of Maintenance (EoM) for the Messaging Server (UMS), Sharing Server (USS), Video Server (UVS), WebRTC Server (WRS), Business Communicator Client (BTBC), and Connect Client was January 31, 2022. The latest RI version available for the UMS is 22.0 and for the USS, UVS, and WRS the latest available is 2022.01.

The AS at 24.0 is compatible with the UMS on 22.0 and 21.sp1. Upgrading the UMS to 22.0 is not recommended. The UMS at 22.0 uses MariaDB instead of Oracle TimesTen necessitating additional steps to upgrade, has a separate Method of Procedure (MoP), and requires an additional node for redundancy. See the UMS Upgrade MOP and the Field Notification about MariaDB 10.1 End of Life .

It is recommended to replace the Collaborate services with WebEx for BroadWorks. Refer to the WebEx for BroadWorks Solutions Guide .

## Review Documentation

Release notes for the target release and any releases between the target and source release must be reviewed.

26.0 Release Notes Upgrade Method of Procedure (MOP) Refer to the Software Compatibility Matrix for the official supported upgrade paths.

## License Requirements

A new license is required for the target release. In order to request a license open a ticket .

## Best Practices

### Notify BroadWorks Support Before an Upgrade

It is recommended to notify BroadWorks Support a few days in advance with a severity 4 (s4) ticket. If an issue arises during the maintenance, raise the severity of the ticket to s1, open a new s1 ticket, or call the support line to speak to an engineer.

### Test Plans

A test plan is essential in order to ensure a smooth upgrade. A test plan must be developed and tested in a lab before a production upgrade. Run the test plan on the system before the upgrade and record the results. This ensures that the system is healthy, verifies that all test users and accounts are correctly configured and functioning, provides an opportunity to catch potential gaps in the test plan, and provides a time estimate on how long testing is expected to take.

Each server must be tested after it has been upgraded in order to ensure that it is functioning as expected before moving on to upgrade to the next server in the sequence.

### Pre-Install Check Script

The pre-install check script must be run on every server, lab, and production, and any warnings or failures must be addressed before the upgrade.

### Lab Upgrade

It is always recommended to test the upgrade, the test plan, and the target release with any third-party tools, applications, or clients in a lab environment that replicates the production environment. The lab can be scaled down but ought to have the same server types, software version, OS version, access devices, Session Border Control (SBC), and so on. Treat the lab upgrade as a dry run for the production environment upgrade. Use the latest target release patch level when upgrading the lab. Keep the time between the lab and production upgrade to 3 months or less.

### Scheduling and Upgrade Sequence

Upgrades are expected to take place over multiple maintenance windows spread across several nights and are performed in the Installation and Upgrade Order as documented in section 4.2 of the Software Management Guide . Always perform upgrades during a predetermined maintenance window (during a non-busy hour). Always upgrade one node at a time, and ensure that one or more than one node of a cluster is down at any given time. The length of the maintenance window (MW), the number of servers to upgrade, the server type, and how long testing is expected to take determine how many maintenance windows are required. All servers in a cluster must be upgraded in the same MW. Leave the time available in the scheduled MW for troubleshooting and/or rollback if required.

### Upgrade Failures

If an issue is discovered during the post-upgrade testing or an upgrade fails, gather logs before reverting to the source release or restoring the server. Backup the entire logs directory in order to ensure all potentially helpful logs are kept. Immediately open a ticket and call Support for assistance while still in the MW.

### Revision History

1.0

19-May-2026

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 19-May-2026 | Initial Release |