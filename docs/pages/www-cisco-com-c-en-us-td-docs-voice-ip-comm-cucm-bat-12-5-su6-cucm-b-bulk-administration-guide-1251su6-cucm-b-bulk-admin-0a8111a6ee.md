---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-su6-cucm-b-bulk-administration-guide-1251su6-cucm-b-bulk-admin-0a8111a6ee
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_SU6/cucm_b_bulk-administration-guide-1251su6/cucm_b_bulk-administration-guide-1251su2_chapter_011000.html
retrieved_at: 2026-08-21T08:55:17.732793+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: February 15, 2022

Chapter: End User CAPF Profiles

## Chapter: End User CAPF Profiles

# End User CAPF Profiles

This chapter provides information about using Unified Communications Manager Bulk Administration Tool to add CAPF Profiles to the existing end users in the Unified Communications Manager database.

## Insert End User CAPF Profile

You can use a CSV data file to insert CAPF profiles for existing end user records in the Unified Communications Manager database.

If any information for a record fails during insertion, BAT does not
                                          			 insert that CAPF profile record.

### Before you begin

You must have a data file in comma-separated value (CSV)
                              		  format that contains the unique details for the end user CAPF profiles.

You can create the CSV data file by using one of these
                              		  methods:

BAT spreadsheet that is converted to CSV format

Export utility that produces an export file of End User CAPF Profile data

Choose Bulk
                                             				  Administration > Users > End User CAPF
                                             				  Profile > Insert End User CAPF
                                             				  Profile .

From the File Name drop-down list box, choose the CSV
                                       			 data file that you created for this specific bulk transaction.

To overwrite the existing CAPF Profile settings with the
                                       			 information that is contained in the file that you want to insert, select the Override the existing configuration check box.

In the Job Information area, enter the job description.

Choose an insert method. Do one of the following:

Click Run Immediately to insert the CAPF profile
                                             				  immediately.

Click Run Later to insert the CAPF profile at a
                                             				  later time.

To create a job for inserting the CAPF profile, click Submit .

If any information for a record fails during insertion, BAT does
                                                      				  not insert that CAPF profile record.

## Delete End User CAPF Profile

You can delete end user CAPF profiles from the Unified Communications Manager database using a custom file.

### Before you begin

Before you can delete an end user CAPF profile from Cisco Unified Communications Manager Administration , you must perform the following tasks:

Create a text file that lists each end user CAPF profile that you
                                    				want to delete on a separate line.

Upload the custom file with the first node of the Unified Communications Manager server.

Do not use the insert or export transaction files that are created
                                          			 with bat.xlt for the delete transaction. Instead, create a custom file with
                                          			 details of the end user CAPF profile records that need to be deleted. Use only
                                          			 this file for the delete transaction. The custom delete file does not require a
                                          			 header and you can enter values for the you can enter values for the Instance
                                          			 ID or End User ID.

Choose Bulk
                                             				  Administration > Users > End User CAPF
                                             				  Profile > Delete End User CAPF
                                             				  Profile .

From the Delete End User CAPF Profile where End User ID/ Instance
                                          				ID in custom file drop-down list box, choose the file that you
                                       			 uploaded for deleting end user CAPF profile.

Click Find .

The Job Information section displays along with the selected end
                                          				user CAPF profile.

You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio buttons.

Click Submit to create a job for deleting the End
                                       			 User CAPF Profile.

Use the Job Scheduler option in the Bulk Administration main menu to schedule and/or
                                       			 activate this job.

## Export End User CAPF
                        	 Profile

You can
                              		  export end user CAPF profiles by using BAT.

Choose Bulk
                                             				  Administration > Users > End User CAPF Profile > Export End User CAPF
                                             				  Profile .

In the first Find End
                                          				User CAPF Profile where drop-down list box, choose a field to query
                                       			 from the following options:

Instance Id

End User Id

In the second
                                       			 drop-down list box, choose from the following options:

begins with

contains

is exactly

ends with

is empty

is not empty

In the search
                                       			 field box, enter the value that you want to locate, such as a specific instance
                                       			 ID or end user ID.

You can choose AND or OR to add multiple filters and repeat Step 2 through Step 4 to further define your query.

Click Find .

All matching
                                          				records display. You can change the number of items that display on each page
                                          				by choosing a different value from the Rows per Page drop-down list box.

To find all
                                                      				  users that are registered in the database, click Find without entering any search text.

From the list of
                                       			 records that display, click the link for the record that you want to view.

Click Next .

The Export
                                             				  End User CAPF Profile Configuration window displays.

In the File Name text
                                       			 box, enter the end user CAPF filename you intend to export.

From the File
                                          				Format drop-down list box, choose the CAPF file format.

In the Job
                                          				Information area, enter the job description.

Choose an export
                                       			 method. Do one of the following:

Click Run
                                                					 Immediately to export the end user CAPF profiles immediately.

Click Run
                                                					 Later to export the end user CAPF profiles at a later time.

Click Submit to create a job for exporting the End User
                                       			 CAPF Profile.

Use the Job
                                          				Scheduler option in the Bulk Administration main menu to schedule and/or
                                          				activate this job.

See BAT Spreadsheet End User CAPF Profile Field Descriptions for field descriptions.

## BAT Spreadsheet End User CAPF Profile Field Descriptions

The following table describes the fields that display when
                              		  you are inserting, deleting, or exporting an end user CAPF profile.

In the BAT user interface, field names that have an asterisk
                              		  require an entry. Treat fields that do not have an asterisk as optional.

Field

Description

End User ID

Enter the end user User ID.

Instance ID

Enter 1-128 alphanumeric characters (a through z, A, through
                                          					 Z, and 0 through 9). The Instance ID identifies the user for the certificate
                                          					 operation.

Certificate Operation

Enter one of the following options:

- No Pending
                                             						Operation—Displays when no certificate operation is occurring. This is the
                                             						default setting for certificate operation.

- Install/Upgrade—Installs a new or
                                             						upgrades an existing locally significant certificate for the application.

Authentication Mode

The authentication mode for the Install/Upgrade certificate
                                          					 operation specifies "By Authentication String," which means that CAPF
                                          					 installs, upgrades, or troubleshoots a locally significant certificate only
                                          					 when the user/administrator enters the CAPF authentication string in the
                                          					 JTAPI/TSP Preferences window.

Authentication String

Enter a numeric string that contains between 4 and 10 digits.

Key Size (bits)

Enter the key size for the certificate. The default setting
                                          					 specifies 1024. Other options include 512 and 2048.

Operation Completes by

This field, which supports all certificate operations,
                                          					 specifies the date and time by which you must complete the operation.

| Attention | If any information for a record fails during insertion, BAT does not
                                          			 insert that CAPF profile record. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Users > End User CAPF
                                             				  Profile > Insert End User CAPF
                                             				  Profile . The Insert End User CAPF Profile Configuration window displays. |
|---|---|
| Step 2 | From the File Name drop-down list box, choose the CSV
                                       			 data file that you created for this specific bulk transaction. |
| Step 3 | To overwrite the existing CAPF Profile settings with the
                                       			 information that is contained in the file that you want to insert, select the Override the existing configuration check box. |
| Step 4 | In the Job Information area, enter the job description. |
| Step 5 | Choose an insert method. Do one of the following: Click Run Immediately to insert the CAPF profile
                                             				  immediately. Click Run Later to insert the CAPF profile at a
                                             				  later time. |
| Step 6 | To create a job for inserting the CAPF profile, click Submit . To schedule and / or activate this job, use the
                                       			 Job Scheduler option in the Bulk Administration main menu. Attention If any information for a record fails during insertion, BAT does
                                                      				  not insert that CAPF profile record. | Attention | If any information for a record fails during insertion, BAT does
                                                      				  not insert that CAPF profile record. |
| Attention | If any information for a record fails during insertion, BAT does
                                                      				  not insert that CAPF profile record. |

| Attention | If any information for a record fails during insertion, BAT does
                                                      				  not insert that CAPF profile record. |
|---|---|

| Note | Do not use the insert or export transaction files that are created
                                          			 with bat.xlt for the delete transaction. Instead, create a custom file with
                                          			 details of the end user CAPF profile records that need to be deleted. Use only
                                          			 this file for the delete transaction. The custom delete file does not require a
                                          			 header and you can enter values for the you can enter values for the Instance
                                          			 ID or End User ID. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Users > End User CAPF
                                             				  Profile > Delete End User CAPF
                                             				  Profile . The Delete End User CAPF Profile Configuration window displays. |
