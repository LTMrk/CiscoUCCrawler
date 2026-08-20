---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-14su2-english-administration-guide-cer0-b-cisco-emergency-responder-admi-f7b5c18eaa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/14su2/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-14su2/cer0_b_cisco-emergency-responder-administration-guide-1401_appendix_010000.html
retrieved_at: 2026-08-20T23:53:12.097154+00:00
---

Cisco Emergency Responder Administration Guide for Release 14 and SUs

# Cisco Emergency Responder Administration Guide for Release 14 and SUs

Updated: January 9, 2025

Chapter: Cisco Emergency Responder Serviceability Web Interface

## Chapter: Cisco Emergency Responder Serviceability Web Interface

# Cisco Emergency Responder Serviceability Web Interface

## Control
                        	 Center

The Control
                              		  Center page appears when you choose Tools > Control
                                 			 Center .

### Authorization
                              		  Requirements

You must
                              		  have serviceability authority to access this page.

### Description

Use the
                              		  Control Center page to view the services running on the server and then start,
                              		  stop, and restart these services. This page displays a list of services
                              		  currently running on the server. Radio buttons in front of each service name
                              		  allows you to select each service to perform the desired action.

The
                              		  following table describes the Control Center page.

Field

Description

Start button

Starts the selected services.

Stop button

Stops the selected services.

Restart button

Restarts the selected services.

Refresh button

Refreshes the list of currently running services on the selected
                                          					 server.

Service Name

Names of the currently running services on the selected server.
                                          					 To select a service, click the radio button next to the service name.

Status

Current status of the selected service.

## Event Viewer

The Event
                              		  Viewer page appears when you choose Tools > Event
                                 			 Viewer .

### Authorization
                              		  Requirements

You must
                              		  have serviceability authority to access this page.

### Description

Use the
                              		  Event Viewer page to view Emergency Responder events for the previous six
                              		  months.

The
                              		  following table describes the Event Viewer page.

Field

Description

Find
                                          					 Events in the month

Select a
                                          					 specific month to view events from the month.

Type drop-down menu

This drop-down menu contains two options: Type and Module. When you choose either Type or Module, the drop-down menu to the
                                                      right changes to display the available Type or Module options.

Allows you to select which type of event you want to view. The
                                          					 available types are:

ALL

INFO

WARN

ERROR

These options are displayed in the drop-down menu to the right of the Type drop-down menu.

Module down menu

This drop-down menu contains two options: Type and Module. When you choose either Type or Module, the drop-down menu to the
                                                      right changes to display the available Type or Module options.

Allows you to select the Emergency Responder module for which you want to view events. When you select Module from the drop-down
                                          menu, the menu to the right changes to show the available modules. The available options are:

All

CER_DATABASE

CER_SYSADMIN

CER_REMOTEUPDATE

CER_TELEPHONY

CER_PHONETRACKINGENGINE

CER_AGGREGATOR

CER_ONSITEALERT

CER_GROUP

CER_CALLENGINE

CER_CLUSTER

CER_PROVIDER

Items Per Page menu

Allows you to select the number of events displayed per page.
                                          					 Options are 10, 20, 30, 40, or 50 events.

Displays search results.

This area
                                                      						of the page is not visible until you perform a search operation.

Type column

Displays the type of event. The Type column displays one of the
                                          					 following:

INFO

WARN

ERROR

Use
                                          					 the Up and Down arrows to perform an ascending or descending sort of the
                                          					 results.

Time column

Displays the time of the event. Use the Up and Down arrows to
                                          					 perform an ascending or descending sort of the results.

Module column

Displays the Emergency Responder module to which the event
                                          					 applies. The modules are:

CER_DATABASE

CER_SYSADMIN

CER_REMOTEUPDATE

CER_TELEPHONY

CER_PHONETRACKINGENGINE

CER_AGGREGATOR

CER_ONSITEALERT

CER_GROUP

CER_CALLENGINE

CER_CLUSTER

CER_PROVIDER

Use the Up and Down arrows to perform an ascending or descending
                                          					 sort of the results.

Message column

Displays the message associated with each event. Use the Up and
                                          					 Down arrows at the right of the text box to scroll through the message.

## Audit Log
                        	 Configuration

The Audit
                              		  Log configuration page appears when you choose Tools > Audit Log
                                    				Configuration .

### Authorization
                              		  Requirements

Only a user with an audit role can change the audit log settings. The administrator can assign users to have auditing privileges
                              in the User Group Configuration window. The Cisco Emergency Responder Audit Administrator assigns privileges to delete audit logs and also to read and update
                              audit configuration in the Cisco Emergency Responder Serviceability interface.

### Description

Use the Audit Log
                              		  Configuration page to configure audit related settings. This page allows you to
                              		  set parameters for Audit level, Remote Syslog, and Local Audit Log
                              		  configuration.

The following
                              		  table describes the Audit Log ER settings.

Field

Description

Audit
                                          					 Level Settings

Audit
                                          					 Event Level

Warning is the default value.

Choose the
                                          					 required severity level for the audit event from the drop-down list.

If you,
                                          					 choose Debug all the syslog messages including Info , Error , and Warning are sent to the remote syslog server and
                                          					 stored locally in audit log file if the local audit logging is enabled.

Remote
                                          					 SysLog Settings

Remote
                                          					 Syslog Server

Enter the hostname or IP address of the remote syslog server to accept syslog messages. This syslog server handles the auditing
                                          of the all user-related operations (for example, login, logout, edit settings, and accessing the information). If server name
                                          is not specified, Cisco Emergency Responder does not send the syslog messages.

601 is the default port to which the messages are sent and used to communicate to the remote syslog server.

Do not
                                                      						specify a Cisco Emergency Responder node as the destination because the Cisco
                                                      						Emergency Responder node does not accept syslog messages from another server.

Local
                                          					 Audit Log Settings

Enable
                                          					 Local Audit Log

Check the
                                          					 check box to create an audit log for the application audit log.

The
                                          					 application audit log supports configuration updates for Cisco Emergency
                                          					 Responder Administration and Cisco Emergency Responder Serviceability.

The option is set to Disabled by default.

The Audit Log Agent Service must be active.

Enable
                                          					 Local Log Rotation

This
                                          					 setting is enabled by default. The system reads this option to rotate the audit
                                          					 log files or to continue to create new files. It begins to overwrite the oldest
                                          					 audit log files after it reaches the maximum number of files.

The
                                          					 maximum number of files cannot exceed 500.

Maximum
                                          					 No. of Files

Enter the
                                          					 maximum number of files that you want to include in the log. The default
                                          					 setting is 250 and the maximum number cannot exceed 500.

