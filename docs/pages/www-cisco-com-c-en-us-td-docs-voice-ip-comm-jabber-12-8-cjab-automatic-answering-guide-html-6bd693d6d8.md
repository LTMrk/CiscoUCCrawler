---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-8-cjab-automatic-answering-guide-html-6bd693d6d8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_8/cjab_automatic-answering-guide.html
retrieved_at: 2026-08-21T07:00:56.619174+00:00
---

Set Up Automatic Answering for Cisco Jabber for iPhone and iPad

# Set Up Automatic Answering for Cisco Jabber for iPhone and iPad

### Download Options

Updated: April 24, 2020

First Published: April 2, 2020

Last Updated: April 24, 2020

## Overview

This guide shows you how to set up Cisco Jabber for iPhone and iPad to automatically answer incoming Jabber calls with voice
                  and video turned on. Ordinarily, users need to tap a button to accept incoming calls. Automatic answering removes this requirement,
                  which allows callers to start video calls with users who are unable to use the app by themselves.

Jabber's automatic answering feature uses Guided Access, an accessibility feature in iOS that limits a device to a single
                  app. When configured correctly in a Guided Access session, Jabber can automatically answer incoming video calls, even from
                  the lock screen.

Automatic answering works best when Apple Push Notifications are enabled. For information on how to turn on push notifications,
                  see the guide Feature Configuration for Cisco Jabber .

To set up automatic answering, you will need to complete these tasks:

Add the AutoAnswerForGuidedAccess Configuration Parameter

Turn on Guided Access

Start a Guided Access Session with Jabber

Turn On Automatic Answering

## Add the AutoAnswerForGuidedAccess Configuration Parameter

You need to add the AutoAnswerForGuidedAccess parameter to the client configuration file. This parameter adds the Auto Answer toggle in the client settings.

Add the AutoAnswerForGuidedAccess parameter to the jabber-config.xml file with a value of true . If you use the Unified CM Administration interface to configure Jabber, you may need to add the AutoAnswerForGuidedAccess parameter as a custom parameter.

Example:

### Example:

```
<AutoAnswerForGuidedAccess>true</AutoAnswerForGuidedAccess>
```

## Turn On Guided Access

Go to Settings > Accessibility > Guided Access , and toggle Guided Access to on.

Tap Passcode Settings , and then select Set Guided Access Passcode.

Enter a passcode for your Guided Access sessions, and then re-enter the passcode to confirm.

## Start a Guided Access Session with Cisco Jabber

Open the Cisco Jabber app.

On devices without a home button, triple-click the side button. On devices with a home button, triple-click the home button.

Tap Start to begin the Guided Access session.

## Turn on Automatic Answering

Jabber needs to have connected at least one phone call before automatic answering can work correctly. If you're on a fresh
                                 installation of the Jabber app, make a phone call before you turn on automatic answering.

Tap your profile picture, and then go to Settings > Call Option .

Toggle Auto Answer to on.

### This Document Applies to These Products

- Jabber for iPhone and iPad

| Add the AutoAnswerForGuidedAccess parameter to the jabber-config.xml file with a value of true . If you use the Unified CM Administration interface to configure Jabber, you may need to add the AutoAnswerForGuidedAccess parameter as a custom parameter. Example: <AutoAnswerForGuidedAccess>true</AutoAnswerForGuidedAccess> |
|---|

| Step 1 | Go to Settings > Accessibility > Guided Access , and toggle Guided Access to on. |
|---|---|
| Step 2 | Tap Passcode Settings , and then select Set Guided Access Passcode. |
| Step 3 | Enter a passcode for your Guided Access sessions, and then re-enter the passcode to confirm. |

| Step 1 | Open the Cisco Jabber app. |
|---|---|
| Step 2 | On devices without a home button, triple-click the side button. On devices with a home button, triple-click the home button. |
| Step 3 | Tap Start to begin the Guided Access session. |

| Note | Jabber needs to have connected at least one phone call before automatic answering can work correctly. If you're on a fresh
                                 installation of the Jabber app, make a phone call before you turn on automatic answering. |
|---|---|

| Step 1 | Tap your profile picture, and then go to Settings > Call Option . |
|---|---|
| Step 2 | Toggle Auto Answer to on. |