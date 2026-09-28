---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-14su1-cucm-b-bulk-administration-guide-14su1-cucm-b-bulk-administra-2ceda2a3b2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/14SU1/cucm_b_bulk-administration-guide-14SU1/cucm_b_bulk-administration-guide-1251su2_chapter_01001.html
retrieved_at: 2026-08-21T09:08:27.500058+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: October 27, 2021

Chapter: Phone Exports

## Chapter: Phone Exports

# Phone Exports

This chapter provides information about using the export utility
                        		to merge records from multiple Cisco Unified Communications Manager servers onto one Cisco Unified Communications Manager server.

## Phone Record Exports

phone records

user records

user device profile records

Optionally, you can edit the CSV file with a text editor. The record format must follow the format that is specified for that
                              file format. For example, records for phones need to follow the phone file format.

Caution

Use extreme care when editing the CSV file. Phones might not work if you insert records that are in the wrong format.

You can choose between two file format options when you export phone records:

Specific Details—For phones that have similar configurations

All Details—For phones that have different line configurations, such as multiple partitions or calling search spaces

When you are ready to insert the exported records, the order in which the records are inserted is important. You must insert
                              user records first to ensure that devices properly associate with existing users.

Upload the CSV file to Unified Communications Manager server.

Insert User Records.

Insert Phone Records.

Insert User Device Profile Records.

Check the log files for errors.

## Exported Phone Record Fields

### Default Phone File Format Exported Fields

The export Default Phone file format option is useful when
                              		  you want to export phone file formats for phones that have similar
                              		  configurations. Default phone records are exported using a defined query.

The following table lists the fields that are exported when
                              		  you choose the Default Phone file format.

Field types

Exported fields

Device Fields

MAC Address, Description, Location

Line Fields

Directory Number, Display, Line Text Label, Forward Busy
                                          					 External, Forward Busy Internal, Forward No Answer Internal, Forward No Answer
                                          					 External, Forward No Coverage Internal, Forward No Coverage External, Call
                                          					 Pickup Group

### All Phone Details File Format Exported Fields

When you export phone records using All Phone Details option,
                              		  you export phone records for a particular model of phone along with all the
                              		  device field information, different line attributes, and services that are
                              		  associated with the phone, or you can export all phone models in a single file.
                              		  To export all phone types to a single file, you can choose All Phone Types from
                              		  the Select the Device Type drop-down list box. You cannot use the query to
                              		  limit the number of records.

The following table lists the fields that are exported when
                              		  you choose the All Phone Details file format.

The device name, not the MAC Address, gets saved when you choose to
                                          			 export by using the All Phone Details file format.

Field types

Exported fields

Device Fields

Device Name, Description, Owner User ID, Device Pool, CSS, AAR
                                          					 CSS, Media Resource Group List, User Hold Audio Source, Network Hold Audio
                                          					 Source, Location, User Locale, Network Locale, Phone Button Template, Expansion
                                          					 Module type I, Expansion Module type II, Softkey Template, Phone Load Name,
                                          					 Module 1 Load Name, Module 2 Load Name, Login user ID, Built in Bridge, MLPP
                                          					 Indication, MLPP Preemption, MLPP Domain, Retry Video call as Audio, Privacy,
                                          					 Security Mode, Ignore Presentation Indicators, Single Packet Capture mode,
                                          					 Packet Capture Duration, Certificate Operation, Authentication Mode,
                                          					 Authentication String, Key Size (bits), Operation Completes By

Model Specific Device Fields

Information, Directory, Messages, Services, Authentication
                                          					 Server, Proxy Server, Idle, Idle Timer, Enable Extension Mobility, Logout
                                          					 Profile, Login User ID, Login Time, Logout Time, Product Specific XML

Line Fields

Directory Number, Partition, Voice Mail Profile, Line CSS, AAR
                                          					 Group, Line User Hold Audio Source, Line Network Hold Audio Source, Auto
                                          					 Answer, Forward All to Voice Mail, Forward All Destination, Forward All CSS,
                                          					 Forward Busy External to Voice Mail, Forward Busy External Destination, Forward
                                          					 Busy External CSS, Forward No Answer External to Voice Mail, Forward No Answer
                                          					 External Destination, Forward No Answer External CSS, Forward On Failure to
                                          					 Voice Mail, Forward On Failure Destination, Forward on Failure CSS, Call pickup
                                          					 group, Forward Busy Internal to Voice Mail, Forward Busy Internal Destination,
                                          					 Forward Busy Internal CSS, Forward No Answer Internal to Voice Mail, Forward No
                                          					 Answer Internal Destination, Forward No Answer Internal CSS, Forward No Call
                                          					 Coverage External to Voice Mail, Forward No Call Coverage External Destination,
                                          					 Forward No Call Coverage External CSS, Forward No Call Coverage Internal to
                                          					 Voice Mail, Forward No Call Coverage Internal Destination, Forward No Call
                                          					 Coverage Internal CSS, Display, External Phone Number Mask, Message Waiting
                                          					 Lamp Policy, Ring Setting When Idle, Line Text Label, Ring Setting When Active,
                                          					 No Answer Ring Duration, MLPP Target Destination, MLPP Calling Search Space,
                                          					 MLPP No Answer Ring Duration, Max Num Calls, Busy Trigger, Call Info Display
                                          					 Mask, Alerting Name

User Fields

User ID

Speed Dials

Speed Dial Number, Speed Dial Label

Services

Service Name, Subscribed Service Name, Parameter Name,
                                          					 Parameter Value

## Export Phone Records

You can export phone records from the Cisco Unified Communications Manager database. After the phone records are
                              		  exported, you can search and download the exported file using the Upload/Download Files option in the Bulk Administration menu.

Step 1

Choose one of the following options:

- Bulk
                                                   						Administration > Phones > Export
                                                   						Phones > Specific Details . The
                                             				  Export Phones Query window displays.

- Bulk
                                                   						Administration > Phones > Export
                                                   						Phones > All Details . The Export
                                             				  Phone Configuration window displays.

Step 2

For All Details option, choose the type of
                                       			 device or specific model in the Device Type drop-down list box. Skip to Step 4 .

Step 3

For Specific Details , you can customize the
                                       			 export file by choosing which set of phones to export, but you cannot configure
                                       			 the phone details.

From the first Find Phone where , drop-down list box,
                                             				  choose from the following options:

- Device Name

- Description

- Directory Number

- Calling Search Space

- Device Pool

- Call Pickup Group

- LSC Status

- Authentication String

- Security Profile

Last Registered

Last Active

In the second drop-down list box, choose from the following
                                             				  options:

- begins with

- contains

- is exactly

- ends with

- is empty

- is not empty

In the search field / list box, either choose
                                             				  or enter the value that you want to locate, such as a device name.

You can click the Search Within Results check box and choose AND or OR to add multiple filters and repeat 3.a through 3.c to further define your query.

Click Find .

Click Next .

From the File Format drop-down list
                                             				  box, choose a Phone file format.

Step 4

Enter the export file name in the File Name text box.

Step 5

In the Job Information area, enter the Job description.

Step 6

Choose an export method. Do one of the following:

Click Run Immediately to export phone records
                                             				  immediately.

Click Run Later to export at a later
                                             				  time.

Step 7

To create a job for exporting phone records, click Submit .

## Multiple User Phones to Export or Import

The exported file name gets suffixed with the timestamp. If
                              		  a recurring job is scheduled for export phones, the information gets exported
                              		  with same filename but different timestamps.

When you import the exported file that has phones with
                              		  multiple users, all users get exported in the same record.

## Topics Related to Phone Exports

Export Phone Records

Export User Records

Export User Device Profile Records

| Caution | Use extreme care when editing the CSV file. Phones might not work if you insert records that are in the wrong format. |
|---|---|

| Field types | Exported fields |
|---|---|
| Device Fields | MAC Address, Description, Location |
| Line Fields | Directory Number, Display, Line Text Label, Forward Busy
                                          					 External, Forward Busy Internal, Forward No Answer Internal, Forward No Answer
                                          					 External, Forward No Coverage Internal, Forward No Coverage External, Call
                                          					 Pickup Group |

| Note | The device name, not the MAC Address, gets saved when you choose to
                                          			 export by using the All Phone Details file format. |
|---|---|

| Field types | Exported fields |
|---|---|
| Device Fields | Device Name, Description, Owner User ID, Device Pool, CSS, AAR
                                          					 CSS, Media Resource Group List, User Hold Audio Source, Network Hold Audio
                                          					 Source, Location, User Locale, Network Locale, Phone Button Template, Expansion
                                          					 Module type I, Expansion Module type II, Softkey Template, Phone Load Name,
                                          					 Module 1 Load Name, Module 2 Load Name, Login user ID, Built in Bridge, MLPP
                                          					 Indication, MLPP Preemption, MLPP Domain, Retry Video call as Audio, Privacy,
                                          					 Security Mode, Ignore Presentation Indicators, Single Packet Capture mode,
                                          					 Packet Capture Duration, Certificate Operation, Authentication Mode,
                                          					 Authentication String, Key Size (bits), Operation Completes By |
| Model Specific Device Fields | Information, Directory, Messages, Services, Authentication
                                          					 Server, Proxy Server, Idle, Idle Timer, Enable Extension Mobility, Logout
                                          					 Profile, Login User ID, Login Time, Logout Time, Product Specific XML |
| Line Fields | Directory Number, Partition, Voice Mail Profile, Line CSS, AAR
                                          					 Group, Line User Hold Audio Source, Line Network Hold Audio Source, Auto
                                          					 Answer, Forward All to Voice Mail, Forward All Destination, Forward All CSS,
                                          					 Forward Busy External to Voice Mail, Forward Busy External Destination, Forward
                                          					 Busy External CSS, Forward No Answer External to Voice Mail, Forward No Answer
                                          					 External Destination, Forward No Answer External CSS, Forward On Failure to
                                          					 Voice Mail, Forward On Failure Destination, Forward on Failure CSS, Call pickup
                                          					 group, Forward Busy Internal to Voice Mail, Forward Busy Internal Destination,
                                          					 Forward Busy Internal CSS, Forward No Answer Internal to Voice Mail, Forward No
                                          					 Answer Internal Destination, Forward No Answer Internal CSS, Forward No Call
                                          					 Coverage External to Voice Mail, Forward No Call Coverage External Destination,
                                          					 Forward No Call Coverage External CSS, Forward No Call Coverage Internal to
                                          					 Voice Mail, Forward No Call Coverage Internal Destination, Forward No Call
                                          					 Coverage Internal CSS, Display, External Phone Number Mask, Message Waiting
                                          					 Lamp Policy, Ring Setting When Idle, Line Text Label, Ring Setting When Active,
                                          					 No Answer Ring Duration, MLPP Target Destination, MLPP Calling Search Space,
                                          					 MLPP No Answer Ring Duration, Max Num Calls, Busy Trigger, Call Info Display
                                          					 Mask, Alerting Name |
| User Fields | User ID |
| Speed Dials | Speed Dial Number, Speed Dial Label |
| Services | Service Name, Subscribed Service Name, Parameter Name,
                                          					 Parameter Value |

| Step 1 | Choose one of the following options: Bulk
                                                   						Administration > Phones > Export
                                                   						Phones > Specific Details . The
                                             				  Export Phones Query window displays. Bulk
                                                   						Administration > Phones > Export
                                                   						Phones > All Details . The Export
                                             				  Phone Configuration window displays. |
|---|---|
| Step 2 | For All Details option, choose the type of
                                       			 device or specific model in the Device Type drop-down list box. Skip to Step 4 . See Table 1 for the list of exported fields in this format. |
| Step 3 | For Specific Details , you can customize the
                                       			 export file by choosing which set of phones to export, but you cannot configure
                                       			 the phone details. From the first Find Phone where , drop-down list box,
                                             				  choose from the following options: Device Name Description Directory Number Calling Search Space Device Pool Call Pickup Group LSC Status Authentication String Security Profile Last Registered Last Active In the second drop-down list box, choose from the following
                                             				  options: begins with contains is exactly ends with is empty is not empty In the search field / list box, either choose
                                             				  or enter the value that you want to locate, such as a device name. You can click the Search Within Results check box and choose AND or OR to add multiple filters and repeat 3.a through 3.c to further define your query. Click Find . The search results display. Click Next . The Export Phones Configuration window displays. From the File Format drop-down list
                                             				  box, choose a Phone file format. |
| Step 4 | Enter the export file name in the File Name text box. |
| Step 5 | In the Job Information area, enter the Job description. |
| Step 6 | Choose an export method. Do one of the following: Click Run Immediately to export phone records
                                             				  immediately. Click Run Later to export at a later
                                             				  time. |
| Step 7 | To create a job for exporting phone records, click Submit . To schedule and / or activate this job, use the Job Scheduler option in the Bulk Administration main menu. |