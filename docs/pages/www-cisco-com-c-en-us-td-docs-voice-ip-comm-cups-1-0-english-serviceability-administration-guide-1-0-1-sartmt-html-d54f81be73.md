---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-english-serviceability-administration-guide-1-0-1-sartmt-html-d54f81be73
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0/english/serviceability/administration/guide/1_0_1/sartmt.html
retrieved_at: 2026-08-21T16:07:36.390870+00:00
---

Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(1)

# Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(1)

Updated: July 17, 2006

Chapter: Real-Time Monitoring Configuration

## Chapter: Real-Time Monitoring Configuration

## Real-Time Monitoring Configuration

This chapter contains the following information for configuring the Cisco Unified Presence Server Real-Time Monitoring Tool (RTMT).

Note Some options available in the current version of the Cisco Real-Time Monitoring Tool do not apply to Cisco Unified Presence Server, Release 1.0(1).

• Installing the Real-Time Monitoring Tool (RTMT)

• Upgrading RTMT

• Uninstalling RTMT

• Using RTMT

• Configuring E-mail Notification

• Working with Configuration Profiles

• Working with Predefined Objects

• Working with Devices

• Where to Find More Information

Tip For information on alert, performance monitoring, trace collection, and syslog viewer configuration, see the "Where to Find More Information" section .

## Installing the Real-Time Monitoring Tool (RTMT)

You can install RTMT, which works for resolutions 800*600 and above, on a Windows 98, Windows XP, Windows 2000, or Red Hat Linux with KDE and/or Gnome client.

Note If you have previously installed RTMT for use with a Cisco Unified CallManager server that is running Microsoft Windows, you must install RTMT for Cisco Unified Presence Server 1.0 in a different folder on your local computer.

To install the tool, perform the following procedure:

Step 1 From Cisco Unified Presence Server Administration, choose Application > Plugins .

Step 2 Click the Find button.

Step 3 Click the Download link for the Cisco Unified Presence Server Real-Time Monitoring Tool.

Step 4 Download the executable to your preferred location.

Step 5 Double-click the RTMT icon that displays on the desktop or locate the directory where you downloaded the file and run the RTMT installation file.

The extraction process begins.

Step 6 In the RTMT welcome window, click Next .

Step 7 To accept the license agreement, click Yes .

Step 8 Choose the location where you want to install RTMT. If you do not want to use the default location, click Browse and navigate to a different location. Click Next .

Step 9 To begin the installation, click Next .

The Setup Status window displays. Do not click Cancel.

Step 10 To complete the installation, click Finish .

Additional Information

See the Related Topics .

## Upgrading RTMT

When you use the tool (RTMT), it saves user preferences and downloaded module jar files locally on the client machine. The system saves profiles in the Cisco Unified Presence Server database, so you can access these items in RTMT after you upgrade the tool.

Tip To ensure compatibility, Cisco recommends that you upgrade RTMT after you complete the Cisco Unified Presence Server upgrade on all servers in the cluster.

To upgrade RTMT, perform the following procedure:

Step 1 From Cisco Unified Presence Server Administration, choose Application > Plugins .

Step 2 Click the Find button.

Step 3 If you are planning to install the RTMT tool on a computer that is running the Microsoft Windows operating system, click the Download link for the Cisco Unified CallManager Real-Time Monitoring Tool-Windows. If you are planning to install the RTMT tool on a computer that is running the Linux operating system, click the Download link for the Cisco Unified CallManager Real-Time Monitoring Tool-Linux.

Step 4 Download the executable to your preferred location.

Step 5 Double-click the RTMT icon that displays on the desktop or locate the directory where you downloaded the file and run the RTMT installation file.

The extraction process begins.

Step 6 In the RTMT welcome window, click Next .

Step 7 Because you cannot change the installation location for upgrades, click Next .

The Setup Status window displays; do not click Cancel.

Step 8 In the Maintenance Complete window, click Finish .

Additional Information

See the Related Topics .

## Uninstalling RTMT

On a Windows client, you uninstall RTMT through Add/Remove Programs under the Control Panel. (Start > Settings > Control Panel >Add/Remove Programs)

To uninstall RTMT on a Red Hat Linux with KDE and/or Gnome client, choose Start > Accessories > Uninstall Real-time Monitoring tool from the task bar.

Additional Information

See the Related Topics .

## Using RTMT

Before You Begin

Before you can use RTMT, you must activate the Cisco AMC Service on each node in the cluster. From Cisco Unified Presence Server Serviceability, choose Tools > Service Activation and check the Cisco AMC Service check box. Click Update .

Step 1 After you install the plug-in, perform one of the following tasks:

• From your Windows desktop, double-click the Cisco Unified CallManager Real-Time Monitoring Tool icon.

• Choose Start > Programs > Cisco CallManager Serviceability > Real-Time Monitoring Tool > Real-Time Monitoring Tool .

The Real-Time Monitoring Tool Login window displays.

Step 2 In the Host IP Address field, enter either the IP address or host name of the first node.

Step 3 In the User Name field, enter the CCMAdministrator application user username; for example, the default username for this user equals CCMAdministrator .

Step 4 In the Password field, enter the CCMAdministrator application user password that you established for the username.

Note If the authentication fails or if the server is unreachable, the tool prompts you to reenter the server and authentication details, or you can click the Cancel button to exit the application. After the authentication succeeds, RTMT launches the monitoring module from local cache or from a remote node, when the local cache does not contain a monitoring module that matches the backend Cisco Unified Presence Server version.

Step 5 Enter the port that the application will use to listen to the server. The default setting equals 8443.

Step 6 Check the Secure Connection check box.

Step 7 Click OK .

Step 8 Add the certificate store by clicking Yes .

Step 9 See the following list for tasks that you can perform in RTMT:

• To configure the mail server for e-mail alerts, see the "Configuring E-mail Notification" section .

• To create configuration profiles, see the "Adding Configuration Profiles" section .

• To monitor predefined objects, see the "Working with Predefined Objects" section .

• To work with devices, see the "Working with Devices" section .

• To work with Alerts, see the "Alert Configuration in RTMT" section on page 8-1 .

• To work with performance monitoring objects, see the "Configuring and Using Performance Monitoring" section on page 9-1 .

• To collect and view traces, see the "Trace Collection and Log Central in RTMT" section on page 10-1 .

• To use SysLog Viewer, see the "Using SysLog Viewer in RTMT" section on page 11-1 .

• To configure the trace setting for RTMT, choose Edit > Trace Setting . Click the radio button that applies.

• To hide the Quick Launch Channel, which is the pane that displays on the left side of the window, choose Edit > Hide Quick Launch Channel .

To display the Quick Launch Channel after it is hidden, choose Edit > Hide Quick Launch Channel .

• To close a monitoring window, choose Window > Close . To close all monitoring windows that display, choose Window > Close All Windows .

• To access Cisco Unified Presence Server Administration or Cisco Unified Presence Server Serviceability from the RTMT window, choose Application > CCMAdmin webpage (or CCM Serviceability webpage ).

• To access the Serviceability Report Archive option from RTMT, choose System > Report Archive . If the Security Alert window displays, click Yes . Enter the administrative user name and password for the server; then, click OK .

• To determine the RTMT version that is installed, choose Help > About . The version information displays in the window. After you view the information, click OK .

• To access documentation for RTMT, choose Help > Help Topics (or For this Window ). For additional information on RTMT or Cisco Unified Presence Server Serviceability, refer to the Cisco Unified CallManager Serviceability System Guide and the Cisco Unified Presence Server Serviceability Administration Guide .

• To monitor JVM information, click System > JVM Information . The JAVA heap memory usage displays in the window. Click OK .

• To log out of RTMT, choose System > Log Off . Performing this task logs off the current user, and the Real-Time Monitoring Tool Login window displays.

• To exit the application, choose System > Exit . Performing this task closes the application.

Additional Information

See the Related Topics .

## Configuring E-mail Notification

To configure e-mail notification, perform the following procedure:

Step 1 In the Mail Server field, enter the e-mail recipient information.

Step 2 In the Port field, enter the port number of the mail server.

Step 3 Click OK .

Additional Information

See the Related Topics .

## Working with Configuration Profiles

This section provides information on the following topics:

• Using the Default Configuration Profile

• Adding Configuration Profiles

• Restoring Profiles

• Deleting Configuration Profiles

### Using the Default Configuration Profile

When you initially load RTMT, the system includes a default profile that is called CM-Default. The first time that you use RTMT, it will use the CM-Default profile and display the summary page in the monitor pane. CM-Default monitors all registered phones dynamically in all the Cisco Unified Presence Server nodes. If your cluster includes five Cisco Unified Presence Server-configured nodes, CM-Default displays all registered phones for each node in a Cisco Unified Presence Server cluster, as well as calls in progress and active gateway ports and channels.

See the "Adding Configuration Profiles" section for information on how to create your own configuration profile.

Additional Information

See the Related Topics .

### Adding Configuration Profiles

After you open multiple monitoring windows in RTMT (such as CPU & Memory, and performance counters), you can create your own configuration profiles so that you can restore these monitoring windows in a single step rather than opening each window again. You can switch between different profiles during the same RTMT session or use the configuration profile in subsequent RTMT sessions.

The following procedure describes how to create a profile.

Step 1 Choose System > Profile .

The Preferences dialog box displays.

Step 2 Click Save .

The Save Current Configuration dialog box displays.

Step 3 In the Configuration name field, enter a name for this particular configuration profile.

Step 4 In the Configuration description field, enter a description of this particular configuration profile.

Note You can enter whatever you want for the configuration profile name and description.

The system creates the new configuration profile.

Additional Information

See the Related Topics .

### Restoring Profiles

Perform the following procedure to restore a profile that you configured:

Step 1 Choose System > Profile .

The Preferences dialog box displays.

Step 2 Click the profile that you want to restore.

Step 3 Click Restore .

All windows with precanned settings and/or performance monitoring counters for the restored configuration open.

Additional Information

See the Related Topics .

### Deleting Configuration Profiles

Perform the following procedure to delete a profile that you configured:

Step 1 Choose System > Profile .

The Preferences dialog box displays.

Step 2 Click the profile that you want to delete.

Step 3 Click Delete .

Step 4 Click Close .

Additional Information

See the Related Topics .

## Working with Predefined Objects

The tool (RTMT) provides a set of default monitoring objects that monitor the health of the system. Default objects include performance counters or critical event status for services that are supported with Cisco Unified Presence Server.

This section provides information on the following topics:

• Viewing/Monitoring a Predefined Object

• Working with Devices

## Viewing/Monitoring a Predefined Object

The monitoring pane for a category, that is, a predefined object, displays the activities of predefined monitoring objects. The following procedure describes how to view information for a category.

Step 1 To view or monitor a category, perform one of the following tasks:

• In the Quick Launch Channel, click the View tab. Then, click a category; for example, Summary, Server, Call Process, and so on. If an icon displays for the category, click the icon to display the information that you want to monitor.

• Depending on which category you want to display, choose one of the following options from Table 7-1 :

Table 7-1 Menu Path for Categories

Summary

Monitor > Summary

Displays memory usage, CPU usage, registered phones, calls in progress, and active gateway ports and channels

Server

Monitor > Server > CPU Usage and Memory (or Process, Disk Usage, or Critical Services)

• CPU Usage and Memory—Displays memory and CPU usage

• Process—Displays the process name, process ID (PID) and percentage of CPU and memory that is used by the process, the resident and shared memory, and the Nice (level)

• Disk Usage—Displays the percentage of disk usage per the largest partition in each host

• Critical Services—Displays the services for a specific server

Call Process

Monitor > Call Process > Call Activity (or Gateway Activity, Trunk Activity, or SIP Activity)

• Call Activity—Displays the call activity for each Cisco Unified Presence Server server in the cluster, including calls completed, calls attempted, and calls in progress

• Gateway Activity—Displays gateway activity for the Cisco Unified Presence Server cluster, including active ports, ports in service, and calls completed

• Trunk Activity—Displays the trunk activity for the Cisco Unified Presence Server cluster, including calls in progress and calls completed

• SIP Activity—Displays SIP activity for each Cisco Unified Presence Server server in the cluster, including summary requests, summary responses, summary of failure responses in, summary of failure responses out, retry requests out, and retry responses out.

Service

Monitor > Service > Cisco TFTP (or Heartbeat or Database Summary)

• Cisco TFTP—Displays Cisco TFTP status for each Cisco Unified Presence Server server in the cluster, including total TFTP requests, total TFTP requests found, and total TFTP requests aborted

• Heartbeat—Displays heartbeat information for the Cisco Unified Presence Server, Cisco TFTP, and the Cisco Presence Server Attendant Console service

• Database Summary—Displays summary information for the database on the Cisco Unified Presence Server server, including connection requests that are queued in the database, connection requests that are queued in memory, total number of clients connected, and the number of device resets that are in the queue.

Device

Monitor > Device Summary (or Phone Summary)

Device Summary displays information for each Cisco Unified Presence Server server in the cluster, including the number of registered phone devices, registered gateway devices, and registered media resource devices.

Device Search displays cluster name and device types in tree hierarchy and allows you to query for information on phones and devices.

Phone Summary displays information for each Cisco Unified Presence Server server in the cluster, including the number of registered phones, registered SIP phones, registered SCCP phones, partially registered phones, and the number of failed registration attempts.

Performance

Performance > Open Performance

Displays perfmon counters.

For more information on using perfmon counters, see the "Configuring and Using Performance Monitoring" section on page 9-1 .

Step 2 Some categories allow you to choose a specific server or device type to monitor. To choose a specific server or device type to monitor, perform one of the following tasks in the panes that are listed:

• CPU and Memory Usage pane—To monitor CPU and memory usage for specific server, choose the server from the Host drop-down list box.

• Disk Usage pane—To monitor disk usage for a specific server, choose the server from the Disk Usage at Host drop-down list box.

• Critical Services pane—To monitor critical services for a specific server, choose the server from the Critical Services at Host drop-down list box.

• Gateway Activity pane—To monitor the gateway activity for a specific gateway type, choose the gateway type from the Gateway Type drop-down list box.

• Trunk Activity pane—To monitor the trunk activity for a specific trunk type, choose the trunk type from the Trunk Type drop-down list box.

Additional Information

See the Related Topics .

## Working with Devices

This section contains information on the following topics:

• Finding Specific Devices to Monitor

• Viewing Phone Information

• Viewing Device Properties

• Configuring Polling Rate for Devices and Performance Monitoring Counters

### Finding Specific Devices to Monitor

By performing the following procedure, you can monitor data for the following device types:

• Phones

• Gateway Devices

• H.323 Devices

• Voice Mail Devices

• Media Resources

• Hunt List

• SIP Trunk

Step 1 Perform one of the following tasks:

• Choose Search > Device > <device type; for example, Phone, Gateway, Hunt List , and so on>. A device selection window displays where you enter the search criteria. Go to Step 4 .

• In the quick launch channel, click Device ; then, click the Device Search icon.

• Choose Device > Open Device Search .

The Device Search window displays the cluster names and tree hierarchy that lists all device types that you can monitor.

Tip After you display the Device Search pane, you can right-click a device type and choose CCMAdmin to go to Cisco Unified Presence Server Administration.

Step 2 To find all devices in the cluster or to view a complete list of device models from which you can choose, right-click the cluster name and choose Monitor .

Step 3 To monitor a specific device type, right-click or double-click the device type from the tree hierarchy.

Tip If you right-click the device type, you must choose Monitor for the device selection window to display.

Step 4 In the Select device with status window, click the radio button that applies.

Step 5 In the drop-down list box next to the radio button that you clicked, choose Any Presence Server or a specific Cisco Unified Presence Server server for which you want the device information to display.

Tip In the remaining steps, you can choose the < Back , Next > , Finish , or Cancel buttons.

Step 6 Click the Next > button.

Step 7 In the Search by device model pane, click the radio button that applies.

Tip If you chose Device Model , choose the device type for which you want the device information to display.

Step 8 Click Next .

Step 9 In the Search with name pane, click one of the following radio buttons and enter the appropriate information in the corresponding fields, if required.

Step 10 Click Next .

Step 11 In the Monitor following attributes pane, check one or all of the search attributes.

Step 12 Click Finish .

Additional Information

See the Related Topics .

### Viewing Phone Information

You can view information about phones that display in the RTMT device monitoring pane. This section describes how to view phone information.

Step 1 To display the phone in the RTMT device monitoring pane, see the "Finding Specific Devices to Monitor" section .

Step 2 Perform one of the following tasks:

• Right-click the phone for which you want information to display and choose Open .

• Click the phone and choose Device > Open .

Step 3 In the Select Device with Status pane, click the radio button that applies.

Step 4 In the drop-down list box next to the radio button that you clicked, choose Any Presence Server or a specific Cisco Unified Presence Server server for which you want the device information to display.

Step 5 In the Search By Device Model pane, choose the phone protocol that you want to display.

Step 6 Click the Any Model or Device Model radio button. If you click on the Device Model radio button, then you will choose a particular phone model that you want to display.

Step 7 Click Next .

Step 8 In the Search With Name pane, click the radio button that applies and enter the appropriate information in the corresponding fields.

Step 9 In the Monitor following attributes pane, check one or all of the search attributes.

Step 10 Click Finish .

The Device Information window displays. For more information on the device, choose any field that is displayed in the left pane of the window.

Additional Information

See the Related Topics .

### Viewing Device Properties

You can view the properties of devices that display in the RTMT device monitoring pane. This section describes how to view device properties.

Step 1 Display the device in the RTMT device monitoring pane. See the "Finding Specific Devices to Monitor" section .

Step 2 Perform one of the following tasks:

• Right-click the device for which you want property information and choose Properties .

• Click the device for which you want property information and choose Device > Properties .

Step 3 To display the device description information, click the Description tab.

Step 4 To display other device information, click the Other Info tab.

Additional Information

See the Related Topics .

### Configuring Polling Rate for Devices and Performance Monitoring Counters

Cisco Unified Presence Server polls counters, devices, and gateway ports to gather status information. In the RTMT monitoring pane, you configure the polling intervals for the performance monitoring counters and devices.

Note High-frequency polling rate may adversely affect Cisco Unified Presence Server performance. The minimum polling rate for monitoring a performance counter in chart view equals 5 seconds; the minimum rate for monitoring a performance counter in table view equals 1 second. The default value for both equals 10 seconds. The default value for devices equals 10 minutes.

Perform the following procedure to update the polling rate:

Step 1 Display the device or performance monitoring counter in the RTMT monitoring pane.

Step 2 Click the device and choose Edit > Polling Rate .

Step 3 In the Polling Interval pane, specify the time that you want to use.

Step 4 Click OK .

Additional Information

See the Related Topics .

## Working with Categories

Categories allow you to monitor performance monitoring counters and devices. For example, the default category, Presence Server, allows you to monitor 6 performance monitoring counters in graph format. If you want to monitor more counters, you can configure a new category and display the data in table format.

If you perform various searches for devices, for example, for phones, gateways, and so on, you can create a category for each search and save the results in the category.

### Adding a Category

To add a category, perform the following procedure:

Step 1 Display the Performance Monitoring or Devices tree hierarchy.

Step 2 Choose Edit > Add New Category .

Step 3 Enter the name of the category; click OK .

The category tab displays at the bottom of the window.

Additional Information

• See the Related Topics .

### Renaming a Category

To rename a category, perform the following procedure:

Step 1 Perform one of the following tasks:

• Right-click the category tab that you want to rename and choose Rename Category .

• Click the category tab that you want to rename and choose Edit > Rename Category .

Step 2 Enter the new name and click OK .

The renamed category displays at the bottom of the window.

Additional Information

• See the Related Topics .

### Deleting a Category

To delete a category, perform one of the following tasks:

• Right-click the category tab that you want to delete and choose Remove Category .

