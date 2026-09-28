---
doc_id: help-webex-com-en-us-article-uhgvzi-415668627a
source_url: https://help.webex.com/en-us/article/uhgvzi
retrieved_at: 2026-09-07T10:36:58.696085+00:00
---

## Microsoft 365 (Cloud-Based Service)

### Deployment

Microsoft 365 users who are assigned to the cloud-based service (indicated in Webex
                                                Control Hub as on cluster "Cisco Webex Cloud") may show a persistent error message in Control Hub, "Could not find cluster with Calendar Connector. Select another Resource Group, or configure a new cluster with Calendar Connector." This error can be ignored.

The cloud-based service does not activate a user whose email address contains an apostrophe. If you are migrating users from the Expressway-based Calendar Connector, the Hybrid Calendar Service does not move these users to the cloud-based service. They remain on the Calendar Connector.

### General Scheduling Issues (All Keywords)

In order for OBTP to work consistently on invited devices, you must ensure that the mail system does not have a policy to automatically delete meeting comments. The following PowerShell command ensures that comments are retained so that the Hybrid Calendar Service can use them to process meetings:

```
Set-CalendarProcessing -identity "room" -DeleteComments $false
```

Hybrid Calendar does not support shared calendars. The service can process meetings that a delegate schedules on behalf of others, as long as they schedule the meeting in the user's actual calendar, not a shared or group calendar.

A meeting that is scheduled more than 5 months in the future may not get immediately processed by the cloud-based Hybrid Calendar Service for Microsoft 365. The service processes meetings that are 5-6 months in the future on a daily basis using a sliding window, so once the meeting's scheduled date falls within the window, it will get processed and show the meeting join details.

If you add a scheduling keyword or supported video address to a single instance of a recurring meeting series, the meeting join details are not updated. As a workaround, add the keyword or video address to the entire meeting series.

Hybrid Calendar does not automatically add meeting join information to a meeting that's scheduled in the past.

### Scheduling a Webex Personal Room Meeting (Keywords Including @webex, @meet:myroom)

Hybrid Calendar does not add Webex details if the meeting invitation already contains Webex join links (for example, added with Productivity Tools or manually by the meeting organizer). The meeting organizer can manually delete any previously added join links so that Hybrid Calendar can add the new join links.

Hybrid Calendar does not process meetings with more than 1500 meeting invitees.

### Scheduling in a Webex App Space (Keywords Including @webex:space, @meet, @spark)

Space keyword scheduling currently supports a maximum of 1500 meeting participants. A
            meeting organizer who invites more than 120 participants will receive an email message
            indicating that they have exceeded the maximum. When the total invitees is less than
            1500, the organizer can see the meeting info in team's client calendar view. As well,
            when the total number of invitees exceeds 1500, the meeting will not show in their
            team's calendar view.

Space keyword scheduling does not currently handle distribution lists. Individual members of the distribution list still receive the meeting invitation with details on joining the space, but are not automatically added to the space. As a workaround, the meeting organizer can expand the mailer on the TO line before sending the invite. That way, each user is individually added to the space.

Attachments that users add to meeting invites with space keywords are not added to the corresponding space.

The Hybrid Calendar Service no longer sends a separate email message to meeting invitees who are not Webex App users, inviting them to sign up.

Webex spaces have an assigned meeting number that's used for the video device Join button each time you schedule a meeting from a space. Webex may recycle the meeting number if it hasn't been used in 180 days. Meetings scheduled after the recycling event get a new number, but the calendar service doesn't update existing meetings.

For example, say you schedule a space meeting (with @meet) for your team more than 180 days in advance, and the space meeting number is 444 444 4444. Your team doesn't meet in the space in the interim, and the meeting number changes to 555 555 5555. When the meeting comes, app participants will join the newer meeting number (555 555 5555). Participants who try to join from video devices using the link in the meeting invitation will connect to the old meeting number, 444 444 4444.

### One Button to Push (OBTP)

For issues involving the Join button and meetings list in Webex App, see Webex App | Known Issues in Meetings .

### Cisco TMS Integration with Microsoft 365

If the conference bridge that is scheduled to host an upcoming meeting becomes unavailable, Cisco TMS updates the meeting join details to use a different bridge. However, the meeting join details do not get updated in Microsoft 365 unless the organizer makes a change to the meeting invitation. This can cause problems when invitees try to join the meeting from the invitation.

If a meeting scheduler's time zone in Microsoft 365 does not match the scheduler's time zone in Cisco TMS, the system may have a problem scheduling recurring meetings. This can cause a mismatch between the instance dates in Microsoft 365 and in Cisco TMS. As a workaround, make sure users' time zones in Microsoft 365 match their time zones in Cisco TMS.

For a recurring meeting series, changes to the start and end dates or number of occurrences in Microsoft 365 are not updated in Cisco TMS. (Changes to the start and end times of the entire series work as expected.) As a workaround, delete the series and create a new one.

When a recurring meeting series scheduled with @meet is edited multiple times, the series updates correctly in Microsoft 365 but may not update correctly in Cisco TMS. The behavior is not consistent. For example, adding attendees to a single instance of the series and then changing the subject of the entire series may result in the subject changing only for the modified instance—or for all instances other than the modified instance.

If an endpoint is already booked in Microsoft 365 for a given time slot for a non-@meet meeting, and an organizer schedules a recurring meeting with @meet which overlaps the booked time slot, the organizer gets a message saying that the endpoint declined the meeting, but Cisco TMS creates the recurring meeting anyway.

For such meetings, the Calendar Connector sends an extra meeting request and logs two different informational messages that each include one of the following strings:

status:MEETING_NOT_FOUND_ON_TMS

status:UN_EXPECTED_EXCEPTION

The Calendar Connector should raise an alarm if the organization to which the Expressway host is registered has the @meet keyword action set to Cisco TelePresence Management Suite but the Calendar Connector has not been linked to Cisco TMS on the Expressway under Applications > Hybrid Services > Calendar Service > Cisco Conferencing Services Configuration page. This alarm has not been implemented.

If you remove the Cisco TMS configuration from the Expressway connector host, users can continue to schedule @meet meetings on Cisco TMS until the Expressway connector host is restarted. The workaround is to restart the Expressway connector host after removing the Cisco TMS configuration.

## Google Calendar (Cloud-Based Service)

### General Scheduling Issues (All Keywords)

Hybrid Calendar does not support shared calendars. The service can process meetings that a delegate schedules on behalf of others, as long as they schedule the meeting in the user's actual calendar, not a shared or group calendar.

If you add a scheduling keyword or supported video address to a single instance of a recurring meeting series, the meeting join details are not updated. As a workaround, add the keyword or video address to the entire meeting series.

Hybrid Calendar does not automatically add meeting join information to a meeting that's scheduled in the past.

### Scheduling a Webex Personal Room Meeting (Keywords Including @webex, @meet:myroom)

Hybrid Calendar does not add Webex details if the meeting invitation already contains Webex join links (for example, added with Productivity Tools or manually by the meeting organizer). The meeting organizer can manually delete any previously added join links so that Hybrid Calendar can add the new join links.

Hybrid Calendar does not process meetings with more than 1500 meeting invitees.

### Scheduling in a Webex App Space (Keywords Including @webex:space, @meet, @spark)

Space keyword scheduling currently supports a maximum of 1500 meeting participants. A
            meeting organizer who invites more than 120 participants will receive an email message
            indicating that they have exceeded the maximum. When the total invitees is less than
            1500, the organizer can see the meeting info in team's client calendar view. As well,
            when the total number of invitees exceeds 1500, the meeting will not show in their
            team's calendar view.

Space keyword scheduling does not currently handle distribution lists. Individual members of the distribution list still receive the meeting invitation with details on joining the space, but are not automatically added to the space. As a workaround, the meeting organizer can expand the mailer on the TO line before sending the invite. That way, each user is individually added to the space.

Attachments that users add to meeting invites with space keywords are not added to the corresponding space.

The Hybrid Calendar Service no longer sends a separate email message to meeting invitees who are not Webex App users, inviting them to sign up.

Webex spaces have an assigned meeting number that's used for the video device Join button each time you schedule a meeting from a space. Webex may recycle the meeting number if it hasn't been used in 180 days. Meetings scheduled after the recycling event get a new number, but the calendar service doesn't update existing meetings.

For example, say you schedule a space meeting (with @meet) for your team more than 180 days in advance, and the space meeting number is 444 444 4444. Your team doesn't meet in the space in the interim, and the meeting number changes to 555 555 5555. When the meeting comes, app participants will join the newer meeting number (555 555 5555). Participants who try to join from video devices using the link in the meeting invitation will connect to the old meeting number, 444 444 4444.

### One Button to Push (OBTP)

For issues involving the Join button and meetings list in Webex App, see Webex App | Known Issues in Meetings .

### Cisco TMS Integration with Google Calendar

If the conference bridge that is scheduled to host an upcoming meeting becomes unavailable, Cisco TMS updates the meeting join details to use a different bridge. However, the meeting join details do not get updated in Google Calendar unless the organizer makes a change to the meeting invitation. This can cause problems when invitees try to join the meeting from the invitation.

If a meeting scheduler's time zone in Google Calendar does not match the scheduler's time zone in Cisco TMS, the system may have a problem scheduling recurring meetings. This can cause a mismatch between the instance dates in Google Calendar and in Cisco TMS. As a workaround, make sure users' time zones in Google Calendar match their time zones in Cisco TMS.

When a recurring meeting series scheduled with @meet is edited multiple times, the series updates correctly in Google Calendar but may not update correctly in Cisco TMS. The behavior is not consistent. For example, changing the subject of a single instance of the series and then changing the subject of the entire series may result in the subject changing only for the modified instance—or for all instances other than the modified instance.

If an endpoint is already booked in Google Calendar for a given time slot for a non-@meet meeting, and an organizer schedules a meeting with @meet which overlaps the booked time slot, the organizer gets a message saying that the endpoint declined the meeting, but Cisco TMS creates the overlapping meeting anyway.

For such meetings, the Calendar Connector sends an extra meeting request and logs two different informational messages that each include one of the following strings:

status:MEETING_NOT_FOUND_ON_TMS

status:UN_EXPECTED_EXCEPTION

The Calendar Connector should raise an alarm if the organization to which the Expressway host is registered has the @meet keyword action set to Cisco TelePresence Management Suite but the Calendar Connector has not been linked to Cisco TMS on the Expressway under Applications > Hybrid Services > Calendar Service > Cisco Conferencing Services Configuration page. This alarm has not been implemented.

If you remove the Cisco TMS configuration from the Expressway connector host, users can continue to schedule @meet meetings on Cisco TMS until the Expressway connector host is restarted. The workaround is to restart the Expressway connector host after removing the Cisco TMS configuration.

## Exchange and Microsoft 365 (Expressway-Based Calendar Connector)

### Calendar Connector Deployment and Configuration

Calendar Connector supports single cluster with a maximum of two Expressway instances per organization.

Proxy connections must use basic authentication or no username and password. No other authentication schemes are supported.

The Calendar Connector currently does not support Exchange organizations that require the service (impersonation) account to use multi-factor authentication (MFA).

For some customers, the Calendar Connector raises a critical alarm described as "Redirected Microsoft Exchange Autodiscovery URL not trusted." The issue may result in some delays processing calendar events for users. In some cases, the Calendar Connector will be unable to provide any service to some portion of the users.

If you see this alarm, use the Autodiscover Redirect URL trust list to configure how the Calendar Connector can locate user mailboxes.

For some customers, the Calendar Connector raises an "NTLM authentication error: Credentials cannot be used for NTLM authentication" warning in the hybrid_services_log files. This can occur if a connector proxy is configured on the Applications > Hybrid Services > Connector Proxy page in Expressway and that proxy requires authentication. No workaround is required as long as the connector proxy supports Basic authentication scheme, or does not require authentication.

If you deregister the Calendar Connector, or deactivate it if it's the only hybrid service on the Expressway, the Expressway can get into an error state where hybrid service connectors will not register, configuration changes do not propagate, or other problems occur. The workaround is to reboot the Expressway and reregister the connector.

You cannot search in Control Hub to return the set of users who have the Hybrid Calendar service turned on or off.

When adding a Webex site to the Calendar Connector configuration, you must enter the Fully Qualified Site Name value entirely in lowercase. Uppercase characters cause the Calendar Connector to raise a "service unreachable or access denied" alarm.

The Cisco TMS integration does not currently support Microsoft Exchange or Hybrid Exchange deployments (Microsoft Exchange and Microsoft 365 together). The integration currently works only with the cloud-based Hybrid Calendar Service for Microsoft 365 or the cloud-based Hybrid Calendar Service for Google Calendar.

The integration uses the Calendar Connector to link the Hybrid Calendar Service with Cisco TMS. Once you configure the TMS scheduling option on an Expressway-C, you cannot link the same Calendar Connector to Microsoft Exchange, and vice versa.

### General Scheduling Issues (All Keywords)

Hybrid Calendar does not support shared calendars. The service can process meetings that a delegate schedules on behalf of others, as long as they schedule the meeting in the user's actual calendar, not a shared or group calendar.

If you add a scheduling keyword or supported video address to a single instance of a recurring meeting series, the meeting join details are not updated. As a workaround, add the keyword or video address to the entire meeting series.

Users may see multiple meeting invitations in their Outlook inbox when receiving meetings scheduled with a keyword or supported video address. As a workaround, check the following check boxes in the Microsoft Outlook Web app under Settings > Calendar > Automatic Processing :

Delete meeting requests and responses that have been updated

Automatically process requests and responses from external senders

These settings are available only in the web app, but the above changes apply to all Outlook clients.

Hybrid Calendar does not add meeting join links to the meeting invitation for any invitees who have single quotes around their email addresses. As a workaround, do not include single quotes around email addresses in the invitation.

In order for OBTP to work consistently on invited devices, you must ensure that the mail system does not have a policy to automatically delete meeting comments. The following PowerShell command ensures that comments are retained so that the Hybrid Calendar Service can use them to process meetings:

```
Set-CalendarProcessing -identity "room" -DeleteComments $false
```

In some versions of Microsoft Outlook 2016, after changing a single instance of a recurrent scheduled meeting where a scheduling keyword is in the location field, the body text and join links might disappear.

If possible, upgrade to the latest version of Outlook.

If you cannot upgrade, delete and reschedule the affected instance.

The other instances of the meeting series should be unaffected.

Meeting organizers using Microsoft Outlook 2011 for Mac may not see the join links in their meeting invites, although the invitees receive the links. This is an issue with Outlook 2011 for Mac and the solution is to upgrade to a more recent version of Outlook for Mac.

Hybrid Calendar does not automatically add meeting join information to a meeting that's scheduled in the past.

When a delegate cancels a meeting on the organizer's behalf, the Hybrid Calendar Service can take up to 24 hours to remove the meeting from the meetings list in Webex App.

### Scheduling a Webex Personal Room Meeting (Keywords Including @webex, @meet:myroom)

Hybrid Calendar does not add Webex details if the meeting invitation already contains Webex join links (for example, added with Productivity Tools or manually by the meeting organizer). The meeting organizer can manually delete any previously added join links so that Hybrid Calendar can add the new join links.

Hybrid Calendar does not process meetings with more than 1500 meeting invitees.

### Scheduling in a Webex App Space (Keywords Including @webex:space, @meet, @spark)

Space keyword scheduling currently supports a maximum of 1500 meeting participants. A
            meeting organizer who invites more than 120 participants will receive an email message
            indicating that they have exceeded the maximum. When the total invitees is less than
            1500, the organizer can see the meeting info in team's client calendar view. As well,
            when the total number of invitees exceeds 1500, the meeting will not show in their
            team's calendar view.

Space keyword scheduling does not currently handle distribution lists. Individual members of the distribution list still receive the meeting invitation with details on joining the space, but are not automatically added to the space. As a workaround, the meeting organizer can expand the mailer on the TO line before sending the invite. That way, each user is individually added to the space.

The Hybrid Calendar Service no longer sends a separate email message to meeting invitees who are not Webex App users, inviting them to sign up.

Attachments that users add to meeting invites with space keywords are not added to the corresponding space.

Webex spaces have an assigned meeting number that's used for the video device Join button each time you schedule a meeting from a space. Webex may recycle the meeting number if it hasn't been used in 180 days. Meetings scheduled after the recycling event get a new number, but the calendar service doesn't update existing meetings.

For example, say you schedule a space meeting (with @meet) for your team more than 180 days in advance, and the space meeting number is 444 444 4444. Your team doesn't meet in the space in the interim, and the meeting number changes to 555 555 5555. When the meeting comes, app participants will join the newer meeting number (555 555 5555). Participants who try to join from video devices using the link in the meeting invitation will connect to the old meeting number, 444 444 4444.

### One Button to Push (OBTP)

For issues involving the Join button and meetings list in Webex App, see Webex App | Known Issues in Meetings .

### Microsoft deprecates Basic Authentication for Exchange Online

Microsoft intends to deprecate Basic Authentication for Exchange Online on October 1, 2022. For more information, see https://techcommunity.microsoft.com/t5/exchange-team-blog/basic-authentication-deprecation-in-exchange-online-may-2022/ba-p/3301866 .

To maintain alignment with this change, the Hybrid Calendar
        Expressway connector will no longer support environments that are using Exchange Online mailboxes as of October 1, 2022. Most Exchange Online customers have migrated to our cloud-based Hybrid Calendar for Microsoft 365, and we require any customers using our Expressway connector to migrate to our cloud-based connector.

The Hybrid Calendar cloud-based connector utilizes Modern Authentication, which is the Microsoft-recommended solution for applications that currently use Basic Authentication. For additional information on Hybrid Calendar for Microsoft 365, see https://techcommunity.microsoft.com/t5/exchange-team-blog/basic-authentication-deprecation-in-exchange-online-may-2022/ba-p/3301866 .

## General scheduling issues

### One Button to Push (OBTP)

Hybrid Calendar has not been tested with, and does not support, third-party services that rewrite meeting invitations or replace the original meeting join links. For example, some revenue-intelligence tools, including Gong ® and Clari ™ /Wingman, may replace meeting links with links to an external consent page. When invitation content is rewritten, Hybrid Calendar may not recognize the meeting provider, and meeting list or One Button to Push behavior may be missing or inconsistent. These examples are not exhaustive.