---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-7a6fdcd777
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_0110011.html
retrieved_at: 2026-08-21T18:01:10.605813+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: Cisco Gateway Deletions

## Chapter: Cisco Gateway Deletions

- Cisco Gateway Deletions

- Delete Cisco Gateway                              	 Records Using Query

- Topics Related to Cisco Gateway Deletions

# Cisco Gateway Deletions

This chapter provides information to locate the gateway records that you want to delete from the database. You must define a query filter to delete a group of gateways. You can only delete Cisco VG200 and Cisco Catalyst
                        6000 gateway records using the Delete Gateway Configuration window.

## Delete Cisco Gateway
                        	 Records Using Query

You can use a query to locate the gateway records that you want to delete from Cisco Unified Communications Manager. You can
                              only delete Cisco VG200 and Cisco Catalyst 6000 gateways using the Delete Gateway Configuration window.

Caution

Step 1

Choose Bulk
                                             				  Administration > Gateways > Delete
                                             				  Gateways .

Step 2

From the Delete Gateways where drop-down list, choose one of the following options:

Name

Description

DN/Route Pattern

Calling Search Space

Device Pool

Device Type

Step 3

From the second Find Gateways where drop-down list, choose one of the following criteria:

begins with

contains

is exactly

ends with

is empty

is not empty

Step 4

From the third drop-down list, choose Show to display the associated endpoints.

Step 5

Specify the
                                       			 appropriate search text, if applicable, and click Find .

Tip

To further
                                          				define your query, you can choose AND or OR to add multiple filters and repeat Step 2 through Step 5 .

A list of discovered templates displays by:

Device Name

Description

Device Pool

Status

IP address

Step 6

In the Job
                                          				Information area, enter the Job description.

Step 7

Choose a delete
                                       			 method. Do one of the following:

Click Run
                                                					 Immediately to delete gateways immediately.

Click Run
                                                					 Later to delete gateways at a later time.

Step 8

Click Submit to create a job for deleting the gateway
                                       			 records.

Step 9

Use the Job
                                       			 Scheduler option in the Bulk
                                          				Administration main menu to schedule and/or activate this job.

Caution

## Topics Related to Cisco Gateway Deletions

| Caution | The delete action is final. You cannot retrieve deleted records. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Gateways > Delete
                                             				  Gateways . |
|---|---|
| Step 2 | From the Delete Gateways where drop-down list, choose one of the following options: Name Description DN/Route Pattern Calling Search Space Device Pool Device Type |
| Step 3 | From the second Find Gateways where drop-down list, choose one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 4 | From the third drop-down list, choose Show to display the associated endpoints. |
| Step 5 | Specify the
                                       			 appropriate search text, if applicable, and click Find . Tip To find all gateways that are registered in the database, click Find without entering any search text. To further
                                          				define your query, you can choose AND or OR to add multiple filters and repeat Step 2 through Step 5 . A list of discovered templates displays by: Device Name Description Device Pool Status IP address | Tip | To find all gateways that are registered in the database, click Find without entering any search text. |
| Tip | To find all gateways that are registered in the database, click Find without entering any search text. |
| Step 6 | In the Job
                                          				Information area, enter the Job description. |
| Step 7 | Choose a delete
                                       			 method. Do one of the following: Click Run
                                                					 Immediately to delete gateways immediately. Click Run
                                                					 Later to delete gateways at a later time. |
| Step 8 | Click Submit to create a job for deleting the gateway
                                       			 records. |
| Step 9 | Use the Job
                                       			 Scheduler option in the Bulk
                                          				Administration main menu to schedule and/or activate this job. Caution If you do not enter any information in the query text box, the system deletes all gateway records. The delete action is final.
                                                   You cannot retrieve deleted records. | Caution | If you do not enter any information in the query text box, the system deletes all gateway records. The delete action is final.
                                                   You cannot retrieve deleted records. |
| Caution | If you do not enter any information in the query text box, the system deletes all gateway records. The delete action is final.
                                                   You cannot retrieve deleted records. |

| Tip | To find all gateways that are registered in the database, click Find without entering any search text. |
|---|---|

| Caution | If you do not enter any information in the query text box, the system deletes all gateway records. The delete action is final.
                                                   You cannot retrieve deleted records. |
|---|---|