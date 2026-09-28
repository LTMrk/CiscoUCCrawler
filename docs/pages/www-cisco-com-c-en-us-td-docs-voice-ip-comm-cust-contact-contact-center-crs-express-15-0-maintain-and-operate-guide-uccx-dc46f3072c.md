---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-15-0-maintain-and-operate-guide-uccx-dc46f3072c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_15_0/maintain_and_operate/guide/uccx_b_1501_admin-and-operations-guide/uccx_m_1501_real-time-monitoring.html
retrieved_at: 2026-08-16T21:29:04.883345+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 15.0

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 15.0

Updated: April 30, 2025

Chapter: Real-Time Monitoring

## Chapter: Real-Time Monitoring

# Real-Time Monitoring

## Installation and
                        	 Configuration

The Unified RTMT
                              		  installer can be downloaded using Tools > Plug-ins menu on the Cisco
                                 			 Unified Contact Center Express Administration web interface. See "Cisco Unified
                                 			 Real-Time Monitoring Tool" section in Cisco Unified Real-Time
                                       				  Monitoring Tool Administration Guide for Cisco Unified Contact Center Express
                                       				  and Cisco Unified IP IVR for installation and configuration procedures, available here:

https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html

## Performance
                        	 Monitoring

Unified CCX provides performance counters (called perfmon counters) for application
                              		  performance monitoring. The perfmon counters help expose various performance
                              		  values and enables to track application performance in real time.

The
                              		  perfmon counters contain counter-based information, such as the name and index
                              		  of the counter, the scale, the type, subcounters to set when setting a counter,
                              		  the current values, and a map containing counter instance data. Each
                              		  performance counter instance object contains instance-based data, like the
                              		  instance ID and current values.

You can
                              		  log perfmon counters locally on the computer and use the performance log viewer
                              		  in Unified RTMT to display the perfmon CSV log files that you collected or the
                              		  Real-time Information Server Data Collection (RISDC) perfmon logs. Choose System > Performance on the Unified RTMT tool
                              		  to view perfmon counters.

### Performance Objects

Unified RTMT provides a set of default monitoring objects that assist
                                 		you in monitoring the health of the system. Default objects include performance
                                 		counters or critical event status for the system and other supported services.

The system logs information every 10 seconds for predefined system
                                 		counters.

### Performance
                           	 Counters

To
                                 		  troubleshoot system performance problems, you add a counter (query) that is
                                 		  associated with the perfmon object to the performance monitor, which displays a
                                 		  chart for the counter. Choose System > Performance > Open Performance
                                       				Monitoring to add a new counter.

For more
                                 		  information about monitoring objects and counters, see "Performance
                                    			 Monitoring" section in the Cisco Unified Real-Time
                                          				  Monitoring Tool Administration Guide for Cisco Unified Contact Center Express
                                          				  and Cisco Unified IP IVR ,
                                 		  available here:

https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html

### Performance
                           	 Objects and Counters for Unified CCX

Unified CCX database monitors

Unified CCX engine JVM heap

Intelligence
                                          				center database performance Info

Intelligence
                                          				center JVM statistics

Intelligence
                                          				center system condition table

Intelligence
                                          				center thread pool section

Intelligence
                                          				center tomcat connector

Reporting
                                          				engine info

Ramfs

SchedulerInfo

Expand the
                                             			 objects in RTMT to display the counters. Right click on each counter and select Counter Description for the description.

### Critical
                           	 Services

The Critical
                                 		  Services monitoring function provides the name of the critical service, the
                                 		  status (whether the service is up, down, activated, stopped by the
                                 		  administrator, starting, stopping, or in an unknown state), and the elapsed
                                 		  time during which the services are functional on the system.

Unified RTMT does not
                                             			 display a partial running status of a service in Unified CCX. For example, it
                                             			 does not display a service as "running" under "Critical Services" if some of its subsystems are down. The partial
                                             			 status of the Unified CCX services will only be viewable from the Unified
                                                				CCX Serviceability Administration web interface.

You can view and manage Cloud Connect services using Cloud Connect CLIs. For more information, see Cloud Connect section in the Command Line Interface chapter.

## Tools

Unified RTMT provides various tools to monitor and troubleshoot system issues. The following section briefly describes these
                              tools.

### Alerts

Unified CCX generates
                                 		  alert messages to notify the administrator when a predefined condition is met,
                                 		  such as when an activated service fails to start. The system sends alerts as
                                 		  email or displays alerts as a popup message on RTMT.

RTMT
                                 		  contains preconfigured and user-defined alerts that support alert
                                 		  modifications. Although you can perform configuration tasks for both types, you
                                 		  cannot delete preconfigured alerts (whereas you can add and delete user-defined
                                 		  alerts). Predefined alerts are configured for perfmon counter value thresholds
                                 		  as wells as event (alarms) notifications.

#### Syslog and Alert

Below are the set of syslog messages and alert which can be viewed from RTMT.

#### Syslog Support for Critical  Log Messages

Cisco Finesse generates syslogs for critical log messages. Use the following procedure to view the logs using Unified RTMT.

##### Before you begin

Download and install RTMT on a client computer from the following URL: https://FQDN:8443/plugins/CcmServRtmtPlugin.exe , where FQDN is the Fully Qualified Domain Name of the Finesse server.

Step 1

Log in to Unified RTMT using Finesse administrator credentials.

Step 2

In the tree hierarchy, select SysLog Viewer or choose System > Tools > SysLog Viewer > Open SysLog Viewer .

Step 3

From the Select a Node drop-down list, choose the server where the logs that you want to view are stored.

Step 4

Under the Logs tab, select Application Logs > CiscoSyslog to view and save the syslog file.

Tip

When you double-click the CiscoSyslog message, the Show Detail dialog displays the syslog definition and recommended actions in an adjacent pane.

For more information, see the Cisco Unified Real-Time Monitoring Tool Administration Guide .

System log messages generated by Cisco Finesse are also available under SysLog Viewer > System Logs > messages .

The following are the different types of messages and corresponding
                                                descriptions that are captured in the SysLog Viewer > System Logs > messages .

CTI_SOCKET_ERROR

System has encountered an error connecting to the CTI server.

CTI_CONNECTION_LOST

System has lost contact with the CTI server.

CTI_OPEN_FAILURE

CTI Server rejected open request.

CTI_CONNECTION_RETRIES_EXCEEDED

System has failed to connect to the CTI server in the allowed number of retries.

CTI_CONNECTION_ESTABLISHED

System has successfully connected to the CTI server.

SUBSYS_INIT_ERROR

Error initializing subsystem.

UNABLE_TO_CONNECT_TO_XMPP_SERVER

Unable to connect xmpp server.

DB_SS_CONNECTION_CHECK

There was an error connecting to the database.

cfservice_CORE_ERROR_DB_CONNECTION

Unable to connect to the Database.

AWDB_NOT_ACCESSIBLE

Unable to connect to AWDB server.

VOS_DB_ADAPTER_ERROR

There was an error on the VOS DB Adapter operation.

FINESSE_APP_STARTUP_ERROR

Error during Finesse Application Startup.

OF_STATE_CHANGED

OF subsystem state successfully changed.

CONNECTED_TO_XMPP_SERVER

Successfully connected to xmpp server.

SSO_API_ERROR

Error processing REST API Request for SSO.

API_ERROR_DETAIL

Error processing REST API request.

AWDB_CONNECTION_ERROR

Error while connecting the AWDB server.

AWDB_CONNECTION_SWITCH_SUCCESS

DRAPI_HOST_ALERT

Failover of Digital Routing API host-pair.

Failover isn’t supported when the Digital Routing API host backup isn’t configured.

DRAPIAsyncRestClient

Failed to create SSL connection to Digital Routing API.

#### Traces and
                              	 Logs

The trace and log
                                    		  central feature in RTMT allows you to configure on-demand trace collection for
                                    		  a specific date range or an absolute time. You can collect trace files that
                                    		  contain search criteria that you specify and save the trace collection criteria
                                    		  for later use, schedule one recurring trace collection and download the trace
                                    		  files to a SFTP or FTP server on your network, or collect a crash dump file.

After you collect
                                    		  the files, you can view them in the appropriate viewer within the RTMT. You can
                                    		  also view traces on the server without downloading the trace files by using the
                                    		  remote browse feature. You can open the trace files by either selecting the
                                    		  internal viewer that is provided with RTMT or choosing an appropriate program
                                    		  as an external viewer.

For more
                                    		  information about traces and logs, see "Tools for
                                       			 traces, logs, and plug-ins" in Cisco Unified Real-Time
                                             				  Monitoring Tool Administration Guide for Cisco Unified Contact Center Express
                                             				  and Cisco Unified IP IVR ,
                                    		  available here:

https://www.cisco.com/en/US/partner/products/sw/voicesw/ps556/prod_maintenance_guides_list.html

#### Cloud Connect Serviceability

### CUCM Telephony
                           	 Data Monitoring

Triggers

Call Control
                                          				Groups

CTI ports

To access CUCM
                                    			 Telephony Data , click Cisco
                                    			 Unified CCX tab in RTMT.

#### Triggers
                              	 Page

The
                                    		  Triggers page displays the following information for the triggers that are
                                    		  configured for Unified CCX :

Counters

Description

TriggerDN

This field
                                                					 displays the directory number that is associated with the trigger.

Trigger
                                                					 State

This field
                                                					 displays the state of the trigger, which can be In Service, Out of Service, or
                                                					 Unknown.

Application
                                                					 Name

This field
                                                					 displays the name of Unified CCX application that is
                                                					 associated with the trigger.

Ready for
                                                					 Call

This field
                                                					 indicates whether the trigger is ready to accept the call.

CallControlGroup ID

This field
                                                					 displays the ID of the call control group that is associated with the trigger.

Media Group
                                                					 ID

This field
                                                					 displays the ID of the media group that is associated with the trigger.

Last State
                                                					 Change Time

This field
                                                					 displays the time of last state change for the trigger.

This field
                                                					 provides the reason the trigger state is Out of Service or Unknown and provides
                                                					 the recommended action to return the trigger state to In Service.

#### Call Control Groups
                              	 page

The Call Control
                                    		  Groups page provides the following information about the current Call Control
                                    		  Group that is configured for Unified
                                       			 CCX :

Counters

Description

CallControlGroup ID

This field
                                                					 displays the ID that is associated with the call control group.

Group State

This field
                                                					 displays the state of the call control group, which can be In Service, Partial
                                                					 Service, or Out of Service.

Total Ports

This field
                                                					 displays the total number of CTI ports that are configured for the call control
                                                					 group.

InService
                                                					 Ports

This field
                                                					 displays the number of in-service CTI ports.

#### CTI Ports
                              	 Page

The CTI Ports page
                                    		  provides the following information about the current CTI ports that are
                                    		  configured for Unified CCX :

Counters

Description

CTI Port DN

This field
                                                					 displays the directory number of the CTI port.

CallControlGroup ID

This field
                                                					 displays the ID of call control group to which the CTI port belongs.

Port State

This field
                                                					 displays the state of CTI port, which can be In Service or Out of Service.

This field
                                                					 displays the call ID of the last call that is available on the CTI port before
                                                					 the port state changed to Out of Service.

Last State
                                                					 Change Time

This field
                                                					 displays the last time when the CTI port state changed.

#### Summary Page

The Summary page
                                    		  provides the following information:

Counters

Description

This field
                                                					 displays the state of the Unified CCX telephony
                                                					 subsystem, which can be In Service, Partial Service, or Out of Service.

Call Control
                                                					 Groups In Service

This field
                                                					 displays the number of call control groups that are in service.

Call Control
                                                					 Groups Out Of Service

This field
                                                					 displays the number of call control groups that are out of service.

In UCCX system, if we do not configure any Trigger and CTI Ports
                                                			 then CM Telephony displays Out of Service status. Similarly in IPIVR, if we do
                                                			 not configure ICM Subsystem then ICM Subsystem displays Out of Service status.

### Cisco Unified Analysis Manager

Use Cisco Unified Analysis Manager, a tool included with the Unified RTMT to perform troubleshooting operations. Unified
                                 Analysis Manager also allows you to monitor various aspects of the devices added to the tool. Unified Analysis Manager is
                                 used to collect troubleshooting information from your system  and analyze the information. It can identify the supported Unified
                                 Communications (UC) products and applications that you have in your system and troubleshoot call failures across these UC
                                 applications, collecting trace and log files and other platform and configuration information. You can use this information
                                 to troubleshoot on your own or send the information to Cisco Technical Assistance for analysis.

#### Unified Analysis
                              	 Manager for Unified CCX

To monitor and troubleshoot a Unified CCX -based solution with the help of Unified Analysis Manager, you must connect to a Unified Communications Manager server and
                                    then add the Unified CCX nodes accordingly. You can add following nodes/servers for monitoring:

