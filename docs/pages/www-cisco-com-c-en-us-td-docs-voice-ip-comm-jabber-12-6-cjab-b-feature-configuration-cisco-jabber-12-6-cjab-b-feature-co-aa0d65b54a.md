---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-6-cjab-b-feature-configuration-cisco-jabber-12-6-cjab-b-feature-co-aa0d65b54a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_6/cjab_b_feature-configuration-cisco-jabber_12-6/cjab_b_feature-configuration-cisco-jabber_12-6_chapter_01.html
retrieved_at: 2026-08-21T05:14:15.070854+00:00
---

Feature Configuration for Cisco Jabber 12.6

# Feature Configuration for Cisco Jabber 12.6

Updated: April 9, 2019

Chapter: Getting Started

## Chapter: Getting Started

# Getting Started

## About Cisco
                        	 Jabber

Cisco Jabber is a suite of Unified Communications applications that allow seamless interaction with your contacts from anywhere.
                              Cisco Jabber offers IM, presence, audio and video calling, voicemail, and conferencing.

The applications in the Cisco Jabber family of products are:

Cisco Jabber for Windows

Cisco Jabber for Mac

Cisco Jabber for iPhone and iPad

Cisco Jabber for Android

Cisco Jabber Softphone for VDI

For more information about the Cisco Jabber suite of products, see https://www.cisco.com/go/jabber or https://www.cisco.com/c/en/us/products/unified-communications/jabber-softphone-for-vdi/index.html .

## Purpose of this Guide

This document describes some of the features of Cisco Jabber.  Configuration information and the list of supported clients
                              is given for each feature.

## Feature Configuration Overview

The following table provides an alphabetical list of the features described in this document, and lists which clients are
                              supported for each feature.

Feature Name

Description

Supported Clients

ActiveControl

Blocked Domain Support for Webex Messenger Users

Bots

A chat bot is an automated service that appears and behaves like a user in Jabber. A Jabber user can add a chat bot to their
                                          Contacts list and start a chat conversation with the bot.

All clients

Bridge Escalations

Bridge escalations allow users to quickly escalate a group chat to a conference call.

All clients

Browser Click to Call

Users can start a call from a browser by right-clicking on any number, URI, or alphanumerical string.

Cisco Jabber for Windows

Cisco Jabber Softphone for VDI

Calendar Integration and Contact Resolution

Lets users view their events from the Meetings tab. Also, let users search for their local contacts.

All clients

Call Park

You can use call park to place a call on hold and pick it up from another phone in a Cisco UnifiedCommunication Manager system.

Cisco Jabber for mobile clients

Call Pickup

Call pickup allows users to pick up incoming calls from a group.

Cisco Jabber for Windows

Cisco Jabber for Mac

Cisco Jabber Softphone for VDI

Chat History in Microsoft Outlook

Allow users to automatically save chat histories to a Cisco Jabber Chats folder in the user's Microsoft Outlook application.

Cisco Jabber for Windows

Cisco Jabber for Mac

Cisco Jabber Softphone for VDI

Chromebook

Allow users to download Cisco Jabber for Android into their Chrombook from Google Play Store. Cisco Jabber on Chromebook works
                                          as an Android tablet. Users can access all Cisco Jabber services on Chromebook when connecetd over MRA.

Cisco Jabber for Android.

Cisco Jabber Mobile App Promotion

Allow users to enable a notificaton to promote the use of the Cisco Jabber for Mobile App (Android and iOS).

Cisco Jabber for Windows

Cisco Jabber Softphone for VDI

Collaboration Meetings Rooms

Cisco Collaboration Meeting Rooms (CMR) Cloud provides easy access for users to join or start Cisco Webex Meetings .

All clients

Custom Embedded Tabs

Custom embedded tabs display HTML content in the client interface.

All clients

Custom Emoticons

Add custom emoticons to Cisco Jabber for Windows by creating emoticon definitions in an XML file and saving it to the file
                                          system.

