---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-118318-config-cucm--9882b3c216
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/118318-config-cucm-00.html
retrieved_at: 2026-08-16T23:37:11.209178+00:00
---

Upgrade CUCM/CUC/CUPS with Prime Collaboration Deployment

# Upgrade CUCM/CUC/CUPS with Prime Collaboration Deployment

### Download Options

Updated: January 29, 2015

Document ID: 118318

Contents

## Contents

## Introduction

This document describes how to upgrade Cisco Unified Communications Manager/Cisco Unity Connection/Cisco Unified Presence Server (CUCM/CUC/CUPS) with Prime Collaboration Deployment (PCD).

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on these software and hardware versions:

- CUCM Release 10.0

- PCD Release 10.5

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact.

## Background Information

Cisco PCD is an application designed to assist in the management of Unified Communications applications. It allows the user to perform tasks such as migration of older software versions of clusters to new virtual machines, fresh installs, and upgrades on current clusters.In summary automates upgrade and migration task.

This document is focused on the upgrade task on PCD Release 10.5.

### Supported Releases for the Upgrade Task on PCD Version 10.5

These include releases for the upgrade task on the Upgrade Application Server or Install COP files:

- Cisco Unified CM Releases Supported: 8.6(1-2), 9.0.(1), 9.1(1), 9.1(2), 10.x

- Cisco Unified Presence (CUP) Releases Supported: 8.6(3), 8.6(4), 8.6(5)

- Cisco Unified CM - IM and Presence Releases Supported: 9.0(1), 9.1(1), 10.x

- Cisco Unified Contact Center Express Releases Supported: 9.0(2), 10.x

- From 8.6(x) to 8.6(x)

- From 8.6(x) to 9.x

- From 9.x to 9.x

- From 10.0(1) to 10.x

## Configure

Complete these steps in order to configure your server:

- From a Linux shell, enter sftp adminsftp@<Cisco Prime Collaboration Deployment server> and then provide the password (this is the same in both the CLI and the GUI).

The Discover Cluster wizard appears.

Note : For a cluster that has both CUCM and IM and Presence (IM/P) nodes, enter the CUCM publisher.

In the process of discovery, a COP file (ciscocm.ucmap_platformconfig.cop) is installed automatically on the active partition of all nodes in the cluster. This COP file is used strictly for the cluster discovery process and does not otherwise impact the call manager.

The cluster appears on the Clusters page, and shows the Cluster Name, Product and Version, and a Cluster Type of "Discovered". Discovery Status should list "Successful".

The Add Upgrade Task wizard displays.

Note : The Next button is disabled if no valid upgrade files are selected.

Note : The "Automatically switch to new version after successful upgrade" option is not available on clusters which contain IM and Presence or Unity Connection nodes.

- [Optional] Specify the sequence of steps to complete the task. If this is not specified, it uses the default option.

Note : The Next button remains enabled, which allows the user to click to be informed of any misconfiguration.

## Verify

Use this section in order to confirm that your configuration works properly.

- Click Monitoring on the main menu in order to view the Monitoring page.

The View Task Log appears.

## Troubleshoot

This section provides information you can use in order to troubleshoot your configuration.

The success or failure of each step in the upgrade task depends on the PCD server being able to receive a response from every server in the cluster in the upgrade process. In case the upgrade fails, verify the COP file installation status directly on the Unified Communications node. A further step ahead is to collect Install and upgrade logs and check the reason for failure.

The install logs can also be collected from the CLI with the file get install /* command.

Additionally, you can obtain PCD Main Application logs with the file get activelog tomcat/logs/ucmap/log4j/* command.

### Contributed by Cisco Engineers

Mohammed Noorulla Khan

Cisco TAC Engineer.

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

- Unified Communications Manager IM & Presence Service