---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-room-kit-eq-221037-configure-mtr-device-to-join-third-party-h-2c0c2818bf
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/room-kit-eq/221037-configure-mtr-device-to-join-third-party.html
retrieved_at: 2026-08-21T12:48:43.832683+00:00
---

Configure MTR Device to Join Third Party Meetings (OBTP)

# Configure MTR Device to Join Third Party Meetings (OBTP)

### Download Options

Updated: July 24, 2026

Document ID: 221037

Contents

## Contents

## Introduction

This document describes how to configure a Cisco Microsoft Teams Room (MTR) device to join third party meetings using one button to push (OBTP)

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Knowledge of Onboarding Cisco Endpoints to MTR

- Knowledge of Microsoft PowerShell

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Codec Pro September Stable version, fully onboarded into Microsoft Teams as an MTR device (or dual registered with Webex Control hub).

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

When your Cisco device is setup in MTR mode, only meetings for Microsoft Teams are presented with a OBTP join option by default. To see join buttons for Webex or Zoom meetings, there are some additional steps needed to achieve this. Without performing these steps, the display can show the meeting information without a join option or it can show no meeting details at all.

## Configure the Device and Resource Mailbox

### Device Configurations

There are two considerations for device configurations:

1. The resource account must be able to process the third-party meeting invite.

2. The device must be enabled to join third-party (Webex and Zoom) meetings.

For number 2, there is a setting on the device when it is running the MTR experience where you must toggle On . This allows it to show the Join button for Webex and Zoom meetings.

To locate and change this setting:

- Navigate to the Home screen of the MTR device.

- Navigate to More > Teams Admin Settings .

- By default, the MTR settings are locked, so they must be unlocked first. If the device is in MTR Only mode, the password is created by the administrator during setup.

Device Settings Teams Admin Settings

- If the device is dual registered (Teams and Webex Control Hub), unlock the settings menu from the Control Hub under All > UserInterface > SettingsMenu > Mode > Cisco Room Bar and select Unlocked .

Control Hub Device Settings Menu

- With the settings menu unlocked, navigate to Meetings > Third party meetings and enable Webex and/or Zoom:

Settings Menu - MTR

## Resource Mailbox Configurations

To change the calendar processing attributes in Office 365, an exchange admin must connect using PowerShell and run this PowerShell command:

PowerShell command:

```
Set-CalendarProcessing -Identity “[ResourceName]” -AutomateProcessing AutoAccept -AddOrganizerToSubject $false -DeleteComments $false -DeleteSubject $false -ProcessExternalMeetingMessages $true -RemovePrivateProperty $false -AddAdditionalResponse $true - AdditionalResponse "This Is a Microsoft Teams Meeting room powered by a Cisco collaboration device!”
```

Some settings are suggested values, with processing third-party meetings, the most important attributes are DeleteComments $false and ProcessExternalMeetingMessages $true. The other attributes vary based on your organizations preferences.

## Troubleshooting

### See the Meeting Invitation but no Join Button

If you see the invite on the device but no join button, check the mailbox settings in Exchange and verify they are correct. Specifically, check calendarProcessing > DeleteComments .

This value must be false , however, by default, it is set to true when creating new resource mailboxes. Also, the third-party meeting support in the Settings > Meetings menu must be enabled.

### Cannot See the Meeting Invitation

If the third-party meetings are not showing at all, it is likely the resource mailbox is not processing the invite. Check the resource mailbox calendarProcessing configurations:

- DeleteComments must be set to false.

- ProcessExternalMeetingMessages must be set to true.

### Revision History

4.0

24-Jul-2026

Adding OBTP note for clarity that this is ONLY to get OBTP Join button on screen

3.0

01-Jul-2026

Updated spelling, spacing, grammar, tags, and CCW alerts.

2.0

02-Apr-2025

Updated Machine Translation, Style Requirements, and Formatting for Recertification.

1.0

05-Oct-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 4.0 | 24-Jul-2026 | Adding OBTP note for clarity that this is ONLY to get OBTP Join button on screen |
| 3.0 | 01-Jul-2026 | Updated spelling, spacing, grammar, tags, and CCW alerts. |
| 2.0 | 02-Apr-2025 | Updated Machine Translation, Style Requirements, and Formatting for Recertification. |
| 1.0 | 05-Oct-2023 | Initial Release |