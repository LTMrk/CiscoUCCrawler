---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-configadminguide-12-5-1-su2-cup0-b-config-and-admin-guide-1-2fbc91bba5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/configAdminGuide/12_5_1_su2/cup0_b_config-and-admin-guide-1251su2/cup0_b_config-and-admin-guide-1251su2_chapter_011010.html
retrieved_at: 2026-08-21T09:07:00.779776+00:00
---

Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU2

# Configuration and Administration of the IM and Presence Service, Release 12.5(1)SU2

Updated: November 27, 2024

Chapter: Migrate Users

## Chapter: Migrate Users

# Migrate Users

## Migrate Users Overview

This section describes how to migrate users between IM and Presence
                           Service clusters.

## Migrate Users Prerequisites

Run full backups of both the current and destination cluster. For details, see Backup the System .

Ensure that the users to be migrated are licensed for the IM and Presence Service or Cisco Jabber on their current home cluster
                                    only. If these users are licensed on any cluster other than the premigration cluster, they must be fully unlicensed before
                                    proceeding with the migration tasks.

## Migrate Users Task Flow

Complete these tasks to migrate IM and Presence users to a new cluster.

Step 1

Remove Stale Entries

Before migrating users, remove all stale rosters, group entries and non-presence contract records.

Step 2

Start Essential Services for Migration

Before migrating, confirm the following services are running:

Cisco AXL Web Service

Cisco Sync Agent

Cisco Intercluster Sync Agent

Step 3

Check for Intercluster Sync Errors

Run the System Troubleshooter and confirm that there are no intercluster sync issues.

Step 4

Configure Standard Presence for Migration

Before migrating users, configure these standard Presence settings.

Step 5

Export User Contact Lists

Complete this procedure to export the contact lists of the migrating users from their current cluster.

Step 6

Complete one of these mini-task flows to move users to the new cluster:

- Migrate Users via LDAP

- Move Users to New Cluster Manually

- Migrate Users via Bulk Administration

Step 7

Import Contact Lists on Home Cluster

After you have migrated users to the new cluster, import the contact lists to restore contact data for the
                                          migrated users.

Step 8

Update Users in Old Cluster

You may not want to remove users from the old cluster until after you confirm that everything is working fine in the new cluster.
                                          Use this procedure to use Bulk Administration's Update Users feature to remove IM and Presence functionality from the old
                                          cluster.

### Remove Stale Entries

Before migrating users, remove stale rosters, group entries and non-presence contact records. This is to be done on the publisher
                                 IM&P node from which the users had presence disabled.

Repeat these steps as necessary in batches of 2000. If it is too time consuming to remove a large amount of stale entries
                                             via CLI, open a TAC case to leverage the stale roster script at the end of this section that requires root access.

Step 1

Start the CLI session. For details on how to start a CLI session, refer to the "Start CLI session" section of the Command Line Interface Reference Guide for Cisco Unified Communications Solutions .

Step 2

Check and remove stale roster entries. To do this, run the following queries:

Check for stale roster entries:

```
run sql select count(*) from rosters where user_id in (select xcp_user_id from enduser where primarynodeid is NULL)
```

Remove stale roster entries:

```
run sql delete from rosters where pkid in (select * from (select first 2000 pkid from rosters where user_id in (select xcp_user_id from enduser where primarynodeid is NULL)))
```

Step 3

Check and remove stale group records. To do this, run the following queries:

Check for stale group records:

```
run sql select count(*) from groups where user_id in (select xcp_user_id from enduser where primarynodeid is NULL)
```

Remove stale group records:

```
run sql delete from groups where pkid in (select * from (select first 2000 pkid from groups where user_id in (select xcp_user_id from enduser where primarynodeid is NULL)))
```

Step 4

Check and remove stale non-contact records (in order). To do this, run the following queries:

Check for stale non-contact records (in order):

```
run sql select count(*) from nonpresencecontacts where fkenduser in (select pkid from enduser where primarynodeid is null)
```

Remove stale non-contact records (in order):

```
run sql delete from nonpresencecontacts where pkid in (select * from (select first 2000 pkid from nonpresencecontacts where fkenduser in (select pkid from enduser where primarynodeid is null)))
```

Use this query if you have root access:

```
run sql delete from epascontactaddinfo where pkid in (select * from (select first 2000 pkid from epascontactaddinfo where pkid not in (select fkepascontactaddinfo from nonpresencecontacts)))
```

### Configure Standard Presence for Migration

Before migrating users, configure these Presence settings.

Step 1

From Cisco Unified CM IM and Presence Administration, choose Presence > Settings > Standard Configuration .

