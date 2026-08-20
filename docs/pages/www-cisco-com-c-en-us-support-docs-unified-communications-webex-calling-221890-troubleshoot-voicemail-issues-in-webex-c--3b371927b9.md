---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-221890-troubleshoot-voicemail-issues-in-webex-c--3b371927b9
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/221890-troubleshoot-voicemail-issues-in-webex-c.html
retrieved_at: 2026-08-20T23:21:32.574402+00:00
---

Troubleshoot Voicemail Issues in Webex Calling

# Troubleshoot Voicemail Issues in Webex Calling

### Download Options

Updated: April 15, 2024

Document ID: 221890

Contents

## Contents

## Introduction

This document describes the most common issues faced with the Voicemail feature in Webex Calling (WxC).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Calling

- Control Hub

- User Hub

### Components Used

This document is not restricted to specific hardware and software version. The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

The Voice Portal is a Calling service that provides an Interactive Voice Response (IVR) that allows administrators to manage automated attendant announcements within the Organization's Location. The phone number or extension set for a Location's Voice Portal is the number that users at that specific Location call to access their Voicemail messages and settings.

The Extended Away Greeting is a feature that allows you to record a new greeting to be heard after the set number of rings set for the user and disable the deposit of new voicemails.

## Common Voicemail Issues

### Ensure Voice Portal Number or Extension is Set for the Location in Control Hub

Step 1 . Click the Location for the users facing the issue.

Step 2. Click Calling .

Step 3. In Calling features settings , click Voice Portal .

Calling Features Settings

Step 4. In Incoming Call , add a Phone Number available from the drop-down menu in the Location or an Extension or both.

Incoming Call

Step 5. Click Save and try to leave a new voicemail.

### Ensure the User has the Voicemail Feature Enabled

Step 1. Under MANAGEMENT , click Users .

Step 2. Click the User.

Step 3. Click Calling .

Step 4. Under Voicemail, fax, announcement language and timezone , click Voicemail .

Voicemail, Fax, Announcement Language and Timezone

Step 5. Click the toggle to enable Voicemail for the user.

Enable Voicemail at User Level

Step 6. Click Save .

### Ensure the Extended Greeting Away is Disabled

Step 1. Call your Location's Voice portal.

Step 2. Enter your Passcode PIN followed by the Pound Key.

Note : Your Pass code is the same as your Voicemail PIN, usually a 6 digit number set by the user or administrator.

Step 3. Press 1 to access your voice mailbox .

Step 4. Press 4 to access the Extended Away Greeting menu.

Step 5. Press 2 to deactivate your Extended Away Greeting .

### User Locked Out of Voicemail

If a user is unable to access their Voicemail because they have been locked out of it, the user can reset their Voicemail PIN in the User Hub.

Step 1. Log in with the User credentials in User Hub .

Step 2. Click Settings > Calling > Voicemail .

Step 3. Click Voicemail PIN > Reset voicemail PIN .

Voicemail PIN

Step 4. Enter a new Voicemail PIN that meets the requirements.

Reset Voicemail PIN

Step 5. Click Save and try a new Log in attempt.

### Voicemail Transcription Not Arriving at User's Email

#### Ensure the User has Use Internal Mailbox as Message Storage

Step 1. Under MANAGEMENT > Users , and click the User .

Step 2. Click Calling > Voicemail, fax, announcement language and timezone > Voicemail .

Step 3. Under Message storage , click Use Internal Mailbox .

Use Internal Mailbox

Step 4. Click Save .

#### Ensure the Correct Language is Selected in the User Set Up for Transcription

The supported Languages for Voicemail transcription are English, German, Spanish, French. For the Voicemail transcription service to recognize the Language and transcribe it, the desired Language must be selected in the user configuration.

Step 1. Under MANAGEMENT > Users , and click the User .

Step 2. Click Calling > Voicemail, fax, announcement language and timezone > Voicemail .

Step 3 . Click Announcement Language .

Step 4. From the drop-down menu, click the desired Language to be transcribed.

Announcement Language

## Recommended Information for a TAC Case

If an issue persists after the troubleshoot steps in this document have been performed and a TAC case is needed, Cisco recommends to include this information:

- Organization ID

- Location ID or Location Name

- User's Number, extension and mail

- Caller number - Callee number - Time zone and Timestamp

- A detailed description of the issue experienced

## Related Inform atio n

### Revision History

1.0

15-Apr-2024

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 15-Apr-2024 | Initial Release |