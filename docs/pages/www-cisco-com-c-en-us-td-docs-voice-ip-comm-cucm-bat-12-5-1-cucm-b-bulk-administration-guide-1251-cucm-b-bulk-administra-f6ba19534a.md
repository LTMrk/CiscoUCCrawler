---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-f6ba19534a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_0111011.html
retrieved_at: 2026-08-21T18:01:44.583171+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: Remote Destination Profiles

## Chapter: Remote Destination Profiles

# Remote Destination Profiles

This chapter provides information to use the Bulk Administration
                        		menu to format, insert, delete, and export Remote Destination Profiles (RDPs)
                        		in batches, rather than performing individual updates through CiscoUnified
                        		Communications Manager Administration.

## Remote Destination Profile Templates

You can use BAT remote destination profile templates to
                              		  define common attributes for remote destinations such as device pool, location,
                              		  calling search space, presence group, and privacy information.

### Find Remote Destination Profile Template

Because you might have several remote destination profile
                                 		  (RDP) templates, Cisco Unified Communications Manager lets you locate specific templates on the
                                 		  basis of specific criteria.

Step 1

Choose Bulk
                                                				  Administration > Mobility > Remote
                                                				  Destination Profiles > Remote Destination Profile
                                                				  Template .

Step 2

From the first Find UDP Templates where drop-down list box,
                                          			 choose one of the following criteria:

- Name

- Description

- Device Pool

- Calling Search Space

From the second Find Remote Destination Template where drop-down list box, choose one of the following criteria:

- begins with

- contains

- ends with

- is exactly

- is empty

- is not empty

Step 3

Specify the appropriate search text, if applicable, and click Find .

Tip

To find all remote destination templates that are registered in
                                                         				  the database, click Find without entering any search text.

A list of discovered templates displays by:

- Template Name

- Description

- Device Pool

- Calling Search Space

Step 4

From the list of records, click the template name that matches
                                          			 your search criteria.

The Remote Destination Profile Template
                                                				  Configuration window displays.

### Create Remote Destination Profile Template

You can create a template to add remote destination profiles
                                 		  in bulk.

Step 1

Choose Bulk
                                                				  Administration > Mobility > Remote
                                                				  Destination Profiles > Remote Destination Profile
                                                				  Template .

Step 2

Click Add New .

Step 3

Enter configuration details in the fields that display.

Step 4

Click Save .

#### What to do next

When the status indicates that the transaction has completed, you can
                                 		  add line attributes.

### Add or Update Lines in Remote Destination Profile Template

You can add one or more lines to the BAT template or to
                                 		  update existing lines.

Step 1

Find the RDP Template to which you want to add line.

Step 2

In the Remote Destination Profile Template
                                             				Configuration window, click Line [1] Add a new DN in the Association Information area.

Step 3

Enter or choose the appropriate values for the line settings that
                                          			 are described in Table 1 , and click Save .

BAT adds the line to the phone template configuration. All RDPs in
                                             				this batch will use the settings that you choose for this line.

After you enter or choose the appropriate values, you must
                                                         				  return to this page to complete the procedure.

Step 4

Repeat Step 2 through Step 3 to add settings for any additional lines.

If you choose Back to Find/List from the Related Links drop-down list box in the upper, right corner of
                                                         				  the Line Template Configuration window, the Find and List Directory Numbers window
                                                         				  displays. To find existing line template, enter the appropriate search criteria
                                                         				  and click Find . To add a new line template, click Add New on Find and List Line Template window.

Cisco recommends that you use alphanumeric characters for Line
                                             				Template. This is because, if numbers are given, a chance exists of conflict
                                             				with an actual directory number. Using this method, you also avoid conflicts
                                             				with features such as Call Pickup group number, Call Park number, and so on.

### Delete Remote Destination Profile Template

You can delete RDP templates when you no longer require them.

Step 1

Find the RDP Template that you want to delete.

Step 2

In the Find and List Remote Destination Profile
                                             				Templates window, check the check box next to the template that you
                                          			 want to delete and click Delete Selected .

A message displays that asks you to confirm the delete operation.

Step 3

To delete the template, click OK . The template name disappears from the list
                                          			 of templates on the Find and List Remote Destination Profile
                                             				Templates window.

Caution

If you submit a job that uses a particulate RDP template and if
                                                         				  you delete the template, the job also gets deleted.

### Remote Destination Profile Template Field Descriptions

The following table provides field descriptions for Remote
                                 		  Destination Profile Template.

In the BAT user interface, field names that have an asterisk require
                                             			 an entry. Treat fields that do not have an asterisk as optional.

Field

Description

Template Name

Enter template name.

Description

Enter a description for the RDP template that you want to
                                             					 create. The description can include up to 50 characters in any language, but it
                                             					 cannot include double-quotes ("), percentage sign
                                             					 (%), ampersand (&), back-slash
                                             					 (\), or angle brackets (<>).

User ID

Provide a Cisco Unified Communications Manager user ID.

Device Pool

Choose a device pool for this group of RDPs.

Calling Search Space

Choose the calling search space for this group of RDPs.

A calling search space specifies the collection of Route
                                             					 Partitions that are searched to determine how a dialed number should be routed.

Media Resource List

Choose the media resource group list (MRGL) for this group of
                                             					 RDPs.

An MRGL specifies a list of prioritized media resource groups.
                                             					 An application can choose required media resources from the available ones
                                             					 according to the order that is defined in the MRGL.

User Hold Audio Source

Choose the user hold audio source for this group of RDPs.

The user hold audio source identifies the audio source from
                                             					 which music is played when a user places a call on hold.

Network Hold MOH Audio Source

Choose the music on hold audio source to be played when the
                                             					 system places a call on hold while the user transfers a call or initiates a
                                             					 conference or call park.

Location

Choose the appropriate location for this group of RDPs.

The location specifies the total bandwidth that is available
                                             					 for calls to and from this location. A location setting of None means that the
                                             					 locations feature does not keep track of the bandwidth that this device
                                             					 consumes.

User Locale

From the drop-down list box, choose the locale that is
                                             					 associated with the phone user interface. The user locale identifies a set of
                                             					 detailed information to support users, including language and font.

Cisco Unified Communications Manager makes this field available only for
                                             					 phone models that support localization.

If no user locale is specified, Cisco Unified Communications Manager uses the user locale that is
                                                         						associated with the device pool.

If the users require that information be displayed (on the
                                                         						phone) in any language other than English, verify that the locale installer is
                                                         						installed before configuring user locale. Refer to the Cisco Unified Communications Manager Locale Installer documentation.

Privacy

Choose On, Off, or Default in the Privacy drop-down list box.

Presence Group

If you want the RDP to receive the status of the presence
                                             					 entity, choose a Presence Group that is allowed to view the status of the
                                             					 Presence Group that is applied to the directory number, as indicated in the
                                             					 Presence Group Configuration window.

Rerouting Calling Search Space

From the drop-down list box, choose a calling search space to
                                             					 use for rerouting.

The rerouting calling search space of the referer gets used to
                                             					 find the route to the refer-to target. When the Refer operation fails due to
                                             					 rerouting of the calling search space, the Refer Primitive rejects the request
                                             					 with the "405 Method Not Allowed" message.

The redirection (3xx) primitive and transfer feature also uses
                                             					 the rerouting calling search space to find the redirect-to or transfer-to
                                             					 target.

Ignore Presentation Indicators (internal calls only)

Check this check box to enable Cisco Unified Communications Manager to ignore any presentation restriction that is
                                             					 received for internal calls.

## Remote Destination Profile File Format

You can configuring file formats for CSV data files that are
                           		created using a text editor.

### CSV Data File Creation for Remote Destination Using Text Editor

You can create the CSV data file by using lines of ASCII
                                 		  text with values separated by commas. The comma separated values (CSV) file
                                 		  provides textual information in tabular form.

You cannot modify or delete the Default Remote Destination
                                 		  file format.

When you use the Cisco Unified Communications Manager Bulk Administration (BAT)
                                             			 spreadsheet to create the CSV data file, you can create the file format within
                                             			 the spreadsheet. When you use a text editor to create the CSV data file, you
                                             			 need to create a file format or use the default file format. You enter the
                                             			 values in the text-based file in the same order as specified in the file
                                             			 format.

### Find Remote Destination File Format

You can find a remote destination file format using BAT.

Step 1

Choose Bulk
                                                				  Administration > Mobility > Remote
                                                				  Destination Profile > Remote Destination Profile File
                                                				  Format > Create File Format .

Step 2

From the Related Links drop-down list box on the top,
                                          			 right corner of the window, choose Back to Find/List and click Go .

Step 3

From the Find Remote Destination File Format where Format
                                             				Name drop-down list box, choose one of the following criteria:

- begins with

- contains

- ends with

- is exactly

- is empty

- is not empty

Step 4

Specify the appropriate search text, if applicable, and click Find .

Tip

To find all Remote Destination Profile formats, click Find without entering any search text.

Step 5

To further define your query and to add multiple filters, check
                                          			 the Search Within Results check box and choose AND or OR from the drop-down box, and repeat Step 3 and Step 4 .

Step 6

From the list of records, click the file format name that matches
                                          			 your search criteria.

### Remote Destination Profile File Format Configuration

You can create, find, copy, modify, or delete a Remote
                                 		  Destination Profile file format using BAT.

#### Create Remote Destination Profile File Format

You can create your file format for the text-based CSV data
                                    		  file.

Step 1

Choose Bulk
                                                   				  Administration > Mobility > Remote
                                                   				  Destination Profile > Remote Destination Profile File
                                                   				  Format > Create File Format .

Step 2

In the Format Name field, enter a name for this
                                             			 custom format.

Step 3

Under Device Fields , choose the device field names
                                             			 that you want to define for each Remote Destination Profile. In the Device Field box, click a device field name
                                             			 and click the arrow to move the field to the Selected Device Fields box.

A CSV data file must include Remote Destination Profile Name and
                                                				Description; therefore, these fields always remain selected.

Tip

You can select several random field names in the list by holding
                                                            				  down the Ctrl key and then clicking the arrow to
                                                            				  select them together. You can select a range of items by using the Shift key.

Step 4

Click line field names in the Line Field box and click the arrow to move the
                                             			 fields to the Selected Line Fields box.

Tip

You can change the order of the items in the Selected Line Fields and Selected Device Fields Order boxes. Select
                                                            				  an item and then use the up arrow to move the item closer to the beginning of
                                                            				  the list or the down arrow to move it to the end of the list.

Step 5

In the IP Phone Services Maximums area, enter the
                                             			 maximum value in the Maximum Number of Lines field.

Step 6

To save your custom file format, click Save . The name of the file format displays in
                                             			 the File Format Names list in the Find and List Remote Destination Profile File
                                                				Formats window.

#### Copy Remote Destination Profile File Format

You can copy an existing format for the CSV data file using
                                    		  BAT.

Step 1

Find the Remote Destination Profile file format that
                                             			 you want to copy.

Step 2

In the Search Results area, choose a file format that
                                             			 you want to copy.

Step 3

To make a copy of the chosen file format, click Copy .

To copy the file format, you can also click the corresponding
                                                            				  Copy icon in the Find and List Remote Destination Profile File
                                                               					 Formats window.

Step 4

In the Format Name field, enter a new name for the
                                             			 copied format.

Step 5

Modify the copied format using any of these methods:

Add new fields by choosing them from the Device Fields or Line Fields box and then clicking the arrow to move the chosen fields into the Selected Device Field or Selected Line Fields Order box.

Remove selected fields by choosing them from the Selected Device Fields or Selected Line Fields Order box and then clicking the arrow to move the chosen fields into the Device Fields or Line Fields box .

Change the order of the fields by choosing a field name in the Selected Device Fields or Selected Line Fields Order box and using the up or down arrow to change its location.

Step 6

After making your changes, click Save to save the copied file format with
                                             			 changes in the list.

#### Modify Remote Destination Profile File Format

You can modify an existing file format for the CSV data file
                                    		  using BAT. You can modify custom formats only.

Step 1

Find the Remote Destination Profile file format that you want to
                                             			 modify.

Step 2

In the Search Results area, choose a file
                                             			 format that you want to modify.

Step 3

Modify the copied format using any of these methods:

Add new fields by choosing them from the Device Fields or Line Fields box and then clicking the arrow to move the chosen fields into the Selected Device Field or Selected Line Fields Order box.

Remove selected fields by choosing them from the Selected Device Fields or Selected Line Fields Order box and then clicking the arrow to move the chosen fields into the Device Fields or Line Fields box .

Change the order of the fields by choosing a field name in the Selected Device Fields Order or Selected Line Fields Order box and using the up or down arrow to change its location.

Step 4

After making your changes, click Save to save the changes to the file format.

#### Delete Remote Destination Profile File Format

You can delete an existing file format for the CSV data
                                    		  file. You can delete only custom formats.

Step 1

Find the Remote Destination Profile file format that you want to
                                             			 delete.

Step 2

In the Search Results area, verify that this is the
                                             			 file(s) that you want to delete and check the check box to select the
                                             			 format(s).

Step 3

To remove the file format(s) from the list, click Delete Selected . A message asks you to confirm
                                             			 that you want to delete the file format(s). Click OK to continue.

Attention

Make sure to browse the entire list of displayed results before
                                                            				  clicking Delete Selected .

### Associate Remote Destination File Format with CSV Data File

You can add the file format with the text-based CSV data
                                 		  file. When you used a text editor to create the CSV data file, you created a
                                 		  file format for entering values in the text-based file. You entered values in
                                 		  the text file in the order that the file format specified

After the CSV data file is completed, you need to associate
                                 		  the file format with the text-based CSV data file. After associating the file
                                 		  format with the CSV file, the names for each field display as the first record
                                 		  in the CSV data file. You can use this information to verify that you entered
                                 		  the values for each field in the correct order.

Step 1

Choose Bulk
                                                				  Administration > Mobility > Remote
                                                				  Destination Profile > Remote Destination Profile File
                                                				  Format > Add File Format .

Step 2

In the File Name field, choose the text-based CSV
                                          			 file that you created for this transaction.

Step 3

In the File Format Name field, choose the file format
                                          			 that you created for this type of bulk transaction.

Step 4

To create a job for associating the matching file format with the
                                          			 CSV data file, click Submit .

Step 5

Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                          			 and / or activate this job.

## Remote Destination Profile Insertions

You can use the Bulk Administration menu to insert Remote
                              		  Destination Profiles (RDPs) in batches, rather than performing individual
                              		  updates through Cisco Unified Communications Manager Administration.

### Insert Remote Destination Profiles in Cisco Unified Communications Manager

You can insert Remote Destination Profiles into
                                 		  Cisco Unified Communications Manager.

#### Before you begin

You must have a Cisco Unified Communications Manager Bulk Administration (BAT) Remote Destination Profile template for the
                                       devices that you are adding.

You must have a data file in comma separated value (CSV) format that contains the unique details for the Remote Destination
                                       Profiles.

Upload the data files by choosing the relevant target and function for the transaction.

Step 1

Choose Bulk
                                                				  Administration > Mobility > Remote
                                                				  Destination Profile > Remote Destination Profile
                                                				  Insert .

Step 2

In the File Name drop-down list box, choose the CSV
                                          			 data file that you created for this specific bulk transaction.

Step 3

In the Remote Destination Profile Template Name drop-down list box, choose the BAT Remote Destination Profile template that you
                                          			 created for this type of bulk transaction.

Remote Destination Profile template is optional while inserting
                                                         				  Remote Destination Profiles. Ensure that the CSV data file has a 'Desk Phone
                                                         				  Name' when a Remote Destination Profile template is not selected.

Step 4

Check the Override the existing configuration check box
                                          			 to overwrite the existing Remote Destination Profile settings with the
                                          			 information that is contained in the file that you want to insert.

Step 5

In the Job Information area, enter the Job description.

Step 6

Choose an insert method. Do one of the following:

Click Run Immediately to insert the Remote
                                                				  Destination Profile records immediately.

Click Run Later to insert the Remote Destination
                                                				  Profile records at a later time.

Step 7

To create a job for inserting the Remote Destination Profile
                                          			 records, click Submit .

Step 8

To create a job for inserting the gateways, click Submit .

## Remote Destination Profile Deletions

You can use the Bulk Administration menu to delete and export Remote Destination Profiles (RDPs) in batches, rather than performing
                              individual updates through Cisco Unified Communications Manager Administration.

### Delete Remote Destination Profiles Using Custom File

Use a text editor to create a custom file of Remote
                                 		  Destination Profiles that you want to delete. You can have MAC addresses and
                                 		  device names in the same custom file, but you cannot have directory numbers in
                                 		  the same file. You need to create separate files—one file that contains the
                                 		  device names and MAC addresses and another file that contains the directory
                                 		  numbers.

#### Before you begin

Create a text file that lists one of these details for the RDPs that you want to delete:

Name

Description

Device Pool

Calling Search Space

Put each item on a separate line in the text file.

Upload the custom file to CiscoUnifiedCallManager server. For more details on uploading files, see the Upload File to Server .

Step 1

Choose Bulk
                                                				  Administration > Mobility > Remote
                                                				  Destination Profile > Remote Destination Profile
                                                				  Delete .

Step 2

In the Delete Remote Destination Profile where drop-down list box, choose the type of custom file that you have created from
                                          			 one of the following criteria:

Name

Description

Device Pool

Calling Search Space

Step 3

In the list of custom files, choose the filename of the custom
                                          			 file for this delete.

Step 4

Click Find . A list of RDPs matching your search
                                          			 criteria displays.

Step 5

In the Job Information area, enter the Job description.

Step 6

Choose a delete method. Do one of the following:

Click Run Immediately to delete RDP records
                                                				  immediately.

Click Run Later to delete RDP records at a later
                                                				  time.

Step 7

Click Submit to create a job for deleting the RDP
                                          			 records.

Step 8

To create a job for inserting the gateways, click Submit .

## Remote Destination Profile Exports Using Export Utility

You can use the export utility to merge records from multiple CiscoUnifiedCallManager servers onto one CiscoUnifiedCallManager
                           server. Use this procedure to move records from one CiscoUnified CallManager server to another.

### Export Remote Destination Profile Using Export Utility

You can export remote destination profile details.

If you are accessing help from the second Export Remote Destination Profile Configuration window after selecting the remote destination profile for export, skip to Step 7 .

Step 1

Choose Bulk
                                                				  Administration > Mobility > Remote
                                                				  Destination Profile > Remote Destination Profile
                                                				  Export .

Step 2

From the first Find Remote Destination Profile where drop-down list, choose one of the following criteria:

Name

Description

Device Pool

Calling Search Space

From the second Find Remote Destination Profile where drop-down list, choose one of the following criteria:

begins with

contains

ends with

is exactly

is empty

is not empty

Step 3

Specify the appropriate search text, if applicable.

Tip

To find all Remote Destination Profiles that are registered in
                                                         				  the database, click Find without entering any search text.

Step 4

To further define your query and to add multiple filters, check the Search Within Results check box, choose AND or OR from the drop-down list, repeat Step 2 and Step 3 .

Step 5

Click Find .

A list of discovered Remote Destination Profiles displays by:

Name

Description

Device Pool

Calling Search Space

Make sure to browse the entire list of displayed results before submitting the job.

Step 6

Click Next .

The next Export Remote Destination Profile
                                                				  Configuration window displays.

Step 7

Enter an export file name in the File Name field.

Step 8

Choose a file format from the File Format drop-down list.

Step 9

In the Job Information area, enter the Job
                                          			 description. Delete Remote Destination Profiles is the default description.

Step 10

Choose an export method. Do one of the following:

Click Run Immediately to export Remote
                                                				  Destination Profile records immediately.

Click Run Later to export Remote Destination
                                                				  Profile records at a later time.

Step 11

Click Submit to create a job for deleting the Remote
                                          			 Destination Profile records.

Step 12

To schedule and / or activate this job, use the Job
                                          			 Scheduler option in the Bulk Administration main menu.

#### Default Remote Destination Profile File Format

When you export Remote Destination Profile records by using
                                    		  Default Remote Destination Profile file format option, you export Remote
                                    		  Destination Profile records along different line attributes that are associated
                                    		  with the Remote Destination Profile. You cannot use the query to limit the
                                    		  number of records.

The following table lists the fields that are exported when
                                    		  you choose the Default Remote Destination Profile Format file format.

Field Types

Exported Fields

Device Fields

Remote Destination Profile Name, Description, User ID, Device
                                                					 Pool, CSS, AAR CSS, Media Resource List, User Hold Audio Source, Location,
                                                					 Privacy, Device Presence Group, Rerouting CSS

Line Fields

Directory Number, Partition, Voice Mail Profile, Line CSS, AAR
                                                					 Group(Line), Line User Hold Audio Source, Line Network Hold Audio Source,
                                                					 Forward All Destination, Forward All CSS, Forward Busy Internal Destination,
                                                					 Forward Busy Internal CSS, Forward Busy External Destination, Forward Busy
                                                					 External CSS, Forward No Answer Internal Destination, Forward No Answer
                                                					 Internal CSS, Forward No Answer External Destination, Forward No Answer
                                                					 External CSS, Forward No Coverage Internal Destination, Forward No Coverage
                                                					 Internal CSS, Forward No Coverage External Destination, Forward No Coverage
                                                					 External CSS, Forward No Answer Ring Duration, Call Pickup Group, MLPP Target,
                                                					 MLPP CSS, MLPP No Answer Ring Duration, External Phone Number Mask, Maximum
                                                					 Number Of Calls, Busy Trigger, Alerting Name, Alerting Name ASCII, Display,
                                                					 Line Description, Line Presence Group, Secondary CSS For Forward All, ASCII
                                                					 Display, Forward On CTI Failure Destination, Forward On CTI Failure CSS, AAR
                                                					 Destination Mask, Forward Unregistered Internal Destination, Forward
                                                					 Unregistered Internal CSS, Forward Unregistered External Destination, Forward
                                                					 Unregistered External CSS, Hold Reversion Ring Duration, Hold Reversion
                                                					 Notification Interval

| Step 1 | Choose Bulk
                                                				  Administration > Mobility > Remote
                                                				  Destination Profiles > Remote Destination Profile
                                                				  Template . The Find and List Remote Destination Templates window displays. Use the two drop-down list boxes to search for a template. |
|---|---|
| Step 2 | From the first Find UDP Templates where drop-down list box,
                                          			 choose one of the following criteria: Name Description Device Pool Calling Search Space From the second Find Remote Destination Template where drop-down list box, choose one of the following criteria: begins with contains ends with is exactly is empty is not empty |
| Step 3 | Specify the appropriate search text, if applicable, and click Find . Tip To find all remote destination templates that are registered in
                                                         				  the database, click Find without entering any search text. A list of discovered templates displays by: Template Name Description Device Pool Calling Search Space | Tip | To find all remote destination templates that are registered in
                                                         				  the database, click Find without entering any search text. |
| Tip | To find all remote destination templates that are registered in
                                                         				  the database, click Find without entering any search text. |
| Step 4 | From the list of records, click the template name that matches
                                          			 your search criteria. The Remote Destination Profile Template
                                                				  Configuration window displays. |

| Tip | To find all remote destination templates that are registered in
                                                         				  the database, click Find without entering any search text. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Mobility > Remote
                                                				  Destination Profiles > Remote Destination Profile
                                                				  Template . |
|---|---|
| Step 2 | Click Add New . The Remote Destination Template Configuration window
                                          			 displays. |
| Step 3 | Enter configuration details in the fields that display. See Remote Destination Profile Template Field Descriptions for field descriptions. |
| Step 4 | Click Save . |

| Step 1 | Find the RDP Template to which you want to add line. |
|---|---|
| Step 2 | In the Remote Destination Profile Template
                                             				Configuration window, click Line [1] Add a new DN in the Association Information area. |
| Step 3 | Enter or choose the appropriate values for the line settings that
                                          			 are described in Table 1 , and click Save . BAT adds the line to the phone template configuration. All RDPs in
                                             				this batch will use the settings that you choose for this line. Note After you enter or choose the appropriate values, you must
                                                         				  return to this page to complete the procedure. | Note | After you enter or choose the appropriate values, you must
                                                         				  return to this page to complete the procedure. |
| Note | After you enter or choose the appropriate values, you must
                                                         				  return to this page to complete the procedure. |
| Step 4 | Repeat Step 2 through Step 3 to add settings for any additional lines. Note If you choose Back to Find/List from the Related Links drop-down list box in the upper, right corner of
                                                         				  the Line Template Configuration window, the Find and List Directory Numbers window
                                                         				  displays. To find existing line template, enter the appropriate search criteria
                                                         				  and click Find . To add a new line template, click Add New on Find and List Line Template window. Cisco recommends that you use alphanumeric characters for Line
                                             				Template. This is because, if numbers are given, a chance exists of conflict
                                             				with an actual directory number. Using this method, you also avoid conflicts
                                             				with features such as Call Pickup group number, Call Park number, and so on. | Note | If you choose Back to Find/List from the Related Links drop-down list box in the upper, right corner of
                                                         				  the Line Template Configuration window, the Find and List Directory Numbers window
                                                         				  displays. To find existing line template, enter the appropriate search criteria
                                                         				  and click Find . To add a new line template, click Add New on Find and List Line Template window. |
| Note | If you choose Back to Find/List from the Related Links drop-down list box in the upper, right corner of
                                                         				  the Line Template Configuration window, the Find and List Directory Numbers window
                                                         				  displays. To find existing line template, enter the appropriate search criteria
                                                         				  and click Find . To add a new line template, click Add New on Find and List Line Template window. |

| Note | After you enter or choose the appropriate values, you must
                                                         				  return to this page to complete the procedure. |
|---|---|

| Note | If you choose Back to Find/List from the Related Links drop-down list box in the upper, right corner of
                                                         				  the Line Template Configuration window, the Find and List Directory Numbers window
                                                         				  displays. To find existing line template, enter the appropriate search criteria
                                                         				  and click Find . To add a new line template, click Add New on Find and List Line Template window. |
|---|---|

| Step 1 | Find the RDP Template that you want to delete. |
|---|---|
| Step 2 | In the Find and List Remote Destination Profile
                                             				Templates window, check the check box next to the template that you
                                          			 want to delete and click Delete Selected . A message displays that asks you to confirm the delete operation. |
| Step 3 | To delete the template, click OK . The template name disappears from the list
                                          			 of templates on the Find and List Remote Destination Profile
                                             				Templates window. Caution If you submit a job that uses a particulate RDP template and if
                                                         				  you delete the template, the job also gets deleted. | Caution | If you submit a job that uses a particulate RDP template and if
                                                         				  you delete the template, the job also gets deleted. |
| Caution | If you submit a job that uses a particulate RDP template and if
                                                         				  you delete the template, the job also gets deleted. |

| Caution | If you submit a job that uses a particulate RDP template and if
                                                         				  you delete the template, the job also gets deleted. |
|---|---|

| Note | In the BAT user interface, field names that have an asterisk require
                                             			 an entry. Treat fields that do not have an asterisk as optional. |
|---|---|

| Field | Description |
|---|---|
| Template Name | Enter template name. |
| Description | Enter a description for the RDP template that you want to
                                             					 create. The description can include up to 50 characters in any language, but it
                                             					 cannot include double-quotes ("), percentage sign
                                             					 (%), ampersand (&), back-slash
                                             					 (\), or angle brackets (<>). |
| User ID | Provide a Cisco Unified Communications Manager user ID. |
| Device Pool | Choose a device pool for this group of RDPs. |
| Calling Search Space | Choose the calling search space for this group of RDPs. A calling search space specifies the collection of Route
                                             					 Partitions that are searched to determine how a dialed number should be routed. |
| Media Resource List | Choose the media resource group list (MRGL) for this group of
                                             					 RDPs. An MRGL specifies a list of prioritized media resource groups.
                                             					 An application can choose required media resources from the available ones
                                             					 according to the order that is defined in the MRGL. |
| User Hold Audio Source | Choose the user hold audio source for this group of RDPs. The user hold audio source identifies the audio source from
                                             					 which music is played when a user places a call on hold. |
| Network Hold MOH Audio Source | Choose the music on hold audio source to be played when the
                                             					 system places a call on hold while the user transfers a call or initiates a
                                             					 conference or call park. |
| Location | Choose the appropriate location for this group of RDPs. The location specifies the total bandwidth that is available
                                             					 for calls to and from this location. A location setting of None means that the
                                             					 locations feature does not keep track of the bandwidth that this device
                                             					 consumes. |
| User Locale | From the drop-down list box, choose the locale that is
                                             					 associated with the phone user interface. The user locale identifies a set of
                                             					 detailed information to support users, including language and font. Cisco Unified Communications Manager makes this field available only for
                                             					 phone models that support localization. Note If no user locale is specified, Cisco Unified Communications Manager uses the user locale that is
                                                         						associated with the device pool. Note If the users require that information be displayed (on the
                                                         						phone) in any language other than English, verify that the locale installer is
                                                         						installed before configuring user locale. Refer to the Cisco Unified Communications Manager Locale Installer documentation. | Note | If no user locale is specified, Cisco Unified Communications Manager uses the user locale that is
                                                         						associated with the device pool. | Note | If the users require that information be displayed (on the
                                                         						phone) in any language other than English, verify that the locale installer is
                                                         						installed before configuring user locale. Refer to the Cisco Unified Communications Manager Locale Installer documentation. |
| Note | If no user locale is specified, Cisco Unified Communications Manager uses the user locale that is
                                                         						associated with the device pool. |
| Note | If the users require that information be displayed (on the
                                                         						phone) in any language other than English, verify that the locale installer is
                                                         						installed before configuring user locale. Refer to the Cisco Unified Communications Manager Locale Installer documentation. |
| Privacy | Choose On, Off, or Default in the Privacy drop-down list box. |
| Presence Group | If you want the RDP to receive the status of the presence
                                             					 entity, choose a Presence Group that is allowed to view the status of the
                                             					 Presence Group that is applied to the directory number, as indicated in the
                                             					 Presence Group Configuration window. |
| Rerouting Calling Search Space | From the drop-down list box, choose a calling search space to
                                             					 use for rerouting. The rerouting calling search space of the referer gets used to
                                             					 find the route to the refer-to target. When the Refer operation fails due to
                                             					 rerouting of the calling search space, the Refer Primitive rejects the request
                                             					 with the "405 Method Not Allowed" message. The redirection (3xx) primitive and transfer feature also uses
                                             					 the rerouting calling search space to find the redirect-to or transfer-to
                                             					 target. |
| Ignore Presentation Indicators (internal calls only) | Check this check box to enable Cisco Unified Communications Manager to ignore any presentation restriction that is
                                             					 received for internal calls. |

| Note | If no user locale is specified, Cisco Unified Communications Manager uses the user locale that is
                                                         						associated with the device pool. |
|---|---|

| Note | If the users require that information be displayed (on the
                                                         						phone) in any language other than English, verify that the locale installer is
                                                         						installed before configuring user locale. Refer to the Cisco Unified Communications Manager Locale Installer documentation. |
|---|---|

| Note | When you use the Cisco Unified Communications Manager Bulk Administration (BAT)
                                             			 spreadsheet to create the CSV data file, you can create the file format within
                                             			 the spreadsheet. When you use a text editor to create the CSV data file, you
                                             			 need to create a file format or use the default file format. You enter the
                                             			 values in the text-based file in the same order as specified in the file
                                             			 format. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Mobility > Remote
                                                				  Destination Profile > Remote Destination Profile File
                                                				  Format > Create File Format . The Create Remote Destination Profile File Format
                                          			 Configuration window displays. |
|---|---|
| Step 2 | From the Related Links drop-down list box on the top,
                                          			 right corner of the window, choose Back to Find/List and click Go . |
| Step 3 | From the Find Remote Destination File Format where Format
                                             				Name drop-down list box, choose one of the following criteria: begins with contains ends with is exactly is empty is not empty |
| Step 4 | Specify the appropriate search text, if applicable, and click Find . Tip To find all Remote Destination Profile formats, click Find without entering any search text. | Tip | To find all Remote Destination Profile formats, click Find without entering any search text. |
| Tip | To find all Remote Destination Profile formats, click Find without entering any search text. |
| Step 5 | To further define your query and to add multiple filters, check
                                          			 the Search Within Results check box and choose AND or OR from the drop-down box, and repeat Step 3 and Step 4 . |
| Step 6 | From the list of records, click the file format name that matches
                                          			 your search criteria. The Remote Destination File Format Configuration window displays. |

| Tip | To find all Remote Destination Profile formats, click Find without entering any search text. |
|---|---|

| Step 1 | Choose Bulk
                                                   				  Administration > Mobility > Remote
                                                   				  Destination Profile > Remote Destination Profile File
                                                   				  Format > Create File Format . The Remote Destination Profile File Format Configuration
                                             			 window displays. |
|---|---|
| Step 2 | In the Format Name field, enter a name for this
                                             			 custom format. |
| Step 3 | Under Device Fields , choose the device field names
                                             			 that you want to define for each Remote Destination Profile. In the Device Field box, click a device field name
                                             			 and click the arrow to move the field to the Selected Device Fields box. A CSV data file must include Remote Destination Profile Name and
                                                				Description; therefore, these fields always remain selected. Tip You can select several random field names in the list by holding
                                                            				  down the Ctrl key and then clicking the arrow to
                                                            				  select them together. You can select a range of items by using the Shift key. | Tip | You can select several random field names in the list by holding
                                                            				  down the Ctrl key and then clicking the arrow to
                                                            				  select them together. You can select a range of items by using the Shift key. |
| Tip | You can select several random field names in the list by holding
                                                            				  down the Ctrl key and then clicking the arrow to
                                                            				  select them together. You can select a range of items by using the Shift key. |
| Step 4 | Click line field names in the Line Field box and click the arrow to move the
                                             			 fields to the Selected Line Fields box. Tip You can change the order of the items in the Selected Line Fields and Selected Device Fields Order boxes. Select
                                                            				  an item and then use the up arrow to move the item closer to the beginning of
                                                            				  the list or the down arrow to move it to the end of the list. | Tip | You can change the order of the items in the Selected Line Fields and Selected Device Fields Order boxes. Select
                                                            				  an item and then use the up arrow to move the item closer to the beginning of
                                                            				  the list or the down arrow to move it to the end of the list. |
| Tip | You can change the order of the items in the Selected Line Fields and Selected Device Fields Order boxes. Select
                                                            				  an item and then use the up arrow to move the item closer to the beginning of
                                                            				  the list or the down arrow to move it to the end of the list. |
| Step 5 | In the IP Phone Services Maximums area, enter the
                                             			 maximum value in the Maximum Number of Lines field. |
| Step 6 | To save your custom file format, click Save . The name of the file format displays in
                                             			 the File Format Names list in the Find and List Remote Destination Profile File
                                                				Formats window. |

| Tip | You can select several random field names in the list by holding
                                                            				  down the Ctrl key and then clicking the arrow to
                                                            				  select them together. You can select a range of items by using the Shift key. |
|---|---|

| Tip | You can change the order of the items in the Selected Line Fields and Selected Device Fields Order boxes. Select
                                                            				  an item and then use the up arrow to move the item closer to the beginning of
                                                            				  the list or the down arrow to move it to the end of the list. |
|---|---|

| Step 1 | Find the Remote Destination Profile file format that
                                             			 you want to copy. |
|---|---|
| Step 2 | In the Search Results area, choose a file format that
                                             			 you want to copy. The Remote Destination Profile File Format
                                                				Configuration window displays. |
| Step 3 | To make a copy of the chosen file format, click Copy . Note To copy the file format, you can also click the corresponding
                                                            				  Copy icon in the Find and List Remote Destination Profile File
                                                               					 Formats window. | Note | To copy the file format, you can also click the corresponding
                                                            				  Copy icon in the Find and List Remote Destination Profile File
                                                               					 Formats window. |
| Note | To copy the file format, you can also click the corresponding
                                                            				  Copy icon in the Find and List Remote Destination Profile File
                                                               					 Formats window. |
| Step 4 | In the Format Name field, enter a new name for the
                                             			 copied format. |
| Step 5 | Modify the copied format using any of these methods: Add new fields by choosing them from the Device Fields or Line Fields box and then clicking the arrow to move the chosen fields into the Selected Device Field or Selected Line Fields Order box. Remove selected fields by choosing them from the Selected Device Fields or Selected Line Fields Order box and then clicking the arrow to move the chosen fields into the Device Fields or Line Fields box . Change the order of the fields by choosing a field name in the Selected Device Fields or Selected Line Fields Order box and using the up or down arrow to change its location. |
| Step 6 | After making your changes, click Save to save the copied file format with
                                             			 changes in the list. |

| Note | To copy the file format, you can also click the corresponding
                                                            				  Copy icon in the Find and List Remote Destination Profile File
                                                               					 Formats window. |
|---|---|

| Step 1 | Find the Remote Destination Profile file format that you want to
                                             			 modify. |
|---|---|
| Step 2 | In the Search Results area, choose a file
                                             			 format that you want to modify. The Remote Destination Profile File Format
                                                				Configuration window displays. |
| Step 3 | Modify the copied format using any of these methods: Add new fields by choosing them from the Device Fields or Line Fields box and then clicking the arrow to move the chosen fields into the Selected Device Field or Selected Line Fields Order box. Remove selected fields by choosing them from the Selected Device Fields or Selected Line Fields Order box and then clicking the arrow to move the chosen fields into the Device Fields or Line Fields box . Note You cannot remove the required fields: Remote Destination Profile Name, and Description. Change the order of the fields by choosing a field name in the Selected Device Fields Order or Selected Line Fields Order box and using the up or down arrow to change its location. | Note | You cannot remove the required fields: Remote Destination Profile Name, and Description. |
| Note | You cannot remove the required fields: Remote Destination Profile Name, and Description. |
| Step 4 | After making your changes, click Save to save the changes to the file format. |

| Note | You cannot remove the required fields: Remote Destination Profile Name, and Description. |
|---|---|

| Step 1 | Find the Remote Destination Profile file format that you want to
                                             			 delete. |
|---|---|
| Step 2 | In the Search Results area, verify that this is the
                                             			 file(s) that you want to delete and check the check box to select the
                                             			 format(s). |
| Step 3 | To remove the file format(s) from the list, click Delete Selected . A message asks you to confirm
                                             			 that you want to delete the file format(s). Click OK to continue. Attention Make sure to browse the entire list of displayed results before
                                                            				  clicking Delete Selected . The system removes the file format(s) name from the list. | Attention | Make sure to browse the entire list of displayed results before
                                                            				  clicking Delete Selected . |
| Attention | Make sure to browse the entire list of displayed results before
                                                            				  clicking Delete Selected . |

| Attention | Make sure to browse the entire list of displayed results before
                                                            				  clicking Delete Selected . |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Mobility > Remote
                                                				  Destination Profile > Remote Destination Profile File
                                                				  Format > Add File Format . Add File Format window displays. |
|---|---|
| Step 2 | In the File Name field, choose the text-based CSV
                                          			 file that you created for this transaction. |
| Step 3 | In the File Format Name field, choose the file format
                                          			 that you created for this type of bulk transaction. |
| Step 4 | To create a job for associating the matching file format with the
                                          			 CSV data file, click Submit . |
| Step 5 | Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                          			 and / or activate this job. |

| Step 1 | Choose Bulk
                                                				  Administration > Mobility > Remote
                                                				  Destination Profile > Remote Destination Profile
                                                				  Insert . The Insert Remote Destination Profile
                                             				Configuration window displays. |
|---|---|
| Step 2 | In the File Name drop-down list box, choose the CSV
                                          			 data file that you created for this specific bulk transaction. |
| Step 3 | In the Remote Destination Profile Template Name drop-down list box, choose the BAT Remote Destination Profile template that you
                                          			 created for this type of bulk transaction. Note Remote Destination Profile template is optional while inserting
                                                         				  Remote Destination Profiles. Ensure that the CSV data file has a 'Desk Phone
                                                         				  Name' when a Remote Destination Profile template is not selected. | Note | Remote Destination Profile template is optional while inserting
                                                         				  Remote Destination Profiles. Ensure that the CSV data file has a 'Desk Phone
                                                         				  Name' when a Remote Destination Profile template is not selected. |
| Note | Remote Destination Profile template is optional while inserting
                                                         				  Remote Destination Profiles. Ensure that the CSV data file has a 'Desk Phone
                                                         				  Name' when a Remote Destination Profile template is not selected. |
| Step 4 | Check the Override the existing configuration check box
                                          			 to overwrite the existing Remote Destination Profile settings with the
                                          			 information that is contained in the file that you want to insert. |
| Step 5 | In the Job Information area, enter the Job description. |
| Step 6 | Choose an insert method. Do one of the following: Click Run Immediately to insert the Remote
                                                				  Destination Profile records immediately. Click Run Later to insert the Remote Destination
                                                				  Profile records at a later time. |
| Step 7 | To create a job for inserting the Remote Destination Profile
                                          			 records, click Submit . |
| Step 8 | To create a job for inserting the gateways, click Submit . Use the Job Scheduler option in the Bulk Administration main menu to schedule and/or
                                          			 activate this job. |

| Note | Remote Destination Profile template is optional while inserting
                                                         				  Remote Destination Profiles. Ensure that the CSV data file has a 'Desk Phone
                                                         				  Name' when a Remote Destination Profile template is not selected. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Mobility > Remote
                                                				  Destination Profile > Remote Destination Profile
                                                				  Delete . The Delete Remote Destination Profile Configuration window displays. |
|---|---|
| Step 2 | In the Delete Remote Destination Profile where drop-down list box, choose the type of custom file that you have created from
                                          			 one of the following criteria: Name Description Device Pool Calling Search Space |
| Step 3 | In the list of custom files, choose the filename of the custom
                                          			 file for this delete. |
| Step 4 | Click Find . A list of RDPs matching your search
                                          			 criteria displays. |
| Step 5 | In the Job Information area, enter the Job description. |
| Step 6 | Choose a delete method. Do one of the following: Click Run Immediately to delete RDP records
                                                				  immediately. Click Run Later to delete RDP records at a later
                                                				  time. |
| Step 7 | Click Submit to create a job for deleting the RDP
                                          			 records. |
| Step 8 | To create a job for inserting the gateways, click Submit . Use the Job Scheduler option in the Bulk Administration main menu to schedule and/or
                                          			 activate this job. |

| Note | If you are accessing help from the second Export Remote Destination Profile Configuration window after selecting the remote destination profile for export, skip to Step 7 . |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Mobility > Remote
                                                				  Destination Profile > Remote Destination Profile
                                                				  Export . The Export Remote Destination Profile
                                             				Configuration window displays. |
|---|---|
| Step 2 | From the first Find Remote Destination Profile where drop-down list, choose one of the following criteria: Name Description Device Pool Calling Search Space From the second Find Remote Destination Profile where drop-down list, choose one of the following criteria: begins with contains ends with is exactly is empty is not empty |
| Step 3 | Specify the appropriate search text, if applicable. Tip To find all Remote Destination Profiles that are registered in
                                                         				  the database, click Find without entering any search text. | Tip | To find all Remote Destination Profiles that are registered in
                                                         				  the database, click Find without entering any search text. |
| Tip | To find all Remote Destination Profiles that are registered in
                                                         				  the database, click Find without entering any search text. |
| Step 4 | To further define your query and to add multiple filters, check the Search Within Results check box, choose AND or OR from the drop-down list, repeat Step 2 and Step 3 . |
| Step 5 | Click Find . A list of discovered Remote Destination Profiles displays by: Name Description Device Pool Calling Search Space Note Make sure to browse the entire list of displayed results before submitting the job. | Note | Make sure to browse the entire list of displayed results before submitting the job. |
| Note | Make sure to browse the entire list of displayed results before submitting the job. |
| Step 6 | Click Next . The next Export Remote Destination Profile
                                                				  Configuration window displays. |
| Step 7 | Enter an export file name in the File Name field. |
| Step 8 | Choose a file format from the File Format drop-down list. |
| Step 9 | In the Job Information area, enter the Job
                                          			 description. Delete Remote Destination Profiles is the default description. |
| Step 10 | Choose an export method. Do one of the following: Click Run Immediately to export Remote
                                                				  Destination Profile records immediately. Click Run Later to export Remote Destination
                                                				  Profile records at a later time. |
| Step 11 | Click Submit to create a job for deleting the Remote
                                          			 Destination Profile records. |
| Step 12 | To schedule and / or activate this job, use the Job
                                          			 Scheduler option in the Bulk Administration main menu. |

| Tip | To find all Remote Destination Profiles that are registered in
                                                         				  the database, click Find without entering any search text. |
|---|---|

| Note | Make sure to browse the entire list of displayed results before submitting the job. |
|---|---|

| Field Types | Exported Fields |
|---|---|
| Device Fields | Remote Destination Profile Name, Description, User ID, Device
                                                					 Pool, CSS, AAR CSS, Media Resource List, User Hold Audio Source, Location,
                                                					 Privacy, Device Presence Group, Rerouting CSS |
| Line Fields | Directory Number, Partition, Voice Mail Profile, Line CSS, AAR
                                                					 Group(Line), Line User Hold Audio Source, Line Network Hold Audio Source,
                                                					 Forward All Destination, Forward All CSS, Forward Busy Internal Destination,
                                                					 Forward Busy Internal CSS, Forward Busy External Destination, Forward Busy
                                                					 External CSS, Forward No Answer Internal Destination, Forward No Answer
                                                					 Internal CSS, Forward No Answer External Destination, Forward No Answer
                                                					 External CSS, Forward No Coverage Internal Destination, Forward No Coverage
                                                					 Internal CSS, Forward No Coverage External Destination, Forward No Coverage
                                                					 External CSS, Forward No Answer Ring Duration, Call Pickup Group, MLPP Target,
                                                					 MLPP CSS, MLPP No Answer Ring Duration, External Phone Number Mask, Maximum
                                                					 Number Of Calls, Busy Trigger, Alerting Name, Alerting Name ASCII, Display,
                                                					 Line Description, Line Presence Group, Secondary CSS For Forward All, ASCII
                                                					 Display, Forward On CTI Failure Destination, Forward On CTI Failure CSS, AAR
                                                					 Destination Mask, Forward Unregistered Internal Destination, Forward
                                                					 Unregistered Internal CSS, Forward Unregistered External Destination, Forward
                                                					 Unregistered External CSS, Hold Reversion Ring Duration, Hold Reversion
                                                					 Notification Interval |