Cisco Jabber for Windows

Cisco Jabber Softphone for VDI

Dial via Office

The DvO feature allows users to initiate Cisco Jabber outgoing calls with their work number using the mobile voice network
                                          for the device.

Cisco Jabber for mobile clients

DND Status Cascading

When a user manually sets the IM Presence status as Do Not Disturb from the Cisco Jabber client, then the status is cascaded
                                          down to all the phone devices that are owned by the user.

All clients

Enterprise Groups for Cisco Unified Communications Manager IM and Presence Service

Cisco Jabber users can search for groups in Microsoft Active Directory and add them to their contact lists.

All clients

Far End Camera Control

Allow users to adjust the far-end camera to give a better view during video calls.

All clients

File Transfers and Screen Captures

Allow users to transfer files and screen captures to other users, ad hoc group chat rooms, and persistent chat rooms.

All clients

Flexible DSCP Values

Flexible Differentiated Services Code Point (DSCP) allows you to specify different DSCP values to separate the audio and video
                                          streams on the network.

Cisco Jabber for Mac

Cisco Jabber for mobile clients

Hunt Group

A Hunt Group is a group of lines that are organized hierarchically, so that if the first number in the hunt group list is
                                          busy, the system dials the second number. If the second number is busy, the system dials the next number, and so on.

All clients

IBM Notes Contact Search and Calendar Integration

Cisco Jabber for Windows supports IBM Notes calendar integration in the Meetings tab of the client. Cisco Jabber also lets
                                          users search for and add local contacts from IBM Notes.

Cisco Jabber for Windows

Cisco Jabber Softphone for VDI

Integration with Microsoft Products

Cisco Jabber supports a range of Microsoft products that integrate with the application:

Internet Explorer

Microsoft Office

Microsoft Office 365

Microsoft SharePoint

Cisco Jabber for Windows

Cisco Jabber for Mac

Cisco Jabber Softphone for VDI

Jabber to Jabber Call

Jabber to Jabber voice and video calling provides basic calling capabilities between two Cisco Jabber clients without using
                                          Cisco Unified Communications Manager.

All clients

Let Users Without Voicemail Ignore Calls

Choose a No Voicemail profile for users who don't have voicemail configured.

All clients

Location Sharing

Allow users to share their location with their contacts.

Cisco Jabber for Windows

Cisco Jabber for Mac

Logout Inactivity Timer

The sign out inactivity timer allows you to automatically sign users out of the client after a specified amount of time of
                                          inactivity.

All clients

Mac Calender Integration for Meetings

Allow users to connect their calendars to their Cisco Jabber client.

Cisco Jabber for Mac

Microsoft Outlook Calendar Events

Display Microsoft Outlook calendar events in the Meetings tab of Cisco Jabber.

Cisco Jabber for Windows

Cisco Jabber Softphone for VDI

Microsoft Outlook Presence Integration

Display presence status in Microsoft Outlook

Cisco Jabber for Windows

Cisco Jabber for Mac

Cisco Jabber Softphone for VDI

Move to Mobile

Users can transfer an active VoIP call from Cisco Jabber to their mobile phone number on the mobile network.

Multiline

You can configure multiple phone lines for your users to perform daily Cisco Jabber tasks. You can add up to eight phone lines
                                          per user.

Cisco Jabber for Windows

Cisco Jabber for Mac

Multiple Device Messaging for Cloud Deployments

Users who are signed into multiple devices can see all sent and received IMs on each device regardless of which device is
                                          active.

All clients

My Jabber Chats and My Jabber Files Directory Location

Specify a directory location for saved instant messages and file transfers, or let users specify their own location.

Cisco Jabber for Windows

Cisco Jabber Softphone for VDI

Persistent Chat Rooms

Persistent chat is a permanent chat room that offers ongoing access to a discussion thread. It is available even if no one
                                          is currently in the chat room and remains available until explicitly removed from the system.

All clients

Personal Rooms

A personal room is a virtual conference room that is always available and can be used to meet with people. Cisco Jabber uses
                                          the personal room feature of Cisco Webex Meetings  to allow users to easily meet with their contacts using the Meet Now option
                                          in the client.

All clients

Problem Reporting

Problem reporting enables users to send a summary of issues that they encounter with the client.

All clients

Prompts for Presence Subscription Requests

You can enable or disable prompts for presence subscription requests from contacts within your organization.

All clients

Push Notification Services for Instant Messaging

The Push Notification service for IM forwards the new IM notification to Cisco Jabber, even if Cisco Jabber is inactive.

Cisco Jabber for iPhone and iPad, and Android in Jabber team messaging mode.

Push Notification Services for Video and Voice Calls

Receive notification about the incoming voice and video calls, even if Cisco Jabber is inactive.

Cisco Jabber for iPhone and iPad.

Restore Chats on Login

Allows users to specify if open 1:1 chat sessions are restored on next sign in.

All clients

Set Device PIN

You can configure if Jabber checks that the device is secured with a PIN.

Cisco Jabber for mobile clients

Sign into Cisco Jabber Using Face or Fingerprint Recognition

Cisco Jabber supports Touch ID, Face ID, or fingerprint authentication for users to securely sign in.

Cisco Jabber for mobile clients.

Silent Monitoring and Call Recording

Silent call monitoring allows a supervisor to hear both call participants, but neither of the call participants can hear the
                                          supervisor. Call recording enables a recording server to archive agent conversations.

All clients

Single Number Reach

You can answer incoming Cisco Jabber calls from any other phone or device such as your mobile or home phone using single number
                                          reach.

All clients

Telemetry

To improve your experience and product performance, Cisco Jabber may collect and send non-personally identifiable usage and
                                          performance data to Cisco. The aggregated data is used by Cisco to understand trends in how Jabber clients are being used
                                          and how they are performing.

All clients

Temporary Presence

You can configure when users can see availability status for contacts in their contact list.

All clients

URI Dialing

URI dialing allows users to make calls and resolve contacts with Uniform Resource Identifiers (URI).

All clients

Voicemail Avoidance

Voicemail avoidance is a feature that prevents calls from being answered by the mobile service provider voicemail.

All clients

Wireless Location Monitoring Service

Wireless location monitoring service allows you to determine the physical location from where your Cisco Jabber users connect
                                          to the corporate network.

All clients except Cisco Jabber Softphone for VDI

| Feature Name | Description | Supported Clients |
|---|---|---|
| ActiveControl | Hold conferences in Jabber using the Cisco Meetings Server (CMS) 2.3 or later. | All clients |
| Blocked Domain Support for Webex Messenger Users | Webex Messenger users can add a specific domain or a contact from a specific domain to the blocked list. Contacts from the
                                       specified domain cannot view your availability or send you instant messages. | Cisco Jabber for Mac |
| Bots | A chat bot is an automated service that appears and behaves like a user in Jabber. A Jabber user can add a chat bot to their
                                          Contacts list and start a chat conversation with the bot. | All clients |
| Bridge Escalations | Bridge escalations allow users to quickly escalate a group chat to a conference call. | All clients |
| Browser Click to Call | Users can start a call from a browser by right-clicking on any number, URI, or alphanumerical string. | Cisco Jabber for Windows Cisco Jabber Softphone for VDI |
| Calendar Integration and Contact Resolution | Lets users view their events from the Meetings tab. Also, let users search for their local contacts. | All clients |
| Call Park | You can use call park to place a call on hold and pick it up from another phone in a Cisco UnifiedCommunication Manager system. | Cisco Jabber for mobile clients |
| Call Pickup | Call pickup allows users to pick up incoming calls from a group. | Cisco Jabber for Windows Cisco Jabber for Mac Cisco Jabber Softphone for VDI |
| Chat History in Microsoft Outlook | Allow users to automatically save chat histories to a Cisco Jabber Chats folder in the user's Microsoft Outlook application. | Cisco Jabber for Windows Cisco Jabber for Mac Cisco Jabber Softphone for VDI |
| Chromebook | Allow users to download Cisco Jabber for Android into their Chrombook from Google Play Store. Cisco Jabber on Chromebook works
                                          as an Android tablet. Users can access all Cisco Jabber services on Chromebook when connecetd over MRA. | Cisco Jabber for Android. |
| Cisco Jabber Mobile App Promotion | Allow users to enable a notificaton to promote the use of the Cisco Jabber for Mobile App (Android and iOS). | Cisco Jabber for Windows Cisco Jabber Softphone for VDI |
| Collaboration Meetings Rooms | Cisco Collaboration Meeting Rooms (CMR) Cloud provides easy access for users to join or start Cisco Webex Meetings . | All clients |
| Custom Embedded Tabs | Custom embedded tabs display HTML content in the client interface. | All clients |
| Custom Emoticons | Add custom emoticons to Cisco Jabber for Windows by creating emoticon definitions in an XML file and saving it to the file
                                          system. | Cisco Jabber for Windows Cisco Jabber Softphone for VDI |
| Dial via Office | The DvO feature allows users to initiate Cisco Jabber outgoing calls with their work number using the mobile voice network
                                          for the device. | Cisco Jabber for mobile clients |
| DND Status Cascading | When a user manually sets the IM Presence status as Do Not Disturb from the Cisco Jabber client, then the status is cascaded
                                          down to all the phone devices that are owned by the user. | All clients |
| Enterprise Groups for Cisco Unified Communications Manager IM and Presence Service | Cisco Jabber users can search for groups in Microsoft Active Directory and add them to their contact lists. | All clients |
| Far End Camera Control | Allow users to adjust the far-end camera to give a better view during video calls. | All clients |
| File Transfers and Screen Captures | Allow users to transfer files and screen captures to other users, ad hoc group chat rooms, and persistent chat rooms. | All clients |
| Flexible DSCP Values | Flexible Differentiated Services Code Point (DSCP) allows you to specify different DSCP values to separate the audio and video
                                          streams on the network. | Cisco Jabber for Mac Cisco Jabber for mobile clients |
| Hunt Group | A Hunt Group is a group of lines that are organized hierarchically, so that if the first number in the hunt group list is
                                          busy, the system dials the second number. If the second number is busy, the system dials the next number, and so on. | All clients |
| IBM Notes Contact Search and Calendar Integration | Cisco Jabber for Windows supports IBM Notes calendar integration in the Meetings tab of the client. Cisco Jabber also lets
                                          users search for and add local contacts from IBM Notes. | Cisco Jabber for Windows Cisco Jabber Softphone for VDI |
| Integration with Microsoft Products | Cisco Jabber supports a range of Microsoft products that integrate with the application: Internet Explorer Microsoft Office Microsoft Office 365 Microsoft SharePoint | Cisco Jabber for Windows Cisco Jabber for Mac Cisco Jabber Softphone for VDI |
| Jabber to Jabber Call | Jabber to Jabber voice and video calling provides basic calling capabilities between two Cisco Jabber clients without using
                                          Cisco Unified Communications Manager. | All clients |
| Let Users Without Voicemail Ignore Calls | Choose a No Voicemail profile for users who don't have voicemail configured. | All clients |
| Location Sharing | Allow users to share their location with their contacts. | Cisco Jabber for Windows Cisco Jabber for Mac |
| Logout Inactivity Timer | The sign out inactivity timer allows you to automatically sign users out of the client after a specified amount of time of
                                          inactivity. | All clients |
| Mac Calender Integration for Meetings | Allow users to connect their calendars to their Cisco Jabber client. | Cisco Jabber for Mac |
| Microsoft Outlook Calendar Events | Display Microsoft Outlook calendar events in the Meetings tab of Cisco Jabber. | Cisco Jabber for Windows Cisco Jabber Softphone for VDI |
| Microsoft Outlook Presence Integration | Display presence status in Microsoft Outlook | Cisco Jabber for Windows Cisco Jabber for Mac Cisco Jabber Softphone for VDI |
| Move to Mobile | Users can transfer an active VoIP call from Cisco Jabber to their mobile phone number on the mobile network. | Cisco Jabber for mobile clients |
| Multiline | You can configure multiple phone lines for your users to perform daily Cisco Jabber tasks. You can add up to eight phone lines
                                          per user. | Cisco Jabber for Windows Cisco Jabber for Mac |
| Multiple Device Messaging for Cloud Deployments | Users who are signed into multiple devices can see all sent and received IMs on each device regardless of which device is
                                          active. | All clients |
| My Jabber Chats and My Jabber Files Directory Location | Specify a directory location for saved instant messages and file transfers, or let users specify their own location. | Cisco Jabber for Windows Cisco Jabber Softphone for VDI |
| Persistent Chat Rooms | Persistent chat is a permanent chat room that offers ongoing access to a discussion thread. It is available even if no one
                                          is currently in the chat room and remains available until explicitly removed from the system. | All clients |
| Personal Rooms | A personal room is a virtual conference room that is always available and can be used to meet with people. Cisco Jabber uses
                                          the personal room feature of Cisco Webex Meetings  to allow users to easily meet with their contacts using the Meet Now option
                                          in the client. | All clients |
| Problem Reporting | Problem reporting enables users to send a summary of issues that they encounter with the client. | All clients |
| Prompts for Presence Subscription Requests | You can enable or disable prompts for presence subscription requests from contacts within your organization. | All clients |
| Push Notification Services for Instant Messaging | The Push Notification service for IM forwards the new IM notification to Cisco Jabber, even if Cisco Jabber is inactive. | Cisco Jabber for iPhone and iPad, and Android in Jabber team messaging mode. |
| Push Notification Services for Video and Voice Calls | Receive notification about the incoming voice and video calls, even if Cisco Jabber is inactive. | Cisco Jabber for iPhone and iPad. |
| Restore Chats on Login | Allows users to specify if open 1:1 chat sessions are restored on next sign in. | All clients |
| Set Device PIN | You can configure if Jabber checks that the device is secured with a PIN. | Cisco Jabber for mobile clients |
| Sign into Cisco Jabber Using Face or Fingerprint Recognition | Cisco Jabber supports Touch ID, Face ID, or fingerprint authentication for users to securely sign in. | Cisco Jabber for mobile clients. |
| Silent Monitoring and Call Recording | Silent call monitoring allows a supervisor to hear both call participants, but neither of the call participants can hear the
                                          supervisor. Call recording enables a recording server to archive agent conversations. | All clients |
| Single Number Reach | You can answer incoming Cisco Jabber calls from any other phone or device such as your mobile or home phone using single number
                                          reach. | All clients |
| Telemetry | To improve your experience and product performance, Cisco Jabber may collect and send non-personally identifiable usage and
                                          performance data to Cisco. The aggregated data is used by Cisco to understand trends in how Jabber clients are being used
                                          and how they are performing. | All clients |
| Temporary Presence | You can configure when users can see availability status for contacts in their contact list. | All clients |
| URI Dialing | URI dialing allows users to make calls and resolve contacts with Uniform Resource Identifiers (URI). | All clients |
| Voicemail Avoidance | Voicemail avoidance is a feature that prevents calls from being answered by the mobile service provider voicemail. | All clients |
| Wireless Location Monitoring Service | Wireless location monitoring service allows you to determine the physical location from where your Cisco Jabber users connect
                                          to the corporate network. | All clients except Cisco Jabber Softphone for VDI |