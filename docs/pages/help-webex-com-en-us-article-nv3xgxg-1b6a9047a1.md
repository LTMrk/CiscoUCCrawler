---
doc_id: help-webex-com-en-us-article-nv3xgxg-1b6a9047a1
source_url: https://help.webex.com/en-us/article/nv3xgxg
retrieved_at: 2026-09-07T12:43:30.216500+00:00
---

## Directory Sync Overview

Directory sync ensures that Webex for Cisco BroadWorks users can use the Webex directory from the Webex App to call any calling entity from the BroadWorks server. This feature syncs BroadWorks calling information that was not a part of user provisioning to the Webex directory.

Webex for Cisco BroadWorks user provisioning updates the Webex directory with calling details for Webex for Cisco BroadWorks users (primary phone number, mobile phone number, extension), but omits external calling records. However, when Directory sync is on, the feature also syncs the following calling records to the Webex directory.

BroadWorks-only calling users (who are not onboarded to Webex)

Non-user calling entities (e.g., a conference room phone, fax machine, hunt group number)

BroadWorks Phone List entries

The following table summarizes BroadWorks calling records and shows how they get added to the Webex directory.

BroadWorks Calling Records

Description

Added to Webex Directory via...

Webex for Cisco BroadWorks users

Users are enabled for Webex for Cisco BroadWorks

User provisioning (e.g, flowthrough provisioning)

BroadWorks-only calling users

Calling users who are not onboarded to Webex

Directory sync

Non-user calling entities

E.g., a conference room phone, fax machine, Hunt group number

Directory sync

BroadWorks phone lists

BroadWorks phone list entries:

Enterprise Common Phone Lists

Group Common Phone Lists (Service Provider Groups or Enterprise Groups)

Personal Phone Lists

Directory sync (phone list sync)

For more details on user provisioning, see the Webex for Cisco BroadWorks Solution Guide .

### Directory Sync Conditions

Partner administrators must enable the feature at the partner level. Partner administrators can turn the feature on or off for multiple customer organizations in a single operation.

By default, the initial sync occurs one week following the enabling of the sync (the time chosen to start the sync is random). However, customer organizations can use the Sync Now option to bypass the one week waiting period and trigger an immediate sync for a given customer organization.

By default, directory Sync runs weekly for each customer. Each sync occurs one week following the last sync, regardless of whether the last sync was scheduled or triggered manually with Sync Now .

The maximum number of simultaneous syncs per BroadWorks cluster is two: one scheduled sync and one on-demand sync (via API or Partner Hub GUI). However, administrators can’t run two on-demand syncs at the same time from the same BroadWorks. This restriction exists irrespective of whether the sync was initiated via the API or via the Sync Now option in Partner Hub. In addition, Webex won’t schedule two scheduled syncs to run at the same time from the same BroadWorks.

If a sync failure occurs, Webex reattempts the sync automatically every 24 hours until the next scheduled sync.

The sync ignores users who don’t have a phone number.

In Partner Hub, you can view sync status information for a given customer. In addition, you can export detailed information on the last sync to a CSV record. The CSV record provides more detail than the Control Hub display and can help in troubleshooting, analytics, and auditing.

Webex stores user contacts in an encrypted format. Only the user who owns the contact has access to the decryption key.

For BroadWorks-only calling users and non-user calling entities, this feature syncs the following phone number types from BroadWorks:

Primary Phone Number

Mobile Phone Number

Extension

However, sync excludes BroadWorks-only calling users and non-user calling entities from the sync if neither a primary phone number or extension is present.

BroadWorks user-level privacy service setting is not supported as part of directory sync.

### BroadWorks Phone List and Contact Maximums

Directory sync also syncs BroadWorks phone list entries to Webex Contacts. Synced entries get added to one of the following contact types:

Organization Contacts—Webex stores these contacts against an organization. Each user can access the organization contacts for their organization. The maximum is up to 30000 contacts.

User Contacts—Webex stores these contacts against a user. Only the user who owns the contact can access the contact entry. The maximum is up to 2000 contacts (1500 synced contacts + 500 manual entry contacts).

Only Phone List entries get added to Webex Contacts. BroadWorks-only calling users and non-user calling entities that are included in Directory sync do not get added to Contacts unless a Webex user adds them to Contacts manually.

The following table maps Webex contact types against the contact source (synced from a BroadWorks phone list or added manually):

Webex Contact Type

Contact Source

Maximum

Synced from BroadWorks...

API used for sync

Organization contacts

Directory sync

30000 contacts

Enterprise Common Phone Lists

/directories/enterprisecommon

Group Common Phone Lists (for a Service Provider group)**

/directories/groupcommon

User contacts

Directory sync

1500 contacts

Personal Phone Lists

Added manually by user

500 contacts

N/A

N/A

Group contacts

Directory sync

30000 contacts per group

Group Common Phone Lists (for an Enterprise group)**

**Group Common Phone Lists entries sync differently depending on whether BroadWorks is in Enterprise Mode or Service Provider mode. The value of the isBroadWorksEnterprise parameter (true or false) determines how the list syncs:

True—Sync as group contact

False—Sync as organization contact

The following conditions apply around how Directory Sync handles contact maximums:

If an organization exceeds the maximum allowed contacts for the sync (30000 organization contacts or 30000 Group common contacts per group), directory sync excludes entries above the maximum threshold. There’s no particular order applied to synced or omitted contacts.

If one of your customers exceeds the maximum allowed number of contacts in either category, we recommend that you raise a case with Cisco to have that organization excluded from directory sync.

Manual contacts are contacts that a user adds manually on the Webex App. A user can add up to 500 manual contacts. Manual contacts fall within the larger User contact category on Webex, but aren’t included in the sync.

The overall combined limit for organization contacts (30000) and group contacts (30000 per group) is 200000.

### Updates

Following is how the Webex directory handles updates:

If the contact name changes on BroadWorks, the existing contact gets deleted from the Webex directory and a new contact is created.

If the contact number changes on BroadWorks, Webex updates the existing contact in the Webex directory with the new number.

After an admin updates a contact on BroadWorks, the following conditions outline when the update displays in a user's Webex App:

If the update is to a BroadWorks-only calling user or a non-user calling entity, the update displays in a user’s Webex App immediately following the subsequent directory sync.

If the update is to a BroadWorks phone list entry:

For user contacts—Updates display in the user’s Webex App immediately following the subsequent directory sync.

For group contacts - Updates display in the users Webex App immediately following the subsequent directory sync.

For organization contacts—The Webex directory gets updated at the subsequent directory sync, but users won’t see the change in the Webex App until they restart the Webex App or until the local 72-hour cache timer expires.

Updates to Webex for Cisco BroadWorks user information get handled as a part of provisioning processes.

Control Hub contains an option to add or edit organization-level contacts in Control Hub via a CSV file. Partner administrators and customer administrators with Control Hub access can access this option. However, updating contacts via Control Hub is not supported by Webex for Cisco BroadWorks. Contact updates applied in Control Hub don’t sync back to BroadWorks and are unavailable to directory searches from desk phones.

## Directory Sync Prerequisites

We recommend that you use the following settings:

The below examples assume that you are using an XSP server. For ADP servers, replace (XSP_CLI) with (ADP_CLI).

Rate Limiting Values—Set the following OverloadControl system properties (XSP_CLI/Applications/Xsi-Actions/OverloadControl):

userDirectoryTransactionLimit—Set to a null value.

globalDirectoryTransactionLimit—Set to a null value.

It's recommended that you set userDirectoryTransactionLimit and globalDirectoryTransactionLimit to a null value. However, if you do decide to assign values, each must be set to at least five times the value of transactionLimitPeriodSeconds (which should be 1).

Transaction Limits—Set the following values (XSP_CLI/System/CommunicationUtility/DefaultSettings):

userTransactionLimit—Set to at least 100.

transactionLimitPeriodSecs—Set to 1.

Paging Values—Set the Paging system properties (XSP_CLI/Applications/Xsi-Actions/Paging):

defaultPageSize—Set to 50

availableUserMaxLimit—Set to 100

CTI Interface—Make sure to upload that Webex CA certificates to the CTI interface trust store and to enable client authentication on the CTI interface.

In addition, depending on your BroadWorks release, we recommend that you apply the following system patches to BroadWorks deployment before you enable this feature:

For R22: AP.as.22.0.1123.ap368517

For R23: AP.as.23.0.1075.ap368517

For R24: no patch required

For the full list of patch requirements that form the minimum requirement for Webex for Cisco BroadWorks, see BroadWorks Software Requirements in the Solution Guide for Webex for Cisco BroadWorks .

## Enable Directory Sync (New Template)

Partner administrators can enable Directory Sync for a customer template while creating the new template. Any new customer organizations that get assigned to that template will have directory sync enabled. For details, see "Configure your Onboarding templates" in Configure Your Partner Organization in Partner Hub within the Solution Guide for Webex for Cisco BroadWorks .

### What to do Next

Make sure that your users know that they must click the Contacts tab on the Webex App at least once in order to turn on the feature on the Webex App. This needs to be completed once only.

## Enable Directory Sync (Existing Template)

Sign in to Partner Hub and choose Customers .

In the Onboarding Templates , select the Customer.

Click on the Service settings , in the Preference section enable Directory Sync.

To enable directory sync by default for new customer organziations that use this template:

Set the Enable BroadWorks Directory & Phone List Sync for all new customer organizations toggle to On .

Click Save .

To enable directory sync for existing customer organizations that use this template:

Click Show list of customers sync status .

Check the adjacent check boxes for each organization for which you want to turn the feature on.

Click Enable Sync .

If you want to disable directory sync, follow the above procedure and:

In step 4a, set the Enable phone directory sync for all new customer organizations toggle to Off to disable directory sync by default for new customer organizations that use this template.

In step 5c, click Disable Sync to turn the feature off for existing organizations.

What to do next

Make sure that your users know that they must click the Contacts tab on the Webex App at least once in order to turn on the feature on the Webex App. This needs to be completed once only.

## Trigger Immediate Sync

Sign in to Partner Hub ( http://admin.webex.com ) and choose Settings .

Scroll to BroadWorks Calling and click View Templates .

Select the appropriate customer template and scroll to BroadWorks Directory Sync .

Click Show list of customers sync status .

For the customer organization that you want to sync, click the three dots on the far right and select Sync Now .

Click Refresh to see the sync results.

## Export Sync Records to CSV

Sign in to Partner Hub ( http://admin.webex.com ) and choose Settings .

Scroll to BroadWorks Calling and click View Templates .

Select the appropriate customer template and scroll to BroadWorks Directory Sync .

Click Show list of customers sync status .

Check the adjacent check boxes for each organization that you want to include in the export.

Click Export results .

## Public APIs for Directory Sync

Public APIs are available on developer.webex.com that allow partner administrators to update Directory Sync settings for the customer organizations that they manage, to trigger an immediate sync, or obtain sync status information. The directory sync methods are grouped under BroadWorks Enterprises :

List BroadWorks Enterprises —Use this API method to obtain a list of enterprises under a given Service Provider and each enterprise's id . You must enter the spEnterpriseId as assigned in provisioning.

Update Directory Sync for a BroadWorks Enterprise —Enter the enterprise id to update the directory syc status for that enterprise, enabling or disabling directory sync.

Trigger Directory Sync for an Enterprise —Use this API method if you want to trigger an immediate sync for a given enterprise id . For the syncStatus , enter the SYNC_NOW command.

Get Directory Sync Status for an Enterprise —Enter the enterprise id and run in order to get a status and trackingId of the latest sync. You can use the trackingID to run additional analytics via tools such as Kibana and Grafana.

In addition, administrators can use the Trigger Directory Sync for a Single User API to trigger an on-demand directory sync for a single user.

For detailed API documentation, see https://developer.webex.com/docs/api/guides/webex-for-broadworks-developers-guide .

You need to sign in to read the API specification at https://developer.webex.com/docs/api/v1/broadworks-subscribers .

## Sync Multiple Enterprises with API

Directory sync lets you sync only a single enterprise from a Broadworks cluster at a time via an on-demand sync. If you attempt to sync more than one enterprise, you will receive a 429 error

The time that it takes to trigger a sync for a single enterprise varies depending on the size of the enterprise.

Run the List BroadWorks Enterprises API to generate a list of enterprises that you want to sync.

Set startWith to the starting string of the enterprise or service provider identifier.

Click Run .

Run the Trigger Directory Sync for an Enterprise API on the first enterprise in the list.

Enter the enterprise id .

Set syncStatus to SYNC_NOW

Click Run .

An immediate sync gets triggered for the enterprise. This sync counts against the single on-demand sync per Broadworks limit.

Wait for a few seconds and then run the Get Directory Sync Status API to get sync status.

Enter the enterprise id

Click Run .

After the sync finishes, complete steps 2 to 4 on the next enterprise in the list. Repeat these steps until you have synced the entire list.

## Error Codes for Directory Sync

The following error codes apply to Directory Sync.

Error Code

Error Message

600000

Broadworks External Directory User Sync unexpected error.

600001

Broadworks External Directory User Sync failed.

600002

Broadworks External Directory User Sync had to be terminated before completion.

600003

Broadworks External Directory User Sync only partially succeeded. Some Customer Organizations failed to sync.

600004

Broadworks External Directory User Sync is not enabled for the ConfigSet.

600005

Broadworks External Directory User Sync is in-progress for the ConfigSet.

600006

Broadworks External Directory User Sync threads are busy or shutting down, hence will not accept more sync request, try again later.

600007

The Identity Org of the CustomerConfig is not found.

600008

The CustomerConfig is not found in the partner org.

600009

Broadworks External Directory User Sync cannot be run as the broadworks cluster associated to the CustomerConfig is busy

600010

Broadworks External Directory User Sync cannot be run as there is no broadworks cluster associated to the CustomerConfig.

600011

Broadworks External Directory User Sync is not enabled for the CustomerConfig.

600012

Broadworks External Directory User Sync cannot be run as the Hybrid Directory sync is already enabled for the CustomerConfig.

600013

Broadworks External Directory User Sync failed to add users and machine accounts to identity store.

600014

Broadworks External Directory User Sync failed while trying to connect to Broadworks cluster. Error from Broadworks - %s.

600015

Broadworks External Directory User Sync didn't find any matching user in identity store.

600017

BroadWorks Phone List Sync failed to sync all user and enterprise/organization contacts.

600018

BroadWorks Phone List Sync failed for users in the enterprise/organization.

600019

BroadWorks Phone List Sync failed to sync enterprise/organization contacts.

600020

BroadWorks External Directory User Sync cannot be disabled as the CustomerConfig sync is in progress.

600022

BroadWorks External Directory Single User Sync is not possible since the enterprise has no provisioned user.

600023

BroadWorks External Directory Single User Sync is not possible because the user already exists in this organization.

600024

BroadWorks External Directory Single User Sync is not possible because no matching user was found in BroadWorks.

600025

BroadWorks External Directory User Sync failed to update the user account in CI.

600026

BroadWorks External Directory User Sync failed to update the machine account in CI.

600027

BroadWorks External Directory Single User Sync is not possible because multiple users were found in BroadWorks.

600028

BroadWorks External Directory Single User Sync is not possible because at least one enterprise directory sync should have been completed.

600029

BroadWorks External Directory User Sync failed since the enterprise has no provisioned user.

## Change History

The following table summarizes updates to this article.

Date

Revision

February 14, 2023

Updated Directory Sync Maximums and Source section.

December 10, 2022

Updated the term Complete Immediate Sync to Trigger Directory Sync

July 19, 2022

Clarifications and corrections to overview information:

Updated Directory Sync Overview to clarify the different syncs involved and how the Webex directory gets updated for each.

Updated BroadWorks Phone List and Contact Maximums to clarify that only phone lists get synced to Contacts.

Corrections to Updates to clarify how long it takes for the Webex App to display updated records.

May 09, 2022

In Directory Sync Overview , corrected Note under the Directory Sync Maximums and Source table. Also updated Note on flowthrough provisioning.

Grammatical edits and fixes

April 07, 2022

Added Note to the Updates section in Directory Sync Overview around limitation of applying organization-level contact edits in Control Hub.

March 28, 2022

Reinserted missing content under Enable Directory Sync (New Template) .

Added information on sync maximums. You can run one scheduled sync and one API sync simultaneously from the same cluster.

Added information on Trigger Directory Sync for a single user API.

March 24, 2022

Added list of synced phone number types to Directory Sync Conditions . The sync now includes mobile phone numbers.

March 16, 2022

Added new error codes.

Added introductory description statement for better usability from web searches.

December 17, 2021

Minor structural edits to fix issue with missing TOC.

December 16, 2021

Updated article with increased maximum values for User contacts.

December 08, 2021

Added section Directory Sync and Contact Maximums to clarify how Directory Sync derives the maximum number of Organization and User contacts.

Revised table formatting in Error Codes for Directory Sync for better readability.

| BroadWorks Calling Records | Description | Added to Webex Directory via... |
|---|---|---|
| Webex for Cisco BroadWorks users | Users are enabled for Webex for Cisco BroadWorks | User provisioning (e.g, flowthrough provisioning) |
| BroadWorks-only calling users | Calling users who are not onboarded to Webex | Directory sync |
| Non-user calling entities | E.g., a conference room phone, fax machine, Hunt group number | Directory sync |
| BroadWorks phone lists | BroadWorks phone list entries: Enterprise Common Phone Lists Group Common Phone Lists (Service Provider Groups or Enterprise Groups) Personal Phone Lists | Directory sync (phone list sync) |

| Webex Contact Type | Contact Source | Maximum | Synced from BroadWorks... | API used for sync |
|---|---|---|---|---|
| Organization contacts | Directory sync | 30000 contacts | Enterprise Common Phone Lists | /directories/enterprisecommon |
| Group Common Phone Lists (for a Service Provider group)** | /directories/groupcommon |
| User contacts | Directory sync | 1500 contacts | Personal Phone Lists | /directories/personal |
| Added manually by user | 500 contacts | N/A | N/A |
| Group contacts | Directory sync | 30000 contacts per group | Group Common Phone Lists (for an Enterprise group)** | /directories/groupcommon |

| 1 | Sign in to Partner Hub and choose Customers . |
|---|---|
| 2 | In the Onboarding Templates , select the Customer. |
| 3 | Click on the Service settings , in the Preference section enable Directory Sync. |
| 4 | To enable directory sync by default for new customer organziations that use this template: Set the Enable BroadWorks Directory & Phone List Sync for all new customer organizations toggle to On . Click Save . |
| 5 | To enable directory sync for existing customer organizations that use this template: Click Show list of customers sync status . Check the adjacent check boxes for each organization for which you want to turn the feature on. Click Enable Sync . If you want to disable directory sync, follow the above procedure and: In step 4a, set the Enable phone directory sync for all new customer organizations toggle to Off to disable directory sync by default for new customer organizations that use this template. In step 5c, click Disable Sync to turn the feature off for existing organizations. |

| 1 | Sign in to Partner Hub ( http://admin.webex.com ) and choose Settings . |
|---|---|
| 2 | Scroll to BroadWorks Calling and click View Templates . |
| 3 | Select the appropriate customer template and scroll to BroadWorks Directory Sync . |
| 4 | Click Show list of customers sync status . |
| 5 | For the customer organization that you want to sync, click the three dots on the far right and select Sync Now . |
| 6 | Click Refresh to see the sync results. |

| 1 | Sign in to Partner Hub ( http://admin.webex.com ) and choose Settings . |
|---|---|
| 2 | Scroll to BroadWorks Calling and click View Templates . |
| 3 | Select the appropriate customer template and scroll to BroadWorks Directory Sync . |
| 4 | Click Show list of customers sync status . |
| 5 | Check the adjacent check boxes for each organization that you want to include in the export. |
| 6 | Click Export results . |

| 1 | Run the List BroadWorks Enterprises API to generate a list of enterprises that you want to sync. Set startWith to the starting string of the enterprise or service provider identifier. Click Run . |
|---|---|
| 2 | Run the Trigger Directory Sync for an Enterprise API on the first enterprise in the list. Enter the enterprise id . Set syncStatus to SYNC_NOW Click Run . An immediate sync gets triggered for the enterprise. This sync counts against the single on-demand sync per Broadworks limit. |
| 3 | Wait for a few seconds and then run the Get Directory Sync Status API to get sync status. Enter the enterprise id Click Run . |
| 4 | After the sync finishes, complete steps 2 to 4 on the next enterprise in the list. Repeat these steps until you have synced the entire list. |

| Error Code | Error Message |
|---|---|
| 600000 | Broadworks External Directory User Sync unexpected error. |
| 600001 | Broadworks External Directory User Sync failed. |
| 600002 | Broadworks External Directory User Sync had to be terminated before completion. |
| 600003 | Broadworks External Directory User Sync only partially succeeded. Some Customer Organizations failed to sync. |
| 600004 | Broadworks External Directory User Sync is not enabled for the ConfigSet. |
| 600005 | Broadworks External Directory User Sync is in-progress for the ConfigSet. |
| 600006 | Broadworks External Directory User Sync threads are busy or shutting down, hence will not accept more sync request, try again later. |
| 600007 | The Identity Org of the CustomerConfig is not found. |
| 600008 | The CustomerConfig is not found in the partner org. |
| 600009 | Broadworks External Directory User Sync cannot be run as the broadworks cluster associated to the CustomerConfig is busy |
| 600010 | Broadworks External Directory User Sync cannot be run as there is no broadworks cluster associated to the CustomerConfig. |
| 600011 | Broadworks External Directory User Sync is not enabled for the CustomerConfig. |
| 600012 | Broadworks External Directory User Sync cannot be run as the Hybrid Directory sync is already enabled for the CustomerConfig. |
| 600013 | Broadworks External Directory User Sync failed to add users and machine accounts to identity store. |
| 600014 | Broadworks External Directory User Sync failed while trying to connect to Broadworks cluster. Error from Broadworks - %s. |
| 600015 | Broadworks External Directory User Sync didn't find any matching user in identity store. |
| 600017 | BroadWorks Phone List Sync failed to sync all user and enterprise/organization contacts. |
| 600018 | BroadWorks Phone List Sync failed for users in the enterprise/organization. |
| 600019 | BroadWorks Phone List Sync failed to sync enterprise/organization contacts. |
| 600020 | BroadWorks External Directory User Sync cannot be disabled as the CustomerConfig sync is in progress. |
| 600022 | BroadWorks External Directory Single User Sync is not possible since the enterprise has no provisioned user. |
| 600023 | BroadWorks External Directory Single User Sync is not possible because the user already exists in this organization. |
| 600024 | BroadWorks External Directory Single User Sync is not possible because no matching user was found in BroadWorks. |
| 600025 | BroadWorks External Directory User Sync failed to update the user account in CI. |
| 600026 | BroadWorks External Directory User Sync failed to update the machine account in CI. |
| 600027 | BroadWorks External Directory Single User Sync is not possible because multiple users were found in BroadWorks. |
| 600028 | BroadWorks External Directory Single User Sync is not possible because at least one enterprise directory sync should have been completed. |
| 600029 | BroadWorks External Directory User Sync failed since the enterprise has no provisioned user. |

| Date | Revision |
|---|---|
| February 14, 2023 | Updated Directory Sync Maximums and Source section. |
| December 10, 2022 | Updated the term Complete Immediate Sync to Trigger Directory Sync |
| July 19, 2022 | Clarifications and corrections to overview information: Updated Directory Sync Overview to clarify the different syncs involved and how the Webex directory gets updated for each. Updated BroadWorks Phone List and Contact Maximums to clarify that only phone lists get synced to Contacts. Corrections to Updates to clarify how long it takes for the Webex App to display updated records. |
| May 09, 2022 | In Directory Sync Overview , corrected Note under the Directory Sync Maximums and Source table. Also updated Note on flowthrough provisioning. Grammatical edits and fixes |
| April 07, 2022 | Added Note to the Updates section in Directory Sync Overview around limitation of applying organization-level contact edits in Control Hub. |
| March 28, 2022 | Reinserted missing content under Enable Directory Sync (New Template) . Added information on sync maximums. You can run one scheduled sync and one API sync simultaneously from the same cluster. Added information on Trigger Directory Sync for a single user API. |
| March 24, 2022 | Added list of synced phone number types to Directory Sync Conditions . The sync now includes mobile phone numbers. |
| March 16, 2022 | Added new error codes. Added introductory description statement for better usability from web searches. |
| December 17, 2021 | Minor structural edits to fix issue with missing TOC. |
| December 16, 2021 | Updated article with increased maximum values for User contacts. |
| December 08, 2021 | Added section Directory Sync and Contact Maximums to clarify how Directory Sync derives the maximum number of Organization and User contacts. Revised table formatting in Error Codes for Directory Sync for better readability. |