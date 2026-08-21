---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-dx80-212294-how-to-upload-background-image-on-dx80-a-html-3a4a8d556f
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/dx80/212294-how-to-upload-background-image-on-dx80-a.html
retrieved_at: 2026-08-21T12:45:00.015145+00:00
---

How to upload background image on DX80 and DX70 endpoints

# How to upload background image on DX80 and DX70 endpoints

### Download Options

Updated: October 18, 2017

Document ID: 212294

Contents

## Contents

## Introduction

This document describes how to upload background image (customer wallpaper) on DX80 and DX70 endpoints.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- DX70, DX80 endpoints

- CUCM (Cisco Unified Communications Manager)

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

Note : The resolution of the background image must be 2985x1080 pixels.

Step 1. In order to u pload the image on all CUCM server nodes, perform the following actions:

- Navigate to Cisco Unified OS Administration > Software Upgrades > TFTP file management

- Click on the button Upload File , a new window will open. Click on the button Choose File and select the desired image. For Directory enter the value Desktops/2985x1080x24. Click on the button Upload File

Caution : You must restart the TFTP service on all CUCM server nodes, on which a background image has been uploaded.

Step 2. In order to restart the TFTP service on a CUCM server node, perform the following actions:

- Login to Cisco Unified Serviceability and navigate to Tools > Control Center - Feature Services

- Select the CUCM server node from the drop-down menu

- At the section CM Services select the Cisco Tftp service and click on the Restart option at the upper left corner

Step 3. Login to Cisco Unified CM Administration and navigate to Device > Device Settings > Common Phone Profile . Select the Standard Common Phone Profile . Perform the following actions:

- Uncheck the Enable End User Access to Phone Background Image Setting

- At the field Background Image e nter the filename of the image as DXimage.png . Put a checkmark at the Override Common Settings check box, located to the right of the field

- Click on Save and then on Apply Config in order for the changes to be applied

Step 4. Under Cisco Unified CM Administration , navigate to Device > Phone and select the DX endpoint for which the image was uploaded.

- At the field Common Phone Profile from the drop-down list select the Standard Common Phone Profile

- At the field Background Image add the filename of the background image

- Click on Save and then on Apply Config in order for the changes to be applied

## Verify

The background image should now be displayed on the DX endpoints, for which it was uploaded.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

18-Oct-2017

Initial Release

### Contributed by Cisco Engineers

Anurag Srivastava

Cisco TAC Engineer

Edited by Lidiya Bogdanova

Cisco TAC Engineer

### This Document Applies to These Products

- Webex DX80

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 18-Oct-2017 | Initial Release |