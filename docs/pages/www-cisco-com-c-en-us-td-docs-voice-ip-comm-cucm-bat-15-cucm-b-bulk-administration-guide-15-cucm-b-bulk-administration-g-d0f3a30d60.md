---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-15-cucm-b-bulk-administration-guide-15-cucm-b-bulk-administration-g-d0f3a30d60
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/15/cucm_b_bulk-administration-guide-15/cucm_b_bulk-administration-guide-1251su2_appendix_01010001.html
retrieved_at: 2026-08-21T09:21:49.042262+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: October 1, 2024

Chapter: Text-Based CSV
	 Files

## Chapter: Text-Based CSV
	 Files

# Text-Based CSV
                     	 Files

Unified Communications Manager Bulk Administration (BAT) uses data that is entered in a comma-separated values (CSV) file
                           format to provide information for insert transactions to the Unified Communications Manager database on the first node server.
                           By using the CSV data format, you can build a textual file that contains data records in a tabular format.

You can
                           		  create a CSV data file by using a text editor, such as Notepad++.
                           		
                           		  You must use a separate line to enter data for each record. Separate each data
                           		  field with a comma and include comma separators for blank fields. Enter data on
                           		  every line in the data file because an error occurs during the insert
                           		  transaction if you enter a blank line in a CSV file.

When you insert the data records to the Unified Communications Manager database, BAT accesses a set of designated folders
                           that reside on the server that is running the first node database. For BAT to access the appropriate CSV data file for the
                           transaction, you must upload the CSV data file to the first node database server of Unified Communications Manager.

## Create Text-Based
                        	 CSV File for Phones

You can create a CSV
                              		  text file for phones, IP telephony devices, and user combinations using a text
                              		  editor, such as Notepad++.

Instead of using the
                              		  BAT spreadsheet for data input when you are adding phones, you can create the
                              		  comma-separated values (CSV) file using lines of ASCII text with values
                              		  separated by commas. There are different CSV data file formats for different
                              		  phone types. You must use the appropriate phone file format for the CSV text
                              		  file.

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Use a separate line to enter the values for each phone, IP telephony device, or user combination that you want to add to . You must create separate CSV files for each type of device. Keep in mind the following rules when you create the CSV data
                                       file.

Always include comma separators, even if a field is blank.

Specify the user ID if the phone is to be associated to a user.

Directory Number fields are optional only when you are creating the CSV file for use with a BAT template that has no lines.
                                                If lines are configured on the BAT phone template, you must supply directory numbers in the CSV file for each device.

An error occurs when you insert a CSV file with blank lines.

While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                                Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node of .

### Phone CSV Data File Formats

Different types of phones require specific data formats. Keep
                                 		  in mind that fields that are labeled as optional in the phone file format
                                 		  become mandatory fields when certain conditions are met.

#### Phones with Users Combinations File Format

The following sample shows the field length and whether the
                                    		  field is optional or mandatory for a text-based CSV file for phones and the
                                    		  fixed user format.

```
First Name (Optional, up to 64 characters), Last Name (Mandatory, 1 to 64 characters), User ID (Mandatory, 1 to 128 characters), Password (Optional, up to 128 characters), Manager User ID (Optional, up to 128 characters, must use the ID that exists in global directory), Department (Optional, up to 64 characters), PIN (Optional, up to 20 numerals), Default Profile (Optional, up to 50 characters), User Locale (Optional, up to 50 characters), Telephone Number (Optional, up to 20 numerals), Primary Extension (Optional, up to 50 numerals), Associated PC (Optional, up to 50 characters), ICD Extension (Optional, up to 50 numerals), Mail ID (Optional, up to 255 characters), Presence Group (Optional, up to 50 characters), Subscribe Calling Search Space (Optional, up to 50 characters), MAC Address (Mandatory, up to 12 characters), Description (Optional, up to 50 characters), Location (Optional, up to 50 characters), Directory Number (Optional, up to 24 numerals and special characters), Display (Optional, up to 30 characters), Line Text Label (Optional, up to 30 characters), Forward Busy External (Optional, up to 50 numerals and special characters), Forward No Answer External (Optional, up to 50 numerals and special characters), Forward No Coverage External (Optional, up to 50 numerals and special characters), Forward Busy Internal (Optional, up to 50 numerals and special characters), Forward No Answer Internal (Optional, up to 50 numerals and special characters), Forward No Coverage Internal (Optional, up to 50 numerals and special characters), Call Pickup Group (Optional, up to 50 characters), Speed Dial (Optional, up to 50 numerals and special characters), Speed Dial Label (Optional, up to 30 characters)
```

##### Sample

```
John,Smith,johns,abcde,Daviss,12,12345,johnProfile,English United States,1,1231123245AB,Dallas,
9725557154,9725557154,Mike,9725557172,9725557196,9725557112,
9725557127,9725557158,9725557189,9725557121/TollByPass,1230000000,Helpdesk
```

#### CTI Ports/H.323 Clients File Format

The following sample shows the field length and whether the
                                    		  field is optional or mandatory for a text-based CSV file for CTI ports and
                                    		  H.323 clients format.

```
Device Name (Mandatory, up to 15 characters for CTI ports and up to 50 characters for H.323 Clients), Description (Optional, up to 50 characters) Location (Optional, up to 50 characters),UserID(Optional, 1 to 30 characters),Directory Number(Optional, up to 24 numerals and special characters),Display (Optional, up to 30 characters), Line Text Label (Optional, up to 30 characters), Forward Busy External(Optional, up to 50 numerals and special characters),Forward No Answer External (Optional, up to 50 numerals and special characters), Forward No Coverage External (Optional, up to 50 numerals and special characters), Forward Busy Internal (Optional, up to 50 numerals and special characters), Forward No Answer Internal (Optional, up to 50 numerals and special characters), Forward No Coverage Internal (Optional, up to 50 numerals and special characters), Call Pickup Group (Optional, up to 50/50 characters)
```

##### Sample

```
TAPS Port 1,CTI TAPS Port 1,Dallas,johns,9728437154,9728437154, Mike,9728437172,9728437196,9728437127,9728437154,9728437178, 9728437189,9728437121/TollByPass,1230000000,Helpdesk
```

#### CTI Ports-Users and H.323 Client-Users Combinations File Format

The following sample shows the field length and whether the
                                    		  field is optional or mandatory for a text-based CSV file for CTI ports with
                                    		  users and H.323 clients with users format.

```
First Name (Optional, up to 64 characters), Last Name (Mandatory, 1 to 64 characters), User ID (Mandatory, 1-128 characters), Password (Optional, up to 128 characters), Manager User ID (Optional, up to 128 characters, must use existing ID in global directory), Department (Optional, up to 64 characters), PIN (Optional, up to 128 numerals), Default Profile (Optional, up to 50 characters), User Locale (Optional, up to 50 characters), Telephone Number (Optional, up to 64 numerals), Primary Extension (Optional, up to 50 numerals), Associated PC (Optional, up to 50 characters), ICD Extension (Optional, up to 50 numerals), Mail ID (Optional, up to 255 characters), Presence Group (Optional, up to 50 characters), Subscribe Calling Search Space (Optional, up to 50 characters),Device Name (Mandatory, up to 15 characters for CTI ports-users combination and up to 50 characters for H.323client-users combinations),Description (Optional, up to 50 characters), Location (Optional, up to 50 characters), Directory Number (Optional, up to 24 numerals and special characters), Display (Optional, up to 30 characters), Line Text Label (Optional, up to 30 characters), Forward Busy External (Optional, up to 50 numerals and special characters), Forward No Answer External (Optional, up to 50 numerals and special characters), Forward No Coverage External (Optional, up to 50 numerals and special characters), Forward Busy Internal (Optional, up to 50 numerals and special characters), Forward No Answer Internal (Optional, up to 50 numerals and special characters), Forward No Coverage Internal (Optional, up to 50 numerals and special characters), Call Pickup Group (Optional, up to 50 characters)
```

##### Sample

```
John,Smith,johns,abcde,Daviss,12,12345,johnProfile,English United States,1,TAPS Port 1,CTI
TAPS Port 1,9725557154,9725557154,Mike,9725557172,9725557196,9725557112,9725557127,9725557158,
9725557189,9725557121/TollByPass,1230000000,Helpdesk
```

If you use a comma or double quotes as part of the value in one of
                                                			 the fields, you must enclose the entire text value with double quotation marks
                                                			 to designate it as a single value.

For example, if you entered John, Bill as a text value, then you
                                                			 must enter the value as "John,Bill" .

If you entered a double quote in a value, then you must replace the
                                                			 double quote with two consecutive double quotes and enclose the value with
                                                			 double quotes. For example you must enter John "Chief as “John" "Chief" .

### Export the Fields for All Phone Details Option

When you are using the export utility to generate a file that
                                 		  containing all the details for the phone records, the export file has the
                                 		  following format.

Caution

Cisco does not recommend editing the file that is generated with the
                                             			 export utility. The system dynamically generates fields, such as Logout time
                                             			 and Login time, that must not be edited at all. You must ensure that the login
                                             			 user ID and Product Specific XML fields are accurate for them to work properly,
                                             			 and you must not edit them. Use BAT to update the product specific
                                             			 configurations.

```
Device Name,Description,Device Pool,Phone Template,CSS,AAR CSS,Location,Extension Mobility,Network Locale,Media Resource Group List,User Hold Audio Source,Network Hold Audio Source,Device User Locale,Signal Packet Capture Mode,Packet Capture Duration,Built in Bridge,Privacy,Retry Video Call as Audio,Ignore Presentation Indicators,Softkey Template,Module 1,Module 2,Phone Load Name,Module 1 Load Name,Module 2 Load Name,Information,Directory,Messages,Services,Authentication Server,Proxy Server,Idle,Idle Timer,MLPP Indication,MLPP Preemption,MLPP Domain,Device Type,User ID,Common Profile,Owner User ID,Allow CTI Control Flag,Device Presence Group,Security Profile,Device Subscribe CSS,Unattended Port,Require DTMF Reception,RFC2833 Disabled,Certificate Operation,Authentication String,Certification Operation Completion Time,Device Protocol,Secure Shell User,Secure Shell Password,XML,Dial Rules,CSS Reroute,CSS Refer,DTMF Signalling,Default DTMF Capability,SIP Profile,SIPCodec_MTPPreferredOrigCodec,Logout Profile,MTP Required,Digest User,Always Use Prime Line,Always Use Prime Line for Voice Messages,Geo Location
```

```
Directory Number,Partition,Voice Mail Profile,Line CSS,AAR Group,Line User Hold Audio Source,Line Network Hold Audio Source,Auto Answer,Forward All Voice Mail,Forward All Destination,Forward All CSS,Forward Busy Internal Voice Mail,Forward Busy Internal Destination,Forward Busy Internal CSS,Forward Busy External Voice Mail,Forward Busy External Destination,Forward Busy External CSS,Forward No Answer Internal Voice Mail,Forward No Answer Internal Destination,Forward No Answer Internal CSS,Forward No Answer External Voice Mail,Forward No Answer External Destination,Forward No Answer External CSS,Forward No Coverage Internal Voice Mail,Forward No Coverage Internal Destination,Forward No Coverage Internal CSS,Forward No Coverage External Voice Mail,Forward No Coverage External Destination,Forward No Coverage External CSS,Forward No Answer Ring Duration,Call Pickup Group,MLPP Target,MLPP CSS,MLPP No Answer Ring Duration,Line Text Label,External Phone Number Mask,Maximum Number of Calls,Busy Trigger,Message Waiting Lamp Policy,Ring setting (Phone Idle),Ring Setting (Phone Active),Caller Name,Caller Number,Redirected Number,Dialed Number,Line Description,Alerting Name,Alerting Name ASCII,Line Presence Group,Secondary CSS for Forward All,Forward on CTI Failure Voice Mail,Forward on CTI Failure Destination,Forward on CTI Failure CSS,Display,ASCII DisplayParty Entrance Tone,Log Missed Calls,Park Monitor Forward No Retrieve Ext Voice Mail,Park Monitor Forward No Retrieve Int Voice Mail,Park Monitor Forward No Retrieve Ext CSS,Park Monitor Forward No Retrieve Int CSS,Park Monitor Forward No Retrieve Ext Destination,Park Monitor Forward No Retrieve Int Destination,Park Monitor Reversion Timer
```