• Click the category tab that you want to delete and choose Edit > Remove Category .

Additional Information

See the Related Topics .

## Where to Find More Information

• Alert Configuration in RTMT, page 8-1

• Configuring and Using Performance Monitoring, page 9-1

• Trace Collection and Log Central in RTMT, page 10-1

Additional Information

See the Related Topics .

## Related Topics

• Adding a Category

• Renaming a Category

• Deleting a Category

• Configuring and Using Performance Monitoring, page 9-1

• Working with Devices

• Viewing Device Properties

• Finding Specific Devices to Monitor

• Viewing Phone Information

• Configuring Polling Rate for Devices and Performance Monitoring Counters

• Using the Default Configuration Profile

• Restoring Profiles

• Using the Default Configuration Profile

• Deleting Configuration Profiles

• Adding Configuration Profiles

• Working with Configuration Profiles

• Working with Predefined Objects

• Alert Configuration in RTMT, page 8-1

• Configuring and Using Performance Monitoring, page 9-1

• Using SysLog Viewer in RTMT, page 11-1

• Installing the Real-Time Monitoring Tool (RTMT)

• Uninstalling RTMT

• Upgrading RTMT

• Using RTMT

| Category | Menu Path | Data that Displays |
|---|---|---|
| Summary | Monitor > Summary | Displays memory usage, CPU usage, registered phones, calls in progress, and active gateway ports and channels |
| Server | Monitor > Server > CPU Usage and Memory (or Process, Disk Usage, or Critical Services) | • CPU Usage and Memory—Displays memory and CPU usage • Process—Displays the process name, process ID (PID) and percentage of CPU and memory that is used by the process, the resident and shared memory, and the Nice (level) • Disk Usage—Displays the percentage of disk usage per the largest partition in each host • Critical Services—Displays the services for a specific server |
| Call Process | Monitor > Call Process > Call Activity (or Gateway Activity, Trunk Activity, or SIP Activity) | • Call Activity—Displays the call activity for each Cisco Unified Presence Server server in the cluster, including calls completed, calls attempted, and calls in progress • Gateway Activity—Displays gateway activity for the Cisco Unified Presence Server cluster, including active ports, ports in service, and calls completed • Trunk Activity—Displays the trunk activity for the Cisco Unified Presence Server cluster, including calls in progress and calls completed • SIP Activity—Displays SIP activity for each Cisco Unified Presence Server server in the cluster, including summary requests, summary responses, summary of failure responses in, summary of failure responses out, retry requests out, and retry responses out. |
| Service | Monitor > Service > Cisco TFTP (or Heartbeat or Database Summary) | • Cisco TFTP—Displays Cisco TFTP status for each Cisco Unified Presence Server server in the cluster, including total TFTP requests, total TFTP requests found, and total TFTP requests aborted • Heartbeat—Displays heartbeat information for the Cisco Unified Presence Server, Cisco TFTP, and the Cisco Presence Server Attendant Console service • Database Summary—Displays summary information for the database on the Cisco Unified Presence Server server, including connection requests that are queued in the database, connection requests that are queued in memory, total number of clients connected, and the number of device resets that are in the queue. |
| Device | Monitor > Device Summary (or Phone Summary) | Device Summary displays information for each Cisco Unified Presence Server server in the cluster, including the number of registered phone devices, registered gateway devices, and registered media resource devices. Device Search displays cluster name and device types in tree hierarchy and allows you to query for information on phones and devices. Phone Summary displays information for each Cisco Unified Presence Server server in the cluster, including the number of registered phones, registered SIP phones, registered SCCP phones, partially registered phones, and the number of failed registration attempts. Tip Instead of choosing Monitor > Device Summary or Monitor > Phone Summary, you can choose Device > Open Device Search to display the cluster name and device or phone types in the tree hierarchy. Tip To monitor devices, you must perform additional configuration steps, as described in the "Finding Specific Devices to Monitor" section . |
| Performance | Performance > Open Performance | Displays perfmon counters. For more information on using perfmon counters, see the "Configuring and Using Performance Monitoring" section on page 9-1 . |