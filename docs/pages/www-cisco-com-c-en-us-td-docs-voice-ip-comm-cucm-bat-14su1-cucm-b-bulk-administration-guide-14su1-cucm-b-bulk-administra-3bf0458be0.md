---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-14su1-cucm-b-bulk-administration-guide-14su1-cucm-b-bulk-administra-3bf0458be0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/14SU1/cucm_b_bulk-administration-guide-14SU1/cucm_b_bulk-administration-guide-1251su2_chapter_0110100.html
retrieved_at: 2026-08-21T09:11:28.537037+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: October 27, 2021

Chapter: Cisco Gateway Report Generation

## Chapter: Cisco Gateway Report Generation

- Cisco Gateway Report Generation

- Generate Cisco Gateway Reports

- Topics Related to Cisco Gateway Reports

# Cisco Gateway Report Generation

This chapter provides information to generate reports for VGXXX
                        		Gateways.

Reports can be generated only for VG200, VG224, VG202, VG310, VG320, VG350, VG450, ISR 4461, , , VG420, and VG204 gateways.

## Generate Cisco Gateway Reports

You can generate a report for all VGXXX Gateways or for a
                              		  limited set of gateways. Reports for VGXXX Gateways have a fixed format.

Step 1

Choose Bulk
                                             				  Administration > Gateways > Generate
                                             				  Gateway Reports .

Step 2

From the Find Gateways where drop-down list, choose one of the following options:

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

Specify the appropriate search text, if applicable, and click Find .

Tip

To further define your query, you can choose AND or OR to add multiple filters and repeat Step 2 through Step 5 .

A list of discovered templates displays by:

Device Name

Description

Device Pool

Status

IP address

Step 6

Click Next to choose details for your type of
                                       			 report.

Step 7

In the File Name field, enter your name for this
                                       			 report (required).

Step 8

Choose the file format from the drop-down list.

Step 9

In the Job Information area, enter the Job description.

Step 10

Choose when to generate a report. Do one of the following:

Click Run Immediately to generate a report
                                             				  immediately.

Click Run Later to generate a report at a later
                                             				  time.

Step 11

Click Submit to create a job for generating the
                                       			 report.

### What to do next

You can search and download the report file using the Upload/Download Files option in the Bulk Administration menu.

## Topics Related to Cisco Gateway Reports

| Note | Reports can be generated only for VG200, VG224, VG202, VG310, VG320, VG350, VG450, ISR 4461, , , VG420, and VG204 gateways. |
|---|---|

| Note | Reports can be generated only for VG200, VG224, VG202, VG310, VG320, VG350, VG450, ISR 4461, , , VG420, and VG204 gateways. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Gateways > Generate
                                             				  Gateway Reports . |
|---|---|
| Step 2 | From the Find Gateways where drop-down list, choose one of the following options: Name Description DN/Route Pattern Calling Search Space Device Pool Device Type |
| Step 3 | From the second Find Gateways where drop-down list, choose one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 4 | From the third drop-down list, choose Show to display the associated endpoints. |
| Step 5 | Specify the appropriate search text, if applicable, and click Find . Tip To find all gateways that are registered in the database, click Find without entering any search text. To further define your query, you can choose AND or OR to add multiple filters and repeat Step 2 through Step 5 . A list of discovered templates displays by: Device Name Description Device Pool Status IP address | Tip | To find all gateways that are registered in the database, click Find without entering any search text. |
| Tip | To find all gateways that are registered in the database, click Find without entering any search text. |
| Step 6 | Click Next to choose details for your type of
                                       			 report. The Gateway Report Configuration window displays and shows
                                       			 the query that you chose. If you want to change the type of query, click Back . |
| Step 7 | In the File Name field, enter your name for this
                                       			 report (required). |
| Step 8 | Choose the file format from the drop-down list. |
| Step 9 | In the Job Information area, enter the Job description. |
| Step 10 | Choose when to generate a report. Do one of the following: Click Run Immediately to generate a report
                                             				  immediately. Click Run Later to generate a report at a later
                                             				  time. |
| Step 11 | Click Submit to create a job for generating the
                                       			 report. Use the Job Scheduler option in the Bulk Administration main menu to schedule and/or activate this job. |

| Tip | To find all gateways that are registered in the database, click Find without entering any search text. |
|---|---|