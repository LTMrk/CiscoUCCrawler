---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-12-5-1-su4-cup0-b-config-and-admin-guide-1-a1803236f9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/12_5_1_su4/cup0_b_config-and-admin-guide-1251su4/cup0_b_config-and-admin-guide-1251su3_chapter_011001.html
retrieved_at: 2026-08-16T16:46:22.487021+00:00
---

Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU4 to 12.5(1)SU7

# Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU4 to 12.5(1)SU7

Updated: November 27, 2024

Chapter: Migrate Users to Centralized Deployment

## Chapter: Migrate Users to Centralized Deployment

# Migrate Users to Centralized Deployment

## Centralized Deployment User Migration Overview

This chapter contains procedures for migrating existing IM and Presence Service users from a standard decentralized IM and
                              Presence deployment (IM and Presence Service on Cisco Unified Communications Manager) to a centralized deployment. With the
                              centralized deployment, the IM and Presence deployment and the telephony deployment are in separate clusters.

## Prerequisite Tasks for Central Cluster Migration

If you are setting up a new IM and Presence central cluster whereby all the users are migrating from existing decentralized
                              clusters, complete the following prerequisite steps to set up the cluster for migration.

If you are adding new users whom are not a part of the migration, you can follow the instructions in Configure Centralized Deployment to set up the central cluster with your new users. Migrate existing users to the central cluster only after you are confident
                                          that your configuration works.

Pre-Migration Tasks

Step 1

Connect your new central cluster to the migrating cluster.

Log in to database publisher node on the IM and Presence Service centralized cluster.

From Cisco Unified CM IM and Presence Administration, choose System > Centralized Deployment .

Click Find and do either of the following:

Select an existing cluster and click Edit Selected .

Click Add New to add the migrating cluster.

Complete the following fields for each migrating cluster:

Peer Address —The FQDN, hostname, IPv4 address, or IPv6 address of the publisher node on the remote telephony

AXL Username —The login username for the AXL account on the remote telephony cluster.

AXL Password —The password for the AXL account on the remote cluster.

Click Save .

Step 2

If the new central cluster will be part of an IM and Presence intercluster network, configure intercluster peering between
                                          the central cluster and any IM and Presence peer clusters that are not a part of the migration. The following guidelines apply:

You do not need to configure intercluster peering between the central cluster and the migrating clusters. However, if a migrating
                                                cluster has an intercluster peer connection configured with any number of non-migrating clusters at the time of the migration,
                                                it’s mandatory that those intercluster peer connections are configured in the central cluster prior to the migration or the
                                                migration will not work.

After configuring intercluster peering, make sure to verify the intercluster peering status to ensure that the configuration
                                                works properly

For details, see Configure Intercluster Peers .

## Migration to Central Cluster Task Flow

Complete these tasks to migrate existing users from a decentralized cluster (IM and Presence Service on Cisco Unified Communications
                              Manager) to a centralized IM and Presence cluster. In this task flow:

IM and Presence Central Cluster refers to the cluster to which you are migating users. Following the migration, this cluster handles IM and Presence only.

Migrating Cluster refers to the cluster from which IM and Presence users are being migrated. Following the migration, this cluster handles
                                    telephony only.

### Before You Begin

If your IM and Presence central cluster is a newly installed cluster, and does not yet have users, complete the Prerequisite Tasks for Central Cluster Migration before you migrate users.

IM and Presence Central Cluster

Migrating Cluster

Purpose

Step 1

Export Contact Lists from Migrating Cluster

Export user contact lists in the migrating cluster to a csv file.

Step 2

Disable High Availability in Migrating Cluster

Disable High Availability for all Presence Redundancy Groups (subclusters) in the migrating cluster.

Step 3

Configure UC Service for IM and Presence

In the migrating cluster, configure IM and Presence UC services that point to the IM and Presence central cluster.

Step 4

Create Service Profile for IM and Presence

In the migrating cluster, create a service profile that uses the IM and Presence UC services that you set up.

Step 5

Disable Presence Users in Telephony Cluster

Use Bulk Administration in the migrating cluster to disable IM and Presence for users.

Step 6

Enable OAuth Authentication for Central Cluster

Optional. In the migrating cluster, enable OAuth Refresh Logins. This will enable the feature for the central cluster as well.

Step 7

Disable High Availability in Central Cluster

Disable High Availability in all Presence Redundancy Groups (subcluster) of the IM and Presence central cluster.

Step 8

Delete Peer Relationship for Central and Migrating Clusters

If intercluster peering exists  between the central cluster and  migrating cluster, delete the peer connection on both clusters.

Step 9

Stop the Cisco Intercluster Sync Agent

Stop the Cisco Intercluster Sync Agent in the IM and Presence central cluster.

Step 10

Enable IM and Presence via Feature Group Template

In the cenral cluster, configure a Feature Group Template that enables the IM and Presence Service.

Step 11

Complete LDAP Sync on Central Cluster

Add the feature group template to an LDAP directory sync. Use the sync to add users from the migrating cluster.

