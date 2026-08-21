---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-rtmt-cucm-b-cisco-unified-rtmt-administration-1251-cucm--50f4b373a1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/rtmt/cucm_b_cisco-unified-rtmt-administration-1251/cucm_mp_m4b3295d_00_manage-performance-counters.html
retrieved_at: 2026-08-21T01:39:09.548069+00:00
---

Cisco Unified Real-Time Monitoring Tool Administration Guide, Release 12.5(1)

# Cisco Unified Real-Time Monitoring Tool Administration Guide, Release 12.5(1)

Updated: September 24, 2024

Chapter: Performance Counters

## Chapter: Performance Counters

# Performance Counters

Counters

## Add Counter Using
                        	 Performance Queries

You can use
                              		  queries to select and display perfmon counters. You can organize the perfmon
                              		  counters to display a set of feature-based counters and save it in a category.
                              		  After you save your Unified RTMT profile, you can quickly access the counters
                              		  in which you are interested.

Unified RTMT displays perfmon counters in chart or table format. The chart format displays the perfmon counter information
                              by using line charts. For each category tab that you create, you can display up to six charts in the Perfmon Monitoring pane
                              with up to three counters in one chart. After you create a category, you cannot change the display from a chart format to
                              a table format, or vice-versa.

Tip

You can display up to three counters in one chart in the Perfmon Monitoring pane. To add another counter in a chart, click
                                          the counter and drag it to the Perfmon Monitoring pane. Repeat, to add up to three counters.

By default, Unified RTMT displays perfmon counters in a chart format. You can also choose to display the perfmon counters
                              in a table format. To display the perfmon counters in a table format, check the Present Data in Table View check-box when you create a new category.

Step 1

Choose System > Performance > Open Performance
                                             				  Monitoring .

Step 2

Click the name
                                       			 of the server where you want to add a counter to monitor.

The tree
                                          				hierarchy expands and displays all the perfmon objects.

Step 3

To monitor a counter in a table format, continue to step 4. To monitor a counter in a chart format, skip to step 9.

Step 4

Choose Edit > New
                                             				  Category .

Step 5

In the Enter
                                       			 Name field, enter a name for the tab.

Step 6

To display the perfmon counters in table format, check the Present Data in Table View check-box.

Step 7

Click OK .

A new tab with
                                          				the name that you entered appears at the bottom of the pane.

Step 8

Perform one of
                                       			 the following actions to select one or more counters with one or more instances
                                       			 for monitoring in table format (skip the remaining step in this procedure):

- Double-click a single counter and select a single instance from the dialog box, and then click Add .

- Double-click a single counter and select multiple instances from the dialog box, and then, click Add .

Tip

To display the counter in a chart format after you display it in a table format, right-click the category tab and choose Remove Category . The counter displays in a chart format.

Step 9

To monitor a counter in a chart format, perform the following tasks:

Click the file icon next to the object name that lists the counters that you want to monitor.

A list of counters appears.

To display the counter information, either right-click the counter and click Counter Monitoring , double-click the counter, or drag and drop the counter into the Perfmon Monitoring pane.

The counter chart appears in the Perfmon Monitoring pane.

## Remove Counter From
                        	 Performance Monitoring Pane

You can remove a counter chart (table entry) with the Remove the Chart or Table Entry menu item in the Perfmon menu in the
                              menu bar.

You can
                              		  remove counters from the RTMT Perfmon Monitoring pane when you no longer need
                              		  them. Follow this procedure to remove a counter from the pane.

Perform one of
                                       			 the following tasks:

- Right-click the counter that
                                          				you want to remove and choose Remove .

- Click the counter that you
                                          				want to remove and choose Perfmon > Remove Chart/Table
                                                					 Entry .

## Add Counter
                        	 Instance

Follow
                              		  this procedure to add a counter instance.

Step 1

Find and display
                                       			 the performance monitoring counter.

Step 2

Click the
                                       			 performance monitoring counter in the performance monitoring tree hierarchy and
                                       			 choose System > Performance > Counter
                                             				  Instances .

Step 3

In the Select
                                          				Instance window, click the instance, and then click Add .

The counter
                                          				appears.

## Set Up Counter Alert
                        	 Notification

Follow
                              		  this procedure to configure alert notification for a counter.

Tip

To remove the
                                          			 alert for the counter, right-click the counter and choose Remove Alert. The
                                          			 option appears gray after you remove the alert.

Step 1

Find and display
                                       			 the performance counter.

Step 2

From the counter
                                       			 chart or table, right-click the counter for which you want to configure the
                                       			 alert notification, and choose Set
                                          				Alert/Properties .

Step 3

Check the Enable
                                          				Alert check box.

Step 4

In the Severity drop-down list box, choose the severity
                                       			 level at which you want to be notified.

Step 5

In the
                                       			 Description pane, enter a description of the alert and click Next .

Step 6

Configure the
                                       			 settings in the Threshold, Value Calculated As, Duration, Frequency, and
                                       			 Schedule panes. After you enter the settings in the window, click Next to proceed to the next panes.

Step 7

To configure the
                                       			 system to send an e-mail message for the alert, check the Enable
                                          				Email check box.

Step 8

To trigger an
                                       			 alert action that is already configured, choose the alert action that you want
                                       			 from the Trigger
                                          				Alert Action drop-down list box.

Step 9

To configure a
                                       			 new alert action for the alert, click Configure .

Whenever the
                                                      				  specified alert is triggered, the system sends the alert action.

The Alert
                                             				  Action dialog box appears.

Step 10

To add a new
                                       			 alert action, click Add .

The Action
                                          				Configuration dialog box appears.

Step 11

In the Name
                                       			 field, enter a name for the alert action.

Step 12

In the
                                       			 Description field, enter a description for the alert action.

Step 13

Click Add to add a new e-mail recipient for the alert
                                       			 action.

The Input
                                          				dialog box appears.

Step 14

Enter either
                                       			 the e-mail or e-page address of the recipient that you want to receive the
                                       			 alert action notification and click OK

Step 15

In the
                                       			 User-defined email text box, enter the text that you want to display in the
                                       			 e-mail message and click Activate .

## Display Counter
                        	 Description

The
                              		  following shows how to obtain a description of the counter:

Step 1

Perform one of
                                       			 the following tasks:

