---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-218153-troubleshoot-incoming-call-problems-for-h-08d8c245c0
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for.html
retrieved_at: 2026-09-27T15:15:00.894624+00:00
---

Troubleshoot Incoming Call Problems for Webex Calling Users

# Troubleshoot Incoming Call Problems for Webex Calling Users

### Download Options

Updated: September 7, 2022

Document ID: 218153

Contents

## Contents

## Introduction

This document describes the most common configuration issues faced with incoming calls for Webex Calling customers.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Calling

- Control Hub (CH) .Ensure you have Admin Access.

- Cisco User Portal (CUP)

## Background Information

You have 3 differents choices to enable the PSTN with Webex Calling services :

- Cloud connected PSTN . This option looks for a cloud PSTN solution from one of the many Cisco CCP partners, or if the Cisco Calling Plan is not available in your location.

- Cisco Calling PSTN . You choose this option if you would like a Cloud PSTN solution from Cisco.

- Premises-based PSTN (Local Gateway) . You can choose this option if you want to keep your current PSTN provider, or you want to connect non-cloud sites with cloud sites.

As Webex Calling solution has different PSTN options, this document is not focused on PSTN interconnection troubleshoot issues. The suggestions are related to Webex Calling users configurations and those apply for any PSTN interconnection.

## Common Configuration Issues

### Validation of Hardphone or Softclient Registration

It is mandatory to have at least one hardphone or softclient registered.

Hardphone registration

Step 1. In Control Hub, select Devices

Step 2. Select [Your-device]

Step 3. In Device Management tab, ensure the status is Reg .

Webex Teams PC/Mobile

Mobile

You must log in and Select Settings > Calling > Phones services . The status must be Connected.

PC

You must log in and Select Settings >Phones services . The status must be Connected.

### Main Number Assigned

It is mandatory to have the main number assigned.

Step 1. In Control Hub, select Calling

Step 2. Select the Locations tab

Step 3. Select [Location-name]

Step 4. Ensure you have a Number assigned in Main Number section.

Note : If your Location does not have any Main Number assigned, the warning message, You will not be able to make or receive calls until this number is added is shown.

### Number Activated and Assigned

It is mandatory to have the number activated and assigned to a user.

Step 1. In Control Hub, select Calling

Step 2. Select the Numbers tab

Step 3. Select [Your-number]

Verify that the status is Active and this is Assigned To any user.

Note : If user is an extension only, the status is Not Applicable .

### Call Forwarding Configuration

Verify you do not have call forwarding activated.

Step 1. In Control Hub, select Users

Step 2. Select [Your-user]

Step 3. Select Calling tab

Step 4. Verify Call forwarding is turned off

### Voicemail Settings

Verify the voicemail settings related to your user.

Step 1. In Control Hub, select Users

Step 2. Select [Your-user]

Step 3. Select Calling tab

Step 4. Select Voicemail

Step 5. Verify the All calls to voicemail box is unchecked.

Step 6. Verify Number of rings before playing the "no answer" message configuration.

Note : The minimum value in the section Number of rings before playing the "no answer" message in Control hub is 2. In CUP, Call settings > Incoming Calls > Call forwarding > When no answer > Number of rings before forwarding , the minimun value is 0. Ensure you check this setting in both portals.

### Incoming Dial Plans

Review the incoming plans configuration.

Step 1. In Control Hub, select Users

Step 2. Select [Your-user]

Step 3. Select Calling tab

Step 4. Select Advanced Call Settings

Step 5. Select Outgoing and Incoming Permissions

Step 6. Select Incoming Calls

Step 7. Validate the toggle is disabled

### Call Intercept

Review call intercept configuration.

Step 1. In Control Hub, select Users

Step 2. Select [Your-user]

Step 3. Select Calling tab

Step 4. Select Advanced Call Settings

Step 5. Verify Call Intercept is off

### Single Number Reach (Office Anywhere) Configuration

Ensure single number reach (office anywhere) is disabled.

Step 1. In CUP, select Call settings

Step 2. Select Incoming Calls

Step 3. Verify the toggle Single Number Reach (Office Anywhere) is disabled.

### Do not Disturb Configuration (DND)

Ensure DND is disabled.

Step 1. In CUP, select Call settings

Step 2. Select Incoming Calls

Step 3. Verify the Do Not Disturb toggle is disabled.

## What is next?

After you review these configurations, if you have any issues, open a case with TAC.

You must add this information:

- Your OrgID

- Specific number with the issue

- Specific symptom experienced: fast, busy, specific recording, and so on.

- Provide a call example: caller, callee, timestamp, with your current TimeZone.

### Revision History

1.0

07-Sep-2022

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 07-Sep-2022 | Initial Release |

## Figuras

![Background Information for Webex Calling](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-00.png)

![Webex Control Hub - Devices - Phones](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-01.png)

![Webex Control Hub - Phones - Users](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-02.png)

![Phone Services Account](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-03.png)

![Webex Control Hub - Locations - Headquarters](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-04.png)

![Webex Control Hub - Main Number](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-05.png)

![Webex Control Hub - Calling - Numbers](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-06.png)

![Webex Control Hub - Users - User 1](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-07.png)

![Webex Control Hub - User 1 - Call Forwarding](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-08.png)

![Webex Control Hub - Users - User 1](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-09.png)

![Webex Control Hub - User 1 - Voicemail](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-10.png)

![Webex Control Hub - User 1 - Send Calls to Voicemail](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-11.png)

![Webex Control Hub - Users - User 1](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-12.png)

![Webex Control Hub - Users - Advanced Call Settings](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-13.png)

![Webex Control Hub - Users - User 1 - Outgoing and Incoming Calls](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-14.png)

![Webex Control Hub - Users - User 1 - Incoming Calls](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-15.png)

![Users - User 1 - Incoming Calls Turned On](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-16.png)

![Webex Control Hub - Users - User 1](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-17.png)

![Webex Control Hub - Users - Advanced Call Settings](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-18.png)

![Webex Control Hub - User 1 - Call Intercept](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-19.png)

![Cisco Webex Calling - Call Settings - Single Number Reach](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-20.png)

![Cisco Webex Calling - Call Settings - Do Not Disturb](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/webex-calling/218153-troubleshoot-incoming-call-problems-for-21.png)