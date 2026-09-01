---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-meetings-220244-understand-webex-meetings-video-resoluti-html-37208a5aed
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-meetings/220244-understand-webex-meetings-video-resoluti.html
retrieved_at: 2026-09-01T14:56:33.006655+00:00
---

Understand Webex Meetings Video Resolution

# Understand Webex Meetings Video Resolution

### Download Options

Updated: February 17, 2023

Document ID: 220244

Contents

## Contents

## Introduction

This document describes how the resolution subscription for video works in Webex meetings for desktop and thin clients.

## Content

Video resolution adjustment in a Webex meeting depends on different factors like the number of attendees,  sender and receiver video layout set and local conditions (like network/performance CPU/memory for ALL the participants), these factos can impact in the video adjustment on the sender/receiver side, so the video resolution that is transmitted, does not mean it is the same resolution received, note not all of these factors depend on Webex side.

### Stage View Description:

Per current Webex Meetings video design, the sender and receiver depend on video subscription strategy to determine the max video resolution allowed, which depends on receiver video port number and size is how can be varied. Check the matrix to understand what the current logic is for Webex desktop and thin clients:

#### Filmstrip/Side by side 2+3: Stage

The maximum number of user videos for each window is:

-Filmstrip/Side by side : Up to 12 User Videos ( on-demand configure up to 24)

-Stage : Content + Up to 8 User Videos

#### Filmstrip/Side by side content + 2: Stage

The maximum number of user videos for each window is:

-Filmstrip/Side by side : Up to 12 User Videos ( on-demand configure up to 24)

-Stage : Content + Up to 8 User Videos

### 1. Active View Port subscription (Desktop Client)

Item1: With Grid Window in the stage, Video up to 360p resolution could be displayed in Active Window.

### 2. GridView / Thumbnail View Webex desktop (window, mac, thinclient)

## Q & A

- Q: If the receiving end chooses video layout Grid, Can the sender sends up to 360p video? A: Receiving end choose video layout Grid, if only 1 port in grid view, can up to 720P; 2~4 can up to 360P, > 4 can up to 180P.

- Q: If the receiving end chooses Focus or Stage video layout, Is this able to send with 720p? A: This depends on the device and the network conditions of both the sender and the receiver, and also depends on the the video port number and size.

- Q: If I have participant A=720p B=360p and C=180P then, the video resolution is adjusted to 180p on the receiver side (the minimum video resolution available between participants) or does it depend on the Active video/speaker? A: Only depend on receiver video port number and size. if A=720p B=360p and C=180P, and the sender has the ability to send 720P, then A can see 720p, B see 360p and C see 180P. if A=720p B=360p and C=180P, and the sender only has the ability to send 360P, then A see 360p, B see 360p and C see 180P.

### Revision History

1.0

17-Feb-2023

Initial Release

### Contributed by Cisco Engineers

Angela Garcia Blancas

### This Document Applies to These Products

- WebEx Meetings

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 17-Feb-2023 | Initial Release |