Unified CCX node

Call record server

Consider the following points while adding nodes/servers for monitoring:

To add nodes/servers, ensure that you select Node Type as Unified CCX .

To add a call record server, enter uccxsct in the JDBC User Name field.

For detailed procedures to perform these actions, see "Cisco Unified Analysis Manager preferences" section in the Cisco Unified Real-Time
                                                   				  Monitoring Tool Administration Guide for Cisco Unified Contact Center Express
                                                   				  and Cisco Unified IP IVR , available here:

https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html

| Note | Expand the
                                             			 objects in RTMT to display the counters. Right click on each counter and select Counter Description for the description. |
|---|---|

| Note | Unified RTMT does not
                                             			 display a partial running status of a service in Unified CCX. For example, it
                                             			 does not display a service as "running" under "Critical Services" if some of its subsystems are down. The partial
                                             			 status of the Unified CCX services will only be viewable from the Unified
                                                				CCX Serviceability Administration web interface. |
|---|---|

| Note | You can view and manage Cloud Connect services using Cloud Connect CLIs. For more information, see Cloud Connect section in the Command Line Interface chapter. |
|---|---|

| Step 1 | Log in to Unified RTMT using Finesse administrator credentials. |
|---|---|
| Step 2 | In the tree hierarchy, select SysLog Viewer or choose System > Tools > SysLog Viewer > Open SysLog Viewer . |
| Step 3 | From the Select a Node drop-down list, choose the server where the logs that you want to view are stored. |
| Step 4 | Under the Logs tab, select Application Logs > CiscoSyslog to view and save the syslog file. Tip When you double-click the CiscoSyslog message, the Show Detail dialog displays the syslog definition and recommended actions in an adjacent pane. For more information, see the Cisco Unified Real-Time Monitoring Tool Administration Guide . Note System log messages generated by Cisco Finesse are also available under SysLog Viewer > System Logs > messages . The following are the different types of messages and corresponding
                                                descriptions that are captured in the SysLog Viewer > System Logs > messages . CTI_SOCKET_ERROR System has encountered an error connecting to the CTI server. CTI_CONNECTION_LOST System has lost contact with the CTI server. CTI_OPEN_FAILURE CTI Server rejected open request. CTI_CONNECTION_RETRIES_EXCEEDED System has failed to connect to the CTI server in the allowed number of retries. CTI_CONNECTION_ESTABLISHED System has successfully connected to the CTI server. SUBSYS_INIT_ERROR Error initializing subsystem. UNABLE_TO_CONNECT_TO_XMPP_SERVER Unable to connect xmpp server. DB_SS_CONNECTION_CHECK There was an error connecting to the database. cfservice_CORE_ERROR_DB_CONNECTION Unable to connect to the Database. AWDB_NOT_ACCESSIBLE Unable to connect to AWDB server. VOS_DB_ADAPTER_ERROR There was an error on the VOS DB Adapter operation. FINESSE_APP_STARTUP_ERROR Error during Finesse Application Startup. OF_STATE_CHANGED OF subsystem state successfully changed. CONNECTED_TO_XMPP_SERVER Successfully connected to xmpp server. SSO_API_ERROR Error processing REST API Request for SSO. API_ERROR_DETAIL Error processing REST API request. AWDB_CONNECTION_ERROR Error while connecting the AWDB server. AWDB_CONNECTION_SWITCH_SUCCESS AWDB
                                                   server connection successfully switched. DRAPI_HOST_ALERT Failover of Digital Routing API host-pair. Failover isn’t supported when the Digital Routing API host backup isn’t configured. DRAPIAsyncRestClient Failed to create SSL connection to Digital Routing API. | Tip | When you double-click the CiscoSyslog message, the Show Detail dialog displays the syslog definition and recommended actions in an adjacent pane. For more information, see the Cisco Unified Real-Time Monitoring Tool Administration Guide . | Note | System log messages generated by Cisco Finesse are also available under SysLog Viewer > System Logs > messages . |
| Tip | When you double-click the CiscoSyslog message, the Show Detail dialog displays the syslog definition and recommended actions in an adjacent pane. For more information, see the Cisco Unified Real-Time Monitoring Tool Administration Guide . |
| Note | System log messages generated by Cisco Finesse are also available under SysLog Viewer > System Logs > messages . |

