---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-troubleshooting-html-fc2f741adf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/troubleshooting.html
retrieved_at: 2026-08-21T23:39:59.424455+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 11, 2014

Chapter: Troubleshooting Using the GUI

## Chapter: Troubleshooting Using the GUI

## Running a Network Connectivity Test

You can run a network connectivity test to initiate a connection between Cisco Unified SRST Manager and all the systems that are configured on the system, including the central call agent and branch call agents.

The test may take several minutes to complete. During the test, the status page will refresh automatically. You can either wait for the test to complete or go to other pages and later return to this page to see the test results.

Step 1 Select Troubleshoot > Network Connectivity and Audit .

The system displays the Network Connectivity Test page.

Step 2 To start a network connectivity test, click Start Network Connectivity Test .

When the test is complete, the system displays a message stating that the test is complete and shows the results. See Viewing Results from a Network Connectivity Test . If the connectivity test fails, the system displays a brief indication of the cause of the failure. You can find additional failure diagnostic information in the trace buffer or message log.

Step 3 To cancel the network connectivity test that is currently running, click Cancel Network Connectivity Test .

Step 4 To see the results of previous network connectivity tests, click Click here for results of previously run test . The system displays the results. See Viewing Results from a Network Connectivity Test .

Note Results of previous tests are only available for the current login session.

Step 5 To restart a previous network connectivity test, click Restart Network Connectivity Test .

Related Topics

Back to the Troubleshooting Using the GUI menu page

## Viewing Results from a Network Connectivity Test

After you run a network connectivity test (see Running a Network Connectivity Test ), the system displays the results. If a connectivity test was run previously, you can view the results by selecting Troubleshoot > Network Connectivity and Audit and clicking “Click here for results of previously run test.”

Table 14 Network Connectivity Test Result Parameters

Cluster Name

Name of the central call agent cluster .

Hostname

Hostname of the central call agent to which Cisco Unified SRST Manager system tried to connect.

Result

Result of the network connectivity test. Can be either Success or Failed.

Time (ms)

The amount of time, in milliseconds, that it took to connect.

Details

Any additional details about this network connectivity test.

Hostname

Hostname of the branch call agent to which Cisco Unified SRST Manager tried to connect.

Result

Result of the network connectivity test. Can be either Success or Failed.

Time (ms)

The amount of time, in milliseconds, that it took to connect.

Details

Any additional details about this network connectivity test.

## Configuring Trace Settings

Use this procedure to enable traces, or debug message output, for components in the Cisco Unified SRST Manager system. Components are modules, entities, and activities in the system. You can review the output by selecting Troubleshoot > View > Trace Buffer . See Viewing a Trace Buffer .

Restriction

Enabling too many traces can adversely affect the system performance.

Step 1 Select Troubleshoot > Traces .

The system displays the Traces page, with a hierarchical listing of the system components.

Step 2 To enable a trace on a system component, select the check box next to the name of the component.

Step 3 To expand the listing of components, click the + sign next to the upper-level components.

Step 4 Select the check box next to an upper-level component (a module or entity) to enable the traces for all of the components under that component. Deselect the check box next to an upper-level component to disable the traces for all of the components under that component.

Step 5 Click Apply to save your changes.

Step 6 Click OK in the confirmation window.

Related Topics

Back to the Troubleshooting Using the GUI menu page

## Viewing Tech Support Information

Step 1 Select Troubleshoot > View > Tech Support .

The system displays the Tech Support page and shows a collection of configuration data.

Step 2 To save the tech support information, click Download Tech Support and save the file to a convenient location.

Related Topics

Back to the Troubleshooting Using the GUI menu page

## Viewing a Trace Buffer

You can enable traces, or debug message output, for components in the Cisco Unified SRST Manager system. For details on configuring the trace, see Configuring Trace Settings . Use the following procedure to view the trace output.

Step 1 Select Troubleshoot > View > Trace Buffer .

The system displays the Trace Buffer page and shows the contents of the trace buffer .

Step 2 To save the trace buffer information, click Download Trace Buffer and save the file to a convenient location.

Step 3 To clear the trace buffer information, do the following:

a. Click Clear Trace Buffer .

b. Click OK at the confirmation message.

Related Topics

Back to the Troubleshooting Using the GUI menu page

## Viewing a Log File

Step 1 Select Troubleshoot > View > Log File .

The system displays the Log File page and shows the contents of the log file .

Step 2 To save the log file, click Download Log File Bundle and save the file to a convenient location.

Related Topics

Back to the Troubleshooting Using the GUI menu page

| Parameter | Description |
|---|---|
| Central Call Agents |
| Cluster Name | Name of the central call agent cluster . |
| Hostname | Hostname of the central call agent to which Cisco Unified SRST Manager system tried to connect. |
| Result | Result of the network connectivity test. Can be either Success or Failed. |
| Time (ms) | The amount of time, in milliseconds, that it took to connect. |
| Details | Any additional details about this network connectivity test. |
| Branch Call Agents |
| Hostname | Hostname of the branch call agent to which Cisco Unified SRST Manager tried to connect. |
| Result | Result of the network connectivity test. Can be either Success or Failed. |
| Time (ms) | The amount of time, in milliseconds, that it took to connect. |
| Details | Any additional details about this network connectivity test. |