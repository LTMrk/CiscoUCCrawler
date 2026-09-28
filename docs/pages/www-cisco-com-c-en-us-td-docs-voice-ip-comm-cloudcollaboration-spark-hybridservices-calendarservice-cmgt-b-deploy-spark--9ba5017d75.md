---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-spark-hybridservices-calendarservice-cmgt-b-deploy-spark--9ba5017d75
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/spark/hybridservices/calendarservice/cmgt_b_deploy-spark-hybrid-calendar-service/cmgt_b_deploy-spark-hybrid-calendar-service_chapter_01000.html
retrieved_at: 2026-08-20T23:53:57.939785+00:00
---

Deployment guide for Hybrid Calendar

# Deployment guide for Hybrid Calendar

Updated: October 17, 2023

Chapter: Prepare Your Environment

## Chapter: Prepare Your Environment

- Prepare Your Environment

- Requirements for Hybrid Calendar with Google Calendar

- Remove Google Hangouts information in meeting events

# Prepare Your Environment

## Requirements for Hybrid Calendar with Google Calendar

A Webex organization with one of the offers documented for the Hybrid Calendar in License requirements for Hybrid Services .

We do not currently support deploying both Google Calendar and Office 365 with the cloud-based Hybrid Calendar in the same Webex organization.

A Google G Suite organization (formerly Google Apps for Work) with Google accounts for all users in your Webex organization:

Each user in your Webex organization can only have one email address associated with only one Hybrid Calendar integration.
                                                In other words, the Hybrid Calendar will only process meetings from a single address for creating spaces, decorating meetings,
                                                showing the meetings list and join button, and sending the join button to video devices.

For Webex Teams scheduling:

Each user's Google account email address must match their Webex App login address.

For Cisco Webex Personal Room scheduling with a Webex Meetings site:

You must enable the Personal Room feature for the Webex site and for the individual users .

The Google account email address should also match the user's Webex account address. If it does not, users must associate their Webex Personal Room with Webex Teams in the app in order to use @webex.

To provide the meetings list and the join button on room resources:

During setup, you need an administrator account which has permissions to manage access control lists on meeting room resources.

In addition, you must verify the domain of the email address of this account .

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

## Remove Google Hangouts information in meeting events

In your G Suite Calendar settings, consider removing the video calls that are automatically added to events. This step ensures
                              that meeting events contain just Webex join links when your users send them out.

This step prevents Google Calendar from including video event details in the meeting invitation that would conflict with the
                                          join details that the Hybrid Calendar Service adds. Suppressing this information does not disable Google Hangouts for your
                                          organization.

Step 1

From https://admin.google.com , go to > Apps > G Suite > Calendar .

Step 2

Click Sharing settings .

Step 3

Under Video Calls, uncheck Automatically add video calls to events created by a user .

| Note | We do not currently support deploying both Google Calendar and Office 365 with the cloud-based Hybrid Calendar in the same Webex organization. |
|---|---|

| Note | Each user in your Webex organization can only have one email address associated with only one Hybrid Calendar integration.
                                                In other words, the Hybrid Calendar will only process meetings from a single address for creating spaces, decorating meetings,
                                                showing the meetings list and join button, and sending the join button to video devices. |
|---|---|

| Note | This step prevents Google Calendar from including video event details in the meeting invitation that would conflict with the
                                          join details that the Hybrid Calendar Service adds. Suppressing this information does not disable Google Hangouts for your
                                          organization. |
|---|---|

| Step 1 | From https://admin.google.com , go to > Apps > G Suite > Calendar . |
|---|---|
| Step 2 | Click Sharing settings . |
| Step 3 | Under Video Calls, uncheck Automatically add video calls to events created by a user . |