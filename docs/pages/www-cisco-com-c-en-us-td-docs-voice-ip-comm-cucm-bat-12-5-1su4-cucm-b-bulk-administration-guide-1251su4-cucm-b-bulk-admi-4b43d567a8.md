---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1su4-cucm-b-bulk-administration-guide-1251su4-cucm-b-bulk-admi-4b43d567a8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1SU4/cucm_b_bulk-administration-guide-1251su4/cucm_b_bulk-administration-guide-1251su2_chapter_011011.html
retrieved_at: 2026-08-21T17:51:18.462962+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: February 22, 2021

Chapter: Phone and User Validations

## Chapter: Phone and User Validations

- Phone and User Validations

- Validate Phones and User Records

- Topics Related to Phone and User Validation

# Phone and User Validations

You can use Cisco Unified Communications Manager Bulk Administration (BAT) to add a group of users and their phones on a Cisco Unified Communications Manager server in one bulk transaction. Two options exist for creating a CSV data file for the phones:

Use the BAT spreadsheet (BAT.xlt) and export the data to the CSV
                              			 format.

Use a text editor to create a text file in CSV format (for
                              			 experienced users).

You can access the Insert Phones with Users option by choosing Bulk Administration > Phones and Users from the Cisco Unified Communications Manager Administration main menu.

## Validate Phones and User Records

You can validate your CSV data file records for phones and
                              		  users. When you choose Validate Phones / Users, the system runs
                              		  a validation routine to check that the CSV data file and BAT phone template
                              		  have populated all required fields, such as device pool and locations. The
                              		  validation checks only the device fields and their dependencies.

The Primary Extension and Primary User Device of the user do not get
                                          			 validated.

### Before you begin

- You must have a BAT phone
                                 			 template for the devices that you are adding. You can use a master phone
                                 			 template with multiple lines to add phones that have a single line or several
                                 			 lines.

You must create a comma separated values (CSV) data file that
                                    				defines individual values for each phone / user that you want to
                                    				validate. You can create the CSV data file using the BAT spreadsheet (BAT.xlt) and export data to the CSV format, or use
                                    a text editor to create a custom text file in CSV format.

Associate the file format with the CSV data file.

Choose Bulk
                                             				  Administration > Phones and
                                             				  Users > Validate Phones/Users .

In the File Name field, choose the CSV data file that
                                       			 you created for this specific bulk transaction.

In the Phone Template Name field, choose the BAT
                                       			 phone template that you created for this bulk transaction.

To create a job for validating users and phones, click Submit .

To schedule and/or activate this job, use the Job Scheduler option
                                       			 in the Bulk Administration main menu.

## Topics Related to Phone and User Validation

| Note | The Primary Extension and Primary User Device of the user do not get
                                          			 validated. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Phones and
                                             				  Users > Validate Phones/Users . The Validate Phones/Users Configuration window
                                       			 displays. |
|---|---|
| Step 2 | In the File Name field, choose the CSV data file that
                                       			 you created for this specific bulk transaction. |
| Step 3 | In the Phone Template Name field, choose the BAT
                                       			 phone template that you created for this bulk transaction. |
| Step 4 | To create a job for validating users and phones, click Submit . |
| Step 5 | To schedule and/or activate this job, use the Job Scheduler option
                                       			 in the Bulk Administration main menu. |