---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-database-setup-12-5-1-cup0-b-database-setup-guide-1251su1-c-7b6288ea99
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/database_setup/12_5_1/cup0_b_database-setup-guide-1251su1/cup0_m_manage-external-database.html
retrieved_at: 2026-08-16T16:51:04.334416+00:00
---

Database Setup Guide for the IM and Presence Service, Release 12.5(1)SU1

# Database Setup Guide for the IM and Presence Service, Release 12.5(1)SU1

Updated: January 8, 2025

Chapter: Database Administration

## Chapter: Database Administration

# Database Administration

## External Database Cleanup Utility

The External Database Cleanup Utility makes it easy for administrators to manage external database growth, thereby ensuring
                              that your system continues to perform at the optimum level. The utility lets you create jobs that monitor the external database
                              on an ongoing basis, deleting old records automatically as they expire. This ensures that the external database has adequate
                              space and that system performance is not impacted by  unchecked database growth.

The External Database Cleanup Utility can delete chat messages records, but cannot delete the entire persistent chat rooms
                                          records.

The External Database Cleanup Utility can be used to manage external database growth for the following IM and Presence Service
                              features, each of which relies on the external database:

Persistent Chat High Availability

Managed File Transfer

Message Archiver

### Interactions

The following interactions apply:

Records that are deleted from the database are deleted without
                                    archiving.

You can run the Database Cleanup utility in offline mode.

A persistent chat room configuration option is provided to override the clusterwide setting for retention durations. This
                                    allows chat room owners to customize the settings within a controlled range. This depends on the Cisco Jabber client changes
                                    to enable this menu option.

### Stored Procedures

The External Database Cleanup Utility uses the following stored procedures to delete records:

tc_msgarchive_auto_cleanup

tc_timelog_auto_cleanup

aft_log_auto_cleanup

im_auto_cleanup

### Run the External Database Cleanup Utility [For Releases upto 15SU2]

Use this procedure to run the External Database Cleanup Utility to delete expired records from the external database. You
                                 can run a manual cleanup to complete a one-time deletion of records from the database or you can configure the system to monitor
                                 and delete records from the external database automatically.

Step 1

Log into Cisco Unified CM IM and Presence Administration on the database publisher node.

Step 2

Choose Messaging > External Server Setup > External Database Jobs .

Step 3

Click Clear External DB .

Step 4

Do one of the following:

- For manual cleanup of an external database that connects to the publisher node, select Same Cup Node .

- For manual cleanup of an external database that connects to a subscriber node, select Other Cup Node and then select the external database details.

- If you are configuring the system to monitor and clean the external database automatically, check the Automatic Clean-up radio button.

We recommend that you run a manual cleanup prior to setting up the automatic cleanup.

Step 5

Set the Number of Days that you want to go back for file deletion. For example, if you enter 90, the system deletes records that are older than
                                          90 days.

Step 6

Click Update Schema to create the Indexes and stored procedures for the database.

Step 7

Set the Number of Days that you want to go back for file deletion. For example, if you enter 90 , the system deletes records that are older than 90 days.

Step 8

In the Feature Tables section, select each feature for which you want to clean records:

- Text Conference (TC) —Select this option to clean database tables for the Persistent Chat feature.

- Message Archiver (MA) —Select this option to clean database tables for the Message Archiver feature.

- Managed File Transfer (MFT) —Select this option to clean database tables for the Managed File Transfer feature

Step 9

Click Submit Clean-up Job .

If you have the Automatic option enabled, and you want to disable it, click the Disable Automatic Clean-up Job button.

#### What to do next

If you just ran a manual cleanup, repeat the procedure and select Automatic Clean-up to set the utility to monitor and delete records automatically.

### Troubleshooting the External Database Cleanup Utility

If you run into issues with the external database utility:

Make sure that the database publisher node can connect to the
                                       external database and that the database has been provisioned. You can verify this on the database publisher node  by selecting Messaging > External Server
                                             Setup > External Databases > External DB Configuration .

For PostgreSQL databases, make sure that the IM and Presence
                                       database publisher node has full access permission to all of the
                                       other configured external databases.

Logs for the External Database Cleanup Tool are available under
                                 admin logs: /var/log/active/tomcat/logs/cupadmin/log4j/

## Merge External Databases

Use this procedure to merge external databases.

Microsoft SQL database is not supported for merging external databases.

Optional. If you have upgraded from a release prior to 11.5(1), and multiple external databases were used to manage redundancy,
                              use the External Database Merge Tool to merge your external databases into a single database.

Example