In the
                                             				  Perfmon tree hierarchy, right-click the counter for which you want property
                                             				  information and choose Counter Description .

In the RTMT
                                             				  Performance Monitoring pane, click the counter and choose System > Performance > Counter
                                                   						Description from the menu bar.

Tip

You can
                                                            						display the counter description and configure data-sampling parameters.

The Counter Property window displays the description of
                                                					 the counter. The description includes the host address, the object to which the
                                                					 counter belongs, the counter name, and a brief overview of what the counter
                                                					 does.

Step 2

To close the Counter
                                          				Property window, click OK .

## Local Perfmon Counter Data Logging

RTMT allows you to choose different perfmon counters to log locally. You can then view the data from the perfmon CSV log by
                              using the performance log viewer.

### Start Perfmon
                           	 Counter Logging

To start
                                 		  logging perfmon counter data into a CSV log file, perform the following
                                 		  procedure:

Step 1

Find and display
                                          			 the performance monitoring counters.

Step 2

If you are
                                          			 displaying perfmon counters in the chart format, right-click the graph for
                                          			 which you want data sample information and choose Start
                                             				Counter(s) Logging .

The Counter
                                                				  Logging Configuration dialog box appears.

Step 3

If you want to
                                          			 log all counters in a screen (both chart and table view format), you can
                                          			 right-click the category name tab at the bottom of the window and choose Start
                                             				Counter(s) Logging .

The Counter
                                                				  Logging Configuration dialog box appears.

Step 4

Configure the maximum file size and maximum number of files parameter.

Step 5

In the Logger
                                             			 File Name field, enter a filename and click OK .

RTMT saves the
                                             				CSV log files in the log folder in the .jrtmt directory under the user home
                                             				directory. For example, in Windows, the path specifies D:\Documents and Settings\userA\.jrtmt\log , or in
                                             				Linux, the path specifies /users/home/.jrtmt/log .

To limit the
                                             				number and size of the files, configure the maximum file size and maximum
                                             				number of files parameter in the trace output setting for the specific service
                                             				in the Trace
                                                				  Configuration window of Cisco Unified
                                                				  Serviceability . See Cisco Unified Serviceability Administration
                                                   					 Guide .

### Stop Perfmon Counter
                           	 Logging

To stop
                                 		  logging perfmon counter data, perform the following procedure:

Step 1

Find and display
                                          			 the performance monitoring counters.

Step 2

If you are
                                          			 displaying perfmon counters in the chart format, right-click the graph for
                                          			 which counter logging is started and choose Stop
                                             				Counter(s) Logging . If you want to stop logging of all counters in
                                          			 a screen (both chart and table view format), you can right-click the category
                                          			 name tab at the bottom of the window and choose Stop
                                             				Counter(s) Logging .

### Configure Data
                           	 Sample

The Counter
                                    			 Property window contains the option to configure data samples for a
                                 		  counter. The perfmon counters that display in the RTMT Perfmon Monitoring pane
                                 		  contain green dots that represent samples of data over time. You can configure
                                 		  the number of data samples to collect and the number of data points to show in
                                 		  the chart. After the data sample is configured, view the information by using
                                 		  the View All Data/View Current Data menu option.

Follow
                                 		  this procedure to configure the number of data samples to collect for a
                                 		  counter.

Step 1

Find and display
                                          			 the counter.

Step 2

Click the
                                          			 counter for which you want data sample information and choose System > Performance > Monitoring
                                                				  Properties .

The Counter Property window displays the description of
                                             				the counter, as well as the tab for configuring data samples. The description
                                             				includes the host address, the object to which the counter belongs, the counter
                                             				name, and a brief overview of what the counter does.

Step 3

To configure the
                                          			 number of data samples for the counter, click the Data
                                             				Sample tab.

Step 4

From the No. of
                                             				data samples drop-down list box, choose the number of samples
                                          			 (between 100 and 1000).

The default
                                             				specifies 100.

Step 5

From the No. of
                                             				data points shown on chart drop-down list box, choose the number of
                                          			 data points to display on the chart (between 10 and 50).

The default
                                             				specifies 20.

Step 6

Click one of the
                                          			 following parameters:

Absolute: Because some counter values are accumulative, choose
                                                   					 Absolute to display the data at its current status.

Delta: Choose Delta to display the difference between the
                                                   					 current counter value and the previous counter value.

Delta Percentage: Choose Delta Percentage to display the counter
                                                   					 performance changes in percentage.

Step 7

To close the Counter
                                             				Property window and return to the RTMT Perfmon Monitoring pane,
                                          			 click OK .

### View Counter
                           	 Data

Follow
                                 		  this procedure to view the data that is collected for a performance counter.

Step 1

In the RTMT
                                          			 Perfmon Monitoring pane, right-click the counter chart for the counter for
                                          			 which you want to view data samples.

Step 2

Choose View All
                                             				Data .

The counter
                                             				chart displays all data that has been sampled. The green dots display close
                                             				together.

Step 3

Right-click the
                                          			 counter that currently appears.

Step 4

Choose View
                                             				Current .

The counter
                                             				chart displays the last configured data samples that were collected.

## Log files on Perfmon Log Viewer and Microsoft Performance Tool

The performance log viewer displays a chart with the data
                              		  from the selected counters. The bottom pane displays the selected counters, a
                              		  color legend for those counters, display option, mean value, minimum value, and
                              		  the maximum value.

The following table describes the functions of different
                              		  buttons that are available on the Performance Log Viewer.

Button

Function

Select Counters

Allows you to add counters that you want to display
                                          					 in the performance log viewer. If you do not want to display a counter, uncheck
                                          					 the Display column next to the counter.

Reset View

Resets the performance log viewer to the initial
                                          					 default view.

Save Downloaded File

Allows you to save the log file to your local
                                          					 computer.

### View Log Files on
                           	 Perfmon Log Viewer

The
                                 		  Performance Log Viewer displays data for counters from perfmon CSV log files in
                                 		  a graphical format. You can use the performance log viewer to display data from
                                 		  the local perfmon logs that you collected, or you can display the data from the
                                 		  Real-time Information Server Data Collection (RISDC) perfmon logs.

#### Before you begin

The local
                                 		  perfmon logs consist of data from counters that you select and store locally on
                                 		  your computer.

Step 1

Select System > Performance > Open Performance Log
                                                				  Viewer .

Step 2

Select the type
                                          			 of perfmon logs that you want to view:

Select
                                                      						RisDC Perfmon Logs in the Select Perfmon Log Location section.

Select a
                                                      						node from the list box.

Select Open .

Select the
                                                      						file and select Open File .

Check the
                                                      						counters that you want to display.

Select OK .

Select Local Perfmon Logs .

Select Open .

Browse to
                                                      						the file directory.

Select the
                                                      						file that you are interested in viewing or enter the filename in the filename
                                                      						field.

Select Open .

Check the
                                                      						counters that you want to display.

Select OK .

Step 3

Select the
                                          			 counters that you want to display.

Step 4

Select OK .

### Zoom In and Out in Performance Log Viewer

The Performance Log viewer includes a zoom feature that
                                 		  allows you to zoom in on and out on an area in the chart.

Step 1

Perform one of the following actions:

On the Quick Launch Channel:

- Select System .

- In the tree
                                                      						hierarchy, double-select Performance to display the performance
                                                         						  icons .

- Select the Performance icon.

Select System > Performance > Open
                                                      						Performance Monitoring .

Step 2

Select the name of the server where the counter is located.

The tree hierarchy expands and displays all the perfmon objects
                                             				for the node.

Step 3

Double-select the performance counter you want to monitor.

Step 4

Perform one of the following actions:

If you want to:

Action

Zoom in on an area in the chart

- Select and
                                                            								drag the left mouse button over the area of the chart in which you are
                                                            								interested.

- Release the
                                                            								left mouse button when you have the selected area.

Reset the chart to the initial default view

Perform one of the following actions:

- Select Reset View .

- Right-mouse
                                                            								select the chart and select Reset .

### View Perfmon Log Files with Microsoft Performance Tool

The method for accessing Performance may vary depending on the
                                             					 version of windows you install on your computer.

Step 1

Select Start > Settings > Control
                                                				  Panel > Administrative
                                                				  Tools > Performance .

Step 2

Perform the following actions in the application window:

Select the right mouse button.

Select Properties .

Step 3

Select the Source tab in the System Monitor Properties dialog box.

Step 4

Browse to the directory where you downloaded the perfmon log file
                                          			 and select the perfmon csv file. The log file includes the following naming
                                          			 convention:
                                          			 PerfMon_<node>_<month>_<day>_<year>_<hour>_<minute>.csv;
                                          			 for example, PerfMon_172.19.240.80_06_15_2005_11_25.csv.

Step 5

Select Apply .

Step 6

Select Time Range . To specify the time range in the
                                          			 perfmon log file that you want to view, drag the bar to the appropriate
                                          			 starting and ending times.

Step 7

To open the Add Counters dialog box, select the Data tab and
                                          			 select Add .

Step 8

Select the perfmon object from the Performance Object drop-down list box. If
                                          			 an object has multiple instances, you may select All instances or select only the instances
                                          			 that you are interested in viewing.

Step 9

You can select All Counters or select only the counters that
                                          			 you are interested in viewing.

Step 10

Select Add to add the selected counters.

Step 11

Select Close when you finish selecting counters .

Troubleshooting

## Perfmon Data Log Troubleshooting

The troubleshooting perfmon data logging feature assists
                              		  Cisco TAC in identifying system problems. When you enable troubleshooting
                              		  perfmon data logging, you initiate the collection of a set of 
                              		  system and operating system performance statistics on the selected
                              		  node. The statistics that are collected include comprehensive information that
                              		  you can use for system diagnosis.

The system automatically enables troubleshooting perfmon data logging to collect statistics from a set of perfmon counters
                              that provides comprehensive information about the system state. When you enable Troubleshooting Perfmon Data Logging, Cisco
                              estimates that the system experiences a less than five percent increase in CPU utilization and an insignificant increase in
                              the amount of memory that is being used, and it writes approximately 50 MB of information to the log files daily.

You can perform the following administrative tasks with the
                              		  troubleshooting perfmon data logging feature:

Enable and disable the trace filter for Troubleshooting perfmon data logging.

Monitor a set of predefined System and performance objects and counters on each server.

Log the monitored performance data in CSV file format on the server in the active log partition in the var/log/active/cm/log/ris/csv
                                    directory. The log file uses the following naming convention: PerfMon_<node>_<month>_<day>_<year>_<hour>_<minute>.csv; for
                                    example, PerfMon_172.19.240.80_06_15_2005_11_25.csv. Specify the polling rate. This rate specifies the rate at which performance
                                    data is gathered and logged. You can configure the polling rate down to 5 seconds. Default polling rate equals 15 seconds.

View the log file in graphical format by using the Microsoft Windows performance tool or by using the Performance Log viewer
                                    in the Real-Time Monitoring Tool.

Specify the maximum number of log files that will be stored on disk. Log files exceeding this limit are purged automatically
                                    by removal of the oldest log file. The default specifies 50 files.

Specify the rollover criteria of the log file based on the maximum size of the file in megabytes. The default value specifies
                                    2 MB.

Collect the Cisco RIS Data Collector PerfMonLog log file by using the Trace & Log Central feature of the Real-Time Monitoring
                                    Tool or Command Line Interface.

The troubleshooting perfmon data-logging feature collects information from the following counters within the following perfmon
                              objects.

Database Change Notification Server Object:

Clients

CNProcessed

QueueDelay

QueuedRequestsInDB

QueuedRequestsInMemory

Database Local DSN Object:

CcmDbSpace_Used

CcmtempDbSpace_Used

CNDbSpace_Used

LocalDSN

RootDbSpace_Used

SharedMemory_Free

SharedMemory_Used

Enterprise Replication DBSpace Monitors Object:

ERDbSpace_Used

ERSBDbSpace_Used

IP Object:

In Receives

In HdrErrors

In UnknownProtos

In Discards

In Delivers

Out Requests

Out Discards

Reasm Reqds

Reasm Oks

Reasm Fails

Frag OKs

Frag Fails

Frag Creates

InOut Requests

Memory Object:

% Page Usage

% VM Used

% Mem Used

Buffers Kbytes

Cached Kbytes

Free Kbytes

Free Swap Kbytes

HighFree

HighTotal

Low Total

Low Free

Page Faults Per Sec

Page Major Faults Per Sec

Pages

Pages Input

Pages Input Per Sec

Pages Output

Pages Output Per Sec

SlabCache

SwapCached

Shared Kbytes

Total Kbytes

Total Swap Kbytes

Total VM Kbytes

Used Kbytes

Used Swap Kbytes

Used VM Kbytes

Network Interface Object:

Rx Bytes

Rx Packets

Rx Errors

Rx Dropped

Rx Multicast

Tx Bytes

Tx Packets

Tx Errors

Tx Dropped

Total Bytes

Total Packets

Tx QueueLen

Number of Replicates Created and State of Replication Object:

Replicate_State

Partition Object:

% CPU Time

%Used

Await Read Time

Await Time

Await Write Time

Queue Length

Read Bytes Per Sec

Total Mbytes

Used Mbytes

Write Bytes Per Sec

Process Object:

% Memory Usage

Data Stack Size

Nice

PID

STime

% CPU Time

Page Fault Count

Process Status

Shared Memory Size

VmData

VmRSS

VmSize

Thread Count

Total CPU Time Used

Processor Object:

Irq Percentage

Softirq Percentage

IOwait Percentage

User Percentage

Nice Percentage

System Percentage

Idle Percentage

%CPU Time

System Object:

Allocated FDs

Freed FDs

Being Used FDs

Max FDs

Total Processes

Total Threads

Total CPU Time

TCP Object:

Active Opens

Passive Opens

Attempt Fails

Estab Resets

Curr Estab

In Segs

Out Segs

Retrans Segs

InOut Segs

Thread Object (Troubleshooting Perfmon Data Logger only logs Unified Communications Manager threads):

%CPU Time

Cisco CallManager Object:

CallManagerHeartBeat

CallsActive

CallsAttempted

CallsCompleted

InitializationState

RegisteredHardwarePhones

RegisteredMGCPGateway

RegisteredOtherStationDevices

Cisco SIP Stack Object:

CCBsAllocated

SCBsAllocated

SIPHandlerSDLQueueSignalsPresent

Cisco CallManager System Performance Object:

AverageExpectedDelay

CallsRejectedDueToThrottling

CodeRedEntryExit

CodeYellowEntryExit

QueueSignalsPresent 1-High

QueueSignalsPresent 2-Normal

QueueSignalsPresent 3-Low

QueueSignalsPresent 4-Lowest

QueueSignalsProcessed 1-High

QueueSignalsProcessed 2-Normal

QueueSignalsProcessed 3-Low

QueueSignalsProcessed 4-Lowest

QueueSignalsProcessed Total

SkinnyDevicesThrottled

ThrottlingSampleActivity

TotalCodeYellowEntry

Cisco TFTP Server Object:

BuildAbortCount

BuildCount

BuildDeviceCount

BuildDialruleCount

BuildDuration

BuildSignCount

BuildSoftkeyCount

BuildUnitCount

ChangeNotifications

DeviceChangeNotifications

DialruleChangeNotifications

EncryptCount

GKFoundCount

GKNotFoundCount

HeartBeat

HttpConnectRequests

HttpRequests

HttpRequestsAborted

HttpRequestsNotFound

HttpRequestsOverflow

HttpRequestsProcessed

HttpServedFromDisk

LDFoundCount

LDNotFoundCount

MaxServingCount

Requests

RequestsAborted

RequestsInProgress

RequestsNotFound

RequestsOverflow

RequestsProcessed

SegmentsAcknowledged

SegmentsFromDisk

SegmentsSent

SEPFoundCount

SEPNotFoundCount

SIPFoundCount

SIPNotFoundCount

SoftkeyChangeNotifications

UnitChangeNotifications

### Troubleshoot
                           	 Perfmon Data Logging

Follow
                                 		  this procedure to collect information from counters within the perfmon objects
                                 		  with the perfmon data-logging feature.

#### Before you begin

- Be aware that RISDC perfmon
                                    			 logging is also known as Troubleshooting Perfmon Data logging. When you enable
                                    			 RISDC perfmon logging, the server collects performance data that are used to
                                    			 troubleshoot problems.

- When you enable RIS Data
                                    			 Collector (RISDC) perfmon logs, Unified Communications
                                       				Manager and the IM and Presence
                                       				Service collect information for the system in logs that are written
                                    			 on the server.

- You can enable or disable
                                    			 RISDC perfmon logs in the administrative interface by selecting System > Service
                                          				  Parameter and selecting the Cisco RIS Data Collector
                                    			 Service from the Service list box. By default, RISDC perfmon logging is
                                    			 enabled.

Step 1

Select System > Service
                                                				  Parameters the administration interface.

Step 2

Select the
                                          			 server from the Server list box.

Step 3

Select the
                                          			 Cisco RIS Data Collector from the Service drop-down list box.

Step 4

Enter the
                                          			 appropriate settings as described in the following table.

Field

Description

Enable Logging

From the drop-down list box, select True to enable or False to disable troubleshooting perfmon data
                                                         						  logging. The default value specifies False.

Polling Rate

Enter the polling rate interval (in seconds). You can enter a
                                                         						  value from 5 (minimum) to 300 (maximum). The default value specifies 15.

Maximum No. of Files

Enter the maximum number of Troubleshooting Perfmon Data Logging
                                                         						  files that you want to store on disk. You can enter a value from 1 (minimum) up
                                                         						  to 100 (maximum). The default value specifies 50.

Consider your storage capacity in configuring the Maximum No. of
                                                         						  Files and Maximum File Size Parameters. We recommend that you do not exceed a
                                                         						  value of 100 MB when you multiply the Maximum Number of Files value by the
                                                         						  Maximum File Size value.

When the number of files exceeds the maximum number of files
                                                         						  that you specified in this field, the system deletes log files with the oldest
                                                         						  time stamp.

Caution

If
                                                                     							 you do not save the log files on another computer before you change this
                                                                     							 parameter, you risk losing the log files.

Maximum File Size (MB)

Enter the maximum file size (in megabytes) that you want to
                                                         						  store in a perfmon log file before a new file is started. You can enter a value
                                                         						  from 1 (minimum) to 500 (maximum). The default value specifies 2 MB.

Consider your storage capacity in configuring the Maximum No. of
                                                         						  Files and Maximum File Size Parameters. We recommend that you do not exceed a
                                                         						  value of 100 MB when you multiply the Maximum Number of Files value by the
                                                         						  Maximum File Size value.

Step 5

Select Save .

You
                                                         				  can collect the log files for Cisco RIS Data Collector service on the server by
                                                         				  using RTMT to download the log files. If you want to download the log files by
                                                         				  using the CLI, refer to Cisco
                                                            					 Unified Communications Operating System Administration Guide . After you
                                                         				  collect the log files, you can view the log file by using the Performance Log
                                                         				  Viewer in RTMT or by using the Microsoft Windows performance tool.

| Tip | You can display up to three counters in one chart in the Perfmon Monitoring pane. To add another counter in a chart, click
                                          the counter and drag it to the Perfmon Monitoring pane. Repeat, to add up to three counters. |
|---|---|

| Step 1 | Choose System > Performance > Open Performance
                                             				  Monitoring . |
|---|---|
| Step 2 | Click the name
                                       			 of the server where you want to add a counter to monitor. The tree
                                          				hierarchy expands and displays all the perfmon objects. |
| Step 3 | To monitor a counter in a table format, continue to step 4. To monitor a counter in a chart format, skip to step 9. |
| Step 4 | Choose Edit > New
                                             				  Category . |
| Step 5 | In the Enter
                                       			 Name field, enter a name for the tab. |
| Step 6 | To display the perfmon counters in table format, check the Present Data in Table View check-box. |
| Step 7 | Click OK . A new tab with
                                          				the name that you entered appears at the bottom of the pane. |
| Step 8 | Perform one of
                                       			 the following actions to select one or more counters with one or more instances
                                       			 for monitoring in table format (skip the remaining step in this procedure): Double-click a single counter and select a single instance from the dialog box, and then click Add . Double-click a single counter and select multiple instances from the dialog box, and then, click Add . Tip To display the counter in a chart format after you display it in a table format, right-click the category tab and choose Remove Category . The counter displays in a chart format. | Tip | To display the counter in a chart format after you display it in a table format, right-click the category tab and choose Remove Category . The counter displays in a chart format. |
| Tip | To display the counter in a chart format after you display it in a table format, right-click the category tab and choose Remove Category . The counter displays in a chart format. |
| Step 9 | To monitor a counter in a chart format, perform the following tasks: Click the file icon next to the object name that lists the counters that you want to monitor. A list of counters appears. To display the counter information, either right-click the counter and click Counter Monitoring , double-click the counter, or drag and drop the counter into the Perfmon Monitoring pane. The counter chart appears in the Perfmon Monitoring pane. |

| Tip | To display the counter in a chart format after you display it in a table format, right-click the category tab and choose Remove Category . The counter displays in a chart format. |
|---|---|

| Perform one of
                                       			 the following tasks: Right-click the counter that
                                          				you want to remove and choose Remove . Click the counter that you
                                          				want to remove and choose Perfmon > Remove Chart/Table
                                                					 Entry . |
|---|

| Step 1 | Find and display
                                       			 the performance monitoring counter. |
|---|---|
| Step 2 | Click the
                                       			 performance monitoring counter in the performance monitoring tree hierarchy and
                                       			 choose System > Performance > Counter
                                             				  Instances . |
| Step 3 | In the Select
                                          				Instance window, click the instance, and then click Add . The counter
                                          				appears. |

| Tip | To remove the
                                          			 alert for the counter, right-click the counter and choose Remove Alert. The
                                          			 option appears gray after you remove the alert. |
|---|---|

| Step 1 | Find and display
                                       			 the performance counter. |
|---|---|
| Step 2 | From the counter
                                       			 chart or table, right-click the counter for which you want to configure the
                                       			 alert notification, and choose Set
                                          				Alert/Properties . |
| Step 3 | Check the Enable
                                          				Alert check box. |
| Step 4 | In the Severity drop-down list box, choose the severity
                                       			 level at which you want to be notified. |
| Step 5 | In the
                                       			 Description pane, enter a description of the alert and click Next . |
| Step 6 | Configure the
                                       			 settings in the Threshold, Value Calculated As, Duration, Frequency, and
                                       			 Schedule panes. After you enter the settings in the window, click Next to proceed to the next panes. |
| Step 7 | To configure the
                                       			 system to send an e-mail message for the alert, check the Enable
                                          				Email check box. |
| Step 8 | To trigger an
                                       			 alert action that is already configured, choose the alert action that you want
                                       			 from the Trigger
                                          				Alert Action drop-down list box. |
| Step 9 | To configure a
                                       			 new alert action for the alert, click Configure . Note Whenever the
                                                      				  specified alert is triggered, the system sends the alert action. The Alert
                                             				  Action dialog box appears. | Note | Whenever the
                                                      				  specified alert is triggered, the system sends the alert action. |
| Note | Whenever the
                                                      				  specified alert is triggered, the system sends the alert action. |
| Step 10 | To add a new
                                       			 alert action, click Add . The Action
                                          				Configuration dialog box appears. |
| Step 11 | In the Name
                                       			 field, enter a name for the alert action. |
| Step 12 | In the
                                       			 Description field, enter a description for the alert action. |
| Step 13 | Click Add to add a new e-mail recipient for the alert
                                       			 action. The Input
                                          				dialog box appears. |
| Step 14 | Enter either
                                       			 the e-mail or e-page address of the recipient that you want to receive the
                                       			 alert action notification and click OK |
| Step 15 | In the
                                       			 User-defined email text box, enter the text that you want to display in the
                                       			 e-mail message and click Activate . |

| Note | Whenever the
                                                      				  specified alert is triggered, the system sends the alert action. |
|---|---|

| Step 1 | Perform one of
                                       			 the following tasks: In the
                                             				  Perfmon tree hierarchy, right-click the counter for which you want property
                                             				  information and choose Counter Description . In the RTMT
                                             				  Performance Monitoring pane, click the counter and choose System > Performance > Counter
                                                   						Description from the menu bar. Tip You can
                                                            						display the counter description and configure data-sampling parameters. The Counter Property window displays the description of
                                                					 the counter. The description includes the host address, the object to which the
                                                					 counter belongs, the counter name, and a brief overview of what the counter
                                                					 does. | Tip | You can
                                                            						display the counter description and configure data-sampling parameters. |
|---|---|---|---|
| Tip | You can
                                                            						display the counter description and configure data-sampling parameters. |
| Step 2 | To close the Counter
                                          				Property window, click OK . |

| Tip | You can
                                                            						display the counter description and configure data-sampling parameters. |
|---|---|

| Step 1 | Find and display
                                          			 the performance monitoring counters. |
|---|---|
| Step 2 | If you are
                                          			 displaying perfmon counters in the chart format, right-click the graph for
                                          			 which you want data sample information and choose Start
                                             				Counter(s) Logging . The Counter
                                                				  Logging Configuration dialog box appears. |
| Step 3 | If you want to
                                          			 log all counters in a screen (both chart and table view format), you can
                                          			 right-click the category name tab at the bottom of the window and choose Start
                                             				Counter(s) Logging . The Counter
                                                				  Logging Configuration dialog box appears. |
| Step 4 | Configure the maximum file size and maximum number of files parameter. |
| Step 5 | In the Logger
                                             			 File Name field, enter a filename and click OK . RTMT saves the
                                             				CSV log files in the log folder in the .jrtmt directory under the user home
                                             				directory. For example, in Windows, the path specifies D:\Documents and Settings\userA\.jrtmt\log , or in
                                             				Linux, the path specifies /users/home/.jrtmt/log . To limit the
                                             				number and size of the files, configure the maximum file size and maximum
                                             				number of files parameter in the trace output setting for the specific service
                                             				in the Trace
                                                				  Configuration window of Cisco Unified
                                                				  Serviceability . See Cisco Unified Serviceability Administration
                                                   					 Guide . Note If you have already started logging perfmon counters and you want to change the maximum file size and maximum number of files,
                                                      you must first stop the counters before you reconfigure the maximum file size and number of files parameters. After resetting
                                                      the parameters, you can then restart logging perfmon counters. | Note | If you have already started logging perfmon counters and you want to change the maximum file size and maximum number of files,
                                                      you must first stop the counters before you reconfigure the maximum file size and number of files parameters. After resetting
                                                      the parameters, you can then restart logging perfmon counters. |
| Note | If you have already started logging perfmon counters and you want to change the maximum file size and maximum number of files,
                                                      you must first stop the counters before you reconfigure the maximum file size and number of files parameters. After resetting
                                                      the parameters, you can then restart logging perfmon counters. |

| Note | If you have already started logging perfmon counters and you want to change the maximum file size and maximum number of files,
                                                      you must first stop the counters before you reconfigure the maximum file size and number of files parameters. After resetting
                                                      the parameters, you can then restart logging perfmon counters. |
|---|---|

| Step 1 | Find and display
                                          			 the performance monitoring counters. |
|---|---|
| Step 2 | If you are
                                          			 displaying perfmon counters in the chart format, right-click the graph for
                                          			 which counter logging is started and choose Stop
                                             				Counter(s) Logging . If you want to stop logging of all counters in
                                          			 a screen (both chart and table view format), you can right-click the category
                                          			 name tab at the bottom of the window and choose Stop
                                             				Counter(s) Logging . |

| Step 1 | Find and display
                                          			 the counter. |
|---|---|
| Step 2 | Click the
                                          			 counter for which you want data sample information and choose System > Performance > Monitoring
                                                				  Properties . The Counter Property window displays the description of
                                             				the counter, as well as the tab for configuring data samples. The description
                                             				includes the host address, the object to which the counter belongs, the counter
                                             				name, and a brief overview of what the counter does. |
| Step 3 | To configure the
                                          			 number of data samples for the counter, click the Data
                                             				Sample tab. |
| Step 4 | From the No. of
                                             				data samples drop-down list box, choose the number of samples
                                          			 (between 100 and 1000). The default
                                             				specifies 100. |
| Step 5 | From the No. of
                                             				data points shown on chart drop-down list box, choose the number of
                                          			 data points to display on the chart (between 10 and 50). The default
                                             				specifies 20. |
| Step 6 | Click one of the
                                          			 following parameters: Absolute: Because some counter values are accumulative, choose
                                                   					 Absolute to display the data at its current status. Delta: Choose Delta to display the difference between the
                                                   					 current counter value and the previous counter value. Delta Percentage: Choose Delta Percentage to display the counter
                                                   					 performance changes in percentage. |
| Step 7 | To close the Counter
                                             				Property window and return to the RTMT Perfmon Monitoring pane,
                                          			 click OK . |

| Step 1 | In the RTMT
                                          			 Perfmon Monitoring pane, right-click the counter chart for the counter for
                                          			 which you want to view data samples. |
|---|---|
| Step 2 | Choose View All
                                             				Data . The counter
                                             				chart displays all data that has been sampled. The green dots display close
                                             				together. |
| Step 3 | Right-click the
                                          			 counter that currently appears. |
| Step 4 | Choose View
                                             				Current . The counter
                                             				chart displays the last configured data samples that were collected. |

| Button | Function |
|---|---|
| Select Counters | Allows you to add counters that you want to display
                                          					 in the performance log viewer. If you do not want to display a counter, uncheck
                                          					 the Display column next to the counter. |
| Reset View | Resets the performance log viewer to the initial
                                          					 default view. |
| Save Downloaded File | Allows you to save the log file to your local
                                          					 computer. |

| Step 1 | Select System > Performance > Open Performance Log
                                                				  Viewer . |
|---|---|
| Step 2 | Select the type
                                          			 of perfmon logs that you want to view: For RisDC Perfmon Logs,
                                             				perform the following steps: Select
                                                      						RisDC Perfmon Logs in the Select Perfmon Log Location section. Select a
                                                      						node from the list box. Select Open . Select the
                                                      						file and select Open File . Check the
                                                      						counters that you want to display. Select OK . For locally stored data,
                                             				perform the following actions: Select Local Perfmon Logs . Select Open . Browse to
                                                      						the file directory. Select the
                                                      						file that you are interested in viewing or enter the filename in the filename
                                                      						field. Select Open . Check the
                                                      						counters that you want to display. Select OK . |
| Step 3 | Select the
                                          			 counters that you want to display. |
| Step 4 | Select OK . |

| Step 1 | Perform one of the following actions: On the Quick Launch Channel: Select System . In the tree
                                                      						hierarchy, double-select Performance to display the performance
                                                         						  icons . Select the Performance icon. Select System > Performance > Open
                                                      						Performance Monitoring . |
|---|---|
| Step 2 | Select the name of the server where the counter is located. The tree hierarchy expands and displays all the perfmon objects
                                             				for the node. |
| Step 3 | Double-select the performance counter you want to monitor. |
| Step 4 | Perform one of the following actions: If you want to: Action Zoom in on an area in the chart Select and
                                                            								drag the left mouse button over the area of the chart in which you are
                                                            								interested. Release the
                                                            								left mouse button when you have the selected area. Reset the chart to the initial default view Perform one of the following actions: Select Reset View . Right-mouse
                                                            								select the chart and select Reset . | If you want to: | Action | Zoom in on an area in the chart | Select and
                                                            								drag the left mouse button over the area of the chart in which you are
                                                            								interested. Release the
                                                            								left mouse button when you have the selected area. | Reset the chart to the initial default view | Perform one of the following actions: Select Reset View . Right-mouse
                                                            								select the chart and select Reset . |
| If you want to: | Action |
| Zoom in on an area in the chart | Select and
                                                            								drag the left mouse button over the area of the chart in which you are
                                                            								interested. Release the
                                                            								left mouse button when you have the selected area. |
| Reset the chart to the initial default view | Perform one of the following actions: Select Reset View . Right-mouse
                                                            								select the chart and select Reset . |

| If you want to: | Action |
|---|---|
| Zoom in on an area in the chart | Select and
                                                            								drag the left mouse button over the area of the chart in which you are
                                                            								interested. Release the
                                                            								left mouse button when you have the selected area. |
| Reset the chart to the initial default view | Perform one of the following actions: Select Reset View . Right-mouse
                                                            								select the chart and select Reset . |

| Note | The method for accessing Performance may vary depending on the
                                             					 version of windows you install on your computer. |
|---|---|

| Step 1 | Select Start > Settings > Control
                                                				  Panel > Administrative
                                                				  Tools > Performance . |
|---|---|
| Step 2 | Perform the following actions in the application window: Select the right mouse button. Select Properties . |
| Step 3 | Select the Source tab in the System Monitor Properties dialog box. |
| Step 4 | Browse to the directory where you downloaded the perfmon log file
                                          			 and select the perfmon csv file. The log file includes the following naming
                                          			 convention:
                                          			 PerfMon_<node>_<month>_<day>_<year>_<hour>_<minute>.csv;
                                          			 for example, PerfMon_172.19.240.80_06_15_2005_11_25.csv. |
| Step 5 | Select Apply . |
| Step 6 | Select Time Range . To specify the time range in the
                                          			 perfmon log file that you want to view, drag the bar to the appropriate
                                          			 starting and ending times. |
| Step 7 | To open the Add Counters dialog box, select the Data tab and
                                          			 select Add . |
| Step 8 | Select the perfmon object from the Performance Object drop-down list box. If
                                          			 an object has multiple instances, you may select All instances or select only the instances
                                          			 that you are interested in viewing. |
| Step 9 | You can select All Counters or select only the counters that
                                          			 you are interested in viewing. |
| Step 10 | Select Add to add the selected counters. |
| Step 11 | Select Close when you finish selecting counters . |

| Note | Cisco Unity Connection counters are not logged to the troubleshooting perfmon data log. |
|---|---|

| Step 1 | Select System > Service
                                                				  Parameters the administration interface. |
|---|---|
| Step 2 | Select the
                                          			 server from the Server list box. |
| Step 3 | Select the
                                          			 Cisco RIS Data Collector from the Service drop-down list box. |
| Step 4 | Enter the
                                          			 appropriate settings as described in the following table. Table 2. Troubleshooting Perfmon Data-Logging Parameters Field Description Enable Logging From the drop-down list box, select True to enable or False to disable troubleshooting perfmon data
                                                         						  logging. The default value specifies False. Polling Rate Enter the polling rate interval (in seconds). You can enter a
                                                         						  value from 5 (minimum) to 300 (maximum). The default value specifies 15. Maximum No. of Files Enter the maximum number of Troubleshooting Perfmon Data Logging
                                                         						  files that you want to store on disk. You can enter a value from 1 (minimum) up
                                                         						  to 100 (maximum). The default value specifies 50. Consider your storage capacity in configuring the Maximum No. of
                                                         						  Files and Maximum File Size Parameters. We recommend that you do not exceed a
                                                         						  value of 100 MB when you multiply the Maximum Number of Files value by the
                                                         						  Maximum File Size value. When the number of files exceeds the maximum number of files
                                                         						  that you specified in this field, the system deletes log files with the oldest
                                                         						  time stamp. Caution If
                                                                     							 you do not save the log files on another computer before you change this
                                                                     							 parameter, you risk losing the log files. Maximum File Size (MB) Enter the maximum file size (in megabytes) that you want to
                                                         						  store in a perfmon log file before a new file is started. You can enter a value
                                                         						  from 1 (minimum) to 500 (maximum). The default value specifies 2 MB. Consider your storage capacity in configuring the Maximum No. of
                                                         						  Files and Maximum File Size Parameters. We recommend that you do not exceed a
                                                         						  value of 100 MB when you multiply the Maximum Number of Files value by the
                                                         						  Maximum File Size value. | Field | Description | Enable Logging | From the drop-down list box, select True to enable or False to disable troubleshooting perfmon data
                                                         						  logging. The default value specifies False. | Polling Rate | Enter the polling rate interval (in seconds). You can enter a
                                                         						  value from 5 (minimum) to 300 (maximum). The default value specifies 15. | Maximum No. of Files | Enter the maximum number of Troubleshooting Perfmon Data Logging
                                                         						  files that you want to store on disk. You can enter a value from 1 (minimum) up
                                                         						  to 100 (maximum). The default value specifies 50. Consider your storage capacity in configuring the Maximum No. of
                                                         						  Files and Maximum File Size Parameters. We recommend that you do not exceed a
                                                         						  value of 100 MB when you multiply the Maximum Number of Files value by the
                                                         						  Maximum File Size value. When the number of files exceeds the maximum number of files
                                                         						  that you specified in this field, the system deletes log files with the oldest
                                                         						  time stamp. Caution If
                                                                     							 you do not save the log files on another computer before you change this
                                                                     							 parameter, you risk losing the log files. | Caution | If
                                                                     							 you do not save the log files on another computer before you change this
                                                                     							 parameter, you risk losing the log files. | Maximum File Size (MB) | Enter the maximum file size (in megabytes) that you want to
                                                         						  store in a perfmon log file before a new file is started. You can enter a value
                                                         						  from 1 (minimum) to 500 (maximum). The default value specifies 2 MB. Consider your storage capacity in configuring the Maximum No. of
                                                         						  Files and Maximum File Size Parameters. We recommend that you do not exceed a
                                                         						  value of 100 MB when you multiply the Maximum Number of Files value by the
                                                         						  Maximum File Size value. |
| Field | Description |
| Enable Logging | From the drop-down list box, select True to enable or False to disable troubleshooting perfmon data
                                                         						  logging. The default value specifies False. |
| Polling Rate | Enter the polling rate interval (in seconds). You can enter a
                                                         						  value from 5 (minimum) to 300 (maximum). The default value specifies 15. |
| Maximum No. of Files | Enter the maximum number of Troubleshooting Perfmon Data Logging
                                                         						  files that you want to store on disk. You can enter a value from 1 (minimum) up
                                                         						  to 100 (maximum). The default value specifies 50. Consider your storage capacity in configuring the Maximum No. of
                                                         						  Files and Maximum File Size Parameters. We recommend that you do not exceed a
                                                         						  value of 100 MB when you multiply the Maximum Number of Files value by the
                                                         						  Maximum File Size value. When the number of files exceeds the maximum number of files
                                                         						  that you specified in this field, the system deletes log files with the oldest
                                                         						  time stamp. Caution If
                                                                     							 you do not save the log files on another computer before you change this
                                                                     							 parameter, you risk losing the log files. | Caution | If
                                                                     							 you do not save the log files on another computer before you change this
                                                                     							 parameter, you risk losing the log files. |
| Caution | If
                                                                     							 you do not save the log files on another computer before you change this
                                                                     							 parameter, you risk losing the log files. |
| Maximum File Size (MB) | Enter the maximum file size (in megabytes) that you want to
                                                         						  store in a perfmon log file before a new file is started. You can enter a value
                                                         						  from 1 (minimum) to 500 (maximum). The default value specifies 2 MB. Consider your storage capacity in configuring the Maximum No. of
                                                         						  Files and Maximum File Size Parameters. We recommend that you do not exceed a
                                                         						  value of 100 MB when you multiply the Maximum Number of Files value by the
                                                         						  Maximum File Size value. |
| Step 5 | Select Save . Note You
                                                         				  can collect the log files for Cisco RIS Data Collector service on the server by
                                                         				  using RTMT to download the log files. If you want to download the log files by
                                                         				  using the CLI, refer to Cisco
                                                            					 Unified Communications Operating System Administration Guide . After you
                                                         				  collect the log files, you can view the log file by using the Performance Log
                                                         				  Viewer in RTMT or by using the Microsoft Windows performance tool. | Note | You
                                                         				  can collect the log files for Cisco RIS Data Collector service on the server by
                                                         				  using RTMT to download the log files. If you want to download the log files by
                                                         				  using the CLI, refer to Cisco
                                                            					 Unified Communications Operating System Administration Guide . After you
                                                         				  collect the log files, you can view the log file by using the Performance Log
                                                         				  Viewer in RTMT or by using the Microsoft Windows performance tool. |
| Note | You
                                                         				  can collect the log files for Cisco RIS Data Collector service on the server by
                                                         				  using RTMT to download the log files. If you want to download the log files by
                                                         				  using the CLI, refer to Cisco
                                                            					 Unified Communications Operating System Administration Guide . After you
                                                         				  collect the log files, you can view the log file by using the Performance Log
                                                         				  Viewer in RTMT or by using the Microsoft Windows performance tool. |

| Field | Description |
|---|---|
| Enable Logging | From the drop-down list box, select True to enable or False to disable troubleshooting perfmon data
                                                         						  logging. The default value specifies False. |
| Polling Rate | Enter the polling rate interval (in seconds). You can enter a
                                                         						  value from 5 (minimum) to 300 (maximum). The default value specifies 15. |
| Maximum No. of Files | Enter the maximum number of Troubleshooting Perfmon Data Logging
                                                         						  files that you want to store on disk. You can enter a value from 1 (minimum) up
                                                         						  to 100 (maximum). The default value specifies 50. Consider your storage capacity in configuring the Maximum No. of
                                                         						  Files and Maximum File Size Parameters. We recommend that you do not exceed a
                                                         						  value of 100 MB when you multiply the Maximum Number of Files value by the
                                                         						  Maximum File Size value. When the number of files exceeds the maximum number of files
                                                         						  that you specified in this field, the system deletes log files with the oldest
                                                         						  time stamp. Caution If
                                                                     							 you do not save the log files on another computer before you change this
                                                                     							 parameter, you risk losing the log files. | Caution | If
                                                                     							 you do not save the log files on another computer before you change this
                                                                     							 parameter, you risk losing the log files. |
| Caution | If
                                                                     							 you do not save the log files on another computer before you change this
                                                                     							 parameter, you risk losing the log files. |
| Maximum File Size (MB) | Enter the maximum file size (in megabytes) that you want to
                                                         						  store in a perfmon log file before a new file is started. You can enter a value
                                                         						  from 1 (minimum) to 500 (maximum). The default value specifies 2 MB. Consider your storage capacity in configuring the Maximum No. of
                                                         						  Files and Maximum File Size Parameters. We recommend that you do not exceed a
                                                         						  value of 100 MB when you multiply the Maximum Number of Files value by the
                                                         						  Maximum File Size value. |

| Caution | If
                                                                     							 you do not save the log files on another computer before you change this
                                                                     							 parameter, you risk losing the log files. |
|---|---|

| Note | You
                                                         				  can collect the log files for Cisco RIS Data Collector service on the server by
                                                         				  using RTMT to download the log files. If you want to download the log files by
                                                         				  using the CLI, refer to Cisco
                                                            					 Unified Communications Operating System Administration Guide . After you
                                                         				  collect the log files, you can view the log file by using the Performance Log
                                                         				  Viewer in RTMT or by using the Microsoft Windows performance tool. |
|---|---|