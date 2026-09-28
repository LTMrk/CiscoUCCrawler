---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-wbxt-ucmcalling-unified-cm-wbx-teams-deployment-guide-uni-8cf1169245
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wbxt/ucmcalling/unified-cm-wbx-teams-deployment-guide/unified-cm-wbx-teams-deployment-guide_chapter_01.html
retrieved_at: 2026-08-16T22:00:05.212532+00:00
---

Deployment guide for Calling in Webex App (Unified CM)

# Deployment guide for Calling in Webex App (Unified CM)

Updated: November 10, 2025

Chapter: Overview of Calling in Webex App (Unified CM)

## Chapter: Overview of Calling in Webex App (Unified CM)

# Overview of Calling in Webex App (Unified CM)

## New and changed information

This table covers content updates related to new features or functionality, changes
                              to existing content, and any major errors that were fixed in the Deployment Guide
                                 for Calling in Webex App (Unified CM) .

For more information about Webex App updates, see the following documentation depending on the type of apps you're
                              deploying to your users:

For the standalone app —See the What's
                                       new documentation for major updates, and see the Release Notes for minor updates and bug fixes
                                    for Webex App .

For the VDI app —See the VDI release notes for major
                                    updates and limitations.

Date

Changes Made

November 2025

Included a note in the chapter "Deploy Calling in Webex App (Unified CM)", section "Service discovery options".

March 2025

Included "Limitation" and "Known Issues" in the "Centralized call history" section. Addressed a few changes to the steps in
                                          "Unified CM" section.

Changed the title of the section from "Multi Call Window" to "Calling Dock".

December 05, 2024

Included a new topic "Centralized Call History" in the "Unified CM feature requirements" section.

Included a new topic "Multi Line Support for Webex App  (Unified CM) on Mobile" in "Unified CM feature requirements" section.
                                          Addressed the following:

Extend the maximum number of phone lines from eight to ten on desktop Webex application.

Multi-line is supported on mobile with up to eight lines.

Updated the "Known issues and limitations with Calling in Webex App (Unified CM)" section.

Updated the "Dial Via Office Reverse" and "Move call to mobile" sections.

Updated "Table 2: Midcall calling features".

Updated the parameter "RemoteInUsePresencePrimaryLineOnly" in the "Appendix > Customization parameters".

April 24, 2024

Included a link to step 3 in the chapter "Deploy Calling in Webex App (Unified CM)" > section "Configure moving a call into
                                          a meeting".

April 22, 2024

New Parameter "ShowSelectiveCallRecordingButton" is added to  "Appendix" > "Policy Parameters" > "Feature Parameters" section.

July 03, 2023

New Parameter "EnableSIPURIDialling" is added to "Appendix" > "Policy Parameters" > "Feature Parameters" section.

New Parameter "LocalPushSSIDList" is added to "Appendix" > "Policy Parameters" > "Feature Parameters" section.

New Feature Name "Local Push Notification Service (LPNS)" along with "Note" is added to the "Deployment Features" table in
                                          the "Deployment Features" section.

Added a Note to "Overview of Calling in Webex App (Unified CM)" > "Calling features in Webex App" > "More information about
                                          Desk Phone Control (DPC)"  section.

April 29, 2023

Revamped the section "Set up calling behavior and UC manager profiles in Control Hub".

March 10, 2023

Changes to the section, "Location reporting for emergency calling". Redsky was the only E911 SP. Now, "Intrado" is integrated
                                          with E911 SP and is called "E911 SP Intrado".

October 18, 2022

In the section "Recommended configuration - SSO redirect URI", under "Requirements", replaced "Unified CM 12.5(x) releases-12.5(1)
                                          SU4 and later (Unified CM 14 is not supported)" to "Unified CM 12.5(x) releases-12.5(1) SU4 and Unified CM 14.0(x) releases-14.0(1)
                                          SU1 and later".

June 7, 2022

New feature "Multi call window" added to the Additional features table in the Overview > Calling features in Webex App section of this document.

Added Multi call window requirements to Prepare > Unified CM feature requirements

Added CucmCallBargeMode parameter to Appendix > Policy parameters > Feature parameters .

There is a new parameter ShowPhoneNumberInLineSelection in the configuration file, for displaying / hiding number in line selection dropdown menu. Added this parameter to the Customization parameters table in the Appendix to this document.

February 15, 2022

Changed the UI path for updating user or organization calling behavior in Control Hub (in the section "Set calling behavior and UC manager profiles in Control Hub" ).

Removed the note that explains "Auto cleanup and deletion of auto-provisioned devices is not supported currently" in Overview of Auto-Provisioning of Webex App .

December 13, 2021

Added prerequisites and a link to configuration steps for
                                                the Auto-Device Provisioning feature for Cloud-Connected
                                                UC.

Added RedSky emergency location reporting to the "Prepare Your Environment" chapter.

In the "Meeting join in desk phone control mode" section of the call flows, added the following
                                                clarifying text: "The meeting must be directly from a
                                                   space and take place only in the Webex App. Full
                                                   Featured Meetings are not supported."

In accordance with style guidelines, changed section
                                                titles from title case to sentence case.

October 5, 2021

In the Customize Parameters table in the Appendix, added
                                                the EnableADLockPrevention parameter.

September 7, 2021

In the Customize Parameters table in the Appendix, added
                                                the following parameters:

For emergency disclaimers:

E911NotificationFrequency

E911NotificationURL

For video settings:

EnableVideo

StartCallWithVideo

Added the following parameters for video settings:

In the Deployment features table, added the following
                                                entries:

Customize emergency dialing disclaimer

Disable video for all 1:1 calls

August 9, 2021

Added new entries to Additional Features:

Network Handoff (Wi-Fi to LTE)

Switch your call from Webex to your mobile phone
                                                      app

Added new section "Wi-Fi to LTE Call Network Handoff
                                                   " to Unified CM Feature Requirements in the Prepare
                                                Your Environment chapter.

Added new section "Configure Move Call to Mobile" to
                                                the deployment chapter.

In "Expressway Certificates (With MRA) " , added
                                                section for migrating Jabber to Webex and considerations
                                                for private CA certification.

In the Feature Parameters table in the Appendix, added
                                                the following parameters for call recording:

EnableRecordingTone

LocalRecordingToneVolume

NearEndRecordingToneVolume

RecordingToneDuration

RecordingToneInterval

In the Feature Parameters table in the Appendix, added
                                                EnableCallPark.

July 7, 2021

Added new section "Contact Center Feature
                                                   Requirements," including a link to Contact Center Integration for
                                                   Webex which lists the latest supported
                                                features.

For SSO Redirect URI, clarified that Unified CM 14.0 is
                                                not supported.

Updated logos in architecture diagrams to reflect new
                                                branding for the Webex app. (See New Webex Suite and Branding for more information.)

June 2, 2021

Added new section "Android Devices and
                                                   Density-Independent Pixels" to explain how Webex
                                                determines whether an Android device is a phone or a
                                                tablet.

Added new section "Configure Additional Features" to
                                                the deployment chapter.

Added new parameter "EnablePhoneDialerOptionOverMRA" to the Customization Parameters in the Appendix.

Added the following items to feature tables:

Added "Virtual Cameras" to the midcall
                                                      features table for desktop.

Added "Virtual Cameras (macOS)" to the
                                                      deployment features table.

Added "PSTN calling for mobile app users in
                                                         India" to the additional calling feature
                                                      table.

May 11, 2021

Added information about how Webex distinguishes Android
                                                phones from tablets by using the device's display dp
                                                (less than 600 for phones; 600 or greater for
                                                tablets).

Removed "Retain Hybrid Call Service for Users" from the
                                                Prepare Your Environment chapter because Hybrid Calling (Call Connector
                                                   architecture) will be End of Life (EOL) .

May 5, 2021

Added Chromebooks as supported devices when the TAB
                                                device type is used in Unified CM.

Added more information about configuring softphone
                                                devices on different platforms for the same user.

Added the following to the Additional Features table:

MRA failover (the minimum requirements (Unified
                                                      CM 14.0 and later, Expressway X14.0 and later) are
                                                      adde to the Call Control Environment Requirements
                                                      section)

Diagnostics in the Webex app

Fixed error in "Configure Moving a Call into a
                                                   Meeting" section: Telephony must be enabled for
                                                this feature to work.

Added more details about how to configure SSO Redirect
                                                URI on Expressway-C.

April 7, 2021

Added new section "Configure Move Call into a
                                                   Meeting" (Deployment chapter)

Added the following entries to the feature tables:

Move a Call into a Meeting (Midcall
                                                      Features—Desktop and Mobile)

In the Overview chapter, added more details about how
                                                Webex pulls configuration from Unified CM and the
                                                cloud.

Improved the architecture section.

March 3, 2021

Added minimum releases for APNs for China and non-China
                                                deployments.

Added Call Recording to the MidCall Features table.

In the Overview chapter, added architecture diagrams for
                                                internal and MRA deployments.

February 3, 2021

In the "Policy Parameters" section in the Index, added the following new parameters:

E911EdgeLocationWhiteList

EnableE911EdgeLocationPolicy

EnableE911OnPremLocationPolicy

In the "Prepare Your Environment" chapter, added new sections on Push Notifications, Location Monitoring, and Cisco Unified Survivable Remote Site Telephony
                                                (SRST).

Made the following changes to the Additional Features table:

For the Call History entry in the Additional Features table, added information about deleting call entries and the 200 call
                                                      over 30 days limit.

For the Suppress Notifications entry in the Additional Features table, added information about muting notifications during
                                                      a call or meeting.

Added Location Monitoring for desktop and mobile.

January 12, 2021

In the "Policy Parameters" section in the Index,
                                                added the following new parameters:

SoftPhoneModeWindowBehavior

DeskPhoneModeWindowBehavior

In the "Prepare Your Environment" chapter, added new
                                                section on Call Park configuration.

Made the following updates to the feature tables in the
                                                Overview chapter:

Added the following feature to the Midcall
                                                      Features table:

Park and retrieve calls

November 24, 2020

In the "Policy Parameters" section in the Index,
                                                added the following new parameters:

SelfCareURL

ShowSelfCarePortal

ShowCallAlerts

Made the following updates to the feature tables in the
                                                Overview chapter:

Added the following note to the "Call on Webex
                                                      Teams" row in the Additional Features table:

Users only have access to the dial pad if they
                                                                  have a paid calling license. If they have a free
                                                                  calling license, they can still call other Webex
                                                                  Teams users.

Added "Mirror Self-View" to the mobile column of
                                                      the Midcall Features table.

Added the following note to the "Apple Push
                                                      Notifications (APNS) for iPhone and iPad and push
                                                      notifications for incoming calls on Android" row
                                                      in the Deployment Features table:

Due to regulations in China, iPhone and iPad
                                                                  users no longer have the slide option to answer
                                                                  incoming calls when their mobile device is locked.
                                                                  Instead, they get an alert notification and must
                                                                  first unlock the screen and then tap the
                                                                  notification to answer the incoming calls.

Added "Configure Self Care Portal Link" (desktop and mobile) to the Deployment Features
                                                      table.

October 29, 2020

In the addition features table, added that "Add a Pause
                                                   to Dial String" is now supported on mobile.

For the multiline and Jabber migration tool parameters,
                                                added a note that states that the parameters are not
                                                selectable presets in Unified CM. You must add these as
                                                custom parameters under policies.

September 30, 2020

Restructured the feature overview table into four separate tables that cover basic call features, midcall features, additional
                                                features, and deployment features. Each table contains columns for desktop and mobile support so it's easier to see at a glance.

In the feature overview tables, added the following entries:

Control Your Video Device from the App (desktop, midcall features)

Simplified call options (mobile, additional features)

Contact Center integration (desktop, additional features)

Jabra headset support (desktop, additional features)

Multiline (desktop, midcall features)

Extend and Connect (desktop, additional features)

Dial via Office (DVO) (mobile, additional features)

Customize virtual background (deployment features for desktop)

Phone Service Connection Error and Action (additional features)

Call Recording (additional features)

Dial Plan Mapping (additional features)

Added "Unified CM Feature Requirements" section in Prepare Your Environment chapter. Added subsections for additional features that need to be configured in advance
                                                to be available in Webex Teams.

Added new section "Configure Users to Move Jabber Contacts and Common Settings to Webex Teams" to the Manage and Troubleshoot chapter.

Moved "Policy Parameters" to Appendix, and added the following new parameters:

RemoteDestinationEditingWithMultipleDevices

RemoteInUsePresencePrimaryLineOnly

SelfCareURL

ShowSelfCarePortal

UserDefinedRemoteDestinations

EnableJabber2TeamsMigration

WebexTeamsDownloadURL

Added "Configure Virtual Background for Users" to Deployment chapter.

August 27, 2020

In the feature overview table, added the following entries:

Simplified call options (enable or disable and order call options)—deployment features for desktop

Push Notifications for incoming calls on Android—mobile

More calling options—desktop

Mirror self-view—desktop

Added new sections "Configure Push Notifications and Recommended Settings" and "Set Calling Options for Users" to the deployment chapter.

In the Voicemail requirements in the prepare environment chapter, clarified that it's recommended to have Unified CM and Unity
                                                Connection  on the same release but required to have them use the same authentication type.

Added Webex Teams for VDI as a supported option for calling.

August 10, 2020

In the "Create and Configure Webex Teams Softphone Devices" section, added a step for configuring emergency numbers for mobile soft clients.

July 30, 2020

Added "PreventDeclineOnHuntCall" to Policy Parameters for the XML config file steps.

In the "Create a UC Manager Profile" section, added the following note:

"Some deployments may require both a voice services and UDS domain. For users with Webex Teams accounts that don't match Unified
                                                   CM, Webex Teams cannot find the home cluster through voice services domain alone. In this case, you must configure the UDS
                                                   servers. The voice service domain is still required for Mobile and Remote Access (MRA) support and locating Expressway servers."

In the feature table, added the following information:

"If a user answers on desk phone, a screen share is still possible. The phone user sees the shared screen from the phone if
                                                         it supports video, otherwise they'll see the shared screen from the app." (Screen sharing for desktop)

"When you add your coworker to your Contacts list, you can edit their profile and add additional phone numbers for them. Then,
                                                         you'll see the new phone number when you make an audio or video call, so it's easier to call them at their alternative number." (Contacts for desktop and mobile)

July 9, 2020

In the deployment chapter, added new section "Voicemail Icon Indicators in Webex Teams "

In the "Allow Untrusted Certificates on Unified CM" section, added the following paragraph: "For iOS devices, you must install a custom root CA on the devices themselves if you're using a private enterprise certificate.
                                                   Otherwise, Webex Teams fails to navigate to the SSO authorization URL."

In the "Expressway Certificates (with MRA)" section, added the following note: "For MRA scenarios, certificates only need to be validated on the Expressway."

In the "Configure Service Profile with UC Services" section, added a step to configure Credential source for voicemail service if not using SSO.

In the "Service Discovery Options" section, updated the note on supported service discovery methods: "We support SRV look up over internal and MRA environments. Service discovery enables clients to automatically detect and locate
                                                   services on or outside your enterprise network. Clients query domain name servers to retrieve service (SRV) records that provide
                                                   the location of servers. See the DNS SRV guidance that follows for internal and external environments."

June 28, 2020

In the feature overview table, added the following entries:

Add Contacts, Search Your Contacts, and Make a Call (desktop and mobile)

Missed calls (desktop)

Call control for Webex Teams calls (desktop)

Call Pickup (desktop and mobile)

Share a specific application (desktop)

Hunt Groups (desktop and mobile)

Lock symbol for secure calls (deployment features—mobile)

Added new sections to the deployment chapter that cover how to configure the XML config file for enabling hunt groups and
                                                call pickup for users:

Set Client Configuration Parameters

Create and Host Client Configuration Files

May 28, 2020

In the feature overview table, added the following entries:

Call history callback (mobile)

Call statistics (mobile)

Desk Phone Control for Webex Teams Calls (desktop)

High Definition (HD) video (desktop)

Health Checker for Phone Services Status (desktop)

May 6, 2020

In the feature overview table, added the following entry:

Auto-Discovery of Service Domain

In the Deployment chapter, added or updated these sections:

"UC Manager Profiles and Calling Behavior Workflow" (New)

"Create a UC Manager Profile" (New)

"Edit a UC Manager Profile" (New)

"Set Calling Behavior and UC Manager Profiles in Control Hub" (Updated)

April 30, 2020

In the feature overview table, added the following entries:

Single Number Reach (mobile)

Voicemail (mobile)

Emergency Calling (mobile)

Call Forwarding (mobile)

Answer call without sharing video (mobile)

March 20, 2020

In the feature overview table, added the following entries:

Automatic Gain Control (AGC) (desktop and mobile)

Conference calls (mobile)

Merge (mobile)

Visual voicemail (desktop—additional features)

Added visual voicemail configuration requirements to the Prepare Your Environment and Deploy chapters.

February 27, 2020

In the feature overview table, added the following entries:

Call Waiting (mobile)

Transfer (mobile)

Support for tel, sip and clicktocall protocols (mobile)

Control Hub headset management (additional features)

Added the following information about Cisco 700 headsets: "If users have Cisco 700 series headset, they can use its USB adapter to answer and end calls, put calls on hold and resume
                                                   them, as well as mute and unmute calls."

Added new section "Manage Cisco Headsets in Webex Control Hub" to the Manage and Troubleshoot chapter.

Added new section "Protocol Handlers for Calling" to the Overview chapter.

Readded Network Requirements section that was previously removed in error.

January 30, 2020

In the feature overview table, added the following entries for Windows and Mac:

Lock icon for secure calls.

Support for Cisco 700 series (bluetooth) headsets.

Popout call window.

Add a pause to a dial string.

In the "License Requirements for Calling in Webex Teams (Unified CM)" , clarified that while a paid subscriptions is required anduser accounts must be managed in your organization, the user accounts
                                                don't require a specific license assignment to use Calling in Webex App (Unified CM) .

December 20, 2019

In the feature overview table, added the following entries:

Hold/resume for mobile platforms.

Resume on different devices for desktop, deskphone control mode, and mobile.

Call history for mobile platforms.

Added the following note to the Headset Requirements section: "When using the Cisco Headset 500 Series or Cisco Headset 700 Series headsets in Webex Teams, the headset firmware can get
                                                   updated automatically. Users can confirm the message that pops up letting them know that an update is available, and then
                                                   they'll get confirmation after it's updated."

December 10, 2019

Added network requirements information to the Prepare Your Environment chapter.

In the Configure SIP Address Routing for your Organization, section, added the following clarification: " *.example.com only matches subdomains, not top-level domains."

November 27, 2019

Added call history to the feature overview table for desktop platforms.

In the "Set DSCP Values on the Network" , changed the signaling packets marking from AF31 to CS3.

November 15, 2019

In the Deploy chapter, added relevant deployment steps
                                                and Webex Teams authentication steps for mobile
                                                softphone mode.

Added the following mobile features to the feature
                                                overview table:

Make call

Answer call

Mute/Unmute

End call

On a Call presence—In Webex Teams, users in the
                                                      same organization can see this presence indicator
                                                      during an active call.

Basic Shared Line Appearance

DTMF input during the call

November 7, 2019

Added the following features to the feature overview table:

Webex Teams call (Windows or Mac)—Users can choose whether to call people using their phone number or using a Webex Teams
                                                      call. A Webex Teams call is a quick way to call someone else who's using Webex Teams. Users can share their screen and whiteboard
                                                      while in the call, but they can't put the call on hold, transfer the call, or use other features only available in phone calls.

SIP (URI) address routing—Configurable in Control
                                                      Hub, this setting allows you to decide which SIP
                                                      addresses are routed through the Webex cloud​. The
                                                      default is for all SIP URIs to be routed through
                                                      Unified CM except for Webex services​.

October 9, 2019

In Unified CM certificates (with MRA in deployment) , removed reference to Cisco CallManager certificate and added the following note: "The Tomcat certificate is also used for secure SIP when Webex Teams is enabled for encrypted calls (SIP Outh operates on the
                                                   default port 5091 for MRA). See "Configure the Phone Security Profile for Encrypted Calls" in this guide for more details."

In Unified CM certificates (no MRA in deployment) , added the following note: "The Tomcat certificate is also used for secure SIP when Webex Teams is enabled for encrypted calls (SIP Oauth operates on
                                                   the default port 5090). See "Configure the Phone Security Profile for Encrypted Calls" in this guide for more details."

September 26, 2019

Added the following features to the feature table in Overview of Calling in Webex App (Unified CM) :

Suppress call notifications when presenting or when DND is enabled.

Support for tel, sip and clicktocall protocols.

Support for Click to Call from Outlook.

Support for Cisco 500 series headsets

Added new section Headset requirements

Removed this incorrect known issue: "Webex Teams does not register to Unified CM in secure softphone mode. You must use non-secure mode as a workaround." Removed other incorrect information that stated secure mode wasn't supported.

Fixed steps for SIP Oath configuration in Configure the phone security profile for encrypted calls . Called out that Unified CM 12.5(1) or later is required for encrypted calls.

Added note to Authenticate with phone services in Webex App : "If both Server address and UC domain are configured, Server Address is used to connect to Unified CM while on-premises only.
                                                   Autodiscovery through DNS SRV is ignored. For MRA, Server Address is ignored."

August 29, 2019

Added new section Configure the phone security profile for encrypted calls .

For both softphone and desk phone control modes, added new midcall features to feature table in Overview of Calling in Webex App (Unified CM) :

Conference

Merge

Transefer

July 25, 2019

Rewrote the "Authenticate with Webex Teams" content to show the user configuration path to take if you have autodiscovery or if you don't.

July 9, 2019

Removed the limited availability disclaimer for Merge and Transfer features for Webex Teams in softphone mode. (These features
                                                are now Generally Available.)

June 27, 2019

Removed the Preview Release Disclaimer. (Calling in Webex Teams (Unified CM) is officially Generally Available.)

Added Merge and Transfer as limited availability features for Webex Teams in softphone mode.

Added new section Allow untrusted certificates on Unified CM to the Appendix.

Added the following information to the certificate requirements and known issues: "Certificates issued with a deprecated signature algorithm (such as SHA-1) do not work; you must use a supported secure signature
                                                   algorithm such as SHA-256 or later, as documented in the Certificates chapter in the Administration Guide for Cisco Unified Communications Manager ."

June 14, 2019

In Calling experience with Webex App for users , added the following information under the "User Experience Changes for Hybrid Call Service Users" section:

"If the Webex device is configured in Control Hub as a Place that is enabled for Hybrid Call Service, the user can dial from
                                                   Webex Teams and the call then starts on the Webex device using that device's directory number as the caller ID on the receiving
                                                   end."

In Certificate requirements , added MRA certificate requirements and restructured as 3 subsections: Unified CM Certificates (No MRA), Unified CM Certificates
                                                (MRA), and Expressway Certificates (MRA).

In Set DSCP values on the network , corrected QoS port range information. Previously, it read "16384 to 24574" for audio streams and "24575 to 32766" for video
                                                streams; now, it reads "16384 to 24575" and "24576 to 32676", respectively.

April 24, 2019

Restructured the Requirements section—Each Calling in Webex Teams (Unified CM) requirement now has its own subsection to make
                                                it easier to find.

Added new section ( Configure Unified CM end users for Calling in Webex App (Unified CM) ) to the Deploy chapter.

April 10, 2019

Added Meeting join in desk phone control mode to the Call Flows.

In Requirements section, added the following points:

In Cisco Unified CM Administration > System > Server , the Unified CM server names must be defined as FQDN.

We do not support the deployment model of MRA without SSO and Unified CM with SSO.

At this time, we support internal only automatic discovery. Service discovery enables clients to automatically detect and
                                                      locate services on your enterprise network. Clients query domain name servers to retrieve service (SRV) records that provide
                                                      the location of servers.

If you're using Server Information for configuration and not SRV records, your users' Webex Teams email addresses must match
                                                      their Unified CM email addresses—at a minimum, the user ID portion before the domain must match.

March 28, 2019

Initial version of the document.

## Overview of Calling in Webex App (Unified CM)

The Calling in Webex App (Unified CM) solution lets you register Webex App directly to your Cisco Unified Communications Manager call control environment
                              (on-premises enterprise, Business Edition 6000/7000, Unified CM Cloud or as
                              delivered through an HCS partner solution).

### Users

This solution enhances the calling experience for end users, allowing them to
                              directly make calls in Webex App through your Unified CM environment, use midcall features, and control their desk
                              phone from Webex App .

When dialing from Webex App , users can use the same dial strings or prefixes as they do on their desk phones; Webex App functions like any other desk phone registered to your Unified CM. Unified CM
                              calls that are established in Webex App use the configuration that's in place for your Unified CM deployment (such as
                              location, bandwidth settings, point to point media, and so on).

### Administrators

As an administrator of Calling in Webex App (Unified CM), you reuse your existing Unified CM and Mobile and Remote Access
                              (MRA) configuration that you may've already had in place. The deployment model is
                              similar to Jabber. The same device types are used: In softphone mode, Webex App registers as a SIP device with the product type "Cisco Unified Client Services
                              Framework" or CSF for desktop, TCT or BOT for mobile, and TAB for tablets.
                              Alternatively, Webex App can connect to Unified CM using CTI to control the user's endpoints.

The Webex App makes its primary connection to the Webex cloud to get its service configuration (messaging, meetings, presence, contact
                              lists, calling behavior, and so on), but it also reads the following configuration
                              from the Unified CM environment to provide specific calling functionality to
                              users:

Initial Unified CM discovery through DNS query to discover any configured
                                    voice services domain. (In a multicluster environment, Intercluster Lookup
                                    Service is also leveraged to determine which cluster the Unified CM user is
                                    homed to.) An outside domain (MRA deployment) is also discovered. (If the
                                    Webex domain does not match the existing Voice Services Domain, you can set
                                    a Voice Services Domain in Control Hub, and associated with specific
                                    users.)

UC service profiles (for voicemail through Unity Connection, CTI services,
                                    and advanced calling functionality through supported parameters in the
                                    Jabber config service profile or XML file)

Single Sign-On (SSO) credentials if an Identity Provider (IdP) is
                                    integrated

Oath tokens, including refresh and expiry timers. (Users need to
                                    reauthenticate if a session expires.)

Certificate validation

## Calling features in Webex App

This integration provides the following feature set in Webex App for desktop (Windows and Mac) and for mobile (Android, iPad, and iPhone). Wherever
                              possible, the feature listings in this table include a link to a relevant help article for
                              end users. See Audio and video calls for more general information on making a call. See Supported calling
                                 options for a feature comparison table for end users.

### Basic calling features

Feature

Description and documentation

Desktop

Mobile

Answer call

—

✓

✓

Answer call without sharing video

See Turn Off Your Video for all Incoming
                                                Calls .

✓

✓

Desk Phone Control

Desk Phone Control (including meetings and calls in Webex App )—See Make
                                                Calls With Your Desk Phone .

✓

DTMF input during the call

—

✓

✓

End call

—

✓

✓

Make call

—

✓

✓

Mute/Unmute

—

✓

✓

On a Call presence

In Webex App , users in the same organization can see this presence
                                             indicator during an active call.

✓

✓

### Midcall calling features

Feature name

Description and documentation

Desktop

Mobile

Call Pickup

If a user is in a customer support role and their coworker isn't able to
                                             answer an incoming call to their phone, the support user gets a notification in Webex App if both are in the same pickup group. That user can answer their call from the
                                             notification in the app. The user can also pick up the calls in other pickup
                                             groups. See Pick Up Someone Else's Call .

✓

✓

Call Recording

You can determine how much control users have over recording calls. Depending on
                                             the setup, incoming and outgoing calls may be recorded automatically or you may be
                                             able to decide which calls you want to record. If you enable users with call
                                             recording, they can start and stop recordings at their own discretion. When a call
                                             is being recorded, that recording continues whether a user moves the call to
                                             another device, merges the call with another active call, or makes a conference
                                             call. They're presented with a visual indicator letting them know when a call is
                                             being recorded. See Record Your Phone Calls .

✓

✓

Call Waiting

When a user is already in call and someone else calls, the called user can choose
                                             how they want to handle the incoming call. For example, the user can put the
                                             active call on hold and answer the second call. See Answer Call Waiting for more information.

✓

✓

Conference calls

When users are on a call with someone else, they might want to add other people
                                             into the call to start a conference call right away. They can add up to 8 other
                                             people into conference calls started in this way. See Start a Conference
                                                Call .

✓

✓

Control Your Video Device from the App

Users can start or stop sharing your video on a connected video device right from
                                             the app. For example, if connected to a Cisco Webex Board and users don't want
                                             to share video, they no longer have to walk up to the board and turn off the
                                             video. They can turn it off from the app. See Turn Off Your Video
                                                During a Meeting or Call On Webex Boards, Room and Desk Devices .

✓

Hold/resume

Users place a call on hold and resume in Webex App . See Put a Phone Call On Hold .

✓

✓

Hunt Groups

Users can sign in or out of a Hunt Group from Call Settings. When they're
                                             signed in and a call comes into a group that they belong to, they'll see the
                                             Hunt Group number on the incoming call notification. Sign in to a Hunt
                                                Group .

✓

✓

Merge

Users take 2 active calls and merge them into a single conference call in Webex App . See Merge Two Phone Calls .

✓

✓

Mirror self-view

Mirror self-view—By default, when users share video during a call, they can see
                                             themselves just like you're looking in a mirror. If they text behind them and
                                             want to read it easily instead of having to read it backwards, tehey may want to
                                             off the Mirror my video view setting. This setting doesn't affect the
                                             way other people in the meeting see you. See Turn Off Mirror View for
                                                Your Self-View Video. .

✓

✓

Move a call into a meeting

Users in a call can take advantage of advanced meetings features such as
                                             transcriptions, real-time translations, notes, action items, recordings, and
                                             whiteboarding. Just move that call into a full-featured meeting. Before moving the
                                             call into a meeting, users can even invite other people into the discussion.

✓

✓

Multiline

Users can use up to 10 phone lines (on desktop) and 8 phone lines (on mobile) with Webex App and leverage advanced calling features on each line such as call forward, transfer, hunt group, shared lines, and voicemail.
                                             And you can turn on presence for shared lines so that line status is displayed for users. See Multiline and Change the Active Line for Calling .

Once Webex users have enabled multiline on mobile, they will no longer be able to sign in to phone services in the Webex mobile
                                                               app prior to version 44.12.

Ten-line support and multiline on mobile will not work for Jabber. Adding either of them to Unified CM will result in phone
                                                               services registration failure on Jabber.

✓

✓

Park and retrieve calls

Users can park a call on one device and that user or someone else can retrieve
                                             the call from another device.

✓

✓

Resume from different devices

A user can put a call on hold from the desktop app and resume it on mobile. Or,
                                             put your mobile call on hold and resume it on a desk phone. Go any direction
                                             between desk phone, mobile, and desktop; just put the call on hold and resume
                                             wherever it's convenient. See Put a Phone Call On
                                                Hold .

✓

✓

Screen sharing

Screen sharing—Share content from a computer screen during a call in Webex App . Users can choose a specific application to share, rather than having to share
                                             their whole screen. If a user answers on desk phone, a screen share is still
                                             possible. The phone user sees the shared screen from the phone if it supports
                                             video, otherwise they'll see the shared screen from the app. See Share Your Screen in a Phone Call .

Users can share your screen regardless of whether the person they called is
                                                         using a cloud-registered device or an on-premises device. The screen share is
                                                         still sent with a high frame rate (30 FPS), high resolution (1080p), and
                                                         includes audio.

✓

Switch between front and back cameras

On mobile phones or tablets, you can switch between front-facing and back-facing
                                             cameras. See the mobile sections in Change Your Video
                                                Settings .

✓

Transfer

Redirects a connected call within Webex App . The target is the user to which another user wants to transfer the call. See Transfer a Phone Call .

✓

✓

Virtual cameras

During a call, users can choose to use a virtual camera. Use a virtual camera,
                                             such as an application, driver, or software, to create an overlay of video,
                                             images, or feeds.

✓

### Additional features

Feature name

Description and documentation

Desktop

Mobile

Add a Pause to Dial String

Users can add a pause to an entered phone number, which they might need if joining a conference call and need to enter numbers
                                             in response to the automated system. They can add a comma (,) to the number, which gives a 1-second delay in the dialing.
                                             They can add several commas in a row to extend the delay. For example: 95556543123,,,,56789.

✓

✓

Add Contacts, Search Your Contacts, and Make a Call

Users can add coworkers into a Contacts list and group them however they like, making people easier to find when users need
                                             to chat or call.

Users can even look up Outlook contacts (Windows), local address book (Mac), and local phone contacts (iPhone, iPad, and Android)
                                             from Webex App , so they can easily find contacts and make a call.

When you add your coworker to your Contacts list, you can edit their profile and add additional phone numbers for them. Then,
                                             you'll see the new phone number when you make an audio or video call, so it's easier to call them at their alternative number.
                                             See Add Someone to Your Contacts List .

✓

✓

Automatic Gain Control (AGC)

AGC is a unique circuit that listens to the incoming audio level and adjusts the recording level when sounds are too loud
                                             or too soft. When the audio volume is too loud, it automatically reduces the sound. When the audio is too soft, it automatically
                                             amplifies the sound. This doesn't adjust the audio volume at the OS level.

✓

✓

Call on Webex App

Users can choose whether to call people using their phone number or using a call
                                             in Webex App . A call in Webex App is a quick way to call someone else who's using Webex App . Users can share their screen and whiteboard while in the call, but they
                                             can't put the call on hold, transfer the call, or use other features only
                                             available in phone calls. See Call Anyone with
                                             a Webex App account.

Users only have access to the dial pad if they have a paid calling license. If
                                                         they have a free calling license, they can still call other Webex App users.

✓

✓

Call control for calls in Webex App

If using a Cisco 730 headset, users can use its USB adapter or Bluetooth to answer and end calls, put calls on hold and resume
                                             them, as well as mute and unmute calls. See Make and Answer Calls on the Cisco Headset 730 .

✓

Call history

When a user calls other people in the organization, they see more details about phone numbers in the call history. So, to
                                             call someone back, that user can see if they're calling a work or mobile number.

Users can select the Call icon beside someone’s name or number in their Call
                                             History and automatically call the person back at the number in the history. Users
                                             no longer need to choose what number to reach others at. After they return a
                                             missed call, they can delete the call from call history. The call history only
                                             shows the last 200 calls over the last 30 days. See View Call and
                                                Meeting History for more information.

✓

✓

Call Statistics

When users are in a call, they can check call statistics, such as packet loss, latency, and resolution rate. See Access Call Statistics .

✓

Click to Call from Outlook

You can set up your Windows or Mac computer so that Webex App is the default option for calling numbers that you click outside of the app, for example, in Microsoft Outlook or from a
                                             link in your web browser. See Click to Call From Another App .

✓

Client Matter Codes (CMCs) and Forced Authorization Codes (FMCs)

With client matter codes (CMCs) and forced authorization codes (FACs), you can
                                             effectively manage call access and accounting. CMCs assist with call accounting
                                             and billing for clients, and FACs regulate the types of calls that certain users
                                             can place.

CMCs force the user to enter a code; this action specifies that the call relates
                                             to a specific client matter. You can assign client matter codes to customers,
                                             students, or other populations for call accounting and billing purposes. FACs
                                             force the user to enter a valid authorization code that is assigned at a certain
                                             access level before the call is completed.  See the "Prepare Your
                                                Environment" chapter.

✓

✓

Contact Center Integration

Webex App can integrate into your Cisco Contact Center application and be controlled in
                                             Finesse desktop (Unified Contact Center Enterprise or Express). This integration
                                             supports contact center features such as multiline, recording, conferencing, and
                                             more. See Contact Center Integration for the latest supported
                                             features.

✓

Diagnostics in the Webex App

If users experience connection issues, they can use the diagnostic tool to
                                             identify configuration errors or export a network diagnostics report. This
                                             information helps you troubleshoot any issues they're experiencing. See the
                                             Troubleshooting chapter.

✓

Dial-via-Office (DVO)

When you set up users with DVO, they have the option to make work calls using their mobile phone connection, which ensures
                                             calls are uninterrupted even if data is unavailable. No matter what option they choose, the work number is always used as
                                             the caller ID so people can easily identify users. See Make Work Calls Over a Mobile Phone Connection .

✓

Dial Plan Mapping

You configure dial plan mapping to ensure that dialing rules on Cisco Unified Communications Manager match dialing rules on
                                             your directory. See the Prepare Your Environment chapter.

✓

✓

Emergency calls

If users make an emergency call in Webex App , the call is made using the device’s Phone app, making it easier for Emergency Services to pinpoint a location through their
                                             network carrier.

✓

Extend and Connect

You can set up users to connect to alternate devices to make and receive calls. Users can see those devices under Alternate Devices when they go to calling settings. That's where they can add or edit the phone numbers for those devices. See Make a Call From an Alternate Device .

✓

Fast failover (MRA)

Webex can detect failure quickly, whether it's a controlled shutdown, node
                                             failure, or network failure, and seamlessly fail over to a backup path through MRA
                                             so user productivity isn't affected. See the Prepare Your Environment chapter.

✓

✓

Health Checker for Phone Services Status

If unsure whether Phone Service is working properly, users can check out the status of the phone connection from the app.
                                             On Windows, they click their profile picture and then go to Help > Health Checker . On Mac, they go to Help > Health Checker . Health Checker tests the connection and lets users know if there's a problem.

✓

High Definition (HD) Video

Users can enable or disable HD video by clicking their profile picture, going to Settings (Windows) or Preferences (Mac), selecting Video , and then enabling or disabling the setting. They may want to disable HD video if their computer CPU is running high or they
                                             want to save network bandwidth during a call or meeting.

✓

Location Monitoring

You can turn on location monitoring so that when users call emergency services
                                             from Webex (for example, 911), their location is automatically shared with
                                             emergency responders.

✓

✓

Missed calls

See how many calls you’ve missed with a red badge counter in the Calls tab. The Calls tab shows a list of incoming and outgoing calls and you can call someone back from your Call History. Your
                                             scheduled meetings are listed in the Meetings tab, making it easier for you to distinguish between the two types of communication.

✓

More calling options

Users can call someone's video address (for example, bburke@biotechnia.com) from anywhere in the app where they'd make any
                                             type of call (example: search for someone or being in a space with that person).

✓

Multi call window

Webex App users with multiple lines see this by default. It is a separate, floating window to help with managing multiple
                                             or shared lines. See Manage your phone calls in the Multi Call window .

✓ (Windows)

Network Handoff (Wi-Fi to LTE)

When you're on an active call and you need to change networks but want to keep
                                             the call in Webex, no need to worry; the change is made automatically without any
                                             interruption or effect to call quality. (See Unified CM features in Prepare Your
                                             Environment.)

