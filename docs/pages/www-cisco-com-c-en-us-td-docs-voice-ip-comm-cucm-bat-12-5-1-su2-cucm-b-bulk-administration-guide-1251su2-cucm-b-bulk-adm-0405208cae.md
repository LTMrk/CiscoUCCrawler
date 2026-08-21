---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-su2-cucm-b-bulk-administration-guide-1251su2-cucm-b-bulk-adm-0405208cae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1_SU2/cucm_b_bulk-administration-guide-1251su2/cucm_b_bulk-administration-guide-1251su2_chapter_011100.html
retrieved_at: 2026-08-21T08:47:34.115829+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: February 3, 2020

Chapter: Phone and User Insertions

## Chapter: Phone and User Insertions

- Phone and User Insertions

- Insert Phones with Users Into Unified Communications Manager

- Topics Related to Phone and User Insertion

# Phone and User Insertions

This chapter provides information to add a group of phones and users to the Unified Communications Manager database and directory.

## Insert Phones with Users Into Unified Communications Manager

You can add a group of phones and users to the Unified Communications Manager database and directory.

Phone records must be validated before insertion.

You can use the dummy MAC address option. When adding CTI ports, this option gives a unique device name to each CTI port in
                              the form of dummy MAC addresses that you can manually update later using the Unified Communications Manager Administration or the Unified CM Auto-Register phone Tool. Do not use the dummy MAC address option for H.323 clients, VGC
                              phones, or VGC virtual phones.

The dummy MAC address option automatically generates dummy MAC
                              		  addresses in the following format:

XXXXXXXXXXXX

where X represents any 12-character, hexadecimal (0-9 and A-F) number.

### Before you begin

- Create a comma-separated values (CSV) data file to define individual values for each phone with users that you want to insert.
                                    You can create the CSV data file using the BAT spreadsheet (BAT.xlt) to add phones with users, or create a custom text file
                                    in CSV format to add phones with users combinations.

- Associate file format with
                                    			 the CSV data file.

- Validate phones with users
                                    			 records.

Choose Bulk
                                             				  Administration > Phones &
                                             				  Users > Insert Phones with Users .

In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction.

In the Phone Template Name field, choose the BAT
                                       			 phone template that you used for this transaction.

If you did not enter individual MAC addresses in the CSV data
                                                      				  file, you must check the Create Dummy MAC Address check box. You
                                                      				  can update this information manually later. If you supplied MAC addresses or
                                                      				  device names in the data input file, do not choose this option.

If you do not know the MAC address of the phone that is assigned to the user, choose this option. When the phone is plugged
                                                      in, a MAC address registers for that device.

In the User Template Name field, choose the BAT user
                                       			 template that you used for this transaction

In the Job Information area, enter the Job description.

Choose an insert method. Do one of the following:

Click Run Immediately to insert the phones with
                                             				  users immediately.

Click Run Later to insert the phones with users
                                             				  at a later time.

To create a job for inserting the phones and user records, click Submit .

## Topics Related to Phone and User Insertion

| Note | Phone records must be validated before insertion. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Phones &
                                             				  Users > Insert Phones with Users . |
|---|---|
| Step 2 | In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction. |
| Step 3 | In the Phone Template Name field, choose the BAT
                                       			 phone template that you used for this transaction. Attention If you did not enter individual MAC addresses in the CSV data
                                                      				  file, you must check the Create Dummy MAC Address check box. You
                                                      				  can update this information manually later. If you supplied MAC addresses or
                                                      				  device names in the data input file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, choose this option. When the phone is plugged
                                                      in, a MAC address registers for that device. | Attention | If you did not enter individual MAC addresses in the CSV data
                                                      				  file, you must check the Create Dummy MAC Address check box. You
                                                      				  can update this information manually later. If you supplied MAC addresses or
                                                      				  device names in the data input file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, choose this option. When the phone is plugged
                                                      in, a MAC address registers for that device. |
| Attention | If you did not enter individual MAC addresses in the CSV data
                                                      				  file, you must check the Create Dummy MAC Address check box. You
                                                      				  can update this information manually later. If you supplied MAC addresses or
                                                      				  device names in the data input file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, choose this option. When the phone is plugged
                                                      in, a MAC address registers for that device. |
| Step 4 | In the User Template Name field, choose the BAT user
                                       			 template that you used for this transaction |
| Step 5 | In the Job Information area, enter the Job description. |
| Step 6 | Choose an insert method. Do one of the following: Click Run Immediately to insert the phones with
                                             				  users immediately. Click Run Later to insert the phones with users
                                             				  at a later time. |
| Step 7 | To create a job for inserting the phones and user records, click Submit . To schedule and activate this job, use the Job Scheduler option
                                       			 in the Bulk Administration main menu. |

| Attention | If you did not enter individual MAC addresses in the CSV data
                                                      				  file, you must check the Create Dummy MAC Address check box. You
                                                      				  can update this information manually later. If you supplied MAC addresses or
                                                      				  device names in the data input file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, choose this option. When the phone is plugged
                                                      in, a MAC address registers for that device. |
|---|---|