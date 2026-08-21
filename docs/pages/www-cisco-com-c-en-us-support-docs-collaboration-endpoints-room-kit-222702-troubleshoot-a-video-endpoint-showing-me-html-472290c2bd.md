---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-room-kit-222702-troubleshoot-a-video-endpoint-showing-me-html-472290c2bd
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/room-kit/222702-troubleshoot-a-video-endpoint-showing-me.html
retrieved_at: 2026-08-21T12:39:45.781396+00:00
---

Troubleshoot a Video Endpoint Showing Media Stats on Display

# Troubleshoot a Video Endpoint Showing Media Stats on Display

### Download Options

Updated: January 17, 2025

Document ID: 222702

Contents

## Contents

## Introduction

This document describes troubleshooting of Audio and Video statistics being displayed on a cloud-registered Video Endpoint.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cloud-registered Endpoints

- Webex Control Hub

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Room Kit Pro Endpoint on version RoomOS 11.18.1.8 8dc7b79ed48

- Webex Control Hub

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

This document describes how to troubleshoot Audio and Video statistics being displayed on a cloud-registered Video Endpoint. The Endpoint (Cisco Room Kit Pro) s hows Audio and Video statistics on the display only when it has joined a Webex Meeting. A restart, as well as a reboot, has been attempted on the Endpoint however, it did not resolve the issue. The Endpoint is using two display monitors and the Audio and Video statistics show up on both of them. They are not shown when the Endpoint is in an idle state.

The Video Endpoint does not show any other abnormal behavior or error messages. A Hard factory reset of the Video Endpoint seems to resolve the issue. Other similar Video Endpoints are not observing the issue.

Audio and Video Statistics Shown on Monitor 1 of the Video Endpoint

Audio and Video Statistics Shown on Monitor 2 of the Video Endpoint

## Troubleshooting Steps

- Have the Video Endpoint join a Webex Meeting and reproduce the issue. Note the time stamp when the statistics are displayed on the Video Endpoint.

- Proceed to collect the log bundle from the Video Endpoint.

- Analyze the logs, focusing on xstatus.txt and xconfig.txt files within the log bundle .

## Logs Analysis

Reviewing the log bundle, you can see the setting xConfiguration Conference Diagnostics StreamStatusOverlay set to On :

xConfiguration Conference Diagnostics StreamStatusOverlay: On

This configuration is responsible for displaying the Audio and Video statistics on the Video Endpoint displays.

## Root Cause

The configuration xConfiguration Conference Diagnostics StreamStatusOverlay: On is responsible for displaying the Audio and Video statistics on the Video Endpoint displays.

Conference Diagnostics StreamStatusOverlay is used to decide whether to show information, for example, bitrates and framerates, about each video stream on-screen. The information is shown in a transparent layer on top of each video frame. It is intended for debugging purposes, so in general, it must be Off . The actual data shown can change without further notice.

Note : The configuration could have any of these values: Default value: Off Off: Show only the video streams; no information overlay. On: Show the transparent data layer on top of the video streams.

Different Values Available for Conference Diagnostics StreamStatusOverlay

## Solution

Changing the value of xConfiguration Conference Diagnostics StreamStatusOverlay to Off resolves the issue.

A Factory reset also changes the value of the aforementioned configuration to the Default one, that is Off, which ultimately resolves the issue.

This explains why the statistics are no longer visible after a hard factory reset.

Please refer to the admin guide for the device which gives out more information.

## Related Information

- Admin Guide for the Device

- Cisco Room Kit Pro Data Sheet

- Cisco Room Kit Pro for Video Conferencing

### Revision History

1.0

17-Jan-2025

Initial Release

### Contributed by Cisco Engineers

Jagatbir Singh Jaijee

Technical Consulting Engineer

### This Document Applies to These Products

- Room Kit

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 17-Jan-2025 | Initial Release |