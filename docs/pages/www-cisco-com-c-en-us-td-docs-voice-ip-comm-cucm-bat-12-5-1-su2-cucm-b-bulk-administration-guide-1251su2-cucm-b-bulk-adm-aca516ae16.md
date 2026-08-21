---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-su2-cucm-b-bulk-administration-guide-1251su2-cucm-b-bulk-adm-aca516ae16
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1_SU2/cucm_b_bulk-administration-guide-1251su2/cucm_b_bulk-administration-guide-1251su2_chapter_01000111.html
retrieved_at: 2026-08-21T08:50:36.086017+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: February 3, 2020

Chapter: Exclusion Group

## Chapter: Exclusion Group

# Exclusion Group

This chapter provides information to use Cisco Unified Communications Manager Bulk Administration (BAT) to insert or delete Exclusion Group records  in Cisco Unified Communications Manager database.

## Insert IME Exclusion Group Configuration

You can add Exclusion Group Configuration to the Cisco Unified Communications Manager database using a custom CSV data file.

### Before you begin

- You must have a CSV data
                                 			 file that contains the name and description.

- You can create the CSV
                                 			 data file by using the BAT spreadsheet that is converted to CSV format.

Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Exclusion Group > Insert
                                             				  Exclusion Group .

In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction.

In the Job Information area, enter the Job description.

The default description is Insert Exclusion Group.

To insert the Insert Unified Exclusion Group records immediately,
                                       			 click the Run Immediately radio button. Click Run Later to insert the records at a later
                                       			 time.

To create a job for inserting the Insert Unified Exclusion Group
                                       			 records, click Submit .

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

## Delete IME Exclusion Group Configuration

You can delete Exclusion Group from the Cisco Unified Communications Manager database using a custom CSV data file.

Do not use the insert transaction files that are created with
                                          			 bat.xlt for the delete transaction. Instead, you must create a custom file with
                                          			 details of the Exclusion Group records that need to be deleted. Use only this
                                          			 file for the delete transaction. In this custom delete file, you do not need a
                                          			 header, and you can enter values for name.

### Before you begin

- Create a text file that
                                 			 lists the name of the Exclusion Group that you want to delete.

- Upload the custom files to
                                 			 the Cisco Unified Communications Manager server first node.

Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Exclusion Group > Delete
                                             				  Exclusion Group .

From the Delete Exclusion Group where Name in custom
                                          				file drop-down list box, choose the filename of the custom file for
                                       			 this delete, and click Find .

Click Submit to create a job to delete the Exclusion
                                       			 Group.

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

## Topics Related to IME Exclusion Group Configuration

| Step 1 | Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Exclusion Group > Insert
                                             				  Exclusion Group . The Insert Exclusion Group Configuration window
                                       			 displays. |
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
                                             				  Exclusion Group . The Delete Exclusion Group Configuration window
                                       			 displays. |
| Step 3 | From the Delete Exclusion Group where Name in custom
                                          				file drop-down list box, choose the filename of the custom file for
                                       			 this delete, and click Find . The Exclusion Group matching your search criteria displays. |
| Step 4 | Click Submit to create a job to delete the Exclusion
                                       			 Group. |
| Step 5 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |