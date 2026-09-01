---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-room-series-222708-troubleshoot-video-endpoint-shut-down-du-h-eb06fdf0c6
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/room-series/222708-troubleshoot-video-endpoint-shut-down-du.html
retrieved_at: 2026-09-01T19:35:13.257884+00:00
---

Troubleshoot Video Endpoint Shut Down Due to High Temperature

# Troubleshoot Video Endpoint Shut Down Due to High Temperature

### Download Options

Updated: January 18, 2025

Document ID: 222708

Contents

## Contents

## Introduction

This document describes troubleshooting a Video Endpoint randomly shutting down due to temperature exceeding critical limit.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cloud-registered Endpoints

- Webex Control Hub

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Room Bar Endpoint on version RoomOS 11.14.1.7 5361a1d6d58

- Webex Control Hub

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

This document describes how temperature exceeding critical limit can cause a cloud-registered Video Endpoint to randomly shutdown. The Video Endpoint (Cisco Room Bar) goes offline/shuts-down randomly. You need to unplug and re-plug the power cable to bring it up back online. Issue persists even after using another power cable/power socket/power adaptor. Hard factory reset of the Video Endpoint has not helped. Other Video Endpoints of the same model are not having issues. The Video Endpoint does not show any error messages or notifications before it goes offline.

## Troubleshooting Steps

- When the Video Endpoint goes offline, note the exact time stamp. The Offline status reflects in Control Hub as well, along with the exact time when the Endpoint was last seen online.

In order to view the last seen online status, navigate to Control Hub > Devices > Search for the concerned Endpoint . Click the Information icon to see the Last seen online details:

Devices Section of Control Hub Showing the Last Seen Online Date and Time

- Proceed to collect the log bundle from the Video Endpoint, once the Endpoint comes back online.

- Analyze the logs correlating with the time stamp when the issue occurs.

## Logs Analysis

When reviewing the log bundle , you can see log lines pointing to temperature exceeding critical limit:

```
2024-07-03T09:27:25.113+08:00 thermal_control[5328]: temperature criticalT_GPU: 94.50 C [0.50 > limit]
```

Error Snippet from the Log Bundle

```
2024-07-03T09:27:25.113+08:00 thermal_control[5328]: temperature exceeding critical limit - shutdown in 20000 ms
```

Error Snippet Showing Temperature Exceeding Critical Limit

```
2024-07-03T09:28:56.115+08:00 thermal_control[5328]: Thermal shutdown due to critical temperature
```

Error Snippet Showing Thermal Shutdown Due to Critical Temperature

Error Snippet Showing System Would Now Shutdown

```
2024-07-03T09:29:06.194+08:00 video[3951]: Received shutdown notification from SYSTEM_MAIN 2024-07-03T09:29:06.194+08:00 video[3951]: bootnotifier: Shutdown due to notification from main
```

## Root Cause

The root cause behind the Video Endpoint shutting down randomly, is due to the temperature of the system exceeding critical limit which causes a thermal shutdown.

Specifications for Operating and storage temperature and humidity:

- Operating temperature and humidity: 0°C to 35°C (32°F to 95°F) ambient temperature at 10% to 90% Relative Humidity (RH)

- Storage temperature and humidity: –20°C to 60°C (–4°F to 140°F) at RH 10% to

- 90% (non-condensing)

Acceptable Values for Operating and Storage Temperature and Humidity

## Solution

Moving the Video Endpoint to a cooler room resolves the issue as the temperature does not exceed the critical limit. The ambient temperature of this room is within acceptable limits for the operation of the Video Endpoint.

It is recommended to view this check-list while troubleshooting such issues:

- Ambient Temperature: Please check the ambient temperature of the room. Ensure the temperature is within acceptable limits for the operation of the device. High ambient temperatures can contribute to the device overheating.

- Overheating: Please check the device physically and see if it is overheating (does it feel unusually hot?). This can help determine if the device itself is overheating.

- Change the location of the device: Preferably, move the device to a room where a similar device is functioning correctly. This helps identify if the issue is environment-specific.

- Ventilation Check: Ensure that the device is placed in a well-ventilated area and that there are no obstructions around the ventilation holes.

- Dust and Debris: Check for any dust or debris that can be blocking the ventilation ports of the device. Cleaning these can help improve the airflow.

- Internal Fans: If possible, check if the internal fans are working correctly. Sometimes, a malfunctioning fan can cause overheating.

- Power Supply: Ensure that the power supply is stable and not fluctuating.

## Related Information

- Admin Guide for the Device

- Cisco Room Bar Data Sheet

### Revision History

1.0

21-Jan-2025

Initial Release

### Contributed by Cisco Engineers

Jagatbir Singh Jaijee

Technical Consulting Engineer

### Customers Also Viewed

- How do I upgrade and downgrade Cloud-Registered Cisco Endpoints on Room OS?

- Console Access for WebEx Room Series Devices and Quad Camera

- Recover Cloud-Registered Endpoint GUI when Offline in Control Hub

### This Document Applies to These Products

- Room Series

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 21-Jan-2025 | Initial Release |