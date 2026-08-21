---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-su6-cucm-b-bulk-administration-guide-1251su6-cucm-b-bulk-admin-76ffcb46d0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_SU6/cucm_b_bulk-administration-guide-1251su6/cucm_b_bulk-administration-guide-1251su2_chapter_0101101.html
retrieved_at: 2026-08-21T08:56:45.317851+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: February 15, 2022

Chapter: UDP Line Additions

## Chapter: UDP Line Additions

# UDP Line Additions

This chapter provides information to add lines to a group of
                        		existing user device profiles. When you use the BAT template to add new lines,
                        		you cannot change phone services or speed dials. Cisco Unified Communications Manager Bulk Administration (BAT) ignores those fields
                        		in the BAT template when you add lines to existing devices.

## Add Lines to Existing UDPs

You can to add lines to a group of existing user device
                              		  profiles using a CSV data file. Cisco Unified Communications Manager Bulk Administration (BAT) ignores changes to
                              		  phone services and speed dials when you add lines to existing devices.

### Before you begin

You must have a BAT template for this transaction.

You must have a CSV data file for this transaction.

Choose Bulk Administration > User Device Profiles > Add/Update
                                             				  Lines > Add Lines .

In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction.

If you are changing the phone settings for existing phones in the
                                       			 template, check the Update the existing phone button template check box. The user device profile information also gets updated when this
                                       			 check box is checked.

In the Template Name field, choose the User Device
                                       			 Profile template to use for this bulk transaction.

In the Job Information area, enter the Job description.

Choose an insert method. Do one of the following:

Click Run Immediately to insert the phone
                                             				  records immediately.

Click Run Later to insert the phone records at a
                                             				  later time.

Click Submit to create a job for inserting the phone
                                       			 records.

## Add Lines to Existing UDPs Using BAT Spreadsheet

You must have a BAT template for this transaction.

You must have a CSV data file for this transaction.

Use the BAT spreadsheet to create the CSV data file for
                              		  adding lines to existing UDPs. Cisco Unified Communications Manager Bulk Administration (BAT) ignores changes to
                              		  phone services and speed dial fields in the template when you add lines to
                              		  existing devices.

After you have finished editing the fields in the BAT spreadsheet, you
                              		  can export the content to a CSV formatted data file. A default filename is
                              		  assigned to the exported CSV formatted data file:

<tabname>-<timestamp>.txt

where <tabname> represents the type of input file that
                              		  you created, such as UDPs, and <timestamp> represents the precise date and time
                              		  that the file was created.

If you enter a comma in one of the fields, BAT.xlt encloses that
                                          			 field entry in double quotes when you export to BAT format.

If you enter a blank row in the spreadsheet, the system treats the
                                          			 empty row as the end of the file. The system does not convert data that is
                                          			 entered after a blank line to the BAT format.

To open the BAT Spreadsheet, locate and double-click the BAT.xlt
                                       			 file.

When prompted, click Enable Macros to use the spreadsheet
                                       			 capabilities.

To display the fields, click the Add Lines tab at the bottom of the
                                       			 spreadsheet.

Select the appropriate radio button from the following options:

Phones

UDP

Enter data for an individual device profile on each line in the
                                       			 spreadsheet.

To transfer the data from the BAT Excel spreadsheet into a CSV
                                       			 formatted data file, click Export to BAT Format .

For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert Phones window in BAT.

### What to do next

Upload the CSV file to Cisco Unified Communications Manager Server first node.

## UDP Line Field Descriptions in BAT Spreadsheet

The following table provides the field descriptions when you
                              		  add lines to UDPs using the BAT spreadsheet.

Field

Description

MAC Address/Device Name

Enter the MAC address for phones, VGC virtual phones, and VGC
                                          					 phones. Enter a unique identifier for CTI ports and H.323 clients. Enter the
                                          					 device name for UDPs

Line Index

Enter a number between 1 and 34 for the line index of a phone.

Directory Number

Enter a directory number, up to 24 numerals and special
                                          					 characters, for this line.

Display

Enter the text that you want to display on the called party's
                                          					 phone display, such as the user name (John Smith) or phone location (Conference
                                          					 Room 1).

If this filed is left blank the system uses the value that
                                                      						is entered in the Directory Number field.

The default language specifies English.

Line Text Label

Enter text that identifies this directory number for a
                                          					 line/phone combination.

The default language specifies English

Forward Busy External

Enter the directory number or directory URI to which a call that is coming from
                                          					 an external number is forwarded when the line is in use.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward No Answer External

Enter the directory number or directory URI to which a call that is coming from
                                          					 an external number is forwarded when the phone is not answered.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward No Coverage External

Enter the directory number or directory URI to which a call that is coming from
                                          					 an external number is forwarded when the phone does not have coverage.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward Busy Internal

Enter the directory number or directory URI to which a call that is coming from
                                          					 an internal number is forwarded when the line is in use.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward No Answer Internal

Enter the directory number or directory URI to which a call that is coming from
                                          					 an internal number is forwarded when the phone is not answered.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Forward No Coverage Internal

Enter the directory number or directory URI to which a call that is coming from
                                          					 an internal number is forwarded when the phone does not have coverage.

This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number.

Party Entrance Tone

Enter one of the following Party Entrance Tone options:

- Default—Use the
                                             						value that you configured in the Party Entrance Tone service parameter.

- On—A tone plays on
                                             						the phone when a basic call changes to a multi-party call; that is, a barge
                                             						call, cBarge call, ad hoc conference, meet-me conference, or a joined call. In
                                             						addition, a different tone plays when a party leaves the multi-party call. If
                                             						the controlling device, that is, the originator of the multi-party call has a
                                             						built-in bridge, the tone gets played to all parties if you choose On for the
                                             						controlling device. When the controlling device, for example, the conference
                                             						controller, is no longer present on the call or if the controlling device
                                             						cannot play the tone, Cisco Unified Communications Manager does not play the
                                             						tone even if you choose On.

- Off—A tone does
                                             						not play on the phone when a basic call changes to a multi-party call.

Park Monitor Forward No Retrieve Ext Destination

When the parkee is an external party, then the call will be
                                          					 forwarded to the specified destination in the parker's Park Monitoring Forward
                                          					 No Retrieve Destination External parameter. If the Forward No Retrieve
                                          					 Destination External field value is empty, the parkee will be redirected to the
                                          					 parker's line.

Park Monitor Forward No Retrieve Int Destination

When the parkee is an internal party, then the call will be
                                          					 forwarded to the specified destination in the parker's Park Monitoring Forward
                                          					 No Retrieve Destination Internal parameter. If the Forward No Retrieve
                                          					 Destination Internal is empty, the parkee will be redirected to the parker's
                                          					 line.

Park Monitor Forward No Retrieve Int Voice Mail

This setting uses settings in the Voice Mail Profile
                                          					 Configuration window.

When this setting is used, Cisco Unified Communications Manager ignores the settings in the Destination box
                                          					 and Calling Search Space.

Park Monitor Forward No Retrieve Ext Voice Mail

This setting uses the settings in the Voice Mail Profile
                                          					 Configuration window.

When this setting is used, Cisco Unified Communications Manager ignores the settings in the Destination box
                                          					 and Calling Search Space.

Park Monitor Forward No Retrieve Ext CSS

Choose the calling search space to apply to the directory
                                          					 number.

Park Monitor Forward No Retrieve Int CSS

Choose the calling search space to apply to the directory
                                          					 number.

Park Monitor Reversion Timer

This parameter determines the number of seconds that Cisco Unified Communications Manager waits before prompting the user to retrieve a
                                          					 call that the user parked. This timer starts when the user presses the Park
                                          					 softkey on the phone, and a reminder is issued when the timer expires.

Default: 60 seconds

If you configure a non-zero value, this value overrides the
                                          					 value of this parameter set in the Service Parameters window. However, if you
                                          					 configure a value of 0 here, then the value in the Service Parameters window
                                          					 will be used.

Log Missed Calls

This field allows you to turn this feature on or off. Enter
                                          					 'T' to enable Cisco Unified Communications Manager to log missed calls in the call history for
                                          					 that directory number on the phone. Enter 'F' to disable this feature.

Call Pickup Group

Enter a Pickup Group Name to specify the call pickup group,
                                          					 which can answer incoming calls to this line by dialing the appropriate pickup
                                          					 group number.

URI (1-5) on Directory Number

Enter a directory URI to associate with the directory number for this phone. Follow the username@host format. Enter a username
                                          of up to 47 alphanumeric characters. For the host address, enter an IPv4 address or fully qualified domain name.

Within Cisco Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when
                                                      you use Bulk Administration to import a csv file that contains directory URIs with embedded double quotes and commas, you
                                                      must use enclose the entire directory URI in double quotes and escape the embedded double quotes with a double quote. For
                                                      example, the Jared, "Jerry",Smith@test.com directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the csv file.

URI (1-5) Route Partition on Directory Number

Enter the partition on which the directory URI belongs. If you do not want to restrict access to the directory URI, leave
                                          the field blank.

URI (1-5) Is Primary on Directory Number

Enter a ' t ' (True) to indicate that this directory URI is the primary directory URI for this extension. Otherwise, enter an ' f' (False) to indicate that this is not the primary directory URI for this extension.

You can associate up to five directory URIs to a single directory number, but you must select one primary directory URI

## Topics Related to UDP Line Additions

| Step 1 | Choose Bulk Administration > User Device Profiles > Add/Update
                                             				  Lines > Add Lines . The UDP Add Lines Configuration window displays. |
|---|---|
| Step 2 | In the File Name field, choose the CSV data file that
                                       			 you created for this bulk transaction. |
| Step 3 | If you are changing the phone settings for existing phones in the
                                       			 template, check the Update the existing phone button template check box. The user device profile information also gets updated when this
                                       			 check box is checked. |
| Step 4 | In the Template Name field, choose the User Device
                                       			 Profile template to use for this bulk transaction. |
| Step 5 | In the Job Information area, enter the Job description. |
| Step 6 | Choose an insert method. Do one of the following: Click Run Immediately to insert the phone
                                             				  records immediately. Click Run Later to insert the phone records at a
                                             				  later time. |
| Step 7 | Click Submit to create a job for inserting the phone
                                       			 records. Use the Job Scheduler option in the Bulk Administration main menu
                                       			 to schedule and/or activate this job. |

| Note | If you enter a comma in one of the fields, BAT.xlt encloses that
                                          			 field entry in double quotes when you export to BAT format. If you enter a blank row in the spreadsheet, the system treats the
                                          			 empty row as the end of the file. The system does not convert data that is
                                          			 entered after a blank line to the BAT format. |
|---|---|

| Step 1 | To open the BAT Spreadsheet, locate and double-click the BAT.xlt
                                       			 file. |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet
                                       			 capabilities. |
| Step 3 | To display the fields, click the Add Lines tab at the bottom of the
                                       			 spreadsheet. |
| Step 4 | Select the appropriate radio button from the following options: Phones UDP |
| Step 5 | Enter data for an individual device profile on each line in the
                                       			 spreadsheet. Complete all mandatory fields and any relevant optional fields.
                                       			 Each column heading specifies the length of the field and whether it is
                                       			 required or optional. See Table 1 for field descriptions. |
| Step 6 | To transfer the data from the BAT Excel spreadsheet into a CSV
                                       			 formatted data file, click Export to BAT Format . Tip For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert Phones window in BAT. The system saves the file using the default name <tabname>-<timestamp>.txt to C:\XLSDataFiles\ or you can use Browse to save
                                       			 your file in another existing folder on your local workstation. | Tip | For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert Phones window in BAT. |
| Tip | For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert Phones window in BAT. |

| Tip | For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert Phones window in BAT. |
|---|---|

| Field | Description |
|---|---|
| MAC Address/Device Name | Enter the MAC address for phones, VGC virtual phones, and VGC
                                          					 phones. Enter a unique identifier for CTI ports and H.323 clients. Enter the
                                          					 device name for UDPs |
| Line Index | Enter a number between 1 and 34 for the line index of a phone. |
| Directory Number | Enter a directory number, up to 24 numerals and special
                                          					 characters, for this line. |
| Display | Enter the text that you want to display on the called party's
                                          					 phone display, such as the user name (John Smith) or phone location (Conference
                                          					 Room 1). Note If this filed is left blank the system uses the value that
                                                      						is entered in the Directory Number field. Note The default language specifies English. | Note | If this filed is left blank the system uses the value that
                                                      						is entered in the Directory Number field. | Note | The default language specifies English. |
| Note | If this filed is left blank the system uses the value that
                                                      						is entered in the Directory Number field. |
| Note | The default language specifies English. |
| Line Text Label | Enter text that identifies this directory number for a
                                          					 line/phone combination. Note The default language specifies English | Note | The default language specifies English |
| Note | The default language specifies English |
| Forward Busy External | Enter the directory number or directory URI to which a call that is coming from
                                          					 an external number is forwarded when the line is in use. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward No Answer External | Enter the directory number or directory URI to which a call that is coming from
                                          					 an external number is forwarded when the phone is not answered. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward No Coverage External | Enter the directory number or directory URI to which a call that is coming from
                                          					 an external number is forwarded when the phone does not have coverage. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward Busy Internal | Enter the directory number or directory URI to which a call that is coming from
                                          					 an internal number is forwarded when the line is in use. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward No Answer Internal | Enter the directory number or directory URI to which a call that is coming from
                                          					 an internal number is forwarded when the phone is not answered. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Forward No Coverage Internal | Enter the directory number or directory URI to which a call that is coming from
                                          					 an internal number is forwarded when the phone does not have coverage. Note This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. | Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
| Party Entrance Tone | Enter one of the following Party Entrance Tone options: Default—Use the
                                             						value that you configured in the Party Entrance Tone service parameter. On—A tone plays on
                                             						the phone when a basic call changes to a multi-party call; that is, a barge
                                             						call, cBarge call, ad hoc conference, meet-me conference, or a joined call. In
                                             						addition, a different tone plays when a party leaves the multi-party call. If
                                             						the controlling device, that is, the originator of the multi-party call has a
                                             						built-in bridge, the tone gets played to all parties if you choose On for the
                                             						controlling device. When the controlling device, for example, the conference
                                             						controller, is no longer present on the call or if the controlling device
                                             						cannot play the tone, Cisco Unified Communications Manager does not play the
                                             						tone even if you choose On. Off—A tone does
                                             						not play on the phone when a basic call changes to a multi-party call. |
| Park Monitor Forward No Retrieve Ext Destination | When the parkee is an external party, then the call will be
                                          					 forwarded to the specified destination in the parker's Park Monitoring Forward
                                          					 No Retrieve Destination External parameter. If the Forward No Retrieve
                                          					 Destination External field value is empty, the parkee will be redirected to the
                                          					 parker's line. |
| Park Monitor Forward No Retrieve Int Destination | When the parkee is an internal party, then the call will be
                                          					 forwarded to the specified destination in the parker's Park Monitoring Forward
                                          					 No Retrieve Destination Internal parameter. If the Forward No Retrieve
                                          					 Destination Internal is empty, the parkee will be redirected to the parker's
                                          					 line. |
| Park Monitor Forward No Retrieve Int Voice Mail | This setting uses settings in the Voice Mail Profile
                                          					 Configuration window. When this setting is used, Cisco Unified Communications Manager ignores the settings in the Destination box
                                          					 and Calling Search Space. |
| Park Monitor Forward No Retrieve Ext Voice Mail | This setting uses the settings in the Voice Mail Profile
                                          					 Configuration window. When this setting is used, Cisco Unified Communications Manager ignores the settings in the Destination box
                                          					 and Calling Search Space. |
| Park Monitor Forward No Retrieve Ext CSS | Choose the calling search space to apply to the directory
                                          					 number. |
| Park Monitor Forward No Retrieve Int CSS | Choose the calling search space to apply to the directory
                                          					 number. |
| Park Monitor Reversion Timer | This parameter determines the number of seconds that Cisco Unified Communications Manager waits before prompting the user to retrieve a
                                          					 call that the user parked. This timer starts when the user presses the Park
                                          					 softkey on the phone, and a reminder is issued when the timer expires. Default: 60 seconds If you configure a non-zero value, this value overrides the
                                          					 value of this parameter set in the Service Parameters window. However, if you
                                          					 configure a value of 0 here, then the value in the Service Parameters window
                                          					 will be used. |
| Log Missed Calls | This field allows you to turn this feature on or off. Enter
                                          					 'T' to enable Cisco Unified Communications Manager to log missed calls in the call history for
                                          					 that directory number on the phone. Enter 'F' to disable this feature. |
| Call Pickup Group | Enter a Pickup Group Name to specify the call pickup group,
                                          					 which can answer incoming calls to this line by dialing the appropriate pickup
                                          					 group number. |
| URI (1-5) on Directory Number | Enter a directory URI to associate with the directory number for this phone. Follow the username@host format. Enter a username
                                          of up to 47 alphanumeric characters. For the host address, enter an IPv4 address or fully qualified domain name. Note Within Cisco Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when
                                                      you use Bulk Administration to import a csv file that contains directory URIs with embedded double quotes and commas, you
                                                      must use enclose the entire directory URI in double quotes and escape the embedded double quotes with a double quote. For
                                                      example, the Jared, "Jerry",Smith@test.com directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the csv file. | Note | Within Cisco Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when
                                                      you use Bulk Administration to import a csv file that contains directory URIs with embedded double quotes and commas, you
                                                      must use enclose the entire directory URI in double quotes and escape the embedded double quotes with a double quote. For
                                                      example, the Jared, "Jerry",Smith@test.com directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the csv file. |
| Note | Within Cisco Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when
                                                      you use Bulk Administration to import a csv file that contains directory URIs with embedded double quotes and commas, you
                                                      must use enclose the entire directory URI in double quotes and escape the embedded double quotes with a double quote. For
                                                      example, the Jared, "Jerry",Smith@test.com directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the csv file. |
| URI (1-5) Route Partition on Directory Number | Enter the partition on which the directory URI belongs. If you do not want to restrict access to the directory URI, leave
                                          the field blank. |
| URI (1-5) Is Primary on Directory Number | Enter a ' t ' (True) to indicate that this directory URI is the primary directory URI for this extension. Otherwise, enter an ' f' (False) to indicate that this is not the primary directory URI for this extension. Note You can associate up to five directory URIs to a single directory number, but you must select one primary directory URI | Note | You can associate up to five directory URIs to a single directory number, but you must select one primary directory URI |
| Note | You can associate up to five directory URIs to a single directory number, but you must select one primary directory URI |

| Note | If this filed is left blank the system uses the value that
                                                      						is entered in the Directory Number field. |
|---|---|

| Note | The default language specifies English. |
|---|---|

| Note | The default language specifies English |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | This setting applies to any dialable phone number, including
                                                      						an outside destination unless restricted, and to all devices that are using
                                                      						this directory number. |
|---|---|

| Note | Within Cisco Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when
                                                      you use Bulk Administration to import a csv file that contains directory URIs with embedded double quotes and commas, you
                                                      must use enclose the entire directory URI in double quotes and escape the embedded double quotes with a double quote. For
                                                      example, the Jared, "Jerry",Smith@test.com directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the csv file. |
|---|---|

| Note | You can associate up to five directory URIs to a single directory number, but you must select one primary directory URI |
|---|---|