---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-221119-guide-for-upgrading-from-broadworks-21-s-htm-dd74ca7009
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks/221119-guide-for-upgrading-from-broadworks-21-s.html
retrieved_at: 2026-09-07T13:01:42.305636+00:00
---

Guide for Upgrading from BroadWorks 21.sp1

# Guide for Upgrading from BroadWorks 21.sp1

### Download Options

Updated: October 19, 2023

Document ID: 221119

Contents

## Contents

## Introduction

This document describes considerations and requirements to aid in planning an upgrade from the source release of BroadWorks 21.sp1.

## Overview

BroadWorks Release 21.sp1 supports upgrades to releases 22.0, 23.0 and 24.0. Release 22.0 is End of Maintenance (EoM) and 23.0 is EoM at the end of July 2024 . Upgrading to 24.0 is the recommended path.

## Release Independent Versions

Starting at release 23.0 the MS is Release Independent (RI) and at 24.0 all servers except the AS Release Independent. All new features, bugs, and security fixes are delivered in a new version. Patches are not available, instead, servers need to be upgraded from one version to another to obtain a fix. A new version of each server is released each month (instead of monthly patch bundles) or more frequently if an urgent fix is required.

RI versions use a different format than the standard Rel_24.0_1.944 format. This RI format is Server_Rel_yyyy.mm_x.xxx:

- The server is MS, for example

- yyyy is the 4-digit year

- mm is the 2-digit month

- x.xxx is the incremental release for that month

MS_Rel_2022.11_1.273.Linux-x86_64.bin is a version of the MS released in November of 2022. Often this is abbreviated to 2022.11 if not referring to a specific server type or incremental version.

## Operating System Requirements

Verify that the source Operating System (OS) is supported by the Target release.

Supported Operating Systems are Red Hat Enterprise Linux, Oracle Linux, and CentOS 7. CentOS 8 , CentOS Stream, Rocky Linux, and Alma Linux are not supported.

Linux 6 support ended on April 30th 2023 with 2023.05. Linux 7 support ends on June 20th 2024 with 2024.07.

### Major Release Supported Linux Versions

R21: 5, 6 and 7 (ap379473 required) R22: 5.9+, 6.5+, 7 R23: 5.9+, 6.5+, 7 and 8.x (ap385046 required) R24: 6.5+, 7, 8

### Release Independent Supported Linux Versions

2018.01+: 5.9+, 6.5+, 7 2019.10+: 6.5+, 7 2020.07+: 6.5+, 7, 8 2023.05+: 7, 8 2023.09+: 7, 8, 9

### Database Server (DBS) Supported Linux Versions

DBS R21: 5, 6 DBS R22: 5.9+, 6.5+ DBS 2018.11 to 2020.08: 6.5+, 7 DBS 2020.11 to 2022.06: 7.5+ only DBS 2022.07+: 7.5+, 8.5+

### OS Upgrades

BroadWorks does not support an in-place upgrade between major Linux versions. It is recommended to perform a hardware swap, build a new server on the target Linux version and migrate the existing server to the new server. Refer to section 5.2.6 of the Software Management Guide and section 12.2 of the Maintenance Guide .

It is not recommended to use a hardware swap to upgrade BroadWorks at the same time or to perform a hardware swap and BroadWorks upgrade in the same maintenance window. Servers with a database must go through the upgrade process; a database from one version of BroadWorks cannot be imported into another version of BroadWorks.

## Upgrade Limitations and Server-Specific Notes

### Network Server Rollback

The Network Server (NS) can upgrade from 21.sp1 to RI but the rollback is not supported, a revert is required if returning to 21.sp1 is necessary. A rollback changes the server version back to the source release and rolls back all changes to the DB keeping any added contents. A revert changes the server version back to the source release and imports the DB backup taken just before the upgrade, any data added to the DB since the upgrade is lost on a revert. The solution is to upgrade the NS to 23.0 first and then upgrade to the desired RI version. If a double upgrade is not desired, a workaround, if the rollback is required, would be to revert the NS and then run through the Network Server and Application Server Synchronization procedure from the Maintenance Guide to sync the NS database with the AS database.

### Profile Server and Xtended Service Platform Upgrade to Application Delivery Platform

Starting at release 24.0, the Profile Server (PS) and Xtended Service Platform (XSP) become the same server type, known as the Application Delivery Platform (ADP). The PS and XSP servers upgrade in place and become the ADP server type after the upgrade.

From 21.sp1 the latest RI version of ADP that the PS and XSPs can upgrade to is 2022.07. To upgrade to 2022.08+, it requires a two-step upgrade. An ADP license and an updated version of the deployed apps are required. XSP upgrades must take place after the Application Servers (AS) are upgraded. There are RI versions of the PS and XSP on the download portal but these are only for systems that deploy the Execution Server (XS) server in place of the AS. All systems with an AS must upgrade PS and XSPs to ADP.

Cisco BroadWorks applications and web applications need to be manually upgraded on XSP, PS and ADP.

### Database Server

The Database Server (DBS) must upgrade in multiple jumps to upgrade to the latest RI release due to OS restrictions. DBS 21.sp1 supports Linux 5 and 6. If running Linux 5 the DBS can only upgrade to 22.0. If running Linux 6 the DBS can upgrade to RI 2020.08. The DBS must then hardware swap to Linux 7 where it can upgrade again. When upgrading the DBS and PS the versions of DBManagement and DBSObserver must match the version of the DBS to ensure that the underlying Oracle version matches for compatibility.

#### DBS Release and Oracle Release Alignment

21.sp1 and 22.0: Oracle 11 2018.11 to 2020.08: Oracle 12 2020.11+: Oracle 19

#### Skipping the DBS Upgrade

There is an option to skip the DBS upgrade and import the DB from 21.sp1 directly into the DBS 2022.03+. However, this process is not quick and ought to be tested in the lab to verify the timing expected for production. Refer to the DBS Release Notes section 6, BWKS-3069 and the DBS Config Guide section 6.5.7.3.

### Enhanced Call Logs

Enhanced Call Logs (ECL) is end of life on the DBS after DBS 2020.08. The ECL database must be migrated to a Network Database Server (NDS) for continued use, the migration is not automatic. Refer to the Enhanced Call Logs Solution Guide and the NDS Enhanced Call Logs Feature Description for more information. Refer to the Network Database Server Configuration Guide for setting up an NDS and the ECL Migration From DBS to NDS Feature Description for the migration procedure. The migration must be performed before the upgrade.

### Collaborate Servers

The End of Maintenance (EoM) for the Messaging Server (UMS), Sharing Server (USS), Video Server (UVS), WebRTC Server (WRS), Business Communicator Client (BTBC), and Connect Client was January 31, 2022. The latest RI version available for the UMS is 22.0 and for the USS, UVS, and WRS the latest available is 2022.01.

The AS at 24.0 is compatible with a UMS at 21.sp1. Upgrading the UMS to 22.0 is not recommended. The UMS at 22.0 uses MariaDB instead of Oracle TimesTen necessitating additional steps to upgrade, has a separate Method of Procedure (MOP), and requires an additional node for redundancy. See the UMS Upgrade MOP and the Field Notification about MariaDB 10.1 End of Life .

It is recommended to replace the Collaborate services with WebEx for BroadWorks. Refer to the WebEx for BroadWorks Solutions Guide .

### Element Management System and Virtual Licensing Server

The Element Management System (EMS) and Virtual Licensing Server (VLS) are End of Life (EoL) as of Q2 2018 and their functionality has been replaced by the Network Function Manager (NFM). There is no upgrade path to the NFM or decommission of any EMS or VLS nodes.

### Network Function Manager

The NFM requires a two-stage upgrade from 21.sp1. It can upgrade to 2019.05, then on to 2022.08+. If Network Monitoring is deployed, there is an additional step required; from 21.sp1 upgrade to 2019.05, then to 2020.11 and then on to 2022.08+.

### Upgrading to 23.0 on Linux 6

If upgrading an Application Server to 23.0 on Linux 6 several patches must not be applied or the upgrade fails at patching "Rel_22.0/v1.450/ ". Do not apply these patches to the AS when upgrading to 23.0: AP.platform.23.0.1075.ap38541, AP.as.23.0.1075.ap385380, AP.as.23.0.1075.ap385413, and AP.as.23.0.1075.ap385453.

## Review Documentation

