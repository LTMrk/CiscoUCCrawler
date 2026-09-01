---
doc_id: help-webex-com-en-us-article-niqovwv-hybrid-calendar-service-with-microsoft-365-integration-reference-0c9c8b6651
source_url: https://help.webex.com/en-us/article/niqovwv/Hybrid-Calendar-Service-with-Microsoft-365-integration-reference
retrieved_at: 2026-09-01T21:38:06.665962+00:00
---

## Hybrid Calendar benefits

Currently, the integration provides the following major features:

Provide end users with the ability to schedule a collaboration meeting with any calendar
          client connected to Microsoft 365 without having to install plug-ins or extensions. Type a
          keyword into the Location field (for example, @webex or @meet) or
          put a video address URI or meeting address into the meeting body.

Show a meetings list in users' Webex App applications—desktop, mobile, and hard endpoints.

Pop up a notification with a Join button, also known as One Button to Push (OBTP).

Update a user’s Webex App presence status when the user sets up automatic replies in Microsoft 365 (sometimes
          referred to as out-of-office status).

This article gives an overview of how the cloud-based Hybrid Calendar Service integrates the
      Microsoft 365 cloud with the Webex cloud to provide these features.

For similar overviews of the other Hybrid Calendar Service integrations, see the following articles:

Cisco Webex Hybrid Calendar Service with Microsoft Exchange integration reference (for Expressway-based Calendar Connector deployments)

Cisco Webex Hybrid Calendar Service with Google Calendar integration reference

For the latest feature and deployment information, see https:/​/​www.cisco.com/​go/​hybrid-services-calendar .

## Data handling

The  Hybrid Calendar receives meeting details from the calendar system and uses them as follows:

- checks the meeting location and body for URIs and URLs to join the meeting

- the title of the invite as the meeting title

- the start and end times to show the meeting slot on the meetings list in Webex App and on some devices

- the invitees to populate the participant list in the meetings list

- the invitees to send them the Join button, when it's time to join

- the meeting invite body to populate the Webex meeting agenda

The service sends encrypted data to the Webex cloud (and stores the data in encrypted form)
      to provide the meetings list and Join button.

The service does not store or transmit unencrypted data. Sensitive data such as meeting
      description, meeting body, and email addresses of invitees is always encrypted when stored and
      transmitted.

The  Hybrid Calendar service retains meeting data for a limited time. The stored data covers meetings from 7
      days in the past through 31 days in the future.

For data encryption, the  Hybrid Calendar uses the same Webex cloud encryption service that Webex App uses. As such, the cloud Key Management Server (KMS) provides key management. If you choose
      to deploy Hybrid Data Security, your own on-premises KMS provides the key management. (For more details, see the Webex App Security Paper .)

## Microsoft 365 tenant support

Note the following considerations for your Microsoft 365 tenant:

- The commercial version of Webex only supports the Worldwide instance of Microsoft 365.
          (Webex doesn't support USGovDoD, USGovGCCHigh, China, and Germany instances.)

Webex for Government supports the Worldwide instance of Microsoft 365 through a tenant in GCC and the
            USGovGCCHigh instance. (Webex for Government doesn't support the USGovDoD, China, and
            Germany instances.)

Microsoft 365 includes Multi-Geo Capabilities that enable your tenants to store data in
            a chosen geography. But, Webex stores data according to its own data residency
            specifications based on the country designated for the customer organization. For more
            information, see https://www.cisco.com/go/webex-teams-locality .

## Authentication and authorization during deployment

The Hybrid Calendar uses Microsoft Graph Authorization to access users' calendars within an organization.

There are two options to providing authorization for Hybrid Calendar to access a user's
        calendar.

In Enterprise environments, the Global administrator of the Microsoft 365 tenant grants the
        permissions to the Hybrid Calendar for all users in the organization. This method is
        exclusive to enterprise customers.

The second option is to allow users to authorize the Hybrid Calendar themselves using Connect your Microsoft
          365 calendar . "Connect your Calendar" requires a periodic user reauthorization.
        This method is available to all types of users.

### Enterprise application authentication process

Provisioning grants the Hybrid Calendar the following required permissions:

Permission

Usage

Read and write calendars in all mailboxes.

Update the meeting text with the join details.

Sign in and read user profile.

Required for the other permissions listed. Hybrid Calendar doesn’t use it
                      directly.

Read and write all user mailbox settings.

Determine the user's language for localization purposes.

Read out-of-office status.

Set out-of-office status (reserved for future use).

Read domains.

Used to efficiently route users to the proper Microsoft 365 tenant

Read directory RBAC settings

To determine if this user is a Global Administrator in the requested tenant

In Control Hub, only administrators with privileged access can set up the Hybrid Calendar
        for a customer's organization. The provisioning process requires authentication by an
        administrator and consent by a Global administrator for the Microsoft 365 tenant to which
        your users belong.

The flow includes the following high-level steps:

The organization administrator signs in to Control Hub and starts the Hybrid Calendar
            with Microsoft 365 setup.

The Hybrid Calendar redirects the browser to the Microsoft 365 cloud for authentication
            and consent.

Microsoft 365 prompts the admin to sign in to the Microsoft 365 tenant. Admin signs in
            with Global administrator account.

The admin must consent to Webex checking that they are a Global Administrator in this
            tenant.

Webex does this check with Microsoft 365. If successful, Webex requests calendar
            permissions.

Microsoft 365 prompts the admin to sign in to the Microsoft 365 tenant. Admin signs in
            with Global administrator account.

The administrator must consent to Webex accessing calendar data. Calendar service
            returns a prompt for a test email account.

The administrator enters a test email address, and Webex tries to create an event in
            the test account's calendar.

Depending on the results of the test, the administrator gets an updated success or
            failure indication.

### User application authentication process

User provisioning grants the Hybrid Calendar the following required permissions:

Permission

Usage

Read and write calendars.

Update the meeting text with the join details.

Offline access.

Grants Webex a refresh token which limits end-user reauthorization requests
                      to every 30 days.

Read and write all user mailbox settings.

Determine the user's language for localization purposes.

Read out-of-office status.

Set out-of-office status (reserved for future use).

Sign in and read user profile.

Required for the other permissions listed. The Hybrid Calendar doesn’t use it
                      directly.

## Hybrid Calendar in the Microsoft Azure portal

After authorizing Webex Calendar service to access your Microsoft 365 tenant for the
        Enterprise, the Microsoft Azure Active Directory admin center displays the service in the
        enterprise applications list.

Click the service name, Cisco Webex Connect Your Calendar and open the Permissions page, to see the permissions that you granted to the service.

## Limit the application scope to specific mailboxes

When you set up the Hybrid Calendar for the enterprise, we request authorization for the entire organization. Microsoft Azure allows you to limit the scope to specific mailboxes either before or after provisioning.

Use the Microsoft documentation to limit the scope. For example, see https://learn.microsoft.com/en-us/graph/auth-limit-mailbox-access for steps to limit the scope before provisioning
            Hybrid Calendar.

## Provisioning Hybrid Calendar with API operations

The  Hybrid Calendar uses the Microsoft Graph API to access Microsoft 365 calendar events. This
        API supports a broad range of operations with Microsoft 365. However, the  Hybrid Calendar only uses a subset of commands that are related to calendar use cases.

Graph operation

Usage

POST /users/{id | userPrincipalName}/calendar/events

Add an event or meeting to a user's calendar.

GET /users/{id | userPrincipalName}/events/{id}

Retrieve details about a single event in a user's calendar.

GET /users/{id | userPrincipalName}/calendar/events/{id}/instances? startDateTime={start_datetime}&endDateTime={end_datetime}

Get the occurrences of a recurring meeting for a specified time range.

GET /users/{id | userPrincipalName}/calendar/events

Retrieve details about events in a user's calendar folder.

POST /subscriptions

Subscribe for notifications on changes to a user's calendar.

GET /users/{id|userPrincipalName}/mailboxSettings

Get a user's locale and out-of-office status.

DELETE /subscriptions/{id}

Unsubscribe from notifications on changes to a user's calendar.

PATCH /users/{id | userPrincipalName}/calendar/events/{id}

Update properties of calendar events (including join information and extended properties) in addition to other fields pertaining to the meeting.

POST /users/{id|userPrincipalName}/calendar/getSchedule

Displays the user availability and free/busy status for a specified time range.

DELETE /users/{id | userPrincipalName}/calendar/events/{id}

Deletes an event from a calendar.

POST /users/{id |
                    userPrincipalName}/calendar/events/{id}/{accept | decline |
                    tentativelyAccept}

Allows the user to accept/decline/tentatively-accept the status for a meeting.

GET
                    /roleManagement/directory/roleAssignments

Retrieve roles assigned to user requesting consent.

| Permission | Usage |
|---|---|
| Read and write calendars in all mailboxes. | Update the meeting text with the join details. |
| Sign in and read user profile. | Required for the other permissions listed. Hybrid Calendar doesn’t use it
                      directly. |
| Read and write all user mailbox settings. | Determine the user's language for localization purposes. Read out-of-office status. Set out-of-office status (reserved for future use). |
| Read domains. | Used to efficiently route users to the proper Microsoft 365 tenant |
| Read directory RBAC settings | To determine if this user is a Global Administrator in the requested tenant |

| Permission | Usage |
|---|---|
| Read and write calendars. | Update the meeting text with the join details. |
| Offline access. | Grants Webex a refresh token which limits end-user reauthorization requests
                      to every 30 days. |
| Read and write all user mailbox settings. | Determine the user's language for localization purposes. Read out-of-office status. Set out-of-office status (reserved for future use). |
| Sign in and read user profile. | Required for the other permissions listed. The Hybrid Calendar doesn’t use it
                      directly. |

| Graph operation | Usage |
|---|---|
| POST /users/{id \| userPrincipalName}/calendar/events | Add an event or meeting to a user's calendar. |
| GET /users/{id \| userPrincipalName}/events/{id} | Retrieve details about a single event in a user's calendar. |
| GET /users/{id \| userPrincipalName}/calendar/events/{id}/instances? startDateTime={start_datetime}&endDateTime={end_datetime} | Get the occurrences of a recurring meeting for a specified time range. |
| GET /users/{id \| userPrincipalName}/calendar/events | Retrieve details about events in a user's calendar folder. |
| POST /subscriptions | Subscribe for notifications on changes to a user's calendar. |
| GET /users/{id\|userPrincipalName}/mailboxSettings | Get a user's locale and out-of-office status. |
| DELETE /subscriptions/{id} | Unsubscribe from notifications on changes to a user's calendar. |
| PATCH /users/{id \| userPrincipalName}/calendar/events/{id} | Update properties of calendar events (including join information and extended properties) in addition to other fields pertaining to the meeting. |
| POST /users/{id\|userPrincipalName}/calendar/getSchedule | Displays the user availability and free/busy status for a specified time range. |
| DELETE /users/{id \| userPrincipalName}/calendar/events/{id} | Deletes an event from a calendar. |
| POST /users/{id \|
                    userPrincipalName}/calendar/events/{id}/{accept \| decline \|
                    tentativelyAccept} | Allows the user to accept/decline/tentatively-accept the status for a meeting. |
| GET
                    /roleManagement/directory/roleAssignments | Retrieve roles assigned to user requesting consent. |