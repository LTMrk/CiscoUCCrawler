---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-216747-troubleshoot-ecb4f1d0ac
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/216747-troubleshoot-zombie-defunct-processes-in.html
retrieved_at: 2026-08-16T18:57:44.292279+00:00
---

Troubleshoot Zombie/Defunct Processes in UC Servers

# Troubleshoot Zombie/Defunct Processes in UC Servers

### Download Options

Updated: February 10, 2021

Document ID: 216747

Contents

## Contents

## Introduction

This document describes how to work with zombie processes seen on CUCM, IMnP, and other Cisco UC products when logged in using Admin CLI.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of using Admin CLI of the UC servers:

- Cisco Unified Communications Manager (CUCM)

- Cisco Unified Instant Messaging and Presence Server (IMnP)

- Cisco Unity Connection Server (CUC)

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

The Unified Communications servers are essentially Linux OS based applications. When a process dies on Linux, it is not all removed from memory immediately, its process descriptor (PID) stays in memory which only takes a tiny amount of memory. This process becomes a defunct process and the process's parent is notified that its child process has died. The parent process is then supposed to read the dead process's exit status and completely remove it from the memory. Once this is done using the wait() system call, the zombie process is eliminated from the process table. This is known as reaping the zombie process. This generally happens very quickly, so you will not see zombie processes accumulating on your system.

However, sometimes the parent processes do not do the wait() signal call, and the child process will stick in the memory until cleaned up. In other words, a zombie process is a process whose execution is completed but it still has an entry in the process table, as the parent process still needs to read its child's exit status.

## Check Zombies using UCOS Admin CLI

From the CLI, the presence of zombies can be checked using the command show process load .

## Troubleshoot/Clear the Zombies Manually

Apart from the tiny memory used to hold the PID as mentioned previously, Zombie processes do not use any system resources, but they do retain their process ID. In UC servers, the memory provided to the system is large so the possibility of the system to run out of PIDs for other processes due to the presence of Zombies is very less.

So, the zombies can be left on the system, where they are automatically cleared at the next system reboot .

However, if there is a requirement to clear out the zombies in the system, you can follow a certain line of action

### Restart the Appropriate Service

It is required to figure out the concerned process and hence the service which leaks the child process.

- Copy the outputs in a text editor and search the file for the text 'defunct'.

- Note down the Process IDs (pid) and Parent Process IDs (ppid) for those defunct processes.

- Track down the ppid in the document to find the associated process.

Example 1

CUCM: When I search the file for the text 'defunct', I see that there's a PID 22908 that is defunct.

The ppid for that PID is 29815. On tracking 29815 in the document, I see that the process is related to AMC service.

Solution- Restart AMC(Alert Manager and Collector Service) on this node clears the Zombie.

Example 2

CUCM: When the file for the text defunct is searched, I see that there's a PID 10025 that is defunct.

The ppid for that PID is 26732. On tracking 26732 in the document, you see that the process is related to the Trace Collection Service.

Solution -Restart the Trace Collection Service on this node clears the Zombie.

Example 3

CUCM: When the file for the text defunct is searched, you see that there's a PID 23959 that is defunct.

The ppid for that PID is 26764. On tracking 26764 in the document, I see that the process is related to the CDR Repository service(cdrrep)

Solution - Restart the CDR Repository Service clears this Zombie.

Example 4

CUC: When the file for the text defunct is searched, you see that there's are three PIDs 325, 370, 387 that are defunct.

The ppid for all those PIDs is 7827. On tracking 7827 in the document, you see that the process is related to the Connection File Syncer service.

Solution - Restart the Connection File Syncer service clears the Zombies.

Example 5

IMnP: When the file for the text defunct is searched, you see that there's a PID 1806 that is defunct.

The ppid for that PID is 1775. On tracking 1775 in the document, you see that the process is an SFTP connection to another IMnP node in the same cluster.

Solution -  In IMnP, SFTP owned Defunct SSH processes might be seen. They have been found to be cosmetic and can be removed by a reboot of the server.

### Reboot the Server

A reboot of the concerned server clears all the stale entries in the process-table and consequentially clears the zombies in the system .

### Kill the Parent Process

From Linux, you can’t kill zombie processes the way normal processes are killed with the SIGKILL signal — zombie processes are already dead. However, you can kill the parent process. The command used in that scenario are:

kill -9 <ppid>

Contact TAC for carrying out this workaround. Ensure care while killing the parent process to ensure that no critical service is abruptly brought down.

## Verify

Once the zombies have been cleared, use the same command show process load to check the zombie count.

### Contributed by Cisco Engineers

Animesh Lochan

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

- Unified Communications Manager IM & Presence Service

- Unity Connection