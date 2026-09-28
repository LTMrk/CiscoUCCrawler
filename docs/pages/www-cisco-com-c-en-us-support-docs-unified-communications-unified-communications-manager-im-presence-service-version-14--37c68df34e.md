---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-im-presence-service-version-14--37c68df34e
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-im-presence-service-version-14/220608-validate-im-and-presence-after-ungracefu.html
retrieved_at: 2026-08-16T23:40:17.257296+00:00
---

Validate IM and Presence after Ungraceful Shutdown

# Validate IM and Presence after Ungraceful Shutdown

### Download Options

Updated: July 21, 2023

Document ID: 220608

Contents

## Contents

## Introduction

This document describes the validation process to perform when ungraceful shutdown warnings are experienced on Cisco IM and Presence (IM&P)

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of Cisco IM and Presence (IM&P).

### Components Used

The information in this document is based on Cisco IM and Presence 14.0.1 SU2a

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## What is an Ungraceful Shutdown?

Ungraceful Shutdowns occur when the IM&P server is shutdown or restarted in a unsupported manner. This includes:

- Power outages

- VMware Power Off

- VMware Reset

- VMware Hard Stop

The proper method of to shutdown or restart IM&P is to execute the utils system shutdown or utils system restart command from the CLI of IM&P.

For information about the listed utils commands please refer to Cisco Command Line Interface Reference Guide.

Note : For information on rebooting a IM&P Cluster please refer to this Video .

## Confirm Ungraceful Shutdown Occurrence

When a ungraceful shutdown has occurred a warning message is display on the Cisco IM and Presence Administration admin website.

IM&P Administration Warning

This warning also displays if you log in via SSH or VMWare Console.

CLI Ungraceful Shutdown

To confirm that a ungraceful shut down occurred, log into the IM&P CLI and execute file view install system-history.log .

Review the output of the system-history.log. If you see two Boot events consecutively without a proceeding shutdown or restart event then a ungraceful shutdown has occurred.

admin:file view install system-history.log

04/06/2023 13:04:36 | root: Install 14.0.1.12901-1 Success

04/06/2023 13:42:21 | root: Shutdown 14.0.1.12901-1 Start

04/07/2023 04:51:49 | root: Boot 14.0.1.12901-1 Start

--- Example of a Good System Restart ---

07/20/2023 10:22:48 | root: Restart 14.0.1.12901-1 Start

07/20/2023 10:24:35 | root: Boot 14.0.1.12901-1 Start

07/20/2023 10:50:50 | root: Restart 14.0.1.12901-1 Start

--- Example of a Ungraceful Shutdown ---

07/20/2023 10:52:43 | root: Boot 14.0.1.12901-1 Start

07/20/2023 11:06:50 | root: Boot 14.0.1.12901-1 Start

## Validate IM&P System Health

To determine the integrity of the effected server perform the listed steps.

Note : Cisco recommends these steps are performed during a outage window

- Start by downloading the recovery ISO for your IM&P version and performing a file system check .

Note : The recovery ISO can be found at software.cisco.com The recovery ISO Is listed under the CUCM version that is compatible with your IM&P.

- utils service list

utils imdb_replication status

utils diagnose test

show network cluster

- show tech dbintegrity

- utils ntp status

- utils ha status

utils dbreplication status

utils dbreplication runtimestate

Warning : During ungraceful shutdown events it is possible that the server can be corrupted, resulting in the server needing to be rebuilt. This is why the ungraceful shutdown warning is displayed anytime a node is unexpectedly rebooted or shutdown.

## Disable the Ungraceful Shutdown Warning

Once all the system health checks have been performed proceed with disabling the ungraceful shutdown warning by executing the listed command on the effected node.

- utils ungraceful warn disable

Note : If your IM&P is running a version less then 12.5.1 SU6 and 14.0.1 SU2 please refer to Cisco bug ID CSCvy68211 as a COP file is needed to enable the utils ungraceful warn disable command.

### Revision History

1.0

21-Jul-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 21-Jul-2023 | Initial Release |