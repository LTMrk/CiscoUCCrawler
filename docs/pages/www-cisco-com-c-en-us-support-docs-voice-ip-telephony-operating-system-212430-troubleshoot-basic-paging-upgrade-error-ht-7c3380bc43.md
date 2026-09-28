---
doc_id: www-cisco-com-c-en-us-support-docs-voice-ip-telephony-operating-system-212430-troubleshoot-basic-paging-upgrade-error-ht-7c3380bc43
source_url: https://www.cisco.com/c/en/us/support/docs/voice/ip-telephony-operating-system/212430-troubleshoot-basic-paging-upgrade-error.html
retrieved_at: 2026-08-21T12:40:24.337213+00:00
---

Troubleshoot Basic Paging Upgrade Error

# Troubleshoot Basic Paging Upgrade Error

### Download Options

Updated: October 29, 2017

Document ID: 212430

Contents

## Contents

## Introduction

This document describes the network card requirements of Cisco Basic Paging Server for an upgrade from version 11.5.1 to version 12.0.1.

Contributed by John Barreto, Cisco TAC Engineer.

## Problem

Upgrade of Cisco Basic Paging Server from version 11.5.1 to version 12.0.1 fails with error "A subcommand of the upgrade failed unexpectedly during pre-flight. Your system is unchanged."

## Troubleshooting

The upgrade fails with the error message as shown in the image here:

Use these steps to identify the issue:

Step 1. Collect the upgrade-preflight-checks logs after the upgrade failure

Note : The information in this link explains how to collect the Informacast logs: https://support.singlewire.com/s/article/InformaCast-Log-Tool

Step 2. Review the upgrade-preflight-checks.log for the error

From the logs we can see this error:

+(/etc/rc5.d/S98startupgrade:162): main(): . /usr/local/singlewire/platform/bin/bring-up-network.sh ++(/usr/local/singlewire/platform/bin/bring-up-network.sh:4): source(): /bin/cp /tmp/deb/etc/network/interfaces /etc/network/interfaces ++(/usr/local/singlewire/platform/bin/bring-up-network.sh:6): source(): /sbin/ifdown eth0 ifdown: interface eth0 not configured ++(/usr/local/singlewire/platform/bin/bring-up-network.sh:7): source(): /sbin/ifup eth0 eth0: ERROR while getting interface flags: No such device SIOCSIFADDR: No such device eth0: ERROR while getting interface flags: No such device SIOCSIFNETMASK: No such device SIOCADDRT: No such device

Step 3. Confirm the current network card enabled on the Cisco Basic Paging 11.5.1 server is VMXNET3

As Cisco Basic Paging server 12.0.1 does not support VMXNET3 network card, the upgrade fails at the upgrade-pre-flight check stage.

## Solution

Power down the Cisco Basic Paging 11.5.1 server and change the network adapter type to E1000 and re-run the upgrade.

### Revision History

1.0

09-Nov-2017

Initial Release

### Contributed by Cisco Engineers

John Barreto

Cisco TAC Engineer

### This Document Applies to These Products

- Paging Server

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 09-Nov-2017 | Initial Release |