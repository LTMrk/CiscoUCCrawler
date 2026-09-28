---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-213256-install-devi-90e293d9f4
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/213256-install-device-pack-in-cisco-unified-com.html
retrieved_at: 2026-08-21T13:58:05.149233+00:00
---

Install Device Pack in Cisco Unified Communication Manager

# Install Device Pack in Cisco Unified Communication Manager

### Download Options

Updated: November 22, 2018

Document ID: 213256

Contents

## Contents

## Introduction

This document describes how to install the device pack in Cisco Unified Communication Manager (CUCM) for new devices.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of CUCM. The official install guide can be found here .

### Components Used

The information in this document is based on CUCM version 10.5.2.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Installation Procedure

Step 1. Download the appropriate device pack from Cisco.com. The image shows an example of a device pack downloaded for CUCM software version 10.5(2.15112). Once the file downloads, locate it on your PC, as shown in the image. CUCM needs to be reachable from this PC.

Step 2. Open a FTP server and connect with CUCM as shown in the image . In this example, Core FTP is the FTP software used, however, similar softwares can be used such as Filezilla.

Step 3. On the FTP server, specify the folder that contains the software to be uploaded, as shown in the image.

Step 4. Start the FTP service and configure a user and password for the connection, as shown in the image.

Step 5. On CUCM web interface, navigate to CUCM > OS Administration page .

Step 6. Select Software Upgrades > Upgrade/Install.

Step 7. Configure the appropriate data as shown in the image. Select Remote Filesystem and use the user and password configured in Step 4.

Step 8. Click Next.

Step 9. Select the software to be installed.

Step 10. Wait for the installation to complete.

Step 11. Perform the same steps on the Publisher and all the CUCM that runs TFTP services.

Note : For the new devices to be added on CUCM, you have to restart all the nodes of the cluster, otherwise you might experience errors with them.