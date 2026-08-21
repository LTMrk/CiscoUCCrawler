---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1-cucm-b-bulk-administration-guide-1251-cucm-b-bulk-administra-63930ca951
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1/cucm_b_bulk-administration-guide-1251/cucm_b_bulk-administration-guide-1251_chapter_0100101.html
retrieved_at: 2026-08-21T18:00:10.356955+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: March 4, 2020

Chapter: User Device Profile File Format

## Chapter: User Device Profile File Format

# User Device Profile File Format

This chapter provides information about configuring user device
                        		profile file formats for CSV data files that you create using a text editor.

## User Device Profile File Format Setup

You can copy, modify, and delete user device profile file
                           		formats for CSV data files that you create using a text editor.

When you use a text editor to create your CSV data file, you
                           		must use a file format to identify the device and line fields within the CSV
                           		data file. You have these options for the file format:

Default User Device Profile—Contains a predetermined set of user
                                 			 device profile device and line fields.

Simple User Device Profile—Contains basic device and line fields for
                                 			 user device profiles.

Customized—Contains device and line fields that you choose and order
                                 			 yourself.

Before creating the CSV file in the text editor, you need to
                           		choose an existing file format or create a new file format. You can then enter
                           		the values as specified in the file format in the text-based CSV data file.

### Find UDP File Format

Use BAT to locate a user device profile file format.

Step 1

Choose Bulk Administration > User Device Profiles > UDP File
                                                				  Format > Create UDP File Format .

Step 2

From the Find UDP File Format where Format Name drop-down list box, choose one of the following criteria:

- begins with

- contains

- is exactly

- ends with

- is empty

- is not empty

Step 3

Specify the appropriate search text, if applicable, and click Find .

Tip

To find all UDP templates that are registered in the database,
                                                         				  click Find without entering any search text.

Step 4

From the list of records, click the file format name that matches
                                          			 your search criteria.

### Create UDP File Format

You can create a UDP file format for the text-based CSV data
                                 		  file.

Step 1

Choose Bulk
                                                				  Administration > User Device
                                                				  Profiles > Create UDP File
                                                				  Format .

Step 2

Click Add new .

Step 3

In the UDP File Format Name field, enter a name for
                                          			 this customized format.

Step 4

Under Device Fields , choose the device field names
                                          			 that you want to define for each user device profile.

Click a device field name in the Device Field box and click the arrow to move
                                             				the field to the Selected Device Fields Order box.

A CSV data file must include Device Profile Name , and Description ; therefore, these fields
                                                         				  always remain selected.

Tip

You can select several random field names in the list by holding
                                                         				  down the Ctrl key, then clicking the arrow to
                                                         				  select them together. You can select a range of items by using the Shift key.

Step 5

Click line field names in the Line Field box and click the arrow to move the
                                          			 fields to the Selected Line Fields Order box.

Directory Number is a mandatory field if
                                                         				  you select line fields in the file format.

Tip

You can change the order of the items in the Selected Line Fields and Selected Device Fields boxes. Select an
                                                         				  item and then use the up arrow to move the field closer to the beginning of the
                                                         				  list or use the down arrow to move it to the end of the list.

Step 6

Click Intercom DN field names in the Intercom DN Field box and click the arrow to
                                          			 move the fields to the Selected Intercom DN Fields Order box.

Step 7

Enter the maximum number of lines, speed dials, IP Phone Services,
                                          			 and IP Phone Service Parameters, you want to include in the CSV file, in their
                                          			 corresponding text boxes.

You can enter zero for maximum number of speed dials, IP Phone
                                                         				  Services, and IP Phone Service Parameters, if you do not want to include them
                                                         				  in the CSV file. But, the maximum number of lines should not be zero if line
                                                         				  fields are chosen in the file format.

Step 8

To save your customized file format, click Save .

### Copy UDP File Format

You can copy an existing user device profile file format for
                                 		  the CSV data file.

Step 1

Find the UDP File Format you want to copy.

Step 2

In the Search Results area, click the file format name
                                          			 that you want to copy.

Step 3

To make a copy of the chosen file format, click Copy .

You can also copy a file format by clicking the icon in the Copy
                                                         				  column corresponding to the format you want to copy, in the UDP File Format Query window.

Step 4

In the File Format Name field, enter a new name for
                                          			 the copied format.

Step 5

Modify the copied format by using one of these methods:

Add new fields by choosing them from the Device Fields, Line
                                                				  Fields or Intercom DN Fields box, and then clicking the arrow to move the
                                                				  chosen fields into the Selected Device Fields Order, Selected Line Fields
                                                				  Order, or Selected Intercom DN Order box.

Remove chosen fields by choosing them from the Selected Device
                                                				  Fields Order, Selected Line Fields Order, or Selected Intercom DN Fields Order
                                                				  box, and then clicking the arrow to move the chosen fields into the Device
                                                				  Fields, Line Fields, or Intercom DN Fields box.

Change the order of the fields by choosing a field name in the
                                                				  Selected Device Field Order, Selected Line Fields Order, or Selected Intercom
                                                				  DN Field Order box and using the up or down arrow to change its location.

Step 6

After making your changes, click Save to save the copied file format with
                                          			 changes in the list.

### Modify UDP File Format

You can modify an existing user device profile file format
                                 		  for the CSV data file.

Step 1

Find the UDP File Format you want to update.

Step 2

In the Search result area, click the file format name
                                          			 that you want to modify. The File Format Configuration window displays.

Step 3

Modify the copied format by using one of these methods:

Add new fields by choosing them from the Device Fields, Line
                                                				  Fields, or Intercom DN Fields box, and then clicking the arrow to move the
                                                				  chosen fields into the Selected Device Field Order, Selected Line Fields Order,
                                                				  or Selected Intercom Fields Order box.

Remove the chosen fields by choosing them from the Selected
                                                				  Device Fields Order, Selected Line Fields Order, or Selected Intercom Fields
                                                				  Order box, and then clicking the arrow to move the chosen fields into the
                                                				  Device Field or Line Fields box.

Change the order of the fields by choosing a field name in the
                                                				  Selected Device Field or Selected Line Fields box and using the up or down
                                                				  arrow to change its location.

Step 4

After making your changes, click Save to save the changes to the file format.

### Delete UDP File Format

You can delete an existing user device profile file format
                                 		  for the CSV data file.

Step 1

Find the UDP File Format you want to delete.

Step 2

In the Search result area, click the file format name
                                          			 that you want to delete.

Step 3

To remove the file format from the File Format Name list, click Delete . A message asks you to confirm that you
                                          			 want to delete the file format. Click OK to continue.

The file format name is removed from the list.

Tip

You can also delete a file format by checking the corresponding
                                                         				  check box and clicking Delete . You can delete all the file
                                                         				  formats by clicking Select All and then clicking Delete Selected .

| Step 1 | Choose Bulk Administration > User Device Profiles > UDP File
                                                				  Format > Create UDP File Format . The Find and List UDP File Formats window displays. |
|---|---|
| Step 2 | From the Find UDP File Format where Format Name drop-down list box, choose one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 3 | Specify the appropriate search text, if applicable, and click Find . Tip To find all UDP templates that are registered in the database,
                                                         				  click Find without entering any search text. A list of discovered templates displays by name of the file
                                          			 format. | Tip | To find all UDP templates that are registered in the database,
                                                         				  click Find without entering any search text. |
| Tip | To find all UDP templates that are registered in the database,
                                                         				  click Find without entering any search text. |
| Step 4 | From the list of records, click the file format name that matches
                                          			 your search criteria. The UDP File Format Configuration window displays. |

| Tip | To find all UDP templates that are registered in the database,
                                                         				  click Find without entering any search text. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > User Device
                                                				  Profiles > Create UDP File
                                                				  Format . The Create UDP File Format Configuration window displays. |
|---|---|
| Step 2 | Click Add new . The Create UDP File Format Configuration window
                                          			 displays. |
| Step 3 | In the UDP File Format Name field, enter a name for
                                          			 this customized format. |
| Step 4 | Under Device Fields , choose the device field names
                                          			 that you want to define for each user device profile. Click a device field name in the Device Field box and click the arrow to move
                                             				the field to the Selected Device Fields Order box. Note A CSV data file must include Device Profile Name , and Description ; therefore, these fields
                                                         				  always remain selected. Tip You can select several random field names in the list by holding
                                                         				  down the Ctrl key, then clicking the arrow to
                                                         				  select them together. You can select a range of items by using the Shift key. | Note | A CSV data file must include Device Profile Name , and Description ; therefore, these fields
                                                         				  always remain selected. | Tip | You can select several random field names in the list by holding
                                                         				  down the Ctrl key, then clicking the arrow to
                                                         				  select them together. You can select a range of items by using the Shift key. |
| Note | A CSV data file must include Device Profile Name , and Description ; therefore, these fields
                                                         				  always remain selected. |
| Tip | You can select several random field names in the list by holding
                                                         				  down the Ctrl key, then clicking the arrow to
                                                         				  select them together. You can select a range of items by using the Shift key. |
| Step 5 | Click line field names in the Line Field box and click the arrow to move the
                                          			 fields to the Selected Line Fields Order box. Note Directory Number is a mandatory field if
                                                         				  you select line fields in the file format. Tip You can change the order of the items in the Selected Line Fields and Selected Device Fields boxes. Select an
                                                         				  item and then use the up arrow to move the field closer to the beginning of the
                                                         				  list or use the down arrow to move it to the end of the list. | Note | Directory Number is a mandatory field if
                                                         				  you select line fields in the file format. | Tip | You can change the order of the items in the Selected Line Fields and Selected Device Fields boxes. Select an
                                                         				  item and then use the up arrow to move the field closer to the beginning of the
                                                         				  list or use the down arrow to move it to the end of the list. |
| Note | Directory Number is a mandatory field if
                                                         				  you select line fields in the file format. |
| Tip | You can change the order of the items in the Selected Line Fields and Selected Device Fields boxes. Select an
                                                         				  item and then use the up arrow to move the field closer to the beginning of the
                                                         				  list or use the down arrow to move it to the end of the list. |
| Step 6 | Click Intercom DN field names in the Intercom DN Field box and click the arrow to
                                          			 move the fields to the Selected Intercom DN Fields Order box. |
| Step 7 | Enter the maximum number of lines, speed dials, IP Phone Services,
                                          			 and IP Phone Service Parameters, you want to include in the CSV file, in their
                                          			 corresponding text boxes. Note You can enter zero for maximum number of speed dials, IP Phone
                                                         				  Services, and IP Phone Service Parameters, if you do not want to include them
                                                         				  in the CSV file. But, the maximum number of lines should not be zero if line
                                                         				  fields are chosen in the file format. | Note | You can enter zero for maximum number of speed dials, IP Phone
                                                         				  Services, and IP Phone Service Parameters, if you do not want to include them
                                                         				  in the CSV file. But, the maximum number of lines should not be zero if line
                                                         				  fields are chosen in the file format. |
| Note | You can enter zero for maximum number of speed dials, IP Phone
                                                         				  Services, and IP Phone Service Parameters, if you do not want to include them
                                                         				  in the CSV file. But, the maximum number of lines should not be zero if line
                                                         				  fields are chosen in the file format. |
| Step 8 | To save your customized file format, click Save . The name of the file format displays in the UDP File Format Query window. |

| Note | A CSV data file must include Device Profile Name , and Description ; therefore, these fields
                                                         				  always remain selected. |
|---|---|

| Tip | You can select several random field names in the list by holding
                                                         				  down the Ctrl key, then clicking the arrow to
                                                         				  select them together. You can select a range of items by using the Shift key. |
|---|---|

| Note | Directory Number is a mandatory field if
                                                         				  you select line fields in the file format. |
|---|---|

| Tip | You can change the order of the items in the Selected Line Fields and Selected Device Fields boxes. Select an
                                                         				  item and then use the up arrow to move the field closer to the beginning of the
                                                         				  list or use the down arrow to move it to the end of the list. |
|---|---|

| Note | You can enter zero for maximum number of speed dials, IP Phone
                                                         				  Services, and IP Phone Service Parameters, if you do not want to include them
                                                         				  in the CSV file. But, the maximum number of lines should not be zero if line
                                                         				  fields are chosen in the file format. |
