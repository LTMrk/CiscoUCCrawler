---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-200198-configuring-dial-via-office-reverse-to-w-htm-c11200e0e0
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/200198-Configuring-Dial-via-Office-Reverse-to-W.html
retrieved_at: 2026-08-16T21:58:12.419167+00:00
---

Configuring Dial via Office-Reverse to Work with Mobile and Remote Access

# Configuring Dial via Office-Reverse to Work with Mobile and Remote Access

### Download Options

Updated: October 29, 2015

Document ID: 200198

Contents

## Contents

## Introduction

This article describes how to configure the Dial via Office-Reverse (DVO-R) feature on Cisco Unified Communications Manager and Cisco Jabber for Android or iPhone to work via Cisco Expressway Mobile and Remote Access.

## Prerequisites

### Requirements

- Cisco Unified Communications Manager 11.0(1a) SU1 (or later)

- Cisco Jabber for Android or Cisco Jabber for iPhone 11.1 (or later)

- Cisco Expressway X8.7

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Unified Communications Manager 11.0(1a) SU1 (or later)

- Cisco Jabber for Android or Cisco Jabber for iPhone 11.1 (or later)

- Cisco Expressway X8.7

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

### Set up DVO-R

To set up DVO-R, you must do the following:

Note : Before configuring and enabling DVO-R, verify that your Cisco Jabber mobile client can register and make a call to an enterprise extension over the Cisco Expressway MRA connection.

### Set up Cisco Unified Communications Manager to Support DVO-R

To set up Cisco Unified Communications Manager to support DVO-R, complete the following steps:

- Set up an Enterprise Feature Access Number.

- Verify that you have the correct Device COP File Version. See the Cisco Jabber for Android Release Notes or the Cisco Jabber for iPhone Release Notes for the version you are running.

- If necessary, make appropriate dial plan changes to allow the system to route calls to the Mobile Identity phone number to the outbound gateway. Ensure that the format of the number is appropriate for call routing in line with your dial plan.

#### Set up an Enterprise Feature Access Number

Use this procedure to set up an Enterprise Feature Access Number (EFAN) for Cisco Jabber DVO-R calls.

Note : When you call someone using DVO-R, the Caller ID received by the called person is your enterprise number and not the EFAN. The EFAN is only used as the caller ID for the callback leg to the Mobile Identity or Alternate Number.

- Open the Cisco Unified CM Administration interface.

- Select Call Routing > Mobility > Enterprise Feature Access Number Configuration .

- Select Add New .

- In the Number field, enter the EFAN. Enter a DID number that is unique in the system. To support dialing internationally, you can prepend this number with \+.

- In the Description field, enter a description of the Mobility EFAN.

- (Optional) Check the Default Enterprise Feature Access Number check box if you want to make this EFAN the default for this system.

- Select Save .

Note : It is also possible to set up a Mobility Profile for Cisco Jabber devices (optional if you have already configured a default EFAN). Mobility profiles allow you to set up the DVO-R settings for a mobile client. After you set up a Mobility Profile, you can assign it to a user or to a group of users, such as the users in a region or location. For more information, see the Cisco Jabber Deployment and Installation Guide for your release.

### Set up DVO-R for each Device

Use the following procedures to set up DVO-R for each TCT or BOT device.

- Add a Mobility Identity to the dual-mode device associated to each user.

- Enable DVO-R on Each Device on the dual-mode device associated with each user.

- If you enable Single Number Reach (optional), verify that it works. Dial the desk phone extension and check that the phone number that is specified in the associated mobile identity rings.

#### Add Mobility Identity

Note : Use this procedure to add a Mobility Identity to specify the number of the mobile device as the destination number. You can specify only one number when you add a Mobility Identity. If you want to specify an Alternate Number, such as a second mobile phone number, you can set up a remote destination. The Mobility Identity configuration characteristics are identical to those of the Remote Destination configuration.

- Open the Cisco Unified CM Administration interface.

- Select Device > Phone .

- Search for the BOT or TCT device that you want to configure.

- Select the device name to open the Phone Configuration window.

- In the Associated Mobility Identity section, select Add a New Mobility Identity .

Note : If you enable DVO-R for a user, you must enter a destination number for the user's Mobility Identity.

- Set the Dial-via-Office Reverse Voicemail Policy to User Control .

- Check the Enable Single Number Reach check box.

- Leave the Ring Schedule at All the time or set up the schedule for routing calls to the mobile number at specific times and/or on specific days.

- Select Save .

The below diagram outlines the required Mobility Identity configuration for an Android device.

The below diagram outlines the required Mobility Identity configuration for an iPhone device.

#### Enable DVO-R on Each Device

- Open the Cisco Unified CM Administration interface.

- Select Device > Phone.

- Search for the BOT or TCT device that you want to configure.

- Select the device name to open the Phone Configuration window.

- In the Protocol Specific Information section, in the Rerouting Calling Search Space drop-down list, select a Calling Search Space (CSS)  that can route the call to the DVO-R callback number.

- In the Product Specific Configuration Layout section, set the Dial via Office drop-down list to Enabled .

- Select Save .

