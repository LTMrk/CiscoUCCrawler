---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-webex-desk-limited-edition-220725-collect-logs-from-webex-clo-b87a09bc69
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/webex-desk-limited-edition/220725-collect-logs-from-webex-cloud-video-devi.html
retrieved_at: 2026-08-21T12:39:50.299602+00:00
---

Collect Logs from Webex Cloud Video Devices

# Collect Logs from Webex Cloud Video Devices

### Download Options

Updated: July 8, 2024

Document ID: 220725

Contents

## Contents

## Introduction

This document describes the procedure to collect logs with extended logging and packet captures from video devices registered to the Webex Cloud.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Methods for Collecting Logs

There are four collection methods available to collect log files from Webex video devices.

- Through Control Hub and Local Device Controls

- From the web Interface of the device

- Through Control Hub only

- From the physical touch interface or touch panel of the device

## Control Hub and Local Device Controls

Users with Webex Control Hub access can collect logs through Local Device Controls from Webex video devices with these steps:

- Navigate to the Webex Control Hub in a web browser and log in with Control Hub credentials. Control Hub Login Screen

- Navigate to Devices under the Management section and select the device to collect logs from. Control Hub Devices

- select Local Device Controls under the Support section and select Proceed . The computer must be on the same network as the device. Control Hub Local Device Controls

- Navigate to Issues and Diagnostics under the System Maintenance section and select the System Logs tab. System Logs Tab

- Reproduce the problem or functionality and note down the TimeStamp and a description of the problem.

- Navigate to the System Logs section, select the drop-down arrow next to Download logs... , and select Full logs (recommended) or Anonymized logs . Anonymized logs have personally identifiable information (PII) r emoved. Download the Full logs to troubleshoot with Cisco TAC (Technical Assistance Center). Log Download Options

- Navigate to the Packet Captures section and select the file name to download the packet captures manually. This is required if the packet captures are too large for the log bundle. Packet Captures Section

## Device Web Interface

Users with device credentials can collect logs from the Webex video device web interface with these steps:

- Navigate to the IP address of the device in a web browser. Enter device credentials at the log in page. Device Login Screen

- Navigate to Issues and Diagnostics under the System Maintenance section and select the System Logs tab. System Logs Tab

- Reproduce the problem or functionality and note down the TimeStamp and a description of the problem.

- Navigate to the System Logs section, select the drop-down arrow next to Download logs... , and select Full logs (recommended) or Anonymized logs . Anonymized logs have Personally Identifiable Information (PII) r emoved. Download the Full logs to troubleshoot with Cisco TAC. Log Download Options

- Navigate to the Packet Captures section and select the file name to download the packet captures manually. This is required if the packet captures are too large for the log bundle. Packet Captures Section

## Control Hub Only

Users with Webex Control Hub access can collect logs from Webex video devices with the next steps. This method does not provide extended logging or packet capture options.

- Navigate to the Webex Control Hub in a web browser and log in with Control Hub credentials. Control Hub Login Screen

- Navigate to Devices under the Management section and select the device to collect logs from. Control Hub Devices

- Select Manage next to Device Logs under the Support section. Device Logs Support Section

- Select the + Generate Log button to generate a full log bundle. Generate Logs Button

- Once the file is generated, select the Download button under the Action column. This log bundle is anonymized. Anonymized logs do not include any details such as meeting names and call information. It is recommended to collect non-anonymized logs when possible. Download Logs in Control Hub

## Device Physical Interface

Users with physical device access can collect logs from the physical interface or touch panel of the Webex video device with these steps:

- Tap the Settings icon in the top left. Device home screen

- Tap Device settings . Settings side window

- Tap Issues and diagnostics . Device settings menu

- Tap the slider button next to Extended logging to enable extended logging and a packet capture. Extended logging option

- Reproduce the problem or functionality and note down the TimeStamp and a description of the problem.

- Navigate back to Issues and diagnostics and tap Send logs . Provide the log ID ( identification) number to Cisco TAC. This method sends logs to Cisco only and does not download a log bundle locally. Send logs and feedback ID

## Related Information

- Cisco Technical Support & Downloads

### Revision History

2.0

08-Jul-2024

Initial Release

1.0

11-Aug-2023

Initial Release

### Contributed by Cisco Engineers

Victoria West

Cisco Escalation Engineer

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 08-Jul-2024 | Initial Release |
| 1.0 | 11-Aug-2023 | Initial Release |