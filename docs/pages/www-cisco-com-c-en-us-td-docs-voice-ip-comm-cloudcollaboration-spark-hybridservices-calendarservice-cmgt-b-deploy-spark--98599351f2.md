---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-spark-hybridservices-calendarservice-cmgt-b-deploy-spark--98599351f2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/spark/hybridservices/calendarservice/cmgt_b_deploy-spark-hybrid-calendar-service/cmgt_b_deploy-spark-hybrid-calendar-service_chapter_0110.html
retrieved_at: 2026-08-20T23:53:53.868085+00:00
---

Deployment guide for Hybrid Calendar

# Deployment guide for Hybrid Calendar

Updated: October 17, 2023

Chapter: Prepare your environment

## Chapter: Prepare your environment

# Prepare your environment

## How the Hybrid Calendar accesses user calendars

When you first set up the Hybrid Calendar , you need to grant it permission to access Office 365 on behalf of your users. Use an account that can authorize multi-tenant
                           apps (like Global Administrator or Privileged Role Administrator) to grant the permission.

The Hybrid Calendar needs these permissions to do the following actions:

Permission

Usage

Read and write calendars in all mailboxes.

Update the meeting text with the join details.

Sign in and read user profile.

Required for the other permissions listed. Hybrid Calendar does not use it directly.

Read and write all user mailbox settings.

Determine the user's language for localization purposes.

Read out-of-office status.

Set out-of-office status (reserved for future use.)

Read domains.

Read domains

When the administrator grants permission for the Hybrid Calendar on behalf of the Office 365 tenant, Webex is notified. This permission enables the Hybrid Calendar to get access tokens from Azure Active Directory (Azure AD) using OAuth 2.0, to authenticate and access user calendars. The Webex cloud does not see or store the administrator login credentials at any point in the process. For more information, see https://docs.microsoft.com/en-us/graph/auth-v2-service .

The Hybrid Calendar uses the Microsoft Graph API to subscribe to changes in users’ calendars, receive notifications for changes made in subscribed users’ calendars, and update
                           meeting invitations with scheduling information when the meeting location field contains keywords such as @webex or @meet,
                           or the meeting body contains a supported video address. The Hybrid Calendar accesses only the calendars of the users that you enable for Hybrid Calendar in the Control Hub .

Webex App follows industry-standard best practices to securely store the Private Key for the application. All meeting details that
                           the service stores are encrypted using Webex App end-to-end encryption. This ensures that only those who are invited to the meeting can see the details. For more information
                           on Webex App encryption, see the Cisco Webex Security and Privacy white paper .

If needed, your Exchange administrator can revoke the Hybrid Calendar access to your Office 365 tenant user calendars from Enterprise Applications in the Azure AD management portal.

## Deploying alongside an existing Expressway-based Calendar Connector

If you have already deployed the Expressway-based Calendar Connector to serve Microsoft Exchange users, Office 365 users or
                           a hybrid of Microsoft Exchange and Office 365 users, you can add the cloud-based Hybrid Calendar with Office 365, running
                           both at the same time. Once you enable the cloud-based service, any Office 365 users who are not a part of a resource group
                           automatically migrate from your Calendar Connector to the new cloud-based service within 24 hours. (The Hybrid Calendar checks
                           for Office 365 users to migrate from Calendar Connectors once a day.)

The Expressway-based Calendar Connector that you deploy with the Hybrid Calendar for Microsoft Exchange or Office 365 has
                           a capacity limit of 1,000 Office 365 users, and requires on-premises equipment. The cloud-based service allows you to scale past the capacity
                           limit.

- Both options (Calendar Connector and cloud-based service) can be enabled at the same time.

- All Office 365 users NOT in a resource group migrate to the cloud-based service automatically.

- To enable some users on the cloud service first for testing, put other users who must stay homed on the on-premises Connector
                              into a resource group before turning on the cloud-based service.

## Change processing timeframes

When you activate the Hybrid Calendar for Office 365 and enable users or move mailboxes, the service processes these changes
                              periodically.

Administrator action

Processing behavior

Expected completion timeframe

Activation

Enable the Hybrid Calendar for the organization.

Once the setup is successful, the Hybrid Calendar tries to subscribe to calendars of users that are listed in "Not activated"
                                          or "Error" states.

Depending on volume, immediate to minutes.

Enable individual users (toggle on Calendar or bulk enable).

Hybrid Calendar attempts to subscribe to the user's calendar.

If the activation fails, the user is in "Error" state and the Hybrid Calendar retries in 60 minutes.

If the activation fails multiple times, the Hybrid Calendar retries in 24 hours.

If everything goes well, immediately. Otherwise, up to 24 hours.

If it takes longer than this, check the user account.

Mailbox migration

Move user mailbox from on-premises Exchange to Office 365.

Once Office 365 has completed the mailbox migration, it takes up to 40 minutes for the Hybrid Calendar to put the user in
                                          "Error" state.

As above, the Hybrid Calendar attempts to reprocess users in "Error" state every 60 minutes.

If everything goes well, up to 100 minutes. Otherwise, up to 24 hours.

If it takes longer than this, check the user account.

Move user mailbox from Office 365 to on-premises Exchange.

Once a day, the Hybrid Calendar runs a watch refresh that detects missing mailboxes and puts them in "Error" state.

Another cloud service then reassigns the user to an Expressway-based Calendar Connector.

Up to 24 hours to detect the change, plus a few minutes of  reassignment time.

## Requirements for Hybrid Calendar with Microsoft Office 365

A Microsoft 365 tenant with Exchange online accounts for users in the organization. During setup, you must sign in with an
                                 account that can authorize multi-tenant apps (like Global Administrator or Privileged Role Administrator) to grant the appropriate
                                 permission.

Note the following considerations for your Microsoft 365 tenant:

The commercial version of Webex only supports the Worldwide instance of Office 365. (Webex doesn't support USGovDoD, USGovGCCHigh,
                                       China, and Germany instances.)

Webex for Government supports the Worldwide instance of Office 365 through a tenant in GCC and the USGovGCCHigh instance. (Webex for Government
                                       doesn't support the USGovDoD, China, and Germany instances.)

Office 365 includes Multi-Geo Capabilities that enable your tenants to store data in a chosen geography. But, Webex stores
                                       data according to its own data residency specifications based on the country designated for the customer organization. For
                                       more information, see https://www.cisco.com/go/webex-teams-locality .

For @webex scheduling, any supported Webex Meetings release.

You must enable the Personal Room feature for the Webex site and for the individual users .

A Webex organization with a paid subscription.

We don’t currently support deploying both Google Calendar and Office 365 with the cloud-based Hybrid Calendar in the same Webex organization.

Users must have activated Webex accounts, with email addresses that are exact matches in Webex Meetings , Webex App , and Exchange online (the Primary Email Address).

Each Webex App user can only have one email address associated with only one Hybrid Calendar integration. In other words, the Hybrid Calendar
                                 will only process meetings from a single address for creating spaces, decorating meetings, showing the meetings list and join
                                 button, and sending the Join button to video devices.

| Permission | Usage |
|---|---|
| Read and write calendars in all mailboxes. | Update the meeting text with the join details. |
| Sign in and read user profile. | Required for the other permissions listed. Hybrid Calendar does not use it directly. |
| Read and write all user mailbox settings. | Determine the user's language for localization purposes. Read out-of-office status. Set out-of-office status (reserved for future use.) |
| Read domains. | Read domains |

| Administrator action | Processing behavior | Expected completion timeframe |
|---|---|---|
| Activation |
| Enable the Hybrid Calendar for the organization. | Once the setup is successful, the Hybrid Calendar tries to subscribe to calendars of users that are listed in "Not activated"
                                          or "Error" states. | Depending on volume, immediate to minutes. |
| Enable individual users (toggle on Calendar or bulk enable). | Hybrid Calendar attempts to subscribe to the user's calendar. If the activation fails, the user is in "Error" state and the Hybrid Calendar retries in 60 minutes. If the activation fails multiple times, the Hybrid Calendar retries in 24 hours. | If everything goes well, immediately. Otherwise, up to 24 hours. If it takes longer than this, check the user account. |
| Mailbox migration |
| Move user mailbox from on-premises Exchange to Office 365. | Once Office 365 has completed the mailbox migration, it takes up to 40 minutes for the Hybrid Calendar to put the user in
                                          "Error" state. As above, the Hybrid Calendar attempts to reprocess users in "Error" state every 60 minutes. | If everything goes well, up to 100 minutes. Otherwise, up to 24 hours. If it takes longer than this, check the user account. |
| Move user mailbox from Office 365 to on-premises Exchange. | Once a day, the Hybrid Calendar runs a watch refresh that detects missing mailboxes and puts them in "Error" state. Another cloud service then reassigns the user to an Expressway-based Calendar Connector. | Up to 24 hours to detect the change, plus a few minutes of  reassignment time. |

| Note | We don’t currently support deploying both Google Calendar and Office 365 with the cloud-based Hybrid Calendar in the same Webex organization. |
|---|---|