```
Speed Dial Number,Speed Dial Label,Speed Dial Label ASCII,Service Name,Subscribed Service Name,Subscribed Service Name ASCII,Parameter Name,Parameter Value,Busy Lamp Field Destination,Busy Lamp Field Directory Number,Busy Lamp Field Label,Busy Lamp Field Label ASCII
```

### Phone CSV File Examples

The following list provides examples of commonly used phone
                                 		  CSV data files:

#### Using a Template Attribute-Forward Busy Destination

If Forward Busy Destination is 3001 on a phone template, all
                                 		  records in a CSV file that have no value for Forward Busy Destination use 3001.

```
1231123245AB,SEP1231123245AB,Dallas,johns,9728437154,9728437154,Mike,,9728437196,9728437127,
9728437154,9728437178,9728437189,9728437121/TollByPass,1230000000,Helpdesk
```

#### No Phone Description Entry

If the description for a phone is blank, use this format:

```
1231123245AB,,Dallas,johns,9728437154,9728437154,Mike,9728437172,9728437196,
9728437127,9728437154,9728437178,9728437189,9728437121/TollByPass,1230000000,Helpdesk
```

#### No Active Line or Location Entry

If no active line is required and the location is also blank,
                                 		  use this format:

```
1231123245AB,SEP1231123245AB,,,1230000000,HelpDesk
```

#### Two Active Lines

If two active lines are required, use this format:

```
1231123245AB,SEP1231123245AB,Dallas,johns,9725557154,9725557154,Mike,9725557172,9725557196,
9728437127,9728437154,9728437178,9728437189,9725557121/TollByPass,9725557155,9725557155,
Kelvin,9725557133,9725557196,9728437112,9728437145,9728437187,9728437198,9725557112/
TollByPass,1230000000,Helpdesk
```

For the MAC Address, enter MAC address values or check the option for creating pseudo MAC addresses.

#### Mandatory Phone Entries

If one line is required and you want to include only the
                                 		  required values and none of the optional values, use this format:

```
1231123245AB,,,,9725557154,,,,,
```

#### Using pseudo MAC Address Option

If the option is checked for a pseudo MAC address and you want one line, use this format:

```
,Dallas,9725557154,9725557154,Mike,9725557172,9725557196,9728437127,9728437154,9728437178,
9728437189,9725557121/TollByPass,johns,1230000000,Helpdesk
```

## Create Text-Based
                        	 CSV User File

You can
                              		  create a CSV text file for users using a text editor, such as such as
                              		  Notepad++.

Instead of
                              		  using the BAT spreadsheet for data input when you are adding users, you can
                              		  create the comma-separated values (CSV) file by using lines of ASCII text with
                              		  values separated by commas. You must use the user file format for the user CSV
                              		  text file.

Cisco recommends
                                          			 uploading Text-Based CSV files saved in the UTF-8 format only, as characters
                                          			 other than ASCII characters can be stored in this format. Using a text editor,
                                          			 such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                          			 (BOM) from the Encoding drop-down. Text-Based
                                          			 CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          			 from Cisco Unified Communications
                                             				Manager .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Using a separate
                                       			 line for each user, enter the values for each user that you want to add to Cisco Unified Communications
                                          				Manager .

You can
                                          				associate any number of existing devices to a new user by entering the device
                                          				name of all the devices separated by a comma at the end of the record.

You can
                                          				associate a directory number to a user, even if that user does not control any
                                          				device.

An error
                                                      				  occurs if any blank lines exist in the CSV file.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the file to
                              		  first node of the Cisco Unified Communications
                                 			 Manager .

## User File Format

Tip

You must specify PIN and Password values, either on the CSV file or
                                          			 when using BAT for file insertion. If you want to apply individual PINs or
                                          			 passwords for each user or group of users, specify the PIN and password
                                          			 information in the CSV file. If you want to use a default PIN and password that
                                          			 all users can use, do not specify PIN or password values in the CSV file and
                                          			 instead provide this information when you use BAT to insert the CSV file in Cisco Unified Communications Manager .

The following sample format and examples show the fields,
                              		  field length, and whether the field is optional or mandatory for a text-based
                              		  CSV file for users.

```
First Name (Optional, up to 64 characters), Last Name (Mandatory, 1 to 64 characters), User ID(Mandatory, up to 128 characters), Manager User ID (Optional, up to 128 characters, must use existing ID in global directory), Department (Optional, up to 64 characters), PIN (Optional, up to 128 numerals), Default Profile (Optional, up to 50 characters), User Locale (Optional, up to 50 characters), Telephone Number (Optional, up to 64 numerals), Primary Extension (Optional, up to 50 numerals), Associated PC (Optional, up to 50 characters), ICD Extension (Optional, up to 50 numerals), Mail ID (Optional, up to 255 characters), Presence Group (Optional, up to 50 characters), Subscribe Calling Search Space (Optional, up to 50 characters).
```

### Sample

```
John,Smith,johns,abc123de,karend,0012055,9989,johns profile,English
United States,SEP1231123245AB,9725557154,SEP0010EB001234
```

You must specify delimiters even if a field is blank. Refer
                              		  to the following examples and sample CSV records when you are creating CSV
                              		  files.

### Example 1

If the manager for a user is blank, use this format:

```
John,Smith,johns,abc123de,,0012055,9989,johns profile,English United
States,SEP1231123245AB,9725557154,SEP0010EB001234
```

### Example 2

When you want to complete only the mandatory fields, use
                              		  this format:

```
Smith,johns,,,,,,,,
```

### Example 3

When you want to complete only the mandatory fields and
                              		  associate the user to a phone, use this format:

```
Smith,johns,,,,,,,SEP1231123245AB,
```

### Example 4

A user can control more than one device. You can add device
                              		  names for additional devices at the end of the record.

If the user controls only one device, use this format:

```
John,Smith,johns,abc123de,karend,0012055,9989,johns profile,English
United States,SEP1231123245AB,9725557154
```

If the user controls three devices, use this format:

```
John,Smith,johns,abc123de,karend,0012055,9989,johns profile,English UnitedStates,SEP1231123245AB,9725557154,SEP0010EB001234,SEP0010EB432101
```

### Update Users File Format

Use a text editor to create the CSV text file for updating
                                 		  users. Upload the file to first node server.

When you are updating a record, you need to supply all
                                 		  mandatory fields for a file. If you have stored values in the optional fields,
                                 		  and you update a record with blank optional fields, you will reset the values
                                 		  to blank. It is possible for you to retain previously stored values during
                                 		  update.

The following sample format shows the field length and
                                 		  string types followed by examples of CSV files for updating users.

```
User ID (Mandatory, 1 to 128 characters), Password (Optional, up to 128 characters), Manager (Optional, up to 128 characters, must use existing ID in global directory), Department (Optional, up to 64 characters), PIN (Optional, up to 128 numerals), Default Profile (Optional, up to 50 characters), User Locale (Optional, up to 50 characters), Telephone Number (Optional, up to 64 numerals), Primary Extension (Optional, up to 50 numerals), Associated PC (Optional, up to 50 characters), ICD Extension (Optional, up to 50 numerals), Mail ID (Optional, up to 255 characters).
```

#### Sample

```
johns,Daviss,123,johnProfile,English United States,SEP8612113425AC,9725557154
```

You must specify delimiters even if a field is blank. Refer to the
                                             			 following examples and sample CSV records when you are creating CSV files.

#### Example 1

If the manager for a user is blank. use this format:

```
johns,,123,johnProfile,English United States,SEP8612113425AC,9725557154
```

#### Example 3

Mandatory fields include the following fields:

```
John,Daviss,123,johnProfile,,,
```

## Create Text-Based
                        	 CSV File for User Device Profile

You can
                              		  create a CSV text file for user device profiles using a text editor, such as
                              		  Notepad++.

Instead of
                              		  using the BAT spreadsheet for data input when you are adding user device
                              		  profiles, you can create the comma-separated values (CSV) file by using lines
                              		  of ASCII text with values separated by commas. You must use the user device
                              		  profile file format for the CSV text file.

If you use comma
                                          			 or double quotes as part of string in one of the fields, you must enclose the
                                          			 entire text string with double quotes.

Cisco recommends
                                          			 uploading Text-Based CSV files saved in the UTF-8 format only, as characters
                                          			 other than ASCII characters can be stored in this format. Using a text editor,
                                          			 such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                          			 (BOM) from the Encoding drop-down. Text-Based
                                          			 CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          			 from Cisco Unified Communications
                                             				Manager .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Using a separate
                                       			 line for each user device profile, enter the values for each user device
                                       			 profile that you want to add to Cisco Unified Communications
                                          				Manager .

An error
                                                      				  occurs if any blank lines exist in the CSV file.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file
                              		  to the first node server for Cisco Unified Communications
                                 			 Manager .

### User Device Profile File Format

The following sample format shows the field length and
                                 		  string types followed by examples of a CSV files for user device profiles.

```
Device Profile Name(Mandatory, 1 to 50 characters),Description(Optional, 1 to 50 characters),Login UserID (Optional, 4 to 30 characters),Directory Number(Optional, up to 24 numerals and special characters),Display(Optional, for internal Caller ID, up to 30 characters),Line Text Label(Optional, up to 30 characters),Forward Busy External Destination(Optional, up to 50 numerals),Forward No Answer External Destination(Optional, up to 50 numerals),Forward No Coverage External(Optional, up to 50 numerals),Forward Busy Internal Destination(Optional, up to 50 numerals),Forward No Answer Internal Destination(Optional, up to 50 numerals),Forward No Coverage Internal(Optional, up to 50 numerals),Call Pickup Group(Optional, up to 50/50 characters),Speed Dial Number(Optional, up to 50 numerals),Speed Dial Label(optional, up to 30 characters)
```

#### Sample

```
John Profile,John's Profile,Johns,9725557154,9725557154,Mike,9725557172,9725557196,
9725557126,9725557154,9725557178,9725557189,9725557121/TollByPass,1230000000,Helpdesk
```

#### Example 1

You must specify delimiters even if a field is blank. The
                                 		  following example shows the correct format for not specifying a Display
                                 		  setting:

```
John Profile,John's Profile,Johns,9725557154,,Mike,9725557172,9725557196,9725557126,9725557154,9725557178,
9725557189,9725557121/TollByPass,1230000000,Helpdesk
```

#### Example 2

If it is a 0-line profile and only mandatory fields are
                                 		  added, use the following example:

```
John Profile,,,,
```

#### Example 3

If only the mandatory fields are completed and you want to
                                 		  associate the user device profile to only one directory number, use this
                                 		  format:

```
John Profile,,,9725557154,,,,,
```

### User Device Profile with Two Lines and Two Speed Dials

The following example format shows the field length and
                                 		  string types of a CSV file for user device profiles with two lines.

```
User Device Profile Name(Mandatory, 1 to 50 characters),Description(Optional, 1 to 50 characters),Login UserID (Optional, 4 to 30 characters),Directory Number1(Optional, up to 24 numerals and special characters),Display1(Optional, for internal Caller ID, up to 30 characters),Line Text Label1(Optional, up to 30 characters),Forward Busy External Destination1(Optional, up to 50 numerals),Forward No Answer External Destination1(Optional, up to 50 numerals),Forward No Coverage External Destination1(Optional, up to 50 numerals),Forward Busy Intermal Destination1(Optional, up to 50 numerals),Forward No Answer Internal Destination1(Optional, up to 50 numerals),Forward No Coverage Internal Destination1(Optional, up to 50 numerals),Call Pickup Group1(Optional, up to 50/50 characters),Directory Number2(Optional, up to 24 numerals and special characters),Display2(Optional, for internal Caller ID, up to 30 characters),Line Text Label2(Optional, up to 30 characters),Forward Busy External Destination2(Optional, up to 50 numerals),Forward No Answer External Destination2(Optional, up to 50 numerals),Forward No Coverage External Destination2(Optional, up to 50 numerals),Forward Busy Intermal Destination2(Optional, up to 50 numerals),Forward No Answer Internal Destination2(Optional, up to 50 numerals),Forward No Coverage Internal Destination2(Optional, up to 50 numerals),Call Pickup Group2(Optional, up to 50/50 characters),Speed Dial Number1(Optional, up to 50 numerals),Speed Dial Label1(optional, up to 30 characters),Speed Dial Number2(Optional, up to 50 numerals),Speed Dial Label2(optional, up to 30 characters)
```

#### Example

```
John Profile,John's Profile,John’s,9725557154,9725557154,Mike,9725557172,9725557196,9725557126,9725557154,
9725557178,9725557189,9725557121/TollByPass,9725557155,9725557155,Kelvin,9725557133,9725557196,
9725557113,9725557145,9725557187,9725557198,9725557112/TollByPass,1230000000,Helpdesk,
2149523460,Keith
```

### Export File Fields for User Device Profile with All Details Option

When you are using the export utility to generate a file
                                 		  that contains all the details for the user device profiles, the export file
                                 		  will have the following format. The example shows the length and type of fields
                                 		  in the export all details file.

The export utility does not generate model-specific fields
                                 		  for user device profiles.

Caution

Cisco does not recommend editing the file that is generated with the
                                             			 export utility. The system dynamically generates some fields, such as Logout
                                             			 time and Login time, that must not be edited at all. You must ensure that the
                                             			 login user ID and Product Specific XML fields are accurate for them to work
                                             			 properly, and you must not edit them. Use BAT to update the product-specific
                                             			 configurations.

```
Device Profile Name,Description,Device Pool,Phone Template,CSS,AAR CSS,Location,Extension Mobility,Network Locale,Media Resource Group List,User Hold Audio Source,Network Hold Audio Source,Device User Locale,Signal Packet Capture Mode,Packet Capture Duration,Built in Bridge,Privacy,Retry Video Call as Audio,Ignore Presentation Indicators,Softkey Template,Module 1,Module 2,Phone Load Name,Module 1 Load Name,Module 2 Load Name,Information,Directory,Messages,Services,Authentication Server,Proxy Server,Idle,Idle Timer,MLPP Indication,MLPP Preemption,MLPP Domain,Device Type,User ID,Common Profile,Owner User ID,Allow CTI Control Flag,Device Presence Group,Security Profile,Device Subscribe CSS,Unattended Port,Require DTMF Reception,RFC2833 Disabled,Certificate Operation,Authentication String,Certification Operation Completion Time,Device Protocol,Secure Shell User,Secure Shell Password,XML,Dial Rules,CSS Reroute,CSS Refer,DTMF Signalling,Default DTMF Capability,SIP Profile,SIPCodec_MTPPreferredOrigCodec,Logout Profile,MTP Required,Digest User,Always Use Prime Line,Always Use Prime Line for Voice Message
```

```
Directory Number,Partition,Voice Mail Profile,Line CSS,AAR Group,Line User Hold Audio Source,Line Network Hold Audio Source,Auto Answer,Forward All Voice Mail,Forward All Destination,Forward All CSS,Forward Busy Internal Voice Mail,Forward Busy Internal Destination,Forward Busy Internal CSS,Forward Busy External Voice Mail,Forward Busy External Destination,Forward Busy External CSS,Forward No Answer Internal Voice Mail,Forward No Answer Internal Destination,Forward No Answer Internal CSS,Forward No Answer External Voice Mail,Forward No Answer External Destination,Forward No Answer External CSS,Forward No Coverage Internal Voice Mail,Forward No Coverage Internal Destination,Forward No Coverage Internal CSS,Forward No Coverage External Voice Mail,Forward No Coverage External Destination,Forward No Coverage External CSS,Forward No Answer Ring Duration,Call Pickup Group,MLPP Target,MLPP CSS,MLPP No Answer Ring Duration,Line Text Label,External Phone Number Mask,Maximum Number of Calls,Busy Trigger,Message Waiting Lamp Policy,Ring setting (Phone Idle),Ring Setting (Phone Active),Caller Name,Caller Number,Redirected Number,Dialed Number,Line Description,Alerting Name,Alerting Name ASCII,Line Presence Group,Secondary CSS for Forward All,Forward on CTI Failure Voice Mail,Forward on CTI Failure Destination,Forward on CTI Failure CSS,Display,ASCII Display,Party Entrance Tone,Log Missed Calls,Park Monitor Forward No Retrieve Ext Voice Mail,Park Monitor Forward No Retrieve Int Voice Mail,Park Monitor Forward No Retrieve Ext CSS,Park Monitor Forward No Retrieve Int CSS,Park Monitor Forward No Retrieve Ext Destination,Park Monitor Forward No Retrieve Int Destination,Park Monitor Reversion Timer
```

```
Speed Dial Number,Speed Dial Label,Speed Dial Label ASCII,Service Name,Subscribed Service Name,Subscribed Service Name ASCII,Parameter Name,Parameter Value,Busy Lamp Field Destination,Busy Lamp Field Directory Number,Busy Lamp Field Label,Busy Lamp Field Label ASCII
```

Use True and False for settings with Boolean values.

## Create Text-Based
                        	 CSV File for Cisco Unified CM Assistant Manager-Assistant Associations

You can
                              		  create a CSV text file for UnifiedCM Assistant manager and assistants using a
                              		  text editor, such as Notepad++.

Instead of
                              		  using the BAT spreadsheet for data input when you are adding UnifiedCM
                              		  Assistant managers and assistants, you can create the comma-separated values
                              		  (CSV) file by using lines of ASCII text with values separated by commas. You
                              		  must use the manager and assistants file format for the CSV text file.

Cisco recommends
                                          			 uploading Text-Based CSV files saved in the UTF-8 format only, as characters
                                          			 other than ASCII characters can be stored in this format. Using a text editor,
                                          			 such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                          			 (BOM) from the Encoding drop-down. Text-Based
                                          			 CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          			 from Cisco Unified Communications
                                             				Manager .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Using a separate
                                       			 line for each manager-assistants association, enter the values for each
                                       			 manager-assistant that you want to add to Cisco Unified Communications
                                          				Manager .

An error
                                                      				  occurs if any blank lines exist in the CSV file.

You can assign
                                          				multiple assistants to a manager by entering the user IDs of the manager and
                                          				assistants separated by a comma at the end of the record.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file
                              		  to the first node server for Cisco Unified Communications
                                 			 Manager .

### Managers and Assistants File Formats

The following sample formats and examples show the field length and string types for UnifiedCommunications Manager Assistant
                                 manager and assistant associations. Use the user ID of the manager for the Manager ID and the user ID of the assistant for
                                 the Assistant ID. You can also associate many managers to one assistant by putting the Assistant ID first, followed by a list
                                 of Manager IDs. When you insert the CSV file, you select the type of association.

### Default Manager-Assistant Association

Use the following default format for manager-assistant
                                 		  association.

```
ManagerID (Mandatory, 1 to 30 characters),AssistantID 1 (Mandatory, 1 to 30 characters),AssistantID 2 (Optional, 1 to 30 characters)...AssistantID # (Optional, 1 to 30 characters)
```

#### Sample

```
Johns,Mikeh,Larryh
```

### Default Assistant-Manager Association

Use the following default format for assistant-manager
                                 		  association.

```
AssistantID (Mandatory, 1 to 30 characters),ManagerID 1(Mandatory, 1 to 30 characters),ManagerID 2 (Optional, 1 to 30 characters)...ManagerID # (Optional, 1 to 30 characters)
```

#### Sample

```
Larryh,Johns,Mikeb,Karend
```

### Custom Manager-Assistant Association

For proxy line configurations, you can build a CSV data file
                                 		  that specifies the proxy lines on assistant phones by using this format.

```
ManagerID (Mandatory, 1 to 30 characters),Device Name (Optional, 15 characters),Intercom DN (Optional, 1 to 24 characters),Assistant User ID (Mandatory, 1 to 30 characters),Device Name (Optional, 15 characters),Intercom DN (Optional, 1 to 24 characters),Proxy Line DN (Mandatory, 1to 24 characters),Manager Line DN (Mandatory, 1 to 24 characters)
```

#### Example

```
Johns,SEP1231123245AB,90001,Mikeh,SEP2342342342AB,20001,20002,90002
```

## Create Text-Based
                        	 CSV File for Cisco VG200 Gateways

You can
                              		  create a CSV text file for VG200 gateways using a text editor, such as
                              		  Notepad++.

Instead of
                              		  using the BAT spreadsheet for data input when you are adding CiscoVG200
                              		  gateways, you can create the comma-separated values (CSV) file by using lines
                              		  of ASCII text with values separated by commas. You must use the appropriate
                              		  file format for the type of trunk and port for the gateway.

Cisco recommends
                                          			 uploading Text-Based CSV files saved in the UTF-8 format only, as characters
                                          			 other than ASCII characters can be stored in this format. Using a text editor,
                                          			 such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                          			 (BOM) from the Encoding drop-down. Text-Based
                                          			 CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          			 from Cisco Unified Communications
                                             				Manager .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Using a separate
                                       			 line for each gateway, enter the values for each gateway and port that you want
                                       			 to add to Cisco Unified Communications
                                          				Manager .

An error
                                                      				  occurs if any blank lines exist in the CSV file.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file
                              		  to the first node server for Cisco Unified Communications
                                 			 Manager .

### FXO or FXS Trunks CSV File Format

The following sample format shows the required field length
                                 		  and string types followed by sample of CSV files for a Cisco VG200 gateway.

```
MGCP Domain Name(Mandatory, 1 to 64 characters),Description(Optional, up to 100 characters), Slot (Mandatory, up to 3 numerals), Subunit (Mandatory, up to 3 numerals), Port Number(Mandatory, up to 3 numerals), Port Description Optional, up to 50 characters),Port Directory Number(Optional, up to 24 numerals and special characters)
```

#### Sample

```
MGCPTest,VG200 Lab Gateway,0,1,0,Port 0,97255576601MGCPTest,VG200 Lab Gateway,0,1,1,Port 1,97255572001
```

You must include comma separators even if a field is blank. Specify
                                             			 the directory number and route partition only if the port type in the Cisco
                                             			 VG200 gateway template is POTS.

#### Example 1

If the Description for a Cisco VG200 gateway is blank, use
                                 		  this format:

```
MGCPTest, ,0,1,0,Port 0,97255576601
```

### T1 CAS T1 PRI or E1 PRI Trunks File Format

The following sample format shows the required field length
                                 		  and string types followed by examples of CSV files for the Cisco VG200 gateway.

#### T1 CAS Trunks

```
MGCP Domain Name(Mandatory, 1 to 64 characters),Description(Optional, up to 100 characters),Slot(Mandatory, up to 3 numerals),Subunit(Mandatory, up to 3 numerals),Port Number(Mandatory, up to 3 numerals),Port Description (Optional, up to 50 characters),CAS Port Number(Optional, up to 3 numerals)
```

#### Sample 1

```
MGCPTest,VG200 Lab Gateway,001,001,001,,,
```

#### T1 PRI or E1 PRI

```
MGCP Domain Name(Mandatory, 1 to 64 characters),Description(Optional, up to 100 characters),Slot(Mandatory, up to 3 numerals), Subunit(Mandatory, up to 3 numerals), Port Number(Mandatory, up to 3 numerals), Port Description (Optional, up to 50 characters)
```

#### Sample 2

```
MGCPTest,VG200 Lab Gateway,001,001,001,,
```

You must include comma separators even if a field is blank.

