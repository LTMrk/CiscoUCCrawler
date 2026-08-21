---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-su6-cucm-b-bulk-administration-guide-1251su6-cucm-b-bulk-admin-6c72be1bbf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_SU6/cucm_b_bulk-administration-guide-1251su6/cucm_b_bulk-administration-guide-1251su2_chapter_0110111.html
retrieved_at: 2026-08-21T08:57:29.174120+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: February 15, 2022

Chapter: Manage Call Pickup
	 Groups

## Chapter: Manage Call Pickup
	 Groups

# Manage Call Pickup
                     	 Groups

This chapter
                        		provides information to set up call pickup groups using BAT. Call pickup allows
                        		you to pick up incoming calls within your own groups or in other groups when
                        		you dial the appropriate pickup group number.

## Call Pickup Group Setup Using BAT

Before you use BAT to set up call pickup groups, review the
                              		  following information:

When you add call pickup group settings for the first time, you
                                    				can create a CSV file through BAT.xlt or create a custom, text-based CSV file.

To update call pickup group settings, you can edit an existing CSV
                                    				file or create a custom, text-based CSV file.

Designate a single line for each pickup group name (and
                                    				corresponding setting). For example, use the following format when you enter
                                    				information for pickup groups:

(Pickup Group Name, Pickup Group Number, Partition, Other
                                          					 Pickup Group Name-Member1... Other Pickup Group Name-Member10)

Marketing,7815,Part1,Marketing,Managers,Training

When you add new pickup groups, you must complete all required
                                    				fields like the pickup group name and pickup group number. If the procedure
                                    				specifies an entry as mandatory, you must provide the information in the file.

Deleting information from a file and leaving the information blank
                                    				does not remove the information from the Cisco Unified Communications Manager database; in other words, a blank value does
                                    				not overwrite an existing value in the database. Updating the values overwrites
                                    				the existing value in the database.

Upload the appropriate CSV files to the first node of the Cisco Unified Communications Manager cluster.

Any time that you create or change a CSV file, you must insert the
                                    				CSV file in BAT to update the Cisco Unified Communications Manager database.

## Create Call Pickup Group CSV Data File Using BAT.xlt

You can create the CSV file for call pickup groups using the
                              		  BAT spreadsheet BAT.xlt.

The BAT.xlt file exists on the first node of the Cisco Unified Communications Manager server; however, you normally do not have
                                          			 Microsoft Excel installed on the server. In that case, copy the file from the
                                          			 first node and move it to a local machine that has Microsoft Excel installed.

### Before you begin

Review important considerations in Call Pickup Group Setup Using BAT before you use BAT to configure call pickup.

Choose Bulk Administration > Upload/Download Files .

Click Find and download the BAT.xlt file.

Copy BAT.xlt to a local machine where Microsoft Excel is
                                       			 installed.

To open the BAT Spreadsheet, locate and double-click the BAT.xlt
                                       			 file.

When prompted, click Enable Macros to use the spreadsheet
                                       			 capabilities.

Click the Call Pickup Group tab.

Enter call pickup group settings in the columns.

Repeat Step 7 until you enter all pickup groups.

To transfer the Excel spreadsheet format to a CSV file, click Export to BAT Format .

The system automatically saves CSV files to C:\XlsDatafiles on the local machine.

Click Browse to choose a different location.

### What to do next

Upload the CSV files to the first node of the Cisco Unified Communications Manager server.

You must add the CSV file to BAT and insert the file to update the Cisco Unified Communications Manager database.

## CSV Data File Creation for Call Pickup Groups Using Text Editor

You can use a text editor to create the text-based CSV data
                              		  file for call pickup groups. The comma separated values (CSV) file provides
                              		  textual information in tabular form and contains lines of ASCII text with
                              		  values separated by commas.

## Edit Existing Call Pickup Group CSV Data File

You update existing codes by manually updating an existing
                              		  CSV file or creating a new CSV file using a text editor.

When you update the Pickup Groups, existing Other Pickup Groups
                                          			 will be disassociated. Do not leave Other Pickup Group as blank fields. Enter
                                          			 all Other Pickup Groups, that you want to associate with Pickup Group,
                                          			 continuously.

You can change any part of an existing record, but you must include
                                          			 the pickup group name.

To edit an existing CSV data file, download the CSV file from the
                                       			 first node of the Cisco Unified Communications Manager server to your local workstation.

Open and edit the existing CSV file using a text editor.

### Example:

You can change any part of an existing record, but you must
                                                      				  include the pickup group name. When you update the Pickup Groups, existing
                                                      				  Other Pickup Groups will be disassociated. Do not leave Other Pickup Group as
                                                      				  blank fields. Enter all Other Pickup Groups, that you want to associate with
                                                      				  Pickup Group, continuously.

### What to do next

Upload the CSV files to the first node of the Cisco Unified Communications Manager server.

You must add the CSV file to BAT and insert the file to update the Cisco Unified Communications Manager database.

## Call Pickup Group CSV File Settings

The following table provides descriptions of the
                              		  configuration settings for call pickup groups.

Setting/Column

Description

For CPG CSV file

Pickup Group Name

For this mandatory field, enter a unique call pickup group
                                          					 name of no more than 50 alphanumeric characters.

Pickup Group Number

For this mandatory field, enter a pickup group number of no
                                          					 more than 24 digits that the user will enter to pick up incoming calls.

Partition

Choose a route partition to which the directory number (pickup
                                          					 group number) belongs.

The directory number (pickup group) can appear in more than
                                                      						one partition.

The combination of Pickup Group Number and Partition should
                                                      						be unique.

This field is optional.

Other Pickup Group Name-Member(x)

Enter the name of the other pickup group to be associated with
                                          					 the new pickup group. This optional field allows each pickup group to be
                                          					 associated with maximum of ten other pickup groups.

## Update Call Pickup Groups in CUCM Database Using BAT

To update the Cisco Unified Communications Manager database, you must insert the call pickup
                              		  group CSV data file using BAT.

### Before you begin

Before you can update pickup groups in Cisco Unified Communications Manager database, you must create or edit a call
                              		  pickup group CSV file and upload it on the first node on the Cisco Unified Communications Manager server.

Choose Bulk
                                             				  Administration > Call Pickup
                                             				  Group > Insert Call Pickup
                                             				  Groups .

In the File Name drop-down list box, choose the CSV
                                       			 file that contains the updated call pickup groups.

To view the contents of the file that you want to insert, click View File .

If you updated an existing list of call pickup groups, check the Override the existing configuration check box.

In the Job Information area, enter the Job description.

Choose an insert method. Do one of the following:

Click Run Immediately to insert pickup groups
                                             				  immediately.

Click Run Later to insert pickup groups at a
                                             				  later time.

Click Submit to create a job for inserting pickup
                                       			 groups.

## BAT Settings to Update Pickup Groups in the Database

The following table provides descriptions of BAT update
                              		  configuration settings for pickup groups.

Setting in BAT

Description

File Name

From the drop-down list box, choose the call pickup file that
                                          					 you want to insert.

Override the existing configuration

This check box applies if you are updating pickup groups for
                                          					 existing settings.

Checking this check box overwrites the other pickup group
                                          					 name- members with the information that is contained in the file that you want
                                          					 to insert. If you do not check the check box, an error, which writes to the log
                                          					 file, indicates that the other pickup group name already exists; therefore, no
                                          					 updates occur.

For each pickup group, ensure the combination of Pickup
                                                      						Group Number and Partition is unique.

While updating pickup groups, Pickup Group Number and
                                                      						Partition values will be ignored and existing Other Pickup Groups will be
                                                      						disassociated.

## Topics Related to Call Pickup Groups