Step 12

Import Contact Lists into Central Cluster

Use Bulk Administration and the csv export file that you created earlier to import contact lists into the central cluster.

Step 13

Start Cisco Intercluster Sync Agent

Start the Cisco Intercluster Sync Agent in the central cluster.

Step 14

Enable High Availability in Central Cluster

In the central cluster, enable High Availability in all Presence Redundancy Groups.

Step 15

Delete Remaining Peers for Migrating Cluster

Delete remaining intercluster peer connections between migrating cluster (now a telephony cluster) and other peer clusters.

### Export Contact Lists from Migrating Cluster

Contact Lists—This list consists of IM and Presence contacts. Contacts whom do not have an IM address will not be exported
                                       with this list (you must export a non-presence contact list).

Non-presence Contact Lists—This list consists of contacts whom do not have an IM address.

Step 1

Log in to Cisco Unified CM IM and Presence Administration in the old clsuter (the telephony cluster).

Step 2

Choose one of the following options, depending on which type of contact list you want to export:

- For Contact List exports, choose Bulk Administration > Contact List > Export Contact List

- for Non-presence Contact List exports, choose Bulk Administration > Non-presence Contact List > Export Non-presence Contact List and skip the next step.

Step 3

Contact Lists only. Select the users for whom you will export contact lists:

Under Export Contact List Options , choose the category of users for whom you will export contact lists. The default option is All users in the cluster .

Click Find to bring up the list of users and then click Next .

Step 4

Enter a File Name .

Step 5

Under Job Information , configure when you want to run this job:

- Run Immediately —Check this button to export contact lists right away.

- Run Later —Check this button if you want to schedule a time for the job to run.

Step 6

Click Submit .

If you chose Run Immediately , your export file gets generated right away. If you chose Run Later , you must use the Job Scheduler at ( Bulk Administration > Job Scheduler ) to schedule a time for this job to run.

Step 7

After the export file is generated, download the csv file:

Choose Bulk Administration > Upload/Download Files .

Click Find .

Select the export file that you want to download and click Download Selected .

Save the file to a safe location.

Step 8

Repeat this procedure if you want to create another csv export file. For example, if you create an export file for Contact
                                          Lists, you may want to create another file for Non-presence Contact Lists.

#### What to do next

### Disable High Availability in Migrating Cluster

For migrations to a Centralized Deployment, disable High Availability in each Presence Redundancy Group (subcluster) on the
                                 migrating telephony cluster.

The Presence Redundancy Group Details page shows all the active JSM sessions, even when the high availability is disabled in the cluster.

Step 1

Log in to the Cisco Unified Communications Manager publisher node on the old cluster.

Step 2

From Cisco Unified CM Administration, choose System > Presence Redundancy Groups .

Step 3

Click Find and select a subcluster.

Step 4

Uncheck the Enable High Availability check box.

Step 5

Click Save .

Step 6

Repeat this procedure for each subcluster.

#### What to do next

### Configure UC Service for IM and Presence

Use this procedure in your remote telephony clusters to configure a UC service that points to the IM and Presence Service
                                 central cluster. Users in the telephony cluster will get IM and Presence services from the IM and Presence central cluster.

Step 1

Log in to the Cisco Unified CM Administration interface on your telephony cluster.

Step 2

Choose User Management > User Settings > UC Service .

Step 3

Do either of the following:

Click Find and select an existing service to edit.

Click Add New to create a new UC service.

Step 4

From the UC Service Type drop-down list box, select IM and Presence and click Next .

Step 5

From the Product type drop-down list box, select IM and Presence Service .

Step 6

Enter a unique Name for the cluster. This does not have to be a hostname.

Step 7

From HostName/IP Address , enter the hostname, IPv4 address, or IPv6 address of the IM and Presence central cluster database publisher node.

Step 8

Click Save .

Step 9

Recommended. Repeat this procedure to create a second IM and Presence service where the HostName/IP Address field points to a subscriber node in the central cluster.

#### What to do next

### Create Service Profile for IM and Presence

Use this procedure in your remote telephony clusters to create a service profile that points to the IM and Presence central
                                 cluster. Users in the telephony cluster will use this service profile to get IM and Presence services from the central cluster.

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > Service Profile .

Step 2

Do one of the following:

Click Find and select an existing service profile to edit.

Click Add New to create a new service profile.

Step 3

In the IM and Presence Profile section, configure IM and Presence services that you configured in the previous task:

From the Primary drop-down, select the database publisher node service.

From the Secondary drop-down, select the subscriber node service.

Step 4

Click Save .

#### What to do next

### Disable Presence Users in Telephony Cluster

If you've already completed an LDAP sync in your telephony deployment, use the Bulk Administration Tool to edit user settings
                                 in the Telephony cluster for IM and Presence users. This configuration will point Presence users to the Central Cluster for
                                 the IM and Presence Service.