Maximum
                                          					 File Size (MB)

Enter the
                                          					 maximum file size for the audit log. The file size value must remain between 1
                                          					 and 5 MB.

Warning
                                          					 Threshold for Approaching Log Rotation Overwrite (%)

Set the threshold at which the system sends you an alert, when the audit logs are approaching the level where they are overwritten.

The total disk space allocated to audit logs is the Maximum No. of Files multiplied by the Maximum File Size. If the size
                                                      of audit logs on the disk exceeds this percentage of total disk space allocated, the system raises an alert in Event Viewer.
                                                      The default value is 80% for the warning threshold.

Set to
                                          					 Default

Click the
                                          					 button to set default values for all the parameters.

Cisco Emergency
                                             				Responder always uses the TCP port to connect and send data to the
                                          			 remote syslog server irrespective of the mode (Enhanced Security Mode or
                                          			 Normal). When Cisco
                                             				Emergency Responder fails to send data to the remote syslog server
                                          			 due to connectivity issues or any other exception, the administrator is
                                          			 notified through email about the failure condition and a notification is sent
                                          			 to the event syslog server that is configured under System > Cisco ER Group
                                                				  Settings . The data sent to event syslog server uses
                                          			 the UDP port in the normal mode and the TCP port in the Enhanced Security Mode.
                                          			 The utils
                                             				remotesyslog CLI command is not supported in Cisco
                                             				Emergency Responder .

## SNMP Community
                        	 String Configuration

The SNMP
                              		  Community String Configuration page appears when you choose SNMP > V1/V2c
                                 			 Configuration > Community String .

### Authorization
                              		  Requirements

You must
                              		  have serviceability authority to access this page.

### Description

Use the
                              		  SNMP Community String Configuration page to view, add, update, and delete
                              		  community strings. Community strings control access to the Emergency Responder
                              		  by clients using SNMP V1 and V2c.

The
                              		  following table describes the SNMP Community String Configuration page.

Field

Description

Community String Name column

Lists all community strings defined for the selected server.
                                          					 Click the name of the community string to update the information for that
                                          					 community string.

Add New button or icon

Add a new community string for the selected server. When you
                                          					 click this button, Emergency Responder opens a second SNMP Community String
                                          					 Configuration page.

Clicking
                                                      						the Add
                                                         						  New button brings up the same screen displayed when you click the Add
                                                         						  New icon.

Delete Selected button or icon

Deletes the selected community strings. To delete a community
                                          					 string, you must first select it from the list of community strings. Click the
                                          					 box to the left of the community string name to select it. To delete all
                                          					 community strings from the selected server, click the box to the left of the Community
                                             						String Name column heading.

Clicking
                                                      						the Delete
                                                         						  Selected button initiates the same action as does clicking the Delete icon at the top of the page.

Use the
                              		  second SNMP Community String Configuration page to add new SNMP community
                              		  strings and to update existing SNMP community strings.

The
                              		  following table describes the second SNMP Community String Configuration page.

Field

Description

Community String Name

If
                                          					 you are adding a new community string, type the name of the new community
                                          					 string into this text box. If you are updating information for an existing
                                          					 community string, the name of community string being updated is displayed.

Accept SNMP Packets from any host

Click this radio button to allow any host to access the
                                          					 Emergency Responder using SNMP.

Accept SNMP Packets only from these hosts

Click this radio button to specify which hosts can access the
                                          					 Emergency Responder using SNMP. To add hosts that you want to have SNMP access,
                                          					 enter the IP addresses of the new hosts and click Insert ; to remove hosts that you no longer want to have SNMP
                                          					 access, enter the IP addresses of the hosts and click Remove .

Access Privileges pulldown menu

When adding a new community string, allows you to specify the
                                          					 access privilege for the new community string. When updating a community
                                          					 string, displays the current access privilege level. The available access
                                          					 privilege levels are as follows:

- ReadOnly

- ReadWrite

- ReadWriteNotify

- NotifyOnly

- None

Insert button or icon

Inserts a new community string for the selected server. You must
                                          					 fill in the other fields on this page before you can insert the new community
                                          					 string.

Clear button or icon

Clears the community string information displayed on the current
                                          					 page.

## SNMP User
                        	 Configuration

The SNMP
                              		  User Configuration page appears when you choose SNMP > V3
                                 			 Configuration > User .

### Authorization
                              		  Requirements

You must
                              		  have serviceability authority to access this page.

### Description

Use the
                              		  SNMP User Configuration page to configure new SNMP V3 users.

The
                              		  following table describes the SNMP User Configuration page.

Field

Description

Server pulldown menu

Name of the server for which you want to view, add, update, or
                                          					 delete users. After you select a server, Emergency Responder displays the
                                          					 currently configured information in the following format:

- User Name

- Authentication Required

- Authentication Protocol

- Privacy Required

- Privacy Protocol

- Access Privileges

Click user name to display the Add and Update SNMP User
                                          					 Configuration page, from which you can update the information for that user.

Add New User button or icon

Add a new user for the selected server. When you click this
                                          					 icon, Emergency Responder opens the Add/Update SNMP User Configuration page.

Delete Selected button or icon

Deletes the users. To delete a user, you must first select it
                                          					 from the list of users. Click in the box to the left of the user name to select
                                          					 it. To delete all users from the selected server, click the box to the left of
                                          					 the User
                                             						Name column heading.

Use the
                              		  second SNMP User Configuration page to configure new SNMP V3 users.

The
                              		  following table describes the Add/Update SNMP User Configuration page.

Field

Description

User Name field

Enter the name of the new SNMP V3 user.

If you
                                                      						reached this page by clicking an existing user name on the SNMP User
                                                      						Configuration page, the fields on this page display the currently configured
                                                      						information.

Authentication Information

Use this section to configure the following information:

- If authentication is required
                                             						for this user, check the check box that is labeled Authentication Required.

- Enter the authentication
                                             						password for the new user in the Password and Reenter Password text boxes.

- To select the authentication
                                             						protocol for the new user, click the radio button for either MD5 or SHA.

Privacy Information

Use this section to configure the following information:

- If privacy is required for
                                             						this user, check the check box that is labelled Privacy Required.

- Enter the privacy password
                                             						for the new user in the Password and Reenter Password text boxes.

- To select the privacy
                                             						protocol for the new user, click on radio button labelled DES .

Host IP Addresses Information

Use the radio buttons in this section of the page to do the
                                          					 following:

