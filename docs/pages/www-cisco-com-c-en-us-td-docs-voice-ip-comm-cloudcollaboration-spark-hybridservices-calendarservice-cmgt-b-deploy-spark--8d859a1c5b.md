---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-spark-hybridservices-calendarservice-cmgt-b-deploy-spark--8d859a1c5b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/spark/hybridservices/calendarservice/cmgt_b_deploy-spark-hybrid-calendar-service/cmgt_b_deploy-spark-hybrid-calendar-service_preface_01.html
retrieved_at: 2026-08-20T23:53:49.546316+00:00
---

Deployment guide for Hybrid Calendar

# Deployment guide for Hybrid Calendar

Updated: October 17, 2023

Chapter: Overview of Hybrid Calendar

## Chapter: Overview of Hybrid Calendar

# Overview of Hybrid Calendar

## Hybrid Calendar features

With Hybrid Calendar , you can connect your on-premises Microsoft Exchange, Office 365 or Google's G Suite Calendar (Google Calendar) environment
                           to Webex . This integration makes it easier to schedule and join meetings, especially when mobile; no plugins are required.

Hybrid Calendar has no Cisco call control dependency—you can use this service to extend features to Webex users, even if you use a third-party UC solution.

### Simple meeting scheduling

To simplify scheduling, your Hybrid Calendar users have a couple of easy ways to add meeting details to a calendar invitation.

1. Type a keyword in the location field.

As an administrator, you can choose what the scheduling keywords @webex and @meet do:

Create a space in Webex App and add join details for it (default for @meet )

Use the scheduler's Webex Personal Room join details (default for @webex )

Use your on-premises resource management and conference hosting environment with TelePresence Management Suite (available
                                    only as an option for )

The TMS integration currently works with the cloud-based Hybrid Calendar  for Office 365 or the cloud-based Hybrid Calendar
                                    for Google Calendar. It is not available for Microsoft Exchange or for hybrid Exchange and Office 365 deployments.

You can choose these keyword actions on the Hybrid Calendar settings page in Control Hub ( https://admin.webex.com ).

Power users can add ":space" or ":myroom" to either keyword to override the administrator default setting. For example, if
                              you configured both @meet and @webex to create a space in Webex App , users can type @meet:myroom or @webex:myroom to schedule the meeting in their Personal Room instead. Note that ":space"
                              is the actual modifier that users enter, and the Hybrid Calendar names the space using the subject line of the invitation (except in 1:1 meetings between two people, where the Hybrid Calendar reuses the existing 1:1 space).

2. Include a video address in the meeting body.

In addition to the scheduling keywords, the Hybrid Calendar can parse a SIP URI or other video address from the body of a calendar invitation, even if it's not a Webex standard meeting, Webex Personal Room meeting, or Webex team meeting address. When the address matches a supported format, the meeting appears in invitees' meetings lists and meeting
                              notifications in the Webex App app. The meeting also appears in the list on any scheduled room or desk devices that are enabled for the Hybrid Calendar , and the devices show the green Join button (One Button To Push) just before the meeting starts.

Description

Examples

Standard SIP address

sip:jdoe@company.com

sips:jdoe@company.com

Special-case URI—all numbers without sip: prefix

12345@company.com

### Meetings list and join button

The meetings list in Webex App lets users see upcoming meetings for the next 4 weeks. Users see a Join button in the meetings list and a scheduled meeting notification 5 minutes before the meeting starts.

Users can add Webex room and desk devices and Webex Boards to a meeting to make conferencing resources available. If the device is enabled for
                              the Hybrid Calendar , the green Join button appears on the device. (The Join button is also known as One Button to Push, and is also available to devices that are registered to Unified Communications
                              Manager, and managed by TelePresence Management Suite.) Hybrid Calendar-enabled room and desk devices can also show meetings
                              to which they've been invited in the meetings list.

### Skype for business addresses

When adding Webex Meetings join details to an invitation, the Hybrid Calendar also includes a Skype for Business-specific video address.

### Out-of-Office status

Your  Hybrid Calendar users, on Microsoft Exchange, Office 365, or Google Calendar, can share their out-of-office status through Webex App . When a user sets an automatic reply, other Webex App users in their organization can see that they are out of the office:

In @mentions directed at the out-of-office user.

In the People space for that user.

In search results for that user's name.

In the expanded people roster for a space.

Changes to the status can take up to 20 minutes to update in Webex App .

### Organization-wide default language

With a global setting in Control Hub , you can determine the language that the Hybrid Calendar uses for all meeting join details in your organization. This setting is useful if you have a legal requirement to present
                              information in one particular language, regardless of the language that meeting schedulers set for their own calendar, mailbox,
                              or invitation.

If you do not change the default to a specific language for the organization, the Hybrid Calendar determines which language to use differently, depending on the calendar integration type:

Calendar integration type

Default if no specific language chosen

Office 365 (using the Microsoft Graph API through the cloud-based service)

"language":{"locale"} setting from the scheduler's mailbox settings

Google G Suite Calendar

locale setting from scheduler's calendar settings

Microsoft Exchange or Office 365 (using EWS through the Expressway-based Calendar Connector)

item.Culture property from the meeting invitation

## Expressway-based Calendar Connector for Microsoft Exchange and Office 365: Architecture

For a detailed overview of Hybrid Services , including architectural and design information for the Expressway-based Calendar Connector, we recommend that you read the Preferred Architecture for Cisco Webex Hybrid Services, Design Overview .

For more information on how the Calendar Connector integrates with Microsoft Exchange and Office 365, see the Cisco Webex Hybrid Calendar Service with Microsoft Exchange Integration Reference .

This diagram shows the components of Hybrid Calendar architecture and where the Expressway-based connectors integrate the on-premises components with the cloud.

The cloud activates OBTP on these devices when they are invited to meetings scheduled with a keyword or supported video address.

This diagram shows Hybrid Calendar and Cisco TMS providing OBTP to Unified Communications Manager -registered video endpoints when they are invited to meetings scheduled with a keyword or supported video address.

## Office 365 and hybrid Exchange environments

Previously, to serve Office 365 users, you had to install the Calendar Connector on an on-premises Expressway. This on-premises
                           deployment was required even if you didn't have a hybrid Exchange environment (on-premises Microsoft Exchange and an Office
                           365 tenant organization).

You can now choose to enable the cloud-based Hybrid Calendar for Office 365. With this service, hybrid Exchange environments
                           have extra considerations:

You can run the Expressway-based Calendar Connector and the cloud-based Office 365 service at the same time.

Once you enable the cloud-based service, all Office 365 users who are not in any resource group automatically migrate to it.

To test the migration on a subset of users, make sure that the rest of the Office 365 users are in a resource group. Then
                                 enable the cloud-based Office 365 service.

The Calendar Connector on the Expressway-C serves both Exchange users and Office 365 users, in Resource Group A and Resource
                           Group B. The cloud-based service serves any Office 365 users who are not in a resource group.

## Cloud-based Hybrid Calendar with Office 365: Scheduling flow

A user creates a meeting in the Office 365 calendar, putting a scheduling keyword or video address in the Location field.

Exchange Online sends a notification to the Hybrid Calendar .

The Hybrid Calendar requests and receives the encryption key, and then uses it to encrypt the meeting information.

The Hybrid Calendar validates meeting creation and recipients, and then creates a Webex team space, if applicable.

The Hybrid Calendar calls the API service and, if applicable, maps the meeting to the space.

The Hybrid Calendar retrieves the meeting join information, including the Webex Personal Room if applicable.

The Hybrid Calendar updates the meeting invite with the meeting join information and, if applicable, the space ID.

The invitees and the organizer get the updated meeting invitation.

For more information on how the cloud-based Hybrid Calendar integrates with Office 365, see the Cisco Webex Hybrid Calendar Service with Office 365 Integration Reference .

## Hybrid Calendar with Google Calendar: Scheduling flow

A user creates a meeting in Google Calendar, putting a scheduling keyword or video address in the location field.

Google sends a notification to the Hybrid Calendar .

The Hybrid Calendar requests and receives the encryption key, and then uses it to encrypt the meeting information.

The Hybrid Calendar validates meeting creation and recipients, and then creates a Webex team space, if applicable.

The Hybrid Calendar calls the API service and maps the meeting to the space.

The Hybrid Calendar retrieves the meeting join information, including the Personal Room if applicable.

The Hybrid Calendar updates the meeting invite with the meeting join information and, if applicable, the space ID.

The updated meeting information appears in Google Calendar.

For more information on how the Hybrid Calendar Service integrates with Google's G Suite Calendar, see the Hybrid Calendar with Google Calendar integration reference .

| Description | Examples |
|---|---|
| Standard SIP address | sip:jdoe@company.com sips:jdoe@company.com |
| Special-case URI—all numbers without sip: prefix | 12345@company.com |

| Calendar integration type | Default if no specific language chosen |
|---|---|
| Office 365 (using the Microsoft Graph API through the cloud-based service) | "language":{"locale"} setting from the scheduler's mailbox settings |
| Google G Suite Calendar | locale setting from scheduler's calendar settings |
| Microsoft Exchange or Office 365 (using EWS through the Expressway-based Calendar Connector) | item.Culture property from the meeting invitation |