✓

✓

Phone numbers in contact cards

Work numbers and mobile numbers are synchronized from Active Directory and appear as selectable items in Webex App . (Requires Cisco Directory Connector to synchronize user phone number attributes to the Webex cloud.)

✓

✓

Phone Service Connection Error and Action

The footer in Webex App shows more descriptive error messages if the phone service disconnects. See Error Messages .

✓

✓

Popout Call Window

When a user calls someone else, the call window pops out, and both users can access calling features. While in the call, users
                                             can still respond to critical messages.

✓

PSTN calling for mobile app users in India

Users in India can make that call when they can't be on the corporate network.
                                             The Webex mobile app gives them the option to use the device's calling app
                                             instead. See "EnablePhoneDialerOptionOverMRA" in the customization policy
                                             parameters in the Appendix.

✓

PSTN for Personal Mode Devices

Leveraging Hybrid Calling, you can provide PSTN access to users' personal mode
                                             devices. (See the Deployment Guide for Hybrid Calling for Cisco
                                                Webex Devices .)

✓

RedSky location reporting for emergency calling

To comply with Ray Baum's act, you can require users to give accurate location
                                             information when they are outside the office.​

✓

✓

Self Care Portal—Call forwarding

If users need to take your work calls from another number, they can set up call forwarding right from Webex App . They just enter the call forwarding number, and their calls all ring at that number. See Forward Phone Calls and Access More Call Settings .

✓

✓

Self Care Portal—Single Number Reach (SNR)

Users can access the Self Care Portal from Webex App and add more numbers for devices they want to ring simultaneously with their enterprise directory number. See Get Work Calls at Any Number and Access More Call Settings .

✓

✓

Support for Cisco 500 series and 700 series (bluetooth) headsets

If users have the Cisco 700 series headset, they can use its USB adapter to answer and end calls, put calls on hold and resume
                                             them, as well as mute and unmute calls.

When users use a Cisco headset with Webex App , you can now keep track of it in Webex Control Hub. This lets you track inventory and troubleshoot issues for your users.
                                             (See the deployment chapter.)

✓

Support for Jabra headsets

See Details%20about%20Headset%20Support for supported models.

✓

Suppress call notifications when presenting, when DND is enabled, or when you're
                                             already in a call or meeting.

Users can mute notifications for incoming calls so that they don't see or hear
                                             someone calling. If voicemail is set up, the caller can leave a message. The call
                                             still shows up in the spaces list and call history.

✓

Switch your call from Webex to your mobile phone app

When you're on an active call in Webex and you want to take your call on the run,
                                             just switch your call from Webex to your mobile phone app. You maintain
                                             connectivity and call quality with only a short pause in your call while you make
                                             the quick switch from More . (See the Deployment chapter and Switch Your
                                                Call to Your Mobile Phone App .)

✓

tel, sip and clicktocall protocol

See the relevant section in this overview chapter.

✓

✓

Voicemail

No more missing calls in Webex App . Users can manage their voicemail in the Calls tab. There's a red badge counter that lets them know how many voice messages
                                             they have. They can check out the details of a message, play it, mark it as read, delete it, or call back the sender. After
                                             they listened to messages, either with Webex App or desk phone, the red badge counter disappears. See Voicemail .

✓

✓

Visual Voicemail

Visual voicemail—No more missing calls in Webex App . Users get a dedicated Voicemail tab to manage all their voicemails. There's a red badge counter that lets them know how many voice messages they have. They can
                                             check out the details of a message, play it, mark it as read, delete it or call back the sender. After they listened to your
                                             messages, either with Webex App or your desk phone, the red badge counter disappears. See Voicemail .

✓

### Deployment features

Feature name

Description and Documentation

Desktop

Mobile

Apple and Android Push Notifications (APNs)

On iPhone, iPad, and Android devices, push notifications let the
                                             user know about incoming calls in Webex App . (See the "Prepare Your Environment" chapter.)

Due to regulations in China, iPhone and iPad users no longer
                                                         have the slide option to answer incoming calls when their
                                                         mobile device is locked. Instead, they get an alert
                                                         notification and must first unlock the screen and then tap
                                                         the notification to answer the incoming calls.

✓

Local Push Notification Service (LPNS)

This is a reliable and secure way to notify Webex  users on iOS devices of incoming VoIP calls under the following operating
                                             conditions:

In a WiFi-constrained network.

No Internet connection hence cannot access Apple Push Notification Service(APNs).

To get LPNS call notifications, users must grant the Local Network permission to Webex App.

If both LPNS and APNs are configured on UCM, UCM will deliver the call through the LPNS channel first, if it fails, APNs will
                                                               be the fallback option with the best effort.

To get LPNs call notifications working properly, when the users have multiple iPhones or iPads, they must ensure the Webex
                                                               app runs only on one iPhone and one iPad.

✓

iOS and iPad OS

Auto-Discovery of Service Domain

You can use Control Hub to configure a UC manager profile to add
                                             a service domain automatically to users' Phone Services settings in Webex App . That way, they don't need to manually enter a domain and can
                                             sign in right away. (See the deployment chapter.)

✓

✓

Configure Self Care Portal Link

You can choose the portal link for your users when they access it
                                             from the Call Settings in their app. (See the deployment
                                             chapter for config file steps and the appendix for related
                                             policy parameters.)

✓

✓

Customize virtual background

You can let users add up to 3 images of their own to use for
                                             virtual backgrounds. See Configure Virtual Backgrounds for Webex
                                                Users .

✓

Customize emergency dialing disclaimer

You can customize the content of the emergency dialing disclaimer
                                             to meet regulations and business needs in various regions and
                                             situations.

You can also change the frequency of the disclaimer pop-up, or
                                             hide the disclaimer if the emergency responder infrastructure is
                                             not ready. (See the customizable parameters in the
                                             Appendix.)

✓

✓

Disable video for all 1:1 calls

Using Control Hub, you can disable video for calling or set the
                                             default to video off for compliance, privacy, or network
                                             purposes.

✓

✓

Expressway Mobile Remote Access (MRA) for Webex App

MRA provides a secure connection for Webex App traffic without having to connect to the corporate network
                                             over a VPN. (See the Mobile and Remote Access
                                                Through Cisco Expressway Deployment Guide .)

✓

✓

Secure and encrypted calls

Encrpyted calls are configurable from Unified CM and indicated by
                                             a lock icon in Webex App . (See the deployment chapter.)

✓

✓

Service Discovery

Service discovery enables clients to automatically detect and
                                             locate services on your enterprise (internal) and MRA (external)
                                             network. (See the deployment chapter.)

✓

✓

Simplified call options (enable or disable and order call
                                             options)

You can set up user calling options to suit their needs. For
                                             example, they may not need to make Webex App calls and only want to call coworkers using their work
                                             number, mobile number, or SIP URI address. You can disable calls
                                             in Webex App so they don't have that option show up when they make a call.
                                             See Configure Call Settings for Your
                                                Organization .

✓

✓

SIP (URI) address routing

Configurable in Control Hub, this
                                                setting allows you to decide which SIP addresses are routed
                                                through the Webex cloud​. The default is for all SIP URIs to
                                                be routed through Unified CM except for Webex
                                                services​. See Configure SIP Address Routing for Your
                                                Organization .

✓

Single Sign-On (SSO)

With SSO integration between your IdP, your premises environment,
                                             and the Webex cloud, users can sign in across applications with
                                             one set of credentials. (See the "Prepare Your Environment" chapter.)

✓

✓

Virtual cameras (macOS)

You can use Webex Control Hub to enable or disable virtual camera
                                             usage for your users' calls and meetings in the Webex app. Users
                                             can use a virtual camera, such as an application, driver, or
                                             software, to create an overlay of video, images, or feeds.

✓ (macOS only)

### More information about Desk Phone Control (DPC)

Any desk phones or Extension Mobility profiles that are associated with the user's
                                 Unified CM account are listed as an available device to connect to in Webex App for Windows or Mac. If the device is selected, Unified CM calls that are dialed
                                 from or answered in Webex App use that desk phone. Users can start or stop the call, enter DTMF input (which
                                 the phone acknowledges), and use the midcall features that are documented in the
                                 preceding feature table. Users can also join meetings from Webex App in desk phone control mode.

Webex App does not support Extension Mobility.

Users can access the description of your desk phone right from their desktop app and
                                 personalize that description to something that makes sense. They can hover over the
                                 phone description and then click to change the name. If you assigned more than one desk phone to
                                 users, customizing each description can be helpful.

## Calling experience with Webex App for users

### Call comparison

This table lists what types of Webex App calls go through Unified CM and types of Webex App calls or meetings that do not go through Unified
                                    CM (and instead go "over the top" as calls to cloud
                                    microservices).

Calls through Unified CM
                                             environment

Calls and meetings through Webex cloud

Calls initiated directly from a
                                             1:1 space or from a contact card in the Webex App

Ad hoc meetings from a group
                                             space in the Webex App

Search and then call a user in
                                             the Webex App

Using the Join button in the Webex App to join an ad hoc or scheduled meeting

Dialing directory numbers or PSTN
                                             numbers from Call in the Webex App

Dialing premises Directory URIs
                                             from Call in the Webex App . (Depends on the Unified CM SIP
                                                Address Routing setting in Control
                                             Hub.)

Desk phone control (DPC) calls
                                             (outgoing: dial a directory or PSTN number in the Webex App , take the call on the Unified CM device;
                                             incoming: answer the call in Webex App , take the call on the device).

Joining a meeting while paired through Room, Desk, or Board devices

1:1 calls that are placed
                                             directly in the Webex App to a free user in the consumer organization, to
                                             a user in another organization, or to a user in
                                             the same organization who doesn't have a directory
                                             number. (Numbers are not shared across
                                             organizations, so don't appear in contact cards.)
                                             These are classified as a Call on Webex App .

### User experience

Unified CM registration in the Webex App stays active.

Incoming calls to a user's
                                             directory number are presented in Webex App and, when accepted, calls are answered on the
                                             desktop app and do not use the paired Room, Desk,
                                             or Board device.

If the Webex device is configured
                                             in Control Hub as a Workspace that is enabled for
                                             Hybrid Calling, the user can dial from Webex App and the call then starts on the Webex device
                                             using that device's directory number as the caller
                                             ID on the receiving end. A user cannot answer an
                                             incoming call to a paired device.

If the Webex device is not in a
                                             Workspace that's enabled for Hybrid Calling, the
                                             directory number or PSTN dialing fails and an
                                             error message is presented in the user's Webex App .

Media (audio and video) for 1:1 calls to users with contact cards and calls that are started from the search or dial view
                                             go through the on-premises desk phone.

Media (audio and video) for group space meetings, Webex meetings (scheduled or ad-hoc), and calls to users without contact
                                             cards go through the on-premises desk phone.

Incoming calls that don't go through Unified CM do not roll over to voicemail and continue to ring until the user answers
                                             or declines.

Incoming calls that go through Unified CM (for example, to a user's corporate directory number) roll over to voicemail.

## Architecture

### On network

This architecture diagram represents Webex integrated with a Unified CM calling
                                 environment that is inside the corporate network.

Icon

Protocol

Purpose

HTTPS

Webex cloud services, Visual Voicemail

SIP

Softphone Mode

CTI/QBE

Deskphone Control

LDAP

Directory

DNS

Service Discovery

SP Agreement

Single Sign-On (SSO) Agreement

### Remote

This architecture diagram represents Webex integrated with a Unified CM calling
                                 environment. The environment also contains Expressway pair that is deployed for
                                 Mobile and Remote Access (MRA) for remote users.

Icon

Protocol

Purpose

HTTPS

Webex cloud services, Visual Voicemail

SIP

Softphone Mode

LDAP

Directory

DNS

Service Discovery

SP Agreement

Single Sign-On (SSO) Agreement

## Call flows for Calling in Webex App (Unified CM)

### Unified CM call answered on Webex App

Using Webex App , Alice calls Bob's directory number from the
                                       contact card in their 1:1 space.

The call rings on Bob's Webex App .

Bob answers the call in the Webex App . Call signaling is established through Unified CM.

Both parties can turn on video and share content. (Video is on by default if a camera is present.)

### Unified CM incoming call answered on desk phone

From her Webex App , Alice calls Bob's directory number from their Webex App 1:1 space. (Bob's directory number is available on his contact card in the app.)

Call signaling is established through Unified CM. The
                                       call rings on both Bob’s desk phone and his Webex App .

Bob answers on his desk phone. Media flows directly
                                       between Alice's Webex App and Bob’s desk phone.

Both parties can turn on video and share content. (Video
                                       is on by default if a camera is present on the Webex App desktop device.)

### Call on Webex App to a user with no directory number

Using Webex App , Alice calls Bob's Webex App from their 1:1 space. (Bob's directory number is not available on his contact card in
                                       the app.)

Bob answers the call on Webex App .

The call is established between the two Webex App users as a call on Webex App . Media flows between the two Webex App instances over the cloud or through an on-premises Video Mesh Node if deployed.

### Unified CM call in Webex App to PSTN number

Alice calls a PSTN number from Webex App using the Call tab.

Call signaling is established through the Unified CM to
                                       the PSTN gateway.

Media flows directly between Webex App and the PSTN gateway.

### Unified CM call in desk phone control mode

Using Webex App , Alice (in desk phone control mode) calls Bob's
                                       directory number from their Webex App 1:1 space. (Bob's directory number is available
                                       on his contact card in the app.)

The call goes through her desk phone. Call signaling is established through Unified CM.

Bob’s desk phone rings and he gets a notification on Webex App .

Bob answers the call in Webex App in desk phone control mode. Media flows directly
                                       between the two desk phones.

### Meeting join in desk phone control mode

Using the Webex App , Alice (while in desk phone control mode) joins a meeting. (The meeting must be
                                       directly from a space and take place only in the Webex App . Full Featured Meetings are not supported.)

In desk phone control mode, the media is established between the Unified CM phone and the meeting over the cloud. Media flows
                                       between the two over the cloud or through a Video Mesh Node if deployed.

| Date | Changes Made |
|---|---|
| November 2025 | Included a note in the chapter "Deploy Calling in Webex App (Unified CM)", section "Service discovery options". |
| March 2025 | Included "Limitation" and "Known Issues" in the "Centralized call history" section. Addressed a few changes to the steps in
                                          "Unified CM" section. Changed the title of the section from "Multi Call Window" to "Calling Dock". |
| December 05, 2024 | Included a new topic "Centralized Call History" in the "Unified CM feature requirements" section. |
| Included a new topic "Multi Line Support for Webex App  (Unified CM) on Mobile" in "Unified CM feature requirements" section.
                                          Addressed the following: Extend the maximum number of phone lines from eight to ten on desktop Webex application. Multi-line is supported on mobile with up to eight lines. |
| Updated the "Known issues and limitations with Calling in Webex App (Unified CM)" section. |
| Updated the "Dial Via Office Reverse" and "Move call to mobile" sections. |
| Updated "Table 2: Midcall calling features". |
| Updated the parameter "RemoteInUsePresencePrimaryLineOnly" in the "Appendix > Customization parameters". |
| April 24, 2024 | Included a link to step 3 in the chapter "Deploy Calling in Webex App (Unified CM)" > section "Configure moving a call into
                                          a meeting". |
| April 22, 2024 | New Parameter "ShowSelectiveCallRecordingButton" is added to  "Appendix" > "Policy Parameters" > "Feature Parameters" section. |
| July 03, 2023 | New Parameter "EnableSIPURIDialling" is added to "Appendix" > "Policy Parameters" > "Feature Parameters" section. |
| New Parameter "LocalPushSSIDList" is added to "Appendix" > "Policy Parameters" > "Feature Parameters" section. |
| New Feature Name "Local Push Notification Service (LPNS)" along with "Note" is added to the "Deployment Features" table in
                                          the "Deployment Features" section. |
| Added a Note to "Overview of Calling in Webex App (Unified CM)" > "Calling features in Webex App" > "More information about
                                          Desk Phone Control (DPC)"  section. |
| April 29, 2023 | Revamped the section "Set up calling behavior and UC manager profiles in Control Hub". |
| March 10, 2023 | Changes to the section, "Location reporting for emergency calling". Redsky was the only E911 SP. Now, "Intrado" is integrated
                                          with E911 SP and is called "E911 SP Intrado". |
| October 18, 2022 | In the section "Recommended configuration - SSO redirect URI", under "Requirements", replaced "Unified CM 12.5(x) releases-12.5(1)
                                          SU4 and later (Unified CM 14 is not supported)" to "Unified CM 12.5(x) releases-12.5(1) SU4 and Unified CM 14.0(x) releases-14.0(1)
                                          SU1 and later". |
| June 7, 2022 | New feature "Multi call window" added to the Additional features table in the Overview > Calling features in Webex App section of this document. Added Multi call window requirements to Prepare > Unified CM feature requirements Added CucmCallBargeMode parameter to Appendix > Policy parameters > Feature parameters . There is a new parameter ShowPhoneNumberInLineSelection in the configuration file, for displaying / hiding number in line selection dropdown menu. Added this parameter to the Customization parameters table in the Appendix to this document. |
| February 15, 2022 | Changed the UI path for updating user or organization calling behavior in Control Hub (in the section "Set calling behavior and UC manager profiles in Control Hub" ). Removed the note that explains "Auto cleanup and deletion of auto-provisioned devices is not supported currently" in Overview of Auto-Provisioning of Webex App . |
| December 13, 2021 | Added prerequisites and a link to configuration steps for
                                                the Auto-Device Provisioning feature for Cloud-Connected
                                                UC. Added RedSky emergency location reporting to the "Prepare Your Environment" chapter. In the "Meeting join in desk phone control mode" section of the call flows, added the following
                                                clarifying text: "The meeting must be directly from a
                                                   space and take place only in the Webex App. Full
                                                   Featured Meetings are not supported." In accordance with style guidelines, changed section
                                                titles from title case to sentence case. |
| October 5, 2021 | In the Customize Parameters table in the Appendix, added
                                                the EnableADLockPrevention parameter. |
| September 7, 2021 | In the Customize Parameters table in the Appendix, added
                                                the following parameters: For emergency disclaimers: E911NotificationFrequency E911NotificationURL For video settings: EnableVideo StartCallWithVideo Added the following parameters for video settings: In the Deployment features table, added the following
                                                entries: Customize emergency dialing disclaimer Disable video for all 1:1 calls |
| August 9, 2021 | Added new entries to Additional Features: Network Handoff (Wi-Fi to LTE) Switch your call from Webex to your mobile phone
                                                      app Added new section "Wi-Fi to LTE Call Network Handoff
                                                   " to Unified CM Feature Requirements in the Prepare
                                                Your Environment chapter. Added new section "Configure Move Call to Mobile" to
                                                the deployment chapter. In "Expressway Certificates (With MRA) " , added
                                                section for migrating Jabber to Webex and considerations
                                                for private CA certification. In the Feature Parameters table in the Appendix, added
                                                the following parameters for call recording: EnableRecordingTone LocalRecordingToneVolume NearEndRecordingToneVolume RecordingToneDuration RecordingToneInterval In the Feature Parameters table in the Appendix, added
                                                EnableCallPark. |
| July 7, 2021 | Added new section "Contact Center Feature
                                                   Requirements," including a link to Contact Center Integration for
                                                   Webex which lists the latest supported
                                                features. For SSO Redirect URI, clarified that Unified CM 14.0 is
                                                not supported. Updated logos in architecture diagrams to reflect new
                                                branding for the Webex app. (See New Webex Suite and Branding for more information.) |
| June 2, 2021 | Added new section "Android Devices and
                                                   Density-Independent Pixels" to explain how Webex
                                                determines whether an Android device is a phone or a
                                                tablet. Added new section "Configure Additional Features" to
                                                the deployment chapter. Added new parameter "EnablePhoneDialerOptionOverMRA" to the Customization Parameters in the Appendix. Added the following items to feature tables: Added "Virtual Cameras" to the midcall
                                                      features table for desktop. Added "Virtual Cameras (macOS)" to the
                                                      deployment features table. Added "PSTN calling for mobile app users in
                                                         India" to the additional calling feature
                                                      table. |
| May 11, 2021 | Added information about how Webex distinguishes Android
                                                phones from tablets by using the device's display dp
                                                (less than 600 for phones; 600 or greater for
                                                tablets). Removed "Retain Hybrid Call Service for Users" from the
                                                Prepare Your Environment chapter because Hybrid Calling (Call Connector
                                                   architecture) will be End of Life (EOL) . |
| May 5, 2021 | Added Chromebooks as supported devices when the TAB
                                                device type is used in Unified CM. Added more information about configuring softphone
                                                devices on different platforms for the same user. Added the following to the Additional Features table: MRA failover (the minimum requirements (Unified
                                                      CM 14.0 and later, Expressway X14.0 and later) are
                                                      adde to the Call Control Environment Requirements
                                                      section) Diagnostics in the Webex app Fixed error in "Configure Moving a Call into a
                                                   Meeting" section: Telephony must be enabled for
                                                this feature to work. Added more details about how to configure SSO Redirect
                                                URI on Expressway-C. |
| April 7, 2021 | Added new section "Configure Move Call into a
                                                   Meeting" (Deployment chapter) Added the following entries to the feature tables: Move a Call into a Meeting (Midcall
                                                      Features—Desktop and Mobile) In the Overview chapter, added more details about how
                                                Webex pulls configuration from Unified CM and the
                                                cloud. Improved the architecture section. |
| March 3, 2021 | Added minimum releases for APNs for China and non-China
                                                deployments. Added Call Recording to the MidCall Features table. In the Overview chapter, added architecture diagrams for
                                                internal and MRA deployments. |
| February 3, 2021 | In the "Policy Parameters" section in the Index, added the following new parameters: E911EdgeLocationWhiteList EnableE911EdgeLocationPolicy EnableE911OnPremLocationPolicy In the "Prepare Your Environment" chapter, added new sections on Push Notifications, Location Monitoring, and Cisco Unified Survivable Remote Site Telephony
                                                (SRST). Made the following changes to the Additional Features table: For the Call History entry in the Additional Features table, added information about deleting call entries and the 200 call
                                                      over 30 days limit. For the Suppress Notifications entry in the Additional Features table, added information about muting notifications during
                                                      a call or meeting. Added Location Monitoring for desktop and mobile. |
| January 12, 2021 | In the "Policy Parameters" section in the Index,
                                                added the following new parameters: SoftPhoneModeWindowBehavior DeskPhoneModeWindowBehavior In the "Prepare Your Environment" chapter, added new
                                                section on Call Park configuration. Made the following updates to the feature tables in the
                                                Overview chapter: Added the following feature to the Midcall
                                                      Features table: Park and retrieve calls |
| November 24, 2020 | In the "Policy Parameters" section in the Index,
                                                added the following new parameters: SelfCareURL ShowSelfCarePortal ShowCallAlerts Made the following updates to the feature tables in the
                                                Overview chapter: Added the following note to the "Call on Webex
                                                      Teams" row in the Additional Features table: Note Users only have access to the dial pad if they
                                                                  have a paid calling license. If they have a free
                                                                  calling license, they can still call other Webex
                                                                  Teams users. Added "Mirror Self-View" to the mobile column of
                                                      the Midcall Features table. Added the following note to the "Apple Push
                                                      Notifications (APNS) for iPhone and iPad and push
                                                      notifications for incoming calls on Android" row
                                                      in the Deployment Features table: Note Due to regulations in China, iPhone and iPad
                                                                  users no longer have the slide option to answer
                                                                  incoming calls when their mobile device is locked.
                                                                  Instead, they get an alert notification and must
                                                                  first unlock the screen and then tap the
                                                                  notification to answer the incoming calls. Added "Configure Self Care Portal Link" (desktop and mobile) to the Deployment Features
                                                      table. | Note | Users only have access to the dial pad if they
                                                                  have a paid calling license. If they have a free
                                                                  calling license, they can still call other Webex
                                                                  Teams users. | Note | Due to regulations in China, iPhone and iPad
                                                                  users no longer have the slide option to answer
                                                                  incoming calls when their mobile device is locked.
                                                                  Instead, they get an alert notification and must
                                                                  first unlock the screen and then tap the
                                                                  notification to answer the incoming calls. |
| Note | Users only have access to the dial pad if they
                                                                  have a paid calling license. If they have a free
                                                                  calling license, they can still call other Webex
                                                                  Teams users. |
| Note | Due to regulations in China, iPhone and iPad
                                                                  users no longer have the slide option to answer
                                                                  incoming calls when their mobile device is locked.
                                                                  Instead, they get an alert notification and must
                                                                  first unlock the screen and then tap the
                                                                  notification to answer the incoming calls. |
| October 29, 2020 | In the addition features table, added that "Add a Pause
                                                   to Dial String" is now supported on mobile. For the multiline and Jabber migration tool parameters,
                                                added a note that states that the parameters are not
                                                selectable presets in Unified CM. You must add these as
                                                custom parameters under policies. |
| September 30, 2020 | Restructured the feature overview table into four separate tables that cover basic call features, midcall features, additional
                                                features, and deployment features. Each table contains columns for desktop and mobile support so it's easier to see at a glance. In the feature overview tables, added the following entries: Control Your Video Device from the App (desktop, midcall features) Simplified call options (mobile, additional features) Contact Center integration (desktop, additional features) Jabra headset support (desktop, additional features) Multiline (desktop, midcall features) Extend and Connect (desktop, additional features) Dial via Office (DVO) (mobile, additional features) Customize virtual background (deployment features for desktop) Phone Service Connection Error and Action (additional features) Call Recording (additional features) Dial Plan Mapping (additional features) Added "Unified CM Feature Requirements" section in Prepare Your Environment chapter. Added subsections for additional features that need to be configured in advance
                                                to be available in Webex Teams. Added new section "Configure Users to Move Jabber Contacts and Common Settings to Webex Teams" to the Manage and Troubleshoot chapter. Moved "Policy Parameters" to Appendix, and added the following new parameters: RemoteDestinationEditingWithMultipleDevices RemoteInUsePresencePrimaryLineOnly SelfCareURL ShowSelfCarePortal UserDefinedRemoteDestinations EnableJabber2TeamsMigration WebexTeamsDownloadURL Added "Configure Virtual Background for Users" to Deployment chapter. |
| August 27, 2020 | In the feature overview table, added the following entries: Simplified call options (enable or disable and order call options)—deployment features for desktop Push Notifications for incoming calls on Android—mobile More calling options—desktop Mirror self-view—desktop Added new sections "Configure Push Notifications and Recommended Settings" and "Set Calling Options for Users" to the deployment chapter. In the Voicemail requirements in the prepare environment chapter, clarified that it's recommended to have Unified CM and Unity
                                                Connection  on the same release but required to have them use the same authentication type. Added Webex Teams for VDI as a supported option for calling. |
| August 10, 2020 | In the "Create and Configure Webex Teams Softphone Devices" section, added a step for configuring emergency numbers for mobile soft clients. |
| July 30, 2020 | Added "PreventDeclineOnHuntCall" to Policy Parameters for the XML config file steps. In the "Create a UC Manager Profile" section, added the following note: "Some deployments may require both a voice services and UDS domain. For users with Webex Teams accounts that don't match Unified
                                                   CM, Webex Teams cannot find the home cluster through voice services domain alone. In this case, you must configure the UDS
                                                   servers. The voice service domain is still required for Mobile and Remote Access (MRA) support and locating Expressway servers." In the feature table, added the following information: "If a user answers on desk phone, a screen share is still possible. The phone user sees the shared screen from the phone if
                                                         it supports video, otherwise they'll see the shared screen from the app." (Screen sharing for desktop) "When you add your coworker to your Contacts list, you can edit their profile and add additional phone numbers for them. Then,
                                                         you'll see the new phone number when you make an audio or video call, so it's easier to call them at their alternative number." (Contacts for desktop and mobile) |
| July 9, 2020 | In the deployment chapter, added new section "Voicemail Icon Indicators in Webex Teams " In the "Allow Untrusted Certificates on Unified CM" section, added the following paragraph: "For iOS devices, you must install a custom root CA on the devices themselves if you're using a private enterprise certificate.
                                                   Otherwise, Webex Teams fails to navigate to the SSO authorization URL." In the "Expressway Certificates (with MRA)" section, added the following note: "For MRA scenarios, certificates only need to be validated on the Expressway." In the "Configure Service Profile with UC Services" section, added a step to configure Credential source for voicemail service if not using SSO. In the "Service Discovery Options" section, updated the note on supported service discovery methods: "We support SRV look up over internal and MRA environments. Service discovery enables clients to automatically detect and locate
                                                   services on or outside your enterprise network. Clients query domain name servers to retrieve service (SRV) records that provide
                                                   the location of servers. See the DNS SRV guidance that follows for internal and external environments." |
| June 28, 2020 | In the feature overview table, added the following entries: Add Contacts, Search Your Contacts, and Make a Call (desktop and mobile) Missed calls (desktop) Call control for Webex Teams calls (desktop) Call Pickup (desktop and mobile) Share a specific application (desktop) Hunt Groups (desktop and mobile) Lock symbol for secure calls (deployment features—mobile) Added new sections to the deployment chapter that cover how to configure the XML config file for enabling hunt groups and
                                                call pickup for users: Set Client Configuration Parameters Create and Host Client Configuration Files |
| May 28, 2020 | In the feature overview table, added the following entries: Call history callback (mobile) Call statistics (mobile) Desk Phone Control for Webex Teams Calls (desktop) High Definition (HD) video (desktop) Health Checker for Phone Services Status (desktop) |
| May 6, 2020 | In the feature overview table, added the following entry: Auto-Discovery of Service Domain In the Deployment chapter, added or updated these sections: "UC Manager Profiles and Calling Behavior Workflow" (New) "Create a UC Manager Profile" (New) "Edit a UC Manager Profile" (New) "Set Calling Behavior and UC Manager Profiles in Control Hub" (Updated) |
| April 30, 2020 | In the feature overview table, added the following entries: Single Number Reach (mobile) Voicemail (mobile) Emergency Calling (mobile) Call Forwarding (mobile) Answer call without sharing video (mobile) |
| March 20, 2020 | In the feature overview table, added the following entries: Automatic Gain Control (AGC) (desktop and mobile) Conference calls (mobile) Merge (mobile) Visual voicemail (desktop—additional features) Added visual voicemail configuration requirements to the Prepare Your Environment and Deploy chapters. |
| February 27, 2020 | In the feature overview table, added the following entries: Call Waiting (mobile) Transfer (mobile) Support for tel, sip and clicktocall protocols (mobile) Control Hub headset management (additional features) Added the following information about Cisco 700 headsets: "If users have Cisco 700 series headset, they can use its USB adapter to answer and end calls, put calls on hold and resume
                                                   them, as well as mute and unmute calls." Added new section "Manage Cisco Headsets in Webex Control Hub" to the Manage and Troubleshoot chapter. Added new section "Protocol Handlers for Calling" to the Overview chapter. Readded Network Requirements section that was previously removed in error. |
| January 30, 2020 | In the feature overview table, added the following entries for Windows and Mac: Lock icon for secure calls. Support for Cisco 700 series (bluetooth) headsets. Popout call window. Add a pause to a dial string. In the "License Requirements for Calling in Webex Teams (Unified CM)" , clarified that while a paid subscriptions is required anduser accounts must be managed in your organization, the user accounts
                                                don't require a specific license assignment to use Calling in Webex App (Unified CM) . |
| December 20, 2019 | In the feature overview table, added the following entries: Hold/resume for mobile platforms. Resume on different devices for desktop, deskphone control mode, and mobile. Call history for mobile platforms. Added the following note to the Headset Requirements section: "When using the Cisco Headset 500 Series or Cisco Headset 700 Series headsets in Webex Teams, the headset firmware can get
                                                   updated automatically. Users can confirm the message that pops up letting them know that an update is available, and then
                                                   they'll get confirmation after it's updated." |
| December 10, 2019 | Added network requirements information to the Prepare Your Environment chapter. In the Configure SIP Address Routing for your Organization, section, added the following clarification: " *.example.com only matches subdomains, not top-level domains." |
| November 27, 2019 | Added call history to the feature overview table for desktop platforms. In the "Set DSCP Values on the Network" , changed the signaling packets marking from AF31 to CS3. |
| November 15, 2019 | In the Deploy chapter, added relevant deployment steps
                                                and Webex Teams authentication steps for mobile
                                                softphone mode. Added the following mobile features to the feature
                                                overview table: Make call Answer call Mute/Unmute End call On a Call presence—In Webex Teams, users in the
                                                      same organization can see this presence indicator
                                                      during an active call. Basic Shared Line Appearance DTMF input during the call |
| November 7, 2019 | Added the following features to the feature overview table: Webex Teams call (Windows or Mac)—Users can choose whether to call people using their phone number or using a Webex Teams
                                                      call. A Webex Teams call is a quick way to call someone else who's using Webex Teams. Users can share their screen and whiteboard
                                                      while in the call, but they can't put the call on hold, transfer the call, or use other features only available in phone calls. SIP (URI) address routing—Configurable in Control
                                                      Hub, this setting allows you to decide which SIP
                                                      addresses are routed through the Webex cloud​. The
                                                      default is for all SIP URIs to be routed through
                                                      Unified CM except for Webex services​. |
| October 9, 2019 | In Unified CM certificates (with MRA in deployment) , removed reference to Cisco CallManager certificate and added the following note: "The Tomcat certificate is also used for secure SIP when Webex Teams is enabled for encrypted calls (SIP Outh operates on the
                                                   default port 5091 for MRA). See "Configure the Phone Security Profile for Encrypted Calls" in this guide for more details." In Unified CM certificates (no MRA in deployment) , added the following note: "The Tomcat certificate is also used for secure SIP when Webex Teams is enabled for encrypted calls (SIP Oauth operates on
                                                   the default port 5090). See "Configure the Phone Security Profile for Encrypted Calls" in this guide for more details." |
| September 26, 2019 | Added the following features to the feature table in Overview of Calling in Webex App (Unified CM) : Suppress call notifications when presenting or when DND is enabled. Support for tel, sip and clicktocall protocols. Support for Click to Call from Outlook. Support for Cisco 500 series headsets Added new section Headset requirements Removed this incorrect known issue: "Webex Teams does not register to Unified CM in secure softphone mode. You must use non-secure mode as a workaround." Removed other incorrect information that stated secure mode wasn't supported. Fixed steps for SIP Oath configuration in Configure the phone security profile for encrypted calls . Called out that Unified CM 12.5(1) or later is required for encrypted calls. Added note to Authenticate with phone services in Webex App : "If both Server address and UC domain are configured, Server Address is used to connect to Unified CM while on-premises only.
                                                   Autodiscovery through DNS SRV is ignored. For MRA, Server Address is ignored." |
| August 29, 2019 | Added new section Configure the phone security profile for encrypted calls . For both softphone and desk phone control modes, added new midcall features to feature table in Overview of Calling in Webex App (Unified CM) : Conference Merge Transefer |
| July 25, 2019 | Rewrote the "Authenticate with Webex Teams" content to show the user configuration path to take if you have autodiscovery or if you don't. |
| July 9, 2019 | Removed the limited availability disclaimer for Merge and Transfer features for Webex Teams in softphone mode. (These features
                                                are now Generally Available.) |
| June 27, 2019 | Removed the Preview Release Disclaimer. (Calling in Webex Teams (Unified CM) is officially Generally Available.) Added Merge and Transfer as limited availability features for Webex Teams in softphone mode. Added new section Allow untrusted certificates on Unified CM to the Appendix. Added the following information to the certificate requirements and known issues: "Certificates issued with a deprecated signature algorithm (such as SHA-1) do not work; you must use a supported secure signature
                                                   algorithm such as SHA-256 or later, as documented in the Certificates chapter in the Administration Guide for Cisco Unified Communications Manager ." |
| June 14, 2019 | In Calling experience with Webex App for users , added the following information under the "User Experience Changes for Hybrid Call Service Users" section: "If the Webex device is configured in Control Hub as a Place that is enabled for Hybrid Call Service, the user can dial from
                                                   Webex Teams and the call then starts on the Webex device using that device's directory number as the caller ID on the receiving
                                                   end." In Certificate requirements , added MRA certificate requirements and restructured as 3 subsections: Unified CM Certificates (No MRA), Unified CM Certificates
                                                (MRA), and Expressway Certificates (MRA). In Set DSCP values on the network , corrected QoS port range information. Previously, it read "16384 to 24574" for audio streams and "24575 to 32766" for video
                                                streams; now, it reads "16384 to 24575" and "24576 to 32676", respectively. |
| April 24, 2019 | Restructured the Requirements section—Each Calling in Webex Teams (Unified CM) requirement now has its own subsection to make
                                                it easier to find. Added new section ( Configure Unified CM end users for Calling in Webex App (Unified CM) ) to the Deploy chapter. |
| April 10, 2019 | Added Meeting join in desk phone control mode to the Call Flows. In Requirements section, added the following points: In Cisco Unified CM Administration > System > Server , the Unified CM server names must be defined as FQDN. We do not support the deployment model of MRA without SSO and Unified CM with SSO. At this time, we support internal only automatic discovery. Service discovery enables clients to automatically detect and
                                                      locate services on your enterprise network. Clients query domain name servers to retrieve service (SRV) records that provide
                                                      the location of servers. If you're using Server Information for configuration and not SRV records, your users' Webex Teams email addresses must match
                                                      their Unified CM email addresses—at a minimum, the user ID portion before the domain must match. |
| March 28, 2019 | Initial version of the document. |

| Note | Users only have access to the dial pad if they
                                                                  have a paid calling license. If they have a free
                                                                  calling license, they can still call other Webex
                                                                  Teams users. |
|---|---|

| Note | Due to regulations in China, iPhone and iPad
                                                                  users no longer have the slide option to answer
                                                                  incoming calls when their mobile device is locked.
                                                                  Instead, they get an alert notification and must
                                                                  first unlock the screen and then tap the
                                                                  notification to answer the incoming calls. |
|---|---|

| Feature | Description and documentation | Desktop | Mobile |
|---|---|---|---|
| Answer call | — | ✓ | ✓ |
| Answer call without sharing video | See Turn Off Your Video for all Incoming
                                                Calls . | ✓ | ✓ |
| Desk Phone Control | Desk Phone Control (including meetings and calls in Webex App )—See Make
                                                Calls With Your Desk Phone . | ✓ |  |
| DTMF input during the call | — | ✓ | ✓ |
| End call | — | ✓ | ✓ |
| Make call | — | ✓ | ✓ |
| Mute/Unmute | — | ✓ | ✓ |
| On a Call presence | In Webex App , users in the same organization can see this presence
                                             indicator during an active call. | ✓ | ✓ |

