---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-221614-collect-prt-logs-from-mpp-ata-devices-htm-c734973ef5
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/221614-collect-prt-logs-from-mpp-ata-devices.html
retrieved_at: 2026-08-21T07:15:58.046658+00:00
---

Collect PRT Logs from MPP ATA Devices

# Collect PRT Logs from MPP ATA Devices

### Download Options

Updated: February 2, 2024

Document ID: 221614

Contents

## Contents

## Introduction

This document describes the process to put the PRT Logs in Cisco MPP ATA Devices.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Control Hub Administration

- Multi Platform Devices (MPP)

- Admin Password Device

- How to access Cisco ATA Web Page.

Note : For Webex Calling (WxC) provisioned devices ask for the password from WxC support; for factory reset devices, the password is admin.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

A Problem Report Tool ( PRT) Log is a file that contains logs and other files in order to help a Cisco Engineer to troubleshoot an issue.

Wjem Cisco ATA 191 or 192 have issues downloading the configuration file or registering to the Webex Calling services, analyzing a PRT Log can help to discover what the source of the problem is.

Step 1. Navigate to https://IP_ADDRESS_ATA/ .

Note : The default IP address for an ATA is 192.168.15.1

Step 2. A log in page opens. You can log into this page with the username admin and a password. Then select the Log in button.

Log In Page

Step 3. Select the option Administation in the top menu.

Top Menu

Step 4. Select the option Log and under that select PRT Viewer in the left menu.

Left Menu

Step 5. Select the option Generate PRT to create a new prt-log.tar.gz file.

Generate PRT

Step 6. A new screen appears confirming that the PRT Log is being created.

Generating PRT

Step 7. A new prt-log.tar.gz file is the output.

New PRT file

Step 8. Right-click on the link prt-log-tar.gz and choose Save link as... in order to download the logs.

## Related Information

- Get Started with Your Cisco ATA 191 and 192

### Revision History

1.0

02-Feb-2024

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 02-Feb-2024 | Initial Release |