- Select Apply Config .

- Instruct the user to sign out of the client and then to sign back in again to access the feature.

The below two diagrams outline how to configure Dual Mode for an Android device and enable DVO-R.

The below two diagrams outline how to configure Dual Mode for an iPhone device and enable DVO-R.

### Set up Single Number Reach (Optional)

Single Number Reach (SNR) allows the native mobile phone number to ring when someone calls the work number if:

- Cisco Jabber is not available. After Jabber becomes available again, and connects to the corporate network, Cisco Unified Communications Manager returns to placing VoIP calls rather than using SNR.

- The user selects the Mobile Voice Network calling option.

- The user selects the Autoselect calling option and the user is outside of the Wi-Fi network.

Note : While SNR can enhance the user experience, it is not required for DVO-R to work.

To set up SNR you must complete the following:

- Enable Single Number Reach.

- Add Mobility Identity.

- Add Remote Destination (optional).

- Test your connection.

#### Enable Single Number Reach

Use the following procedure to enable SNR for an end user.

- Open the Cisco Unified CM Administration interface.

- Select Device > Remote Destination .

- Search for the destination number.

- Delete the destination number.

- Select User Management > End User .

- Search for the end user.

- Select the User ID to open the End User Configuration window.

- In the Mobility Information section, check the Enable Mobility check box.

- Select Save .

- Navigate to Device > Phone .

- Search for the BOT or TCT device that you want to configure.

- Select the device name to open the Phone Configuration window.

- Softkey Template: Choose a softkey template that includes the Mobility button. For information about setting up softkey templates, refer to the Cisco Unified Communications Manager Administration Guide for your release (see  the Related Information section or the below diagram for more information).

- Mobility User ID: Select the user.

- Owner User ID: Select the user. The value must match the mobility user ID.

- Rerouting Calling Search Space: Choose a Rerouting Calling Search Space that routes to the mobile phone number.

- Select Save .

Note : Cisco Jabber allows users to specify a callback number for DVO-R calls that is different from the mobile phone number of the device, and the Rerouting Calling Search Space controls which callback numbers are reachable. If the user sets up the DVO-R Callback Number with an Alternate Number, ensure that you set up the dial plan to route calls to the Alternate Number.

The below two diagrams outline how to complete the configuration for an end user.

### Add Remote Destination (Optional)

Use this procedure to add a Remote Destination and specify an additional number as the destination number. The Mobility Identity configuration characteristics are identical to those of the Remote Destination configuration. Additional remote destinations can be any type of phone number, such as home phone numbers, conference room numbers, or multiple mobile phone numbers for additional mobile devices. You can add more than one remote destination.

- Open the Cisco Unified CM Administration interface.

- Select Device > Phone .

- Search for the BOT or TCT device that you want to configure.

- Select the device name to open the Phone Configuration window.

- In the Associated Remote Destinations section, select Add a New Remote Destination .

- Enter the desired phone number as the Destination Number . You must be able to route the number to an outbound gateway. Generally, the number is the full E.164 number.

- Enter the initial values for the following call timers. For more information, see the online help in Cisco Unified Communications Manager.

- Check the Enable Single Number Reach check box.

- Set up the schedule for routing calls to the mobile number at specific times and/or specific days.

- Select Save .

### Set up User-Controlled Voicemail Avoidance

Note : To prevent the callback leg from Cisco Unified Communications Manager routing to your voicemail — thus stopping the voicemail call going through to the person you are dialing — Cisco recommends that you set your DVO-R voicemail policy to ‘user controlled’. This ensures you must generate a DTMF tone by pressing any key on the keypad before your call can proceed.

Caution : When enabling user-controlled voicemail avoidance, DTMF must be successfully propagated from the carrier to Cisco Unified Communications Manager in order for users to make DVO-R calls.

Use this procedure to set up Cisco Unified Communications Manager to support user-controlled voicemail avoidance.

- Navigate to the Mobility Identity configuration page ( see Add a Mobility Identity ).

- Check that Dial-via-Office Reverse Voicemail Policy is set to User Control .

The below diagram shows how to enable DTMF-based features.

### Configure Cisco Jabber Client Settings

Under settings in your Cisco Jabber client, set your calling options to Mobile Voice Network (or Autoselect) and set a DVO-R callback number.

The callback number will automatically be populated with the number configured as Mobility Identity within Cisco Unified Communications Manager. For DVO-R with callback to an Alternate Number, the user-configured Alternate Number is used. The selected number will be the number that is called when making DVO-R calls.

The below diagram outlines how to configure Cisco Jabber for Android for DVO-R.

The below diagram outlines how to configure Cisco Jabber for iPhone for DVO-R.

## Verify

The below diagram shows the client call flow for DVO-R - using Mobility identity - once it has been set up correctly on Cisco Jabber for Android.

The below diagram shows the client call flow for DVO-R -  using Alternate Number - once it has been set up correctly.

The below diagram shows the client call flow for DVO-R - using Mobility identity - once it has been set up correctly on Cisco Jabber for iPhone.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

## Related Information

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- Remote Access

- TelePresence Video Communication Server (VCS)