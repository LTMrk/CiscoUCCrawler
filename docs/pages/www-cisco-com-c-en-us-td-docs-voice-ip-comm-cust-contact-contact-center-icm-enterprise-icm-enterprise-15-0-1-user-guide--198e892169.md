---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-user-guide--198e892169
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/user/guide/ucce_b_scripting-and-media-routing-guide-for-cisco-unified-icm-contact-center-enterprise-release-15_0/script_administration.html
retrieved_at: 2026-08-16T20:38:49.852743+00:00
---

Scripting and Media Routing Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# Scripting and Media Routing Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: April 30, 2025

Chapter: Script Administration

## Chapter: Script Administration

# Script Administration

## Check Script Routes

After you save a script, you should check that all routes referenced
                              have valid labels for the routing clients and dialed numbers for which
                              you have scheduled the script.

For the Unified CCE to route calls through a script, you must have defined a routing label for each route referenced in the script. Each label
                              is valid only for specific routing clients and, optionally, for specific dialed numbers.

To check script routes:

Step 1

Start Check Routes from the Administration & Data Server group.
                                       The Check Routes window opens.

Step 2

Using the drop-down lists, choose the following:

Name of the routing client to send calls through the
                                                script.

Dialed number for the call to be sent through the script.

The routing script name.

The version number of the routing script. (The default is
                                                the active version.)

Step 3

To validate the route of a network transfer call target, check Use
                                       Network Transfer specify a routing client and a Dialed Number.

Step 4

Use the drop-down list to select Routes Used Directly by Script (the
                                       default) or Translation Route Used in Script. The routes referenced in
                                       the script appear in the left column. (If any of these routes do not
                                       have an associated label that is valid for the routing client and Dialed
                                       Number you have chosen, an error message appears in the Errors
                                       field.)

Step 5

To see the specific peripheral targets associated with a route,
                                       select the route name in the left column. The associated peripheral
                                       targets appear in the center column.

The routes referenced in the script appear in the left column. If
                                          any of these routes does not have an associated label that is valid
                                          for the routing client and Dialed Number you have chosen, an error
                                          message appears in the Errors field at the bottom of the
                                          window.

Step 6

To see the specific labels associated with any of these peripheral
                                       targets, select the peripheral target. The associated peripheral targets
                                       appear in the right column.

Symbols might appear next to a
                                          label, explaining the following:

The label is not valid for the specified routing
                                                client.

The label is not valid for the specified Dialed
                                                Number.

Step 7

To check configuration information for a route or peripheral target,
                                       double-click a route or peripheral target name. Check Routes to display
                                       the configuration information for that route or peripheral
                                       target.

Step 8

To correct any problems you find through Check Routes, make and save changes within the Script Editor or the Unified CCE Configuration Manager.

Step 9

To update the changes, click Reload in the Check
                                       Routes window. (If you have created a new version of the script, be sure
                                       to update the Version field.) Check Routes reads the latest version of
                                       scripts and configuration data from the local database.

## Active Scripts

Although the Script Editor may contain several versions of a script, only one version of a particular script can be active
                              at one time: This is the version that Unified CCE runs if the script is currently scheduled.

You can use one of three methods to set the active version of
                              a script:

Preferences

Make Active Version command

Script Explorer

## Use Preferences to Set an Active Script

Step 1

Within Script Editor, select Options > Preferences . The Script Editor Preferences dialog
                                       box opens.

Step 2

Optionally, select the Automatically Make a Script Active
                                          When Saved option.

When you select this option, whenever you save a valid script, the Unified CCE makes that new version the active version.

When you clear this check box, you must manually activate
                                                the script after saving it.

## Use Script  Make Active Version Command

In an open script in edit mode, select Script > Make Active Version or click Make Active
                                          Version . The system makes the open script version the
                                       current active version.

## View Enabled Scripts

After you save and schedule a script, it is considered enabled.
                              Use the Enabled Scripts dialog box to examine all scripts currently
                              enabled in the system.

To view all enabled routing and administrative scripts:

Step 1

Within Script Editor, choose Scripts > Enabled Scripts . The Enabled Scripts dialog box
                                       opens listing all routing scripts that are scheduled for the current
                                       date and time.

The dialog box lists all call types and the script that is
                                          currently scheduled for each. The Call Count column lists the number
                                          of calls the script has processed.

Step 2

Optionally, use the Display Count From section of the dialog box to
                                       choose how to display the number of calls processed. Whichever option
                                       you choose, the counts are updated every 15 seconds. This allows you to
                                       see which scripts are currently handling calls.

Step 3

To see all administrative scripts scheduled for the current date and
                                       time, click the Administrative Scripts tab. This lists
                                       all administrative scripts.

## Schedule Administrative Script

To schedule an administrative script:

Step 1

Within Script Editor, choose Script > Administrative Manager . The Administrative Manager
                                       dialog box opens, listing any administrative scripts that are currently
                                       scheduled.

Step 2

Click Add . The Add Administrative Schedule dialog
                                       box appears, opening at the Script tab.

Step 3

Select the script you want to schedule and click the Period tab.

Step 4

Specify when you want the script to be active:

In the Date Range, Recurrence Pattern, and Duration
                                             sections, specify the range of times when this script may run.

In the Frequency section, specify how often the script
                                             should run during the specified time range.

Step 5

Optionally, click the Description tab and add a
                                       descriptive text about this schedule.

Step 6

Click OK to submit the
                                       schedule and return to the Administration Manager.

Step 7

Click OK to save your changes to the Unified CCE database and close the Administrative Manager.

The first execution occurs at the start time of the schedule.

The last execution occurs before or at the end time of the schedule.

The timing of script execution might not be exact. Typically, scripts run within a few seconds after the scheduled time. The
                                                            last script execution might occur slightly after the scheduled end time.

## Script Monitoring

After you save a routing or administrative script, you can observe how it
                              runs. Watching routing requests moving through a script in real-time helps
                              ensure that the routing script is operating as expected.

When you monitor a script, that is, view the script in Monitor mode,
                              labels appear on each connection in the script.

A script can have a maximum of 900 script meters. If a script exceeds that limit some of the real-time monitors stop working.
                                          In this case, you see periodic messages in the Router log and Event report that the script exceeds the monitor limit. If you
                                          edit a script that is over the limit, a warning displays when you attempt to save the script. For more details about monitor
                                          labels, see the List of Monitor Labels .

### Monitor Labels

Most monitor labels display the raw number and percentage of route
                                 requests that have passed through the connection since the start of the
                                 monitoring period.

Each target set also lists the number and percentage of calls routed
                                 to each of the targets in that set. Each statistic is updated
                                 automatically as new real-time data become available about every 15
                                 seconds.

When you edit a script, position nodes so that there is enough space
                                 for the monitor labels to display. (Because you cannot make any changes
                                 to a script while in Monitor mode, you cannot rearrange the nodes at
                                 that time, unless you have enabled Quick Edit from Monitor mode as
                                 described in the following section). Use the Script > Display Monitor
                                    Labels command while in edit mode to display blank monitor
                                 labels on each connection of the script.

### Enable Quick Edit from Monitor Mode

Step 1

From the Options menu, choose Preferences .

Step 2

Check Allow quick edit from monitor mode .

Step 3

Click OK .

#### What to do next

You can now perform quick edits when monitoring a script.

### List of Monitor Labels

The Script Editor displays counters in monitor labels to indicate which paths or targets the voice calls or digital channel
                                 tasks are routed to. Each of these counts consumes a script meter. The following table describes how many meters are consumed
                                 per node in your script.

The total number of script meters in a script cannot exceed 900 monitored objects. If your script exceeds this limit, a warning
                                 message appears when you modify and save the script. The Script Editor displays only up to 900 script meters; any additional
                                 meters are not updated. Ensure your scripts are modular and contain fewer nodes to maintain the count limit.

Name of the node

Meters allocated

1, if requery is enabled.

Otherwise 0

The monitor labels can display two or more of the following meters:

InQueue meter - Displays the number of calls in the queue.

InProgress meter - Displays the number of calls in progress in the node.

Abort meter - Displays the number of calls aborted.

Routed meter - Displays the number of calls that are routed to the Precision Queue.

The Terminal nodes that end script processing and do not contribute to any monitoring meters are listed below:

Requalify

ReleaseCall

Termination

Ring

Busy

Announcement

End

Goto

The InProgress meter appears in the top row of all the monitor labels for all the listed nodes, except the Queue and Precision
                                 Queue nodes. The top row of the Queue node monitor label displays the InQueue meter and the top row of the Precision Queue
                                 monitor label displays the Routed meter.

The following meters are applicable only for Queue to Skill Group and Precision Queue node:

Picked by another Skill Group/Precision Queue meter - Displays the number of nonvoice task requests that are picked from a
                                       Skill Groups/Precision Queue other than the targets specified in the node.

Pulled by another Skill Group/Precision Queue meter - Displays the number of nonvoice task requests that are pulled from a
                                       Skill Groups/Precision Queue other than the targets specified in the node.

The following meters are applicable only for the Pick/Pull node.

Pick meter - Displays the number of nonvoice task pick requests that were successful.

Pull meter - Displays the number of nonvoice task pull requests that were successful.

Pick error meter - Displays the number of nonvoice task pick requests that failed.

Pull error meter - Displays the number of nonvoice task pull requests that failed.

Since Picked by another Skill Group/Precision Queue and Pulled by another Skill Group/Precision Queue meters are specific to nonvoice task routing, these are not populated in case of voice call routing.

### Adjust Monitor Label Location

Step 1

In the Properties dialog box of a node within Script Editor,
                                          click the Labels tab.

Step 2

Specify the following:

Label position (Slider): Choose if you want the
                                                connection labels to appear close to the node
                                                (Origin), close to the targeted node (Destination), or
                                                half way in-between (Center).

Display monitor labels (check box): If you select this check box, then when the Script Editor is in Monitor mode,
                                                labels display for each connection from the node. If you clear the
                                                check box, no labels display for connections
                                                from the node.

Step 3

Click OK to apply changes and to close the Select Properties dialog box.

### Access Monitor Mode

Choose File > Open to
                                       access the Open dialog box and choose the Monitor option from
                                       the Open Mode drop-down list.

Within an open script in the Script Editor workspace, choose Script > Monitor Script or click Monitor Script in the toolbar.

Within the Enabled Scripts dialog box, choose the Monitor radio button in the Open Script in
                                       Mode section and click Open .

#### What to do next

The script displays in Monitor mode in the Script Editor workspace.

### Set Monitor Mode Options

Step 1

In Script Editor, do one of the following:

Choose Script > Monitor Options .

Click Monitor on the status bar. A drop-down list appears.

Step 2

Choose one of the following options:

Start of Day. Initial monitor values are totals since
                                                   midnight. New values are added to these totals every 15
                                                   seconds.

Starting Now. Initial monitor values are all zeros.
                                                   New values are added to these totals every 15 seconds.

For Each Interval. Initial monitor values are the
                                                   values reported for the most recent 15-second interval.
                                                   New values are added to these numbers every 15 seconds.

Percentages for Each Node. The percentages for each
                                                   connection from a node are calculated by dividing the
                                                   number of executions that passed though the connection
                                                   by the number of executions that entered the node. All
                                                   connections coming from each node add up to 100%.

Percentages for Entire Script. The percentages for
                                                   each connection are calculated by dividing the number of
                                                   executions that passed through that connection by the
                                                   total number of executions handled by the script.

### View Real-Time Data

For more information about the real-time data, see the descriptions of the Service Real Time and Skill Group Real Time tables
                                 in the Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

Step 1

While in Monitor mode in Script Editor, choose Script
                                             > Display Real-Time Data .

The Real-Time Data
                                             window appears. By default, the Real-Time Data window displays data about the
                                             Services referenced in the current script. (Scroll to the right
                                             to see additional columns.) The values in the screen are updated
                                             continuously as new real-time data arrives at the Administration
                                             & Data Server.

When an External Authorization server is used with Internet Script Editor, you can only select from the list of available
                                                         Call Types or Precision Queues as identified by the Authorization server.

Step 2

To display information about skill groups or scheduled
                                          targets, rather than services, change the value in the field in
                                          the upper-left corner of the Real-Time Data window. The window
                                          contents automatically change to show skill group data.

Step 3

When finished, click Close .

#### View Dynamic Real-Time Data

You can view dynamic call types, dynamic precision queues, or dynamic skill groups.

Step 1

While in Monitor Mode in Script Editor, open an active script and choose Script > Display Real-Time Data .

Step 2

To display dynamic call types, dynamic precision queues, or dynamic skill groups from the drop-down list, choose Call Type , Precision Queue , or Skill Group in the upper-left corner.

Step 3

Click Add Dynamic .

Step 4

In the Available dynamic objects list, select the objects to monitor and then click Add .

Step 5

Click OK .

### Change Real-Time Data Configuration

Step 1

Click Configure in the real-time data window
                                          or choose Script > Configure Real-Time Data .
                                          The Configure real-time data dialog box opens.Use this dialog box to add new columns, remove existing
                                          columns, reorder the columns, or change the column labels.

Step 2

Choose a Routing target type (Service, Scheduled
                                          Target, or Skill groups). This updates the other fields:

The Real-Time Columns list contains all the real-time
                                                   columns available in the database for the target type.

The Routing Target Columns list contains the columns
                                                   to appear in the Real-Time Data window.

If you select a column in the Routing Target Columns
                                                   list, the heading for that column appears in the Column
                                                   Header field.

Step 3

Use the Add and Remove buttons to move columns between the
                                          lists. Use the Move buttons to change the order of the selected
                                          columns. (To change back to the default column order, click Default Columns .)

Step 4

Optionally, to edit a Routing Target Columns heading, make
                                          changes within the Column Header field. (To change back to the
                                          default header, highlight the Routing Target Column name and
                                          click the Default Header button.)

Step 5

Optionally, select the Short Headers / Long Headers radio buttons to change
                                          between the full and abbreviated forms of the default column
                                          headers. The abbreviated forms are typically three to four
                                          letters. (For example, AHT is used for Average Handle Time.)

Step 6

To save the changes, click OK . The settings
                                          apply to the current and future Script Editor sessions.

## View Router Logs

You can view CallRouter log messages to determine how contacts are routed and to see any errors the Unified CCE encounters in processing routing requests.

You start the Router Log Viewer from the Administration & Data Server
                           group. The Router Log Viewer window opens.

The top field of the Router Log Viewer window displays information about each call the Unified CCE routes, including:

The time that routing request was received

The Dialed Number (DN), or script selector, and the caller's
                                 billing telephone number (ANI)

Any Caller-Entered Digits (CED)

The label that Unified CCE returned to the routing client

The bottom field of the window displays any errors that the Unified CCE encounters in routing calls, including:

The time the error occurred

Text describing the error

## Export a
                        	 Script

Step 1

Choose File > Export
                                          				Script . The Export Script dialog box opens with the name of the current
                                       			 script and version number in the File name field.

Step 2

Optionally,
                                       			 change the file name. You cannot change the file type; you can only save the
                                       			 script in .ICMS format.

Step 3

Click Save . If the
                                       			 file name already exists, the system prompts you to confirm the save.

Step 4

If prompted,
                                       			 click OK .

## Import a
                        	 Script

Step 1

Choose File > Import
                                          				Script . The Select Script to Import dialog box opens.

Step 2

Choose a file
                                       			 name with an Unified ICM Script extension (.ICMS) and click Open . The
                                       			 Script Editor performs automapping and the following happens:

If all
                                                					 imported objects were successfully auto-mapped, a message window appears
                                                					 prompting you to review the mappings. Click OK to
                                                					 access the Object Mapping dialog box.

If some
                                                					 imported objects were not successfully auto-mapped, the partially mapped script
                                                					 is opened as a new script in Import mode and the Object Mapping dialog box
                                                					 appears, with all unmapped objects labeled

- -
                                                   						Unmapped - - . The Object Mapping dialog box contains three columns:

Object
                                                      						  Types. The type of the imported object.

Imported
                                                      						  Object. The name of the imported object.

Mapped
                                                      						  To. What this imported object will be mapped to.

Step 3

Click an
                                       			 Imported Object value. The Mapped To column's drop-down list shows all the
                                       			 valid objects on the target system. (The Script Editor window also highlights
                                       			 the script nodes that refer to this object.)

Step 4

Optionally,
                                       			 choose an object from the Mapped To drop-down list on the target system that
                                       			 you want to map the imported object to.

Choose an
                                                      				  object from the Mapped To drop-down list on the target system that you want to
                                                      				  map the imported object to.

Step 5

When the mapping
                                       			 is complete, click Apply and
                                       			 Finish.

## Modify Script Version and Schedule System Information

Step 1

Within the Unified CCE Configuration Manager, choose Tools > Miscellaneous Tools > System Information . The System Information window opens.

Step 2

Enter the Minimum Script Schedule Time.

Step 3

Set the number of script versions to be retained in the Retain
                                       Script Versions field.

Step 4

Click Save to apply your changes.

## Script Editor and Internet Script Editor

In a Unified CCE deployment, two tools are available for creating routing and administration scripts—Script Editor and Internet
                           Script Editor. You can use either or both of these two tools. They provide the same functionality, and that functionality
                           is documented in this section. This table lists some considerations:

Script Editor

Internet Script Editor

Is automatically deployed as part of the Unified CCE AW-HDS or AW-HDS-DDS installation.

Must be enabled during the installation of the Unified CCE AW-HDS or AW-HDS-DDS Server by selecting it in Web Setup, then
                                       downloaded and installed.

Requires a full Administration and Data server. You must run it from the Unified CCE AW-HDS or AW-HDS-DDS Server, based on
                                       your deployment.

Can be run on a local machine.

Can be used by global administrators.

Can be used by global administrators and departmental administrators.

Imposes no scripting access restrictions for global administrators.

Imposes scripting access restrictions for departmental administrators.

## Administrator Privileges in Internet Script Editor

In a Unified CCE deployment, global administrators and departmental administrators have different access permissions in Internet
                           Script Editor.

Global administrators have access as follows:

Full access to scripts and can reference all global and all departments objects when they create scripts.

Full access to dynamic scripting nodes.

Departmental administrators have access as follows:

Full access to scripts that reference global objects and objects in their departments.

Read-only access to scripts that reference Dynamic Scripting Nodes such as formulas.

No access to scripts that reference objects that are associated with departments they do not administer.

| Note | You must have saved the script to the Unified CCE database before you can check the routes. |
|---|---|

| Step 1 | Start Check Routes from the Administration & Data Server group.
                                       The Check Routes window opens. |
|---|---|
| Step 2 | Using the drop-down lists, choose the following: Name of the routing client to send calls through the
                                                script. Dialed number for the call to be sent through the script. The routing script name. The version number of the routing script. (The default is
                                                the active version.) |
| Step 3 | To validate the route of a network transfer call target, check Use
                                       Network Transfer specify a routing client and a Dialed Number. |
| Step 4 | Use the drop-down list to select Routes Used Directly by Script (the
                                       default) or Translation Route Used in Script. The routes referenced in
                                       the script appear in the left column. (If any of these routes do not
                                       have an associated label that is valid for the routing client and Dialed
                                       Number you have chosen, an error message appears in the Errors
                                       field.) Note To see the configuration details for a translation route, select
                                                   the route name and click View Translation Route .
                                                   (This button becomes enabled after you choose a specific translation
                                                   route.) The Translation Route dialog box opens. | Note | To see the configuration details for a translation route, select
                                                   the route name and click View Translation Route .
                                                   (This button becomes enabled after you choose a specific translation
                                                   route.) The Translation Route dialog box opens. |
| Note | To see the configuration details for a translation route, select
                                                   the route name and click View Translation Route .
                                                   (This button becomes enabled after you choose a specific translation
                                                   route.) The Translation Route dialog box opens. |
| Step 5 | To see the specific peripheral targets associated with a route,
                                       select the route name in the left column. The associated peripheral
                                       targets appear in the center column. The routes referenced in the script appear in the left column. If
                                          any of these routes does not have an associated label that is valid
                                          for the routing client and Dialed Number you have chosen, an error
                                          message appears in the Errors field at the bottom of the
                                          window. |
| Step 6 | To see the specific labels associated with any of these peripheral
                                       targets, select the peripheral target. The associated peripheral targets
                                       appear in the right column. Symbols might appear next to a
                                          label, explaining the following: The label is not valid for the specified routing
                                                client. The label is not valid for the specified Dialed
                                                Number. |
| Step 7 | To check configuration information for a route or peripheral target,
                                       double-click a route or peripheral target name. Check Routes to display
                                       the configuration information for that route or peripheral
                                       target. Note From the Peripheral Target dialog box, you can access information
                                                   about the route by clicking the Route button. | Note | From the Peripheral Target dialog box, you can access information
                                                   about the route by clicking the Route button. |
| Note | From the Peripheral Target dialog box, you can access information
                                                   about the route by clicking the Route button. |
| Step 8 | To correct any problems you find through Check Routes, make and save changes within the Script Editor or the Unified CCE Configuration Manager. |
| Step 9 | To update the changes, click Reload in the Check
                                       Routes window. (If you have created a new version of the script, be sure
                                       to update the Version field.) Check Routes reads the latest version of
                                       scripts and configuration data from the local database. |

| Note | To see the configuration details for a translation route, select
                                                   the route name and click View Translation Route .
                                                   (This button becomes enabled after you choose a specific translation
                                                   route.) The Translation Route dialog box opens. |
|---|---|

| Note | From the Peripheral Target dialog box, you can access information
                                                   about the route by clicking the Route button. |
|---|---|

| Step 1 | Within Script Editor, select Options > Preferences . The Script Editor Preferences dialog
                                       box opens. |
|---|---|
| Step 2 | Optionally, select the Automatically Make a Script Active
                                          When Saved option. When you select this option, whenever you save a valid script, the Unified CCE makes that new version the active version. When you clear this check box, you must manually activate
                                                the script after saving it. |

| In an open script in edit mode, select Script > Make Active Version or click Make Active
                                          Version . The system makes the open script version the
                                       current active version. |
|---|

| Step 1 | Within Script Editor, choose Scripts > Enabled Scripts . The Enabled Scripts dialog box
                                       opens listing all routing scripts that are scheduled for the current
                                       date and time. The dialog box lists all call types and the script that is
                                          currently scheduled for each. The Call Count column lists the number
                                          of calls the script has processed. |
|---|---|
| Step 2 | Optionally, use the Display Count From section of the dialog box to
                                       choose how to display the number of calls processed. Whichever option
                                       you choose, the counts are updated every 15 seconds. This allows you to
                                       see which scripts are currently handling calls. Note The Call Count values are associated with scripts, not necessarily
                                                   with call types. If the script has been scheduled for more than one
                                                   call type, the Call Count value includes all calls processed by the
                                                   script regardless of call type. | Note | The Call Count values are associated with scripts, not necessarily
                                                   with call types. If the script has been scheduled for more than one
                                                   call type, the Call Count value includes all calls processed by the
                                                   script regardless of call type. |
| Note | The Call Count values are associated with scripts, not necessarily
                                                   with call types. If the script has been scheduled for more than one
                                                   call type, the Call Count value includes all calls processed by the
                                                   script regardless of call type. |
| Step 3 | To see all administrative scripts scheduled for the current date and
                                       time, click the Administrative Scripts tab. This lists
                                       all administrative scripts. |

| Note | The Call Count values are associated with scripts, not necessarily
                                                   with call types. If the script has been scheduled for more than one
                                                   call type, the Call Count value includes all calls processed by the
                                                   script regardless of call type. |
|---|---|

| Step 1 | Within Script Editor, choose Script > Administrative Manager . The Administrative Manager
                                       dialog box opens, listing any administrative scripts that are currently
                                       scheduled. |
|---|---|
| Step 2 | Click Add . The Add Administrative Schedule dialog
                                       box appears, opening at the Script tab. |
| Step 3 | Select the script you want to schedule and click the Period tab. |
| Step 4 | Specify when you want the script to be active: In the Date Range, Recurrence Pattern, and Duration
                                             sections, specify the range of times when this script may run. In the Frequency section, specify how often the script
                                             should run during the specified time range. |
| Step 5 | Optionally, click the Description tab and add a
                                       descriptive text about this schedule. |
| Step 6 | Click OK to submit the
                                       schedule and return to the Administration Manager. |
| Step 7 | Click OK to save your changes to the Unified CCE database and close the Administrative Manager. Note The first execution occurs at the start time of the schedule. The last execution occurs before or at the end time of the schedule. The timing of script execution might not be exact. Typically, scripts run within a few seconds after the scheduled time. The
                                                            last script execution might occur slightly after the scheduled end time. | Note | The first execution occurs at the start time of the schedule. The last execution occurs before or at the end time of the schedule. The timing of script execution might not be exact. Typically, scripts run within a few seconds after the scheduled time. The
                                                            last script execution might occur slightly after the scheduled end time. |
| Note | The first execution occurs at the start time of the schedule. The last execution occurs before or at the end time of the schedule. The timing of script execution might not be exact. Typically, scripts run within a few seconds after the scheduled time. The
                                                            last script execution might occur slightly after the scheduled end time. |

| Note | The first execution occurs at the start time of the schedule. The last execution occurs before or at the end time of the schedule. The timing of script execution might not be exact. Typically, scripts run within a few seconds after the scheduled time. The
                                                            last script execution might occur slightly after the scheduled end time. |
|---|---|

| Note | A script can have a maximum of 900 script meters. If a script exceeds that limit some of the real-time monitors stop working.
                                          In this case, you see periodic messages in the Router log and Event report that the script exceeds the monitor limit. If you
                                          edit a script that is over the limit, a warning displays when you attempt to save the script. For more details about monitor
                                          labels, see the List of Monitor Labels . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | From the Options menu, choose Preferences . |  |
| Step 2 | Check Allow quick edit from monitor mode . |  |
| Step 3 | Click OK . |  |

| Name of the node | Meters allocated |
|---|---|
| PercentAlloc* | Total number of connections |
| CallType | 1 |
| DatabaseLookup | 4 |
| Distribute | 2 |
| DistributeTime | Total number of connections |
| ECCPayload | 2 |
| If | 2 |
| Label | 1, if requery is enabled. Otherwise 0 |
| PickPull | 6 |
| CallerEnteredDigits (CED) | 1 + (Number of success path to other nodes) |
| CallerLineID(CLID) | 1 + (Number of success path to other nodes) |
| DialedNumber | 2 |
| ApplicationGateway | 4 |
| CancelQueuing | 1 |
| CollectData | 3 |
| DayOfWeek | Total number of labels configured |
| Line Connector | 1 |
| Media domain | Total number of connections |
| Menu | 2 + Number of success path to other nodes |
| Play | 3 |
| PrecisionQueue | 8 |
| QueueToAgent | 5 + Total number of targets |
| Queue | 7 + Total number of targets |
| RouteRequest | 4 |
| RunVRUScript | 4 |
| ScheduledSelect | 1 + Number of targets |
| AgentToAgent | 3 |
| QueuePriority | 1 |
| Switch | Total Number of connections |
| TranRouteToVRU | 5 + Total number of targets |
| TransferToVRU | 4 |
| VRUSettings | 2 |
| RouteSelect | 1 + Total number of targets |
| Select | 2 |
| Set | 1 |
| Start | 1 |
| Agent | Total number of targets |
| SkillGroup | Total number of targets |
| Service | Total number of targets |
| Enterprise Service | Total number of targets |
| Enterprise SkillGroup | Total number of targets |
| Wait | 3 |

| Note | Since Picked by another Skill Group/Precision Queue and Pulled by another Skill Group/Precision Queue meters are specific to nonvoice task routing, these are not populated in case of voice call routing. |
|---|---|

| Step 1 | In the Properties dialog box of a node within Script Editor,
                                          click the Labels tab. |
|---|---|
| Step 2 | Specify the following: Label position (Slider): Choose if you want the
                                                connection labels to appear close to the node
                                                (Origin), close to the targeted node (Destination), or
                                                half way in-between (Center). Display monitor labels (check box): If you select this check box, then when the Script Editor is in Monitor mode,
                                                labels display for each connection from the node. If you clear the
                                                check box, no labels display for connections
                                                from the node. |
| Step 3 | Click OK to apply changes and to close the Select Properties dialog box. |

| Step 1 | In Script Editor, do one of the following: Choose Script > Monitor Options . Click Monitor on the status bar. A drop-down list appears. |
|---|---|
| Step 2 | Choose one of the following options: Start of Day. Initial monitor values are totals since
                                                   midnight. New values are added to these totals every 15
                                                   seconds. Starting Now. Initial monitor values are all zeros.
                                                   New values are added to these totals every 15 seconds. For Each Interval. Initial monitor values are the
                                                   values reported for the most recent 15-second interval.
                                                   New values are added to these numbers every 15 seconds. Percentages for Each Node. The percentages for each
                                                   connection from a node are calculated by dividing the
                                                   number of executions that passed though the connection
                                                   by the number of executions that entered the node. All
                                                   connections coming from each node add up to 100%. Percentages for Entire Script. The percentages for
                                                   each connection are calculated by dividing the number of
                                                   executions that passed through that connection by the
                                                   total number of executions handled by the script. |

| Step 1 | While in Monitor mode in Script Editor, choose Script
                                             > Display Real-Time Data . The Real-Time Data
                                             window appears. By default, the Real-Time Data window displays data about the
                                             Services referenced in the current script. (Scroll to the right
                                             to see additional columns.) The values in the screen are updated
                                             continuously as new real-time data arrives at the Administration
                                             & Data Server. Note When an External Authorization server is used with Internet Script Editor, you can only select from the list of available
                                                         Call Types or Precision Queues as identified by the Authorization server. | Note | When an External Authorization server is used with Internet Script Editor, you can only select from the list of available
                                                         Call Types or Precision Queues as identified by the Authorization server. |
|---|---|---|---|
| Note | When an External Authorization server is used with Internet Script Editor, you can only select from the list of available
                                                         Call Types or Precision Queues as identified by the Authorization server. |
| Step 2 | To display information about skill groups or scheduled
                                          targets, rather than services, change the value in the field in
                                          the upper-left corner of the Real-Time Data window. The window
                                          contents automatically change to show skill group data. |
| Step 3 | When finished, click Close . |

| Note | When an External Authorization server is used with Internet Script Editor, you can only select from the list of available
                                                         Call Types or Precision Queues as identified by the Authorization server. |
|---|---|

| Step 1 | While in Monitor Mode in Script Editor, open an active script and choose Script > Display Real-Time Data . The Real-Time Data window appears. |
|---|---|
| Step 2 | To display dynamic call types, dynamic precision queues, or dynamic skill groups from the drop-down list, choose Call Type , Precision Queue , or Skill Group in the upper-left corner. |
| Step 3 | Click Add Dynamic . The Select Dynamic Call Type Objects , Select Dynamic Precision Queue Objects , or Select Dynamic Skill Group Objects dialog box appears, depending on your list choice. |
| Step 4 | In the Available dynamic objects list, select the objects to monitor and then click Add . You can monitor up to 20 dynamic call types, up to 20 dynamic precision queues, or up to 20 skill groups. You cannot monitor
                                             dynamic call types, dynamic precision queues, and dynamic skill groups in the same Real-Time Data window. |
| Step 5 | Click OK . The selected dynamic objects appear in the Real-Time Data window. Data for the selected objects appear when the data next refreshes. |

| Step 1 | Click Configure in the real-time data window
                                          or choose Script > Configure Real-Time Data .
                                          The Configure real-time data dialog box opens.Use this dialog box to add new columns, remove existing
                                          columns, reorder the columns, or change the column labels. |
|---|---|
| Step 2 | Choose a Routing target type (Service, Scheduled
                                          Target, or Skill groups). This updates the other fields: The Real-Time Columns list contains all the real-time
                                                   columns available in the database for the target type. The Routing Target Columns list contains the columns
                                                   to appear in the Real-Time Data window. If you select a column in the Routing Target Columns
                                                   list, the heading for that column appears in the Column
                                                   Header field. |
| Step 3 | Use the Add and Remove buttons to move columns between the
                                          lists. Use the Move buttons to change the order of the selected
                                          columns. (To change back to the default column order, click Default Columns .) |
| Step 4 | Optionally, to edit a Routing Target Columns heading, make
                                          changes within the Column Header field. (To change back to the
                                          default header, highlight the Routing Target Column name and
                                          click the Default Header button.) |
| Step 5 | Optionally, select the Short Headers / Long Headers radio buttons to change
                                          between the full and abbreviated forms of the default column
                                          headers. The abbreviated forms are typically three to four
                                          letters. (For example, AHT is used for Average Handle Time.) |
| Step 6 | To save the changes, click OK . The settings
                                          apply to the current and future Script Editor sessions. |

| Step 1 | Choose File > Export
                                          				Script . The Export Script dialog box opens with the name of the current
                                       			 script and version number in the File name field. |
|---|---|
| Step 2 | Optionally,
                                       			 change the file name. You cannot change the file type; you can only save the
                                       			 script in .ICMS format. |
| Step 3 | Click Save . If the
                                       			 file name already exists, the system prompts you to confirm the save. |
| Step 4 | If prompted,
                                       			 click OK . |

| Note | ICM Scripts,
                                          			 which are created on newer versions of the ICM Script editor, will be unable to
                                          			 import the newer scripts into the older ICM versions. |
|---|---|

| Step 1 | Choose File > Import
                                          				Script . The Select Script to Import dialog box opens. |
|---|---|
| Step 2 | Choose a file
                                       			 name with an Unified ICM Script extension (.ICMS) and click Open . The
                                       			 Script Editor performs automapping and the following happens: If all
                                                					 imported objects were successfully auto-mapped, a message window appears
                                                					 prompting you to review the mappings. Click OK to
                                                					 access the Object Mapping dialog box. If some
                                                					 imported objects were not successfully auto-mapped, the partially mapped script
                                                					 is opened as a new script in Import mode and the Object Mapping dialog box
                                                					 appears, with all unmapped objects labeled - -
                                                   						Unmapped - - . The Object Mapping dialog box contains three columns: Object
                                                      						  Types. The type of the imported object. Imported
                                                      						  Object. The name of the imported object. Mapped
                                                      						  To. What this imported object will be mapped to. |
| Step 3 | Click an
                                       			 Imported Object value. The Mapped To column's drop-down list shows all the
                                       			 valid objects on the target system. (The Script Editor window also highlights
                                       			 the script nodes that refer to this object.) |
| Step 4 | Optionally,
                                       			 choose an object from the Mapped To drop-down list on the target system that
                                       			 you want to map the imported object to. Note Choose an
                                                      				  object from the Mapped To drop-down list on the target system that you want to
                                                      				  map the imported object to. | Note | Choose an
                                                      				  object from the Mapped To drop-down list on the target system that you want to
                                                      				  map the imported object to. |
| Note | Choose an
                                                      				  object from the Mapped To drop-down list on the target system that you want to
                                                      				  map the imported object to. |
| Step 5 | When the mapping
                                       			 is complete, click Apply and
                                       			 Finish. |

| Note | Choose an
                                                      				  object from the Mapped To drop-down list on the target system that you want to
                                                      				  map the imported object to. |
|---|---|

| Note | ICM Scripts,
                                          			 which are created on newer versions of the ICM Script editor, will be unable to
                                          			 import the newer scripts into the older ICM versions. |
|---|---|

| Step 1 | Within the Unified CCE Configuration Manager, choose Tools > Miscellaneous Tools > System Information . The System Information window opens. |
|---|---|
| Step 2 | Enter the Minimum Script Schedule Time. |
| Step 3 | Set the number of script versions to be retained in the Retain
                                       Script Versions field. |
| Step 4 | Click Save to apply your changes. |

| Script Editor | Internet Script Editor |
|---|---|
| Is automatically deployed as part of the Unified CCE AW-HDS or AW-HDS-DDS installation. | Must be enabled during the installation of the Unified CCE AW-HDS or AW-HDS-DDS Server by selecting it in Web Setup, then
                                       downloaded and installed. |
| Requires a full Administration and Data server. You must run it from the Unified CCE AW-HDS or AW-HDS-DDS Server, based on
                                       your deployment. | Can be run on a local machine. |
| Can be used by global administrators. | Can be used by global administrators and departmental administrators. |
| Imposes no scripting access restrictions for global administrators. | Imposes scripting access restrictions for departmental administrators. |