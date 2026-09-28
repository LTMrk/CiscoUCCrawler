---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-15-systemconfig-cucm-b-system-configuration-guide-15-cucm-b-syste-82823e2725
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/systemConfig/cucm_b_system-configuration-guide-15/cucm_b_system-configuration-guide-14_chapter_011100.html
retrieved_at: 2026-08-16T16:12:06.694952+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# System Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: August 7, 2026

Chapter: Provisioning Users and Devices Using Bulk Administration Tool

## Chapter: Provisioning Users and Devices Using Bulk Administration Tool

# Provisioning Users and Devices Using Bulk Administration Tool

## Bulk Administration Tool Overview

The Bulk Administration Tool (BAT) is a web-based application that you can use to perform bulk transactions to the Unified
                           Communications Manager database. You can use BAT to add, update, or delete a large number of similar phones, users, or ports
                           at the same time.

The Bulk Administration menu is visible only on the first node of Unified Communications Manager server.

The Cisco Bulk Provisioning Service (BPS) administers and maintains all jobs that are submitted through the Bulk Administration
                           menu of Cisco Unified CM Administration. You can start this service from Cisco Unified Serviceability. You need to activate
                           the Cisco Bulk Provisioning Service only on the first node of Unified Communications Manager.

You can use BAT to perform the following:

Add, update, or delete large numbers of phones in batches

Define the common phone attributes to add a group of new phones

Creates new BAT phone templates

Adds a group of new users and to associate users to phones and other IP Telephony devices

Creates User CSV Data File From BAT Spreadsheet

Creates CSV data file for adding phones and users in batches

Adds a group of phones and users to the Unified Communications Manager database and directory

## Bulk Administration Tool Prerequisites

Configure User and Service Profiles

## Bulk Administration Tool Task Flow

Step 1

Add Phones to Database

You use BAT to add phones and other IP telephony devices in bulk to the Unified Communications Manager database.

Step 2

Create New BAT Phone Template

You can create new BAT phone templates.

Step 3

Create Phone CSV Data File Using BAT Spreadsheet

You can add new phones or IP telephony devices to the system using the .xls spreadsheet that was designed for use with BAT.

Step 4

Create Custom Phone File Format Using Text Editor

You can use a text editor to create a custom phone file format for the text-based CSV data file.

Step 5

Insert Phones Into Unified Communications Manager

You can add phones, Cisco VGC Phones, CTI ports, or H.323 clients into the Unified Communications Manager database.

Step 6

Add Users

You can use BAT to add a group of new users and to associate users to phones and other IP Telephony devices.

Step 7

Create User CSV Data File From BAT Spreadsheet

You can provide details for adding new users to the Unified Communications Manager database in the BAT spreadsheet and then
                                          convert it in to a CSV data file.

Step 8

Insert Users in Unified Communications Manager Database

You can add a group of users to the Unified Communications Manager database using a CSV data file.

Step 9

Add Phone and User File Format

You can add the phone and user file format with a text-based CSV data file. After the CSV data file is created, you need to
                                          associate the file format with the text-based CSV data file.

Step 10

Insert Phones with Users Into Unified Communications Manager

You can add a group of phones and users to the Unified Communications Manager database and directory.

### Add Phones to Database

When you use BAT to add phones and other IP telephony devices in bulk to the Unified Communications Manager database, you can add multiple lines, services, and speed dials for each phone. You can also add CTI ports and H.323 clients.

- Use the BAT spreadsheet (BAT.xlt) and export the data to the CSV format

- Use a text editor to create a text file in CSV format (for experienced users)

Step 1

Choose Bulk
                                                				  Administration > Phones > Phone
                                                				  Template .

The Find and List Phone Templates window displays.

Step 2

Create a CSV data file to insert the phone templates.

Perform one of the following options:

Create a CSV data file using the BAT spreadsheet.

Create a CSV data file using a text editor as follows:

- Choose Bulk Administration > Phones > Phone File Format > Create File Format .

- Use a text editor
                                                      						and create the CSV data file for phones that follows the file format that you
                                                      						want to use.

- Choose Bulk
                                                            							 Administration > Phones > Phone File
                                                            							 Format > Add File Format to associate the text-based file format with the CSV data file.

Step 3

Choose Bulk
                                                				  Administration > Phones > Validate
                                                				  Phones .

Step 4

Choose Bulk Administration > phones > Insert phones to insert phone records into the Unified Communications Manager database.

### Create New BAT Phone Template

You can create new BAT phone templates. After you create a
                                 		  phone template, you can add lines, services, and speed dials.

Step 1

Choose Bulk
                                                				  Administration > Phones > Phone
                                                				  Template .

Step 2

Click Add New . The Add a New Phone Template window displays.

Step 3

From the Phone Type drop-down list, choose the phone model for which you are creating the template. Click Next .

Step 4

From the Select the Device Protocol drop-down list, choose the device protocol. Click Next .

The Phone Template Configuration window displays with fields and default entries for the chosen device type.

Step 5

In the Template Name field, enter a name for the
                                          			 template.

Step 6

In the Device Information area, enter the phone settings that this
                                          			 batch has in common.

Step 7

After you have entered all the settings for this BAT phone
                                          			 template, click Save .

#### Add or Update Phone Lines in BAT Template

You can add one or more lines to the BAT template or to update existing lines. The button template in use for the BAT template
                                    determines the number of lines that you can add or update. You can create a primary phone template that has multiple lines.
                                    Then, you can use the standard template to add phones with a single line or up to the number of lines in the standard template.
                                    All phones or user device profiles in this batch will use the settings that you choose.

Cisco recommends that you use alphanumeric characters for the line
                                    		  template value, so if numbers are given, a chance exists of this conflicting
                                    		  with an actual directory number. This would also avoid conflicts with features
                                    		  such as Call Pickup group number and Call Park number.

The maximum number of lines that display for a BAT template depends on
                                    		  the model and button template that you chose when you created the BAT phone
                                    		  template. For some CiscoUnifiedIPPhone models, you can also add
                                    		  CiscoUnifiedIPPhone services and speed dials to the template.

Step 1

Find the Phone Template to which you want to add the line.

Step 2

In the Phone Template Configuration window,
                                             			 click Line [1] Add a new DN , in the Associated Information area.

Step 3

Enter or choose the appropriate values for the line settings.

Step 4

Click Save .

Step 5

To add settings for any additional lines, repeat Step 2 through Step 4 .

To find existing line template, enter the appropriate search
                                                   				  criteria and click Find .

To add a new line template, click Add New .

#### Add or Update IP Services in BAT Template

You can subscribe CiscoUnifiedIPPhone services to the
                                    		  CiscoUnifiedIPPhone models that include this feature directly in the BAT
                                    		  template. To bulk subscribe users or phones to IP services, the IP services
                                    		  must have common service parameters and be subscribed through a phone template.
                                    		  You can not bulk subscribe IP services that have unique service parameters. For
                                    		  services with unique parameters, use the CSV file.

Step 1

Find the Phone Template to which you want add an IP service.

Step 2

From the Phone Template Configuration window,
                                             			 click Add a new SURL in the Associated Information area.

Step 3

In the Select a Service drop-down list box, choose a
                                             			 service to which you want all phones to be subscribed. The Service Description box displays details about
                                             			 the service that you choose.

Step 4

Click Next .

Step 5

In the Service Name field, modify the name of the
                                             			 service, if required.

Step 6

Associate the selected services or add more services to the
                                             			 template.

To associate these phone services to the phone template, click Save .

To add more services, repeat Step 3 through Step 6 .

To add all the services to the template, click Update .

Step 7

Close the popup window.

#### Add or Update Speed Dials in BAT Template

You can add and update speed dials in the BAT template for
                                    		  phones and Cisco VGC phones if the Phone Button Template provides speed-dial
                                    		  buttons. The Phone Button Template in use for the BAT template determines the
                                    		  number of available speed-dial buttons.

Step 1

Find the Phone Template to which you want to add speed dials.

Step 2

From the Phone Template Configuration window, do one of
                                             			 the following:

Click Add a new SD in the Associated Information area.

Choose Add/Update Speed Dials from the Related Links drop-down list box in the
                                                   				  upper, right-hand corner of the window.

Step 3

In the Speed Dial Settings area, enter the phone
                                             			 number, including any access or long-distance codes, in the Number field.

When you enter the phone number, it can be followed by Forced Authorized Code (FAC)/Client Matter Code (CMC) if applicable.
                                                            You can enter the Phone number, FAC, CMC either in sequence or separated by a comma (,). The Speed dial may include any PIN,
                                                            Password or any other digits to be sent as DTMF digits after the call is connected. If you require a pause while connecting
                                                            through speed dial, you can enter one or more comma (,) where each comma represents a pause of 2 seconds. DTMF digits will
                                                            be sent after the call is connected and the appropriate pause duration corresponding to the number of commas is entered.

Step 4

In the Label field, enter a label that corresponds to
                                             			 the speed-dial number.

Step 5

In the Abbreviated Dial Settings area, you can set
                                             			 abbreviated speed dials for applicable IP phone models. Repeat Step 3 .

Step 6

Click Save .

#### Add or Update Busy Lamp Field in BAT Template

You can add and update busy lamp filed speed dials in the
                                    		  BAT template for phones and Cisco VGC phones if the Phone Button Template
                                    		  provides speed-dial buttons. The Phone Button Template in use for the BAT
                                    		  template determines the number of available BLF SD buttons.

Step 1

Find the Phone Template to which you want to add speed dials.

Step 2

In the Phone Template Configuration window, do one of
                                             			 the following:

Click Add a new BLF SD in the Associated Information area.

Choose Add/Update Busy Lamp Field Speed Dials from the Related Links drop-down list in the upper, right-hand corner of the window.

Step 3

In the Speed Dial Settings area, enter the destination,
                                             			 including any access or long-distance codes, in the Destination field.

Step 4

Choose the directory number from the drop-down list. You can click Find to search for directory numbers.

Step 5

In the Label field, enter a label that corresponds to
                                             			 the BLF SD number.

Step 6

Click Save .

#### Add or Update Busy Lamp Field Directed Call Park in BAT Template

You can add and update busy lamp field (BLF) directed call
                                    		  park in the BAT template for phones and Cisco VGC phones if the Phone Button
                                    		  Template provides speed-dial buttons. The Phone Button Template in use for this
                                    		  BAT template determines the number of available BLF Directed Call Park buttons.

Step 1

Find the Phone Template to which you want to add BLF speed
                                             			 directed call park.

Step 2

In the Phone Template Configuration window, do one of
                                             			 the following:

Click Add a new BLF Directed Call Park in the Associated Information area.

Choose Add/Update BLF Directed Call Park from the Related Links drop-down list box in the
                                                   				  upper, right-hand corner of the window.

Step 3

In the Unassigned Busy Lamp Field/Directed Call Park Settings area, choose the directory number from the drop-down list. You can click Find to search for directory numbers.

Step 4

In the Label field, enter a label that corresponds to
                                             			 the BLF Directed Call Park number.

Step 5

Click Save .

#### Add or Update Intercom Template in BAT Template

You can add one or more Intercom templates to the BAT template, or update existing Intercom templates in the BAT template
                                    The button template in use for the BAT template determines the number of lines that you can add or update. You can create
                                    a standard phone template that has multiple lines. Then, you can use the standard template to add phones with a single line
                                    or up to the number of lines in the standard template. All phones or user device profiles in this batch will use the settings
                                    that you choose for the intercom template.

We recommend that you use alphanumeric characters for intercom template, so if numbers are given, a chance exists of this
                                    conflicting with an actual directory number. This would also avoid conflicts with features such as Call Pickup group number
                                    and Call Park number.

The maximum number of lines that display for a BAT template depends on
                                    		  model and button template that you chose when you created the BAT phone
                                    		  template. For some CiscoUnifiedIPPhone models, you can also add
                                    		  CiscoUnifiedIPPhone services and speed dials to the template.

Step 1

Find the Phone Template to which you want to add the intercom
                                             			 template.

Step 2

In the Phone Template Configuration window, click Intercom [1] - Add a new Intercom in the Associated Information area.

Step 3

Enter or choose the appropriate values for the intercom template
                                             			 settings.

Step 4

Click Save .

Step 5

To add settings for any additional intercom templates, repeat Step 2 through Step 4 .

Click Find and enter the appropriate search criteria and to find existing Intercom directory numbers.

In the Find and List Intercom Directory Number window, click Add New to add a new intercom directory number.

### Create Phone CSV Data File Using BAT Spreadsheet

Use the BAT spreadsheet to create the CSV data file. You can define
                                 		  the file format within the spreadsheet, and the BAT spreadsheet uses the data
                                 		  file formats to display the fields for the CSV data file.

If you enter a comma in one of the fields, BAT.xlt encloses that
                                             			 field entry in double quotes when you export to BAT format.

If you enter a blank row in the BAT spreadsheet, the system treats
                                             			 the empty row as the end of the file and does not convert data that is entered
                                             			 after a blank line to the BAT format.

You can use the pseudo MAC address option when adding CTI ports. This option gives a unique device name to each CTI port in the form of pseudo MAC addresses that you can manually update later using the Cisco Unified Communications Manager Administration or the Unified CM Auto-Register phone Tool. Do not use the pseudo MAC address option for H.323 clients, VGC phones, or VGC virtual phones.

The pseudo MAC address option automatically generates pseudo MAC addresses in the following format:

XXXXXXXXXXXX

where X represents any 12-character, hexadecimal (0-9 and A-F) number.

Attention

The number of lines and speed dials that you define for phones in
                                             			 the BAT spreadsheet must not exceed the numbers that are defined in the BAT
                                             			 phone template, otherwise, an error occurs when you attempt to insert the CSV
                                             			 data file and BAT template.

After you have finished editing all the fields in the BAT spreadsheet,
                                 		  you can export the content to a CSV formatted data file. A default filename is
                                 		  assigned to the exported CSV formatted data file:

<tabname>-<timestamp>.txt

where <tabname> represents the type of input file that
                                 		  you created, such as phones, and <timestamp> represents the precise date and time
                                 		  that the file was created.

You can rename the CSV formatted data file after you save the exported
                                 		  file to your local workstation.

You cannot upload a CSV filename that contains a comma (for example, abcd,e.txt) to the Unified Communications Manager server.

Step 1

To open the BAT spreadsheet, locate and double-click the BAT.xlt
                                          			 file

Step 2

When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities.

Step 3

To display the phones options, click the Phones tab at the bottom of the spreadsheet.

Step 4

Choose the radio button for one of the following device types:

The device type that you select determines the validation criteria
                                             				for data in the BAT spreadsheet.

Phones

CTI Port

H.323 Client

VGC Phones

VGC Virtual Phones

Cisco IP Communicator Phone

Step 5

Choose the device and line fields to appear in the BAT spreadsheet
                                          			 for each phone. Do the following:

Click Create File Format .

To choose the device fields, click a device field name in
                                                				  the Device Field box and then click the arrow to move
                                                				  the field to the Selected Device Fields box.

A CSV data file must include MAC Address/Device Name and Description ; therefore, these fields
                                                   					 always remain selected.

Tip

To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names.

Click a line field name in the Line Field box and click the arrow to move
                                                				  the field to the Selected Line Fields box.

Tip

To change the order of the items in the Selected Line and Device boxes, choose an item and use
                                                               						the up and down arrows to move the field up or down in the list.

A message asks whether you want to overwrite the existing CSV
                                                				  format. Click Create to modify the CSV data file format.

Click OK .

Step 6

Scroll to the right to locate the Number of Phone Lines box and enter the number
                                          			 of lines for the phone.

The number of lines you enter must not exceed the number of lines that are configured in the BAT template.

Step 7

For phones, you must enter the number of speed-dial buttons in the Maximum Number of Speed Dials box.

The number of speed dials you enter must not exceed the number of speed dials that are configured in the BAT template.

Step 8

Enter the number of Busy Lamp Field (BLF) speed-dial buttons in
                                          			 the Maximum Number of BLF Speed Dials box.

Step 9

Enter data for an individual phone on each line in the
                                          			 spreadsheet.

Complete all mandatory fields and any relevant, optional fields. Each column heading specifies the length of the field and
                                             whether it is required or optional. See online help for phone field descriptions.

Step 10

If you did not enter the MAC address for each phone, check the Create Pseudo MAC Address check box.

Attention

Do not use the pseudo MAC address option for H.323 clients, VGC phones, or VGC virtual phones.

Step 11

To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 formatted data file, click Export to BAT Format .

Tip

For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 phones window in BAT.

### Create Custom Phone File Format Using Text Editor

You can use a text editor to create a custom phone file
                                 		  format for the text-based CSV data file.

Step 1

Choose Bulk
                                                				  Administration > Phones > Phone File
                                                				  Format > Create File Format .

Step 2

Click Add New .

Step 3

In the Format Name field, enter a name for this
                                          			 custom format.

Step 4

Choose the fields to appear in the custom file format. Do the
                                          			 following:

To choose the device fields, click a device field name in
                                                				  the Device Field box and then click the arrow to move
                                                				  the field to the Selected Device Fields box.

A CSV data file must include MAC Address/Device Name and Description ; therefore, these fields
                                                   					 always remain selected.

Tip

To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names.

Click a line field name in the Line Field box and click the arrow to move
                                                				  the field to the Selected Line Fields box.

Click the intercom DN field names in the Intercom DN Fields box and click the arrow
                                                				  to move the fields to the Selected Intercom DN Fields Order box.

Tip

You can change the order of the items in the Selected Line Fields , Selected Device Fields , and Selected Intercom DN Fields Order boxes. Choose an item and use the up and down arrows to move the field up or
                                                               						down in the list.

Step 5

In the IP Phone Services Maximums area, enter the
                                          			 maximum values for the following fields:

Maximum Number of Speed Dials

Maximum Number of BLF Speed Dials

Maximum Number of BLF Directed Call Parks

Maximum Number of IP Phone Services

Maximum Number of IP Phone Service Parameters

Step 6

Click Save .

### Insert Phones Into Unified Communications Manager

When you insert phone records into the Unified Communications Manager database, you define the target CSV data file and how the phone records get inserted. Select any combination of the listed
                                 actions to overwrite the existing phone records, or you can choose to insert the records during upload:

Delete all existing Speed Dials before adding new one

Delete all existing BLF Speed Dials before adding new one

Delete all existing BLF Directed Call Parks before adding new one

Delete all existing Subscribed Services before adding new one

Phone records
                                             			 must be validated before insertion.

BAT expects Directory Number URI fields for directory
                                             			 numbers in the following format:

URI 1 on
                                             			 Directory Number 1, URI 1 Route Partition on Directory Number 1, URI 1 is
                                             			 Primary on Directory Number 1.

You can use the pseudo MAC address option. When adding CTI ports, this option gives a unique device name to each CTI port in the form of pseudo MAC addresses that you can manually update later using the Unified Communications Manager Administration or the Unified CM Auto-Register Phone Tool. Do not use the pseudo MAC address option for H.323 clients, VGC phones, or VGC virtual phones.

The pseudo MAC address option automatically generates pseudo MAC addresses in the following format:

XXXXXXXXXXXX

where X represents
                                 		  any 12-character, hexadecimal (0-9 and A-F) number.

#### Before you begin

You must have a Unified Communications Manager Bulk Administration (BAT) phone template for the devices that you are adding. You can choose the target and method of the
                                       data file upload. Phone records must be validated before insertion.

You must have a data file in comma separated value (CSV) format that contains the unique details for the phones or other IP
                                       telephony devices.

Step 1

Choose Bulk
                                                				  Administration > Phones > Insert Phones .

Step 2

Specify the file
                                          			 format type for the phone record that you are uploading.

To insert
                                                				  phone records that use a customized file format, click Insert Phones Specific Details radio button and
                                                				  continue with Step 3 and Step 5 .

To insert phone records from an exported phone's file that was generated using the All Details option, click Insert phones All Details radio button.

Step 3

In the File Name drop-down list box, choose the CSV data file that you created for this specific bulk transaction. Next, check the Allow Update Phone with Custom File check box to allow updating the phone with the chosen custom file.

Step 4

Check the Override the existing configuration check box to overwrite the existing phone settings with the information that is contained in the file that you want to insert.
                                          Next, check the check boxes beside the upload action(s) to perform during the upload.

The following upload actions get enabled for selection after you have checked the Override the existing configuration check box.

Delete all existing Speed Dials before adding new one.

Delete all existing BLF Speed Dials before adding new one.

Delete all existing BLF Directed Call Parks before adding new one.

Delete all existing Subscribed Services before adding new one.

Leave the check boxes clear to append those records to the existing records in the CSV data file during the upload.

Step 5

For the Specific Details option, in the Phone Template Name drop-down list, choose the BAT phone template that you created for this type of bulk transaction.

Attention

If you did not enter individual MAC addresses in the CSV data file, you must check the Create Pseudo MAC Address check box. You can update this information manually later. Skip to Step 8 . If you supplied MAC addresses or device names in the data input file, do not choose this option.

If you do not know the MAC address of the phone that is assigned to the user, then choose this option. When the phone is plugged
                                                         in, a MAC address registers for that device.

Step 6

In the Job
                                             				Information area, enter the Job description.

Step 7

Choose an insert
                                          			 method. Do one of the following:

Click Run
                                                   					 Immediately to insert the phone records immediately.

Click Run Later to insert the phone records later.

Step 8

Click Submit to create a job for inserting the phone
                                          			 records.

#### What to do next

If the phones
                                 		  inserted are of the type Cisco Unified Mobile Communicator, then you must reset
                                 		  the devices after the insert job is completed. You can reset the phones using
                                 		  the Bulk
                                       				Administration > Phones > Reset/Restart Phones option.

### Add Users

You must create a CSV data file to add new users in bulk to the Unified Communications Manager database using the BAT spreadsheet. For users who have applications that require a CTI port, such as CiscoIPSoftPhone, BAT
                                 can associate CTI ports to existing users.

Step 1

Create a comma separated values (CSV) data file to define
                                          			 individual values for each user that you want to add.

Step 2

Use BAT to insert the users in the Unified Communications Manager database.

### Create User CSV Data File From BAT Spreadsheet

You can provide details for adding new users to the Unified Communications Manager database in the BAT spreadsheet and then convert it in to a CSV data file.

If you enter a blank row in the BAT spreadsheet, the system treats
                                             			 the empty row as the end of the file and does not convert data that is entered
                                             			 after a blank line to the BAT format.

After you have finished editing the fields to add users in the BAT
                                 		  spreadsheet, you can export the content to a CSV formatted data file. A default
                                 		  filename is assigned to the exported CSV formatted data file:

<tabname>-<timestamp>.txt

where <tabname> represents the type of input file that
                                 		  you created, such as phones, and <timestamp> represents the precise date and time
                                 		  that the file was created.

You can rename the CSV formatted data file after you save the exported
                                 		  file to your local workstation. If you enter a comma in one of the fields,
                                 		  BAT.xlt encloses that field entry in double quotes when you export to BAT
                                 		  format.

You cannot upload a CSV filename that contains a comma (for example, abcd,e.txt) to the Unified Communications Manager server.

Step 1

To open the BAT spreadsheet, locate and double-click BAT.xlt file.

Step 2

When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities.

Step 3

To add users, click the Users tab at the bottom of the spreadsheet.

Step 4

Complete all mandatory fields and any relevant optional fields.
                                          			 Each column heading specifies the length of the field and whether it is
                                          			 required or optional.

- If a user has multiple devices, the device name field should be repeated, once for each device.

- To enter additional device names that will be associated to a new user, enter a value in the Number of Controlled Devices text box.

You can associate all devices, including CTI ports, ATA ports, and H.323 clients, with a user.

Step 5

To enter additional device names that will be associated to a new
                                          			 user, enter a value in the Number of Controlled Devices text box.

Step 6

Click Export to BAT Format to transfer the data from
                                          			 the BAT Excel spreadsheet into a CSV formatted data file.

The system saves the file to C:\XLSDataFiles with the default file name <tabname>-<timestamp>.txt , or uses Browse to save the file to another existing folder.

Tip

For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Users window in BAT.

#### What to do next

You must upload the CSV data file to the first node of Unified Communications Manager database server so that BAT can access the data file.

### Insert Users in Unified Communications Manager Database

You can add a group of users to the Unified Communications Manager database using a CSV data file. The field values that you enter in the CSV file for inserting users override the values provided
                                 in the user template.

Attention

If the credential policy has "check for trivial password" enabled, and the password in the
                                             			 user template is the user ID, inserting users through BAT may fail if the user
                                             			 ID does not satisfy the necessary criteria for the trivial password.

Users can be inserted using BAT with primary extension configured without any devices selected for controlled devices. To
                                 do so, you must pre-populate the DN in Unified Communications Manager before inserting the users using BAT. The following
                                 steps outline the process of pre-populating the DN:

Create range of DNs to be associated for primary extension for users in the DN page.

Create a BAT template with primary extension configured (which should be the same DN's pre-populated).

Insert the users using BAT (as shown in the following procedure)

#### Before you begin

You must have a CSV data file that is saved in the UTF-8 encoding format and that contains the usernames, controlled device
                                 names, and directory numbers. You can create the CSV data file by using one of these methods:

- BAT spreadsheet that is
                                    			 converted to CSV format

- Export utility that
                                    			 produces an export file of user data

When you are inserting users by using an exported BAT file, you
                                             			 might get errors stating "User ID already exists" for some users that were exported in
                                             			 more than one file. For example, a list of first line managers and a list of
                                             			 users might both include the same manager user ID.

Step 1

Choose Bulk
                                                				  Administration > Users > Insert
                                                				  Users .

Step 2

In the File Name field, choose the CSV data file that you created for this
                                          			 bulk transaction.

Step 3

If the CSV data file was created by using the export utility,
                                          			 check the File created with Export Users check box.

Step 4

From the User Template Name drop-down list, choose the user template you want to use for this insert.

The User Profile, Controlled Device Name, and Directory Number should exist in the Unified Communications Manager database. The controlled device name should be entered in full. If it contains only MAC Address, then BAT displays a non-existing
                                                         device error.

Step 5

In the Job Information area, enter the Job
                                          			 description.

Step 6

Choose an insert method. Do one of the following:

Click Run Immediately to insert the user records
                                                				  immediately.

Click Run Later to insert the user records at a
                                                				  later time.

Step 7

To create a job for inserting the user records, click Submit .

### Add Phones with Users Using the BAT Spreadsheet

Create a CSV data file for adding phones and users in bulk.

Step 1

To open the BAT spreadsheet, locate and double-click BAT.xlt file.

Step 2

When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities.

Step 3

At the bottom of the spreadsheet, click the Phones-Users tab.

Step 4

Follow steps 4 through 10 in Create Phone CSV Data File Using BAT Spreadsheet .

### Add Phone and User File Format

You can add the phone and user file format with a text-based
                                 		  CSV data file. After the CSV data file is created, you need to associate the
                                 		  file format with the text-based CSV data file. After associating the file
                                 		  format with the CSV file, the names for each field display as the first record
                                 		  in the CSV data file. You can use this information to verify that you entered
                                 		  the values for each field in the correct order.

#### Before you begin

You must create a CSV data file that defines individual values for each user that you want to update.

When you use a text editor to create the CSV data file, you create a
                                 		  file format for entering values in the text-based file. You enter values in the
                                 		  text file in the order that the file format specifies.

Step 1

Choose Bulk
                                                				  Administration > Phones and
                                                				  Users > Phones & Users File
                                                				  Format > Assign File Format .

Step 2

In the File Name field, choose the text-based CSV
                                          			 file that you created for this transaction.

Step 3

In the Format File Name field, choose the file format
                                          			 that you created for this type of bulk transaction.

Step 4

To create a job for associating the matching file format with the
                                          			 CSV data file, click Submit .

Step 5

To schedule and/or activate this job, use the Job Scheduler option
                                          			 in the Bulk Administration main menu.

### Insert Phones with Users Into Unified Communications Manager

You can add a group of phones and users to the Unified Communications Manager database and directory.

Phone records must be validated before insertion.

You can use the pseudo MAC address option. When adding CTI ports, this option gives a unique device name to each CTI port in the form of pseudo MAC addresses that you can manually update later using the Unified Communications Manager Administration or the Unified CM Auto-Register phone Tool. Do not use the pseudo MAC address option for H.323 clients, VGC phones, or VGC virtual phones.

The pseudo MAC address option automatically generates pseudo MAC addresses in the following format:

XXXXXXXXXXXX

where X represents any 12-character, hexadecimal (0-9 and A-F) number.

#### Before you begin

Create a comma-separated values (CSV) data file to define individual values for each phone with users that you want to insert.
                                       You can create the CSV data file using the BAT spreadsheet (BAT.xlt) to add phones with users, or create a custom text file
                                       in CSV format to add phones with users combinations.

Associate file format with the CSV data file.

Validate phones with users records.

Step 1

Choose Bulk
                                                				  Administration > Phones &
                                                				  Users > Insert Phones with Users .

Step 2

In the File Name field, choose the CSV data file that
                                          			 you created for this bulk transaction.

Step 3

In the Phone Template Name field, choose the BAT
                                          			 phone template that you used for this transaction.

Attention

If you did not enter individual MAC addresses in the CSV data file, you must check the Create Pseudo MAC Address check box. You can update this information manually later. If you supplied MAC addresses or device names in the data input
                                                         file, do not choose this option.

If you do not know the MAC address of the phone that is assigned to the user, choose this option. When the phone is plugged
                                                         in, a MAC address registers for that device.

Step 4

In the User Template Name field, choose the BAT user
                                          			 template that you used for this transaction

Step 5

In the Job Information area, enter the Job description.

Step 6

Choose an insert method. Do one of the following:

Click Run Immediately to insert the phones with
                                                				  users immediately.

Click Run Later to insert the phones with users
                                                				  at a later time.

Step 7

To create a job for inserting the phones and user records, click Submit .

| Note | The Bulk Administration menu is visible only on the first node of Unified Communications Manager server. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Add Phones to Database | You use BAT to add phones and other IP telephony devices in bulk to the Unified Communications Manager database. |
| Step 2 | Create New BAT Phone Template | You can create new BAT phone templates. |
| Step 3 | Create Phone CSV Data File Using BAT Spreadsheet | You can add new phones or IP telephony devices to the system using the .xls spreadsheet that was designed for use with BAT. |
| Step 4 | Create Custom Phone File Format Using Text Editor | You can use a text editor to create a custom phone file format for the text-based CSV data file. |
| Step 5 | Insert Phones Into Unified Communications Manager | You can add phones, Cisco VGC Phones, CTI ports, or H.323 clients into the Unified Communications Manager database. |
| Step 6 | Add Users | You can use BAT to add a group of new users and to associate users to phones and other IP Telephony devices. |
| Step 7 | Create User CSV Data File From BAT Spreadsheet | You can provide details for adding new users to the Unified Communications Manager database in the BAT spreadsheet and then
                                          convert it in to a CSV data file. |
| Step 8 | Insert Users in Unified Communications Manager Database | You can add a group of users to the Unified Communications Manager database using a CSV data file. |
| Step 9 | Add Phone and User File Format | You can add the phone and user file format with a text-based CSV data file. After the CSV data file is created, you need to
                                          associate the file format with the text-based CSV data file. |
| Step 10 | Insert Phones with Users Into Unified Communications Manager | You can add a group of phones and users to the Unified Communications Manager database and directory. |

| Step 1 | Choose Bulk
                                                				  Administration > Phones > Phone
                                                				  Template . The Find and List Phone Templates window displays. |
|---|---|
| Step 2 | Create a CSV data file to insert the phone templates. Perform one of the following options: Create a CSV data file using the BAT spreadsheet. Create a CSV data file using a text editor as follows: Choose Bulk Administration > Phones > Phone File Format > Create File Format . Use a text editor
                                                      						and create the CSV data file for phones that follows the file format that you
                                                      						want to use. Choose Bulk
                                                            							 Administration > Phones > Phone File
                                                            							 Format > Add File Format to associate the text-based file format with the CSV data file. |
| Step 3 | Choose Bulk
                                                				  Administration > Phones > Validate
                                                				  Phones . |
| Step 4 | Choose Bulk Administration > phones > Insert phones to insert phone records into the Unified Communications Manager database. |

| Step 1 | Choose Bulk
                                                				  Administration > Phones > Phone
                                                				  Template . |
|---|---|
| Step 2 | Click Add New . The Add a New Phone Template window displays. |
| Step 3 | From the Phone Type drop-down list, choose the phone model for which you are creating the template. Click Next . |
| Step 4 | From the Select the Device Protocol drop-down list, choose the device protocol. Click Next . The Phone Template Configuration window displays with fields and default entries for the chosen device type. |
| Step 5 | In the Template Name field, enter a name for the
                                          			 template. The name can contain up to 50 alphanumeric characters. |
| Step 6 | In the Device Information area, enter the phone settings that this
                                          			 batch has in common. Some phone models and device types do not have all the attributes that the table lists. See, the phone model documentation
                                          for information on all the attributes. |
| Step 7 | After you have entered all the settings for this BAT phone
                                          			 template, click Save . |

| Step 1 | Find the Phone Template to which you want to add the line. |
|---|---|
| Step 2 | In the Phone Template Configuration window,
                                             			 click Line [1] Add a new DN , in the Associated Information area. The Line Template Configuration window displays. |
| Step 3 | Enter or choose the appropriate values for the line settings. |
| Step 4 | Click Save . |
| Step 5 | To add settings for any additional lines, repeat Step 2 through Step 4 . If you choose Back to Find/List from the Related
                                                				Links drop-down list box in the upper, right, corner of
                                             			 the Line Template Configuration window, the Find and List Line Template window displays. To find existing line template, enter the appropriate search
                                                   				  criteria and click Find . To add a new line template, click Add New . |

| Step 1 | Find the Phone Template to which you want add an IP service. |
|---|---|
| Step 2 | From the Phone Template Configuration window,
                                             			 click Add a new SURL in the Associated Information area. A popup window displays. In this window, you can subscribe
                                             			 to CiscoUnifiedIPPhone services that are available. |
| Step 3 | In the Select a Service drop-down list box, choose a
                                             			 service to which you want all phones to be subscribed. The Service Description box displays details about
                                             			 the service that you choose. |
| Step 4 | Click Next . |
| Step 5 | In the Service Name field, modify the name of the
                                             			 service, if required. |
| Step 6 | Associate the selected services or add more services to the
                                             			 template. To associate these phone services to the phone template, click Save . To add more services, repeat Step 3 through Step 6 . To add all the services to the template, click Update . After you are done adding or updating services for the
                                             			 selected template, proceed to the next step. |
| Step 7 | Close the popup window. |

| Step 1 | Find the Phone Template to which you want to add speed dials. |
|---|---|
| Step 2 | From the Phone Template Configuration window, do one of
                                             			 the following: Click Add a new SD in the Associated Information area. Choose Add/Update Speed Dials from the Related Links drop-down list box in the
                                                   				  upper, right-hand corner of the window. A popup window displays. In this window, you can designate
                                             			 speed-dial buttons for CiscoUnifiedIPPhones and expansion modules. |
| Step 3 | In the Speed Dial Settings area, enter the phone
                                             			 number, including any access or long-distance codes, in the Number field. Note When you enter the phone number, it can be followed by Forced Authorized Code (FAC)/Client Matter Code (CMC) if applicable.
                                                            You can enter the Phone number, FAC, CMC either in sequence or separated by a comma (,). The Speed dial may include any PIN,
                                                            Password or any other digits to be sent as DTMF digits after the call is connected. If you require a pause while connecting
                                                            through speed dial, you can enter one or more comma (,) where each comma represents a pause of 2 seconds. DTMF digits will
                                                            be sent after the call is connected and the appropriate pause duration corresponding to the number of commas is entered. | Note | When you enter the phone number, it can be followed by Forced Authorized Code (FAC)/Client Matter Code (CMC) if applicable.
                                                            You can enter the Phone number, FAC, CMC either in sequence or separated by a comma (,). The Speed dial may include any PIN,
                                                            Password or any other digits to be sent as DTMF digits after the call is connected. If you require a pause while connecting
                                                            through speed dial, you can enter one or more comma (,) where each comma represents a pause of 2 seconds. DTMF digits will
                                                            be sent after the call is connected and the appropriate pause duration corresponding to the number of commas is entered. |
| Note | When you enter the phone number, it can be followed by Forced Authorized Code (FAC)/Client Matter Code (CMC) if applicable.
                                                            You can enter the Phone number, FAC, CMC either in sequence or separated by a comma (,). The Speed dial may include any PIN,
                                                            Password or any other digits to be sent as DTMF digits after the call is connected. If you require a pause while connecting
                                                            through speed dial, you can enter one or more comma (,) where each comma represents a pause of 2 seconds. DTMF digits will
                                                            be sent after the call is connected and the appropriate pause duration corresponding to the number of commas is entered. |
| Step 4 | In the Label field, enter a label that corresponds to
                                             			 the speed-dial number. |
| Step 5 | In the Abbreviated Dial Settings area, you can set
                                             			 abbreviated speed dials for applicable IP phone models. Repeat Step 3 . |
| Step 6 | Click Save . BAT inserts the speed-dial settings in the template and the
                                             			 popup window closes. |

| Note | When you enter the phone number, it can be followed by Forced Authorized Code (FAC)/Client Matter Code (CMC) if applicable.
                                                            You can enter the Phone number, FAC, CMC either in sequence or separated by a comma (,). The Speed dial may include any PIN,
                                                            Password or any other digits to be sent as DTMF digits after the call is connected. If you require a pause while connecting
                                                            through speed dial, you can enter one or more comma (,) where each comma represents a pause of 2 seconds. DTMF digits will
                                                            be sent after the call is connected and the appropriate pause duration corresponding to the number of commas is entered. |
|---|---|

| Step 1 | Find the Phone Template to which you want to add speed dials. |
|---|---|
| Step 2 | In the Phone Template Configuration window, do one of
                                             			 the following: Click Add a new BLF SD in the Associated Information area. Choose Add/Update Busy Lamp Field Speed Dials from the Related Links drop-down list in the upper, right-hand corner of the window. A popup window displays. In this window, you can designate
                                             			 busy lamp field speed-dial (BLF SD) buttons for CiscoUnifiedIPPhones and
                                             			 expansion modules. |
| Step 3 | In the Speed Dial Settings area, enter the destination,
                                             			 including any access or long-distance codes, in the Destination field. |
| Step 4 | Choose the directory number from the drop-down list. You can click Find to search for directory numbers. |
| Step 5 | In the Label field, enter a label that corresponds to
                                             			 the BLF SD number. |
| Step 6 | Click Save . BAT inserts the BLF SD settings in the template, and the
                                             			 popup window closes. |

| Step 1 | Find the Phone Template to which you want to add BLF speed
                                             			 directed call park. |
|---|---|
| Step 2 | In the Phone Template Configuration window, do one of
                                             			 the following: Click Add a new BLF Directed Call Park in the Associated Information area. Choose Add/Update BLF Directed Call Park from the Related Links drop-down list box in the
                                                   				  upper, right-hand corner of the window. A popup window displays. In this window, you can designate
                                             			 BLF Directed Call Park buttons for CiscoUnifiedIPPhones and expansion
                                             			 modules. |
| Step 3 | In the Unassigned Busy Lamp Field/Directed Call Park Settings area, choose the directory number from the drop-down list. You can click Find to search for directory numbers. |
| Step 4 | In the Label field, enter a label that corresponds to
                                             			 the BLF Directed Call Park number. |
| Step 5 | Click Save . BAT inserts the BLF Directed Call Park settings in the
                                             			 template, and the popup window closes. |

| Step 1 | Find the Phone Template to which you want to add the intercom
                                             			 template. |
|---|---|
| Step 2 | In the Phone Template Configuration window, click Intercom [1] - Add a new Intercom in the Associated Information area. The Intercom Template Configuration window displays. |
| Step 3 | Enter or choose the appropriate values for the intercom template
                                             			 settings. |
| Step 4 | Click Save . BAT adds the intercom template to the phone template
                                             			 configuration. |
| Step 5 | To add settings for any additional intercom templates, repeat Step 2 through Step 4 . If you choose Back to Find/List from the Related Links drop-down list box in the upper, right, corner of the Intercom Template Configuration window, the Find and List Intercom Directory Number window displays. Note If you choose Back to Find/List from the Related Links drop-down list box in the upper, right, corner of the Intercom Template Configuration window, the Find and List Intercom Directory Number window displays. Click Find and enter the appropriate search criteria and to find existing Intercom directory numbers. In the Find and List Intercom Directory Number window, click Add New to add a new intercom directory number. | Note | If you choose Back to Find/List from the Related Links drop-down list box in the upper, right, corner of the Intercom Template Configuration window, the Find and List Intercom Directory Number window displays. |
| Note | If you choose Back to Find/List from the Related Links drop-down list box in the upper, right, corner of the Intercom Template Configuration window, the Find and List Intercom Directory Number window displays. |

| Note | If you choose Back to Find/List from the Related Links drop-down list box in the upper, right, corner of the Intercom Template Configuration window, the Find and List Intercom Directory Number window displays. |
|---|---|

| Note | If you enter a comma in one of the fields, BAT.xlt encloses that
                                             			 field entry in double quotes when you export to BAT format. If you enter a blank row in the BAT spreadsheet, the system treats
                                             			 the empty row as the end of the file and does not convert data that is entered
                                             			 after a blank line to the BAT format. |
|---|---|

| Attention | The number of lines and speed dials that you define for phones in
                                             			 the BAT spreadsheet must not exceed the numbers that are defined in the BAT
                                             			 phone template, otherwise, an error occurs when you attempt to insert the CSV
                                             			 data file and BAT template. |
|---|---|

| Note | You cannot upload a CSV filename that contains a comma (for example, abcd,e.txt) to the Unified Communications Manager server. |
|---|---|

| Step 1 | To open the BAT spreadsheet, locate and double-click the BAT.xlt
                                          			 file |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities. |
| Step 3 | To display the phones options, click the Phones tab at the bottom of the spreadsheet. |
| Step 4 | Choose the radio button for one of the following device types: The device type that you select determines the validation criteria
                                             				for data in the BAT spreadsheet. Phones CTI Port H.323 Client VGC Phones VGC Virtual Phones Cisco IP Communicator Phone The spreadsheet displays options that are available for the
                                          			 chosen device. For example, when you choose phones, fields for the number of
                                          			 phone lines and the number of speed dials display. |
| Step 5 | Choose the device and line fields to appear in the BAT spreadsheet
                                          			 for each phone. Do the following: Click Create File Format . To choose the device fields, click a device field name in
                                                				  the Device Field box and then click the arrow to move
                                                				  the field to the Selected Device Fields box. A CSV data file must include MAC Address/Device Name and Description ; therefore, these fields
                                                   					 always remain selected. Tip To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names. Click a line field name in the Line Field box and click the arrow to move
                                                				  the field to the Selected Line Fields box. Tip To change the order of the items in the Selected Line and Device boxes, choose an item and use
                                                               						the up and down arrows to move the field up or down in the list. A message asks whether you want to overwrite the existing CSV
                                                				  format. Click Create to modify the CSV data file format. Click OK . New columns for the selected fields display in the BAT
                                                				  spreadsheet in the order that you specified. | Tip | To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names. | Tip | To change the order of the items in the Selected Line and Device boxes, choose an item and use
                                                               						the up and down arrows to move the field up or down in the list. |
| Tip | To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names. |
| Tip | To change the order of the items in the Selected Line and Device boxes, choose an item and use
                                                               						the up and down arrows to move the field up or down in the list. |
| Step 6 | Scroll to the right to locate the Number of Phone Lines box and enter the number
                                          			 of lines for the phone. Note The number of lines you enter must not exceed the number of lines that are configured in the BAT template. | Note | The number of lines you enter must not exceed the number of lines that are configured in the BAT template. |
| Note | The number of lines you enter must not exceed the number of lines that are configured in the BAT template. |
| Step 7 | For phones, you must enter the number of speed-dial buttons in the Maximum Number of Speed Dials box. Note The number of speed dials you enter must not exceed the number of speed dials that are configured in the BAT template. After you enter the number, columns display for each
                                          			 speed-dial number. | Note | The number of speed dials you enter must not exceed the number of speed dials that are configured in the BAT template. |
| Note | The number of speed dials you enter must not exceed the number of speed dials that are configured in the BAT template. |
| Step 8 | Enter the number of Busy Lamp Field (BLF) speed-dial buttons in
                                          			 the Maximum Number of BLF Speed Dials box. After you enter the number, columns display for each BLF
                                          			 speed-dial number. |
| Step 9 | Enter data for an individual phone on each line in the
                                          			 spreadsheet. Complete all mandatory fields and any relevant, optional fields. Each column heading specifies the length of the field and
                                             whether it is required or optional. See online help for phone field descriptions. |
| Step 10 | If you did not enter the MAC address for each phone, check the Create Pseudo MAC Address check box. Attention Do not use the pseudo MAC address option for H.323 clients, VGC phones, or VGC virtual phones. | Attention | Do not use the pseudo MAC address option for H.323 clients, VGC phones, or VGC virtual phones. |
| Attention | Do not use the pseudo MAC address option for H.323 clients, VGC phones, or VGC virtual phones. |
| Step 11 | To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 formatted data file, click Export to BAT Format . Tip For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 phones window in BAT. The system saves the file with the default filename: <tabname>-<timestamp>.txt to your choice of a folder on your local workstation. | Tip | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 phones window in BAT. |
| Tip | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 phones window in BAT. |

| Tip | To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names. |
|---|---|

| Tip | To change the order of the items in the Selected Line and Device boxes, choose an item and use
                                                               						the up and down arrows to move the field up or down in the list. |
|---|---|

| Note | The number of lines you enter must not exceed the number of lines that are configured in the BAT template. |
|---|---|

| Note | The number of speed dials you enter must not exceed the number of speed dials that are configured in the BAT template. |
|---|---|

| Attention | Do not use the pseudo MAC address option for H.323 clients, VGC phones, or VGC virtual phones. |
|---|---|

| Tip | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 phones window in BAT. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Phones > Phone File
                                                				  Format > Create File Format . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the Format Name field, enter a name for this
                                          			 custom format. |
| Step 4 | Choose the fields to appear in the custom file format. Do the
                                          			 following: To choose the device fields, click a device field name in
                                                				  the Device Field box and then click the arrow to move
                                                				  the field to the Selected Device Fields box. A CSV data file must include MAC Address/Device Name and Description ; therefore, these fields
                                                   					 always remain selected. Tip To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names. Click a line field name in the Line Field box and click the arrow to move
                                                				  the field to the Selected Line Fields box. Click the intercom DN field names in the Intercom DN Fields box and click the arrow
                                                				  to move the fields to the Selected Intercom DN Fields Order box. Tip You can change the order of the items in the Selected Line Fields , Selected Device Fields , and Selected Intercom DN Fields Order boxes. Choose an item and use the up and down arrows to move the field up or
                                                               						down in the list. | Tip | To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names. | Tip | You can change the order of the items in the Selected Line Fields , Selected Device Fields , and Selected Intercom DN Fields Order boxes. Choose an item and use the up and down arrows to move the field up or
                                                               						down in the list. |
| Tip | To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names. |
| Tip | You can change the order of the items in the Selected Line Fields , Selected Device Fields , and Selected Intercom DN Fields Order boxes. Choose an item and use the up and down arrows to move the field up or
                                                               						down in the list. |
| Step 5 | In the IP Phone Services Maximums area, enter the
                                          			 maximum values for the following fields: Maximum Number of Speed Dials Maximum Number of BLF Speed Dials Maximum Number of BLF Directed Call Parks Maximum Number of IP Phone Services Maximum Number of IP Phone Service Parameters |
| Step 6 | Click Save . The name of the custom file format displays in the File Format Names list in the Find and List Phone File Formats window. |

| Tip | To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names. |
|---|---|

| Tip | You can change the order of the items in the Selected Line Fields , Selected Device Fields , and Selected Intercom DN Fields Order boxes. Choose an item and use the up and down arrows to move the field up or
                                                               						down in the list. |
|---|---|

| Note | Phone records
                                             			 must be validated before insertion. |
|---|---|

| Note | BAT expects Directory Number URI fields for directory
                                             			 numbers in the following format: URI 1 on
                                             			 Directory Number 1, URI 1 Route Partition on Directory Number 1, URI 1 is
                                             			 Primary on Directory Number 1. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Phones > Insert Phones . |
|---|---|
| Step 2 | Specify the file
                                          			 format type for the phone record that you are uploading. To insert
                                                				  phone records that use a customized file format, click Insert Phones Specific Details radio button and
                                                				  continue with Step 3 and Step 5 . To insert phone records from an exported phone's file that was generated using the All Details option, click Insert phones All Details radio button. |
| Step 3 | In the File Name drop-down list box, choose the CSV data file that you created for this specific bulk transaction. Next, check the Allow Update Phone with Custom File check box to allow updating the phone with the chosen custom file. |
| Step 4 | Check the Override the existing configuration check box to overwrite the existing phone settings with the information that is contained in the file that you want to insert.
                                          Next, check the check boxes beside the upload action(s) to perform during the upload. The following upload actions get enabled for selection after you have checked the Override the existing configuration check box. Delete all existing Speed Dials before adding new one. Delete all existing BLF Speed Dials before adding new one. Delete all existing BLF Directed Call Parks before adding new one. Delete all existing Subscribed Services before adding new one. Note Leave the check boxes clear to append those records to the existing records in the CSV data file during the upload. | Note | Leave the check boxes clear to append those records to the existing records in the CSV data file during the upload. |
| Note | Leave the check boxes clear to append those records to the existing records in the CSV data file during the upload. |
| Step 5 | For the Specific Details option, in the Phone Template Name drop-down list, choose the BAT phone template that you created for this type of bulk transaction. Attention If you did not enter individual MAC addresses in the CSV data file, you must check the Create Pseudo MAC Address check box. You can update this information manually later. Skip to Step 8 . If you supplied MAC addresses or device names in the data input file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, then choose this option. When the phone is plugged
                                                         in, a MAC address registers for that device. | Attention | If you did not enter individual MAC addresses in the CSV data file, you must check the Create Pseudo MAC Address check box. You can update this information manually later. Skip to Step 8 . If you supplied MAC addresses or device names in the data input file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, then choose this option. When the phone is plugged
                                                         in, a MAC address registers for that device. |
| Attention | If you did not enter individual MAC addresses in the CSV data file, you must check the Create Pseudo MAC Address check box. You can update this information manually later. Skip to Step 8 . If you supplied MAC addresses or device names in the data input file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, then choose this option. When the phone is plugged
                                                         in, a MAC address registers for that device. |
| Step 6 | In the Job
                                             				Information area, enter the Job description. |
| Step 7 | Choose an insert
                                          			 method. Do one of the following: Click Run
                                                   					 Immediately to insert the phone records immediately. Click Run Later to insert the phone records later. |
| Step 8 | Click Submit to create a job for inserting the phone
                                          			 records. Use the Job Configuration window to schedule or activate this job. |

| Note | Leave the check boxes clear to append those records to the existing records in the CSV data file during the upload. |
|---|---|

| Attention | If you did not enter individual MAC addresses in the CSV data file, you must check the Create Pseudo MAC Address check box. You can update this information manually later. Skip to Step 8 . If you supplied MAC addresses or device names in the data input file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, then choose this option. When the phone is plugged
                                                         in, a MAC address registers for that device. |
|---|---|

| Step 1 | Create a comma separated values (CSV) data file to define
                                          			 individual values for each user that you want to add. |
|---|---|
| Step 2 | Use BAT to insert the users in the Unified Communications Manager database. |

| Note | If you enter a blank row in the BAT spreadsheet, the system treats
                                             			 the empty row as the end of the file and does not convert data that is entered
                                             			 after a blank line to the BAT format. |
|---|---|

| Note | You cannot upload a CSV filename that contains a comma (for example, abcd,e.txt) to the Unified Communications Manager server. |
|---|---|

| Step 1 | To open the BAT spreadsheet, locate and double-click BAT.xlt file. |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities. |
| Step 3 | To add users, click the Users tab at the bottom of the spreadsheet. |
| Step 4 | Complete all mandatory fields and any relevant optional fields.
                                          			 Each column heading specifies the length of the field and whether it is
                                          			 required or optional. In each row, provide the information as described in the online help files. If a user has multiple devices, the device name field should be repeated, once for each device. To enter additional device names that will be associated to a new user, enter a value in the Number of Controlled Devices text box. Note You can associate all devices, including CTI ports, ATA ports, and H.323 clients, with a user. | Note | You can associate all devices, including CTI ports, ATA ports, and H.323 clients, with a user. |
| Note | You can associate all devices, including CTI ports, ATA ports, and H.323 clients, with a user. |
| Step 5 | To enter additional device names that will be associated to a new
                                          			 user, enter a value in the Number of Controlled Devices text box. |
| Step 6 | Click Export to BAT Format to transfer the data from
                                          			 the BAT Excel spreadsheet into a CSV formatted data file. The system saves the file to C:\XLSDataFiles with the default file name <tabname>-<timestamp>.txt , or uses Browse to save the file to another existing folder. Tip For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Users window in BAT. | Tip | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Users window in BAT. |
| Tip | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Users window in BAT. |

| Note | You can associate all devices, including CTI ports, ATA ports, and H.323 clients, with a user. |
|---|---|

| Tip | For information on how to read the exported CSV data file, click
                                                         				  the link to View Sample File in the Insert
                                                            					 Users window in BAT. |
|---|---|

| Attention | If the credential policy has "check for trivial password" enabled, and the password in the
                                             			 user template is the user ID, inserting users through BAT may fail if the user
                                             			 ID does not satisfy the necessary criteria for the trivial password. |
|---|---|

| Note | When you are inserting users by using an exported BAT file, you
                                             			 might get errors stating "User ID already exists" for some users that were exported in
                                             			 more than one file. For example, a list of first line managers and a list of
                                             			 users might both include the same manager user ID. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Users > Insert
                                                				  Users . |
|---|---|
| Step 2 | In the File Name field, choose the CSV data file that you created for this
                                          			 bulk transaction. |
| Step 3 | If the CSV data file was created by using the export utility,
                                          			 check the File created with Export Users check box. |
| Step 4 | From the User Template Name drop-down list, choose the user template you want to use for this insert. Note The User Profile, Controlled Device Name, and Directory Number should exist in the Unified Communications Manager database. The controlled device name should be entered in full. If it contains only MAC Address, then BAT displays a non-existing
                                                         device error. | Note | The User Profile, Controlled Device Name, and Directory Number should exist in the Unified Communications Manager database. The controlled device name should be entered in full. If it contains only MAC Address, then BAT displays a non-existing
                                                         device error. |
| Note | The User Profile, Controlled Device Name, and Directory Number should exist in the Unified Communications Manager database. The controlled device name should be entered in full. If it contains only MAC Address, then BAT displays a non-existing
                                                         device error. |
| Step 5 | In the Job Information area, enter the Job
                                          			 description. |
| Step 6 | Choose an insert method. Do one of the following: Click Run Immediately to insert the user records
                                                				  immediately. Click Run Later to insert the user records at a
                                                				  later time. |
| Step 7 | To create a job for inserting the user records, click Submit . To schedule and / or activate this job, use the
                                          			 Job Scheduler option in the Bulk Administration main menu. |

| Note | The User Profile, Controlled Device Name, and Directory Number should exist in the Unified Communications Manager database. The controlled device name should be entered in full. If it contains only MAC Address, then BAT displays a non-existing
                                                         device error. |
|---|---|

| Step 1 | To open the BAT spreadsheet, locate and double-click BAT.xlt file. You can download a  BAT.xlt file. |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities. |
| Step 3 | At the bottom of the spreadsheet, click the Phones-Users tab. |
| Step 4 | Follow steps 4 through 10 in Create Phone CSV Data File Using BAT Spreadsheet . |

| Step 1 | Choose Bulk
                                                				  Administration > Phones and
                                                				  Users > Phones & Users File
                                                				  Format > Assign File Format . The Add File Format Configuration window displays. |
|---|---|
| Step 2 | In the File Name field, choose the text-based CSV
                                          			 file that you created for this transaction. |
| Step 3 | In the Format File Name field, choose the file format
                                          			 that you created for this type of bulk transaction. |
| Step 4 | To create a job for associating the matching file format with the
                                          			 CSV data file, click Submit . |
| Step 5 | To schedule and/or activate this job, use the Job Scheduler option
                                          			 in the Bulk Administration main menu. Note The user fields get added automatically when you add the file
                                                         				  format. | Note | The user fields get added automatically when you add the file
                                                         				  format. |
| Note | The user fields get added automatically when you add the file
                                                         				  format. |

| Note | The user fields get added automatically when you add the file
                                                         				  format. |
|---|---|

| Note | Phone records must be validated before insertion. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Phones &
                                                				  Users > Insert Phones with Users . |
|---|---|
| Step 2 | In the File Name field, choose the CSV data file that
                                          			 you created for this bulk transaction. |
| Step 3 | In the Phone Template Name field, choose the BAT
                                          			 phone template that you used for this transaction. Attention If you did not enter individual MAC addresses in the CSV data file, you must check the Create Pseudo MAC Address check box. You can update this information manually later. If you supplied MAC addresses or device names in the data input
                                                         file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, choose this option. When the phone is plugged
                                                         in, a MAC address registers for that device. | Attention | If you did not enter individual MAC addresses in the CSV data file, you must check the Create Pseudo MAC Address check box. You can update this information manually later. If you supplied MAC addresses or device names in the data input
                                                         file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, choose this option. When the phone is plugged
                                                         in, a MAC address registers for that device. |
| Attention | If you did not enter individual MAC addresses in the CSV data file, you must check the Create Pseudo MAC Address check box. You can update this information manually later. If you supplied MAC addresses or device names in the data input
                                                         file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, choose this option. When the phone is plugged
                                                         in, a MAC address registers for that device. |
| Step 4 | In the User Template Name field, choose the BAT user
                                          			 template that you used for this transaction |
| Step 5 | In the Job Information area, enter the Job description. |
| Step 6 | Choose an insert method. Do one of the following: Click Run Immediately to insert the phones with
                                                				  users immediately. Click Run Later to insert the phones with users
                                                				  at a later time. |
| Step 7 | To create a job for inserting the phones and user records, click Submit . To schedule and activate this job, use the Job Scheduler option
                                          			 in the Bulk Administration main menu. |

| Attention | If you did not enter individual MAC addresses in the CSV data file, you must check the Create Pseudo MAC Address check box. You can update this information manually later. If you supplied MAC addresses or device names in the data input
                                                         file, do not choose this option. If you do not know the MAC address of the phone that is assigned to the user, choose this option. When the phone is plugged
                                                         in, a MAC address registers for that device. |
|---|---|