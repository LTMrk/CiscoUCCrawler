---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-teams-215414-troubleshooting-webex-teams-call-failure-ht-a8c9c0a4cb
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-teams/215414-troubleshooting-webex-teams-call-failure.html
retrieved_at: 2026-08-16T22:06:16.743305+00:00
---

Troubleshoot Calling in Webex Failure when Paired to an On-Prem Registered Device

# Troubleshoot Calling in Webex Failure when Paired to an On-Prem Registered Device

### Download Options

Updated: December 9, 2020

Document ID: 215414

Contents

## Contents

## Introduction

This document describes an issue where Webex is not able to place calls when it is paired to an on-premise registered device via proximity.

## Problem: Webex Unable to Place Calls when it is Paired to an On-Premise Registered Device

When you attempt to make an outbound call or join a Webex meeting from Webex app, while it is paired to an on-premise device, Webex throws the error "This device does not allow you to start calls or join meetings using your Webex app. Try placing the call directly from the device.". Steps to reproduce the problem are described here:

Step 1. The Webex app successfully pairs to the device as shown in the image:

Step 2. When the meeting becomes available to join, click the Now button to launch the join screen as shown in the image:

Step 3. Verify the device is selected and click Join Meeting as shown in the image:

Step 4. After you click on Join meeting you are  presented with an error as shown in the image:

If you need these error collect logs from the Webex app for analysis.

Location of log files for Webex Application is:

- Windows: %USERPROFILE%\AppData\Local\CiscoSpark

- MacOS: ~/Library/Logs/SparkMacDesktop

Log Review

In the earlier mentioned log path, find the current_log.txt file and review to check:

From the log file, the TelephonyDevices.cpp and TelephonyService.cpp service keywords are used to find the attempted call made by the client.

```
2020-04-19T01:46:47.024Z <Debug> [0x1190cadc0] TelephonyDevices.cpp:1252 create:Creating device of type: PairedXApiDevice 2020-04-19T01:46:47.024Z <Debug> [0x1190cadc0] TelephonyService.cpp:3851 getSelectedCallDevice:Call Device created of type: PairedXApiDevice
```

After the call is attempted, you must see the error thrown for the call failure as shown:

```
2020-04-19T01:46:47.029Z <Error> [0x1190cadc0] TelephonyDevices.cpp:1158 notifyXapiCallError:Notifying UI of call failure due to xAPI error : Call Control setting disabled for OnPrem Device 2020-04-19T01:46:47.030Z <Debug> [0x1190cadc0] TelephonyService.cpp:5436 notifyCallFailure:Will notify head about error
```

## Solution

This issue occurs when CallControl under Proximity settings is not enabled. You should enable CallControl under the Proximity settings of the device. This can be achieved with one of these options:

### Option 1. The GUI of the Device

Log in to the endpoints GUI and Navigate to Setup > Configuration > Proximity and enable CallControl as shown in the image:

### Option 2. CUCM if the Device is Registered to CUCM

From Cisco Unified Communications Manager (CUCM) Administration , Navigate to Device > Phone > Select Affected Device and scroll down to the Proximity settings and enable Call Control as shown in the image:

### Option 3: The CLI of the Device

```
xConfiguration Proximity Services CallControl: Enabled
```

## Related Information

- Cisco Webex Guide for On-Prem Registered Devices

- Technical Support & Documentation - Cisco Systems

### Contributed by Cisco Engineers

Payven Simien

Cisco TAC Engineer

### This Document Applies to These Products

- Webex App