---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-66e80dd7ff
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_0111100.html
retrieved_at: 2026-08-21T18:01:48.316096+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: Mobility Profile

## Chapter: Mobility Profile

# Mobility Profile

This chapter provides information to use Cisco Unified Communications Manager Bulk Administration Tool manage Mobility Profiles in the Cisco Unified Communications Manager database with a unique identity. You can
                        		insert, delete, and export Mobility Profiles using BAT.

## Insert Mobility Profile

You can use BAT to insert mobility profiles in bulk.

Step 1

Choose Bulk
                                             				  Administration > Mobility > Mobility
                                             				  Profile > Insert Mobility
                                             				  Profile .

Step 2

From the File Name drop-down list box, choose the CSV
                                       			 data file that you created for this specific bulk transaction.

Step 3

Checking the Override the existing configuration check box,
                                       			 overwrites the existing Mobility Profile settings with the information that is
                                       			 contained in the file that you want to insert.

Step 4

In the Job Information field, enter the Job
                                       			 description.

Step 5

Choose an insert method. Do one of the following:

Click Run Immediately to insert the profile
                                             				  immediately.

Click Run Later to insert the profile at a later
                                             				  time.

Step 6

Click Submit to create a job for inserting the
                                       			 Mobility Profile.

## Delete Mobility Profile

You can delete a Mobility Profile from the Cisco Unified Communications Manager database.

### Before you begin

Before you can delete a Mobility Profile from Cisco Unified Communications Manager Administration,
                              		  you must do the following:

Create a text file that lists each Mobility Profile that you want to delete on a separate line.

Upload the custom file with the first node of the Cisco Unified Communications Manager server.

To delete mobility profiles by using a custom file, use the
                              		  following procedure.

Do not use the insert or export transaction files that are created
                                          			 with bat.xlt for the delete transaction. Instead, you must create a custom file
                                          			 with details of the Mobility Profile records that need to be deleted. Use only
                                          			 this file for the delete transaction. The custom delete file does not require a
                                          			 header and you can enter values for the name or description or mobile client
                                          			 calling option.

Step 1

Choose Bulk
                                             				  Administration > Mobility > Mobility
                                             				  Profile > Delete Mobility
                                             				  Profile .

Step 2

From the Delete Mobility Profile where Name/Description/Mobile
                                       			 Client Calling Option in custom file drop-down list box, choose the file that
                                       			 you uploaded for deleting Mobility Profile.

Step 3

Click Find .

Step 4

The Job Information section displays along with the selected
                                       			 Mobility Profile.

Step 5

You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio buttons.

Step 6

Click Submit to create a job for deleting the
                                       			 Mobility Profile.

A message in the Status section lets you know that the job was
                                          				submitted successfully.

Step 7

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

## Export Mobility Profile

Use BAT to export Mobility Profiles.

If you are accessing help from the Export Mobility Profile Configuration window,
                                          			 skip to Step 7 .

Step 1

Choose Bulk
                                             				  Administration > Mobility > Mobility
                                             				  Profile > Export Mobility
                                             				  Profile .

Step 2

In the first Find Mobility Profile where drop-down list
                                       			 box, choose a field to query from the following options:

Name

Description

Mobile Client Calling Option

Step 3

In the second drop-down list box, choose from the following
                                       			 options:

begins with

contains

is exactly

ends with

is empty

is not empty

Step 4

In the search field box, enter the value that you want to locate,
                                       			 such as a specific profile name or profile description, and click Find .

Step 5

From the list of records that display, click the link for the
                                       			 record that you want to view.

To find all the mobility profiles that are registered in the
                                          				database, click Find without entering any search text. The
                                          				window displays the record that you choose.

Step 6

Click Next .

The Export Mobility Profile Configuration window
                                          				displays.

Step 7

In the File Name text box, enter the Mobility Profile
                                       			 file name you intend to export.

Step 8

From the File Format drop-down list box, choose the
                                       			 Mobility Profile file format.

Step 9

In the Job Information area, enter the Job description.

Step 10

Choose an export method. Do one of the following:

Click Run Immediately to export mobility
                                             				  profiles immediately.

Click Run Later to export mobility profiles at a
                                             				  later time.

Step 11

Click Submit to create a job for exporting Mobility
                                       			 Profile.

Step 12

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

| Step 1 | Choose Bulk
                                             				  Administration > Mobility > Mobility
                                             				  Profile > Insert Mobility
                                             				  Profile . The Insert Mobility Profile Configuration window
                                       			 displays |
|---|---|
| Step 2 | From the File Name drop-down list box, choose the CSV
                                       			 data file that you created for this specific bulk transaction. |
| Step 3 | Checking the Override the existing configuration check box,
                                       			 overwrites the existing Mobility Profile settings with the information that is
                                       			 contained in the file that you want to insert. |
| Step 4 | In the Job Information field, enter the Job
                                       			 description. |
| Step 5 | Choose an insert method. Do one of the following: Click Run Immediately to insert the profile
                                             				  immediately. Click Run Later to insert the profile at a later
                                             				  time. |
| Step 6 | Click Submit to create a job for inserting the
                                       			 Mobility Profile. Use the Job Scheduler option in the Bulk Administration main menu to schedule and/or
                                       			 activate this job. |

| Note | Do not use the insert or export transaction files that are created
                                          			 with bat.xlt for the delete transaction. Instead, you must create a custom file
                                          			 with details of the Mobility Profile records that need to be deleted. Use only
                                          			 this file for the delete transaction. The custom delete file does not require a
                                          			 header and you can enter values for the name or description or mobile client
                                          			 calling option. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Mobility > Mobility
                                             				  Profile > Delete Mobility
                                             				  Profile . The Delete Mobility Profile Configuration window displays. |
|---|---|
| Step 2 | From the Delete Mobility Profile where Name/Description/Mobile
                                       			 Client Calling Option in custom file drop-down list box, choose the file that
                                       			 you uploaded for deleting Mobility Profile. |
| Step 3 | Click Find . |
| Step 4 | The Job Information section displays along with the selected
                                       			 Mobility Profile. |
| Step 5 | You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio buttons. |
| Step 6 | Click Submit to create a job for deleting the
                                       			 Mobility Profile. A message in the Status section lets you know that the job was
                                          				submitted successfully. |
| Step 7 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |

| Note | If you are accessing help from the Export Mobility Profile Configuration window,
                                          			 skip to Step 7 . |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Mobility > Mobility
                                             				  Profile > Export Mobility
                                             				  Profile . The Find and List Mobility Profiles To Export window
                                       			 displays. |
|---|---|
| Step 2 | In the first Find Mobility Profile where drop-down list
                                       			 box, choose a field to query from the following options: Name Description Mobile Client Calling Option |
| Step 3 | In the second drop-down list box, choose from the following
                                       			 options: begins with contains is exactly ends with is empty is not empty |
| Step 4 | In the search field box, enter the value that you want to locate,
                                       			 such as a specific profile name or profile description, and click Find . You can choose AND or OR to add multiple filters and repeat Step 2 through Step 4 to further define your query. All matching records display. You can change the number of
                                       			 items that display on each page by choosing a different value from the Rows per Page drop-down list box. |
| Step 5 | From the list of records that display, click the link for the
                                       			 record that you want to view. To find all the mobility profiles that are registered in the
                                          				database, click Find without entering any search text. The
                                          				window displays the record that you choose. |
| Step 6 | Click Next . The Export Mobility Profile Configuration window
                                          				displays. |
| Step 7 | In the File Name text box, enter the Mobility Profile
                                       			 file name you intend to export. |
| Step 8 | From the File Format drop-down list box, choose the
                                       			 Mobility Profile file format. |
| Step 9 | In the Job Information area, enter the Job description. |
| Step 10 | Choose an export method. Do one of the following: Click Run Immediately to export mobility
                                             				  profiles immediately. Click Run Later to export mobility profiles at a
                                             				  later time. |
| Step 11 | Click Submit to create a job for exporting Mobility
                                       			 Profile. |
| Step 12 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |