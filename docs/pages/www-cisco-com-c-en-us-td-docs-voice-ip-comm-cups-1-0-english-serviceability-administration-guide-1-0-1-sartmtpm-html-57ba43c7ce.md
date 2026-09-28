---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-english-serviceability-administration-guide-1-0-1-sartmtpm-html-57ba43c7ce
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0/english/serviceability/administration/guide/1_0_1/sartmtpm.html
retrieved_at: 2026-08-21T16:07:44.594509+00:00
---

Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(1)

# Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(1)

Updated: July 17, 2006

Chapter: Configuring and Using Performance Monitoring

## Chapter: Configuring and Using Performance Monitoring

## Configuring and Using Performance Monitoring

You can monitor the performance of Cisco Unified Presence Server by choosing the counters for any object by using RTMT. The counters for each object display when the folder expands.

You can log perfmon counters locally on the computer and use the performance log viewer in RTMT to display the perfmon CSV log files that you collected or the Alert Manager and Collector (AMC) perfmon logs and Realtime Information Server Data Collection (RISDC) perfmon logs.

You can also enable troubleshooting perfmon data logging to automatically collect statistics from a set of perfmon counters that will provide comprehensive information on the system state. Be aware that enabling troubleshooting perfmon data logging may impact system performance on the server.

This chapter contains information on the following topics:

• Displaying Performance Counters

• Removing a Counter from the RTMT Performance Monitoring Pane

• Adding a Counter Instance

• Configuring Alert Notification for a Counter

• Zooming a Counter

• Displaying a Counter Description

• Configuring a Data Sample

• Viewing Counter Data

• Local Logging of Data from Perfmon Counters

• Displaying Log Files on the Perfmon Log Viewer

## Displaying Performance Counters

RTMT displays perfmon counters in chart or table format. The chart format, as shown in Figure 9-1 , displays the perfmon counter information by using line charts. For each category tab that you create, you can display up to six charts in the RTMT Perfmon Monitoring pane with up to three counters in one chart.

Tip You can display up to three counters in one chart in the RTMT Perfmon Monitoring pane. To add another counter in a chart, click the counter and drag it to the RTMT Perfmon Monitoring pane. Repeat again to add up to three counters.

Figure 9-1

Performance Counters In a Chart Format

By default, RTMT displays perfmon counters in a chart format. You can also choose to display the perfmon counters in a table format, as shown in Figure 9-2 . To display the perfmon counters in table format, you need to check the Present Data in Table View check box when you create a new category.

Figure 9-2 Performance Counters in a Table Format

You can organize the perfmon counters to display a set of feature-based counters and save it in a category. After you save your RTMT profile, you can quickly access the counters that you are interested in. After you create a category, you cannot change the display from a chart format to a table format, or vice versa.

Step 1 Perform one of the following tasks:

• In the Quick Launch Channel, click Performance ; then, click the Perfmon Monitoring icon.

• Choose Performance > Open Performance Monitoring .

Step 2 Click the name of the server where you want to add a counter to monitor.

The tree hierarchy expands and displays all the perfmon objects for the node.

Step 3 To monitor a counter in table format, see Step 4 . To monitor a counter in chart format, see Step 5 .

Step 4 To monitor a counter in table format, perform the following procedure.

a. Choose Edit > New Category .

b. In the Enter Name field, enter a name for the tab.

c. To display the perfmon counters in table format, check the Present Data in Table View check box.

d. Click OK .

A new tab with the name that you entered displays at the bottom of the pane.

e. Click the file icon next to the object name that lists the counters that you want to monitor.

Tip To display the counter in chart format after you display it in table format, right-click the category tab and choose Remove Category . The counter displays in chart format.

Step 5 To monitor a counter in chart format, perform the following tasks:

• Click the file icon next to the object name that lists the counters that you want to monitor.

A list of counters displays.

• To display the counter information, either right-click the counter and click Counter Monitoring , double-click the counter, or drag and drop the counter into the RTMT Perfmon Monitoring pane.

The counter chart displays in the RTMT Perfmon Monitoring pane.

Additional Information

See the Choose Performance > Open Performance Log Viewer .

## Removing a Counter from the RTMT Performance Monitoring Pane

You can remove counters from the RTMT Perfmon Monitoring pane when you no longer need them. This section describes how to remove a counter from the pane.

Perform one of the following tasks:

• Right-click the counter that you want to remove and choose Remove .

