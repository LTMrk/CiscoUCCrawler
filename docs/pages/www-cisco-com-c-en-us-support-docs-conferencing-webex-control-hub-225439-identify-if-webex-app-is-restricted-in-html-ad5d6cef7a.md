---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-225439-identify-if-webex-app-is-restricted-in-html-ad5d6cef7a
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/225439-identify-if-webex-app-is-restricted-in.html
retrieved_at: 2026-08-21T06:32:09.646452+00:00
---

Identify if Webex App is Restricted in Certain Regions

# Identify if Webex App is Restricted in Certain Regions

### Download Options

Updated: January 28, 2026

Document ID: 225439

Contents

## Contents

## Introduction

This document describes how to identify if the Webex app is restricted or not accessible in certain regions.

## Prerequisites

### Requirement

Cisco recommends that you have knowledge of these topics:

- Webex Control Hub

- Webex App

### Components Used

The information in this document is based on these software and hardware versions:

- Webex Control Hub

- Webex App on version 44.3.0.28993

- Windows OS

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background

This document describes how to identify if the Webex app ( free version of Webex App) is restricted or not accessible in certain regions. Webex App login results in the error “ App unavailable in your location. You can find out where you can use Webex, or if a paid plan is available in your country, at our Help Center ”.

Error as seen during Webex App Login

## Troubleshooting Steps

- Reproduce the issue, collect Fiddler logs, and capture a snippet of the error that is observed.

- Generate an Msinfo32 log file from your system (not mandatory but good to have).

- Analyse the Fiddler logs to ascertain failures related to the error.

Note : These steps are for Windows OS.

## Logs Analysis

1. Access Fiddler.

2. Click the Import Sessions option under File and select HTTP Archive , then navigate to the file and click Open to open within Fiddler.

3. In Fiddler, click Find from the navigation bar and type Operation denied due to region restriction . Then, click Find Sessions .

4. These messages can be seen in the Fiddler logs.

You can see this POST request:

```
POST https://wdm-a.wbx2.com/wdm/api/v1/devices?includeUpstreamServices=features%2Csettings%2Cwebsocket HTTP/1.1 Connection: Keep-Alive Date: 2024-04-01T04:05:42.801Z Content-Type: application/json Accept-Encoding: deflate, gzip User-Agent: sparkwindows/44.3.0.28993 TrackingID: CLIENT_88fc9de5-65fc-41b6-8713-39d9297789f2 Content-Length: 312 Host: wdm-a.wbx2.com {"capabilities":{"groupCallSupported":false,"sdpSupported":false},"clientAddress":"127.0.0.1","countryCode":"CN","deviceType":"WINDOWS","localizedModel":"DESKTOP","model":"DESKTOP"
```

POST Request as seen in Fiddler logs

In response to this request, you can see this 451 Unknown Response:

```
HTTP/1.1 451 Unknown Vary: Origin X-Content-Type-Options: nosniff Cisco-Spark-Error-Codes: 4404003 Content-Type: application/json Content-Length: 227 Date: Mon, 01 Apr 2024 04:05:42 GMT Server: istio-envoy X-Envoy-Upstream-Service-Time: 4 {" errorCode ":4404003,"message":" Operation denied due to region restriction ","errors":[{"errorCode":4404003,"description":"Operation denied due to region restriction"}],"
```

451 Unknown Response as seen in Fiddler logs

## Root Cause

The login was not successful as the " Operation denied due to region restriction " is seen in the Fiddler logs.

The free version of Webex App is not available for use in export control restricted countries (Cuba, Iran, North Korea, and Syria) and Crimea, Mainland China, Russia, and Belarus.

Free version of Webex App features:

- Provides unlimited messaging and calling with other Webex users.

- Allows hosting secure virtual meetings lasting up to 40 minutes.

- Supports up to 100 attendees per meeting.

- Available for download with a set of features suitable for basic collaboration needs.

- Free accounts are available in many countries and regions.

- Users can upgrade to paid plans to schedule longer meetings and access more features.

14-Day Trial Version features:

- Typically offers a full set of paid features for a limited time (14 days).

- Enables users to experience the complete capabilities of Webex, including extended meeting durations and advanced collaboration tools not available in the free version.

- Designed to allow evaluation of the full Webex experience before committing to a paid subscription.

## Solution

Check which d ifferent Webex capabilities, subscriptions and devices are available depending on where you are located. Review this link to understand where Webex is available.

## Related Information

### Revision History

1.0

28-Jan-2026

Initial Release

### Contributed by Cisco Engineers

Jagatbir Singh Jaijee

Technical Consulting Engineer

### This Document Applies to These Products

- Webex Control Hub

- WebEx Meetings

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 28-Jan-2026 | Initial Release |