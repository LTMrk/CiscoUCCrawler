---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-15-cucm-b-bulk-administration-guide-15-cucm-b-bulk-administration-g-7a0fc4ab44
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/15/cucm_b_bulk-administration-guide-15/cucm_b_bulk-administration-guide-1251su2_chapter_01.html
retrieved_at: 2026-08-21T09:16:06.921986+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: October 1, 2024

Chapter: Cisco Unified Communications Manager Bulk Administration Tool (BAT)

## Chapter: Cisco Unified Communications Manager Bulk Administration Tool (BAT)

# Cisco Unified Communications Manager Bulk Administration Tool (BAT)

This chapter provides information about the Cisco Unified Communications Manager Bulk Administration Tool (BAT).

## About Cisco Unified
                        	 Communications Manager Bulk Administration Tool

The Unified Communications Manager Bulk Administration Tool (BAT) is a web-based application that you can use to perform bulk transactions to the Unified Communications Manager database. You can use BAT to add, update, or delete a large number of similar phones, users, or ports at the same time. When
                              you use Unified Communications Manager Administration, each database transaction requires an individual manual operation, while BAT automates the process and achieves
                              faster add, update, and delete operations.

The Bulk Administration menu is visible only on the first node of Unified Communications Manager server.

Bulk Provision Service (BPS) administers and maintains all jobs that are submitted through Bulk Administration menu of Unified Communications Manager administration. You can start this service from Unified Communications Manager Serviceability.

The BPS Server service parameter determines whether the service is activated on a particular server. You need to activate
                              BPS only on the first node of Unified Communications Manager .

You can use
                              		  BAT to work with the following types of devices and records:

Add, update, and delete Cisco Unified IP Phones including voice gateway (VG) phones, computer telephony interface (CTI) ports,
                                    and H.323 clients, and migrate phones from Skinny Client Control Protocol (SCCP) to Session Initiation Protocol (SIP)

Add, update, and
                                    				delete users

Add, update, and
                                    				delete User Device Profiles

Add, update, and delete Unified Communications Manager Assistant and Managers associations

Add, update, and delete ports on a Cisco Catalyst 6000 FXS Analog Interface Module

Add or delete
                                    				Cisco VG200 and Cisco VG224 analog gateways and ports

Add or delete
                                    				Forced Authorization Codes

Add or delete
                                    				Client Matter Codes

Add or delete
                                    				Call Pickup Groups

Update or export
                                    				CUP/CUPC users

Populate or
                                    				depopulate the Region Matrix

Insert, delete,
                                    				or export the Access List

Export or import
                                    				configuration

Insert, delete,
                                    				or export Remote Destination and Remote Destination Profile

Add
                                    				Infrastructure Devices

When you perform a
                                          			 bulk transaction, limit the number of records to a maximum of 12,000 records.
                                          			 This applies when you insert, update, delete, or query any records using BAT.

You can also work with these devices in combination with the user information. For example, when you add CTI ports and users,
                              you can use BAT to "Enable CTI Application Use." This saves time when you add users who have applications that require a CTI port, such as Cisco IP SoftPhone.

An optional component of BAT, the Unified Communications Manager Auto-Register Phone Tool, further reduces the time and effort that is involved in administering a large system. To add a
                              large block of new phones, you can use BAT to add the devices with pseudo media access control (MAC) addresses instead of entering each MAC address in the data input file. After the phones are installed,
                              the phone users or the administrator can call the Unified CM Auto-Register phone Tool directory number, follow the voice prompts,
                              and download the correct user device profiles for their phones.

If you want to import or export the LDAP configurations using BAT, make sure that the LDAP server supports the minimum TLS
                                          version configured on Unified CM.

## BAT Installation

BAT is installed as part of the Unified Communications Manager Administration.

## BAT Data Input Files

Every device includes a multitude of individual attributes,
                              		  settings, and information fields that enable the device to function in the
                              		  network and provide its telephony features. Many devices have the same
                              		  attributes and settings in common, while other values, such as the directory
                              		  number, are unique to a user or to a device. To condense the BAT data input
                              		  file contents, BAT uses templates for settings that devices usually have in
                              		  common.

