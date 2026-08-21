---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-15-cucm-b-bulk-administration-guide-15-cucm-b-bulk-administration-g-7b3fcd295b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/15/cucm_b_bulk-administration-guide-15/cucm_b_bulk-administration-guide-1251su2_chapter_010111.html
retrieved_at: 2026-08-21T09:17:42.071819+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: October 1, 2024

Chapter: Line Appearance

## Chapter: Line Appearance

# Line Appearance

This chapter provides information to use the Line Appearance
                        		menu in BAT to view, export, and update line appearances.

A line appearance is the linkage of a line to a device. The end
                        		user is now linked to a line appearance rather than a line.

The system did not provide detailed presence information about relationships such as shared lines to Cisco Unified Presence previously, which led to inaccurate or incomplete presence state. The Line Appearance feature provides detailed information
                        are multiple line appearances associate with a user.

## View Line Appearances

Because you might have several line appearance records, Unified Communications Manager lets you locate specific records on the basis of specific criteria.

During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate
                                          to other menu items and return to this menu item, or if you close the browser and then reopen a new browser window, the system
                                          retains your Cisco Unified Communications Manager search preferences until you modify your search.

Step 1

Choose Bulk
                                             				  Administration > Users > Line
                                             				  Appearance > Export Line
                                             				  Appearance .

Step 2

To find all records in the database, ensure the dialog box is
                                       			 empty; go to Step 3 .

To filter or search records

- From the first
                                             				  drop-down list box, select a search parameter.

- From the second
                                             				  drop-down list box, choose a search pattern.

To add additional search criteria click the + button. When you add criteria, the system
                                                            						searches for a record that matches all criteria that you specify. To remove
                                                            						criteria, click the – button to remove the last added criteria
                                                            						or click the Clear Filter button to remove all added search criteria.

Step 3

Click Find .

All or matching records display. You can change the number of
                                          				items that display on each page by choosing a different value from the Rows per Page drop-down list box.

You can delete multiple records from the database by checking
                                                      				  the check boxes next to the appropriate record and clicking Delete Selected . You can delete all
                                                      				  configurable records for this selection by clicking Select All and then clicking Delete Selected .

Step 4

From the list of records that display, click the link for the
                                       			 record that you want to view.

To reverse the sort order, click the up or down arrow, if
                                                      				  available, in the list header.

The window displays the item that you choose.

## Export Line Appearances

Create a text file that lists details of the line appearance that you want to export.

Upload the custom file into Unified Communications Manager first node.

Find the line appearance records you want to export.

After you have selected line appearance items to export, you
                              		  can proceed to export the selected line appearances.

Step 1

After you have located the items to export, click Next .

Step 2

In the In Custom File field, enter the filename for the
                                       			 custom file.

Step 3

In the File Format drop-down list box, choose the
                                       			 file format.

Step 4

Check one or more of the following check boxes:

Export line appearances for Cisco Unified Presence users only—The export operation will only get performed on Cisco Unified Presence users.

Export line appearances for all the primary extensions—Line
                                                					 appearances for all devices that share a line to which a user is associated
                                                					 will get exported.

Export line appearances for the devices associated—Line
                                                					 appearances for all the lines that share a device to which a user is associated
                                                					 will be exported.

Step 5

In the Job Information area, enter the Job description.

Step 6

Choose an export method. Do one of the following:

Click Run Immediately to export line appearances
                                             				  immediately.

Click Run Later to export line appearances at a
                                             				  later time.

Step 7

To create a job for generate reports, click Submit .

To schedule and / or activate this job, use the Job
                                          				Scheduler option in the Bulk Administration main menu.

### What to do next

The log file displays the number of users that were updated and the
                              		  number of records that failed, including an error code.

## Update Line Appearances

Create a text file that lists the following details for the line appearances that you want to update:

User ID

Device

Directory numbers

Partition (optional)

Put each item on a separate line in the text file.

Upload the custom file to Unified Communications Manager server.

You can update line appearances that are listed in a custom file.

Attention

The line must be associated to the end user for the Update Line
                                          			 Appearance transaction to be successful.

Step 1

Choose Bulk
                                             				  Administration > Users > Line
                                             				  Appearance > Update Line
                                             				  Appearance .

Step 2

From the File Name drop-down list box, choose the name
                                       			 of the custom file.

Step 3

Check the following check boxes to select these options, or skip
                                       			 to Step 4 .

If you want to update the line appearance for Cisco Unified Presence users only, check the Update line appearance for CUP users only check box.

If you want to disassociate the line appearance, check the Disassociate line appearances check box.

Step 4

In the Job Information area, enter the Job description.

Step 5

Choose a method to update line appearances. Do one of the
                                       			 following:

Click Run Immediately to update line appearances
                                             				  immediately.

Click Run Later to update line appearances at a
                                             				  later time.

Step 6

To create a job for updating line appearances, click Submit .

| Note | During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate
                                          to other menu items and return to this menu item, or if you close the browser and then reopen a new browser window, the system
                                          retains your Cisco Unified Communications Manager search preferences until you modify your search. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Users > Line
                                             				  Appearance > Export Line
                                             				  Appearance . The Export Users Query window displays. |
|---|---|
| Step 2 | To find all records in the database, ensure the dialog box is
                                       			 empty; go to Step 3 . To filter or search records From the first
                                             				  drop-down list box, select a search parameter. From the second
                                             				  drop-down list box, choose a search pattern. Specify the
                                             				  appropriate search text, if applicable. Note To add additional search criteria click the + button. When you add criteria, the system
                                                            						searches for a record that matches all criteria that you specify. To remove
                                                            						criteria, click the – button to remove the last added criteria
                                                            						or click the Clear Filter button to remove all added search criteria. | Note | To add additional search criteria click the + button. When you add criteria, the system
                                                            						searches for a record that matches all criteria that you specify. To remove
                                                            						criteria, click the – button to remove the last added criteria
                                                            						or click the Clear Filter button to remove all added search criteria. |
| Note | To add additional search criteria click the + button. When you add criteria, the system
                                                            						searches for a record that matches all criteria that you specify. To remove
                                                            						criteria, click the – button to remove the last added criteria
                                                            						or click the Clear Filter button to remove all added search criteria. |
| Step 3 | Click Find . All or matching records display. You can change the number of
                                          				items that display on each page by choosing a different value from the Rows per Page drop-down list box. Note You can delete multiple records from the database by checking
                                                      				  the check boxes next to the appropriate record and clicking Delete Selected . You can delete all
                                                      				  configurable records for this selection by clicking Select All and then clicking Delete Selected . | Note | You can delete multiple records from the database by checking
                                                      				  the check boxes next to the appropriate record and clicking Delete Selected . You can delete all
                                                      				  configurable records for this selection by clicking Select All and then clicking Delete Selected . |
| Note | You can delete multiple records from the database by checking
                                                      				  the check boxes next to the appropriate record and clicking Delete Selected . You can delete all
                                                      				  configurable records for this selection by clicking Select All and then clicking Delete Selected . |
| Step 4 | From the list of records that display, click the link for the
                                       			 record that you want to view. Note To reverse the sort order, click the up or down arrow, if
                                                      				  available, in the list header. The window displays the item that you choose. | Note | To reverse the sort order, click the up or down arrow, if
                                                      				  available, in the list header. |
| Note | To reverse the sort order, click the up or down arrow, if
                                                      				  available, in the list header. |

| Note | To add additional search criteria click the + button. When you add criteria, the system
                                                            						searches for a record that matches all criteria that you specify. To remove
                                                            						criteria, click the – button to remove the last added criteria
                                                            						or click the Clear Filter button to remove all added search criteria. |
|---|---|

| Note | You can delete multiple records from the database by checking
                                                      				  the check boxes next to the appropriate record and clicking Delete Selected . You can delete all
                                                      				  configurable records for this selection by clicking Select All and then clicking Delete Selected . |
|---|---|

| Note | To reverse the sort order, click the up or down arrow, if
                                                      				  available, in the list header. |
|---|---|

| Step 1 | After you have located the items to export, click Next . The Export Line Appearance Configuration window
                                       			 displays. |
|---|---|
| Step 2 | In the In Custom File field, enter the filename for the
                                       			 custom file. |
| Step 3 | In the File Format drop-down list box, choose the
                                       			 file format. The Line Appearance Format is available by default. |
| Step 4 | Check one or more of the following check boxes: Export line appearances for Cisco Unified Presence users only—The export operation will only get performed on Cisco Unified Presence users. Export line appearances for all the primary extensions—Line
                                                					 appearances for all devices that share a line to which a user is associated
                                                					 will get exported. Export line appearances for the devices associated—Line
                                                					 appearances for all the lines that share a device to which a user is associated
                                                					 will be exported. |
| Step 5 | In the Job Information area, enter the Job description. |
| Step 6 | Choose an export method. Do one of the following: Click Run Immediately to export line appearances
                                             				  immediately. Click Run Later to export line appearances at a
                                             				  later time. |
| Step 7 | To create a job for generate reports, click Submit . To schedule and / or activate this job, use the Job
                                          				Scheduler option in the Bulk Administration main menu. |

| Attention | The line must be associated to the end user for the Update Line
                                          			 Appearance transaction to be successful. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Users > Line
                                             				  Appearance > Update Line
                                             				  Appearance . The Update Line Appearance Configuration window
                                       			 displays. |
|---|---|
| Step 2 | From the File Name drop-down list box, choose the name
                                       			 of the custom file. |
| Step 3 | Check the following check boxes to select these options, or skip
                                       			 to Step 4 . If you want to update the line appearance for Cisco Unified Presence users only, check the Update line appearance for CUP users only check box. If you want to disassociate the line appearance, check the Disassociate line appearances check box. |
| Step 4 | In the Job Information area, enter the Job description. |
| Step 5 | Choose a method to update line appearances. Do one of the
                                       			 following: Click Run Immediately to update line appearances
                                             				  immediately. Click Run Later to update line appearances at a
                                             				  later time. |
| Step 6 | To create a job for updating line appearances, click Submit . To schedule and / or activate this job, use the
                                       			 Job Scheduler option in the Bulk Administration main menu. |