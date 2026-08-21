---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-su6-cucm-b-bulk-administration-guide-1251su6-cucm-b-bulk-admin-cf682722f7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_SU6/cucm_b_bulk-administration-guide-1251su6/cucm_b_bulk-administration-guide-1251su2_chapter_01000110.html
retrieved_at: 2026-08-21T08:58:32.461292+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: February 15, 2022

Chapter: Enrolled Group

## Chapter: Enrolled Group

# Enrolled Group

This chapter provides information to use Cisco Unified Communications Manager Bulk Administration (BAT) to insert or delete Enrolled Group records  in Cisco Unified Communications Manager database.

## Insert IME Enrolled Group Configuration

You can add Enrolled Group Configuration to the Cisco Unified Communications Manager database using a custom CSV data file.

### Before you begin

You must have a CSV data file that contains the group name,
                              		  description, fallback profile, and all patterns in group are aliases data.

You can create the CSV data file by using the BAT spreadsheet
                              		  that is converted to CSV format.

Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Enrolled Group > Insert
                                             				  Enrolled Group .

In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction.

In the Job Information area, enter the Job description.

The default description is Insert Enrolled Group.

To insert the Insert Unified Enrolled Group records immediately,
                                       			 click the Run Immediately radio button. Click Run Later to insert the records at a later
                                       			 time.

To create a job for inserting the Insert Unified Enrolled Group
                                       			 records, click Submit .

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

## Delete IME Enrolled Group Configuration

You can delete Enrolled Group from the database using a custom CSV data file.

Do not use the insert transaction files that are created with
                                          			 bat.xlt for the delete transaction. Instead, you must create a custom file with
                                          			 details of the Enrolled Group records that need to be deleted. Use only this
                                          			 file for the delete transaction. In this custom delete file, you do not need a
                                          			 header, and you can enter values for name.

### Before you begin

Create a text file that lists the Group name for the Enrolled Group that you want to delete.

Upload the custom to the server first node.

Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Enrolled Group > Delete
                                             				  Enrolled Group .

From the Delete Enrolled Group where Name in custom
                                          				file drop-down list box, choose the filename of the custom file for
                                       			 this delete, and click Find .

Click Submit to create a job to delete the Enrolled
                                       			 Group.

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

## Topics Related to IME Enrolled Group Configuration

| Step 1 | Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Enrolled Group > Insert
                                             				  Enrolled Group . The Insert Enrolled Group Configuration window
                                       			 displays. |
|---|---|
| Step 2 | In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction. |
| Step 3 | In the Job Information area, enter the Job description. The default description is Insert Enrolled Group. |
| Step 4 | To insert the Insert Unified Enrolled Group records immediately,
                                       			 click the Run Immediately radio button. Click Run Later to insert the records at a later
                                       			 time. |
| Step 5 | To create a job for inserting the Insert Unified Enrolled Group
                                       			 records, click Submit . |
| Step 6 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |

| Note | Do not use the insert transaction files that are created with
                                          			 bat.xlt for the delete transaction. Instead, you must create a custom file with
                                          			 details of the Enrolled Group records that need to be deleted. Use only this
                                          			 file for the delete transaction. In this custom delete file, you do not need a
                                          			 header, and you can enter values for name. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Enrolled Group > Delete
                                             				  Enrolled Group . |
|---|---|
| Step 2 | From the Delete Enrolled Group where Name in custom
                                          				file drop-down list box, choose the filename of the custom file for
                                       			 this delete, and click Find . The Enrolled Group matching your search criteria displays. |
| Step 3 | Click Submit to create a job to delete the Enrolled
                                       			 Group. |
| Step 4 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |