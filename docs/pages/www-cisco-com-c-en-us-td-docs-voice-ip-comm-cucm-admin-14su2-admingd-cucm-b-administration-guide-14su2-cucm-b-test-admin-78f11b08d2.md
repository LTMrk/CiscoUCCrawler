---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-14su2-admingd-cucm-b-administration-guide-14su2-cucm-b-test-admin-78f11b08d2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/14SU2/adminGd/cucm_b_administration-guide-14su2/cucm_b_test-adminguide_chapter_01001.html
retrieved_at: 2026-08-17T00:41:14.965984+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: April 8, 2025

Chapter: View Usage Records

## Chapter: View Usage Records

# View Usage Records

## Usage Records Overview

Cisco Unified Communications Manager provides records that allow you to see how configured items are used in your system. Configured items include devices, as
                              well as system-level settings such as device pools, date and time groups, and route plans.

### Dependency Records

Use
                                 		  dependency records for the following purposes:

Find
                                       				information about system-level settings, such as servers, device pools, and
                                       				date and time groups.

Determine the
                                       				records in the database that use other records. For example, you can determine
                                       				which devices, such as CTI route points or phones, use a particular calling
                                       				search space.

Show dependencies between records before you delete any records. For example, before you delete a partition, use dependency
                                       records to see which calling search spaces (CSSs) and devices are associated with it.  
                                       				You can then reconfigure the settings to remove the dependency.

### Route Plan Reports

The route plan report allows you to view either a partial or
                                 		  full list of numbers, routes, and patterns that are configured in the system. When you generate a report, you can access
                                 the configuration window for each item by
                                 		  clicking the entry in the Pattern/Directory Number, Partition, or Route Detail
                                 		  columns of the report.

In addition, the route plan report allows you to save report
                                 		  data into a.CSV file that you can import into other applications. The.CSV
                                 		  file contains more detailed information than the web pages, including directory
                                 		  numbers for phones, route patterns, pattern usage, device name, and device
                                 		  description.

Cisco Unified Communications Manager uses the route
                                 		  plan to route both internal calls and external public switched telephone
                                 		  network (PSTN) calls. Because you might have several records in your network, Cisco Unified Communications Manager Administration lets you locate specific route plan records on the basis of specific criteria.

## Usage Report Tasks

Step 1

To view route plan records and use them to manage unassigned directory numbers, see the following procedures:

Use these procedures to locate specific route plan records, save the records in a .CSV file, and manage unassigned directory
                                          numbers.

Step 2

To use dependency records, see the following procedures:

- View Dependency Records

Use these procedures to find
                                          				information about system-level settings and show dependencies between records in the database.

### Route Plan Reports
                           	 Task Flow

Step 1

View Route Plan Records .

View route plan records and generate customized route plan
                                             				reports.

Step 2

Save Route Plan Reports .

View route plan reports in a.csv file format.

Step 3

Delete Unassigned Directory Numbers .

Delete an unassigned directory number from the route plan report.

Step 4

Update Unassigned Directory Numbers .

Update the settings of an unassigned directory number from the
                                             				route plan report.

#### View Route Plan
                              	 Records

This
                                    		  section describes how to view route plan records. Because you might have
                                    		  several records in your network, Cisco Unified Communications
                                       			 Manager Administration lets you locate specific route plan records on
                                    		  the basis of specific criteria. Use the following procedure to generate
                                    		  customized route plan reports.

Step 1

Choose Call
                                                   				  Routing > Route Plan Report .

Step 2

To find all
                                             			 records in the database, ensure the dialog box is empty and proceed to step 3.

To filter or
                                                				search records

From the
                                                   				  first drop-down list box, select a search parameter.

From the
                                                   				  second drop-down list box, select a search pattern.

Specify the
                                                   				  appropriate search text, if applicable.

Step 3

Click Find .

All or matching
                                                				records display. You can change the number of items that display on each page
                                                				by choosing a different value from the Rows per Page drop-down list box.

Step 4

From the list of
                                             			 records that display, click the link for the record that you want to view.

The window
                                                				displays the item that you choose.

#### Save Route Plan
                              	 Reports

This
                                    		  section contains information on how to view route plan reports in a.csv file.

Step 1

Choose Call
                                                   				  Routing > Route Plan Report .

Step 2

Choose View In
                                                				File from the Related
                                                				Links drop-down list on the Route
                                                				Plan Report window and click Go .

From the dialog
                                                				box that appears, you can either save the file or import it into another
                                                				application.

Step 3

Click Save .

Another window
                                                				displays that allows you to save this file to a location of your choice.

You may also
                                                            				  save the file as a different file name, but the file name must include a.CSV
                                                            				  extension.

Step 4

Choose the
                                             			 location in which to save the file and click Save . This action should save the file to the
                                             			 location that you designated.

Step 5

Locate the.CSV
                                             			 file that you just saved and double-click its icon to view it.

#### Delete Unassigned
                              	 Directory Numbers

This
                                    		  section describes how to delete an unassigned directory number from the route
                                    		  plan report. Directory numbers get configured and removed in the Directory
                                    		  Number Configuration window of Cisco Unified Communications
                                       			 Manager Administration . When a directory number gets removed from a
                                    		  device or a phone gets deleted, the directory number still exists in the Cisco Unified Communications
                                       			 Manager database. To delete the directory number from the database,
                                    		  use the Route Plan Report window.

Step 1

Choose Call Call
                                                   				  Routing > Route Plan Report .

Step 2

In the Route
                                             			 Plan Report window, use the three drop-down lists to specify a route plan
                                             			 report that lists all unassigned DNs.

Step 3

Three ways exist
                                             			 to delete directory numbers:

Click the
                                                   				  directory number that you want to delete. When the Directory Number
                                                   				  Configuration window displays, click Delete.

Check the
                                                   				  check box next to the directory number that you want to delete. Click Delete
                                                   				  Selected.

To delete
                                                   				  all found unassigned directory numbers, click Delete All Found Items.

A warning
                                                      					 message verifies that you want to delete the directory number.

Step 4

To delete the
                                             			 directory number, click OK. To cancel the delete request, click Cancel.

#### Update Unassigned
                              	 Directory Numbers

This
                                    		  section describes how to update the settings of an unassigned directory number
                                    		  from the route plan report. Directory numbers get configured and removed in the
                                    		  Directory Number Configuration window of Cisco Unified Communications
                                       			 Manager Administration . When a directory number gets removed from a
                                    		  device, the directory number still exists in the Cisco Unified Communications
                                       			 Manager database. To update the settings of the directory number, use
                                    		  the Route Plan Report window.

Step 1

Choose Call
                                                   				  Routing > Route Plan Report .

Step 2

In the Route
                                                				Plan Report window, use the three drop-down lists to specify a
                                             			 route plan report that lists all unassigned DNs.

Step 3

Click the
                                             			 directory number that you want to update.

You can update
                                                            				  all the settings of the directory number except the directory number and
                                                            				  partition.

Step 4

Make the
                                             			 required updates such as calling search space or forwarding options.

Step 5

Click Save .

The Directory
                                                				Number Configuration window redisplays, and the directory number field is
                                                				blank.

### Dependency Records
                           	 Task Flow

Step 1

Configure Dependency Records .

Use this
                                             				procedure to enable or disable dependency records. This procedure runs at
                                             				below-normal priority and may take time to complete due to dial plan size and
                                             				complexity, CPU speed, and CPU requirements of other applications.

Step 2

View Dependency Records .

After
                                             				you enable dependency records, you can access them from the configuration
                                             				windows on the interface.

#### Configure Dependency Records

Use dependency records to view relationships between records in the Cisco Unified Communications Manager database. For example, before you delete a partition, use dependency records to see which calling search spaces (CSSs) and
                                    devices are associated with it.

Caution

Dependency records  cause high CPU usage. This procedure runs at below-normal priority and may take time to complete due to
                                                dial plan size and complexity, CPU speed, and CPU requirements of other applications.

If you have dependency records enabled and your system is experiencing CPU usage issues, you can disable dependency records.

Step 1

From Cisco Unified CM Administration , choose System > Enterprise Parameters .

Step 2

Scroll to the CCMAdmin Parameters section and from the Enable Dependency Records drop-down list, choose one of the following options:

- True —Enable dependency records.

- False —Disable dependency records.

Step 3

Click OK .

Step 4

Click Save .

#### View Dependency
                              	 Records

After you enable dependency records, you can access them from the configuration windows on the interface.

##### Before you begin

Configure Dependency Records

Step 1

From Cisco
                                                				Unified CM Administration , navigate to the configuration window for
                                             			 the records that you want to view.

##### Example:

You cannot view dependency records from the Device Defaults and Enterprise Parameters Configuration windows.

Step 2

Click Find .

Step 3

Click one of
                                             			 the records.

Step 4

From
                                             			 the Related
                                                				Links list box, choose Dependency Records box, and click Go .

If you have
                                                            				  not enabled the dependency records, the Dependency Records Summary window displays a message,
                                                            				  not the information about the record.

Step 5

Select one of
                                             			 the following dependency record buttons in this window:

Refresh —Update
                                                   				  the window with current information.

Close —Close the
                                                   				  window without returning to the configuration window in which you clicked the
                                                   				  Dependency Records link.

Close and Go
                                                      					 Back —Close the window and returns to the configuration window in
                                                   				  which you clicked the Dependency Records link.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | To view route plan records and use them to manage unassigned directory numbers, see the following procedures: | Use these procedures to locate specific route plan records, save the records in a .CSV file, and manage unassigned directory
                                          numbers. |
| Step 2 | To use dependency records, see the following procedures: View Dependency Records | Use these procedures to find
                                          				information about system-level settings and show dependencies between records in the database. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | View Route Plan Records . | View route plan records and generate customized route plan
                                             				reports. |
| Step 2 | Save Route Plan Reports . | View route plan reports in a.csv file format. |
| Step 3 | Delete Unassigned Directory Numbers . | Delete an unassigned directory number from the route plan report. |
| Step 4 | Update Unassigned Directory Numbers . | Update the settings of an unassigned directory number from the
                                             				route plan report. |

| Step 1 | Choose Call
                                                   				  Routing > Route Plan Report . |
|---|---|
| Step 2 | To find all
                                             			 records in the database, ensure the dialog box is empty and proceed to step 3. To filter or
                                                				search records From the
                                                   				  first drop-down list box, select a search parameter. From the
                                                   				  second drop-down list box, select a search pattern. Specify the
                                                   				  appropriate search text, if applicable. |
| Step 3 | Click Find . All or matching
                                                				records display. You can change the number of items that display on each page
                                                				by choosing a different value from the Rows per Page drop-down list box. |
| Step 4 | From the list of
                                             			 records that display, click the link for the record that you want to view. The window
                                                				displays the item that you choose. |

| Step 1 | Choose Call
                                                   				  Routing > Route Plan Report . |
|---|---|
| Step 2 | Choose View In
                                                				File from the Related
                                                				Links drop-down list on the Route
                                                				Plan Report window and click Go . From the dialog
                                                				box that appears, you can either save the file or import it into another
                                                				application. |
| Step 3 | Click Save . Another window
                                                				displays that allows you to save this file to a location of your choice. Note You may also
                                                            				  save the file as a different file name, but the file name must include a.CSV
                                                            				  extension. | Note | You may also
                                                            				  save the file as a different file name, but the file name must include a.CSV
                                                            				  extension. |
| Note | You may also
                                                            				  save the file as a different file name, but the file name must include a.CSV
                                                            				  extension. |
| Step 4 | Choose the
                                             			 location in which to save the file and click Save . This action should save the file to the
                                             			 location that you designated. |
| Step 5 | Locate the.CSV
                                             			 file that you just saved and double-click its icon to view it. |

| Note | You may also
                                                            				  save the file as a different file name, but the file name must include a.CSV
                                                            				  extension. |
|---|---|

| Step 1 | Choose Call Call
                                                   				  Routing > Route Plan Report . |
|---|---|
| Step 2 | In the Route
                                             			 Plan Report window, use the three drop-down lists to specify a route plan
                                             			 report that lists all unassigned DNs. |
| Step 3 | Three ways exist
                                             			 to delete directory numbers: Click the
                                                   				  directory number that you want to delete. When the Directory Number
                                                   				  Configuration window displays, click Delete. Check the
                                                   				  check box next to the directory number that you want to delete. Click Delete
                                                   				  Selected. To delete
                                                   				  all found unassigned directory numbers, click Delete All Found Items. A warning
                                                      					 message verifies that you want to delete the directory number. |
| Step 4 | To delete the
                                             			 directory number, click OK. To cancel the delete request, click Cancel. |

| Step 1 | Choose Call
                                                   				  Routing > Route Plan Report . |
|---|---|
| Step 2 | In the Route
                                                				Plan Report window, use the three drop-down lists to specify a
                                             			 route plan report that lists all unassigned DNs. |
| Step 3 | Click the
                                             			 directory number that you want to update. Note You can update
                                                            				  all the settings of the directory number except the directory number and
                                                            				  partition. | Note | You can update
                                                            				  all the settings of the directory number except the directory number and
                                                            				  partition. |
| Note | You can update
                                                            				  all the settings of the directory number except the directory number and
                                                            				  partition. |
| Step 4 | Make the
                                             			 required updates such as calling search space or forwarding options. |
| Step 5 | Click Save . The Directory
                                                				Number Configuration window redisplays, and the directory number field is
                                                				blank. |

| Note | You can update
                                                            				  all the settings of the directory number except the directory number and
                                                            				  partition. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Dependency Records . | Use this
                                             				procedure to enable or disable dependency records. This procedure runs at
                                             				below-normal priority and may take time to complete due to dial plan size and
                                             				complexity, CPU speed, and CPU requirements of other applications. |
| Step 2 | View Dependency Records . | After
                                             				you enable dependency records, you can access them from the configuration
                                             				windows on the interface. |

| Caution | Dependency records  cause high CPU usage. This procedure runs at below-normal priority and may take time to complete due to
                                                dial plan size and complexity, CPU speed, and CPU requirements of other applications. |
|---|---|

| Step 1 | From Cisco Unified CM Administration , choose System > Enterprise Parameters . |
|---|---|
| Step 2 | Scroll to the CCMAdmin Parameters section and from the Enable Dependency Records drop-down list, choose one of the following options: True —Enable dependency records. False —Disable dependency records. Based on the option you choose, a dialog box appears with a message about the consequences of enabling or disabling the dependency
                                             records. Read the message before you click OK in this dialog box. |
| Step 3 | Click OK . |
| Step 4 | Click Save . The Update Successful message appears confirming the change. |

| Step 1 | From Cisco
                                                				Unified CM Administration , navigate to the configuration window for
                                             			 the records that you want to view. Example: To view
                                             			 dependency records for a device pool, select System > Device
                                                   				  Pool . Note You cannot view dependency records from the Device Defaults and Enterprise Parameters Configuration windows. | Note | You cannot view dependency records from the Device Defaults and Enterprise Parameters Configuration windows. |
|---|---|---|---|
| Note | You cannot view dependency records from the Device Defaults and Enterprise Parameters Configuration windows. |
| Step 2 | Click Find . |
| Step 3 | Click one of
                                             			 the records. The
                                             			 configuration window appears. |
| Step 4 | From
                                             			 the Related
                                                				Links list box, choose Dependency Records box, and click Go . Note If you have
                                                            				  not enabled the dependency records, the Dependency Records Summary window displays a message,
                                                            				  not the information about the record. The Dependency Records Summary window appears showing the
                                             			 records that are used by other records in the database. | Note | If you have
                                                            				  not enabled the dependency records, the Dependency Records Summary window displays a message,
                                                            				  not the information about the record. |
| Note | If you have
                                                            				  not enabled the dependency records, the Dependency Records Summary window displays a message,
                                                            				  not the information about the record. |
| Step 5 | Select one of
                                             			 the following dependency record buttons in this window: Refresh —Update
                                                   				  the window with current information. Close —Close the
                                                   				  window without returning to the configuration window in which you clicked the
                                                   				  Dependency Records link. Close and Go
                                                      					 Back —Close the window and returns to the configuration window in
                                                   				  which you clicked the Dependency Records link. |

| Note | You cannot view dependency records from the Device Defaults and Enterprise Parameters Configuration windows. |
|---|---|

| Note | If you have
                                                            				  not enabled the dependency records, the Dependency Records Summary window displays a message,
                                                            				  not the information about the record. |
|---|---|