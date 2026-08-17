---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-ip-phone-8851-218093-configure-debug-level-in-mpp-phones-regi-ffbe67b7c9
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/ip-phone-8851/218093-configure-debug-level-in-mpp-phones-regi.html
retrieved_at: 2026-08-17T01:12:58.999848+00:00
---

Configure Debug Level in MPP Phones Registered in Webex Calling

# Configure Debug Level in MPP Phones Registered in Webex Calling

### Download Options

Updated: August 25, 2022

Document ID: 218093

Contents

## Contents

## Introduction

This document describes the procedure to set the log level to Debug in MPP (Multiplatform Firmware) Phones from Control Hub.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Calling

- Control Hub

### Components Used

The information in this document is based on these software versions:

- Cisco 8851 IP Phone - MPP Firmware 11.3.7

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

When an MPP Phone has a problem or error, the log level must be set in Debug before a PRT (Problem Report Tool) is retrieved from the device to troubleshoot.

## Set the log level

In order to correctly configure the log level, navigate to Control Hub > Devices and select the device that has the issue. Confirm that the device shows Online :

On the Device Page, navigate to the Device Management section and select Device Settings.

On Device Settings , confirm that Default Logging Level is set to Debugging and select Save.

Note : In order for the changes to take place, reset the device so that it downloads the updated configuration file.

## Generate the PRT

Once the correct log level has been configured in the device, allow time for the problem to occur and generate the PRT.

### Generate the PRT from the Device

Step 1. On the device, press the Applications button .

Step 2. Go to Status > Report Problem.

Step 3. Enter Date and Time of the problem.

Step 4. Select a Description from the list.

Step 5. Press Submit.

### Generate the PRT from Control Hub

Step 1. Navigate to Control Hub > Devices and select the device:

Step 2. On the Phone page go to Support > Device Logs.

Step 3. On the Manage Logs page, select Generate Log.

## Verify

Once the PRT has been submitted either manually or via Control Hub, the available logs are listed on the Manage Logs section:

## Related information

- Demand PRT Collection in Control Hub

- Report All Phone Issues

- Cisco Technical Support and Documentation

### Revision History

1.0

26-Aug-2022

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 26-Aug-2022 | Initial Release |