|---|---|

| Step 1 | Find the UDP File Format you want to copy. |
|---|---|
| Step 2 | In the Search Results area, click the file format name
                                          			 that you want to copy. The File Format Configuration window displays. |
| Step 3 | To make a copy of the chosen file format, click Copy . Note You can also copy a file format by clicking the icon in the Copy
                                                         				  column corresponding to the format you want to copy, in the UDP File Format Query window. | Note | You can also copy a file format by clicking the icon in the Copy
                                                         				  column corresponding to the format you want to copy, in the UDP File Format Query window. |
| Note | You can also copy a file format by clicking the icon in the Copy
                                                         				  column corresponding to the format you want to copy, in the UDP File Format Query window. |
| Step 4 | In the File Format Name field, enter a new name for
                                          			 the copied format. |
| Step 5 | Modify the copied format by using one of these methods: Add new fields by choosing them from the Device Fields, Line
                                                				  Fields or Intercom DN Fields box, and then clicking the arrow to move the
                                                				  chosen fields into the Selected Device Fields Order, Selected Line Fields
                                                				  Order, or Selected Intercom DN Order box. Remove chosen fields by choosing them from the Selected Device
                                                				  Fields Order, Selected Line Fields Order, or Selected Intercom DN Fields Order
                                                				  box, and then clicking the arrow to move the chosen fields into the Device
                                                				  Fields, Line Fields, or Intercom DN Fields box. Change the order of the fields by choosing a field name in the
                                                				  Selected Device Field Order, Selected Line Fields Order, or Selected Intercom
                                                				  DN Field Order box and using the up or down arrow to change its location. |
| Step 6 | After making your changes, click Save to save the copied file format with
                                          			 changes in the list. |

| Note | You can also copy a file format by clicking the icon in the Copy
                                                         				  column corresponding to the format you want to copy, in the UDP File Format Query window. |
|---|---|

| Step 1 | Find the UDP File Format you want to update. |
|---|---|
| Step 2 | In the Search result area, click the file format name
                                          			 that you want to modify. The File Format Configuration window displays. |
| Step 3 | Modify the copied format by using one of these methods: Add new fields by choosing them from the Device Fields, Line
                                                				  Fields, or Intercom DN Fields box, and then clicking the arrow to move the
                                                				  chosen fields into the Selected Device Field Order, Selected Line Fields Order,
                                                				  or Selected Intercom Fields Order box. Remove the chosen fields by choosing them from the Selected
                                                				  Device Fields Order, Selected Line Fields Order, or Selected Intercom Fields
                                                				  Order box, and then clicking the arrow to move the chosen fields into the
                                                				  Device Field or Line Fields box. Change the order of the fields by choosing a field name in the
                                                				  Selected Device Field or Selected Line Fields box and using the up or down
                                                				  arrow to change its location. |
| Step 4 | After making your changes, click Save to save the changes to the file format. . |

| Step 1 | Find the UDP File Format you want to delete. |
|---|---|
| Step 2 | In the Search result area, click the file format name
                                          			 that you want to delete. The File Format Configuration window displays.
                                          			 Verify that you want to delete this file. |
| Step 3 | To remove the file format from the File Format Name list, click Delete . A message asks you to confirm that you
                                          			 want to delete the file format. Click OK to continue. The file format name is removed from the list. Tip You can also delete a file format by checking the corresponding
                                                         				  check box and clicking Delete . You can delete all the file
                                                         				  formats by clicking Select All and then clicking Delete Selected . | Tip | You can also delete a file format by checking the corresponding
                                                         				  check box and clicking Delete . You can delete all the file
                                                         				  formats by clicking Select All and then clicking Delete Selected . |
| Tip | You can also delete a file format by checking the corresponding
                                                         				  check box and clicking Delete . You can delete all the file
                                                         				  formats by clicking Select All and then clicking Delete Selected . |

| Tip | You can also delete a file format by checking the corresponding
                                                         				  check box and clicking Delete . You can delete all the file
                                                         				  formats by clicking Select All and then clicking Delete Selected . |
|---|---|