If you have upgraded from a release prior to 11.5(1), and you had persistent chat configured with each persistent chat node
                              connecting to a separate external database instance, use this procedure to merge the two databases in a subcluster into a
                              single database that connects to both nodes.

### Before you begin

Ensure that the two source destination databases are assigned correctly to each IM and Presence Service node in the presence
                                    redundancy group. This verifies that both of their schemas are valid.

Back up the tablespace of the destination database.

Ensure that there is enough space in the destination database for
                                    the new merged databases.

Ensure that the database users, created for the source and
                                    destination databases, have the permissions to run these commands:

CREATE TABLE

CREATE PUBLIC DATABASE LINK

If your database users do not have these permissions, you can use
                                    these commands to grant them:

PostgreSQL:

CREATE EXTENTION —This creates the dblink and requires super user or dbowner privileges. After this, you EXECUTE privilege for dblink by running
                                          following:

GRANT EXECUTE ON FUNCTION DBLINK_CONNECT(text) to <user>

GRANT EXECUTE ON FUNCTION DBLINK_CONNECT(text,text) to <user>

Oracle:

GRANT CREATE TABLE TO <user_name>;

GRANT CREATE PUBLIC DATABASE LINK TO <user_name>;

If you are using a PostgreSQL external database, make sure that the following access is configured in the pg_hba.conf file:

The IM and Presence publisher node must  have full access to each external database.

The external PostgreSQL database must have full access to each database instance. For example, if the external database is
                                          configured on 192.168.10.1 then each database instance must be configured in the pg_hba.conf file as host dbName username 192.168.10.0/24 password .

Step 1

Log into Cisco Unified CM IM and Presence Administration on the IM and Presence Service publisher node.

Step 2

Stop the Cisco XCP Text Conference Service on the System > Services window for each IM and Presence Service node in the
                                       presence redundancy group.

Step 3

Click Messaging > External Server Setup > External Database Jobs .

Step 4

Click on External Database Merge Job radio button.

Step 5

Click Find if you want to see the list of merge jobs. Choose Add
                                          Merge Job to add a new job.

Step 6

On the Merging External Databases window, enter the following
                                       details:

- Choose Oracle or Postgres from the Database Type drop-down list.

- Choose the IP address and hostname of the two source databases and
                                          the destination database that will contain the merged data.

If you chose Oracle as the Database Type enter the tablespace name
                                          and database name. If you chose Postgres as the Database Type you
                                          provide the database name.

Example

Select DB1 as external database currently in use which is mapped to the persistent chat room.

Select DB2 as destination database which is an external database on which data needs to be merged, DB2 database should not
                                          be empty and should have atleast one persistent chat room which meets the criteria MINVALUE(1).

After the merge, the data of source database DB1 and destination database DB2 will be saved in destination database DB2. Also,
                                          DB1 and DB2 will have unique data.

Step 7

In the Feature Tables pane, the Text Conference(TC) check-box is
                                       checked by default. For the current release, the other options are
                                       not available.

Step 8

Click Validate Selected Tables .

If the Cisco XCP Text Conference service has not been stopped you
                                                      receive an error message. Once the service has been stopped,
                                                      validation will complete.

Step 9

If there are no errors in the Validation Details pane, click Merge
                                          Selected Tables .

Step 10

When merging has completed successfully, the Find And List External
                                          Database Jobs window is loaded. Click Find to refresh the window
                                       and view the new job.

Click Find to refresh the window and view the new job.

Click the ID of the job if you want to view its details.

Step 11

Restart the Cisco XCP Router service.

Step 12

Start the Cisco XCP Text Conference Service on both IM and Presence
                                       Service nodes.

Step 13

You must reassign the newly merged external database (destination
                                       database) to the presence redundancy group

| Note | The External Database Cleanup Utility can delete chat messages records, but cannot delete the entire persistent chat rooms
                                          records. |
|---|---|

| Step 1 | Log into Cisco Unified CM IM and Presence Administration on the database publisher node. |
|---|---|
| Step 2 | Choose Messaging > External Server Setup > External Database Jobs . |
| Step 3 | Click Clear External DB . |
| Step 4 | Do one of the following: For manual cleanup of an external database that connects to the publisher node, select Same Cup Node . For manual cleanup of an external database that connects to a subscriber node, select Other Cup Node and then select the external database details. If you are configuring the system to monitor and clean the external database automatically, check the Automatic Clean-up radio button. Note We recommend that you run a manual cleanup prior to setting up the automatic cleanup. | Note | We recommend that you run a manual cleanup prior to setting up the automatic cleanup. |
| Note | We recommend that you run a manual cleanup prior to setting up the automatic cleanup. |
| Step 5 | Set the Number of Days that you want to go back for file deletion. For example, if you enter 90, the system deletes records that are older than
                                          90 days. |
