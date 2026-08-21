---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-0be3f79a33
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_01110.html
retrieved_at: 2026-08-21T17:56:17.199177+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: Intercom Additions and Updates

## Chapter: Intercom Additions and Updates

# Intercom Additions and Updates

The Intercom feature allows one user to call another user, and
                        		that call automatically gets answered with one-way media from caller to called
                        		party, regardless of whether the called party is busy or idle.

You can use the Add / Update Intercom utility to
                        		add or update intercoms in bulk to Cisco Unified Communications Manager server.

## Update Intercom DNs

You can update Intercom DNs for phones or devices.

Step 1

Choose which intercom DN to update. Do one of the following:

Choose Bulk
                                                   						Administration > Phones > Add/Update
                                                   						Intercom > Update Intercom
                                                   						Directory Numbers to update Phone intercom directory numbers.

Choose Bulk
                                                   						Administration > User Device
                                                   						Profiles > Add/Update Intercom > Update Intercom Directory Numbers to
                                             				  update User Device Profile intercom directory numbers.

Step 2

From the first Find and List Intercom Directory Numbers To Update where drop-down list, choose one of the following criteria:

Intercom Directory Number

Route Partition

Description

Step 3

From the second Find and List Intercom Directory Numbers To Update where drop-down list, choose one of the following criteria:

begins with

contains

ends with

is exactly

is empty

is not empty

Step 4

Specify the appropriate search text in the text field, if
                                       			 applicable.

Tip

Step 5

To further define your query, you can choose AND or OR to add multiple filters and repeat Step 2 and Step 3 .

Step 6

Click Find .

A list of discovered Intercom DNs displays by:

Intercom DN Pattern

Route Partition

Description

Step 7

Click Next .

Step 8

Specify the settings that you want to update for all the records
                                       			 that you have defined in your query.

## Add Intercom DNs

You can add Intercom DNs to a Unified Communications Manager server.

### Before you begin

You must have a data file in comma separated value (CSV) format that contains the unique details for the phones or other IP
                                    telephony devices.

Upload the data files by choosing the relevant target and function for the transaction.

Step 1

Choose Bulk Administration > Phones > Add/Update Intercom > Add Intercom Directory Numbers .

Step 2

In the File Name drop-down list box, choose the CSV
                                       			 data file that you created for this specific bulk transaction.

Step 3

In the Phone Template Name drop-down list, choose the BAT Phone template that you created for this type of bulk transaction.

Step 4

Check the Override Configuration Settings check box to
                                       			 update the existing phone button template settings with the information that is
                                       			 contained in the file that you want to insert.

Step 5

In the Job Information area, enter the Job description.

The default job description for this transaction specifies Insert
                                          				Intercom DNs.

Step 6

Choose a method to add Intercom DNs. Do one of the following:

Click Run Immediately to add Intercom DNs
                                             				  immediately.

Click Run Later to add Intercom DNs at a later
                                             				  time.

Step 7

To create a job for adding Intercom DNs, click Submit .

## Intercom DN Update Field Descriptions

The following table provides the field descriptions for
                              		  updating line details.

Field

Description

Intercom Directory Number Information

Route Partition

Choose a route partition to which the directory number
                                          					 belongs.

The directory number can appear in more than one partition.

Description

