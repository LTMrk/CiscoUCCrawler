---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-221052-generate-prt-manually-for-mpp-phones-reg--cd5445b67a
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/221052-generate-prt-manually-for-mpp-phones-reg.html
retrieved_at: 2026-08-20T23:21:44.499007+00:00
---

Generate PRT Manually for MPP Phones Registered on Webex Calling

# Generate PRT Manually for MPP Phones Registered on Webex Calling

### Download Options

Updated: October 10, 2023

Document ID: 221052

Contents

## Contents

## Introduction

This document describes how to get the PRT log from an MPP Phone that is currently registered on Webex Calling.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Calling

- Control Hub

- Multi-Platform Phones (MPP)

### Components Used

The information in this document is based only on Multi-Platform Phones.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

When you try to get the Problem Report Tool (PRT) logs from Control Hub and it fails, you must know how to download the PRT logs manually from an MPP device.

## Enable Web Access for the MPP Phone

By default, in Webex Calling, when a device is onboarded in Control Hub, it has the web access disabled. In order to enable it, navigate to Control Hub > Devices and choose the device that you want to enable Web Access.

Once the device is chosen, click Device Settings :

Device settings 1

By default, the device uses the location settings. First, you must change the device settings to use custom settings:

Device settings 2

Once chosen, custom settings are now available.

Scroll down the page, find the option MPP Web Access (User) , enable the toggle, and click Save :

MPP Web Access (User)

The device must be rebooted in order to take the new configuration.

## Generate the PRT from the Device

Step 1.On the device, click the Applications button Applications button .

Step 2. Navigate to Status > Report Problem .

Step 3.Enter the Date and Time of the problem.

Step 4. Choose a Description from the list.

Step 5.Click Submit .

## Get the PRT Log from the Web GUI

Step 1. Log in to https://IP_ADDRESS_PHONE/ .

Note : If the IP Address is unknown, it can be obtained from Settings > Status > Network Status > IPv4 Status .

Step 2. The first time the page shows a warning message, choose Advanced .

Warning message 1

And then click, Proceed to 10.152.212.70 (unsafe) .

Warning message 2

Step 3. Navigate to Info > Debug Info . Download the PRT Log. Right-click on the link and choose Save link as... in order to download the logs.

Web GUI

The PRT log is now downloaded to your PC.

### Revision History

1.0

10-Oct-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 10-Oct-2023 | Initial Release |