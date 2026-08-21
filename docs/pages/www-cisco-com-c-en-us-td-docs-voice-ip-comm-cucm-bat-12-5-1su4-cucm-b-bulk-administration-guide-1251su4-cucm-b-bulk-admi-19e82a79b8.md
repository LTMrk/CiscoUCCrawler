---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1su4-cucm-b-bulk-administration-guide-1251su4-cucm-b-bulk-admi-19e82a79b8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1SU4/cucm_b_bulk-administration-guide-1251su4/cucm_b_bulk-administration-guide-1251su2_chapter_0101111.html
retrieved_at: 2026-08-21T17:52:42.744658+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Chapter: Intercom DN Additions and Updates for UDPs

## Chapter: Intercom DN Additions and Updates for UDPs

# Intercom DN Additions and Updates for UDPs

This chapter provides information to use the
                        		Add / Update Intercom utility to add or update intercoms in bulk
                        		for user device profiles in Cisco Unified Communications Manager server.

The Intercom feature allows one user to call another user, and
                        		that call automatically gets answered with one-way media from caller to called
                        		party, regardless of whether the called party is busy or idle.

## Update Intercom DNs for User Device Profiles

Use BAT to update Intercom DNs for user device profiles.

Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > Add/Update Intercom > Update Intercom Directory Numbers .

From the first Find and List Intercom Directory Numbers To Update
                                          				where drop-down list box, choose one of the following criteria:

- Intercom Directory
                                             				  Number

- Route Partition

- Description

From the second Find and List Intercom Directory
                                          				Numbers To Update where drop-down list box, choose one of the
                                       			 following criteria:

- begins with

- contains

- ends with

- is exactly

- is empty

- is not empty

Specify the appropriate search text in the text field, if
                                       			 applicable, and click Find .

To find all Intercom DNs that are registered in the database,
                                                      				  click Find without entering any search text.

To further define your query, you can choose AND or OR to add multiple filters and repeat 2 and 3 .

A list of discovered Intercom DNs displays by

- Intercom DN Pattern

- Route Partition

- Description

Click Next . The next Update Intercom Directory Number window
                                       			 displays.

Specify the settings that you want to update for all the records
                                       			 that you have defined in your query. You can choose multiple parameters to
                                       			 update. See Update Intercom DN Field Descriptions for UDPs for descriptions of the parameters.

## Add Intercom DNs to User Device Profiles

You can use a CSV data file to add Intercom DNs to user
                              		  device profiles in a Cisco Unified Communications Manager server.

### Before you begin

- You must have a data file
                                 			 in comma separated value (CSV) format that contains the unique details for the
                                 			 UDPs or other IP telephony devices.

- Upload the data files by
                                 			 choosing the relevant target and function for the transaction.

Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > Add/Update Intercom > Add Intercom Directory Numbers .

In the File Name drop-down list box, choose the CSV
                                       			 data file that you created for this specific bulk transaction.

In the User Device Profile Template Name drop-down
                                       			 list box, choose the BAT UDP template that you created for this type of bulk
                                       			 transaction.

Check the Override Configuration Settings check box to
                                       			 update the existing UDP template settings with the information that is
                                       			 contained in the file that you want to insert.

In the Job Information area, enter the Job
                                       			 description.

The default job description for this transaction specifies Insert
                                          				Intercom DNs.

Choose when to add Intercom DNs. Do one of the following:

Click Run Immediately to add Intercom DNs
                                             				  immediately.

Click Run Later to add Intercom DNs at a later
                                             				  time.

To create a job for adding Intercom DNs, click Submit .

## Update Intercom DN Field Descriptions for UDPs

The following table provides the field descriptions for
                              		  updating line details in user device profiles.

Field

Description

Intercom Directory Number Information

Route Partition

Choose a route partition to which the directory number
                                          					 belongs.

The directory number can appear in more than one partition.

Description

Enter a description that makes the device easy to recognize.

Alerting Name

This name represents the name that displays during an alert to
                                          					 a shared directory number. For non-shared directory numbers, during alerts, the
                                          					 system uses the name that is entered in the Display field.

ASCII Alerting Name

This field provides the same information as the Alerting Name
                                          					 field, but you must limit input to ASCII characters. Devices that do not
                                          					 support Unicode (internationalized) characters display the content of the
                                          					 Alerting Name ASCII field.

Intercom Directory Number Settings

Calling Search Space

Choose the calling search space to which this group of
                                          					 UDPs/ports should belong.

A calling search space specifies the collection of route
                                          					 partitions that are searched to determine how a dialed number should be routed.

Presence Group

Used with the Presence feature, the SIP or SCCP device serves
                                          					 as a watcher because it requests status about the presence entity, for example,
                                          					 directory number, that is configured as a BLF speed dial button on the device.

If you want the device to receive the status of the presence
                                          					 entity, choose a Presence Group that is allowed to view the status of the
                                          					 Presence Group that is applied to the directory number, as indicated in the Presence Group Configuration window.

| Step 1 | Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > Add/Update Intercom > Update Intercom Directory Numbers . The Update Intercom Directory Number window displays |
|---|---|
| Step 2 | From the first Find and List Intercom Directory Numbers To Update
                                          				where drop-down list box, choose one of the following criteria: Intercom Directory
                                             				  Number Route Partition Description |
| Step 3 | From the second Find and List Intercom Directory
                                          				Numbers To Update where drop-down list box, choose one of the
                                       			 following criteria: begins with contains ends with is exactly is empty is not empty |
| Step 4 | Specify the appropriate search text in the text field, if
                                       			 applicable, and click Find . Tip To find all Intercom DNs that are registered in the database,
                                                      				  click Find without entering any search text. To further define your query, you can choose AND or OR to add multiple filters and repeat 2 and 3 . A list of discovered Intercom DNs displays by Intercom DN Pattern Route Partition Description | Tip | To find all Intercom DNs that are registered in the database,
                                                      				  click Find without entering any search text. |
| Tip | To find all Intercom DNs that are registered in the database,
                                                      				  click Find without entering any search text. |
| Step 5 | Click Next . The next Update Intercom Directory Number window
                                       			 displays. |
| Step 6 | Specify the settings that you want to update for all the records
                                       			 that you have defined in your query. You can choose multiple parameters to
                                       			 update. See Update Intercom DN Field Descriptions for UDPs for descriptions of the parameters. |

| Tip | To find all Intercom DNs that are registered in the database,
                                                      				  click Find without entering any search text. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > User Device
                                             				  Profiles > Add/Update Intercom > Add Intercom Directory Numbers . The Bulk UDP Intercom DN Insert window displays. |
|---|---|
| Step 2 | In the File Name drop-down list box, choose the CSV
                                       			 data file that you created for this specific bulk transaction. |
| Step 3 | In the User Device Profile Template Name drop-down
                                       			 list box, choose the BAT UDP template that you created for this type of bulk
                                       			 transaction. |
| Step 4 | Check the Override Configuration Settings check box to
                                       			 update the existing UDP template settings with the information that is
                                       			 contained in the file that you want to insert. Consider overriding the configuration settings as optional. |
| Step 5 | In the Job Information area, enter the Job
                                       			 description. The default job description for this transaction specifies Insert
                                          				Intercom DNs. |
| Step 6 | Choose when to add Intercom DNs. Do one of the following: Click Run Immediately to add Intercom DNs
                                             				  immediately. Click Run Later to add Intercom DNs at a later
                                             				  time. |
| Step 7 | To create a job for adding Intercom DNs, click Submit . Use the Job Configuration window to schedule
                                       			 and / or activate this job. |

| Field | Description |
|---|---|
| Intercom Directory Number Information |
| Route Partition | Choose a route partition to which the directory number
                                          					 belongs. Note The directory number can appear in more than one partition. | Note | The directory number can appear in more than one partition. |
| Note | The directory number can appear in more than one partition. |
| Description | Enter a description that makes the device easy to recognize. |
| Alerting Name | This name represents the name that displays during an alert to
                                          					 a shared directory number. For non-shared directory numbers, during alerts, the
                                          					 system uses the name that is entered in the Display field. |
| ASCII Alerting Name | This field provides the same information as the Alerting Name
                                          					 field, but you must limit input to ASCII characters. Devices that do not
                                          					 support Unicode (internationalized) characters display the content of the
                                          					 Alerting Name ASCII field. |
| Intercom Directory Number Settings |
| Calling Search Space | Choose the calling search space to which this group of
                                          					 UDPs/ports should belong. A calling search space specifies the collection of route
                                          					 partitions that are searched to determine how a dialed number should be routed. |
| Presence Group | Used with the Presence feature, the SIP or SCCP device serves
                                          					 as a watcher because it requests status about the presence entity, for example,
                                          					 directory number, that is configured as a BLF speed dial button on the device. If you want the device to receive the status of the presence
                                          					 entity, choose a Presence Group that is allowed to view the status of the
                                          					 Presence Group that is applied to the directory number, as indicated in the Presence Group Configuration window. |

| Note | The directory number can appear in more than one partition. |
|---|---|