Release notes for the target release and any releases between the target and source release must be reviewed. If the target release is 24.0 the release notes for 22.0, 23.0 and 24.0 must be reviewed.

22.0 Release Notes 23.0 Release Notes

24.0 Release Notes Upgrade Method of Procedure Refer to the Software Compatibility Matrix for the official supported upgrade paths. There are several features that are EoM starting with Release 22.0. These are documented in the End Of Maintenance Product Removal Feature Description . These features are no longer available after the upgrade.

## License Requirements

A new license is required for the target release. To request a license open a ticket . For upgrades to 24.0, request that the PS and XSP licenses be converted to ADP licenses; the ADP does not accept a PS or XSP license.

### Alignment of RI to Major Release

2017.xx = R22 2018.xx = R22 2019.01 to 2020.06 = R23 2020.07 to 2022.07 = R24

## Best Practices

### Request Support

Direct upgrade support is available from the BroadWorks Upgrade Team.

The BroadWorks Upgrade Team provides support for upgrades to a current 'in support' release, for lab and production, once per year under the Maintenance and Support contract. The Upgrade Team can provide support with preparing for an upgrade and real-time support during the upgrade, which can include Cisco engineers performing the upgrade remotely. The Upgrade Team scope is limited to the upgrade activity only and does not provide direct support for issues that need to be resolved before the upgrade such as hardware or Operating System updates, or debugging pre-existing issues and does not provide comprehensive post-upgrade testing beyond general server health checks.

Contact the BroadWorks Upgrade Team, through the account team, or email at bwupgrade@cisco.com . Availability for real-time upgrade support is not available on short notice, schedule in advance.

### Notify BroadWorks Support Before an Upgrade

If performing an upgrade without the support of the Upgrade Team it is recommended to notify BroadWorks Support a few days in advance with a severity 4 (s4) ticket. If an issue arises during the maintenance, raise the severity of the ticket to s1, open a new s1 ticket or call the support line to speak to an engineer.

### Test Plans

A test plan is essential to ensure a smooth upgrade. A test plan must be developed and tested in a lab before a production upgrade. Run the test plan on the system before the upgrade and record the results. This ensures that the system is healthy, verifies that all test users and accounts are correctly configured and functioning, provides an opportunity to catch potential gaps in the test plan and provides a time estimate on how long testing is expected to take.

Each server must be tested after it has been upgraded to ensure that it is functioning as expected before moving on to upgrade to the next server in the sequence.

### Patching

Patch the source release to 6 months or less of the latest patch level before upgrading.

### Pre-Install Check Script

The pre-install check script must be run on every server, lab and production and any warnings or failures addressed before the upgrade.

### Lab Upgrade

It is always recommended to test the upgrade, the test plan, and the target release with any third-party tools, applications or clients in a lab environment that replicates the production environment. The lab can be scaled down but ought to have the same server types, software version, OS version, access devices, Session Border Control (SBC), and so on. Treat the lab upgrade as a dry run for the production environment upgrade. Use the latest target release patch level when upgrading the lab. Keep the time between the lab and production upgrade to 3 months or less.

### Scheduling and Upgrade Sequence

Upgrades are expected to take place over multiple maintenance windows spread across several nights and are performed in the Installation and Upgrade Order as documented in section 4.2 of the Software Management Guide . Always perform upgrades during a predetermined maintenance window (during a non-busy hour). Always upgrade one node at a time, and ensure that one or more than one node of a cluster is down at any given time. The length of the maintenance window (MW), the number of servers to upgrade, the server type and how long testing is expected to take determine how many maintenance windows are required. All servers in a cluster must be upgraded in the same MW. Leave time available in the scheduled MW for troubleshooting and/or rollback if required.

### Upgrade Failures

If an issue is discovered during the post-upgrade testing or an upgrade fails, gather logs before reverting to the source release or restoring the server. Backup the entire logs directory to ensure all potentially helpful logs are kept. Immediately open a ticket and call Support for assistance while still in the MW.

### Revision History

1.0

18-Oct-2023

Initial Release

### Contributed by Cisco Engineers

Mike Dibert

Cisco Technical Lead

### This Document Applies to These Products

- BroadWorks

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 18-Oct-2023 | Initial Release |