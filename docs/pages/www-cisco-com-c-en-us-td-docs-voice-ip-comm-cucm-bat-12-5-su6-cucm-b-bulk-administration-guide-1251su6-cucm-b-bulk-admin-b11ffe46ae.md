---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-su6-cucm-b-bulk-administration-guide-1251su6-cucm-b-bulk-admin-b11ffe46ae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_SU6/cucm_b_bulk-administration-guide-1251su6/cucm_b_bulk-administration-guide-1251su2_chapter_0111010.html
retrieved_at: 2026-08-21T08:57:41.817764+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: February 15, 2022

Chapter: Remote Destination

## Chapter: Remote Destination

# Remote Destination

This chapter provides information to use BAT to insert, delete,
                        		and export remote destination details.

## Insert Remote Destination

You can insert remote destination details using BAT.

### Before you begin

You must have a data file in comma separated value (CSV) format that contains the unique details for the remote destination.

Upload the data files by choosing the relevant target and function for the transaction.

Choose Bulk Administration > Mobility > Remote Destination > Remote
                                             				  Destination Insert .

From the File Name drop-down list box, choose the file
                                       			 that you uploaded.

To override the existing configuration, check the Override the existing configuration check box.

In the Job Information section, enter a description
                                       			 for the job. Insert Remote Destination specifies the
                                       			 default description.

You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio button.

To create a job for inserting the remote destination, click Submit .

A message in the Status section lets you know that the job was
                                          				submitted successfully.

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job.

## Delete Remote Destination

You can delete remote destinations using BAT.

### Before you begin

You must have a data file in comma separated value (CSV) format that contains the unique details for the remote destination.

Upload the data files by choosing the relevant target and function for the transaction.

Choose Bulk
                                             				  Administration > Mobility > Remote
                                             				  Destination > Remote Destination
                                             				  Delete .

From the Delete Remote Destination where drop-down list
                                       			 box, choose one of the following options:

Name

Destination

Remote Destination Profile

Dual Mode Phone

From the custom file drop-down list box, choose the file that you
                                       			 uploaded for deleting remote destination, and click Find .

The Job Information section displays along with the selected
                                       			 remote destination.

You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio button.

To create a job for deleting the remote destination, click Submit .

A message in the Status section lets you know that the job was
                                          				submitted successfully.

To schedule and / or activate this job, use the Job
                                       			 Scheduler option in the Bulk Administration main menu.

When you delete a remote destination, the time-of-day access,
                                                      				  time period, and time schedule records associated with the remote destination
                                                      				  also get deleted.

## Export Remote Destination

You can export a remote destination using BAT.

If you are accessing help from the second Export Remote Destination Configuration window after selecting the remote destination for export,
                                          			 skip to Step 8 .

Choose Bulk
                                             				  Administration > Mobility > Remote
                                             				  Destination > Remote Destination
                                             				  Export .

From the first Find Remote Destination where drop-down list
                                       			 box, choose one of the following options:

- Name

- Destination

- Remote Destination
                                             				  Profile

- Dual Mode Phone

From the second Find Remote Destination
                                          				where drop-down list box, choose one of the following options:

- begins with

- contains

- ends with

- is exactly

- is empty

- is not empty

Specify the appropriate search text, if applicable.

To find all files that are registered in the database, click Find without entering any search text.

To further define your query, you can

Choose AND or OR from the drop-down box, and repeat Step 2 through Step 4 .

Add multiple filters by clicking the + button, and remove them by clicking the —
                                             				  button.

Remove all the filters at once by clicking the Clear Filter button.

Click Find .

A list of discovered files displays by

- Name

- Destination

- Remote Destination
                                             				  Profile

- Dual Mode Phone

Click Next .

In the Export Remote Destination section, enter a
                                       			 file name in the File Name field.

From the File Format drop-down list box, choose Remote Destination Format .

You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio button in the Job Information section.

To create a job for exporting the remote destination, click Submit .

A message in the Status section lets you know that the job was
                                          				submitted successfully.

To schedule and / or activate this job, use the Job
                                       			 Scheduler option in the Bulk Administration main menu.

| Note | You must enter the time zone details without parenthesis or asterisk. For example, if you are entering Greenwich Mean Time
                                             as the time zone, enter it as "Etc / GMT" and not "(GMT) Etc / GMT*" . |
|---|---|

| Step 1 | Choose Bulk Administration > Mobility > Remote Destination > Remote
                                             				  Destination Insert . |
|---|---|
| Step 2 | From the File Name drop-down list box, choose the file
                                       			 that you uploaded. |
| Step 3 | To override the existing configuration, check the Override the existing configuration check box. |
| Step 4 | In the Job Information section, enter a description
                                       			 for the job. Insert Remote Destination specifies the
                                       			 default description. |
| Step 5 | You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio button. |
| Step 6 | To create a job for inserting the remote destination, click Submit . A message in the Status section lets you know that the job was
                                          				submitted successfully. |
| Step 7 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |

| Note | Do not use the insert or export transaction files that are created with bat.xlt for the delete transaction. Instead, you must
                                             create a custom file with details of the remote destination records that need to be deleted. Use only this file for the delete
                                             transaction. In this custom delete file, you do not need a header, and you can enter values for name, or description. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Mobility > Remote
                                             				  Destination > Remote Destination
                                             				  Delete . |
|---|---|
| Step 2 | From the Delete Remote Destination where drop-down list
                                       			 box, choose one of the following options: Name Destination Remote Destination Profile Dual Mode Phone |
| Step 3 | From the custom file drop-down list box, choose the file that you
                                       			 uploaded for deleting remote destination, and click Find . |
| Step 4 | The Job Information section displays along with the selected
                                       			 remote destination. |
| Step 5 | You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio button. |
| Step 6 | To create a job for deleting the remote destination, click Submit . A message in the Status section lets you know that the job was
                                          				submitted successfully. |
| Step 7 | To schedule and / or activate this job, use the Job
                                       			 Scheduler option in the Bulk Administration main menu. Attention When you delete a remote destination, the time-of-day access,
                                                      				  time period, and time schedule records associated with the remote destination
                                                      				  also get deleted. | Attention | When you delete a remote destination, the time-of-day access,
                                                      				  time period, and time schedule records associated with the remote destination
                                                      				  also get deleted. |
| Attention | When you delete a remote destination, the time-of-day access,
                                                      				  time period, and time schedule records associated with the remote destination
                                                      				  also get deleted. |

| Attention | When you delete a remote destination, the time-of-day access,
                                                      				  time period, and time schedule records associated with the remote destination
                                                      				  also get deleted. |
|---|---|

| Note | If you are accessing help from the second Export Remote Destination Configuration window after selecting the remote destination for export,
                                          			 skip to Step 8 . |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Mobility > Remote
                                             				  Destination > Remote Destination
                                             				  Export . The Export Remote Destination Configuration window
                                       			 displays. |
|---|---|
| Step 2 | From the first Find Remote Destination where drop-down list
                                       			 box, choose one of the following options: Name Destination Remote Destination
                                             				  Profile Dual Mode Phone |
| Step 3 | From the second Find Remote Destination
                                          				where drop-down list box, choose one of the following options: begins with contains ends with is exactly is empty is not empty |
| Step 4 | Specify the appropriate search text, if applicable. Tip To find all files that are registered in the database, click Find without entering any search text. | Tip | To find all files that are registered in the database, click Find without entering any search text. |
| Tip | To find all files that are registered in the database, click Find without entering any search text. |
| Step 5 | To further define your query, you can Choose AND or OR from the drop-down box, and repeat Step 2 through Step 4 . Add multiple filters by clicking the + button, and remove them by clicking the —
                                             				  button. Remove all the filters at once by clicking the Clear Filter button. |
| Step 6 | Click Find . A list of discovered files displays by Name Destination Remote Destination
                                             				  Profile Dual Mode Phone |
| Step 7 | Click Next . The next Export Remote Destination Configuration window
                                       			 displays. |
| Step 8 | In the Export Remote Destination section, enter a
                                       			 file name in the File Name field. |
| Step 9 | From the File Format drop-down list box, choose Remote Destination Format . |
| Step 10 | You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio button in the Job Information section. |
| Step 11 | To create a job for exporting the remote destination, click Submit . A message in the Status section lets you know that the job was
                                          				submitted successfully. |
| Step 12 | To schedule and / or activate this job, use the Job
                                       			 Scheduler option in the Bulk Administration main menu. |

| Tip | To find all files that are registered in the database, click Find without entering any search text. |
|---|---|