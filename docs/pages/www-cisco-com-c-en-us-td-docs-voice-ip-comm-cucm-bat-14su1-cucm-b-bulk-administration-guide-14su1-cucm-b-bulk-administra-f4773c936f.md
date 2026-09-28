---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-14su1-cucm-b-bulk-administration-guide-14su1-cucm-b-bulk-administra-f4773c936f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/14SU1/cucm_b_bulk-administration-guide-14SU1/cucm_b_bulk-administration-guide-1251su2_chapter_0111001.html
retrieved_at: 2026-08-21T09:11:49.527615+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: October 27, 2021

Chapter: Access List

## Chapter: Access List

# Access List

This chapter provides information to use the Bulk Administration
                        		menu to insert, delete, and export access lists. An access list comprises a
                        		sequential list that consists of at least one permit statement and possibly one
                        		or more deny statements that apply to IP addresses and possibly upper-layer IP
                        		protocols. The access list has a name by which it is referenced. Many software
                        		commands accept an access list as part of their syntax.

## Insert Access Lists

You can insert access lists using BAT.

### Before you begin

You must have a data file in comma separated value (CSV) format that contains the unique details for the access lists.

Upload the data files by choosing the relevant target and function for the transaction.

Step 1

Choose Bulk
                                             				  Administration > Mobility > Access
                                             				  List > Access List Insert .

Step 2

From the File Name drop-down list box, choose the file
                                       			 that you uploaded.

Step 3

To override the existing configuration, check the Override the existing configuration check box.

Step 4

In the Job Information section, enter a description
                                       			 for the job.

Step 5

You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio button.

Step 6

To create a job for inserting the access list, click Submit .

A message in the Status section lets you know that the job was
                                          				submitted successfully.

Step 7

To schedule and / or activate this job, use the Job
                                       			 Scheduler option in the Bulk Administration main menu.

## Delete Access Lists

You can delete access lists using BAT.

### Before you begin

You must have a data file that contains the access list names.

Upload the data files by choosing the relevant target and function for the transaction.

Do not use the insert or export transaction files that are created with bat.xlt for the delete transaction. Instead, you must
                                                create a custom file with details of the access list records that need to be deleted. Use only this file for the delete transaction.
                                                In this custom delete file, you do not need a header, and you can enter values for access list names.

Step 1

Choose Bulk
                                             				  Administration > Mobility > Access
                                             				  List > Access List Delete .

Step 2

From the Delete Access List where name in custom file drop-down list box, choose the file that you uploaded for deleting access list,
                                       			 and click Find .

Step 3

The Job Information section displays along with the selected
                                       			 access list.

Step 4

You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio button.

Step 5

To create a job for deleting the access list, click Submit .

A message in the Status section lets you know that the job was
                                          				submitted successfully.

Step 6

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and/or activate this job.

## Export Access Lists

You can export access lists using BAT.

If you are accessing help from the Export Access List Configuration
                                          			 window, skip to Step 8 .

Step 1

Choose Bulk
                                             				  Administration > Mobility > Access
                                             				  List > Access List Export . The
                                       			 Export Access List Configuration window displays.

Step 2

From the first Find Access List where drop-down list box,
                                       			 choose one of the following options.

- Name

- Description

- Owner

Step 3

From the second Find Access List where drop-down list box,
                                       			 choose one of the following options.

- begins with

- contains

- ends with

- is exactly

- is empty

- is not empty

Step 4

Specify the appropriate search text, if applicable.

Tip

To find all files that are registered in the database, click Find without entering any search text.

Step 5

To further define your query, you can:

Choose AND or OR from the drop-down box and repeat Step 2 through Step 4 .

Add multiple filters by clicking the + button, and remove them by clicking the —
                                             				  button.

Remove all the filters at once by clicking the Clear Filter button.

Step 6

Click Find .

A list of discovered files displays by

- Name

- Description

- Allowed

- Owner

Step 7

Click Next .

Step 8

