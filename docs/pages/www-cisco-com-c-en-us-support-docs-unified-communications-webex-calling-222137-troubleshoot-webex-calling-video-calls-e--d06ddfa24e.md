---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-222137-troubleshoot-webex-calling-video-calls-e--d06ddfa24e
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/222137-troubleshoot-webex-calling-video-calls-e.html
retrieved_at: 2026-08-21T07:16:23.588675+00:00
---

Troubleshoot Webex Calling Video Calls Establishment

# Troubleshoot Webex Calling Video Calls Establishment

### Download Options

Updated: July 17, 2024

Document ID: 222137

Contents

## Contents

## Introduction

This document describes the troubleshooting process for internal calls in Webex Calling not establishing with video.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Calling

- Webex Control Hub

### Components Used

This document is not restricted to specific hardware and software versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Webex Calling supports video calls across any compatible endpoints that can successfully negotiate and establish the session with video capabilities.

It is important to outline that the support for video calls using Webex Calling services is restricted to endpoints within the same organization. All calls that are routed through the Public Switched Telephone Network (PSTN) are limited to audio-only, as PSTN services generally do not support video functionality.

For video to be displayed correctly during a call, it is essential that the endpoints with video capabilities are configured appropriately to handle video communications.

## Common Configuration Issues

### User License Assigned

Verify that the user(s) affected have Webex Calling licenses assigned.

Step 1. Inside Control Hub select Users , select the User .

Step 2. Scroll to Summary > License .

Step 3. Ensure that Webex Calling license is assigned.

User License Assignment

### Workspace License Assigned

Verify that the workspace(s) affected have Webex Calling licenses assigned.

Step 1. Inside Control Hub select Workspaces , select the Workspace .

Step 2. Scroll to Overview > Calling .

Step 3. Ensure that Webex Calling license is assigned.

Workspace License Assignment

### Webex Application Settings in Control Hub

In case the issue resides with the Webex Application not establishing video calls, verify these configurations.

#### Organization Toggles in Control Hub

In order to allow the video capabilities for all of the users in your organization with the Webex Application, enable the In-call feature access toggles.

Step 1. Under SERVICES > Calling > Client Settings .

Step 2. Scroll to In-call feature access .

Step 3. Activate the toggles to allow desktop/mobile users to support video calls.

When these toggles are enabled, another option appears to set all calls to start with video for desktop or mobile endpoints. If needed, click the checkbox for each of these options.

Organization Video Toggles

#### User Toggles in Control Hub

In order to allow the video capabilities for certain users in your organization with the Webex Application, enable the In-call feature access toggles.

Step 1. Navigate to the User(s) experiencing the issue and select Calling .

Step 2. Scroll to In-call feature access .

Step 3. Activate the toggles to allow desktop or mobile users to support video calls.

When these toggles are enabled, another option appears to set all calls to start with video for desktop or mobile endpoints. If needed, click the checkbox for each of these options.

User Video Toggles

Note : The user toggles take precedence over the settings configured at organization level in Control Hub.

#### Configuration Preferences in the Webex Application

The configuration to start all incoming calls with video can also be configured in the Webex Application, and it takes precedence over the settings configured at user level inside Control Hub.

Step 1. Inside the Webex Application select Settings > Calling .

Step 2. If needed, click the checkbox to answer all incoming calls with video.

Incoming Video Calls

Note : If the video toggles in Control Hub are disabled at the both the organization and user level, the video icon inside the Webex Application of the user(s) do not appear when trying to do a call, and when the call is established the Enable video option does not appear either.

Video Icon Removed Video Option Removed

### Compression Settings in Control Hub

In case the issue replicates from any video capable endpoint apart from the Webex Application or the issue persists after checking the previous configurations, check that the users or workspaces making the video call have the correct compression settings.

Step 1. Inside Control Hub navigate to the Calling tab of the corresponding user or workspace.

Step 2. Scroll to Compression options .

Step 3. Review that the Normal compression option is selected, otherwise the user can only make audio calls.

Step 4. If required, click the radial button to set the compression to Normal compression . After doing this change reboot all of the devices associated to the user or workspace.

Compression Options

## Recommended Information for a TAC Case

If the issue persists after the troubleshooting steps in this document have been performed and a TAC case is needed, Cisco recommends you to include this information.

- Organization ID

- E-mail of the affected user(s).

- A description of the issue experienced, including the information of the devices being used for the video call.

- A call example with the issue, including caller and called numbers along with the time when the call was made.

## Related Information

- Webex Calling Preferred Architecture

### Revision History

1.0

18-Jul-2024

Initial Release

### Contributed by Cisco Engineers

Alejandro Gomez LUNA

Technical Consulting Engineer

### This Document Applies to These Products

- Webex Calling

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 18-Jul-2024 | Initial Release |