#### Example for Both Trunk Options

If you provide only the mandatory value, use this format:

```
MGCPTest,,001,001,001,,
```

T1 CAS Examples

If the Description for a Cisco VG200 gateway is blank, use
                                 		  this option:

```
MGCPTest,,001001,001,001,MGCP Port,
```

For port identifiers, ensure the first digit is either 0 or
                                 		  1 (signifying either Sub-Unit 0 or Sub-Unit 1), followed by the port number, 01
                                 		  to 24. Acceptable values include 001 through 024 or 101 through 124. If the
                                 		  Cisco VG200 gateway template has three port identifiers, use this option:

```
MGCPTest,VG200 Lab Gateway,001,002,003
```

## Create Text-Based
                        	 CSV File for Cisco VG224 Gateways

You can
                              		  create a CSV text file for VG224 gateways using a text editor, such as
                              		  Notepad++.

Instead of
                              		  using the BAT spreadsheet for data input when you are adding CiscoVG224
                              		  gateways, you can create the comma-separated values (CSV) file by using lines
                              		  of ASCII text with values separated by commas. You must use the appropriate
                              		  file format for the type of trunk and port for the gateway.

Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Using a separate line for each gateway, enter the values for each gateway and port that you want to add to .

An error occurs if any blank lines exist in the CSV file.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node server for .

### FXS Trunks CSV File Format for VG224

The following sample format shows the required field length
                                 		  and string types followed by sample of CSV files for a Cisco VG224 gateway.

```
MGCP Domain Name(Mandatory, 1 to 64 characters),Description(Optional, up to 100 characters),Slot(Mandatory, up to 3 numerals), Subunit (Mandatory, up to 3 numerals), Port Number(Mandatory, up to 3 numerals), Port Description Optional, up to 50 characters),Port Directory Number(Optional, up to 24 numerals and special characters)
```

#### Sample

```
MGCPTest,VG224 Lab Gateway,2,0,0,Port 0,97255576601MGCPTest,VG224 Lab Gateway,2,0,1,Port 1,97255572001
```

You must include comma separators even if a field is blank. Specify
                                             			 the directory number and route partition only if the port type in the Cisco
                                             			 VG224 gateway template is POTS.

#### Example 1

If the Description for a Cisco VG224 gateway is blank, use
                                 		  this format:

```
MGCPTest, ,2,0,0,Port 0,97255576601
```

## Create Text-Based CSV File for Cisco VG310 Gateways

You can create a CSV text file for VG310 gateways using a text editor, such as Notepad++.

Instead of using the BAT spreadsheet for data input when you are adding Cisco VG310 gateways, you can create the comma-separated
                              values (CSV) file by using lines of ASCII text with values separated by commas. You must use the appropriate file format for
                              the type of trunk and port for the gateway.

Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from .

Step 1

Open a text editor or any application that allows you to export or create a text-based CSV file.

Step 2

Using a separate line for each gateway, enter the values for each gateway and port that you want to add to .

An error occurs if any blank lines exist in the CSV file.

Step 3

While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                       Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node server for .

### FXS Trunks CSV File Format for VG310

The following sample format shows the required field length and string types followed by sample of CSV files for a Cisco VG310
                                 gateway.

```
MGCP Domain Name(Mandatory, 1 to 64 characters),Description(Optional, up to 100 characters),Slot(Mandatory, up to 3 numerals), Subunit (Mandatory, up to 3 numerals), Port Number(Mandatory, up to 3 numerals), Port Description Optional, up to 50 characters),Port Directory Number(Optional, up to 24 numerals and special characters)
```

#### Sample

```
MGCPTest,VG310 Lab Gateway,2,0,0,Port 0,97255576601MGCPTest,VG310 Lab Gateway,2,0,1,Port 1,97255572001
```

You must include comma separators even if a field is blank. Specify the directory number and route partition only if the port
                                             type in the Cisco VG310 gateway template is POTS.

#### Example 1

If the Description for a Cisco VG310 gateway is blank, use this format:

```
MGCPTest, ,2,0,0,Port 0,97255576601
```

## Create Text-Based CSV File for VG320 Gateways

You can create a CSV text file for VG320 gateways using a text editor, such as Notepad++.

Instead of using the BAT spreadsheet for data input when you are adding CiscoVG320 gateways, you can create the comma-separated
                              values (CSV) file by using lines of ASCII text with values separated by commas. You must use the appropriate file format for
                              the type of trunk and port for the gateway.

Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from .

Step 1

Open a text editor or any application that allows you to export or create a text-based CSV file.

Step 2

Using a separate line for each gateway, enter the values for each gateway and port that you want to add to .

An error occurs if any blank lines exist in the CSV file.

Step 3

While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                       Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node server for .

### FXS Trunks CSV File Format for VG320

The following sample format shows the required field length and string types followed by sample of CSV files for a Cisco VG320
                                 gateway.

```
MGCP Domain Name(Mandatory, 1 to 64 characters),Description(Optional, up to 100 characters),Slot(Mandatory, up to 3 numerals), Subunit (Mandatory, up to 3 numerals), Port Number(Mandatory, up to 3 numerals), Port Description Optional, up to 50 characters),Port Directory Number(Optional, up to 24 numerals and special characters)
```

#### Sample

```
MGCPTest,VG320 Lab Gateway,2,0,0,Port 0,97255576601MGCPTest,VG320 Lab Gateway,2,0,1,Port 1,97255572001
```

You must include comma separators even if a field is blank. Specify the directory number and route partition only if the port
                                             type in the Cisco VG320 gateway template is POTS.

#### Example 1

If the Description for a Cisco VG320 gateway is blank, use this format:

```
MGCPTest, ,2,0,0,Port 0,97255576601
```

## Create Text-Based CSV File for VG350 Gateways

You can create a CSV text file for VG350 gateways using a text editor, such as Notepad++.

Instead of using the BAT spreadsheet for data input when you are adding Cisco VG350 gateways, you can create the comma-separated
                              values (CSV) file by using lines of ASCII text with values separated by commas. You must use the appropriate file format for
                              the type of trunk and port for the gateway.

Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from .

Step 1

Open a text editor or any application that allows you to export or create a text-based CSV file.

Step 2

Using a separate line for each gateway, enter the values for each gateway and port that you want to add to .

An error occurs if any blank lines exist in the CSV file.

Step 3

While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                       Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node server for .

### FXS Trunks CSV File Format for VG350

The following sample format shows the required field length and string types followed by sample of CSV files for a Cisco VG350
                                 gateway.

```
MGCP Domain Name(Mandatory, 1 to 64 characters),Description(Optional, up to 100 characters),Slot(Mandatory, up to 3 numerals), Subunit (Mandatory, up to 3 numerals), Port Number(Mandatory, up to 3 numerals), Port Description Optional, up to 50 characters),Port Directory Number(Optional, up to 24 numerals and special characters)
```

#### Sample

```
MGCPTest,VG350 Lab Gateway,2,0,0,Port 0,97255576601MGCPTest,VG350 Lab Gateway,2,0,1,Port 1,97255572001
```

You must include comma separators even if a field is blank. Specify the directory number and route partition only if the port
                                             type in the Cisco VG350 gateway template is POTS.

#### Example 1

If the Description for a Cisco VG350 gateway is blank, use this format:

```
MGCPTest, ,2,0,0,Port 0,97255576601
```

## Create Text-Based CSV File for VG410 Gateways

You can create a CSV text file for VG410 gateways using a text editor, such as Notepad++.

Instead of using the BAT spreadsheet for data input when you're adding Cisco VG410 gateways, you can create the comma-separated
                              values (CSV) file by using lines of ASCII text with values separated by commas. You must use the appropriate file format for
                              the type of trunk and port for the gateway.

Step 1

Open a text editor or any application that allows you to export or create a text-based CSV file.

Step 2

Using a separate line for each gateway, enter the values for each gateway and port that you want to add to Unified Communications
                                       Manager.

Step 3

While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                       Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node server for Unified Communications Manager.

## Create Text-Based CSV File for VG420 Gateways

You can create a CSV text file for VG420 gateways using a text editor, such as Notepad++.

Instead of using the BAT spreadsheet for data input when you are adding CiscoVG420 gateways, you can create the comma-separated
                              values (CSV) file by using lines of ASCII text with values separated by commas. You must use the appropriate file format for
                              the type of trunk and port for the gateway.

Step 1

Open a text editor or any application that allows you to export or create a text-based CSV file.

Step 2

Using a separate line for each gateway, enter the values for each gateway and port that you want to add to Unified Communications
                                       Manager.

Step 3

While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                       Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node server for Unified Communications Manager.

## Create Text-Based CSV File for VG450 Gateways

You can create a CSV text file for VG450 gateways using a text editor, such as Notepad++.

Instead of using the BAT spreadsheet for data input when you are adding Cisco VG450 gateways, you can create the comma-separated
                              values (CSV) file by using lines of ASCII text with values separated by commas. You must use the appropriate file format for
                              the type of trunk and port for the gateway.

Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from .

Step 1

Open a text editor or any application that allows you to export or create a text-based CSV file.

Step 2

Using a separate line for each gateway, enter the values for each gateway and port that you want to add to .

An error occurs if any blank lines exist in the CSV file.

Step 3

While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                       Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node server for .

### FXS Trunks CSV File Format for VG450

The following sample format shows the required field length and string types followed by sample of CSV files for a Cisco VG450
                                 gateway.

```
MGCP Domain Name(Mandatory, 1 to 64 characters),Description(Optional, up to 100 characters),Slot(Mandatory, up to 3 numerals), Subunit (Mandatory, up to 3 numerals), Port Number(Mandatory, up to 3 numerals), Port Description Optional, up to 50 characters),Port Directory Number(Optional, up to 24 numerals and special characters)
```

#### Sample

```
MGCPTest,VG450 Lab Gateway,2,0,0,Port 0,97255576601MGCPTest,VG450 Lab Gateway,2,0,1,Port 1,97255572001
```

You must include comma separators even if a field is blank. Specify the directory number and route partition only if the port
                                             type in the Cisco VG450 gateway template is POTS.

#### Example 1

If the Description for a Cisco VG450 gateway is blank, use this format:

```
MGCPTest, ,2,0,0,Port 0,97255576601
```

## Create Text-Based CSV File for ISR 4461 Gateways

You can create a CSV text file for ISR 4461 gateways using a text editor, such as Notepad++.

Instead of using the BAT spreadsheet for data input when you are adding Cisco ISR 4461 gateways, you can create the comma-separated
                              values (CSV) file by using lines of ASCII text with values separated by commas. You must use the appropriate file format for
                              the type of trunk and port for the gateway.

Step 1

Open a text editor or any application that allows you to export or create a text-based CSV file.

Step 2

Using a separate line for each gateway, enter the values for each gateway and port that you want to add to Unified Communications
                                       Manager.

Step 3

While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                       Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node server for Unified Communications Manager.

## Create Text-Based
                        	 CSV File for Cisco Catalyst 6000 FXS Ports

You can
                              		  create a CSV text file for Cisco Catalyst 6000 FXS ports using a text editor,
                              		  such as Notepad++.

Instead of using the BAT spreadsheet for data input when you are adding Cisco Catalyst 6000 FXS ports, you can create the
                              comma-separated values (CSV) file by using lines of ASCII text with values separated by commas. You must use the appropriate
                              file format for the type of gateway.

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Using a separate line for each port, enter the values for each port that you want to add to .

An error occurs if any blank lines exist in the CSV file.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node server for .

## Cisco Catalyst 6000 (FXS) Torts File Format

The CSV file contains information about each port as a
                              		  record. Each record specifies the gateway MAC address and port number on that
                              		  gateway to which you want to add or update the port details.

BAT does not add CiscoCatalyst 6000 (FXS) gateways. It only adds or
                                          			 updates ports to an existing gateway.

For the MAC address, enter no MACaddress values for an
                              		  existing CiscoCatalyst 6000 (FXS) gateway. This MACaddress uses the last 12
                              		  characters in the Gateway Name.

If you provide no values for Partition for any record on the
                              		  CSV file, the system uses values from the BAT template for these fields.

The following sample format shows the required field length
                              		  and string types followed by examples of CSV files for Catalyst 6000 (FXS)
                              		  ports.

```
MAC Address (Mandatory, 12 characters),Port Number (Mandatory, 2 numerals),Directory Number(Optional, up to 24 numerals and special characters)
```

### Sample

```
1231123245AB,23,9725557250
```

You must include comma separators even if a field is blank.

Do not specify a partition unless you have also specified a
                                          			 directory number.

### Examples

If the directory number for a port is blank, use this
                              		  format:

```
1231123245AB,23,
```

If you want to add only the mandatory values, use this
                              		  format:

```
1231123245AB,23,
```

## Create Text-Based
                        	 CSV File for Cisco VG202 and VG204 Gateways

You can
                              		  create a CSV text file for VG202 or VG204 gateways using a text editor, such as
                              		  Notepad++.

Instead of using the BAT spreadsheet for data input when you are adding Cisco VG202 and VG204 gateways, you can create the
                              comma-separated values (CSV) file by using lines of ASCII text with values separated by commas. You must use the appropriate
                              file format for the gateway.

Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Using a separate line for each gateway, enter the values for each gateway and port that you want to add to .

An error occurs if any blank lines exist in the CSV file.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node server for .

### CSV File Format for VG202 and VG204 Gateways

The following sample formats and examples show the fields,
                                 		  field length, and whether the field is optional or mandatory for a text-based
                                 		  CSV file for VG202 and VG204 Gateways.

There are two CSV file formats for VG202 and VG204 Gateways
                                 		  depending upon the Protocol:

MGCP

SCCP

#### For MGCP Gateway

```
Domain Name(Mandatory, 1 to 64 characters),Description(Optional, up to 100 characters),Slot(Mandatory, up to 3 numerals),Subunit(Mandatory, up to 3 numerals),Port Number(Mandatory, up to 3 numerals),Port Description(Optional, up to 50 characters),Port Directory Number(Optional, up to 24 numerals and special characters).
```

#### Sample

```
test,test,0,0,0,sample,1000
```

#### For SCCP Gateway

```
Mac Address(Mandatory, 1 to 64 characters),Description(Optional, up to 100 characters),Slot(Mandatory, up to 3 numerals),Subunit(Mandatory, up to 3 numerals),Port Number(Mandatory, up to 3 numerals),Port Description(Optional, up to 50 characters),Port Directory Number(Optional, up to 24 numerals and special characters).
```

Sample

```
SKIGW1111111111,test,0,0,0,sample,1000
```

## Create Custom
                        	 Text-Based CSV Files for Client Matter Codes and Forced Authorized
                        	 Codes

You can
                              		  create a custom text-based CSV file using a text editor, such as Notepad++.

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Using a separate
                                       			 line for each code, create a custom Client Matter Codes (CMC) CSV file or a
                                       			 Forced Authorized Codes (FAC) CSV file, as described in the following steps:

For CMC—Step 3 and Step 4

For FAC— Step 3 and Step 4

Tip

Remember that
                                                      				  you must create two separate CSV files, one for CMC and one for FAC.

Step 3

To create a CMC
                                       			 CSV file, enter the corresponding information, where x, y represent the
                                       			 following fields:

x—The client matter code (mandatory entry for all additions, updates, and deletions)

y—The description (optional if you update the entry)

For example, you
                                          				may enter 5555,Acme Toys, where 5555 equals the mandatory client matter code,
                                          				and Acme Toys equals the description.

Step 4

To create a FAC
                                       			 CSV file, enter the corresponding information, where x,y,z represent the
                                       			 following fields:

x—The forced authorization code (mandatory entry for all additions, updates, and deletions)

y—The authorization code name (optional if you update the entry)

z—The authorization level (optional if you update the entry)

For example, you
                                          				may enter 1234,John Smith,20, where 1234 equals the forced authorization code,
                                          				John Smith equals the authorization code name, and 20 equals the authorization
                                          				level.

Caution

If you add new
                                                      				  codes at the same time that you update them, make sure that you enter all
                                                      				  required information. You can change any part of an existing record, but you
                                                      				  must include the code; for example, the forced authorization code or client
                                                      				  matter code. Deleting information and leaving it blank does not remove the
                                                      				  information from the database; a blank value does not overwrite an existing
                                                      				  value in the database, but, updating the value, for example, to Acme Toys,
                                                      				  Inc., or John L. Smith from the preceding examples, overwrites the existing
                                                      				  value in the database.

Step 5

Upload the CSV file to the first node of .

While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                          Order Mark (BOM) from the Encoding drop-down.

Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                                      can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                                      Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                                      from .

Step 6

Perform one of
                                       			 the following tasks:

If you made additions or updates, insert the file in the CUCM database using BAT.

You can delete code settings.

You cannot
                                                      				  perform insert and update operations simultaneously with the same CSV file. You
                                                      				  have to create separate CSV files for insert and update.

### CMC File Format

The following sample format and examples show the fields,
                                 		  field length, and whether the field is optional or mandatory for a text-based
                                 		  CSV file for client matter codes.

```
Client Matter Code(Mandatory, 1 to 16 numerals),Description(Optional, 1 to 50 Characters)
```

#### Sample

```
1234567890123456,Marketing
```

#### Example

If the value of the field includes a comma, that field must
                                 		  be enclosed in double quotes. Use this format for fields with commas:

```
1234567890123456, "Marketing, team"
```

### Update CMC File Format

Use a text editor to create the CSV text file for updating
                                 		  client matter codes.

The following sample format shows the field length and
                                 		  string types followed by examples of CSV files for updating client matter
                                 		  codes.

```
Client Matter Code(Mandatory, 1 to 16 numerals),Description(Optional, 1 to 50 Characters)
```

#### Sample

```
1234567890123456,Marketing
```

#### Example

If the description is empty, use this format:

```
1234567890123456,
```

### FAC File Format

The following sample format and examples show the fields,
                                 		  field length, and whether the field is optional or mandatory for a text-based
                                 		  CSV file for forced authorization codes.

```
Forced Authorization Code(Mandatory, 1 to 16 numerals),Authorization Code Name (Mandatory, 1 to 50 Characters),Authorization Level(Mandatory,values range from 0 to 255)
```

#### Sample

```
1234567890123456,John FAC,251
```

### Update FAC File Format

Use a text editor to create the CSV text file for updating
                                 		  forced authorization codes.

The following sample format shows the field length and
                                 		  string types followed by examples of CSV files for updating forced
                                 		  authorization codes.

Forced Authorization Code(Mandatory, 1 to 16
                                    			 numerals),Authorization Code Name (Mandatory, 1 to 50 Characters),Authorization
                                    			 Level(Mandatory,values range from 0 to 255)

#### Sample

```
1234567890123456,John FAC,251
```

#### Example

Values you do not want to update must still include the
                                 		  delimiter. If only the Authorization Code Name has to be updated use the
                                 		  following format:

```
1234567890123456,John FAC,
```

If only the Authorization level has to be updated, use the
                                 		  following format:

```
1234567890123456,John FAC,220
```

## Create Text-Based
                        	 CSV File for Call Pickup Groups

You can
                              		  create a custom text-based CSV file for call pickup groups using a text editor,
                              		  such as Notepad++.

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Use a separate
                                          				line for each call pickup group name.

Step 2

Enter the Pickup
                                       			 Group Name, Pickup Group Number, Partition, Other Pickup Group Name-Member1...
                                       			 Other Pickup Group Name-Member10.

For example, you
                                          				may enter Marketing,7815,Part1,Marketing,Managers,Training, where Marketing is
                                          				the mandatory pickup group name, 7815 is the mandatory pickup group number.
                                          				Part1 is the partition, Marketing, Managers, and Training are the other pickup
                                          				group names that are associated to the pickup group Marketing.

Caution

Deleting
                                                      				  information and leaving it blank does not remove the information from the
                                                      				  database; a blank value does not overwrite an existing value in the database,
                                                      				  but updating the value, for example, to Sales from Marketing, from the
                                                      				  preceding examples, overwrites the existing value in the database.

Step 3

Upload the CSV file to the first node of .

While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                          Order Mark (BOM) from the Encoding drop-down.

Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                                      can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                                      Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                                      from .

Step 4

Perform one of
                                       			 the following tasks:

If you made additions or updates, insert the file in the CUCM database using BAT.

You can delete call pickup groups settings.

### CPG File Format

The following sample format and examples show the fields,
                                 		  field length, and whether the field is optional or mandatory for a text-based
                                 		  CSV file for call pickup groups.

```
Pickup Group Name(Mandatory, 1 to 50 characters),Pickup Group Number(Mandatory, 1 to 24 numerals),Partition(Optional, 1 to 50 Characters),Other Pickup Group Name-Member1... Other Pickup Group Name-Member10(Optional, 1 to 50 Characters)
```

#### Sample

```
Marketing,7815,Part1,Marketing,Managers,Training
```

#### Example

Optional values that you do not want to specify at this time
                                 		  must still include the delimiter (a comma) except for Other Pickup Group
                                 		  members.

If the Partition for a Pickup Group is blank, use the
                                 		  following format:

```
Marketing,7815,
```

### Update CPG File Format

Use a text editor to create the CSV text file for updating
                                 		  the call pickup group.

The following sample format shows the field length and
                                 		  string types followed by examples of CSV files for updating call pickup groups.

```
Pickup Group Name(Mandatory, 1 to 50 characters),Pickup Group Number(Mandatory, 1 to 24 numerals),Partition(Optional, 1 to 50 Characters),Other Pickup Group Name-Member1... Other Pickup Group Name-Member10(Optional, 1 to 50 Characters)
```

#### Sample

```
Marketing,,,Marketing,Managers,Training
```

#### Example

```
Marketing,,,Managers,Marketing,Training
```

If you do not want to update Other Pickup Group member, do
                                 		  not include the delimiter (a comma). Use the following format:

## Create Text-Based
                        	 CSV File for Remote Destination Profile

Instead of
                              		  using the BAT spreadsheet for data input when you are adding Remote Destination
                              		  Profiles (RDPs), you can create the comma-separated values (CSV) file by using
                              		  lines of ASCII text with values separated by commas. You can use a text editor
                              		  such as Notepad++.

Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Use a separate line to enter the values for each RDP that you want to add to . Keep in mind the following rules when you create the CSV data file.

Always include comma separators, even if a field is blank.

Specify the user ID if the RDP is to be associated to a user.

Consider Directory Number fields as optional only when you are creating the CSV file for use with a BAT template that has
                                                no lines. If lines are configured on the BAT RDP template, you must supply directory numbers in the CSV file for each RDP.

An error occurs when you insert a CSV file with blank lines.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node of .

## Creating Text-Based
                        	 CSV File for Phone Migration

Instead of
                              		  using the BAT spreadsheet for data input when you are migrating phones, you can
                              		  create the comma-separated values (CSV) file by using lines of ASCII text with
                              		  values separated by commas. You can use a text editor such as Notepad++.

Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Use a separate
                                       			 line to enter the values for each phone that you want to migrate. Keep in mind
                                       			 the following rules when you create the CSV data file.

Always include comma separators, even if a field is blank.

An error occurs when you insert a CSV file with blank lines.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node of .

### Phone Migration File Format

The following sample format and example shows the fields,
                                 		  field length, and whether the field is optional or mandatory for a text-based
                                 		  CSV file for phone migration.

```
Old Device Name(Mandatory, 1 to 50 characters),New Device MAC Address(Mandatory, 12 characters)Description(Optional, 1 to 50 characters).
```

#### Sample

Old Device Name,New Device MAC Address,Description

```
SEP123456789012,123333789012,Marketing
```

## Create Text-Based
                        	 CSV File for IME Trusted Element Configuration

Instead of
                              		  using the BAT spreadsheet for data input when you are inserting IME Trusted
                              		  Element Configuration, you can create the comma-separated values (CSV) file by
                              		  using lines of ASCII text with values separated by commas. You can use a text
                              		  editor such as Notepad++.

Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Use a separate
                                       			 line to enter the values for each IME Trusted Element Configuration that you
                                       			 want to add. Keep in mind the following rules when you create the CSV data
                                       			 file.

Always include comma separators, even if a field is blank.

An error occurs when you insert a CSV file with blank lines.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node server for .

### IME Trusted Element Configuration File Format

The following sample format and example shows the fields,
                                 		  field length, and whether the field is optional or mandatory for a text-based
                                 		  CSV file for IME Trusted Element Configuration.

Name (Mandatory 1 to 50 characters), Description (Optional,
                                 		  1 to128 characters), Element Type (Mandatory, 1 to 50 characters), Cisco IME
                                 		  Link Route Filter Group (Mandatory, 1 to 50 characters).

#### Sample

Name, Description, Element Type, Cisco IME Link Route Filter
                                 		  Group

```
Elem1,sample_file,Prefix,grp1
```

## Create Text-Based
                        	 CSV File for IME Trusted Group Configuration

Instead of
                              		  using the BAT spreadsheet for data input when you are inserting IME Trusted
                              		  Group Configuration, you can create the comma-separated values (CSV) file by
                              		  using lines of ASCII text with values separated by commas. You can use a text
                              		  editor such as Notepad++.

Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Use a separate
                                       			 line to enter the values for each IME Trusted Group Configuration that you want
                                       			 to add. Keep in mind the following rules when you create the CSV data file.

Always include comma separators, even if a field is blank.

An error occurs when you insert a CSV file with blank lines.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node of .

### IME Trusted Element Configuration File Format

The following sample format and example shows the fields, field length, and whether the field is optional or mandatory for
                                 a text-based CSV file for IME Trusted Group Configuration.

Name (Mandatory 1 to 50 characters), Description (Optional, 1 to128 characters), Element Type (Mandatory, 1 to 50 characters),
                                 Cisco IME Link Route Filter Group (Mandatory, T/F).

#### Sample

Name, Description, Trusted

```
grp1,sample_file,t
```

## Create Text-Based
                        	 CSV File for IME Enrolled Group Configuration

Instead of
                              		  using the BAT spreadsheet for data input when you are inserting IME Enrolled
                              		  Group Configuration, you can create the comma-separated values (CSV) file by
                              		  using lines of ASCII text with values separated by commas. You can use a text
                              		  editor such as Notepad++.

Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Use a separate
                                       			 line to enter the values for each IME Enrolled Group Configuration that you
                                       			 want to add. Keep in mind the following rules when you create the CSV data
                                       			 file.

Always include comma separators, even if a field is blank.

An error occurs when you insert a CSV file with blank lines.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node of .

### IME Enrolled Group Configuration File Format

The following sample format and example shows the fields, field length, and whether the field is optional or mandatory for
                                 a text-based CSV file for IME Enrolled Group Configuration.

Group Name (Mandatory 1 to 50 characters), Description (Optional, 1 to128 characters), Fallback Profile (Optional, 1 to 50
                                 characters), All Patterns In Group Are Aliases (Optional, T/F).

#### Sample

Group Name, Description,Fallback Profile, All Patterns In Group Are Aliases

```
Enrol_grp1,sample_file,profile1,t
```

## Create Text-Based
                        	 CSV File for IME Exclusion Group Configuration

Instead of
                              		  using the BAT spreadsheet for data input when you are inserting IME Exclusion
                              		  Group Configuration, you can create the comma-separated values (CSV) file by
                              		  using lines of ASCII text with values separated by commas. You can use a text
                              		  editor such as Notepad++.

Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Use a separate
                                       			 line to enter the values for each IME Exclusion Group Configuration that you
                                       			 want to add. Keep in mind the following rules when you create the CSV data
                                       			 file.

Always include comma separators, even if a field is blank.

An error occurs when you insert a CSV file with blank lines.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node of . See the Upload File to Server .

### IME Exclusion Group Configuration File Format

The following sample format and example shows the fields, field length, and whether the field is optional or mandatory for
                                 a text-based CSV file for IME Exclusion Group Configuration.

Group Name (Mandatory 1 to 50 characters), Description (Optional, 1 to128 characters).

#### Sample

Name,Description

```
Exclu_grp1,sample_file
```

## Create Text-Based
                        	 CSV File for Fallback Profile Configuration

Instead of
                              		  using the BAT spreadsheet for data input when you are inserting Fallback
                              		  Profile Configuration, you can create the comma-separated values (CSV) file by
                              		  using lines of ASCII text with values that are separated by commas. You can use
                              		  a text editor such as Notepad++.

Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Use a separate
                                       			 line to enter the values for each Fallback Profile Configuration that you want
                                       			 to add. Keep in mind the following rules when you create the CSV data file.

Always include comma separators, even if a field is blank.

An error occurs when you insert a CSV file with blank lines.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file to the first node of .

### Fallback Profile Configuration File Format

The following sample format and example shows the fields, field length, and whether the field is optional or mandatory for
                                 a text-based CSV file for Fallback Profile Configuration.

Name (Mandatory, 1 to 50 characters), Description (Optional, 1 to128 characters), Advertised Fallback Directory E.164 Number
                                 (Optional, 1 to16 characters), Fallback Qos Sensitivity Level (Mandatory, 1 to 2 characters), Fallback Call CSS (Mandatory,
                                 1 to2 characters), Fallback Call Answer Timer (Mandatory, 1 to2 characters), Fallback Directory Number Partition (Mandatory,
                                 1 to 50 characters), Fallback Directory Number (Mandatory, 1 to 50 characters), Number of Digits for Caller Id Partial Match
                                 (Mandatory, 1 to 2 characters).

#### Sample

Name,Description,Advertised Fallback Directory E.164 Number, Fallback Qos Sensitivity Level, Fallback Call CSS, Fallback Call
                                 Answer Timer, Fallback Directory Number Partition, Fallback Directory Number, Number of Digits for Caller Id Partial Match.

```
profile1,sample_file,+91233232,1,Trunk Reroute Calling Search Space,2,partition1,1212,1
```

## Create Text-Based
                        	 CSV File for End User CAPF Profile

Instead of
                              		  using the BAT spreadsheet for data input when you are inserting end user CAPF
                              		  profiles, you can create the comma-separated values (CSV) file by using lines
                              		  of ASCII text with values separated by commas. You can use a text editor such
                              		  as Notepad++.

Cisco recommends
                                          			 uploading Text-Based CSV files saved in the UTF-8 format only, as characters
                                          			 other than ASCII characters can be stored in this format. Using a text editor,
                                          			 such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                          			 (BOM) from the Encoding drop-down. Text-Based
                                          			 CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          			 from Cisco Unified Communications
                                             				Manager .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Use a separate
                                       			 line to enter the values for each end user CAPF profile that you want to add.
                                       			 Keep in mind the following rules when you create the CSV data file:

Always include comma separators, even if a field is blank.

An error occurs when you insert a CSV file with blank lines.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file
                              		  to the first node of Cisco Unified Communications
                                 			 Manager .

### End User CAPF Profile File Format

The following sample format and example shows the fields, field length, and whether the field is optional or mandatory for
                                 a text-based CSV file for end user CAPF profile.

Instance ID (Mandatory, 1 to 132 characters), End User ID (Mandatory, 1 to 128 characters), Certificate Operation (Mandatory,
                                 1 to 100 characters), Authentication Mode (Mandatory, 1 to 100 characters), Authentication String (Optional, 1 to 50 characters),
                                 Key Size (Mandatory, 1 to 4 characters), Operation Completes By (Mandatory, 1 to 15 characters)

#### Sample

Instance ID,End User ID,Certificate Operation,Authentication Mode,Authentication String,Key Size,Operation Completes By

```
11,user,No Pending Operation,By Existing Certificate (precedence to LSC),1234567,512,2010:1:21:12
```

## Create Text-Based
                        	 CSV File for Mobility Profile

Instead of
                              		  using the BAT spreadsheet for data input when you are inserting mobility
                              		  profiles, you can create the comma-separated values (CSV) file by using lines
                              		  of ASCII text with values that are separated by commas. You can use a text
                              		  editor such as Notepad++.

Cisco recommends
                                          			 uploading Text-Based CSV files saved in the UTF-8 format only, as characters
                                          			 other than ASCII characters can be stored in this format. Using a text editor,
                                          			 such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                          			 (BOM) from the Encoding drop-down. Text-Based
                                          			 CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          			 from Cisco Unified Communications
                                             				Manager .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

Use a separate
                                       			 line to enter the values for each mobility profile that you want to add. Keep
                                       			 in mind the following rules when you create the CSV data file:

Always include comma separators, even if a field is blank.

An error occurs when you insert a CSV file with blank lines.

Step 3

While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down.

### What to do next

Upload the CSV file
                              		  to the first node of Cisco Unified Communications
                                 			 Manager .

### Mobility Profile File Format

The following sample format and example shows the fields, field length, and whether the field is optional or mandatory for
                                 a text-based CSV file for Mobility Profile.

Mobility Profile Name (Mandatory, 1 to 50 characters), Description (Optional, 1 to128 characters), Service Access Number (Optional,
                                 1 to 50 characters), Enterprise Feature Access Number/Partition (Optional, 1 to 50 characters), Callback Caller ID (Optional,
                                 1 to 50 characters), Mobile Client Calling Option (Mandatory, 1 to 50 characters).

#### Sample

Mobility Profile Name,Description,Service Access Number,Enterprise Feature Access Number/Partition,Callback Caller Id,Mobile
                                 Client Calling Option

```
MoProfile1,testexport,2323,123456 in part1,33,Dial via Office Reverse
```

## Create Text based
                        	 CSV file for Infrastructure Devices

You can
                              		  create a CSV text file for Infrastructure Devices using a text editor, such as
                              		  Notepad++.

Cisco recommends
                                          			 uploading Text-Based CSV files saved in the UTF-8 format only, as characters
                                          			 other than ASCII characters can be stored in this format. Using a text editor,
                                          			 such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                          			 (BOM) from the Encoding drop-down. Text-Based
                                          			 CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          			 from Cisco Unified
                                             				Communications Manager .

Step 1

Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file.

Step 2

The first
                                       			 line of the CSV file must be "ACCESSPOINT OR SWITCH NAME,IPV4 ADDRESS,IPV6
                                       			 ADDRESS,BSSID,DESCRIPTION".

Step 3

Use a separate
                                       			 line to enter the values for each infrastructure device that you want to add.
                                       			 The CSV file must have the following comma delineated columns:

- Device Name

- IPv4 Address

- IPv6 Address

- BSSID

- Description

Step 4

To View sample
                                       			 csv data file, Click Bulk
                                             				  administration > Infrastructure Device > Insert Infrastructure
                                             				  Device .

Step 5

Click View
                                          				Sample File .

## Related Topics

| Note | We recommend uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters can
                                    be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                    (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                    from Unified Communications Manager. |
|---|---|

| Note | We recommend uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters can
                                       be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                       (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                       from . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Use a separate line to enter the values for each phone, IP telephony device, or user combination that you want to add to . You must create separate CSV files for each type of device. Keep in mind the following rules when you create the CSV data
                                       file. Always include comma separators, even if a field is blank. Specify the user ID if the phone is to be associated to a user. Directory Number fields are optional only when you are creating the CSV file for use with a BAT template that has no lines.
                                                If lines are configured on the BAT phone template, you must supply directory numbers in the CSV file for each device. An error occurs when you insert a CSV file with blank lines. While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                                Order Mark (BOM) from the Encoding drop-down. |

| Note | If you use a comma or double quotes as part of the value in one of
                                                			 the fields, you must enclose the entire text value with double quotation marks
                                                			 to designate it as a single value. For example, if you entered John, Bill as a text value, then you
                                                			 must enter the value as "John,Bill" . If you entered a double quote in a value, then you must replace the
                                                			 double quote with two consecutive double quotes and enclose the value with
                                                			 double quotes. For example you must enter John "Chief as “John" "Chief" . |
|---|---|

| Caution | Cisco does not recommend editing the file that is generated with the
                                             			 export utility. The system dynamically generates fields, such as Logout time
                                             			 and Login time, that must not be edited at all. You must ensure that the login
                                             			 user ID and Product Specific XML fields are accurate for them to work properly,
                                             			 and you must not edit them. Use BAT to update the product specific
                                             			 configurations. |
|---|---|

| Note | For the MAC Address, enter MAC address values or check the option for creating pseudo MAC addresses. |
|---|---|

| Note | Cisco recommends
                                          			 uploading Text-Based CSV files saved in the UTF-8 format only, as characters
                                          			 other than ASCII characters can be stored in this format. Using a text editor,
                                          			 such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                          			 (BOM) from the Encoding drop-down. Text-Based
                                          			 CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          			 from Cisco Unified Communications
                                             				Manager . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Using a separate
                                       			 line for each user, enter the values for each user that you want to add to Cisco Unified Communications
                                          				Manager . You can
                                          				associate any number of existing devices to a new user by entering the device
                                          				name of all the devices separated by a comma at the end of the record. You can
                                          				associate a directory number to a user, even if that user does not control any
                                          				device. Note An error
                                                      				  occurs if any blank lines exist in the CSV file. | Note | An error
                                                      				  occurs if any blank lines exist in the CSV file. |
| Note | An error
                                                      				  occurs if any blank lines exist in the CSV file. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | An error
                                                      				  occurs if any blank lines exist in the CSV file. |
|---|---|

| Tip | You must specify PIN and Password values, either on the CSV file or
                                          			 when using BAT for file insertion. If you want to apply individual PINs or
                                          			 passwords for each user or group of users, specify the PIN and password
                                          			 information in the CSV file. If you want to use a default PIN and password that
                                          			 all users can use, do not specify PIN or password values in the CSV file and
                                          			 instead provide this information when you use BAT to insert the CSV file in Cisco Unified Communications Manager . |
|---|---|

| Note | You must specify delimiters even if a field is blank. Refer to the
                                             			 following examples and sample CSV records when you are creating CSV files. |
|---|---|

| Note | If you use comma
                                          			 or double quotes as part of string in one of the fields, you must enclose the
                                          			 entire text string with double quotes. |
|---|---|

| Note | Cisco recommends
                                          			 uploading Text-Based CSV files saved in the UTF-8 format only, as characters
                                          			 other than ASCII characters can be stored in this format. Using a text editor,
                                          			 such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                          			 (BOM) from the Encoding drop-down. Text-Based
                                          			 CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          			 from Cisco Unified Communications
                                             				Manager . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Using a separate
                                       			 line for each user device profile, enter the values for each user device
                                       			 profile that you want to add to Cisco Unified Communications
                                          				Manager . Note An error
                                                      				  occurs if any blank lines exist in the CSV file. | Note | An error
                                                      				  occurs if any blank lines exist in the CSV file. |
| Note | An error
                                                      				  occurs if any blank lines exist in the CSV file. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | An error
                                                      				  occurs if any blank lines exist in the CSV file. |
|---|---|

| Caution | Cisco does not recommend editing the file that is generated with the
                                             			 export utility. The system dynamically generates some fields, such as Logout
                                             			 time and Login time, that must not be edited at all. You must ensure that the
                                             			 login user ID and Product Specific XML fields are accurate for them to work
                                             			 properly, and you must not edit them. Use BAT to update the product-specific
                                             			 configurations. |
|---|---|

| Note | Use True and False for settings with Boolean values. |
|---|---|

| Note | Cisco recommends
                                          			 uploading Text-Based CSV files saved in the UTF-8 format only, as characters
                                          			 other than ASCII characters can be stored in this format. Using a text editor,
                                          			 such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                          			 (BOM) from the Encoding drop-down. Text-Based
                                          			 CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          			 from Cisco Unified Communications
                                             				Manager . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Using a separate
                                       			 line for each manager-assistants association, enter the values for each
                                       			 manager-assistant that you want to add to Cisco Unified Communications
                                          				Manager . Note An error
                                                      				  occurs if any blank lines exist in the CSV file. You can assign
                                          				multiple assistants to a manager by entering the user IDs of the manager and
                                          				assistants separated by a comma at the end of the record. | Note | An error
                                                      				  occurs if any blank lines exist in the CSV file. |
| Note | An error
                                                      				  occurs if any blank lines exist in the CSV file. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | An error
                                                      				  occurs if any blank lines exist in the CSV file. |
|---|---|

| Note | Cisco recommends
                                          			 uploading Text-Based CSV files saved in the UTF-8 format only, as characters
                                          			 other than ASCII characters can be stored in this format. Using a text editor,
                                          			 such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                          			 (BOM) from the Encoding drop-down. Text-Based
                                          			 CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          			 from Cisco Unified Communications
                                             				Manager . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Using a separate
                                       			 line for each gateway, enter the values for each gateway and port that you want
                                       			 to add to Cisco Unified Communications
                                          				Manager . Note An error
                                                      				  occurs if any blank lines exist in the CSV file. | Note | An error
                                                      				  occurs if any blank lines exist in the CSV file. |
| Note | An error
                                                      				  occurs if any blank lines exist in the CSV file. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | An error
                                                      				  occurs if any blank lines exist in the CSV file. |
|---|---|

| Note | You must include comma separators even if a field is blank. Specify
                                             			 the directory number and route partition only if the port type in the Cisco
                                             			 VG200 gateway template is POTS. |
|---|---|

| Note | You must include comma separators even if a field is blank. |
|---|---|

| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Using a separate line for each gateway, enter the values for each gateway and port that you want to add to . Note An error occurs if any blank lines exist in the CSV file. | Note | An error occurs if any blank lines exist in the CSV file. |
| Note | An error occurs if any blank lines exist in the CSV file. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | An error occurs if any blank lines exist in the CSV file. |
|---|---|

| Note | You must include comma separators even if a field is blank. Specify
                                             			 the directory number and route partition only if the port type in the Cisco
                                             			 VG224 gateway template is POTS. |
|---|---|

| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from . |
|---|---|

| Step 1 | Open a text editor or any application that allows you to export or create a text-based CSV file. |
|---|---|
| Step 2 | Using a separate line for each gateway, enter the values for each gateway and port that you want to add to . Note An error occurs if any blank lines exist in the CSV file. | Note | An error occurs if any blank lines exist in the CSV file. |
| Note | An error occurs if any blank lines exist in the CSV file. |
| Step 3 | While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                       Order Mark (BOM) from the Encoding drop-down. |

| Note | An error occurs if any blank lines exist in the CSV file. |
|---|---|

| Note | You must include comma separators even if a field is blank. Specify the directory number and route partition only if the port
                                             type in the Cisco VG310 gateway template is POTS. |
|---|---|

| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from . |
|---|---|

| Step 1 | Open a text editor or any application that allows you to export or create a text-based CSV file. |
|---|---|
| Step 2 | Using a separate line for each gateway, enter the values for each gateway and port that you want to add to . Note An error occurs if any blank lines exist in the CSV file. | Note | An error occurs if any blank lines exist in the CSV file. |
| Note | An error occurs if any blank lines exist in the CSV file. |
| Step 3 | While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                       Order Mark (BOM) from the Encoding drop-down. |

| Note | An error occurs if any blank lines exist in the CSV file. |
|---|---|

| Note | You must include comma separators even if a field is blank. Specify the directory number and route partition only if the port
                                             type in the Cisco VG320 gateway template is POTS. |
|---|---|

| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from . |
|---|---|

| Step 1 | Open a text editor or any application that allows you to export or create a text-based CSV file. |
|---|---|
| Step 2 | Using a separate line for each gateway, enter the values for each gateway and port that you want to add to . Note An error occurs if any blank lines exist in the CSV file. | Note | An error occurs if any blank lines exist in the CSV file. |
| Note | An error occurs if any blank lines exist in the CSV file. |
| Step 3 | While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                       Order Mark (BOM) from the Encoding drop-down. |

| Note | An error occurs if any blank lines exist in the CSV file. |
|---|---|

| Note | You must include comma separators even if a field is blank. Specify the directory number and route partition only if the port
                                             type in the Cisco VG350 gateway template is POTS. |
|---|---|

| Note | We recommend uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters can
                                       be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                       (BOM) from the Encoding drop-down list. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                       from Unified Communications Manager. |
|---|---|

| Step 1 | Open a text editor or any application that allows you to export or create a text-based CSV file. |
|---|---|
| Step 2 | Using a separate line for each gateway, enter the values for each gateway and port that you want to add to Unified Communications
                                       Manager. Note An error occurs if any blank lines exist in the CSV file. | Note | An error occurs if any blank lines exist in the CSV file. |
| Note | An error occurs if any blank lines exist in the CSV file. |
| Step 3 | While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                       Order Mark (BOM) from the Encoding drop-down. |

| Note | An error occurs if any blank lines exist in the CSV file. |
|---|---|

| Note | We recommend uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters can
                                       be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                       (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                       from Unified Communications Manager. |
|---|---|

| Step 1 | Open a text editor or any application that allows you to export or create a text-based CSV file. |
|---|---|
| Step 2 | Using a separate line for each gateway, enter the values for each gateway and port that you want to add to Unified Communications
                                       Manager. Note An error occurs if any blank lines exist in the CSV file. | Note | An error occurs if any blank lines exist in the CSV file. |
| Note | An error occurs if any blank lines exist in the CSV file. |
| Step 3 | While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                       Order Mark (BOM) from the Encoding drop-down. |

| Note | An error occurs if any blank lines exist in the CSV file. |
|---|---|

| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from . |
|---|---|

| Step 1 | Open a text editor or any application that allows you to export or create a text-based CSV file. |
|---|---|
| Step 2 | Using a separate line for each gateway, enter the values for each gateway and port that you want to add to . Note An error occurs if any blank lines exist in the CSV file. | Note | An error occurs if any blank lines exist in the CSV file. |
| Note | An error occurs if any blank lines exist in the CSV file. |
| Step 3 | While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                       Order Mark (BOM) from the Encoding drop-down. |

| Note | An error occurs if any blank lines exist in the CSV file. |
|---|---|

| Note | You must include comma separators even if a field is blank. Specify the directory number and route partition only if the port
                                             type in the Cisco VG450 gateway template is POTS. |
|---|---|

| Note | We recommend uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters can
                                       be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                       (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                       from Unified Communications Manager. |
|---|---|

| Step 1 | Open a text editor or any application that allows you to export or create a text-based CSV file. |
|---|---|
| Step 2 | Using a separate line for each gateway, enter the values for each gateway and port that you want to add to Unified Communications
                                       Manager. Note An error occurs if any blank lines exist in the CSV file. | Note | An error occurs if any blank lines exist in the CSV file. |
| Note | An error occurs if any blank lines exist in the CSV file. |
| Step 3 | While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                       Order Mark (BOM) from the Encoding drop-down. |

| Note | An error occurs if any blank lines exist in the CSV file. |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Using a separate line for each port, enter the values for each port that you want to add to . Note An error occurs if any blank lines exist in the CSV file. | Note | An error occurs if any blank lines exist in the CSV file. |
| Note | An error occurs if any blank lines exist in the CSV file. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | An error occurs if any blank lines exist in the CSV file. |
|---|---|

| Note | BAT does not add CiscoCatalyst 6000 (FXS) gateways. It only adds or
                                          			 updates ports to an existing gateway. |
|---|---|

| Note | You must include comma separators even if a field is blank. |
|---|---|

| Note | Do not specify a partition unless you have also specified a
                                          			 directory number. |
|---|---|

| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Using a separate line for each gateway, enter the values for each gateway and port that you want to add to . Note An error occurs if any blank lines exist in the CSV file. | Note | An error occurs if any blank lines exist in the CSV file. |
| Note | An error occurs if any blank lines exist in the CSV file. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | An error occurs if any blank lines exist in the CSV file. |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Using a separate
                                       			 line for each code, create a custom Client Matter Codes (CMC) CSV file or a
                                       			 Forced Authorized Codes (FAC) CSV file, as described in the following steps: For CMC—Step 3 and Step 4 For FAC— Step 3 and Step 4 Tip Remember that
                                                      				  you must create two separate CSV files, one for CMC and one for FAC. | Tip | Remember that
                                                      				  you must create two separate CSV files, one for CMC and one for FAC. |
| Tip | Remember that
                                                      				  you must create two separate CSV files, one for CMC and one for FAC. |
| Step 3 | To create a CMC
                                       			 CSV file, enter the corresponding information, where x, y represent the
                                       			 following fields: x—The client matter code (mandatory entry for all additions, updates, and deletions) y—The description (optional if you update the entry) For example, you
                                          				may enter 5555,Acme Toys, where 5555 equals the mandatory client matter code,
                                          				and Acme Toys equals the description. |
| Step 4 | To create a FAC
                                       			 CSV file, enter the corresponding information, where x,y,z represent the
                                       			 following fields: x—The forced authorization code (mandatory entry for all additions, updates, and deletions) y—The authorization code name (optional if you update the entry) z—The authorization level (optional if you update the entry) For example, you
                                          				may enter 1234,John Smith,20, where 1234 equals the forced authorization code,
                                          				John Smith equals the authorization code name, and 20 equals the authorization
                                          				level. Caution If you add new
                                                      				  codes at the same time that you update them, make sure that you enter all
                                                      				  required information. You can change any part of an existing record, but you
                                                      				  must include the code; for example, the forced authorization code or client
                                                      				  matter code. Deleting information and leaving it blank does not remove the
                                                      				  information from the database; a blank value does not overwrite an existing
                                                      				  value in the database, but, updating the value, for example, to Acme Toys,
                                                      				  Inc., or John L. Smith from the preceding examples, overwrites the existing
                                                      				  value in the database. | Caution | If you add new
                                                      				  codes at the same time that you update them, make sure that you enter all
                                                      				  required information. You can change any part of an existing record, but you
                                                      				  must include the code; for example, the forced authorization code or client
                                                      				  matter code. Deleting information and leaving it blank does not remove the
                                                      				  information from the database; a blank value does not overwrite an existing
                                                      				  value in the database, but, updating the value, for example, to Acme Toys,
                                                      				  Inc., or John L. Smith from the preceding examples, overwrites the existing
                                                      				  value in the database. |
| Caution | If you add new
                                                      				  codes at the same time that you update them, make sure that you enter all
                                                      				  required information. You can change any part of an existing record, but you
                                                      				  must include the code; for example, the forced authorization code or client
                                                      				  matter code. Deleting information and leaving it blank does not remove the
                                                      				  information from the database; a blank value does not overwrite an existing
                                                      				  value in the database, but, updating the value, for example, to Acme Toys,
                                                      				  Inc., or John L. Smith from the preceding examples, overwrites the existing
                                                      				  value in the database. |
| Step 5 | Upload the CSV file to the first node of . While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                          Order Mark (BOM) from the Encoding drop-down. Note Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                                      can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                                      Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                                      from . | Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                                      can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                                      Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                                      from . |
| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                                      can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                                      Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                                      from . |
| Step 6 | Perform one of
                                       			 the following tasks: If you made additions or updates, insert the file in the CUCM database using BAT. You can delete code settings. Note You cannot
                                                      				  perform insert and update operations simultaneously with the same CSV file. You
                                                      				  have to create separate CSV files for insert and update. | Note | You cannot
                                                      				  perform insert and update operations simultaneously with the same CSV file. You
                                                      				  have to create separate CSV files for insert and update. |
| Note | You cannot
                                                      				  perform insert and update operations simultaneously with the same CSV file. You
                                                      				  have to create separate CSV files for insert and update. |

| Tip | Remember that
                                                      				  you must create two separate CSV files, one for CMC and one for FAC. |
|---|---|

| Caution | If you add new
                                                      				  codes at the same time that you update them, make sure that you enter all
                                                      				  required information. You can change any part of an existing record, but you
                                                      				  must include the code; for example, the forced authorization code or client
                                                      				  matter code. Deleting information and leaving it blank does not remove the
                                                      				  information from the database; a blank value does not overwrite an existing
                                                      				  value in the database, but, updating the value, for example, to Acme Toys,
                                                      				  Inc., or John L. Smith from the preceding examples, overwrites the existing
                                                      				  value in the database. |
|---|---|

| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                                      can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                                      Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                                      from . |
|---|---|

| Note | You cannot
                                                      				  perform insert and update operations simultaneously with the same CSV file. You
                                                      				  have to create separate CSV files for insert and update. |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. Use a separate
                                          				line for each call pickup group name. |
|---|---|
| Step 2 | Enter the Pickup
                                       			 Group Name, Pickup Group Number, Partition, Other Pickup Group Name-Member1...
                                       			 Other Pickup Group Name-Member10. For example, you
                                          				may enter Marketing,7815,Part1,Marketing,Managers,Training, where Marketing is
                                          				the mandatory pickup group name, 7815 is the mandatory pickup group number.
                                          				Part1 is the partition, Marketing, Managers, and Training are the other pickup
                                          				group names that are associated to the pickup group Marketing. Caution Deleting
                                                      				  information and leaving it blank does not remove the information from the
                                                      				  database; a blank value does not overwrite an existing value in the database,
                                                      				  but updating the value, for example, to Sales from Marketing, from the
                                                      				  preceding examples, overwrites the existing value in the database. | Caution | Deleting
                                                      				  information and leaving it blank does not remove the information from the
                                                      				  database; a blank value does not overwrite an existing value in the database,
                                                      				  but updating the value, for example, to Sales from Marketing, from the
                                                      				  preceding examples, overwrites the existing value in the database. |
| Caution | Deleting
                                                      				  information and leaving it blank does not remove the information from the
                                                      				  database; a blank value does not overwrite an existing value in the database,
                                                      				  but updating the value, for example, to Sales from Marketing, from the
                                                      				  preceding examples, overwrites the existing value in the database. |
| Step 3 | Upload the CSV file to the first node of . While saving your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select encoding as UTF-8 without Byte
                                          Order Mark (BOM) from the Encoding drop-down. Note Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                                      can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                                      Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                                      from . | Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                                      can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                                      Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                                      from . |
| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                                      can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                                      Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                                      from . |
| Step 4 | Perform one of
                                       			 the following tasks: If you made additions or updates, insert the file in the CUCM database using BAT. You can delete call pickup groups settings. |

| Caution | Deleting
                                                      				  information and leaving it blank does not remove the information from the
                                                      				  database; a blank value does not overwrite an existing value in the database,
                                                      				  but updating the value, for example, to Sales from Marketing, from the
                                                      				  preceding examples, overwrites the existing value in the database. |
|---|---|

| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                                      can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                                      Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                                      from . |
|---|---|

| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Use a separate line to enter the values for each RDP that you want to add to . Keep in mind the following rules when you create the CSV data file. Always include comma separators, even if a field is blank. Specify the user ID if the RDP is to be associated to a user. Consider Directory Number fields as optional only when you are creating the CSV file for use with a BAT template that has
                                                no lines. If lines are configured on the BAT RDP template, you must supply directory numbers in the CSV file for each RDP. An error occurs when you insert a CSV file with blank lines. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Use a separate
                                       			 line to enter the values for each phone that you want to migrate. Keep in mind
                                       			 the following rules when you create the CSV data file. Always include comma separators, even if a field is blank. An error occurs when you insert a CSV file with blank lines. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Use a separate
                                       			 line to enter the values for each IME Trusted Element Configuration that you
                                       			 want to add. Keep in mind the following rules when you create the CSV data
                                       			 file. Always include comma separators, even if a field is blank. An error occurs when you insert a CSV file with blank lines. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Use a separate
                                       			 line to enter the values for each IME Trusted Group Configuration that you want
                                       			 to add. Keep in mind the following rules when you create the CSV data file. Always include comma separators, even if a field is blank. An error occurs when you insert a CSV file with blank lines. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Use a separate
                                       			 line to enter the values for each IME Enrolled Group Configuration that you
                                       			 want to add. Keep in mind the following rules when you create the CSV data
                                       			 file. Always include comma separators, even if a field is blank. An error occurs when you insert a CSV file with blank lines. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Use a separate
                                       			 line to enter the values for each IME Exclusion Group Configuration that you
                                       			 want to add. Keep in mind the following rules when you create the CSV data
                                       			 file. Always include comma separators, even if a field is blank. An error occurs when you insert a CSV file with blank lines. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters
                                          can be stored in this format. Using a text editor, such as Notepad++, you can select encoding as UTF-8 without Byte Order
                                          Mark (BOM) from the Encoding drop-down. Text-Based CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          from . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Use a separate
                                       			 line to enter the values for each Fallback Profile Configuration that you want
                                       			 to add. Keep in mind the following rules when you create the CSV data file. Always include comma separators, even if a field is blank. An error occurs when you insert a CSV file with blank lines. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | Cisco recommends
                                          			 uploading Text-Based CSV files saved in the UTF-8 format only, as characters
                                          			 other than ASCII characters can be stored in this format. Using a text editor,
                                          			 such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                          			 (BOM) from the Encoding drop-down. Text-Based
                                          			 CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          			 from Cisco Unified Communications
                                             				Manager . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Use a separate
                                       			 line to enter the values for each end user CAPF profile that you want to add.
                                       			 Keep in mind the following rules when you create the CSV data file: Always include comma separators, even if a field is blank. An error occurs when you insert a CSV file with blank lines. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | Cisco recommends
                                          			 uploading Text-Based CSV files saved in the UTF-8 format only, as characters
                                          			 other than ASCII characters can be stored in this format. Using a text editor,
                                          			 such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                          			 (BOM) from the Encoding drop-down. Text-Based
                                          			 CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          			 from Cisco Unified Communications
                                             				Manager . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | Use a separate
                                       			 line to enter the values for each mobility profile that you want to add. Keep
                                       			 in mind the following rules when you create the CSV data file: Always include comma separators, even if a field is blank. An error occurs when you insert a CSV file with blank lines. |
| Step 3 | While saving
                                       			 your CSV file, choose to save it as UTF-8 encoded. In Notepad++, you can select
                                       			 encoding as UTF-8 without Byte Order Mark (BOM) from the Encoding drop-down. |

| Note | Cisco recommends
                                          			 uploading Text-Based CSV files saved in the UTF-8 format only, as characters
                                          			 other than ASCII characters can be stored in this format. Using a text editor,
                                          			 such as Notepad++, you can select encoding as UTF-8 without Byte Order Mark
                                          			 (BOM) from the Encoding drop-down. Text-Based
                                          			 CSV files saved in formats other than UTF-8 may render garbled when downloaded
                                          			 from Cisco Unified
                                             				Communications Manager . |
|---|---|

| Step 1 | Open a text
                                       			 editor or any application that allows you to export or create a text-based CSV
                                       			 file. |
|---|---|
| Step 2 | The first
                                       			 line of the CSV file must be "ACCESSPOINT OR SWITCH NAME,IPV4 ADDRESS,IPV6
                                       			 ADDRESS,BSSID,DESCRIPTION". |
| Step 3 | Use a separate
                                       			 line to enter the values for each infrastructure device that you want to add.
                                       			 The CSV file must have the following comma delineated columns: Device Name IPv4 Address IPv6 Address BSSID Description |
| Step 4 | To View sample
                                       			 csv data file, Click Bulk
                                             				  administration > Infrastructure Device > Insert Infrastructure
                                             				  Device . The Insert
                                          				Infrastructure Device Configuration window opens. |
| Step 5 | Click View
                                          				Sample File . |