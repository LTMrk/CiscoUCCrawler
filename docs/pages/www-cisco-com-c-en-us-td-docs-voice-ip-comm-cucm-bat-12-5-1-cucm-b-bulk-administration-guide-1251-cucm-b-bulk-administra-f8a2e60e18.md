---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-f8a2e60e18
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_01000111.html
retrieved_at: 2026-08-21T18:02:34.040242+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: Exclusion Group

## Chapter: Exclusion Group

# Exclusion Group

This chapter provides information to use Cisco Unified Communications Manager Bulk Administration (BAT) to insert or delete Exclusion Group records  in Cisco Unified Communications Manager database.

## Insert IME Exclusion Group Configuration

You can add Exclusion Group Configuration to the database using a custom CSV data file.

### Before you begin

You must have a CSV data file that contains the name and description.

You can create the CSV data file by using the BAT spreadsheet that is converted to CSV format.

Step 1

Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Exclusion Group > Insert
                                             				  Exclusion Group .

Step 2

In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction.

Step 3

In the Job Information area, enter the Job description.

The default description is Insert Exclusion Group.

Step 4

To insert the Insert Unified Exclusion Group records immediately,
                                       			 click the Run Immediately radio button. Click Run Later to insert the records at a later
                                       			 time.

Step 5

To create a job for inserting the Insert Unified Exclusion Group
                                       			 records, click Submit .

Step 6

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

## Delete IME Exclusion Group Configuration

You can delete Exclusion Group from the database using a custom CSV data file.

Do not use the insert transaction files that are created with
                                          			 bat.xlt for the delete transaction. Instead, you must create a custom file with
                                          			 details of the Exclusion Group records that need to be deleted. Use only this
                                          			 file for the delete transaction. In this custom delete file, you do not need a
                                          			 header, and you can enter values for name.

### Before you begin

Create a text file that lists the name of the Exclusion Group that you want to delete.

Upload the custom files to the server first node.

Step 1

Step 2

Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Exclusion Group > Delete
                                             				  Exclusion Group .

Step 3

From the Delete Exclusion Group where Name in custom file drop-down list, choose the filename of the custom file for this delete, and click Find .

Step 4

Click Submit to create a job to delete the Exclusion
                                       			 Group.

Step 5

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

## Topics Related to IME Exclusion Group Configuration

| Step 1 | Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Exclusion Group > Insert
                                             				  Exclusion Group . |
|---|---|
| Step 2 | In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction. |
| Step 3 | In the Job Information area, enter the Job description. The default description is Insert Exclusion Group. |
| Step 4 | To insert the Insert Unified Exclusion Group records immediately,
                                       			 click the Run Immediately radio button. Click Run Later to insert the records at a later
                                       			 time. |
| Step 5 | To create a job for inserting the Insert Unified Exclusion Group
                                       			 records, click Submit . |
| Step 6 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |

| Note | Do not use the insert transaction files that are created with
                                          			 bat.xlt for the delete transaction. Instead, you must create a custom file with
                                          			 details of the Exclusion Group records that need to be deleted. Use only this
                                          			 file for the delete transaction. In this custom delete file, you do not need a
                                          			 header, and you can enter values for name. |
|---|---|

| Step 1 |  |
|---|---|
| Step 2 | Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Exclusion Group > Delete
                                             				  Exclusion Group . |
| Step 3 | From the Delete Exclusion Group where Name in custom file drop-down list, choose the filename of the custom file for this delete, and click Find . |
| Step 4 | Click Submit to create a job to delete the Exclusion
                                       			 Group. |
| Step 5 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |