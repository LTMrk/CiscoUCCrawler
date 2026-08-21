---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-14su1-cucm-b-bulk-administration-guide-14su1-cucm-b-bulk-administra-7f68a2f96a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/14SU1/cucm_b_bulk-administration-guide-14SU1/cucm_b_bulk-administration-guide-1251su2_chapter_01011.html
retrieved_at: 2026-08-21T09:08:35.890352+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: October 27, 2021

Chapter: Phone Resets and Restarts

## Chapter: Phone Resets and Restarts

# Phone Resets and Restarts

This chapter provides information to reset or restart devices without updating any
                        		attributes. Use this procedure if a problem arises, and you must reset or
                        		restart the phones with a bulk transaction. You can locate phones that you want
                        		to reset using either a query or a custom file.

## Reset or Restart Phone Using Query

You can create a query to locate phones that you want to reset
                              		  or restart.

Step 1

Choose Bulk
                                             				  Administration > Phones > Reset/Restart
                                             				  Phones > Query .

Step 2

From the first Find Phones where drop-down list box, choose
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

- Common Device
                                             				  Configuration

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

To further define your query, you can choose AND or OR to add multiple filters and repeat Step 2 and Step 3 .

Step 5

Click Find .

A list of discovered templates displays by

- Device Name

- Description

- Device Pool

- Device Protocol

- Status

- IP Address

Step 6

From the list of records, click the device name that matches your
                                       			 search criteria.

Step 7

Click one of the following options:

- Reset—To reset
                                             				  (power-cycle) the phones

- Restart—To reset
                                             				  phones without power-cycling

- Apply Config—To reset
                                             				  only the settings that have changed since the last reset

Step 8

In the Job Information area, enter the Job description.

Step 9

Choose an insert method. Do one of the following:

Click Run Immediately to insert phone records
                                             				  immediately.

Click Run Later to insert phone records at a
                                             				  later time.

Step 10

To create a job for inserting the phone records, click Submit .

## Reset or Restart Phone Using Custom File

You can create a custom file of phones that you want to reset
                              		  or restart using a text editor. You can use either device names or directory
                              		  numbers in the custom file.

### Before you begin

Device names

Description

Directory numbers

Put each item on a separate line in the text file.

- Upload the file to the first node of Unified Communications Manager .

Step 1

Choose Bulk
                                             				  Administration > Phones > Reset/Restart
                                             				  Phones > Custom File .

Step 2

In the Update Phones where drop-down list box, choose
                                       			 the type of custom file that you have created from one of the following
                                       			 criteria:

- Device Name

- Directory Number

- Description

Step 3

In the list of custom files, choose the filename of the custom
                                       			 file for this update and then click Find .

Caution

If no information is entered into the query text box, the system
                                                      				  resets or restarts all phones.

Step 4

Click one of the following

- Reset—To reset
                                             				  (power-cycle) the phones

- Restart—To reset
                                             				  phones without power-cycling

- Apply Config—To reset
                                             				  only the settings that have changed since the last reset

Step 5

In the Job Information area, enter the Job
                                       			 description.

Step 6

Choose an insert method. Do one of the following:

Click Run Immediately to insert phone records
                                             				  immediately.

Click Run Later to insert phone records at a
                                             				  later time.

Step 7

To create a job for inserting the phone records, click Submit .

## Wipe or Lock Phones Using Query

You can create a query to locate phones that you want to wipe and/or lock.

Caution

The wipe operation cannot be undone. You should only perform this
                                          operation when you are sure you want to reset the phone to its
                                          factory
                                          settings.

Step 1

Choose Bulk
                                             				  Administration > Phones > Wipe and Lock Phones > Query .

Step 2

From the first Find Phones where drop-down list box, choose
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

- Common Device
                                             				  Configuration

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

To further define your query, you can choose AND or OR to add multiple filters and repeat 2 and 3 .

Step 5

Click Find .

A list of discovered templates displays by

- Device Name

- Description

- Device Pool

- Device Protocol

- Status

- IP Address

Step 6

From the list of records, click the device name that matches your
                                       			 search criteria.

Step 7

Click one of the following options:

- Lock—To lock the phones

- Wipe—To wipe the phones

- Wipe and Lock—To wipe and lock the phones

If a phone does not support the functionality you have chosen, the transaction will fail
                                                      for that phone. It will also fail if the functionality has already been requested for the phone.

Step 8

In the Job Information area, enter the Job description.

Step 9

Choose an insert method. Do one of the following:

Click Run Immediately to wipe or lock phones
                                             				  immediately.

Click Run Later to wipe or lock phones at a
                                             				  later time.

Step 10

To create a job for locking and/or wiping the phones, click Submit .

