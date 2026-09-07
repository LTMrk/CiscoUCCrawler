---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-attendant-console-standard-119249-config-cuac-00-html-399fade0c1
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-attendant-console-standard/119249-config-cuac-00.html
retrieved_at: 2026-09-07T15:48:41.792923+00:00
---

Configure Cisco Unified Attendant Console 10.5.x Standard Edition

# Configure Cisco Unified Attendant Console 10.5.x Standard Edition

### Download Options

Updated: November 9, 2015

Document ID: 119249

Contents

## Contents

## Introduction

This document describes the basic configuration steps for the Cisco Unified Attendant Console 10.5.x Standard Edition.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Unified Attendant Console 10.5.1.1543

- Cisco Unified Communications Manager 8.6.2.23900-10

- Microsoft Windows 7 Professional Edition (64-bit)

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

Complete these steps:

Note : Do not confuse this application user to the actual operator. The application user will act as a resource by the Telephony Service Provider (TSP) in order to gain device information/control when the need is raised by the operator.

This image shows the devices that this application includes in its controlled device section. Note that these include the device that operator will use for "login" and for BLF.

This application user also needs to have these roles included:

- Standard AXL API Access

- Standard CTI Allow Calling Number Modification

- Standard CTI Allow Call Park Monitoring

- Standard CTI Allow Control of All Devices

- Standard CTI Allow Reception of SRTP Key Material

- Standard CTI Enabled

This user would be be referenced for log in via the Cisco TAPI client (TSP) to CallManager. Make sure all required devices are entered in the controlled device section for this user. If that is not done, the login to Cisco Unifed Attendant Console standard client will fail.

- Double-click the installation file.

Note : Treat this login screen more like a Jabber login screen, as you do not need to enter the Cisco Presence Admin ID and password. Instead, enter the UID and password of the operator who will administer the Cisco Unified Attendant Console standard software. This user needs to be enabled/licensed for IM and Presence so that appropriate Presence information can be fetched from the Cisco Presence/IM and Presence node.

In this example, the operator UID is "nupurk" and the extension is "1008". As soon as the extension is entered, TSP resolves the device information. This only comes with the application User ID which the TSP uses (this comes from step 1) in order to control this device. All that needs to be completed once the device information is found is to click the device. Log in happens automatically.

Note : The red warning is standard and expected. It is a reference for the operator to ensure that they select the correct extension.

## Verify

If all goes as expected per the steps in the Configure section, this log in screen displays. The directory population with the Presence information displays as soon as the sync with CallManager is complete. The directory sync process is usually very fast.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

## Related Information

- CUAC 10.5 Standard Edition Administration Guide

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

09-Nov-2015

Initial Release

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 09-Nov-2015 | Initial Release |