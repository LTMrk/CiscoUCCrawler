---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-0f699ed196
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_0101100.html
retrieved_at: 2026-08-21T18:00:40.066295+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: Line Attribute Updates for Devices and User Device Profiles

## Chapter: Line Attribute Updates for Devices and User Device Profiles

# Line Attribute Updates for Devices and User Device Profiles

This chapter provides information to use a query to update lines
                        		for devices and User Device Profiles.

## Device and UDP Line Updates

You can use a query to update lines for devices and User Device Profiles. To
                              		update line attributes for a specific group of devices or user device profiles,
                              		use the Update Lines option. Lines for a phone and a user device profile get
                              		updated at the same time when both are part of the query result.

Tip

When a phone is deleted from the Cisco Unified Communications Manager database, the directory number remains in the
                                          		  database. To manage these orphan directory numbers, you can use the Update
                                          		  Lines option to search for unassigned directory numbers and delete or update
                                          		  these directory numbers.

## Update Device and UDP Lines Using Query

Use a query to update lines in devices and user device
                              		  profiles.

Step 1

Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > Add/Update Lines > Update
                                             				  Lines .

The Update Lines Query window displays.

You can update all lines by not specifying a query. Skip to 2 .

Step 2

From the first Find Line where drop-down list box, choose one
                                       			 of the following criteria:

Directory Number

Route Pattern

Line Description

Calling Search Space (Phone)

Calling Search Space (Line)

Device Pool

Device Description

Line Position

Unassigned DN

Call Pickup Group

To locate and delete orphaned directory numbers, use "Unassigned DN."

Step 3

From the second Find Line where drop-down list box, choose one
                                       			 of the following criteria:

begins with

contains

is exactly

ends with

is empty

is not empty

Step 4

In the search field list box, choose or enter the value that you
                                       			 want to locate.

For example, you can choose the Line Partition from the list or
                                          				enter a range of directory numbers.

Tip

To find all lines that are registered in the database, click Find without entering any search text.

Step 5

To further define your query and to add multiple filters, check
                                       			 the Search Within Results check box, choose AND or OR from the drop-down box, and repeat 2 and 3 .

Step 6

To display the records that are going to be affected, click Find .

A list of discovered lines displays by

Pattern/Directory Number

Partition

Description

Step 7

Click Next .

Tip

If you want to change the type of query, click Back .

Step 8

Specify the setting that you want to update for all the records
                                       			 that you have defined in your query. You can choose multiple parameters to
                                       			 update. See BAT Template Phone Line Field Descriptions for field descriptions.

Values that display in some fields display from Cisco Unified Communications Manager . You must configure these values by using Cisco Unified Communications Manager Administration.

Step 9

In the Job Information area, enter the Job description.

Step 10

Choose an insert method. Do one of the following:

Click Run Immediately to insert lines
                                             				  immediately.

Click Run Later to insert lines at a later time.

Step 11

Click Submit to create a job for inserting the phone
                                       			 records.

If any information for a line record fails, Cisco Unified Communications Manager Bulk Administration (BAT) does not update that
                                                      				  line record.

## Topics Related to User Device Profile Line Updates

| Tip | When a phone is deleted from the Cisco Unified Communications Manager database, the directory number remains in the
                                          		  database. To manage these orphan directory numbers, you can use the Update
                                          		  Lines option to search for unassigned directory numbers and delete or update
                                          		  these directory numbers. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > Add/Update Lines > Update
                                             				  Lines . The Update Lines Query window displays. Note You can update all lines by not specifying a query. Skip to 2 . | Note | You can update all lines by not specifying a query. Skip to 2 . |
|---|---|---|---|
| Note | You can update all lines by not specifying a query. Skip to 2 . |
| Step 2 | From the first Find Line where drop-down list box, choose one
                                       			 of the following criteria: Directory Number Route Pattern Line Description Calling Search Space (Phone) Calling Search Space (Line) Device Pool Device Description Line Position Unassigned DN Call Pickup Group Note To locate and delete orphaned directory numbers, use "Unassigned DN." | Note | To locate and delete orphaned directory numbers, use "Unassigned DN." |
| Note | To locate and delete orphaned directory numbers, use "Unassigned DN." |
| Step 3 | From the second Find Line where drop-down list box, choose one
                                       			 of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 4 | In the search field list box, choose or enter the value that you
                                       			 want to locate. For example, you can choose the Line Partition from the list or
                                          				enter a range of directory numbers. Tip To find all lines that are registered in the database, click Find without entering any search text. | Tip | To find all lines that are registered in the database, click Find without entering any search text. |
| Tip | To find all lines that are registered in the database, click Find without entering any search text. |
| Step 5 | To further define your query and to add multiple filters, check
                                       			 the Search Within Results check box, choose AND or OR from the drop-down box, and repeat 2 and 3 . |
| Step 6 | To display the records that are going to be affected, click Find . A list of discovered lines displays by Pattern/Directory Number Partition Description |
| Step 7 | Click Next . The Update Lines window shows the type of query that
                                       			 you chose at the top. Tip If you want to change the type of query, click Back . | Tip | If you want to change the type of query, click Back . |
| Tip | If you want to change the type of query, click Back . |
| Step 8 | Specify the setting that you want to update for all the records
                                       			 that you have defined in your query. You can choose multiple parameters to
                                       			 update. See BAT Template Phone Line Field Descriptions for field descriptions. Note Values that display in some fields display from Cisco Unified Communications Manager . You must configure these values by using Cisco Unified Communications Manager Administration. | Note | Values that display in some fields display from Cisco Unified Communications Manager . You must configure these values by using Cisco Unified Communications Manager Administration. |
| Note | Values that display in some fields display from Cisco Unified Communications Manager . You must configure these values by using Cisco Unified Communications Manager Administration. |
| Step 9 | In the Job Information area, enter the Job description. |
| Step 10 | Choose an insert method. Do one of the following: Click Run Immediately to insert lines
                                             				  immediately. Click Run Later to insert lines at a later time. |
| Step 11 | Click Submit to create a job for inserting the phone
                                       			 records. Use the Job Configuration window to schedule
                                       			 and / or activate this job. Note If any information for a line record fails, Cisco Unified Communications Manager Bulk Administration (BAT) does not update that
                                                      				  line record. | Note | If any information for a line record fails, Cisco Unified Communications Manager Bulk Administration (BAT) does not update that
                                                      				  line record. |
| Note | If any information for a line record fails, Cisco Unified Communications Manager Bulk Administration (BAT) does not update that
                                                      				  line record. |

| Note | You can update all lines by not specifying a query. Skip to 2 . |
|---|---|

| Note | To locate and delete orphaned directory numbers, use "Unassigned DN." |
|---|---|

| Tip | To find all lines that are registered in the database, click Find without entering any search text. |
|---|---|

| Tip | If you want to change the type of query, click Back . |
|---|---|

| Note | Values that display in some fields display from Cisco Unified Communications Manager . You must configure these values by using Cisco Unified Communications Manager Administration. |
|---|---|

| Note | If any information for a line record fails, Cisco Unified Communications Manager Bulk Administration (BAT) does not update that
                                                      				  line record. |
|---|---|