| Step 6 | Click Update Schema to create the Indexes and stored procedures for the database. Note You need to update the schema only the first time that you run the job. | Note | You need to update the schema only the first time that you run the job. |
| Note | You need to update the schema only the first time that you run the job. |
| Step 7 | Set the Number of Days that you want to go back for file deletion. For example, if you enter 90 , the system deletes records that are older than 90 days. |
| Step 8 | In the Feature Tables section, select each feature for which you want to clean records: Text Conference (TC) —Select this option to clean database tables for the Persistent Chat feature. Message Archiver (MA) —Select this option to clean database tables for the Message Archiver feature. Managed File Transfer (MFT) —Select this option to clean database tables for the Managed File Transfer feature |
| Step 9 | Click Submit Clean-up Job . Note If you have the Automatic option enabled, and you want to disable it, click the Disable Automatic Clean-up Job button. | Note | If you have the Automatic option enabled, and you want to disable it, click the Disable Automatic Clean-up Job button. |
| Note | If you have the Automatic option enabled, and you want to disable it, click the Disable Automatic Clean-up Job button. |

| Note | We recommend that you run a manual cleanup prior to setting up the automatic cleanup. |
|---|---|

| Note | You need to update the schema only the first time that you run the job. |
|---|---|

| Note | If you have the Automatic option enabled, and you want to disable it, click the Disable Automatic Clean-up Job button. |
|---|---|

| Note | Microsoft SQL database is not supported for merging external databases. |
|---|---|

| Step 1 | Log into Cisco Unified CM IM and Presence Administration on the IM and Presence Service publisher node. |
|---|---|
| Step 2 | Stop the Cisco XCP Text Conference Service on the System > Services window for each IM and Presence Service node in the
                                       presence redundancy group. |
| Step 3 | Click Messaging > External Server Setup > External Database Jobs . |
| Step 4 | Note This step is applicable for Release 15SU2 onwards. Click on External Database Merge Job radio button. | Note | This step is applicable for Release 15SU2 onwards. Click on External Database Merge Job radio button. |
| Note | This step is applicable for Release 15SU2 onwards. Click on External Database Merge Job radio button. |
| Step 5 | Click Find if you want to see the list of merge jobs. Choose Add
                                          Merge Job to add a new job. |
| Step 6 | On the Merging External Databases window, enter the following
                                       details: Choose Oracle or Postgres from the Database Type drop-down list. Choose the IP address and hostname of the two source databases and
                                          the destination database that will contain the merged data. If you chose Oracle as the Database Type enter the tablespace name
                                          and database name. If you chose Postgres as the Database Type you
                                          provide the database name. Example Select DB1 as external database currently in use which is mapped to the persistent chat room. Select DB2 as destination database which is an external database on which data needs to be merged, DB2 database should not
                                          be empty and should have atleast one persistent chat room which meets the criteria MINVALUE(1). After the merge, the data of source database DB1 and destination database DB2 will be saved in destination database DB2. Also,
                                          DB1 and DB2 will have unique data. |
| Step 7 | In the Feature Tables pane, the Text Conference(TC) check-box is
                                       checked by default. For the current release, the other options are
                                       not available. |
| Step 8 | Click Validate Selected Tables . Note If the Cisco XCP Text Conference service has not been stopped you
                                                      receive an error message. Once the service has been stopped,
                                                      validation will complete. | Note | If the Cisco XCP Text Conference service has not been stopped you
                                                      receive an error message. Once the service has been stopped,
                                                      validation will complete. |
| Note | If the Cisco XCP Text Conference service has not been stopped you
                                                      receive an error message. Once the service has been stopped,
                                                      validation will complete. |
| Step 9 | If there are no errors in the Validation Details pane, click Merge
                                          Selected Tables . |
| Step 10 | When merging has completed successfully, the Find And List External
                                          Database Jobs window is loaded. Click Find to refresh the window
                                       and view the new job. Click Find to refresh the window and view the new job. Click the ID of the job if you want to view its details. |
| Step 11 | Restart the Cisco XCP Router service. |
| Step 12 | Start the Cisco XCP Text Conference Service on both IM and Presence
                                       Service nodes. |
| Step 13 | You must reassign the newly merged external database (destination
                                       database) to the presence redundancy group |

| Note | This step is applicable for Release 15SU2 onwards. Click on External Database Merge Job radio button. |
|---|---|

| Note | If the Cisco XCP Text Conference service has not been stopped you
                                                      receive an error message. Once the service has been stopped,
                                                      validation will complete. |
|---|---|