This procedure assumes that you have already completed an LDAP sync in your telephony cluster. However, if you haven't yet
                                             completed the initial LDAP sync, you can add the Central Deployment settings for Presence users into your initial sync. In
                                             this case, do the following in your telephony cluster:

Configure a Feature Group Template that includes the Service Profile that you just set up. Make sure that have the Home Cluster option selected and the Enable User for Unified CM IM and Presence option unselected.

In LDAP Directory Configuration , add the Feature Group Template to your LDAP Directory sync.

Complete the initial sync.

For additional details on configuring Feature Group Templates and LDAP Directory, see the "Configure End Users" part of the System Configuration Guide for Cisco Unified Communications Manager .

Step 1

From Cisco Unified CM Administration, choose Query > Bulk Administration > Users > Update Users > Query .

Step 2

From the Filter, select Has Home Cluster Enabled and click Find . The window displays all of the end users for whom this is their Home Cluster.

Step 3

Click Next .

Step 4

Under Service Settings , check the far left check box for each of the following fields to indicate that you want to update these fields, and then
                                          edit the adjacent setting as follows:

- Home Cluster —Check the right check box to enable the telephony cluster as the home cluster.

- Enable User for Unified CM IM and Presence —Leave the right check box unchecked. This setting disables the telephony cluster as the provider of IM and Presence.

- UC Service Profile —From the drop-down, select the service profile that you configured in the previous task. This setting points users to the
                                             IM and Presence central cluster, which will be the provider of the IM and Presence Service.

For Expressway Mobile and Remote Access configuration, see Mobile and Remote Access via Cisco Expressway Deployment Guide at https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html .

Step 5

Complete any remaining fields that you want. For help with the fields and their settings, see the online help.

Step 6

Under Job Information , select Run Immediately .

Step 7

Click Submit .

#### What to do next

### Enable OAuth Authentication for Central Cluster

Step 1

Log in to Cisco Unified CM Administration on the telephony cluster.

Step 2

Choose System > Enterprise Parameters

Step 3

Under SSO And OAuth Configuration , set the OAuth with Refresh Login Flow enterprise parameter to Enabled .

Step 4

If you edited the parameter setting, click Save .

### Disable High Availability in Central Cluster

The Presence Redundancy Group Details page shows all the active JSM sessions, even when the high availability is disabled in the cluster.

Step 1

Log in to Cisco Unified CM Administration instance for the central cluster.

Step 2

Choose System > Presence Redundancy Groups .

Step 3

Click Find and select an existing subcluster.

Step 4

Uncheck the Enable High Availability check box.

Step 5

Click Save .

Step 6

Repeat this step for each subcluster.

#### What to do next

### Delete Peer Relationship for Central and Migrating Clusters

Step 1

Log in to the IM and Presence Service central cluster's database publisher node.

Step 2

From Cisco Unified CM IM and Presence Administration, choose Presence > Inter-Clustering .

Step 3

Click Find and select the migrating cluster.

Step 4

Click Delete .

Step 5

Restart the Cisco XCP Router :

Log in to Unified IM and Presence Serviceability and choose Tools > Control Center - Network Services .

From the Server list, choose the database publisher node and click Go .

Under IM and Presence Services , select Cisco XCP Router and click Restart .

Step 6

Repeat these steps on the migrating cluster.

### Stop the Cisco Intercluster Sync Agent

Step 1

From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services .

Step 2

From the Server drop-down, select the central cluster database publisher node, and click Go .

Step 3

Confirm the status of the Cisco Intercluster Sync Agent service. If the service is running or activated, select the adjacent radio button and click Stop .

#### What to do next

### Enable IM and Presence via Feature Group Template

Use this procedure to configure a feature group template with IM and Presence settings for the central cluster. You can add
                                 the feature group template to an LDAP Directory configuration to configure IM and Presence for synced users.

You can apply a feature group template only to an LDAP directory configuration where the initial sync has not yet occurred.
                                             Once you've synced your LDAP configuration from the central cluster, you cannot apply edits to the LDAP configuration in Cisco
                                             Unified Communications Manager. If you have already synced your directory, you will need to use Bulk Administration to configure
                                             IM and Presence for users. For details, see Enable Users for IM and Presence via Bulk Admin .

Step 1

Log into the Cisco Unified CM Administration interface of the IM and Presence centralized cluster. This server should have
                                          no telephony configured.

Step 2

Choose User Management > User Phone/Add > Feature Group Template .

Step 3

Do one of the following:

- Click Find and select an existing template

- Click Add New to create a new template

Step 4

Check both of the following check boxes:

- Home Cluster

- Enable User for Unified CM IM and Presence

Step 5

Complete the remaining fields in the Feature Group Template Configuration window. For help with the fields and their settings, refer to the online help.

Step 6

Click Save .

#### What to do next

To propagate the setting to users, you must add the Feature Group Template to an LDAP directory configuration where the initial
                                 sync has not yet occurred, and then complete the initial sync.

Complete LDAP Sync on Central Cluster

### Complete LDAP Sync on Central Cluster

Use this procedure on your remote Cisco Unified Communications Manager telephony clusters to use an LDAP sync to deploy your
                                 centralized IM and Presence settings to your Cisco Unified Communications Manager deployment.

Step 1

From Cisco Unified CM Administration, choose the System > LDAP > LDAP Directory .

Step 2

Do either of the following:

- Click Find and select an existing LDAP Directory sync.

- Click Add New to create a new LDAP Directory sync.

Step 3

From the Feature Group Template drop-down list box, select the feature group template that you created in the previous task. IM and Presence must be disabled
                                          on this template.

Step 4

Complete the remaining fields in the LDAP Directory window. For help with the fields and their settings, refer to the online help.

Step 5

Click Save .

Step 6

Click Perform Full Sync .

#### What to do next

### Enable Users for IM and Presence via Bulk Admin

If you have already synced users into the central cluster, and those users were not enabled for the IM and Presence Service,
                                 use Bulk Administration's Update Users feature to enable those users for the IM and Presence Service.

You can also use Bulk Administration's Import Users or Insert Users feature to import new users via a csv file. For procedures,
                                             see the Bulk Administration Guide for Cisco Unified Communications Manager . Make sure that the imported users have the below options selected:

Home Cluster

Enable User for Unified CM IM and Presence

Step 1

From Cisco Unified CM Administration, choose Bulk Administration > Users > Update Users > Query .

Step 2

From the Filter , select Has Home Cluster Enabled and click Find . The window displays all of the end users for whom this is their Home Cluster

Step 3

Click Next .

Step 4

Under Service Settings , check the left check box for each of the following fields to indicate that you want to update these fields, and then edit
                                          the adjacent field setting as follows:

- Home Cluster —Check the right check box to enable this cluster as the home cluster.

- Enable User for Unified CM IM and Presence —Check the right check box. This setting enables the central cluster as the provider of IM and Presence Service for these
                                             users.

Step 5

Complete any remaining fields that you want to update. For help with the fields and their settings, see the online help:

Step 6

Under Job Information , select Run Immediately .

Step 7

Click Submit .

### Import Contact Lists into Central Cluster

Contact lists—This list contains IM and Presence contacts.

Non-presence contact lists—This list contains contacts whom do not have an IM address.

#### Before you begin

Step 1

Log in to Cisco Unified CM IM and Presence Administration on the IM and Presence central cluster.

Step 2

Upload the csv file that you exported from the telephony cluster:

Choose Bulk Administration > Upload/Download Files .

Click Add New .

Click Choose File and select the csv file that you want to import.

From the Select the Target drop-down select either of the following: Contact Lists or Non-presence Contact Lists depending on which type of contact list you are importing.

From the Select Transaction Type , select the import job.

Click Save .

Step 3

Import the csv information into the central cluster:

From Cisco Unified CM IM and Presence Administration, do either of the following:

For Contact List imports, choose Bulk Administration > Contact Lists > Update Contact Lists .

For Non-presence Contact List imports, choose Bulk Administration > Non-presence Contact Lists > Import Non-presence Contact Lists .

From the File Name drop-down, select the csv file that you uploaded.

Under Job Information , select either Run Immediately or Run Later depending on when you want the job to run.

Click Submit . If you chose Run Immediately , the contact lists get imported right away

Step 4

Repeat this procedure if you have a second csv file to import.

#### What to do next

### Start Cisco Intercluster Sync Agent

Step 1

From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services .

Step 2

From the Server drop-down, select the IM and Presence database publisher node and click Go .

Step 3

Under IM and Presence Services , select the Cisco Intercluster Sync Agent and click Start .

#### What to do next

### Enable High Availability in Central Cluster

Step 1

Log in to the Cisco Unified CM Administration instance on the IM and Presence central cluster.

Step 2

Choose System > Presence Redundancy Groups .

Step 3

Click Find and select an existing subcluster.

Step 4

Check the Enable High Availability check box.

Step 5

Click Save .

Step 6

Repeat this procedure for each subcluster in the IM and Presence central cluster.

### Delete Remaining Peers for Migrating Cluster

Step 1

Log in to the migrating cluster's IM and Presence database publisher node.

Step 2

From Cisco Unified CM IM and Presence Administration, choose Presence > Inter-Clustering .

Step 3

Click Find and select the peer cluster.

Step 4

Click Delete .

Step 5

Restart the Cisco XCP Router :

Log in to Unified IM and Presence Serviceability and choose Tools > Control Center - Network Services .

From the Server list, choose the database publisher node and click Go .

Under IM and Presence Services , select Cisco XCP Router and click Restart .

Step 6

Repeat these steps on the IM and Presence Service peer cluster.

| Note | If you are adding new users whom are not a part of the migration, you can follow the instructions in Configure Centralized Deployment to set up the central cluster with your new users. Migrate existing users to the central cluster only after you are confident
                                          that your configuration works. |
|---|---|

|  | Pre-Migration Tasks |
|---|---|
| Step 1 | Connect your new central cluster to the migrating cluster. Log in to database publisher node on the IM and Presence Service centralized cluster. From Cisco Unified CM IM and Presence Administration, choose System > Centralized Deployment . Click Find and do either of the following: Select an existing cluster and click Edit Selected . Click Add New to add the migrating cluster. Complete the following fields for each migrating cluster: Peer Address —The FQDN, hostname, IPv4 address, or IPv6 address of the publisher node on the remote telephony AXL Username —The login username for the AXL account on the remote telephony cluster. AXL Password —The password for the AXL account on the remote cluster. Click Save . |
| Step 2 | If the new central cluster will be part of an IM and Presence intercluster network, configure intercluster peering between
                                          the central cluster and any IM and Presence peer clusters that are not a part of the migration. The following guidelines apply: You do not need to configure intercluster peering between the central cluster and the migrating clusters. However, if a migrating
                                                cluster has an intercluster peer connection configured with any number of non-migrating clusters at the time of the migration,
                                                it’s mandatory that those intercluster peer connections are configured in the central cluster prior to the migration or the
                                                migration will not work. After configuring intercluster peering, make sure to verify the intercluster peering status to ensure that the configuration
                                                works properly For details, see Configure Intercluster Peers . |

|  | IM and Presence Central Cluster | Migrating Cluster | Purpose |
|---|---|---|---|
| Step 1 |  | Export Contact Lists from Migrating Cluster | Export user contact lists in the migrating cluster to a csv file. |
| Step 2 |  | Disable High Availability in Migrating Cluster | Disable High Availability for all Presence Redundancy Groups (subclusters) in the migrating cluster. |
| Step 3 |  | Configure UC Service for IM and Presence | In the migrating cluster, configure IM and Presence UC services that point to the IM and Presence central cluster. |
| Step 4 |  | Create Service Profile for IM and Presence | In the migrating cluster, create a service profile that uses the IM and Presence UC services that you set up. |
| Step 5 |  | Disable Presence Users in Telephony Cluster | Use Bulk Administration in the migrating cluster to disable IM and Presence for users. |
| Step 6 |  | Enable OAuth Authentication for Central Cluster | Optional. In the migrating cluster, enable OAuth Refresh Logins. This will enable the feature for the central cluster as well. |
| Step 7 | Disable High Availability in Central Cluster |  | Disable High Availability in all Presence Redundancy Groups (subcluster) of the IM and Presence central cluster. |
| Step 8 | Delete Peer Relationship for Central and Migrating Clusters |  | If intercluster peering exists  between the central cluster and  migrating cluster, delete the peer connection on both clusters. |
| Step 9 | Stop the Cisco Intercluster Sync Agent |  | Stop the Cisco Intercluster Sync Agent in the IM and Presence central cluster. |
| Step 10 | Enable IM and Presence via Feature Group Template |  | In the cenral cluster, configure a Feature Group Template that enables the IM and Presence Service. |
| Step 11 | Complete LDAP Sync on Central Cluster |  | Add the feature group template to an LDAP directory sync. Use the sync to add users from the migrating cluster. |
| Step 12 | Import Contact Lists into Central Cluster |  | Use Bulk Administration and the csv export file that you created earlier to import contact lists into the central cluster. |
| Step 13 | Start Cisco Intercluster Sync Agent |  | Start the Cisco Intercluster Sync Agent in the central cluster. |
| Step 14 | Enable High Availability in Central Cluster |  | In the central cluster, enable High Availability in all Presence Redundancy Groups. |
| Step 15 | Delete Remaining Peers for Migrating Cluster |  | Delete remaining intercluster peer connections between migrating cluster (now a telephony cluster) and other peer clusters. |

| Step 1 | Log in to Cisco Unified CM IM and Presence Administration in the old clsuter (the telephony cluster). |
|---|---|
| Step 2 | Choose one of the following options, depending on which type of contact list you want to export: For Contact List exports, choose Bulk Administration > Contact List > Export Contact List for Non-presence Contact List exports, choose Bulk Administration > Non-presence Contact List > Export Non-presence Contact List and skip the next step. |
| Step 3 | Contact Lists only. Select the users for whom you will export contact lists: Under Export Contact List Options , choose the category of users for whom you will export contact lists. The default option is All users in the cluster . Click Find to bring up the list of users and then click Next . |
| Step 4 | Enter a File Name . |
| Step 5 | Under Job Information , configure when you want to run this job: Run Immediately —Check this button to export contact lists right away. Run Later —Check this button if you want to schedule a time for the job to run. |
| Step 6 | Click Submit . Note If you chose Run Immediately , your export file gets generated right away. If you chose Run Later , you must use the Job Scheduler at ( Bulk Administration > Job Scheduler ) to schedule a time for this job to run. | Note | If you chose Run Immediately , your export file gets generated right away. If you chose Run Later , you must use the Job Scheduler at ( Bulk Administration > Job Scheduler ) to schedule a time for this job to run. |
| Note | If you chose Run Immediately , your export file gets generated right away. If you chose Run Later , you must use the Job Scheduler at ( Bulk Administration > Job Scheduler ) to schedule a time for this job to run. |
| Step 7 | After the export file is generated, download the csv file: Choose Bulk Administration > Upload/Download Files . Click Find . Select the export file that you want to download and click Download Selected . Save the file to a safe location. |
| Step 8 | Repeat this procedure if you want to create another csv export file. For example, if you create an export file for Contact
                                          Lists, you may want to create another file for Non-presence Contact Lists. |

| Note | If you chose Run Immediately , your export file gets generated right away. If you chose Run Later , you must use the Job Scheduler at ( Bulk Administration > Job Scheduler ) to schedule a time for this job to run. |
|---|---|

| Note | The Presence Redundancy Group Details page shows all the active JSM sessions, even when the high availability is disabled in the cluster. |
|---|---|

| Step 1 | Log in to the Cisco Unified Communications Manager publisher node on the old cluster. |
|---|---|
| Step 2 | From Cisco Unified CM Administration, choose System > Presence Redundancy Groups . |
| Step 3 | Click Find and select a subcluster. |
| Step 4 | Uncheck the Enable High Availability check box. |
| Step 5 | Click Save . |
| Step 6 | Repeat this procedure for each subcluster. Note After completing this procedure for all subclusters, wait at least 2 minutes before completing any additional configurations
                                                      on this cluster. | Note | After completing this procedure for all subclusters, wait at least 2 minutes before completing any additional configurations
                                                      on this cluster. |
| Note | After completing this procedure for all subclusters, wait at least 2 minutes before completing any additional configurations
                                                      on this cluster. |

| Note | After completing this procedure for all subclusters, wait at least 2 minutes before completing any additional configurations
                                                      on this cluster. |
|---|---|

| Step 1 | Log in to the Cisco Unified CM Administration interface on your telephony cluster. |
|---|---|
| Step 2 | Choose User Management > User Settings > UC Service . |
| Step 3 | Do either of the following: Click Find and select an existing service to edit. Click Add New to create a new UC service. |
| Step 4 | From the UC Service Type drop-down list box, select IM and Presence and click Next . |
| Step 5 | From the Product type drop-down list box, select IM and Presence Service . |
| Step 6 | Enter a unique Name for the cluster. This does not have to be a hostname. |
| Step 7 | From HostName/IP Address , enter the hostname, IPv4 address, or IPv6 address of the IM and Presence central cluster database publisher node. |
| Step 8 | Click Save . |
| Step 9 | Recommended. Repeat this procedure to create a second IM and Presence service where the HostName/IP Address field points to a subscriber node in the central cluster. |

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > Service Profile . |
|---|---|
| Step 2 | Do one of the following: Click Find and select an existing service profile to edit. Click Add New to create a new service profile. |
| Step 3 | In the IM and Presence Profile section, configure IM and Presence services that you configured in the previous task: From the Primary drop-down, select the database publisher node service. From the Secondary drop-down, select the subscriber node service. |
| Step 4 | Click Save . |

| Note | This procedure assumes that you have already completed an LDAP sync in your telephony cluster. However, if you haven't yet
                                             completed the initial LDAP sync, you can add the Central Deployment settings for Presence users into your initial sync. In
                                             this case, do the following in your telephony cluster: Configure a Feature Group Template that includes the Service Profile that you just set up. Make sure that have the Home Cluster option selected and the Enable User for Unified CM IM and Presence option unselected. In LDAP Directory Configuration , add the Feature Group Template to your LDAP Directory sync. Complete the initial sync. For additional details on configuring Feature Group Templates and LDAP Directory, see the "Configure End Users" part of the System Configuration Guide for Cisco Unified Communications Manager . |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Query > Bulk Administration > Users > Update Users > Query . |
|---|---|
| Step 2 | From the Filter, select Has Home Cluster Enabled and click Find . The window displays all of the end users for whom this is their Home Cluster. |
| Step 3 | Click Next . In the Update Users Configuration window, the check boxes on the far left indicate whether you want to edit this setting with this query. If you don't check
                                          the left check box, the query will not update that field. The field on the right indicates the new setting for this field.
                                          If two check boxes appear, you must check the check box on the left to update the field, and in the right check box, enter
                                          the new setting. |
| Step 4 | Under Service Settings , check the far left check box for each of the following fields to indicate that you want to update these fields, and then
                                          edit the adjacent setting as follows: Home Cluster —Check the right check box to enable the telephony cluster as the home cluster. Enable User for Unified CM IM and Presence —Leave the right check box unchecked. This setting disables the telephony cluster as the provider of IM and Presence. UC Service Profile —From the drop-down, select the service profile that you configured in the previous task. This setting points users to the
                                             IM and Presence central cluster, which will be the provider of the IM and Presence Service. Note For Expressway Mobile and Remote Access configuration, see Mobile and Remote Access via Cisco Expressway Deployment Guide at https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html . | Note | For Expressway Mobile and Remote Access configuration, see Mobile and Remote Access via Cisco Expressway Deployment Guide at https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html . |
