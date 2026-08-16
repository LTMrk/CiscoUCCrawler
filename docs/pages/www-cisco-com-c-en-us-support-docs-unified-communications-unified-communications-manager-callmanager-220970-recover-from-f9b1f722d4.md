---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-220970-recover-from-f9b1f722d4
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/220970-recover-from-ungraceful-shutdowns-on-vos.html
retrieved_at: 2026-08-16T18:00:22.182182+00:00
---

Recover from Ungraceful Shutdowns on VOS

# Recover from Ungraceful Shutdowns on VOS

### Download Options

Updated: July 24, 2025

Document ID: 220970

Contents

## Contents

## Introduction

This document describes how to troubleshoot and resolve ungraceful shutdown issues on Voice Operating System (VOS) based systems.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of one or more of these topics:

- Cisco Unified Communications Manager (CUCM)

- Cisco Unified Instant Messaging & Presence (IM&P)

- Cisco Emergency Responder (CER)

- Cisco Unity Connection (CUC)

### Components Used

The information in this document is based on these software and hardware versions:

- CUCM 12.5 or higher

- IM&P 12.5 or higher

- CER 12.5 or higher

- CUC 12.5 or higher

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## What is an Ungraceful Shutdown

An ungraceful shutdown refers to the sudden or abrupt termination of VOS without performing the proper shutdown procedures. It typically occurs when the system is forced to stop or power off unexpectedly, without allowing the necessary processes and services to shut down gracefully.

When a ungraceful shutdown has occurred, a warning message is displayed on the servers administration website.

Ungraceful Shutdown Web Interface Warning

This warning also displays if you log in via SSH or VMWare Console.

Ungraceful Shutdown CLI

Common causes for ungraceful shutdowns include:

- Power outages

- Hardware failures

- Improper Virtual Machine shutdown, restart or halt procedures

Warning : Ungraceful shutdowns can result in service interruptions, data loss, and system instability.

### Verifying a Ungraceful Shutdown Event

To confirm that a ungraceful shut down occurred, log into the CLI and execute file view install system-history.log .

Review the output of the system-history.log. If two boot events are consecutive without a proceeding shutdown or restart event, then a ungraceful shutdown has occurred.

admin:file view install system-history.log

06/20/2023 10:22:48 | root: Shutdown 14.0.1.13900-155 Start

06/20/2023 10:24:35 | root: Boot 14.0.1.13900-155 Start = OK, prior Shutdown

07/10/2023 10:29:08 | root: Restart 14.0.1.13900-155 Start

07/10/2023 10:30:05 | root: Boot 14.0.1.13900-155 Start = OK, prior Restart

07/15/2023 11:14:29 | root: Boot 14.0.1.13900-155 Start = Ungraceful Shutdown, no prior Restart or Shutdown statement

## Validate System Health

It is important to identify the underlying cause of an ungraceful shutdown in order to take appropriate measures to prevent its recurrence and minimize the impact on the system and its users.

### Verify Power

Check if the VOS server has a stable power supply and is properly connected to power sources. Ensure that power cables are securely connected and not damaged.

### Verify Hardware

Access the servers Integrated Management Controller (IMC) or Integrated Dell Remote Access Controller (iDRAC) to review the server logs. Review the server logs for any hardware errors or warnings that indicate issues with hardware components.

Many servers offer diagnostic tools that can be accessed during the boot process. These tools can perform comprehensive hardware tests, including memory tests, CPU tests, and disk checks. Use these diagnostic tools to identify any hardware issues or failures.

Note : It is important to consult server manufacturers documentation and support resources for specific instructions on how to verify and troubleshoot hardware issues.

### Verify Shutdown Procedure

Forcing the VOS server to shut down using methods such as pressing the power button or unplugging the server without allowing the operating system to perform the necessary shutdown processes can lead to an ungraceful shutdown.

### VOS Stability Checks

To verify the stability of the VOS system, several utilities can be utilized. These utilities provide valuable information about the services, diagnostics, network, database integrity, and time synchronization.

Utility

Description

utils service list

This VOS command is used to check the status and health of the services running on the server. Reviewing the service list ensures that all essential services are running as expected. Any services that are stopped or experiencing issues can be an indication of a potential stability problems within the system.

utils diagnose test

This VOS command initiates a diagnostic test that performs various checks on system components, configurations, and services. It helps identify any potential issues or misconfiguration that could impact system stability. The diagnostic output provides administrators with diagnostic information and recommendations for resolving any identified problems.

show network cluster

This VOS command verifies the network connectivity between cluster nodes and displays the status of each cluster member. Administrators can examine the output data to ensure that the network is properly configured, all cluster members are online, and communication between them is stable. Network issues or inconsistencies can significantly impact the stability and reliability of the VOS system.

show tech dbintegrity

This VOS command generates a technical support file that includes information about the database integrity. It verifies the replication status, counters, and other crucial details related to the database. Checking the database integrity is vital for ensuring data consistency and system stability. Any issues detected by this command can help with the identification and resolution of potential database problems.

utils ntp status

This VOS command displays the Network Time Protocol (NTP) synchronization status on the server. It shows the NTP source being used, the synchronization status, and the time offset between the server and the configured NTP source. Proper time synchronization is essential for various system functions. Verifying the NTP status ensure that the VOS systems time is accurate and minimizes potential issues related to timing.

Recovery ISO File Check

This ISO utility is used to examine and verify the integrity of the file system on the VOS server. Perform the file check to confirm that the file system is healthy and free of any corruption or errors. The file check does not cover the integrity of the individual files which could contain corrupted elements

For information about downloading and using the recovery ISO, please refer to the Obtain and Run Recovery Software on the CUCM VM guide.

## Mitigation

To mitigate the impact of ungraceful shutdowns, it is important to implement preventive measures such as regular backups, monitoring, and redundancy strategies.

If proper shutdown procedures are not followed during maintenance activities, system upgrades, virtual machine restart or virtual machine shutdown, it can result in an ungraceful shutdown.

## Remediation

Recommended remediation for an ungraceful shutdown at the VOS level is to rebuild the affected nodes and restore from a good backup. This ensures file integrity of the system and restores the system to a stable state.

Refer to the links provided for Instructions on how to restore from a backup.

There is another option available in situations were rebuilding is not possible or unfavorable. The VOS command utils ungraceful warn disable is used to suppress the Web Administration and Console ungraceful shutdown warnings.

Command

Description

utils ungraceful warn disable

This vos command can be used to disable the Web Administration and Console warning message that appears when an ungraceful shutdown is detected. This command does not  execute any system checks for file corruption.

This is not the recommended solution as this only suppresses the warning and does not address the underlying cause of the ungraceful shutdown. It is crucial to address the root cause and ensure the stability and integrity of the VOS system

Note : If your server is unable to execute the utils ungraceful warn disable command please refer to Cisco bug ID CSCvy68211 as a COP file is needed to enable the command.

### Revision History

2.0

24-Jul-2025

Updated Formatting. Recertification

1.0

27-Sep-2023

Initial Release

| Utility | Description |
|---|---|
| utils service list | This VOS command is used to check the status and health of the services running on the server. Reviewing the service list ensures that all essential services are running as expected. Any services that are stopped or experiencing issues can be an indication of a potential stability problems within the system. |
| utils diagnose test | This VOS command initiates a diagnostic test that performs various checks on system components, configurations, and services. It helps identify any potential issues or misconfiguration that could impact system stability. The diagnostic output provides administrators with diagnostic information and recommendations for resolving any identified problems. |
| show network cluster | This VOS command verifies the network connectivity between cluster nodes and displays the status of each cluster member. Administrators can examine the output data to ensure that the network is properly configured, all cluster members are online, and communication between them is stable. Network issues or inconsistencies can significantly impact the stability and reliability of the VOS system. |
| show tech dbintegrity | This VOS command generates a technical support file that includes information about the database integrity. It verifies the replication status, counters, and other crucial details related to the database. Checking the database integrity is vital for ensuring data consistency and system stability. Any issues detected by this command can help with the identification and resolution of potential database problems. |
| utils ntp status | This VOS command displays the Network Time Protocol (NTP) synchronization status on the server. It shows the NTP source being used, the synchronization status, and the time offset between the server and the configured NTP source. Proper time synchronization is essential for various system functions. Verifying the NTP status ensure that the VOS systems time is accurate and minimizes potential issues related to timing. |
| Recovery ISO File Check | This ISO utility is used to examine and verify the integrity of the file system on the VOS server. Perform the file check to confirm that the file system is healthy and free of any corruption or errors. The file check does not cover the integrity of the individual files which could contain corrupted elements For information about downloading and using the recovery ISO, please refer to the Obtain and Run Recovery Software on the CUCM VM guide. |

| Command | Description |
|---|---|
| utils ungraceful warn disable | This vos command can be used to disable the Web Administration and Console warning message that appears when an ungraceful shutdown is detected. This command does not  execute any system checks for file corruption. |

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 24-Jul-2025 | Updated Formatting. Recertification |
| 1.0 | 27-Sep-2023 | Initial Release |