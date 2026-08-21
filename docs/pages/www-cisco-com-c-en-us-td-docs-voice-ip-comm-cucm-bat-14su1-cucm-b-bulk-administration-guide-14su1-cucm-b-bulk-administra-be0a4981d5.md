---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-14su1-cucm-b-bulk-administration-guide-14su1-cucm-b-bulk-administra-be0a4981d5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/14SU1/cucm_b_bulk-administration-guide-14SU1/cucm_b_bulk-administration-guide-1251su2_chapter_01001000.html
retrieved_at: 2026-08-21T09:12:51.616093+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: October 27, 2021

Chapter: Fallback Profile

## Chapter: Fallback Profile

# Fallback Profile

This chapter provides information to use Cisco Unified Communications Manager Bulk Administration (BAT) to insert or delete Fallback Profile records  in Cisco Unified Communications Manager database.

## Insert Fallback Profile Configuration

You can add Fallback Profile Configuration to the database using a custom CSV data file.

### Before you begin

You must have a CSV data file that contains the Name, Description, Advertised Fallback Directory E.164 Number, Fallback QOS
                                    Sensitivity Level, Fallback Call Answer Timer, Fallback Directory Number Partition, Fallback Directory Number, Number of Digits
                                    for Caller ID Partial Match and Fallback Call CSS.

You can create the CSV data file by using the BAT spreadsheet that is converted to CSV format.

Step 1

Choose Bulk Administration > Intercompany
                                             				  Media Services > Fallback
                                             				  Profie > Insert Fallback Profile .

Step 2

In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction.

Step 3

In the Job Information area, enter the Job description.

The default description is Insert Fallback Profile.

Step 4

To insert the Insert Unified Fallback Profile records immediately,
                                       			 click the Run Immediately radio button. Click Run Later to insert the records at a later
                                       			 time.

Step 5

To create a job for inserting the Insert Unified Fallback Profile
                                       			 records, click Submit .

Step 6

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

## Delete Fallback Profile Configuration

You can delete Fallback Profile from the database using a custom CSV data file.

Do not use the insert transaction files that are created with
                                          			 bat.xlt for the delete transaction. Instead, you must create a custom file with
                                          			 details of the Fallback Profile records that need to be deleted. Use only this
                                          			 file for the delete transaction. In this custom delete file, you do not need a
                                          			 header, and you can enter values for name.

### Before you begin

Create a text file that lists the name of the Fallback Profile that you want to delete.

Upload the custom files to the server first node.

Step 1

Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Fallback Profile > Delete
                                             				  Fallback Profile .

Step 2

From the Delete Fallback Profile where Name in custom file drop-down list, choose the filename of the custom file for this delete, and click Find .

Step 3

Click Submit to create a job to delete the Fallback
                                       			 Profile.

Step 4

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

## Topics Related to Fallback Profile Configuration

| Step 1 | Choose Bulk Administration > Intercompany
                                             				  Media Services > Fallback
                                             				  Profie > Insert Fallback Profile . |
|---|---|
| Step 2 | In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction. |
| Step 3 | In the Job Information area, enter the Job description. The default description is Insert Fallback Profile. |
| Step 4 | To insert the Insert Unified Fallback Profile records immediately,
                                       			 click the Run Immediately radio button. Click Run Later to insert the records at a later
                                       			 time. |
| Step 5 | To create a job for inserting the Insert Unified Fallback Profile
                                       			 records, click Submit . |
| Step 6 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |

| Note | Do not use the insert transaction files that are created with
                                          			 bat.xlt for the delete transaction. Instead, you must create a custom file with
                                          			 details of the Fallback Profile records that need to be deleted. Use only this
                                          			 file for the delete transaction. In this custom delete file, you do not need a
                                          			 header, and you can enter values for name. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Fallback Profile > Delete
                                             				  Fallback Profile . |
|---|---|
| Step 2 | From the Delete Fallback Profile where Name in custom file drop-down list, choose the filename of the custom file for this delete, and click Find . The Fallback Profile matching your search criteria displays. |
| Step 3 | Click Submit to create a job to delete the Fallback
                                       			 Profile. |
| Step 4 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |