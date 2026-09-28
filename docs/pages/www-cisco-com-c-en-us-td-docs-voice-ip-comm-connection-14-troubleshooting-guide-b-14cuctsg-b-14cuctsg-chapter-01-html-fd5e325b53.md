---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-troubleshooting-guide-b-14cuctsg-b-14cuctsg-chapter-01-html-fd5e325b53
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/troubleshooting/guide/b_14cuctsg/b_14cuctsg_chapter_01.html
retrieved_at: 2026-08-17T02:16:26.113652+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 14

# Troubleshooting Guide for Cisco Unity Connection Release 14

Updated: August 14, 2024

Chapter: Troubleshooting Utilities

## Chapter: Troubleshooting Utilities

# Troubleshooting Utilities

## Grammar Statistics Tool

The Grammar Statistics tool shows information about the dynamic name grammars that are used by the Unity Connection voice-recognition
                           conversation to match caller utterances to the names of objects on the system (for example, usernames and alternate names,
                           distribution list names, and so on). When administrators add or change names on the Unity Connection system, the names are
                           not recognized by the voice-recognition conversation until they are compiled in the grammars.

For each name grammar, the tool displays information such as the finish time of the last grammar recompilation, the total
                           number of unique items in the grammar, whether there are updates pending to the grammar, and whether the grammar is currently
                           in the process of being recompiled.

By default, Unity Connection recompiles grammars when administrators add named objects or change object names on the system
                           (unless a bulk operation is in progress, in which case Unity Connection waits ten minutes for the operation to complete before
                           recompiling the grammars), or when there are more than five changes requested in the space of a minute. If the grammars have
                           grown to the point where the name grammar recompilation process is affecting the performance of your Unity Connection server
                           during busy periods, you can modify the default Voice Recognition Update Schedule (under System Settings > Schedules in Cisco Unity
                           Connection Administration) to limit the times and days when the Unity Connection voice-recognition transport utility can automatically
                           rebuild the voice-recognition name grammars. By default, all days and times are active for this schedule; if you modify the
                           schedule but want to override the schedule while it is inactive and force an immediate recompilation of all grammars, or if
                           you want to force recompilation during the ten minute wait period after a bulk operation has been initiated, you can select
                           the Rebuild Grammars button on the Grammar Statistics tool.

## Cisco Unity
                        	 Connection Serviceability

Cisco Unity
                           		Connection Serviceability, a web-based troubleshooting tool for Unity
                           		Connection, provides the following functionality:

Displaying Unity Connection alarm definitions, which you can use
                                 			 for troubleshooting.

Enabling Unity Connection traces. You can collect and view trace
                                 			 information in the Real-Time Monitoring Tool (RTMT).

Configuring the logs to which Unity Connection trace information
                                 			 is saved.

Viewing and changing the server status of the Unity Connection
                                 			 servers when a Unity Connection cluster is configured.

Viewing the status of the Unity Connection feature services.

Activating, deactivating, starting, and stopping the Unity
                                 			 Connection services.

Generating reports that can be viewed in different file formats.

Depending on the service and component involved, you may
                           		complete serviceability-related tasks in both Cisco Unity Connection
                           		Serviceability and Cisco Unified Serviceability. For example, you may need to
                           		start and stop services, view alarms, and configure traces in both applications
                           		to troubleshoot a problem.

For more information, see the Administration Guide for Cisco Unity Connection Serviceability Release 14 , at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/serv_administration/guide/b_14cucservag.html .

## Task Management Tool

The Task Management pages list a variety of system maintenance and troubleshooting tasks that Unity Connection automatically
                           runs on a regular schedule. Tasks can be run at the same time as backups and anti-virus scans.

The default settings and schedules for each task are optimized for functionality and performance. We recommend that you not
                           change the default settings and schedules.

Caution

Some tasks are critical to Unity Connection functionality. Disabling or changing the frequency of critical tasks may adversely
                                       affect performance or cause Unity Connection to stop functioning.

### Accessing the Task
                           	 Management Tool

Step 1

In Cisco Unity Connection Administration, expand Tools .

Step 2

Select Task Management .

## Cisco Voice Technology Group Subscription Tool

You can use the Cisco Voice Technology Group Subscription tool to be notified by email of any Unity Connection software updates.
                           To subscribe, go to the Cisco Voice Technology Group Subscription Tool page at http://www.cisco.com/cgi-bin/Software/Newsbuilder/Builder/VOICE.cgi.

## Real-Time Monitoring Tool

The Real-Time Monitoring Tool (RTMT), which runs as a client-side application, uses HTTPS and TCP to monitor system performance,
                           device status, device discovery, and CTI applications for Unity Connection. RTMT can connect directly to devices via HTTPS
                           to troubleshoot system problems. RTMT can also monitor the voice messaging ports on Unity Connection.

RTMT allows you to perform the following tasks:

Monitoring a set of predefined management objects that focus on the health of the system.

Generating various alerts, in the form of emails, for objects when values go over or below user-configured thresholds.

Collecting and viewing traces in various default viewers that exist in RTMT.

Viewing syslog messages and alarm definitions in SysLog Viewer.

Working with performance-monitoring counters.

Monitoring the voice messaging ports on Unity Connection. When a Unity Connection cluster is configured, you can open multiple
                                 instances of RTMT to monitor voice messaging ports on each server in the Unity Connection cluster.

For more information, see the Cisco Unified Real-Time Monitoring Tool Administration Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .

## Cisco Unified Serviceability

Cisco Unified Serviceability, a web-based troubleshooting tool for Unity Connection, provides the following functionality:

Saving alarms and events for troubleshooting and providing alarm message definitions.

Saving trace information to various log files for troubleshooting.

Providing feature services that you can turn on, turn off, and view through the Service Activation window.

Providing an interface for starting and stopping feature and network services.

Generating and archiving daily reports; for example, alert summary or server statistic reports.

Monitoring the number of threads and processes in the system; uses cache to enhance the performance.

Depending on the service and component involved, you may complete serviceability-related tasks in both Cisco Unified Serviceability
                           and Cisco Unity Connection Serviceability. For example, you may need to start and stop services, view alarms, and configure
                           traces in both applications to troubleshoot a problem.

## Remote Database
                        	 Administration Tools

A
                           		database proxy can be enabled to allow the use of some Windows-based remote
                           		database administration tools that are available on the Cisco Unity Tools
                           		website ( http://ciscounitytools.com ),
                           		where updates to utilities are frequently posted between Unity Connection
                           		releases.

You can sign up to be notified when the utilities posted on the
                                       		  Cisco Unity Tools website are updated. Go to http://ciscounitytools.com and select Sign Up Here.

For details on enabling remote database access, see the “ Enabling Database Access for Remote Administration Tools ” section in the “Tools” chapter of the System Administration Guide for Cisco Unity Connection Release 14 , available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/administration/guide/b_14cucsag.html .

## Cisco Utilities Database Link for Informix (CUDLI)

The Cisco Utilities Database Link for Informix (CUDLI) tool allows you to navigate the Unity Connection database, learn about
                           the purpose of data in a particular table or column, and jump between referenced objects in the database. It also shows stored
                           procedures and includes a custom query builder.

Download the tool and view training videos and Help at http://www.ciscounitytools.com/Applications/CxN/CUDLI/CUDLI.html .

## Remote Port Status Monitor

The Remote Port Status Monitor (rPSM) provides a real-time view of the activity of each voice messaging port on Unity Connection
                           to assist in troubleshooting conversation flow and other problems.

Download the tool and view training videos and Help at http://www.ciscounitytools.com/Applications/CxN/PortStatusMonitorCUC7x/PortStatusMonitorCUC7x.html .

## Application Audit Logging

Application audit logging reports configuration and administrative changes for Cisco Unity Connection Administration, Cisco Personal
                           Communications Assistant, Cisco Unity Connection Serviceability, Cisco Unified Serviceability, Real-Time Monitoring Tool (RTMT),
                           and the command-line interface (CLI). It also reports user authentication events for Unity Connection clients that use the
                           Representational State Transfer (REST) APIs, and reports API calls for clients that use the Cisco Unity Connection Provisioning
                           Interface (CUPI) or the Diagnostic Portal API (used by Analysis Manager in RTMT).

Application audit logging is enabled by default. Users with the Audit Administrator role can configure auditing on the Tools >
                           Audit Log Configuration page in Cisco Unified Serviceability. (By default, the application administration account that is
                           created during installation is assigned the Audit Administrator role.) For Cisco Business Edition, the Audit Log Configuration
                           page settings also control auditing for Cisco Unified Communications Manager components.

To access the audit logs, users with the Audit Administrator role can use the Real-Time Monitoring Tool. In Trace and Log
                           Central, go to System > Audit Logs > Nodes. After you select the node, another window displays System > Cisco Audit Logs.
                           The application audit logs are stored in the AuditApp folder. In a Unity Connection cluster, the publisher and subscriber
                           each have separate application audit logs which you can reach by selecting the appropriate node.

Database and operating system audit logging are also available in Unity Connection, although they are disabled by default.
                           For more information on audit logging, see the “Configuring the Audit Log” chapter of the applicable Cisco Unified Serviceability Administration Guide at http://www.cisco.com/en/US/products/ps6509/prod_maintenance_guides_list.html .

## Network
                        	 Analyzer

The Network Analyzer
                           		is a tool that allows administrators to analyze the state of the network and
                           		monitor every node through visual representation of the network topology. It
                           		also enables administrators to synchronize the data in HTTP(S) networking
                           		through tool itself.

For more information
                           		on network analyzer, see the network analyzer documentation available at http://www.ciscounitytools.com/Applications/General/NetworkAnalyzer/Help/ConnectionNetworkAnalyzer.htm .

## System Restore
                        	 Tool

To diagnose the issues related to
                           		System Restore Tool, you can view the ERRORS.log file created at path
                           		/common/RestorePoints/recent. You can also use the diag_CuSysAgent.uc logs to
                           		troubleshoot issues corresponding to System Restore sysagent task. This section
                           		further covers the errors that you might get while using System Restore Tool.

### Database Error
                           	 While Creating Restore Point

If you are getting the "Database is
                              		not online" error while creating a restore point through CLI, reboot the system
                              		to get the database up.

### Error in Index
                           	 Validation

If you are getting any or all of
                              		the following errors related to index validation in ERROR.log file, drop and
                              		recreate the corrupted indexes.

ERROR: Bad key information in
                                    			 TBLspace description.

ERROR: Index ix_tbl_message_messageobjectidtypepriority for
                                    			 unitymbxdb1:informix.tbl_message is bad.

| Caution | Some tasks are critical to Unity Connection functionality. Disabling or changing the frequency of critical tasks may adversely
                                       affect performance or cause Unity Connection to stop functioning. |
|---|---|

| Step 1 | In Cisco Unity Connection Administration, expand Tools . |
|---|---|
| Step 2 | Select Task Management . |

| Note | You can sign up to be notified when the utilities posted on the
                                       		  Cisco Unity Tools website are updated. Go to http://ciscounitytools.com and select Sign Up Here. |
|---|---|