---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1su4-cucm-b-bulk-administration-guide-1251su4-cucm-b-bulk-admi-acf6e95faa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1SU4/cucm_b_bulk-administration-guide-1251su4/cucm_b_bulk-administration-guide-1251su2_chapter_010001.html
retrieved_at: 2026-08-21T17:50:36.723175+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: February 22, 2021

Chapter: User Insertions

## Chapter: User Insertions

- User Insertions

- Insert Users in Unified Communications Manager Database

- Topics Related to User Insertions

# User Insertions

This chapter provides information to use Cisco Unified Communications Manager Bulk Administration (BAT) to add a group of
                        		users to the Cisco Unified Communications Manager database.

This feature supports only custom files that are saved with the UTF-8
                                    		  encoding format.

## Insert Users in Unified Communications Manager Database

You can add a group of users to the Unified Communications Manager database using a CSV data file. The field values that you enter in the CSV file for inserting users override the values provided
                              in the user template.

If the credential policy has "check for trivial password" enabled, and the password in the
                                          			 user template is the user ID, inserting users through BAT may fail if the user
                                          			 ID does not satisfy the necessary criteria for the trivial password.

Users can be inserted using BAT with primary extension configured without any devices selected for controlled devices. To
                              do so, you must pre-populate the DN in Unified Communications Manager before inserting the users using BAT. The following
                              steps outline the process of pre-populating the DN:

Create range of DNs to be associated for primary extension for users in the DN page.

Create a BAT template with primary extension configured (which should be the same DN's pre-populated).

Insert the users using BAT (as shown in the following procedure)

### Before you begin

You must have a CSV data file that is saved in the UTF-8 encoding format and that contains the usernames, controlled device
                              names, and directory numbers. You can create the CSV data file by using one of these methods:

- BAT spreadsheet that is
                                 			 converted to CSV format

- Export utility that
                                 			 produces an export file of user data

When you are inserting users by using an exported BAT file, you
                                          			 might get errors stating "User ID already exists" for some users that were exported in
                                          			 more than one file. For example, a list of first line managers and a list of
                                          			 users might both include the same manager user ID.

Choose Bulk
                                             				  Administration > Users > Insert
                                             				  Users .

In the File Name field, choose the CSV data file that you created for this
                                       			 bulk transaction.

If the CSV data file was created by using the export utility,
                                       			 check the File created with Export Users check box.

From the User Template Name drop-down list, choose the user template you want to use for this insert.

The User Profile, Controlled Device Name, and Directory Number should exist in the Unified Communications Manager database. The controlled device name should be entered in full. If it contains only MAC Address, then BAT displays a non-existing
                                                      device error.

In the Job Information area, enter the Job
                                       			 description.

Choose an insert method. Do one of the following:

Click Run Immediately to insert the user records
                                             				  immediately.

Click Run Later to insert the user records at a
                                             				  later time.

To create a job for inserting the user records, click Submit .

## Topics Related to User Insertions

Create New BAT User Template

BAT User Template Field Descriptions

Insert Users in Unified Communications Manager Database

| Note | This feature supports only custom files that are saved with the UTF-8
                                    		  encoding format. |
|---|---|

| Attention | If the credential policy has "check for trivial password" enabled, and the password in the
                                          			 user template is the user ID, inserting users through BAT may fail if the user
                                          			 ID does not satisfy the necessary criteria for the trivial password. |
|---|---|

| Note | When you are inserting users by using an exported BAT file, you
                                          			 might get errors stating "User ID already exists" for some users that were exported in
                                          			 more than one file. For example, a list of first line managers and a list of
                                          			 users might both include the same manager user ID. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Users > Insert
                                             				  Users . |
|---|---|
| Step 2 | In the File Name field, choose the CSV data file that you created for this
                                       			 bulk transaction. |
| Step 3 | If the CSV data file was created by using the export utility,
                                       			 check the File created with Export Users check box. |
| Step 4 | From the User Template Name drop-down list, choose the user template you want to use for this insert. Note The User Profile, Controlled Device Name, and Directory Number should exist in the Unified Communications Manager database. The controlled device name should be entered in full. If it contains only MAC Address, then BAT displays a non-existing
                                                      device error. | Note | The User Profile, Controlled Device Name, and Directory Number should exist in the Unified Communications Manager database. The controlled device name should be entered in full. If it contains only MAC Address, then BAT displays a non-existing
                                                      device error. |
| Note | The User Profile, Controlled Device Name, and Directory Number should exist in the Unified Communications Manager database. The controlled device name should be entered in full. If it contains only MAC Address, then BAT displays a non-existing
                                                      device error. |
| Step 5 | In the Job Information area, enter the Job
                                       			 description. |
| Step 6 | Choose an insert method. Do one of the following: Click Run Immediately to insert the user records
                                             				  immediately. Click Run Later to insert the user records at a
                                             				  later time. |
| Step 7 | To create a job for inserting the user records, click Submit . To schedule and / or activate this job, use the
                                       			 Job Scheduler option in the Bulk Administration main menu. |

| Note | The User Profile, Controlled Device Name, and Directory Number should exist in the Unified Communications Manager database. The controlled device name should be entered in full. If it contains only MAC Address, then BAT displays a non-existing
                                                      device error. |
|---|---|