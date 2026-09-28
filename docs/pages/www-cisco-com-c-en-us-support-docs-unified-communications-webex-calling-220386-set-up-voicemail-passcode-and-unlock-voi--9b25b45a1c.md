---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-220386-set-up-voicemail-passcode-and-unlock-voi--9b25b45a1c
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/220386-set-up-voicemail-passcode-and-unlock-voi.html
retrieved_at: 2026-08-21T07:12:32.522227+00:00
---

Set-up Voicemail Passcode and Unlock Voice Portal

# Set-up Voicemail Passcode and Unlock Voice Portal

### Download Options

Updated: April 12, 2023

Document ID: 220386

Contents

## Contents

## Introduction

This document describes the basic functionality of the Voice portal PIN and Passcode and how to have the Voice portal unlocked.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Basic understanding of features such as Voice portal, Location, and Voicemail

- Have admin roles in the organization

- Have a clear understanding of what needs to be configured

- Active Telephone Number (TN) assigned to the desired features

### Components Used

The information in this document is based on Control Hub.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

This document describes the steps and clarifications required to have a user unlock the voice portal.

Voice portals provide an Interactive Voice Response (IVR) system so administrators can manage Auto Attendant announcements. Users from the location can call in and access their voicemail messages or change their passcode.

A Webex Calling user has the option to verify their voicemail messages by either with a call to the voice portal number set for the Location they reside or press the voicemail button on their desktop phone.

Note: The users have the option to check voicemail messages on the User portal, where they are also able to configure voicemail settings. For further details you can visit: Configure your voicemail settings in the User Portal .

## Voice Portal and Voicemail

You can review the concepts you must understand when it comes to voice portals.

### Voice Portal

When you activate this service, you are to receive an email that contains your voice portal number. Call this phone number to record your auto attendant greetings. This is also the phone number users at this location call to access their voicemail messages and settings.

The voice portal is a service that is automatically enabled when you create a Location. Administrators must choose a number or/and extension so the service works properly.

For further details. please visit Configure voice portals for Webex Calling in Control Hub .

### Voice Portal Passcode

Administrators must only have access to this passcode.

Administrators can enter the voice portal phone number and passcode configured here to manage auto attendant greetings and mailbox settings. Users can also use this option when they call from a number that is not their assigned number.

In order to set this Passcode, you must navigate to Locations > Calling > Voice Portal as shown in this image.

Note: The user enters their Voicemail PIN password to access their own mailbox when they call from their own number and/or extension. Entry of the admin passcode for this option is the failure to gain access to the voice portal.

### Default Voicemail Passcode

As an administrator, you can assign a default passcode to new users.

If you choose to set a default passcode for the new users added to your organization, communicate to your users what that passcode is, and that it must be reset through their device or app before they can access their voicemail.

If this feature is not turned on, each new user must initially set their own passcode on Webex Settings .

In order to set this feature, you must navigate to Calling > Service Settings .

Note: Once you turn this feature on, all new users created after this must use this default passcode when they access their voice portals for the first time. Users created prior to this change, must continue to use their current passcodes.

## Access to your Voice Portal

You have the option to access your voicemail in one of the presented ways:

- You can call the Voice portal number/extension from the Location you reside in, from your desktop phone or Webex app.

- If you have a Cisco IP Phone, you can click the voicemail button (for further details, visit: https://help.webex.com/en-us/article/nhved1q/Check-Your-Voicemail ).

- You can check the voicemail messages through Webex Settings . Click the Webex Calling tab and it takes you to User Portal . Then click Voicemail tab.

Note: I f you do not know your voice portal phone number from your location, ask your administrator.

Once you access the voice portal, you hear the next prompt:

"Welcome to your Webex Voice Portal. Please enter your passcode, then enter the pound key (#). If you are not calling from your own phone, please press the star key (*)."

The passcode you enter in this step can be different and depends on the presented scenarios.

#### Scenario 1

You are a new user that calls for the first time to your voice portal.

If your administrator provided you with a Passcode set at the organization level (view Default Voicemail Passcode section), you must use that.

Once you have entered the Default passcode, you are prompted with the next message for you to configure your new and personalized passcode:

"Before you can use your voice portal, you must change your passcode and record your personalized name. Please enter your new passcode, then press the pound key."

You are then prompted to record your personalized name.

This passcode is the one you must use from now on when you access your voice portal through your phone.

#### Scenario 2

You are a new user that has not configured the voice portal yet.

You can also be a new user and change the default in the Webex Settings portal.

For further details, please visit: Set up and manage your voicemail .

Note: In this context, the passcode concept is the same as Voicemail PIN.

After you have set your passcode in Webex Settings , you are now able to access your voice portal. You are prompted with the message so you configure your personalized name.

#### Scenario 3

Your user exists and you have set your passcode in the past.

If your user has been configured with a passcode already, you must use that one.

It is recommended to have it noted so you do not forget it.

If you enter an invalid passcode up to 4 times, your voice portal is locked.

## Voice Portal Locked

You as the user can face a common issue when you attempt to check your voicemail, and after you enter your passcode, you hear the next error message:

"Your voice portal access is locked out, please contact your group administrator to reset the passcode".

This error occurs when you have attempted to use an invalid passcode up to 4 times.

In this case, there are two ways to recover your passcode and unlock your voice portal:

1. If there is a Default Voicemail Passcode set by the administrator , you as the administrator can navigate to the user profile; Users > Calling > Voicemail > Voicemail PIN , and click Reset Voicemail PIN . This automatically unlocks the voice portal of the user and sets the passcode to the Default passcode. Users must use this one to access their voicemail and configure a new Passcode. They are prompted with the next message:

"Before you can use your voice portal, you must change your passcode and record your personalized name. Please enter your new passcode, then press the pound key".

2. You can navigate to Webex Settings and reset your own password in order to unlock their voice portal. You must click Reset voicemail PIN .

For further details, please visit: Set up and manage your voicemail .

After this, you can access your voice portal and use this new PIN and immediately review your voicemail box as usual.

## Related Information

### Revision History

1.0

12-Apr-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 12-Apr-2023 | Initial Release |