---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-su6-cucm-b-bulk-administration-guide-1251su6-cucm-b-bulk-admin-0131ddd0d5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_SU6/cucm_b_bulk-administration-guide-1251su6/cucm_b_bulk-administration-guide-1251su2_chapter_0111000.html
retrieved_at: 2026-08-21T08:57:33.243969+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: February 15, 2022

Chapter: Call Pickup Group Deletions

## Chapter: Call Pickup Group Deletions

- Call Pickup Group Deletions

- Delete Call Pickup Groups

# Call Pickup Group Deletions

This chapter provides information to delete call pickup groups
                        		by creating a query to locate the pickup group records you want to delete.

## Delete Call Pickup Groups

You can use BAT to delete call pickup groups.

Choose Bulk
                                             				  Administration > Call Pickup
                                             				  Group > Delete Call Pickup Groups

In first Find Call Pickup Groups where drop-down list box,
                                       			 choose from the following options:

Pickup Group Number

Pickup Group Name

Partition

From the second Find Call Pickup Groups where drop-down list
                                       			 box, choose one of the following criteria:

begins with

contains

is exactly

ends with

is empty

is not empty

Specify the appropriate search text, if applicable, and click Find .

In the Job Information area, enter the Job description.

Choose a delete method. Do one of the following:

Click Run Immediately to delete pickup groups
                                             				  immediately.

Click Run Later to delete pickup groups at a
                                             				  later time.

Click Submit to create a job for deleting pickup
                                       			 groups.

If you do not enter any information in the query text box, the
                                                      				  system creates a job for deleting all pickup group records.

Confirm that you want to delete all the pickup groups displayed
                                                      				  in the result set by browsing the entire set of results, before submitting a
                                                      				  job for deleting call pickup groups.

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                          				and / or activate this job.

| Step 1 | Choose Bulk
                                             				  Administration > Call Pickup
                                             				  Group > Delete Call Pickup Groups The Find and List Call Pickup Groups window
                                       			 displays. |
|---|---|
| Step 2 | In first Find Call Pickup Groups where drop-down list box,
                                       			 choose from the following options: Pickup Group Number Pickup Group Name Partition |
| Step 3 | From the second Find Call Pickup Groups where drop-down list
                                       			 box, choose one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 4 | Specify the appropriate search text, if applicable, and click Find . To add multiple filters, check the Search Within Results check
                                       			 box and select, AND or OR . To further define your query, repeat Step 2 through Step 4 . |
| Step 5 | In the Job Information area, enter the Job description. |
| Step 6 | Choose a delete method. Do one of the following: Click Run Immediately to delete pickup groups
                                             				  immediately. Click Run Later to delete pickup groups at a
                                             				  later time. |
| Step 7 | Click Submit to create a job for deleting pickup
                                       			 groups. Note If you do not enter any information in the query text box, the
                                                      				  system creates a job for deleting all pickup group records. Caution Confirm that you want to delete all the pickup groups displayed
                                                      				  in the result set by browsing the entire set of results, before submitting a
                                                      				  job for deleting call pickup groups. Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                          				and / or activate this job. | Note | If you do not enter any information in the query text box, the
                                                      				  system creates a job for deleting all pickup group records. | Caution | Confirm that you want to delete all the pickup groups displayed
                                                      				  in the result set by browsing the entire set of results, before submitting a
                                                      				  job for deleting call pickup groups. |
| Note | If you do not enter any information in the query text box, the
                                                      				  system creates a job for deleting all pickup group records. |
| Caution | Confirm that you want to delete all the pickup groups displayed
                                                      				  in the result set by browsing the entire set of results, before submitting a
                                                      				  job for deleting call pickup groups. |

| Note | If you do not enter any information in the query text box, the
                                                      				  system creates a job for deleting all pickup group records. |
|---|---|

| Caution | Confirm that you want to delete all the pickup groups displayed
                                                      				  in the result set by browsing the entire set of results, before submitting a
                                                      				  job for deleting call pickup groups. |
|---|---|