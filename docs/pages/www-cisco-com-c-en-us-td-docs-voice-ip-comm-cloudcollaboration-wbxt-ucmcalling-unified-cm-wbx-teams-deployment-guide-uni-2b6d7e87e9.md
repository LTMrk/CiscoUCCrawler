---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-wbxt-ucmcalling-unified-cm-wbx-teams-deployment-guide-uni-2b6d7e87e9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wbxt/ucmcalling/unified-cm-wbx-teams-deployment-guide/unified-cm-wbx-teams-deployment-guide_preface_011.html
retrieved_at: 2026-08-21T20:26:03.629805+00:00
---

Deployment guide for Calling in Webex App (Unified CM)

# Deployment guide for Calling in Webex App (Unified CM)

Updated: April 10, 2019

Chapter: New and changed information

## Chapter: New and changed information

- New and changed information

# New and changed information

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

| Date | Changes Made |
|---|---|
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