Step 2

Check the Allow users to view the availability of other users without being prompted for approval check box.

Step 3

For the Maximum Contact List Size (per user) setting, check the No Limit check box.

Step 4

For the Maximum Watchers (per user) setting, check the No Limit check box

Step 5

Click Save .

#### What to do next

Check for Intercluster Sync Errors

### Check for Intercluster Sync Errors

Before migrating, confirm that there are no intercluster sync errors.

Step 1

From Cisco Unified CM IM and Presence Administration, choose Diagnostics > System Troubleshooter .

Step 2

Confirm that there are no intercluster sync errors. If there are errors, fix them before proceeding.

#### What to do next

Start Essential Services for Migration

### Start Essential Services for Migration

In Cisco Unified IM and Presence Serviceability, confirm that the following essential services for the migration are running:

Cisco AXL Web Service

Cisco Sync Agent

Cisco Intercluster Sync Agent

Step 1

From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services.

Step 2

From the Server drop-down select your IM and Presence node and click Go .

Step 3

Under Database and Admin Services , confirm that the Cisco AXL Web Service is Started. If the service is not running (the default setting is not running), select the service and click Start .

Step 4

Choose Tools > Control Center - Network Services .

Step 5

From the Server drop-down select your IM and Presence node and click Go .

Step 6

Under IM and Presence Services , confirm that both the Cisco Sync Agent and Cisco Intercluster Sync Agent services are running. If they are  not running, Start them.

#### What to do next

Export User Contact Lists

### Export User Contact Lists

Complete this procedure to export the contact lists of the migrating users from their current cluster.

Step 1

Export the contact lists of the migrating users from the current
                                          home cluster.

In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Contact List > Export .

Choose All unassigned users in the cluster and click Find .

Review the results and use the AND/OR filter to filter the search
                                                results as required.

When the list is complete, click Next .

Choose a filename for the exported contact list data.

Optionally update the Job Description.

Click Run Now or schedule the job to run later.

Step 2

Monitor the status of the contact list export job.

In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Job Scheduler .

Click Find to list all BAT jobs.

Find your contact list export job and when it is reported as
                                                completed, choose the job.

Choose the CSV File Name link to view the contents of the contact list export file. A time stamp is appended to the filename.

From the Job Results section, choose the log file to see a summary of what was uploaded. The log file includes the start and end time and result
                                                summary for the job.

Step 3

Download the contact list export file and store it for use later
                                          when the user migration is complete.

In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Upload/Download Files .

Click Find .

Choose the contact list export file and click Download Selected .

Save the CSV file locally for upload later in the procedure.

#### What to do next

Go to one of the following task flows to assign users in the new cluster:

Migrate Users via LDAP

Move Users to New Cluster Manually

### Migrate  Users via LDAP

Complete these tasks if your users are synced with an LDAP Directory and you want to migrate to a new cluster.

You must add your LDAP Directory configuration into the new cluster. This includes any service profiles, user profiles, and
                                             feature group templates. Make sure that your feature group template configuration has the Enable Users for Unified CM IM and Presence check box checked.

Step 1

Update External LDAP Directory

You may need to update your external LDAP directory if your deployment uses a separate LDAP structure for each cluster and
                                             where users are synchronized only to their home cluster.

Step 2

Configure LDAP in New Cluster

If LDAP is enabled on Cisco Unified Communications Manager, import users to your new cluster by synchronizing your new cluster
                                             with the updated LDAP directory.

#### What to do next

Import Contact Lists on Home Cluster

#### Update External LDAP Directory

You may need to update your external LDAP directory if your deployment uses a separate LDAP structure  for each cluster and
                                    where users are synchronized only to their home cluster.

You do not need to move the users if the deployment uses a flat
                                                LDAP structure, that is, all users are synchronized to all Cisco
                                                Unified Communications Manager and IM and Presence Service clusters
                                                where users are licensed to only one cluster.

Depending on how you have your LDAP Directory sync configured in the old and new cluster, moving your users within the external
                                                LDAP Directory may automatically migrate those users to the new IM and Presence Service cluster when the next sync occurs.

Step 1

Update users in your external LDAP directory.

Step 2

After you move the users, delete the LDAP entries from the old LDAP cluster.

##### What to do next

Configure LDAP in New Cluster

#### Configure LDAP in New Cluster

##### Before you begin

Provision the LDAP directory in your new
                                    cluster. If your LDAP directory sync includes universal line and
                                    device templates, and feature group templates, you must configure
                                    these templates in your new cluster. Make sure that your feature group template has the following options checked:

Home Cluster

Enable Users for Unified CM IM and Presence

For details on how to configure an LDAP
                                    directory sync, refer to the "Configure End Users" section of the System Configuration Guide for Cisco Unified Communications
                                       Manager .

Step 1

From Cisco Unified CM Administration, choose System > LDAP > LDAP Directory .

Step 2

Click Find and select the LDAP Directory that you've configured

Step 3

Click Perform Full Sync Now .

##### What to do next

Import Contact Lists on Home Cluster

### Move Users to New Cluster Manually

Complete these tasks to move a user to the new cluster manually.

If you have a large number of users, you may want to use the Bulk Administration Tool in Cisco Unified Communications Manager
                                             to update a large number of users via a csv file. For details, see the Bulk Administration Guide for Cisco Unified Communications Manager .

Step 1

Disable IM and Presence For User Manually

Disable a migrating user for IM and Presence Service and Cisco Jabber on their current home cluster.

Step 2

Import Users Manually

If LDAP synchronization is not configured in the new cluster, provision  users manually to your new Cisco Unified Communications
                                             Manager cluster.

Step 3

Enable Users for IM and Presence Service on New Cluster

When the users have been synchronized, or manually provisioned, on the new home cluster, you must enable the users for IM
                                             and Presence Service and Cisco Jabber.

#### What to do next

Import Contact Lists on Home Cluster

#### Disable IM and Presence For User Manually

The following procedure describes how to disable a migrating user
                                    for IM and Presence Service and Cisco Jabber on their current home
                                    cluster.

##### Before you begin

Export User Contact Lists

Step 1

In Cisco Unified CM Administration , choose > User Management > End User .

Step 2

Use the filters to find the user that you want to disable for IM
                                             and Presence Service.

Step 3

In the End User Configuration screen, uncheck Enable User for
                                                Unified CM IM and Presence .

Step 4

Click Save .

##### What to do next

Import Users Manually

#### Import Users Manually

If LDAP synchronization is not configured in the new cluster, import users manually to your new Cisco Unified Communications
                                    Manager cluster.

For details, see Configure User Settings .

##### What to do next

#### Enable Users for IM and Presence Service on New Cluster

When the users have been synchronized, or manually provisioned, on
                                    the new home cluster, you must enable the users for IM and Presence
                                    Service and Cisco Jabber.

Step 1

In Cisco Unified CM Administration , choose User Management > End User .

Step 2

Use the filters to find the user that you want to enable for IM and
                                             Presence Service.

Step 3

In the End User Configuration screen, check Enable User for Unified
                                                CM IM and Presence .

Step 4

Click Save .

Step 5

Provision the users on Cisco Unified Communications Manager for Phone and CSF. See the Administration Guide for Cisco Unified Communications Manager for more information.

##### What to do next

Import Contact Lists on Home Cluster

### Migrate Users via Bulk Administration

Move the users to a new cluster via the Bulk Administration Tool (for example, migrating from cluster 1 to cluster 2).

#### Before you begin

The Cisco Bulk Provisioning Service must be running in both clusters.

If the number of users to be moved from source to destination in IM and Presence cluster are less than 100 then, do not start
                                             or stop Cisco Intercluster Sync Agent service.

If you are moving 100 to 1,000 users from any source / destination cluster perform the below steps by stopping Intercluster
                                             Sync Agent service on both source and destination clusters.

If the number of users to be moved are more than 1000, For example, if we have to move 16K users then first move 8K users
                                             by following below steps and stop the Intercluster Sync Agent service while moving users in chunks of 1K users. Later move
                                             the next 8K in a balanced and serial sequence in chunks of 1K users.

On the IM and Presence cluster where the users are being moved from source:

Step 1 On the associated subscriber node of the IM and Presence publisher's Presence Redundancy Group (PRG) pair                
                                 stop Intercluster Sync Agent service.

Step  2 On the publisher node of the publisher IM and Presence Presence Redundancy Group pair stop Intercluster                  
                                 Sync Agent service.

On the IM and Presence cluster where the users are being moved from destination:

Step 3 On the secondary node of the publisher Presence Redundancy Group pair stop Intercluster Sync Agent service.

Step 4 On the publisher node of the publisher Presence Redundancy Group pair stop Intercluster Sync Agent service.

Step 5 Peform the steps mentioned in Migrate Users via Bulk Administration.

Step 6 Start the Intercluster Sync Agent service on the IM and Presence publisher and subscriber nodes on both                  
                                 destination and source clusters.

Step 7 It can take up to 30 minutes for all other clusters to complete their sync with the destination cluster.

