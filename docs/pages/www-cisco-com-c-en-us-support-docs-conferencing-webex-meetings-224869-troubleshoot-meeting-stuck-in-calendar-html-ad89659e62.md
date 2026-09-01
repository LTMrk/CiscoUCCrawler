---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-meetings-224869-troubleshoot-meeting-stuck-in-calendar-html-ad89659e62
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-meetings/224869-troubleshoot-meeting-stuck-in-calendar.html
retrieved_at: 2026-09-01T14:57:02.566337+00:00
---

Troubleshoot Meeting Stuck in Calendar after Cancellation

# Troubleshoot Meeting Stuck in Calendar after Cancellation

### Download Options

Updated: September 11, 2025

Document ID: 224869

Contents

## Contents

## Introduction

This document describes the issue where Webex meetings canceled on the Webex site (browser platform) persist in Microsoft Calendar.

## Prerequisites

Basic knowledge of scheduling and managing meetings in Webex.

Access to both Calendar and the Webex scheduling platform (Web, Desktop, or Outlook integration).

### Requirements

Microsoft Outlook / Google Calendar.

Webex account with scheduling permissions.

### Components Used

Microsoft Outlook (desktop application).

Webex site (browser platform) .

Webex Desktop App (optional).

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Cause

This behavior occurs when a meeting is:

- Scheduled from Outlook / Google Calendar or the Webex desktop app ,

- But later canceled from the Webex site (browser platform) .

Because Outlook does not synchronize cancellations made outside of its platform, the meeting continues to appear in the Outlook calendar.

When you attempt to delete the meeting from the Webex site, you can see a notification similar to this:

### Meeting Cancellation Window

## Solution

Cancel the meeting directly from the Calendar (Outlook) and send a cancellation to attendees.

Cancellation Steps (if meeting persists in Outlook)

Open Outlook Calendar .

Locate the canceled Webex meeting.

Right-click the meeting and select Cancel meeting .

In the window that opens, click Send Cancellation .

Cancellation Email

## Prevention

To avoid this issue in the future:

- Always cancel meetings from the same platform where they were created.

- If the meeting was scheduled in Outlook , cancel it in Outlook.

- If the meeting was scheduled on the Webex site , cancel it from the Webex site.

### Revision History

1.0

11-Sep-2025

Initial Release

### Contributed by Cisco Engineers

Mohammad Bakir

Technical Consulting Engineer

### This Document Applies to These Products

- WebEx Meetings

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 11-Sep-2025 | Initial Release |