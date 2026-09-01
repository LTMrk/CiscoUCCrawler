---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-meetings-222722-troubleshoot-camera-issues-in-webex-app-html-c41381eae8
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-meetings/222722-troubleshoot-camera-issues-in-webex-app.html
retrieved_at: 2026-09-01T14:56:07.684611+00:00
---

Troubleshoot Camera Issues in Webex App on Windows

# Troubleshoot Camera Issues in Webex App on Windows

### Download Options

Updated: January 23, 2025

Document ID: 222722

Contents

## Contents

## Introduction

This document describes how to identify and resolve common camera issues in the Webex App on Windows.

## Prerequisites

### Requirements

It is recommended that you have some familiarity with these topics:

- Windows Operating Systems

- Webex App

### Components Used

The software listed here has been used to make the tests and produce the results described in this document:

- Windows 11

- Webex App on version 45.2

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Overview of Common Camera Issues

When using Webex on Windows, it is possible for users to encounter various camera-related issues, such as:

- Camera access denied.

- Camera disabled or not detected.

- Application or driver conflicts.

- Camera device not found.

Here are some examples of camera connection issues and the troubleshooting steps to address them.

### Issue 1: Access to the Camera Denied

#### Error:

#### Logs:

```
2024 - 11 -25T15: 41 : 28. 579Z <Error> [ 0x3330 ][]WME: 0 ::[WSE] CWseMFSourceReaderSink::CreateSourceReader() ActivateObject failed, hr=- 2147024891 2024 - 11 -25T15: 41 : 28. 579Z <Info> [ 0x3330 ][]WME: 0 ::[WSE] CWSEMFVideoCapEngine::Start() Result = - 2147024891 2024 - 11 -25T15: 41 : 28. 579Z <Error> [ 0x3330 ][]WME: 0 ::[WME] CWmeLocalVideoTrack::StartCamera, m_pVideoCapEngine start error, ret= 1174552834
```

#### Root Cause :

The system denies access to the camera, possibly due to privacy settings.

#### Solution :

1. Open Settings in Windows.

2. Navigate to Privacy & Security > Camera .

3. Ensure that camera access is enabled for apps, and Webex is allowed to access the camera.

Reference: Camera Privacy Settings .

### Issue 2: Camera Disabled

#### Error:

#### Logs :

```
2024 - 11 -25T17: 14 : 42. 426Z <Debug> [ 0x3330 ][]MediaConnection.cpp: 7505 media::Connection::sendMediaErrorDirectly::media error: VideoCameraNoDevicePreCheck 2024 - 11 -25T17: 19 : 03. 259Z <Debug> [ 0x326c ][]AudioVideoSettingsViewModel::onMediaDeviceError:: 2 , Media Device Error
```

#### Root Cause :

The camera is disabled in the system settings or not detected.

#### Solution :

1. Open Device Manager .

2. Locate your camera under Cameras .

3. Right-click the device and select Enable .

### Issue 3: Camera Already in Use

#### Error:

#### Logs :

```
2024 - 11 -27T21: 04 : 33. 393Z <Warn> [ 0x2634 ][]CWseMFSourceReaderSink::OnReadSample failed! Result = - 1072875772 2024 - 11 -27T21: 04 : 33. 882Z <Debug> [ 0x1e50 ][]MediaConnection.cpp: 10692 media::Connection::OnError::error type: VideoCameraOccupied
```

#### Root Cause :

Another application (Example: Zoom, Microsoft Teams) is using the camera, preventing Webex from accessing it.

#### Solution :

1. Close any other applications that are possibly using the camera.

2. Restart Webex and try again.

### Issue 4: Camera Device Not Found

#### Error:

#### Logs :

```
2024 - 11 -22T03: 06 : 53. 268Z <Error> [ 0x492c ][]CWseVideoCapDevice::InitCapCapability(), GetBaseFilter_i failed, hr=- 2147024894
```

#### Root Cause :

The error code 0x80070002 (ERROR_FILE_NOT_FOUND) indicates that the camera device was not found.

#### Solution :

1. Open Device Manager and uninstall the Integrated Webcam .

2. Reboot the system, and let Windows reinstall the driver automatically.

3. Ensure the camera driver is up to date.

4. Verify if antivirus software is blocking Webex from accessing the device.

### Revision History

1.0

23-Jan-2025

Initial Release

### Contributed by Cisco Engineers

Sunil Gurav

Technical Consulting Engineer

### Customers Also Viewed

- Record Webex Sessions Automatically

### This Document Applies to These Products

- WebEx Meetings

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 23-Jan-2025 | Initial Release |