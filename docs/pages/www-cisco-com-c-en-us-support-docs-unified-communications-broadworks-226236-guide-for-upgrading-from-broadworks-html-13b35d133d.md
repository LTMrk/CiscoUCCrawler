---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-226236-guide-for-upgrading-from-broadworks-html-13b35d133d
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks/226236-guide-for-upgrading-from-broadworks.html
retrieved_at: 2026-09-07T13:01:29.759762+00:00
---

Guide for Upgrading from BroadWorks 23.0

# Guide for Upgrading from BroadWorks 23.0

### Download Options

Updated: June 23, 2025

Document ID: 226236

Contents

## Contents

## Introduction

This document describes the considerations and requirements to aid in planning an upgrade from the source release of BroadWorks 23.0.

## Overview

BroadWorks Release 23.0 supports upgrades to releases, 24.0 and 25.0. Release 23.0 was EoM at the end of July 2024 , and 24.0 End of Maintenance (EoM) is expected at the end of July 2026. Non-Application Servers upgrade to the latest Release Independent version available (consult the Software Compatibility Matrix section titled 'Supported Upgrade Maps'). Application servers upgrade to 2024.07. Once all servers are upgraded the Application Servers must be upgraded again to the latest version up to 2026.07.

## Release Independent Versions

Starting at release 23.0 the MS is Release Independent (RI), at 24.0 all servers except the Application Servers (AS) RI, and at 25.0 all servers are Release Independent. All new features, bugs, and security fixes are delivered in a new version. Patches are not available, instead, servers must be upgraded from one version to another in order to obtain a fix. A new version of each server is released each month (instead of monthly patch bundles) or more frequently if an urgent fix is required.

RI versions use a different format than the standard Rel_24.0_1.944 format. This RI format is Server_Rel_yyyy.mm_x.xxx:

- The server is MS, for example:

- yyyy is the four-digit year

- mm is the two-digit month

- x.xxx is the incremental release for that month

MS_Rel_2022.11_1.273.Linux-x86_64.bin is a version of the MS released in November of 2022. Often this is abbreviated to 2022.11 if not referring to a specific server type or incremental version.

## Operating System Requirements

Verify that the source Operating System (OS) is supported by the Target release.

Supported OS are Red Hat Enterprise Linux, Oracle Linux, and CentOS 7. CentOS 8 , CentOS Stream, Rocky Linux, and Alma Linux are not supported.

Linux 6 support ended on April 30th, 2023 with 2023.05 . Linux 7 support ended on June 20th, 2024 with 2024.07 .

Linux 9 support is available from 2023.09+.

### Major Release Supported Linux Versions

R23: 5.9+, 6.5+, 7 and 8.x (ap385046 required) R24: 6.5+, 7, 8

### Release Independent Supported Linux Versions

2018.01+: 5.9+, 6.5+, 7 2019.10+: 6.5+, 7 2020.07+: 6.5+, 7, 8 2023.05+: 7, 8

2023.10+: 7, 8, 9 (Linux 9 is not supported on the AS until 2024.04)

2024.04+: 7, 8, 9 2024.07+: 8, 9

### Database Server (DBS) Supported Linux Versions

2018.11 to 2020.08: 6.5+, 7 2020.11 to 2022.06: 7.5+ only 2022.07+: 7.5+, 8.5+

2024.07+: 8.5+

2024.09: Final Release/End of Life

### OS Upgrades

BroadWorks has not historically supported in-place upgrades between major Linux versions. Historically, the recommendation is to perform a hardware swap, build a new server on the target Linux version, and migrate the existing server to the new server. Starting with release 2023.12, in-place Linux upgrades are supported from Linux 7 to 8 and 8 to 9. In order to perform an in-place Linux upgrade, servers must first be upgraded to 2023.12 or later.

For documentation on in-place Linux upgrades, refer to section 9 of the Software Management Guide . For documentation on the hardware swap process, refer to section 5.2.6 of the Software Management Guide and section 12.2 of the Maintenance Guide .

It is not recommended to use a hardware swap to upgrade BroadWorks at the same time or to perform a hardware swap or in-place Linux upgrade and a BroadWorks upgrade in the same maintenance window. Servers with a database must go through the upgrade process; a database from one version of BroadWorks cannot be imported into another version of BroadWorks.

## Upgrade Limitations and Server-Specific Notes

### Profile Server and Xtended Service Platform Upgrade to Application Delivery Platform

Starting at release 24.0, the Profile Server (PS) and Xtended Service Platform (XSP) become the same server type, known as the Application Delivery Platform (ADP). The PS and XSP servers upgrade in place and become the ADP server type after the upgrade. When upgrading from 23.0 the PS and XSP can only upgrade as far as ADP 2024.07. After which the ADP must be upgraded again in order to get to the latest version.

An ADP license and an updated version of the deployed apps are required. XSP upgrades must take place after the Application Servers (AS) are upgraded. There are RI versions of the PS and XSP on the download portal but these are only for systems that deploy the Execution Server (XS) server in place of the AS. All systems with an AS must upgrade PS and XSPs to ADP.

Cisco BroadWorks applications and web applications must be manually upgraded on XSP, PS, and ADP.

### Database Server

