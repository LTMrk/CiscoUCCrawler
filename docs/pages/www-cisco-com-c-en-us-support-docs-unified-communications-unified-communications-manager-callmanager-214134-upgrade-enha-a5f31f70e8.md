---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-214134-upgrade-enha-a5f31f70e8
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/214134-upgrade-enhancements-in-cisco-unified-c.html
retrieved_at: 2026-08-21T01:42:45.410157+00:00
---

Upgrade Enhancements in Cisco Unified Communications Manager(CUCM) 12.5

# Upgrade Enhancements in Cisco Unified Communications Manager(CUCM) 12.5

### Download Options

Updated: November 14, 2022

Document ID: 214134

Contents

## Contents

## Introduction

This document describes the new features of Cisco Unified Communications Manager (CUCM) 12.5 which helps simplify tasks like Upgrade/Restart/Switch Version of a Single Server or Multi node Cluster.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communications Manager 12.5

- IM and Presence Server 12.5

### Components Used

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Pervious to CUCM 12.5, When you need to install or upgrade , the procedure required you to log into each individual node to perform the required task.

The new enhancement in CUCM 12.5 allows you to perform that procedure from one web interface, the primary (publisher) node of the cluster. This allows you to install, upgrade, and switch versions for the cluster using a more controlled and structured method which saves time and is more efficient.

### Single Server Upgrade

- The software configuration setting does not persist. Admin needs to enter the values every time an upgrade needs to be done.

- Admin needs to enter the configuration at each node.

- After the download, if the upgrade fails then admin may fix the issue and have to start again from download step for an upgrade.

### Cluster Upgrade

- Nodes have to be upgraded individually and do switch version in a specific order.

- The Admin needs to remember and manually upgrade nodes in that order to achieve a successful upgrade. Admin has to wait for the upgrade of one node to finish before he starts the next node.

### Reboot Cluster/Switch Version

There is no any option prior to 12.5 to control and manage the reboot/switch version of the entire cluster. Admin has to go on the CLI of each server which starts with Pub and perform the operation.

CUCM 12.5 has enhancements to these features which is very helpful for an administrator.

## Configure

### Step 1. Single Server upgrade Enhancements.

#### GUI Enhancements

These are the enhancements done on the OS Admin page when Install/Upgrade for Single Server is selected.

Option 1. Use Download Credential from Publisher.

This option is available on Subscribers and selected by default. Through this option, the upgrade file from the Publisher can be used.

Option 2. Use the Local File System.

This option enables to use the previously downloaded file which is present on the local directory of the server.

Option 3. Persistent Values are Pre-populated.

The Secure FTP (SFTP) server details are persistent and prepopulated. In case the admin wants to use the same details as the previous one,  they need not to be re-entered.

Option 4. Continue with System Upgrade and Switch version option before the image file is downloaded.

In earlier versions of CUCM and IM&P, the option to select a switch version is given once the image is downloaded. In this case, the admin has to wait for the download to finish and then select further action to start the upgrade.

Using this feature if the admin does not want to verify the MD5 value of the ISO, they can select to continue the installation post download of iso and it won’t require any further intervention.

Option 4. In case of an Upgrade failure, the image file does no to be downloaded again.

If the upgrade fails due to any reasons, Local File can be used and download of the iso file again can be avoided.

#### CLI Enhancements

There have been enhancements in the CLI command for Upgrade of Single Server to support the above features.

The command to start the upgrade is still the same(utils system upgrade initiate) but there are new options added.

From Publisher CLI:

```
admin:utils system upgrade initiate

Warning: Do not close this window without first cancelling the upgrade.

Warning: Before upgrading the cluster Cisco recommends installing the latest Upgrade Readiness COP file. Refer to the Upgrade Guide on cisco.com for details.

Source:

1) Remote Filesystem via SFTP

2) Remote Filesystem via FTP

3) Local DVD/CD

4) Local Image <UCSInstall_UCOS_12.5.1.10000-19.sgn.iso>

q) quit

Please select an option (1 - 4 or "q" ):

“Local Image< image >” introduced in the list of the source  that allows admin to select a local image that is already downloaded to UCM and use that image to upgrade the UCM
```