In the Export Access Lists section, enter a file name
                                       			 in the File Name field.

Step 9

From the Bulk Access List Export Format drop-down list
                                       			 box, choose Access List Format .

Step 10

You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio button in the Job Information section.

Step 11

To create a job for exporting the access list, click Submit .

A message in the Status section lets you know that the job was
                                          				submitted successfully.

Step 12

To schedule and / or activate this job, use the Job
                                       			 Scheduler option in the Bulk Administration main menu.

| Step 1 | Choose Bulk
                                             				  Administration > Mobility > Access
                                             				  List > Access List Insert . The Insert Access List Configuration window
                                       			 displays. |
|---|---|
| Step 2 | From the File Name drop-down list box, choose the file
                                       			 that you uploaded. |
| Step 3 | To override the existing configuration, check the Override the existing configuration check box. |
| Step 4 | In the Job Information section, enter a description
                                       			 for the job. The default description specifies Insert Access List. |
| Step 5 | You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio button. |
| Step 6 | To create a job for inserting the access list, click Submit . A message in the Status section lets you know that the job was
                                          				submitted successfully. |
| Step 7 | To schedule and / or activate this job, use the Job
                                       			 Scheduler option in the Bulk Administration main menu. |

| Note | Do not use the insert or export transaction files that are created with bat.xlt for the delete transaction. Instead, you must
                                                create a custom file with details of the access list records that need to be deleted. Use only this file for the delete transaction.
                                                In this custom delete file, you do not need a header, and you can enter values for access list names. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Mobility > Access
                                             				  List > Access List Delete . The Delete Access List Configuration window
                                       			 displays. |
|---|---|
| Step 2 | From the Delete Access List where name in custom file drop-down list box, choose the file that you uploaded for deleting access list,
                                       			 and click Find . |
| Step 3 | The Job Information section displays along with the selected
                                       			 access list. |
| Step 4 | You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio button. |
| Step 5 | To create a job for deleting the access list, click Submit . A message in the Status section lets you know that the job was
                                          				submitted successfully. |
| Step 6 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and/or activate this job. |

| Note | If you are accessing help from the Export Access List Configuration
                                          			 window, skip to Step 8 . |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Mobility > Access
                                             				  List > Access List Export . The
                                       			 Export Access List Configuration window displays. |
|---|---|
| Step 2 | From the first Find Access List where drop-down list box,
                                       			 choose one of the following options. Name Description Owner |
| Step 3 | From the second Find Access List where drop-down list box,
                                       			 choose one of the following options. begins with contains ends with is exactly is empty is not empty |
| Step 4 | Specify the appropriate search text, if applicable. Tip To find all files that are registered in the database, click Find without entering any search text. | Tip | To find all files that are registered in the database, click Find without entering any search text. |
| Tip | To find all files that are registered in the database, click Find without entering any search text. |
| Step 5 | To further define your query, you can: Choose AND or OR from the drop-down box and repeat Step 2 through Step 4 . Add multiple filters by clicking the + button, and remove them by clicking the —
                                             				  button. Remove all the filters at once by clicking the Clear Filter button. |
| Step 6 | Click Find . A list of discovered files displays by Name Description Allowed Owner |
| Step 7 | Click Next . The next Export Access List Configuration window
                                       			 displays. |
| Step 8 | In the Export Access Lists section, enter a file name
                                       			 in the File Name field. |
| Step 9 | From the Bulk Access List Export Format drop-down list
                                       			 box, choose Access List Format . |
| Step 10 | You can choose to run the job immediately or later by selecting
                                       			 the corresponding radio button in the Job Information section. |
| Step 11 | To create a job for exporting the access list, click Submit . A message in the Status section lets you know that the job was
                                          				submitted successfully. |
| Step 12 | To schedule and / or activate this job, use the Job
                                       			 Scheduler option in the Bulk Administration main menu. |

| Tip | To find all files that are registered in the database, click Find without entering any search text. |
|---|---|