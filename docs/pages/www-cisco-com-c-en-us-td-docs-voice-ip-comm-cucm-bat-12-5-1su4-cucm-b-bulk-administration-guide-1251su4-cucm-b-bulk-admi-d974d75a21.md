---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-1su4-cucm-b-bulk-administration-guide-1251su4-cucm-b-bulk-admi-d974d75a21
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_1SU4/cucm_b_bulk-administration-guide-1251su4/cucm_b_bulk-administration-guide-1251su2_chapter_0100.html
retrieved_at: 2026-08-21T17:49:41.819199+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: February 22, 2021

Chapter: Phone File Formats

## Chapter: Phone File Formats

# Phone File Formats

This chapter provides information about configuring file formats
                        		for CSV data files that are created using a text editor.

## Text Editors for Phone CSV Data File Creation

You can create the CSV data file by using lines of ASCII text
                              		  with values separated by commas. The comma separated values (CSV) file provides
                              		  textual information in tabular form.

Default Phone —Contains a predetermined set of
                                       		phone device and line fields.

Simple Phone —Contains basic device and line fields
                                       		for phones.

Custom —Contains device and line fields that you
                                       		choose and order yourself.

You cannot modify or delete the Simple Phone or Default Phone
                              		  file formats.

When you use the Unified Communications Manager Bulk Administration (BAT) spreadsheet to create the CSV data file, you can create the file format within the spreadsheet.
                                          When you use a text editor to create the CSV data file, you need to create a file format or use the simple or default file
                                          format. You enter the values in the text-based file in the same order as specified in the file format.

## Find Phone File Formats

You can use the BAT to find a phone file format.

Choose Bulk
                                             				  Administration > Phones > Phone File
                                             				  Format > Create File Format .

From the Find Phone File Format where Format Name drop-down list box, choose one of the following criteria:

- begins
                                                				with

- contains

- is
                                                				exactly

- ends
                                                				with

- is
                                                				empty

- is not
                                                				empty

Specify the appropriate search text, if applicable, and click Find.

To find all phone formats, click Find without entering any search text.

To further define your query and to add multiple filters, check
                                       			 the Search Within Results check box and choose AND or OR from the drop-down box, and repeat Step 2 and Step 3 .

To clear the text specified, click Clear Filter .

From the list of records, click the file format name that matches
                                       			 your search criteria.

## Configure Phone File Format for CSV Data File

You can create, copy, modify, and delete a phone file format
                              		  for a CSV data file.

### Create Custom Phone File Format Using Text Editor

You can use a text editor to create a custom phone file
                                 		  format for the text-based CSV data file.

Choose Bulk
                                                				  Administration > Phones > Phone File
                                                				  Format > Create File Format .

Click Add New .

In the Format Name field, enter a name for this
                                          			 custom format.

Choose the fields to appear in the custom file format. Do the
                                          			 following:

To choose the device fields, click a device field name in
                                                				  the Device Field box and then click the arrow to move
                                                				  the field to the Selected Device Fields box.

A CSV data file must include MAC Address/Device Name and Description ; therefore, these fields
                                                   					 always remain selected.

To select a range of items in the list, hold down the Shift key. To select random field
                                                               						names, hold down the Ctrl key and click field names.

Click a line field name in the Line Field box and click the arrow to move
                                                				  the field to the Selected Line Fields box.

Click the intercom DN field names in the Intercom DN Fields box and click the arrow
                                                				  to move the fields to the Selected Intercom DN Fields Order box.

You can change the order of the items in the Selected Line Fields , Selected Device Fields , and Selected Intercom DN Fields Order boxes. Choose an item and use the up and down arrows to move the field up or
                                                               						down in the list.

In the IP Phone Services Maximums area, enter the
                                          			 maximum values for the following fields:

Maximum Number of Speed Dials

Maximum Number of BLF Speed Dials

Maximum Number of BLF Directed Call Parks

Maximum Number of IP Phone Services

Maximum Number of IP Phone Service Parameters

Click Save .

### Copy Custom Phone File Format for CSV Data File

You can copy an existing custom phone file format for the
                                 		  text-based CSV data file.

Find the phone file format that you want to copy.

In the Search Results area, choose the file format that
                                          			 you want to copy.

To make a copy of the chosen file format, click Copy .

You can also click the corresponding Copy icon in the Find and List Phone File Formats window to
                                                         				  copy the file format.

In the Format Name field, enter a new name for the
                                          			 copied format.

Modify the fields that appear in the copied file format. Do the
                                          			 following:

To add new fields to the file format, click the field name in
                                                				  the Device Fields , Line Fields , or Intercom DN Fields box and then click the
                                                				  arrow to move the field to the Selected Device Field , Selected Line Fields , or Selected Intercom DN Fields Order box.

To remove fields from the file format, click the field name in
                                                				  the Selected Device Fields , Selected Line Fields , or Selected Intercom DN Fields Order box and
                                                				  then click the arrow to move the field to the Device Fields , Line Fields , or Intercom DN Fields box.

You cannot remove the required fields: Number of lines, MAC
                                                               						address, and description.

To change the order of items in the Selected Device Fields , Selected Line Fields , and Selected Intercom DN Fields Order boxes,
                                                				  choose an item and use the up and down arrows to move the field up or down in
                                                				  the list.

Click Save .

### Modify Custom File Format for CSV Data File

You can modify an existing custom file format for the
                                 		  text-based CSV data file. You can modify custom formats only.

Find the phone file format that you want to modify.

In the Search Results area, choose the file format that
                                          			 you want to modify.

To modify the fields that appear in the file format, do the
                                          			 following:

To add new fields to the file format, click the field name in
                                                				  the Device Fields , Line Fields , or Intercom DN Fields box and then click the
                                                				  arrow to move the field to the Selected Device Field , Selected Line Fields , or Selected Intercom DN Fields Order box.

To remove fields from the file format, click the field name in
                                                				  the Selected Device Fields , Selected Line Fields , or Selected Intercom DN Fields Order box and
                                                				  then click the arrow to move the field to the Device Fields , Line Fields , or Intercom DN Fields box.

You cannot remove the required fields: Number of lines, MAC
                                                               						address, and description.

To change the order of items in the Selected Device Fields , Selected Line Fields , and Selected Intercom DN Fields Order boxes,
                                                				  choose an item and use the up and down arrows to move the field up or down in
                                                				  the list.

Click Save .

### Delete Existing CSV Data File Format

You can delete an existing custom file format for the CSV
                                 		  data file. You can delete only custom formats.

Find the phone file format that you want to edit.

In the Search Results area, verify that this is the
                                          			 file(s) that you want to delete.

To remove the file format(s) from the list, click Delete Selected. A message asks you to confirm that you want to
                                          			 delete the file format(s). Click OK to continue.

Make sure you browse the entire list of displayed results before
                                                         				  you click Delete Selected .

## Associate Text-Based File Format with CSV Data File

When you used a text editor to create the CSV data file, you
                              		  created a file format for entering values in the text-based file. You entered
                              		  values in the text file in the order that the file format specified

After the CSV data file is completed, you need to associate
                              		  the file format with the text-based CSV data file. After associating the file
                              		  format with the CSV file, the names for each field display as the first record
                              		  in the CSV data file. You can use this information to verify that you entered
                              		  the values for each field in the correct order.

Choose Bulk Administration > Phones > Phone
                                             				  File Format > Add File Format .
                                       			 Add File Format window displays.

In the File Name field, choose the text-based CSV
                                       			 file that you created for this transaction.

In the Format File Name field, choose the file format
                                       			 that you created for this type of bulk transaction.

In the Job Information area, enter the job description.

To create a job for associating the matching file format with the
                                       			 CSV data file, click Submit .

| Note | When you use the Unified Communications Manager Bulk Administration (BAT) spreadsheet to create the CSV data file, you can create the file format within the spreadsheet.
                                          When you use a text editor to create the CSV data file, you need to create a file format or use the simple or default file
                                          format. You enter the values in the text-based file in the same order as specified in the file format. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Phones > Phone File
                                             				  Format > Create File Format . The Find and List Phone File Formats window
                                       			 displays. |
|---|---|
| Step 2 | From the Find Phone File Format where Format Name drop-down list box, choose one of the following criteria: begins
                                                				with contains is
                                                				exactly ends
                                                				with is
                                                				empty is not
                                                				empty |
| Step 3 | Specify the appropriate search text, if applicable, and click Find. Tip To find all phone formats, click Find without entering any search text. | Tip | To find all phone formats, click Find without entering any search text. |
| Tip | To find all phone formats, click Find without entering any search text. |
| Step 4 | To further define your query and to add multiple filters, check
                                       			 the Search Within Results check box and choose AND or OR from the drop-down box, and repeat Step 2 and Step 3 . Tip To clear the text specified, click Clear Filter . | Tip | To clear the text specified, click Clear Filter . |
| Tip | To clear the text specified, click Clear Filter . |
| Step 5 | From the list of records, click the file format name that matches
                                       			 your search criteria. The Create Phone File Format Configuration window
                                       			 displays. |

| Tip | To find all phone formats, click Find without entering any search text. |
|---|---|

| Tip | To clear the text specified, click Clear Filter . |
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

| Step 1 | Find the phone file format that you want to copy. |
|---|---|
| Step 2 | In the Search Results area, choose the file format that
                                          			 you want to copy. The Phone File Format Configuration window displays. |
| Step 3 | To make a copy of the chosen file format, click Copy . Tip You can also click the corresponding Copy icon in the Find and List Phone File Formats window to
                                                         				  copy the file format. | Tip | You can also click the corresponding Copy icon in the Find and List Phone File Formats window to
                                                         				  copy the file format. |
| Tip | You can also click the corresponding Copy icon in the Find and List Phone File Formats window to
                                                         				  copy the file format. |
| Step 4 | In the Format Name field, enter a new name for the
                                          			 copied format. |
| Step 5 | Modify the fields that appear in the copied file format. Do the
                                          			 following: To add new fields to the file format, click the field name in
                                                				  the Device Fields , Line Fields , or Intercom DN Fields box and then click the
                                                				  arrow to move the field to the Selected Device Field , Selected Line Fields , or Selected Intercom DN Fields Order box. To remove fields from the file format, click the field name in
                                                				  the Selected Device Fields , Selected Line Fields , or Selected Intercom DN Fields Order box and
                                                				  then click the arrow to move the field to the Device Fields , Line Fields , or Intercom DN Fields box. Note You cannot remove the required fields: Number of lines, MAC
                                                               						address, and description. To change the order of items in the Selected Device Fields , Selected Line Fields , and Selected Intercom DN Fields Order boxes,
                                                				  choose an item and use the up and down arrows to move the field up or down in
                                                				  the list. | Note | You cannot remove the required fields: Number of lines, MAC
                                                               						address, and description. |
| Note | You cannot remove the required fields: Number of lines, MAC
                                                               						address, and description. |
| Step 6 | Click Save . The edited copy of the file format is saved. |

| Tip | You can also click the corresponding Copy icon in the Find and List Phone File Formats window to
                                                         				  copy the file format. |
|---|---|

| Note | You cannot remove the required fields: Number of lines, MAC
                                                               						address, and description. |
|---|---|

| Step 1 | Find the phone file format that you want to modify. |
|---|---|
| Step 2 | In the Search Results area, choose the file format that
                                          			 you want to modify. The Phone File Format Configuration window displays. |
| Step 3 | To modify the fields that appear in the file format, do the
                                          			 following: To add new fields to the file format, click the field name in
                                                				  the Device Fields , Line Fields , or Intercom DN Fields box and then click the
                                                				  arrow to move the field to the Selected Device Field , Selected Line Fields , or Selected Intercom DN Fields Order box. To remove fields from the file format, click the field name in
                                                				  the Selected Device Fields , Selected Line Fields , or Selected Intercom DN Fields Order box and
                                                				  then click the arrow to move the field to the Device Fields , Line Fields , or Intercom DN Fields box. Note You cannot remove the required fields: Number of lines, MAC
                                                               						address, and description. To change the order of items in the Selected Device Fields , Selected Line Fields , and Selected Intercom DN Fields Order boxes,
                                                				  choose an item and use the up and down arrows to move the field up or down in
                                                				  the list. | Note | You cannot remove the required fields: Number of lines, MAC
                                                               						address, and description. |
| Note | You cannot remove the required fields: Number of lines, MAC
                                                               						address, and description. |
| Step 4 | Click Save . The changes to the custom file format are saved. |

| Note | You cannot remove the required fields: Number of lines, MAC
                                                               						address, and description. |
|---|---|

| Step 1 | Find the phone file format that you want to edit. |
|---|---|
| Step 2 | In the Search Results area, verify that this is the
                                          			 file(s) that you want to delete. |
| Step 3 | To remove the file format(s) from the list, click Delete Selected. A message asks you to confirm that you want to
                                          			 delete the file format(s). Click OK to continue. Tip Make sure you browse the entire list of displayed results before
                                                         				  you click Delete Selected . The system removes the file format(s) name from the list. | Tip | Make sure you browse the entire list of displayed results before
                                                         				  you click Delete Selected . |
| Tip | Make sure you browse the entire list of displayed results before
                                                         				  you click Delete Selected . |

| Tip | Make sure you browse the entire list of displayed results before
                                                         				  you click Delete Selected . |
|---|---|

| Step 1 | Choose Bulk Administration > Phones > Phone
                                             				  File Format > Add File Format .
                                       			 Add File Format window displays. |
|---|---|
| Step 2 | In the File Name field, choose the text-based CSV
                                       			 file that you created for this transaction. |
| Step 3 | In the Format File Name field, choose the file format
                                       			 that you created for this type of bulk transaction. |
| Step 4 | In the Job Information area, enter the job description. |
| Step 5 | To create a job for associating the matching file format with the
                                       			 CSV data file, click Submit . Use the Job Scheduler option in the Bulk Administration main menu
                                       			 to schedule and / or activate this job. |