Step 1

Export Users to CSV File

In the original cluster (cluster 1) export the migrating users to a CSV file.

Step 2

Download CSV Export File

Download the CSV export file.

Step 3

Upload CSV Export File to New Cluster

Upload the CSV file to the destination cluster (cluster 2).

Step 4

Configure User Template

In the destination cluster, configure a User Template with the user settings.

Step 5

Import Users to New Cluster

Use the Insert Users menu in Bulk Administration to import users from the CSV file.

Step 6

Verify User Migration via Bulk Administration

Verify the user migration via bulk administration.

#### Export Users to CSV File

In the original cluster, use the Bulk Administration Tool to export the users whom you want to migrate to a CSV file.

Note: After the job runs, you can go to the Job Scheduler to
                                    check the status of the job and confirm that the file was created.
                                    If you selected Run Later, you can use the Job Scheduler to set the
                                    time for the job to run.

Step 1

From Cisco Unified CM Administration, choose Bulk Administration > Users > Export Users .

Step 2

Use the Filter tools to search for and select the users whom you
                                             want to migrate and click Find .

Step 3

Click Next .

Step 4

Enter a File Name for the file.

Step 5

From the File Format drop-down, select the format of the export file.

Step 6

To run the job right away, select Run Immediately and click Submit .

##### What to do next

After the job runs, you can go to the Job Scheduler to check the status of the job and confirm that the file was created. If you selected Run Later , you can use the Job Scheduler to set the time for the job to run.

Once you have confirmed that the file was created, Download CSV Export File .

#### Download CSV Export File

Once you have confirmed that the export file was created, download the file.

Step 1

From Cisco Unified CM Administration, choose Bulk Administration > Upload/Download Files .

Step 2

Click Find .

Step 3

Select the file that was created and click Download
                                                Selected .

Step 4

Download the file.

##### What to do next

Upload CSV Export File to New Cluster

#### Upload CSV Export File to New Cluster

In the destination cluster (cluster 2), upload the csv file that you exported from cluster 1.

Step 1

From Cisco Unified CM Administration, choose Bulk Administration > Upload/Download Files .

Step 2

Click Add New .

Step 3

Click Choose File . Browse and select the export file from the other
                                             system.

Step 4

From the Target drop-down, select the Bulk Administration menu that you want to use to import the file contents. For example, Users or Phones and Users .

Step 5

From the Transaction Type drop-down, select the submenu that you want to use to import the file contents. For example, Insert Users or Insert Phones/Users .

Step 6

Click Save

##### What to do next

Configure User Template

#### Configure User Template

In the destination cluster, configure a user template with the settings that you want to apply to imported users.

Step 1

From Cisco Unified CM Administration choose Bulk Administration > Users > User Templates .

Step 2

Do either of the following:

- Click Find and select an existing template.

- Click Add New to create a new template.

Step 3

Configure the user settings that you want to apply to your
                                             imported users. For example, make sure that the following fields
                                             are checked

- Home Cluster

- Enable User for Unified CM IM and Presence

Step 4

If you want users to be enabled for calendar integration with
                                             Microsoft Outlook, check the Include meeting information in
                                                Presence check box .

Step 5

Configure any remaining fields.

Step 6

Click Save .

##### What to do next

Import Users to New Cluster

#### Import Users to New Cluster

Use Bulk Administration's Insert Users menu to import the
                                    exported users into the new Cluster.

Step 1

From Cisco Unified CM Administration, choose Bulk Administration > Users > Insert Users .

Step 2

From File Name , select the file that was exported from the other
                                             system.

Step 3

From the User Template Name , select the user template that you
                                             just created.

Step 4

Check the File created with Export Users check box.

Step 5

Check Run Immediately and click Submit .

##### What to do next

Import Contact Lists on Home Cluster

#### Verify User Migration via Bulk Administration

After migrating users via Bulk Administration and starting Cisco Intercluster Sync Agent Services on the source and destination
                                    clusters, it is necessary to verify that other clusters than source and destination clusters received notifications that user
                                    move has been occurred.

It can take up to 30 minutes for all other clusters to complete their sync with the destination cluster. While you wait, you
                                    can open a terminal session to sample (5) IMP publishers in parallel that are not part of the change (source or destination)
                                    to monitor the CiscoSyslogs.

Step 1

Run the below command to observe if the sample IMP publisher node has already completed its sync after migrating users via
                                             Bulk Administration and starting Cisco Intercluster Sync Agent Services on the source and destination clusters. Notify the
                                             timestamp for this moment. In the following example syntax, the destination cluster name is dst-name. Replace this with your
                                             destination cluster name.

```
admin:file search activelog syslog/CiscoSyslog ".*InterClusterSyncAgentStatus:.*dst-name.*"
```

Step 2

If the time stamp in the ICSA status is not more recent than the timestamp recorded, then use the following command for up
                                             to 30 minutes for a successful sync:

```
admin:file tail activelog syslog/CiscoSyslog regexp ".*InterClusterSyncAgentStatus:.*dst-name.*"
```

If you see an ICSA failed sync status alarm on the selected sample cluster/node, wait for 5-10 minutes for a successful sync
                                                status alarm. ICSA will retry every 5 minutes. If you do not have a successful sync alarm or have consistent sync failures,
                                                please open a TAC case.

At this point you have verified the 5 remote sample clusters if the current time is 30 minutes later than timestamp recorded
                                                after migrating users via Bulk Administration and starting Cisco Intercluster Sync Agent Services on source and destination
                                                clusters. You can now proceed to the next move process or if there no other moves, you are finished.

### Import Contact Lists on Home Cluster

After you have migrated users to the new cluster, import the contact lists to restore contact data for the
                                 migrated users.

Step 1

Upload the previously exported contact list CSV file.

In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Upload/Download Files .

Click Add New .

Click Browse to locate and choose the contact list CSV file.

Choose Contact Lists as the Target.

Choose Import Users' Contacts - Custom File as the Transaction
                                                Type.

Optionally check Overwrite File if it exists .

Click Save to upload the file.

Click Save to upload the file.

Step 2

Run the import contact list job.

In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Contact List > Update .

Choose the CSV file you uploaded in Step 1.

Optionally update the Job Description.

To run the job now, click Run Immediately . Click Run Later to
                                                schedule the update for a later time.

Click Submit .

Step 3

Monitor the contact list import status

In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Contact List > Job Scheduler .

Click Find to list all BAT jobs.

Choose the job ID of the contact list import job when its status is
                                                reported as complete.

To view the contents of the contact list file, choose the file
                                                listed at CSV File Name .

Click the Log File Name link to open the log.

The begin time and end time of the job is listed and a result summary is
                                                   also displayed.

### Update Users in Old Cluster

You may not want to remove users from the old cluster until after you confirm that everything is working fine in the new cluster.
                                 Use this procedure to use Bulk Administration's Update Users feature to remove IM and Presence functionality from the old
                                 cluster.

Step 1

From Cisco Unified CM Administration, choose Bulk Administration > Users > Update Users > Query .

Step 2

Use the Filter tools to search for the migrating users. For
                                          example, you can search for all users whom meet this condition: Has
                                             IM and Presence Enabled .

Step 3

Click Next

Step 4

For each of the following two fields, check the far left box and leave the adjacent box on the right unchecked. The left
                                          box indicates that you want to update the field and the right box indicates the new setting: unchecked.

- Home Cluster

- Enable User for Unified CM IM and Presence

Step 5

Under Job Information , select Run Immediately .

Step 6

Click Submit .

#### What to do next

Once you are confident that the migration worked, and that all users are configured properly in the new cluster, you can delete
                                 migrated users in the old cluster.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Remove Stale Entries | Before migrating users, remove all stale rosters, group entries and non-presence contract records. |
| Step 2 | Start Essential Services for Migration | Before migrating, confirm the following services are running: Cisco AXL Web Service Cisco Sync Agent Cisco Intercluster Sync Agent |
| Step 3 | Check for Intercluster Sync Errors | Run the System Troubleshooter and confirm that there are no intercluster sync issues. |
| Step 4 | Configure Standard Presence for Migration | Before migrating users, configure these standard Presence settings. |
| Step 5 | Export User Contact Lists | Complete this procedure to export the contact lists of the migrating users from their current cluster. |
| Step 6 | Complete one of these mini-task flows to move users to the new cluster: Migrate Users via LDAP Move Users to New Cluster Manually Migrate Users via Bulk Administration | Move users to the new cluster. You can use LDAP to provision users in the new cluster, move users manually, or use Bulk Administration
                                       to migrate users to the new cluster. |
| Step 7 | Import Contact Lists on Home Cluster | After you have migrated users to the new cluster, import the contact lists to restore contact data for the
                                          migrated users. |
| Step 8 | Update Users in Old Cluster | You may not want to remove users from the old cluster until after you confirm that everything is working fine in the new cluster.
                                          Use this procedure to use Bulk Administration's Update Users feature to remove IM and Presence functionality from the old
                                          cluster. |

| Note | Repeat these steps as necessary in batches of 2000. If it is too time consuming to remove a large amount of stale entries
                                             via CLI, open a TAC case to leverage the stale roster script at the end of this section that requires root access. |
|---|---|

| Step 1 | Start the CLI session. For details on how to start a CLI session, refer to the "Start CLI session" section of the Command Line Interface Reference Guide for Cisco Unified Communications Solutions . |
|---|---|
| Step 2 | Check and remove stale roster entries. To do this, run the following queries: Check for stale roster entries: run sql select count(*) from rosters where user_id in (select xcp_user_id from enduser where primarynodeid is NULL) Remove stale roster entries: run sql delete from rosters where pkid in (select * from (select first 2000 pkid from rosters where user_id in (select xcp_user_id from enduser where primarynodeid is NULL))) |
| Step 3 | Check and remove stale group records. To do this, run the following queries: Check for stale group records: run sql select count(*) from groups where user_id in (select xcp_user_id from enduser where primarynodeid is NULL) Remove stale group records: run sql delete from groups where pkid in (select * from (select first 2000 pkid from groups where user_id in (select xcp_user_id from enduser where primarynodeid is NULL))) |
| Step 4 | Check and remove stale non-contact records (in order). To do this, run the following queries: Check for stale non-contact records (in order): run sql select count(*) from nonpresencecontacts where fkenduser in (select pkid from enduser where primarynodeid is null) Remove stale non-contact records (in order): run sql delete from nonpresencecontacts where pkid in (select * from (select first 2000 pkid from nonpresencecontacts where fkenduser in (select pkid from enduser where primarynodeid is null))) Use this query if you have root access: run sql delete from epascontactaddinfo where pkid in (select * from (select first 2000 pkid from epascontactaddinfo where pkid not in (select fkepascontactaddinfo from nonpresencecontacts))) |

| Step 1 | From Cisco Unified CM IM and Presence Administration, choose Presence > Settings > Standard Configuration . |
|---|---|
| Step 2 | Check the Allow users to view the availability of other users without being prompted for approval check box. |
| Step 3 | For the Maximum Contact List Size (per user) setting, check the No Limit check box. |
| Step 4 | For the Maximum Watchers (per user) setting, check the No Limit check box |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM IM and Presence Administration, choose Diagnostics > System Troubleshooter . |
|---|---|
| Step 2 | Confirm that there are no intercluster sync errors. If there are errors, fix them before proceeding. |

| Step 1 | From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services. |
|---|---|
| Step 2 | From the Server drop-down select your IM and Presence node and click Go . |
| Step 3 | Under Database and Admin Services , confirm that the Cisco AXL Web Service is Started. If the service is not running (the default setting is not running), select the service and click Start . |
| Step 4 | Choose Tools > Control Center - Network Services . |
| Step 5 | From the Server drop-down select your IM and Presence node and click Go . |
| Step 6 | Under IM and Presence Services , confirm that both the Cisco Sync Agent and Cisco Intercluster Sync Agent services are running. If they are  not running, Start them. |

| Step 1 | Export the contact lists of the migrating users from the current
                                          home cluster. In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Contact List > Export . Choose All unassigned users in the cluster and click Find . Review the results and use the AND/OR filter to filter the search
                                                results as required. When the list is complete, click Next . Choose a filename for the exported contact list data. Optionally update the Job Description. Click Run Now or schedule the job to run later. |
|---|---|
| Step 2 | Monitor the status of the contact list export job. In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Job Scheduler . Click Find to list all BAT jobs. Find your contact list export job and when it is reported as
                                                completed, choose the job. Choose the CSV File Name link to view the contents of the contact list export file. A time stamp is appended to the filename. From the Job Results section, choose the log file to see a summary of what was uploaded. The log file includes the start and end time and result
                                                summary for the job. |
| Step 3 | Download the contact list export file and store it for use later
                                          when the user migration is complete. In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Upload/Download Files . Click Find . Choose the contact list export file and click Download Selected . Save the CSV file locally for upload later in the procedure. |

| Note | You must add your LDAP Directory configuration into the new cluster. This includes any service profiles, user profiles, and
                                             feature group templates. Make sure that your feature group template configuration has the Enable Users for Unified CM IM and Presence check box checked. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Update External LDAP Directory | You may need to update your external LDAP directory if your deployment uses a separate LDAP structure for each cluster and
                                             where users are synchronized only to their home cluster. |
| Step 2 | Configure LDAP in New Cluster | If LDAP is enabled on Cisco Unified Communications Manager, import users to your new cluster by synchronizing your new cluster
                                             with the updated LDAP directory. |

