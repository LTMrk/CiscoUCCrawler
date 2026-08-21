---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-cc79e94acb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_01000001.html
retrieved_at: 2026-08-21T18:02:09.210155+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: Manage Phone
	 Migration

## Chapter: Manage Phone
	 Migration

# Manage Phone
                     	 Migration

This chapter
                        		provides information to use the Phone Migration feature in Cisco Unified Communications
                           		  Manager Bulk Administration
                           		  Tool to migrate phones from one type to another in bulk. You can
                        		access the Phone Migration submenu from the Bulk Administration menu of Cisco Unified Communications
                           		  Manager .

## Phone Migration Considerations

A text-based CSV data file is used to migrate phones. You can create
                              		  the CSV data file using either the BAT spreadsheet or a text editor.

Some limitations to keep in mind while migrating phones are:

Migrating to a phone with fewer speed dials or lines will not
                                    				remove lines or speed dials. However, some of the lines/speed dials will no
                                    				longer show up on the phone. You can still find all of the original lines/speed
                                    				dials on the phone configuration page.

Even migrating to a newer phone can cause loss of features like in
                                    				the case of moving from SIP to SCCP or vice versa.

Only existing phones can be migrated. If you enter a non-existing
                                    				device in the CSV file, the system displays an error message.

If the phone gets migrated successfully, the old phone will be
                                    				updated with the new phone settings.

If you select the reset or restart option, the new phone would be
                                    				reset.

### Create CSV Data Files for Phone Migration Using BAT Spreadsheet

You can use the BAT spreadsheet to create the CSV data file
                                 		  that contains the details for phone migration.

After you have finished editing the fields in the BAT spreadsheet, you
                                 		  can export the content to a CSV formatted data file. A default filename is
                                 		  assigned to the exported CSV formatted data file:

PhoneMigration#timestamp.txt

where " timestamp " represents the precise date and time
                                 		  that the file was created.

If you enter a comma in one of the fields, BAT.xlt encloses that
                                             			 field entry in double quotes when you export to BAT format.

If you enter a blank row in the spreadsheet, the system treats the
                                             			 empty row as the end of the file. The system does not convert data that is
                                             			 entered after a blank line to the BAT format.

Step 1

To open the BAT spreadsheet, locate and double-click BAT.xlt file

Step 2

When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities.

Step 3

Click the Phone Migration tab.

Step 4

In each row, provide the information for the following fields:

Old Device Name—Enter the name of the phone that you are migrating, from 1 to 50 characters that identifies the old device.
                                                   This field is mandatory.

New Device MAC Address—Enter the MAC address of the new Device, 12 characters. This is a mandatory field.

Description—Enter a description, up to 50 characters. This is an optional field. The description can include up to 50 characters
                                                   in any language, but it cannot include double-quotes ( " ), percentage sign ( % ), ampersand (&), back-slash ( \ ), or angle brackets (<>).

Step 5

To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 file, click Export to BAT Format .

The system saves the file using the default filename PhoneMigration#timestamp.txt to C:\XLSDataFiles or you can use Browse to save
                                             				your file in another existing folder on your local workstation

For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Phone Migration Configuration window in BAT.

#### What to do next

Upload the CSV data file to the first node of the Cisco Unified Communications Manager server so BAT can access the data input file.

## Migrate Phones

Use the Phone Migration feature in BAT to migrate phones in
                              		  bulk.

### Before you begin

You must have a data file in comma separated value (CSV) format that contains device name of the phone that you wish to migrate,
                                    the MAC address for the new phone, and the description for the new phone.

You must have a phone template of a specific type, and the protocol you wish to use for migration configured and ready.

Upload the data files by choosing the relevant target and function for the transaction.

Step 1

Choose Bulk
                                             				  Administration > Phone Migration .

Step 2

You can choose to reset or restart phones by selecting the
                                       			 appropriate radio button from the Reset/Restart Information section.

Step 3

In the Phone Migration Information section, from the File Name drop-down list box, choose the file
                                       			 that you uploaded.

Step 4

From the Phone Template Name drop-down list box, choose
                                       			 the phone template that you wish to use for migration.

Step 5

In the Job Information section, enter a description for the job.

Step 6

You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio button.

Step 7

To create a job for migrating phones, click Submit .

Step 8

A warning message informing you of a possible loss of
                                       			 features/data displays. Do one of the following:

Click Cancel to return to the Phone Migration Configuration window
                                             				  without submitting the job.

Click OK , to continue with submitting the job.

Step 9

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

| Note | If you enter a comma in one of the fields, BAT.xlt encloses that
                                             			 field entry in double quotes when you export to BAT format. If you enter a blank row in the spreadsheet, the system treats the
                                             			 empty row as the end of the file. The system does not convert data that is
                                             			 entered after a blank line to the BAT format. |
|---|---|

| Step 1 | To open the BAT spreadsheet, locate and double-click BAT.xlt file |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities. |
| Step 3 | Click the Phone Migration tab. |
| Step 4 | In each row, provide the information for the following fields: Old Device Name—Enter the name of the phone that you are migrating, from 1 to 50 characters that identifies the old device.
                                                   This field is mandatory. New Device MAC Address—Enter the MAC address of the new Device, 12 characters. This is a mandatory field. Description—Enter a description, up to 50 characters. This is an optional field. The description can include up to 50 characters
                                                   in any language, but it cannot include double-quotes ( " ), percentage sign ( % ), ampersand (&), back-slash ( \ ), or angle brackets (<>). |
| Step 5 | To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 file, click Export to BAT Format . The system saves the file using the default filename PhoneMigration#timestamp.txt to C:\XLSDataFiles or you can use Browse to save
                                             				your file in another existing folder on your local workstation Note For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Phone Migration Configuration window in BAT. | Note | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Phone Migration Configuration window in BAT. |
| Note | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Phone Migration Configuration window in BAT. |

| Note | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Phone Migration Configuration window in BAT. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Phone Migration . The Phone Migration Configuration window displays. |
|---|---|
| Step 2 | You can choose to reset or restart phones by selecting the
                                       			 appropriate radio button from the Reset/Restart Information section. Don’t Reset/Restart phones is the default
                                       			 setting. |
| Step 3 | In the Phone Migration Information section, from the File Name drop-down list box, choose the file
                                       			 that you uploaded. |
| Step 4 | From the Phone Template Name drop-down list box, choose
                                       			 the phone template that you wish to use for migration. |
| Step 5 | In the Job Information section, enter a description for the job. The default description specifies Phone Migration. |
| Step 6 | You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio button. |
| Step 7 | To create a job for migrating phones, click Submit . |
| Step 8 | A warning message informing you of a possible loss of
                                       			 features/data displays. Do one of the following: Click Cancel to return to the Phone Migration Configuration window
                                             				  without submitting the job. Click OK , to continue with submitting the job. A message in the Status section lets you know that the job
                                       			 was submitted successfully. |
| Step 9 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |