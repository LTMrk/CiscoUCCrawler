---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-15-cucm-b-bulk-administration-guide-15-cucm-b-bulk-administration-g-53a65c5bce
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/15/cucm_b_bulk-administration-guide-15/cucm_b_bulk-administration-guide-1251su2_chapter_0101011.html
retrieved_at: 2026-08-21T09:19:06.749914+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: October 1, 2024

Chapter: User Device Profile Exports

## Chapter: User Device Profile Exports

# User Device Profile Exports

This chapter provides information to export user device profile
                        		records. You can choose between two file format names when you are exporting
                        		user device profile records:

All User Device Profile Details: To export all the line attributes,
                              			 services and User IDs that are associated with the user device profile.

Specific User Device Profile Details: To export a limited set of
                              			 details that are associated with the user device profile

## All User Device Profile Details Format

For phones that have different line configurations, such as
                              		  multiple partitions or calling search spaces, use the All User Device Profile
                              		  Details format.

The following table lists the fields that are exported when
                              		  you choose the All User Device Profile Details file format.

Field Types

Exported Fields

Device Fields

User Device Profile Name, Description, Device Pool, Calling
                                          					 Search Space, AAR Calling Search Space, Media Resource Group List, User Hold
                                          					 Audio Service, Network Hold Audio Source, Login User ID, User Locale, Network
                                          					 Locale, Phone Button Template, Expansion Module Type I, Expansion Module Type
                                          					 II, Softkey Template, Phone Load Name, Module 1 Load Name, Module 2 Load Name,
                                          					 MLPP Indication, MLPP Preemption, MLPP Domain

Model Specific Device Fields

Information, Directory, Messages, Services, Authentication
                                          					 Server, Proxy Server, Idle, Idle Timer, Enable Extension Mobility, Logout
                                          					 Profile, Login User ID, Login Time, Logout Time

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

## Specific User Device Profile Format

To export a limited set of details that are associated with
                              		  the user device profile, use the Default User Device Profile format. You can
                              		  choose specific query options to customize the export file.

The following table lists the fields that can be exported
                              		  when you choose the Default User Device Profile format.

Field Types

Exported Fields

Device Fields

MAC Address, Description, Login User ID

Line Fields

Directory Number,Display,Line Text Label,Forward Busy
                                          					 External,Forward Busy Internal,Forward No Answer External,Forward No Answer
                                          					 Internal,Forward No Coverage External,Forward No Coverage Internal,Call pickup
                                          					 group

## Export User Device Profile Records

You can export user device profiles from Cisco Unified Communications Manager

Step 1

Choose one of the following options:

Choose Bulk
                                                   						Administration > User Device
                                                   						Profiles > Export User Device
                                                   						Profiles > Specific Details .

Choose Bulk
                                                   						Administration > User Device
                                                   						Profiles > Export User Device
                                                   						Profiles > All Details .

Step 2

For All Details option, choose the type of device
                                       			 or specific model from the Device Type drop-down list box. Skip to Step 4 .

Step 3

For Specific Details option, you can customize the
                                       			 export file and set any of the following detail options:

Choose Device Type and Device Protocol from the drop-down list
                                             				  boxes.

In the first Find a User Device Profile drop-down list
                                             				  box, choose from the following options:

Profile Name

Profile Description

In the second drop-down list box, choose from the following
                                             				  options:

begins with

contains

is exactly

ends with

is empty

is not empty

In the search field box, enter the value that you want to
                                             				  locate, such as a specific profile name or profile description.

You can click the Search Within Results check box and choose AND or OR to add multiple filters and repeat 3.b through 3.d to further define your query.

Click Find . The search results display.

Click Next .

Choose file format from the File Format drop-down list box.

Step 4

In the File Name field, enter the file name that you
                                       			 want to use.

Step 5

In the Job Information area, enter the Job description.

Step 6

Choose an export method. Do one of the following:

Click Run Immediately to export user device
                                             				  profiles immediately.

Click Run Later to export user device profiles
                                             				  at a later time.

Step 7

Click Submit to create a job for exporting user
                                       			 device profiles.

| Field Types | Exported Fields |
|---|---|
| Device Fields | User Device Profile Name, Description, Device Pool, Calling
                                          					 Search Space, AAR Calling Search Space, Media Resource Group List, User Hold
                                          					 Audio Service, Network Hold Audio Source, Login User ID, User Locale, Network
                                          					 Locale, Phone Button Template, Expansion Module Type I, Expansion Module Type
                                          					 II, Softkey Template, Phone Load Name, Module 1 Load Name, Module 2 Load Name,
                                          					 MLPP Indication, MLPP Preemption, MLPP Domain |
| Model Specific Device Fields | Information, Directory, Messages, Services, Authentication
                                          					 Server, Proxy Server, Idle, Idle Timer, Enable Extension Mobility, Logout
                                          					 Profile, Login User ID, Login Time, Logout Time |
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

| Field Types | Exported Fields |
|---|---|
| Device Fields | MAC Address, Description, Login User ID |
| Line Fields | Directory Number,Display,Line Text Label,Forward Busy
                                          					 External,Forward Busy Internal,Forward No Answer External,Forward No Answer
                                          					 Internal,Forward No Coverage External,Forward No Coverage Internal,Call pickup
                                          					 group |

| Step 1 | Choose one of the following options: Choose Bulk
                                                   						Administration > User Device
                                                   						Profiles > Export User Device
                                                   						Profiles > Specific Details . The Find and List User Device Profiles To Export window displays. Choose Bulk
                                                   						Administration > User Device
                                                   						Profiles > Export User Device
                                                   						Profiles > All Details . The Export User Device Profiles Configuration window displays. |
|---|---|
| Step 2 | For All Details option, choose the type of device
                                       			 or specific model from the Device Type drop-down list box. Skip to Step 4 . |
| Step 3 | For Specific Details option, you can customize the
                                       			 export file and set any of the following detail options: Choose Device Type and Device Protocol from the drop-down list
                                             				  boxes. In the first Find a User Device Profile drop-down list
                                             				  box, choose from the following options: Profile Name Profile Description In the second drop-down list box, choose from the following
                                             				  options: begins with contains is exactly ends with is empty is not empty In the search field box, enter the value that you want to
                                             				  locate, such as a specific profile name or profile description. You can click the Search Within Results check box and choose AND or OR to add multiple filters and repeat 3.b through 3.d to further define your query. Click Find . The search results display. Click Next . Choose file format from the File Format drop-down list box. |
| Step 4 | In the File Name field, enter the file name that you
                                       			 want to use. |
| Step 5 | In the Job Information area, enter the Job description. |
| Step 6 | Choose an export method. Do one of the following: Click Run Immediately to export user device
                                             				  profiles immediately. Click Run Later to export user device profiles
                                             				  at a later time. |
| Step 7 | Click Submit to create a job for exporting user
                                       			 device profiles. Use the Job Scheduler option in the Bulk Administration main menu to schedule and/or
                                       			 activate this job. |