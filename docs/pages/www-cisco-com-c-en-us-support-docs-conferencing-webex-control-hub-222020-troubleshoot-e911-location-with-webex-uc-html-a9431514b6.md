---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-222020-troubleshoot-e911-location-with-webex-uc-html-a9431514b6
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/222020-troubleshoot-e911-location-with-webex-uc.html
retrieved_at: 2026-08-16T18:00:34.094395+00:00
---

Troubleshoot E911 Location with Webex UCM Calling

# Troubleshoot E911 Location with Webex UCM Calling

### Download Options

Updated: May 31, 2024

Document ID: 222020

Contents

## Contents

## Introduction

This document describes how to add E911 Location with UCM Calling in Webex App.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex App

- Unified Communications Manager (UCM)

- Cisco Emergency Responder

- Cisco Expressway

- 3rd party vendor RedSky

### Supported Deployment Types

- Webex App 42.2 and later

- UCM 12.5SU6 and later

- Cisco Emergency Responder 12.5SU6 and later

- Cisco Expressway X14.1 and later

- UCM 12.5SU5a and later

- Cisco Emergency Responder 12.5SU5a and later

- Cisco Expressway X14.0.4 and later

### Components Used

The information in this document is based on these software and hardware versions:

- Webex App 44.2

- UCM Version 12.5SU5a

- Cisco Emergency Responder 12.5SU5a

- Cisco Expressway X14.0.4

- 3rd party vendor RedSky

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem: Unable to add E911 Location with UCM Calling on Webex App

The user is unable to add E911 location on Webex App.

Error message: "Something went wrong. Please try again." seen on the Edit emergency 911 address pop-up window:

Error on Webex App Pop-Up Window

### Log Review

Location of log files for Webex App for analysis:

- Windows: %USERPROFILE%\AppData\Local\CiscoSpark

- MacOS: ~/Library/Logs/SparkMacDesktop

From the mentioned log paths, find the current_log.txt file:

- Use the TelephonyFeatureFlags.cpp keyword to check that the Emergency Calling feature is enabled:

```
2024-02-28T09:37:35.453Z <Debug> [0x4ee0][]TelephonyFeatureFlags.cpp:7178 TelephonyFeatureFlags::isUcmRedSkyIntegrationEnabled:DESKTOP_PLATFORM, isUcmRedSkyIntegrationEnabled: 1
```

2. Use the E911RedSkyHttpRequester.cpp keyword to find the token request and the subsequent 401 error from RedSky:

```
2024-02-28T09:10:05.479Z <Info> [0xe57c][]E911RedSkyHttpRequester.cpp:19 E911RedSkyHttpRequester::getAccessToken:E911RedSky: getAccessToken request 2024-02-28T09:10:06.831Z <Error> [0xeaa0][]E911RedSkyHttpRequester.cpp:97 E911RedSkyHttpRequester::getAccessTokenRequest::<lambda_2>::operator ():E911RedSky: ERROR: request http or server error 401 2024-02-28T09:10:06.831Z <Error> [0xeaa0][]E911RedSkyManager.cpp:637 E911RedSkyManager::getAccessToken::<lambda_3>::operator ():E911RedSky: ERROR: action token fetch error: 401 message 2024-02-28T09:10:06.832Z <Debug> [0xeaa0][]E911RedSkyTelemetry.cpp:63 E911RedSkyTelemetry::sendGetTokenFailedTelemetry:E911RedSky: Telemetry - sendGetTokenFailedTelemetry
```

## Solution: Fix RedSky-Related Configuration in UCM Service Profile

Webex App clients need to get configuration from UCM to enable the HELD+ location updates.

A UCM admininistrator must configure the required paramentes in the UCM Service Profile(s) and ensure that the correct Organization ID is used.

### Configuration Procedure for UCM Service Profile

- In UCM admin, navigate to User Management > User Settings > Service Profile .

Note : In some instances, there can be multiple Service Profiles that need to be updated.

- Emergency Calling Profile Parameters

- Click the Enable Emergency Calling check box.

Warning : Organization ID under Emergency Calling Profile refers to the HELD company ID provided by RedSky.

This is NOT the same value as the Control Hub Organization ID.

- Secret ( provided by RedSky)

Caution : RedSky Location URL change Revised RedSky Location URL Address

- Emergency Numbers: 911, 933 (default)

- Click Save .

- Repeat steps 1-6 on any other Service Profiles that require E911 location.

## Related Information

- Deployment guide for Calling in Webex App (Unified CM)

### Revision History

1.0

31-May-2024

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 31-May-2024 | Initial Release |