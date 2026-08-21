---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-116517-problem-jabber-00-html-f1581a9699
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/116517-problem-jabber-00.html
retrieved_at: 2026-08-21T07:00:11.025597+00:00
---

Jabber for Windows Issue with Voicemail Credentials

# Jabber for Windows Issue with Voicemail Credentials

Updated: September 23, 2013

Document ID: 116517

Contents

## Contents

## Introduction

This document describes a problem encountered when you set up Cisco Jabber for Windows in order to access Voicemail messages, and offers a solution to the problem.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Call Manager (CCM) Version 9.1.1

- Cisco Unity Connection (UC) Version 9.x

- Cisco Unified Presence (CUP) Version 9.1.1

- Cisco Jabber for Windows Version 9.2.x

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Problem

At times, you might have Jabber set up for users to enter their UC credentials. In order to manually enter credentials on Jabber, navigate to File > Options > Phone accounts > Voicemail. Once you populate the Username and Password fields and click Apply , a spinning circle displays, and you never receive a success or failure message.

Note : In order for the Phone Accounts tab to display, you must complete these steps in CCM under the Service Profile you have set up. Navigate to User Management > User Settings > Service Profile . Select the profile that you previously built. Under Voicemail Profile, you must set Credentials source for voicemail service to Not set . Also, under MailStore Profile, you must populate at least the Primary field with a MailStore . If you do not complete these steps, then the Phone Accounts tab does not display in Jabber.

## Solution

If the authentication message in Jabber for Windows continues to spin endlessly, open UC and complete these steps:

- Navigate to Users > <select the user who wants to log into Jabber> > Edit > Password Settings .

- From the drop-down menu under heading Choose Password , change the selection from Voicemail to Web Application .

Note : The User Must Change at Next Sign-in setting is often the default setting in User Templates, so it is automatically applied to newly created or newly imported users. It might be a good idea change this in the User Templates as well in order to avoid future problems.

- Once you have unchecked the setting, exit Jabber.

- Return to the sign in page, and complete the process again. This time, authentication should work.

### Revision History

1.0

23-Sep-2013

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 23-Sep-2013 | Initial Release |