|---|---|
| Step 2 | From the Delete End User CAPF Profile where End User ID/ Instance
                                          				ID in custom file drop-down list box, choose the file that you
                                       			 uploaded for deleting end user CAPF profile. |
| Step 3 | Click Find . The Job Information section displays along with the selected end
                                          				user CAPF profile. |
| Step 4 | You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio buttons. |
| Step 5 | Click Submit to create a job for deleting the End
                                       			 User CAPF Profile. A message in the Status section lets you know that the job
                                       			 was submitted successfully. |
| Step 6 | Use the Job Scheduler option in the Bulk Administration main menu to schedule and/or
                                       			 activate this job. |

| Step 1 | Choose Bulk
                                             				  Administration > Users > End User CAPF Profile > Export End User CAPF
                                             				  Profile . The Find and
                                          				List End User CAPF Profiles To Export window displays. |
|---|---|
| Step 2 | In the first Find End
                                          				User CAPF Profile where drop-down list box, choose a field to query
                                       			 from the following options: Instance Id End User Id |
| Step 3 | In the second
                                       			 drop-down list box, choose from the following options: begins with contains is exactly ends with is empty is not empty |
| Step 4 | In the search
                                       			 field box, enter the value that you want to locate, such as a specific instance
                                       			 ID or end user ID. |
| Step 5 | You can choose AND or OR to add multiple filters and repeat Step 2 through Step 4 to further define your query. |
| Step 6 | Click Find . All matching
                                          				records display. You can change the number of items that display on each page
                                          				by choosing a different value from the Rows per Page drop-down list box. Tip To find all
                                                      				  users that are registered in the database, click Find without entering any search text. | Tip | To find all
                                                      				  users that are registered in the database, click Find without entering any search text. |
| Tip | To find all
                                                      				  users that are registered in the database, click Find without entering any search text. |
| Step 7 | From the list of
                                       			 records that display, click the link for the record that you want to view. The
                                       			 window displays the record that you choose. |
| Step 8 | Click Next . The Export
                                             				  End User CAPF Profile Configuration window displays. |
| Step 9 | In the File Name text
                                       			 box, enter the end user CAPF filename you intend to export. |
| Step 10 | From the File
                                          				Format drop-down list box, choose the CAPF file format. |
| Step 11 | In the Job
                                          				Information area, enter the job description. |
| Step 12 | Choose an export
                                       			 method. Do one of the following: Click Run
                                                					 Immediately to export the end user CAPF profiles immediately. Click Run
                                                					 Later to export the end user CAPF profiles at a later time. |
| Step 13 | Click Submit to create a job for exporting the End User
                                       			 CAPF Profile. Use the Job
                                          				Scheduler option in the Bulk Administration main menu to schedule and/or
                                          				activate this job. Note See BAT Spreadsheet End User CAPF Profile Field Descriptions for field descriptions. | Note | See BAT Spreadsheet End User CAPF Profile Field Descriptions for field descriptions. |
| Note | See BAT Spreadsheet End User CAPF Profile Field Descriptions for field descriptions. |

| Tip | To find all
                                                      				  users that are registered in the database, click Find without entering any search text. |
|---|---|

| Note | See BAT Spreadsheet End User CAPF Profile Field Descriptions for field descriptions. |
|---|---|

| Field | Description |
|---|---|
| End User ID | Enter the end user User ID. |
| Instance ID | Enter 1-128 alphanumeric characters (a through z, A, through
                                          					 Z, and 0 through 9). The Instance ID identifies the user for the certificate
                                          					 operation. |
| Certificate Operation | Enter one of the following options: No Pending
                                             						Operation—Displays when no certificate operation is occurring. This is the
                                             						default setting for certificate operation. Install/Upgrade—Installs a new or
                                             						upgrades an existing locally significant certificate for the application. |
| Authentication Mode | The authentication mode for the Install/Upgrade certificate
                                          					 operation specifies "By Authentication String," which means that CAPF
                                          					 installs, upgrades, or troubleshoots a locally significant certificate only
                                          					 when the user/administrator enters the CAPF authentication string in the
                                          					 JTAPI/TSP Preferences window. |
| Authentication String | Enter a numeric string that contains between 4 and 10 digits. |
| Key Size (bits) | Enter the key size for the certificate. The default setting
                                          					 specifies 1024. Other options include 512 and 2048. |
| Operation Completes by | This field, which supports all certificate operations,
                                          					 specifies the date and time by which you must complete the operation. |