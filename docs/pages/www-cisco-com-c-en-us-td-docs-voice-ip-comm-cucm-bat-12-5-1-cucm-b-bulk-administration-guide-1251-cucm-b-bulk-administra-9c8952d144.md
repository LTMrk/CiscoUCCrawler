---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-9c8952d144
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_010100.html
retrieved_at: 2026-08-21T17:56:42.444046+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: User Record Exports

## Chapter: User Record Exports

- User Record Exports

- Export User Records

- Topics Related to User Record Exports

# User Record Exports

When you use Unified Communications Manager Bulk Administration (BAT) to export user records, the export utility sorts users according to the organizational hierarchy
                        in the database.

From the Exports Users Configuration window, if Default User Format is selected from the File Format drop-down list box. the export utility only exports the default user device profile that is associated with a user. You must
                        insert the other user device profiles for that user separately by using Cisco Unified Communications Manager Administrator.

## Export User Records

When you export user records using BAT, some users might have a blank PIN because these user records were created prior to Unified Communications Manager 3.1. If this is the case, you must specify a default PIN before reinserting the user records in the BAT user interface.

Caution

Step 1

Choose Bulk Administration > Users > Export Users .

The Find and List Users to Export window displays.

Step 2

In the first Find User where drop-down list, choose a field to query from the following options:

User ID

First Name

Middle Name

Last Name

Manager

Department

Step 3

In the second drop-down list, choose from the following options:

begins with

contains

is exactly

ends with

is empty

is not empty

Step 4

In the search field/list box, enter the value that you want to
                                       			 locate, such as a specific name or User ID.

To choose users from more than one department, enter multiple
                                                      				  departments in this field. For example, to choose users from departments 12 and
                                                      				  34, enter 12, 34 in the third box instead of performing two operations.

Step 5

You can click the Search Within Results check box and choose AND or OR to add multiple filters and repeat Step 2 through Step 4 to further define your query.

Step 6

Click Find . The search results display.

Step 7

Click Next .

Step 8

Enter the export users file name in the File Name text box.

Step 9

Choose file format from the File Format drop-down list.

Step 10

In the Job Information area, enter the Job description.

Step 11

Choose a method to export user records. Do one of the following:

Click Run Immediately to export user records
                                             				  immediately.

Click Run Later to export at a later time.

Step 12

To create a job for exporting user records, click Submit .

### What to do next

You can search and download the exported file using the
                              		  Upload/Download Files option in the Bulk Administration menu.

Caution

## Topics Related to User Record Exports

BAT Log Files

Upload and Download Files

| Caution | The user ID, PKID, password, pin, and digest credentials columns in the exported file should not be modified under any circumstances. |
|---|---|

| Step 1 | Choose Bulk Administration > Users > Export Users . The Find and List Users to Export window displays. |
|---|---|
| Step 2 | In the first Find User where drop-down list, choose a field to query from the following options: User ID First Name Middle Name Last Name Manager Department |
| Step 3 | In the second drop-down list, choose from the following options: begins with contains is exactly ends with is empty is not empty |
| Step 4 | In the search field/list box, enter the value that you want to
                                       			 locate, such as a specific name or User ID. Note To choose users from more than one department, enter multiple
                                                      				  departments in this field. For example, to choose users from departments 12 and
                                                      				  34, enter 12, 34 in the third box instead of performing two operations. | Note | To choose users from more than one department, enter multiple
                                                      				  departments in this field. For example, to choose users from departments 12 and
                                                      				  34, enter 12, 34 in the third box instead of performing two operations. |
| Note | To choose users from more than one department, enter multiple
                                                      				  departments in this field. For example, to choose users from departments 12 and
                                                      				  34, enter 12, 34 in the third box instead of performing two operations. |
| Step 5 | You can click the Search Within Results check box and choose AND or OR to add multiple filters and repeat Step 2 through Step 4 to further define your query. |
| Step 6 | Click Find . The search results display. Note To find all users that are registered in the database, click Find without entering any search text. | Note | To find all users that are registered in the database, click Find without entering any search text. |
| Note | To find all users that are registered in the database, click Find without entering any search text. |
| Step 7 | Click Next . |
| Step 8 | Enter the export users file name in the File Name text box. |
| Step 9 | Choose file format from the File Format drop-down list. |
| Step 10 | In the Job Information area, enter the Job description. |
| Step 11 | Choose a method to export user records. Do one of the following: Click Run Immediately to export user records
                                             				  immediately. Click Run Later to export at a later time. |
| Step 12 | To create a job for exporting user records, click Submit . To schedule and / or activate this job, use the
                                       			 Job Scheduler option in the Bulk Administration main menu. |

| Note | To choose users from more than one department, enter multiple
                                                      				  departments in this field. For example, to choose users from departments 12 and
                                                      				  34, enter 12, 34 in the third box instead of performing two operations. |
|---|---|

| Note | To find all users that are registered in the database, click Find without entering any search text. |
|---|---|

| Caution | The user ID, PKID, password, pin, and digest credentials columns in the exported file should not be modified under any circumstances. |
|---|---|