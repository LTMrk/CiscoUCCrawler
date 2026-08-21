---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-12-5-su6-cucm-b-bulk-administration-guide-1251su6-cucm-b-bulk-admin-98955e153e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/12_5_SU6/cucm_b_bulk-administration-guide-1251su6/cucm_b_bulk-administration-guide-1251su2_chapter_0110001.html
retrieved_at: 2026-08-21T08:57:03.379492+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: February 15, 2022

Chapter: Gateway File Format

## Chapter: Gateway File Format

# Gateway File Format

This chapter provides information to use Cisco Unified Communications Manager Bulk Administration (BAT) to configure Cisco
                        		gateway file formats in the Cisco Unified Communications Manager database in batches.

## Find Gateway File Format

Use BAT to find a gateway file format.

Choose Bulk
                                             				  Administration > Gateways > Gateway
                                             				  File Format > Create File Format .

Do one of the following:

To find all records in the database, ensure the dialog box is
                                             				  empty; go to Step 3 .

To filter or search records:

- From the first
                                                   						drop-down list box, select a search parameter.

- From the second
                                                   						drop-down list box, choose a search pattern.

To add additional search criteria click the + button. When you add criteria, the
                                                                  							 system searches for a record that matches all criteria that you specify. To
                                                                  							 remove criteria, click the – button to remove the last added criteria or click
                                                                  							 the Clear Filter button to remove all
                                                                  							 added search criteria.

Click Find .

All or matching records display. You can change the number of
                                          				items that display on each page by choosing a different value from the Rows per
                                          				Page drop-down list box.

You can delete multiple records from the database by checking
                                                      				  the check boxes next to the appropriate record and clicking Delete Selected . You can delete all
                                                      				  configurable records for this selection by clicking Select All and then clicking Delete Selected .

From the list of records that display, click the link for the
                                       			 record you want to view.

To reverse the sort order, click the up or down arrow, if
                                                      				  available, in the list header.

## Gateway File Format Configuration

You can use BAT to create, copy, modify, or delete a gateway
                           		file format.

### Create Gateway File Format for CSV Data File

You can create a gateway file format for the text-based CSV
                                 		  data file.

Choose Bulk
                                                				  Administration > Gateways > Gateway
                                                				  File Format > Create File Format .

Click Add New .

In the Format Name field, enter a name for this
                                          			 custom format.

Under Device Fields , choose the device field names
                                          			 that you want to define for each gateway. In the Device Field box, click a device field name
                                          			 and click the arrow to move the field to the Selected Device Fields box.

Gateway Name and Description are always selected.

You can select several random field names in the list by holding
                                                         				  down the Ctrl key, and then clicking the arrow to select them
                                                         				  together. You can select a range of items by using the Shift key.

Click line field names in the Line Field box and click the arrow to move the
                                          			 fields to the Selected Line Fields box.

Make sure that you select Directory Number if you select Line for
                                                         				  the file format.

You can change the order of the items in the Selected Line Fields and Selected Device Fields Order boxes. Select
                                                         				  an item and then use the up arrow to move the field closer to the beginning of
                                                         				  the list or the down arrow to move it to the end of the list.

In the IP Phone Lines Maximums area, enter the maximum
                                          			 values for the Maximum Number of Lines field.

To save your custom file format, click Save . The name of the file format displays in
                                          			 the File Format Names list in the Gateway File Format Find and List window.

### Copy Existing Gateway File Format

You can copy an existing gateway file format.

Find the gateway file format you want to copy.

In the Search Results area, choose a file format that
                                          			 you want to copy.

To make a copy of the chosen file format, click Copy .

To copy the file format, you can also click the corresponding
                                                         				  Copy icon in the Gateway File Format Find and List window.

In the Format Name field, enter a new name for the
                                          			 copied format.

After making your changes, click Save to save the copied file format with
                                          			 changes in the list.

### Modify Existing Gateway File Format

Use BAT to modify an existing gateway file format. You can
                                 		  modify custom file formats only.

Find the gateway file format that you want to modify.

In the Search Results area, choose a file format that
                                          			 you want to modify.

Modify the format using the following methods:

To add new fields, choose them from the Device Fields or Line Fields box, then click the arrow to
                                                				  move the chosen fields into the Selected Device Field or Selected Line Fields Order box.

To remove fields, choose them from the Selected Device Fields or Selected Line Fields Order box, then click
                                                				  the arrow to move the selected fields into the Device Field or Line Fields box.

You cannot remove the required fields: Gateway Name and
                                                               						Description.

To change the order of the fields, choose a field name in the Selected Device Fields Order or Selected Line Fields Order box and use the
                                                				  up or down arrow to change its location.

After making your changes, click Save to save the changes to the file format.

### Delete File Format From CSV Data File

Use BAT to delete an existing file format for the CSV data
                                 		  file. You can delete only custom formats.

Find the gateway file format that you want to delete.

In the Search Results area, verify that this is the
                                          			 file(s) that you want to delete.

To remove the file format(s) from the list, click Delete Selected . A message asks you to confirm
                                          			 that you want to delete the file format(s). Click OK to continue.

Make sure to browse the entire list of displayed results before
                                                         				  clicking Delete Selected .

## Associate File Format with CSV Data File

You can add the file format with the text-based CSV data
                              		  file.

When you used a text editor to create the CSV data file, you created
                              		  a file format for entering values in the text-based file. You entered values in
                              		  the text file in the order that the file format specified

After the CSV data file is completed, you need to associate
                              		  the file format with the text-based CSV data file. After associating the file
                              		  format with the CSV file, the names for each field display as the first record
                              		  in the CSV data file. You can use this information to verify that you entered
                              		  the values for each field in the correct order.

Choose Bulk
                                             				  Administration > Gateways > Gateway
                                             				  File Format > Add File Format .

In the File Name field, choose the text-based CSV
                                       			 file that you created for this transaction.

In the Format File Name field, choose the file format
                                       			 that you created for this type of bulk transaction.

To create a job for associating the matching file format with the
                                       			 CSV data file, click Submit .

| Step 1 | Choose Bulk
                                             				  Administration > Gateways > Gateway
                                             				  File Format > Create File Format . The Gateway File Format Find and List window
                                       			 displays. |
|---|---|
| Step 2 | Do one of the following: To find all records in the database, ensure the dialog box is
                                             				  empty; go to Step 3 . To filter or search records: From the first
                                                   						drop-down list box, select a search parameter. From the second
                                                   						drop-down list box, choose a search pattern. Specify the
                                                   						appropriate search text, if applicable. Note To add additional search criteria click the + button. When you add criteria, the
                                                                  							 system searches for a record that matches all criteria that you specify. To
                                                                  							 remove criteria, click the – button to remove the last added criteria or click
                                                                  							 the Clear Filter button to remove all
                                                                  							 added search criteria. | Note | To add additional search criteria click the + button. When you add criteria, the
                                                                  							 system searches for a record that matches all criteria that you specify. To
                                                                  							 remove criteria, click the – button to remove the last added criteria or click
                                                                  							 the Clear Filter button to remove all
                                                                  							 added search criteria. |
| Note | To add additional search criteria click the + button. When you add criteria, the
                                                                  							 system searches for a record that matches all criteria that you specify. To
                                                                  							 remove criteria, click the – button to remove the last added criteria or click
                                                                  							 the Clear Filter button to remove all
                                                                  							 added search criteria. |
| Step 3 | Click Find . All or matching records display. You can change the number of
                                          				items that display on each page by choosing a different value from the Rows per
                                          				Page drop-down list box. Note You can delete multiple records from the database by checking
                                                      				  the check boxes next to the appropriate record and clicking Delete Selected . You can delete all
                                                      				  configurable records for this selection by clicking Select All and then clicking Delete Selected . | Note | You can delete multiple records from the database by checking
                                                      				  the check boxes next to the appropriate record and clicking Delete Selected . You can delete all
                                                      				  configurable records for this selection by clicking Select All and then clicking Delete Selected . |
| Note | You can delete multiple records from the database by checking
                                                      				  the check boxes next to the appropriate record and clicking Delete Selected . You can delete all
                                                      				  configurable records for this selection by clicking Select All and then clicking Delete Selected . |
| Step 4 | From the list of records that display, click the link for the
                                       			 record you want to view. Tip To reverse the sort order, click the up or down arrow, if
                                                      				  available, in the list header. The window displays the item that you choose. | Tip | To reverse the sort order, click the up or down arrow, if
                                                      				  available, in the list header. |
| Tip | To reverse the sort order, click the up or down arrow, if
                                                      				  available, in the list header. |

| Note | To add additional search criteria click the + button. When you add criteria, the
                                                                  							 system searches for a record that matches all criteria that you specify. To
                                                                  							 remove criteria, click the – button to remove the last added criteria or click
                                                                  							 the Clear Filter button to remove all
                                                                  							 added search criteria. |
|---|---|

| Note | You can delete multiple records from the database by checking
                                                      				  the check boxes next to the appropriate record and clicking Delete Selected . You can delete all
                                                      				  configurable records for this selection by clicking Select All and then clicking Delete Selected . |
|---|---|

| Tip | To reverse the sort order, click the up or down arrow, if
                                                      				  available, in the list header. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Gateways > Gateway
                                                				  File Format > Create File Format . |
|---|---|
| Step 2 | Click Add New . The Create Gateway File Format window displays. |
| Step 3 | In the Format Name field, enter a name for this
                                          			 custom format. |
| Step 4 | Under Device Fields , choose the device field names
                                          			 that you want to define for each gateway. In the Device Field box, click a device field name
                                          			 and click the arrow to move the field to the Selected Device Fields box. Gateway Name and Description are always selected. Tip You can select several random field names in the list by holding
                                                         				  down the Ctrl key, and then clicking the arrow to select them
                                                         				  together. You can select a range of items by using the Shift key. | Tip | You can select several random field names in the list by holding
                                                         				  down the Ctrl key, and then clicking the arrow to select them
                                                         				  together. You can select a range of items by using the Shift key. |
| Tip | You can select several random field names in the list by holding
                                                         				  down the Ctrl key, and then clicking the arrow to select them
                                                         				  together. You can select a range of items by using the Shift key. |
| Step 5 | Click line field names in the Line Field box and click the arrow to move the
                                          			 fields to the Selected Line Fields box. Note Make sure that you select Directory Number if you select Line for
                                                         				  the file format. Tip You can change the order of the items in the Selected Line Fields and Selected Device Fields Order boxes. Select
                                                         				  an item and then use the up arrow to move the field closer to the beginning of
                                                         				  the list or the down arrow to move it to the end of the list. | Note | Make sure that you select Directory Number if you select Line for
                                                         				  the file format. | Tip | You can change the order of the items in the Selected Line Fields and Selected Device Fields Order boxes. Select
                                                         				  an item and then use the up arrow to move the field closer to the beginning of
                                                         				  the list or the down arrow to move it to the end of the list. |
| Note | Make sure that you select Directory Number if you select Line for
                                                         				  the file format. |
| Tip | You can change the order of the items in the Selected Line Fields and Selected Device Fields Order boxes. Select
                                                         				  an item and then use the up arrow to move the field closer to the beginning of
                                                         				  the list or the down arrow to move it to the end of the list. |
| Step 6 | In the IP Phone Lines Maximums area, enter the maximum
                                          			 values for the Maximum Number of Lines field. |
| Step 7 | To save your custom file format, click Save . The name of the file format displays in
                                          			 the File Format Names list in the Gateway File Format Find and List window. |

| Tip | You can select several random field names in the list by holding
                                                         				  down the Ctrl key, and then clicking the arrow to select them
                                                         				  together. You can select a range of items by using the Shift key. |
|---|---|

| Note | Make sure that you select Directory Number if you select Line for
                                                         				  the file format. |
|---|---|

| Tip | You can change the order of the items in the Selected Line Fields and Selected Device Fields Order boxes. Select
                                                         				  an item and then use the up arrow to move the field closer to the beginning of
                                                         				  the list or the down arrow to move it to the end of the list. |
|---|---|

| Step 1 | Find the gateway file format you want to copy. |
|---|---|
| Step 2 | In the Search Results area, choose a file format that
                                          			 you want to copy. The Gateway File Format Configuration window
                                          			 displays. |
| Step 3 | To make a copy of the chosen file format, click Copy . Tip To copy the file format, you can also click the corresponding
                                                         				  Copy icon in the Gateway File Format Find and List window. | Tip | To copy the file format, you can also click the corresponding
                                                         				  Copy icon in the Gateway File Format Find and List window. |
| Tip | To copy the file format, you can also click the corresponding
                                                         				  Copy icon in the Gateway File Format Find and List window. |
| Step 4 | In the Format Name field, enter a new name for the
                                          			 copied format. |
| Step 5 | After making your changes, click Save to save the copied file format with
                                          			 changes in the list. |

| Tip | To copy the file format, you can also click the corresponding
                                                         				  Copy icon in the Gateway File Format Find and List window. |
|---|---|

| Step 1 | Find the gateway file format that you want to modify. |
|---|---|
| Step 2 | In the Search Results area, choose a file format that
                                          			 you want to modify. The Gateway File Format Configuration window
                                          			 displays. |
| Step 3 | Modify the format using the following methods: To add new fields, choose them from the Device Fields or Line Fields box, then click the arrow to
                                                				  move the chosen fields into the Selected Device Field or Selected Line Fields Order box. To remove fields, choose them from the Selected Device Fields or Selected Line Fields Order box, then click
                                                				  the arrow to move the selected fields into the Device Field or Line Fields box. Note You cannot remove the required fields: Gateway Name and
                                                               						Description. To change the order of the fields, choose a field name in the Selected Device Fields Order or Selected Line Fields Order box and use the
                                                				  up or down arrow to change its location. | Note | You cannot remove the required fields: Gateway Name and
                                                               						Description. |
| Note | You cannot remove the required fields: Gateway Name and
                                                               						Description. |
| Step 4 | After making your changes, click Save to save the changes to the file format. |

| Note | You cannot remove the required fields: Gateway Name and
                                                               						Description. |
|---|---|

| Step 1 | Find the gateway file format that you want to delete. |
|---|---|
| Step 2 | In the Search Results area, verify that this is the
                                          			 file(s) that you want to delete. |
| Step 3 | To remove the file format(s) from the list, click Delete Selected . A message asks you to confirm
                                          			 that you want to delete the file format(s). Click OK to continue. Note Make sure to browse the entire list of displayed results before
                                                         				  clicking Delete Selected . The system removes the file format(s) name from the list. | Note | Make sure to browse the entire list of displayed results before
                                                         				  clicking Delete Selected . |
| Note | Make sure to browse the entire list of displayed results before
                                                         				  clicking Delete Selected . |

| Note | Make sure to browse the entire list of displayed results before
                                                         				  clicking Delete Selected . |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Gateways > Gateway
                                             				  File Format > Add File Format . Add Gateway File Format window displays. |
|---|---|
| Step 2 | In the File Name field, choose the text-based CSV
                                       			 file that you created for this transaction. |
| Step 3 | In the Format File Name field, choose the file format
                                       			 that you created for this type of bulk transaction. |
| Step 4 | To create a job for associating the matching file format with the
                                       			 CSV data file, click Submit . Use the Job Scheduler option in the Bulk Administration main menu to schedule
                                       			 and / or activate this job. |