| Note | For Expressway Mobile and Remote Access configuration, see Mobile and Remote Access via Cisco Expressway Deployment Guide at https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html . |
| Step 5 | Complete any remaining fields that you want. For help with the fields and their settings, see the online help. |
| Step 6 | Under Job Information , select Run Immediately . |
| Step 7 | Click Submit . |

| Note | For Expressway Mobile and Remote Access configuration, see Mobile and Remote Access via Cisco Expressway Deployment Guide at https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html . |
|---|---|

| Step 1 | Log in to Cisco Unified CM Administration on the telephony cluster. |
|---|---|
| Step 2 | Choose System > Enterprise Parameters |
| Step 3 | Under SSO And OAuth Configuration , set the OAuth with Refresh Login Flow enterprise parameter to Enabled . |
| Step 4 | If you edited the parameter setting, click Save . |

| Note | The Presence Redundancy Group Details page shows all the active JSM sessions, even when the high availability is disabled in the cluster. |
|---|---|

| Step 1 | Log in to Cisco Unified CM Administration instance for the central cluster. |
|---|---|
| Step 2 | Choose System > Presence Redundancy Groups . |
| Step 3 | Click Find and select an existing subcluster. |
| Step 4 | Uncheck the Enable High Availability check box. |
| Step 5 | Click Save . |
| Step 6 | Repeat this step for each subcluster. |

| Step 1 | Log in to the IM and Presence Service central cluster's database publisher node. |
|---|---|
| Step 2 | From Cisco Unified CM IM and Presence Administration, choose Presence > Inter-Clustering . |
| Step 3 | Click Find and select the migrating cluster. |
| Step 4 | Click Delete . |
| Step 5 | Restart the Cisco XCP Router : Log in to Unified IM and Presence Serviceability and choose Tools > Control Center - Network Services . From the Server list, choose the database publisher node and click Go . Under IM and Presence Services , select Cisco XCP Router and click Restart . |
| Step 6 | Repeat these steps on the migrating cluster. |

| Step 1 | From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services . |
|---|---|
| Step 2 | From the Server drop-down, select the central cluster database publisher node, and click Go . |
| Step 3 | Confirm the status of the Cisco Intercluster Sync Agent service. If the service is running or activated, select the adjacent radio button and click Stop . |

| Note | You can apply a feature group template only to an LDAP directory configuration where the initial sync has not yet occurred.
                                             Once you've synced your LDAP configuration from the central cluster, you cannot apply edits to the LDAP configuration in Cisco
                                             Unified Communications Manager. If you have already synced your directory, you will need to use Bulk Administration to configure
                                             IM and Presence for users. For details, see Enable Users for IM and Presence via Bulk Admin . |
|---|---|

| Step 1 | Log into the Cisco Unified CM Administration interface of the IM and Presence centralized cluster. This server should have
                                          no telephony configured. |
|---|---|
| Step 2 | Choose User Management > User Phone/Add > Feature Group Template . |
| Step 3 | Do one of the following: Click Find and select an existing template Click Add New to create a new template |
| Step 4 | Check both of the following check boxes: Home Cluster Enable User for Unified CM IM and Presence |
| Step 5 | Complete the remaining fields in the Feature Group Template Configuration window. For help with the fields and their settings, refer to the online help. |
| Step 6 | Click Save . |

| Note | For more details on how to set up an LDAP Directory sync, see the "Configure End Users" part of the System Configuration Guide for Cisco Unified Communications Manager . |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose the System > LDAP > LDAP Directory . |
|---|---|
| Step 2 | Do either of the following: Click Find and select an existing LDAP Directory sync. Click Add New to create a new LDAP Directory sync. |
| Step 3 | From the Feature Group Template drop-down list box, select the feature group template that you created in the previous task. IM and Presence must be disabled
                                          on this template. |
| Step 4 | Complete the remaining fields in the LDAP Directory window. For help with the fields and their settings, refer to the online help. |
| Step 5 | Click Save . |
| Step 6 | Click Perform Full Sync . Cisco Unified Communications Manager synchronizes its database with the LDAP directory and assigns the updated IM and Presence
                                          settings. |

| Note | You can also use Bulk Administration's Import Users or Insert Users feature to import new users via a csv file. For procedures,
                                             see the Bulk Administration Guide for Cisco Unified Communications Manager . Make sure that the imported users have the below options selected: Home Cluster Enable User for Unified CM IM and Presence |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Bulk Administration > Users > Update Users > Query . |
|---|---|
| Step 2 | From the Filter , select Has Home Cluster Enabled and click Find . The window displays all of the end users for whom this is their Home Cluster |
| Step 3 | Click Next . In the Update Users Configuration window, the check boxes on the far left indicate whether you want to edit this setting with this query. If you don't check
                                          the left check box, the query will not update that field. The field on the right indicates the new setting for this field.
                                          If two check boxes appear, you must check the check box on the left to update the field, and in the right check box, enter
                                          the new setting. |