Enter a description that makes the device easy to recognize.
                                          					 The description can include up to 50 characters in any language, but it cannot
                                          					 include double-quotes ("), percentage sign ( % ),
                                          					 ampersand (&), or angle brackets (<>).

Alerting Name

This name represents the name that displays during an alert to
                                          					 a shared directory number. For non-shared directory numbers, during alerts, the
                                          					 system uses the name that is entered in the Display field.

ASCII Alerting Name

This field provides the same information as the Alerting Name field, but you must limit
                                          					 input to ASCII characters. Devices that do not support Unicode
                                          					 (internationalized) characters display the content of the Alerting Name ASCII field.

Intercom Directory Number Settings

Calling Search Space

Choose the calling search space to which this group of
                                          					 phones/ports should belong.

A calling search space specifies the collection of route
                                          					 partitions that are searched to determine how a dialed number should be routed.

Presence Group

Used with the Presence feature, the phone that is running SIP
                                          					 or SCCP serves as a watcher because it requests status about the presence
                                          					 entity, for example, directory number, that is configured as a BLF speed dial
                                          					 button on the phone.

If you want the phone to receive the status of the presence
                                          					 entity, choose a Presence Group that is allowed to view the status of the
                                          					 Presence Group that is applied to the directory number, as indicated in the Presence Group Configuration window.

| Step 1 | Choose which intercom DN to update. Do one of the following: Choose Bulk
                                                   						Administration > Phones > Add/Update
                                                   						Intercom > Update Intercom
                                                   						Directory Numbers to update Phone intercom directory numbers. Choose Bulk
                                                   						Administration > User Device
                                                   						Profiles > Add/Update Intercom > Update Intercom Directory Numbers to
                                             				  update User Device Profile intercom directory numbers. |
|---|---|
| Step 2 | From the first Find and List Intercom Directory Numbers To Update where drop-down list, choose one of the following criteria: Intercom Directory Number Route Partition Description |
| Step 3 | From the second Find and List Intercom Directory Numbers To Update where drop-down list, choose one of the following criteria: begins with contains ends with is exactly is empty is not empty |
| Step 4 | Specify the appropriate search text in the text field, if
                                       			 applicable. Tip To find all Intercom DNs that are registered in the database, click Find without entering any search text. | Tip | To find all Intercom DNs that are registered in the database, click Find without entering any search text. |
| Tip | To find all Intercom DNs that are registered in the database, click Find without entering any search text. |
| Step 5 | To further define your query, you can choose AND or OR to add multiple filters and repeat Step 2 and Step 3 . |
| Step 6 | Click Find . A list of discovered Intercom DNs displays by: Intercom DN Pattern Route Partition Description |
| Step 7 | Click Next . |
| Step 8 | Specify the settings that you want to update for all the records
                                       			 that you have defined in your query. You can choose multiple parameters to update. |

| Tip | To find all Intercom DNs that are registered in the database, click Find without entering any search text. |
|---|---|

| Step 1 | Choose Bulk Administration > Phones > Add/Update Intercom > Add Intercom Directory Numbers . |
|---|---|
| Step 2 | In the File Name drop-down list box, choose the CSV
                                       			 data file that you created for this specific bulk transaction. |
| Step 3 | In the Phone Template Name drop-down list, choose the BAT Phone template that you created for this type of bulk transaction. |
| Step 4 | Check the Override Configuration Settings check box to
                                       			 update the existing phone button template settings with the information that is
                                       			 contained in the file that you want to insert. Consider overriding the configuration settings as optional. |
| Step 5 | In the Job Information area, enter the Job description. The default job description for this transaction specifies Insert
                                          				Intercom DNs. |
| Step 6 | Choose a method to add Intercom DNs. Do one of the following: Click Run Immediately to add Intercom DNs
                                             				  immediately. Click Run Later to add Intercom DNs at a later
                                             				  time. |
| Step 7 | To create a job for adding Intercom DNs, click Submit . To schedule and / or activate this job, use the Job Configuration window. |

| Field | Description |
|---|---|
| Intercom Directory Number Information |
| Route Partition | Choose a route partition to which the directory number
                                          					 belongs. Note The directory number can appear in more than one partition. | Note | The directory number can appear in more than one partition. |
| Note | The directory number can appear in more than one partition. |
| Description | Enter a description that makes the device easy to recognize.
                                          					 The description can include up to 50 characters in any language, but it cannot
                                          					 include double-quotes ("), percentage sign ( % ),
                                          					 ampersand (&), or angle brackets (<>). |
| Alerting Name | This name represents the name that displays during an alert to
                                          					 a shared directory number. For non-shared directory numbers, during alerts, the
                                          					 system uses the name that is entered in the Display field. |
| ASCII Alerting Name | This field provides the same information as the Alerting Name field, but you must limit
                                          					 input to ASCII characters. Devices that do not support Unicode
                                          					 (internationalized) characters display the content of the Alerting Name ASCII field. |
| Intercom Directory Number Settings |
| Calling Search Space | Choose the calling search space to which this group of
                                          					 phones/ports should belong. A calling search space specifies the collection of route
                                          					 partitions that are searched to determine how a dialed number should be routed. |
| Presence Group | Used with the Presence feature, the phone that is running SIP
                                          					 or SCCP serves as a watcher because it requests status about the presence
                                          					 entity, for example, directory number, that is configured as a BLF speed dial
                                          					 button on the phone. If you want the phone to receive the status of the presence
                                          					 entity, choose a Presence Group that is allowed to view the status of the
                                          					 Presence Group that is applied to the directory number, as indicated in the Presence Group Configuration window. |

| Note | The directory number can appear in more than one partition. |
|---|---|