## Wipe or Lock Phones Using Custom File

You can create a custom file of phones that you want to wipe and/or lock using a text editor. You can use either device names
                              or directory
                              		  numbers in the custom file.

### Before you begin

Caution

The wipe operation cannot be undone. You should only perform this
                                          operation when you are sure you want to reset the phone to its
                                          factory
                                          settings.

Device names

Description

Directory numbers

Put each item on a separate line in the text file.

- Upload the file to the first node of Unified Communications Manager .

Step 1

Choose Bulk
                                             				  Administration > Phones > Wipe and Lock Phones > Custom File .

Step 2

In the Update Phones where drop-down list box, choose
                                       			 the type of custom file that you have created from one of the following
                                       			 criteria:

- Device Name

- Directory Number

- Description

Step 3

In the list of custom files, choose the filename of the custom
                                       			 file for this update and then click Find .

Caution

If no information is entered into the query text box, the system
                                                      				  wipes or locks all phones.

Step 4

Click one of the following:

- Lock—To lock the phones

- Wipe—To wipe the phones

- Wipe and Lock—To wipe and lock the phones

If a phone does not support the functionality you have chosen, the transaction will fail
                                                      for that phone. It will also fail if the functionality has already been requested for the phone.

Step 5

In the Job Information area, enter the Job
                                       			 description.

Step 6

Choose an insert method. Do one of the following:

Click Run Immediately to wipe or lock phones
                                             				  immediately.

Click Run Later to wipe or lock phones at a
                                             				  later time.

Step 7

To create a job for locking and/or wiping the phones, click Submit .

| Step 1 | Choose Bulk
                                             				  Administration > Phones > Reset/Restart
                                             				  Phones > Query . The Reset/Restart Phones Configuration window
                                       			 displays. |
|---|---|
| Step 2 | From the first Find Phones where drop-down list box, choose
                                       			 one of the following criteria: Device Name Description Directory Number Calling Search Space Device Pool Device Type Call Pickup Group LSC Status Authentication String Device Protocol Security Profile Common Device
                                             				  Configuration From the second Find Phone where drop-down list box, choose
                                          				one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 3 | Specify the appropriate search text, if applicable. Tip To find all phones that are registered in the database, click Find without entering any search text. | Tip | To find all phones that are registered in the database, click Find without entering any search text. |
| Tip | To find all phones that are registered in the database, click Find without entering any search text. |
| Step 4 | To further define your query, you can choose AND or OR to add multiple filters and repeat Step 2 and Step 3 . |
| Step 5 | Click Find . A list of discovered templates displays by Device Name Description Device Pool Device Protocol Status IP Address |
| Step 6 | From the list of records, click the device name that matches your
                                       			 search criteria. |
| Step 7 | Click one of the following options: Reset—To reset
                                             				  (power-cycle) the phones Restart—To reset
                                             				  phones without power-cycling Apply Config—To reset
                                             				  only the settings that have changed since the last reset |
| Step 8 | In the Job Information area, enter the Job description. |
| Step 9 | Choose an insert method. Do one of the following: Click Run Immediately to insert phone records
                                             				  immediately. Click Run Later to insert phone records at a
                                             				  later time. |
| Step 10 | To create a job for inserting the phone records, click Submit . To schedule this job, activate this job, or both, use the Job Configuration window. |

| Tip | To find all phones that are registered in the database, click Find without entering any search text. |
|---|---|

| Note | Put each item on a separate line in the text file. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Phones > Reset/Restart
                                             				  Phones > Custom File . The Reset/Restart Phones Custom Configuration window
                                       			 displays. |
|---|---|
| Step 2 | In the Update Phones where drop-down list box, choose
                                       			 the type of custom file that you have created from one of the following
                                       			 criteria: Device Name Directory Number Description |
| Step 3 | In the list of custom files, choose the filename of the custom
                                       			 file for this update and then click Find . Caution If no information is entered into the query text box, the system
                                                      				  resets or restarts all phones. | Caution | If no information is entered into the query text box, the system
                                                      				  resets or restarts all phones. |
| Caution | If no information is entered into the query text box, the system
                                                      				  resets or restarts all phones. |
| Step 4 | Click one of the following Reset—To reset
                                             				  (power-cycle) the phones Restart—To reset
                                             				  phones without power-cycling Apply Config—To reset
                                             				  only the settings that have changed since the last reset |
| Step 5 | In the Job Information area, enter the Job
                                       			 description. |
| Step 6 | Choose an insert method. Do one of the following: Click Run Immediately to insert phone records
                                             				  immediately. Click Run Later to insert phone records at a
                                             				  later time. |
| Step 7 | To create a job for inserting the phone records, click Submit . To schedule and / or activate this job, use the Job Configuration window. |

| Caution | If no information is entered into the query text box, the system
                                                      				  resets or restarts all phones. |
|---|---|

| Caution | The wipe operation cannot be undone. You should only perform this
                                          operation when you are sure you want to reset the phone to its
                                          factory
                                          settings. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Phones > Wipe and Lock Phones > Query . The Wipe and Lock Phones Configuration window
                                       			 displays. |
|---|---|
| Step 2 | From the first Find Phones where drop-down list box, choose
                                       			 one of the following criteria: Device Name Description Directory Number Calling Search Space Device Pool Device Type Call Pickup Group LSC Status Authentication String Device Protocol Security Profile Common Device
                                             				  Configuration From the second Find Phone where drop-down list box, choose
                                          				one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 3 | Specify the appropriate search text, if applicable. Tip To find all phones that are registered in the database, click Find without entering any search text. | Tip | To find all phones that are registered in the database, click Find without entering any search text. |
| Tip | To find all phones that are registered in the database, click Find without entering any search text. |
| Step 4 | To further define your query, you can choose AND or OR to add multiple filters and repeat 2 and 3 . |
| Step 5 | Click Find . A list of discovered templates displays by Device Name Description Device Pool Device Protocol Status IP Address |
| Step 6 | From the list of records, click the device name that matches your
                                       			 search criteria. |
| Step 7 | Click one of the following options: Lock—To lock the phones Wipe—To wipe the phones Wipe and Lock—To wipe and lock the phones Note If a phone does not support the functionality you have chosen, the transaction will fail
                                                      for that phone. It will also fail if the functionality has already been requested for the phone. | Note | If a phone does not support the functionality you have chosen, the transaction will fail
                                                      for that phone. It will also fail if the functionality has already been requested for the phone. |
| Note | If a phone does not support the functionality you have chosen, the transaction will fail
                                                      for that phone. It will also fail if the functionality has already been requested for the phone. |
| Step 8 | In the Job Information area, enter the Job description. |
| Step 9 | Choose an insert method. Do one of the following: Click Run Immediately to wipe or lock phones
                                             				  immediately. Click Run Later to wipe or lock phones at a
                                             				  later time. |
| Step 10 | To create a job for locking and/or wiping the phones, click Submit . To schedule and / or activate this job, use the Job Configuration window. |

| Tip | To find all phones that are registered in the database, click Find without entering any search text. |
|---|---|

| Note | If a phone does not support the functionality you have chosen, the transaction will fail
                                                      for that phone. It will also fail if the functionality has already been requested for the phone. |
|---|---|

| Caution | The wipe operation cannot be undone. You should only perform this
                                          operation when you are sure you want to reset the phone to its
                                          factory
                                          settings. |
|---|---|

| Note | Put each item on a separate line in the text file. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Phones > Wipe and Lock Phones > Custom File . The Wipe and Lock Phones Configuration window
                                       			 displays. |
|---|---|
| Step 2 | In the Update Phones where drop-down list box, choose
                                       			 the type of custom file that you have created from one of the following
                                       			 criteria: Device Name Directory Number Description |
| Step 3 | In the list of custom files, choose the filename of the custom
                                       			 file for this update and then click Find . Caution If no information is entered into the query text box, the system
                                                      				  wipes or locks all phones. | Caution | If no information is entered into the query text box, the system
                                                      				  wipes or locks all phones. |
| Caution | If no information is entered into the query text box, the system
                                                      				  wipes or locks all phones. |
| Step 4 | Click one of the following: Lock—To lock the phones Wipe—To wipe the phones Wipe and Lock—To wipe and lock the phones Note If a phone does not support the functionality you have chosen, the transaction will fail
                                                      for that phone. It will also fail if the functionality has already been requested for the phone. | Note | If a phone does not support the functionality you have chosen, the transaction will fail
                                                      for that phone. It will also fail if the functionality has already been requested for the phone. |
| Note | If a phone does not support the functionality you have chosen, the transaction will fail
                                                      for that phone. It will also fail if the functionality has already been requested for the phone. |
| Step 5 | In the Job Information area, enter the Job
                                       			 description. |
| Step 6 | Choose an insert method. Do one of the following: Click Run Immediately to wipe or lock phones
                                             				  immediately. Click Run Later to wipe or lock phones at a
                                             				  later time. |
| Step 7 | To create a job for locking and/or wiping the phones, click Submit . To schedule and / or activate this job, use the Job Configuration window. |

| Caution | If no information is entered into the query text box, the system
                                                      				  wipes or locks all phones. |
|---|---|

| Note | If a phone does not support the functionality you have chosen, the transaction will fail
                                                      for that phone. It will also fail if the functionality has already been requested for the phone. |
|---|---|