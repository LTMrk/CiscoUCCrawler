---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-14su1-cucm-b-bulk-administration-guide-14su1-cucm-b-bulk-administra-654cd427cb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/14SU1/cucm_b_bulk-administration-guide-14SU1/cucm_b_bulk-administration-guide-1251su2_chapter_010010.html
retrieved_at: 2026-08-21T09:09:05.605060+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: October 27, 2021

Chapter: User Updates

## Chapter: User Updates

# User Updates

This chapter provides information about updating existing user
                        		records in the Cisco Unified Communications Manager database.

## Update User Information Using CSV Data File

You can update existing user information that is in the database using a comma-separated value (CSV) data file you create using the Bulk Administration (BAT) spreadsheet, or you
                              can update a user file format using a custom text-based CSV file.

You can retain existing user information and settings that were previously stored in the Unified CM directory.

You do not require a user template for the update users
                                          				  transaction using a custom text-based CSV file. If you choose a user template, the system takes the fields that are
                                          not provided in
                                          				  the CSV from the template for the update or else these fields are ignored. Also, if you specify another value for fields
                                          to be ignored (for example, 
                                          				  #), then the fields with the value 
                                          				  # are ignored, because blank is not a value to
                                          				  be ignored for such fields.

The Bulk Administration Tool (BAT) cannot be used to disassociate devices that are already associated to an end user. If you
                                          manually delete a controlled device from an exported end user record and then insert the modified user record back in to the
                                          Cisco Unified Communications Manager database as a custom CSV data file, the insertion appears as successful when you check
                                          the job results using Bulk Administration > Job Scheduler . However, the controlled device is still listed on the end-user page.

Step 1

Create a CSV data file to define
                                       			 individual values for each user that you want to update.

Step 2

Use BAT to insert the updated user records that are in the database.

### Retain Existing User Information During Update

```
userid,#,department,,,123456789012,
```

To identify the value to use to retain a stored value, use
                                 		  the following procedure.

Step 1

Choose Bulk
                                                				  Administration > Users > Update
                                                				  Users .

The User Update Configuration window appears.

Step 2

Notice the Value for fields to be ignored field . When you insert
                                          			 the CSV data file with the updated user values, you must enter the symbol that
                                          			 you used to retain values in this box.

Step 3

Decide the symbol that you want to use for retaining values.

Step 4

Enter this value that is in the Value for fields to be ignored
                                          			 field into the BAT spreadsheet box.

Step 5

Use this symbol in BAT spreadsheet fields for any values that you
                                          			 want to retain.

### Create User Update CSV Data File Using BAT Spreadsheet

You can create a CSV data file using the BAT spreadsheet to
                                 		  update a group of existing users.

After you add lines in the BAT spreadsheet, you can
                                 		  export the content to a CSV formatted data file. A default filename is assigned
                                 		  to the exported CSV formatted update users data file:

Update_Users-timestamp.txt

where <timestamp> represents the precise date and time
                                 		  that the file was created.

The system saves the file with a default filename to C:\XlsDataFiles\ , or you can save the file to
                                 		  another existing folder on your local workstation. You can rename the CSV
                                 		  formatted data file after you save the exported file to your local workstation.
                                 		  If you enter a comma in one of the fields, BAT.xlt encloses that field entry in
                                 		  double quotes when you export to BAT format.

You cannot upload a CSV filename that contains a comma (for example, abcd,e.txt) to the server.

If you enter a blank row in the spreadsheet, the system treats the
                                             			 empty row as the end of the file. Data that you enter after a blank line is not converted to the BAT format.

The Bulk Administration Tool (BAT) cannot be used to disassociate devices that are already associated to an end user. If you
                                 manually delete a controlled device from an exported end-user record and then insert the modified user record back in to the Unified Communications Manager database as a custom CSV data file, the insertion appears successful when you check the job results using Bulk Administration > Job Scheduler . However, the controlled device is still listed on the End User Configuration window in Cisco Unified Communications Manager Administration.

Step 1

Download and open the BAT.xlt file.

Step 2

When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities.

Step 3

To add user information, click the Update Users tab at the bottom of the
                                          			 spreadsheet.

Step 4

Complete all mandatory fields and any relevant, optional fields.

Step 5

In the Value for fields to be ignored field, enter the symbol that
                                          			 you will use to tell BAT that you want to keep the value that was previously
                                          			 stored in the DC directory. Enter the same value in the value of the field you
                                          			 want to retain.

Step 6

To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 file, click Export to BAT .

The system saves the file to C:\XlsDataFiles\ with the default filename Update_Users-timestamp.txt or you can
                                             				use Browse to save the file to another existing folder
                                             				on your local workstation.

For information about how to read the CSV data file, click the View Sample File link in the Update Users window in BAT.

#### What to do next

You must upload the CSV data file to the first node of the Unified CM server, so BAT can access the CSV data file.

### BAT Spreadsheet
                           	 Update User Data Field Descriptions

The following
                                 		  table provides the field descriptions for updating user details in the BAT
                                 		  spreadsheet.

Field

Description

User ID

Enter the
                                             					 last name, from 1 to 128 characters, of the phone user.

Manager User
                                             					 ID

Enter
                                             					 manager user ID, up to 128 characters, for the user of this phone.

Password

Enter the
                                             					 password, up to 128 characters, that the user needs to access the Cisco IP Phone Configuration window.

You must
                                             					 specify the Password either in the CSV data file or by using the BAT user
                                             					 interface when you add the user template. If you want to apply individual
                                             					 passwords for each user or groups of users, specify the password information in
                                             					 the CSV data file. If you want to use a default password for all users, provide
                                             					 the default password when you insert the users in BAT.

Department

Enter the
                                             					 department number, up to 64 characters, for the user of this phone.

Default
                                             					 Profile

Enter the
                                             					 default profile for this user and device, up to 50 characters. You can choose
                                             					 the user device profile from the list of existing UDPs in Unified CM Administration that appears in BAT.

User Locale

Enter the
                                             					 language and country set, up to 50 characters, that you want to associate with
                                             					 this user. Your choice determines which cultural-dependent attributes exist for
                                             					 this user and which language displays in the Unified CM user
                                             					 windows and phones.

Password

Enter the
                                             					 password, up to 128 characters, that the user needs to access the Cisco IP Phone Configuration window.

You must
                                             					 specify the password either in the CSV data file or by using the BAT user
                                             					 interface during user template addition. If you want to apply individual
                                             					 passwords for each user or groups of users, specify the password information in
                                             					 the CSV data file. If you want to use a default password for all users, provide
                                             					 the default password when you insert the users in BAT.

PIN

Enter the
                                             					 personal identification number (PIN), up to 128 numerals, to be used for
                                             					 extension mobility.

You must
                                             					 enter a PIN either in the CSV data file or by using the BAT user interface
                                             					 during user template addition. If you want to apply individual PINs for each
                                             					 user or groups of users, specify the PIN in the CSV data file. To use a default
                                             					 PIN that all users can use, provide a default PIN when you insert the users in
                                             					 BAT.

Telephone
                                             					 Number

Enter the
                                             					 telephone number, up to 64 numerals, for the primary extension (usually Line 1)
                                             					 for the phone.

Primary
                                             					 Extension

This field
                                             					 appears after you add the user and represents the primary directory number for
                                             					 the user. You choose no primary line when you associate devices to the user.
                                             					 Users can have multiple lines on their phones.

If you
                                             					 configure the system for Unity Integration, the Create Voice Mailbox link
                                             					 appears.

Associated
                                             					 PC

This field,
                                             					 which is required for Cisco SoftPhone and Unified CM Attendant Console users, displays after the user is added.

IPCC
                                             					 Extension

Enter an IPCC extension, up to 50 characters, for this user.

Mail ID

Enter the user e-mail address up to 255 characters.

BLF Presence
                                             					 Group

Enter the
                                             					 BLF presence group that watches the status of the database number, the presence
                                             					 entity.

For
                                             					 information about the BLF Presence feature, see the Feature Configuration Guide for Cisco Unified
                                                						Communications Manager .

SUBSCRIBE
                                             					 Calling Search Space

All calling search spaces that you configure in Unified CM Administration appear in the SUBSCRIBE Calling Search Space drop-down list box.

The SUBSCRIBE Calling Search Space determines how Unified CM routes the Presence subscription requests that come from the user. To configure a calling search space specifically for this
                                             purpose, you configure a calling search space as you do all calling search spaces ( Call Routing > Class Control > Calling Search Space ).

To set up a
                                             					 calling search space, see the Cisco Unified Communications Manager Online Help .

Digest
                                             					 Credentials

When you configure digest authentication for phones that are running SIP, Unified CM challenges the identity of the phone every time the phone sends a SIP request to Unified Communications Manager . The digest credentials that you enter in this field is associated with the phone when you choose a digest user in the Phone Configuration window.

Enter a
                                             					 string of up to 128 alphanumeric characters.

For more information about digest authentication, see the Cisco Unified Communications Manager Security Guide .

User Group

Enter the
                                             					 user group to which the user belongs.

The User Group fields appear when you set the Number of User Groups field to greater than zero.

Directory
                                             					 URI

Enter the
                                             					 primary directory URI that you want to associate to this user's primary
                                             					 extension. Follow the username@host format. Enter a username of up to 47
                                             					 alphanumeric characters. For the host address, enter an IPv4 address or fully
                                             					 qualified domain name.

Within Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when you use Bulk Administration
                                                         to import a CSV file that contains directory URIs with embedded double quotes and commas, you must use enclose the entire
                                                         directory URI in double quotes and escape the embedded double quotes with a double quote. For example, the Jared, "Jerry",Smith@test.com
                                                         directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the CSV file.

Self-Service User ID

The Self-Service User ID is a DTMF digit string that is used to identify a user (usually same as the user directory number).

User
                                             					 Profile

The User
                                             					 Profile is a profile that collects settings to share across a group of users.
                                             					 This profile is used when you create new devices.

EM MAX LOGIN TIME

Enter the maximum login time for Extension Mobility and Extension Mobility Cross Cluster users. Enter the value in minutes.The
                                             range of the value is from 0 to 10080 minutes (7 days).

## Update User
                        	 Information in Cisco Unified Communications Manager Directory

You can update a group of user records in the Cisco Unified Communications Manager directory.

### Before you begin

You must
                              		  have a .csv data file with updated user information.

Step 1

Choose Bulk
                                             				  Administration > Users > Update Users > Custom
                                             				  File .

The User
                                             				  Update Configuration window appears.

Step 2

From the File
                                          				Name drop-down list box, choose the .csv data file that you created
                                       			 for this bulk transaction.

Click View
                                                         					 File to view the uploaded .csv data file.

Click View Sample
                                                         					 File to view a sample .csv data file.

Step 3

From the User
                                          				Template Name drop-down list box, choose the user template that you
                                       			 created for this bulk transaction.

Step 4

In the Value
                                          				for fields to be ignored field, enter the symbol that you want to
                                       			 tell Unified CM Bulk Administration Tool to retain the value that was
                                       			 previously stored in the DC directory.

The value that
                                                      				  you enter in the .csv file for updating users overrides the values that are
                                                      				  provided in the user template.

Step 5

In the Job
                                          				Information area, enter the Job description.

Step 6

Choose a method
                                       			 to update user records. Do one of the following:

- Select Run
                                             				  Immediately to update user records immediately.

- Select Run
                                             				  Later to insert the user records at a later time.

Step 7

To create a job
                                       			 for updating the user records, click Submit .

## User Update Settings

Values that appear in some fields display from . You must configure these values by using .

Be aware that some fields have two check boxes. The first check box determines if you need to update the field; the second
                                          check box determines the value (checked or unchecked) to use for the field.

Tip

Check the first check box if you need to update the field and the second check box to apply a checked value to the users you
                                          select. For example, if you check the first box for Home Cluster and leave the second one unchecked, you update users with
                                          an unchecked value for Home Cluster.

The following table provides descriptions for
                                 all possible fields when you update users with the Query option.

User Information

Manager User ID

Enter manager user ID, up to 128 characters, for the user of this phone.

Department

Enter the department number, up to 64 characters, for the user of this phone.

Associated PC

This field, which is required for Cisco SoftPhone and Cisco Unified Communications Manager Attendant Console users, displays after you add the user.

User Locale

Choose the language and country set that you want to associate with this user from the drop-down list. Your choice determines
                                          which cultural-dependent attributes exist for this user and which language displays in the Cisco Unified Communications Manager user windows and phones.

Digest Credentials

When you configure digest authentication for phones that are running, Cisco Unified Communications Manager challenges the identity of the phone every time the phone sends a SIP request to Cisco Unified Communications Manager . The digest credentials that you enter in this field get associated with the phone when you choose a digest user in the Phone
                                          Configuration window.

Enter a string of up to 128 alphanumeric characters.

For more information on digest authentication, see the Cisco Unified Communications Manager Security Guide .

Confirm Digest Credentials

To confirm that you entered the digest credentials correctly, reenter the credentials in this field.

Service Setting

Home Cluster

Check the check box if the end user is associated with this cluster. The end user must be associated with one cluster
                                          within the enterprise.

IM and Presence feature does not function properly if an end user is associated with more than one home cluster.

Enable  User for Unified CM IM and Presence

Check the  check box to enable the end user (on the home cluster) for IM and Presence feature. Configure IM and Presence feature
                                          in the associated service profile.

You can only enable IM and Presence feature for users that have this Unified CM cluster marked as their home cluster.

Tip

Use the User Management > User Settings > UC Service menu to configure the IM and Presence feature.

Assigned Presence Server

Assign the end user to an server that is installed in the cluster if the system is nonbalanced. The server you specify using the Bulk Administration
                                          Tool must be part of a Presence Redundancy Group.

For clusters that have the user assignment mode for the IM and Presence server set to balanced or active-standby, user assignments
                                          that are made using the Bulk Administration Tool override the automatic user assignments.

UC Service Profile

Select a UC service profile from the drop-down list box to associate with end users.

Use the User Management > User Settings > Service Profile menu to set up service profiles for end users.

Include Meeting Information in Presence (Requires Exchange Presence Gateway to be configured on CUCM IM and Presence server.)

Check this check box to create a sync between CUCM IM and Presence server so that  it can include the meeting information
                                          under the  Presence feature.

You can only access this field if Home Cluster and Enable User for Unified CM IM and Presence is enabled.

Extension Mobility

BLF Presence Group

From the drop-down list, choose the BLF presence group that watches the status of the directory number, the presence entity.

SUBSCRIBE Calling Search Space

All calling search spaces that you configure in Cisco Unified Communications Manager Administration display in the SUBSCRIBE Calling Search Space drop-down list.

The SUBSCRIBE Calling Search Space determines how Cisco Unified Communications Manager routes the Presence subscription requests that come from the end user. Use the Call Routing > Class Control > Calling Search Space menu to configure a calling search space specifically for this purpose.

Maximum Login Time (HHH:MM)

Enter the maximum login time in the HHH:MM format to configure maximum login time for Extension Mobility and Extension Mobility
                                          Cross Cluster users.

The value ranges from 00:01 to 168:00 hours.

For example: 168:00, 25:16, 025:16, :30 or 00:30.

Allow Control of Device from CTI

Check this check box to allow CTI to control and monitor this device.

If the associated directory number specifies a shared line, the check box should be checked as long as at least one associated
                                          device specifies a combination of device type and protocol that CTI supports.

Enable Extension Mobility Cross Cluster

Check this check box to enable the Extension Mobility Cross Cluster CSS setting that gets used as the device CSS of the remote
                                          phone when the user selects this device profile during the EMCC login.

Mobility Information

Enable Mobility

Check this check box to activate Mobile Connect, which allows the user to manage calls by using a single phone number and
                                          to pick up and manage calls on the desk phone and mobile phone.

Enable Mobile Voice Access

Check this check box to allow the user to access the Mobile Voice Access integrated voice response (IVR) system to initiate
                                          Mobile Connect calls and activate or deactivate Mobile Connect capabilities.

Maximum Wait Time for Desk Pickup

Enter the maximum wait time, up to 5 numerals, for this user.

This indicates the maximum time that is permitted to pass before the user pickup a call that is transferred from the mobile
                                          phone to the desktop phone.

Remote Destination Limit

Enter the maximum number of phones, up to 2 numerals, to which the user is permitted to transfer calls from the desk phone.

Job Information

Job Description

Enter the job description.

Run Immediately

Click this radio button to schedule and immediately activate the update users job.

Run Later (To schedule and activate this job, use Job Scheduler page.)

Click this radio button to schedule and activate the update users job later.

### Update Users Using Query

Use this procedure to create a query to locate users to update. After locating users, you must select the update parameters.

#### Before you begin

To update all users, select Find and do not specify a query.

Step 1

Select Bulk Administration > Users > Update Users > Query

The Update Users Query window appears.

Step 2

From the first Find Phone where drop-down list, select one of the following criteria:

Last Name

First Name

User ID

Manager

Department

Has Home Cluster Enabled

Does not have Home Cluster Enabled

Has IM and Presence Enabled

Does not have IM and Presence Enabled

Step 3

From the second Find Users where drop-down list, select one of the following criteria:

begins with

contains

is exactly

ends with

is empty

is not empty

Step 4

Specify the appropriate search text, if applicable.

Tip

To find all users that are registered in the database, select Find without entering any search text.

Tip

To further define your query and to add multiple filters, click the plus (+) button and repeat step 2 and step 3.

Step 5

Select Find .

A list of discovered users appears. The Update Users window displays the details of the users that you select.

#### What to do next

Select update parameters for the user.

### Select Update Parameters for User Query

After you locate the users to update, use this procedure to select the parameters and define values for updating those users.

Step 1

In the Update Users Query window, select Next .

If you want to change the type of query, select Back .

The Update Users shows the type of query that you select.

Step 2

Check the check box to the left of the field that you want to update.

This selection tells BAT to overwrite the existing value for the field.

BAT updates only those fields for which you check the update check box.

Step 3

Update the required user parameters. See the "User update settings" topic.

Step 4

In the Job Information area , enter the job description.

Step 5

Select one of the following methods to update user records:

Select Run Immediately to update users immediately.

Select Run Later to update users at a later time.

Step 6

Select Submit .

This action creates a job for updating the records.

Use the Job Scheduler option in the Bulk Administration main menu to schedule and activate this job.

## Topics Related to User Updates

| Note | You do not require a user template for the update users
                                          				  transaction using a custom text-based CSV file. If you choose a user template, the system takes the fields that are
                                          not provided in
                                          				  the CSV from the template for the update or else these fields are ignored. Also, if you specify another value for fields
                                          to be ignored (for example, 
                                          				  #), then the fields with the value 
                                          				  # are ignored, because blank is not a value to
                                          				  be ignored for such fields. The Bulk Administration Tool (BAT) cannot be used to disassociate devices that are already associated to an end user. If you
                                          manually delete a controlled device from an exported end user record and then insert the modified user record back in to the
                                          Cisco Unified Communications Manager database as a custom CSV data file, the insertion appears as successful when you check
                                          the job results using Bulk Administration > Job Scheduler . However, the controlled device is still listed on the end-user page. |
|---|---|

| Step 1 | Create a CSV data file to define
                                       			 individual values for each user that you want to update. |
|---|---|
| Step 2 | Use BAT to insert the updated user records that are in the database. |

| Step 1 | Choose Bulk
                                                				  Administration > Users > Update
                                                				  Users . The User Update Configuration window appears. |
|---|---|
| Step 2 | Notice the Value for fields to be ignored field . When you insert
                                          			 the CSV data file with the updated user values, you must enter the symbol that
                                          			 you used to retain values in this box. |
| Step 3 | Decide the symbol that you want to use for retaining values. |
| Step 4 | Enter this value that is in the Value for fields to be ignored
                                          			 field into the BAT spreadsheet box. |
| Step 5 | Use this symbol in BAT spreadsheet fields for any values that you
                                          			 want to retain. |

| Note | You cannot upload a CSV filename that contains a comma (for example, abcd,e.txt) to the server. If you enter a blank row in the spreadsheet, the system treats the
                                             			 empty row as the end of the file. Data that you enter after a blank line is not converted to the BAT format. |
|---|---|

| Step 1 | Download and open the BAT.xlt file. |
|---|---|
| Step 2 | When prompted, click Enable Macros to use the spreadsheet
                                          			 capabilities. |
| Step 3 | To add user information, click the Update Users tab at the bottom of the
                                          			 spreadsheet. |
| Step 4 | Complete all mandatory fields and any relevant, optional fields. Each column heading specifies the length of the field and whether
                                          			 it is required or optional. For field descriptions, see Table 1 . |
| Step 5 | In the Value for fields to be ignored field, enter the symbol that
                                          			 you will use to tell BAT that you want to keep the value that was previously
                                          			 stored in the DC directory. Enter the same value in the value of the field you
                                          			 want to retain. |
| Step 6 | To transfer the data from the BAT Excel spreadsheet into a CSV
                                          			 file, click Export to BAT . The system saves the file to C:\XlsDataFiles\ with the default filename Update_Users-timestamp.txt or you can
                                             				use Browse to save the file to another existing folder
                                             				on your local workstation. For information about how to read the CSV data file, click the View Sample File link in the Update Users window in BAT. |

| Field | Description |
|---|---|
| User ID | Enter the
                                             					 last name, from 1 to 128 characters, of the phone user. |
| Manager User
                                             					 ID | Enter
                                             					 manager user ID, up to 128 characters, for the user of this phone. |
| Password | Enter the
                                             					 password, up to 128 characters, that the user needs to access the Cisco IP Phone Configuration window. You must
                                             					 specify the Password either in the CSV data file or by using the BAT user
                                             					 interface when you add the user template. If you want to apply individual
                                             					 passwords for each user or groups of users, specify the password information in
                                             					 the CSV data file. If you want to use a default password for all users, provide
                                             					 the default password when you insert the users in BAT. |
| Department | Enter the
                                             					 department number, up to 64 characters, for the user of this phone. |
| Default
                                             					 Profile | Enter the
                                             					 default profile for this user and device, up to 50 characters. You can choose
                                             					 the user device profile from the list of existing UDPs in Unified CM Administration that appears in BAT. |
| User Locale | Enter the
                                             					 language and country set, up to 50 characters, that you want to associate with
                                             					 this user. Your choice determines which cultural-dependent attributes exist for
                                             					 this user and which language displays in the Unified CM user
                                             					 windows and phones. |
| Password | Enter the
                                             					 password, up to 128 characters, that the user needs to access the Cisco IP Phone Configuration window. You must
                                             					 specify the password either in the CSV data file or by using the BAT user
                                             					 interface during user template addition. If you want to apply individual
                                             					 passwords for each user or groups of users, specify the password information in
                                             					 the CSV data file. If you want to use a default password for all users, provide
                                             					 the default password when you insert the users in BAT. |
| PIN | Enter the
                                             					 personal identification number (PIN), up to 128 numerals, to be used for
                                             					 extension mobility. You must
                                             					 enter a PIN either in the CSV data file or by using the BAT user interface
                                             					 during user template addition. If you want to apply individual PINs for each
                                             					 user or groups of users, specify the PIN in the CSV data file. To use a default
                                             					 PIN that all users can use, provide a default PIN when you insert the users in
                                             					 BAT. |
| Telephone
                                             					 Number | Enter the
                                             					 telephone number, up to 64 numerals, for the primary extension (usually Line 1)
                                             					 for the phone. |
| Primary
                                             					 Extension | This field
                                             					 appears after you add the user and represents the primary directory number for
                                             					 the user. You choose no primary line when you associate devices to the user.
                                             					 Users can have multiple lines on their phones. If you
                                             					 configure the system for Unity Integration, the Create Voice Mailbox link
                                             					 appears. |
| Associated
                                             					 PC | This field,
                                             					 which is required for Cisco SoftPhone and Unified CM Attendant Console users, displays after the user is added. |
| IPCC
                                             					 Extension | Enter an IPCC extension, up to 50 characters, for this user. |
| Mail ID | Enter the user e-mail address up to 255 characters. |
| BLF Presence
                                             					 Group | Enter the
                                             					 BLF presence group that watches the status of the database number, the presence
                                             					 entity. For
                                             					 information about the BLF Presence feature, see the Feature Configuration Guide for Cisco Unified
                                                						Communications Manager . |
| SUBSCRIBE
                                             					 Calling Search Space | All calling search spaces that you configure in Unified CM Administration appear in the SUBSCRIBE Calling Search Space drop-down list box. The SUBSCRIBE Calling Search Space determines how Unified CM routes the Presence subscription requests that come from the user. To configure a calling search space specifically for this
                                             purpose, you configure a calling search space as you do all calling search spaces ( Call Routing > Class Control > Calling Search Space ). To set up a
                                             					 calling search space, see the Cisco Unified Communications Manager Online Help . |
| Digest
                                             					 Credentials | When you configure digest authentication for phones that are running SIP, Unified CM challenges the identity of the phone every time the phone sends a SIP request to Unified Communications Manager . The digest credentials that you enter in this field is associated with the phone when you choose a digest user in the Phone Configuration window. Enter a
                                             					 string of up to 128 alphanumeric characters. For more information about digest authentication, see the Cisco Unified Communications Manager Security Guide . |
| User Group | Enter the
                                             					 user group to which the user belongs. Note The User Group fields appear when you set the Number of User Groups field to greater than zero. | Note | The User Group fields appear when you set the Number of User Groups field to greater than zero. |
| Note | The User Group fields appear when you set the Number of User Groups field to greater than zero. |
| Directory
                                             					 URI | Enter the
                                             					 primary directory URI that you want to associate to this user's primary
                                             					 extension. Follow the username@host format. Enter a username of up to 47
                                             					 alphanumeric characters. For the host address, enter an IPv4 address or fully
                                             					 qualified domain name. Note Within Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when you use Bulk Administration
                                                         to import a CSV file that contains directory URIs with embedded double quotes and commas, you must use enclose the entire
                                                         directory URI in double quotes and escape the embedded double quotes with a double quote. For example, the Jared, "Jerry",Smith@test.com
                                                         directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the CSV file. | Note | Within Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when you use Bulk Administration
                                                         to import a CSV file that contains directory URIs with embedded double quotes and commas, you must use enclose the entire
                                                         directory URI in double quotes and escape the embedded double quotes with a double quote. For example, the Jared, "Jerry",Smith@test.com
                                                         directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the CSV file. |
| Note | Within Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when you use Bulk Administration
                                                         to import a CSV file that contains directory URIs with embedded double quotes and commas, you must use enclose the entire
                                                         directory URI in double quotes and escape the embedded double quotes with a double quote. For example, the Jared, "Jerry",Smith@test.com
                                                         directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the CSV file. |
| Self-Service User ID | The Self-Service User ID is a DTMF digit string that is used to identify a user (usually same as the user directory number). |
| User
                                             					 Profile | The User
                                             					 Profile is a profile that collects settings to share across a group of users.
                                             					 This profile is used when you create new devices. |
| EM MAX LOGIN TIME | Enter the maximum login time for Extension Mobility and Extension Mobility Cross Cluster users. Enter the value in minutes.The
                                             range of the value is from 0 to 10080 minutes (7 days). |

| Note | The User Group fields appear when you set the Number of User Groups field to greater than zero. |
|---|---|

| Note | Within Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when you use Bulk Administration
                                                         to import a CSV file that contains directory URIs with embedded double quotes and commas, you must use enclose the entire
                                                         directory URI in double quotes and escape the embedded double quotes with a double quote. For example, the Jared, "Jerry",Smith@test.com
                                                         directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the CSV file. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Users > Update Users > Custom
                                             				  File . The User
                                             				  Update Configuration window appears. |
|---|---|
| Step 2 | From the File
                                          				Name drop-down list box, choose the .csv data file that you created
                                       			 for this bulk transaction. Note Click View
                                                         					 File to view the uploaded .csv data file. Click View Sample
                                                         					 File to view a sample .csv data file. | Note | Click View
                                                         					 File to view the uploaded .csv data file. Click View Sample
                                                         					 File to view a sample .csv data file. |
| Note | Click View
                                                         					 File to view the uploaded .csv data file. Click View Sample
                                                         					 File to view a sample .csv data file. |
| Step 3 | From the User
                                          				Template Name drop-down list box, choose the user template that you
                                       			 created for this bulk transaction. |
| Step 4 | In the Value
                                          				for fields to be ignored field, enter the symbol that you want to
                                       			 tell Unified CM Bulk Administration Tool to retain the value that was
                                       			 previously stored in the DC directory. Note The value that
                                                      				  you enter in the .csv file for updating users overrides the values that are
                                                      				  provided in the user template. | Note | The value that
                                                      				  you enter in the .csv file for updating users overrides the values that are
                                                      				  provided in the user template. |
| Note | The value that
                                                      				  you enter in the .csv file for updating users overrides the values that are
                                                      				  provided in the user template. |
| Step 5 | In the Job
                                          				Information area, enter the Job description. |
| Step 6 | Choose a method
                                       			 to update user records. Do one of the following: Select Run
                                             				  Immediately to update user records immediately. Select Run
                                             				  Later to insert the user records at a later time. |
| Step 7 | To create a job
                                       			 for updating the user records, click Submit . To schedule or
                                       			 activate this job, use the Job Scheduler option in the Bulk Administration main
                                       			 menu. |

| Note | Click View
                                                         					 File to view the uploaded .csv data file. Click View Sample
                                                         					 File to view a sample .csv data file. |
|---|---|

| Note | The value that
                                                      				  you enter in the .csv file for updating users overrides the values that are
                                                      				  provided in the user template. |
|---|---|

| Note | Be aware that some fields have two check boxes. The first check box determines if you need to update the field; the second
                                          check box determines the value (checked or unchecked) to use for the field. |
|---|---|

| Tip | Check the first check box if you need to update the field and the second check box to apply a checked value to the users you
                                          select. For example, if you check the first box for Home Cluster and leave the second one unchecked, you update users with
                                          an unchecked value for Home Cluster. |
|---|---|

| Field | Description |
|---|---|
| User Information |
| Manager User ID | Enter manager user ID, up to 128 characters, for the user of this phone. |
| Department | Enter the department number, up to 64 characters, for the user of this phone. |
| Associated PC | This field, which is required for Cisco SoftPhone and Cisco Unified Communications Manager Attendant Console users, displays after you add the user. |
| User Locale | Choose the language and country set that you want to associate with this user from the drop-down list. Your choice determines
                                          which cultural-dependent attributes exist for this user and which language displays in the Cisco Unified Communications Manager user windows and phones. |
| Digest Credentials | When you configure digest authentication for phones that are running, Cisco Unified Communications Manager challenges the identity of the phone every time the phone sends a SIP request to Cisco Unified Communications Manager . The digest credentials that you enter in this field get associated with the phone when you choose a digest user in the Phone
                                          Configuration window. Enter a string of up to 128 alphanumeric characters. For more information on digest authentication, see the Cisco Unified Communications Manager Security Guide . |
| Confirm Digest Credentials | To confirm that you entered the digest credentials correctly, reenter the credentials in this field. |
| Service Setting |
| Home Cluster | Check the check box if the end user is associated with this cluster. The end user must be associated with one cluster
                                          within the enterprise. Note IM and Presence feature does not function properly if an end user is associated with more than one home cluster. | Note | IM and Presence feature does not function properly if an end user is associated with more than one home cluster. |
| Note | IM and Presence feature does not function properly if an end user is associated with more than one home cluster. |
| Enable  User for Unified CM IM and Presence | Check the  check box to enable the end user (on the home cluster) for IM and Presence feature. Configure IM and Presence feature
                                          in the associated service profile. Note You can only enable IM and Presence feature for users that have this Unified CM cluster marked as their home cluster. Tip Use the User Management > User Settings > UC Service menu to configure the IM and Presence feature. | Note | You can only enable IM and Presence feature for users that have this Unified CM cluster marked as their home cluster. | Tip | Use the User Management > User Settings > UC Service menu to configure the IM and Presence feature. |
| Note | You can only enable IM and Presence feature for users that have this Unified CM cluster marked as their home cluster. |
| Tip | Use the User Management > User Settings > UC Service menu to configure the IM and Presence feature. |
| Assigned Presence Server | Assign the end user to an server that is installed in the cluster if the system is nonbalanced. The server you specify using the Bulk Administration
                                          Tool must be part of a Presence Redundancy Group. For clusters that have the user assignment mode for the IM and Presence server set to balanced or active-standby, user assignments
                                          that are made using the Bulk Administration Tool override the automatic user assignments. |
| UC Service Profile | Select a UC service profile from the drop-down list box to associate with end users. Note Use the User Management > User Settings > Service Profile menu to set up service profiles for end users. | Note | Use the User Management > User Settings > Service Profile menu to set up service profiles for end users. |
| Note | Use the User Management > User Settings > Service Profile menu to set up service profiles for end users. |
| Include Meeting Information in Presence (Requires Exchange Presence Gateway to be configured on CUCM IM and Presence server.) | Check this check box to create a sync between CUCM IM and Presence server so that  it can include the meeting information
                                          under the  Presence feature. Note You can only access this field if Home Cluster and Enable User for Unified CM IM and Presence is enabled. | Note | You can only access this field if Home Cluster and Enable User for Unified CM IM and Presence is enabled. |
| Note | You can only access this field if Home Cluster and Enable User for Unified CM IM and Presence is enabled. |
| Extension Mobility |
| BLF Presence Group | From the drop-down list, choose the BLF presence group that watches the status of the directory number, the presence entity. |
| SUBSCRIBE Calling Search Space | All calling search spaces that you configure in Cisco Unified Communications Manager Administration display in the SUBSCRIBE Calling Search Space drop-down list. The SUBSCRIBE Calling Search Space determines how Cisco Unified Communications Manager routes the Presence subscription requests that come from the end user. Use the Call Routing > Class Control > Calling Search Space menu to configure a calling search space specifically for this purpose. |
| Maximum Login Time (HHH:MM) | Enter the maximum login time in the HHH:MM format to configure maximum login time for Extension Mobility and Extension Mobility
                                          Cross Cluster users. The value ranges from 00:01 to 168:00 hours. For example: 168:00, 25:16, 025:16, :30 or 00:30. |
| Allow Control of Device from CTI | Check this check box to allow CTI to control and monitor this device. If the associated directory number specifies a shared line, the check box should be checked as long as at least one associated
                                          device specifies a combination of device type and protocol that CTI supports. |
| Enable Extension Mobility Cross Cluster | Check this check box to enable the Extension Mobility Cross Cluster CSS setting that gets used as the device CSS of the remote
                                          phone when the user selects this device profile during the EMCC login. |
| Mobility Information |
| Enable Mobility | Check this check box to activate Mobile Connect, which allows the user to manage calls by using a single phone number and
                                          to pick up and manage calls on the desk phone and mobile phone. |
| Enable Mobile Voice Access | Check this check box to allow the user to access the Mobile Voice Access integrated voice response (IVR) system to initiate
                                          Mobile Connect calls and activate or deactivate Mobile Connect capabilities. |
| Maximum Wait Time for Desk Pickup | Enter the maximum wait time, up to 5 numerals, for this user. This indicates the maximum time that is permitted to pass before the user pickup a call that is transferred from the mobile
                                          phone to the desktop phone. |
| Remote Destination Limit | Enter the maximum number of phones, up to 2 numerals, to which the user is permitted to transfer calls from the desk phone. |
| Job Information |
| Job Description | Enter the job description. |
| Run Immediately | Click this radio button to schedule and immediately activate the update users job. |
| Run Later (To schedule and activate this job, use Job Scheduler page.) | Click this radio button to schedule and activate the update users job later. |

| Note | IM and Presence feature does not function properly if an end user is associated with more than one home cluster. |
|---|---|

| Note | You can only enable IM and Presence feature for users that have this Unified CM cluster marked as their home cluster. |
|---|---|

| Tip | Use the User Management > User Settings > UC Service menu to configure the IM and Presence feature. |
|---|---|

| Note | Use the User Management > User Settings > Service Profile menu to set up service profiles for end users. |
|---|---|

| Note | You can only access this field if Home Cluster and Enable User for Unified CM IM and Presence is enabled. |
|---|---|

| Step 1 | Select Bulk Administration > Users > Update Users > Query The Update Users Query window appears. |
|---|---|
| Step 2 | From the first Find Phone where drop-down list, select one of the following criteria: Last Name First Name User ID Manager Department Has Home Cluster Enabled Does not have Home Cluster Enabled Has IM and Presence Enabled Does not have IM and Presence Enabled |
| Step 3 | From the second Find Users where drop-down list, select one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 4 | Specify the appropriate search text, if applicable. Tip To find all users that are registered in the database, select Find without entering any search text. Tip To further define your query and to add multiple filters, click the plus (+) button and repeat step 2 and step 3. | Tip | To find all users that are registered in the database, select Find without entering any search text. | Tip | To further define your query and to add multiple filters, click the plus (+) button and repeat step 2 and step 3. |
| Tip | To find all users that are registered in the database, select Find without entering any search text. |
| Tip | To further define your query and to add multiple filters, click the plus (+) button and repeat step 2 and step 3. |
| Step 5 | Select Find . A list of discovered users appears. The Update Users window displays the details of the users that you select. |

| Tip | To find all users that are registered in the database, select Find without entering any search text. |
|---|---|

| Tip | To further define your query and to add multiple filters, click the plus (+) button and repeat step 2 and step 3. |
|---|---|

| Step 1 | In the Update Users Query window, select Next . If you want to change the type of query, select Back . The Update Users shows the type of query that you select. |
|---|---|
| Step 2 | Check the check box to the left of the field that you want to update. This selection tells BAT to overwrite the existing value for the field. Note BAT updates only those fields for which you check the update check box. | Note | BAT updates only those fields for which you check the update check box. |
| Note | BAT updates only those fields for which you check the update check box. |
| Step 3 | Update the required user parameters. See the "User update settings" topic. |
| Step 4 | In the Job Information area , enter the job description. |
| Step 5 | Select one of the following methods to update user records: Select Run Immediately to update users immediately. Select Run Later to update users at a later time. |
| Step 6 | Select Submit . This action creates a job for updating the records. Note Use the Job Scheduler option in the Bulk Administration main menu to schedule and activate this job. | Note | Use the Job Scheduler option in the Bulk Administration main menu to schedule and activate this job. |
| Note | Use the Job Scheduler option in the Bulk Administration main menu to schedule and activate this job. |

| Note | BAT updates only those fields for which you check the update check box. |
|---|---|

| Note | Use the Job Scheduler option in the Bulk Administration main menu to schedule and activate this job. |
|---|---|