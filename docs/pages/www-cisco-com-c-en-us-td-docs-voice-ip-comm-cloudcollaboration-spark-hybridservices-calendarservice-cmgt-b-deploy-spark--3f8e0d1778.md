---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-spark-hybridservices-calendarservice-cmgt-b-deploy-spark--3f8e0d1778
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/spark/hybridservices/calendarservice/cmgt_b_deploy-spark-hybrid-calendar-service/cmgt_b_deploy-spark-hybrid-calendar-service_appendix_01010.html
retrieved_at: 2026-08-20T22:17:08.354376+00:00
---

Deployment guide for Hybrid Calendar

# Deployment guide for Hybrid Calendar

Updated: July 21, 2017

Chapter: Known Issues with Hybrid Calendar Service

## Chapter: Known Issues with Hybrid Calendar Service

# Known Issues with Hybrid Calendar Service

## Office 365 (Cloud-Based Service)

### Deployment

Office 365 users who are assigned to the cloud-based service (indicated in Cisco Webex Control Hub as on cluster "Cisco Webex
                                    Cloud") may show a persistent error message in Control Hub, "Could not find cluster with Calendar Connector. Select another
                                    Resource Group, or configure a new cluster with Calendar Connector." This error can be ignored.

The cloud-based service does not activate a user whose email address contains an apostrophe. If you are migrating users from
                                    the Expressway-based Calendar Connector, the Hybrid Calendar Service does not move these users to the cloud-based service.
                                    They remain on the Calendar Connector.

### General Scheduling Issues (All Keywords)

In order for OBTP to work consistently on invited devices, you must ensure that the mail system does not have a policy to
                                    automatically delete meeting comments. The following PowerShell command ensures that comments are retained so that the Hybrid
                                    Calendar Service can use them to process meetings:

```
Set-CalendarProcessing -identity "room" -DeleteComments $false
```

Hybrid Calendar Service does not support shared calendars. The service can process meetings that a delegate schedules on behalf of others, as long
                                    as they schedule the meeting in the user's actual calendar, not a shared or group calendar.

A meeting that is scheduled more than 5 months in the future may not get immediately processed by the cloud-based Hybrid Calendar
                                    Service for Microsoft Office 365. The service processes meetings that are 5-6 months in the future on a daily basis using
                                    a sliding window, so once the meeting's scheduled date falls within the window, it will get processed and show the meeting
                                    join details.

If you add a scheduling keyword or supported video address to a single instance of a recurring meeting series, the meeting
                                    join details are not updated. As a workaround, add the keyword or video address to the entire meeting series.

Hybrid Calendar Service does not automatically add meeting join information to a meeting that's scheduled in the past.

### Scheduling a Webex Personal Room Meeting (Keywords Including @webex, @meet:myroom)

Hybrid Calendar Service does not add Webex details if the meeting invitation already contains Webex join links (for example, added with Productivity Tools or manually by the meeting organizer). The meeting organizer can manually
                                    delete any previously added join links so that Hybrid Calendar Service can add the new join links.

Hybrid Calendar Service does not process meetings with more than 300 meeting invitees.

You cannot customize the meeting details template except to modify the line of text that is included if you check Use a Pilot Number in Webex Site Administration. For instructions, see Can I Customize the Email Template Used by the Cisco Webex Hybrid Calendar Services with @Webex?

### Scheduling in a Cisco Webex Space (Keywords Including @webex:space, @meet, @spark)

Space keyword scheduling currently supports a maximum of 60 meeting participants. A meeting organizer who invites more than
                                    60 participants will receive an email message indicating that they have exceeded the maximum.

Space keyword scheduling does not currently handle distribution lists. Individual members of the distribution list still receive
                                    the meeting invitation with details on joining the space, but are not automatically added to the space. As a workaround, the
                                    meeting organizer can expand the mailer on the TO line before sending the invite. That way, each user is individually added
                                    to the space.

Attachments that users add to meeting invites with space keywords are not added to the corresponding space.

The Hybrid Calendar Service no longer sends a separate email message to meeting invitees who are not Cisco Webex users, inviting them to sign up.

You cannot customize the meeting details template that is used for meetings scheduled in a space.

### One Button to Push (OBTP)

For issues involving the Join button and meetings list in the Webex app, see the Known Issues for Cisco Webex Meetings article.

### Cisco TMS Integration with Office 365

If the conference bridge that is scheduled to host an upcoming meeting becomes unavailable, Cisco TMS updates the meeting
                                    join details to use a different bridge. However, the meeting join details do not get updated in Office 365 unless the organizer
                                    makes a change to the meeting invitation. This can cause problems when invitees try to join the meeting from the invitation.

If a meeting scheduler's time zone in Office 365 does not match the scheduler's time zone in Cisco TMS, the system may have
                                    a problem scheduling recurring meetings. This can cause a mismatch between the instance dates in Office 365 and in Cisco TMS.
                                    As a workaround, make sure users' time zones in Office 365 match their time zones in Cisco TMS.

For a recurring meeting series, changes to the start and end dates or number of occurrences in Office 365 are not updated
                                    in Cisco TMS. (Changes to the start and end times of the entire series work as expected.) As a workaround, delete the series
                                    and create a new one.

When a recurring meeting series scheduled with @meet is edited multiple times, the series updates correctly in Office 365
                                    but may not update correctly in Cisco TMS. The behavior is not consistent. For example, adding attendees to a single instance
                                    of the series and then changing the subject of the entire series may result in the subject changing only for the modified
                                    instance—or for all instances other than the modified instance.

If an endpoint is already booked in Office 365 for a given time slot for a non-@meet meeting, and an organizer schedules a
                                    recurring meeting with @meet which overlaps the booked time slot, the organizer gets a message saying that the endpoint declined
                                    the meeting, but Cisco TMS creates the recurring meeting anyway.

For such meetings, the Calendar Connector sends an extra meeting request and logs two different informational messages that
                                    each include one of the following strings:

status:MEETING_NOT_FOUND_ON_TMS

status:UN_EXPECTED_EXCEPTION

The Calendar Connector should raise an alarm if the organization to which the Expressway host is registered has the @meet
                                    keyword action set to Cisco TelePresence Management Suite but the Calendar Connector has not been linked to Cisco TMS on the Expressway Applications > Hybrid Services > Calendar Service > Cisco Conferencing Services Configuration page. This alarm has not been implemented.

If you remove the Cisco TMS configuration from the Expressway connector host, users can continue to schedule @meet meetings
                                    on Cisco TMS until the Expressway connector host is restarted. The workaround is to restart the Expressway connector host
                                    after removing the Cisco TMS configuration.

## Google Calendar (Cloud-Based Service)

### General Scheduling Issues (All Keywords)

Hybrid Calendar Service does not support shared calendars. The service can process meetings that a delegate schedules on behalf of others, as long
                                    as they schedule the meeting in the user's actual calendar, not a shared or group calendar.

If you add a scheduling keyword or supported video address to a single instance of a recurring meeting series, the meeting
                                    join details are not updated. As a workaround, add the keyword or video address to the entire meeting series.

Hybrid Calendar Service does not automatically add meeting join information to a meeting that's scheduled in the past.

### Scheduling a Webex Personal Room Meeting (Keywords Including @webex, @meet:myroom)

Hybrid Calendar Service does not add Webex details if the meeting invitation already contains Webex join links (for example, added with Productivity Tools or manually by the meeting organizer). The meeting organizer can manually
                                    delete any previously added join links so that Hybrid Calendar Service can add the new join links.

Hybrid Calendar Service does not process meetings with more than 300 meeting invitees.

You cannot customize the meeting details template except to modify the line of text that is included if you check Use a Pilot Number in Webex Site Administration. For instructions, see Can I Customize the Email Template Used by the Cisco Webex Hybrid Calendar Services with @Webex?

### Scheduling in a Cisco Webex Space (Keywords Including @webex:space, @meet, @spark)

Space keyword scheduling currently supports a maximum of 60 meeting participants. A meeting organizer who invites more than
                                    60 participants will receive an email message indicating that they have exceeded the maximum.

Space keyword scheduling does not currently handle distribution lists. Individual members of the distribution list still receive
                                    the meeting invitation with details on joining the space, but are not automatically added to the space. As a workaround, the
                                    meeting organizer can expand the mailer on the TO line before sending the invite. That way, each user is individually added
                                    to the space.

Attachments that users add to meeting invites with space keywords are not added to the corresponding space.

The Hybrid Calendar Service no longer sends a separate email message to meeting invitees who are not Cisco Webex users, inviting them to sign up.

You cannot customize the meeting details template that is used for meetings scheduled in a space.

### One Button to Push (OBTP)

For issues involving the Join button and meetings list in the Webex app, see the Known Issues for Cisco Webex Meetings article.

### Cisco TMS Integration with Google Calendar

If the conference bridge that is scheduled to host an upcoming meeting becomes unavailable, Cisco TMS updates the meeting
                                    join details to use a different bridge. However, the meeting join details do not get updated in Google Calendar unless the
                                    organizer makes a change to the meeting invitation. This can cause problems when invitees try to join the meeting from the
                                    invitation.

If a meeting scheduler's time zone in Google Calendar does not match the scheduler's time zone in Cisco TMS, the system may
                                    have a problem scheduling recurring meetings. This can cause a mismatch between the instance dates in Google Calendar and
                                    in Cisco TMS. As a workaround, make sure users' time zones in Google Calendar match their time zones in Cisco TMS.

When a recurring meeting series scheduled with @meet is edited multiple times, the series updates correctly in Google Calendar
                                    but may not update correctly in Cisco TMS. The behavior is not consistent. For example, changing the subject of a single instance
                                    of the series and then changing the subject of the entire series may result in the subject changing only for the modified
                                    instance—or for all instances other than the modified instance.

If an endpoint is already booked in Google Calendar for a given time slot for a non-@meet meeting, and an organizer schedules
                                    a meeting with @meet which overlaps the booked time slot, the organizer gets a message saying that the endpoint declined the
                                    meeting, but Cisco TMS creates the overlapping meeting anyway.

For such meetings, the Calendar Connector sends an extra meeting request and logs two different informational messages that
                                    each include one of the following strings:

status:MEETING_NOT_FOUND_ON_TMS

status:UN_EXPECTED_EXCEPTION

The Calendar Connector should raise an alarm if the organization to which the Expressway host is registered has the @meet
                                    keyword action set to Cisco TelePresence Management Suite but the Calendar Connector has not been linked to Cisco TMS on the Expressway Applications > Hybrid Services > Calendar Service > Cisco Conferencing Services Configuration page. This alarm has not been implemented.

If you remove the Cisco TMS configuration from the Expressway connector host, users can continue to schedule @meet meetings
                                    on Cisco TMS until the Expressway connector host is restarted. The workaround is to restart the Expressway connector host
                                    after removing the Cisco TMS configuration.

## Exchange and Office 365 (Expressway-Based Calendar Connector)

### Calendar Connector Deployment and Configuration

Calendar Connector supports single cluster with a maximum of two Expressway instances per organization.

Proxy connections must use basic authentication or no username and password. No other authentication schemes are supported.

The Calendar Connector currently does not support Exchange organizations that require the service (impersonation) account
                                    to use multi-factor authentication (MFA).

For some customers, the Calendar Connector raises a critical alarm described as "Redirected Microsoft Exchange Autodiscovery
                                    URL not trusted." The issue may result in some delays processing calendar events for users. In some cases, the Calendar Connector
                                    will be unable to provide any service to some portion of the users.

If you see this alarm, use the Autodiscover Redirect URL trust list to configure how the Calendar Connector can locate user mailboxes.

For some customers, the Calendar Connector raises an "NTLM authentication error: Credentials cannot be used for NTLM authentication"
                                    warning in the hybrid_services_log files. This can occur if a connector proxy is configured on the Applications > Hybrid Services
                                    > Connector Proxy page in Expressway and that proxy requires authentication. No workaround is required as long as the connector
                                    proxy supports Basic authentication scheme, or does not require authentication.

If you deregister the Calendar Connector, or deactivate it if it's the only hybrid service on the Expressway , the Expressway can get into an error state where hybrid service connectors will not register, configuration changes do not propagate, or
                                    other problems occur. The workaround is to reboot the Expressway and reregister the connector.

You cannot search in https://admin.webex.com to return the set of users who have hybrid calendar service turned on or off.

When adding a Cisco Webex site to the Calendar Connector configuration, you must enter the Fully Qualified Site Name value
                                    entirely in lowercase. Uppercase characters cause the Calendar Connector to raise a "service unreachable or access denied"
                                    alarm.

The Cisco TMS integration does not currently support Microsoft Exchange or hybrid Exchange deployments (Microsoft Exchange
                                    and Office 365 together). The integration currently works only with the cloud-based Hybrid Calendar Service for Office 365
                                    or the cloud-based Hybrid Calendar Service for Google Calendar.

The integration uses the Calendar Connector to link the Hybrid Calendar Service with Cisco TMS. Once you configure the TMS
                                    scheduling option on an Expressway-C, you cannot link the same Calendar Connector to Microsoft Exchange, and vice versa.

### General Scheduling Issues (All Keywords)

Hybrid Calendar Service does not support shared calendars. The service can process meetings that a delegate schedules on behalf of others, as long
                                    as they schedule the meeting in the user's actual calendar, not a shared or group calendar.

If you add a scheduling keyword or supported video address to a single instance of a recurring meeting series, the meeting
                                    join details are not updated. As a workaround, add the keyword or video address to the entire meeting series.

Users may see multiple meeting invitations in their Outlook inbox when receiving meetings scheduled with a keyword or supported
                                    video address. As a workaround, check the following check boxes in the Microsoft Outlook Web app under Settings > Calendar > Automatic Processing :

Delete meeting requests and responses that have been updated

Automatically process requests and responses from external senders

These settings are available only in the web app, but the above changes apply to all Outlook clients.

Hybrid Calendar Service does not add meeting join links to the meeting invitation for any invitees who have single quotes around their email addresses.
                                    As a workaround, do not include single quotes around email addresses in the invitation.

In order for OBTP to work consistently on invited devices, you must ensure that the mail system does not have a policy to
                                    automatically delete meeting comments. The following PowerShell command ensures that comments are retained so that the Hybrid
                                    Calendar Service can use them to process meetings:

```
Set-CalendarProcessing -identity "room" -DeleteComments $false
```

In some versions of Microsoft Outlook 2016, after changing a single instance of a recurrent scheduled meeting where a scheduling
                                    keyword is in the location field, the body text and join links might disappear.

If possible, upgrade to the latest version of Outlook.

If you cannot upgrade, delete and reschedule the affected instance.

The other instances of the meeting series should be unaffected.

Meeting organizers using Microsoft Outlook 2011 for Mac may not see the join links in their meeting invites, although the
                                    invitees receive the links. This is an issue with Outlook 2011 for Mac and the solution is to upgrade to a more recent version
                                    of Outlook for Mac.

Hybrid Calendar Service does not automatically add meeting join information to a meeting that's scheduled in the past.

When a delegate cancels a meeting on the organizer's behalf, the Hybrid Calendar Service can take up to 24 hours to remove
                                    the meeting from the  meetings list in the Webex app.

### Scheduling a Webex Personal Room Meeting (Keywords Including @webex, @meet:myroom)

Hybrid Calendar Service does not add Webex details if the meeting invitation already contains Webex join links (for example, added with Productivity Tools or manually by the meeting organizer). The meeting organizer can manually
                                    delete any previously added join links so that Hybrid Calendar Service can add the new join links.

Hybrid Calendar Service does not process meetings with more than 300 meeting invitees.

You cannot customize the meeting details template except to modify the line of text that is included if you check Use a Pilot Number in Webex Site Administration. For instructions, see Can I Customize the Email Template Used by the Cisco Webex Hybrid Calendar Services with @Webex?

### Scheduling in a Cisco Webex Space (Keywords Including @webex:space, @meet, @spark)

Space keyword scheduling currently supports a maximum of 60 meeting participants. A meeting organizer who invites more than
                                    60 participants will receive an email message indicating that they have exceeded the maximum.

Space keyword scheduling does not currently handle distribution lists. Individual members of the distribution list still receive
                                    the meeting invitation with details on joining the space, but are not automatically added to the space. As a workaround, the
                                    meeting organizer can expand the mailer on the TO line before sending the invite. That way, each user is individually added
                                    to the space.

The Hybrid Calendar Service no longer sends a separate email message to meeting invitees who are not Cisco Webex users, inviting them to sign up.

Attachments that users add to meeting invites with space keywords are not added to the corresponding space.

You cannot customize the meeting details template that is used for meetings scheduled in a space.

### One Button to Push (OBTP)

For issues involving the Join button and meetings list in the Webex app, see the Known Issues for Cisco Webex Meetings article.

### Customers Also Viewed

- Troubleshooting Guide for Cisco Webex Hybrid Call Service Connect