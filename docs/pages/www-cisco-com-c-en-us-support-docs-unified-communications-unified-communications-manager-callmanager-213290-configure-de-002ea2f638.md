---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-213290-configure-de-002ea2f638
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/213290-configure-device-pack-on-cisco-call-mana.html
retrieved_at: 2026-08-21T13:57:10.248324+00:00
---

Configure Device Pack on Cisco Call Manager

# Configure Device Pack on Cisco Call Manager

Updated: April 27, 2018

Document ID: 213290

Contents

## Contents

## Introduction

This document describes the procedure to install device pack on Cisco Unified Communications Manager (CUCM).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUCM

- Secure FTP ( SFTP) server

- Device pack file (respective version Unified Communication Manager)

Refer these links in order to understand the device which are support on CUCM version.

- https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/matrix/CMDP_BK_CCBDA741_00_cucm-device-package-compatibility-matrix/CMDP_BK_CCBDA741_00_cucm-device-package-compatibility-matrix_chapter_01.html

- https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/matrix/CMDP_BK_CCBDA741_00_cucm-device-package-compatibility-matrix/CMDP_BK_CCBDA741_00_cucm-device-package-compatibility-matrix_chapter_00.html

### Components Used

The information in this document is based on these software and hardware versions:

- CUCM

- SFTP server

- Device pack file (respective version Unified Communication Manager)

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Device pack file is installed in order to update new feature and functionality to Communications Manager, it’s also accomplished with firmware upgrade on end point. However, there are scenarios when device pack is updated only for the purpose of additional feature and functionality and cluster wide firmware upgrade needs to be avoided.

This document describes the procedure in order to update device pack while avoiding cluster wide firmware upgrade.

## Configure

You need to download device pack from Cisco website, which respectively version of CUCM.

Refer this link and select the version that you would download for device pack as shown in the image.

https://software.cisco.com/download/home/268439621

Before you can install device pack on Communication manager, you need to copy the Firmware version on a separate file.

Navigate to Device > Device setting > Device default and copy the firmware information which you would like to keep as same firmware on end points and as shown in the image.

Once you downloaded the device pack from Cisco website, you need to upload the file to Unified Communication manger with the use of SFTP server.

Navigate to OS admin page > Software Upgrade > Install/Upgrade

Also, enter the mandatory information on this page and as shown in the image

- Source: Choose your local source (CD/DVD) or remote source (Remote Filesystem) of your upgrade files

- Directory: For remote file systems, enter the path to the patch file on the remote system

- Server: For remote file systems, enter the FTP or SFTP server name

- User Name: Enter the username for the remote node

- User Password: Enter the password for the remote node

- Transfer Protocol: Choose the transfer protocol, for example, SFTP

Note : When you apply a device package to enable new device support, a cluster-wide reboot is not required for CUCM version 11.5(1) or later. Instead, after you add the device pack, follow this in CUCM:

- Restart the Cisco Tomcat service on all nodes

- Restart Cisco TFTP on all servers, where this service is running

- Restart Cisco CallManager on the Publisher. If you’re not running the Cisco CallManager service on the Publisher, you can skip this step.

If you use CUCM version 11.0(1) or earlier, a cluster-wide reboot is required. A cluster-wide reboot is not required when you apply a device package in order to update the current firmware or configuration

Once Device pack installation is complete, you need to paste the firmware information on Device default Communication manager. Navigate to Device > Device Default > paste the firmware information that you would like to the keep as same firmware on Endpoints then click the icon in order to swap firmware on endpoint and as shown in the image.

## Verify

Use this section in order to confirm that your configuration works properly.

In order to verify that the phone has copied the new firmware image, use one of these methods:

- Find the IP address of the IP phone on which the upgrade is performed. Use the IP address in the browser in order to obtain the Device information of the IP phone. Check for the version to see if the firmware has changed to the new one.

- Physically go to the IP phone and press the Settings button. Scroll down to Model Information and press Select . Then, scroll down to Load File and verify that it is the same load file which is upgraded.

## Troubleshoot

This section provides information you can use in order to troubleshoot your configuration.

Troubleshooting section will be covered in different document.