| Note | You do not need to move the users if the deployment uses a flat
                                                LDAP structure, that is, all users are synchronized to all Cisco
                                                Unified Communications Manager and IM and Presence Service clusters
                                                where users are licensed to only one cluster. |
|---|---|

| Note | Depending on how you have your LDAP Directory sync configured in the old and new cluster, moving your users within the external
                                                LDAP Directory may automatically migrate those users to the new IM and Presence Service cluster when the next sync occurs. |
|---|---|

| Step 1 | Update users in your external LDAP directory. |
|---|---|
| Step 2 | After you move the users, delete the LDAP entries from the old LDAP cluster. |

| Step 1 | From Cisco Unified CM Administration, choose System > LDAP > LDAP Directory . |
|---|---|
| Step 2 | Click Find and select the LDAP Directory that you've configured |
| Step 3 | Click Perform Full Sync Now . |

| Note | If you have a large number of users, you may want to use the Bulk Administration Tool in Cisco Unified Communications Manager
                                             to update a large number of users via a csv file. For details, see the Bulk Administration Guide for Cisco Unified Communications Manager . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Disable IM and Presence For User Manually | Disable a migrating user for IM and Presence Service and Cisco Jabber on their current home cluster. |
| Step 2 | Import Users Manually | If LDAP synchronization is not configured in the new cluster, provision  users manually to your new Cisco Unified Communications
                                             Manager cluster. |
| Step 3 | Enable Users for IM and Presence Service on New Cluster | When the users have been synchronized, or manually provisioned, on the new home cluster, you must enable the users for IM
                                             and Presence Service and Cisco Jabber. |

| Note | If you are migrating a large number of users at once, you may want to use the Bulk Administration Tool in Cisco Unified Communications
                                             Manager. For details, see the Bulk Administration Guide for Cisco
                                                Unified Communications Manager . |
|---|---|

| Step 1 | In Cisco Unified CM Administration , choose > User Management > End User . |
|---|---|
| Step 2 | Use the filters to find the user that you want to disable for IM
                                             and Presence Service. |
| Step 3 | In the End User Configuration screen, uncheck Enable User for
                                                Unified CM IM and Presence . |
| Step 4 | Click Save . |

| Step 1 | In Cisco Unified CM Administration , choose User Management > End User . |
|---|---|
| Step 2 | Use the filters to find the user that you want to enable for IM and
                                             Presence Service. |
| Step 3 | In the End User Configuration screen, check Enable User for Unified
                                                CM IM and Presence . |
| Step 4 | Click Save . |
| Step 5 | Provision the users on Cisco Unified Communications Manager for Phone and CSF. See the Administration Guide for Cisco Unified Communications Manager for more information. |

| Note | If the number of users to be moved from source to destination in IM and Presence cluster are less than 100 then, do not start
                                             or stop Cisco Intercluster Sync Agent service. If you are moving 100 to 1,000 users from any source / destination cluster perform the below steps by stopping Intercluster
                                             Sync Agent service on both source and destination clusters. If the number of users to be moved are more than 1000, For example, if we have to move 16K users then first move 8K users
                                             by following below steps and stop the Intercluster Sync Agent service while moving users in chunks of 1K users. Later move
                                             the next 8K in a balanced and serial sequence in chunks of 1K users. |
|---|---|

| Note | No other cluster nodes require Intercluster Sync Agent service to be stopped. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Export Users to CSV File | In the original cluster (cluster 1) export the migrating users to a CSV file. |
| Step 2 | Download CSV Export File | Download the CSV export file. |
| Step 3 | Upload CSV Export File to New Cluster | Upload the CSV file to the destination cluster (cluster 2). |
| Step 4 | Configure User Template | In the destination cluster, configure a User Template with the user settings. |
| Step 5 | Import Users to New Cluster | Use the Insert Users menu in Bulk Administration to import users from the CSV file. |
| Step 6 | Verify User Migration via Bulk Administration | Verify the user migration via bulk administration. |

| Step 1 | From Cisco Unified CM Administration, choose Bulk Administration > Users > Export Users . |
|---|---|
| Step 2 | Use the Filter tools to search for and select the users whom you
                                             want to migrate and click Find . |
| Step 3 | Click Next . |
| Step 4 | Enter a File Name for the file. The tool appends the .txt extension to the end of your file. For example, <csvfilename>.txt . |
| Step 5 | From the File Format drop-down, select the format of the export file. |
| Step 6 | To run the job right away, select Run Immediately and click Submit . |

