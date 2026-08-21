---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-ad9a144dab
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_010010.html
retrieved_at: 2026-08-21T17:56:34.035666+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

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
                                             					 information about the BLF Presence feature, see the Cisco Unified Communications Manager Features and
                                                						Services Guide .

SUBSCRIBE
                                             					 Calling Search Space

All calling search spaces that you configure in Unified CM Administration appear in the SUBSCRIBE Calling Search Space drop-down list box.

The SUBSCRIBE Calling Search Space determines how Unified CM routes the Presence subscription requests that come from the user. To configure a calling search space specifically for this
                                             purpose, you configure a calling search space as you do all calling search spaces ( Call Routing > Class Control > Calling Search Space ).

To
                                             					 set up a calling search space, see the Cisco Unified Communications Manager Administration Guide .

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

Home Cluster

Check the check box if the end user is associated with this cluster. The end user must be associated with one cluster
                                          within the enterprise.

IM and Presence feature does not function properly if an end user is associated with more than one home cluster.

Enable  User for Unified CM IM and Presence

Check the  check box to enable the end user (on the home cluster) for IM and Presence feature. Configure IM and Presence feature
                                          in the associated service profile.

You must install a Unified CM IM and Presence node along with this Unified CM cluster.

You can only enable IM and Presence feature for users that have this Unified CM cluster marked as their home cluster.

Tip

Use the User Management > User Settings > UC Service menu to configure the IM and Presence feature.

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
                                          				  be ignored for such fields. |
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
                                             					 information about the BLF Presence feature, see the Cisco Unified Communications Manager Features and
                                                						Services Guide . |
| SUBSCRIBE
                                             					 Calling Search Space | All calling search spaces that you configure in Unified CM Administration appear in the SUBSCRIBE Calling Search Space drop-down list box. The SUBSCRIBE Calling Search Space determines how Unified CM routes the Presence subscription requests that come from the user. To configure a calling search space specifically for this
                                             purpose, you configure a calling search space as you do all calling search spaces ( Call Routing > Class Control > Calling Search Space ). To
                                             					 set up a calling search space, see the Cisco Unified Communications Manager Administration Guide . |
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

| Note | The User Group fields appear when you set the Number of User Groups field to greater than zero. |
|---|---|

| Note | Within Unified CM Administration, you can enter directory URIs with embedded double quotes or commas. However, when you use Bulk Administration
                                                         to import a CSV file that contains directory URIs with embedded double quotes and commas, you must use enclose the entire
                                                         directory URI in double quotes and escape the embedded double quotes with a double quote. For example, the Jared, "Jerry",Smith@test.com
                                                         directory URI must be input as "Jared,""Jerry"",Smith@test.com" in the CSV file. |
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
|  |  |
| Home Cluster | Check the check box if the end user is associated with this cluster. The end user must be associated with one cluster
                                          within the enterprise. Note IM and Presence feature does not function properly if an end user is associated with more than one home cluster. | Note | IM and Presence feature does not function properly if an end user is associated with more than one home cluster. |
| Note | IM and Presence feature does not function properly if an end user is associated with more than one home cluster. |
| Enable  User for Unified CM IM and Presence | Check the  check box to enable the end user (on the home cluster) for IM and Presence feature. Configure IM and Presence feature
                                          in the associated service profile. Note You must install a Unified CM IM and Presence node along with this Unified CM cluster. Note You can only enable IM and Presence feature for users that have this Unified CM cluster marked as their home cluster. Tip Use the User Management > User Settings > UC Service menu to configure the IM and Presence feature. | Note | You must install a Unified CM IM and Presence node along with this Unified CM cluster. | Note | You can only enable IM and Presence feature for users that have this Unified CM cluster marked as their home cluster. | Tip | Use the User Management > User Settings > UC Service menu to configure the IM and Presence feature. |
| Note | You must install a Unified CM IM and Presence node along with this Unified CM cluster. |
| Note | You can only enable IM and Presence feature for users that have this Unified CM cluster marked as their home cluster. |
| Tip | Use the User Management > User Settings > UC Service menu to configure the IM and Presence feature. |
| Job Information |
| Job Description | Enter the job description. |
| Run Immediately | Click this radio button to schedule and immediately activate the update users job. |
| Run Later (To schedule and activate this job, use Job Scheduler page.) | Click this radio button to schedule and activate the update users job later. |

| Note | IM and Presence feature does not function properly if an end user is associated with more than one home cluster. |
|---|---|

| Note | You must install a Unified CM IM and Presence node along with this Unified CM cluster. |
|---|---|

| Note | You can only enable IM and Presence feature for users that have this Unified CM cluster marked as their home cluster. |
|---|---|

| Tip | Use the User Management > User Settings > UC Service menu to configure the IM and Presence feature. |
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