| Step 4 | Under Service Settings , check the left check box for each of the following fields to indicate that you want to update these fields, and then edit
                                          the adjacent field setting as follows: Home Cluster —Check the right check box to enable this cluster as the home cluster. Enable User for Unified CM IM and Presence —Check the right check box. This setting enables the central cluster as the provider of IM and Presence Service for these
                                             users. |
| Step 5 | Complete any remaining fields that you want to update. For help with the fields and their settings, see the online help: |
| Step 6 | Under Job Information , select Run Immediately . |
| Step 7 | Click Submit . |

| Step 1 | Log in to Cisco Unified CM IM and Presence Administration on the IM and Presence central cluster. |
|---|---|
| Step 2 | Upload the csv file that you exported from the telephony cluster: Choose Bulk Administration > Upload/Download Files . Click Add New . Click Choose File and select the csv file that you want to import. From the Select the Target drop-down select either of the following: Contact Lists or Non-presence Contact Lists depending on which type of contact list you are importing. From the Select Transaction Type , select the import job. Click Save . |
| Step 3 | Import the csv information into the central cluster: From Cisco Unified CM IM and Presence Administration, do either of the following: For Contact List imports, choose Bulk Administration > Contact Lists > Update Contact Lists . For Non-presence Contact List imports, choose Bulk Administration > Non-presence Contact Lists > Import Non-presence Contact Lists . From the File Name drop-down, select the csv file that you uploaded. Under Job Information , select either Run Immediately or Run Later depending on when you want the job to run. Click Submit . If you chose Run Immediately , the contact lists get imported right away Note . If you chose Run Later , you must go to Bulk Administration > Job Scheduler where you can select the job and schedule a time for it to run. | Note | . If you chose Run Later , you must go to Bulk Administration > Job Scheduler where you can select the job and schedule a time for it to run. |
| Note | . If you chose Run Later , you must go to Bulk Administration > Job Scheduler where you can select the job and schedule a time for it to run. |
| Step 4 | Repeat this procedure if you have a second csv file to import. |

| Note | . If you chose Run Later , you must go to Bulk Administration > Job Scheduler where you can select the job and schedule a time for it to run. |
|---|---|

| Step 1 | From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services . |
|---|---|
| Step 2 | From the Server drop-down, select the IM and Presence database publisher node and click Go . |
| Step 3 | Under IM and Presence Services , select the Cisco Intercluster Sync Agent and click Start . |

| Step 1 | Log in to the Cisco Unified CM Administration instance on the IM and Presence central cluster. |
|---|---|
| Step 2 | Choose System > Presence Redundancy Groups . |
| Step 3 | Click Find and select an existing subcluster. |
| Step 4 | Check the Enable High Availability check box. |
| Step 5 | Click Save . |
| Step 6 | Repeat this procedure for each subcluster in the IM and Presence central cluster. |

| Note | Removing intercluster connections can be postponed to a later date depending on the Cisco XCP Router restart availability
                                          across the entire mesh. As long as there are existing intercluster connections between telephony cluster and any number of
                                          peer clusters, currently running Cisco XCP Router services should be kept in Running state on the telephony cluster. |
|---|---|

| Step 1 | Log in to the migrating cluster's IM and Presence database publisher node. |
|---|---|
| Step 2 | From Cisco Unified CM IM and Presence Administration, choose Presence > Inter-Clustering . |
| Step 3 | Click Find and select the peer cluster. |
| Step 4 | Click Delete . |
| Step 5 | Restart the Cisco XCP Router : Log in to Unified IM and Presence Serviceability and choose Tools > Control Center - Network Services . From the Server list, choose the database publisher node and click Go . Under IM and Presence Services , select Cisco XCP Router and click Restart . |
| Step 6 | Repeat these steps on the IM and Presence Service peer cluster. Note If the migrating cluster has intercluster peer connections to multiple clusters, you must repeat this procedure for each peer
                                                      cluster that remains in the intercluster network. This means that, on the migrating cluster, there will be as many cycles
                                                      of Cisco XCP Router restarts as there are peer cluster connections that are being broken. | Note | If the migrating cluster has intercluster peer connections to multiple clusters, you must repeat this procedure for each peer
                                                      cluster that remains in the intercluster network. This means that, on the migrating cluster, there will be as many cycles
                                                      of Cisco XCP Router restarts as there are peer cluster connections that are being broken. |
| Note | If the migrating cluster has intercluster peer connections to multiple clusters, you must repeat this procedure for each peer
                                                      cluster that remains in the intercluster network. This means that, on the migrating cluster, there will be as many cycles
                                                      of Cisco XCP Router restarts as there are peer cluster connections that are being broken. |

| Note | If the migrating cluster has intercluster peer connections to multiple clusters, you must repeat this procedure for each peer
                                                      cluster that remains in the intercluster network. This means that, on the migrating cluster, there will be as many cycles
                                                      of Cisco XCP Router restarts as there are peer cluster connections that are being broken. |
|---|---|