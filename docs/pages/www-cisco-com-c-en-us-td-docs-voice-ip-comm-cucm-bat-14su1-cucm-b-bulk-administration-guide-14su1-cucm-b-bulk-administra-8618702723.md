---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-14su1-cucm-b-bulk-administration-guide-14su1-cucm-b-bulk-administra-8618702723
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/14SU1/cucm_b_bulk-administration-guide-14SU1/cucm_b_bulk-administration-guide-1251su2_chapter_01000000.html
retrieved_at: 2026-08-21T09:12:18.147148+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: October 27, 2021

Chapter: Import File Validation

## Chapter: Import File Validation

# Import File Validation

This chapter provides information to use the Validate Import File page in BAT to validate the import .tar file.

## Import File Validation Items

The Validate Import File page in BAT validates the following items in the  import .tar file:

- The .tar file includes a header file.

- All files listed in the header file are actually present in the .tar file.

- All files in the .tar file are listed in header file.

- File names are correct (as per the Import/Export convention).

- File format for the CSV files in the .tar file is correct.

This feature does not include field level validation for valid characters, string length, etc.

## Validate Import File

Use the Validate Import File page in BAT to validate the
                              		  import.tar file.

The validation procedure is carried out only for the items specified
                                          			 for the import.tar file.

Step 1

Choose Bulk
                                             				  Administration > Import/Export > Validate
                                             				  Import File .

Step 2

Select the.tar file name in the Tar File Name field and click Submit .

Step 3

To check the status of the job, use the Job Scheduler option in
                                       			 the Bulk Administration main menu.

### What to do next

If there are any problems encountered during validation,
                              		  these are listed in the log files.

## Topics Related to Import File Validation

| Note | This feature does not include field level validation for valid characters, string length, etc. |
|---|---|

| Note | The validation procedure is carried out only for the items specified
                                          			 for the import.tar file. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Import/Export > Validate
                                             				  Import File . The Validate Import File window displays. |
|---|---|
| Step 2 | Select the.tar file name in the Tar File Name field and click Submit . The File Name drop-down list box lists all
                                       			 uploaded.tar files. A message in the Status section lets you know that the job
                                       			 was submitted successfully. |
| Step 3 | To check the status of the job, use the Job Scheduler option in
                                       			 the Bulk Administration main menu. |