- Specify which hosts can
                                             						access the Emergency Responder using SNMP. You can insert IP addresses for new
                                             						hosts that you want to have SNMP access to the Emergency Responder, or you can
                                             						remove IP addresses of hosts that you no longer want to have SNMP access to
                                             						Emergency Responder.

- Allow any host to access
                                             						Emergency Responder using SNMP.

Access Privileges pulldown menu

When adding a new user, this pull-down menu allows you to
                                          					 specify the access privilege for the new user. When updating a user's
                                          					 information, this field displays the current access privilege level. The
                                          					 available access privilege levels are as follows:

- ReadOnly

- ReadWrite

- ReadWriteNotify

- NotifyOnly

- None

Insert button or icon

Insert the new user information for the selected server.

Clear button or icon

Clears the user information displayed on the current page.

## MIB2 System Group
                        	 Configuration

The MIB2
                              		  SystemGroup Configuration page appears when you choose SNMP > System
                                 			 Group Configuration > MIB2 System Group Configuration .

### Authorization
                              		  Requirements

You must
                              		  have serviceability authority to access this page.

### Description

Use the
                              		  MIB2 System Group Configuration page to specify the name and physical location
                              		  of the contact person for MIB2 managed mode.

The
                              		  following table describes the MIB2 System Group Configuration page.

Field

Description

System Contact

The name of the MIB2 contact.

System Location

The physical location of the managed node.

Update button or icon

Saves the updated MIB2 contact information.

Clear button or icon

Clears the MIB2 contact information displayed on the current
                                          					 page.

## CPU and Memory
                        	 Usage

The CPU
                              		  and Memory Usage page appears when you choose System Monitor
                                 			 > CPU & Memory Usage .

### Authorization
                              		  Requirements

You must
                              		  have serviceability authority to access this page.

### Description

Use the
                              		  CPU and Memory Usage page to view the CPU and memory usage for the Emergency
                              		  Responder system.

The
                              		  following table describes the CPU and Memory Usage page.

Field

Description

Disable Auto-Refresh

Check this check box to disable auto-refresh of the information
                                          					 displayed on this page.

Set the screen reset value

Specify in seconds how often this page should be refreshed.

Set CPU Logging Interval

Specify in seconds how often CPU usage is logged. The interval
                                          					 must be between 5 and 600 seconds.

This section displays the percentage of CPU time being used by
                                          					 various system components.

Download CPU Log File

Click this link to download the currently displayed CPU and
                                          					 memory usage information to a file. When you click on this link, a new page
                                          					 opens that lists all the saved CPU log files. For more information about this
                                          					 screen, see Table 2 .

Processor

Name of the processor.

%User

Percentage of processor time being used by the User mode.

%System

Percentage of processor time being used by the System mode.

%Nice

Percentage of processor time being used by nice tasks.

Nice is a
                                                      						value associated with a process that determines when the process is executed.
                                                      						Nice tasks are only those tasks whose nice value is positive.

%Idle

Percentage of time in which the processor is idle.

%Irq

Percentage of processor time being used by interrupt requests
                                          					 (IRQ).

%Softirq

Percentage of processor time being used by soft IRQs.

A soft IRQ
                                                      						is an interrupt request that can be deferred.

%I/O Wait

Percentage of time that the processor is executing read or write
                                          					 operations.

%CPU

The processor's share of the elapsed CPU time (excluding idle
                                          					 time) since last update, expressed as a percentage of CPU time.

Start Log button

Starts a log file of the current CPU usage.

You can
                                                      						create a maximum of 25 CPU log files.

This section displays the percentage of memory allocated for
                                          					 different uses.

Download Memory Log File

Click this link to download to a file the currently displayed
                                          					 CPU and memory usage information. When you click this link, a new page opens
                                          					 that lists all the saved CPU log files. For more information about this screen,
                                          					 see Table 3 .

Total (KB)

The amount of memory available, in kilobytes.

Used (KB)

Amount of memory currently being used, in kilobytes.

Free (KB)

Amount of memory that is available for use, in kilobytes.

Shared (KB)

Amount of memory used by shared processes, in kilobytes.

Buffers (KB)

Amount of memory used by buffers, in kilobytes.

Cached (KB)

Amount of memory used for caching, in kilobytes.

Total Swap (KB)

Amount of total swap space, in kilobytes

Used Swap (KB)

Amount of swap space currently being used, in kilobytes.

Free Swap (KB)

Amount of available swap space, in kilobytes

%VM Used

Amount of virtual memory being used.

Start Log button

Starts a log file of the current memory usage.

Use the
                              		  CPU Log Files page to view and download the CPU log files.

The
                              		  following table describes the CPU Log Files page.

Field

Description

Download button

Download the selected log files. You must first select the file
                                          					 to be downloaded. To do so, click the box to the left of the File Name. If you
                                          					 click the box to the left of the File Name column heading, all files are
                                          					 selected for download.

This section displays the details of the saved CPU log files.

File Name

Name of the saved CPU log file. If you click on the file name, a
                                          					 new screen opens and displays the contents of the log file.

Last Modified

Date and time of the last modification to the CPU log file.

File Size (KB)

Size of the CPU log file, in kilobytes.

Use the
                              		  Memory Log Files page to view and download the memory log files.

The
                              		  following table describes the Memory Log Files page.

Field

Description

Download button

Download the selected log files. You must first select the file
                                          					 to be downloaded. To do so, click the box to the left of the File Name. If you
                                          					 click the box to the left of the File
                                             						Name column heading, all files are selected for download.

This section displays the details of the saved Memory log files.

File Name

Name of the saved Memory log file. If you click on the file
                                          					 name, a new screen opens and displays the contents of the log file.

Last Modified

Date and time of the last modification to the Memory log file.

File Size (KB)

Size of the Memory log file, in kilobytes.

## Processes

The
                              		  Processes page appears when you choose System Monitor
                                 			 > Processes .

### Authorization
                              		  Requirements

You must
                              		  have serviceability authority to access this page.

### Description

Use the
                              		  Processes page to view and download information about currently running
                              		  processes.

Use the Up and
                                          			 Down arrows next to each column heading on the Processes page to sort the
                                          			 information by each category.

The
                              		  following table describes the Processes page.

Field

Description

Disable Auto-Refresh

Check this check box to disable auto-refresh of the information
                                          					 displayed on this page.

Refresh Rate

To
                                          					 specify in seconds how often this page should be refreshed, enter a number in
                                          					 the text box, then click the Set button to the right of the text box.

Download Log File

Click this link to download log files you have created. You
                                          					 cannot download log files until you have first created them.

Select

Check boxes that allow you to select files to be viewed or
                                          					 downloaded.

Process

Name of the process.

PID

ID
                                          					 number of the process.

%CPU

Percentage of processor time being used by the process.

Status

Task's
                                          					 process status: Running (R), Sleeping (S), Uninterruptible disk sleep (D),
                                          					 Zombie (Z), 4 Traced (T), Paging (P)

Nice (Level)

Represents scheduling priority for the process. A nice value of
                                          					 20 is the highest priority and 19 is the lowest priority. The default nice
                                          					 value for most processes is 0.

Vm
                                          					 RSS (KB)

Resident set currently in physical memory in kilobytes,
                                          					 including Code, Data and Stack.

Vm
                                          					 Size (KB)

Size of virtual memory, in kilobytes.

Vm
                                          					 Data (KB)

Amount of data currently stored in virtual memory, in kilobytes.

Thread Count

Number of program threads currently running.

Data Stack (KB)

Size of the data stack, in kilobytes.

Page Fault Count

Number of major page faults the task has made requiring loading
                                          					 of memory.

Use the
                              		  View Selected Processes page to view the selected processes and download the
                              		  processes log files.

The
                              		  following table describes the View Selected Processes page.

Field

Description

Disable Auto-Refresh

Check this check box to disable auto-refresh of the information
                                          					 displayed on this page.

Refresh Rate

To specify in seconds how often this page should be refreshed,
                                          					 enter a number in the text box, then click the Set button to the right of the text box.

View All Processes button

Returns you to the previous Processes screen, which displays all
                                          					 running processes.

Start Log button

Creates a log of the selected processes displayed on this page.

Download Log File link

Download the selected processes log file.

This section displays the details of the selected processes. The
                                          					 details are the same as those listed in Table 1 .

## Disk Usage

The Disk
                              		  Usage page appears when you choose System Monitor
                                 			 > Disk Usage .

### Authorization
                              		  Requirements

You must
                              		  have serviceability authority to access this page.

### Description

Use the
                              		  Disk Usage page to list the percentage of disk space used by the different
                              		  partitions in the system.

Use the Up and
                                          			 Down arrows next to each column heading on the Disk Usage page to sort the
                                          			 information by each category.

The
                              		  following table describes the Disk Usage page.

Field

Description

Partition

Name of the partition.

Size

Size of the partition.

Percentage Used

How much disk space is the partition using, as a percentage of
                                          					 total allocated disk space.

Available Space

How much disk space is currently available on the partition.

Used Space

How much disk space is the partition using.

## System Logs
                        	 Menu

The System
                              		  Logs menu contains the following submenus, under which all system logs are
                              		  grouped:

System Logs > CER Logs

System Logs > Platform Logs

System Logs > DB Logs

System Logs > CLI Output Files

System Logs > SLM Logs

### Authorization
                              		  Requirements

You must
                              		  have serviceability authority to access the System Logs pages.

The
                              		  following table describes the System Logs pages.

Field

Description

Download button

Download the selected log files. You must first select the file to be downloaded. To do so, click the box to the left of the
                                          File Name. If you click the box to the left of the File Name column heading, all files are selected for download.

File Name

Name of the log file. If you click the file name, the contents of the log file display on a new screen.

Log files of size 0 KB or  greater than 15 MB will not have hyperlinks for viewing the content. Also, files with .gz and .gzo
                                                      extensions do not include hyperlinks.

You must download the log file to view the complete list of contents. To access the content, select the required file from Cisco ER Serviceability > System Logs and click Download Log .

Reload Log File button

Reloads the log file currently being viewed, so that any updates
                                          					 can be seen.

Last Modified

Date the log file was last modified.

File Size (KB)

Size of the log file, in kilobytes.

Menu/Log File Page

Description

CER Logs > CER Admin

View or download Emergency Responder Admin logs.

CER Logs > CER
                                             						Server

View or download Emergency Responder Server logs.

CER Logs > CER Phone
                                             						Tracking

View or download Emergency Responder Phone Tracking logs.

CER Logs > CER Audit

View or download Emergency Responder audit logs.

CER Logs> CER API Services

View or download API service logs.

CER Logs > JTAPI

View or download JTAPI logs.

CER Logs > Tomcat

View or download Tomcat logs.

CER Logs > Event
                                             						Viewer

View or download Emergency Responder Event logs.

CER Logs > Audio
                                             						Driver

View or download Emergency Responder Audio Driver logs.

CER Logs > Detailed Logs

View or download Emergency Responder detailed logs.

Platform Logs > CLI

View or download CLI operations logs.

Platform Logs > CLM

View or download CLM (Cluster Manager) logs.

Platform Logs >
                                             						Certificate Management/IPSec

View or download Certificate Management and IPSec logs.

Platform Logs > DRS

View or download DRS (Disaster Recovery System) logs.

Platform Logs >
                                             						Install/Upgrade

View or download Installation and Upgrade logs.

Platform Logs > Remote
                                             						Support

View or download Remote Account creation and operations logs.

Platform Logs >
                                             						Syslog

View or download Syslog logs.

Platform Logs >
                                             						Servm

View or download Servm (Services Manager) logs.

DB Logs > Cerdbmon

View or download Cerdbmon logs.

DB Logs > Install DB

View or download InstallDB Utility logs.

CLI OutputFiles
                                             						>Platform

View or download Platform log files.

CLI OutputFiles > DB

View or download DB log files.

SLM
                                                						  Logs > SLM

View or
                                          					 download SLM log files.

SLM
                                                						  Logs > GCH

View or
                                          					 download GCH log files.

SLM
                                                						  Logs > TP

View or
                                          					 download TP log files.

| Field | Description |
|---|---|
| Start button | Starts the selected services. |
| Stop button | Stops the selected services. |
| Restart button | Restarts the selected services. |
| Refresh button | Refreshes the list of currently running services on the selected
                                          					 server. |
| Service Name | Names of the currently running services on the selected server.
                                          					 To select a service, click the radio button next to the service name. |
| Status | Current status of the selected service. |

| Field | Description |
|---|---|
| Find
                                          					 Events in the month | Select a
                                          					 specific month to view events from the month. |
| Type drop-down menu | Note This drop-down menu contains two options: Type and Module. When you choose either Type or Module, the drop-down menu to the
                                                      right changes to display the available Type or Module options. Allows you to select which type of event you want to view. The
                                          					 available types are: ALL INFO WARN ERROR These options are displayed in the drop-down menu to the right of the Type drop-down menu. | Note | This drop-down menu contains two options: Type and Module. When you choose either Type or Module, the drop-down menu to the
                                                      right changes to display the available Type or Module options. |
| Note | This drop-down menu contains two options: Type and Module. When you choose either Type or Module, the drop-down menu to the
                                                      right changes to display the available Type or Module options. |
| Module down menu | Note This drop-down menu contains two options: Type and Module. When you choose either Type or Module, the drop-down menu to the
                                                      right changes to display the available Type or Module options. Allows you to select the Emergency Responder module for which you want to view events. When you select Module from the drop-down
                                          menu, the menu to the right changes to show the available modules. The available options are: All CER_DATABASE CER_SYSADMIN CER_REMOTEUPDATE CER_TELEPHONY CER_PHONETRACKINGENGINE CER_AGGREGATOR CER_ONSITEALERT CER_GROUP CER_CALLENGINE CER_CLUSTER CER_PROVIDER | Note | This drop-down menu contains two options: Type and Module. When you choose either Type or Module, the drop-down menu to the
                                                      right changes to display the available Type or Module options. |
| Note | This drop-down menu contains two options: Type and Module. When you choose either Type or Module, the drop-down menu to the
                                                      right changes to display the available Type or Module options. |
| Items Per Page menu | Allows you to select the number of events displayed per page.
                                          					 Options are 10, 20, 30, 40, or 50 events. |
|  | Displays search results. Note This area
                                                      						of the page is not visible until you perform a search operation. | Note | This area
                                                      						of the page is not visible until you perform a search operation. |
| Note | This area
                                                      						of the page is not visible until you perform a search operation. |
| Type column | Displays the type of event. The Type column displays one of the
                                          					 following: INFO WARN ERROR Use
                                          					 the Up and Down arrows to perform an ascending or descending sort of the
                                          					 results. |
| Time column | Displays the time of the event. Use the Up and Down arrows to
                                          					 perform an ascending or descending sort of the results. |
| Module column | Displays the Emergency Responder module to which the event
                                          					 applies. The modules are: CER_DATABASE CER_SYSADMIN CER_REMOTEUPDATE CER_TELEPHONY CER_PHONETRACKINGENGINE CER_AGGREGATOR CER_ONSITEALERT CER_GROUP CER_CALLENGINE CER_CLUSTER CER_PROVIDER Use the Up and Down arrows to perform an ascending or descending
                                          					 sort of the results. |
| Message column | Displays the message associated with each event. Use the Up and
                                          					 Down arrows at the right of the text box to scroll through the message. |

| Note | This drop-down menu contains two options: Type and Module. When you choose either Type or Module, the drop-down menu to the
                                                      right changes to display the available Type or Module options. |
|---|---|

| Note | This drop-down menu contains two options: Type and Module. When you choose either Type or Module, the drop-down menu to the
                                                      right changes to display the available Type or Module options. |
|---|---|

| Note | This area
                                                      						of the page is not visible until you perform a search operation. |
|---|---|

| Field | Description |
|---|---|
| Audit
                                          					 Level Settings |
| Audit
                                          					 Event Level Warning is the default value. | Choose the
                                          					 required severity level for the audit event from the drop-down list. If you,
                                          					 choose Debug all the syslog messages including Info , Error , and Warning are sent to the remote syslog server and
                                          					 stored locally in audit log file if the local audit logging is enabled. |
| Remote
                                          					 SysLog Settings |
| Remote
                                          					 Syslog Server | Enter the hostname or IP address of the remote syslog server to accept syslog messages. This syslog server handles the auditing
                                          of the all user-related operations (for example, login, logout, edit settings, and accessing the information). If server name
                                          is not specified, Cisco Emergency Responder does not send the syslog messages. 601 is the default port to which the messages are sent and used to communicate to the remote syslog server. Note Do not
                                                      						specify a Cisco Emergency Responder node as the destination because the Cisco
                                                      						Emergency Responder node does not accept syslog messages from another server. | Note | Do not
                                                      						specify a Cisco Emergency Responder node as the destination because the Cisco
                                                      						Emergency Responder node does not accept syslog messages from another server. |
| Note | Do not
                                                      						specify a Cisco Emergency Responder node as the destination because the Cisco
                                                      						Emergency Responder node does not accept syslog messages from another server. |
| Local
                                          					 Audit Log Settings |
| Enable
                                          					 Local Audit Log | Check the
                                          					 check box to create an audit log for the application audit log. The
                                          					 application audit log supports configuration updates for Cisco Emergency
                                          					 Responder Administration and Cisco Emergency Responder Serviceability. The option is set to Disabled by default. Note The Audit Log Agent Service must be active. | Note | The Audit Log Agent Service must be active. |
| Note | The Audit Log Agent Service must be active. |
| Enable
                                          					 Local Log Rotation | This
                                          					 setting is enabled by default. The system reads this option to rotate the audit
                                          					 log files or to continue to create new files. It begins to overwrite the oldest
                                          					 audit log files after it reaches the maximum number of files. The
                                          					 maximum number of files cannot exceed 500. |
| Maximum
                                          					 No. of Files | Enter the
                                          					 maximum number of files that you want to include in the log. The default
                                          					 setting is 250 and the maximum number cannot exceed 500. |
| Maximum
                                          					 File Size (MB) | Enter the
                                          					 maximum file size for the audit log. The file size value must remain between 1
                                          					 and 5 MB. |
| Warning
                                          					 Threshold for Approaching Log Rotation Overwrite (%) | Set the threshold at which the system sends you an alert, when the audit logs are approaching the level where they are overwritten. Note The total disk space allocated to audit logs is the Maximum No. of Files multiplied by the Maximum File Size. If the size
                                                      of audit logs on the disk exceeds this percentage of total disk space allocated, the system raises an alert in Event Viewer.
                                                      The default value is 80% for the warning threshold. | Note | The total disk space allocated to audit logs is the Maximum No. of Files multiplied by the Maximum File Size. If the size
                                                      of audit logs on the disk exceeds this percentage of total disk space allocated, the system raises an alert in Event Viewer.
                                                      The default value is 80% for the warning threshold. |
| Note | The total disk space allocated to audit logs is the Maximum No. of Files multiplied by the Maximum File Size. If the size
                                                      of audit logs on the disk exceeds this percentage of total disk space allocated, the system raises an alert in Event Viewer.
                                                      The default value is 80% for the warning threshold. |
| Set to
                                          					 Default | Click the
                                          					 button to set default values for all the parameters. |

| Note | Do not
                                                      						specify a Cisco Emergency Responder node as the destination because the Cisco
                                                      						Emergency Responder node does not accept syslog messages from another server. |
|---|---|

| Note | The Audit Log Agent Service must be active. |
|---|---|

| Note | The total disk space allocated to audit logs is the Maximum No. of Files multiplied by the Maximum File Size. If the size
                                                      of audit logs on the disk exceeds this percentage of total disk space allocated, the system raises an alert in Event Viewer.
                                                      The default value is 80% for the warning threshold. |
|---|---|

| Note | Cisco Emergency
                                             				Responder always uses the TCP port to connect and send data to the
                                          			 remote syslog server irrespective of the mode (Enhanced Security Mode or
                                          			 Normal). When Cisco
                                             				Emergency Responder fails to send data to the remote syslog server
                                          			 due to connectivity issues or any other exception, the administrator is
                                          			 notified through email about the failure condition and a notification is sent
                                          			 to the event syslog server that is configured under System > Cisco ER Group
                                                				  Settings . The data sent to event syslog server uses
                                          			 the UDP port in the normal mode and the TCP port in the Enhanced Security Mode.
                                          			 The utils
                                             				remotesyslog CLI command is not supported in Cisco
                                             				Emergency Responder . |
|---|---|

| Field | Description |
|---|---|
| Community String Name column | Lists all community strings defined for the selected server.
                                          					 Click the name of the community string to update the information for that
                                          					 community string. |
| Add New button or icon | Add a new community string for the selected server. When you
                                          					 click this button, Emergency Responder opens a second SNMP Community String
                                          					 Configuration page. Note Clicking
                                                      						the Add
                                                         						  New button brings up the same screen displayed when you click the Add
                                                         						  New icon. | Note | Clicking
                                                      						the Add
                                                         						  New button brings up the same screen displayed when you click the Add
                                                         						  New icon. |
| Note | Clicking
                                                      						the Add
                                                         						  New button brings up the same screen displayed when you click the Add
                                                         						  New icon. |
| Delete Selected button or icon | Deletes the selected community strings. To delete a community
                                          					 string, you must first select it from the list of community strings. Click the
                                          					 box to the left of the community string name to select it. To delete all
                                          					 community strings from the selected server, click the box to the left of the Community
                                             						String Name column heading. Note Clicking
                                                      						the Delete
                                                         						  Selected button initiates the same action as does clicking the Delete icon at the top of the page. | Note | Clicking
                                                      						the Delete
                                                         						  Selected button initiates the same action as does clicking the Delete icon at the top of the page. |
| Note | Clicking
                                                      						the Delete
                                                         						  Selected button initiates the same action as does clicking the Delete icon at the top of the page. |

| Note | Clicking
                                                      						the Add
                                                         						  New button brings up the same screen displayed when you click the Add
                                                         						  New icon. |
|---|---|

| Note | Clicking
                                                      						the Delete
                                                         						  Selected button initiates the same action as does clicking the Delete icon at the top of the page. |
|---|---|

| Field | Description |
|---|---|
| Community String Name | If
                                          					 you are adding a new community string, type the name of the new community
                                          					 string into this text box. If you are updating information for an existing
                                          					 community string, the name of community string being updated is displayed. |
| Host IP Address Information |
| Accept SNMP Packets from any host | Click this radio button to allow any host to access the
                                          					 Emergency Responder using SNMP. |
| Accept SNMP Packets only from these hosts | Click this radio button to specify which hosts can access the
                                          					 Emergency Responder using SNMP. To add hosts that you want to have SNMP access,
                                          					 enter the IP addresses of the new hosts and click Insert ; to remove hosts that you no longer want to have SNMP
                                          					 access, enter the IP addresses of the hosts and click Remove . |
| Access Privileges pulldown menu | When adding a new community string, allows you to specify the
                                          					 access privilege for the new community string. When updating a community
                                          					 string, displays the current access privilege level. The available access
                                          					 privilege levels are as follows: ReadOnly ReadWrite ReadWriteNotify NotifyOnly None |
| Insert button or icon | Inserts a new community string for the selected server. You must
                                          					 fill in the other fields on this page before you can insert the new community
                                          					 string. |
| Clear button or icon | Clears the community string information displayed on the current
                                          					 page. |

| Field | Description |
|---|---|
| Server pulldown menu | Name of the server for which you want to view, add, update, or
                                          					 delete users. After you select a server, Emergency Responder displays the
                                          					 currently configured information in the following format: User Name Authentication Required Authentication Protocol Privacy Required Privacy Protocol Access Privileges Click user name to display the Add and Update SNMP User
                                          					 Configuration page, from which you can update the information for that user. |
| Add New User button or icon | Add a new user for the selected server. When you click this
                                          					 icon, Emergency Responder opens the Add/Update SNMP User Configuration page. |
| Delete Selected button or icon | Deletes the users. To delete a user, you must first select it
                                          					 from the list of users. Click in the box to the left of the user name to select
                                          					 it. To delete all users from the selected server, click the box to the left of
                                          					 the User
                                             						Name column heading. |

| Field | Description |
|---|---|
| User Name field | Enter the name of the new SNMP V3 user. Note If you
                                                      						reached this page by clicking an existing user name on the SNMP User
                                                      						Configuration page, the fields on this page display the currently configured
                                                      						information. | Note | If you
                                                      						reached this page by clicking an existing user name on the SNMP User
                                                      						Configuration page, the fields on this page display the currently configured
                                                      						information. |
| Note | If you
                                                      						reached this page by clicking an existing user name on the SNMP User
                                                      						Configuration page, the fields on this page display the currently configured
                                                      						information. |
| Authentication Information | Use this section to configure the following information: If authentication is required
                                             						for this user, check the check box that is labeled Authentication Required. Enter the authentication
                                             						password for the new user in the Password and Reenter Password text boxes. To select the authentication
                                             						protocol for the new user, click the radio button for either MD5 or SHA. |
| Privacy Information | Use this section to configure the following information: If privacy is required for
                                             						this user, check the check box that is labelled Privacy Required. Enter the privacy password
                                             						for the new user in the Password and Reenter Password text boxes. To select the privacy
                                             						protocol for the new user, click on radio button labelled DES . |
| Host IP Addresses Information | Use the radio buttons in this section of the page to do the
                                          					 following: Specify which hosts can
                                             						access the Emergency Responder using SNMP. You can insert IP addresses for new
                                             						hosts that you want to have SNMP access to the Emergency Responder, or you can
                                             						remove IP addresses of hosts that you no longer want to have SNMP access to
                                             						Emergency Responder. Allow any host to access
                                             						Emergency Responder using SNMP. |
| Access Privileges pulldown menu | When adding a new user, this pull-down menu allows you to
                                          					 specify the access privilege for the new user. When updating a user's
                                          					 information, this field displays the current access privilege level. The
                                          					 available access privilege levels are as follows: ReadOnly ReadWrite ReadWriteNotify NotifyOnly None |
| Insert button or icon | Insert the new user information for the selected server. |
| Clear button or icon | Clears the user information displayed on the current page. |

| Note | If you
                                                      						reached this page by clicking an existing user name on the SNMP User
                                                      						Configuration page, the fields on this page display the currently configured
                                                      						information. |
|---|---|

| Field | Description |
|---|---|
| System Contact | The name of the MIB2 contact. |
| System Location | The physical location of the managed node. |
| Update button or icon | Saves the updated MIB2 contact information. |
| Clear button or icon | Clears the MIB2 contact information displayed on the current
                                          					 page. |

| Field | Description |
|---|---|
| Disable Auto-Refresh | Check this check box to disable auto-refresh of the information
                                          					 displayed on this page. |
| Set the screen reset value | Specify in seconds how often this page should be refreshed. |
| Set CPU Logging Interval | Specify in seconds how often CPU usage is logged. The interval
                                          					 must be between 5 and 600 seconds. |
| Processors | This section displays the percentage of CPU time being used by
                                          					 various system components. |
| Download CPU Log File | Click this link to download the currently displayed CPU and
                                          					 memory usage information to a file. When you click on this link, a new page
                                          					 opens that lists all the saved CPU log files. For more information about this
                                          					 screen, see Table 2 . |
| Processor | Name of the processor. |
| %User | Percentage of processor time being used by the User mode. |
| %System | Percentage of processor time being used by the System mode. |
| %Nice | Percentage of processor time being used by nice tasks. Note Nice is a
                                                      						value associated with a process that determines when the process is executed.
                                                      						Nice tasks are only those tasks whose nice value is positive. | Note | Nice is a
                                                      						value associated with a process that determines when the process is executed.
                                                      						Nice tasks are only those tasks whose nice value is positive. |
| Note | Nice is a
                                                      						value associated with a process that determines when the process is executed.
                                                      						Nice tasks are only those tasks whose nice value is positive. |
| %Idle | Percentage of time in which the processor is idle. |
| %Irq | Percentage of processor time being used by interrupt requests
                                          					 (IRQ). |
| %Softirq | Percentage of processor time being used by soft IRQs. Note A soft IRQ
                                                      						is an interrupt request that can be deferred. | Note | A soft IRQ
                                                      						is an interrupt request that can be deferred. |
| Note | A soft IRQ
                                                      						is an interrupt request that can be deferred. |
| %I/O Wait | Percentage of time that the processor is executing read or write
                                          					 operations. |
| %CPU | The processor's share of the elapsed CPU time (excluding idle
                                          					 time) since last update, expressed as a percentage of CPU time. |
| Start Log button | Starts a log file of the current CPU usage. Note You can
                                                      						create a maximum of 25 CPU log files. | Note | You can
                                                      						create a maximum of 25 CPU log files. |
| Note | You can
                                                      						create a maximum of 25 CPU log files. |
| Memory | This section displays the percentage of memory allocated for
                                          					 different uses. |
| Download Memory Log File | Click this link to download to a file the currently displayed
                                          					 CPU and memory usage information. When you click this link, a new page opens
                                          					 that lists all the saved CPU log files. For more information about this screen,
                                          					 see Table 3 . |
| Total (KB) | The amount of memory available, in kilobytes. |
| Used (KB) | Amount of memory currently being used, in kilobytes. |
| Free (KB) | Amount of memory that is available for use, in kilobytes. |
| Shared (KB) | Amount of memory used by shared processes, in kilobytes. |
| Buffers (KB) | Amount of memory used by buffers, in kilobytes. |
| Cached (KB) | Amount of memory used for caching, in kilobytes. |
| Total Swap (KB) | Amount of total swap space, in kilobytes |
| Used Swap (KB) | Amount of swap space currently being used, in kilobytes. |
| Free Swap (KB) | Amount of available swap space, in kilobytes |
| %VM Used | Amount of virtual memory being used. |
| Start Log button | Starts a log file of the current memory usage. |

| Note | Nice is a
                                                      						value associated with a process that determines when the process is executed.
                                                      						Nice tasks are only those tasks whose nice value is positive. |
|---|---|

| Note | A soft IRQ
                                                      						is an interrupt request that can be deferred. |
|---|---|

| Note | You can
                                                      						create a maximum of 25 CPU log files. |
|---|---|

| Field | Description |
|---|---|
| Download button | Download the selected log files. You must first select the file
                                          					 to be downloaded. To do so, click the box to the left of the File Name. If you
                                          					 click the box to the left of the File Name column heading, all files are
                                          					 selected for download. |
| CPU Log Files | This section displays the details of the saved CPU log files. |
| File Name | Name of the saved CPU log file. If you click on the file name, a
                                          					 new screen opens and displays the contents of the log file. |
| Last Modified | Date and time of the last modification to the CPU log file. |
| File Size (KB) | Size of the CPU log file, in kilobytes. |

| Field | Description |
|---|---|
| Download button | Download the selected log files. You must first select the file
                                          					 to be downloaded. To do so, click the box to the left of the File Name. If you
                                          					 click the box to the left of the File
                                             						Name column heading, all files are selected for download. |
| Memory Log Files | This section displays the details of the saved Memory log files. |
| File Name | Name of the saved Memory log file. If you click on the file
                                          					 name, a new screen opens and displays the contents of the log file. |
| Last Modified | Date and time of the last modification to the Memory log file. |
| File Size (KB) | Size of the Memory log file, in kilobytes. |

| Note | Use the Up and
                                          			 Down arrows next to each column heading on the Processes page to sort the
                                          			 information by each category. |
|---|---|

| Field | Description |
|---|---|
| Disable Auto-Refresh | Check this check box to disable auto-refresh of the information
                                          					 displayed on this page. |
| Refresh Rate | To
                                          					 specify in seconds how often this page should be refreshed, enter a number in
                                          					 the text box, then click the Set button to the right of the text box. |
| Download Log File | Click this link to download log files you have created. You
                                          					 cannot download log files until you have first created them. |
| Select | Check boxes that allow you to select files to be viewed or
                                          					 downloaded. |
| Process | Name of the process. |
| PID | ID
                                          					 number of the process. |
| %CPU | Percentage of processor time being used by the process. |
| Status | Task's
                                          					 process status: Running (R), Sleeping (S), Uninterruptible disk sleep (D),
                                          					 Zombie (Z), 4 Traced (T), Paging (P) |
| Nice (Level) | Represents scheduling priority for the process. A nice value of
                                          					 20 is the highest priority and 19 is the lowest priority. The default nice
                                          					 value for most processes is 0. |
