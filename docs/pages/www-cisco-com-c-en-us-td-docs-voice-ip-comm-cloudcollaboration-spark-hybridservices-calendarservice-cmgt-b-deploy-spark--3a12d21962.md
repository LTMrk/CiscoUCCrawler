---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-spark-hybridservices-calendarservice-cmgt-b-deploy-spark--3a12d21962
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/spark/hybridservices/calendarservice/cmgt_b_deploy-spark-hybrid-calendar-service/cmgt_b_deploy-spark-hybrid-calendar-service_chapter_01001.html
retrieved_at: 2026-08-20T23:21:15.771760+00:00
---

Deployment guide for Hybrid Calendar

# Deployment guide for Hybrid Calendar

Updated: October 17, 2023

Chapter: Deploy cloud-based Hybrid Calendar with Google Calendar

## Chapter: Deploy cloud-based Hybrid Calendar with Google Calendar

# Deploy cloud-based Hybrid Calendar with Google Calendar

## Hybrid Calendar with Google Calendar deployment task flow

To deploy Hybrid Calendar with your Google Calendar environment, perform the following tasks.

### Before you begin

Prepare Your Environment

Step 1

Enable and configure Hybrid Calendar with Google Calendar

Register your Google Calendar environment to the Webex cloud, test the connection, and set the default Webex site.

Step 2

(Optional) Localize meeting join details

To override how the Hybrid Calendar localizes meeting join details for your entire organization, set the Default Language setting in https://admin.webex.com .

Step 3

(Optional) Configure @webex and @meet keywords

To change the action that the Hybrid Calendar takes when users enter @webex or @meet, set the Keywords settings in https://admin.webex.com .

Step 4

(Optional) Customize email templates

Choose what the Hybrid Calendar adds to meeting invitations, including audio or video join details and a localized header and footer in any language that
                                          the service supports.

Step 5

Enable the Hybrid Calendar with Google for users

After successfully provisioning the service, you must explicitly activate users to allow the service to access their respective
                                          G suite calendars.

Step 6

(Optional) Add Hybrid Calendar to workspaces with Board, Desk, and Room series

If you want One Button to Push (OBTP) functionality to be provided to cloud-registered room and desk devices and Webex Boards, toggle on the calendar service for the devices, and configure the resource email address.

Step 7

(Optional) Associate personal rooms with Webex App

For OBTP on Webex room and desk devices and Webex Boards, make sure that meeting schedulers have their Personal Rooms associated with their Webex App accounts.

Step 8

Test the Google Calendar and Hybrid Calendar integration

## Enable and configure Hybrid Calendar with Google Calendar

Follow these steps to register your Google Calendar environment to the Webex cloud. The setup wizard in Control Hub guides you through the process.

Step 1

Sign in to Control Hub .

Step 2

Under Services , select Hybrid > Hybrid Calendar (Google) > Set Up .

- Domain-wide Delegation : Choose this option if you want to give Webex access to all rooms and calendars.

This authorization expires every 180 days, per Google security policy. You must reauthorize this every 180 days by following
                                                         steps a—c in the Workspaces Only section below and clicking Reauthorize .

If you selected Domain-wide Delegation , proceed to step 3.

If you selected Workspaces Only , proceed to step 4.

Step 3

For Domain-wide Delegation , complete the following steps.

In a new browser tab, open your G Suite account dashboard.

From the Google Admin console, go to Security > Access and data control > API controls .

In the Domain-wide delegation section, click MANAGE DOMAIN WIDE DELEGATION .

Click Add New to add an API client.

Copy the value for Client ID to the clipboard from the Control Hub tab you have open, and paste it into the corresponding field in your G Suite settings
                                             tab.

Copy the text for Scope to the clipboard from the Control Hub tab you have open, and paste it into the corresponding field in your G Suite settings
                                             tab.

Click Authorize , then return to this page and click Next .

Enter the address of a test email account that already has a G Suite license, then click Next . This is used to test the connection with Google Calendar.

(Optional) To enable Hybrid Calendar for Workspaces, provide a Workspace Admin account that has either Google super admin rights, or Make changes to events privileges, for all Google rooms that will be enabled with Hybrid Calendar .

(Optional) To enable Room Scheduling from Workspaces , configure a Room scheduling account. This account requires either Google super admin rights, or Make changes to events privileges, for all Google rooms that require in-room scheduling. You can reuse the Workspace Admin account from the previous
                                             step.

After the set up completed prompt appears, click Done .

From the Hybrid Calendar card, go to the Google Calendar Settings .

Choose or type the default Webex Meetings site that you want to use for @webex scheduling, and save your changes.

The default site is used for @webex unless the user has a different site configured in their My Personal Room setting in the Webex App app (either because the user's Webex site has been linked to Control Hub by an administrator , or because the user configured the setting with a different site).

Step 4

For Workspaces Only , complete the following steps.

Click Workspaces Only , then click Next .

Enter the Google account email address you want Hybrid Calendar to use to access Google room calendars. Make sure this account has either Google super admin rights, or Make changes to events privileges, for all Google rooms that will be enabled with Hybrid Calendar .

To use this Workspace Admin account for in-room scheduling, select Also use this account for in-room scheduling .

Click Next .

When prompted to choose a Google account, choose the same account you entered in step c.

Click Finish .

Once your authorization is complete, you can make changes to it. Click Settings , then in the Authorization section, click Edit Authorization .

## Localize meeting join details

In Control Hub , the Default Language setting controls the language of the join details that the Hybrid Calendar adds to invitations. If
                              you leave the setting at its default, the service uses the language from the locale setting from scheduler's calendar settings .

To override choosing languages based on meeting schedulers' settings, choose a specific language to use for join details for
                              all meetings across your organization.

Step 1

Sign in to the customer view of https://admin.webex.com .

Step 2

In the left-hand navigation pane, under Services click Hybrid .

Step 3

From the Hybrid Calendar card for Google, click Edit settings .

Step 4

In the Meeting Invitations section, choose a language from the Default Language drop-down list, and click Save .

## Configure @webex and @meet keywords

By default, when users add @webex to a meeting location, the calendar service updates the meeting with their Webex Personal Room details. When users add @meet , by default the service updates the meeting with Webex App space details. As an administrator, you can change these default actions for either keyword.

Regardless of how you set these actions, power users can add the modifier :space , :myroom or :onetime to specify the action for either keyword. For example, adding @webex:space causes the service to update the meeting with Webex App space details. As well, @webex:onetime creates a one-time Webex meeting.

Step 1

Sign in to the customer view of https://admin.webex.com/login .

Step 2

In the left-hand navigation pane, under Services click Hybrid .

Step 3

From the Hybrid Calendar card for your calendar environment, click Edit settings .

If you have the Hybrid Calendar set up for multiple calendar environments, you can access the keywords settings from multiple pages in Control Hub , but the values that you set apply to all environments.

Step 4

Select the tenant to configure.

Step 5

Click the Settings tab.

Step 6

In the Keywords section, select the default action that you want for each keyword.

Step 7

Click Save .

## Customize email templates

Step 1

Sign in to the customer view of https://admin.webex.com/login .

Step 2

In the left-hand navigation pane, under Services click Meeting .

Step 3

Locate the Customize Meeting Join Details section.

Step 4

Choose whether to show Join by Phone details.

When you include the dial-in details, you can also choose to
                                          add a link to global call-in numbers, a link to toll-free calling
                                          restrictions, or both.

Step 5

Show or hide details on joining from an application or video conferencing device.

When you include the video dialing details, you can also
                                          choose to include an IVR IP address, a Skype for Business join link, or
                                          both.

Step 6

Click Add a Language and then select the language from the drop-down menu to create a custom header and footer for any of the languages that the
                                       Hybrid Calendar supports. When you've got the header and footer text that you want, click Save .

The header and footer values have a maximum of 1024 characters each (including spaces).

Step 7

Once you've added a custom header and footer for a language, you can choose that language as a default for any other language
                                       that doesn't have a custom header and footer defined. Your default language choice saves automatically.

## Enable the Hybrid Calendar with Google for users

Use this procedure to enable a small number of Webex App users for Hybrid Calendar with Google Calendar.

See Ways to add and manage users in Control Hub for other methods, such as using a bulk CSV template.

Any of these methods requires that users have signed in to the Webex App to be fully activated. To enable @webex for users who have never signed in to the app, add and verify the users' domain using
                              the Add, verify, and claim domains process. (You must own a domain for it to be verifiable. You do not need to claim the domain.)

### Before you begin

To successfully activate a user for calendar access, the following conditions must be met:

Successful validation is a requirement for using the Hybrid Calendar functionality. If the service can't validate a user,
                              it puts the user in error state. The service enforces a policy to access only the calendars of successfully activated users
                              for ongoing processing.

Step 1

Sign in to the customer view in https://admin.webex.com .

Step 2

In the left-hand navigation pane, under Management click Users and then choose a specific user from the list.

You can use the search function to narrow down the list of users.

Step 3

Click the row to open an overview of the user.

Step 4

Choose one and then save your changes:

- In a new environment, click Calendar Service , toggle on Calendar , and ensure that the Google Calendar is selected.

- In an existing environment with Exchange, click Calendar Service , and under calendar type, ensure that the Google Calendar is selected.

After you activate the service, the Webex App user status changes from Pending Activation to Activated. The length of time for this change depends on the number of users
                                          that you're enabling for the service.

Users receive an email that indicates the feature is enabled. See the documentation below if you want to disable email notifications.

### What to do next

Schedule a  Webex Meeting from Your Calendar .

## Add Hybrid Calendar to workspaces with Board, Desk, and Room series

This task assumes that you've already created places for the Board, Desk, and Room devices. If you need to create the workspace,
                              see Add shared devices and services to a workspace .

### Before you begin

Webex room devices must have email addresses that match the Google room resource format, @resource.calendar.google.com .

If your room device email format uses a domain prefix, you must verify the domain in the prefix. For example, verify company.com (if you didn't already do so when verifying the domain of the account that manages access control lists) for devices that
                                    have email addresses such as:

```
company.com__3130313639353739333032@resource.calendar.google.com
```

Newer resource email addresses may not include a domain prefix, as in the following example:

```
c_0803348627605091471198@resource.calendar.google.com
```

Step 1

Sign in to the customer view of https://admin.webex.com/login .

Step 2

In the left-hand navigation pane, under Management click Workspaces .

Step 3

Go to Scheduling and select Calendar so that users can use One Button to Push (OBTP) on their devices.

Step 4

Select the calendar provider.

Step 5

Enter or paste the Google resource email address from G Suite (Calendar > Resources).

This is the email address that will be used to schedule meetings.

Step 6

Click Save .

## Associate personal rooms with Webex App

To provide the join button to devices when scheduling Webex Personal Room meetings, users must have their Personal Room associated
                              with their Webex App account. This can happen in one of the following ways:

The users on your Webex site have been Webex App linked. (For site linking steps, see Link Webex sites to Control Hub .)

Users change their own preferred Webex site from the Webex App settings or preferences, see Change your default meeting site

For a comprehensive approach, use the bulk CSV import process from Control Hub to set users’ preferredWebExSite in the steps
                                    that follow.

Step 1

Sign in to the customer view in https://admin.webex.com .

Step 2

In the left-hand navigation pane, under Management click Users .

Step 3

Click Manage Users .

Step 4

See this article for the detailed CSV import/export procedure.

Step 5

Use a CSV editor to change the preferredWebExSite attribute for all or some users.

Step 6

Import the CSV file.

## Test the Google Calendar and Hybrid Calendar  integration

Use these steps to set up a test meeting and verify the Google Calendar integration. Direct users to the documentation below
                              for how to schedule meetings.

Step 1

Sign in to https://calendar.google.com with one of the test Google user accounts enabled for Hybrid Calendar .

Step 2

Click Create to start an event, and then add a space scheduling keyword (such as @webex:space or @meet) to the Where field. Fill out other meeting information, as needed, and then click Save .

Step 3

Open https://teams.webex.com , and sign in with the test user account.

Step 4

Verify whether a new Webex space was created and contains the calendar invite card.

Step 5

To test out-of-office status, in https://calendar.google.com , navigate to Settings and turn on Vacation responder .

The display picture update is triggered when others see your presence in a space. If the test user does not interact with
                                                      other active users, you may need to use another account to verify the update.

Step 6

To test the join button with a Webex room or desk device or Webex Board:

In https://calendar.google.com , click Create to start an event, and then add a scheduling keyword (such as @webex) to the Location field.

Click Rooms , and choose the device you want to add.

Fill out other meeting information, as needed, and then click Save .

When the meeting is scheduled to begin, verify that the Join button appears on the device.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable and configure Hybrid Calendar with Google Calendar | Register your Google Calendar environment to the Webex cloud, test the connection, and set the default Webex site. |
| Step 2 | (Optional) Localize meeting join details | (Optional) To override how the Hybrid Calendar localizes meeting join details for your entire organization, set the Default Language setting in https://admin.webex.com . |
| Step 3 | (Optional) Configure @webex and @meet keywords | (Optional) To change the action that the Hybrid Calendar takes when users enter @webex or @meet, set the Keywords settings in https://admin.webex.com . |
| Step 4 | (Optional) Customize email templates | (Optional) Choose what the Hybrid Calendar adds to meeting invitations, including audio or video join details and a localized header and footer in any language that
                                          the service supports. |
| Step 5 | Enable the Hybrid Calendar with Google for users | After successfully provisioning the service, you must explicitly activate users to allow the service to access their respective
                                          G suite calendars. |
| Step 6 | (Optional) Add Hybrid Calendar to workspaces with Board, Desk, and Room series | (Optional) If you want One Button to Push (OBTP) functionality to be provided to cloud-registered room and desk devices and Webex Boards, toggle on the calendar service for the devices, and configure the resource email address. |
| Step 7 | (Optional) Associate personal rooms with Webex App | (Optional) For OBTP on Webex room and desk devices and Webex Boards, make sure that meeting schedulers have their Personal Rooms associated with their Webex App accounts. |
| Step 8 | Test the Google Calendar and Hybrid Calendar integration |  |

| Step 1 | Sign in to Control Hub . |
|---|---|
| Step 2 | Under Services , select Hybrid > Hybrid Calendar (Google) > Set Up . Domain-wide Delegation : Choose this option if you want to give Webex access to all rooms and calendars. Workspaces Only : Choose this option if you do not want to give domain-wide access, but still require Hybrid Calendar for Workspaces. In the
                                          steps below, you'll specify a Workspace Admin account that has Make changes to events access to all Google room resources. Note This authorization expires every 180 days, per Google security policy. You must reauthorize this every 180 days by following
                                                         steps a—c in the Workspaces Only section below and clicking Reauthorize . If you selected Domain-wide Delegation , proceed to step 3. If you selected Workspaces Only , proceed to step 4. | Note | This authorization expires every 180 days, per Google security policy. You must reauthorize this every 180 days by following
                                                         steps a—c in the Workspaces Only section below and clicking Reauthorize . |
| Note | This authorization expires every 180 days, per Google security policy. You must reauthorize this every 180 days by following
                                                         steps a—c in the Workspaces Only section below and clicking Reauthorize . |
| Step 3 | For Domain-wide Delegation , complete the following steps. In a new browser tab, open your G Suite account dashboard. From the Google Admin console, go to Security > Access and data control > API controls . In the Domain-wide delegation section, click MANAGE DOMAIN WIDE DELEGATION . Click Add New to add an API client. Copy the value for Client ID to the clipboard from the Control Hub tab you have open, and paste it into the corresponding field in your G Suite settings
                                             tab. Copy the text for Scope to the clipboard from the Control Hub tab you have open, and paste it into the corresponding field in your G Suite settings
                                             tab. Click Authorize , then return to this page and click Next . Enter the address of a test email account that already has a G Suite license, then click Next . This is used to test the connection with Google Calendar. (Optional) To enable Hybrid Calendar for Workspaces, provide a Workspace Admin account that has either Google super admin rights, or Make changes to events privileges, for all Google rooms that will be enabled with Hybrid Calendar . (Optional) To enable Room Scheduling from Workspaces , configure a Room scheduling account. This account requires either Google super admin rights, or Make changes to events privileges, for all Google rooms that require in-room scheduling. You can reuse the Workspace Admin account from the previous
                                             step. After the set up completed prompt appears, click Done . From the Hybrid Calendar card, go to the Google Calendar Settings . Choose or type the default Webex Meetings site that you want to use for @webex scheduling, and save your changes. The default site is used for @webex unless the user has a different site configured in their My Personal Room setting in the Webex App app (either because the user's Webex site has been linked to Control Hub by an administrator , or because the user configured the setting with a different site). |
| Step 4 | For Workspaces Only , complete the following steps. Click Workspaces Only , then click Next . Enter the Google account email address you want Hybrid Calendar to use to access Google room calendars. Make sure this account has either Google super admin rights, or Make changes to events privileges, for all Google rooms that will be enabled with Hybrid Calendar . To use this Workspace Admin account for in-room scheduling, select Also use this account for in-room scheduling . Click Next . When prompted to choose a Google account, choose the same account you entered in step c. Click Finish . Once your authorization is complete, you can make changes to it. Click Settings , then in the Authorization section, click Edit Authorization . |

| Note | This authorization expires every 180 days, per Google security policy. You must reauthorize this every 180 days by following
                                                         steps a—c in the Workspaces Only section below and clicking Reauthorize . |
|---|---|

| Step 1 | Sign in to the customer view of https://admin.webex.com . |
|---|---|
| Step 2 | In the left-hand navigation pane, under Services click Hybrid . |
| Step 3 | From the Hybrid Calendar card for Google, click Edit settings . |
| Step 4 | In the Meeting Invitations section, choose a language from the Default Language drop-down list, and click Save . After you save the change, the Hybrid Calendar uses the language you choose each time it adds join to details a meeting. It
                                       doesn’t change the language for existing join details. |

| Step 1 | Sign in to the customer view of https://admin.webex.com/login . |
|---|---|
| Step 2 | In the left-hand navigation pane, under Services click Hybrid . |
| Step 3 | From the Hybrid Calendar card for your calendar environment, click Edit settings . Note If you have the Hybrid Calendar set up for multiple calendar environments, you can access the keywords settings from multiple pages in Control Hub , but the values that you set apply to all environments. The Hybrid Calendar (Microsoft 365) displays a list of  tenants included in this organization. | Note | If you have the Hybrid Calendar set up for multiple calendar environments, you can access the keywords settings from multiple pages in Control Hub , but the values that you set apply to all environments. |
| Note | If you have the Hybrid Calendar set up for multiple calendar environments, you can access the keywords settings from multiple pages in Control Hub , but the values that you set apply to all environments. |
| Step 4 | Select the tenant to configure. |
| Step 5 | Click the Settings tab. |
| Step 6 | In the Keywords section, select the default action that you want for each keyword. |
| Step 7 | Click Save . |

| Note | If you have the Hybrid Calendar set up for multiple calendar environments, you can access the keywords settings from multiple pages in Control Hub , but the values that you set apply to all environments. |
|---|---|

| Step 1 | Sign in to the customer view of https://admin.webex.com/login . |
|---|---|
| Step 2 | In the left-hand navigation pane, under Services click Meeting . |
| Step 3 | Locate the Customize Meeting Join Details section. |
| Step 4 | Choose whether to show Join by Phone details. When you include the dial-in details, you can also choose to
                                          add a link to global call-in numbers, a link to toll-free calling
                                          restrictions, or both. |
| Step 5 | Show or hide details on joining from an application or video conferencing device. When you include the video dialing details, you can also
                                          choose to include an IVR IP address, a Skype for Business join link, or
                                          both. |
| Step 6 | Click Add a Language and then select the language from the drop-down menu to create a custom header and footer for any of the languages that the
                                       Hybrid Calendar supports. When you've got the header and footer text that you want, click Save . The header and footer values have a maximum of 1024 characters each (including spaces). |
| Step 7 | Once you've added a custom header and footer for a language, you can choose that language as a default for any other language
                                       that doesn't have a custom header and footer defined. Your default language choice saves automatically. |

| Step 1 | Sign in to the customer view in https://admin.webex.com . |
|---|---|
| Step 2 | In the left-hand navigation pane, under Management click Users and then choose a specific user from the list. You can use the search function to narrow down the list of users. |
| Step 3 | Click the row to open an overview of the user. |
| Step 4 | Choose one and then save your changes: In a new environment, click Calendar Service , toggle on Calendar , and ensure that the Google Calendar is selected. In an existing environment with Exchange, click Calendar Service , and under calendar type, ensure that the Google Calendar is selected. After you activate the service, the Webex App user status changes from Pending Activation to Activated. The length of time for this change depends on the number of users
                                          that you're enabling for the service. Users receive an email that indicates the feature is enabled. See the documentation below if you want to disable email notifications. |

| Step 1 | Sign in to the customer view of https://admin.webex.com/login . |
|---|---|
| Step 2 | In the left-hand navigation pane, under Management click Workspaces . |
| Step 3 | Go to Scheduling and select Calendar so that users can use One Button to Push (OBTP) on their devices. |
| Step 4 | Select the calendar provider. |
| Step 5 | Enter or paste the Google resource email address from G Suite (Calendar > Resources). This is the email address that will be used to schedule meetings. |
| Step 6 | Click Save . |

| Step 1 | Sign in to the customer view in https://admin.webex.com . |
|---|---|
| Step 2 | In the left-hand navigation pane, under Management click Users . |
| Step 3 | Click Manage Users . |
| Step 4 | See this article for the detailed CSV import/export procedure. |
| Step 5 | Use a CSV editor to change the preferredWebExSite attribute for all or some users. |
| Step 6 | Import the CSV file. |

| Step 1 | Sign in to https://calendar.google.com with one of the test Google user accounts enabled for Hybrid Calendar . |
|---|---|
| Step 2 | Click Create to start an event, and then add a space scheduling keyword (such as @webex:space or @meet) to the Where field. Fill out other meeting information, as needed, and then click Save . |
| Step 3 | Open https://teams.webex.com , and sign in with the test user account. |
| Step 4 | Verify whether a new Webex space was created and contains the calendar invite card. |
| Step 5 | To test out-of-office status, in https://calendar.google.com , navigate to Settings and turn on Vacation responder . Within 20 minutes, you should see the test account's profile picture display an out-of-office overlay in Webex Teams, like
                                       this: Note The display picture update is triggered when others see your presence in a space. If the test user does not interact with
                                                      other active users, you may need to use another account to verify the update. | Note | The display picture update is triggered when others see your presence in a space. If the test user does not interact with
                                                      other active users, you may need to use another account to verify the update. |
| Note | The display picture update is triggered when others see your presence in a space. If the test user does not interact with
                                                      other active users, you may need to use another account to verify the update. |
| Step 6 | To test the join button with a Webex room or desk device or Webex Board: In https://calendar.google.com , click Create to start an event, and then add a scheduling keyword (such as @webex) to the Location field. Click Rooms , and choose the device you want to add. Fill out other meeting information, as needed, and then click Save . When the meeting is scheduled to begin, verify that the Join button appears on the device. |

| Note | The display picture update is triggered when others see your presence in a space. If the test user does not interact with
                                                      other active users, you may need to use another account to verify the update. |
|---|---|