---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1su4-cucm-b-bulk-administration-guide-1251su4-cucm-b-bulk-admi-d03b0cd5d5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1SU4/cucm_b_bulk-administration-guide-1251su4/cucm_b_bulk-administration-guide-1251su2_chapter_01000100.html
retrieved_at: 2026-08-21T17:54:11.086542+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: February 22, 2021

Chapter: Trust Element

## Chapter: Trust Element

# Trust Element

This chapter provides information to use Cisco Unified Communications Manager Bulk Administration (BAT) to insert or delete Trust Element records  in Cisco Unified Communications Manager database.

## Insert Trust Element Configuration

Use BAT to add Trust Element Configuration to the Cisco Unified Communications Manager database.

### Before you begin

- You must have a CSV data
                                 			 file that contains the Element name, Description, Element Type, and the Trust
                                 			 Group

- You can create the CSV
                                 			 data file by using the BAT spreadsheet that is converted to CSV format.

Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Trust Element > Insert Trust
                                             				  Element .

In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction.

(Optional) Check the Override the existing configuration check box if you want to update settings for existing trust elements in your system.

In the Job Information area, enter the Job description.

The default description is Insert Trust Element.

To insert the Insert Cisco Trust Element records immediately,
                                       			 click the Run Immediately radio button. Click Run Later to insert the records at a later
                                       			 time.

To create a job for inserting the Unified Trust Element records,
                                       			 click Submit .

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

## Delete IME Trust Element Configuration

You can delete Trust Element from the Cisco Unified Communications Manager database using a custom CSV data file.

Do not use the insert transaction files that are created with
                                          			 bat.xlt for the delete transaction. Instead, you must create a custom file with
                                          			 details of the Trust Element records that need to be deleted. Use only this
                                          			 file for the delete transaction. In this custom delete file, you do not need a
                                          			 header, and you can enter values for name, description, and so on.

### Before you begin

- Create a text file that
                                 			 lists the Element Name for the Trust Element that you want to delete.

- Upload the custom files to
                                 			 the Cisco Unified Communications Manager server first node.

Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Trust Element > Delete Trust
                                             				  Element .

From the Delete Trust Element where Name in custom file drop-down list box, choose the filename of the custom file for this delete, and
                                       			 click Find .

Click Submit to create a job to delete the Trust
                                       			 Element.

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

## Topics Related to IME

| Step 1 | Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Trust Element > Insert Trust
                                             				  Element . The Insert Trust Element Configuration window
                                       			 displays. |
|---|---|
| Step 2 | In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction. |
| Step 3 | (Optional) Check the Override the existing configuration check box if you want to update settings for existing trust elements in your system. |
| Step 4 | In the Job Information area, enter the Job description. The default description is Insert Trust Element. |
| Step 5 | To insert the Insert Cisco Trust Element records immediately,
                                       			 click the Run Immediately radio button. Click Run Later to insert the records at a later
                                       			 time. |
| Step 6 | To create a job for inserting the Unified Trust Element records,
                                       			 click Submit . |
| Step 7 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |

| Note | Do not use the insert transaction files that are created with
                                          			 bat.xlt for the delete transaction. Instead, you must create a custom file with
                                          			 details of the Trust Element records that need to be deleted. Use only this
                                          			 file for the delete transaction. In this custom delete file, you do not need a
                                          			 header, and you can enter values for name, description, and so on. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Intercompany Media
                                             				  Services > Trust Element > Delete Trust
                                             				  Element . The Delete Trust Element Configuration window
                                       			 displays. |
|---|---|
| Step 2 | From the Delete Trust Element where Name in custom file drop-down list box, choose the filename of the custom file for this delete, and
                                       			 click Find . The Trust Element matching your search criteria displays. |
| Step 3 | Click Submit to create a job to delete the Trust
                                       			 Element. |
| Step 4 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |