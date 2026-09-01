---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-meetings-214861-exception-meetings-on-google-calendar-html-5ee57c8dd0
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-meetings/214861-exception-meetings-on-google-calendar.html
retrieved_at: 2026-09-01T14:56:45.772115+00:00
---

Exception meetings on Google Calendar

# Exception meetings on Google Calendar

### Download Options

Updated: September 20, 2019

Document ID: 214861

Contents

## Contents

## Introduction

This document describes how to avoid creating several instances of the same meeting on "My Meetings" calendar if those were scheduled on Google Calendar

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of:

- Cisco Webex.

- Integration with Google Calendar.

### Components Used

This document is not restricted to specific software, however, the information in this document is based on Google Chrome Version 76.0.3809.132 (Official Build) (64-bit)

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

One of the requirements to use this document is for the Webex Site to have a working integration with Google Calendar on the gsuite.

This document is created in order to provide detailed steps on how several exception meetings can be created on a production environment.

## Problem

One meeting in WebEx is displaying multiple times for the same date and time on My WebEx Meetings .

### Steps to duplicate the problem

Step 1. Host schedules a recurrent meeting via Google calendar.

Step 2. The meeting is scheduled correctly, visible on Google calendar and Webex calendar.

Step 3. Host edits the meeting. Added a room resource, change date, etc.

Step 4. Select This and following events , click OK .

Step 5. On the Google Calendar, there is a new meeting number with the updated details. This is expected.

Step 6. On My Meetings Calendar, there are two instances of the same meeting with different details and meeting number.

#### Example on Test Meeting 1

Host schedules a recurrent meeting via Google calendar. Scheduled Weekly on Monday. Meeting number ending on 153, as shown in the image below.

Host edits the meeting. Modified the Location from Almagro Cave 2 to Shijo, as shown in the image below.

Select This and following events.

On the Google Calendar, there is a new meeting number with the updated details, as shown in the image below.

On My Webex Meetings, there are two instances of the same meeting

Although such meetings do not have the same meeting number, which means they are different meetings.

## Solution

After update a recurrent meeting in Google Calendar and select This and following events option, this causes a meeting exception.

With this action, Google sets that meeting and all future meetings as a meeting exception to the series which causes Google to change the uid in the calendar invite and causes to see it as a new meeting.

In the image below, the instances of a recurrent meeting are shown graphically.

On the 9th instance, it is described how the meeting is edited while select This event , only one exception is created.

On the 11th instance, the meeting is edited while select This and following events , which creates an exception to the series which causes Google to change the uid in the calendar invite.

If you choose This event or All Events, Google does not send this as a new meeting invite to invitees and updates the existing meeting.

This does not appear to be a Webex integration issue but rather how Google calendar handles the event update and how they generate/update the calendar invites which get sent to non-Google users.

As a workaround, if the host chooses one of the other options (This event or All events) the issue does not occur.

### Contributed by Cisco Engineers

Erika Radillo

Cisco TAC Engineers

O'Bryan Stull

Cisco TAC Engineers

### This Document Applies to These Products

- WebEx Meetings