• Click the counter that you want to remove and choose Perfmon > Remove Chart/Table Entry .

The counter no longer displays in the RTMT Perfmon Monitoring pane.

Additional Information

See the Choose Performance > Open Performance Log Viewer .

## Adding a Counter Instance

To add a counter instance, perform the following procedure:

Step 1 Display the performance monitoring counter, as described in the "Displaying Performance Counters" section .

Step 2 Perform one of the following tasks:

• Double-click the performance monitoring counter in the performance monitoring tree hierarchy.

• Click the performance monitoring counter in the performance monitoring tree hierarchy and choose Performance > Counter Instances .

• Right-click the performance monitoring counter in the performance monitoring tree hierarchy and choose Counter Instances .

Step 3 In the Select Instance window, click the instance; then, click Add .

The counter displays.

Additional Information

See the Choose Performance > Open Performance Log Viewer .

## Configuring Alert Notification for a Counter

The following procedure describes how to configure alert notification for a counter.

Tip To remove the alert for the counter, right-click the counter and choose Remove Alert. The option appears gray after you remove the alert.

Step 1 Display the performance counter, as described in the "Displaying Performance Counters" section .

Step 2 From the counter chart or table, right-click the counter for which you want to configure the alert notification, and choose Alert/Threshold .

Step 3 Check the Enable Alert check box.

Step 4 In the Severity drop-down list box, choose the severity level at which you want to be notified.

Step 5 In the Description pane, enter a description of the alert.

Step 6 Click Next .

Step 7 Use Table 9-1 to configure the settings in the Threshold, Value Calculated As, Duration, Frequency, and Schedule panes. After you enter the settings in the window, click Next to proceed to the next panes.

Table 9-1 Counter Alert Configuration Parameters

Trigger alert when following conditions met (Over, Under)

Check the check box and enter the value that applies.

• Over—Check this check box to configure a maximum threshold that must be met before an alert notification is activated. In the Over value field, enter a value. For example, enter a value that equals the number of calls in progress.

• Under—Check this check box to configure a minimum threshold that must be met before an alert notification is activated. In the Under value field, enter a value. For example, enter a value that equals the number of calls in progress.

Absolute, Delta, % Delta

Click the radio button that applies.

• Absolute—Because some counter values are accumulative (for example, CallsAttempted or CallsCompleted), choose Absolute to display the data at its current status.

• Delta—Choose Delta to display the difference between the current counter value and the previous counter value.

• % Delta—Choose % Delta to display the counter performance changes in percentage.

Trigger alert only when value constantly...; Trigger alert immediately

• Trigger alert only when value constantly... — If you want the alert notification only when the value is constantly below or over threshold for a desired number of seconds, click this radio button and enter seconds after which you want the alert to be sent.

• Trigger alert immediately—If you want the alert notification to be sent immediately, click this radio button.

Trigger alert on every poll; trigger up to...

Click the radio button that applies.

• trigger alert on every poll—If you want the alert notification to activate on every poll when the threshold is met, click this radio button.

If the calls in progress continue to go over or under the threshold, the system does not send another alert notification. When the threshold is normal (between 50 and 100 calls in progress), the system deactivates the alert notification; however, if the threshold goes over or under the threshold value again, the system reactivates alert notification.

• trigger up to...—If you want the alert notification to activate at certain intervals, click this radio button and enter the number of alerts that you want sent and the number of minutes within which you want them sent.

24-hours daily; start/stop

Click the radio button that applies:

• 24-hours daily—If you want the alert to be triggered 24 hours a day, click this radio button.

• start/stop—If you want the alert notification activated within a specific time frame, click the radio button and enter a start time and a stop time. If the check box is checked, enter the start and stop times of the daily task. For example, you can configure the counter to be checked every day from 9:00 am to 5:00 pm or from 9:00 pm to 9:00 am.

Step 8 If you want the system to send an e-mail message for the alert, check the Enable Email check box.

Step 9 If you want to trigger an alert action that is already configured, choose the alert action that you want from the Trigger Alert Action drop-down list box.

Step 10 If you want to configure a new alert action for the alert, click Configure .

Note Whenever the specified alert is triggered, the system sends the alert action.

The Alert Action dialog box displays.

Step 11 To add a new alert action, click Add .

The Action Configuration dialog box displays.

Step 12 In the Name field, enter a name for the alert action.

Step 13 In the Description field, enter a description for the alert action.

Step 14 To add a new e-mail recipient for the alert action, click Add .

The Input dialog box displays.

Step 15 Enter either the e-mail or e-page address of the recipient that you want to receive the alert action notification.

Step 16 Click OK .

The recipient address displays in the Recipient list. The Enable check box gets checked.

Tip To disable the recipient address, uncheck the Enable check box. To delete a recipient address from the Recipient list, highlight the address and click Delete .

Step 17 Click OK .

Step 18 The alert action that you added displays in Action List.

Tip To delete an alert action from the action list, highlight the alert action and click Delete . You can also edit an existing alert action by clicking Edit .

Step 19 Click Close .

Step 20 In the User-defined email text box, enter the text that you want to display in the e-mail message.

Step 21 Click Activate .

Additional Information

See the Choose Performance > Open Performance Log Viewer .

## Zooming a Counter

To get a closer look at perfmon counters, you can zoom the perfmon monitor counter in the RTMT Perfmon Monitoring pane.

Step 1 Perform one of the following tasks:

• In the RTMT Performance Monitoring pane, double-click the counter that you want to zoom. The box with the counter appears highlighted, and the Zoom window automatically displays.

• In the RTMT Performance Monitoring pane, click the counter that you want to zoom. The box with the counter appears highlighted. Choose Perfmon > Zoom Chart . The Zoom window automatically displays.

The minimum, maximum, average, and last fields show the values for the counter since the monitoring began for the counter.

Step 2 To close the window, click OK .

Additional Information

See the Choose Performance > Open Performance Log Viewer .

## Displaying a Counter Description

Use one of two methods to obtain a description of the counter:

Step 1 Perform one of the following tasks:

• In the Perfmon tree hierarchy, right-click the counter for which you want property information and choose Counter Description .

• In the RTMT Performance Monitoring pane, click the counter and choose Perfmon > Counter Description .

Tip To display the counter description and to configure data-sampling parameters, see the "Configuring a Data Sample" section .

The Counter Property window displays the description of the counter. The description includes the host address, the object to which the counter belongs, the counter name, and a brief overview of what the counter does.

Step 2 To close the Counter Property window, click OK .

Additional Information

See the Choose Performance > Open Performance Log Viewer .

## Configuring a Data Sample

The Counter Property window contains the option to configure data samples for a counter. The perfmon counters that display in the RTMT Perfmon Monitoring pane contain green dots that represent samples of data over time. You can configure the number of data samples to collect and the number of data points to show in the chart. After the data sample is configured, view the information by using the View All Data/View Current Data menu option. See the "Viewing Counter Data" section .

This section describes how to configure the number of data samples to collect for a counter.

Step 1 Display the counter, as described in the "Displaying Performance Counters" section .

Step 2 Perform one of the following tasks:

• Right-click the counter for which you want data sample information and choose Monitoring Properties if you are using chart format and Properties if you are using table format.

• Click the counter for which you want data sample information and choose Perfmon > Monitoring Properties .

The Counter Property window displays the description of the counter, as well as the tab for configuring data samples. The description includes the host address, the object to which the counter belongs, the counter name, and a brief overview of what the counter does.

Step 3 To configure the number of data samples for the counter, click the Data Sample tab.

Step 4 From the No. of data samples drop-down list box, choose the number of samples (between 100 and 1000). The default specifies 100.

Step 5 From the No. of data points shown on chart drop-down list box, choose the number of data points to display on the chart (between 10 and 50). The default specifies 20.

Step 6 Click one parameter, as described in Table 9-2 .

Table 9-2 Data Sample Parameters

Absolute

Because some counter values are accumulative (for example, CallsAttempted or CallsCompleted), choose Absolute to display the data at its current status.

Delta

Choose Delta to display the difference between the current counter value and the previous counter value.

% Delta

Choose % Delta to display the counter performance changes in percentage.

Step 7 To close the Counter Property window and return to the RTMT Perfmon Monitoring pane, click the OK button.

Additional Information

See the Choose Performance > Open Performance Log Viewer .

## Viewing Counter Data

Perform the following procedure to view the data that is collected for a performance counter.

Step 1 In the RTMT Perfmon Monitoring pane, right-click the counter chart for the counter for which you want to view data samples and choose View All Data .

The counter chart displays all data that has been sampled. The green dots display close together, almost forming a solid line.

Step 2 Right-click the counter that currently displays and choose View Current .

The counter chart displays the last configured data samples that were collected. See the "Configuring a Data Sample" section procedure for configuring data samples.

Additional Information

See the Choose Performance > Open Performance Log Viewer .

## Local Logging of Data from Perfmon Counters

RTMT allows you to choose different perfmon counters to log locally. You can then view the data from the perfmon CSV log by using the performance log viewer. See "Displaying Log Files on the Perfmon Log Viewer" section .

### Starting the Counter Logs

To start logging perfmon counter data into a CSV log file, perform the following procedure:

Step 1 Display the performance monitoring counters, as described in the "Displaying Performance Counters" section .

Step 2 If you are displaying perfmon counters in the chart format, right-click the graph for which you want data sample information and choose Start Counter(s) Logging . If you want to log all counters in a screen (both chart and table view format), you can right-click the category name tab at the bottom of the window and choose Start Counter(s) Logging.

The Counter Logging Configuration dialog box displays.

Step 3 In the Logger File Name field, enter a file name and choose OK.

RTMT saves the CSV log files in the log folder in the .jrtmt directory under the user home directory. For example, in Windows, the path specifies D:\Documents and Settings\userA\.jrtmt\log, or in Linux, the path specifies /users/home/.jrtmt/log.

To limit the number and size of the files, specify the maximum file size and maximum number of files parameter in the trace output settings. See "Configuring Trace Parameters" section .

### Stopping the Counter Logs

To stop logging perfmon counter data, perform the following procedure:

Step 1 Display the performance monitoring counters, as described in the "Displaying Performance Counters" section .

Step 2 If you are displaying perfmon counters in the chart format, right-click the graph for which counter logging is started and choose Stop Counter(s) Logging. If you want to stop logging of all counters in a screen (both chart and table view format), you can right-click the category name tab at the bottom of the window and choose Stop Counter(s) Logging .

## Displaying Log Files on the Perfmon Log Viewer

The Performance Log Viewer displays data for counters from perfmon CSV log files in a graphical format. You can use the performance log viewer to display data from the local perfmon logs that you collected, or you can display the data from the Alert Manager and Collector (AMC) perfmon logs and Realtime Information Server Data Collection (RISDC) perfmon logs.

The local perfmon logs consist of data from counters that you choose and store locally on your computer. For more information on how to choose the counters and how to start and stop local logging, see "Local Logging of Data from Perfmon Counters" section .

When you enable AMC and RISDC perfmon logs, Cisco Unified Presence Server collects information for the system in logs that are written on the Cisco Unified Presence Server server. You can enable or disable AMC and RISDC perfmon logs on Cisco Unified Presence Server Administration by choosing System > Service Management . By default, AMC perfmon logging is enabled and RISDC perfmon logging is disabled. RISDC perfmon logging is also known as Troubleshooting Perfmon Data logging. When you enable RISDC perfmon logging, the server collects data that are used to troubleshoot problems. Because Cisco Unified Presence Server collects a large amount of data in a short period of time, you should limit the period of time that RISDC perfmon data logging (troubleshooting perfmon data logging) is enabled.

Step 1 Perform one of the following tasks:

• In the Quick Launch Channel, click Performance ; then, click the Performance Log Viewer .

• Choose Performance > Open Performance Log Viewer

Step 2 Choose the type of perfmon logs that you want to view:

• For AMC or RisDC Perfmon Logs, perform the following steps:

a. Click on either AMC Perfmon Logs or Perfmon Logs and choose a node from the Select a node drop-down box.

b. Click Open .

The File Selection Dialog Box displays.

c. Choose the file and Click Open File .

The Select Counters Dialog Box displays.

d. Choose the counters that you want to display by checking the check box next to the counter.

e. Click OK .

• For locally stored data, perform the following steps:

a. Click Local Perfmon Logs.

b. Click Open .

The File Selection Dialog Box displays. RTMT saves the perfmon CSV log files in the log folder in the .jrtmt directory under the user home directory. In Windows, the path specifies D:\Documents and Settings\userA\.jrtmt\log, or in Linux, the path specifies /users/home/.jrtmt/log.

c. Browse to the file directory.

d. Choose the file that you are interested in viewing or enter the file name in the filename field.

e. Click Open .

The Select Counters Dialog Box displays.

f. Choose the counters that you want to display by checking the check box next to the counter.

g. Click OK .

