---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-222958-troubleshoot-hybrid-calendar-error-an-html-a688ed3b07
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/222958-troubleshoot-hybrid-calendar-error-an.html
retrieved_at: 2026-08-21T06:32:31.027170+00:00
---

Troubleshoot Hybrid Calendar Error "An unknown validation error occurred."

# Troubleshoot Hybrid Calendar Error "An unknown validation error occurred."

### Download Options

Updated: April 16, 2025

Document ID: 222958

Contents

## Contents

## Introduction

This document describes how to identity root cause and fix error while enable Scheduling with Hybrid Calendar with Google for Cloud devices in Control Hub.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- A Webex Organization.

- Webex Hybrid Calendar.

- Google Workspace Admin Console.

### Components Used

The information in this document is based on these software and hardware versions:

- Webex Control Hub build 20240919-84b27c9

- Google Workspace Business Starter or higher

- Chrome browser 129.0.6668.58 (Official Build) (arm64)

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background

Enabling Hybrid Calendar (Scheduling) with Google requires an email address validation which is performed by CSDM which assist Atlas in managing device registration and activation.

## Control Hub error

From Control Hub > Management > Workspaces add "Scheduling" for a Workspace after click Validate button returns the error " An unknown validation error occurred. If you still see this error after repeated attempts, contact support. "

Google error

## Gathering logs

### Control Hub

From a browser tab, preferily using incognito. If using Chrome open DevTools > Network; for FireFox Web Developer Tools > Network. Go to admin.webex.com > Management > Workspaces > Scheduling. Choose Calendar provider and add email address, click on Validate .

HTTP Inspection

### Error Message

```
{"status":403,"errorMessage":"Email validation failed: null","valid":false}
```

## Validation

### Google APIs Explorer

Go to Google APIs Explorer , select GET as an HTTP request method, and run a query with this URL:

```
https://admin.googleapis.com/admin/directory/v1/customer/{customer}/resources/calendars/{calendarResourceId}
```

Google API

Caution : customerId and calendarResourceId are mandatory fields, see additional references to know how to get them.

## Root Cause

Webex Cloud devices must have a valid email addresses that match the Google room resource format, @resource.calendar.google.com .

## Solution

From Google Workspace Admin > Directory > Building and resources > Manage resources confirm Resource email field.

Google Resource

Email address used in Control Hub

```
c_1888af8kmnb1ojo6nu3drhdg01pa@resource.calendar.google.com
```

Email address in Google admin

```
c_1888af8kmnb1ojo6nu3drhdg01pa u @resource.calendar.google.com
```

Add Resource email into Scheduling > Email address and click Validate . A 200 API response confirms the change, then click Save .

200 OK

Workspace successfully activated for Hybrid Calendar with Google.

Configuration applied

Calendar Activated

## Error codes

## Related Information

- Requirements for Hybrid Calendar with Google Calendar

- Add Hybrid Calendar to workspaces with Board, Desk, and Room series

Chrome DevTools

- Firefox DevTools

- Find your customer ID

- Managing resources with the resourceID field

### Revision History

1.0

16-Apr-2025

Initial Release

### Contributed by Cisco Engineers

Josue Jonathan Vizcaino Huape

Technical Consulting Engineer

### This Document Applies to These Products

- Webex Control Hub

| 400 Bad Request | Invalid email format for resource |
|---|---|
| 403 Forbidden | Contains invalid data |

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 16-Apr-2025 | Initial Release |