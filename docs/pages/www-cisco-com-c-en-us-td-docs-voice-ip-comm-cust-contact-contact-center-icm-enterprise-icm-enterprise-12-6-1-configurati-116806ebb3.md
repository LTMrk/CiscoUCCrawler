---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-configurati-116806ebb3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/configuration/guide/configuration-guide-for-cisco-unified-icm-contact-center-enterprise-release-12-6-1/ucce_b_1251-configuration-guide-unified-cce_chapter_01011.html
retrieved_at: 2026-08-16T14:42:57.761971+00:00
---

Configuration Guide for Cisco Unified ICM Enterprise-Release 12.6(1)

# Configuration Guide for Cisco Unified ICM Enterprise-Release 12.6(1)

Updated: May 14, 2021

Chapter: Unified CCE User Integration for Unified Intelligence Center

## Chapter: Unified CCE User Integration for Unified Intelligence Center

# Unified CCE User Integration for Unified Intelligence Center

## User Authentication

Any user who is imported with the Unified CCE User Integration feature can log in. After they are integrated, Unified CCE
                              supervisors can log into Unified Intelligence Center with their Active Directory user ID and password.

## Unified CCE User
                        	 Integration

The Unified CCE
                              		  user integration feature imports supervisors and their teams from Unified
                              		  ICM/Unified CCE from the Unified ICM Configuration Manager and database into
                              		  Unified Intelligence Center.

Supervisors are
                              		  automatically given Unified Intelligence Center user roles and can log in to
                              		  Unified Intelligence Center to access collections and run reports for their
                              		  agent teams.

Note

You cannot run User Integration until you upload the license for Unified Intelligence Center.

There are
                                                				  five tasks in the initial setup for Unified CCE User Integration. Some are
                                                				  performed in the Administration interface. Some are performed in the Reporting
                                                				  interface. As the System Application User has access to both interfaces, it is
                                                				  efficient for that user to set up Unified CCE User Integration.

The tasks are to:

Enable Unified CCE User Integration in the Administration interface.

Complete the configuration of the Unified CCE Historical Data Source in the Reporting Interface.

Synchronize Users in the Administration Interface.

Validate Collections of Agents and Agent Teams in the Reporting Interface.

Set up a synchronization schedule in the Administration Interface.

Results of Unified
                              		  CCE User Integration:

Integrated Supervisors can sign in to Unified Intelligence Center Reporting (provided their Active Directory authentication
                                    is configured).

Integrated Supervisors are added to the Unified Intelligence Center Reporting User List with the roles of Report Designer
                                    and Dashboard Designer.

The Unified Intelligence Center Value Lists page is updated with Agents and Agent Teams collections.

ntegrated Supervisors can view their Agents and Agent Teams collections ( Unified IC Reporting > Value Lists drawer).

Integrated Supervisors are granted permissions only to the Agents and Agent Teams collections that they own.

After you
                              		  configure the Unified CCE User Integration schedule, Unified Intelligence
                              		  Center updates with every synchronization the changes to supervisors and their
                              		  teams.

## Enable Unified CCE User Integration

Users who you configure as agent supervisors in Unified CCE Configuration manager and save in the Unified ICM database can
                              be integrated into Unified Intelligence Center.

To enable Unified CCE user integration:

### Procedure

Step 1

Log in to CUIC OAMP.

Step 2

From the Administration application, click Cluster Configuration > UCCE User Integration .

Step 3

Click Enable UCCE User Integration .

Step 4

Optionally, set the schedule for time of day and days of the week
                                       			 when you want to user integration. (You can return to this page and set the
                                       			 schedule later, after you configure the Unified CCE Historical Data Source.)

Step 5

Click Save .

Step 6

Do not click Synchronize Now . (You must first configure the
                                       			 Unified CCE Historical data source.)

### What to do next

Set up security for remote database.

## Set Up User Roles,  Permissions, and  Groups

Unified Intelligence Center users who correspond to Unified CCE supervisors are created by Unified CCE User Integration and
                              have the Report Designer and Dashboard Designer roles.

## Data Collections

When you implement the Unified CCE User Integration feature, the Unified Intelligence Center Value List page is updated with
                              collection values for Agent and Agent Teams value lists.

## Collections

When you use the Unified CCE User Synchronization feature, the Agent and Agent Team Value Lists are populated with collections
                              for all agents and agent teams that were imported for all Unified ICM supervisors

## All Collections Panel

The All Collections panel displays when you select a
                              		  Value List and click Collections . 
                              		 
                              		Doing this extends the Value List page so that it displays any  All
                              		  Collections for that Value List. The collections are presented in two
                              		  panels: Collection Name and Collection Type.

Note

### Actions for Collections

Create —click this to open the Create/Edit
                                    				Collection Page.

Edit —select a collection name and click
                                    				this to open the Create/Edit Collection Page. This button is disabled for System collections
                                    				imported by Unified CCE User Integration.

Delete —select a collection and click this to confirm the deletion. If you delete a
                                    				Collection, it does not appear as a filtering option for a report. This button is disabled
                                    				for System collections imported by UCCE User Integration.

Populate Values —This button is enabled only
                                    				for Collections of Type Identifier and Wildcard. This button is disabled for System
                                    				collections imported by Unified CCE User Integration.

Show Values —select a collection and click
                                    				this to see all the values in that collection; for example, to see all
                                    				agents in an Agent Team collection.

## Collections from Unified CCE User Integration

If you implement Unified CCE User Integration, the stock Agent and
                              		  Agent Teams Value Lists are updated with collections of agents and agent teams
                              		  that are automatically created from the synchronization.

The collections that are imported from the synchronization are
                              		  identified as system collections and do not affect any custom collections you might have created for the Agent or Agent
                              		  Teams Value Lists.

Supervisors who are imported with Unified CCE User Integration become Unified Intelligence Center Dashboard Designer and Report
                              Designer Users. As Report Designer Users, they
                              		  have execute access for the Value List drawer and  for the Agent and Agent Team collections for which they are
                              		  supervisors.

All imported Supervisors have execute permission for all Value Lists. However, for the imported team collections
                              		  under the Agents and Agent Teams Value Lists, only the Supervisors for those teams have execute permission to those Collections.

The system collections for Agent and Agent Team that are created by
                              		  Unified CCE User Integration are distinguished from the custom Agent and Agent Team collections in that you cannot edit,
                              		  delete, or modify the system collections.

## User List Page

The first time the Super User administrator who installed the system opens this page, the list is populated with his or her
                              name and with the names of all Supervisors who integrated from Unified CCE (if the initial User Integration has been run).

Unified CCE User Integration is configured and scheduled in the Unified Intelligence Center Operations Console (Cluster Configuration
                              > ICM User Integration). It is documented in the online help for the Operations Console.

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

| Note | You cannot run User Integration until you upload the license for Unified Intelligence Center. There are
                                                				  five tasks in the initial setup for Unified CCE User Integration. Some are
                                                				  performed in the Administration interface. Some are performed in the Reporting
                                                				  interface. As the System Application User has access to both interfaces, it is
                                                				  efficient for that user to set up Unified CCE User Integration. |
|---|---|

| Step 1 | Log in to CUIC OAMP. |
|---|---|
| Step 2 | From the Administration application, click Cluster Configuration > UCCE User Integration . |
| Step 3 | Click Enable UCCE User Integration . |
| Step 4 | Optionally, set the schedule for time of day and days of the week
                                       			 when you want to user integration. (You can return to this page and set the
                                       			 schedule later, after you configure the Unified CCE Historical Data Source.) |
| Step 5 | Click Save . |
| Step 6 | Do not click Synchronize Now . (You must first configure the
                                       			 Unified CCE Historical data source.) |

| Note | Collections imported by Unified CCE User Integration are called System collections. You cannot delete or modify these collections
                                       as they are pulled from Unified ICM configuration data. |
|---|---|