| Vm
                                          					 RSS (KB) | Resident set currently in physical memory in kilobytes,
                                          					 including Code, Data and Stack. |
| Vm
                                          					 Size (KB) | Size of virtual memory, in kilobytes. |
| Vm
                                          					 Data (KB) | Amount of data currently stored in virtual memory, in kilobytes. |
| Thread Count | Number of program threads currently running. |
| Data Stack (KB) | Size of the data stack, in kilobytes. |
| Page Fault Count | Number of major page faults the task has made requiring loading
                                          					 of memory. |

| Field | Description |
|---|---|
| Disable Auto-Refresh | Check this check box to disable auto-refresh of the information
                                          					 displayed on this page. |
| Refresh Rate | To specify in seconds how often this page should be refreshed,
                                          					 enter a number in the text box, then click the Set button to the right of the text box. |
| View All Processes button | Returns you to the previous Processes screen, which displays all
                                          					 running processes. |
| Start Log button | Creates a log of the selected processes displayed on this page. |
| Download Log File link | Download the selected processes log file. |
| Processes | This section displays the details of the selected processes. The
                                          					 details are the same as those listed in Table 1 . |

| Note | Use the Up and
                                          			 Down arrows next to each column heading on the Disk Usage page to sort the
                                          			 information by each category. |
|---|---|

| Field | Description |
|---|---|
| Disk Usage Details |  |
| Partition | Name of the partition. |
| Size | Size of the partition. |
| Percentage Used | How much disk space is the partition using, as a percentage of
                                          					 total allocated disk space. |
| Available Space | How much disk space is currently available on the partition. |
| Used Space | How much disk space is the partition using. |

| Note | Use the Up and Down arrows next to each column heading to sort the information by each category. |
|---|---|

| Field | Description |
|---|---|
| Download button | Download the selected log files. You must first select the file to be downloaded. To do so, click the box to the left of the
                                          File Name. If you click the box to the left of the File Name column heading, all files are selected for download. Note If you select multiple log files, the system creates a Zip file that contains the log files to be downloaded. | Note | If you select multiple log files, the system creates a Zip file that contains the log files to be downloaded. |
| Note | If you select multiple log files, the system creates a Zip file that contains the log files to be downloaded. |
| File Name | Name of the log file. If you click the file name, the contents of the log file display on a new screen. Note After viewing the contents, click the Back button in your browser to return to the log file page. Note Log files of size 0 KB or  greater than 15 MB will not have hyperlinks for viewing the content. Also, files with .gz and .gzo
                                                      extensions do not include hyperlinks. You must download the log file to view the complete list of contents. To access the content, select the required file from Cisco ER Serviceability > System Logs and click Download Log . | Note | After viewing the contents, click the Back button in your browser to return to the log file page. | Note | Log files of size 0 KB or  greater than 15 MB will not have hyperlinks for viewing the content. Also, files with .gz and .gzo
                                                      extensions do not include hyperlinks. You must download the log file to view the complete list of contents. To access the content, select the required file from Cisco ER Serviceability > System Logs and click Download Log . |
| Note | After viewing the contents, click the Back button in your browser to return to the log file page. |
| Note | Log files of size 0 KB or  greater than 15 MB will not have hyperlinks for viewing the content. Also, files with .gz and .gzo
                                                      extensions do not include hyperlinks. You must download the log file to view the complete list of contents. To access the content, select the required file from Cisco ER Serviceability > System Logs and click Download Log . |
| Reload Log File button | Reloads the log file currently being viewed, so that any updates
                                          					 can be seen. Note This button is only available when you have clicked a file name and are viewing the contents of a particular log file. | Note | This button is only available when you have clicked a file name and are viewing the contents of a particular log file. |
| Note | This button is only available when you have clicked a file name and are viewing the contents of a particular log file. |
| Last Modified | Date the log file was last modified. |
| File Size (KB) | Size of the log file, in kilobytes. |

| Note | If you select multiple log files, the system creates a Zip file that contains the log files to be downloaded. |
|---|---|

| Note | After viewing the contents, click the Back button in your browser to return to the log file page. |
|---|---|

| Note | Log files of size 0 KB or  greater than 15 MB will not have hyperlinks for viewing the content. Also, files with .gz and .gzo
                                                      extensions do not include hyperlinks. You must download the log file to view the complete list of contents. To access the content, select the required file from Cisco ER Serviceability > System Logs and click Download Log . |
|---|---|

| Note | This button is only available when you have clicked a file name and are viewing the contents of a particular log file. |
|---|---|

| Menu/Log File Page | Description |
|---|---|
| CER Logs > CER Admin | View or download Emergency Responder Admin logs. |
| CER Logs > CER
                                             						Server | View or download Emergency Responder Server logs. |
| CER Logs > CER Phone
                                             						Tracking | View or download Emergency Responder Phone Tracking logs. |
| CER Logs > CER Audit | View or download Emergency Responder audit logs. |
| CER Logs> CER API Services | View or download API service logs. |
| CER Logs > JTAPI | View or download JTAPI logs. |
| CER Logs > Tomcat | View or download Tomcat logs. |
| CER Logs > Event
                                             						Viewer | View or download Emergency Responder Event logs. |
| CER Logs > Audio
                                             						Driver | View or download Emergency Responder Audio Driver logs. |
| CER Logs > Detailed Logs | View or download Emergency Responder detailed logs. |
| Platform Logs > CLI | View or download CLI operations logs. |
| Platform Logs > CLM | View or download CLM (Cluster Manager) logs. |
| Platform Logs >
                                             						Certificate Management/IPSec | View or download Certificate Management and IPSec logs. |
| Platform Logs > DRS | View or download DRS (Disaster Recovery System) logs. |
| Platform Logs >
                                             						Install/Upgrade | View or download Installation and Upgrade logs. |
| Platform Logs > Remote
                                             						Support | View or download Remote Account creation and operations logs. |
| Platform Logs >
                                             						Syslog | View or download Syslog logs. |
| Platform Logs >
                                             						Servm | View or download Servm (Services Manager) logs. |
| DB Logs > Cerdbmon | View or download Cerdbmon logs. |
| DB Logs > Install DB | View or download InstallDB Utility logs. |
| CLI OutputFiles
                                             						>Platform | View or download Platform log files. |
| CLI OutputFiles > DB | View or download DB log files. |
| SLM
                                                						  Logs > SLM | View or
                                          					 download SLM log files. |
| SLM
                                                						  Logs > GCH | View or
                                          					 download GCH log files. |
| SLM
                                                						  Logs > TP | View or
                                          					 download TP log files. |