| Note | The BAT.xlt file exists on the first node of the Cisco Unified Communications Manager server; however, you normally do not have
                                          			 Microsoft Excel installed on the server. In that case, copy the file from the
                                          			 first node and move it to a local machine that has Microsoft Excel installed. |
|---|---|

| Step 1 | Choose Bulk Administration > Upload/Download Files . The Find and List Files window opens. |
|---|---|
| Step 2 | Click Find and download the BAT.xlt file. |
| Step 3 | Copy BAT.xlt to a local machine where Microsoft Excel is
                                       			 installed. |
| Step 4 | To open the BAT Spreadsheet, locate and double-click the BAT.xlt
                                       			 file. |
| Step 5 | When prompted, click Enable Macros to use the spreadsheet
                                       			 capabilities. |
| Step 6 | Click the Call Pickup Group tab. |
| Step 7 | Enter call pickup group settings in the columns. See Table 1 for descriptions of configuration settings. Note Repeat Step 7 until you enter all pickup groups. | Note | Repeat Step 7 until you enter all pickup groups. |
| Note | Repeat Step 7 until you enter all pickup groups. |
| Step 8 | To transfer the Excel spreadsheet format to a CSV file, click Export to BAT Format . The system automatically saves CSV files to C:\XlsDatafiles on the local machine. Tip Click Browse to choose a different location. | Tip | Click Browse to choose a different location. |
| Tip | Click Browse to choose a different location. |

| Note | Repeat Step 7 until you enter all pickup groups. |
|---|---|

| Tip | Click Browse to choose a different location. |
|---|---|

| Caution | When you update the Pickup Groups, existing Other Pickup Groups
                                          			 will be disassociated. Do not leave Other Pickup Group as blank fields. Enter
                                          			 all Other Pickup Groups, that you want to associate with Pickup Group,
                                          			 continuously. You can change any part of an existing record, but you must include
                                          			 the pickup group name. |
|---|---|

| Step 1 | To edit an existing CSV data file, download the CSV file from the
                                       			 first node of the Cisco Unified Communications Manager server to your local workstation. |
|---|---|
| Step 2 | Open and edit the existing CSV file using a text editor. Delete existing settings, add new call pickup groups, or update
                                       			 existing settings. See Table 1 for descriptions of configuration settings. Example: To update a call pickup group CSV file, you may enter
                                       			 Marketing,,,Marketing,Managers,Training, where Marketing is the mandatory
                                       			 pickup group name. Marketing, Managers, and Training are the other pickup group
                                       			 names associated to the pickup group Marketing. Caution You can change any part of an existing record, but you must
                                                      				  include the pickup group name. When you update the Pickup Groups, existing
                                                      				  Other Pickup Groups will be disassociated. Do not leave Other Pickup Group as
                                                      				  blank fields. Enter all Other Pickup Groups, that you want to associate with
                                                      				  Pickup Group, continuously. | Caution | You can change any part of an existing record, but you must
                                                      				  include the pickup group name. When you update the Pickup Groups, existing
                                                      				  Other Pickup Groups will be disassociated. Do not leave Other Pickup Group as
                                                      				  blank fields. Enter all Other Pickup Groups, that you want to associate with
                                                      				  Pickup Group, continuously. |
| Caution | You can change any part of an existing record, but you must
                                                      				  include the pickup group name. When you update the Pickup Groups, existing
                                                      				  Other Pickup Groups will be disassociated. Do not leave Other Pickup Group as
                                                      				  blank fields. Enter all Other Pickup Groups, that you want to associate with
                                                      				  Pickup Group, continuously. |

| Caution | You can change any part of an existing record, but you must
                                                      				  include the pickup group name. When you update the Pickup Groups, existing
                                                      				  Other Pickup Groups will be disassociated. Do not leave Other Pickup Group as
                                                      				  blank fields. Enter all Other Pickup Groups, that you want to associate with
                                                      				  Pickup Group, continuously. |
|---|---|

