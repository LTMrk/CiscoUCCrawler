---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-hosted-collaboration-solution-version-1061-212358-cisco-unifie-dfb536d050
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/hosted-collaboration-solution-version-1061/212358-cisco-unified-communication-domain-manag.html
retrieved_at: 2026-09-01T14:58:35.035936+00:00
---

Cisco Unified Communication Domain Manager 8.x (Cisco UCDM) usmcli Password Recovery

# Cisco Unified Communication Domain Manager 8.x (Cisco UCDM) usmcli Password Recovery

### Download Options

Updated: October 24, 2017

Document ID: 212358

Contents

## Contents

## Introduction

This document describes how to reset the Cisco UCDM 8.x platform usmcli password if you forgot the password and you are not able to access the Common Line Interface (CLI) via usmcli user.

## Problem

The usmcli user can't login to the CLI due a bad password.

### Components Used

The information in this document is based on CUCDM 8.1.6

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Solution

This section describes the Cisco UDCM 8.x Password Recovery Procedure.

Note : This procedure is applicable only to Cisco UCDM 8.x GRUB version 1.98-1ubuntu5

Step 1. Disable connections, if possible, to achieve that - disable the network. This ensures that transactions are not lost.

Step 2. Login to VMWare and choose the CUCDM Virtual Machine (VM).

Step 3. Right-click the VM and choose Edit Settings .

Step 4. Click the Options tab, choose Boot Options and set Power On Boot Delay for 7000ms (7 seconds) as example. Each time the virtual machine boots, it will wait additional 7 seconds. This setting allow us to read BIOS startup messages and press any additional keys if required.

Step 5. Open the Cisco UCDM display (Launch Virtual Machine Console).

Step 6. Click the reboot button (Restart Guest).

Step 7. During bootup process we see countdown timer.

Step 8. Before timer reach 0:00, press and keep SHIFT until grub screen appear.

Step 9. On GRUB screen press e for edit.

Step 10. Navigate to the end of line which starts with linux , and add to the end of the line init=/bin/bash as shown in this image.

Note : Sometimes init=/bin/bash can be splitted at the end of a line and result as below.

Step 11. Press Ctrl-X in order to boot the system and you see prompt like. Step 12. Enter mount -o remount,rw / once the system has booted.

Step 13. Enter passwd usmcli and enter a new desired password for usmcli account. Step 14. Type sync in order to force a file system sync. Step 15. Type exit . Step 16. Reboot VM.

Step 17. Login as usmcli user with the password set in step number 13.

### Revision History

1.0

22-Oct-2017

Initial Release

### Contributed by Cisco Engineers

Sebastian Danik

Cisco TAC Engineer

### This Document Applies to These Products

- Hosted Collaboration Solution (HCS)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 22-Oct-2017 | Initial Release |