| Step 1 | From Cisco Unified CM Administration, choose Bulk Administration > Upload/Download Files . |
|---|---|
| Step 2 | Click Find . |
| Step 3 | Select the file that was created and click Download
                                                Selected . |
| Step 4 | Download the file. |

| Step 1 | From Cisco Unified CM Administration, choose Bulk Administration > Upload/Download Files . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Click Choose File . Browse and select the export file from the other
                                             system. |
| Step 4 | From the Target drop-down, select the Bulk Administration menu that you want to use to import the file contents. For example, Users or Phones and Users . |
| Step 5 | From the Transaction Type drop-down, select the submenu that you want to use to import the file contents. For example, Insert Users or Insert Phones/Users . |
| Step 6 | Click Save |

| Step 1 | From Cisco Unified CM Administration choose Bulk Administration > Users > User Templates . |
|---|---|
| Step 2 | Do either of the following: Click Find and select an existing template. Click Add New to create a new template. |
| Step 3 | Configure the user settings that you want to apply to your
                                             imported users. For example, make sure that the following fields
                                             are checked Home Cluster Enable User for Unified CM IM and Presence |
| Step 4 | If you want users to be enabled for calendar integration with
                                             Microsoft Outlook, check the Include meeting information in
                                                Presence check box . |
| Step 5 | Configure any remaining fields. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Bulk Administration > Users > Insert Users . |
|---|---|
| Step 2 | From File Name , select the file that was exported from the other
                                             system. |
| Step 3 | From the User Template Name , select the user template that you
                                             just created. |
| Step 4 | Check the File created with Export Users check box. |
| Step 5 | Check Run Immediately and click Submit . |

| Step 1 | Run the below command to observe if the sample IMP publisher node has already completed its sync after migrating users via
                                             Bulk Administration and starting Cisco Intercluster Sync Agent Services on the source and destination clusters. Notify the
                                             timestamp for this moment. In the following example syntax, the destination cluster name is dst-name. Replace this with your
                                             destination cluster name. admin:file search activelog syslog/CiscoSyslog ".*InterClusterSyncAgentStatus:.*dst-name.*" |
|---|---|
| Step 2 | If the time stamp in the ICSA status is not more recent than the timestamp recorded, then use the following command for up
                                             to 30 minutes for a successful sync: admin:file tail activelog syslog/CiscoSyslog regexp ".*InterClusterSyncAgentStatus:.*dst-name.*" If you see an ICSA failed sync status alarm on the selected sample cluster/node, wait for 5-10 minutes for a successful sync
                                                status alarm. ICSA will retry every 5 minutes. If you do not have a successful sync alarm or have consistent sync failures,
                                                please open a TAC case. At this point you have verified the 5 remote sample clusters if the current time is 30 minutes later than timestamp recorded
                                                after migrating users via Bulk Administration and starting Cisco Intercluster Sync Agent Services on source and destination
                                                clusters. You can now proceed to the next move process or if there no other moves, you are finished. |

| Step 1 | Upload the previously exported contact list CSV file. In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Upload/Download Files . Click Add New . Click Browse to locate and choose the contact list CSV file. Choose Contact Lists as the Target. Choose Import Users' Contacts - Custom File as the Transaction
                                                Type. Optionally check Overwrite File if it exists . Click Save to upload the file. Click Save to upload the file. |
|---|---|
| Step 2 | Run the import contact list job. In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Contact List > Update . Choose the CSV file you uploaded in Step 1. Optionally update the Job Description. To run the job now, click Run Immediately . Click Run Later to
                                                schedule the update for a later time. Click Submit . |
| Step 3 | Monitor the contact list import status In Cisco Unified CM IM and Presence Administration , choose Bulk Administration > Contact List > Job Scheduler . Click Find to list all BAT jobs. Choose the job ID of the contact list import job when its status is
                                                reported as complete. To view the contents of the contact list file, choose the file
                                                listed at CSV File Name . Click the Log File Name link to open the log. The begin time and end time of the job is listed and a result summary is
                                                   also displayed. |

| Step 1 | From Cisco Unified CM Administration, choose Bulk Administration > Users > Update Users > Query . |
|---|---|
| Step 2 | Use the Filter tools to search for the migrating users. For
                                          example, you can search for all users whom meet this condition: Has
                                             IM and Presence Enabled . |
| Step 3 | Click Next |
| Step 4 | For each of the following two fields, check the far left box and leave the adjacent box on the right unchecked. The left
                                          box indicates that you want to update the field and the right box indicates the new setting: unchecked. Home Cluster Enable User for Unified CM IM and Presence |
| Step 5 | Under Job Information , select Run Immediately . |
| Step 6 | Click Submit . |