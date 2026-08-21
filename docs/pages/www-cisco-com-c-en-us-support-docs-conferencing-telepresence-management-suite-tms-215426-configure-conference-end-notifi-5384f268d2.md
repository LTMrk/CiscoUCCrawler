---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-telepresence-management-suite-tms-215426-configure-conference-end-notifi-5384f268d2
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/telepresence-management-suite-tms/215426-configure-conference-end-notifications-f.html
retrieved_at: 2026-08-21T06:28:35.662245+00:00
---

Configure Conference End Notifications for meetings in Telepresence Management Server

# Configure Conference End Notifications for meetings in Telepresence Management Server

### Download Options

Updated: April 22, 2020

Document ID: 215426

Contents

## Contents

## Introduction

This document describes how to configure Conference End Notifications for meetings in Telepresence Management Server (TMS).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco TMS

- Cisco Endpoint running Telepresence Codec (TC) or Collaboration Endpoint (CE) Software

### Components Used

The information in this document is based on these software and hardware versions:

- TMS 15.x

- Cisco Endpoint running TC or CE Software (CE9.x)

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

Conference End Notifications appear on the Endpoint as shown in the image:

## Configure

The Conference End Notification parameter is configurable. To show the message multiple times, separate the minutes with a comma. For example, 1,5 displays the message 5 minutes and 1 minute before the conference is scheduled to end.

To configure the Conference End Notification Navigate to TMS > Administrative Tools > Configuration > Conference Settings and then to the Conference Ending section as shown in the image:

Below is how this setting can be applied to different kinds of meetings:

### Point to Point meeting (booked from TMS, no bridge engaged).

When a meeting is scheduled in TMS with 2 endpoints (no Bridge), TMS sends out an ApplicatIon Programming Interface (API) to the endpoint as shown in the image:

Logs from Endpoint:
CuilApp : User admin about to execute command '/UserInterface/Message/Alert/Display Duration: 10 Text: Scheduled meeting ends in 1 minute. To extend meeting call video administrator.' from 10.106.124.202.

### When using a TMS managed Bridge (Conductor, Cisco Meeting Server(CMS), Telepresence Server(TPS), Media Control Unit(MCU)).

If a meeting is scheduled via a CMS use the Show In-Video Warnings About Conference Ending setting as shown in the image:

If set to Yes , the remote participants receives an in-video warning about conference ending. This setting applies only to multipoint conferences hosted on a bridge.

- Book a meeting with 2 endpoints and include a bridge in TMS as shown in the image:

2. Event logs from TMS appear as shown in the image:

If this option is set to No , the TMS sends the message to the individual endpoints

1. Book a meeting meeting with 2 endpoints and include a bridge in TMS as shown in the image:

2. TMS Event Log appear as shown in the image:

### Book meetings using External Hosted Conference.

When you book a meeting using an External Hosted conference, only a minimal number of features are available on the TMS. TMS does not have control of the booking. TMS doesn’t end the meeting.

For example, book a meeting and use an External Hosted Address, meeting was booked for 3 minutes, Meeting started on time, however meeting never disconnected. The conference runs for over 15 minutes.

TMS does not disconnect the call, so TMS does not send a end meeting notification for this type of meetings as shown in the image:

TMS event logs does not indicate that the endpoint is disconnected from the conference as shown in the image:

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Contributed by Cisco Engineers

Amrinder Singh

Cisco TAC Engineer

### This Document Applies to These Products

- TelePresence Management Suite (TMS)