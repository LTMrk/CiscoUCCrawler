---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-08e0797a96
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_010011.html
retrieved_at: 2026-08-21T17:56:38.327985+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: User Deletions

## Chapter: User Deletions

- User Deletions

- Delete Users Using Query

- Delete Users Using Custom File

# User Deletions

This chapter provides information to delete a group of users from the Unified Communications Manager directory. You can locate existing user records to delete using either a query search or a custom file.

## Delete Users Using Query

You can create a query filter to locate the user records for
                              		  the users that you want to delete.

Caution

The delete action is final. You cannot retrieve deleted records.

Step 1

Choose Bulk
                                             				  Administration > Users > Delete
                                             				  Users > Query .

The Delete Users Configuration window displays.

Step 2

From the first Find User where drop-down list box, choose one
                                       			 of the following criteria:

User ID

First Name

Middle Name

Last Name

Manager

Department Name

From the second Find User where drop-down list box, choose
                                          				one of the following criteria:

begins with

contains

is exactly

ends with

is empty

is not empty

Step 3

Specify the appropriate search text, if applicable.

Tip

To find all users that are registered in the database, click Find without entering any search text.

Step 4

To further define your query and to add multiple filters, check
                                       			 the Search Within Results check box, choose AND or OR from the drop-down box, and repeat Step 2 and Step 3 .

Step 5

Click Find .

A list of discovered templates displays by:

User ID

First Name

Middle Name

Last Name

Manager

Department Name

LDAP Sync Status

Step 6

In the Job Information area, enter the Job description.

Step 7

Choose a method to delete user records. Do one of the following:

Click Run Immediately to delete user records
                                             				  immediately.

Click Run Later to delete the user records at a
                                             				  later time.

Caution

The delete action is final. You cannot retrieve deleted records.

Step 8

To create a job for deleting the user records, click Submit .

## Delete Users Using Custom File

Create a text file that lists each user ID that you want to delete on a separate line.

Upload the custom file with the first node of the Unified Communications Manager server.

To locate and delete users, you can create a custom file of user IDs by using a text editor.

Do not use the insert or export transaction files that are created with bat.xlt for the delete transaction. Instead, you must
                                          create a custom file with details of the user records that need to be deleted. Use only this file for the delete transaction.
                                          In this custom delete file, you do not need a header, and you can enter values for user ID.

Caution

The delete action is final. You cannot retrieve deleted records.

Step 1

Choose Bulk Administration > Users > Delete Users > Custom File .

The Find and List Users - Delete Users Based on Custom
                                             				  File window displays.

Step 2

In Delete Users where drop-down list box, choose
                                       			 one of the following criteria:

User ID

First Name

Middle Name

Last Name

Department

Step 3

In the Custom file where drop-down list box, choose the filename for the custom
                                       			 file.

Step 4

To check that the query includes the information that you need,
                                       			 click Find .

Step 5

In the Job Information area, enter the Job description.

Step 6

Choose a method to delete user records. Do one of the following:

Click Run Immediately to delete user records
                                             				  immediately.

Click Run Later to delete the user records at a
                                             				  later time.

Caution

The delete action is final. You cannot retrieve deleted records.

Step 7

To create a job for deleting the user records, click Submit .

| Caution | The delete action is final. You cannot retrieve deleted records. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Users > Delete
                                             				  Users > Query . The Delete Users Configuration window displays. |
|---|---|
| Step 2 | From the first Find User where drop-down list box, choose one
                                       			 of the following criteria: User ID First Name Middle Name Last Name Manager Department Name From the second Find User where drop-down list box, choose
                                          				one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 3 | Specify the appropriate search text, if applicable. Tip To find all users that are registered in the database, click Find without entering any search text. | Tip | To find all users that are registered in the database, click Find without entering any search text. |
| Tip | To find all users that are registered in the database, click Find without entering any search text. |
| Step 4 | To further define your query and to add multiple filters, check
                                       			 the Search Within Results check box, choose AND or OR from the drop-down box, and repeat Step 2 and Step 3 . |
| Step 5 | Click Find . A list of discovered templates displays by: User ID First Name Middle Name Last Name Manager Department Name LDAP Sync Status |
| Step 6 | In the Job Information area, enter the Job description. |
| Step 7 | Choose a method to delete user records. Do one of the following: Click Run Immediately to delete user records
                                             				  immediately. Click Run Later to delete the user records at a
                                             				  later time. Caution The delete action is final. You cannot retrieve deleted records. | Caution | The delete action is final. You cannot retrieve deleted records. |
| Caution | The delete action is final. You cannot retrieve deleted records. |
| Step 8 | To create a job for deleting the user records, click Submit . To schedule and / or activate this job, use the
                                       			 Job Scheduler option in the Bulk Administration main menu. |

| Tip | To find all users that are registered in the database, click Find without entering any search text. |
|---|---|

| Caution | The delete action is final. You cannot retrieve deleted records. |
|---|---|

| Note | Do not use the insert or export transaction files that are created with bat.xlt for the delete transaction. Instead, you must
                                          create a custom file with details of the user records that need to be deleted. Use only this file for the delete transaction.
                                          In this custom delete file, you do not need a header, and you can enter values for user ID. |
|---|---|

| Caution | The delete action is final. You cannot retrieve deleted records. |
|---|---|

| Step 1 | Choose Bulk Administration > Users > Delete Users > Custom File . The Find and List Users - Delete Users Based on Custom
                                             				  File window displays. |
|---|---|
| Step 2 | In Delete Users where drop-down list box, choose
                                       			 one of the following criteria: User ID First Name Middle Name Last Name Department |
| Step 3 | In the Custom file where drop-down list box, choose the filename for the custom
                                       			 file. |
| Step 4 | To check that the query includes the information that you need,
                                       			 click Find . |
| Step 5 | In the Job Information area, enter the Job description. |
| Step 6 | Choose a method to delete user records. Do one of the following: Click Run Immediately to delete user records
                                             				  immediately. Click Run Later to delete the user records at a
                                             				  later time. Caution The delete action is final. You cannot retrieve deleted records. | Caution | The delete action is final. You cannot retrieve deleted records. |
| Caution | The delete action is final. You cannot retrieve deleted records. |
| Step 7 | To create a job for deleting the user records, click Submit . To schedule and / or activate this job, use the
                                       			 Job Scheduler option in the Bulk Administration main menu. |

| Caution | The delete action is final. You cannot retrieve deleted records. |
|---|---|