| Tip | When you double-click the CiscoSyslog message, the Show Detail dialog displays the syslog definition and recommended actions in an adjacent pane. For more information, see the Cisco Unified Real-Time Monitoring Tool Administration Guide . |
|---|---|

| Note | System log messages generated by Cisco Finesse are also available under SysLog Viewer > System Logs > messages . |
|---|---|

| Counters | Description |
|---|---|
| TriggerDN | This field
                                                					 displays the directory number that is associated with the trigger. |
| Trigger
                                                					 State | This field
                                                					 displays the state of the trigger, which can be In Service, Out of Service, or
                                                					 Unknown. |
| Application
                                                					 Name | This field
                                                					 displays the name of Unified CCX application that is
                                                					 associated with the trigger. |
| Ready for
                                                					 Call | This field
                                                					 indicates whether the trigger is ready to accept the call. |
| CallControlGroup ID | This field
                                                					 displays the ID of the call control group that is associated with the trigger. |
| Media Group
                                                					 ID | This field
                                                					 displays the ID of the media group that is associated with the trigger. |
| Last State
                                                					 Change Time | This field
                                                					 displays the time of last state change for the trigger. |
| Recommended Action | This field
                                                					 provides the reason the trigger state is Out of Service or Unknown and provides
                                                					 the recommended action to return the trigger state to In Service. Note This
                                                         					 field is populated only if the trigger is in Out of Service state or Unknown
                                                         					 state. | Note | This
                                                         					 field is populated only if the trigger is in Out of Service state or Unknown
                                                         					 state. |
| Note | This
                                                         					 field is populated only if the trigger is in Out of Service state or Unknown
                                                         					 state. |

| Note | This
                                                         					 field is populated only if the trigger is in Out of Service state or Unknown
                                                         					 state. |
|---|---|

| Counters | Description |
|---|---|
| CallControlGroup ID | This field
                                                					 displays the ID that is associated with the call control group. |
| Group State | This field
                                                					 displays the state of the call control group, which can be In Service, Partial
                                                					 Service, or Out of Service. |
| Total Ports | This field
                                                					 displays the total number of CTI ports that are configured for the call control
                                                					 group. |
| InService
                                                					 Ports | This field
                                                					 displays the number of in-service CTI ports. |
| OOS Ports | This field displays the number of out-of-service CTI ports. |

| Counters | Description |
|---|---|
| CTI Port DN | This field
                                                					 displays the directory number of the CTI port. |
| CallControlGroup ID | This field
                                                					 displays the ID of call control group to which the CTI port belongs. |
| Port State | This field
                                                					 displays the state of CTI port, which can be In Service or Out of Service. |
| CallID | This field
                                                					 displays the call ID of the last call that is available on the CTI port before
                                                					 the port state changed to Out of Service. Note This
                                                            						field is populated only if the port state is Out of Service. | Note | This
                                                            						field is populated only if the port state is Out of Service. |
| Note | This
                                                            						field is populated only if the port state is Out of Service. |
| Last State
                                                					 Change Time | This field
                                                					 displays the last time when the CTI port state changed. |

| Note | This
                                                            						field is populated only if the port state is Out of Service. |
|---|---|

| Counters | Description |
|---|---|
| Overall Telephony Subsystem State | This field
                                                					 displays the state of the Unified CCX telephony
                                                					 subsystem, which can be In Service, Partial Service, or Out of Service. |
| Call Control
                                                					 Groups In Service | This field
                                                					 displays the number of call control groups that are in service. |
| Call Control
                                                					 Groups Out Of Service | This field
                                                					 displays the number of call control groups that are out of service. |
| Call Control Groups In Partial Service | This field displays the number of call control groups that are
                                             				  in partial service. |
| Enabled Triggers | This field displays the number of triggers that are associated
                                             				  with valid call control group IDs. |
| Disabled Triggers | This field displays the number of triggers that are associated
                                             				  with invalid call control group IDs. |
| Triggers With Config Errors | This field displays the number of triggers with configuration
                                             				  errors. |

| Note | In UCCX system, if we do not configure any Trigger and CTI Ports
                                                			 then CM Telephony displays Out of Service status. Similarly in IPIVR, if we do
                                                			 not configure ICM Subsystem then ICM Subsystem displays Out of Service status. |
|---|---|