The Database Server (DBS) must upgrade in multiple jumps in order to upgrade to the latest RI release due to OS restrictions. DBS 22.0 supports Linux 5 and 6. If running Linux 5 the DBS cannot upgrade beyond 22.0. RI builds of the DBS do not support Linux 5. If running Linux 6 the DBS can upgrade to 2020.08. The DBS must then hardware swap to Linux 7 where it can upgrade again. When upgrading the DBS and PS the versions of DBManagement and DBSObserver must match the version of the DBS in order to ensure that the underlying Oracle version matches for compatibility.

#### DBS Release and Oracle Release Alignment

22.0: Oracle 11 2018.11 to 2020.08: Oracle 12 2020.11+: Oracle 19

#### Skipping the DBS Upgrade

There is an option to skip the DBS upgrade and import the DB from 22.0 directly into the DBS 2022.03+. However, this process is not quick and must be tested in the lab in order to verify the timing expected for production. Refer to the DBS Release Notes section 6, BWKS-3069, and the DBS Config Guide section 6.5.7.3.

### Enhanced Call Logs

Enhanced Call Logs (ECL) is end of life on the DBS after DBS 2020.08. The ECL database must be migrated to a Network Database Server (NDS) for continued use, the migration is not automatic. Refer to the Enhanced Call Logs Solution Guide and the NDS Enhanced Call Logs Feature Description for more information. Refer to the Network Database Server Configuration Guide for setting up an NDS and the ECL Migration From DBS to NDS Feature Description for the migration procedure. The migration must be performed prior to the upgrade.

### Collaborate Servers

The EoM for the Messaging Server (UMS), Sharing Server (USS), Video Server (UVS), WebRTC Server (WRS), Business Communicator Client (BTBC), and Connect Client was January 31, 2022. The latest RI version available for the UMS is 22.0 and for the USS, UVS, and WRS the latest available is 2022.01.

The AS at 24.0 is compatible with the UMS on 22.0 and 21.sp1. Upgrading the UMS to 22.0 is not recommended. The UMS at 22.0 uses MariaDB instead of Oracle TimesTen necessitating additional steps in order to upgrade, has a separate Method of Procedure (MoP), and requires an additional node for redundancy. See the UMS Upgrade MOP and the Field Notification about MariaDB 10.1 End of Life .

It is recommended to replace the Collaborate services with WebEx for BroadWorks. Refer to the WebEx for BroadWorks Solutions Guide .

## Review Documentation

Release notes for the target release and any releases between the target and source release must be reviewed. If the target release is 24.0 the release notes for 24.0 and 25.0 must be reviewed. 24.0 Release Notes

25.0 and up Release Notes Upgrade Method of Procedure Refer to the Software Compatibility Matrix for the official supported upgrade paths.

## License Requirements

A new license is required for the target release. In order to request a licence open a ticket . Request that the PS and XSP licenses be converted to ADP licenses; the ADP does not accept a PS or XSP license.

## Best Practices

### Notify BroadWorks Support Before an Upgrade

If performing an upgrade without the support of the Upgrade Team it is recommended to notify BroadWorks Support a few days in advance with a severity 4 (s4) ticket. If an issue arises during the maintenance, raise the severity of the ticket to s1, open a new s1 ticket, or call the support line in order to speak to an engineer.

### Test Plans

A test plan is essential in order to ensure a smooth upgrade. A test plan must be developed and tested in a lab prior to a production upgrade. Run the test plan on the system before the upgrade and record the results. This ensures that the system is healthy, verifies that all test users and accounts are correctly configured and functioning, provides an opportunity to catch potential gaps in the test plan, and provides a time estimate on how long testing is expected to take.

Each server must be tested after it has been upgraded in order to ensure that it is functioning as expected before moving on to upgrade to the next server in the sequence.

### Patching

Patch the source release to six months or less of the latest patch level before upgrading.

### Pre-Install Check Script

The pre-install check script must be run on every server, lab, and production, and any warnings or failures addressed before the upgrade.

### Lab Upgrade

It is always recommended to test the upgrade, the test plan, and the target release with any third-party tools, applications, or clients in a lab environment that replicates the production environment. The lab can be scaled down but ought to have the same server types, software version, OS version, access devices, Session Border Control (SBC), and so on. Treat the lab upgrade as a dry run for the production environment upgrade. Use the latest target release patch level when upgrading the lab. Keep the time between the lab and production upgrade to three months or less.

### Scheduling and Upgrade Sequence

Upgrades are expected to take place over multiple maintenance windows spread across several nights and are performed in the Installation and Upgrade Order as documented in section 4.2 of the Software Management Guide . Always perform upgrades during a predetermined maintenance window (during a non-busy hour). Always upgrade one node at a time, and ensure that one or more than one node of a cluster is down at any given time. The length of the maintenance window (MW), the number of servers to upgrade, the server type, and how long testing is expected to take determine how many maintenance windows are required. All servers in a cluster must be upgraded in the same MW. Leave time available in the scheduled MW for troubleshooting and/or rollback if required.

### Upgrade Failures

If an issue is discovered during the post-upgrade testing or an upgrade fails, gather logs before reverting to the source release or restoring the server. Backup the entire logs directory in order to ensure all potentially helpful logs are kept. Immediately open a ticket and call Support for assistance while still in the MW.

### Revision History

1.0

06-Aug-2026

Initial Release

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- BroadWorks

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 06-Aug-2026 | Initial Release |