---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-su6-cucm-b-bulk-administration-guide-1251su6-cucm-b-bulk-admin-4b39ddf953
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_SU6/cucm_b_bulk-administration-guide-1251su6/cucm_b_bulk-administration-guide-1251su2_chapter_01111.html
retrieved_at: 2026-08-21T08:54:39.640197+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: February 15, 2022

Chapter: User Additions

## Chapter: User Additions

# User Additions

This chapter describes how to manage user records and work with
                        		user combinations, such as phones and users or CTI ports and user records in
                        		the Cisco Unified Communications Manager LDAP database.

## New User Group Additions and User Associations

You can use Unified Communications Manager Bulk Administration (BAT) to add a group of new users and to associate users to phones and other IP Telephony devices in
                              the Unified Communications Manager database.

If you use your corporate directory and have Lightweight Directory Access Protocol (LDAP) synchronization enabled (in Cisco Unified Communications Manager Administration, choose System > LDAP > LDAP System ), then you cannot use BAT to reset passwords, and insert/update or delete users.

## Add Users

You must create a CSV data file to add new users in bulk to the Unified Communications Manager database using the BAT spreadsheet. For users who have applications that require a CTI port, such as CiscoIPSoftPhone, BAT
                              can associate CTI ports to existing users.

Create a comma separated values (CSV) data file to define
                                       			 individual values for each user that you want to add.

Use BAT to insert the users in the Unified Communications Manager database.

## Create User CSV Data File From BAT Spreadsheet

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

To open the BAT spreadsheet, locate and double-click BAT.xlt file.

When prompted, click Enable Macros to use the spreadsheet
                                       			 capabilities.

To add users, click the Users tab at the bottom of the spreadsheet.

Complete all mandatory fields and any relevant optional fields.
                                       			 Each column heading specifies the length of the field and whether it is
                                       			 required or optional.

- If a user has multiple devices, the device name field should be repeated, once for each device.

- To enter additional device names that will be associated to a new user, enter a value in the Number of Controlled Devices text box.

You can associate all devices, including CTI ports, ATA ports, and H.323 clients, with a user.

To enter additional device names that will be associated to a new
                                       			 user, enter a value in the Number of Controlled Devices text box.

Click Export to BAT Format to transfer the data from
                                       			 the BAT Excel spreadsheet into a CSV formatted data file.

The system saves the file to C:\XLSDataFiles with the default file name <tabname>-<timestamp>.txt , or uses Browse to save the file to another existing folder.

For information on how to read the exported CSV data file, click
                                                      				  the link to View Sample File in the Insert
                                                         					 Users window in BAT.

### What to do next

You must upload the CSV data file to the first node of Unified Communications Manager database server so that BAT can access the data file.

## BAT Spreadsheet User Data Field Descriptions

The following table provides the field descriptions for
                              		  adding users details.

Field

Description

First Name

Enter the first name, up to 64 characters, of the phone user.

Middle Name

Enter the middle name, up to 64 characters, of the phone user.

Last Name

Enter the last name, from 1 to 64 characters, of the phone
                                          					 user.

User ID

Enter the last name, from 1 to 128 characters, of the phone
                                          					 user.

Password

Enter the password, up to 128 characters, that the user needs
                                          					 to access the CiscoIPPhone Configuration window.

You must specify the Password either in the CSV data file or by using the BAT user interface during the user template addition.
                                          If you want to apply individual passwords for each user or groups of users, specify the password information in the CSV data
                                          file. If you want to use a default password for all users, provide the default password when you insert the users in BAT.

Manager User ID

Enter manager user ID, up to 128 characters, for the user of
                                          					 this phone.

Department

Enter the department number, up to 64 characters, for the user
                                          					 of this phone.

PIN

Enter the personal identification number (PIN), up to 128
                                          					 numerals, to be used for extension mobility.

You must enter a PIN either in the CSV data file or by using the BAT user interface during the user template addition. If
                                          you want to apply individual PINs for each user or groups of users, specify the PIN in the CSV data file. To use a default
                                          PIN that all users can use, provide default PIN when you insert the users in BAT.

Default Profile

Enter the default profile for this user and device, up to 50 characters. You can choose the user device profile from the list
                                          of existing UDPs in Cisco Unified Communications Manager Administration that appears in BAT.

User Locale

Enter the language and country set, up to 50 characters, that you want to associate with this user. Your choice determines
                                          which cultural-dependent attributes exist for this user and which language displays in the Unified Communications Manager user windows and phones.

Controlled Device 1

Enter the name, up to 50 characters, for the phone or device
                                          					 that you want to associate with this user.

The Controlled Device field(s)
                                                      						displays when the Number of Controlled Devices field, at
                                                      						the extreme right in the spreadsheet, is set to greater than Zero.

Telephone Number

Enter the telephone number, up to 64 numerals for the primary
                                          					 extension (usually Line 1) for the phone.

Primary Extension

This field displays after the user is added and represents the
                                          					 primary database number for the user. You choose no primary line when you
                                          					 associate devices to the user. Users can have multiple lines on their phones.

Associated PC

This field, which is required for Cisco SoftPhone and Cisco Unified Communications Manager Attendant Console users, displays after the user is added.

IPCC Extension

From the drop-down list box, choose an IPCC extension for this user.

Mail ID

Enter the user e-mail address up to 255 characters.

Controlled Device 2

Enter the name, up to 50 characters, for any additional phones
                                          					 that you want to associate with this user.

The Controlled Device field(s)
                                                      						displays when the Number of Controlled Devices field, at
                                                      						the extreme right in the spreadsheet, is set to greater than zero.

Presence Group

Enter the presence group that watches the status of the
                                          					 database number, the presence entity.

SUBSCRIBE Calling Search Space

All calling search spaces that you configure in Cisco Unified Communications Manager Administration display in the SUBSCRIBE Calling Search Space drop-down list box.

The SUBSCRIBE Calling Search Space determines how Cisco Unified Communications Manager routes the Presence subscription requests that come from the user. To configure a calling search space specifically for this
                                          purpose, you configure a calling search space as you do all calling search spaces ( Call Routing > Class Control > Calling Search Space ).

Digest Credentials

When you configure digest authentication for phones that are running SIP, Cisco Unified Communications Manager challenges the identity of the phone every time the phone sends a SIP request to Cisco Unified Communications Manager . The digest credentials that you enter in this field get associated with the phone when you choose a digest user in the Phone Configuration window.

Enter a string of up to 128 alphanumeric characters.

For more information on digest authentication, refer to the Cisco Unified Communications Manager Security Guide Security Guide .

User Group

Enter the user group to which the user belongs.

The User Group field(s) displays when the Number of User Groups field, at the
                                                      						extreme right in the spreadsheet, is set to greater than zero.

Directory URI

Enter the primary directory URI that you want to associate to this user’s primary extension. Follow the username@host format.
                                          Enter a username of up to 47 alphanumeric characters. For the host address, enter an IPv4 address or fully qualified domain
                                          name.

Within Cisco Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when
                                                      you use Bulk Administration to import a csv file that contains directory URIs with embedded double quotes and commas, you
                                                      must use enclose the entire directory URI in double quotes and escape the embedded double quotes with a double quote. For
                                                      example, the Jared, "Jerry",Smith@test.com directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the csv file.

Self-Service User ID

The Self-Service User ID is a DTMF digit string that is  used to identify a
                                          user (usually same as the user directory number).

User Profile

The User Profile is a profile that collects settings to share across a group of users. This profile is used when you create
                                          new devices.

EM MAX LOGIN TIME

Enter the maximum login time for Extension Mobility and Extension Mobility Cross Cluster users. Enter the value in minutes.
                                          The range of the value is from 0 to 10080 minutes (7 days).

## Topics Related to User Additions

| Note | If you use your corporate directory and have Lightweight Directory Access Protocol (LDAP) synchronization enabled (in Cisco Unified Communications Manager Administration, choose System > LDAP > LDAP System ), then you cannot use BAT to reset passwords, and insert/update or delete users. |
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

| Field | Description |
|---|---|
| First Name | Enter the first name, up to 64 characters, of the phone user. |
| Middle Name | Enter the middle name, up to 64 characters, of the phone user. |
| Last Name | Enter the last name, from 1 to 64 characters, of the phone
                                          					 user. |
| User ID | Enter the last name, from 1 to 128 characters, of the phone
                                          					 user. |
| Password | Enter the password, up to 128 characters, that the user needs
                                          					 to access the CiscoIPPhone Configuration window. You must specify the Password either in the CSV data file or by using the BAT user interface during the user template addition.
                                          If you want to apply individual passwords for each user or groups of users, specify the password information in the CSV data
                                          file. If you want to use a default password for all users, provide the default password when you insert the users in BAT. |
| Manager User ID | Enter manager user ID, up to 128 characters, for the user of
                                          					 this phone. |
| Department | Enter the department number, up to 64 characters, for the user
                                          					 of this phone. |
| PIN | Enter the personal identification number (PIN), up to 128
                                          					 numerals, to be used for extension mobility. You must enter a PIN either in the CSV data file or by using the BAT user interface during the user template addition. If
                                          you want to apply individual PINs for each user or groups of users, specify the PIN in the CSV data file. To use a default
                                          PIN that all users can use, provide default PIN when you insert the users in BAT. |
| Default Profile | Enter the default profile for this user and device, up to 50 characters. You can choose the user device profile from the list
                                          of existing UDPs in Cisco Unified Communications Manager Administration that appears in BAT. |
| User Locale | Enter the language and country set, up to 50 characters, that you want to associate with this user. Your choice determines
                                          which cultural-dependent attributes exist for this user and which language displays in the Unified Communications Manager user windows and phones. |
| Controlled Device 1 | Enter the name, up to 50 characters, for the phone or device
                                          					 that you want to associate with this user. Note The Controlled Device field(s)
                                                      						displays when the Number of Controlled Devices field, at
                                                      						the extreme right in the spreadsheet, is set to greater than Zero. | Note | The Controlled Device field(s)
                                                      						displays when the Number of Controlled Devices field, at
                                                      						the extreme right in the spreadsheet, is set to greater than Zero. |
| Note | The Controlled Device field(s)
                                                      						displays when the Number of Controlled Devices field, at
                                                      						the extreme right in the spreadsheet, is set to greater than Zero. |
| Telephone Number | Enter the telephone number, up to 64 numerals for the primary
                                          					 extension (usually Line 1) for the phone. |
| Primary Extension | This field displays after the user is added and represents the
                                          					 primary database number for the user. You choose no primary line when you
                                          					 associate devices to the user. Users can have multiple lines on their phones. |
| Associated PC | This field, which is required for Cisco SoftPhone and Cisco Unified Communications Manager Attendant Console users, displays after the user is added. |
| IPCC Extension | From the drop-down list box, choose an IPCC extension for this user. |
| Mail ID | Enter the user e-mail address up to 255 characters. |
| Controlled Device 2 | Enter the name, up to 50 characters, for any additional phones
                                          					 that you want to associate with this user. Note The Controlled Device field(s)
                                                      						displays when the Number of Controlled Devices field, at
                                                      						the extreme right in the spreadsheet, is set to greater than zero. | Note | The Controlled Device field(s)
                                                      						displays when the Number of Controlled Devices field, at
                                                      						the extreme right in the spreadsheet, is set to greater than zero. |
| Note | The Controlled Device field(s)
                                                      						displays when the Number of Controlled Devices field, at
                                                      						the extreme right in the spreadsheet, is set to greater than zero. |
| Presence Group | Enter the presence group that watches the status of the
                                          					 database number, the presence entity. |
| SUBSCRIBE Calling Search Space | All calling search spaces that you configure in Cisco Unified Communications Manager Administration display in the SUBSCRIBE Calling Search Space drop-down list box. The SUBSCRIBE Calling Search Space determines how Cisco Unified Communications Manager routes the Presence subscription requests that come from the user. To configure a calling search space specifically for this
                                          purpose, you configure a calling search space as you do all calling search spaces ( Call Routing > Class Control > Calling Search Space ). |
| Digest Credentials | When you configure digest authentication for phones that are running SIP, Cisco Unified Communications Manager challenges the identity of the phone every time the phone sends a SIP request to Cisco Unified Communications Manager . The digest credentials that you enter in this field get associated with the phone when you choose a digest user in the Phone Configuration window. Enter a string of up to 128 alphanumeric characters. For more information on digest authentication, refer to the Cisco Unified Communications Manager Security Guide Security Guide . |
| User Group | Enter the user group to which the user belongs. Note The User Group field(s) displays when the Number of User Groups field, at the
                                                      						extreme right in the spreadsheet, is set to greater than zero. | Note | The User Group field(s) displays when the Number of User Groups field, at the
                                                      						extreme right in the spreadsheet, is set to greater than zero. |
| Note | The User Group field(s) displays when the Number of User Groups field, at the
                                                      						extreme right in the spreadsheet, is set to greater than zero. |
| Directory URI | Enter the primary directory URI that you want to associate to this user’s primary extension. Follow the username@host format.
                                          Enter a username of up to 47 alphanumeric characters. For the host address, enter an IPv4 address or fully qualified domain
                                          name. Note Within Cisco Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when
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
| Self-Service User ID | The Self-Service User ID is a DTMF digit string that is  used to identify a
                                          user (usually same as the user directory number). |
| User Profile | The User Profile is a profile that collects settings to share across a group of users. This profile is used when you create
                                          new devices. |
| EM MAX LOGIN TIME | Enter the maximum login time for Extension Mobility and Extension Mobility Cross Cluster users. Enter the value in minutes.
                                          The range of the value is from 0 to 10080 minutes (7 days). |

| Note | The Controlled Device field(s)
                                                      						displays when the Number of Controlled Devices field, at
                                                      						the extreme right in the spreadsheet, is set to greater than Zero. |
|---|---|

| Note | The Controlled Device field(s)
                                                      						displays when the Number of Controlled Devices field, at
                                                      						the extreme right in the spreadsheet, is set to greater than zero. |
|---|---|

| Note | The User Group field(s) displays when the Number of User Groups field, at the
                                                      						extreme right in the spreadsheet, is set to greater than zero. |
|---|---|

| Note | Within Cisco Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when
                                                      you use Bulk Administration to import a csv file that contains directory URIs with embedded double quotes and commas, you
                                                      must use enclose the entire directory URI in double quotes and escape the embedded double quotes with a double quote. For
                                                      example, the Jared, "Jerry",Smith@test.com directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the csv file. |
|---|---|