| Setting/Column | Description |
|---|---|
| For CPG CSV file |
| Pickup Group Name | For this mandatory field, enter a unique call pickup group
                                          					 name of no more than 50 alphanumeric characters. |
| Pickup Group Number | For this mandatory field, enter a pickup group number of no
                                          					 more than 24 digits that the user will enter to pick up incoming calls. |
| Partition | Choose a route partition to which the directory number (pickup
                                          					 group number) belongs. Note The directory number (pickup group) can appear in more than
                                                      						one partition. Note The combination of Pickup Group Number and Partition should
                                                      						be unique. This field is optional. | Note | The directory number (pickup group) can appear in more than
                                                      						one partition. | Note | The combination of Pickup Group Number and Partition should
                                                      						be unique. |
| Note | The directory number (pickup group) can appear in more than
                                                      						one partition. |
| Note | The combination of Pickup Group Number and Partition should
                                                      						be unique. |
| Other Pickup Group Name-Member(x) | Enter the name of the other pickup group to be associated with
                                          					 the new pickup group. This optional field allows each pickup group to be
                                          					 associated with maximum of ten other pickup groups. |

| Note | The directory number (pickup group) can appear in more than
                                                      						one partition. |
|---|---|

| Note | The combination of Pickup Group Number and Partition should
                                                      						be unique. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Call Pickup
                                             				  Group > Insert Call Pickup
                                             				  Groups . The Insert Pickup Groups window displays. |
|---|---|
| Step 2 | In the File Name drop-down list box, choose the CSV
                                       			 file that contains the updated call pickup groups. Tip To view the contents of the file that you want to insert, click View File . | Tip | To view the contents of the file that you want to insert, click View File . |
| Tip | To view the contents of the file that you want to insert, click View File . |
| Step 3 | If you updated an existing list of call pickup groups, check the Override the existing configuration check box. See BAT Settings to Update Pickup Groups in the Database for descriptions of configuration settings. |
| Step 4 | In the Job Information area, enter the Job description. |
| Step 5 | Choose an insert method. Do one of the following: Click Run Immediately to insert pickup groups
                                             				  immediately. Click Run Later to insert pickup groups at a
                                             				  later time. |
| Step 6 | Click Submit to create a job for inserting pickup
                                       			 groups. Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |

| Tip | To view the contents of the file that you want to insert, click View File . |
|---|---|

| Setting in BAT | Description |
|---|---|
| File Name | From the drop-down list box, choose the call pickup file that
                                          					 you want to insert. |
| Override the existing configuration | This check box applies if you are updating pickup groups for
                                          					 existing settings. Checking this check box overwrites the other pickup group
                                          					 name- members with the information that is contained in the file that you want
                                          					 to insert. If you do not check the check box, an error, which writes to the log
                                          					 file, indicates that the other pickup group name already exists; therefore, no
                                          					 updates occur. Note For each pickup group, ensure the combination of Pickup
                                                      						Group Number and Partition is unique. Note While updating pickup groups, Pickup Group Number and
                                                      						Partition values will be ignored and existing Other Pickup Groups will be
                                                      						disassociated. | Note | For each pickup group, ensure the combination of Pickup
                                                      						Group Number and Partition is unique. | Note | While updating pickup groups, Pickup Group Number and
                                                      						Partition values will be ignored and existing Other Pickup Groups will be
                                                      						disassociated. |
| Note | For each pickup group, ensure the combination of Pickup
                                                      						Group Number and Partition is unique. |
| Note | While updating pickup groups, Pickup Group Number and
                                                      						Partition values will be ignored and existing Other Pickup Groups will be
                                                      						disassociated. |

| Note | For each pickup group, ensure the combination of Pickup
                                                      						Group Number and Partition is unique. |
|---|---|

| Note | While updating pickup groups, Pickup Group Number and
                                                      						Partition values will be ignored and existing Other Pickup Groups will be
                                                      						disassociated. |
|---|---|