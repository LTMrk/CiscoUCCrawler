---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-control-hub-222559-enable-1080p-video-resolution-for-webex-html-d08a922daf
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-control-hub/222559-enable-1080p-video-resolution-for-webex.html
retrieved_at: 2026-08-21T06:29:42.714107+00:00
---

Enable 1080p Video Resolution for Webex App

# Enable 1080p Video Resolution for Webex App

### Download Options

Updated: May 9, 2025

Document ID: 222559

Contents

## Contents

## Introduction

This document describes how to enable and utilize 1080p video resolution for Webex App users.

## Prerequisites

### Requirements

It is recommended that you have some familiarity with these topics:

- Control Hub Platform

- Webex App

### Components Used

The software listed here has been used to make the tests and produce the results described in this document:

- Control Hub Organization, on Webex Suite

- Webex App on version 44.10

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Scenario and Feature Clarification

Webex is a platform that offers many video and audio options that can be used by the products that exist under its "umbrella".  This article focuses on 1080p video resolution for users using the Webex App. It explains what the caveats are and the options that users and admins have. A comparison is made between the settings for 360p, 720p, and 1080p, but only from an administration perspective. Video resolution results are not compared or analyzed in this article.

The assumed scenario is that a Control Hub full administrator wishes to enable 1080p video resolution for the users within a Control Hub Organization.

## 360p and 720p Video Resolution

As an administrator, you are advised to initially read through the article describing how to enable high-quality (360p) video and high-definition quality(720p) video that can be found here: Enable High-Quality or High-Definition Video for a Cisco Webex Site in Cisco Webex Control Hub . In addition, the Video Webex Support article describes the different resolutions available for Webex App users, the minimum requirements for each, and the features that are supported by each video resolution.

Based on the information in these articles, the Video resolution settings can be seen under this section in Control Hub:

Video and Recordings Settings under Meetings Section in Control Hub

You have the option to enable and disable these settings individually for each site in your Organization. Apart from setting the video resolution on site level, you have the option to set it up on user level too.

To do so:

1. Log in to Control Hub as a full administrator and navigate to Users under Management section.

2. Select a user from the list of users in your Organization and navigate to Meetings .

3. Scroll down to Video section. From this section, you can enable/disable video resolution options available for the specific user selected, as seen in the picture:

Video Resolution Settings for Individual User in Control Hub

Note : When the administrator navigates to the video resolution settings for individual users in Control Hub, they toggle to enable 360p and 720p and videos are seen twice in two separate columns. One column represents the internal and the other the external meeting settings for video resolution that can be set separately per user.

## How to Enable 1080p for Webex Users

If you would like to enable 1080p for the users of your Organization, you need to contact your Customer Success Manager (CSM) or TAC (if a CSM is not available for your account) and address your request. You do not have the option to enable 1080p as a Control Hub full administrator. This feature can only be enabled from the backend and involving your CSM or TAC is necessary.

If you open a ticket with TAC, the engineer assigned to your case is going to reach out to the backend provisioning team and ask for the enablement. There is a chance that you need to wait for some days for the feature to be completed.

Warning : If you have a Control Hub organization that has multiple Webex sites, your request to enable 1080p is going to enable this feature for all the sites under your organization by default. If you obtain a new Webex site in the future, that site is going to be enabled for 1080p too. If you would like to have 1080p only for one of the sites in your organization, you must clearly address it in the case opened with TAC.

Once the feature has been provisioned, the TAC engineer assigned to your case notifies you that the new feature is ready for testing.

## User Experience after Enabling 1080p

After enabling 1080p, the users do not notice any changes. The users in your Organization need to log out, then log back in to their Webex App. Once they have successfully logged back in, the users need to click their User Avatar on the top left corner of the Webex App and navigate to Settings . Then, select Video and click the drop-down menu next to Camera resolution under the Camera section.

Camera Resolution Settings in Webex App

Under this menu, users can see all the available video resolution options for their user account. Each user can enable 1080p individually from this menu. If a user chooses 720p or 360p instead, 1080p is not going to be used even though the 1080p feature is enabled for your Organization.

## Administrator Experience after Enabling 1080p

Once 1080p is enabled, Control Hub administrators are not going to be able to see the 1080p option under the Video and recordings section of the Common Settings of their Webex sites. This section is going to be as seen in the picture:

Video and Recordings Settings under Meetings Section in Control Hub

The option to enable/disable 1080p is not present for any of the Webex sites under your Organization. In addition, administrators are going to notice that when selecting an individual user and trying to change the video resolution options for each user, only affect 360p and 720p are affected. There is no option to enable or disable 1080p at the user level from Control Hub:

Video Resolution Settings for Individual User in Control Hub

Both behaviors seen in Control Hub are expected and are by design. The backend engineering can enable 1080p for your Organization and the Webex sites in it, but this feature can not be managed by the Control Hub administrator at the time of writing this article. The 1080p feature is going to be available to all users for all your sites. This feature can only be controlled by each individual user, who can enable/disable it on his/her own from the Webex App settings. Administrators can not control this behavior, so only users can enable 1080p for each user or each site.

## Users Do Not See the 1080p Resolution in Webex App

In cases where the users of your Organization do not see the option of 1080p video resolution under the video settings of their Webex App, there are some basic troubleshooting steps that you must do:

- Make sure that the affected users are on the latest Webex App version. If not, then ask the users to update their App and test again.

- Ask the users to log out of the Webex App. then log in again. This step is necessary. Once 1080p is enabled for the users of an Organization, the changes are not automatically propagated to the users. For the change to be available, users need to do a fresh log in on their Webex App.

- Completely delete the Webex App from the user PC and re-install it.

If the issue persists, you must contact TAC to further troubleshoot the issue. Ensure that you clarify which users are affected and which Webex site they use. Report to TAC the approximate date the1080p feature was enabled. In addition, clarify whether a new Webex site has been added to your Organization in Control Hub and if the users affected are using this new site. This information helps TAC engineers and expedites the investigation.

From a logs perspective, when contacting TAC for an issue related to resolution you need to provide:

- Logs from the Webex App as described in this video .

- A screenshot of the Video resolution options under your Webex App settings, showing the available resolutions for your client.

## Related Information

- Enable High-Quality or High-Definition Video for a Cisco Webex Site in Cisco Webex Control Hub

- Webex Video Support

- Webex - How to Collect Webex Desktop Client Logs Locally

### Revision History

2.0

09-May-2025

Updated Formatting.

1.0

04-Nov-2024

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 09-May-2025 | Updated Formatting. |
| 1.0 | 04-Nov-2024 | Initial Release |