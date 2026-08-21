---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-14su1-cucm-b-bulk-administration-guide-14su1-cucm-b-bulk-administra-f1f5ab3fe7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/14SU1/cucm_b_bulk-administration-guide-14SU1/cucm_b_bulk-administration-guide-1251su2_chapter_01000.html
retrieved_at: 2026-08-21T09:08:23.069162+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: October 27, 2021

Chapter: Phone Deletions

## Chapter: Phone Deletions

# Phone Deletions

This chapter provides information to delete a group of phones or
                        		other IP telephony devices from the Cisco Unified Communications Manager database. You can locate existing phone
                        		records that you want to delete using either a query or a custom file. You can
                        		also search for and delete unassigned directory numbers.

## Delete Phones Using Query

Create a query to locate phone records for deletion.

Caution

The delete action is final. You cannot retrieve deleted records.

Step 1

Choose Bulk
                                             				  Administration > Phones > Delete
                                             				  Phones > Query .

Step 2

From the first Find Phone where drop-down list box, choose
                                       			 one of the following criteria:

- Device Name

- Description

- Directory Number

- Calling Search Space

- Device Pool

- Device Type

- Call Pickup Group

- LSC Status

- Authentication String

- Device Protocol

- Security Profile

- Unassigned DN

Last Registered

Last Active

From the second Find Phone where drop-down list box, choose
                                          				one of the following criteria:

- begins with

- contains

- is exactly

- ends with

- is empty

- is not empty

Step 3

Specify the appropriate search text, if applicable.

Tip

To find all phones that are registered in the database, click Find without entering any search text.

Step 4

To further define your query and to add multiple filters, check
                                       			 the Search Within Results check box, choose AND or OR from the drop-down box, repeat Step 2 and Step 3 .

Step 5

Click Find .

A list of discovered phones displays by

- Device Name

- Description

- Device Pool

- Device Protocol

- Status

Last Registered

Last Active

Unified CM

- IP Address

Step 6

In the Job Information area, enter the Job description.

Step 7

Choose a deletion method. Do one of the following:

Click Run Immediately to delete phone records
                                             				  immediately

Click Run Later to delete the phone records at a
                                             				  later time.

Caution

If you do not enter any information in the query text box, the
                                                      				  system deletes all phone records. The delete action is final. You cannot
                                                      				  retrieve deleted records.

Step 8

Click Submit to create a job for deleting the phone
                                       			 records.

Make sure you browse the entire list of displayed results before
                                                      				  submitting the job.

To schedule and/or activate this job, use the Job Configuration window.

## Delete Phones Using Custom File

You can create a custom file of phones that you want to
                              		  delete using a text editor. You can have MAC addresses and device names in the
                              		  same custom file, but you cannot have directory numbers in the same file. You
                              		  need to create separate files—one file that contains the device names and MAC
                              		  addresses and another file that contains the directory numbers.

Do not use the insert or export transaction files that are created
                                          			 with bat.xlt for the delete transaction. Instead, you must create a custom file
                                          			 with details of the phone records that need to be deleted. Use only this file
                                          			 for the delete transaction.

Caution

The delete action is final. You cannot retrieve deleted records.

### Before you begin

Device names

Description

Directory numbers

Enter values for device name, description, or directory number
                                                				  in the custom delete file. You do not need to include a header in the custom
                                                				  delete file.

- Upload the custom file to Unified Communications Manager server.

Step 1

Choose Bulk
                                             				  Administration > Phones > Delete
                                             				  Phones > Custom File .

Step 2

In the Delete Phones where drop-down list box, choose
                                       			 the type of custom file that you have created from one of the following
                                       			 criteria:

- Device Name

- Directory Number

- Description

Step 3

In the list of custom files, choose the filename of the custom
                                       			 file for this delete.

Step 4

Click Find . A list of phones matching your search
                                       			 criteria display.

Step 5

In the Job Information area, enter the Job description.

Step 6

Choose a deletion method. Do one of the following:

Click Run Immediately to delete phone records
                                             				  immediately

Click Run Later to delete the phone records at a
                                             				  later time.

Caution

The delete action is final. You cannot retrieve deleted records.

Step 7

Click Submit to create a job for deleting the phone
                                       			 records.

## Delete Unassigned Directory Numbers

Delete unassigned directory numbers for phone records that
                              		  you locate using query.

Caution

The delete action is final. You cannot retrieve deleted unassigned
                                          			 directory numbers.

Step 1

Choose Bulk
                                             				  Administration > Phones > Delete
                                             				  Phones > Delete Unassigned DN .

Step 2

From the first Delete Bulk Unassigned Directory Number where drop-down list box, choose one of the following criteria:

- Pattern

- Description

- Route Partition

From the second Delete Bulk Unassigned Directory Number
                                             				  where drop-down list box, choose one of the following criteria:

- begins with

- contains

- is exactly

- ends with

- is empty

- is not empty

Step 3

Specify the appropriate search text, if applicable.

Step 4

Click Find .

A list of discovered phones displays by the following criteria:

- Pattern

- Description

- Partition

Tip

To find all unassigned directory numbers that are registered in
                                                      				  the database, click Find without entering any search text.

Step 5

In the Job Information area, enter the Job description.

The default description is Delete Unassigned DN - Query.

Step 6

Choose a deletion method. Do one of the following:

Click Run Immediately to delete the unassigned
                                             				  directory numbers immediately.

Click Run Later to delete the phone records at a later time.

Caution

The delete action is final. You cannot retrieve deleted
                                                      				  unassigned directory numbers.

Step 7

Click Submit to create a job for deleting the phone
                                       			 records.

Make sure you browse the entire list of displayed results before
                                                      				  submitting the job.

To schedule and/or activate this job, use the Job Configuration window.

| Caution | The delete action is final. You cannot retrieve deleted records. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Phones > Delete
                                             				  Phones > Query . The Bulk Phones Delete Configuration window
                                       			 displays. |
|---|---|
| Step 2 | From the first Find Phone where drop-down list box, choose
                                       			 one of the following criteria: Device Name Description Directory Number Calling Search Space Device Pool Device Type Call Pickup Group LSC Status Authentication String Device Protocol Security Profile Unassigned DN Last Registered Last Active From the second Find Phone where drop-down list box, choose
                                          				one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 3 | Specify the appropriate search text, if applicable. Tip To find all phones that are registered in the database, click Find without entering any search text. | Tip | To find all phones that are registered in the database, click Find without entering any search text. |
| Tip | To find all phones that are registered in the database, click Find without entering any search text. |
| Step 4 | To further define your query and to add multiple filters, check
                                       			 the Search Within Results check box, choose AND or OR from the drop-down box, repeat Step 2 and Step 3 . |
| Step 5 | Click Find . A list of discovered phones displays by Device Name Description Device Pool Device Protocol Status Last Registered Last Active Unified CM IP Address |
| Step 6 | In the Job Information area, enter the Job description. |
| Step 7 | Choose a deletion method. Do one of the following: Click Run Immediately to delete phone records
                                             				  immediately Click Run Later to delete the phone records at a
                                             				  later time. Caution If you do not enter any information in the query text box, the
                                                      				  system deletes all phone records. The delete action is final. You cannot
                                                      				  retrieve deleted records. | Caution | If you do not enter any information in the query text box, the
                                                      				  system deletes all phone records. The delete action is final. You cannot
                                                      				  retrieve deleted records. |
| Caution | If you do not enter any information in the query text box, the
                                                      				  system deletes all phone records. The delete action is final. You cannot
                                                      				  retrieve deleted records. |
| Step 8 | Click Submit to create a job for deleting the phone
                                       			 records. Note Make sure you browse the entire list of displayed results before
                                                      				  submitting the job. To schedule and/or activate this job, use the Job Configuration window. | Note | Make sure you browse the entire list of displayed results before
                                                      				  submitting the job. |
| Note | Make sure you browse the entire list of displayed results before
                                                      				  submitting the job. |

| Tip | To find all phones that are registered in the database, click Find without entering any search text. |
|---|---|

| Caution | If you do not enter any information in the query text box, the
                                                      				  system deletes all phone records. The delete action is final. You cannot
                                                      				  retrieve deleted records. |
|---|---|

| Note | Make sure you browse the entire list of displayed results before
                                                      				  submitting the job. |
|---|---|

| Note | Do not use the insert or export transaction files that are created
                                          			 with bat.xlt for the delete transaction. Instead, you must create a custom file
                                          			 with details of the phone records that need to be deleted. Use only this file
                                          			 for the delete transaction. |
|---|---|

| Caution | The delete action is final. You cannot retrieve deleted records. |
|---|---|

| Note | Enter values for device name, description, or directory number
                                                				  in the custom delete file. You do not need to include a header in the custom
                                                				  delete file. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Phones > Delete
                                             				  Phones > Custom File . The Bulk Phones Delete Configuration window
                                       			 displays. |
|---|---|
| Step 2 | In the Delete Phones where drop-down list box, choose
                                       			 the type of custom file that you have created from one of the following
                                       			 criteria: Device Name Directory Number Description |
| Step 3 | In the list of custom files, choose the filename of the custom
                                       			 file for this delete. |
| Step 4 | Click Find . A list of phones matching your search
                                       			 criteria display. |
| Step 5 | In the Job Information area, enter the Job description. |
| Step 6 | Choose a deletion method. Do one of the following: Click Run Immediately to delete phone records
                                             				  immediately Click Run Later to delete the phone records at a
                                             				  later time. Caution The delete action is final. You cannot retrieve deleted records. | Caution | The delete action is final. You cannot retrieve deleted records. |
| Caution | The delete action is final. You cannot retrieve deleted records. |
| Step 7 | Click Submit to create a job for deleting the phone
                                       			 records. To schedule and/or activate this job, use the Job Configuration window. |

| Caution | The delete action is final. You cannot retrieve deleted records. |
|---|---|

| Caution | The delete action is final. You cannot retrieve deleted unassigned
                                          			 directory numbers. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Phones > Delete
                                             				  Phones > Delete Unassigned DN . The Delete Unassigned Directory Numbers window displays. |
|---|---|
| Step 2 | From the first Delete Bulk Unassigned Directory Number where drop-down list box, choose one of the following criteria: Pattern Description Route Partition From the second Delete Bulk Unassigned Directory Number
                                             				  where drop-down list box, choose one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 3 | Specify the appropriate search text, if applicable. |
| Step 4 | Click Find . A list of discovered phones displays by the following criteria: Pattern Description Partition Tip To find all unassigned directory numbers that are registered in
                                                      				  the database, click Find without entering any search text. | Tip | To find all unassigned directory numbers that are registered in
                                                      				  the database, click Find without entering any search text. |
| Tip | To find all unassigned directory numbers that are registered in
                                                      				  the database, click Find without entering any search text. |
| Step 5 | In the Job Information area, enter the Job description. The default description is Delete Unassigned DN - Query. |
| Step 6 | Choose a deletion method. Do one of the following: Click Run Immediately to delete the unassigned
                                             				  directory numbers immediately. Click Run Later to delete the phone records at a later time. Caution The delete action is final. You cannot retrieve deleted
                                                      				  unassigned directory numbers. | Caution | The delete action is final. You cannot retrieve deleted
                                                      				  unassigned directory numbers. |
| Caution | The delete action is final. You cannot retrieve deleted
                                                      				  unassigned directory numbers. |
| Step 7 | Click Submit to create a job for deleting the phone
                                       			 records. Note Make sure you browse the entire list of displayed results before
                                                      				  submitting the job. To schedule and/or activate this job, use the Job Configuration window. | Note | Make sure you browse the entire list of displayed results before
                                                      				  submitting the job. |
| Note | Make sure you browse the entire list of displayed results before
                                                      				  submitting the job. |

| Tip | To find all unassigned directory numbers that are registered in
                                                      				  the database, click Find without entering any search text. |
|---|---|

| Caution | The delete action is final. You cannot retrieve deleted
                                                      				  unassigned directory numbers. |
|---|---|

| Note | Make sure you browse the entire list of displayed results before
                                                      				  submitting the job. |
|---|---|