For bulk configuration transactions on the Unified Communications Manager database, the BAT process uses two components: a template for the device type and a data file in comma separated value (CSV)
                              format that contains the unique values for configuring a new device or updating an existing record in the database. The CSV
                              data file works in conjunction with the device template.

For instance, when you create a bulk transaction for a group
                              		  of CiscoIPPhones, you set up the CSV data file that contains the unique
                              		  information for each phone, such as the directory number and MAC address. In
                              		  addition, you set up or choose the BAT template that contains the common
                              		  settings for all phones in the transaction, such as a CiscoIPPhone7960
                              		  template.

## Perform BAT Configuration Multistep Process

BAT uses a multistep process to prepare the bulk
                              		  configuration transaction. BAT uses Bulk Administration menu options to guide
                              		  you through the configuration tasks. The BAT process includes these tasks:

Step 1

Set up the template for data input.

Step 2

Define a format for the CSV data file.

Step 3

Collect the data for each device in the bulk transaction.

Step 4

Upload the data files choosing the relevant target and function
                                       			 for the transaction.

Step 5

Validate the data input files with the Unified Communications Manager database.

Step 6

Submit jobs for execution.

Step 7

Schedule jobs.

Step 8

Execute jobs to insert the devices into the Unified Communications Manager database.

### About the BAT
                           	 Menu

From the Bulk
                                 		  Administration menu, you can choose one of these device or configuration
                                 		  options:

- Upload/Download Files

- Phones

- Users

- Phones and Users

- Manager/Assistants

- User Device Profiles

- Gateways

- Forced Authorization Codes

- Client Matter Codes

- Call Pickup Group

- Mobility

- Region Matrix

- Import/Export

- Phone Migration

- EMCC

- Intercompany Media Engine

- CUPS

- TAPS

- Infrastructure Devices

- Job Scheduler

When you
                                 		  choose an option, the corresponding menu items display. For example, when you
                                 		  choose phones, the following list of menu items displays:

- Validate Phones—Validate
                                    			 phones records.

- Insert Phones—Add new phones.

- Update Phones—Locate and
                                    			 modify existing phones.

- Delete Phones—Locate and
                                    			 delete phones.

- Export Phones—Locate and
                                    			 export specific phone records or all phone records.

- Add/Update Lines—Add new
                                    			 lines to existing phones, and locate and modify lines on existing phones.

- Reset/Restart Phones—Locate
                                    			 and reset or restart phones.

- Generate Phone
                                    			 Reports—Generate customized reports for phones.

- Migrate Phones—Migrate phones
                                    			 from SCCP to SIP.

When you
                                 		  choose a menu option from the Bulk Administration menu, the corresponding
                                 		  window opens, such as the phone Template Configuration window. The
                                 		  configuration window provides the entry fields for defining a template.

### BAT Configuration Templates

As the first task in the BAT configuration process, you set up a template for the devices that you are configuring. You specify
                                 the type of phone or device that you want to add or modify, and then you create a BAT template that has features that are
                                 common to all the phones or devices in that bulk transaction.

You can create BAT templates for the following types of device options:

Phones: All CiscoUnifiedIPPhones and Cisco ATA 186, Cisco VGC phones, CTI ports, and H.323 clients

Gateways: Cisco VG200 and Cisco Catalyst 6000 FXS Analog Interface Module

User Device Profiles: CiscoUnifiedIPPhone 7900 series and Cisco Softphone

Define a BAT template by specifying values in the template fields that will be common to all the devices in the bulk transaction.
                                 The BAT template fields require similar values to those that you enter when you are adding a device in Unified Communications Manager Administration.

Prior to creating the BAT template, make sure settings such as device pools, locations, calling search spaces, button templates,
                                 and softkey templates have already been configured in Unified Communications Manager Administration.

After you create a BAT template, you save it with a name. Later in the configuration process, you associate the template name
                                 with the CSV data file. The system stores the templates, so they are reusable for future bulk transactions. For example, you
                                 can configure a CiscoIPPhone7960 template with a specific button template and calling search space and then configure another
                                 CiscoIPPhone7960 template with a different button template and the Extension Mobility feature enabled. When you need to add
                                 a large number of phones with the same configuration, you can reuse the existing BAT template.

### Standard Phone Templates

When you are adding a group of phones that have multiple lines, you can create a standard phone template that provides multiple
                                 lines and the most common values for a specific phone model. You can use the standard template to add phones that have differing
                                 number of lines, but do not exceed the number of lines in the master phone template. For example, you can create a standard
                                 phone template for a CiscoUnifiedIPPhone 7960 that has eight lines. You can use this template to add phones that have one
                                 line, two lines, or up to eight lines.

### CSV Data File Overrides Template Values

The CSV data file contains the unique settings and
                                 		  information for each individual device, such as its directory number, MAC
                                 		  address, and description. Make sure that all phones and devices in a CSV data
                                 		  file are the same phone or device model and match the BAT template. The CSV
                                 		  data file can contain duplicates of some values from the BAT template. Values
                                 		  in the CSV data file override any values that were set in the BAT template. You
                                 		  can use the override feature for special configuration cases.

#### Example Template Override

The CSV data file for phones can contain multiple directory numbers. Keep in mind that the number of directory numbers that
                                    are entered in the CSV data file must not exceed—but can be less than— the number of lines that are configured in the BAT
                                    phone template, or an error will result.

If you want most of the phones in the bulk transaction to be redirected to a voice-messaging system, you can set the Call
                                    Forward Busy (Internal/External) (CFB) and Call Forward No Answer (Internal/External) (CFNA) fields to the voice-messaging
                                    number. However, if a few phones in the bulk transaction need to be redirected to a secretary instead of to a voice messaging
                                    system, you can specify the secretary directory number in the Call CFB and CFNA fields in the CSV data file. Most of the phones
                                    will use the CFB and CFNA values from the BAT phone template, but certain phones will use the secretary directory number as
                                    specified in the CSV data file.

#### CSV Data File Adds New Devices

Data file templates with macros for the different devices

Customized file format definition

Support for multiple phone lines

Record error checking

File conversion to CSV format

When you are creating new records, use the BAT spreadsheet,
                                    		  which is named BAT.xlt, because the data gets validated automatically when you
                                    		  export to the CSV format.

BAT.xlt validates data only for valid characters, data types, and
                                                			 field length for particular fields.

For experienced BAT users who are comfortable with working
                                    		  in a CSV formatted file, you can use a text editor to create a CSV data file by
                                    		  following the sample text file that is provided on the device insert task
                                    		  window.

#### CSV Data File Updates Existing Devices

To modify or update existing phones and devices, you need to
                                    		  locate the records for these devices. BAT provides two methods for locating
                                    		  phones, gateways, and device profiles. You can search by using a customized
                                    		  query or by using a custom file.

You can also extract a group of phone records from the Unified Communications Manager database for inclusion in a CSV data file using the export utility.

##### Customized Query
                                 	 Searches

BAT
                                       		  provides a window for defining your query criteria. You can choose the specific
                                       		  device model and/or choose criteria from a list of device details and a list of
                                       		  line details. To locate all devices of a specific device model, you choose the
                                       		  model but add no other criteria for the search. You get the records for all the
                                       		  Cisco Unified IP Phones that are configured in the database.

##### Custom File Searches

When no common attribute to use for a query exists, BAT provides the custom file option. A custom file includes device names
                                       or directory numbers. You can build a custom text file by putting each record on a separate line. The search gives you all
                                       the records that match the criteria.

##### Export Phone Records to CSV Data File

When you need to move a group of phones, you can use the export utility. You use the export utility to extract existing records
                                       from the Unified Communications Manager database to move them into a CSV data file. When you move phones, use the option, Export Phones with the All Phone Details.
                                       This option generates an export file that contains records with all the information, including the device attributes, line
                                       attributes, and services, that is associated with that phone. You can also export phone records with specific details when
                                       phones have similar line configurations and you want to use a template.

#### CSV Data File and Custom File Formats

Default format—CSV files that have a fixed and limited number of attributes and settings for each device.