The performance log viewer displays a chart with the data from the selected counters. The bottom pane displays the selected counters, a color legend for those counters, display option, mean value, minimum value, and the maximum value.

Table 9-3 describes the functions of different buttons that are available on the performance log viewer.

Tip You can order each column by clicking on a column heading. The first time that you click on a column heading, the records display in ascending order. A small triangle pointing up indicates ascending order. If you click the column heading again, the records display in descending order. A small triangle pointing down indicates descending order. If you click the column heading one more time, the records displays in the unsorted state.

Table 9-3 Performance Log Viewer

Select Counters

Allows you to add counters that you want to display in the performance log viewer. To not display a counter, uncheck the Display column next to the counter.

Reset View

Resets the performance log viewer to the initial default view.

Save Downloaded File

Allows you to save the log file to your local computer.

## Zooming In and Out

The performance Log viewer includes a zoom feature that allows you to zoom in on an area in the chart. To, zoom in, click and drag the left button of the mouse until you have the desired area selected.

To reset the chart to the initial default view, click Reset View or right-mouse click the chart and choose Reset .

## Related Topics

• Displaying Performance Counters

• Removing a Counter from the RTMT Performance Monitoring Pane

• Configuring Alert Notification for a Counter

• Zooming a Counter

• Displaying a Counter Description

• Configuring a Data Sample

• Viewing Counter Data

• Local Logging of Data from Perfmon Counters

• Displaying Log Files on the Perfmon Log Viewer

| Setting | Description |
|---|---|
| Threshold Pane |
| Trigger alert when following conditions met (Over, Under) | Check the check box and enter the value that applies. • Over—Check this check box to configure a maximum threshold that must be met before an alert notification is activated. In the Over value field, enter a value. For example, enter a value that equals the number of calls in progress. • Under—Check this check box to configure a minimum threshold that must be met before an alert notification is activated. In the Under value field, enter a value. For example, enter a value that equals the number of calls in progress. Tip Use these check boxes in conjunction with the Frequency and Schedule configuration parameters. |
| Value Calculated As Pane |
| Absolute, Delta, % Delta | Click the radio button that applies. • Absolute—Because some counter values are accumulative (for example, CallsAttempted or CallsCompleted), choose Absolute to display the data at its current status. • Delta—Choose Delta to display the difference between the current counter value and the previous counter value. • % Delta—Choose % Delta to display the counter performance changes in percentage. |
| Duration Pane |
| Trigger alert only when value constantly...; Trigger alert immediately | • Trigger alert only when value constantly... — If you want the alert notification only when the value is constantly below or over threshold for a desired number of seconds, click this radio button and enter seconds after which you want the alert to be sent. • Trigger alert immediately—If you want the alert notification to be sent immediately, click this radio button. |
| Frequency Pane |
| Trigger alert on every poll; trigger up to... | Click the radio button that applies. • trigger alert on every poll—If you want the alert notification to activate on every poll when the threshold is met, click this radio button. If the calls in progress continue to go over or under the threshold, the system does not send another alert notification. When the threshold is normal (between 50 and 100 calls in progress), the system deactivates the alert notification; however, if the threshold goes over or under the threshold value again, the system reactivates alert notification. • trigger up to...—If you want the alert notification to activate at certain intervals, click this radio button and enter the number of alerts that you want sent and the number of minutes within which you want them sent. |
| Schedule Pane |
| 24-hours daily; start/stop | Click the radio button that applies: • 24-hours daily—If you want the alert to be triggered 24 hours a day, click this radio button. • start/stop—If you want the alert notification activated within a specific time frame, click the radio button and enter a start time and a stop time. If the check box is checked, enter the start and stop times of the daily task. For example, you can configure the counter to be checked every day from 9:00 am to 5:00 pm or from 9:00 pm to 9:00 am. |

| Parameter | Description |
|---|---|
| Absolute | Because some counter values are accumulative (for example, CallsAttempted or CallsCompleted), choose Absolute to display the data at its current status. |
| Delta | Choose Delta to display the difference between the current counter value and the previous counter value. |
| % Delta | Choose % Delta to display the counter performance changes in percentage. |

| Button | Function |
|---|---|
| Select Counters | Allows you to add counters that you want to display in the performance log viewer. To not display a counter, uncheck the Display column next to the counter. |
| Reset View | Resets the performance log viewer to the initial default view. |
| Save Downloaded File | Allows you to save the log file to your local computer. |