From a Subscriber CLI:

```
admin:utils system upgrade initiate

Warning: Do not close this window without first cancelling the upgrade.
Warning: Before upgrading the cluster Cisco recommends installing the latest Upgrade Readiness COP file. Refer to the Upgrade Guide on cisco.com for details.

Use download credentials from Publisher (yes/no) [yes]: no
Source:

1) Remote Filesystem via SFTP
2) Remote Filesystem via FTP
3) Local DVD/CD
4) Local Image <None>
q) quit

Please select an option (1 - 4 or "q" ):

utils system upgrade initiate for CUCM Subcrobers andIM&P Pub/Sub nodes has been modified and the option is  “Use download credentials from Publisher (yes/no) [yes]”
```

When you click on the option, the upgrade file is selected through the Publisher configurations. Checks are done on the image to see if its valid before the upgrade.

If the publisher provides a location that does not have any valid image then it \exits the upgrade prompts

### Step 2. Centralized Cluster Upgrade.

This is a new feature introduced in CUCM version 12.5 to manage the upgrade of Cluster. The Cluster Upgrade option is available on Publisher and whole cluster upgrade can be started through OS Admin page or CLI. Cluster Upgrade includes IM&Presence Servers as they are part of the cluster.

Note :Valid Tomcat certificates must exist within CUCM and IM&P Publisher if cluster wide upgrade involves CUCM and IM&P nodes.

#### GUI Enhancements

In Software Upgrades, a new option Install/Upgrade Cluster is introduced for this.

If Cluster contains IMP Servers as well then whether to Upgrade IMP Servers or not can be chosen.

Once the Upgrade starts the status can be monitored through the GUI or CLI interface.The parameter Historical Time to Complete shows the amount of time it took for the particular step when last time upgrade was successfully done. This can be matched with the Time Elapsed option to see whether the upgrade is going as expected.

If it is the first time System is being upgraded then Historical Values have the Standard Values defined by the Developers which is taken from local test results.

#### CLI Enhancements

A new CLI has been introduced on Publisher which would help to trigger and manage the Cluster Upgrade.

admin: utils system upgrade cluster {initiate/status/cancel}

The above  CLI command is available only on the CUCM publisher.

### Step 3. Centralized Cluster Switch-Version or Reboot.

This feature is present on CUCM Publisher Server only and can be managed through GUI interface only as there are no CLI commands for this.

Using this feature, the Switch Version and Upgrade of the whole cluster can be managed. The operation is performed in a batch of servers and Publisher that is always in the first batch. There should be some Server in each batch and batch skipping is not possible. The operation starts with Batch1 and then Batch2 and onwards. The current status of operation can be viewed from the Status menu.

### Step 4. Parallel Upgrades Of Cluster Nodes.

Using the Cluster Upgrade option, the upgrade for all nodes is started at the same time, and Admin does not need to wait for the Publisher upgrade to get finish before he can start the next server. Even though the Upgrade for all Servers is started simultaneously, in the backend CUCM Subscriber waits for the CUCM Publisher database installation to get finish and IMP Subscriber waits for the CUCM Publisher and IMP Publisher installation to get finish.

Note : If cluster-wide upgrade is set to auto-switch as Yes. All the selected nodes should complete the upgrade then switch version is performed, Incase upgrade fails, switch version isn't performed.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

Before the upgrade is started for a Single Server or Cluster ensure that there is no upgrade or DRS task which runs already.

The upgrade can fail at different stages and to correct that related checks needs to be done.

### Revision History

1.0

16-Sep-2021

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 16-Sep-2021 | Initial Release |