All details format—CSV files that are created by using the export utility and include all attributes and settings for each
                                             device.

The first row of every CSV data file shows the file format
                                    		  by displaying the name of each field that the CSV file includes. The file
                                    		  format information makes it easier to locate the entry for a specific field in
                                    		  the CSV data file. For instance, in the following sample CSV file, USER ID
                                    		  represents the fourth field in the header, and the fifth field in the CSV file
                                    		  for the phone shows "johns."

##### Sample CSV Data File with the Default File Format

```
MAC ADDRESS,DESCRIPTION,LOCATION,USER ID,DIRECTORY NUMBER 1,DISPLAY 1,LINE TEXT LABEL 1,FORWARD BUSY EXTERNAL 1,FORWARD NO ANSWER EXTERNAL 1,FORWARD NO COVERAGE EXTERNAL 1,FORWARD BUSY INTERNAL 1,FORWARD NO ANSWER INTERNAL 1,FORWARD NO COVERAGE INTERNAL 1,CALL PICKUP GROUP 1,SPEED DIAL NUMBER 1,SPEED DIAL LABEL 1,
1231123245AB,SEP1231123245AB,Dallas,Johns,9728437154,9728437154,Mike,9728437172,9728437196,
9728437127,9728437154,9728437178,9728437189,9728437121/TollByPass,1230000000,Helpdesk,
9728437127,9728437154,9728437178,9728437189,Marketing,1230000000,Helpdesk
```

Now, you can customize the file format for the CSV data file
                                    		  by using the Create Phone File Format Configuration window. You can add
                                    		  attributes to your file format that are also in the BAT template. This allows
                                    		  you to override the template entry with a specific attribute for a device. For
                                    		  instance, you can choose the route partition attribute for your file format and
                                    		  enter different partitions for each phone in the CSV data file.

From this window, you can choose specific attributes from
                                    		  Device fields and Line fields

MAC Address

Description

The File Format Configuration dialog box makes it easy to
                                    		  choose the device attribute in the Device Field box and click an arrow to move
                                    		  the attribute into the Selected Device Field box. You can select multiple
                                    		  attributes at the same time by holding down the Ctrl key.

You can rearrange the order of the device attribute fields
                                    		  and line attribute fields in the file format by using the Up and Down arrows.
                                    		  You can select an attribute and then click the Up arrow to move the item closer
                                    		  to the first record or click the down arrow to move the item further away from
                                    		  the first record. You cannot move line attributes before device attributes or
                                    		  change the order of speed dials.

Tip

You can customize a CSV file format, so it matches the arrangement of your employee phone information that is stored in another
                                                database. This method simplifies exporting data between a company database and the Unified Communications Manager database.

##### Sample CSV Data File with the Customized File Format

Device fields—MAC Address, Description, Device Pool, Calling
                                    		  Search Space

Line fields—Directory number, Partition, Line Text Label
                                    		  (moved to position after directory number in file)

The File Format does not include speed-dial codes. Choose
                                    		  speed-dials by selecting the Include Speed Dials in the CSV Format check box.

```
MAC ADDRESS,DESCRIPTION,DEVICE POOL,CSS,DIRECTORY NUMBER,LINE TEXT LABEL,
PARTITION,2234900AEF01,SEP2234900AEF01,DP_1,CSS_Restricted,
9725098827,LobbyPhone,Part1
```

##### Associate Custom File Format with CSV Data File

When you are using a text editor to create a CSV data file,
                                       		  you can create a customized file format and then enter values in the same order
                                       		  as specified by that file format. Before inserting the text-based CSV data file
                                       		  that uses the customized file format, you must associate the file format name
                                       		  with the CSV data file. You can associate only one file format with a CSV data
                                       		  file.

Step 1

In the Add File Format window, choose the
                                                			 name of the CSV data file <CSVfilename>.txt from the File Name drop-down list.

Step 2

Choose a file format from the File Format Name drop-down list.

### BAT Spreadsheet Data Collection for CSV Data File Creation

The BAT spreadsheet simplifies the creation of CSV data
                                 		  files. You can add multiple devices and view the records for each device in a
                                 		  spreadsheet format. It allows you to customize the file format within the
                                 		  spreadsheet and provides validation and error checking automatically to help
                                 		  reduce configuration errors. The BAT spreadsheet includes tabs along the bottom
                                 		  of the spreadsheet for access to the required data input fields for the various
                                 		  devices and user combinations in BAT.

BAT.xlt validates data only for valid characters, data types, and
                                             			 field length for particular fields.

The CSV data file works in combination with the BAT
                                 		  template. For example, when you choose the Phone tab in the BAT spreadsheet,
                                 		  you can leave Location, Forward Busy Destination, or Call Pickup Group blank.
                                 		  The values from the BAT phone template get used for these fields; however, if
                                 		  you specify values for Forward Busy Destination or Call Pickup Group, those
                                 		  values override the values for these fields that were set in the BAT phone
                                 		  template.

Tip

When Unified Communications Manager is installed, the Microsoft Excel file for the BAT spreadsheet gets placed on the first node database server; however, you
                                             probably do not have Microsoft Excel running on the first node database server. You must download the file from the first
                                             node database server to the local machine on which you plan to work.

Download the file BAT.xlt file to a local machine where Microsoft Excel is
                                 		  installed. 
                                 		To use the BAT.xlt spreadsheet to create a CSV data file,
                                 		  locate and double-click the BAT.xlt file. You must choose to "enable macros" when you open the BAT spreadsheet.

Most of the times when you download the BAT.xlt file to a local Windows machine, you will see a blocked content warning: "Macros
                                             in this document have been disabled by your enterprise administrator for security reasons." To solve this issue, download
                                             your BAT.xlt files in 97-2003 format (.xls instead of the new .xlsx format). Use this (*.xls) format to create BAT spreadsheets.

BAT.xlt files functions work best on a Windows machine and not on a Mac OS machine. We recommend you to use BAT.xlt files
                                             on a Windows machine.

The spreadsheet displays a set of columns with attribute
                                 		  headings that specify the BAT field names, whether the field is a required or
                                 		  optional, and the maximum number of characters that are allowed in the field.

Tabs for every device display along the bottom of the
                                 		  spreadsheet. When you click the tab for the type of device with which you want
                                 		  to work, the columns adjust to display all relevant fields for the chosen
                                 		  device. For example, to add phones and users all at once, click the tab that is
                                 		  marked Phones-Users.

Tip

If the "enable macros" option does not display while you are opening
                                             			 the spreadsheet, a possibility exists that macro security on the Excel program
                                             			 is set to high. Ensure that Macro security is medium or low for the macros to
                                             			 run. To set the Macro security to medium, do the following task: choose Tools > Macro > Security from Excel menu. Set the security level to medium. Close the Excel program and
                                             			 open it again. This action should give you the "enable macros" option when you open the spreadsheet the next
                                             			 time.

Next, define the file format for the CSV data file by clicking the Create File Format button. You can use the Field Selection dialog box to choose items and their order in your CSV data file. When you click Create , the columns in the spreadsheet adjust to your new file format.

In the first row, enter data for a device in all mandatory
                                 		  fields and any relevant optional fields. You enter data in a new row for each
                                 		  device.

The system treats blank rows in the spreadsheet as "end of file" markers and discards subsequent records.

After all device records are completed, you export the BAT spreadsheet data to the CSV file format that BAT must use to perform
                                 the bulk transaction with the Unified Communications Manager first node database.

If you enter a comma in one of the fields, BAT.xlt encloses that
                                             			 field entry in double quotes when you export to BAT format.

The system saves the CSV formatted file as a text file to the folder that you choose. The filename format follows:

<tabname><timestamp>.txt

where <tabname> represents the type of device input
                                 		  file that you created (such as phones, user device profiles), and
                                 		  <timestamp> represents the precise date and time that the file was
                                 		  created.

Next, you must upload the converted CSV data file (CSV format version) back to the Unified Communications Manager database server by using Upload/Download Files option in the Bulk Administration of Unified Communications Manager Administration.

### Validate BAT Data Input File

The system runs a validation routine to check for errors in the CSV data file and the BAT template against the first node
                                 database. These checks include the following items:

Fields, such as description, display text, and speed-dial label that do not have a dependency on a database table, use valid
                                       characters.

BAT Validate transaction only validates data type, length and relational dependency.

Consider the following example:

MAC ADDRESS,DESCRIPTION,PARTITION

AABBCC112233,Lab Phone,Dallas

If the Partition does not exist, Validate displays an error saying "Dallas is not an existing PARTITION."

Number of lines that are configured on a device matches the device template. (Only for Specific Details)

Validation does not check for the existence of a user or for mandatory/optional fields that are BAT defined, such as the pseudo MAC address.

Step 1

Select the Validate File option and choose the name of
                                          			 the CSV data input file, the BAT template for the device, and the model, if
                                          			 applicable.

Step 2

Select the validation method.

Choose Specific Details for validating records that
                                                				  follow the Default or Custom file format.

Choose All Details for validating records from a file
                                                				  that was generated from the export utility using the All Details option.

### Insert BAT Data Input File Records Into Database

When the data input file has passed validation, you are ready to use the Insert window to add the device records into the Unified Communications Manager first node database.

#### Before you begin

The CSV data input file must be valid. If any line information for a
                                 		  phone record fails, BAT does not insert that phone record.

Step 1

In the Insert window choose the name of the CSV data
                                          			 input file, the BAT template for the device, and the model, if applicable.

Step 2

Select the insert method.

Choose Specific Details to insert records that use a
                                                				  customized file format.

Choose All Details to insert records from a file that
                                                				  was generated from the export utility using the All Details option.

Step 3

Enter Job Information details and click Submit .

If any line information for a phone record fails, BAT does not
                                                         				  insert that phone record.

## BAT Application Web Browser Considerations

The BAT is a web-based application that requires the use of a web browser. A web browser is a resource-intensive application
                              that can consume large amounts of system memory and CPU cycles. When a web browser takes resources away from Unified Communications Manager , it adversely affects call processing.

Caution

## Access BAT Online Help

Online help provides a multivolume system that allows you to
                              		  access several different help systems, all from the same window. You can also
                              		  access a comprehensive search engine and index.

Step 1

Select the Help menu to access BAT online help.

Step 2

Choose a help feature.

Choose Contents and Index to open the BAT help file that you
                                             				  can browse for information or search the index.

Choose For This Page to open the help
                                             				  directly for the window that you are currently viewing.

## Verify Cisco Unified Communications Manager Version

Select Help > About to find the current version of Unified Communications Manager

| Note | The Bulk Administration menu is visible only on the first node of Unified Communications Manager server. |
|---|---|

| Note | When you perform a
                                          			 bulk transaction, limit the number of records to a maximum of 12,000 records.
                                          			 This applies when you insert, update, delete, or query any records using BAT. |
|---|---|

| Note | If you want to import or export the LDAP configurations using BAT, make sure that the LDAP server supports the minimum TLS
                                          version configured on Unified CM. |
|---|---|

| Step 1 | Set up the template for data input. |
|---|---|
| Step 2 | Define a format for the CSV data file. |
| Step 3 | Collect the data for each device in the bulk transaction. |
| Step 4 | Upload the data files choosing the relevant target and function
                                       			 for the transaction. |
| Step 5 | Validate the data input files with the Unified Communications Manager database. |
| Step 6 | Submit jobs for execution. |
| Step 7 | Schedule jobs. |
| Step 8 | Execute jobs to insert the devices into the Unified Communications Manager database. Note To blank out a field, type "NULL" (without quotations) in the field. Do not leave the field blank. | Note | To blank out a field, type "NULL" (without quotations) in the field. Do not leave the field blank. |
| Note | To blank out a field, type "NULL" (without quotations) in the field. Do not leave the field blank. |

| Note | To blank out a field, type "NULL" (without quotations) in the field. Do not leave the field blank. |
|---|---|

| Note | BAT.xlt validates data only for valid characters, data types, and
                                                			 field length for particular fields. |
|---|---|

| Note | To blank out a field, type "NULL" (without quotations) in the field. Do not leave the field blank. |
|---|---|

| Tip | You can customize a CSV file format, so it matches the arrangement of your employee phone information that is stored in another
                                                database. This method simplifies exporting data between a company database and the Unified Communications Manager database. |
|---|---|

| Step 1 | In the Add File Format window, choose the
                                                			 name of the CSV data file <CSVfilename>.txt from the File Name drop-down list. |
|---|---|
| Step 2 | Choose a file format from the File Format Name drop-down list. The data in the CSV data file must match the custom file format
                                                			 that is chosen. |

| Note | BAT.xlt validates data only for valid characters, data types, and
                                             			 field length for particular fields. |
|---|---|

| Tip | When Unified Communications Manager is installed, the Microsoft Excel file for the BAT spreadsheet gets placed on the first node database server; however, you
                                             probably do not have Microsoft Excel running on the first node database server. You must download the file from the first
                                             node database server to the local machine on which you plan to work. |
|---|---|

| Note | Most of the times when you download the BAT.xlt file to a local Windows machine, you will see a blocked content warning: "Macros
                                             in this document have been disabled by your enterprise administrator for security reasons." To solve this issue, download
                                             your BAT.xlt files in 97-2003 format (.xls instead of the new .xlsx format). Use this (*.xls) format to create BAT spreadsheets. BAT.xlt files functions work best on a Windows machine and not on a Mac OS machine. We recommend you to use BAT.xlt files
                                             on a Windows machine. |
|---|---|

| Tip | If the "enable macros" option does not display while you are opening
                                             			 the spreadsheet, a possibility exists that macro security on the Excel program
                                             			 is set to high. Ensure that Macro security is medium or low for the macros to
                                             			 run. To set the Macro security to medium, do the following task: choose Tools > Macro > Security from Excel menu. Set the security level to medium. Close the Excel program and
                                             			 open it again. This action should give you the "enable macros" option when you open the spreadsheet the next
                                             			 time. |
|---|---|

| Note | The system treats blank rows in the spreadsheet as "end of file" markers and discards subsequent records. |
|---|---|

| Note | If you enter a comma in one of the fields, BAT.xlt encloses that
                                             			 field entry in double quotes when you export to BAT format. |
|---|---|

| Step 1 | Select the Validate File option and choose the name of
                                          			 the CSV data input file, the BAT template for the device, and the model, if
                                          			 applicable. The CSV data file should contain all details. |
|---|---|
| Step 2 | Select the validation method. Choose Specific Details for validating records that
                                                				  follow the Default or Custom file format. Choose All Details for validating records from a file
                                                				  that was generated from the export utility using the All Details option. |

| Step 1 | In the Insert window choose the name of the CSV data
                                          			 input file, the BAT template for the device, and the model, if applicable. The CSV data file should contain all details and be valid. |
|---|---|
| Step 2 | Select the insert method. Choose Specific Details to insert records that use a
                                                				  customized file format. Choose All Details to insert records from a file that
                                                				  was generated from the export utility using the All Details option. |
| Step 3 | Enter Job Information details and click Submit . This creates a job that can be accessed using the Job Scheduler option in the Bulk
                                             				Administration menu. Use the Job Configuration window to view the status and
                                          			 to schedule and activate the job. Note If any line information for a phone record fails, BAT does not
                                                         				  insert that phone record. | Note | If any line information for a phone record fails, BAT does not
                                                         				  insert that phone record. |
| Note | If any line information for a phone record fails, BAT does not
                                                         				  insert that phone record. |

| Note | If any line information for a phone record fails, BAT does not
                                                         				  insert that phone record. |
|---|---|

| Caution | Possible consequences of using the browser on the same machine as the web server and Unified Communications Manager include delayed dial tone and dropped calls. |
|---|---|

| Step 1 | Select the Help menu to access BAT online help. |
|---|---|
| Step 2 | Choose a help feature. Choose Contents and Index to open the BAT help file that you
                                             				  can browse for information or search the index. Choose For This Page to open the help
                                             				  directly for the window that you are currently viewing. You can still browse the remainder of the help or use the
                                             				  index. |

| Select Help > About to find the current version of Unified Communications Manager |
|---|