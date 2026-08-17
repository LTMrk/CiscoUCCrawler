---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unity-connection-117555-probsol-cucorcucm-00-html-d5b0162afa
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/117555-probsol-cucorcucm-00.html
retrieved_at: 2026-08-17T02:23:57.560338+00:00
---

CUC/CUCM vCPU Mismatch can Cause Upgrade Failure

# CUC/CUCM vCPU Mismatch can Cause Upgrade Failure

### Download Options

Updated: January 20, 2015

Document ID: 117555

Contents

## Contents

## Introduction

This document describes the procedure to correct the Unsupported Hardware error issue.

Upgrades on Cisco Unity Connection (CUC) / Cisco Unified Communications Manager (CUCM) fail with an ' Unsupported Hardware ' error. This is because of the vCPU (Virtual CPU) mismatch seen on the Virtual Machine(VM) properties (vSphere Client - This is the value that is set correctly) and seen on CUC / CUCM via the CLI.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unity Connection

- Cisco Unified Communications Manager

- Virtual Machines

### Components Used

The information in this document is based on these software versions:

- Cisco Unity Connection Release 8.X or later

- Cisco Unified Communications Manager Release 8.X or later

The information in this document is created from the devices in a specific lab environment. All of the devices used in this document is started with a clear (default) configuration. If the network is live, make sure that you understand the potential impact of any command.

## Problem

Upgrade fails with this error:

```
05/31/2013 21:40:18 upgrade_manager.sh|File:/common/download/8.6.2.23900-10/upgrade_manager. sh:1048, Function: validate_upgrade_allowed(), This server is not supported for use with the version of "connection" that you are trying to install.
```

The actual value for vCPU while you create the VM is shown here:

Here the VM is created with one vCPU. However when you log into the CUC/CUCM, the CLI displays a different value for vCPU, and show hardware also displays 8 vCPU .

## Resolution

By default, Hot Plug (add vCPU) for VMs is in the disabled state. Verify if this is in an enabled state. If you enable this feature, it allows the VMs to access more resources if required.

In order to disable the Hot Plug (add vCPU), shut down the VM. This parameter cannot be modified while the VM is in execution.

- Open the VM's properties window, and choose Options > Memory/CPU Hotplug in the Advanced section.

For older versions of ESXi host, complete these steps.

- Open the VM's properties window, and choose Options > General in the Advanced section.

- On the right-hand side of the window, click Configuration Parameters .

### Contributed by Cisco Engineers

Anirudh Mavilakandy

Cisco TAC Engineer.

### This Document Applies to These Products

- Unity Connection