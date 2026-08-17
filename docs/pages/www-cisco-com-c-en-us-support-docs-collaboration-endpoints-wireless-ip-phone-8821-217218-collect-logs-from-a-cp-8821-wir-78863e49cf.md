---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-wireless-ip-phone-8821-217218-collect-logs-from-a-cp-8821-wir-78863e49cf
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/wireless-ip-phone-8821/217218-collect-logs-from-a-cp-8821-wireless-pho.html
retrieved_at: 2026-08-17T01:16:01.326827+00:00
---

Collect Logs From a CP-8821 Wireless Phone

# Collect Logs From a CP-8821 Wireless Phone

### Download Options

Updated: July 19, 2021

Document ID: 217218

Contents

## Contents

## Introduction

This document describes all of the methods that can be used to collect logs from a CP-8821 wireless phone.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on a CP-8821 on 11.0.5-SR1 firmware.

The log collection methods are the same as other firmware releases. There are some slight differences in what you are able to collect but that information is covered throughout this document.

The information in this document was created from the devices in a lab environment. All of the devices used in this document started with a cleared (default) configuration. If you are performing these tasks in a production environment, ensure that you understand the potential impact of any command.

## Log Collection Methods

### Device with Network Connectivity

The easiest and most commonly used method to collect logs from an 8821 is to download them via your browser. This is the best method to use in a scenario where the has network connectivity.

Step 1. In order for this method to work, you need to ensure that Web Access is enabled on the device.

Step 2. Once that's done, navigate to the IP of the phone in your browser.

Step 3. Select Console Logs on the left side as shown in the image.

Step 4. Once you select Console Logs you'll be presented with a list of logs stored on the device:

The most commonly used files are all_logs.tar and the Problem Report Tool Logs:

- Select all_logs.tar to download all log files on the device.

- Select an option under the Problem Report Tool (PRT) Logs section to pull some helpful diagnostic information in addition to the standard phone console logs.  This is the preferred option in most scenarios due to the additional diagnostic output that is collected.

PRTs can be generated with one of two methods:

- If you have physical access to the phone, access Settings > Phone Information > Report Problem > Submit . After about a minute, a notification indicates that the report was generated, and you can find it on the phone web page.

- The second option allows the administrator to generate the PRT from the phone web page, as shown in the image, but it requires the phone to be on 11.0(5) or higher.  This also requires access to the Admin web page ( https://x.x.x.x:8443 where x.x.x.x is the 8821 IP address).  The credentials for this page are configurable in CUCM and the default name and password is admin // Cisco as shown in the image.

### Device Without Network Connectivity

The first thing to do to collect logs from a device without network connectivity is to try to determine if the phone connects to the Access Point (AP) but does not acquire an IP. If this is happening, it would be a good idea to set a static IP on the device and use the first log collection method . However, in a scenario where the device does not connect to the AP, log collection can be done with one of two methods, both of which require additional hardware.

#### Phone Dock (CP-DSKCH-8821)

The first method allows us to put the 8821 on the wired network. This requires that you have a few things:

- 8821 Dock ( CP-DSKCH-8821)

- USB to Ethernet dongle ( List of supported USB dongles)

Note : The USB dongle is not intended to be connected to the desktop charger for day-to-day use. It is intended only to provision the device or for log collection.

Once you have a dock with the USB dongle attached and connected to the network, you can go to the Network Settings on the phone and confirm that the phone receives an IP address. If this phone doesn't have Web Access enabled already, you'll need the phone to acquire a config file from CUCM. In order to do this, ensure that the phone is receiving an option 150 (or manually configure the TFTP server on the phone) to allow it to acquire that file. Once that's done, navigate to the phone's IP in your browser.

#### USB Cable

The final method of log collection requires that you have the USB cable that shipped with the phone. It also requires that the phone already have Web Access or SSH Access enabled.

Step 1. Connect the phone to your computer with the USB cable. Windows machines do not require any driver installation but ensure that you have this driver installed if you use a Mac.

Step 2. Set the phone's IP to 192.168.1.100 (255.255.255.0) and put your PC on the same network. For reference, I use 192.168.1.101.

Step 3. If Web Access is enabled, enter the phone IP into your browser.

Step 4. If SSH Access is enabled, you can SSH to the phone IP. After a successful connection, you are presented with two prompts for credentials. The first prompt is to establish the SSH connection and these credentials are those configured on the device page in CUCM. After entering those, the phone prompts for the second set of credentials for which you can use debug // debug for the username and password.

Step 5. After the second prompt, configure your SSH application to log the terminal output to a file and then run the sdump command which dumps all of the console logs into the Putty session.

Note : Logs collected via SSH are only helpful to troubleshoot issues that are reproducible on-demand. Collection of historical logs or a PRT is not possible via SSH.

## Related Information

- How to Troubleshoot Wireless Phones

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

19-Jul-2021

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 19-Jul-2021 | Initial Release |