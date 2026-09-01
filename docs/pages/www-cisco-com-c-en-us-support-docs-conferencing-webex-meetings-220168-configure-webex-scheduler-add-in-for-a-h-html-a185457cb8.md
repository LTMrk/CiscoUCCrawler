---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-webex-meetings-220168-configure-webex-scheduler-add-in-for-a-h-html-a185457cb8
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/webex-meetings/220168-configure-webex-scheduler-add-in-for-a-h.html
retrieved_at: 2026-09-01T14:56:16.362119+00:00
---

Configure Webex Scheduler Add-in for a Hybrid Environment

# Configure Webex Scheduler Add-in for a Hybrid Environment

### Download Options

Updated: January 30, 2023

Document ID: 220168

Contents

## Contents

## Introduction

This document describes how to deploy and configure Webex Scheduler Add-in for Outlook in a Hybrid environment.

## Background

Previously, Webex Scheduler could only be used in either an On-Prem Exchange environment or a Microsoft 365 (M365) environment but could not be configured for both (Hybrid) at the same time. Now, Webex Scheduler has been enhanced so that the add-in automatically checks if a user is configured for M365, and if they are not the add-in falls back to use the scheduler in on-prem mode.

## Prerequisites

- Environment where both On Prem Exchange and M365 are deployed to users or currently in a migration from On Prem Exchange to M365

- Webex Meetings site to configure options for Webex Scheduler

- Admin/Global Admin Accounts for Exchange, M365, and Webex Meetings site

Once the prerequisites are met, deployment and configuration for Webex Scheduler in a hybrid environment can be done in 2 steps.

Step 1. Deploy Webex Scheduler to M365 and on prem exchange.

Step 2. Configure Webex Meetings site with options related to Webex Scheduler.

## Step 1. Deploy Webex Scheduler Add-in to Both M365 and On Prem Exchange

Note : Cisco Webex Scheduler requires specific domains to be allowed in order to function properly. Please refer to the Prepare your environment document for the domains that need to be allowed and add these exceptions to your proxy and/or firewall configurations

### Deploy to M365

Deploy Webex Scheduler to M365 can be done either through Microsoft Appsource or through a Manifest file within the M365 Admin Center. To deploy either method, navigate to Settings > Integrated apps .

#### Deploy with Appsource

- Click on Get Apps in the Integrated Apps section to bring up Appsource

- Search for Cisco Webex Scheduler

- Click Get it now

- Appsource redirects you back to the admin center to finish setup

#### Deploy with Manifest File

- Navigate to the Webex Scheduler manifest file . C opy the link or Right Click > Save As XML for use in the next step

- Navigate back to the Integrated apps section of the M365 Admin Center and click on Upload custom apps in the Integrated apps section

- Choose either Upload manifest file (.xml) from device or Provide link to manifest file based on your preference from earlier

- Review instructions to finish deployment of app within the M365 Admin Center

Note : Cisco Webex Scheduler does require permissions before installation. Review the Microsoft 365 Permissions Requested by Webex to see the permissions requested and the reason behind it.

Note : For more information about deployment options and settings when you deploy through the M365 Admin Center, refer to Deploy add-ins in the Microsoft 365 admin center .

### Deploy to On Prem Exchange

To deploy the Webex Scheduler to On Prem Exchange, review Add-ins for Outlook in Exchange Server . This document includes a link to the manifest file used in the deployment process.

Note : For more information about the deployment process with On Prem Exchange with additional settings and more, refer to Microsoft documentation here .

## Step 2. Configure Webex Meetings Site with Options Related to Webex Scheduler

Webex Meeting Sites can be managed with either Control Hub or Site Admin. Based upon on how your site is managed, you can navigate to the configuration page in multiple ways.

### Site Admin Sites

Log in to your Webex Meeting site admin page, then Navigate to Configuration > Common Site Settings > Options . Scroll to the section Third-Party Integration and go to the section Microsoft (Microsoft 365 and Microsoft Teams)

### Control Hub Sites

Log into Control Hub, then Navigate to Services > Meeting > Select your Meeting site > Click the Settings tab > Click on Site Options > Scroll down to Third-Party Integration and go to the sections Microsoft (Microsoft 365 and Microsoft Teams) and Microsoft 365 Tenant

Once in the correct area, a screen is shown like this:

M365 Settings for Webex Meeting SItes

Here are the detailed settings explanation:

- Allow users to sign into Webex Meetings with their Microsoft 365 accounts - This configuration option allows end users to sign into Webex Meetings with their M365 accounts

- Allow individual users to add the calendar integration for their upcoming meetings list in Modern View (Microsoft 365 only) - This configuration gives users the ability to manually link and unlink their Webex Meetings account with their Microsoft 365 Account Under Preferences > General > Calendar integration

- List Microsoft 365 calendar events on the Webex site when authorized by tenant administrator (Microsoft 365 only) - When a site is configured and linked to a Microsoft Tenant, future meetings on an end users Outlook calendar that normally would not be displayed on the Upcoming Meetings section of their Webex site is now displayed

- Automatically link users with this Webex site if their Webex account email address matches their Microsoft 365 email address - When a site is configured and linked to a Microsoft Tenant, this option automatically links the users Webex Meetings account with their M365 account on the backend, so the user is not prompted with a screen to manually link the two accounts when they log in to the Webex Scheduler Add-in for the first time.

- Microsoft 365 tenant - This area is used to authorize Webex Meetings to connect to a Microsoft Tenant and enables features such as automatic meeting updates and meeting sync between Webex and Outlook

- Enable Microsoft Outlook integration while disallowing Webex Meetings from accessing Microsoft 365 account information - This option breaks the connection between Webex Scheduler and M365 and is mainly used in on prem exchange environments only where there is no M365 setup at all.

### Recommend Site Settings

#### For M365 Users

- Add New Authorization under Microsoft 365 Tenant - This is recommended to configure and enable with an Admin and a Global Admin account on both the Webex and M365 Tenant side so that full functionality can take place for M365 users, with features that include meeting sync for non-Webex meetings and automatic updates of a Webex Meeting when changes are made in Outlook

- Automatically link users with this Webex site if their Webex account email address matches their Microsoft 365 email address - This is recommended to enable so users are not prompted with another window during initial log in to the scheduler that asks to manually link their M365 and Webex Meeting accounts, otherwise with this enabled the accounts are automatically linked as long as the email address for both services are the same.

#### For on Prem Exchange Users

For hybrid environments, no other configuration options are needed on the Webex Meetings site other than what has been mentioned previously for M365 users. This is because the scheduler add-in automatically detects if a user is M365 or on prem exchange and adjust accordingly, however, to have similar functionality like M365 where meetings are synced and automatic meeting updates when changes are made in Outlook it is recommended to also configure Hybrid Calendar for Exchange. For more information, refer to Deployment Guide for Hybrid Calendar .

## Verify

After deployment of the add-in is complete and the site has been configured, you can verify and test with accounts on M365 and on prem in your environment to make sure that the setup runs as it should. If any issues come up, please contact Cisco TAC.

## Related Information

- Known issues and limitations for Webex Scheduler for Microsoft Outlook

- Cisco Technical Support & Downloads

### Revision History

2.0

30-Jan-2023

Initial Release

1.0

27-Jan-2023

Initial Release

### Contributed by Cisco Engineers

Andy Hoy

Cisco Technical Consulting Engineer

### This Document Applies to These Products

- WebEx Meetings

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 30-Jan-2023 | Initial Release |
| 1.0 | 27-Jan-2023 | Initial Release |