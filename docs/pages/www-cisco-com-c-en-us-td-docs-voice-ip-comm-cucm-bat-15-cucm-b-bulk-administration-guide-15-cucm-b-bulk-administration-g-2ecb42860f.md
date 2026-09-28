---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-15-cucm-b-bulk-administration-guide-15-cucm-b-bulk-administration-g-2ecb42860f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/15/cucm_b_bulk-administration-guide-15/cucm_b_bulk-administration-guide-1251su2_chapter_0110.html
retrieved_at: 2026-08-21T09:16:30.132729+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: October 1, 2024

Chapter: Phone Insertions

## Chapter: Phone Insertions

- Phone Insertions

- Insert Phones Into Unified Communications Manager

- Topics Related to Inserting Phones

# Phone Insertions

This chapter provides information to add phones, Cisco VGC
                        		Phones, CTI ports, or H.323 clients into the Cisco Unified Communications Manager database.

You must have a Cisco Unified Communications Manager Bulk Administration (BAT) phone template for the devices that you are adding, and a data file in comma separated value (CSV)
                        format that contains the unique details for the phones or other IP telephony devices. You can choose the target and method
                        of the data file upload. Phone records must be validated before insertion.

## Insert Phones Into Unified Communications Manager

When you insert phone records into the Unified Communications Manager database, you define the target CSV data file and how the phone records get inserted. Select any combination of the listed
                              actions to overwrite the existing phone records, or you can choose to insert the records during upload:

Delete all existing Speed Dials before adding new one

Delete all existing BLF Speed Dials before adding new one

Delete all existing BLF Directed Call Parks before adding new one

Delete all existing Subscribed Services before adding new one

Phone records
                                          			 must be validated before insertion.

BAT expects Directory Number URI fields for directory
                                          			 numbers in the following format:

URI 1 on
                                          			 Directory Number 1, URI 1 Route Partition on Directory Number 1, URI 1 is
                                          			 Primary on Directory Number 1.

You can use the pseudo MAC address option. When adding CTI ports, this option gives a unique device name to each CTI port in the form of pseudo MAC addresses that you can manually update later using the Unified Communications Manager Administration or the Unified CM Auto-Register Phone Tool. Do not use the pseudo MAC address option for H.323 clients, VGC phones, or VGC virtual phones.

The pseudo MAC address option automatically generates pseudo MAC addresses in the following format:

XXXXXXXXXXXX

where X represents
                              		  any 12-character, hexadecimal (0-9 and A-F) number.

### Before you begin

You must have a Unified Communications Manager Bulk Administration (BAT) phone template for the devices that you are adding. You can choose the target and method of the
                                    data file upload. Phone records must be validated before insertion.

You must have a data file in comma separated value (CSV) format that contains the unique details for the phones or other IP
                                    telephony devices.

Step 1

Choose Bulk
                                             				  Administration > Phones > Insert Phones .

Step 2

Specify the file
                                       			 format type for the phone record that you are uploading.

To insert
                                             				  phone records that use a customized file format, click Insert Phones Specific Details radio button and
                                             				  continue with Step 3 and Step 5 .

To insert phone records from an exported phone's file that was generated using the All Details option, click Insert phones All Details radio button.

Step 3

In the File Name drop-down list box, choose the CSV data file that you created for this specific bulk transaction. Next, check the Allow Update Phone with Custom File check box to allow updating the phone with the chosen custom file.

Step 4

Check the Override the existing configuration check box to overwrite the existing phone settings with the information that is contained in the file that you want to insert.
                                       Next, check the check boxes beside the upload action(s) to perform during the upload.

The following upload actions get enabled for selection after you have checked the Override the existing configuration check box.

Delete all existing Speed Dials before adding new one.

Delete all existing BLF Speed Dials before adding new one.

Delete all existing BLF Directed Call Parks before adding new one.

Delete all existing Subscribed Services before adding new one.

Leave the check boxes clear to append those records to the existing records in the CSV data file during the upload.

Step 5

For the Specific Details option, in the Phone Template Name drop-down list, choose the BAT phone template that you created for this type of bulk transaction.

Attention

If you did not enter individual MAC addresses in the CSV data file, you must check the Create Pseudo MAC Address check box. You can update this information manually later. Skip to Step 8 . If you supplied MAC addresses or device names in the data input file, do not choose this option.

If you do not know the MAC address of the phone that is assigned to the user, then choose this option. When the phone is plugged
                                                      in, a MAC address registers for that device.

Step 6

In the Job
                                          				Information area, enter the Job description.

Step 7

Choose an insert
                                       			 method. Do one of the following:

Click Run
                                                					 Immediately to insert the phone records immediately.

Click Run Later to insert the phone records later.

Step 8

Click Submit to create a job for inserting the phone
                                       			 records.

### What to do next

If the phones
                              		  inserted are of the type Cisco Unified Mobile Communicator, then you must reset
                              		  the devices after the insert job is completed. You can reset the phones using
                              		  the Bulk
                                    				Administration > Phones > Reset/Restart Phones option.

## Topics Related to Inserting Phones

| Note | Phone records
                                          			 must be validated before insertion. |
|---|---|

| Note | BAT expects Directory Number URI fields for directory
                                          			 numbers in the following format: URI 1 on
                                          			 Directory Number 1, URI 1 Route Partition on Directory Number 1, URI 1 is
                                          			 Primary on Directory Number 1. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Phones > Insert Phones . |
|---|---|
| Step 2 | Specify the file
                                       			 format type for the phone record that you are uploading. To insert
                                             				  phone records that use a customized file format, click Insert Phones Specific Details radio button and
                                             				  continue with Step 3 and Step 5 . To insert phone records from an exported phone's file that was generated using the All Details option, click Insert phones All Details radio button. |
| Step 3 | In the File Name drop-down list box, choose the CSV data file that you created for this specific bulk transaction. Next, check the Allow Update Phone with Custom File check box to allow updating the phone with the chosen custom file. |
| Step 4 | Check the Override the existing configuration check box to overwrite the existing phone settings with the information that is contained in the file that you want to insert.
                                       Next, check the check boxes beside the upload action(s) to perform during the upload. The following upload actions get enabled for selection after you have checked the Override the existing configuration check box. Delete all existing Speed Dials before adding new one. Delete all existing BLF Speed Dials before adding new one. Delete all existing BLF Directed Call Parks before adding new one. Delete all existing Subscribed Services before adding new one. Note Leave the check boxes clear to append those records to the existing records in the CSV data file during the upload. | Note | Leave the check boxes clear to append those records to the existing records in the CSV data file during the upload. |
| Note | Leave the check boxes clear to append those records to the existing records in the CSV data file during the upload. |
| Step 5 | For the Specific Details option, in the Phone Template Name drop-down list, choose the BAT phone template that you created for this type of bulk transaction. Attention If you did not enter individual MAC addresses in the CSV data file, you must check the Create Pseudo MAC Address check box. You can update this information manually later. Skip to Step 8 . If you supplied MAC addresses or device names in the data input file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, then choose this option. When the phone is plugged
                                                      in, a MAC address registers for that device. | Attention | If you did not enter individual MAC addresses in the CSV data file, you must check the Create Pseudo MAC Address check box. You can update this information manually later. Skip to Step 8 . If you supplied MAC addresses or device names in the data input file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, then choose this option. When the phone is plugged
                                                      in, a MAC address registers for that device. |
| Attention | If you did not enter individual MAC addresses in the CSV data file, you must check the Create Pseudo MAC Address check box. You can update this information manually later. Skip to Step 8 . If you supplied MAC addresses or device names in the data input file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, then choose this option. When the phone is plugged
                                                      in, a MAC address registers for that device. |
| Step 6 | In the Job
                                          				Information area, enter the Job description. |
| Step 7 | Choose an insert
                                       			 method. Do one of the following: Click Run
                                                					 Immediately to insert the phone records immediately. Click Run Later to insert the phone records later. |
| Step 8 | Click Submit to create a job for inserting the phone
                                       			 records. Use the Job Configuration window to schedule or activate this job. |

| Note | Leave the check boxes clear to append those records to the existing records in the CSV data file during the upload. |
|---|---|

| Attention | If you did not enter individual MAC addresses in the CSV data file, you must check the Create Pseudo MAC Address check box. You can update this information manually later. Skip to Step 8 . If you supplied MAC addresses or device names in the data input file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, then choose this option. When the phone is plugged
                                                      in, a MAC address registers for that device. |
|---|---|