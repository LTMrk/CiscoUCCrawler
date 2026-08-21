---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-su6-cucm-b-bulk-administration-guide-1251su6-cucm-b-bulk-admin-e730e1d726
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_SU6/cucm_b_bulk-administration-guide-1251su6/cucm_b_bulk-administration-guide-1251su2_chapter_011010.html
retrieved_at: 2026-08-21T08:55:26.052408+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: February 15, 2022

Chapter: Phones and Users File Formats

## Chapter: Phones and Users File Formats

- Phones and Users File Formats

- Add Phone and User File Format

- Topics Related to Phone and User File Formats

# Phones and Users File Formats

This chapter provides information to update phones and users
                        		file formats using a comma separated values (CSV) data file.

## Add Phone and User File Format

You can add the phone and user file format with a text-based
                              		  CSV data file. After the CSV data file is created, you need to associate the
                              		  file format with the text-based CSV data file. After associating the file
                              		  format with the CSV file, the names for each field display as the first record
                              		  in the CSV data file. You can use this information to verify that you entered
                              		  the values for each field in the correct order.

### Before you begin

You must create a CSV data file that defines individual values for each user that you want to update.

When you use a text editor to create the CSV data file, you create a
                              		  file format for entering values in the text-based file. You enter values in the
                              		  text file in the order that the file format specifies.

Choose Bulk
                                             				  Administration > Phones and
                                             				  Users > Phones & Users File
                                             				  Format > Assign File Format .

In the File Name field, choose the text-based CSV
                                       			 file that you created for this transaction.

In the Format File Name field, choose the file format
                                       			 that you created for this type of bulk transaction.

To create a job for associating the matching file format with the
                                       			 CSV data file, click Submit .

To schedule and/or activate this job, use the Job Scheduler option
                                       			 in the Bulk Administration main menu.

## Topics Related to Phone and User File Formats

Add Phones with Users Using the BAT Spreadsheet

Phones with Users Combinations File Format

BAT Log Files

| Step 1 | Choose Bulk
                                             				  Administration > Phones and
                                             				  Users > Phones & Users File
                                             				  Format > Assign File Format . The Add File Format Configuration window displays. |
|---|---|
| Step 2 | In the File Name field, choose the text-based CSV
                                       			 file that you created for this transaction. |
| Step 3 | In the Format File Name field, choose the file format
                                       			 that you created for this type of bulk transaction. |
| Step 4 | To create a job for associating the matching file format with the
                                       			 CSV data file, click Submit . |
| Step 5 | To schedule and/or activate this job, use the Job Scheduler option
                                       			 in the Bulk Administration main menu. Note The user fields get added automatically when you add the file
                                                      				  format. | Note | The user fields get added automatically when you add the file
                                                      				  format. |
| Note | The user fields get added automatically when you add the file
                                                      				  format. |

| Note | The user fields get added automatically when you add the file
                                                      				  format. |
|---|---|