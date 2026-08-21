---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-su6-cucm-b-bulk-administration-guide-1251su6-cucm-b-bulk-admin-658f001934
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_SU6/cucm_b_bulk-administration-guide-1251su6/cucm_b_bulk-administration-guide-1251su2_chapter_0100110.html
retrieved_at: 2026-08-21T08:56:16.078821+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: February 15, 2022

Chapter: User Device Profile File Format Addition

## Chapter: User Device Profile File Format Addition

- User Device Profile File Format Addition

- Add User Device Profile File Format

- Topics Related to UDP File Format Creation

# User Device Profile File Format Addition

This chapter provides information to associate the user device
                        		file format with the text-based CSV data file.

After you have entered all the values into the text-based CSV data file
                        		in the order that the file format specified, you need to upload the text-based
                        		CSV data file to the first node in Cisco Unified Communications Manager . You must then associate the file format with
                        		the text-based CSV data file.

## Add User Device Profile File Format

Use BAT to associate the file format with the text-based CSV
                              		  data file.

Choose Bulk
                                             				  Administration > User Device
                                             				  Profile > UDP File Format > Add File
                                             				  Format .

In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction.

In the File Format Name field, choose the file format
                                       			 that you created for this type of bulk transaction.

To add the matching file format with the CSV data file, click Submit .

A job is created in the Job Scheduler option in the Bulk Administration menu. Use Job Configuration window to modify the job
                                          				schedule.

## Topics Related to UDP File Format Creation

| Step 1 | Choose Bulk
                                             				  Administration > User Device
                                             				  Profile > UDP File Format > Add File
                                             				  Format . The Add File Format Configuration window displays. |
|---|---|
| Step 2 | In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction. |
| Step 3 | In the File Format Name field, choose the file format
                                       			 that you created for this type of bulk transaction. |
| Step 4 | To add the matching file format with the CSV data file, click Submit . A job is created in the Job Scheduler option in the Bulk Administration menu. Use Job Configuration window to modify the job
                                          				schedule. |