| Feature name | Description and documentation | Desktop | Mobile |
|---|---|---|---|
| Call Pickup | If a user is in a customer support role and their coworker isn't able to
                                             answer an incoming call to their phone, the support user gets a notification in Webex App if both are in the same pickup group. That user can answer their call from the
                                             notification in the app. The user can also pick up the calls in other pickup
                                             groups. See Pick Up Someone Else's Call . | ✓ | ✓ |
| Call Recording | You can determine how much control users have over recording calls. Depending on
                                             the setup, incoming and outgoing calls may be recorded automatically or you may be
                                             able to decide which calls you want to record. If you enable users with call
                                             recording, they can start and stop recordings at their own discretion. When a call
                                             is being recorded, that recording continues whether a user moves the call to
                                             another device, merges the call with another active call, or makes a conference
                                             call. They're presented with a visual indicator letting them know when a call is
                                             being recorded. See Record Your Phone Calls . | ✓ | ✓ |
| Call Waiting | When a user is already in call and someone else calls, the called user can choose
                                             how they want to handle the incoming call. For example, the user can put the
                                             active call on hold and answer the second call. See Answer Call Waiting for more information. | ✓ | ✓ |
| Conference calls | When users are on a call with someone else, they might want to add other people
                                             into the call to start a conference call right away. They can add up to 8 other
                                             people into conference calls started in this way. See Start a Conference
                                                Call . | ✓ | ✓ |
| Control Your Video Device from the App | Users can start or stop sharing your video on a connected video device right from
                                             the app. For example, if connected to a Cisco Webex Board and users don't want
                                             to share video, they no longer have to walk up to the board and turn off the
                                             video. They can turn it off from the app. See Turn Off Your Video
                                                During a Meeting or Call On Webex Boards, Room and Desk Devices . | ✓ |  |
| Hold/resume | Users place a call on hold and resume in Webex App . See Put a Phone Call On Hold . | ✓ | ✓ |
| Hunt Groups | Users can sign in or out of a Hunt Group from Call Settings. When they're
                                             signed in and a call comes into a group that they belong to, they'll see the
                                             Hunt Group number on the incoming call notification. Sign in to a Hunt
                                                Group . | ✓ | ✓ |
| Merge | Users take 2 active calls and merge them into a single conference call in Webex App . See Merge Two Phone Calls . | ✓ | ✓ |
| Mirror self-view | Mirror self-view—By default, when users share video during a call, they can see
                                             themselves just like you're looking in a mirror. If they text behind them and
                                             want to read it easily instead of having to read it backwards, tehey may want to
                                             off the Mirror my video view setting. This setting doesn't affect the
                                             way other people in the meeting see you. See Turn Off Mirror View for
                                                Your Self-View Video. . | ✓ | ✓ |
| Move a call into a meeting | Users in a call can take advantage of advanced meetings features such as
                                             transcriptions, real-time translations, notes, action items, recordings, and
                                             whiteboarding. Just move that call into a full-featured meeting. Before moving the
                                             call into a meeting, users can even invite other people into the discussion. | ✓ | ✓ |
| Multiline | Users can use up to 10 phone lines (on desktop) and 8 phone lines (on mobile) with Webex App and leverage advanced calling features on each line such as call forward, transfer, hunt group, shared lines, and voicemail.
                                             And you can turn on presence for shared lines so that line status is displayed for users. See Multiline and Change the Active Line for Calling . Note Once Webex users have enabled multiline on mobile, they will no longer be able to sign in to phone services in the Webex mobile
                                                               app prior to version 44.12. Ten-line support and multiline on mobile will not work for Jabber. Adding either of them to Unified CM will result in phone
                                                               services registration failure on Jabber. | Note | Once Webex users have enabled multiline on mobile, they will no longer be able to sign in to phone services in the Webex mobile
                                                               app prior to version 44.12. Ten-line support and multiline on mobile will not work for Jabber. Adding either of them to Unified CM will result in phone
                                                               services registration failure on Jabber. | ✓ | ✓ |
| Note | Once Webex users have enabled multiline on mobile, they will no longer be able to sign in to phone services in the Webex mobile
                                                               app prior to version 44.12. Ten-line support and multiline on mobile will not work for Jabber. Adding either of them to Unified CM will result in phone
                                                               services registration failure on Jabber. |
| Park and retrieve calls | Users can park a call on one device and that user or someone else can retrieve
                                             the call from another device. | ✓ | ✓ |
| Resume from different devices | A user can put a call on hold from the desktop app and resume it on mobile. Or,
                                             put your mobile call on hold and resume it on a desk phone. Go any direction
                                             between desk phone, mobile, and desktop; just put the call on hold and resume
                                             wherever it's convenient. See Put a Phone Call On
                                                Hold . | ✓ | ✓ |
| Screen sharing | Screen sharing—Share content from a computer screen during a call in Webex App . Users can choose a specific application to share, rather than having to share
                                             their whole screen. If a user answers on desk phone, a screen share is still
                                             possible. The phone user sees the shared screen from the phone if it supports
                                             video, otherwise they'll see the shared screen from the app. See Share Your Screen in a Phone Call . Note Users can share your screen regardless of whether the person they called is
                                                         using a cloud-registered device or an on-premises device. The screen share is
                                                         still sent with a high frame rate (30 FPS), high resolution (1080p), and
                                                         includes audio. | Note | Users can share your screen regardless of whether the person they called is
                                                         using a cloud-registered device or an on-premises device. The screen share is
                                                         still sent with a high frame rate (30 FPS), high resolution (1080p), and
                                                         includes audio. | ✓ |  |
| Note | Users can share your screen regardless of whether the person they called is
                                                         using a cloud-registered device or an on-premises device. The screen share is
                                                         still sent with a high frame rate (30 FPS), high resolution (1080p), and
                                                         includes audio. |
| Switch between front and back cameras | On mobile phones or tablets, you can switch between front-facing and back-facing
                                             cameras. See the mobile sections in Change Your Video
                                                Settings . |  | ✓ |
| Transfer | Redirects a connected call within Webex App . The target is the user to which another user wants to transfer the call. See Transfer a Phone Call . | ✓ | ✓ |
| Virtual cameras | During a call, users can choose to use a virtual camera. Use a virtual camera,
                                             such as an application, driver, or software, to create an overlay of video,
                                             images, or feeds. | ✓ |  |

| Note | Once Webex users have enabled multiline on mobile, they will no longer be able to sign in to phone services in the Webex mobile
                                                               app prior to version 44.12. Ten-line support and multiline on mobile will not work for Jabber. Adding either of them to Unified CM will result in phone
                                                               services registration failure on Jabber. |
|---|---|

| Note | Users can share your screen regardless of whether the person they called is
                                                         using a cloud-registered device or an on-premises device. The screen share is
                                                         still sent with a high frame rate (30 FPS), high resolution (1080p), and
                                                         includes audio. |
|---|---|

| Feature name | Description and documentation | Desktop | Mobile |
|---|---|---|---|
| Add a Pause to Dial String | Users can add a pause to an entered phone number, which they might need if joining a conference call and need to enter numbers
                                             in response to the automated system. They can add a comma (,) to the number, which gives a 1-second delay in the dialing.
                                             They can add several commas in a row to extend the delay. For example: 95556543123,,,,56789. | ✓ | ✓ |
| Add Contacts, Search Your Contacts, and Make a Call | Users can add coworkers into a Contacts list and group them however they like, making people easier to find when users need
                                             to chat or call. Users can even look up Outlook contacts (Windows), local address book (Mac), and local phone contacts (iPhone, iPad, and Android)
                                             from Webex App , so they can easily find contacts and make a call. When you add your coworker to your Contacts list, you can edit their profile and add additional phone numbers for them. Then,
                                             you'll see the new phone number when you make an audio or video call, so it's easier to call them at their alternative number.
                                             See Add Someone to Your Contacts List . | ✓ | ✓ |
| Automatic Gain Control (AGC) | AGC is a unique circuit that listens to the incoming audio level and adjusts the recording level when sounds are too loud
                                             or too soft. When the audio volume is too loud, it automatically reduces the sound. When the audio is too soft, it automatically
                                             amplifies the sound. This doesn't adjust the audio volume at the OS level. | ✓ | ✓ |
| Call on Webex App | Users can choose whether to call people using their phone number or using a call
                                             in Webex App . A call in Webex App is a quick way to call someone else who's using Webex App . Users can share their screen and whiteboard while in the call, but they
                                             can't put the call on hold, transfer the call, or use other features only
                                             available in phone calls. See Call Anyone with
                                             a Webex App account. Note Users only have access to the dial pad if they have a paid calling license. If
                                                         they have a free calling license, they can still call other Webex App users. | Note | Users only have access to the dial pad if they have a paid calling license. If
                                                         they have a free calling license, they can still call other Webex App users. | ✓ | ✓ |
| Note | Users only have access to the dial pad if they have a paid calling license. If
                                                         they have a free calling license, they can still call other Webex App users. |
| Call control for calls in Webex App | If using a Cisco 730 headset, users can use its USB adapter or Bluetooth to answer and end calls, put calls on hold and resume
                                             them, as well as mute and unmute calls. See Make and Answer Calls on the Cisco Headset 730 . | ✓ |  |
| Call history | When a user calls other people in the organization, they see more details about phone numbers in the call history. So, to
                                             call someone back, that user can see if they're calling a work or mobile number. Users can select the Call icon beside someone’s name or number in their Call
                                             History and automatically call the person back at the number in the history. Users
                                             no longer need to choose what number to reach others at. After they return a
                                             missed call, they can delete the call from call history. The call history only
                                             shows the last 200 calls over the last 30 days. See View Call and
                                                Meeting History for more information. | ✓ | ✓ |
| Call Statistics | When users are in a call, they can check call statistics, such as packet loss, latency, and resolution rate. See Access Call Statistics . |  | ✓ |
| Click to Call from Outlook | You can set up your Windows or Mac computer so that Webex App is the default option for calling numbers that you click outside of the app, for example, in Microsoft Outlook or from a
                                             link in your web browser. See Click to Call From Another App . | ✓ |  |
| Client Matter Codes (CMCs) and Forced Authorization Codes (FMCs) | With client matter codes (CMCs) and forced authorization codes (FACs), you can
                                             effectively manage call access and accounting. CMCs assist with call accounting
                                             and billing for clients, and FACs regulate the types of calls that certain users
                                             can place. CMCs force the user to enter a code; this action specifies that the call relates
                                             to a specific client matter. You can assign client matter codes to customers,
                                             students, or other populations for call accounting and billing purposes. FACs
                                             force the user to enter a valid authorization code that is assigned at a certain
                                             access level before the call is completed.  See the "Prepare Your
                                                Environment" chapter. | ✓ | ✓ |
| Contact Center Integration | Webex App can integrate into your Cisco Contact Center application and be controlled in
                                             Finesse desktop (Unified Contact Center Enterprise or Express). This integration
                                             supports contact center features such as multiline, recording, conferencing, and
                                             more. See Contact Center Integration for the latest supported
                                             features. | ✓ |  |
| Diagnostics in the Webex App | If users experience connection issues, they can use the diagnostic tool to
                                             identify configuration errors or export a network diagnostics report. This
                                             information helps you troubleshoot any issues they're experiencing. See the
                                             Troubleshooting chapter. | ✓ |  |
| Dial-via-Office (DVO) | When you set up users with DVO, they have the option to make work calls using their mobile phone connection, which ensures
                                             calls are uninterrupted even if data is unavailable. No matter what option they choose, the work number is always used as
                                             the caller ID so people can easily identify users. See Make Work Calls Over a Mobile Phone Connection . |  | ✓ |
| Dial Plan Mapping | You configure dial plan mapping to ensure that dialing rules on Cisco Unified Communications Manager match dialing rules on
                                             your directory. See the Prepare Your Environment chapter. | ✓ | ✓ |
| Emergency calls | If users make an emergency call in Webex App , the call is made using the device’s Phone app, making it easier for Emergency Services to pinpoint a location through their
                                             network carrier. |  | ✓ |
| Extend and Connect | You can set up users to connect to alternate devices to make and receive calls. Users can see those devices under Alternate Devices when they go to calling settings. That's where they can add or edit the phone numbers for those devices. See Make a Call From an Alternate Device . | ✓ |  |
| Fast failover (MRA) | Webex can detect failure quickly, whether it's a controlled shutdown, node
                                             failure, or network failure, and seamlessly fail over to a backup path through MRA
                                             so user productivity isn't affected. See the Prepare Your Environment chapter. | ✓ | ✓ |
| Health Checker for Phone Services Status | If unsure whether Phone Service is working properly, users can check out the status of the phone connection from the app.
                                             On Windows, they click their profile picture and then go to Help > Health Checker . On Mac, they go to Help > Health Checker . Health Checker tests the connection and lets users know if there's a problem. | ✓ |  |
| High Definition (HD) Video | Users can enable or disable HD video by clicking their profile picture, going to Settings (Windows) or Preferences (Mac), selecting Video , and then enabling or disabling the setting. They may want to disable HD video if their computer CPU is running high or they
                                             want to save network bandwidth during a call or meeting. | ✓ |  |
| Location Monitoring | You can turn on location monitoring so that when users call emergency services
                                             from Webex (for example, 911), their location is automatically shared with
                                             emergency responders. | ✓ | ✓ |
| Missed calls | See how many calls you’ve missed with a red badge counter in the Calls tab. The Calls tab shows a list of incoming and outgoing calls and you can call someone back from your Call History. Your
                                             scheduled meetings are listed in the Meetings tab, making it easier for you to distinguish between the two types of communication. | ✓ |  |
| More calling options | Users can call someone's video address (for example, bburke@biotechnia.com) from anywhere in the app where they'd make any
                                             type of call (example: search for someone or being in a space with that person). | ✓ |  |
| Multi call window | Webex App users with multiple lines see this by default. It is a separate, floating window to help with managing multiple
                                             or shared lines. See Manage your phone calls in the Multi Call window . | ✓ (Windows) |  |
| Network Handoff (Wi-Fi to LTE) | When you're on an active call and you need to change networks but want to keep
                                             the call in Webex, no need to worry; the change is made automatically without any
                                             interruption or effect to call quality. (See Unified CM features in Prepare Your
                                             Environment.) | ✓ | ✓ |
| Phone numbers in contact cards | Work numbers and mobile numbers are synchronized from Active Directory and appear as selectable items in Webex App . (Requires Cisco Directory Connector to synchronize user phone number attributes to the Webex cloud.) | ✓ | ✓ |
| Phone Service Connection Error and Action | The footer in Webex App shows more descriptive error messages if the phone service disconnects. See Error Messages . | ✓ | ✓ |
| Popout Call Window | When a user calls someone else, the call window pops out, and both users can access calling features. While in the call, users
                                             can still respond to critical messages. | ✓ |  |
| PSTN calling for mobile app users in India | Users in India can make that call when they can't be on the corporate network.
                                             The Webex mobile app gives them the option to use the device's calling app
                                             instead. See "EnablePhoneDialerOptionOverMRA" in the customization policy
                                             parameters in the Appendix. |  | ✓ |
| PSTN for Personal Mode Devices | Leveraging Hybrid Calling, you can provide PSTN access to users' personal mode
                                             devices. (See the Deployment Guide for Hybrid Calling for Cisco
                                                Webex Devices .) | ✓ |  |
| RedSky location reporting for emergency calling | To comply with Ray Baum's act, you can require users to give accurate location
                                             information when they are outside the office.​ | ✓ | ✓ |
| Self Care Portal—Call forwarding | If users need to take your work calls from another number, they can set up call forwarding right from Webex App . They just enter the call forwarding number, and their calls all ring at that number. See Forward Phone Calls and Access More Call Settings . | ✓ | ✓ |
| Self Care Portal—Single Number Reach (SNR) | Users can access the Self Care Portal from Webex App and add more numbers for devices they want to ring simultaneously with their enterprise directory number. See Get Work Calls at Any Number and Access More Call Settings . | ✓ | ✓ |
| Support for Cisco 500 series and 700 series (bluetooth) headsets | If users have the Cisco 700 series headset, they can use its USB adapter to answer and end calls, put calls on hold and resume
                                             them, as well as mute and unmute calls. When users use a Cisco headset with Webex App , you can now keep track of it in Webex Control Hub. This lets you track inventory and troubleshoot issues for your users.
                                             (See the deployment chapter.) | ✓ |  |
| Support for Jabra headsets | See Details%20about%20Headset%20Support for supported models. | ✓ |  |
| Suppress call notifications when presenting, when DND is enabled, or when you're
                                             already in a call or meeting. | Users can mute notifications for incoming calls so that they don't see or hear
                                             someone calling. If voicemail is set up, the caller can leave a message. The call
                                             still shows up in the spaces list and call history. | ✓ |  |
| Switch your call from Webex to your mobile phone app | When you're on an active call in Webex and you want to take your call on the run,
                                             just switch your call from Webex to your mobile phone app. You maintain
                                             connectivity and call quality with only a short pause in your call while you make
                                             the quick switch from More . (See the Deployment chapter and Switch Your
                                                Call to Your Mobile Phone App .) |  | ✓ |
| tel, sip and clicktocall protocol | See the relevant section in this overview chapter. | ✓ | ✓ |
| Voicemail | No more missing calls in Webex App . Users can manage their voicemail in the Calls tab. There's a red badge counter that lets them know how many voice messages
                                             they have. They can check out the details of a message, play it, mark it as read, delete it, or call back the sender. After
                                             they listened to messages, either with Webex App or desk phone, the red badge counter disappears. See Voicemail . | ✓ | ✓ |
| Visual Voicemail | Visual voicemail—No more missing calls in Webex App . Users get a dedicated Voicemail tab to manage all their voicemails. There's a red badge counter that lets them know how many voice messages they have. They can
                                             check out the details of a message, play it, mark it as read, delete it or call back the sender. After they listened to your
                                             messages, either with Webex App or your desk phone, the red badge counter disappears. See Voicemail . | ✓ |  |

| Note | Users only have access to the dial pad if they have a paid calling license. If
                                                         they have a free calling license, they can still call other Webex App users. |
|---|---|

| Feature name | Description and Documentation | Desktop | Mobile |
|---|---|---|---|
| Apple and Android Push Notifications (APNs) | On iPhone, iPad, and Android devices, push notifications let the
                                             user know about incoming calls in Webex App . (See the "Prepare Your Environment" chapter.) Note Due to regulations in China, iPhone and iPad users no longer
                                                         have the slide option to answer incoming calls when their
                                                         mobile device is locked. Instead, they get an alert
                                                         notification and must first unlock the screen and then tap
                                                         the notification to answer the incoming calls. | Note | Due to regulations in China, iPhone and iPad users no longer
                                                         have the slide option to answer incoming calls when their
                                                         mobile device is locked. Instead, they get an alert
                                                         notification and must first unlock the screen and then tap
                                                         the notification to answer the incoming calls. |  | ✓ |
| Note | Due to regulations in China, iPhone and iPad users no longer
                                                         have the slide option to answer incoming calls when their
                                                         mobile device is locked. Instead, they get an alert
                                                         notification and must first unlock the screen and then tap
                                                         the notification to answer the incoming calls. |
| Local Push Notification Service (LPNS) | This is a reliable and secure way to notify Webex  users on iOS devices of incoming VoIP calls under the following operating
                                             conditions: In a WiFi-constrained network. No Internet connection hence cannot access Apple Push Notification Service(APNs). Note To get LPNS call notifications, users must grant the Local Network permission to Webex App. If both LPNS and APNs are configured on UCM, UCM will deliver the call through the LPNS channel first, if it fails, APNs will
                                                               be the fallback option with the best effort. To get LPNs call notifications working properly, when the users have multiple iPhones or iPads, they must ensure the Webex
                                                               app runs only on one iPhone and one iPad. | Note | To get LPNS call notifications, users must grant the Local Network permission to Webex App. If both LPNS and APNs are configured on UCM, UCM will deliver the call through the LPNS channel first, if it fails, APNs will
                                                               be the fallback option with the best effort. To get LPNs call notifications working properly, when the users have multiple iPhones or iPads, they must ensure the Webex
                                                               app runs only on one iPhone and one iPad. |  | ✓ iOS and iPad OS |
| Note | To get LPNS call notifications, users must grant the Local Network permission to Webex App. If both LPNS and APNs are configured on UCM, UCM will deliver the call through the LPNS channel first, if it fails, APNs will
                                                               be the fallback option with the best effort. To get LPNs call notifications working properly, when the users have multiple iPhones or iPads, they must ensure the Webex
                                                               app runs only on one iPhone and one iPad. |
| Auto-Discovery of Service Domain | You can use Control Hub to configure a UC manager profile to add
                                             a service domain automatically to users' Phone Services settings in Webex App . That way, they don't need to manually enter a domain and can
                                             sign in right away. (See the deployment chapter.) | ✓ | ✓ |
| Configure Self Care Portal Link | You can choose the portal link for your users when they access it
                                             from the Call Settings in their app. (See the deployment
                                             chapter for config file steps and the appendix for related
                                             policy parameters.) | ✓ | ✓ |
| Customize virtual background | You can let users add up to 3 images of their own to use for
                                             virtual backgrounds. See Configure Virtual Backgrounds for Webex
                                                Users . | ✓ |  |
| Customize emergency dialing disclaimer | You can customize the content of the emergency dialing disclaimer
                                             to meet regulations and business needs in various regions and
                                             situations. You can also change the frequency of the disclaimer pop-up, or
                                             hide the disclaimer if the emergency responder infrastructure is
                                             not ready. (See the customizable parameters in the
                                             Appendix.) | ✓ | ✓ |
| Disable video for all 1:1 calls | Using Control Hub, you can disable video for calling or set the
                                             default to video off for compliance, privacy, or network
                                             purposes. | ✓ | ✓ |
| Expressway Mobile Remote Access (MRA) for Webex App | MRA provides a secure connection for Webex App traffic without having to connect to the corporate network
                                             over a VPN. (See the Mobile and Remote Access
                                                Through Cisco Expressway Deployment Guide .) | ✓ | ✓ |
| Secure and encrypted calls | Encrpyted calls are configurable from Unified CM and indicated by
                                             a lock icon in Webex App . (See the deployment chapter.) | ✓ | ✓ |
| Service Discovery | Service discovery enables clients to automatically detect and
                                             locate services on your enterprise (internal) and MRA (external)
                                             network. (See the deployment chapter.) | ✓ | ✓ |
| Simplified call options (enable or disable and order call
                                             options) | You can set up user calling options to suit their needs. For
                                             example, they may not need to make Webex App calls and only want to call coworkers using their work
                                             number, mobile number, or SIP URI address. You can disable calls
                                             in Webex App so they don't have that option show up when they make a call.
                                             See Configure Call Settings for Your
                                                Organization . | ✓ | ✓ |
| SIP (URI) address routing | Configurable in Control Hub, this
                                                setting allows you to decide which SIP addresses are routed
                                                through the Webex cloud​. The default is for all SIP URIs to
                                                be routed through Unified CM except for Webex
                                                services​. See Configure SIP Address Routing for Your
                                                Organization . | ✓ |  |
| Single Sign-On (SSO) | With SSO integration between your IdP, your premises environment,
                                             and the Webex cloud, users can sign in across applications with
                                             one set of credentials. (See the "Prepare Your Environment" chapter.) | ✓ | ✓ |
| Virtual cameras (macOS) | You can use Webex Control Hub to enable or disable virtual camera
                                             usage for your users' calls and meetings in the Webex app. Users
                                             can use a virtual camera, such as an application, driver, or
                                             software, to create an overlay of video, images, or feeds. | ✓ (macOS only) |  |

| Note | Due to regulations in China, iPhone and iPad users no longer
                                                         have the slide option to answer incoming calls when their
                                                         mobile device is locked. Instead, they get an alert
                                                         notification and must first unlock the screen and then tap
                                                         the notification to answer the incoming calls. |
|---|---|

| Note | To get LPNS call notifications, users must grant the Local Network permission to Webex App. If both LPNS and APNs are configured on UCM, UCM will deliver the call through the LPNS channel first, if it fails, APNs will
                                                               be the fallback option with the best effort. To get LPNs call notifications working properly, when the users have multiple iPhones or iPads, they must ensure the Webex
                                                               app runs only on one iPhone and one iPad. |
|---|---|

| Note | Webex App does not support Extension Mobility. |
|---|---|

| Calls through Unified CM
                                             environment | Calls and meetings through Webex cloud |
|---|---|
| Calls initiated directly from a
                                             1:1 space or from a contact card in the Webex App | Ad hoc meetings from a group
                                             space in the Webex App |
| Search and then call a user in
                                             the Webex App | Using the Join button in the Webex App to join an ad hoc or scheduled meeting |
| Dialing directory numbers or PSTN
                                             numbers from Call in the Webex App | Dialing premises Directory URIs
                                             from Call in the Webex App . (Depends on the Unified CM SIP
                                                Address Routing setting in Control
                                             Hub.) |
| Desk phone control (DPC) calls
                                             (outgoing: dial a directory or PSTN number in the Webex App , take the call on the Unified CM device;
                                             incoming: answer the call in Webex App , take the call on the device). | Joining a meeting while paired through Room, Desk, or Board devices |
| 1:1 calls that are placed
                                             directly in the Webex App to a free user in the consumer organization, to
                                             a user in another organization, or to a user in
                                             the same organization who doesn't have a directory
                                             number. (Numbers are not shared across
                                             organizations, so don't appear in contact cards.)
                                             These are classified as a Call on Webex App . |

| Icon | Protocol | Purpose |
|---|---|---|
|  | HTTPS | Webex cloud services, Visual Voicemail |
|  | SIP | Softphone Mode |
|  | CTI/QBE | Deskphone Control |
|  | LDAP | Directory |
|  | DNS | Service Discovery |
|  | SP Agreement | Single Sign-On (SSO) Agreement |

| Icon | Protocol | Purpose |
|---|---|---|
|  | HTTPS | Webex cloud services, Visual Voicemail |
|  | SIP | Softphone Mode |
|  | LDAP | Directory |
|  | DNS | Service Discovery |
|  | SP Agreement | Single Sign-On (SSO) Agreement |