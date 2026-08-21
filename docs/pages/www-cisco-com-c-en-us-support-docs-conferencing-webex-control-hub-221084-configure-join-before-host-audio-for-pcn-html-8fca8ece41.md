---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-221084-configure-join-before-host-audio-for-pcn-html-8fca8ece41
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/221084-configure-join-before-host-audio-for-pcn.html
retrieved_at: 2026-08-21T06:29:51.383033+00:00
---

Configure Join before Host Audio for PCN or Control Hub Meeting

# Configure Join before Host Audio for PCN or Control Hub Meeting

### Download Options

Updated: October 11, 2023

Document ID: 221084

Contents

## Contents

## Introduction

This document describes how to enable Audio/teleconference Join Before Host for Personal Conference Number (PCN) and Control hub.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- PCN

- Join Before Host

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem

Help articles are currently for Webex Personal Conferencing (PCN Meetings) only, within Site Administration. This article provides directions to enable it within Control Hub sites.

## Solution

### Site Level

In the new UI you can navigate to Services > Meeting. Select the meeting site you wish to modify, and enable join before host.  Choose Settings > Common Setting > Security. Scroll down to Attendees .

Control Hub Meetings

Common Settings Popup

Toggle both Allow attendees or panelists to join before host (Meetings, Training and Events) and Allow attendees to join the audio conference (Meetings) and then scroll down and select Save

Attendee menu to enable Join Before Host

### In Classic Site Management

Navigate to Meeting> Site and then under Site Name select the site to configure. A Configure icon appears. Then choose Common Settings and navigate to the Security tab. Toggle both Allow attendees or panelists to join before host (Meetings, Training and Events) and Allow attendees to join the audio conference (Meetings) and then scroll down and select Update . Then close Security tab.

The Common Settings page opens.

Common Settings menu

### User Level (In Control Hub)

Navigate to Users then find user in search. Choose the meetings tab, then in Settings apply to field choose your site.

Users Meetings tab

Under Advance Settings select Advanced User Settings then Webex Meetings and check Allow attendee to join audio portion of Personal Conference before host. Click Update and close.

Advanced Settings menu

Allow attendees to Join Before Host check box

After Site and User levels are enabled, attendees are able to join the audio portion of Personal Conferences and/or Webex Meetings.

## Related Information

- Cisco Technical Support & Downloads

### Revision History

2.0

11-Oct-2023

Initial Release

1.0

11-Oct-2023

Initial Release

### Contributed by Cisco Engineers

Jadda Jenkins

Cisco Technical Consulting Engineer

### This Document Applies to These Products

- Webex Control Hub

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 11-Oct-2023 | Initial Release |
| 1.0 | 11-Oct-2023 | Initial Release |