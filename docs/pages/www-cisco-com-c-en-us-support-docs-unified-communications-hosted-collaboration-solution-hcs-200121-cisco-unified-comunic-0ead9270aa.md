---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-hosted-collaboration-solution-hcs-200121-cisco-unified-comunic-0ead9270aa
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/hosted-collaboration-solution-hcs/200121-Cisco-Unified-Comunication-Domain-Manage.html
retrieved_at: 2026-09-01T14:58:39.145534+00:00
---

Cisco Unified Communication Domain Manager (CUCDM) Platform Password Recovery

# Cisco Unified Communication Domain Manager (CUCDM) Platform Password Recovery

### Download Options

Updated: October 19, 2016

Document ID: 200121

Contents

## Contents

## Introduction

This document describes how to reset the Cisco UCDM platform password if you forget the password and you are not able to access the CLI via platform user.

## Password Recovery Procedure

This section describes the Cisco UDCM Password Recovery Procedure.

Note : This procedure is applicable only to CUCDM 10.1.x and 10.6  GRUB version 1.99-21ubuntu3.17 and 3.18.

- Disable connections, if possible, by way of disabling network. This ensures that transactions are not lost.

- Log in to VMWare and choose the Cisco UCDM Virtual Machine (VM).

- Right-click the VM and choose Edit Settings .

- Open the Cisco UCDM display (Launch Virtual Machine Console).

- Click the reboot button (Restart Guest).

- The VM enters in BIOS and exits from the BIOS without making any changes. (The next step needs to be performed quickly before the system boot).

- Press Ctrl-X in order to boot the system.

- Type exit and then power off and on the VM.

You can now log in as platform user with the password set in step number 13.

### Contributed by Cisco Engineers

Andrea Cingolani

Cisco TAC Engineer

### This Document Applies to These Products

- Hosted Collaboration Solution (HCS)